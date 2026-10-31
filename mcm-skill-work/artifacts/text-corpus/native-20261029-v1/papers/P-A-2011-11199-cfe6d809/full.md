# P-A-2011-11199-cfe6d809

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | title | pages [1] -->
Designing the Optimal

<!-- b000003 | title | pages [1] -->
Snowboard Half-Pipe

<!-- b000004 | title | pages [1] -->
Mathematical Contest in Modeling

<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | prose | pages [1] -->
Group # 11199

<!-- b000007 | prose | pages [1] -->
2/14/2011

<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | furniture | pages [1] -->


<!-- b000012 | furniture | pages [1] -->


<!-- b000013 | furniture | pages [1] -->


<!-- b000014 | furniture | pages [2] -->
Team # 11199

<!-- b000015 | furniture | pages [2] -->


<!-- b000016 | furniture | pages [2] -->
2

<!-- b000017 | heading | pages [2] -->
I. Introduction

<!-- b000018 | heading | pages [2] -->
I.1 Introduction to Problem

<!-- b000019 | prose | pages [2] -->
Since its introduction in the Winter Olympic Games in 1998, the popularity of half-pipe snowboarding competitions has surged. i At the Turin 2006 Olympic Winter Games, snowboarding competitions posted the second-highest average viewer hours per day of competition (Figure 1). It is widely believed that, when released, the comparable statistics for the Vancouver 2010 Olympic Winter Games will show even greater proportional viewership of snowboarding events. The objective of competitive half-pipe snowboarding is to perform well-executed, unique routines comprised of challenging aerial acrobatic manoeuvres that are executed as high in the air as possible.ii Similar to figure skating, half-pipe snowboard competitions are adjudicated events, whereby a panel of judges assign each competitor’s performance a subjective score. Recent studies of elite half-pipe snowboarding competitions have confirmed that total air-time (TAT) and average degree of rotation (ADR) are the key performance variables that best correlate with an athlete’s subjectively judged score.iii For this reason, there is broad interest in designing snowboard courses that optimize one or both of these key performance variables. This paper seeks to design such courses, using both heuristic and mathematical arguments, which are supported by simulations.

<!-- b000020 | furniture | pages [2] -->


<!-- b000021 | caption | pages [2] -->
Figure 1: Average Viewer Hours per Day of Competition, Turin 2006 Olympic Winter Gamesiv

<!-- b000022 | prose | pages [2] -->
I.2 Current Half-Pipe Engineering & Dimensions

<!-- b000023 | prose | pages [2] -->
To understand half-pipe engineering dimensions, one must first familiarize themselves with the components of a half-pipe (Figure 2). The “deck” can only be used for very few tricks that are less concerned with air time or rotation (and thus produce paltry scores). Its main purpose is for the safety of the riders. Thus, altering the shape of the deck is less relevant for the objective of this paper, and we will incorporate the average dimensions of existing half-pipe decks in our structure.

<!-- b000024 | furniture | pages [2] -->


<!-- b000025 | caption | pages [2] -->
Figure 2: Components of a Half-Pipe (Not to Scale)v

<!-- b000026 | furniture | pages [3] -->
Team # 11199

<!-- b000027 | furniture | pages [3] -->


<!-- b000028 | furniture | pages [3] -->


<!-- b000029 | furniture | pages [3] -->
3

<!-- b000030 | prose | pages [3] -->
Currently, no governing body of major half-pipe snowboard competitions, including the International Olympic Committee (Olympics) and ESPN (Winter X Games), have established strict requirements for the dimensions of half-pipe courses. In fact, in each of the last four Olympics that snowboarding competitions have been a part of, the half-pipe courses have had uniquely different dimensions (Figure 3).

<!-- b000031 | prose | pages [3] -->
Approximate Course Specifications Olympic Event

<!-- b000032 | prose | pages [3] -->
Average Inner Wall Length (m) Gradient (°) Host City Year

<!-- b000033 | prose | pages [3] -->
1998 Nagano 120 2002 Salt Lake 160 2006 Torino 145 2010 Vancouver 160

<!-- b000034 | prose | pages [3] -->
Width (m) Height (m)

<!-- b000035 | prose | pages [3] -->
18.0 15.0 3.5 n/a 16.5 4.5 16.5 n/a 5.7 18.0 18.0 6.0

<!-- b000036 | furniture | pages [3] -->


<!-- b000037 | caption | pages [3] -->
Figure 3: Half-Pipe Dimensions for 1998, 2002, 2006, and 2010 Winter Olympic Gamesvi,vii,viii,ix

<!-- b000038 | prose | pages [3] -->
However, as observed in Figure 3, a general trend has been an increase in the overall “wall” height (as measured from “floor” to “coping”). The most popular courses recently are 22 foot-tall ‘super pipes’, which are shaped using specialized snow-carving machines (Figure 4). The world’s largest supplier of such machines, in conjunction with the International Ski Federation, has published a document outlining recommended course dimensions, according to the desired wall height (Figure 5).

<!-- b000039 | prose | pages [3] -->
Quarter Pipe Extension

<!-- b000040 | prose | pages [3] -->
New 22 Foot Monster

<!-- b000041 | heading | pages [3] -->
18 Foot Monster

<!-- b000042 | prose | pages [3] -->
Base

<!-- b000043 | heading | pages [3] -->
22 Ft.

<!-- b000044 | heading | pages [3] -->
18 Ft.

<!-- b000045 | furniture | pages [3] -->


<!-- b000046 | furniture | pages [3] -->


<!-- b000047 | furniture | pages [3] -->


<!-- b000048 | caption | pages [3] -->
Figure 4: ‘Super Pipe’ Snow-Carving Machinex              Figure 5: Recommended Half-Pipe Dimensions,

<!-- b000049 | furniture | pages [3] -->


<!-- b000050 | prose | pages [3] -->
Zaugg AG & International Ski Federationxi

<!-- b000051 | heading | pages [3] -->
II. Maximizing Vertical Air – Design and Implementation of Models

<!-- b000052 | prose | pages [3] -->
It is clear from the above Figure 5 that the problem at hand is an interesting one, as there are many variables about the course design that can be altered. Moreover, simplifying assumptions including: no friction, no downward sloping angle of the course (i.e. flat), and those listed below, yield results that are dramatically

<!-- b000053 | furniture | pages [4] -->
Team # 11199

<!-- b000054 | furniture | pages [4] -->


<!-- b000055 | furniture | pages [4] -->
4

<!-- b000056 | prose | pages [4] -->
different than those when these simplifying assumptions are removed. The assumptions/constraints that we hold constant for all discussed course designs in this paper include:

<!-- b000057 | heading | pages [4] -->
1. Symmetry: To be a ‘fair’ course, the half-pipe cross-section must be symmetric to accommodate

<!-- b000058 | prose | pages [4] -->
both right- and left-footed snowboarders. This also allows boarders to perform multiple jumps on either side of the course, which enhances the overall audience entertainment factor.

<!-- b000059 | furniture | pages [4] -->


<!-- b000060 | heading | pages [4] -->
2. Rigid & Inelastic Body: The snowboarder mounted on her snowboard is assumed to be a rigid and

<!-- b000061 | prose | pages [4] -->
inelastic body. As such, “Amonton’s Second Law” tells us that the force of friction is independent of the surface area of contact between the snowboard and snow, as well as that of the athlete and air. Thus, a “corrugated” surface that incorporates small groves parallel to the direction of the course’s slope would produce the same work done by friction as a “smooth” surface. Moreover, this suggests that work done by friction is independent of the shape of the snowboard/athlete.

<!-- b000062 | furniture | pages [4] -->


<!-- b000063 | heading | pages [4] -->
3. Point Mass: In addition to the above assumption, the snowboarder and her board are assumed to be

<!-- b000064 | prose | pages [4] -->
a single point-mass that moves along the surface of the half-pipe. This is a reasonable assumption, since it only eliminates the consideration of rotational energy from the model.

<!-- b000065 | furniture | pages [4] -->


<!-- b000066 | heading | pages [4] -->
4. Friction Model: The “Coulomb model” is used to describe the frictional force that acts on the

<!-- b000067 | prose | pages [4] -->
snowboarder throughout the course. In such a model, the frictional force is proportional to the normal force.

<!-- b000068 | furniture | pages [4] -->


<!-- b000069 | heading | pages [4] -->
5. Continuity: The curve that describes the surface of the course’s cross-section must be smooth or

<!-- b000070 | prose | pages [4] -->
piecewise continuous. If the curve was allowed to have discontinuities, such as a ‘hole’ or an ‘instantaneously vertical wall of snow’, then the snowboarder (assumed to be a point mass), would either ‘fall into the hole’ or ‘slam into a wall of snow.’

<!-- b000071 | furniture | pages [4] -->


<!-- b000072 | heading | pages [4] -->
6. Course Slope: As “vertical air” is defined as the component of height achieved relative to the

