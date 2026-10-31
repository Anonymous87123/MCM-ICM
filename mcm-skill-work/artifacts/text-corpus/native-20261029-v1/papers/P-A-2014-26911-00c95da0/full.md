# P-A-2014-26911-00c95da0

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Team Control

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | prose | pages [1] -->
Number

<!-- b000004 | prose | pages [1] -->
For office use only

<!-- b000005 | title | pages [1] -->
26911

<!-- b000006 | prose | pages [1] -->
For office use only T1 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T2 ________________

<!-- b000009 | prose | pages [1] -->
F1 ________________ F2 ________________ F3 ________________

<!-- b000010 | prose | pages [1] -->
Problem Chosen

<!-- b000011 | prose | pages [1] -->
T3 ________________ T4 ________________

<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | prose | pages [1] -->
F4 ________________

<!-- b000014 | title | pages [1] -->
B

<!-- b000015 | furniture | pages [1] -->


<!-- b000016 | furniture | pages [1] -->


<!-- b000017 | title | pages [1] -->
Who is the Centennial Best Coach?

<!-- b000018 | prose | pages [1] -->
In this paper, we present a three-stage comprehensive evaluation model. Firstly, in the light of the common sense and logical analysis, we deduce a detailed Assessment Metrics set (Winning Percentage, Stability, Championship Number, Personal Awards, Clicking Rate, Players’ Honors, Draftees by the professional league) and convert some abstract concepts to quantized and concrete values by utilizing unique methods including Google Trends to aid in our analysis. Then to simplify the following work, we filter the coach candidates according to the shared characteristics of excellent coaches and modify the index value with various methods. What’s more, as to the timeline deviation,  two modification models are proposed for our google trends statistics, a linear-fitting model and a weighted-sum model included.

<!-- b000019 | prose | pages [1] -->
Secondly, a model combining Analytical Hierarchy Process (AHP) and a novel method called Max Entropy Model (Maxent) based on Grey Relation Analysis (GRA)is applied in order to calculate both the subjective and objective weights. In our model, AHP diminishes the possible deviation of subjective weights, and Maxent based on GRA renders an insight into the intrinsic statistics and objective weights concerned are in turn provided.

<!-- b000020 | prose | pages [1] -->
In the final stage, we combine both weights mentioned above together to obtain the final comprehensive weights and in turn render the final ranking. According to relevant documents, our ranking results are fairly credible. Besides, we apply sensitive analysis to our model and test our model in women’s volleyball. The outcome of the model proves the robustness and universality in our model.

<!-- b000021 | furniture | pages [1] -->


<!-- b000022 | keywords | pages [1] -->
Key words:

<!-- b000023 | prose | pages [1] -->
Timeline deviation compensation      AHP      Maxent        GRA

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | furniture | pages [1] -->


<!-- b000028 | furniture | pages [1] -->


<!-- b000029 | furniture | pages [2] -->
Team # 26911

<!-- b000030 | furniture | pages [2] -->
Page 1 of 19

<!-- b000031 | prose | pages [2] -->
1

<!-- b000032 | heading | pages [2] -->
Introduction

<!-- b000033 | prose | pages [2] -->
When we are sitting on bleachers, cheering for a college football bowl game held in an immense college stadium, the hero behind the scenes should always be kept in our heart-the coach. Different coaches display their unique skills in training and communicating with their players, and, in the meantime, accom- plish different achievements in their career.

<!-- b000034 | prose | pages [2] -->
Different people hold distinct standards for the best coach all time. Much too subjective factors are involved in the personal evaluation of the ’best’. In this paper, however, we focus on ﬁguring out a more objective and convinc- ing approach to evaluating the best coach ever in the past century (1900-Now) .Considering the fact that a large proportion of this problem depends on the subjective factors, we build the following model in order that some implicit in- formation lurking in the problem can also be utilized to make the approach more robust and convincing:

<!-- b000035 | prose | pages [2] -->
• Step 1:According to the characteristics of the sports, we set the fundamen- tal assessment metrics in this problem and browse the Internet to obtain the relevant statistics.

<!-- b000036 | prose | pages [2] -->
• Step 2:Apply an improved Analytical Hierarchy Process (Synthesis Hier- archy Process) to this problem and calculate the subjective weights in the evaluation problem.

<!-- b000037 | heading | pages [2] -->
• Step 3:Combine Grey Relational Analysis (GRA) Model and Max Entropy

<!-- b000038 | prose | pages [2] -->
Model (MaXent) in Information Theory to provide a detailed insight into the objective weights.

<!-- b000039 | prose | pages [2] -->
• Step 4: Render the comprehensive assessment value of each candidates in this problem according to the subjective& objective weights and the rele- vant statistics in this problem and provide the best college coach all time in turn.

<!-- b000040 | prose | pages [2] -->
2

<!-- b000041 | heading | pages [2] -->
Background

<!-- b000042 | prose | pages [2] -->
American competitive sports are categorized to Professional Sports and A- mateur Sports. The former is in the charge of each professional clubs while the latter is mainly under the management of American Olympic Committee (AOC). American Olympic Committee divides its members into four groups which are respectively marked by ABCD. The group marked by B consists of the Nation- al Collegiate Athletic Association (NCAA) which is directly responsible for all

<!-- b000043 | furniture | pages [3] -->
Team # 26911

<!-- b000044 | furniture | pages [3] -->
Page 2 of 19

<!-- b000045 | prose | pages [3] -->
kinds of intercollegiate games. Owing to the great enthusiasm of the college for the sports and the large scale of the athletic teams in each school, the NCAA is thus a considerably enormous organization which is then subdivided into three divisions and dozens of leagues, where football, basketball, baseball, volleyball and some track and ﬁeld games are held annually.[1]

<!-- b000046 | prose | pages [3] -->
The different location in the divisions is a direct indicator of the level of this college’s athletic teams. Not only does the division I school pour more invest- ment to the sports teams but they are also capable of recruiting more potential players and more excellent coaches in the meantime.

<!-- b000047 | prose | pages [3] -->
Hence, an assumption can be made about this problem that the division one school in NCAA has greater strength in the athletic games and symbolizes the highest level among the American colleges.[2]

<!-- b000048 | prose | pages [3] -->
3

<!-- b000049 | heading | pages [3] -->
Model Assumptions and Deﬁnitions

<!-- b000050 | prose | pages [3] -->
3.1

<!-- b000051 | heading | pages [3] -->
Model Assumptions

<!-- b000052 | prose | pages [3] -->
• Top ﬁve coaches must be in the top divisions of NCAA (Division I for Baseball and Basketball, Division I-A for Football).

<!-- b000053 | prose | pages [3] -->
• The searched frequency of a coach on Google is in direct proportion to the prestige of him (her).

<!-- b000054 | prose | pages [3] -->
• The searched frequency is a nonlinear function of the current time and the coach’s retiring time.

