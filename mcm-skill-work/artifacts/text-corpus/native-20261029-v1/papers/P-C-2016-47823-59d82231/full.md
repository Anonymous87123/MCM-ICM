# P-C-2016-47823-59d82231

Status: machine-draft; not source-verified.


<!-- b000001 | prose | pages [1] -->
Team	  Control	  Number

<!-- b000002 | prose | pages [1] -->
For	  office	  use	  only

<!-- b000003 | prose | pages [1] -->
For	  office	  use	  only

<!-- b000004 | prose | pages [1] -->
47823

<!-- b000005 | prose | pages [1] -->
T1 ________________

<!-- b000006 | prose | pages [1] -->
T2 ________________

<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | prose | pages [1] -->
T3 ________________

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem	  Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | prose | pages [1] -->
C C

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | prose | pages [1] -->
2016

<!-- b000020 | prose | pages [1] -->
MCM/ICM

<!-- b000021 | heading | pages [1] -->
Summary Sheet

<!-- b000022 | prose | pages [1] -->
(Your team's summary should be included as the first page of your electronic submission.)

<!-- b000023 | prose | pages [1] -->
Type	  a	  summary	  of	  your	  results	  on	  this	  page.	  Do	  not	  include	  the	  name	  of	  your	  school,	  advisor,	  or	  team	  members	  on	  this

<!-- b000024 | prose | pages [1] -->
page.

<!-- b000025 | prose | pages [1] -->
We	  develop	  a	  model	  to	  determine	  an	  optimal	  investment	  strategy	  to	  improve

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
the	  performance	  of	  undergraduate	  students	  in	  the	  US.	  Our	  model	  has	  three	  parts:

<!-- b000028 | prose | pages [1] -->
In	   the	   first	   part,	   we	   collect	   data	   about	   the	   focus	   of	   other	   foundations’

<!-- b000029 | furniture | pages [1] -->


<!-- b000030 | prose | pages [1] -->
investment	  by	  subjects	  and	  locations.	  We	  consider	  the	  charitable	  identity	  of	  the Goodgrant	  as	  well.	  Then	  we	  set	  out	  to	  decide	  our	  focus,	  which	  is	  to	  invest	  more on	   those	   schools	   with	   more	   minority	   races,	   lower	   educational	   performance, higher	  debt	  ratio	  and	  so	  on.	  In	  this	  part,	  we	  also	  classify	  the	  data	  into	  two	  groups, one	  for	  school	  selecting,	  and	  another	  for	  ROI	  determining.

<!-- b000031 | prose | pages [1] -->
In	   the	   second	   part,	   as	   a	   data	   extraction,	   we	   build	   a	   efficient	   and	   intuitive

<!-- b000032 | furniture | pages [1] -->


<!-- b000033 | prose | pages [1] -->
model	  to	  rank	  the	  candidate	  schools	  in	  accordance	  with	  the	  correlation	  of	  our focus,	  using	  the	  PCA	  method.	  After	  that,	  the	  top	  50	  schools	  are	  selected	  as	  our target	  schools.

<!-- b000034 | prose | pages [1] -->
In	  the	  third	  part，we	  make	  a	  key	  assumption	  that	  the	  social	  utility	  of	  a	  school

<!-- b000035 | furniture | pages [1] -->


<!-- b000036 | prose | pages [1] -->
has	   logarithmic	   relationship	   with	   the	   earnings	   of	   graduated	   students	   and	   the graduation	  rate.	  More	  over,	  we	  create	  a	  parameter	  k	  to	  denote	  the	  marginal	  rate of	   substitution	   (MRS)	   between	   the	   two	   factors	   above.	   After	   that,	   we	   come	   to define	  the	  ROI	  function	  of	  each	  target	  school	  as	  the	  incremental	  utility.

<!-- b000037 | prose | pages [1] -->
We	  further	  discuss	  how	  to	  devise	  the	  best	  strategy	  with	  several	  methods.	  At

<!-- b000038 | furniture | pages [1] -->


<!-- b000039 | prose | pages [1] -->
last,	   we	   choose	   the	   improved	   PSO	   algorithm	   based	   on	   augmented	   Lagrange function.	   This	   algorithm	   is	   a	   typical	   method	   to	   solve	   the	   multivariable optimization	  problem	  with	  constraint	  conditions.	  Then	  we	  offer	  a	  recommending list	  by	  the	  cumulative	  ROI	  in	  five	  years.	  What’s	  more,	  our	  model	  is	  broad	  enough to	  accommodate	  any	  non-­‐linear	  constraint	  optimization	  problem.

<!-- b000040 | prose | pages [1] -->
Finally,	   we	   change	   the	   numerical	   value	   of	   parameter	   k	   to	   examine	   the

<!-- b000041 | furniture | pages [1] -->


<!-- b000042 | prose | pages [1] -->
sensitivity	  of	  our	  investment	  strategy.	  The	  result	  shows	  that	  our	  model	  is	  robust.

<!-- b000043 | furniture | pages [1] -->


<!-- b000044 | furniture | pages [1] -->


<!-- b000045 | furniture | pages [1] -->


<!-- b000046 | furniture | pages [1] -->


<!-- b000047 | prose | pages [2] -->
The	  Optimal	  Investment	  Strategy	  Based	  on	  the	  Large-­‐scale

<!-- b000048 | prose | pages [2] -->
Non-­‐linear	  Constraint	  Optimization	  Methods

<!-- b000049 | heading | pages [2] -->
Contents

<!-- b000050 | furniture | pages [2] -->


<!-- b000051 | contents | pages [2] -->
1	   Problem	  Statement	  .....................................................................................................................	  3

<!-- b000052 | contents | pages [2] -->
2	   Planned	  Approach	  ......................................................................................................................	  3

<!-- b000053 | contents | pages [2] -->
3	   Assumptions	  ..................................................................................................................................	  4

<!-- b000054 | contents | pages [2] -->
4	   Data	  Analysis	  and	  Focus	  Decision	  .......................................................................................	  5

<!-- b000055 | contents | pages [2] -->
4.1	   Data	  Analysis	  ...................................................................................................................	  5

<!-- b000056 | contents | pages [2] -->
4.2	   Focus	  Decision	  ................................................................................................................	  6

<!-- b000057 | contents | pages [2] -->
5	   School	  Selecting	  ...........................................................................................................................	  8

<!-- b000058 | contents | pages [2] -->
5.1	   Manual	  Selection	  ............................................................................................................	  8

<!-- b000059 | contents | pages [2] -->
5.2	   PCA	  Selection	  ...................................................................................................................	  8

<!-- b000060 | contents | pages [2] -->
5.2.1	   Standardization	  .................................................................................................	  8

<!-- b000061 | contents | pages [2] -->
5.2.2	   Calculation	  ..........................................................................................................	  9

<!-- b000062 | contents | pages [2] -->
5.2.3	   Principle	  Components	  ....................................................................................	  9

<!-- b000063 | contents | pages [2] -->
5.2.4	   PCA	  Results	  .........................................................................................................	  9

<!-- b000064 | contents | pages [2] -->
6	   Strategy	  Making	  .........................................................................................................................	  10

<!-- b000065 | contents | pages [2] -->
6.1	   The	  ROI	  Function	  .........................................................................................................	  11

<!-- b000066 | contents | pages [2] -->
6.2	   Optimizing	  the	  Total	  ROI	  ..........................................................................................	  12

<!-- b000067 | contents | pages [2] -->
6.2.1	   Karush-­‐Kuhn-­‐Tucker	  Conditions	  ............................................................	  14

<!-- b000068 | contents | pages [2] -->
6.2.2	   PSO	  Algorithm	  .................................................................................................	  16

<!-- b000069 | contents | pages [2] -->
6.2.3	   Improved	   PSO	   algorithm	   based	   on	   augmented	   Lagrange

<!-- b000070 | contents | pages [2] -->
function	  (LA_PSO_GT)	  .................................................................................................	  16

<!-- b000071 | contents | pages [2] -->
7	   Result	  .............................................................................................................................................	  16

<!-- b000072 | contents | pages [2] -->
7.1	   Optimal	  Investment	  Strategy	  and	  Recommending	  List	  ..............................	  17

<!-- b000073 | contents | pages [2] -->
8	   Testing	  our	  Model	  .....................................................................................................................	  18

<!-- b000074 | contents | pages [2] -->
8.1	   Sensitivity	  Analysis	  .....................................................................................................	  18

<!-- b000075 | contents | pages [2] -->
8.2	   Strengths	  .........................................................................................................................	  19

<!-- b000076 | contents | pages [2] -->
8.3	   Weaknesses	  ....................................................................................................................	  19

<!-- b000077 | contents | pages [2] -->
9	   Conclusion	  ....................................................................................................................................	  20

<!-- b000078 | contents | pages [2] -->
10	   Letter	  to	  the	  CFO	  of	  the	  Goodgrant	  Foundation	  .......................................................	  20

<!-- b000079 | contents | pages [2] -->
11	   References	  .................................................................................................................................	  22

<!-- b000080 | contents | pages [2] -->
12	   Appendix	  1:	  Recommending	  List	  .....................................................................................	  23

<!-- b000081 | contents | pages [2] -->
13	   Appendix	  2	  An	  Introduction	  to	  the	  Improved	  PSO

<!-- b000082 | contents | pages [2] -->
Algorithm	  Based	  on	  Augmented	  Lagrange	  Function	  ........................................................	  25

<!-- b000083 | furniture | pages [2] -->


<!-- b000084 | furniture | pages [3] -->
Team	  #47823

<!-- b000085 | furniture | pages [3] -->
Page	  3	  of	  27

<!-- b000086 | heading | pages [3] -->
1	   Problem	  Statement

<!-- b000087 | furniture | pages [3] -->


<!-- b000088 | prose | pages [3] -->
Private	  foundations	  are	  created	  by	  an	  individual,	  family,	  or	  business	  to	  fulfill specific	  charitable	  missions.	  Those	  like	  Gates	  foundation	  and	  Lumina	  foundation make	  great	  efforts	  to	  improve	  the	  quality	  of	  health	  and	  education	  in	  relatively poor	  areas.	  We	  must	  set	  big	  goals	  and	  spare	  no	  effort	  on	  the	  way	  because	  the world	  won’t	  get	  better	  by	  itself.	  The	  Goodgrant,	  one	  of	  the	  foundations,	  intends to	   help	   improving	   educational	   performance	   of	   undergraduates	   attending colleges	  and	  universities	  in	  the	  United	  States.	  Given	  its	  potential	  donation	  of	  100 million	  dollars	  per	  year	  in	  five	  years,	  what	  is	  the	  best	  investment	  strategy?	  We are	  tasked	  with	  creating	  models	  that	  can	  be	  applied	  in	  the	  universities	  across	  the nation.	  The	  solution	  proposed	  within	  this	  paper	  will	  offer	  an	  insight	  to	  use	  the big	  data	  and	  will	  objectively	  devise	  the	  investment	  strategy	  including	  the	  target schools,	  investment	  amount	  and	  duration.

<!-- b000089 | heading | pages [3] -->
2	   Planned	  Approach

<!-- b000090 | furniture | pages [3] -->


<!-- b000091 | prose | pages [3] -->
Our	  objective	  is	  to	  set	  out	  the	  best	  strategy	  including	  three	  components:(1) target	   schools;(2)	   the	   investment	   amount	   per	   school;	   (3)	   the	   investment duration.	  And	  also	  we	  will	  offer	  an	  optimized	  and	  prioritized	  recommendation list	  of	  candidate	  schools	  based	  on	  each	  school’s	  return	  on	  investment	  (ROI).

<!-- b000092 | furniture | pages [3] -->


<!-- b000093 | prose | pages [3] -->
Faced	  with	  the	  big	  data	  problem,	  we	  can’t	  use	  the	  data	  directly	  because	  of the	   limitation	   of	   our	   personal	   computers	   and	   the	   length	   of	   the	   contest.	   If	   the data	  are	  directly	  applied,	  the	  computing	  system	  will	  run	  several	  days	  or	  weeks. As	  a	  result,	  the	  data	  selection	  is	  extremely	  important,	  which	  will	  also	  reflect	  the focus	  of	  the	  foundation.	  To	  determine	  the	  most	  effective	  computing	  system,	  we divide	  the	  problem	  into	  three	  parts	  together	  with	  the	  procedures	  as	  follows:

<!-- b000094 | furniture | pages [3] -->


<!-- b000095 | prose | pages [3] -->
Part	  one:	  Data	  Analysis	  and	  Focus	  Decision

<!-- b000096 | prose | pages [3] -->
1. We	  will	  give	  an	  analysis	  of	  the	  big	  data	  of	  the	  problem,	  which	  includes information	  of	  near	  3000	  schools.

<!-- b000097 | prose | pages [3] -->
2. Based	   on	   the	   data	   given	   and	   the	   statistics	   of	   the	   focus	   of	   foundations collected	   from	   the	   Internet,	   we	   will	   decide	   the	   focus	   of	   the	   Goodgrant, avoiding	   duplicating	   the	   investment	   and	   focus	   of	   other	   large	   grant organizations.

<!-- b000098 | furniture | pages [3] -->


<!-- b000099 | prose | pages [3] -->
Part	  two:	  School	  Selecting

<!-- b000100 | furniture | pages [4] -->
Team	  #47823

<!-- b000101 | furniture | pages [4] -->
Page	  4	  of	  27

<!-- b000102 | prose | pages [4] -->
1. Manual	  selection.	  We	  have	  taken	  some	  schools	  out	  of	  consideration	  for certain	   reasons	   (the	   reason	   will	   be	   explained	   below).	   For	   example,	   we exclude	   the	   schools	   located	   at	   NY,	   CA,	   WA	   and	   MA	   due	   to	   the	   large amount	  of	  existing	  grant	  foundations.

<!-- b000103 | prose | pages [4] -->
2. PCA	   (principle	   component	   analysis)	   selection.	   According	   to	   part	   of	   the data,	  the	  PCA	  method	  can	  rank	  the	  candidate	  schools	  by	  the	  degree	  of correlation	  of	  our	  focus.	  The	  top	  50	  schools	  will	  be	  selected	  out.

<!-- b000104 | furniture | pages [4] -->


<!-- b000105 | prose | pages [4] -->
Part	  three:	  Strategy	  Making

<!-- b000106 | prose | pages [4] -->
1. Derive	   a	   ROI	   function	   that,	   given	   the	   year	   and	   a	   specific	   investment amount	   of	   a	   candidate	   school,	   can	   output	   the	   utility	   in	   an	   appropriate manner.	   The	   function	   is	   based	   on	   the	   graduation	   rate,	   earnings	   of graduated	  students	  and	  so	  on.

<!-- b000107 | prose | pages [4] -->
2. Utilize	   an	   optimization	   algorithm	   to	   maximize	   the	   total	   utility	   of	   the target	  50	  schools	  (in	  part	  two	  (2)),	  return	  the	  amount	  of	  investment	  and the	  time	  duration	  per	  school.

<!-- b000108 | heading | pages [4] -->
3	   Assumptions

<!-- b000109 | furniture | pages [4] -->


<!-- b000110 | prose | pages [4] -->
Due	   to	   limited	   data	   about	   the	   educational	   performance	   of	   the	   candidate schools,	   the	   performance	   of	   the	   undergraduate	   students	   and	   the	   specific distribution	  of	  other	  grants	  by	  subjects,	  races	  and	  locations,	  we	  use	  the	  following assumptions	  to	  complete	  our	  model.	  These	  simplified	  assumptions	  will	  be	  used through	  our	  paper	  and	  can	  be	  improved	  with	  more	  reliable	  data.

<!-- b000111 | prose | pages [4] -->
The	   statistics	   of	   the	   candidate	   schools	   can	   be	   regarded	   as	   constant !

<!-- b000112 | prose | pages [4] -->
within	   five	   years.	   This	   assumption	   is	   reasonable	   to	   a	   large	   extent because	   the	   identities	   of	   a	   specific	   college	   won’t	   change	   a	   lot	   in	   five years.

<!-- b000113 | prose | pages [4] -->
The	  school	  will	  devote	  all	  the	  funding	  received	  this	  year	  to	  improving !

<!-- b000114 | prose | pages [4] -->
the	  students’	  performance.

<!-- b000115 | prose | pages [4] -->
The	  appropriate	  manner	  to	  measure	  the	  return	  on	  the	  investment	  is	  the !

<!-- b000116 | prose | pages [4] -->
school’s	   incremental	   utility.	   The	   utility	   function	   must	   be	   concave (𝜕!𝑦/𝜕𝑥!<0).	  If	  not,	  we	  should	  give	  the	  whole	  100	  million	  to	  one	  college to	  maximize	  the	  total	  incremental	  utility,	  which	  is	  opposite	  against	  the common	  sense.	  And	  it’s	  reasonable	  in	  economic	  consideration,	  as	  with the	  capital	  growth,	  the	  marginal	  production	  will	  be	  less	  and	  less.	  So	  we assume	   the	   utility	   function	   has	   this	   typical	   formulation	   𝑈! = log  (𝑥), where	   𝑈!	   is	  the	  utility,	   𝑥	   are	  the	  independent	  variables.

<!-- b000117 | prose | pages [4] -->
Neglect	  the	  discount	  rate	  of	  the	  capital.	  In	  this	  paper,	  we	  do	  not	  take	  the !

<!-- b000118 | furniture | pages [5] -->
Team	  #47823

<!-- b000119 | prose | pages [5] -->
inflation	  into	  consideration.

<!-- b000120 | furniture | pages [5] -->
Page	  5	  of	  27

<!-- b000121 | prose | pages [5] -->
Here	  are	  the	  notations	  and	  their	  meanings	  in	  our	  paper:

<!-- b000122 | furniture | pages [5] -->


<!-- b000123 | heading | pages [5] -->
Notation

<!-- b000124 | prose | pages [5] -->
Meaning Social	  utility	  of	  the	  school U Amount	  of	  the	  investment x Time	  period	  (j	  =0,1,2,3,4,5) j Share	  of	  students	  earning	  over	  $25,000/year m Median	  earnings	  of	  students	  working	  and	  not	  enrolled	  10	  years	  after	  entry M Number	  of	  undergraduate	  degree-­‐seeking	  students N MRS	  (marginal	  rate	  of	  substitution) k g λ,ν Graduation	  rate Lagrange	  multiplier

<!-- b000125 | caption | pages [5] -->
Table	  1:	  notation

<!-- b000126 | heading | pages [5] -->
4	   Data	  Analysis	  and	  Focus	  Decision

<!-- b000127 | prose | pages [5] -->
Since	  we	  are	  tackling	  with	  a	  problem	  with	  big	  data,	  there	  is	  a	  diversity	  of

<!-- b000128 | furniture | pages [5] -->


<!-- b000129 | prose | pages [5] -->
inputs	   with	   different	   types.	   On	   the	   other	   hand,	   the	   inputs	   interact	   with	   each other	  to	  some	  degree.	  We	  must	  deeply	  analyze	  the	  data	  to	  dig	  out	  the	  meaning	  of each	  column	  and	  separate	  them	  in	  different	  groups.

<!-- b000130 | prose | pages [5] -->
After	   the	   analysis,	   we	   set	   out	   to	   collect	   the	   data	   of	   other	   large	   grant

<!-- b000131 | furniture | pages [5] -->


<!-- b000132 | prose | pages [5] -->
foundations，including	   their	   focus	   by	   different	   subjects,	   races	   and	   locations, together	  with	  other	  information	  available.	  Based	  on	  the	  data	  collected,	  we	  can determine	   the	   focus	   of	   the	   Goodgrant,	   which	   ensures	   the	   least	   degree	   of duplication.

<!-- b000133 | heading | pages [5] -->
4.1	  Data	  Analysis

<!-- b000134 | prose | pages [5] -->
We	  analyze	  the	  data	  in	  the	  attached	  Excel	  sheet	  Most	  Recent	  Cohorts	  Data.

<!-- b000135 | furniture | pages [5] -->


<!-- b000136 | prose | pages [5] -->
We	  find	  out	  that	  there	  are	  continuous	  and	  discrete	  data.	  The	  continuous	  data	  can be	  separated	  into	  two	  groups,	  one	  for	  determining	  the	  focus	  as	  well	  as	  school selecting,	  another	  for	  measuring	  the	  school’s	  utility	  as	  well	  as	  determining	  the ROI.	  So	  at	  last,	  we	  separate	  them	  into	  three	  components,	  each	  for	  different	  use.

<!-- b000137 | prose | pages [5] -->
Type	  and	  use Variable

<!-- b000138 | prose | pages [5] -->
SAT/ACT	  scores PCIP	  (the	  distribution	  by	  subject)

<!-- b000139 | prose | pages [5] -->
Continuous	  data	  for

<!-- b000140 | prose | pages [5] -->
school	  selecting

<!-- b000141 | prose | pages [5] -->
UGDS_(the	  distribution	  by	  race)

<!-- b000142 | prose | pages [5] -->
PPTUG_EF(part-­‐time	  ratio)

<!-- b000143 | furniture | pages [6] -->
Team	  #47823

<!-- b000144 | furniture | pages [6] -->
Page	  6	  of	  27

<!-- b000145 | prose | pages [6] -->
PCTPELL(pell	  grant	  ratio) UG_25_abv(the	  percentage	  of	  students	  above	  25)

<!-- b000146 | prose | pages [6] -->
GRAD_DEBT_MDN_SUPP(debt)

<!-- b000147 | prose | pages [6] -->
RPY_3YR_RT_SUPP(debt	  ratio)

<!-- b000148 | prose | pages [6] -->
Discrete	  data	  for

<!-- b000149 | prose | pages [6] -->
CONTRAL	  PBI	  ANNHI	  TRIBAL	  AANAPII	  HIS	  NANTI school	  selecting

<!-- b000150 | prose | pages [6] -->
UGDS	  (the	  number	  of	  students) C150	   	   C200	  (graduation	  rate)

<!-- b000151 | prose | pages [6] -->
Continuous	  data	  for determining	  the	  ROI

<!-- b000152 | prose | pages [6] -->
md_earn_wne_p10(median	  of	  earnings)

<!-- b000153 | prose | pages [6] -->
gt_25k_p6(earnings	  above	  25k	  ratio)

<!-- b000154 | caption | pages [6] -->
Table	  2:	  the	  different	  types	  of	  variables	  and	  their	  use

<!-- b000155 | heading | pages [6] -->
4.2	  Focus	  Decision

<!-- b000156 | furniture | pages [6] -->


<!-- b000157 | prose | pages [6] -->
First	  of	  all,	  we	  define	  the	  Goodgrant	  as	  a	  charitable	  organization	  to	  make	  the world	   more	   equal.	   Based	   on	   this	   duty,	   the	   Goodgrant	   aims	   at	   helping	   those undergraduate	   students	   who	   are	   relatively	   poor,	   under	   debt,	   or	   has	   low SAT/ACT	   scores	   and	   those	   schools	   located	   at	   small	   cities,	   consisting	   of	   more minority	  races,	  with	  low	  graduated	  rate	  and	  so	  on.

<!-- b000158 | furniture | pages [6] -->


<!-- b000159 | prose | pages [6] -->
Secondly,	  for	  not	  duplicating	  other	  organizations’	  investment	  and	  focus,	  we collect	  the	  data	  of	  the	  distribution	  of	  1000	  foundations	  by	  location	  and	  subject. The	  statistics	  are	  presented	  below.

<!-- b000160 | caption | pages [6] -->
Figure	  1:	  distribution	  of	  grants	  from	  FC	  1000	  foundations	  by	  subject	  area	  [1]

<!-- b000161 | prose | pages [6] -->
Source:	  http://data.foundationcenter.org/#/fc1000/subject:all/all/total/bar:amount/2012

<!-- b000162 | furniture | pages [6] -->


<!-- b000163 | prose | pages [6] -->
We	   can	   see	   that	   most	   foundation	   invested	   in	   the	   following	   three	   subjects:

<!-- b000164 | furniture | pages [7] -->
Team	  #47823

<!-- b000165 | furniture | pages [7] -->
Page	  7	  of	  27

<!-- b000166 | prose | pages [7] -->
Health,	   Education	   and	   Human	   services	   from	   Figure	   1.	   We	   define	   these	   three subjects	   as	   strong	   subjects.	   Notice	   that	   we	   have	   already	   the	   PCIP	   data	   (the percentage	  of	  degree	  awarded	  in	  different	  subjects).	  Compared	  to	  other	  subjects, the	  above	  three	  major	  subjects	  have	  received	  a	  large	  amount	  of	  grants.	  Further, the	  students	  who	  major	  in	  these	  three	  subjects	  will	  benefit	  a	  lot.	  So	  we	  decide	  to invest	  less	  on	  these	  three	  subjects	  but	  more	  on	  other	  subjects.

<!-- b000167 | furniture | pages [7] -->


<!-- b000168 | prose | pages [7] -->
However,	   there	   is	   a	   problem	   behind	   the	   logic	   above.	   The	   large	   amount	   of capital	  invested	  on	  these	  three	  subjects	  doesn’t	  mean	  that	  we	  should	  invest	  less on	   them.	   We	   only	   consider	   the	   capital	   supply	   while	   neglecting	   the	   capital demand.	  In	  other	  word,	  the	  financing	  gap	  really	  counts.	  However,	  taking	  capital demand	  into	  consideration	  will	  make	  the	  problem	  even	  complex.	  Also,	  we	  find	  it difficult	  to	  acquire	  the	  data	  of	  capital	  demand.	  As	  a	  result,	  we	  only	  consider	  the supply	  of	  capital,	  reluctantly.

<!-- b000169 | furniture | pages [7] -->


<!-- b000170 | caption | pages [7] -->
Figure	  2:	  distribution	  of	  grants	  from	  FC	  1000	  foundations	  by	  recipient	  location

<!-- b000171 | prose | pages [7] -->
Source:	  http://data.foundationcenter.org/#/fc1000/subject:all/all/total/bar:amount/2012

<!-- b000172 | furniture | pages [7] -->


<!-- b000173 | caption | pages [7] -->
Figure	   2	   tells	   us	   that	   most	   of	   the	   recipients	   are	   in	   four	   states:	   New	   York,

<!-- b000174 | prose | pages [7] -->
California,	   District	   of	   Columbia	   and	   Massachusetts.	   Follow	   the	   focus	   of	   the Goodgrant,	  we	  decide	  not	  to	  invest	  on	  these	  four	  states	  because	  these	  four	  states are	   relatively	   wealthy	   and	   already	   have	   many	   foundations.	   However,	   the problem	  also	  exists	  which	  is	  similar	  to	  the	  above.

<!-- b000175 | furniture | pages [7] -->


<!-- b000176 | prose | pages [7] -->
Here	   is	   a	   summary	   of	   our	   focus.	   We	   will	   invest	   more	   on	   schools	   which are/have:

<!-- b000177 | furniture | pages [8] -->
Team	  #47823

<!-- b000178 | furniture | pages [8] -->
Page	  8	  of	  27

<!-- b000179 | prose | pages [8] -->
1. Lower	  SAT/ACT	  scores

<!-- b000180 | prose | pages [8] -->
2. Lower	  percentage	  of	  students	  who	  receive	  pell	  grant

<!-- b000181 | prose | pages [8] -->
3. Higher	  percentage	  of	  minority	  races

<!-- b000182 | prose | pages [8] -->
4. Higher	  percentage	  of	  degree	  awarded	  in	  week	  subjects

<!-- b000183 | prose | pages [8] -->
5. Higher	  part-­‐time	  ratio

<!-- b000184 | prose | pages [8] -->
6. Higher	  debt/loan

<!-- b000185 | heading | pages [8] -->
5	   School	  Selecting

<!-- b000186 | furniture | pages [8] -->


<!-- b000187 | prose | pages [8] -->
Based	   on	   the	   data	   analysis	   and	   our	   focus	   explained	   above,	   we	   intend	   to reduce	  the	  number	  of	  candidate	  schools	  from	  2977	  to	  500	  by	  manual	  selection and	  PCA	  selection.	  The	  smaller	  number	  of	  schools	  will	  make	  the	  algorithm	  easier to	  run	  in	  the	  next	  part	  “strategy	  making”.

<!-- b000188 | heading | pages [8] -->
5.1	  Manual	  Selection

<!-- b000189 | furniture | pages [8] -->


<!-- b000190 | prose | pages [8] -->
According	   to	   the	   analysis	   and	   explanation	   above,	   we	   don’t	   invest	   on	   the schools	   in	   four	   states:	   New	   York,	   California,	   District	   of	   Columbia	   and Massachusetts.	  So	  we	  directly	  delete	  the	  schools	  in	  these	  four	  states	  from	  our candidate	  sheet.	  This	  step	  reduces	  the	  number	  from	  2977	  to	  2323.

<!-- b000191 | heading | pages [8] -->
5.2	  PCA	  Selection

<!-- b000192 | furniture | pages [8] -->


<!-- b000193 | prose | pages [8] -->
In	  this	  part,	  we	  intend	  to	  rank	  the	  schools	  based	  on	  the	  correlation	  between the	  school’s	  identities	  and	  our	  focus.	  Since	  we	  make	  use	  of	  68	  indicators	  with complex	  interactions,	  we	  ought	  to	  extract	  a	  few	  principle	  indicators	  (usually	  3	  or 4)	  from	  the	  original	  68	  ones.	  And	  give	  them	  different	  weights	  to	  computer	  the final	  score	  to	  rank	  the	  schools.

<!-- b000194 | furniture | pages [8] -->


<!-- b000195 | prose | pages [8] -->
The	   PCA	   (principle	   component	   analysis)	   is	   an	   ideal	   method	   to	   tackle	   this problem	   with	   high	   efficiency	   [2].	   PCA	   uses	   linear	   equation	   to	   combine	   the original	   indicators,	   generating	   principle	   components	   𝐹!  with	   the	   maximized variance.	   	   The	   variance	   of	   a	   component	   was	   defined	   as	   its	   amount	   of information.

<!-- b000196 | prose | pages [8] -->
5.2.1 Standardization

<!-- b000197 | furniture | pages [8] -->


<!-- b000198 | prose | pages [8] -->
Firstly,	   we	   recognize	   that	   the	   original	   data	   are	   not	   complete.	   We	   use	   the mean	   value	   to	   fill	   up	   the	   data,	   where	   𝑖	   is	   the	   number	   of	   the	   school,	   𝑗	   is	   the

<!-- b000199 | furniture | pages [9] -->
Team	  #47823

<!-- b000200 | furniture | pages [9] -->
Page	  9	  of	  27

<!-- b000201 | prose | pages [9] -->
number	   of	   the	   indicator.	   This	   treatment	   is	   reasonable	   because	   it	   doesn’t influence	  the	  result	  [3].

<!-- b000202 | prose | pages [9] -->
NULLj = 1

<!-- b000203 | furniture | pages [9] -->


<!-- b000204 | prose | pages [9] -->
n

<!-- b000205 | prose | pages [9] -->
n n ∑ ∑

<!-- b000206 | prose | pages [9] -->
xij = x j

<!-- b000207 | furniture | pages [9] -->


<!-- b000208 | prose | pages [9] -->
(1)

<!-- b000209 | prose | pages [9] -->
i=1 i=1

<!-- b000210 | prose | pages [9] -->
(i =1,2,…,n; j =1,2,…,p)

<!-- b000211 | prose | pages [9] -->
Secondly,	  we	  use	  the	  equation	  below	  to	  standardize	  the	  data:

<!-- b000212 | prose | pages [9] -->
xij −x j * =

<!-- b000213 | prose | pages [9] -->
xij

<!-- b000214 | prose | pages [9] -->
V ar(x j)

<!-- b000215 | prose | pages [9] -->
1

<!-- b000216 | furniture | pages [9] -->


<!-- b000217 | prose | pages [9] -->
Var(x j)= n−1

<!-- b000218 | heading | pages [9] -->
5.2.2	  Calculation

<!-- b000219 | prose | pages [9] -->
n∑

<!-- b000220 | furniture | pages [9] -->


<!-- b000221 | prose | pages [9] -->
(2)

<!-- b000222 | prose | pages [9] -->
(xij −x j)2

<!-- b000223 | prose | pages [9] -->
i=1

<!-- b000224 | prose | pages [9] -->
We	   use	   the	   equation	   below	   to	   compute	   the	   covariance	   matrix	   where	   𝑖, 𝑗

<!-- b000225 | furniture | pages [9] -->


<!-- b000226 | prose | pages [9] -->
both	  are	  the	  indicators	  and	   𝑥	   are	  the	  data	  after	  standardization.

<!-- b000227 | prose | pages [9] -->
rij = cov(xi ,x j)=

<!-- b000228 | furniture | pages [9] -->


<!-- b000229 | prose | pages [9] -->
∑ ∑ (xi −xi) (x j −x j)

<!-- b000230 | furniture | pages [9] -->


<!-- b000231 | prose | pages [9] -->
(3) n−1

<!-- b000232 | prose | pages [9] -->
And	  then	  we	  calculate	  the	  eigenvalue	  and	  eigenvector	  of	  the	  covariance	  matrix:

<!-- b000233 | prose | pages [9] -->
Eigenvalue:	   λi ;	  Eigenvector:	   !ai ,	   (i =1,2,…,p)

<!-- b000234 | prose | pages [9] -->
5.2.3 Principle	  Components

<!-- b000235 | prose | pages [9] -->
The	  steps	  above	  can	  generate	  68	  principle	  components	  while	  we	  can	  only

<!-- b000236 | furniture | pages [9] -->


<!-- b000237 | prose | pages [9] -->
utilize	  3	  or	  4	  of	  the	  components,	  which	  have	  the	  highest	  contribution	  rate.	  The contribution	  rate	  can	  be	  calculated	  by	  the	  equation:

<!-- b000238 | prose | pages [9] -->
λi Contribution	  rate=

<!-- b000239 | furniture | pages [9] -->


<!-- b000240 | furniture | pages [9] -->


<!-- b000241 | prose | pages [9] -->
(4)

<!-- b000242 | prose | pages [9] -->
p ∑

<!-- b000243 | prose | pages [9] -->
λi i=1

<!-- b000244 | prose | pages [9] -->
The	  sum	  of	  the	  contribution	  rate	  is	  denoted	  by	   𝑇,	  the	  cumulative	  contribution rate.	  The	  higher	  T,	  the	  more	  information	  contained	  in	  the	  principle	  components.

<!-- b000245 | prose | pages [9] -->
At	  last,	  we	  can	  sum	  the	  scores	  of	  the	  principle	  components	  and	  use	  the	  total

<!-- b000246 | furniture | pages [9] -->


<!-- b000247 | prose | pages [9] -->
score	  to	  rank	  the	  schools.

<!-- b000248 | prose | pages [9] -->
5.2.4

<!-- b000249 | heading | pages [9] -->
PCA	  Results

<!-- b000250 | prose | pages [9] -->
We	  set	  the	  cumulative	  contribution	  rate	   𝑇= 90%,	  the	  2323	  schools	  and	  68

<!-- b000251 | furniture | pages [9] -->


<!-- b000252 | furniture | pages [10] -->
Team	  #47823

<!-- b000253 | furniture | pages [10] -->
Page	  10	  of	  27

<!-- b000254 | prose | pages [10] -->
indicators	   as	   inputs.	   And	   apply	   the	   PCA	   method	   to	   compute	   the	   score	   of	   the schools,	  the	  top	  500	  schools	  will	  go	  around	  to	  next	  part.	  Here	  is	  the	  table	  of	  the top	  ten	  schools.

<!-- b000255 | prose | pages [10] -->
Rank UNITID INSTNM PCA	  Score

<!-- b000256 | prose | pages [10] -->
Widener	  University-­‐Delaware	  Campus 1 244190 32.87

<!-- b000257 | prose | pages [10] -->
Paul	  Quinn	  College 2 227429 30.15

<!-- b000258 | prose | pages [10] -->
Andrew	  College 3 138761 27.14

<!-- b000259 | prose | pages [10] -->
Huston-­‐Tillotson	  University 4 225575 25.09

<!-- b000260 | prose | pages [10] -->
Stillman	  College 5 102270 24.99

<!-- b000261 | prose | pages [10] -->
Paine	  College 6 140720 21.81

<!-- b000262 | prose | pages [10] -->
New	  River	  Community	  and	  Technical	  College 7 447582 21.58

<!-- b000263 | prose | pages [10] -->
Livingstone	  College 8 198862 21.30

<!-- b000264 | prose | pages [10] -->
Texas	  Southern	  University 9 229063 20.43

<!-- b000265 | prose | pages [10] -->
Richard	  Bland	  College	  of	  the	  College	  of	  William	  and	  Mary 10 233338 20.21

<!-- b000266 | caption | pages [10] -->
Table	  3:	  top	  ten	  candidate	  schools	  by	  PCA

<!-- b000267 | prose | pages [10] -->
In	  the	  table	  above,	  the	  school	  that	  has	  the	  highest	  PCA	  scores	  has	  the	  largest

<!-- b000268 | furniture | pages [10] -->


<!-- b000269 | prose | pages [10] -->
demand	   of	   grant	   based	   on	   our	   focus.	   Please	   notice	   that	   this	   is	   not	   the	   final recommending	   list	   of	   the	   schools,	   because	   we	   haven’t	   considered	   the	   ROI	   of these	  schools.	  After	  deriving	  the	  ROI	  function,	  we	  will	  offer	  a	  list	  based	  on	  the potential	  use	  of	  the	  investment.	  Further	  more,	  we	  will	  compare	  the	  difference between	  the	  PCA	  rank	  list	  between	  the	  final	  list	  later.

<!-- b000270 | prose | pages [10] -->
Checking	   the	   statistics	   of	   the	   top	   school	   Widener	   University-­‐Delaware

<!-- b000271 | furniture | pages [10] -->


<!-- b000272 | prose | pages [10] -->
Campus,	  we	  find	  that	  the	  students	  in	  this	  school	  are	  under	  a	  large	  amount	  of	  debt. It	   is	   the	   main	   indicator	   pushing	   the	   school	   to	   the	   top	   one.	   To	   some	   degree,	   it reflects	  that	  our	  model	  is	  reasonable	  and	  efficient	  for	  we	  pay	  attention	  to	  those schools	  whose	  students	  are	  under	  much	  debt.	  On	  another	  hand,	  our	  PCA-­‐ranking model	  has	  a	  clear,	  easy-­‐to-­‐understand	  basis	  in	  focus	  correlation	  measures	  and gives	   reasonably	   accurate	   results.	   It	   should	   be	   noted	   that	   we	   choose	   this approach	   to	   ranking	   schools	   over	   a	   much	   simpler	   approach	   such	   as	   simply summing	   the	   indicators	   for	   various	   reasons,	   one	   of	   which	   is	   that	   there	   are interactions	   between	   the	   indicators	   and	   PCA	   is	   skilled	   at	   solving	   this	   kind	   of problems.

<!-- b000273 | heading | pages [10] -->
6	   Strategy	  Making

<!-- b000274 | prose | pages [10] -->
The	   model	   we	   created	   in	   the	   sections	   above	   works	   well	   for	   selecting	   the

<!-- b000275 | furniture | pages [10] -->


<!-- b000276 | prose | pages [10] -->
target	  schools.	  In	  this	  part,	  in	  order	  to	  rank	  the	  target	  schools	  and	  determine	  the investment	  strategy,	  we	  must	  determine	  the	  return	  on	  investment	  (ROI),	  before this,	  we	  should	  derive	  a	  utility	  function	  which	  measures	  the	  contribution	  of	  the school	  to	  the	  society.	  ROI	  is	  defined	  as	  the	  difference	  between	  the	  utility	  before and	  after	  the	  investment.

<!-- b000277 | furniture | pages [11] -->
Team	  #47823

<!-- b000278 | furniture | pages [11] -->
Page	  11	  of	  27

<!-- b000279 | furniture | pages [11] -->


<!-- b000280 | prose | pages [11] -->
The	  utility	  of	  a	  school	  is	  an	  abstract	  value,	  and	  it	  has	  no	  real	  unit	  for	  it’s	  not money,	  not	  earnings	  or	  other	  things.	  And	  the	  input	  x	  is	  a	  vector,	  including	  four main	  factors,	  student	  number,	  graduated	  ratio,	  earnings	  of	  graduated	  students and	  the	  investment.	  The	  construct	  of	  x	  will	  be	  explained	  later.	  Here	  is	  the	  key assumption:	  the	  utility	   𝑈!	   and	  the	  inputs	  x	  have	  the	  relationship	  below:

<!-- b000281 | prose | pages [11] -->
Ui = log(x)

<!-- b000282 | furniture | pages [11] -->


<!-- b000283 | prose | pages [11] -->
(5)

<!-- b000284 | furniture | pages [11] -->


<!-- b000285 | prose | pages [11] -->
First	  of	  all,	  the	  utility	  function	  must	  be	  concave	  for	  two	  reasons:

<!-- b000286 | prose | pages [11] -->
1. If	  the	  function	  is	  linear	  or	  convex,	  the	  best	  strategy	  is	  to	  give	  the	  whole 100	  million	  to	  one	  school	  to	  maximize	  the	  total	  utility.

<!-- b000287 | prose | pages [11] -->
2. The	   utility	   is	   a	   state	   value.	   If	   both	   a	   high	   state	   and	   a	   low	   state	   school receive	  a	  same	  amount	  of	  investment,	  the	  low	  state	  school	  will	  generate more	   incremental	   utility.	   Because	   there	   are	   more	   opportunities	   to	   use the	  money	  and	  more	  things	  to	  be	  improved	  in	  the	  low	  state	  one.

<!-- b000288 | furniture | pages [11] -->


<!-- b000289 | prose | pages [11] -->
Secondly,	   motivated	   by	   the	   utility	   function	   in	   microeconomics,	   we	   use	   the “log”	   relationship	   to	   determine	   the	   utility	   function.	   Although	   the	   relationship may	  be	  more	  complex	  in	  real	  life,	  it	  gives	  us	  reasonable	  ROI	  function	  below	  and works	  well	  with	  our	  model.

<!-- b000290 | heading | pages [11] -->
6.1	  The	  ROI	  Function

<!-- b000291 | furniture | pages [11] -->


<!-- b000292 | prose | pages [11] -->
Here	  we	  come	  to	  the	  ROI	  function,	  the	  function	  describes	  the	  relationship between	  investment	  and	  incremental	  utility.	  Once	  the	  ROI	  function	  is	  decided, we	  can	  make	  the	  investment	  strategy	  to	  maximize	  the	  total	  ROI.

<!-- b000293 | furniture | pages [11] -->


<!-- b000294 | prose | pages [11] -->
Naturally,	  the	  ROI	  function	  is	  the	  difference	  of	  the	  utility	  function:

<!-- b000295 | prose | pages [11] -->
ROIi = ΔUi = log(x0 + Δxi)−log(x0)

<!-- b000296 | furniture | pages [11] -->


<!-- b000297 | prose | pages [11] -->
(6)

<!-- b000298 | furniture | pages [11] -->


<!-- b000299 | prose | pages [11] -->
We	  can	  plot	  a	  figure	  to	  describe	  the	  relationship:

<!-- b000300 | caption | pages [11] -->
Figure	  3:	  the	  relationship	  between	  incremental	  utility	  and	  investment

<!-- b000301 | furniture | pages [12] -->
Team	  #47823

<!-- b000302 | furniture | pages [12] -->
Page	  12	  of	  27

<!-- b000303 | prose | pages [12] -->
In	  Figure	  3	  and	  equation	  (6),	   ∆𝑥!	   is	  the	  incremental	  amount	  of	  the	  inputs

<!-- b000304 | furniture | pages [12] -->


<!-- b000305 | prose | pages [12] -->
triggered	   by	   the	   investment.	   In	   the	   following	   steps,	   we	   will	   derive	   an	   explicit equation	  of	  x.

<!-- b000306 | prose | pages [12] -->
Firstly,	  we	  consider	  the	  number	  of	  the	  students	  N,	  median	  of	  earnings	  after

<!-- b000307 | furniture | pages [12] -->


<!-- b000308 | prose | pages [12] -->
10	  years	  M	  and	  the	  ratio	  of	  students	  who	  earn	  more	  than	  25k	  per	  year	  after	  6 years	  m.	  We	  multiply	  them	  together	  to	  measure	  the	  total	  earnings	  [4]:	   m⋅M ⋅N . The	  earnings	  measure	  one	  aspect	  of	  the	  utility,	  the	  higher	  it	  is,	  the	  higher	  the state	  of	  school	  will	  be.

<!-- b000309 | prose | pages [12] -->
Secondly,	  we	  take	  a	  deep	  look	  at	  the	  graduation	  rate	  g	  (same	  for	  two	  year

<!-- b000310 | furniture | pages [12] -->


<!-- b000311 | prose | pages [12] -->
school	  or	  four	  year	  school).	  This	  indicator	  measures	  another	  aspect	  of	  the	  utility. It	  also	  has	  a	  positive	  relationship	  between	  the	  utility.	  We	  intend	  to	  combine	  the two	  aspects	  together	  but	  the	  units	  are	  not	  equal.	  Then,	  we	  define	  a	  constant	  k	  to balance	   the	   unit.	   As	   a	   result,	   the	   utility	   function	   can	   be	   written	   as	   the	   form below:

<!-- b000312 | prose | pages [12] -->
U0 = log(m⋅M ⋅N + k ⋅g)

<!-- b000313 | furniture | pages [12] -->


<!-- b000314 | prose | pages [12] -->
(7)

<!-- b000315 | prose | pages [12] -->
Here	   all	   the	   variables	   are	   different	   for	   each	   school,	   for	   simplicity,	   we

<!-- b000316 | furniture | pages [12] -->


<!-- b000317 | prose | pages [12] -->
eliminate	  the	  subscript	  i.

<!-- b000318 | prose | pages [12] -->
Take	  the	  investment	  into	  consideration,	  the	  utility	  will	  be:

<!-- b000319 | furniture | pages [12] -->


<!-- b000320 | prose | pages [12] -->
j−1 ∑ + x j + m⋅M ⋅N + k ⋅g)

