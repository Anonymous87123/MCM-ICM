# P-A-2021-2122025-d8c8e767

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | front_matter | pages [1] -->
Problem Chosen

<!-- b000003 | furniture | pages [1] -->
2021

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM

<!-- b000006 | title | pages [1] -->
A

<!-- b000007 | furniture | pages [1] -->
2122025

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
Fungal Decomposition Modeling via Stochastic Gradient

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | title | pages [1] -->
Descent and Cellular Automata

<!-- b000012 | prose | pages [1] -->
Fungus plays an important role as decomposers in the ecosystem. However, the efﬁciency of fungal growth and decomposition is inﬂuenced by the environment and the interaction among different species of fungi. Therefore, the study of factors affecting fungal activity is important.

<!-- b000013 | prose | pages [1] -->
In this paper, we establish relation models among the factors that affect the extension rate and decomposition rate of the fungi. Based on the relation models, we introduce the cellular automata model to simulate the growth and decomposition of multiple species of fungi.

<!-- b000014 | prose | pages [1] -->
Speciﬁcally, we ﬁrst establish the extension rate model. The extension rate is modeled as Arrhenius relation to the temperature and the humidity. Based on the extension rate model, we establish the decomposition rate model. The decomposition rate is determined by extension rate and moisture trade-off, where the relation is nonlinear. To estimate the parameters in the

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
nonlinear decomposition rate model, we establish an optimization model that ﬁts the collected decomposition rate data. The stochastic gradient descent (SGD) algorithm is utilized to solve the nonlinear optimization problem. The stable convergence behavior shows the effectiveness of the algorithm.

<!-- b000017 | prose | pages [1] -->
Based on the decomposition rate model, we establish the cellular automata model to simu- late the growth and decomposition of the fungi. The extension rate and decomposition rate are utilized to determine the rules of cellular automata. The simulation results show that under the same environment, the number of different species of fungi increased signiﬁcantly at the ﬁrst 5−10 days. Then, after about 10 days of extension, the number of fungi decreases to a certain extent and then stabilized after about 40 days. The decomposition rate after 122 days is 0.68.

<!-- b000018 | prose | pages [1] -->
Next, we describe the interactions among different species of fungi by competitive relation- ship. To describe the competitive relationship, we propose a deﬁnition to measure the reduction of the extension rate. Based on this deﬁnition, we establish the cellular automata model under fungal interactions to simulate the fungal activity under interactions. The results show that after considering the interaction, the number of different types of fungi is considerably decreased by an average percentage of 33.65%. And the decomposition rate after 122 days is 0.39, which is 42.69% lower than that of the situation without competition.

<!-- b000019 | prose | pages [1] -->
Afterward, we analyze the inﬂuence of fungal interactions. In the short term, the interaction between different types of fungi is not obvious. In the long-term, the inﬂuence is signiﬁcant due to the shortage of nutrients. Afterward, the sensitivity of our models is studied. We show that our models are sensitive to 8% change of temperature and humidity. Then, the analysis of combinations of fungi and different environments are included. The dominant and disad- vantaged species in different situations are obtained, e.g., Trichoderma becomes the dominant species in the tropical rain forest after 122 days with the decomposition rate of 68.29%. At last, we analyze the importance of biodiversity. The results show that biodiversity is important to the efﬁciency of fungal decomposition, where the decomposition rate of fungi under multi-species is 2.89 times higher than that of single species.

<!-- b000020 | keywords | pages [1] -->
Keywords: Fungal decomposition, Stochastic gradient descent, Nonlinear, Cellular automata

<!-- b000021 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000022 | prose | pages [1] -->
关注数学模型

<!-- b000023 | furniture | pages [1] -->
2

<!-- b000024 | furniture | pages [1] -->
MATHmodels

<!-- b000025 | furniture | pages [1] -->
获取更多资讯

<!-- b000026 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000027 | heading | pages [2] -->
Contents

<!-- b000028 | contents | pages [2] -->
1 Introduction

<!-- b000029 | contents | pages [2] -->
2

<!-- b000030 | contents | pages [2] -->
1.1

<!-- b000031 | contents | pages [2] -->
Problem Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000032 | contents | pages [2] -->
2

<!-- b000033 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000034 | contents | pages [2] -->
1.2

<!-- b000035 | contents | pages [2] -->
Restatement of Problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
2

<!-- b000037 | contents | pages [2] -->
1.3

<!-- b000038 | contents | pages [2] -->
Literature Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000039 | contents | pages [2] -->
3

<!-- b000040 | contents | pages [2] -->
1.4

<!-- b000041 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [2] -->
3

<!-- b000043 | contents | pages [2] -->
2 Assumptions and Notations

<!-- b000044 | contents | pages [2] -->
4

<!-- b000045 | contents | pages [2] -->
2.1

<!-- b000046 | contents | pages [2] -->
Assumptions

<!-- b000047 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
4

<!-- b000049 | contents | pages [2] -->
2.2

<!-- b000050 | contents | pages [2] -->
Notations

<!-- b000051 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
5

<!-- b000053 | contents | pages [2] -->
3 Models and Results

<!-- b000054 | contents | pages [2] -->
5

<!-- b000055 | contents | pages [2] -->
3.1

<!-- b000056 | contents | pages [2] -->
Decomposition Rate Model and Parameters Estimation . . . . . . . . . . . . .

<!-- b000057 | contents | pages [2] -->
5

<!-- b000058 | contents | pages [2] -->
3.1.1

<!-- b000059 | contents | pages [2] -->
Decomposition Rate Based on Extension Rate and Moisture Trade-off .

<!-- b000060 | contents | pages [2] -->
6

<!-- b000061 | contents | pages [2] -->
3.1.2

<!-- b000062 | contents | pages [2] -->
Extension Rate Based on Temperature and Humidity . . . . . . . . . .

<!-- b000063 | contents | pages [2] -->
7

<!-- b000064 | contents | pages [2] -->
3.1.3

<!-- b000065 | contents | pages [2] -->
Moisture Trade-off Based on Lower Limit of Humidity . . . . . . . . .

<!-- b000066 | contents | pages [2] -->
7

<!-- b000067 | contents | pages [2] -->
微信号：MATHmodels

<!-- b000068 | contents | pages [2] -->
3.1.4

<!-- b000069 | contents | pages [2] -->
Fungal Decomposition Rate Model

<!-- b000070 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [2] -->
8

<!-- b000072 | contents | pages [2] -->
3.1.5

<!-- b000073 | contents | pages [2] -->
Parameters Estimation Using SGD . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
8

<!-- b000075 | contents | pages [2] -->
3.2

<!-- b000076 | contents | pages [2] -->
Cellular Automata Model for Breakdown Process . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
10

<!-- b000078 | contents | pages [2] -->
3.2.1

<!-- b000079 | contents | pages [2] -->
Relation Between Cellular and Fungal Extension . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
10

<!-- b000081 | contents | pages [2] -->
3.2.2

<!-- b000082 | contents | pages [2] -->
Relation Between Cellular and Fungal Decomposition

<!-- b000083 | contents | pages [2] -->
. . . . . . . . .

<!-- b000084 | contents | pages [2] -->
11

<!-- b000085 | contents | pages [2] -->
3.2.3

<!-- b000086 | contents | pages [2] -->
Cellular Automata Model

<!-- b000087 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000088 | contents | pages [2] -->
12

<!-- b000089 | contents | pages [2] -->
3.2.4

<!-- b000090 | contents | pages [2] -->
Model Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000091 | contents | pages [2] -->
12

<!-- b000092 | contents | pages [2] -->
3.3

<!-- b000093 | contents | pages [2] -->
Cellular Automata Model Under Interactions Among Fungi . . . . . . . . . . .

<!-- b000094 | contents | pages [2] -->
12

<!-- b000095 | contents | pages [2] -->
3.3.1

<!-- b000096 | contents | pages [2] -->
Model Establishment . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [2] -->
13

<!-- b000098 | contents | pages [2] -->
3.3.2

<!-- b000099 | contents | pages [2] -->
Model Solution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [2] -->
14

<!-- b000101 | contents | pages [2] -->
3.4

<!-- b000102 | contents | pages [2] -->
Analysis and Experimental Results . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000103 | contents | pages [2] -->
14

<!-- b000104 | contents | pages [2] -->
3.4.1

<!-- b000105 | contents | pages [2] -->
Overall Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [2] -->
15

<!-- b000107 | contents | pages [2] -->
3.4.2

<!-- b000108 | contents | pages [2] -->
Interactions Among Different fungi . . . . . . . . . . . . . . . . . . .

<!-- b000109 | contents | pages [2] -->
15

<!-- b000110 | contents | pages [2] -->
3.4.3

<!-- b000111 | contents | pages [2] -->
Sensitive Analysis of Environment . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [2] -->
16

<!-- b000113 | contents | pages [2] -->
3.4.4

<!-- b000114 | contents | pages [2] -->
Simulations Under Different Combinations and Regions . . . . . . . .

<!-- b000115 | contents | pages [2] -->
17

<!-- b000116 | contents | pages [2] -->
3.5

<!-- b000117 | contents | pages [2] -->
Inﬂuence of Species Diversity

<!-- b000118 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000119 | contents | pages [2] -->
19

<!-- b000120 | contents | pages [2] -->
4 Strengths and Weaknesses

<!-- b000121 | contents | pages [2] -->
20

<!-- b000122 | contents | pages [2] -->
4.1

<!-- b000123 | contents | pages [2] -->
Strengths

<!-- b000124 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000125 | contents | pages [2] -->
20

<!-- b000126 | contents | pages [2] -->
4.2

<!-- b000127 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000128 | contents | pages [2] -->
20

<!-- b000129 | contents | pages [2] -->
5 Article

<!-- b000130 | contents | pages [2] -->
21

<!-- b000131 | contents | pages [2] -->
References

<!-- b000132 | contents | pages [2] -->
23

<!-- b000133 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000134 | contents | pages [2] -->
关注数学模型

<!-- b000135 | furniture | pages [2] -->
2

<!-- b000136 | furniture | pages [2] -->
MATHmodels

<!-- b000137 | furniture | pages [2] -->
获取更多资讯

<!-- b000138 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000139 | furniture | pages [3] -->
Team # 2122025

<!-- b000140 | furniture | pages [3] -->
Page 2 of 24

<!-- b000141 | heading | pages [3] -->
1 Introduction

<!-- b000142 | heading | pages [3] -->
1.1 Problem Background

<!-- b000143 | prose | pages [3] -->
微信公众号：数学模型 The material cycle in a forest ecosystem includes two relative processes: biosynthesis and biodegradation [1]. The former is the organic process of inorganic matter, which is mainly com- pleted by green plants and some inorganic nutrient microorganisms. The latter is the inorganic process of organic matter, which is mainly completed by forest microorganisms, which is the decomposition process of forest litter.

<!-- b000144 | prose | pages [3] -->
Forest litter is not only an important part of the ecosystem but also the main source of energy required by plants and microorganisms. Forest litter contains different chemical substances: cellulose, hemicellulose, lignin, water-soluble, ether soluble and alcohol soluble parts, protein, and minerals [2]. Fungi are one of the main members involved in the decomposition of various organic substances in soil. Many fungi can decompose cellulose, hemicellulose, and other similar compounds. At the same time, fungi can also decompose nitrogen-containing protein compounds and have a strong ability to decompose some refractory substances (such as lignin). 微信号：MATHmodels Therefore, fungi play an important role in material transformation [3].

<!-- b000145 | heading | pages [3] -->
1.2 Restatement of Problem

<!-- b000146 | prose | pages [3] -->
Fungi play a key role in the decomposition of woody ﬁbers and ground litter. Fungi is unique amongst the soil biota in their ability to translocate nutrients, a trait enabling them to establish extensive hyphal networks in a heterogeneous environment and to utilize spatially separated nutrient resources that may differ signiﬁcantly in nutrient quality [4].