<!-- b000055 | prose | pages [3] -->
• The number of websites returned by the Google search engine concerning an award name for the coach is in direct ratio with the importance of it.

<!-- b000056 | prose | pages [3] -->
• All the football championships of the same sport used in our model have the identical signiﬁcance.

<!-- b000057 | prose | pages [3] -->
• All the awards received by the players in one sport all used in our model to estimate a coachs ability of cultivating players can be seemed equally.

<!-- b000058 | prose | pages [3] -->
• The number of websites returned by the Google search engine concerning an award name for the coach is in direct ratio with the importance of it.

<!-- b000059 | prose | pages [3] -->
3.2 Parameter Deﬁnitions

<!-- b000060 | prose | pages [3] -->
m: Number of the evaluation index; n: Number of the evaluation object;

<!-- b000061 | furniture | pages [4] -->
Team # 26911

<!-- b000062 | furniture | pages [4] -->
Page 3 of 19

<!-- b000063 | prose | pages [4] -->
yi(k): the kth index value of evaluation object i; xi(k): the normalized kth index value of evaluation object i; x0(k): the ideal sequence in Grey Relation Analysis ∆i(k): Absolute difference γ(xi(k), x0(k)): grey relation coefﬁcient qi(k):grey relation depth coefﬁcient wj: the weight of the jth index in the second model(GRA&Maxent) vj: the weight of the jth index in the ﬁrst model(AHP) zj: the comprehensive weight of the jth index Ri: the ith coach’s renewed ranking after the weight is altered Qi: the ith coach’s ranking before the weight is altered. EI: absolute entropy increment SI: relative entropy increment

<!-- b000064 | prose | pages [4] -->
4 Assessment Metrics

<!-- b000065 | prose | pages [4] -->
To provide a detailed evaluation mechanism for the best college coach in a certain sports, we ﬁrst divide the inﬂuencing factor to three main parts, the per- formance of the teams, the capacity of cultivating & recruiting the players and the personal prestige of the coach. The three leading factors are then subdivided into some more detailed indexes.

<!-- b000066 | prose | pages [4] -->
4.1 Teams’ Performance

<!-- b000067 | prose | pages [4] -->
Undoubtedly, the prior factor in determining the overall level of a coach is the professional level of him (her). The most direct indicator of the level is the professional performance of the team.

<!-- b000068 | prose | pages [4] -->
4.1.1 Winning percentage in his (her) career

<!-- b000069 | prose | pages [4] -->
The most explicit indicator of the strength of a team is the statistical record- s in various competitive games, which in the meantime, can largely reﬂect the professional level of this coach. As is widely known, NCAA divides its members into different divisions and leagues.[2] These diverse divisions and leagues al- so indicate teams’ diverse levels and strengths in competitive sports. Hence, the division and the league the college is in should not be taken for granted in this is- sue. Thus, different weights must be applied to the statistics in the preprocessing

<!-- b000070 | furniture | pages [5] -->
Team # 26911

<!-- b000071 | furniture | pages [5] -->
Page 4 of 19

<!-- b000072 | prose | pages [5] -->
of the winning percentage according to the Division the team is in. We browse on the Internet for the top winning percentage records holders.[3][4][5][6][7]

<!-- b000073 | prose | pages [5] -->
4.1.2 Stability of the team’s performance

<!-- b000074 | prose | pages [5] -->
The stability of the performance should also be a main concern of us when analyzing the performance of the team. If a coach cannot keep the good perfor- mance of the team, but usually leads to great ups and downs of a team, then he (she) cannot be recognized as the ’best’ as well.[7]

<!-- b000075 | prose | pages [5] -->
4.1.3 Number of victories in signiﬁcant games

<!-- b000076 | prose | pages [5] -->
Because of the special game system of NCAA, different games have diverse importance. Thus, considerations should be taken into about the difference be- tween the weight of the games.

<!-- b000077 | prose | pages [5] -->
4.2 Player’s performance

<!-- b000078 | prose | pages [5] -->
Great coaches should also have great insight when recruiting the candidates of the team members, since the main role of the coach is selecting the seed play- ers for the team and motivating the players.

<!-- b000079 | prose | pages [5] -->
4.2.1 Professional honors of the players

<!-- b000080 | prose | pages [5] -->
On the one hand, in competitive sports, some personal honor is also award- ed to the talented and eye-catching players in the game.[8][9][10][11][12]

<!-- b000081 | prose | pages [5] -->
On the other hand, another indispensable element in assessing a coach’s leading ability is number of the players drafted by the professional athletic league in US.[13][14][15]

<!-- b000082 | prose | pages [5] -->
4.2.2 Academic Progress Rate(APR)

<!-- b000083 | prose | pages [5] -->
Despite the great emphasis on the sports teams, the majority of the colleges are still aimed at improving the overall academic performance of the students,especially for those Division I schools. Thus, Academic Progress Rate(APR) is recently in- troduced by NCAA to evaluate the overall level of the player’s academic per-

<!-- b000084 | furniture | pages [6] -->
Team # 26911

<!-- b000085 | furniture | pages [6] -->
Page 5 of 19

<!-- b000086 | prose | pages [6] -->
formances, which in turn aids in the assessment of the player’s comprehensive qualities.[16]

<!-- b000087 | prose | pages [6] -->
4.3 Personal Prestige

<!-- b000088 | prose | pages [6] -->
We believe that it sufﬁces to say that a superior college coach possesses good prestige. Nonetheless, there is no denying that great difﬁculty exists in the quan- tization of the ’prestige’ since it is a relatively abstract concept. In the following model, we ﬁgure out approaches to converting the abstract intangible concepts to some concrete number indexes.

<!-- b000089 | prose | pages [6] -->
4.3.1 Awards Received

<!-- b000090 | prose | pages [6] -->
The personal honors awarded to the coaches symbolize recognition from the professional committee, the media and the public. Organizations and media also award coach of the year to the eye-catching coach that year. But considerations should be taken about the diversity of the award’s weight.[17][18][19][20][21][22][23][24][25] [26][27][28][29][30]

<!-- b000091 | prose | pages [6] -->
4.3.2 Searched times (By Google Trends engine)

<!-- b000092 | prose | pages [6] -->
Google Trends engine cite31 is a public web facility of Google Inc., based on Google search, that shows how often a particular search-term is entered relative to the total search-volume across various regions of the world, and in various languages.[wiki] If a coach is searched more frequently, then assumption can be made that he is a ’popular’ and good coach in time. Utilizing Google Trends engine to obtain the relevant number of searched times.

<!-- b000093 | prose | pages [6] -->
4.4 Others Metrics

<!-- b000094 | prose | pages [6] -->
Apart from the metrics mentioned above, some seemingly insigniﬁcant fac- tors might also contribute to the evaluation of the coach.

