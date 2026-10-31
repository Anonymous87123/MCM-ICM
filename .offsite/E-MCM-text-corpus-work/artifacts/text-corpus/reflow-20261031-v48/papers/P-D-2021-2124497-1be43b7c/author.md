Summary

Music is a form of art that profoundly influences humans and societies. Given the four data sets, we are motivated to develop a series of objective measurements to analyze the music from four perspectives.

First of all, the measurement of music influence between artists is given by the combination of three indicators: 1) the indicator related to artists active in one certain decade being followed by artists active in other decades, 2) the indicator related to artists of one certain genre being followed by artists of other genres, and 3) the out-degree of the influencers. A weighted directed graph G(V, E) is constructed to represent the influence network, where an edge is directed from the influencer to the follower. Therefore, the calculated influence between the two artists is the weight of a directed edge.

Secondly, the music similarity is quantified. Since the provided data sets full_music_data contains high-dimensional data, thus the dimension reduction is needed. We are motivated to use the modified randomly distributed embedding (RDE) framework to take good advantage of interaction information of high-dimensional data. Moreover, the Bayes error rate is used to identify whether the distributions of within-genre and between-genre are significantly different.

Thirdly, we analyzed two kinds of roles of musical characteristics by examining the p-values from Kruskal-Wallis test. We removed each characteristic one at a time, and compared the p-values before and after the certain characteristics is removed. From the experiment results, the most influential characteristics in distinguishing genres are Energy, Valence, and Speechiness. The most contagious characteristics among artists are Acousticness, Danceability, and Valence.

Finally, we detected the most revolutionary artists by detecting the important nodes in the influence network using the modified closeness centrality (the synthesized centrality of in-closeness and out-closeness centrality). The calculated top 12 evolutionary artists are listed, including Bob Dylan, Chuck Berry, The Beatles, etc. In addition, the dynamic process of evolution is analyzed. By conducting discrete Fourier transform (DFT) and detecting the time series which is reconstructed from low-frequency components, we can observe the low-frequency components in a musical characteristic over time. An indicator σ is proposed to measure the proportion of low-frequency components among all the frequency components. Energy and Popularity have large σ values according to the experiment, meaning that there are rich low-frequency components in the time series of these two characteristics.

1 Introduction

1.1 Background

微信公众号：数学模型 Music has had a profound eﬀect on humans and societies throughout history. The evolution of music occurs constantly, inﬂuenced by advanced technology, personal experiences, social events, etc. The internal inﬂuence between artists also accounts for the music changes. Analysis of music is usually deemed relatively perceptual and subjective. However, music that is more abstract in itself can be quantiﬁed by various characteristics, which makes it possible for us to analyze the music systematically and objectively.

One of our goals in this paper is to develop appropriate measures to quantify the inﬂuence and similarity of music. Based on the quantiﬁcation, more thorough analyses could be conducted, including identifying the signiﬁcant artists and characteristics. We believe that a better understand- ing of the music evolved could be also be obtained with a series of carefully designed models and experiments.

微信号：MATHmodels

1.2 Restatement of the Problem

The analysis of music inﬂuence involves detail ranging from methods for quantiﬁcation to identiﬁcation of decisive factors. Thus, in order to analyze the inﬂuence of music in a clear and systematic way, we restate the problem as follows.

• Develop a measurement of music inﬂuence between artists, and construct a directed inﬂuence network that connects inﬂuencers and followers accordingly;

• Quantify the music similarities and compare the music similarities between and within genres;

• Testify whether there are signiﬁcant diﬀerences between the distributions of within-genre and between-genre similarities;

• Discover the decisive music characteristics that distinguish genres;

• Determine the most contagious music characteristics among artists;

• Identify the revolutionary artists, and analyze the evolution of music.

1.3 An Overview of Our work

To address the problem, this paper proposed ﬁve models to solve the respective sub-problems. The rest of the paper is structured as follows. Section 2 states a thorough problem analysis and our motivations. In Section 3, we give the assumptions and notations of the model. Section 4 provides suﬃcient details of our model. In Section 5, we test the proposed model. Section 6 analyzed the strengths and weaknesses of our model. At lat, a conclusion is given in Section 7. A one-page document to the ICM Society is given in the appendices???.

2 Problem Analysis

Based on the detailed information provided by the four data sets, we ﬁrst systematically analyze the problem. After exploring and reviewing the relevant literature research, we then construct a 微信公众号：数学模型 detailed model.

To begin with, the a directed network is required to be constructed from the inﬂuence_data data set. In inﬂuence_data, a detailed relationship between inﬂuencers and followers is given. For an inﬂuence network, an edge is directed from the inﬂuencer to the follower. Though a directed graph is easy to construct, a measurement of inﬂuence should be developed to describe the strength of the inﬂuence. Therefore, three factors are taking into account to measure the inﬂuence:1) the indicator related to artists active in one certain decade being followed by artists active in other decades, 2) the indicator related to artists of one certain genre being followed by artists of other genres, and 3) the out-degree of the inﬂuencers.

