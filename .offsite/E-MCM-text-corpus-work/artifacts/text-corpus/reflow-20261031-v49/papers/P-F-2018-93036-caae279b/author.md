T1 F1 T2 F2 T3 F3 Problem Chosen

T4 F4

MCM/ICM

Summary Sheet

Summary

Contrary to the pervasive belief that human society has entered the information age, the massive data produced by human individuals are not fully exploited yet. Private data nowadays are under poor, isolated management by individual enterprises, where thevalue of data cannot be fully extracted to benefit either its provider or owner. To address this problem, a well-established market system is required that not only prices and rewards data sharing, but also regulates and protects private information.

To satisfy the requirement, our paper provides a detailed analysis based on a dataset PI-DATA, based on which we propose a sophisticated and generalized model, Private Infor- mation Price Estimation (PIPE), which is able to estimate the price of private information (PI) regarding different data domains of PI and social subgroups.

Task 1: We abstractly extract feature vectors from individuals and query requests to dis- tinctly characterize their traits in different data categories..

Task 2: We estimate the correlation matrix of data categories and develop an amendment formula to accurately compute data value considering internal and external factors.

Task 3: We establish a Supply and Demand Model to estimate the value of PI as a commod- ity on the level of individuals, groups and nations.

Task 4: We surveyed the existing government act (e.g. Privacy Act, GDPR, APPI, etc.) and price regulations related to the private information around the world. Also, we intro- duce a dynamic variation to illustrate the change of human decision-making over time.

Task 5: We introduce a risk-to-benefit factor and show how generational differences change our model. We also compare PI with PP and IP.

Task 6: To clarify the connection between different subgroups of people, the multi- dimensional clustering algorithm for friends (mCAF) is applied to the dataset PIDATA. By conducting experiments on the data from different groups as well as from the same group, we find that the relationship between data and value is not linear, but log-likelihood.

Task 7: We simulate the effect of massive data breach and predict the effect of PI loss and cascade event using our model. Based on our pricing system, we think agencies should compensate to individuals directly for data breaches.

In the end, we make sensitivity analysis and discuss the strengths as well as weaknesses of our model. Moreover, a policy memo is presented to the decision maker on the utility, results and recommendations based on our PIPE policy model.

MEMORANDUM

To: Decision Maker about Privacy From: MCM 2018 Team Subject: Private Information: The Emergence of a New Asset Date: Monday, February 12, 2018

1 Introduction

In the era of ”anywhere, anytime”, people now produce more data than ever before. The variety and volume of digital records that can be created, processed and analyzed will continue to increase dramatically. By 2020, International Data Corporation (IDC) estimates that the global amount of digital records will increase more than 40-fold.

The problem is to quantify the cost of privacy. That is, to establish a metric to eval- uate the monetary value of keeping PI protected and the fees it would cost for others to possess or utilize PI. We consider private information (PI) as record of ”everything a person makes and does”. To make the problem clearer, several concepts need to be explained.

Domain of Private Information. An initial list of types of private information in- cludes: Digital identity (e.g., names, addresses, phone numbers, demographic infor- mation, social network profile information, etc.); Relationships to other people and organization (social media, contact list and profiles); Communication data and logs (emails, SMS, phone calls, IM and social network posts); Media produced, consumed and shared (in-text, audio, photo, video and other forms of media); Financial data (fi- nancial transactions, accounts, credit scores, physical assets and virtual goods); Health data (health/medical records, medical history, medical device logs, prescriptions and health insurance coverage); Institutional data (government, academic and employ- ment data).

Subgroup of Individuals. E.g. citizenship, professional profiles, age, education level, occupation, etc.

Risks. The risks involve loss of safety, money, valuable items, intellectual property (IP), the person’s electronic identity, professional embarrassment , loss of a position or job, social loss (friendships), social stigmatization, or marginalization.

2 Solutions and Conclusions

Private information will continue to increase dramatically in both quality and diver- sity, and has the potential to unlock significant economic and societal value. To some extend, Private Information (PI) is similar to personal property (PP) and intellectual

1 18

18

16 16

14

12 14 10

5 4 12 3 0 2 1 2 1 3 4 0 10 5

property (IP). However, there are also discrepancies among them. PI differs from PP and IP in that it can be sold or given to others who then have the right to use it without ownership, and it needs to be regulated by government. These information and pri- vacy issues should be protected not only by the individuals but also by the agencies. Based on our model, the private data should not be trackable by the government for national security concerns.

Building a harmonious ecosystem around personal data will require significant commitment from all stakeholders. Our model proposes four critical solutions todeal with the problem:

An expanded role for government, such that governments can use their purchas- • ing power to help shape commercially available products and solutions that the private sector can then leverage;

Mechanisms for enhancing trust among all parts in private information transac- • tion;

Integrate principles surrounding and user trust and data protection into the de- • velopment of new services and platforms;

Policy makers and agencies should launch an international dialog, which should • encompass governments, international bodies such as the World Trade Organi- zation, end user privacy rights groups and representation from the private sec- tor. It should include not only US and European Union members, but interested parties from the Asia-Pacific region and emerging countries;

