Summary

This paper presents a model to maximize both the economic output and job satisfaction for the workforce with sustainability in the scope. We build a self-adaptive system and deﬁne its dynamics. We run simula- tions of the system with real-world census data(PUMS 2015[1]) to ﬁnd out the optimal feasible solution. Based on the solution, we propose strategies to improve the living conditions of human immigrants on Mars. Our model has capabilities to deal with issues of population scalability, social development modality and evolution dynamics.

To address the problem of creating an optimal economic-workforce-education system, we decompose it into six sub-problems.

First, we constructed a parameter frame that integrates variables related to three aspects: income, edu- cation and social equality. We include basic parameters that exist in the census database, from which we derive metrics that reveal the characteristics of the society. Through an Analytical Hierarchy Process, we identify the critical parameters, among which the Happiness Index is an important comprehensive evaluation of citizens well-being.

Second, we formulate criteria to select 10000 immigrants for Population Zero. In comparison to the selected group, we generate a random sample by extracting data from PUMS 2015 database of 1,618,489 U.S. citizens. We study the demographics of both the selected group and the random sample. The selected group shows an obvious advantage in building a successful society.

Third, we construct a model to simulate the dynamic evolution of Population Zero. Consisting of vari- ous systems such as job, marriage, child generation, education, salary, salvation and migration system, this model evolves like our real world. We discuss one sample result in details using demographics, economics and Happiness Index.

In addition, we use this model to ﬁnd the equilibrium point between two contradictory goals of faster economic development and better social welfare. By implementing a Principle Component Analysis on the demographic data, we deﬁne the key elements of a successful society as high average family income, high minimum wage and low standard deviation of income. We solve the three-objective optimization problem by Elite Genetic Algorithm. We ﬁnd that the optimal minimum wage is $33526 per year, and the optimal parental leave pay is $50200 per year.

Next, we merge the models of income, education and social equality into a global model to and test it in different social groups. We identify the subgroups as professional labors and unskilled workers. The we build a non-linear programming model to decide the resources allocation strategy among different subgroups. We ﬁnd that maximizing the parental leave pay will not reduce the minimum wage and average income signiﬁcantly.

Finally, we study the effect of immigrant waves from the view of complex network theory. We generate a scale-free complex network with small world property to represent the interpersonal relationship among all individuals including Mars residents and new immigrants. Our model shows strategy of 10000 migrants every ten years are sustainable, and capable of dealing with a large number of refugees from Earth.

1 Policy Recommendation

Honored Director of LIFE, Thank you for hiring and trusting us. We have seen the great success of planned communities that are built across Earth. However, after detailed investigation and deliberate consideration, we ﬁnd that labor management and society plan of the existing experimental communities can be further optimized. Therefore, we feel obliged to recommend the optimal strategies to LIFE to ensure the successful launch of project UTOPIA:2100. Our recommendations are based on precise modeling and computer simulation based on real-world data, thus we are conﬁdent of our proposals.

We study the problem both on a micro and macro level. We consider 3 important balancing factors: economy, education, and equality in the vision of sustainability. We have run a 2000-year simulation and validated the robustness of our model. Here we suggest a series of strategies.

Select Educated Immigrants In terms of economic development, we propose that LIFE recruit more immigrants who own bachelor degree or higher, and increase the ratio of citizens under 40. Individual with strong innovation ability should be granted privilege in the selection procedure. Our model shows higher ratio of innovator and higher average education level contribute to faster growth of GDP.

Maximize Minimum Wage Higher minimum wage results in lower standard deviation of income but lower average income. Nevertheless, concerns about the negative effect of high minimum wage on GDP is unnecessary. Although average income decreases as the minimum wage grows, the change is negligible. The slight negative effect can also be compensated by recruiting skilled labor from Earth.

We deﬁne a Happiness Index to evaluation the citizens attitude toward life in Mars. Lower variance of family income leads to higher Happiness Index but lower Net Domestic Product. We balance the two factors and ﬁnd the equilibrium point, at which the minimum wage is around $31708 less than the average personal income. We recommend that minimum wage should be around $33526 and increase as economy grows.

Emphasize Education The signiﬁcance of education is ampliﬁed by its correlation with the economic development. Since higher education level leads to higher income and better education of the children, emphasis on education of Population Zero incurs a virtuous circle. If education of the ﬁrst generation is insufﬁcient, chain reaction will lead to a cascade and ﬁnally the downfall of Population Zero.

Increase Parental Leave Pay We suggest that LIFE offer parental leave to both fathers and mothers to maintain the equality and maximize the birthrate. Since population need to expand on Mars to created more active labor forces, encouraging birth giving by implementing high parental leave pay is beneﬁcial to the long term development on Mars.

Eliminate Discrimination In our complex network model, we ﬁnd that larger scale of population and closer relationship among individuals contribute to higher economic growth speed. Discrimination between local residents of Mars and new immigrants from Earth should be eliminated, since marriages between individuals of the two group is fundamental to the stability of population.

Robustness Of Our Model

We compare samples of Population Zero with randomly added noises on database. Results show the optimal strategies do not vary much.Since we do not consider the limitation of natural resources on Mars, our model may be less effective in modelling a large scale of population. Health care is not considered, which means additional models should be integrated to our simulation.

We hope that our suggestions are useful for LIFE and the UTOPIA:2100 will be a successful beginning of migration to Mars.

Sincerely, Team 64486

11 Strengths and Weaknesses

23 11.1 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23 11.2 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

2 Introduction

Background

In this year of 2095, a series of short-term planned living experiments have been completed on Mars. A group of 10000 people, called Population Zero, will migrate to Mars. Besides all the ad- vanced technologies that make life on Mars possible, an optimal strategy regarding workforce, economy and education should be designed to facilitate the development of Population Zero.

Restatement and Clariﬁcation Our team is bound to construct a policy model, which include a set of policy recommendations that will create a sustainable life-plan. To ﬁnd out the optimal strategies, we need to build models, run simulations and present the visualized results. Our model should be scalable, multi- tiered and dynamic. However, trade-offs should be made if two objectives contradict, and the 3 balancing factors are income, education and equality.

We aim to solve the following problems:

• Deﬁne a set of parameters and metrics and clarify their relations.

• Select a group of 10000 citizens as Population Zero and analyze the demographic characteristics.

Decide the selection criteria that make UTOPIA:2100 a well-functioning society.

• Deﬁne the key elements of a successful society in a 10-year period. Find out the equilibrium between the optimal minimum wage and salary distribution. Find out the optimal parental leave pay.

• Identify the major subgroups of your workforce, and identify their main priorities. Adjust our mod- els to balance the needs of different subgroups. Maximize the priority outcomes without sharply reducing the global outcomes.

• Build a sustainable Small World network model and deﬁne the dynamics of evolution. Analyze the impact of immigration phased over the next 100 years.

• Test the scalability of our network model. Consider a much larger population. Study the robustness of the model.

3 Parameter Deﬁnition And Speciﬁc Outcomes

3.1 PUMS Database

The American Community Survey (ACS) Public Use Microdata Sample (PUMS)[1] ﬁles are a set of 284 different untabulated records including population and housing unit records with individual information such as relationship, sex, educational attainment, and employment status, et cetera. It is convenient for people who are looking for accessibility to inexpensive data for research projects. However, there is a thing worth noting that PUMS does not contain information of people under 16 years old.