<!-- b000321 | prose | pages [12] -->
U j = log(

<!-- b000322 | furniture | pages [12] -->


<!-- b000323 | prose | pages [12] -->
xp p=0

<!-- b000324 | prose | pages [12] -->
(8)

<!-- b000325 | prose | pages [12] -->
where	   j	   represents	   the	   time	   period,	   j = 1,2,3,4,5	   and	   x0 = 0 .	   x0 is	   the	   initial

<!-- b000326 | prose | pages [12] -->
investment	   the	   school	   received	   from	   other	   foundations	   or	   the	   government.	   In this	  problem,	  we	  simply	  assume	   x0 = 0 	   because	  of	  the	  limited	  data.

<!-- b000327 | prose | pages [12] -->
At	  last,	  we	  can	  write	  down	  the	  ROI	  function:

<!-- b000328 | furniture | pages [12] -->


<!-- b000329 | prose | pages [12] -->
⎧

<!-- b000330 | prose | pages [12] -->
log(x j +m⋅M⋅N +k⋅g)−log(m⋅M⋅N +k⋅g)! j =1

<!-- b000331 | prose | pages [12] -->
⎪

<!-- b000332 | furniture | pages [12] -->


<!-- b000333 | prose | pages [12] -->
ROI =

<!-- b000334 | prose | pages [12] -->
⎨

<!-- b000335 | prose | pages [12] -->
j−1 ∑

<!-- b000336 | prose | pages [12] -->
(9)

<!-- b000337 | prose | pages [12] -->
j−2 ∑

<!-- b000338 | prose | pages [12] -->
+ x j +m⋅M⋅N +k⋅g)−log(

<!-- b000339 | prose | pages [12] -->
log( xp

<!-- b000340 | prose | pages [12] -->
⎪ ⎩

<!-- b000341 | prose | pages [12] -->
p=0

<!-- b000342 | prose | pages [12] -->
+ x j−1 +m⋅M⋅N +k⋅g)! j = 2,3,4,5

<!-- b000343 | prose | pages [12] -->
xp p=0

<!-- b000344 | prose | pages [12] -->
The	   ROI	   function	   above	   is	   dynamic	   with	   respect	   to	   time	   period.	   In	   other

<!-- b000345 | furniture | pages [12] -->


<!-- b000346 | prose | pages [12] -->
words,	  when	  time	  changes,	  the	  ROI	  function	  changes	  in	  response.	  To	  be	  more specific,	  once	  we	  invest	  in	  a	  school,	  the	  ROI	  in	  the	  next	  period	  will	  decrease.	  The larger	  amount	  of	  investment	  there	  is,	  the	  lower	  the	  ROI	  will	  be.	  This	  character	  of our	  ROI	  function	  describes	  the	  real	  situation	  precisely,	  which	  makes	  model	  close to	  the	  reality.

<!-- b000347 | heading | pages [12] -->
6.2	  Optimizing	  the	  Total	  ROI

<!-- b000348 | prose | pages [12] -->
We	  now	  assign	  100	  million	  dollars	  to	  50	  target	  schools	  to	  maximize	  the	  total

<!-- b000349 | furniture | pages [12] -->


<!-- b000350 | furniture | pages [13] -->
Team	  #47823

<!-- b000351 | furniture | pages [13] -->
Page	  13	  of	  27

<!-- b000352 | prose | pages [13] -->
ROI.	  Each	  school’s	  ROI	  is	  defined	  in	  Equation	  (9).	  We	  use	  the	  equations	  below	  to simplify	  the	  form	  of	  our	  ROI	  function:

<!-- b000353 | prose | pages [13] -->
j−1 ∑ + m⋅M ⋅N + k ⋅g!! j ≥1

<!-- b000354 | prose | pages [13] -->
c j = xp

<!-- b000355 | furniture | pages [13] -->


<!-- b000356 | prose | pages [13] -->
p=0

<!-- b000357 | furniture | pages [13] -->


<!-- b000358 | prose | pages [13] -->
(10)

<!-- b000359 | prose | pages [13] -->
co = m⋅M ⋅N + k ⋅g!!!!! j = 0

<!-- b000360 | furniture | pages [13] -->


<!-- b000361 | prose | pages [13] -->
The	  utility	  function	  will	  be:

<!-- b000362 | prose | pages [13] -->
⎧

<!-- b000363 | prose | pages [13] -->
log(x j +c j)!!!!!!! j ≥1

<!-- b000364 | prose | pages [13] -->
⎨⎪

<!-- b000365 | prose | pages [13] -->
U j =

<!-- b000366 | furniture | pages [13] -->


<!-- b000367 | furniture | pages [13] -->


<!-- b000368 | prose | pages [13] -->
(11)

<!-- b000369 | prose | pages [13] -->
logc0!!!!!!!!! j = 0

<!-- b000370 | prose | pages [13] -->
⎩⎪

<!-- b000371 | furniture | pages [13] -->


<!-- b000372 | prose | pages [13] -->
The	  ROI	  function	  will	  be:

<!-- b000373 | prose | pages [13] -->
ROI= ΔU j =U j −U j−1

<!-- b000374 | furniture | pages [13] -->


<!-- b000375 | prose | pages [13] -->
(12)

<!-- b000376 | prose | pages [13] -->
We	  want	  to	  maximize	  the	  total	  ROI,	  the	  function	  can	  be:

<!-- b000377 | furniture | pages [13] -->


<!-- b000378 | prose | pages [13] -->
i∑ j∑ ΔUij

<!-- b000379 | prose | pages [13] -->
i∑ + (Ui2 −Ui1) + (Ui3 −Ui2) + (Ui4 −Ui3) + (Ui5 −Ui4)]

