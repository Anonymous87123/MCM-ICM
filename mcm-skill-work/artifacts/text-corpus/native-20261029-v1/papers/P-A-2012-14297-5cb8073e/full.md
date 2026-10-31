# P-A-2012-14297-5cb8073e

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team # 14297

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
Page 1 of 45

<!-- b000004 | heading | pages [1] -->
Summary

<!-- b000005 | prose | pages [1] -->
Leaf shape plasticity has long been a heated topic in the field of morphology and

<!-- b000006 | prose | pages [1] -->
taxonomy. Although numerous researchers have been involved in the study of how the

<!-- b000007 | prose | pages [1] -->
shape formation is controlled by genes and environmental stress, little has been done

<!-- b000008 | prose | pages [1] -->
to address the interactions between different plant organs. In this paper, we approach

<!-- b000009 | prose | pages [1] -->
this issue in a creative way: starting from isolated parts (leaves), building connections

<!-- b000010 | prose | pages [1] -->
(leaf-leaf, leaf-branch) and drawing the big picture of the entire system (tree).

<!-- b000011 | prose | pages [1] -->
The mathematical model introduced in this paper describes morphological,

<!-- b000012 | prose | pages [1] -->
physiological and partially ecological properties of the vegetations. First and foremost,

<!-- b000013 | prose | pages [1] -->
relative errors of the numerical outputs are limited within 7.5% and all the values

<!-- b000014 | prose | pages [1] -->
predicted are within the right order of magnitude. Moreover, biological intuition is

<!-- b000015 | prose | pages [1] -->
presented in the consistent manner. For instance, the dynamic positive feedback is

<!-- b000016 | prose | pages [1] -->
applied to describe leaf growth pattern and transportation process. It is also worth

<!-- b000017 | prose | pages [1] -->
noticing that a much simple and flexible algorithm is achieved by executing ingenious

<!-- b000018 | prose | pages [1] -->
geometric strategy.

<!-- b000019 | prose | pages [1] -->
Interestingly findings were generated in the procedures of solving the problems.

<!-- b000020 | prose | pages [1] -->
The seemly unrelated bio-phenomena could be explained when morphological,

<!-- b000021 | prose | pages [1] -->
physiological and partially ecological interactions were taken into account. To

<!-- b000022 | prose | pages [1] -->
illustrate, as we conducted the leaf mass estimation, it could give us a rough picture of

<!-- b000023 | prose | pages [1] -->
leaf-leaf, leaf-branch, and leaf-tree relations.

<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | furniture | pages [1] -->


<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | furniture | pages [2] -->
Team # 14297

<!-- b000028 | furniture | pages [2] -->


<!-- b000029 | furniture | pages [2] -->
Page 2 of 45

<!-- b000030 | prose | pages [2] -->
Dear editor,

<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | prose | pages [2] -->
The topic of this paper is about mathematical modeling of tree leaves as well as how

<!-- b000033 | prose | pages [2] -->
leaf traits impose influence on the tree system.

<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | prose | pages [2] -->
In this paper, we addressed the morphological, physiological and partially ecological

<!-- b000036 | prose | pages [2] -->
properties of the vegetations by applying a series of modeling process to related issues.

<!-- b000037 | prose | pages [2] -->
The performance of our model in the sensitivity test satisfied our expectation.

<!-- b000038 | prose | pages [2] -->
Different from the previous research, we approached this issue in a creative way:

<!-- b000039 | prose | pages [2] -->
starting from isolated parts (leaves), building connections (leaf-leaf, leaf-branch) and

<!-- b000040 | prose | pages [2] -->
drawing the big picture of the entire system (tree).

<!-- b000041 | furniture | pages [2] -->


<!-- b000042 | prose | pages [2] -->
Interestingly, the seemly unrelated bio-phenomena could be explained when

<!-- b000043 | prose | pages [2] -->
morphological, physiological and partially ecological interactions were taken into

<!-- b000044 | prose | pages [2] -->
account. Properties of the individual leaves are closely related to the characteristics of

<!-- b000045 | prose | pages [2] -->
the entire tree system.

<!-- b000046 | furniture | pages [2] -->


<!-- b000047 | prose | pages [2] -->
We are looking forward to your comments and revision. Hopefully, our paper could be

<!-- b000048 | prose | pages [2] -->
published in this Journal.

<!-- b000049 | furniture | pages [2] -->


<!-- b000050 | prose | pages [2] -->
Your sincerely

<!-- b000051 | furniture | pages [2] -->


<!-- b000052 | furniture | pages [2] -->


<!-- b000053 | furniture | pages [2] -->


<!-- b000054 | furniture | pages [3] -->
Team # 14297

<!-- b000055 | furniture | pages [3] -->


<!-- b000056 | furniture | pages [3] -->
Page 3 of 45

<!-- b000057 | heading | pages [3] -->
Introduction

<!-- b000058 | prose | pages [3] -->
The mechanism of plant shape plasticity has long been a topic of numerous

<!-- b000059 | prose | pages [3] -->
researches in the field of morphometrics. And leaves have been always favored as the

<!-- b000060 | prose | pages [3] -->
subject because of its two-dimensionality and relative simplicity. The change of leaf

<!-- b000061 | prose | pages [3] -->
shapes are generally regarded as both a genetically determination (Howell, 1998) and

<!-- b000062 | prose | pages [3] -->
results of structural optimization to environmental stress (Hemsley and Poole, 2004).

<!-- b000063 | prose | pages [3] -->
However, little attention is drawn to the interactions between different plant organs

<!-- b000064 | prose | pages [3] -->
(e.g. leaf, branch) and the influence from the system as an entity. To fill this gap, we

<!-- b000065 | prose | pages [3] -->
construct a mathematical model to interpret such in-leaf communications, and

<!-- b000066 | prose | pages [3] -->
perform our analysis on simple leaves.

<!-- b000067 | prose | pages [3] -->
As is shown in some literatures (Stern et al., 2008), simple leaves are classified into

<!-- b000068 | prose | pages [3] -->
different shape catalogs (Figure 1), such as flabellate leaves (e.g. ginkgo), palmate

<!-- b000069 | prose | pages [3] -->
leaves (e.g. maple), and cordate leaves (e.g. Hibiscus tiliaceus). The major criteria of

<!-- b000070 | prose | pages [3] -->
classification are the shape apex, base, and margin of leaves.

<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | caption | pages [3] -->
Figure 1 Shape of Leaves

<!-- b000073 | prose | pages [3] -->
Leaf venation is also a critical component of leaf types. There are three major

<!-- b000074 | prose | pages [3] -->
patterns of major vein organization: pinnate, palmate, and parallel, as are shown in

<!-- b000075 | caption | pages [3] -->
Figure 2.

<!-- b000076 | furniture | pages [4] -->
Team # 14297

<!-- b000077 | furniture | pages [4] -->


<!-- b000078 | furniture | pages [4] -->
Page 4 of 45

<!-- b000079 | furniture | pages [4] -->


<!-- b000080 | caption | pages [4] -->
Figure 2 Leaf Venation

<!-- b000081 | prose | pages [4] -->
Besides the diversification in leaf shapes and venation, arrangement of leaves on a

<!-- b000082 | prose | pages [4] -->
stem (phyllotaxy) are generally in three distinct patterns (Figure 3), which are defined

<!-- b000083 | prose | pages [4] -->
by the number of leaves attached to a single node. In most species, leaves are attached

<!-- b000084 | prose | pages [4] -->
alternately or in a spiral along a stem, with one leaf per node. This is called an

<!-- b000085 | prose | pages [4] -->
alternate arrangement. If two leaves are attached at each node, they provide an

<!-- b000086 | prose | pages [4] -->
opposite arrangement. Leaves are whorled when three or more occur at a node. A

<!-- b000087 | prose | pages [4] -->
special case in opposite arrangement is called decussate, if successive pairs are

<!-- b000088 | prose | pages [4] -->
orientated at 90o to each other.

<!-- b000089 | furniture | pages [4] -->


<!-- b000090 | furniture | pages [4] -->


<!-- b000091 | caption | pages [4] -->
Figure 3 Leaf Arrangement

<!-- b000092 | prose | pages [4] -->
Review of previous researches shows that most models developed are based on

<!-- b000093 | prose | pages [4] -->
statistical results (Greig-Smith, 1983). And so far, no model is built to indicate the

<!-- b000094 | prose | pages [4] -->
effect of plant organ interactions (leaf-leaf, leaf-branch) on leaf shapes. The

<!-- b000095 | prose | pages [4] -->
mathematical model presented by us demonstrates the logic of plant-environment and

<!-- b000096 | prose | pages [4] -->
in-plant communications at physiology, inter-organ, and tree system levels. We first

<!-- b000097 | furniture | pages [5] -->
Team # 14297

<!-- b000098 | furniture | pages [5] -->


<!-- b000099 | furniture | pages [5] -->
Page 5 of 45

<!-- b000100 | prose | pages [5] -->
start from isolated parts (leaves), build connections (leaf-leaf, leaf-branch) and end

<!-- b000101 | prose | pages [5] -->
with the big picture of the entire system (tree).

<!-- b000102 | prose | pages [5] -->
Problem A requires mathematical modeling of tree leaves as well as how leaf traits

<!-- b000103 | prose | pages [5] -->
impose influence on the tree system. It is suggested that shape factor of individual

<!-- b000104 | prose | pages [5] -->
leaves to be analyzed via the following aspects.

<!-- b000105 | prose | pages [5] -->
 Influencing elements of leaf shapes;

<!-- b000106 | prose | pages [5] -->
 Inter-leaf relations (i.e. overlapping between leaves)

<!-- b000107 | prose | pages [5] -->
 Branch-leaf relations

<!-- b000108 | prose | pages [5] -->
 Tree-leaf relations (i.e. estimating mass of leaves)

<!-- b000109 | prose | pages [5] -->
The model used should be able to capture not only the characteristics of single

<!-- b000110 | prose | pages [5] -->
leaves but also their interactions with other plant organs and eventually the tree

<!-- b000111 | prose | pages [5] -->
system. We have to start from isolated parts (leaves), build connections (leaf-leaf,

<!-- b000112 | prose | pages [5] -->
leaf-branch) and end with the big picture of the entire system (tree).

<!-- b000113 | prose | pages [5] -->
We divide the modeling section into four subsections.

<!-- b000114 | prose | pages [5] -->
 Section 2.1: Descriptive model of leaf traits;

<!-- b000115 | prose | pages [5] -->
 Section 2.2: Model of cell growth & physiological activities;

<!-- b000116 | prose | pages [5] -->
(photosynthesis, transportation, transpiration)

<!-- b000117 | prose | pages [5] -->
 Section 2.3: Model of leaf arrangement & branching structure;

<!-- b000118 | prose | pages [5] -->
 Section 2.4: Model of the tree characteristics.

<!-- b000119 | prose | pages [5] -->
(ATP governing equation, Driving Force governing equation)

<!-- b000120 | prose | pages [5] -->
The first two subsections of modeling are for analysis at leaf level. To quantify the

<!-- b000121 | prose | pages [5] -->
geometric characteristics of various leaves, shapes are described by functions and

<!-- b000122 | prose | pages [5] -->
curves are placed in Polar Coordinates, so that differences can be visualized.

<!-- b000123 | prose | pages [5] -->
Parameter selection can then easily adjust the leaf shapes, thus providing more

<!-- b000124 | prose | pages [5] -->
flexibility in deriving the bio-features such as size and perimeter. As for the shape

<!-- b000125 | prose | pages [5] -->
influencing factors, processes of growth and photosynthesis are assumed to determine

<!-- b000126 | prose | pages [5] -->
the effective blade area of leaves, while plant transport system and transpiration are

<!-- b000127 | prose | pages [5] -->
closely related with leaf venation. These physiological activities are modeled in

<!-- b000128 | prose | pages [5] -->
Section 2.2.

<!-- b000129 | furniture | pages [5] -->


<!-- b000130 | furniture | pages [6] -->
Team # 14297

<!-- b000131 | furniture | pages [6] -->


<!-- b000132 | furniture | pages [6] -->
Page 6 of 45

<!-- b000133 | prose | pages [6] -->
At the branch level in Section2.3, arrangements of leaves and branches are taken

<!-- b000134 | prose | pages [6] -->
into account. We compute the overlapping area of leaves via geometric analysis. Since

<!-- b000135 | prose | pages [6] -->
finding the area of irregular shadow region is troublesome and not easily compared,

<!-- b000136 | prose | pages [6] -->
we standardized the computation by using round circles as equivalents to diverse leaf

<!-- b000137 | prose | pages [6] -->
shapes. The angle over the two opposite leaf-edges is taken as indicators for leaf types.

<!-- b000138 | prose | pages [6] -->
Tree profile is modeled by rod-based method (LA system). In Section2.4,by solving

<!-- b000139 | prose | pages [6] -->
the two governing equations for ATP and driving force, tree height and angles of shoot

<!-- b000140 | prose | pages [6] -->
can be derived, which will be then applied to compute the volume of the tree.

<!-- b000141 | prose | pages [6] -->
Eventually, traits of isolated leaves and the tree are linked together.

<!-- b000142 | furniture | pages [6] -->


<!-- b000143 | furniture | pages [6] -->


<!-- b000144 | furniture | pages [6] -->


<!-- b000145 | furniture | pages [7] -->
Team # 14297

<!-- b000146 | furniture | pages [7] -->


<!-- b000147 | furniture | pages [7] -->


<!-- b000148 | furniture | pages [7] -->
Page 7 of 45

<!-- b000149 | heading | pages [7] -->
The Models

<!-- b000150 | heading | pages [7] -->
2.1 Descriptive Model of Leaf Shape

<!-- b000151 | prose | pages [7] -->
In Section 2.1 we present several kinds of leaf shapes to describe some mostly-seen

<!-- b000152 | prose | pages [7] -->
single leaves. Although shapes of tree leaves can be in great variety, the classification

<!-- b000153 | prose | pages [7] -->
discussed here only applies to selected types of single leaves, which are flattened,

<!-- b000154 | prose | pages [7] -->
colored in green, and spinelike, regardless of textures. Leaves that are tubular,

<!-- b000155 | prose | pages [7] -->
feathery, cup-shaped, or needlelike require 3-dimensional models and are not taken

<!-- b000156 | prose | pages [7] -->
into account for simplicity purpose. In Table 2.1, some of the typical plant and their

<!-- b000157 | prose | pages [7] -->
leaf shapes are listed before we transform their morphological features into the

<!-- b000158 | prose | pages [7] -->
language of mathematics.

<!-- b000159 | caption | pages [7] -->
Table 1 Representative Plant with Various Leaf Types

<!-- b000160 | prose | pages [7] -->
Type of Leaf

<!-- b000161 | prose | pages [7] -->
Shapes

<!-- b000162 | prose | pages [7] -->
Orbicular

<!-- b000163 | furniture | pages [7] -->


