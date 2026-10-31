Summary

Leaf shape plasticity has long been a heated topic in the field of morphology and taxonomy. Although numerous researchers have been involved in the study of how the shape formation is controlled by genes and environmental stress, little has been done to address the interactions between different plant organs. In this paper, we approach this issue in a creative way: starting from isolated parts (leaves), building connections (leaf-leaf, leaf-branch) and drawing the big picture of the entire system (tree).

The mathematical model introduced in this paper describes morphological, physiological and partially ecological properties of the vegetations. First and foremost, relative errors of the numerical outputs are limited within 7.5% and all the values predicted are within the right order of magnitude. Moreover, biological intuition is presented in the consistent manner. For instance, the dynamic positive feedback is applied to describe leaf growth pattern and transportation process. It is also worth noticing that a much simple and flexible algorithm is achieved by executing ingenious geometric strategy.

Interestingly findings were generated in the procedures of solving the problems. The seemly unrelated bio-phenomena could be explained when morphological, physiological and partially ecological interactions were taken into account. To illustrate, as we conducted the leaf mass estimation, it could give us a rough picture of leaf-leaf, leaf-branch, and leaf-tree relations.

Dear editor,

The topic of this paper is about mathematical modeling of tree leaves as well as how

leaf traits impose influence on the tree system.

In this paper, we addressed the morphological, physiological and partially ecological

properties of the vegetations by applying a series of modeling process to related issues.

The performance of our model in the sensitivity test satisfied our expectation.

Different from the previous research, we approached this issue in a creative way:

starting from isolated parts (leaves), building connections (leaf-leaf, leaf-branch) and

drawing the big picture of the entire system (tree).

Interestingly, the seemly unrelated bio-phenomena could be explained when

morphological, physiological and partially ecological interactions were taken into

account. Properties of the individual leaves are closely related to the characteristics of

the entire tree system.

We are looking forward to your comments and revision. Hopefully, our paper could be

published in this Journal.

Your sincerely

Introduction

The mechanism of plant shape plasticity has long been a topic of numerous researches in the field of morphometrics. And leaves have been always favored as the subject because of its two-dimensionality and relative simplicity. The change of leaf shapes are generally regarded as both a genetically determination (Howell, 1998) and results of structural optimization to environmental stress (Hemsley and Poole, 2004). However, little attention is drawn to the interactions between different plant organs (e.g. leaf, branch) and the influence from the system as an entity. To fill this gap, we construct a mathematical model to interpret such in-leaf communications, and perform our analysis on simple leaves.

As is shown in some literatures (Stern et al., 2008), simple leaves are classified into different shape catalogs (Figure 1), such as flabellate leaves (e.g. ginkgo), palmate leaves (e.g. maple), and cordate leaves (e.g. Hibiscus tiliaceus). The major criteria of classification are the shape apex, base, and margin of leaves.

Leaf venation is also a critical component of leaf types. There are three major patterns of major vein organization: pinnate, palmate, and parallel, as are shown in Besides the diversification in leaf shapes and venation, arrangement of leaves on a stem (phyllotaxy) are generally in three distinct patterns (Figure 3), which are defined by the number of leaves attached to a single node. In most species, leaves are attached alternately or in a spiral along a stem, with one leaf per node. This is called an alternate arrangement. If two leaves are attached at each node, they provide an opposite arrangement. Leaves are whorled when three or more occur at a node. A special case in opposite arrangement is called decussate, if successive pairs are orientated at 90o to each other.

Review of previous researches shows that most models developed are based on statistical results (Greig-Smith, 1983). And so far, no model is built to indicate the effect of plant organ interactions (leaf-leaf, leaf-branch) on leaf shapes. The mathematical model presented by us demonstrates the logic of plant-environment and in-plant communications at physiology, inter-organ, and tree system levels. We first start from isolated parts (leaves), build connections (leaf-leaf, leaf-branch) and end with the big picture of the entire system (tree).

Problem A requires mathematical modeling of tree leaves as well as how leaf traits impose influence on the tree system. It is suggested that shape factor of individual leaves to be analyzed via the following aspects.  Influencing elements of leaf shapes;  Inter-leaf relations (i.e. overlapping between leaves)  Branch-leaf relations  Tree-leaf relations (i.e. estimating mass of leaves) The model used should be able to capture not only the characteristics of single leaves but also their interactions with other plant organs and eventually the tree system. We have to start from isolated parts (leaves), build connections (leaf-leaf, leaf-branch) and end with the big picture of the entire system (tree).

We divide the modeling section into four subsections.  Section 2.1: Descriptive model of leaf traits;  Section 2.2: Model of cell growth & physiological activities;

(photosynthesis, transportation, transpiration)  Section 2.3: Model of leaf arrangement & branching structure;  Section 2.4: Model of the tree characteristics.

(ATP governing equation, Driving Force governing equation) The first two subsections of modeling are for analysis at leaf level. To quantify the geometric characteristics of various leaves, shapes are described by functions and curves are placed in Polar Coordinates, so that differences can be visualized. Parameter selection can then easily adjust the leaf shapes, thus providing more flexibility in deriving the bio-features such as size and perimeter. As for the shape influencing factors, processes of growth and photosynthesis are assumed to determine the effective blade area of leaves, while plant transport system and transpiration are closely related with leaf venation. These physiological activities are modeled in Section 2.2.

