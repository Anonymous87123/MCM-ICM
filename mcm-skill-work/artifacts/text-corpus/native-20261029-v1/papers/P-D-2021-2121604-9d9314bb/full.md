# P-D-2021-2121604-9d9314bb

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
微信公众号：数学模型

<!-- b000002 | furniture | pages [1] -->
2021

<!-- b000003 | prose | pages [1] -->
Problem Chosen

<!-- b000004 | furniture | pages [1] -->
Team Control Number

<!-- b000005 | prose | pages [1] -->
MCM/ICM

<!-- b000006 | title | pages [1] -->
D

<!-- b000007 | furniture | pages [1] -->
2121604

<!-- b000008 | heading | pages [1] -->
Summary Sheet

<!-- b000009 | title | pages [1] -->
An Exploration of Music Evolution Based on Inﬂuencer

<!-- b000010 | title | pages [1] -->
微信公众号：数学模型

<!-- b000011 | title | pages [1] -->
Network and Cosine Similarity

<!-- b000012 | heading | pages [1] -->
Summary

<!-- b000013 | prose | pages [1] -->
Aiming to comprehend the evolution of music, we combine the network science, cosine similarity, Cooling Model and Gravity Model in physics, as well as other sta- tistical methods to explore how music evolves through inﬂuence across artists and genres.

<!-- b000014 | prose | pages [1] -->
Above all, we created the directed inﬂuencer network to visualize the relationship between inﬂuencers and followers. We then explain the concept of music inﬂuence with the help of the Cooling Model to describe one’s declining inﬂuence as the time interval gets longer. Having done that, we show the music inﬂuence of artists in a subnetwork by the size of nodes and conduct detailed analysis.

<!-- b000015 | title | pages [1] -->
微信号：MATHmodels

<!-- b000016 | prose | pages [1] -->
Next, after data pre-processing, we use PCA to reduce the dimensionality of music characteristics and extract four factors. Based on the eigenvector formed by the four factors, we calculate cosine similarity between artisits or genres. Our method to mea- sure similarity proves to be right since artists within genres get higher similarity than artists between genres.

<!-- b000017 | prose | pages [1] -->
Then, we develop our basic model of network and similarity to solve tasks about the evolution of music.Our analysis is from the following four perspectives.

<!-- b000018 | prose | pages [1] -->
For tasks about inﬂuencers and followers, we compare the similarity density curve between followers and inﬂuencers or non-inﬂuencers and afﬁrm the inﬂuencers’ im- pact on followers music. Then, we rebuild the eigenvector to calculate similarity by removing each characteristic to see which one is more contagious during the inﬂuence process of a particular genre.

<!-- b000019 | prose | pages [1] -->
For tasks about trends of genres, ﬁrstly we calculate the similarity matrix of genres and describe relations and difference between genres accordingly. Next, based on the Gravity Model, we estimate the dominant genre of each year and analyze the trends of genres changing over time. In addition, we analyze the evolution of country mu- sic particularly by using popularity and counts to ﬁgure out dynamic inﬂuencer and explain the fusion of country and other genres during its evolution.

<!-- b000020 | prose | pages [1] -->
For tasks about musical revolutions, we analyze the cosine similarity between each year and its following year to identify signiﬁcant changes as revolutions. We ﬁnd that the periods of the 1940s, 1960s and 1980s are revolutionary period and we particularly anaylze the revolution between 1965 and 1967 to ﬁnd out the Beatles and Bob Dylan are two artists represent revolution in this periods.

<!-- b000021 | prose | pages [1] -->
For tasks about other impacts of music evolution, we give a detailed analysis on the genre timeline and revolution period with major cultural, social, political or tech- nological changes, explaining how events like the Cold War, Civil Rights Movements inﬂuenced the evolution of music.

<!-- b000022 | prose | pages [1] -->
To summarize, our models have enlightening values for further study due to its comprehensiveness, innovation and good performace in sensitive analysis.

<!-- b000023 | furniture | pages [1] -->
微信号：MATHmodels

<!-- b000024 | prose | pages [1] -->
关注数学模型

<!-- b000025 | furniture | pages [1] -->
2

<!-- b000026 | furniture | pages [1] -->
MATHmodels

<!-- b000027 | furniture | pages [1] -->
获取更多资讯

<!-- b000028 | furniture | pages [2] -->
Team # 2121604

<!-- b000029 | furniture | pages [2] -->
微信公众号：数学模型

<!-- b000030 | furniture | pages [2] -->
Page 2 of 22

<!-- b000031 | heading | pages [2] -->
Contents

<!-- b000032 | contents | pages [2] -->
1

<!-- b000033 | contents | pages [2] -->
Overview

<!-- b000034 | contents | pages [2] -->
3

<!-- b000035 | contents | pages [2] -->
Problem Restatement . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000036 | contents | pages [2] -->
1.1

<!-- b000037 | contents | pages [2] -->
3

<!-- b000038 | contents | pages [2] -->
微信公众号：数学模型

<!-- b000039 | contents | pages [2] -->
Background Research . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [2] -->
1.2

<!-- b000041 | contents | pages [2] -->
3

<!-- b000042 | contents | pages [2] -->
Our Work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000043 | contents | pages [2] -->
1.3

<!-- b000044 | contents | pages [2] -->
2

<!-- b000045 | heading | pages [2] -->
Preparation of the Models

<!-- b000046 | prose | pages [2] -->
3

<!-- b000047 | prose | pages [2] -->
4 Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.1 4 Notations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.2 4 Data Pre-processing . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2.3 5

<!-- b000048 | heading | pages [2] -->
Basic Models: The inﬂuencer Network and Similarity

<!-- b000049 | prose | pages [2] -->
3 5 . . . . . . . . . . . . . . . . . . . . . . . . . 3.1 Directed Inﬂuencer Network 5 Musical Inﬂuence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.2 6 Exploration of Subnetworks . . . . . . . . . . . . . . . . . . . . . . . . . . 3.3 7 Music Similarity . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3.4 8

<!-- b000050 | prose | pages [2] -->
微信号：MATHmodels

<!-- b000051 | prose | pages [2] -->
Development & Exploration: How Does Music Evolves? 4 9 The Impact if Inﬂuencers on Followers . . . . . . . . . . . . . . . . . . . . 4.1 9 Inﬂuencer’s Effect on Music Created by the Followers . . . . . . . 4.1.1 4.1.2 Contagious Characteristics 9 . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | prose | pages [2] -->
9 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2 Trends of Genres 10 . . . . . . . . . . . . . . . . . . . . . . . . . . 4.2.1 Similarity of Genres 10 What Distinguishes a Genre? . . . . . . . . . . . . . . . . . . . . . 4.2.2 11 The General Evolution of Genres . . . . . . . . . . . . . . . . . . . 4.2.3 12 Relations Between Genres . . . . . . . . . . . . . . . . . . . . . . . 4.2.4 13 Evolution in A Speciﬁc Genre: Country . . . . . . . . . . . . . . . 4.2.5 14 From Evolution to Revolution . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 15 When Did the Revolutions Happen? . . . . . . . . . . . . . . . . . 4.3.1 15 What Artists Represent Revolutionaries? . . . . . . . . . . . . . . 4.3.2 16 Other Factors in Music Evolution . . . . . . . . . . . . . . . . . . . . . . . 4.4 17 Cultural Inﬂuence of Music . . . . . . . . . . . . . . . . . . . . . . 4.4.1 17 Social, Political, Technological Changes . . . . . . . . . . . . . . . 4.4.2

<!-- b000053 | prose | pages [2] -->
5 Sensitive Analysis

<!-- b000054 | prose | pages [2] -->
6 Assessment

<!-- b000055 | prose | pages [2] -->
17

<!-- b000056 | prose | pages [2] -->
18

<!-- b000057 | prose | pages [2] -->
19 Strengths . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.1 19 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6.2 Weaknesses 20

<!-- b000058 | heading | pages [2] -->
Conclusion & Further Considerations: A Document to the ICM Society

<!-- b000059 | prose | pages [2] -->
7

<!-- b000060 | heading | pages [2] -->
References