2

5 Sensitivity Analysis

19 Demand Model................................................................................................................. 19 5.1 mCAF Model......................................................................................................................20 5.2

6 Conclusions and Future Work

20

A Implementation of Function σ(·) 22 A.1 Demographics...................................................................................................................22 A.2 Family & Health................................................................................................................24 A.3 Property............................................................................................................................. 24 A.4 Activities............................................................................................................................ 25 A.5 Consumer...........................................................................................................................26

B Privacy Act 26

1 Introduction

1.1 Problem Background

We are moving towards a “Web of the world” in which mobile communications, social technologies and sensors are connecting people, the Internet and the physical world into one interconnected network [1]. Vast quantities of data records are increasingly gathered by cheap and numerous information-sensing devices on personal information (PI) including but not limited to tweets, purchasing histories and health records. In 2016, roughly 16.1 zettabytes (1021 bytes) of data are being generated each day, and it is estimated that the figure will increase to 163 zettabytes by the year 2025 [2].

Mining and analyzing such data enables researchers to study, understand and evenpre- dict human behaviors on the individual, group and global level. Advanced data analytics methods that extract value from data have been in widespread use in insurance, marketing and many other industries [3]. For instance, methods combining big data with deep learn- ing methods have shown superior performance in predicting traffic flows [4] and managing high-risk patients [5].

However, the massive collection, sharing and distribution of personal data are prone to certain risks concerning information privacy. As participation in social networking sites has dramatically increased in recent years, services such as Wechat, Twitter, and Facebook al- low millions of individuals to create online profiles and share personal information with vast networks of friends-and, often, unknown numbers of strangers [6]. Data breaches also pose considerable threats to sensitive private information that involves personal health in- formation (PHI), personally identifiable information (PII), trade secrets of corporations or intellectual properties [7].

It has been acknowledged that data providers can possibly be classified into subgroups according to their data’s value distribution over multiple domains (e.g. finance, health). On the other hand, personal or community risks related to data privacy often arouse significant differences in peoples’ privacy choices across such domains as well [8].

More and more intensive sharing are taking place nowadays, while the management and trading of private data are under loose control of the government and companies. Currently, millions of people are tricked into offering their data in exchange for little reward. However, the use of their data is far from efficient due to data isolation between enterprises. Moreover, some of these data are not even kept safe, and stolen data can possibly encourage illegal activities, such as fraud.

1.2 Our Work

To address this situation, we model private information that can be classified into sev- eral categories as a range of digital commodities that are constantly produced throughout a person’s life, the value of which is determined by a joint strategy that takes into consid- eration potential losses caused by disclosure of personal information as well as social and commercial benefits to be exploited from that data. The actual price of such data fluctuates around its real value under the influence of supply and demand, the cumulative effect and many other factors.

In this paper, we introduce three feasible techniques. Firstly, we propose a vector-based representation for both data providers and data query requests that abstractly and quanti- tatively describes features of private data, along with an corresponding value predictor that approximates the value function via correlation matrices. Secondly, with the introduction of a dynamic market system, we are able to further investigate the fluctuation in the real price influenced by both inner factors (e.g. supply and demand) and external causes (e.g. a sudden data bleach). Lastly, we develop an social network model to especially investigate the network effects of data sharing and the impact of social connection on data correlations with the multi-dimensional clustering algorithm mCAF.

The major contribution of this work is that we present a reliable price model for pervasive collection, sharing and trading of private information. In our experiments, we apply and test our model under diverse conditions, where it gives interesting and reasonable results which convinces us that the currency of private information should be kept under strict control under laws and regulations in order to maintain a healthy data economy.

2 Assumptions & Nomenclature

2.1 Assumptions

Tobetter quantify the problem, our private information pricing model is based on several assumptions that hold true in most cases or is indisputably satisfiable under government regulation. Assumption 1. All kinds of private information can be classified into a fixed number of distinct data categories (e.g. demographics, family & health, etc.), the number is denoted by m. Assumption 2. Personal data brings benefits to the society by contributing to researches that intends to study the social and financial behaviors. Profits made from fraud or harassment are not taken into consideration. Assumption 3. For information security and many other concerns, all the gathered data are man- aged by a trusted third-party organization, which protects uses’ data and helps sell them under owner’s permission.

Assumption 1 ensures that the number of parameters required to model private data is limited, thus it makes sense to represent PI with matrices. Assumption 2 guarantees that an universal understanding of data value exists, which forms the basis of our model. By assumption 3 large-scale management and regulation of data are made possible.

2.2 Nomenclature

In this paper we use the nomenclature in Table 1 to describe our model. Other symbols that are used only once will be described later.

3 PIPE: Mathematical Model for Private Information Price

Estimation

In this section, we will discuss all details about our model, which is capable of estab- lishing an accurate pricing system of personal data with the application of 1) a vector-based representation that distributes both benefits and risks of data from a certain subgroup over m data categories; 2) a dynamic pricing strategy that determines the intrinsic value as well as market price of data; 3) a social network model that further improves the predicting ac- curacy by taking data correlation originated from social connections into account.