On top of that, the music similarity also needs to be quantiﬁed. An abundant amount of data are provided in full_music_data data set, and the quantiﬁcation of high-dimensional data is therefore 微信号：MATHmodels essential. Classical methods, such as the principal components analysis (PCA), are commonly used for dimension reduction. However, we are motivated to use the modiﬁed the randomly distributed framework (RDE) instead, which can take good advantage of interaction information provided by high-dimensional data. We also testify diﬀerence between the distribution of within-genre and between-genre similarities to justify whether the inﬂuencers indeed inﬂuence the followers.

Thirdly, we need to analyze roles of characteristics under diﬀerent circumstances. The inﬂuential characteristics are deﬁned to be the ones that are eﬀective in distinguishing the genres, and the contagious characteristics are deﬁned to represent the common inherent music features among artists. We are inspired to test the inﬂuence of a characteristics by comparing the p-values (obtained by conducting non-parametric test) before and after it is removed from other characteristics.

Afterwards, the artists who signify the revolutionaries is detected. Empirically, we assume that the revolutionary artists have great impact on others while receiving small inﬂuence from others. Therefore, we are motivated to calculate closeness centrality of the directed inﬂuence network, and use the diﬀerence between out-closeness and in-closeness centrality to measure how revolutionary an artist is.

Finally, the analyze of dynamic process of evolution is needed. With the date given in data_year, we aim at analyzing the evolution trend of each musical characteristics from the perspective of frequency domain. Therefore, we are motivated to conduct the discrete Fourier transform in order to observe the diﬀerent frequency components. Since it is not objective to observe the series by the curve shapes, we developed an indicator σ that measures the proportion of low-frequency components.

3 Model Assumptions and Notations

3.1 Assumptions and Justiﬁcations

• The musical characteristics chosen in the data set are representative;

• The data collected are reliable;

• The revolutionary artist are the ones who have large impact on others while receiving small inﬂuence from others;

微信公众号：数学模型

3.2 Notations

Symbol Deﬁnition G A directed graph describing the inﬂuence among artists

vi The ith node in the graph G

eij The edge in graph G directed from node vi to node vj wij The weight of edge eij

n0 The number of nodes in graph G

nj The in-degree of node vj

Iij The inﬂuence of inﬂuencer vi on follower vj 微信号：MATHmodels wij The weight on edge eij in graph G Sij The musical similarity between two nodes

ci The ith musical characteristics, i = 1, 2, ...13

Fi The set of labels of artists that followed artist vi

CCi(i) The in-closeness centrality of node vi

CCo(i) The out-closeness centrality of node vi

C(i) The synthesized closeness centrality of node vi

4 Model Construction

4.1 Measurement of Inﬂuence between Artists

According to the inﬂuence relationship revealed in the inﬂuence_data data set, a directed graph G(V, E) can be constructed, where V is a set of nodes and E is a set of links directed from one node to another. Let n0 be the number of nodes (the number of artists mentioned in inﬂuence_data). The n0 nodes are labeled from v1 to vn0, and eij denotes the edge directed from vi to vj. For each follower vj, let nj represent its in-degree (i. e. the number of artists that inﬂuence vj). A subgraph showing the relation among one follower and its inﬂuencers is illustrated in Fig. 1.

In a addition to construct a directed network by simply connecting the inﬂuencer to the follower, we aim at measuring the inﬂuence by three indicators from the perspective of a pair of the follower and inﬂuencer on edge eij: 1) frequency ekij that indicates the inﬂuence according to the period where inﬂuencer vi and follower vj are active, 2) frequency emij that describes the inﬂuence due to 微信公众号：数学模型

the main genres of inﬂuencer vi and follower vj, and 3) the out degree Oi of the inﬂuencer vi. To better explain the three indicator, more explicit deﬁnitions of ekij and emij are given as follows. 微信号：MATHmodels Let Di be the decade when the artist vi begin his or her music career. For inﬂuencer vi and follower vj on edge eij, kij is deﬁned to be the total number of times that artists in period Di are followed by artists in period Dj.

Deﬁnition 4.1. For edge eij that is directed from inﬂuencer vi to follower vj, the indicator ekij is deﬁned as:

kij ekij = (1) P l∈Sj klj

where Sj is the set of labels of inﬂuencers of follower vj.

Similarly, let Ri be the main genre of artist vi. Then mij is deﬁned as the total number of times that artists of genre Ri are followed by artists in genre Rj. Deﬁnition 4.2. For edge eij that is directed from inﬂuencer vi to follower vj, the indicator emij is deﬁned as: mij emij = (2) P l∈Sj mlj

where Sj is the set of labels of inﬂuencers of follower vj.

Applying the data from inﬂuence_data), the ekij and emij for inﬂuencers and followers of each type (including the decade when they began their music career and their main genres) are shown in

