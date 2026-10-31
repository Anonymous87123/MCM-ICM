# P-E-2020-2016287-6ed5334f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
2020

<!-- b000002 | prose | pages [1] -->
Problem Chosen

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

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
Global Disposable Plastic Waste Crisis

<!-- b000010 | heading | pages [1] -->
Summary

<!-- b000011 | prose | pages [1] -->
The plastic waste pollution, is posing a great threat to the global ecosystem and human health while causing global equity issues, and the rise of disposable plastics is even worsening the situation. To better understand and tackle these problems, this paper focuses on measuring disposable plastic waste’s influence, predicting its trend and give some reasonable advice.

<!-- b000012 | prose | pages [1] -->
For sake of estimating the maximum levels of disposable plastic waste that can safely be alleviated without further environmental damage, we created an Environment Bearing Rate Model (EBRM). Firstly, the relationship of disposable plastic waste and Environmental Bearing Quantity (EBQ) are given by analyzing the source and disposal of plastic waste. Secondly, we derive the interaction relationship between EBQ and Environmental Bearing Capacity (EBC) to get the Threshold Conditions for environmental self-recovery, which is EBQ equals to EBC. Finally, the maximum level of disposable plastic waste is deduced.

<!-- b000013 | prose | pages [1] -->
To discuss the extent disposable plastic waste level can be reduced to, we establish a DPWPM (Disposable Plastic Waste Prediction Model). Firstly, 11 quantifiable indicators influencing the generation and management of disposable plastic waste are selected. Then we classify the regions according to development degree, pollution level and whether it is coastal. Next, we do Principal Component Analysis with these indicators to reduce dimensionality. Finally, we use Multivariate Time Series Model to obtain the relationship between the disposable plastic waste proportion and these indicators and predict to what extent it will be reduced. To verify the model, we apply it to Ireland and the results are the disposable plastic waste rate in total waste will decrease to 0.3%, close to official statistic data. What’s more, we analyze the policy effectiveness in different regions and measure how the reduction will influence ecosystem and human health using the EBRM and Human-Friendly Indicator.

<!-- b000014 | prose | pages [1] -->
For giving a minimal achievable level of global waste of disposable plastic, we firstly use Quadratic Exponential Smoothing Model to predict total global plastic production. Then, DPWPM is used to predict the its proportion in plastic waste in different country groups. Combined with EWM (Entropy Weight Method), we get a global curve of its proportion in plastic. At last, we get the result that the minimal achievable level of global waste of disposable plastic is 15.88 million tones till 2030. Besides, we also draw a conclusion of how the target will influence human life, environmental and the plastic industry.

<!-- b000015 | prose | pages [1] -->
The unfair problems of the global plastic waste crisis are mainly reflected in the uneven distribution of plastic waste production and pollution and the different economic investment in the disposal of plastic waste of different countries. We propose four intended solutions including allocating Permits for the plastic waste and clarification of inter-state property rights.

<!-- b000016 | prose | pages [1] -->
Finally, we use Rotation Estimation and Gaussian noise to test the robustness for the models and write a memo to the ICM about the minimal achievable level of global plastic waste.

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | furniture | pages [1] -->


<!-- b000020 | furniture | pages [1] -->


<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | furniture | pages [1] -->


<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | furniture | pages [1] -->


<!-- b000030 | keywords | pages [1] -->
Keywords: Disposable Plastic, Multivariate Time Series, EWM, PCA

<!-- b000031 | prose | pages [1] -->
关注数学模型

<!-- b000032 | furniture | pages [1] -->
2

<!-- b000033 | furniture | pages [1] -->
MATHmodels

<!-- b000034 | furniture | pages [1] -->
获取更多资讯

<!-- b000035 | furniture | pages [2] -->
Team # 2016287                                                                                                                                Page  1  of  21

<!-- b000036 | heading | pages [2] -->
Contents

<!-- b000037 | contents | pages [2] -->
1. Introduction ............................................................................................................................ 2

<!-- b000038 | contents | pages [2] -->
1.1 Background .................................................................................................................. 2

<!-- b000039 | contents | pages [2] -->
1.2 Restatement of Problem ............................................................................................... 2

<!-- b000040 | contents | pages [2] -->
1.3 Overview of Our Work ................................................................................................ 2

<!-- b000041 | contents | pages [2] -->
2. Assumptions and Justifications .............................................................................................. 3

<!-- b000042 | contents | pages [2] -->
3. Notations ................................................................................................................................ 3

<!-- b000043 | contents | pages [2] -->
4. Maximum Levels of Disposable Plastic Waste ..................................................................... 3

<!-- b000044 | contents | pages [2] -->
4.1 Source of the waste ...................................................................................................... 3

<!-- b000045 | contents | pages [2] -->
4.2 Waste Management ...................................................................................................... 4

<!-- b000046 | contents | pages [2] -->
4.2.1 Recycling .......................................................................................................... 4

<!-- b000047 | contents | pages [2] -->
4.2.2 Incineration ....................................................................................................... 4

<!-- b000048 | contents | pages [2] -->
4.2.3 Landfill .............................................................................................................. 4

<!-- b000049 | contents | pages [2] -->
4.2.4 Uncontrolled Deposit in Ocean ......................................................................... 5

<!-- b000050 | contents | pages [2] -->
4.3

<!-- b000051 | contents | pages [2] -->
Environmental Bearing Rate Model ......................................................................... 5

<!-- b000052 | contents | pages [2] -->
4.3.1 Environmental Bearing Rate ............................................................................. 6

<!-- b000053 | contents | pages [2] -->
4.3.2 Environmental Bearing Quantity Measurement ............................................... 7

<!-- b000054 | contents | pages [2] -->
4.3.3 Environmental Bearing Capacity Measurement ............................................... 8

<!-- b000055 | contents | pages [2] -->
4.4

<!-- b000056 | contents | pages [2] -->
Maximum Levels of Disposable Plastic Product Waste .......................................... 8

<!-- b000057 | contents | pages [2] -->
4.4.1 Current Waste Quantity and Capacity .............................................................. 8

<!-- b000058 | contents | pages [2] -->
5. Reduction of Plastic Waste and the Environmentally Safe Level after Reduction ................ 8

<!-- b000059 | contents | pages [2] -->
5.1 Factors Influencing Plastic Waste Reduction .............................................................. 9

<!-- b000060 | contents | pages [2] -->
5.1.1 Factors in the Waste Production of Disposable Plastic .................................... 9

<!-- b000061 | contents | pages [2] -->
5.1.2 Factors in the Waste Management of Disposable Plastic ............................... 11

<!-- b000062 | contents | pages [2] -->
5.2 Classification of the Country ..................................................................................... 12

<!-- b000063 | contents | pages [2] -->
5.3 Disposable Plastic Waste Prediction Model .............................................................. 13

<!-- b000064 | contents | pages [2] -->
5.3.1 Principal Component Analysis of Influencing Indicators ............................... 13

<!-- b000065 | contents | pages [2] -->
5.3.2 Multivariate Time Series Analysis with Principal Component ...................... 14

<!-- b000066 | contents | pages [2] -->
5.3.3 Model Application .......................................................................................... 14

<!-- b000067 | contents | pages [2] -->
5.4 Environmentally Safe Level ...................................................................................... 15

<!-- b000068 | contents | pages [2] -->
5.4.1 Environmental Bearing Rate after Reduction of Plastic Waste ...................... 16

<!-- b000069 | contents | pages [2] -->
5.4.2 Human-friendly Indicator ............................................................................... 16

<!-- b000070 | contents | pages [2] -->
6. Targets and Impacts for Achieving the Minimal Achievable Level of Global Waste ......... 16

<!-- b000071 | contents | pages [2] -->
6.1 Targets for Minimal Achievable Level of Global Waste ........................................... 17

<!-- b000072 | contents | pages [2] -->
6.1.1 Prediction of Global Plastics Production ........................................................ 17

<!-- b000073 | contents | pages [2] -->
6.1.2 Prediction of Disposable Plastic Waste Proportion ........................................ 17

<!-- b000074 | contents | pages [2] -->
6.1.3 Result of Achievable Level of Disposable Plastic Waste ............................... 18

<!-- b000075 | contents | pages [2] -->
6.2 Impacts for Achieving the Minimal Achievable Level of Global Waste .................. 18

<!-- b000076 | contents | pages [2] -->
6.2.1 Impacts on Human Life .................................................................................. 19

<!-- b000077 | contents | pages [2] -->
6.2.2 Impacts on the Environment ........................................................................... 19

<!-- b000078 | contents | pages [2] -->
6.2.3 Impacts on the Plastic Industry ....................................................................... 19

<!-- b000079 | contents | pages [2] -->
7. Equity Issues and Solutions ................................................................................................. 19

<!-- b000080 | contents | pages [2] -->
7.1 Equity Issues .............................................................................................................. 20

<!-- b000081 | contents | pages [2] -->
7.2 Solutions to Equity Issues .......................................................................................... 20

<!-- b000082 | contents | pages [2] -->
8. Sensitivity Analysis ............................................................................................................. 20

<!-- b000083 | contents | pages [2] -->
8.1 Rotation Estimation for Multivariate Time Series Model ......................................... 20

<!-- b000084 | contents | pages [2] -->
8.2

<!-- b000085 | contents | pages [2] -->
Gaussian Noise ....................................................................................................... 21

<!-- b000086 | contents | pages [2] -->
9. Evaluation of the Model....................................................................................................... 21

<!-- b000087 | contents | pages [2] -->
9.1 Strength ...................................................................................................................... 21

<!-- b000088 | contents | pages [2] -->
9.2 Weakness ................................................................................................................... 21

<!-- b000089 | furniture | pages [2] -->


<!-- b000090 | contents | pages [2] -->
关注数学模型

<!-- b000091 | furniture | pages [2] -->
2

<!-- b000092 | furniture | pages [2] -->
MATHmodels

<!-- b000093 | furniture | pages [2] -->
获取更多资讯

<!-- b000094 | furniture | pages [3] -->
Team # 2016287                                                                                                                                Page  2  of  21

<!-- b000095 | heading | pages [3] -->
1. Introduction

<!-- b000096 | heading | pages [3] -->
1.1 Background

<!-- b000097 | prose | pages [3] -->
Single-use plastics products, referred to as items intended to be used only once before thrown away, are almost everywhere in our life, including grocery bags, food packaging, bottles, straws, containers, cups, cutlery, etc.[2] However, with the large-scale production of single-use plastic products, the white pollution caused by them is severe nowadays. According to a UNEP report[2], single-use plastics take most of the spots in the Top Ten most common finds during international coastal cleanups. What’s worse, poor waste management systems will exacerbate the extent of pollution. At present, several methods are used to dispose them, including incineration, dump, recycling, landfill and discard in the natural environment[1].

<!-- b000098 | prose | pages [3] -->
Since the plastic waste take even several hundred year to break down, it is posing a great threat to the ecosystem and human health[2].Especially, Marine ecosystems are being hit hard as most plastic waste flows into the ocean. Effects can be seen by the approximately 4-12 million tons of plastic waste that enter the oceans each year[1]. The economic damage caused by plastic waste is vast. Plastic litter in the Asia-Pacific region alone costs its tourism, fishing and shipping industries $1.3 billion per year[3].

<!-- b000099 | prose | pages [3] -->
Recently years, many governments has taken positive interventions to tackle this problem, mainly by improving waste management practices, introduce financial incentives, financing more research and development of alternative materials, raising awareness among consumers and so on[3]. However, there are little research about the prediction of disposable plastic waste.

<!-- b000100 | heading | pages [3] -->
1.2 Restatement of Problem

<!-- b000101 | prose | pages [3] -->
In order to solve the plastic waste problem, we need to formulate a plan to reduce or even eliminate disposable plastic products by slowing down plastic production and improving waste utilization. Considering that plastics is mostly single-use, we focus particularly on disposable Plastic Products.

<!-- b000102 | prose | pages [3] -->
What we need to do is as follows: ⚫ Establish a model to estimate the maximum level of disposable plastic product waste

<!-- b000103 | prose | pages [3] -->
Under the premise that waste can safely be mitigated without further environmental pollution. ⚫ Research how much plastic waste can be reduced to reach an environmentally safe

<!-- b000104 | prose | pages [3] -->
level. ⚫ Based on the above research, set a goal for minimal achievable level of disposable

<!-- b000105 | prose | pages [3] -->
plastic waste globally and explore the impact on many aspects of reaching that goal. ⚫ Considering that the causes and consequences of disposable plastic problems vary

<!-- b000106 | prose | pages [3] -->
from place to place, discuss related equity issues and propose solutions.

<!-- b000107 | heading | pages [3] -->
1.3 Overview of Our Work

<!-- b000108 | prose | pages [3] -->
We have established a model to determine the maximum level of the disposable plastic waste using the theory of environment bearing rate. Moreover, a model for predicting the extent the level of the disposable plastic waste can be reduced to according to many influence factors and historic data. Using the two models, we evaluate the effectiveness of different policies in different kinds of regions and give a reasonable minimum targeted achievable level for the global disposable plastic waste and advocates some solutions to solve the equality issues caused by the global plastic waste crisis. The whole modeling process are shown in Fig 1.

<!-- b000109 | prose | pages [3] -->
关注数学模型

<!-- b000110 | furniture | pages [3] -->
2

<!-- b000111 | furniture | pages [3] -->
MATHmodels

<!-- b000112 | furniture | pages [3] -->
获取更多资讯

<!-- b000113 | furniture | pages [4] -->
Team # 2016287                                                                                                                                Page  3  of  21

<!-- b000114 | furniture | pages [4] -->


