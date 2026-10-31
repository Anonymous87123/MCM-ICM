# P-B-2010-7507-24d34e5d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | prose | pages [1] -->
Centroids, Clusters and Crime: Anchoring the Geographic Profiles of Serial Criminals Crime prediction is an old human tradition. The technology employed has changed drastically over the last fifty years with the advent of the computer, yet the techniques employed are the same as ever. The task of predicting future crime locations is still fundamentally about discovering and exploiting patterns and is therefore a mathematical task. A particularly challenging problem in this field is modeling the behavior of serial killers, as most (violent) repeat offenders choose victims who are complete strangers to them. Since finding correlations between the victims of a serial criminal is algorithmically difficult, we predict where a criminal will strike next, instead of whom. This practice of predicting a criminal’s spatial patterns is called Geographic Profiling.

<!-- b000010 | prose | pages [1] -->
Geographic profiling research has clearly shown that, for most violent serial criminals, there is a significant and strong correlation between the distance between crime sites and the distance to the criminal’s home or residence; roughly, serial criminals tend to commit crimes in a distinct radial band around a central point. Subsequent researchers, however, have extended the idea of ‘home’ to include areas of significance to the criminal’s activities: for example, a serial killer may strike around his workplace, or only in the part of town where prostitutes abound. These centers of activity, termed “anchor points” provide a strong pattern within serial criminal behavior with which we can build a predictive algorithm.

<!-- b000011 | prose | pages [1] -->
We build our models off the assumptions that the entire domain of analysis is a potential crime spot, movement of the criminal is uninhibited, and area in question is large enough to contain all possible strike points. With these three assumptions we are able to consider our domain a metric space on which our predictive algorithms can create spatial likelihoods. Additionally, we assume that the offender in question is a “violent” serial criminal, as research suggests serial burglars and arsonists are less likely to obey the aforementioned spatial patterns. From this, we may assume the existence of one or more anchor points, which will provide the basis for our model.

<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | prose | pages [1] -->
There are substantial differences, however, in the criminal’s expected behavior depending on whether he has one anchor point, or several. We treat the single anchor point case first, taking only the spatial coordinates of the criminal’s last strikes and the sequence of the crimes as inputs. Estimate the single anchor point to be the centroid of the previous crimes, we generate a “likelihood crater”: a !-distribution whose parameters are fit to the preexisting data, including time trends. Height of this crater then corresponds to the likelihood of a future crime at that location. Next, we consider the multiple anchor point case: using a cluster finding and sorting method, we identify groupings in the data and then build likelihood craters around the centroids of each. Individual clusters are then given weight according to recency and number of points. Finally, we test each algorithm on the criminal’s past offences (using the first N to predict crime N+1) and determine which of the two techniques performs better. From these tests we also develop a standard metric for measuring our level of confidence in the output.

<!-- b000014 | prose | pages [1] -->
There is a notable dearth of public domain data giving both locations and sequencing data for the crimes of violent serial killers, so we extract seven datasets (for three offenders) from published research. We use four in developing our model and examining its response to changes in sequence, geographic concentration, and total number of points. The location of the last crime is removed from the input, and then compared to the models’ predictions. To evaluate, we assume the police want ideally to distribute their resources so that one will be on scene when the next crime is committed and compute an “effectiveness multiplier,” which describes how much more usefully police resources would be distributed under our model versus a random guess.

<!-- b000015 | prose | pages [1] -->
Then, we evaluate our models by running blind on the remaining datasets. The results show a clear superiority to the multiple anchor points method, and qualitatively support or model, but we would require more data to claim success with statistical significance. Overall, the model will be most successful in predicting longer crime sprees with clearly clustered data. We also demonstrate clear failure if criminal suddenly changes behavior, and also note that the model’s output must be partnered with the knowledge and experience of a veteran cop. Finally, we note that by construction, our algorithm will tend to predict the criminal’s anchor points more accurately than it predicts his next strike point. Our recommendation is that police consider using the anchor point prediction as their primary investigative tool.

<!-- b000016 | prose | pages [2] -->
CENTROIDS, CLUSTERS AND CRIME: ANCHORING

<!-- b000017 | prose | pages [2] -->
THE GEOGRAPHIC PROFILES OF SERIAL

<!-- b000018 | prose | pages [2] -->
CRIMINALS

<!-- b000019 | furniture | pages [2] -->
Team # 7507

<!-- b000020 | prose | pages [2] -->
February 22, 2010

<!-- b000021 | prose | pages [2] -->
1

<!-- b000022 | furniture | pages [3] -->
Team # 7507

<!-- b000023 | heading | pages [3] -->
Table of Contents

<!-- b000024 | contents | pages [3] -->
1

<!-- b000025 | contents | pages [3] -->
Introduction

<!-- b000026 | contents | pages [3] -->
2

<!-- b000027 | contents | pages [3] -->
Background

<!-- b000028 | contents | pages [3] -->
3

<!-- b000029 | contents | pages [3] -->
Assumptions

<!-- b000030 | furniture | pages [3] -->
Page 2

<!-- b000031 | contents | pages [3] -->
3

<!-- b000032 | contents | pages [3] -->
4

<!-- b000033 | contents | pages [3] -->
6

<!-- b000034 | contents | pages [3] -->
Domain is Approximately Urban . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000035 | contents | pages [3] -->
3.1

<!-- b000036 | contents | pages [3] -->
6

<!-- b000037 | contents | pages [3] -->
Violent Serial Crimes by a Single Offender

<!-- b000038 | contents | pages [3] -->
3.2

<!-- b000039 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . .

<!-- b000040 | contents | pages [3] -->
8

<!-- b000041 | contents | pages [3] -->
Spatial Focus . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000042 | contents | pages [3] -->
3.3

<!-- b000043 | contents | pages [3] -->
4

<!-- b000044 | contents | pages [3] -->
Developing a Serial Crime Test Set

<!-- b000045 | contents | pages [3] -->
9

<!-- b000046 | contents | pages [3] -->
9

<!-- b000047 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [3] -->
4.1

<!-- b000049 | contents | pages [3] -->
The Scarcity of Source Data

<!-- b000050 | contents | pages [3] -->
9

<!-- b000051 | contents | pages [3] -->
An Alternative: Pixel Point Analysis . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [3] -->
4.2

<!-- b000053 | contents | pages [3] -->
11

<!-- b000054 | contents | pages [3] -->
Metrics of Success: The Psychic and the Hairﬁnder

<!-- b000055 | contents | pages [3] -->
5

<!-- b000056 | contents | pages [3] -->
11

<!-- b000057 | contents | pages [3] -->
The Effectiveness Multiplier . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000058 | contents | pages [3] -->
5.1

<!-- b000059 | contents | pages [3] -->
12

<!-- b000060 | contents | pages [3] -->
Robustness of the Metric . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000061 | contents | pages [3] -->
5.2

<!-- b000062 | contents | pages [3] -->
6

<!-- b000063 | contents | pages [3] -->
Two Schemes for Spatial Prediction

<!-- b000064 | contents | pages [3] -->
7

<!-- b000065 | contents | pages [3] -->
Single Anchor Point: Centroid Method

<!-- b000066 | contents | pages [3] -->
14

<!-- b000067 | contents | pages [3] -->
15

<!-- b000068 | contents | pages [3] -->
15

<!-- b000069 | contents | pages [3] -->
Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000070 | contents | pages [3] -->
7.1

<!-- b000071 | contents | pages [3] -->
16

<!-- b000072 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000073 | contents | pages [3] -->
7.2

<!-- b000074 | contents | pages [3] -->
Results and Analysis

<!-- b000075 | contents | pages [3] -->
19

<!-- b000076 | contents | pages [3] -->
Extensions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [3] -->
7.3

<!-- b000078 | contents | pages [3] -->
8

<!-- b000079 | contents | pages [3] -->
Multiple Anchor Points: Cluster Method

<!-- b000080 | contents | pages [3] -->
21

<!-- b000081 | contents | pages [3] -->
24

<!-- b000082 | contents | pages [3] -->
Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [3] -->
8.1

<!-- b000084 | contents | pages [3] -->
24

<!-- b000085 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000086 | contents | pages [3] -->
8.2

<!-- b000087 | contents | pages [3] -->
Results and Analysis

<!-- b000088 | contents | pages [3] -->
28

<!-- b000089 | contents | pages [3] -->
Possible Extensions of the Cluster Model

<!-- b000090 | contents | pages [3] -->
8.3

<!-- b000091 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [3] -->
34

<!-- b000093 | contents | pages [3] -->
The Final Predictor: Combining the Schemes

<!-- b000094 | contents | pages [3] -->
9

<!-- b000095 | contents | pages [3] -->
34

<!-- b000096 | contents | pages [3] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000097 | contents | pages [3] -->
9.1

<!-- b000098 | contents | pages [3] -->
Results and Analysis

<!-- b000099 | contents | pages [3] -->
36

<!-- b000100 | contents | pages [3] -->
Possible Extensions to the General Model . . . . . . . . . . . . . . . . . . . .

<!-- b000101 | contents | pages [3] -->
9.2

<!-- b000102 | contents | pages [3] -->
10 Conclusion

<!-- b000103 | contents | pages [3] -->
11 Executive Summary

<!-- b000104 | contents | pages [3] -->
References

<!-- b000105 | contents | pages [3] -->
38

<!-- b000106 | contents | pages [3] -->
40

<!-- b000107 | contents | pages [3] -->
42

<!-- b000108 | contents | pages [3] -->
44

<!-- b000109 | furniture | pages [4] -->
Team # 7507

<!-- b000110 | furniture | pages [4] -->
Page 3

<!-- b000111 | contents | pages [4] -->
1

<!-- b000112 | heading | pages [4] -->
Introduction

<!-- b000113 | prose | pages [4] -->
Crime analysis and prediction is an old human practice. Rachel Boba, in her chapter on the

<!-- b000114 | prose | pages [4] -->
‘History of Crime Analysis’ describes the Rancher in the old American West who “noticed that

<!-- b000115 | prose | pages [4] -->
he was losing one or two head of cattle from his grazing land every week.” Our Rancher begins

<!-- b000116 | prose | pages [4] -->
to notice that these cattle go missing only at night and from a certain ﬁeld. His detective-like

<!-- b000117 | prose | pages [4] -->
observations and intuition may have led him to respond in a way ﬁtting for the lone rancher:

<!-- b000118 | prose | pages [4] -->
watch at night with a gun or move the herd altogether.[1] Although primitive compared to our

<!-- b000119 | prose | pages [4] -->
popular notions of crime analysis (ala television shows like 24 and Numb3rs), the techniques of

<!-- b000120 | prose | pages [4] -->
the Rancher from the American West are the same as those employed today. Current criminol-

<!-- b000121 | prose | pages [4] -->
ogy theory posits that criminals behave in patterns that are deeply tied to environment, social

<!-- b000122 | prose | pages [4] -->
surroundings, and personal history. The goal of any crime analysis and prediction, whether

<!-- b000123 | prose | pages [4] -->
by the FBI of the present or the Rancher of the past, is fundamentally one of discovering and

<!-- b000124 | prose | pages [4] -->
exploiting patterns and is therefore an explicitly mathematical task.

<!-- b000125 | prose | pages [4] -->
The task of predicting a serial criminal’s next crime location is consequentially a problem of

<!-- b000126 | prose | pages [4] -->
ﬁnding and using patterns from that criminal’s crime history. There is an established literature

<!-- b000127 | prose | pages [4] -->
on geographic patterns in serial crime sequences that has shown a strong patterning of serial

<!-- b000128 | prose | pages [4] -->
crimes around an “anchor point” - locations of daily familiarity for individual serial criminals.

<!-- b000129 | prose | pages [4] -->
We build two prediction schemes based on this underlying theory of anchor points in order to

<!-- b000130 | prose | pages [4] -->
predict future crime geography . Both schemes are given an ordered sequence of past crime

<!-- b000131 | prose | pages [4] -->
locations and then produce a surface of likelihood values and a robust metric. The surface

<!-- b000132 | prose | pages [4] -->
produced is equivalent to a geographic proﬁle of potential crime locations. The schemes differ

<!-- b000133 | prose | pages [4] -->
in their underlying assumption of the number of anchor points.

<!-- b000134 | prose | pages [4] -->
The ﬁrst scheme ﬁnds a single anchor point using a center of mass method and uses it to

<!-- b000135 | prose | pages [4] -->
predict likely future crime locations. The second scheme assumes two to four anchor points

<!-- b000136 | prose | pages [4] -->
and uses a cluster ﬁnding algorithm to sort and group points. These clusters are used to predict

<!-- b000137 | prose | pages [4] -->
likely future crime locations. Both schemes use a statistical technique we call cratering to

<!-- b000138 | prose | pages [4] -->
predict future crime locations. The comparison and eventual choice/rejection of a scheme will

<!-- b000139 | prose | pages [4] -->
use an algorithm based on our effectiveness multiplier.

<!-- b000140 | prose | pages [4] -->
The strength of our model is its close connection to the research that surrounds serial

<!-- b000141 | prose | pages [4] -->
crimes. We will see that for the several sample serial crime sequences, our ﬁnal prediction

<!-- b000142 | prose | pages [4] -->
algorithm provides a result that is honest about when it preforms well and honest when the

<!-- b000143 | prose | pages [4] -->
underlying data does not ﬁt the pattern at the heart of our model. Our end goal is not to beat

<!-- b000144 | prose | pages [4] -->
the intuitive cop, but we believe that this algorithm detects and utilizes underlying serial crime

<!-- b000145 | prose | pages [4] -->
patterns in a way that can drastically reduce the resources needed to help curb the devastating

<!-- b000146 | prose | pages [4] -->
effects of a serial criminal.

<!-- b000147 | furniture | pages [5] -->
Team # 7507

<!-- b000148 | furniture | pages [5] -->
Page 4

<!-- b000149 | prose | pages [5] -->
2

<!-- b000150 | heading | pages [5] -->
Background

<!-- b000151 | prose | pages [5] -->
When Peter Sutcliffe was arrested in Shefﬁeld, England, on suspicion of being the man be-

<!-- b000152 | prose | pages [5] -->
hind the so-called “Yorkshire Ripper killings,” the nature of quantitative criminology changed

<!-- b000153 | prose | pages [5] -->
forever. The arrest (and subsequent conviction) of Sutcliffe marked a personal victory for Stu-

<!-- b000154 | prose | pages [5] -->
art Kind, the forensic biologist whose ground-breaking application of mathematical principles

<!-- b000155 | prose | pages [5] -->
had successfully predicted that the Yorkshire Ripper lived between the towns of Shettley and

<!-- b000156 | prose | pages [5] -->
Bingley. More importantly, however, this success in early 1981 marked the beginning of three

<!-- b000157 | prose | pages [5] -->
decades of research developing increasingly-powerful methods of analyzing criminal patterns

<!-- b000158 | prose | pages [5] -->
with mathematics.[4]

<!-- b000159 | prose | pages [5] -->
Kind certainly was not the ﬁrst to put mathematics in the hands of police ofﬁcers; indeed

<!-- b000160 | prose | pages [5] -->
the use of statistical techniques to improve a law enforcement agency’s understanding of crim-

<!-- b000161 | prose | pages [5] -->
inal patterns has existed since at least 1847, when the Metropolitan Police of London began

<!-- b000162 | prose | pages [5] -->
tracking yearly aggregate levels of various crimes.[1] These techniques have gradually grown

<!-- b000163 | prose | pages [5] -->
in sophistication to the present day, and now, information-intensive models can be constructed

<!-- b000164 | prose | pages [5] -->
using heat map techniques to identify the hot spots for a speciﬁc type of crime, or to derive cor-

<!-- b000165 | prose | pages [5] -->
relations between the rate of criminal activity and the various attributes of a location (such as

<!-- b000166 | prose | pages [5] -->
lighting, urbanization, etc.)[1] Although, by 1980, such techniques in forecasting trends in gen-

<!-- b000167 | prose | pages [5] -->
eral categories of crime, committed by many, unconnected individuals were familiar to crime

<!-- b000168 | prose | pages [5] -->
analysts, Kind’s approach took the practice of mixing computations and crime-prevention into a

<!-- b000169 | prose | pages [5] -->
new realm by applying algorithmic analysis to the criminal acts of a single, serial offender.[15]

<!-- b000170 | prose | pages [5] -->
Since Kind’s groundbreaking calculation, the practice of “geographically proﬁling” the

<!-- b000171 | prose | pages [5] -->
crimes of a single criminal has produced a substantial body of research, principally focused

<!-- b000172 | prose | pages [5] -->
upon techniques for locating the criminal’s “anchor points”– locations (such as a home, work-

<!-- b000173 | prose | pages [5] -->
place, or a relative’s house) at which he spends substantial amounts of time and to which he

<!-- b000174 | prose | pages [5] -->
returns regularly between crimes. This is can be a difﬁcult proposition, as narrowing the focus

<!-- b000175 | prose | pages [5] -->
to one individual offender reduces the number of available data points substantially. In gen-

<!-- b000176 | prose | pages [5] -->
eral, therefore, these techniques exploit experimentally validated correlations between bases of

<!-- b000177 | prose | pages [5] -->
apprehended serial criminals and the areas where they committed their crimes.