<!-- b000061 | furniture | pages [2] -->
微信号：MATHmodels

<!-- b000062 | references | pages [2] -->
21

<!-- b000063 | references | pages [2] -->
21

<!-- b000064 | references | pages [2] -->
关注数学模型

<!-- b000065 | furniture | pages [2] -->
2

<!-- b000066 | furniture | pages [2] -->
MATHmodels

<!-- b000067 | furniture | pages [2] -->
获取更多资讯

<!-- b000068 | furniture | pages [3] -->
Team # 2121604

<!-- b000069 | references | pages [3] -->
1

<!-- b000070 | references | pages [3] -->
Overview

<!-- b000071 | references | pages [3] -->
1.1

<!-- b000072 | heading | pages [3] -->
Problem Restatement

<!-- b000073 | furniture | pages [3] -->
微信公众号：数学模型

<!-- b000074 | furniture | pages [3] -->
Page 3 of 22

<!-- b000075 | prose | pages [3] -->
微信公众号：数学模型

<!-- b000076 | prose | pages [3] -->
Music has gone through rapid development in the past 100 years. In order to un- derstand the evolution of music from the angle of inﬂuence across artists, we need to solve the following problems:

<!-- b000077 | prose | pages [3] -->
• Construct directed networks of inﬂuencing relationships based on the provided "inﬂuence_data" data set and develop measures of music inﬂuence. The net- works should include both the parent network and the subnetwork with detailed description;

<!-- b000078 | prose | pages [3] -->
• Build a model to measure the music similarity based on the rest of the given data sets, and examine this model by comparing the similarity between artists within genres and artists between genres;

<!-- b000079 | prose | pages [3] -->
微信号：MATHmodels

<!-- b000080 | prose | pages [3] -->
• Explore whether the inﬂuencer really affects the music of the followers, and whether each feature of the music plays an equally vital role in the process of inﬂuencing;

<!-- b000081 | prose | pages [3] -->
• Find out the differences and connections between genres and explore the devel- opments of genres over time, not only the developments of representative music genres at different times, but also the developments of the same music genres in different periods; identify indicators to ﬁnd out the most dynamic inﬂuencer and analyze the evolution process of a particular genre;

<!-- b000082 | prose | pages [3] -->
• Introduce an indicator to imply major changes in the evolution process, and point out the artists who represent revolutionaries;

<!-- b000083 | prose | pages [3] -->
• Discuss the cultural impacts of music or other factors that may inﬂuence music evolutions;

<!-- b000084 | prose | pages [3] -->
1.2 Background Research

<!-- b000085 | prose | pages [3] -->
During the 20th century, the inﬂuence of the United States was almost all over the world, especially in music. In the meantime, the music genre has evolved rapidly, from Blues to Country, a large number of genres have appeared in almost 100 years (History Detectives) [1]. The work of predecessors is basically to process audio. Nicola Orio et.al constructed a melody similarity measurement model based on music structure diagram, and they also trained this model in a small test collecting and got preliminary results in terms of music similarity [2]. Juan P.Bello showed a new methods to measure the structure similarity between music records. Compared with traditional methods, It assumes a block-based music model and therefore focuses on the segmentation and clustering parts. They have ﬁnally got achievements in characterizing similarity and provided the best parameters for the proposed method [3].

<!-- b000086 | prose | pages [3] -->
1.3 Our Work

<!-- b000087 | prose | pages [3] -->
While there have been some previous research on the similarity of music, few of

<!-- b000088 | furniture | pages [3] -->
微信号：MATHmodels

<!-- b000089 | prose | pages [3] -->
the researchers before have tried to use the similarity data to interpret the evolution关注数学模型

<!-- b000090 | furniture | pages [3] -->
2

<!-- b000091 | furniture | pages [3] -->
MATHmodels

<!-- b000092 | furniture | pages [3] -->
获取更多资讯

<!-- b000093 | furniture | pages [4] -->
Team # 2121604

<!-- b000094 | furniture | pages [4] -->
微信公众号：数学模型

<!-- b000095 | furniture | pages [4] -->
Page 4 of 22

<!-- b000096 | prose | pages [4] -->
of music. Based on the given data sets, we try to convey the evolution of music in an inspiring way. After data pre-processing, we build the basic model for constructing the inﬂuencer network and use the Cooling Model and cosine similarity to describe the parameters. Next, we apply our model to further explorations of the evolution of

<!-- b000097 | prose | pages [4] -->
微信公众号：数学模型

<!-- b000098 | prose | pages [4] -->
music in the scale of artists, genres, revolutions and other social impacts.

<!-- b000099 | heading | pages [4] -->
Preparation of the Models

<!-- b000100 | prose | pages [4] -->
2

<!-- b000101 | prose | pages [4] -->
2.1

<!-- b000102 | heading | pages [4] -->
Assumptions

<!-- b000103 | prose | pages [4] -->
• Music inﬂuence decreases as the time interval gets bigger. Works generally have a certain timeliness, and the popularity of works decays over time. The amount of decline has nothing to do with the year of release and popular year, but with the time interval. The longer the time interval from the judging point to the year of release is, the less inﬂuences the works may have on musicians

<!-- b000104 | prose | pages [4] -->
微信号：MATHmodels

<!-- b000105 | prose | pages [4] -->
nowadays..

<!-- b000106 | prose | pages [4] -->
• Every follower was inﬂuenced by inﬂuencers in the year they started to make music. It is difﬁcult to deﬁne when a person’s peak period is, so it is fair and reasonable to use one’s active start year to calculate.

<!-- b000107 | prose | pages [4] -->
• Each artist belongs to only one genre, and the genre has not changed during his entire career.Generally speaking, an artist who decides to choose a genre must have been inﬂuenced by the works of his predecessors, so it is unlikely that he will change the genre in his later creations.

<!-- b000108 | prose | pages [4] -->
• Artist can reﬂect the characteristics of his genre.Artists need to reﬂect the char- acteristics of his category, otherwise he won’t be classiﬁed into this genre.

<!-- b000109 | prose | pages [4] -->
• The existing data set can reﬂect the music market situation. We fully trust the statistics of various indicators such as the number of followers and popularity, and believe that the trends reﬂected are correct.

<!-- b000110 | prose | pages [4] -->
2.2

<!-- b000111 | heading | pages [4] -->
Notations

<!-- b000112 | prose | pages [4] -->
The primary notations used in this paper are listed in Table 1.

<!-- b000113 | caption | pages [4] -->
Table 1: Notations

<!-- b000114 | prose | pages [4] -->
Symbol

<!-- b000115 | prose | pages [4] -->
MI sim

<!-- b000116 | prose | pages [4] -->
Deﬁnition

<!-- b000117 | prose | pages [4] -->
Music Inﬂuence The cosine similarity of two vectors G The sphere that represent a genre u The dominant genre of a particular year which is unknown Fi One of the factors drawn from PCA

<!-- b000118 | furniture | pages [4] -->
微信号：MATHmodels

<!-- b000119 | prose | pages [4] -->
关注数学模型

<!-- b000120 | furniture | pages [4] -->
2

<!-- b000121 | furniture | pages [4] -->
MATHmodels

<!-- b000122 | furniture | pages [4] -->
获取更多资讯

<!-- b000123 | furniture | pages [5] -->
Team # 2121604

<!-- b000124 | prose | pages [5] -->
2.3 Data Pre-processing

<!-- b000125 | furniture | pages [5] -->
微信公众号：数学模型

<!-- b000126 | furniture | pages [5] -->
Page 5 of 22

<!-- b000127 | prose | pages [5] -->
To smooth the modelling process, we remove all artists who could not be located in a certain category in the data set inﬂuence_data. Furthurmore, we do the normalization

<!-- b000128 | prose | pages [5] -->
微信公众号：数学模型

<!-- b000129 | prose | pages [5] -->
work on all the music characteristics in advance, in order to eliminate the effects of different dimensions when measuring these characteristics.

<!-- b000130 | heading | pages [5] -->
Basic Models: The inﬂuencer Network and Similar-

<!-- b000131 | prose | pages [5] -->
3 ity