<!-- b000147 | prose | pages [3] -->
Hyphae are the branch cells of fungi, which constitute the ﬁlaments and structures of fungi. Different kinds of hyphae play different roles in the life cycle of fungi. Mycelial elongation is essentially the growth rate of fungi [5]. We need to focus on several characteristics of fungi: the growth rate of the fungi, the fungi’ tolerance to moisture, and hyphal extension rate. Based on the above understanding, we need to solve the following problems:

<!-- b000148 | prose | pages [3] -->
• A mathematical model for the decomposition of litter and woody ﬁbers by fungi needs to be established in the presence of a variety of fungi.

<!-- b000149 | prose | pages [3] -->
• In the model, we need to combine the interaction among different kinds of fungi, which have different growth rates and different moisture tolerance.

<!-- b000150 | prose | pages [3] -->
• Analyze the model and describe the interaction among different types of fungi. The dy- namic characteristics and description of interactions should include short-term and long- term trends. Model analysis needs to account for sensitivity to rapid ﬂuctuations in the environment. Meanwhile, we need to determine the overall impact of changes in atmo- spheric trends to assess the impact of changes in local weather patterns.

<!-- b000151 | prose | pages [3] -->
• Forecast the relative strengths and weaknesses of each species and possible persistent species combination, as well as their status in different environments, including arid, semi-arid, temperate, arboreal, and tropical rainforests.

<!-- b000152 | prose | pages [3] -->
• Describe how the diversity of fungal communities in the system affects the overall efﬁ- ciency of the system in decomposing ground litters. Predict the importance and role of biodiversity.

<!-- b000153 | prose | pages [3] -->
• Write a two-page article. This article needs to be suitable as an introductory textbook for university biology to discuss the latest progress in our understanding of the role of fungi

<!-- b000154 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000155 | prose | pages [3] -->
关注数学模型

<!-- b000156 | furniture | pages [3] -->
2

<!-- b000157 | prose | pages [3] -->
in ecosystems.

<!-- b000158 | furniture | pages [3] -->
MATHmodels

<!-- b000159 | furniture | pages [3] -->
获取更多资讯

<!-- b000160 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000161 | furniture | pages [4] -->
Team # 2122025

<!-- b000162 | furniture | pages [4] -->
Page 3 of 24

<!-- b000163 | heading | pages [4] -->
1.3 Literature Review

<!-- b000164 | prose | pages [4] -->
The most obvious identity of fungi is decomposer. According to Chen M R [6], litter de- composition generally includes three stages: leaching stage, crushing stage, and organic matter 微信公众号：数学模型 catabolism stage. Among them, the leaching stage refers to that the soluble matter in the litter is washed away by water. Physical comminution, for instance, animal chewing, alternation of soil drying and wetting, freezing and thawing, precipitation, and other factors can crush the tree residues in varying degrees [6, 7]. Metabolism refers to the transformation of more complex organic compounds to simple salt and water molecules.

<!-- b000165 | prose | pages [4] -->
The catabolism of organic matter is generally accomplished by microorganisms. Yu shuling [8] proposed that fungi, especially ﬁlamentous fungi, play an important role in litter decompo- sition. Findlay et al. [1] pointed out the hyphae of fungi can penetrate into plant debris and secrete extracellular enzymes to degrade recalcitrant substances (such as lignin) contained in the litter, so as to soften plant debris, change the structure and chemical composition of litter, which is conducive to the further colonization of bacteria and other microorganisms and the feeding of soil animals [9, 10]. 微信号：MATHmodels The complete decomposition of litter is completed under the action of various litter decom- posing enzymes [11]. Dick [12] showed that the activities of litter decomposing enzymes were signiﬁcantly positively correlated with the microbial biomass. Zhang Ruiqing et al. [13] mea- sured a variety of enzymes related to the carbon cycle in the process of litter decomposition in the tropical rain forest, and pointed out that enzymes related to the carbon cycle can be used as an important indicator of organic matter decomposition.

<!-- b000166 | prose | pages [4] -->
Wang Qibing et al. [14] claimed that the decomposition rate of litter will increase with the increasing temperature [15]. The research results of Liu Qiang and Vitousek [14, 15] showed that the temperature will begin to decrease with the increasing altitude, and the decomposition rate will be signiﬁcantly reduced. Moore et al. [16] believed that on a large spatial scale, the annual average temperature was considered to be the dominant climate factor affecting forest litter decomposition. The decomposition rate of litter in each climate zone was tropical > subtropical > temperate > cold temperate [17, 18]. Under the action of high temperature and high humidity, the soil microbial activity in low latitude and low altitude areas is generally higher, the decomposition rate of litter is faster, and the accumulation rate of forest surface organic matter is slow. On the contrary, limited by low temperature, microbial activity in high latitude and high altitude areas is generally low, litter decomposition rate is slow, and forest surface organic matter accumulation is large [1, 16, 17].

<!-- b000167 | heading | pages [4] -->
1.4 Our Work

<!-- b000168 | prose | pages [4] -->
In this paper, we ﬁrst study the relationship among fungal extension rate, moisture trade-off, and decomposition rate. According to [5], the relationship among diffusion rate and decomposi- tion rate is determined as 1/2 order. In addition, the relationship among moisture trade-off and log decomposition rate is linear. Then we unify these three factors into a single nonlinear equa- tion. A multivariate nonlinear optimization model is established and is solved by SGD. In that case, the quantitative relationship among extension rate, moisture trade-off, and decomposition rate is established.

<!-- b000169 | prose | pages [4] -->
Then, we introduce cellular automata to simulate the growth and decomposition of fungi. We introduce three deﬁnitions to quantify decomposition rate and extension rate into cellular automata. Meanwhile, we consider the interaction among different species of fungi and the

<!-- b000170 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000171 | prose | pages [4, 5] -->
impact of different environments. Numerous simulation experiments are conducted to test the关注数学模型 robustness, sensitivity, and effectiveness of our models.

<!-- b000172 | furniture | pages [4] -->
2

<!-- b000173 | furniture | pages [4] -->
MATHmodels

<!-- b000174 | furniture | pages [4] -->
获取更多资讯

<!-- b000175 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000176 | furniture | pages [5] -->
Team # 2122025

<!-- b000177 | furniture | pages [5] -->
Page 4 of 24

<!-- b000179 | prose | pages [5] -->
In summarize, our models are as follows:

<!-- b000180 | prose | pages [5] -->
• The relationship among extension rate, moisture trade-off, and decomposition rate (7). 微信公众号：数学模型

<!-- b000181 | prose | pages [5] -->
• The nonlinear optimization model to ﬁx the undetermined factors of the relationship (8).

<!-- b000182 | prose | pages [5] -->
• The cellular automata model under multiple species of fungi (20).

<!-- b000183 | prose | pages [5] -->
• The cellular automata model under interactions among different fungi (22).

<!-- b000184 | prose | pages [5] -->
It is worth pointing out that the answers to the ﬁve questions are respcetively listed in Sec. 3.2 (the ﬁrst question), Sec. 3.3 (the second question), Sec. 3.4 (the third and fourth question), and Sec. 3.5 (the ﬁfth question).

<!-- b000185 | heading | pages [5] -->
2 Assumptions and Notations

<!-- b000186 | heading | pages [5] -->
2.1 Assumptions

<!-- b000187 | prose | pages [5] -->
微信号：MATHmodels Through the full analysis of the problem, in order to simplify our model, we make the following reasonable assumptions.

<!-- b000188 | prose | pages [5] -->
Assumption 1 Assuming that the effects of forest soil fertility, tree species, and forest age on litter decomposition are negligible.

<!-- b000189 | prose | pages [5] -->
The effect and inﬂuence on fungal decomposition are mainly limited to the environment and its own characteristic [10].

<!-- b000190 | prose | pages [5] -->
Assumption 2 Ignoring the impacts of external factors such as forest pests and animal activi- ties on the matrix quality and decomposition rate of forest litter.

<!-- b000191 | prose | pages [5] -->
Assumption 3 The effect of light intensity on fungal decomposition was not considered.

<!-- b000192 | prose | pages [5] -->
The intensity of light can lead to the difference of leaf structure and material composition [19]. Speciﬁcally, the intensity of light will affect the content of nutrients, cellulose, and lignin in leaves. This paper focuses on the inﬂuence of temperature and humidity, so the inﬂuence of light intensity is ignored in this paper.

<!-- b000193 | prose | pages [5] -->
Assumption 4 The phenomenon of alternation of drying and wetting, freezing and thawing caused by light and rainfall is not considered.

<!-- b000194 | prose | pages [5] -->
Assumption 5 Assuming that the decomposition of litter and woody ﬁber has gone through the leaching stage and comminution stage, the model is aimed at the catabolism stage of organic matter.

<!-- b000195 | prose | pages [5] -->
The nature of leaching and comminution stages requires additional analysis [6].

<!-- b000196 | prose | pages [5] -->
Assumption 6 It is assumed that due to the limitation of the actual situation, the fungi would never surpass its theoretical extension rate.

<!-- b000197 | prose | pages [5] -->
The theoretical maximum growth rate of the microorganism is based on ideal condition [5, 20]. Thus, it is not likely for the fungi to surpass the theoretical maximum growth rate.

<!-- b000198 | prose | pages [5] -->
Assumption 7 In reality, the growth of fungi has a lower limit of humidity. In order to simplify the model, we assume that the higher the humidity, the higher the extension rate.

<!-- b000199 | prose | pages [5] -->
There are lower limits of the humidity for the growth of the fungi [21]. However, as far as

<!-- b000200 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000201 | prose | pages [5] -->
关注数学模型

<!-- b000202 | furniture | pages [5] -->
2

<!-- b000203 | prose | pages [5] -->
we know, there are no upper limits. Thus, it is reasonable to make this assumption.

<!-- b000204 | furniture | pages [5] -->
MATHmodels

<!-- b000205 | furniture | pages [5] -->
获取更多资讯

<!-- b000206 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000207 | furniture | pages [6] -->
Team # 2122025

<!-- b000208 | furniture | pages [6] -->
Page 5 of 24

<!-- b000209 | heading | pages [6] -->
2.2 Notations

<!-- b000210 | prose | pages [6] -->
The primary notations used in this paper are listed in Table 1. In addition, a set containing element · is expressed as {·}. Different types of fungi are distinguished by subscripts i, e.g., 微信公众号：数学模型 Fi,VEi. Generally, symbols with the same capital letter but different subscripts represent the variables with similar properties, e.g., VE and VD both represent the rate, while VE denotes the extension rate and VD denotes the decomposition rate.

<!-- b000211 | caption | pages [6] -->
Table 1: Notations

<!-- b000212 | prose | pages [6] -->
Symbol Deﬁnition temperature (The unit is ◦C) T Tmax The most suitable temperature of a type of fungi Hl The lower limit of the humidity of a type of fungi λ,a,K The undetermined parameters in optimization model (3.3) L The square loss of the groud-truth data and the predict data VE Extension rate (The scope is [0,10] according to [5]) 微信号：MATHmodels VEmax The theoretical maximum extension rate Decomposition rate (The scope is [0,1]) VD The moisture trade-off (The scope is [−1,1] [5]) M Humidity (The scope is [0,1]) H The map in cellular automata (∈N500×500) G The set containing multiple cells, representing a type of fungi (⊂N2) Fi The number of cells infected by a type of fungi (Ni = |Fi|) Ni PEi The extension probability deﬁned in Deﬁnition 1 PCi The competitive-extension probability deﬁned in Deﬁnition 3 TDi The decomposition time deﬁned in Deﬁnition 2

<!-- b000213 | heading | pages [6] -->
3 Models and Results

<!-- b000214 | prose | pages [6] -->
This section describes the main models and results of our work. Speciﬁcally, Sec. 3.1 es- tablishes the relationship among extension rate, moisture trade-off, and the decomposition rate, where the SGD algorithm is utilized to determine the model parameters. Sec. 3.2 establishes the cellular automata model to describe the growth and decomposition process of the fungi. In Sec. 3.3, we add the interactions of different fungi and re-formulate the cellular automata model. In Sec. 3.4, we analyze the proposed models from the perspective of the connections of different factors, and the sensitivity to environmental change. Finally in Sec. 3.5, we analyze the importance of biodiversity to fungal growth and decomposition.