<!-- b000095 | prose | pages [6] -->
• Scandal involved

<!-- b000096 | prose | pages [6] -->
• Outstanding historical contribution

<!-- b000097 | furniture | pages [7] -->
Team # 26911

<!-- b000098 | furniture | pages [7] -->
Page 6 of 19

<!-- b000099 | prose | pages [7] -->
• Money manipulating rights

<!-- b000100 | prose | pages [7] -->
• Salary

<!-- b000101 | prose | pages [7] -->
• · · ·

<!-- b000102 | prose | pages [7] -->
However, these factors are too abstract to be quantized, which means that they can hardly be utilized in our model.

<!-- b000103 | prose | pages [7] -->
5

<!-- b000104 | heading | pages [7] -->
Models

<!-- b000105 | prose | pages [7] -->
5.1 Preliminary Filtering of the Candidates Coach:

<!-- b000106 | prose | pages [7] -->
Due to the great amount of the existent data, simpliﬁcation is required to make it executable. We ﬁrst ﬁnd out the coaches working for the Division I teams (Division I-A for college football) who ranks the top 20 in winning percentage and have a minimum training age of 10 years.

<!-- b000107 | prose | pages [7] -->
5.1.1 Pre-Standards for ﬁltering

<!-- b000108 | prose | pages [7] -->
When we are assessing the best college coach of the century, huge amount of database statistics hinders the manual selection of the outstanding ones. Thus, ﬁrstly, the shared good characteristics of the excellent coaches are the ﬁlter stan- dard to provide easier and simpler method of later data processing.

<!-- b000109 | prose | pages [7] -->
Considering the special arrangement of NCAA’s games and the common s- tandard in evaluating an athletic coach, winning percentage and division loca- tion of the team are the two pre-standards in ﬁltering. The assumption stipu- lated here puts that the top 5 coaches must have a winning percentage record among the top 20 and work for the top-division teams in his (her) career.

<!-- b000110 | prose | pages [7] -->
5.1.2 Examination of the potential scandals

<!-- b000111 | prose | pages [7] -->
In both the competitive sports and the personal private life of the coaches, scandals are occasionally revealed about the coach which can soon ruin the sta- tus of the him (her) completely. Thus, an extra examination should not be taken for granted about the morality of the coach. After the examination, none of the candidates are found to involve in scandals.

<!-- b000112 | furniture | pages [8] -->
Team # 26911

<!-- b000113 | furniture | pages [8] -->
Page 7 of 19

<!-- b000114 | prose | pages [8] -->
5.2 Data Preprocessing

<!-- b000115 | prose | pages [8] -->
5.2.1 Preprocessing of Index Values

<!-- b000116 | prose | pages [8] -->
The Championship of a Coach When calculating the championships of a team, one important thing should be noted that the data collected in this problem is all in the division I, which means that the basis of our analysis is set in the top level division. Despite the slight difference in various championship games’ importance degree, it can still be assumed that these games have the identical signiﬁcance in this problem . For instance, in college football, there exist six bowl games championships, namely, the Rose Bowl, the Orange Bowl, the Sug- ar Bowl, the Cotton Bowl, the Chick-ﬁl-A Peach Bowl and the Fiesta Bowl.

<!-- b000117 | prose | pages [8] -->
The Personal Honor of a Player When collecting the personal awards data of a player, we ﬁrstly browse all kinds of awards for the players and search the database for the coach when the honor was awarded. In the realistic analysis of the data collected here, there is a considerably wide range of player awards annually and a long list of players in the meantime. Due to the tediousness of the information and the relatively slighter weight in this index, assumption can be made that all the awards can be seemed equally to simplify the problem. The absolute statistical number of awards can therefore symbolize the honor of a player.

<!-- b000118 | prose | pages [8] -->
The Number of Draftees into Later Professional League The number of draftees into later professional league symbolizes a coach’s ability to foster a potential player and supply seed players to the higher level of professional career. Be- cause of the lack of the available information about all players drafted to coach and the infeasibility of data processing, we simplify the problem by only taking the ﬁrst overall draft picks into consideration. The information about the ﬁrst overall draft picks, can add to the personal honor of a player and symbolize the overall draft pick data to some extent.

<!-- b000119 | prose | pages [8] -->
The Personal Honor of a Coach When counting the honors and awards of the 20 candidate coaches. However, different honors usually have diverse signif- icance. Compared with the analyzing method in players’ awards, the coach’s honor has direct relationship with the overall level of a coach. Thus, the signiﬁ- cance of the individual awards is calculated according to the number of websites returned by Google Search.

<!-- b000120 | prose | pages [8] -->
After the number of websites returned is obtained, a normalized method is calculated to derive the relative weights of each award. Deﬁne the number of

<!-- b000121 | furniture | pages [9] -->
Team # 26911

<!-- b000122 | furniture | pages [9] -->
Page 8 of 19

<!-- b000123 | prose | pages [9] -->
websites as ,,then the weights of the awards are calculated by the following ex- pression.Then, the weighted sum method is applied to the awards number and the relative index value of the coach is in turn obtained.

<!-- b000124 | prose | pages [9] -->
5.2.2 Modiﬁcation of the Timeline

<!-- b000125 | prose | pages [9] -->
Modiﬁcation of Google Trends Data An inevitably tough problem is bound to happen when we are ranking the top college coach over the past century in terms of coach’s personal prestige, that is, the deviation brought about by the timeline. On the one hand, with time elapsing, the once prominent coach stands a good chance to fade the public. On the other hand, the popularity of the In- ternet also experiences great ups during the recent decades along the positive direction of the timeline. Both of the two factors mentioned above undermine the prestige of the early coach. To revise the model, we put forward two possi- ble amending and compensating methods. Undoubtedly, the deviation resulting from the timeline cannot be completely removed. However, the credibility and objectiveness are sure to be improved.

<!-- b000126 | prose | pages [9] -->
Timeline-Modiﬁcation Method based on Weighted Relative Searching Pop- ularity (WRSP)

<!-- b000127 | prose | pages [9] -->
Generally speaking , the attention on the coaches vary in different times due to some unique historic background, namely, war, ﬁnancial recession or some signiﬁcant revolution in this sport. Thus, if we only analyze the absolute atten- tion degree of a college coach, deviation will happen.

<!-- b000128 | prose | pages [9] -->
According to the analysis mentioned above, assumption can be made about this problem that the most outstanding coach in each era has approximately close public inﬂuence. Hence, the WRSP based modiﬁcation method is rectiﬁed in the following two aspects:

<!-- b000129 | prose | pages [9] -->
• Figure out ratio of the popularity index (relative searched times)the most popular coach in each era and the most popular one in recent decades.

<!-- b000130 | prose | pages [9] -->
• Refresh and rectify the statistics by multiplying the searched times in early era and the ratio.

