# P-B-2014-30680-9f0c0d05

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->
Team #30680

<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | heading | pages [1] -->
Summary

<!-- b000007 | prose | pages [1] -->
The objective of our team was to find the five best coaches of the last 100 years for three different college sports. Our team decided to look at men’s basketball, football, and baseball. We wanted to be able to definitively determine team skill from the games played, and then use a machine- learning algorithm to calculate the correct coach skills for each team in a given year. We created a networks-based model to calculate team skill from historical game data. For basketball, we were able to obtain the final scores of every single Div. I game played from 1939 to 2013. The range for football was even larger: 1869 to 2013. The data for baseball was sparse. We were only able to obtain the final scores of tournament games from 1947 to 2013. A digraph was created for each year in each sport. Nodes represented teams, and edges represented a game played between two teams. The arrowhead pointed towards the losing team.

<!-- b000008 | prose | pages [1] -->
We calculated the team skill of each graph using a right-hand eigenvector centrality measure. Eigenvector centrality calculates the relative ‘importance’ of a node based on both the number of connections and the importance of the nodes that it is connected to. In this way, teams that beat good teams will be ranked higher than teams that beat mediocre teams. The eigenvector centrality rankings for most years were well correlated with tournament performance and poll-based rankings.

<!-- b000009 | prose | pages [1] -->
We assumed that the relationship between coach skill (𝐶!), player skill (𝑃!), and team skill (𝑇!) was this: 𝐶! ∗𝑃! = 𝑇!. Our team then created a function to describe the probability that a given score difference would occur based on player skill and coach skill. Our rationale was this: if two teams have unevenly matched players, coach skill will likely not influence the outcome of the game. However, if two teams have evenly matched players, coach skill will manifest itself in player substitutions, time- outs, etc. and will determine the team that won and the score difference. We multiplied the probabilities of all edges in the network together to find the probability that the correct network would occur with any given player skill and coach skill matrix. Our team was able to determine player skill as a function of team skill and coach skill, eliminating the need to optimize two unknown matrices. The top five coaches in each year were noted, and the top coach of all time was calculated by dividing the number of times that coach ranked in the yearly top five by the years said coach had been active. The top five coaches in the last century are: Basketball: John Wooden (0.28), Lute Olson (0.26), Jim Boeheim (0.24), Gregg Marshall (0.23), and Jamie Dixon (0.21). Football: Glenn Scobey Warner (0.24), Bobby Bowden (0.23), Jim Grobe (0.18), Bob Stoops (0.17), and Bill Peterson (0.16). Baseball: Mark Marquess (0.27), Augie Garrido (0.24), Tom Chandler (0.22), Richard Jones (0.19), and Bill Walkenbach (0.16).

<!-- b000010 | prose | pages [2] -->
Who’s	  the	  Best	  Coach? By:	  MCM	  Team	  #30680

<!-- b000011 | furniture | pages [2] -->


<!-- b000012 | prose | pages [2] -->
As	  football	  and	  basketball	  legends	  like	  Nick	  Saban	  and	  Mike	  Krzyzewski	  fight	  hard on	  the	  court	  to	  keep	  their	  reputations	  high,	  those	  of	  us	  at	  home	  would	  like	  to	  ask: are	  these	  reputations	  justified?	  Does	  being	  well-­‐known	  necessarily	  make	  a	  coach better?	  Is	  the	  best	  coach,	  contrary	  to	  popular	  belief,	  someone	  who	  is	  less	  well-­‐ known	  than	  some	  of	  their	  colleagues?	  We	  are	  going	  to	  set	  out	  to	  find	  the	  best	  coach of	  the	  last	  one	  hundred	  years	  in	  the	  college	  sports	  of	  basketball,	  football,	  and baseball.	  We	  will	  utilize	  some	  cool	  mathematics	  during	  our	  journey	  to	  make	  our rankings	  less	  biased	  than	  other	  rankings	  like	  the	  AP	  Poll	  or	  USA	  Today.

<!-- b000013 | furniture | pages [2] -->


<!-- b000014 | prose | pages [2] -->
We	  will	  start	  by,	  for	  every	  year	  in	  the	  last	  century,	  ranking	  the	  college	  sports	  teams that	  play	  in	  the	  top	  college	  division.	  We	  do	  this	  in	  a	  really	  interesting	  way	  that	  is quite	  simple	  to	  understand.	  Let’s	  say	  you	  have	  two	  teams	  that	  are	  playing	  a	  game against	  one	  another.	  On	  a	  piece	  of	  paper,	  draw	  two	  circles	  representing	  the	  two teams.	  Then,	  draw	  an	  arrow	  from	  one	  circle	  to	  the	  other.	  The	  arrow	  head	  will	  point to	  the	  team	  that	  lost	  the	  game.	  Now,	  we	  have	  created	  a	  very	  simple	  drawing	  that	  can represent	  this	  game.

<!-- b000015 | furniture | pages [2] -->


<!-- b000016 | furniture | pages [2] -->


<!-- b000017 | furniture | pages [2] -->


<!-- b000018 | prose | pages [2] -->
Now	  imagine	  that	  this	  process	  is	  repeated	  for	  all	  5000	  games	  played	  in	  the	  2012-­‐

<!-- b000019 | heading | pages [2] -->
2013	  basketball	  season.	  The	  resulting	  drawing	  will	  look	  something	  like	  this:

<!-- b000020 | furniture | pages [2] -->


<!-- b000021 | furniture | pages [2] -->


<!-- b000022 | prose | pages [2] -->
From	  this	  drawing,	  we	  can	  see	  exactly	  which	  teams	  beat	  which	  teams.	  From	  this,	  we can	  use	  various	  different	  graph	  metrics	  to	  calculate	  the	  best	  teams.	  In	  the	  drawing above,	  the	  best	  teams	  have	  the	  biggest	  circles	  drawn.

<!-- b000023 | furniture | pages [2] -->


<!-- b000024 | prose | pages [2] -->
So	  what	  does	  the	  best	  coach	  have	  to	  do	  with	  any	  of	  this?	  Well,	  we	  think	  that	  coaches that	  lead	  the	  highest	  ranked	  teams	  must	  be	  doing	  something	  right.	  However,	  we aren’t	  just	  going	  to	  give	  the	  highest	  ranked	  teams	  the	  distinction	  of	  having	  the	  best

<!-- b000025 | prose | pages [3] -->
coaches.	  The	  highest	  ranked	  teams	  will	  on	  average	  have	  better	  coaches	  –	  sure,	  but there’s	  no	  reason	  that	  the	  #2	  team	  won’t	  have	  a	  better	  coach	  than	  the	  #1	  team.

<!-- b000026 | furniture | pages [3] -->


