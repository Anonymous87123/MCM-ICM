Summary

In order to evaluate the performance of a coach, we describe metrics in five aspects: historical record, game gold content, playoff performance, honors and contribution to the sports. Moreover, each aspect is subdivided into several secondary metrics. Take playoff performance as example, we collect postseason result (Sweet Sixteen, Final Four, etc.) per year from NCAA official website, Wikimedia and so on.

First, Analytic Hierarchy Process (AHP) Model is established to determine the weight of each metric to coaches’ evaluation grade. All metrics are adequately filled into the three-hierarchy structure, and then we obtain the metric weight based on which evaluation grade is calculated. Second, Fuzzy Synthetic Evaluation (FSE) is built to overcome weakness of excess subjective factors in AHP. This model takes data processing by membership function to generate fuzzy matrix. After that, entropy method and linear weighted method are applied to obtain evaluation grade.

To evaluate the accuracy of the two models, hit score is defined. It is supposed to reflect the difference between our results and standard rankings from several authorities such as ESPN and Sporting News. Take NCAA basketball as a case study, AHP receives 78.77 hit score while FSE gets 81.81, which indicates that FSE performs better than AHP. Afterwards, Aggregation Model (AM) can be developed by combining the two models based on hit score. The top 5 college basketball coaches, in turn, are John Wooden, Mike Krzyzewski, Adolph Rupp, Dean Smith and Bob Knight.

Time line horizon does make a difference. According to turning points in NCAA history, we divide the previous century into six periods with different time weights which lead to the change of ranking. We apply our model into college women’s basketball only to find that genders do not matter. Model proves to be efficient in other sports. The ranking of college football is: Bear Bryant, Knute Rockne, Tom Osborne, Joe Paterno , Bobby Bowden, and the top 5 coaches in college hockey are Bob Johnson, Red Berenson, Jack Parker, Jerry York, Ron Mason.

We conduct sensitivity analysis on FSE to find best membership function and calculation rule. Sensitivity analysis on aggregation weight is also performed. It proves AM performs better than single model. As a creative use, top 3 presidents (U.S.) are picked out: Abraham Lincoln, George Washington, Franklin D. Roosevelt.

At last, the strength and weakness of our mode are discussed, non-technical explanation is presented and the future work is pointed as well.

I. Introduction

1.1 Problem Background

Sports Illustrated is an American sports media franchise owned by media conglomerate Time Warner [1]. This magazine is looking for the “best all time college coach” male or female for the previous century. The best college coach or coaches can be from among either male or female coaches in different fields, such as college hockey or field hockey, football, baseball or softball, basketball, or soccer. We face mainly four problems:  Articulate our own metrics and build a mathematical model;  Set up the evaluation system for the performance of the model.  Discuss how our model can be applied with time factor or across both genders and all possible sports;  Analyze the influences of the parameters, then discuss whether your model could be applied into wide fields.

1.2 Previous Research

Some magazines or websites that focus mainly on college sports have ranked the top college coaches of different sports. For example, rivels.com has made a basket- ball power rankings [2] which shows the top 25 coaches of college basketball.

Considering the best college coaches is an evaluation problem. There are some models which can solve such problem. One is the Analytic hierarchy process (AHP), which was developed by Thomas L. Saaty [3] in the 1970s. The AHP provides a comprehensive and rational framework for structuring a decision problem, for representing and quantifying its elements, for relating those elements to overall goals, and for evaluating alternative solutions [4]. Another is the Fuzzy Synthetic Evaluation Model. Fuzzy mathematics forms a branch of mathematics related to fuzzy set theory and fuzzy logic [5]. It started in 1965 after the publication of Lotfi Asker Zadeh's seminal work Fuzzy sets [6].

1.3 Our Work

In this paper we determine the best college coaches from among either male or female coaches in different sports. In Section 2, we provide the terminology definitions and assumptions that will be utilized in the rest of the paper. In Section 3, we give the definitions of evaluation standard and specific evaluation norms which we used in our models, and show some of the data we have collected. In Section 4, we build two mathematical models to choose the best college coaches, and Section 5 considers combination of the two models mentioned above. In Section 6 we extend our models and take time, genders and types of sports into consideration. Section 7 provides further discuss of our models. In Section 8, we provide an overview of our approach and give a non-technical explanation of our models that sports fans will understand. Section 9 shows some work we can do in the future.

II. Symbols, Definitions and Assumptions

2.1 Symbols and Definitions

 Symbols for evaluation norms:

Symbol

Definition 𝒂𝒂𝒊𝒊 wins for the 𝑖𝑖𝑡𝑡ℎ year 𝒃𝒃𝒊𝒊 losses for the 𝑖𝑖𝑡𝑡ℎ year 𝐑𝐑 the average SRS 𝐎𝐎 the average SOS 𝒏𝒏𝒌𝒌 the times for each class of playoff 𝓴𝓴𝒊𝒊 the weight of each award 𝓬𝓬𝒊𝒊 point for each aspect of contribution  Symbols for Analytic Hierarchy Process:

Symbol

Definition 𝐀𝐀 the judging matrix 𝝀𝝀𝒎𝒎𝒎𝒎𝒎𝒎 the greatest eigenvalue of matrix A 𝐂𝐂𝐂𝐂 the indicator of consistency check 𝐂𝐂𝐂𝐂 the consistency ratio 𝐑𝐑𝐑𝐑 the random consistency index 𝐂𝐂𝐂𝐂 the weight vector for criteria level 𝐀𝐀𝐀𝐀 the weight vector for alternatives level 𝒀𝒀𝟏𝟏 the evaluation grade for model I  Symbols for Fuzzy Synthetic Evaluation:

Symbol

Definition 𝑿𝑿𝒊𝒊 the grades for each aspect 𝝁𝝁𝒋𝒋൫𝑿𝑿𝒊𝒊𝒊𝒊൯ the membership function 𝑿𝑿𝒇𝒇 the fuzzy matrix 𝒑𝒑𝒊𝒊𝒊𝒊 the characteristic weight 𝒆𝒆𝒋𝒋 the entropy for the 𝑗𝑗𝑡𝑡ℎ evaluation grade 𝑬𝑬𝐖𝐖 the weight vector in entropy method 𝒀𝒀𝟐𝟐 the evaluation grade for model II  Symbols for Aggregation Model:

Symbol

Definition 𝐃𝐃 the average offset distance 𝑾𝑾𝟏𝟏 the weight for model I 𝐘𝐘 the evaluation grade for aggregation model