<!-- b000178 | prose | pages [5] -->
Canter and Larkin (1993), for example, proposed that a serial criminal’s home (or other

<!-- b000179 | prose | pages [5] -->
anchor point) tends to be contained within a circle constructed such that its diameter is the line

<!-- b000180 | prose | pages [5] -->
segment between the two crime locations with the greatest distance between them. Further

<!-- b000181 | prose | pages [5] -->
studies have shown that this is indeed true in the vast majority of cases, particularly for violent

<!-- b000182 | prose | pages [5] -->
serial criminals like rapists and murderers. [8] Observations like these can be used to create

<!-- b000183 | prose | pages [5] -->
algorithms which prioritize the areas needing to be searched in order to ﬁnd the criminal’s

<!-- b000184 | prose | pages [5] -->
home or base; Canter et. al. (2000) ﬁnd that (for the speciﬁc case of serial murders), these

<!-- b000185 | furniture | pages [6] -->
Team # 7507

<!-- b000186 | furniture | pages [6] -->
Page 5

<!-- b000187 | prose | pages [6] -->
techniques on average reduce the area to be searched by nearly a factor of 10.[2]

<!-- b000188 | prose | pages [6] -->
By contrast, the practice of forecasting where a criminal will strike next has not been ex-

<!-- b000189 | prose | pages [6] -->
plored deeply in quantitative criminology literature[15]. Indeed, predicting where, say, a serial

<!-- b000190 | prose | pages [6] -->
rapist will strike next may require (in addition to an uncomfortable level of clinical detachment

<!-- b000191 | prose | pages [6] -->
from the past victims), a far more complex set of inputs, as it is far less clear what information

<!-- b000192 | prose | pages [6] -->
might inform the criminals decision about where to strike.

<!-- b000193 | prose | pages [6] -->
Naively, one might be tempted to simply generate a heat map of rape incidents in the rapists

<!-- b000194 | prose | pages [6] -->
region of activity, and predict that the next strike will occur where the most rapes have occurred

<!-- b000195 | prose | pages [6] -->
before. Clearly, however, this approach essentially discards all previous information about the

<!-- b000196 | prose | pages [6] -->
modus operandi of the criminal in question, whose individual pattern of strikes may differ

<!-- b000197 | prose | pages [6] -->
substantially from the aggregate behavior of previous rapists. Paulsen and Robinson (2009)

<!-- b000198 | prose | pages [6] -->
also observe that for many departments there are substantial practical, ethical, and legal issues

<!-- b000199 | prose | pages [6] -->
involved in collecting the data for a detailed mapping of criminal tendencies, with the result

<!-- b000200 | prose | pages [6] -->
that only 16% of local police departments in the United States employ a computerized mapping

<!-- b000201 | prose | pages [6] -->
technique.

<!-- b000202 | prose | pages [6] -->
A more sophisticated technique could map a wide variety of variables from lighting levels

<!-- b000203 | prose | pages [6] -->
or proximity to bars, and seek to correlate the rapists previous strikes to whichever variables

<!-- b000204 | prose | pages [6] -->
appear most signiﬁcant. But this too has its drawbacks, for in this low-statistics environment,

<!-- b000205 | prose | pages [6] -->
it is not at all clear that a sufﬁciently strong correlation could be found.

<!-- b000206 | prose | pages [6] -->
Furthermore, this method only exacerbates the practical problems of data collection, po-

<!-- b000207 | prose | pages [6] -->
tentially requiring police ofﬁcers to trawl the streets with clipboards subjectively evaluating

<!-- b000208 | prose | pages [6] -->
dozens of criteria at each city block. While a computer model might indeed produce valuable

<!-- b000209 | prose | pages [6] -->
output once this encyclopedic compendium of data was compiled, we suspect in many cases

<!-- b000210 | prose | pages [6] -->
that a highly trained ofﬁcer who is familiar with the ins and outs of his city could likely in-

<!-- b000211 | prose | pages [6] -->
tuit a similar result at a reduced cost. Rossmo (1987), for example, describes the case of one

<!-- b000212 | prose | pages [6] -->
Richard Ramirez, who raped or killed 33 individuals in the mid-eighties and “seemed to tar-

<!-- b000213 | prose | pages [6] -->
get single-story houses painted in light, pastel colors.” Naturally, all but the most egregiously

<!-- b000214 | prose | pages [6] -->
detailed mapping schemes would fail to identify this pattern computationally, whereas an alert

<!-- b000215 | prose | pages [6] -->
policeman might well notice it instantly.

<!-- b000216 | prose | pages [6] -->
Our treatment of the problem will therefore employ an approach more akin to the anchor

<!-- b000217 | prose | pages [6] -->
point ﬁnding algorithms described above. By examining experimentally conﬁrmed trends in

<!-- b000218 | prose | pages [6] -->
the relationships between crime locations (and between crime locations and estimated anchor

<!-- b000219 | prose | pages [6] -->
points), we generate likelihood surfaces which effectively act as a prioritization scheme for

<!-- b000220 | prose | pages [6] -->
regions which should be monitored or patrolled more aggressively in hopes of intercepting the

<!-- b000221 | prose | pages [6] -->
next crime.

<!-- b000222 | furniture | pages [7] -->
Team # 7507

<!-- b000223 | furniture | pages [7] -->
Page 6

<!-- b000224 | prose | pages [7] -->
3

<!-- b000225 | heading | pages [7] -->
Assumptions

<!-- b000226 | prose | pages [7] -->
As with any numerical model, we will make use of a number of simplifying assumptions in

<!-- b000227 | prose | pages [7] -->
order to make it mathematically tractable. In general, however, we ﬁnd that these assumptions

<!-- b000228 | prose | pages [7] -->
are not only computationally necessary, but also justiﬁed by empirical research or by the practi-

<!-- b000229 | prose | pages [7] -->
cal considerations of implementing this model as a law enforcement tool. Generally speaking,

<!-- b000230 | prose | pages [7] -->
these assumptions can be summarized in two groups:

<!-- b000231 | prose | pages [7] -->
3.1 Domain is Approximately Urban

<!-- b000232 | prose | pages [7] -->
Here, we are not literally requiring that the criminal in question operates in lower Manhattan.

<!-- b000233 | prose | pages [7] -->
We use the word “urban” because there are certain properties of a highly urbanized area which

<!-- b000234 | prose | pages [7] -->
substantially simplify our modeling treatment: namely, that the entire domain is a potential

<!-- b000235 | prose | pages [7] -->
crime spot, that the movement of the criminal is completely uninhibited, and that the area in

<!-- b000236 | prose | pages [7] -->
question is large enough to contain all possible strike points. It is important to note, however,

<!-- b000237 | prose | pages [7] -->
that even for serial crime committed in suburbs, villages, or spread between towns, the urban-

<!-- b000238 | prose | pages [7] -->
ization condition holds on the subset of the map in which crimes are regularly committed. To

<!-- b000239 | prose | pages [7] -->
see this, consider the three urbanization conditions separately:

<!-- b000240 | prose | pages [7] -->
3.1.1 Entire Domain is a Potential Crime Spot

<!-- b000241 | prose | pages [7] -->
Put more technically, we assume the potential targets of the criminal are dense within the do-

<!-- b000242 | prose | pages [7] -->
main of interest; that is, that any neighborhood selected within the map will contain a possible

<!-- b000243 | prose | pages [7] -->
crime location. Naturally, a continuous version of this condition would not actually be sat-

<!-- b000244 | prose | pages [7] -->
isﬁed by any physical city, but when we discretized our model, taking the minimum area of

<!-- b000245 | prose | pages [7] -->
interest to be about the size of a city block, then (particularly for violent crimes, where the

<!-- b000246 | prose | pages [7] -->
targets are any human being), it is hardly unreasonable that each block contains a potential tar-

<!-- b000247 | prose | pages [7] -->
get. Indeed, an equivalent assumption is present in nearly all the existing geographic proﬁling

<!-- b000248 | prose | pages [7] -->
techniques.[2][15]

<!-- b000249 | prose | pages [7] -->
It is obvious that every domain will violate these conditions to some extent: All but the

<!-- b000250 | prose | pages [7] -->
most inventive serial killers, for example, will not commit a crime in the middle of a lake, or in

<!-- b000251 | prose | pages [7] -->
the uninhabited farmland between small towns. Nevertheless, this observation simply requires

<!-- b000252 | prose | pages [7] -->
that the output of the model be interpreted intelligently. In other words, while we assume for

<!-- b000253 | prose | pages [7] -->
simplicity that the entire map is a potential target, police ofﬁcers interpreting the results can

<!-- b000254 | prose | pages [7] -->
easily ignore any predictions we make which fall into an obvious “dead zone.”

<!-- b000255 | furniture | pages [8] -->
Team # 7507

<!-- b000256 | furniture | pages [8] -->
Page 7

<!-- b000257 | prose | pages [8] -->
3.1.2 Criminal’s Movement is Uninhibited

<!-- b000258 | prose | pages [8] -->
This assumption is required for us to compute distances using a simple L2 norm. As we shall

<!-- b000259 | prose | pages [8] -->
discuss, many of our predictions are based upon observations about how far a criminal tends

<!-- b000260 | prose | pages [8] -->
to travel to commit a crime. Since these observations are meant to reﬂect the actual experi-

<!-- b000261 | prose | pages [8] -->
ences of the killer, one might imagine that if the “as the crow ﬂies” distance between, say, the

<!-- b000262 | prose | pages [8] -->
criminal’s home and place of attack were appreciably different from the “real-world” distance

<!-- b000263 | prose | pages [8] -->
along roads and highways, the latter would be a more reasonable measure. Finding this data,

<!-- b000264 | prose | pages [8] -->
however, quickly becomes quite difﬁcult as the scope of the crimes scales up (even in the age of

<!-- b000265 | prose | pages [8] -->
GoogleMaps), and so we invoke the so called “Manhattan assumption”: that there are enough

<!-- b000266 | prose | pages [8] -->
streets and sidewalks, laid out in a sufﬁciently grid-like pattern, that the criminals movements

<!-- b000267 | prose | pages [8] -->
around the map following real-world movement routes is the same as “straight line” movement

<!-- b000268 | prose | pages [8] -->
in a space discretized into areas of city blocks.[15]

<!-- b000269 | prose | pages [8] -->
Moreover, there is some evidence to suggest that considering real-world travel times is not

<!-- b000270 | prose | pages [8] -->
beneﬁcial. Kent et. al. (2006) demonstrated that, across several types of serial crime, the use

<!-- b000271 | prose | pages [8] -->
of real-world distance instead of Euclidean or “Manhattan” distance, actually performs more

<!-- b000272 | prose | pages [8] -->
poorly in predicting criminal anchor points, and that the Euclidean and Manhattan distances are

<!-- b000273 | prose | pages [8] -->
essentially interchangeable. Although our model is concerned with predicting the next crime

<!-- b000274 | prose | pages [8] -->
site rather than the anchor points, the methods employed have the same theoretical basis, and

<!-- b000275 | prose | pages [8] -->
thus, based on this evidence, we can safely take the L2 norm of points when generating data

<!-- b000276 | prose | pages [8] -->
about distances.

<!-- b000277 | prose | pages [8] -->
3.1.3 Domain Contains All Possible Strike Points

<!-- b000278 | prose | pages [8] -->
This condition, perhaps the most trivial of the three, simply says that the two conditions above

<!-- b000279 | prose | pages [8] -->
hold on a sufﬁciently large area that they will still hold wherever the criminal may strike next.

<!-- b000280 | prose | pages [8] -->
Put another way, if out model ever predicts that the next strike will be outside the initially

<!-- b000281 | prose | pages [8] -->
considered area, we will expand our total examined area until this is not so, implicitly assuming

<!-- b000282 | prose | pages [8] -->
that the targets continue to be dense and movement is still uninhibited.

<!-- b000283 | prose | pages [8] -->
To ensure this, we simply look to make sure that our likelihood surfaces decay sufﬁciently

<!-- b000284 | prose | pages [8] -->
at the boundary of the region being mapped, expanding the region if this is not so.

<!-- b000285 | prose | pages [8] -->
Taken together, these three conditions describe the region of interest as a metric space in which

<!-- b000286 | prose | pages [8] -->
1. The subset of potential targets is dense,

<!-- b000287 | prose | pages [8] -->
2. The metric is the L2 norm, and

<!-- b000288 | furniture | pages [9] -->
Team # 7507

<!-- b000289 | furniture | pages [9] -->
Page 8

<!-- b000290 | prose | pages [9] -->
3. The space is “complete” in the rough sense that sequences of crimes do not lead to

<!-- b000291 | prose | pages [9] -->
predictions of crimes which lie outside the metric space.

<!-- b000292 | prose | pages [9] -->
3.2 Violent Serial Crimes by a Single Offender

<!-- b000293 | prose | pages [9] -->
Naturally, in addition to making assumptions about the map space in which the criminal moves,

<!-- b000294 | prose | pages [9] -->
we must make assumptions about the criminal himself in order to attempt to anticipate his

<!-- b000295 | prose | pages [9] -->
behavior. To do so, we focus the scope to violent crimes, develop a deﬁnition for “serial,” and

<!-- b000296 | prose | pages [9] -->
assume all crimes were committed by the same offender.

<!-- b000297 | prose | pages [9] -->
3.2.1 Focus on Violent Crimes

<!-- b000298 | prose | pages [9] -->
Empirical research has consistently shown that geographic proﬁling is most successful for mur-

<!-- b000299 | prose | pages [9] -->
ders and rapes, with the average anchor point prediction algorithm being 30% less effective for

<!-- b000300 | prose | pages [9] -->
criminals who are serial burglars or arsonists.[15][2] It is easy to imagine reasons why this

<!-- b000301 | prose | pages [9] -->
might be the case: an arsonist who sets ﬁre to churches, for example, violates the “dense-

<!-- b000302 | prose | pages [9] -->
ness” assumption described above, as does a burglar who targets electronics stores. While a

<!-- b000303 | prose | pages [9] -->
“generic” residential burglar would still satisfy this assumption, the very fact that his behavior

<!-- b000304 | prose | pages [9] -->
is “generic” suggests simple heat-mapping of burglary might be more apt.

<!-- b000305 | prose | pages [9] -->
Those employing our model may of course use it to predict the strike points of nonviolent

<!-- b000306 | prose | pages [9] -->
offenders, but should only do so when a qualitative reason exists to suspect the criminal will

<!-- b000307 | prose | pages [9] -->
behave like a serial killer or rapist.

<!-- b000308 | prose | pages [9] -->
3.2.2 Serial Crimes

<!-- b000309 | prose | pages [9] -->
Quite simply, we assume we are predicting only the behavior of serial offenders. Contemporary

<!-- b000310 | prose | pages [9] -->
literature most commonly deﬁnes a serial killing as the murder of “three or more people over a

<!-- b000311 | prose | pages [9] -->
period of 30 or more days, with a signiﬁcant cooling-off period between the murders.”[6] We

<!-- b000312 | prose | pages [9] -->
will deﬁne “serial violent crime” equivalently, as three or more assaults, rapes, and/or murders

<!-- b000313 | prose | pages [9] -->
over 30 or more days, with a cooling off period that is on the order of one ore more days.

<!-- b000314 | prose | pages [9] -->
In this way, we exclude the murder or assault of multiple people in one mass “event” (like a

<!-- b000315 | prose | pages [9] -->
school shooting or a suicide bombing) from which there is no particular reason to project future

<!-- b000316 | prose | pages [9] -->
crimes.

<!-- b000317 | prose | pages [9] -->
This also means that, whenever inputting data points in our model, two or more events

<!-- b000318 | prose | pages [9] -->
whose spatial-temporal separation is far smaller the average for the data set with high statis-

<!-- b000319 | prose | pages [9] -->
tical signiﬁcance (p > 0.01), should be coded as one single event.[15]

<!-- b000320 | furniture | pages [10] -->
Team # 7507

<!-- b000321 | furniture | pages [10] -->
Page 9

<!-- b000322 | prose | pages [10] -->
3.2.3 Single Offender

<!-- b000323 | prose | pages [10] -->
Finally, we must assume that there is only one actor involved in the killings. There is some

<!-- b000324 | prose | pages [10] -->
leeway, of course, in the interpretation of the word “actor”; some sources consider two or more

<!-- b000325 | prose | pages [10] -->
individuals acting with collective intent to be a single “actor” for the purposes of geographic

<!-- b000326 | prose | pages [10] -->
proﬁling.[15]. For the purposes of our model, if multiple individuals committing the crimes are

<!-- b000327 | prose | pages [10] -->
truly acting with the same shared mindset, we should be able to project their next strike with

<!-- b000328 | prose | pages [10] -->
the same level of conﬁdence. What is more important to note is that the model treats all input

<!-- b000329 | prose | pages [10] -->
data points as crimes which were deﬁnitively committed by the same person. Consequently,

<!-- b000330 | prose | pages [10] -->
it is inadvisable to include a crime which “might have been the work of the serial criminal”

<!-- b000331 | prose | pages [10] -->
solely for the purposes of improving statistics.

<!-- b000332 | prose | pages [10] -->
3.3 Spatial Focus