3.2 Three-tier Basic Parameter System

In order to quantify the characteristics of Population Zero, we clarify the fundamental parameters that would be applied in our models. The parameters are classiﬁed according to the objects they describe and the aspect of the outcomes they contribute to.

There are 3 tiers of parameters, which deliver quantitative information about Population Zero on indi- vidual level, family level and societal level respectively. In each tier, important factors related to income, education and equality are adopted as parameters. The Fig.1 below illustrates a clear structure of predomi- nate parameters whose detailed information is in Tab.1.

3.3 Derived Index System

To simplify the 3-tier basic parameter, we design a comprehensive index system to present a more de- tailed quantitative description of Population Zero and try to reveal the relation or dependency among the parameters.

3.3.1 Income Factor

From individual level, personal income, personal savings rate are most important parameters. The relation- ship between them are as follows, according to U.S. Bureau of Economic Analysis[2]

DPI = RPI ∗(1 −rtax) (1)

where RPI is real personal income(adjusted for inﬂation, but in our model equals to personal income), DPI is disposable personal income, rtax is tax rate.

rs = DPI −PCE (2) DPI

where PCE is personal consuption expenditure, rs is personal saving rate. rs < 0 indicates that his income can’t meet his expenditure thus in bad condition. If rs ≥0 and is low, then he is in good condition and there is no need for him to worry about future. If rs ≥0 and is high, then he is in good condition but has to worry about his future.

From household level, child care takes a large proportion of family expenditure.

rce = Fc (3) Fexp

where rce is childcare expenditures rate, Fc is average family childcare expenditure, Fexp is average family expenditure.

From societal level, GDP and NDP are most essential outcomes.

GDP = α ∗P ∗(1 −run) (4) where α is average workforce productivity which is related to working hours and creative activity involved in producing innovations, P is the total number of people, run is unemployment rate.

NDP = GDP −Wmin ∗Pmww −Bcc (5)

where Wminis minimum wage, Pmww is the number of minimum wage workers, Bcc is annual childcare budget.

3.3.2 Education Factor

Present education level(EDL) of a population can be calculate by following formulation[3]

EDL = (Yave,s + Yexp,s 18 ) ∗0.5 (6) 15

where Yave,s is “expected years of schooling” (Number of years a child of school entrance age can expect to spend in a given level of education) and “Mean years of schooling” (Average number of completed years of education of a population [25 years and older]).

3.3.3 Equality Factor

Given a continuous probability distribution function of income pin(x), where pin(x)dx is the fraction of the population with income x to x + dx, then the Gini coefﬁcient[4] is half of the relative mean absolute difference: ∫∞ ∫∞ Gse = 1 p(x)p(y) |x −y| dx dy (7) 2µ −∞ −∞ ∫∞ where µ is the mean of the distribution µ = −∞x p(x) dx and the lower limits of integration may be replaced by zero when all incomes are positive.

3.4 Evaluation Metrics

The frequency of words related to the topic “a well-being society” in the Social Science Research Network database[5] effectively reﬂects the importance of factors contributing to a successful society. According to the word frequency, we allocate different weights to the factors in our model. To better visualize the most concerned factors, we generated a word cloud as shown in Fig.2.

Name

Symbol

Type Tier Factor Dict[6] Unit ral Active Labor Force Ratio Numerical Societal Income A Age Numerical Individual Equality AGEP Year Fexp Annual Family Expenditure Numerical Family Income $ Hin Annual Family Income Numerical Family Income FINCP $ Aavg Average Age Numerical Societal Income Year Yave,s Average Educational Attainment Class Societal Education SCHL Bcc Childcare Budget Numerical Societal Equality $ DPI Disposable Personal Income Numerical Individual Income $ Meb Education Budget Numerical Societal Education $ EDL Education Development Level Numerical Societal Education Seth Ethnicity Class Individual Equality ACN1P rer Ethnicity Ratio Numerical Societal Equality Yexp,s Expected Years of Schooling Numerical Societal Education Fc Family Childcare Expenditure Numerical Family Equality $ Nfs Family Size Interger Family Income NPF Person Sft Family Type Class Family Income FES G Gender 0-1Variable Individual Equality SEX Gie Gini Coefﬁcient of Income Equality Numerical Societal Equality rcp Making Childcare Payment Rate Percent Family Equality Sms Marital status Class Individual Equality MAR Wmin Minimum Wage Numerical Societal Income $ Pmww Number of Minimum Wage Worker Interger Societal Income Person Soc Occupation Class Individual Income OCCP PLP Parental Leave Pay Numerical Societal Equality $ PCE Personal Consumption Expenditures Numerical Individual Income $ rs Personal Savings Rate Percent Individual Income P Population Integer Societal Income Person RPI Real Personal Income Numerical Individual Income PINCP $ rsr Sex Ratio Numerical Societal Equality rtax Tax Payment Percentage Percent Individual Income run Unemployment Rate Percent Societal Equality tw Weekly Working Hours Numerical Individual Income WKHP Hour

Through the Analytical Hierarchy Process(AHP), we deﬁne two sets of weights when calculating GDP Index and Happiness respectively. Starting from the ﬁrst criteria of the hierarchy ﬁgure(Fig.1), we structure comparison matrix by Comparison Method of 1-9[7]. Then, we get the weights of income factor, education factor and equality factor to Happiness Index, as is shown in Tab.2. By calculating the weights of three factors in hierarchy II, we get the maximum eigenvalue is 3.0044, consistency ratio CR = 0.0043, which meets AHP’s consistency ratio requirement.

Following the above procedures and adjusting comparison matrix until every matrix’s consistency ratio CR ≤0.1, we obtain two set of weights. Due to limitation of paper page, other pairwise comparison matrix is not appended. Finally, all the weights are shown in Tab.3 and Tab.4. They can used to evaluate GDP Index and Happiness Index of Population Zero.

Happiness Income Education Equality Weight Income 1 2 1/5 0.247 Education 1/2 1 1/6 0.202 Equality 5 6 1 0.550

Factor GDP Happiness Income 0.462 0.299 Education 0.373 0.259 Equality 0.165 0.442

Name GDP Happiness Factor Annual Family Expenditure 0.134 0.123 Income Annual Family Income 0.145 0.107 Income Minimum Wage 0.061 0.176 Income Number of Minimum Wage Worker 0.155 0.083 Income Personal Savings Rate 0.048 0.184 Income Real Personal Income 0.397 0.142 Income Weekly Working Hours 0.060 0.185 Income Education Budget 0.399 0.462 Education Education Development Level 0.601 0.538 Education Childcare Budget 0.133 0.131 Equality Ethnicity Ratio 0.129 0.173 Equality Family Childcare Expenditures Rate 0.144 0.141 Equality Gini Coefﬁcient of Income Equality 0.252 0.252 Equality Sex Ratio 0.127 0.214 Equality Unemployment Rate 0.215 0.089 Equality

4 Population Zero: PUMS Dempgraphics And Immigrants Selec-

tion

4.1 Random Sample Of 10000 People

