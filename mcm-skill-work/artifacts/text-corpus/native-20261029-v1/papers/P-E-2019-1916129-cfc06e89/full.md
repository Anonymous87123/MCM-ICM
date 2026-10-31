# P-E-2019-1916129-cfc06e89

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->
Team Control Number

<!-- b000006 | prose | pages [1] -->
For office use only

<!-- b000007 | prose | pages [1] -->
For office use only

<!-- b000008 | prose | pages [1] -->
1916129

<!-- b000009 | prose | pages [1] -->
T1 ________________

<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | prose | pages [1] -->
T2 ________________

<!-- b000012 | prose | pages [1] -->
F1 ________________

<!-- b000013 | prose | pages [1] -->
F2 ________________

<!-- b000014 | prose | pages [1] -->
F3 ________________

<!-- b000015 | prose | pages [1] -->
Problem Chosen

<!-- b000016 | prose | pages [1] -->
T3 ________________

<!-- b000017 | prose | pages [1] -->
T4 ________________

<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
E E

<!-- b000020 | prose | pages [1] -->
F4 ________________

<!-- b000021 | prose | pages [1] -->
2019 MCM/ICM

<!-- b000022 | heading | pages [1] -->
Summary Sheet

<!-- b000023 | prose | pages [1] -->
To evaluate the unmeasurable cost of environmental services, our team introduces an accounting model to calculate the economic costs of ecosystem services. We divide the true economic costs of land use projects into three parts: natural resource consumption, cost of environmental pollution and cost of environmental degradation.

<!-- b000024 | prose | pages [1] -->
To measure the natural resource consumption more accurately, we discuss the non-market consumption and market consumption separately. For the non-market consumption, we express it with the ecological value of the natural resource we put in. For market consumption, we express it with the shadow price of the net primary production (NPP), which can be calculated by CASA model.

<!-- b000025 | prose | pages [1] -->
When it comes to cost of environmental pollution, we divide the environmental pollution into water pollution, air pollution and industrial waste. Then we consider the derivative effect of pollution by calculating the economic loss it causes.

<!-- b000026 | prose | pages [1] -->
As for the cost of environmental degradation, we divide it into the cost of vegetation depletion, land degradation and biodiversity decrease. We introduce the concept of ecological value to measure the cost of vegetation depletion, while the cost of land degradation is measured by its opportunity cost. Then we introduce Shannon Wiener Index to measure the biodiversity decrease.

<!-- b000027 | prose | pages [1] -->
To calculate the environmental degradation cost of land use projects, we regard the self-recovery process of ecosystem as a negative feedback process based on the feedback principle of BP nerve network. Then we construct a long-term ecological self-recover model. In order to weight different factors’ influence more accurately, we develop an OBP (One-way back propagation) nerve network, which is significantly simplified from the well-known BP nerve network. Firstly, we train the known data in the net without considering environmental recovery. After obtaining the weight of each factor, we use it in the long-term ecological self-recover model and calculate the cost of environmental degradation.

<!-- b000028 | prose | pages [1] -->
Then we cite three typical cases to conduct the cost-benefit analysis, which are House, Subway and Steel Mill. After our cost-benefit analysis, the House is not worth building considering the cost of ecosystem services, while it is worth building in the traditional analysis model. The Subway and Steel Mill is worth constructing in both the traditional way and our new model. From the cases, we can see the significance of considering the cost of ecosystem services for it may influence the decision of planners.

<!-- b000029 | prose | pages [1] -->
At the end of the paper, we have a further discussion about the cost of ecosystem services. We put forward an innovative expression of Green GDP with the model we built. Moreover, to relieve the externalities of land use projects, we consider Pigou tax and define it in a new way.

<!-- b000030 | furniture | pages [1] -->


<!-- b000031 | keywords | pages [1] -->
Key Words: ecological value, BP nerve network, long-term ecological self-recover model, cost-benefit

<!-- b000032 | prose | pages [1] -->
analysis, Green GDP, externalities

<!-- b000033 | furniture | pages [1] -->


<!-- b000034 | furniture | pages [2] -->
Team# 1916129

<!-- b000035 | furniture | pages [2] -->


<!-- b000036 | furniture | pages [2] -->
Page 1 of 20

<!-- b000037 | prose | pages [2] -->
CONTENT

<!-- b000038 | prose | pages [2] -->
1 Introduction ............................................................................................................................................. 2 1.1 Background .................................................................................................................................. 2 1.2 Problem Restatement ................................................................................................................... 2 1.3 Symbol Description ..................................................................................................................... 2 2 Measurement of Natural Resource Consumption ................................................................................... 3 2.1 Net Primary Production ............................................................................................................... 3 2.2 Modified Cobb-Douglas Production Function ............................................................................. 4 2.3 Measurement of Non-Market Consumption ................................................................................ 4 2.4 Measurement of Market Consumption ........................................................................................ 6 3 Cost of Environmental Pollution ............................................................................................................ 6 3.1 Cost of Water Pollution Control ................................................................................................... 7 3.2 Cost of Air Pollution Control ....................................................................................................... 7 3.3 Cost of Industrial Waste Control .................................................................................................. 7 3.4 Cost of Derivative Effects of Pollution ........................................................................................ 8 4 Cost of Environmental Degradation ....................................................................................................... 8 4.1 Cost of Vegetation Depletion ....................................................................................................... 8 4.2 Cost of Land Degradation ............................................................................................................ 9 4.3 Cost of Biodiversity Decrease ..................................................................................................... 9 5 Long-Term Ecological Self-Recover Model ......................................................................................... 10 5.1 General Assumption ................................................................................................................... 10 5.2 Weight Update Formula ............................................................................................................. 10 5.3 Simulation Process ..................................................................................................................... 11 5.4 Practical Application of the Model ............................................................................................ 12 6 Cost-Benefit Analysis of Land Use Project .......................................................................................... 13 6.1 General Assumption ................................................................................................................... 13 6.2 Cost Analysis of Land Use Project ............................................................................................ 13 6.3 Benefit Analysis of Land Use Project ........................................................................................ 14 6.4 Cost-Benefit Ratio ..................................................................................................................... 15 6.5 Case Analysis ............................................................................................................................. 15 7 Sensitivity Analysis ............................................................................................................................... 17 8 Strength and Weakness ......................................................................................................................... 18 8.1 Strength ...................................................................................................................................... 18 8.2 Weakness .................................................................................................................................... 18 9 Further Discussion ................................................................................................................................ 19 9.1 Pigou Tax for Externalities of Natural Resources ...................................................................... 19 9.2 Inspiration to the Expression of Green GDP ............................................................................. 19 Appendix .................................................................................................................................................... 1

<!-- b000039 | prose | pages [2] -->
I. Reference ........................................................................................................................................ 1 II. Cost of Ecological Service Data Sheet .......................................................................................... 1

<!-- b000040 | furniture | pages [2] -->


<!-- b000041 | furniture | pages [2] -->


<!-- b000042 | furniture | pages [3] -->
Team# 1916129

<!-- b000043 | furniture | pages [3] -->


<!-- b000044 | furniture | pages [3] -->
Page 2 of 20

<!-- b000045 | heading | pages [3] -->
1 Introduction

<!-- b000046 | heading | pages [3] -->
1.1 Background

<!-- b000047 | prose | pages [3] -->
Ecosystem services are the conditions and processes through which natural ecosystems and the species that make them up, sustain and fulfil human life [1]. Ecosystem services provide a guarantee for the survival of all life on earth. In traditional economic theory, Ecosystem services tend to be ignored and make no difference to the calculation of some economic indexes, such as GDP. However, Ecosystem services can be limited or removed by the human activities, which can influence the biodiversity and cause environmental degradation cumulatively. Moreover, as a research shows, the value of the entire biosphere (most of which is outside the market) is estimated at between $16 trillion and $54 trillion per year, with an average of $33 trillion per year [2]. Therefore, it is necessary to put a value on the environmental cost of human activities that have a negative impact on environment.

<!-- b000048 | heading | pages [3] -->
1.2 Problem Restatement

<!-- b000049 | prose | pages [3] -->
In this paper, we are aimed to find out the negative impacts of human activities on environment and value the environmental cost of them. We need to solve the following problems:

<!-- b000050 | prose | pages [3] -->
 Create a model to calculate the environmental cost of land use development projects. It is consist of

<!-- b000051 | prose | pages [3] -->
natural resource consumption, cost of environmental pollution and cost of environmental degradation.  Use the model to conduct a cost-benefit analysis of actual land use development projects.  Evaluate the effectiveness and timeliness of the model.

<!-- b000052 | heading | pages [3] -->
1.3 Symbol Description

<!-- b000053 | caption | pages [3] -->
Table 1. Symbol Description

<!-- b000054 | prose | pages [3] -->
Symbol Description Natural Resource Consumption C𝑟𝑒𝑠 C𝑝𝑜𝑙 Cost of Environmental Pollution C𝑑𝑒𝑔 Cost of Environmental Degradation N Net Primary Production (NPP) Y Total Output of an Economic Entity Technology Level of the Economic Entity 𝐴 Labor Put into Production 𝐿 Capital Put into Production 𝐾

<!-- b000055 | furniture | pages [3] -->


<!-- b000056 | furniture | pages [3] -->


<!-- b000057 | furniture | pages [4] -->
Team# 1916129

<!-- b000058 | furniture | pages [4] -->


<!-- b000059 | furniture | pages [4] -->