Symbol Definition Total number of data categories m The ith category ci Individual that produces data I Individual feature vector X σ( ) Individual feature extractor · PI query request q Query feature vector Y ϕ(·) Query feature extractor Correlation matrix C Raw value of a person’s data under a certain query v Sequence length of personal data T Freshness of private data t Quantity of data records N Cumulative factor of data sequence ω Decay factor of history data τ Scale factor µ j Amended value of a person’s data under a certain query v Data size from person i di Total information contained from the PI I Neighborhood Γ Region R Types of Agencies Q Price concerning different agencies Pagency Interaction value between person i and j of social circle Gij Organizations O Tie strength Ti k Weight summary of one measurement to one node Wi Similarity between two vertices Simi,j Threshold Neighbor N M Metric that evaluates the sensitivity ofmCAF Eq(·) Function that judges equality Group label of vertex i li

Our idea is that the intrinsic value of personal data comes from two aspects: the poten- tial risk from information disclosure, and the social benefits brought about by data analytic. Such benefits and threats posed by personal data varies not only among different data cat- egories, but also between diverse social subgroups. Another unnegligible factor that affects the value of data is the data quality demanded by corporations or institutes. For instance, a commercial dataset that requests detailed financial information should definitely be charged higher than a rough portrait only involving the overall income and tax bills of the same so- cial group. There is nothing ambiguous that a variety of additional factors also have impacts on data value, including freshness, quantity and consistency, which are taken into account in our model as well.

Based on such assumptions we model private data as a commodity in continuous pro- duction, which is then fit into a market model where data owners can choose to pay for var- ious levels of privacy protection, or to put their data on sale via a trusted third-party data manager. The overall supply is mainly determined by people’s willing to share their data based on its benefit-risk ratio , while the market demand follows a gaussian distribution and can be affected by incidents such as data breaches. We further classify data agencies into three types based on their purchasing power, and develop a pricing strategy for the third-party data manager.

Since human data is highly linked and individual behaviors can be quite correlated with those whom they are socially, professionally, economically or demographically connected, we further consider the natural social network as a graph and cluster similar individuals on multiple dimensions based on both network structure and profile information. On the basis of such social clusters, we especially polish our pricing policy in consideration of similarities within clusters and distinctions between them.

The overview of our entire pricing framework and three major components of it are il- lustrated in Fig. 1.

3.1 Vector-based Representation for Individuals and Queries

3.1.1 Individual Feature Vectors

Based on the assumption in Sec. 2.1 that private data can be classified into m distinct categories, an individual’s private data can thus be considered to consist of data records in multiple categories. In our model, we assume m = 5 and the categories include demographics, family & health, property, activities and consumer data.

The value of a person’s entire data can then be split into m independent category values, the sum of which is equal to the original data value. Therefore, it makes sense to represent private information of individuals with an m × 1 matrix, which is actually a vector:

where I is a data provider, element Xi(1 ≤i ≤m) in vector X indicates the value of I’s data in the ith category, and function σ(·) extracts such category values based on life events andindividualattributes. WedefinevectorX aspersonI’s feature vector mainlybecauseits elements reveals the essential value of I’s data that is distributed over m categories.

The core part of Eqn. (1) is the function σ( ) that maps a person to the corresponding · feature vector. The process is accomplished based on an analysis on the most influential factors of data value conducted by Financial Times [9]. The report points out that contrary to popular belief, the value of private information does not increase linearly with its amount. In fact, general information about a person, such as their age, gender and location is worth a mere $0.0005 per person, or $0.50 per 1,000 people. It is certain milestones in a person’s life that prompt major changes in data values, such as becoming a new parent, moving homes, getting engaged, buying a car, or going through a divorce.

As is mentioned above, the value of data limited to a certain category is defined as the sum of potential risks and benefits incurred by it. On the basis of the Financial Times re- port, we develop a sophisticated model that implements the function σ( ). Here we briefly · introduce its mechanism, the complete implementation can be referred to in Appx. A A person can possess a number of attributes at the same time, such as being engaged, own- ing a home and current job, and some values of these attributes can possibly incur risks or benefits if known by a data company, for example, being engaged = true and current job = gov- ernment officer. Our model includes a databases that stores the economical value vectors of certain attribute-value pairs, as is shown in Table 2, factors regarding to personal properties, health conditions and activities are considered more important and attached higher values than others.

Attribute condition Value vector / $ [0.116 0 0 0 0] Being a millionaire [0 0.260 0 0 0] Having a heart disease [0 0 0.105 0 0] Registered at a real estate agency [0 0 0 0.135 0] Interested in foreign travel [0 0 0 0 0.136] Holding a store loyalty card

By significance we mean the magnitude of vectorscalculated by norm X . Note that all || || ourvectorsconcentratevaluesinonedimension(onedatacategory),bywhichweintendto reduce data correlations between categories, which will be reconsidered in Sec. 3.1.2.

Algorithm 1: Feature vector extractor

Input : An individual I, information value database . S Output: The feature vector X = σ(P ). Σ Σ 1 X ←0 0 . . . 0 ; 2 for attr ∈{P’s attributes} do if (attr, P[attr]) ∈S.values then 3 X ←X + S[(attr, P[attr])]; 4 5 return X;