<!-- b000333 | prose | pages [10] -->
While some research in the temporal patterns of serial criminals exists, research seems that the

<!-- b000334 | prose | pages [10] -->
best predictor of future geographic crime location is past geographic data. Temporal data is

<!-- b000335 | prose | pages [10] -->
problematic for use in our model for several key reasons.

<!-- b000336 | prose | pages [10] -->
1. While research has found cyclical patterns within the time between crimes, these patterns

<!-- b000337 | prose | pages [10] -->
don’t correlate directly to predicting the next geographic location. What is useful is

<!-- b000338 | prose | pages [10] -->
general trends in spacial movement over an ordering of the locations. We will utilize this

<!-- b000339 | prose | pages [10] -->
in our model by ignoring the speciﬁc time data that is present in crime sets, using this

<!-- b000340 | prose | pages [10] -->
information only to develop an ordering within the crime sequence itself.

<!-- b000341 | prose | pages [10] -->
2. For the most violent of serial crimes (murder, rape/murder), time data can be incredibly

<!-- b000342 | prose | pages [10] -->
inaccurate. While it is generally good enough to establish an ordering in the time se-

<!-- b000343 | prose | pages [10] -->
quence, the dates and times of murders are usually discerned from the remnants of body

<!-- b000344 | prose | pages [10] -->
dumps. While rape cases generally have clear time stamps, we use only an ordering of

<!-- b000345 | prose | pages [10] -->
the data to stay inclusive over the set of violent crimes which we want our model to

<!-- b000346 | prose | pages [10] -->
address.

<!-- b000347 | prose | pages [10] -->
4 Developing a Serial Crime Test Set

<!-- b000348 | prose | pages [10] -->
4.1 The Scarcity of Source Data

<!-- b000349 | prose | pages [10] -->
Finding representative and accurate data is a unique challenge within the development process

<!-- b000350 | prose | pages [10] -->
of any algorithm. Testing our models accuracy in predicting actual crimes is is an obvious best

<!-- b000351 | furniture | pages [11] -->
Team # 7507

<!-- b000352 | furniture | pages [11] -->
Page 10

<!-- b000353 | prose | pages [11] -->
practice before proposing a method to an agency that plans to utilize these techniques in real

<!-- b000354 | prose | pages [11] -->
life serial cases.

<!-- b000355 | prose | pages [11] -->
4.1.1 Existing Crime Sets

<!-- b000356 | prose | pages [11] -->
The most prominent researchers within the ﬁeld have built large databases of serial crimes to

<!-- b000357 | prose | pages [11] -->
use in their own evaluations (Rossmos FBI and SFU databases[15], LeBeaus San Diego Rape

<!-- b000358 | prose | pages [11] -->
Case data-set[9], or Canter’s Baltimore crime set[2]). Each of these databases was developed

<!-- b000359 | prose | pages [11] -->
with speciﬁc methods of integrity and speciﬁc source locations. For example, Rossmo devel-

<!-- b000360 | prose | pages [11] -->
ops a data set of serial murderers using an FBI source (created using newspaper and media

<!-- b000361 | prose | pages [11] -->
information). Rossmo then combs this data for cases where a set of criterion is used to elimi-

<!-- b000362 | prose | pages [11] -->
nate weakly justiﬁed and inapplicable data.[13]. Other databases are generated using the crime

<!-- b000363 | prose | pages [11] -->
reports of local police forces.[9]

<!-- b000364 | prose | pages [11] -->
The difﬁculty in our own search is that the databases found in our literature review are

<!-- b000365 | prose | pages [11] -->
all private and proprietary. Additionally, the resources that used police department data were

<!-- b000366 | prose | pages [11] -->
working directly with departments to gain access to this information. This meant practically

<!-- b000367 | prose | pages [11] -->
that no established data source was directly available for our algorithmic analysis. Here we

<!-- b000368 | prose | pages [11] -->
are faced with two options: simulate serial criminal data or ﬁnd an indirect way of using the

<!-- b000369 | prose | pages [11] -->
private data.

<!-- b000370 | prose | pages [11] -->
4.1.2 The Problem with Simulation

<!-- b000371 | prose | pages [11] -->
Simulation (by computer, not employed serial criminal) might seem like an initially attrac-

<!-- b000372 | prose | pages [11] -->
tive solution to the low level of data available. However, a brief examination of the types of

<!-- b000373 | prose | pages [11] -->
simulated data one might produce provides motivation to use another source of data.

<!-- b000374 | prose | pages [11] -->
1. The easiest simulation of crime data would be a random crime site generation within a

<!-- b000375 | prose | pages [11] -->
given space. This would be unhelpful in general however because the basic assumption

<!-- b000376 | prose | pages [11] -->
underlying our approach is that serial crimes are strongly connected to spatial patterns.

<!-- b000377 | prose | pages [11] -->
A randomly generated crime set violates this basic assumption and seems to contradict

<!-- b000378 | prose | pages [11] -->
the large amount of research in environmental patterns in crime.

<!-- b000379 | prose | pages [11] -->
2. The next intuitive approach might be to generate the crime sequence using an underlying

<!-- b000380 | prose | pages [11] -->
distribution supported by research. For example, one might generate a series of crimes

<!-- b000381 | prose | pages [11] -->
using a journey to crime model or some periodic model. Many of these such models

<!-- b000382 | prose | pages [11] -->
could be found in the criminal psychology research. The problem with this approach

<!-- b000383 | prose | pages [11] -->
is subtle. While certainly having a model of how criminals choose crime sites is both

<!-- b000384 | prose | pages [11] -->
intelligent and inherently necessary in the problem of spatial prediction, the predictive

<!-- b000385 | furniture | pages [12] -->
Team # 7507

<!-- b000386 | furniture | pages [12] -->
Page 11

<!-- b000387 | prose | pages [12] -->
algorithm will also be based on this model. this means that both the predictive algorithm

<!-- b000388 | prose | pages [12] -->
and the generated criminal data will be created from the same model and will therefore

<!-- b000389 | prose | pages [12] -->
give a false conﬁdence in the chosen algorithm. Actual criminal data must be used if

<!-- b000390 | prose | pages [12] -->
there is to be any conﬁdence in the underlying assumptions made when creating a model.

<!-- b000391 | prose | pages [12] -->
4.2 An Alternative: Pixel Point Analysis

<!-- b000392 | prose | pages [12] -->
With these limitations in mind, we decided that the best approach to developing a set of crime

<!-- b000393 | prose | pages [12] -->
series sequences in the absence of an actual explicit data set would be to “mine” the data types

<!-- b000394 | prose | pages [12] -->
that are available. The clearest spacial (and sometimes temporal) occurrence of serial crime

<!-- b000395 | prose | pages [12] -->
data is represented as scatter plots in Journey-to-Crime research (see Figure 1). While this data

<!-- b000396 | prose | pages [12] -->
is not numerically explicit, it is the closest we found to direct data. The two sources of the

<!-- b000397 | prose | pages [12] -->
crime sequences are found in a Ph.D. thesis by Rossmo[13] and a spatial analysis of journey-

<!-- b000398 | prose | pages [12] -->
to-crime patterns in serial rape cases by LeBeau[9]. To translate this pictorial representation

<!-- b000399 | prose | pages [12] -->
of a crime sequence, pixel point analysis was used to scale the raster coordinate to a meter

<!-- b000400 | prose | pages [12] -->
coordinate. Although there is a small error in this scaling due to pixel representation, the error

<!-- b000401 | prose | pages [12] -->
is smaller than the discretization that we use in our own models. This process was applied

<!-- b000402 | prose | pages [12] -->
to seven different criminals’ crime data. Four of these are serial killer sequences and three

<!-- b000403 | prose | pages [12] -->
are serial rape sequences. The serial rape sequences have an explicit ordering while the serial

<!-- b000404 | prose | pages [12] -->
murder sequences are unordered.

<!-- b000405 | prose | pages [12] -->
We note several strengths of this approach to further justify our choice of pixel data over

<!-- b000406 | prose | pages [12] -->
simulation. First and most importantly, this data is already combed for inconsistency by the

<!-- b000407 | prose | pages [12] -->
researchers and ﬁts both our deﬁnitions of serial crime and the basic assumptions. The consid-

<!-- b000408 | prose | pages [12] -->
erations and rules in data mining are complex and numerous. Using data that has already been

<!-- b000409 | prose | pages [12] -->
deemed appropriate for serial crime analysis by leaders in the ﬁeld is clearly superior to trying

<!-- b000410 | prose | pages [12] -->
to mine or simulate data ourselves. Additionally, the data presented in the papers has been

<!-- b000411 | prose | pages [12] -->
chosen to represent the range of possible patterns and scales within serial crimes. This means

<!-- b000412 | prose | pages [12] -->
that our algorithm is being tested over a semi-representative set of data. We also incorporate

<!-- b000413 | prose | pages [12] -->
two types of violent serial crime to add robustness in our testing.

<!-- b000414 | prose | pages [12] -->
5 Metrics of Success: The Psychic and the Hairﬁnder

<!-- b000415 | prose | pages [12] -->
In a 1998 presentation to a conference of the Naval Criminal Investigative Service, Rossmo

<!-- b000416 | prose | pages [12] -->
recalled the investigation of the disappearance of a little girl named Mindy Tran. Tran’s ap-

<!-- b000417 | prose | pages [12] -->
parent abduction attracted a substantial amount of media attention and prompted a both a self-

<!-- b000418 | prose | pages [12] -->
described psychic woman and a man claiming to be a “hairﬁnder” to volunteer their services

<!-- b000419 | furniture | pages [13] -->
Team # 7507

<!-- b000420 | furniture | pages [13] -->
Page 12

<!-- b000421 | caption | pages [13] -->
Figure 1: Comparison of crime sequence for violent offender in LeBeau[9] and scatter plot of same

<!-- b000422 | prose | pages [13] -->
data found through pixel analysis.

<!-- b000423 | prose | pages [13] -->
to the local police

<!-- b000424 | prose | pages [13] -->
As Rossmo describes a hairﬁnder, “You have a little plastic ﬁlm canister and you take the

<!-- b000425 | prose | pages [13] -->
hair of the person you’re looking for and you put it in that plastic ﬁlm canister, you attach

<!-- b000426 | prose | pages [13] -->
that to a stick, and it takes you to the person you’re looking for.” [14] Nevertheless, when the

<!-- b000427 | prose | pages [13] -->
police sent the two out together (to “get rid of two nuts at once”), the psychic identiﬁed a park

<!-- b000428 | prose | pages [13] -->
to search, and the hairﬁnder wandered his way over to the body. In Rossmo’s words, “Those

<!-- b000429 | prose | pages [13] -->
people could put [crime proﬁlers] out of business” if their models are not better than random

<!-- b000430 | prose | pages [13] -->
chance.[14] We take this advice to heart, and insist that for a model to be successful, it must

<!-- b000431 | prose | pages [13] -->
outperform a random predictive algorithm or else it does more harm than good. In other words,

<!-- b000432 | prose | pages [13] -->
we must beat the psychic and the hairﬁnder.

<!-- b000433 | prose | pages [13] -->
5.1 The Effectiveness Multiplier

<!-- b000434 | prose | pages [13] -->
To quantify this condition (that we outperform a randomly-guessing team of pseudoscience

<!-- b000435 | prose | pages [13] -->
practitioners), we must deﬁne what it means to “outperform.” We suggest the following in-

<!-- b000436 | prose | pages [13] -->
tuitive deﬁnition: suppose a police department has a ﬁnite number of “resource” (cops, de-

<!-- b000437 | prose | pages [13] -->
tectives, community watch groups, etc) with which to attempt to intercept the criminal’s next

<!-- b000438 | prose | pages [13] -->
strike. In response to the output of any model they ﬁnd trustworthy, they should distribute their

<!-- b000439 | prose | pages [13] -->
resources such that the number of resources at any point is proportional to the supposed likeli-

<!-- b000440 | prose | pages [13] -->
hood of the criminal attempt to strike at that point. We say that one model outperforms another

<!-- b000441 | prose | pages [13] -->
if it recommends allocating more resources to the point where the next crime was actually

<!-- b000442 | furniture | pages [14] -->
Team # 7507

<!-- b000443 | furniture | pages [14] -->
Page 13

<!-- b000444 | prose | pages [14] -->
committed.

<!-- b000445 | prose | pages [14] -->
A logical next step is to ask how much a model outperforms another, which can simply

<!-- b000446 | prose | pages [14] -->
be done by taking the ratio of the amount of resources allocated at the crime point under the

<!-- b000447 | prose | pages [14] -->
ﬁrst model to the amount allocated under the second. When this ratio is greater than 1, the

<!-- b000448 | prose | pages [14] -->
ﬁrst metric outperforms the second, and vice-versa. Assuming that the police force is twice as

<!-- b000449 | prose | pages [14] -->
effective at a location when they have twice the resources allocated, we can think of this ratio

<!-- b000450 | prose | pages [14] -->
as an effectiveness multiplier, representing how many times more prepared to stop the criminal

<!-- b000451 | prose | pages [14] -->
the police will be under the ﬁrst model compared to the second. In this paper, effectiveness

<!-- b000452 | prose | pages [14] -->
ratios will be denoted by the symbol κ:

<!-- b000453 | prose | pages [14] -->
κ ≡resource allocation at crime point, model 1

<!-- b000454 | prose | pages [14] -->
resource allocation at crime point, model 2

<!-- b000455 | prose | pages [14] -->
Observe that if we normalize the integral of each likelihood plot to the total number of

<!-- b000456 | prose | pages [14] -->
resources available to the department in question, the equation above is simply a ratio of the

<!-- b000457 | prose | pages [14] -->
percentage of department resources allocated to the point, and since the total resources avail-

<!-- b000458 | prose | pages [14] -->
able are the same under both models, we can evaluate κ simply as

<!-- b000459 | prose | pages [14] -->
κ = Z1(CrimePoint)

<!-- b000460 | prose | pages [14] -->
Z2(CrimePoint)

<!-- b000461 | prose | pages [14] -->
where Zn is the likelihood function of model n and CrimePoint is the location of the actual

<!-- b000462 | prose | pages [14] -->
next crime. We note that though this information is obviously not available in most cases, we

<!-- b000463 | prose | pages [14] -->
use our metric by truncating a data sequence and using that set to predict the truncated crime.

<!-- b000464 | prose | pages [14] -->
Finally, note that since a randomly guessing algorithm, like an unconvincing psychic, will

<!-- b000465 | prose | pages [14] -->
have no reason to privilege any one point over another, averaging over a large number of

<!-- b000466 | prose | pages [14] -->
attempts to predict a crime location, their resource allocation appears the same as a model

<!-- b000467 | prose | pages [14] -->
which produces a perfectly ﬂat likelihood plot. This allows us to compare our model to a

<!-- b000468 | prose | pages [14] -->
random guess by computing a “standard effectiveness multiplier,” in which model 2 is assumed

<!-- b000469 | prose | pages [14] -->
to be a uniform, ﬂat distribution

<!-- b000470 | prose | pages [14] -->
Z1(CrimePoint) κs = Zflat(CrimePoint)

<!-- b000471 | prose | pages [14] -->
This standard effectiveness multiplier κs is the metric we will use to assess how well our

<!-- b000472 | prose | pages [14] -->
model performs. A value of exactly 1 indicated it is no better (on average) than a random guess,

<!-- b000473 | prose | pages [14] -->
and a fractional value would indicate we are actively misleading the police. The upper bound

<!-- b000474 | prose | pages [14] -->
of this number is simply the magnitude of the maximum potential striking area considered by

<!-- b000475 | prose | pages [14] -->
the model, which is achieved only if the model predicts the next crime point exactly and assigns

<!-- b000476 | prose | pages [14] -->
it 100% likelihood 1.

<!-- b000477 | prose | pages [14] -->
1Although much of the formalism developed around anchor point ﬁnding algorithms is applicable, this metric

<!-- b000478 | furniture | pages [15] -->
Team # 7507

<!-- b000479 | furniture | pages [15] -->
Page 14

<!-- b000480 | prose | pages [15] -->
5.2 Robustness of the Metric

<!-- b000481 | prose | pages [15] -->
Primarily, we use this metric to compare the effectiveness of different models when looking

<!-- b000482 | prose | pages [15] -->
at the same data set. In such a case, the metric is perfectly robust and needs no qualiﬁcation.

<!-- b000483 | prose | pages [15] -->
However, we will also want to compare the success of a single algorithm across multiple data-

<!-- b000484 | prose | pages [15] -->
sets, which introduces a slight problem. Clearly, the distribution of a ﬁxed resources under a

<!-- b000485 | prose | pages [15] -->
ﬂat likelihood plot depends on the area to be covered (i.e, if there are 100 cops to be deployed

<!-- b000486 | prose | pages [15] -->
over 10 city blocks, each receives 10 cops, but over 100 blocks each receives only 1). Our

<!-- b000487 | prose | pages [15] -->
algorithm, however, is not area dependent, and consequently, one can make κs arbitrarily large

<!-- b000488 | prose | pages [15] -->
by simply including more and more pointless area well outside the killer’s active region.

<!-- b000489 | prose | pages [15] -->
It is therefore only legitimate to compare κs values between two data sets between which