<!-- b000060 | furniture | pages [4] -->
Page 3 of 20

<!-- b000061 | heading | pages [4] -->
2 Measurement of Natural Resource Consumption

<!-- b000062 | heading | pages [4] -->
2.1 Net Primary Production

<!-- b000063 | prose | pages [4] -->
Net primary production (NPP) is a significant indicator for evaluating the level of ecosystem service. It weighs the amount of solar energy that is fixed by vegetation per unit of time after expending the energy of its metabolism. Net primary production (NPP) reflects the regulatory capacity of an ecosystem. The higher the value of NPP, the more carbon dioxide fixed by vegetation through photosynthesis and more nitrogen deposited. It means lower carbon dioxide content in the atmosphere, which directly reduce the greenhouse effect [5].

<!-- b000064 | heading | pages [4] -->
2.1.1 CASA Model for NNP Assessing

<!-- b000065 | prose | pages [4] -->
By referring to conference, we find out a method to roughly estimate the value of NPP. It is the product of vegetation absorbs photosynthetic effective radiation (APAR) and efficiency for solar energy utilization.

<!-- b000066 | prose | pages [4] -->
𝑁𝑃𝑃= 𝐴𝑃𝐴𝑅∙𝜀 [5]

<!-- b000067 | furniture | pages [4] -->


<!-- b000068 | prose | pages [4] -->
(1)

<!-- b000069 | prose | pages [4] -->
Where, NPP is Net Primary Production, 𝐴𝑃𝐴𝑅 is vegetation absorbs photosynthetic effective radiation and 𝜀 is efficiency for solar energy utilization.

<!-- b000070 | heading | pages [4] -->
1) APAR is influenced by fraction of photosynthetically active radiation (FPAR), total solar radiation

<!-- b000071 | prose | pages [4] -->
(TSR) and effective radiation ratio, which is 0.5.

<!-- b000072 | furniture | pages [4] -->


<!-- b000073 | prose | pages [4] -->
𝐴𝑃𝐴𝑅= 𝐹𝑃𝐴𝑅∙𝑆𝑂𝐿∙0.5 [5] (2)

<!-- b000074 | prose | pages [4] -->
Where, FPAR is fraction of photosynthetically active radiation, SOL is total solar radiation, which can be acknowledged by interpolating all of solar radiation stations in space.

<!-- b000075 | prose | pages [4] -->
𝐹𝑃𝐴𝑅𝑁𝐷𝑉𝐼+𝐹𝑃𝐴𝑅𝑆𝑅

<!-- b000076 | furniture | pages [4] -->


<!-- b000077 | prose | pages [4] -->
𝐹𝑃𝐴𝑅=

<!-- b000078 | prose | pages [4] -->
[5] (3) 2

<!-- b000079 | prose | pages [4] -->
Where，FPAR𝑁𝐷𝑉𝐼 can be calculated by NDVI image and NDVI pixel value, FPAR𝑆𝑅 can be calculated by SR index. The value of NDVI depends on the type of the vegetation. The SR index can be calculated by normalized difference vegetation index (NDVI).

<!-- b000080 | prose | pages [4] -->
2)  𝛆 depends on the maximum light utilization, temperature stress factor and image coefficients of water stress.

<!-- b000081 | furniture | pages [4] -->


<!-- b000082 | prose | pages [4] -->
(4) 𝜀= 𝜀𝑚𝑎𝑥∙𝑇𝜀∙𝑊𝜀 [5]

<!-- b000083 | prose | pages [4] -->
Where, ε𝑚𝑎𝑥 is maximum light utilization, which is a constant and depends on the type of the vegetation; Tε is temperature stress factor while Wε is image coefficients of water stress.

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | furniture | pages [5] -->
Team# 1916129

<!-- b000086 | furniture | pages [5] -->


<!-- b000087 | furniture | pages [5] -->


<!-- b000088 | furniture | pages [5] -->
Page 4 of 20

<!-- b000089 | heading | pages [5] -->
2.2 Modified Cobb-Douglas Production Function

<!-- b000090 | prose | pages [5] -->
Cobb-Douglas production function is an accounting equation measuring the total output of an economic entity. In classical economic theory, the contribution of Ecosystem services to the growth of output tend to be ignored. In this way, the traditional Cobb-Douglas production function has a form like this:

<!-- b000091 | furniture | pages [5] -->


<!-- b000092 | prose | pages [5] -->
(5) 𝑌= 𝐴∙𝐿𝛼∙𝐾𝛽

<!-- b000093 | prose | pages [5] -->
Where, Y is the total output of an economic entity, A is technology level of the economic entity, L is labor put into production, K is capital put into production, α, β are the output elasticities of labor and capital. Output elasticity measures the change of output introduced by the increase of unit factor input.

<!-- b000094 | prose | pages [5] -->
The environmental cost of human activities cannot be reflected in the above formula. Therefore, we introduce the modified Cobb-Douglas production function:

<!-- b000095 | furniture | pages [5] -->


<!-- b000096 | prose | pages [5] -->
𝑌= 𝐴∙𝐿𝛼∙𝐾𝛽∙𝑁𝜆

<!-- b000097 | furniture | pages [5] -->


<!-- b000098 | prose | pages [5] -->
(6) [3]

<!-- b000099 | prose | pages [5] -->
Where, N is Net Primary Production (NPP), 𝜆 is the output elasticities of Net Primary Production (NPP).

<!-- b000100 | heading | pages [5] -->
2.3 Measurement of Non-Market Consumption

<!-- b000101 | prose | pages [5] -->
It is hard for us to know the non-market consumption for there is no way to measure the consumers’ willingness to pay. On this occasion, we introduce ecological value to represent the natural resource consumption. Ecological value can be divided into five parts: the value of fixed carbon dioxide, oxygen released, purifying the water quality, cleaning the dust and conserving the soil.

<!-- b000102 | heading | pages [5] -->
2.3.1 Value of Fixed Carbon Dioxide and Oxygen released

<!-- b000103 | prose | pages [5] -->
Vegetation has the ability to fix carbon dioxide and release oxygen by photosynthesis. The reaction equation is as follows:

<!-- b000104 | furniture | pages [5] -->


<!-- b000105 | prose | pages [5] -->
(7) 6𝐶𝑂2 + 12𝐻2𝑂→𝐶6𝐻12𝑂6 + 6𝑂2 + 6𝐻2𝑂

<!-- b000106 | prose | pages [5] -->
The ratio of NPP, the quality of carbon dioxide and oxygen is 100:163:120 [4]. In the method of carbon tax approach and oxygen cost method, we can calculate the value of fixed carbon dioxide and oxygen released with the following formula:

<!-- b000107 | prose | pages [5] -->
𝑉𝑃= 𝑆∙(𝑐𝑂2 ∙𝑚𝑂2 + 𝑐𝐶∙(𝑚𝐶+ 𝐻𝑆))

<!-- b000108 | furniture | pages [5] -->


<!-- b000109 | prose | pages [5] -->
(8)

<!-- b000110 | prose | pages [5] -->
Where, 𝑉𝑃 is the value of fixed carbon dioxide and oxygen released, 𝑆 is the floor space of vegetation, 𝑐𝑂2, 𝑐𝐶 are respectively the price of oxygen and coal per ton, 𝑚𝑂2, 𝑚𝐶 are respectively the amount of oxygen released and carbon fixed, 𝐻𝑆 is carbon content of the soil.

<!-- b000111 | prose | pages [5] -->
The value of each constant can be seen in the following table:

<!-- b000112 | furniture | pages [5] -->


<!-- b000113 | furniture | pages [5] -->


<!-- b000114 | furniture | pages [5] -->


<!-- b000115 | furniture | pages [5] -->


<!-- b000116 | furniture | pages [6] -->
Team# 1916129

<!-- b000117 | furniture | pages [6] -->


<!-- b000118 | furniture | pages [6] -->


<!-- b000119 | furniture | pages [6] -->
Page 5 of 20

<!-- b000120 | caption | pages [6] -->
Table 2. Value of Constants in Formula (8) [8]

<!-- b000121 | prose | pages [6] -->
Constant 𝑐𝑂2 𝑚𝑂2 𝑐𝐶 𝑚𝐶 𝐻𝑆

<!-- b000122 | heading | pages [6] -->
2.3.2 Value of Conserving the Soil

<!-- b000123 | prose | pages [6] -->
Value 198.6 $/kg 0.05625 kg/m2 150 $/t 0.07755 kg/m2 0.505 kg/m2

<!-- b000124 | prose | pages [6] -->
The roots of vegetation are firmly entwined with the soil, which can help conserve the soil. The value of conserving the soil can be calculated by the following formula:

<!-- b000125 | prose | pages [6] -->
𝑆∙𝑐𝑠𝑜𝑖𝑙∙(𝑥2−𝑥1)

<!-- b000126 | furniture | pages [6] -->


<!-- b000127 | prose | pages [6] -->
𝑉𝑠=

<!-- b000128 | prose | pages [6] -->
[9] (9) 𝜌

<!-- b000129 | prose | pages [6] -->
Where, 𝑉𝑠 is the value of conserving the soil, S is the floor space of vegetation, c𝑠𝑜𝑖𝑙 is the cost of digging up and transporting a unit volume of soil, x2 is soil erosion modulus without vegetation, x1 is soil erosion modulus with vegetation, 𝜌 is soil bulk density.

<!-- b000130 | prose | pages [6] -->
The value of each constant can be seen in the following table:

<!-- b000131 | caption | pages [6] -->
Table 3. Value of Constants in Formula (9) [9]

<!-- b000132 | prose | pages [6] -->
Constant c𝑠𝑜𝑖𝑙 x2 x1 𝜌 Value 6 $/m³ 38.02 t/hm² 2.86 t/hm² 1.09 g/cm³

<!-- b000133 | heading | pages [6] -->
2.3.3 Value of Purifying the Water Quality

<!-- b000134 | prose | pages [6] -->
The branches, leaves and soil of vegetation are able to filter the pollutant in the rainfall. The value of purifying the rainfall quality can be calculated by the following formula:

<!-- b000135 | prose | pages [6] -->
𝑉𝑤= 10 ∙𝑆∙(𝑐𝑤𝑎𝑡+ 𝑐𝑝𝑜𝑜) ∙(𝑅−𝑇𝑅) [10]

<!-- b000136 | furniture | pages [6] -->


<!-- b000137 | prose | pages [6] -->
(10)

<!-- b000138 | prose | pages [6] -->
Where, 𝑉𝑤 is the value of purifying the water quality, 10 is conversion ratio, S is the floor space of vegetation, c𝑤𝑎𝑡, c𝑝𝑜𝑜 are respectively the cost of dealing polluted water and building reservoir per reservoir capacity, R is the amount of rainfall, TR is the amount of transpiration.

<!-- b000139 | prose | pages [6] -->
The value of each constant can be seen in the following table:

<!-- b000140 | caption | pages [6] -->
Table 4. Value of Constants in Formula (10) [10]

<!-- b000141 | prose | pages [6] -->
Constant c𝑤𝑎𝑡 c𝑝𝑜𝑜 R TR

<!-- b000142 | furniture | pages [6] -->


<!-- b000143 | prose | pages [6] -->
Value 0.417 $/t 0.147 $/a 483.3 mm/a 374.8 mm/a

<!-- b000144 | furniture | pages [7] -->
Team# 1916129

<!-- b000145 | heading | pages [7] -->
2.3.4 Value of Cleaning the Dust

<!-- b000146 | furniture | pages [7] -->


<!-- b000147 | furniture | pages [7] -->


<!-- b000148 | furniture | pages [7] -->
Page 6 of 20

<!-- b000149 | prose | pages [7] -->
Vegetation is able to absorb the hazardous substance in the atmosphere, such as S𝑂2, HF, N𝑂𝑋 and dust. The value of it can be calculated by the following formula:

<!-- b000150 | furniture | pages [7] -->


<!-- b000151 | prose | pages [7] -->
𝑉𝑑= 𝑆∙∑ ∙𝑄𝑖 [10] 4 (11) 𝑐𝑖 𝑖=1

<!-- b000152 | prose | pages [7] -->
Where, 𝑉𝑑 is the value of cleaning the dust, S is the floor space of vegetation, c𝑖 is the cost of controlling hazardous substance, Q𝑖 is the amount of absorption per unit area, i can be S𝑂2, HF, N𝑂𝑋 and dust.

<!-- b000153 | prose | pages [7] -->
The value of each constant can be seen in the following table:

<!-- b000154 | caption | pages [7] -->
Table 5. Value of Constants in Formula (11) [10]

<!-- b000155 | prose | pages [7] -->
Constant QS𝑂2 QHF QN𝑂𝑋 cS𝑂2 cHF cN𝑂𝑋 Value 37.3 kg/(hm².a) 1.68 kg/(hm².a) 6.00 kg/(hm².a) 0.171 $/kg 0.099 $/kg 0.090 $/kg

<!-- b000156 | heading | pages [7] -->
2.4 Measurement of Market Consumption

<!-- b000157 | prose | pages [7] -->
In the factor market, the factor inputs can be adjusted over time. With the Modified Cobb-Douglas Production Function, we use the shadow price of net primary production (NNP) to represent the natural resource consumption. The shadow price reflects the marginal contribution of net primary production (NPP) to output. Based on formula (2), we can calculate the value of it by taking the partial of net primary production (NPP) with respect to output.

<!-- b000158 | prose | pages [7] -->
𝐶𝑟𝑒𝑠= 𝜕𝑌

<!-- b000159 | furniture | pages [7] -->


<!-- b000160 | prose | pages [7] -->
(12) 𝜕𝑁= 𝐴∙𝜆∙𝐿𝛼∙𝐾𝛽∙𝑁𝜆−1 [3]

<!-- b000161 | prose | pages [7] -->
Where, Y is total output of an economic entity, N is Net Primary Production (NPP), A is technology level of the economic entity, L is labor put into production, K is capital put into production, α, β, 𝜆 are the output elasticities of labor, capital and NPP.

<!-- b000162 | heading | pages [7] -->
3 Cost of Environmental Pollution

<!-- b000163 | prose | pages [7] -->
The cost of environmental pollution is mainly consist of four parts: the control cost of water pollution, air pollution, industrial waste and the cost of derivative effects of pollution. It can be represented as the following formula:

<!-- b000164 | prose | pages [7] -->
𝐶𝑝𝑜𝑙= 𝐶𝑤+ 𝐶𝑎+ 𝐶𝑖+ 𝐶𝑑

<!-- b000165 | furniture | pages [7] -->


<!-- b000166 | prose | pages [7] -->
(13)

<!-- b000167 | prose | pages [7] -->
Where, C𝑝𝑜𝑙 is the cost of environmental pollution, C𝑤, C𝑎, C𝑖, C𝑑 is respectively the control cost of water pollution, air pollution, industrial waste and the cost of derivative effects of pollution.

<!-- b000168 | furniture | pages [7] -->


<!-- b000169 | furniture | pages [8] -->
Team# 1916129

<!-- b000170 | furniture | pages [8] -->


<!-- b000171 | furniture | pages [8] -->


<!-- b000172 | furniture | pages [8] -->
Page 7 of 20

<!-- b000173 | heading | pages [8] -->
3.1 Cost of Water Pollution Control

<!-- b000174 | prose | pages [8] -->
Water pollution is mainly caused by cyanide and harmful metals. Moreover, high level of chemical oxygen demand (COD) is also an evidence of water pollution. Therefore, the cost of water pollution control comes from the three parts. The cost of each part is shown in the following table:

<!-- b000175 | caption | pages [8] -->
Table 6. Control Cost of Water Pollution [6]

<!-- b000176 | prose | pages [8] -->
Type of Water Pollution COD Cyanide Harmful Metals

<!-- b000177 | furniture | pages [8] -->


<!-- b000178 | prose | pages [8] -->
Cost of Pollution Control ($/t) 1671.43 357.00 225.57

<!-- b000179 | prose | pages [8] -->
The cost of control the water pollution can be calculated as the following formula:

<!-- b000180 | prose | pages [8] -->
𝐶𝑤= 1671.43 ∙𝑛𝐶𝑂𝐷+ 357 ∙𝑛𝐶𝑦𝑎+ 225.57 ∙𝑛𝑚𝑒𝑡

<!-- b000181 | furniture | pages [8] -->


<!-- b000182 | prose | pages [8] -->
(14)

<!-- b000183 | prose | pages [8] -->
Where, C𝑤 is the cost of water pollution control, 𝑛𝐶𝑂𝐷 is the difference of COD above the standard value, 𝑛𝐶𝑦𝑎, 𝑛𝑚𝑒𝑡 respectively represent the amount of cyanide and harmful Metals.

<!-- b000184 | heading | pages [8] -->
3.2 Cost of Air Pollution Control

<!-- b000185 | prose | pages [8] -->
Air pollution is mainly caused by the pollutants S𝑂𝑥, C𝑂2, N𝑂𝑥, dust and smoke. The control cost of each part is shown in the following table:

<!-- b000186 | caption | pages [8] -->
Table 7. Control Cost of Air Pollution [6]

<!-- b000187 | prose | pages [8] -->
Type of Air Pollution S𝑂𝑥 C𝑂2 N𝑂𝑥 Dust Smoke Cost of Pollution Control ($/t) 92.86 97.14 432.86 32.86 20.00 The cost of control the air pollution can be calculated as the following formula:

<!-- b000188 | prose | pages [8] -->
𝐶𝑎= 92.86 ∙𝑛𝑆𝑂𝑥+ 97.14 ∙𝑛𝐶𝑂2 + 432.86 ∙𝑛𝑁𝑂𝑥+ 32.86 ∙𝑛𝐷𝑢𝑠+ 20 ∙𝑛𝑆𝑚𝑜 (15)

<!-- b000189 | prose | pages [8] -->
Where, C𝑎 is the cost of air pollution control, 𝑛S𝑂𝑥, 𝑛C𝑂2, 𝑛N𝑂𝑥, 𝑛Dus, 𝑛Smo respectively represent the amount of S𝑂𝑥, C𝑂2, N𝑂𝑥, dust and smoke.

<!-- b000190 | heading | pages [8] -->
3.3 Cost of Industrial Waste Control

<!-- b000191 | prose | pages [8] -->
Industrial waste can be divided into general industrial solid waste and hazardous fixed waste. The actual cost of control industrial waste is composed of the treatment cost and storage treatment cost of industrial solid waste. The calculation formula is as follows:

<!-- b000192 | furniture | pages [8] -->


<!-- b000193 | prose | pages [8] -->
(16) 𝐶𝑖= 𝐶𝑐𝑡𝑙 + 𝐶𝑠𝑡𝑜