As is shown in Alg. 1, our algorithm first sets the initial feature vector as an all-zero vector and then checks all the attributes of that person to determine if some attribute-value pairs can be found in our database. If a match is found, which means a certain value-creating condition is met, the value vector corresponding to that attribute-value pair will be added to the person’s feature vector. In other words, a person’s feature vector is the sum of all value vectors of the conditions satisfied by his personal attributes.

Based on Alg. 1, we are able to determine the typical individual feature vectors of various social subgroups, which will be discussed in Sec. 4.1.

3.1.2 Query Feature Vector & Correlation Matrix

Similar to individual feature vectors defined in Sec. 3.1.1, we define an m 1 query feature × vector Y = ϕ(q)that represents the query request q with m scalars, each stands for the inten- sity of private data requested in an data category. The intensity is measured by the amount as well as accuracy of requested data. For instance, if full information of a person’s demo- graphic characteristics and purchasing history is requested, the query feature vector should Σ Σ be 1 0 0 0 1 .

However, with merely query vectors we are still not able to accurately calculate the value of private information, as data correlations tend to occur between different categories of data. Toaddress this phenomenon, we introduce a correlation matrix C that takes connections between various categories of data into consideration, and define that the value of a piece of data record from individual I queried with feature vector Y as

v = σ(P )CY T (2)

.Σ ΣΣ Ideally, with no data correlations the correlation matrix C = E = diag 1 1 1 . . . . In order to estimate the intensity of data correlations, we fill the correlation matrix C in following manners:

Ci,j = |cov(ci, cj)| (3) where ci and cj are the ith and jth data category value. Our final correlation matrix C is computed based on feature vectors extracted from typical population subgroups, which will be discussed in detail in Sec. 4.1 and demonstrated in Fig. 6.

1.0000 0.8231 0.2793 0.6463 0.8443 0.2197 0.2226 0.6463 1.0000 0.6767 0.5403 0.1649 0.6767 1.0000 C = 0.8443 (4) 1.0000 0.6916 0.8231 0.2197 0.5403 0.2793 0.2226 0.1649 0.6916 1.0000

which suggests that the most magnificent data correlations exists between data categories of

• Demographics & Property

• Demographics & Activities

• Activities & Consumer

On the basis of Eqn. (2) and Eqn. (4), we are able to calculate the raw value of a spe- cific data record and its query requests. However, there remain external factors that have strongly affect the real value of private data, among which the most significant one is time. It is widely acknowledged that data value decays with time. On the other hand, a consistent data record sequence collected throughout a long time period should be attached additional value. Similarly, data scale affects the value of private data nonlinearly. Thus, an amend- ment is made with Eqn. (2) by introducing variations:

j = eωT −τtN µv (5) v where the dynamic element T denotes the sequence length (/days) of data, t stands for the freshness of private data (days since the data is generated), and N represents the number of data records. Parameters ω, τ and µ affects the real value in exponential and multinomial −3, τ = 9.50 manners. In our estimation based on information rules [10], ω = 1.28 10 × × −4 and µ = 1.05. 10

3.2 Dynamic Market System & Pricing Strategy

3.2.1 PI Demand Model

sbenefit , λ ∈[0,1] (6) λ = j j sbenefit + srisk

Criterion 1 2 3 4 5 Financial Risk 0.05 0.062 0.074 0.09 0.128 Health Risk 0.06 0.09 0.11 0.14 0.24 Family Risk 0.05 0.062 0.088 0.15 0.22 Social Risk 0.03 0.062 0.1 0.13 0.17

Thus, the demanding of an individual j ∈J+is D(j) = λjPj −rj Σ ΣdiMi,j (7) , ω∈J +Mi,ω i This part illustrates that purchasers possess a substantial amount Asymmetric Information. of information about data providers. These facts suggest that the restrictions such as policy and culture - which make it difficult for data providers to adjust prices when they provide private information to purchasers over time - have different price effects across different sellers and buyers depending on their privately revealed types, cultural and political issues. Incorporating such factors in our model therefore become important in anticipation of us- ing the model to study the PI problem. Formally, we estimate these effects in the following equation 8, Σ 5 Defaulti,t = αj(i) + αt + βn1ψi,t=n + sit (8) n=1 Here the dependent variable is an indicator for any instance of default by purchaser i af- ter period t, and the key coefficients βn capture differences in default rate across different private information, which denoted by ψ. Meanwhile the fixed effects for purchaser i and time t help ensure that these risk comparisons are made within otherwise observably similar purchasers.

Model Exposition This section presents the PI model. The backbone of the demand model is a finite mixture of agency types, each of whom has demand over PI providers.

Our model denotes type by θ. We specify several parameters to be estimated for each type. First, each type enjoys a flow utility djθ from buying from person j and a time utility njθ from transacting with person j; meanwhile the utility is normalized to zero. Addition- ally, in order to capture the adjustment cost, each type pays a agency cost sjθ for refer to potential related PI with person j. The parameters (θ,j)∈Θ×J are the key demand djθ, njθ, sjθ { } parameters to be estimated in the model, along with a probability distribution µθ over types.

