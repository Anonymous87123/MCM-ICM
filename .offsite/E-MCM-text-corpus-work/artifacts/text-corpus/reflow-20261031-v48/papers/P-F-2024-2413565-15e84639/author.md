MCM/ICM

Summary Sheet

Technique Innovations Terminating Illegal Wildlife Trade

The illegal wildlife trade does serious harm to global biodiversity and the balance of ecosystems,

and we urgently need more people to get involved in stopping it. Finding suitable organizations and convincing them to participate is a great challenge.

Firstly, we constructed the client triangle profile model based on three dimensions (power, resources, and interests), encompassed three categories of related clients: governments, enterprises, and non-governmental organizations (NGOs). We established this model to get the scores of each client with many indicators summarized for each dimension and then used the Entropy Weight Method (EWM) to get the corresponding weights. Some indicators and the corresponding weights are listed for samples as follows: country law (0.8967), industry influence (0.2248), or media platform promotion (0.4349) in the power dimension; GDP (0.8789), technological advancements (0.1283), or volunteer network (0.6878) in the resources dimension; crime rate reduction and public security (0.2540), optimizing reputation (0.1368), or biodiversity conservation (0.7460) in the interests dimen- sion.

Secondly, we systematically evaluated the comprehensive scores of three different client categories

from bottom to top by utilizing the Analytic Hierarchy Process (AHP) respectively. Then we calculated all the different potential client scores from 265 countries, 157 enterprises, and 30 organizations, and chose the client with the highest score. The famous luxury company, LVMH group, with the normalized client triangle profile (0.44, 0.94, 0.24) achieves the most potential score of 0.4157, and it is surprisingly an enterprise, neither a government nor a NGO.

Thirdly, we established a win-win model, innovatively introducing new revenue indicators such as penalty revenues and eradication of transactions (replaceable materials). As in the case of Apple Inc., discontinuing the use of leather products and adopting new materials has yielded more gains. We assessed the benefits that the project brings to our client through aﬀine mapping analysis and estimated the additional profit value ($128.06 million) in a year for LVMH. We believe this project is ideally suitable for LVMH with its reputation for animal protection significantly enhanced.

Additionally, we’ve devised a complementary vector model to evaluate the extra capabilities needed by clients during project execution. The resulting complementary vector of our client LVMH is (0.56, 0.06, 0.76), then we used the maximum matching model to identify the Seychelles govern- ment with profile data (0.35, 0.03, 0.46) from our previously evaluated potential clients which have the closest (99.9%) complementary vector based on cosine similarity. Our client LVMH may need some resources such as an exclusive economic zone of nearly 1.4 million square kilometers. LVMH can also benefit from the Seychelles government’s support for wildlife protection policies, thereby enhancing its brand image.

Finally, we established an impact model with the collected data on illegal wildlife trade from 2015 to 2022. We used multiple linear regression model based on the least squares method to compute measurable impact from factors such as medical trade, experimental trade, food trade, fur trade, and decoration trade, yielding coeﬀicients for the influencing vectors of (2.651, 0.812, 0.164, -0.147, -1.811). We can decrease the future five-year illegal wildlife trade value to $20 billion, assuming positive factors decrease by 10% annually and negative factors increase by 5%. The model resulted in a final predicted value of 17.54 billion, indicating a 33.81% decrease in trade volume. We utilized a weighted probability model based on the five-point estimation to assess the likelihood of project success, resulting in a probability of 87.2%.

Furthermore, we put the wildlife trade within the larger ecological system and adapted the Leslie- Gower model as a fundamental framework to elucidate the dynamics of prey-predator interactions, the experiment results show the environmental protection factor will boost wildlife survival rates.

Moreover, when we slightly adjusted the initial trade values (±5%), the future illegal wildlife trade value will change within 0.047%, thus it shows that our models have strong robustness. 关注数学模型

1 Introduction

1.1 Overview

微信公众号：数学模型

1.1.1 Background

Wildlife traﬀicking, ranking as the world’s fourth-largest illegal trade, encompasses a diverse range of trades, including fur trade, food trade, decorative item trade, Medical trade, experimen- tal trade, and more. Like intricate root systems, it penetrates various dark corners of the world. Estimated to involve as much as $26.5 billion annually, illegal wildlife trade has profound and far- reaching impacts on biodiversity, the environment, and social stability, gradually drawing heightened attention from the international community. Governments, enterprises, and organizations are taking measures, wielding three swords, as depicted in Figure 1, to cut off the sources and pathways of illegal wildlife trade from different angles.

微信号：MATHmodels Enterprises Providing training and education for employees Enhancing supply chain management Adhering to all relevant regulations and laws

Food Trade Trading meat from wildly Selling protected animal components

Fur Trade Hunting wildlife to obtain fur product Selling products containing animal fur

Medical Trade Government Strengthen regulations with stricter penalties Conduct public education campaigns Establish reward systems

Organizations Conduct independent investigations Initiate advocacy campaigns

Decoration Trade Obtaining endangered wildlife for making decoration Trading ivory used in crafting artifacts

Experimental Trade Breeding animals for scientific experiments Illegally Trade genetic material or laboratory supplies Trading organs of  wildlife for traditional medical Selling drugs containing protected animal or plant

In the current context, the urgency of this issue becomes more apparent, prompting the interna- tional community to emphasize the imperative need for measures to combat wildlife crime through a series of international agreements.

However, despite these agreements, substantive and systematic measures for effective inter- vention still require further proposal and implementation. Confronting this global challenge, the international community needs to collaborate synergistically, actively exploring and formulating in- novative policy frameworks that not only robustly curb illegal wildlife traﬀicking but also contribute to maintaining the ecological balance of the planet and safeguarding precious natural resources.

When developing such policy frameworks, it is crucial for countries to work together to ensure they are comprehensive, feasible, and innovative, capable of addressing this urgent issue comprehen- sively and globally, guaranteeing the sustained protection of wildlife on a worldwide scale. 关注数学模型

1.1.2 Problem Restatement and Analysis

• Task 1: Evaluate scores of different clients in the dimensions of power, resources, and interests.

Evaluate their abilities to combat illegal wildlife trade and select the most suitable client. 微信公众号：数学模型

• Task 2: Analyze the selected clients from Task 1 and calculate the benefits they may gain from combating illegal wildlife trade.

• Task 3: Identify the weaknesses of the chosen clients based on their scores in power, resources, and interests. Collaborate with other clients who have stronger capabilities in these areas.

• Task 4: Evaluate the impact of clients on combating illegal wildlife trade by predicting the increase in biodiversity after project implementation.

• Task 5: Assess the likelihood of achieving the expected goals through predicting the required time for project implementation. Conduct a sensitivity analysis on the project model consid- ering the impact on the ecosystem.

微信号：MATHmodels To effectively illustrate the steps presented in our solution, we have created a visual guide showcasing our workflow, as depicted in Figure 2. In the process diagram, we clearly present the key steps in solving the problem and the modeling approach taken.

1.2 Terminology

Here we list the frequent symbols and their definitions used in the paper, as shown in Table 1. More minor symbols will be defined later.

Symbol

Description

The normalized evaluation of the client’s ability to decrease illegal wildlife trade, reflecting power factor. P The normalized evaluation of the client resources that can be used, reflecting the resources factor. R The normalized evaluation of the client to enact our project, reflecting interest factor. W The score of the client potential that can decrease the illegal wildlife trade. S 关注数学模型

1.3 Assumptions