<!-- b000073 | prose | pages [4] -->
copings that is perpendicular to the length of the course (which is sloped), we are only concerned with designing the shape of the cross-section of the half-pipe. Theoretically, if the course was infinitely steep (i.e. vertical), then total air time would be large, since there would be a horizontal component of air achieved (the snowboarder would essentially be in free-fall for a vertical course). However, this horizontal component of air is not our variable of interest. The only relevant model is the total air achieved if the snowboarder oscillated in a flat (0° incline) cross-section of the half-pipe.

<!-- b000074 | furniture | pages [4] -->


<!-- b000075 | heading | pages [4] -->
7. Cross-Section Shape: The curvature of the surface of the course’s cross-section must point towards

<!-- b000076 | prose | pages [4] -->
the “inside” of the half-pipe. That is to say, the curve must be concave. In addition, the ends of the curve (i.e. “copings”) must be approximately vertical so that the snowboarder is launched into the air at an angle as close to perpendicular as possible. Since elite snowboarders perform a technique known as “pumping” whereby they push off with their legs at the copings, it is best for the angle of the curve at the copings to be slightly less than 90° to the horizontal.xii

<!-- b000077 | heading | pages [4] -->
II.1 Frictionless Models

<!-- b000078 | prose | pages [4] -->
Vertical Air Model 1.1 – No Friction (No Fixed Height and/or No Fixed Width)

<!-- b000079 | prose | pages [4] -->
The simplest model is one in which there is no friction acting on the snowboarder. Under such a model, by the law of conservation of energy, none of the potential energy from starting at the top of the hill is lost to work done by friction. Thus, as the rider progresses down the hill, all of the initial potential energy is converted into kinetic energy. It is easiest to consider the cross-section of a course, and momentarily ignore the downward slope of the course. In such a model, we view the snowboarder as oscillating from one side of the half-pipe to the other. Since there is no friction, this system experiences no dampening and thus achieves the same vertical air with each oscillation. If we were to assume that this course was shaped as a half-circle,

<!-- b000080 | furniture | pages [5] -->
Team # 11199

<!-- b000081 | furniture | pages [5] -->


<!-- b000082 | furniture | pages [5] -->


<!-- b000083 | furniture | pages [5] -->
5

<!-- b000084 | prose | pages [5] -->
then this model is equivalent to imagining the snowboarder as being a mass on the end of a pendulum, whose length is equal to the radius of the half-circle (i.e. the course height).

<!-- b000085 | prose | pages [5] -->
If we align the copings of the course as having a “reference height of 0,” then there is zero potential energy when starting the course from one of the copings. As such, since no work is lost to friction, and the course must be symmetric, any kinetic energy achieved when leaving the coping opposite the ‘starting point’ coping must be a result of kinetic energy when initially entering the course. Thus, if we assume the positioning of any curve at a reference height of 0, as well as a fixed initial kinetic energy, the vertical air achieved will be independent of the curve of the cross-section.

<!-- b000086 | heading | pages [5] -->
Vertical Air Model 1.2 – No Friction (Fixed Height & Fixed Width)

<!-- b000087 | prose | pages [5] -->
Now we assume the same model as above, but add the caveat that the course must be of fixed height (݄) and width (2݈). Since the course must be symmetric, we can therefore think of this as the need to pick a curve that passes through points ܣ, ܤ, and ܥ. Three possible profiles for such a half-pipe are outlined in Figure 6. For the bottommost candidate profile, one must imagine adding an infinitesimally small quarter of a circle in each corner, thus allowing the vertical speed to be transformed into horizontal speed. This profile would be dangerous for athletes, as they would experience unmanageable G-forces at the corners; however it would allow the athlete to pick up a great deal of speed very quickly. The topmost path consists of two straight line segments connecting the required points, and therefore has the shortest arc length of the plotted candidates.

<!-- b000088 | furniture | pages [5] -->


<!-- b000089 | caption | pages [5] -->
Figure 6: Three Sample Candidate Profiles for Half-Pipe with Fixed Height and Widthxiii

<!-- b000090 | prose | pages [5] -->
We know from Model 1.1 that the curve chosen does not alter the amount of vertical air that can be achieved. However, from a spectator’s perspective, watching a slow-moving snowboarder would not be entertaining. The question then becomes, can we find the shape of the curve that permits the athlete to travel through all three points in the least amount of time? This famous problem is known as the “brachistochrone,” which ultimately launched a field of mathematics known as calculus of variations. Due to the symmetry assumption, this is the same problem as solving for the first half of the curve. Without loss of generality, we set fixed ଵሺ݈,݄ ሻ in the Euclidean plane (with the convention that downward moves in ଴ሺ0,0ሻ and ܤൌܲ points ܣൌܲ the ݕ-axis are positive). The kinetic energy of the sliding body of mass at each instant must equal the potential energy lost from the initial height (by law of conservation of total energy). In order words, ݒଶൌ݉݃ ܧ௄ሺܲ௡ሻൌሺ1/2ሻ݉ ݕ, where ݃ is the acceleration due to gravity. We therefore see that ݒൌඥ2݃ݕ. From multivariate calculus we also know that the arc length of the curve; ݕൌݕሺݔሻ, ݔ଴൑ݔ൑ݔ் is:

<!-- b000091 | prose | pages [5] -->
௫೅

<!-- b000092 | prose | pages [5] -->
ൌන݀ ݎܿ ݈݁݊݃ ݐ݄

<!-- b000093 | prose | pages [5] -->
௫బ

<!-- b000094 | prose | pages [5] -->
௫೅

<!-- b000095 | prose | pages [5] -->
ඥ1 ൅ሾݕ′ሿଶ݀ݔ ൌන

<!-- b000096 | prose | pages [5] -->
ݏ ݏ

<!-- b000097 | furniture | pages [5] -->


<!-- b000098 | prose | pages [5] -->
௫బ

<!-- b000099 | prose | pages [5] -->
଴ሺ0,0ሻ to position ܤൌܲ ଵሺ݈, ݄ ሻ is: Thus in our problem, the total time, ܶ, needed to move from ܣൌܲ

<!-- b000100 | furniture | pages [6] -->
Team # 11199

<!-- b000101 | prose | pages [6] -->
ݏݐܽ݊ܿ݁ ݐݎܽݒ݈݈݁݁݀ ൌන݀݅ ݏ݌݁݁݀

<!-- b000102 | furniture | pages [6] -->


<!-- b000103 | furniture | pages [6] -->


<!-- b000104 | furniture | pages [6] -->
6

<!-- b000105 | prose | pages [6] -->
௟

<!-- b000106 | prose | pages [6] -->
ݒൌනඥ1 ൅ሾݕᇱሿଶ

<!-- b000107 | prose | pages [6] -->
ൌන݀ݏ

<!-- b000108 | prose | pages [6] -->
ݔ

<!-- b000109 | prose | pages [6] -->
ඥ2݃ݕ

<!-- b000110 | prose | pages [6] -->
଴

<!-- b000111 | prose | pages [6] -->
Our objective is to find the curve ݕൌݕሺݔሻ that minimizes ܶ. Using the Euler-Lagrange equation we have:

<!-- b000112 | prose | pages [6] -->
ሾݕᇱሿଶ

<!-- b000113 | prose | pages [6] -->
൱െቌ൫ݕ′൯߲߲ݕԢ ൭ඥ1 ൅ሾݕᇱሿଶ

<!-- b000114 | prose | pages [6] -->
ൌ൭ඥ1 ൅ሾݕᇱሿଶ ଵඥ2݃ ଶൌܿ

<!-- b000115 | prose | pages [6] -->
ඥݕ

<!-- b000116 | prose | pages [6] -->
൱ቍൌ൭ඥ1 ൅ሾݕᇱሿଶ

<!-- b000117 | prose | pages [6] -->
൱െ൭

<!-- b000118 | prose | pages [6] -->
ඥݕඥ1 ൅ሾݕᇱሿଶ൱

<!-- b000119 | prose | pages [6] -->
ඥݕ

<!-- b000120 | prose | pages [6] -->
ඥݕ

<!-- b000121 | prose | pages [6] -->
ଶ are constants. Multiplying both sides by factor ඥݕඥ1 ൅ሾݕᇱሿଶ and then squaring yields: where ܿଵ and ݕሺ1 ൅ሾݕᇱሿଶሻൌሺ1/ܿଶሻଶൌߛ. Solving for ݕᇱ, we get: ݕԢ ൌ݀ ݕ/݀ݔൌඥሺߛെݕሻ/ݕ. Now we change variables such that: ඥݕ/ሺߛെݕሻൌtan ሺ߮ሻ. Isolating for ݕ, we get: ݕൌߛsinଶሺ߮ሻ. Use chain rule as follows:

<!-- b000122 | prose | pages [6] -->
ݕ݀ 1 1 1 2ߛሺsinሺ߮ሻሻሺcos ሺ߮ሻሻ· ݔൌ݀߮݀ ݕ· ݔൌ

<!-- b000123 | prose | pages [6] -->
We re-write the above as: ݀ݔൌ2ߛሺsinଶሺ߮ሻሻ݀߮