<!-- b000115 | caption | pages [4] -->
Figure 1: whole modeling process of the paper

<!-- b000116 | heading | pages [4] -->
2. Assumptions and Justifications

<!-- b000117 | prose | pages [4] -->
To simplify the cost benefit analysis model, this paper makes following basic assumption, each of which is properly justified.

<!-- b000118 | prose | pages [4] -->
⚫ We assume that the increase in Environmental Bearing Capacity can be ignored

<!-- b000119 | prose | pages [4] -->
because the evolution of the ecosystem is a long-time process. ⚫ Sudden change in the environment can be ignored, because of its rareness. ⚫ We assume that all the regions will react positively to the worsening problems of dis

<!-- b000120 | prose | pages [4] -->
posable plastic waste and take suitable measures to improve it. This assumption is m ade according to reactions of most countries.

<!-- b000121 | heading | pages [4] -->
3. Notations

<!-- b000122 | prose | pages [4] -->
We list the symbols and notations used in this paper in Table 1.

<!-- b000123 | caption | pages [4] -->
Table 1: Symbols and Definitions

<!-- b000124 | prose | pages [4] -->
Symbols          Meanings                                                                                         Unit

<!-- b000125 | prose | pages [4] -->
C t          Environmental Bearing Capacity in year t                                             -- ( ) Q t          Environmental Bearing Quantity in year t                                             --

<!-- b000126 | furniture | pages [4] -->


<!-- b000127 | prose | pages [4] -->
( ) EBR           Environmental Bearing Rate                                                                  -- HFI           Human-friendly Indicator                                                                       --

<!-- b000128 | heading | pages [4] -->
4. Maximum Levels of Disposable Plastic Waste

<!-- b000129 | prose | pages [4] -->
If the amount pollution caused by the plastic waste is within the controllable range, it won’t cause damage to the environment. However, when the single-use plastic product waste reaches a certain level, it will exceed the environment's own ability to repair, making the environment worse and difficult to recover. Therefore, we hope to develop a model to estimate the maximum levels of single-use or disposable plastic product waste that can safely be mitigated without further environmental damage.

<!-- b000130 | heading | pages [4] -->
4.1 Source of the waste

<!-- b000131 | prose | pages [4] -->
In most situation, single-use plastics are used for packaging, such as shopping bags, wrappers and bottles. After the use of these products, they will be discarded and become plastics waste. Among these wastes, as stated in the UNEP report[2], plastic bags and foamed plastic products are perceived as the most problematic source of the plastic wastes. It is because single-use plastic bags are the most common disposable plastic products in life to hold items[1]. And as for foamed plastics, its lightness, strength and thermal insulation make it great for disposable tableware such as lunch boxes. In china, with the rise of the takeaway industry, the use of foam has increased uncontrollably[1].

<!-- b000132 | prose | pages [4] -->
关注数学模型

<!-- b000133 | furniture | pages [4] -->
2

<!-- b000134 | furniture | pages [4] -->
MATHmodels

<!-- b000135 | furniture | pages [4] -->
获取更多资讯

<!-- b000136 | furniture | pages [5] -->
Team # 2016287                                                                                                                                Page  4  of  21

<!-- b000137 | prose | pages [5] -->
To simplify our model, only two sources of the waste mentioned above is considered.

<!-- b000138 | prose | pages [5] -->
fP are introduced to represent the annual production of plastic bags and foamed bP and Also, plastic products respectively.

<!-- b000139 | heading | pages [5] -->
4.2 Waste Management

<!-- b000140 | prose | pages [5] -->
The current consumption of plastic waste is large, which makes it more important to manage their end-of-life in an environment-friendly way. Scientifically speaking, “energy recovery processes are preferable to landfilling or improper forms of disposal[2]”. To show this more clearly, a waste management hierarchy, reflecting the degree of impact on the environment during different process of plastic wastes is shown in Fig. 2.

<!-- b000141 | furniture | pages [5] -->


<!-- b000142 | caption | pages [5] -->
Figure 2: Different ways to deal with plastic waste and the degree of impact on the environment.

<!-- b000143 | prose | pages [5] -->
For each level of the waste management hierarchy: Recycling is quite environment- friendly because it decrease the production of disposable plastics. Landfill has a bad impact on the environment because it takes thousands of years for plastics to decompose. Incineration harms the environment due to the toxic gas in the burning process of plastics. Uncontrolled deposit in places like ocean is extremely detrimental to the environment owing to its harm to marine wildlife.

<!-- b000144 | prose | pages [5] -->
Thus, we mainly focus on four of them. They are recycling, incineration, landfill and uncontrolled deposit in ocean.

<!-- b000145 | heading | pages [5] -->
4.2.1 Recycling

<!-- b000146 | prose | pages [5] -->
Some disposable plastic products, usually made of thermoplastic materials, can be recycled through factory processing. In this way, not only the consumption of resources is reduced, but also the plastic waste does, thereby greatly reducing environmental pollution.

<!-- b000147 | prose | pages [5] -->
To measure the availability of the resources to recycle the waste, the percentage of plastic rp t is introduced. The larger the value of waste recycled ( ) recycling resources are.

<!-- b000148 | heading | pages [5] -->
4.2.2 Incineration

<!-- b000149 | prose | pages [5] -->
rp t is, the more available the ( )

<!-- b000150 | prose | pages [5] -->
Although the plastic waste can be decomposed through incineration, large amount of exhaust gas released will damage the atmosphere and have a negative impact on the environment

<!-- b000151 | prose | pages [5] -->
To measure the availability of the resources to incinerate the waste, the percentage of ip t is introduced. The larger the value of ( ) plastic waste incinerated available the incineration resources are.

<!-- b000152 | heading | pages [5] -->
4.2.3 Landfill

<!-- b000153 | prose | pages [5] -->
ip t is, the more ( )

<!-- b000154 | prose | pages [5] -->
Landfill means to bury the plastic waste in soil. It’s widely used in China because of low cost and good sanitation. However, chemical substances decomposed will also harm the soil.

<!-- b000155 | prose | pages [5] -->
关注数学模型

<!-- b000156 | furniture | pages [5] -->
2

<!-- b000157 | furniture | pages [5] -->
MATHmodels

<!-- b000158 | furniture | pages [5] -->
获取更多资讯

<!-- b000159 | furniture | pages [6] -->
Team # 2016287                                                                                                                                Page  5  of  21

<!-- b000160 | prose | pages [6] -->
To measure the availability of the resources to landfill the waste, the percentage of plastic lp t is introduced. The larger the value of waste landfilled ( ) landfill resources are.

<!-- b000161 | prose | pages [6] -->
lp t is, the more available the ( )

<!-- b000162 | heading | pages [6] -->
4.2.4 Uncontrolled Deposit in Ocean

<!-- b000163 | prose | pages [6] -->
Every year, there is a large amount of plastic product waste entering the ocean in various ways. And scientists estimate that the amount of plastic into the ocean is up to 4.8–12.7 million metric tons in 2010[3].

<!-- b000164 | prose | pages [6] -->
During weathering and biological processes, plastic wastes into the ocean will gradually turn into plastic debris, which is easy to be ingested by marine wildlife. This is extremely harmful to marine ecology. Also, there is large plastics, which can interfere the navigation of ships. And the toxic chemicals in plastics will also pollute seawater, putting marine life at risk of being poisoned

<!-- b000165 | prose | pages [6] -->
To measure the availability of the resources to deposit the waste in ocean uncontrollably, the percentage of plastic waste deposited into the ocean op t is introduced. The larger the ( )

<!-- b000166 | prose | pages [6] -->
op t is, the more plastic waste is deposited into the ocean. value of ( )

<!-- b000167 | heading | pages [6] -->
4.3 Environmental Bearing Rate Model

<!-- b000168 | prose | pages [6] -->
As we all know, ecosystems are capable of self-regulating. When they suffer certain damage, such as environmental pollution and reduction in the number of species, as long as these impacts do not exceed the threshold for ecosystem self-regulation, the environment can self-recover within a certain period of time.

<!-- b000169 | prose | pages [6] -->
Ecologically, terms like Environmental Bearing Capacity (EBC) and Environmental Bearing Quantity (EBQ) are applied to descript the process above.

<!-- b000170 | prose | pages [6] -->
When the plastic waste related EBQ is smaller than EBC, the single-use plastic product waste that can safely be mitigated without further environmental damage. The definition and property of EBC and EBQ are as follows:

<!-- b000171 | prose | pages [6] -->
⚫ Environmental Bearing Quantity (EBQ). This refers to the impacts that human

<!-- b000172 | prose | pages [6] -->
activities make to the environment in a period. For example, human activities such as emitting the exhaust, discharging the plastic waste into the ocean will cause damage to the natural environment. The harmful influence includes but is not limited to the increase of the exhaust, the reduction in species, etc. All of these impacts to nature in a period belong to EBQ. And this can be measured by some metrics described in Section 5.3.2. ⚫ Environmental Bearing Capacity (EBC). This refers to the maximum impacts that

<!-- b000173 | prose | pages [6] -->
human activities make to the environment, otherwise the environment will suffer irreversible damage. In other words, EBC is the threshold of EBQ. For example, when the amount of exhaust emitted exceeds what the environment can afford, the ecosystem is damaged. There are 2 cases of the relationship between EBQ and EBC. When EBQ is less than EBC,  0 , the EBC won’t change in the near future because that is, the difference between them  0 of the ecological stability. However, when EBQ is more than EBC, that is, , the EBC will

<!-- b000174 | prose | pages [6] -->
f  ( ) decrease in the near future because of the irreversible damage, with the damage rate resembling the Sigmoid function. Thus, we have

<!-- b000175 | prose | pages [6] -->
+ 

<!-- b000176 | prose | pages [6] -->
C t

<!-- b000177 | prose | pages [6] -->
( 1)

<!-- b000178 | prose | pages [6] -->
=

<!-- b000179 | prose | pages [6] -->
C t

<!-- b000180 | prose | pages [6] -->
( )

<!-- b000181 | prose | pages [6] -->


<!-- b000182 | furniture | pages [6] -->


<!-- b000183 | prose | pages [6] -->
= = − 

<!-- b000184 | prose | pages [6] -->
C t

<!-- b000185 | prose | pages [6] -->
( )[1

<!-- b000186 | prose | pages [6] -->
f

<!-- b000187 | prose | pages [6] -->
( )]

<!-- b000188 | prose | pages [6] -->
(1)

<!-- b000189 | prose | pages [6] -->
−

<!-- b000190 | prose | pages [6] -->
Q t

<!-- b000191 | prose | pages [6] -->
( )

<!-- b000192 | furniture | pages [6] -->


<!-- b000193 | prose | pages [6] -->
Q t represents the amount of EBC and EBQ in year t respectively, the where C t and ( ) ( ) f  is presented below. expression of ( )

<!-- b000194 | prose | pages [6] -->
= f ( )

<!-- b000195 | furniture | pages [6] -->


<!-- b000196 | prose | pages [6] -->
  1  , 0   e−+ +

<!-- b000197 | prose | pages [6] -->
(2)

<!-- b000198 | prose | pages [6] -->
5   1 1    0,

<!-- b000199 | furniture | pages [6] -->
0

<!-- b000200 | prose | pages [6] -->
 

<!-- b000201 | prose | pages [6] -->
关注数学模型

<!-- b000202 | furniture | pages [6] -->


<!-- b000203 | furniture | pages [6] -->
2

<!-- b000204 | furniture | pages [6] -->
MATHmodels

<!-- b000205 | furniture | pages [6] -->
获取更多资讯

<!-- b000206 | furniture | pages [7] -->
Team # 2016287                                                                                                                                Page  6  of  21

<!-- b000207 | prose | pages [7] -->
f   is shown in Fig.3. And the figure of ( )

<!-- b000208 | furniture | pages [7] -->


<!-- b000209 | prose | pages [7] -->
f  ( )

<!-- b000210 | caption | pages [7] -->
Figure 3: The shape of

<!-- b000211 | heading | pages [7] -->
4.3.1 Environmental Bearing Rate

<!-- b000212 | prose | pages [7] -->
Considering that the relationship between EBC an EBQ can serve as a criterion to EBR judge whether the ecosystem is damaged, Environmental Bearing Rate (EBR) is introduced to simplify the analysis.

<!-- b000213 | prose | pages [7] -->
The EBR is defined as the ratio of EBQ and EBC, which is shown as Eq.3.

<!-- b000214 | prose | pages [7] -->
EBR

<!-- b000215 | furniture | pages [7] -->


<!-- b000216 | prose | pages [7] -->
EBQ =

<!-- b000217 | prose | pages [7] -->
(3)

<!-- b000218 | prose | pages [7] -->
EBC

<!-- b000219 | furniture | pages [7] -->


<!-- b000220 | prose | pages [7] -->
As Section 5.3.2 will mention, EBC and EBQ can be divided into several categories such as water, atmosphere and soil. Thus, the overall EBR is the weighted sum of the ratio, which can be expressed as Eq.4.

<!-- b000221 | prose | pages [7] -->
EBR

<!-- b000222 | furniture | pages [7] -->


<!-- b000223 | prose | pages [7] -->
EBQ

<!-- b000224 | prose | pages [7] -->
n

<!-- b000225 | prose | pages [7] -->
 = = 

<!-- b000226 | prose | pages [7] -->
i

<!-- b000227 | prose | pages [7] -->
(4)

<!-- b000228 | prose | pages [7] -->
W

<!-- b000229 | prose | pages [7] -->
i

<!-- b000230 | prose | pages [7] -->
EBC

<!-- b000231 | furniture | pages [7] -->