<!-- b000194 | furniture | pages [8] -->


<!-- b000195 | furniture | pages [9] -->
Team# 1916129

<!-- b000196 | furniture | pages [9] -->


<!-- b000197 | furniture | pages [9] -->


<!-- b000198 | furniture | pages [9] -->
Page 8 of 20

<!-- b000199 | prose | pages [9] -->
Where, 𝐶𝑖 is the cost of industrial waste control, 𝐶𝑐𝑡𝑙 is the treatment cost and 𝐶𝑠𝑡𝑜 is storage treatment cost.

<!-- b000200 | prose | pages [9] -->
The control cost of each part is shown in the following table:

<!-- b000201 | caption | pages [9] -->
Table 8. Control Cost of Industrial Waste [7]

<!-- b000202 | prose | pages [9] -->
Type of Cost Type of Waste Unit Control Cost ($/t)

<!-- b000203 | prose | pages [9] -->
General Industrial Solid Waste Control Cost 3.14 Hazardous Waste 214.29

<!-- b000204 | prose | pages [9] -->
General Industrial Solid Waste Storage Cost 0.64 Hazardous Waste 2.15

<!-- b000205 | heading | pages [9] -->
3.4 Cost of Derivative Effects of Pollution

<!-- b000206 | prose | pages [9] -->
The derivative effects of pollution mainly refer to greenhouse effect, ozone hole and acid rain. The cost of it is calculated by the following formula:

<!-- b000207 | furniture | pages [9] -->


<!-- b000208 | prose | pages [9] -->
(17) 𝐶𝑑= 𝐿𝐺𝐻+ 𝐿𝑂𝐻+ 𝐿𝐴𝑅

<!-- b000209 | prose | pages [9] -->
Where, C𝑑 is the cost of derivative effects of pollution, L𝐺𝐻, L𝑂𝐻, L𝐴𝑅 are respectively the economic loss caused by greenhouse effect, ozone hole and acid rain.

<!-- b000210 | prose | pages [9] -->
The main evaluation index of greenhouse effect is carbon dioxide emissions. The greater the carbon dioxide emissions, the severer the greenhouse effect. Therefore, we approximate the severity of the greenhouse effect in terms of carbon dioxide emissions. The loss of greenhouse effect can be calculated with the following formula:

<!-- b000211 | furniture | pages [9] -->


<!-- b000212 | prose | pages [9] -->
(18) 𝐿𝐺𝐻= 𝛼∙𝐸𝑐

<!-- b000213 | prose | pages [9] -->
Where, L𝐺𝐻 is the loss caused by greenhouse effect, 𝛼 is the marginal rate of substitution of capital for carbon dioxide emissions, 𝐸𝑐 is the amount of carbon dioxide emissions.

<!-- b000214 | heading | pages [9] -->
4 Cost of Environmental Degradation

<!-- b000215 | prose | pages [9] -->
Environmental degradation refers to the deterioration or compromise of the natural environment through consumption of assets by either natural processes or human activities. The classic examples of Environmental degradation are vegetation depletion, land degradation and biodiversity decrease.

<!-- b000216 | prose | pages [9] -->
𝐶𝑑𝑒𝑔= 𝐶𝑣𝑒𝑔𝑒+ 𝐶𝑙𝑎𝑛𝑑+ 𝐶𝑏𝑖𝑜𝑑

<!-- b000217 | furniture | pages [9] -->


<!-- b000218 | prose | pages [9] -->
(19)

<!-- b000219 | prose | pages [9] -->
Where, C𝑑𝑒𝑔 is the cost of environmental degradation, C𝑣𝑒𝑔𝑒, C𝑙𝑎𝑛𝑑, C𝑏𝑖𝑜𝑑 respectively are the loss of vegetation depletion, land degradation and biodiversity decrease.

<!-- b000220 | prose | pages [9] -->
Then we will have a further discussion about the cost of the losses.

<!-- b000221 | heading | pages [9] -->
4.1 Cost of Vegetation Depletion

<!-- b000222 | prose | pages [9] -->
Vegetation depletion weakens the ability of ecosystem to purify the air, which means it fails to absorb the harmful gas such as S𝑂𝑥 and N𝑂𝑥. Moreover, vegetation depletion decreases the 𝑂2 in the atmosphere

<!-- b000223 | furniture | pages [9] -->


<!-- b000224 | furniture | pages [10] -->
Team# 1916129

<!-- b000225 | furniture | pages [10] -->


<!-- b000226 | furniture | pages [10] -->


<!-- b000227 | furniture | pages [10] -->
Page 9 of 20

<!-- b000228 | prose | pages [10] -->
and increases the 𝐶𝑂2 in the atmosphere. The loss of them can be measured by their ecological value. The way to calculate the ecological value of the loss is represented by the formula (7).

<!-- b000229 | heading | pages [10] -->
4.2 Cost of Land Degradation

<!-- b000230 | prose | pages [10] -->
Land degradation leads to loss of land nutrient substance and sediment hazards. Based on the theory of market value, we can calculate soil conservation value by the opportunity cost of land nutrient substance and the control cost of sediment hazards.

<!-- b000231 | furniture | pages [10] -->


<!-- b000232 | prose | pages [10] -->
(20) 𝐶𝑙𝑎𝑛𝑑= ∆𝐴∙(𝐶𝑛𝑢𝑡+ 𝐶𝑠𝑒𝑑)

<!-- b000233 | prose | pages [10] -->
Where, C𝑙𝑎𝑛𝑑 is the total cost of land degradation, A is soil retention, C𝑛𝑢𝑡 is the unit opportunity cost of land nutrient substance, C𝑠𝑒𝑑 is the control cost of sediment hazards.

<!-- b000234 | prose | pages [10] -->
𝐴= 𝑅∙𝐾∙𝐿𝑆∙(1 −𝐶∙𝑃)[8]

<!-- b000235 | furniture | pages [10] -->


<!-- b000236 | prose | pages [10] -->
(21)

<!-- b000237 | prose | pages [10] -->
Where, R is rainfall erosion, which can be observed, K is factor of soil erodibility, LS is slope length slope factor, C is land cover factor, P is soil conservation measures factor. All of the parameters except R are constants.

<!-- b000238 | heading | pages [10] -->
4.3 Cost of Biodiversity Decrease

<!-- b000239 | prose | pages [10] -->
Misuse of ecological services leads to the decrease of biodiversity. To measure the biodiversity in a district, we adopt the Shannon Wiener Index formula with the method of theory of information.

<!-- b000240 | prose | pages [10] -->
𝐻= −∑𝑃𝑖∙𝑙𝑛 (𝑃𝑖)

<!-- b000241 | furniture | pages [10] -->


<!-- b000242 | prose | pages [10] -->
(22)

<!-- b000243 | prose | pages [10] -->
Where, H is Shannon Wiener Index, 𝑃𝑖 is the proportion of species individualities in total number of individuals.

<!-- b000244 | prose | pages [10] -->
We can learn from the formula that biodiversity is proportional to Shannon Wiener Index. In case of species distribution uniformity, the Shannon Wiener Index is one. When there is only one species, the Shannon Wiener Index is zero. The decrease of species diversity is a long-term qualitative change process. Therefore, the large-scale land project during long period will have negative effects on biodiversity. The cost of ecological services due to biodiversity loss is approximately equal to the difference of Shannon Wiener Index over a long period of time multiplied the unit service value. The unit service value is shown in the following table:

<!-- b000245 | caption | pages [10] -->
Table 9. Unit Service Value of Biodiversity

<!-- b000246 | prose | pages [10] -->
Range of Shannon Wiener Index 0 < H < 1 1 ≤H < 2 2 ≤H < 3 3 ≤H < 4 4 ≤H < 5 5 ≤H < 6 6 ≤H

<!-- b000247 | furniture | pages [10] -->


<!-- b000248 | prose | pages [10] -->
Unit Service Value ($/hm2) 428.57 714.29 1428.57 2857.14 4285.71 5714.28 7142.86

<!-- b000249 | furniture | pages [11] -->
Team# 1916129

<!-- b000250 | furniture | pages [11] -->


<!-- b000251 | furniture | pages [11] -->
Page 10 of 20

<!-- b000252 | heading | pages [11] -->
5 Long-Term Ecological Self-Recover Model

<!-- b000253 | prose | pages [11] -->
All of the ecosystems have the ability to self-recover. It is reflected in the renewable nature of resources, the self-decomposition of waste and so on. Based on the feedback principle of BP neural network, we regard the self-recovery process of ecosystem as a negative feedback process, and thus construct the time evolution model of ecological self-recovery.

<!-- b000254 | heading | pages [11] -->
5.1 General Assumption

<!-- b000255 | prose | pages [11] -->
 The original ecological environment is not polluted.  The resistance stability of environment is very rapid while the restorative stability is slow.

<!-- b000256 | heading | pages [11] -->
5.2 Weight Update Formula

<!-- b000257 | prose | pages [11] -->
Considering the practicability of the model, the weights of the new model cannot be randomly selected. At the same time, we give up the method of AHP to find the weights. Through our database, we establish a training set of 20 different engineering data set. We use neural network machine learning method under the condition of satisfying error accuracy to train a group of appropriate weight.

<!-- b000258 | caption | pages [11] -->
Figure 1. Hierarchical Structure of Neural Network

<!-- b000259 | furniture | pages [11] -->


<!-- b000260 | furniture | pages [11] -->