At the branch level in Section2.3, arrangements of leaves and branches are taken into account. We compute the overlapping area of leaves via geometric analysis. Since finding the area of irregular shadow region is troublesome and not easily compared, we standardized the computation by using round circles as equivalents to diverse leaf shapes. The angle over the two opposite leaf-edges is taken as indicators for leaf types. Tree profile is modeled by rod-based method (LA system). In Section2.4,by solving the two governing equations for ATP and driving force, tree height and angles of shoot can be derived, which will be then applied to compute the volume of the tree. Eventually, traits of isolated leaves and the tree are linked together.

The Models

2.1 Descriptive Model of Leaf Shape

In Section 2.1 we present several kinds of leaf shapes to describe some mostly-seen single leaves. Although shapes of tree leaves can be in great variety, the classification discussed here only applies to selected types of single leaves, which are flattened, colored in green, and spinelike, regardless of textures. Leaves that are tubular, feathery, cup-shaped, or needlelike require 3-dimensional models and are not taken into account for simplicity purpose. In Table 2.1, some of the typical plant and their leaf shapes are listed before we transform their morphological features into the language of mathematics.

Type of Leaf Representative Plant Shapes Nasturtium Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Orbicular Class: Magnoliopsida – Dicotyledons Order: Geraniales Family: Tropaeolaceae – Nasturtium family Genus: Tropaeolum L. – nasturtium Eastern redbud Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Cordate Order: Fabales Family: Fabaceae – Pea family Genus: Cercis L. – redbud Species: Cercis canadensis L. – eastern redbud Spadeleaf Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Reniform Order: Apiales Family: Apiaceae – Carrot family Genus: Centella L. – centella Species: Centella asiatica (L.) Urb. – spadeleaf Cassava Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Lobed Order: Euphorbiales Family: Euphorbiaceae – Spurge family Genus: Manihot Mill. – cassava Species: Manihot esculenta Crantz – cassava Wine Grape Kingdom: Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Palmate Order: Rhamnales Family: Vitaceae – Grape family Genus: Vitis L. – grape Species: Vitis vinifera L. – wine grape Tea Kingdom : Plantae – Plants Division: Magnoliophyta – Flowering plants Class: Magnoliopsida – Dicotyledons Elliptic Order: Theales Family: Theaceae – Tea family Genus: Camellia L. – camellia Species: Camellia sinensis (L.) Kuntze – tea Maidenhair Tree Kingdom: Plantae – Plants Division: Ginkgophyta – Ginkgo Class: Ginkgoopsida Flabellate Order: Ginkgoales Family: Ginkgoaceae – Ginkgo family Genus: Ginkgo L. – ginkgo Species: Ginkgo biloba L. – maidenhair tree

These leaf shape types are described by functions with adjustable parameters.

Plotting their curve functions with specific coefficients in Polar Coordinates, we can

visualize differences between shapes. To quantify such differences, we derive the

expression of leaf area A as well as length of leaf margins S , by finding the following

integrals.

 rdrd A

 rd S It should be noted that S refers to the part of leaf margin where cell division

occurs, rather than the perimeter of the blade. In Figure 1 to 6, this portion is

illustrated by the black edge of the shape curves, and the red nod at the origin denotes

the auxin sink of the leaf.

 Type 1: Orbicular leaves

Shape of an orbicular leaf is a round circle, and can be written as

a   0 r a , (1) where a interprets the radius of the leaf.

By integration, we can find the size and cell-division margin length of orbicular

leaves

  2 1A a (2)

  S 2 a (3) 1

 Type 2: Cordate leaves & Reniform leaves

The shapes of cordate and reniform leaves have a lot in common, with the

former one shapes like a heart and the latter a kidney. Such features can both be captured by a trigonometric function.

a     0 , (4) r a (1 cos )

Size of Leaf area and cell-division margin length are

 2 3 a  (5) A 2 2

     S 2 a (6) 2

 Type 3: Lobed leaves, & Palmate leaves

Another form of trigonometric function is used to describe lobed and palmate

leaves. We can adjust the range of parameter to control the indentation of

margins.

  k (7) r a b sin( )

where a, b are both positive constants, k are natural numbers indicating the

amount of lobes.

Area and margin length of leaves

  b  2 2 A ( a ) (8) 3

  S 2 a (9) 3

 Type 4: Elliptic Leaves

Leaves of this type are oval-shaped, which is expressed by a pair of symmetric

trigonometric functions (10).

1 1 (sin         a cos ) 4 2 ( a  0 )               (10) 1 3         a (sin cos ) 2 4

The cell division accounts for a proportion much larger than the none-division

part (i.e. the black edge in Figure 5), and can be ignored when we compute the

margin length S .

Area and cell division margin length of the leaf are

  1 1    2 A a (11)   4  4 2 

       S 2 a sin( k ) cos( k ) 1 (12) 4

 Type 5: Flabellate Leaves

Flabellate leaves are fan-shaped, which can be resembled by a sector of a pie.

By changing the central angle and radius, the leaf shape can be adjusted. It is

described by function (13).

      r a k k , (13) 1 2

2k are constants defining the domain of the central angle . 1k , where

The following graph illustrates the shape of flabellate leaves by taking the radius to be 5, and central angle 1 3      . 4 4

Area and margin length of leaves are shown below.

  k a  2 (14) A 2( k ) 5 2 1     S ( k k a ) 2 a (15) 5 2 1