<!-- b000132 | prose | pages [5] -->
First of all, in order to understand how the music evolves through inﬂuence across artists, we build the basic model to describe this kind of inﬂuencing relationship by networks and develop the concept of similarity between artists or genres.

<!-- b000133 | prose | pages [5] -->
微信号：MATHmodels

<!-- b000134 | prose | pages [5] -->
3.1 Directed Inﬂuencer Network

<!-- b000135 | caption | pages [5] -->
Figure 2: A Part of the Directed Inﬂuencer

<!-- b000136 | caption | pages [5] -->
Figure 1: The Full View of the Directed In-

<!-- b000137 | prose | pages [5] -->
Network

<!-- b000138 | prose | pages [5] -->
ﬂuencer Network

<!-- b000139 | prose | pages [5] -->
We use a network to show the relationship between inﬂuencers and their follow- ers, and the size of each node represents the artist’s MI. When building the inﬂuence networks, we ﬁrst select all the artists who started their careers in the 1930s from "inﬂu- ence_data" and put them on nodes. Then, we seek out those artists in the next decade, the 1940s, and put them inside the circle of the former ones, connecting inﬂuencers and followers with directed lines pointing to the followers. By doing so to artists from each decade, we get an inﬂuencing network in the end as shown in ﬁgure xxx. The dots near the center represents artists of recent decades and vice versa. From the full view we can see that there are some artists who started early in 20th century but have great im- pact on artists of all decades. We also discover that the center of network seems quite messy, implying a complex inﬂuencing relationship of artists nowadays. Apart from

<!-- b000140 | furniture | pages [5] -->
微信号：MATHmodels

<!-- b000141 | prose | pages [5] -->
关注数学模型

<!-- b000142 | furniture | pages [5] -->
2

<!-- b000143 | furniture | pages [5] -->
MATHmodels

<!-- b000144 | furniture | pages [5] -->
获取更多资讯

<!-- b000145 | furniture | pages [6] -->
Team # 2121604

<!-- b000146 | furniture | pages [6] -->
微信公众号：数学模型

<!-- b000147 | furniture | pages [6] -->
Page 6 of 22

<!-- b000148 | prose | pages [6] -->
微信公众号：数学模型

<!-- b000149 | caption | pages [6] -->
Figure 3: A Partial Enlarged Network to Show Inﬂuencing Details

<!-- b000150 | prose | pages [6] -->
微信号：MATHmodels

<!-- b000151 | prose | pages [6] -->
the full view of the network, we also show the partial enlarged network to illustrate the inﬂuencing directions and names of some artists that can be observed.

<!-- b000152 | prose | pages [6] -->
3.2 Musical Inﬂuence

<!-- b000153 | prose | pages [6] -->
In order to measure music inﬂuence, we should reasonably sum the number of artists affected by different durations. Considering that the inﬂuence of songs changes over time as well as the cooling of high-temperature objects should show a downward trend, and the speed of decline is fast and then slow, we use the cooling model to simulate the general trend of inﬂuence. Imagine how shocked you were when you ﬁrst heard electronic music. And when you listen to a lot of similar works, listening to new songs in the same category is not refreshing. However, considering the actual situation, the decline may not be manifested within the ﬁrst decade (this will be reﬂected in more detail in the next 3.3), just like a cup of hot water can remains hot for a short period of time. We need to refer to real data to simulate this delay process and calculate the delay function. The combined effect of the two produces MI coefﬁcient. First, solve the cooling model. The rate of MI decline is proportional to the difference between its current year’s inﬂuence and the last year. which is

<!-- b000154 | prose | pages [6] -->
MI′ (t) = −α(MI (t) −MI0)

<!-- b000155 | prose | pages [6] -->
Integrate and solve the equation, we can get

<!-- b000156 | prose | pages [6] -->
(1)

<!-- b000157 | prose | pages [6] -->
MI (t) = MI0 + Ce−at (2)

<!-- b000158 | prose | pages [6] -->
Where C is a constant and α is the attenuation coefﬁcient. Assuming that at time t_0, the musician’s inﬂuence is MI(t_0), substituting (2) into (1) and we can get

<!-- b000159 | prose | pages [6] -->
MI(t) = MI0 + (MI(t0) −MI0)e−a(t−t0) (3)

<!-- b000160 | prose | pages [6] -->
Assuming that after many years, the inﬂuence drops to a negligible level, we think MI_0=0. At this time, (3) can be simpliﬁed to

<!-- b000161 | furniture | pages [6] -->
微信号：MATHmodels

<!-- b000162 | prose | pages [6] -->
(4)关注数学模型 MI(t) = MI(t0)e−a(t−t0)

<!-- b000163 | furniture | pages [6] -->
2

<!-- b000164 | furniture | pages [6] -->
MATHmodels

<!-- b000165 | furniture | pages [6] -->
获取更多资讯

<!-- b000166 | furniture | pages [7] -->
微信公众号：数学模型

<!-- b000167 | furniture | pages [7] -->
Team # 2121604

<!-- b000168 | furniture | pages [7] -->
Page 7 of 22

<!-- b000169 | prose | pages [7] -->
It can be seen that the MI of the current year is related to the initial inﬂuence, attenua- tion coefﬁcient, and time interval. Secondly, we calculated the average of the number of followers of "inﬂuence_data" every 10 years, and used MATLAB to perform smooth- ing spline ﬁtting to obtain the function f(t). Apply f(t) and MI(t) together on the known

<!-- b000170 | prose | pages [7] -->
微信公众号：数学模型

<!-- b000171 | prose | pages [7] -->
data set, and normalize the data to obtain the MI coefﬁcient.

<!-- b000172 | prose | pages [7] -->
3.3 Exploration of Subnetworks

<!-- b000173 | prose | pages [7] -->
When we selected the names of all the artists, we did not draw dots with varying sizes that represent their respective MI, otherwise the densely connected areas would become unclear. Hence, in this part, we will explain our futher exploration. Letting the lengendary electronic band Kraftwerk be the center, we create this subnetwork to give a detailed explanation of the inﬂuencing network and our measures of music inﬂuence.

<!-- b000174 | prose | pages [7] -->
微信号：MATHmodels

<!-- b000175 | caption | pages [7] -->
Figure 4: A Subnetwork of the Directed Inﬂuencer Network

<!-- b000176 | prose | pages [7] -->
From the subnetwork we can see how wide the inﬂuence of Kraftwerk is. There are 108 artists who have been inﬂuence by them and even the legendary musician David Bowie has been affected by this band. We can also spot that the decades of their fol- lowers range between the 1970s to the 2020s, which is a relatively long inﬂuencing time range. In the year he ﬁrst came out, he gained 30 followers. In the next 4 decades, he inﬂuenced 43, 25, 9 and 1 artists respectively. We found that Kraftwerk’s inﬂuence may reach its peak in the ﬁrst decade, which coincides with our assumption in 3.2. that MI doesn’t decrease directly. Through sampling and analysis of the overall data and more artists, we have veriﬁed this idea. The size of dots in this subnetwork stands for an artist’s MI . We ﬁnd that though the MI of Kraftwerk is comparably large, their fol- lower David Bowie owns a even larger scale of MI, suggesting that Bowie has greater music inﬂuence nowadays than Kraftwerk. This can be explained that due to the lin-

<!-- b000177 | furniture | pages [7] -->
微信号：MATHmodels

<!-- b000178 | prose | pages [7] -->
guistic and regional restrictions, the German band Kraftwerk is not that well-known关注数学模型

<!-- b000179 | furniture | pages [7] -->
2

<!-- b000180 | furniture | pages [7] -->
MATHmodels

<!-- b000181 | furniture | pages [7] -->
获取更多资讯

<!-- b000182 | furniture | pages [8] -->
Team # 2121604

<!-- b000183 | furniture | pages [8] -->
微信公众号：数学模型

<!-- b000184 | furniture | pages [8] -->
Page 8 of 22

<!-- b000185 | prose | pages [8] -->
as David Bowie, yet they have impacted artists who make bigger achievements after- wards and their inﬂuence in music really can’t be ignored.

<!-- b000186 | prose | pages [8] -->
微信公众号：数学模型

<!-- b000187 | prose | pages [8] -->
3.4 Music Similarity