<!-- b000164 | prose | pages [7] -->
Cordate

<!-- b000165 | furniture | pages [7] -->


<!-- b000166 | prose | pages [7] -->
Reniform

<!-- b000167 | furniture | pages [7] -->


<!-- b000168 | prose | pages [7] -->
Representative Plant

<!-- b000169 | prose | pages [7] -->
Nasturtium Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Order: Geraniales Family: Tropaeolaceae – Nasturtium family Genus: Tropaeolum L. – nasturtium

<!-- b000170 | prose | pages [7] -->
Eastern redbud Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Order: Fabales Family: Fabaceae – Pea family Genus: Cercis L. – redbud Species: Cercis canadensis L. – eastern redbud

<!-- b000171 | prose | pages [7] -->
Spadeleaf Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Order: Apiales Family: Apiaceae – Carrot family Genus: Centella L. – centella Species: Centella asiatica (L.) Urb. – spadeleaf

<!-- b000172 | furniture | pages [8] -->
Team # 14297

<!-- b000173 | prose | pages [8] -->
Lobed

<!-- b000174 | furniture | pages [8] -->


<!-- b000175 | prose | pages [8] -->
Palmate

<!-- b000176 | furniture | pages [8] -->


<!-- b000177 | prose | pages [8] -->
Elliptic

<!-- b000178 | furniture | pages [8] -->


<!-- b000179 | prose | pages [8] -->
Flabellate

<!-- b000180 | furniture | pages [8] -->


<!-- b000181 | furniture | pages [8] -->


<!-- b000182 | furniture | pages [8] -->


<!-- b000183 | furniture | pages [8] -->
Page 8 of 45

<!-- b000184 | prose | pages [8] -->
Cassava Kingdom: Plantae – Plants Division:

<!-- b000185 | prose | pages [8] -->
Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Order: Euphorbiales Family: Euphorbiaceae – Spurge family Genus: Manihot Mill. – cassava Species: Manihot esculenta Crantz – cassava

<!-- b000186 | prose | pages [8] -->
Wine Grape Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Order: Rhamnales Family: Vitaceae – Grape family Genus: Vitis L. – grape Species: Vitis vinifera L. – wine grape

<!-- b000187 | prose | pages [8] -->
Tea Kingdom : Plantae – Plants Division:

<!-- b000188 | prose | pages [8] -->
Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Order: Theales Family: Theaceae – Tea family Genus: Camellia L. – camellia Species: Camellia sinensis (L.) Kuntze – tea

<!-- b000189 | prose | pages [8] -->
Maidenhair Tree Kingdom: Plantae – Plants Division: Ginkgophyta – Ginkgo Class: Ginkgoopsida Order: Ginkgoales Family: Ginkgoaceae – Ginkgo family Genus: Ginkgo L. – ginkgo Species: Ginkgo biloba L. – maidenhair tree

<!-- b000190 | prose | pages [8] -->
These leaf shape types are described by functions with adjustable parameters.

<!-- b000191 | prose | pages [8] -->
Plotting their curve functions with specific coefficients in Polar Coordinates, we can

<!-- b000192 | prose | pages [8] -->
visualize differences between shapes. To quantify such differences, we derive the

<!-- b000193 | prose | pages [8] -->
expression of leaf area A as well as length of leaf margins S , by finding the following

<!-- b000194 | prose | pages [8] -->
integrals.

<!-- b000195 | prose | pages [8] -->
 A

<!-- b000196 | prose | pages [8] -->
 S

<!-- b000197 | prose | pages [8] -->
rdrd

<!-- b000198 | furniture | pages [8] -->


<!-- b000199 | prose | pages [8] -->
rd

<!-- b000200 | furniture | pages [8] -->


<!-- b000201 | furniture | pages [9] -->
Team # 14297

<!-- b000202 | furniture | pages [9] -->


<!-- b000203 | furniture | pages [9] -->


<!-- b000204 | furniture | pages [9] -->
Page 9 of 45

<!-- b000205 | prose | pages [9] -->
It should be noted that S refers to the part of leaf margin where cell division

<!-- b000206 | prose | pages [9] -->
occurs, rather than the perimeter of the blade. In Figure 1 to 6, this portion is

<!-- b000207 | prose | pages [9] -->
illustrated by the black edge of the shape curves, and the red nod at the origin denotes

<!-- b000208 | prose | pages [9] -->
the auxin sink of the leaf.

<!-- b000209 | prose | pages [9] -->
 Type 1: Orbicular leaves

<!-- b000210 | prose | pages [9] -->
Shape of an orbicular leaf is a round circle, and can be written as

<!-- b000211 | prose | pages [9] -->
a   r a , 0 0 (1)

<!-- b000212 | prose | pages [9] -->
where a interprets the radius of the leaf.

<!-- b000213 | furniture | pages [9] -->


<!-- b000214 | furniture | pages [9] -->


<!-- b000215 | caption | pages [9] -->
Figure 4 Shape function of Orbicular leaves (a=5)

<!-- b000216 | prose | pages [9] -->
By integration, we can find the size and cell-division margin length of orbicular

<!-- b000217 | prose | pages [9] -->
leaves

<!-- b000218 | prose | pages [9] -->
  2 (2) 1A a

<!-- b000219 | prose | pages [9] -->
  S 2 a (3) 1

<!-- b000220 | furniture | pages [9] -->


<!-- b000221 | prose | pages [9] -->
 Type 2: Cordate leaves & Reniform leaves

<!-- b000222 | prose | pages [9] -->
The shapes of cordate and reniform leaves have a lot in common, with the

<!-- b000223 | prose | pages [9] -->
former one shapes like a heart and the latter a kidney. Such features can both be

<!-- b000224 | furniture | pages [10] -->
Team # 14297

<!-- b000225 | prose | pages [10] -->
captured by a trigonometric function.

<!-- b000226 | prose | pages [10] -->
   , r a (1 cos )

<!-- b000227 | furniture | pages [10] -->


<!-- b000228 | furniture | pages [10] -->


<!-- b000229 | furniture | pages [10] -->
Page 10 of 45

<!-- b000230 | prose | pages [10] -->
a  0 (4)

<!-- b000231 | furniture | pages [10] -->


<!-- b000232 | caption | pages [10] -->
Figure 5 Shape function of Reniform Leaves (a = 5)

<!-- b000233 | prose | pages [10] -->
Size of Leaf area and cell-division margin length are

<!-- b000234 | prose | pages [10] -->
 3  A 2 2

<!-- b000235 | prose | pages [10] -->
    S 2

<!-- b000236 | prose | pages [10] -->
2 2

<!-- b000237 | prose | pages [10] -->
a a

<!-- b000238 | prose | pages [10] -->
(5)

<!-- b000239 | furniture | pages [10] -->


<!-- b000240 | prose | pages [10] -->
  2 2 a (6)

<!-- b000241 | prose | pages [10] -->
 Type 3: Lobed leaves, & Palmate leaves

<!-- b000242 | prose | pages [10] -->
Another form of trigonometric function is used to describe lobed and palmate

<!-- b000243 | prose | pages [10] -->
leaves. We can adjust the range of parameter to control the indentation of

<!-- b000244 | prose | pages [10] -->
margins.

<!-- b000245 | prose | pages [10] -->
  r a b sin( k (7) )

<!-- b000246 | prose | pages [10] -->
where a, b are both positive constants, k are natural numbers indicating the

<!-- b000247 | prose | pages [10] -->
amount of lobes.

<!-- b000248 | furniture | pages [11] -->
Team # 14297

<!-- b000249 | furniture | pages [11] -->


<!-- b000250 | furniture | pages [11] -->


<!-- b000251 | furniture | pages [11] -->
Page 11 of 45

<!-- b000252 | furniture | pages [11] -->


<!-- b000253 | caption | pages [11] -->
Figure 6 Shape function of lobed Leaves (a = 3, b=2, k=5)

<!-- b000254 | furniture | pages [11] -->


<!-- b000255 | caption | pages [11] -->
Figure 7 Shape function of Palmate Leaves (a = 3.8, b=1.2, k=5)

<!-- b000256 | prose | pages [11] -->
Area and margin length of leaves

<!-- b000257 | prose | pages [11] -->
 A ( a 3

<!-- b000258 | prose | pages [11] -->
 S 3

<!-- b000259 | prose | pages [11] -->
 Type 4: Elliptic Leaves

<!-- b000260 | prose | pages [11] -->
 b  2 2 2 (8) )

<!-- b000261 | prose | pages [11] -->
 2 2 a (9)

<!-- b000262 | prose | pages [11] -->
Leaves of this type are oval-shaped, which is expressed by a pair of symmetric

<!-- b000263 | prose | pages [11] -->
trigonometric functions (10).

<!-- b000264 | furniture | pages [12] -->
Team # 14297

<!-- b000265 | prose | pages [12] -->
1 (sin    a cos ) 4

<!-- b000266 | furniture | pages [12] -->


<!-- b000267 | furniture | pages [12] -->


<!-- b000268 | prose | pages [12] -->
1    a (sin cos ) 2

<!-- b000269 | furniture | pages [12] -->


<!-- b000270 | furniture | pages [12] -->


<!-- b000271 | furniture | pages [12] -->
Page 12 of 45

<!-- b000272 | prose | pages [12] -->
1      2

<!-- b000273 | prose | pages [12] -->
( a  0 )               (10)

<!-- b000274 | prose | pages [12] -->
3       4

<!-- b000275 | furniture | pages [12] -->


<!-- b000276 | caption | pages [12] -->
Figure 8 Shape Function of Elliptic Leaves (a=10, k=1/4)

<!-- b000277 | prose | pages [12] -->
The cell division accounts for a proportion much larger than the none-division

<!-- b000278 | prose | pages [12] -->
part (i.e. the black edge in Figure 5), and can be ignored when we compute the

<!-- b000279 | prose | pages [12] -->
margin length S .

<!-- b000280 | prose | pages [12] -->
Area and cell division margin length of the leaf are

<!-- b000281 | prose | pages [12] -->
 1    2 A a  4 4 

<!-- b000282 | prose | pages [12] -->
   S 2 a sin( k 4

<!-- b000283 | prose | pages [12] -->
 Type 5: Flabellate Leaves

<!-- b000284 | prose | pages [12] -->
 1 1

<!-- b000285 | prose | pages [12] -->
(11)

<!-- b000286 | prose | pages [12] -->
 2 2 

<!-- b000287 | prose | pages [12] -->
     ) ) cos( k ) 1 (12)

<!-- b000288 | prose | pages [12] -->
Flabellate leaves are fan-shaped, which can be resembled by a sector of a pie.

<!-- b000289 | prose | pages [12] -->
By changing the central angle and radius, the leaf shape can be adjusted. It is

<!-- b000290 | prose | pages [12] -->
described by function (13).

<!-- b000291 | prose | pages [12] -->
  r a k , 1      k (13) 2

<!-- b000292 | prose | pages [12] -->
2k are constants defining the domain of the central angle . 1k , where

<!-- b000293 | prose | pages [12] -->
The following graph illustrates the shape of flabellate leaves by taking the

<!-- b000294 | furniture | pages [13] -->
Team # 14297

<!-- b000295 | prose | pages [13] -->
radius to be 5, and central angle 1  4

<!-- b000296 | furniture | pages [13] -->


<!-- b000297 | furniture | pages [13] -->


<!-- b000298 | furniture | pages [13] -->
Page 13 of 45

<!-- b000299 | prose | pages [13] -->
3      . 4

<!-- b000300 | furniture | pages [13] -->


<!-- b000301 | caption | pages [13] -->
Figure 9 Shape Function of Flabellate Leaves (a=5)

<!-- b000302 | prose | pages [13] -->
Area and margin length of leaves are shown below.

<!-- b000303 | prose | pages [13] -->
  A 2( k 5 2

<!-- b000304 | prose | pages [13] -->
 

<!-- b000305 | prose | pages [13] -->
k a  2 (14) ) 1 1

<!-- b000306 | prose | pages [13] -->
  k a S ( k 5 2 ) ) 2 a (15) 1 1

<!-- b000307 | furniture | pages [13] -->


<!-- b000308 | heading | pages [13] -->
2.2 Model of cell growth and physiological activities

<!-- b000309 | heading | pages [13] -->
2.2.1 Growth Model

<!-- b000310 | prose | pages [13] -->
Given the prominence of leaves in our environment and their importance for plant

<!-- b000311 | prose | pages [13] -->
function, it is surprising that so little is known about the physiological process

<!-- b000312 | prose | pages [13] -->
developing these organs. Most studies of leaf function have focused on photosynthetic

<!-- b000313 | prose | pages [13] -->
capacity, light interception, and responses of leaves to the environment. However up

<!-- b000314 | prose | pages [13] -->
to the current time, there is no exactly biological theory that could explain the inner

<!-- b000315 | prose | pages [13] -->
mechanism of cell growth.

<!-- b000316 | prose | pages [13] -->
Many factors contribute to the regulation of cell growth, involving biophysical

<!-- b000317 | prose | pages [13] -->
considerations, wall extension, osmotic regulation, photobiological control of ion

<!-- b000318 | prose | pages [13] -->
fluxes, and other extraneous factors in the environment (Van Volkengurgh, 1999).

<!-- b000319 | furniture | pages [14] -->
Team # 14297

<!-- b000320 | furniture | pages [14] -->


<!-- b000321 | furniture | pages [14] -->


<!-- b000322 | furniture | pages [14] -->
Page 14 of 45

<!-- b000323 | prose | pages [14] -->
Our model for leaf expansion is derived from the one proposed in the work of

<!-- b000324 | prose | pages [14] -->
Lizaso et al. (2002), but improves the original version by including cell division along

<!-- b000325 | prose | pages [14] -->
the leaf margin. The sigmoidal logistic model is applied to fulfill the basic

<!-- b000326 | prose | pages [14] -->
requirement of cell growth model and to simulate the process of leaf expansion.

<!-- b000327 | prose | pages [14] -->
LA by a sigmoidal Lizaso et al. (2002) show the expansion of each leaf blade

<!-- b000328 | prose | pages [14] -->
logistic function:

<!-- b000329 | prose | pages [14] -->
Ae  LA e i 1

<!-- b000330 | prose | pages [14] -->
i