2.2 Model of cell growth and physiological activities

2.2.1 Growth Model

Given the prominence of leaves in our environment and their importance for plant function, it is surprising that so little is known about the physiological process developing these organs. Most studies of leaf function have focused on photosynthetic capacity, light interception, and responses of leaves to the environment. However up to the current time, there is no exactly biological theory that could explain the inner mechanism of cell growth.

Many factors contribute to the regulation of cell growth, involving biophysical considerations, wall extension, osmotic regulation, photobiological control of ion fluxes, and other extraneous factors in the environment (Van Volkengurgh, 1999).

Our model for leaf expansion is derived from the one proposed in the work of Lizaso et al. (2002), but improves the original version by including cell division along the leaf margin. The sigmoidal logistic model is applied to fulfill the basic requirement of cell growth model and to simulate the process of leaf expansion.

LA by a sigmoidal Lizaso et al. (2002) show the expansion of each leaf blade i logistic function:

Ae  (16) i LA i e  ke t te ( ) 1 i i

Ae is the final surface area of the ith leaf, te is the thermal time when the leaf where i i reaches 50% of its final area.

ke , we define this term as a polynomial of Differing from Lizaso’s definition of i degree n about the length of cell-division leaf margin S :

n  i (17) ke a S i i  i 0

GR ei Daily calculation of leaf expansion is conducted in the form of growth rate of

each leaf at thermal timet . The result is obtained from the first derivative of (1):

  ke t te ( ) dLA e i i   (18) i GR e ( Ae ke ) (1 i i i    ke t te ( ) 2 dt e ) i i

Ae is the final area of leaf blade. where parameter i

2.2.2 Model for physiological activities

In this subsection, we devote our interest to the structure of leaves and how those structures are adapted to carry out effectively certain physiological and biochemical functions. Three types of physiological activities are modeled and evaluation of their effects on leaves’ shape characters is performed. These physiological functions are photosynthesis, substance transportation, and transpiration.

Photosynthesis: Energy Conservation

Photosynthesis is the primary function of green vegetation which allows the plant to conserve solar energy to stable chemical form (William & Norman, 2009). After the photosynthesis machine generates utilizable energy, ATP is provided to the whole plant. To absorb light efficiently, leaves usually present a large surface area to the incoming sunlight. And the effective area is to a great extent associated with the efficiency of photosynthesis. The physiological and biochemical functions of leaves are targeted in our model at the same time.

We model the energy conservation process by simulating its two stages: Light-dependent reactions and CO2 assimilation.

 Harvesting sunlight

A series of steps, called light-dependent reactions describe how chloroplasts conserve energy from sunlight to ATP and reducing potential (as NADPH). The biological principle followed in this stage is that plant leaves are photosynthetic machines that maximize the absorption of light. This principle is the guideline of our model constructing procedures. It also applies to our model construction in Section 2.3 when considering leaf overlapping.

The efficiency of photosynthesis denoted by  can be estimated by a function of

incident light intensity I and the probability of radiation penetration in forest canopies P , where P can be expressed as a function of the zenith angle:

   (19) I P ( )

The intensity of incident light I is generated from the Black-radiation formula in general physics, which is expressed by the following equation:

 5 k  I (20) c  e 1 kT

where k is the Boltzmann constant; is the wavelength; is the Planck constant; c is the speed of light; and T is the absolute temperature of the black body.

Radiation penetration probability P is developed based on the work of Chen et al. (1997a). It is the probability of a direct bean penetrating through a forest at zenith angle 

      K ( ) ( ) L   P ( ) exp e (21)       (1 )cos( )   e

 e  ( ) where L is the Leaf Area Index (LAI); is the canopy non-randomness index;

eis a correction factor for within-shoot clumping in conifers; is the woody-to-total foliage hemi-surface area ratio in the canopy and can be numerically demonstrated by:

W  (22)  W L

where W is the total woody hemi-surface area index of branches and stems.

 CO2 assimilation

Photosynthetic gas exchange between leaf and air is controlled by the opening and closing of stomata, where photosynthetic carbon reduction (PCR) cycle occurs. We focus on the CO2 assimilation process: how CO2 enters the leaf and subsequently is reduced through the utilization of the NADPH and ATP produced by photosynthetic electron transport.

The assumption is made that the production ratio of CO2 over O2 is taken as 1. We model the time dependence of CO2 assimilation by a set of differential equations proposed by Marcelo et al. (2000). The model is divided into three parts. The number of CO2 receivers and excited receivers are determined by concentration of CO2 and radiant flux intensity. The amount of product, substance and complex can be all predicted by time-dependent differential equations. The product can be seen as one kind of indicator to demonstrate how much energy has been generated by the plant.

 Part A

Two main phenomenological differential equations are introduced for the number of light excited receiver N t and the quantity of CO2 receivers M t , respectively: ( ) ( )

dN t ( )      (23) k I N N t ( ) k M t N t ( ) ( ) 1 r max 2 dt dM t ( )      (24) k C M M t ( ) k M t N t ( ) ( ) 3 max 4 dt

1k , 2k , 3k ,and 4k are phenomenological parameters; N where is the total number max rI is the radiant flux intensity; C is the concentration of of light excited receivers,

M CO2 in the mesophyll, and is the total number of CO2 receivers. max

 Part B

Marcelo et al. (2000) show another equation for result comparison. This equation

involves the assimilation of CO2 in closed measurement system:

dC t ( )      (25) k C t ( ) 1 m t ( ) k 5 6 dt

6k where represents the effect of CO2-production by photorespiration,

M t ( )      k 5 1 m t ( ) , and the term represents the effect of CO2 reduction on m t ( ) M max

the CO2 concentration of the measurement system.

 Part C

To formulate the enzyme reaction equations, the following set of differential

equations are constructed:

dp t ( )  (26) k se t ( ) 7 dt

dse t ( )     (27) k s t ( ) ( k s t ( ) k k se t ) ( ) 8 8 8 7 dt

ds t ( )    (28) k s t ( ) ( k s t ( ) k se t ) ( ) 8 8 8 dt

7k and 8k are the rates of the reactions; where p t is the product; s t is the ( ) ( )

substrate; and se t is a complex. ( )

The amount of product will be shown in the governing equations in Section 2.4 to

estimate the properties of the whole tree system.

Transportation

Nutrient salts, ions, and steroids are of vital importance to the growth and development of plants. Take auxin as an example, which is a kind of plant hormone, plays a central role in the in-plant activities including vascular development. The uptake of these substances by plants involves various types of transportation procedures like simple diffusion, facilitated diffusion, or active transportation. Facilitated diffusion and active transport are mediated by channel and carrier proteins, of which the latter requires a source of metabolic energy, normally in the form of ATP.

We model the auxin-transport system since it captures all the related elements in the transport activities — the transport channel, the carrier, and the energy consumed. Another notable reason for our choice is that the auxin model has the least number of disturbing factors, like the potential distinction between external eco-system and the internal environment of the plant to list a few.

Leaf venation patterns are used to describe the transportation behavior. To support this view point, we provide the following reasons.

 According to fluid mechanics, after divided by the efficiency of transportation mechanism, the flux of auxin in the veins could reflect the distribution of transportation channels (Falkovich et al, 2011).

 In order to make this model comparable with the photosynthesis process which occurs only inside the chloroplast of leaves, transportation activities should also be analyzed by observing the section structure of isolated leaves.

Hence, the geometric traits of leaves, in this case cell-division margin and size, become the determinant factors in the physiological mechanism. This matches the intention of out model to start from individual units and extend it to the entire system by simulating the in-plant communication.

Here we adopt the approach proposed by Hironori and Atsushi (2006), which examine the formation of leaf venation patterns by modeling the positive feedback

regulation between plant hormone auxin and its efflux carrier. And the mathematical

model is presented below.

Individual cells are aligned as two-dimensional hexagons, with position of the cell

denoted byi and j , which are two independent directions of the hexagonal cell.

Another indicator k represents the cell membrane side of the cell. Auxin and auxin

efflux carrier are located in each side of the cell membrane, respectively.

Assuming auxin outflow from the k-th side of cell membrane of the( , ) i j cell to the

adjacent k’-th side of the( ', ') i j cell is proportional to the product of auxin efflux

carrier p and auxin a densities, the auxin flow between neighboring cells f ijk ijk ijk

can be obtained by the difference in the auxin outflows from the two cells:

  f cp a cp a (29) ijk ijk ij i j k ' ' ' i j ' '

where c is a constant.

The differential equations for the dynamics of auxin efflux carrier p and auxin ijk

a are described in the following form: ijk

dp g f ( ) ijk  ijk  s d p (30)  p p ijk dt g f ( ) ijk k

da  dt  ij  (31) s d a f a a ij ijk k

g f ( )  ijk g f ( ) (32) ijk     1 exp[ ( f f )] ijk 0

as is the ps is the carrier synthesis rate; d is the carrier degradation rate, where p d is the auxin degradation rate; , ,  auxin synthesis rate; f cs s / ( d d ) are a 0 p a p a

constants, and g is an increasing function of auxin flow.

Transpiration

Transpiration is the process that large amounts of water are lost by plants through evaporation from leaf surfaces. It is driven by differences in water vapor pressure between internal leaf spaces and the ambient air. A variety of factors influence transpiration rate, including temperature, humidity, wind, and leaf structure. Water is conducted upward through the plant primarily in the xylem, a tube-like system of treachery elements. And lost water by transpiration is replenished by the absorption of water from the soil through the root (Figure 1). It is worth noticing that transpiration process provides the principle driving force to the operation of the whole plant system (William & Norman, 2009).

Water movement in xylem is driven by transpiration and the resulting tension in the water column which is maintained because of the high tensile strength of water. Following this statement, we construct the transpiration model via the approach taken by Edwards et al. (1986). While he modeled flow of water in a single tree was

modeled in terms of the Darcy equation using a set of four compartments: root, stem,

branches, and leaves, we only consider transpiration through xylem.

Assumptions presented by Edward et al. (1986) are also adopted:

1) Water moves in the plant from points of high potential to points of low

potential, along pathways that exert a frictional drag or resistance to flow.

2) Flow in the xylem of plants is adequately represented by the Darcy equation.

3) The relative conductivity of the xylem is a unique function of the proportion

of void volume filled with water (i.e. relative water content).

4) The proportion of void volume that is water-filled is a function of the water

potential of the tissue.

5) Axial flow in the stem is confined to the sapwood which has uniform

proportions of void and woody metric volumes

6) The cross-sectional area of sapwood in the stem is a function of height.

7) The leaves, branches and roots are not subdivided but are treated as uniform

compartments attached in series to the clear stem.