<!-- b000490 | prose | pages [15] -->
the ratio of the killer’s active region to the total area considered stays constant. Necessarily,

<!-- b000491 | prose | pages [15] -->
the size of the killer’s active region cannot be precisely known; however, we will employ a

<!-- b000492 | prose | pages [15] -->
standard technique to make this condition approximately true, based on one used by Canter

<!-- b000493 | prose | pages [15] -->
et. al. (2000) to assess algorithms which predict anchor points. From the ﬁndings of Canter

<!-- b000494 | prose | pages [15] -->
and Larkin (1993) and Paulsen (2005), we know that experimentally speaking that in more

<!-- b000495 | prose | pages [15] -->
than 90% of cases, all future crimes committed by an offender will fall within a square whose

<!-- b000496 | prose | pages [15] -->
side length is the maximum distance between previous crime points and whose center is the

<!-- b000497 | prose | pages [15] -->
centroid of the data.[3][11] For each of our test data-sets, we construct such a square and them

<!-- b000498 | prose | pages [15] -->
multiply each side length by 3, creating an overall search area which can very nearly be said

<!-- b000499 | prose | pages [15] -->
to be 9 times larger than the criminal’s active area. Since this ratio is now (nearly) constant

<!-- b000500 | prose | pages [15] -->
between the data sets, this will allow us to compare effectiveness multipliers between different

<!-- b000501 | prose | pages [15] -->
data-sets as well.

<!-- b000502 | prose | pages [15] -->
It is important to note that, since we have only three complete data sets on which to test

<!-- b000503 | prose | pages [15] -->
our model, our results are not generalizable to predict success or failure when applied to any

<!-- b000504 | prose | pages [15] -->
other serial crime cases, and we will not be able say with statistical signiﬁcance whether or not

<!-- b000505 | prose | pages [15] -->
we outperform a random guess. Instead, because the data-sets we do use were at least selected

<!-- b000506 | prose | pages [15] -->
to be as representative as possible of a typical violent serial crime, we will simply make some

<!-- b000507 | prose | pages [15] -->
qualitative assessments of success.

<!-- b000508 | prose | pages [15] -->
Notwithstanding our limited access to data, any police department with access to a sufﬁ-

<!-- b000509 | prose | pages [15] -->
ciently large number of sample serial crime cases (research suggests approximately n > 50)[2]

<!-- b000510 | prose | pages [15] -->
could easily employ the methods outlined above to test our algorithm, with the average effec-

<!-- b000511 | prose | pages [15] -->
of success is necessarily an exception. The conventional measure of an anchor-ﬁnder’s effectiveness is a “search

<!-- b000512 | prose | pages [15] -->
reduction factor,” which can be computed precisely because one can assume the police are sequentially searching

<!-- b000513 | prose | pages [15] -->
locations in order of descending likelihood (Canter, 2000). A strike-point predictor cannot make this assumption

<!-- b000514 | prose | pages [15] -->
(that is, it may instead be used to patrol many locations simultaneously in hopes of deterring the next crime), so

<!-- b000515 | prose | pages [15] -->
an alternative metric is called for.

<!-- b000516 | furniture | pages [16] -->
Team # 7507

<!-- b000517 | furniture | pages [16] -->
Page 15

<!-- b000518 | prose | pages [16] -->
tiveness multiplier serving as a representation of our model’s utility in a general case of serial

<!-- b000519 | prose | pages [16] -->
crime.

<!-- b000520 | prose | pages [16] -->
6 Two Schemes for Spatial Prediction

<!-- b000521 | prose | pages [16] -->
As discussed in the Background, the problem of predicting next crime location is not well

<!-- b000522 | prose | pages [16] -->
documented. The most common approach to analyzing a criminal crime sequence is to predict

<!-- b000523 | prose | pages [16] -->
a home location. The research literature on journey-to-crime research for violent serial crimes

<!-- b000524 | prose | pages [16] -->
strongly suggests that serial crime is patterned around a criminals home, workplace, or other

<!-- b000525 | prose | pages [16] -->
place of daily activity[15, 8, 4, 6, 17]. This has lead researchers to spend most of their resources

<!-- b000526 | prose | pages [16] -->
developing and evaluating methods of ﬁnding this crime center point. The centroid is then

<!-- b000527 | prose | pages [16] -->
investigated as an anchor point in the criminal’s daily activity. For the majority of research,

<!-- b000528 | prose | pages [16] -->
this anchor point is the serial criminal’s home. This method has been tested on large sets of

<!-- b000529 | prose | pages [16] -->
data and was found to reduce the necessary search area by a factor of ten.

<!-- b000530 | prose | pages [16] -->
Our schemes will use the strength of an anchor point ﬁnding algorithm to predict likely

<!-- b000531 | prose | pages [16] -->
locations of future crimes. The motivation is straightforward: if we know the location of an

<!-- b000532 | prose | pages [16] -->
anchor point and the pattern of crime location from this anchor point, we can generate an area

<!-- b000533 | prose | pages [16] -->
of future likely hood by projecting from the anchor point back to the crime points. It seems

<!-- b000534 | prose | pages [16] -->
that this conceptualization of patterning is more accurate than a direct forecasting scheme that

<!-- b000535 | prose | pages [16] -->
ignores anchor point behavior.

<!-- b000536 | prose | pages [16] -->
We develop two schemes with the base assumption of the existence of anchor point pat-

<!-- b000537 | prose | pages [16] -->
terning. The ﬁrst scheme assumes only a single anchor point. The second scheme assumes

<!-- b000538 | prose | pages [16] -->
multiple anchor points. These related schemes can then be used in combination to provide an

<!-- b000539 | prose | pages [16] -->
analysis of likely future crime locations.

<!-- b000540 | prose | pages [16] -->
7 Single Anchor Point: Centroid Method

<!-- b000541 | caption | pages [16] -->
Figure 2 is the algorithm used to predict likely crime locations using a single anchor point.

<!-- b000542 | prose | pages [16] -->
Because of the use of centroid to calculate the single anchor, we call this the centroid method

<!-- b000543 | prose | pages [16] -->
(although centroids will be used in both methods). Description of the algorithm and discussion

<!-- b000544 | prose | pages [16] -->
of its results are presented. The green blocks in the diagram represent extensions of the model

<!-- b000545 | prose | pages [16] -->
which will be discussed.

<!-- b000546 | furniture | pages [17] -->
Team # 7507

<!-- b000547 | furniture | pages [17] -->
Page 16

<!-- b000548 | prose | pages [17] -->
!"#$%#&'#$"()&*+,$-.&

<!-- b000549 | prose | pages [17] -->
/-.0&!#.%"+-0&+1&

<!-- b000550 | prose | pages [17] -->
!"-,#&'-%#2&

<!-- b000551 | prose | pages [17] -->
34-50&6-7#5-)++0& !"$%#"&

<!-- b000552 | prose | pages [17] -->
8942%&1+"& :#,;+"$5&:"#.02&

<!-- b000553 | prose | pages [17] -->
<#-=)%&>?& @"#A-+42&!"-,#2&

<!-- b000554 | prose | pages [17] -->
B4%;4%&6-7#5-)++02&!

<!-- b000555 | caption | pages [17] -->
Figure 2: Algorithm Flow Chart for Centroid Method

<!-- b000556 | prose | pages [17] -->
7.1

<!-- b000557 | heading | pages [17] -->
Algorithm

<!-- b000558 | prose | pages [17] -->
7.1.1 Create Search Domain

<!-- b000559 | prose | pages [17] -->
Bluntly put, we carefully construct the smallest square which will contain every previous crime,

<!-- b000560 | prose | pages [17] -->
then wildly scale up each dimension by a factor of 3. This ensures that all of our fundamental

<!-- b000561 | prose | pages [17] -->
assumptions about the underlying domain are satisﬁed, and the consistent scale factor of 3

<!-- b000562 | prose | pages [17] -->
allows us to compare the algorithm between data sets with different degrees of geographical

<!-- b000563 | prose | pages [17] -->
separation (recall Section 3 for justiﬁcation).

<!-- b000564 | prose | pages [17] -->
7.1.2 Find Centroid of Crime Sites

<!-- b000565 | prose | pages [17] -->
The anchor point of the crime sequence is determined by ﬁnding the “center of mass” of the

<!-- b000566 | prose | pages [17] -->
crime points. Each point is given a common weight making the computation an average of n

<!-- b000567 | prose | pages [17] -->
crime coordinates (xi, yi). The coordinate of the centroid is, simply,

<!-- b000568 | prose | pages [17] -->
" yi

<!-- b000569 | prose | pages [17] -->
!" xi

<!-- b000570 | prose | pages [17] -->
(˜x, ˜y) =

<!-- b000571 | prose | pages [17] -->
#

<!-- b000572 | prose | pages [17] -->
, n

<!-- b000573 | prose | pages [17] -->
n

<!-- b000574 | prose | pages [17] -->
While we choose to use the centroid to model the anchor point, this is not the only approach

<!-- b000575 | prose | pages [17] -->
taken in the literature. Speciﬁcally, Rossmo ﬁrst introduced the idea of placing distributions

<!-- b000576 | furniture | pages [18] -->
Team # 7507

<!-- b000577 | furniture | pages [18] -->
Page 17

<!-- b000578 | prose | pages [18] -->
(Gaussian or negative exponential) over each crime site. The sum of these produce a surface

<!-- b000579 | prose | pages [18] -->
of likely home sites (CGT Method)[15]. This method is more effective for determining likely

<!-- b000580 | prose | pages [18] -->
anchor point locations because it assigns values of ‘likelihood’ over the entire search, as op-

<!-- b000581 | prose | pages [18] -->
posed to the centroid method which gives one anchor point location. Since we use the centroid

<!-- b000582 | prose | pages [18] -->
only as a step to predicting crime locations (and not as a method for searching anchor points)

<!-- b000583 | prose | pages [18] -->
the singular output of the centroid approach makes more sense to use in our algorithm.

<!-- b000584 | prose | pages [18] -->
7.1.3 Building a Likelihood Crater

<!-- b000585 | prose | pages [18] -->
With the estimate of an anchor point location, we now predict future crime locations using

<!-- b000586 | prose | pages [18] -->
the “journey-to-crime” model within serial killer psychology. Again, this says that the serial

<!-- b000587 | prose | pages [18] -->
criminal’s spatial pattern of crime around an anchor point, in general, does not change. For

<!-- b000588 | prose | pages [18] -->
example, if a serial rapist commits his crimes 120 meters away from his home, on average, we

<!-- b000589 | prose | pages [18] -->
can predict that he will likely strike again within this distance from his home[17]. A rough and

<!-- b000590 | prose | pages [18] -->
ﬁrst pass prediction discussed in Paulsen’s 2005 conference proceedings might be to draw a

<!-- b000591 | prose | pages [18] -->
large shape (circle, square, polygon, etc) around this anchor point based on the largest distance

<!-- b000592 | prose | pages [18] -->
from a crime point to the anchor point. This prediction method was shown to be incredibly

<!-- b000593 | prose | pages [18] -->
ineffective against the largest circle guess described in the background[11].

<!-- b000594 | prose | pages [18] -->
We instead use a more effective cratering technique ﬁrst described in a home ﬁnd algorithm

<!-- b000595 | prose | pages [18] -->
by Rossmo. To do this, the two dimensional crime points xi are mapped to their radius from

<!-- b000596 | prose | pages [18] -->
the anchor point ai i.e. f : xi →ri where f(xi) = ∥xi −ai∥2 (a shifted modulus). The set ri is then used to generate a crater around the anchor point.

<!-- b000597 | prose | pages [18] -->
There are two dominating theories for the pattern serial crimes follow around an anchor

<!-- b000598 | prose | pages [18] -->
point. The ﬁrst says that there should be a buffer zone around the anchor point. A serial crimi-

<!-- b000599 | prose | pages [18] -->
nal, according to this theory, will commit crimes in an annulus centered at the anchor point[8].

<!-- b000600 | prose | pages [18] -->
This theory alone is often modeled using the positive portion of a Gaussian curve with parame-

<!-- b000601 | prose | pages [18] -->
ters mean and variance of {ri}. The other theory says that crimes follow a decaying exponential

<!-- b000602 | prose | pages [18] -->
pattern from the attractor point. Both theories have been substantiated by analysis on journey

<!-- b000603 | prose | pages [18] -->
to crime research. Yet we seek a distribution that would model either theory, depending on the

<!-- b000604 | prose | pages [18] -->
patterns displayed in the crime sequence. For this we turn to the ﬂexibility of the Γ-distribution.

<!-- b000605 | prose | pages [18] -->
Hogg et. al. note that the probability density function (pdf) for the Γ-distribution is a good

<!-- b000606 | prose | pages [18] -->
model “for many nonnegative random variables of the continuous type” due to the two ﬂexi-

<!-- b000607 | prose | pages [18] -->
ble parameters[5]. The Γ-distribution provides a compelling shape for our model: it offers a

<!-- b000608 | prose | pages [18] -->
“shifted-Gaussian” like behavior when points lie further away and a curve similar to a nega-

<!-- b000609 | prose | pages [18] -->
tive exponential when the parameters are small. Figure 3 displays two plots demonstrating the

<!-- b000610 | prose | pages [18] -->
ﬂexibility of the shape of the Γ-distribution.

<!-- b000611 | furniture | pages [19] -->
Team # 7507

<!-- b000612 | prose | pages [19] -->
pdf

<!-- b000613 | prose | pages [19] -->
2.0

<!-- b000614 | prose | pages [19] -->
1.5

<!-- b000615 | prose | pages [19] -->
1.0

<!-- b000616 | prose | pages [19] -->
0.5

<!-- b000617 | prose | pages [19] -->
0.5 1.0 1.5 2.0

<!-- b000618 | prose | pages [19] -->
(a) k = 1, θ = .5

<!-- b000619 | furniture | pages [19] -->
Page 18

<!-- b000620 | prose | pages [19] -->
pdf

<!-- b000621 | prose | pages [19] -->
0.020

<!-- b000622 | prose | pages [19] -->
0.015

<!-- b000623 | prose | pages [19] -->
0.010

<!-- b000624 | prose | pages [19] -->
0.005

<!-- b000625 | prose | pages [19] -->
r r

<!-- b000626 | prose | pages [19] -->
r 20 40 60 80 100

<!-- b000627 | prose | pages [19] -->
(b) k = 4, θ = 10

<!-- b000628 | caption | pages [19] -->
Figure 3: Example Γ probability density functions

<!-- b000629 | prose | pages [19] -->
Let us deﬁne the random variable X to be the radius between crime point and anchor point,

<!-- b000630 | prose | pages [19] -->
r. As stated in above, X ∼Γ(k, θ). For purposes of computing the estimators, we assume

<!-- b000631 | prose | pages [19] -->
independence of {X}. The two parameters of the Γ-distribution, k and θ, are determined using

<!-- b000632 | prose | pages [19] -->
the gamﬁt function in MatLab(2009). This routine uses the maximum likelihood estimators

<!-- b000633 | prose | pages [19] -->
(MLE) of the Γ-distribution to estimate the parameters. The MLE is found by ﬁrst noting that

<!-- b000634 | prose | pages [19] -->
independence gives us our likelihood function for a set of N {xn}

<!-- b000635 | prose | pages [19] -->
N $

<!-- b000636 | prose | pages [19] -->
N $

<!-- b000637 | prose | pages [19] -->
xk−1exp(−x/θ)

<!-- b000638 | prose | pages [19] -->
f(xi; k, θ) =

<!-- b000639 | prose | pages [19] -->
L(k, θ) = f(x; k, θ) =

<!-- b000640 | prose | pages [19] -->
i=1

<!-- b000641 | prose | pages [19] -->
Γ(k)θk

<!-- b000642 | prose | pages [19] -->
i=1

<!-- b000643 | prose | pages [19] -->
Taking the logarithm of this gives us the log-likelihood function

<!-- b000644 | prose | pages [19] -->
N %

<!-- b000645 | prose | pages [19] -->
ℓ(k, θ) = (k −1)

<!-- b000646 | prose | pages [19] -->
ln(xi) −

<!-- b000647 | prose | pages [19] -->
i=1

<!-- b000648 | prose | pages [19] -->
N N %

<!-- b000649 | prose | pages [19] -->
xi/θ −Nk ln(θ) −N ln Γ(k)

<!-- b000650 | prose | pages [19] -->
i=1

<!-- b000651 | prose | pages [19] -->
To ﬁnd the MLE for θ, ℓ(k, θ) is maximized with respect to θ and r:

<!-- b000652 | prose | pages [19] -->
1 ˆθ = kN

<!-- b000653 | prose | pages [19] -->
N N %

<!-- b000654 | prose | pages [19] -->
xi = x

<!-- b000655 | prose | pages [19] -->
k

<!-- b000656 | prose | pages [19] -->
i=1

<!-- b000657 | prose | pages [19] -->
There is no closed form solution for ˆr, and gamﬁt numerically solves for this MLE. One could

<!-- b000658 | prose | pages [19] -->
also use a Newton method to do this as described by Minka[10].

<!-- b000659 | prose | pages [19] -->
We use these parameters to ﬁt the Γ-distribution to our set of ri and then build the crater