▶Assumption 1: The mentioned factors including power, resources, and interests in this article are all related to combating illegal wildlife trade. 微信公众号：数学模型 ◦Justification: We focus on key powers and resources that can decrease the illegal wildlife trade:

government enforcement, international organization leadership, and sustainable development efforts by businesses. The required resources include funding, technology, and expertise, with a concentrated interest in supporting wildlife conservation and sustainable development goals.

▶Assumption 2: The power, resources, and interest factors for government, enterprises, and

non-governmental organizations have different meanings.

◦Justification: Each party has independent and distinct roles in the efforts to combat illegal wildlife trade. This delineation is beneficial for considering them as different types of clients, enabling the more precise formulation of targeted projects and strategies.

▶Assumption 3: New technologies and materials allow traditional industries that use animals

微信号：MATHmodels as raw materials to be upgraded.

◦Justification: There are many famous examples, such as Apple Inc. discontinuing the use of leather products and adopting new materials, which eventually led to more gains.

▶Assumption 4: Our clients are rational and can be persuaded by potential gains or reputation.

◦Justification: Our model assumes that enterprises have a certain level of operational feasibility in their willingness to accept our project for decreasing the wildlife trade.

▶Assumption 5: The amount of illegal trade is roughly proportional to the amount of related industries and is relatively stable.

◦Justification: The illegal wildlife trade can be viewed as a input cost of the related industry, and its share is relatively stable and roughly proportional to the total industry dollar amount.

1.4 Data Pre-processing

Suﬀicient data is the fundamental step in designing a project. To ensure the authenticity and reliability of our project design to the greatest extent possible, we have extensively collected relevant data from around the world, encompassing multiple countries, businesses, and organizations. We particularly focused on countries where illegal wildlife trade is prevalent, such as in Africa, and identified relevant businesses and organizations with a need for wildlife conservation projects.

Our data comes from a diverse range of sources, including various oﬀicial websites and statisti- [9] data, and oﬀicial national cal studies, such as oﬀicial reports on illegal wildlife trade, World Bank databases of each country. Such diverse data sources ensure the quality and credibility of the foun- dational data for our project, enabling us to more accurately assess and formulate effective strategies to combat illegal wildlife trade.

What seems diﬀicult is to assure the fully complete data in the procession of collecting. However, the availability of the data is a crucial issue, therefore it is necessary for us to process the missing data properly to enhance the accuracy and validity of our model. The methods of this procession are shown as follows:

• Mean Complement: If the data before and after the missing value exists, the mean value of the two will be used to substitute it. 关注数学模型 • Kindred Complement: While the two series of data are the same or in similarity, if one of them is attainable, the other one can be complemented by parallel.

• Fitting Complement: When the database is smooth and few continuous data is missed, we 微信公众号：数学模型 set the fitted curve to complement.

2 The Client Triangle Profile Model

2.1 Weight Calculation using EWM

The customer portrait model is a critical tool for evaluating different categories of clients, aiming to comprehensively assess each client’s ability to reduce illegal wildlife trade. From the perspective of client categories, we categorize clients into three distinct groups: government, businesses, and non-governmental organizations.

To depict the customer portrait, we conducted data analysis focusing on the dimensions of power (P), resources (R), and interests (W). We used the Entropy Weight Method (EWM) to calculate 微信号：MATHmodels the weights of indicators under each dimension. We assume that these dimensions have mP, mR, and mW indicators, and we use Pi, Ri, and Wi (i = 1, 2, 3, . . . , n) to represent the power score, the resources and the interests score of the n clients.

Firstly, we standardized the data for each indicator, using P ′ij, R′ij, W ′ij to represent the standardized values:

Pij −min Pij Rij −min Rij Wij −min Wij P ′ R′ W ′ (1) ij = , ij = , ij = max Pij −min Pij max Rij −min Rij max Wij −min Wij

where Pij, Rij, Wij represent the values of the j-th sample for the i-th indicator under the power, resources, and interests dimensions, respectively.

Secondly, for each dimension (P for power, R for resources, W for interests), we calculate their information entropy H(P) , H(R) , H(W) : j j j  n ∑  = −log2(n)  H(P) p′ ij log2 p′   ij  j n    j=1    n ∑ = −log2(n) H(R) r′ ij log2 r′ (2) ij j n    j=1    n ∑  = −log2(n)  H(W)  w′ ij log2 w′   ij j n j=1

where the nomarlized frequencies are / / / n n n ∑ ∑ ∑ p′ ij = P ′ P ′ ij, r′ ij = R′ P ′ ij, w′ ij = P ′ P ′ ij. ij ij ij i=1 i=1 i=1

According to the formula for information entropy, we calculate the information entropy of each indicator under power, resources, and interests dimensions. Using information entropy, we then cal- culate the weights of each indicator under power (Pi), resources (Ri), and interests (Wi) dimensions:

 

1 −H(P) 1 −H(R) 1 −H(W)     j j j (3) , ,   ∑ ∑ ∑ mP mR mW H(P) H(R) H(W) k − k − k − j j j 关注数学模型 j=1 j=1 j=1 We have selected two important indicators for each corner of the triangle for a comprehensive evaluation. The specific indicators and corresponding results are as follows:

微信公众号：数学模型

• Government category of clients

Power: Resources: Interests:

⋆GDP: The Gross Domes- ⋆Country Policy and Insti- ⋆Reducing Disease Transmis- tic Product serves as a criti- tutional Assessment (Policy): sion (Disease): The govern- cal financial indicator, reflect- The government’s capacity to ment focuses on the impact of ing the government’s financial formulate laws and policies to illegal wildlife trade on public strength in addressing illegal combat illegal wildlife trade by trade issues. reviewing and updating regula- health, especially in reducing the transmission of diseases.

⋆Citizens’ Education Level tions. ⋆Crime Rate Reduction and (Education): Higher education Public Security (Stability): levels among citizens facilitate ⋆Law Enforcement (Law): Addressing the connection be- better understanding and sup- The government’s enforcement tween illegal wildlife trade and 微信号：MATHmodels port for government regula- capabilities, include monitor- crime, to reduce overall crime tions, contributing to improved ing, apprehending, and prose- rates and enhance societal se- enforcement effectiveness. cuting illegal trade activities.

• Enterprise of clients

Power: Resources: ⋆Industry Influence (Indus- Financial ⋆ curity levels.

Interests: Support (Fi- ⋆Increasing Visibility (Visi- nance): The financial strength try): The influence of busi- bility): Businesses contribute of businesses, utilized to fund nesses within their respective to combatting illegal wildlife projects and activities aimed industries, with the potential trade to enhance their societal at combating illegal wildlife to drive industry legalization and standardization. trade. visibility.

Optimizing Reputation Technological Government Collabora- ⋆ ⋆ Advance- ⋆ ments (Technology): tion (Collaboration): Whether Posses- (Reputation): Active partic- ipation in social responsibility sion of advanced technologi- businesses have established col- cal capabilities for monitoring, laborative relationships with projects to optimize corporate reputation and improve brand tracking, and combating illegal the government to collectively combat illegal wildlife trade. trade. image.

[2]

• Non-Governmental Organizations of clients(NGOs)

