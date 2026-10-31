# P-E-2020-2016287-6ed5334f

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Problem Chosen

<!-- b000002 | furniture | pages [1] -->
2020

<!-- b000003 | furniture | pages [1] -->
Team Control Number

<!-- b000004 | prose | pages [1] -->
MCM/ICM

<!-- b000005 | title | pages [1] -->
E

<!-- b000006 | furniture | pages [1] -->
2016287

<!-- b000007 | heading | pages [1] -->
Summary Sheet

<!-- b000008 | title | pages [1] -->
Global Disposable Plastic Waste Crisis

<!-- b000009 | heading | pages [1] -->
Summary

<!-- b000010 | prose | pages [1] -->
The plastic waste pollution, is posing a great threat to the global ecosystem and human health while causing global equity issues, and the rise of disposable plastics is even worsening the situation. To better understand and tackle these problems, this paper focuses on measuring disposable plastic waste’s influence, predicting its trend and give some reasonable advice.

<!-- b000011 | prose | pages [1] -->
For sake of estimating the maximum levels of disposable plastic waste that can safely be alleviated without further environmental damage, we created an Environment Bearing Rate Model (EBRM). Firstly, the relationship of disposable plastic waste and Environmental Bearing Quantity (EBQ) are given by analyzing the source and disposal of plastic waste. Secondly, we derive the interaction relationship between EBQ and Environmental Bearing Capacity (EBC) to get the Threshold Conditions for environmental self-recovery, which is EBQ equals to EBC. Finally, the maximum level of disposable plastic waste is deduced.

<!-- b000012 | prose | pages [1] -->
To discuss the extent disposable plastic waste level can be reduced to, we establish a DPWPM (Disposable Plastic Waste Prediction Model). Firstly, 11 quantifiable indicators influencing the generation and management of disposable plastic waste are selected. Then we classify the regions according to development degree, pollution level and whether it is coastal. Next, we do Principal Component Analysis with these indicators to reduce dimensionality. Finally, we use Multivariate Time Series Model to obtain the relationship between the disposable plastic waste proportion and these indicators and predict to what extent it will be reduced. To verify the model, we apply it to Ireland and the results are the disposable plastic waste rate in total waste will decrease to 0.3%, close to official statistic data. What’s more, we analyze the policy effectiveness in different regions and measure how the reduction will influence ecosystem and human health using the EBRM and Human-Friendly Indicator.

<!-- b000013 | prose | pages [1] -->
For giving a minimal achievable level of global waste of disposable plastic, we firstly use Quadratic Exponential Smoothing Model to predict total global plastic production. Then, DPWPM is used to predict the its proportion in plastic waste in different country groups. Combined with EWM (Entropy Weight Method), we get a global curve of its proportion in plastic. At last, we get the result that the minimal achievable level of global waste of disposable plastic is 15.88 million tones till 2030. Besides, we also draw a conclusion of how the target will influence human life, environmental and the plastic industry.

<!-- b000014 | prose | pages [1] -->
The unfair problems of the global plastic waste crisis are mainly reflected in the uneven distribution of plastic waste production and pollution and the different economic investment in the disposal of plastic waste of different countries. We propose four intended solutions including allocating Permits for the plastic waste and clarification of inter-state property rights.

<!-- b000015 | prose | pages [1] -->
Finally, we use Rotation Estimation and Gaussian noise to test the robustness for the models and write a memo to the ICM about the minimal achievable level of global plastic waste.

<!-- b000016 | keywords | pages [1] -->
Keywords: Disposable Plastic, Multivariate Time Series, EWM, PCA

<!-- b000017 | prose | pages [1] -->
关注数学模型

<!-- b000018 | furniture | pages [1] -->
2

<!-- b000019 | furniture | pages [1] -->
MATHmodels

<!-- b000020 | furniture | pages [1] -->
获取更多资讯

<!-- b000021 | furniture | pages [2] -->
Team # 2016287                                                                                                                                Page  1  of  21

<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
1. Introduction ............................................................................................................................ 2

<!-- b000024 | contents | pages [2] -->
1.1 Background .................................................................................................................. 2

<!-- b000025 | contents | pages [2] -->
1.2 Restatement of Problem ............................................................................................... 2

<!-- b000026 | contents | pages [2] -->
1.3 Overview of Our Work ................................................................................................ 2

<!-- b000027 | contents | pages [2] -->
2. Assumptions and Justifications .............................................................................................. 3

<!-- b000028 | contents | pages [2] -->
3. Notations ................................................................................................................................ 3

<!-- b000029 | contents | pages [2] -->
4. Maximum Levels of Disposable Plastic Waste ..................................................................... 3

<!-- b000030 | contents | pages [2] -->
4.1 Source of the waste ...................................................................................................... 3

<!-- b000031 | contents | pages [2] -->
4.2 Waste Management ...................................................................................................... 4

<!-- b000032 | contents | pages [2] -->
4.2.1 Recycling .......................................................................................................... 4

<!-- b000033 | contents | pages [2] -->
4.2.2 Incineration ....................................................................................................... 4

<!-- b000034 | contents | pages [2] -->
4.2.3 Landfill .............................................................................................................. 4

<!-- b000035 | contents | pages [2] -->
4.2.4 Uncontrolled Deposit in Ocean ......................................................................... 5

<!-- b000036 | contents | pages [2] -->
4.3

<!-- b000037 | contents | pages [2] -->
Environmental Bearing Rate Model ......................................................................... 5

<!-- b000038 | contents | pages [2] -->
4.3.1 Environmental Bearing Rate ............................................................................. 6

<!-- b000039 | contents | pages [2] -->
4.3.2 Environmental Bearing Quantity Measurement ............................................... 7

<!-- b000040 | contents | pages [2] -->
4.3.3 Environmental Bearing Capacity Measurement ............................................... 8

<!-- b000041 | contents | pages [2] -->
4.4

<!-- b000042 | contents | pages [2] -->
Maximum Levels of Disposable Plastic Product Waste .......................................... 8

<!-- b000043 | contents | pages [2] -->
4.4.1 Current Waste Quantity and Capacity .............................................................. 8

<!-- b000044 | contents | pages [2] -->
5. Reduction of Plastic Waste and the Environmentally Safe Level after Reduction ................ 8

<!-- b000045 | contents | pages [2] -->
5.1 Factors Influencing Plastic Waste Reduction .............................................................. 9

<!-- b000046 | contents | pages [2] -->
5.1.1 Factors in the Waste Production of Disposable Plastic .................................... 9

<!-- b000047 | contents | pages [2] -->
5.1.2 Factors in the Waste Management of Disposable Plastic ............................... 11

<!-- b000048 | contents | pages [2] -->
5.2 Classification of the Country ..................................................................................... 12

<!-- b000049 | contents | pages [2] -->
5.3 Disposable Plastic Waste Prediction Model .............................................................. 13

<!-- b000050 | contents | pages [2] -->
5.3.1 Principal Component Analysis of Influencing Indicators ............................... 13

<!-- b000051 | contents | pages [2] -->
5.3.2 Multivariate Time Series Analysis with Principal Component ...................... 14

<!-- b000052 | contents | pages [2] -->
5.3.3 Model Application .......................................................................................... 14

<!-- b000053 | contents | pages [2] -->
5.4 Environmentally Safe Level ...................................................................................... 15

<!-- b000054 | contents | pages [2] -->
5.4.1 Environmental Bearing Rate after Reduction of Plastic Waste ...................... 16

<!-- b000055 | contents | pages [2] -->
5.4.2 Human-friendly Indicator ............................................................................... 16

<!-- b000056 | contents | pages [2] -->
6. Targets and Impacts for Achieving the Minimal Achievable Level of Global Waste ......... 16

<!-- b000057 | contents | pages [2] -->
6.1 Targets for Minimal Achievable Level of Global Waste ........................................... 17

<!-- b000058 | contents | pages [2] -->
6.1.1 Prediction of Global Plastics Production ........................................................ 17

<!-- b000059 | contents | pages [2] -->
6.1.2 Prediction of Disposable Plastic Waste Proportion ........................................ 17

<!-- b000060 | contents | pages [2] -->
6.1.3 Result of Achievable Level of Disposable Plastic Waste ............................... 18

<!-- b000061 | contents | pages [2] -->
6.2 Impacts for Achieving the Minimal Achievable Level of Global Waste .................. 18

<!-- b000062 | contents | pages [2] -->
6.2.1 Impacts on Human Life .................................................................................. 19

<!-- b000063 | contents | pages [2] -->
6.2.2 Impacts on the Environment ........................................................................... 19

<!-- b000064 | contents | pages [2] -->
6.2.3 Impacts on the Plastic Industry ....................................................................... 19

<!-- b000065 | contents | pages [2] -->
7. Equity Issues and Solutions ................................................................................................. 19

<!-- b000066 | contents | pages [2] -->
7.1 Equity Issues .............................................................................................................. 20

<!-- b000067 | contents | pages [2] -->
7.2 Solutions to Equity Issues .......................................................................................... 20

<!-- b000068 | contents | pages [2] -->
8. Sensitivity Analysis ............................................................................................................. 20

<!-- b000069 | contents | pages [2] -->
8.1 Rotation Estimation for Multivariate Time Series Model ......................................... 20

<!-- b000070 | contents | pages [2] -->
8.2

<!-- b000071 | contents | pages [2] -->
Gaussian Noise ....................................................................................................... 21

<!-- b000072 | contents | pages [2] -->
9. Evaluation of the Model....................................................................................................... 21

<!-- b000073 | contents | pages [2] -->
9.1 Strength ...................................................................................................................... 21

<!-- b000074 | contents | pages [2] -->
9.2 Weakness ................................................................................................................... 21

<!-- b000075 | contents | pages [2] -->
关注数学模型

<!-- b000076 | furniture | pages [2] -->
2

<!-- b000077 | furniture | pages [2] -->
MATHmodels

<!-- b000078 | furniture | pages [2] -->
获取更多资讯

<!-- b000079 | furniture | pages [3] -->
Team # 2016287                                                                                                                                Page  2  of  21

<!-- b000080 | heading | pages [3] -->
1. Introduction

<!-- b000081 | heading | pages [3] -->
1.1 Background

<!-- b000082 | prose | pages [3] -->
Single-use plastics products, referred to as items intended to be used only once before thrown away, are almost everywhere in our life, including grocery bags, food packaging, bottles, straws, containers, cups, cutlery, etc.[2] However, with the large-scale production of single-use plastic products, the white pollution caused by them is severe nowadays. According to a UNEP report[2], single-use plastics take most of the spots in the Top Ten most common finds during international coastal cleanups. What’s worse, poor waste management systems will exacerbate the extent of pollution. At present, several methods are used to dispose them, including incineration, dump, recycling, landfill and discard in the natural environment[1].