<!-- b000660 | prose | pages [19] -->
of likely crime locations using this distribution. This is accomplished by computing r (the

<!-- b000661 | prose | pages [19] -->
distance from the point to the anchor point) at every point in the search region and evaluating

<!-- b000662 | prose | pages [19] -->
Γ function pdf with ﬁtted parameters at these values. We then normalize such that the sum of

<!-- b000663 | prose | pages [19] -->
our likelihood surface is exactly 1.

<!-- b000664 | prose | pages [19] -->
Applying this method to the set of crime locations of Peter Sutcliffe, the heat map shown

<!-- b000665 | prose | pages [19] -->
in Figure 4.

<!-- b000666 | furniture | pages [20] -->
Team # 7507

<!-- b000667 | furniture | pages [20] -->
Page 19

<!-- b000668 | caption | pages [20] -->
Figure 4: Heat Map showing cratering technique applied to the crime sequence of Peter Sutcliffe

<!-- b000669 | prose | pages [20] -->
7.1.4 Adjust for Temporal Trends

<!-- b000670 | prose | pages [20] -->
We would also like our prediction to account for any radial trend in time (the criminal becoming

<!-- b000671 | prose | pages [20] -->
more bold and committing a crime closer or further away from home). Some research has

<!-- b000672 | prose | pages [20] -->
suggested that an outward or inward trend in ri may suggest that the next crime will follow this

<!-- b000673 | prose | pages [20] -->
trend[8]. To accomplish this, we let ˜X = X + △r where △r = rn −rn−1. We note that this

<!-- b000674 | prose | pages [20] -->
new random variable, ˜X, gives our intended temporal adjustment in expected value:

<!-- b000675 | prose | pages [20] -->
E[ ˜X] = E[X + △r] = E[X] + △r

<!-- b000676 | prose | pages [20] -->
7.2

<!-- b000677 | heading | pages [20] -->
Results and Analysis

<!-- b000678 | prose | pages [20] -->
To evaluate this ﬁrst method, we feed it data from three serial rape sprees. Since the mecha-

<!-- b000679 | prose | pages [20] -->
nisms of the model were developed before these data-sets were collected and debugging was

<!-- b000680 | prose | pages [20] -->
done with different data-sets entirely, we can consider this a blind test.

<!-- b000681 | prose | pages [20] -->
In each test case, we remove the data point representing the chronologically last crime, and

<!-- b000682 | prose | pages [20] -->
produce a likelihood surface Z(x, y). As outlined above, we then identify the actual location

<!-- b000683 | prose | pages [20] -->
of the ﬁnal crime and compute the standard effectiveness multiplier κs for each case.

<!-- b000684 | prose | pages [20] -->
Our ﬁrst test data-set, coded as “Offender C,” is a comparative success for the model (Fig-

<!-- b000685 | prose | pages [20] -->
ure 5). With ks = 12.19, it is a full order of magnitude better to distribute police resources

<!-- b000686 | prose | pages [20] -->
using this model instead of distributing uniformly (although it should be remembered that the

<!-- b000687 | prose | pages [20] -->
absolute size of this number is somewhat more arbitrary for our data than it would be if the

<!-- b000688 | prose | pages [20] -->
maximum search area had been deﬁned intuitively by a cop familiar with the region).

<!-- b000689 | prose | pages [20] -->
Qualitatively, one can see the reason for the high κs: the next crime does indeed on the

<!-- b000690 | prose | pages [20] -->
surface of our ”crater,” and falls satisfyingly near the isoline of maximum height. Nevertheless,

<!-- b000691 | furniture | pages [21] -->
Team # 7507

<!-- b000692 | furniture | pages [21] -->
Page 20

<!-- b000693 | prose | pages [21] -->
(a) Heat Map of Offender C Predictions, Centroid Model

<!-- b000694 | prose | pages [21] -->
(b) Surface Plot of Offender C Predictions, Centroid Model

<!-- b000695 | caption | pages [21] -->
Figure 5: Offender C, Centroid Model Output (a), (b)

<!-- b000696 | prose | pages [21] -->
there are some 120 grid square rated greater or equal in likelihood, meaning some 0.3 km2 of

<!-- b000697 | prose | pages [21] -->
area are being patrolled with the same intensity for no reason. This amount of area is small

<!-- b000698 | prose | pages [21] -->
in an absolute sense, but is large given that the vast majority of the crimes in this case were

<!-- b000699 | prose | pages [21] -->
committed within an area of 1 square kilometer

<!-- b000700 | prose | pages [21] -->
With ¯δr = −0.276, the temporal corrections in this distribution are negligible; our pro-

<!-- b000701 | prose | pages [21] -->
jection is simply a radially symmetric ﬁt to the geographic dispersion of previous crimes. The

<!-- b000702 | prose | pages [21] -->
surface plot also shows the steepness of the ”inside” of the crater, as the geographic distribution

<!-- b000703 | prose | pages [21] -->
apparently suggests a small but sharply deﬁned buffer zone around the centroid (with all the

<!-- b000704 | furniture | pages [22] -->
Team # 7507

<!-- b000705 | furniture | pages [22] -->
Page 21

<!-- b000706 | prose | pages [22] -->
crimes contained within two square kilometers, any buffer zone would have to be small).

<!-- b000707 | prose | pages [22] -->
Our second test data-set, coded “Offender B,” (see Figure 6) is similarly successful, with

<!-- b000708 | prose | pages [22] -->
ks = 12.15. Here, the ﬁt parameters of the Γ estimate the existence of a substantially larger

<!-- b000709 | prose | pages [22] -->
buffer zone than for Offender C, but the substantial dispersion of the points along the horizontal

<!-- b000710 | prose | pages [22] -->
axis results in a larger outer radius, so that a similar portion of the high-likelihood grid points

<!-- b000711 | prose | pages [22] -->
appear “ wasted,” particularly in the upper right section of the crater. Here too, temporal

<!-- b000712 | prose | pages [22] -->
connections are negligible with ¯δr = −0.0076 .

<!-- b000713 | prose | pages [22] -->
Just as our naive desire to extrapolate from two data points begins to insist our model must

<!-- b000714 | prose | pages [22] -->
be robust, we apply our model to Offender A and ﬁnd a clear example of how it can fail. In

<!-- b000715 | prose | pages [22] -->
this case, the last crime (see Figure 7) is one of two substantial outliers, and in fact, with a

<!-- b000716 | prose | pages [22] -->
standard effectiveness multiplier of ks = 0.38, our model is nearly three times less helpful

<!-- b000717 | prose | pages [22] -->
than the average random guess in selecting a distribution of resources and manpower. Note,

<!-- b000718 | prose | pages [22] -->
however, that the vast majority of previous crimes are still well-described by the model, so the

<!-- b000719 | prose | pages [22] -->
assumption of an anchor point somewhere within the crater region does not appear to have been

<!-- b000720 | prose | pages [22] -->
a poor one. It is simply the case, as it will often be in real life, that some scheme, whim, or

<!-- b000721 | prose | pages [22] -->
outside inﬂuence caused the criminal to deviate sharply from his previous pattern in this case.

<!-- b000722 | prose | pages [22] -->
As remarked in the development of our metric, testing the model on these three data points

<!-- b000723 | prose | pages [22] -->
alone is hardly sufﬁcient to draw any broad conclusions about the utility of our model in a gen-

<!-- b000724 | prose | pages [22] -->
eral setting. Still, since these three data sets were selected arbitrarily from published literature

<!-- b000725 | prose | pages [22] -->
from within samples considered to be highly representative of typical serial killings, it is at

<!-- b000726 | prose | pages [22] -->
least reassuring that our model is somewhat successful in two of three cases, and it is hard to

<!-- b000727 | prose | pages [22] -->
imagine any model being highly successful in the third case.

<!-- b000728 | prose | pages [22] -->
7.3 Extensions

<!-- b000729 | prose | pages [22] -->
Several of the test cases considered above stray from the idealized, radially symmetric distri-

<!-- b000730 | prose | pages [22] -->
bution which centroid model assumes. In particular, the data from offender B has considerably

<!-- b000731 | prose | pages [22] -->
more variation along the horizontal axis than the vertical, and informally, it appears an elon-

<!-- b000732 | prose | pages [22] -->
gated ellipsoid might be a better ﬁt than a perfect circle. Alternatively, one might imagine that

<!-- b000733 | prose | pages [22] -->
points on the right and left of the circle should have higher likelihood scores than the ones in

<!-- b000734 | prose | pages [22] -->
the top and bottom, as though some of the volume under the crater surface had ”gravitated” to-

<!-- b000735 | prose | pages [22] -->
wards the regions more dense with points. Indeed, there is some empirical evidence to suggest

<!-- b000736 | prose | pages [22] -->
that many serial crime patterns display such angular asymmetries.[13]

<!-- b000737 | prose | pages [22] -->
The ﬁrst idea could be accomplished by constructing a special, two dimensional distribution

<!-- b000738 | prose | pages [22] -->
function which would ﬁt the points elliptically, or the construction of the function in a space

<!-- b000739 | prose | pages [22] -->
where the geometry was non-Euclidean and determined by the presence of past-crime data

<!-- b000740 | furniture | pages [23] -->
Team # 7507

<!-- b000741 | furniture | pages [23] -->
Page 22

<!-- b000742 | prose | pages [23] -->
(a) Heat Map of Offender B Predictions, Centroid Model

<!-- b000743 | prose | pages [23] -->
(b) Surface Plot of Offender C Predictions, Centroid Model

<!-- b000744 | caption | pages [23] -->
Figure 6: Offender B, Centroid Model Output (a), (b)

<!-- b000745 | prose | pages [23] -->
points. To simulate the second, a convolution with a kernel built around the nearness to the

<!-- b000746 | prose | pages [23] -->
centroid as seen by each of the crime-points could potentially be used, or an actual ”gravity-

<!-- b000747 | prose | pages [23] -->
like” simulation could be performed via the transport equation, with previous crime points as

<!-- b000748 | prose | pages [23] -->
attractors.

<!-- b000749 | prose | pages [23] -->
A cursory investigation of all of these methods during the development of our model

<!-- b000750 | furniture | pages [24] -->
Team # 7507

<!-- b000751 | furniture | pages [24] -->
Page 23

<!-- b000752 | prose | pages [24] -->
(a) Heat Map of Offender A Predictions, Centroid Model

<!-- b000753 | prose | pages [24] -->
(b) Surface Plot of Offender A Predictions, Centroid Model

<!-- b000754 | caption | pages [24] -->
Figure 7: Offender A, Centroid Model Output (a), (b)

<!-- b000755 | prose | pages [24] -->
showed some potential successes, but all would have to contain additional parameters. Without

<!-- b000756 | prose | pages [24] -->
access to a large data-set, however, from which to empirically determine the best values of these

<!-- b000757 | prose | pages [24] -->
parameters, any extension of the centroid model to include such algorithms would be at best an

<!-- b000758 | prose | pages [24] -->
arbitrary guess. Since one of the central premises of our model is that it assumes only behav-

<!-- b000759 | prose | pages [24] -->
ioral and psychological trends which are robustly supported by broad studies of serial crime, it

<!-- b000760 | prose | pages [24] -->
does not seem appropriate to include such additional modiﬁcations in our single-anchor point

<!-- b000761 | prose | pages [24] -->
model.

<!-- b000762 | furniture | pages [25] -->
Team # 7507

<!-- b000763 | furniture | pages [25] -->
Page 24

<!-- b000764 | prose | pages [25] -->
8 Multiple Anchor Points: Cluster Method

<!-- b000765 | prose | pages [25] -->
A different way to account for the angular asymmetries like the ones in the Offender B data-set,

<!-- b000766 | prose | pages [25] -->
however, would be to simply assume that no angular symmetry should be expected because

<!-- b000767 | prose | pages [25] -->
there is not simply one anchor point around which crimes are arrayed. Our second method

<!-- b000768 | prose | pages [25] -->
explicitly assumes that instead, there are at least two anchor points in the distribution of crimes

<!-- b000769 | prose | pages [25] -->
(for example, a home and a workplace), and treats each anchor point as the centroid of its own

<!-- b000770 | prose | pages [25] -->
local cluster of crimes. Like the single-anchor point extensions described above, this method

<!-- b000771 | prose | pages [25] -->
will require an additional input parameter: the number of clusters to be created. However, we

<!-- b000772 | prose | pages [25] -->
show that this parameter can be derived for each data set from only the locations of the previous

<!-- b000773 | prose | pages [25] -->
crimes, removing the need to set parameters arbitrarily.

<!-- b000774 | prose | pages [25] -->
8.1

<!-- b000775 | heading | pages [25] -->
Algorithm

<!-- b000776 | prose | pages [25] -->
The basis of this algorithm is a hierarchical clustering scheme [7]. Once clusters are found

<!-- b000777 | prose | pages [25] -->
the previously described algorithm for centroids is used at each computed cluster centroid. A

<!-- b000778 | prose | pages [25] -->
sketch of the algorithm can be seen in Figure 8. The algorithm starts with the same data as the

<!-- b000779 | prose | pages [25] -->
Centroid method but begins computations with a cluster determination scheme.

<!-- b000780 | prose | pages [25] -->
8.1.1 Finding Clusters in Crime Sequences

<!-- b000781 | prose | pages [25] -->
The ﬁrst objective of this algorithm is to determine the number of clusters and group points

<!-- b000782 | prose | pages [25] -->
into various clusters. This is accomplished through the use of hierarchical clustering and com-

<!-- b000783 | prose | pages [25] -->
parison of Silhouettes for various cluster counts.

<!-- b000784 | prose | pages [25] -->
The ﬁrst step towards this goal is to cluster the data such that there are a total of 2-4 clusters.

<!-- b000785 | prose | pages [25] -->
We forced a minimum of 2 clusters because the single cluster case is identical to the earlier

<!-- b000786 | prose | pages [25] -->
centroid method. A maximum of 4 clusters was chosen based on our assumption that each of

<!-- b000787 | prose | pages [25] -->
these clusters represents crimes around an anchor point. Subdividing into too many clusters

<!-- b000788 | prose | pages [25] -->
would be akin to saying a serial criminal has six or seven signiﬁcant points of daily activity.

<!-- b000789 | prose | pages [25] -->
While this may be the case, anchor-point theory would suggest a number of four or fewer. The

<!-- b000790 | prose | pages [25] -->
clustering algorithm is accomplished in a 3 step process.

<!-- b000791 | prose | pages [25] -->
In general the ﬁrst step to clustering is to compute the distances between all points on a

<!-- b000792 | prose | pages [25] -->
selected metric [7]. In this case the euclidian distance, henceforth designated d(x, y), is used

<!-- b000793 | prose | pages [25] -->
since the only measure we care about is physical distance between points. Once all of these

<!-- b000794 | prose | pages [25] -->
distances have been computed the data is organized into a hierarchical cluster tree, the tree can

<!-- b000795 | prose | pages [25] -->
be represented by what is known as a dendrogram [7]. The dendrogram for Offender B is seen

<!-- b000796 | prose | pages [25] -->
in Figure 9.

<!-- b000797 | furniture | pages [26] -->
Team # 7507

<!-- b000798 | furniture | pages [26] -->
Page 25

<!-- b000799 | caption | pages [26] -->
Figure 8: Algorithm Flow Chart for Cluster Method

<!-- b000800 | prose | pages [26] -->
This cluster tree, of N data points Pi, i = 1, ..., N, is built up by ﬁrst assuming that each

<!-- b000801 | prose | pages [26] -->
data point is its own cluster. Clusters are then merged based on which 2 are the closest in some

<!-- b000802 | prose | pages [26] -->
deﬁned metric dc. Formally if we have clusters 1, ..., n denoted as Ci, i = 1, ..., n we choose

<!-- b000803 | prose | pages [26] -->
to merge the two clusters i and j, i < j into cluster i and delete cluster j where i, j minimizes

<!-- b000804 | prose | pages [26] -->
dc(Ci, Cj).

<!-- b000805 | prose | pages [26] -->
This process is repeated until all of the points have been merged into the number of desired

<!-- b000806 | prose | pages [26] -->
clusters, to create a dendrogram the number of desired clusters is set to one. In this case we

<!-- b000807 | prose | pages [26] -->
used as our metric the distance between the centroids of any two clusters. These cluster merges

<!-- b000808 | prose | pages [26] -->
are plotted as the horizontal lines in the dendrogram, and their height is based on the distance

<!-- b000809 | prose | pages [26] -->
between merged clusters at the time of merging.

<!-- b000810 | prose | pages [26] -->
The above algorithm requires a ﬁxed number of clusters, however we have no a priori

<!-- b000811 | prose | pages [26] -->
knowledge of the number of actual clusters. Because of this we needed a way to determine

<!-- b000812 | prose | pages [26] -->
the optimal number of clusters. To accomplish this we use the notion of Silhouettes [16]. The

<!-- b000813 | prose | pages [26] -->
silhouette at at point is denoted as s(Pi) and is computed for all data points.

<!-- b000814 | prose | pages [26] -->
We denote a(Pi) as the average distance from Pi to all other points in its cluster and b(Pi, k)

<!-- b000815 | furniture | pages [27] -->
Team # 7507

<!-- b000816 | furniture | pages [27] -->
Page 26

