# P-A-2012-14297-5cb8073e

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team # 14297

<!-- b000002 | furniture | pages [1] -->
Page 1 of 45

<!-- b000003 | heading | pages [1] -->
Summary

<!-- b000004 | prose | pages [1] -->
Leaf shape plasticity has long been a heated topic in the field of morphology and taxonomy. Although numerous researchers have been involved in the study of how the shape formation is controlled by genes and environmental stress, little has been done to address the interactions between different plant organs. In this paper, we approach this issue in a creative way: starting from isolated parts (leaves), building connections (leaf-leaf, leaf-branch) and drawing the big picture of the entire system (tree).

<!-- b000005 | prose | pages [1] -->
The mathematical model introduced in this paper describes morphological, physiological and partially ecological properties of the vegetations. First and foremost, relative errors of the numerical outputs are limited within 7.5% and all the values predicted are within the right order of magnitude. Moreover, biological intuition is presented in the consistent manner. For instance, the dynamic positive feedback is applied to describe leaf growth pattern and transportation process. It is also worth noticing that a much simple and flexible algorithm is achieved by executing ingenious geometric strategy.

<!-- b000006 | prose | pages [1] -->
Interestingly findings were generated in the procedures of solving the problems. The seemly unrelated bio-phenomena could be explained when morphological, physiological and partially ecological interactions were taken into account. To illustrate, as we conducted the leaf mass estimation, it could give us a rough picture of leaf-leaf, leaf-branch, and leaf-tree relations.

<!-- b000007 | furniture | pages [2] -->
Team # 14297

<!-- b000008 | furniture | pages [2] -->
Page 2 of 45

<!-- b000009 | prose | pages [2] -->
Dear editor,

<!-- b000010 | prose | pages [2] -->
The topic of this paper is about mathematical modeling of tree leaves as well as how

<!-- b000011 | prose | pages [2] -->
leaf traits impose influence on the tree system.

<!-- b000012 | prose | pages [2] -->
In this paper, we addressed the morphological, physiological and partially ecological

<!-- b000013 | prose | pages [2] -->
properties of the vegetations by applying a series of modeling process to related issues.

<!-- b000014 | prose | pages [2] -->
The performance of our model in the sensitivity test satisfied our expectation.

<!-- b000015 | prose | pages [2] -->
Different from the previous research, we approached this issue in a creative way:

<!-- b000016 | prose | pages [2] -->
starting from isolated parts (leaves), building connections (leaf-leaf, leaf-branch) and

<!-- b000017 | prose | pages [2] -->
drawing the big picture of the entire system (tree).

<!-- b000018 | prose | pages [2] -->
Interestingly, the seemly unrelated bio-phenomena could be explained when

<!-- b000019 | prose | pages [2] -->
morphological, physiological and partially ecological interactions were taken into

<!-- b000020 | prose | pages [2] -->
account. Properties of the individual leaves are closely related to the characteristics of

<!-- b000021 | prose | pages [2] -->
the entire tree system.

<!-- b000022 | prose | pages [2] -->
We are looking forward to your comments and revision. Hopefully, our paper could be

<!-- b000023 | prose | pages [2] -->
published in this Journal.

<!-- b000024 | prose | pages [2] -->
Your sincerely

<!-- b000025 | furniture | pages [3] -->
Team # 14297

<!-- b000026 | furniture | pages [3] -->
Page 3 of 45

<!-- b000027 | heading | pages [3] -->
Introduction

<!-- b000028 | prose | pages [3] -->
The mechanism of plant shape plasticity has long been a topic of numerous researches in the field of morphometrics. And leaves have been always favored as the subject because of its two-dimensionality and relative simplicity. The change of leaf shapes are generally regarded as both a genetically determination (Howell, 1998) and results of structural optimization to environmental stress (Hemsley and Poole, 2004). However, little attention is drawn to the interactions between different plant organs (e.g. leaf, branch) and the influence from the system as an entity. To fill this gap, we construct a mathematical model to interpret such in-leaf communications, and perform our analysis on simple leaves.

<!-- b000029 | prose | pages [3] -->
As is shown in some literatures (Stern et al., 2008), simple leaves are classified into different shape catalogs (Figure 1), such as flabellate leaves (e.g. ginkgo), palmate leaves (e.g. maple), and cordate leaves (e.g. Hibiscus tiliaceus). The major criteria of classification are the shape apex, base, and margin of leaves.

<!-- b000030 | caption | pages [3] -->
Figure 1 Shape of Leaves

<!-- b000031 | prose | pages [3, 4] -->
Leaf venation is also a critical component of leaf types. There are three major patterns of major vein organization: pinnate, palmate, and parallel, as are shown in Besides the diversification in leaf shapes and venation, arrangement of leaves on a stem (phyllotaxy) are generally in three distinct patterns (Figure 3), which are defined by the number of leaves attached to a single node. In most species, leaves are attached alternately or in a spiral along a stem, with one leaf per node. This is called an alternate arrangement. If two leaves are attached at each node, they provide an opposite arrangement. Leaves are whorled when three or more occur at a node. A special case in opposite arrangement is called decussate, if successive pairs are orientated at 90o to each other.

<!-- b000032 | caption | pages [3] -->
Figure 2.

<!-- b000033 | furniture | pages [4] -->
Team # 14297

<!-- b000034 | furniture | pages [4] -->
Page 4 of 45

<!-- b000035 | caption | pages [4] -->
Figure 2 Leaf Venation

<!-- b000037 | caption | pages [4] -->
Figure 3 Leaf Arrangement

<!-- b000038 | prose | pages [4, 5] -->
Review of previous researches shows that most models developed are based on statistical results (Greig-Smith, 1983). And so far, no model is built to indicate the effect of plant organ interactions (leaf-leaf, leaf-branch) on leaf shapes. The mathematical model presented by us demonstrates the logic of plant-environment and in-plant communications at physiology, inter-organ, and tree system levels. We first start from isolated parts (leaves), build connections (leaf-leaf, leaf-branch) and end with the big picture of the entire system (tree).

<!-- b000039 | furniture | pages [5] -->
Team # 14297

<!-- b000040 | furniture | pages [5] -->
Page 5 of 45

<!-- b000042 | prose | pages [5] -->
Problem A requires mathematical modeling of tree leaves as well as how leaf traits impose influence on the tree system. It is suggested that shape factor of individual leaves to be analyzed via the following aspects.  Influencing elements of leaf shapes;  Inter-leaf relations (i.e. overlapping between leaves)  Branch-leaf relations  Tree-leaf relations (i.e. estimating mass of leaves) The model used should be able to capture not only the characteristics of single leaves but also their interactions with other plant organs and eventually the tree system. We have to start from isolated parts (leaves), build connections (leaf-leaf, leaf-branch) and end with the big picture of the entire system (tree).

<!-- b000043 | prose | pages [5] -->
We divide the modeling section into four subsections.  Section 2.1: Descriptive model of leaf traits;  Section 2.2: Model of cell growth & physiological activities;

<!-- b000044 | prose | pages [5] -->
(photosynthesis, transportation, transpiration)  Section 2.3: Model of leaf arrangement & branching structure;  Section 2.4: Model of the tree characteristics.

<!-- b000045 | prose | pages [5] -->
(ATP governing equation, Driving Force governing equation) The first two subsections of modeling are for analysis at leaf level. To quantify the geometric characteristics of various leaves, shapes are described by functions and curves are placed in Polar Coordinates, so that differences can be visualized. Parameter selection can then easily adjust the leaf shapes, thus providing more flexibility in deriving the bio-features such as size and perimeter. As for the shape influencing factors, processes of growth and photosynthesis are assumed to determine the effective blade area of leaves, while plant transport system and transpiration are closely related with leaf venation. These physiological activities are modeled in Section 2.2.

<!-- b000046 | furniture | pages [6] -->
Team # 14297

<!-- b000047 | furniture | pages [6] -->
Page 6 of 45

<!-- b000048 | prose | pages [6] -->
At the branch level in Section2.3, arrangements of leaves and branches are taken into account. We compute the overlapping area of leaves via geometric analysis. Since finding the area of irregular shadow region is troublesome and not easily compared, we standardized the computation by using round circles as equivalents to diverse leaf shapes. The angle over the two opposite leaf-edges is taken as indicators for leaf types. Tree profile is modeled by rod-based method (LA system). In Section2.4,by solving the two governing equations for ATP and driving force, tree height and angles of shoot can be derived, which will be then applied to compute the volume of the tree. Eventually, traits of isolated leaves and the tree are linked together.

<!-- b000049 | furniture | pages [7] -->
Team # 14297

<!-- b000050 | furniture | pages [7] -->
Page 7 of 45

<!-- b000051 | heading | pages [7] -->
The Models

<!-- b000052 | heading | pages [7] -->
2.1 Descriptive Model of Leaf Shape

<!-- b000053 | prose | pages [7] -->
In Section 2.1 we present several kinds of leaf shapes to describe some mostly-seen single leaves. Although shapes of tree leaves can be in great variety, the classification discussed here only applies to selected types of single leaves, which are flattened, colored in green, and spinelike, regardless of textures. Leaves that are tubular, feathery, cup-shaped, or needlelike require 3-dimensional models and are not taken into account for simplicity purpose. In Table 2.1, some of the typical plant and their leaf shapes are listed before we transform their morphological features into the language of mathematics.