<!-- b000331 | prose | pages [14] -->
(16) i i  ke t te ( ( ) i i i

<!-- b000332 | prose | pages [14] -->
Ae is the final surface area of the ith leaf, where i

<!-- b000333 | prose | pages [14] -->
reaches 50% of its final area.

<!-- b000334 | prose | pages [14] -->
Differing from Lizaso’s definition of

<!-- b000335 | prose | pages [14] -->
te is the thermal time when the leaf i

<!-- b000336 | prose | pages [14] -->
ke , we define this term as a polynomial of i i

<!-- b000337 | prose | pages [14] -->
degree n about the length of cell-division leaf margin S :

<!-- b000338 | prose | pages [14] -->
n

<!-- b000339 | prose | pages [14] -->


<!-- b000340 | prose | pages [14] -->
ke i

<!-- b000341 | prose | pages [14] -->


<!-- b000342 | prose | pages [14] -->
i

<!-- b000343 | prose | pages [14] -->
0

<!-- b000344 | prose | pages [14] -->
i

<!-- b000345 | prose | pages [14] -->
(17)

<!-- b000346 | prose | pages [14] -->
a S a S i i

<!-- b000347 | prose | pages [14] -->
GR ei Daily calculation of leaf expansion is conducted in the form of growth rate of

<!-- b000348 | prose | pages [14] -->
each leaf at thermal timet . The result is obtained from the first derivative of (1):

<!-- b000349 | prose | pages [14] -->
dLA

<!-- b000350 | prose | pages [14] -->
 

<!-- b000351 | prose | pages [14] -->
i GR

<!-- b000352 | prose | pages [14] -->
e (

<!-- b000353 | prose | pages [14] -->
Ae ke i dt

<!-- b000354 | prose | pages [14] -->
 

<!-- b000355 | prose | pages [14] -->
ke t te

<!-- b000356 | prose | pages [14] -->
( )

<!-- b000357 | prose | pages [14] -->
e

<!-- b000358 | prose | pages [14] -->
i i

<!-- b000359 | prose | pages [14] -->
(18)

<!-- b000360 | prose | pages [14] -->
) (1

<!-- b000361 | prose | pages [14] -->
 

<!-- b000362 | prose | pages [14] -->
i i i i

<!-- b000363 | prose | pages [14] -->


<!-- b000364 | prose | pages [14] -->
ke t te

<!-- b000365 | prose | pages [14] -->
( ) 2

<!-- b000366 | prose | pages [14] -->
e

<!-- b000367 | prose | pages [14] -->
)

<!-- b000368 | prose | pages [14] -->
i i

<!-- b000369 | prose | pages [14] -->
Ae is the final area of leaf blade. where parameter i

<!-- b000370 | heading | pages [14] -->
2.2.2 Model for physiological activities

<!-- b000371 | prose | pages [14] -->
In this subsection, we devote our interest to the structure of leaves and how those

<!-- b000372 | prose | pages [14] -->
structures are adapted to carry out effectively certain physiological and biochemical

<!-- b000373 | prose | pages [14] -->
functions. Three types of physiological activities are modeled and evaluation of their

<!-- b000374 | prose | pages [14] -->
effects on leaves’ shape characters is performed. These physiological functions are

<!-- b000375 | furniture | pages [15] -->
Team # 14297

<!-- b000376 | furniture | pages [15] -->


<!-- b000377 | furniture | pages [15] -->
Page 15 of 45

<!-- b000378 | prose | pages [15] -->
photosynthesis, substance transportation, and transpiration.

<!-- b000379 | prose | pages [15] -->
Photosynthesis: Energy Conservation

<!-- b000380 | furniture | pages [15] -->


<!-- b000381 | caption | pages [15] -->
Figure 10 Photosynthesis Process

<!-- b000382 | prose | pages [15] -->
Photosynthesis is the primary function of green vegetation which allows the plant

<!-- b000383 | prose | pages [15] -->
to conserve solar energy to stable chemical form (William & Norman, 2009). After

<!-- b000384 | prose | pages [15] -->
the photosynthesis machine generates utilizable energy, ATP is provided to the whole

<!-- b000385 | prose | pages [15] -->
plant. To absorb light efficiently, leaves usually present a large surface area to the

<!-- b000386 | prose | pages [15] -->
incoming sunlight. And the effective area is to a great extent associated with the

<!-- b000387 | prose | pages [15] -->
efficiency of photosynthesis. The physiological and biochemical functions of leaves

<!-- b000388 | prose | pages [15] -->
are targeted in our model at the same time.

<!-- b000389 | prose | pages [15] -->
We model the energy conservation process by simulating its two stages:

<!-- b000390 | prose | pages [15] -->
Light-dependent reactions and CO2 assimilation.

<!-- b000391 | furniture | pages [15] -->


<!-- b000392 | furniture | pages [16] -->
Team # 14297

<!-- b000393 | prose | pages [16] -->
 Harvesting sunlight

<!-- b000394 | furniture | pages [16] -->


<!-- b000395 | furniture | pages [16] -->


<!-- b000396 | furniture | pages [16] -->
Page 16 of 45

<!-- b000397 | prose | pages [16] -->
A series of steps, called light-dependent reactions describe how chloroplasts

<!-- b000398 | prose | pages [16] -->
conserve energy from sunlight to ATP and reducing potential (as NADPH). The

<!-- b000399 | prose | pages [16] -->
biological principle followed in this stage is that plant leaves are photosynthetic

<!-- b000400 | prose | pages [16] -->
machines that maximize the absorption of light. This principle is the guideline of our

<!-- b000401 | prose | pages [16] -->
model constructing procedures. It also applies to our model construction in Section

<!-- b000402 | prose | pages [16] -->
2.3 when considering leaf overlapping.

<!-- b000403 | prose | pages [16] -->
The efficiency of photosynthesis denoted by  can be estimated by a function of

<!-- b000404 | prose | pages [16] -->
incident light intensity I and the probability of radiation penetration in forest

<!-- b000405 | prose | pages [16] -->
canopies P , where P can be expressed as a function of the zenith angle:

<!-- b000406 | prose | pages [16] -->
   (19) I P ( )

<!-- b000407 | prose | pages [16] -->
The intensity of incident light I is generated from the Black-radiation formula in

<!-- b000408 | prose | pages [16] -->
general physics, which is expressed by the following equation:

<!-- b000409 | prose | pages [16] -->


<!-- b000410 | prose | pages [16] -->
5

<!-- b000411 | prose | pages [16] -->
k

<!-- b000412 | prose | pages [16] -->


<!-- b000413 | prose | pages [16] -->
I

<!-- b000414 | prose | pages [16] -->
(20)

<!-- b000415 | prose | pages [16] -->
c

<!-- b000416 | prose | pages [16] -->


<!-- b000417 | prose | pages [16] -->
e

<!-- b000418 | prose | pages [16] -->
1

<!-- b000419 | prose | pages [16] -->
kT

<!-- b000420 | prose | pages [16] -->
where k is the Boltzmann constant; is the wavelength;

<!-- b000421 | prose | pages [16] -->
is the Planck constant;

<!-- b000422 | prose | pages [16] -->
c is the speed of light; and T is the absolute temperature of the black body.

<!-- b000423 | prose | pages [16] -->
Radiation penetration probability P is developed based on the work of Chen et

<!-- b000424 | prose | pages [16] -->
al. (1997a). It is the probability of a direct bean penetrating through a forest at

<!-- b000425 | prose | pages [16] -->
zenith angle 

<!-- b000426 | prose | pages [16] -->
     K

<!-- b000427 | prose | pages [16] -->
( ) ( )

<!-- b000428 | prose | pages [16] -->
  P

<!-- b000429 | prose | pages [16] -->
( ) exp

<!-- b000430 | prose | pages [16] -->
e

<!-- b000431 | prose | pages [16] -->
   

<!-- b000432 | prose | pages [16] -->
(1 )cos( )

<!-- b000433 | prose | pages [16] -->


<!-- b000434 | prose | pages [16] -->
e

<!-- b000435 | prose | pages [16] -->
 where L is the Leaf Area Index (LAI);

<!-- b000436 | prose | pages [16] -->
 L L

<!-- b000437 | prose | pages [16] -->
(21)

<!-- b000438 | prose | pages [16] -->
   

<!-- b000439 | prose | pages [16] -->
e  ( ) is the canopy non-randomness index;

<!-- b000440 | prose | pages [16] -->
eis a correction factor for within-shoot clumping in conifers; is the

<!-- b000441 | furniture | pages [17] -->
Team # 14297

<!-- b000442 | furniture | pages [17] -->


<!-- b000443 | furniture | pages [17] -->


<!-- b000444 | furniture | pages [17] -->
Page 17 of 45

<!-- b000445 | prose | pages [17] -->
woody-to-total foliage hemi-surface area ratio in the canopy and can be

<!-- b000446 | prose | pages [17] -->
numerically demonstrated by:

<!-- b000447 | prose | pages [17] -->
W  (22)  W L

<!-- b000448 | prose | pages [17] -->
where W is the total woody hemi-surface area index of branches and stems.

<!-- b000449 | prose | pages [17] -->
 CO2 assimilation

<!-- b000450 | prose | pages [17] -->
Photosynthetic gas exchange between leaf and air is controlled by the opening and

<!-- b000451 | prose | pages [17] -->
closing of stomata, where photosynthetic carbon reduction (PCR) cycle occurs. We

<!-- b000452 | prose | pages [17] -->
focus on the CO2 assimilation process: how CO2 enters the leaf and subsequently is

<!-- b000453 | prose | pages [17] -->
reduced through the utilization of the NADPH and ATP produced by photosynthetic

<!-- b000454 | prose | pages [17] -->
electron transport.

<!-- b000455 | prose | pages [17] -->
The assumption is made that the production ratio of CO2 over O2 is taken as 1. We

<!-- b000456 | prose | pages [17] -->
model the time dependence of CO2 assimilation by a set of differential equations

<!-- b000457 | prose | pages [17] -->
proposed by Marcelo et al. (2000). The model is divided into three parts. The number

<!-- b000458 | prose | pages [17] -->
of CO2 receivers and excited receivers are determined by concentration of CO2 and

<!-- b000459 | prose | pages [17] -->
radiant flux intensity. The amount of product, substance and complex can be all

<!-- b000460 | prose | pages [17] -->
predicted by time-dependent differential equations. The product can be seen as one

<!-- b000461 | prose | pages [17] -->
kind of indicator to demonstrate how much energy has been generated by the plant.

<!-- b000462 | prose | pages [17] -->
 Part A

<!-- b000463 | prose | pages [17] -->
Two main phenomenological differential equations are introduced for the number

<!-- b000464 | prose | pages [17] -->
N t and the quantity of CO2 receivers of light excited receiver ( )

<!-- b000465 | prose | pages [17] -->
dN t ( )    k I N N t 1 r max dt

<!-- b000466 | prose | pages [17] -->
dM t ( )    k C M 3 max dt

<!-- b000467 | prose | pages [17] -->
M t , respectively:

<!-- b000468 | prose | pages [17] -->
( )

<!-- b000469 | prose | pages [17] -->
  (23) ( ) k M t N t ( ) ( ) 2

<!-- b000470 | prose | pages [17] -->
  (24) M t ( ) k M t N t ( ) ( ) 4

<!-- b000471 | prose | pages [17] -->
4k are phenomenological parameters; 1k , 2k , 3k ,and where N is the total number max

<!-- b000472 | furniture | pages [18] -->
Team # 14297

<!-- b000473 | furniture | pages [18] -->


<!-- b000474 | furniture | pages [18] -->


<!-- b000475 | furniture | pages [18] -->
Page 18 of 45

<!-- b000476 | prose | pages [18] -->
rI is the radiant flux intensity; C is the concentration of of light excited receivers,

<!-- b000477 | prose | pages [18] -->
M is the total number of CO2 receivers. CO2 in the mesophyll, and max

<!-- b000478 | prose | pages [18] -->
 Part B

<!-- b000479 | prose | pages [18] -->
Marcelo et al. (2000) show another equation for result comparison. This equation

<!-- b000480 | prose | pages [18] -->
involves the assimilation of CO2 in closed measurement system:

<!-- b000481 | prose | pages [18] -->
dC t ( )       (25) ( ) 1 k C t 5 dt

<!-- b000482 | prose | pages [18] -->
6k where represents the effect of

<!-- b000483 | prose | pages [18] -->
M t ( )     k 5 1 m t ( ) , and the term m t ( ) M

<!-- b000484 | prose | pages [18] -->
max

<!-- b000485 | prose | pages [18] -->
m t ( ) k 6

<!-- b000486 | prose | pages [18] -->
CO2-production by photorespiration,

<!-- b000487 | prose | pages [18] -->
  represents the effect of CO2 reduction on

<!-- b000488 | prose | pages [18] -->
the CO2 concentration of the measurement system.

<!-- b000489 | prose | pages [18] -->
 Part C

<!-- b000490 | prose | pages [18] -->
To formulate the enzyme reaction equations, the following set of differential

<!-- b000491 | prose | pages [18] -->
equations are constructed:

<!-- b000492 | prose | pages [18] -->
dp t ( )  k se t ( ) 7 dt

<!-- b000493 | prose | pages [18] -->
dse t ( )   k s t ( ) ( k s t ( ) 8 8 dt

<!-- b000494 | prose | pages [18] -->
ds t ( )   k s t ( ) ( k s t 8 8 dt

<!-- b000495 | prose | pages [18] -->
(26)

<!-- b000496 | prose | pages [18] -->
   (27) k k k se t ) ( ) 8 7

<!-- b000497 | prose | pages [18] -->
 (28) ( ) ( ) k se t ) ( ) 8

<!-- b000498 | prose | pages [18] -->
8k are the rates of the reactions; 7k and where

<!-- b000499 | prose | pages [18] -->
substrate; and se t is a complex. ( )

<!-- b000500 | prose | pages [18] -->
p t is the product;

<!-- b000501 | prose | pages [18] -->
s t is the ( ) ( )

<!-- b000502 | prose | pages [18] -->
The amount of product will be shown in the governing equations in Section 2.4 to

<!-- b000503 | prose | pages [18] -->
estimate the properties of the whole tree system.

<!-- b000504 | furniture | pages [19] -->
Team # 14297

<!-- b000505 | furniture | pages [19] -->


<!-- b000506 | furniture | pages [19] -->
Page 19 of 45

<!-- b000507 | prose | pages [19] -->
Transportation

<!-- b000508 | prose | pages [19] -->
Nutrient salts, ions, and steroids are of vital importance to the growth and

<!-- b000509 | prose | pages [19] -->
development of plants. Take auxin as an example, which is a kind of plant hormone,

<!-- b000510 | prose | pages [19] -->
plays a central role in the in-plant activities including vascular development. The

<!-- b000511 | prose | pages [19] -->
uptake of these substances by plants involves various types of transportation

<!-- b000512 | prose | pages [19] -->
procedures like simple diffusion, facilitated diffusion, or active transportation.

<!-- b000513 | prose | pages [19] -->
Facilitated diffusion and active transport are mediated by channel and carrier proteins,

<!-- b000514 | prose | pages [19] -->
of which the latter requires a source of metabolic energy, normally in the form of ATP.

<!-- b000515 | prose | pages [19] -->
We model the auxin-transport system since it captures all the related elements in the

<!-- b000516 | prose | pages [19] -->
transport activities — the transport channel, the carrier, and the energy consumed.

<!-- b000517 | prose | pages [19] -->
Another notable reason for our choice is that the auxin model has the least number of

<!-- b000518 | prose | pages [19] -->
disturbing factors, like the potential distinction between external eco-system and the

<!-- b000519 | prose | pages [19] -->
internal environment of the plant to list a few.

<!-- b000520 | prose | pages [19] -->
Leaf venation patterns are used to describe the transportation behavior. To support

<!-- b000521 | prose | pages [19] -->
this view point, we provide the following reasons.

<!-- b000522 | prose | pages [19] -->
 According to fluid mechanics, after divided by the efficiency of

<!-- b000523 | prose | pages [19] -->
transportation mechanism, the flux of auxin in the veins could reflect the

<!-- b000524 | prose | pages [19] -->
distribution of transportation channels (Falkovich et al, 2011).

<!-- b000525 | prose | pages [19] -->
 In order to make this model comparable with the photosynthesis process

<!-- b000526 | prose | pages [19] -->
which occurs only inside the chloroplast of leaves, transportation activities

<!-- b000527 | prose | pages [19] -->
should also be analyzed by observing the section structure of isolated leaves.

<!-- b000528 | prose | pages [19] -->
Hence, the geometric traits of leaves, in this case cell-division margin and

<!-- b000529 | prose | pages [19] -->
size, become the determinant factors in the physiological mechanism. This

<!-- b000530 | prose | pages [19] -->
matches the intention of out model to start from individual units and extend it

<!-- b000531 | prose | pages [19] -->
to the entire system by simulating the in-plant communication.

<!-- b000532 | prose | pages [19] -->
Here we adopt the approach proposed by Hironori and Atsushi (2006), which

<!-- b000533 | furniture | pages [20] -->
Team # 14297

<!-- b000534 | furniture | pages [20] -->


<!-- b000535 | furniture | pages [20] -->


<!-- b000536 | furniture | pages [20] -->
Page 20 of 45

<!-- b000537 | prose | pages [20] -->
examine the formation of leaf venation patterns by modeling the positive feedback

<!-- b000538 | prose | pages [20] -->
regulation between plant hormone auxin and its efflux carrier. And the mathematical

<!-- b000539 | prose | pages [20] -->
model is presented below.

<!-- b000540 | prose | pages [20] -->
Individual cells are aligned as two-dimensional hexagons, with position of the cell

<!-- b000541 | prose | pages [20] -->
denoted byi and j , which are two independent directions of the hexagonal cell.

<!-- b000542 | prose | pages [20] -->
Another indicator k represents the cell membrane side of the cell. Auxin and auxin

<!-- b000543 | prose | pages [20] -->
efflux carrier are located in each side of the cell membrane, respectively.

<!-- b000544 | prose | pages [20] -->
Assuming auxin outflow from the k-th side of cell membrane of the( , ) i j cell to the

<!-- b000545 | prose | pages [20] -->
i j cell is proportional to the product of auxin efflux adjacent k’-th side of the( ', ')

<!-- b000546 | prose | pages [20] -->
a densities, the auxin flow between neighboring cells carrier p and auxin ijk ijk

<!-- b000547 | furniture | pages [20] -->


<!-- b000548 | prose | pages [20] -->
f ijk

<!-- b000549 | prose | pages [20] -->
can be obtained by the difference in the auxin outflows from the two cells:

<!-- b000550 | prose | pages [20] -->
  f cp a cp ijk ijk ij

<!-- b000551 | prose | pages [20] -->
where c is a constant.

<!-- b000552 | prose | pages [20] -->
a (29) i j k ' ' ' i j ' '

<!-- b000553 | prose | pages [20] -->
p The differential equations for the dynamics of auxin efflux carrier

<!-- b000554 | prose | pages [20] -->
a are described in the following form: ijk

<!-- b000555 | prose | pages [20] -->
dp g f

<!-- b000556 | prose | pages [20] -->
(

<!-- b000557 | prose | pages [20] -->


<!-- b000558 | prose | pages [20] -->
ijk

<!-- b000559 | prose | pages [20] -->
s 

<!-- b000560 | prose | pages [20] -->
p

<!-- b000561 | prose | pages [20] -->
dt g f

<!-- b000562 | prose | pages [20] -->
k

<!-- b000563 | prose | pages [20] -->
da dt  

<!-- b000564 | prose | pages [20] -->
ij

<!-- b000565 | prose | pages [20] -->
s d a a a

<!-- b000566 | prose | pages [20] -->
 g f

<!-- b000567 | prose | pages [20] -->
( )

<!-- b000568 | prose | pages [20] -->
ijk

<!-- b000569 | prose | pages [20] -->
1 exp[

<!-- b000570 | prose | pages [20] -->
ps is the carrier synthesis rate; where

<!-- b000571 | prose | pages [20] -->
and auxin ijk

<!-- b000572 | prose | pages [20] -->
) )

<!-- b000573 | prose | pages [20] -->


<!-- b000574 | prose | pages [20] -->
ijk ijk

<!-- b000575 | prose | pages [20] -->
d p

<!-- b000576 | prose | pages [20] -->
(30)

<!-- b000577 | prose | pages [20] -->
p ijk

<!-- b000578 | prose | pages [20] -->
( ( )

<!-- b000579 | prose | pages [20] -->
ijk

<!-- b000580 | prose | pages [20] -->
 (31) f ij ij ijk k

<!-- b000581 | prose | pages [20] -->
g f

<!-- b000582 | prose | pages [20] -->
( )

<!-- b000583 | prose | pages [20] -->
ijk

<!-- b000584 | prose | pages [20] -->
(32)     

<!-- b000585 | prose | pages [20] -->
(

<!-- b000586 | prose | pages [20] -->
f f

<!-- b000587 | prose | pages [20] -->
)]

<!-- b000588 | prose | pages [20] -->
ijk

<!-- b000589 | prose | pages [20] -->
0

<!-- b000590 | prose | pages [20] -->
as is the d is the carrier degradation rate, p p

<!-- b000591 | furniture | pages [21] -->
Team # 14297

<!-- b000592 | furniture | pages [21] -->


<!-- b000593 | furniture | pages [21] -->


<!-- b000594 | furniture | pages [21] -->
Page 21 of 45

<!-- b000595 | prose | pages [21] -->
d is the auxin degradation rate; , , auxin synthesis rate;

<!-- b000596 | prose | pages [21] -->
a  are f cs s / ( d d ) 0 p a p a

<!-- b000597 | prose | pages [21] -->
constants, and g is an increasing function of auxin flow.

<!-- b000598 | prose | pages [21] -->
Transpiration

<!-- b000599 | prose | pages [21] -->
Transpiration is the process that large amounts of water are lost by plants through

<!-- b000600 | prose | pages [21] -->
evaporation from leaf surfaces. It is driven by differences in water vapor pressure

<!-- b000601 | prose | pages [21] -->
between internal leaf spaces and the ambient air. A variety of factors influence

<!-- b000602 | prose | pages [21] -->
transpiration rate, including temperature, humidity, wind, and leaf structure. Water is

<!-- b000603 | prose | pages [21] -->
conducted upward through the plant primarily in the xylem, a tube-like system of

<!-- b000604 | prose | pages [21] -->
treachery elements. And lost water by transpiration is replenished by the absorption of

<!-- b000605 | prose | pages [21] -->
water from the soil through the root (Figure 1). It is worth noticing that transpiration

<!-- b000606 | prose | pages [21] -->
process provides the principle driving force to the operation of the whole plant system

<!-- b000607 | prose | pages [21] -->
(William & Norman, 2009).

<!-- b000608 | furniture | pages [21] -->


<!-- b000609 | caption | pages [21] -->
Figure 11 Illustration of Transpiration

<!-- b000610 | prose | pages [21] -->
Water movement in xylem is driven by transpiration and the resulting tension in the

<!-- b000611 | prose | pages [21] -->
water column which is maintained because of the high tensile strength of water.

<!-- b000612 | prose | pages [21] -->
Following this statement, we construct the transpiration model via the approach taken

<!-- b000613 | furniture | pages [22] -->
Team # 14297

<!-- b000614 | furniture | pages [22] -->


<!-- b000615 | furniture | pages [22] -->
Page 22 of 45

<!-- b000616 | prose | pages [22] -->
by Edwards et al. (1986). While he modeled flow of water in a single tree was

<!-- b000617 | prose | pages [22] -->
modeled in terms of the Darcy equation using a set of four compartments: root, stem,

<!-- b000618 | prose | pages [22] -->
branches, and leaves, we only consider transpiration through xylem.

<!-- b000619 | prose | pages [22] -->
Assumptions presented by Edward et al. (1986) are also adopted:

<!-- b000620 | prose | pages [22] -->
1) Water moves in the plant from points of high potential to points of low