<!-- b000188 | prose | pages [8] -->
The similarity of music can be comprehensively evaluated through multiple indica- tors. The "full_music_data" provides numerous indicators such as danceability, energy, valence, etc. However, some indicators, like energy, tempo and loudness, may overlap across each other when describing the music features and certain characteristics may be repeatedly considered when using high-dimensional data directly. Therefore, hav- ing removed characteristics that don’t belong to the songs’ creation, like release_date, count, etc., we employ PCA as a dimensionality reduction method to extract four prin- cipal factors for the exploration afterwards. Some of the values in the examination of PCA method are listed below:

<!-- b000189 | prose | pages [8] -->
微信号：MATHmodels

<!-- b000190 | prose | pages [8] -->
KMO Value 0.782 Barlett’s Test of Sphericity Approx.Chi-Square df Sig.

<!-- b000191 | prose | pages [8] -->
22406.735 78 0.000

<!-- b000192 | prose | pages [8] -->
Unless particularly speciﬁed, the following analysis will be based on these four factors. We choose the cosine similarity to describe the similarity between songs, artists and genres. According to the four characteristic values, we construct the eigenvector for each artist (i):

<!-- b000193 | prose | pages [8] -->
Fi = (Fi1, Fi2, Fi3, Fi4)

<!-- b000194 | prose | pages [8] -->
Calculate the cosine similarity between two eigenvectors as follows:

<!-- b000195 | prose | pages [8] -->
simij = p (Fi ∗Fj)

<!-- b000196 | prose | pages [8] -->
q

<!-- b000197 | prose | pages [8] -->
F 2

<!-- b000198 | prose | pages [8] -->
F 2

<!-- b000199 | prose | pages [8] -->
i ∗

<!-- b000200 | prose | pages [8] -->
j

<!-- b000201 | prose | pages [8] -->
The cosine similarity is the cosine of the angle between the two eigenvectors. Its value range is [-1,1]. The closer the value gets to 1, the more similar the two artists are, and vice versa. Compared with Euclidean distance, cosine similarity focuses on the difference between two samples in the scale of direction, and the similarity value range is automatically changed to [-1, 1], saving the need of normalization when applying Euclidean distance.

<!-- b000202 | prose | pages [8] -->
In order to test the reliability of our similarity algorithm, we use it to calculate the similarity of artists within genres and artists between genres. We extract the similarity between the artists of the same genre and the artists of the different genres, and draw the following density curve.

<!-- b000203 | prose | pages [8] -->
The yellow line represents similarity between artists within genres, while the pink represents between genres. The horizontal axis represents similarity, and the verti- cal axis represents density. It can be seen that the similarity of artists within genre is mostly around 0.6, while the similarity between artists of different genres is around - 0.1. This shows that artists within genres are more similar than artists between genres, which is consistent with common sense, proving that the measures of music similarity

<!-- b000204 | furniture | pages [8] -->
微信号：MATHmodels

<!-- b000205 | prose | pages [8] -->
is reasonable.

<!-- b000206 | prose | pages [8] -->
关注数学模型

<!-- b000207 | furniture | pages [8] -->
2

<!-- b000208 | furniture | pages [8] -->
MATHmodels

<!-- b000209 | furniture | pages [8] -->
获取更多资讯

<!-- b000210 | furniture | pages [9] -->
Team # 2121604

<!-- b000211 | furniture | pages [9] -->
微信公众号：数学模型

<!-- b000212 | furniture | pages [9] -->
Page 9 of 22

<!-- b000213 | prose | pages [9] -->
微信公众号：数学模型

<!-- b000214 | caption | pages [9] -->
Figure 5: The Similarity Density Curve of Artists Within/Between Genres

<!-- b000215 | prose | pages [9] -->
Development & Exploration: How Does Music Evolves? 4

<!-- b000216 | prose | pages [9] -->
微信号：MATHmodels

<!-- b000217 | prose | pages [9] -->
In the long river of music development, we will always see some important inﬂu- encers. They promote the development and transformation of music, and promote the exchange and integration of genres. This has allowed the music to gradually evolve from the original 9 genres to today’s 20 mainstream genres. Therefore, studying the similarity between genres will be very helpful for us to use scientiﬁc methods to inter- pret human history from a large amount of data. At the same time, those who have played a leading role in different eras are also worth analyzing.

<!-- b000218 | prose | pages [9] -->
The Impact if Inﬂuencers on Followers 4.1

<!-- b000219 | prose | pages [9] -->
Inﬂuencer’s Effect on Music Created by the Followers 4.1.1

<!-- b000220 | prose | pages [9] -->
The provided data set "inﬂuence_data" shows the correlation between followers and identiﬁed inﬂuencers. Nevertheless, these inﬂuencing relationships are based on artists’ or experts’ subjective judgment. In order to examine whether the inﬂuencing relationships actually exist, we calculate similarities between each follower and his inﬂuencers and compare their density curve with that of similarities between each fol- lower and other artists who are not his inﬂuencer, as shown in ﬁgure 6.

<!-- b000221 | prose | pages [9] -->
As we can see, the similarities between inﬂuencers and followers are around 0.8, while the similarities between followers and other artists drop to -0.1. Hence we con- clude that the identiﬁed inﬂuencers in the data set have indeed inﬂuenced their fol- lowers, at least in music creating process.

<!-- b000222 | prose | pages [9] -->
4.1.2 Contagious Characteristics

<!-- b000223 | prose | pages [9] -->
Among all the music characteristics provided, we suppose that some characteristics play more essential roles in the inﬂuencing process. These characteristics, namely con- tagious characteristics, may show higher similarity between inﬂuencers and followers. Consequently, the removal of them during the similarity calculation process may cause great decline in similarity. Since we suppose the contagious characteristics may vary across genres, we take the genre “Pop/Rock” as an example to plot the similarity den-关注数学模型

<!-- b000224 | furniture | pages [9] -->
微信号：MATHmodels

<!-- b000225 | furniture | pages [9] -->
2

<!-- b000226 | furniture | pages [9] -->
MATHmodels

<!-- b000227 | furniture | pages [9] -->
获取更多资讯

<!-- b000228 | furniture | pages [10] -->
微信公众号：数学模型

<!-- b000229 | furniture | pages [10] -->
Team # 2121604

<!-- b000230 | furniture | pages [10] -->
Page 10 of 22

<!-- b000231 | prose | pages [10] -->
微信公众号：数学模型

<!-- b000232 | caption | pages [10] -->
Figure 6: The Density Curve of Similarities Between Followers and Inﬂuencers

<!-- b000233 | prose | pages [10] -->
sity curve below to show detailed analysis.

<!-- b000234 | prose | pages [10] -->
微信号：MATHmodels

<!-- b000235 | caption | pages [10] -->
Figure 7: The Similarity Density Curves to Identify the Contagious Characteristics

<!-- b000236 | prose | pages [10] -->
Firstly, we use all the twelve music characteristics (excluding description charac- teristics unrelated to the creation of the song itself) to construct a 12-dimension eigen- vector for each inﬂuencer and follower and calculate their cosine similarity density, as shown in ﬁgure by the brown line and shade. Next, we respectively remove each of these characteristics and construct a 11-dimension eigenvector to calculate the similar- ity between inﬂuencer and follower again. We can see from the ﬁgure that the removal of acousticness and energy give rise to the biggest loss in similarity, while the removal of others only cause slight losses or even increases. Therefore, we draw the conclu- sion that energy and acousticness are relatively contagious characteristics in the genre “Pop/Rock, indicating that they are more likely to leave a deep impression on follow- ers and be imitated afterwards.

<!-- b000237 | prose | pages [10] -->
The full results of contagious characteristics is shown in ﬁgure 8. Generally speak- ing, tempo and danceability seem to be the most contagious among all the characteris- tics, given that they are respectively contagious in ﬁve genres.

<!-- b000238 | furniture | pages [10] -->
微信号：MATHmodels

<!-- b000239 | prose | pages [10] -->
关注数学模型

<!-- b000240 | furniture | pages [10] -->
2

<!-- b000241 | furniture | pages [10] -->
MATHmodels