<!-- b000054 | caption | pages [7] -->
Table 1 Representative Plant with Various Leaf Types

<!-- b000055 | prose | pages [7, 8] -->
Type of Leaf Representative Plant Shapes Nasturtium Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Orbicular Class: Magnoliopsida – Dicotyledons Order: Geraniales Family: Tropaeolaceae – Nasturtium family Genus: Tropaeolum L. – nasturtium Eastern redbud Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Cordate Order: Fabales Family: Fabaceae – Pea family Genus: Cercis L. – redbud Species: Cercis canadensis L. – eastern redbud Spadeleaf Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Reniform Order: Apiales Family: Apiaceae – Carrot family Genus: Centella L. – centella Species: Centella asiatica (L.) Urb. – spadeleaf Cassava Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Lobed Order: Euphorbiales Family: Euphorbiaceae – Spurge family Genus: Manihot Mill. – cassava Species: Manihot esculenta Crantz – cassava Wine Grape Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Palmate Order: Rhamnales Family: Vitaceae – Grape family Genus: Vitis L. – grape Species: Vitis vinifera L. – wine grape Tea Kingdom : Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Elliptic Order: Theales Family: Theaceae – Tea family Genus: Camellia L. – camellia Species: Camellia sinensis (L.) Kuntze – tea Maidenhair Tree Kingdom: Plantae – Plants Division: Ginkgophyta – Ginkgo Class: Ginkgoopsida Flabellate Order: Ginkgoales Family: Ginkgoaceae – Ginkgo family Genus: Ginkgo L. – ginkgo Species: Ginkgo biloba L. – maidenhair tree

<!-- b000056 | furniture | pages [8] -->
Team # 14297

<!-- b000057 | furniture | pages [8] -->
Page 8 of 45

<!-- b000059 | prose | pages [8] -->
These leaf shape types are described by functions with adjustable parameters.

<!-- b000060 | prose | pages [8] -->
Plotting their curve functions with specific coefficients in Polar Coordinates, we can

<!-- b000061 | prose | pages [8] -->
visualize differences between shapes. To quantify such differences, we derive the

<!-- b000062 | prose | pages [8] -->
expression of leaf area A as well as length of leaf margins S , by finding the following

<!-- b000063 | prose | pages [8] -->
integrals.

<!-- b000064 | prose | pages [8] -->
 rdrd A

<!-- b000065 | prose | pages [8, 9] -->
 rd S It should be noted that S refers to the part of leaf margin where cell division

<!-- b000066 | furniture | pages [9] -->
Team # 14297

<!-- b000067 | furniture | pages [9] -->
Page 9 of 45

<!-- b000069 | prose | pages [9] -->
occurs, rather than the perimeter of the blade. In Figure 1 to 6, this portion is

<!-- b000070 | prose | pages [9] -->
illustrated by the black edge of the shape curves, and the red nod at the origin denotes

<!-- b000071 | prose | pages [9] -->
the auxin sink of the leaf.

<!-- b000072 | prose | pages [9] -->
 Type 1: Orbicular leaves

<!-- b000073 | prose | pages [9] -->
Shape of an orbicular leaf is a round circle, and can be written as

<!-- b000074 | prose | pages [9] -->
a   0 r a , (1) where a interprets the radius of the leaf.

<!-- b000075 | caption | pages [9] -->
Figure 4 Shape function of Orbicular leaves (a=5)

<!-- b000076 | prose | pages [9] -->
By integration, we can find the size and cell-division margin length of orbicular

<!-- b000077 | prose | pages [9] -->
leaves

<!-- b000078 | prose | pages [9] -->
  2 1A a (2)

<!-- b000079 | prose | pages [9] -->
  S 2 a (3) 1

<!-- b000080 | prose | pages [9] -->
 Type 2: Cordate leaves & Reniform leaves

<!-- b000081 | prose | pages [9] -->
The shapes of cordate and reniform leaves have a lot in common, with the

<!-- b000082 | prose | pages [9, 10] -->
former one shapes like a heart and the latter a kidney. Such features can both be captured by a trigonometric function.

<!-- b000083 | furniture | pages [10] -->
Team # 14297

<!-- b000084 | furniture | pages [10] -->
Page 10 of 45

<!-- b000086 | prose | pages [10] -->
a     0 , (4) r a (1 cos )

<!-- b000087 | caption | pages [10] -->
Figure 5 Shape function of Reniform Leaves (a = 5)

<!-- b000088 | prose | pages [10] -->
Size of Leaf area and cell-division margin length are

<!-- b000089 | prose | pages [10] -->
 2 3 a  (5) A 2 2

<!-- b000090 | prose | pages [10] -->
     S 2 a (6) 2

<!-- b000091 | prose | pages [10] -->
 Type 3: Lobed leaves, & Palmate leaves

<!-- b000092 | prose | pages [10] -->
Another form of trigonometric function is used to describe lobed and palmate

<!-- b000093 | prose | pages [10] -->
leaves. We can adjust the range of parameter to control the indentation of

<!-- b000094 | prose | pages [10] -->
margins.

<!-- b000095 | prose | pages [10] -->
  k (7) r a b sin( )

<!-- b000096 | prose | pages [10] -->
where a, b are both positive constants, k are natural numbers indicating the

<!-- b000097 | prose | pages [10] -->
amount of lobes.

<!-- b000098 | furniture | pages [11] -->
Team # 14297

<!-- b000099 | furniture | pages [11] -->
Page 11 of 45

<!-- b000100 | caption | pages [11] -->
Figure 6 Shape function of lobed Leaves (a = 3, b=2, k=5)

<!-- b000101 | caption | pages [11] -->
Figure 7 Shape function of Palmate Leaves (a = 3.8, b=1.2, k=5)

<!-- b000102 | prose | pages [11] -->
Area and margin length of leaves

<!-- b000103 | prose | pages [11] -->
  b  2 2 A ( a ) (8) 3

<!-- b000104 | prose | pages [11] -->
  S 2 a (9) 3

<!-- b000105 | prose | pages [11] -->
 Type 4: Elliptic Leaves

<!-- b000106 | prose | pages [11] -->
Leaves of this type are oval-shaped, which is expressed by a pair of symmetric

<!-- b000107 | prose | pages [11] -->
trigonometric functions (10).

<!-- b000108 | furniture | pages [12] -->
Team # 14297

<!-- b000109 | furniture | pages [12] -->
Page 12 of 45

<!-- b000110 | prose | pages [12] -->
1 1 (sin         a cos ) 4 2 ( a  0 )               (10) 1 3         a (sin cos ) 2 4

<!-- b000111 | caption | pages [12] -->
Figure 8 Shape Function of Elliptic Leaves (a=10, k=1/4)

<!-- b000112 | prose | pages [12] -->
The cell division accounts for a proportion much larger than the none-division

<!-- b000113 | prose | pages [12] -->
part (i.e. the black edge in Figure 5), and can be ignored when we compute the

<!-- b000114 | prose | pages [12] -->
margin length S .

<!-- b000115 | prose | pages [12] -->
Area and cell division margin length of the leaf are

<!-- b000116 | prose | pages [12] -->
  1 1    2 A a (11)   4  4 2 

<!-- b000117 | prose | pages [12] -->
       S 2 a sin( k ) cos( k ) 1 (12) 4

<!-- b000118 | prose | pages [12] -->
 Type 5: Flabellate Leaves

<!-- b000119 | prose | pages [12] -->
Flabellate leaves are fan-shaped, which can be resembled by a sector of a pie.

<!-- b000120 | prose | pages [12] -->
By changing the central angle and radius, the leaf shape can be adjusted. It is

<!-- b000121 | prose | pages [12] -->
described by function (13).

<!-- b000122 | prose | pages [12] -->
      r a k k , (13) 1 2

<!-- b000123 | prose | pages [12] -->
2k are constants defining the domain of the central angle . 1k , where

<!-- b000124 | prose | pages [12, 13] -->
The following graph illustrates the shape of flabellate leaves by taking the radius to be 5, and central angle 1 3      . 4 4

<!-- b000125 | furniture | pages [13] -->
Team # 14297

<!-- b000126 | furniture | pages [13] -->
Page 13 of 45

<!-- b000128 | caption | pages [13] -->
Figure 9 Shape Function of Flabellate Leaves (a=5)

<!-- b000129 | prose | pages [13] -->
Area and margin length of leaves are shown below.

<!-- b000130 | prose | pages [13] -->
  k a  2 (14) A 2( k ) 5 2 1     S ( k k a ) 2 a (15) 5 2 1

<!-- b000131 | heading | pages [13] -->
2.2 Model of cell growth and physiological activities

<!-- b000132 | heading | pages [13] -->
2.2.1 Growth Model

<!-- b000133 | prose | pages [13] -->
Given the prominence of leaves in our environment and their importance for plant function, it is surprising that so little is known about the physiological process developing these organs. Most studies of leaf function have focused on photosynthetic capacity, light interception, and responses of leaves to the environment. However up to the current time, there is no exactly biological theory that could explain the inner mechanism of cell growth.

