MCM/ICM

Summary Sheet

Summary

Research has identiﬁed a fact that several island countries are at risk of completely disappearing due to the raising sea level. This put the problem of relocating Environmentally Displaced Persons (EDPs) and protecting their unique culture forward for the international society.

To measure the severity of the problem, a circular cone model is built to simulate the world geography and two kinds of conditions are discussed: raising in a constant speed and in an accelerated speed. By 2050, the sea level will raise 0.16 m and about thirty million people will be affected directly. Eleven countries including Tuvalu, Maldives, Marshall, Tonga, Palau, Kiribati, Micronesia, Fiji, Bahamas and Gambia will sink and about ﬁve million people will be EDPs by then.

To ﬁnd the countries who are in responsibility for the terrible disaster, we built the site selection and moving model based on the game theory. We built the responsibility index with three chosen fac- tors: population density, accumulative carbon emission and GDP. Finally, eight countries are selected to accept EDPs and other countries should share the duty to provide economical supports. We use game theory to simulate the negotiation between big powers in order to select the speciﬁc country who accepts the refugees. Considering the complexity of political conﬂicts, international pressure is deﬁned and it pushes the country change their action. Finally we give a schedule for international society which includes when and which country will submerge and who should accept the EDPs.

To show how the culture will evolve as locals and the EDPs are mixing, we use the non-linear ordinary differencial equation build National Culture Changing model and use the Lyapunov’s second method to solve it. We use the number of people who master the culture to measure the existence of culture and we use differential equation to describe the change of the number of people who master of the culture. In the model, two important factors that the possibility of marriage between two groups of people and the possibility of inheriting the culture of mixed-blood crowd are stressed. We separately calculate the range of two parameters that makes the culture protected best. Then we analysis ﬁve single policies and six combined policies and give the suggested policy: inhabit and education combined policy in the initial decades and scatter and powerful culture protection combined policy.

Finally, the models and results are tested. The circular cone model performs well under the present condition. In the National Culture Changing model, two parameters act well with the test and show well robustness, which ensure the efﬁciency of our work.

National culture changing model, combined policies, Lyapunov’s second method.

关注数学模型

1 Introduction

1.1 Background

Some low attitude countries will disappear due to the rising sea level in the near future, which will not only bring lots of environmentally displaced persons but also put their unique and valuable culture into a dangerous situation. Therefore, It’s necessary to relocate people and protect their culture.

The environmentally displaced persons (EDPs) need a new home, but what they need is not only a piece of land. The EDPs should have some human rights, and some scholars think the country that lost their land is still a country. Therefore, the policy that the accepting countries apply to them is also a problem.

1.2 Our works

In order to help the UN to relocate the EDPs and protect their culture, we have completed the following tasks:

• We use the circular cone to simulating the real geography of the submerged island and we assume the population density decreases linearly with altitude. Then we calculated the sea level in the future when the sea level rises at a constant speed and accelerated. We assume that if 30% population is inﬂuenced, the persons in the island should migrate so we predict the migration timetable.

• In order to determine where the EDPs should migrate, ﬁrst, we choose some candidate coun- tries. We build a comprehensive index to measure the responsibility and ability of a country and we choose eight candidate countries. Then we use the Game Theory to simulate the negotiation process, ﬁnally we predict four countries that will accept EDPs in the future 50 years, including Australia, Canada, The USA, Russian.

• We use the number of persons who get command of the culture to measure the decrease of the culture. We use a differential equation to describe the change of different kind of people and we get the numerical solution.

2 Assumptions of models

1. The population density on the island decreases linearly with the elevation. Most people live

in the plant, because the mountain is not suitable for farming and ﬁshing. In order to simplify the question, we can assume it decreases linearly.

2. The EDPs from a country should migrate to another country as a whole part instead of separately move to several countries. The number of EDPs from a country is just about several ten thousands, and some may be less. The country that accept them has the ability to accept a whole country. And it’s better to

3. It’s harmful for a country to accept EDPs or donate some money and suppliers if we only consider the economic factors. The government will spend money to offer them jobs, living space and some social welfare, and the coming of the EDPs may cause the discontent of the local people. 关注数学模型 4. The policy to the problem of EDPs will be inﬂuenced by the pressure from other countries.

The problem of EDPs is a worldwide problem, if a country refuse to contribute to solve the problem, other countries will give him some of the sanction.

5. If the EDPs move to another country, they should join another country and have the nationality of another country, at the same time, they will have the same rights with citizens of another country. If the country of the EDPs still exists, it’s hard for another country to accept them. If some EDPs aren’t willing to change their nationality, they can negotiate with another country before they have to migrate, the UN only gives them a guaranteed option.

3 Notations and signs

declaired or deﬁned when using.

Symbols Unit Description

H m Altitude of land L m Length of generatrix h m Raised height of sea level P or p - Population in a country m·a−1 v The speed of raising sea level m·a−2 a The acceleration of raising sea level R - Responsibility index w - The weight of speciﬁc factor X - The result vector of game theory XE - The expectation of the solution XD - The difference between reality and expectation Pt - the international pressure FH - favor or hate index between two country

