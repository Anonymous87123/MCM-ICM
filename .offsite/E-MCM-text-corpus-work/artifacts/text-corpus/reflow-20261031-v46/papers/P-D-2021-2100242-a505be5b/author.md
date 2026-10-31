Summary

Music does not evolve isolately, but is always influenced by other artists, other music, or by society and events. To quantify the musical influence, we developed four models based on building networks.

First, we established Influence Evaluation Model Based on PageRank Algorithm for problem 1. The influence relationship between follower and influencer is constructed into an artist influence directed network, where the influencers are the father nodes and the followers are the child nodes. We set sub network of artists by genre. Then, we improved the PageRank algorithm to calculate the absolute influence of each node in overall and sub network. Through this model, we sought for the nodes with high-influence, and got the top 20 influential artists as shown in the table 2.

Second, we established Similarity Model Based on Distance of Vector for problem 2. We developed the music characteristic vector of the artist, which is positively correlated with vector distance. By calculating the distance and drawing heatmap, we got the similarity between artists at each node. The results show that most of the artists had a high degree of similarity with artists of the same genre, but a few artists had a high degree of similarity with artists of other genres.

Third, we established Hybrid Model of Influence and Similarity for question 3 and question 4. We generalized the indexes of influence and similarity to describe genres. Based on this, we distinguished different genres and got the influence relation. We analyzed the changing ways of genres through line charts, completing question 3. Then, we established Inheriting Degree Model of Music Characteristics, combining the connection of network nodes with similarity to develop the inheriting degree index. According to the value of index, we completed question 4 and found that some musical characteristics are more "contagious" than others; the same musical characteristic has different influence in different genres.

Fourth, we established Analysis Model of Music Evolution Process for questions 5, 6 and 7. We selected musical characteristics with moderate inheriting degree, analyzing the major changes over time in music. Take the 1960’s for example, we found that the Beatles were the revolutionaries of music, completing question 5. We averaged the whole genre of music, obtained genre characteristics and its change over time. We set music popularity as an indicator of dynamic influencers, completing question 6. We calculated the overall influence of music genres, observed its change over time, analyzing the influence of social environment on music, completing question 7.

Finally, we conducted a sensitivity analysis for our model, and the result of test goes well. We have optimized the model to meet larger amounts of data. We analyzed the strengths and weakness of the model. In the end, we introduced our model to ICM Society.

1 Introduction

1.1 Restatement of Problem

微信公众号：数学模型 As a kind of art, music is an indispensable cultural element in the development of human civilization. Integrative Collective Music (ICM) Society invites our team to study the evolution and revolution process of music artists and music genres. Since the development of new music is bound to be affected by various factors, the study of the inﬂuence of music is the breakthrough point for our study. Therefore, we need to build models to measure musical inﬂuence.

Musical inﬂuence can be measured in three ways. First, artists are inﬂuenced by other artists. Second, new music are inﬂuenced by previously produced music, which can be seen from the similarities between previous and new music. Third, music changes over time because of social or technological events.

The model we are to build should solve the following problems: 微信号：MATHmodels

1. Establish directed network and its subnetwork between music inﬂuencers and fol-

lowers; ﬁnd parameters that can describe the inﬂuence of inﬂuencers.

2. Establish music similarity measure; compare similarity between and within the gen-

res.

3. Compare the "music similarity and artists inﬂuence" between and within genres;

distinguish genres; describe change tendency and the relationship of the genre.

4. Describe efforts "inﬂuence" makes on "similarity"; ﬁnd music characteristics that are more "contagious".

5. Find music characteristics and artists that represent revolution of music.

6. Further analyze music genres’ and artists’ change over time; ﬁnd a dynamic inﬂu-

encers measure.

7. Describe how music is inﬂuenced by time and environment.

1.2 Our Work

After making reasonable assumptions to simplify the model, we built four models to solve the above seven problems, as shown in the ﬂow chart, ﬁgure 1 below.

• First, we established the Inﬂuence Evaluation Model Based on PageRank Algo- rithm, to complete the question 1.

• Second, we established the Similarity Model Based on Distance of Vector, to solve the question 2.

• Third, we set up the Hybrid Model of Inﬂuence and Similarity, to analyze the question 3 and 4.

• Fourth, we set up the Analysis Model of Music Evolution Process, to make the

关注数学模型 analysis of question 5, 6 and 7.

In addition to the models, we have also done optimization and sensitivity analysis of our models. Finally, we wrote a one-page document for the ICM Society.

微信公众号：数学模型 微信号：MATHmodels

2 Assumptions and Justiﬁcations

1. We assume that the inﬂuence from inﬂuencer to every follower is the same. Be- cause it is not mentioned in the data set, that the inﬂuence weight of the inﬂuencers for one follower.

2. We assume that the impact of a major change of music could be reﬂected in a year.