8) At any moment, temperature is constant throughout the system.

Functions describing the process of transpiration are derived as following. The

Darcy equation defines axial flow Q by

 KA  (33) Q l

where l is length; A is the cross-sectional area; is the potential difference; K is

the relative conductivity of the sapwood;is the viscosity of the sap.

Within each component, the flow resistance R was defined by rearrangement of (33) as

  l   (34) R Q KA

In the absence of flow, water potential is directly related to the height of measurement z above a reference level (taken to be ground level) through the effect of gravity, as follows:

  (35) z g

where is the density of water and g the acceleration due to gravity.

2.3 Model of leaf arrangement & branching structure

2.3.1 Leaf arrangement

The biological principle states that plant leaves are photosynthetic machines that maximize the absorption of light. Thus to minimize overlapping individual shadows and achieving the maximum exposure, leaves have evolved the optimal response to mix of environmental elements. Among such evolutionary features, leaf shape and phyllotaxy are two critical traits that affect the interactions between leaves. In this section, inter-leaf relations are examined in terms of position arrangement on the stem. And such arrangement determines the angle of the petioles. Here we present two types of models applying to different dimensions. The 2-D model assumes that sunlight is perpendicular to the ground surface, thus leaves at different level spots can be projected to a 2-D plane (Figure 12). The model can be extended to 3-D cases by adding the angle of incidence of sunlight.

 Two-dimensional modeling

To simplify the computation of overlapping areas and add more comparability, we

standardize various shapes into their circumcircles with the equal-length radius, and

the overlapping area can be obtained by finding the intersection of two circles in plane

geometry (Figure 13).

    OCA O CA We denote the radius of circles as r ; length of petiole as x ; ; 1 2

     AOO BOO O F m ; 1 2 1 2 1

Area of intersection is written as m     1 2 2 2 (36) A 2cos ( ) r 2 m r m shade r    where r is the radius of the circles; . m ( r x )sin

The overlapping conditions are sorted into two general catalogs: convex-margin leaves and concave-margin leaves. For leaves with convex, the overlapping area is estimated by calculating the area of the shaded region, while for concave-margin leaves, overlapping area is computed by adjusting the area in shadow with a ratio  related to the included angle ( 2) of the two petioles (Table 1). ( )

Convex-margin Leaves Concave-margin Leaves

   A A A ( ) A overlap shade overlap shade The area exposed under sunlight can be derived as the difference between total size of leaves and sum of the overlapping regions.

    A A A (37) exposure i overlap where A is the size of a single piece of leaves.

 Three-dimensional modeling

In the 3-D model, the position of leaves in branch and tree volume will be transferred into two indicators: height and angle. Some assumptions embedded in the three-dimensional model of phyllotaxy are listed below:

 Vertex (i.e. leaves at top-ends) is not considered

 The distance ( h ) between adjacent nodes is large enough.

 Number of leaves ( n ) is large enough.

Consider the height and interactions of leaves, and take the elliptic leaf as an example, the overlapping area can be derived under different leaf arrangement patterns. Assuming an anglebe the inclination of angle of direct solar beam. a andb

are the semiminor and semimajor axis of the elliptic leaf; s is the width of area without shadow casted by the leaves above, and is denoted by the formula   (38) s h cot

Observing the effect of leaf arrangement on the overlapping areas, situations for alternate and opposite arrangements are quite similar, while the whorled arrangement is taken as a special case if the last two assumptions are fulfilled (Table 2).

Alternate Opposite

Whorled

Overlapping areas for the three arrangements are formulated by   2 2 2 n s a ( b )    (39) A n ab alt 4 ab  2 n s a    (40) A n ab opp 2 b      2 (41) A 2 s x ( r ) s whr

A , A where A , denote the overlapping areas for alternate, opposite, and alt whr opp whorled arrangement, respectively.

2.3.2 Branching structure

In this subsection, we use the LA system model, which is one kind of rod-based model to simulate the growth of branches. Development of branching structure is largely influenced by various ecological factors, among which “wind can be an important mortality factor to branch structure” as stated by Stiling (2002) in the book Ecology. The guiding principle of the model is to find the most stable cases by classical mechanics. In the model constructing process, two critical elements are taken into account, namely branch growth tendency and effective leaf area. Mostly, leaves area is probably the variable that has the largest influence on branch structure in the evolution history, since in the vegetation life span, branches and leaves develop inter-dependently (Walter, 2001). The list of assumptions for this model is provided:

 Branch structure will exist in the most stable case;

 Leaves in each branch are identical in size, and distributed uniformly;

 All branches are rigid;

 All the leaves are located at the end of branches. Since the growth of a plant axis is subject to the external force oriented in the direction of the preferred tendency of growth, we first develop the formula describing force of wind by   F Av (42) wind where A is the effective area of leaves; v is the constant speed of wind.

 The torque of the wind force is expressed as wind

      Av l cos( ) (43) wind i i

iis the angle between segments i and i-1. il is the length of segment i, and where

The torque exerted by an individual spring is shown as

   k (44) i i i x x x

xiis the rotational displacement due to external where xik is the spring constant;

forces.

To maintain the stable, the two torque must be equal

   (45) wind i x

The rotational displacement can be obtained by solving (10)

1      (46) Av l cos( ) i i k x i x

Each new layer that is added to a segment has a unique spring constant which can

be used to calculate the overall spring constant at that point. The spring constant about