4 Countries at risk model

4.1 The way of simulating a island country

4.1.1 Simulation of the world geography

There are almost two hundred countries in the world but some of them will never be effected by the raising sea level in two hundred years because they are inland countries. So here we select countries with coastline as research objects.

In this problem, we need to consider two major aspects: how much the land will be submerged and how many people will be affected. The ﬁrst question is directly relating to the geography of the country. But the real terrain and coastline of a country are too rough. So we need to ﬁnd a way to simplify the geography. Here we select two major character to simulating the real geography:

关注数学模型 elevation and national territorial area. the simplest but most useful geometry is circular cone. See the following ﬁgure 1 to get more details

In the ﬁgure 1, H means the average altitude of the country and S means the national territory area of it. These two parameters are given by the real world. Other parameters that play an important role for the following model can be inferred from the given data by elementary geometry and elementary calculus:

v  q t−H2 + u H4 + 4S2  u  π2  R =    2    v  L = S 2 (1) u u q π t −H2 + H2 + 4S2    π2    A = R     L

The equations (1) above show how to infer the basic parameters of a circular cone. Now we get the point on simulating the nature geography environment.

4.1.2 Simulation of the distribution of people

A parameter ρ which means the population density is introduced. The simplest idea is assuming population are uniform distribution. But it gives an obvious error because people always live in the cities that the density is far away from uniform distribution. Fortunately, we ﬁnd a group of data that describing how many people are living in the land under ﬁve meters’ sea level in the database of World Bank. So we use this data to correct the density. See the distribution in the Figure 2.

Firstly we assume the linear relation between ρ and l:

ρ = kl (2)

The equation (2) means the out layer of the sector shares more density which means we assum- ing more population are distributing on the bottom of the country and less people are living in the mountains. This is much more close than uniform distribution. And then we calculate the ρ under the condition of Linear Distribution:

Z L Z L 3PA 0 Ak ·2πl2 dl = 2 3AkπL3 = PA ⇒k = 0 A·2πlρ dl = (3) 关注数学模型 2AπL3 Following the equation (3), we can get the coefﬁcient k to describe the linear relation. But this also can be improved by the data that describing how many people are living in the land under ﬁve meters’ sea level. We can solve it similarly that

2Pp k = (4) 2Aπ(3DL2 +D3 −3LD2)

In the equation (4), Pp means the population living in the land under ﬁve meters’ sea level. Using the equation, we obtain the corrected linear relation of population in the circular cone.

4.2 The timetable of countries sunk

4.2.1 The speed of sea level rising

As we all know, some nations may disappear slowly, while other nations may be wiped out in a catastrophic disaster such as tsunami. But it’s too hard to predict when the sudden disaster will happen, so we use probability of disaster happening to describe when the people should migrate. We use the number of persons who is inﬂuenced by the rising sea level to measure the probability of disaster happening. So, by this way, we turn an uncertain problem into a deﬁnite problem.

The raising sea level is deﬁnitely the directly cause of the risks. Now we have measures to simulate the geography, we need to know how the sea level is raising, and then we can give the direct answer to the questions that when the territory will be submerged and how many people will be affected.

According to the research conducted by the former people, we get to know the basic description of the question. The sea level is raising at the speed of 1.3−1.9 mm·a−1 since the twentieth century. The trend is accelerating when the world stepped into the 1990s. The speed is about 3.1 mm·a−1. In the latest research, The latest speed is 3.8 mm·a−1. And we will use the speed to measure the raising of sea level. So use a character here:

v0 = 3.8 mm·a−1

However, we notice a fact that the trend is accelerating: the value of speed is 2.72 mm·a−1 in 2002, but in 2014 the value is about 3.83 mm·a−1. Within twelve years the speed has added a half, so we couldn’t ignore the accelerating trend. So we assume that the accelerating trend is described by a which means the accelerating speed. The value can be acquired by the equation:

a = v2014 −v2002 2014−2002 = 0.0925 mm·a−2 ≈0.01 mm·a−1 (5) 关注数学模型 Now we can describe the raising sea level. as the years go, the sea level will raising the following height: hy = v0y+ a 2y2 (6)

In the equation (6), y means the added year since 2020, hy means the raised height of sea level. But we need an extra transfer, to make the height map the d in the sector:

hy H = dy L ⇒dy = hyL (7) H

Using the equation (7) to transfer the height to submerged area in the sector.

4.2.2 The result of sea level rising

Combing the simulation of geography and the model of raising sea level, we can answer the two question: when and how severe the risk is. We show the link between the two models in the following ﬁgure 3.

The meanings in the ﬁgure 3 is as followings: the sea level at present is the bottom of the circular cone. With the sea level raising, the sea will submerge the circular cone and the layer will also sink into the ocean. The submerged area represents the sink territory. Then we spread the surface, and use equation (4) to calculate the population who are suffering.

Before we point out which country will be at risk, we do the work on the world to ﬁgure out how severely the problem will be.

First we assuming every country will take no more attention to the raising sea level and the sea level will raise with accelerate speed. The outcome are showed in the following table 2.