<!-- b000134 | prose | pages [13] -->
Many factors contribute to the regulation of cell growth, involving biophysical considerations, wall extension, osmotic regulation, photobiological control of ion fluxes, and other extraneous factors in the environment (Van Volkengurgh, 1999).

<!-- b000135 | furniture | pages [14] -->
Team # 14297

<!-- b000136 | furniture | pages [14] -->
Page 14 of 45

<!-- b000137 | prose | pages [14] -->
Our model for leaf expansion is derived from the one proposed in the work of Lizaso et al. (2002), but improves the original version by including cell division along the leaf margin. The sigmoidal logistic model is applied to fulfill the basic requirement of cell growth model and to simulate the process of leaf expansion.

<!-- b000138 | prose | pages [14] -->
LA by a sigmoidal Lizaso et al. (2002) show the expansion of each leaf blade i logistic function:

<!-- b000139 | prose | pages [14] -->
Ae  (16) i LA i e  ke t te ( ) 1 i i

<!-- b000140 | prose | pages [14] -->
Ae is the final surface area of the ith leaf, te is the thermal time when the leaf where i i reaches 50% of its final area.

<!-- b000141 | prose | pages [14] -->
ke , we define this term as a polynomial of Differing from Lizaso’s definition of i degree n about the length of cell-division leaf margin S :

<!-- b000142 | prose | pages [14] -->
n  i (17) ke a S i i  i 0

<!-- b000143 | prose | pages [14] -->
GR ei Daily calculation of leaf expansion is conducted in the form of growth rate of

<!-- b000144 | prose | pages [14] -->
each leaf at thermal timet . The result is obtained from the first derivative of (1):

<!-- b000145 | prose | pages [14] -->
  ke t te ( ) dLA e i i   (18) i GR e ( Ae ke ) (1 i i i    ke t te ( ) 2 dt e ) i i

<!-- b000146 | prose | pages [14] -->
Ae is the final area of leaf blade. where parameter i

<!-- b000147 | heading | pages [14] -->
2.2.2 Model for physiological activities

<!-- b000148 | prose | pages [14, 15] -->
In this subsection, we devote our interest to the structure of leaves and how those structures are adapted to carry out effectively certain physiological and biochemical functions. Three types of physiological activities are modeled and evaluation of their effects on leaves’ shape characters is performed. These physiological functions are photosynthesis, substance transportation, and transpiration.

<!-- b000149 | furniture | pages [15] -->
Team # 14297

<!-- b000150 | furniture | pages [15] -->
Page 15 of 45

<!-- b000152 | prose | pages [15] -->
Photosynthesis: Energy Conservation

<!-- b000153 | caption | pages [15] -->
Figure 10 Photosynthesis Process

<!-- b000154 | prose | pages [15] -->
Photosynthesis is the primary function of green vegetation which allows the plant to conserve solar energy to stable chemical form (William & Norman, 2009). After the photosynthesis machine generates utilizable energy, ATP is provided to the whole plant. To absorb light efficiently, leaves usually present a large surface area to the incoming sunlight. And the effective area is to a great extent associated with the efficiency of photosynthesis. The physiological and biochemical functions of leaves are targeted in our model at the same time.

<!-- b000155 | prose | pages [15] -->
We model the energy conservation process by simulating its two stages: Light-dependent reactions and CO2 assimilation.

<!-- b000156 | furniture | pages [16] -->
Team # 14297

<!-- b000157 | furniture | pages [16] -->
Page 16 of 45

<!-- b000158 | prose | pages [16] -->
 Harvesting sunlight

<!-- b000159 | prose | pages [16] -->
A series of steps, called light-dependent reactions describe how chloroplasts conserve energy from sunlight to ATP and reducing potential (as NADPH). The biological principle followed in this stage is that plant leaves are photosynthetic machines that maximize the absorption of light. This principle is the guideline of our model constructing procedures. It also applies to our model construction in Section 2.3 when considering leaf overlapping.

<!-- b000160 | prose | pages [16] -->
The efficiency of photosynthesis denoted by  can be estimated by a function of

<!-- b000161 | prose | pages [16] -->
incident light intensity I and the probability of radiation penetration in forest canopies P , where P can be expressed as a function of the zenith angle:

<!-- b000162 | prose | pages [16] -->
   (19) I P ( )

<!-- b000163 | prose | pages [16] -->
The intensity of incident light I is generated from the Black-radiation formula in general physics, which is expressed by the following equation:

<!-- b000164 | prose | pages [16] -->
 5 k  I (20) c  e 1 kT

<!-- b000165 | prose | pages [16] -->
where k is the Boltzmann constant; is the wavelength; is the Planck constant; c is the speed of light; and T is the absolute temperature of the black body.

<!-- b000166 | prose | pages [16] -->
Radiation penetration probability P is developed based on the work of Chen et al. (1997a). It is the probability of a direct bean penetrating through a forest at zenith angle 

<!-- b000167 | prose | pages [16] -->
      K ( ) ( ) L   P ( ) exp e (21)       (1 )cos( )   e

<!-- b000168 | prose | pages [16] -->
 e  ( ) where L is the Leaf Area Index (LAI); is the canopy non-randomness index;

<!-- b000169 | prose | pages [16, 17] -->
eis a correction factor for within-shoot clumping in conifers; is the woody-to-total foliage hemi-surface area ratio in the canopy and can be numerically demonstrated by:

<!-- b000170 | furniture | pages [17] -->
Team # 14297

<!-- b000171 | furniture | pages [17] -->
Page 17 of 45

<!-- b000173 | prose | pages [17] -->
W  (22)  W L

<!-- b000174 | prose | pages [17] -->
where W is the total woody hemi-surface area index of branches and stems.

<!-- b000175 | prose | pages [17] -->
 CO2 assimilation

<!-- b000176 | prose | pages [17] -->
Photosynthetic gas exchange between leaf and air is controlled by the opening and closing of stomata, where photosynthetic carbon reduction (PCR) cycle occurs. We focus on the CO2 assimilation process: how CO2 enters the leaf and subsequently is reduced through the utilization of the NADPH and ATP produced by photosynthetic electron transport.

<!-- b000177 | prose | pages [17] -->
The assumption is made that the production ratio of CO2 over O2 is taken as 1. We model the time dependence of CO2 assimilation by a set of differential equations proposed by Marcelo et al. (2000). The model is divided into three parts. The number of CO2 receivers and excited receivers are determined by concentration of CO2 and radiant flux intensity. The amount of product, substance and complex can be all predicted by time-dependent differential equations. The product can be seen as one kind of indicator to demonstrate how much energy has been generated by the plant.

<!-- b000178 | prose | pages [17] -->
 Part A

<!-- b000179 | prose | pages [17] -->
Two main phenomenological differential equations are introduced for the number of light excited receiver N t and the quantity of CO2 receivers M t , respectively: ( ) ( )

<!-- b000180 | prose | pages [17] -->
dN t ( )      (23) k I N N t ( ) k M t N t ( ) ( ) 1 r max 2 dt dM t ( )      (24) k C M M t ( ) k M t N t ( ) ( ) 3 max 4 dt

<!-- b000181 | prose | pages [17, 18] -->
1k , 2k , 3k ,and 4k are phenomenological parameters; N where is the total number max rI is the radiant flux intensity; C is the concentration of of light excited receivers,

<!-- b000182 | furniture | pages [18] -->
Team # 14297

<!-- b000183 | furniture | pages [18] -->
Page 18 of 45

<!-- b000185 | prose | pages [18] -->
M CO2 in the mesophyll, and is the total number of CO2 receivers. max

<!-- b000186 | prose | pages [18] -->
 Part B

<!-- b000187 | prose | pages [18] -->
Marcelo et al. (2000) show another equation for result comparison. This equation

<!-- b000188 | prose | pages [18] -->
involves the assimilation of CO2 in closed measurement system:

<!-- b000189 | prose | pages [18] -->
dC t ( )      (25) k C t ( ) 1 m t ( ) k 5 6 dt

<!-- b000190 | prose | pages [18] -->
6k where represents the effect of CO2-production by photorespiration,

<!-- b000191 | prose | pages [18] -->
M t ( )      k 5 1 m t ( ) , and the term represents the effect of CO2 reduction on m t ( ) M max

<!-- b000192 | prose | pages [18] -->
the CO2 concentration of the measurement system.

<!-- b000193 | prose | pages [18] -->
 Part C

<!-- b000194 | prose | pages [18] -->
To formulate the enzyme reaction equations, the following set of differential

<!-- b000195 | prose | pages [18] -->
equations are constructed:

<!-- b000196 | prose | pages [18] -->
dp t ( )  (26) k se t ( ) 7 dt

<!-- b000197 | prose | pages [18] -->
dse t ( )     (27) k s t ( ) ( k s t ( ) k k se t ) ( ) 8 8 8 7 dt

<!-- b000198 | prose | pages [18] -->
ds t ( )    (28) k s t ( ) ( k s t ( ) k se t ) ( ) 8 8 8 dt

<!-- b000199 | prose | pages [18] -->
7k and 8k are the rates of the reactions; where p t is the product; s t is the ( ) ( )