<!-- b000027 | prose | pages [3] -->
We	  think	  that	  it	  is	  pretty	  safe	  to	  say	  that,	  if	  the	  players	  of	  one	  team	  are	  much	  worse than	  the	  players	  of	  one	  of	  their	  opponents,	  even	  the	  best	  coaching	  won’t	  help	  the team	  pull	  off	  a	  win.	  However,	  when	  two	  teams	  are	  evenly	  matched	  and	  they	  face each	  other,	  we	  think	  that	  coaching	  actually	  has	  a	  big	  impact	  on	  who	  wins	  the	  game. Think	  about	  it	  this	  way:	  If	  the	  players	  of	  two	  teams	  are	  evenly	  matched,	  then	  the game	  is	  probably	  going	  to	  be	  close	  all	  the	  way	  from	  the	  start	  to	  the	  end.	  The	  coaches of	  either	  team	  will	  be	  the	  ones	  determining	  who	  wins	  the	  game	  through	  things	  like the	  the	  timing	  of	  player	  substitutions	  and	  time-­‐outs,	  as	  well	  as	  effectively	  raising team	  morale	  and	  calling	  good	  plays.

<!-- b000028 | furniture | pages [3] -->


<!-- b000029 | prose | pages [3] -->
Therefore,	  when	  two	  teams	  that	  are	  evenly	  matched	  (we	  determine	  ‘evenly matched’	  based	  upon	  the	  ranking	  system	  described	  above),	  the	  team	  that	  wins	  will have	  a	  better	  coach	  than	  the	  team	  that	  loses.	  If	  we	  calculate	  this	  for	  any	  year	  in	  a college	  sport,	  we	  will	  get	  a	  list	  of	  the	  top	  coaches.	  We	  can	  do	  this	  up	  to	  100	  years	  in the	  past	  and	  see	  which	  coaches	  show	  up	  highest	  on	  the	  list.	  These	  are	  then determined,	  through	  the	  power	  of	  mathematics,	  to	  be	  the	  best	  coaches	  in	  said	  sport for	  the	  last	  100	  years.

<!-- b000030 | furniture | pages [3] -->


<!-- b000031 | prose | pages [3] -->
Everything	  you	  just	  read	  wasn’t	  just	  an	  exercise	  in	  thought.	  We	  have	  actually	  gone through	  this	  entire	  process,	  just	  as	  it	  was	  described	  to	  you	  (it	  is	  actually	  a	  little	  more complicated	  than	  this).	  We	  were	  able	  to	  come	  up	  with	  the	  best	  coaches	  of	  the	  last

<!-- b000032 | heading | pages [3] -->
100	  years	  for	  the	  college	  sports	  of	  mens	  basketball,	  football,	  and	  baseball.	  These

<!-- b000033 | prose | pages [3] -->
coaches	  are:

<!-- b000034 | furniture | pages [3] -->


<!-- b000035 | prose | pages [3] -->
Rank Basketball Football Baseball 1 John	  Wooden Glenn	  Scobey	  Warner Mark	  Marquess 2 Lute	  Olson Bobby	  Bowden Augie	  Garrido 3 Jim	  Boeheim Jim	  Grobe Tom	  Chandler 4 Gregg	  Marshall Bob	  Stoops Richard	  Jones 5 Jamie	  Dixon Bill	  Peterson Bill	  Walkenbach

<!-- b000036 | furniture | pages [3] -->


<!-- b000037 | prose | pages [3] -->
Thanks	  so	  much	  for	  reading!	  Agree	  with	  our	  results?	  Disagree?	  Feel	  free	  to	  send	  us an	  email	  at:	  mcm30680@comap.com.	  We’re	  always	  happy	  to	  hear	  from	  our	  readers.

<!-- b000038 | furniture | pages [3] -->


<!-- b000039 | furniture | pages [3] -->


<!-- b000040 | prose | pages [4] -->
A Networks and Machine Learning Approach to

<!-- b000041 | prose | pages [4] -->
Determine the Best College Coaches of the

<!-- b000042 | prose | pages [4] -->
20th-21st Centuries

<!-- b000043 | furniture | pages [4] -->
Team #30680

<!-- b000044 | prose | pages [4] -->
February 10, 2014

<!-- b000045 | prose | pages [4] -->
1

<!-- b000046 | furniture | pages [5] -->
Team #30680

<!-- b000047 | heading | pages [5] -->
Contents

<!-- b000048 | contents | pages [5] -->
1

<!-- b000049 | contents | pages [5] -->
Problem Statement

<!-- b000050 | contents | pages [5] -->
2

<!-- b000051 | contents | pages [5] -->
Planned Approach

<!-- b000052 | contents | pages [5] -->
3

<!-- b000053 | heading | pages [5] -->
Assumptions

<!-- b000054 | prose | pages [5] -->
4

<!-- b000055 | heading | pages [5] -->
Data Sources and Collection

<!-- b000056 | furniture | pages [5] -->
Page 2 of 18

<!-- b000057 | prose | pages [5] -->
3

<!-- b000058 | prose | pages [5] -->
3

<!-- b000059 | prose | pages [5] -->
3

<!-- b000060 | prose | pages [5] -->
4 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.1 College Football 5 Men’s College Basketball . . . . . . . . . . . . . . . . . . . . . . . 4.2 5 . . . . . . . . . . . . . . . . . . . . . . . . . . . 4.3 College Baseball 5

<!-- b000061 | heading | pages [5] -->
Network-based Model for Team Ranking

<!-- b000062 | prose | pages [5] -->
5 6 . . . . . . . . . . . . . . . . . . . . . . . . 5.1 Building the Network 6 Analyzing the Network . . . . . . . . . . . . . . . . . . . . . . . . 5.2 6 Degree Centrality . . . . . . . . . . . . . . . . . . . . . . . 5.2.1 6 Betweenness and Closeness Centrality . . . . . . . . . . . 5.2.2 7 Eigenvector Centrality . . . . . . . . . . . . . . . . . . . . 5.2.3

<!-- b000063 | prose | pages [5] -->
6 Separating the Coach Eﬀect 6.1 When is Coach Skill Important?

<!-- b000064 | prose | pages [5] -->
8

<!-- b000065 | prose | pages [5] -->
10 . . . . . . . . . . . . . . . . . .

<!-- b000066 | prose | pages [5] -->
11 Margin of Win Probability . . . . . . . . . . . . . . . . . . . . . . 6.2 12 Optimizing the Probability Function . . . . . . . . . . . . . . . . 6.3 13 Genetic Algorithm . . . . . . . . . . . . . . . . . . . . . . 6.3.1 6.3.2 Nelder-Mead Method 13 . . . . . . . . . . . . . . . . . . . .

<!-- b000067 | prose | pages [5] -->
14 . . . . . . . . . . . . . . . . . . . . . . . 6.3.3 Powell’s Method

<!-- b000068 | prose | pages [5] -->
7 Ranking Coaches

<!-- b000069 | prose | pages [5] -->
14

<!-- b000070 | prose | pages [5] -->
15 Top Coaches of the Last 100 Years . . . . . . . . . . . . . . . . . 7.1

<!-- b000071 | prose | pages [5] -->
8

<!-- b000072 | heading | pages [5] -->
Testing our Model

<!-- b000073 | prose | pages [5] -->
15