<!-- b000261 | prose | pages [11] -->
Note: G.S. Waste = General Industrial Solid Waste

<!-- b000262 | prose | pages [11] -->
H. Waste = Hazardous Waste

<!-- b000263 | furniture | pages [11] -->


<!-- b000264 | furniture | pages [12] -->
Team# 1916129

<!-- b000265 | furniture | pages [12] -->


<!-- b000266 | furniture | pages [12] -->


<!-- b000267 | furniture | pages [12] -->
Page 11 of 20

<!-- b000268 | prose | pages [12] -->
When we train the known training set, the process of neural network back propagation is influenced by only one “mother”. We keep adjusting the weights until it is within the margin of error. The advantage of determining the weight in this way is that the unit influence of different parameters can be reflected in the weight.

<!-- b000269 | prose | pages [12] -->
The weight update formula from hidden layer to output layer is as follows:

<!-- b000270 | prose | pages [12] -->
= 𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000271 | prose | pages [12] -->
𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000272 | furniture | pages [12] -->


<!-- b000273 | prose | pages [12] -->
𝜕𝑊11

<!-- b000274 | prose | pages [12] -->
𝜕𝑊𝑜𝑢𝑡

<!-- b000275 | prose | pages [12] -->
∙𝜕𝑊𝑜𝑢𝑡

<!-- b000276 | prose | pages [12] -->
∙𝜕𝑊𝑛𝑒

<!-- b000277 | furniture | pages [12] -->


<!-- b000278 | prose | pages [12] -->
(23)

<!-- b000279 | prose | pages [12] -->
𝜕𝑊𝑛𝑒

<!-- b000280 | prose | pages [12] -->
𝜕𝑊11

<!-- b000281 | prose | pages [12] -->
𝑊11′ = 𝑊11 −𝜂∙𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000282 | furniture | pages [12] -->


<!-- b000283 | prose | pages [12] -->
(24)

<!-- b000284 | furniture | pages [12] -->


<!-- b000285 | prose | pages [12] -->
𝜕𝑊11

<!-- b000286 | prose | pages [12] -->
Where, 𝐸𝑡𝑜𝑡𝑎𝑙 is the binary norm of the total error between the output and the actual value of the output layer neural unit, 𝑊𝑜𝑢𝑡 is the output of the neuron, 𝑊𝑛𝑒 is the linear summation of output values of

<!-- b000287 | prose | pages [12] -->
𝜕𝑊𝑜𝑢𝑡

<!-- b000288 | prose | pages [12] -->
𝜕𝑊𝑛𝑒 is to find derivative of the activation function, η is the learning rate.

<!-- b000289 | prose | pages [12] -->
hidden layer,

<!-- b000290 | prose | pages [12] -->
The weight formula updating the first layer is as follows:

<!-- b000291 | prose | pages [12] -->
= 𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000292 | prose | pages [12] -->
𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000293 | furniture | pages [12] -->


<!-- b000294 | prose | pages [12] -->
𝜕𝑊11

<!-- b000295 | prose | pages [12] -->
𝜕𝑊𝑜𝑤

<!-- b000296 | prose | pages [12] -->
𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000297 | furniture | pages [12] -->


<!-- b000298 | prose | pages [12] -->
𝜕𝑊𝑜𝑤

<!-- b000299 | prose | pages [12] -->
∙𝜕𝑊𝑜𝑤

<!-- b000300 | prose | pages [12] -->
∙𝜕𝑊𝑛𝑤

<!-- b000301 | prose | pages [12] -->
(25)

<!-- b000302 | furniture | pages [12] -->


<!-- b000303 | prose | pages [12] -->
𝜕𝑊𝑛𝑒

<!-- b000304 | prose | pages [12] -->
𝜕𝑊11

<!-- b000305 | prose | pages [12] -->
= 𝜕𝐸𝑤

<!-- b000306 | prose | pages [12] -->
(26)

<!-- b000307 | furniture | pages [12] -->


<!-- b000308 | prose | pages [12] -->
𝜕𝑊𝑜𝑤

<!-- b000309 | prose | pages [12] -->
𝑊11′ = 𝑊11 −𝜂∙𝜕𝐸𝑡𝑜𝑡𝑎𝑙

<!-- b000310 | furniture | pages [12] -->


<!-- b000311 | prose | pages [12] -->
(27)

<!-- b000312 | furniture | pages [12] -->


<!-- b000313 | prose | pages [12] -->
𝜕𝑊11

<!-- b000314 | prose | pages [12] -->
Where, 𝐸𝑤 is the overall error of hidden layer (water pollution) nerve cell, 𝑊𝑜𝑤 is the output if nerve

<!-- b000315 | prose | pages [12] -->
𝜕𝑊𝑜𝑤

<!-- b000316 | prose | pages [12] -->
cell (water pollution), 𝑊𝑛𝑤 is the linear summation of output values of input layer,

<!-- b000317 | prose | pages [12] -->
𝜕𝑊𝑛𝑒 is to find

<!-- b000318 | prose | pages [12] -->
derivative of the activation function, η is the learning rate.

<!-- b000319 | heading | pages [12] -->
5.3 Simulation Process

<!-- b000320 | prose | pages [12] -->
Firstly, based on the life cycle theory, we divide the project into five cycles, which are the planning and design period, the raw material processing period, the construction period, the operation period and the end of life period. Here, we consider the evolution law of the pollution discharge with time in the raw material processing period, construction period and operation period.

<!-- b000321 | prose | pages [12] -->
We can substitute the weights trained by BP neural network into our ecological self-recover model. The pollutants discharged in the projects must be treated before they flow into the ecosystem. The pollutants flowing into the ecosystem are partly eliminated by the resistance of ecosystem while the others remain there. In the long term, this part could be purified because of the self –recover ability of ecosystem. Furthermore, something needs to be noticed.

<!-- b000322 | prose | pages [12] -->
 When the level of pollution exceeds the critical value that the ecosystem can withstand (k/2), the

<!-- b000323 | prose | pages [12] -->
pollutant will not be purified.

<!-- b000324 | furniture | pages [12] -->


<!-- b000325 | furniture | pages [13] -->
Team# 1916129

<!-- b000326 | furniture | pages [13] -->


<!-- b000327 | furniture | pages [13] -->


<!-- b000328 | furniture | pages [13] -->
Page 12 of 20

<!-- b000329 | prose | pages [13] -->
 The stability of ecosystem decreased with the increase of pollution degree, and the stability of resilience

<!-- b000330 | prose | pages [13] -->
increases with the increase of pollution degree.

<!-- b000331 | prose | pages [13] -->
The pollutant of the first year can be calculated by the following formula:

<!-- b000332 | prose | pages [13] -->
3

<!-- b000333 | furniture | pages [13] -->


<!-- b000334 | prose | pages [13] -->
(28)

<!-- b000335 | furniture | pages [13] -->


<!-- b000336 | prose | pages [13] -->
𝐸1 = ∑𝑥1𝑖(1 −𝛽𝑖)) ∙(1 −𝜆)

<!-- b000337 | prose | pages [13] -->
𝑖=1

<!-- b000338 | prose | pages [13] -->
The pollutant in year m+1 can be calculated by the following formula:

<!-- b000339 | prose | pages [13] -->
𝑚+1

<!-- b000340 | furniture | pages [13] -->


<!-- b000341 | prose | pages [13] -->
3

<!-- b000342 | prose | pages [13] -->
(29)

<!-- b000343 | furniture | pages [13] -->


<!-- b000344 | prose | pages [13] -->
𝐸𝑚+1 = ∑𝐸𝑛∙𝑓(𝑚+ 1 −𝑛, 𝛾) +∙∑𝑥1𝑖(1 −𝛽𝑖)) ∙(1 −𝜆)

<!-- b000345 | prose | pages [13] -->
𝑖=1

<!-- b000346 | prose | pages [13] -->
Where, γ = g(∑𝐸), λ = h(∑𝐸)

<!-- b000347 | prose | pages [13] -->
𝑖=1

<!-- b000348 | prose | pages [13] -->
As the system evolves, the ecosystem collapses because either the pollution level exceeds k/2, or it will reach a dynamic equilibrium. When it reaches the dynamic equilibrium, the status can be represented by the following formula:

<!-- b000349 | prose | pages [13] -->
𝑚−1

<!-- b000350 | furniture | pages [13] -->


<!-- b000351 | prose | pages [13] -->
3

<!-- b000352 | prose | pages [13] -->
(30) (1 −𝜆)

<!-- b000353 | prose | pages [13] -->
𝐸𝑚+1 ∙(1 −𝑓(1)) = ∑𝐸𝑛∙𝑓(𝑚+ 𝑛−1, 𝛾) + (∑𝑥1𝑖∙(1 −𝛽)

<!-- b000354 | prose | pages [13] -->
𝑛=1

<!-- b000355 | prose | pages [13] -->
) ∙

<!-- b000356 | prose | pages [13] -->
𝑖=1

<!-- b000357 | prose | pages [13] -->
Where, f(a, b) is a function that reflects the ecosystem restoration changed with recovery capability and time, g(E) is the function that reflects the ecosystem restoration increases with the pollution level increasing, h(E) is the ecosystem resilience decreases with the pollution level increasing.

<!-- b000358 | heading | pages [13] -->
5.4 Practical Application of the Model

<!-- b000359 | prose | pages [13] -->
Using our model, we can calculate the environmental degradation cost in different years more accurately. Then we use four practical examples to apply the model, the details of the data can be seen in the appendix. The computed results are as follows:

<!-- b000360 | caption | pages [13] -->
Figure 2. Environmental Degradation Cost of Bridge and Steel Plant

<!-- b000361 | furniture | pages [13] -->


<!-- b000362 | furniture | pages [13] -->


<!-- b000363 | furniture | pages [14] -->
Team# 1916129

<!-- b000364 | furniture | pages [14] -->


<!-- b000365 | furniture | pages [14] -->
Page 13 of 20

<!-- b000366 | caption | pages [14] -->
Figure 3. Environmental Degradation Cost of House and Subway

<!-- b000367 | furniture | pages [14] -->


<!-- b000368 | prose | pages [14] -->
There is a turning point in both figures. The curve before the turning point is our raw material and construction. In this part of curve, a large amount of pollutant emission rises rapidly. Therefore, there is a little bit steep. The curve after the turning point is the operating period. In this part of curve, we find that because of the purification of ecosystem, the houses and bridges in the projects with less pollution will self- recover over time. However, for the steel mill and subway project with more pollution, the purification of the annual quantity is less than new emissions pollution. Without man-made management, pollution become more serious.

<!-- b000369 | heading | pages [14] -->
6 Cost-Benefit Analysis of Land Use Project

<!-- b000370 | heading | pages [14] -->
6.1 General Assumption

<!-- b000371 | prose | pages [14] -->
 Net cash flow (NCF) is the same every year.  The depreciation method is linear depreciation.

<!-- b000372 | heading | pages [14] -->
6.2 Cost Analysis of Land Use Project

<!-- b000373 | prose | pages [14] -->
In order to simplify the model, we use factor cost to calculate the main cost of projects. The components of long-term costs of land use project are shown in the table below:

<!-- b000374 | caption | pages [14] -->
Figure 4. Components of Main Long-Term Costs of Project

<!-- b000375 | furniture | pages [14] -->


<!-- b000376 | furniture | pages [14] -->


<!-- b000377 | furniture | pages [14] -->


<!-- b000378 | furniture | pages [14] -->


<!-- b000379 | furniture | pages [14] -->


<!-- b000380 | furniture | pages [14] -->


<!-- b000381 | furniture | pages [14] -->


<!-- b000382 | furniture | pages [14] -->


<!-- b000383 | furniture | pages [15] -->
Team# 1916129

<!-- b000384 | heading | pages [15] -->
6.2.1 Cost in Construction Time

<!-- b000385 | furniture | pages [15] -->


<!-- b000386 | furniture | pages [15] -->


<!-- b000387 | furniture | pages [15] -->
Page 14 of 20

<!-- b000388 | prose | pages [15] -->
Considering the lifetime of the project, we introduce the concept of present worth, which is calculated by expected cash flow, present value factor and discount rate. By adopting the present value approach rather than simply adding the cash flow of each year together, we can get a more accurate cost figure. In this way, we fully account for the time cost of the input factor.

<!-- b000389 | prose | pages [15] -->
𝑡1

<!-- b000390 | prose | pages [15] -->
𝐶1 = ∑𝑤𝑖+ 𝑘𝑖+ 𝑇𝑖+ 𝐶𝑐𝑜𝑛,𝑖

<!-- b000391 | furniture | pages [15] -->


<!-- b000392 | prose | pages [15] -->
𝑖=1

<!-- b000393 | prose | pages [15] -->
(31)

<!-- b000394 | furniture | pages [15] -->


<!-- b000395 | prose | pages [15] -->
(1 + 𝑟)𝑡1

<!-- b000396 | prose | pages [15] -->
Where, C1 is the cost in construction time, 𝑡1 is the construction period, 𝑟 is discount rate, 𝑤𝑖, 𝑘𝑖, 𝑇𝑖, 𝐶𝑐𝑜𝑛,𝑖 are respectively the employee compensation, capital input, technology input and pollution treatment cost in year i.

<!-- b000397 | heading | pages [15] -->
6.2.2 Cost in Operation Time

<!-- b000398 | prose | pages [15] -->
Likewise, we take the lifetime of the project into consideration. The depreciation method is linear depreciation. The cost in operation time can be calculated by the following formula:

<!-- b000399 | prose | pages [15] -->
𝑡2

<!-- b000400 | prose | pages [15] -->
𝐶2 = ∑𝑚𝑗+ 𝑑𝑗

<!-- b000401 | furniture | pages [15] -->


<!-- b000402 | prose | pages [15] -->
𝑗=1

<!-- b000403 | prose | pages [15] -->
(32)

<!-- b000404 | furniture | pages [15] -->


<!-- b000405 | prose | pages [15] -->
(1 + 𝑟)𝑡2

<!-- b000406 | prose | pages [15] -->
Where, C2 is the cost in operation time, 𝑡2 is the operation period, which is equal to expected useful life of the asset, 𝑟 is discount rate, 𝑚𝑗, 𝑑𝑗 are respectively the maintenance charge and depreciation expense. The depreciation expense can be calculated according to formula (20).

<!-- b000407 | prose | pages [15] -->
𝑑𝑗= 𝐾

<!-- b000408 | furniture | pages [15] -->


<!-- b000409 | furniture | pages [15] -->


<!-- b000410 | prose | pages [15] -->
(33)

<!-- b000411 | prose | pages [15] -->
𝑡2

<!-- b000412 | prose | pages [15] -->
Where, K is constructed assets that need to be depreciated，𝑡2 is the expected useful life of the asset.

<!-- b000413 | heading | pages [15] -->
6.3 Benefit Analysis of Land Use Project

<!-- b000414 | prose | pages [15] -->
The long-term benefit of land use project is mainly consists of future inward cash flow and estimated net residual value of the project.

<!-- b000415 | prose | pages [15] -->
Considering the time cost, we calculate the benefit by the following formula:

<!-- b000416 | prose | pages [15] -->
𝐼𝑂

<!-- b000417 | furniture | pages [15] -->


<!-- b000418 | prose | pages [15] -->
𝑡2 𝑡2

<!-- b000419 | prose | pages [15] -->
𝐼𝑗

<!-- b000420 | prose | pages [15] -->
(34) + 𝐼𝑢𝑛

<!-- b000421 | prose | pages [15] -->
(1 + 𝑟)𝑡2 + ∑ 𝐼= (1 + 𝑟)𝑡2

<!-- b000422 | prose | pages [15] -->
𝑗=1

<!-- b000423 | prose | pages [15] -->
Where, I is the total benefit of the project, 𝐼𝑂 is expected net residual value, 𝑟 is discount rate, 𝑡2 is the operation period, 𝐼𝑗 is inward cash flow in year j, 𝐼𝑢𝑛 is the non-market benefit, which depends on the type of projects.

<!-- b000424 | furniture | pages [15] -->


<!-- b000425 | furniture | pages [16] -->
Team# 1916129

<!-- b000426 | heading | pages [16] -->
6.4 Cost-Benefit Ratio

<!-- b000427 | furniture | pages [16] -->


<!-- b000428 | furniture | pages [16] -->


<!-- b000429 | furniture | pages [16] -->
Page 15 of 20

<!-- b000430 | furniture | pages [16] -->


<!-- b000431 | prose | pages [16] -->
Cost-benefit ratio is to reflect the profitability of the project, which can help decision makers to determine whether the project is beneficial to conduct. The cost-benefit ratio can be calculated by the following formula:

<!-- b000432 | prose | pages [16] -->
𝑟= 𝐶

<!-- b000433 | furniture | pages [16] -->


<!-- b000434 | prose | pages [16] -->
(35) 𝐼

<!-- b000435 | prose | pages [16] -->
Where, r is cost-benefit ratio, C is the financial cost, I is inward cash flow. In the traditional cost-benefit analysis, the decision maker may underestimate the total cost by ignoring the cost of ecosystem services.

<!-- b000436 | prose | pages [16] -->
In the developed cost-benefit analysis, we take the cost of ecosystem services and the social benefit into consideration. The developed formula can be represented as follows:

<!-- b000437 | prose | pages [16] -->
𝑟= 𝐶+ 𝐶𝑒

<!-- b000438 | furniture | pages [16] -->


<!-- b000439 | furniture | pages [16] -->


<!-- b000440 | prose | pages [16] -->
(36)

<!-- b000441 | prose | pages [16] -->
𝐼+ 𝐼𝑠

<!-- b000442 | prose | pages [16] -->
Where, r is cost-benefit ratio, C is the financial cost, 𝐶𝑒 is cost of ecosystem services, I is inward cash flow and 𝐼𝑠 is social benefit.

<!-- b000443 | heading | pages [16] -->
6.5 Case Analysis

<!-- b000444 | prose | pages [16] -->
In this part, we will conduct cost-benefit analysis of three different size projects using the self-recover model. Details of cost of ecosystem services and pollution are listed in the appendix. Moreover, we assume that the discount rate is 3%.

<!-- b000445 | heading | pages [16] -->
6.5.1 House of One Hundred Square Meters

<!-- b000446 | prose | pages [16] -->
The construction time of residential building is around one year, while the lifetime of it is around twenty years. The expected net residual value rate is about 5%. The cost and benefit can be seen in the following table:

<!-- b000447 | caption | pages [16] -->
Table 10. Cost Analysis of House

<!-- b000448 | prose | pages [16] -->
House Employee Compensation Capital Input Technology Input Maintenance Charge Cost of Derivative Effects of Pollution Cost of Environmental Degradation TOTAL