<!-- b000124 | prose | pages [6] -->
ሺtan ሺ߮ሻሻൌ 2ߛሺsinଶሺ߮ሻሻ

<!-- b000125 | prose | pages [6] -->
, indicating a relationship between two infinitesimal values ݔ and . Integrate both sides to get:

<!-- b000126 | prose | pages [6] -->
ൌ2ߛቆ߮2 െsinሺ2߮ሻ

<!-- b000127 | prose | pages [6] -->
ݔൌන݀ݔൌ2ߛන1 െcos ሺ2߮ሻ

<!-- b000128 | prose | pages [6] -->
2݀߮

<!-- b000129 | prose | pages [6] -->
ቇ൅ܿ ଷ    ሺܿଷ:ܿ݋݊ݏݐܽ݊ ݐሻ 4

<!-- b000130 | prose | pages [6] -->
଴ሺ0,0ሻ as the initial point of the trajectory, we can fix ܿଷ. At ܲ଴ሺ0,0ሻ, we have: By having chosen point ܣൌܲ ଶሺ߮ሻ, and thus ݕൌ0 ൌߛݏ݅݊ ൌ0, േ1, േ2, … Plugging in ൌ݇ ߨ,݇

<!-- b000131 | prose | pages [6] -->
ୱ୧୬ሺଶ·଴ሻ

<!-- b000132 | prose | pages [6] -->
଴

<!-- b000133 | prose | pages [6] -->
gives: ݔൌ0 ൌ2ߛቀ

<!-- b000134 | prose | pages [6] -->
ቁ൅ܿ

<!-- b000135 | prose | pages [6] -->
ଶെ

<!-- b000136 | prose | pages [6] -->
ଷൌܿ ଷ. Thus ସ

<!-- b000137 | prose | pages [6] -->
ൌ0 into the above equation for ݔ

<!-- b000138 | prose | pages [6] -->
ଷൌ0. After introducing another change of variables ൌߠ, we get the parametric equations: where: ߛ/2 ൌݎ and 2

<!-- b000139 | prose | pages [6] -->
൜ݔൌݎሺߠെݏ݅݊ ߠሻ ݕൌݎሺߠെܿ݋ݏߠሻ

<!-- b000140 | prose | pages [6] -->
This is the parameterized set of equations describing a shape known as a “cycloid,” which can be thought of as the curve traced by a red dot on a ball of radius ݎ as it rolls along the ݔ-axis (Figure 7). Thus, assuming no friction and a fixed height and width, the ideal half-pipe – from an entertainment perspective in which we minimize the time of oscillations from coping to coping – is a cycloid.

<!-- b000141 | furniture | pages [6] -->


<!-- b000142 | caption | pages [6] -->
Figure 7: Construction of a Cycloidxiv

<!-- b000143 | heading | pages [6] -->
II.2 Models with Friction

<!-- b000144 | prose | pages [6] -->
Prior to introducing our models that include the work done by friction, we must introduce some notation and simple balance equations.

<!-- b000145 | furniture | pages [7] -->
Team # 11199

<!-- b000146 | furniture | pages [7] -->


<!-- b000147 | furniture | pages [7] -->


<!-- b000148 | furniture | pages [7] -->
7

<!-- b000149 | prose | pages [7] -->
travels along the half-pipe's cross section given by an arbitrary curve, Assume the snowboarder of mass ݎԦሺݏሻ, parameterized by the arc length, ݏ. Establish the co-ordinate system in the Euclidean plane, where ݔ is positive in the right direction and ݕ is positive in the downward direction. At any point on the curve, define the tangential unit vector, the normal unit vector, and curvature using the familiar formulas:

<!-- b000150 | prose | pages [7] -->
ݐ݋ݎൌܶሬԦሺݏሻൌݎԦ′ሺݏሻ ݐ ݒ݁ܿ

<!-- b000151 | prose | pages [7] -->
|ݎԦ′ሺݏሻ| ;   ܰ݋ݎ݈݉ܽ ݒ݁ܿ

<!-- b000152 | prose | pages [7] -->
ሬԦ′ሺݏሻ

<!-- b000153 | prose | pages [7] -->
ሺݏሻൌหܶሬԦ′ሺݏሻห

<!-- b000154 | prose | pages [7] -->
ݐ݋ݎൌ݊ሬԦሺݏሻൌܶ

<!-- b000155 | prose | pages [7] -->
;  ܥݑݎݒܽݐݑݎ݁ ൌࣥ

<!-- b000156 | prose | pages [7] -->
หܶሬԦ′ሺݏሻห

<!-- b000157 | prose | pages [7] -->
We use the following free-body diagram to illustrate the three forces acting on the snowboarder at any particular point on the curve (Figure 8).

<!-- b000158 | prose | pages [7] -->
Frictional Force

<!-- b000159 | prose | pages [7] -->
θ

<!-- b000160 | prose | pages [7] -->
mgsin(θ) =

<!-- b000161 | prose | pages [7] -->
x+

<!-- b000162 | prose | pages [7] -->
Normal Force

<!-- b000163 | prose | pages [7] -->
y+

<!-- b000164 | prose | pages [7] -->
Gravitational Force

<!-- b000165 | prose | pages [7] -->
θ

<!-- b000166 | prose | pages [7] -->
mgcos(θ)=

<!-- b000167 | prose | pages [7] -->
= mg

<!-- b000168 | furniture | pages [7] -->


<!-- b000169 | caption | pages [7] -->
Figure 8: Free-Body Diagram of Snowboarder at a Particular Angle, ߠ, Relative to the Horizontal Axis