Sink territory (km2) Year (since 2020) Raised Sea Level(m) inﬂuenced people 63,183/0.05%1 2050 0.16 26,566,782/0.31% 2100 0.62 247,864/0.22% 104,179,229/1.21% 2170 1.70 672,668/0.58% 282,468,896/3.30% 2220 2.76 1,094,319/0.95% 459,111,711/5.37%

There are a few conclusions summarized from the table 2. First, With the accelerating speed, the sea level will raise rapidly and will reach 2.76m in 2220. By then, about 460 million people will be 关注数学模型 1The form a/b is value/percentage. The same rule in next table.

inﬂuenced directly and several billion people will be inﬂuenced indirectly with reasonable inference. Second, within about one hundred years, about 2% population will lose their homeland and it may affect about 10% people in the world and cause international problem. So the raising sea level really present big problem for the whole world.

But the inference is somehow unreal because countries will do something to stop the awful trend. If major countries, such as American, China and Russia, are aware of the seriousness of the problem, they will take measures to stop the sea level raising so rapid. To show this condition ,we recalculate the result under the condition of a constant speed.

Sink territory (km2) Year (since 2020) Raised Sea Level(m) inﬂuenced people

2050 0.11 45,303/0.04% 19,046,347/0.22% 2100 0.304 120,787/0.11% 50,781,761/0.59% 2170 0.57 226,425/0.20% 95,172,506/1.11% 2220 0.76 301,851/0.26% 126,855,452/1.48%

In the table 3, we can know that even if the sea level is raising at a constant speed, by 2220 there will be 127 million people will lose place to live and about one billion people will be inﬂuenced. So on the level of world, sea level raising is really a big problem that may destroy the whole modern society.

For island countries such as Maldives, their homeland will be submerged within several years, and their population will transfer into EDPs. For them the problem is so disastrous that they will never overcome it without any support from the international world. To provide support, we need to illustrate when and which country will face the disaster. To ﬁgure out the solution, we calculate all of the countries in the world and ﬁnd eleven countries are at risk within 200 years with constant raising speed. They are Tuvalu, Maldives, Tonga, Marshall, Samoa, Palau, Kiribati, Micronesia, Fiji, Bahamas, Gambia. Put them in a world map and we can get the ﬁgure 4.

In the ﬁgure 4, we can get the conclusion that most of them are island countries in the middle of major oceans. To give the international world a much more detailed time schedule, we list the pre- dicted time for these eleven countries with four standards which based on the inﬂuenced population.

with constant raising speed. Here we give four standard to judge whether the country is at risk:

关注数学模型 2standard: the percentage of directly inﬂuenced population in the country country 100% 80% 50% 30% country 100% 80% 50% 30%

Tuvalu 2054 2047 2037 2030 Kiribati 2158 2128 2085 2058 Maldives 2094 2078 2055 2041 Micronesia 2161 2130 2086 2059 Tonga 2098 2081 2057 2042 Fiji 2207 2166 2108 2071 Marshall 2123 2100 2069 2049 Bahamas no risk no risk 2193 2122 Samoa 2142 2115 2077 2054 Gambia no risk no risk 2194 2123 Palau 2153 2124 2083 2057

1. 30% people are affected means the problem is severe enough that the government must start to act to ﬁnd support in the international society.

2. The line of 50% means the citizens should start to leave their homeland because the original land couldn’t support all of the citizens.

3. 80% means ﬁnal year for the country to remove all the citizens from the homeland to other countries.

4. 100% means the country lose all their land and the nation has disappeared. The country is disappeared in the meanings of geography. The government becomes an Exile government.

The international society should judge whether they could still be called nations.

5 Site selection of refugees moving model

5.1 Countries in responsibility

All eleven countries are suffering from the sea level, and all of their citizens become EDPs. Ac- cording to the research about the raising sea level, the major reason is global warming caused by greenhouse gases. Since industry revolution in 18th century, countries around the world is exhausting gases by using fossil fuels. And most of them become developed countries who shares most GDP in the world. But the consequence caused by them is making small island countries in Paciﬁc disappear. So all the countries who pollute the earth environment should take the responsibility to support the countries at risk.

To ﬁnd out which countries are in the most responsibility, we build the Responsibility Index Rcountry to describe the fact. We include three major factors:

1. Accumulative carbon emission of a country since 18th is used to measure the direct responsi- bility in causing the raising sea level.

2. Total GDP in a year of a country is included to show the international morality and justice.

Because the developed country should concentrate more on the global affairs to build the world a better one.

3. Population density of a country. This measures the objective condition for a country to accept refugees. If a country have too much citizens, they won’t have extra resources to support added people, and this also create difﬁculty in preserving the unique culture of EDPs.

关注数学模型 To build the Responsibility Index, we use the equation below:

Rcountry = wcarbon ·CB∗+WGDP ·GDP∗+WPD ·PD∗ (8)

In equation 8, w means the weight distributed among three factors. CB∗means the carbon emis- sion of a country. GDP∗means the gross domestic product, and PD∗means the population density of a country. All three factors in the equation should be normalized to remove dimension and create comparability. Also they are transferred into maximum type index.