2.2 General Assumptions

 The elements that we already have taken into consideration play a vital role in the evaluation.  The ignored elements of coach do not influence the ranking.  The data that we have collected is enough and accurate and the quantification is correct.  There exists objective and accurate ranking for coaches, and the rankings from selected media could reflect the accurate ranking to some extent.

III. Articulate our metrics

3.1 Specify evaluation norms

As for the evaluation standard for players, there are mainly five aspects [9] that count: strength, speed, skill, defense and attack. Similarly a coach could be evaluated from following five aspects: historical record, game gold content, play-off performance, honors and contribution to the sports. What follows in the chapter will hammer at accounting for the five aspects.  Historical record: The team’s record undoubtedly accounts for the largest proportion in the coach evaluation. According to the mainstream statistic indexes for the team record, wins and losses are most notable. The team’s historical record could directly reflects the coaching ability.

The total wins a could be calculated as follows:

a = ෍𝑎𝑎𝑖𝑖 (3.1) 𝑖𝑖 -Where 𝑎𝑎𝑖𝑖 denotes wins for the 𝑖𝑖𝑡𝑡ℎ year.

The total loses b could be calculated as follows:

b = ෍𝑏𝑏𝑖𝑖 (3.2) 𝑖𝑖 -Where 𝑏𝑏𝑖𝑖 denotes losses for the 𝑖𝑖𝑡𝑡ℎ year.  Game gold content: If all wins are produced during the fights with weak teams, apparently the wins could not illustrate the real coaching ability. At the same time, the average point difference also makes a difference. It reflects the coaching style that whether a coach is conservative or radical. To illustrate the upon two points, we choose the following two norms:

 Simple Rating System (SRS) [8]: The simple rating system works by first finding how many points, on average, a team wins/loses by. For each game, the point differential is then weighted based on how much better or worse than average their opponent's point differential is.

Let R denote the total SRS, then it could be calculated as follows:

R = ∑𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 𝑖𝑖 (3.3) 𝑡𝑡 -Where 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the SRS value for the 𝑖𝑖𝑡𝑡ℎ year, t denotes the number of the years.

 Strength of Schedule (SOS) [8]: In sports, strength of schedule (SOS) refers to the difficulty or ease of a team's/person's opponent as compared to other teams/persons. This is especially important if teams in a league do not play each other the same number of times.

Let O denote the total SOS, then it could be calculated as follows:

O = ∑𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 𝑖𝑖 (3.4) 𝑡𝑡 -Where 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the SOS value for the 𝑖𝑖𝑡𝑡ℎ year, t denotes the number of the years.  Playoff performance: Generally, during the regular season, teams play more games in their division than outside it, but the league's best teams might not play against each other in the regular season [11]. Therefore, in the postseason any group-winning team is eligible to participate thus making the playoff performance extremely important in the coach evaluating [12]. For college basketball in U.S., the playoff performance could be divided as follows:

 First round: The team is eliminated in the first round.

 Second round: The team is eliminated in the second round.

 Sweet sixteen: The last sixteen teams remaining in the playoff tournament  Final four: The last four teams remaining in the playoff tournament.

 Runner-up: The team loses in the finals.

 Champion: The team wins in the finals.

To quantify the aspect, we count the number of times for each class using the symbol 𝑛𝑛𝑘𝑘. Let a binary variable 𝑚𝑚𝑘𝑘𝑘𝑘 denote whether the team get the 𝑘𝑘𝑡𝑡ℎ (for first round k = 1, champion k = 7) class in the 𝑖𝑖𝑡𝑡ℎ year. Thus  𝑛𝑛𝑘𝑘 could be calculated as follows:

𝑛𝑛𝑘𝑘= ෍𝑚𝑚𝑘𝑘𝑘𝑘 (3.5) 𝑖𝑖

 Honors: There are various awards in this field which make up the honors of the coach, at the same time, the basketball hall of fame and college basketball hall of fame [7] are also honors. To quantify the honor, we count the times of main award such as the Naismith College Coach of the Year, Basketball Times National Coach of the Year [9] and so on. Different awards have different gold content. To determine the weight of each award (𝓀𝓀𝑖𝑖), we collect its time period, based on which weights are designated. Let ℋ denote the total weights of all the awards a coach has got:

ℋ= ෍𝓀𝓀𝑖𝑖 (3.6) 𝑖𝑖

Namely ℋ reflects the how much honor a coach have ever obtained.  Contribution to sports: This concept covers a wide range. In order to quantify the contribution, we divide the contribution into five parts:

 Star players: Evaluate the number of the star players the coach have trained.

 Coaching age: When the coaching career start and how long does it last.

 Tactical Innovation: Have the coach invented tactical innovation?

 Performance in international competitions: Have the coach ever fight in the international competitions? Then How many gold or silver medals?

 Popularity: The number of the results when search its name in Google.

We give 𝒸𝒸𝑖𝑖 points for each aspect above: 0 for mediocre, 1 for good, 2 for excellent. Then add the points up to form the final grade 𝒞𝒞 in this aspect (the full mark is 10):

𝒞𝒞= ෍𝒸𝒸𝑖𝑖 (3.7) 𝑖𝑖 A figure is prepared to conclude the evaluation norms above. (See figure)

3.2 Collect data

We use men’s college basketball that will be utilized in the following models discussion as an example, and collect relative data from the Internet. We choose those 70 coaches who were in the list of the National Collegiate Basketball Hall of Fame [7], because those coaches had gained tremendous glory and are more competitive to be chosen as the best coaches. What’s more, we select other 5 college coaches who are not in the Hall of Fame but still made significant contributions.

Searching from the sports-reference.com [8], a website that can provide specific data about coaches, we can find relative data of our specific evaluation norms. Combining those data with the statistics we search from the Wikipedia, we finally conclude the relative statistics of those 75 college coaches and list them in a form. Here we give statistics of 10 coaches as an example.

In the following table, “FR”, “SR”, “SS”, “EE”, “FF”, “RU”, and “CH” refer to “First Round”, “Second Round”, “Sweet Sixteen”, “Elite Eight”, “Final Four”, “Runner-Up”, and “Campion”, respectively. Name from to year win lose SRS SOS FR SR SS EE FF RU CH Jim 1905 1995 48 719 259 15.81 7.27 5 8 11 2 1 2 1 Boeheim Jim 1972 2001 40 877 382 12.64 4.74 5 5 4 5 1 0 3 Calhoun Larry 1979 2013 9 210 83 13.08 5.95 0 3 1 0 1 1 1 Brown … Mike 1975 2013 39 975 302 20.16 8.78 2 6 6 2 3 4 4 Krzyzewski