<!-- b000232 | prose | pages [7] -->
=

<!-- b000233 | prose | pages [7] -->
i i

<!-- b000234 | prose | pages [7] -->
1

<!-- b000235 | prose | pages [7] -->
i

<!-- b000236 | prose | pages [7] -->
EBC represent the weight, the value of EBQ and the value o EBQ ,and W , where i i i − EBC of the i category respectively. th EBR 1 : This refers to the situation that EBQ is far more less than EBC. When ▪ The ecosystem won’ be damaged, so the EBC won’t change either. The relationship between EBQ and time t at this situation is showed in Fig.4.

<!-- b000237 | prose | pages [7] -->
EBR  : This refers to the situation that EBQ is less than EBC. The 1 When ▪ ecosystem will be slightly damaged, so the EBC will fluctuate but also can be back to normal. The relationship between EBQ and time t at this situation is showed in

<!-- b000238 | caption | pages [7] -->
Fig.4.

<!-- b000239 | prose | pages [7] -->
EBR  : This refers to the situation that EBQ is larger than EBC. The 1 When ▪ ecosystem will be damaged, so the EBC will decline continuously. Then, although people may take actions to decrease the pollution, as the drop of EBC, the value of EBR is still more than 1, and this will create a vicious circle. The relationship among EBQ, EBC and time t at this situation is showed in Fig.4.

<!-- b000240 | furniture | pages [7] -->


<!-- b000241 | caption | pages [7] -->
Figure 4: The relationship among EBQ, EBC and time t when EBR is different

<!-- b000242 | prose | pages [7] -->
To sum up, to safely mitigate the plastic waste without further environmental damage, the value of EBR must be controlled under 1. And the maximum levels of plastic waste refers to the situation when EBR equals 1.

<!-- b000243 | prose | pages [7] -->
关注数学模型

<!-- b000244 | furniture | pages [7] -->
2

<!-- b000245 | furniture | pages [7] -->
MATHmodels

<!-- b000246 | furniture | pages [7] -->
获取更多资讯

<!-- b000247 | furniture | pages [8] -->
Team # 2016287                                                                                                                                Page  7  of  21

<!-- b000248 | heading | pages [8] -->
4.3.2 Environmental Bearing Quantity Measurement

<!-- b000249 | prose | pages [8] -->
Based on the analysis in Section 5.2, we develop some EBQ metrics according to the ways to process the plastic waste, in order to measure the impacts that processing the waste makes to the environment.

<!-- b000250 | prose | pages [8] -->
To embrace a more detailed description of the measurements of EBQ, pay attention to

<!-- b000251 | caption | pages [8] -->
Fig.5.

<!-- b000252 | furniture | pages [8] -->


<!-- b000253 | caption | pages [8] -->
Figure 5: Measurements of EBQ

<!-- b000254 | prose | pages [8] -->
Water Bearing Quantity(WBQ). It refers to the amount of plastic marine debris in a ⚫ period. Study shows that the plastic contamination is threatening marine wildlife[5]. It is estimated by UNEP that marine litter harms over 600 marine species and about 15% of species affected by ingestion & entanglement from marine litter are endangered. And the plastic marine debris is produced by the plastic waste which is discharged into the ocean[5],cf. Eq.5.

<!-- b000255 | prose | pages [8] -->
WBQ

<!-- b000256 | furniture | pages [8] -->


<!-- b000257 | prose | pages [8] -->
= =  + p ( P P ) (5)

<!-- b000258 | furniture | pages [8] -->


<!-- b000259 | prose | pages [8] -->
o b f

<!-- b000260 | prose | pages [8] -->
fP bP and op t refers to the percentage of plastic waste deposited into the ocean, ( ) where represent the annual production of plastic bags and foamed plastic products respectively.

<!-- b000261 | furniture | pages [8] -->


<!-- b000262 | prose | pages [8] -->
⚫ Atmosphere Bearing Quantity(ABQ). It refers to the amount of dioxin and benzene ring

<!-- b000263 | prose | pages [8] -->
compounds produced by burning the plastic waste in a period. The main compound of plastic products is PVC(polyvinyl chloride). The chemical equation in the process can be expressed as Eq.6.

<!-- b000264 | prose | pages [8] -->
5 ( ) → CH CHCl + n O 2 2 n 2

<!-- b000265 | furniture | pages [8] -->


<!-- b000266 | prose | pages [8] -->
+ +  2n CO n H O n HCl

<!-- b000267 | prose | pages [8] -->
(6)

<!-- b000268 | prose | pages [8] -->
2 2

<!-- b000269 | furniture | pages [8] -->


<!-- b000270 | prose | pages [8] -->
During combustion, the polyvinyl chloride will also release highly toxic gas such dioxin and benzene ring compound, which can damage the immune system of animal, interfere with hormones and also cause cancer[6]. What’ more, dioxin and benzene ring compound are produced by the plastic waste which is incinerated, cf. Eq.7.

<!-- b000271 | prose | pages [8] -->
= ABQ ( q

<!-- b000272 | furniture | pages [8] -->


<!-- b000273 | prose | pages [8] -->
d + +   + q ) p ( P P ) (7)

<!-- b000274 | furniture | pages [8] -->


<!-- b000275 | prose | pages [8] -->
b i b f

<!-- b000276 | prose | pages [8] -->
bq refer to the amount of dioxin and benzene ring compounds produced in dq and where

<!-- b000277 | prose | pages [8] -->
ip represents the percentage of plastic waste incinerated. the incineration of plastics, ⚫ Soil Bearing Quantity(SBQ). It refers to the amount of Phthalate and Bisphenol A

<!-- b000278 | prose | pages [8] -->
produced by the decomposition of plastic waste in landfill in a period. When plastic particles break down, additives like phthalates and bisphenol A (BPA) will leach, which will disrupt the hormone systems of animals[7]. Moreover, phthalate and bisphenol A are produced by the plastic waste which is landfilled, cf. Eq.8.

<!-- b000279 | prose | pages [8] -->
= SBQ ( q

<!-- b000280 | furniture | pages [8] -->


<!-- b000281 | prose | pages [8] -->
p + +   + q ) p ( P P ) (8)

<!-- b000282 | furniture | pages [8] -->


<!-- b000283 | prose | pages [8] -->
a l b f

<!-- b000284 | prose | pages [8] -->
关注数学模型

<!-- b000285 | furniture | pages [8] -->
2

<!-- b000286 | furniture | pages [8] -->
MATHmodels

<!-- b000287 | furniture | pages [8] -->
获取更多资讯

<!-- b000288 | furniture | pages [9] -->
Team # 2016287                                                                                                                                Page  8  of  21

<!-- b000289 | prose | pages [9] -->
q and aq refer to the amount of phthalate and bisphenol A produced in the landfill where p

<!-- b000290 | prose | pages [9] -->
lp represents the percentage of plastic waste landfilled. of plastics,

<!-- b000291 | heading | pages [9] -->
4.3.3 Environmental Bearing Capacity Measurement

<!-- b000292 | prose | pages [9] -->
Based on the calculation of ecosystem’s ability to self-recovery, we determine the value of EBC corresponding with the measurement in Section .3.3 ⚫ Water Bearing Capacity (WBC). It refers to the amount of plastic marine debris that

<!-- b000293 | prose | pages [9] -->
people can salvage from the ocean in a period. Considering that the marine wildlife can’t digest and decompose plastic waste, we assume that any amount of plastic marine debris over WBC will damage the ecosystem. Atmosphere Bearing Capacity (ABC). It refers to the amount of dioxin and benzene ⚫ ring compounds that the microorganism can decompose in a period. Research shows that some enzymes existing in the fungus and bacterial are effective in decomposing these toxic gas[8]. Although there may be other ways to decompose them in the environment, we only consider microorganism to simply our model. Thus, we assume that any amount of dioxin and benzene ring compounds over ABC will damage the ecosystem. ⚫ Soil Bearing Capacity (SBC). It refers to the amount of Phthalate and Bisphenol A that

<!-- b000294 | prose | pages [9] -->
the microorganism can decompose in a period. It is similar to what is going on in the description above. And we assume that any amount of dioxin and benzene ring compounds over SBC will damage the ecosystem.

<!-- b000295 | heading | pages [9] -->
4.4 Maximum Levels of Disposable Plastic Product Waste

<!-- b000296 | heading | pages [9] -->
4.4.1 Current Waste Quantity and Capacity

<!-- b000297 | prose | pages [9] -->
Considering that the waste situation is accumulating with time, the total waste in the future definitely equals what the waste currently adding the waste that will increase in a period. Therefore, to better reflect the cumulative nature of waste, Current Waste Quantity (CWQ) and Current Waste Capacity(CWC) are introduced. The calculation of CWQ and CWC be analogized to equations in Section 4.3.2 and Section 4.3.3, with the only difference that the value in the above equations is not what will be in the future, but what is at present. Meanwhile, we can modify our previous equation, Eq.9, to the following format:

<!-- b000298 | prose | pages [9] -->
n

<!-- b000299 | prose | pages [9] -->
 =

<!-- b000300 | prose | pages [9] -->
EBR

<!-- b000301 | furniture | pages [9] -->


<!-- b000302 | prose | pages [9] -->
=

<!-- b000303 | prose | pages [9] -->
i

<!-- b000304 | prose | pages [9] -->
1

<!-- b000305 | prose | pages [9] -->
+

<!-- b000306 | prose | pages [9] -->
EBQ CWQ

<!-- b000307 | prose | pages [9] -->


<!-- b000308 | prose | pages [9] -->
i i

<!-- b000309 | prose | pages [9] -->
(9)

<!-- b000310 | prose | pages [9] -->
W W

<!-- b000311 | prose | pages [9] -->
i i

<!-- b000312 | prose | pages [9] -->
+

<!-- b000313 | prose | pages [9] -->
EBC CWC

<!-- b000314 | furniture | pages [9] -->


<!-- b000315 | prose | pages [9] -->
i i

<!-- b000316 | prose | pages [9] -->
where i (i=1,2,3)represents the measurement in water, atmosphere, or soil, In order to have a specific view of the relationship between the amount of plastic waste and EBR, pay attention to Eq.10.

<!-- b000317 | prose | pages [9] -->
3

<!-- b000318 | prose | pages [9] -->
 =

<!-- b000319 | prose | pages [9] -->
EBR

<!-- b000320 | furniture | pages [9] -->


<!-- b000321 | prose | pages [9] -->
=

<!-- b000322 | prose | pages [9] -->
i

<!-- b000323 | prose | pages [9] -->
1

<!-- b000324 | prose | pages [9] -->
+

<!-- b000325 | prose | pages [9] -->
EBQ CWQ

<!-- b000326 | prose | pages [9] -->


<!-- b000327 | prose | pages [9] -->
i i

<!-- b000328 | prose | pages [9] -->
(10)

<!-- b000329 | prose | pages [9] -->
W W

<!-- b000330 | prose | pages [9] -->
i i

<!-- b000331 | prose | pages [9] -->
+

<!-- b000332 | prose | pages [9] -->
EBC CWC

<!-- b000333 | furniture | pages [9] -->


<!-- b000334 | prose | pages [9] -->
i i

<!-- b000335 | prose | pages [9] -->
When EBR equals 1, we can get the maximum levels of single-use plastic products that can be safely reduced without further environmental damage.

<!-- b000336 | heading | pages [9] -->
5. Reduction of Plastic Waste and the Environmentally Safe

<!-- b000337 | prose | pages [9] -->
Level after Reduction

<!-- b000338 | prose | pages [9] -->
Research shows that plastic waste is exerting great pressure on both ecological environment and human health, among which disposable waste makes the problem even more

<!-- b000339 | prose | pages [9] -->
[2][9]. Given the time constraints, we mainly focus on the single-use plastics. Meanwhile,

<!-- b000340 | prose | pages [9] -->
serious

<!-- b000341 | prose | pages [9] -->
people have made great efforts to limit the production and consumption of disposable plastics nowadays, such as introducing related laws and alternatives. However, the amount of disposable plastic that can be reduced after these trials still remains a question, along with the impact on the environment and human beings.

<!-- b000342 | prose | pages [9] -->
关注数学模型

<!-- b000343 | furniture | pages [9] -->
2

<!-- b000344 | furniture | pages [9] -->
MATHmodels

<!-- b000345 | furniture | pages [9] -->
获取更多资讯

<!-- b000346 | furniture | pages [10] -->
Team # 2016287                                                                                                                                Page  9  of  21

<!-- b000347 | heading | pages [10] -->
5.1 Factors Influencing Plastic Waste Reduction

<!-- b000348 | prose | pages [10] -->
In recent decades, due to the improvement of people's environmental protection awareness and the promotion of the government legislation, the level of disposable plastic waste shows a decreasing trend. How much disposable waste can be reduced, however, remains a complex question, which is closely related to factors like policy, market, etc.

<!-- b000349 | prose | pages [10] -->
According to their roles in plastic waste reduction, influencing factors are divided into two categories: waste production and waste management. Specifically speaking, factors in waste production affect the amount of disposable plastic produced and entering the market; while factors in waste management affect the amount of pollution in plastic waste disposal.

<!-- b000350 | prose | pages [10] -->
What’s more, according to the survey[15], if the policy is effective, the reduction of single- use plastic waste will decreases significantly in the short term, after that, the reduction trend may also rebound.

<!-- b000351 | heading | pages [10] -->
5.1.1 Factors in the Waste Production of Disposable Plastic