Therefore, the inﬂuence Iij of inﬂuencer vi on follower vj should be able to aggregate the data and information provided by the three indicators, i. e. ekij, emij and Oi. Deﬁnition 4.3. The inﬂuence Iij of inﬂuencer vi on follower vj on edge eij is deﬁned as:

Iij = ekij · emij · Oi (3) 微信公众号：数学模型 (a) The indicator kij

微信号：MATHmodels (b) The indicator mij

followers, where the vertical axis denotes the decade when the followers began their music career, and the horizontal axis denotes the time interval of the decade of followers and inﬂuencers. (b) The indicator mij for any pair of inﬂuencers and followers, where the vertical and horizontal axes represent the main genre of the followers and inﬂuencers, respectively.

Here, in Example 1, we give a brief example to better illustrate the calculation of inﬂuence emij (the indicator ekij can be calculated by using the exact same method). Since the number of inﬂuencer is huge and the out-degree Oi for the inﬂuencers in each edge can be easily found out from the data set, we will avoid displaying the cumbersome data here.

Consider an inﬂuencer vi and a follower vj whose main genres are Avant_garde Example 1 and Classical, respectively. Through the statistics in inﬂuence_data data set, the total number of times for artists of genre Classical to be inﬂuenced by artists of genre Avant_garde is 11, i. e. mij = 11. Additionally, there are in total 37 artists of various genres being followed by the artists of genre Avant_garde. Therefore, it can be calculated that the indicator emij between these two artists is emij = 11/37 ≈0.2973. It should be noted that the emij remains the same for any pair of inﬂuencer and follower whose genres are respectively Avant_garde and Classical.

By employing the calculation method illustrated in Example 1, let the weight wij of each 微信公众号：数学模型 directed edge in graph G be the quantiﬁed inﬂuence Iij (i. e. wij = Iij). Therefore, a weight matrix W is obtained, and graph G can be extended to G(V, E, W ). Fig. 3 demonstrated the overall structure of graph G.

微信号：MATHmodels

nodes are Bod Dylan and The Beatles, whose subnetwork is presented in Fig. 4

In Fig. 3, the color of nodes represent the genre they belong to, and the thickness of an edge denote the its weight (the thicker the edge is, the larger its weight is). Fig. 3 gives a rough distribution of genres and inﬂuence among artist, but is hard to discover details from. To give a better insight into the inﬂuence among artists, a subnetwork shown in Fig. 4 is provided.

4.2 The Music Similarity

With an abundant amount of data regarding the music-related characteristics, it is essential to develop a measurement to quantify the similarity with these high-dimensional data. Moreover, it is also of great importance to analysis whether the genres are distinguishable according to the similarity measurement that we developed. In this section, we proposed a modiﬁed randomly distributed embedding (MRDE) framework to measure the music similarity, which takes good advantage of interaction information among high-dimensional data. Afterwards, we analyze the similarity distribution between and within genres to identify whether the diﬀerence between within- genre similarity and between-genre similarity is signiﬁcant. Finally, we test the eﬀectiveness of the proposed measurement of inﬂuence in Section 4.1 by analyzing the similarity distribution among artist who do or do nor have mutual inﬂuence.

微信公众号：数学模型

微信号：MATHmodels

4.2.1 Quantiﬁcation of Similarities Based on the MRDE Framework

In this section, we demonstrate our model for quantifying the musical similarity. The proposed MRDE framework is explained carefully, and the quantiﬁcation result is then given and visualized.

To begin with, a brief introduction of the original RDE (randomly distributed embedding) framework is given. The RDE framework is ﬁrst proposed by Ma et al. in 2018 published on PNAS [1]. When dealing with high-dimensional data, dimension reduction techniques are usually applied, but the application is likely to overlook the interactions among high-dimensional variables. To make good use of the interaction information, the RDE framework builds a distribution of a suﬃcient number of embeddings of low-dimension. While each low-dimensional embedding preserves a part a information of the whole system, these low-dimensional embeddings form a probability distribution which can be used to obtain the ﬁnal one-dimensional variable (or the value). Readers could refer to more details in [1]. Hence, we proposed the MRDE framework to adapt the original RDE framework for the problem discussed in this paper, which provides another perspective for the comprehensive evaluation.

Among the fourteen musical characteristics summarized in data_by_artist, we eliminate the factor count for the experiment in this section, since count is not music-related and do not provide any information about an artist’s music style. Then we are left with 13 musical characteristics from danceability to popularity. In the MRDE framework, we choose the embedding dimension e to be e = 3 empirically according to the experiment in [1]. In other words, for each 3-dimension embedding, we randomly choose 3 characteristics out of the 13 musical characteristics. There are in total q kinds of combination of the chosen 3 characteristics, which can be calculated by Eq. (4).

E  q = (4) e

where E = 13 is the total number of musical characteristics involved in the analysis, e = 3 is the embedding dimension.