We also collect college basketball coaching record about each season of every candidate. Here we take Larry Brown as an example. Season win lose SRS SOS AP Pre AP High AP Final

Result

— 1979-80 22 10 15.67 6.1 8 7 NCAA Runner-up 1980-81 20 7 14.89 5.26 6 3 10 NCAA Second Round — 1983-84 22 10 9.76 5.86 17 17 NCAA Second Round 1984-85 26 8 11.84 6.27 19 9 13 NCAA Second Round 1985-86 35 4 23.18 10.42 5 2 2 NCAA Final Four 1986-87 25 11 13.36 7.73 8 6 20 NCAA Sweet Sixteen 1987-88 27 11 15.71 10.77 7 7 NCAA Champions — — — — 2012-13 15 17 -0.59 -1.33 — — — — 2013-14 18 5 13.88 2.45

3.3 Preprocess data

When we collect data from Internet, we notice that some data is missing due to age. Given the fact, we have to preprocess the data from Internet. As for the data for college basketball, SRS&SOS are sometimes missing. The solution adopt by us is filling the data mainly based on interpolation according to the ranking generated by the other metrics.

IV. Two models for coach ranking

4.1 Model I: Analytic Hierarchy Process (AHP)

When we try to obtain the weight of mainly five aspects as the first class index and the weight of several second class index, subjective judgment is ill-considered. So we choose the Analytic Hierarchy Process [4] (AHP) as the way to conform the weighting coefficient of all the indicators in the evaluation system.

4.1.1 The three-hierarchy structure

The three hierarchy structure which contains criteria level and alternatives level is shown in following table. Goal Criteria Alternatives The influence of coach Historical Record Wins Losses Game Gold Content SRS SOS Playoff Performance First Round … Champion Honors Different Awards Hall of Fame Contribution to sports Star Player Coaching Age Tactical Innovation International Games Popularity

4.1.2 Obtain the index weight

 Determine the judging matrix We use the pairwise comparison method and one-nine method to construct judging matrix A = (𝑎𝑎𝑖𝑖𝑖𝑖).

𝑎𝑎𝑖𝑖𝑖𝑖∗𝑎𝑎𝑘𝑘𝑘𝑘= 𝑎𝑎𝑖𝑖𝑖𝑖           (4.1).

Where 𝑎𝑎𝑖𝑖𝑖𝑖 is set according to the one-nine method  Calculate the eigenvalues and eigenvectors The greatest eigenvalue of matrix A is 𝜆𝜆𝑚𝑚𝑚𝑚𝑚𝑚, and the corresponding eigenvector

is u = (𝑢𝑢1,𝑢𝑢2,𝑢𝑢3, … 𝑢𝑢𝑛𝑛)𝑇𝑇. Then we normalize the u by the expression:

𝑢𝑢𝑖𝑖 𝑥𝑥𝑖𝑖= (4.2) 𝑛𝑛 ∑ 𝑢𝑢𝑗𝑗 𝑖𝑖=0  Do the consistency check The indicator of consistency check formula:

CI = 𝜆𝜆𝑚𝑚𝑚𝑚𝑚𝑚−𝑛𝑛 (4.3) 𝑛𝑛−1 Where n denotes the exponent number of matrix.

The expression of consistency ratio:

CR = 𝐶𝐶𝐶𝐶 𝑅𝑅𝑅𝑅                                     (4.4)

As we have confirmed the weighting coefficient of all the indicators in the evaluation system, now we quantify the importance of coaches.

𝐶𝐶𝐶𝐶𝑖𝑖 denotes the weight of 𝑖𝑖𝑡𝑡ℎ criteria level factor, where 𝐴𝐴𝐴𝐴𝑗𝑗 is the weight of 𝑗𝑗𝑡𝑡ℎ secondary critical level factor, and 𝐹𝐹𝑗𝑗 denotes the 𝑗𝑗𝑡𝑡ℎ secondary critical level factor.

The evaluation grade 𝑌𝑌1 should be:

5 𝑚𝑚𝑚𝑚 𝑌𝑌1 = ෍𝐶𝐶𝐶𝐶𝑖𝑖∗෍𝐴𝐴𝐴𝐴𝑗𝑗∗𝐹𝐹𝑗𝑗 (4.5) 𝑖𝑖=1 𝑗𝑗=1

4.1.3 Results & analysis

Based on the data we have already collected in section 3.2, we solve the model and obtain the following results:  Judging matrix:

⎡1 5 5/9 1 1 ⎤ 1/5 1 1/9 1/5 1/5 ⎢ ⎥ 7/5 7 1 7/5 9/5 A = ⎢ ⎥ 1 5 5/7 1 9/5 ⎢ ⎥ ⎣ 1 5 5/7 1/5 1 ⎦  Weight vector of criteria level:

CW = [0.1996 0.2092] 0.0399 0.3093 0.2419 𝐶𝐶𝐶𝐶 For this level, CI=0.301, CR=0.0269 satisfying 𝑅𝑅𝑅𝑅< 0.1.

 Weight vector of alternatives level:  Historical Record:A𝑊𝑊1 = [1.5 −0.5]  Game Gold Content:A𝑊𝑊2 = [0.75 0.25]  Playoff Performance: A𝑊𝑊3 = [0.0079 0.5039] 0.0157 0.0315 0.126 0.252 𝐶𝐶𝐶𝐶 All of these eight vectors satisfy 𝑅𝑅𝑅𝑅< 0.1.

Finally, we can obtain the final rankings of the top ten college basketball coaches using AHP models. Rank Name Grade(𝒀𝒀𝟏𝟏) Rank Name Grade(𝒀𝒀𝟏𝟏) 1 6 Mike Krzyzewski 0.8426 Roy Williams 0.5637 2 7 John Wooden 0.7334 Bob Knight 0.5479 3 8 Adolph Rupp 0.6048 Phog Allen 0.4788 4 9 Jim Boeheim 0.5985 Rick Pitino 0.4683 5 10 Dean Smith 0.5844 Lute Olson 0.4132

Conclusion:

 Analyzing the weight vector of criteria level, we can know that the highest value is the weight of Playoff Performance, so coaches with better game results have more chance in top ranking.

 SOS plays a less important role than SRS when determining the Game Gold Content, and the weight of the Game Gold Content is the lowest value in criteria value.

4.2 Model II: Fuzzy Synthetic Evaluation (FSE)

4.2.1 Quantify grades in the five aspects