<!-- b000242 | furniture | pages [10] -->
获取更多资讯

<!-- b000243 | furniture | pages [11] -->
Team # 2121604

<!-- b000244 | furniture | pages [11] -->
微信公众号：数学模型

<!-- b000245 | furniture | pages [11] -->
Page 11 of 22

<!-- b000246 | prose | pages [11] -->
微信公众号：数学模型

<!-- b000247 | caption | pages [11] -->
Figure 8: The Contagious Characteristics for Each Genre

<!-- b000248 | prose | pages [11] -->
4.2 Trends of Genres

<!-- b000249 | prose | pages [11] -->
4.2.1 Similarity of Genres

<!-- b000250 | prose | pages [11] -->
The characteristics of the genre are reﬂected by the characteristics of the songs cre-

<!-- b000251 | prose | pages [11] -->
微信号：MATHmodels

<!-- b000252 | prose | pages [11] -->
ated by the artists within the genre. According to the information about artists’ genre in ‘inﬂuence_data’, the genre of each artist in ‘data_by_artist’ can be identiﬁed. Ac- cording to fourth Assumption mentioned above, we believe that every artist can em- body the characteristics of the genre it represents. So we average the eigenvectors of all artists in each genre as the central value of each genre, and get 20 genres’ eigenvec- tors. We calculate the cosine similarity between 20 eigenvectors to obtain the similarity matrix of genres. For the convenience of observation, we have made a heat map as below. You can obtain the similarity between any two of the genres by checking out the grid in corresponding row and column. The darker the grid is, the higher the sim- ilarity should be. This cosine similarity matrix is a symmetrical matrix. You can see that the grid on the diagonal has the darkest color, demonstrating that each category has the highest similarity to itself. The following exploration of the trends of genres will mainly be based on this matrix of genre similarity.

<!-- b000253 | caption | pages [11] -->
Figure 9: The Heat Map of Similarities Between Genres

<!-- b000254 | prose | pages [11] -->
4.2.2 What Distinguishes a Genre?

<!-- b000255 | prose | pages [11] -->
When it comes to genre distinguishing, we suppose it nearly impossible to iden-

<!-- b000256 | furniture | pages [11] -->
微信号：MATHmodels

<!-- b000257 | prose | pages [11] -->
tify a single characteristic to distinguish a particular genre from all the others. After关注数学模型

<!-- b000258 | furniture | pages [11] -->
2

<!-- b000259 | furniture | pages [11] -->
MATHmodels

<!-- b000260 | furniture | pages [11] -->
获取更多资讯

<!-- b000261 | furniture | pages [12] -->
微信公众号：数学模型

<!-- b000262 | furniture | pages [12] -->
Team # 2121604

<!-- b000263 | furniture | pages [12] -->
Page 12 of 22

<!-- b000264 | prose | pages [12] -->
all, we’ve got nearly twenty super-genres in total and some of them barely have any similarities, yet others may have close resemblance. As a result, we choose to answer the question of distinguishing a genre by explaining how to distinguish similar gen- res from one another, using R&B as an example. We can see from ﬁgure 10(heatmap)

<!-- b000265 | prose | pages [12] -->
微信公众号：数学模型

<!-- b000266 | prose | pages [12] -->
that R&B is quite similar to Blues and Jazz. As a matter of fact, R&B, also known as Rhythm and Blues, has its origins in other Black Music including Jazz and Blues. Aim- ing to distinguish R&B from its two origins, we make a radar chart based on the genres’ four factors explained in the previous article.

<!-- b000267 | prose | pages [12] -->
微信号：MATHmodels

<!-- b000268 | caption | pages [12] -->
Figure 10: How to Distinguish R&B from Jazz or Blues?

<!-- b000269 | prose | pages [12] -->
From the chart we can know that the major difference between R&B and Jazz lays in Factor 1, and though R&B and Blues are quite similar, they are still different in Factor 2. Consulting to the component matrix generated in the PCA method, we know that Factor 1 better explains the characteristics of energy and loudness, while Factor 2 better explains valence and danceability. Hence we come the conclusion that we may distinguish R&B from Jazz by energy and loudness, and from Blues by valence and danceability. In fact, the name Rhythm and Blues implies that there are more rhythmic elements within the music like rap or hip-hop, while Jazz applies more importance to chords and tones and Blues focuses on melody and responses from the audience. So our distinguishing method proves to be practicable on the common sense.

<!-- b000270 | prose | pages [12] -->
4.2.3 The General Evolution of Genres

<!-- b000271 | prose | pages [12] -->
Although there are many genres of music ﬂooding the market every year, there is always one genre of music that is the most popular in each year. As long as we can identify the most popular music genre each year, we can know how genres change over time. Therefore, we establish a "Gravity Model" to solve this task. Considering that physical mass objects will have a gravitational inﬂuence on other objects placed in their space, the popularity of songs has a similar "attractive" effect to the music trend. We make full use of the “data_by_year” data set to gain music characteristics information and social feedback like "popularity", to establish the "gravity model" .

<!-- b000272 | prose | pages [12] -->
In this model, we regard the genre and the most popular genre of the year (which

<!-- b000273 | furniture | pages [12] -->
微信号：MATHmodels

<!-- b000274 | prose | pages [12] -->
remains unknown untill we ﬁnd it) as quality spheres G and u respectively. There is关注数学模型

<!-- b000275 | furniture | pages [12] -->
2

<!-- b000276 | furniture | pages [12] -->
MATHmodels

<!-- b000277 | furniture | pages [12] -->
获取更多资讯

<!-- b000278 | furniture | pages [13] -->
Team # 2121604

<!-- b000279 | furniture | pages [13] -->
微信公众号：数学模型

<!-- b000280 | furniture | pages [13] -->
Page 13 of 22

<!-- b000281 | prose | pages [13] -->
微信公众号：数学模型

<!-- b000282 | prose | pages [13] -->
Figure 11

<!-- b000283 | prose | pages [13] -->
微信号：MATHmodels

<!-- b000284 | prose | pages [13] -->
no interaction between the genres, and the genre only has a gravitational effect on u. The average of the popularity in each genre is taken as the quality M of G, and the eigenvector of the genre is taken as its coordinate. Similarly, the average popularity of all songs in each year is taken as the quality m of u, and the average value of the eigenvector is taken as the coordinate of u. The gravity of the ball G to the ball u should be proportional to the masses of M and m, and inversely proportional to the square of the distance between them. For example, G1 is farther from u than G2, but since the mass of G1 is greater than G2, which one’s gravitational force is bigger is not for sure. Since our previous work to solve similarity is relatively mature, and similarity and distance show an obvious inverse relationship, we use similarity to replace distance. Before we put sim into the funcion, we normalized it as simnew to make it ranges bewtween [0,1].

<!-- b000285 | prose | pages [13] -->
simnew = (1 + sim)

<!-- b000286 | prose | pages [13] -->
Gravity = GU

<!-- b000287 | prose | pages [13] -->
2

<!-- b000288 | prose | pages [13] -->
r2 →GU(sim2

<!-- b000289 | prose | pages [13] -->
new)

<!-- b000290 | prose | pages [13] -->
In our method, the G that has the greatest gravity with u is the most popular genre of the year. We calculated the dominant genre in each year from 1921 to 2020, as shown in the full view of the evolution timeline.

<!-- b000291 | prose | pages [13] -->
From the timeline we can see that before the 1950s, the dominant genres are pre- dominantly Jazz, Blues and Folk. Country and Vocal had chances of ﬂourishing in the 1950s, but it was Pop/Rock who won at last. From 1955 to 1976, Pop/Rock is al- most the dominant genre of every year, suggesting its unprecedented popularity. In the 1980s, however, R&B, Reggae and Folk started to stand out. When it comes to gen- res of the 21st century, the dominant genre becomes more various and we notice the emerging genres like New Age and Electronic are also gaining more popularity.

<!-- b000292 | furniture | pages [13] -->
微信号：MATHmodels

<!-- b000293 | prose | pages [13] -->
关注数学模型

<!-- b000294 | furniture | pages [13] -->
2

<!-- b000295 | furniture | pages [13] -->
MATHmodels