<!-- b000621 | prose | pages [22] -->
potential, along pathways that exert a frictional drag or resistance to flow.

<!-- b000622 | prose | pages [22] -->
2) Flow in the xylem of plants is adequately represented by the Darcy equation.

<!-- b000623 | prose | pages [22] -->
3) The relative conductivity of the xylem is a unique function of the proportion

<!-- b000624 | prose | pages [22] -->
of void volume filled with water (i.e. relative water content).

<!-- b000625 | prose | pages [22] -->
4) The proportion of void volume that is water-filled is a function of the water

<!-- b000626 | prose | pages [22] -->
potential of the tissue.

<!-- b000627 | prose | pages [22] -->
5) Axial flow in the stem is confined to the sapwood which has uniform

<!-- b000628 | prose | pages [22] -->
proportions of void and woody metric volumes

<!-- b000629 | prose | pages [22] -->
6) The cross-sectional area of sapwood in the stem is a function of height.

<!-- b000630 | prose | pages [22] -->
7) The leaves, branches and roots are not subdivided but are treated as uniform

<!-- b000631 | prose | pages [22] -->
compartments attached in series to the clear stem.

<!-- b000632 | prose | pages [22] -->
8) At any moment, temperature is constant throughout the system.

<!-- b000633 | prose | pages [22] -->
Functions describing the process of transpiration are derived as following. The

<!-- b000634 | prose | pages [22] -->
Darcy equation defines axial flow Q by

<!-- b000635 | prose | pages [22] -->


<!-- b000636 | prose | pages [22] -->
KA

<!-- b000637 | prose | pages [22] -->
 (33)

<!-- b000638 | prose | pages [22] -->
Q l

<!-- b000639 | prose | pages [22] -->
where l is length; A is the cross-sectional area; is the potential difference; K is

<!-- b000640 | prose | pages [22] -->
the relative conductivity of the sapwood;is the viscosity of the sap.

<!-- b000641 | furniture | pages [23] -->
Team # 14297

<!-- b000642 | furniture | pages [23] -->


<!-- b000643 | furniture | pages [23] -->


<!-- b000644 | furniture | pages [23] -->
Page 23 of 45

<!-- b000645 | prose | pages [23] -->
Within each component, the flow resistance R was defined by rearrangement of (33)

<!-- b000646 | prose | pages [23] -->
as

<!-- b000647 | prose | pages [23] -->
  

<!-- b000648 | prose | pages [23] -->
R Q

<!-- b000649 | prose | pages [23] -->


<!-- b000650 | prose | pages [23] -->
l l

<!-- b000651 | prose | pages [23] -->
(34)

<!-- b000652 | prose | pages [23] -->
KA

<!-- b000653 | prose | pages [23] -->
In the absence of flow, water potential is directly related to the height of

<!-- b000654 | prose | pages [23] -->
measurement z above a reference level (taken to be ground level) through the effect of

<!-- b000655 | prose | pages [23] -->
gravity, as follows:

<!-- b000656 | prose | pages [23] -->
  z g (35)

<!-- b000657 | prose | pages [23] -->
where is the density of water and g the acceleration due to gravity.

<!-- b000658 | furniture | pages [23] -->


<!-- b000659 | heading | pages [23] -->
2.3 Model of leaf arrangement & branching structure

<!-- b000660 | heading | pages [23] -->
2.3.1 Leaf arrangement

<!-- b000661 | prose | pages [23] -->
The biological principle states that plant leaves are photosynthetic machines that

<!-- b000662 | prose | pages [23] -->
maximize the absorption of light. Thus to minimize overlapping individual shadows

<!-- b000663 | prose | pages [23] -->
and achieving the maximum exposure, leaves have evolved the optimal response to

<!-- b000664 | prose | pages [23] -->
mix of environmental elements. Among such evolutionary features, leaf shape and

<!-- b000665 | prose | pages [23] -->
phyllotaxy are two critical traits that affect the interactions between leaves. In this

<!-- b000666 | prose | pages [23] -->
section, inter-leaf relations are examined in terms of position arrangement on the stem.

<!-- b000667 | prose | pages [23] -->
And such arrangement determines the angle of the petioles.

<!-- b000668 | prose | pages [23] -->
Here we present two types of models applying to different dimensions. The 2-D

<!-- b000669 | prose | pages [23] -->
model assumes that sunlight is perpendicular to the ground surface, thus leaves at

<!-- b000670 | prose | pages [23] -->
different level spots can be projected to a 2-D plane (Figure 12). The model can be

<!-- b000671 | prose | pages [23] -->
extended to 3-D cases by adding the angle of incidence of sunlight.

<!-- b000672 | furniture | pages [24] -->
Team # 14297

<!-- b000673 | furniture | pages [24] -->


<!-- b000674 | furniture | pages [24] -->


<!-- b000675 | furniture | pages [24] -->
Page 24 of 45

<!-- b000676 | furniture | pages [24] -->


<!-- b000677 | caption | pages [24] -->
Figure12 Three Types of Leaf Arrangements Projected on a Plane

<!-- b000678 | heading | pages [24] -->
 Two-dimensional modeling

<!-- b000679 | prose | pages [24] -->
To simplify the computation of overlapping areas and add more comparability, we

<!-- b000680 | prose | pages [24] -->
standardize various shapes into their circumcircles with the equal-length radius, and

<!-- b000681 | prose | pages [24] -->
the overlapping area can be obtained by finding the intersection of two circles in plane

<!-- b000682 | prose | pages [24] -->
geometry (Figure 13).

<!-- b000683 | furniture | pages [24] -->


<!-- b000684 | caption | pages [24] -->
Figure 13 Standardized Overlapping Leaves

<!-- b000685 | prose | pages [24] -->
    OCA O CA We denote the radius of circles as r ; length of petiole as x ;

<!-- b000686 | prose | pages [24] -->
     AOO BOO O F m ;

<!-- b000687 | furniture | pages [24] -->


<!-- b000688 | prose | pages [24] -->
1 2 1 2 1

<!-- b000689 | prose | pages [24] -->
Area of intersection is written as

<!-- b000690 | prose | pages [24] -->
; 1 2

<!-- b000691 | furniture | pages [25] -->
Team # 14297

<!-- b000692 | prose | pages [25] -->
m

<!-- b000693 | prose | pages [25] -->
  

<!-- b000694 | prose | pages [25] -->
1 2