<!-- b000083 | prose | pages [3] -->
Since the plastic waste take even several hundred year to break down, it is posing a great threat to the ecosystem and human health[2].Especially, Marine ecosystems are being hit hard as most plastic waste flows into the ocean. Effects can be seen by the approximately 4-12 million tons of plastic waste that enter the oceans each year[1]. The economic damage caused by plastic waste is vast. Plastic litter in the Asia-Pacific region alone costs its tourism, fishing and shipping industries $1.3 billion per year[3].

<!-- b000084 | prose | pages [3] -->
Recently years, many governments has taken positive interventions to tackle this problem, mainly by improving waste management practices, introduce financial incentives, financing more research and development of alternative materials, raising awareness among consumers and so on[3]. However, there are little research about the prediction of disposable plastic waste.

<!-- b000085 | heading | pages [3] -->
1.2 Restatement of Problem

<!-- b000086 | prose | pages [3] -->
In order to solve the plastic waste problem, we need to formulate a plan to reduce or even eliminate disposable plastic products by slowing down plastic production and improving waste utilization. Considering that plastics is mostly single-use, we focus particularly on disposable Plastic Products.

<!-- b000087 | prose | pages [3] -->
What we need to do is as follows:

<!-- b000088 | prose | pages [3] -->
⚫ Establish a model to estimate the maximum level of disposable plastic product waste Under the premise that waste can safely be mitigated without further environmental pollution.

<!-- b000089 | prose | pages [3] -->
⚫ Research how much plastic waste can be reduced to reach an environmentally safe level.

<!-- b000090 | prose | pages [3] -->
⚫ Based on the above research, set a goal for minimal achievable level of disposable plastic waste globally and explore the impact on many aspects of reaching that goal.

<!-- b000091 | prose | pages [3] -->
⚫ Considering that the causes and consequences of disposable plastic problems vary from place to place, discuss related equity issues and propose solutions.

<!-- b000092 | heading | pages [3] -->
1.3 Overview of Our Work

<!-- b000093 | prose | pages [3] -->
We have established a model to determine the maximum level of the disposable plastic waste using the theory of environment bearing rate. Moreover, a model for predicting the extent the level of the disposable plastic waste can be reduced to according to many influence factors and historic data. Using the two models, we evaluate the effectiveness of different policies in different kinds of regions and give a reasonable minimum targeted achievable level for the global disposable plastic waste and advocates some solutions to solve the equality issues caused by the global plastic waste crisis. The whole modeling process are shown in Fig 1.

<!-- b000094 | prose | pages [3] -->
关注数学模型

<!-- b000095 | furniture | pages [3] -->
2

<!-- b000096 | furniture | pages [3] -->
MATHmodels

<!-- b000097 | furniture | pages [3] -->
获取更多资讯

<!-- b000098 | furniture | pages [4] -->
Team # 2016287                                                                                                                                Page  3  of  21

<!-- b000099 | caption | pages [4] -->
Figure 1: whole modeling process of the paper

<!-- b000100 | heading | pages [4] -->
2. Assumptions and Justifications

<!-- b000101 | prose | pages [4] -->
To simplify the cost benefit analysis model, this paper makes following basic assumption, each of which is properly justified.

<!-- b000102 | prose | pages [4] -->
⚫ We assume that the increase in Environmental Bearing Capacity can be ignored because the evolution of the ecosystem is a long-time process.

<!-- b000103 | prose | pages [4] -->
⚫ Sudden change in the environment can be ignored, because of its rareness.

<!-- b000104 | prose | pages [4] -->
⚫ We assume that all the regions will react positively to the worsening problems of dis posable plastic waste and take suitable measures to improve it. This assumption is m ade according to reactions of most countries.

<!-- b000105 | heading | pages [4] -->
3. Notations

<!-- b000106 | prose | pages [4] -->
We list the symbols and notations used in this paper in Table 1.

<!-- b000107 | caption | pages [4] -->
Table 1: Symbols and Definitions

<!-- b000108 | prose | pages [4] -->
Symbols          Meanings                                                                                         Unit C t          Environmental Bearing Capacity in year t                                             -- ( ) Q t          Environmental Bearing Quantity in year t                                             -- ( ) EBR           Environmental Bearing Rate                                                                  -- HFI           Human-friendly Indicator                                                                       --

<!-- b000109 | heading | pages [4] -->
4. Maximum Levels of Disposable Plastic Waste

<!-- b000110 | prose | pages [4] -->
If the amount pollution caused by the plastic waste is within the controllable range, it won’t cause damage to the environment. However, when the single-use plastic product waste reaches a certain level, it will exceed the environment's own ability to repair, making the environment worse and difficult to recover. Therefore, we hope to develop a model to estimate the maximum levels of single-use or disposable plastic product waste that can safely be mitigated without further environmental damage.

<!-- b000111 | heading | pages [4] -->
4.1 Source of the waste

<!-- b000112 | prose | pages [4] -->
In most situation, single-use plastics are used for packaging, such as shopping bags, wrappers and bottles. After the use of these products, they will be discarded and become plastics waste. Among these wastes, as stated in the UNEP report[2], plastic bags and foamed plastic products are perceived as the most problematic source of the plastic wastes. It is because single-use plastic bags are the most common disposable plastic products in life to hold items[1]. And as for foamed plastics, its lightness, strength and thermal insulation make it great for disposable tableware such as lunch boxes. In china, with the rise of the takeaway industry, the use of foam has increased uncontrollably[1].

<!-- b000113 | prose | pages [4, 5] -->
关注数学模型 To simplify our model, only two sources of the waste mentioned above is considered.

<!-- b000114 | furniture | pages [4] -->
2

<!-- b000115 | furniture | pages [4] -->
MATHmodels

<!-- b000116 | furniture | pages [4] -->
获取更多资讯

<!-- b000117 | furniture | pages [5] -->
Team # 2016287                                                                                                                                Page  4  of  21

<!-- b000119 | prose | pages [5] -->
fP are introduced to represent the annual production of plastic bags and foamed bP and Also, plastic products respectively.

<!-- b000120 | heading | pages [5] -->
4.2 Waste Management

<!-- b000121 | prose | pages [5] -->
The current consumption of plastic waste is large, which makes it more important to manage their end-of-life in an environment-friendly way. Scientifically speaking, “energy recovery processes are preferable to landfilling or improper forms of disposal[2]”. To show this more clearly, a waste management hierarchy, reflecting the degree of impact on the environment during different process of plastic wastes is shown in Fig. 2.

<!-- b000122 | caption | pages [5] -->
Figure 2: Different ways to deal with plastic waste and the degree of impact on the environment.

<!-- b000123 | prose | pages [5] -->
For each level of the waste management hierarchy: Recycling is quite environment- friendly because it decrease the production of disposable plastics. Landfill has a bad impact on the environment because it takes thousands of years for plastics to decompose. Incineration harms the environment due to the toxic gas in the burning process of plastics. Uncontrolled deposit in places like ocean is extremely detrimental to the environment owing to its harm to marine wildlife.

<!-- b000124 | prose | pages [5] -->
Thus, we mainly focus on four of them. They are recycling, incineration, landfill and uncontrolled deposit in ocean.

<!-- b000125 | heading | pages [5] -->
4.2.1 Recycling

<!-- b000126 | prose | pages [5] -->
Some disposable plastic products, usually made of thermoplastic materials, can be recycled through factory processing. In this way, not only the consumption of resources is reduced, but also the plastic waste does, thereby greatly reducing environmental pollution.

<!-- b000127 | prose | pages [5] -->
To measure the availability of the resources to recycle the waste, the percentage of plastic waste recycled rp t is introduced. The larger the value of ( ) rp t is, the more available the ( ) recycling resources are.

<!-- b000128 | heading | pages [5] -->
4.2.2 Incineration

<!-- b000129 | prose | pages [5] -->
Although the plastic waste can be decomposed through incineration, large amount of exhaust gas released will damage the atmosphere and have a negative impact on the environment To measure the availability of the resources to incinerate the waste, the percentage of ip t is introduced. The larger the value of ( ) ip t is, the more ( ) plastic waste incinerated available the incineration resources are.

<!-- b000130 | heading | pages [5] -->
4.2.3 Landfill

<!-- b000131 | prose | pages [5] -->
Landfill means to bury the plastic waste in soil. It’s widely used in China because of low cost and good sanitation. However, chemical substances decomposed will also harm the soil.

<!-- b000132 | prose | pages [5, 6] -->
关注数学模型 To measure the availability of the resources to landfill the waste, the percentage of plastic waste landfilled lp t is introduced. The larger the value of lp t is, the more available the ( ) ( ) landfill resources are.

<!-- b000133 | furniture | pages [5] -->
2

<!-- b000134 | furniture | pages [5] -->
MATHmodels

<!-- b000135 | furniture | pages [5] -->
获取更多资讯

<!-- b000136 | furniture | pages [6] -->
Team # 2016287                                                                                                                                Page  5  of  21

<!-- b000138 | heading | pages [6] -->
4.2.4 Uncontrolled Deposit in Ocean

<!-- b000139 | prose | pages [6] -->
Every year, there is a large amount of plastic product waste entering the ocean in various ways. And scientists estimate that the amount of plastic into the ocean is up to 4.8–12.7 million metric tons in 2010[3].

<!-- b000140 | prose | pages [6] -->
During weathering and biological processes, plastic wastes into the ocean will gradually turn into plastic debris, which is easy to be ingested by marine wildlife. This is extremely harmful to marine ecology. Also, there is large plastics, which can interfere the navigation of ships. And the toxic chemicals in plastics will also pollute seawater, putting marine life at risk of being poisoned To measure the availability of the resources to deposit the waste in ocean uncontrollably, the percentage of plastic waste deposited into the ocean op t is introduced. The larger the ( ) value of op t is, the more plastic waste is deposited into the ocean. ( )

<!-- b000141 | heading | pages [6] -->
4.3 Environmental Bearing Rate Model

<!-- b000142 | prose | pages [6] -->
As we all know, ecosystems are capable of self-regulating. When they suffer certain damage, such as environmental pollution and reduction in the number of species, as long as these impacts do not exceed the threshold for ecosystem self-regulation, the environment can self-recover within a certain period of time.

<!-- b000143 | prose | pages [6] -->
Ecologically, terms like Environmental Bearing Capacity (EBC) and Environmental Bearing Quantity (EBQ) are applied to descript the process above.

<!-- b000144 | prose | pages [6] -->
When the plastic waste related EBQ is smaller than EBC, the single-use plastic product waste that can safely be mitigated without further environmental damage. The definition and property of EBC and EBQ are as follows:

<!-- b000145 | prose | pages [6] -->
⚫ Environmental Bearing Quantity (EBQ). This refers to the impacts that human activities make to the environment in a period. For example, human activities such as emitting the exhaust, discharging the plastic waste into the ocean will cause damage to the natural environment. The harmful influence includes but is not limited to the increase of the exhaust, the reduction in species, etc. All of these impacts to nature in a period belong to EBQ. And this can be measured by some metrics described in Section 5.3.2.

<!-- b000146 | prose | pages [6] -->
⚫ Environmental Bearing Capacity (EBC). This refers to the maximum impacts that human activities make to the environment, otherwise the environment will suffer irreversible damage. In other words, EBC is the threshold of EBQ. For example, when the amount of exhaust emitted exceeds what the environment can afford, the ecosystem is damaged.

<!-- b000147 | prose | pages [6] -->
There are 2 cases of the relationship between EBQ and EBC. When EBQ is less than EBC,  0 that is, the difference between them , the EBC won’t change in the near future because  0 of the ecological stability. However, when EBQ is more than EBC, that is, , the EBC will f  ( ) decrease in the near future because of the irreversible damage, with the damage rate resembling the Sigmoid function. Thus, we have + = −   C t ( 1) C t ( )[1 f ( )] (1) = − C t ( ) Q t ( )  where C t and Q t represents the amount of EBC and EBQ in year t respectively, the ( ) ( ) f  is presented below. expression of ( )  1  , 0  = e−+ + (2) f ( ) 5  1   0,

<!-- b000148 | furniture | pages [6] -->
0

<!-- b000149 | prose | pages [6, 7] -->
 关注数学模型 f   is shown in Fig.3. And the figure of ( )

<!-- b000150 | furniture | pages [6] -->
2

<!-- b000151 | furniture | pages [6] -->
MATHmodels

<!-- b000152 | furniture | pages [6] -->
获取更多资讯

<!-- b000153 | furniture | pages [7] -->
Team # 2016287                                                                                                                                Page  6  of  21

<!-- b000155 | prose | pages [7] -->
f  ( )

<!-- b000156 | caption | pages [7] -->
Figure 3: The shape of

<!-- b000157 | heading | pages [7] -->
4.3.1 Environmental Bearing Rate

<!-- b000158 | prose | pages [7] -->
Considering that the relationship between EBC an EBQ can serve as a criterion to EBR judge whether the ecosystem is damaged, Environmental Bearing Rate (EBR) is introduced to simplify the analysis.

<!-- b000159 | prose | pages [7] -->
The EBR is defined as the ratio of EBQ and EBC, which is shown as Eq.3.

<!-- b000160 | prose | pages [7] -->
EBQ = EBR (3) EBC As Section 5.3.2 will mention, EBC and EBQ can be divided into several categories such as water, atmosphere and soil. Thus, the overall EBR is the weighted sum of the ratio, which can be expressed as Eq.4.

<!-- b000161 | prose | pages [7] -->
n EBQ  =  i EBR W (4) i EBC = i 1 i W , EBQ ,and EBC represent the weight, the value of EBQ and the value o where i i i − EBC of the i category respectively. th EBR 1 When : This refers to the situation that EBQ is far more less than EBC. ▪ The ecosystem won’ be damaged, so the EBC won’t change either. The relationship between EBQ and time t at this situation is showed in Fig.4.

<!-- b000162 | prose | pages [7] -->
EBR  : This refers to the situation that EBQ is less than EBC. The 1 When ▪ ecosystem will be slightly damaged, so the EBC will fluctuate but also can be back to normal. The relationship between EBQ and time t at this situation is showed in

<!-- b000163 | caption | pages [7] -->
Fig.4.

<!-- b000164 | prose | pages [7] -->
EBR  : This refers to the situation that EBQ is larger than EBC. The 1 When ▪ ecosystem will be damaged, so the EBC will decline continuously. Then, although people may take actions to decrease the pollution, as the drop of EBC, the value of EBR is still more than 1, and this will create a vicious circle. The relationship among EBQ, EBC and time t at this situation is showed in Fig.4.

<!-- b000165 | caption | pages [7] -->
Figure 4: The relationship among EBQ, EBC and time t when EBR is different

<!-- b000166 | prose | pages [7] -->
To sum up, to safely mitigate the plastic waste without further environmental damage, the value of EBR must be controlled under 1. And the maximum levels of plastic waste refers to the situation when EBR equals 1.

<!-- b000167 | prose | pages [7] -->
关注数学模型

<!-- b000168 | furniture | pages [7] -->
2

<!-- b000169 | furniture | pages [7] -->
MATHmodels

<!-- b000170 | furniture | pages [7] -->
获取更多资讯

<!-- b000171 | furniture | pages [8] -->
Team # 2016287                                                                                                                                Page  7  of  21

<!-- b000172 | heading | pages [8] -->
4.3.2 Environmental Bearing Quantity Measurement

<!-- b000173 | prose | pages [8] -->
Based on the analysis in Section 5.2, we develop some EBQ metrics according to the ways to process the plastic waste, in order to measure the impacts that processing the waste makes to the environment.

<!-- b000174 | prose | pages [8] -->
To embrace a more detailed description of the measurements of EBQ, pay attention to

<!-- b000175 | caption | pages [8] -->
Fig.5.

<!-- b000176 | caption | pages [8] -->
Figure 5: Measurements of EBQ

<!-- b000177 | prose | pages [8] -->
Water Bearing Quantity(WBQ). It refers to the amount of plastic marine debris in a ⚫ period. Study shows that the plastic contamination is threatening marine wildlife[5]. It is estimated by UNEP that marine litter harms over 600 marine species and about 15% of species affected by ingestion & entanglement from marine litter are endangered. And the plastic marine debris is produced by the plastic waste which is discharged into the ocean[5],cf. Eq.5.

<!-- b000178 | prose | pages [8] -->
=  + WBQ p ( P P ) (5) o b f fP bP and op t refers to the percentage of plastic waste deposited into the ocean, ( ) where represent the annual production of plastic bags and foamed plastic products respectively.

<!-- b000179 | prose | pages [8] -->
⚫ Atmosphere Bearing Quantity(ABQ). It refers to the amount of dioxin and benzene ring compounds produced by burning the plastic waste in a period. The main compound of plastic products is PVC(polyvinyl chloride). The chemical equation in the process can be expressed as Eq.6.

<!-- b000180 | prose | pages [8] -->
5 ( ) → + +  CH CHCl + n O 2n CO n H O n HCl (6) 2 2 2 2 n 2 During combustion, the polyvinyl chloride will also release highly toxic gas such dioxin and benzene ring compound, which can damage the immune system of animal, interfere with hormones and also cause cancer[6]. What’ more, dioxin and benzene ring compound are produced by the plastic waste which is incinerated, cf. Eq.7.

<!-- b000181 | prose | pages [8] -->
= +   + ABQ ( q q ) p ( P P ) (7) d b i b f dq and bq refer to the amount of dioxin and benzene ring compounds produced in where ip represents the percentage of plastic waste incinerated. the incineration of plastics, ⚫ Soil Bearing Quantity(SBQ). It refers to the amount of Phthalate and Bisphenol A produced by the decomposition of plastic waste in landfill in a period. When plastic particles break down, additives like phthalates and bisphenol A (BPA) will leach, which will disrupt the hormone systems of animals[7]. Moreover, phthalate and bisphenol A are produced by the plastic waste which is landfilled, cf. Eq.8.

<!-- b000182 | prose | pages [8, 9] -->
= +   + SBQ ( q q ) p ( P P ) (8) p a l b f 关注数学模型 q and aq refer to the amount of phthalate and bisphenol A produced in the landfill where p lp represents the percentage of plastic waste landfilled. of plastics,

<!-- b000183 | furniture | pages [8] -->
2

<!-- b000184 | furniture | pages [8] -->
MATHmodels

<!-- b000185 | furniture | pages [8] -->
获取更多资讯

<!-- b000186 | furniture | pages [9] -->
Team # 2016287                                                                                                                                Page  8  of  21

<!-- b000188 | heading | pages [9] -->
4.3.3 Environmental Bearing Capacity Measurement

<!-- b000189 | prose | pages [9] -->
Based on the calculation of ecosystem’s ability to self-recovery, we determine the value of EBC corresponding with the measurement in Section .3.3 ⚫ Water Bearing Capacity (WBC). It refers to the amount of plastic marine debris that people can salvage from the ocean in a period. Considering that the marine wildlife can’t digest and decompose plastic waste, we assume that any amount of plastic marine debris over WBC will damage the ecosystem.

<!-- b000190 | prose | pages [9] -->
Atmosphere Bearing Capacity (ABC). It refers to the amount of dioxin and benzene ⚫ ring compounds that the microorganism can decompose in a period. Research shows that some enzymes existing in the fungus and bacterial are effective in decomposing these toxic gas[8]. Although there may be other ways to decompose them in the environment, we only consider microorganism to simply our model. Thus, we assume that any amount of dioxin and benzene ring compounds over ABC will damage the ecosystem. ⚫ Soil Bearing Capacity (SBC). It refers to the amount of Phthalate and Bisphenol A that the microorganism can decompose in a period. It is similar to what is going on in the description above. And we assume that any amount of dioxin and benzene ring compounds over SBC will damage the ecosystem.

<!-- b000191 | heading | pages [9] -->
4.4 Maximum Levels of Disposable Plastic Product Waste

<!-- b000192 | heading | pages [9] -->
4.4.1 Current Waste Quantity and Capacity

<!-- b000193 | prose | pages [9] -->
Considering that the waste situation is accumulating with time, the total waste in the future definitely equals what the waste currently adding the waste that will increase in a period. Therefore, to better reflect the cumulative nature of waste, Current Waste Quantity (CWQ) and Current Waste Capacity(CWC) are introduced. The calculation of CWQ and CWC be analogized to equations in Section 4.3.2 and Section 4.3.3, with the only difference that the value in the above equations is not what will be in the future, but what is at present. Meanwhile, we can modify our previous equation, Eq.9, to the following format:

<!-- b000194 | prose | pages [9] -->
+ n EBQ CWQ  =  i i (9) EBR W i + EBC CWC = i 1 i i where i (i=1,2,3)represents the measurement in water, atmosphere, or soil, In order to have a specific view of the relationship between the amount of plastic waste and EBR, pay attention to Eq.10.

<!-- b000195 | prose | pages [9] -->
+ 3 EBQ CWQ  =  i i EBR W (10) i + EBC CWC = i 1 i i When EBR equals 1, we can get the maximum levels of single-use plastic products that can be safely reduced without further environmental damage.