<!-- b000131 | prose | pages [9] -->
Timeline-Modiﬁcation Method based on Compensational in Two Variables. Not only does Google Trends provide the relative popularity index of the key words in the individual search boxes, it also sketches the relative search record curve from 1994-2014. Search record curve reﬂects people’s attention on the searched coach and the trends of the popularity of the coach to some extent.The decade in this period can reﬂect the prestige of the coaches to some extent. Fur- ther analyzing leads to a classiﬁcation of clicking rates trends into 4 categories.

<!-- b000132 | furniture | pages [10] -->
Team # 26911

<!-- b000133 | furniture | pages [10] -->
Page 9 of 19

<!-- b000134 | prose | pages [10] -->
• A slowly declining trend.

<!-- b000135 | prose | pages [10] -->
• A stable trend

<!-- b000136 | prose | pages [10] -->
• A declining trend following a climb.

<!-- b000137 | prose | pages [10] -->
• Very low clicking rates.

<!-- b000138 | prose | pages [10] -->
Some assumptions are made about the most outstanding coaches through the analysis of the curve:

<!-- b000139 | prose | pages [10] -->
1.

<!-- b000140 | prose | pages [10] -->
For a coach before the Internet era, the clicking rates should be declining slowly because of the fewer opportunities for them to be known. For instance, for Knute Rockne, a college football coach,coaching from 1918-1930, the curve is shown in the following ﬁgure.

<!-- b000141 | caption | pages [10] -->
Figure 1: Google Trends Trend Sketch of Knute Rockne(1918-30)

<!-- b000142 | prose | pages [10] -->
2.

<!-- b000143 | prose | pages [10] -->
Those who haven’t access to Internet until retiring’s clicking rates should remain stable, since that when a well-known coach retires, the social inﬂuence will witness an apparent declination. However, during the period between 2004- 2014, a considerable number of people still have knowledge of the coach, thus the clicking rate will not change a lot. A peak might exist in this kind of trend especially in his or her retiring time.For example,Mike Krzyzewski,a college bas- ketball coach who retired in 2010,has the following trend sketch.

<!-- b000144 | caption | pages [10] -->
Figure 2: Google Trends Trend Sketch of Mike Krzyzewski(1976-2010)

<!-- b000145 | furniture | pages [11] -->
Team # 26911

<!-- b000146 | furniture | pages [11] -->
Page 10 of 19

<!-- b000147 | prose | pages [11] -->
3.

<!-- b000148 | prose | pages [11] -->
For those who are still coaching till now, the trend will exhibit a regular ups and downs and in the long time span between 2004-2014, conspicuous declining or inclining trend won’t happen.

<!-- b000149 | prose | pages [11] -->
Our initial intent if to compensate the deviation derived from the difference of the time and attempts are made to ﬁnd a linear or nonlinear ﬁtting function. However ,because of the limited data, we didn’t obtain an ideal outcome. We eventually decide to take it as an examinational standard for a ’best coach’, with relatively small weight in the evaluation system.

<!-- b000150 | prose | pages [11] -->
Modiﬁcation of Coach Awards Data From the awards data analysis,there is an apparent fact that almost all awards do not start from the same year.For a college sports coach, if he was in the time when few coach honors are awarded to the talented, then if we continue with our former analytical index calculation, bias and injustice will bring about considerable deviation to our model index analysis. In order to attenuate the inﬂuence of the timeline on the prestige of the coach, a modiﬁcation approach is applied to the problem here.

<!-- b000151 | prose | pages [11] -->
In different time, the awards set for the coaches, the number of the games and the recognition of the coach vary. Thus, when we are assessing the best coach, it is necessary to provide some compensation for the deviation due to the difference of time.

<!-- b000152 | prose | pages [11] -->
• 1. Modify the deviation of awards’ number Because the time awards are set is different from each other, thus the probability for the coach to win the award varies in the meantime. To compensate for the deviation, we set the ratio between the coach’s award number and the total number of awards when the coach was still coaching.

<!-- b000153 | prose | pages [11] -->
• 2. Modify the deviation of champion number Due to the different num- ber of games held in different time, the absolute number cannot symbolize the competence of the team accurately. Thus a comparative value is de- ﬁned as the ratio between the champion number of the coach and the total champion number.

<!-- b000154 | prose | pages [11] -->
• 3. Modify the deviation of clicking rates. Because the internet does not appear until the recent decades, the recognition of the coaches by the pub- lic varies. In order to compensate for this deviation, an index is set as the multiplication of the clicking rate and the retiring year of a coach.

<!-- b000155 | furniture | pages [12] -->
Team # 26911

<!-- b000156 | furniture | pages [12] -->
Page 11 of 19

<!-- b000157 | prose | pages [12] -->
5.3 Subjective Weights Analysis: Analytical Hierarchy Process (AHP)

<!-- b000158 | prose | pages [12] -->
Analytical Hierarchy Process (AHP) is a policy decision method which quan- tizes the subjective factors.[31] It aims at judging the importance degree between the two indexes and therefore simplifying a complex problem by decomposing the problem to several hierarchies and factors. Then, by examining the consis- tency of the pairwise matrix, we can minimize the evaluation deviation deriving from the subjective factors and thus render a more reasonable and convincing evaluation scheme systematically.[32]

<!-- b000159 | prose | pages [12] -->
In this problem, in light of the relevant index analysis mentioned above, the following Index Hierarchy Relationship Figure is displayed in Figure As is vividly shown in Figure 2, AHP provides a systematic assessment of the prob- lem and renders a detailed analysis of the weights for each index.

<!-- b000160 | caption | pages [12] -->
Figure 3: The Hierarchy of the Evaluation System in AHP

<!-- b000161 | prose | pages [12] -->
5.4 Objective Weights Analysis: Combined Method of Grey Re- lation Analysis based on Grey Relation Depth Coefﬁcient

<!-- b000162 | heading | pages [12] -->
and Max Entropy Model(Maxent)

<!-- b000163 | prose | pages [12] -->
After the subjective weight analysis based on Analytical Hierarchy Process(AHP), Grey Relation Analysis (GRA)[33]and Max Entropy Model(MaxEnt)[34] are then applied to the evaluation problem for the analysis of objective weight so as to fully exploit the hidden information. In the mathematical evaluation model, the observation sequence is set as the behavior sequence and a new concept de- ﬁned as the grey relation depth coefﬁcient (GRDC) is put to improve the model. The Max Entropy model is naturally built based on the GRDC to derive the ob- jective weight in view of MaxEnt Conﬁguration Model(MCM). This combined

<!-- b000164 | furniture | pages [13] -->
Team # 26911

<!-- b000165 | furniture | pages [13] -->
Page 12 of 19

<!-- b000166 | prose | pages [13] -->
application of three models better broadens the horizon for the comprehensive evaluation and provides an exhaustive relational degree between the evaluation objects and the evaluation indexes.