<!-- b000200 | prose | pages [18] -->
substrate; and se t is a complex. ( )

<!-- b000201 | prose | pages [18] -->
The amount of product will be shown in the governing equations in Section 2.4 to

<!-- b000202 | prose | pages [18] -->
estimate the properties of the whole tree system.

<!-- b000203 | furniture | pages [19] -->
Team # 14297

<!-- b000204 | furniture | pages [19] -->
Page 19 of 45

<!-- b000205 | prose | pages [19] -->
Transportation

<!-- b000206 | prose | pages [19] -->
Nutrient salts, ions, and steroids are of vital importance to the growth and development of plants. Take auxin as an example, which is a kind of plant hormone, plays a central role in the in-plant activities including vascular development. The uptake of these substances by plants involves various types of transportation procedures like simple diffusion, facilitated diffusion, or active transportation. Facilitated diffusion and active transport are mediated by channel and carrier proteins, of which the latter requires a source of metabolic energy, normally in the form of ATP.

<!-- b000207 | prose | pages [19] -->
We model the auxin-transport system since it captures all the related elements in the transport activities — the transport channel, the carrier, and the energy consumed. Another notable reason for our choice is that the auxin model has the least number of disturbing factors, like the potential distinction between external eco-system and the internal environment of the plant to list a few.

<!-- b000208 | prose | pages [19] -->
Leaf venation patterns are used to describe the transportation behavior. To support this view point, we provide the following reasons.

<!-- b000209 | prose | pages [19] -->
 According to fluid mechanics, after divided by the efficiency of transportation mechanism, the flux of auxin in the veins could reflect the distribution of transportation channels (Falkovich et al, 2011).

<!-- b000210 | prose | pages [19] -->
 In order to make this model comparable with the photosynthesis process which occurs only inside the chloroplast of leaves, transportation activities should also be analyzed by observing the section structure of isolated leaves.

<!-- b000211 | prose | pages [19] -->
Hence, the geometric traits of leaves, in this case cell-division margin and size, become the determinant factors in the physiological mechanism. This matches the intention of out model to start from individual units and extend it to the entire system by simulating the in-plant communication.

<!-- b000212 | prose | pages [19, 20] -->
Here we adopt the approach proposed by Hironori and Atsushi (2006), which examine the formation of leaf venation patterns by modeling the positive feedback

<!-- b000213 | furniture | pages [20] -->
Team # 14297

<!-- b000214 | furniture | pages [20] -->
Page 20 of 45

<!-- b000216 | prose | pages [20] -->
regulation between plant hormone auxin and its efflux carrier. And the mathematical

<!-- b000217 | prose | pages [20] -->
model is presented below.

<!-- b000218 | prose | pages [20] -->
Individual cells are aligned as two-dimensional hexagons, with position of the cell

<!-- b000219 | prose | pages [20] -->
denoted byi and j , which are two independent directions of the hexagonal cell.

<!-- b000220 | prose | pages [20] -->
Another indicator k represents the cell membrane side of the cell. Auxin and auxin

<!-- b000221 | prose | pages [20] -->
efflux carrier are located in each side of the cell membrane, respectively.

<!-- b000222 | prose | pages [20] -->
Assuming auxin outflow from the k-th side of cell membrane of the( , ) i j cell to the

<!-- b000223 | prose | pages [20] -->
adjacent k’-th side of the( ', ') i j cell is proportional to the product of auxin efflux

<!-- b000224 | prose | pages [20] -->
carrier p and auxin a densities, the auxin flow between neighboring cells f ijk ijk ijk

<!-- b000225 | prose | pages [20] -->
can be obtained by the difference in the auxin outflows from the two cells:

<!-- b000226 | prose | pages [20] -->
  f cp a cp a (29) ijk ijk ij i j k ' ' ' i j ' '

<!-- b000227 | prose | pages [20] -->
where c is a constant.

<!-- b000228 | prose | pages [20] -->
The differential equations for the dynamics of auxin efflux carrier p and auxin ijk

<!-- b000229 | prose | pages [20] -->
a are described in the following form: ijk

<!-- b000230 | prose | pages [20] -->
dp g f ( ) ijk  ijk  s d p (30)  p p ijk dt g f ( ) ijk k

<!-- b000231 | prose | pages [20] -->
da  dt  ij  (31) s d a f a a ij ijk k

<!-- b000232 | prose | pages [20] -->
g f ( )  ijk g f ( ) (32) ijk     1 exp[ ( f f )] ijk 0

<!-- b000233 | prose | pages [20, 21] -->
as is the ps is the carrier synthesis rate; d is the carrier degradation rate, where p d is the auxin degradation rate; , ,  auxin synthesis rate; f cs s / ( d d ) are a 0 p a p a

<!-- b000234 | furniture | pages [21] -->
Team # 14297

<!-- b000235 | furniture | pages [21] -->
Page 21 of 45

<!-- b000237 | prose | pages [21] -->
constants, and g is an increasing function of auxin flow.

<!-- b000238 | prose | pages [21] -->
Transpiration

<!-- b000239 | prose | pages [21] -->
Transpiration is the process that large amounts of water are lost by plants through evaporation from leaf surfaces. It is driven by differences in water vapor pressure between internal leaf spaces and the ambient air. A variety of factors influence transpiration rate, including temperature, humidity, wind, and leaf structure. Water is conducted upward through the plant primarily in the xylem, a tube-like system of treachery elements. And lost water by transpiration is replenished by the absorption of water from the soil through the root (Figure 1). It is worth noticing that transpiration process provides the principle driving force to the operation of the whole plant system (William & Norman, 2009).

<!-- b000240 | caption | pages [21] -->
Figure 11 Illustration of Transpiration

<!-- b000241 | prose | pages [21, 22] -->
Water movement in xylem is driven by transpiration and the resulting tension in the water column which is maintained because of the high tensile strength of water. Following this statement, we construct the transpiration model via the approach taken by Edwards et al. (1986). While he modeled flow of water in a single tree was

<!-- b000242 | furniture | pages [22] -->
Team # 14297

<!-- b000243 | furniture | pages [22] -->
Page 22 of 45

<!-- b000245 | prose | pages [22] -->
modeled in terms of the Darcy equation using a set of four compartments: root, stem,

<!-- b000246 | prose | pages [22] -->
branches, and leaves, we only consider transpiration through xylem.

<!-- b000247 | prose | pages [22] -->
Assumptions presented by Edward et al. (1986) are also adopted:

<!-- b000248 | prose | pages [22] -->
1) Water moves in the plant from points of high potential to points of low

<!-- b000249 | prose | pages [22] -->
potential, along pathways that exert a frictional drag or resistance to flow.

<!-- b000250 | prose | pages [22] -->
2) Flow in the xylem of plants is adequately represented by the Darcy equation.

<!-- b000251 | prose | pages [22] -->
3) The relative conductivity of the xylem is a unique function of the proportion

<!-- b000252 | prose | pages [22] -->
of void volume filled with water (i.e. relative water content).

<!-- b000253 | prose | pages [22] -->
4) The proportion of void volume that is water-filled is a function of the water

<!-- b000254 | prose | pages [22] -->
potential of the tissue.

<!-- b000255 | prose | pages [22] -->
5) Axial flow in the stem is confined to the sapwood which has uniform

<!-- b000256 | prose | pages [22] -->
proportions of void and woody metric volumes

<!-- b000257 | prose | pages [22] -->
6) The cross-sectional area of sapwood in the stem is a function of height.

<!-- b000258 | prose | pages [22] -->
7) The leaves, branches and roots are not subdivided but are treated as uniform

<!-- b000259 | prose | pages [22] -->
compartments attached in series to the clear stem.

<!-- b000260 | prose | pages [22] -->
8) At any moment, temperature is constant throughout the system.

<!-- b000261 | prose | pages [22] -->
Functions describing the process of transpiration are derived as following. The

<!-- b000262 | prose | pages [22] -->
Darcy equation defines axial flow Q by

<!-- b000263 | prose | pages [22] -->
 KA  (33) Q l

<!-- b000264 | prose | pages [22] -->
where l is length; A is the cross-sectional area; is the potential difference; K is

<!-- b000265 | prose | pages [22] -->
the relative conductivity of the sapwood;is the viscosity of the sap.

<!-- b000266 | furniture | pages [23] -->
Team # 14297

<!-- b000267 | furniture | pages [23] -->
Page 23 of 45

<!-- b000268 | prose | pages [23] -->
Within each component, the flow resistance R was defined by rearrangement of (33) as

<!-- b000269 | prose | pages [23] -->
  l   (34) R Q KA

<!-- b000270 | prose | pages [23] -->
In the absence of flow, water potential is directly related to the height of measurement z above a reference level (taken to be ground level) through the effect of gravity, as follows:

<!-- b000271 | prose | pages [23] -->
  (35) z g

<!-- b000272 | prose | pages [23] -->
where is the density of water and g the acceleration due to gravity.

<!-- b000273 | heading | pages [23] -->
2.3 Model of leaf arrangement & branching structure

<!-- b000274 | heading | pages [23] -->
2.3.1 Leaf arrangement