Each of the 13 musical characteristic is label from c1 to c13. For each 3-dimensional embedding, we construct an index tuple l = (l1, l2, l2), (lk = 1, 2, ...13, k = 1, 2, 3), where l1, l2 and l3 are Let Cj represent the tuple of values of 3 chosen the indexes of characteristics in this tuple. characteristics for node vj, then the three characteristics of artist vj is represented as Cj = 微信公众号：数学模型 (cl1, cl2, cl3).

When measuring the similarity between artist vi and artist vj, we need to ﬁrst identify their rough similarity calculated by each embedding. For the kth 3-dimensional embedding (k=1, 2, ..., q), we deﬁne its rough similarity srk as

srk = 1 −∥Ci −Cj∥2 (5)

Let Sr be the random variable where srk(k = 1, 2, ..., q) are the speciﬁc value. Therefore, the q rough similarity labeled from sr1 to srq can form a probability distribution. The actual similarity Sij between vi and vj is deﬁned as the expectation value of the distribution, formulated in Eq. (6).

Sij = E(Sr) (6) 微信号：MATHmodels where Sij ∈[0, 1], and E(Sr) is the expectation of random variable Sr. When Sij is large, it indicates that the these two artist are more similar, and vice versa.

By using Eq. (5) and Eq. (6), the similarity Sij between vi and vj can be calculated. The proposed MRDE framework can be better illustrated by the following steps:

Step 1: Randomly choose q tuples. Each tuple contains 3 index numbers denoted as l = (l1, l2, l2), and the musical characteristics in this tuple are denoted as (cl1, cl2, cl3);

Step 2: For the q tuples (namely the 3-dimensional embeddings), calculated the rough similarity srk, k = 1, 2, ..., q by using Eq. (5);

Step 3: Aggregate the rough similarities calculated in each embedding to form the probability distribution of the random variable Sr;

Step 4: Given the distribution of Sr, obtain the similarity Sij = E(Sr) by calculating the expec- tation value of random variable Sr.

A undirected network G1(V1, E1) is constructed, where V1 is the set of nodes and E1 the set of undirected edges. Since nodes being analyzed are the same as in G, so the label of nodes remain the same (such v1, v2 etc.). It should be noted that even though Eq. (6) and Fig. ?? measures the musical similarity between two artists, the proposed MRDE scheme can also be applied to quantify the musical similarity between genres and songs, as long as the musical characteristics are available.

Discussion

In the original data_by_artist data set, the order of magnitude of each musical characteristics varies from −6 to 5 . However, since the Euclidean norm is used to measure the rough similarity, the inﬂuence of order of magnitude must be eliminated as much as possible before calculating the Euclidean norm. Thus, the min-max normalization is utilized to normalize each characteristics. All of the normalized value of musical characteristics range from 0 to 1. Moreover, when we apply √ 3. Thus, the calculated the 3-dimensional embedding, the maximum value of rough similarity is √ 微信公众号：数学模型 similarities Sij are reduced to 1/ 3 of the original scale.

4.2.2 Distribution of Similarities Between and Within Genres

From Section 4.2.1, we have obtained the similarity between every two artists. From the inﬂuence_data data set, we can easily label each artist with his or her main genre. Therefore, the similarity distribution among artists can easily be transformed into similarity distribution between and within genres. From our intuitive understanding, we would assume that the similarity within genres are smaller than between genres. We might assume that the similarity between genres might also varies. For instance, the genre of Electronic and Country may diﬀer from each other from our daily experience. In this section, we will use the similarity distribution, Gaussian ﬁtting and Bayes error rate for a thorough analysis.

微信号：MATHmodels Among the 19 genres (the genre Unknown is eliminated due to the possible interference of  19  wrong or missing information), there are in total kinds of combinations. Fig. 5 is an example 2 of the similarity distribution within the genre Folk and between Folk and Reggae.

within the genre of Folk, while the red part denotes the distribution between Folk and Reggae. The vertical axis represents the number of times that a certain value of similarity appears in the total calculated similarities, and the horizontal axis represents the similarity ranged from 0 to 1.

From Fig. 5, we can have an intuitive understanding that the similarity distribution within and between genres is diﬀerent in the given example. But now a question arises: how can this diﬀerence be measured?

We are motivated to measure the above-mentioned diﬀerence by using Bayes error rate. Bayesian decision theory can address the patter classiﬁcation problem from the perspective of statistics [2].

The theory quantiﬁes the trade-oﬀbetween the decision made and the costs that accompany the decision. Bayes error, on the other hand, is the lowest possible error rate for a pattern classiﬁcation problem [3]. Let class ω1 denote the within genres, class ω2 denote the between genres, and s denote 微信公众号：数学模型 the similarity value. P(ωi|s), i = 1, 2 is the posterior probability. For the distribution illustrated in Fig. 6, the probability of error can be calculated by Eq. (7).