Fuzzy set theory [6] has been developed and extensively applied since 1965 (Zadeh, 1965). It was designed to supplement the interpretation of linguistic or measured uncertainties for real-world random phenomena.

In section III, we have already articulate our metrics for ranking. Totally, there are five aspects: historical record, game gold content, playoff performance, honors, contribution to sports. Before using the fuzzy set theory, we calculate the grades {𝑋𝑋1, 𝑋𝑋2, 𝑋𝑋3, 𝑋𝑋4, 𝑋𝑋5}in each of the 5 aspect using the collected data.  Calculation rule for historical record:

𝒶𝒶 denotes the number of wins, 𝒷𝒷 denotes the number of loses, 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤 denotes the weight for single win, and 𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙 denotes the weight for single lose.

𝑋𝑋1 = 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤𝒶𝒶−𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝒷𝒷                 (4.6) This formula provides a comprehensive assessment for wins and losses, obviously 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤> 𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙.  Calculation rule for game gold content:

R denotes the value of SRS, O denotes the value of SOS，𝑂𝑂𝑚𝑚𝑚𝑚𝑚𝑚 denotes the maximum value of SOS in the Strength of Schedule system.

𝑂𝑂 𝑋𝑋2 = 𝑅𝑅൬1 + ൰                    (4.7) 𝑂𝑂𝑚𝑚𝑚𝑚𝑚𝑚 If a coach has higher SRS, it will have higher grade in this aspect because his team is always far ahead its opponents. At the same time, the higher SOS is, the harder games are. So we let the SOS be an addition to SRS.  Calculation rule for playoff performance:

𝑛𝑛𝑘𝑘 denotes the number of times for each class of the playoff results.

7 𝑋𝑋3 = ෍2𝑘𝑘𝑛𝑛𝑘𝑘 (4.8) 𝑘𝑘=1 The number of teams decreases exponentially with power of 2, thus making the weight increase exponentially with power of 2. Sum up the times by designated weight then we could finally draw 𝑋𝑋3.  Calculation rule for honors:

We have already count up the awards by weight (ℋ) in section III, so the formula:

𝑋𝑋4 = ℋ                                (4.9)  Calculation rule for contribution to sports:

We have already give a final grade 𝒞𝒞 for this aspect in section III, so the formula is:

𝑋𝑋5 = 𝒞𝒞                                    (4.10) In conclusion, we form the following quantification rules:

⎧𝑋𝑋1 = 𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤𝒶𝒶−𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝒷𝒷 𝑂𝑂 ⎪ 𝑋𝑋2 = 𝑅𝑅൬1 + ൰ 𝑂𝑂𝑚𝑚𝑚𝑚𝑚𝑚 ⎪ 7 (4.11) 𝑋𝑋3 = ෍2𝑘𝑘𝑛𝑛𝑘𝑘 ⎨ ⎪ 𝑘𝑘=1 𝑋𝑋4 = ℋ ⎪ ⎩ 𝑋𝑋5 = 𝒞𝒞

4.2.2 Determine membership functions

A fuzzy set is defined in terms of a membership function [6] which maps the domain of interest, e.g. concentrations, onto the interval [0, 1]. The shape of the curves shows the membership function for each set. The membership functions represent the degree, or weighting, that the specified value belongs to the set.

Let 𝑋𝑋𝑖𝑖𝑖𝑖 denote the 𝑋𝑋𝑗𝑗 value for the 𝑖𝑖𝑡𝑡ℎ coach and 𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚) denote the maximum 𝑋𝑋𝑗𝑗 value for all the coaches.

Here we use the normalization function as membership function:

𝑋𝑋𝑖𝑖𝑖𝑖 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= (4.12) 𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)

After calculating 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯ for each of the 𝑋𝑋𝑖𝑖𝑖𝑖, we could concluded the fuzzy matrix 𝑋𝑋𝑓𝑓 (N denotes the total number of the coaches).

𝜇𝜇1(𝑋𝑋11) 𝜇𝜇1(𝑋𝑋15) … … 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯ … 𝑋𝑋𝑓𝑓= [ ] 𝜇𝜇𝑁𝑁(𝑋𝑋𝑁𝑁1) 𝜇𝜇𝑁𝑁(𝑋𝑋𝑁𝑁5) …

4.2.3 Determine the weights using entropy method

The principle of entropy method [13] states that, subject to precisely stated prior data (such as a proposition that expresses testable information), the probability distribution which best represents the current state of knowledge is the one with largest entropy. To use entropy method, there are mainly 5 steps:  Calculate the characteristic weight 𝑝𝑝𝑖𝑖𝑖𝑖for the 𝑖𝑖𝑡𝑡ℎ coach’s 𝑗𝑗𝑡𝑡ℎ evaluation grade (𝑋𝑋𝑖𝑖𝑖𝑖) based on the normalized fuzzy matrix 𝑋𝑋𝑓𝑓:

𝑋𝑋𝑓𝑓(𝑖𝑖,𝑗𝑗) 𝑝𝑝𝑖𝑖𝑖𝑖= (4.13) 𝑁𝑁 ∑ 𝑋𝑋𝑓𝑓(𝑖𝑖,𝑗𝑗) 𝑖𝑖=1

 Calculate the entropy for the 𝑗𝑗𝑡𝑡ℎ evaluation grade:

𝑁𝑁 1 𝑒𝑒𝑗𝑗= − ln(𝑁𝑁) ෍𝑝𝑝𝑖𝑖𝑖𝑖𝑙𝑙𝑙𝑙(𝑝𝑝𝑖𝑖𝑖𝑖) (4.14) 𝑖𝑖=1  Calculate the diversity factor for the 𝑗𝑗𝑡𝑡ℎ evaluation grade:

𝑔𝑔𝑗𝑗= 1 −𝑒𝑒𝑗𝑗                                (4.15)  Determine the weight for each evaluation grade: 𝑔𝑔𝑗𝑗 𝑤𝑤𝑗𝑗= (4.16) 5 ∑ 𝑔𝑔𝑗𝑗 𝑗𝑗=1  Determine the final score Y for each coach； 𝑌𝑌2 = W ∗ 𝑋𝑋𝑓𝑓                     (4.17)

4.2.4 Results & analysis

Characteristic weight, entropy, diversity factor and weight are shown as follows:

𝒑𝒑𝒊𝒊𝒊𝒊 𝑿𝑿𝟏𝟏 𝑿𝑿𝟐𝟐 𝑿𝑿𝟑𝟑 𝑿𝑿𝟑𝟑 𝑿𝑿𝟓𝟓 𝒀𝒀𝟐𝟐