<!-- b000352 | prose | pages [10] -->
In this section, factors about waste production will be introduced, including the effectiveness of local policies like bans or taxes, alternatives to plastics, citizen’s environmental protection awareness, supply and demand relationship in the single-use plastic market, etc. What’s more, it is worth noting that most conditions such as demand, policies and even the effectiveness of policies may vary from the degree of local development, geographical conditions and some other regional-specific restraints. ⚫ Ban Policy

<!-- b000353 | prose | pages [10] -->
Ban policy, usually targeted at the production, import, marketing and distribution of non- biodegradable plastic bags, is the most effective way to decrease the plastic waste[2]. Unfortunately, not all countries are suitable for this approach. Take Rwanda and China as examples. After Rwanda implemented its ban policy, although the smuggling of plastics occurred in the beginning, plastic waste decreased significantly in the long run. However, China did so in 1999 and few effects taken on disposable plastic waste. Impact of national bans (based on more than 60 countries experience)[2] shows that the influence of ban policy varies greatly from country to country. That is to say, some countries are suitable for controlling disposable plastic waste through bans, but others are not. And the detailed discussion will be 1x cf. Table 2. presented in Section 4.2. Here we introduce a 0-1 variable

<!-- b000354 | caption | pages [10] -->
Table 2: Selected indictors in terms of ban policy

<!-- b000355 | prose | pages [10] -->
Brief explanation Indicators

<!-- b000356 | prose | pages [10] -->
x =

<!-- b000357 | furniture | pages [10] -->


<!-- b000358 | prose | pages [10] -->
0 , the country is unsuitable for ban policy When 1 1x

<!-- b000359 | prose | pages [10] -->
x = , the country is suitable for ban policy 1 When 1 ⚫ Alternatives

<!-- b000360 | prose | pages [10] -->
Alternatives to plastics, serving as an environmental friendly replacement, are correlated with the price and quantity demanded of the target goods[10]. They include materials like paper and cloth. Although they can’t perfectly replace plastics due to their higher manufacturing costs and inconvenience in some cases, they will still play a positive role in promoting the reduction of disposable plastics under the appropriate policy guidance.

<!-- b000361 | prose | pages [10] -->
Economically, Cross-Price Elasticity of Demand is used to describe the competitive process[11],cf. Eq.11.

<!-- b000362 | prose | pages [10] -->
E

<!-- b000363 | prose | pages [10] -->
ab

<!-- b000364 | furniture | pages [10] -->


<!-- b000365 | prose | pages [10] -->
 Q

<!-- b000366 | prose | pages [10] -->
/

<!-- b000367 | prose | pages [10] -->
Q = 

<!-- b000368 | prose | pages [10] -->
a a

<!-- b000369 | prose | pages [10] -->
(11)

<!-- b000370 | prose | pages [10] -->
P

<!-- b000371 | prose | pages [10] -->
/

<!-- b000372 | prose | pages [10] -->
P

<!-- b000373 | furniture | pages [10] -->


<!-- b000374 | prose | pages [10] -->
b b

<!-- b000375 | prose | pages [10] -->
where 𝐸𝑎𝑏 represents the cross-price elasticity of demand, 𝑄𝑎 refers to the demand change for product 𝑎 and 𝑃𝑏 refers to the price of product 𝑏. Therefore, the supply and demand diagram is shown as follows.

<!-- b000376 | prose | pages [10] -->
关注数学模型

<!-- b000377 | furniture | pages [10] -->
2

<!-- b000378 | furniture | pages [10] -->
MATHmodels

<!-- b000379 | furniture | pages [10] -->
获取更多资讯

<!-- b000380 | furniture | pages [11] -->
Team # 2016287                                                                                                                                Page  10  of  21

<!-- b000381 | prose | pages [11] -->
The Q-P curve

<!-- b000382 | prose | pages [11] -->
Qy

<!-- b000383 | prose | pages [11] -->
Px

<!-- b000384 | furniture | pages [11] -->


<!-- b000385 | caption | pages [11] -->
Figure 6: Q-P curve of the disposable plastic product and its substitute goods

<!-- b000386 | prose | pages [11] -->
Obviously, the demand for single-use plastic products will decrease with the fall of the price of alternatives. To quantify the competitiveness of alternatives in a region, the financial investment by government will also be considered.

<!-- b000387 | prose | pages [11] -->
To sum up, two indicators are selected to measure the competitiveness of alternatives, cf.

<!-- b000388 | caption | pages [11] -->
Table 3.

<!-- b000389 | caption | pages [11] -->
Table 3: Selected indictors in terms of alternatives

<!-- b000390 | prose | pages [11] -->
Brief explanation Indicators

<!-- b000391 | prose | pages [11] -->
Price of Alternatives to Disposable Plastic Products 2x

<!-- b000392 | prose | pages [11] -->
Financial Investment by Government in Alternative Industries 3x ⚫ Environmental Protection Awareness

<!-- b000393 | prose | pages [11] -->
Environmental protection awareness plays an important role in the effectiveness of policies and consuming behaviors in plastics. Study shows that general environmental awareness of citizens may be influenced by the education level received, level of government advocacy, efforts made by social welfare organizations, etc[12]. Considering the uncertainty of other factors, only the first two factors are discussed here. They are the average education level of citizens and the government’s advocation rate on environmental protection.

<!-- b000394 | prose | pages [11] -->
Average education level of citizens counts because there are environmental education courses carried out in universities, colleges, and elementary schools, which will effectively improve citizens' awareness of ecology and environment protection[12]. Also, government’s advocation rate on environmental protection is important because if the government is committed to popularizing the environmental protection knowledge and guiding citizens to ecological consumption[12], it will be easier for people to be environmentally awareness.

<!-- b000395 | prose | pages [11] -->
To sum up, two indicators are selected to measure the level of the environmental protection awareness, cf. Table 4.

<!-- b000396 | caption | pages [11] -->
Table 4: Selected indictors in terms of environmental awareness

<!-- b000397 | prose | pages [11] -->
Brief explanation Indicators

<!-- b000398 | prose | pages [11] -->
Average Education Level of Citizens 4x

<!-- b000399 | prose | pages [11] -->
Government’s Advocation Rate on Environmental Protection 5x ⚫ Tax Policy

<!-- b000400 | prose | pages [11] -->
Tax policy is the most common-used economic incentive[13] to address waste. Up tp June 2019, over 60 countries in the world have taken distinct steps in the form of bans and taxes on single-use plastic products to decrease the plastic waste[14]. Nowadays, there are many kinds of tax system and charges, which vary from region to region. In general, three kinds of tax system are considered. They are production tax, landfill tax and carrier bag charge[13].

<!-- b000401 | prose | pages [11] -->
Production tax is targeted at the manufacturing level and tax on the factories whose amount of plastic products produced exceeds the regulation value. Landfill tax is concentrated on the waste management level and tax on the amount of factories who landfilled plastic waste. Carrier bag charge is focused on the consumption level and tax on single-use plastic packaging.

<!-- b000402 | prose | pages [11] -->
From an economic point of view, we take the effect of the carrier bag charge as an example. We assume that when there is no plastic bags charge, people will use a disposable plastic bag as long as they buy one item.

<!-- b000403 | prose | pages [11] -->
关注数学模型

<!-- b000404 | furniture | pages [11] -->
2

<!-- b000405 | furniture | pages [11] -->
MATHmodels

<!-- b000406 | furniture | pages [11] -->
获取更多资讯

<!-- b000407 | furniture | pages [12] -->
Team # 2016287                                                                                                                                Page  11  of  21

<!-- b000408 | furniture | pages [12] -->


<!-- b000409 | prose | pages [12] -->
Figure 7：The relationship between the amount of single-use plastic bags and items sold.

<!-- b000410 | prose | pages [12] -->
Q represents sales volume of Q represents volume of single-use plastic bags, where 1 items of the supermarket.

<!-- b000411 | prose | pages [12] -->
2

<!-- b000412 | prose | pages [12] -->
When there is plastic bags charge, people may reuse the bags so that the number of plastic bags will decrease.

<!-- b000413 | prose | pages [12] -->
To sum up, three indicators are selected to measure the tax policy, cf. Table 5.

<!-- b000414 | caption | pages [12] -->
Table 5: Selected indictors in terms of tax policy

<!-- b000415 | prose | pages [12] -->
Brief explanation Indicators

<!-- b000416 | prose | pages [12] -->
Production Tax 6x

<!-- b000417 | prose | pages [12] -->
Landfill Tax 7x

<!-- b000418 | prose | pages [12] -->
Carrier Bag Charge 8x

<!-- b000419 | heading | pages [12] -->
5.1.2 Factors in the Waste Management of Disposable Plastic

<!-- b000420 | prose | pages [12] -->
In this section, factors about waste management will be introduced, including the effectiveness of local policies like encouraging the recycling of the plastic waste, increasing subsidies for environment-friendly factories, as well infrastructures like trash bins, plastic incineration plants, etc. ⚫ Recycling Industry Investment

<!-- b000421 | prose | pages [12] -->
Infrastructure will affect the behavior of citizens, which will indirectly influence the recycle rate of disposable plastic. To measure and simplify this relationship, this paper uses the number of trash cans to represent the plastic-relative infrastructure level. To verify the conjecture, we analyzed the correlation of the data by investigating the number of garbage cans and the recycling rate of their disposable garbage in a range of regions or cities.

<!-- b000422 | furniture | pages [12] -->


<!-- b000423 | caption | pages [12] -->
Figure 8: Correlation of recovery rate and garbage can number in ten cities.

<!-- b000424 | prose | pages [12] -->
we can learn from Fig.8  that the Pearson Correlation Coefficient between the number of garbage cans and the recycling rate of disposable garbage was 0.7631, indicating a relatively strong linear relationship between them. What’s more, the government investment are supposed to be considered, since this will determined the future infrastructure level increase[11].

<!-- b000425 | prose | pages [12] -->
To sum up, two indicators are selected to measure the recycling infrastructure level, cf.

<!-- b000426 | caption | pages [12] -->
Table 6.

<!-- b000427 | caption | pages [12] -->
Table 6: Selected indictors in terms of the recycling industry investment

<!-- b000428 | prose | pages [12] -->
Brief explanation Indicators

<!-- b000429 | prose | pages [12] -->
Number of Trash Cans 9x

<!-- b000430 | prose | pages [12] -->
Financial Investment by Government in Recycling Industry x

<!-- b000431 | furniture | pages [12] -->
10

<!-- b000432 | prose | pages [12] -->
关注数学模型

<!-- b000433 | furniture | pages [12] -->
2

<!-- b000434 | furniture | pages [12] -->
MATHmodels

<!-- b000435 | furniture | pages [12] -->
获取更多资讯

<!-- b000436 | furniture | pages [13] -->
Team # 2016287                                                                                                                                Page  12  of  21

<!-- b000437 | prose | pages [13] -->
⚫ Infrastructure Level

<!-- b000438 | prose | pages [13] -->
According to a scientific estimate, almost 79% of the plastic waste produced sits in landfills or in the natural environment such as ocean, while about 12% has been incinerated and only 9% has been recycled[2]. Although the incineration of the plastics will produce lots of toxic gas, we can use chemical methods to decompose them, which makes the harm caused by incineration is far less than that is caused by landfill and uncontrolled deposit.

<!-- b000439 | prose | pages [13] -->
Uncontrolled deposit in ocean is detrimental to the environment, especially the marine environment, as what is discussed in Section 4.2.4. Based on a survey published by UNEP[2], the uneven proportion of different ways of plastic waste management is partially because of the lack of the plastic waste incineration infrastructure, usually measured by the amount of plastic waste incineration plant.

<!-- b000440 | prose | pages [13] -->
The following predictions are made by UNEP, that is, if the amount of the plastic waste incineration plant increases by 50%, the percentage of the plastic waste landfilled or deposited in the environment will decrease greatly[2]. To get an intuitive understanding, the percentage data is presented in the pie chart in Fig.9.

<!-- b000441 | furniture | pages [13] -->


<!-- b000442 | caption | pages [13] -->
Figure 9: Global flow of plastic packaging waste in 2015 and predictions in 2030 when the amount of

<!-- b000443 | prose | pages [13] -->
the plastic waste incineration plant increases by 50% Therefore, by increasing the amount of plastic waste incineration plant, the marine plastic litter may decline greatly, which is beneficial for marine environment.

<!-- b000444 | prose | pages [13] -->
To sum up, one indicator is selected to measure the incineration infrastructure level, cf.

<!-- b000445 | caption | pages [13] -->
Table 7.

<!-- b000446 | caption | pages [13] -->
Table 7: Selected indictors in terms of incineration infrastructure level

<!-- b000447 | prose | pages [13] -->
Brief explanation Indicators

<!-- b000448 | prose | pages [13] -->
Amount of Plastic Waste Incineration Plant x 11

<!-- b000449 | heading | pages [13] -->
5.2 Classification of the Country

<!-- b000450 | prose | pages [13] -->
Although plastic waste is a global issue, the causes behind them may vary from countries, due to some regional-specific constraints. In this section, three categories are considered. They are the degree of economic development, sea-land location and degree of environmental pollution caused by plastics waste.

<!-- b000451 | prose | pages [13] -->
With respect to the degree of economic development, it is closely related to whether the ban policy can be implemented in the country. For developed countries like Denmark and Belgium, ban policies such as banning on the use of single-use plastic bags take effects, cf. Appendix 2. However, in some developing or undeveloped countries like China and Bangladesh, things are different. This is because plastics is a necessity owing to its convenience and low production cost, and banning plastics will certainly require alternatives, whose cost is likely to be higher than plastics. Only when the government provide subsidies to alternatives, can the price of this goes down, leading to the success of ban policy. Therefore, it’s easy to think of that, the wealthier the country is, the more success probability in ban policy.