<!-- b000817 | caption | pages [27] -->
Figure 9: Dendrogram for Offender B

<!-- b000818 | prose | pages [27] -->
as the average distance from Pi to points in cluster Ck where Pi /∈Ck. Now we can deﬁne

<!-- b000819 | prose | pages [27] -->
(i = 1, ..., N)

<!-- b000820 | prose | pages [27] -->
!

<!-- b000821 | prose | pages [27] -->
#

<!-- b000822 | prose | pages [27] -->
k|Pi /∈Ck (b(Pi, k)) −a(Pi) min

<!-- b000823 | prose | pages [27] -->
!

<!-- b000824 | prose | pages [27] -->
s(Pi) =

<!-- b000825 | prose | pages [27] -->
(1) #

<!-- b000826 | prose | pages [27] -->
a(Pi), min

<!-- b000827 | prose | pages [27] -->
max

<!-- b000828 | prose | pages [27] -->
k|Pi /∈Ck (b(Pi, k))

<!-- b000829 | prose | pages [27] -->
Inspection of (1) shows that s can take values in [−1, 1]. Where the value of 1 is only taken

<!-- b000830 | prose | pages [27] -->
if a cluster is a single point and the value −1 can only be taken in cases where multiple points

<!-- b000831 | prose | pages [27] -->
at the same location belong to different clusters. The closer s(Pi) is to 1 the better Pi ﬁts into

<!-- b000832 | prose | pages [27] -->
its current cluster and the closer to s(Pi) is to -1 the worse it ﬁts within its current cluster.

<!-- b000833 | prose | pages [27] -->
Now to optimize the number of clusters we compute the clustering such that there are 2, 3

<!-- b000834 | prose | pages [27] -->
and 4 clusters. Then in each case we compute the average Silhouette value across every point

<!-- b000835 | prose | pages [27] -->
that is not the only point in a cluster. The Silhouette values at these single point clusters are

<!-- b000836 | prose | pages [27] -->
ignored because otherwise clusters of 1 inﬂuence the average in an undesirable way. We then

<!-- b000837 | prose | pages [27] -->
seek to maximize the average Silhouette value across the number of clusters. A sample plot of

<!-- b000838 | prose | pages [27] -->
average Silhouette value versus number of clusters is seen in Figure 10

<!-- b000839 | prose | pages [27] -->
In this case we select 4 as the desired number of clusters. The cluster groupings computed

<!-- b000840 | prose | pages [27] -->
by the algorithm are shown in Figure 11. We note that because the average Silhouette plot has

<!-- b000841 | prose | pages [27] -->
a tendency to increase with number of clusters we cap the possible number of clusters at 4. It

<!-- b000842 | furniture | pages [28] -->
Team # 7507

<!-- b000843 | furniture | pages [28] -->
Page 27

<!-- b000844 | caption | pages [28] -->
Figure 10: Offender B average Silhouette Values Vs Number of Clusters

<!-- b000845 | prose | pages [28] -->
is important to note however that the algorithm does not always pick 4 clusters, for example

<!-- b000846 | prose | pages [28] -->
the clustering of Offender C’s crimes is optimized by having 2 clusters.

<!-- b000847 | caption | pages [28] -->
Figure 11: Offender B Crime Points Sorted into Four Clusters

<!-- b000848 | furniture | pages [29] -->
Team # 7507

<!-- b000849 | furniture | pages [29] -->
Page 28

<!-- b000850 | prose | pages [29] -->
We now have a method that not only clusters the data, but also determines based on our met-

<!-- b000851 | prose | pages [29] -->
ric of distance, what an optimal clustering is. Now we can take the output from this algorithm

<!-- b000852 | prose | pages [29] -->
and progress to developing our likelihood surface.

<!-- b000853 | prose | pages [29] -->
8.1.2 Cluster Loop Algorithm

<!-- b000854 | prose | pages [29] -->
From this point forward our clustering algorithm draws heavily from our centroid algorithm

<!-- b000855 | prose | pages [29] -->
with a few small changes. The ﬁrst thing we do is compute the likelihood surface for the

<!-- b000856 | prose | pages [29] -->
centroid of each cluster, in the case where a cluster contains more than two points we simply

<!-- b000857 | prose | pages [29] -->
use our centroid algorithm to develop this likelihood surface. If a cluster contains a single point

<!-- b000858 | prose | pages [29] -->
we treat it differently, we do not assume that this cluster represents an anchor point.

<!-- b000859 | prose | pages [29] -->
Instead we treat this point as an outlier. However, based on the idea that this point exists for

<!-- b000860 | prose | pages [29] -->
some reason we do want to add some likelihood to the area. Towards this end we use a gaussian

<!-- b000861 | prose | pages [29] -->
centered at that point as our likelihood surface. The mean of this gaussian is determined by

<!-- b000862 | prose | pages [29] -->
the expected value of the gamma function placed over every anchor point of a cluster that has

<!-- b000863 | prose | pages [29] -->
more than 1 point.

<!-- b000864 | prose | pages [29] -->
8.1.3 Combining Cluster Predictions: Temporal and Size Weighting

<!-- b000865 | prose | pages [29] -->
Using the separate likelihood surfaces computed for each cluster we can create our ﬁnal surface

<!-- b000866 | prose | pages [29] -->
through a linear combination of the individual surfaces. The surfaces returned by the centroid

<!-- b000867 | prose | pages [29] -->
function are normalized, so there is some equivilance between them.

<!-- b000868 | prose | pages [29] -->
We now compute weights for each likelihood surface. There are two major components of

<!-- b000869 | prose | pages [29] -->
our weights, one is simply number of points in that weights cluster over total number of points.

<!-- b000870 | prose | pages [29] -->
This weights the more common crime locations. The next component of the weighting is the

<!-- b000871 | prose | pages [29] -->
average temporal index of the events in a given cluster over the ﬁnal point index. This weights

<!-- b000872 | prose | pages [29] -->
more recent clusters and is not inﬂuenced directly by the number of points in a cluster.

<!-- b000873 | prose | pages [29] -->
Once all of the likelihood surfaces are weighted they are summed together and the result is

<!-- b000874 | prose | pages [29] -->
again normalized to have sum 1. This weighted sum is the ﬁnal output of our algorithm and is

<!-- b000875 | prose | pages [29] -->
equivalent in type to the output of our centroid algorithm.

<!-- b000876 | prose | pages [29] -->
8.2

<!-- b000877 | heading | pages [29] -->
Results and Analysis

<!-- b000878 | prose | pages [29] -->
The three test data-sets conveniently display the cluster method’s superior adaptability. In the

<!-- b000879 | prose | pages [29] -->
case of Offender C (see Figure 12) for example, the highly localized nature of the data points

<!-- b000880 | prose | pages [29] -->
means there is very little difference between the centroid method and and the cluster method

<!-- b000881 | prose | pages [29] -->
results (and indeed, as the data becomes increasingly centralized, one would hope the two

<!-- b000882 | furniture | pages [30] -->
Team # 7507

<!-- b000883 | furniture | pages [30] -->
Page 29

<!-- b000884 | prose | pages [30] -->
results would converge). Indeed, the only difference is that the cluster method, insisting on at

<!-- b000885 | prose | pages [30] -->
least two separate clusters, identiﬁes the point directly below the centroid as a cluster of one

<!-- b000886 | prose | pages [30] -->
(an outlier), and therefore excludes it from the computation of the larger cluster’s centroid (a

<!-- b000887 | prose | pages [30] -->
slight Gaussian contribution from this point’s “own” cluster can be seen in the surface plot).

<!-- b000888 | prose | pages [30] -->
This has the effect of slightly reducing the variance and therefore narrowing the ﬁt function;

<!-- b000889 | prose | pages [30] -->
consequently, the standard effectiveness multiplier rises slightly to 15.82.

<!-- b000890 | prose | pages [30] -->
Testing with Offender B (see Figure 13), by contrast, shows the cluster method operating at

<!-- b000891 | prose | pages [30] -->
the other edge of its range, as the silhouette optimization routine decides this data is best repre-

<!-- b000892 | prose | pages [30] -->
sented by four distinct clusters with four separate anchor points. After unblinding the details of

<!-- b000893 | prose | pages [30] -->
this case, we discover that the researcher documenting the case also found it notable for the fact

<!-- b000894 | prose | pages [30] -->
that the offender seemed to choose his targets alternately between three city blocks, then brieﬂy

<!-- b000895 | prose | pages [30] -->
expanded his range geographically to an additional neighborhood further away before return-

<!-- b000896 | prose | pages [30] -->
ing to offend again in one of his earlier active areas. The researcher hypothesizes this may have

<!-- b000897 | prose | pages [30] -->
been a tactic to avoid known locations of parole ofﬁcers, as the offender was a parolee during

<!-- b000898 | prose | pages [30] -->
the majority of his crimes;[9] whatever the reason, it is a success (if a statistically insigniﬁcant

<!-- b000899 | prose | pages [30] -->
one) for our model that we discerned this pattern from the geographic dispersion alone. This

<!-- b000900 | prose | pages [30] -->
data-set also provides a good example of a case where multiple anchor point analysis seems

<!-- b000901 | prose | pages [30] -->
valid even though most do not represent homes or workplaces: the model is simply responding

<!-- b000902 | prose | pages [30] -->
to the statistical evidence that criminal seems most comfortable committing crimes in one of 4

<!-- b000903 | prose | pages [30] -->
distinct locations.

<!-- b000904 | prose | pages [30] -->
On ﬁrst glance, however, it might appear that the centroid method still outperforms the

<!-- b000905 | prose | pages [30] -->
cluster algorithm for this data-set; after all, the actual crime point no longer appears in the

<!-- b000906 | prose | pages [30] -->
band of maximum likelihood. This is true and intentional, as the model chooses to weight

<!-- b000907 | prose | pages [30] -->
the largest cluster most strongly and the “freshest” cluster behind it. Nevertheless, while not

<!-- b000908 | prose | pages [30] -->
accurately predicting that the offender would choose to return to one of his earliest activity

<!-- b000909 | prose | pages [30] -->
zones, it still outperforms the centroid method with a κs value of 22.95. This is because the

<!-- b000910 | prose | pages [30] -->
craters generated by the cluster method are sharper and taller for this data set, so there are

<!-- b000911 | prose | pages [30] -->
fewer resources “wasted” at high-likelihood areas where no crime is committed. We argue that

<!-- b000912 | prose | pages [30] -->
this is the correct weighting, a model which makes a bolder, narrower prediction which is still

<!-- b000913 | prose | pages [30] -->
successful is more valuable than one which covers the right point by simply splashing guesses

<!-- b000914 | prose | pages [30] -->
across a large swath of area.

<!-- b000915 | prose | pages [30] -->
Unsurprisingly, the cluster model fares no better than the centroid method when confronted

<!-- b000916 | prose | pages [30] -->
with Offender A (see Figure 14). Indeed, since the outlier points are excluded from the centroid

<!-- b000917 | prose | pages [30] -->
calculation for the larger cluster, the model bets even more aggressively on this macro-cluster,

<!-- b000918 | prose | pages [30] -->
and with a resulting measurement of κs = 0.001, we can see that following this procedure

<!-- b000919 | prose | pages [30] -->
would virtually eliminate the ability of the police to anticipate the next crime.

<!-- b000920 | furniture | pages [31] -->
Team # 7507

<!-- b000921 | furniture | pages [31] -->
Page 30

<!-- b000922 | prose | pages [31] -->
On the whole, these low-statistics tests are consistent with (while still not predictive of)

<!-- b000923 | prose | pages [31] -->
our earlier belief that the cluster model is more concerned with avoiding waste: it makes more

<!-- b000924 | prose | pages [31] -->
precise guesses in the hopes of wasting few resources on average, but runs the risk of being

<!-- b000925 | prose | pages [31] -->
dramatically wrong from time to time. This can also be seen from the comparatively smaller

<!-- b000926 | prose | pages [31] -->
size of the buffer zones within craters, and the tendency for the maximum point on the like-

<!-- b000927 | prose | pages [31] -->
lihood surface plot to be higher when using the cluster method. This tendency of the cluster

<!-- b000928 | prose | pages [31] -->
method to gamble more aggressively has paid off in the three datasets we examine (one might

<!-- b000929 | prose | pages [31] -->
call it “cluster luck”), but our complete model will need a way to balance this boldness when a

<!-- b000930 | prose | pages [31] -->
more conservative approach is warranted.

<!-- b000931 | furniture | pages [32] -->
Team # 7507

<!-- b000932 | furniture | pages [32] -->
Page 31

<!-- b000933 | prose | pages [32] -->
(a) Heat Map of Offender C Predictions, Cluster Model

<!-- b000934 | prose | pages [32] -->
(b) Surface Plot of Offender S Predictions, Centroid Model

<!-- b000935 | caption | pages [32] -->
Figure 12: Offender C, Cluster Model Output (a), (b)

<!-- b000936 | furniture | pages [33] -->
Team # 7507

<!-- b000937 | furniture | pages [33] -->
Page 32

<!-- b000938 | prose | pages [33] -->
(a) Heat Map of Offender B Predictions, Cluster Model

<!-- b000939 | prose | pages [33] -->
(b) Surface Plot of Offender B Predictions, Centroid Model

<!-- b000940 | caption | pages [33] -->
Figure 13: Offender B, Cluster Model Output (a), (b)

<!-- b000941 | furniture | pages [34] -->
Team # 7507

<!-- b000942 | furniture | pages [34] -->
Page 33

<!-- b000943 | prose | pages [34] -->
(a) Heat Map of Offender A Predictions, Cluster Model

<!-- b000944 | prose | pages [34] -->
(b) Surface Plot of Offender B Predictions, Centroid Model

<!-- b000945 | caption | pages [34] -->
Figure 14: Offender A, Cluster Model Output (a), (b)

<!-- b000946 | furniture | pages [35] -->
Team # 7507

<!-- b000947 | furniture | pages [35] -->
Page 34

<!-- b000948 | prose | pages [35] -->
8.3

<!-- b000949 | heading | pages [35] -->
Possible Extensions of the Cluster Model

<!-- b000950 | prose | pages [35] -->
One potential extension which could have been made to the cluster algorithm would be to al-

<!-- b000951 | prose | pages [35] -->
low it to consider a higher maximum number of clusters. We ﬁnd that the common trend in

<!-- b000952 | prose | pages [35] -->
geographic proﬁling research is that most serial crime data-sets do not suggest more than three

<!-- b000953 | prose | pages [35] -->
or four anchor points[15] but this is not strongly validated by empirical studies. It seems intu-

<!-- b000954 | prose | pages [35] -->
itively clear that, since most violent serial crime sprees contain between 5 and 25 offenses,[2]

<!-- b000955 | prose | pages [35] -->
it is unlikely that increasing the cluster size appreciably would be reasonable. On the other

<!-- b000956 | prose | pages [35] -->
hand, if one were confronted with an unusually long crime spree (say, 40 events or more) or if

<!-- b000957 | prose | pages [35] -->
one wanted to apply this to residential crime sprees (which are generally longer[12]), it might

<!-- b000958 | prose | pages [35] -->
well be prudent to allow 5 or more clusters. The ideal maximum number in such cases would

<!-- b000959 | prose | pages [35] -->
have to be determined by testing across sample data, or through an intelligent human guess.

<!-- b000960 | prose | pages [35] -->
Another natural way to extend the cluster model would be to allow it to create only one

<!-- b000961 | prose | pages [35] -->
anchor point if there was insufﬁciently strong evidence that something deserved to be treated

<!-- b000962 | prose | pages [35] -->
as a separate cluster. However, there are mathematical problems which arise in attempting to

<!-- b000963 | prose | pages [35] -->
implement this; for one thing, the silhouette of a point is only deﬁned if there is more than one

<!-- b000964 | prose | pages [35] -->
cluster under consideration, so there is no simply way to evaluate via silhouettes whether the

<!-- b000965 | prose | pages [35] -->
single-cluster case is superior to the others. Similarly, one could reject this method and simply

<!-- b000966 | prose | pages [35] -->
use a single cluster if the average silhouette value dropped below some threshold; as always,

<!-- b000967 | prose | pages [35] -->
however, we can only select this threshold arbitrarily since we do not have sufﬁcient data to

<!-- b000968 | prose | pages [35] -->
experimentally estimate a reasonable value. As we shall see, however, there is a different

<!-- b000969 | prose | pages [35] -->
method which can be used to combine these two schemes.

<!-- b000970 | prose | pages [35] -->
9 The Final Predictor: Combining the Schemes

<!-- b000971 | prose | pages [35] -->
Given that our two methods each show some ability to identify geographic trends in serial

<!-- b000972 | prose | pages [35] -->
criminals, we develop a method to decide if, in a give situation, one method is more appropriate

<!-- b000973 | prose | pages [35] -->
then the other. On the way to this decision we also present criteria for whether or not our

<!-- b000974 | prose | pages [35] -->
methods have any predictive value at all.

<!-- b000975 | prose | pages [35] -->
The ﬁrst step towards making a decision is to run the algorithm many times on truncated

<!-- b000976 | prose | pages [35] -->
data and compute effectiveness values at each step. This is accomplished by truncating the