<!-- b000196 | heading | pages [9] -->
5. Reduction of Plastic Waste and the Environmentally Safe

<!-- b000197 | prose | pages [9] -->
Level after Reduction Research shows that plastic waste is exerting great pressure on both ecological environment and human health, among which disposable waste makes the problem even more [2][9]. Given the time constraints, we mainly focus on the single-use plastics. Meanwhile, serious people have made great efforts to limit the production and consumption of disposable plastics nowadays, such as introducing related laws and alternatives. However, the amount of disposable plastic that can be reduced after these trials still remains a question, along with the impact on the environment and human beings.

<!-- b000198 | prose | pages [9] -->
关注数学模型

<!-- b000199 | furniture | pages [9] -->
2

<!-- b000200 | furniture | pages [9] -->
MATHmodels

<!-- b000201 | furniture | pages [9] -->
获取更多资讯

<!-- b000202 | furniture | pages [10] -->
Team # 2016287                                                                                                                                Page  9  of  21

<!-- b000203 | heading | pages [10] -->
5.1 Factors Influencing Plastic Waste Reduction

<!-- b000204 | prose | pages [10] -->
In recent decades, due to the improvement of people's environmental protection awareness and the promotion of the government legislation, the level of disposable plastic waste shows a decreasing trend. How much disposable waste can be reduced, however, remains a complex question, which is closely related to factors like policy, market, etc.

<!-- b000205 | prose | pages [10] -->
According to their roles in plastic waste reduction, influencing factors are divided into two categories: waste production and waste management. Specifically speaking, factors in waste production affect the amount of disposable plastic produced and entering the market; while factors in waste management affect the amount of pollution in plastic waste disposal.

<!-- b000206 | prose | pages [10] -->
What’s more, according to the survey[15], if the policy is effective, the reduction of single- use plastic waste will decreases significantly in the short term, after that, the reduction trend may also rebound.

<!-- b000207 | heading | pages [10] -->
5.1.1 Factors in the Waste Production of Disposable Plastic

<!-- b000208 | prose | pages [10] -->
In this section, factors about waste production will be introduced, including the effectiveness of local policies like bans or taxes, alternatives to plastics, citizen’s environmental protection awareness, supply and demand relationship in the single-use plastic market, etc. What’s more, it is worth noting that most conditions such as demand, policies and even the effectiveness of policies may vary from the degree of local development, geographical conditions and some other regional-specific restraints. ⚫ Ban Policy Ban policy, usually targeted at the production, import, marketing and distribution of non- biodegradable plastic bags, is the most effective way to decrease the plastic waste[2]. Unfortunately, not all countries are suitable for this approach. Take Rwanda and China as examples. After Rwanda implemented its ban policy, although the smuggling of plastics occurred in the beginning, plastic waste decreased significantly in the long run. However, China did so in 1999 and few effects taken on disposable plastic waste. Impact of national bans (based on more than 60 countries experience)[2] shows that the influence of ban policy varies greatly from country to country. That is to say, some countries are suitable for controlling disposable plastic waste through bans, but others are not. And the detailed discussion will be 1x cf. Table 2. presented in Section 4.2. Here we introduce a 0-1 variable

<!-- b000209 | caption | pages [10] -->
Table 2: Selected indictors in terms of ban policy

<!-- b000210 | prose | pages [10] -->
Indicators Brief explanation x = 0 When , the country is unsuitable for ban policy 1 1x x = , the country is suitable for ban policy 1 When 1 ⚫ Alternatives Alternatives to plastics, serving as an environmental friendly replacement, are correlated with the price and quantity demanded of the target goods[10]. They include materials like paper and cloth. Although they can’t perfectly replace plastics due to their higher manufacturing costs and inconvenience in some cases, they will still play a positive role in promoting the reduction of disposable plastics under the appropriate policy guidance.

<!-- b000211 | prose | pages [10] -->
Economically, Cross-Price Elasticity of Demand is used to describe the competitive process[11],cf. Eq.11.

<!-- b000212 | prose | pages [10] -->
 Q / Q =  a a E (11) ab P / P b b where 𝐸𝑎𝑏 represents the cross-price elasticity of demand, 𝑄𝑎 refers to the demand change for product 𝑎 and 𝑃𝑏 refers to the price of product 𝑏. Therefore, the supply and demand diagram is shown as follows.

<!-- b000213 | prose | pages [10, 11] -->
关注数学模型 The Q-P curve

<!-- b000214 | furniture | pages [10] -->
2

<!-- b000215 | furniture | pages [10] -->
MATHmodels

<!-- b000216 | furniture | pages [10] -->
获取更多资讯

<!-- b000217 | furniture | pages [11] -->
Team # 2016287                                                                                                                                Page  10  of  21

<!-- b000219 | prose | pages [11] -->
Qy

<!-- b000220 | prose | pages [11] -->
Px

<!-- b000221 | caption | pages [11] -->
Figure 6: Q-P curve of the disposable plastic product and its substitute goods

<!-- b000222 | prose | pages [11] -->
Obviously, the demand for single-use plastic products will decrease with the fall of the price of alternatives. To quantify the competitiveness of alternatives in a region, the financial investment by government will also be considered.

<!-- b000223 | prose | pages [11] -->
To sum up, two indicators are selected to measure the competitiveness of alternatives, cf.

<!-- b000224 | caption | pages [11] -->
Table 3.

<!-- b000225 | caption | pages [11] -->
Table 3: Selected indictors in terms of alternatives

<!-- b000226 | prose | pages [11] -->
Indicators Brief explanation Price of Alternatives to Disposable Plastic Products 2x Financial Investment by Government in Alternative Industries 3x ⚫ Environmental Protection Awareness Environmental protection awareness plays an important role in the effectiveness of policies and consuming behaviors in plastics. Study shows that general environmental awareness of citizens may be influenced by the education level received, level of government advocacy, efforts made by social welfare organizations, etc[12]. Considering the uncertainty of other factors, only the first two factors are discussed here. They are the average education level of citizens and the government’s advocation rate on environmental protection.

<!-- b000227 | prose | pages [11] -->
Average education level of citizens counts because there are environmental education courses carried out in universities, colleges, and elementary schools, which will effectively improve citizens' awareness of ecology and environment protection[12]. Also, government’s advocation rate on environmental protection is important because if the government is committed to popularizing the environmental protection knowledge and guiding citizens to ecological consumption[12], it will be easier for people to be environmentally awareness.

<!-- b000228 | prose | pages [11] -->
To sum up, two indicators are selected to measure the level of the environmental protection awareness, cf. Table 4.

<!-- b000229 | caption | pages [11] -->
Table 4: Selected indictors in terms of environmental awareness

<!-- b000230 | prose | pages [11] -->
Indicators Brief explanation Average Education Level of Citizens 4x Government’s Advocation Rate on Environmental Protection 5x ⚫ Tax Policy Tax policy is the most common-used economic incentive[13] to address waste. Up tp June 2019, over 60 countries in the world have taken distinct steps in the form of bans and taxes on single-use plastic products to decrease the plastic waste[14]. Nowadays, there are many kinds of tax system and charges, which vary from region to region. In general, three kinds of tax system are considered. They are production tax, landfill tax and carrier bag charge[13].

<!-- b000231 | prose | pages [11] -->
Production tax is targeted at the manufacturing level and tax on the factories whose amount of plastic products produced exceeds the regulation value. Landfill tax is concentrated on the waste management level and tax on the amount of factories who landfilled plastic waste. Carrier bag charge is focused on the consumption level and tax on single-use plastic packaging.

<!-- b000232 | prose | pages [11] -->
From an economic point of view, we take the effect of the carrier bag charge as an example. We assume that when there is no plastic bags charge, people will use a disposable plastic bag as long as they buy one item.

<!-- b000233 | prose | pages [11, 12] -->
关注数学模型 Figure 7：The relationship between the amount of single-use plastic bags and items sold.

<!-- b000234 | furniture | pages [11] -->
2

<!-- b000235 | furniture | pages [11] -->
MATHmodels

<!-- b000236 | furniture | pages [11] -->
获取更多资讯

<!-- b000237 | furniture | pages [12] -->
Team # 2016287                                                                                                                                Page  11  of  21

<!-- b000239 | prose | pages [12] -->
Q represents volume of single-use plastic bags, Q represents sales volume of where 1 2 items of the supermarket.

<!-- b000240 | prose | pages [12] -->
When there is plastic bags charge, people may reuse the bags so that the number of plastic bags will decrease.

<!-- b000241 | prose | pages [12] -->
To sum up, three indicators are selected to measure the tax policy, cf. Table 5.

<!-- b000242 | caption | pages [12] -->
Table 5: Selected indictors in terms of tax policy

<!-- b000243 | prose | pages [12] -->
Indicators Brief explanation Production Tax 6x Landfill Tax 7x Carrier Bag Charge 8x

<!-- b000244 | heading | pages [12] -->
5.1.2 Factors in the Waste Management of Disposable Plastic

<!-- b000245 | prose | pages [12] -->
In this section, factors about waste management will be introduced, including the effectiveness of local policies like encouraging the recycling of the plastic waste, increasing subsidies for environment-friendly factories, as well infrastructures like trash bins, plastic incineration plants, etc. ⚫ Recycling Industry Investment Infrastructure will affect the behavior of citizens, which will indirectly influence the recycle rate of disposable plastic. To measure and simplify this relationship, this paper uses the number of trash cans to represent the plastic-relative infrastructure level. To verify the conjecture, we analyzed the correlation of the data by investigating the number of garbage cans and the recycling rate of their disposable garbage in a range of regions or cities.

<!-- b000246 | caption | pages [12] -->
Figure 8: Correlation of recovery rate and garbage can number in ten cities.

<!-- b000247 | prose | pages [12] -->
we can learn from Fig.8  that the Pearson Correlation Coefficient between the number of garbage cans and the recycling rate of disposable garbage was 0.7631, indicating a relatively strong linear relationship between them. What’s more, the government investment are supposed to be considered, since this will determined the future infrastructure level increase[11].

<!-- b000248 | prose | pages [12] -->
To sum up, two indicators are selected to measure the recycling infrastructure level, cf.

<!-- b000249 | caption | pages [12] -->
Table 6.

<!-- b000250 | caption | pages [12] -->
Table 6: Selected indictors in terms of the recycling industry investment

<!-- b000251 | prose | pages [12, 13] -->
Indicators Brief explanation Number of Trash Cans 9x Financial Investment by Government in Recycling Industry x 关注数学模型 ⚫ Infrastructure Level According to a scientific estimate, almost 79% of the plastic waste produced sits in landfills or in the natural environment such as ocean, while about 12% has been incinerated and only 9% has been recycled[2]. Although the incineration of the plastics will produce lots of toxic gas, we can use chemical methods to decompose them, which makes the harm caused by incineration is far less than that is caused by landfill and uncontrolled deposit.