<!-- b000275 | prose | pages [23] -->
The biological principle states that plant leaves are photosynthetic machines that maximize the absorption of light. Thus to minimize overlapping individual shadows and achieving the maximum exposure, leaves have evolved the optimal response to mix of environmental elements. Among such evolutionary features, leaf shape and phyllotaxy are two critical traits that affect the interactions between leaves. In this section, inter-leaf relations are examined in terms of position arrangement on the stem. And such arrangement determines the angle of the petioles. Here we present two types of models applying to different dimensions. The 2-D model assumes that sunlight is perpendicular to the ground surface, thus leaves at different level spots can be projected to a 2-D plane (Figure 12). The model can be extended to 3-D cases by adding the angle of incidence of sunlight.

<!-- b000276 | furniture | pages [24] -->
Team # 14297

<!-- b000277 | furniture | pages [24] -->
Page 24 of 45

<!-- b000278 | caption | pages [24] -->
Figure12 Three Types of Leaf Arrangements Projected on a Plane

<!-- b000279 | heading | pages [24] -->
 Two-dimensional modeling

<!-- b000280 | prose | pages [24] -->
To simplify the computation of overlapping areas and add more comparability, we

<!-- b000281 | prose | pages [24] -->
standardize various shapes into their circumcircles with the equal-length radius, and

<!-- b000282 | prose | pages [24] -->
the overlapping area can be obtained by finding the intersection of two circles in plane

<!-- b000283 | prose | pages [24] -->
geometry (Figure 13).

<!-- b000284 | caption | pages [24] -->
Figure 13 Standardized Overlapping Leaves

<!-- b000285 | prose | pages [24] -->
    OCA O CA We denote the radius of circles as r ; length of petiole as x ; ; 1 2

<!-- b000286 | prose | pages [24] -->
     AOO BOO O F m ; 1 2 1 2 1

<!-- b000287 | prose | pages [24, 25] -->
Area of intersection is written as m     1 2 2 2 (36) A 2cos ( ) r 2 m r m shade r    where r is the radius of the circles; . m ( r x )sin

<!-- b000288 | furniture | pages [25] -->
Team # 14297

<!-- b000289 | furniture | pages [25] -->
Page 25 of 45

<!-- b000291 | prose | pages [25] -->
The overlapping conditions are sorted into two general catalogs: convex-margin leaves and concave-margin leaves. For leaves with convex, the overlapping area is estimated by calculating the area of the shaded region, while for concave-margin leaves, overlapping area is computed by adjusting the area in shadow with a ratio  related to the included angle ( 2) of the two petioles (Table 1). ( )

<!-- b000292 | caption | pages [25] -->
Table 2: Computation of Overlapping Areas

<!-- b000293 | prose | pages [25] -->
Convex-margin Leaves Concave-margin Leaves

<!-- b000294 | prose | pages [25] -->
   A A A ( ) A overlap shade overlap shade The area exposed under sunlight can be derived as the difference between total size of leaves and sum of the overlapping regions.

<!-- b000295 | prose | pages [25] -->
    A A A (37) exposure i overlap where A is the size of a single piece of leaves.

<!-- b000296 | heading | pages [25] -->
 Three-dimensional modeling

<!-- b000297 | prose | pages [25] -->
In the 3-D model, the position of leaves in branch and tree volume will be transferred into two indicators: height and angle. Some assumptions embedded in the three-dimensional model of phyllotaxy are listed below:

<!-- b000298 | prose | pages [25] -->
 Vertex (i.e. leaves at top-ends) is not considered

<!-- b000299 | prose | pages [25] -->
 The distance ( h ) between adjacent nodes is large enough.

<!-- b000300 | prose | pages [25] -->
 Number of leaves ( n ) is large enough.

<!-- b000301 | furniture | pages [26] -->
Team # 14297

<!-- b000302 | furniture | pages [26] -->
Page 26 of 45

<!-- b000303 | prose | pages [26] -->
Consider the height and interactions of leaves, and take the elliptic leaf as an example, the overlapping area can be derived under different leaf arrangement patterns. Assuming an anglebe the inclination of angle of direct solar beam. a andb

<!-- b000304 | prose | pages [26] -->
are the semiminor and semimajor axis of the elliptic leaf; s is the width of area without shadow casted by the leaves above, and is denoted by the formula   (38) s h cot

<!-- b000305 | prose | pages [26] -->
Observing the effect of leaf arrangement on the overlapping areas, situations for alternate and opposite arrangements are quite similar, while the whorled arrangement is taken as a special case if the last two assumptions are fulfilled (Table 2).

<!-- b000306 | caption | pages [26] -->
Table 3: Overlapping under Different Leaf Arrangements

<!-- b000307 | prose | pages [26] -->
Alternate Opposite

<!-- b000308 | prose | pages [26] -->
Whorled

<!-- b000309 | prose | pages [26, 27] -->
Overlapping areas for the three arrangements are formulated by   2 2 2 n s a ( b )    (39) A n ab alt 4 ab  2 n s a    (40) A n ab opp 2 b      2 (41) A 2 s x ( r ) s whr

<!-- b000310 | furniture | pages [27] -->
Team # 14297

<!-- b000311 | furniture | pages [27] -->
Page 27 of 45

<!-- b000313 | prose | pages [27] -->
A , A where A , denote the overlapping areas for alternate, opposite, and alt whr opp whorled arrangement, respectively.

<!-- b000314 | heading | pages [27] -->
2.3.2 Branching structure

<!-- b000315 | prose | pages [27] -->
In this subsection, we use the LA system model, which is one kind of rod-based model to simulate the growth of branches. Development of branching structure is largely influenced by various ecological factors, among which “wind can be an important mortality factor to branch structure” as stated by Stiling (2002) in the book Ecology. The guiding principle of the model is to find the most stable cases by classical mechanics. In the model constructing process, two critical elements are taken into account, namely branch growth tendency and effective leaf area. Mostly, leaves area is probably the variable that has the largest influence on branch structure in the evolution history, since in the vegetation life span, branches and leaves develop inter-dependently (Walter, 2001). The list of assumptions for this model is provided:

<!-- b000316 | prose | pages [27] -->
 Branch structure will exist in the most stable case;

<!-- b000317 | prose | pages [27] -->
 Leaves in each branch are identical in size, and distributed uniformly;

<!-- b000318 | prose | pages [27] -->
 All branches are rigid;

<!-- b000319 | prose | pages [27] -->
 All the leaves are located at the end of branches. Since the growth of a plant axis is subject to the external force oriented in the direction of the preferred tendency of growth, we first develop the formula describing force of wind by   F Av (42) wind where A is the effective area of leaves; v is the constant speed of wind.

<!-- b000320 | furniture | pages [28] -->
Team # 14297

<!-- b000321 | furniture | pages [28] -->
Page 28 of 45

<!-- b000322 | prose | pages [28] -->
 The torque of the wind force is expressed as wind

<!-- b000323 | prose | pages [28] -->
      Av l cos( ) (43) wind i i

<!-- b000324 | prose | pages [28] -->
iis the angle between segments i and i-1. il is the length of segment i, and where

<!-- b000325 | prose | pages [28] -->
The torque exerted by an individual spring is shown as

<!-- b000326 | prose | pages [28] -->
   k (44) i i i x x x

<!-- b000327 | prose | pages [28] -->
xiis the rotational displacement due to external where xik is the spring constant;

<!-- b000328 | prose | pages [28] -->
forces.

<!-- b000329 | prose | pages [28] -->
To maintain the stable, the two torque must be equal

<!-- b000330 | prose | pages [28] -->
   (45) wind i x

<!-- b000331 | prose | pages [28] -->
The rotational displacement can be obtained by solving (10)

<!-- b000332 | prose | pages [28] -->
1      (46) Av l cos( ) i i k x i x

<!-- b000333 | prose | pages [28] -->
Each new layer that is added to a segment has a unique spring constant which can

<!-- b000334 | prose | pages [28] -->
be used to calculate the overall spring constant at that point. The spring constant about

<!-- b000335 | prose | pages [28] -->
the x-axis at joint i for an individual layer m is calculated by

<!-- b000336 | prose | pages [28] -->
E I  i i 1  k (47) x x i l xm  i 1

<!-- b000337 | prose | pages [28] -->
il is the length of where xiE is the shear modulus of the material about the x-axis, 1

<!-- b000338 | prose | pages [28] -->
segment i-1 that rotates about joint i, and iI is the torsional constant of the layer 1x

<!-- b000339 | prose | pages [28] -->
about joint i.

<!-- b000340 | prose | pages [28] -->
We assume the new layer to be a hollow ring, and the torsional constant iI is 1x

<!-- b000341 | prose | pages [28] -->
calculated using the formula    4 4 (48) I ( R r )    i 1 i 1 i 1 2 x

<!-- b000342 | prose | pages [28] -->
iR is the distance from the center of the cross-section to the outer edge of the where 1

<!-- b000343 | prose | pages [28, 29] -->
ir  is the distance from the center of the cross-section to the inner edge of layer and 1 the layer. We have obtained the computation results about the x axes. For y and z axes,    4 4 (49) I ( R r )    i 1 i 1 i 1 4