<!-- b000977 | prose | pages [35] -->
availible data and testing both algorithms against the actual next crime. Starting with N crimes

<!-- b000978 | prose | pages [35] -->
we seek to determine which method, if either, should be used to predict the N +1 crime. Based

<!-- b000979 | prose | pages [35] -->
on our assumption that you are not trying to predict with less than 4 crimes we must enforce

<!-- b000980 | prose | pages [35] -->
N ≥5. Now for M = 4, ..., N −1 use the ﬁrst M crimes to predict the M + 1 crime and then

<!-- b000981 | prose | pages [35] -->
based on the actual location of the M + 1 crime determine the effectiveness multiplier. Denote

<!-- b000982 | furniture | pages [36] -->
Team # 7507

<!-- b000983 | furniture | pages [36] -->
Page 35

<!-- b000984 | prose | pages [36] -->
these effectiveness multipliers κm,c

<!-- b000985 | prose | pages [36] -->
M , where κm

<!-- b000986 | prose | pages [36] -->
M indicates the multiplier for the cluster method

<!-- b000987 | prose | pages [36] -->
M the centroid method. Also denote κm,c

<!-- b000988 | prose | pages [36] -->
M as the mean of κm,c

<!-- b000989 | prose | pages [36] -->
, ..., κm,c

<!-- b000990 | prose | pages [36] -->
and κc

<!-- b000991 | prose | pages [36] -->
M . In Figure 15 we

<!-- b000992 | prose | pages [36] -->
4

<!-- b000993 | prose | pages [36] -->
see κc

<!-- b000994 | prose | pages [36] -->
M and κm

<!-- b000995 | prose | pages [36] -->
M for Offender C. In Figure 16 we see κm

<!-- b000996 | prose | pages [36] -->
M and κc

<!-- b000997 | prose | pages [36] -->
M for Offender C.

<!-- b000998 | caption | pages [36] -->
Figure 15: Running Mean of Effectiveness Multiplier

<!-- b000999 | caption | pages [36] -->
Figure 16: Effectiveness Multiplier vs. Crime Predicted

<!-- b001000 | prose | pages [36] -->
We now determine if either of our methods recognizes a geographic trend. To do this,

<!-- b001001 | prose | pages [36] -->
denote ac as the number of κc

<!-- b001002 | prose | pages [36] -->
M that are less than 1 and similarly denote am as the number of

<!-- b001003 | prose | pages [36] -->
M that are less than 1. If ac > N−4

<!-- b001004 | prose | pages [36] -->
we state the our centroid method is invalid, and similarly

<!-- b001005 | prose | pages [36] -->
κm

<!-- b001006 | prose | pages [36] -->
2

<!-- b001007 | furniture | pages [37] -->
Team # 7507

<!-- b001008 | prose | pages [37] -->
if am > N−4

<!-- b001009 | furniture | pages [37] -->
Page 36

<!-- b001010 | prose | pages [37] -->
we state the our cluster method is invalid. We place our break point at half of the 2

<!-- b001011 | prose | pages [37] -->
effectiveness multipliers being less that 1 because that means that over 50% of time we do not

<!-- b001012 | prose | pages [37] -->
increase effectiveness, thus we note that our algorithm is not detecting geographic trends in the

<!-- b001013 | prose | pages [37] -->
data.

<!-- b001014 | prose | pages [37] -->
If only one of the methods is determined to be valid we choose to use that one. If neither is

<!-- b001015 | prose | pages [37] -->
valid we simply state that no geographic trends have been found in the data and our algorithm

<!-- b001016 | prose | pages [37] -->
should not be heavily relied upon in relation to other methods which may be available.

<!-- b001017 | prose | pages [37] -->
N−1 and κm

<!-- b001018 | prose | pages [37] -->
N−1, if κc

<!-- b001019 | prose | pages [37] -->
If both methods are determined to be valid we simply look at κc

<!-- b001020 | prose | pages [37] -->
N−1 >

<!-- b001021 | prose | pages [37] -->
N−1 then we pick the centroid method, otherwise we pick the cluster method. In Figure 15

<!-- b001022 | prose | pages [37] -->
κm

<!-- b001023 | prose | pages [37] -->
we note that the cluster method would be picked.

<!-- b001024 | prose | pages [37] -->
9.1

<!-- b001025 | heading | pages [37] -->
Results and Analysis

<!-- b001026 | prose | pages [37] -->
Using the aforementioned decision algorithm, our combined method would choose to use the

<!-- b001027 | prose | pages [37] -->
clustering algorithm for all three cases (the end results then being those given in the cluster

<!-- b001028 | prose | pages [37] -->
section above). In fact, one would have to have a a highly cohesive single cluster of data with

<!-- b001029 | prose | pages [37] -->
no outliers in order for the Centroid method to ever prevail, and this is as it should be, for even

<!-- b001030 | prose | pages [37] -->
when there appears to be only one true anchor point, cluster is capable of rejecting up to 3

<!-- b001031 | prose | pages [37] -->
statistical outliers before computing the centroid, which should in general improve the ﬁts and

<!-- b001032 | prose | pages [37] -->
consequently improve the results.

<!-- b001033 | prose | pages [37] -->
Our combined model contains one other piece of information: the average effectiveness

<!-- b001034 | prose | pages [37] -->
multiplier κs = κm,c

<!-- b001035 | prose | pages [37] -->
N−1, which we are now treating as a rough conﬁdence estimate for the model

<!-- b001036 | prose | pages [37] -->
when applied to a given data set. While the interpretation is not perfect, this value essentially

<!-- b001037 | prose | pages [37] -->
tells us how well the algorithm would have fared against this criminal in the past, and assumes

<!-- b001038 | prose | pages [37] -->
this value will also represent its effectiveness in the immediate future. The ﬂatness in the tail

<!-- b001039 | prose | pages [37] -->
of of the κs plot for Offender C (Figure 15), while insufﬁcient to justify this metric, is at least

<!-- b001040 | prose | pages [37] -->
consistent with the assumptions. We can also test this mean against the actual values computed

<!-- b001041 | prose | pages [37] -->
above:

<!-- b001042 | prose | pages [37] -->
Offender C

<!-- b001043 | prose | pages [37] -->
B

<!-- b001044 | prose | pages [37] -->
A

<!-- b001045 | prose | pages [37] -->
κs κs 6.65 15.82

<!-- b001046 | prose | pages [37] -->
8.473 22.95

<!-- b001047 | prose | pages [37] -->
12.25 0.001

<!-- b001048 | prose | pages [37] -->
As one would suspect for the mean over a small number of points, it is not a perfect estima-

<!-- b001049 | prose | pages [37] -->
tor of the next value. Our now-familiar nemesis, Offender A, completely deceives the model

<!-- b001050 | prose | pages [37] -->
once again, because it predicts his movements extremely well up until his very last crime. It

<!-- b001051 | prose | pages [37] -->
does seem, though, that if one allows for occasional outliers, this mean effectiveness multiplier

<!-- b001052 | furniture | pages [38] -->
Team # 7507

<!-- b001053 | furniture | pages [38] -->
Page 37

<!-- b001054 | prose | pages [38] -->
provides a ballpark estimate of our conﬁdence in the model. Note that in the two more well-

<!-- b001055 | prose | pages [38] -->
behaved cases, the model with the higher projected effectiveness κs is in fact the more effective

<!-- b001056 | prose | pages [38] -->
model in reality. Moreover, by simply properties of averages, it should be true that to within

<!-- b001057 | prose | pages [38] -->
the level of uncertainty created by the number of points in the data-set, when one compares size

<!-- b001058 | prose | pages [38] -->
of κs for the same model on two different data sets, the one with the larger κs will on average

<!-- b001059 | prose | pages [38] -->
be the more trustworthy.

<!-- b001060 | prose | pages [38] -->
9.1.1 The Psychic, the Hairﬁnder, and the Intuitive Cop

<!-- b001061 | prose | pages [38] -->
Although the size of our datasets will not allow us to demonstrate anything conclusively, the

<!-- b001062 | prose | pages [38] -->
model we develop is a strong candidate to beat the psychic and the hairﬁnder (random chance),

<!-- b001063 | prose | pages [38] -->
for several reasons.

<!-- b001064 | prose | pages [38] -->
• The predictions are based on the assumption of trends in serial crime behavior which

<!-- b001065 | prose | pages [38] -->
have been tested on large sets of real-world data. [12] [2] [8]

<!-- b001066 | prose | pages [38] -->
• Similar mathematical techniques are used in the anchor-point estimation schemes cur-

<!-- b001067 | prose | pages [38] -->
rently being employed and researched, which also consistently outperform random guesses

<!-- b001068 | prose | pages [38] -->
when tested across data samples

<!-- b001069 | prose | pages [38] -->
• The model was successful in the two of the three datasets on which it was tested, and

<!-- b001070 | prose | pages [38] -->
these datasets were selected from preexisting research as representative samples of serial

<!-- b001071 | prose | pages [38] -->
crime data

<!-- b001072 | prose | pages [38] -->
• Several crimes in each dataset can be predicted well, including the case where our model

<!-- b001073 | prose | pages [38] -->
fails to predict the ﬁnal, outlier crime point– i.e., in a dataset of 16 crimes, we are also

<!-- b001074 | prose | pages [38] -->
often able to predict the 15 crime using the preceding 14, the 14th using the preceding

<!-- b001075 | prose | pages [38] -->
13, etc., all with more success than a random guess.

<!-- b001076 | prose | pages [38] -->
This evidence suggests, without proving, that on average, our model will be better than

<!-- b001077 | prose | pages [38] -->
blind chance. We do not, however, make the claim that we will do better than a police depart-

<!-- b001078 | prose | pages [38] -->
ment assigning resources based off no model at all. In the absence of mathematical guidance,

<!-- b001079 | prose | pages [38] -->
a policeman in such a department would have rely on his own knowledge of his patrol area,

<!-- b001080 | prose | pages [38] -->
his sense of patterning in the offender’s crimes, and any “ gut feelings” he developed about

<!-- b001081 | prose | pages [38] -->
the offender’s psychology, based on his previous experience in law enforcement. This “Intu-

<!-- b001082 | prose | pages [38] -->
itive Cop” has considerably more information at his disposal than our model, as he knows,

<!-- b001083 | prose | pages [38] -->
for example, that a killer targeting prostitutes is more likely to strike in the red-light district

<!-- b001084 | prose | pages [38] -->
of his city. Additionally, research suggests that with a little informal training, any layperson

<!-- b001085 | prose | pages [38] -->
can perform nearly as well as anchor point prediction algorithms when guessing a criminal’s

<!-- b001086 | furniture | pages [39] -->
Team # 7507

<!-- b001087 | furniture | pages [39] -->
Page 38

<!-- b001088 | prose | pages [39] -->
home location.[18] 2. As a result, one might well expect the intuitive cop to outperform the

<!-- b001089 | prose | pages [39] -->
model overall, as he can apparently approximate many of its mathematical strengths through

<!-- b001090 | prose | pages [39] -->
intelligent estimation and also brings a breadth of knowledge to bear about the physical char-

<!-- b001091 | prose | pages [39] -->
acteristics of the underlying map.

<!-- b001092 | prose | pages [39] -->
9.2

<!-- b001093 | heading | pages [39] -->
Possible Extensions to the General Model

<!-- b001094 | prose | pages [39] -->
9.2.1 Partnership With the Intuitive Cop

<!-- b001095 | prose | pages [39] -->
The best possible extension of this model, therefore, is simply to ensure that its output results

<!-- b001096 | prose | pages [39] -->
are always interpreted by the intuitive cop himself (or indeed, by the intuitive police force as a

<!-- b001097 | prose | pages [39] -->
whole). In this way, obvious “dead zones” in the underlying map (such as lakes, military bases,

<!-- b001098 | prose | pages [39] -->
or uninhabited farmland) can be immediately rejected as priority areas without signiﬁcantly de-

<!-- b001099 | prose | pages [39] -->
creasing the odds of preventing the next crime. This immediately increases the effectiveness

<!-- b001100 | prose | pages [39] -->
multiplier for the combined process. Similarly, the intuitive cop might be called upon to man-

<!-- b001101 | prose | pages [39] -->
ually set (or at least experiment with) some of the parameters we assign based purely off of

<!-- b001102 | prose | pages [39] -->
geography. It may be clear to a human, for example, that the killer in question has three anchor

<!-- b001103 | prose | pages [39] -->
points, as he is committing crimes in each of three different rural towns. If these towns are

<!-- b001104 | prose | pages [39] -->
quite close, however, our model could be deceived into believing that there are fewer than 3

<!-- b001105 | prose | pages [39] -->
clusters on the map.

<!-- b001106 | prose | pages [39] -->
Just as it should be for statisticians, historians, and tabloid journalists everywhere, the

<!-- b001107 | prose | pages [39] -->
general mantra for a police department hoping to employ computational geographic proﬁling

<!-- b001108 | prose | pages [39] -->
should be “more data is better.” We have repeatedly made a point of saying that our model

<!-- b001109 | prose | pages [39] -->
cannot be considered robust until it has been tested on a large dataset, but it is similarly true

<!-- b001110 | prose | pages [39] -->
that any additional data input in the form of human intuition and interpolation will tend to

<!-- b001111 | prose | pages [39] -->
improve results. The best extension of this algorithm is simply to ensure it does not overrule

<!-- b001112 | prose | pages [39] -->
the pre-existing predictions and theories of local law enforcement, but rather simply augments

<!-- b001113 | prose | pages [39] -->
them.

<!-- b001114 | prose | pages [39] -->
9.2.2 Crime Prediction Versus Anchor Point Prediction

<!-- b001115 | prose | pages [39] -->
Finally, as all our discussions to this point have presupposed that predicting a criminal’s next

<!-- b001116 | prose | pages [39] -->
strike point is the right thing to do, it is important to observe that in many ways, this may

<!-- b001117 | prose | pages [39] -->
not always be the case. On the contrary, having examined in detail the scope of literature on

<!-- b001118 | prose | pages [39] -->
quantitative criminology, we ﬁnd at least three reasons to believe it is often a better practice to

<!-- b001119 | prose | pages [39] -->
2Rossmo (2004) has critiqued the Snook study as insufﬁciently representative; however, Paulsen (2006) has

<!-- b001120 | prose | pages [39] -->
reproduced Snook’s result in a manner which removes many of these insufﬁciencies.

<!-- b001121 | furniture | pages [40] -->
Team # 7507

<!-- b001122 | furniture | pages [40] -->
Page 39

<!-- b001123 | prose | pages [40] -->
attempt to predict the location of his anchor points instead.

<!-- b001124 | prose | pages [40] -->
1. Uncertainty in the estimate will tend to be smaller for an anchor point predictor. This

<!-- b001125 | prose | pages [40] -->
is easy to see from the inner workings of our algorithm. Each method postulates the

<!-- b001126 | prose | pages [40] -->
existence of an anchor point at the centroid of a local cluster (or the entire dataset), and

<!-- b001127 | prose | pages [40] -->
then predicts future crimes based on geographic trends about that anchor. As a result, all

<!-- b001128 | prose | pages [40] -->
the uncertainty in the anchor point prediction will contribute also to error in the crime

<!-- b001129 | prose | pages [40] -->
point prediction, and on average, the total uncertainty will be their quadrature sum, which

<!-- b001130 | prose | pages [40] -->
is necessarily greater than or equal to the uncertainty in the anchor location itself.

<!-- b001131 | prose | pages [40] -->
2. Anchor point prediction schemes are much more widely researched and documented.

<!-- b001132 | prose | pages [40] -->
Criminologists like Rossmo, Canter, and many others have studied a broad family of

<!-- b001133 | prose | pages [40] -->
anchor point predictors and tested them against large sets real-world data from serial

<!-- b001134 | prose | pages [40] -->
criminals. This allows them to optimize over a wide variety of parameters such as dis-

<!-- b001135 | prose | pages [40] -->
tance functions, decay weightings, temporal weightings, etc. While our model attempts

<!-- b001136 | prose | pages [40] -->
to compensate by minimizing the number of such parameters that need to be set and

<!-- b001137 | prose | pages [40] -->
choosing the others based on the data being examined, the fact remains that its methods

<!-- b001138 | prose | pages [40] -->
simply have not been validated to the same level of conﬁdence

<!-- b001139 | prose | pages [40] -->
3. Real-world considerations often make an anchor point search more practical. The sim-

<!-- b001140 | prose | pages [40] -->
ple truth is that, equipped with a prediction of likely crime points, the best a police force

<!-- b001141 | prose | pages [40] -->
can hope to do is increase patrol levels and other resources in the likely areas, and wait

<!-- b001142 | prose | pages [40] -->
to see if the criminal strikes again. On the other hand, when given a predicted region for

<!-- b001143 | prose | pages [40] -->
the criminal’s anchor point, they can take a more active approach by searching the area

<!-- b001144 | prose | pages [40] -->
in question for suspicious behavior, eyewitness data, and additional evidence. Recall that

<!-- b001145 | prose | pages [40] -->
at least one of the anchor points is almost certainly the suspect’s home (one study found

<!-- b001146 | prose | pages [40] -->
this to be true 83% of the time[15]); and consequently, pursuing this anchor point can