<!-- b000296 | furniture | pages [13] -->
获取更多资讯

<!-- b000297 | furniture | pages [14] -->
微信公众号：数学模型

<!-- b000298 | furniture | pages [14] -->
Team # 2121604

<!-- b000299 | furniture | pages [14] -->
Page 14 of 22

<!-- b000300 | prose | pages [14] -->
微信公众号：数学模型

<!-- b000301 | prose | pages [14] -->
微信号：MATHmodels

<!-- b000302 | caption | pages [14] -->
Figure 12: The Timeline of the Dominant Genre of Each Year

<!-- b000303 | prose | pages [14] -->
4.2.4 Relations Between Genres

<!-- b000304 | prose | pages [14] -->
Making use of the similarity matrix and heat map created above, we can grasp some relationships between those genres. For instance, we see that there is high similarity between Folk and Vocal. This kind of relations drawn from the numerical perspective can be explained by analyzing the music characteristic of genres. The well-known song "Blowin’ in the Wind" is a representative work of folk music. You can hear the melody sung by a clear male voice without much technical enhancement, indicating that folk music and vocal are very similar. Folk music and vocal are both genres with a long history, strong originality, and more prominent vocals. Let’s take another example. We can see from the heatmap that R&B and Reggae possess high cosine similarity close to 1.0, suggesting their strong relations. Virtually, both of them are typical Black Music contain lots of dance rhythms and drumbeats. Reggae stems from the so-called New Orleans R&B and has close relationship with the traditional R&B itself, which provides evidence for the strong relation identiﬁed in the heat map. In short, with the heatmap of the similarity between genres, we can easily identify how genres related to others and do further analysis on the basis of professional knowledge.

<!-- b000305 | furniture | pages [14] -->
微信号：MATHmodels

<!-- b000306 | prose | pages [14] -->
关注数学模型

<!-- b000307 | furniture | pages [14] -->
2

<!-- b000308 | furniture | pages [14] -->
MATHmodels

<!-- b000309 | furniture | pages [14] -->
获取更多资讯

<!-- b000310 | furniture | pages [15] -->
Team # 2121604

<!-- b000311 | furniture | pages [15] -->
微信公众号：数学模型

<!-- b000312 | furniture | pages [15] -->
Page 15 of 22

<!-- b000313 | prose | pages [15] -->
Evolution in A Speciﬁc Genre: Country 4.2.5

<!-- b000314 | prose | pages [15] -->
Having analyzed the overall trends of genres, we now zoom in to Country, this spe- ciﬁc genre, to gain better understanding of its inﬂuence processes and detailed evolu-

<!-- b000315 | prose | pages [15] -->
微信公众号：数学模型

<!-- b000316 | prose | pages [15] -->
tion. It is without a doubt that the greatest inﬂuencer of country music varies as the music itself develops. To identify the dynamic inﬂuencers of country music, we look for the most inﬂuential artists in country music in each decade since 1930 by ranking them in the order of popularity. We assume that the higher the popularity is, the wider inﬂuence this artist has on country music. Moreover, if there are two artists whose popularities are very near but have a huge difference in the counts of songs, we tend to recognize the artist with more songs as the dynamic inﬂuencer of the decade, consid- ering the contribution of the number of high-quality works. Using our method, there are seven dynamic inﬂuencers of country music, as shown in fugure 13.

<!-- b000317 | prose | pages [15] -->
微信号：MATHmodels

<!-- b000318 | caption | pages [15] -->
Figure 13: Dynamic Inﬂuencers of Country Music

<!-- b000319 | prose | pages [15] -->
Besides dynamic inﬂuencers, we also want to capture the fusion of country and other related genres. To achieve this goal, we use the "full_data" data set to generate the similarity between country music in each decade and all genres in the decade before. The result is shown in ﬁgure 14. For example, the country music in the 1960s is most similar to Pop/Rock of the 1950s, rather than country itself of the 1950s, indicating fusion of these two genres in the 1960s.

<!-- b000320 | caption | pages [15] -->
Figure 14: Related Genres of Country Music in Different Decades

<!-- b000321 | prose | pages [15] -->
Combining ﬁgure13 and ﬁgure14 together, we can analyze the evolution of country music in a more detailed way. Before 1960, the evolution of country went on smoothly and stuck to the traditional country music like Blue Grass Music. During this peace- ful period, prestigious musicians like Roy Acuff, Lefty frizzell and Johnny Cash are the greatest inﬂuencers of country music. However, as Rock and Roll arose in the 1960s, the country music experienced great fusion with other genres like Pop/Rock, Folk and Jazz. The traditional country music enjoyed a short time of revival during the 1980s due to the inﬂuential artist Alan Jackson and the birth of a subgenre called New Country. Nevertheless, traditional country music has ﬁnally been divided into more branches in the 21st century and the fusion between country and other genres never stops. In recent years, the most inﬂuential country musicians are Kenny Ches- ney and Luke Combs, who do well in combining country music with elements from

<!-- b000322 | furniture | pages [15] -->
微信号：MATHmodels

<!-- b000323 | prose | pages [15] -->
other genres.

<!-- b000324 | prose | pages [15] -->
关注数学模型

<!-- b000325 | furniture | pages [15] -->
2

<!-- b000326 | furniture | pages [15] -->
MATHmodels

<!-- b000327 | furniture | pages [15] -->
获取更多资讯

<!-- b000328 | furniture | pages [16] -->
Team # 2121604

<!-- b000329 | furniture | pages [16] -->
微信公众号：数学模型

<!-- b000330 | furniture | pages [16] -->
Page 16 of 22

<!-- b000331 | prose | pages [16] -->
From Evolution to Revolution 4.3

<!-- b000332 | prose | pages [16] -->
When Did the Revolutions Happen? 4.3.1

<!-- b000333 | prose | pages [16] -->
微信公众号：数学模型

<!-- b000334 | prose | pages [16] -->
Earlier in this article, we have made the most of our basic model to explore the evolutionary process of both artists and genres. Nevertheless, what matter more in music evolution are those revolutionary shifts that have taken music to the next level. We interpret “revolutions” as signiﬁcant leaps between two years during the evolution of music. Consequently, with the "data_by_year" data set, we calculate the values of four factors for each year following the PCA method described above. Having done that, we can get the cosine similarity between each year and its following year as an indicator to signify revolutions, as shown in ﬁgure 15.

<!-- b000335 | prose | pages [16] -->
微信号：MATHmodels

<!-- b000336 | caption | pages [16] -->
Figure 15: The Similarity Between Each Year and Its Following Year

<!-- b000337 | prose | pages [16] -->
The smaller the similarity is, the greater the difference exists between those two year. From the timeline we can conclude that most of the time the evolution of music is quite smooth, with the similarity between two years above 0.8. However, there are some dramatic decreases that have been marked red near the year 1929, 1938, 1945, 1949, 1966, 1974, 1980. Also, there are some small dips in the 21st century. These years which have a lower similarity with the year before can be seen as a period of music revolution, resulting in major leaps in music characteristics and signiﬁcant reduction of similarity. We ﬁnd that there are less revolution periods in recent years. Considering the diversity of music genres nowadays and the comparably peaceful world situation, we think this result is quite reasonable.

<!-- b000338 | prose | pages [16] -->
What Artists Represent Revolutionaries? 4.3.2

<!-- b000339 | prose | pages [16] -->
Artists who represent revolutionaries are those whose works have greatly inﬂu- enced artists of his time. Since revolutionaries varies with each revolution periods, we will just take the typical period 1965 1967 as an example and the revolutionaries of other periods can be analyzed with similar methods. To ﬁgure out who is the inﬂu- encer of the major change during this period, we analyze all the artists who released songs between 1965 and 1967 and their corresponding inﬂuencers. The result is shown in ﬁgure16, where the y-axis stands for the number of a particular inﬂuencer’s follow- ers who released songs during 1965 1967.

<!-- b000340 | prose | pages [16] -->
We can see from the ﬁgure that among all the artists active during 1965 1967, 94 of them have been inﬂuenced by The Beatles and 64 artists have been inﬂuenced by Bob Dylan, obviously outnumbering the other inﬂuencers. This can be explained by the striking British Invasion led by The Beatles and Dylan’s American responses to such