<!-- b000074 | prose | pages [5] -->
15 Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . 8.1 15 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.2 Strengths 16 Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8.3

<!-- b000075 | prose | pages [5] -->
9

<!-- b000076 | heading | pages [5] -->
Conclusions

<!-- b000077 | prose | pages [5] -->
16

<!-- b000078 | prose | pages [5] -->
17

<!-- b000079 | prose | pages [5] -->
2 2

<!-- b000080 | furniture | pages [6] -->
Team #30680

<!-- b000081 | furniture | pages [6] -->
Page 3 of 18

<!-- b000082 | prose | pages [6] -->
1 Problem Statement

<!-- b000083 | prose | pages [6] -->
College sport coaches often achieve widespread recognition. Coaches like Nick Saban in football and Mike Krzyzewski in basketball repeatedly lead their schools to national championships.

<!-- b000084 | prose | pages [6] -->
Because coaches inﬂuence both the per- formance and reputation of the teams they lead, a question of great concern to universities, players, and fans alike is: Who is the best coach in a given sport? Sports Illustrated, a magazine for sports enthusiasts, has asked us to ﬁnd the best all-time college coaches for the previous century. We are tasked with creat- ing a model that can be applied in general across both genders and all possible sports at the college-level. The solution proposed within this paper will oﬀer an insight to these problems and will objectively determine the top ﬁve coaches of all time in the sports of baseball, men’s basketball, and football.

<!-- b000085 | prose | pages [6] -->
2 Planned Approach

<!-- b000086 | prose | pages [6] -->
Our objective is to rank the top 5 coaches in each of 3 diﬀerent college-level sports. We need to determine which metrics reﬂect most accurately the ranking of coaches within the last 100 years. To determine the most eﬀective ranking system, we will proceed as follows:

<!-- b000087 | prose | pages [6] -->
1. Create a network-based model to visualize all college sports teams, the teams won/lost against, and the margin of win/loss. Each network de- scribes the games of one sport over a single year.

<!-- b000088 | prose | pages [6] -->
2. Analyze various properties of the network in order to calculate the skill of each team.

<!-- b000089 | prose | pages [6] -->
3. Develop a means by which to decouple the eﬀect of the coach from the team performance.

<!-- b000090 | prose | pages [6] -->
4. Create a model that, given the player and coach skills for every team, can predict the probability of the occurrence of a speciﬁc network of a) wins and losses and b) the point margin with which a win or loss occurred.

<!-- b000091 | prose | pages [6] -->
5. Utilize an optimization algorithm to maximize the probability that the coach skill matrix, once plugged into our model, generates the network of wins/losses and margins described in (1).

<!-- b000092 | prose | pages [6] -->
6. Analyze the results of the optimization algorithm for each year to deter- mine an overall ranking for all coaches across history.

<!-- b000093 | prose | pages [6] -->
3

<!-- b000094 | heading | pages [6] -->
Assumptions

<!-- b000095 | prose | pages [6] -->
Due to limited data about the coaching habits of all coaches at all teams over the last century in various collegiate sports, we use the following assumptions to

<!-- b000096 | prose | pages [6] -->
3

<!-- b000097 | furniture | pages [7] -->
Team #30680

<!-- b000098 | furniture | pages [7] -->
Page 4 of 18

<!-- b000099 | prose | pages [7] -->
complete our model. These simplifying assumptions will be used in our report and can be replaced with more reliable data when it becomes available.

<!-- b000100 | prose | pages [7] -->
• The skill level of a coach is ultimately expressed through his/her team’s wins over another and the margin by which they win. This assumes that a team must win to a certain degree for their coach to be good. Even if the coach signiﬁcantly ampliﬁes the skills of his/her players, he/she still cannot be considered “good” if the team wins no games.

<!-- b000101 | prose | pages [7] -->
• The skills of teams are constant throughout any given year (ex: No players are injured in the middle of a season). This assumption will allow us to compare a team’s games from any point in the season to any other point in the season. In reality, changing player skills throughout the season make it more diﬃcult to determine the eﬀect of the coach on a game.

<!-- b000102 | prose | pages [7] -->
• Winning k games against a good team improves team skill more than winning k games against an average team. This assumption is intuitive and allows us to use the eigenvector centrality metric as a measure of total team skill.

<!-- b000103 | prose | pages [7] -->
• The skill of a team is a function of the skill of the players and the skill of the coach. We assume that the skill of a coach is multiplicative over the skill of the players. That is: Ts = Cs · Ps where Ts is the skill of the team, Cs is the skill of the coach, and Ps is a measure of the skill of the players. Making coach skill multiplicative over player skill assumes that the coach has the same eﬀect on each player. This assumption is important because it simpliﬁes the relationship between player and coach skill to a point where we can easily optimize coach skill vectors.

<!-- b000104 | prose | pages [7] -->
• The eﬀect of coach skill is only large when the diﬀerence between player skill is small. For example, if team A has the best players in the conference and team B has the worst, it is likely that even the best coach would not be able to, in the short run, bring about wins over team A. However, if two teams are similarly matched in players, a more-skilled coach will make advantageous plays that lead to his/her team winning more often than not.

<!-- b000105 | prose | pages [7] -->
• When player skills between two teams are similarly matched, coach skill is the only factor that determines the team that wins and the margin by which they win by. By making this assumption, we do not have to account for any other factors.

<!-- b000106 | prose | pages [7] -->
4

<!-- b000107 | heading | pages [7] -->
Data Sources and Collection

<!-- b000108 | prose | pages [7] -->
Since our model requires as an input the results of all the games played in a season of a particular sport, we ﬁrst set out to collect this data. Since we were unable to identify a single resource that had all of the data that we required, we

<!-- b000109 | prose | pages [7] -->
4

<!-- b000110 | furniture | pages [8] -->
Team #30680

<!-- b000111 | furniture | pages [8] -->
Page 5 of 18

<!-- b000112 | prose | pages [8] -->
found a number of diﬀerent websites, each with a portion of the requisite data. For each of these websites, we created a customized program to scrape the data from the relevant webpages. Once we gathered all the data from our sources, we processed it to standardize the formatting. We then aimed to merge the data gathered from each source into a useable format. For example, we gathered basketball game results from one source, and data identifying team coaches from another. To merge them and show the game data for a speciﬁc coach, we attempted to match on common ﬁelds (ex. “Team Name”). Often, however, the data from each source did not match exactly (ex. “Florida State” vs “Florida St.”). In these situations, we had to manually create a matching table that would allow our program to merge the data sources.

<!-- b000113 | prose | pages [8] -->
Although we are seeking to identify the best college coach for each sport of interest for the last century, it should be noted that many current college sports did not exist a century ago. The National Collegiate Athletic Association (NCAA), the current managing body for nearly all college athletics, was only oﬃcially established in 1906 and the ﬁrst NCAA national championship took place in 1921, 7 years short of a century ago. Although some college sports were independently managed before being brought into the NCAA, it is often diﬃcult to gather accurate data for this time.

<!-- b000114 | prose | pages [8] -->
4.1 College Football