the x-axis at joint i for an individual layer m is calculated by

E I  i i 1  k (47) x x i l xm  i 1

il is the length of where xiE is the shear modulus of the material about the x-axis, 1

segment i-1 that rotates about joint i, and iI is the torsional constant of the layer 1x

about joint i.

We assume the new layer to be a hollow ring, and the torsional constant iI is 1x

calculated using the formula    4 4 (48) I ( R r )    i 1 i 1 i 1 2 x

iR is the distance from the center of the cross-section to the outer edge of the where 1

ir  is the distance from the center of the cross-section to the inner edge of layer and 1 the layer. We have obtained the computation results about the x axes. For y and z axes,    4 4 (49) I ( R r )    i 1 i 1 i 1 4

2.4 Model of the tree characteristics

Generally speaking, in the early stage, characteristics of a tree such as height, volume and mass relate positively with the mass accumulation of leaves. As we know, almost all structures of the tree, including leaves, stems, branches, and root, will growth simultaneously, although at various growth rate. It is also possible for us to find the inner link between them by the governing equations based on the vital physiological activities mentioned in Section 2.2.

However, after the tree researches maturity, the observable relationship between the size of the tree and leaf mass will fade way. This is because that the percentage of dead cells in xylem will end up being the major part of the tree. The metabolic activities will demonstrate seasonal pattern instead of strict positive correlations. And the environmental factors will outweigh the inner traits of the plant and reshape some of the biophysical features. Hence, out model is restricted to the early stage of trees.

Two distinct modeling approaches are addressed in this subsection: physiological and structural. And we will demonstrate and evaluate both models respectively.

 Physiological Approach

We have talked about the energy conservation balance and the driving force operation in Section 2.2. By applying the bio-mechanism of metabolic energy cycle and inner force equilibrium, two governing equations can be obtained.

Assumptions adopted by this approach are:

(1) Photosynthesis is the only energy source for plant functioning.

(2) Transpiration mechanism is the only driving force generator for the active transportation plant.

The energy transformation function is derived by describing the process of ATP

production and consumption. The left-hand-side represents the ATP produced by

photosynthesis; and the right-hand-side equation is the amount of energy consumer,

both are in Joule.

       (50) nA P n Q f h

where n is the unit of ATP; P is the product of photosynthesis; A is the total

effective leaf area; Q indicates total flow in transpiration; f indicates total flow in

transportation; h is the height of the tree; is the amount of ATP consumed in other

activates; and , ,are constant coefficients.

The equilibrium condition reached by the driving force (i.e. transpiration can

provide sufficient driving force needed by the substance transport process) in the plant

system is presented by

     (51) n ' Q ' f h '

, are constant coefficients. where ' '

The height of tree ( h ) can be solved by solving the equation set (51) & (50).

However, this approach is almost impossible to carry out, since we may never

obtain the precise value of the coefficients in the equations and it is of great difficulty

to quantify the elements presented in the above equations.

 Structural Approach

 Tree Volume Estimation

To estimate the volume of the tree, we resemble the cone-shaped tree as round platforms piling up. These platforms can be generated by rotating the branches around

the tree trunk, with the curved surface indicating the route of branch-top leaf piece

wiping through the air (Figure 1).