<!-- b000449 | furniture | pages [16] -->


<!-- b000450 | furniture | pages [16] -->


<!-- b000451 | furniture | pages [16] -->


<!-- b000452 | furniture | pages [16] -->


<!-- b000453 | prose | pages [16] -->
Cost/$

<!-- b000454 | furniture | pages [16] -->


<!-- b000455 | prose | pages [16] -->
2,914.29

<!-- b000456 | furniture | pages [16] -->


<!-- b000457 | prose | pages [16] -->
25,714.29

<!-- b000458 | furniture | pages [16] -->


<!-- b000459 | prose | pages [16] -->
7,142.86

<!-- b000460 | furniture | pages [16] -->


<!-- b000461 | prose | pages [16] -->
2,571.43

<!-- b000462 | furniture | pages [16] -->


<!-- b000463 | prose | pages [16] -->
41,214.72

<!-- b000464 | furniture | pages [16] -->


<!-- b000465 | prose | pages [16] -->
699.00

<!-- b000466 | furniture | pages [16] -->


<!-- b000467 | prose | pages [16] -->
80,256.59

<!-- b000468 | furniture | pages [16] -->


<!-- b000469 | furniture | pages [17] -->
Team# 1916129

<!-- b000470 | furniture | pages [17] -->


<!-- b000471 | furniture | pages [17] -->


<!-- b000472 | furniture | pages [17] -->
Page 16 of 20

<!-- b000473 | caption | pages [17] -->
Table 11. Benefit Analysis of House

<!-- b000474 | prose | pages [17] -->
Annual Payment/$ House Rent Income 5,142.84 Net Residual 1,917.74 Social TOTAL Present Value of Annuity/$ 76,512.60 1,061.85 0 0 0

<!-- b000475 | furniture | pages [17] -->


<!-- b000476 | furniture | pages [17] -->


<!-- b000477 | prose | pages [17] -->
77576.45

<!-- b000478 | prose | pages [17] -->
The cost-benefit ratio calculated in the traditional way is 0.49, which means the project is worth conducting. However, the cost-ratio calculated considering the ecosystem services is 1.03, which means the project is not worth conducting.

<!-- b000479 | heading | pages [17] -->
6.5.2 Subway of Forty Kilometers

<!-- b000480 | prose | pages [17] -->
The construction time of subway is around five years, while the lifetime of it is around sixty years. The rate of depreciation of subway is 1%. The cost and benefit can be seen in the following table:

<!-- b000481 | caption | pages [17] -->
Table 12. Cost Analysis of Subway

<!-- b000482 | prose | pages [17] -->
Subway

<!-- b000483 | prose | pages [17] -->
Employee Compensation Capital Input Technology Input Maintenance Charge Cost of Derivative Effects of Pollution Cost of Environmental Degradation TOTAL

<!-- b000484 | prose | pages [17] -->
Annual Payment/$ Present Value of Annuity/$

<!-- b000485 | prose | pages [17] -->
137,142,857.14 626,742,857.14 274,285,714.29 1,253,485,714.29 45,714,285.71 208,914,285.71 1,142,857.14 5,222,857.13 9,300,938.57 42,595,508.37 125.71 575.73 2,136,961,798.37

<!-- b000486 | caption | pages [17] -->
Table 13. Benefit Analysis of Subway

<!-- b000487 | prose | pages [17] -->
Annual Payment/$ Subway Present Value of Annuity/$

<!-- b000488 | prose | pages [17] -->
81,428,571.43 Service Charge Income 2,253,581,612.85 835,657,142.86 Net Residual Value 141,838,669.05 4,428,571.43 Social Benefit 122,563,210.56 2,517,983,492.46 TOTAL

<!-- b000489 | prose | pages [17] -->
The cost-benefit ratio calculated in the traditional way is 0.83, which means the project is worth conducting. However, the cost-ratio calculated considering the ecosystem services is 0.84, which means the project is worth conducting as well.

<!-- b000490 | heading | pages [17] -->
6.5.3 Large-Scale Steel Mill of Twenty-Three Square Kilometers

<!-- b000491 | prose | pages [17] -->
The construction time of a steel mill is around five years, while the lifetime of it is around twenty years. The rate of depreciation of steel mill is 1%.The cost and benefit can be seen in the following table:

<!-- b000492 | caption | pages [17] -->
Table 14. Cost Analysis of Steel Mill

<!-- b000493 | prose | pages [17] -->
Annual Payment/$ Steel Mill Present Value of Annuity/$ 141,181,111.74 Employee Compensation 646,567,137.44 988,267,782.17 Capital Input

<!-- b000494 | furniture | pages [17] -->


<!-- b000495 | prose | pages [17] -->
4,525,969,962.01

<!-- b000496 | furniture | pages [18] -->
Team# 1916129

<!-- b000497 | furniture | pages [18] -->


<!-- b000498 | furniture | pages [18] -->


<!-- b000499 | furniture | pages [18] -->
Page 17 of 20

<!-- b000500 | prose | pages [18] -->
282,362,223.48 Technology Input 1,293,134,274.87 27,697,106.54 Maintenance Charge 126,844,438.84 38,696,421.71 Cost of Derivative Effects of 177,218,002.52 719.67 Cost of Environmental Degradation TOTAL 3,295.89 6,769,737,111.57

<!-- b000501 | caption | pages [18] -->
Table 15. Benefit Analysis of Steel Mill

<!-- b000502 | prose | pages [18] -->
Annual Payment/$ Steel Mill Present Value of Annuity/$

<!-- b000503 | prose | pages [18] -->
1,858,571,428.60 Revenue from Operations Net Residual Value Social Benefit TOTAL 51,437,011,900.24 0 0 0 0 51,437,011,900.24

<!-- b000504 | prose | pages [18] -->
The cost-benefit ratio calculated in the traditional way is 0.13, which means the project is worth conducting. However, the cost-ratio calculated considering the ecosystem services is 0.13, which means the project is worth conducting as well.

<!-- b000505 | heading | pages [18] -->
7 Sensitivity Analysis

<!-- b000506 | prose | pages [18] -->
In order to test the robustness of the model, we added 1% noise value to the above index parameters of our model and observed the change rate of output cost. The results are shown in the following table.

<!-- b000507 | caption | pages [18] -->
Table 16. Error of the Ecological Cost Corresponding to the Different Input Error

<!-- b000508 | prose | pages [18] -->
Parameter Housing H(1%) 0.025% SO𝑥(1%) 0.15% N𝑂𝑥(1%) 0.14% Cyanide (1%) 0.11% 0.14% General Industrial Waste (1%) Hazardous waste (1%) 0.09% Bridge Subway Steel Plant 0.003% 0.02% 0.56% 0.14% 0.05% 0.13% 0.21% 0.12% 0.20% 0.12% 0.19% 0.10% 0.17% 0.14% 0.13% 0.12% 0.10% 0.09%

<!-- b000509 | prose | pages [18] -->
When we apply the model to practice, the margin k/2 is much higher than the damage caused by the project. Therefore, the ecosystem can always reach a dynamic balance. In order to verify the accuracy of the model, we replace k/2 value with a lower value, which can be reached more easily. We can see from the graph that once the degree of pollution surpasses the values of k/2, it stops to increase. It means that ecosystem collapsed under the weight of pollution.

<!-- b000510 | prose | pages [18] -->
The results can be seen by the following figure:

<!-- b000511 | furniture | pages [18] -->


<!-- b000512 | furniture | pages [18] -->


<!-- b000513 | furniture | pages [18] -->


<!-- b000514 | furniture | pages [18] -->


<!-- b000515 | furniture | pages [18] -->


<!-- b000516 | furniture | pages [18] -->


<!-- b000517 | furniture | pages [18] -->


<!-- b000518 | furniture | pages [18] -->


<!-- b000519 | furniture | pages [18] -->


<!-- b000520 | furniture | pages [19] -->
Team# 1916129

<!-- b000521 | furniture | pages [19] -->


<!-- b000522 | furniture | pages [19] -->
Page 18 of 20

<!-- b000523 | furniture | pages [19] -->


<!-- b000524 | caption | pages [19] -->
Figure 5. Results with Different K

<!-- b000525 | furniture | pages [19] -->


<!-- b000526 | heading | pages [19] -->
8 Strength and Weakness

<!-- b000527 | heading | pages [19] -->
8.1 Strength

<!-- b000528 | prose | pages [19] -->
 The model comprehensively considers multiple factors such as ecosystem services and environmental

<!-- b000529 | prose | pages [19] -->
degradation.  We estimates the value of ecosystem services by opportunity cost and shadow cost, which can reflect

<!-- b000530 | prose | pages [19] -->
real value objectively.  We use the negative feedback form of artificial neural network to construct our ecosystem self-recover

<!-- b000531 | prose | pages [19] -->
model originally.  Based on the model we conducted, we have a further discussion about the Green GDP and talk about

<!-- b000532 | prose | pages [19] -->
the expression of Pigou tax for the externalities problem.

<!-- b000533 | heading | pages [19] -->
8.2 Weakness

<!-- b000534 | prose | pages [19] -->
 Limited by our knowledge, there exists some factors that we fail to consider.  We do not consider the factor of inflation. Therefore, there may be errors in project costs.  Due to the limitation of space and data, we cannot do the cost analysis of land engineering in different

<!-- b000535 | prose | pages [19] -->
zones.  The cost-benefit analysis of steel mill could be not representative for we selected a steel mill with high