<!-- b000115 | prose | pages [8] -->
One of the earliest college sports, College Football has been popular since its inception in the 1800’s. The data that we collected ranges from 1869 to the present, and includes the results and ﬁnal scores of every game played between Division 1 men’s college football teams (or the equivalent before the inception of NCAA) [2]. Additionally, we have gathered data listing the coach of each team for every year we have collected game data [4], and combined the data in order to match the coach with his/her complete game record for every year that data was available.

<!-- b000116 | prose | pages [8] -->
4.2 Men’s College Basketball

<!-- b000117 | prose | pages [8] -->
The data that we gathered for Men’s College Basketball ranges from the sea- son of the ﬁrst NCAA Men’s Basketball championship in 1939 to the present. Similarly to College Football, we gathered data on the result and ﬁnal scores of each game in the season and in ﬁnals [2]. Combining this with another source of coach names for each team and year generated the game record for each coach for each season [4].

<!-- b000118 | prose | pages [8] -->
4.3 College Baseball

<!-- b000119 | prose | pages [8] -->
Although College Baseball has historically had limited popularity, interest in the sport has grown greatly in the past decades with improved media coverage and collegiate spending on the sport. The game result data that we collected

<!-- b000120 | prose | pages [8] -->
5

<!-- b000121 | furniture | pages [9] -->
Team #30680

<!-- b000122 | furniture | pages [9] -->
Page 6 of 18

<!-- b000123 | prose | pages [9] -->
ranges from 1949 to the present, and was merged with coach data for the same time period.

<!-- b000124 | prose | pages [9] -->
5

<!-- b000125 | heading | pages [9] -->
Network-based Model for Team Ranking

<!-- b000126 | prose | pages [9] -->
Through examination of all games played for a speciﬁc year we can accurately rank teams for that year. By creating a network of teams and games played, we can not only analyze the number of wins and losses each team had, but can also break down each win/loss with regard to the opponent’s skill.

<!-- b000127 | prose | pages [9] -->
5.1 Building the Network

<!-- b000128 | prose | pages [9] -->
We made use of a weighted digraph to represent all games played in a single year. Each node in the graph represents a single college sports team. If team A wins over team B, a directed edge with a weight of 1 will be drawn from A pointing towards B. Each additional time A wins over B, the weight of the edge will be increased by 1. If B beats A, an edge with the same information is drawn in the opposing direction. Additionally, a list containing the margin of win/loss for each game is associated with the edge. For example, if A beat B twice with score : 64 −60, 55 −40, an edge with weight two is constructed and the winning margin list 4, 15 is associated with the edge. Since each graph represents a single season of a speciﬁc sport, and we are interested in analyzing a century of data about three diﬀerent sports, we have created a program to automate the creation of the nearly 300 graphs used to model this system. The program Gephi was used to visualize and manipulate the generated graphs.

<!-- b000129 | prose | pages [9] -->
5.2 Analyzing the Network

<!-- b000130 | prose | pages [9] -->
We are next interested in calculating the skill of each team based on the graphs generated in the previous section. To do this, we will use the concept of central- ity to investigate the properties of the nodes and their connections. Centrality is a measure of the relative importance of a speciﬁc node on a graph based on the connections to and from that node. There are a number of ways to calculate centrality, but the four main measures of centrality are degree, betweenness, closeness, and eigenvector centrality.

<!-- b000131 | prose | pages [9] -->
5.2.1 Degree Centrality

<!-- b000132 | prose | pages [9] -->
Degree centrality is the simplest centrality measure, and is simply the total number of edges connecting to a speciﬁc node. For a directional graph, indegree is the number of edges directed into the node, while outdegree is the number of edges directed away from the node. Since in our network, edges directed inward are losses and edges directed outwards are wins, indegree represents the total number of losses and outdegree measures the total number of wins. Logically, therefore, outdegreee

<!-- b000133 | prose | pages [9] -->
indegreee represents the win

<!-- b000134 | prose | pages [9] -->
loss ratio of the team. This ratio is often used as a metric of the skill of a team; however, there are several

<!-- b000135 | prose | pages [9] -->
6

<!-- b000136 | furniture | pages [10] -->
Team #30680

<!-- b000137 | furniture | pages [10] -->
Page 7 of 18

<!-- b000138 | caption | pages [10] -->
Figure 1: A complete network for the 2009-2010 NCAA Div. I basketball season.

<!-- b000139 | prose | pages [10] -->
Each node represents a team, and each edge represents a game between the two teams. Note that, since teams play other teams in their conference most often, many teams have clustered into one of the 32 NCAA Div.1 Conferences.

<!-- b000140 | prose | pages [10] -->
weaknesses to this metric. The most prominent of these weaknesses arises from the fact that, since not every team plays every other team over the course of the season, some teams will naturally play more diﬃcult teams while others will play less diﬃcult teams. This is exaggerated by the fact that many college sports are arranged into conferences, with some conferences containing mostly highly-ranked teams and others containing mostly low-ranked teams. Therefore, win/loss percentage often exaggerates the skill of teams in weaker conferences while failing to highlight teams in more diﬃcult conferences.

<!-- b000141 | prose | pages [10] -->
5.2.2 Betweenness and Closeness Centrality

<!-- b000142 | prose | pages [10] -->
Betweenness centrality is deﬁned as a measure of how often a speciﬁc node acts as a bridge along the shortest path between two other nodes in the graph. Although a very useful metric in, for example, social networks, betweenness centrality is less relevant in our graphs as the distance between nodes is based on the game schedule and conference layout, and not on team skill. Similarly, closeness centrality is a measure of the average distance of a speciﬁc node to

<!-- b000143 | prose | pages [10] -->
7

<!-- b000144 | furniture | pages [11] -->
Team #30680

<!-- b000145 | furniture | pages [11] -->
Page 8 of 18

<!-- b000146 | prose | pages [11] -->
another node in the graph - also not particularly relevant in our graphs because distance between nodes is not related to team skills.

<!-- b000147 | prose | pages [11] -->
5.2.3 Eigenvector Centrality

<!-- b000148 | prose | pages [11] -->
Eigenvector centrality is a measure of the inﬂuence of a node in a network based on its connections to other nodes. However, instead of each connection to another node having a ﬁxed contribution to the centrality rating (e.g. de- gree centrality), the contribution of each connection in eigenvector centrality is proportional to the eigenvector centrality of the node being connected to. Therefore, connections to high-ranked nodes will have a greater inﬂuence on the ranking of a node than connections to low-ranking nodes. When applied to our graph, the metric of eigenvector centrality will assign a higher ranking to teams that win over other high-ranking teams, while winning over lower- ranking nodes has a lesser contribution. This is important because it addresses the main limitation over degree centrality or win/loss percentage, where winning over many low-ranked teams can give a team a high rank.

<!-- b000149 | prose | pages [11] -->
If we let G represent a graph with nodes N, and let A = (an,t) be an adjacency matrix where an,t = 1 if node n is connected to node t and an,t = 0 otherwise. If we deﬁne xa as the eigenvector centrality score of node a, then the eigenvector centrality score of node n is given by:

<!-- b000150 | prose | pages [11] -->
xn = 1

<!-- b000151 | prose | pages [11] -->
X

<!-- b000152 | prose | pages [11] -->
λ

<!-- b000153 | prose | pages [11] -->
t∈M(n)

<!-- b000154 | prose | pages [11] -->
xt = 1

<!-- b000155 | prose | pages [11] -->
X

<!-- b000156 | prose | pages [11] -->
an,txt (1)

<!-- b000157 | prose | pages [11] -->
λ

<!-- b000158 | prose | pages [11] -->
t∈G

<!-- b000159 | prose | pages [11] -->
where λ represents a constant and M(n) represents the set of neighbors of node n.

<!-- b000160 | prose | pages [11] -->
If we convert this equation into vector notation, we ﬁnd that this equation is identical to the eigenvector equation:

<!-- b000161 | prose | pages [11] -->
Ax = λx (2)

<!-- b000162 | prose | pages [11] -->
If we place the restriction that the ranking of each node must be positive, we ﬁnd that there is a unique solution for the eigenvector x, where the nth

<!-- b000163 | prose | pages [11] -->
component of x represents the ranking of node n. There are multiple diﬀerent methods of calculating x; most of them are iterative methods that converge on a ﬁnal value of x after numerous iterations. One interesting and intuitive method of calculating the eigenvector x is highlighted below. It has been shown that the eigenvector x is proportional to the row sums of a matrix S formed by the following equation [6, 9]:

<!-- b000164 | prose | pages [11] -->
S = A + λ−1A2 + λ−2A3 + ... + λn−1An + ...

<!-- b000165 | prose | pages [11] -->
(3)

<!-- b000166 | prose | pages [11] -->
where A is the adjacency matrix of the network and λ is a constant (the principle eigenvalue). We know that the powers of an adjacency matrix describe the number of walks of a certain length from node to node.

<!-- b000167 | prose | pages [11] -->
The power of the eigenvalue (x) describes some function of length.

<!-- b000168 | prose | pages [11] -->
Therefore, S and the

<!-- b000169 | prose | pages [11] -->
8 8

<!-- b000170 | furniture | pages [12] -->
Team #30680

<!-- b000171 | furniture | pages [12] -->
Page 9 of 18

<!-- b000172 | prose | pages [12] -->
eigenvector centrality matrix both describe the number of walks of all lengths weighted inversely by the length of the walk. This explanation is an intuitive way to describe the eigenvector centrality metric.

<!-- b000173 | prose | pages [12] -->
We utilized NetworkX (a Python library) to calculate the eigenvector centrality measure for our sports game networks.

<!-- b000174 | prose | pages [12] -->
We can apply eigenvector centrality in the context of this problem because it takes into account both the number of wins and losses and whether those wins and losses were against “good” or “bad” teams. If we have the following graph: A →B →C and know that C is a good team, it follows that A is also a good team because they beat a team who then went on to beat C. This is an example of the kind of interaction that the metric of eigenvector centrality takes into account. Calculating this metric over the entire yearly graph, we can create a list of teams ranked by eigenvector centrality that is quite accurate. Below is a table of top ranks from eigenvector centrality compared to the AP and USA Today polls for a random sample of our data, the 2009-2010 NCAA Division I Mens Basketball season. It shows that eigenvector centrality creates an accurate ranking of college basketball teams. The italicized entries are ones that appear in the top ten of both eigenvector centrality ranking and one of the AP and USA Today polls.

<!-- b000175 | prose | pages [12] -->
Rank Eigenvector Centrality 1 Duke 2 West Virginia 3 Kansas 4 Syracuse 5 Purdue 6 Georgetown 7 Ohio St. 8 Washington 9 Kentucky 10 Kansas St.

<!-- b000176 | prose | pages [12] -->
AP Poll USA Today Poll Kansas Kansas Michigan St.

<!-- b000177 | prose | pages [12] -->
Michigan St. Texas Texas Kentucky North Carolina Villanova Kentucky North Carolina Villanova Purdue Purdue West Virginia Duke Duke West Virginia Tennessee Butler

<!-- b000178 | prose | pages [12] -->
As seen in the table above, six out of the top ten teams as determined by eigenvector centrality are also found on the top ten rankings list of popular polls such as AP and USA Today. We can see that the metric we have created using a networks-based model creates results that aﬃrms the results of commonly- accepted rankings. Our team-ranking model has a clear, easy-to-understand basis in networks-based centrality measures and gives reasonably accurate re- sults. It should be noted that we chose this approach to ranking teams over a much simpler approach such as simply gathering the AP rankings for vari- ous reasons, one of which is that there are not reliable sources of college sport ranking data that cover the entire history of the sports we are interested in. Therefore, by calculating the rankings ourselves, we can analyze a wider range of historical data.

<!-- b000179 | prose | pages [12] -->
Below is a graph that visualizes the eigenvector centrality values for all games played in the 2010-2011 NCAA Division I Mens Football tournament.

<!-- b000180 | prose | pages [12] -->
9 9

<!-- b000181 | furniture | pages [13] -->
Team #30680

<!-- b000182 | furniture | pages [13] -->
Page 10 of 18

<!-- b000183 | prose | pages [13] -->
Larger and darker nodes represent teams that have high eigenvector centrality values, while smaller and lighter nodes represent teams that have low eigenvector centrality values. The large nodes therefore represent the best teams in the 2010-2011 season.

<!-- b000184 | caption | pages [13] -->
Figure 2: A complete network for the 2012-2013 NCAA Div. I Men’s Basketball

<!-- b000185 | prose | pages [13] -->
season. The size and darkness of each nodes represents its relative eigenvector centrality value. Again, note the clustering of teams into NCAA conferences.

<!-- b000186 | prose | pages [13] -->
6 Separating the Coach Eﬀect

<!-- b000187 | prose | pages [13] -->
The model we created in the previous section works well for ﬁnding the relative skills of teams for any given year. However, in order to rank the coaches, it is necessary to decouple the coach skill from the overall team skill. Let us assume that the overall team skill is a function of two main factors, coach skill and player skill. Speciﬁcally, if Cs is the coach skill, Ps is the player skill, and Ts is

<!-- b000188 | prose | pages [13] -->
10

<!-- b000189 | furniture | pages [14] -->
Team #30680

<!-- b000190 | furniture | pages [14] -->
Page 11 of 18

<!-- b000191 | prose | pages [14] -->
the team skill, we hypothesize that

<!-- b000192 | prose | pages [14] -->
Ts = Cs · Ps, (4)

<!-- b000193 | prose | pages [14] -->
as Cs of any particular team could be thought of as a multiplier on the player skill Ps, which results in team skill Ts.

<!-- b000194 | prose | pages [14] -->
Although the relationship between these factors may be more complex in real life, this relationship gives us reasonable results and works well with our model.

<!-- b000195 | prose | pages [14] -->
6.1 When is Coach Skill Important?