<!-- b000167 | prose | pages [13] -->
Grey relational Analysis (GRA) is a multi-factor analytical method. It de- scribes the relationship between the factors in line of the gray relation degree. It utilizes the degree of similarity between the geometrical shapes to judge the extent to which the sequences are related. The closer the curve is, the closer the relationship is too, and vice versa. Ideal sequence provided, which means a good standard is set for the evaluation model , we can thus assess a policy deci- sion’s merits by measuring the similarity of the sequence of the policy decision and that of the given ideal one.

<!-- b000168 | heading | pages [13] -->
Max Entropy Model(Maxent)

<!-- b000169 | prose | pages [13] -->
The principle was ﬁrst expounded by E.T. Jaynes in two papers in 1957 where he emphasized a natural correspondence between statistical mechanics and information theory. In information theory, information entropy signiﬁes the amount of the information, which inspires a new approach in maximize the usage of the information in statistical analysis. In actual, we always wish that we can retain the information itself and its uncertainty. Based on Maxent, speculations can be made about the possible distributional model and lurking information can be fully exploited.

<!-- b000170 | prose | pages [13] -->
In our model, we combine the two model mentioned above- GRA and Max- ent to fully exploit the existent information in our statistics.

<!-- b000171 | prose | pages [13] -->


<!-- b000172 | prose | pages [13] -->


<!-- b000173 | prose | pages [13] -->
· · · y2(1) y1(1)

<!-- b000174 | prose | pages [13] -->


<!-- b000175 | prose | pages [13] -->
yn(1)

<!-- b000176 | prose | pages [13] -->


<!-- b000177 | prose | pages [13] -->
· · · y2(2) y1(2)

<!-- b000178 | prose | pages [13] -->


<!-- b000179 | prose | pages [13] -->
Y =

<!-- b000180 | prose | pages [13] -->


<!-- b000181 | prose | pages [13] -->
...

<!-- b000182 | prose | pages [13] -->


<!-- b000183 | prose | pages [13] -->
yn(2)

<!-- b000184 | prose | pages [13] -->
  (1)

<!-- b000185 | prose | pages [13] -->
... ...

<!-- b000186 | prose | pages [13] -->
... ...

<!-- b000187 | prose | pages [13] -->


<!-- b000188 | prose | pages [13] -->
· · · y2(m) y1(m) yn(m)

<!-- b000189 | prose | pages [13] -->
Because of the difference between the property and the dimension, a standardiz- ing process is needed to standardize the evaluation matrix. In actual problems, properties can be categorized into three groups:

<!-- b000190 | prose | pages [13] -->
which is further described by the following expressions:

<!-- b000191 | prose | pages [13] -->
yi(k) −min

<!-- b000192 | prose | pages [13] -->
xi(k) =

<!-- b000193 | prose | pages [13] -->
yi(k) i

<!-- b000194 | prose | pages [13] -->
(2)

<!-- b000195 | prose | pages [13] -->
yi(k) −min

<!-- b000196 | prose | pages [13] -->
max

<!-- b000197 | prose | pages [13] -->
i

<!-- b000198 | prose | pages [13] -->
yi(k) i

<!-- b000199 | prose | pages [13] -->
we can then derive the standardized evaluation matrix as

<!-- b000200 | prose | pages [13] -->


<!-- b000201 | prose | pages [13] -->


<!-- b000202 | prose | pages [13] -->
· · · x2(1) x1(1)

<!-- b000203 | prose | pages [13] -->


<!-- b000204 | prose | pages [13] -->
xn(1)

<!-- b000205 | prose | pages [13] -->


<!-- b000206 | prose | pages [13] -->
· · · x2(2) x1(2)

<!-- b000207 | prose | pages [13] -->


<!-- b000208 | prose | pages [13] -->
X =

<!-- b000209 | prose | pages [13] -->


<!-- b000210 | prose | pages [13] -->
...

<!-- b000211 | prose | pages [13] -->


<!-- b000212 | prose | pages [13] -->
xn(2)

<!-- b000213 | prose | pages [13] -->
  (3)

<!-- b000214 | prose | pages [13] -->
... ...

<!-- b000215 | prose | pages [13] -->
... ...

<!-- b000216 | prose | pages [13] -->


<!-- b000217 | prose | pages [13] -->
· · · x2(m) x1(m) xn(m)

<!-- b000218 | furniture | pages [14] -->
Team # 26911

<!-- b000219 | furniture | pages [14] -->
Page 13 of 19

<!-- b000220 | prose | pages [14] -->
Now the preparing work has been ﬁnished and a standardized suitable for later data processing has been obtained.Next,we calculate the Grey Relation Coefﬁ- cient(GRC) concerning this problem. We reset Xi = xi(k)|k = 1, 2, ..., m(1, 2, ..., n) as the new system behavior sequence and X0 = (x0(1), x0(2), ...x0(m)) as the ide- al sequence, than we have the following expression to deﬁne the grey relation coefﬁcient between Xi and Xi as:

<!-- b000221 | prose | pages [14] -->
γ(Xi(k), X0(k)) = ∆min + ρ∆max

<!-- b000222 | prose | pages [14] -->
where

<!-- b000223 | prose | pages [14] -->
(4)

<!-- b000224 | prose | pages [14] -->
∆i(k) + ρ∆max

<!-- b000225 | prose | pages [14] -->
∆min = min |xi(k) −x0(k)| (5)

<!-- b000226 | prose | pages [14] -->
∆i(k) = |xi(k) −x0(k)|.

<!-- b000227 | prose | pages [14] -->
(6)

<!-- b000228 | prose | pages [14] -->
∆max = max |xi(k) −x0(k)|, (7)

<!-- b000229 | prose | pages [14] -->
After we have obtained the Grey Relation Coefﬁcients, the degree of relationship between the indexes can be quantized. However,in order to construct the index- weight model, further data processing is required to quantize the inner-relation between the sequence elements. Another concept is then put forward to reﬂect the relative importance of the indexes in the evaluation sequences.

<!-- b000230 | prose | pages [14] -->
γ(Xi(k), X0(k)) qi(k) = n∑

<!-- b000231 | prose | pages [14] -->
(8)

<!-- b000232 | prose | pages [14] -->
γ(Xi(k), X0(k))

<!-- b000233 | prose | pages [14] -->
i=1

<!-- b000234 | prose | pages [14] -->
∑

<!-- b000235 | prose | pages [14] -->
D(k) = 1

<!-- b000236 | prose | pages [14] -->
n

<!-- b000237 | prose | pages [14] -->
i=1

<!-- b000238 | prose | pages [14] -->
n n

<!-- b000239 | prose | pages [14] -->
(qi(k) −1

<!-- b000240 | prose | pages [14] -->
n)2 (9)