<!-- b000215 | prose | pages [6] -->
In order to better carry out our work, it is expected to collect multiple species of fungi and their parameters. Generally, the main components of ground litter and lignocellulose include lignin, cellulose, and hemicellulose. Thus, the types of fungi we select should be able to favor- ably decompose these elements. Based on the information on common types of fungi [5, 26], we collected 6 types of fungi, as listed in Table 2.

<!-- b000216 | heading | pages [6] -->
3.1 Decomposition Rate Model and Parameters Estimation

<!-- b000217 | prose | pages [6] -->
This section establishes the fungal decomposition rate model, which is considered via two aspects: the extension rate and the moisture trade-off. Our model is a general framework and could be applied to all types of fungi. Speciﬁcally, we ﬁrst qualitatively establish the relation-

<!-- b000218 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000219 | prose | pages [6, 7] -->
ship among decomposition rate and extension rate and moisture trade-off. Then, we establish关注数学模型 from the appendix of [5]).

<!-- b000220 | furniture | pages [6] -->
2

<!-- b000221 | furniture | pages [6] -->
MATHmodels

<!-- b000222 | furniture | pages [6] -->
获取更多资讯

<!-- b000223 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000224 | furniture | pages [7] -->
Team # 2122025

<!-- b000225 | furniture | pages [7] -->
Page 6 of 24