<!-- b000380 | prose | pages [13] -->
= [(Ui1 −Ui0)

<!-- b000381 | furniture | pages [13] -->


<!-- b000382 | prose | pages [13] -->
i∑

<!-- b000383 | prose | pages [13] -->
= (Ui5 −Ui0)

<!-- b000384 | prose | pages [13] -->
i∑ i∑

<!-- b000385 | prose | pages [13] -->
= Ui5 −

<!-- b000386 | prose | pages [13] -->
Ui0

<!-- b000387 | furniture | pages [13] -->


<!-- b000388 | prose | pages [13] -->
(13)

<!-- b000389 | prose | pages [13] -->
The	  result	  is	  really	  exciting!	  It	  is	  noted	  that	  the	  ROI	  of	  one	  school	  in	  different

<!-- b000390 | furniture | pages [13] -->


<!-- b000391 | prose | pages [13] -->
i∑ time	  period	  cancels	  out	  with	  each	  other.	  As

<!-- b000392 | prose | pages [13] -->
be	  in	  this	  form:

<!-- b000393 | prose | pages [13] -->
i∑

<!-- b000394 | prose | pages [13] -->
i∑

<!-- b000395 | prose | pages [13] -->
is	  constant,	  the	  problem	  will Ui0

<!-- b000396 | prose | pages [13] -->
log(xi1 + xi2 + xi3 + xi4 + xi5 + ci0) = max Ui5

<!-- b000397 | prose | pages [13] -->
⎧

<!-- b000398 | prose | pages [13] -->
i∑ = 1×108 xi1

<!-- b000399 | prose | pages [13] -->
⎪ ⎪ ⎪

<!-- b000400 | furniture | pages [13] -->


<!-- b000401 | prose | pages [13] -->
i∑ = 1×108 xi2

<!-- b000402 | prose | pages [13] -->
⎪ ⎪ ⎪

<!-- b000403 | prose | pages [13] -->
i∑ = 1×108 xi3

<!-- b000404 | prose | pages [13] -->
⎪

<!-- b000405 | furniture | pages [13] -->


<!-- b000406 | prose | pages [13] -->
(14)

<!-- b000407 | prose | pages [13] -->
i = 1,2,!,50; j = 1,2,!,5

<!-- b000408 | prose | pages [13] -->
s.t.

<!-- b000409 | prose | pages [13] -->
⎨

<!-- b000410 | prose | pages [13] -->
⎪

<!-- b000411 | prose | pages [13] -->
i∑

<!-- b000412 | prose | pages [13] -->
⎪

<!-- b000413 | prose | pages [13] -->
= 1×108 xi4

<!-- b000414 | prose | pages [13] -->
⎪ ⎪

<!-- b000415 | prose | pages [13] -->
i∑

<!-- b000416 | prose | pages [13] -->
⎪

<!-- b000417 | prose | pages [13] -->
= 1×108 xi5

<!-- b000418 | prose | pages [13] -->
⎪ ⎪

<!-- b000419 | prose | pages [13] -->
xij ≥0

<!-- b000420 | prose | pages [13] -->
⎩

<!-- b000421 | furniture | pages [14] -->
Team	  #47823

<!-- b000422 | furniture | pages [14] -->
Page	  14	  of	  27

<!-- b000423 | prose | pages [14] -->
The	   equations	   (14)	   are	   the	   final	   form	   of	   our	   model.	   Up	   to	   know,	   we	   have

<!-- b000424 | furniture | pages [14] -->


<!-- b000425 | prose | pages [14] -->
already	  derived	  a	  mathematical	  problem	  of	  the	  real	  situation.	  Now,	  we	  attempt to	  choose	  the	  best	  method	  to	  solve	  the	  optimization	  problem.

<!-- b000426 | prose | pages [14] -->
Karush-­‐Kuhn-­‐Tucker	  Conditions 6.2.1

<!-- b000427 | prose | pages [14] -->
At	   first,	   we	   set	   out	   to	   implement	   KKT	   conditions	   to	   solve	   the	   optimization problem	  [5].	  For	  the	  problem	  below:

<!-- b000428 | prose | pages [14] -->
min f0(x)

<!-- b000429 | prose | pages [14] -->
fi(x) ≤0,i = 1,2,!!m

<!-- b000430 | furniture | pages [14] -->


<!-- b000431 | furniture | pages [14] -->


<!-- b000432 | prose | pages [14] -->
(15)

<!-- b000433 | prose | pages [14] -->
hi(x) = 0,i = 1,2,!! p

<!-- b000434 | prose | pages [14] -->
the	  KKT	  conditions	  are	  presented	  as	  follows:

<!-- b000435 | prose | pages [14] -->
⎧

<!-- b000436 | prose | pages [14] -->
m

<!-- b000437 | prose | pages [14] -->
∗ λi

<!-- b000438 | prose | pages [14] -->
∑

<!-- b000439 | prose | pages [14] -->
⎪

<!-- b000440 | prose | pages [14] -->
p

<!-- b000441 | prose | pages [14] -->
∗ νi

<!-- b000442 | prose | pages [14] -->
∑

<!-- b000443 | prose | pages [14] -->
∇fi(x∗)+

<!-- b000444 | prose | pages [14] -->
∇f0(x∗)+

<!-- b000445 | prose | pages [14] -->
⎪

<!-- b000446 | prose | pages [14] -->
i=1

<!-- b000447 | prose | pages [14] -->
⎪

<!-- b000448 | prose | pages [14] -->
fi(x∗)≤0

<!-- b000449 | prose | pages [14] -->
⎪⎪

<!-- b000450 | prose | pages [14] -->
hi(x∗)= 0

<!-- b000451 | furniture | pages [14] -->


<!-- b000452 | prose | pages [14] -->
⎨

<!-- b000453 | prose | pages [14] -->
⎪

<!-- b000454 | prose | pages [14] -->
∗ λi ≥0

<!-- b000455 | prose | pages [14] -->
⎪ ⎪ ⎪

<!-- b000456 | prose | pages [14] -->
∗ λi fi(x∗)= 0

<!-- b000457 | prose | pages [14] -->
⎪

<!-- b000458 | prose | pages [14] -->
⎩

<!-- b000459 | prose | pages [14] -->
∇hi(x∗)= 0

<!-- b000460 | prose | pages [14] -->
i=1

<!-- b000461 | furniture | pages [14] -->


<!-- b000462 | prose | pages [14] -->
(16)

<!-- b000463 | prose | pages [14] -->
where	   λi is	  Lagrange	  multiplier	  associated	  with	   fi(x) ≤0;

<!-- b000464 | prose | pages [14] -->
νi is	  Lagrange	  multiplier	  associated	  with hi(x) = 0 .

<!-- b000465 | prose | pages [14] -->
For	  our	  problem,	  we	  can	  easily	  transform	  the	  formulation	  into	  the	  standard

<!-- b000466 | furniture | pages [14] -->


<!-- b000467 | prose | pages [14] -->
form,	  and	  the	  corresponding	  KKT	  conditions	  are:

<!-- b000468 | prose | pages [14] -->
⎧

<!-- b000469 | prose | pages [14] -->
1 ∀i,

<!-- b000470 | prose | pages [14] -->
⎪

<!-- b000471 | prose | pages [14] -->
∗

<!-- b000472 | prose | pages [14] -->
∗

<!-- b000473 | prose | pages [14] -->
∗

<!-- b000474 | prose | pages [14] -->
p

<!-- b000475 | prose | pages [14] -->
m

<!-- b000476 | prose | pages [14] -->
∗

<!-- b000477 | prose | pages [14] -->
∗

<!-- b000478 | prose | pages [14] -->
λi +

<!-- b000479 | prose | pages [14] -->
νi = 0

<!-- b000480 | prose | pages [14] -->
∑

<!-- b000481 | prose | pages [14] -->
∑

<!-- b000482 | prose | pages [14] -->
−

<!-- b000483 | prose | pages [14] -->
∗ ∗

<!-- b000484 | prose | pages [14] -->
∗

<!-- b000485 | prose | pages [14] -->
xi4 +

<!-- b000486 | prose | pages [14] -->
xi1 +

<!-- b000487 | prose | pages [14] -->
xi2 +

<!-- b000488 | prose | pages [14] -->
xi3 +

<!-- b000489 | prose | pages [14] -->
⎪ ⎪ ⎪

<!-- b000490 | prose | pages [14] -->
xij ≥0

<!-- b000491 | prose | pages [14] -->
⎪⎪

<!-- b000492 | prose | pages [14] -->
ij∑

<!-- b000493 | prose | pages [14] -->
xij =1×108, j =1,2,3,4,5

<!-- b000494 | furniture | pages [14] -->


<!-- b000495 | prose | pages [14] -->
⎨

<!-- b000496 | prose | pages [14] -->
⎪ ⎪

<!-- b000497 | prose | pages [14] -->
∗ λi ≥0

<!-- b000498 | prose | pages [14] -->
⎪ ⎪

<!-- b000499 | prose | pages [14] -->
∗

<!-- b000500 | prose | pages [14] -->
⎪

<!-- b000501 | prose | pages [14] -->
λi fi(x∗)= 0

<!-- b000502 | prose | pages [14] -->
⎪

<!-- b000503 | prose | pages [14] -->
⎩

<!-- b000504 | prose | pages [14] -->
xi5

<!-- b000505 | prose | pages [14] -->
i=1

<!-- b000506 | prose | pages [14] -->
i=1

<!-- b000507 | furniture | pages [14] -->


<!-- b000508 | prose | pages [14] -->
(17)

<!-- b000509 | furniture | pages [15] -->
Team	  #47823

<!-- b000510 | furniture | pages [15] -->
Page	  15	  of	  27

<!-- b000511 | furniture | pages [15] -->


<!-- b000512 | caption | pages [15] -->
Figure	  4:	  flow	  chart	  of	  the	  LA_PSA_GT	  algorithm

<!-- b000513 | prose | pages [15] -->
𝑓𝑔𝑏𝑒𝑠𝑡	   is	  the	  maximum	  of	  the	  total	  ROI	  function

<!-- b000514 | prose | pages [15] -->
𝑔𝑏𝑒𝑠𝑡	   is	  vector	  of	  investment	  amount	  per	  year

<!-- b000515 | furniture | pages [16] -->
Team	  #47823

<!-- b000516 | furniture | pages [16] -->
Page	  16	  of	  27

<!-- b000517 | prose | pages [16] -->
The	  KKT	  conditions	  ensures	  the	  existence	  of	  the	  solutions.	  Solving	  the	  equations above,	  we	  will	  absolutely	  get	  the	  optimized	  strategy.	  However,	  the	  equations	  are extremely	  difficult	  since	  there	  are	  250	  variables.	  In	  general,	  the	  KKT	  method	  is highly	   efficient	   dealing	   with	   small	   number	   of	   variables.	   So,	   as	   a	   result,	   the number	  of	  the	  variable	  is	  too	  big	  for	  us	  to	  solve	  the	  equation	  when	  it	  comes	  to our	  problem.	  In	  other	  words,	  we	  are	  not	  able	  to	  create	  a	  program	  to	  solve	  the equations.	  Consequently,	  we	  have	  to	  give	  up	  and	  search	  for	  other	  algorithms.

<!-- b000518 | prose | pages [16] -->
6.2.2

<!-- b000519 | heading | pages [16] -->
PSO	  Algorithm

<!-- b000520 | furniture | pages [16] -->


<!-- b000521 | prose | pages [16] -->
The	  PSO	  (particle	  swarm	  optimization)	  is	  an	  efficient	  method,	  imitating	  the flying	  path	  of	  a	  bird	  swarm.	  PSO	  algorithm	  uses	  three	  flying	  principles,	  collision avoidance,	  velocity	  matching	  and	  flock	  centering	  to	  search	  the	  extrema	  within the	   boundary	   conditions.	   The	   algorithm	   starts	   with	   a	   randomly	   initialized investment	  vectors	  and	  iterate	  them	  until	  reaching	  the	  maximum	  point	  [6].	  We create	  a	  program	  based	  on	  the	  PSO,	  but	  the	  algorithm	  takes	  a	  very	  long	  time	  to converge	  and	  does	  not	  produce	  the	  optimal	  values.	  Therefore,	  we	  decide	  to	  use another	  method	  to	  improve	  the	  performance.

<!-- b000522 | prose | pages [16] -->
6.2.3

<!-- b000523 | heading | pages [16] -->
Improved	   PSO	   algorithm	   based	   on	   augmented	   Lagrange	   function

<!-- b000524 | prose | pages [16] -->
(LA_PSO_GT)

<!-- b000525 | furniture | pages [16] -->


<!-- b000526 | prose | pages [16] -->
We	  search	  for	  other	  literary	  researches	  and	  decide	  to	  use	  the	  method	  above. The	   algorithms	   utilize	   the	   augmented	   Lagrange	   function	   to	   change	   the optimization	  problem	  into	  boundary	  constraint	  optimization	  problem.	  After	  that, the	   LA_PSO_GT	   combines	   Conjugate	   Gradient	   method	   and	   PSO	   algorithm together,	  which	  overcome	  the	  defect	  of	  the	  length	  of	  the	  convergence	  time	  and improves	  the	  computing	  efficiency	  [7].	  The	  whole	  procedures	  will	  be	  attached	  in the	  appendix.	  Above	  is	  the	  flow	  chart	  of	  this	  algorithm.

<!-- b000527 | heading | pages [16] -->
7	   Result

<!-- b000528 | furniture | pages [16] -->


<!-- b000529 | prose | pages [16] -->
After	  running	  the	  program,	  we	  get	  the	  amount	  of	  investment	  for	  each	  target school	  in	  each	  year	  and	  the	  ROI	  in	  five	  years.

<!-- b000530 | furniture | pages [16] -->


<!-- b000531 | prose | pages [16] -->
The	  fitness	  figure	  of	  the	  algorithm	  is	  presented	  below:

<!-- b000532 | furniture | pages [16] -->


<!-- b000533 | prose | pages [16] -->
From	  the	  fitness	  figure	  below,	  we	  can	  see	  that	  the	  algorithm	  converges	  after 50	  iterations.	  It	  proves	  that	  our	  method	  is	  efficient	  and	  powerful.

<!-- b000534 | furniture | pages [17] -->
Team	  #47823

<!-- b000535 | furniture | pages [17] -->
Page	  17	  of	  27

<!-- b000536 | caption | pages [17] -->
Figure	  5:	  fitness	  of	  the	  algorithm

<!-- b000537 | prose | pages [17] -->
For	   some	   schools,	   the	   investment	   is	   too	   small.	   For	   example,	   if	   only	   1000

<!-- b000538 | furniture | pages [17] -->


<!-- b000539 | prose | pages [17] -->
dollars	  is	  invested	  in	  a	  school	  in	  a	  year,	  it	  is	  obviously	  useless	  in	  real	  situation. Therefore,	  we	  eliminate	  the	  value	  and	  set	  it	  as	  zero.	  Although	  we	  don’t	  use	  the whole	  100	  million,	  but	  the	  utilization	  rates	  are	  all	  above	  99%.

<!-- b000540 | heading | pages [17] -->
7.1	  Optimal	  Investment	  Strategy	  and	  Recommending	  List

<!-- b000541 | prose | pages [17] -->
Here	  is	  a	  table	  of	  top	  ten	  schools	  in	  the	  recommending	  list	  ranked	  by	  total

<!-- b000542 | furniture | pages [17] -->


<!-- b000543 | prose | pages [17] -->
ROI	   in	   five	   years,	   including	   the	   investment	   amount	   each	   year	   and	   the	   time duration.	  The	  full	  table	  of	  all	  target	  schools	  will	  be	  attached	  in	  appendix.

<!-- b000544 | prose | pages [17] -->
Rank INSTNM

<!-- b000545 | prose | pages [17] -->
1 MacCormac	  College

<!-- b000546 | prose | pages [17] -->
2 Paul	  Quinn	  College

<!-- b000547 | prose | pages [17] -->
3 Andrew	  College

<!-- b000548 | prose | pages [17] -->
4 Bidwell	  Training	  Center	  Inc

<!-- b000549 | prose | pages [17] -->
5 Colorado	  Heights	  University

<!-- b000550 | prose | pages [17] -->
6 Tougaloo	  College

<!-- b000551 | prose | pages [17] -->
7 Brevard	  College

<!-- b000552 | prose | pages [17] -->
8 Paine	  College

<!-- b000553 | prose | pages [17] -->
9 Fisk	  University

<!-- b000554 | prose | pages [17] -->
10 Southeast	  Missouri	  Hospital	  College	  of

<!-- b000555 | prose | pages [17] -->
Nursing	  and	  Health	  Sciences

<!-- b000556 | prose | pages [17] -->
… …

<!-- b000557 | furniture | pages [17] -->


<!-- b000558 | prose | pages [17] -->
Utilization	  rate	  of	  funds	  in	  each	  year(%)

<!-- b000559 | prose | pages [17] -->
ROI t 1 2 3 4 5

<!-- b000560 | prose | pages [17] -->
2.22 4 13.62 0.17 0.00 5.69 4.78

<!-- b000561 | prose | pages [17] -->
2.02 5 7.84 1.02 3.09 2.92 5.10

<!-- b000562 | prose | pages [17] -->
1.81 3 0.00 0.00 0.33 5.11 7.94

<!-- b000563 | prose | pages [17] -->
1.80 4 0.18 0.00 7.18 0.66 0.75

<!-- b000564 | prose | pages [17] -->
1.64 3 8.24 0.46 11.32 0.00 0.00

<!-- b000565 | prose | pages [17] -->
1.12 5 12.01 0.31 0.44 5.62 2.29

<!-- b000566 | prose | pages [17] -->
1.05 4 5.46 0.00 9.13 0.22 1.85

<!-- b000567 | prose | pages [17] -->
0.98 4 0.00 0.98 3.48 6.12 0.43

<!-- b000568 | prose | pages [17] -->
0.90 5 8.84 1.49 0.70 0.71 0.14

<!-- b000569 | prose | pages [17] -->
0.84 4 2.38 1.32 0.00 5.59 3.80

<!-- b000570 | prose | pages [17] -->
… … … … … … …

<!-- b000571 | furniture | pages [17] -->


<!-- b000572 | furniture | pages [17] -->


<!-- b000573 | prose | pages [17] -->
99.60 99.79 99.63 99.71 99.69

<!-- b000574 | caption | pages [17] -->
Table	  4:	  the	  top	  ten	  schools	  and	  their	  investment	  amount	  in	  our	  recommending	  list

<!-- b000575 | prose | pages [17] -->
(unit:million)[8] As	   we	   can	   see	   in	   the	   recommending	   list,	   two	   of	   the	   schools,	   Paul	   Quinn

<!-- b000576 | furniture | pages [17] -->


<!-- b000577 | furniture | pages [18] -->
Team	  #47823

<!-- b000578 | furniture | pages [18] -->
Page	  18	  of	  27

<!-- b000579 | prose | pages [18] -->
College	  and	  Andrew	  College	  are	  also	  the	  top	  ten	  schools	  in	  the	  PCA	  result.	  Note that	   we	   use	   different	   data	   to	   rank	   the	   schools,	   it	   proves	   that	   the	   data	   has correlation.	   What’s	   more,	   it	   shows	   that	   two	   results	   are	   consistent	   with	   each other.	  The	  target	  schools	  are	  those	  with	  high	  ROI	  and	  worth	  investmemt.

<!-- b000580 | heading | pages [18] -->
8	   Testing	  our	  Model

<!-- b000581 | prose | pages [18] -->
To	  test	  our	  model	  whether	  it	  duplicates	  the	  investment	  and	  focus	  of	  Gates

<!-- b000582 | furniture | pages [18] -->


<!-- b000583 | prose | pages [18] -->
Foundation	   or	   not,	   we	   collect	   data	   of	   the	   investment	   distribution	   of	   the	   two foundations,	  and	  compare	  them	  to	  our	  recommending	  list.

<!-- b000584 | prose | pages [18] -->
Rank INSTNM 1 Harvard	  University 2 University	  of	  Washington 3 Seattle	  University 4 Yale	  University 5 Texas	  Tech	  University 6 University	  of	  Michigan 7 Land-­‐Grant	  Universities 8 University	  of	  Kentucky 9 Columbia	  University 10 Stanford	  University Investment	  amount	  (million) 24.14 16.42 15.80 7.50 6.96 6.85 4.95 4.50 3.78 3.25

<!-- b000585 | caption | pages [18] -->
Table	  5:	  the	  top	  ten	  schools	  ranked	  by	  Gates	  Foundation’s	  investment	  amount

<!-- b000586 | prose | pages [18] -->
In	   the	   table	   above,	   we	   can	   see	   that	   Gates	   Foundation	   invested	   mostly	   on

<!-- b000587 | furniture | pages [18] -->


<!-- b000588 | prose | pages [18] -->
those	   well-­‐known	   schools	   like	   Harvard	   and	   Yale.	   But	   none	   of	   these	   schools appear	  in	  our	  recommending	  list.	  It	  proves	  that	  our	  model	  efficiently	  eliminate other	  foundations’	  investment	  and	  focus.

<!-- b000589 | heading | pages [18] -->
8.1	  Sensitivity	  Analysis

<!-- b000590 | prose | pages [18] -->
In	   the	   process	   of	   determining	   the	   ROI	   function,	   we	   create	   a	   constant	   k	   to

<!-- b000591 | furniture | pages [18] -->


<!-- b000592 | prose | pages [18] -->
make	   the	   unit	   equal	   while	   this	   parameter	   lacks	   database.	   We	   use	   the	   ratio	   of mean	  earnings	  and	  mean	  graduation	  rate	  to	  determine	  the	  value	  of	  k.	  To	  some degree,	  k	  is	  the	  marginal	  rate	  of	  substitution	  between	  the	  two	  factors.	  How	  does the	  change	  of	  k	  influence	  our	  outputs?	  We	  analyze	  the	  standard	  deviation	  of	  the invest	  mount	  caused	  by	  a	  slightly	  change	  of	  k.

<!-- b000593 | prose | pages [18] -->
𝒌−𝟓% Year 𝒌−𝟏𝟎% 𝒌+ 𝟓% 𝒌+ 𝟏𝟎% 5.33% 1 12.18% 4.52% 9.51% 4.25% 2 9.09% 5.64% 11.88% 6.37% 3 10.88% 5.63% 13.28% 3.29% 4 7.64% 3.27% 13.33%

<!-- b000594 | furniture | pages [19] -->
Team	  #47823

<!-- b000595 | furniture | pages [19] -->
Page	  19	  of	  27

<!-- b000596 | prose | pages [19] -->
5 12.67% 4.90% 4.94% 7.41% Mean	  value 10.49% 4.83% 4.80% 11.08%

<!-- b000597 | caption | pages [19] -->
Table	  6:	  the	  standard	  deviation	  of	  the	  investment	  amount	  correspond	  to	  the	  change	  of	  MRS	  k

<!-- b000598 | prose | pages [19] -->
From	  the	  table	  above,	  we	  can	  see	  that	  the	  influence	  of	  k	  is	  not	  very	  large,	  and within	  the	  range	  we	  can	  bear.

<!-- b000599 | heading | pages [19] -->
8.2	  Strengths

<!-- b000600 | heading | pages [19] -->
1. Data	   classification.	   When	   faced	   with	   big	   data	   problems,	   the	   pattern

<!-- b000601 | prose | pages [19] -->
classification	   is	   extremely	   useful	   and	   important.	   Based	   on	   this	   insight, our	  model	  firstly	  implements	  a	  data	  classification,	  separating	  the	  data	  for two	  major	  purposes,	  one	  for	  selection,	  another	  for	  determining	  the	  ROI function.	  By	  this	  means,	  we	  make	  the	  most	  use	  of	  the	  data	  attached.

<!-- b000602 | heading | pages [19] -->
2. Data	  extraction.	  Our	  model	  utilizes	  the	  PCA	  method	  to	  select	  the	  target

<!-- b000603 | prose | pages [19] -->
schools	  based	  on	  the	  focus	  of	  our	  foundation.	  The	  data	  selection	  is	  also	  an important	  part	  in	  big	  data	  problem,	  which	  will	  improve	  the	  efficiency	  for further	  data	  processing.

<!-- b000604 | heading | pages [19] -->
3. Reasonable	   ROI	   function.	   Another	   strength	   of	   our	   model	   is	   that	   we

<!-- b000605 | prose | pages [19] -->
create	   an	   ROI	   function	   by	   analyzing	   the	   relationship	   between	   earnings and	  graduation	  rate.	  Furthermore,	  our	  function	  can	  easily	  be	  modified	  if other	  researches	  find	  the	  accurate	  relationship.

<!-- b000606 | heading | pages [19] -->
4. Suitable	  algorithm.	  In	  the	  third	  part,	  we	  derive	  a	  mathematical	  problem

<!-- b000607 | prose | pages [19] -->
to	   describe	   the	   strategy	   in	   a	   general	   form.	   In	   order	   to	   solve	   the	   math problem,	  we	  have	  tried	  several	  algorithms	  and	  finally	  decide	  to	  choose the	  most	  suitable	  one.

<!-- b000608 | heading | pages [19] -->
8.3	  Weaknesses

<!-- b000609 | heading | pages [19] -->
1. Data	  vacancy.	  There	  are	  too	  many	  vacancies	  (NULL)	  in	  the	  data	  attached.

<!-- b000610 | prose | pages [19] -->
And	  we	  fill	  in	  the	  blanks	  with	  the	  mean	  value	  of	  this	  column,	  which	  is	  a main	  source	  of	  errors.

<!-- b000611 | heading | pages [19] -->
2. Parameter	  without	  database.	  When	  determining	  the	  ROI	  function,	  we

<!-- b000612 | prose | pages [19] -->
create	  a	  constant	  k	  to	  balance	  the	  unit,	  where	  k	  is	  the	  marginal	  rate	  of substitution.	  The	  value	  k	  will	  influence	  our	  outputs	  to	  some	  degree.	  So we	  made	  a	  sensitivity	  analysis	  to	  study	  the	  influence	  of	  k.

<!-- b000613 | heading | pages [19] -->
3. Algorithm	  limitations.	  Although	  the	  PSO	  algorithm	  is	  a	  suitable	  method

<!-- b000614 | prose | pages [19] -->
to	   compute	   our	   model,	   it	   has	   several	   limitations.	   The	   local	   search capacity	  of	  PSO	  is	  not	  very	  well,	  so	  the	  accuracy	  of	  outputs	  is	  limited.	  On the	   other	   hand,	   the	   algorithms	   may	   converge	   too	   early	   before	   the particles	  find	  the	  global	  optimization	  points.	  Although	  the	  particles	  are

<!-- b000615 | furniture | pages [20] -->
Team	  #47823

<!-- b000616 | furniture | pages [20] -->
Page	  20	  of	  27

<!-- b000617 | prose | pages [20] -->
near	  the	  final	  positions,	  they	  lack	  the	  capacity	  to	  jump	  out	  of	  the	  situation because	  of	  the	  low	  velocity.

<!-- b000618 | heading | pages [20] -->
9	   Conclusion

<!-- b000619 | furniture | pages [20] -->


<!-- b000620 | prose | pages [20] -->
We	  have	  been	  asked	  by	  the	  Goodgrant	  Foundation	  to	  determine	  the	  optimal investment	  strategy	  base	  on	  the	  potential	  and	  ROI	  of	  the	  candidate	  schools.	  Since it	  is	  a	  big	  data	  problem,	  we	  use	  data	  classification,	  data	  selection	  as	  pretreatment, after	  which	  we	  decide	  the	  investment	  focus	  of	  the	  foundation	  and	  the	  ROI	  of	  the schools.	  Finally,	  we	  make	  the	  optimal	  strategy	  by	  PSO	  algorithm.

<!-- b000621 | furniture | pages [20] -->


<!-- b000622 | prose | pages [20] -->
We	  deeply	  analyze	  the	  types,	  meanings,	  and	  interactions	  of	  the	  data.	  Then, by	   deciding	   our	   focus	   for	   charitable	   meanings,	   we	   attempt	   to	   invest	   much	   on those	  schools	  with	  more	  minority	  races,	  low	  SAT	  scores,	  high	  debt	  ratio	  and	  so on.	  We	  want	  to	  help	  those	  schools	  who	  don’t	  performance	  well	  as	  they	  have	  the highest	  likelihood	  of	  producing	  a	  strong	  positive	  effect	  on	  student	  performance.

<!-- b000623 | furniture | pages [20] -->


<!-- b000624 | prose | pages [20] -->
Then,	  we	  select	  the	  target	  schools	  by	  PCA	  based	  on	  the	  key	  indicators	  we focused.	  PCA	  ranks	  the	  candidate	  schools	  by	  the	  correlation	  with	  our	  concern, and	  we	  select	  the	  top	  50	  of	  them	  as	  target	  schools.	  After	  that,	  we	  determine	  an estimated	   ROI	   function	   to	   quantify	   the	   incremental	   utility	   of	   the	   schools	   that receive	  our	  investment	  based	  on	  the	  earnings	  and	  graduate	  rate.

<!-- b000625 | furniture | pages [20] -->


<!-- b000626 | prose | pages [20] -->
Using	  an	  iterative,	  multivariable,	  machine-­‐learning	  algorithm,	  we	  are	  able	  to optimize	  the	  total	  ROI	  of	  our	  target	  schools	  in	  five	  years.	  The	  solutions	  combine the	   investment	   amount	   and	   time	   duration	   of	   each	   school.	   Since	   we	   have	   the investment	  amount	  already,	  we	  can	  calculate	  the	  cumulative	  ROI	  in	  five	  years	  of each	  school	  and	  offer	  a	  recommending	  list.	  The	  top	  schools	  in	  the	  list	  are	  not	  well known	   schools,	   but	   the	   schools	   in	   village,	   small	   cities	   and	   so	   on,	   which correspond	  to	  our	  foundation’s	  focus.

<!-- b000627 | heading | pages [20] -->
10	  Letter	  to	  the	  CFO	  of	  the	  Goodgrant	  Foundation

<!-- b000628 | prose | pages [20] -->
Dear	  Mr.	  Alpha	  Chiang,

<!-- b000629 | furniture | pages [20] -->


<!-- b000630 | prose | pages [20] -->
In	  response	  to	  your	  questions	  regarding	  the	  optimal	  investment	  strategy	  to improve	  the	  performance	  of	  undergraduate	  students,	  we	  are	  writing	  to	  inform you	  of	  our	  work.

<!-- b000631 | furniture | pages [20] -->


<!-- b000632 | prose | pages [20] -->
We	   first	   decide	   the	   focus	   of	   your	   foundation.	   Since	   your	   foundation	   is	   a charitable	  organization	  intending	  to	  improve	  the	  educational	  performance,	  we recommend	   you	   to	   invest	   on	   the	   schools	   whose	   students	   has	   lower	   SAT/ACT scores,	  under	  much	  debt,	  from	  minority	  races	  and	  so	  on.	  This	  concern	  reflects your	  charitable	  identity	  and	  has	  the	  higher	  potential	  to	  improve	  the	  performance.

<!-- b000633 | furniture | pages [21] -->
Team	  #47823

<!-- b000634 | furniture | pages [21] -->
Page	  21	  of	  27

<!-- b000635 | prose | pages [21] -->
Then,	  we	  rank	  the	  schools	  by	  the	  correlation	  with	  the	  focus.	  If	  a	  school	  has	  these characters	  above,	  it	  will	  come	  first.

<!-- b000636 | furniture | pages [21] -->


<!-- b000637 | prose | pages [21] -->
The	   most	   creative	   work	   is	   that	   we	   determine	   a	   reasonable	   ROI	   function based	   on	   the	   social	   utility.	   We	   use	   “utility”	   to	   measure	   the	   contribution	   of	   a school.	  Firstly,	  we	  notice	  that	  if	  a	  school	  have	  more	  students,	  the	  contribution	  of the	   school	   is	   higher	   (assume	   other	   conditions	   are	   same).	   Because	   the	   school trains	   more	   students	   to	   workers.	   Secondly,	   we	   notice	   that	   the	   higher	   the earnings	  of	  graduated	  students	  are,	  the	  higher	  the	  utility	  is.	  So	  we	  multiply	  the number	   of	   students	   and	   the	   median	   of	   earning	   together	   to	   measure	   the	   total earning.	  Thirdly,	  we	  also	  notice	  that	  a	  higher	  utility	  school	  has	  high	  graduation rate.	  Therefore,	  we	  add	  the	  earnings	  and	  the	  graduation	  rate	  together	  as	  the	  total inputs.	  The	  investment	  amount	  will	  be	  added	  to	  the	  part	  of	  the	  earnings.	  Further more,	  we	  create	  a	  marginal	  rate	  of	  substitution	  to	  measure	  the	  interaction	  of	  the two	  factors.	  We	  can’t	  find	  the	  accurate	  value	  of	  the	  MRS	  but	  can	  be	  modified	  by deep	  researches.

<!-- b000638 | furniture | pages [21] -->


<!-- b000639 | prose | pages [21] -->
The	   ROI	   function	   is	   the	   incremental	   utility	   after	   the	   investment,	   which	   is easy	   to	   understand.	   And	   another	   point	   is	   that	   the	   utility	   function	   is	   concave, which	  means	  the	  ROI	  will	  be	  less	  if	  invest	  more	  on	  a	  school.	  In	  other	  words,	  if	  we invest	  the	  same	  amount	  on	  a	  certain	  school,	  the	  ROI	  will	  be	  less	  than	  this	  year.	  So the	  schools	  with	  less	  earnings	  and	  lower	  graduation	  rate	  have	  large	  ROI,	  which means	   the	   potential	   of	   the	   effective	   use	   of	   funding	   is	   high.	   We	   think	   that	   this model	  describe	  the	  real	  situation	  well.

<!-- b000640 | furniture | pages [21] -->


<!-- b000641 | prose | pages [21] -->
Another	  accomplishment	  is	  that	  we	  utilize	  a	  complex	  algorithm	  to	  maximize the	  total	  ROI	  of	  the	  target	  schools.	  The	  algorithm	  is	  typically	  useful	  to	  solve	  the problem	  to	  determine	  the	  future	  investment	  amount	  and	  time	  duration	  for	  each target	  school.	  Further	  more,	  our	  algorithm	  can	  easily	  be	  changed	  to	  solve	  other investment	   strategy	   making	   problems	   with	   different	   amount	   of	   donations	   and different	  ROI	  functions.	  In	  other	  word,	  we	  offer	  a	  general	  method	  to	  solve	  this kind	  of	  problems.

<!-- b000642 | furniture | pages [21] -->


<!-- b000643 | prose | pages [21] -->
Almost	   none	   of	   our	   invested	   schools	   are	   well-­‐known,	   which	   is	   consistent with	   our	   focus,	   because	   the	   well-­‐known	   schools	   receive	   so	   much	   investment from	   other	   organizations	   like	   Gates	   Foundation.	   The	   complete	   investment strategy	  is	  attached	  in	  the	  appendix.

<!-- b000644 | furniture | pages [21] -->


<!-- b000645 | prose | pages [21] -->
To	  summarize,	  we	  cling	  to	  the	  belief	  that	  our	  model	  is	  a	  powerful	  tool	  to	  help you	  devise	  the	  best	  investment	  strategy,	  including	  the	  amount	  of	  investment	  and time	  duration	  per	  school.

<!-- b000646 | prose | pages [21] -->
Yours,	  sincerely

<!-- b000647 | prose | pages [21] -->
Team	  47823

<!-- b000648 | furniture | pages [21] -->


<!-- b000649 | furniture | pages [22] -->
Team	  #47823

<!-- b000650 | furniture | pages [22] -->
Page	  22	  of	  27

<!-- b000651 | heading | pages [22] -->
11	  References

<!-- b000652 | furniture | pages [22] -->


<!-- b000653 | references | pages [22] -->
[1]Retrieved	  January	  31,	  2016,	  from

<!-- b000654 | references | pages [22] -->
http://data.foundationcenter.org/#/fc1000/subject:all/all/total/bar:amount/

<!-- b000655 | references | pages [22] -->
2012

<!-- b000656 | references | pages [22] -->
[2]Zhuo	  Jinwu.	  Application	  of	  Matlab	  in	  Mathematical	  Modeling[M].	  Beijing:

<!-- b000657 | references | pages [22] -->
Beihang	  University	  Press,2014:41.

<!-- b000658 | references | pages [22] -->
[3]Wan	  Xinghuo,	  Tan	  Yili.	  Problem	  of	  the	  pretreatment	  on	  raw	  data	  with	  PCA[J].

<!-- b000659 | references | pages [22] -->
Chinese	  Journal	  of	  Health	  Statistics,	  2005,22(5)：327-­‐329.

<!-- b000660 | references | pages [22] -->
[4]Paul	  Wachtel	  .	  The	  Effect	  of	  Earnings	  of	  School	  and	  College	  Investment

<!-- b000661 | references | pages [22] -->
Expenditures[J].	  Review	  of	  Economics	  &	  Statistics,	  1976,	  58(58):326-­‐331

<!-- b000662 | references | pages [22] -->
[5]Stephen	  Boyd,	  Lieven	  Vandenberghe.	  Convex	  Optimization[M].	  Cambridge:

<!-- b000663 | references | pages [22] -->
Cambridge	  University	  Press,2014

<!-- b000664 | references | pages [22] -->
[6]Yu	  Shengwei.	  Analysis	  and	  application	  of	  cases	  of	  Matlab	  optimization

<!-- b000665 | references | pages [22] -->
algorithm[M].	  Beijing:	  Tsinghua	  University	  Press,2014:179.

<!-- b000666 | references | pages [22] -->
[7]Li	  Desheng.	  Improvement	  and	  Application	  of	  Particle	  Swarm	  Optimization

<!-- b000667 | references | pages [22] -->
Coupling	  with	  Classic	  Optimization[D].Beijing:	  Beijing	  University	  of	  Civil

<!-- b000668 | references | pages [22] -->
Engineering	  and	  Architecture,	  2014:	  29-­‐43.

<!-- b000669 | references | pages [22] -->
[8]Retrieved	  January	  31,	  2016,	  from

<!-- b000670 | references | pages [22] -->
http://www.gatesfoundation.org/How-­‐We-­‐Work/Quick-­‐Links/Grants-­‐Database

<!-- b000671 | references | pages [22] -->
#

<!-- b000672 | furniture | pages [22] -->


<!-- b000673 | furniture | pages [22] -->


<!-- b000674 | furniture | pages [22] -->


<!-- b000675 | furniture | pages [22] -->


<!-- b000676 | furniture | pages [22] -->


<!-- b000677 | furniture | pages [22] -->


<!-- b000678 | furniture | pages [22] -->


<!-- b000679 | furniture | pages [22] -->


<!-- b000680 | furniture | pages [23] -->
Team	  #47823

<!-- b000681 | furniture | pages [23] -->
Page	  23	  of	  27

<!-- b000682 | heading | pages [23] -->
12	  Appendix	  1:	  Recommending	  List

<!-- b000683 | prose | pages [23] -->
INSTNM

<!-- b000684 | prose | pages [23] -->
Rank

<!-- b000685 | prose | pages [23] -->
1 MacCormac	  College

<!-- b000686 | prose | pages [23] -->
2 Paul	  Quinn	  College

<!-- b000687 | prose | pages [23] -->
3 Andrew	  College

<!-- b000688 | prose | pages [23] -->
4 Bidwell	  Training	  Center	  Inc

<!-- b000689 | prose | pages [23] -->
5 Colorado	  Heights	  University

<!-- b000690 | prose | pages [23] -->
6 Tougaloo	  College

<!-- b000691 | prose | pages [23] -->
7 Brevard	  College

<!-- b000692 | prose | pages [23] -->
8 Paine	  College

<!-- b000693 | prose | pages [23] -->
9 Fisk	  University

<!-- b000694 | prose | pages [23] -->
10 Southeast	  Missouri	  Hospital	  College	  of

<!-- b000695 | prose | pages [23] -->
Nursing	  and	  Health	  Sciences

<!-- b000696 | prose | pages [23] -->
11 Stillman	  College

<!-- b000697 | prose | pages [23] -->
12 Livingstone	  College

<!-- b000698 | prose | pages [23] -->
13 Leech	  Lake	  Tribal	  College

<!-- b000699 | prose | pages [23] -->
14 Virginia	  Union	  University

<!-- b000700 | prose | pages [23] -->
15 Widener	  University-­‐Delaware	  Campus

<!-- b000701 | prose | pages [23] -->
16 University	  of	  South	  Carolina-­‐Salkehatchie

<!-- b000702 | prose | pages [23] -->
17 Elizabeth	  City	  State	  University

<!-- b000703 | prose | pages [23] -->
18 Huston-­‐Tillotson	  University

<!-- b000704 | prose | pages [23] -->
19 Edward	  Waters	  College

<!-- b000705 | prose | pages [23] -->
20 Claflin	  University

<!-- b000706 | prose | pages [23] -->
21 Sterling	  College

<!-- b000707 | prose | pages [23] -->
22 Olivet	  College

<!-- b000708 | prose | pages [23] -->
23 Ohio	  Valley	  University

<!-- b000709 | prose | pages [23] -->
24 Rust	  College

<!-- b000710 | prose | pages [23] -->
25 Culver-­‐Stockton	  College

<!-- b000711 | prose | pages [23] -->
26 Bethany	  College

<!-- b000712 | prose | pages [23] -->
27 Greensboro	  College

<!-- b000713 | prose | pages [23] -->
28 Ottawa	  University-­‐Ottawa

<!-- b000714 | prose | pages [23] -->
29 Webber	  International	  University

<!-- b000715 | prose | pages [23] -->
30 Bacone	  College

<!-- b000716 | prose | pages [23] -->
31 Dillard	  University

<!-- b000717 | prose | pages [23] -->
32 North	  Greenville	  University

<!-- b000718 | prose | pages [23] -->
33 Manor	  College

<!-- b000719 | prose | pages [23] -->
34 Newberry	  College

<!-- b000720 | prose | pages [23] -->
35 New	  River	  Community	  and	  Technical

<!-- b000721 | prose | pages [23] -->
College

<!-- b000722 | prose | pages [23] -->
ROI t 1 2 3 4 5

<!-- b000723 | prose | pages [23] -->
2.22 4 13.62 0.17 0.00 5.69 4.78

<!-- b000724 | prose | pages [23] -->
2.02 5 7.84 1.02 3.09 2.92 5.10

<!-- b000725 | prose | pages [23] -->
1.81 3 0.00 0.00 0.33 5.11 7.94

<!-- b000726 | prose | pages [23] -->
1.80 5 0.18 0.00 7.18 0.66 0.75

<!-- b000727 | prose | pages [23] -->
1.64 3 8.24 0.46 11.32 0.00 0.00

<!-- b000728 | prose | pages [23] -->
1.12 6 12.01 0.31 0.44 5.62 2.29

<!-- b000729 | prose | pages [23] -->
1.05 5 5.46 0.00 9.13 0.22 1.85

<!-- b000730 | prose | pages [23] -->
0.98 5 0.00 0.98 3.48 6.12 0.43

<!-- b000731 | prose | pages [23] -->
0.90 6 8.84 1.49 0.70 0.71 0.14

<!-- b000732 | prose | pages [23] -->
0.84 5 2.38 1.32 0.00 5.59 3.80

<!-- b000733 | prose | pages [23] -->
0.83 3 0.00 1.95 2.75 6.29 0.00

<!-- b000734 | prose | pages [23] -->
0.75 3 0.00 6.15 0.00 0.78 3.92

<!-- b000735 | prose | pages [23] -->
0.73 2 2.00 3.60 0.00 0.00 0.00

<!-- b000736 | prose | pages [23] -->
0.70 5 1.95 10.62 2.42 1.70 0.32

<!-- b000737 | prose | pages [23] -->
0.69 3 0.00 2.02 0.11 1.98 0.00

<!-- b000738 | prose | pages [23] -->
0.66 5 2.10 2.58 0.25 0.30 1.28

<!-- b000739 | prose | pages [23] -->
0.66 5 3.26 8.59 6.22 2.30 4.88

<!-- b000740 | prose | pages [23] -->
0.65 4 1.32 7.13 0.39 0.00 3.80

<!-- b000741 | prose | pages [23] -->
0.64 4 0.00 3.49 1.08 1.89 0.24

<!-- b000742 | prose | pages [23] -->
0.62 4 2.46 4.10 5.49 0.00 5.61

<!-- b000743 | prose | pages [23] -->
0.60 3 0.00 0.00 4.92 0.26 3.06

<!-- b000744 | prose | pages [23] -->
0.60 4 0.00 3.49 5.29 2.33 3.47

<!-- b000745 | prose | pages [23] -->
0.51 2 1.35 0.00 3.40 0.00 0.00

<!-- b000746 | prose | pages [23] -->
0.49 5 0.30 0.46 1.10 0.10 1.67

<!-- b000747 | prose | pages [23] -->
0.48 4 0.00 9.01 0.16 1.78 0.26

<!-- b000748 | prose | pages [23] -->
0.47 4 0.00 1.55 0.30 6.24 0.82

<!-- b000749 | prose | pages [23] -->
0.46 4 0.00 0.43 5.36 0.11 4.16

<!-- b000750 | prose | pages [23] -->
0.46 3 0.00 0.38 0.00 8.62 0.20

<!-- b000751 | prose | pages [23] -->
0.44 3 0.00 6.00 1.43 0.17 0.00

<!-- b000752 | prose | pages [23] -->
0.42 3 2.72 0.00 0.45 4.32 0.00

<!-- b000753 | prose | pages [23] -->
0.38 5 0.53 1.10 1.98 3.74 1.86

<!-- b000754 | prose | pages [23] -->
0.38 5 2.10 0.20 3.70 0.26 9.26

<!-- b000755 | prose | pages [23] -->
0.36 4 0.00 2.31 0.12 5.08 0.66

<!-- b000756 | prose | pages [23] -->
0.36 5 0.35 0.44 0.70 0.80 5.42

<!-- b000757 | prose | pages [23] -->
0.36 5 0.15 3.26 0.49 1.26 8.15

<!-- b000758 | furniture | pages [24] -->
Team	  #47823

<!-- b000759 | prose | pages [24] -->
36 Orleans	  Technical	  Institute

<!-- b000760 | prose | pages [24] -->
37 Louisburg	  College

<!-- b000761 | prose | pages [24] -->
38 Bethune-­‐Cookman	  University

<!-- b000762 | prose | pages [24] -->
39 Richard	  Bland	  College	  of	  the	  College	  of

<!-- b000763 | prose | pages [24] -->
William	  and	  Mary

<!-- b000764 | prose | pages [24] -->
40 Chowan	  University

<!-- b000765 | prose | pages [24] -->
41 Alabama	  State	  University

<!-- b000766 | prose | pages [24] -->
42 Campbell	  University

<!-- b000767 | prose | pages [24] -->
43 Delaware	  State	  University

<!-- b000768 | prose | pages [24] -->
44 Texas	  Southern	  University

<!-- b000769 | prose | pages [24] -->
45 Cumberland	  University

<!-- b000770 | prose | pages [24] -->
46 Cochise	  College

<!-- b000771 | prose | pages [24] -->
47 Central	  State	  University

<!-- b000772 | prose | pages [24] -->
48 Alcorn	  State	  University

<!-- b000773 | prose | pages [24] -->
49 Saint	  Augustine's	  University

<!-- b000774 | prose | pages [24] -->
50 Chattanooga	  State	  Community	  College

<!-- b000775 | furniture | pages [24] -->


<!-- b000776 | prose | pages [24] -->
Utilization	  rate	  of	  funds	  of	  each	  year	  (%)

<!-- b000777 | furniture | pages [24] -->


<!-- b000778 | furniture | pages [24] -->


<!-- b000779 | furniture | pages [24] -->


<!-- b000780 | furniture | pages [24] -->


<!-- b000781 | furniture | pages [24] -->


<!-- b000782 | furniture | pages [24] -->


<!-- b000783 | furniture | pages [24] -->


<!-- b000784 | furniture | pages [24] -->


<!-- b000785 | furniture | pages [24] -->


<!-- b000786 | furniture | pages [24] -->


<!-- b000787 | furniture | pages [24] -->


<!-- b000788 | furniture | pages [24] -->


<!-- b000789 | furniture | pages [24] -->
Page	  24	  of	  27

<!-- b000790 | prose | pages [24] -->
0.31 4 0.89 1.19 0.00 0.16 0.36

<!-- b000791 | prose | pages [24] -->
0.27 3 0.00 0.81 1.07 0.00 0.18

<!-- b000792 | prose | pages [24] -->
0.21 3 8.43 1.15 0.00 0.78 0.00

<!-- b000793 | prose | pages [24] -->
0.21 4 1.32 0.00 1.56 1.26 0.40

<!-- b000794 | prose | pages [24] -->
0.20 3 0.42 1.55 0.00 3.32 0.00

<!-- b000795 | prose | pages [24] -->
0.16 5 1.69 0.00 0.54 5.06 1.28

<!-- b000796 | prose | pages [24] -->
0.12 5 2.59 0.61 6.94 0.10 5.85

<!-- b000797 | prose | pages [24] -->
0.11 3 0.00 3.41 0.00 0.53 3.69

<!-- b000798 | prose | pages [24] -->
0.10 4 1.13 1.95 4.85 0.00 1.20

<!-- b000799 | prose | pages [24] -->
0.09 3 0.37 0.00 0.11 2.02 0.00

<!-- b000800 | prose | pages [24] -->
0.09 2 2.61 2.36 0.00 0.00 0.00

<!-- b000801 | prose | pages [24] -->
0.07 4 0.17 0.14 0.12 0.76 0.00

<!-- b000802 | prose | pages [24] -->
0.07 3 0.81 0.00 0.00 2.19 0.61

<!-- b000803 | prose | pages [24] -->
0.06 2 0.00 0.18 0.00 0.56 0.00

<!-- b000804 | prose | pages [24] -->
0.02 2 0.00 1.83 0.65 0.00 0.00

<!-- b000805 | furniture | pages [24] -->


<!-- b000806 | furniture | pages [24] -->


<!-- b000807 | prose | pages [24] -->
99.60 99.79 99.63 99.71 99.69

<!-- b000808 | furniture | pages [25] -->
Team	  #47823

<!-- b000809 | furniture | pages [25] -->
Page	  25	  of	  27

<!-- b000810 | heading | pages [25] -->
13	  Appendix	   2:	   An	   Introduction	   to	   the	   Improved	   PSO

<!-- b000811 | heading | pages [25] -->
Algorithm	  Based	  on	  Augmented	  Lagrange	  Function

<!-- b000812 | prose | pages [25] -->
(source:	   Li	   Desheng.	   Improvement	   and	   Application	   of	   Particle	   Swarm

<!-- b000813 | furniture | pages [25] -->


<!-- b000814 | prose | pages [25] -->
Optimization	  Coupling	  with	  Classic	  Optimization[D].Beijing:	  Beijing	  University	  of Civil	  Engineering	  and	  Architecture,	  2014:	  29-­‐43.)

<!-- b000815 | prose | pages [25] -->
The	   algorithm	   attempts	   to	   solve	   the	   non-­‐linear	   constraint	   optimization

<!-- b000816 | furniture | pages [25] -->


<!-- b000817 | prose | pages [25] -->
problem	  below:

<!-- b000818 | prose | pages [25] -->
min: f (x)

<!-- b000819 | prose | pages [25] -->
⎧

<!-- b000820 | prose | pages [25] -->
ci(x)= 0,i =1,2,!,me

<!-- b000821 | prose | pages [25] -->
⎪

<!-- b000822 | furniture | pages [25] -->


<!-- b000823 | furniture | pages [25] -->


<!-- b000824 | prose | pages [25] -->
(1)

<!-- b000825 | prose | pages [25] -->
c j(x)≥0, j = me+1,!,m

<!-- b000826 | prose | pages [25] -->
s.t.

<!-- b000827 | prose | pages [25] -->
⎨

<!-- b000828 | prose | pages [25] -->
⎪

<!-- b000829 | prose | pages [25] -->
l ≤x ≤u

<!-- b000830 | prose | pages [25] -->
⎩

<!-- b000831 | prose | pages [25] -->
For	   this	   problem,	   if	   there	   is	   not	   the	   constraint	   l ≤x ≤u ,	   we	   can	   use	   the

<!-- b000832 | furniture | pages [25] -->


<!-- b000833 | prose | pages [25] -->
augmented	  Lagrange	  multiplier	  method	  to	  solve	  it.	  Given	  the	  Lagrange	  multiplier

<!-- b000834 | prose | pages [25] -->
vector	   λ k 	   and	  the	  barrier	  parameter	  vectorσ k ,	  the	  sub-­‐problem	  of	  the	  step	  k	  is:

<!-- b000835 | prose | pages [25] -->
min P(x,λ k,σ k )

<!-- b000836 | furniture | pages [25] -->


<!-- b000837 | prose | pages [25] -->
where:

<!-- b000838 | prose | pages [25] -->
me∑

<!-- b000839 | prose | pages [25] -->
(2)

<!-- b000840 | prose | pages [25] -->
m

<!-- b000841 | prose | pages [25] -->
[λici(x) −1 P(x,λ,σ ) = f (x) −

<!-- b000842 | furniture | pages [25] -->


<!-- b000843 | prose | pages [25] -->
i=1

<!-- b000844 | prose | pages [25] -->
⎧

<!-- b000845 | prose | pages [25] -->
λici(x) −1

<!-- b000846 | prose | pages [25] -->
∑

<!-- b000847 | prose | pages [25] -->
2σ i(ci(x))2]−

<!-- b000848 | prose | pages [25] -->
(x,λ,σ ) (3)

<!-- b000849 | prose | pages [25] -->
Pi i=me+1

<!-- b000850 | prose | pages [25] -->
2σ i(ci(x))2,if λi −σ ici(x) > 0

<!-- b000851 | prose | pages [25] -->
⎪⎪

<!-- b000852 | prose | pages [25] -->
Pi(x,λ,σ ) =

<!-- b000853 | furniture | pages [25] -->


<!-- b000854 | prose | pages [25] -->
⎨

<!-- b000855 | prose | pages [25] -->
1

<!-- b000856 | prose | pages [25] -->
2

<!-- b000857 | furniture | pages [25] -->


<!-- b000858 | prose | pages [25] -->
(4)

<!-- b000859 | prose | pages [25] -->
λi /σ i ,otherwise

<!-- b000860 | prose | pages [25] -->
⎪ ⎪

<!-- b000861 | prose | pages [25] -->
2

<!-- b000862 | prose | pages [25] -->
⎩

<!-- b000863 | prose | pages [25] -->
If	   there	   is	   the	   boundary	   constraint	   l ≤x ≤u 	   in	   the	   non-­‐linear	   constraint

<!-- b000864 | furniture | pages [25] -->


<!-- b000865 | prose | pages [25] -->
optimization	   problem,	   we	   modify	   the	   augmented	   Lagrange	   multiplier	   method

<!-- b000866 | prose | pages [25] -->
above.	   We	   assume	   that	   we	   knew	   the	   Lagrange	   multiplier	   vector	   λ k 	   and	   the

<!-- b000867 | prose | pages [25] -->
barrier	  parameter	  vectorσ k .	  So	  we	  solve	  the	  sub-­‐problem	  in	  step	  k:

<!-- b000868 | prose | pages [25] -->
minP(x,λ k ,σ k)

<!-- b000869 | prose | pages [25] -->
⎧

<!-- b000870 | furniture | pages [25] -->


<!-- b000871 | prose | pages [25] -->
⎨

<!-- b000872 | furniture | pages [25] -->


<!-- b000873 | prose | pages [25] -->
(5)

<!-- b000874 | prose | pages [25] -->
s.t.l ≤x ≤µ

<!-- b000875 | prose | pages [25] -->
⎩

<!-- b000876 | prose | pages [25] -->
The	   Lagrange	   multiplier	   method	   is	   accomplished	   by	   inside	   and	   outside

<!-- b000877 | furniture | pages [25] -->


<!-- b000878 | furniture | pages [26] -->
Team	  #47823

<!-- b000879 | furniture | pages [26] -->
Page	  26	  of	  27

<!-- b000880 | prose | pages [26] -->
to-­‐tier	  construct.	  We	  solve	  the	  equations	  (5)	  inside	  the	  construct,	  generating	  a group	  of	  new	  initial	  variable.	  And	  modify	  the	  outside	  barrier	  parameter	  vector and	  the	  multiplier	  vector.	  Test	  whether	  satisfies	  the	  iteration	  criterion	  or	  not.	   	   If not,	  construct	  the	  sub-­‐problem	  in	  the	  next	  iteration.	  If	  so,	  stop	  the	  algorithm.

<!-- b000881 | prose | pages [26] -->
When	  initialing	  the	  multiplier	  vector	   λ 0 	   and	  the	  barrier	  parameter	  vector

<!-- b000882 | furniture | pages [26] -->


<!-- b000883 | prose | pages [26] -->
σ 0 ,	  they	  are	  usually	  set	  as	  positive	  vector.	  In	  the	  process	  of	  iteration,	  we	  use	  the

<!-- b000884 | prose | pages [26] -->
equations	  below	  to	  modify	  the	  Lagrange	  multiplier	  vector	   λ :

<!-- b000885 | prose | pages [26] -->
⎧

<!-- b000886 | prose | pages [26] -->
k+1 = λi

<!-- b000887 | prose | pages [26] -->
k −σ i

<!-- b000888 | prose | pages [26] -->
k

<!-- b000889 | prose | pages [26] -->
λi

<!-- b000890 | prose | pages [26] -->
kci(x

<!-- b000891 | prose | pages [26] -->
⎨⎪

<!-- b000892 | furniture | pages [26] -->


<!-- b000893 | prose | pages [26] -->
k+1 = max{λi

<!-- b000894 | prose | pages [26] -->
k −σ i

<!-- b000895 | prose | pages [26] -->
⎩⎪

<!-- b000896 | prose | pages [26] -->
λi

<!-- b000897 | prose | pages [26] -->
),i =1,2,!me

<!-- b000898 | furniture | pages [26] -->


<!-- b000899 | prose | pages [26] -->
(6)

<!-- b000900 | prose | pages [26] -->
k

<!-- b000901 | prose | pages [26] -->
),0},i = me+1,!,m