0.04 0.06 0.15 0.13 0.08 0.8708 John Wooden 0.07 0.06 0.10 0.13 0.08 0.8629 Mike Krzy 0.06 0.06 0.08 0.11 0.02 0.675 Adolph Rupp 0.06 0.06 0.08 0.04 0.05 0.609 Dean Smith 0.05 0.06 0.06 0.07 0.05 0.6052 Bob Knight 0.06 0.05 0.06 0.04 0.08 0.5872 Roy Williams 0.06 0.03 0.05 0.03 0.01 0.5864 Jim Boeheim 0.04 0.04 0.05 0.05 0.05 0.4874 Phog Allen 0.04 0.04 0.04 0.04 0.02 0.4664 Henry Iba 0.06 0.04 0.04 0.06 0.07 0.4538 Lute Olson 𝒈𝒈𝒋𝒋 -0.99 -1.00 -1.04 -0.96 -0.93 0.4336 𝒘𝒘𝒋𝒋 0.18 0.16 0.23 0.20 0.22 0.8708

 The weights for each aspect is near to each other.

 The playoff performance (𝑋𝑋3) plays the most important role (with 0.23 weight) in FSE evaluating.

 The coaches whose playoff performance is better will enjoy priority to some extent.

At the same time, the coaches who have amazing game gold content (with only 0.16 weight) might not outstand.

V. Models Combination

5.1 Evaluation of individual model

In order to evaluate the accuracy of our two individual models, average offset distance D is defined.

We collect ranking lists of top 10 NCAA basketball coaches from several authoritative media such as ESPN, Bleacher Report, Yahoo Sports, and Sporting News [15]. Then compare our results to those lists and average offset distance D reflects the difference.

Here we use the first-order Minkowski distance to denote the average offset distance of the top 10.

𝑛𝑛 10 D = 1 10𝑛𝑛෍෍ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห (5.1) 𝑖𝑖=1 𝑗𝑗=1 Where n is the number of the top 10 ranking lists, j is the ranking in the 𝑖𝑖𝑡𝑡ℎ list,

and 𝑟𝑟𝑗𝑗 is the ranking of 𝑗𝑗𝑡𝑡ℎ coach in our results. So ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห denotes the difference

between result of media and ours, and D means the average difference. If our results

are the same as all media selection results, then D is equal to zero. 𝐷𝐷𝛼𝛼  is the average offset distance of top 5 𝑛𝑛 5 𝐷𝐷𝛼𝛼= 1 5𝑛𝑛෍෍ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห (5.2) 𝑖𝑖=1 𝑗𝑗=1

𝐷𝐷𝛽𝛽  is the average offset distance of 6th to 10th.

𝑛𝑛 10 𝐷𝐷𝛽𝛽= 1 5𝑛𝑛෍෍ห𝑗𝑗− 𝑟𝑟𝑗𝑗ห (5.3) 𝑖𝑖=1 𝑗𝑗=6 Obviously model with smaller average offset distance should get higher score. So

We can define hit score

900 g = 9+𝐷𝐷 (0 < 𝑔𝑔< 100)           (5.4)

When D = 0, g= 100, means if there is no average offset distance, this model can

get full marks 100. Here are our results:

AHP FSE 𝑫𝑫𝜶𝜶 1.75 1.15

𝑫𝑫𝜷𝜷 3.1 2.85

𝐃𝐃 2.425 2

𝒈𝒈𝜶𝜶 83.72 88.67

𝒈𝒈𝜷𝜷 73.38 75.94

𝐠𝐠 78.77 81.81

Conclusions:

 Vertical comparison: Either AHP or Fuzzy Synthetic Evaluation  𝐷𝐷𝛼𝛼 is obviously smaller than 𝐷𝐷𝛽𝛽. It means that the results are more reasonable in top 5 than in top 10.

 Horizontal comparison: Fuzzy Synthetic Evaluation performs better than AHP in both top 5 and top 10. It proves that Fuzzy Synthetic Evaluation is more accurate than AHP. Because AHP depends on artificial scoring which is too subjective.

5.2 Aggregation Model

AHP is a subjective method, it largely depends on artificial scoring; Relatively, Fuzzy Synthetic Evaluation is an objective method, it all depends on the data. To comprehensively consider the effect of subjective and objective factors, we adopt linear weighted method:

൜ 𝑊𝑊1 + 𝑊𝑊2 = 1 Y =  𝑊𝑊1𝑌𝑌1 + 𝑊𝑊2𝑌𝑌2         (5.5)

𝑌𝑌1 is the evaluation grade of AHP model , 𝑌𝑌2 is the evaluation grade of Fuzzy Synthetic Evaluation model. All of them range from 0 to 1.

To determine the weight 𝑊𝑊1 and 𝑊𝑊2, we take D(the average offset distance) into consideration. Since smaller average offset distance means the more accuracy results, we can assign higher weight to the mode with smaller D. Then we get 𝐷𝐷2 ⎧𝑊𝑊1 = 𝐷𝐷1 + 𝐷𝐷2 (5.6) 𝐷𝐷1 ⎨ 𝑊𝑊2 = ⎩ 𝐷𝐷1 + 𝐷𝐷2 In conclusion, our final model can be defined as:

Y =  𝑊𝑊1𝑌𝑌1 + 𝑊𝑊2𝑌𝑌2              (5.7)

5.3 Results & analysis

AHP FSE AM Rank 1 Mike Krzyzewski John Wooden John Wooden Rank 2 John Wooden Mike Krzyzewski Mike Krzyzewski Rank 3 Adolph Rupp Adolph Rupp Adolph Rupp Rank 4 Jim Boeheim Dean Smith Dean Smith Rank 5 Dean Smith Bob Knight Bob Knight Rank 6 Roy Williams Roy Williams Jim Boeheim Rank 7 Bob Knight Jim Boeheim Roy Williams Rank 8 Phog Allen Phog Allen Phog Allen Rank 9 Rick Pitino Rick Pitino Rick Pitino Rank 10 Lute Olson Henry Iba Henry Iba Top5 Hit score 83.72 88.67 88.67 Top10 Hit score 78.77 81.81 82.57

Conclusion:

 All our models perform better in top 5 than in top 10. It proves that the top 5 coaches in college basketball history are less controversial than top 10.

 The result of AM is very similar to FSE. They have the same hit score 88.67 in top 5; but in top 10, AM have highest hit score 82.57 in these three models. It proves the combination can improve our model.

 According to our final result, our model’s top 5 coaches in college basketball are John Wooden, Mike Krzyzewski, Adolph Rupp, Dean Smith and Bob Knight.