Power: Resources: Interests: Crowdfunding: ⋆Advocacy and Collaboration ⋆ Access- ⋆Biodiversity Conservation public-supported (Advocacy): NGO capabilities ing funds (Conservation): Core interest crowdfunding in advocating for environmen- through tal policies and driving legal ities. changes. activ- of NGOs is the protection and maintenance of biodiversity. ⋆Volunteer Networks (Volun- teer): Operating extensive vol- ⋆Media Platform Promotion ⋆Climate Change Improve- unteer networks effectively en- (Media): Using media plat- ment (Climate): Potential in- gaged in monitoring and pro- forms to widely disseminate in- volvement in climate change tecting against illegal wildlife formation and generate social awareness. trade. projects related to illegal 关注数学模型 wildlife trade.

Clients Governments Enterprises Organizations Dimensions Indicators Weights Indicators Weights Indicators Weights 微信公众号：数学模型 Policy 0.131256514 Industry 0.224751434 Advocacy 0.256513982 Power Law 0.896743486 Collaboration 0.087471007 Media 0.434860180 GDP 0.878863122 Finance 0.605497597 Crowdfunding 0.312210962 Resources Education 0.121136878 Technology 0.12833233 Volunteer 0.687789038 Death 0.254019689 Visibility 0.12643817 Conservation 0.745980311 Interests Stability 0.745980311 Reputation 0.136802914 Climate 0.254019689

Through the analysis of weight data, we have identified unique strengths within each category. Government clients excel in the dimension of power, business clients demonstrate robust resource capabilities, and non-governmental organization (NGO) clients exhibit outstanding performance in the dimension of interests. This indicates that government clients possess a significant advantage in the power dimension, business clients exhibit remarkable capabilities in the resource dimension, and 微信号：MATHmodels NGO clients have a notable advantage in the interests dimension.

2.2 Typical Clients

For each category of customers, we selected specific examples closely related to illegal wildlife trade and conducted an analysis. ♢ Government Client: South Africa South Africa, as one of the countries with the richest biodiversity on the African continent, has drawn global attention to its abundant wildlife resources. However, due to the high profitability of wildlife products such as rhino horns and ivory in the international market, South Africa faces significant challenges in controlling the illegal trade of rhinos and elephants. This illicit trade poses a severe threat to South Africa’s wildlife population. Therefore, the government of the country needs to implement effective measures to combat this issue and protect its precious ecological resources.

We calculated the scores for South Africa in power (PA), resources (RA), and interests (WA) based on the indicators and their weights outlined in Table 2.

(PA, RA, WA) = (0.6644, 0.2772, 0.4644)

In this triangle porfile depicting South Africa, we can deduce that its scores in power, resources, and interest are (0.6644, 0.2772, 0.4644) respectively, as shown in Figure 3(a). Thus, we can conclude that LVMH holds a significant advantage in terms of power.

Enterprise Client: LVMH ♢ LVMH, as a luxury goods company based in France, is often under suspicion for the use of animal fur or precious animal products. This has raised concerns about the company’s social responsibility and sustainability in the context of wildlife trade. With the increasing global demand for sustainable practices, companies like LVMH need to scrutinize their supply chains and take measures to ensure that their products are not associated with illegal wildlife trade, thereby maintaining their reputation and social responsibility.

We calculated the scores for LVMH in power (PB), resources (RB), and interests (WB) based on the indicators and their weights outlined in Table 2.

(PB, RB, WB) = (0.4470, 0.9387, 0.2287)

In this triangle porfile depicting LVMH, we can deduce that its scores in power, resources, and interest are (0.4470, 0.9387, 0.2287) respectively, as shown in Figure 3(b). Thus, we can conclude that LVMH holds a significant advantage in terms of resources. 关注数学模型 Power Power, 0.66 － －＿＿ ......0呻．9--i---- 、、、、 Power, 0.44 」。46- 乡乡 ，会 Power, 0.22 ，， 、、、、、、 ＇， 、、、 ＇ / ，， / , / o; 微信公众号：数学模型 / / 、、、、、 / I / 、 I / 、 ，， 、、、、、 I ｀ ＇， I I ,; 、 ＼ I I I ｀ ＼ ／ ， I I / I ＼ ＼ I ＼ I ， ＼ I ＼ I ＼ ｀ ｀ Resources, 0.33 Resources ,0.28 Resources, 0.94 I I I 、人 I ＇ I 、、 I 心＇、 ，， ，， ／ Willings, 0.24 森么 I / - － － － － ＿一 / 、 / / I 、、、 、 Willings,  0.24 、、 、、＿ / Willings, 0.92 / / 、、、 、... _ / ;

.,. z Z / 一＿－ － － － － － ， / _ 多 / 乙 － －------ 乡'

•WCS (a) Porfile radar chart of South Africa (b) Porfile radar chart of LVMH (c) Porfile radar chart of WCS

微信号：MATHmodels Non-Governmental Organization (NGO) Client: WCS ♢ WCS is an international non-profit environmental organization dedicated to protecting wildlife and their habitats globally. As an organization actively engaged in addressing the issue of illegal wildlife trade, WCS strives to combat this challenge through scientific research, implementing conser- vation projects, advocating for policy changes, and collaborating with local communities. Through these efforts, WCS is committed to maintaining biodiversity, protecting endangered species, and promoting sustainable approaches to wildlife conservation.

We calculated the scores for WCS in power (PC), resources (RC), and interests (WC) based on the indicators and their weights outlined in Table 2.

(PC, RC, WC) = (0.2235, 0.3376, 0.9215)

In this triangle porfile depicting WCS, we can deduce that its scores in power, resources, and interest are (0.2235, 0.3376, 0.9215) respectively, as shown in Figure 3(c). Thus, we can conclude that LVMH holds a significant advantage in terms of resources.

2.3 Our choice of clients by AHP

In summary, we categorize clients into three main groups: government, businesses, and organi- zations. For each client, we construct a three-dimensional vector to reflect their varying proportions in terms of power, resources, and interests, thereby depicting their capability in combating illegal wildlife trade.

Through the calculation steps of the Analytic Hierarchy Process (AHP), we collected data from 265 countries, 157 enterprises, and 30 organizations, which are shown as Figure 4. Then we established a multi-level hierarchy to analyze the ability of governments, enterprises, and non- governmental organizations (NGOs) in combating illegal wildlife trade across the dimensions of power, resources, and interests. By formulating judgment matrices and computing weights, we quantified the relationships and importance of different indicators. The three-dimensional eigenvector E composed of power (VP), resources (VR), and interests (VW) is:

E = (VP, VR, VW) = (1.357, 2.289, 0.322)

[9], considering them as Government We collected indicators data related to 265 countries Clients. By applying the Analytic Hierarchy Process (AHP) method, we computed the following 关注数学模型 0.8 0.9

0.8 0.7 0.8 0.8 微信公众号：数学模型 1.0 0.6 0.7 0.9 0.6 0.6 0.8 0.8 0.5 0.6 0.6 0.7 0.4 0.6 0.4 0.4 0.4 0.2 0.5 0.5 0.2 0.4 0.3 1.0 0.225 0.3 0.0 0.2 0.0 0.4 0.8 0.200 1.0 0.2 0.175 0.6 0.2 0.0 0.8 0.4 0.150 0.05 0.1 0.4 0.2 0.10 0.6 0.125 0.6 0.3 0.15 0.3 0.2 0.4 0.4 0.100 0.20 0.8 0.5 0.25 0.6 0.0 0.2 0.075 1.0 0.7 0.30 (a) government (b) enterprise (c) organization

scores.

微信号：MATHmodels (P, R, W) = (0.705, 0.262, 0.271)

S = (P, R, W) · E = 1.646