3. We assume that the inheritance of music characteristic is pure probability inheri- tance.

4. We assume that the most popular music of the year has a greater impact on the genre than any other music. Because a hit song is often a sign of genre develop- ment.

3 Notations

The notation we used is shown in the table 1.

4 Inﬂuence Evaluation Model Based on PageRank Algo-

rithm

This model is built for question 1. According to the requirement, we need to create

a directed network graph connecting followers and inﬂuencers, with inﬂuencers as the关注数学模型 Symbol Deﬁnition

Vi Nodes in the network (artists) 微信公众号：数学模型 L(Vi) The in-degree of node Vi N Number of nodes in the network F(Vi) The node set of the outgoing chain of Vi PR Inﬂuence coefﬁcient of nodes in network p Attenuation coefﬁcient in PageRank algorithm Ci Feature vector of music xik The k-th feature of music i d Distance between eigenvectors sim Similarity between music a The number of the follower with the same genre as Vi b The number of the follower with different genres from Vi PRin The inﬂuence of the artists within the genre 微信号：MATHmodels PRoutk The inﬂuence of the artists on the genre k mk The number of artists and music in genre k FIk The inﬂuence of the genre k on the inner FOk1k2 The inﬂuence of the genre k1 on the k2 SIk The similarity of the inner music in genre k SOk1k2 The similarity between genre k1 and genre k2 IH The inheritance degree of the feature of the music Ek The average of the feature vector of music in genre Pk The most popular of the feature vector of music in genre Pg The sum of the inﬂuence of the genre musicians

father nodes and followers as the child nodes. We also set parameters that represent musical inﬂuence. In social networks, PageRank algorithm can be used to get the infor- mation of "which pages are more important" through the network connection of web pages. Inspired by PageRank[1], we calculate the inﬂuence of nodes and the relative inﬂuence among nodes.

In this model, the value of PR is used as a parameter to measure inﬂuence. It should be noted that in the original PageRank algorithm, the edge of the network graph points to the parent node. In our model, however, the edge points to the child node.

4.1 Establishment of Model

According to the dataset inﬂuence-data, we built a directed network graph with artists as the point and the inﬂuence relationship between artists as the edge. The direction of each edge is from inﬂuencer to follower. The network is shown in the ﬁgure 2 below. The larger the area of the node, the more outgoing links of the node.

In the ﬁgure 2, different colors represent different music genres. The corresponding relationship between color and music genre is shown in the following pie chart as ﬁgure 3.

The network can be divided into some sub networks. Artists of the same music

genre form a sub network. For example, the blue part of the graph is the subnet of Pop关注数学模型 微信公众号：数学模型 微信号：MATHmodels

/ rock music artists, while the orange part of the graph is the subnet of R&B artists.

The advanced PageRank algorithm[2] is applied to our network. The usage and meaning of this algorithm are as follows:

• The goal of this algorithm is to ﬁnd out the "importance" of each node in the network, that is, "inﬂuence".

• The father node has inﬂuence on the child node, and the child node reﬂects the inﬂuence of the parent node. The more child nodes a father node points to , the more the father node inﬂuences, and the greater the inﬂuence of the father node.

In the network, the more the number of outgoing links of a node, the greater the inﬂuence of the node.

• Every child node is called "next generation" relative to its parent node. With the increase of generation, the inﬂuence of the child node on the parent node is less and less obvious. Therefore, we introduce an attenuation coefﬁcient of p.

The idea of PageRank algorithm is iterative operation. Before the calculation, each node is given the same PR value, and each iteration updates, the node will evenly allocate the new PR value to its outgoing nodes. The iteration continues until the allocated value of PR is no longer updated.

In our model, in order to adapt to the problem we need to solve, we change the PageRank algorithm to: in the iterative update, all nodes will allocate the new PR value to their own in chain nodes. That is, the propagation order of the value of PR is from the child node to the father node.

In the iterative update phase, the speciﬁc process of allocating PR value from the child node to the father node is as follows. Figure 4 shows the process as well.

Assuming a network with only three nodes: A, B, C. If both B and C have edges关注数学模型 微信公众号：数学模型

tween color and music genre 微信号：MATHmodels pointing to A, then the PR value of A will be the sum of B, C.

PR(A) = PR(B) + PR(C) (1)

Continue assuming that B also has an edge pointing to C. The number of incoming links of B nodes is 2. PR(A) = PR(B) + PR(C) (2) 2 It is generalized to the general case,

PR(A) = PR(B) L(B) + PR(C) (3) L(C)

where L(B) is the number of inbound links of node B.

As can be seen from the above ﬁgure 4, the child node will divide its own PR value equally, and then assign it to the father node. The PR value after allocation is the edge weight between two nodes. In this way, it forms a "music inﬂuence network". When the iteration stops, the edge weight between the two points means the inﬂuence of the parent node on the child node. At the same time, the calculation method of the PR value of any node Vi in the network is as follows:

PR(Vj) PR(Vi) = 1 −p ∑ + p (4) L(Vj) N Vj∈F(Vj)

Where p represents the attenuation coefﬁcient to reduce the inﬂuence of generations, generally 0.85. N represents the total number of nodes in the network. F(Vi) represents the node set of Vi’s outgoing chain, Vj is any point in this set. Obviously, the greater the PR value, the greater the inﬂuence of the artist.

4.2 Solution of Problem 1

The ﬁgure 2 shows inﬂuence-data set, an overall network of all artists. The blue

part is a subnet of Pop/Rock artists. The ﬁgure 5 below shows the top 10 artists with关注数学模型 the value of PR in the overall network, in which the columns with different colors represent different genres. The following table 2 shows the top 20 artists with PR value.

微信公众号：数学模型

微信号：MATHmodels We ﬁnd that all the characters in the picture are legends of their genres. As an inﬂuence parameter, the value of PR is consistent with the reality and achieves our expected effect.

In order to prove the stability of our model, we apply our algorithm to Pop/Rock sub network and get the following results.

This is the top 10 most inﬂuential Pop/Rock artists. We ﬁnd that the order of Pop/Rock artists in the general list is the same as that in the table 2, so we can prove that our model is stable. The Beatles is no doudt the most inﬂuencial band in the world.

Conclusion: Whether in the subnetwork or the overall network, inﬂuential artists

will stand out with PR.

5 Similarity Model Based on Distance of Vector

This model is built for question 2. We use the characteristics of music to measure

the similarity of music. The characteristics of music, as already given in the dataset, are关注数学模型 PR of artist artist ID artist name artist genre 754032 The Beatles Pop/Rock 0.011573239 259529 Lester Young Jazz 0.007705564 66915 Bob Dylan Pop/Rock 0.007210347 微信公众号：数学模型 403120 The Mills Brothers Vocal 0.006589893 287604 Louis Jordan Jazz 0.006422992 898336 Mississippi Sheiks Blues 0.005855095 848784 Roy Acuff Country 0.00540526 577531 Woody Guthrie Folk 0.005334219 898331 Mississippi Fred McDowell Blues 0.005315981 79016 Billie Holiday Vocal 0.00523804 894465 The Rolling Stones Pop/Rock 0.004968142 317093 Nat King Cole Jazz 0.004940834 549797 Hank Williams Country 0.004919624 120521 Chuck Berry Pop/Rock 0.004888935 608701 Muddy Waters Blues 0.00452981 微信号：MATHmodels 354105 Jimi Hendrix Pop/Rock 0.004285491 128099 James Brown R&B; 0.004214594 200775 Ernest Tubb Country 0.004151536 180228 Elvis Presley Pop/Rock 0.004072049 824022 Little Richard Pop/Rock 0.003939197

quantiﬁable. These characteristics include the following: danceability, energy, valence, tempo, loudness, and mode. We also consider the normalized human voice character- istics. After learning music theory, we think that key has little inﬂuence on music style, so we don’t consider key in music characteristics.

The smaller the absolute value of the difference between the values of a certain characteristic of two music, the more similar the characteristics of two music. If we consider these characteristics as dimensions, then a music is a vector including these dimensions. The closer the two music vectors are, the higher the similarity between the two music vectors is.

For question 2, we need to use this model to calculate the music similarity between artists, and analyze whether the similarity between two musicians in different genres is higher than that between two artists in different genres. According to data set data- by-artist, we can get the average level of each artist’s musical characteristics. In other words, we assume that each artist has only one piece of music, and we compare the similarity between two pieces of music, that is, we compare the similarity between two artists.

5.1 Establishment of Model

In order to make the data of music vector can be compared, we need to normalize the data. We normalized tempo and loudness in music characteristics, and other data have been normalized in data set.

Next, there are two ways to calculate the distance between two vectors. Assume关注数学模型 that the eigenvector of artist i is Ci(xi1, xi2, ..., xim), and the eigenvector of artist j is Cj(xj1, xj2, ..., xjm).

1. We use Minkowski Distance[3] to calculate the distance d between two vectors and

微信公众号：数学模型 transform it into similarity.

pq (xi1 −xj1)p + (xi2 −xj2)p + · · · + (xim −xjm)p d(Ci, Cj)p = (5)

Let p = 2, that is, we choose Euclidean distance as the calculation of vector distance.

We convert the vector distance d into similarity sim. The smaller the d is, the greater the similarity is, as shown below.

sim(Ci, Cj) = e−d(Ci,Cj)2 (6)

2. We use cosine distance[4] to calculate the similarity of two vectors, as shown below.