VI. Extend Our Models

6.1 Genders do not matter

Now we take genders into consideration. We still use basketball as an example, and rank the top ten college women’s basketball coaches [20] for the previous century. Searching from the internet, we collect the relative data about 50 college women’s basketball coaches [18] with 600 and other 5 coaches who have established outstanding traditions, earned many awards and garnered recognition for their colleges. Then we rank them with our models mentioned above.

Coaches’ ranking with the Aggregation Model: Rank Name Grade Rank Name Grade Pat Summitt Sylvia Hatchell 1 6 0.8532 0.5875 Geno Auriemma Jody Conradt 2 7 0.8434 0.5673 Tara VanDerveer Kay Yow 3 8 0.7465 0.5486 Leon Barmore Sue Gunter 4 9 0.7236 0.4783 C. Vivian Stringer Gail Goestenkors 5 10 0.6074 0.4379

From the sports.yahoo.com [19], we get a list of the all-time top ten NCAA women’s basketball coaches, and the list is shown in following table.

Rank Name Rank Name Pat Summitt Jody Conradt 1 6 Geno Auriemma Kay Yow 2 7 Leon Barmore Sylvia Hatchell 3 8 C. Vivian Stringer 4 9 Gail Goestenkors Tara VanDerveer Sue Gunter 5 10

Using the average offset distance mentioned in section 5; we can measure the hit score for our models. All results of our models are in agreement within reasonable error range (hit score = 87.57), so that we can safely address the conclusion that our models can be applied in general across both genders.

6.2 Time factor does make a difference

6.2.1 Why time factor matters?

National Collegiate Athletic Association Basketball Tournament [14] started at 1939, during the 74 years’ development, while the number of teams participating in the tournament increasing a lot, the competition becomes fiercer. Also in different historical periods, the NCAA Basketball Tournament gained different popularity, and this also influences the quality of the evaluation grades.

To quantify the time factor, we attach weight 𝑤𝑤𝑖𝑖 (1-10) to different time periods mainly based on the turning points that occurred in the period.

The following table shows the critical years in the NCAA history [14]: Year Turning points 𝒘𝒘𝒊𝒊 1913-1939 There are no national college basketball competition. 5 1939-1951 NCAA Basketball Tournament started, and 8 teams 6 anticipated. There are two college tournament: NIT and NCAA. 1951-1975 16 teams anticipated, NIT became second class competition. 7 1975-1980 32 teams anticipated, especially in 1979, Magic Johnson fight 8 with Larry Bird in the finals, achieving 24.1% audience rating, then a golden age came. 1980-1985 48 teams anticipated, 9 1985-2013 64 teams anticipated. 10

6.2.2 How time factor matters?

The whole metric system will change after introducing the time weight. What follows in the chapter will be devoted to explaining the changes in detail.  The evaluation norms will change after introducing the time weight (𝑤𝑤𝑖𝑖).

⎧a = ෍𝑤𝑤𝑖𝑖𝑎𝑎𝑖𝑖 ⎪ 𝑖𝑖 ⎪ b = ෍𝑤𝑤𝑖𝑖𝑏𝑏𝑖𝑖 ⎪ ⎪ 𝑖𝑖 R = ∑𝑤𝑤𝑖𝑖𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 ⎪ 𝑖𝑖 ⎪ 𝑡𝑡 ⎪ O = ∑𝑤𝑤𝑖𝑖𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 𝑖𝑖 (6.1) 𝑡𝑡 ⎨ ⎪ 𝑛𝑛𝑘𝑘= ෍𝑤𝑤𝑖𝑖𝑚𝑚𝑘𝑘𝑘𝑘 ⎪ 𝑖𝑖 ⎪ ⎪ ℋ= ෍𝓀𝓀𝑖𝑖 ⎪ 𝑖𝑖 ⎪ ⎪ 𝒞𝒞= ෍𝒸𝒸𝑖𝑖 ⎩ 𝑖𝑖 Where  a  denotes the wins, 𝑎𝑎𝑖𝑖 denotes the wins per year.  b  denotes the loses, 𝑏𝑏𝑖𝑖 denotes the loses per year.  R denotes the average SRS, 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the losses per year.  O denotes the average SOS, 𝑆𝑆𝑆𝑆𝑆𝑆𝑖𝑖 denotes the losses per year, t denotes the number of years.  The binary variable 𝑚𝑚𝑘𝑘𝑘𝑘 denotes whether the team get the 𝑘𝑘𝑡𝑡ℎ class in the 𝑖𝑖𝑡𝑡ℎ year.  𝑛𝑛𝑘𝑘 denotes the number of times for each class.  𝓀𝓀𝑖𝑖 denotes the weight for each award, ℋ denotes the total weights of all the awards a coach has ever got.  𝒸𝒸𝑖𝑖 denotes the points for each aspect, 𝒞𝒞 denotes the total points.

 Accordingly, the results for AHP (model I) & FSE (model II) will change. The following table shows how AHP (model I) will change (The names in bold are the people whose rank has changed): AHP(without 𝒘𝒘𝒊𝒊) Grades (Top 10) AHP(with 𝒘𝒘𝒊𝒊 ) Grades (Top 10) Mike Krzyzewski 0.8426 Mike Krzyzewski 0.8894 John Wooden 0.7334 John Wooden 0.7601 Adolph Rupp Jim Boeheim 0.6048 0.6465 Jim Boeheim Adolph Rupp 0.5985 0.6322 Dean Smith 0.5844 Dean Smith 0.6251 Roy Williams 0.5637 Roy Williams 0.6137 Bob Knight 0.5479 Bob Knight 0.5922 Phog Allen Rick Pitino 0.4788 0.5171 Rick Pitino Phog Allen 0.4683 0.5062 Lute Olson 0.4132 Lute Olson 0.4606 Top10 Hit score Top10 Hit score 78.77 76.60 Top5 Hit score Top5 Hit score 83.72 83.56

Conclusion:

 In model I (AHP), Top5 hit score changes from 83.72 to 83.56, namely, Top5 hit score nearly remains unchanged.

 Top10 hit score changes from 78.77 to 76.60, namely, Top10 hit score falls to some extent.

 The changes in rankings occur only locally, not globally.