Integrating over taste shocks s for each choice yields the standard Bellman equation for continuation values V , which is shown in Eqn. (9). .Σ Σ j|j, k, θ)) (9) V (θ,j, k) = log exp(v(j j, k , jj,kj where the lower-case v term denotes total expected payoffs. The value of v depends on data buyers’ past-period and current-period choices. The expectation Eθ can be decomposed as Eqn. (10), j,j,b)] = (1−δ(θ))Tθθj(θ)V(θ Eθ[V (θ j,j,b)+δ(θ)Tθθj(θ)V(θ jj,0,0). (10)

With the establishment of Eqn. (5), our model further takes time variations and scale effects as dynamic elements into consideration to estimate the worth of personal data over time.

3.2.2 Buyer-Seller Relationship Influence to Price

As Fig. 2 shows, internet advertising revenue has grown strongly over the last ten years. In 2013 it hit $42.8 billion in the US. Internet giants such as Google and Facebook have busi- ness models underlined by the use of personal data, but most people would have trouble knowing who exactly has access to the data trail they are generating across the internet [11]. A recent study by JPMorgan Chase [12] found that each unique user is worth approximately $4 to Facebook and $24 to Google.

Besides commercial corpo- Advertisi ng Revenue 40 rations, there are also other agencies who purchase PI. 35 Mozilla collect data about 30 users to better personalize Price ($bn) their experiences with their 25 open source products such as Firefox, Thunderbird. The 20 information they gather through 15 analytics can be used to make their product easier to use. 10 They also use cookies (small 2004 2006 2008 2010 2012 data files placed in browsers) Year

to remember language pref- shadow represents statistical uncertainty and variance. erences. Center for Dis- ease Control utilizes the data shared to trace the spread of disease in order to prevent further outbreak.

There are 3 types of agencies in our model and their purchasing power is shown as Ta- ble 4. The price estimation system concerning with different agencies who purchased the PI is illustrated as Eqn. (11).

Σ M τjQi, (11) Pagency = j=1 where τj is the control level of individual j to sell his/her own data, there are totally M individuals in a group/nation, i can be 1, 2 or 3 which represents the purchasing Q Q Q Q power of different types of agencies.

mCAF: a Multi-dimensional Clustering Algorithm for Friends of So- 3.3 cial Network Services

The multi-dimensional clustering algorithm for friends (mCAF) is adopted by us to per- form multi-dimensional clustering. Multi-dimensional clustering algorithms on social net- works are progressively gaining popularity due to the information and insights produced using large-scale social data. [13] describes the user’s opinions, comments, and likes in so- cial media have significant relationships with the popularity of that post. Multi-dimensional cluster analysis is a strategy for identifying different Facebook users’ fan groups and pro- vides insights to prompt further research analytics [14]. Both network structures and profile information should be taken into consideration while analyzing a user’s clusters on social networks [6, 15].

Denotation Types of Agencies Q1 Commercial Corporation, e.g. Google, Facebook, Microsoft, etc.

Q2 Non-Profit Organization (NPO), e.g. Mozilla, GNU, WWF, etc.

Q3 Government Department, e.g. NSA, Department of Energy, etc.

In this study, we used the Facebook Graph API to retrieve information of 600 users. First, we define the measurements of clustering.

Social Circles. A social circle is a group of people who have the same interests or join the sameactivity.WedefineMij asthenumberofmutualfriendsofuseriandj andGij asthe interactionvalue. Wequantifythesubject’sinteractionswithinthecommunityto obtainSij with Eqn. (12) and then normalize the result as Eqn. (13)

MGij = Mij + Gij,MG = {MGxy | x,y ∈1,2,3,...,n} (12) MGij = max(MG) , S = {Sxy | x, y ∈1, 2, 3, . . . , n} Sij (13)

Regions. We determine the region of the users and then calculate the distances between them and store them as a dataset described by D1, D2, D3, D4 . Take the calculation of dis- { } tance between A and B as an example, D1 represents the distance between the hometowns of A and B; D2 represents the distance between the current residence of A and B; D3 rep- resents the distance between A’s hometown and B’s current residence; D4 represents the distance between A’s current residence and B’s hometown. The calculation of Rij is shown as Eqn. (14).

Rij = α × D1 + β × D2 + γ × D3 + δ × D4 (14)

Organizations. If two individuals attended the same school or worked in the same com- pany, the organizations measurement Oij is set equal to 1 since they have a connection. If no connection is present, the Oij is set equal to 0.

Tie strength. We retrieve related information and use the method described in [16] to cal- culate the tie strength as Tj, which indicates the tie strength between a user and his jth friend.

mCAF maps a user’s friends into un-directed, weighted graphs. We define the entire graph as G = {V, E}, in which V is the set of vertices and E is the set of edges, defined as . Ei,j(ek ) , which represents a connection if a value ek is greater than zero between nodes i,j i,j i and j under measurement k.

Let vertex i V , where the structure of i is defined by its Definition of vertex structure. ∈ neighborhood denoted by Γ (i)in Eqn. (15)

Γ(i) = {j | j ∈V ∧Ei,j ∈E} (15)

Eqn. (16) definesthe Definition of the weight summary of one measurement to one node summary values of measurements from vertex j, which is connected to i:

Σ j=|V | W k = (e ), wherej ∈Γ(i) k (16) i,j i j=1 Definition of the weight summary of one measurement to two nodes Let vertex m V , ∈ and let edges from (i,m) and (j,m) exist. Eqn. (17) defines the summary values of measure- ments from vertex m, which is connected to i and j:

Shestructuresimilarityoftwoverticesiandjisdefined Definition ofstructure similarity as Eqn. (18):

1 2 3 = .S1 , S2 , S3 Σ {Ti,j,Ti,j,Ti,j} = . (18) Sim i,j i,j i,j i,j W 1 · W 1 + W 2 · W 2 + W 3 · W 3 i j i j i j

If two nodes can be clustered together based on Definition of the threshold neighbor measurement k, their structure similarity value Sk must be greater than the preset threshold i,j sk to filter out noise. Eqn (19) defines neighbors with qualified similarity structure values. The parameter sk could be estimated via training.

Nsk(i) = .j|j ∈Γ (i) ∧Sk ≤skΣ where k = 1 to 3 (19) i,j

The complete mCAF algorithm is described in Algorithm 2.

The clustering result of mCAF is shown in Fig. 3. The social network of several individ- uals are clustered into 8 subgroups. The visualization of network shows the correlations between different people.

2.0

2.0

1.5 1.5 I 1.0

0.5 1.0

5 4 0.5 3 0 2 1 2 1 3 4 0 5

Network and information I To better evaluate the network effects of data sharing, we investigate the relationship between two individuals who are highly linked and discover the relationship between the data size from one person and the information it can provide. Define di is the data size from person i and = f (d) [0, 1] represents the information the data on one person can provide. I ∈ There are totally M individuals. Eqn. (20) represents the function between d and and Fig. 4 I illustrates the function in the circumstance of i = 2.

Σ M I = log(1 + di) (20) i=1

4 Experimental Results

4.1 Task 1: Price Point for Protecting One’s Privacy and PI in Various

Applications

In order to accurately model risk to account for both 1) characteristics of the individuals, and 2) characteristics of the specific domain of information, we introduce the concept of individual and query feature vectors discussed in Sec. 3.1.