<!-- b000241 | prose | pages [14] -->
where qi(k) is the Gray Relation Depth Coefﬁcients(GRDC).

<!-- b000242 | prose | pages [14] -->
In line of the former analysis, the range of a certain index’s weight can be determined by the Grey Relation Depth Coefﬁcient, thus, the weight’s range can be expressed as below.

<!-- b000243 | prose | pages [14] -->
wk ∈[min(qi(k)), max(qi(k))], (10)

<!-- b000244 | prose | pages [14] -->
i = 1, 2, ..., n,

<!-- b000245 | prose | pages [14] -->
k = 1, 2, ..., m.

<!-- b000246 | prose | pages [14] -->
The range of the variance of the weight should also be taken into considera- tion and its range is also directly related to the GRDC.

<!-- b000247 | prose | pages [14] -->
m ∑

<!-- b000248 | prose | pages [14] -->
1

<!-- b000249 | prose | pages [14] -->
(wk −1

<!-- b000250 | prose | pages [14] -->
m)2 ⊂(min(D(k)), max(D(k)))

<!-- b000251 | prose | pages [14] -->
m

<!-- b000252 | prose | pages [14] -->
k=1

<!-- b000253 | prose | pages [14] -->
(11)

<!-- b000254 | prose | pages [14] -->
k = 1, 2, ..., m

<!-- b000255 | furniture | pages [15] -->
Team # 26911

<!-- b000256 | furniture | pages [15] -->
Page 14 of 19

<!-- b000257 | prose | pages [15] -->
Combining the analysis mentioned above, a Max Entropy Model of the index’s weight can be constructed as follows. It is equivalent to an Optimal Program- ming Problem(OOP) and it can be proved that this programming problem has an optimal solution.

<!-- b000258 | prose | pages [15] -->
m ∑

<!-- b000259 | prose | pages [15] -->
F = − max

<!-- b000260 | prose | pages [15] -->
wk ln wk

<!-- b000261 | prose | pages [15] -->
k=1

<!-- b000262 | prose | pages [15] -->
m ∑

<!-- b000263 | prose | pages [15] -->
wk = 1,

<!-- b000264 | prose | pages [15] -->
s.t.

<!-- b000265 | prose | pages [15] -->
k=1

<!-- b000266 | prose | pages [15] -->
wk ⊂(0, 1),

<!-- b000267 | prose | pages [15] -->
(LP)

<!-- b000268 | prose | pages [15] -->
(12)

<!-- b000269 | prose | pages [15] -->
wk ∈[min(qi(k)), max(qi(k))],

<!-- b000270 | prose | pages [15] -->
m ∑

<!-- b000271 | prose | pages [15] -->
(wk −1

<!-- b000272 | prose | pages [15] -->
1

<!-- b000273 | prose | pages [15] -->
m)2 ⊂(min(D(k)), max(D(k)))

<!-- b000274 | prose | pages [15] -->
m

<!-- b000275 | prose | pages [15] -->
k=1

<!-- b000276 | prose | pages [15] -->
6

<!-- b000277 | heading | pages [15] -->
Results

<!-- b000278 | prose | pages [15] -->
From the information mentioned above, by following the steps of the mod- el, we can ﬁnally ﬁgure out both the AHP weight and the Maxent&GRC Weight. The value of the weight’s elements are sequentially Winning Percentage,Variance,Team championship,Player Award,Player draftees to professional league,Personal Honor,Clicking Rate on Google

<!-- b000279 | prose | pages [15] -->
According to the expression:

<!-- b000280 | prose | pages [15] -->
zj = wjvj ∑ ∑

<!-- b000281 | prose | pages [15] -->
(13)

<!-- b000282 | prose | pages [15] -->
wjvj

<!-- b000283 | prose | pages [15] -->
j j

<!-- b000284 | prose | pages [15] -->
We can derive the value of the comprehensive weight z. The three weights of the three sports and the top coaches according to our evaluation system are listed in the following tables respectively.

<!-- b000285 | furniture | pages [16] -->
Team # 26911

<!-- b000286 | furniture | pages [16] -->
Page 15 of 19

<!-- b000287 | prose | pages [16] -->
7

<!-- b000288 | heading | pages [16] -->
Model Testing

<!-- b000289 | prose | pages [16] -->
The change of the results arising from the slight variation of the model weight- s is applied to aid in the analysis of sensitivity.

<!-- b000290 | prose | pages [16] -->
7.1

<!-- b000291 | heading | pages [16] -->
Sensitivity Analysis

<!-- b000292 | prose | pages [16] -->
7.1.1

<!-- b000293 | heading | pages [16] -->
Sensitivity Analysis of Grey Relation Analysis based on Max Entropy

<!-- b000294 | heading | pages [16] -->
Model

<!-- b000295 | prose | pages [16] -->
According to the change of the rankings, the concept of Entropy Increase(EI) is introduced to the evaluation system.

<!-- b000296 | prose | pages [16] -->
The entropy increase is deﬁned as the relative average increment in the rank- ing after the weights are slightly altered.

<!-- b000297 | prose | pages [16] -->
20 ∑

<!-- b000298 | prose | pages [16] -->
EI = 1

<!-- b000299 | prose | pages [16] -->
(Ri −Qi).

<!-- b000300 | prose | pages [16] -->
20

<!-- b000301 | prose | pages [16] -->
i=1

<!-- b000302 | furniture | pages [17] -->
Team # 26911

<!-- b000303 | furniture | pages [17] -->
Page 16 of 19

<!-- b000304 | prose | pages [17] -->
where Ri denotes the nth coach’s renewed ranking after the weight is altered, while Qi denotes the ranking before the alternation.

<!-- b000305 | prose | pages [17] -->
Take the baseball for example, when the weight of the variance is increased by 20%, the EI will be 0.2. Hence,the Sensitivity Index(SI) of this model will be

<!-- b000306 | prose | pages [17] -->
SI = (0.2 ÷ 20)% = 0.01% (14)

<!-- b000307 | prose | pages [17] -->
The Sensitivity Index shown above means that when the weight of variance is increased by 1%,the EI will in turn increase by 0.01%. Thus, conclusions an be made that the sensitivity of Grey Relation Analysis based on Max Entropy Model and the slight variation of the model’s weight has minor effects on the outcomes of our model.

<!-- b000308 | prose | pages [17] -->
7.1.2

<!-- b000309 | heading | pages [17] -->
Sensitivity Analysis of Analytical Hierarchy Process

<!-- b000310 | prose | pages [17] -->
In the same context as the last section, we recalculate the sensitivity index of the Analytical Hierarchy Process model, which leads to the result:

<!-- b000311 | prose | pages [17] -->
SI = (0.1 ÷ 20)% = 0.005% (15)

<!-- b000312 | prose | pages [17] -->
Similarly,we can conclude that the variation of parameters in the weight has minor inﬂuence on the results and our model is very robust.