<!-- b000196 | prose | pages [14] -->
We will now make a key assumption regarding player skill and coach skill. In order to separate the eﬀects of these two factors on the overall team skill, we must deﬁne some diﬀerence in eﬀect between the two. That is, the player skill will inﬂuence the team skill in some fundamentally diﬀerent way from the coach skill.

<!-- b000197 | prose | pages [14] -->
Think again to a game played between two arbitrary teams A and B. There are two main cases to be considered:

<!-- b000198 | prose | pages [14] -->
Case one: Player skills diﬀer signiﬁcantly: Without loss of generality, assume that P(A) >> P(B), where P(x) is a function returning the player skills of any given team x. It is clear that A winning the game is a likely outcome. We can draw a plot approximating the probability of winning by a certain margin, which is shown in Figure 3.

<!-- b000199 | prose | pages [14] -->
Probability

<!-- b000200 | prose | pages [14] -->
Margin of Win

<!-- b000201 | caption | pages [14] -->
Figure 3: A has a high chance of winning when its players are more skilled.

<!-- b000202 | prose | pages [14] -->
Because the player skills are very imbalanced, the coach skill will likely not change the outcome of the game. Even if B has an excellent coach, the eﬀect of the coach’s skill will not be enough to make B’s win likely.

<!-- b000203 | prose | pages [14] -->
Case two: Player skills approximately equal: If the player skills of the two teams are approximately evenly matched, the coach skill has a much higher likelihood of impacting the outcome of the game. When the player skills are

<!-- b000204 | prose | pages [14] -->
11

<!-- b000205 | furniture | pages [15] -->
Team #30680

<!-- b000206 | furniture | pages [15] -->
Page 12 of 18

<!-- b000207 | prose | pages [15] -->
similar for both teams, the Gaussian curve looks like the one shown in Figure 4. In this situation, the coach has a much greater inﬂuene on the outcome of the game - crucial calls of time-outs, player substitutions, and strategies can make or break an otherwise evenly matched game. Therefore, if the coach skills are unequal, causing the Gaussian curve is shifted even slightly, one team will have a higher chance of winning (even if the margin of win will likely be small).

<!-- b000208 | prose | pages [15] -->
Probability

<!-- b000209 | prose | pages [15] -->
Margin of Win

<!-- b000210 | caption | pages [15] -->
Figure 4: Neither A nor B are more likely to win when player skills are the

<!-- b000211 | prose | pages [15] -->
same (if player skill is the only factor considered).

<!-- b000212 | prose | pages [15] -->
With the assumptions regarding the eﬀect of coach skill given a diﬀerence in player skills, we can say that the eﬀect of a coach can be expressed as:

<!-- b000213 | prose | pages [15] -->


<!-- b000214 | prose | pages [15] -->
(CA −CB) ·

<!-- b000215 | prose | pages [15] -->


<!-- b000216 | prose | pages [15] -->
1

<!-- b000217 | prose | pages [15] -->
(5)

<!-- b000218 | prose | pages [15] -->
1 + α|PA −PB|

<!-- b000219 | prose | pages [15] -->
Where CA is the coach skill of team A, CB is the coach skill of team B, PA is the player skill of team A, PB is the player skill of team B, and α is some scalar constant. With this expression, the diﬀerence in coach skills is diminished if the diﬀerence in player skills is large, and coach eﬀect is fully present when players have equal skill.

<!-- b000220 | prose | pages [15] -->
Margin of Win Probability 6.2

<!-- b000221 | prose | pages [15] -->
Now we wish to use the coach eﬀect expression to create a function giving the probability that team A will beat team B by a margin of x points. A negative value of x means that team B beat team A. The probability that A beats B is:

<!-- b000222 | prose | pages [15] -->
 1

<!-- b000223 | prose | pages [15] -->
−

<!-- b000224 | prose | pages [15] -->
2

<!-- b000225 | prose | pages [15] -->
E (C · player eﬀect + D · coach eﬀect −margin)

<!-- b000226 | prose | pages [15] -->
K · e

<!-- b000227 | prose | pages [15] -->
(6)

<!-- b000228 | prose | pages [15] -->
where C, D, E are constant weights, player eﬀect is PA −PB, coach eﬀect is given by Equation 5, and margin is x.

<!-- b000229 | prose | pages [15] -->
12 12

<!-- b000230 | furniture | pages [16] -->
Team #30680

<!-- b000231 | prose | pages [16] -->
This probability is maximized when

<!-- b000232 | furniture | pages [16] -->
Page 13 of 18

<!-- b000233 | prose | pages [16] -->
C · player eﬀect + D · coach eﬀect = margin.

<!-- b000234 | prose | pages [16] -->
This accurately models our situation, as it is more likely that team A wins by a margin equal to their combined coach and team eﬀects over team B.

<!-- b000235 | prose | pages [16] -->
Since team skill is comprised of player skill and coach skill, we may calculate a given team’s player skill using their team skill and coach skill.

<!-- b000236 | prose | pages [16] -->
Thus, the probability that team A beats team B by margin x can be determined solely using the coach skills of the respective teams and their eigenvector centrality measures.

<!-- b000237 | prose | pages [16] -->
Optimizing the Probability Function 6.3

<!-- b000238 | prose | pages [16] -->
We want to assign all the coaches various skill levels to maximize the likelihood that the given historical game data occurred.

<!-- b000239 | prose | pages [16] -->
To do this, we maximize the probability function described in Equation 6 over all games from historical data by ﬁnding an optimal value for the coach skill vectors CA and CB. Formally, the probability that the historical data occurred in a given year is

<!-- b000240 | prose | pages [16] -->
 1

<!-- b000241 | prose | pages [16] -->
2

<!-- b000242 | prose | pages [16] -->
E (C · player eﬀect + D · coach eﬀect −margin)

<!-- b000243 | prose | pages [16] -->
−

<!-- b000244 | prose | pages [16] -->
Y

<!-- b000245 | prose | pages [16] -->
K · e

<!-- b000246 | prose | pages [16] -->
all games

<!-- b000247 | prose | pages [16] -->
.

<!-- b000248 | prose | pages [16] -->
(7)

<!-- b000249 | prose | pages [16] -->
After some algebra, we notice that maximizing this value is equalivalent to minimizing the value of the cost function J, where

<!-- b000250 | prose | pages [16] -->
X

<!-- b000251 | prose | pages [16] -->
(C · player eﬀect + D · coach eﬀect −margin)2

<!-- b000252 | prose | pages [16] -->
J(Cs) =

<!-- b000253 | prose | pages [16] -->
all games

<!-- b000254 | prose | pages [16] -->
(8)

<!-- b000255 | prose | pages [16] -->
Because P(A beats B by x) is a nonlinear function of four variables for each edge in our network, and because we must iterate over all edges, calculus and linear algebra techniques are not applicable. We will investigate three techniques (Genetic Algorithm, Nelder-Mead Search, and Powell Search) to ﬁnd the global maximum of our probability function.

<!-- b000256 | prose | pages [16] -->
6.3.1