<!-- b000252 | furniture | pages [12] -->
10

<!-- b000253 | furniture | pages [12] -->
2

<!-- b000254 | furniture | pages [12] -->
MATHmodels

<!-- b000255 | furniture | pages [12] -->
获取更多资讯

<!-- b000256 | furniture | pages [13] -->
Team # 2016287                                                                                                                                Page  12  of  21

<!-- b000258 | prose | pages [13] -->
Uncontrolled deposit in ocean is detrimental to the environment, especially the marine environment, as what is discussed in Section 4.2.4. Based on a survey published by UNEP[2], the uneven proportion of different ways of plastic waste management is partially because of the lack of the plastic waste incineration infrastructure, usually measured by the amount of plastic waste incineration plant.

<!-- b000259 | prose | pages [13] -->
The following predictions are made by UNEP, that is, if the amount of the plastic waste incineration plant increases by 50%, the percentage of the plastic waste landfilled or deposited in the environment will decrease greatly[2]. To get an intuitive understanding, the percentage data is presented in the pie chart in Fig.9.

<!-- b000260 | caption | pages [13] -->
Figure 9: Global flow of plastic packaging waste in 2015 and predictions in 2030 when the amount of

<!-- b000261 | prose | pages [13] -->
the plastic waste incineration plant increases by 50% Therefore, by increasing the amount of plastic waste incineration plant, the marine plastic litter may decline greatly, which is beneficial for marine environment.

<!-- b000262 | prose | pages [13] -->
To sum up, one indicator is selected to measure the incineration infrastructure level, cf.

<!-- b000263 | caption | pages [13] -->
Table 7.

<!-- b000264 | caption | pages [13] -->
Table 7: Selected indictors in terms of incineration infrastructure level

<!-- b000265 | prose | pages [13] -->
Indicators Brief explanation Amount of Plastic Waste Incineration Plant x 11

<!-- b000266 | heading | pages [13] -->
5.2 Classification of the Country

<!-- b000267 | prose | pages [13] -->
Although plastic waste is a global issue, the causes behind them may vary from countries, due to some regional-specific constraints. In this section, three categories are considered. They are the degree of economic development, sea-land location and degree of environmental pollution caused by plastics waste.

<!-- b000268 | prose | pages [13] -->
With respect to the degree of economic development, it is closely related to whether the ban policy can be implemented in the country. For developed countries like Denmark and Belgium, ban policies such as banning on the use of single-use plastic bags take effects, cf. Appendix 2. However, in some developing or undeveloped countries like China and Bangladesh, things are different. This is because plastics is a necessity owing to its convenience and low production cost, and banning plastics will certainly require alternatives, whose cost is likely to be higher than plastics. Only when the government provide subsidies to alternatives, can the price of this goes down, leading to the success of ban policy. Therefore, it’s easy to think of that, the wealthier the country is, the more success probability in ban policy.

<!-- b000269 | prose | pages [13] -->
With respect to the sea-land location, it is closely related to whether the amount of plastic waste incineration plant is more important than others. For coastal areas, plastics wastes that isn’t be recycled or incinerated is more likely to be littered into the ocean, which causes irreversible impacts on marine environment. However, for landlocked areas, it is harder to deposit the plastics in ocean.

<!-- b000270 | prose | pages [13, 14] -->
With respect to the degree of environmental pollution caused by plastics waste, it is also closely related to whether the ban policy can be implemented in the country, especially in 关注数学模型 undeveloped countries. If the environmental pollution is extremely serious in the country, the corresponding enforcement will be stricter, which makes the policy more effective. For example, Rwanda, though undeveloped, still managed to replace all the plastic bags with paper bags, cf. Appendix 1.

<!-- b000271 | furniture | pages [13] -->
2

<!-- b000272 | furniture | pages [13] -->
MATHmodels

<!-- b000273 | furniture | pages [13] -->
获取更多资讯

<!-- b000274 | furniture | pages [14] -->
Team # 2016287                                                                                                                                Page  13  of  21

<!-- b000276 | prose | pages [14] -->
The graphical view of the classification of the country is shown in Fig.10.

<!-- b000277 | caption | pages [14] -->
Figure 10: Cause and effects of the classification of the country

<!-- b000278 | heading | pages [14] -->
5.3 Disposable Plastic Waste Prediction Model

<!-- b000279 | prose | pages [14] -->
Based on the qualitative analysis in Section 6.1, indicators affecting the amount of plastic waste has been extracted. Then, in this section, the quantitative relationship between indicators and the amount of plastic waste will be determined correspondingly. First, PCA (Principle Components Analysis) was applied to decrease the internal correlation. Then, to predict the proportion of disposable plastic waste in total waste, MTSA (Multivariate Time Series Analysis) is used. Finally, the effectiveness of policies with regional-specific constraints was analyzed by comparing the weights of influence factors in different countries.

<!-- b000280 | heading | pages [14] -->
5.3.1 Principal Component Analysis of Influencing Indicators

<!-- b000281 | prose | pages [14] -->
Since there may be strong internal correlation among the 11 indicators, we first conduct principal component analysis on these indicators to realize the dimensionality reduction of date and eliminate the collinearity between variables. The analysis steps are as follows. ⚫ Data normalization Because the units and orders of magnitude of different indicators are greatly different, in order to eliminate this effect, data normalization is done first, which means the value of all data will be converted to the number between 0 and 1 without the units.

<!-- b000282 | prose | pages [14] -->
Let 𝑥𝑖𝑗 denotes the 𝑖𝑡ℎ influencing indicators of the 𝑗𝑡ℎ region[16], cf. Eq.12. − x x ij = jmean x (12) ij s j where 𝑖 = 1,2 … 𝑛, 𝑗= 1,2 … 𝑚. 𝑛 and 𝑚 is the number of indicators and sample areas n n ( )   ( ) 2 = = − − x x / , n s x x / n 1 respectively jmean ij j ij inean = = i 1 i 1 ⚫ Principal component determination Step 1: Calculate the covariance matrix of the matrix[𝑥𝑖𝑗]𝑛×𝑚.

<!-- b000283 | prose | pages [14] -->
Step 2: Calculate the eigenvalues and normalized eigenvectors of the covariance matrix.

<!-- b000284 | prose | pages [14] -->
Step 3: All principal components are derived from the computed eigenvalues and eigenvectors.

<!-- b000285 | prose | pages [14, 15] -->
m = Z C x (13) i ij ij = j 1 ijc is the( ) where 𝑖= 1,2 … 𝑛, 𝑍𝑖 is 𝑖𝑡ℎ principal component, ,i j  elements of the covariance matrix. 关注数学模型 Step 4: Choose the number of principal components by determining whether the cumulative contribution rate is greater than 85%. We suppose that the number is 𝑃[17].

<!-- b000286 | furniture | pages [14] -->
2

<!-- b000287 | furniture | pages [14] -->
MATHmodels

<!-- b000288 | furniture | pages [14] -->
获取更多资讯

<!-- b000289 | furniture | pages [15] -->
Team # 2016287                                                                                                                                Page  14  of  21

<!-- b000291 | heading | pages [15] -->
5.3.2 Multivariate Time Series Analysis with Principal Component

<!-- b000292 | prose | pages [15] -->
Multivariate time series analysis can not only predict the trend of the target variable, but also give the relationship of horizontal relationship of different variables[18]. Its normal expression is as follow.

<!-- b000293 | prose | pages [15] -->
( )   B P  =  + +  l i y B z  i ( ) t it t  B  = k 1 i (14) ( )  B a   = i  ( ) t t  B  i ( )  is the polynomial of the autoregressive coefficient of the thi input variable, where i B ( )  is the polynomial of the moving average coefficient of the  thi input variable, il is the i B t  is the regression residual sequence, and delay order of the  thi input variable, ta is the sequence of zero mean white noise.

<!-- b000294 | prose | pages [15] -->
These parameters can be estimated by the Maximum Likelihood Method, but the process is rather complex and needs large amount of calculation. Therefore, we choose Multiple Linear Regression and Least Squares Difference Method to simplify it, in which ty  and itx of each year, cf. Eq.15. the former can be used to get the relationship of P + =   (15) y x l l il il = i 1   to estimate   with the constraint Then, using it i Q  − 2 (16) min { ( y y ) } l l = l 1 where 𝑙 denotes the current year, and Q is the length of statistical time period. At last, ty and itx . we can get the Least Squares Difference relationship between P + =   (17) y x t t it it = i 1 itx ,we can predict the targeted variables So, if we can predict the future influence factor ty .

<!-- b000295 | heading | pages [15] -->
5.3.3 Model Application

<!-- b000296 | heading | pages [15] -->
⚫ Results of Principal Component Analysis

<!-- b000297 | prose | pages [15] -->
For the six regions divided according to different standards, nine indicators of 10 regions in different categories were selected for principal component analysis, and the cumulative curve of principal component contribution was shown in Fig.11.

<!-- b000298 | prose | pages [15, 16] -->
关注数学模型 As can be seen from the figure, in all cases, the sum of contributions of the first three principal components is greater than 85%, so we selected the first three principal components for subsequent analysis. ⚫ Prediction of Disposable Plastic Waste Reduction in Ireland Since disposable plastic bags account for the majority of Ireland's disposable plastic waste[20]. We use the MTSA to predict the proportion of disposable plastic bags in the country's total waste. Using the Multivariate Time Series Analysis, we adapt the data from 2000 to 2010[20], and give the prediction from 2011 to 2015.The results is in Fig.12.

<!-- b000299 | furniture | pages [15] -->
2

<!-- b000300 | furniture | pages [15] -->
MATHmodels

<!-- b000301 | furniture | pages [15] -->
获取更多资讯

<!-- b000302 | furniture | pages [16] -->
Team # 2016287                                                                                                                                Page  15  of  21

<!-- b000303 | caption | pages [16] -->
Figure 11: curve of principal component contribution

<!-- b000305 | caption | pages [16] -->
Figure 12: The prediction of the proportion of disposable plastic bags in the country's total waste

<!-- b000306 | prose | pages [16] -->
As seen in Fig.12, the predicted data is similar with the official one. In fact, the Relative Mean Square Deviation is just 4.2%, which demonstrates the effectiveness of the model. ⚫ Effectiveness of Policy The effectiveness of policy can be measured by the coefficient of each indicator. If the policy is effective, the reduction of the plastic production will be obvious, reflected in big coefficients. We make predications on the coefficients of some typical countries according to the classification in Section 5.2. and the corresponding radar chart is shown in Fig.13.

<!-- b000307 | caption | pages [16] -->
Figure 13: Comparison of coefficients of indicators between different kinds of countries