( P(ω1|s) whenP(ω2|s) > P(ω1|s) P(error|s) = (7) P(ω2|s) whenP(ω1|s) > P(ω2|s)

The Bayes error rate is therefore formulated in Eq. (8).

Z ∞ Z s0 P(ω2|s)p(s)ds + P(ω1|s)p(s)ds P(error) = (8) −∞ s0

where s0 is a certain point on the horizontal axis shown in Fig. 6 that divides the space into two parts. P(error) can also be denoted as the size of shadow area. 微信号：MATHmodels Due to the large scale of data, we demonstrate some typical similarity distribution here. First of all, Fig. 7 shows the similarity within and between the genres of Country and Eletronic.

From Fig. 7, it can be observed that the overall similarity within Country is much smaller than the one within Electronic and between these two genres. The results indicate that value of musical characteristics of artists of genre Country are highly similar, whereas the ones of artists of genre Electronic are relatively scattered. Moreover, by performing Gaussian ﬁtting, the estimated distribution for within the genre Country, within the genre Electronic and between the two genres are N(0.85, 0.06), N(0.74, 0.0.8) and N(0.75, 0.09), respectively. With the Gaussian ﬁtting results, the Bayes error of distributions in Fig. 7(a) and Fig. 7(b) are 0.486 and 0.916, respectively, indicating again that the similarity distributions in Fig. 7(a) are more diﬀerent and distinguishable.

In order to have an overall understanding of the similarity within and between genres, Fig. 8 shows the similarity distribution by combining all the values of similarity within each genre and between every two genres.

The Gaussianﬁttingresultofthewithin-genreandbetween-genredistributionareN(0.806, 0.078) and N(0.758, 0.095), respectively. The Bayes error rate calculated is 0.770. Combining the vi- sualization result in Fig. 8, the Gaussian ﬁtting result and the calculated Bayes error rate, we can 微信公众号：数学模型 (a) The similarity within Country and between genres (b) The similarity within Electronic and between genres

微信号：MATHmodels blue curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result between Country and Electronic. The light orange and orange curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result within Country. (b) The light blue and blue curves denote the same thing as in subgraph a. The light orange and orange curves denote the uniformed similarity distribution and the corresponding Gaussian ﬁtting result within Electronic.

reach a conclusion: 1) the similarity between genres is generally larger than within genres, and 2) the smaller the between-genre similarity is, the less similar are the corresponding two genres.

4.2.3 Test the Measurement of Inﬂuence by the Similarity Network

In section 4.1, the measurement of inﬂuence among artists is proposed. In Section 4.2.1, we quantify the similarities of musical characteristics. To discover the interaction relationship between the above-mentioned two measurements, we conduct another experiment by combining the directed network G of inﬂuence and the undirected network G1 of similarities. The experiment is aim at detecting whether the measurement of inﬂuence in Section 4.1 can actually reﬂect the real-world inﬂuence among artists.

First of all, we will explained how the combination works in this paper. Basically, we will reallocate the similarity distribution in G1 in to two distribution, based on whether two artists have unilateral or mutual inﬂuence on each other in graph G. Let S1 and S2 be two random variables, where S1 denotes the similarity distribution of edges in G1 that are connected in graph G (the directed graph describing the inﬂuence), and S2 denotes the similarity distribution of edges in G1 that are not connected in graph G.

Step 1: Start traversing all edges in the undirected similarity network G1;

Step 2: Consider an undirected edge that connect node vi and vj. If there exists a directed edge in the inﬂuence network G directed from vi to vj or from vj to vi, then the similarity value Sij on this undirected edge is a possible value of the random variable S1;

微信公众号：数学模型

微信号：MATHmodels that concludes the between-genre similarity of any combination of two genres. The light blue and blue curves denote the distribution that concludes all the within-genre similarity of every genre.

Step 3: Consider the same edge in Step 2. If no directed edge exists between vi and vj in graph G, then the similarity value Sij is a possible value of the random variable S2;

Step 4: Repeat Step 2 and Step 3 until all the undirected edges in graph G1 have been traversed;

Step 5: Compute the distributions of random variables S1 and S2.

The visualization of distributions of the two random variables are displayed in Fig. 9.

when there is no inﬂuence between to artists. The light blue and blue curves denote the distribution when two artists are unilaterally or mutually inﬂuence by each other.

The GaussianﬁttingresultforthedistributionofS1 andS2 are N(0.830, 0.067)andN(0.781, 0.076), respectively. The Bayes error rate is 0.6452. The overall similarity between the artists who uni- laterally or mutually inﬂuenced one another is signiﬁcantly larger than similarity of artists that did 微信公众号：数学模型 not inﬂuence each other. The result demonstrates that the similarity of artists who have a inﬂuence relationship is in fact larger than the artists who do not. That is to say, the identiﬁed inﬂuencers indeed inﬂuence the respective followers from a statistical perspective.

4.3 The Roles of Characteristics