<!-- b000257 | heading | pages [16] -->
Genetic Algorithm

<!-- b000258 | prose | pages [16] -->
At ﬁrst, our team set out to implement a Genetic Algorithm to create the coach skill and player skill vectors that would maximize the probability of the win/loss margins occurring. We created a program that would initialize 1000 random coach skill and player skill vectors.

<!-- b000259 | prose | pages [16] -->
The probability function was calculated for each pair of vectors, and then the steps of the Genetic Algorithm were ran (carry over the “most ﬁt” solution to the next generation, cross random elements of the coach skill vectors with each other, and mutate a certain percentage of the data randomly). However, our genetic algorithm took a very long time to converge and did not produce the optimal values. Therefore, we decided to forgo optimization with genetic algorithm methods.

<!-- b000260 | prose | pages [16] -->
13 13

<!-- b000261 | furniture | pages [17] -->
Team #30680

<!-- b000262 | prose | pages [17] -->
6.3.2 Nelder-Mead Method

<!-- b000263 | furniture | pages [17] -->
Page 14 of 18

<!-- b000264 | prose | pages [17] -->
We wanted to attempt optimization with a technique that would iterate over the function instead of mutating and crossing over. The Nelder-Mead method starts with a randomly initialized coach skills vector Cs and uses a simplex to tweak the values of Cs to improve the value of a function for the next iteration [7]. However, running Nelder-Mead found local extrema which barely increased the probability of the historical data occurring, so we excluded it from this report.

<!-- b000265 | prose | pages [17] -->
6.3.3 Powell’s Method

<!-- b000266 | prose | pages [17] -->
A more eﬃcient method of ﬁnding minima is Powell’s Method. This algorithm works by initalizing a random coach skills vector Cs, and uses bi-directional search methods along several search vectors to ﬁnd the optimal coach skills. A detailed explanation of the mathematical basis for Powell’s method can be found in Powell’s paper on the algorithm [8]. We found that Powell’s method was several times faster than the Nelder-Mead Method and produced reasonable results for the minimization of our probability function. Therefore, our team decided to use Powell’s method as the main algorithm to determine the coach skills vector. We implemented this algorithm in Python and ran it across every edge in our network for each year that we had data. It signiﬁcantly lowered our cost function J over several thousand iterations.

<!-- b000267 | prose | pages [17] -->
Rank 1962 1 John Wooden 2 Forrest Twogood 3 LaDell Anderson 2000 2005 Lute Olson Jim Boeheim John Wooden Roy Williams Jerry Dunn Thad Matta

<!-- b000268 | prose | pages [17] -->
The table above shows the results of running Powell’s method until the probability function shown in Equation 6 is optimized, for three widely separated arbitrary years. We have chosen to show the top three coaches per year for the purposes of conciseness. We will additionally highlight the performance of our top three three outstanding coaches.

<!-- b000269 | prose | pages [17] -->
John Wooden - UCLA: John Wooden built one of the ’greatest dynasties in all of sports at UCLA’, winning 10 NCAA Division I Basketball tournaments and leading an unmatched streak of seven tournaments in a row from 1967 to 1973 [1]. He won 88 straight games during one stretch Jim Boeheim - Syracuse: Boeheim has led Syracuse to the NCAA Tour- nament 28 of the 37 years that he has been coaching the team [3]. He is second only to Mike Krzyzewsky of Duke in total wins. He consistently performs even when his players vary - he is the only head coach in NCAA history to lead a school to four ﬁnal four appearences in four separate decades.

<!-- b000270 | prose | pages [17] -->
Roy Williams - North Carolina: Williams is currently the head of the basketball program at North Carolina where he is sixth all-time in the NCAA for winning percentage [5]. He performs impressively no matter who his players are - he is one of two coaches in history to have led two diﬀerent teams to the Final Four at least three times each.

<!-- b000271 | prose | pages [17] -->
14 14

<!-- b000272 | furniture | pages [18] -->
Team #30680

<!-- b000273 | prose | pages [18] -->
7 Ranking Coaches

<!-- b000274 | furniture | pages [18] -->
Page 15 of 18

<!-- b000275 | prose | pages [18] -->
Knowing that we are only concerned with ﬁnding the top ﬁve coaches per sport, we decided to only consider the ﬁve highest-ranked coaches for each year. To calculate the overall ranking of a coach over all possible years, we considered the number of years coached and the frequency which the coach appeared in the yearly top ﬁve list. That is:

<!-- b000276 | prose | pages [18] -->
Cv = Na

<!-- b000277 | prose | pages [18] -->
(9)

<!-- b000278 | prose | pages [18] -->
Nc

<!-- b000279 | prose | pages [18] -->
Where Cv is the overall value assigned to a certain coach, Na is the number of times a coach appears in yearly top ﬁve coach lists, and Nc is the number of years that the coach has been active. This method of measuring overall coach skill is especially strong because we can account for instances where coaches change teams.

<!-- b000280 | prose | pages [18] -->
Top Coaches of the Last 100 Years 7.1

<!-- b000281 | prose | pages [18] -->
After optimizing the coach skill vectors for each year, taking the top ﬁve, and ranking the coaches based on the number of times they appeared in the top ﬁve list, we arrived at the following table. This is our deﬁnitive ranking of the top ﬁve coaches for the last 100 years, and their associated career-history ranking:

<!-- b000282 | prose | pages [18] -->
Rank Mens Basketball Mens Football Mens Baseball Glenn Scobey Warner - 0.24 1 John Wooden - 0.28 Mark Marquess - 0.27 Bobby Bowden - 0.23 2 Lute Olson - 0.26 3 Jim Boeheim - 0.24 4 Gregg Marshall - .23 Augie Garrido - 0.24 Jim Grobe - 0.18 Tom Chandler - 0.22 Bob Stoops - 0.17 Richard Jones - 0.19 Bill Peterson - 0.16 5 Jamie Dixon - .21

<!-- b000283 | prose | pages [18] -->
8

<!-- b000284 | heading | pages [18] -->
Testing our Model

<!-- b000285 | prose | pages [18] -->
8.1

<!-- b000286 | heading | pages [18] -->
Sensitivity Analysis

<!-- b000287 | prose | pages [18] -->
Bill Walkenbach - 0.16

<!-- b000288 | prose | pages [18] -->
A requirement of any good model is that it must be tolerant to a small amount of error in its inputs. In our model, possible sources of error could include im- properly recorded game results, incorrect ﬁnal scores, or entirely missing games. These sources of error could cause a badly written algorithm to return incorrect results. To test the sensitivity of our model to these sources of error, we decided to create intentional small sources of error in the data and compare the results to the original, unmodiﬁed results.

<!-- b000289 | prose | pages [18] -->
The ﬁrst intentional source of error that we incorporated into our model was the deletion of a game, speciﬁcally a regular-season win for Alabama (the team with the top-ranked coach in 1975) over Providence with a score of 67 to 60. We expected that the skill value of the coach of the Alabama team would

<!-- b000290 | prose | pages [18] -->
15 15