<!-- b000452 | prose | pages [13] -->
With respect to the sea-land location, it is closely related to whether the amount of plastic waste incineration plant is more important than others. For coastal areas, plastics wastes that isn’t be recycled or incinerated is more likely to be littered into the ocean, which causes irreversible impacts on marine environment. However, for landlocked areas, it is harder to deposit the plastics in ocean.

<!-- b000453 | prose | pages [13] -->
With respect to the degree of environmental pollution caused by plastics waste, it is also closely related to whether the ban policy can be implemented in the country, especially in

<!-- b000454 | prose | pages [13] -->
关注数学模型

<!-- b000455 | furniture | pages [13] -->
2

<!-- b000456 | furniture | pages [13] -->
MATHmodels

<!-- b000457 | furniture | pages [13] -->
获取更多资讯

<!-- b000458 | furniture | pages [14] -->
Team # 2016287                                                                                                                                Page  13  of  21

<!-- b000459 | prose | pages [14] -->
undeveloped countries. If the environmental pollution is extremely serious in the country, the corresponding enforcement will be stricter, which makes the policy more effective. For example, Rwanda, though undeveloped, still managed to replace all the plastic bags with paper bags, cf. Appendix 1.

<!-- b000460 | prose | pages [14] -->
The graphical view of the classification of the country is shown in Fig.10.

<!-- b000461 | furniture | pages [14] -->


<!-- b000462 | caption | pages [14] -->
Figure 10: Cause and effects of the classification of the country

<!-- b000463 | heading | pages [14] -->
5.3 Disposable Plastic Waste Prediction Model

<!-- b000464 | prose | pages [14] -->
Based on the qualitative analysis in Section 6.1, indicators affecting the amount of plastic waste has been extracted. Then, in this section, the quantitative relationship between indicators and the amount of plastic waste will be determined correspondingly. First, PCA (Principle Components Analysis) was applied to decrease the internal correlation. Then, to predict the proportion of disposable plastic waste in total waste, MTSA (Multivariate Time Series Analysis) is used. Finally, the effectiveness of policies with regional-specific constraints was analyzed by comparing the weights of influence factors in different countries.

<!-- b000465 | heading | pages [14] -->
5.3.1 Principal Component Analysis of Influencing Indicators

<!-- b000466 | prose | pages [14] -->
Since there may be strong internal correlation among the 11 indicators, we first conduct principal component analysis on these indicators to realize the dimensionality reduction of date and eliminate the collinearity between variables. The analysis steps are as follows. ⚫ Data normalization

<!-- b000467 | prose | pages [14] -->
Because the units and orders of magnitude of different indicators are greatly different, in order to eliminate this effect, data normalization is done first, which means the value of all data will be converted to the number between 0 and 1 without the units.

<!-- b000468 | prose | pages [14] -->
Let 𝑥𝑖𝑗 denotes the 𝑖𝑡ℎ influencing indicators of the 𝑗𝑡ℎ region[16], cf. Eq.12.

<!-- b000469 | prose | pages [14] -->
= x

<!-- b000470 | prose | pages [14] -->
ij

<!-- b000471 | furniture | pages [14] -->


<!-- b000472 | prose | pages [14] -->
− x x

<!-- b000473 | prose | pages [14] -->
ij

<!-- b000474 | prose | pages [14] -->
jmean

<!-- b000475 | prose | pages [14] -->
(12)

<!-- b000476 | prose | pages [14] -->
s

<!-- b000477 | furniture | pages [14] -->


<!-- b000478 | prose | pages [14] -->
j

<!-- b000479 | prose | pages [14] -->
where 𝑖 = 1,2 … 𝑛, 𝑗= 1,2 … 𝑚. 𝑛 and 𝑚 is the number of indicators and sample areas

<!-- b000480 | prose | pages [14] -->
n n

<!-- b000481 | prose | pages [14] -->
(

<!-- b000482 | prose | pages [14] -->
  = = −

<!-- b000483 | prose | pages [14] -->
x x

<!-- b000484 | prose | pages [14] -->
/ ,

<!-- b000485 | prose | pages [14] -->
n s x x

<!-- b000486 | prose | pages [14] -->
respectively

<!-- b000487 | prose | pages [14] -->
jmean ij j ij inean

<!-- b000488 | prose | pages [14] -->
= =

<!-- b000489 | prose | pages [14] -->
i

<!-- b000490 | prose | pages [14] -->
1

<!-- b000491 | prose | pages [14] -->
i

<!-- b000492 | prose | pages [14] -->
1

<!-- b000493 | prose | pages [14] -->
⚫

<!-- b000494 | prose | pages [14] -->
) ( ) 2

<!-- b000495 | prose | pages [14] -->
−

<!-- b000496 | prose | pages [14] -->
/

<!-- b000497 | prose | pages [14] -->
n

<!-- b000498 | prose | pages [14] -->
1

<!-- b000499 | furniture | pages [14] -->


<!-- b000500 | prose | pages [14] -->
Principal component determination Step 1: Calculate the covariance matrix of the matrix[𝑥𝑖𝑗]𝑛×𝑚. Step 2: Calculate the eigenvalues and normalized eigenvectors of the covariance matrix. Step 3: All principal components are derived from the computed eigenvalues and eigenvectors.

<!-- b000501 | prose | pages [14] -->
=

<!-- b000502 | prose | pages [14] -->
Z

<!-- b000503 | furniture | pages [14] -->


<!-- b000504 | prose | pages [14] -->
i

<!-- b000505 | prose | pages [14] -->
m m

<!-- b000506 | prose | pages [14] -->
C x

<!-- b000507 | furniture | pages [14] -->


<!-- b000508 | prose | pages [14] -->
(13)

<!-- b000509 | prose | pages [14] -->
ij ij

<!-- b000510 | prose | pages [14] -->
= =

<!-- b000511 | prose | pages [14] -->
j j

<!-- b000512 | prose | pages [14] -->
1 1

<!-- b000513 | prose | pages [14] -->
ijc is the( ) where 𝑖= 1,2 … 𝑛, 𝑍𝑖 is 𝑖𝑡ℎ principal component,

<!-- b000514 | prose | pages [14] -->
matrix.

<!-- b000515 | prose | pages [14] -->
,i j  elements of the covariance

<!-- b000516 | prose | pages [14] -->
关注数学模型

<!-- b000517 | furniture | pages [14] -->
2

<!-- b000518 | furniture | pages [14] -->
MATHmodels

<!-- b000519 | furniture | pages [14] -->
获取更多资讯

<!-- b000520 | furniture | pages [15] -->
Team # 2016287                                                                                                                                Page  14  of  21

<!-- b000521 | prose | pages [15] -->
Step 4: Choose the number of principal components by determining whether the cumulative contribution rate is greater than 85%. We suppose that the number is 𝑃[17].

<!-- b000522 | heading | pages [15] -->
5.3.2 Multivariate Time Series Analysis with Principal Component

<!-- b000523 | prose | pages [15] -->
Multivariate time series analysis can not only predict the trend of the target variable, but also give the relationship of horizontal relationship of different variables[18]. Its normal expression is as follow.

<!-- b000524 | prose | pages [15] -->


<!-- b000525 | prose | pages [15] -->
P

<!-- b000526 | prose | pages [15] -->


<!-- b000527 | prose | pages [15] -->
=

<!-- b000528 | prose | pages [15] -->


<!-- b000529 | prose | pages [15] -->
+

<!-- b000530 | prose | pages [15] -->
y

<!-- b000531 | prose | pages [15] -->


<!-- b000532 | prose | pages [15] -->
t

<!-- b000533 | prose | pages [15] -->


<!-- b000534 | prose | pages [15] -->
=

<!-- b000535 | prose | pages [15] -->
k

<!-- b000536 | prose | pages [15] -->
1

<!-- b000537 | furniture | pages [15] -->


<!-- b000538 | furniture | pages [15] -->


<!-- b000539 | prose | pages [15] -->


<!-- b000540 | prose | pages [15] -->


<!-- b000541 | prose | pages [15] -->
= 

<!-- b000542 | prose | pages [15] -->
t

<!-- b000543 | prose | pages [15] -->


<!-- b000544 | prose | pages [15] -->
( ) 

<!-- b000545 | prose | pages [15] -->
( )

<!-- b000546 | prose | pages [15] -->
 

<!-- b000547 | prose | pages [15] -->
B

<!-- b000548 | prose | pages [15] -->
+

<!-- b000549 | prose | pages [15] -->


<!-- b000550 | prose | pages [15] -->
l i

<!-- b000551 | prose | pages [15] -->
B z

<!-- b000552 | prose | pages [15] -->
i

<!-- b000553 | prose | pages [15] -->
( )

<!-- b000554 | prose | pages [15] -->
it t

<!-- b000555 | prose | pages [15] -->
 

<!-- b000556 | prose | pages [15] -->
B

<!-- b000557 | prose | pages [15] -->
i

<!-- b000558 | furniture | pages [15] -->


<!-- b000559 | prose | pages [15] -->
(14)

<!-- b000560 | prose | pages [15] -->
( )

<!-- b000561 | prose | pages [15] -->
 

<!-- b000562 | prose | pages [15] -->
B a

<!-- b000563 | prose | pages [15] -->
i

<!-- b000564 | prose | pages [15] -->
( )

<!-- b000565 | prose | pages [15] -->
t

<!-- b000566 | prose | pages [15] -->
 

<!-- b000567 | prose | pages [15] -->
B

<!-- b000568 | prose | pages [15] -->
i

<!-- b000569 | prose | pages [15] -->
is the polynomial of the autoregressive coefficient of the thi input variable, where i B

<!-- b000570 | prose | pages [15] -->
( )  is the polynomial of the moving average coefficient of the  thi input variable, il is the i B

<!-- b000571 | prose | pages [15] -->
t  is the regression residual sequence, and delay order of the  thi input variable, sequence of zero mean white noise.

<!-- b000572 | prose | pages [15] -->
ta is the

<!-- b000573 | prose | pages [15] -->
These parameters can be estimated by the Maximum Likelihood Method, but the process is rather complex and needs large amount of calculation. Therefore, we choose Multiple Linear Regression and Least Squares Difference Method to simplify it, in which the former can be used to get the relationship of

<!-- b000574 | prose | pages [15] -->
=

<!-- b000575 | prose | pages [15] -->


<!-- b000576 | furniture | pages [15] -->


<!-- b000577 | prose | pages [15] -->
y l l

<!-- b000578 | prose | pages [15] -->
ty  and itx of each year, cf. Eq.15.

<!-- b000579 | prose | pages [15] -->
P

<!-- b000580 | prose | pages [15] -->
+

<!-- b000581 | prose | pages [15] -->


<!-- b000582 | furniture | pages [15] -->


<!-- b000583 | prose | pages [15] -->
(15)

<!-- b000584 | prose | pages [15] -->
x il il

<!-- b000585 | prose | pages [15] -->
=

<!-- b000586 | prose | pages [15] -->
i i

<!-- b000587 | prose | pages [15] -->
1

<!-- b000588 | prose | pages [15] -->
  with the constraint   to estimate Then, using it i

<!-- b000589 | prose | pages [15] -->
Q

<!-- b000590 | prose | pages [15] -->


<!-- b000591 | furniture | pages [15] -->


<!-- b000592 | prose | pages [15] -->
min