To study the demographics of the potential Population Zero members, we extract data from PUMS database, which contains personal data of 1618489 individuals, and carry out data mining. Regarding the limitation of computational power, analyzing the whole data set is inconvenient and unnecessary. Instead, we ﬁrst generate a sample of 10000 immigrants totally randomly using SAS, SQL Server. We suppose that every individual has an equal opportunity to be selected as a member of Population Zero.

4.2 Selection Criteria And Algorithm

To build a peaceful, cooperative, egalitarian society of Utopia:2100, we select members of Population Zero under certain criteria. We believe that an ideal society should be balanced and harmonic, which can be speciﬁed as:

• We deﬁne innovators as individual under 40 and own bachelor degrees or higher. Since Population Zero will migrate to a new and undeveloped environment, innovation will be vital to help them adapt to the uncertainties and changeability in the Martian habitation. Innovators should outnumber producers. We set the innovator-to-producer ratio as 7:3.

• Building the Martian habitation need skilled labor. We deﬁne ”skilled labor” as individuals working for more than 35 hours per week. We have a strong preference for skilled labor when selecting members, therefore we set the skilled-to-unskilled labor ratio as 9:1.

• In order to maximize the birth rate, we set the male-female ratio as exactly 1:1.

• To ensure the stability of the society, we require citizens to migrate together with their spouses . Citizens will not be selected if their spouses are not eligible for Population Zero Program, and children should migrate with their parents.

• In consideration of equality, the selection process is based on a non-biased policy, i.e. other individual differences such as ethnicity, characteristics, and sexual orientation will not be considered.

Based on the criteria, we classify the candidates and tag them as 4 different types, and then select a partic- ular number of each type to join the Population One. The classiﬁcation procedure and the numbers of each type are speciﬁed in Fig.3.

After this procedure, we ﬁlter out those candidates whose spouses are not in the selected Population Zero and check if their spouses can take the place of another candidate. If not, the those candidates will be substituted.

4.3 Comparison Between Population Zero And The Random Sample

In order to validate our selection criteria, we compare the demographics of the random sample and Pop- ulation Zero. We ﬁnd that Population Zero’s advantages are apparent in regard to income, education and equality.

4.3.1 Demographic Distributions

As is show in Fig.4 and Fig.5, Population Zero has a higher average annual income and a lower standard deviation of 46844.11 dollars, compared to 52043.95 of the random sample. We believe that higher income and smaller income difference alleviate inequality and increase citizens’ happiness to an extend.

From Fig.6 and Fig.7, we can not tell a huge difference between the random sample and Population Zero. Since working hour per week centers near 40 hours/week, we ﬁnd this criterion unnecessary.

Population Zero have a higher average education level(shown in Fig.8 and Fig.9), since we have a strong preference for innovators, who own bachelor degrees or higher.

income income

working hour working hour

tion level tion level

In terms of age distribution, we believe a younger group have a stronger ability to innovate and repro- duce, which will be important for new Mars residents. Population Zero has an obvious advantage over the random sample. Besides, Sex ratio is adjusted to the optimal 1:1 to maximize birthrate.

We draw funnel charts and pyramid charts to analyze the if gender affects education level. We ﬁnd that male have higher degrees in general, and the selected Population Zero show less difference between male and female regarding education level, which makes marriage easier and improves equality.

5 Evolution Model and Dynamic System

As we have thoroughly discussed the methods and variables to describe the features of Population Zero, we need to know how these variables change with time. Therefore, a dynamic evolution model is required.

5.1 Model Structure and Overview Of Sample Results

Here we present the general algorithm and a sample result of one-hundred-year evolution shown in Fig.12. Our model starts with the Population Zero data and the evolution part provides the social environment for each person. This evolution model is close to reality because it simulates a lot of natural process including job, marriage, education, etc. Systems which describe aforementioned process is discussed in detail in Sec 4.3.1.

In the ﬁrst ﬁve years after Population Zero’s arrival on Mars, young and unmarried migrants give birth to children, which causes the “boomer generation I”(Fig.12(b),(g)) and the population grows. However, after the ﬁrst ten years, there is no newly born child, meanwhile part of migrants pass away. Therefore, the population and GDP decrease. The situation is generally getting worse in the ﬁrst sixty years(Fig.12(a),(e)) . After that, most migrants from Population Zero pass away and “baby boomer generation I” with its echo ”baby boomer generation II-III” reaches a relatively stable stage of population evolution(Fig.12(a),(g)). After approximately year 60, population and GDP started to rise with ﬂuctuation, according to our 200- year evolution simulation result.

Apart from the sample results shown in the Fig.12, our model provides statistical data on education, working hours and occupation distribution. In addition, this model enables us to keep track on the marriage relationship and father(mother)-child relationship which is helpful for future racial and genetic research.

5.2 Assumptions and Mathematical Expression For Each System

After our effective selection procedure, Population Zero are now prepared to construct a whole new city on Mars. We simulate their evolution by MATLAB programming, and test whether our selection criteria are truly beneﬁcial to their new life on Mars.

Our model and simulation are based on the following assumptions:

• Residents only die off naturally. Foods are sufﬁciently supplied and there is no diseases and natural catastrophe which causes death irregularly. The death probability as a logistic function of age is deﬁned as p = 1/(1 + exp (−0.15(x −70)))

• Every employed citizen has tax obligation. We set the unemployment rate at 5% according to the estimation method proposed by Blanchard et al(2010).[9]

• To ensure the well-being and equality of the society, we design a social security system, which requires the minimum annual wage to be $5000. Social relief fund is offered to non-labor individuals.

• In our ideal situation, wealth is redistributed more equitably among society. We set the tax rate at 0.15, which will be a reasonable number according to Maniquet and Neumann(2016)[10].

Database structure, algorithm and a sample result of the model.(a)population of certain kind of people each year(AL=alive,D=dead,AD=adult,M=male,F=female,W=people whose income under minimal wage); (b)sex ratio of male/female each year; (c)rate of unemployment(un), rehire(reh) and retire(ret) each year; (d)population of newly born children each year; (e)Gross Domestic Product(GDP) and Net Domestic Product(NDP) each year; (f)GDP per capita each year; (g)histogram of age distribution of Population Zero(start) and population after 100 years(end); (h) Average happiness index each year; All person’s information in Population Zero corre- sponds to a person in reality(Data source:[1]); Other parameters: minimal wage 5000$/year; Parental leave pay is 40000$/year;retirement age is 65; rate of natural unemployment is 5 %; NO migration from earth after year 0;

• Effective functioning of the society needs active labor force, retirement age is 65 in our simulation.

Referring to information provided by National Academy of Social Insurance[11], we believe it is reasonable.

• Parental leave is allowed. Parents who have newly-born children are granted a one-year leave with a subsidy of 40000 dollars.

Based on the assumptions and the notations system in Task 1, we present our algorithm and its math- ematical expression. We denote the ith individual as Pi. Every individual has 6 attributes: individual ID number IDi, education level Sed,i, sex Gi, age Ai, annual income Pri,i and marital status Sma,i. We deﬁne 6 vectors to store the information of the living individuals. It is worth noting that the length of the vectors changes after every iteration when the population changes, which we will elaborate in Sec 5.5.

5.3 Job System