微信号：MATHmodels ∑m k=1 (xik × xjk) Cj Ci ∥Ci∥· cos θ = = (7) ∥Cj∥ q q ∑m ∑m k=1 x2 k=1 x2 ik × jk

where θ is the angle between Ci and Cj. the smaller θ is, the greater cosθ is, the greater the similarity is. Therefore, the similarity sim is as follows.

sim(Ci, Cj) = cos θ (8)

5.2 Solution of Problem 2

We’ve sorted more than 5000 artists by doing the following. First, all the genres are arranged in dictionary order, and then all the artists in a genre are arranged in their ID.

After sorting, we use the model to calculate the Minkowski distance similarities and cosine distance similarities of any two artists. The heatmap ﬁgure 7 shows the Minkowski distance similarity of all artists we get, and the heatmap ﬁgure 8 is the cosine distance similarity. Among them, as shown in the color bar, the color at the top of the color bar represents high similarity, while the color at the bottom of the color bar represents low similarity.

similarity ilarity

关注数学模型

Conclusions:

• Although the colors of the two heatmaps are different, the shapes of the color blocks are basically the same. The two images are symmetrical about the main diagonal, and the effect is basically the same.

微信公众号：数学模型

• On both sides of the main diagonal are red (the color with higher similarity) square areas. In the sorting process, we arrange the artists of the same music genre together, which means that the similarity of artists within the genre is high- er.

• There are also light color areas on the main diagonal, which means that the simi- larity of very few artists in some genres is not high enough.

• In other areas, we can also see the similarities and differences between different artists through different color shades.

Similar to question 1, we compare the similarity of the top ten inﬂuencers of the overall network and Pop/Rock subnet (using Minkowski distance), as shown in the following ﬁgure 9 and ﬁgure 10. 微信号：MATHmodels 1.0 The Beatles 1.0 The Beatles Lester Young Bob Dylan 0.8 Bob Dylan 0.8 Chuck Berry The Mills Brothers Elvis Presley 0.6 Louis Jordan 0.6 Little Richard Mississippi Sheiks Esquerita 0.4 Roy Acuff 0.4 The Rolling Stones Woody Guthrie Buddy Holly 0.2 Mississippi Fred McDowell 0.2 Bo Diddley Billie Holiday The Velvet Underground 0.0 0.0 The Beatles Lester Young Bob Dylan The Mills Brothers Louis Jordan Mississippi Sheiks Roy Acuff Woody Guthrie Mississippi Fred McDowell Billie Holiday The Beatles Bob Dylan Chuck Berry Elvis Presley Little Richard Esquerita The Rolling Stones Buddy Holly Bo Diddley The Velvet Underground

Conclusions:

• In the overall network list, the similarity of artists of different genres is generally low.

• In the sub network list, the similarity of artists in one genre is high.

We took the Beatles, Bob Dylan and Lester Young as examples, drew two radar maps of their musical characteristics, as shown in ﬁgure 11 and ﬁgure 12.

Obviously, the Beatles and Bob Dylan belong to the same genre, their musical char- acteristics are indeed very similar; The Beatles and Lester Young belong to different genres, their musical characteristics are very different. This conﬁrms our conclu- sions.

• Most of the artists have high similarity with the artists of the same genre, while very few artists have high similarity with the artists of other genres.

We think this is reasonable. Music and art blend with each other. If an artist always studies one genre, he must have a higher similarity with the artists of that genre. But for some other artists, if they are involved in a wide range of genres or like to create experimental music, their works will integrate the characteristics

关注数学模型 of different genres of music.

微信公众号：数学模型

tics of the Beatles and Lester Young tics of the Beatles and Bob Dylan

6 Hybrid Model of Inﬂuence and Similarity

This model is built for questions 3 and 4. Some people think that an artist is in- 微信号：MATHmodels ﬂuenced by other artists as well as other music. Ours "inﬂuence evaluation model" is used to measure personal inﬂuence of an artist. But after generalization, this model can be used to measure the music inﬂuence an artist receives. Ours "Similarity model" is used to measure the similarity of music. But after generalization, this model can be used to measure the similarity between music genres. In question 3, we will compare A with B, C with D. Among them, A is the similarity among genres, B is the similarity within genres, C is the inﬂuence among genres and D is the inﬂuence within genres. In question 4, one of our tasks is to prove whether "inﬂuence" works on "similarity". Therefore, this model needs to combine and compare the above two models.

For question 3, we generalize the "inﬂuence index" and "similarity index" from sin- gle artist to music genres, and ﬁnd the way to distinguish genres. For question 4, we start from similarity, analyze the "infectivity" of the characteristics of music.

6.1 Generalization of The Two Indicators

6.1.1 Generalization of The Inﬂuence Indicator

In the previous model, we considered the absolute inﬂuence of artists themselves and their relative inﬂuence on their followers. In this model, we generalize the "inﬂu- ence index" to the relative inﬂuence of artists on genres.