When measuring the music similarity, we have combined the information of 13 musical char- acteristics to form the quantiﬁcation. However, what remains unknown is the roles that diﬀerent musical characteristics plays in inﬂuencing the music. In other words, we wish to identify the one or several characteristics that are signiﬁcant in distinguishing the genres. We also analyze which characteristics indicate the more general inherent features among artists. In this section, we ﬁrst deﬁne the central node in each genre. Then we eliminate the characteristics one at a time or one by one, and conduct the non-parametric test to identify the roles of characteristics. 微信号：MATHmodels

4.3.1 Characteristics that Distinguish Genres

Due to the lack of synthesized data for each genre, we ﬁrst synthesize the information about musical characteristics by deﬁning the central nodes. Then the Kruskal-Wallis test is utilized to identify the most inﬂuential characteristics that distinguish genres.

The Central Nodes of Each Genre:

We assume that each node in one genre is accounted for a certain percentage when deciding the central node of this genre. The percentage of node vj is denoted as Pj, formulated in Eq. (9).

P k∈Fj IjkSjk Pj = (9) Oj

where Fj is the set of labels of artists that follow artist vj. Ijk and Sjk denote the inﬂuence and similarity between vj and vk, respectively.

Let Ri be the set of labels of nodes that belong to the ith genre, where i = 1, 2, ...19. Let Chi represent the 13 musical characteristics of the central node of the ith genre, then Chi is deﬁned in Eq. (10).

P j∈Ri Pj · Cj Chi = (10) P j∈Ri Pj where Cj is the vector of 13 musical characteristics of node vj.

We can then obtain the 13 musical characteristics of central nodes of each genre by using Eq. (10).

The Most Inﬂuential Characteristics:

Let M1 be the 19 × 13 matrix, where each row stores the vector of 13 musical characteristics of the central node of each genre. M1 is formulated in Eq. (11).

  Ch1 Ch2   微信公众号：数学模型 M1 = (11) ...

Ch19

where Chi represents the 13 musical characteristics of the central node of the ith genre.

The uniformed values of matrix M1 is visualized in Fig. 10. For each column in Fig. 10, the corresponding characteristics has a great inﬂuence in distinguishing genres if the colors of each cube demonstrates a greater variability. We could roughly observe that the values of characteristics of Energy, Valence, Speechiness varies to a large extent, while values of Acousticness, Instrumen- talness have relatively concentrated distribution. We will test the rough conclusion by conducting Kruskal-Wallis test on these 5 characteristics in the following part.

微信号：MATHmodels

The Kruskal-Wallis test is a non-parametric test that can assess the the signiﬁcant diﬀerences by two or more groups of variables [4]. The null hypothesis H0 and the alternative hypothesis H1 are deﬁned. The null hypothesis represents no eﬀect or no diﬀerence, while the alternative hypothesis denotes the presence of an eﬀect or a diﬀerence [5]. A p−value is the probability that assumes H0 is true. Namely, the smaller the p-value, the strong the evidence evidence against the null hypothesis.

By the most inﬂuential characteristics, we mean that theses characteristics play important roles in distinguishing the genres. In other words, the similarity between genres will signiﬁcantly increase once theses characteristics are removed from matrix M1. Therefore, we removed each one of the 13 columns in M1, and calculate the respective p-value before and after the elimination. The Kruskal-Wallis test is applied in calculating the p-value. The typical p-values calculated are presented in Table 2.

The removed characteristics Energy Valence Speechiness Acousticness Instrumentalness 微信公众号：数学模型 p-value before elimination 0.1284 0.1284 0.1284 0.1284 0.1284

p-value after elimination 0.6500 0.5319 0.3057 0.0086 0.0035

* The p-values in the second row denote the non-parametric results before elimination. The p-values in the third row is the result after the characteristics of this column has been eliminated.

From Table 2, the result shows that after eliminating Energy, Valence and Speechiness, the p-value increases signiﬁcantly, meaning that the similarity distributions of each genre become less diﬀerent after the elimination. Therefore, Energy, Valence, Speechiness are inﬂuential character- istics in distinguishing genres. The experiment result analysis is similar for other characteristics. On the other hand, the p-values become extremely small after eliminating Acousticness and Instru- mentalness, meaning that these two characteristics are distributed similarly among genres. We can 微信号：MATHmodels conclude that Energy, Valence and Speechiness are the relatively inﬂuential characteristics, while Energy is even more inﬂuential than other inﬂuential characteristics.

4.3.2 The Contagious Characteristics among Artists

In the last section, we discussed how inﬂuential the characteristics are when distinguishing the genres. In this section, we aim at discovering how Contagious the characteristics are when deciding the musical style of various artists.

The Selected Artists:

Since there are in total 5854 artists in the data_by_artists data set, it is neither practical nor necessary to perform the Kruskal-Wallis test among all the available artists. Therefore, we selected the top 25 artists who have the highest Pj value (who accounted for more percentage when deciding the central nodes) introduced in Section 4.3.1. Let M1 be the 25 × 13 matrix, where each row stores the vector of 13 musical characteristics of the central node of each genre. M1 is formulated in Eq. (11).

  Ch1 Ch2   M2 = (12) ...