<!-- b000695 | prose | pages [25] -->
A

<!-- b000696 | prose | pages [25] -->
2cos ( )

<!-- b000697 | prose | pages [25] -->
r

<!-- b000698 | prose | pages [25] -->
shade

<!-- b000699 | prose | pages [25] -->
r

<!-- b000700 | prose | pages [25] -->
 where r is the radius of the circles;

<!-- b000701 | prose | pages [25] -->
m ( r

<!-- b000702 | furniture | pages [25] -->


<!-- b000703 | furniture | pages [25] -->


<!-- b000704 | furniture | pages [25] -->
Page 25 of 45

<!-- b000705 | prose | pages [25] -->


<!-- b000706 | prose | pages [25] -->
2 2

<!-- b000707 | prose | pages [25] -->
(36)

<!-- b000708 | prose | pages [25] -->
2 2

<!-- b000709 | prose | pages [25] -->
m r m

<!-- b000710 | prose | pages [25] -->
   . x )sin

<!-- b000711 | prose | pages [25] -->
The overlapping conditions are sorted into two general catalogs: convex-margin

<!-- b000712 | prose | pages [25] -->
leaves and concave-margin leaves. For leaves with convex, the overlapping area is

<!-- b000713 | prose | pages [25] -->
estimated by calculating the area of the shaded region, while for concave-margin

<!-- b000714 | prose | pages [25] -->
leaves, overlapping area is computed by adjusting the area in shadow with a ratio

<!-- b000715 | prose | pages [25] -->
 related to the included angle ( 2) of the two petioles (Table 1). ( )

<!-- b000716 | caption | pages [25] -->
Table 2: Computation of Overlapping Areas

<!-- b000717 | prose | pages [25] -->
Convex-margin Leaves

<!-- b000718 | furniture | pages [25] -->


<!-- b000719 | prose | pages [25] -->


<!-- b000720 | furniture | pages [25] -->


<!-- b000721 | prose | pages [25] -->
A A overlap shade

<!-- b000722 | prose | pages [25] -->
Concave-margin Leaves

<!-- b000723 | furniture | pages [25] -->


<!-- b000724 | prose | pages [25] -->
 

<!-- b000725 | furniture | pages [25] -->


<!-- b000726 | prose | pages [25] -->
A ( ) A overlap shade

<!-- b000727 | prose | pages [25] -->
The area exposed under sunlight can be derived as the difference between total size

<!-- b000728 | prose | pages [25] -->
of leaves and sum of the overlapping regions.

<!-- b000729 | prose | pages [25] -->
    A A A exposure i (37) overlap

<!-- b000730 | prose | pages [25] -->
where A is the size of a single piece of leaves.

<!-- b000731 | heading | pages [25] -->
 Three-dimensional modeling

<!-- b000732 | prose | pages [25] -->
In the 3-D model, the position of leaves in branch and tree volume will be

<!-- b000733 | prose | pages [25] -->
transferred into two indicators: height and angle.

<!-- b000734 | prose | pages [25] -->
Some assumptions embedded in the three-dimensional model of phyllotaxy are

<!-- b000735 | prose | pages [25] -->
listed below:

<!-- b000736 | prose | pages [25] -->
 Vertex (i.e. leaves at top-ends) is not considered

<!-- b000737 | prose | pages [25] -->
 The distance ( h ) between adjacent nodes is large enough.

<!-- b000738 | prose | pages [25] -->
 Number of leaves ( n ) is large enough.

<!-- b000739 | furniture | pages [26] -->
Team # 14297

<!-- b000740 | furniture | pages [26] -->


<!-- b000741 | furniture | pages [26] -->


<!-- b000742 | furniture | pages [26] -->
Page 26 of 45

<!-- b000743 | prose | pages [26] -->
Consider the height and interactions of leaves, and take the elliptic leaf as an

<!-- b000744 | prose | pages [26] -->
example, the overlapping area can be derived under different leaf arrangement

<!-- b000745 | prose | pages [26] -->
patterns. Assuming an anglebe the inclination of angle of direct solar beam. a andb

<!-- b000746 | prose | pages [26] -->
are the semiminor and semimajor axis of the elliptic leaf; s is the width of area

<!-- b000747 | prose | pages [26] -->
without shadow casted by the leaves above, and is denoted by the formula

<!-- b000748 | prose | pages [26] -->
  (38) s h cot

<!-- b000749 | prose | pages [26] -->
Observing the effect of leaf arrangement on the overlapping areas, situations for

<!-- b000750 | prose | pages [26] -->
alternate and opposite arrangements are quite similar, while the whorled arrangement

<!-- b000751 | prose | pages [26] -->
is taken as a special case if the last two assumptions are fulfilled (Table 2).

<!-- b000752 | caption | pages [26] -->
Table 3: Overlapping under Different Leaf Arrangements

<!-- b000753 | prose | pages [26] -->
Alternate

<!-- b000754 | prose | pages [26] -->
Opposite

<!-- b000755 | prose | pages [26] -->
Whorled

<!-- b000756 | furniture | pages [26] -->


<!-- b000757 | furniture | pages [26] -->


<!-- b000758 | prose | pages [26] -->
Overlapping areas for the three arrangements are formulated by

<!-- b000759 | prose | pages [26] -->
 

<!-- b000760 | prose | pages [26] -->
2 2 2

<!-- b000761 | prose | pages [26] -->
n s a

<!-- b000762 | prose | pages [26] -->
(

<!-- b000763 | prose | pages [26] -->
b

<!-- b000764 | prose | pages [26] -->
)

<!-- b000765 | prose | pages [26] -->
  A

<!-- b000766 | prose | pages [26] -->
alt 4

<!-- b000767 | prose | pages [26] -->
ab  (39) n ab

<!-- b000768 | furniture | pages [27] -->
Team # 14297

<!-- b000769 | prose | pages [27] -->


<!-- b000770 | prose | pages [27] -->
2

<!-- b000771 | prose | pages [27] -->
n s a    A n ab

<!-- b000772 | prose | pages [27] -->
opp 2

<!-- b000773 | prose | pages [27] -->
b

<!-- b000774 | prose | pages [27] -->
    A 2 s x ( r ) whr

<!-- b000775 | prose | pages [27] -->
A , A

<!-- b000776 | furniture | pages [27] -->


<!-- b000777 | furniture | pages [27] -->


<!-- b000778 | furniture | pages [27] -->
Page 27 of 45

<!-- b000779 | prose | pages [27] -->
(40)

<!-- b000780 | prose | pages [27] -->
 2 (41) s

<!-- b000781 | prose | pages [27] -->
denote the overlapping areas for alternate, opposite, and where , A alt whr opp

<!-- b000782 | prose | pages [27] -->
whorled arrangement, respectively.

<!-- b000783 | heading | pages [27] -->
2.3.2 Branching structure

<!-- b000784 | prose | pages [27] -->
In this subsection, we use the LA system model, which is one kind of rod-based

<!-- b000785 | prose | pages [27] -->
model to simulate the growth of branches. Development of branching structure is

<!-- b000786 | prose | pages [27] -->
largely influenced by various ecological factors, among which “wind can be an

<!-- b000787 | prose | pages [27] -->
important mortality factor to branch structure” as stated by Stiling (2002) in the book

<!-- b000788 | prose | pages [27] -->
Ecology.

<!-- b000789 | prose | pages [27] -->
The guiding principle of the model is to find the most stable cases by classical

<!-- b000790 | prose | pages [27] -->
mechanics. In the model constructing process, two critical elements are taken into

<!-- b000791 | prose | pages [27] -->
account, namely branch growth tendency and effective leaf area. Mostly, leaves area

<!-- b000792 | prose | pages [27] -->
is probably the variable that has the largest influence on branch structure in the

<!-- b000793 | prose | pages [27] -->
evolution history, since in the vegetation life span, branches and leaves develop

<!-- b000794 | prose | pages [27] -->
inter-dependently (Walter, 2001).

<!-- b000795 | prose | pages [27] -->
The list of assumptions for this model is provided:

<!-- b000796 | prose | pages [27] -->
 Branch structure will exist in the most stable case;

<!-- b000797 | prose | pages [27] -->
 Leaves in each branch are identical in size, and distributed uniformly;

<!-- b000798 | prose | pages [27] -->
 All branches are rigid;

<!-- b000799 | prose | pages [27] -->
 All the leaves are located at the end of branches.

<!-- b000800 | prose | pages [27] -->
Since the growth of a plant axis is subject to the external force oriented in the

<!-- b000801 | prose | pages [27] -->
direction of the preferred tendency of growth, we first develop the formula describing

<!-- b000802 | prose | pages [27] -->
force of wind by

<!-- b000803 | prose | pages [27] -->
  F wind Av (42)

<!-- b000804 | prose | pages [27] -->
where A is the effective area of leaves; v is the constant speed of wind.

<!-- b000805 | furniture | pages [28] -->
Team # 14297

<!-- b000806 | prose | pages [28] -->


<!-- b000807 | furniture | pages [28] -->


<!-- b000808 | furniture | pages [28] -->


<!-- b000809 | furniture | pages [28] -->
Page 28 of 45

<!-- b000810 | prose | pages [28] -->
is expressed as The torque of the wind force wind

<!-- b000811 | prose | pages [28] -->
    Av wind   l l cos( ) (43) i i

<!-- b000812 | prose | pages [28] -->
iis the angle between segments i and i-1. il is the length of segment i, and where

<!-- b000813 | furniture | pages [28] -->


<!-- b000814 | prose | pages [28] -->
The torque exerted by an individual spring is shown as

<!-- b000815 | prose | pages [28] -->
   k i i i x x x (44)

<!-- b000816 | prose | pages [28] -->
xiis the rotational displacement due to external

<!-- b000817 | prose | pages [28] -->
where

<!-- b000818 | prose | pages [28] -->
xik is the spring constant;

<!-- b000819 | prose | pages [28] -->
forces.

<!-- b000820 | prose | pages [28] -->
To maintain the stable, the two torque must be equal

<!-- b000821 | prose | pages [28] -->
   wind (45) i i x x

<!-- b000822 | prose | pages [28] -->
The rotational displacement can be obtained by solving (10)

<!-- b000823 | prose | pages [28] -->
1

<!-- b000824 | prose | pages [28] -->
   Av

<!-- b000825 | prose | pages [28] -->
i

<!-- b000826 | prose | pages [28] -->
k

<!-- b000827 | prose | pages [28] -->
x

<!-- b000828 | prose | pages [28] -->
i

<!-- b000829 | prose | pages [28] -->
x

<!-- b000830 | prose | pages [28] -->
  (46) l

<!-- b000831 | prose | pages [28] -->
cos( )

<!-- b000832 | prose | pages [28] -->
i

<!-- b000833 | prose | pages [28] -->
Each new layer that is added to a segment has a unique spring constant which can

<!-- b000834 | prose | pages [28] -->
be used to calculate the overall spring constant at that point. The spring constant about

<!-- b000835 | prose | pages [28] -->
the x-axis at joint i for an individual layer m is calculated by

<!-- b000836 | prose | pages [28] -->
E I

<!-- b000837 | prose | pages [28] -->
i

<!-- b000838 | prose | pages [28] -->


<!-- b000839 | prose | pages [28] -->
k

<!-- b000840 | prose | pages [28] -->
x

<!-- b000841 | prose | pages [28] -->
i

<!-- b000842 | prose | pages [28] -->
l

<!-- b000843 | prose | pages [28] -->
xm

<!-- b000844 | prose | pages [28] -->
i

<!-- b000845 | prose | pages [28] -->
 

<!-- b000846 | prose | pages [28] -->
i i

<!-- b000847 | prose | pages [28] -->
1 1

<!-- b000848 | prose | pages [28] -->
(47)

<!-- b000849 | prose | pages [28] -->
x

<!-- b000850 | prose | pages [28] -->
 

<!-- b000851 | prose | pages [28] -->
1 1

<!-- b000852 | prose | pages [28] -->
il is the length of xiE is the shear modulus of the material about the x-axis,

<!-- b000853 | prose | pages [28] -->
where

<!-- b000854 | prose | pages [28] -->
segment i-1 that rotates about joint i, and

<!-- b000855 | prose | pages [28] -->
about joint i.

<!-- b000856 | prose | pages [28] -->
1

<!-- b000857 | prose | pages [28] -->
iI is the torsional constant of the layer 1x

<!-- b000858 | prose | pages [28] -->
iI is We assume the new layer to be a hollow ring, and the torsional constant

<!-- b000859 | prose | pages [28] -->
calculated using the formula

<!-- b000860 | prose | pages [28] -->


<!-- b000861 | prose | pages [28] -->


<!-- b000862 | prose | pages [28] -->
I ( R

<!-- b000863 | prose | pages [28] -->


<!-- b000864 | prose | pages [28] -->
i 1 i 2 x

<!-- b000865 | prose | pages [28] -->
1x

<!-- b000866 | prose | pages [28] -->


<!-- b000867 | prose | pages [28] -->
4 4 4

<!-- b000868 | prose | pages [28] -->
(48)

<!-- b000869 | prose | pages [28] -->
r )

<!-- b000870 | prose | pages [28] -->
  

<!-- b000871 | prose | pages [28] -->
1 1 i 1

<!-- b000872 | prose | pages [28] -->
iR is the distance from the center of the cross-section to the outer edge of the where 1

<!-- b000873 | prose | pages [28] -->
ir  is the distance from the center of the cross-section to the inner edge of layer and 1

<!-- b000874 | furniture | pages [29] -->
Team # 14297

<!-- b000875 | prose | pages [29] -->
the layer.

<!-- b000876 | furniture | pages [29] -->


<!-- b000877 | furniture | pages [29] -->


<!-- b000878 | furniture | pages [29] -->
Page 29 of 45

<!-- b000879 | prose | pages [29] -->
We have obtained the computation results about the x axes. For y and z axes,

<!-- b000880 | prose | pages [29] -->


<!-- b000881 | prose | pages [29] -->


<!-- b000882 | prose | pages [29] -->
I ( R

<!-- b000883 | prose | pages [29] -->


<!-- b000884 | prose | pages [29] -->
i 1 i 4

<!-- b000885 | heading | pages [29] -->
2.4 Model of the tree characteristics

<!-- b000886 | prose | pages [29] -->


<!-- b000887 | prose | pages [29] -->
4 4 4

<!-- b000888 | prose | pages [29] -->
(49)

<!-- b000889 | prose | pages [29] -->
r )

<!-- b000890 | prose | pages [29] -->
  

<!-- b000891 | prose | pages [29] -->
1 1 i 1

<!-- b000892 | prose | pages [29] -->
Generally speaking, in the early stage, characteristics of a tree such as height,

<!-- b000893 | prose | pages [29] -->
volume and mass relate positively with the mass accumulation of leaves. As we know,

<!-- b000894 | prose | pages [29] -->
almost all structures of the tree, including leaves, stems, branches, and root, will