We then compute the volume of single platform by

 l 2 iT   r  (52) V T (2 x 4 ) i  sin

 where r is the radius of leaves’ blade; T 2 r ; x is the length of petiole; l is the

 ); is the equivalent angle between the l l equivalent length of the bottom branch ( 1

branch and tree trunk.

  The volume of the tree is thus the summation the platform volumes till l 2 iT 0

 V V (53) tree i

 Tree Height Estimation Illustrated in Figure 14, the height of a single platform can be expressed by

    ih 2 sin r T sin (54)

Therefore, height of a tree is obtained by

     H l cos h h (55) tree i trunk

h where is the height of tree trunk. trunk

 Leaf mass Estimation

In order to reach equilibrium, the function which represents gravity moment used

by Aaron & Karl (1988) express the mass function at bending moment by

   2 2 (56) M d l Pg sin 2 bending 

where d is the diameter of branch’s cross section; l is the length of branch; P is

the mass of tissue; is the rotation angle; is the bifurcation angle.

The gravity function of mass is written as

2 l   (57) M cos( ) M g G 0 2

M is the mass of leaves on a single branch. where 0

The equal relation is then derived by applying the bending movement principle in

engineering

 M M (58) bending G

By rearranging (9), we can obtain the mass of leaves on a single branch   2 2 d P sin 2  (59) M 0   cos

The total mass of leaves for a tree is derived by

 M M N (60) 0 branch

N where the max value of is the number of branches of the tree, which can be branch

represented by i in the estimation of tree volume.

l  (61) max N branch 2 T

Solutions and Results

In this section, we describe in detail how the problem can be solved by applying the mathematical model built in the previous section. Since thorough descriptions have been given on the modeling process and the biological or physiological interpretations behind it, we will focus on testing how accurately the models can capture information in practice. Why do leaves have various shapes?

While previous literatures mostly take the development of leaf shapes as governed by genetic elements or the result of structural optimization to environmental stress, in this paper we drew more attention to the interaction between plant organs. To answer this question, we examined the impact of cell growth and physiological activities on the formation of the leaf’s blade area and its venation patterns. The growth model simulates the leaf expansion process and proposed a positive correlation between the size of blade area and cell-division margins. Physiological activities discussed in Section 2.2.2 starts from a microscopic functioning of inner leaf structures, showing evidence supporting the optimal selection of physiological features and suggesting necessity of in-plant communications. The evaluation of the models presented in Section 2.2 was conducted by running regression analysis of variable correlations. Data were sourced from the university biological department and ecology labs. Figure 1 and 2 show the regression results of the Growth Model and the ATP determine function in Photosynthesis models. It is observable that most data points fit quite well on the estimated function curves, which suggests a satisfactory accuracy level of the model constructed.

parameter 0.05

0.04

0.03

kei 0.02

0.01

0.00 10 15 20 25 30 35 S (perimeter) (cm)

ATP

10000000

8000000

6000000 product (J) 4000000

2000000

0

0 20 40 60 80 100 120 140 160 180 200 time (min)

In order to test the transportation model, we applied the graph theory and the basic

data structure method to conduct algorithm on the dynamic positive feedback

networking (Mark Allen Weiss 1997). In this process, finite volume method was in

use to solve the time-dependent differential equation. The following picture

demonstrated results of our model. Graph comparison with field data, (Adrian D. Bell

1991) verified our model.

Do leaf shapes minimize overlapping so as to maximize exposure?

In Section 2.3, 2-D and 3-D models were constructed which linked the general shape

features with the size of overlapping regions. Our hypothesis stated that leaves

develop its shapes to optimize the utilization of sunlight. To test this hypothesis, we

compare computational output with experimental results.

Table 5

2-D Model

Input data Output data True value Error

Radius of a 5.00 leaf r(cm)

Length of Calculated 1.20 True shadowed petiole x(cm) shadowed area 51.00 47.22 6.93% area As_ture(cm2) As(cm2) Number of

leaves in a 8

circle Table 6

3-D Model for Opposite Arrangement

Input data Output data True value Error

Semi-major axis

of a ellipse leaf 4.60

a(cm)

Semi-minor axis 1.70 b(cm)

Distance between Calculated True shadowed

two levels of 2.00 shadowed area 18.90 area 20.10 5.00%

As(cm2) As_ture(cm2) branches h(cm)

Light incident π/3 angle ψ

Number of leaves

in the same height 20

of branch n

Table 7

3-D Model for Alternative Arrangement

Input data Output data True value Error

Semi-major axis

of a ellipse leaf 4.60

a(cm) Calculated Semi-minor axis True shadowed 1.70 shadowed area b(cm) 19.80 area per leaf 18.37 7.19% per leaf As_ture(cm2) Distance As(cm2) between two 2.00 levels of

branches h(cm) Light incident π/3 angle ψ Number of leaves in the 20 same height of branch n

Table 8

3-D Model for Whorled Arrangement

Input data Output data True value Error Radius of a leaf 4.60 r(cm) Length of 2.00 Calculated True shadowed petiole x(cm) shadowed area 27.00 area 28.34 4.72% Distance As(cm2) As_ture(cm2) between two 1.2 levels of branches h(cm)

As can be seen from our result, the error between field data and the computational result is less than 7.5%. Hence, our hypothesis that leaf shapes minimize overlapping so as to maximize exposure was verified. To conclude, leaf shapes minimize overlapping as to maximize exposure and this statement matched the biological principle which is mentioned in the photosynthesis section.

Speaking of profiles, is leaf shape (general characteristics related to tree profile/branching structure? As mentioned in Section 2.4, this model was constructed following principles of the mechanic equilibrium system. The hypothesis of this model is that the effective area of leaves would influence the branching structure.

Table 9

Tree Profile/Branching Structure under Wind Influence

Input data Output data Error

Wind resistance coefficient α 0.10

Blade area of a branch facing 90.00 the wind A(cm2)

Wind speed(m/s) 3.00 Torque from wind on the 0.0068 branch(N﹒m) Number of branches n 3

50

Length of each branch(cm) 20

10

0.6283

Measured angle(rad) 0.3927 6.53% 0.3142

0.015

shear modulus(GPa) 0.024

0.034 Torque from gravity on 0.0063 the branch(N﹒m) 0.25 Old segment branch 0.22 radius(cm) 0.20

0.15 New segment branch 0.12 radius(cm) 0.1

As can be seen from the result, the error is less than 7.5%. Also, all the simulation

data was in right order of magnitude, which means our model is applicable.

Estimate the leaf mass of a tree Two methods were presented to solve this problem. Theoretically speaking, the first approach should be able to give consideration to sufficient biochemistry and metabolic activities. Was it highly comparable, experimental conditions would be in good control and minimize both systematic and operational error. However, according to the experimental results so far, most results were inconsistent and had large variation. Hence, at this stage, we could not use those data to test our model. Although, with the development of new biological technology, the result will be much more consistent and comparable in order to better serve the modeling procedures (Heldt, 2011). 2) The second approach is obtained from the physical and structural properties to estimate the total leaf mass. From Section 2.4, we could see that it ended with a logical solution to the problem.

Table 11 Crown Volume and Mass Estimation Input data Output data True value Error Radius of a 3.50 circle leaf r(cm) Length of 2.00 petiole x(cm) Maximum level True 10 of the crown volume Calculated volume 0.0857 of the 0.8021 7.12% Equivalent of the crown(m3) crown angle between 1.34 (m3) branch and trunk Number of leaves in the 20 same height of branch n

Diameter of the

cross section of 0.80 a branch d(cm)

Calculated total

mass of the 41.5178 Equivalent

crown(kg) length of the

branch in the 0.8768

Lowest level

l(1)(m)

Coefficient of

equivalent

length of the 0.90

branch form Calculated average bottom to top c density of the 0.593 Density of treeρ’(×103kg/m3) wood 0.90

ρ(×103kg/m3)

Acceleration of 9.80 gravity

As can be seen from the above data, the error is less than 7.5%, which provided

sufficient evidence to verify our estimation method.

Discussion

In this section, strengths and limitations of models constructed are discussed. In Section 2.1, shape functions are derived to quantify the distinctions between the representative leaves. These functions allow us to better control the properties of leaf shapes by applying traits parameters (e.g. blade area, cell-division margin) in the evaluation of bio-functions. However, it is still questionable how accurately these parameters can capture the structural and functional variations at organ levels. In the section followed, a series of mathematical models are derived to simulate the leaf expansion and three kinds of physiological activities in leaves. The photosynthesis model provides complete description about the process of sunlight harvesting and carbon dioxide assimilation. As for the transportation model, advanced algorithm are employed for precisely control the complex dynamic procedures and the analysis is highly comparable with other system of metabolic activities at the level of leaves.

Section 2.3 is where we start to extend the model to inter-organ relations and communications. To solve the overlapping puzzle, solid and plane geometry are adopted to find the intersection area of circles, which largely simplify the problem solving procedures without losing the basic biological intuition. The branch structure model considers both mechanical properties and the dynamic process of branch development. It builds connections with vital environmental factors (e.g. wind force) and further expands the model by catering for the inter-organ relationships. The models addressed in Section 2.4 develop a comparison between the physiological and structural approach in performing leaf mass estimations. Logical reasoning is derived in the way that associates the tree characteristics with leaf properties.

Since our work in this paper majorly focus on the bio-functioning and communications within an ideal and isolated case, the consistency of results can be easily destroyed when encountering external shocks. Elements from eco-system could be taken into account if further work was carried out. These elements involve both the physical factors (e.g. sunlight, water, longitude) and inter-species relations (e.g. competition, pray). In such way, we could provide more accurate and comprehensive model in the future.

1. Howell, S.H. (1998). Molecular genetics of plant development Cambridge; New

York: Cambridge University Press.

2. Hemsley, A.R. & Poole, I. (2004). The evolution of plant physiology : from whole

plants to ecosystems Amsterdam; Boston: Published for the Linnean Society of

London by Elsevier Academic Press

3. Stern, K.R., Bidlack, J.E., & Jansky, S.H. (2008). Introductory plant biology

Boston : McGraw-Hill Higher Education

4. Greig-Smith, P. (1983). Quantitative plant ecology BLACKWELL SCIENTIFIC

PUBLICATIONS, OXFORD (UK).

5. Dickison, William C et al (2000) integrative plant anatomy published in Academic

Press

6. Adrian D. Bell & Alan Bryan(1991). Plant Form: an illustrated guide to flowering

plant morphology; Oxford (UK);

7. Van Volkengurgh, (1999) leaf expansion—an integrating plant behavior plant cell

and environment publication

8. J. I. Lizaso, W. D Batchelor, M.E Westgate (2002) A leaf area model to simulate

cultivar-specific expansion and senescence of maize leaves published in Field

Crop Research

9. William G. & Norman P.A H (2008) introduction to Plant Physiology  published

in University of Western Ontario

10. Christopher J. Kucharik, John M Norman, Stith T. GoWer (1998) Measurement of

branch area and adjusting leaf area index indirect measurements published in

Agricultural And Forest Meteorology

11. Marcelo Shoey de O M, Carlos Eduardo N C, Affonso G G & Helion Vargas

(2001) A simple model for the dynamics of photosynthesis published in Analytical

Sciences

12. Falkovich & Gregory  (2011) Fluid mechanics: a short course for physicists

published in Cambridge ; New York : Cambridge University Press 13. Hironori Fujita and Atsushi Mochizuki (2006) The origin of the diversity of leave venation pattern published in Developmental Dynamics 14. W R N. Edenwards, P.G.Jarvis, J.J. Landscerg and H. Talbot (1986) A dynamic model for studying flow of studying of water in single trees published in Tree Physiology 15.  Peter Stiling (2001) ecology theories and applications published in University of South Florida 16. M.N.V Prasad (1996) plant ecophysiology published in New York 17. Walter Larcher (2003) physiology plant ecology – ecophysiology and stress physiology of functional groups published in Springer 18. Aaron M.E& Karl J N (1988)Branching patterns of salicornia europaea (chenopodiaceae)at different successional stages: a comparison of theoretical and real plants published in American Journal Botany 19.  Michael Hickey and Clive King (1997) common families of flowering plants published in Cambridge Press 20. Heldt, Hans-Walter (2011): plant biochemistry published in University of Amsterdan 21. Harold C Bold (1973) Morphology of plants published in Harper International Edition 22. Frank R. G, William P. F, Steven B H, Maurice D W (2009) A first course in mathematical modeling published in China Machine Press 23. Mark Allen Wesis (1997) Data structures and Algorithm Analysis in C published in Addison Wesley Longman 24. Daniel P, George C.T & Ruey S T (2001)A course in time series analysis published in a wiley-interscience
