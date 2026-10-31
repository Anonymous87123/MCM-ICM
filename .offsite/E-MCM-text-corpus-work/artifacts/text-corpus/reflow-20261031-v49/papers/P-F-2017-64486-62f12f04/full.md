# P-F-2017-64486-62f12f04

Status: machine-draft; not source-verified.


<!-- b000001 | title | pages [1] -->
Society Planning: Model, Simulation And Visualization

<!-- b000002 | heading | pages [1] -->
Summary

<!-- b000003 | prose | pages [1] -->
This paper presents a model to maximize both the economic output and job satisfaction for the workforce with sustainability in the scope. We build a self-adaptive system and deﬁne its dynamics. We run simula- tions of the system with real-world census data(PUMS 2015[1]) to ﬁnd out the optimal feasible solution. Based on the solution, we propose strategies to improve the living conditions of human immigrants on Mars. Our model has capabilities to deal with issues of population scalability, social development modality and evolution dynamics.

<!-- b000004 | prose | pages [1] -->
To address the problem of creating an optimal economic-workforce-education system, we decompose it into six sub-problems.

<!-- b000005 | prose | pages [1] -->
First, we constructed a parameter frame that integrates variables related to three aspects: income, edu- cation and social equality. We include basic parameters that exist in the census database, from which we derive metrics that reveal the characteristics of the society. Through an Analytical Hierarchy Process, we identify the critical parameters, among which the Happiness Index is an important comprehensive evaluation of citizens well-being.

<!-- b000006 | prose | pages [1] -->
Second, we formulate criteria to select 10000 immigrants for Population Zero. In comparison to the selected group, we generate a random sample by extracting data from PUMS 2015 database of 1,618,489 U.S. citizens. We study the demographics of both the selected group and the random sample. The selected group shows an obvious advantage in building a successful society.

<!-- b000007 | prose | pages [1] -->
Third, we construct a model to simulate the dynamic evolution of Population Zero. Consisting of vari- ous systems such as job, marriage, child generation, education, salary, salvation and migration system, this model evolves like our real world. We discuss one sample result in details using demographics, economics and Happiness Index.

<!-- b000008 | prose | pages [1] -->
In addition, we use this model to ﬁnd the equilibrium point between two contradictory goals of faster economic development and better social welfare. By implementing a Principle Component Analysis on the demographic data, we deﬁne the key elements of a successful society as high average family income, high minimum wage and low standard deviation of income. We solve the three-objective optimization problem by Elite Genetic Algorithm. We ﬁnd that the optimal minimum wage is $33526 per year, and the optimal parental leave pay is $50200 per year.

<!-- b000009 | prose | pages [1] -->
Next, we merge the models of income, education and social equality into a global model to and test it in different social groups. We identify the subgroups as professional labors and unskilled workers. The we build a non-linear programming model to decide the resources allocation strategy among different subgroups. We ﬁnd that maximizing the parental leave pay will not reduce the minimum wage and average income signiﬁcantly.

<!-- b000010 | prose | pages [1] -->
Finally, we study the effect of immigrant waves from the view of complex network theory. We generate a scale-free complex network with small world property to represent the interpersonal relationship among all individuals including Mars residents and new immigrants. Our model shows strategy of 10000 migrants every ten years are sustainable, and capable of dealing with a large number of refugees from Earth.

<!-- b000011 | furniture | pages [2] -->
Team # 64486

<!-- b000012 | furniture | pages [2] -->
Page 1 of 33

<!-- b000013 | heading | pages [2] -->
1 Policy Recommendation

<!-- b000014 | prose | pages [2] -->
Honored Director of LIFE, Thank you for hiring and trusting us. We have seen the great success of planned communities that are built across Earth. However, after detailed investigation and deliberate consideration, we ﬁnd that labor management and society plan of the existing experimental communities can be further optimized. Therefore, we feel obliged to recommend the optimal strategies to LIFE to ensure the successful launch of project UTOPIA:2100. Our recommendations are based on precise modeling and computer simulation based on real-world data, thus we are conﬁdent of our proposals.

<!-- b000015 | prose | pages [2] -->
We study the problem both on a micro and macro level. We consider 3 important balancing factors: economy, education, and equality in the vision of sustainability. We have run a 2000-year simulation and validated the robustness of our model. Here we suggest a series of strategies.

<!-- b000016 | prose | pages [2] -->
Select Educated Immigrants In terms of economic development, we propose that LIFE recruit more immigrants who own bachelor degree or higher, and increase the ratio of citizens under 40. Individual with strong innovation ability should be granted privilege in the selection procedure. Our model shows higher ratio of innovator and higher average education level contribute to faster growth of GDP.

<!-- b000017 | prose | pages [2] -->
Maximize Minimum Wage Higher minimum wage results in lower standard deviation of income but lower average income. Nevertheless, concerns about the negative effect of high minimum wage on GDP is unnecessary. Although average income decreases as the minimum wage grows, the change is negligible. The slight negative effect can also be compensated by recruiting skilled labor from Earth.

<!-- b000018 | prose | pages [2] -->
We deﬁne a Happiness Index to evaluation the citizens attitude toward life in Mars. Lower variance of family income leads to higher Happiness Index but lower Net Domestic Product. We balance the two factors and ﬁnd the equilibrium point, at which the minimum wage is around $31708 less than the average personal income. We recommend that minimum wage should be around $33526 and increase as economy grows.

<!-- b000019 | prose | pages [2] -->
Emphasize Education The signiﬁcance of education is ampliﬁed by its correlation with the economic development. Since higher education level leads to higher income and better education of the children, emphasis on education of Population Zero incurs a virtuous circle. If education of the ﬁrst generation is insufﬁcient, chain reaction will lead to a cascade and ﬁnally the downfall of Population Zero.

<!-- b000020 | prose | pages [2] -->
Increase Parental Leave Pay We suggest that LIFE offer parental leave to both fathers and mothers to maintain the equality and maximize the birthrate. Since population need to expand on Mars to created more active labor forces, encouraging birth giving by implementing high parental leave pay is beneﬁcial to the long term development on Mars.

<!-- b000021 | prose | pages [2] -->
Eliminate Discrimination In our complex network model, we ﬁnd that larger scale of population and closer relationship among individuals contribute to higher economic growth speed. Discrimination between local residents of Mars and new immigrants from Earth should be eliminated, since marriages between individuals of the two group is fundamental to the stability of population.

<!-- b000022 | heading | pages [2] -->
Robustness Of Our Model

<!-- b000023 | prose | pages [2] -->
We compare samples of Population Zero with randomly added noises on database. Results show the optimal strategies do not vary much.Since we do not consider the limitation of natural resources on Mars, our model may be less effective in modelling a large scale of population. Health care is not considered, which means additional models should be integrated to our simulation.

<!-- b000024 | prose | pages [2] -->
We hope that our suggestions are useful for LIFE and the UTOPIA:2100 will be a successful beginning of migration to Mars.

<!-- b000025 | prose | pages [2] -->
Sincerely, Team 64486

<!-- b000026 | furniture | pages [3] -->
Team # 64486

<!-- b000027 | furniture | pages [3] -->
Page 2 of 33

<!-- b000028 | heading | pages [3] -->
Contents

<!-- b000029 | contents | pages [3] -->
1 Policy Recommendation

<!-- b000030 | contents | pages [3] -->
1

<!-- b000031 | contents | pages [3] -->
2 Introduction

<!-- b000032 | contents | pages [3] -->
4

<!-- b000033 | contents | pages [3] -->
3 Parameter Deﬁnition And Speciﬁc Outcomes

<!-- b000034 | contents | pages [3] -->
4

<!-- b000035 | contents | pages [3] -->
3.1

<!-- b000036 | contents | pages [3] -->
PUMS Database . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [3] -->
4

<!-- b000038 | contents | pages [3] -->
3.2

<!-- b000039 | contents | pages [3] -->
Three-tier Basic Parameter System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [3] -->
4

<!-- b000041 | contents | pages [3] -->
3.3

<!-- b000042 | contents | pages [3] -->
Derived Index System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [3] -->
5

<!-- b000044 | contents | pages [3] -->
3.3.1

<!-- b000045 | contents | pages [3] -->
Income Factor

<!-- b000046 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000047 | contents | pages [3] -->
5

<!-- b000048 | contents | pages [3] -->
3.3.2

<!-- b000049 | contents | pages [3] -->
Education Factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000050 | contents | pages [3] -->
6

<!-- b000051 | contents | pages [3] -->
3.3.3

<!-- b000052 | contents | pages [3] -->
Equality Factor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000053 | contents | pages [3] -->
6

<!-- b000054 | contents | pages [3] -->
3.4

<!-- b000055 | contents | pages [3] -->
Evaluation Metrics

<!-- b000056 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000057 | contents | pages [3] -->
6

<!-- b000058 | contents | pages [3] -->
4 Population Zero: PUMS Dempgraphics And Immigrants Selection

<!-- b000059 | contents | pages [3] -->
8

<!-- b000060 | contents | pages [3] -->
4.1

<!-- b000061 | contents | pages [3] -->
Random Sample Of 10000 People . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [3] -->
8

<!-- b000063 | contents | pages [3] -->
4.2

<!-- b000064 | contents | pages [3] -->
Selection Criteria And Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [3] -->
8

<!-- b000066 | contents | pages [3] -->
4.3

<!-- b000067 | contents | pages [3] -->
Comparison Between Population Zero And The Random Sample . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [3] -->
9

<!-- b000069 | contents | pages [3] -->
4.3.1

<!-- b000070 | contents | pages [3] -->
Demographic Distributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000071 | contents | pages [3] -->
9

<!-- b000072 | contents | pages [3] -->
5 Evolution Model and Dynamic System

<!-- b000073 | contents | pages [3] -->
11

<!-- b000074 | contents | pages [3] -->
5.1

<!-- b000075 | contents | pages [3] -->
Model Structure and Overview Of Sample Results . . . . . . . . . . . . . . . . . . . . . .

<!-- b000076 | contents | pages [3] -->
11

<!-- b000077 | contents | pages [3] -->
5.2

<!-- b000078 | contents | pages [3] -->
Assumptions and Mathematical Expression For Each System . . . . . . . . . . . . . . . .

<!-- b000079 | contents | pages [3] -->
11

<!-- b000080 | contents | pages [3] -->
5.3

<!-- b000081 | contents | pages [3] -->
Job System

<!-- b000082 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [3] -->
12

<!-- b000084 | contents | pages [3] -->
5.4

<!-- b000085 | contents | pages [3] -->
Education System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [3] -->
13

<!-- b000087 | contents | pages [3] -->
5.5

<!-- b000088 | contents | pages [3] -->
Marriage System

<!-- b000089 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000090 | contents | pages [3] -->
13

<!-- b000091 | contents | pages [3] -->
5.6

<!-- b000092 | contents | pages [3] -->
New Individuals: Child born And Migration System

<!-- b000093 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000094 | contents | pages [3] -->
13

<!-- b000095 | contents | pages [3] -->
5.6.1

<!-- b000096 | contents | pages [3] -->
Newly Born Children . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [3] -->
13

<!-- b000098 | contents | pages [3] -->
5.6.2

<!-- b000099 | contents | pages [3] -->
Migration System . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000100 | contents | pages [3] -->
14

<!-- b000101 | contents | pages [3] -->
6 Trade-offs And Social Equilibrium