<!-- b000902 | prose | pages [26] -->
kci(x

<!-- b000903 | prose | pages [26] -->
where	   x k 	   is	   the	   solution	   of	   NO.k	   sub-­‐problem	   (5),	   and	   we	   use	   the	   equation

<!-- b000904 | prose | pages [26] -->
below	  to	  modify	  the	  barrier	  parameter	  vector:

<!-- b000905 | prose | pages [26] -->
σ k+1 = γσ k

<!-- b000906 | furniture | pages [26] -->


<!-- b000907 | prose | pages [26] -->
When	   ! c(xk+1) !2≤1

<!-- b000908 | prose | pages [26] -->
(7)

<!-- b000909 | prose | pages [26] -->
4 ! c(xk ) !2 ,	  we	  set	   γ =1;	  if	  not,	  we	  set	   γ ≻1 	   (usually	  10

<!-- b000910 | furniture | pages [26] -->


<!-- b000911 | prose | pages [26] -->
or	  100),	  where:

<!-- b000912 | prose | pages [26] -->
me∑

<!-- b000913 | prose | pages [26] -->
m

<!-- b000914 | prose | pages [26] -->
(ci(x))2 + ! c(x) !2=

<!-- b000915 | furniture | pages [26] -->


<!-- b000916 | prose | pages [26] -->
i=1 ∑

<!-- b000917 | prose | pages [26] -->
(min{ci(x),0})2

<!-- b000918 | furniture | pages [26] -->


<!-- b000919 | prose | pages [26] -->
(8)

<!-- b000920 | prose | pages [26] -->
i=me+1

<!-- b000921 | prose | pages [26] -->
Given	   an	   𝜀,	   the	   stopping	   criterion	   is	   ! c(x) !2≤	   𝜀,	   stop	   the	   iteration	   of

<!-- b000922 | furniture | pages [26] -->


<!-- b000923 | prose | pages [26] -->
Lagrange	  multiplier	  method.	   x k 	   is	  an	  approximate	  optimization	  of	  (1)

<!-- b000924 | prose | pages [26] -->
The	   specific	   process	   of	   the	   improved	   PSO	   algorithm	   based	   on	   augmented

<!-- b000925 | furniture | pages [26] -->


<!-- b000926 | prose | pages [26] -->
Lagrange	  function:

<!-- b000927 | prose | pages [26] -->
Step	  A:	  initialize	   λ 0 	   and	   σ 0 	   ;

<!-- b000928 | furniture | pages [26] -->


<!-- b000929 | prose | pages [26] -->
Step	  B:	  construct	  boundary	  constraint	  optimization	  problem	  (5);

<!-- b000930 | furniture | pages [26] -->


<!-- b000931 | prose | pages [26] -->
Step	  C:	  initialize	  PSO	  parameters,	  including	  initial	  position	  and	  velocity;

<!-- b000932 | furniture | pages [26] -->


<!-- b000933 | prose | pages [26] -->
Step	  D:	  compute	  the	  position x j(t +1)and	  velocityv j(t +1) of	  the	  next	  period;

<!-- b000934 | furniture | pages [26] -->


<!-- b000935 | furniture | pages [27] -->
Team	  #47823

<!-- b000936 | furniture | pages [27] -->
Page	  27	  of	  27

<!-- b000937 | furniture | pages [27] -->


<!-- b000938 | prose | pages [27] -->
Step	  E:	  update	  the	  personal	  best	  particle p j and	  global	  best	  particle pg ;

<!-- b000939 | prose | pages [27] -->
Step	  F:	  set	   x0 = pg,γ = 0.001,eps = 1.0e−3,d0 = −g0,kk = 0

<!-- b000940 | furniture | pages [27] -->


<!-- b000941 | prose | pages [27] -->
Step	  G:	  if	   ! dkk !≤epsor kk > 2,	  switch	  to	  Step	  L,	  or	  switch	  to	  Step	  H

<!-- b000942 | furniture | pages [27] -->


<!-- b000943 | prose | pages [27] -->
Step	  H:	  setα = 1;

<!-- b000944 | furniture | pages [27] -->


<!-- b000945 | prose | pages [27] -->
Step	  I: xkk+1 = xkk +αdkk

<!-- b000946 | furniture | pages [27] -->


<!-- b000947 | prose | pages [27] -->
T ,	  switch	  to	  Step	  K,	  or	  set	   α = 0.5∗α ,	  back

<!-- b000948 | prose | pages [27] -->
Step	  J:	  if f (xkk+1) < f (xkk ) −γαd0d0

<!-- b000949 | furniture | pages [27] -->


<!-- b000950 | prose | pages [27] -->
to	  Step	  I;

<!-- b000951 | prose | pages [27] -->
T

<!-- b000952 | prose | pages [27] -->
Step	   K:	   compute βkk = gkk+1

<!-- b000953 | prose | pages [27] -->
gkk+1

<!-- b000954 | prose | pages [27] -->
, dkk+1 = −gkk+1 + βkkdkk ,	   set	   kk = kk +1,back	   to

<!-- b000955 | furniture | pages [27] -->


<!-- b000956 | prose | pages [27] -->
T gkk

<!-- b000957 | prose | pages [27] -->
gkk

<!-- b000958 | prose | pages [27] -->
Step	  G;

<!-- b000959 | prose | pages [27] -->
Step	  L:	  update pg = xkk

<!-- b000960 | furniture | pages [27] -->


<!-- b000961 | furniture | pages [27] -->


<!-- b000962 | prose | pages [27] -->
Step	  M:	  judge	  the	  PSO	  stopping	  criterion,	  if	  so,	  switch	  to	  Step	  N,	  or	  back	  to Step	  D;

<!-- b000963 | furniture | pages [27] -->


<!-- b000964 | prose | pages [27] -->
Step	   N:	   judge	   the	   Lagrange	   multiplier	   stopping	   criterion,	   if	   so,	   stop	   the algorithm,	  output	  the	  result,	  or	  switch	  to	  Step	  O;

<!-- b000965 | prose | pages [27] -->
Step	   O:	   modify	   the	   Lagrange	   multiplier	   parameter λ k,σ k according	   to

<!-- b000966 | furniture | pages [27] -->


<!-- b000967 | prose | pages [27] -->
(6)~(9)