<!-- b000895 | prose | pages [29] -->
growth simultaneously, although at various growth rate. It is also possible for us to

<!-- b000896 | prose | pages [29] -->
find the inner link between them by the governing equations based on the vital

<!-- b000897 | prose | pages [29] -->
physiological activities mentioned in Section 2.2.

<!-- b000898 | prose | pages [29] -->
However, after the tree researches maturity, the observable relationship between the

<!-- b000899 | prose | pages [29] -->
size of the tree and leaf mass will fade way. This is because that the percentage of

<!-- b000900 | prose | pages [29] -->
dead cells in xylem will end up being the major part of the tree. The metabolic

<!-- b000901 | prose | pages [29] -->
activities will demonstrate seasonal pattern instead of strict positive correlations. And

<!-- b000902 | prose | pages [29] -->
the environmental factors will outweigh the inner traits of the plant and reshape some

<!-- b000903 | prose | pages [29] -->
of the biophysical features. Hence, out model is restricted to the early stage of trees.

<!-- b000904 | prose | pages [29] -->
Two distinct modeling approaches are addressed in this subsection: physiological

<!-- b000905 | prose | pages [29] -->
and structural. And we will demonstrate and evaluate both models respectively.

<!-- b000906 | prose | pages [29] -->
 Physiological Approach

<!-- b000907 | prose | pages [29] -->
We have talked about the energy conservation balance and the driving force

<!-- b000908 | prose | pages [29] -->
operation in Section 2.2. By applying the bio-mechanism of metabolic energy cycle

<!-- b000909 | prose | pages [29] -->
and inner force equilibrium, two governing equations can be obtained.

<!-- b000910 | prose | pages [29] -->
Assumptions adopted by this approach are:

<!-- b000911 | prose | pages [29] -->
(1) Photosynthesis is the only energy source for plant functioning.

<!-- b000912 | prose | pages [29] -->
(2) Transpiration mechanism is the only driving force generator for the active

<!-- b000913 | furniture | pages [30] -->
Team # 14297

<!-- b000914 | prose | pages [30] -->
transportation plant.

<!-- b000915 | furniture | pages [30] -->


<!-- b000916 | furniture | pages [30] -->


<!-- b000917 | furniture | pages [30] -->
Page 30 of 45

<!-- b000918 | prose | pages [30] -->
The energy transformation function is derived by describing the process of ATP

<!-- b000919 | prose | pages [30] -->
production and consumption. The left-hand-side represents the ATP produced by

<!-- b000920 | prose | pages [30] -->
photosynthesis; and the right-hand-side equation is the amount of energy consumer,

<!-- b000921 | prose | pages [30] -->
both are in Joule.

<!-- b000922 | prose | pages [30] -->
     nA P n Q   (50) f h

<!-- b000923 | prose | pages [30] -->
where n is the unit of ATP; P is the product of photosynthesis; A is the total

<!-- b000924 | prose | pages [30] -->
effective leaf area; Q indicates total flow in transpiration; f indicates total flow in

<!-- b000925 | prose | pages [30] -->
transportation; h is the height of the tree; is the amount of ATP consumed in other

<!-- b000926 | prose | pages [30] -->
activates; and , ,are constant coefficients.

<!-- b000927 | prose | pages [30] -->
The equilibrium condition reached by the driving force (i.e. transpiration can

<!-- b000928 | prose | pages [30] -->
provide sufficient driving force needed by the substance transport process) in the plant

<!-- b000929 | prose | pages [30] -->
system is presented by

<!-- b000930 | prose | pages [30] -->
   n ' Q ' f h

<!-- b000931 | prose | pages [30] -->
are constant coefficients. , where ' '

<!-- b000932 | prose | pages [30] -->
   (51) '

<!-- b000933 | prose | pages [30] -->
The height of tree ( h ) can be solved by solving the equation set (51) & (50).

<!-- b000934 | prose | pages [30] -->
However, this approach is almost impossible to carry out, since we may never

<!-- b000935 | prose | pages [30] -->
obtain the precise value of the coefficients in the equations and it is of great difficulty

<!-- b000936 | prose | pages [30] -->
to quantify the elements presented in the above equations.

<!-- b000937 | prose | pages [30] -->
 Structural Approach

<!-- b000938 | prose | pages [30] -->
 Tree Volume Estimation

<!-- b000939 | prose | pages [30] -->
To estimate the volume of the tree, we resemble the cone-shaped tree as round

<!-- b000940 | furniture | pages [31] -->
Team # 14297

<!-- b000941 | furniture | pages [31] -->


<!-- b000942 | furniture | pages [31] -->


<!-- b000943 | furniture | pages [31] -->
Page 31 of 45

<!-- b000944 | prose | pages [31] -->
platforms piling up. These platforms can be generated by rotating the branches around

<!-- b000945 | prose | pages [31] -->
the tree trunk, with the curved surface indicating the route of branch-top leaf piece

<!-- b000946 | prose | pages [31] -->
wiping through the air (Figure 1).

<!-- b000947 | prose | pages [31] -->
We then compute the volume of single platform by

<!-- b000948 | prose | pages [31] -->
  r  V T

<!-- b000949 | prose | pages [31] -->
(2

<!-- b000950 | prose | pages [31] -->
x

<!-- b000951 | prose | pages [31] -->
4 ) i

<!-- b000952 | prose | pages [31] -->
where r is the radius of leaves’ blade;

<!-- b000953 | prose | pages [31] -->
T

<!-- b000954 | prose | pages [31] -->
l equivalent length of the bottom branch (

<!-- b000955 | prose | pages [31] -->
branch and tree trunk.

<!-- b000956 | prose | pages [31] -->
 l l

<!-- b000957 | prose | pages [31] -->
2

<!-- b000958 | prose | pages [31] -->
iT (52) 

<!-- b000959 | prose | pages [31] -->
sin

<!-- b000960 | prose | pages [31] -->
  ; x is the length of petiole; l is the 2 r

<!-- b000961 | prose | pages [31] -->
  ); is the equivalent angle between the l 1

<!-- b000962 | furniture | pages [31] -->


<!-- b000963 | caption | pages [31] -->
Figure 14 Estimate Volume of the Tree by Round Platform

<!-- b000964 | prose | pages [31] -->
  The volume of the tree is thus the summation the platform volumes till

<!-- b000965 | furniture | pages [31] -->


<!-- b000966 | prose | pages [31] -->
l 2 iT 0

<!-- b000967 | prose | pages [31] -->
 V tree

<!-- b000968 | prose | pages [31] -->
 Tree Height Estimation

<!-- b000969 | prose | pages [31] -->
V (53) i

<!-- b000970 | furniture | pages [32] -->
Team # 14297

<!-- b000971 | furniture | pages [32] -->


<!-- b000972 | furniture | pages [32] -->


<!-- b000973 | furniture | pages [32] -->
Page 32 of 45

<!-- b000974 | prose | pages [32] -->
Illustrated in Figure 14, the height of a single platform can be expressed by

<!-- b000975 | prose | pages [32] -->
  ih 2 sin r

<!-- b000976 | prose | pages [32] -->
Therefore, height of a tree is obtained by

<!-- b000977 | prose | pages [32] -->
  H l cos tree

<!-- b000978 | prose | pages [32] -->
h where is the height of tree trunk. trunk

<!-- b000979 | prose | pages [32] -->
 Leaf mass Estimation

<!-- b000980 | prose | pages [32] -->
   T sin (54)

<!-- b000981 | prose | pages [32] -->
    h h (55) i trunk

<!-- b000982 | prose | pages [32] -->
In order to reach equilibrium, the function which represents gravity moment used

<!-- b000983 | prose | pages [32] -->
by Aaron & Karl (1988) express the mass function at bending moment by

<!-- b000984 | prose | pages [32] -->
  2 2  (56) d l Pg M bending  sin 2

<!-- b000985 | prose | pages [32] -->
where d is the diameter of branch’s cross section; l is the length of branch; P is

<!-- b000986 | prose | pages [32] -->
the mass of tissue; is the rotation angle; is the bifurcation angle.

<!-- b000987 | prose | pages [32] -->
The gravity function of mass is written as

<!-- b000988 | prose | pages [32] -->
2

<!-- b000989 | prose | pages [32] -->
l   M

<!-- b000990 | prose | pages [32] -->
cos( ) G 2

<!-- b000991 | prose | pages [32] -->
(57) M g

<!-- b000992 | prose | pages [32] -->
0

<!-- b000993 | prose | pages [32] -->
M is the mass of leaves on a single branch. where 0

<!-- b000994 | prose | pages [32] -->
The equal relation is then derived by applying the bending movement principle in

<!-- b000995 | prose | pages [32] -->
engineering

<!-- b000996 | prose | pages [32] -->
 M M bending (58) G G

<!-- b000997 | prose | pages [32] -->
By rearranging (9), we can obtain the mass of leaves on a single branch

<!-- b000998 | furniture | pages [33] -->
Team # 14297

<!-- b000999 | prose | pages [33] -->


<!-- b001000 | prose | pages [33] -->
2

<!-- b001001 | prose | pages [33] -->
2

<!-- b001002 | prose | pages [33] -->
d P

<!-- b001003 | prose | pages [33] -->


<!-- b001004 | prose | pages [33] -->
M

<!-- b001005 | prose | pages [33] -->
0

<!-- b001006 | prose | pages [33] -->


<!-- b001007 | prose | pages [33] -->
cos

<!-- b001008 | furniture | pages [33] -->


<!-- b001009 | furniture | pages [33] -->


<!-- b001010 | furniture | pages [33] -->
Page 33 of 45

<!-- b001011 | prose | pages [33] -->


<!-- b001012 | prose | pages [33] -->
sin 2

<!-- b001013 | prose | pages [33] -->
(59) 

<!-- b001014 | prose | pages [33] -->
The total mass of leaves for a tree is derived by

<!-- b001015 | prose | pages [33] -->
 M M N 0

<!-- b001016 | prose | pages [33] -->
N

<!-- b001017 | prose | pages [33] -->
(60) branch

<!-- b001018 | prose | pages [33] -->
is the number of branches of the tree, which can be where the max value of branch

<!-- b001019 | prose | pages [33] -->
represented by i in the estimation of tree volume.

<!-- b001020 | prose | pages [33] -->
max

<!-- b001021 | prose | pages [33] -->
N

<!-- b001022 | prose | pages [33] -->
branch

<!-- b001023 | furniture | pages [33] -->


<!-- b001024 | furniture | pages [33] -->


<!-- b001025 | prose | pages [33] -->
l   (61)

<!-- b001026 | prose | pages [33] -->
2

<!-- b001027 | prose | pages [33] -->
T

<!-- b001028 | furniture | pages [34] -->
Team # 14297

<!-- b001029 | furniture | pages [34] -->


<!-- b001030 | furniture | pages [34] -->
Page 34 of 45

<!-- b001031 | heading | pages [34] -->
Solutions and Results

<!-- b001032 | prose | pages [34] -->
In this section, we describe in detail how the problem can be solved by applying the

<!-- b001033 | prose | pages [34] -->
mathematical model built in the previous section. Since thorough descriptions have

<!-- b001034 | prose | pages [34] -->
been given on the modeling process and the biological or physiological interpretations

<!-- b001035 | prose | pages [34] -->
behind it, we will focus on testing how accurately the models can capture information

<!-- b001036 | prose | pages [34] -->
in practice.

<!-- b001037 | prose | pages [34] -->
Why do leaves have various shapes?

<!-- b001038 | prose | pages [34] -->
While previous literatures mostly take the development of leaf shapes as governed

<!-- b001039 | prose | pages [34] -->
by genetic elements or the result of structural optimization to environmental stress, in

<!-- b001040 | prose | pages [34] -->
this paper we drew more attention to the interaction between plant organs.

<!-- b001041 | prose | pages [34] -->
To answer this question, we examined the impact of cell growth and physiological

<!-- b001042 | prose | pages [34] -->
activities on the formation of the leaf’s blade area and its venation patterns. The

<!-- b001043 | prose | pages [34] -->
growth model simulates the leaf expansion process and proposed a positive

<!-- b001044 | prose | pages [34] -->
correlation between the size of blade area and cell-division margins. Physiological

<!-- b001045 | prose | pages [34] -->
activities discussed in Section 2.2.2 starts from a microscopic functioning of inner leaf

<!-- b001046 | prose | pages [34] -->
structures, showing evidence supporting the optimal selection of physiological

<!-- b001047 | prose | pages [34] -->
features and suggesting necessity of in-plant communications.

<!-- b001048 | prose | pages [34] -->
The evaluation of the models presented in Section 2.2 was conducted by running

<!-- b001049 | prose | pages [34] -->
regression analysis of variable correlations. Data were sourced from the university

<!-- b001050 | prose | pages [34] -->
biological department and ecology labs. Figure 1 and 2 show the regression results of

<!-- b001051 | prose | pages [34] -->
the Growth Model and the ATP determine function in Photosynthesis models. It is

<!-- b001052 | prose | pages [34] -->
observable that most data points fit quite well on the estimated function curves, which

<!-- b001053 | prose | pages [34] -->
suggests a satisfactory accuracy level of the model constructed.

<!-- b001054 | furniture | pages [35] -->
Team # 14297

<!-- b001055 | prose | pages [35] -->
0.05

<!-- b001056 | prose | pages [35] -->
0.04

<!-- b001057 | prose | pages [35] -->
0.03

<!-- b001058 | prose | pages [35] -->
kei

<!-- b001059 | prose | pages [35] -->
0.02

<!-- b001060 | prose | pages [35] -->
0.01

<!-- b001061 | prose | pages [35] -->
0.00 10 15

<!-- b001062 | furniture | pages [35] -->


<!-- b001063 | furniture | pages [35] -->


<!-- b001064 | furniture | pages [35] -->
Page 35 of 45

<!-- b001065 | prose | pages [35] -->
parameter

<!-- b001066 | prose | pages [35] -->
20 25 30 35

<!-- b001067 | prose | pages [35] -->
S (perimeter) (cm)

<!-- b001068 | furniture | pages [35] -->


<!-- b001069 | caption | pages [35] -->
Figure 15 Regression Results of the Growth Model

<!-- b001070 | prose | pages [35] -->
10000000

<!-- b001071 | prose | pages [35] -->
8000000

<!-- b001072 | prose | pages [35] -->
6000000

<!-- b001073 | prose | pages [35] -->
product (J)

<!-- b001074 | prose | pages [35] -->
4000000

<!-- b001075 | prose | pages [35] -->
2000000

<!-- b001076 | prose | pages [35] -->
0

<!-- b001077 | prose | pages [35] -->
0 20 40 60 80

<!-- b001078 | prose | pages [35] -->
ATP

<!-- b001079 | prose | pages [35] -->
100 120 140 160 180 200

<!-- b001080 | prose | pages [35] -->
time (min)