<!-- b000536 | prose | pages [19] -->
profit rate for example.

<!-- b000537 | furniture | pages [19] -->


<!-- b000538 | furniture | pages [20] -->
Team# 1916129

<!-- b000539 | furniture | pages [20] -->


<!-- b000540 | furniture | pages [20] -->
Page 19 of 20

<!-- b000541 | heading | pages [20] -->
9 Further Discussion

<!-- b000542 | heading | pages [20] -->
9.1 Pigou Tax for Externalities of Natural Resources

<!-- b000543 | prose | pages [20] -->
Externality refers to the non-marketable influence of economic activities of economic subjects (including manufacturers and individuals) on others or society. Environmental pollution we discussed above is a typical negative externality, which do harm to the ecosystem and society. Both policy makers and business decision makers should consider the cost of Ecosystem services while making decisions. Then we will discuss the establishment of the Pigou tax levied on polluters.

<!-- b000544 | prose | pages [20] -->
The target of Pigou tax is to equalize the gap between the private and social costs of polluters' production by the way of levying. From the model we built above, the Pigou tax can be formulated as the following formula:

<!-- b000545 | prose | pages [20] -->
T𝑝= C𝑑𝑒𝑔+ C𝑑

<!-- b000546 | furniture | pages [20] -->


<!-- b000547 | prose | pages [20] -->
(37)

<!-- b000548 | prose | pages [20] -->
Where, T𝑝 is Pigou tax for a specific land use project, C𝑑𝑒𝑔 is the cost of environmental degradation, C𝑑 is the cost of derivative effects of pollution.

<!-- b000549 | heading | pages [20] -->
9.2 Inspiration to the Expression of Green GDP

<!-- b000550 | heading | pages [20] -->
9.2.1 Traditional Accounting of Green GDP

<!-- b000551 | prose | pages [20] -->
Green GDP refers to Gross domestic product (GDP) accounting considering the ecosystem services. Based on the traditional GDP accounting system, the value of Green GDP is the value of GDP after deducting the cost of natural resources and cost of environmental pollution. It can be represented by the following formula:

<!-- b000552 | prose | pages [20] -->
EDP = NDP −C𝑟𝑒𝑠−C𝑝𝑜𝑙

<!-- b000553 | furniture | pages [20] -->


<!-- b000554 | prose | pages [20] -->
(38)

<!-- b000555 | prose | pages [20] -->
Where, EDP is Green GDP, NDP is net domestic product, C𝑟𝑒𝑠 is the non-market consumption of natural resources, and C𝑝𝑜𝑙 is the cost of environmental pollution.

<!-- b000556 | heading | pages [20] -->
9.2.2 Innovative Expression of Green GDP

<!-- b000557 | prose | pages [20] -->
In the previous section, we put forward the concept of natural resources consumption. We use it to represent the initial production cost, which can reflect the total natural resource input in the entity district.

<!-- b000558 | heading | pages [20] -->
9.2.2.1 General Assumption

<!-- b000559 | prose | pages [20] -->
 All of the capital input come from nature.  All of the labor input come from the consumption of natural resources consumption.  All of the labors are put into production.  There is no natural resources escaping from the ecosystem.

<!-- b000560 | furniture | pages [20] -->


<!-- b000561 | furniture | pages [21] -->
Team# 1916129

<!-- b000562 | heading | pages [21] -->
9.2.2.2 Process of Calculability

<!-- b000563 | furniture | pages [21] -->


<!-- b000564 | furniture | pages [21] -->


<!-- b000565 | furniture | pages [21] -->
Page 20 of 20

<!-- b000566 | prose | pages [21] -->
Firstly, we replace the capital input and labor input with the previous natural resources consumption. GDP can be calculated with the total natural resources consumption.

<!-- b000567 | furniture | pages [21] -->


<!-- b000568 | prose | pages [21] -->
𝑛

<!-- b000569 | prose | pages [21] -->
) (39)

<!-- b000570 | prose | pages [21] -->
GDP𝑛= σ(C𝑟𝑒𝑠,𝑛+ ∑δ ∙C𝑖𝑛𝑝,𝑖

<!-- b000571 | prose | pages [21] -->
𝑖=𝑜

<!-- b000572 | prose | pages [21] -->
Where, GDP𝑛 is GDP in year n, C𝑟𝑒𝑠,𝑛 is the natural resourced consumption in year n, σ is production efficiency, δ is resource depreciation rate, and C𝑖𝑛𝑝,𝑖 is the natural resources input generated in year i.

<!-- b000573 | prose | pages [21] -->
On this basis, the value of Green GDP in year n is the previous results minus the pollution treatment costs, pollution derivative effects and environmental degradation losses generated in all processing processes. The following formula represent the whole process:

<!-- b000574 | prose | pages [21] -->
EDP𝑛= GDP𝑛−C𝑝𝑜𝑙,𝑛−C𝑑𝑒𝑔,𝑛

<!-- b000575 | furniture | pages [21] -->


<!-- b000576 | prose | pages [21] -->
(40)

<!-- b000577 | prose | pages [21] -->
Where, GDP𝑛 is GDP in year n, C𝑝𝑜𝑙,𝑛 is the cost of environmental pollution in year n, C𝑑𝑒𝑔,𝑛 is the cost of environmental degradation in year n.

<!-- b000578 | furniture | pages [21] -->


<!-- b000579 | furniture | pages [21] -->


<!-- b000580 | furniture | pages [21] -->


<!-- b000581 | furniture | pages [22] -->
Team# 1916129

<!-- b000582 | furniture | pages [22] -->


<!-- b000583 | furniture | pages [22] -->


<!-- b000584 | prose | pages [22] -->
Appendix-1

<!-- b000585 | heading | pages [22] -->
Appendix

<!-- b000586 | heading | pages [22] -->
I. Reference

<!-- b000587 | prose | pages [22] -->
[1] Chee, Y., 2004. An ecological perspective on the valuation of ecosystem services. Biological Conservation 120, 549-565. [2] Costanza, R., d’Arge, R., de Groot, R., Farber, S., Grasso, M., Hannon, B., Limburg, K., Naeem, S., O’Neill, R.V., Paruelo, J., Raskin, R.G., Sutton, P., van den Belt, M., 1997. The value of the world’s ecosystem services and natural capital. Nature 387, 253– 260. [3] Richmond, A., Kaufmann R., Myneni, R., 2007, Valuing ecosystem services: A shadow price for net primary production. Ecological Economics 64, 454-462. [4] Xuning Qiao, Linfeng Wang, Haipeng Niu, Yalin Yang, Yangyang Gu,2016. Ecological and economic coordination analysis of huaihe river basin in henan province based on NPP data. Economic Geography 36, 173-183. [5] Ke Liang, 2017. Estimation of land vegetation NPP in shaanxi province based on CASA model. [6] Liu MuYu, Chen FangFang. Research on environmental impact cost analysis model of bridge life cycle. Chinese journal of civil engineering,2010(43):373-378. [7] Yu Fang, Wang JinNan, Cao Dong. ,2009.Technical guide to environmental economic accounting in China. China science press. [8] Han Xiao, Zhiyun Ouyang, Jingzhu Zhao, Xiaoke Wang, 2000. Preliminary study on forest ecosystem service function and ecological economic value evaluation. [9] Weidong Han, Xiumei Gao, Changyi Lu, Peng Lin, 2000. Ecological value assessment of mangrove ecosystem in China. Ecological Science 19(1):40-46. [10] Zhuolin Li, 2014. Study on ecological value accounting of jishan jujube forest in Shanxi Province.

<!-- b000588 | heading | pages [22] -->
II. Cost of Ecological Service Data Sheet

<!-- b000589 | prose | pages [22] -->
House Cost of Ecosystem Services Subway Steel Mill 159.57 Oxygen 114.86 5,874.30 94.86 Carbon Dioxide 68.29 3,485.70 225.29 Water Purified 225.14 4,142.90 80.14 Soil Fertilizer 124.86 2,234.30 9.14 Dust Clean 7.14 674.30 130.00 Biodiversity 88.29 8,777.10 699.00 Cost of Pollution 628.57 25,188.60 171.43 COD 4,646,571.43 57,497,142.90 2,428.57 Cyanide 10,174,500.00 157,794,000.00 371.43 Harmful Metals 800,778.57 22,557,142.90 1,200.00 SO

<!-- b000590 | furniture | pages [22] -->


<!-- b000591 | prose | pages [22] -->
2,925,000.00 216,357,142.90

<!-- b000592 | furniture | pages [23] -->
Team# 1916129

<!-- b000593 | furniture | pages [23] -->


<!-- b000594 | furniture | pages [23] -->


<!-- b000595 | prose | pages [23] -->
Appendix-2

<!-- b000596 | prose | pages [23] -->
44.29 CO 476,000.00 9,646,285.70 242.86 NO 6,319,714.29 328,971,428.60 3,142.86 Dust 7,162,857.14 153,771,428.60 1,057.14 Smoke 838,000.00 38,200,000.00 28,571.43 General Industrial Solid Waste 7,685,000.00 222,600,000.00 3,285.71 Hazardous Waste 5,475,642.86 146,955,000.00 41,913.72 TOTAL

<!-- b000597 | furniture | pages [23] -->


<!-- b000598 | furniture | pages [23] -->


<!-- b000599 | prose | pages [23] -->
46,505,321.44 1,354,399,948.80

<!-- b000600 | furniture | pages [23] -->