A person’s job is his role in society. Most people spend up to forty or more hours each week in paid em- ployment. Some exceptions are non-labor force population including children (under 18), retirees (above 65), and people with disabilities. Labor population is comprised of unemployed (with a rate rre of ﬁnding a job again) and employed (with a rate run of losing job) workforce. Unskilled (with a rate rdis to become disabled) and professional are deﬁned by their age and education and working hours. The type of job of each employee and income is determined by his education level and age. Speciﬁcally, income is determined )×(1.5−|A−35 by the following function I = rtex×Norm(NDPPmean, NDPPσ)×(1+ SCHL−18 100 ) where 18 NDPPmean and NDPPσ are mean value and standard deviation of productivity last year. This function is modiﬁed if some of the parameters are irrelevant in order to run this complex simulation program quicker on our personal computer.

5.4 Education System

It has been argued that high rates of education are essential for countries to be able to achieve high levels of economic growth[12]. Therefore, we grant everyone in our model equal access to education opportunities no matter they are rich or pool, no matter they are male or female. However, where they are going to end their education depends on their personal experience. And we use normal distribution to describe his probability to ﬁnish education at different stages. The normal distribution is determined by mean value and standard deviation of EDL(SCHL) last year.

5.5 Marriage System

It is widely quoted that “love is a chemical reaction”. In our system, we stipulate that the closer two individuals of opposite sexes are, the more likely the “chemical reaction” will occur, and they will found a marriage relationship. We deﬁne the distance between two individual as √ (Ai −Aj)2 + (Pri,i −Pri,j)2 dij = (8)

We generate an adjacent matrix to record the distance between every 2 individuals and initialize a path matrix to record marriage relationships. Suppose there are m males and n females in Population Zero. When a marriage occurs betweeen Pi and Pj, the element pij in matrix P will become 1. We deﬁne the marriage probability between a male adult and a female adult as

Prmar,ij = 1 −dij (9) dmax

We ﬁrst ﬁnd out the 2 individuals Pi and Pj with the highest possibility to get married, turn pij in matrix P to 1 and let Prmar,iq = 0 and Prmar,pj = 0,where 0 ≤m and 0 ≤n. In the next iteration, the repeat the same steps. Under this marriage mechanism, we simulate the process with MATLAB and our code is attached in the Appendix. We input a sample of 10000 selected members of Population Zero, and we get the result after 100 iterations, which are interpreted as a 100-year evolution.

To have a clear view of marriage and parenthood relationship among citizens, we present an a visual- ization of family network of 40 citizens(Fig.13). Citizen ID are shown as the number in circle. Apparently, marriage linkages are far more sparse than parent hood linkages. It might be caused by our evolution mechanism: in our model, one marriage may generate more than 2 babies.

5.6 New Individuals: Child born And Migration System

New population come from 2 sources: newly born children of residents on Mars and new immigrant from Earth. We discuss their mechanism respectively.

5.6.1 Newly Born Children

Once marriage relationship is established between 2 individuals[8], the couple are granted the right to give births to children. Every couple expect to have 2 children throughout their life. The couple are able to bidirectional arrows represent mar- moves to a stabilization. riages and the grey directional arrows show the parenthood.

give birth if and only if both of the husband and the wife are between 19 and 40 years old. Every couple has 20-year child-bearing period and expect to have 2 children in total, thus they have a probability of 0.1 to give birth to a baby every year. In further consideration, pregnancy will be more dangerous if the wife is above 35. According to van Kooij et al(1996)[13], pregnancy rate is age-dependent. We adjust the pregnancy probability according to the wife’s age. The new probability density function of age Ai is

f(A) = −1.875 × 10−4A2 −6.14 × 10−3A (10)

f(A) satisﬁes ∫40 f(A)dA = 1 20 ∫40 Af(A)dA = 2 20

Newly born children are designated a citizen ID simultaneously, attributes are added according to the following rules:

• A baby has a 50% probability to be male or female.

• Child’s ethnicity is the same as his/her father.

• Children under 18 have NULL value in attributes of income, marital status and education level. Once they turn 19, they are allocated a random value of the attributes in a certain probability, which is dependent on their parent’s attributes.

5.6.2 Migration System

New immigrants from Earth have their original attribute, and they may contribute to the diversity of the population on Mars. Meanwhile, they may also increase the burden on the welfare system.

Marriage relationship may be established between a new immigrant and a member of Population Zero or a Mars-born adult. The marriage linkages are built based on the same rules as stated above. New immigrants are allowed to get married to a Mars resident right after they arrive on Mars, no time lag is considered.

6 Trade-offs And Social Equilibrium

We have built models of evolution and relationship network in the previous sections. By inputting different parameters into the model and simulation, we obtain varied outcomes, which provide vital information for deciding the optimal strategies of economics, education, and governance policies on Mars.

6.1 Additional Assumptions And Constraints

Our model is capable of simulating more than 2000 years of Population Zero’s evolution, which we have validated. Nonetheless, adjustments of constraints and parameters should be made every 10 years to ensure the population’s healthy development.

Since the population is self-adaptive, changes of parameters may be caused by internal factors or ex- ternal manipulation. In our analysis, we divide the impact factors into 2 categories: endogenous and exogenous inﬂuences.

• Residents on Mars are not allowed to return to Earth.

• When the population on Mars is below 1000, a group of 10000 immigrants from Earth must be sent to Mars.

• If the number of newly born children is below 60, parental leave pay will be raised by 20% and the pregnancy probability will be raised by 10%.

6.2 Policy For Balance Between Minimum Wage And High Productivity

Instead of searching for the global optimum, we aim to ﬁnd out the local optimum of the minimum wage near $25000 per year, which is almost half of the average annual income. The minimum wage must be lower than the average annual income and within a reasonable range, thus global optimization of the minimum wage is unnecessary.

We input different value of minimum wages and ﬁnd that it is negatively correlative with the Net Domestic Product, as is shown in Fig.15 .

Through the Analytical Hierarchy Process in Section3.4, we ﬁnd that the standard deviation of personal income has the greatest inﬂuence on the Happiness Index. We deﬁne the optimal minimum wage and salary distribution that minimize the standard deviation of personal income. For simplicity, we take family as the vital unit. In our model, “family” is deﬁned as a couple with or without children under 18. Based on our previous simulation, we count the number of families.

Consider the Mars city of families which has been divided into 5 economic brackets: class A, B, C, D, and E according to their economic condition. The annual income of each class according to the following distribution: Each year families move among the 5 classes with certain probability, the class transition chart

Class A B C D E Wmin Income($) 35000 60000 85000 160000 Proportion 5% 20% 45% 25% 10% Cumulative Proportion 5% 25% 70% 75% 100%

below speciﬁes the process: λ1 ration of Class A families transit to Class B, et cetera.

The NDP-minimum wage

curve from the 7th to 10th year of evolu- tion

Suppose that the transition state is stable, i.e. the proportion of each class is constant (denoted as the Class capital letter), we have

λ1A = µ4B (11) λ1A + µ3C = (λ2 + µ4)B (12) λ2A + µ2C = (λ3 + µ3)C (13) λ3A + µ1C = (λ4 + µ2)C (14) λ4A = µ1B (15)

Our objective is to increase the minimum wage and average income, but decrease the standard deviation. Denote the family income of Class k as xk and the proportion of each Class as nk respectively, we have the objective function

5 ∑ maxZ1 = xknk (16) k=1 v u 5 ∑ u t (xk −AV G)2nk minZ2 = (17) k=1 maxZ3 = Wmin (18)

The calculation of nk is also speciﬁed in Tab.6 The problem of ﬁnding the equilibrium point between high quality of life and optimal minimum wage is deducted to a multi-objective optimization. Using a controlled elitist genetic algorithm[14], we ﬁnd out the optimal solution, Fig.17 gives detailed information about all the feasible solutions after 50 iterations. And the optimal feasible solution is (Z1, Z2, Z3) = (65234, 9848, 33526)

6.3 Best Childcare And Parental Leave Strategy

We are interested in deciding the optimal parental leave pay. We continue to use the model in section 6.2 to carry out the computational optimization. We assume that parental leave pay will be given to both the mother and father. Therefore, we add an additional class P to represent families that are in a parental leave status and receive a ﬁxed parental leave pay. The State Transition Chart should be altered, as is shown in A Class Wmin Income($) n1 = 5% −5%λ1 + 20%µ4 Adjusted Proportion B Class Income($) 35000 n2 = 20% −20%(λ2 + µ4) + 5%λ1 −45%µ3 Adjusted Proportion C Class Income($) 60000 n3 = 45% −45%(λ3 + µ3) + 20%λ2 −25%µ2 Adjusted Proportion D Class Income($) 85000 n4 = 25% −25%(λ4 + µ2) + 5%λ3 −45%µ1 Adjusted Proportion E Class Income($) 160000 n5 = 10% + 25%4 −10%µ1 Adjusted Proportion

respectively.

Furthermore, considering that higher parental leave pay Mpl may promote birth giving, we deﬁne p as the as a function of Mpl p = 1 πarctan(x −55000) + 0.5 (19)

The result is presented in Fig.19. We ﬁnd the interesting facts that

• Parental leave pay doesn’t affect average family income much. It can be explained that if wealthy family start a parental leave, families in lower class have more opportunity to move upward since the standard deviation need to be minimized.

• Higher parental leave pay leads to lower minimum wage, since minimizing the standard deviation is also one of the objectives. Meanwhile, average income are maximized so the decrease in the minimum wage is not sharp.

• We ﬁnd the minimum of standard deviation $9806.001651, and the correspondent parental leave pay equal chance to transit to parental leave

minimum wage change by parental leave pay.

$50200 per person for both the father and mother. This provides important evidence for our parental leave strategy.

7 Model’s Function For Different Groups

7.1 Outcomes Across Different Subgroups

Our model function differently across age, education level. Fig20 shows that young people and old people are slight happier than middle age people. Because middle age people have to work and take care of their children and old parents. Fig21 shows that people with education level like a regular high school diploma are less happier. Because they have to unskilled work for longer hours but getting lower payment. Therefore, we ﬁnd that our model function much more different across age and education.

7.2 Major Subgroup Identiﬁcation

There are a variety of way to categorize the workforce of a country. For example, workforce is can be divided into subcategories like professional and unskilled workforce, male and female workforce, agricul- tural and non-agricultural workforce. Since UTOPIA:2100 is an egalitarian society, there is no difference in productivity between male and female workforce in our model. Moreover, ﬁeld of workforce is not involved due to the simpliﬁcation of our model. Finally, our model function differently across age and edu- cation which are criteria to identify skilled workforce and unskilled workforce. Therefore, the predominate subgroups of workforce in our model are professional workforce, unskilled workforce and unemployed workforce.

Professional workforce is the specialized part of the labor force with advanced education and earns a large income.There is no need for them to worry about how to make a living. Hence, they require more time off and parental leave to enhance the sense of happiness.

Unskilled workforce is generally characterized by a lower educational attainment, such as a high school diploma and typically results in smaller wages. And their main priority is work hours, disability care, child care, and minimum wage.

Their priorities are shown in Tab.7 and

Symbol Description rdc Disability Care Budget Rate Nplo Paid Leave Off Days Per Year

7.3 Best Allocation Strategy

With the consideration of identiﬁed subgroups, we adjust our model by changing evaluation method and providing improved allocation strategies. Previously, our model take all the workforce as a whole which ignored the difference between subgroups’ priorities. To maximum global outcome, limited resources like education budget, childcare budget should be allocated wisely to where it is more needed. To simplify this strategy model, we consider two-subgroup two-resource situation. We add such assumptions:

• There are only two limited resources.

• There are only two subgroups.

• Resources like education opportunity and child care budget are limited.

min z = (Gp −Ga) + λ1 ∗(x1,1 −x2,1)2 + λ2 ∗(x1,2 −x2,2)2 (20)

s.t.

x1,1 + x1,2 ≤Re1 (21)

x2,1 + x2,2 ≤Re2 (22)

a1,1 ∗x1,1 + a1,2 ∗x2,1 + a2,1 ∗x1,2 + a2,2 ∗x2,2 = Ga (23)

where λ1 ≥0, λ2 ≥0 (24)

In the nonlinear programming formulation above, Gp is global outcome obtained previously, Ga is adjusted global outcome, Rei is i th resource concerning subgroup’s priority, xi,j is the amount of i th resource allocated to j th subgroup, λi is penalty coefﬁcient of i th resource allocation inequality. Inequa- tion (21)and(22) are resource constrains which mean that the sum of amount of resources allocated to each subgroup should be no more than present resources amount. λi ensures that the difference of resource allocated to each group should not be too large, or it will affect the value of objective function. The optimal solution (x1,1, x1,2, x2,1, x2,2) is the best resource allocation strategy.

8 Interpersonal Relationship Network And New Immigrants

In section 5.6.2, we have presented a family network of 40 citizen. In this section, we apply complex network theory to analyze the employment, marriage and parenthood relationship.

8.1 Generation Of Interpersonal Network

Based in the complex network theory, we generate a interpersonal network to study the impact of immi- grants. Social networks have the ”small world” property, which means one can ﬁnd a short path along the links between most pairs of nodes[15]. According to Watts and Strogatz(1998)[16], social networks dis- play a degree of clustering higher than expected for random networks. In our synthesized social network on Mars, the degree distribution contains important information about the nature of the network and its social representation. Many large networks follow a scale-free power-law distribution[17], which is also an important attribute of the network in our model.

We deﬁne the nodes in the network as the individuals of the population, and the edges as any kind of interpersonal relationship(employment, friendship and teacher-student relationship et cetera) except for marriage and parenthood. We will later combine this network with the family network we have constructed in section 5.6.2.

Indeed, the interpersonal network constantly expands by the addition of new immigrants to the database, as well as the addition of new internal links representing new linkages to Mars residents that are already part of the database. The topological properties of the network are determined by the dynamical and growth processes deﬁned by our assumptions. Fig.22 shows the connection of individual with ID number 1 to 24 in the 10th year of evolution.

age groups has ”pulse”, because children under 16 are not included in Population Zero. There is a 16-year age

gap between the ﬁrst generation of Mars-born babies and the youngest immigrants of Population Zero.

Network Dynamics We assume that residents and immigrants of the same occupation and education level establish a immediate relationship. Edeges should also be added is an individual is linked to another individual’s mother and father at the same time.

We initialize the network with all the individuals in Population Zero with 0 edges. We link the individ- uals following the connection rules. Certain parameters that describe the network should be speciﬁed.

Linkage Graph Matrix The linkage matrix is   · · · f11 f12 f1n   ... ... ... ... G = (25)   · · · fn1 fn2 fnn

where fij is a 0-1 variable that record if there is a relationship between individual i and j, fii = 0.

ki is the degree of node i, Average Degree

N ∑ < k >= 1 ki (26) N i=1

Since individuals who are well-connected usually have a better access to information and resources, we assume that an individual with high degree is in good ﬁnancial condition, and an society with high average degree is wealthy.

We denote the connectivity of the graph as c(G), we assume that a link graph matrix with Connectivity higher degree represents a society with higher equality.

8.2 Stationary Increment Model And Impact Of Immmigration Waves

In this scenario, we assume that a group of 10000 immigrants are sent to Mars every 10 years, and no children under 16 are included in the group, for it is too dangerous to bring children on a space trip. This result in a discontinuous age distribution in Fig.23.

To alleviate retro-gradation tide effect, we sent immigrant from Earth to Mars every 16 years when the birth rate is low. We compare the distribution of node degree on the 10th, 100th year of evolution.

9 Migration Plan Analysis

As LIFE has planed additional migration phase over the next 100 years, it is important to study how population evolve after new migrants settled in Mars under different migrational plan.

9.1 Inﬂuences By Choosing Different Migration Year

Given a total number of migrants, if we want to optimize our plan on phases, we have to study how one group of migrants inﬂuence the evolving process. Speciﬁcally, we study the following plan: ten thousand migrants same as Population Zero migrate in year 10, 20, 30, 40, 50. We ﬁnd that migration plan of mi- grating in year 10, 30 have relative high population and GDP when combined society come to a stable state(Fig.24(a),(b)). This result show the signiﬁcance of immigrants of children at age 1-15. As afore- mentioned feature of PUMS database in Sec. 4.3.1, we ﬁnd that immigrants who are able to give birth to children have mostly impact on evolution. The reason is that those immigrants arriving at year 10 and 30 ﬁlling the blank of the age gap of Population Zero because they give another ”baby boomer generation” between the original age gap(Fig.24(c)).

migrants in year 10, 20, 30, 40 and 50; (b)GDP diagram of UTOPIA:2100 in year 10, 20, 30, 40 and 50;(c) Age distribution in year 50 of UTOPIA:2100 in comparison with no migration

9.2 Phased Over and One-Year Migration

Given a number of population to be moved, we generally have two options: to move phased over or to move in one year. Speciﬁcally, we mainly study following plan to move 50000 people to Mars:

• Option 1: Phased Over Move 10000 migrants every ten year to Population Zero with the ﬁrst group of migrants arrived in year 10 and the last in year 50

• Option 2: Move In One Year Move 50000 migrants in year 50.

Using the evolution model, we ﬁnd that option 1 is much better than option2 both on population and GDP in two hundred year range(Fig.25). There are two reasons. One is that option 1 shorten the gap ”baby boomer generation” and therefore reach to stable stage of population quicker as we discussed in Sec9.1. The other is that part of the migrants arrived in year 50 can hardly ﬁnd a job since the number of job offered is proportional to GDP last year.

gram;(b)GDP diagram;(c) GDP per person diagram

10 Robustness Analysis

To testify the robustness of our model, we add noise to different initial values and calculate the mean and standard deviation of statistical outcomes[18]. Results are shown in the Tab.8.

50 of 30 independent runs); IP for initial population, MW for minimal wage, PLP for parental leave pay.Unbiased parameters: IP=10000; MW=5000; PLP=40000; Other parameters: retire age is 65; rate of natural unemployment is 5%; no migration from earth after year 0

