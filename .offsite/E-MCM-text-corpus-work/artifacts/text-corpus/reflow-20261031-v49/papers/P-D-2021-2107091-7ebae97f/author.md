Summary

During the revolution of music, interactions within and between genres can have a critical impact on the direction of musical change. In this paper, we develop models to analyze the inﬂuence between musicians, measure the degree of similarity between music, and reveal the changes in genres over time, as well as the inﬂuence of social, cultural, and historical aspects.

In TASK 1: First, we take each musician as a node and calculate the directed inﬂuence between musicians as weights by considering the factors of time span and genre span to build a directed music inﬂuence network. Then we use social network analysis (SNA) to analyze the inﬂuence network. The Degree Centrality of musicians in the network is calculated, and the Pagerank-modiﬁed eigenvector centrality is further used to measure the inﬂuence of musicians(MI), obtaining that Bob Dylan, The Rolling Stones, Chuck Berry, and Elvis Presley have the highest inﬂuence. We also ﬁnd that MI obeys power-law distribution, implying that the inﬂuence network between inﬂuencers and followers is a scale-free network. Finally, we explore the sub-network to analyze the meaning of the subset of MI.

In TASK 2 & 3: First, we use Cosine similarity and Euclidean similarity to measure global similarity Sglobal and local similarity Spart in two aspects of music, and consider the inﬂuence of popular trends to build Multi-dimensional music similarity evaluation model to measure the similarity of music (MS). Music within genres is found to be more similar than between genres. Then, to investigate the distinguishing features of genres, we combine different features and built the Discrimination evaluation model of feature combination to select the feature combinations that better distinguish genres from each other. Finally, we analyze changes in genres over time.

In TASK 4: To investigate whether the inﬂuencers actually inﬂuence the followers’ music, we develop a Long-short term inﬂuence model based on sliding window to calculate the inﬂuence degree score (IDS), considering the time sequence of release of the followers’ music and the inﬂuencers’ music, and determine the inﬂuence threshold. The result shows that followers are indeed inﬂuenced by the inﬂuencers. Subsequently, to determine the "contagiousness" of speciﬁc musical characteristics to musicians, we also consider speciﬁc musical characteristics, analyze the degree of closeness (DC) of characteristics of followers’ and inﬂuencers’ music, and establish the Contagious evaluation model of musical characteristics to ﬁnd the most contagious musical characteristics for different followers.

In TASK 5 & 6 & 7: First we establish constraint equations to identify musical revolution points based on the musical characteristics of the genre and the number of musicians in the genre. And based on the popularity before and after the musical revolution point to identify the main inﬂuencers in the musical revolution. Then we take 10 years as the examination period to calculate the IDS of the analyzed object to everyone within the genre based on the IDS in Task 4, and weight the sum to get the dynamic inﬂuencer index (DII) for identifying the leading ﬁgures within the genre in different generations. Ultimately, we analyze the relationship between music and politics, culture, and society.

Finally, we perform a sensitivity analysis of the model and investigate the effect of changes in the variable parameters of the model on the results.

1 Introduction

1.1 Background and Problem Statement

Music is a cultural product that people use to express their emotions and relax their bod- 微信公众号：数学模型 ies and minds. The inﬂuence of musicians on each other has a very important impact on the development and evolution of music. The development of computer technology allows us un- precedented access to data and computing power to analyze the network of inﬂuences between musicians, from which we can extract and analyze the key factors that inﬂuence the process of musical development, which will also help us understand the meaning of music better. In this problem, we need to accomplish the following objectives:

• Create a music inﬂuence network to analyze the inﬂuence between musicians and capture the music inﬂuence parameters in the inﬂuence network.

• Develop similarity evaluation model to explore the degree of inﬂuence and similarity between or within genres and between musicians.

• Identify indicators of revolution in genres and analyze the interplay between them in 微信号：MATHmodels relation to society, politics, and culture.

• Applying a dynamic analysis of the similarities and inﬂuences between and within genres of musicians over time.

1.2 Our work

The work we have done in this problem is mainly shown in the following Figure(1).

Musical Influence Network Analysis based on SNA Degree Centrality Influence Type data_by_artist Moditied Eigenvector Centrality Time Span Influence + Degree CentraPareto Principle Genre Span influence data_by_year Power-law Distribution Data Processing + Analysis Sub-Network SNA Network Analysis full_music_data Music Similarity Multi-dimensional Music Similarity Global Similarity What Distinguishes a Genre influence_data Data Processing Partial Similarity Genre Changes Over Time

Long-Short Term Influence Evaluation Model based on Sliding Window

Influencers Actually Affect Followers’ Music Musical Characteristics’ Contagious

Musical Revolution Dynamic Influencer  Indicator Music Evolution Influence of Social, Politics or Technology

2 Preparation of the Models

2.1 Assumptions

We made the following assumptions to help us with our modeling. These assumptions are the promise of our subsequent analysis.

• Assuming that the data is accurate and there is no falsiﬁed data: This means our analysis accords with the truth.

• Assuming that followers can only be inﬂuenced by songs released before the current year, and that songs after the current year have no effect on the follower’s for that year: this is done

关注数学模型 to measure the true inﬂuenceability of the inﬂuencers in a sliding window model.

• Assuming that the decade when the musician begin his carrer is the year when they debut, because the accurate years when the musicians debut are not given.

• Assuming that the musician’s genre is limited to the genre provided by the data, and have no genre changes, that all his/her songs are in the style of his or her genre 微信公众号：数学模型

2.2 Notations

The primary notations used in this paper are listed in Table 1.

parameter description T time-span inﬂuence factor DCi degree centrality ECi eigenvector centrality MI music inﬂuence Sglobal global similarity Spart partial similarity 微信号：MATHmodels V (i) music feature vector MS multi-similarity SMS short-term similarity LMS long-term similarity IDS inﬂuence degree score DC degree of closeness DII dynamic inﬂuencer indicator

3 TASK 1: Musical Inﬂuence Network Analysis Based on

SNA

3.1 Data Processing

An overview of the given data shows that some songs are sung by more than one person (e.g. It Can’t Happen Here and I Wonder If I Take You Home), and such songs cannot reﬂect the characteristics of a single musician, so to avoid disturbing the model, we remove the data of a total of 4410 chorus songs (4.4% of the original data). Since there are singers with only choral music, they have no music data after the deletion of choral music, which are invalid data. We remove these people, including those who are not shared between two dataset, to prevent any effect on the model. The data processing is shown in the Figure(2).

Data processing •Removing the chorus song: 4410 songs(4% of the dateset) •(songs cannot reflect the characteristics of a single musician) step1

• Removing 174 musicians not shared between two datasets step2

3.2 Model Overview

To analyze the musical inﬂuences among musicians, we establish a directed network of

musical inﬂuences with each musician as a node and directional inﬂuences among musicians as关注数学模型 weights. We then further explore the inﬂuence among musicians using social network analysis (SNA) to capture the music inﬂuence in the network to measure the inﬂuence of each musician. Finally, we explore the sub-networks of the inﬂuence network and explore the signiﬁcance of music inﬂuence in the sub-networks. 微信公众号：数学模型

3.3 Musical Inﬂuence Network Analysis Based on SNA

3.3.1 Establishment of Musical Inﬂuence Network and Analysis Using SNA

▶Establishment of Musical Inﬂuence Network

The directed graph can be well used to describe the mutual inﬂuence relationship among musicians. Based on the relationship between inﬂuencers and followers among musicians given by inﬂuence_data, we build a directed network of musical inﬂuence among musicians with each musician as a node and the directed inﬂuence among musicians as a weight.