In this analytical formula, S represents the comprehensive ability scores of the Government category in the dimensions of Power (P), Resources (R), and Interests (W). The numerical value 1.646 is obtained through the Analytic Hierarchy Process (AHP), where the relative importance of each dimension is calculated through judgment matrices for each dimension of the government. This value is then derived by multiplying the three-dimensional eigenvector (1.357, 2.289, 0.322) and the three-dimensional weight vector (0.705, 0.262, 0.271) and summing the products. It indicates that the Government category achieves a comprehensive performance score of 1.646 across the three dimensions.

[10], considering them as Enterprise We collected indicators data related to 157 enterprises category of Clients. By applying the Analytic Hierarchy Process (AHP) method, we computed the following scores.

(P, R, W) = (0.211, 0.659, 0.085)

S = (P, R, W) · E = 1.822

Similar to the previous formula, S represents the comprehensive ability scores of the Enterprise category. The numerical value 1.822 is obtained through the Analytic Hierarchy Process (AHP), where the relative importance of each dimension is calculated through judgment matrices for each dimension of the enterprise. This value is then derived by multiplying the three-dimensional eigenvec- tor (1.357, 2.289, 0.322) and the three-dimensional weight vector (0.211, 0.659, 0.085) and summing the products. It indicates that the Enterprise category achieves a comprehensive performance score of 1.822 across the three dimensions.

[11], which can be considered as Non- We collected indicators data related to 30 organizations Governmental Organizations category of clients (NGOs). By applying the Analytic Hierarchy Process (AHP) method, we computed the following scores.

(P, R, W) = (0.084, 0.079, 0.644)

S = (P, R, W) · E = 0.5022

Likewise, S represents the comprehensive ability scores of the Non-Governmental Organizations (NGOs) category. The numerical value 0.5022 is obtained through the Analytic Hierarchy Process (AHP), where the relative importance of each dimension is calculated through judgment matrices for 关注数学模型 each dimension of NGOs. This value is then derived by multiplying the three-dimensional eigenvector (1.357, 2.289, 0.322) and the three-dimensional weight vector (0.084, 0.079, 0.644) and summing the products. It indicates that NGOs achieve a comprehensive performance score of 0.5022 across the 微信公众号：数学模型 three dimensions.

Consistency checks were conducted during the calculation process to ensure the coherence of our judgments. By synthesizing weights at each level, we derived comprehensive ability scores for each category in combating illegal wildlife trade. The cumulative scores reveal that enterprises (1.822) > governments (1.646) > NGOs (0.5022), highlighting that enterprises have the highest overall score. This systematic and interpretable process provides a logical foundation for selecting enterprise-type clients and sheds light on the strengths of each category. The data analysis process indicates that governments excel in the power dimension, enterprises demonstrate robust resource capabilities, and NGOs exhibit significant strength in the interest dimension. However, after a thorough assessment across the three dimensions, enterprises emerge with the highest overall score, leading us to identify enterprise-type clients as the most suitable collaborators to address the global challenge of illegal wildlife trade.

The computation results align with the pivotal role that enterprise-type clients play in combating 微信号：MATHmodels illegal wildlife trade in real-world scenarios. These clients play a crucial role by effectively disrupting the circulation of illegal products through the provision of resources, technical support, and global supply chain supervision. Their awareness of social responsibility propels active engagement, and collaborative efforts and information sharing further strengthen the anti-illegal trade mechanisms. Adherence to regulations and pursuit of innovative solutions provide opportunities for enterprise-type clients to lead the industry while contributing to a reduction in the demand for illegal products in the market. Their involvement not only aids in maintaining ecological balance and wildlife protection but also underscores their commitment to social responsibility and sustainable development, enhancing their corporate image.

However, considering the multitude of global enterprises, and to facilitate effective project col- laboration, Figure 5 showed few sample enterprises from 157 enterprises related to illegal wildlife trade.They include media, technology, fashion apparel, and pharmaceutical enterprises. These vari- ous types of enterprises can play various roles in combating illegal wildlife trade, such as publicity, research and development of drugs and materials, and more.

Through the characterization of these enterprises using a Triangle Profile, we evaluated their comprehensive abilities in power, resources, and interest, assigning scores as depicted in Figure 5.

in Figure 6 Although LVMH may not necessarily be the top scorer in certain aspects when comparing the scores in three dimensions among these 10 enterprises (few samples from 157 enterprises), its 关注数学模型 overall qualities align better with our collaborative objectives after comprehensive weighting. LVMH scores 0.4157 totally. It demonstrates significant potential in combating illegal wildlife trade, leading us to choose LVMH as a partner to collectively address this challenge.

微信公众号：数学模型 (a) Scores of Power (b) Scores of Resources (c) Scores of Interests (d) Scores of Total

微信号：MATHmodels

3 Win-Win Model

To assess whether the project meets customer needs and has practical utility, breaking the dif- ficult situation of traditional projects and achieving innovative win-win situations with customers is crucial. The key to project innovation lies in accurately understanding customer expectations, specif- ically by delineating the benefits customers can derive through project collaboration. This process involves comprehensive consideration of the customer’s goals, desires, and anticipated outcomes. The project needs to be closely linked to the customer’s interests to ensure it meets their expectations and delivers tangible returns and value. Tailored measures are developed for different types of clients based on an in-depth understanding of customer needs.

3.1 The Project Developed

For our chosen client LVMH, we propose developing technologies in areas such as new mate- rials to replace the uses of wildlife and their fur. Additionally, these actions, aimed at combating illegal trade, contribute to shaping a positive brand image for the enterprise, providing visibility for innovative products, and creating a positive cycle.

To assess the benefits we bring to the enterprises. We have chosen the following indicators to calculate.