In question 1, we got the PR value of all artists: PR(Vi). The number of people in- ﬂuenced by artist Vi is L(Vi). We assumed that among the artists inﬂuenced by Vi, there are a artists of the same genre as artist Vi, and b artists of different genres. therefore

L(Vi) = a + b (9)

b = b1 + b2 + · · · + bk (10)

The formula (10) indicates that b artists may come from k different genres.

So we get the inﬂuence of the artist Vi on the inner genre as follows:

PRin(Vi) = 1 −p + pαi × PR(Vi) (11)关注数学模型

N The inﬂuence of artist Vi on genre k is:

PRoutk(Vi) = pβik × PR(Vi) (12)

微信公众号：数学模型 where a αi = (13) L(Vi) bk βik = (14) L(Vi)

Average the formula (11), the inner inﬂuence of genre k is

1 −p ∑mk + pαi × PR(Vi) i=1 N FIk = (15) ∑mk i=1 PR(Vi)

where mk is the number of artists in the genre k. Average the formula (12), the inﬂuence 微信号：MATHmodels of genre k1 on genre k2 is

FOk1k2 = ∑mk1 i=1 pβik2 × PR(Vk1i) (16) ∑mk2 i=1 PR(Vk1i)

6.1.2 Generalization of The similarity Indicator

It is known that the similarity between two pieces of music is sim(Vi, Vj). The same as in the previous section, taking the average similarity within the genre, then the inner music similarity of genre k is

∑mk i=1 ∑mk j=1 sim(Vi, Vj) SIk = (17) m2 k

The music similarity of genre k1 and genre k2 is

∑mk1 i=1 ∑mk2 j=1 sim(Vk1i, Vk2j) SOk1k2 = (18) mk1mk2

6.2 Inheriting Degree Model of Music Characteristics

When two artists have an inﬂuential relationship and their music has a certain sim- ilarity, we call one inheriting music characteristic from another one. Therefore, we mixed the two indexes and established a model to measure the inheriting degree.

We think that follower is inﬂuenced by many inﬂuencers, and it is impossible for him or her to completely inherit the musical characteristics of an artist. At the same time, artists have their own creativity, and their musical characteristics are not com- pletely inherited.

Because the characteristics of different genres are different, the same kind of music characteristics may have different inheritance ability in different genres. Music char- acteristics inheriting degree can be divided into cross genre and within genre. Cross

genre music characteristics inheriting degree is affected by music genre similarities,关注数学模型 which is difﬁcult to measure quantitatively. Therefore, we think that the inheriting degree within the genre can better reﬂect the inheritance of music characteristics.

The artist’s music feature vector is Ci(xi1, xi2, ..., xi9). Setting Boolean variables G, which means whether a certain characteristic of two artists is similar in value, there is 微信公众号：数学模型  1, xik ≈xjk G(k) = (19) xik̸ = xjk 0,

We assume that, if |xik −xjk| ≤±5%xik, then xik ≈xjk. When G(k) = 1, We think the characteristic k has been successfully inherited.

Let IH(xk) be kth of the 10 music characteristics in a genre with a total population of m, it is reﬂected in the ratio of "the number of successful inheritees of characteristic xk" to "the total number of inheritees of characteristic xk".

L(Vi) ∑m j=1 G(k) i=1 ∑ IH(xk) = (20) ∑m 微信号：MATHmodels i=1 L(Vi)

The larger the index IH is, the easier it is to inherit the feature, and the more infec- tious it is.

6.3 Solution of Problem 3

According to formula (15) and formula (16), we draw the heatmap of genres inﬂu- ence, as shown in the ﬁgure 13 below.

Avant-Garde Blues 0.8 Children's 1.0 Avant-Garde Classical Blues 0.7 Comedy/Spoken Children's Country Classical 0.8 Comedy/Spoken Easy Listening 0.6 Country Electronic Easy Listening Folk 0.5 Electronic International 0.6 Folk Jazz International 0.4 Latin Jazz New Age Latin Pop/Rock 0.3 0.4 New Age R&B; Pop/Rock Reggae R&B; 0.2 Reggae Religious 0.2 Religious Stage & Screen 0.1 Stage & Screen Unknown Unknown Vocal Vocal 0.0 0.0 Avant-Garde Blues Children's Classical Comedy/Spoken Country Easy Listening Electronic Folk International Jazz Latin New Age Pop/Rock R&B; Reggae Religious Stage & Screen Unknown Vocal Avant-Garde Blues Children's Classical Comedy/Spoken Country Easy Listening Electronic Folk International Jazz Latin New Age Pop/Rock R&B; Reggae Religious Stage & Screen Unknown Vocal

In the heatmap, the diagonal blocks represent inner inﬂuence of the genres. The column of blocks represent the inﬂuence of other genres on diagonal music genre; the row of blocks represent the inﬂuence of diagonal music genre on other genres.