<!-- b000102 | contents | pages [3] -->
15

<!-- b000103 | contents | pages [3] -->
6.1

<!-- b000104 | contents | pages [3] -->
Additional Assumptions And Constraints

<!-- b000105 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000106 | contents | pages [3] -->
15

<!-- b000107 | contents | pages [3] -->
6.2

<!-- b000108 | contents | pages [3] -->
Policy For Balance Between Minimum Wage And High Productivity . . . . . . . . . . . .

<!-- b000109 | contents | pages [3] -->
15

<!-- b000110 | contents | pages [3] -->
6.3

<!-- b000111 | contents | pages [3] -->
Best Childcare And Parental Leave Strategy . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000112 | contents | pages [3] -->
16

<!-- b000113 | contents | pages [3] -->
7 Model’s Function For Different Groups

<!-- b000114 | contents | pages [3] -->
18

<!-- b000115 | contents | pages [3] -->
7.1

<!-- b000116 | contents | pages [3] -->
Outcomes Across Different Subgroups . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000117 | contents | pages [3] -->
18

<!-- b000118 | contents | pages [3] -->
7.2

<!-- b000119 | contents | pages [3] -->
Major Subgroup Identiﬁcation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000120 | contents | pages [3] -->
18

<!-- b000121 | contents | pages [3] -->
7.3

<!-- b000122 | contents | pages [3] -->
Best Allocation Strategy

<!-- b000123 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000124 | contents | pages [3] -->
19

<!-- b000125 | contents | pages [3] -->
8 Interpersonal Relationship Network And New Immigrants

<!-- b000126 | contents | pages [3] -->
20

<!-- b000127 | contents | pages [3] -->
8.1

<!-- b000128 | contents | pages [3] -->
Generation Of Interpersonal Network

<!-- b000129 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000130 | contents | pages [3] -->
20

<!-- b000131 | contents | pages [3] -->
8.2

<!-- b000132 | contents | pages [3] -->
Stationary Increment Model And Impact Of Immmigration Waves . . . . . . . . . . . . .

<!-- b000133 | contents | pages [3] -->
21

<!-- b000134 | contents | pages [3] -->
9 Migration Plan Analysis

<!-- b000135 | contents | pages [3] -->
21

<!-- b000136 | contents | pages [3] -->
9.1

<!-- b000137 | contents | pages [3] -->
Inﬂuences By Choosing Different Migration Year . . . . . . . . . . . . . . . . . . . . . .

<!-- b000138 | contents | pages [3] -->
21

<!-- b000139 | contents | pages [3] -->
9.2

<!-- b000140 | contents | pages [3] -->
Phased Over and One-Year Migration

<!-- b000141 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000142 | contents | pages [3] -->
22

<!-- b000143 | contents | pages [3] -->
10 Robustness Analysis

<!-- b000144 | contents | pages [3] -->
23

<!-- b000145 | furniture | pages [4] -->
Team # 64486

<!-- b000146 | furniture | pages [4] -->
Page 3 of 33

<!-- b000147 | heading | pages [4] -->
11 Strengths and Weaknesses

<!-- b000148 | prose | pages [4] -->
23 11.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 11.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

<!-- b000149 | heading | pages [4] -->
References

<!-- b000150 | references | pages [4] -->
24

<!-- b000151 | references | pages [4] -->
A Appendix

<!-- b000152 | references | pages [4] -->
26

<!-- b000153 | references | pages [4] -->
MATLAB Script Of Evolution Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000154 | references | pages [4] -->
A.1

<!-- b000155 | references | pages [4] -->
26

<!-- b000156 | furniture | pages [5] -->
Team # 64486

<!-- b000157 | furniture | pages [5] -->
Page 4 of 33

<!-- b000158 | heading | pages [5] -->
2 Introduction

<!-- b000159 | heading | pages [5] -->
Background

<!-- b000160 | prose | pages [5] -->
In this year of 2095, a series of short-term planned living experiments have been completed on Mars. A group of 10000 people, called Population Zero, will migrate to Mars. Besides all the ad- vanced technologies that make life on Mars possible, an optimal strategy regarding workforce, economy and education should be designed to facilitate the development of Population Zero.

<!-- b000161 | prose | pages [5] -->
Restatement and Clariﬁcation Our team is bound to construct a policy model, which include a set of policy recommendations that will create a sustainable life-plan. To ﬁnd out the optimal strategies, we need to build models, run simulations and present the visualized results. Our model should be scalable, multi- tiered and dynamic. However, trade-offs should be made if two objectives contradict, and the 3 balancing factors are income, education and equality.

<!-- b000162 | prose | pages [5] -->
We aim to solve the following problems:

<!-- b000163 | prose | pages [5] -->
• Deﬁne a set of parameters and metrics and clarify their relations.

<!-- b000164 | prose | pages [5] -->
• Select a group of 10000 citizens as Population Zero and analyze the demographic characteristics.

<!-- b000165 | prose | pages [5] -->
Decide the selection criteria that make UTOPIA:2100 a well-functioning society.

<!-- b000166 | prose | pages [5] -->
• Deﬁne the key elements of a successful society in a 10-year period. Find out the equilibrium between the optimal minimum wage and salary distribution. Find out the optimal parental leave pay.

<!-- b000167 | prose | pages [5] -->
• Identify the major subgroups of your workforce, and identify their main priorities. Adjust our mod- els to balance the needs of different subgroups. Maximize the priority outcomes without sharply reducing the global outcomes.

<!-- b000168 | prose | pages [5] -->
• Build a sustainable Small World network model and deﬁne the dynamics of evolution. Analyze the impact of immigration phased over the next 100 years.

<!-- b000169 | prose | pages [5] -->
• Test the scalability of our network model. Consider a much larger population. Study the robustness of the model.

<!-- b000170 | heading | pages [5] -->
3 Parameter Deﬁnition And Speciﬁc Outcomes

<!-- b000171 | heading | pages [5] -->
3.1 PUMS Database

<!-- b000172 | prose | pages [5] -->
The American Community Survey (ACS) Public Use Microdata Sample (PUMS)[1] ﬁles are a set of 284 different untabulated records including population and housing unit records with individual information such as relationship, sex, educational attainment, and employment status, et cetera. It is convenient for people who are looking for accessibility to inexpensive data for research projects. However, there is a thing worth noting that PUMS does not contain information of people under 16 years old.

<!-- b000173 | heading | pages [5] -->
3.2 Three-tier Basic Parameter System

<!-- b000174 | prose | pages [5] -->
In order to quantify the characteristics of Population Zero, we clarify the fundamental parameters that would be applied in our models. The parameters are classiﬁed according to the objects they describe and the aspect of the outcomes they contribute to.

<!-- b000175 | prose | pages [5] -->
There are 3 tiers of parameters, which deliver quantitative information about Population Zero on indi- vidual level, family level and societal level respectively. In each tier, important factors related to income, education and equality are adopted as parameters. The Fig.1 below illustrates a clear structure of predomi- nate parameters whose detailed information is in Tab.1.

<!-- b000176 | furniture | pages [6] -->
Team # 64486

<!-- b000177 | furniture | pages [6] -->
Page 5 of 33

<!-- b000178 | caption | pages [6] -->
Figure 1: Hierarchy Figure

<!-- b000179 | heading | pages [6] -->
3.3 Derived Index System

<!-- b000180 | prose | pages [6] -->
To simplify the 3-tier basic parameter, we design a comprehensive index system to present a more de- tailed quantitative description of Population Zero and try to reveal the relation or dependency among the parameters.

<!-- b000181 | heading | pages [6] -->
3.3.1 Income Factor

<!-- b000182 | prose | pages [6] -->
From individual level, personal income, personal savings rate are most important parameters. The relation- ship between them are as follows, according to U.S. Bureau of Economic Analysis[2]

<!-- b000183 | prose | pages [6] -->
DPI = RPI ∗(1 −rtax) (1)

<!-- b000184 | prose | pages [6] -->
where RPI is real personal income(adjusted for inﬂation, but in our model equals to personal income), DPI is disposable personal income, rtax is tax rate.

<!-- b000185 | prose | pages [6] -->
rs = DPI −PCE (2) DPI

<!-- b000186 | prose | pages [6] -->
where PCE is personal consuption expenditure, rs is personal saving rate. rs < 0 indicates that his income can’t meet his expenditure thus in bad condition. If rs ≥0 and is low, then he is in good condition and there is no need for him to worry about future. If rs ≥0 and is high, then he is in good condition but has to worry about his future.

<!-- b000187 | prose | pages [6] -->
From household level, child care takes a large proportion of family expenditure.

<!-- b000188 | prose | pages [6] -->
rce = Fc (3) Fexp

<!-- b000189 | prose | pages [6] -->
where rce is childcare expenditures rate, Fc is average family childcare expenditure, Fexp is average family expenditure.

<!-- b000190 | prose | pages [6] -->
From societal level, GDP and NDP are most essential outcomes.

<!-- b000191 | prose | pages [6, 7] -->
GDP = α ∗P ∗(1 −run) (4) where α is average workforce productivity which is related to working hours and creative activity involved in producing innovations, P is the total number of people, run is unemployment rate.

<!-- b000192 | furniture | pages [7] -->
Team # 64486

<!-- b000193 | furniture | pages [7] -->
Page 6 of 33

<!-- b000195 | prose | pages [7] -->
NDP = GDP −Wmin ∗Pmww −Bcc (5)

<!-- b000196 | prose | pages [7] -->
where Wminis minimum wage, Pmww is the number of minimum wage workers, Bcc is annual childcare budget.

<!-- b000197 | heading | pages [7] -->
3.3.2 Education Factor

<!-- b000198 | prose | pages [7] -->
Present education level(EDL) of a population can be calculate by following formulation[3]

<!-- b000199 | prose | pages [7] -->
EDL = (Yave,s + Yexp,s 18 ) ∗0.5 (6) 15

<!-- b000200 | prose | pages [7] -->
where Yave,s is “expected years of schooling” (Number of years a child of school entrance age can expect to spend in a given level of education) and “Mean years of schooling” (Average number of completed years of education of a population [25 years and older]).

<!-- b000201 | heading | pages [7] -->
3.3.3 Equality Factor

<!-- b000202 | prose | pages [7] -->
Given a continuous probability distribution function of income pin(x), where pin(x)dx is the fraction of the population with income x to x + dx, then the Gini coefﬁcient[4] is half of the relative mean absolute difference: ∫∞ ∫∞ Gse = 1 p(x)p(y) |x −y| dx dy (7) 2µ −∞ −∞ ∫∞ where µ is the mean of the distribution µ = −∞x p(x) dx and the lower limits of integration may be replaced by zero when all incomes are positive.

<!-- b000203 | heading | pages [7] -->
3.4 Evaluation Metrics

<!-- b000204 | prose | pages [7] -->
The frequency of words related to the topic “a well-being society” in the Social Science Research Network database[5] effectively reﬂects the importance of factors contributing to a successful society. According to the word frequency, we allocate different weights to the factors in our model. To better visualize the most concerned factors, we generated a word cloud as shown in Fig.2.

<!-- b000205 | caption | pages [7] -->
Figure 2: Word cloud: the ﬁgure shows equality is the most concerned factor.

<!-- b000206 | furniture | pages [8] -->
Team # 64486

<!-- b000207 | furniture | pages [8] -->
Page 7 of 33