<!-- b000341 | furniture | pages [16] -->
微信号：MATHmodels

<!-- b000342 | prose | pages [16] -->
invasion. Since both The Beatles and Bob Dylan are well-known artists who started关注数学模型

<!-- b000343 | furniture | pages [16] -->
2

<!-- b000344 | furniture | pages [16] -->
MATHmodels

<!-- b000345 | furniture | pages [16] -->
获取更多资讯

<!-- b000346 | furniture | pages [17] -->
Team # 2121604

<!-- b000347 | furniture | pages [17] -->
微信公众号：数学模型

<!-- b000348 | furniture | pages [17] -->
Page 17 of 22

<!-- b000349 | prose | pages [17] -->
微信公众号：数学模型

<!-- b000350 | caption | pages [17] -->
Figure 16: The Greatest Inﬂuencer of the Revolution Occured in 1960s

<!-- b000351 | prose | pages [17] -->
微信号：MATHmodels

<!-- b000352 | prose | pages [17] -->
their career in the 1960s and play vital roles in the evolution of modern pop and rock, we consider them as the top two artists who can represent revolutionaries of the 1960s. Meanwhile,artists from the 1950s,like Hank Williams,Chuck Berry and Elvis Presley, may also resulted in the revolution between 1965 and 1967 more or less.

<!-- b000353 | prose | pages [17] -->
Other Factors in Music Evolution 4.4

<!-- b000354 | prose | pages [17] -->
4.4.1 Cultural Inﬂuence of Music

<!-- b000355 | prose | pages [17] -->
Although there is no culture-related data provided, we still can speculate about music impacts on culture based on the evolution timeline we’ve created in ﬁgure17. From the timeline we can see how typical Black Music (Jazz, Blues, Reggae, etc.) gained popularity in the western world and how music genres diversify in the 21st century. We explain those trends as implications of music’s inﬂuence on the revival of Black Culture and on the cultural globalization. However, these speculations need to be further investigated based on other data.

<!-- b000356 | prose | pages [17] -->
Social, Political, Technological Changes 4.4.2

<!-- b000357 | prose | pages [17] -->
Social or political changes often leads to abrupt shifts in social atmosphere and can therefore be related to musical revolutions. To explore effects on music of such changes, we consult some research in social science and identiﬁed major events happened in the revolution year that may have played a role in the revolution in ﬁgure17.

<!-- b000358 | prose | pages [17] -->
In addition, we analyze the start year of inﬂuencers of active artists in 1965 1967, and surprisingly ﬁnd that only 21 percent of the inﬂuencers are artists who launched their careers in the 1960s, which means active artists in 1965 1967 received the biggest inﬂuence from artists decades ago but made revolutionary work in the 1960s. So why hadn’t artists from the 1950s brought about the same revolution? We attribute the splendid music created during 1965 1967 to the unrest society in the 1960s. Due to events like Cuban Missile Crisis, Summer of Love and the Hippie Movement, African- American Civil Rights Movement led by Martin Luther King, the artists showed more

<!-- b000359 | furniture | pages [17] -->
微信号：MATHmodels

<!-- b000360 | prose | pages [17] -->
reﬂection of human rights and the rebellion spirit in their work in 1965 1967. The rise关注数学模型

<!-- b000361 | furniture | pages [17] -->
2

<!-- b000362 | furniture | pages [17] -->
MATHmodels

<!-- b000363 | furniture | pages [17] -->
获取更多资讯

<!-- b000364 | furniture | pages [18] -->
微信公众号：数学模型

<!-- b000365 | furniture | pages [18] -->
Team # 2121604

<!-- b000366 | furniture | pages [18] -->
Page 18 of 22

<!-- b000367 | prose | pages [18] -->
微信公众号：数学模型

<!-- b000368 | caption | pages [18] -->
Figure 17: Social or Political Events Realated to Music Revolutions

<!-- b000369 | prose | pages [18] -->
微信号：MATHmodels

<!-- b000370 | caption | pages [18] -->
Figure 18: The Start Year of Inﬂuencers of Active Artists in 1965 1967

<!-- b000371 | prose | pages [18] -->
of Pop/Rock during this time is the evidence of such effects.

<!-- b000372 | caption | pages [18] -->
Figure 19: The Decline in Acousticness

<!-- b000373 | prose | pages [18] -->
As for technological changes, we discover from evolution timeline that the bur- geoning genre “Electronic” is increasingly gaining popularity in the 21st century. Mean- while, the music characteristic “acousticness” has declined steadily in recent decades, implying more technological enhancements or electrical ampliﬁcation have been ap- plied to soundtracks.

<!-- b000374 | furniture | pages [18] -->
微信号：MATHmodels

<!-- b000375 | prose | pages [18] -->
关注数学模型

<!-- b000376 | furniture | pages [18] -->
2

<!-- b000377 | furniture | pages [18] -->
MATHmodels

<!-- b000378 | furniture | pages [18] -->
获取更多资讯

<!-- b000379 | furniture | pages [19] -->
Team # 2121604

<!-- b000380 | prose | pages [19] -->
5 Sensitive Analysis

<!-- b000381 | furniture | pages [19] -->
微信公众号：数学模型

<!-- b000382 | furniture | pages [19] -->
Page 19 of 22

<!-- b000383 | prose | pages [19] -->
The assessment of music inﬂuence has a signiﬁcant impact on the results of our ex-

<!-- b000384 | prose | pages [19] -->
微信公众号：数学模型

<!-- b000385 | prose | pages [19] -->
ploration. Different music inﬂuence values may lead to wrong judgment of the greatest inﬂuencer, which is inconsistent with the process of music history. However, whether the inﬂuence assessment is reasonable depends on the attenuation coefﬁcient in the cooling model we bulit in the earlier article. So here we will have a more in-depth discussion on the attenuation coefﬁcient. MI coefﬁcient can be effected by changing α. If the ﬂuctuation is too large or even destroyed the declining trend of music inﬂuence over time, we should give the model a second thought.

<!-- b000386 | prose | pages [19] -->
微信号：MATHmodels

<!-- b000387 | caption | pages [19] -->
Figure 20: Sensitivity of α

<!-- b000388 | prose | pages [19] -->
We can see that when α changes from 0.1 to 0.6, the overall trend of MI coefﬁcient varies the same over time. Meanwhile, the larger α is, the more inﬂuential the inﬂu- encer is in its active start year. When α=0.7, artist’s MI has the greatest inﬂuence in it’s active start year, and then gradually decreases. This situation should be avoided because it does not conform to the lag of the actual music popular trend. When α=0.6, the MI coefﬁcient of the inﬂuencers’active start year is already 0.97. We have made many attempts around 0.6 and found that the MI coefﬁcient changes become very sen- sitive and the trend is easy to be destroyed, which is not a good thing for different data sets. Therefore, the attenuation coefﬁcient α should be set between 0.1 to 0.6 where the model is relatively stable.

<!-- b000389 | furniture | pages [19] -->
微信号：MATHmodels

<!-- b000390 | prose | pages [19] -->
关注数学模型

<!-- b000391 | furniture | pages [19] -->
2

<!-- b000392 | furniture | pages [19] -->
MATHmodels

<!-- b000393 | furniture | pages [19] -->
获取更多资讯

<!-- b000394 | furniture | pages [20] -->
Team # 2121604

<!-- b000395 | prose | pages [20] -->
6 Assessment

<!-- b000396 | prose | pages [20] -->
6.1

<!-- b000397 | heading | pages [20] -->
Strengths

<!-- b000398 | furniture | pages [20] -->
微信公众号：数学模型

<!-- b000399 | furniture | pages [20] -->
Page 20 of 22

<!-- b000400 | prose | pages [20] -->
微信公众号：数学模型

<!-- b000401 | prose | pages [20] -->
Our models and solutions stand out on the following points:

<!-- b000402 | prose | pages [20] -->
• Our model contains both a macro description and a case-by-case analysis,provided a more accessible report for the ICM Society.