The heatmap directly reﬂects the inﬂuence degree of a certain genre on another genres. For example, the reddest block Pop/Rock is inﬂuenced by Blues, Country, Folk, Jazz, R&B (column) and so on. At the same time, Pop/Rock has a strong inﬂuence on Country and Electronic (row).

The rule of genres changing over time is: most genres have strong inheritance abil- ity, and the larger the genre, the greater the inner inﬂuence. As shown in the heatmap, the color on the diagonal represents the degrees of the inner inﬂuence of genres, and

it can be seen that most of them are clearly visible color blocks. After consulting the关注数学模型 data, we found that our model results accord with the actual situation, so our inﬂuence model is successful.

According to formula (17) and formula (18), we draw the heatmap of similarity, as shown in the ﬁgure 14. 微信公众号：数学模型 In the heatmap, the image is symmetrical about the diagonal, the diagonal blocks represent the average similarity within one genre, and the other blocks represent the average music similarity between two genres.

On the whole, genre similarity and artist similarity have the same features. The blocks on the diagonal show that the similarity within genres is greater than that be- tween genres, showing the feature of centralization. What’s more, Pop/Rock is more similar to R&B, Country, Blues, Reggae and Latin in this similarity heatmap, because they are all dark red, and in the inﬂuence heat map above, it shows that Pop/Rock is inﬂuenced by them. The two heatmaps show a certain consistency. Therefore, our similarity model is also successful.

Based on the above analysis, we draw the following conclusions. 微信号：MATHmodels

Conclusions:

• The way of distinguishing different genres: music similarity model is used for clustering, and genre labels are added to the clustering results through the inner genre similarity.

• The way music genres change over time: The change of inﬂuence parameters FI and FO over time can reﬂect the dynamic inﬂuence and dynamic stability of a genre. Considering the increasing number of people in a genre, we can analyze the development of a genre. Take Pop/Rock as an example, its change of FI and FO over time is shown as ﬁgure 15.

Pop/Rock was born in 1930. During the period of 1930-1940, this genre had a great inner inﬂuence, indicating that it was accepting the inﬂuence of other genres and was in its stage of infancy. In 1950, the population of genre increased for the ﬁrst time, and its between genres inﬂuence increased. This new genre had a great impact on the music circles. Representing Pop/Rock entered stage of development. In 1960, a large number of artists invested in Pop/Rock music creation, Pop/Rock’s inner inﬂuence increased

and maintain stability. Pop/Rock genre entered stage of mature. After 1960, FI = 0.9,关注数学模型 FO = 0.1, the number of Pop/Rock genre is still increasing, but the inﬂuence of the genre is basically shaped, it has stable self-development power, and music inﬂuence. By 2010, only 100 artists joined this genre, and there is no signiﬁcant change of FI, FO. Therefore, from the perspective of population growth, Pop / Rock may be being 微信公众号：数学模型 surpassed by other genres.

6.4 Solution of Problem 4

According to the model, we got the inheriting degree heatmap of 10 × 20 by calcu- lation, as shown in the ﬁgure 16 below.

0.8 danceability energy 0.7 valence tempo 0.6 loudness 微信号：MATHmodels 0.5 mode acousticness 0.4 instrumentalness liveness 0.3 speechiness 0.2 Avant-Garde Blues Children's Classical Comedy/Spoken Country Easy Listening Electronic Folk International Jazz Latin New Age Pop/Rock R&B; Reggae Religious Stage & Screen Unknown Vocal

In different genres, different musical characteristics are inherited with different de- grees of inheritance. We assumed that when IH ≥0.6, musical characteristics are considered as good inheritance.

Among the 20 genres, at least four characteristics are inherited, and at most nine characteristics are inherited. For example, Avant-Garde inherits only tempo, dance a- bility, liveness and speech, while Children’s inherits all the characteristics. If we further increase the IH, we can further screen representative music characteristics of different genres, and show the differences between genres.

Conclusions:

• The inﬂuencer does have inﬂuence on the followers, and the inﬂuence is reﬂected by the inheritance of music characteristics. For example, the characteristic speech of jazz genre has a 0.78 probability of being inherited in the process of inﬂuence between inﬂuencers and followers.

• Some music characteristics are more "contagious" than others. For example, the speech (0.78) of jazz is more inheritable than the valence (0.61).

• The same music characteristic has different inﬂuence ability in different genres.

For example, the speech (0.78) of jazz genre is more inheritable than speech (0.44) of Comedy/Spoken genre.

• The inheritance abilities of some music characteristics in all genres are generally

关注数学模型 not weak, such as tempo (0.68-0.83).

• The inheritance abilities of some music characteristics in all genres are generally not strong, such as mode (0.16-0.77).

微信公众号：数学模型

7 Analysis Model of Music Evolution Process