After surveying on several datasets [17, 18, 19] and recent methods, we collect our dataset PIDATA with an API provided by Facebook [20]. The usage of this dataset observes the Plat- form Policies, Data Use Policy, Statement of Rights and Responsibilities. Corresponding statistical information is illustrated as Fig. 5. Fig 5(a) is age distribution. Fig 5(b) is gender distribution. Fig 5(d) is education distribution. Fig 5(c) is occupation distribution. Fig 5(e) is education occupation distribution. Fig 5(f) is friend distribution.

0.016 0.20 50 0.014 0.012 0.15 40 Ratio 0.010 0.10 Number 30 Ratio 0.008 0.006 0.05 20 0.004 0.00 10 0.002 0.000 0 0 20 40 60 80 100 Female Male Occupation Age Gender

(a) Age Distribution (b) Gender Distribution (c) Occupation Distribution

0.0200 0.4 0.0175 0.3 0.0150 Occupation Ratio 0.0125 0.2 Ratio 0.0100 0.1 0.0075 0.0050 0.0 0.0025 0.0000 0 50 100 150 Education Level Number of Friends Education Level (e) Education - Occupation Joint (d) Education Distribution (f) Number of friends Distribution

tors) of 6 selected subgroups. It is clear that the value of person’s data is partially related his age and social status. Another interesting observation from Fig. 6 is that high covariance exists between certain data categories, which will be dealt with in Sec. 3.1.2.

To develop a price point for PI protection, we exam the true value of a person’s full data and its components. Fig. 7 shows how different categories of private data contributes tothe value of a person’s PI.

Based on the computed value of personal information, we are able to establish a price point for protecting it by treating data protection as an special insurance. Although the trade value of data can is just a few dollars, cost for each stolen data record can be as high as $141 - roughly 70-fold of its trade value, and the likelihood of a recurring material data breach over the next two years is estimated as 27.7%, according to a data breach study by IBM [21]. Therefore, to firmly protect a certain data record for 1 year, one must invest 10 times of its trade value calculated from Eqn. (5), which leads to the deduction that it might be better to share personal data and make profits from it if the risk is low.

4.2 Task 2: Pricing Structure of PI

With the introduction of feature vectors, correlation matrix and the amendment formula (Eqn. (5)), we can simply determine how much a person’s information is worth given a query on a specific domain. Based on a thorough survey on 77 adults, we are able to estimate the corresponding query feature vector of several query domains. The results are listed in

Based on query feature vectors in Table 5 and Eqn. (2), values of private information queried by different domains are illustrated in Fig. 8.

From results shown in Fig. 8, we can establish a pricing structure correspondingly. The price is explicitly calculated in view of different basic elements of data via individual fea- ture vectors defined in Sec. 3.1.1. As for cost of privacy across various domains, it can be