<!-- b000291 | furniture | pages [19] -->
Team #30680

<!-- b000292 | furniture | pages [19] -->
Page 16 of 18

<!-- b000293 | prose | pages [19] -->
decrease slightly with this modiﬁcation. When we ran and analyzed the results, we found that the coach skill value did in fact decrease by approximately 1%, as we expected. However, the Alabama coach maintained his ranking of top coach for the season.

<!-- b000294 | prose | pages [19] -->
The second change that we incorporated was to switch the results of the same game (Alabama 67, Providence 60) to a win for Providence (Providence 67, Alabama 60).

<!-- b000295 | prose | pages [19] -->
We expect this will have a greater negative inﬂuence on the skill value of the Alabama coach, and when we ran the analysis we found that, indeed, the Alabama coach skill value decreased by approximately 4%. Although a relatively minor diﬀerence, the second-ranked coach originally had a skill value only very slightly behind the Alabama coach, and the 4% loss in fact placed the second-ranked coach in the ﬁrst ranking position.

<!-- b000296 | prose | pages [19] -->
From this analysis we can see that our model follows our predictions accu- rately, and that removing factors that add positively to the skill ranking of a coach is detrimental to their skill value. Although the changes we made were minor, there is often a lot of competition for the ﬁrst-place ranking of a coach, and due to the limited number of games played per season, a change to this data can have an inﬂuence on the ﬁnal ranking. Although these results indicate that error in our data can eﬀect the ﬁnal ranking, the analysis also shows that our model responds predictably to a variation in the input.

<!-- b000297 | prose | pages [19] -->
8.2

<!-- b000298 | heading | pages [19] -->
Strengths

<!-- b000299 | prose | pages [19] -->
The main strength of our approach is that it is able to separate coach proﬁciency from team proﬁciency by calculating probabilities that the historical game data occur given coach skills.

<!-- b000300 | prose | pages [19] -->
This allows us to more accurately gauge the skills of a coach without factoring in the skills of his/her players. Furthermore, our approach is ﬂexible as many relationships can be modiﬁed. For example, if a study shows that there is a better function to describe the relationship between coach skill, player skill, and team skill, it can easily be used in our model. Our model is also able to compare the relative eﬀectiveness of coaches from all time periods, as long as the average margin of victory is similar across time periods.

<!-- b000301 | prose | pages [19] -->
8.3

<!-- b000302 | heading | pages [19] -->
Weaknesses

<!-- b000303 | prose | pages [19] -->
The main weakness of our model pertains to computational eﬃciency, as our computers could not always adequately calculate all necessary values in our model.

<!-- b000304 | prose | pages [19] -->
For example, the computer could not ﬁnd the eigenvector centrality values on a small percentage of the graphs, as the Von Mises iteration failed to converge. Furthermore, sometimes Powell’s method of minimizing our cost function yielded high costs relative to other years because the initialized array of coach skills was close to a local minima. This could be solved by running Powell’s method from several randomly initialized coach skills arrays, but this increases computational time. In fact, the overall results of our model could likely be improved signiﬁcantly given more time to run the iterative optimization

<!-- b000305 | prose | pages [19] -->
16

<!-- b000306 | furniture | pages [20] -->
Team #30680

<!-- b000307 | furniture | pages [20] -->
Page 17 of 18

<!-- b000308 | prose | pages [20] -->
algorithms with a higher accuracy, resulting in better approximations for the ideal matrix of coach skills.

<!-- b000309 | prose | pages [20] -->
9

<!-- b000310 | heading | pages [20] -->
Conclusions

<!-- b000311 | prose | pages [20] -->
In this report, we have analyzed nearly 300 years of data in order to determine the most accurate and unbiased ranking of all-time best college sports coaches. By constructing comprehensive networks with with edges representing each and every game played in the last century of the college sports that we analyzed, we were able to create a comprehensive metric of team skill using the concept of eigenvector centrality.

<!-- b000312 | prose | pages [20] -->
By considering win/loss margins, we were able to identify patterns that enabled us to separate the team skill measure into its two components - player skill and coach skill. We then created a probability function based on player skill and coach skill to determine the likelihood of an edge in our network occurring. By multiplying this probability across all edges, we were able to determine the probability of the entire graph occurring given team skill and coach skill vectors. Using an iterative, multivariable, machine learning algorithm, we maximized this probability function for coach skill for each season and for each sport. Using data that mapped the name of a coach to his/her team for each season, we were able to combine the results of each individual season and analyze the skill of each individual coach over their entire coaching history. From this data, we selected the top 5 coaches from every sport to feature as our all-time best coaches of the century.

<!-- b000313 | prose | pages [20] -->
17

<!-- b000314 | furniture | pages [21] -->
Team #30680

<!-- b000315 | furniture | pages [21] -->
Page 18 of 18

<!-- b000316 | heading | pages [21] -->
References

<!-- b000317 | references | pages [21] -->
[1] John

<!-- b000318 | references | pages [21] -->
Wooden.

<!-- b000319 | references | pages [21] -->
Retrieved

<!-- b000320 | references | pages [21] -->
from:

<!-- b000321 | references | pages [21] -->
http://msn.foxsports.com/

<!-- b000322 | references | pages [21] -->
collegebasketball/story/John-Wooden-dies-UCLA-coach-99-060410,

<!-- b000323 | references | pages [21] -->
2010.

<!-- b000324 | references | pages [21] -->
[2] ShrpSports. Retrieved from: http://www.shrpsports.com/, 2011.

<!-- b000325 | references | pages [21] -->
[3] Jim Boeheim. Retrieved from: http://cuse.com/coaches.aspx?rc=405&

<!-- b000326 | references | pages [21] -->
path=mbasket, 2012.

<!-- b000327 | references | pages [21] -->
[4] Sports-Reference. Retrieved from: http://www.sports-reference.com/,

<!-- b000328 | references | pages [21] -->
2013.

<!-- b000329 | references | pages [21] -->
[5] Roy Williams. Retrieved from: http://www.goheels.com/ViewArticle.

<!-- b000330 | references | pages [21] -->
dbml?ATCLID=205497516, 2014.

<!-- b000331 | references | pages [21] -->
[6] Stephen P. Borgatti. Centrality and network ﬂow. Social Networks, 27(1):55–

<!-- b000332 | references | pages [21] -->
71, January 2005.

<!-- b000333 | references | pages [21] -->
[7] JA Nelder and R Mead. A simplex method for function minimization. The

<!-- b000334 | references | pages [21] -->
Computer Journal, 1965.

<!-- b000335 | references | pages [21] -->
[8] MJD Powell. An eﬃcient method for ﬁnding the minimum of a function

<!-- b000336 | references | pages [21] -->
of several variables without calculating derivatives. The Computer Journal,

<!-- b000337 | references | pages [21] -->
1964.

<!-- b000338 | references | pages [21] -->
[9] Leo Spizzirri. Justiﬁcation and Application of Eigenvector Centrality. 2011.

<!-- b000339 | references | pages [21] -->
18