The following table shows how FSE (model II) will change (The names in bold are the people whose rank has changed): FSE (without 𝒘𝒘𝒊𝒊) Grades (Top 10) FSE (with 𝒘𝒘𝒊𝒊 ) Grades (Top 10) John Wooden Mike Krzyzewski 0.8708 0.9337 Mike Krzyzewski John Wooden 0.8629 0.7850 Adolph Rupp Roy Williams 0.6750 0.6556 Dean Smith Jim Boeheim 0.6090 0.6260 Bob Knight 0.6052 Bob Knight 0.6207 Roy Williams Dean Smith 0.5872 0.5984 Jim Boeheim Adolph Rupp 0.5864 0.5445 Phog Allen Rick Pitino 0.4874 0.5164 Rick Pitino Lute Olson 0.4664 0.4603 Henry Iba Tom Izzo 0.4538 0.4292 Top10 Hit score Top10 Hit score 81.81 75.31 Top5 Hit score Top5 Hit score 88.67 84.51

Conclusion:

 In model II (FSE), Top5 hit score changes from 88.67 to 84.51, namely, Top5 hit score falls to some extent.

 Top10 hit score changes from 81.81 to 75.31, namely, Top10 hit score falls a lot.

The model appears to be more inaccurate.

 The changes in rankings occur globally. The model appears to be easily influenced by the time weights.

 There is no doubt that the results for Aggregation Model (AM) will also change.

The following table shows how aggregation model (final model) will change (The names in bold are the people whose rank has changed):

AM (without 𝒘𝒘𝒊𝒊) Grades (Top 10) AM (with 𝒘𝒘𝒊𝒊 ) Grades (Top 10) John Wooden Mike Krzyzewski 0.8568 0.9204 Mike Krzyzewski John Wooden 0.8296 0.7775 Adolph Rupp Roy Williams 0.6539 0.6430 Dean Smith Jim Boeheim 0.6016 0.6322 Bob Knight 0.5900 Bob Knight 0.6122 Jim Boeheim Dean Smith 0.5880 0.6064 Roy Williams Adolph Rupp 0.5802 0.5708 Phog Allen Rick Pitino 0.4848 0.5166 Rick Pitino Lute Olson 0.4669 0.4604 Henry Iba Phog Allen 0.4308 0.4354 Top10 Hit score Top10 Hit score 82.57 76.6 Top5 Hit score Top5 Hit score 88.67 85.47

Conclusion:

 The changes in rankings occur globally. The model appears to be easily influenced by the time weights.

 The performance for AM appears to be easily influenced by FSE because of the weight distribution for the two models.

Take Bob Knight for example, the following figure shows how evaluation grade changes in the two different situations:

6.2.3 What is the variation tendency?

From the results in section 6.2.2, variation tendency could be concluded as follows:  For coaches in earlier ages, their rankings will fall to some extent.

Take Phog Allen [21]for example, he is known as the "Father of Basketball Coaching", but most of his games occurred in 1920-1959, which means that NCAA had not started or though started the teams were few. The time weight for his age is relatively low thus making the ranking fall.  For coaches in recent years, they will enjoy some superiority.

Take Roy Williams [22]and Adolph Rupp [20]for example, the two coaches’ performance are quiet close to each other, Adolph Rupp was even better in in historical record, but due to the time weight, the historical record for Adolph Rupp does not count that much, and Roy Williams is ahead of him.  Introducing time weights does not necessarily mean higher hit score.

In section V, We have stated that we choose some existed rankings as criterion, but these rankings generally do not take coaching ages into consideration, moreover, some authorities hold the viewpoints that the coaches in early ages are of more authority, leading to the hit score falling.

6.3 Model also works in other sports

It obviously could not live up to our expectations if the model could only be used in basketball. This chapter we will explain in detail how our models can be applied in general across all possible sports.

There are mainly 4 steps to apply the model in any sport as you want.  Step1: Adjust the metrics according to the feature of the sports.

Main differences are in the Playoff Performance, different sports may have different playoff rules, so the metrics in this aspect should be adapted according to the rule. Take football as example:

5-aspect norms Metrics for Metrics for basketball football Historical record Wins Wins Losses Losses Gold content SRS SRS SOS SOS First round Fiesta Bowl Second round Orange Bowl Sweet sixteen Sugar Bowl Playoff Elite eight Rose Bowl Performance Final four National Championship Runner-up Game Champion Non-BSC bowls Honors Awards Awards Contribution Star players Star players to sports Coaching ages Coaching ages Tactical innovation Tactical innovation International International Popularity Popularity

 Step2: Adapt the calculation rules according to the feature of the sports.

For example, the metrics for football in playoff performance have already changed, each class of performance should be assigned another weight according to the gold content of different bowls. At the same time, the awards and their weights under consideration should also be adjusted for the “Honors” aspect.  Step3: Adjust the time weight according to the history of the sport.

For example, as for football, before 2006, there are no BSC bowls. After 2006, 5 BSC bowls came into being, enjoying extremely high gold content.  Step4: Solve the Aggregation model again and analyze the results.

The following figure shows the steps of applying the model into all possible sports:

Start

Adjust the metrics

Adjust the calculation rules

Adjust time weights

Solve the model

Following the 4 steps presented above, we apply the model in other 2 different sports: football and hockey. Top5 for football  Grades Top5 for hockey Grades Bear Bryant 0.8874 Bob Johnson 0.8963 Knute Rockne 0.8664 Red Berenson 0.8732 Tom Osborne 0.8538 Jack Parker 0.8525 Joe Paterno 0.7872 Jerry York 0.7756 Bobby Bowden 0.7864 Ron Mason 0.7632

VII. Further discussion

7.1 Sensitivity Analysis on FSE

7.1.1 Vary Membership function

In FSE discussed in section 4.2, we choose (4.12) as the membership function. But there are also other available membership functions. The following table shows the membership functions that are taken into consideration in this part.

Type Membership function 1 𝑋𝑋𝑖𝑖𝑖𝑖 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= ( )𝑘𝑘 𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)

2 𝑋𝑋𝑖𝑖𝑖𝑖−𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚) 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= ( )𝑘𝑘 𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚) −𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚)

3 𝜇𝜇𝑗𝑗൫𝑋𝑋𝑖𝑖𝑖𝑖൯= 1 −𝑒𝑒−𝑘𝑘(𝑋𝑋𝑖𝑖𝑖𝑖−𝑋𝑋𝑗𝑗(𝑚𝑚𝑚𝑚𝑚𝑚))

 For type 1, we will analyze how the weight distribution (only for FSE) for different aspects will change while varying k.