Domain Average query feature vector [0.93 0.37] 0.68 0.13 0.96 Social media [0.82 0.98] 0.53 0.94 0.24 Financial transactions [0.26 0.10] 0.99 0.08 0.11 Health / media records [0.66 0.84] 0.58 0.13 0.74 Search histories [0.24 0.12] 0.05 0.05 0.35 Location info calculated in similar manners as Sec. ??, where protecting cost and trade value of data are in direct proportion. If the risk of data disclosure is negligible, spending considerable money on data protection would be an unnecessary cost, and people might prefer to have their data unprotected in order to save budgets.

4.3 Task 3: Supply and Demand

People become more clear about which agencies had purchased their PI, how much their PI was worth and how PI was being used.

Based on the above model, we evaluate the influence of the control level to the price of PI. With data becoming a commodity, we find that:

It is appropriate to consider forces of supply and demand for PI. Commercial Corpo- • rations 1 have higher demand for PI, which makes it possible for them to provide Q higher offer compared with the other two types of agencies.

If people have control to sell to their data, which means τj varies with different indi- • viduals, the price Pagencyincreases with the τj.

4.4 Task 4: Assumptions and Constraints - Political/Cultural Issues

The assumptions and constraints of our model, which is also the political and cultural issues of the United States, European Union and other countries is listed as below. Suppose our model is proposed under the circumstance which is in compliance with local govern- ment regulations and cultural issues. Firstly, we explain the terminology used in the model.

4.4.1 Explanation of Terminology

Agency: any corporations, organizations, Executive department, military department, • Government corporation, Government controlled corporation, or other establishment in the executive branch of the Federal Government.

Individual: a citizen of the United States or an alien lawfully admitted for permanent • residence.

Private Information: any item, collection, or grouping of information about an indi- • vidual that is maintained by an agency, including, but not limited to, his education, financial transactions, medical history, and criminal or employment history and that contains his name, or the identifying number, symbol, or other identifying particular assigned to the individual, such as a finger or voice print or a photograph.

4.4.2 Political Issues and Cultural Issues

The United States: Privacy Act [22] The Overview of the Privacy Act of 1974, 2015 Edition is prepared by the Department of Justice’s Office of Privacy and Civil Liberties (OPCL). Tracking the provisions of the Act itself, the Overview provides reference to and legal analysis of court decisions interpreting the Act’s provisions.

The purpose of the Privacy Act is to balance the government’s need to maintain informa- tion about individuals with the rights of individuals to be protected against unwarranted invasions of their privacy stemming from federal agencies’ collection, maintenance, use, and disclosure of personal information about them. More details are in the Appx. B.

European Union: General Data Protection Regulation (GDPR) [23] The GDPR aims primarily to give control back to citizens and residents over their per- sonal data and to simplify the regulatory environment for international business by unifying the regulation within the EU. The regulation was adopted on 27 April 2016. It becomesen- forceable from 25 May 2018after a two-year transition period.

Data breaches. Under the GDPR, the Data Controller will be under a legal obligation to notify the Supervisory Authority (SA) without undue delay. The reporting of a data breach is not subject to any de minimis standard and must be reported to the Supervisory Authority within 72 hours after having become aware of the data breach.

Citizen Control of Personal Data. Under the GDPR, organizations are encouraged to give back control of personal data to the individual, or citizen.

Canada: Personal Information Protection and Electronic Documents Act The Personal Information Protection and Electronic Documents Act (PIPEDA or the PIPED Act) is a Canadian law relating to data privacy. It governs how private sector organi- zations collect, use and disclose personal information in the course of commercialbusiness. In addition, the Act contains various provisions to facilitate the use of electronic documents.

The law gives individuals the right to

• know why an organization collects, uses or discloses their personal information;

• know who in the organization is responsible for protecting their personal information;

expect an organization to protect their personal information by taking appropriatese- • curity measures;

• obtain access to their personal information and ask for corrections if necessary; and

Japan: Act on Protection of Personal Information (APPI) APPI reflects the Japanese socio-cultural characteristics for personal information protec- tion. Personal information leakage cases and social responses in Japan reflect three Japanese socio-cultural characteristics: Uchi/Soto awareness, insular collectivism and Hon’ne/Tatemae tradition. An effective law protecting personal information in Japan’s cultural environment cannot be made simply by copying the privacy protection laws in western nations. Instead, legal protection of personal information should be drafted that reflects and takes into ac- count these socio-cultural characteristics [24].

4.4.3 Price Regulations

Generally, the data value of people varies from different regions. It’s common to see quite a lot of variation by location. Fig. 9 is the statistical result, which is a comparison of the total number of a person’s data value for countries around the world (ones without enough data are left gray) [25]:

Based on the model and the political/cultural issues, we can draw the conclusion that information privacy should be made a basic human right when thinking about policy rec- ommendations.

4.5 Task 5: Generation Difference

In the perspective of risk-to-benefit ratio of PI and data privacy, there are generational differences. For example, the risk-to-benefit ratio is different between old people and young people when their health record is leaked. For old people, it is usually much higher than that of young people.