<!-- b001147 | prose | pages [40] -->
give the police a sense of the perpatrator’s home region, provides potential neighbors

<!-- b001148 | prose | pages [40] -->
who can be interviewed, and could even lead to the capture of the criminal in his own

<!-- b001149 | prose | pages [40] -->
home.

<!-- b001150 | prose | pages [40] -->
We do not completely eschew the utility of crime-point prediction: it has the obvious beneﬁt of

<!-- b001151 | prose | pages [40] -->
potentially saving a life or preventing a rape. Depending on circumstances, it could also be of

<!-- b001152 | prose | pages [40] -->
use in predicting the body location of a missing person presumed to have been taken by a serial

<!-- b001153 | prose | pages [40] -->
criminal, or even in determining whether a new crime was committed by the same individual

<!-- b001154 | prose | pages [40] -->
as those in a previous dataset. Once again, we appeal to the expertise of the intuitive cop: when

<!-- b001155 | prose | pages [40] -->
resources permit or circumstances demand, predicting a future crime point may be a good idea,

<!-- b001156 | prose | pages [40] -->
but our model itself makes no claims as to whether this is a good idea in any given case.

<!-- b001157 | furniture | pages [41] -->
Team # 7507

<!-- b001158 | furniture | pages [41] -->
Page 40

<!-- b001159 | prose | pages [41] -->
10

<!-- b001160 | heading | pages [41] -->
Conclusion

<!-- b001161 | prose | pages [41] -->
Taking only the most basic and well-supported trends in the psychological and geographical

<!-- b001162 | prose | pages [41] -->
patterns of violent serial criminals, one ﬁnds that a basic estimate of a criminal’s next strike

<!-- b001163 | prose | pages [41] -->
point can be obtained from only the spatial-temporal coordinates of previous offenses. The twin

<!-- b001164 | prose | pages [41] -->
assumptions that a serial criminal has an “anchor point” (like a house), and to avoid detection,

<!-- b001165 | prose | pages [41] -->
he may tend to avoid committing crimes in his own backyard, have been used for years in

<!-- b001166 | prose | pages [41] -->
quantitative techniques to estimate a criminal’s home or other anchor point. We instead begin

<!-- b001167 | prose | pages [41] -->
with this likely anchor point location. Then, we use it to predict potential next-strike points by

<!-- b001168 | prose | pages [41] -->
presuming the distribution of crimes around the anchor will be described by a Γ function of the

<!-- b001169 | prose | pages [41] -->
radial distance from the anchor. The use of a Γ allows us to ﬁt the mean and variance to the

<!-- b001170 | prose | pages [41] -->
distribution to the points already on the grid. In this way, we create a buffer zone only when

<!-- b001171 | prose | pages [41] -->
the existing data suggest one, and with a size also deﬁned by existing data.

<!-- b001172 | prose | pages [41] -->
There is, however, nothing fundamental, about the single anchor point assumption, and

<!-- b001173 | prose | pages [41] -->
some research suggests it is not uncommon to ﬁnd more than one. We therefore also consider

<!-- b001174 | prose | pages [41] -->
a model which begins by searching for evidence of multiple anchor points. This model uses

<!-- b001175 | prose | pages [41] -->
cluster theory techniques to detect groups of points which have more in common with each

<!-- b001176 | prose | pages [41] -->
other than with the larger group. Then, we assume an additional anchor point at the center of

<!-- b001177 | prose | pages [41] -->
each cluster, and model each cluster with another gamma distribution. Weighting the clusters

<!-- b001178 | prose | pages [41] -->
relative to each other allows us to prioritize larger clusters or ones the criminal has visited more

<!-- b001179 | prose | pages [41] -->
recently.

<!-- b001180 | prose | pages [41] -->
Lacking any readily available, public-domain datasets, we extract data from past research

<!-- b001181 | prose | pages [41] -->
projects and test these two models on the cases of three serial rapists. We deﬁne a parameter

<!-- b001182 | prose | pages [41] -->
κs, which essentially represents how much better a police department would do in attempting

<!-- b001183 | prose | pages [41] -->
to stop the next crime if they distributed their energy and resources according to our model

<!-- b001184 | prose | pages [41] -->
rather than randomly. We ﬁnd evidence that our models are substantially better than simple

<!-- b001185 | prose | pages [41] -->
guessing, but it is not statistically signiﬁcant for the amount of data available to us.

<!-- b001186 | prose | pages [41] -->
Finally, we propose a method for treating a general serial crime data set, by testing both

<!-- b001187 | prose | pages [41] -->
models abilities to predict known points, and deciding which is most likely to succeed in future

<!-- b001188 | prose | pages [41] -->
predictions. This also allows us to calculate a new value, κs, which roughly represents our

<!-- b001189 | prose | pages [41] -->
conﬁdence in the model. A higher κs value indicates a higher degree of conﬁdence in future

<!-- b001190 | prose | pages [41] -->
predictions, although we demonstrate a real-world dataset where the presence of an outlier

<!-- b001191 | prose | pages [41] -->
contradicts our conﬁdence level.

<!-- b001192 | prose | pages [41] -->
On the whole, we believe we can produce a model which can beat a ”psychic and a hair

<!-- b001193 | prose | pages [41] -->
ﬁnder”– i.e., which can outperform random guesses and uniform distributions of resources. We

<!-- b001194 | prose | pages [41] -->
cannot, however, reasonably expect to beat an ”intuitive cop”; a human with a strong familiarity

<!-- b001195 | furniture | pages [42] -->
Team # 7507

<!-- b001196 | furniture | pages [42] -->
Page 41

<!-- b001197 | prose | pages [42] -->
of actual map underlying our abstract data points will always have access to information we

<!-- b001198 | prose | pages [42] -->
do not. Indeed, to be most effective, our model should be combined with this kind of human

<!-- b001199 | prose | pages [42] -->
intelligence.

<!-- b001200 | prose | pages [42] -->
Finally, it is important to note that there while predicting the next crime point is an interest-

<!-- b001201 | prose | pages [42] -->
ing mathematical problem and would be an excellent tool in theory, there may be many cases

<!-- b001202 | prose | pages [42] -->
where it is not the ideal approach in practice. When it is, we provide a potentially powerful

<!-- b001203 | prose | pages [42] -->
tool that can be used should to predict future crime locations.

<!-- b001204 | furniture | pages [43] -->
Team # 7507

<!-- b001205 | furniture | pages [43] -->
Page 42

<!-- b001206 | prose | pages [43] -->
11

<!-- b001207 | heading | pages [43] -->
Executive Summary

<!-- b001208 | prose | pages [43] -->
Overview: Strengths and Weaknesses of the Model

<!-- b001209 | prose | pages [43] -->
This paper presents a model of where a violent serial criminal will strike next, based upon

<!-- b001210 | prose | pages [43] -->
the locations and times of his previous crimes. Our algorithm creates a color-coded map of

<!-- b001211 | prose | pages [43] -->
the area surrounding the criminal’s previous strikes, with the color at each point indicating the

<!-- b001212 | prose | pages [43] -->
likelihood of a strike there. The model has several key strengths:

<!-- b001213 | prose | pages [43] -->
• The model contains no arbitrary parameters. In other words, most aspects of the

<!-- b001214 | prose | pages [43] -->
model are determined simply by trends which researchers have observed in many serial

<!-- b001215 | prose | pages [43] -->
criminals across many many datasets.

<!-- b001216 | prose | pages [43] -->
• The model can estimate the level of conﬁdence in its predictions. Before making a

<!-- b001217 | prose | pages [43] -->
prediction, our model ﬁrst checks how well it would have predicted the criminals previ-

<!-- b001218 | prose | pages [43] -->
ous crimes, in order to provide an estimate of how well it can predict his future crimes.

<!-- b001219 | prose | pages [43] -->
• The model understands that police have limited resources. In particular, the conﬁ-

<!-- b001220 | prose | pages [43] -->
dence number described above becomes large if we are making good predictions, but

<!-- b001221 | prose | pages [43] -->
will shrink again if our predicted areas is so large as to become unhelpful.

<!-- b001222 | prose | pages [43] -->
At the same time, it must be observed that our model contains some fundamental limita-

<!-- b001223 | prose | pages [43] -->
tions:

<!-- b001224 | prose | pages [43] -->
• The model is only clearly applicable to violent serial criminals. We only claim appli-

<!-- b001225 | prose | pages [43] -->
cability in the case of serial killers and rapists, as our research shows serial burglars and

<!-- b001226 | prose | pages [43] -->
arsonists are more unpredictable and inﬂuenced by non-geographic factors.

<!-- b001227 | prose | pages [43] -->
The model cannot predict when a criminal will strike. While we do consider the •

<!-- b001228 | prose | pages [43] -->
order of previous crimes in our model in order to predict locations, we do not predict a

<!-- b001229 | prose | pages [43] -->
strike time.

<!-- b001230 | prose | pages [43] -->
• The model cannot make use of underlying map data. To maintain generality, we do

<!-- b001231 | prose | pages [43] -->
not make any assumptions about the underlying physical geography. A human being

<!-- b001232 | prose | pages [43] -->
must interpret the output (for example, choosing to ignore a prediction in the middle of

<!-- b001233 | prose | pages [43] -->
a lake).

<!-- b001234 | prose | pages [43] -->
The model has not been validated on a large set of empirical data. The fact is, •

<!-- b001235 | prose | pages [43] -->
sizable sets of data on serial criminals are not widely available. Any police department

<!-- b001236 | prose | pages [43] -->
using this model should test it on a large number of previous cases ﬁrst, as described in

<!-- b001237 | prose | pages [43] -->
our paper.

<!-- b001238 | furniture | pages [44] -->
Team # 7507

<!-- b001239 | furniture | pages [44] -->
Page 43

<!-- b001240 | prose | pages [44] -->
In addition, the standard warnings that would apply to any geographic proﬁling scheme

<!-- b001241 | prose | pages [44] -->
apply: The output should not be treated as a single prediction, but rather as a tool to help

<!-- b001242 | prose | pages [44] -->
prioritize areas of focus. It is designed to do well on average, but may fail in outlier cases.

<!-- b001243 | prose | pages [44] -->
And to implement it reliably, it must be paired with a human assessment. Please note also

<!-- b001244 | prose | pages [44] -->
that models for predicting the offenders “home base” are much more well-researched, and in

<!-- b001245 | prose | pages [44] -->
general will be more accurate than any algorithm claiming to predict the next strike point. A

<!-- b001246 | prose | pages [44] -->
police department should choose which model type to use on a case-by-case basis.

<!-- b001247 | prose | pages [44] -->
Internal Workings of the Model

<!-- b001248 | prose | pages [44] -->
Inputs

<!-- b001249 | prose | pages [44] -->
Our model requires the coordinate locations of a serial criminal’s previous offenses, as well as

<!-- b001250 | prose | pages [44] -->
the order in which these crimes were committed.

<!-- b001251 | prose | pages [44] -->
Assumpitons

<!-- b001252 | prose | pages [44] -->
1. The Criminal will tend to strike at locations around one or more “anchor points.” (often,

<!-- b001253 | prose | pages [44] -->
the criminal’s house).

<!-- b001254 | prose | pages [44] -->
2. Around this anchor point, there may be a “buffer zone” within which he will not strike.

<!-- b001255 | prose | pages [44] -->
3. If the criminal has multiple anchor points, the regions around those from which he has

<!-- b001256 | prose | pages [44] -->
struck most often or most recently are more likely.

<!-- b001257 | prose | pages [44] -->
Method

<!-- b001258 | prose | pages [44] -->
The algorithm implements two different models, and then decides which is better.

<!-- b001259 | prose | pages [44] -->
• In the ﬁrst method, we assume the criminal has a single anchor point, and build likelihood

<!-- b001260 | prose | pages [44] -->
regions around the anchor point based on the distribution of his past crimes.

<!-- b001261 | prose | pages [44] -->
• In the second, we assume multiple anchor points, calculate the best number of anchor

<!-- b001262 | prose | pages [44] -->
points to use, and determine likelihood around each point individually. Then area around

<!-- b001263 | prose | pages [44] -->
each is weighted by the criminal’s apparent preferences, if any.

<!-- b001264 | prose | pages [44] -->
Finally, the algorithm tests both models to see how well they would have predicted the

<!-- b001265 | prose | pages [44] -->
previous crimes, and uses the model with the better track record.

<!-- b001266 | prose | pages [44] -->
Summary and Recommendations

<!-- b001267 | prose | pages [44] -->
While our model needs more real-world testing, its strong theoretical basis, self-evaluation

<!-- b001268 | prose | pages [44] -->
scheme and awareness of practical considerations make it a good option for a police department

<!-- b001269 | prose | pages [44] -->
looking to forecast a criminal’s next strike. Combining its results with the intuition of a human

<!-- b001270 | prose | pages [44] -->
being will maximize its utility.

<!-- b001271 | furniture | pages [45] -->
Team # 7507

<!-- b001272 | furniture | pages [45] -->
Page 44

<!-- b001273 | heading | pages [45] -->
References

<!-- b001274 | references | pages [45] -->
[1] R. Boba. Crime analysis and crime mapping. Sage, 2005.

<!-- b001275 | references | pages [45] -->
[2] D. Canter, T. Coffey, M. Huntley, and C. Missen. Predicting serial killers’ home base

<!-- b001276 | references | pages [45] -->
using a decision support system. Journal of Quantitative Criminology, 16(4):457–478,

<!-- b001277 | references | pages [45] -->
2000.

<!-- b001278 | references | pages [45] -->
[3] D. Canter and P. Larkin. The environmental range of serial rapists. Journal of Environ-

<!-- b001279 | references | pages [45] -->
mental Psychology, 13:63–63, 1993.

<!-- b001280 | references | pages [45] -->
[4] G.M. Godwin and F. Rosen. Tracker: hunting down serial killers. Running Press, 2005.

<!-- b001281 | references | pages [45] -->
[5] R.V. Hogg, A.T. Craig, and J. McKean. Introduction to mathematical statistics. 1978.

<!-- b001282 | references | pages [45] -->
[6] R.M. Holmes. Contemporary perspectives on serial murder. Sage Pubns, 1998.

<!-- b001283 | references | pages [45] -->
[7] AK Jain, MN Murty, and PJ Flynn. Data clustering: a review. ACM computing surveys

<!-- b001284 | references | pages [45] -->
(CSUR), 31(3):264–323, 1999.

<!-- b001285 | references | pages [45] -->
[8] R.N. Kocsis and H.J. Irwin.

<!-- b001286 | references | pages [45] -->
Analysis of Spatial Patterns in Serial Rape, Arson, and

<!-- b001287 | references | pages [45] -->
Burglary: The Utility of the Circle Theory of Environmental Range for Psychological

<!-- b001288 | references | pages [45] -->
Proﬁling, An. Psychiatry Psychol. & L., 4:195, 1997.

<!-- b001289 | references | pages [45] -->
[9] J.L. LeBeau. Four case studies illustrating the spatial-temporal analysis of serial rapists.

<!-- b001290 | references | pages [45] -->
Police Stud.: Int’l Rev. Police Dev., 15:124, 1992.

<!-- b001291 | references | pages [45] -->
[10] T.P. Minka. Estimating a Gamma distribution. 2002.

<!-- b001292 | references | pages [45] -->
[11] Derek J. Paulsen. Predicting next event locations in a time sequence using advanced

<!-- b001293 | references | pages [45] -->
spatial prediction methods. In 1005 UK Crime Mapping Conference, 2005.

<!-- b001294 | references | pages [45] -->
[12] D.J. Paulsen and M.B. Robinson. Crime mapping and spatial aspects of crime. Prentice

<!-- b001295 | references | pages [45] -->
Hall.

<!-- b001296 | references | pages [45] -->
[13] D.K. Rossmo. Geographic proﬁling: Target patterns of serial murderers. PhD thesis,

<!-- b001297 | references | pages [45] -->
Simon Fraser University, 1995.

<!-- b001298 | references | pages [45] -->
[14] D.K. Rossmo. NCIS Conference. 1998.

<!-- b001299 | references | pages [45] -->
[15] D.K. Rossmo. Geographic proﬁling. CRC, 1999.

<!-- b001300 | references | pages [45] -->
[16] P.J. Rousseeuw. Silhouettes: A graphical aid to the interpretation and validation of cluster

<!-- b001301 | references | pages [45] -->
analysis. Journal of computational and applied mathematics, 20(1):53–65, 1987.

<!-- b001302 | furniture | pages [46] -->
Team # 7507

<!-- b001303 | furniture | pages [46] -->
Page 45

<!-- b001304 | references | pages [46] -->
[17] B. Snook, R.M. Cullen, A. Mokros, and S. Harbort. Serial murderers spatial decisions:

<!-- b001305 | references | pages [46] -->
Factors that inﬂuence crime location choice. Journal of Investigative Psychology and

<!-- b001306 | references | pages [46] -->
Offender Proﬁling, 2(3), 2005.

<!-- b001307 | references | pages [46] -->
[18] B. Snook, P.J. Taylor, and C. Bennell. Geographic proﬁling: The fast, frugal, and accurate

<!-- b001308 | references | pages [46] -->
way. Applied Cognitive Psychology, 18(1):105–121, 2004.