<!-- b000593 | prose | pages [15] -->
{

<!-- b000594 | prose | pages [15] -->
=

<!-- b000595 | prose | pages [15] -->
l

<!-- b000596 | prose | pages [15] -->
1

<!-- b000597 | prose | pages [15] -->
−

<!-- b000598 | prose | pages [15] -->
2

<!-- b000599 | furniture | pages [15] -->


<!-- b000600 | prose | pages [15] -->
(16)

<!-- b000601 | prose | pages [15] -->
( (

<!-- b000602 | prose | pages [15] -->
y y y

<!-- b000603 | prose | pages [15] -->
) }

<!-- b000604 | prose | pages [15] -->
l l l

<!-- b000605 | prose | pages [15] -->
where 𝑙 denotes the current year, and Q is the length of statistical time period. At last, ty and itx . we can get the Least Squares Difference relationship between

<!-- b000606 | prose | pages [15] -->
=

<!-- b000607 | prose | pages [15] -->


<!-- b000608 | furniture | pages [15] -->


<!-- b000609 | prose | pages [15] -->
y t t

<!-- b000610 | prose | pages [15] -->
P

<!-- b000611 | prose | pages [15] -->
+

<!-- b000612 | prose | pages [15] -->


<!-- b000613 | furniture | pages [15] -->


<!-- b000614 | prose | pages [15] -->
(17)

<!-- b000615 | prose | pages [15] -->
x it it

<!-- b000616 | prose | pages [15] -->
=

<!-- b000617 | prose | pages [15] -->
i i

<!-- b000618 | prose | pages [15] -->
1

<!-- b000619 | prose | pages [15] -->
itx ,we can predict the targeted variables So, if we can predict the future influence factor

<!-- b000620 | prose | pages [15] -->
ty .

<!-- b000621 | heading | pages [15] -->
5.3.3 Model Application

<!-- b000622 | heading | pages [15] -->
⚫ Results of Principal Component Analysis

<!-- b000623 | prose | pages [15] -->
For the six regions divided according to different standards, nine indicators of 10 regions in different categories were selected for principal component analysis, and the cumulative curve of principal component contribution was shown in Fig.11.

<!-- b000624 | prose | pages [15] -->
关注数学模型

<!-- b000625 | furniture | pages [15] -->


<!-- b000626 | furniture | pages [15] -->
2

<!-- b000627 | furniture | pages [15] -->
MATHmodels

<!-- b000628 | furniture | pages [15] -->
获取更多资讯

<!-- b000629 | furniture | pages [16] -->
Team # 2016287                                                                                                                                Page  15  of  21

<!-- b000630 | caption | pages [16] -->
Figure 11: curve of principal component contribution

<!-- b000631 | prose | pages [16] -->
As can be seen from the figure, in all cases, the sum of contributions of the first three principal components is greater than 85%, so we selected the first three principal components for subsequent analysis. ⚫ Prediction of Disposable Plastic Waste Reduction in Ireland

<!-- b000632 | prose | pages [16] -->
Since disposable plastic bags account for the majority of Ireland's disposable plastic waste[20]. We use the MTSA to predict the proportion of disposable plastic bags in the country's total waste. Using the Multivariate Time Series Analysis, we adapt the data from 2000 to 2010[20], and give the prediction from 2011 to 2015.The results is in Fig.12.

<!-- b000633 | furniture | pages [16] -->


<!-- b000634 | caption | pages [16] -->
Figure 12: The prediction of the proportion of disposable plastic bags in the country's total waste

<!-- b000635 | prose | pages [16] -->
As seen in Fig.12, the predicted data is similar with the official one. In fact, the Relative Mean Square Deviation is just 4.2%, which demonstrates the effectiveness of the model. ⚫ Effectiveness of Policy

<!-- b000636 | prose | pages [16] -->
The effectiveness of policy can be measured by the coefficient of each indicator. If the policy is effective, the reduction of the plastic production will be obvious, reflected in big coefficients. We make predications on the coefficients of some typical countries according to the classification in Section 5.2. and the corresponding radar chart is shown in Fig.13.

<!-- b000637 | furniture | pages [16] -->


<!-- b000638 | caption | pages [16] -->
Figure 13: Comparison of coefficients of indicators between different kinds of countries

<!-- b000639 | prose | pages [16] -->
As shown above, in terms of the incineration indicator, the policy is more effective in coastal countries than landlocked ones. As for the ban policy indicator, the policy is more effective in developed countries than undeveloped ones and in serious pollution countries than in slight ones, which match the analysis in Section 5.2.

<!-- b000640 | heading | pages [16] -->
5.4 Environmentally Safe Level

<!-- b000641 | prose | pages [16] -->
To measure whether the level of the plastic waste after reduction is environmentally safe, two aspects are considered. One aspect is the Environmental Bearing Rate(EBR) mentioned in Section 5.4, which is used to measure the damage that the plastic waste does to the environment. The other one is human-friendly indicator, applied to measure the threat that plastic waste poses to human health.

<!-- b000642 | prose | pages [16] -->
关注数学模型

<!-- b000643 | furniture | pages [16] -->
2

<!-- b000644 | furniture | pages [16] -->
MATHmodels

<!-- b000645 | furniture | pages [16] -->
获取更多资讯

<!-- b000646 | furniture | pages [17] -->
Team # 2016287                                                                                                                                Page  16  of  21

<!-- b000647 | heading | pages [17] -->
5.4.1 Environmental Bearing Rate after Reduction of Plastic Waste

<!-- b000648 | prose | pages [17] -->
The calculation of EBR is based on Eq.10. To get the EBR after the reduction of the plastic waste, the predicted amount of annual plastic production has to substitute the relating variable in Eq.10. Next, based on the analysis in Section 5.4, if the value of EBR is less than 1, then it reaches an environmentally safe level.

<!-- b000649 | heading | pages [17] -->
5.4.2 Human-friendly Indicator

<!-- b000650 | prose | pages [17] -->
The plastic waste is also harmful to human’s health in both direct and indirect ways. In direct ways, people will take in water or air polluted by plastic waste. And in indirect ways, people may intake the toxic chemicals in plastics though food chain. What’s more, because humans are at the top of the food chain, the toxic accumulation is quite high comparing to other animals, which may do great harm to human health. Two ways are showed in Fig.14.

<!-- b000651 | furniture | pages [17] -->


<!-- b000652 | caption | pages [17] -->
Figure 14: Direct and Indirect way that plastic waste harms human health

<!-- b000653 | prose | pages [17] -->
In this section, we mainly focused on the impacts of in the indirect way, because the harm caused by the direct way can be calculated through the previous analysis in environment in Section 6.4.1. Here we propose the Human Risk Index(HRI) to measure the threat that plastic waste poses to human health.

<!-- b000654 | prose | pages [17] -->
More specifically, we consider humans to be on the top of n food chains with m food i grade. And the weight of plastic waste is W kg. Considering the difference in food chains, we iu as the plastic waste absorbed by bottom species, donate R as the transfer efficiency of ij

<!-- b000655 | prose | pages [17] -->
different stages in food chains. And the expression of HRI can be expressed as Eq.18.

<!-- b000656 | prose | pages [17] -->
=

<!-- b000657 | prose | pages [17] -->
HRI

<!-- b000658 | prose | pages [17] -->
ln(

<!-- b000659 | furniture | pages [17] -->


<!-- b000660 | prose | pages [17] -->
m n i

<!-- b000661 | prose | pages [17] -->


<!-- b000662 | prose | pages [17] -->
W u R

<!-- b000663 | prose | pages [17] -->
)

<!-- b000664 | prose | pages [17] -->
(18)

<!-- b000665 | prose | pages [17] -->
i ij

<!-- b000666 | prose | pages [17] -->
= =

<!-- b000667 | prose | pages [17] -->
i

<!-- b000668 | prose | pages [17] -->
1

<!-- b000669 | prose | pages [17] -->
j

<!-- b000670 | prose | pages [17] -->
1

<!-- b000671 | furniture | pages [17] -->


<!-- b000672 | prose | pages [17] -->
If plastic waste can be reduced by a% by prediction, then Eq.19 can modified as follows.

<!-- b000673 | prose | pages [17] -->


<!-- b000674 | prose | pages [17] -->
(

<!-- b000675 | prose | pages [17] -->
=

<!-- b000676 | prose | pages [17] -->
HRI

<!-- b000677 | prose | pages [17] -->
ln 1

<!-- b000678 | prose | pages [17] -->
 

<!-- b000679 | furniture | pages [17] -->


<!-- b000680 | prose | pages [17] -->


<!-- b000681 | prose | pages [17] -->
m n i

<!-- b000682 | prose | pages [17] -->


<!-- b000683 | prose | pages [17] -->
)

<!-- b000684 | prose | pages [17] -->
− −

<!-- b000685 | prose | pages [17] -->
a

<!-- b000686 | prose | pages [17] -->
%

<!-- b000687 | prose | pages [17] -->
W u R

<!-- b000688 | prose | pages [17] -->
(19)

<!-- b000689 | prose | pages [17] -->


<!-- b000690 | prose | pages [17] -->
i ij

<!-- b000691 | prose | pages [17] -->


<!-- b000692 | prose | pages [17] -->
= =

<!-- b000693 | prose | pages [17] -->
i

<!-- b000694 | prose | pages [17] -->
1

<!-- b000695 | prose | pages [17] -->
j

<!-- b000696 | prose | pages [17] -->
1

<!-- b000697 | furniture | pages [17] -->


<!-- b000698 | prose | pages [17] -->
Therefore, with the reduction of plastic waste, HRI will be improved, and the risk of people being harmed by plastic waste will decrease.

<!-- b000699 | heading | pages [17] -->
6. Targets and Impacts for Achieving the Minimal

<!-- b000700 | prose | pages [17] -->
Achievable Level of Global Waste The problem of plastic waste has become a global issue. According to UNEP[2], in 2010, the global plastic waste was 275 million tons, and the amount of mismanaged waste is up to 31.9 million tons, which is at the significant risk of leakage to the environment[2]. Therefore, to protect our Mother Earth, target for global waste of single-use plastic products have to be set. Meanwhile, we are also looking forward to changes in human life, environment and plastic industries after the goals are reached.

<!-- b000701 | prose | pages [17] -->
关注数学模型

<!-- b000702 | furniture | pages [17] -->
2

<!-- b000703 | furniture | pages [17] -->
MATHmodels

<!-- b000704 | furniture | pages [17] -->
获取更多资讯

<!-- b000705 | furniture | pages [18] -->
Team # 2016287                                                                                                                                Page  17  of  21

<!-- b000706 | heading | pages [18] -->
6.1 Targets for Minimal Achievable Level of Global Waste

<!-- b000707 | prose | pages [18] -->
The problem of plastic waste has become a global issue. To set a realistic target to tackle this, we plan to predict the amount of disposable plastic waste in the future, after some policies have been enforced.

<!-- b000708 | prose | pages [18] -->
Firstly, we will use Second Exponential Smoothing Method(SESM) to predict the Global Plastics Production till 2030. Then, based on the regional classification criteria in Section 5.2, all countries will be divided into 6 categories, then, proportion and recycling rate of disposable plastic waste of each category will be estimated. At last, the minimal achievable level of single-use plastic waste will be obtained.

<!-- b000709 | heading | pages [18] -->
6.1.1 Prediction of Global Plastics Production

<!-- b000710 | prose | pages [18] -->
According to the research of UNDP, the amount of global plastic production is predicted to increase in a long period. Therefore, we use the Second Exponential Smoothing Method to establish the Global Plastics Production Prediction Model, cf. Eq.20.

<!-- b000711 | prose | pages [18] -->
= +

<!-- b000712 | prose | pages [18] -->
Y a bT

<!-- b000713 | prose | pages [18] -->
+

<!-- b000714 | prose | pages [18] -->
t T t

<!-- b000715 | prose | pages [18] -->
=

<!-- b000716 | prose | pages [18] -->
(2) (1)

<!-- b000717 | prose | pages [18] -->
S aS

<!-- b000718 | furniture | pages [18] -->


<!-- b000719 | prose | pages [18] -->
t t

<!-- b000720 | prose | pages [18] -->
 =

<!-- b000721 | prose | pages [18] -->
a

<!-- b000722 | prose | pages [18] -->
2

<!-- b000723 | prose | pages [18] -->
S

<!-- b000724 | prose | pages [18] -->


<!-- b000725 | prose | pages [18] -->
t t

<!-- b000726 | prose | pages [18] -->
a

<!-- b000727 | prose | pages [18] -->
=

<!-- b000728 | prose | pages [18] -->
b

<!-- b000729 | prose | pages [18] -->
(

<!-- b000730 | prose | pages [18] -->


<!-- b000731 | prose | pages [18] -->
t

<!-- b000732 | prose | pages [18] -->
− 

<!-- b000733 | prose | pages [18] -->
1

<!-- b000734 | prose | pages [18] -->
a

<!-- b000735 | prose | pages [18] -->
( )1

<!-- b000736 | prose | pages [18] -->
t t

<!-- b000737 | prose | pages [18] -->
+ + −

<!-- b000738 | prose | pages [18] -->
(2)

<!-- b000739 | prose | pages [18] -->
(1

<!-- b000740 | prose | pages [18] -->
a S

<!-- b000741 | prose | pages [18] -->
)

<!-- b000742 | furniture | pages [18] -->


<!-- b000743 | prose | pages [18] -->
(20)

<!-- b000744 | prose | pages [18] -->
−

<!-- b000745 | prose | pages [18] -->
t

<!-- b000746 | prose | pages [18] -->
1

<!-- b000747 | prose | pages [18] -->
+

<!-- b000748 | prose | pages [18] -->
(1) (1) (2)

<!-- b000749 | prose | pages [18] -->
S

<!-- b000750 | prose | pages [18] -->
t

<!-- b000751 | prose | pages [18] -->
−

<!-- b000752 | prose | pages [18] -->
(1) (2)

<!-- b000753 | prose | pages [18] -->
S S S

<!-- b000754 | prose | pages [18] -->
)

<!-- b000755 | prose | pages [18] -->
t t t

<!-- b000756 | prose | pages [18] -->
( ) 2 is smooth value of the primary index, where tS is the smooth value of the second tS

<!-- b000757 | prose | pages [18] -->
Y +  is the predicted global plastics production of tht  year. Results are shown in index and t T

<!-- b000758 | caption | pages [18] -->
Fig. 15.

<!-- b000759 | furniture | pages [18] -->


<!-- b000760 | caption | pages [18] -->
Figure 15: The prediction of global plastics production

<!-- b000761 | heading | pages [18] -->
6.1.2 Prediction of Disposable Plastic Waste Proportion

<!-- b000762 | prose | pages [18] -->
According Section 6.2, countries are divided into 6 categories. With multivariate time series model, we obtained the prediction of the proportion of disposable plastics in Fig.16.

<!-- b000763 | prose | pages [18] -->
关注数学模型

<!-- b000764 | furniture | pages [18] -->


<!-- b000765 | furniture | pages [18] -->
2

<!-- b000766 | furniture | pages [18] -->
MATHmodels

<!-- b000767 | furniture | pages [18] -->
获取更多资讯

<!-- b000768 | furniture | pages [19] -->
Team # 2016287                                                                                                                                Page  18  of  21

<!-- b000769 | caption | pages [19] -->
Figure 16: The predicted proportion of disposable plastic waste in different regions

<!-- b000770 | prose | pages [19] -->
Then we combine them with Entropy weight method to make the prediction.

<!-- b000771 | heading | pages [19] -->
6.1.3 Result of Achievable Level of Disposable Plastic Waste

<!-- b000772 | prose | pages [19] -->
⚫ Annual Amount of Production of Disposable Plastic Waste The production of disposable plastic waste is demonstrated in Fig. 17.

<!-- b000773 | furniture | pages [19] -->


<!-- b000774 | caption | pages [19] -->
Figure 17: The prediction of global disposable plastic waste and its proportion in global waste

<!-- b000775 | prose | pages [19] -->
Therefore, we set the targeted level as 15.88 Million tones, based on the assumption that policy of limiting disposable plastic won’t change in the next ten years.

<!-- b000776 | prose | pages [19] -->
⚫ Percentage of Ways of Plastic Waste Management Due to the policy of increasing the number of plastic waste incineration plants, the percentage of the two ways of waste management will change in the future, cf.Fig18

<!-- b000777 | furniture | pages [19] -->


<!-- b000778 | caption | pages [19] -->
Figure 18: The percentage of two ways of plastic waste management

<!-- b000779 | prose | pages [19] -->
Therefore, we set the targeted percentage of plastics into ocean declining to 18% and the percentage of plastics incinerated increasing to 65%.

<!-- b000780 | heading | pages [19] -->
6.2 Impacts for Achieving the Minimal Achievable Level of

<!-- b000781 | prose | pages [19] -->
Global Waste

<!-- b000782 | prose | pages [19] -->
If the target of 15.88 million tons is reached, there will be profound impact on wide range of our world, including the human life, the environment and the plastic industry.

<!-- b000783 | prose | pages [19] -->
To get a better understanding of the impacts, cf. Fig 19.

<!-- b000784 | prose | pages [19] -->
关注数学模型

<!-- b000785 | furniture | pages [19] -->
2

<!-- b000786 | furniture | pages [19] -->
MATHmodels

<!-- b000787 | furniture | pages [19] -->
获取更多资讯

<!-- b000788 | furniture | pages [20] -->
Team # 2016287                                                                                                                                Page  19  of  21

<!-- b000789 | furniture | pages [20] -->


<!-- b000790 | caption | pages [20] -->
Figure 19: Impacts on the human life, environment and plastic industry

<!-- b000791 | heading | pages [20] -->
6.2.1 Impacts on Human Life

<!-- b000792 | prose | pages [20] -->
Based on Section 6.1, the factors can be divided into 2 categories. From the aspect of 3x ) will lead to the plastic waste production, the financial investment to alternative industry(

<!-- b000793 | prose | pages [20] -->
2x ). Meanwhile, the price of single-use plastic products decrease of the price of substitutes(

<!-- b000794 | prose | pages [20] -->
8x ) and the production tax on the production( will rise due to the carrier bag charge( 6x ) of plastic. Therefore, according to Q-P curve in Fig.6, the consumption of single-use products 5x ). It is will decline, also due to the government’s advocation on environmental protection( estimated that by that time, most people will use paper or cloth bags instead of plastic ones.

<!-- b000795 | heading | pages [20] -->
6.2.2 Impacts on the Environment

<!-- b000796 | prose | pages [20] -->
In analogy to analysis in Section 7.2.1, from the aspect of plastic waste production, if these policies such as ban, tax, alternatives (factors x x x ) are effective, the amount of production 1 1 9 will decrease by 55%. From the aspect of plastic waste management, the financial investment x ) will increase the percentage of recycling, which lead to 47% decline of toxic in recycling( 10

<!-- b000797 | prose | pages [20] -->
x ), the percentage of depositing the exhaust. What’s more, with the rise of incineration plant( 11 waste in the ocean will decline to 12%, which is good for marine life.

<!-- b000798 | heading | pages [20] -->
6.2.3 Impacts on the Plastic Industry

<!-- b000799 | prose | pages [20] -->
Although the government's policies on enterprises are not the same in the short term, they will all lead to a reduction in the production of disposable plastics in the long run. In addition, with the increase of peoples' environmental awareness and government ’s supervision, the production of disposable plastics will be gradually reduced, and many companies may face bankruptcy and transformation.

<!-- b000800 | heading | pages [20] -->
7. Equity Issues and Solutions

<!-- b000801 | prose | pages [20] -->
The pollution caused by disposable plastics is a global problem, but the distribution of mismanaged waste varies significantly among countries, cf. Fig.20.

<!-- b000802 | prose | pages [20] -->
关注数学模型

<!-- b000803 | furniture | pages [20] -->
2

<!-- b000804 | furniture | pages [20] -->
MATHmodels

<!-- b000805 | furniture | pages [20] -->
获取更多资讯

<!-- b000806 | furniture | pages [21] -->
Team # 2016287                                                                                                                                Page  20  of  21

<!-- b000807 | furniture | pages [21] -->


<!-- b000808 | caption | pages [21] -->
Figure 20: The distribution  of mismanaged waste around the world, 2010

<!-- b000809 | prose | pages [21] -->
As shown above, the share of mismanaged waste in China is 27.7%, while that in some countries is less than 0.1 %, which shows inequity in plastic wastes. This is a visual description.

<!-- b000810 | heading | pages [21] -->
7.1 Equity Issues

<!-- b000811 | prose | pages [21] -->
The reasons that cause equity issues can be divided into two aspects[19]. One is the difference in the generation of waste or pollution. The other is the difference in the economic expenditure of disposable waste. And the corresponding solutions will be introduced next.

<!-- b000812 | heading | pages [21] -->
7.2 Solutions to Equity Issues

<!-- b000813 | prose | pages [21] -->
After analyzing the equity issues caused by disposable plastic waste, the following schemes are proposed. ⚫ License for the Plastic Waste

<!-- b000814 | prose | pages [21] -->
The first solution is to introduce a license that only permits for certain amount of plastic waste according to population and economic levels of the country.

<!-- b000815 | prose | pages [21] -->
Not only can the license regulate the total amount of plastic waste, but also circulate between countries as a commodity. Countries that able to decrease the production of plastic waste can sell their licenses to those that can’t in the short term. In this way, countries with high share of mismanaged waste can compensate the ones with low share.  What’s more. considering that the production of excess plastic waste may increase the cost, countries will consider reducing their waste production. ⚫ Clarification of Inter-state Property Rights

<!-- b000816 | prose | pages [21] -->
The second solution is to clarify of property rights of environmental resources. Economically, the equity issue is partly caused by the ambiguity of the ownership of the property rights in environmental resources. According to Coase's theorem[19], without the negotiation cost, as long as the resource allocation is clear, the market will reach the most effective configuration. Therefore, the clarification of property rights of environmental resources is helpful to solve the issue. ⚫ Seeking International Cooperation

<!-- b000817 | prose | pages [21] -->
The third solution is to combine experts and professional organizations in various fields worldwide to develop more practical solutions to protect the environment[19]. ⚫ Strengthening international legislation

<!-- b000818 | prose | pages [21] -->
The fourth solution is to enhance the effectiveness of global policies can help solve the equity issues, considering that the intensity of policy implementation will affect the effectiveness of policies to some extent.

<!-- b000819 | heading | pages [21] -->
8. Sensitivity Analysis

<!-- b000820 | heading | pages [21] -->
8.1 Rotation Estimation for Multivariate Time Series Model

<!-- b000821 | prose | pages [21] -->
Since we use the data of different regions to construct the Multivariate Time Series Model Based on Principal Component Analysis, rotation estimation will be applied to make sure that the model is well-adapted. Since 10-fold cross validation is the most commonly used

<!-- b000822 | prose | pages [21] -->
关注数学模型

<!-- b000823 | furniture | pages [21] -->
2

<!-- b000824 | furniture | pages [21] -->
MATHmodels

<!-- b000825 | furniture | pages [21] -->
获取更多资讯

<!-- b000826 | furniture | pages [22] -->
Team # 2016287                                                                                                                                Page  21  of  21

<!-- b000827 | prose | pages [22] -->
method. we randomly partition the data of 10 regions into tenths, and for each tenth, the remaining nine are used to calculate its Mean Square Error.

<!-- b000828 | furniture | pages [22] -->


<!-- b000829 | caption | pages [22] -->
Figure 21: Error contrast                                          Figure 22: Gaussian Noise Curve

<!-- b000830 | prose | pages [22] -->
As shown in Fig.21, the Cross-Validation Error is only slightly higher than the Testing Set Error, demonstrating the robustness of the model.

<!-- b000831 | heading | pages [22] -->
8.2 Gaussian Noise

<!-- b000832 | prose | pages [22] -->
In setting a minimum target for the world's single-use plastic waste, we used the historical amount of production of global waste. However, we found the data is slightly different because it comes from different sources, which could lead to inaccuracy of the input data. And this may bring some deviations to the results of our model. Therefore, to verify the stability of our Global Garbage Forecasting Model, we add some gaussian noise to the input data to see how the relative deviation of results changes with the standard deviation increasing, cf. Fig.22.

<!-- b000833 | prose | pages [22] -->
It can be seen that when the standard deviation of gaussian noise is no more than 0.6, the relative deviation of the results does not exceed 20%, showing the robustness of our model.

<!-- b000834 | heading | pages [22] -->
9. Evaluation of the Model

<!-- b000835 | heading | pages [22] -->
9.1 Strength

<!-- b000836 | prose | pages [22] -->
⚫ The data are from official website and official journal, which is relatively rigorous.

<!-- b000837 | prose | pages [22] -->
Considering the changes in the environment, our model is extensible and can add new ⚫ environment variables to get accurate results. Through the combination of the established mathematical model and the knowledge of ⚫ economics, we have proposed feasible solutions to equity issues caused by the disposable plastic products. Lots of factors are taken into account ranging from economics to social behavior, ⚫ Therefore, we have obtained a reliable result.

<!-- b000838 | heading | pages [22] -->
9.2 Weakness

<!-- b000839 | prose | pages [22] -->
⚫ Although we try to use appropriate methods to deal with missing values, the lack of real

<!-- b000840 | prose | pages [22] -->
data still affects the model. ⚫ Our model does not take the natural disasters into account, so there is bias in our analysis.

<!-- b000841 | prose | pages [22] -->
关注数学模型

<!-- b000842 | furniture | pages [22] -->
2

<!-- b000843 | furniture | pages [22] -->
MATHmodels

<!-- b000844 | furniture | pages [22] -->
获取更多资讯

<!-- b000845 | heading | pages [23] -->
MEMO

<!-- b000846 | furniture | pages [23] -->


<!-- b000847 | prose | pages [23] -->
From: Team  2016287, ICM 2020

<!-- b000848 | prose | pages [23] -->
To: the International Council of Plastic Waste Management(ICM)

<!-- b000849 | prose | pages [23] -->
Date: February 17, 2020

<!-- b000850 | prose | pages [23] -->
Subject: Realistic global target of single-use plastic waste

<!-- b000851 | furniture | pages [23] -->


<!-- b000852 | prose | pages [23] -->
Dear ICM, we are honored to describe the realistic global target of single-use plastic waste for you.

<!-- b000853 | furniture | pages [23] -->


<!-- b000854 | prose | pages [23] -->
After the careful study of global single-use plastic product waste and policies, we get the following results. First, a realistic target for the annual amount of production of global single- use plastics in 2030 is 15.88 Million tones, with the percentage of plastics into ocean declining to 18% and the percentage of plastics incinerated increasing to 65%. To reach the target, considering the regional-specific constraints, different countries should enforce different policies.

<!-- b000855 | furniture | pages [23] -->


<!-- b000856 | prose | pages [23] -->
We divided the countries into 6 categories. Here we provide advice for three of them.

<!-- b000857 | furniture | pages [23] -->


<!-- b000858 | prose | pages [23] -->
▪ For developed and coastal countries, we suggest they focus on the ban policy about plastic bags, alternatives to plastics and building more plastic incineration plants to decrease the amount of plastic into the ocean.

<!-- b000859 | furniture | pages [23] -->


<!-- b000860 | prose | pages [23] -->
▪ For developing and coastal countries, we suggest they focus on the tax policies including the landfill tax, production tax and carrying bag charge. Also, they should pay attention to the plastic incineration plants.

<!-- b000861 | furniture | pages [23] -->


<!-- b000862 | prose | pages [23] -->
▪ For undeveloped and severely polluted countries, we suggest they focus on the ban policy, alternatives to plastics and the improvement of people’s environmental protection awareness.

<!-- b000863 | furniture | pages [23] -->


<!-- b000864 | prose | pages [23] -->
Second, the target that we set is environmentally safe. In 2030, the reduction of plastic waste will have profound impact in the wide range of our world, including the human life, the environment and the plastic industry. At that time, with the improvement of environmental protection awareness, people will use cloth bags or paper bags more frequently, rather than plastic bags. Due to the ban policy, many traditional plastic companies may face a fate of transformation or bankruptcy. Instead, some high-tech companies that produce biodegradable plastics will rise and replace most of the traditional ones. All of these are good for both environment and human beings. With the decrease of plastic debris in ocean, marine wildlife such as sea turtle and seagull will be prevented from digesting plastics, which is beneficial for marine ecosystem. As for the human beings, we can take in food with less chemicals in plastic accumulated in the food chain, which will extend the life span of human beings.

<!-- b000865 | furniture | pages [23] -->


<!-- b000866 | prose | pages [23] -->
Third, although the vision of the target is wonderful, there may be some obstacles in the process. The timeline of our target is 10 years. According to the previous data and the prediction of our model, in the first 2 years, the effects of the policies may not be as good as we expect. Due to the low cost and inconvenience of the single-use plastic products, most people will feel uncomfortable when the carrier bags are charged or they have to use paper or cloth bags. Feelings of resistance may appear among people and this may hinder the enforcement of policies. However, in the 3rd to 8th year, the situation begins to change. With the embedding of the environmental protection awareness, people start to realize the importance of the Mother Earth and harm brought by the single-use plastic waste. Then, they begin to obey these policies and try a greener lifestyle. That’s when the amount of production of single-use plastic products

<!-- b000867 | prose | pages [23] -->
关注数学模型

<!-- b000868 | furniture | pages [23] -->
2

<!-- b000869 | furniture | pages [23] -->
MATHmodels

<!-- b000870 | furniture | pages [23] -->
获取更多资讯

<!-- b000871 | prose | pages [24] -->
decline most rapidly. And the environment is improved to a great extend. In the last two years, most people are accustomed to green life and the market share of single-use plastics and alternatives is relatively fixed. Therefore, the amount of production of single-use plastics decrease slowly and finally reaches the target of 15.88 million tones at the end of 2030.

<!-- b000872 | furniture | pages [24] -->


<!-- b000873 | furniture | pages [24] -->


<!-- b000874 | prose | pages [24] -->
Despite what is mentioned above, our team has to remind you that there are some other circumstances that may accelerate or hinder the achievement of the target.

<!-- b000875 | furniture | pages [24] -->


<!-- b000876 | furniture | pages [24] -->


<!-- b000877 | prose | pages [24] -->
Other circumstances that may accelerate the achievement of the target are as follows:

<!-- b000878 | furniture | pages [24] -->


<!-- b000879 | prose | pages [24] -->
▪ The price of crude oil is on the rise. It is because crude oil serves as the raw material of the single-use plastics. And the price of the plastics will increase along with it. According to the theory of Supply and Demand economically, the plastics will become less competitive to alternatives, thus accelerating the achievement of the target.

<!-- b000880 | furniture | pages [24] -->


<!-- b000881 | prose | pages [24] -->
▪ Alternatives like biodegradable materials have a big breakthrough in technology. This will promote mass production and lead to the drop in the cost, which makes it more competitive in the market and replace the single-use plastics more rapidly.

<!-- b000882 | furniture | pages [24] -->


<!-- b000883 | prose | pages [24] -->
Other circumstances that may hinder the achievement of the target are as follows:

<!-- b000884 | furniture | pages [24] -->


<!-- b000885 | prose | pages [24] -->
▪ The law enforcement in a country is not strong enough. If so, even though a strict law is enacted, it is still difficult to control the production of plastics. Take the country, Bangladesh as an example, although strict limits had been released on plastic, the single-use plastic waste has not declined significantly.

<!-- b000886 | furniture | pages [24] -->


<!-- b000887 | prose | pages [24] -->
▪ Countries don’t take on their own international responsibilities and don’t join agreements on reduction of the production of the single-use plastics. If so, the plastic industry in these countries may flourish uncontrollably, making it extremely difficult to meet global targets. What’s more, it also does harm to the equity issue among countries.

<!-- b000888 | furniture | pages [24] -->


<!-- b000889 | prose | pages [24] -->
We hope that our analysis will help you to tackle the plastic waste problem in the future. And we draw a poster to send our best wishes to the world.

<!-- b000890 | furniture | pages [24] -->


<!-- b000891 | furniture | pages [24] -->


<!-- b000892 | prose | pages [24] -->
Yours Sincerely,

<!-- b000893 | furniture | pages [24] -->
Team # 2016287

<!-- b000894 | furniture | pages [24] -->


<!-- b000895 | prose | pages [24] -->
关注数学模型

<!-- b000896 | furniture | pages [24] -->
2

<!-- b000897 | furniture | pages [24] -->
MATHmodels

<!-- b000898 | furniture | pages [24] -->
获取更多资讯

<!-- b000899 | heading | pages [25] -->
References

<!-- b000900 | references | pages [25] -->
[1] Geyer, R., Jambeck, J. R., & Law, K. L. (2017). Production, use, and fate of all plastics

<!-- b000901 | references | pages [25] -->
ever made. Science Advances, 3(7), e1700782.

<!-- b000902 | references | pages [25] -->
[2] UN environment, SINGLE-USE PLASTICSA Roadmap for Sustainability

<!-- b000903 | references | pages [25] -->
[3] Kara Lavender Law, Plastics in the Marine Environment, Sea Education Association,

<!-- b000904 | references | pages [25] -->
Woods Hole, Massachusetts 02543;

<!-- b000905 | references | pages [25] -->
[4] Jianwu, T., & Wenhu, Y. (1998). Study on environmental bearing capacity and its

<!-- b000906 | references | pages [25] -->
quantification.[J]. China Environmental Science, 3.

<!-- b000907 | references | pages [25] -->
[5] Li, W. C., Tse, H. F., & Fok, L. (2016). Plastic waste in the marine environment: A

<!-- b000908 | references | pages [25] -->
review of sources, occurrence and effects. Science of the Total Environment, 566, 333-349.

<!-- b000909 | references | pages [25] -->
[6] Ahlborg, U. G., Becking, G. C., Birnbaum, L. S., Brouwer, A. A., Derks, H. J. G. M.,

<!-- b000910 | references | pages [25] -->
Feeley, M., ... & Safe, S. H. (1994). Toxic equivalency factors for dioxin-like

<!-- b000911 | references | pages [25] -->
PCBs. Chemosphere, 28(6), 1049-1068.

<!-- b000912 | references | pages [25] -->
[7] Forschungsverbund Berlin. (2018, February 5). An underestimated threat: Land-based

<!-- b000913 | references | pages [25] -->
pollution with microplastics. ScienceDaily. Retrieved February 14, 2020 from

<!-- b000914 | references | pages [25] -->
www.sciencedaily.com/releases/2018/02/180205125728.htm

<!-- b000915 | references | pages [25] -->
[8] Hu, Y., Zhang, P., Chen, D., Zhou, B., Li, J., & Li, X. W. (2012). Hydrothermal treatment

<!-- b000916 | references | pages [25] -->
of municipal solid waste incineration fly ash for dioxin decomposition. Journal of hazardous

<!-- b000917 | references | pages [25] -->
materials, 207, 79-85.

<!-- b000918 | references | pages [25] -->
[9] Galloway T.S. (2015) Micro- and Nano-plastics and Human Health. In: Bergmann M.,

<!-- b000919 | references | pages [25] -->
Gutow L., Klages M. (eds) Marine Anthropogenic Litter.

<!-- b000920 | references | pages [25] -->
[10] https://en.wikipedia.org/wiki/Substitute_good

<!-- b000921 | references | pages [25] -->
[11] https://en.wikipedia.org/wiki/Market_(economics)

<!-- b000922 | references | pages [25] -->
[12] Wang Weiwei. Cultivation of Chinese citizens' ecological and environmental protection

<!-- b000923 | references | pages [25] -->
awareness from the perspective of ecological culture [D] .Bohai University, 2017.

<!-- b000924 | references | pages [25] -->
[13] Treasury, H. M. (2018). Tackling the Plastic Problem. Using the Tax System or Charges

<!-- b000925 | references | pages [25] -->
to Address Single-Use Plastic Waste.

<!-- b000926 | references | pages [25] -->
[14] https://www.azocleantech.com/article.aspx?ArticleID=928

<!-- b000927 | references | pages [25] -->
[15] Liao Qin, Wang Jinping, Wang Fang. International Single-use Plastic Pollution Control

<!-- b000928 | references | pages [25] -->
Policy and Its Implications for China [J]. Global Economic Outlook,2018,33(07):63-71.

<!-- b000929 | references | pages [25] -->
[16] Wei-Xiang XU, Quan-shou ZHANG. An Algorithm of Meta-Synthesis Based on the

<!-- b000930 | references | pages [25] -->
Grey The- ory and Fuzzy Mathematics [J].Systems engineering theory and practice, 2001,(4):

<!-- b000931 | references | pages [25] -->
114-119

<!-- b000932 | references | pages [25] -->
[17] Westerhuis J A , Kourti T , Macgregor J F . Analysis of multiblock and hierarchical PCA

<!-- b000933 | references | pages [25] -->
and PLS models[J]. Journal of Chemometrics, 1998, 12(5):301-321.

<!-- b000934 | references | pages [25] -->
[18] Chan, N. H. . (1973). Multivariate Time Series. Time Series: Applications to Finance

<!-- b000935 | references | pages [25] -->
with R and S-Plus, Second Edition. John Wiley & Sons, Inc.

<!-- b000936 | references | pages [25] -->
[19] Dawei He, Jingsheng Chen On the International Law Solution to Transnational Pollution

<!-- b000937 | references | pages [25] -->
from the Perspetive of Efficiency and Equity (Department of Urban and Environmental

<!-- b000938 | references | pages [25] -->
Sciences, Peking University, Beijing 100871)

<!-- b000939 | references | pages [25] -->
[20] The Litter Monitoring Body. The National Litter Pollution Monitoring System: Systems

<!-- b000940 | references | pages [25] -->
Survey Report 2015[R/OL].(2016-04-26)[2017-11-16].

<!-- b000941 | heading | pages [25] -->
Appendix

<!-- b000942 | prose | pages [25] -->
Appendix 1: Ban policies of some countries

<!-- b000943 | heading | pages [25] -->
Appendix 2: Ban policies of some countries

<!-- b000944 | prose | pages [25] -->
Country Year Policy Impact Belgium 2016 Ban on the use of single-use

<!-- b000945 | prose | pages [25] -->
Over time, plastic bags were replaced

<!-- b000946 | prose | pages [25] -->
plastic bags in Wallonia.

<!-- b000947 | prose | pages [25] -->
by paper bags.

<!-- b000948 | prose | pages [25] -->
Exception of thin compostable bags for foods

<!-- b000949 | prose | pages [25] -->
that can be moist, until the

<!-- b000950 | prose | pages [25] -->
end of 2018 (Surfrider Foundation Europe, 2017).

<!-- b000951 | prose | pages [25] -->
关注数学模型

<!-- b000952 | furniture | pages [25] -->
2

<!-- b000953 | furniture | pages [25] -->
MATHmodels

<!-- b000954 | furniture | pages [25] -->
获取更多资讯

<!-- b000955 | prose | pages [26] -->
2008 Ban on non-biodegradable China plastic bags <25 μ

<!-- b000956 | prose | pages [26] -->
Ban has been ineffectively enforced in food markets and among small retailers. (Xanthos, 2017). Bangladesh 2002 Ban on polyethylene plastic

<!-- b000957 | prose | pages [26] -->
bags.

<!-- b000958 | prose | pages [26] -->
Initial positive response from the public. Use of plastic bags increased after some years due to lack of enforcement and absence of cost- effective alternatives (IRIN, 2011). 2008 Ban on the production, use, Rwanda

<!-- b000959 | prose | pages [26] -->
In the first phase the ban resulted in

<!-- b000960 | prose | pages [26] -->
importation and sale of all polyethylene bags.

<!-- b000961 | prose | pages [26] -->
a black market for plastic bags. Over time, plastic bags were replaced by paper bags (Clavel, 2014; Pilgrim, 2016).

<!-- b000962 | prose | pages [26] -->
关注数学模型

<!-- b000963 | furniture | pages [26] -->
2

<!-- b000964 | furniture | pages [26] -->
MATHmodels

<!-- b000965 | furniture | pages [26] -->
获取更多资讯

<!-- b000966 | prose | pages [27] -->
Appendix 2: Main Code

<!-- b000967 | prose | pages [27] -->
alpha=0.3;

<!-- b000968 | prose | pages [27] -->
beta=0.3;

<!-- b000969 | prose | pages [27] -->
gamma=0.5;

<!-- b000970 | prose | pages [27] -->
fc=12;

<!-- b000971 | prose | pages [27] -->
k=12;

<!-- b000972 | prose | pages [27] -->
%%

<!-- b000973 | prose | pages [27] -->
X=load('passengers.txt');

<!-- b000974 | prose | pages [27] -->
S=reshape(X,[144,1]);

<!-- b000975 | prose | pages [27] -->
plot(S,'r');

<!-- b000976 | prose | pages [27] -->
n=length(S);

<!-- b000977 | prose | pages [27] -->
a(1)=sum(S(1:k))/k;

<!-- b000978 | prose | pages [27] -->
b(1)=(sum(S(k+1:2*k))-sum(S(1:k)))/k^2;

<!-- b000979 | prose | pages [27] -->
s=S-a(1);

<!-- b000980 | prose | pages [27] -->
y=a(1)+b(1)+s(1);

<!-- b000981 | furniture | pages [27] -->


<!-- b000982 | prose | pages [27] -->
f=zeros(144,1);

<!-- b000983 | prose | pages [27] -->
for i=1:n+fc

<!-- b000984 | prose | pages [27] -->
if i==length(S)

<!-- b000985 | prose | pages [27] -->
S(i+1)=a(end)+b(end)+s(end-k+1);

<!-- b000986 | prose | pages [27] -->
end

<!-- b000987 | prose | pages [27] -->
a(i+1)=alpha*(S(i)-s(i))+(1-alpha)*(a(i)+b(i));

<!-- b000988 | prose | pages [27] -->
b(i+1)=beta*(a(i+1)-a(i))+(1-beta)*b(i);%

<!-- b000989 | prose | pages [27] -->
s(i+1)=gamma*(S(i)-a(i)-b(i))+(1-gamma)*s(i);%

<!-- b000990 | prose | pages [27] -->
y(i+1)=a(i+1)+b(i+1)+s(i+1);

<!-- b000991 | prose | pages [27] -->
end

<!-- b000992 | furniture | pages [27] -->


<!-- b000993 | prose | pages [27] -->
hold on

<!-- b000994 | prose | pages [27] -->
plot(y,'b');

<!-- b000995 | prose | pages [27] -->
hold off

<!-- b000996 | prose | pages [27] -->
关注数学模型

<!-- b000997 | furniture | pages [27] -->
2

<!-- b000998 | furniture | pages [27] -->
MATHmodels

<!-- b000999 | furniture | pages [27] -->
获取更多资讯