<!-- b000308 | prose | pages [16] -->
As shown above, in terms of the incineration indicator, the policy is more effective in coastal countries than landlocked ones. As for the ban policy indicator, the policy is more effective in developed countries than undeveloped ones and in serious pollution countries than in slight ones, which match the analysis in Section 5.2.

<!-- b000309 | heading | pages [16] -->
5.4 Environmentally Safe Level

<!-- b000310 | prose | pages [16] -->
To measure whether the level of the plastic waste after reduction is environmentally safe, two aspects are considered. One aspect is the Environmental Bearing Rate(EBR) mentioned in Section 5.4, which is used to measure the damage that the plastic waste does to the environment. The other one is human-friendly indicator, applied to measure the threat that plastic waste poses to human health.

<!-- b000311 | prose | pages [16] -->
关注数学模型

<!-- b000312 | furniture | pages [16] -->
2

<!-- b000313 | furniture | pages [16] -->
MATHmodels

<!-- b000314 | furniture | pages [16] -->
获取更多资讯

<!-- b000315 | furniture | pages [17] -->
Team # 2016287                                                                                                                                Page  16  of  21

<!-- b000316 | heading | pages [17] -->
5.4.1 Environmental Bearing Rate after Reduction of Plastic Waste

<!-- b000317 | prose | pages [17] -->
The calculation of EBR is based on Eq.10. To get the EBR after the reduction of the plastic waste, the predicted amount of annual plastic production has to substitute the relating variable in Eq.10. Next, based on the analysis in Section 5.4, if the value of EBR is less than 1, then it reaches an environmentally safe level.

<!-- b000318 | heading | pages [17] -->
5.4.2 Human-friendly Indicator

<!-- b000319 | prose | pages [17] -->
The plastic waste is also harmful to human’s health in both direct and indirect ways. In direct ways, people will take in water or air polluted by plastic waste. And in indirect ways, people may intake the toxic chemicals in plastics though food chain. What’s more, because humans are at the top of the food chain, the toxic accumulation is quite high comparing to other animals, which may do great harm to human health. Two ways are showed in Fig.14.

<!-- b000320 | caption | pages [17] -->
Figure 14: Direct and Indirect way that plastic waste harms human health

<!-- b000321 | prose | pages [17] -->
In this section, we mainly focused on the impacts of in the indirect way, because the harm caused by the direct way can be calculated through the previous analysis in environment in Section 6.4.1. Here we propose the Human Risk Index(HRI) to measure the threat that plastic waste poses to human health.

<!-- b000322 | prose | pages [17] -->
More specifically, we consider humans to be on the top of n food chains with m food i grade. And the weight of plastic waste is W kg. Considering the difference in food chains, we iu as the plastic waste absorbed by bottom species, donate R as the transfer efficiency of ij different stages in food chains. And the expression of HRI can be expressed as Eq.18.

<!-- b000323 | prose | pages [17] -->
m n i  = HRI ln( W u R ) (18) i ij = = i 1 j 1 If plastic waste can be reduced by a% by prediction, then Eq.19 can modified as follows.

<!-- b000324 | prose | pages [17] -->
  m n i  ( ) = − HRI ln 1 a % W u R (19)   i ij   = = i 1 j 1 Therefore, with the reduction of plastic waste, HRI will be improved, and the risk of people being harmed by plastic waste will decrease.

<!-- b000325 | heading | pages [17] -->
6. Targets and Impacts for Achieving the Minimal

<!-- b000326 | prose | pages [17] -->
Achievable Level of Global Waste The problem of plastic waste has become a global issue. According to UNEP[2], in 2010, the global plastic waste was 275 million tons, and the amount of mismanaged waste is up to 31.9 million tons, which is at the significant risk of leakage to the environment[2]. Therefore, to protect our Mother Earth, target for global waste of single-use plastic products have to be set. Meanwhile, we are also looking forward to changes in human life, environment and plastic industries after the goals are reached.

<!-- b000327 | prose | pages [17] -->
关注数学模型

<!-- b000328 | furniture | pages [17] -->
2

<!-- b000329 | furniture | pages [17] -->
MATHmodels

<!-- b000330 | furniture | pages [17] -->
获取更多资讯

<!-- b000331 | furniture | pages [18] -->
Team # 2016287                                                                                                                                Page  17  of  21

<!-- b000332 | heading | pages [18] -->
6.1 Targets for Minimal Achievable Level of Global Waste

<!-- b000333 | prose | pages [18] -->
The problem of plastic waste has become a global issue. To set a realistic target to tackle this, we plan to predict the amount of disposable plastic waste in the future, after some policies have been enforced.

<!-- b000334 | prose | pages [18] -->
Firstly, we will use Second Exponential Smoothing Method(SESM) to predict the Global Plastics Production till 2030. Then, based on the regional classification criteria in Section 5.2, all countries will be divided into 6 categories, then, proportion and recycling rate of disposable plastic waste of each category will be estimated. At last, the minimal achievable level of single-use plastic waste will be obtained.

<!-- b000335 | heading | pages [18] -->
6.1.1 Prediction of Global Plastics Production

<!-- b000336 | prose | pages [18] -->
According to the research of UNDP, the amount of global plastic production is predicted to increase in a long period. Therefore, we use the Second Exponential Smoothing Method to establish the Global Plastics Production Prediction Model, cf. Eq.20.

<!-- b000337 | prose | pages [18] -->
= + Y a bT + t T t t = + − (2) (1) (2) S aS (1 a S ) (20) − t t t 1  = + (1) (2) a 2 S S  t t t a = − (1) (2) b ( S S )  t t t −  1 a ( )1 ( ) 2 where is smooth value of the primary index, is the smooth value of the second tS tS Y +  is the predicted global plastics production of tht  year. Results are shown in index and t T

<!-- b000338 | caption | pages [18] -->
Fig. 15.

<!-- b000339 | caption | pages [18] -->
Figure 15: The prediction of global plastics production

<!-- b000340 | heading | pages [18] -->
6.1.2 Prediction of Disposable Plastic Waste Proportion

<!-- b000341 | prose | pages [18] -->
According Section 6.2, countries are divided into 6 categories. With multivariate time series model, we obtained the prediction of the proportion of disposable plastics in Fig.16.

<!-- b000342 | prose | pages [18, 19] -->
关注数学模型 Then we combine them with Entropy weight method to make the prediction.

<!-- b000343 | furniture | pages [18] -->
2

<!-- b000344 | furniture | pages [18] -->
MATHmodels

<!-- b000345 | furniture | pages [18] -->
获取更多资讯

<!-- b000346 | furniture | pages [19] -->
Team # 2016287                                                                                                                                Page  18  of  21

<!-- b000347 | caption | pages [19] -->
Figure 16: The predicted proportion of disposable plastic waste in different regions

<!-- b000349 | heading | pages [19] -->
6.1.3 Result of Achievable Level of Disposable Plastic Waste

<!-- b000350 | prose | pages [19] -->
⚫ Annual Amount of Production of Disposable Plastic Waste The production of disposable plastic waste is demonstrated in Fig. 17.

<!-- b000351 | caption | pages [19] -->
Figure 17: The prediction of global disposable plastic waste and its proportion in global waste

<!-- b000352 | prose | pages [19] -->
Therefore, we set the targeted level as 15.88 Million tones, based on the assumption that policy of limiting disposable plastic won’t change in the next ten years.

<!-- b000353 | prose | pages [19] -->
⚫ Percentage of Ways of Plastic Waste Management Due to the policy of increasing the number of plastic waste incineration plants, the percentage of the two ways of waste management will change in the future, cf.Fig18

<!-- b000354 | caption | pages [19] -->
Figure 18: The percentage of two ways of plastic waste management

<!-- b000355 | prose | pages [19] -->
Therefore, we set the targeted percentage of plastics into ocean declining to 18% and the percentage of plastics incinerated increasing to 65%.

<!-- b000356 | heading | pages [19] -->
6.2 Impacts for Achieving the Minimal Achievable Level of

<!-- b000357 | prose | pages [19] -->
Global Waste

<!-- b000358 | prose | pages [19] -->
If the target of 15.88 million tons is reached, there will be profound impact on wide range of our world, including the human life, the environment and the plastic industry.

<!-- b000359 | prose | pages [19] -->
To get a better understanding of the impacts, cf. Fig 19.

<!-- b000360 | prose | pages [19] -->
关注数学模型

<!-- b000361 | furniture | pages [19] -->
2

<!-- b000362 | furniture | pages [19] -->
MATHmodels

<!-- b000363 | furniture | pages [19] -->
获取更多资讯

<!-- b000364 | furniture | pages [20] -->
Team # 2016287                                                                                                                                Page  19  of  21

<!-- b000365 | caption | pages [20] -->
Figure 19: Impacts on the human life, environment and plastic industry

<!-- b000366 | heading | pages [20] -->
6.2.1 Impacts on Human Life