{ L = Investment in Relevant Innovative Projects + Echnology Expenses M = Income from Product Development

where L represents the cost, M represents the benefit of these indicators. And it’s easy to calculate the total profit of clients of this type is T = M −L.

3.2 Estimated Profit of Adopting Our Project based on Aﬀine Mapping

In the real-life example, Apple’s decision to discontinue leather products has brought tangible benefits and a positive reputation, providing us with insights.

[17], we obtained Apple’s iPhone sales revenue for the year By consulting the financial report 2023, which amounted to $2.01 × 1010. We computed the ratio of leather products from the oﬀicial sales website, and it was determined to be 4.7%. 关注数学模型 For the cost calculation (L1), we deducted the sales revenue related to leather products from the total iPhone sales revenue. This was achieved by identifying the proportion of leather-related products in Apple’s product line and subtracting it from the overall sales revenue.

微信公众号：数学模型 L1 = 2.01 × 1010 × 4.7% = 9.4563 × 109

By calculating the average research funding for three past projects similar to the development of leather alternatives, we estimated the research expenses for developing new materials. We also considered the research funding for the development of new materials as a cost (L2).

L2 = (3.875 × 109 + 4.761 × 109 + 4.295 × 109)/3 = 4.310 × 109

Next, we used industry-related sales forecasting models for the smartphone market to predict the sales revenue (M = 2.79528 × 1010) of the new material product for the next year.

The specific calculation formula for profit (T) is as follows:

T = M −L1 −L2 = 1.41865 × 1010 微信号：MATHmodels Based on the above calculations, it can be concluded that Apple has experienced an increase in profit after discontinuing the trade of leather products. From before the discontinuation (9.4563×109) to after (1.41865 × 1010), the company has gained more profitability.

By conducting aﬀine mapping (roughly proportional transformation with their total values) between Apple Inc. and LVMH, we follow a similar calculation approach to predict the profit of LVMH and other comparative clients. The prediction of the profit of LVMH is $128.06 × 109. Based on this profit data, it is evident that LVMH’s participation in our proposed project has the potential to yield substantial and tangible returns. Therefore, we choose to use this project as compelling evidence to persuade them, and the likelihood of success is significant.

3.3 Other Clients

We can use similar methods to analyze other clients by substituting their data into the corre- sponding expressions for calculation (the results are shown in the following Figure 7).

• Governments: Tanzania, South Africa.

• Enterprises: Louis Vuitton (LV), Saga Furs.

• Non-governmental organizations: Wildlife Conservation Society (WCS), Traﬀic.

After comparing the data in Figure 7, it is evident that whether it is government clients, enter- prise clients, or non-governmental organization (NGO) clients, each has experienced varying degrees of profit in the positive cycle of innovative projects. This underscores the project’s capacity to drive sustainable development for these three client types, indicating its value across diverse client cate- gories. From the data, it is apparent that enterprise clients have generally garnered more substantial profits in the relevant projects. This aligns with our conclusions in 2.2 and 2.3.

For instance, enterprise clients like LVMH may not necessarily have advantages in terms of power and interests, but they possess extensive resources. They can drive technological development and research new products to replace wildlife products in the implementation of measures against illegal wildlife trade. This approach addresses the problem at its source, demonstrating significant potential. By developing new products, enterprises can establish new industry chains, generate sales profits, and create a positive cycle. This makes them more robust and faster in terms of benefits compared to the other two client categories. 关注数学模型 微信公众号：数学模型

This further emphasizes that within the collaborative relationship, innovative projects are mu- 微信号：MATHmodels tually beneficial when working with enterprise clients. The projects not only promote the sustainable development of enterprises but also provide an opportunity for them to play a proactive role in ad- dressing the issue of illegal wildlife trade. Through close collaboration with enterprises, projects are likely to achieve a broader societal impact, forming more dynamic solutions.

4 The Complement Vector Model

In the process of selecting the clients mentioned earlier, we conducted a comprehensive evaluation of each potential client’s overall capabilities. Different clients exhibit significant variations in their scores across the dimensions of power, resources, and interests. Recognizing that a single client may have slight deficiencies in certain aspects during project execution, we introduced the Complement Vector Model.

For the current user, denoted as C, their scores in the comprehensive evaluation are represented ( ) as P, R, and W. We can obtain their complement vectors using the formulas: C(P), C(R), C(W)   C(P) = Sall · P −Pc  (4) C(R) = Sall · R −Rc   C(W) = Sall · W −Wc

4.1 Maximum Matching of The Complement

Assuming we have additional potential clients, C1, C2, . . . , Cn besides the client C we’ve already selected, and the profile data of Ci is (Pi, Ri, Wi). We can utilize the cosine similarity model:

( ) ( ) C(P), C(R), C(W) · (Pi, Ri, Wi) ( ) similarity( C(P), C(R), C(W) (5) , (Pi, Ri, Wi)) = cos (θi) = ∥ C(P), C(R), C(W) ∥∥(Pi, Ri, Wi)∥

This model helps identify another client Cx whose complement vector is most similar to that of client C, and we present the details in Algorithm 1. By examining the profile of Cx, we can gain insights into the specific capabilities in power, resources, and interests that client C needs to acquire through collaboration.

We created distinct client triangle profiles for over 200 government entities, over 100 enter- prises, and 13 international non-governmental organizations. Additionally, we visualized the three- dimensional capability vectors of all potential clients, as illustrated in Figure 4. 关注数学模型

Algorithm 1 Cosine Similarity Model

Input: C and C1,2,...,n representing the current client and a list of other clients. Output: Returns the closestClient to the current client.

微信公众号：数学模型 1: function CosineSimilarity(C, Ci) dotProduct ←DotProduct(C, Ci) 2:

magnitude_C ←Magnitude(C) 3:

magnitude_Ci ←Magnitude(Ci) 4:

dotProduct similarity ← 5: magnitude_C×magnitude_Ci return similarity 6: 7: end function 8: function FindClosestClient(C, {C1, C2, . . . , Cn}) maxSimilarity ←−1 9:

closestClient ←None 10:

for each client Ci ∈{C1, C2, . . . , Cn} do 11:

currentSimilarity ←CosineSimilarity(C, Ci) 12:

if currentSimilarity > maxSimilarity then 13: 微信号：MATHmodels maxSimilarity ←currentSimilarity 14:

closestClient ←Ci 15:

end if 16:

end for 17:

return closestClient 18: 19: end function

In the previous section, we selected LVMH as our client. To enhance its capabilities at min- imal cost, we calculated its three-dimensional complementary vector, denoted as S, with values (0.56, 0.06, 0.76). Subsequently, employing the cosine similarity method, we computed the similarity between S and the three-dimensional vectors of all other potential clients, as illustrated in Figure 8. The most optimal match, in which cosine similarity reached an impressive 99.9%, was found to be (0.35, 0.03, 0.46). This vector corresponds to the government of Seychelles, a country in the western Indian Ocean.

99.9% 1.00 Cosine Similarity 0.75 0.50 0.25 Cosine Similarity 0.00 Potential Clients

Seychelles is situated in the western Indian Ocean, 1500 kilometers east of the east coast of the African continent, comprising 115 islands. The overall economic scale of Seychelles is relatively small, with no large enterprises that have international influence or notable merger and acquisition projects. In recent years, Seychelles has focused on strengthening its relations with Western countries and international financial institutions while actively developing ties with emerging powers such as China and India to attract foreign aid and investment. The local workforce is proficient in English, French, and Creole. 关注数学模型 Seychelles maintains a relatively good overall social security situation, although there has been a noticeable increase in theft cases in recent years. In 2017, the Seychelles government issued a 10-year bond worth $15 million, with guarantees provided by the World Bank and the Global Environmental 微信公众号：数学模型 Facility, supporting sustainable fisheries development. The “Blue Bond” mechanism in Seychelles received the “Ocean Innovation Challenge Award” at the 2017 World Ocean Summit.

In August 2019, President Faure of Seychelles announced the initiation of the “Vision 2033 and National Development Strategy 2019-2023.” ”Vision 2033” outlines Seychelles’ development strategy for the next 15 years, aiming to build a vibrant, responsible, and prosperous nation with a healthy, knowledgeable, and capable population, in harmony with nature and aligned with the broader world.

Seychelles is renowned for its success in wildlife conservation, dedicating 42% of its territory to conservation efforts. Over 50% of its land is designated as a natural reserve, and it boasts an Exclu- sive Economic Zone (EEZ) covering nearly 1.4 million square kilometers, ranking second in Africa. The key industries supporting the national economy are tourism, fisheries, and handicrafts. While Seychelles prioritizes environmental protection in its industrial and agricultural systems, preserv- ing its pristine natural landscapes, this approach has somewhat constrained economic development. Seychelles is home to a rich biodiversity, featuring over 1,000 species of fish, rare birds such as the 微信号：MATHmodels Seychelles Black Parrot, Falco araeus, and Otus insularis, along with 26 species of crabs and various endangered sea turtles, including the critically endangered Hawksbill Turtle.

In 2023, LVMH achieved record-breaking annual highs in both sales revenue and net profit, surpassing the figures from 2022. Sales revenue reached 861.53 billion euros, marking a 9% year- on-year increase, while net profit reached 151.74 billion euros, reflecting an 8% year-on-year growth. The gross profit amounted to 592.77 billion euros, up 9%, and the operating profit reached 225.6 billion euros, experiencing a 7% year-on-year increase.

Initiating collaboration with the United Nations Educational, Scientific, and Cultural Organi- zation (UNESCO) in 2019, LVMH embarked on various projects aimed at minimizing the impact of climate change on biodiversity and enhancing the resilience of ecosystems. The group has set ambitious goals for itself, intending to restore 5 million hectares of wildlife habitats by 2030, fos- tering ecosystem regeneration, and safeguarding critically endangered flora and fauna. Biodiversity conservation stands as a cornerstone across all activities of the LVMH group, with the primary raw materials for its six major business sectors sourced from the natural environment.

Seychelles has earned worldwide acclaim for its achievements in wildlife conservation. Through its partnership with Seychelles, LVMH can play a more substantial role in combating wildlife traf- ficking, consistent with its commitment to environmental sustainability and biodiversity. Serving as a biodiversity hotspot, Seychelles offers LVMH an opportunity to access unique resources, serving as a potential wellspring of innovation for the company’s products. By providing financial support to Seychelles, LVMH has the potential to elevate its brand image and appeal to environmentally conscious consumers.

5 Impact Model

This research endeavor involves a meticulous investigation into the determinants influencing illicit wildlife trade, with due consideration given to related industries such as the animal fur trade market and the wildlife food industry. We systematically quantified trade volumes associated with various factors to formulate a precisely calibrated function, accommodating the intricacies of trade dynamics. we judiciously selected five key indicators. We have selected the animal fur trade market, biomedical industry, animal jewelry industry, and wildlife food industry, and their impact flows can be observed in Figure 1. Following a thorough and detailed study, we carefully selected trade data related to illegal wildlife traﬀicking. 关注数学模型 In our study, we employed the intricate statistical technique of multiple linear regression anal- ysis. We designated illegal wildlife trade as the dependent variable Y and identified fur trade, food trade, medicine trade, experimental trade, and decoration trade as independent variables Xi 微信公众号：数学模型 (i ∈{1, 2, ..., 5}). Meticulously selecting trade data spanning from 2015 to 2022, our investigation aimed at a comprehensive analysis. The systematic research seeks to unveil the price trends of key wildlife products. The study takes into account the trade volumes of these five variables Xi (i ∈{1, 2, ..., 5}) and their impact on the overall volume of illegal wildlife trade (Y ).

5.1 Basic Judgments based on scatter plots

Typically, before establishing a regression relationship, it is necessary to ascertain the presence of correlations within the data. To facilitate a more intuitive analysis, we utilized SPSS software to create scatter plots for each indicator’s trade against illegal animal and plant trade, resulting in a total of 36 scatter plots Figure 9. These scatter plots are divided into four parts, as depicted in Figure 9. Upon examining these 36 scatter plots, we identified a preliminary linear relationship between 微信号：MATHmodels each independent variable (fur trade, food trade, medical trade, experimental trade, decorative trade) and the dependent variable (illegal wildlife trade).

[15] for the years 2015 to We filtered illegal wildlife trade data from the CITES Trade Database 2022 and separated the trade values for the aforementioned five categories from it.

Food trade Experimental trade Pharmace Experimental trade Food trade Pharmace Decoration trade Fur trade Total Trade Decoration trade Total Trade Fur trade Total Trade Pharmace Pharmace Total Trade Total Trade Total Trade Pharmace Pharmace

Food trade Food trade Food trade Fur trade Fur trade Fur trade Food trade Fur trade Experimental trade Experimental trade Decoration trade Experimental trade Decoration trade Experimental trade Decoration trade Decoration trade Pharmace Experimental trade Food trade Food trade Experimental trade Decoration trade Pharmace Decoration trade Total Trade Total Trade Fur trade Fur trade

(a) Total & Fur & Decoration (b) Pharmance & Food & Ex- (c) Total & Fur & Decoration (d) Pharmance & Food & Ex- perimental perimental

5.2 Construction of curve Fitting Model based on least square Method

Model Development

♢ In constructing the fitting model for this study, we chose the amount of illegal wildlife trade Y as a quantitative indicator to intricately measure the scale of illicit trade in wild animals and plants. The designed fitting function takes into account various influencing factors within the matrix Xi (i = 1, 2, ..., 5). In this model, each coeﬀicient βi for independent variables is defined as a regression coeﬀicient, quantifying the impact of the independent variable Xi on Y while keeping all other independent variables constant. The intercept is denoted by β0, and the residual term ϵ represents a random variable with a mean of 0 and a variance of σ2, symbolizing the influence of random factors on Y .

For the model development, we carefully selected the trade amounts of fur trade, food trade, medicine trade, experimental trade, and decoration trade from 2015 to 2022 as the independent variable matrix. The impact of each independent variable is represented through E1 to E5 as follows: 关注数学模型   (Influence of fur trade market demand) E1 = β1X1      (Influence of the medical industry) E2 = β2X2  微信公众号：数学模型 (6) (Influence of decorative sales) E3 = β3X3    (Influence of wildlife food sales) E4 = β4X4     (Influence of scientific experiments) E5 = β5X5

Thus, we have successfully established the functional equation for the fur trade, food trade, medicine trade, experimental trade, decoration trade, and illegal wildlife trade:

(7) Y = f(β1X1, β2X2, β3X3, β4X4, β5X5)

5.3 Multivariate Linear Regression Test

Preliminary Model Testing and Assessment

♢ Based on the established linear model, we conducted multivariate linear regression analysis on 微信号：MATHmodels Xi (i ∈1, 2, ..., 5) using SPSS software. The primary step involved performing an analysis of variance (ANOVA), primarily employed to verify the successful model construction. In this process, the F value represents the ratio of between-group mean square and within-group mean square. Each F value corresponds to a P value. Hence, a smaller P value indicates a higher likelihood of retaining the respective feature.

Upon detailed analysis of the model summary, we observed an F value of 65.784, with a signif- icance level P of 0.015, less than 0.05. This suggests that at least one independent variable explains a portion of the variance in the dependent variable, leading to an increase in regression variance and a decrease in residual variance. Therefore, we can aﬀirm the successful construction of the model. ♢ In-depth Testing of the Multivariate Linear Regression Model We conducted a thorough examination of the model summary in Table 3, delving into the as- sessment of linear relationships and regression fit. The key observations derived from this analysis are highlighted below. We emphasize the pivotal metric, R2 = 0.979, signifying that all indepen- dent variables collectively account for a remarkable 97.9% of the variance in illegal wildlife trade. The robustness of this result is underscored by the diminished impact of the variable count on R2, fortifying our confidence in the model’s explanatory power.

R2 β t P V IF

Illegal Fur Trade -0.147 -0.158 -0.042 0.507 12.88 Illegal Food Trade 0.164 0.075 0.039 0.729 11.725 Illegal Medical Trade 0.812 1.01 0.027 0.396 14.092 Illegal Decoration Trade -1.811 -0.03 -0.025 0.823 4.65 Illegal Experimental trade 2.651 0.068 0.003 0.927 14.175

Furthermore, a detailed scrutiny of the Durbin-Watson test value (DW value of 2.320) within the range of 0 to 4 unequivocally indicates a strong independence of residuals. This finding further bolsters our confidence in the model, highlighting its reliability in capturing data characteristics and trends. The histogram of residuals Figure 10 follows a normal distribution with a mean close to 0 and a standard deviation close to 1 (standard normal distribution). This indicates that the linear regression meets the normality assumption. The P-P plot Figure 11 also confirms the satisfaction of the normality assumption. 关注数学模型 This in-depth testing not only showcases the model’s outstanding performance in capturing linear relationships but also underscores its high degree of fit to the data and effective handling of residuals. These comprehensive observations collectively unveil the richness of the multivariate linear 微信公众号：数学模型 regression model in elucidating the intricate dynamics of the illegal wildlife trade.

1.0

3 Average=4.79e-15 Standard Expected cumulative probability Difference=0.535 0.8 Number of Cases=8

Frequency 2 0.6

0.4 1

0.2

0 -1.0 -0.5 0.0 0.5 1.0 微信号：MATHmodels 0.0 0.0 0.2 0.4 0.6 0.8 1.0 Standardized residuals Actual cumulative probability

5.4 Model Solving and Analysis of Impact Results

Solution using Least Squares

♢ We employ the least squares method to estimate the coeﬀicients β of the multiple linear re- gression equation. The primary objective of the least squares method is to minimize the residual sum of squares (RSS). In this context, Yi represents the actual observed values, with the selected data comprising true values spanning from 2015 to 2022. The predicted values, denoted as ˆYi, can be observed in Figure 12. Here, n denotes the range of years selected for the data. β signifies the coeﬀicient vector, X is the independent variable matrix, Y is the dependent variable vector, and X′ denotes the transposed matrix used in the least squares coeﬀicients calculation. This approach ensures a rigorous estimation of the coeﬀicients, enhancing our ability to delve into a comprehensive analysis of the impact results.  2022 ∑   (Yi −ˆYi)2 RSS = (8)  n=2015  β = (X′X)−1X′Y

In-Depth Analysis of Impact Factors β ♢ Through a detailed examination of the regression coeﬀicients β in Table 3, we can accurately assess the influence of various industries on the target variable. This impact relationship is visually observed through a chord diagram, where the width of the lines reflects the degree of influence.

• Fur Trade (-0.147): A negative coeﬀicient indicates a negative correlation with the target variable. Increasing fur trade may lead to a decrease in the target variable.

• Food Trade (0.164): Although the coeﬀicient is positive but relatively small, it suggests a slight positive impact on the target variable. Increasing food trade may slightly elevate the target variable.

• Medical Trade (0.812): A larger positive coeﬀicient implies a significant positive impact on the target variable. Increasing medical trade may notably enhance the target variable. 关注数学模型 • Decoration Trade (-1.811): A highly negative coeﬀicient indicates a substantial negative impact on the target variable. Increasing decoration trade may result in a sharp decline in the target variable.

微信公众号：数学模型

• Experimental Trade (2.651): A highly positive coeﬀicient suggests a considerable positive impact on the target variable. Increasing experimental trade may lead to a significant increase in the target variable.

Decoration Experiment Medicine 一．－Real ．． 尸Prediction 5,400 FOOD 5、100 4书800 Hundred million Fur 4,500

4,200

3,900 微信号：MATHmodels 3.600

3,300 6 7 2015 2022 2016 5 2021 2019 2020 2018 2017 2 4 Trade volume of illegal animals and plants 3 Year

Through a thorough analysis of the regression coeﬀicients in the multiple linear regression equa- tion, we have derived a comprehensive conclusion regarding the relationships between different indus- tries and the target variable. In this equation, medical trade and experimental trade are identified as key driving factors for the target variable, while decorative trade is considered a factor exerting a negative impact on the target variable.

Y = 1.527 −0.147X1 + 0.164X2 + 0.812X3 −1.811X4 + 2.651X5

In essence, within the context of illegal wildlife trade, our integrated ranking reveals that ex- perimental trade has the most significant impact on the target variable, followed by medical trade in second place, and food trade ranking third. However, the fur trade and decorative trade exhibit negative correlations, with the decorative trade showing the most pronounced adverse impact.

5.5 Probability Weighted Assessment Model

To assess the likelihood of achieving the anticipated goal of 20 billion in illegal wildlife trade within a 5-year timeframe, we employed a five-point estimation weighted probability model for fur trade, food trade, medical trade, decoration trade, and experimental trade. Firstly, we estimated the probability of each illegal trade indicator achieving its respective goal and then calculated the probability of overall project success by weighting the factors.

Initially, we assumed the most optimistic time for each trade to achieve its respective target (denoted as m) years, the most likely time (denoted as r) years, and the most pessimistic time (denoted as h) years. Based on these time estimates, we computed the probability of a single illegal trade indicator achieving its goal within the given s years.

 e = (m + 4r + h)/6     b = [(h −m)/6]2 (9)  q = (s −e)/b    关注数学模型 Gi = 50% + σ/q (i = 1, . . . , 5) where e represents the average time for a specific illegal trade indicator to achieve its goal, and b denotes the standard deviation of the expected time, and q indicates the deviation from the average duration, and Gi (i = 1, . . . , 5) represents the probability of a single illegal trade indicator achieving 微信公众号：数学模型 its goal within 5 years, with 50% indicating the probability on the normal distribution curve. The σ coeﬀicients corresponding to q take values of (1σ = 68.37%, 2σ = 95.46%, 3σ = 99.73%).

The probability of completing all activities within 5 years is calculated as the sum of each trade’s probability multiplied by its normalized weighted factor:

G = G1q1 + G2q2 + G3q3 + G4q4 + G5q5.

In a specific scenario, assuming the most optimistic time (m) for government, organization, and business to achieve their respective goals is 2 years, the most likely time (o) is 4 years, and the most pessimistic time (h) is 6 years. The calculated mean time (e) and standard deviation (b) are obtained, with deviations from the mean project duration (q) being (4, 0.666, 2). Based on these time estimates, the probability of each trade indicator completing its goal within 5 years is 97.3%, and the probability of completing all trade indicators within 5 years is 87.2%.

微信号：MATHmodels To enrich and make the language more scientific: In order to preliminarily assess the feasibility of the multiple linear regression model, we assume that the positive influencing factor, trade volume, decreases by 10% annually, while the negative influencing factor increases by 5% annually. Setting a target that the illegal trade in plants and animals will decrease to 20$ billion after 5 years, we input these values into our linear regression equation and predict that the trade volume in 2027 will decrease to $17.54 billion. This represents a 33.81% decrease from the $25.6 billion in 2022, achieving the expected goal and indicating the rationality of the model.

5.6 Sensitivity analysis

In discussing the influencing factors of illegal wildlife trade, there exist five distinct independent variables, namely fur trade (X1), food trade (X2), medical trade(X3), decoration trade (X4), and experimental trade (X5). Their initial values are (140.80, 76.56, 58.65, 0.41, 0.21). We subject each of these trade variables to a continuous fluctuation of ±5% while keeping the other four trade variables constant. Since the medical trade has the greatest impact factor on the illegal wildlife trade, we simulate a 5% downward fluctuation in the medical trade. The schematic diagrams illustrating the relationship between these five parameters and illegal wildlife trade are plotted using Python software, as shown in Figure 14.

Original Value Prediction Value Original Value Prediction Value 30.00 30.00 25.00 25.00 AIM 17.45 AIM 20.00 20.00 16.93 15.00 15.00 10.00 10.00 5.00 5.00 0.00 0.00 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 2032 2033 2034 2035 2036 2037 2038 2039 2040 2041 2042 2043 2044 2045 2046 2047 2048 2049 2050 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027 2028 2029 2030 2031 2032 2033 2034 2035 2036 2037 2038 2039 2040 2041 2042 2043 2044 2045 2046 2047 2048 2049 2050 TotalTrade FurTrade FoodTrade MedicineTrade DecorTrade ExperimentTrade TotalTrade FurTrade FoodTrade MedicineTrade DecorTrade ExperimentTrade

(a) Before adjustment (b) After adjustment

The predicted trend changes in the images are minimal, and by 2027, the overall trade variation is not significant. Illegal wildlife trade sees only a marginal decrease of 0.047%, indicating the robustness of our model in considering various factors and intervention measures. 关注数学模型

6 Wildlife Trade within Larger Ecological Model

6.1 The Leslie-Gower Model

微信公众号：数学模型 [8] as a fundamental framework to We utilize the wildlife trade within larger ecological model elucidate the dynamics of the interaction between wildlife populations and the ecological environment. The continuous-time representation of the Leslie-Gower model is described by the following system of differential equations: ( )  dx r1 c1y   1 + ky −βx − dt = x  x + k1 ( ) (10)  dy c2y   r2 − −E dt = y x + k1

where x and y represent the densities of the prey and predator populations, respectively; r1 and r2 are the growth rates of the prey and predator populations, respectively; β denotes the internal competition intensity within the prey population; c1 and c2 are the maximum per capita decrease 微信号：MATHmodels rates for the prey and predator populations, respectively; k1 represents the environmental protection level for both the prey and predator populations; k is the anti-predator ability of the prey population; E stands for the harvesting capacity; and r2 > E.

Based on the difference equation form of (10), we obtain ( )  1 vn   −un − un+1 = un exp  1 + dvn un + s ( ) (11)  fvn   γ − un + s −p vn+1 = vn exp

6.2 Population Dynamics

The outcomes from applying the Runge-Kutta method to solve differential equations under varying degrees of environmental protection k1 are depicted in Figure 15. It is evident that the distinctions among the curves are negligible, suggesting minimal impact of environmental protection factors on the temporal evolution of population density. From this figure, we can also conclude that although the enhancement of environmental protection may not directly reduce illegal trade, it can slightly mitigate the impact of illegal trade.

0.07 k1=0 k1=0.1 k1=0.2 0.065 k1=0.3 Population k1=0.4 k1=0.5 k1=0.6 0.06 k1=0.7 k1=0.8 k1=0.9 k1=1 0.055 0 10 20 30 40 50 60 70 80 90 Time(month)

关注数学模型

7 Strengths and Weaknesses

7.1 Strengths

微信公众号：数学模型

• Refined Quantified: The Client Triangle Profile Model takes a holistic approach by consid- ering three client categories—governments, enterprises, and non-governmental organizations.

This ensures a comprehensive evaluation of capabilities and potential across various dimensions.

• Innovative Revenue Model: The Win-Win model introduces innovative revenue indicators, especially the methond of discontinuing the use of leather products and adopting new materials

• Cost Reduction and Progress Advancement: The application of complementary vectors and cosine similarity helps assess deficiencies in client capabilities eﬀiciently. This strategy, aiming at mutual complementarity with minimal cost, can significantly reduce project costs and expedite progress.

7.2 Weaknesses

微信号：MATHmodels

• Long Computation Time: The success of predictive modeling relies on accurate and up- to-date data. Any inaccuracies or changes in influencing factors could affect the reliability of future predictions.

8 Conclusion and Future Works

8.1 Conclusion

Our comprehensive models and innovative technologies to address illegal wildlife trade have demonstrated significant advantages. The Client Triangle Profile Model, considering government, enterprise, and non-governmental organization capabilities, accurately identified LVMH as the most suitable enterprise for collaboration using the EWM method. The Win-Win Model introduced inno- vative revenue indicators, providing a sustainable financing avenue, while the Complementary Vector Model and Maximum Matching method offered clear criteria for selecting strategic partners. The Impact Model and Future Predictions, utilizing a vast amount of illegal wildlife trade data, increased project implementation flexibility by adapting content to market trends. Overall, our approach has yielded satisfactory results in improving client selection accuracy, innovating financing models, and adapting to market dynamics.

8.2 Future Works

In the future, we will be committed to collecting broader and more accurate data, utilizing emerging technologies to continuously improve and optimize our client’s triangular profile model, further enhancing the accurate assessment of our client’s capabilities and potentials, and ensuring that our model remains highly adaptable in the ever-changing business environment.

At the same time, we will continue to explore partnership opportunities beyond the LVMH Group and conduct comprehensive assessments of companies in different industries to identify po- tential partners, bringing together expertise and resources from different sectors to build lasting and mutually beneficial partnerships!

关注数学模型

MEMO

To: Louis Vuitton Moët Hennessy (LVMH) From: ICM Team 微信公众号：数学模型 Date: February 6, 2024 Subject: The project to Reduce Illegal Wildlife Trade I am pleased to share a comprehensive summary of our recent initiatives in combating ille- gal wildlife trade through innovative techniques. Our multi-faceted approach encompasses diverse methodologies to address this critical global challenge. Below is a concise overview of our key strate- gies and findings:

• Client Triangle Profile Model and Enterprise Selection:

We constructed the Client Triangle Profile Model, considering three categories of clients: gov- ernments, enterprises, and non-governmental organizations, and we calculated weights for in- dicators across Power, Resources, and Interests dimensions.

To comprehensively assess the capabilities and potential achieved by different types of clients 微信号：MATHmodels across various dimensions, we selected indicators including economic, technological, and promo- tional aspects, and scored different clients. Then We calculated that LVMH was the enterprise with the highest score among all enterprises. Namely, LVMH can develop new technologies and materials as alternatives to wildlife products, and engage in extensive promotional activities.

• Win-Win Model and Revenue Innovation:

In real-life examples, Apple Inc.’s ban on new leather products has brought objective benefits and reputation to Apple, which has inspired us. Then we introduced a Win-Win model, incorporating new revenue indicators such as penalty revenues, eradication of transactions, and joy-driven education. Through extensive data analysis, we assess project benefits for clients, with specific technological and developmental suggestions provided. We estimate LVMH’s annual profit value at $128.06 million, emphasizing its significant potential as a client.

• Complementary Vector Model and Collaborative Operations:

We developed a complementary vector model to identify additional capabilities required by clients during project execution. we applied Maximum Matching to pinpoint potential collab- orators, emphasizing the Seychelles government as a strategic partner for LVMH.

• Impact Model and Future Predictions:

We have collected a substantial amount of data on the illegal wildlife trade (2015-2022), in- cluding specific trades such as the Medical Trade, Experimental Trade, Food Trade, Fur Trade, and Decoration Trade. We use these data as indicators to assess their overall impact on illegal wildlife trade, adjusting our project content accordingly. We have set a five-year goal for the project at $20 billion, through predictive modeling and consideration of relevant influencing factors, then we calculate the likelihood of achieving this goal to be 87.2%. It indicates that the implementation of our project and the associated adjustments are quite reasonable.

Our Innovative technology initiatives establish a robust framework for addressing illegal wildlife trade with LVMH, and provide opportunities for strategic partnerships, revenue enhancement, and future sustainable development predictions.

This concludes our project. Thank you.

关注数学模型