<!-- b000344 | furniture | pages [29] -->
Team # 14297

<!-- b000345 | furniture | pages [29] -->
Page 29 of 45

<!-- b000347 | heading | pages [29] -->
2.4 Model of the tree characteristics

<!-- b000348 | prose | pages [29] -->
Generally speaking, in the early stage, characteristics of a tree such as height, volume and mass relate positively with the mass accumulation of leaves. As we know, almost all structures of the tree, including leaves, stems, branches, and root, will growth simultaneously, although at various growth rate. It is also possible for us to find the inner link between them by the governing equations based on the vital physiological activities mentioned in Section 2.2.

<!-- b000349 | prose | pages [29] -->
However, after the tree researches maturity, the observable relationship between the size of the tree and leaf mass will fade way. This is because that the percentage of dead cells in xylem will end up being the major part of the tree. The metabolic activities will demonstrate seasonal pattern instead of strict positive correlations. And the environmental factors will outweigh the inner traits of the plant and reshape some of the biophysical features. Hence, out model is restricted to the early stage of trees.

<!-- b000350 | prose | pages [29] -->
Two distinct modeling approaches are addressed in this subsection: physiological and structural. And we will demonstrate and evaluate both models respectively.

<!-- b000351 | prose | pages [29] -->
 Physiological Approach

<!-- b000352 | prose | pages [29] -->
We have talked about the energy conservation balance and the driving force operation in Section 2.2. By applying the bio-mechanism of metabolic energy cycle and inner force equilibrium, two governing equations can be obtained.

<!-- b000353 | prose | pages [29] -->
Assumptions adopted by this approach are:

<!-- b000354 | prose | pages [29] -->
(1) Photosynthesis is the only energy source for plant functioning.

<!-- b000355 | prose | pages [29, 30] -->
(2) Transpiration mechanism is the only driving force generator for the active transportation plant.

<!-- b000356 | furniture | pages [30] -->
Team # 14297

<!-- b000357 | furniture | pages [30] -->
Page 30 of 45

<!-- b000359 | prose | pages [30] -->
The energy transformation function is derived by describing the process of ATP

<!-- b000360 | prose | pages [30] -->
production and consumption. The left-hand-side represents the ATP produced by

<!-- b000361 | prose | pages [30] -->
photosynthesis; and the right-hand-side equation is the amount of energy consumer,

<!-- b000362 | prose | pages [30] -->
both are in Joule.

<!-- b000363 | prose | pages [30] -->
       (50) nA P n Q f h

<!-- b000364 | prose | pages [30] -->
where n is the unit of ATP; P is the product of photosynthesis; A is the total

<!-- b000365 | prose | pages [30] -->
effective leaf area; Q indicates total flow in transpiration; f indicates total flow in

<!-- b000366 | prose | pages [30] -->
transportation; h is the height of the tree; is the amount of ATP consumed in other

<!-- b000367 | prose | pages [30] -->
activates; and , ,are constant coefficients.

<!-- b000368 | prose | pages [30] -->
The equilibrium condition reached by the driving force (i.e. transpiration can

<!-- b000369 | prose | pages [30] -->
provide sufficient driving force needed by the substance transport process) in the plant

<!-- b000370 | prose | pages [30] -->
system is presented by

<!-- b000371 | prose | pages [30] -->
     (51) n ' Q ' f h '

<!-- b000372 | prose | pages [30] -->
, are constant coefficients. where ' '

<!-- b000373 | prose | pages [30] -->
The height of tree ( h ) can be solved by solving the equation set (51) & (50).

<!-- b000374 | prose | pages [30] -->
However, this approach is almost impossible to carry out, since we may never

<!-- b000375 | prose | pages [30] -->
obtain the precise value of the coefficients in the equations and it is of great difficulty

<!-- b000376 | prose | pages [30] -->
to quantify the elements presented in the above equations.

<!-- b000377 | prose | pages [30] -->
 Structural Approach

<!-- b000378 | prose | pages [30] -->
 Tree Volume Estimation

<!-- b000379 | prose | pages [30, 31] -->
To estimate the volume of the tree, we resemble the cone-shaped tree as round platforms piling up. These platforms can be generated by rotating the branches around

<!-- b000380 | furniture | pages [31] -->
Team # 14297

<!-- b000381 | furniture | pages [31] -->
Page 31 of 45

<!-- b000383 | prose | pages [31] -->
the tree trunk, with the curved surface indicating the route of branch-top leaf piece

<!-- b000384 | prose | pages [31] -->
wiping through the air (Figure 1).

<!-- b000385 | prose | pages [31] -->
We then compute the volume of single platform by

<!-- b000386 | prose | pages [31] -->
 l 2 iT   r  (52) V T (2 x 4 ) i  sin

<!-- b000387 | prose | pages [31] -->
 where r is the radius of leaves’ blade; T 2 r ; x is the length of petiole; l is the