<!-- b000226 | caption | pages [7] -->
Table 2: The type of fungi selected and the corresponding parameters (Some parameters are selected

<!-- b000228 | prose | pages [7] -->
Tmax VEmax Hl M Fungal types 微信公众号：数学模型 28◦C −0.60 8.23 Trichoderma 80% 18◦C −0.80 6.46 Penicillium 90% 32◦C −0.84 5.17 Aspergillus 92% 25◦C −0.60 1.56 Rust fungi 80% 27◦C −0.80 7.26 Gibberella 90% 28◦C −0.40 4.68 Fusarium 70%

<!-- b000229 | prose | pages [7] -->
the relationship among extension rate and humidity and temperature. For the uncertain param- eters in the model, we use the data in the relevant literature [5] to determine these parameters by SGD, and ﬁnally we can determine the decomposition rate model.

<!-- b000230 | heading | pages [7] -->
3.1.1 Decomposition Rate Based on Extension Rate and Moisture Trade-off

<!-- b000231 | prose | pages [7] -->
微信号：MATHmodels The decomposition rate, which is deﬁned as the mass loss of the wood over 122 days [5], has high relations with the extension rate and the moisture trade-off. For the extension rate, we can observe that the decomposition rate increased with the increase of the extension rate. The magnitude of this increase is approximated by the power of 1/2, and the temperature T affects the decomposition rate with a constant ratio. Thus, the univariate function of decomposition rate with respect to the extension rate can be formulated as

<!-- b000232 | prose | pages [7] -->
1 E +V 1 VD = T ×V 2 D0, (1)

<!-- b000233 | prose | pages [7] -->
where VD denotes the decomposition rate, T denotes the temperature, VE denotes the extension rate, and V 1 D0 is a constant, which is undetermined.

<!-- b000234 | prose | pages [7] -->
The moisture trade-off M is deﬁned as the difference of each isolate’s competitive ranking and their moisture niche width [5]. It is believed that the fungi with a bigger moisture trade-off are likely to have a higher decomposition rate [5]. In fact, the linear correlation can be found among the moisture trade-off and logVD, i.e.,

<!-- b000235 | prose | pages [7] -->
logVD = α ×M +V 2 D0, (2)

<!-- b000236 | prose | pages [7] -->
where α is the linear coefﬁcient and V 2 D0 is a constant. Taking exponential function on both sides and let λ = 10VD0 and a = 10α, we have

<!-- b000237 | prose | pages [7] -->
VD = λaM. (3)

<!-- b000238 | prose | pages [7] -->
Here, λ,a become two undetermined parameters of the model.

<!-- b000239 | prose | pages [7] -->
Note that (1) and (3) are two independent functions that consider the inﬂuence of the exten- sion rate and the moisture trade-off, respectively. In fact, these two factors consistently affect the decomposition rate with a synchronous manner. Thus, it is expected to unify these two factors into a single model, which derives

<!-- b000240 | prose | pages [7] -->
1 E +λaM +K, VD = T ×V 2 (4)

<!-- b000241 | prose | pages [7] -->
where K is an undetermined constant.

<!-- b000242 | prose | pages [7] -->
In the fungi decomposition rate model (4), the independent variables are the extension rate

<!-- b000243 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000244 | prose | pages [7, 8] -->
VE and the moisture trade-off M. For M, the lower limit of the humidity of a speciﬁc specie of关注数学模型 fungi can be used to determine M [21]. However, for VE, it is depends on both the temperature and the humidity. Thus, it is of needs to establish a particular model to describe the relations among temperature, humidity, and the extension rate VE.

<!-- b000245 | furniture | pages [7] -->
2

<!-- b000246 | furniture | pages [7] -->
MATHmodels

<!-- b000247 | furniture | pages [7] -->
获取更多资讯

<!-- b000248 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000249 | furniture | pages [8] -->
Team # 2122025

<!-- b000250 | furniture | pages [8] -->
Page 7 of 24

<!-- b000252 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000253 | heading | pages [8] -->
3.1.2 Extension Rate Based on Temperature and Humidity

<!-- b000254 | prose | pages [8] -->
Fungi provide energy for themselves by decomposing organic matter. Since the decom- position mainly depends on the function of the enzyme, the activity of the decomposing en- zyme greatly affects the decomposing efﬁciency, thus affecting the growth rate of fungi [22]. Generally speaking, the activity of decomposing enzymes is highly related to temperature and humidity. Therefore, the growth rate of fungi depends on temperature and humidity.

<!-- b000255 | prose | pages [8] -->
According to [22], the temperature rise can be linearized by the Arrhenius diagram. The slope of the Arrhenius diagram gives the activation energy, which determines VE. Generally, the effect of humidity on the growth of fungi is positively correlated. However, for the temperature, too high temperature will inactivate the enzyme in the fungi. Therefore, we employ Tmax to express the temperature which causes inactivation. Beyond this temperature, the extension rate 微信号：MATHmodels would go down as the temperature still increase.

<!-- b000256 | prose | pages [8] -->
Based on the above analysis, we formulate the extension rate of the fungi with respect to the temperature T and the humidity H as the following Arrhenius diagram [23]:

<!-- b000257 | prose | pages [8] -->
 VEmax VE = VEmaxe− T×H , 0 ≤T ≤Tmax     VEmax (5) VE = VEmaxe− (2Tmax−T)×H , Tmax ≤T ≤2Tmax    VE = 0, other. 

<!-- b000258 | prose | pages [8] -->
where VEmax denotes the theoretical maximum extension rate (According to Assumption 6, due to the limitation of the actual situation, the fungi would never surpass its theoretical extension rate). For different species of fungi, the VEmax and Tmax are different. They are depend on the essential characteristics of the fungi.

<!-- b000259 | prose | pages [8] -->
In order to illustrate the rationality of the above model (5), we display the value of VE with respect to different T and H in Fig. 1. We can see that when the maximum extension rate VEmax of the fungi is large, the fungi are sensitive to the change of environment (temperature and humidity). For example, the yellow line in the Fig. 1 represents a maximum extension rate of 10. When the temperature or humidity changes a lot, the extension rate of these fungi is even lower than that of the fungi with a maximum extension rate of 2.5, which is represented by the blue line. That is to say, the fungi with a higher extension rate are not robust to the change of environment. This phenomenon is consistent with the analysis in the literature [5].

<!-- b000260 | heading | pages [8] -->
3.1.3 Moisture Trade-off Based on Lower Limit of Humidity

<!-- b000261 | prose | pages [8] -->
For the moisture trade-off M (whose scope is [−1,1] [5]), we directly use the lower limit data of the humidity to induce M. Speciﬁcally, according to [21], the lower limit of humidity Hl of a species of fungi is deﬁnite (The scope is [0,1]). Besides, the lower this limit is, the higher the moisture trade-off of the fungi species would be, as expounded in Assumption 7. Thus, we directly formulate M with linear correlation to Hl, i.e.,

<!-- b000262 | prose | pages [8] -->
M = −2Hl +1. (6)

<!-- b000263 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000264 | prose | pages [8, 9] -->
关注数学模型 微信公众号：数学模型

<!-- b000265 | furniture | pages [8] -->
2

<!-- b000266 | furniture | pages [8] -->
MATHmodels

<!-- b000267 | furniture | pages [8] -->
获取更多资讯

<!-- b000268 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000269 | furniture | pages [9] -->
Team # 2122025

<!-- b000270 | furniture | pages [9] -->
Page 8 of 24

<!-- b000272 | caption | pages [9] -->
Figure 1: The test of the extension rate model (5). Left: the value of VE with respect to different

<!-- b000273 | prose | pages [9] -->
temperature T with ﬁxed H = 0.8. Right: the value of VE with respect to different humidity H with ﬁxed T = 38. The optimum temperature Tmax is set as 38.

<!-- b000274 | heading | pages [9] -->
3.1.4 Fungal Decomposition Rate Model

<!-- b000275 | prose | pages [9] -->
微信号：MATHmodels Based on the above analysis, the ﬁnal model of the fungal decomposition rate is

<!-- b000276 | prose | pages [9] -->
 1 E +λaM +K VD = T ×V 2     λ,a,K ∈R      M = −2Hl +1    (7) VEmax VE = VEmaxe− T×H , 0 ≤T ≤Tmax     VEmax  VE = VEmaxe− (2Tmax−T)×H , Tmax ≤T ≤2Tmax       VE = 0, other. 

<!-- b000277 | heading | pages [9] -->
3.1.5 Parameters Estimation Using SGD

<!-- b000278 | prose | pages [9] -->
In order to establish a deﬁnite relationship of extension rate, moisture trade-odd, and the decomposition rate, we need to estimate the undetermined parameters λ,a,K in model (7). Speciﬁcally, these parameters should be determined according to the data. Our data come from the appendix of [5]. The equation (4) is a multi-parameters undetermined nonlinear equation. Therefore, it is expected to determine these parameters via minimizing the error among the decomposition rate data at hand and the predicted decomposition rate, which could be described as the following optimization model:

<!-- b000279 | prose | pages [9] -->
{λ ∗,a∗,K∗} = arg min (V i D −V i Ddata)2, {λ,a,K}∑ i (8) 1 2 +λaMi V i D = T i data ×V i data +K. Edata

<!-- b000280 | prose | pages [9] -->
Here, {T i data,V i Edata,Mi data,V i Ddata} are the set of data obtained from [5]. The above optimization model aims at minimizing the square error of the ground-truth data VDdata and the predicted data VD using (4).

<!-- b000281 | prose | pages [9] -->
It is hard to ﬁnd the closed-form solution of model (8) . Hence, it is of necessity to use it- erative methods. In solving unconstrained optimization problems, the iterative gradient descent

<!-- b000282 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000283 | prose | pages [9, 10] -->
is one of the most commonly used methods. Since there is multiple data, we introduce the SGD关注数学模型 algorithm [24], which is highly efﬁcient under multiple data, to tackle model (8). Speciﬁcally, we update θ = {λ,a,K} via θt+1 = θt −r∇θL, (9) Ddata)2 is the energy function, r is the updating rate [24], and t = 1,2,··· ,I where L = (V i D −V i 微信公众号：数学模型 denotes the iteration step. Concretely, we have the following updating rules:

<!-- b000284 | furniture | pages [9] -->
2

<!-- b000285 | furniture | pages [9] -->
MATHmodels

<!-- b000286 | furniture | pages [9] -->
获取更多资讯

<!-- b000287 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000288 | furniture | pages [10] -->
Team # 2122025

<!-- b000289 | furniture | pages [10] -->
Page 9 of 24

<!-- b000291 | prose | pages [10] -->
λ-updating:

<!-- b000292 | prose | pages [10] -->
λt+1 = λt −r ∂L Ddata)×atMi ∂λ = λt −2r(V i D −V i data. (10)

<!-- b000293 | prose | pages [10] -->
a-updating:

<!-- b000294 | prose | pages [10] -->
at+1 = at −r∂L dataat(Mi ∂a = at −2r(V i data−1). D −V i Ddata)×λMi (11)

<!-- b000295 | prose | pages [10] -->
K-updating:

<!-- b000296 | prose | pages [10] -->
Kt+1 = Kt −r ∂L ∂K = Kt −2r(V i D −V i Ddata). (12) 微信号：MATHmodels The optimization process is described in Table 3.

<!-- b000297 | caption | pages [10] -->
Table 3: The solution of the proposed model (8).

<!-- b000298 | heading | pages [10] -->
Algorithm 1: Parameters estimation using SGD

<!-- b000299 | prose | pages [10] -->
r, I, dataset {T i data,V i Edata,Mi data,V i Ddata}N 1: input: i=1 2: Initialize λ 0 = 1,a0 = 1,K0 = 1;

<!-- b000300 | prose | pages [10] -->
3: for k = 1 : I 4: t=mod(k,N);

<!-- b000301 | prose | pages [10] -->
5: Update λ via (10);

<!-- b000302 | prose | pages [10] -->
Update a via (11); 6:

<!-- b000303 | prose | pages [10] -->
Update K via (12); 7:

<!-- b000304 | prose | pages [10] -->
8: end for λ I,aI,KI 9: output:

<!-- b000305 | prose | pages [10] -->
The loss value (L) and λ with respect to the iteration is shown in Fig. 2. We can see that during the SGD iteration, the loss gradually converges to a relatively small value, and the λ converges to 31.9 stably. Although we use SGD, where the loss value is locally unstable. However, the SGD algorithm can accelerate the iteration and convergence speed [24].

<!-- b000306 | prose | pages [10] -->
Finally, we have λ = 31.90,a = 1.26,K = −64.80, which deduces

<!-- b000307 | prose | pages [10] -->
1 E +31.90×1.26M −64.80. VD = T ×V 2 (13)

<!-- b000308 | prose | pages [10] -->
Based on th above solution, the calculation model of decomposition rate and extension rate are simultaneously described as follows:

<!-- b000309 | prose | pages [10] -->
1  E +31.90×1.26M −64.80 VD = T ×V 2     M = −2Hl +1     VEmax  VE = VEmaxe− T×H , 0 ≤T ≤Tmax (14)  VEmax  VE = VEmaxe−  (2Tmax−T)×H , Tmax ≤T ≤2Tmax  

<!-- b000310 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000311 | prose | pages [10, 11] -->
 关注数学模型   VE = 0, other.  微信公众号：数学模型 Iteration

<!-- b000312 | furniture | pages [10] -->
2

<!-- b000313 | furniture | pages [10] -->
MATHmodels

<!-- b000314 | furniture | pages [10] -->
获取更多资讯

<!-- b000315 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000316 | furniture | pages [11] -->
Team # 2122025

<!-- b000317 | furniture | pages [11] -->
Page 10 of 24

<!-- b000319 | caption | pages [11] -->
Figure 2: The loss value (L) and λ with respect to the iteration using algorithm in Table 3.

<!-- b000320 | prose | pages [11] -->
Speciﬁcally, given the temperature T and humidity H, we can compute the extension rate VE of different species of fungi with different VEmax,Tmax. Next, the decomposition rate VD is com- puted by combining the extension rate VE and the moisture trade-off M (determined by the tolerance of different fungi to water). This model provides the basis for our cellular automata model to simulate the decomposition of organic matter by fungi.

<!-- b000321 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000322 | heading | pages [11] -->
3.2 Cellular Automata Model for Breakdown Process

<!-- b000323 | prose | pages [11] -->
The ﬁrst question is to model the breakdown process by the fungi. In practice, the rate of decomposition by fungi is not constant due to various conditions, so the decomposition time is dynamic. In order to better simulate the decomposition process, we suggest the cellular automata to address this problem.

<!-- b000324 | prose | pages [11] -->
Speciﬁcally, the set (containing multiple cells) that represents the fungi is denoted by Fi ⊂ N2. The whole map grid (represents the woody ﬁbers) is G ∈N500×500. At the beginning stage, every grid is set to 1, i.e., G(p,q) = 1,∀s,t. Then, for each grid, there is a initial possibility to be infected by the fungi Fi (if (p,q) is infected by Fi, then we update G(p,q) = i + 1). After the initialization, Fi begins to extend to other grids. Once Fi extends to a new grid, it begins to decompose this grid, which takes some time. After the decomposition, the wood disappears, and the fungi on the grid die for lack of hosts. The whole simulation process of cellular automata describes the dynamic process of fungi growth and decomposition on wood. However, some parameters in cellular automata, such as the rules of invading adjacent cells and the decomposition time, need to be further determined.

<!-- b000325 | prose | pages [11] -->
Here, we use the extension rate VE and decomposition rate VD that we calculated before to determine the parameters in the cellular automata.

<!-- b000326 | heading | pages [11] -->
3.2.1 Relation Between Cellular and Fungal Extension

<!-- b000327 | prose | pages [11] -->
For the extension process of fungi, we use the infection of adjacent cells in cellular automata as the simulation of growth. Naturally, this process is parameterized by the extension rate VE. However, we can not directly use VE in the cellular automata since the simulation process is a discrete process. In such a condition, not only the number but also the position of the cells should be studied. Thus, we propose to transform VE into a probability factor to determine whether an uninfected grid would be infected by the fungi in the adjacent grid.

<!-- b000328 | prose | pages [11] -->
According to [25], the sigmoid function can commendably describe the process of biological growth. For fungi, it is also a kind of organism, so some of its behaviors and characteristics can be simulated by sigmoid function. Given the extension rate VE, we propose to use sigmoid function to transform VE into a controllable probability factor. The probability (determined via

<!-- b000329 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000330 | prose | pages [11, 12] -->
the extension rate VE) of a fungus is used to determine whether the fungi cell Fi could extend关注数学模型 into adjacent lattices. Speciﬁcally, we induce the following deﬁnition.

<!-- b000331 | furniture | pages [11] -->
2

<!-- b000332 | furniture | pages [11] -->
MATHmodels

<!-- b000333 | furniture | pages [11] -->
获取更多资讯

<!-- b000334 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000335 | furniture | pages [12] -->
Team # 2122025

<!-- b000336 | furniture | pages [12] -->
Page 11 of 24

<!-- b000338 | prose | pages [12] -->
Deﬁnition 1 (Extension probability) Given the fungi cell Fi with extension rate VEi, the exten- sion probability of Fi is deﬁned as 微信公众号：数学模型 PEi = sigmoid( 1 1 ) = . (15) −1 VEi VEi 1+e

<!-- b000339 | prose | pages [12] -->
This probability is used to determine the extent of the growth of the fungi cell. Speciﬁcally, for each uninfected cell, if it is adjacent to an infected fungi Fi, then the grid may be infected with probability PEi, which is determined by the extension rate VE. When the extension rate increases, PEi increases (with upper limit 1). Then the probability of cell infection increases, which on the other hand describes the rate of the fungal extension. Thus, the validity of Deﬁni- tion 1 is justiﬁed.

<!-- b000340 | prose | pages [12] -->
Based on the above analysis, for each grid (p,q) that is not being infected, we do the fol- lowing operation in the time t:

<!-- b000341 | prose | pages [12] -->
( = Ft Ft+1 i ∪{(p,q)}, ξ ≤PEi 微信号：MATHmodels i (16) Ft+1 = Ft i , ξ > PEi, i where ξ ∼U(0,1). The above formula is the growth simulation process of fungi. Note that there are grids {pt D,qt D} that being fully decomposed by the fungi Fi, thus we do Ft+1 = Ft+1 \{(pt D,qt D)}. (17) i i For the total number of fungi Ni (the number of grids infected by Fi), we have Ni = |Fi|, where |·| denotes the number of elements in the set. For the variation of the number of cells infected by fungi, we have the following differential form:

<!-- b000342 | prose | pages [12] -->
dNi dt = (Nt+1 −Nt i )−Nt Di, (18) i

<!-- b000343 | prose | pages [12] -->
where Nt Di denotes the number of cells that fully decomposed by the fungi Fi at time t. The equation (18) is crucial since we can use it to observe the variation of the number of fungi in the simulation process.

<!-- b000344 | heading | pages [12] -->
3.2.2 Relation Between Cellular and Fungal Decomposition

<!-- b000345 | prose | pages [12] -->
Similar to the extension rate, the decomposition rate can not be directly used in the cellular automata model. Therefore, it is of necessity to convert the decomposition rate calculated pre- viously into the decomposition time of a fungus to fully decompose a cell that being infected. Naturally, when the decomposition rate is high, the decomposition time is relatively low [26]. Therefore, we propose the following deﬁnition of decomposition time.

<!-- b000346 | prose | pages [12] -->
Deﬁnition 2 (Decomposition time) The decomposition time of fungi Fi with decomposition rate VDi, which is the time of a fungus in a cell to fully decompose the woody ﬁber, is deﬁned as 122 TDi = c VDi ×5002, (19)

<!-- b000347 | prose | pages [12] -->
where c is a correction factor. The unit of TDi is day.

<!-- b000348 | prose | pages [12] -->
122 is the number of days in the expeirments in [5], and 500 is the size of G. In our work, c is set as 5×106. Given the decomposition time TDi, we can simulate the decomposition process of the fungi in a cell. Consequently, according to Eq. (17), the decomposition time is a factor

<!-- b000349 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000350 | prose | pages [12] -->
关注数学模型

<!-- b000351 | furniture | pages [12] -->
2

<!-- b000352 | prose | pages [12] -->
that inﬂuences the cellular automata model.

<!-- b000353 | furniture | pages [12] -->
MATHmodels

<!-- b000354 | furniture | pages [12] -->
获取更多资讯

<!-- b000355 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000356 | furniture | pages [13] -->
Team # 2122025

<!-- b000357 | furniture | pages [13] -->
Page 12 of 24

<!-- b000358 | heading | pages [13] -->
3.2.3 Cellular Automata Model

<!-- b000359 | prose | pages [13] -->
Based on the above analysis, let n denots the number of fungal species, the proposed cellular automata model to simulate the decomposition process is formulated as:

<!-- b000360 | prose | pages [13] -->
微信公众号：数学模型  Ft+1 = (Ft i ∪{(p,q)})\{(pt D,qt D)}, ξ ≤PEi i    Ft+1 = Ft i \{(pt D,qt  D)}, ξ > PEi  i     ξ ∼U(0,1), i = 1,··· ,n    (20) PEi = sigmoid( 1 1 ) =  −1 VEi  VEi  1+e    122    TDi = c VDi ×5002.   

<!-- b000361 | heading | pages [13] -->
3.2.4 Model Solution

<!-- b000362 | prose | pages [13] -->
微信号：MATHmodels The model (20) is a simulation framework based on the cellular automata. Thus, the solution can be obtained by stimulating the decomposition process via time iteration. The algorithm of the simulation process is described in Table 4. Note that during the simulation, we consider the falling leaves which provide uninfected cells (We change the cells that are fully decomposed into uninfected cells, i.e., G(p,q) = 1 to simulate the falling leaves). In this section, we select 3 types of fungi to conduct the experiments, i.e., Trichoderma, Penicillium, and Aspergillus (see details in Table 2). Also, we choose the environment in tropical rain forest for question 1, 2, and 3 (The details of different areas can be seen in Table 5). The simulation results are shown in Fig. 3.

<!-- b000363 | prose | pages [13] -->
From the left ﬁgure of Fig. 3, we can see that the wood ﬁber is infected and decomposed by different fungi. This kind of infection and decomposition happen all over woody ﬁber, i.e., fungi can use all the nutrients in woody ﬁber when they grow without restriction. From the middle ﬁgure of Fig. 3, we can see that in the initial stage, which is about 5 −10 days, fungi infect the woody ﬁber at an approximately exponential rate. After 10 days, however, the number of fungi began to decline. This is because the nutrient content of wood (that is, the number of uninfected wood in the cell map) is decreasing, while the decomposed wood is increasing. In addition, the existence of several fungi led to the rapid consumption of nutrients. Therefore, the growth environment of fungi became worse, and the number of fungi began to decrease due to the lack of nutrients. After about 40 days, the number of fungi tends to be more stable around 6×104. The decomposition rate after 122 days is 0.68.

<!-- b000364 | prose | pages [13] -->
From the right ﬁgure of Fig. 3, the change rate of the number of fungi is very high at ﬁrst and then tends to be stable. This is consistent with the results in most laboratories [26, 10, 16]. Because in the beginning, the nutrients are sufﬁcient and the growth rate is high. After that, the nutrients decreased and most of the wood was decomposed, and at the same time there are fallen leaves that provide extra nutrients (not enough for the fungi for further extension), so the rate of change of the number of fungi tends to be 0.

<!-- b000365 | heading | pages [13] -->
3.3 Cellular Automata Model Under Interactions Among Fungi

<!-- b000366 | prose | pages [13] -->
In this section, we address the second problem. In order to describe the interaction among different species of fungi, we mainly consider the changes of the extension rate, where the interaction among organisms mainly comes from the perspective of growth [25]. Speciﬁcally,

<!-- b000367 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000368 | prose | pages [13, 14] -->
we should consider whether there are mutually beneﬁcial and mutually exclusive effects among关注数学模型 微信公众号：数学模型

<!-- b000369 | furniture | pages [13] -->
2

<!-- b000370 | furniture | pages [13] -->
MATHmodels

<!-- b000371 | furniture | pages [13] -->
获取更多资讯

<!-- b000372 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000373 | furniture | pages [14] -->
Team # 2122025

<!-- b000374 | furniture | pages [14] -->
Page 13 of 24

<!-- b000376 | caption | pages [14] -->
Figure 3: The simulation results of question 1. Left: The illustration of woody ﬁber infected by different

<!-- b000377 | prose | pages [14] -->
species of fungi and decomposed by the fungi. Middle: The number of different fungi Ni with respect to the time. Right: The difference of the number of different fungi dNi dt with respect to the time.

<!-- b000378 | caption | pages [14] -->
Table 4: The algorithm corresponding to model (20).

<!-- b000379 | heading | pages [14] -->
Algorithm 1: The fungal extension and decomposition simulation process

<!-- b000380 | prose | pages [14] -->
微信号：MATHmodels G ∈N500×500, tmax, {Tmaxi}, {VEmaxi}, {Mi} 1: input:

<!-- b000381 | prose | pages [14] -->
2: Initialize Fi ∈N2,i = 1,··· ,n;

<!-- b000382 | prose | pages [14] -->
3: for t = 1 : tmax for (p,q) = (1,1) : (500,500) 4:

<!-- b000383 | prose | pages [14] -->
Find adjacent points {(p j,q j)}; 5:

<!-- b000384 | prose | pages [14] -->
if G(pj,qj)̸ = 1 6:

<!-- b000385 | prose | pages [14] -->
Compute PEi via (15); 7:

<!-- b000386 | prose | pages [14] -->
Compute TDi via (19); 7:

<!-- b000387 | prose | pages [14] -->
Update Fi via (16) and (17); 7:

<!-- b000388 | prose | pages [14] -->
G(p j,qj) = i+1; 7:

<!-- b000389 | prose | pages [14] -->
end if 6:

<!-- b000390 | prose | pages [14] -->
end for 6:

<!-- b000391 | prose | pages [14] -->
i |; Compute dNi Nt i = |Ft 6: dt via (18);

<!-- b000392 | prose | pages [14] -->
8: end for {Ni},{dNi dt } 9: output:

<!-- b000393 | prose | pages [14] -->
fungi. This effect should be quantiﬁed as the effect on extension rate. Then, cellular automata was used to re simulate the activity of fungi under intrinsic interactions.

<!-- b000394 | heading | pages [14] -->
3.3.1 Model Establishment

<!-- b000395 | prose | pages [14] -->
When modeling the relationship among fungi of different species, we should have consid- ered two aspects: mutual beneﬁt and mutual exclusion. However, as far as we konw, the mutual beneﬁt exists only among fungi and other organisms [27, 28]. Therefore, when we consider the relationship among fungi, we mainly consider the competitive relationship. That is to say, the extension rate VE would decrease under interactions of different fungi. Following our previous work (Deﬁnition 1), the extension probability would change. We induce the following deﬁnition of the extension probability under fungal interactions.

<!-- b000396 | prose | pages [14] -->
Deﬁnition 3 (Competitive-extension probability) Given the fungi cell Fi with extension rate VEi and the competitive fungi {Fj} with quantity {Nj}, the competitive-extension probability of Fi

<!-- b000397 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000398 | prose | pages [14, 15] -->
关注数学模型 is deﬁned as 1 1 PCi = sigmoid( ) = . (21) 1 VEi ×(1−∑j |Nj| − 5002 ) VEi×(1−∑j |Nj| 5002 ) 1+e 微信公众号：数学模型 Evidently, PCi is lower than PEi due to the percentage factor (1 −∑j |Nj| 5002 ). This factor con- siders that the extent of the impact of the competing fungi on the fungi Fi is related to the total number ∑j |Nj|. When the number of the competing fungi is large, the impact is considerable. This is consistent with the analysis in [27]. Thus, the validity of Deﬁnition 3 is justiﬁed.

<!-- b000399 | furniture | pages [14] -->
2

<!-- b000400 | furniture | pages [14] -->
MATHmodels

<!-- b000401 | furniture | pages [14] -->
获取更多资讯

<!-- b000402 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000403 | furniture | pages [15] -->
Team # 2122025

<!-- b000404 | furniture | pages [15] -->
Page 14 of 24

<!-- b000406 | prose | pages [15] -->
Based on the above analysis, the cellular automata model with fungi interactions can be formulated by re-written model (20) as

<!-- b000407 | prose | pages [15] -->
 Ft+1 = (Ft i ∪{(p,q)})\{(pt D,qt D)}, ξ ≤PCi i    Ft+1 = Ft i \{(pt D,qt  D)}, ξ > PCi  i     ξ ∼U(0,1), i = 1,··· ,n     微信号：MATHmodels 1 1 (22) PCi = sigmoid( ) = 1 VEi ×(1−∑j |Nj| −  5002 ) VEi×(1−∑j |Nj|   5002 )  1+e    122    TDi = c VDi ×5002.   

<!-- b000408 | heading | pages [15] -->
3.3.2 Model Solution

<!-- b000409 | prose | pages [15] -->
The algorithm to solve model (22) is similar to that of model (20). Thus, the algorithm can be also described as Table 4. The only difference is the computation of the probability. In Table 4, the probability is computed via (15). Here, the probability is computed via (21).

<!-- b000410 | prose | pages [15] -->
The results are shown in Fig. 4. According to the left ﬁgure of Fig. 4, the infection and decomposition of wood are overall and random. Among them, the number of decomposed wood is signiﬁcantly reduced compared with the result of the ﬁrst question. Speciﬁcally, the number of fungi after stabilization is around 4.5 × 104, which is concretely 33.65% lower than that of the situation without fungal competition. According to the middle ﬁgure of Fig. 4, similar to the result of the ﬁrst question, the number of fungi ﬁrst increased and then decreased. According to the right ﬁgure of Fig. 4, the rate of change in the number of fungi is very large at ﬁrst and then tends to 0. The decomposition rate after 122 days is 0.39, which is 42.69% lower than that of the situation without fungal competition.

<!-- b000411 | prose | pages [15] -->
Unlike the ﬁrst question, we consider the competition among different types of fungi in this section. Under such consideration, our experimental results are quite different from the ﬁrst question. Speciﬁcally, according to the middle ﬁgure of Fig. 4, although the overall growth trend of fungi increased and then decreased, the overall number of fungi decreased signiﬁcantly compared with the result of the ﬁrst question. This is because we consider the competition among fungi. Based on Deﬁnition 3, fungi are less likely to infect wood. Therefore, the general number of fungi has decreased signiﬁcantly.

<!-- b000412 | heading | pages [15] -->
3.4 Analysis and Experimental Results

<!-- b000413 | prose | pages [15] -->
We answer the third and fourth questions in this section. First, we conduct an overall anal-

<!-- b000414 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000415 | prose | pages [15, 16] -->
ysis of the previous models. Then, we analyze the competitive relationship among different关注数学模型 微信公众号：数学模型

<!-- b000416 | furniture | pages [15] -->
2

<!-- b000417 | furniture | pages [15] -->
MATHmodels

<!-- b000418 | furniture | pages [15] -->
获取更多资讯

<!-- b000419 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000420 | furniture | pages [16] -->
Team # 2122025

<!-- b000421 | furniture | pages [16] -->
Page 15 of 24

<!-- b000423 | caption | pages [16] -->
Figure 4: The simulation results of question 2 (Fungal decomposition and growth simulation under

<!-- b000424 | prose | pages [16] -->
interactions of different species of fungi). Left: The illustration of woody ﬁber infected by different species of fungi and decomposed by the fungi. Middle: The number of different fungi Ni with respect to the time. Right: The difference of the number of different fungi dNi dt with respect to the time.

<!-- b000425 | prose | pages [16] -->
species. Then, we analyze the sensitivity of environmental changes (mainly the changes of 微信号：MATHmodels temperature and humidity). Finally, we simulate the extension and decomposition of differ- ent fungal species in different environments and analyze the advantages and disadvantages of different fungal species in different environments.

<!-- b000426 | heading | pages [16] -->
3.4.1 Overall Analysis

<!-- b000427 | prose | pages [16] -->
The models we established are intrinsically linked. This connection is quantiﬁed by various parameters. The speciﬁc connection can be described as Fig. 5. Started with the fungal type, the lower limit of the humidity and the maximum extension rate of this type of fungi are determined. Then, the extension rate and the moisture trade-off are computed. Using model (7) and (8), the decomposition rate is determined. Next, we induce three deﬁnitions which respectively consider the extension probability, the decomposition time, and the competitive extension probability. Finally, the cellular automata models (20) and (22) are established according to these factors.

<!-- b000428 | prose | pages [16] -->
Based on the above analysis, our model has good ﬂexibility and a robust relationship struc- ture. In addition, our consideration is based on the actual situation of fungal decomposition, so it has good credibility. We formulate the decomposition rate according to the moisture trade-off and the extension rate, which is inspired by [5]. Our experimental results demonstrate that our motivations are correct, where the growth process of fungi and the decomposition process of woody ﬁbers depend on the types and parameters of fungi, as well as the changes of environ- ment (to be discussed in the next part).

<!-- b000429 | heading | pages [16] -->
3.4.2 Interactions Among Different fungi

<!-- b000430 | prose | pages [16] -->
In model (22), we summarize the internal interaction among different types of fungi as the competition among different types of fungi. We put forward a deﬁnition (Deﬁnition 3). This deﬁnition considers the effect of another species on a type of fungi mainly based on the exten- sion rate. A percentage factor is used to reduce the original extension rate. This competitive relationship is relative, so it will affect the whole process of decomposition and growth.

<!-- b000431 | prose | pages [16] -->
From the perspective of the short run, according to Fig 3 and Fig. 4, the additional consider- ation of fungal competition does not have much impact. This is because in the initial stage, the remaining amount of wood, that is, nutrients, is sufﬁcient. Even if the growth rate of fungi is limited, their growth process takes place in a similar exponential form. Therefore, in the short term, the impact of competition is not obvious.

<!-- b000432 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000433 | prose | pages [16, 17] -->
关注数学模型 Starts here Eq. (21) Comp. exten. proba. Model (22) Fungal type Max. extension rate Eq. (15) Model (20) Exten. probability 微信公众号：数学模型 Temperature Eq. (5)

<!-- b000434 | furniture | pages [16] -->
2

<!-- b000435 | furniture | pages [16] -->
MATHmodels

<!-- b000436 | furniture | pages [16] -->
获取更多资讯

<!-- b000437 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000438 | furniture | pages [17] -->
Team # 2122025

<!-- b000439 | furniture | pages [17] -->
Page 16 of 24

<!-- b000441 | heading | pages [17] -->
Extension rate

<!-- b000442 | prose | pages [17] -->
Humidity Eq. (19) Model (7) Decomposition rate Decomposition time

<!-- b000443 | prose | pages [17] -->
Eq. (6) Humidity limit Moisture trade-off

<!-- b000444 | prose | pages [17] -->
Determine the parameters

<!-- b000445 | prose | pages [17] -->
Data in [18] Model (8)

<!-- b000446 | caption | pages [17] -->
Figure 5: The overall analysis of the relationship of different parameters and models of this paper.

<!-- b000447 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000448 | caption | pages [17] -->
Figure 6: The sensitivity analysis of different temperature and humidity.

<!-- b000449 | prose | pages [17] -->
However, from the perspective of the long run, the impact of considering the fungal compe- tition is huge. From the middle ﬁgures of Fig. 3 and 4, we can ﬁnd that when we do not consider the interaction, every species of fungi grows at an independent pace, where the intensity of the number Ni is much higher than that of Fig. 4. After considering the interaction, the general number Ni decreased a lot. This is because when the woody ﬁber being decomposed, the nutri- ents are becoming more and more limited. In such conditions, competition among fungi makes their growth extremely slow. Thus, their quantities Ni are very low.

<!-- b000450 | heading | pages [17] -->
3.4.3 Sensitive Analysis of Environment

<!-- b000451 | prose | pages [17] -->
In order to prove that our model has a good internal relationship, especially can make a good response to environmental changes, we carry out the sensitivity analysis of environmental

<!-- b000452 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000453 | prose | pages [17, 18] -->
changes (temperature and humidity). Speciﬁcally, we use three fungal types, i.e., Trichoderma,关注数学模型 Aspergillus Penicillium Trichoderma Arid area Arid area Arid area Arid area Arid area Arid area Semi arid area Semi arid area Semi arid area Semi arid area Semi arid area Semi arid area Temperate area Temperate area Temperate area Temperate area Temperate area Temperate area Arboreal area Arboreal area Arboreal area Arboreal area Arboreal area Arboreal area Tropical rain forest Tropical rain forest Tropical rain forest Tropical rain forest Tropical rain forest Tropical rain forest

<!-- b000454 | furniture | pages [17] -->
2

<!-- b000455 | furniture | pages [17] -->
MATHmodels

<!-- b000456 | furniture | pages [17] -->
获取更多资讯

<!-- b000457 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000458 | furniture | pages [18] -->
Team # 2122025

<!-- b000459 | furniture | pages [18] -->
Page 17 of 24

<!-- b000461 | prose | pages [18] -->
微信公众号：数学模型 Day Day Day Rust fungi Fusarium Gibberella Arid area Arid area Arid area Arid area Arid area Arid area Semi arid area Semi arid area Semi arid area Semi arid area Semi arid area Semi arid area Temperate area Temperate area Temperate area Temperate area Temperate area Temperate area Arboreal area Arboreal area Arboreal area Arboreal area Arboreal area Arboreal area Tropical rain forest Tropical rain forest Tropical rain forest Tropical rain forest Tropical rain forest Tropical rain forest

<!-- b000462 | prose | pages [18] -->
微信号：MATHmodels Day Day Day

<!-- b000463 | caption | pages [18] -->
Figure 7: The number of fungi Ni with respect to the time under different environments of different types

<!-- b000464 | prose | pages [18] -->
of fungi.

<!-- b000465 | prose | pages [18] -->
Penicillium, Aspergillus to simulate the decomposition process under different environments with slightly different temperatures and humidities. The results of the sensitivity analysis are shown in Fig. 6.

<!-- b000466 | prose | pages [18] -->
In Fig. 6, we can observe that the proposed models are sensitive to considerable changes in the environments. Speciﬁcally, an 8% change of the temperature would lead to an impact on the ﬁnal determination of the dominant species. Meanwhile, there is an impact of the change of the humidity on the ﬁnal dominant species. The sensitivity of our models is mainly because of the connection of the environmental factors and the extension rate as well as the competitive interactions. Also, different species of fungi have different Tmax and Hl, which leads to the sensitiveness of the proposed model with different temperatures and humidity.

<!-- b000467 | prose | pages [18] -->
From our sensitivity test results, we can see that the temperature change near the optimal temperature will have a greater impact on the activity of fungi. If the local atmosphere changes abnormally, the temperature or humidity will change greatly and may deviate from the optimal temperature or humidity limit of fungi, so the growth of fungi and the decomposition efﬁciency of woody ﬁber will be reduced. Speciﬁcally, for the local tropical rain forest area, if the tem- perature decreases or increases in the future (deviates from the optimal temperature of fungi), the extension and decomposition rate of fungi will decrease. In terms of humidity, the activity of fungi will be greatly limited when the humidity drops and becomes relatively dry in autumn and winter.

<!-- b000468 | heading | pages [18] -->
3.4.4 Simulations Under Different Combinations and Regions

<!-- b000469 | prose | pages [18] -->
Next, we conduct more experiments to verify the effectiveness of our models. Speciﬁcally, we conduct the simulation on different conditions, i.e., the arid area, the semi-arid area, the tem- perate area, and the tropical rain forest area. Speciﬁc temperature and humidity data is shown in

<!-- b000470 | caption | pages [18] -->
Table 5 (refered from

<!-- b000471 | prose | pages [18] -->
https://gis.ncdc.noaa.gov/maps/ncei/summaries/daily). Meanwhile, we employ different species of fungi in these areas to see the corresponding results.

<!-- b000472 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000473 | prose | pages [18, 19] -->
First, we simulate each selected species of fungi (they have different model parameters) in关注数学模型 Arid area Semi arid area Temperate area

<!-- b000474 | furniture | pages [18] -->
2

<!-- b000475 | furniture | pages [18] -->
MATHmodels

<!-- b000476 | furniture | pages [18] -->
获取更多资讯

<!-- b000477 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000478 | furniture | pages [19] -->
Team # 2122025

<!-- b000479 | furniture | pages [19] -->
Page 18 of 24

<!-- b000481 | prose | pages [19] -->
微信公众号：数学模型 Day Day Day Tropical rain forest Arboreal area

<!-- b000482 | prose | pages [19] -->
微信号：MATHmodels Day Day

<!-- b000483 | caption | pages [19] -->
Figure 8: The number of fungi Ni with respect to the time under different environments with the com-

<!-- b000484 | prose | pages [19] -->
petitive combination of different fungi.

<!-- b000485 | caption | pages [19] -->
Table 5: The types of environments and the corresponding parameters (We use the temperature and

<!-- b000486 | prose | pages [19] -->
humidity data from a speciﬁc observation point whose longitude and latitude are displayed).

<!-- b000487 | prose | pages [19] -->
T H Areas longitude latitude 20.4◦C 87.7◦E 40.6◦N 0.16 Arid area 22.12◦C 118.8◦E 42.3◦N 0.39 Semi arid area 27.63◦C 102.2◦W 39.2◦N 0.56 Temperate area 26.07◦C 82.2◦W 29.2◦N 0.69 Arboreal area 28.72◦C 61.2◦W 5.8◦S 0.88 Tropical rain forest

<!-- b000488 | prose | pages [19] -->
ﬁve different environments. The results are shown in Fig. 7. We can see that the growth of each fungus in different environments is similar, but their number Ni is not consistent, which is due to their maximum extension rate VEmax is not the same. The tropical rain forest occupied the highest number of growth in all simulation results. This is because in the tropical rain forest, the humidity is very sufﬁcient, and the temperature is more appropriate. In such conditions, all types of fungi can favorably grow and decompose the woody ﬁber. However, some types of fungi are difﬁcult to grow in arid environments. Especially for Rust fungi, Gibberella, and Fusarium, the number decreased to 0 in an arid area, which reﬂected that these three kinds of fungi were not suitable for living in this environment.

<!-- b000489 | prose | pages [19, 20] -->
Then, we simulate the growing and decomposition process of fungal species combinations (under their competitive interactions) in different areas. The results are shown in Fig. 8. The simulation results show that in arid areas, the studied species are Trichoderma, Aspergillus, and Penicillium, in which the dominant species is Trichoderma and the inferior species is As- pergillus. In the semi-arid area, the studied species are Rust fungi, Aspergillus and Fusarium, in which the dominant species is Aspergillus and the inferior species is Rust. In the temperate zone, Fusarium, Aspergillus, and Gibberella are the studied species, in which Aspergillus is the dominant species and Gibberella is the inferior species. In arboreal areas, the studied species are Trichoderma, Hyphomycetes, and Gibberella, in which the dominant species is Trichoderma and the inferior species is Gibberella. In the tropical rain forest area, the studied species are Tri-关注数学模型 微信公众号：数学模型 Decomposition rate Proportion

<!-- b000490 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000491 | furniture | pages [19] -->
2

<!-- b000492 | furniture | pages [19] -->
MATHmodels

<!-- b000493 | furniture | pages [19] -->
获取更多资讯

<!-- b000494 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000495 | furniture | pages [20] -->
Team # 2122025

<!-- b000496 | furniture | pages [20] -->
Page 19 of 24

<!-- b000498 | prose | pages [20] -->
Day Number of tests

<!-- b000499 | caption | pages [20] -->
Figure 9: Left: The decomposition rate with respect to the time under different combinations of the

<!-- b000500 | prose | pages [20] -->
species of fungi. Right: The proportion between the decomposition rate of “All three” and the decompo- sition rate of a single species of fungi with respect to the number of tests.

<!-- b000501 | prose | pages [20] -->
微信号：MATHmodels choderma, Penicillium, and Aspergillus, in which the dominant species is Aspergillus and the inferior species is Penicillium. In these simulation results, the decomposition rate is different, e.g., the decomposition rate of fungi in the tropical rain forest area is 68.29% after 122 days. Here, we do not elaborate on all the decomposition rates due to the page limit.

<!-- b000502 | prose | pages [20] -->
It is notable that the growth process of different fungi combinations in the ﬁve types of environments is very different. This is due to two reasons. First, the temperature and humid- ity in different environments are very different, which changes the growth process of fungi. Secondly, different combinations of fungi have different optimal temperatures and moisture trade-off, which also change the growth process. Speciﬁcally, we can ﬁnd that in two areas, the Trichoderma obtains the highest number Ni. This is due to high VEmax value (VEmax = 8.23) of Trichoderma, and the value of the most suitable temperature Tmax (Tmax = 28◦C) is also around the most common temperature at earth. Thus, Trichoderma could gain superiority against other species of fungi under competitive interactions.

<!-- b000503 | heading | pages [20] -->
3.5 Inﬂuence of Species Diversity

<!-- b000504 | prose | pages [20] -->
This section responds to the ﬁfth question, i.e., we study the importance of biodiversity on the decomposition of the woody ﬁbers. Speciﬁcally, we simulate the decomposition process with three single types of fungi and their combinations, respectively. The results are shown in

<!-- b000505 | caption | pages [20] -->
Fig. 9. Here, we plot the decomposition rate with respect to the time in the left ﬁgure. Then, we

<!-- b000506 | prose | pages [20] -->
re-conduct the experiments 1000 times and compute the proportion between the decomposition rate of “All three” and the decomposition rate of a single species, where the proportion with respect to the number of the experiment is shown in the right ﬁgure of Fig. 9.

<!-- b000507 | prose | pages [20] -->
From the left ﬁgure of Fig. 9, we can clearly observe that when the three fungal species are combined (that is, the biodiversity increases), the decomposition rate is much higher than that of a single species. Also in the right ﬁgure of Fig. 9, we can ﬁnd that at the most time the decomposition rate of “All three” combination is considerably larger than that of a single species of fungi. Speciﬁcally, the average proportion is 2.89. Therefore, in this environment, the impact of species diversity is huge. This is basically because multiple species not only bring the high quantity of the fungi but also increase the robustness of multiple species, i.e., if the environment (temperature and humidity) is not adapted to one of the fungal species, there may be another fungal species adapted to this environment. Therefore, the decomposition rate under biodiversity can be guaranteed. That is to say, biodiversity is very important to the effectiveness

<!-- b000508 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000509 | prose | pages [20] -->
关注数学模型 of fungal decomposition in the ecosystem.

<!-- b000510 | furniture | pages [20] -->
2

<!-- b000511 | furniture | pages [20] -->
MATHmodels

<!-- b000512 | furniture | pages [20] -->
获取更多资讯

<!-- b000513 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000514 | furniture | pages [21] -->
Team # 2122025

<!-- b000515 | furniture | pages [21] -->
Page 20 of 24

<!-- b000516 | heading | pages [21] -->
4 Strengths and Weaknesses

<!-- b000517 | prose | pages [21] -->
In this paper, we propose to model the relation of the extension rate, moisture trade-off, and the decomposition rate via SGD. The ﬁnal relationship is described as (14). Then, we employ 微信公众号：数学模型 the cellular automata to simulate the decomposition process. Three deﬁnitions are subsequently induced to guide the simulation process. Extensive experiments on multiple types of fungi and different environments forcefully demonstrate the effectiveness and robustness of the proposed models. The strengths of the proposed model are as follows.

<!-- b000518 | heading | pages [21] -->
4.1 Strengths

<!-- b000519 | prose | pages [21] -->
• Robust relation description Our relational model (7) is nonlinear and can describe re- lationships among extension rate, moisture trade-off, and decomposition rate robustly.

<!-- b000520 | prose | pages [21] -->
Meanwhile, the parameters of this model are adaptively ﬁtted according to the literature [5] data, which is accurate.

<!-- b000521 | prose | pages [21] -->
• Efﬁcient algorithm We employ the SGD algorithm to tackle the non-convex and non- 微信号：MATHmodels linear optimization problem (8). According to the good generalization property of SGD [24], the iterative process can commendably converge to some critical points.

<!-- b000522 | prose | pages [21] -->
• Accurate simulation We employ the discrete cellular automata to adaptively and pre- cisely simulate the decomposition and extension process of the fungi, with a concise and efﬁcient implementation. The cellular automata model (20) can be addressed via simple time iteration, which is computationally efﬁcient and has high consistency with the real situation.

<!-- b000523 | prose | pages [21] -->
• Intrinsic connections Three deﬁnitions (Deﬁnition 1, 2, and 3) are introduced to ro- bustly characterize the extension process in the cellular automata, the decomposition pro- cess of the fungi, and the extension rate under interactions of different fungi, respectively.

<!-- b000524 | prose | pages [21] -->
Thus, the inﬂuence of all factors is connected and reﬂected simultaneously in cellular automata, which leads to precise modeling of the activity of fungi.

<!-- b000525 | prose | pages [21] -->
• High ﬂexibility and portability Our model has multiple parameters, e.g., VEmax,M,T, et al. These parameters represent the essential characteristics of fungi and environmental parameters. Therefore, our model is considerably ﬂexible and sensitive to different fungal types and environments (basically temperature and humidity). Hence, it is easy to apply our model under different conditions.

<!-- b000526 | prose | pages [21] -->
However, there are weaknesses of the proposed models:

<!-- b000527 | heading | pages [21] -->
4.2 Weaknesses

<!-- b000528 | prose | pages [21] -->
• Difﬁculty in parameter adjustment Although the multiple parameters in our model ensure the ﬂexibility of the model, the adjustment and setting of parameters require addi- tional data collection, which would be time-consuming and difﬁcult if the studied objects have no open access data.

<!-- b000529 | prose | pages [21] -->
• Lack of theoretical explanation Our model gives the empirical relationship among var- ious factors and stimulates the growth and decomposition of fungi in different situations.

<!-- b000530 | prose | pages [21] -->
However, the theoretical biological mechanism of these phenomena has not been identi- ﬁed and needs further study.

<!-- b000531 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000532 | prose | pages [21] -->
关注数学模型

<!-- b000533 | furniture | pages [21] -->
2

<!-- b000534 | furniture | pages [21] -->
MATHmodels

<!-- b000535 | furniture | pages [21] -->
获取更多资讯

<!-- b000536 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000537 | furniture | pages [22] -->
Team # 2122025

<!-- b000538 | furniture | pages [22] -->
Page 21 of 24

<!-- b000539 | heading | pages [22] -->
5 Article

<!-- b000540 | prose | pages [22] -->
Recent Advances in the Role of Fungi in Ecosystems 微信公众号：数学模型 Any ecosystem has the basic functions of energy ﬂow, material circulation, and information transmission.

<!-- b000541 | prose | pages [22] -->
The material cycle in the ecosystem includes two relative processes: biosynthesis and biodegra- dation. The former is the organic process of inorganic matter, which is mainly completed by green plants and some inorganic nutrient microorganisms. The latter is the inorganic process of organic matter, which is mainly completed by forest microorganisms, that is, the decomposition process of forest litter. Litter decomposition generally includes three stages: leaching stage, crushing stage, and organic matter catabolism stage.

<!-- b000542 | prose | pages [22] -->
There are two groups of soil organisms related to material decomposition, namely soil an- imals and soil microorganisms. They are not only different in morphology and structure, but also play different roles in the process of material decomposition. From the process of litter 微信号：MATHmodels decomposition, the decomposition of animals is mainly mechanical fragmentation, while mi- croorganisms participate in the biochemical process of litter decomposition.

<!-- b000543 | prose | pages [22] -->
Soil microorganism is the general term of microorganisms living in the soil. As decom- posers, they are an indispensable part of the forest ecosystem. The diversity of nutrient sub- strates in the litter layer determines the diversity of decomposers. Bacteria, actinomycetes, fungi (including yeasts), algae, and protozoa are all involved in the decomposition of organic matter. Fungi, especially ﬁlamentous fungi, are thought to play a major role in litter decompo- sition.

<!-- b000544 | prose | pages [22] -->
The decomposition of litter by fungi is an enzymatic process based on the level of decom- poser cells. The hyphae of fungi can penetrate into the plant debris and secrete extracellular enzymes to degrade the recalcitrant substances (such as lignin) contained in the litter, so as to soften the plant debris and change the structure and chemical composition of the litter. Based on this, fungi play the following important roles in the ecosystem.

<!-- b000545 | prose | pages [22] -->
• Participate in the carbon cycle and maintain ecosystem balance. The CO2 produced by microbial respiration accounts for about 80% of the total CO2 required by plant photo- synthesis, and fungi account for about 13%. Therefore, fungi are closely related to main- taining the balance of forest ecosystems and play a crucial role in the global terrestrial carbon cycle.

<!-- b000546 | prose | pages [22] -->
• Participate in soil nutrient cycle and enhance forest productivity. Nitrogen and phospho- rus are essential nutrients for life activities. Fungi participate in the decomposition of 4 and NO− organic nitrogen in litter and transform it into mineral ions NH+ 3 , which can be absorbed and utilized by forest plants. Phosphorus is temporarily enriched and then released by microorganisms, which increases the availability of phosphorus and improves the utilization efﬁciency of phosphorus by forest plants.

<!-- b000547 | prose | pages [22] -->
• Participate in phytoremediation to improve plant stress resistance. In soils contaminated by metals or organic compounds, mycorrhiza may reduce the bioabsorbable concentra- tion of pollutants in the soil by increasing the degradation of organic pollutants in the mycorrhizal zone, thus contributing to plant resistance.

<!-- b000548 | prose | pages [22] -->
• Decomposition of plant litter, promote the formation of humic acid. Soil fungi can pro-

<!-- b000549 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000550 | prose | pages [22, 23] -->
mote the formation of humic acid from the organic matter around roots. Humic acid salt关注数学模型 contains a large number of functional groups, which can not only improve the soil but also stimulate crop growth. The increase of humic acid in the soil directly promotes the growth and development of plants.

<!-- b000551 | furniture | pages [22] -->
2

<!-- b000552 | furniture | pages [22] -->
MATHmodels

<!-- b000553 | furniture | pages [22] -->
获取更多资讯

<!-- b000554 | furniture | pages [23] -->
微信公众号：数学模型

<!-- b000555 | furniture | pages [23] -->
Team # 2122025

<!-- b000556 | furniture | pages [23] -->
Page 22 of 24

<!-- b000558 | prose | pages [23] -->
微信公众号：数学模型

<!-- b000559 | prose | pages [23] -->
• Provide a barrier to reduce pathogen invasion. In order to protect the root growth of plants from pathogens and insects, soil microorganisms such as fungi in the rhizosphere will parasitize and colonize around the roots of soil plants, forming a physical protective layer.

<!-- b000560 | prose | pages [23] -->
However, the efﬁciency of fungal growth and decomposition is inﬂuenced by the environ- ment and the interaction among different species of fungi. In our study, we come to the follow- ing conclusion.

<!-- b000561 | prose | pages [23] -->
• The inﬂuence of fungal species interaction

<!-- b000562 | prose | pages [23] -->
From the perspective of the short run, there was no obvious effect on the interaction between 微信号：MATHmodels different kinds of fungi. This is because in the initial stage, the remaining amount of wood, that is, nutrients, is sufﬁcient. Even if the growth rate of fungi is limited, their growth process takes place in a similar exponential form. Therefore, in the short term, the impact of competition is not obvious. However, from the perspective of the long run, the impact of considering the fungal competition is huge. When we do not consider the interaction, every species of fungi grows at an independent pace, where the intensity of the number Ni is much higher. After considering the interaction, the general number Ni decreased a lot. This is because when the woody ﬁber being decomposed, the nutrients are becoming more and more limited. In such conditions, competition among fungi makes their growth extremely slow. Thus, their quantities Ni are very low.

<!-- b000563 | prose | pages [23] -->
• The inﬂuence of environment on fungi

<!-- b000564 | prose | pages [23] -->
From our sensitivity experimental results, the temperature change near the optimal temper- ature will have a greater impact on the fungal activity. If the local weather changes abnormally, the growth of fungi and the decomposition of woody ﬁber will have lower efﬁciency and more unpredictable changes. For humidity, if it is too dry, the activity of fungi would be greatly limited as well.

<!-- b000565 | prose | pages [23] -->
In a word, fungi, as decomposers, play an important role in the ecosystem. In abstract terms, the vital signiﬁcance of fungi decomposition is to release these chemical substances combined with organisms into nature again. There are limited chemical substances that can be used by living organisms. If these chemical substances are always bound to the dead organisms indeﬁnitely and cannot be utilized by living organisms, then the life of organisms will end ultimately.

<!-- b000566 | furniture | pages [23] -->
微信号：MATHmodels

<!-- b000567 | prose | pages [23] -->
关注数学模型

<!-- b000568 | furniture | pages [23] -->
2

<!-- b000569 | furniture | pages [23] -->
MATHmodels

<!-- b000570 | furniture | pages [23] -->
获取更多资讯

<!-- b000571 | furniture | pages [24] -->
微信公众号：数学模型

<!-- b000572 | furniture | pages [24] -->
Team # 2122025

<!-- b000573 | furniture | pages [24] -->
Page 23 of 24

<!-- b000574 | heading | pages [24] -->
References

<!-- b000575 | references | pages [24] -->
[1] Yan Haiyuan, Gu Xirong, and Shen Hong. Microbial decomposition of forest litter. Jour-

<!-- b000576 | references | pages [24] -->
微信公众号：数学模型

<!-- b000577 | references | pages [24] -->
nal of ecology, 029(009):1827–1835, 2010.

<!-- b000578 | references | pages [24] -->
[2] Wang xiang’e, Xue Li, and Xie Tengfang. Review on litter decomposition. Soil bulletin,

<!-- b000579 | references | pages [24] -->
(06):1473–1478, 2009.

<!-- b000580 | references | pages [24] -->
[3] Zhang Shuxian. Characteristics of fungi during decomposition of forest dead leaves. Jour-

<!-- b000581 | references | pages [24] -->
nal of ecology, (06):30–32, 1988.

<!-- b000582 | references | pages [24] -->
[4] S. D. Frey, J. Six, and E. T. Elliott. Reciprocal transfer of carbon and nitrogen by de-

<!-- b000583 | references | pages [24] -->
composer fungi at the soil-litter interface. Soil Biology & Biochemistry, 35(7):1001–1004,

<!-- b000584 | references | pages [24] -->
2003.

<!-- b000585 | references | pages [24] -->
[5] Nicky Lustenhouwer, Daniel S. Maynard, Mark A. Bradford, Daniel L. Lindner, Brad

<!-- b000586 | references | pages [24] -->
Oberle, Amy E. Zanne, and Thomas W. Crowther. A trait-based understanding of wood de-

<!-- b000587 | references | pages [24] -->
微信号：MATHmodels

<!-- b000588 | references | pages [24] -->
composition by fungi. Proceedings of the National Academy of Sciences, 117(21):11551–

<!-- b000589 | references | pages [24] -->
11558, 2020.

<!-- b000590 | references | pages [24] -->
[6] Chen m R. Diversity of endophytic fungi in Chinese ﬁr leaves and their effects on litter

<!-- b000591 | references | pages [24] -->
decomposition. PhD thesis, 2020.

<!-- b000592 | references | pages [24] -->
[7] Pei Bei and Gao Guorong. Research progress on effects of litter decomposition on forest

<!-- b000593 | references | pages [24] -->
soil carbon pool. Chinese agricultural bulletin, 34(26):64–70, 2018.

<!-- b000594 | references | pages [24] -->
[8] Yu Shuling. Research progress of saprophytic fungi in the process of organic matter de-

<!-- b000595 | references | pages [24] -->
composition. Journal of Hebei Normal University, 27(5):519–522, 7 2003.

<!-- b000596 | references | pages [24] -->
[9] S. Findlay, J. Tank, S. Dye, H. M. Valett, P. J. Mulholland, W. H. Mcdowell, S. L. Johnson,

<!-- b000597 | references | pages [24] -->
S. K. Hamilton, J. Edmonds, and W. K. Doddsw. B. Bowden. A cross-system comparison

<!-- b000598 | references | pages [24] -->
of bacterial and fungal biomass in detritus pools of headwater streams. Microbial Ecology,

<!-- b000599 | references | pages [24] -->
43(1):55–66, 2002.

<!-- b000600 | references | pages [24] -->
[10] Hua Chen, Mark E Harmon, Robert P Grifﬁths, and William Hicks. Effects of tempera-

<!-- b000601 | references | pages [24] -->
ture and moisture on carbon respired from decomposing woody roots. Forest Ecology &

<!-- b000602 | references | pages [24] -->
Management, 138(1-3):51–64, 2000.

<!-- b000603 | references | pages [24] -->
[11] Oliver Dilly and Jean Charles Munch. Microbial biomass content, basal respiration and

<!-- b000604 | references | pages [24] -->
enzyme activities during the course of decomposition of leaf litter in a black alder (alnus

<!-- b000605 | references | pages [24] -->
glutinosa (l.) gaertn.) forest. Soil Biology & Biochemistry, 28(8):1073–1081, 1996.

<!-- b000606 | references | pages [24] -->
[12] Anna K. Bandick and Richard P. Dick. Field management effects on soil enzyme activities.

<!-- b000607 | references | pages [24] -->
Soil Biology & Biochemistry, 31(11):1471–1479, 1999.

<!-- b000608 | references | pages [24] -->
[13] Ruiqing Zhang, Zhenjun Sun, Chong Wang, and Tangyu Yuan. Ecological process of leaf

<!-- b000609 | references | pages [24] -->
litter decomposition in tropical rainforest in xishuangbanna, southwest china. iii. enzyme

<!-- b000610 | references | pages [24] -->
dynamics. Frontiers of Forestry in China, 4:28–37, 03 2009.

<!-- b000611 | references | pages [24] -->
[14] Peter M. Vitousek, Douglas R. Turner, William J. Parton, and Robert L. Sanford. Litter

<!-- b000612 | references | pages [24] -->
decomposition on the mauna loa environmental matrix, hawai’i: Patterns, mechanisms,

<!-- b000613 | references | pages [24] -->
and models. Ecology, 75(2), 1994.

<!-- b000614 | furniture | pages [24] -->
微信号：MATHmodels

<!-- b000615 | references | pages [24] -->
关注数学模型

<!-- b000616 | furniture | pages [24] -->
2

<!-- b000617 | furniture | pages [24] -->
MATHmodels

<!-- b000618 | furniture | pages [24] -->
获取更多资讯

<!-- b000619 | furniture | pages [25] -->
微信公众号：数学模型

<!-- b000620 | furniture | pages [25] -->
Team # 2122025

<!-- b000621 | furniture | pages [25] -->
Page 24 of 24

<!-- b000622 | references | pages [25] -->
[15] Bai Yongfei, Li Linghao, Li Xin, and Wang Qibing. Effects of simulated climate change

<!-- b000623 | references | pages [25] -->
on decomposition of mixed litter in three grassland plant communities. Journal of plant

<!-- b000624 | references | pages [25] -->
ecology, 24(6):674–679, 2000.

<!-- b000625 | references | pages [25] -->
微信公众号：数学模型

<!-- b000626 | references | pages [25] -->
[16] T. R. Moore, J. A. Trofymow, B. Taylor, C. Prescott, C. Camiré, L. Duschene, J. Fyles,

<!-- b000627 | references | pages [25] -->
L. Kozak, M. Kranabetter, and I. and Morrison. Litter decomposition rates in canadian

<!-- b000628 | references | pages [25] -->
forests. Global Change Biology, 5(1):75–82, 2010.

<!-- b000629 | references | pages [25] -->
[17] Klaus Lorenz, Caroline M Preston, Stephan Raspe, Ian K Morrison, and Karl Heinz Feger.

<!-- b000630 | references | pages [25] -->
Litter decomposition and humus characteristics in canadian and german spruce ecosys-

<!-- b000631 | references | pages [25] -->
tems: information from tannin analysis and 13c cpmas nmr. Soil Biology and Biochem-

<!-- b000632 | references | pages [25] -->
istry, 32(6), 2000.

<!-- b000633 | references | pages [25] -->
[18] Gladys Loranger, Jean-Franois Ponge, Daniel Imbert, and Patrick Lavelle. Leaf decompo-

<!-- b000634 | references | pages [25] -->
sition in two semi-evergreen tropical forests: inﬂuence of litter quality. Biology & Fertility

<!-- b000635 | references | pages [25] -->
of Soils, 35(4):247–252, 2002.

<!-- b000636 | references | pages [25] -->
[19] Li Xiuyun and Li Runxiang. Factors affecting forest litter decomposition. Friends of

<!-- b000637 | references | pages [25] -->
微信号：MATHmodels

<!-- b000638 | references | pages [25] -->
farmers’ wealth, (20), 6 2012.

<!-- b000639 | references | pages [25] -->
[20] Lindgren D. The temperature inﬂuence on the spontaneous mutation rate. i. literature

<!-- b000640 | references | pages [25] -->
review. Hereditas, 70(27):165–78, 1972.

<!-- b000641 | references | pages [25] -->
[21] M.-N. Leclercq-Perlat, M. Sicard, I.C. Trelea, D. Picque, and G. Corrieu.

<!-- b000642 | references | pages [25] -->
Tempera-

<!-- b000643 | references | pages [25] -->
ture and relative humidity inﬂuence the microbial and physicochemical characteristics of

<!-- b000644 | references | pages [25] -->
camembert-type cheese ripening. Journal of Dairy Science, 95(8):4666–4682, 2012.

<!-- b000645 | references | pages [25] -->
[22] Hans Bisswanger. pH and Temperature Dependence of Enzymes, chapter 6, pages 145–

<!-- b000646 | references | pages [25] -->
152. John Wiley & Sons, Ltd, 2017.

<!-- b000647 | references | pages [25] -->
[23] F. Li, D. Fu, R. Zhang, H. Ma, and Q. Lu. Correlation simulation study of 71◦C method

<!-- b000648 | references | pages [25] -->
formula and arrhenius formula. In 2020 Asia-Paciﬁc Conference on Image Processing,

<!-- b000649 | references | pages [25] -->
Electronics and Computers (IPEC), pages 330–333, 2020.

<!-- b000650 | references | pages [25] -->
[24] J. Koneˇcný, J. Liu, P. Richtárik, and M. Takáˇc. Mini-batch semi-stochastic gradient de-

<!-- b000651 | references | pages [25] -->
IEEE Journal of Selected Topics in Signal Processing,

<!-- b000652 | references | pages [25] -->
scent in the proximal setting.

<!-- b000653 | references | pages [25] -->
10(2):242–255, 2016.

<!-- b000654 | references | pages [25] -->
[25] Colin P.D. Birch. A new generalized logistic sigmoid growth equation compared with the

<!-- b000655 | references | pages [25] -->
richards growth equation. Annals of Botany, 83(6):713–723, 1999.

<!-- b000656 | references | pages [25] -->
[26] Fang Miao, Minxia Liang, Xubing Liu, Wenbin Li, Erhan Huang, and Shixiao Yu. Abun-

<!-- b000657 | references | pages [25] -->
dance of saprotrophic fungi determines decomposition rates of leaf litter from arbuscular

<!-- b000658 | references | pages [25] -->
mycorrhizal and ectomycorrhizal trees in a subtropical forest. Soil Biology and Biochem-

<!-- b000659 | references | pages [25] -->
istry, 149:107966, 08 2020.

<!-- b000660 | references | pages [25] -->
[27] A. Pedro Goncalves, Jens Heller, Adriana M. Rico-Ramírez, Asen Daskalov, Gabriel

<!-- b000661 | references | pages [25] -->
Rosenﬁeld, and N. Louise Glass. Conﬂict, competition, and cooperation regulate social

<!-- b000662 | references | pages [25] -->
interactions in ﬁlamentous fungi. Annual Review of Microbiology, 74(1):693–712, 2020.

<!-- b000663 | references | pages [25] -->
[28] Aurélie Deveau, Gregory Bonito, Jessie Uehling, Mathieu Paoletti, Matthias Becker,

<!-- b000664 | references | pages [25] -->
Saskia Bindschedler, Stéphane Hacquard, Vincent Hervé, Jessy Labbé, Olga A Lastovet-

<!-- b000665 | references | pages [25] -->
sky, Sophie Mieszkin, Larry J Millet, Balázs Vajna, Pilar Junier, Paola Bonfante, Basti-

<!-- b000666 | references | pages [25] -->
aan P Krom, Stefan Olsson, Jan Dirk van Elsas, and Lukas Y Wick. Bacterial–fungal inter-

<!-- b000667 | references | pages [25] -->
actions: ecology, mechanisms and challenges. FEMS Microbiology Reviews, 42(3):335–

<!-- b000668 | furniture | pages [25] -->
微信号：MATHmodels

<!-- b000669 | references | pages [25] -->
关注数学模型

<!-- b000670 | references | pages [25] -->
352, 02 2018.

<!-- b000671 | furniture | pages [25] -->
2

<!-- b000672 | furniture | pages [25] -->
MATHmodels

<!-- b000673 | furniture | pages [25] -->
获取更多资讯