We use the index to calculate the responsibility of each country. How they deal with the EDPs problem should be discussed now. There are two basic ways to help refugees: supply economic aids or accept refugees. The way to accept EDPs is relating to many international law problems, we will discuss in the following part but not here. Here we just assume that one country need to accept refugees from one sink country. As for supplying economic support, we think it is a 0-1 variable that we’ll not discuss the speciﬁc number. But a fact that we need to notice is not all country can accept refugees for various reasons, such as tiny territory, weak economic power or small number of original citizens. So here we spread countries into two group — Group A countries are countries that can provide economic and accept refugees; Group B countries are countries that only provide economic support.

Then we calculate Rcountry for almost 200 countries. Here we make wcarbon = 0.5, wGDP = 0.3 and WPD = 0.2 and do the rank in the table 5.

Rcountry Rcountry Country Country

The United States 0.99123124 Canada 0.276076 China 0.67102307 French 0.258283 Japan 0.31580978 Brazil 0.256073 Russian 0.30011196 Australia 0.249246

All eight countries above are selected into the group A country for they have the direct responsi- bility to deal with international problems. The following countries that share less responsibility are spread into Group B countries.

Rcountry Rcountry Rcountry Country Country Country

Germany 0.24279395 South Africa 0.225945 Argentina 0.215719 The British 0.23614349 Iran 0.223709 Poland 0.214322 Mexico 0.23563659 Spain 0.223441 India 0.213933 Saudi Arabia 0.23044163 Italy 0.221203 The Swedish 0.210407

Up to now we have illustrated three things: how severe the problem is, which countries are at risk and which country need to take the responsibility to deal with the EDPs. But the refugee problem is so complex that we need discuss the deﬁnition in law of EDPs and we couldn’t solve it with simple optimization model.

5.2 The basic attitude towards EDPs

According to the research conducted by international law experts, a country without territory 关注数学模型 couldn’t be called modern national country. So, if a humane country is willing to donate them a piece of land to help them rebuild the modern national country, they are not refugees. But if not, they should be deﬁned as refugees and the international society should treat them fairly.

Out of the concern of international morality, the great power should provide them with an option that ensures the basic human right for the refugees. But this option couldn’t ensure the existence of the original country or government. Because EDP refugees have no choice, there must be a country who accept them permanent. To ensure them with human right, they should be the citizens of the new country. At the same time, a small island country has little population and a big country have the ability to accept them as a whole. This also give beneﬁts to protect their culture. Also, relocating is a costly work, every country should provide economic supports.

Now we obtain the basic attitude to EDPs:

1. The international society will provide EDPs with the last choice if they don’t ﬁnd the humane country;

2. The last choice should ensure the basic right for EDPs but not nation or government. All the refugees should be the new citizens of the new country and be governed by the country. EDPs from one country should be accept as a whole for beneﬁts of protecting culture.

3. Countries in the world should provide economic support to EDPs.

5.3 Game of great power

After illustrating the basic points about EDPs, we have to discuss the pairing question: which big country will accept which disappearing country. Take a glance at the refugee problem of Syria and we know accepting refugees isn’t optimization among international society but is the game among great powers. They will negotiate for years to decide who take the duty. So here using the game theory ﬁts the problem better.

In this problem, the selected eight countries are players and we use i (i = 1,2...8) to represent them, and we rank it by table 5 in the last section. They should do the decision on whether accept refugees and whether provide large quantity of economic supports. So decision domain includes four solutions:

xi = (xi1,xi2) ∈{(0,0),(0,1),(1,0),(1,1)} (9)

In this equation, xi means the decision vector of the country, and the decision is a 0-1 type variable. xi1 represents accept refugees and xi2 represents providing economical supports. One country has four basic solutions. We can easily give the priority sequence among four solutions out of the concern of national interest:

xi = (0,0) →xi = (0,1) →xi = (1,0) →xi = (1,1) (10)

This rank show that a country will protect their own interest and avoid doing more in this problem. If they have to change their solution, they will improve the solution gradually. But if a country shares the smallest and negative pressure, he can improve the solution backwards to meet his interest. Then for all eight countries, we have the processing and result vector X:

x11  ··· x21 x81 X = (x1,x2,...,x8) = (11) ··· x12 x22 x81

There are in total 48 kinds of mathematical solution. Now we have to consider how to obtain feasi- ble solution. The solution space is so big that we couldn’t solve it with pure game theory mathematic 关注数学模型 method, so we introduce simulating theory into the game to decide the actions order of the country to ﬁnd the ﬁnal conclusion.

But the game may not make every country satisﬁed. If so, we have to set an end condition: at least one country have decided to accept the EDPs and all the other countries provide supplies. This can be deﬁned:

( ∑8 i=1 xi1 ≥1 ∑8 i=1 xi2 = 8

5.3.1 International pressure simulation

The simulation index we introduce is the international pressure. The reason we choose it is in- ternational pressure always is the ﬁnal factor to push a country act to face an international problem. The pressure in political can be produced in many ways such as censuring, economic sanctions or isolation policy. Here we deﬁne a matrix to show the international pressure:

Pt = [pi j]8×8

pi j is an index that measures how much pressure the country i gives to the country j which is inﬂuenced by many factors. And then we know the pressure that the county j bears is:

8 pj = ∑ pi j i=1

The country that bears most pressure will give in and act to change his solution xj by the priority sequence.

5.3.2 Game rules

The problem turns into how we give the speciﬁc value to international pressure matrix X. This should be reasonable to ensure the ﬁnal solution is reasonable. Here we give some quantitatively described game rules to give the speciﬁc value.

1. Higher rank means higher pressure. In the analysis of rcountry, they ate the cake of greenhouse gases emission, but the island countries eat the poison. So in this problem, biggest power should bear the biggest pressure. to make it quantitatively, we have:

8 8 |pi j| > |pi(j+1)| ∑ ∑ i=1 i=1

2. Bigger power can put more pressure on others. In international political games, the country

with more military force, gross domestic product or extreme government like North Korean will have more weight in negotiation. This is related to the strength of a country and it is objective.

At the same time, one country has limited inﬂuence on this issue so the pressure given by the biggest power have an upper limit and we make it is 8.0 here. So we can get:

( 8 ≥∑8 j=1 |p1j| ∑8 j=1 |pi j| ≥∑8 j=1 |p(i+1)j| 关注数学模型 3. The exact pressure value is decided by the difference between reality and expectation. We assume that each country has their own ideas about the best solution for the refugee problem.

To present it, we deﬁne result vector:

xe11  ··· xe21 xe81 XEi = (xe1,xe2,...,xe8)i = ··· xe12 xe22 xe82 i

In this equation, XEi represents the best solution that country i expects. xej means the detailed expectation for country j. The expectation may be different from the real condition represented by vector X. We use the vector to show it:

XDi = (xd1,...,xd8)i = {(xe11)i −x11 +2((xe12)i −x12),...,(xe81)i −x81 +2((xe82)i −x82)}

In the equation, XDi represents the difference between the real condition and expectation of coun- try i. xd j is the detailed difference of country j. Also every country don’t want to accepting EDPs, so it 2 times difference. Here we should pay special attention that the real condition may be better than the expectation. So xd could be a negative number. That means the country i will stand with country j and say words for him to prevent country j to do so much. And this means the negative international pressure.

However, the difference couldn’t decide the ﬁnal pressure and another two factor should be con- cluded. Firstly, xdi and pressure couldn’t linear relation. Bigger difference means much bigger pres- sure. Here we make the relation in cubic function. Another factor is that many countries have their own political favors or hates, so the coefﬁcient couldn’t be the same for the function. We deﬁne the coefﬁcient matrix: FH+ = [fh+ ( i j]8×i FH−= [fh− i j]8×i

In the equation, fhij means the coefﬁcient for the cubic function. The meanings in reality means the relations between two countries. If country i and country j are in good relation, they will share i j and larger fh− smaller fh+ ij. If their relation is bad, the consequence of fh will be a reversal. Also, fh should be a positive number. Now we can get the exact international pressure value that country i give to country j:

( fh+ i j(xdj)3 i , (xdj)i > 0 pij = fh− i j(xdj)3 i , (xdj)i < 0

So with the quantitative formula to calculate the pressure, we can summarize the ﬁnal gaming theory model as follows:

the ﬁnal results in the game. According to the model, at least one country will accept the EDPs and other countries will provide the economic supports. But the model have two parts that couldn’t be a quantitative factor: the judgement of expectation of one country and the relation between two countries. So the reasonable result should be built in the well judgment of international politics.

5.4 The solution and result of the game theory model

The game theory is a totally abstract one. To get the ﬁnal results, we need to do plenty of works. Here we select one circle to show how the model is running.

In the circle, we have the solution:

关注数学模型 X = {(1,0),(0,0),(0,0),(1,0),(0,0),(1,0),(1,0)(0,0)} This means America, Russia, France and Brazil are going to donate help to the disappearing country, but now no country is willing to accept the EDPs. so we have to run a circle now. This solution is totally different from the expectation of America:

XE1 = {(0,0),(1,1),(1,0),(1,1),(0,0),(1,0),(1,0),(0,1)}

America expects China and Russia provide economic support and provide candidate habitats for EDPs, but he doesn’t want himself and his alliances to do anything. And other countries should provide suppliers within their ability. So we can get:

XD1 = (−1,2,1,1,0,0,0,1)

The value means that America will put pressure on China, Japan, Russia and Australia. Combined with the pressure calculating formula, we can get the pressure given by America in this circle:

(p1)t = (−0.8,0.995,0.336,0.64,0,0,0,0.425)

This value means America is trying to tell the world that he should stop from providing assistance. But China and Russia should take the responsibility because they doesn’t full ﬁll their duty. As for Japan and Australia, they need step a little forward to meet the demand of America. Also, America will tell the world that Canada, French and Brazil have done the right thing.

We need to repeat this work for eight times to get the international pressure and ﬁnally we can get the result P = (−0.128,3.685,1.229,3.421,0.263,0.528,0.355,2.335)

In the pressure matrix, we can know that China are bearing biggest international pressure and he need to change his decision. After this circle game, we get the new solution matrix:

X = {(1,0),(1,0),(0,0),(1,0),(0,0),(1,0),(1,0)(0,0)}

The only difference is China agree to provide economic assistance due to the international pres- sure. Then we do the circle again and again till the solution reach the end condition. We record this progress.

In table 7 we can see the gaming between eight countries. At ﬁrst no country wants to do anything. But with the circle going on, we almost every country is going to donate. Then the gaming actually 关注数学模型 3D means Donating economic supports; A means accepting EDPs; blank means doing nothing.

Circle 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 D3 America D D D D D China D D D D D D D A A D D D Japan D D D D D D D D D D D Russia D D D D D D D D D D D D Canada D D D D D D D D D France D D D D D D D D D D D D D D D Brazil D D D D D D D D D D D D D D Australia D D A A A D D D A A

is playing between big powers: America, China and Russia. There is no possibility to make every country satisﬁed, so the game end in circle 16. The condition is Australia agree to accept EDPs, other seven countries agree to donate.

In the front part, we know eight countries are going to sink. So we run the model for ﬁve times and get the ﬁnal schedule for the EDPs in all ﬁve countries.

The sinking country The countries accepting the EDPs Year of the game

Tuvalu Australia 2030 Maldives America 2041 Tonga Canada 2042 Marshall China 2049 Samoa Russian 2054

6 The protection and inheritage of culture

In order to ﬁnd the best way to protect the culture from the sunk countries, we should ﬁnd the rule in national culture inheriting. There is three main ways in inheriting a kind of culture: inheriting with the development of the nation, spreading and being accepted by other peoples (especially the native people) and being recorded in literatures and books.

The ﬁrst way is the most common and easy way to inherit a culture, while the other two is remedial measures preparing for the worst situation which we should try our best to avoid. Therefore, we should analyse and predict the change of the people in the nation.

6.1 Change of people and culture

Once a island country sink and move to another country, we can consider it a new nation in the country it moves to. They will marry freely and raise their children, grandchildren and even further descendents, which mainly inherit the culture of the nation. We divide the people into three categories:

• The aborigines or assimilated immigrations who have few knowledge of culture of the immi- grant nation, marked A; 关注数学模型 • The immigrations who completely master knowledge of the immigrant nation, marked I;

• The mix-bloods or other amateurs who partly master and spread knowledge of the immigrant nation, marked M.

A country accepting refugees usually have more than 10 million people and usually accept no more than 100 thousand refugees. Therefore, we assume the number of A is far more than M or I in a long time.

Considering that both of parents will inﬂunce their children more or less (especially in their culture attribution), the kind of children is depended by parents in probabilities. The rule of six kind of family (A×A, A×B, A×C, B×B, B×C, C ×C) is shown as Table 9.

A M I Parents

(1−α)A+αM A A M (1−α)A+αM M M M I M M I

The α in this table is two constants in [0,1] dependent by nation relationship and policy.

Considering the relationship between the diffenent nations, for a people of M and I, the probablity to marry with A can be considered as a constant, marked p. In other situation, M and I will marry randomly and freely. We can use a differencial equation to describe the change of diffenent kind of people:

     dM M I pαM +(1−p) −kdM dt = kb 2(M +I) + + pI   M +I  dI I dt = kb(1−p) 2(M +I) −kdI   

Which kb and kd are birth and death rate which are two constants close to each other. Simplify this two equations and considering the starting value M(0) = 0, I(0) = I0, we can get the culture develop model:

  1−p dM I  dt = (kbpα −kd)M +kbpI +kb 1+   M +I 2    dI I (12) dt = −kdI +kb(1−p) 2(M +I)     M(0) = 0, I(0) = I0 

We need to solve the model and accept or reject them under the guide of the model.

6.2 The solution to the model

Model (12) is a starting value problem of a nonlinear differencial equation. In order to ﬁnd the possible situation of the equation, we solve it numerically in some spacial situations.

关注数学模型

6.2.1 The numerical solution in some special cases

Situation 1 We let kb = 0.0155, kd = 0.015, p = 0.9, α = 0.4. The result is shown in Figure 6(a). In this situation, p is very large but α is not so large. We can see from Figure 6(a) that the culture deciline quickly and ﬁnally get almost lost after 700 years. This is the situation that the nation completely integrate into the host nation and accept its culture in a very short time.

10000 10000 9000 9000 8000 8000 7000 7000 6000 6000 5000 5000 4000 4000 3000 3000 2000 2000 1000 1000 0 0 0 100 200 300 400 500 600 700 0 100 200 300 400 500 600 700

(a) Situation 2 (b) Situation 1

Situation 2 We let kb = 0.0155, kd = 0.015, p = 0.05, α = 0.8. The result is shown as Figure 6(b). In this situation, p is much smaller but α is larger. We can see from Figure 6(b) that the culture have a period of deciline and ﬁnally converge into a stable situation. This is the situation that the nation have their own society envionment and have a limit communication with the host nation.

6.2.2 The tendency analysis based on Lyapunov’s second method

The model itself is obviously impossible to solve the equation analytically. Therefore, we use the Lyapunov’s second method to analyze the tendency and stability of the solution to the equation. The differencial equation (12) has the only constant solution:

 M∗= (pk2 b +2k2 d)(1−p)    2k2 d −p(1−2α)k2  b pα(1−p)k2 b I∗=   2k2 d −p(1−2α)k2   b

Let the Lyapunov function f(M,I) = a(M −M∗)2 + b(I −I∗)2 + c(M −M∗)(I −I∗), then in the direction of the equation, we have

 (kbpα −kd)x+kpby+ kb(1−p)y  d f dt = ∂f dM dt + ∂f dI dt =(2ax+cy) ∂M ∂I 2(M +I)  −kdy−kb(1−p)x  +(2by+cx) 2(M +I)

关注数学模型 2kbp which x := M −M∗, y := I −I∗. Let a = b = 1, c = kbpα−2kd , we get x2 +y2 2k2 bp2 y2 −k2 bp(1−p)   d f dt = 2(kbpα −kd)x2 − 2kd − (13) kbpα −kd kbpα −2kd M +I

kb , we can get that d f When p < kd dt ≤0. Moreover,

∆f = c2 −4ab = 4k2 b(kb(p+ pα)−2kd)(kb(p−pα)+2kd) (14) (kbpα −2kd)2

then it’s obvious that ∆f ≤0 ⇐⇒α ≥2kd kbp −1.

kbp −1, there is f > 0 and d f Therefore, when p < kd kb and α ≥2kd dt ≤0 for all (M,I)̸ = (M∗,I∗). From the Luapunov’s theorem we can konw that the constant solution (M,I) ≡(M∗,I∗) is stable. Because (M∗,I∗) is in the ﬁrst quartile, the solution will converge into a positive point, which means that the culture development will go into a stable balance situation rather than disappear gradually.

In order to protect the immegrate culture and lead it into a stable balance, we should control p in a small number but let α as big as possible. Therefore, out policy need to decrease excessive communication between nations and increase the effect of the immigrate culture.

6.3 Politics design guided by the model

Now we have use mathematical method to obtain the conclusion that controlling parameter p and enlarging α makes the unique culture be protected well.

Here we list four different policies:

1. Strong culture protect policy. such as organizing associations relative, applying for intangible

cultural heritage for their culture and so on;

2. Receive local education policy. Require the refugees to receive the politics, culture education

systematically of the host country.

3. Encourage non-government communication policy. This means the government will give

less barrier for people to communicate with each other.

4. Inhabit policy.

This means that the government will spread a piece of land to settle the refugees.

5. Scatter policy. This means the refugees can move around the country and settle at anywhere they like.

According to the research conducted by socialist, we can list the change of p and α with different policies.

From the table 10 we know a fact that no policy is all-powerful. If we want to protect the culture well, we need to pay the price. Sometimes the cost is unacceptable. If we control the EDPs with in a limited area, we can surely protect the culture well but the international society may accuse the policy is another kind of discrimination. But if we make all the EDPs act as local people, it may arouse the wave of nationalism in the country and the local people will refuse the EDPs and totally destroy the culture which is gradually disappearing. So we need to push a series of policies to maximum the effect of protecting and minimum the cost.

关注数学模型 p Policy number Culture protection other inﬂuence α ↑ ↓ 1 Well Discrimination ↓ ↑ 2 Bad Nationalism ↑ 3 — Very Well Costly ↑ ↑ 4 Unknown Unknown ↓ 5 — Bad Better adapts to new environment

In the table 2, we can easily know that culture protection may arouse the nationalism in all condi- tion and may be costly. If the government encourage non-government communication between locals and EDPs, they could get along well with each other but the culture is at high risk disappearing. As for the local education, it can make EDPs adapt well and give a better chance for the government to take culture protect policy.

So take a conclusion, the best policies the local government takes should be:

1. The government should take inhabit policy when the EDPs going into their territory. At the same time, providing EDPs with local education till two kinds of people get along well with each other. This policy combination may last few decades.

2. Then take the policy combination of strong culture protection and scatter. Because two kinds of people are getting well with each other, so there is low risk in nationalism and discrimination.

7 Exhibition of results

Now we have done all the work about modeling and solving. Here we will answer all ﬁve ques- tions in the Problem.

According to our circular cone model and the prediction of sea level, the sea level will raise 0.16m and 63,183 km2 (0.05%) territory will sink. About 26,566,782 people (0.31% of all population) will be affected directly and more than one hundred million people will be inﬂuenced indirectly around the world. At the same time, eleven countries will disappear. They are Tuvalu, Maldives, Tonga, Marshall, Samoa, Palau, Kiribati, Micronesia, Fiji, Bahamas, Gambia (ranked by the sink time). About 4,680,563 people in total will be affected and Eleven kind of unique culture will be at risk.

According to analysis international laws, EDPs should be treated as refugees and be treated with all basic rights. But the government or the national country may not be last if no humane country is 关注数学模型 willing to accept the government. If no country accepts the EDPs, the international society should select a country to receive all refugees of a country as a whole. But all of them should be citizens of the new country but listen to the local government. Also, other countries who didn’t accept EDPs should provide economical supports.

To help the international society to select one, we use game theory and political simulating to ﬁnd the solution. And ﬁnally we get the schedule: Australia should accept Tuvalu in 2030; America should accept Maldives in 2041; Canada should accept Tonga in 2042; China should accept Marshall in 2049 and Russia should accept Samoa in 2054. Other countries who didn’t accept refugees should provide enough supports.

To answer the question 3 and 4, we build Nation culture changing model to describe the possible inﬂuence about the culture after the EDPs moves to new country. We use the population who know the culture well to describe the existence of one speciﬁc culture. In the model, we use p representing the probability to marry and α representing the probability of inheriting the culture of the mixed-blood crowd to be the major factors that inﬂuence the inherit condition. Then we use specialized mathematic method to ﬁnd the stable point of the model to ﬁnd the best value of solution. We get the point that p should be a small number but α should be big. Then we give ﬁve single policy that inﬂuence the two parameter to ﬁnd the possible consequence of the policy. To optimize the policy, we do research on policy combination and ﬁnally ﬁnd the best policy combination: in the initial decades, inhabit and education policy should be used, and scatter and strong culture protection policy should be used afterwards. On this way can ﬁnd the best condition that avoid the discrimination and nationalism, also receive well effect on culture protection.

If no country accepts the EDPs, one of the most merciless things will happen in the modern international society. If the country that receiving the EDPs take the wrong policy into use, they may face the problem of discrimination or nationalism. There also another possibility that cost a lot but receive no effect on protecting.

8 Sensitivity analysis

8.1 When the circular cone model be accurate

When we simulate the raise of the sea level, we list two conditions: raising at a constant speed of 3.8 mm·a−1 and raising with accelerate speed of 0.01 mm·a−2. Then we obtain the conclusion that the problem is really awful. Now we’ll research the sensitivity of the two parameters to perfect our discussion. Here we use algebraic expression to show the sensitivity.

In the part of calculating sink area, we have:

= πL2 2H   ∂S y −2v0 −ay   H2 ∂v0  (15) ∂2S = −2πL2   ∂v2 H2  0

We can conclude that the circular cone model has well robustness at the beginning of the year. In other words, higher value of v0 means less added sink area. it is the same for a. Also, if we use the population equation, it will be the same because there are more people living in the bottom.

So the model has limited work area: 1) at the initial time of the raising sea level; 2) relatively small raising speed. 3) can predict recent hundreds years well but will lose veracity after thousand years. In our solving part, the height of every country is well bigger than the raised level, so the 关注数学模型 solving part is reasonable.

8.2 The countries who have to accept refugees.

In the solving part of selecting humane countries, we make wcarbon = 0.5, wGDP = 0.3 and wPD = 0.2. But do these weight matter a lot? Here we change the weight to show the sensitivity.

In the ﬁgure 7 we can see that the value don’t vary much as the wcarbon is raising. And the rank didn’t change so much. This is to say, under our model, the ﬁnal selected country won’t change so much especially the big powers.

8.3 Sensitivity analysis of the protection and inheritage of culture model

In this model, we need to analyse the sensitivity of the model parameters p and α. We ﬁx one and move another, in order to observe the change of rate of converge.

Fix α = 0.4 and move p, the result of M is shown in Figure 8:

6000

5000

4000

3000

2000

1000

0 0 100 200 300 400 500 600 700

From the ﬁgure we can see that the change of converge rate and converge point is not sensitive with p when p is close to 1, but sensitive when p is close to 0.

Fix p = 0.05 and move α, the result is shown in Figure 9: 关注数学模型 6000

5000

4000

3000

2000

1000

0 0 100 200 300 400 500 600 700

From the ﬁgure we can know that not only the point and the rate of convergence is not sensitive with α changing.

9 Strengthes and Weaknesses

9.1 The strengthes of the model

1. Close to the reality. We consider the population density in the island and let the EDPs migrate when thirty percent persons are inﬂuenced, which conforms to the reality. And we use the Game Theory to simulate the negotiation process between several countries, which reﬂect the way that countries deal with international problems.

2. Practical to the culture protection. We measure the culture protection by people who get

command of it, which make the protection quantiﬁed. So, we can change the probability to marry EDPs and change the probability that the descendants get command of the culture to protect the culture.

3. Both responsibility and ability are token into consideration. When we choose the candidate countries to accept the EDPs, we give thought to the carbon emissions, population density and average GDP. It’s fair to set up burden-sharing based on nations’ relative contributions to the rising of sea level and it’s rational to ask the great power to take on more responsibility because the small countries cannot accept too many EDPs.

9.2 The weaknesses of the model

Although we try our best to improve our models, but there are still some weaknesses in our models. When we use the game theory to simulate the negotiation process, we cannot predict every country’s future action accurately, and when we make the policy to protect the culture, we cannot predict how much the policy will inﬂuence the possibility that the local people marry EDPs and the possibility that the descendants still get command of the culture, which make it difﬁcult to specify our policy.

关注数学模型