<!-- b000367 | prose | pages [20] -->
Based on Section 6.1, the factors can be divided into 2 categories. From the aspect of 3x ) will lead to the plastic waste production, the financial investment to alternative industry( 2x ). Meanwhile, the price of single-use plastic products decrease of the price of substitutes( 8x ) and the production tax on the production( 6x ) will rise due to the carrier bag charge( of plastic. Therefore, according to Q-P curve in Fig.6, the consumption of single-use products 5x ). It is will decline, also due to the government’s advocation on environmental protection( estimated that by that time, most people will use paper or cloth bags instead of plastic ones.

<!-- b000368 | heading | pages [20] -->
6.2.2 Impacts on the Environment

<!-- b000369 | prose | pages [20] -->
In analogy to analysis in Section 7.2.1, from the aspect of plastic waste production, if these x x ) are effective, the amount of production policies such as ban, tax, alternatives (factors 1 9 will decrease by 55%. From the aspect of plastic waste management, the financial investment x ) will increase the percentage of recycling, which lead to 47% decline of toxic in recycling( 10 x ), the percentage of depositing the exhaust. What’s more, with the rise of incineration plant( 11 waste in the ocean will decline to 12%, which is good for marine life.

<!-- b000370 | heading | pages [20] -->
6.2.3 Impacts on the Plastic Industry

<!-- b000371 | prose | pages [20] -->
Although the government's policies on enterprises are not the same in the short term, they will all lead to a reduction in the production of disposable plastics in the long run. In addition, with the increase of peoples' environmental awareness and government ’s supervision, the production of disposable plastics will be gradually reduced, and many companies may face bankruptcy and transformation.

<!-- b000372 | heading | pages [20] -->
7. Equity Issues and Solutions

<!-- b000373 | prose | pages [20] -->
The pollution caused by disposable plastics is a global problem, but the distribution of mismanaged waste varies significantly among countries, cf. Fig.20.

<!-- b000374 | prose | pages [20, 21] -->
关注数学模型 As shown above, the share of mismanaged waste in China is 27.7%, while that in some countries is less than 0.1 %, which shows inequity in plastic wastes. This is a visual description.

<!-- b000375 | furniture | pages [20] -->
2

<!-- b000376 | furniture | pages [20] -->
MATHmodels

<!-- b000377 | furniture | pages [20] -->
获取更多资讯

<!-- b000378 | furniture | pages [21] -->
Team # 2016287                                                                                                                                Page  20  of  21

<!-- b000379 | caption | pages [21] -->
Figure 20: The distribution  of mismanaged waste around the world, 2010

<!-- b000381 | heading | pages [21] -->
7.1 Equity Issues

<!-- b000382 | prose | pages [21] -->
The reasons that cause equity issues can be divided into two aspects[19]. One is the difference in the generation of waste or pollution. The other is the difference in the economic expenditure of disposable waste. And the corresponding solutions will be introduced next.

<!-- b000383 | heading | pages [21] -->
7.2 Solutions to Equity Issues

<!-- b000384 | prose | pages [21] -->
After analyzing the equity issues caused by disposable plastic waste, the following schemes are proposed. ⚫ License for the Plastic Waste The first solution is to introduce a license that only permits for certain amount of plastic waste according to population and economic levels of the country.

<!-- b000385 | prose | pages [21] -->
Not only can the license regulate the total amount of plastic waste, but also circulate between countries as a commodity. Countries that able to decrease the production of plastic waste can sell their licenses to those that can’t in the short term. In this way, countries with high share of mismanaged waste can compensate the ones with low share.  What’s more. considering that the production of excess plastic waste may increase the cost, countries will consider reducing their waste production. ⚫ Clarification of Inter-state Property Rights The second solution is to clarify of property rights of environmental resources.

<!-- b000386 | prose | pages [21] -->
Economically, the equity issue is partly caused by the ambiguity of the ownership of the property rights in environmental resources. According to Coase's theorem[19], without the negotiation cost, as long as the resource allocation is clear, the market will reach the most effective configuration. Therefore, the clarification of property rights of environmental resources is helpful to solve the issue. ⚫ Seeking International Cooperation The third solution is to combine experts and professional organizations in various fields worldwide to develop more practical solutions to protect the environment[19]. ⚫ Strengthening international legislation The fourth solution is to enhance the effectiveness of global policies can help solve the equity issues, considering that the intensity of policy implementation will affect the effectiveness of policies to some extent.

<!-- b000387 | heading | pages [21] -->
8. Sensitivity Analysis

<!-- b000388 | heading | pages [21] -->
8.1 Rotation Estimation for Multivariate Time Series Model

<!-- b000389 | prose | pages [21, 22] -->
Since we use the data of different regions to construct the Multivariate Time Series Model Based on Principal Component Analysis, rotation estimation will be applied to make sure that the model is well-adapted. Since 10-fold cross validation is the most commonly used 关注数学模型 method. we randomly partition the data of 10 regions into tenths, and for each tenth, the remaining nine are used to calculate its Mean Square Error.

<!-- b000390 | furniture | pages [21] -->
2

<!-- b000391 | furniture | pages [21] -->
MATHmodels

<!-- b000392 | furniture | pages [21] -->
获取更多资讯

<!-- b000393 | furniture | pages [22] -->
Team # 2016287                                                                                                                                Page  21  of  21

<!-- b000395 | caption | pages [22] -->
Figure 21: Error contrast                                          Figure 22: Gaussian Noise Curve

<!-- b000396 | prose | pages [22] -->
As shown in Fig.21, the Cross-Validation Error is only slightly higher than the Testing Set Error, demonstrating the robustness of the model.

<!-- b000397 | heading | pages [22] -->
8.2 Gaussian Noise

<!-- b000398 | prose | pages [22] -->
In setting a minimum target for the world's single-use plastic waste, we used the historical amount of production of global waste. However, we found the data is slightly different because it comes from different sources, which could lead to inaccuracy of the input data. And this may bring some deviations to the results of our model. Therefore, to verify the stability of our Global Garbage Forecasting Model, we add some gaussian noise to the input data to see how the relative deviation of results changes with the standard deviation increasing, cf. Fig.22.

<!-- b000399 | prose | pages [22] -->
It can be seen that when the standard deviation of gaussian noise is no more than 0.6, the relative deviation of the results does not exceed 20%, showing the robustness of our model.

<!-- b000400 | heading | pages [22] -->
9. Evaluation of the Model

<!-- b000401 | heading | pages [22] -->
9.1 Strength

<!-- b000402 | prose | pages [22] -->
⚫ The data are from official website and official journal, which is relatively rigorous.

<!-- b000403 | prose | pages [22] -->
Considering the changes in the environment, our model is extensible and can add new ⚫ environment variables to get accurate results.

<!-- b000404 | prose | pages [22] -->
Through the combination of the established mathematical model and the knowledge of ⚫ economics, we have proposed feasible solutions to equity issues caused by the disposable plastic products.

<!-- b000405 | prose | pages [22] -->
Lots of factors are taken into account ranging from economics to social behavior, ⚫ Therefore, we have obtained a reliable result.

<!-- b000406 | heading | pages [22] -->
9.2 Weakness

<!-- b000407 | prose | pages [22] -->
⚫ Although we try to use appropriate methods to deal with missing values, the lack of real data still affects the model. ⚫ Our model does not take the natural disasters into account, so there is bias in our analysis.

<!-- b000408 | prose | pages [22] -->
关注数学模型

<!-- b000409 | furniture | pages [22] -->
2

<!-- b000410 | furniture | pages [22] -->
MATHmodels

<!-- b000411 | furniture | pages [22] -->
获取更多资讯

<!-- b000412 | heading | pages [23] -->
MEMO

<!-- b000413 | prose | pages [23] -->
From: Team  2016287, ICM 2020

<!-- b000414 | prose | pages [23] -->
To: the International Council of Plastic Waste Management(ICM)

<!-- b000415 | prose | pages [23] -->
Date: February 17, 2020

<!-- b000416 | prose | pages [23] -->
Subject: Realistic global target of single-use plastic waste

<!-- b000417 | prose | pages [23] -->
Dear ICM, we are honored to describe the realistic global target of single-use plastic waste for you.

<!-- b000418 | prose | pages [23] -->
After the careful study of global single-use plastic product waste and policies, we get the following results. First, a realistic target for the annual amount of production of global single- use plastics in 2030 is 15.88 Million tones, with the percentage of plastics into ocean declining to 18% and the percentage of plastics incinerated increasing to 65%. To reach the target, considering the regional-specific constraints, different countries should enforce different policies.

<!-- b000419 | prose | pages [23] -->
We divided the countries into 6 categories. Here we provide advice for three of them.

<!-- b000420 | prose | pages [23] -->
▪ For developed and coastal countries, we suggest they focus on the ban policy about plastic bags, alternatives to plastics and building more plastic incineration plants to decrease the amount of plastic into the ocean.

<!-- b000421 | prose | pages [23] -->
▪ For developing and coastal countries, we suggest they focus on the tax policies including the landfill tax, production tax and carrying bag charge. Also, they should pay attention to the plastic incineration plants.

<!-- b000422 | prose | pages [23] -->
▪ For undeveloped and severely polluted countries, we suggest they focus on the ban policy, alternatives to plastics and the improvement of people’s environmental protection awareness.

<!-- b000423 | prose | pages [23] -->
Second, the target that we set is environmentally safe. In 2030, the reduction of plastic waste will have profound impact in the wide range of our world, including the human life, the environment and the plastic industry. At that time, with the improvement of environmental protection awareness, people will use cloth bags or paper bags more frequently, rather than plastic bags. Due to the ban policy, many traditional plastic companies may face a fate of transformation or bankruptcy. Instead, some high-tech companies that produce biodegradable plastics will rise and replace most of the traditional ones. All of these are good for both environment and human beings. With the decrease of plastic debris in ocean, marine wildlife such as sea turtle and seagull will be prevented from digesting plastics, which is beneficial for marine ecosystem. As for the human beings, we can take in food with less chemicals in plastic accumulated in the food chain, which will extend the life span of human beings.

<!-- b000424 | prose | pages [23, 24] -->
Third, although the vision of the target is wonderful, there may be some obstacles in the process. The timeline of our target is 10 years. According to the previous data and the prediction of our model, in the first 2 years, the effects of the policies may not be as good as we expect. Due to the low cost and inconvenience of the single-use plastic products, most people will feel uncomfortable when the carrier bags are charged or they have to use paper or cloth bags. Feelings of resistance may appear among people and this may hinder the enforcement of policies. However, in the 3rd to 8th year, the situation begins to change. With the embedding of the environmental protection awareness, people start to realize the importance of the Mother Earth and harm brought by the single-use plastic waste. Then, they begin to obey these policies and try a greener lifestyle. That’s when the amount of production of single-use plastic products 关注数学模型 decline most rapidly. And the environment is improved to a great extend. In the last two years, most people are accustomed to green life and the market share of single-use plastics and alternatives is relatively fixed. Therefore, the amount of production of single-use plastics decrease slowly and finally reaches the target of 15.88 million tones at the end of 2030.

<!-- b000425 | furniture | pages [23] -->
2

<!-- b000426 | furniture | pages [23] -->
MATHmodels

<!-- b000427 | furniture | pages [23] -->
获取更多资讯

<!-- b000429 | prose | pages [24] -->
Despite what is mentioned above, our team has to remind you that there are some other circumstances that may accelerate or hinder the achievement of the target.

<!-- b000430 | prose | pages [24] -->
Other circumstances that may accelerate the achievement of the target are as follows:

<!-- b000431 | prose | pages [24] -->
▪ The price of crude oil is on the rise. It is because crude oil serves as the raw material of the single-use plastics. And the price of the plastics will increase along with it.

<!-- b000432 | prose | pages [24] -->
According to the theory of Supply and Demand economically, the plastics will become less competitive to alternatives, thus accelerating the achievement of the target.

<!-- b000433 | prose | pages [24] -->
▪ Alternatives like biodegradable materials have a big breakthrough in technology. This will promote mass production and lead to the drop in the cost, which makes it more competitive in the market and replace the single-use plastics more rapidly.

<!-- b000434 | prose | pages [24] -->
Other circumstances that may hinder the achievement of the target are as follows:

<!-- b000435 | prose | pages [24] -->
▪ The law enforcement in a country is not strong enough. If so, even though a strict law is enacted, it is still difficult to control the production of plastics. Take the country, Bangladesh as an example, although strict limits had been released on plastic, the single-use plastic waste has not declined significantly.

<!-- b000436 | prose | pages [24] -->
▪ Countries don’t take on their own international responsibilities and don’t join agreements on reduction of the production of the single-use plastics. If so, the plastic industry in these countries may flourish uncontrollably, making it extremely difficult to meet global targets. What’s more, it also does harm to the equity issue among countries.

<!-- b000437 | prose | pages [24] -->
We hope that our analysis will help you to tackle the plastic waste problem in the future. And we draw a poster to send our best wishes to the world.

<!-- b000438 | prose | pages [24] -->
Yours Sincerely,

<!-- b000439 | furniture | pages [24] -->
Team # 2016287

<!-- b000440 | prose | pages [24] -->
关注数学模型

<!-- b000441 | furniture | pages [24] -->
2

<!-- b000442 | furniture | pages [24] -->
MATHmodels

<!-- b000443 | furniture | pages [24] -->
获取更多资讯

<!-- b000444 | heading | pages [25] -->
References

<!-- b000445 | references | pages [25] -->
[1] Geyer, R., Jambeck, J. R., & Law, K. L. (2017). Production, use, and fate of all plastics

<!-- b000446 | references | pages [25] -->
ever made. Science Advances, 3(7), e1700782.

<!-- b000447 | references | pages [25] -->
[2] UN environment, SINGLE-USE PLASTICSA Roadmap for Sustainability

<!-- b000448 | references | pages [25] -->
[3] Kara Lavender Law, Plastics in the Marine Environment, Sea Education Association,

<!-- b000449 | references | pages [25] -->
Woods Hole, Massachusetts 02543;

<!-- b000450 | references | pages [25] -->
[4] Jianwu, T., & Wenhu, Y. (1998). Study on environmental bearing capacity and its

<!-- b000451 | references | pages [25] -->
quantification.[J]. China Environmental Science, 3.

<!-- b000452 | references | pages [25] -->
[5] Li, W. C., Tse, H. F., & Fok, L. (2016). Plastic waste in the marine environment: A

<!-- b000453 | references | pages [25] -->
review of sources, occurrence and effects. Science of the Total Environment, 566, 333-349.

<!-- b000454 | references | pages [25] -->
[6] Ahlborg, U. G., Becking, G. C., Birnbaum, L. S., Brouwer, A. A., Derks, H. J. G. M.,

<!-- b000455 | references | pages [25] -->
Feeley, M., ... & Safe, S. H. (1994). Toxic equivalency factors for dioxin-like

<!-- b000456 | references | pages [25] -->
PCBs. Chemosphere, 28(6), 1049-1068.

<!-- b000457 | references | pages [25] -->
[7] Forschungsverbund Berlin. (2018, February 5). An underestimated threat: Land-based

<!-- b000458 | references | pages [25] -->
pollution with microplastics. ScienceDaily. Retrieved February 14, 2020 from

<!-- b000459 | references | pages [25] -->
www.sciencedaily.com/releases/2018/02/180205125728.htm

<!-- b000460 | references | pages [25] -->
[8] Hu, Y., Zhang, P., Chen, D., Zhou, B., Li, J., & Li, X. W. (2012). Hydrothermal treatment

<!-- b000461 | references | pages [25] -->
of municipal solid waste incineration fly ash for dioxin decomposition. Journal of hazardous

<!-- b000462 | references | pages [25] -->
materials, 207, 79-85.

<!-- b000463 | references | pages [25] -->
[9] Galloway T.S. (2015) Micro- and Nano-plastics and Human Health. In: Bergmann M.,

<!-- b000464 | references | pages [25] -->
Gutow L., Klages M. (eds) Marine Anthropogenic Litter.

<!-- b000465 | references | pages [25] -->
[10] https://en.wikipedia.org/wiki/Substitute_good

<!-- b000466 | references | pages [25] -->
[11] https://en.wikipedia.org/wiki/Market_(economics)

<!-- b000467 | references | pages [25] -->
[12] Wang Weiwei. Cultivation of Chinese citizens' ecological and environmental protection

<!-- b000468 | references | pages [25] -->
awareness from the perspective of ecological culture [D] .Bohai University, 2017.

<!-- b000469 | references | pages [25] -->
[13] Treasury, H. M. (2018). Tackling the Plastic Problem. Using the Tax System or Charges

<!-- b000470 | references | pages [25] -->
to Address Single-Use Plastic Waste.

<!-- b000471 | references | pages [25] -->
[14] https://www.azocleantech.com/article.aspx?ArticleID=928

<!-- b000472 | references | pages [25] -->
[15] Liao Qin, Wang Jinping, Wang Fang. International Single-use Plastic Pollution Control

<!-- b000473 | references | pages [25] -->
Policy and Its Implications for China [J]. Global Economic Outlook,2018,33(07):63-71.

<!-- b000474 | references | pages [25] -->
[16] Wei-Xiang XU, Quan-shou ZHANG. An Algorithm of Meta-Synthesis Based on the

<!-- b000475 | references | pages [25] -->
Grey The- ory and Fuzzy Mathematics [J].Systems engineering theory and practice, 2001,(4):

<!-- b000476 | references | pages [25] -->
114-119

<!-- b000477 | references | pages [25] -->
[17] Westerhuis J A , Kourti T , Macgregor J F . Analysis of multiblock and hierarchical PCA

<!-- b000478 | references | pages [25] -->
and PLS models[J]. Journal of Chemometrics, 1998, 12(5):301-321.

<!-- b000479 | references | pages [25] -->
[18] Chan, N. H. . (1973). Multivariate Time Series. Time Series: Applications to Finance

<!-- b000480 | references | pages [25] -->
with R and S-Plus, Second Edition. John Wiley & Sons, Inc.

<!-- b000481 | references | pages [25] -->
[19] Dawei He, Jingsheng Chen On the International Law Solution to Transnational Pollution

<!-- b000482 | references | pages [25] -->
from the Perspetive of Efficiency and Equity (Department of Urban and Environmental

<!-- b000483 | references | pages [25] -->
Sciences, Peking University, Beijing 100871)

<!-- b000484 | references | pages [25] -->
[20] The Litter Monitoring Body. The National Litter Pollution Monitoring System: Systems

<!-- b000485 | references | pages [25] -->
Survey Report 2015[R/OL].(2016-04-26)[2017-11-16].

<!-- b000486 | heading | pages [25] -->
Appendix

<!-- b000487 | heading | pages [25] -->
Appendix 1: Ban policies of some countries

<!-- b000488 | heading | pages [25] -->
Appendix 2: Ban policies of some countries

<!-- b000489 | prose | pages [25] -->
Country Year Policy Impact Belgium 2016 Ban on the use of single-use Over time, plastic bags were replaced plastic bags in Wallonia. by paper bags.

<!-- b000490 | prose | pages [25, 26] -->
Exception of thin compostable bags for foods that can be moist, until the end of 2018 (Surfrider Foundation Europe, 2017). 关注数学模型 China 2008 Ban on non-biodegradable Ban has been ineffectively enforced in plastic bags <25 μ food markets and among small retailers. (Xanthos, 2017). Bangladesh 2002 Ban on polyethylene plastic Initial positive response from the bags. public. Use of plastic bags increased after some years due to lack of enforcement and absence of cost- effective alternatives (IRIN, 2011).

<!-- b000491 | furniture | pages [25] -->
2

<!-- b000492 | furniture | pages [25] -->
MATHmodels

<!-- b000493 | furniture | pages [25] -->
获取更多资讯

<!-- b000495 | prose | pages [26] -->
Rwanda 2008 Ban on the production, use, In the first phase the ban resulted in importation and sale of all a black market for plastic bags.

<!-- b000496 | prose | pages [26] -->
polyethylene bags. Over time, plastic bags were replaced by paper bags (Clavel, 2014; Pilgrim, 2016).

<!-- b000497 | prose | pages [26] -->
关注数学模型

<!-- b000498 | furniture | pages [26] -->
2

<!-- b000499 | furniture | pages [26] -->
MATHmodels

<!-- b000500 | furniture | pages [26] -->
获取更多资讯

<!-- b000501 | heading | pages [27] -->
Appendix 2: Main Code

<!-- b000502 | prose | pages [27] -->
alpha=0.3;

<!-- b000503 | prose | pages [27] -->
beta=0.3;

<!-- b000504 | prose | pages [27] -->
gamma=0.5;

<!-- b000505 | prose | pages [27] -->
fc=12;

<!-- b000506 | prose | pages [27] -->
k=12;

<!-- b000507 | prose | pages [27] -->
%%

<!-- b000508 | prose | pages [27] -->
X=load('passengers.txt');

<!-- b000509 | prose | pages [27] -->
S=reshape(X,[144,1]);

<!-- b000510 | prose | pages [27] -->
plot(S,'r');

<!-- b000511 | prose | pages [27] -->
n=length(S);

<!-- b000512 | prose | pages [27] -->
a(1)=sum(S(1:k))/k;

<!-- b000513 | prose | pages [27] -->
b(1)=(sum(S(k+1:2*k))-sum(S(1:k)))/k^2;

<!-- b000514 | prose | pages [27] -->
s=S-a(1);

<!-- b000515 | prose | pages [27] -->
y=a(1)+b(1)+s(1);

<!-- b000516 | prose | pages [27] -->
f=zeros(144,1);

<!-- b000517 | prose | pages [27] -->
for i=1:n+fc

<!-- b000518 | prose | pages [27] -->
if i==length(S)

<!-- b000519 | prose | pages [27] -->
S(i+1)=a(end)+b(end)+s(end-k+1);

<!-- b000520 | prose | pages [27] -->
end

<!-- b000521 | prose | pages [27] -->
a(i+1)=alpha*(S(i)-s(i))+(1-alpha)*(a(i)+b(i));

<!-- b000522 | prose | pages [27] -->
b(i+1)=beta*(a(i+1)-a(i))+(1-beta)*b(i);%

<!-- b000523 | prose | pages [27] -->
s(i+1)=gamma*(S(i)-a(i)-b(i))+(1-gamma)*s(i);%

<!-- b000524 | prose | pages [27] -->
y(i+1)=a(i+1)+b(i+1)+s(i+1);

<!-- b000525 | prose | pages [27] -->
end

<!-- b000526 | prose | pages [27] -->
hold on

<!-- b000527 | prose | pages [27] -->
plot(y,'b');

<!-- b000528 | prose | pages [27] -->
hold off

<!-- b000529 | prose | pages [27] -->
关注数学模型

<!-- b000530 | furniture | pages [27] -->
2

<!-- b000531 | furniture | pages [27] -->
MATHmodels

<!-- b000532 | furniture | pages [27] -->
获取更多资讯