GDP GDP per person Happiness Edu. level Final Population 1% noise mean std mean std mean std mean std mean std 1.38 ∗108 0.18 ∗108 3.58 ∗104 0.39 ∗104 4.98 ∗103 0.39 ∗103 0.745 0.134 15.3 0.4 Unbiased 1.35 ∗108 0.21 ∗108 3.46 ∗104 0.47 ∗104 4.97 ∗103 0.34 ∗103 0.715 0.115 15.4 0.6 IP 1.34 ∗108 0.25 ∗108 3.52 ∗104 0.52 ∗104 4.83 ∗103 0.41 ∗103 0.789 0.571 15.5 0.4 MW 1.37 ∗108 0.17 ∗108 3.52 ∗104 0.35 ∗103 5.03 ∗103 0.42 ∗103 0.715 0.059 15.3 0.4 PLP

11 Strengths and Weaknesses

11.1 Strengths

• We take a lot of basic and derived parameters into consideration and establish a comprehensive evaluation system which can reﬂect various aspects of a society. What’s more, AHP is implemented to build a metric.

• We extract parameters’ data we deﬁned as much as possible from PUMS database which makes our numerical results more reliable.

• Our system consists of job, marriage, child generation, education, salary, salvation and migration system. Therefore this model evolves like our real world.