Conclusions:

 Weight distribution is sensitive to the value of k and changes of weight distribution can be seen clearly in Figure 7.1。

 As the value of k increases, 𝑋𝑋1 and 𝑋𝑋2 tend to be less important but 𝑋𝑋3 and 𝑋𝑋5 tend to be more important.

 When  1 ≤k ≤4, 𝑋𝑋3 and 𝑋𝑋5 have the highest weight, 𝑋𝑋1 and 𝑋𝑋2 have the lowest weight.  For all three types, we will analyze how hit score (only for FSE) will change varying k.

Conclusions:

 Membership function 1 and member function 2 are sensitive to the value of k, while membership function 3 is not sensitive to the value of k.

 Membership function 1 reaches its maximum value at k = 3; membership function 2 reaches its maximum value at k = 2.

 Obviously, membership function1 and membership function 2 perform much better than membership function 3. And membership function 3 is not suitable for our model.

 For best results, membership function1 with k = 3 is most appropriate in this model.

7.1.2 Vary calculation rule

𝜆𝜆𝑤𝑤𝑤𝑤𝑤𝑤 Here we focus on figuring out how hit score will change to the ratio 𝜆𝜆𝑙𝑙𝑙𝑙𝑙𝑙𝑙𝑙.

Conclusions:

 Model performs best when the weight of winning a game is two times as much as losing a game.

 If we attach the same weight to winning a game and losing a game, the model will have a poor hit score. And if the ratio of the weight of wins and loses is too high, it will also lead to a bad result.

7.2 Sensitivity Analysis on Aggregation weight

In this part, we will analyze how hit score (For AM) and rankings will change while varying the weight for AHP (𝑊𝑊1).

Conclusion:

 As the weight of AHP increases, the rank list will change. The rank of Dean Smith and Bob knight tend to decline and the rank of Jim Boeheim tend to rise.

 Since AHP is less accurate than FSE, hit score of AM would be optimal when the weight of AHP is small. But when the weight of AHP is zero, hit score doesn’t reach the maximum. The maximum hit score is reached when the weight of AHP is 0.1-0.2.

 It proves that AM can perform well than either AHP or FSE.

7.3 Exploration: Evaluating Best President

Now we use our models to find the top ten presidents of the United States. We choose the 43 men who have been president of USA, and collect relative data from the internet [24].

A president can be evaluated also from following five aspects: personal qualities, presidential achievements, leadership qualities, failures and faults, and popular opinion:

The personal qualities includes imagination, intelligence and being willing to take risks, while the presidential achievements can be valued with ability of domestic accomplishments, executive appointments, foreign policy accomplishments, and ability of compromise. And the leadership qualities can be measured by party leadership ability and relations with congress. We also take popular opinion into consideration, and we gather votes from different polls, such as C-SPAN poll, ABC News poll, Washington College poll, Gallup poll, Rasmussen poll, and 2012 Gallup poll. The ranking of presidents of the United States is shown in following table.

Rank Name Rank Name Abraham Lincoln Harry S. Truman 1 6 George Washington Woodrow Wilson 2 7 Dwight D. Eisenhower Franklin D. Roosevelt 3 8 Thomas Jefferson James K. Polk 4 9 Theodore Roosevelt Andrew Jackson 5 10

VIII. Strength and Weakness

Strength:  When we articulate our own metrics for assessment, we try our best to include all the important elements of a coach to make the ranking more accurate. Time factor, gender, category are all discussed in the model.  We evaluate the performance of a coach from 5 specific perspectives.  We set up two different models to form an aggregation model. AHP includes more subjective factors while FSE appears to be more objective. The aggregation model is devoted to make clear the tradeoff between the two sides.  We states a distinct quantification system which is expected to live up to the common sense. Weakness:  We adopt totally eighteen indicators to evaluate a coach, namely not all elements is under consideration.  Weights are everywhere in the model, but some weight assignments might not be the best scheme.

IX. Non-technical Explanation

For better or worse, coaches are often the faces of college sports programs. Different from players who stay only for a few years, coaches can exert longer influence in the college games. Here is a list of the top 5 coaches in the college basketball, college football, and college hockey.

Rank college basketball college football college hockey 1

John Wooden Bear Bryant Bob Johnson 2

Mike Krzyzewski Knute Rockne Red Berenson 3

Adolph Rupp Tom Osborne Jack Parker 4

Dean Smith Joe Paterno Jerry York 5

Bob Knight Bobby Bowden Ron Mason The rankings proved to be a difficult task and job of a college coach is multifaceted. Firstly, we choose some coaches, who are in the list of Hall of Fame, or people who have established outstanding traditions and earned many awards, as our ranking candidates. Then, searching from the internet or other data sources, we try to collect relative data as detailed as possible. After choosing proper data, college coaches’ rankings can be obtained. What’s more, we search the existing rankings from the internet to serve as the evaluation criterion.

During the procedure of choosing data, we evaluate the coaches in our list of candidates from five aspects. As is known to all, the best college coaches tend to have good team’s historical record, such as more wins and high win rate. What’s more, SRS (Simple Rating System) and SOS (Strength of Schedule) can reflect the coaching ability. We also examined each coach’s success in the postseason. Taking basketball as an example, the performance could be valued by counting the number of times for “Champion”, “Runner-up”, “Final Four”, “Sweet Sixteen”, “Second Round”, and “First Round”. In many case, we take into account coaches’ contribution to the sports and honors, such as various awards in their field or putting their name in the “Hall of Fame”.

After collecting and choosing coaches’ detailed data, we define the importance of those aspects which can measure coaches’ ability, and use the results to give each coach a score. The higher the coaches’ scored on the relative aspects, the better their position on the ranking.

We use the data of the best college basketball coach–John Wooden to give some example. In his college basketball coach career, his team had won 826 games, and during his sixteen years NCAA tournament, he won ten championships and twelve straight trips to Final Fours. John Wooden has been recognized tremendous times for his achievements and created longer legacies in the college basketball games. Besides his fantastic and glory record, Wooden was recognized for his impact on college basketball as a member of the founding class of the National Collegiate Basketball Hall of Fame and was named The Sporting News "Greatest Coach of All Time" [23]. With so many honors and awards which can’t be listed in detail there, John gets the highest score when we rank the coaches and is worthy the title of the best college basketball coach.

X. Future work

 Consider all possible sports coaches together, and make a college coaches rankings, regardless of what kind of sports coaches they are.  Take other relevant coach information into consideration, because research suggests that characteristics of the coaches, such as the breadth of coaches’ knowledge, authority, the ability of searching and cultivating talents, and attention to details, play a role in determining the best college coaches.  Develop a general method to rank everything when there is one way to quantify.