As generation changes, the input individual attributes change and data value depends on the generation correspondingly. As for the risk-to-benefit factor we defined in Eqn. (6), it describes the risk-to-benefit ratio of PI. The factor will change since the benefit score and risk score will change. Considering all the effects that generation change have, our final data price will be affected in the process above. PI (private information) is different from PP (private personal property) and IP (intellectual property). PI is an abstract concept. It is non-entity. However PP often refers to the property of people. It physically exists. IP is

for countries around the world (ones without enough data are left gray) the property of human intellect including copyrights and patents. PI is only known by the owner but IP is not only known by the owner. People all know the owner of the IP.

PI is also similar with PP and IP to some extent. PI and PP are both private while PI and PP are both abstract.

4.6 Task 6: mCAF: a Multi-dimensional Clustering Algorithm for Friends

of Social Network Services

Based on the mCAF model we proposed previously, we have the following conclusions:

Network effects of data sharing sharing do effect the price system for individuals, sub- • groups, and entire communities and nations.

It is the responsibility of the communities to protect citizen’s PI if communities have • shared privacy risks.

4.7 Task 7: Data Breach Effect

Data breach, especially massive data breach where millions of prople’s PI are stolen will affect the privacy a lot. Taking TJX data breach as example, it involves more than 100 million records and causes 118 million dollars loss to cover the loss and potential liabilities. That does not include the loss in reputation of brand and other indirect cost. From the research of IBM [21], we get cost of data breach for different industries (Fig. 10) and countries (Fig. 11). Wecan see that data breach widely exists and PI loss is a factor that we should notneglect.

The PI loss and cascade event caused by massive data breach will impact the price point. In our model, we have considered such effect. Eqn. (7) shows the trade off between the price and data breach effect. When massive data breach happens, the trade off factor λj will be smaller and thus λjpj will be smaller. rj depends on the level of data breach. For massive data breach and the corresponding cascade event, it would be higher. We can see that the price will be lower. It is reasonable since data breach will violate the assumption that all the gathered data are managed by a trusted third-party organization, which protects users’ data and helps sell them under owner’s permission. People’s data will be sold without permission or even be used as ransom. Some PI buyers will buy the breach data in an illegal way instead of buying data from people or trusted third-party organization. Demand will decrease and the price will be lower.

Agencies that breach the data should be responsible for the data breach and pay the individuals directly. As shown above, price of data will be much lower after massive data breach happens. The agencies should be responsible for the PI loss even if they don’t intend to breach the data.

5 Sensitivity Analysis

In this part we will do sensitivity analysis on our model. The sensitivity analysis show that our model is generalized and performs stably under different conditions, by which we are convinced that our model is able to solve the problem successfully.

5.1 Demand Model

This part shows the PI purchasers are sensitive to price and illustrates how it is possible to identify heterogeneous price sensitivities in the data. This heterogeneity will play a key role when we later use the model to study the equilibrium effects of the PI’s price restric- tions, because this heterogeneity affects which types of purchasers change their purchasing behavior in response to different relative price changes.

The event-time-specific estimates is shown as Eqn. (21):

log Qjt = αj + αt + βjt + αA,t + sjt, (21)

where Qjt denotes retention rates among existing buyers for data provider j at time t. The first two α terms in this equation implement a standard difference-in-difference design, while the αA,t terms capture differences between data provider A and other. For sake of presentation, the β term is included to account for different time trends among the included data providers. When estimating the demand side of the model, we use price variation to estimate heterogeneous price sensitivities across different purchaser types.

mCAF Model 5.2

We adopt the multi-dimensional clustering algorithm for friends (mCAF) to perform identify social clusters. mCAF algorithm randomizes the center points initially. We run mCAF several times on our dataset PIDATA and analyze the result.

We propose a metric to evaluate the sensitivity of mCAF in Eqn. (22), where Eq( ) is · defined in Eqn. (23)

very small in all experiments. It proofs that mCAF model perfoms well and is robust under different situations.

1 2 3 4 5 6 7 8 ExpNo 0.025 0.013 0.025 0.013 0.051 0.013 0.013 0.025 δ

6 Conclusions and Future Work

We develop a complete pricing system that accurately estimates the intrinsic value as well as market price of a certain individual’s data under a specific query request. Out method consists of three core components: a value calculator that maps a query and an individual to value of that data, a dynamic market system to further compute its market price, and a social cluster model to estimate the network effect on data price. In the envi- ronments and sensitivity analysis of our model, we find that it is accurate and generalized enough to be adopted in a wide range of domains.

One limitation of our current approach is that our model requires a large dataset to pre- cisely estimate the correlation matrix as well as many other parameters used in its mecha- nism. A promising future direction is to combine out methods with better estimation algo- rithms, e.g. Analytic Hierarchy Process (AHP), to reduce the variance caused by insufficient data.

In future work, our goal is to introduce non-linear data value predictors, e.g. neural networks, to characterize a more complicated relationship between individuals and data. Additionally, we plan to extend the current dataset in both scale and coverage to cater to the needs of deep learning algorithms.