• When we build our model, we intentionally make our model easy to adjust to further research re- quirements such as complex network research of epidemic or family tree analysis of genetic diseases, which enables this model to provide strategies for our home.

11.2 Weaknesses

• The values of some parameters are determined subjectively, since we can not ﬁnd related essays to refer. Those values may not be reasonable in reality, especially on Mars.

• The database used in our model are partly extracted from given websites and partly generated by computer. Therefore, some results of model may not be repeated on other databases, even though the database is quiet large already.

• In our job system, we ignore the job competition. This might be reasonable in short term but fail to model the unemployment situation in long run.

Appendix

A.1

MATLAB Script Of Evolution Model

Notes:

• Due to the page limit and ﬁle limit, we can not provide every script of each simulation because they have slight differences to meet different task requirements. However, the codes of main part of our model stays the same. The following script is one version consists of all system described in our paper. Readers may modiﬁed few lines to get all the simulations mentioned in our paper.

• Because this model based on probability calculations in marriage decision and Death system, same input in this model may have different results. However, the mean value of many runs should not vary far from the simulation results presented on our paper.

clear all; 1 close all; 2 clc; 3 tic 4 database=xlsread(’D:\mcmcode\database.xlsx’); 5 %----------------------------------------------- 6 %INITIALIZE constants 7 taxratio=0.15; 8 wage=5000; 9 parentincome=44000; 10 maxyear=50; 11 count=1; 12 rate_u=0.05;%rate of unemployment %probability of unemp.(regardless of edu) 13 age_retire=65; %retire age 14 rate_re=0.75; %rehire % probab. if rehire. 15 mig_times=0; 16 %----------------------------------------------- 17 %INITIALIZE DATA 18 19 [num_introw,num_intcol]=size(database); 20 for i=1:num_introw 21 %intitialize FOM 22 if database(i,8)>=2 23 database(i,17)=0; 24 else 25 database(i,17)=1; 26 end 27 %intialize FOD 28 if database(i,2)<=50 29 database(i,11)=0; 30 else 31 database(i,11)=1; 32 end 33 %initialize FOW 34 if database(i,2)<=18%age<18 35 database(i,14)=3;%3=child; 36 else 37 database(i,14)=1;%1= work 2=paretalleave 3=child 0 = unempol 38 end 39 %intialize FON need of marriage 1=in need 0 =no need 40 if database(i,2)>18 && database(i,2)<33 && database(i,17)==0 41 database(i,12)=1; 42 else 43 database(i,12)=0; 44 end 45 46 end 47 %inialize income 48 database(:,10)=database(:,5); 49 %----------------------------------------------- 50 %initial data stat 51 age_ave(1)=mean(database(:,2)); 52 age_std(1)=std(database(:,2)); 53 edu_ave(1)=mean(database(:,4)); 54 edu_std(1)=std(database(:,4)); 55 temp=0; 56 temp=find(database(:,3)==1); 57 [temp_row,temp_col]=size(temp); 58 num_male(1)=temp_row; 59 num_female(1)=num_introw-num_male(1); 60 61 temp=0; 62 temp=find(database(:,2)>18); 63 [temp_row,temp_col]=size(temp); 64 num_adult(1)=temp_row;% adult and alive 65 adult=database(temp(:,1),1);%id of adults 66 eco_tot(1)=sum(database(adult(:,1),5));%total production 67 eco_ave(1)=eco_tot(1)/num_adult(1); 68 eco_std(1)=std(database(adult(:,1),5)); 69 %sex_ratio(1)=num_male/num_female(1); 70 71 temp=0; 72 temp=find(database(:,5)<wage); 73 temp=temp(find(database(temp(:,1),14)˜=3),1);%not child 74 [temp_row,temp_col]=size(temp); 75 num_wage(1)=temp_row; 76 num_live(1)=num_introw; 77 num_dead(1)=0; 78 num_child(1)=0; 79 num_par(1)=0; 80 ndp(1)=eco_tot(1)-wage*num_wage(1)-parentincome*num_par(1); 81 82 age_matrix_ini=database(:,2); 83 age_x=1:1:100; 84 age_num_ini=hist(age_matrix_ini,age_x); 85 age_num_ini=age_num_ini/num_introw; 86 migrants=database; 87 migrants(1,25)=0; 88 89 %=============================================== 90 for t=2:maxyear 91 t; 92 %----------------------------------------------- 93 %find people alive 94 livepeople=find(database(:,11)<2); 95 [live_row,live_cow]=size(livepeople); 96 num_live(t)=live_row; 97 %----------------------------------------------- 98 %initilize num tracker 99 num_dead(t)=0; 100 num_un(t)=0; 101 num_re(t)=0;%re for rehire 102 num_tx(t)=0;%tx for tuixiu(retire) 103 num_child(t)=0; 104 num_par(t)=0; 105 % for people alive 106 %age+1 107 database(livepeople(:,1),2)=database(livepeople(:,1),2)+1; 108 %=============================================== 109 for i=1:live_row 110 id=livepeople(i,1); 111 %----------------------------------------------- 112 %renew FOD 113 if database(id,2)>50 114 database(id,11)=1; 115 end 116 %----------------------------------------------- 117 %death penalty 118 if database(id,11)==1; 119 temp_rand=rand(); 120 %dig=database(id,2); 121 temp_live=1/(1+exp(-0.3*(database(id,2)-75))); 122 if temp_rand<temp_live%then dead 123 database(id,11)=2; 124 num_dead(t)=num_dead(t)+1; 125 end 126 end 127 end 128 %=============================================== 129 %----------------------------------------------- 130 %find people still alive 131 stlivepeople=find(database(:,11)<2); 132 [stlive_row,stlive_cow]=size(stlivepeople); 133 num_live(t)=stlive_row; 134 %------------------------------------------------ 135 %=============================================== 136 % JOB experience 137 %----------------------------------------------- 138 for i=1:stlive_row 139 id=stlivepeople(i,1); 140 %----------------------------------------------- 141 %lose job naturally 142 if database(id,14)==1 143 temp_rand=rand; 144 if temp_rand<rate_u 145 database(id,14)=0; 146 num_un=num_un+1; 147 end 148 end 149 %gain job naturally 150 if (database(id,14)==0 && database(id,2)<=age_retire) 151 temp_rand=rand; 152 if temp_rand<rate_re 153 database(id,14)=1; 154 num_re=num_re+1; 155 end 156 end 157 %retire num_tx for the sake of avoiding duplicaton of variable’s 158 %name 159 if (database(id,2)>age_retire &&database(id,14)==1) 160 database(id,14)=0; 161 num_tx(t)=num_tx(t)+1; 162 end 163 %----------------------------------------------- 164 end 165 %=============================================== 166 %marrige and child generate 167 %----------------------------------------------- 168 %find target list 169 temp=0; 170 temp=find(database(:,12)==1); 171 malistmale=temp(find(database(temp(:,1),3)==1),1); 172 [temp_row,temp_col]=size(malistmale); 173 num_ls_male=temp_row; 174 175 temp=0; 176 temp=find(database(:,12)==1); 177 malistfemale=temp(find(database(temp(:,1),3)==2),1); 178 [temp_row,temp_col]=size(malistfemale); 179 num_ls_female=temp_row; 180 num_mar=min([num_ls_male,num_ls_female]); 181 if num_mar>0 182 %----------------------------------------------- 183 %distance calculation 184 mal_eco=database(malistmale(:,1),10); 185 fem_eco=database(malistfemale(:,1),10); 186 mal_age=database(malistmale(:,1),2); 187 fem_age=database(malistfemale(:,1),2); 188 for i=1:num_ls_male 189 for j=1:num_ls_female 190 distance(i,j)=sqrt((mal_eco(i)-fem_eco(j))ˆ2+(mal_age(i)-fem_age(j)) 191 ˆ2); end 192 end 193 distance=distance/(max(max(distance))); 194 for i=1:num_ls_male 195 for j=1:num_ls_female 196 mar_p(i,j)=1-distance(i,j); 197 end 198 end 199 %find partner 200 while max(max(mar_p))˜=0 201 [mar_row,mar_col]=find(mar_p==max(max(mar_p))); 202 temp_rand=rand(); 203 if temp_rand>mar_p(mar_row,mar_col) 204 %marrige 205 [temp_row,temp_col]=size(mar_row); 206 if temp_row>1 207 mar_row=mar_row(1); 208 mar_col=mar_col(1); 209 end 210 mar_p(mar_row,:)=0; 211 mar_p(:,mar_col)=0; 212 temp_rand=rand(); 213 if temp_rand<0.33%one child 214 childnum=1; 215 elseif (temp_rand>=0.33 &temp_rand<=0.66) 216 childnum=2; 217 else 218 childnum=3; 219 end 220 221 for child_index=1:childnum 222 %generate children 223 %generateid 224 %insident=1 225 [temp_row,temp_col]=size(database); 226 database(temp_row+1,1)=temp_row+1; 227 database(temp_row+1,2)=1; 228 229 %parents 230 database(temp_row+1,24)=malistmale(mar_row,1);%FATER id 231 database(temp_row+1,25)=malistfemale(mar_col,1);%mother id 232 %generate racial 233 temp_rand=rand(); 234 if temp_rand<=0.5 235 database(temp_row+1,7)=database(malistmale(mar_row,1),7); 236 else 237 database(temp_row+1,7)=database(malistfemale(mar_col,1),7); 238 end 239 %generate gender 240 temp_rand=rand(); 241 if temp_rand<=0.5 242 database(temp_row+1,3)=1; 243 else 244 database(temp_row+1,3)=2; 245 end 246 247 database(temp_row+1,11)=0;%FOD 248 database(temp_row+1,12)=0;%FON 249 database(temp_row+1,14)=3;%FOW 250 database(temp_row+1,17)=0;%FOM 251 %parents 252 database(malistmale(mar_row,1),17+child_index)=temp_row+1; 253 database(malistmale(mar_row,1),15)=malistfemale(mar_col,1);% 254 database(malistfemale(mar_col,1),17+child_index)=temp_row+1; 255 database(malistfemale(mar_col,1),15)=malistmale(mar_row);% 256 %stat 257 num_child(t)=num_child(t)+1; 258 end 259 database(malistmale(mar_row,1),12)=0;%FON 260 database(malistmale(mar_row,1),14)=2; 261 database(malistmale(mar_row,1),17)=1; 262 database(malistfemale(mar_col,1),12)=0;%FON 263 database(malistfemale(mar_col,1),14)=2; 264 database(malistfemale(mar_col,1),17)=1; 265 database(malistmale(mar_row,1),22)=childnum; 266 database(malistfemale(mar_col,1),22)=childnum; 267 num_par(t)=num_par(t)+2; 268 else %clear relation prob 269 mar_p(mar_row,mar_col)=0; 270 end 271 end 272 end 273 temp=0; 274 temp=find(database(stlivepeople(:,1),2)==33); 275 database(stlivepeople(temp(:,1),1),12)=0; 276 %=============================================== 277 %18 years old transition 278 %----------------------------------------------- 279 temp=0; 280 temp=find(database(stlivepeople(:,1),2)==18); 281 grow=stlivepeople(temp(:,1),1);%grow =citizen id 282 283 [temp_row,temp_col]=size(grow); 284 for i=1:temp_row 285 schl=floor(normrnd(21,3)); 286 if schl<1 287 schl=1; 288 end 289 if schl>24 290 schl=24; 291 end 292 % while (schl<1 || schl>24) 293 % schl=floor(normrnd(21,3)); 294 % end 295 database(grow(i,1),4)=schl;%schl for 18 296 database(grow(i,1),5)=normrnd(eco_ave(t-1),eco_std(t-1))*(1+(schl-18)/18);% 297 productivity%not considering age % if database(grow(i,1),5)<0 298 % databse(grow(i,1),) 299 % end 300 301 database(grow(i,1),12)=1;%fon 302 database(grow(i,1),14)=1;%fow 303 end 304 %=============================================== 305 %Income calculation *wage 306 [temp_row,temp_col]=size(stlivepeople); 307 for i=1:temp_row 308 if database(stlivepeople(i,1),5)<wage 309 database(stlivepeople(i,1),10)=wage; 310 else 311 database(stlivepeople(i,1),10)=database(stlivepeople(i,1),5); 312 end 313 if database(stlivepeople(i,1),14)==2 %parent leave situation 314 database(stlivepeople(i,1),10)=parentincome;%INCOME= PI 315 database(stlivepeople(i,1),14)=1;%FOW=1 (work) not parentleave any more 316 end 317 end 318 %----------------------------------------------- 319 %=============================================== 320 %datastat 321 322 age_ave(t)=mean(database(stlivepeople(:,1),2)); 323 age_std(t)=std(database(stlivepeople(:,1),2)); 324 325 edu_ave(t)=mean(database(stlivepeople(:,1),4)); 326 edu_std(t)=std(database(stlivepeople(:,1),4)); 327 328 temp=0; 329 temp=find(database(stlivepeople(:,1),3)==1); 330 [temp_row,temp_col]=size(temp); 331 num_male(t)=temp_row; 332 num_female(t)=num_live(t)-num_male(t); 333 334 temp=0; 335 temp=find(database(stlivepeople(:,1),2)>18); 336 [temp_row,temp_col]=size(temp); 337 num_adult(t)=temp_row; 338 339 adult=database(stlivepeople(temp(:,1),1)); 340 eco_tot(t)=sum(database(adult(:,1),5));%total production 341 eco_ave(t)=eco_tot(t)/num_adult(t); 342 eco_std(t)=std(database(adult(:,1),5)); 343 344 hap_ave(t)=mean(database(adult(:,1),4)./24*0.5+database(adult(:,1),22) 345 ./3*0.2+0.3*(abs(database(adult(:,1),5)-wage))./database(adult(:,1),5)); 346 sex_ratio(t)=num_male(t)/num_female(t); 347 348 temp=0; 349 temp=find(database(stlivepeople(:,1),5)<wage); 350 temp=temp(find(database(stlivepeople(temp(:,1),1),4)˜=3),1);%not child 351 [temp_row,temp_col]=size(temp); 352 num_wage(t)=temp_row; 353 ndp(t)=eco_tot(t)-wage*num_wage(t)-parentincome*num_par(t); 354 ratio_un(t)=num_un(t)/num_adult(t); 355 ratio_re(t)=num_re(t)/num_adult(t); 356 ratio_tx(t)=num_tx(t)/num_adult(t); 357 count=count+1; 358 if num_adult(t)<50 359 break; 360 end 361 %=============================================== 362 %migrataion system 363 if (mod(t,10)==1 && mig_times<5) 364 [temp_row,˜]=size(database); 365 k=1; 366 for i=temp_row+1:temp_row+500 367 database(i,1)=i; 368 369 for j=1:25 370 database(i,j)=migrants(k,j); 371 end 372 k=k+1; 373 374 end 375 mig_times=mig_times+1; 376 377 end 378 end 379 380 381 t=1:count; 382 num_un(1)=nan; 383 num_re(1)=nan; 384 num_tx(1)=nan; 385 hap_ave(1)=nan; 386 toc 387 subplot(4,2,1) 388 plot(t,num_live,’o-’);hold on; 389 plot(t,num_dead,’d-’);hold on; 390 plot(t,num_adult,’+-’);hold on; 391 plot(t,num_male,’*-’);hold on; 392 plot(t,num_female,’square-’);hold on; 393 plot(t,num_wage,’.-’) 394 h=legend(’AL’,’D’,’AD’,’M’,’F’,’W’); 395 set(h,’Fontsize’,6) 396 397 subplot(4,2,2) 398 plot(t,sex_ratio,’o-’); 399 subplot(4,2,3) 400 plot(t,ratio_un,’o-’);hold on; 401 plot(t,ratio_re,’d-’);hold on; 402 plot(t,ratio_tx,’+-’) 403 legend(’un’,’reh’,’ret’) 404 subplot(4,2,4) 405 plot(t,num_child,’o-’);hold on 406 subplot(4,2,5) 407 plot(t,eco_tot,’-’);hold on; 408 plot(t,ndp,’-’); 409 legend(’GDP’,’NDP’) 410 subplot(4,2,6) 411 plot(t,eco_ave,’-’); 412 subplot(4,2,7) 413 plot(t,hap_ave,’-’); 414 %age_hist 415 age_matrix=database(stlivepeople(:,1),2); 416 [temp_row,temp_col]=size(stlivepeople); 417 age_x=1:1:100; 418 age_num=hist(age_matrix,age_x); 419 age_num=age_num/temp_row; 420 bar([age_num_ini’,age_num’],’grouped’);hold on; 421 legend(’start’,’end’) 422 axis([0,100,0,(max(age_num)+0.05)]) 423 subplot(4,2,8) 424 plot(t,hap_ave,’-’); 425