7.1 Establishment and Solution of Problem 5

We think that the stronger the inheriting degree of a certain musical characteristic is, the less the musical characteristic changes with time. Therefore, we take the muta- tion of musical characteristics with strong inheriting degree as an indicator, reﬂecting whether revolutionaries have taken place. However, if the inheriting degree is too strong, this characteristic will be too stable. If a strong inherited music characteristic in the data set data-by-year mutates in a certain year, according to the assumption, it shows that as a great revolutionaries, the artist played his role in that year.

微信号：MATHmodels We selected ﬁve music charateristics with moderate inheriting degree: energy, tem- po, acousticness, instrumentalness, and speechiness. We drew a line chart, as shown in the ﬁgure 17.

Conclusion: from 1964 to 1969, acousticness dropped sharply, and energy contin-

ued to rise. We found the active musicians and their albums in the corresponding peri- od. We found that the Beatles were one of the most active inﬂuencers. Their following ﬁve songs had a very low level of acousticness and high energy, and were among the most popular in the same era.

The ﬁve songs are: a. Tomorrow Never Knows - Remastered ****; b. Sgt. Pepper’s Lonely Hearts **** Band (Reprise) - Remix; c. Sgt. Pepper’s Lonely Hearts **** Band - Reprise / Remastered ****; d.And Your Bird Can Sing - Remastered ****; e. Nowhere Man - Remastered ****. The information of the ﬁve songs is shown in the table 3.

7.2 Establishment and Solution of Problem 6

In question 6, we set up a model to represent the changes of music characteristics within the genre over time. We start with the dataset full-music-data to get the average value of the music characteristics of a certain genre every year, written as a vector is

关注数学模型 Ek(ext1, ext2, ..., ext10).

song energy tempo acoustic instrumental speechi popularity year a 0.829 125.887 8.40E-05 0.00208 0.0405 58 1966 b 0.951 118.769 0.000249 0.214 0.0521 40 1967 c 0.889 118.773 0.0061 0.589 0.0453 52 1967 微信公众号：数学模型 d 0.65 132.59 0.0067 0.0491 0.0282 59 1966 e 0.624 121.402 0.00797 0 0.0462 64 1965

We draw a time-dependent curve of each dimension eti to show the evolution trend of music characteristics of one genre changed over time. Then we take the most pop- ular song of the genre every year, drew the same curve of each dimension Pki of the music characteristics of the song. We compared the changes and differences between the two. Here, we take Electronic as an example. We only select one characteristic va- lence and chose the representative work, Tangerine Dream, that is, compared Eki with 微信号：MATHmodels Pki, as shown in the ﬁgure 18 below.

As we can see from the ﬁgure, we draw the curve of Eki, which reﬂected the overall evolution trend of the music characteristics of the Electronic genre. By comparing the evolution curve of the overall characteristics of genres, with the characteristic curve of the most popular music of genres, we draw conclusions.

Conclusions:

• The trend of the two curves is similar.

• The trend of Eki is slightly behind that of Pki.

• Eki is more stable than Pki.

Therefore, we infer that the most popular music in the genre inﬂuences the whole genre and promotes and guides the evolution of the genre, which is the law of genre change. For a piece of music, we examined two indicators: popularity and Pk. Among them, popular determines whether a piece of music can be rated as "contagious", and Pk determines the direction of music’s inﬂuence in the music circle.

关注数学模型 We think that the artists who make these music are "dynamic inﬂuencers".

7.3 Establishment and Solution of Problem 7

Any historical event is likely to inﬂuence on each genre and form a huge inﬂuence network. In order to simplify the model, we chose three genres (Blues, Electronic and 微信公众号：数学模型 Pop/Rock) and several historical events to illustrate the model.

We calculated the sum of artist inﬂuence of each genre in each era PGikt.

mk ∑ PGikt = PR(Vikt) (21) i=1

We drew a total inﬂuence curve PG(t), as shown in the ﬁgure 19 below. Each inﬂu- ence curve is normalized into the same graph, and historical events are added to the time line for analysis.

微信号：MATHmodels

Combined with the actual history, the following conclusions can be drawn from the ﬁgure 19.

Conclusions:

• After the end of the economic depression, the music curve shows an upward trend, and it is speculated that it will be frustrated during the depression.

• In the Second World War, classical music suffered a serious setback[5]. Because the cost of classical music performance is high after the formation of the perfor- mance agent, the war leads to people’s retrenchment, and ﬁnancial institutions invest their funds in the war, and the lack of funds has a huge impact on it. With the economic recovery after the war, the inﬂuence of classical music recovered with the improvement of people’s economic strength.

• The rise of American civil rights movement from 1950 to 1970 promoted the de- velopment of Blues: 1. Blues originated from black slaves in the past[6]. 2. In the early 1950s, the center of blue was in Chicago, USA. 3. The music of the civil rights movement and the freedom of speech movement in the United States led to the study of the early black American music.