Exploring the data reveals that the types of inﬂuence between musicians are divided into two categories: inﬂuence within the same genre and inﬂuence among different genres. Inﬂuence 微信号：MATHmodels among musicians exists not only that a predecessor inﬂuences a junior, but also that a junior inﬂuences a predecessor. Therefore, we classify the types of inter-musician inﬂuence as follows.

From genre span: Inﬂuence occurs within the same genre and between different genres.

From time span: Junior inﬂuences predecessor and predecessor inﬂuences junior.

Fully considering the difference between the span of genres and the span of time in which the inﬂuence occurs, we deﬁne the weight of each side of the music inﬂuence network:

• Time span impact factor

Assuming that existing musician i inﬂuences musician j, the time difference ∆t is deﬁned as follows: ∆t = t j −ti (1) where ti and tj are the debut times of musician i and musician j, respectively.

In general, juniors are more likely to be inﬂuenced by predecessors as they grow up, while predecessors are less likely to be inﬂuenced by juniors. Therefore, we can conclude that the probability of the older generation being inﬂuenced by the younger generation is lower. And if this happens, it means the inﬂuence of the younger generation is very strong. Compared to predecessors inﬂuencing juniors, juniors inﬂuencing predecessors should be considered that the juniors have a stronger inﬂuence. We therefore deﬁne the time-span inﬂuence factor T as follows { −β∆t, if ∆t < 0 T = (2) ∆t, if ∆t ≥0 In equation(2), β is a set parameter and β > 1, indicating the difference in the effect of the two inﬂuence categories.

• Genre span impact factor

Generally speaking, musicians in the same genre are more likely to inﬂuence each other because they share the same direction and research areas. In contrast, musicians from different genres are less likely to inﬂuence each other because their work styles rarely overlap. There- fore, we argue that cross-genre inﬂuencers have stronger inﬂuence compared to within-genre inﬂuencers. The genre-spanning inﬂuence factor aij between inﬂuencer i and follower j is given as follows:

关注数学模型 { 1, cross-genre aij = (3) 0, within-genre

• Edge weights of a directed graph 微信公众号：数学模型 Combining the above analysis on the time span and genre span impact factors, we give the formula for the directed graph weights wi j as follows:

T wij = (1+aij)·e (4) 80

In equation(4), wij is the weight of the directed edge between musician nodes i to j. The time interval |∆t| between the inﬂuencer and the inﬂuenced is at most 80, so T is normalized using T 80. wij also represents the intensity of the inﬂuence of musician i on musician j. The larger the value of wij, the stronger the intensity of musician i’s inﬂuence. ▶SNA Network Analysis Method

In order to capture the musical inﬂuence in the established musical inﬂuence directed net- work, we analyze the directed network using social network analysis (SNA) method[1]. The inﬂuence of each musician is measured and analyzed by calculating the Degree Centrality of 微信号：MATHmodels each musician in the musical inﬂuence directed network and further calculating the Eigenvector Centrality modiﬁed by the PageRank idea. The speciﬁc steps are as follows:

Step 1: Calculating Degree Centrality

In an undirected network, the degree of a node can be used to measure the centrality of that point. Analogously, in the music inﬂuence directed network we built, we can use the sum of the out-degree weights of a node to measure the importance of a node’s inﬂuence at the microscopic level. The assumption behind this metric is that nodes with many connections are important nodes, which means that musicians who have an impact on more people have a stronger inﬂuence. We therefore give the deﬁnition of degree centrality (DCi) for point i as shown in the equation(5) n ∑ DCi = wijdij (5) j=1 In equation(5) n represents the total number of nodes in the network and di j denotes the existence of directed edges between node i to node j. And di j is deﬁned as follows:

{ 1, no directed edge from i to j di j = (6) 0, there is directed edge from i to j Step 2: Calculating Eigenvector Centrality

The importance of a node depends both on the number of its neighboring nodes and on the importance of its neighboring nodes. This means that the more important the nodes connected to node i, the more important node i will be. We deﬁne the eigenvector centrality ECi to measure the importance of node i at the macro level, as shown in the iterative equation(7) n ∑ ECi = λ iterative equation: di jEC j (7) j=1

where lambda is a scaling constant and the initial value of the iteration is set in the equa- tion(8) j = 1 ∼n EC j = DC j, initial value: (8) However, for the directed network we build, the above analysis process only takes the im- portance of neighboring nodes into account. To increase the inﬂuence of the nodes themselves on the outside, we modify the equation based on the PageRank idea.

PageRank[2] is an algorithm proposed by Sergey Brin and Lawrence Page to rank the im-

portance of nodes in a network. The PageRank algorithm assumes that a node exerts inﬂuence关注数学模型 on the system is the result of its own inﬂuence combining with the results of its followers’ inﬂu- ences. Therefore, we modify the model shown in the following equation: Therefore, we modify the model shown in the following equation:

n 微信公众号：数学模型 ∑ ECi = λ di jEC j +(1−λ)ECi iterative equation: (9) j=1 After several iterations, ECi converges to a ﬁxed value E′ Ci. We deﬁne the musical inﬂuence (MIi) of musician i as follows:

E′ Ci MIi = (10) max{E′ C j, j = 1,2,··· ,n}

3.3.2 Model Test on Musical Inﬂuence Network

Using all data given in the inﬂuence_data, the musical inﬂuence (MI) of each musician is calculated, and the MI of somes musician are shown in the Table(2).

微信号：MATHmodels Musician MI Musician MI The Beatles Bob Dylan 1 0.738 The Rolling Stones Chuck Berry 0.546 0.5 Hank Williams Elvis Presley 0.424 0.424 Jimi Hendrix Little Richard 0.397 0.39 James Brown The Velvet Underground 0.387 0.356

As can be seen from the above table, The Beatles has the highest MI, followed by Bob Dylan, The Rolling Stones, Chuck Berry, Elvis Presley and so on. The similarity between the most inﬂuential musicians we analyzed and The 20 Most Representative Musicians in the World Jointly selected by CNN and Songlines[3] (a world-class music publication) is relatively high. We can conclude that the establishment and analysis process of the model is accurate, reasonable and feasible.

3.4 Analysis of The Result

Most real-world networks are not random networks, and a few nodes tend to have a large number of connections, while most nodes have only a small number of connections, generally obeying the Pareto Principle law[4]. Complex networks with degree distribution conforming to power-law distribution are usually called scale-free networks[5].

In section 3.2.3, we calculated the musical inﬂuence (MI) of each musician. A line graph of the frequency distribution of MI is plotted as shown in the blue solid line in the Figure(3).

关注数学模型 To investigate the nature of the MI distribution, we ﬁt the frequency distribution curve of MI. Observe that the distribution of MI in the ﬁgure resembles a power-law distribution, so the complementary cumulative distribution function of the power-law distribution is deﬁned as equation(11) 微信公众号：数学模型 P(X|X > x) = cx−a, c > 0,a > 0 (11) We solve for the power-law distribution parameters using the maximum likelihood estima- tion, and the distribution parameters at a conﬁdence level of 95% are shown in the Table(3).

distribution parameter estimated value 95% Conﬁdence interval c 0.001173 (0.0009809, 0.001366) α -1.526 (-1.565, -1.488)

With the goodness of ﬁt R2 = 0.9931, we can consider that the Musical Inﬂuence Network 微信号：MATHmodels is a scale-free network. Musical inﬂuence network obeys the law of Pareto Principle, i.e., only a small number of musicians inﬂuence many other musicians, while most musicians do not inﬂuence other musicians. This also means that a small number of highly inﬂuential musicians will have an impact on the music world. And this will be analyzed in detail in the subsequent analysis.

3.5 Analysis of Musical Inﬂuence Sub-network

In the model building process, we categorize time span and genre span: inﬂuence within genre, inﬂuence across genre, inﬂuence of predecessors on juniors, and inﬂuence of juniors on predecessors. We build independent sub-networks on genre and time span separately and use SNA analysis to explore each musician’s inﬂuence on predecessors and on juniors EIpre & EIjun, inﬂuence within and across genres EIwit & EIout. EIpre, EIjun, EIwit, and EIout are all subsets of the total inﬂuence EI.

The cross-genre inﬂuence data, within-genre inﬂuence data, predecessor inﬂuence data, and juniors inﬂuence data are selected from inﬂuence_data, respectively, to establish the musical inﬂuence sub network. Then the musical inﬂuences are calculated separately and normalized. The results of the calculation of each type of inﬂuence and the musical inﬂuence sub-network are shown in the Figure(4).

In the Figure(4), the size of nodes in each subnetwork represents the MI of the correspond- ing type of singer, while the thickness of the directed curve represents the weight of inﬂuence. As can be seen from the Figure(4), the occurrence frequency of inﬂuence within genres is higher than that between genres, and the occurrence frequency of inﬂuence of predecessors on their successors is higher than that of the latter on their predecessors. It can be concluded that in the interaction of musicians, musicians are more likely to inﬂuence musicians in the same genre, and musicians are more likely to inﬂuence younger generations rather than predecessors. It can also be seen from The MI subseries that The Beatles and Bob Dylan have a huge inﬂuence on musicians both in and out of The genre, and Bob Dylan goes one step further and has a strong inﬂuence on his predecessors as well.

关注数学模型 e

s 微信公众号：数学模型 Th Michael elin Mile Se g

nes

Intra-genre influence Cross-genre influence

T

G

erk W 微信号：MATHmodels g Stones Jimi H

nton Gordon h Boys E one Si

Predecessor influence junior Junior  influence Predecessor

4 TASK 2 & 3: Multi-dimensional Music Similarity Evalua-

tion Model

4.1 Model Overview

To adequately measure the similarity between the music, we evaluate the similarity between the music using cosine similarity and Euclidean similarity, respectively. The global similarity Sglobal between the music is ﬁrst calculated. We further explore the partial similarity Spart between music. Finally, the trend of the year when the music was released is considered to inﬂuence Stime. The multidimensional similarity evaluation between music is constructed to obtain the similarity between music. An overview of the model is shown in the Figure(5).

Multi-dimensional Similarity Evaluation

S global S time S part

Euclidean Metric Cosine similarity Cosine similarity

Songs feature vector element Years feature vector element Cosine similarity+Euclidean Metric

关注数学模型

4.2 Establishment of Multi-dimensional Music Similarity Evaluation Model

4.2.1 Global Similarity of Music

微信公众号：数学模型

• Euclidean similarity

The Euclidean similarity measure is based on the absolute distance between the feature vectors and is used to reﬂect the absolute difference in the feature values between the two songs. Then the distance between the eigenvectors of music A and music B distanceAB is deﬁned as √ follows: n ∑ (Ai −Bi)2 distanceAB = (12) i=1 Then the Euclidean similarity between music AB SE(A,B) is deﬁned by the following equa- tion: 1 SE(A,B) = (13) 1+distanceAB

• Cosine similarity

Different from Euclidean similarity, cosine similarity uses the cosine of the angle between 微信号：MATHmodels two vectors in vector space to measure the similarity between two vectors. The cosine similarity focuses more on the difference between the two vectors in terms of direction rather than the difference between the values. The cosine similarity between the eigenvectors of music A and music B Scos(A,B) is deﬁned by the following equation(14) n Ai ·Bi ∑ Scos(A,B) = 1+ cosθ A·B 2·||A||·||B|| = 1+ 1 i=1 √n √n 2 · = 1+ (14) 2 (A2 (B2 i )+ i ) ∑ ∑ i=1 i=1

The ﬁnal global similarity Sglobal between music A and B is deﬁned by the following equa- tion(15)

Sglobal(A,B) = SE(A,B)+Scos(A,B) (15)

4.2.2 Partial Similarity of Music

The global similarity measure between music is deﬁned above, and the high-latitude feature vectors containing all the music features are considered. But this does not fully reﬂect the sim- ilarities between the music. The similarity measurement of music should be multi-dimensional and separate measurements should be made between different characteristic dimensions of mu- sic. In fact, in life, music can be considered similar if it is similar in some aspects such as rhythm, emotional tendencies, and instrumentation, but not in all characteristics. At the same time, songs from the same genre are not similar in all characteristics but may be similar only in certain aspects. To weigh the similarity between the whole dimension and the partial dimension of music, we explore the local similarity of music from the micro point of view, in terms of each feature.

We randomly select two, three, and four features from the key features of music to form different feature vectors V. There are a total of N new feature vectors composed of the extracted features.

N = C2 12 +C3 12 +C4 12 +C5 12 = 1573

The new feature vectors are V (1),V (2),··· ,V (1573), respectively. For music i and music j, we

关注数学模型 ﬁrst calculate the Sglobal of each combination of their features and select the highest 50 Sglobal to calculate the average value as the partial similarity (Spart(i, j)) between music i and music j. Spart(i, j) is deﬁned in the equation(16).

50 Sglobal(V(k) ,V(k) j ) ∑ i 微信公众号：数学模型 k=1 Spart(i, j) = (16) 50

4.2.3 Fashion Trends Impact Factor

Considering that music is a literary and artistic product with strong social and cultural at- tributes, we should also consider the inﬂuence of the popular trend in the year of music release when analyzing the similarity of two pieces of music. Usually, the style of the song will evolve in the direction of the popular trend of the year. If there is a big difference in the popularity of the two songs in the year of their release, then the difference in melody and vocals between the two songs will change with the pop trends of the two songs in the year of their release.

Therefore, when measuring music similarity, the inﬂuence of pop trends on the music itself 微信号：MATHmodels should be reduced, so as to explore the intrinsic similarity of songs after stripping away the impact of pop trends. For the two songs released in year a and year b, we deﬁned the trend impact factor Stime as:

Stime = Sglobal(Yeara,Yearb) (17) Where Yeara and Yearb are the music style attribute vectors of year a and b, respectively.

In summary, we establish a multidimensional music similarity (MS) evaluation model con- sidering the inﬂuence of popular trends, deﬁned as follows, β is a parameter deﬁned later (0<δ<1). MS = ((1−δ)Sglobal +δSpart)·(1+ 0.1 ) (18) Stime

4.3 Evaluation of Music Similarity

We count the number of genres to which all inﬂuencers and followers belonged, and plot the following Figure(6) for each type of musician’s genre.

Influencer number of Main Genre Follower  number of Main Genre

Folk Folk Blues 81 85 Blues 79 88 1,779 2,676 Reggae Reggae 114125 111 Electronic 128 Vocal Vocal 147 135 Latin Latin 182 164 Country Electroni Jazz 351 c 273 R&B; Jazz 378 292 470 Pop/Rock 597

As can be seen from the Figure(6), Pop/Rock, R&B, and Jazz have the largest number of inﬂuencers, accounting for nearly 75% of all musicians. Therefore the subsequent analysis is based mainly on songs and musicians from these three genres.

• Similarity of Songs

关注数学模型 Pop/Rock Blind Faith So Alone Africa Long Cool Woman 微信公众号：数学模型 R&B Don’t Stop ’Til You ··· Thinking of You Long Way Go Who’s Loving You Jazz **** ’N Boogie What’s New Floatin Summer Breeze

We select four songs from Pop/Rock, R&B, and Jazz as shown in the Table(4) and then analyzed their similarity.

The established Multi-dimensional Music Similarity Evaluation Model is used to calculate the overall similarity Sglobal between each song and the similarity MS after adding the partial similarity Spart. Set δ = 0.5, the calculation results of Sglobal and MS are shown in the Figure(7) 微信号：MATHmodels and (8).

Pop/Rock R&B Jazz Pop/Rock R&B Jazz

1.00 0.39 0.30 0.49 0.52 0.60 0.32 0.47 0.28 0.17 0.45 0.34 1 0.58 0.55 0.69 0.57 0.64 0.47 0.5 0.33 0.27 0.43 0.36

0.39 1.00 0.23 0.33 0.33 0.37 0.24 0.41 0.23 0.15 0.29 0.29 0.58 1 0.4 0.58 0.46 0.46 0.35 0.49 0.23 0.22 0.29 0.28

0.30 0.23 1.00 0.38 0.36 0.34 0.63 0.26 0.47 0.27 0.36 0.37 0.55 0.4 1 0.59 0.46 0.47 0.66 0.38 0.47 0.34 0.41 0.4

0.49 0.33 0.38 1.00 0.62 0.63 0.39 0.42 0.33 0.19 0.47 0.39 0.69 0.58 0.59 1 0.64 0.5 0.46 0.52 0.33 0.27 0.42 0.37

0.52 0.33 0.36 0.62 1.00 0.64 0.38 0.44 0.32 0.18 0.48 0.38 0.57 0.46 0.46 0.64 1 0.75 0.55 0.65 0.31 0.26 0.41 0.36

0.60 0.37 0.34 0.63 0.64 1.00 0.36 0.47 0.30 0.18 0.45 0.37 0.64 0.46 0.47 0.5 0.75 1 0.56 0.7 0.33 0.27 0.41 0.37

0.32 0.24 0.63 0.39 0.38 0.36 1.00 0.26 0.48 0.26 0.40 0.37 0.47 0.35 0.66 0.46 0.55 0.56 1 0.46 0.48 0.34 0.45 0.38

0.47 0.41 0.26 0.42 0.44 0.47 0.26 1.00 0.24 0.15 0.34 0.30 0.5 0.49 0.38 0.52 0.65 0.7 0.46 1 0.24 0.23 0.31 0.3

0.28 0.23 0.47 0.33 0.32 0.30 0.48 0.24 1.00 0.26 0.34 0.39 0.33 0.23 0.47 0.33 0.31 0.33 0.48 0.24 1 0.46 0.53 0.49

0.17 0.15 0.27 0.19 0.18 0.18 0.26 0.15 0.26 1.00 0.19 0.21 0.27 0.22 0.34 0.27 0.26 0.27 0.34 0.23 0.46 1 0.41 0.38

0.45 0.29 0.36 0.47 0.48 0.45 0.40 0.34 0.34 0.19 1.00 0.35 0.43 0.29 0.41 0.42 0.41 0.41 0.45 0.31 0.53 0.41 1 0.48

0.34 0.29 0.37 0.39 0.38 0.37 0.37 0.30 0.39 0.21 0.35 1.00 0.36 0.28 0.4 0.37 0.36 0.37 0.38 0.3 0.49 0.38 0.48 1

Figure(7) shows the similarity between songs in each genre without the addition of Spart, and Figure(8) shows the similarity between songs in each genre with the addition of Spart. As can be seen from the ﬁgure that songs within the same genre have higher similarity scores between them. Comparing Figure(7) and Figure(8) with the part circled by the box (i.e., the similarity scores between songs and songs within the same genre), it can be found that: the similarity scores between songs of the same genre have increased after the introduction of the parital similarity of songs (Spart), while the similarity between songs of different genres has decreased. The addition of local similarity makes the measurement of musical similarity more accurate and reasonable.

Thus we can consider the discussion about local similarity in 4.2.2 to be accurate: that is, songs in the same genre may have high similarity in the characteristics of several di- mensions. Songs within the same genre can be distinguished from songs in other genres by a combination of several features.

关注数学模型 • Similarity of Musicians

We used the established Multi-dimensional Music Similarity Evaluation Model to calculate the similarity of Pop/Rock, R&B, and Jazz musicians within and between genres. The speciﬁc values are shown in the Table(5). 微信公众号：数学模型

Within genres Between genres Genres Pop/ROCK R&B Jazz Pop and R&B Pop and Jazz R&B and Jazz Average 0.659 0.683 0.627 0.647 0.560 0.592 Min 0.399 0.439 0.382 0.309 0.374 0.359 Max 0.917 0.906 0.916 0.949 0.869 0.898

Observing the Table(5), we can learn that the intra-genre artists of each genre are more similar than the similarity with the artists of other genres. Therefore we can assume that the artists within each genre are more similar than the artists between genres. At the same time, we can also see that the average similarity between POP and R&B artists reached 0.647, which is 微信号：MATHmodels very close to the average similarity within Pop. From this, it can be concluded that there may be more similarities between genres. To visualize the relationship between genres, we used PCA to downscale the characteristics of Pop/Rock, R&B, Jazz and plot the distribution of their musicians in three dimensions, as shown in the Figure(9).

Pop Pop/Roc R&B kR&B Jazz Jazz

As can be seen from the Figure(9), the artists in the genres are more similar, but there is no clear line of distinction between genres. This coincides with the conclusion of our analysis of the Table(5).

4.4 Analysis of the Musical Discrimination and Inﬂuences of Genres

4.4.1 Discrimination Evaluation Model of Feature Combination

Combining with the discussion of partial similarity in music in 4.2.2 and 4.3: songs between similar genres may do not share a high degree of similarity in all features, while the combination of several particular features may give music in the same genre a very high degree of similarity and thus distinguish it from music in other genres. Similarly, there may be a high similarity between different genres in the combination of certain characteristics.

To analyze what combination of features distinguishes a genre, we arrange and combine the

12 musical features except popularity in two-two, three-three, four-four, and ﬁve-ﬁve combina-关注数学模型 tions to obtain a total of N′ types of new feature combinations: V (1),V (2),··· ,V (1573) N′ = C2 12 +C3 12 +C4 12 +C5 12 = 1573 (19)

Based on the new combination V, the partial similarity Spart deﬁned by the equation(16) in 4.2.2 between the genres and the other genres is calculated. The minimum value of Spart is 微信公众号：数学模型 1 2, which represents the minimum local similarity. For the ith new feature combination V (i), a metric vector Spart I = [Spart 1,Spart 2,··· ,Spart 18]T is obtained by the partial similarity between the genre to be evaluated and other genres, as shown in the Figure(10).

Pop/Rock Blue Jazz . . . . . . Folk . . . . . . . . . . . . . . . . . . . . . Country Vocal 微信号：MATHmodels Muti-Similarity between Pop Valence & tempo and Vocal by [mode,key] Mode & energy & key mode & key

Spart i reﬂects the similarity of the genre between other genres when only the features con- tained within V (i) are considered. If the features contained within V (i) can well distinguish the genre from other genres, then these features can be considered as the signiﬁcant differences between the music of the genre and other genres. Ideally, if the combination of features cho- sen can completely distinguish the genre from other genres, then the optimal partial similarity 2]T is deﬁned. vector S′ part = [1 2, 1 2,··· , 1 Cosine similarity and Euclidean similarity are used to measure the discriminationi of feature combination vector V (i) discriminationi = Scos(S′ part,Spart i)+SE(S′ part,Spart i) (20)

We selected two genres, Electronic and Latin, for analysis, and obtained the top three dis- crimination scores as shown in the Table(6).

Feature combination Discrimination [acousticness, instrumentalness, speechiness]* 1.1588 [energy, acousticness, instrumentalness, speechiness]* 1.1588 Electronic [energy, acousticness, instrumentalness, liveness, speechiness] 1.1586 Feature combination Discrimination [energy, valence, tempo, danceability]* 1.1474 [energy, valence, loudness, danceability] 1.1473 Latin [energy, valence, tempo, danceability, liveness] 1.1470

As can be seen from the Table(6):

• For Electronic: Electronic is different from other genres in four aspects, including acous- ticness, instrumentalness, speechiness, and energy. These characteristics are in line with those of electronic-synth music, which has a strong sense of rhythm and is more likely to evoke the desire to dance.

• For Latin: Its concentrated characteristics are embodied in energy, valence, tempo,

关注数学模型 danceability, which coincide with the energetic, dynamic, rhythm-centered characteristics of

Latin music.

4.4.2 Analysis of Genre Changes Over Time

• Analysis of single genre changes over time

Take Electronic’s music characteristics change as an example. The analysis process is shown 微信公众号：数学模型 below:

Step 1: Data visualization

We use the four most distinguishing attributes of Electronic: acousticness, instrumentalness, speechiness, and energy, which are analyzed in 4.4.1. We add the number of musicians within the genre and the popularity to obtain six variables. The curves of these six variables over time are plotted as Figure(11).

1.2 1 energy 0.8 acousticness 0.6 value 0.4 instrumentalness 0.2 微信号：MATHmodels speechiness 0 1930 1940 1950 1960 1970 1980 1990 2000 2010 2020 Year 250 200 150 artist number value popularity 100 50 0 1930 1940 1950 1960 1970 1980 1990 2000 2010 2020 Year

Step 2: Identiﬁcation of mutation points

From the Figure(11), we can see that electronic music mutated in the 1950s and character- istics changed from 1970 to 1980. In total, it can be divided into three development stages: in the 1950s, 1970∼1980, and after the 1980s.

Step 3: Analysis with historical facts

1. In the 1950s, there were signiﬁcant changes in the variety of attributes of electronic music, from 0.93 to 0.10, and the score for acousticness, instrumentalness, iTunes, and energy increased by more than 200%. After the 1950s, electronic music became more intense and electrically enhanced. According to Wikipedia[6], the ﬁrst electronic music recorded on tape was composed by Louis and Bebe Barron in 1950, signifying the creation of true electronic music.

2. From the 1970s to the 1980s, there were a lot of innovations in electronic music equip- ment. Digital synthesizers and samplers replaced analog synthesizers, and more musicians could use a synthesizer for music creation.

3. After the 1980s, the Acid House movement in the UK pushed the development of elec- tronic music into the mainstream, and between the late 1990s and the beginning of the 21st cen- tury, electronic music using only electronic instruments became increasingly popular, a trend that continues today. Nightclubs around the world are playing electronic music on a regular basis.

• Analysis of correlation of changes between genres over time

We use Easy listening and New age as examples to analyze the interplay of genres during关注数学模型 their change over time. We choose three characteristics of acousticness, tampo, and speechiness of these two genres to analyze how they change over time.

eacy listening new age eacy listening new age eacy listening new age 0.08 0.6 1.2 微信公众号：数学模型 0.07 1 0.5 0.06 0.8 0.4 0.05 0.6 0.04 0.3 0.03 0.4 0.2 0.02 0.2 0.1 0.01 0 0 0 1921 1940 1959 1978 1997 2016 1921 1940 1959 1978 1997 2016 1921 1940 1959 1978 1997 2016 acousticness speechiness tampo

As can be seen from the Figure(12), both Easy listening and New age have a similar trend: acousticness gradually decreases, tempo stabilizes, and speechiness continues to decrease on top of the already low values. This is also in line with the development history of the real Easy listening and New age, that is, the rhythm is soothing, there is less spoken word, and gradually 微信号：MATHmodels introduced a small number of electronic instruments.

Exploring the sequential correlation between the changes of the two curves, we can also learn that the changes of New age always lag behind Easy listening and change in the direction of Easy listening changes. It can be further concluded that New age is inﬂuenced by Easy listening as it changes over time, which coincides with the fact that New age started later and is inﬂuenced by Easy listening.

5 Task 4 :Long-Short Term Inﬂuence Evaluation Model Based

on Sliding Window

5.1 Establishment of Sliding Window Model

To explore whether inﬂuencers inﬂuence the music created by followers, we evaluated the similarity between the music of inﬂuencers and followers by MS. Considering that the inﬂu- ence of followers by inﬂuencers changes continuously over time, we add sliding windows[9] to explore the short-term similarity MS of music based on the similarity evaluation model es- tablished in TASK 2 & 3, to capture the short-term inﬂuence STS of inﬂuencers on followers’ music. Finally, the magnitude of the change in short-term similarity is summed to obtain the long-term inﬂuence LTS of the inﬂuencer on the follower. An overview of the model is shown in the Figure(13).

We arrange the songs of inﬂuencers and followers by time, and as the window slides along the time line, new songs are added continuously on the right side, while some outdated songs are dropped on the left. We swipe two windows on the timelines of the works of inﬂuencers and followers at different times. Additionally, we ensure that the music in the inﬂuencer window is released earlier than the music in the follower window. Then calculate the similarity of inﬂuencer’s music and follower’s music MS in both windows.

In order to ﬁnd the most similar songs (songs with real inﬂuence relationships), we deﬁne the similarity of the song in the i th follower window to the inﬂuencer (MSi):

MSi = max{MS(Fli,In j), j = 1 to n} (21) Fli and In j are the music within the follower window i and the inﬂuencer window j, respec- tively. MS(Fli,In j) represents the short-term similarity of music within the inﬂuencer window j to music within the follower window i. To satisfy that the music within the inﬂuencer window

关注数学模型 is released earlier than the followers, n changes as i changes.

… … Follower

微信公众号：数学模型 Time Line

Muti-Similarity Maximum

Influencer …

… Time Line

Deﬁne the magnitude of similarity change (∆MS)i for the follower’s timeline window:

(∆MS)i = MSi −MSi−1 (22) MSi−1 微信号：MATHmodels Deﬁne short-term similarity (STS) and long-term similarity (LTS): { STS = max{(∆MS)i} (23) LTS = ∑(∆MS)i

We consider that when STS > 0.01, i.e., in the short term, there is a period of time when followers’ song styles are substantially closer to those of the inﬂuencers, and this is when the inﬂuencers can be considered to have inﬂuenced the followers. When LTS > 0, the follower’s music style is generally close to the inﬂuencer’s in the long run, and the inﬂuencer can be considered to have a long-term inﬂuence on the follower. Deﬁning the degree of inﬂuence long-term-short-term score IDS, when IDS > 0, the inﬂuencer can be considered to have an inﬂuence on the follower.

IDS = max(0,LTS)+max(0,STS−0.01) (24)

5.2 Test of the Established Model

We set the window size to 5 and the move step to 3 for window sliding detection. The IDS between all inﬂuencers and followers are calculated using the model developed above and ﬁnd that 86.08% of the IDS are greater than 0. It can be concluded that in general inﬂuencers do inﬂuence the music created by their followers.

We choose the inﬂuencer: Black Box, and his followers: Soda Stereo and Dave Matthews Band as an example, the results are shown in the Table(7).

Inﬂuencer Follower LTS STS IDS Black Box Soda Stereo 0.00033 0.01251 0.000334 Black Box Dave Matthews Band 0.00553 0.00549 0.00553

It can be seen that Black Box did inﬂuence the music making of its followers, Soda Stereo and Dave Matthews Band, to varying degrees.

• For Soda Stereo: STS≫LTS, the short-term impact is greater.Inspired by a few songs from an inﬂuencer and subsequently less inﬂuenced by the inﬂuencer.

• For Dave Matthews Band: LTS>STS, the long-term impact is greater. Dave Matthews

关注数学模型 Band has been inﬂuenced by inﬂuencers for a long time and is a loyal follower.

5.3 Contagious Evaluation of Musical Characteristics

Music has many different characteristics, and in order to explore whether there are more contagious (easy to spread) ones among different characteristics, we established a contagious 微信公众号：数学模型 evaluation system for music characteristics based on the timeline of inﬂuencers’ and followers’ works in the previous section, and the music similarity (MS) evaluation model in 4.2.1. For a speciﬁc musician (as a follower), the contagious evaluation steps of musical features v(k) are as follows.

Step 1: Build the timelines of the works of this musician (single) and his inﬂuencer (possibly multiple) respectively, as shown in Figure(13) (4.4.2).

Step 2: For a musician’s song i, it is combined with an inﬂuencer’s song j, and then calculate the difference dif(i, j)(k) of the musical characteristics v(k) of the two songs.

dif(i, j)(k) = v(k) −v(k) (25) i j Step 3: Musicians’ works may be inﬂuenced by only a relatively small number of enlighten- ing works, so there should be the smallest feature difference between them on v(k). We choose 微信号：MATHmodels the three smallest values of dif(i, j)(k) for weighted summation to obtain the difference DIF(k) i between the follower’s song i on feature v(k) and and its corresponding enlightening work. dif (k) 1 , di f (k) 2 , di f (k) for the ﬁrst three smallest characteristic differences. 3 = 1 + 1 + 1 DIF(k) 2dif (k) 3dif (k) 6dif (k) (26) i 1 2 3

Step 4: Analyze the contagion of all the features within this musician’s works. Deﬁne the degree of closeness DC(k) of all songs of a follower to the songs of its inﬂuencer on v(k). And D[d](k) is the variance of all songs of this musician on the feature v(k). The smaller the ﬁnal value of DC(k) is, the more susceptible the musician is to inﬂuencers on v(k), and the more contagious the v(k) is.

DC(k) = ((1+average(DIF(k) ))·(1+minimum(DIF(k) ))·D[d](k) (27) i i

Using the above analysis process, Soda Stereo and Dave Matthews are selected as followers for the contagious analysis of music characteristics, and the results are obtained as shown in the following Table(8).

speechiness energy instrumentalness Characteristics Soda Stereo DC 0.000249 0.0068 0.007554 Characteristic speechiness instrumentalness danceability 8.5279×10−5 9.6721×10−5 Dave Matthews DC 0.012702

As can be seen from the Table(8), not all characteristics are highly contagious to a particular musician, and the most contagious characteristics vary from one musician to another. For Soda Stereo, the musical characteristic speechiness is the most contagious. For Dave Matthews, the musical characteristics of speechiness and instrumentalness are the most contagious.

6 Task 5 & 6 & 7: Analysis of Music Revolution Over Time

6.1 The Identiﬁcation of the Musical revolution

We analyze the given data to identify musical revolutions in terms of two symbol: changes

关注数学模型 in existing musical genres, the creation of new musical genres.

• Changes in existing musical genres

Dramatic changes in musical characteristics within existing musical genres can be recog- nized as temporal musical revolution. The following are the conditions for determining the point in time when an evolution occurs: 微信公众号：数学模型 A. The musical characteristics of the genre remained stable before and after the revolution.

B. In the year of the revolution, the musical characteristics of the genre change greatly.

C. There are at least two features that have taken a signiﬁcant turn at the same time.

The above conditions are quantiﬁed using mathematical formulas to explore whether a sig- niﬁcant change occurs within a six-year period of analysis. For the characteristic v(k) of the genre, the condition for determining that an evolution occurs in the 3th ∼4th year of the analy- sis cycle is deﬁned by the equation(28)  |v(k) 3 −v(k)  2 | < 0.03     |v(k) 2 −v(k)   1 | < 0.03  |v(k) 4 −v(k) 微信号：MATHmodels (28) 3 | > 0.1    |(v(k) 5 −v(k) 4 )−(v(k) 4 −v(k) 3 )| < 0.02 or |v(k) 5 −v(k)  4 | < 0.03     |(v(k) 6 −v(k) 5 )−(v(k) 5 −v(k) 4 )| < 0.02 or |v(k) 6 −v(k) 5 | < 0.03 Using a six-year time span as the width of the sliding window, a sliding window model is used for analysis to identify the years in which the upper constraint is satisﬁed, i.e., the time when a revolution occurs. If the trend of change continues in the years following a turning point, we consider a long-term change to have occurred during that period. Electronic is selected as the study object to explore the characteristics of signiﬁcant revolution in Electronic. With the above constraint equation, we capture the year 1950 and 1969 as the time points of the revolution. And the characteristics of Electronic in 1950 and 1969 are shown in the Table(9).

Year 1950 1969 speechiness acousticness energy instrumentalness acousticness Characteristic Change 0.796 0.513 0.210 0.131 0.123

From the Table(9), it can be seen that Electronic in 1950 speechiness, energy and acous- ticness changed a lot. In 1969 instrumentalness and acousticness changed a lot. This is also similar to the conclusion of our analysis of Electronic in 4.4.2, and it can be considered that the established constraint equations can identify the revolution in the existing music genres.

• Creation of new musical genres

To identify the new generation of music genres, we visualize the number of musicians in each genre over time in Figure(14). Each surge in the number of musicians in each genre can be considered as an evolution in the genre. The ﬁrst surge in the number of musicians in each genre can be identiﬁed as the creation of a new genre.

Observe the Figure(14), using the analysis of R&B and Country as an example:

1. The ﬁrst explosion in the number of musicians in R&B occurred in 1950. There had not been an explosion in the number of musicians in the genre before that, so it can be argued that an evolution happened in 1950, when R&B was created. This also coincides with the start date of the R&B genre, according to Sound and Music from Xinhua News Agency[7].

2. The ﬁrst surge in the number of musicians in Country occurred in 1920, and it is also

logical to assume that Country had an evolution in 1920, when Country was born. The results关注数学模型 2500 Total musicians number Vocal Religious 2000 Reggae R&B; 1500 微信公众号：数学模型 Latin Jazz 1000

500 Electronic Country

0 Blues 1930 1950 1970 1990 2010 year

of the analysis are also consistent with the facts[7].

6.2 Major Inﬂuencers of Revolution

For a genre revolution, we analyze the music published within the genre in the two years 微信号：MATHmodels before and after the evolution, looking for the most popular artists during that part of the time. We sum the popularity of each musician’s works released during that period separately to obtain the popularity of each musician during that period, with the highest being the most inﬂuential in the evolution. Electronic is analyzed using the above method.

In 1950, Freestyle’s music has the highest sum of popularity: 144, can be considered as a major inﬂuencer on the 1950 evolution. In 1969, Jean-Jacques Perrey’s music has the highest sum of popularity: 139, can be considered as a major inﬂuencer for the 1969 evolution.

The trend of evolution in 1969 was maintained from the beginning of the evolution in 1969 to 1978, and we believe that a long-term change was produced during this period. We also identiﬁed the major inﬂuencers near 1969 to 1979 as Kraftwerk : sum of popularity=822, Yellow Magic Orchestra: sum of popularity=495, Vangelis: sum of popularity= 473.

6.3 Dynamic Inﬂuencer Evaluation Indicator

In the equation(24) in 5.1, we deﬁne IDS to measure the degree of inﬂuence that inﬂuencers have on their followers. As genres develop over time, there may be different key inﬂuencers within the genre at different times who will inﬂuence other musicians within the genre and lead the direction of the genre. To reveal the dynamic inﬂuencers within genre i, we deﬁne the Dynamic Inﬂuencer Indicator DII as follows.

For musician i, ﬁrst calculate its degree of inﬂuence IDSi,j on all musicians within the genre in turn and sum up IDS, to obtain the dynamic inﬂuencer index DIIi for musician i:

n ∑ DIIi = IDSi,j (29) j=1 Within this genre, the musicians are ranked according to the DII of each musician. From the analysis of the percentage of major inﬂuencers in 3.3, a point threshold of 20% is used based on the law of Pareto’s Principle[4]. Musicians with DII ranking in the top 20% are then identiﬁed as dynamic inﬂuencers within this genre. We take Pop/Rock as an example, taking ten years as the analysis period, the DII of musicians within the genre of every period is calculated, and we list the two largest DII after normalization of musicians every decade shown in the Table(10).

As can be seen from the Table(10), the dynamic inﬂuencers within Pop/Rock are not the same in different eras, which is a good indication of the turnover of leading ﬁgures within the关注数学模型 Year 1950s 1960s 1970s 1980s 1990s Musician Elvis Presley Bob dylan The Clash Sex Pistols Blur 微信公众号：数学模型 DII 0.9951 0.9926 0.9635 0.8964 0.9131 Musician Little Richard Beatles David Bowie Nirvana Beach Boys DII 0.9814 1 0.9804 0.8413 0.8971

genre. The recognition threshold of DII is 0.8127, and musicians above this threshold can be identiﬁed as dynamic inﬂuencers.

6.4 Inﬂuence from Social, Political and Cultural Aspects

Changes in musical genre attributes often reﬂect the social, political, and cultural aspects of the time to some extent. We explore the social and cultural changes of the time by analyzing the changes in musical attributes such as valence related to emotions and acousticness related 微信号：MATHmodels to the use of science and technology in the music inﬂuence network across genres.

• From the general trends in the music industry

Taking the analysis of the emotional tendency of music as an example, we count the emo- tional tendency valence statistics of several genres of music that account for a relatively large proportion of the genre as shown in the Figure(15).

0.9 0.8 0.7 0.6 0.5 value 0.4 Comedy/Spoken 0.3 Jazz 0.2 R&B; 0.1 Religious 0 1921 1931 1941 1951 1961 1971 1981 1991 2001 2011 year

From the Figure(15), we can see that the emotional tendency of most genre songs started to become negative in 1947 and then became positive after 1965. Combined with the historical fact that the African-American Civil Rights Movement started in 1950 and ended in 1970, African- Americans were oppressed by society prior to the Civil Rights Movement, and the musicians used music to express their long-held negative feelings. After the civil rights movement, the future of African-Americans became clearer and they used music to express their desire for a better life. Thus we can consider that the emotional tendencies of music can, to some extent, reﬂect the implicit tendencies of society, politics, and culture, and be used to predict social revolution.

• From trends in speciﬁc music genres

Take the analysis of Electronic characteristics over time in 4.4.2 as an example. As shown in the Figure(11) in 4.4.2, the acousticness of Electronic increased signiﬁcantly in 1950, and so did the energy. It can be considered that Electronic has become more energetic and dynamic, which is related to the fact that people were in the ecstasy of achieving victory in the anti-fascist关注数学模型 war after the Second World War in the 1950s. The cultural products of this historical period also fully reﬂect the optimistic and exciting social trends.

• From the listener’s reaction to the music 微信公众号：数学模型 In addition to the music itself, the connection between music and social development can also be glimpsed in the changes in listeners’ reactions to music. The trend of popularity in each category over time is plotted in Figure(16). It can be seen that there are more and more music listeners, which reﬂects the unprecedented increase in people’s ability to access information through the Internet as a result of the development of science and technology, making music accessible to a wider audience. This will further increase the inﬂuence of music on society, politics, and culture.

350 Vocal Religious 300 Total popularity 250 Reggae R&B;

200 Pop/Rock Latin 150 100 Jazz Electronic 50 微信号：MATHmodels 0 Blues 1921 1940 1959 1978 1997 2016 Year

7 Sensitive Analysis

7.1 Sensitive Analysis of Model in TASK 2

In Task 2 to build the Multi-dimensional Music Similarity Evaluation Model, we weight the local similarity Spart and the global similarity Sglobal to obtain MS:

MS = ((1−δ)Sglobal +δSpart)·(1+ 0.1 ) (30) Stime The different weights δ may affect the evaluation results of similarity. Therefore, we choose 12 pieces of music from 3 genres to study the effect of different δ on the results, and choose δ = 0.2,0.5,0.8 to obtain the results of MS as Figure(17).

Looking at the above Figure(17) we can see that a change in δ does not change the broad similarity results respectively. However, the number of the parameter can have some effect on some speciﬁc categories of music, resulting in changes in musical similarity between or within genres, respectively.

• When δ is small, we can see higher similarity between genres. And Sglobal has a large weight and pays more attention to the differences of songs in all characteristics, which leads to lower similarity within the genre.

• When δ is large, it can be seen that the similarity between genres is lower. Spart has a larger weight and pays more attention to the differences in important features of songs, which makes the the similarity within the genre become higher.

Therefore, we choose δ = 0.5 in the model of the main text to make our similarity evaluation more balanced between local and global features.

7.2 Sensitive Analysis of Model in TASK 4

In the sliding window model in Task 4, the size of the window and step size may lead to

different results. We use a variance-based sensitivity analysis method (Sobol method)[8] to关注数学模型 Pop/Rock R&B Jazz δ =0.5 Pop/Rock R&B Jazz Stash Old Treat Red Almaz Lady Halo **** Doxy Oleo Work Maria Stash 1.00 0.47 0.52 0.42 0.51 0.51 0.44 0.43 0.44 0.44 0.64 0.41 Stash Old Treat Red Alma Lady Halo **** Doxy Oleo Work Maria Old 0.47 1.00 0.39 0.52 0.40 0.51 0.57 0.56 0.34 0.35 0.45 0.37 Treat 0.52 0.39 1.00 0.36 0.51 0.43 0.39 0.37 0.49 0.58 0.56 0.44 Stash 1.00 0.65 0.69 0.60 0.68 0.68 0.62 0.61 0.59 0.60 0.72 0.51 Red 0.42 0.52 0.36 1.00 0.40 0.50 0.57 0.63 0.34 0.33 0.42 0.36 微信公众号：数学模型 Almaz 0.51 0.40 0.51 0.40 1.00 0.52 0.44 0.41 0.47 0.43 0.54 0.42 Old 0.65 1.00 0.59 0.67 0.57 0.66 0.71 0.70 0.49 0.51 0.58 0.44 Lady 0.51 0.51 0.43 0.50 0.52 1.00 0.63 0.57 0.41 0.39 0.49 0.40 Halo 0.44 0.57 0.39 0.57 0.44 0.63 1.00 0.72 0.36 0.35 0.43 0.38 Treat 0.69 0.59 1.00 0.55 0.68 0.63 0.58 0.57 0.62 0.68 0.67 0.53 **** 0.43 0.56 0.37 0.63 0.41 0.57 0.72 1.00 0.35 0.34 0.42 0.37 Doxy 0.44 0.34 0.49 0.34 0.47 0.41 0.36 0.35 1.00 0.51 0.43 0.35 Red 0.60 0.67 0.55 1.00 0.58 0.66 0.71 0.76 0.49 0.48 0.55 0.43 Oleo 0.44 0.35 0.58 0.33 0.43 0.39 0.35 0.34 0.51 1.00 0.45 0.37 Work 0.64 0.45 0.56 0.42 0.54 0.49 0.43 0.42 0.43 0.45 1.00 0.31 Alma 0.68 0.57 0.68 0.58 1.00 0.69 0.62 0.59 0.62 0.58 0.65 0.52 Maria 0.41 0.37 0.44 0.36 0.42 0.40 0.38 0.37 0.35 0.37 0.31 1.00 z Lady 0.68 0.66 0.63 0.66 0.69 1.00 0.76 0.72 0.57 0.55 0.61 0.49 Stash Old Treat Red Almaz Lady Halo **** Doxy Oleo Work Maria Stash 1.00 0.82 0.87 0.79 0.85 0.85 0.80 0.79 0.74 0.75 0.80 0.70 Halo 0.62 0.71 0.58 0.71 0.62 0.76 1.00 0.82 0.52 0.51 0.56 0.46 Old 0.82 1.00 0.78 0.82 0.74 0.81 0.85 0.84 0.63 0.67 0.71 0.62 Treat 0.87 0.78 1.00 0.80 0.86 0.83 0.78 0.76 0.75 0.79 0.78 0.73 **** 0.61 0.70 0.57 0.76 0.59 0.72 0.82 1.00 0.50 0.50 0.55 0.44 Red 0.79 0.82 0.80 1.00 0.76 0.82 0.84 0.88 0.64 0.63 0.69 0.59 Almaz 0.85 0.74 0.86 0.76 1.00 0.85 0.79 0.78 0.76 0.74 0.76 0.72 Doxy 0.59 0.49 0.62 0.49 0.62 0.57 0.52 0.50 1.00 0.69 0.63 0.59 Lady 0.85 0.81 0.83 0.82 0.85 1.00 0.89 0.86 0.73 0.72 0.74 0.69 Halo 0.80 0.85 0.78 0.84 0.79 0.89 1.00 0.92 0.68 0.68 0.69 0.64 Oleo 0.60 0.51 0.68 0.48 0.58 0.55 0.51 0.50 0.69 1.00 0.65 0.60 **** 0.79 0.84 0.76 0.88 0.78 0.86 0.92 1.00 0.66 0.66 0.68 0.61 Doxy 0.74 0.63 0.75 0.64 0.76 0.73 0.68 0.66 1.00 0.86 0.82 0.83 Work 0.72 0.58 0.67 0.55 0.65 0.61 0.56 0.55 0.63 0.65 1.00 0.56 Oleo 0.75 0.67 0.79 0.63 0.74 0.72 0.68 0.66 0.86 1.00 0.85 0.84 Work 0.80 0.71 0.78 0.69 0.76 0.74 0.69 0.68 0.82 0.85 1.00 0.80 Maria 0.51 0.44 0.53 0.43 0.52 0.49 0.46 0.44 0.59 0.60 0.56 1.00 Maria 0.70 0.62 0.73 0.59 0.72 0.69 0.64 0.61 0.83 0.84 0.80 1.00

微信号：MATHmodels investigate the effect on the results when multiple hyperparameters are varied simultaneously. The Sobol method simulates Monte Carlo sampling of the parameters in the feasible space and obtains a large number of outputs. The variance of the model output is the sum of all order variances of a single parameter. The equation for the contribution of the computed variance of the Sobol method is as follows:

p−1 p ∑ ∑ Vi j +···+V1,···,p V(Y) = i=1 j=i+1 (31) STi = EX∼i(VarXi(Y|X∼i)) = 1−VarX∼i(EXi(Y|X∼i) Var(Y) Var(Y)

The above equation measures the proportion of variance change caused by the interaction between one variable and other variables that change simultaneously. We then use the Sobol method on the sliding window model to study the sensitivity of window size and step size and show the sensitivity (ST) as Figure(18).

It can be seen that the change in the size of the window of followers has the greatest im- pact on the results, which can indicate that the number of music selected in the calculation of short-term inﬂuences has the greatest impact on the ﬁnal inﬂuence results. This represents that

for different musicians, when inﬂuenced by an inﬂuencer, different musicians may reﬂect the关注数学模型 inﬂuence of the inﬂuencer on several consecutive different songs. Some musicians may be in- spired only in the short term with only a small time period of songs reﬂecting this inﬂuence. While others may be inspired in the long term, with multiple songs over a long period of time reﬂecting the inﬂuence of an inﬂuencer on them. 微信公众号：数学模型

8 Strengths and Weaknesses

8.1 Strengths

• We used the theory of SNA to construct a network of inﬂuences between musicians and to measure the internal parameters of the network with more well-considered metrics.

• In analyzing whether inﬂuencers actually have an impact on followers, we used a sliding window time series approach to synthesize the short- and long-term impact of inﬂuencers on followers.

• We have done sufﬁcient visualization work on the algorithms and results of the model to facilitate understanding. 微信号：MATHmodels

• Most of our models are built with innovative ideas or improved based on original theories and speciﬁc problems, making our models both theoretical and innovative.

8.2 Weaknesses

• We could also go deeper into the analysis of certain issues, but due to space limitations, we can only stop here.

• Due to the lack of actual numerical reference, we can only observe the accuracy of our model from the actual situation and cannot numerically measure the accuracy of our model.

MEMO

To: Experts in The ICM Society 微信公众号：数学模型 From: Team 2107091 Date: February 8th, 2021 Subject: Analysis of Music Inﬂuence and Similarity, Suggestions for Futher Study

Dear experts in the ICM Society:

We are honored to inform you our achievement after performing data analysis and estab- lishing the music inﬂuence and similarity evaluation model.

Our team conducted a modeling analysis of the interactions between and within musicians across genres from 1921 to 2020. We develop a directed network for analyzing the interactions between musicians to understand the interactions that exist between musicians. An evaluation model to measure the similarity between the music is developed to provide an evaluation of the similarity between and within genres and to give the distinctive features of music in each genre. 微信号：MATHmodels An evaluation model based on a sliding window is developed to select the leaders of each genre in different time periods. With the model we developed, we obtained the following valuable conclusions:

• The inﬂuence of musicians on each other is consistent with Pareto’s Principle, which states that a very small number of musicians have inﬂuenced the vast majority of musicians. We can consider that a very small number of outstanding musicians led the entire music world, and in-depth exploration of the works of these musicians may deepen our understanding of music.

• Although there are differences between the genres, they are not completely independent but have no clear boundaries. As a carrier of human emotions, music has similarities among genres. The study of the evolutionary process of musical alternation and fusion among genres is conducive to enhancing our perception of the evolution of music as a whole.

• Changes in music can clearly reﬂect social change. Music is a tool for people to express their feelings, and by monitoring changes in musical emotions, we can probe into the pent-up emotions in society and thus make predictions about social revolution.

The model we developed still has limitations due to incomplete data and space limitations. We also need more data to achieve the following objectives

• We found that some of the artists are not common to both datasets, and some of the artists’ debut dates are unknown, which causes some inaccuracy in our analysis. We hope to obtain a more complete dataset of artists and music.

• If we know the speciﬁc year in which the followers were inﬂuenced by the inﬂuencer, then we can reﬁne the model for determining the contagiousness of music and whether it actually produces change by the change in the music of the follower before and after the year of inﬂu- ence. Also, the dynamic impact indicators of inﬂuencers can be reﬁned based on the change in the number of inﬂuenced people.

• If we know the album information where the song is located, then we can modify our sliding window model to capture the short-term impact by directly comparing the similarity between albums.

We expect to build a dynamic network in the future in the dimension of time and genre.We also hope to make a more detailed division in genre and to develop a set of visualization system in the future, to more describe the internal development. The above are the results of our team’s

关注数学模型 research, and we sincerely hope they can provide you with useful information and data.