<!-- b000403 | prose | pages [20] -->
• The measurement scale is uniform. We all use cosine similarity to measure the degree of similarity between music, artists, and genres which ensure consistency and understandability.

<!-- b000404 | prose | pages [20] -->
• We creatively quoted physics models in to give a good answer.This communi- cates the links between disciplines and provides new ideas for answering math- ematical questions.

<!-- b000405 | prose | pages [20] -->
微信号：MATHmodels

<!-- b000406 | prose | pages [20] -->
• We analyzed the sensitivity of the parameters and got the range that can be changed, which provides hints for the users of the model.

<!-- b000407 | prose | pages [20] -->
6.2

<!-- b000408 | heading | pages [20] -->
Weaknesses

<!-- b000409 | prose | pages [20] -->
Due to the limitation in time and data, there are unavoidably some weaknesses in our models that we would like to improve and modify afterwards:

<!-- b000410 | prose | pages [20] -->
• The dimentionality reduction method can be further improved. Though the PCA method we use in this report pass the Barlett’s Test, there are still information losses while extracting the four factors. We hope to ﬁnd a better method to reduce the dimensionality in future exploration.

<!-- b000411 | prose | pages [20] -->
• The value of the coefﬁcient we use in the Cooling Model is assigned to by our- selves. Though it performs well in the sensitive analysis, we still hope to research more in this model and calculate the coefﬁcient with scientiﬁc data sets.

<!-- b000412 | prose | pages [20] -->
• Our exploration of the dominant genre of each year inevitably makes small mis- takes in some years. With more data provided, we hope to reform our algorithm and correct these errors.

<!-- b000413 | furniture | pages [20] -->
微信号：MATHmodels

<!-- b000414 | prose | pages [20] -->
关注数学模型

<!-- b000415 | furniture | pages [20] -->
2

<!-- b000416 | furniture | pages [20] -->
MATHmodels

<!-- b000417 | furniture | pages [20] -->
获取更多资讯

<!-- b000418 | furniture | pages [21] -->
Team # 2121604

<!-- b000419 | furniture | pages [21] -->
微信公众号：数学模型

<!-- b000420 | furniture | pages [21] -->
Page 21 of 22

<!-- b000421 | heading | pages [21] -->
Conclusion & Further Considerations: A Document

<!-- b000422 | prose | pages [21] -->
7 to the ICM Society

<!-- b000423 | prose | pages [21] -->
微信公众号：数学模型

<!-- b000424 | prose | pages [21] -->
Dear ICM Society:

<!-- b000425 | prose | pages [21] -->
We have ﬁnished all the tasks requested for the inﬂuence of music and our ap- proaches and values of work are listed below:

<!-- b000426 | prose | pages [21] -->
Above all, we create directed networks of music inﬂuence, where inﬂuencers are connected to followers.Then, we build a cooling model which depicts the declining trend to calculate MI. After the analysis of subnetwork, we ﬁnd that the inﬂuecing relationship in recent decades tends to be more complex and there may be some inﬂu- encers who have less MI nowadays but have inﬂuenced greater musicians in their ca- reer. In the second task, we calculate the cosine similarity using eigenvectors between artists or genres, which is generated through PCA method. We ﬁnd that the similar- ity within the genre is about 0.6, and the similarity between the genres is around -0.1, indicating that the artists within the genre are more similar.

<!-- b000427 | prose | pages [21] -->
微信号：MATHmodels

<!-- b000428 | prose | pages [21] -->
In the third task, we obtain the similarity matrix and have drawn the heat map to show which genre may relate to others. To distinguish similar genres, we selecte R&B to compare with jazz and blues, drawing the radar chart and found that the main difference with the former is energy, and with the latter is valence. We construct the eigenvector of each year and calculate the similarity with the central value of the genre one by one. We introduce the gravity model to measure the similarity and popularity at the same time, and judge the hottest music every year, so as to see how genres change over time. In the fourth task, by observing the density curve, we can see that the fol- lower has a high degree of similarity with its inﬂuencers, but a low degree of similarity with non-inﬂuencers, indicating that the inﬂuencer really has an impact. Then, by an- alyzing the impact of the lack of different features on the similarity within a speciﬁc genre, we ﬁnd the contagious characteristic for each genre. In the ﬁfth question, we are committed to ﬁnding turning points and important inﬂuencers in genre change. We draw a line chart by calculating the degree of similarity between years, and the inﬂection point is the year of major change. In this question, we add time limits to the selected data, and still use MI to ﬁnd greatest inﬂuencers in different time periods. The model has been well continued and developed. Finally, we combine models we’ve constructed and analyze the dynamic inﬂuencer and evolution trend of country music in details. Since the background of social environment is constantly reﬂected in our research process, our model not only works from the aspect of mathematics, but also adds the interaction of society and music, which makes the model more reliable.

<!-- b000429 | prose | pages [21] -->
However, our work is based on the data sets provided and hence may not apply to a larger scale of data. With richer data, we would optimize our models by re-ﬁtting the time curve in the Cooling Model to better capture one’s music inﬂuence and consider developing new indicators of dynamic inﬂuencers. As for furthur study in the ﬁeld of music, we recommend an exploration into how the fusion of genres emerges and how music revolutions relate to cultural changes , since we ﬁnd the fusion and branching of genres quite common and inﬂuential in music evolution. To summarize, we hope you can gain meaningful understanding of music evolution from our report and wish we all enjoy the happiness that music can bring to us afterwards!

<!-- b000430 | furniture | pages [21] -->
微信号：MATHmodels

<!-- b000431 | prose | pages [21] -->
Sincerely,

<!-- b000432 | furniture | pages [21] -->
Team #2121604关注数学模型

<!-- b000433 | furniture | pages [21] -->
2

<!-- b000434 | furniture | pages [21] -->
MATHmodels

<!-- b000435 | furniture | pages [21] -->
获取更多资讯

<!-- b000436 | furniture | pages [22] -->
微信公众号：数学模型

<!-- b000437 | furniture | pages [22] -->
Team # 2121604

<!-- b000438 | furniture | pages [22] -->
Page 22 of 22

<!-- b000439 | heading | pages [22] -->
References

<!-- b000440 | references | pages [22] -->
[1] History Detectives. PCB. 20th Century Music.

<!-- b000441 | references | pages [22] -->
微信公众号：数学模型

<!-- b000442 | references | pages [22] -->
[2] Nicola Orio, Antonio Roda. A measure of melody similarity based on a graph pre-

<!-- b000443 | references | pages [22] -->
sentation of the music structure. 10th International Society for Music Information

<!-- b000444 | references | pages [22] -->
Retrieval Conference (ISMIR 2009).

<!-- b000445 | references | pages [22] -->
[3] Juan P.Bello. Measuring structural similarity in music. IEEE Transactions on Au-

<!-- b000446 | references | pages [22] -->
dio, Speech, and Language Processing, 2011,19(7), 2013-2025.

<!-- b000447 | references | pages [22] -->
[4] G. Tzanetakis, P. Cook. Musical genre classiﬁcation of audio signals. IEEE Trans-

<!-- b000448 | references | pages [22] -->
actions on Speech and Audio Processing, vol. 10, no. 5, pp. 293-302, 2002

<!-- b000449 | references | pages [22] -->
[5] Schedl, Markus. Investigating country-speciﬁc music preferences and music rec-

<!-- b000450 | references | pages [22] -->
ommendation algorithms with the LFM-1b dataset[J]. International Journal of

<!-- b000451 | references | pages [22] -->
Multimedia Information Retrieval, 6(1):71-84,2017

<!-- b000452 | references | pages [22] -->
微信号：MATHmodels

<!-- b000453 | references | pages [22] -->
[6] Musicmap | The Genealogy and History of Popular Music Genres. (2020). Re-

<!-- b000454 | references | pages [22] -->
trieved February 5, 2021, from https://musicmap.info/

<!-- b000455 | furniture | pages [22] -->
微信号：MATHmodels

<!-- b000456 | references | pages [22] -->
关注数学模型

<!-- b000457 | furniture | pages [22] -->
2

<!-- b000458 | furniture | pages [22] -->
MATHmodels

<!-- b000459 | furniture | pages [22] -->
获取更多资讯