<!-- b001081 | furniture | pages [35] -->


<!-- b001082 | caption | pages [35] -->
Figure 16 Regression Result of Photosynthesis model

<!-- b001083 | prose | pages [35] -->
In order to test the transportation model, we applied the graph theory and the basic

<!-- b001084 | prose | pages [35] -->
data structure method to conduct algorithm on the dynamic positive feedback

<!-- b001085 | prose | pages [35] -->
networking (Mark Allen Weiss 1997). In this process, finite volume method was in

<!-- b001086 | prose | pages [35] -->
use to solve the time-dependent differential equation. The following picture

<!-- b001087 | prose | pages [35] -->
demonstrated results of our model. Graph comparison with field data, (Adrian D. Bell

<!-- b001088 | prose | pages [35] -->
1991) verified our model.

<!-- b001089 | furniture | pages [36] -->
Team # 14297

<!-- b001090 | furniture | pages [36] -->


<!-- b001091 | furniture | pages [36] -->


<!-- b001092 | furniture | pages [36] -->
Page 36 of 45

<!-- b001093 | furniture | pages [36] -->


<!-- b001094 | caption | pages [36] -->
Figure 17 Finite Volume Method

<!-- b001095 | prose | pages [36] -->
Do leaf shapes minimize overlapping so as to maximize exposure?

<!-- b001096 | prose | pages [36] -->
In Section 2.3, 2-D and 3-D models were constructed which linked the general shape

<!-- b001097 | prose | pages [36] -->
features with the size of overlapping regions. Our hypothesis stated that leaves

<!-- b001098 | prose | pages [36] -->
develop its shapes to optimize the utilization of sunlight. To test this hypothesis, we

<!-- b001099 | prose | pages [36] -->
compare computational output with experimental results.

<!-- b001100 | prose | pages [36] -->
Table 5

<!-- b001101 | heading | pages [36] -->
2-D Model

<!-- b001102 | prose | pages [36] -->
Input data Output data

<!-- b001103 | prose | pages [36] -->
Radius of a

<!-- b001104 | prose | pages [36] -->
5.00

<!-- b001105 | prose | pages [36] -->
leaf r(cm)

<!-- b001106 | prose | pages [36] -->
Length of

<!-- b001107 | prose | pages [36] -->
Calculated

<!-- b001108 | prose | pages [36] -->
1.20

<!-- b001109 | prose | pages [36] -->
petiole x(cm)

<!-- b001110 | prose | pages [36] -->
shadowed area

<!-- b001111 | prose | pages [36] -->
As(cm2)

<!-- b001112 | prose | pages [36] -->
Number of

<!-- b001113 | prose | pages [36] -->
leaves in a

<!-- b001114 | prose | pages [36] -->
8

<!-- b001115 | prose | pages [36] -->
circle

<!-- b001116 | furniture | pages [36] -->


<!-- b001117 | furniture | pages [36] -->


<!-- b001118 | prose | pages [36] -->
True value Error

<!-- b001119 | prose | pages [36] -->
True shadowed 51.00

<!-- b001120 | prose | pages [36] -->
47.22 6.93%

<!-- b001121 | prose | pages [36] -->
area As_ture(cm2)

<!-- b001122 | furniture | pages [37] -->
Team # 14297

<!-- b001123 | furniture | pages [37] -->


<!-- b001124 | furniture | pages [37] -->


<!-- b001125 | furniture | pages [37] -->
Page 37 of 45

<!-- b001126 | prose | pages [37] -->
Table 6

<!-- b001127 | heading | pages [37] -->
3-D Model for Opposite Arrangement

<!-- b001128 | prose | pages [37] -->
Output data Input data

<!-- b001129 | prose | pages [37] -->
Semi-major axis

<!-- b001130 | prose | pages [37] -->
of a ellipse leaf

<!-- b001131 | prose | pages [37] -->
4.60

<!-- b001132 | prose | pages [37] -->
a(cm)

<!-- b001133 | prose | pages [37] -->
Semi-minor axis

<!-- b001134 | prose | pages [37] -->
1.70

<!-- b001135 | prose | pages [37] -->
b(cm)

<!-- b001136 | prose | pages [37] -->
Distance between

<!-- b001137 | prose | pages [37] -->
Calculated

<!-- b001138 | prose | pages [37] -->
two levels of

<!-- b001139 | prose | pages [37] -->
2.00

<!-- b001140 | prose | pages [37] -->
shadowed area

<!-- b001141 | prose | pages [37] -->
As(cm2)

<!-- b001142 | prose | pages [37] -->
branches h(cm)

<!-- b001143 | prose | pages [37] -->
Light incident

<!-- b001144 | prose | pages [37] -->
π/3

<!-- b001145 | prose | pages [37] -->
angle ψ

<!-- b001146 | prose | pages [37] -->
Number of leaves

<!-- b001147 | prose | pages [37] -->
in the same height

<!-- b001148 | prose | pages [37] -->
20

<!-- b001149 | prose | pages [37] -->
of branch n

<!-- b001150 | furniture | pages [37] -->


<!-- b001151 | prose | pages [37] -->
True value Error

<!-- b001152 | prose | pages [37] -->
True shadowed

<!-- b001153 | prose | pages [37] -->
18.90

<!-- b001154 | prose | pages [37] -->
area

<!-- b001155 | prose | pages [37] -->
20.10 5.00%

<!-- b001156 | prose | pages [37] -->
As_ture(cm2)

<!-- b001157 | prose | pages [37] -->
Table 7

<!-- b001158 | heading | pages [37] -->
3-D Model for Alternative Arrangement

<!-- b001159 | prose | pages [37] -->
Input data Output data

<!-- b001160 | prose | pages [37] -->
Semi-major axis

<!-- b001161 | prose | pages [37] -->
of a ellipse leaf

<!-- b001162 | prose | pages [37] -->
4.60

<!-- b001163 | prose | pages [37] -->
a(cm)

<!-- b001164 | prose | pages [37] -->
Calculated

<!-- b001165 | prose | pages [37] -->
Semi-minor axis

<!-- b001166 | prose | pages [37] -->
1.70

<!-- b001167 | prose | pages [37] -->
shadowed area

<!-- b001168 | prose | pages [37] -->
b(cm)

<!-- b001169 | prose | pages [37] -->
per leaf

<!-- b001170 | prose | pages [37] -->
Distance

<!-- b001171 | prose | pages [37] -->
As(cm2)

<!-- b001172 | prose | pages [37] -->
between two

<!-- b001173 | prose | pages [37] -->
2.00

<!-- b001174 | prose | pages [37] -->
levels of

<!-- b001175 | prose | pages [37] -->
branches h(cm)

<!-- b001176 | prose | pages [37] -->
True value Error

<!-- b001177 | prose | pages [37] -->
True shadowed

<!-- b001178 | prose | pages [37] -->
19.80

<!-- b001179 | prose | pages [37] -->
area per leaf

<!-- b001180 | prose | pages [37] -->
18.37 7.19%

<!-- b001181 | prose | pages [37] -->
As_ture(cm2)

<!-- b001182 | furniture | pages [38] -->
Team # 14297

<!-- b001183 | prose | pages [38] -->
Light incident

<!-- b001184 | prose | pages [38] -->
π/3

<!-- b001185 | prose | pages [38] -->
angle ψ

<!-- b001186 | prose | pages [38] -->
Number of

<!-- b001187 | prose | pages [38] -->
leaves in the

<!-- b001188 | prose | pages [38] -->
20

<!-- b001189 | prose | pages [38] -->
same height of

<!-- b001190 | prose | pages [38] -->
branch n

<!-- b001191 | furniture | pages [38] -->


<!-- b001192 | furniture | pages [38] -->


<!-- b001193 | furniture | pages [38] -->


<!-- b001194 | furniture | pages [38] -->
Page 38 of 45

<!-- b001195 | prose | pages [38] -->
Table 8

<!-- b001196 | heading | pages [38] -->
3-D Model for Whorled Arrangement

<!-- b001197 | prose | pages [38] -->
Input data Output data

<!-- b001198 | prose | pages [38] -->
Radius of a leaf

<!-- b001199 | prose | pages [38] -->
4.60

<!-- b001200 | prose | pages [38] -->
r(cm)

<!-- b001201 | prose | pages [38] -->
Length of

<!-- b001202 | prose | pages [38] -->
2.00

<!-- b001203 | prose | pages [38] -->
Calculated

<!-- b001204 | prose | pages [38] -->
petiole x(cm)

<!-- b001205 | prose | pages [38] -->
shadowed area

<!-- b001206 | prose | pages [38] -->
Distance

<!-- b001207 | prose | pages [38] -->
As(cm2)

<!-- b001208 | prose | pages [38] -->
between two

<!-- b001209 | prose | pages [38] -->
1.2

<!-- b001210 | prose | pages [38] -->
levels of

<!-- b001211 | prose | pages [38] -->
branches h(cm)

<!-- b001212 | furniture | pages [38] -->


<!-- b001213 | prose | pages [38] -->
True value Error

<!-- b001214 | prose | pages [38] -->
True shadowed

<!-- b001215 | prose | pages [38] -->
27.00

<!-- b001216 | prose | pages [38] -->
area

<!-- b001217 | prose | pages [38] -->
28.34 4.72%

<!-- b001218 | prose | pages [38] -->
As_ture(cm2)

<!-- b001219 | prose | pages [38] -->
As can be seen from our result, the error between field data and the computational

<!-- b001220 | prose | pages [38] -->
result is less than 7.5%. Hence, our hypothesis that leaf shapes minimize overlapping

<!-- b001221 | prose | pages [38] -->
so as to maximize exposure was verified. To conclude, leaf shapes minimize

<!-- b001222 | prose | pages [38] -->
overlapping as to maximize exposure and this statement matched the biological

<!-- b001223 | prose | pages [38] -->
principle which is mentioned in the photosynthesis section.

<!-- b001224 | furniture | pages [38] -->


<!-- b001225 | prose | pages [38] -->
Speaking of profiles, is leaf shape (general characteristics related to tree

<!-- b001226 | prose | pages [38] -->
profile/branching structure?

<!-- b001227 | prose | pages [38] -->
As mentioned in Section 2.4, this model was constructed following principles of the

<!-- b001228 | prose | pages [38] -->
mechanic equilibrium system. The hypothesis of this model is that the effective area

<!-- b001229 | furniture | pages [39] -->
Team # 14297

<!-- b001230 | furniture | pages [39] -->


<!-- b001231 | furniture | pages [39] -->


<!-- b001232 | furniture | pages [39] -->
Page 39 of 45

<!-- b001233 | prose | pages [39] -->
of leaves would influence the branching structure.

<!-- b001234 | prose | pages [39] -->
Table 9

<!-- b001235 | prose | pages [39] -->
Tree Profile/Branching Structure under Wind Influence

<!-- b001236 | prose | pages [39] -->
Input data

<!-- b001237 | prose | pages [39] -->
Wind resistance coefficient α 0.10

<!-- b001238 | prose | pages [39] -->
Blade area of a branch facing

<!-- b001239 | prose | pages [39] -->
90.00

<!-- b001240 | prose | pages [39] -->
the wind A(cm2)

<!-- b001241 | prose | pages [39] -->
Wind speed(m/s) 3.00

<!-- b001242 | prose | pages [39] -->
Number of branches n 3

<!-- b001243 | prose | pages [39] -->
50

<!-- b001244 | prose | pages [39] -->
Length of each branch(cm)

<!-- b001245 | prose | pages [39] -->
20

<!-- b001246 | prose | pages [39] -->
10

<!-- b001247 | prose | pages [39] -->
0.6283

<!-- b001248 | prose | pages [39] -->
Measured angle(rad)

<!-- b001249 | prose | pages [39] -->
0.3927

<!-- b001250 | prose | pages [39] -->
0.3142

<!-- b001251 | prose | pages [39] -->
0.015

<!-- b001252 | prose | pages [39] -->
shear modulus(GPa)

<!-- b001253 | prose | pages [39] -->
0.024

<!-- b001254 | prose | pages [39] -->
0.034

<!-- b001255 | prose | pages [39] -->
0.25

<!-- b001256 | prose | pages [39] -->
Old segment branch

<!-- b001257 | prose | pages [39] -->
0.22

<!-- b001258 | prose | pages [39] -->
radius(cm)

<!-- b001259 | prose | pages [39] -->
0.20

<!-- b001260 | prose | pages [39] -->
0.15

<!-- b001261 | prose | pages [39] -->
New segment branch

<!-- b001262 | prose | pages [39] -->
0.12

<!-- b001263 | prose | pages [39] -->
radius(cm)

<!-- b001264 | prose | pages [39] -->
0.1

<!-- b001265 | furniture | pages [39] -->


<!-- b001266 | prose | pages [39] -->
Output data Error

<!-- b001267 | prose | pages [39] -->
Torque from wind on the

<!-- b001268 | prose | pages [39] -->
0.0068

<!-- b001269 | prose | pages [39] -->
branch(N﹒m)

<!-- b001270 | prose | pages [39] -->
6.53%

<!-- b001271 | prose | pages [39] -->
Torque from gravity on

<!-- b001272 | prose | pages [39] -->
0.0063

<!-- b001273 | prose | pages [39] -->
the branch(N﹒m)

<!-- b001274 | prose | pages [39] -->
As can be seen from the result, the error is less than 7.5%. Also, all the simulation

<!-- b001275 | prose | pages [39] -->
data was in right order of magnitude, which means our model is applicable.

<!-- b001276 | furniture | pages [39] -->


<!-- b001277 | furniture | pages [39] -->


<!-- b001278 | furniture | pages [40] -->
Team # 14297

<!-- b001279 | prose | pages [40] -->
Estimate the leaf mass of a tree

<!-- b001280 | furniture | pages [40] -->


<!-- b001281 | furniture | pages [40] -->


<!-- b001282 | furniture | pages [40] -->
Page 40 of 45

<!-- b001283 | prose | pages [40] -->
Two methods were presented to solve this problem. Theoretically speaking, the first

<!-- b001284 | prose | pages [40] -->
approach should be able to give consideration to sufficient biochemistry and

<!-- b001285 | prose | pages [40] -->
metabolic activities.

<!-- b001286 | prose | pages [40] -->
Was it highly comparable, experimental conditions would be in good control and

<!-- b001287 | prose | pages [40] -->
minimize both systematic and operational error. However, according to the

<!-- b001288 | prose | pages [40] -->
experimental results so far, most results were inconsistent and had large variation.

<!-- b001289 | prose | pages [40] -->
Hence, at this stage, we could not use those data to test our model. Although, with the

<!-- b001290 | prose | pages [40] -->
development of new biological technology, the result will be much more consistent

<!-- b001291 | prose | pages [40] -->
and comparable in order to better serve the modeling procedures (Heldt, 2011).

<!-- b001292 | prose | pages [40] -->
2) The second approach is obtained from the physical and structural properties to