<!-- b000170 | prose | pages [7] -->
ݒଶ, Basic physics laws tell us that the net force in the direction ݊ሬԦ equals the centripetal force, ௖ൌ݉ࣥ ௖ is the centripetal acceleration, ݒ is the speed of the snowboarder and where is the curvature of the , acts in the centripetal direction, while the a component of gravitational surface. Since the normal force, ݒଶ. Since the sinሺߠሻሿൌ݉ࣥ sinሺߠሻ, acts against the centripetal direction, we have: [ force, െ݉݃ frictional force is proportional to the normal force by a (constant) coefficient of friction, ߤ, we have:

<!-- b000171 | prose | pages [7] -->
ܨሺݏሻൌߤܰሺݏሻൌߤሾ݉݃ ሺݏሻݒଶሺݏሻሿ sinሺߠሺݏሻሻ൅݉ࣥ

<!-- b000172 | prose | pages [7] -->
We also know that by law of conservation of energy, the total initial energy of the snowboarder equals the total mechanical (kinetic plus potential) energy at some later point plus the total work done by friction up ݒଶሺݏሻ, and ܧ௉ሺݏሻൌ݉݃ until that point. Let ܧ௄ሺݏሻൌሺ1/2ሻ݉ ݎ௬ሺݏሻ be functions with respect to arc length, ݏ, representing kinetic and potential energy, respectively. Then we represent the law of conservation of energy mathematically by:

<!-- b000173 | prose | pages [7] -->
௦

<!-- b000174 | prose | pages [7] -->
ሼܶܧሺ0ሻൌܧ௄ሺ0ሻ൅ܧ௉ሺ0ሻሽ ൌቊܶܧሺݏሻൌܧ௄ሺݏሻ൅ܧ௉ሺݏሻ൅නܨሺݑሻ݀ݑ

<!-- b000175 | prose | pages [7] -->
ቋ

<!-- b000176 | prose | pages [7] -->
଴

<!-- b000177 | prose | pages [7] -->
where the last term represents the total heat energy, or energy lost to friction along the curve from 0 to ݏ. Without loss of generality, we can orient the curve in a manner such that we set the initial potential energy to be zero (ܧ௉ሺ0ሻൌ0). Further, we assume an initial speed of ݒሺ0ሻ. Using this and re-arranging the above equation, we get:

<!-- b000178 | furniture | pages [8] -->
Team # 11199

<!-- b000179 | furniture | pages [8] -->


<!-- b000180 | furniture | pages [8] -->


<!-- b000181 | furniture | pages [8] -->
8

<!-- b000182 | prose | pages [8] -->
௦

<!-- b000183 | prose | pages [8] -->
ܧ௄ሺݏሻൌܧ௉ሺ0ሻ൅ሺ0ሻ൅ܧ௉ሺݏሻെනܨሺݑሻ݀ݑ

<!-- b000184 | prose | pages [8] -->
ܧ௄ሺݏሻൌ 1

<!-- b000185 | prose | pages [8] -->
ݒଶሺ0ሻ൅݉݃

<!-- b000186 | furniture | pages [8] -->


<!-- b000187 | prose | pages [8] -->
଴

<!-- b000188 | prose | pages [8] -->
௦

<!-- b000189 | prose | pages [8] -->
ሺݑሻݒଶሺݑሻሿ݀ݑ ݎ௬ሺݏሻെߤනሾ݉݃ 2݉

<!-- b000190 | prose | pages [8] -->
ܧ௄ሺݏሻൌ 1

<!-- b000191 | prose | pages [8] -->
ݒଶሺ0ሻ൅݉݃

<!-- b000192 | prose | pages [8] -->
sinሺߠሺݑሻሻ൅݉ࣥ

<!-- b000193 | furniture | pages [8] -->


<!-- b000194 | prose | pages [8] -->
଴ ଴

<!-- b000195 | prose | pages [8] -->
௦

<!-- b000196 | prose | pages [8] -->
௦

<!-- b000197 | prose | pages [8] -->
ߤනsin൫ߠሺݑሻ൯݀ݑ ݎ௬ሺݏሻെ݉݃ 2݉

<!-- b000198 | prose | pages [8] -->
ሺݑሻܧ௄ሺݑሻ݀ݑ െ2ߤනࣥ

<!-- b000199 | furniture | pages [8] -->


<!-- b000200 | prose | pages [8] -->
଴ ଴

<!-- b000201 | prose | pages [8] -->
଴

<!-- b000202 | prose | pages [8] -->
where ݎ௬ሺݏሻ is the ݕ-component net distance traveled (in the downward direction) of the parametric curve. Note that the sinሾߠሺݑሻሿ݀ݑ term in the first integral represents the infinitesimal distance travelled in the horizontal direction, which we can re-write as ݀ݎ௫ሺݑሻ. Thus, the equation becomes:

<!-- b000203 | prose | pages [8] -->
ܧ௄ሺݏሻൌ 1

<!-- b000204 | prose | pages [8] -->
ݒଶሺ0ሻ൅݉݃ ݎ௬ሺݏሻെ݉݃ 2݉

<!-- b000205 | prose | pages [8] -->
௦

<!-- b000206 | prose | pages [8] -->
௦

<!-- b000207 | prose | pages [8] -->
ሺݑሻܧ௄ሺݑሻ݀ݑ

<!-- b000208 | prose | pages [8] -->
ߤනݎ௫ሺݑሻ݀ሺݑሻ

<!-- b000209 | prose | pages [8] -->
െ2ߤනࣥ

<!-- b000210 | furniture | pages [8] -->


<!-- b000211 | prose | pages [8] -->
଴

<!-- b000212 | prose | pages [8] -->
଴

<!-- b000213 | prose | pages [8] -->
The value of interest is the kinetic energy at the end of the curve of arc length ݏ, ܧ௄ሺݏ்ை்஺௅ሻ, where ݏ்ை்஺௅ is the total arc length of the entire cross-section from one coping to the other. Since the course is symmetric, at the “exit” coping we know that ݎ௬ሺݏ்ை்஺௅ሻൌ0 since we set the reference height of ݎ௬ሺݏൌ0ሻൌ0. Thus, the above formula simplifies to:

<!-- b000214 | prose | pages [8] -->
ܧ௄ሺݏ்ை்஺௅ሻൌ 1

<!-- b000215 | prose | pages [8] -->
ݒଶሺ0ሻെ݉݃ 2݉

<!-- b000216 | prose | pages [8] -->
௦೅ೀ೅ಲಽ

<!-- b000217 | prose | pages [8] -->
ሺݑሻܧ௄ሺݑሻ݀ݑ ߤݓെ2ߤනࣥ

<!-- b000218 | furniture | pages [8] -->


<!-- b000219 | prose | pages [8] -->
଴

<!-- b000220 | prose | pages [8] -->
Where ݓ is the width of the half pipe measured from one coping to the other.

<!-- b000221 | prose | pages [8] -->
ݒଶሺݏ்ை்஺௅ሻ, thus each of the terms in the above equation can be divided Recall that, ܧ௄ሺݏ்ை்஺௅ሻൌሺ1/2ሻ݉ by ሺ1/2ሻ݉ to yield the an equation for the square of the velocity with which the athlete exits the half-pipe, ሺݏሻ: ൌݒଶሺݏሻ, as:

<!-- b000222 | prose | pages [8] -->
ሺݏ்ை்஺௅ሻൌ߰

<!-- b000223 | prose | pages [8] -->
௦೅ೀ೅ಲಽ

<!-- b000224 | prose | pages [8] -->
ሺ0ሻെ2݃ߤݓെ2ߤනࣥ ሺݑሻ

<!-- b000225 | prose | pages [8] -->
ሺݑሻ݀ݑ      ሺכሻ

<!-- b000226 | prose | pages [8] -->
଴

<!-- b000227 | prose | pages [8] -->
This clearly shows that the exiting velocity is independent of mass. Throughout the models that soon follow, we therefore assume the (arbitrary) single unit mass, such that we can interchange the kinetic energy at the exit coping with the square of the exiting velocity (keeping in mind that they must be interchanged by a scaling factor of 2 to account for the fact that ܧ௄ሺݏሻ· 2 ൌሺ݉ ሺݏሻ. ൌ1ሻ·߰

<!-- b000228 | prose | pages [8] -->
We now comment on, and explain why there are two terms involved for the work done by friction (the two ߤݓ, represents the total horizontal component of friction terms involving the integral). The first term, resulting from the normal force when travelling along a path with constant slope (i.e. zero curvature). The ሺݑሻܧ௄ሺݑሻ݀ݑ represents the additional friction resulting from the component of second term involving 2 the normal force that produces centripetal acceleration. To illustrate, consider a half-pipe that is a simple horizontal straight line connecting both copings. In this case, the first term would make sense since we would lose energy to friction equal to 2݃ߤ across the entire line of length ݓ. Further, since a line has zero curvature,

<!-- b000229 | prose | pages [8] -->
ሺݑሻൌ0, ׊ 0 ൑ݑ൑ݏ்ை்஺௅, thus the second integral is zero. Therefore, our total work lost to friction is 2݃ߤݓ, as is intuitively required.

<!-- b000230 | prose | pages [8] -->
It is difficult to solve ሺכሻ analytically, however we can make the following observations:

<!-- b000231 | prose | pages [8] -->
1. A smaller coefficient of friction, ߤ, would mean that less work is lost to friction and thus ߰ሺݏ்ை்஺௅ሻ (and therefore vertical air) will be larger.

<!-- b000232 | furniture | pages [9] -->
Team # 11199

<!-- b000233 | furniture | pages [9] -->


<!-- b000234 | furniture | pages [9] -->


<!-- b000235 | furniture | pages [9] -->
9

<!-- b000236 | prose | pages [9] -->
2. A smaller total cross-section width from coping to coping, ݓ, results in less work lost to friction by the term 2݃ߤݓ, and thus greater ߰ሺݏ்ை்஺௅ሻ (and therefore vertical air). Having said that, one must also consider the second term involving work lost to friction. Since the integral term:

<!-- b000237 | prose | pages [9] -->
௦೅ೀ೅ಲಽ ሺݑሻ ሺݑሻ݀ݑ confounds two factors – curvature and arc length – our intuition alone 2ߤ׬ࣥ ଴ cannot answer the question of what the asymptotic properties of this term behave like. Since the snowboarder must enter and exit the course cross-section at copings that are nearly perpendicular to the horizon (by assumption 7), there must be some curvature in the half pipe to allow her to change vertical momentum into horizontal momentum, and back into vertical momentum in the opposite ሺݑሻ becomes infinitely large. Thus, if direction. However, for infinitely small curves, the curvature, the half-pipe were designed as a straight horizontal line with infinitely small curves at the end, we ௦೅ೀ೅ಲಽ ሺݑሻ ሺݑሻ݀ݑ), know that the total arc length, ݏ்ை்஺௅ is reduced (thus serving to reduce 2ߤ׬ࣥ ଴

<!-- b000238 | prose | pages [9] -->
௦೅ೀ೅ಲಽ ሺݑሻ, becomes large, (serving to increase 2ߤ׬ࣥ however curvature, ሺݑሻ ሺݑሻ݀ݑ). Thus, it is ଴ clearly difficult to understand how these confounding factors interact in this term using either intuition, or mathematics. For this reason, the following models – designed to incorporate friction – use modeling and simulation to discover which curves produce the optimal overall “exit” velocity, ݒሺݏ்ை்஺௅ሻ.

<!-- b000239 | prose | pages [9] -->
There are few curves in the Euclidean plane that: (i) satisfy all of our seven stated assumptions and constraints, and (ii) can be parameterized by arc length. The following three curves were of interest in our modeling: semicircles, cycloids, and “flat ovals” (horizontal lines with quarter circles attached at either end).

<!-- b000240 | heading | pages [9] -->
Vertical Air Model 2.1 – Semicircle (Friction Included)

<!-- b000241 | prose | pages [9] -->
One obvious sample curve to model is the semicircle, due to the simplicity of its parametric form. For such a shape, we defined the equation of the curve as: ݎԦሺ߶ሻൌሾݎെݎcosሺ߶ሻ, ݎsinሺ߶ሻሿ, ߶א ሾ0, ߨሿ, where ݎ is the radius of the semi-circle and ߶ is the angle transversed from the reference point.  We now re-parameterize ߶ with respect to arc length, ݏ, using the well-known relationship: ݏൌݎ߶. Since the semicircle has symmetric properties and a constant curvature, the expressions needed to describe equation ሺכሻ are simple:

<!-- b000242 | prose | pages [9] -->
ݎ௫ሺݏሻൌݎቀ1 െcos ቀݏ

<!-- b000243 | prose | pages [9] -->
ݎቁቁ;    ݎ௬ሺݏሻൌݎsin ቀݏ

<!-- b000244 | prose | pages [9] -->
ሺݏሻൌ൬1 ݎቁ;     ࣥ

<!-- b000245 | prose | pages [9] -->
ݎ൰;    ݏ்ை்஺௅ൌߨݎ;     ݓൌ2ݎ

<!-- b000246 | prose | pages [9] -->
It is interesting to note that the entire model of the circle can be determined uniquely by the its radius, ݎ.

<!-- b000247 | heading | pages [9] -->
Vertical Air Model 2.2 – Cycloid (Friction Included)

<!-- b000248 | prose | pages [9] -->
Another interesting curve to model is the cycloid, for reasons discussed in Model 1.2. Since it is the solution to both the brachistochrone and tautochrone problems under a frictionless assumption, it may hold special properties even when friction is non-zero. The standard parameterization of a cycloid is given by the following: ݎԦሺݐሻൌሾݎሺݐെsinሺ߶ሻሻ, ݎሺ1 െcosሺ߶ሻሻሿ, ߶א ሾ0,2ߨሿ. It is important to note that the curvature of a cycloid is infinite at ߶ൌ0, 2ߨ, thus in our model, we slightly truncated the parameterized curve to approximate the parametric equation over the interval ߶א ሺ0,2ߨሻ, the effect of which is slightly less-than- vertical angles at the copings. With some basic algebraic manipulation, we can derive the following functions parameterized by arc length, ݏ:

<!-- b000249 | prose | pages [9] -->
൰;    ݎ௬ሺݏሻൌቆݏെݏଶ

<!-- b000250 | prose | pages [9] -->
ݎ௫ሺݏሻൌݏଶ൬12ݎെݏ

<!-- b000251 | prose | pages [9] -->
8ݎቇ;     ࣥ

<!-- b000252 | prose | pages [9] -->
24ݎ

<!-- b000253 | prose | pages [9] -->
1 ሺݏሻൌ

<!-- b000254 | prose | pages [9] -->
√8ݎݏെݏଶ;    ݏ்ை்஺௅ൌ8ݎ;     ݓൌ2ߨݎ

<!-- b000255 | prose | pages [9] -->
Like the semicircle, the cycloid is also uniquely determined by the choice of the radius, radius, ݎ.

<!-- b000256 | furniture | pages [9] -->


<!-- b000257 | furniture | pages [10] -->
Team # 11199

<!-- b000258 | furniture | pages [10] -->


<!-- b000259 | furniture | pages [10] -->


<!-- b000260 | furniture | pages [10] -->
10

<!-- b000261 | heading | pages [10] -->
Vertical Air Model 2.3 – “Flat Oval” (Friction Included)

<!-- b000262 | prose | pages [10] -->
The third curve considered is a modification of the semicircle, whereby a horizontal line is used to connect two small quarter circles at either end in a manner such that the function is piecewise continuous (Figure 9). Although this shape lacks elegant properties, it allows us to investigate a much broader class of potential curves if we fix a cross-section width. This shape, unlike the others is not uniquely determined by one variable, but rather two variables (the radius of the quarter circle sections and the length of the horizontal line connecting them).

<!-- b000263 | prose | pages [10] -->
r

<!-- b000264 | prose | pages [10] -->
w

<!-- b000265 | prose | pages [10] -->
b b

<!-- b000266 | furniture | pages [10] -->


<!-- b000267 | caption | pages [10] -->
Figure 9: Illustrative “Flat Oval” Shape

<!-- b000268 | prose | pages [10] -->
ሺݑሻ݀ݑ needed for equation ሺכሻ are merely piecewise functions that are similar to The functions ݎ௫ሺݏሻ and ሺݑሻ݀ݑൌ0 for all values of 0 ൑ݑ൑ݏ்ை்஺௅ such that the those of the semi-circle (Model 2.1). Note that end-point given by ݑ runs along horizontal base, since a line has zero curvature.  The arc length and ൅ߨݎ, and ݓൌܾ horizontal distance are given by: ݏ்ை்஺௅ൌܾ ൅2ݎ, respectively, where ݎ is the radius of ൒0 is the length of the connecting line. the two quarter circles, and

<!-- b000269 | heading | pages [10] -->
II.3 Results & Comparison of Models Including Friction (Models 2.1 – 2.3)

<!-- b000270 | prose | pages [10] -->
The above models are very flexible, thus allowing us to test the relationships of many variables. First, we fix the total width of the course from coping to coping for each of the models to be the same. To model a realistic course, we fix a course width, ݓൌ18.0 ݉ , since this was the width of the most recent Vancouver 2010 Olympic half-pipe course. Once the width is fixed, we can plot the speed as a function of the arc length travelled for these three different non-zero friction models. We also look at two versions of Model 2.3; one ൌ15 and another with with a length of the line, ൌ5. Empirical studies have shown that the coefficient of friction acting on a snowboarder from the snow and the air, ߤ, ranges between 0.01 and 0.15,  with an average of 0.05.xv Thus, for these simulations, we assume a coefficient of friction, ߤൌ0.05 as well as an (arbitrary) initial “entry speed” into the half-pipe of ݒሺ0ሻൌ20 ݉ /ݏ. The plots of speed as a function of arc length travelled for these four sample curves are then given by Figure 10.

<!-- b000271 | furniture | pages [11] -->
Team # 11199

<!-- b000272 | furniture | pages [11] -->


<!-- b000273 | furniture | pages [11] -->


<!-- b000274 | furniture | pages [11] -->
11

<!-- b000275 | furniture | pages [11] -->


<!-- b000276 | caption | pages [11] -->
Figure 10: Speed vs. Arc Length Travelled on Four Sample Curves (Fixed Width & “Entry Speed”)

<!-- b000277 | prose | pages [11] -->
We can summarize the variables of interest that are plotted above by the following chart, which outlines the final speed upon exiting the other side of the half-pipe as well as the total arc length travelled (Figure 11).

<!-- b000278 | heading | pages [11] -->
Model

<!-- b000279 | prose | pages [11] -->
Curve Shape 2.1 Circle 2.2 Cycloid ൌ15) 2.3 Flat Oval ( ൌ5) 2.3 Short Oval (

<!-- b000280 | furniture | pages [11] -->


<!-- b000281 | prose | pages [11] -->
Exit Speed (m/s) Arc Length (m) 15.7 28.3 14.0 22.9 16.5 19.7 16.0 25.4

<!-- b000282 | caption | pages [11] -->
Figure 11: Resultant Sample Curve Statistics for Four Sample Curves (Fixed Width & “Entry Speed”)

<!-- b000283 | prose | pages [11] -->
From the above results, it seems that Models 2.1 and 2.3 (the “circular family of curves”) demonstrate the property that shorter arc lengths are associated with higher exit speeds. To test this hypothesis, we run the simulation again, however this time we fix the total arc length, ݏ்ை்஺௅ൌ28.274 ݉ , which is the arc length associated with a semi-circle of radius 18.0 m. Now we repeat the plots as above with these new constraints (Figure 12).

<!-- b000284 | furniture | pages [12] -->
Team # 11199

<!-- b000285 | furniture | pages [12] -->


<!-- b000286 | furniture | pages [12] -->


<!-- b000287 | furniture | pages [12] -->
12

<!-- b000288 | furniture | pages [12] -->


<!-- b000289 | caption | pages [12] -->
Figure 12: Speed vs. Arc Length Travelled on Four Sample Curves (Fixed Arc Length & “Entry Speed”)

<!-- b000290 | prose | pages [12] -->
We can find the final speed upon exiting the other side of the half-pipe from our model, as well as the width from coping to coping resulting from fixing the total arc length (Figure 13).

<!-- b000291 | heading | pages [12] -->
Model

<!-- b000292 | prose | pages [12] -->
Curve Shape 2.1 Circle 2.2 Cycloid ൌ15) 2.3 Flat Oval ( ൌ5) 2.3 Short Oval (

<!-- b000293 | furniture | pages [12] -->


<!-- b000294 | prose | pages [12] -->
Exit Speed (m/s) Course Width (m) 15.7 18.00 12.6 22.21 16.1 23.45 15.8 19.82

<!-- b000295 | caption | pages [12] -->
Figure 13: Resultant Sample Curve Statistics for Four Sample Curves (Fixed Arc Length & “Entry Speed”)

<!-- b000296 | prose | pages [12] -->
We notice from these results that the exit speeds still seem to differ among the “circular family of curves.” Now, we can analyze how the four different sample curves, generated by our three non-zero friction models, behave as the total width of the curve varies (Figure 14).

<!-- b000297 | furniture | pages [13] -->
Team # 11199

<!-- b000298 | furniture | pages [13] -->


<!-- b000299 | furniture | pages [13] -->


<!-- b000300 | furniture | pages [13] -->
13

<!-- b000301 | furniture | pages [13] -->


<!-- b000302 | caption | pages [13] -->
Figure 14: Speed vs. Width of 200 Sample Curves (Fixed “Entry Speed”)

<!-- b000303 | prose | pages [13] -->
ൌ15), blue dots represent short “flat oval” In the above plot, green dots represent long “flat oval” curves ( ൌ5), black dots represent semicircle curves, dots represent cycloid curves. We see that the optimal curves ( cross-section shape of the four sample curves is the “long flat oval.” We can make the following observations from these above results:

<!-- b000304 | prose | pages [13] -->
1. The black dots for the semi-circle curve (Model 2.1) can be thought of the limiting case of the “flat ՜ 0. One conclusion then is that that assuming a fixed curve oval” (Model 2.3) in the limit as ൐0 (as the semi-circle curve represents width, Model 2.3 outperforms Model 2.1 for all values of ൌ0). the lower bound of exit speed for the flat oval when

<!-- b000305 | furniture | pages [13] -->


<!-- b000306 | prose | pages [13] -->
2. Further, we notice that the cycloid (Model 2.2) is clearly less efficient at reducing the amount of energy lost to friction relative to the other sample curves. The most likely reason for this is the fact that the curvature of the cycloid approaches infinity as the snowboarder approaches either coping, as discussed for Model 2.2. For reasons explained later under “Considerations & Limitations of Models,” extremely high curvature is unpractical for the snowboarder, and thus the cycloid is henceforth discarded from our list of candidates for the “best” curve to maximize vertical air.

<!-- b000307 | furniture | pages [13] -->


<!-- b000308 | prose | pages [13] -->
3. It is also important to note that in running these simulations, we assumed the snowboarder progresses along the curve at a step size of 0.01 m. We see clearly that there is some error due to the disretization of these continuous curves, since the above dots – representing different observations for a fixed width – ‘bump around’ a curve of best fit. This error however is minimal, and the results were similar when an even smaller step size was used. For this reason, we feel confident about drawing conclusions about the plotted realizations in Figure 14.

<!-- b000309 | prose | pages [13] -->
To explore whether ovals with a larger horizontal base component (length ܾ) are always better than those with smaller base components, we can fix the width of the half pipe at ݓൌ18.0 ݉ and simulate the kinetic

<!-- b000310 | furniture | pages [14] -->
Team # 11199

<!-- b000311 | furniture | pages [14] -->


<!-- b000312 | furniture | pages [14] -->
14

<!-- b000313 | prose | pages [14] -->
energy achieved upon exiting the course at the exit coping for varying values of ܾ (as a percentage of total width, ݓ) (Figure 15).

<!-- b000314 | furniture | pages [14] -->


<!-- b000315 | caption | pages [14] -->
Figure 15: Kinetic Energy upon Exiting Cross-Section of Long Oval Shape (Model 2.3) vs. (ܾ/ݓ)

<!-- b000316 | prose | pages [14] -->
It is clear from the above graph that the longer the length of the connecting horizontal line, ܾ, (and consequently the larger the curvature at the end quarter circles), for a fixed total width, ݓ, the more efficient the curve is at reducing work lost to friction. If we re-plot the data with respect to total arc length, ݏ்ை்஺௅, we get the following Figure 16:

<!-- b000317 | furniture | pages [14] -->


<!-- b000318 | caption | pages [14] -->
Figure 16: Kinetic Energy upon Exiting Course Cross-Section of Long Oval Shape (Model 2.3) vs. ݏ்ை்஺௅

<!-- b000319 | furniture | pages [15] -->
Team # 11199

<!-- b000320 | furniture | pages [15] -->


<!-- b000321 | furniture | pages [15] -->


<!-- b000322 | furniture | pages [15] -->
15

<!-- b000323 | prose | pages [15] -->
Thus, we are finally ready to draw some conclusions about the asymptotic properties of the term:

<!-- b000324 | prose | pages [15] -->
௦೅ೀ೅ಲಽ ሺݑሻ݀ݑ (as well as the relative roles that curvature, ሺݑሻ 2ߤ׬ࣥ ଴ in determining how large the term is) in the equation:

<!-- b000325 | prose | pages [15] -->
ሺݑሻ, and total arc length, ݏ்ை்஺௅ play

<!-- b000326 | prose | pages [15] -->
௦೅ೀ೅ಲಽ

<!-- b000327 | prose | pages [15] -->
ሺ0ሻെ2݃ߤݓെ2ߤනࣥ ሺݏ்ை்஺௅ሻൌ߰ ሺݑሻ

<!-- b000328 | prose | pages [15] -->
ሺݑሻ݀ݑ      ሺכሻ

<!-- b000329 | prose | pages [15] -->
଴

<!-- b000330 | prose | pages [15] -->
By setting the width of the half pipe to be the same for all curves, we see from the last simulation that it is more desirable to have very high curvature over a very short portion of the curve, rather than low curvature spread out over longer portions of the curve. In other words, our goal for designing the optimal half-pipe for maximal vertical air should to design a course with small portions of the curve with high curvature and larger portions with zero curvature. Essentially, the “best” curve would therefore be a straight line from coping to coping with infinitesimal quarter circles at either end.

<!-- b000331 | heading | pages [15] -->
II.4 Considerations & Limitations of Models Including Friction (Models 2.1 – 2.3)

<!-- b000332 | prose | pages [15] -->
Air Resistance

<!-- b000333 | prose | pages [15] -->
Air resistance, or “drag” through a fluid, is a very complex quantity that depends on numerous variables, including but not limited to: density, temperature, speed, shape of the snowboarder, and the air’s viscosity. Most models for drag are extremely complex and unreliable. However, there are two simplified models of air resistance. The “quadratic model” assumes drag force is proportional to the speed squared, and is reserved for objects moving at very high speeds through the fluid. The “linear” or “Stokes’ model” is more appropriate for slower objects and assumes drag is proportional to speed. Our model of frictional force already contains a quadratic term with respect to the speed, since we embed the coefficient of friction related to air in our assumed ߤൌ0.05. Thus our model of such air resistance is reasonable if using the quadratic model. The following graph shows what the effects on the exiting kinetic energy are by simply increasing the coefficient of friction, assuming a constant width of ݓൌ18.0 ݉ considered (Figure 17).

<!-- b000334 | prose | pages [15] -->
for all four sample curves previously

<!-- b000335 | furniture | pages [15] -->


<!-- b000336 | caption | pages [15] -->
Figure 17: Kinetic Energy upon Exiting Course Cross-Section of all Four Sample Curves vs. ߤ (Fixed ݓ)

<!-- b000337 | furniture | pages [16] -->
Team # 11199

<!-- b000338 | furniture | pages [16] -->


<!-- b000339 | furniture | pages [16] -->
16

<!-- b000340 | prose | pages [16] -->
ൌ15), the blue line As throughout the prior sections in the report, the green line is for the long “flat oval” ( ൌ5), the black line is for the semi-circle, and the red line is for the cycloid. As is for the short “flat oval” ( desired, the above graph shows that the “optimal” half-pipe shape for maximizing vertical air does not change as the coefficient of friction changes. Clearly, the closer the curve is to a horizontal line with infinitesimal quarter circles at the end, the better the vertical air one will achieve, regardless of the coefficient of friction.

<!-- b000341 | prose | pages [16] -->
Our model could be extended even further to include a drag term corresponding to a linear and a quadratic form of drag (and not proportional to surface friction as assumed in our model). However, without careful experimentation and measurements, and a detailed understanding of fluid mechanics, it is impossible to say whether a linear, quadratic or even a more complex model is needed.

<!-- b000342 | prose | pages [16] -->
In summary, although air resistance is not modeled ‘perfectly’ in this report, our approximation by assuming it is proportional to the friction force is a reasonable one for this ‘broad-scale’ study.

<!-- b000343 | heading | pages [16] -->
Less Conventional Friction Models

<!-- b000344 | prose | pages [16] -->
Our model assumes that friction between the snowboard and the snow follows the Coulomb model. Many reference resources measure the quality of snowboards by their coefficient of friction, which helps support our belief that this is an appropriate model of friction. New materials or snowboard designs could conceivably follow non-linear friction models. Our model can easily be adapted to different friction models, by collecting data on the frictional force as a function of the speed of the snowboard.

<!-- b000345 | prose | pages [16] -->
Movement down the Slope

<!-- b000346 | prose | pages [16] -->
Our simplified model does not account for the snowboarder travelling down a sloped hill (i.e. we focus on the cross-section of the curve, as if assuming a 0° slope). However, such a simplification does not result in a loss of generality. Let us assume a third dimension, z, perpendicular to x and y with the convention that z is positive in the direction towards the bottom of the hill (along the given slope). If the speed of the snowboarder in the direction of z is small relative to their speed in the x-y plane, then the frictional force in that direction will in turn be a small percentage of the total friction. While the snowboarder would also lose work due to friction as she moves down the hill in the z direction, she also continues to exhaust more and more potential energy with each jump. If she uses the same amount of potential energy resulting from movement in the z-direction, then we can approximately assume that this entire additional component of potential energy is converted into work. Thus, our model becomes a reasonable approximation for any slope of the hill.

<!-- b000347 | prose | pages [16] -->
Imperfect Surfaces

<!-- b000348 | prose | pages [16] -->
The trajectory of the snowboarder in our model is perfectly smooth. However, real-life half pipes will be subjected to wearing out, scratches, and other imperfections. The Coulomb model of friction is still very accurate, if the imperfections are much smaller than the area of the contact surface (i.e. bottom of the snowboard). Extensions to the model where the coefficient of friction is allowed to vary stochastically could be an interesting area of further research, to simulate random imperfections.

<!-- b000349 | prose | pages [16] -->
Angle of Cross-Section “Vertical” < 90°

<!-- b000350 | prose | pages [16] -->
The standard angle of the “vertical” on half pipes is 83° to allow for a technique known as “pumping” by the snowboarder.xvi The actual launch angle of the snowboarder in our model is much closer to 90° to maximize to ensure that 100% of total air achieved is in the vertical direction (thus maximizing vertical air). However, snowboards are flexible, and the movement of snowboarders upon exiting the half-pipe at the coping is imperfect. Thus, small deviations from the optimal 90° launch angle should be accounted for to accommodate “pumping” in the model. If the actual launch angle is off the desired 90° mark by ߶, then the new maximum vertical air (height) is given by the following:

<!-- b000351 | furniture | pages [17] -->
Team # 11199

<!-- b000352 | prose | pages [17] -->
maxሺݒ݁ݎݐ݈݅ܿܽ ܽ݅ ݎ;  90° ݈ܽ

<!-- b000353 | prose | pages [17] -->
maxሺݒ݁ݎݐ݈݅ܿܽ ܽ݅ ݎ;  90° േ߶ ݈ܽ ݑ݄݊ܿ

<!-- b000354 | furniture | pages [17] -->


<!-- b000355 | furniture | pages [17] -->


<!-- b000356 | furniture | pages [17] -->
17

<!-- b000357 | prose | pages [17] -->
ൌݒଶ ሻؔ݀ ݑ݄݊ܿ ݈ܽ݊݃݁

<!-- b000358 | prose | pages [17] -->
2݃

<!-- b000359 | prose | pages [17] -->
ሺ1 െcosሺ߶ሻሻଶݒଶ

<!-- b000360 | prose | pages [17] -->
ሻؔ݀ ௔ௗ௝ൌ ݈ܽ݊݃݁ ݈ܽ݊݃݁

<!-- b000361 | furniture | pages [17] -->


<!-- b000362 | prose | pages [17] -->
2

<!-- b000363 | prose | pages [17] -->
Even for deviations of up to: ߶ൌ20°, the difference in these maximum vertical heights achieved is less than 0.3%. Therefore, this limitation of our model turns out to be negligible.

<!-- b000364 | heading | pages [17] -->
III. Maximizing Rotation (Twist) – Design and Implementation of Models

<!-- b000365 | prose | pages [17] -->
According to the principle of conservation of angular momentum, “when the net external torque acting on a system is zero, the total angular momentum of the system is constant (conserved).”xvii Since the snowboarder cannot spin her body by either internal or external forces once she is in the air, she must already have an initial angular momentum prior to exiting the course at the coping. That is to say, any rotation in the air is entirely determined by the rotation initiated by the athlete while still in contact with the surface of the half- pipe.

<!-- b000366 | prose | pages [17] -->
For now, we also assume that the shape of the half-pipe is static and there are no “man-made” external forces (for example, from moving parts) acting to rotate the athlete while in contact with the surface. Thus all angular momentum must be entirely produced by the athlete herself, suggesting that total rotation (or “twist”) depends on her overall skill-level.

<!-- b000367 | prose | pages [17] -->
For simplicity and generality, assume that all athletes have the same skill-level and ability to maximize rotation. Then clearly, the only other factor determining the degree of total rotation is the amount of time over which the snowboarder can remain airborne. Intuitively, the longer the snowboarder can stay in the air, the more she will rotate overall since angular velocity is maintained throughout the entire jump. We can ൌܶ /ݐ, where therefore model the total number of rotations an athlete can perform per jump by:

<!-- b000368 | furniture | pages [17] -->


<!-- b000369 | prose | pages [17] -->
represents the total amount of time the snowboarder can remain airborne, and ݐ represents the amount of time needed to complete one rotation. Thus, since we are assuming each athlete can maximize rotation such that ݐ is constant, in order to maximize ܴ, we must maximize ܶ.

<!-- b000370 | prose | pages [17] -->
Naturally, the slope of the hill would help to produce additional total air time since ܶ would contain both lengthwise and vertical air-time components. Thus, the “best” course would have a 90° incline (i.e. vertical) since the athlete could rotate in free-fall for the entirety of the course length. However, this is unrealistic, and thus we clarify the objective at hand as follows: assuming a given course slope, how can one maximize the rotation resulting only from vertical air (i.e. assuming a flat cross-section of the course)?

<!-- b000371 | heading | pages [17] -->
Rotational Model 1 – (No Pumping)

<!-- b000372 | prose | pages [17] -->
If we assume that athletes do not “pump” (and thus horizontal air time is zero), then by ignoring air-time related to the course's slope, the remaining air-time is entirely due to vertical air. For simplicity, assume that ௩௘௥௧ൌ݀ െ݀ air resistance is negligible. The equation for the amount of vertical displacement, ଴, at any ௩௘௥௧ൌݒ଴ݐെሺ1/2ሻ݃ݐଶ, where ݒ଴ is the initial point in time of the jump, ݐ, must be given by equation: speed of the snowboarder when she leaves the half-pipe and ݃ is the acceleration due to gravity. Since ݃ is known, and we take ݒ଴ as fixed, the total vertical air is entirely a deterministic function of time in the air.

<!-- b000373 | prose | pages [17] -->
Since we are assuming no friction, by law of conservation of energy, the velocity of the snowboarder upon re- entering (or 'falling back into') the half-pipe should be equal in magnitude and opposite in direction to the ൌെݒ଴ and the equation for acceleration becomes: speed when exiting the half-pipe. Thus ݒ

<!-- b000374 | furniture | pages [18] -->
Team # 11199

<!-- b000375 | furniture | pages [18] -->


<!-- b000376 | furniture | pages [18] -->


<!-- b000377 | furniture | pages [18] -->
18

<!-- b000378 | prose | pages [18] -->
ൌሺെݒ଴ሻെሺݒ଴ሻܶ

<!-- b000379 | prose | pages [18] -->
ൌݒ்െሺݒ଴ሻܶ െ݃

<!-- b000380 | prose | pages [18] -->
ൌെ2ݒ଴ܶ

<!-- b000381 | prose | pages [18] -->
ൌ2ݒ଴/݃. Given this, we can update our equation for the number of total rotations an Thus, we get that athlete can perform in one jump to get:

<!-- b000382 | prose | pages [18] -->
ൌܶݐൌ2ݒ଴

<!-- b000383 | prose | pages [18] -->
ݐ

<!-- b000384 | prose | pages [18] -->
Thus, we see that the total number of rotations that the athlete can perform in the air is entirely a function of the speed at which the individual exits the half-pipe at the coping, ݒ଴, and ݐ. Essentially then, the objective of maximizing rotations due merely to vertical air (and lengthwise air resulting from the slope of the hill) is logically equivalent to maximizing the total vertical air, which was addressed earlier.

<!-- b000385 | heading | pages [18] -->
Rotational Model 2 – (Pumping)

<!-- b000386 | prose | pages [18] -->
In reality, snowboarders use a technique known as “pumping” to push off at the copings, which ultimately provides greater rotation. This technique also provides the athlete with a horizontal component of speed, thus moving her towards the center of the half-pipe in mid-air. As such, the athlete's trajectory now creates a projectile motion that is no longer strictly vertical (as was the case in Rotational Model 1). Since the shape of the half-pipe is curved, this means that the athlete will land farther into the course's “transition” section rather than back on the “vertical.” In such a case, it is no surprise that total air time is increased since the athlete now has 'farther to fall' until she regains contact with the snow surface. With increased total air time, ܶ, we /ݐ, the total number of rotations (twists) one can perform must also ൌܶ know that by our equation: increase (since ݐ is fixed).

<!-- b000387 | prose | pages [18] -->
Indeed, in practice this technique does allow snowboarders to perform larger rotations (more challenging aerial acrobatics), thus resulting in a higher score. If we compare landings of the final jump for two top performing snowboarders in the most recent Vancouver 2010 Winter Olympic Games, we see empirically that this theoretical posit is in fact true (Figure 18).

<!-- b000388 | prose | pages [18] -->
Iouri Podladtchikov Athlete Name

<!-- b000389 | prose | pages [18] -->
Picture of

<!-- b000390 | prose | pages [18] -->
Landing “Touch- Down” Region

<!-- b000391 | prose | pages [18] -->
of Final Jump

<!-- b000392 | prose | pages [18] -->
Country of Switzerland Representation

<!-- b000393 | prose | pages [18] -->
Shaun White

<!-- b000394 | prose | pages [18] -->
U.S.A.

<!-- b000395 | prose | pages [18] -->
“Double McTwist 1260°” (a forward-flipping

<!-- b000396 | prose | pages [18] -->
“Rodeo Flip 540°” (a backward-flipping front-side

<!-- b000397 | prose | pages [18] -->
Trick Performed

<!-- b000398 | prose | pages [18] -->
spin performed with a 540° rotation)

<!-- b000399 | prose | pages [18] -->
Overall Score 42.4 / 50.0 Overall Final

<!-- b000400 | prose | pages [18] -->
Fourth

<!-- b000401 | prose | pages [18] -->
Olympic Standings

<!-- b000402 | furniture | pages [18] -->


<!-- b000403 | prose | pages [18] -->
backside spin with a mute grab that performed

<!-- b000404 | prose | pages [18] -->
with a 1260° rotation) 48.4 / 50.0

<!-- b000405 | prose | pages [18] -->
First (Gold Medalist)

<!-- b000406 | caption | pages [18] -->
Figure 18: Illustrative Empirical Evidence that Landing Further Inside Half-Pipe Allows for more Rotation

<!-- b000407 | prose | pages [18] -->
(and thus a Higher Score/Performance Ranking), Vancouver 2010 Winter Olympic Games

<!-- b000408 | furniture | pages [19] -->
Team # 11199

<!-- b000409 | furniture | pages [19] -->


<!-- b000410 | furniture | pages [19] -->
19

<!-- b000411 | prose | pages [19] -->
It is therefore clear that in order to design a course that maximizes the amount of rotation (or twist) that an athlete can perform, one must design a very “deep” course with inner walls that are rather steep. In other words, the walls (“vertical” component) of such a course must be very high. Building a course in this way allows for maximal total air-time, and thus maximal rotation. However, we note here that there are obviously limitations (many of which are mentioned in the analysis of maximal vertical air models) with how high the course is and how steep the walls are. These limitations include: the snowboard’s inability to flex around a nearly instantaneous change from momentum in the horizontal to the vertical direction, the riders inability to withstand the resulting g-forces, and the reduction in exiting velocity (and thus total air time and total rotation) resulting from greater overall friction when the walls are very high.

<!-- b000412 | heading | pages [19] -->
IV. Conclusion

<!-- b000413 | prose | pages [19] -->
Immediately evident is the inherent trade-off of designing an ultimate course that maximizes both (i) vertical air, and (ii) total rotation (or twist). The prior requires a course with minimal height and width so as to reduce total energy lost to friction. The latter requires a course with significant height and width to achieve additional total air time via pumping. It is no wonder then that, the likely answer to the question: “What half-pipe shape would maximize performance, including vertical air and twist?” is: “It depends on what performance variable you place more emphasis on.” As such, this suggests that there is no ‘perfect’ course design, and thus a course’s shape allows for a level of uniqueness by placing greater emphasis on different performance variables. Ultimately, new course shapes allow for riders to attempt new daring moves, thus adding excitement to the sport for both the rider and the observer.

<!-- b000414 | furniture | pages [19] -->


<!-- b000415 | furniture | pages [19] -->


<!-- b000416 | furniture | pages [20] -->
Team # 11199

<!-- b000417 | furniture | pages [20] -->


<!-- b000418 | furniture | pages [20] -->
20

<!-- b000419 | heading | pages [20] -->
References

<!-- b000420 | references | pages [20] -->
Amateur Athletic Foundation of Los Angeles. "The Fire Within: Salt Lake 2002 Olympic Winter Games."

<!-- b000421 | references | pages [20] -->
2004.

<!-- b000422 | references | pages [20] -->
Cypress Mountain. 2010 Olympic Venue Stats and Info Sheet. 2011.

<!-- b000423 | references | pages [20] -->
<http://cypressmountain.com/system/files/2010%20Venue%20Stats%20Information.pdf>.

<!-- b000424 | references | pages [20] -->
Half-pipe. wikipedia. 13 2 2011 <http://en.wikipedia.org/wiki/Half-pipe>.

<!-- b000425 | references | pages [20] -->
Harding, J.W., J.W. Small and D.A. James. Feature Extraction of Performance Variables in Elite Half-Pipe

<!-- b000426 | references | pages [20] -->
Snowboarding Using Body Mounted Inertial Sensors. Ed. Dan V.Nicolau, et al. 6799 vols. SPIE, 2007.

<!-- b000427 | references | pages [20] -->
International Olympic Committee. "Final Report: XX Olympic Winter Games." 2007.

<!-- b000428 | references | pages [20] -->
—. Olympic Programme Commission Report, 119th IOC Session. 2007.

<!-- b000429 | references | pages [20] -->
MacCluer, Charles R. Calculus of Variations Mechanics, Control, and Other Applications. Pearson Education,

<!-- b000430 | references | pages [20] -->
Inc, 2005.

<!-- b000431 | references | pages [20] -->
PBL Enterprises. Zaugg AG Eggwil. 12 2 2011

<!-- b000432 | references | pages [20] -->
<http://www.zauggamerica.com/resort/pipegroomers/pipemonster/stats.shtml>.

<!-- b000433 | references | pages [20] -->
—. Zaugg AG Eggwil. 12 2 2011

<!-- b000434 | references | pages [20] -->
<http://www.zauggamerica.com/resort/pipegroomers/pipemonster/stats.shtml>.

<!-- b000435 | references | pages [20] -->
Rousseau, C. and Y. Saint-Aubin. "Calculus of Variations with Applications." Mathematics and Technology.

<!-- b000436 | references | pages [20] -->
Springer Science+Business Media, 2008. 4.

<!-- b000437 | references | pages [20] -->
The Organizing Committee for the XVIII Olympic Winter Games. "The XVIII Olympic Winter Games

<!-- b000438 | references | pages [20] -->
Official Report II." 1999.

<!-- b000439 | references | pages [20] -->
Yen, Christopher. Snowboard Acceleration. 10 4 2003. The University of Northern Carolina at Chapel Hill.

<!-- b000440 | references | pages [20] -->
13 2 2011 <http://www.unc.edu/~cyen/WebSiteAcceleration.html>.

<!-- b000441 | references | pages [20] -->
Young, Hugh D. and Roger A. Freedman. Sears and Zemansky’s university physics: with modern physics.

<!-- b000442 | references | pages [20] -->
Pearson Education, Inc., 2004.

<!-- b000443 | furniture | pages [20] -->


<!-- b000444 | furniture | pages [20] -->


<!-- b000445 | furniture | pages [20] -->


<!-- b000446 | furniture | pages [20] -->


<!-- b000447 | furniture | pages [20] -->


<!-- b000448 | furniture | pages [20] -->


<!-- b000449 | furniture | pages [20] -->


<!-- b000450 | furniture | pages [20] -->


<!-- b000451 | furniture | pages [20] -->


<!-- b000452 | furniture | pages [20] -->


<!-- b000453 | furniture | pages [20] -->


<!-- b000454 | furniture | pages [20] -->


<!-- b000455 | furniture | pages [20] -->


<!-- b000456 | furniture | pages [20] -->


<!-- b000457 | furniture | pages [21] -->
Team # 11199

<!-- b000458 | furniture | pages [21] -->


<!-- b000459 | furniture | pages [21] -->
21

<!-- b000460 | furniture | pages [21] -->


<!-- b000461 | references | pages [21] -->
End Notes

<!-- b000462 | furniture | pages [21] -->


<!-- b000463 | references | pages [21] -->
i (International Olympic Committee 94)

<!-- b000464 | references | pages [21] -->
ii (Harding, Small and James 1)

<!-- b000465 | references | pages [21] -->
iii Libd. Page 1

<!-- b000466 | references | pages [21] -->
iv (International Olympic Committee 127)

<!-- b000467 | references | pages [21] -->
v (Half‐pipe)

<!-- b000468 | references | pages [21] -->
vi (The Organizing Committee for the XVIII Olympic Winter Games 176)

<!-- b000469 | references | pages [21] -->
vii (Amateur Athletic Foundation of Los Angeles 101)

<!-- b000470 | references | pages [21] -->
viii (International Olympic Committee 200)

<!-- b000471 | references | pages [21] -->
ix (Cypress Mountain 2)

<!-- b000472 | references | pages [21] -->
x (PBL Enterprises)

<!-- b000473 | references | pages [21] -->
xi libd

<!-- b000474 | references | pages [21] -->
xii libd

<!-- b000475 | references | pages [21] -->
xiii (Rousseau and Saint‐Aubin, Calculus of Variations with Applications 4)

<!-- b000476 | references | pages [21] -->
xiv Libd. Page 13

<!-- b000477 | references | pages [21] -->
xv (Yen)

<!-- b000478 | references | pages [21] -->
xvi (PBL Enterprises)

<!-- b000479 | references | pages [21] -->
xvii (Young and Freedman 382‐383)