<!-- b000388 | prose | pages [31] -->
 ); is the equivalent angle between the l l equivalent length of the bottom branch ( 1

<!-- b000389 | prose | pages [31] -->
branch and tree trunk.

<!-- b000390 | caption | pages [31] -->
Figure 14 Estimate Volume of the Tree by Round Platform

<!-- b000391 | prose | pages [31] -->
  The volume of the tree is thus the summation the platform volumes till l 2 iT 0

<!-- b000392 | prose | pages [31] -->
 V V (53) tree i

<!-- b000393 | prose | pages [31, 32] -->
 Tree Height Estimation Illustrated in Figure 14, the height of a single platform can be expressed by

<!-- b000394 | furniture | pages [32] -->
Team # 14297

<!-- b000395 | furniture | pages [32] -->
Page 32 of 45

<!-- b000397 | prose | pages [32] -->
    ih 2 sin r T sin (54)

<!-- b000398 | prose | pages [32] -->
Therefore, height of a tree is obtained by

<!-- b000399 | prose | pages [32] -->
     H l cos h h (55) tree i trunk

<!-- b000400 | prose | pages [32] -->
h where is the height of tree trunk. trunk

<!-- b000401 | prose | pages [32] -->
 Leaf mass Estimation

<!-- b000402 | prose | pages [32] -->
In order to reach equilibrium, the function which represents gravity moment used

<!-- b000403 | prose | pages [32] -->
by Aaron & Karl (1988) express the mass function at bending moment by

<!-- b000404 | prose | pages [32] -->
   2 2 (56) M d l Pg sin 2 bending 

<!-- b000405 | prose | pages [32] -->
where d is the diameter of branch’s cross section; l is the length of branch; P is

<!-- b000406 | prose | pages [32] -->
the mass of tissue; is the rotation angle; is the bifurcation angle.

<!-- b000407 | prose | pages [32] -->
The gravity function of mass is written as

<!-- b000408 | prose | pages [32] -->
2 l   (57) M cos( ) M g G 0 2

<!-- b000409 | prose | pages [32] -->
M is the mass of leaves on a single branch. where 0

<!-- b000410 | prose | pages [32] -->
The equal relation is then derived by applying the bending movement principle in

<!-- b000411 | prose | pages [32] -->
engineering

<!-- b000412 | prose | pages [32] -->
 M M (58) bending G

<!-- b000413 | prose | pages [32, 33] -->
By rearranging (9), we can obtain the mass of leaves on a single branch   2 2 d P sin 2  (59) M 0   cos

<!-- b000414 | furniture | pages [33] -->
Team # 14297

<!-- b000415 | furniture | pages [33] -->
Page 33 of 45

<!-- b000417 | prose | pages [33] -->
The total mass of leaves for a tree is derived by

<!-- b000418 | prose | pages [33] -->
 M M N (60) 0 branch

<!-- b000419 | prose | pages [33] -->
N where the max value of is the number of branches of the tree, which can be branch

<!-- b000420 | prose | pages [33] -->
represented by i in the estimation of tree volume.

<!-- b000421 | prose | pages [33] -->
l  (61) max N branch 2 T

<!-- b000422 | furniture | pages [34] -->
Team # 14297

<!-- b000423 | furniture | pages [34] -->
Page 34 of 45

<!-- b000424 | heading | pages [34] -->
Solutions and Results

<!-- b000425 | prose | pages [34] -->
In this section, we describe in detail how the problem can be solved by applying the mathematical model built in the previous section. Since thorough descriptions have been given on the modeling process and the biological or physiological interpretations behind it, we will focus on testing how accurately the models can capture information in practice. Why do leaves have various shapes?

<!-- b000426 | prose | pages [34] -->
While previous literatures mostly take the development of leaf shapes as governed by genetic elements or the result of structural optimization to environmental stress, in this paper we drew more attention to the interaction between plant organs. To answer this question, we examined the impact of cell growth and physiological activities on the formation of the leaf’s blade area and its venation patterns. The growth model simulates the leaf expansion process and proposed a positive correlation between the size of blade area and cell-division margins. Physiological activities discussed in Section 2.2.2 starts from a microscopic functioning of inner leaf structures, showing evidence supporting the optimal selection of physiological features and suggesting necessity of in-plant communications. The evaluation of the models presented in Section 2.2 was conducted by running regression analysis of variable correlations. Data were sourced from the university biological department and ecology labs. Figure 1 and 2 show the regression results of the Growth Model and the ATP determine function in Photosynthesis models. It is observable that most data points fit quite well on the estimated function curves, which suggests a satisfactory accuracy level of the model constructed.

<!-- b000427 | furniture | pages [35] -->
Team # 14297

<!-- b000428 | furniture | pages [35] -->
Page 35 of 45

<!-- b000429 | prose | pages [35] -->
parameter 0.05

<!-- b000430 | prose | pages [35] -->
0.04

<!-- b000431 | prose | pages [35] -->
0.03

<!-- b000432 | prose | pages [35] -->
kei 0.02

<!-- b000433 | prose | pages [35] -->
0.01

<!-- b000434 | prose | pages [35] -->
0.00 10 15 20 25 30 35 S (perimeter) (cm)

<!-- b000435 | caption | pages [35] -->
Figure 15 Regression Results of the Growth Model

<!-- b000436 | prose | pages [35] -->
ATP

<!-- b000437 | prose | pages [35] -->
10000000

<!-- b000438 | prose | pages [35] -->
8000000

<!-- b000439 | prose | pages [35] -->
6000000 product (J) 4000000

<!-- b000440 | prose | pages [35] -->
2000000

<!-- b000441 | prose | pages [35] -->
0

<!-- b000442 | prose | pages [35] -->
0 20 40 60 80 100 120 140 160 180 200 time (min)

<!-- b000443 | caption | pages [35] -->
Figure 16 Regression Result of Photosynthesis model

<!-- b000444 | prose | pages [35] -->
In order to test the transportation model, we applied the graph theory and the basic

<!-- b000445 | prose | pages [35] -->
data structure method to conduct algorithm on the dynamic positive feedback

<!-- b000446 | prose | pages [35] -->
networking (Mark Allen Weiss 1997). In this process, finite volume method was in

<!-- b000447 | prose | pages [35] -->
use to solve the time-dependent differential equation. The following picture

<!-- b000448 | prose | pages [35] -->
demonstrated results of our model. Graph comparison with field data, (Adrian D. Bell

<!-- b000449 | prose | pages [35] -->
1991) verified our model.

<!-- b000450 | furniture | pages [36] -->
Team # 14297

<!-- b000451 | furniture | pages [36] -->
Page 36 of 45

<!-- b000452 | caption | pages [36] -->
Figure 17 Finite Volume Method

<!-- b000453 | prose | pages [36] -->
Do leaf shapes minimize overlapping so as to maximize exposure?

<!-- b000454 | prose | pages [36] -->
In Section 2.3, 2-D and 3-D models were constructed which linked the general shape

<!-- b000455 | prose | pages [36] -->
features with the size of overlapping regions. Our hypothesis stated that leaves

<!-- b000456 | prose | pages [36] -->
develop its shapes to optimize the utilization of sunlight. To test this hypothesis, we

<!-- b000457 | prose | pages [36] -->
compare computational output with experimental results.

<!-- b000458 | prose | pages [36] -->
Table 5

<!-- b000459 | heading | pages [36] -->
2-D Model

<!-- b000460 | prose | pages [36] -->
Input data Output data True value Error

<!-- b000461 | prose | pages [36] -->
Radius of a 5.00 leaf r(cm)

<!-- b000462 | prose | pages [36] -->
Length of Calculated 1.20 True shadowed petiole x(cm) shadowed area 51.00 47.22 6.93% area As_ture(cm2) As(cm2) Number of

<!-- b000463 | prose | pages [36] -->
leaves in a 8

<!-- b000464 | prose | pages [36, 37] -->
circle Table 6

<!-- b000465 | furniture | pages [37] -->
Team # 14297

<!-- b000466 | furniture | pages [37] -->
Page 37 of 45

<!-- b000468 | heading | pages [37] -->
3-D Model for Opposite Arrangement

<!-- b000469 | prose | pages [37] -->
Input data Output data True value Error

<!-- b000470 | prose | pages [37] -->
Semi-major axis

<!-- b000471 | prose | pages [37] -->
of a ellipse leaf 4.60

<!-- b000472 | prose | pages [37] -->
a(cm)

<!-- b000473 | prose | pages [37] -->
Semi-minor axis 1.70 b(cm)

<!-- b000474 | prose | pages [37] -->
Distance between Calculated True shadowed

<!-- b000475 | prose | pages [37] -->
two levels of 2.00 shadowed area 18.90 area 20.10 5.00%

<!-- b000476 | prose | pages [37] -->
As(cm2) As_ture(cm2) branches h(cm)

<!-- b000477 | prose | pages [37] -->
Light incident π/3 angle ψ

<!-- b000478 | prose | pages [37] -->
Number of leaves

<!-- b000479 | prose | pages [37] -->
in the same height 20

<!-- b000480 | prose | pages [37] -->
of branch n

<!-- b000481 | prose | pages [37] -->
Table 7

<!-- b000482 | heading | pages [37] -->
3-D Model for Alternative Arrangement

<!-- b000483 | prose | pages [37] -->
Input data Output data True value Error

<!-- b000484 | prose | pages [37] -->
Semi-major axis

<!-- b000485 | prose | pages [37] -->
of a ellipse leaf 4.60

<!-- b000486 | prose | pages [37] -->
a(cm) Calculated Semi-minor axis True shadowed 1.70 shadowed area b(cm) 19.80 area per leaf 18.37 7.19% per leaf As_ture(cm2) Distance As(cm2) between two 2.00 levels of

<!-- b000487 | prose | pages [37, 38] -->
branches h(cm) Light incident π/3 angle ψ Number of leaves in the 20 same height of branch n

<!-- b000488 | furniture | pages [38] -->
Team # 14297

<!-- b000489 | furniture | pages [38] -->
Page 38 of 45

<!-- b000491 | prose | pages [38] -->
Table 8

<!-- b000492 | heading | pages [38] -->
3-D Model for Whorled Arrangement

<!-- b000493 | prose | pages [38] -->
Input data Output data True value Error Radius of a leaf 4.60 r(cm) Length of 2.00 Calculated True shadowed petiole x(cm) shadowed area 27.00 area 28.34 4.72% Distance As(cm2) As_ture(cm2) between two 1.2 levels of branches h(cm)

<!-- b000494 | prose | pages [38] -->
As can be seen from our result, the error between field data and the computational result is less than 7.5%. Hence, our hypothesis that leaf shapes minimize overlapping so as to maximize exposure was verified. To conclude, leaf shapes minimize overlapping as to maximize exposure and this statement matched the biological principle which is mentioned in the photosynthesis section.

<!-- b000495 | prose | pages [38, 39] -->
Speaking of profiles, is leaf shape (general characteristics related to tree profile/branching structure? As mentioned in Section 2.4, this model was constructed following principles of the mechanic equilibrium system. The hypothesis of this model is that the effective area of leaves would influence the branching structure.

<!-- b000496 | furniture | pages [39] -->
Team # 14297

<!-- b000497 | furniture | pages [39] -->
Page 39 of 45

<!-- b000499 | prose | pages [39] -->
Table 9

<!-- b000500 | prose | pages [39] -->
Tree Profile/Branching Structure under Wind Influence

<!-- b000501 | prose | pages [39] -->
Input data Output data Error

<!-- b000502 | prose | pages [39] -->
Wind resistance coefficient α 0.10

<!-- b000503 | prose | pages [39] -->
Blade area of a branch facing 90.00 the wind A(cm2)

<!-- b000504 | prose | pages [39] -->
Wind speed(m/s) 3.00 Torque from wind on the 0.0068 branch(N﹒m) Number of branches n 3

<!-- b000505 | prose | pages [39] -->
50

<!-- b000506 | prose | pages [39] -->
Length of each branch(cm) 20

<!-- b000507 | prose | pages [39] -->
10

<!-- b000508 | prose | pages [39] -->
0.6283

<!-- b000509 | prose | pages [39] -->
Measured angle(rad) 0.3927 6.53% 0.3142

<!-- b000510 | prose | pages [39] -->
0.015

<!-- b000511 | prose | pages [39] -->
shear modulus(GPa) 0.024

<!-- b000512 | prose | pages [39] -->
0.034 Torque from gravity on 0.0063 the branch(N﹒m) 0.25 Old segment branch 0.22 radius(cm) 0.20

<!-- b000513 | prose | pages [39] -->
0.15 New segment branch 0.12 radius(cm) 0.1

<!-- b000514 | prose | pages [39] -->
As can be seen from the result, the error is less than 7.5%. Also, all the simulation

<!-- b000515 | prose | pages [39] -->
data was in right order of magnitude, which means our model is applicable.

<!-- b000516 | furniture | pages [40] -->
Team # 14297

<!-- b000517 | furniture | pages [40] -->
Page 40 of 45

<!-- b000518 | prose | pages [40] -->
Estimate the leaf mass of a tree Two methods were presented to solve this problem. Theoretically speaking, the first approach should be able to give consideration to sufficient biochemistry and metabolic activities. Was it highly comparable, experimental conditions would be in good control and minimize both systematic and operational error. However, according to the experimental results so far, most results were inconsistent and had large variation. Hence, at this stage, we could not use those data to test our model. Although, with the development of new biological technology, the result will be much more consistent and comparable in order to better serve the modeling procedures (Heldt, 2011). 2) The second approach is obtained from the physical and structural properties to estimate the total leaf mass. From Section 2.4, we could see that it ended with a logical solution to the problem.

<!-- b000519 | prose | pages [40, 41] -->
Table 11 Crown Volume and Mass Estimation Input data Output data True value Error Radius of a 3.50 circle leaf r(cm) Length of 2.00 petiole x(cm) Maximum level True 10 of the crown volume Calculated volume 0.0857 of the 0.8021 7.12% Equivalent of the crown(m3) crown angle between 1.34 (m3) branch and trunk Number of leaves in the 20 same height of branch n

<!-- b000520 | furniture | pages [41] -->
Team # 14297

<!-- b000521 | furniture | pages [41] -->
Page 41 of 45

<!-- b000523 | prose | pages [41] -->
Diameter of the

<!-- b000524 | prose | pages [41] -->
cross section of 0.80 a branch d(cm)

<!-- b000525 | prose | pages [41] -->
Calculated total

<!-- b000526 | prose | pages [41] -->
mass of the 41.5178 Equivalent

<!-- b000527 | prose | pages [41] -->
crown(kg) length of the

<!-- b000528 | prose | pages [41] -->
branch in the 0.8768

<!-- b000529 | prose | pages [41] -->
Lowest level

<!-- b000530 | prose | pages [41] -->
l(1)(m)

<!-- b000531 | prose | pages [41] -->
Coefficient of

<!-- b000532 | prose | pages [41] -->
equivalent

<!-- b000533 | prose | pages [41] -->
length of the 0.90

<!-- b000534 | prose | pages [41] -->
branch form Calculated average bottom to top c density of the 0.593 Density of treeρ’(×103kg/m3) wood 0.90

<!-- b000535 | prose | pages [41] -->
ρ(×103kg/m3)

<!-- b000536 | prose | pages [41] -->
Acceleration of 9.80 gravity

<!-- b000537 | prose | pages [41] -->
As can be seen from the above data, the error is less than 7.5%, which provided

<!-- b000538 | prose | pages [41] -->
sufficient evidence to verify our estimation method.

<!-- b000539 | furniture | pages [42] -->
Team # 14297

<!-- b000540 | furniture | pages [42] -->
Page 42 of 45

<!-- b000541 | heading | pages [42] -->
Discussion

<!-- b000542 | prose | pages [42] -->
In this section, strengths and limitations of models constructed are discussed. In Section 2.1, shape functions are derived to quantify the distinctions between the representative leaves. These functions allow us to better control the properties of leaf shapes by applying traits parameters (e.g. blade area, cell-division margin) in the evaluation of bio-functions. However, it is still questionable how accurately these parameters can capture the structural and functional variations at organ levels. In the section followed, a series of mathematical models are derived to simulate the leaf expansion and three kinds of physiological activities in leaves. The photosynthesis model provides complete description about the process of sunlight harvesting and carbon dioxide assimilation. As for the transportation model, advanced algorithm are employed for precisely control the complex dynamic procedures and the analysis is highly comparable with other system of metabolic activities at the level of leaves.

<!-- b000543 | prose | pages [42] -->
Section 2.3 is where we start to extend the model to inter-organ relations and communications. To solve the overlapping puzzle, solid and plane geometry are adopted to find the intersection area of circles, which largely simplify the problem solving procedures without losing the basic biological intuition. The branch structure model considers both mechanical properties and the dynamic process of branch development. It builds connections with vital environmental factors (e.g. wind force) and further expands the model by catering for the inter-organ relationships. The models addressed in Section 2.4 develop a comparison between the physiological and structural approach in performing leaf mass estimations. Logical reasoning is derived in the way that associates the tree characteristics with leaf properties.

<!-- b000544 | prose | pages [42, 43] -->
Since our work in this paper majorly focus on the bio-functioning and communications within an ideal and isolated case, the consistency of results can be easily destroyed when encountering external shocks. Elements from eco-system could be taken into account if further work was carried out. These elements involve both the physical factors (e.g. sunlight, water, longitude) and inter-species relations (e.g. competition, pray). In such way, we could provide more accurate and comprehensive model in the future.

<!-- b000545 | furniture | pages [43] -->
Team # 14297

<!-- b000546 | furniture | pages [43] -->
Page 43 of 45

<!-- b000548 | furniture | pages [44] -->
Team # 14297

<!-- b000549 | furniture | pages [44] -->
Page 44 of 45

<!-- b000550 | heading | pages [44] -->
References

<!-- b000551 | heading | pages [44] -->
1. Howell, S.H. (1998). Molecular genetics of plant development Cambridge; New

<!-- b000552 | prose | pages [44] -->
York: Cambridge University Press.

<!-- b000553 | heading | pages [44] -->
2. Hemsley, A.R. & Poole, I. (2004). The evolution of plant physiology : from whole

<!-- b000554 | prose | pages [44] -->
plants to ecosystems Amsterdam; Boston: Published for the Linnean Society of

<!-- b000555 | prose | pages [44] -->
London by Elsevier Academic Press

<!-- b000556 | heading | pages [44] -->
3. Stern, K.R., Bidlack, J.E., & Jansky, S.H. (2008). Introductory plant biology

<!-- b000557 | prose | pages [44] -->
Boston : McGraw-Hill Higher Education

<!-- b000558 | heading | pages [44] -->
4. Greig-Smith, P. (1983). Quantitative plant ecology BLACKWELL SCIENTIFIC

<!-- b000559 | prose | pages [44] -->
PUBLICATIONS, OXFORD (UK).

<!-- b000560 | heading | pages [44] -->
5. Dickison, William C et al (2000) integrative plant anatomy published in Academic

<!-- b000561 | prose | pages [44] -->
Press

<!-- b000562 | prose | pages [44] -->
6. Adrian D. Bell & Alan Bryan(1991). Plant Form: an illustrated guide to flowering

<!-- b000563 | prose | pages [44] -->
plant morphology; Oxford (UK);

<!-- b000564 | prose | pages [44] -->
7. Van Volkengurgh, (1999) leaf expansion—an integrating plant behavior plant cell

<!-- b000565 | prose | pages [44] -->
and environment publication

<!-- b000566 | prose | pages [44] -->
8. J. I. Lizaso, W. D Batchelor, M.E Westgate (2002) A leaf area model to simulate

<!-- b000567 | prose | pages [44] -->
cultivar-specific expansion and senescence of maize leaves published in Field

<!-- b000568 | prose | pages [44] -->
Crop Research

<!-- b000569 | prose | pages [44] -->
9. William G. & Norman P.A H (2008) introduction to Plant Physiology  published

<!-- b000570 | prose | pages [44] -->
in University of Western Ontario

<!-- b000571 | prose | pages [44] -->
10. Christopher J. Kucharik, John M Norman, Stith T. GoWer (1998) Measurement of

<!-- b000572 | prose | pages [44] -->
branch area and adjusting leaf area index indirect measurements published in

<!-- b000573 | prose | pages [44] -->
Agricultural And Forest Meteorology

<!-- b000574 | prose | pages [44] -->
11. Marcelo Shoey de O M, Carlos Eduardo N C, Affonso G G & Helion Vargas

<!-- b000575 | prose | pages [44] -->
(2001) A simple model for the dynamics of photosynthesis published in Analytical

<!-- b000576 | prose | pages [44] -->
Sciences

<!-- b000577 | heading | pages [44] -->
12. Falkovich & Gregory  (2011) Fluid mechanics: a short course for physicists

<!-- b000578 | prose | pages [44, 45] -->
published in Cambridge ; New York : Cambridge University Press 13. Hironori Fujita and Atsushi Mochizuki (2006) The origin of the diversity of leave venation pattern published in Developmental Dynamics 14. W R N. Edenwards, P.G.Jarvis, J.J. Landscerg and H. Talbot (1986) A dynamic model for studying flow of studying of water in single trees published in Tree Physiology 15.  Peter Stiling (2001) ecology theories and applications published in University of South Florida 16. M.N.V Prasad (1996) plant ecophysiology published in New York 17. Walter Larcher (2003) physiology plant ecology – ecophysiology and stress physiology of functional groups published in Springer 18. Aaron M.E& Karl J N (1988)Branching patterns of salicornia europaea (chenopodiaceae)at different successional stages: a comparison of theoretical and real plants published in American Journal Botany 19.  Michael Hickey and Clive King (1997) common families of flowering plants published in Cambridge Press 20. Heldt, Hans-Walter (2011): plant biochemistry published in University of Amsterdan 21. Harold C Bold (1973) Morphology of plants published in Harper International Edition 22. Frank R. G, William P. F, Steven B H, Maurice D W (2009) A first course in mathematical modeling published in China Machine Press 23. Mark Allen Wesis (1997) Data structures and Algorithm Analysis in C published in Addison Wesley Longman 24. Daniel P, George C.T & Ruey S T (2001)A course in time series analysis published in a wiley-interscience

<!-- b000579 | furniture | pages [45] -->
Team # 14297

<!-- b000580 | furniture | pages [45] -->
Page 45 of 45