<!-- b000208 | caption | pages [8] -->
Table 1: Parameter List

<!-- b000209 | prose | pages [8] -->
Name

<!-- b000210 | heading | pages [8] -->
Symbol

<!-- b000211 | prose | pages [8] -->
Type Tier Factor Dict[6] Unit ral Active Labor Force Ratio Numerical Societal Income A Age Numerical Individual Equality AGEP Year Fexp Annual Family Expenditure Numerical Family Income $ Hin Annual Family Income Numerical Family Income FINCP $ Aavg Average Age Numerical Societal Income Year Yave,s Average Educational Attainment Class Societal Education SCHL Bcc Childcare Budget Numerical Societal Equality $ DPI Disposable Personal Income Numerical Individual Income $ Meb Education Budget Numerical Societal Education $ EDL Education Development Level Numerical Societal Education Seth Ethnicity Class Individual Equality ACN1P rer Ethnicity Ratio Numerical Societal Equality Yexp,s Expected Years of Schooling Numerical Societal Education Fc Family Childcare Expenditure Numerical Family Equality $ Nfs Family Size Interger Family Income NPF Person Sft Family Type Class Family Income FES G Gender 0-1Variable Individual Equality SEX Gie Gini Coefﬁcient of Income Equality Numerical Societal Equality rcp Making Childcare Payment Rate Percent Family Equality Sms Marital status Class Individual Equality MAR Wmin Minimum Wage Numerical Societal Income $ Pmww Number of Minimum Wage Worker Interger Societal Income Person Soc Occupation Class Individual Income OCCP PLP Parental Leave Pay Numerical Societal Equality $ PCE Personal Consumption Expenditures Numerical Individual Income $ rs Personal Savings Rate Percent Individual Income P Population Integer Societal Income Person RPI Real Personal Income Numerical Individual Income PINCP $ rsr Sex Ratio Numerical Societal Equality rtax Tax Payment Percentage Percent Individual Income run Unemployment Rate Percent Societal Equality tw Weekly Working Hours Numerical Individual Income WKHP Hour

<!-- b000212 | prose | pages [8] -->
Through the Analytical Hierarchy Process(AHP), we deﬁne two sets of weights when calculating GDP Index and Happiness respectively. Starting from the ﬁrst criteria of the hierarchy ﬁgure(Fig.1), we structure comparison matrix by Comparison Method of 1-9[7]. Then, we get the weights of income factor, education factor and equality factor to Happiness Index, as is shown in Tab.2. By calculating the weights of three factors in hierarchy II, we get the maximum eigenvalue is 3.0044, consistency ratio CR = 0.0043, which meets AHP’s consistency ratio requirement.

<!-- b000213 | prose | pages [8] -->
Following the above procedures and adjusting comparison matrix until every matrix’s consistency ratio CR ≤0.1, we obtain two set of weights. Due to limitation of paper page, other pairwise comparison matrix is not appended. Finally, all the weights are shown in Tab.3 and Tab.4. They can used to evaluate GDP Index and Happiness Index of Population Zero.

<!-- b000214 | furniture | pages [9] -->
Team # 64486

<!-- b000215 | furniture | pages [9] -->
Page 8 of 33

<!-- b000216 | caption | pages [9] -->
Table 2: Comparison matrix of happiness hierarchy I-II

<!-- b000217 | prose | pages [9] -->
Happiness Income Education Equality Weight Income 1 2 1/5 0.247 Education 1/2 1 1/6 0.202 Equality 5 6 1 0.550

<!-- b000218 | caption | pages [9] -->
Table 3: Criteria weights of hierarchy I-II

<!-- b000219 | prose | pages [9] -->
Factor GDP Happiness Income 0.462 0.299 Education 0.373 0.259 Equality 0.165 0.442

<!-- b000220 | caption | pages [9] -->
Table 4: Criteria weights of hierarchy II-III

<!-- b000221 | prose | pages [9] -->
Name GDP Happiness Factor Annual Family Expenditure 0.134 0.123 Income Annual Family Income 0.145 0.107 Income Minimum Wage 0.061 0.176 Income Number of Minimum Wage Worker 0.155 0.083 Income Personal Savings Rate 0.048 0.184 Income Real Personal Income 0.397 0.142 Income Weekly Working Hours 0.060 0.185 Income Education Budget 0.399 0.462 Education Education Development Level 0.601 0.538 Education Childcare Budget 0.133 0.131 Equality Ethnicity Ratio 0.129 0.173 Equality Family Childcare Expenditures Rate 0.144 0.141 Equality Gini Coefﬁcient of Income Equality 0.252 0.252 Equality Sex Ratio 0.127 0.214 Equality Unemployment Rate 0.215 0.089 Equality

<!-- b000222 | heading | pages [9] -->
4 Population Zero: PUMS Dempgraphics And Immigrants Selec-

<!-- b000223 | prose | pages [9] -->
tion

<!-- b000224 | heading | pages [9] -->
4.1 Random Sample Of 10000 People

<!-- b000225 | prose | pages [9] -->
To study the demographics of the potential Population Zero members, we extract data from PUMS database, which contains personal data of 1618489 individuals, and carry out data mining. Regarding the limitation of computational power, analyzing the whole data set is inconvenient and unnecessary. Instead, we ﬁrst generate a sample of 10000 immigrants totally randomly using SAS, SQL Server. We suppose that every individual has an equal opportunity to be selected as a member of Population Zero.

<!-- b000226 | heading | pages [9] -->
4.2 Selection Criteria And Algorithm

<!-- b000227 | prose | pages [9] -->
To build a peaceful, cooperative, egalitarian society of Utopia:2100, we select members of Population Zero under certain criteria. We believe that an ideal society should be balanced and harmonic, which can be speciﬁed as:

<!-- b000228 | furniture | pages [10] -->
Team # 64486

<!-- b000229 | furniture | pages [10] -->
Page 9 of 33

<!-- b000230 | caption | pages [10] -->
Figure 3: Selection Criteria

<!-- b000231 | prose | pages [10] -->
• We deﬁne innovators as individual under 40 and own bachelor degrees or higher. Since Population Zero will migrate to a new and undeveloped environment, innovation will be vital to help them adapt to the uncertainties and changeability in the Martian habitation. Innovators should outnumber producers. We set the innovator-to-producer ratio as 7:3.

<!-- b000232 | prose | pages [10] -->
• Building the Martian habitation need skilled labor. We deﬁne ”skilled labor” as individuals working for more than 35 hours per week. We have a strong preference for skilled labor when selecting members, therefore we set the skilled-to-unskilled labor ratio as 9:1.

<!-- b000233 | prose | pages [10] -->
• In order to maximize the birth rate, we set the male-female ratio as exactly 1:1.

<!-- b000234 | prose | pages [10] -->
• To ensure the stability of the society, we require citizens to migrate together with their spouses . Citizens will not be selected if their spouses are not eligible for Population Zero Program, and children should migrate with their parents.

<!-- b000235 | prose | pages [10] -->
• In consideration of equality, the selection process is based on a non-biased policy, i.e. other individual differences such as ethnicity, characteristics, and sexual orientation will not be considered.

<!-- b000236 | prose | pages [10] -->
Based on the criteria, we classify the candidates and tag them as 4 different types, and then select a partic- ular number of each type to join the Population One. The classiﬁcation procedure and the numbers of each type are speciﬁed in Fig.3.

<!-- b000237 | prose | pages [10] -->
After this procedure, we ﬁlter out those candidates whose spouses are not in the selected Population Zero and check if their spouses can take the place of another candidate. If not, the those candidates will be substituted.

<!-- b000238 | heading | pages [10] -->
4.3 Comparison Between Population Zero And The Random Sample

<!-- b000239 | prose | pages [10] -->
In order to validate our selection criteria, we compare the demographics of the random sample and Pop- ulation Zero. We ﬁnd that Population Zero’s advantages are apparent in regard to income, education and equality.

<!-- b000240 | heading | pages [10] -->
4.3.1 Demographic Distributions

<!-- b000241 | prose | pages [10] -->
As is show in Fig.4 and Fig.5, Population Zero has a higher average annual income and a lower standard deviation of 46844.11 dollars, compared to 52043.95 of the random sample. We believe that higher income and smaller income difference alleviate inequality and increase citizens’ happiness to an extend.

<!-- b000242 | prose | pages [10] -->
From Fig.6 and Fig.7, we can not tell a huge difference between the random sample and Population Zero. Since working hour per week centers near 40 hours/week, we ﬁnd this criterion unnecessary.

<!-- b000243 | prose | pages [10] -->
Population Zero have a higher average education level(shown in Fig.8 and Fig.9), since we have a strong preference for innovators, who own bachelor degrees or higher.

<!-- b000244 | furniture | pages [11] -->
Team # 64486

<!-- b000245 | furniture | pages [11] -->
Page 10 of 33

<!-- b000246 | caption | pages [11] -->
Figure 4: Random sample: distribution of annual

<!-- b000247 | caption | pages [11] -->
Figure 5: Population Zero: distribution of annual

<!-- b000248 | prose | pages [11] -->
income income

<!-- b000249 | caption | pages [11] -->
Figure 6: Random sample: distribution of weekly

<!-- b000250 | caption | pages [11] -->
Figure 7: Population Zero: distribution of weekly

<!-- b000251 | prose | pages [11] -->
working hour working hour

<!-- b000252 | caption | pages [11] -->
Figure 8: Random sample: distribution of educa-

<!-- b000253 | caption | pages [11] -->
Figure 9: Population Zero: distribution of educa-

<!-- b000254 | prose | pages [11] -->
tion level tion level

<!-- b000255 | caption | pages [11] -->
Figure 10: Random sample: distribution of age

<!-- b000256 | caption | pages [11] -->
Figure 11: Population Zero: distribution of age

<!-- b000257 | prose | pages [11, 12] -->
In terms of age distribution, we believe a younger group have a stronger ability to innovate and repro- duce, which will be important for new Mars residents. Population Zero has an obvious advantage over the random sample. Besides, Sex ratio is adjusted to the optimal 1:1 to maximize birthrate.

<!-- b000258 | furniture | pages [12] -->
Team # 64486

<!-- b000259 | furniture | pages [12] -->
Page 11 of 33

<!-- b000261 | prose | pages [12] -->
We draw funnel charts and pyramid charts to analyze the if gender affects education level. We ﬁnd that male have higher degrees in general, and the selected Population Zero show less difference between male and female regarding education level, which makes marriage easier and improves equality.

<!-- b000262 | heading | pages [12] -->
5 Evolution Model and Dynamic System

<!-- b000263 | prose | pages [12] -->
As we have thoroughly discussed the methods and variables to describe the features of Population Zero, we need to know how these variables change with time. Therefore, a dynamic evolution model is required.

<!-- b000264 | heading | pages [12] -->
5.1 Model Structure and Overview Of Sample Results

<!-- b000265 | prose | pages [12] -->
Here we present the general algorithm and a sample result of one-hundred-year evolution shown in Fig.12. Our model starts with the Population Zero data and the evolution part provides the social environment for each person. This evolution model is close to reality because it simulates a lot of natural process including job, marriage, education, etc. Systems which describe aforementioned process is discussed in detail in Sec 4.3.1.