<!-- b000313 | prose | pages [17] -->
7.2 Universality Testing

<!-- b000314 | prose | pages [17] -->
We apply our model to the college volleyball coaches and render the follow- ing rankings.

<!-- b000315 | furniture | pages [18] -->
Team # 26911

<!-- b000316 | furniture | pages [18] -->
Page 17 of 19

<!-- b000317 | prose | pages [18] -->
8

<!-- b000318 | heading | pages [18] -->
Strengths and Weaknesses

<!-- b000319 | heading | pages [18] -->
Strengths

<!-- b000320 | prose | pages [18] -->
• We apply an improved novel concept Grey Relation Depth Coefﬁcient (GRD- C) into the Grey Relation Analysis and combine the subjective and objec- tive weights together to render a more convincing and efﬁcient evaluation model.

<!-- b000321 | prose | pages [18] -->
• Multiple Internet tools are utilized to convert the abstract and unquanti- zable index to numerical values.i.e.the master use of Google Trends and Google Search Database.

<!-- b000322 | prose | pages [18] -->
• The two models are proved to be robust to variation of index values and the comprehensive evaluation results are proved to be consistent with the reality according to the existent documents.

<!-- b000323 | heading | pages [18] -->
Weaknesses

<!-- b000324 | prose | pages [18] -->
• In the competition involving multiple teams, winning percentage does not make sense in assessing the team’s performance.Extra adjustments of pro- cessing data will be required under that circumstances.

<!-- b000325 | prose | pages [18] -->
• When calculating the comprehensive weight, we suppose that Maxent and AHP have same importance to simplify problem.However,things might be much more complicated in reality.

<!-- b000326 | prose | pages [18] -->
• Model’s outcome greatly depends on given statistics.Thus,the outcome might not be robust if lots of information is lost.

<!-- b000327 | heading | pages [18] -->
References

<!-- b000328 | references | pages [18] -->
[1] http://en.wikipedia.org/wiki/National_Collegiate_

<!-- b000329 | references | pages [18] -->
Athletic_Association.

<!-- b000330 | references | pages [18] -->
[2] http://baike.baidu.com/view/68509.htm.

<!-- b000331 | references | pages [18] -->
[3] http://baike.baidu.com/link?url=pciZbXKhxFyFNtvdnrFMtYoYhwCFwvvErTVG

<!-- b000332 | references | pages [18] -->
[4] http://fs.ncaa.org/Docs/stats/football_records/DI/

<!-- b000333 | references | pages [18] -->
2010/Coaching.pdf.

<!-- b000334 | furniture | pages [19] -->
Team # 26911

<!-- b000335 | furniture | pages [19] -->
Page 18 of 19

<!-- b000336 | references | pages [19] -->
[5] http://fs.ncaa.org/Docs/stats/basketball_records/DI/

<!-- b000337 | references | pages [19] -->
2010/Coaching.pdf.

<!-- b000338 | references | pages [19] -->
[6] http://fs.ncaa.org/Docs/stats/baseball_records/DI/

<!-- b000339 | references | pages [19] -->
2010/Coaching.pdf?.

<!-- b000340 | references | pages [19] -->
[7] http://web1.ncaa.org/stats/StatsSrv/careersearch.

<!-- b000341 | references | pages [19] -->
[8] http://en.wikipedia.org/w/index.php?search=john+woody+

<!-- b000342 | references | pages [19] -->
award+&button=&title=Special%3ASearch.

<!-- b000343 | references | pages [19] -->
[9] http://en.wikipedia.org/wiki/Naismith_College_Player_

<!-- b000344 | references | pages [19] -->
of_the_Year.

<!-- b000345 | references | pages [19] -->
[10] http://en.wikipedia.org/wiki/Oscar_Robertson_Trophy.

<!-- b000346 | references | pages [19] -->
[11] http://en.wikipedia.org/wiki/Naismith_College_Player_

<!-- b000347 | references | pages [19] -->
of_the_Year.

<!-- b000348 | references | pages [19] -->
[12] http://en.wikipedia.org/wiki/NABC_Player_of_the_Year.

<!-- b000349 | references | pages [19] -->
[13] http://en.wikipedia.org/wiki/NBA_draft_first_pick.

<!-- b000350 | references | pages [19] -->
[14] http://en.wikipedia.org/wiki/List_of_first_overall_

<!-- b000351 | references | pages [19] -->
NFL_draft_picks.

<!-- b000352 | references | pages [19] -->
[15] http://en.wikipedia.org/wiki/List_of_first_overall_

<!-- b000353 | references | pages [19] -->
MLB_draft_picks.

<!-- b000354 | references | pages [19] -->
[16] http://en.wikipedia.org/wiki/Academic_Progress_Rate.

<!-- b000355 | references | pages [19] -->
[17] http://en.wikipedia.org/wiki/Atlantic_Coast_

<!-- b000356 | references | pages [19] -->
Conference_Men%27s_Basketball_Coach_of_the_Year.

<!-- b000357 | references | pages [19] -->
[18] http://en.wikipedia.org/wiki/Big_12_Conference_Men%

<!-- b000358 | references | pages [19] -->
27s_Basketball_Coach_of_the_Yearhttp://en.wikipedia.

<!-- b000359 | references | pages [19] -->
org/wiki/Colonial_Athletic_Association_Men%27s_

<!-- b000360 | references | pages [19] -->
Basketball_Coach_of_the_Year.

<!-- b000361 | references | pages [19] -->
[19] http://en.wikipedia.org/wiki/Associated_Press_College_

<!-- b000362 | references | pages [19] -->
Basketball_Coach_of_the_Year.

<!-- b000363 | references | pages [19] -->
[20] http://en.wikipedia.org/wiki/Clair_Bee_Coach_of_the_

<!-- b000364 | references | pages [19] -->
Year_Award.

<!-- b000365 | references | pages [19] -->
[21] http://en.wikipedia.org/wiki/Henry_Iba_Award.

<!-- b000366 | references | pages [19] -->
[22] http://en.wikipedia.org/wiki/NABC_Coach_of_the_Year.

<!-- b000367 | furniture | pages [20] -->
Team # 26911

<!-- b000368 | furniture | pages [20] -->
Page 19 of 19

<!-- b000369 | references | pages [20] -->
[23] http://en.wikipedia.org/wiki/Naismith_College_Coach_

<!-- b000370 | references | pages [20] -->
of_the_Year.

<!-- b000371 | references | pages [20] -->
[24] http://en.wikipedia.org/wiki/UPI_College_Basketball_

<!-- b000372 | references | pages [20] -->
Coach_of_the_Year.

<!-- b000373 | references | pages [20] -->
[25] http://en.wikipedia.org/wiki/Associated_Press_College_

<!-- b000374 | references | pages [20] -->
Football_Coach_of_the_Year_Award.