Ch25

where Chi represents the 13 musical characteristics of the central node of the ith artists.

The Most Contagious Characteristics:

Diﬀerent from the level of characteristics inﬂuence in Section 4.3.1, we deﬁne the characteristics to be Contagious when they represent the common inherent features of artists’ musical styles. Following the idea of non-parametric test in Section 4.3.1, the Kruskal-Wallis test can also be used here to measure the level Contagious. The adapted method is illustrated as follows:

Step 1: For the 13 musical characteristics, calculate the corresponding 13 p-values. Each p-value is obtained by conducting Kruskal-Wallis test when the certain one out of 13 characteristics is temporally removed;

Step 2: Pick out the smallest p-value in step one and eliminate the respective characteristics per- 微信公众号：数学模型 manently from M2. Name the characteristics as the most contagious characteristics;

Step 3: For the rest 12 characteristics, repeat the process in Step 1 and Step2. The characteristics that was picked out and eliminated is named as the the second most contagious characteristics;

Step 4: Repeat the process described from Step 1 to Step 3, until all the 13 characteristics have been sorted with an order.

Due to the limited length of the article, we will only demonstrate the 4 most contagious characteristics calculated from the above steps. Moreover, among the 25 artists we chose, their characteristics Mode all possess the value 1. Since Mode is apparently the same for all the selected artists, it can be deemed as the most contagious characteristics. Table 3 listed the p-values of the 微信号：MATHmodels other 3 most contagious characteristics before and after they are eliminated.

The removed characteristics Acousticness Danceability Valence

p-value before elimination 0.7786 0.2631 0.0326

p-value after elimination 0.2631 0.0326 0.0205

* The p-values in the second row denote the non-parametric results before elimination of the characteristics of the corresponding column, while the third row denotes results after elimination.

From Table 3, we can draw a conclusion that Mode, Acousticness, Danceability and Valence are the most contagious characteristics among artists, while the Mode and Acousticness have the highest and the second highest level of contagiousness. The Danceability and Valence are the third and fourth most contagious characteristics, respectively. Since the smaller p-values represent larger signiﬁcant diﬀerence, our experiment results are valid because: the elimination of our discovered contagious characteristics will lead to signiﬁcant reduction of the p-value, indicating that characteristics have more concentrated distribution after the contagious characteristics are removed. The results is in correspondence with our deﬁnition of contagiousness.

4.4 Revolutionary Artists Based on Closeness Centrality

By revolutionary artists, we generally mean that their contribution to the ﬁeld should be signiﬁcant. Moreover, they ought to have great impact on others while receiving small inﬂuence from others. Inspired by the structure of the inﬂuence network G constructed in Section 4.1, we apply the evaluation of important nodes in discovering the revolutionary artists. To be more speciﬁc, we combine the in-closeness and out-closeness centrality to evaluate the signiﬁcance of an artists in revolutionaries. Our goal is to discover the artists with small in-closeness centrality and large out-closeness centrality.

For the inﬂuence network G(V, E), the closeness centrality CC(i) of node vi is the average farness to all the other nodes in the network, formulated in Eq. (13).

n −1 微信公众号：数学模型 CC(i) = (13) P j̸=i d(i, j)

where n is the number of nodes in graph G.

Since closeness is a directional measure in the directed graph, the in-closeness centrality CCi(i) and the out-closeness centrality CCo(i) can be calculated accordingly. To evaluate the inﬂuence of the evolutionary artists who have large out-closeness centrality and small in-closeness centrality, the synthesized closeness centrality of artist vi is deﬁned in Eq. (14).

C(i) = CCo(i) −CCi(i) (14)

The synthesized closeness centrality of the top 12 artists are shown in Fig. 11. 微信号：MATHmodels

The basic information of top 12 evolutionary artists are listed in Table 4.

Reader can easily ﬁnd our results reliable according the name of these 12 artist. For instance, Dylan was awarded the Nobel Prize in Literature in 2016, Chuck Berry is one of the pioneers of Rock and Roll music, and The Beatles is regarded as the most inﬂuential band of all time.

4.5 Dynamic Process of Evolution

From data_by_year data set, we have known the evolution trend of the musical characteristics over time. Though the general trend is easy to observe by visualizing the data, deeper information Artist ID Name Centrality Artist ID Name Centrality 微信公众号：数学模型 120521 Chuck Berry 0.2921 287604 Louis Jordan 0.2777 824022 Little Richard 0.2904 269972 Little Willie John 0.2731 66915 Bob Dylan 0.2838 549797 Hank Williams 0.2730 79016 Billie Holiday 0.2806 317093 Nat King Cole 0.2729 608701 Muddy Waters 0.2801 754032 The Beatles 0.2708 46861 Ray Charles 0.2783 238115 Sam Cooke 0.2702