<!-- b000266 | prose | pages [12] -->
In the ﬁrst ﬁve years after Population Zero’s arrival on Mars, young and unmarried migrants give birth to children, which causes the “boomer generation I”(Fig.12(b),(g)) and the population grows. However, after the ﬁrst ten years, there is no newly born child, meanwhile part of migrants pass away. Therefore, the population and GDP decrease. The situation is generally getting worse in the ﬁrst sixty years(Fig.12(a),(e)) . After that, most migrants from Population Zero pass away and “baby boomer generation I” with its echo ”baby boomer generation II-III” reaches a relatively stable stage of population evolution(Fig.12(a),(g)). After approximately year 60, population and GDP started to rise with ﬂuctuation, according to our 200- year evolution simulation result.

<!-- b000267 | prose | pages [12] -->
Apart from the sample results shown in the Fig.12, our model provides statistical data on education, working hours and occupation distribution. In addition, this model enables us to keep track on the marriage relationship and father(mother)-child relationship which is helpful for future racial and genetic research.

<!-- b000268 | heading | pages [12] -->
5.2 Assumptions and Mathematical Expression For Each System

<!-- b000269 | prose | pages [12] -->
After our effective selection procedure, Population Zero are now prepared to construct a whole new city on Mars. We simulate their evolution by MATLAB programming, and test whether our selection criteria are truly beneﬁcial to their new life on Mars.

<!-- b000270 | prose | pages [12] -->
Our model and simulation are based on the following assumptions:

<!-- b000271 | prose | pages [12] -->
• Residents only die off naturally. Foods are sufﬁciently supplied and there is no diseases and natural catastrophe which causes death irregularly. The death probability as a logistic function of age is deﬁned as p = 1/(1 + exp (−0.15(x −70)))

<!-- b000272 | prose | pages [12] -->
• Every employed citizen has tax obligation. We set the unemployment rate at 5% according to the estimation method proposed by Blanchard et al(2010).[9]

<!-- b000273 | prose | pages [12] -->
• To ensure the well-being and equality of the society, we design a social security system, which requires the minimum annual wage to be $5000. Social relief fund is offered to non-labor individuals.

<!-- b000274 | prose | pages [12] -->
• In our ideal situation, wealth is redistributed more equitably among society. We set the tax rate at 0.15, which will be a reasonable number according to Maniquet and Neumann(2016)[10].

<!-- b000275 | furniture | pages [13] -->
Team # 64486

<!-- b000276 | furniture | pages [13] -->
Page 12 of 33

<!-- b000277 | caption | pages [13] -->
Figure 12:

<!-- b000278 | prose | pages [13] -->
Database structure, algorithm and a sample result of the model.(a)population of certain kind of people each year(AL=alive,D=dead,AD=adult,M=male,F=female,W=people whose income under minimal wage); (b)sex ratio of male/female each year; (c)rate of unemployment(un), rehire(reh) and retire(ret) each year; (d)population of newly born children each year; (e)Gross Domestic Product(GDP) and Net Domestic Product(NDP) each year; (f)GDP per capita each year; (g)histogram of age distribution of Population Zero(start) and population after 100 years(end); (h) Average happiness index each year; All person’s information in Population Zero corre- sponds to a person in reality(Data source:[1]); Other parameters: minimal wage 5000$/year; Parental leave pay is 40000$/year;retirement age is 65; rate of natural unemployment is 5 %; NO migration from earth after year 0;

<!-- b000279 | prose | pages [13] -->
• Effective functioning of the society needs active labor force, retirement age is 65 in our simulation.

<!-- b000280 | prose | pages [13] -->
Referring to information provided by National Academy of Social Insurance[11], we believe it is reasonable.

<!-- b000281 | prose | pages [13] -->
• Parental leave is allowed. Parents who have newly-born children are granted a one-year leave with a subsidy of 40000 dollars.

<!-- b000282 | prose | pages [13] -->
Based on the assumptions and the notations system in Task 1, we present our algorithm and its math- ematical expression. We denote the ith individual as Pi. Every individual has 6 attributes: individual ID number IDi, education level Sed,i, sex Gi, age Ai, annual income Pri,i and marital status Sma,i. We deﬁne 6 vectors to store the information of the living individuals. It is worth noting that the length of the vectors changes after every iteration when the population changes, which we will elaborate in Sec 5.5.

<!-- b000283 | heading | pages [13] -->
5.3 Job System