<!-- b001293 | prose | pages [40] -->
estimate the total leaf mass. From Section 2.4, we could see that it ended with a

<!-- b001294 | prose | pages [40] -->
logical solution to the problem.

<!-- b001295 | prose | pages [40] -->
Table 11

<!-- b001296 | prose | pages [40] -->
Crown Volume and Mass Estimation

<!-- b001297 | prose | pages [40] -->
Output data Input data

<!-- b001298 | prose | pages [40] -->
Radius of a

<!-- b001299 | prose | pages [40] -->
3.50

<!-- b001300 | prose | pages [40] -->
circle leaf r(cm)

<!-- b001301 | prose | pages [40] -->
Length of

<!-- b001302 | prose | pages [40] -->
2.00

<!-- b001303 | prose | pages [40] -->
petiole x(cm)

<!-- b001304 | prose | pages [40] -->
Maximum level

<!-- b001305 | prose | pages [40] -->
10

<!-- b001306 | prose | pages [40] -->
of the crown

<!-- b001307 | prose | pages [40] -->
True value Error

<!-- b001308 | prose | pages [40] -->
True

<!-- b001309 | prose | pages [40] -->
volume

<!-- b001310 | prose | pages [40] -->
Calculated volume

<!-- b001311 | prose | pages [40] -->
Equivalent

<!-- b001312 | prose | pages [40] -->
0.0857

<!-- b001313 | prose | pages [40] -->
of the

<!-- b001314 | prose | pages [40] -->
0.8021 7.12%

<!-- b001315 | prose | pages [40] -->
of the crown(m3)

<!-- b001316 | prose | pages [40] -->
angle between

<!-- b001317 | prose | pages [40] -->
1.34

<!-- b001318 | prose | pages [40] -->
branch and

<!-- b001319 | prose | pages [40] -->
trunk

<!-- b001320 | prose | pages [40] -->
Number of

<!-- b001321 | prose | pages [40] -->
leaves in the

<!-- b001322 | prose | pages [40] -->
20

<!-- b001323 | prose | pages [40] -->
same height of

<!-- b001324 | prose | pages [40] -->
crown

<!-- b001325 | prose | pages [40] -->
(m3)

<!-- b001326 | furniture | pages [41] -->
Team # 14297

<!-- b001327 | prose | pages [41] -->
branch n

<!-- b001328 | prose | pages [41] -->
Diameter of the

<!-- b001329 | prose | pages [41] -->
cross section of

<!-- b001330 | prose | pages [41] -->
0.80

<!-- b001331 | prose | pages [41] -->
a branch d(cm)

<!-- b001332 | furniture | pages [41] -->


<!-- b001333 | furniture | pages [41] -->


<!-- b001334 | furniture | pages [41] -->


<!-- b001335 | furniture | pages [41] -->
Page 41 of 45

<!-- b001336 | prose | pages [41] -->
Calculated total

<!-- b001337 | prose | pages [41] -->
mass of the

<!-- b001338 | prose | pages [41] -->
Equivalent

<!-- b001339 | prose | pages [41] -->
crown(kg)

<!-- b001340 | prose | pages [41] -->
length of the

<!-- b001341 | prose | pages [41] -->
branch in the

<!-- b001342 | prose | pages [41] -->
0.8768

<!-- b001343 | prose | pages [41] -->
Lowest level

<!-- b001344 | prose | pages [41] -->
l(1)(m)

<!-- b001345 | prose | pages [41] -->
Coefficient of

<!-- b001346 | prose | pages [41] -->
equivalent

<!-- b001347 | prose | pages [41] -->
length of the

<!-- b001348 | prose | pages [41] -->
0.90

<!-- b001349 | prose | pages [41] -->
branch form

<!-- b001350 | prose | pages [41] -->
41.5178

<!-- b001351 | furniture | pages [41] -->


<!-- b001352 | furniture | pages [41] -->


<!-- b001353 | prose | pages [41] -->
Calculated average

<!-- b001354 | prose | pages [41] -->
bottom to top c

<!-- b001355 | prose | pages [41] -->
density of the

<!-- b001356 | prose | pages [41] -->
Density of 0.593

<!-- b001357 | furniture | pages [41] -->


<!-- b001358 | furniture | pages [41] -->


<!-- b001359 | prose | pages [41] -->
treeρ’(×103kg/m3)

<!-- b001360 | prose | pages [41] -->
wood

<!-- b001361 | prose | pages [41] -->
0.90

<!-- b001362 | prose | pages [41] -->
ρ(×103kg/m3)

<!-- b001363 | prose | pages [41] -->
Acceleration of

<!-- b001364 | prose | pages [41] -->
9.80

<!-- b001365 | prose | pages [41] -->
gravity

<!-- b001366 | furniture | pages [41] -->


<!-- b001367 | prose | pages [41] -->
As can be seen from the above data, the error is less than 7.5%, which provided

<!-- b001368 | prose | pages [41] -->
sufficient evidence to verify our estimation method.

<!-- b001369 | furniture | pages [41] -->


<!-- b001370 | furniture | pages [41] -->


<!-- b001371 | furniture | pages [42] -->
Team # 14297

<!-- b001372 | furniture | pages [42] -->


<!-- b001373 | furniture | pages [42] -->
Page 42 of 45

<!-- b001374 | heading | pages [42] -->
Discussion

<!-- b001375 | prose | pages [42] -->
In this section, strengths and limitations of models constructed are discussed. In

<!-- b001376 | prose | pages [42] -->
Section 2.1, shape functions are derived to quantify the distinctions between the

<!-- b001377 | prose | pages [42] -->
representative leaves. These functions allow us to better control the properties of leaf

<!-- b001378 | prose | pages [42] -->
shapes by applying traits parameters (e.g. blade area, cell-division margin) in the

<!-- b001379 | prose | pages [42] -->
evaluation of bio-functions. However, it is still questionable how accurately these

<!-- b001380 | prose | pages [42] -->
parameters can capture the structural and functional variations at organ levels. In the

<!-- b001381 | prose | pages [42] -->
section followed, a series of mathematical models are derived to simulate the leaf

<!-- b001382 | prose | pages [42] -->
expansion and three kinds of physiological activities in leaves. The photosynthesis

<!-- b001383 | prose | pages [42] -->
model provides complete description about the process of sunlight harvesting and

<!-- b001384 | prose | pages [42] -->
carbon dioxide assimilation. As for the transportation model, advanced algorithm are

<!-- b001385 | prose | pages [42] -->
employed for precisely control the complex dynamic procedures and the analysis is

<!-- b001386 | prose | pages [42] -->
highly comparable with other system of metabolic activities at the level of leaves.

<!-- b001387 | prose | pages [42] -->
Section 2.3 is where we start to extend the model to inter-organ relations and

<!-- b001388 | prose | pages [42] -->
communications. To solve the overlapping puzzle, solid and plane geometry are

<!-- b001389 | prose | pages [42] -->
adopted to find the intersection area of circles, which largely simplify the problem

<!-- b001390 | prose | pages [42] -->
solving procedures without losing the basic biological intuition. The branch structure

<!-- b001391 | prose | pages [42] -->
model considers both mechanical properties and the dynamic process of branch

<!-- b001392 | prose | pages [42] -->
development. It builds connections with vital environmental factors (e.g. wind force)

<!-- b001393 | prose | pages [42] -->
and further expands the model by catering for the inter-organ relationships. The

<!-- b001394 | prose | pages [42] -->
models addressed in Section 2.4 develop a comparison between the physiological and

<!-- b001395 | prose | pages [42] -->
structural approach in performing leaf mass estimations. Logical reasoning is derived

<!-- b001396 | prose | pages [42] -->
in the way that associates the tree characteristics with leaf properties.

<!-- b001397 | prose | pages [42] -->
Since our work in this paper majorly focus on the bio-functioning and

<!-- b001398 | prose | pages [42] -->
communications within an ideal and isolated case, the consistency of results can be

<!-- b001399 | prose | pages [42] -->
easily destroyed when encountering external shocks. Elements from eco-system could

<!-- b001400 | prose | pages [42] -->
be taken into account if further work was carried out. These elements involve both the

<!-- b001401 | prose | pages [42] -->
physical factors (e.g. sunlight, water, longitude) and inter-species relations (e.g.

<!-- b001402 | prose | pages [42] -->
competition, pray). In such way, we could provide more accurate and comprehensive

<!-- b001403 | furniture | pages [43] -->
Team # 14297

<!-- b001404 | furniture | pages [43] -->


<!-- b001405 | furniture | pages [43] -->
Page 43 of 45

<!-- b001406 | prose | pages [43] -->
model in the future.

<!-- b001407 | furniture | pages [43] -->


<!-- b001408 | furniture | pages [43] -->


<!-- b001409 | furniture | pages [43] -->


<!-- b001410 | furniture | pages [43] -->


<!-- b001411 | furniture | pages [44] -->
Team # 14297

<!-- b001412 | furniture | pages [44] -->


<!-- b001413 | furniture | pages [44] -->
Page 44 of 45

<!-- b001414 | heading | pages [44] -->
References

<!-- b001415 | heading | pages [44] -->
1. Howell, S.H. (1998). Molecular genetics of plant development Cambridge; New

<!-- b001416 | prose | pages [44] -->
York: Cambridge University Press.

<!-- b001417 | heading | pages [44] -->
2. Hemsley, A.R. & Poole, I. (2004). The evolution of plant physiology : from whole

<!-- b001418 | prose | pages [44] -->
plants to ecosystems Amsterdam; Boston: Published for the Linnean Society of

<!-- b001419 | prose | pages [44] -->
London by Elsevier Academic Press

<!-- b001420 | heading | pages [44] -->
3. Stern, K.R., Bidlack, J.E., & Jansky, S.H. (2008). Introductory plant biology

<!-- b001421 | prose | pages [44] -->
Boston : McGraw-Hill Higher Education

<!-- b001422 | heading | pages [44] -->
4. Greig-Smith, P. (1983). Quantitative plant ecology BLACKWELL SCIENTIFIC

<!-- b001423 | prose | pages [44] -->
PUBLICATIONS, OXFORD (UK).

<!-- b001424 | heading | pages [44] -->
5. Dickison, William C et al (2000) integrative plant anatomy published in Academic

<!-- b001425 | prose | pages [44] -->
Press

<!-- b001426 | prose | pages [44] -->
6. Adrian D. Bell & Alan Bryan(1991). Plant Form: an illustrated guide to flowering

<!-- b001427 | prose | pages [44] -->
plant morphology; Oxford (UK);

<!-- b001428 | prose | pages [44] -->
7. Van Volkengurgh, (1999) leaf expansion—an integrating plant behavior plant cell

<!-- b001429 | prose | pages [44] -->
and environment publication

<!-- b001430 | prose | pages [44] -->
8. J. I. Lizaso, W. D Batchelor, M.E Westgate (2002) A leaf area model to simulate

<!-- b001431 | prose | pages [44] -->
cultivar-specific expansion and senescence of maize leaves published in Field

<!-- b001432 | prose | pages [44] -->
Crop Research

<!-- b001433 | prose | pages [44] -->
9. William G. & Norman P.A H (2008) introduction to Plant Physiology  published

<!-- b001434 | prose | pages [44] -->
in University of Western Ontario

<!-- b001435 | prose | pages [44] -->
10. Christopher J. Kucharik, John M Norman, Stith T. GoWer (1998) Measurement of

<!-- b001436 | prose | pages [44] -->
branch area and adjusting leaf area index indirect measurements published in

<!-- b001437 | prose | pages [44] -->
Agricultural And Forest Meteorology

<!-- b001438 | heading | pages [44] -->
11. Marcelo Shoey de O M, Carlos Eduardo N C, Affonso G G & Helion Vargas

<!-- b001439 | prose | pages [44] -->
(2001) A simple model for the dynamics of photosynthesis published in Analytical

<!-- b001440 | prose | pages [44] -->
Sciences

<!-- b001441 | heading | pages [44] -->
12. Falkovich & Gregory  (2011) Fluid mechanics: a short course for physicists

<!-- b001442 | prose | pages [44] -->
published in Cambridge ; New York : Cambridge University Press

<!-- b001443 | furniture | pages [45] -->
Team # 14297

<!-- b001444 | furniture | pages [45] -->


<!-- b001445 | furniture | pages [45] -->
Page 45 of 45

<!-- b001446 | prose | pages [45] -->
13. Hironori Fujita and Atsushi Mochizuki (2006) The origin of the diversity of

<!-- b001447 | prose | pages [45] -->
leave venation pattern published in Developmental Dynamics

<!-- b001448 | prose | pages [45] -->
14. W R N. Edenwards, P.G.Jarvis, J.J. Landscerg and H. Talbot (1986) A dynamic

<!-- b001449 | prose | pages [45] -->
model for studying flow of studying of water in single trees published in Tree

<!-- b001450 | prose | pages [45] -->
Physiology

<!-- b001451 | prose | pages [45] -->
15.  Peter Stiling (2001) ecology theories and applications published in University of

<!-- b001452 | prose | pages [45] -->
South Florida

<!-- b001453 | prose | pages [45] -->
16. M.N.V Prasad (1996) plant ecophysiology published in New York

<!-- b001454 | prose | pages [45] -->
17. Walter Larcher (2003) physiology plant ecology – ecophysiology and stress

<!-- b001455 | prose | pages [45] -->
physiology of functional groups published in Springer

<!-- b001456 | prose | pages [45] -->
18. Aaron M.E& Karl J N (1988)Branching patterns of salicornia europaea

<!-- b001457 | prose | pages [45] -->
(chenopodiaceae)at different successional stages: a comparison of theoretical and

<!-- b001458 | prose | pages [45] -->
real plants published in American Journal Botany

<!-- b001459 | prose | pages [45] -->
19.  Michael Hickey and Clive King (1997) common families of flowering plants

<!-- b001460 | prose | pages [45] -->
published in Cambridge Press

<!-- b001461 | prose | pages [45] -->
20. Heldt, Hans-Walter (2011): plant biochemistry published in University of

<!-- b001462 | prose | pages [45] -->
Amsterdan

<!-- b001463 | prose | pages [45] -->
21. Harold C Bold (1973) Morphology of plants published in Harper International

<!-- b001464 | prose | pages [45] -->
Edition

<!-- b001465 | prose | pages [45] -->
22. Frank R. G, William P. F, Steven B H, Maurice D W (2009) A first course in

<!-- b001466 | prose | pages [45] -->
mathematical modeling published in China Machine Press

<!-- b001467 | prose | pages [45] -->
23. Mark Allen Wesis (1997) Data structures and Algorithm Analysis in C published

<!-- b001468 | prose | pages [45] -->
in Addison Wesley Longman

<!-- b001469 | prose | pages [45] -->
24. Daniel P, George C.T & Ruey S T (2001)A course in time series analysis

<!-- b001470 | prose | pages [45] -->
published in a wiley-interscience