• Since 1970, Moore’s law has created affordable music technology, and the use of electronic music has become more and more popular. In the 1970s, personal com- puters began to be popular, corresponding to the acceleration of the development of electronic music.

• In the information age, the high-speed information ﬂow keeps the inﬂuence of

关注数学模型 each school at a high level.

The change of PG(t) curve perfectly reﬂects the change of music inﬂuence, can make timely response to historical events, and conforms to historical common sense. So, our PG(t) curve is successful.

微信公众号：数学模型

8 Sensitivity Analysis

Inﬂuence Evaluation Model and Similarity Model are our basic models, so we con- ducted sensitivity analysis on these two models.

• We changed the damping coefﬁcient p in the PageRank algorithm to a range of 0.85 ± 0.15, and the error ratio of PR is shown in the ﬁgure 20 below. It can be seen that when the damping coefﬁcient p changes, the error ratio is less than 5%, which meets our expectation. The model has passed the sensitivity analysis.

• We changed the dimension of vector with a range of 10 ± 3 dimensions, and the 微信号：MATHmodels error ratio of the similarity is shown in the ﬁgure 21 below. It can be seen that when the dimension changes, the error ratio is less than 2%, which meets our expectation. The model has passed the sensitivity analysis.

9 Optimization of Model

Since the data set given by ICM Society has certain limitation, we consider the op- timization of our model when the data set becomes larger. When the generation in- volved in the data set increases, the time series becomes worse with the time span.

We introduced the time factor ∆t and the outcome indicator Wi[7] as the inﬂuence coefﬁcient, where Wi is from evaluation system. So we got

i × e−c∆t Pi = aWb (22)

PR(Vj) ∑ PR(Vi) = (1 −p)Pi + p (23) L(Vj) Vj∈F(Vj)

where a, b and c are the parameters that need to be adjusted in the model. The PageR- ank algorithm itself is suitable for processing big data. After we add time factor, we can process data with long generation span better than the original algorithm.

关注数学模型

10 Strengths and Weaknesses

10.1 Strengths

微信公众号：数学模型

• Lightweight: Our models are not complicated in construction, and can use the least data to analyze the problem. The results are obvious. The time and space complexity of the algorithm is low.

• Creativity: In order to analyze the changes of evolution progress, we have created several indicators. The analysis results can be veriﬁed quantitatively, which also makes our model original.

• Accuracy: According to the results of quantitative analysis, our models are logi- cally self-consistent and practical, making them successful and accurate.

• Stability: Our basic models have been tested by sensitivity analysis, and the error is acceptable, so the model is stable. 微信号：MATHmodels

• Scalability: We optimize our model to handle much larger amounts of data.

10.2 Weakness

When it comes to problem 5, our model can only identify a few particular super inﬂuencers; For question 6, we chose the most popular music, ignoring the inﬂuence of other music on the list.

关注数学模型

Inﬂuence Evaluation Model Based on PageRank Algorithm, to calculate the absolute

微信号：MATHmodels and relative inﬂuence of artists. Then, we treat music as a vector, assigning properties to the network nodes. This is the second model, Similarity Model Based on Distance of Vector. We use it to calculate the similarity between two nodes. Next, we build the third model,Hybrid Model of Inﬂuence and Similarity. With the connections between nodes and their own properties. this model can calculate the similarity and inﬂuence of the whole network.The inheriting degree between two pieces of music, known as "contagious", can be sovled as well. Finally, the fourth model, Analysis Model of Music Evolution Process is built to analyze the variation of eigenvectors of each node.

Second, what are the advantages of our model? Our models are simple to use, highly original, and calculate the inﬂuence of music quantitatively. The models passed sensitivity analysis, and we optimized the models to accommodate larger data sets.

Thirdly, based on the data set, our model draws the following conclusions.

• The Beatles are undoubtedly the most inﬂuential artists, both absolutely and rel- atively. At the same time, they are the revolutionaries of our music network.

• In terms of genres, artists of most genres are similar in music characteristics. The more inﬂuential the genre is, the higher the internal similarity is, and the more stable the inheritance is.

• Music similarity is indeed inﬂuenced by the inﬂuencer. Some music characteris- tics are more "contagious" than others. The same music characteristics has differ- ent inﬂuence ability in different genres.

• In our network, the way we analyze social inﬂuences on music is by comparing changes in musical characteristics over time to historical axes of events.

As John Lennon said, "Music never gets old." Music is a bridge connecting human society, is a manifestation of human joys and sorrows. Music is always evolving, and artists are taking advantage of society and technology to add new vitality to the music. Artists learn from each other, making the development of music full of vitality. In this age of technology, artists, and ordinary people, have never been closer to art. It was, arguably, the best age for music.

关注数学模型