<!-- b000375 | references | pages [20] -->
[26] http://en.wikipedia.org/wiki/Paul_%22Bear%22_Bryant_

<!-- b000376 | references | pages [20] -->
Award.

<!-- b000377 | references | pages [20] -->
[27] http://en.wikipedia.org/wiki/AFCA_Coach_of_the_Year.

<!-- b000378 | references | pages [20] -->
[28] http://en.wikipedia.org/wiki/Eddie_robinson_coach_of_

<!-- b000379 | references | pages [20] -->
the_year.

<!-- b000380 | references | pages [20] -->
[29] http://en.wikipedia.org/wiki/Baseball_awards.

<!-- b000381 | references | pages [20] -->
[30] http://en.wikipedia.org/wiki/National_Collegiate_

<!-- b000382 | references | pages [20] -->
Baseball_Writers_Association.

<!-- b000383 | references | pages [20] -->
[31] Mikko Kurttila, Mauno Pesonen, Jyrki Kangas, and Miika Kajanus. Utiliz-

<!-- b000384 | references | pages [20] -->
ing the analytic hierarchy process (ahp) in swot analysisła hybrid method

<!-- b000385 | references | pages [20] -->
and its application to a forest-certiﬁcation case. Forest Policy and Economics,

<!-- b000386 | references | pages [20] -->
1(1):41–52, 2000.

<!-- b000387 | references | pages [20] -->
[32] Mikko Kurttila, Mauno Pesonen, Jyrki Kangas, and Miika Kajanus. Utiliz-

<!-- b000388 | references | pages [20] -->
ing the analytic hierarchy process (ahp) in swot analysisła hybrid method

<!-- b000389 | references | pages [20] -->
and its application to a forest-certiﬁcation case. Forest Policy and Economics,

<!-- b000390 | references | pages [20] -->
1(1):41–52, 2000.

<!-- b000391 | references | pages [20] -->
[33] TC Chang and SJ Lin. Grey relation analysis of carbon dioxide emissions

<!-- b000392 | references | pages [20] -->
from industrial production and energy uses in taiwan. Journal of Environ-

<!-- b000393 | references | pages [20] -->
mental Management, 56(4):247–257, 1999.

<!-- b000394 | references | pages [20] -->
[34] R Konig, Renato Renner, and Christian Schaffner. The operational mean-

<!-- b000395 | references | pages [20] -->
Information Theory, IEEE Transactions on,

<!-- b000396 | references | pages [20] -->
ing of min-and max-entropy.

<!-- b000397 | references | pages [20] -->
55(9):4337–4347, 2009.

<!-- b000398 | references | pages [21] -->
Magazine Article

<!-- b000399 | references | pages [21] -->
In your opinion, who is the best college coach over the past century? Who

<!-- b000400 | references | pages [21] -->
can be seen as a legend? Just as there are a thousand Hamlets in a thousand

<!-- b000401 | references | pages [21] -->
people's eyes, I bet your answers are varied. In this article we will provide our

<!-- b000402 | references | pages [21] -->
best college coach name list with a mathematical model.

<!-- b000403 | references | pages [21] -->
With always-high winning percentage in their career, splendid ability of

<!-- b000404 | references | pages [21] -->
cultivating players, and incomparable personal prestige, they are legends in the

<!-- b000405 | references | pages [21] -->
history of sports. According to our assessment system, the centennial top 5 best

<!-- b000406 | references | pages [21] -->
football college coaches are Tom Osborne, Knute Rockne, Fielding Yost, Frank

<!-- b000407 | references | pages [21] -->
Leahy and Bear Bryant sequentially. The top 5 basketball college coaches are

<!-- b000408 | references | pages [21] -->
John Wooden, Roy Williams, Adolph Rupp, Mike Krzyzewski, Clair Bee. And the

<!-- b000409 | references | pages [21] -->
top 5 baseball college coaches are Cliff Gustafson, Bobby Winkles, John Barry,

<!-- b000410 | references | pages [21] -->
William Spaulding, Bibb Falk.

<!-- b000411 | references | pages [21] -->
As can be seen from our description above, we judge a coach’s

<!-- b000412 | references | pages [21] -->
comprehensive level mainly according to the team’s performance, personal

<!-- b000413 | references | pages [21] -->
prestige and the player’s performance.

<!-- b000414 | references | pages [21] -->
This might trigger a really interesting question for many sport fans: What’s

<!-- b000415 | heading | pages [21] -->
the difference between the public poll and our mathematical model? As a

<!-- b000416 | prose | pages [21] -->
matter of fact, different aspects of emphasis lie in the problem. With the help of

<!-- b000417 | heading | pages [21] -->
our model, we minimize the uncertainty and deviation arising from the

<!-- b000418 | prose | pages [21] -->
subjective factors. Briefly speaking, on one hand, individuals hold different weights for the same index. On the other hand, however, our dear readers should be reminded of the fact that the ones that we are selecting today is ‘best college coach all time’, but not ‘best college coach this time’, since we are more inclined to know more about the contemporary coaches and take those forgotten but still prominent coaches for granted.

<!-- b000419 | prose | pages [21] -->
In our model, three steps are followed to lead to the final results. Firstly, determine the evaluation index and the relevant statistical records. For example, when we are assessing the performance of the team, we are prone

<!-- b000420 | heading | pages [21] -->
to evaluating based on personal preference. Nonetheless, in our model, the

<!-- b000421 | prose | pages [21] -->
winning percentage, the stability of the winning percentage and the number of championships are the main concern of us. What’s more, some subjective factors are also included in our evaluation system. For instance, when we are talking about the personal prestige of the coach, we base our index value on the number of personal awards and the relevant popularity. Google trends is utilized to render a comparative popularity index among the coaches. However, considering the fact that the older coach tends to be more difficult to be known by the public, we will compensate the statistics with professional approaches.

<!-- b000422 | prose | pages [21] -->
Secondly, our weights tend to be more scientific with our application of the mathematical method. As is known to us, when there are a large amount of indexes for evaluation, humans tend to render a less accurate judge. Thus, our method focuses on categorizing the indexes with similar attributes and therefore forms a hierarchy structure to make it more convincing. What’s more,

<!-- b000423 | prose | pages [22] -->
apart from the subjective factors, some lurking information in the data itself can also compensate the model and in turn make the model more robust.  The objective weights derived here, combined with the subjective weights, forms the final comprehensive weights.

<!-- b000424 | prose | pages [22] -->
Finally, combining index values and weights, it is easier to calculate the comprehensive index value of each candidate.

<!-- b000425 | prose | pages [22] -->
Our model is exactly described as above. Hope you enjoy reading it!

<!-- b000426 | furniture | pages [22] -->


<!-- b000427 | furniture | pages [22] -->


<!-- b000428 | furniture | pages [22] -->


<!-- b000429 | furniture | pages [22] -->