<!-- b000284 | prose | pages [13, 14] -->
A person’s job is his role in society. Most people spend up to forty or more hours each week in paid em- ployment. Some exceptions are non-labor force population including children (under 18), retirees (above 65), and people with disabilities. Labor population is comprised of unemployed (with a rate rre of ﬁnding a job again) and employed (with a rate run of losing job) workforce. Unskilled (with a rate rdis to become disabled) and professional are deﬁned by their age and education and working hours. The type of job of each employee and income is determined by his education level and age. Speciﬁcally, income is determined )×(1.5−|A−35 by the following function I = rtex×Norm(NDPPmean, NDPPσ)×(1+ SCHL−18 100 ) where 18 NDPPmean and NDPPσ are mean value and standard deviation of productivity last year. This function is modiﬁed if some of the parameters are irrelevant in order to run this complex simulation program quicker on our personal computer.

<!-- b000285 | furniture | pages [14] -->
Team # 64486

<!-- b000286 | furniture | pages [14] -->
Page 13 of 33

<!-- b000288 | heading | pages [14] -->
5.4 Education System

<!-- b000289 | prose | pages [14] -->
It has been argued that high rates of education are essential for countries to be able to achieve high levels of economic growth[12]. Therefore, we grant everyone in our model equal access to education opportunities no matter they are rich or pool, no matter they are male or female. However, where they are going to end their education depends on their personal experience. And we use normal distribution to describe his probability to ﬁnish education at different stages. The normal distribution is determined by mean value and standard deviation of EDL(SCHL) last year.

<!-- b000290 | heading | pages [14] -->
5.5 Marriage System

<!-- b000291 | prose | pages [14] -->
It is widely quoted that “love is a chemical reaction”. In our system, we stipulate that the closer two individuals of opposite sexes are, the more likely the “chemical reaction” will occur, and they will found a marriage relationship. We deﬁne the distance between two individual as √ (Ai −Aj)2 + (Pri,i −Pri,j)2 dij = (8)

<!-- b000292 | prose | pages [14] -->
We generate an adjacent matrix to record the distance between every 2 individuals and initialize a path matrix to record marriage relationships. Suppose there are m males and n females in Population Zero. When a marriage occurs betweeen Pi and Pj, the element pij in matrix P will become 1. We deﬁne the marriage probability between a male adult and a female adult as

<!-- b000293 | prose | pages [14] -->
Prmar,ij = 1 −dij (9) dmax

<!-- b000294 | prose | pages [14] -->
We ﬁrst ﬁnd out the 2 individuals Pi and Pj with the highest possibility to get married, turn pij in matrix P to 1 and let Prmar,iq = 0 and Prmar,pj = 0,where 0 ≤m and 0 ≤n. In the next iteration, the repeat the same steps. Under this marriage mechanism, we simulate the process with MATLAB and our code is attached in the Appendix. We input a sample of 10000 selected members of Population Zero, and we get the result after 100 iterations, which are interpreted as a 100-year evolution.

<!-- b000295 | prose | pages [14] -->
To have a clear view of marriage and parenthood relationship among citizens, we present an a visual- ization of family network of 40 citizens(Fig.13). Citizen ID are shown as the number in circle. Apparently, marriage linkages are far more sparse than parent hood linkages. It might be caused by our evolution mechanism: in our model, one marriage may generate more than 2 babies.

<!-- b000296 | heading | pages [14] -->
5.6 New Individuals: Child born And Migration System

<!-- b000297 | prose | pages [14] -->
New population come from 2 sources: newly born children of residents on Mars and new immigrant from Earth. We discuss their mechanism respectively.

<!-- b000298 | heading | pages [14] -->
5.6.1 Newly Born Children

<!-- b000299 | prose | pages [14, 15] -->
Once marriage relationship is established between 2 individuals[8], the couple are granted the right to give births to children. Every couple expect to have 2 children throughout their life. The couple are able to bidirectional arrows represent mar- moves to a stabilization. riages and the grey directional arrows show the parenthood.

<!-- b000300 | furniture | pages [15] -->
Team # 64486

<!-- b000301 | furniture | pages [15] -->
Page 14 of 33

<!-- b000302 | caption | pages [15] -->
Figure 13: Family Network:The red

<!-- b000303 | caption | pages [15] -->
Figure 14: Marriage ratio increases in the ﬁrst 60 years and

<!-- b000305 | prose | pages [15] -->
give birth if and only if both of the husband and the wife are between 19 and 40 years old. Every couple has 20-year child-bearing period and expect to have 2 children in total, thus they have a probability of 0.1 to give birth to a baby every year. In further consideration, pregnancy will be more dangerous if the wife is above 35. According to van Kooij et al(1996)[13], pregnancy rate is age-dependent. We adjust the pregnancy probability according to the wife’s age. The new probability density function of age Ai is

<!-- b000306 | prose | pages [15] -->
f(A) = −1.875 × 10−4A2 −6.14 × 10−3A (10)

<!-- b000307 | prose | pages [15] -->
f(A) satisﬁes ∫40 f(A)dA = 1 20 ∫40 Af(A)dA = 2 20

<!-- b000308 | prose | pages [15] -->
Newly born children are designated a citizen ID simultaneously, attributes are added according to the following rules:

<!-- b000309 | prose | pages [15] -->
• A baby has a 50% probability to be male or female.

<!-- b000310 | prose | pages [15] -->
• Child’s ethnicity is the same as his/her father.

<!-- b000311 | prose | pages [15] -->
• Children under 18 have NULL value in attributes of income, marital status and education level. Once they turn 19, they are allocated a random value of the attributes in a certain probability, which is dependent on their parent’s attributes.

<!-- b000312 | heading | pages [15] -->
5.6.2 Migration System

<!-- b000313 | prose | pages [15] -->
New immigrants from Earth have their original attribute, and they may contribute to the diversity of the population on Mars. Meanwhile, they may also increase the burden on the welfare system.

<!-- b000314 | prose | pages [15] -->
Marriage relationship may be established between a new immigrant and a member of Population Zero or a Mars-born adult. The marriage linkages are built based on the same rules as stated above. New immigrants are allowed to get married to a Mars resident right after they arrive on Mars, no time lag is considered.

<!-- b000315 | furniture | pages [16] -->
Team # 64486

<!-- b000316 | furniture | pages [16] -->
Page 15 of 33

<!-- b000317 | heading | pages [16] -->
6 Trade-offs And Social Equilibrium

<!-- b000318 | prose | pages [16] -->
We have built models of evolution and relationship network in the previous sections. By inputting different parameters into the model and simulation, we obtain varied outcomes, which provide vital information for deciding the optimal strategies of economics, education, and governance policies on Mars.

<!-- b000319 | heading | pages [16] -->
6.1 Additional Assumptions And Constraints

<!-- b000320 | prose | pages [16] -->
Our model is capable of simulating more than 2000 years of Population Zero’s evolution, which we have validated. Nonetheless, adjustments of constraints and parameters should be made every 10 years to ensure the population’s healthy development.

<!-- b000321 | prose | pages [16] -->
Since the population is self-adaptive, changes of parameters may be caused by internal factors or ex- ternal manipulation. In our analysis, we divide the impact factors into 2 categories: endogenous and exogenous inﬂuences.

<!-- b000322 | prose | pages [16] -->
• Residents on Mars are not allowed to return to Earth.

<!-- b000323 | prose | pages [16] -->
• When the population on Mars is below 1000, a group of 10000 immigrants from Earth must be sent to Mars.

<!-- b000324 | prose | pages [16] -->
• If the number of newly born children is below 60, parental leave pay will be raised by 20% and the pregnancy probability will be raised by 10%.

<!-- b000325 | heading | pages [16] -->
6.2 Policy For Balance Between Minimum Wage And High Productivity

<!-- b000326 | prose | pages [16] -->
Instead of searching for the global optimum, we aim to ﬁnd out the local optimum of the minimum wage near $25000 per year, which is almost half of the average annual income. The minimum wage must be lower than the average annual income and within a reasonable range, thus global optimization of the minimum wage is unnecessary.

<!-- b000327 | prose | pages [16] -->
We input different value of minimum wages and ﬁnd that it is negatively correlative with the Net Domestic Product, as is shown in Fig.15 .

<!-- b000328 | prose | pages [16] -->
Through the Analytical Hierarchy Process in Section3.4, we ﬁnd that the standard deviation of personal income has the greatest inﬂuence on the Happiness Index. We deﬁne the optimal minimum wage and salary distribution that minimize the standard deviation of personal income. For simplicity, we take family as the vital unit. In our model, “family” is deﬁned as a couple with or without children under 18. Based on our previous simulation, we count the number of families.

<!-- b000329 | prose | pages [16] -->
Consider the Mars city of families which has been divided into 5 economic brackets: class A, B, C, D, and E according to their economic condition. The annual income of each class according to the following distribution: Each year families move among the 5 classes with certain probability, the class transition chart

<!-- b000330 | caption | pages [16] -->
Table 5: Distribution Of Annual Family Income (Wmin is the minimum wage)

<!-- b000331 | prose | pages [16] -->
Class A B C D E Wmin Income($) 35000 60000 85000 160000 Proportion 5% 20% 45% 25% 10% Cumulative Proportion 5% 25% 70% 75% 100%

<!-- b000332 | prose | pages [16] -->
below speciﬁes the process: λ1 ration of Class A families transit to Class B, et cetera.

<!-- b000333 | furniture | pages [17] -->
Team # 64486

<!-- b000334 | furniture | pages [17] -->
Page 16 of 33

<!-- b000335 | caption | pages [17] -->
Figure 15:

<!-- b000336 | prose | pages [17] -->
The NDP-minimum wage

<!-- b000337 | caption | pages [17] -->
Figure 16: Class Transition Of Family Class

<!-- b000338 | prose | pages [17] -->
curve from the 7th to 10th year of evolu- tion

<!-- b000339 | prose | pages [17] -->
Suppose that the transition state is stable, i.e. the proportion of each class is constant (denoted as the Class capital letter), we have

<!-- b000340 | prose | pages [17] -->
λ1A = µ4B (11) λ1A + µ3C = (λ2 + µ4)B (12) λ2A + µ2C = (λ3 + µ3)C (13) λ3A + µ1C = (λ4 + µ2)C (14) λ4A = µ1B (15)

<!-- b000341 | prose | pages [17] -->
Our objective is to increase the minimum wage and average income, but decrease the standard deviation. Denote the family income of Class k as xk and the proportion of each Class as nk respectively, we have the objective function

<!-- b000342 | prose | pages [17] -->
5 ∑ maxZ1 = xknk (16) k=1 v u 5 ∑ u t (xk −AV G)2nk minZ2 = (17) k=1 maxZ3 = Wmin (18)

<!-- b000343 | prose | pages [17] -->
The calculation of nk is also speciﬁed in Tab.6 The problem of ﬁnding the equilibrium point between high quality of life and optimal minimum wage is deducted to a multi-objective optimization. Using a controlled elitist genetic algorithm[14], we ﬁnd out the optimal solution, Fig.17 gives detailed information about all the feasible solutions after 50 iterations. And the optimal feasible solution is (Z1, Z2, Z3) = (65234, 9848, 33526)

<!-- b000344 | heading | pages [17] -->
6.3 Best Childcare And Parental Leave Strategy

<!-- b000345 | prose | pages [17, 18] -->
We are interested in deciding the optimal parental leave pay. We continue to use the model in section 6.2 to carry out the computational optimization. We assume that parental leave pay will be given to both the mother and father. Therefore, we add an additional class P to represent families that are in a parental leave status and receive a ﬁxed parental leave pay. The State Transition Chart should be altered, as is shown in A Class Wmin Income($) n1 = 5% −5%λ1 + 20%µ4 Adjusted Proportion B Class Income($) 35000 n2 = 20% −20%(λ2 + µ4) + 5%λ1 −45%µ3 Adjusted Proportion C Class Income($) 60000 n3 = 45% −45%(λ3 + µ3) + 20%λ2 −25%µ2 Adjusted Proportion D Class Income($) 85000 n4 = 25% −25%(λ4 + µ2) + 5%λ3 −45%µ1 Adjusted Proportion E Class Income($) 160000 n5 = 10% + 25%4 −10%µ1 Adjusted Proportion

<!-- b000346 | caption | pages [17] -->
Fig.18.

<!-- b000347 | furniture | pages [18] -->
Team # 64486

<!-- b000348 | furniture | pages [18] -->
Page 17 of 33

<!-- b000349 | caption | pages [18] -->
Table 6: Calculation Of nk

<!-- b000351 | caption | pages [18] -->
Figure 17: The 3 axes show the data of standard deviation, minimum wage and average family income

<!-- b000352 | prose | pages [18] -->
respectively.

<!-- b000353 | prose | pages [18] -->
Furthermore, considering that higher parental leave pay Mpl may promote birth giving, we deﬁne p as the as a function of Mpl p = 1 πarctan(x −55000) + 0.5 (19)

<!-- b000354 | prose | pages [18] -->
The result is presented in Fig.19. We ﬁnd the interesting facts that

<!-- b000355 | prose | pages [18] -->
• Parental leave pay doesn’t affect average family income much. It can be explained that if wealthy family start a parental leave, families in lower class have more opportunity to move upward since the standard deviation need to be minimized.

<!-- b000356 | prose | pages [18] -->
• Higher parental leave pay leads to lower minimum wage, since minimizing the standard deviation is also one of the objectives. Meanwhile, average income are maximized so the decrease in the minimum wage is not sharp.

<!-- b000357 | prose | pages [18, 19] -->
• We ﬁnd the minimum of standard deviation $9806.001651, and the correspondent parental leave pay equal chance to transit to parental leave

<!-- b000358 | furniture | pages [19] -->
Team # 64486

<!-- b000359 | furniture | pages [19] -->
Page 18 of 33

<!-- b000360 | caption | pages [19] -->
Figure 18: Families of Class A,B,C,D,E have

<!-- b000362 | caption | pages [19] -->
Figure 19: Average income, and standard deviation and

<!-- b000363 | prose | pages [19] -->
minimum wage change by parental leave pay.

<!-- b000364 | prose | pages [19] -->
$50200 per person for both the father and mother. This provides important evidence for our parental leave strategy.

<!-- b000365 | heading | pages [19] -->
7 Model’s Function For Different Groups

<!-- b000366 | heading | pages [19] -->
7.1 Outcomes Across Different Subgroups

<!-- b000367 | prose | pages [19] -->
Our model function differently across age, education level. Fig20 shows that young people and old people are slight happier than middle age people. Because middle age people have to work and take care of their children and old parents. Fig21 shows that people with education level like a regular high school diploma are less happier. Because they have to unskilled work for longer hours but getting lower payment. Therefore, we ﬁnd that our model function much more different across age and education.

<!-- b000368 | caption | pages [19] -->
Figure 20: Happiness across age

<!-- b000369 | caption | pages [19] -->
Figure 21: Happiness across education

<!-- b000370 | heading | pages [19] -->
7.2 Major Subgroup Identiﬁcation

<!-- b000371 | prose | pages [19, 20] -->
There are a variety of way to categorize the workforce of a country. For example, workforce is can be divided into subcategories like professional and unskilled workforce, male and female workforce, agricul- tural and non-agricultural workforce. Since UTOPIA:2100 is an egalitarian society, there is no difference in productivity between male and female workforce in our model. Moreover, ﬁeld of workforce is not involved due to the simpliﬁcation of our model. Finally, our model function differently across age and edu- cation which are criteria to identify skilled workforce and unskilled workforce. Therefore, the predominate subgroups of workforce in our model are professional workforce, unskilled workforce and unemployed workforce.

<!-- b000372 | furniture | pages [20] -->
Team # 64486

<!-- b000373 | furniture | pages [20] -->
Page 19 of 33

<!-- b000375 | prose | pages [20] -->
Professional workforce is the specialized part of the labor force with advanced education and earns a large income.There is no need for them to worry about how to make a living. Hence, they require more time off and parental leave to enhance the sense of happiness.

<!-- b000376 | prose | pages [20] -->
Unskilled workforce is generally characterized by a lower educational attainment, such as a high school diploma and typically results in smaller wages. And their main priority is work hours, disability care, child care, and minimum wage.

<!-- b000377 | prose | pages [20] -->
Their priorities are shown in Tab.7 and

<!-- b000378 | caption | pages [20] -->
Table 7: Added Parameters

<!-- b000379 | prose | pages [20] -->
Symbol Description rdc Disability Care Budget Rate Nplo Paid Leave Off Days Per Year

<!-- b000380 | heading | pages [20] -->
7.3 Best Allocation Strategy

<!-- b000381 | prose | pages [20] -->
With the consideration of identiﬁed subgroups, we adjust our model by changing evaluation method and providing improved allocation strategies. Previously, our model take all the workforce as a whole which ignored the difference between subgroups’ priorities. To maximum global outcome, limited resources like education budget, childcare budget should be allocated wisely to where it is more needed. To simplify this strategy model, we consider two-subgroup two-resource situation. We add such assumptions:

<!-- b000382 | prose | pages [20] -->
• There are only two limited resources.

<!-- b000383 | prose | pages [20] -->
• There are only two subgroups.

<!-- b000384 | prose | pages [20] -->
• Resources like education opportunity and child care budget are limited.

<!-- b000385 | prose | pages [20] -->
min z = (Gp −Ga) + λ1 ∗(x1,1 −x2,1)2 + λ2 ∗(x1,2 −x2,2)2 (20)

<!-- b000386 | prose | pages [20] -->
s.t.

<!-- b000387 | prose | pages [20] -->
x1,1 + x1,2 ≤Re1 (21)

<!-- b000388 | prose | pages [20] -->
x2,1 + x2,2 ≤Re2 (22)

<!-- b000389 | prose | pages [20] -->
a1,1 ∗x1,1 + a1,2 ∗x2,1 + a2,1 ∗x1,2 + a2,2 ∗x2,2 = Ga (23)

<!-- b000390 | prose | pages [20] -->
where λ1 ≥0, λ2 ≥0 (24)

<!-- b000391 | prose | pages [20] -->
In the nonlinear programming formulation above, Gp is global outcome obtained previously, Ga is adjusted global outcome, Rei is i th resource concerning subgroup’s priority, xi,j is the amount of i th resource allocated to j th subgroup, λi is penalty coefﬁcient of i th resource allocation inequality. Inequa- tion (21)and(22) are resource constrains which mean that the sum of amount of resources allocated to each subgroup should be no more than present resources amount. λi ensures that the difference of resource allocated to each group should not be too large, or it will affect the value of objective function. The optimal solution (x1,1, x1,2, x2,1, x2,2) is the best resource allocation strategy.

<!-- b000392 | furniture | pages [21] -->
Team # 64486

<!-- b000393 | furniture | pages [21] -->
Page 20 of 33

<!-- b000394 | heading | pages [21] -->
8 Interpersonal Relationship Network And New Immigrants

<!-- b000395 | prose | pages [21] -->
In section 5.6.2, we have presented a family network of 40 citizen. In this section, we apply complex network theory to analyze the employment, marriage and parenthood relationship.

<!-- b000396 | heading | pages [21] -->
8.1 Generation Of Interpersonal Network

<!-- b000397 | prose | pages [21] -->
Based in the complex network theory, we generate a interpersonal network to study the impact of immi- grants. Social networks have the ”small world” property, which means one can ﬁnd a short path along the links between most pairs of nodes[15]. According to Watts and Strogatz(1998)[16], social networks dis- play a degree of clustering higher than expected for random networks. In our synthesized social network on Mars, the degree distribution contains important information about the nature of the network and its social representation. Many large networks follow a scale-free power-law distribution[17], which is also an important attribute of the network in our model.

<!-- b000398 | prose | pages [21] -->
We deﬁne the nodes in the network as the individuals of the population, and the edges as any kind of interpersonal relationship(employment, friendship and teacher-student relationship et cetera) except for marriage and parenthood. We will later combine this network with the family network we have constructed in section 5.6.2.

<!-- b000399 | prose | pages [21] -->
Indeed, the interpersonal network constantly expands by the addition of new immigrants to the database, as well as the addition of new internal links representing new linkages to Mars residents that are already part of the database. The topological properties of the network are determined by the dynamical and growth processes deﬁned by our assumptions. Fig.22 shows the connection of individual with ID number 1 to 24 in the 10th year of evolution.

<!-- b000400 | caption | pages [21] -->
Figure 23: Age distribution: The proportion of different

<!-- b000401 | prose | pages [21] -->
age groups has ”pulse”, because children under 16 are not included in Population Zero. There is a 16-year age

<!-- b000402 | caption | pages [21] -->
Figure 22: 24-people linkage graph

<!-- b000403 | prose | pages [21] -->
gap between the ﬁrst generation of Mars-born babies and the youngest immigrants of Population Zero.

<!-- b000404 | prose | pages [21] -->
Network Dynamics We assume that residents and immigrants of the same occupation and education level establish a immediate relationship. Edeges should also be added is an individual is linked to another individual’s mother and father at the same time.

<!-- b000405 | prose | pages [21] -->
We initialize the network with all the individuals in Population Zero with 0 edges. We link the individ- uals following the connection rules. Certain parameters that describe the network should be speciﬁed.

<!-- b000406 | furniture | pages [22] -->
Team # 64486

<!-- b000407 | furniture | pages [22] -->
Page 21 of 33

<!-- b000408 | prose | pages [22] -->
Linkage Graph Matrix The linkage matrix is   · · · f11 f12 f1n   ... ... ... ... G = (25)   · · · fn1 fn2 fnn

<!-- b000409 | prose | pages [22] -->
where fij is a 0-1 variable that record if there is a relationship between individual i and j, fii = 0.

<!-- b000410 | prose | pages [22] -->
ki is the degree of node i, Average Degree

<!-- b000411 | prose | pages [22] -->
N ∑ < k >= 1 ki (26) N i=1

<!-- b000412 | prose | pages [22] -->
Since individuals who are well-connected usually have a better access to information and resources, we assume that an individual with high degree is in good ﬁnancial condition, and an society with high average degree is wealthy.

<!-- b000413 | prose | pages [22] -->
We denote the connectivity of the graph as c(G), we assume that a link graph matrix with Connectivity higher degree represents a society with higher equality.

<!-- b000414 | heading | pages [22] -->
8.2 Stationary Increment Model And Impact Of Immmigration Waves

<!-- b000415 | prose | pages [22] -->
In this scenario, we assume that a group of 10000 immigrants are sent to Mars every 10 years, and no children under 16 are included in the group, for it is too dangerous to bring children on a space trip. This result in a discontinuous age distribution in Fig.23.

<!-- b000416 | prose | pages [22] -->
To alleviate retro-gradation tide effect, we sent immigrant from Earth to Mars every 16 years when the birth rate is low. We compare the distribution of node degree on the 10th, 100th year of evolution.

<!-- b000417 | heading | pages [22] -->
9 Migration Plan Analysis

<!-- b000418 | prose | pages [22] -->
As LIFE has planed additional migration phase over the next 100 years, it is important to study how population evolve after new migrants settled in Mars under different migrational plan.

<!-- b000419 | heading | pages [22] -->
9.1 Inﬂuences By Choosing Different Migration Year

<!-- b000420 | prose | pages [22] -->
Given a total number of migrants, if we want to optimize our plan on phases, we have to study how one group of migrants inﬂuence the evolving process. Speciﬁcally, we study the following plan: ten thousand migrants same as Population Zero migrate in year 10, 20, 30, 40, 50. We ﬁnd that migration plan of mi- grating in year 10, 30 have relative high population and GDP when combined society come to a stable state(Fig.24(a),(b)). This result show the signiﬁcance of immigrants of children at age 1-15. As afore- mentioned feature of PUMS database in Sec. 4.3.1, we ﬁnd that immigrants who are able to give birth to children have mostly impact on evolution. The reason is that those immigrants arriving at year 10 and 30 ﬁlling the blank of the age gap of Population Zero because they give another ”baby boomer generation” between the original age gap(Fig.24(c)).

<!-- b000421 | furniture | pages [23] -->
Team # 64486

<!-- b000422 | furniture | pages [23] -->
Page 22 of 33

<!-- b000423 | caption | pages [23] -->
Figure 24: Results of different migrantional plan.(a)Population diagram of Population Zero with ten thousands

<!-- b000424 | prose | pages [23] -->
migrants in year 10, 20, 30, 40 and 50; (b)GDP diagram of UTOPIA:2100 in year 10, 20, 30, 40 and 50;(c) Age distribution in year 50 of UTOPIA:2100 in comparison with no migration

<!-- b000425 | heading | pages [23] -->
9.2 Phased Over and One-Year Migration

<!-- b000426 | prose | pages [23] -->
Given a number of population to be moved, we generally have two options: to move phased over or to move in one year. Speciﬁcally, we mainly study following plan to move 50000 people to Mars:

<!-- b000427 | prose | pages [23] -->
• Option 1: Phased Over Move 10000 migrants every ten year to Population Zero with the ﬁrst group of migrants arrived in year 10 and the last in year 50

<!-- b000428 | prose | pages [23] -->
• Option 2: Move In One Year Move 50000 migrants in year 50.

<!-- b000429 | prose | pages [23] -->
Using the evolution model, we ﬁnd that option 1 is much better than option2 both on population and GDP in two hundred year range(Fig.25). There are two reasons. One is that option 1 shorten the gap ”baby boomer generation” and therefore reach to stable stage of population quicker as we discussed in Sec9.1. The other is that part of the migrants arrived in year 50 can hardly ﬁnd a job since the number of job offered is proportional to GDP last year.

<!-- b000430 | caption | pages [23] -->
Figure 25: Results of option 1 and option 2 to move 50000 migrants to UTOPIA:2100.(a)Population dia-

<!-- b000431 | prose | pages [23] -->
gram;(b)GDP diagram;(c) GDP per person diagram

<!-- b000432 | furniture | pages [24] -->
Team # 64486

<!-- b000433 | furniture | pages [24] -->
Page 23 of 33

<!-- b000434 | heading | pages [24] -->
10 Robustness Analysis

<!-- b000435 | prose | pages [24] -->
To testify the robustness of our model, we add noise to different initial values and calculate the mean and standard deviation of statistical outcomes[18]. Results are shown in the Tab.8.

<!-- b000436 | caption | pages [24] -->
Table 8: Result for robustness analysis at 1% random noise of initial value (mean and stardard value at year

<!-- b000437 | prose | pages [24] -->
50 of 30 independent runs); IP for initial population, MW for minimal wage, PLP for parental leave pay.Unbiased parameters: IP=10000; MW=5000; PLP=40000; Other parameters: retire age is 65; rate of natural unemployment is 5%; no migration from earth after year 0

<!-- b000438 | prose | pages [24] -->
GDP GDP per person Happiness Edu. level Final Population 1% noise mean std mean std mean std mean std mean std 1.38 ∗108 0.18 ∗108 3.58 ∗104 0.39 ∗104 4.98 ∗103 0.39 ∗103 0.745 0.134 15.3 0.4 Unbiased 1.35 ∗108 0.21 ∗108 3.46 ∗104 0.47 ∗104 4.97 ∗103 0.34 ∗103 0.715 0.115 15.4 0.6 IP 1.34 ∗108 0.25 ∗108 3.52 ∗104 0.52 ∗104 4.83 ∗103 0.41 ∗103 0.789 0.571 15.5 0.4 MW 1.37 ∗108 0.17 ∗108 3.52 ∗104 0.35 ∗103 5.03 ∗103 0.42 ∗103 0.715 0.059 15.3 0.4 PLP

<!-- b000439 | heading | pages [24] -->
11 Strengths and Weaknesses

<!-- b000440 | heading | pages [24] -->
11.1 Strengths

<!-- b000441 | prose | pages [24] -->
• We take a lot of basic and derived parameters into consideration and establish a comprehensive evaluation system which can reﬂect various aspects of a society. What’s more, AHP is implemented to build a metric.

<!-- b000442 | prose | pages [24] -->
• We extract parameters’ data we deﬁned as much as possible from PUMS database which makes our numerical results more reliable.

<!-- b000443 | prose | pages [24] -->
• Our system consists of job, marriage, child generation, education, salary, salvation and migration system. Therefore this model evolves like our real world.

<!-- b000444 | prose | pages [24] -->
• When we build our model, we intentionally make our model easy to adjust to further research re- quirements such as complex network research of epidemic or family tree analysis of genetic diseases, which enables this model to provide strategies for our home.

<!-- b000445 | heading | pages [24] -->
11.2 Weaknesses

<!-- b000446 | prose | pages [24] -->
• The values of some parameters are determined subjectively, since we can not ﬁnd related essays to refer. Those values may not be reasonable in reality, especially on Mars.

<!-- b000447 | prose | pages [24] -->
• The database used in our model are partly extracted from given websites and partly generated by computer. Therefore, some results of model may not be repeated on other databases, even though the database is quiet large already.

<!-- b000448 | prose | pages [24] -->
• In our job system, we ignore the job competition. This might be reasonable in short term but fail to model the unemployment situation in long run.

<!-- b000449 | furniture | pages [25] -->
Team # 64486

<!-- b000450 | furniture | pages [25] -->
Page 24 of 33

<!-- b000451 | heading | pages [25] -->
References

<!-- b000452 | references | pages [25] -->
[1] Public Use Microdata Sample (PUMS),census bureau of united states, http://www2.census.

<!-- b000453 | references | pages [25] -->
gov/programs-surveys/acs/data/pums/2015/1-Year/

<!-- b000454 | references | pages [25] -->
[2] U.S. Bureau of Economic Analysis, Personal Saving Rate [PSAVERT], retrieved from FRED, Federal

<!-- b000455 | references | pages [25] -->
Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/PSAVERT, January 23, 2017.

<!-- b000456 | references | pages [25] -->
[3] Huebler, Friedrich (14 June 2013). ”Education indicators in the HDI: Expected years of schooling

<!-- b000457 | references | pages [25] -->
and mean years of schooling”. UNESCO Institute for Statistics. Archived from the original on 2014-

<!-- b000458 | references | pages [25] -->
10-08.

<!-- b000459 | references | pages [25] -->
[4] Sen, Amartya (1977), On Economic Inequality (2nd ed.), Oxford: Oxford University Press

<!-- b000460 | references | pages [25] -->
[5] Social Science Research Network(SSRN)https://ssrn.com/en/

<!-- b000461 | references | pages [25] -->
[6] PUMS

<!-- b000462 | references | pages [25] -->
data

<!-- b000463 | references | pages [25] -->
dictionary

<!-- b000464 | references | pages [25] -->
http://www2.census.gov/programs-surveys/acs/tech_

<!-- b000465 | references | pages [25] -->
docs/pums/data_dict/PUMSDataDict15.pdf

<!-- b000466 | references | pages [25] -->
[7] Saaty, T.L. (2008) Decision making with the analytic hierarchy process, Int. J. Services Sciences, Vol.

<!-- b000467 | references | pages [25] -->
1, No. 1, pp.8398.

<!-- b000468 | references | pages [25] -->
[8] U.S. Census Bureau, Current Population Survey, Annual Social and Economic Supplements, 1955,

<!-- b000469 | references | pages [25] -->
1960, 1965 and 1970 to 2016

<!-- b000470 | references | pages [25] -->
[9] Blanchard O, Gal J. Labor markets and monetary policy: A New Keynesian model with unemploy-

<!-- b000471 | references | pages [25] -->
ment[J]. American economic journal: macroeconomics, 2010, 2(2): 1-30.

<!-- b000472 | references | pages [25] -->
[10] Maniquet F, Neumann D. For Online Publication Well-Being, Poverty and Labor Income Taxation:

<!-- b000473 | references | pages [25] -->
Theory and Application to Europe and the US[J]. 2016.

<!-- b000474 | references | pages [25] -->
[11] What is the Social Security Retirement Age? National Academy of Social Insurance

<!-- b000475 | references | pages [25] -->
Website

<!-- b000476 | references | pages [25] -->
[12] Eric A. Hanushek (2005). Economic outcomes and school quality. International Institute for Educa-

<!-- b000477 | references | pages [25] -->
tional Planning. ISBN 978-92-803-1279-9. Retrieved 21 October 2011.

<!-- b000478 | references | pages [25] -->
[13] Roelof J. van Kooij, Caspar W.N. Looman, Johannes D.F. Habbema, Marinus Dorland, Egbert R. te

<!-- b000479 | references | pages [25] -->
Velde, Age-dependent decrease in embryo implantation rate after in vitro fertilization, Fertility and

<!-- b000480 | references | pages [25] -->
Sterility, Volume 66, Issue 5, November 1996, Pages 769-775, ISSN 0015-0282,http://dx.doi.

<!-- b000481 | references | pages [25] -->
org/10.1016/S0015-0282(16)58634-8.

<!-- b000482 | references | pages [25] -->
[14] Deb, Kalyanmoy. Multi-Objective Optimization Using Evolutionary Algorithms. John Wiley Sons,

<!-- b000483 | references | pages [25] -->
2001.

<!-- b000484 | references | pages [25] -->
[15] Kleinberg J. The small-world phenomenon: An algorithmic perspective[C]Proceedings of the thirty-

<!-- b000485 | references | pages [25] -->
second annual ACM symposium on Theory of computing. ACM, 2000: 163-170.

<!-- b000486 | references | pages [25] -->
[16] Watts D J, Strogatz S H. Collective dynamics of small-worldnetworks[J]. nature, 1998, 393(6684):

<!-- b000487 | references | pages [25] -->
440-442.

<!-- b000488 | references | pages [25] -->
[17] Santos F C, Pacheco J M. Scale-free networks provide a unifying framework for the emergence of

<!-- b000489 | references | pages [25] -->
cooperation[J]. Physical Review Letters, 2005, 95(9): 098104.

<!-- b000490 | furniture | pages [26] -->
Team # 64486

<!-- b000491 | furniture | pages [26] -->
Page 25 of 33

<!-- b000492 | references | pages [26] -->
[18] Nissen, Volker, and Jrn Propach. ”On the robustness of population-based versus point-based optimiza-

<!-- b000493 | references | pages [26] -->
tion in the presence of noise.” IEEE Transactions on Evolutionary Computation 2.3 (1998): 107-119.

<!-- b000494 | furniture | pages [27] -->
Team # 64486

<!-- b000495 | furniture | pages [27] -->
Page 26 of 33

<!-- b000496 | references | pages [27] -->
A

<!-- b000497 | heading | pages [27] -->
Appendix

<!-- b000498 | prose | pages [27] -->
A.1

<!-- b000499 | heading | pages [27] -->
MATLAB Script Of Evolution Model

<!-- b000500 | prose | pages [27] -->
Notes:

<!-- b000501 | prose | pages [27] -->
• Due to the page limit and ﬁle limit, we can not provide every script of each simulation because they have slight differences to meet different task requirements. However, the codes of main part of our model stays the same. The following script is one version consists of all system described in our paper. Readers may modiﬁed few lines to get all the simulations mentioned in our paper.

<!-- b000502 | prose | pages [27] -->
• Because this model based on probability calculations in marriage decision and Death system, same input in this model may have different results. However, the mean value of many runs should not vary far from the simulation results presented on our paper.

<!-- b000503 | prose | pages [27, 28, 29, 30, 31, 32, 33, 34] -->
clear all; 1 close all; 2 clc; 3 tic 4 database=xlsread(’D:\mcmcode\database.xlsx’); 5 %----------------------------------------------- 6 %INITIALIZE constants 7 taxratio=0.15; 8 wage=5000; 9 parentincome=44000; 10 maxyear=50; 11 count=1; 12 rate_u=0.05;%rate of unemployment %probability of unemp.(regardless of edu) 13 age_retire=65; %retire age 14 rate_re=0.75; %rehire % probab. if rehire. 15 mig_times=0; 16 %----------------------------------------------- 17 %INITIALIZE DATA 18 19 [num_introw,num_intcol]=size(database); 20 for i=1:num_introw 21 %intitialize FOM 22 if database(i,8)>=2 23 database(i,17)=0; 24 else 25 database(i,17)=1; 26 end 27 %intialize FOD 28 if database(i,2)<=50 29 database(i,11)=0; 30 else 31 database(i,11)=1; 32 end 33 %initialize FOW 34 if database(i,2)<=18%age<18 35 database(i,14)=3;%3=child; 36 else 37 database(i,14)=1;%1= work 2=paretalleave 3=child 0 = unempol 38 end 39 %intialize FON need of marriage 1=in need 0 =no need 40 if database(i,2)>18 && database(i,2)<33 && database(i,17)==0 41 database(i,12)=1; 42 else 43 database(i,12)=0; 44 end 45 46 end 47 %inialize income 48 database(:,10)=database(:,5); 49 %----------------------------------------------- 50 %initial data stat 51 age_ave(1)=mean(database(:,2)); 52 age_std(1)=std(database(:,2)); 53 edu_ave(1)=mean(database(:,4)); 54 edu_std(1)=std(database(:,4)); 55 temp=0; 56 temp=find(database(:,3)==1); 57 [temp_row,temp_col]=size(temp); 58 num_male(1)=temp_row; 59 num_female(1)=num_introw-num_male(1); 60 61 temp=0; 62 temp=find(database(:,2)>18); 63 [temp_row,temp_col]=size(temp); 64 num_adult(1)=temp_row;% adult and alive 65 adult=database(temp(:,1),1);%id of adults 66 eco_tot(1)=sum(database(adult(:,1),5));%total production 67 eco_ave(1)=eco_tot(1)/num_adult(1); 68 eco_std(1)=std(database(adult(:,1),5)); 69 %sex_ratio(1)=num_male/num_female(1); 70 71 temp=0; 72 temp=find(database(:,5)<wage); 73 temp=temp(find(database(temp(:,1),14)˜=3),1);%not child 74 [temp_row,temp_col]=size(temp); 75 num_wage(1)=temp_row; 76 num_live(1)=num_introw; 77 num_dead(1)=0; 78 num_child(1)=0; 79 num_par(1)=0; 80 ndp(1)=eco_tot(1)-wage*num_wage(1)-parentincome*num_par(1); 81 82 age_matrix_ini=database(:,2); 83 age_x=1:1:100; 84 age_num_ini=hist(age_matrix_ini,age_x); 85 age_num_ini=age_num_ini/num_introw; 86 migrants=database; 87 migrants(1,25)=0; 88 89 %=============================================== 90 for t=2:maxyear 91 t; 92 %----------------------------------------------- 93 %find people alive 94 livepeople=find(database(:,11)<2); 95 [live_row,live_cow]=size(livepeople); 96 num_live(t)=live_row; 97 %----------------------------------------------- 98 %initilize num tracker 99 num_dead(t)=0; 100 num_un(t)=0; 101 num_re(t)=0;%re for rehire 102 num_tx(t)=0;%tx for tuixiu(retire) 103 num_child(t)=0; 104 num_par(t)=0; 105 % for people alive 106 %age+1 107 database(livepeople(:,1),2)=database(livepeople(:,1),2)+1; 108 %=============================================== 109 for i=1:live_row 110 id=livepeople(i,1); 111 %----------------------------------------------- 112 %renew FOD 113 if database(id,2)>50 114 database(id,11)=1; 115 end 116 %----------------------------------------------- 117 %death penalty 118 if database(id,11)==1; 119 temp_rand=rand(); 120 %dig=database(id,2); 121 temp_live=1/(1+exp(-0.3*(database(id,2)-75))); 122 if temp_rand<temp_live%then dead 123 database(id,11)=2; 124 num_dead(t)=num_dead(t)+1; 125 end 126 end 127 end 128 %=============================================== 129 %----------------------------------------------- 130 %find people still alive 131 stlivepeople=find(database(:,11)<2); 132 [stlive_row,stlive_cow]=size(stlivepeople); 133 num_live(t)=stlive_row; 134 %------------------------------------------------ 135 %=============================================== 136 % JOB experience 137 %----------------------------------------------- 138 for i=1:stlive_row 139 id=stlivepeople(i,1); 140 %----------------------------------------------- 141 %lose job naturally 142 if database(id,14)==1 143 temp_rand=rand; 144 if temp_rand<rate_u 145 database(id,14)=0; 146 num_un=num_un+1; 147 end 148 end 149 %gain job naturally 150 if (database(id,14)==0 && database(id,2)<=age_retire) 151 temp_rand=rand; 152 if temp_rand<rate_re 153 database(id,14)=1; 154 num_re=num_re+1; 155 end 156 end 157 %retire num_tx for the sake of avoiding duplicaton of variable’s 158 %name 159 if (database(id,2)>age_retire &&database(id,14)==1) 160 database(id,14)=0; 161 num_tx(t)=num_tx(t)+1; 162 end 163 %----------------------------------------------- 164 end 165 %=============================================== 166 %marrige and child generate 167 %----------------------------------------------- 168 %find target list 169 temp=0; 170 temp=find(database(:,12)==1); 171 malistmale=temp(find(database(temp(:,1),3)==1),1); 172 [temp_row,temp_col]=size(malistmale); 173 num_ls_male=temp_row; 174 175 temp=0; 176 temp=find(database(:,12)==1); 177 malistfemale=temp(find(database(temp(:,1),3)==2),1); 178 [temp_row,temp_col]=size(malistfemale); 179 num_ls_female=temp_row; 180 num_mar=min([num_ls_male,num_ls_female]); 181 if num_mar>0 182 %----------------------------------------------- 183 %distance calculation 184 mal_eco=database(malistmale(:,1),10); 185 fem_eco=database(malistfemale(:,1),10); 186 mal_age=database(malistmale(:,1),2); 187 fem_age=database(malistfemale(:,1),2); 188 for i=1:num_ls_male 189 for j=1:num_ls_female 190 distance(i,j)=sqrt((mal_eco(i)-fem_eco(j))ˆ2+(mal_age(i)-fem_age(j)) 191 ˆ2); end 192 end 193 distance=distance/(max(max(distance))); 194 for i=1:num_ls_male 195 for j=1:num_ls_female 196 mar_p(i,j)=1-distance(i,j); 197 end 198 end 199 %find partner 200 while max(max(mar_p))˜=0 201 [mar_row,mar_col]=find(mar_p==max(max(mar_p))); 202 temp_rand=rand(); 203 if temp_rand>mar_p(mar_row,mar_col) 204 %marrige 205 [temp_row,temp_col]=size(mar_row); 206 if temp_row>1 207 mar_row=mar_row(1); 208 mar_col=mar_col(1); 209 end 210 mar_p(mar_row,:)=0; 211 mar_p(:,mar_col)=0; 212 temp_rand=rand(); 213 if temp_rand<0.33%one child 214 childnum=1; 215 elseif (temp_rand>=0.33 &temp_rand<=0.66) 216 childnum=2; 217 else 218 childnum=3; 219 end 220 221 for child_index=1:childnum 222 %generate children 223 %generateid 224 %insident=1 225 [temp_row,temp_col]=size(database); 226 database(temp_row+1,1)=temp_row+1; 227 database(temp_row+1,2)=1; 228 229 %parents 230 database(temp_row+1,24)=malistmale(mar_row,1);%FATER id 231 database(temp_row+1,25)=malistfemale(mar_col,1);%mother id 232 %generate racial 233 temp_rand=rand(); 234 if temp_rand<=0.5 235 database(temp_row+1,7)=database(malistmale(mar_row,1),7); 236 else 237 database(temp_row+1,7)=database(malistfemale(mar_col,1),7); 238 end 239 %generate gender 240 temp_rand=rand(); 241 if temp_rand<=0.5 242 database(temp_row+1,3)=1; 243 else 244 database(temp_row+1,3)=2; 245 end 246 247 database(temp_row+1,11)=0;%FOD 248 database(temp_row+1,12)=0;%FON 249 database(temp_row+1,14)=3;%FOW 250 database(temp_row+1,17)=0;%FOM 251 %parents 252 database(malistmale(mar_row,1),17+child_index)=temp_row+1; 253 database(malistmale(mar_row,1),15)=malistfemale(mar_col,1);% 254 database(malistfemale(mar_col,1),17+child_index)=temp_row+1; 255 database(malistfemale(mar_col,1),15)=malistmale(mar_row);% 256 %stat 257 num_child(t)=num_child(t)+1; 258 end 259 database(malistmale(mar_row,1),12)=0;%FON 260 database(malistmale(mar_row,1),14)=2; 261 database(malistmale(mar_row,1),17)=1; 262 database(malistfemale(mar_col,1),12)=0;%FON 263 database(malistfemale(mar_col,1),14)=2; 264 database(malistfemale(mar_col,1),17)=1; 265 database(malistmale(mar_row,1),22)=childnum; 266 database(malistfemale(mar_col,1),22)=childnum; 267 num_par(t)=num_par(t)+2; 268 else %clear relation prob 269 mar_p(mar_row,mar_col)=0; 270 end 271 end 272 end 273 temp=0; 274 temp=find(database(stlivepeople(:,1),2)==33); 275 database(stlivepeople(temp(:,1),1),12)=0; 276 %=============================================== 277 %18 years old transition 278 %----------------------------------------------- 279 temp=0; 280 temp=find(database(stlivepeople(:,1),2)==18); 281 grow=stlivepeople(temp(:,1),1);%grow =citizen id 282 283 [temp_row,temp_col]=size(grow); 284 for i=1:temp_row 285 schl=floor(normrnd(21,3)); 286 if schl<1 287 schl=1; 288 end 289 if schl>24 290 schl=24; 291 end 292 % while (schl<1 || schl>24) 293 % schl=floor(normrnd(21,3)); 294 % end 295 database(grow(i,1),4)=schl;%schl for 18 296 database(grow(i,1),5)=normrnd(eco_ave(t-1),eco_std(t-1))*(1+(schl-18)/18);% 297 productivity%not considering age % if database(grow(i,1),5)<0 298 % databse(grow(i,1),) 299 % end 300 301 database(grow(i,1),12)=1;%fon 302 database(grow(i,1),14)=1;%fow 303 end 304 %=============================================== 305 %Income calculation *wage 306 [temp_row,temp_col]=size(stlivepeople); 307 for i=1:temp_row 308 if database(stlivepeople(i,1),5)<wage 309 database(stlivepeople(i,1),10)=wage; 310 else 311 database(stlivepeople(i,1),10)=database(stlivepeople(i,1),5); 312 end 313 if database(stlivepeople(i,1),14)==2 %parent leave situation 314 database(stlivepeople(i,1),10)=parentincome;%INCOME= PI 315 database(stlivepeople(i,1),14)=1;%FOW=1 (work) not parentleave any more 316 end 317 end 318 %----------------------------------------------- 319 %=============================================== 320 %datastat 321 322 age_ave(t)=mean(database(stlivepeople(:,1),2)); 323 age_std(t)=std(database(stlivepeople(:,1),2)); 324 325 edu_ave(t)=mean(database(stlivepeople(:,1),4)); 326 edu_std(t)=std(database(stlivepeople(:,1),4)); 327 328 temp=0; 329 temp=find(database(stlivepeople(:,1),3)==1); 330 [temp_row,temp_col]=size(temp); 331 num_male(t)=temp_row; 332 num_female(t)=num_live(t)-num_male(t); 333 334 temp=0; 335 temp=find(database(stlivepeople(:,1),2)>18); 336 [temp_row,temp_col]=size(temp); 337 num_adult(t)=temp_row; 338 339 adult=database(stlivepeople(temp(:,1),1)); 340 eco_tot(t)=sum(database(adult(:,1),5));%total production 341 eco_ave(t)=eco_tot(t)/num_adult(t); 342 eco_std(t)=std(database(adult(:,1),5)); 343 344 hap_ave(t)=mean(database(adult(:,1),4)./24*0.5+database(adult(:,1),22) 345 ./3*0.2+0.3*(abs(database(adult(:,1),5)-wage))./database(adult(:,1),5)); 346 sex_ratio(t)=num_male(t)/num_female(t); 347 348 temp=0; 349 temp=find(database(stlivepeople(:,1),5)<wage); 350 temp=temp(find(database(stlivepeople(temp(:,1),1),4)˜=3),1);%not child 351 [temp_row,temp_col]=size(temp); 352 num_wage(t)=temp_row; 353 ndp(t)=eco_tot(t)-wage*num_wage(t)-parentincome*num_par(t); 354 ratio_un(t)=num_un(t)/num_adult(t); 355 ratio_re(t)=num_re(t)/num_adult(t); 356 ratio_tx(t)=num_tx(t)/num_adult(t); 357 count=count+1; 358 if num_adult(t)<50 359 break; 360 end 361 %=============================================== 362 %migrataion system 363 if (mod(t,10)==1 && mig_times<5) 364 [temp_row,˜]=size(database); 365 k=1; 366 for i=temp_row+1:temp_row+500 367 database(i,1)=i; 368 369 for j=1:25 370 database(i,j)=migrants(k,j); 371 end 372 k=k+1; 373 374 end 375 mig_times=mig_times+1; 376 377 end 378 end 379 380 381 t=1:count; 382 num_un(1)=nan; 383 num_re(1)=nan; 384 num_tx(1)=nan; 385 hap_ave(1)=nan; 386 toc 387 subplot(4,2,1) 388 plot(t,num_live,’o-’);hold on; 389 plot(t,num_dead,’d-’);hold on; 390 plot(t,num_adult,’+-’);hold on; 391 plot(t,num_male,’*-’);hold on; 392 plot(t,num_female,’square-’);hold on; 393 plot(t,num_wage,’.-’) 394 h=legend(’AL’,’D’,’AD’,’M’,’F’,’W’); 395 set(h,’Fontsize’,6) 396 397 subplot(4,2,2) 398 plot(t,sex_ratio,’o-’); 399 subplot(4,2,3) 400 plot(t,ratio_un,’o-’);hold on; 401 plot(t,ratio_re,’d-’);hold on; 402 plot(t,ratio_tx,’+-’) 403 legend(’un’,’reh’,’ret’) 404 subplot(4,2,4) 405 plot(t,num_child,’o-’);hold on 406 subplot(4,2,5) 407 plot(t,eco_tot,’-’);hold on; 408 plot(t,ndp,’-’); 409 legend(’GDP’,’NDP’) 410 subplot(4,2,6) 411 plot(t,eco_ave,’-’); 412 subplot(4,2,7) 413 plot(t,hap_ave,’-’); 414 %age_hist 415 age_matrix=database(stlivepeople(:,1),2); 416 [temp_row,temp_col]=size(stlivepeople); 417 age_x=1:1:100; 418 age_num=hist(age_matrix,age_x); 419 age_num=age_num/temp_row; 420 bar([age_num_ini’,age_num’],’grouped’);hold on; 421 legend(’start’,’end’) 422 axis([0,100,0,(max(age_num)+0.05)]) 423 subplot(4,2,8) 424 plot(t,hap_ave,’-’); 425

<!-- b000504 | furniture | pages [28] -->
Team # 64486

<!-- b000505 | furniture | pages [28] -->
Page 27 of 33

<!-- b000507 | furniture | pages [29] -->
Team # 64486

<!-- b000508 | furniture | pages [29] -->
Page 28 of 33

<!-- b000510 | furniture | pages [30] -->
Team # 64486

<!-- b000511 | furniture | pages [30] -->
Page 29 of 33

<!-- b000513 | furniture | pages [31] -->
Team # 64486

<!-- b000514 | furniture | pages [31] -->
Page 30 of 33

<!-- b000516 | furniture | pages [32] -->
Team # 64486

<!-- b000517 | furniture | pages [32] -->
Page 31 of 33

<!-- b000519 | furniture | pages [33] -->
Team # 64486

<!-- b000520 | furniture | pages [33] -->
Page 32 of 33

<!-- b000522 | furniture | pages [34] -->
Team # 64486

<!-- b000523 | furniture | pages [34] -->
Page 33 of 33