* From left to right, top to bottom, the 12 artists are sorted according to their synthesized centrality.

could still be discovered. We are then motivated to analyze the frequency components of time series of each musical characteristics.

微信号：MATHmodels Discrete Fourier transform (DFT) could transform a sequence of samples with a ﬁnite length into a equally-spaced samples discrete-time Fourier transform with the same length [7]. Let x[n] denote a time series. The DFT X[k] of the series x[n] is formulated in Eq. (15).

N−1 x[n]e−j 2π X N kn, k = 0, 1, 2, ..., N −1 X[k] = (15) n=0

where N is the length of series x[n].

An indicator σ is developed in Eq. (16), which measures the proportion of low-frequency components in the time series x[n].

σ = 2 P4 m=1 |X[m]|2 (16) PN−1 m=0 |X[m]|2

PN−1 m=0 |X[m]|2 where N is the length of x[n], is the energy of series x[n]. It should be noted that FFT N (fast Fourier transform) is used instead of DFT when computing DFT by computers.

Eq. (16) is reasonable because |X[0]| = 0 (the DC component) according to data preprocessing, x[n]−¯x[n] where ˆx[n] = x[n]max−¯x[n]. ¯x[n] and x[n]max denote the average and maximum value of series x[n], respectively.

For computers, we apply IFFT (inverse fast Fourier transform) to the four low-frequency components illustrated in Eq. (16). The time series x[n] is the data of Acousticness from 1955 to 2014 of the genre Pop & Rock. N = 60 is the length of x[n]. The results of FFT are shown in Fig. 12.

From Fig. 12, we can observe that the time series reconstructed from the low-frequency com- ponents can well represent the overall trend of the original time series. The result also indicates the the low-frequency components takes up more percentage in the time series of Acousticness of the genre Pop & Rock 微信公众号：数学模型 (a) Amplitude of the FFT result (b) Phase of the FFT result

微信号：MATHmodels (c) The original time series (d) The IFFT of low-frequency components of the original seires

We calculate σ for other typical characteristics of the genre Pop & Rock. The result is listed in

Energy Popularity Liveness Characteristics

σ 0.7895 0.8481 0.4936

The results indicate that Energy and Popularity have larger proportion of low-frequency com- ponents, and have a smoother revolution over time. Meanwhile, Liveness has more high-frequency components. The dynamic process of evolution for other characteristics can be computed and analyzed in the exact same way.

5 Test the Model

In Section 4.3.1 we introduced the deﬁnition of Central node in each genre. Therefore, we will test the eﬀectiveness of our Central node model in this section. 微信公众号：数学模型 The within-genre similarity distribution of Country is given in Section 4.2.2, while the Gaussian ﬁtting result is N(0.85, 0.06). Diﬀerent from the similarity distribution deﬁned previously (where similarity denotes the similarity between every two nodes in the certain genre), we re-deﬁne the distribution of similarity values between the central node and other nodes within Country.

From the deﬁnition of central nodes, we can have an intuitive understanding that the overall similarity will become smaller after the re-deﬁnition, because the central node is likely to locate at the "center" of the genre. The new similarity distribution within Country is shown in Fig. 13.

微信号：MATHmodels

The Gaussian ﬁtting result for the new distribution is N(0.45, 0.04). Compared with the original distribution (which is N(0.85, 0.06)), the expectation value of similarity is signiﬁcantly reduced, meaning that our proposed model of central nodes is valid.

6 Strengths and Weaknesses

6.1 Strengths

1. For the measurement of inﬂuence, we have considered comprehensive aspects with the provided information in the inﬂuence relationship;

2. The MRDE framework we proposed for similarity measurement can well retain information of high-dimensional data;

3. Closeness centrality is used to detect the revolutionary artists. The idea of this method is tested to be eﬀective by comparing the results with real-life information of corresponding artists.

6.2 Weaknesses

微信公众号：数学模型 1. The aggregation we used in the MRDE framework is not accurate enough for deﬁning the actual similarity value from the distribution;

2. When we introduced the method for time series analysis, more state-of-the-art mechanism can be utilized.

7 Conclusion

In this paper, we proposed a detailed model in order to analyze the music objectively. The measurement of inﬂuence and quantiﬁcation of similarity is proposed. Kruskal-Wallis test is performed to identify the inﬂuential characteristics in distinguishing genres, and the contagious nodes are detected using the similar method. Moreover, careful analyses of dynamic process 微信号：MATHmodels evolution are done by transforming the characteristics’ time series by discrete Fourier transform.

In the future, more state-of-the-art techniques could be utilized to analyze the evolution process. For example, the long short term memory (LSTM) framework to predict the time series, providing insight into the possible future trend of music evolution. Meanwhile, the external inﬂuence on the evolution of music could be examined or even quantiﬁed by calculating the correlation value (the Pearson correlation for instance) between the given the time series of external factors and a certain characteristics.
