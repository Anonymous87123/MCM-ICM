# P-A-2012-15065-1cbc0cd9

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
15065

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
A

<!-- b000005 | front_matter | pages [1] -->
2012 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000006 | prose | pages [1] -->
In our paper, we construct a mathematical model for estimating total leaf mass of a tree and investigating the relationship between leaf shape and tree profile.

<!-- b000007 | prose | pages [1] -->
Our approach consists of two main models.

<!-- b000008 | prose | pages [1] -->
The vector tree model uses vector and linear transformation to simulate the  geometrical structures of a tree, based on empirical and theoretical research on tree structures. A key assumption for this model is that the branching structure of a tree is paracladial.

<!-- b000009 | prose | pages [1] -->
The sunlight model simulates light irradiance inside the tree crown. It starts by  simulating the spiral motion of the sun in the course of a year using the brightness function for the sky. Then, the sunlight irradiance inside the tree crown is evaluated using a model based on the Monsi-Saeki equation.

<!-- b000010 | prose | pages [1] -->
To investigate the relationship between leaf shape and tree profile. We use the vector tree model to generate different tree profiles. We change the leaf shape under the same branching structure and see whether the real world leaf shape maximizes sunlight exposure among different shapes. Projection of shadow is used to measure sunlight exposure. Spherical integration is used to calculate the weighted sunlight exposure rate based on the brightness function for the sky. For each tree branching structure, leaves of three different leaf shapes are tested for the total amount of exposure to the sunlight. Comparing the simulated data to real-life data, we found that leaf shapes generally maximize the total exposure. Furthermore, our algorithm is good for medium and small sized leafs, but tends to be unreliable and generate answers with large variance for large sized leaves.

<!-- b000011 | prose | pages [1] -->
To estimate the total leaf mass of a tree, we incorporate the tree profile with the photosynthesis model, and use indexes like leaf mass per area (LMA) and leaf area index (LAI) to estimate the total leaf mass of a tree. Photosynthesis rates are assumed to be affected only by sunlight irradiance. We compute the leaf mass of Cinnamomum camphora using this proposed method. Comparing to the real-life data, our method is accurate enough with the limited amount of data.

<!-- b000012 | prose | pages [2] -->
Geometrical Tree

<!-- b000013 | prose | pages [2] -->
Leaf mass & leaf-tree relationship

<!-- b000014 | furniture | pages [2] -->
Team # 15065

<!-- b000015 | heading | pages [3] -->
Content

<!-- b000016 | contents | pages [3] -->
1.

<!-- b000017 | contents | pages [3] -->
Introduction ...................................................................................................................... 3

<!-- b000018 | contents | pages [3] -->
1.1

<!-- b000019 | contents | pages [3] -->
Outline of Our Approach ............................................................................................ 3

<!-- b000020 | contents | pages [3] -->
1.2

<!-- b000021 | contents | pages [3] -->
General Assumptions ................................................................................................. 4

<!-- b000022 | contents | pages [3] -->
2

<!-- b000023 | contents | pages [3] -->
Vector Tree Model ............................................................................................................ 4

<!-- b000024 | contents | pages [3] -->
2.1

<!-- b000025 | contents | pages [3] -->
Leaf classification ....................................................................................................... 4

<!-- b000026 | contents | pages [3] -->
2.2

<!-- b000027 | contents | pages [3] -->
Branching Structure Model ........................................................................................ 6

<!-- b000028 | contents | pages [3] -->
3

<!-- b000029 | contents | pages [3] -->
Sunlight Model ................................................................................................................ 10

<!-- b000030 | contents | pages [3] -->
3.1

<!-- b000031 | contents | pages [3] -->
Orbit of the sun & Brightness function for the sky .................................................. 10

<!-- b000032 | contents | pages [3] -->
3.2

<!-- b000033 | contents | pages [3] -->
Modeling the light irradiation at a certain position inside the tree crown.............. 11

<!-- b000034 | contents | pages [3] -->
4

<!-- b000035 | contents | pages [3] -->
Leaf shape & tree profile/branching structure .............................................................. 12

<!-- b000036 | contents | pages [3] -->
4.1

<!-- b000037 | contents | pages [3] -->
Sunlight exposure rate ............................................................................................. 12

<!-- b000038 | contents | pages [3] -->
4.2

<!-- b000039 | contents | pages [3] -->
Matching leaf shape with tree profile/branching structure .................................... 14

<!-- b000040 | contents | pages [3] -->
5

<!-- b000041 | contents | pages [3] -->
Leaf Mass of a Tree ......................................................................................................... 15

<!-- b000042 | contents | pages [3] -->
5.1

<!-- b000043 | contents | pages [3] -->
Computation of Leaf Mass per Area Ratio (LMA) .................................................... 16

<!-- b000044 | contents | pages [3] -->
5.2

<!-- b000045 | contents | pages [3] -->
Total leaf Area .......................................................................................................... 18

<!-- b000046 | contents | pages [3] -->
5.3

<!-- b000047 | contents | pages [3] -->
Case study: a real tree— Cinnamomum camphora ................................................. 19

<!-- b000048 | contents | pages [3] -->
5.4

<!-- b000049 | contents | pages [3] -->
Correlation between the leaf mass and the size characteristics of the tree ............... 21

<!-- b000050 | contents | pages [3] -->
6

<!-- b000051 | contents | pages [3] -->
Improving the model ...................................................................................................... 23

<!-- b000052 | contents | pages [3] -->
6.1

<!-- b000053 | contents | pages [3] -->
Leaf classification ..................................................................................................... 23

<!-- b000054 | contents | pages [3] -->
6.2

<!-- b000055 | contents | pages [3] -->
Exposure area of leaves ........................................................................................... 23

<!-- b000056 | contents | pages [3] -->
6.3

<!-- b000057 | contents | pages [3] -->
Determinants of photosynthesis rate ...................................................................... 23

<!-- b000058 | contents | pages [3] -->
7

<!-- b000059 | contents | pages [3] -->
Conclusion ....................................................................................................................... 23

<!-- b000060 | contents | pages [3] -->
8

<!-- b000061 | contents | pages [3] -->
Letter to a scientific journal editor ................................................................................. 24

<!-- b000062 | contents | pages [3] -->
Reference ................................................................................................................................ 24

<!-- b000063 | contents | pages [3] -->
Appendix: Matlab code for implementing our model ............................................................. 26

<!-- b000064 | heading | pages [4] -->
1. Introduction

<!-- b000065 | prose | pages [4] -->
In this paper we present a mathematical model for investigating the relationship between tree profiles and leaf shapes and estimating the total leaf mass of a tree. Specifically, we created a tree profile using 3-dimensional coordinates and linear transformation. We simulate the sunlight irradiance in the tree crown using the brightness function of the sky and Monsi and Saeki equation (Monsi, 1953). We then incorporate the sunlight irradiance into different tree profiles to find a leaf shape that maximizes sunlight exposure. The chosen shapes match with real leaf shapes, suggesting a close relationship between leaf shape and tree profile: leaf shape maximizes the overall sunlight exposure under a given tree profile. We then incorporate the tree profile with the photosynthesis model (Tsukaya, 2006), and use indexes like leaf mass per area (LMA) and leaf area index (LAI) to estimate the total leaf mass of a tree.

<!-- b000066 | prose | pages [4] -->
1.1 Outline of Our Approach

<!-- b000067 | prose | pages [4] -->
We first introduce two models which will be useful in the latter applications:

<!-- b000068 | prose | pages [4] -->
Vector Tree Model: The first part of our paper will be devoted to presenting the  theoretical framework of this model. Our objective is to create a spatial structure of the tree crown (branching structure and leaf distribution). We use vectors to simulate leaf shape, distribution of leaves on branches, and the tree profile/branching structure. Linear transformation of vectors is used to simulate the relationship between daughter branch and parent branch.

<!-- b000069 | prose | pages [4] -->
Sunlight Model: The second part of the paper will introduce the sunlight model.  Our objective is to simulate solar irradiance across a year. Brightness function over the celestial sphere is used to describe solar irradiance from different directions, Monsi and Saeki equation is used to calculate the light attenuation in a tree crown due to overlapping of leaf shadows.

<!-- b000070 | prose | pages [4] -->
The latter sections present two applications of the models.

<!-- b000071 | prose | pages [4] -->
 Investigating the Relationship between Leaf Shape and Tree Profile We use the vector tree model to construct different tree profiles. Combining the tree profile with the sunlight model, we are able to calculate the sunlight exposure rate of the leaves. We then adopt different leaf shapes for the same tree profile and find the one that maximizes the sunlight exposure. Comparing this chosen leaf shape with the real leaf shape of the tree, if there is a match, we may conclude that the leaf shape is associated with the tree profile in that it maximizes the sunlight exposure.

<!-- b000072 | prose | pages [5] -->
 Estimating Total Leaf Mass of a Tree Given a tree, we use the vector tree model to simulate its profile, and use the sunlight model to determine the light irradiance at each leaf. Then, we derive the relationship between light irradiance and the leaf mass per area (LMA) according to a photosynthesis model. Thus, we can derive the LMA for each leaf and calculate the weighted average LMA for the entire tree. We then use the sunlight model again to find the shadow of the tree crown and calculate the total leaf area of the tree using leaf area index (LAI). Finally, the total leaf mass is calculated by multiplying LMA with the total leaf area.

<!-- b000073 | prose | pages [5] -->
1.2 General Assumptions

<!-- b000074 | prose | pages [5] -->
Trees are assumed to be paracladial, i.e. if any branch is cut off, it has the same  structural characteristics, apart from size, as the parent from which it is cut.

<!-- b000075 | prose | pages [5] -->
The majority of leaves will grow on the last generation of branches.  Sun light is assumed to propagate in a straight line. Diffraction and refraction of  lights are ignored.

<!-- b000076 | prose | pages [5] -->
Photosynthesis rate is assumed to be affected only by the rate of light irradiance.  Other factors such as CO2 concentration in the air are assumed to be homogeneous at any part of the tree crown.

<!-- b000077 | prose | pages [5] -->
Photosynthesis due to light sources other than the sun is neglected. (e.g.  moonlight at night and artificial light) The environmental destructive effects are minimized and thus negligible, such as  natural disasters and herbivory.

<!-- b000078 | prose | pages [5] -->
Nutrient supplies are sufficient. 

<!-- b000079 | heading | pages [5] -->
2 Vector Tree Model

<!-- b000080 | prose | pages [5] -->
2.1 Leaf classification

<!-- b000081 | prose | pages [5] -->
The leaf is a major part of the plant-body plan. How to classify different leaves? Traditional plant taxonomy focuses on leaf functions and leaf shape. Recent research also suggests that venation is a strong indicator in leaf classification.

<!-- b000082 | prose | pages [5] -->
The general leaf shape is an important factor for the plant to receive sunlight. Traditional parameters in describing leaf shape include presence/absence of leaf petiole, flatness, leaf index (a ratio of leaf length to leaf width), margin type, and overall size. (Tsukaya, 2006)

<!-- b000083 | prose | pages [5] -->
Since we are going to construct a computerized simulation of a tree, is it important for us to classify leaves quantitatively such that they are easy for representation and simulation. Hence we develop a model to classify the leaves into 4 basic shape categories.

<!-- b000084 | prose | pages [6] -->
To classify a given leaf to one of the four basic shape categories, we focus on 3 factors of the leaf: shape convexity, leaf index (ratio of leaf length to leaf width), and the position of the longest width on a leaf.

<!-- b000085 | prose | pages [6] -->
To determine the shape convexity, we first simulate a leaf using a polygon. We first fit the leaf into a grid with each cell size 0.5cm×0.5cm. Next we select the outmost grids that have been covered more than half by the leaf. Then we plot and connect the centers of these grids. Hence we have a simulating polygon of the leaf. Two illustrations are shown as below.

<!-- b000086 | prose | pages [6] -->
We are now able to determine the convexity of the polygon of leaf— convex polygons are such that all diagonals lie entirely inside the polygon; concave polygons are such that some diagonals will lie outside the polygon. Hence we can determine the convexity of the leaf.

<!-- b000087 | prose | pages [6] -->
If a leaf is concave, we immediately classify it as Palmate. Convex leaves are left for further determination.

<!-- b000088 | prose | pages [6, 7] -->
To classify other leaves, the second factor we look at is leaf index, which is the ratio of leaf length to leaf width. According to empirical data (Tsukaya, 2006) (Johnson, 1990), we classify leaves with leaf ratio of 3.5 and above as Linear. Those with leaf ratio below 3.5 will be either Elliptic or Deltoid.

<!-- b000090 | prose | pages [7] -->
To classify Elliptic leaf and Deltoid leaf, we look at the position of longest-width on a leaf. In order to have a more quantitative view, we are interested in the ratio of distance between leaf tip and longest-width-position (D) to the leaf length (L).

<!-- b000091 | prose | pages [7] -->
If the ratio (D/L) lies within [1/4, 3/4], we classify the leaf as Elliptic. Leaves whose ratio<1/4 or >3/4 are Deltoid.

<!-- b000092 | prose | pages [7] -->
To summarize the decision rule of classifying a leaf, we provide a decision flow chart.

<!-- b000093 | prose | pages [7] -->
Leaf polygon: convex?

<!-- b000094 | prose | pages [7] -->
Concave Convex Palmate Leaf index ≥3.5 Linear <3.5

<!-- b000095 | prose | pages [7] -->
Ratio of distance between leaf tip ∈[1/4, 3/4] Elliptic and longest-width-position (D) to the leaf length (L)

<!-- b000096 | prose | pages [7] -->
<1/4 or >3/4 Deltoid

<!-- b000097 | prose | pages [7] -->
2.2 Branching Structure

<!-- b000098 | prose | pages [7] -->
2.2.1 Biological Backgrounds and Existing Models

<!-- b000099 | prose | pages [7] -->
The existing geometrical models simulating branching structures of trees are essentially empirical based on a rule that specifies the relative angular direction and length of a daughter branch to its parent branch (Johnson, 1990). In order to obtain a more realistic model, studies considering whorls and bifurcations as rule in branching simulation have also been carried out (Fisher, 1977) (Fisher, 1979).

<!-- b000100 | prose | pages [8] -->
2.2.2 Model Description

<!-- b000101 | prose | pages [8] -->
(http://www.infovisual.info/01/002_en.html)

<!-- b000102 | prose | pages [8] -->
In this model, our objective is to represent each branching point and the position of each leaf using their position vector (x,y,z) in a 3D coordinate shown above with z-axis set to be the main stem of the tree.

<!-- b000103 | prose | pages [8] -->
2.2.2.1 Child Branch Formation

<!-- b000104 | prose | pages [8] -->
Given the length and location of a parent branch, we want to find the direction and length of the child branch. At this point, the Child branches generated will subject to the following:

<!-- b000105 | prose | pages [8] -->
a) Number of child branches at the branching point N is given by N=[𝜃∗𝜎(𝑘)], where 𝑘: A species-wise constant coefficient which is related to the mean of the  number of child branches for the species.

<!-- b000106 | prose | pages [8] -->
θ: Uncertainty compensator which incorporates the genetic uncertainties and  environmental uncertainties.

<!-- b000107 | prose | pages [8] -->
𝜎: A function which maps the species of a tree to the mean number of child  branches generated at this branching point.

<!-- b000108 | prose | pages [9] -->
b) At each branching point, the length and direction of the N child branches are determined by multiplying the direction vector of the parent branch with transformation matrices 𝐴1, 𝐴2, … , 𝐴𝑁 respectively.

<!-- b000109 | prose | pages [9] -->
𝐴𝑖 is defined as the following:

<!-- b000110 | prose | pages [9] -->
𝑐𝑜𝑠𝜑𝑖 𝑠𝑖𝑛𝜑𝑖 0 −𝑐𝑜𝑠𝜃𝑖𝑠𝑖𝑛𝜑𝑖 𝑐𝑜𝑠𝜃𝑖𝑐𝑜𝑠𝜑𝑖 𝑠𝑖𝑛𝜃𝑖 𝐴𝑖(𝜃𝑖, 𝜑𝑖) =        𝜆𝑖∗( ) 𝑠𝑖𝑛𝜃𝑖𝑠𝑖𝑛𝜑𝑖 −𝑠𝑖𝑛𝜃𝑖𝑐𝑜𝑠𝜑𝑖 𝑐𝑜𝑠𝜃𝑖

<!-- b000111 | prose | pages [9] -->
where 𝜆𝑖 is the length change, 𝜑𝑖 is the rotated angle with respect to the parent branch about 𝑂𝑧 and 𝜃𝑖 is the rotated angle with respect to the parent branch about local x axis 𝑂𝑥 with respect to the parent branch. Note that at each branching point, the coordinate system adopted for this transformation will be the local coordinate system with respect to the local parent branch, and the parent branch will lie on the z-axis.

<!-- b000112 | prose | pages [9] -->
c) Now, we are able to determine the coordinate of each branch. We first number the branches according to the generating sequence. Let 𝑟𝑁 denotes the vector representing the branch of the Nth generated branch. If 𝑟𝑡 is the parent branch of 𝑟𝑘, then the equation:

<!-- b000113 | prose | pages [9] -->
𝑟𝑘= 𝐴𝑗𝑟𝑡 is to be satisfied, where 𝐴𝑗 is the transformation matrix that governs the rule between tth  branch and kth branch (abbreviated as branch t and branch k in later context).

<!-- b000114 | prose | pages [9] -->
Let 𝑅𝑁 denote the coordinate of Nth generated branch. Then 𝑅1 = 𝑟1 and 𝑅𝑘= 𝑅𝑡+ 𝑟𝑘.

<!-- b000115 | prose | pages [9] -->
In particular, in the situation where only bifurcations are concerned (Johnson, 1990), { 𝑟2𝑘= 𝐴1𝑟𝑘 𝑟2𝑘+1 = 𝐴2𝑟𝑘 and 𝑅2𝑘= 𝑟2𝑘+ 𝑅𝑘 { 𝑅2𝑘+1 = 𝑟2𝑘+1 + 𝑅𝑘

<!-- b000116 | prose | pages [9, 10] -->
2.2.2.2 Leaf Formation Now, we are ready to construct leaves on the branches.

<!-- b000118 | prose | pages [10] -->
Define set 𝐴= {𝑟𝑝 𝜖 𝑇𝑟𝑒𝑒| ∀ 𝑟𝑘 𝜖 𝑇𝑟𝑒𝑒, 𝑏𝑟𝑎𝑛𝑐ℎ 𝑝 𝑖𝑠 𝑛𝑜𝑡 𝑡ℎ𝑒 𝑝𝑎𝑟𝑒𝑛𝑡 𝑜𝑓 𝑏𝑟𝑎𝑛𝑐ℎ 𝑘}

<!-- b000119 | prose | pages [10] -->
and the growing of leaves is subject to the following:

<!-- b000120 | prose | pages [10] -->
a) Basic phyllotaxis patterns:

<!-- b000121 | prose | pages [10] -->
(http://www.math.smith.edu/phyllo//About/Classification.html) Distichous Phyllotaxis, in distichous phyllotaxis, leaves or other botanical  elements grow one by one, each at 180 degrees from the previous one.;

<!-- b000122 | prose | pages [10] -->
Whorled Phyllotaxis, In whorled phyllotaxis, two or more elements grow at the  same node on the stem.;

<!-- b000123 | prose | pages [10] -->
Spiral Phyllotaxis, In spiral phyllotaxis, botanical elements grow one by one, each  at a constant divergence angle d from the previous one.;

<!-- b000124 | prose | pages [10] -->
Multijugate Phyllotaxis, elements in a whorl (group of elements at a node) are  spread evenly around the stem and each whorl is at a constant divergence angle d from the previous one.

<!-- b000125 | prose | pages [10] -->
The spacing of leaves on the branch is determined by the function d(I) b) which takes in the intensity of sunlight irradiance and outputs the spacing of the leaves. c) The probability that a leaf grows at a certain spot is determined by the function 𝑝(𝐼) which takes in the intensity of sunlight irradiance and outputs the probability that a leaf is likely to grow on a certain spot of the branch.

<!-- b000126 | prose | pages [10] -->
In our model, for each 𝑟𝑝 𝜖 𝐴, we grow the leaves on branch p according to the archived Basic phyllotaxis patterns for different species. The spacing between two different potential leaf-growing spots is d(I) and the probability of a leaf growing at a certain spot is 𝑝(𝐼).

<!-- b000127 | prose | pages [10] -->
2.2.3 Different tree profiles generated by our model

<!-- b000128 | prose | pages [10] -->
Using the model introduced above, we are able to generate a wide range of tree profiles by varying the coefficients in the model. Three examples are shown below.

<!-- b000129 | prose | pages [10] -->
Zooming in to the picture, the leaves are represented as this:

<!-- b000130 | heading | pages [11] -->
3 Sunlight Model

<!-- b000131 | prose | pages [11] -->
Photosynthesis is important for the growth of leaves, and it is driven by solar energy. Thus, in this section, we will consider the light irradiance in a tree crown. By modeling the sun radiation using brightness function, and using Monsi-Saeki equation (Monsi, 1953) to describe the light attenuation within a tree crown, we will be able to calculate light irradiance at any point within the tree crown.

<!-- b000132 | prose | pages [11] -->
3.1 Orbit of the sun & Brightness function for the sky

<!-- b000133 | prose | pages [11] -->
Orbit of the sun Since the sun moves in a spiral during the course of a year (in the view of an observer standing on the earth), we will first model its orbit using celestial sphere. At different latitude, the sun will trace out a different trajectory in a year. Three examples are shown below.

<!-- b000134 | prose | pages [11] -->
North temperate zone    Equator       the Arctic Pole

<!-- b000135 | prose | pages [11] -->
Brightness function for the sky The brightness function (Johnson, 1990) for the sky is defined in terms of spherical polar coordinates (r, θ, φ), although it does not involve the r coordinate. When defining the position of the sun, θ is known as the zenith angle (when θ = 0, the sun is directly overhead) and φ is termed the azimuth angle.

<!-- b000136 | prose | pages [11] -->
The brightness function of the sky is defined as B(θ, φ), with units W m-2 srad-1. The steradian (srad) is the SI unit for solid angle: a solid angle is the area of the surface of a portion of sphere divided by the square of the radius of the sphere. Thus the total solid angle of a sphere is 4π srad

<!-- b000137 | prose | pages [11, 12] -->
Deriving the brightness function To illustrate the method of deriving B(θ, φ), we use trees on the equator as an example. Brightness function for the sky at other latitude and longitude can be derived in a similar way with slight modification of the algorithm.

<!-- b000139 | prose | pages [12] -->
A     B On the equator, the orbit of the sun will shift from circle A to circle B from summer solstice to winter solstice (strictly speaking it is not a circle but a spiral).

<!-- b000140 | prose | pages [12] -->
We denote the rate of solar radiation that reaches the earth as E with unit of W m-2 s-1. E is known from previous research of solar energy.

<!-- b000141 | prose | pages [12] -->
When the sun is at a certain position (θ, φ) on the celestial sphere, the rate of solar energy that is absorbed by the earth surface (Ea) depends on the angle between the ground and the light beam (γ).

<!-- b000142 | prose | pages [12] -->
𝜋 𝐸𝑎≈E × sinγ, (γ = 2 −𝜑)

<!-- b000143 | prose | pages [12] -->
Thus, since we know the orbit of the sun in the course of a year, the brightness function can be derived by integration of Ea over time (t). This should be done by computer simulation and discretization of the spiral trajectory is used for ease of implementation.

<!-- b000144 | prose | pages [12] -->
3.2 Sunlight irradiation inside the tree crown

<!-- b000145 | prose | pages [12] -->
In plant models, light attenuation in a canopy is generally described by the equation (known as Monsi and Saeki equation (Monsi, 1953)):

<!-- b000146 | prose | pages [12] -->
𝐼(𝑙) = 𝐼0𝑒−𝑘𝑠

<!-- b000147 | prose | pages [12, 13] -->
where 𝐼0 and 𝐼(𝑙) (W (m2 ground)-1) are the irradiances above and within the tree crown respectively at path-length s, and 𝑘(m2 ground(m2 leaf)-1) is known as the extinction coefficient which is assumed to be constant.

<!-- b000149 | prose | pages [13] -->
B(θ, φ)

<!-- b000150 | prose | pages [13] -->
s P

<!-- b000151 | prose | pages [13] -->
For any point P within the tree crown, the path-length s varies with the angles θ and φ. Monsi-Saeki equation can be used to describe the attenuation along the path-length s that the radiation passes to reach P. And according to our definition of brightness function, 𝐼0 = B(θ, φ). Thus, the total irradiation at a point P within the plant 𝐼𝑝 is given by the integral 𝜋/2 2𝜋 𝐵(𝜃, 𝜑)𝑒−𝑘𝑠cosθsinφ 𝑑𝜃𝑑𝜑 𝐼𝑝= ∫ ∫ 0 0

<!-- b000152 | prose | pages [13] -->
In practice, this integral is evaluated numerically using computer programs.

<!-- b000153 | heading | pages [13] -->
4 Leaf shape & tree profile/branching structure

<!-- b000154 | prose | pages [13] -->
In this section, we use the model developed in chapter 2 to investigate the relationship between leaf shape and tree profile/branching structure. We raise a hypothesis that for any tree profile, the leaf shape will maximize its exposure to sunlight.

<!-- b000155 | prose | pages [13] -->
To test this hypothesis, we calculate the sunlight exposure rate for each type of leaf shape under a given branching structure. Then, we will choose the leaf shape which maximizes sunlight exposure. If the leaf shape chosen coincides with the real life shape, our hypothesis is true.

<!-- b000156 | prose | pages [13] -->
4.1 Sunlight exposure rate

<!-- b000157 | prose | pages [13, 14] -->
To define the sunlight exposure rate of leaves, we first ignore the motion of the sun in the sky and assume that the sun is always directly overhead of the tree. Then, the sunlight exposure rate (SE) is defined as ∑ 𝐴𝑖 SE = 𝑇𝐴, Where Ai is the area of  shadow casted by an individual leave with index i (denoted by pink dots on the graph below), and TA is the total area within the borderline of the shadow casted by the tree crown (denoted by the red circle on the graph below). SE measures the proportion of sunlight on the tree crown that is blocked by leaves.

<!-- b000159 | prose | pages [14] -->
Now, we consider the motion of the sun in the sky. We have introduced the concept of brightness function for the sky B(θ, φ) in section 2.2 which models the motion of sun in the course of a year by assigning each point (θ, φ) on the celestial sphere a solar irradiance rate.

<!-- b000160 | prose | pages [14] -->
We define the sunlight exposure rate for each direction (θ, φ) in a similar way to the overhead sunlight.

<!-- b000161 | prose | pages [14] -->
SE(θ, φ) = ∑ 𝐴𝑖(𝜃, 𝜑) 𝑇𝐴(𝜃, 𝜑) Then, the overall sunlight exposure rate for the tree is an integral of SE(θ, φ) over the entire celestial sphere with weight B(θ, φ) for each (θ, φ):

<!-- b000162 | prose | pages [14] -->
𝜋/2 2𝜋 𝐵(𝜃, 𝜑) ∙𝑆𝐸(𝜃, 𝜑)𝑐𝑜𝑠𝜃𝑠𝑖𝑛𝜑dθ𝑑𝜑 ∫ ∫ 0 0 SEtotal = , 𝑁

<!-- b000163 | prose | pages [14, 15] -->
𝜋/2 2𝜋 where N = ∫ 𝐵(𝜃, 𝜑)𝑐𝑜𝑠𝜃𝑠𝑖𝑛𝜑dθ𝑑𝜑 ∫ is a normalization factor. The range of 0 0 SEtotal is [0, 1].

<!-- b000165 | prose | pages [15] -->
4.2 Matching leaf shape with tree profile

<!-- b000166 | prose | pages [15] -->
Now, we are ready to investigate the relationship between leaf shape and branching structures.

<!-- b000167 | prose | pages [15] -->
As illustrated in section 2, we classify leaf shapes into the following categories.

<!-- b000168 | prose | pages [15] -->
We choose three types of tree profiles to study:

<!-- b000169 | prose | pages [15] -->
Profile 1: pine tree    Profile 2: poplar tree  Profile 3: Janpanese banana

<!-- b000170 | prose | pages [15] -->
For each tree profile, we calculate the SEtotal for the four types of leaves and chose the one with the highest SEtotal. We set d (the distance between adjacent leaves on the same branch) and S (the size of a leaf) based on data in ‘manual of leaf architecture’ (Beth Ellis, 2009) To derive the brightness function of the sky, we assume that the tree is located at a place with latitude: 45oN. The results are shown below:

<!-- b000171 | prose | pages [15] -->
Tree Profile： Triangular: pine Elliptic: poplar Semi-spherical:

<!-- b000172 | prose | pages [15] -->
tree tree Japanese banana Leaf distribution on branches:

<!-- b000173 | prose | pages [15] -->
0.53 0.62 0.82

<!-- b000174 | prose | pages [15] -->
0.67 0.49 0.83

<!-- b000175 | prose | pages [15, 16] -->
0.49 0.63 0.82 0.47 0.62 0.85

<!-- b000177 | prose | pages [16] -->
Shape chosen Real leaf shape

<!-- b000178 | prose | pages [16] -->
This figure is the detailed implementation of poplar tree with Deltoid leaves (numerical discretion is adopted). From the figure we could see that different angles of sun will influence the exposure area of the leaves on the tree. In our implementation, when θ and φ are small, the light irradiance on the tree is largest. We computed the weighted sum according to the method described in the previous sections.

<!-- b000179 | prose | pages [16] -->
Since the results are generally expected, our hypothesis stands, i.e. there is correlation between leaf shapes and tree structures: leaf shapes tend to maximize sunlight exposure of this tree. This provides insights into why leaves have different shapes. A larger pool of tree profiles should be studied using this model before we can draw a solid conclusion on the exact relationship. However, that is beyond the mathematical context of this topic, we leave it for readers who are interested to investigate further.

<!-- b000180 | heading | pages [16] -->
5 Leaf Mass of a Tree

<!-- b000181 | prose | pages [16] -->
In this section, we will use the vector tree model and sunlight model to estimate the total leaf mass of a tree. The general formula to calculate total leaf mass of a tree is Total leaf mass = weighted Leaf mass per area ratio(LMA) × total leaf area The computation of LMA and leaf area will be introduced.

<!-- b000182 | prose | pages [17] -->
5.1 Leaf Mass per Area Ratio (LMA)

<!-- b000183 | prose | pages [17] -->
Leaf Mass per Area (LMA) is defined as the ratio of leaf mass over its area (g m-2).

<!-- b000184 | prose | pages [17] -->
In this section, we describe a method to calculate the average LMA for the tree. Since Leaves on a tree have different thicknesses due to different photosynthesis rate determined by the sunlight irradiance at the leaf (SARAH J. COOKSON1, 2005), they tend to have different LMA. Thus, we need to calculate LMA for each leaf based on their photosynthesis rate and then calculate the weighted average of all the individual LMAs.

<!-- b000185 | prose | pages [17] -->
5.1.1 Photosynthesis Rate

<!-- b000186 | prose | pages [17] -->
We adopted the model in (Johnson, 1990) which relates the internal gross photosynthetic rate P with sunlight irradiance Il , internal 𝐶𝑂2 concentration of the plant 𝐶𝑖 and the 𝐶𝑂2 concentration in the air 𝐶𝑎.

<!-- b000187 | prose | pages [17] -->
𝛼𝐼𝑙𝐶𝑖 𝑟𝑥 𝑃= (*) 𝐶𝑖 𝛼𝐼𝑙+ 𝑟𝑥 where α is known as the photochemical efficiency (𝑘𝑔 𝐶𝑂2 J-1) and 𝑟𝑥 as the carboxylation resistance (𝑠𝑚−1).

<!-- b000188 | prose | pages [17] -->
Next, denote Pn as the net photosynthetic rate, and the following equation is

<!-- b000189 | prose | pages [17] -->
satisfied

<!-- b000190 | prose | pages [17] -->
Pn = P - Rd (**)

<!-- b000191 | prose | pages [17] -->
and Pn = Ca - Ci (***) rd

<!-- b000192 | prose | pages [17] -->
where Rd is the constant dart respiration rate, rd is the diffusion rate. Use (*) (**) and (***) to solve for P and 𝑃𝑛 , we get 0 = Pn 2rd - Pn[aI1(rx + rd)+Ca - Rdrd]+aI1Ca - Rd(aI1rx +Ca) Therefore, we get Pn = -[aI1(rx + rd ) + Ca - Rdrd]± [aI1(rx + rd )+ Ca - Rdrd]2 + 4rdRd(aI1rx + Ca) 2rd

<!-- b000193 | prose | pages [17] -->
However, by (Johnson, 1990) only the negative root is biologically valid, thus we can solve for Pn. In our model, Il is obtained from the sunlight model in section 3, Ca rx rd Rd are all assumed to be constant at any position in the tree crown.

<!-- b000194 | prose | pages [17, 18] -->
5.1.2 Leaf Mass Per Area Ratio (LMA) Affected by Venation Networks In modern ecology, LMA is an important measure in classifying different kinds of leaves. By observing the venation network of a given leaf area, one can also find a surprisingly correlated relationship between three venation functional traits and LMA (Benjamin Blonder, 2011). We follow the modeling process of the derivation of LMA with respect to the following functional traits:

<!-- b000196 | prose | pages [18] -->
Density σ :  total path length of veins in the area of interest (ROI) divided by  the ROI area;

<!-- b000197 | prose | pages [18] -->
Distance d : the mean diameter of the largest circular masks that fit in each  closed loop Loopiness x: the mean number of closed loops in ROI 

<!-- b000198 | prose | pages [18] -->
In (Benjamin Blonder, 2011) the derivation of the relationship between LMA and three functional traits shows the following relationship:

<!-- b000199 | prose | pages [18] -->
d = k0d (1)

<!-- b000200 | prose | pages [18] -->
2(rV - rL)s + 2rLd LMA = prV (2) k0

<!-- b000201 | prose | pages [18] -->
Where ρ𝑣is the inner radius of the veins in the ROI  r𝑣is mass density of the terminal veins  ρ𝑙 is the mass density of the lamina  𝛿 is the thickness of the leaf at ROI  k0 is a constant which relates d and δ 

<!-- b000202 | prose | pages [18] -->
5.1.3 Peak Carbon Assimilation Rate Per Mass

<!-- b000203 | prose | pages [18] -->
In [BB], a detailed model is given to derive the Peak Carbon Assimilation Rate per Mass (𝐴𝑚) [pc0(1- h)k0nsasWUE]s (3) Am = 2(rV - rL)s ][(pts + sqrt(pas))s + 2asnslog( d [2rLd + k0prV )] k0rV

<!-- b000204 | prose | pages [18] -->
where 𝑎𝑠 is the maximum aperture of a stomate, 𝑛𝑠 is the number density of open stomata, 𝑡𝑠 is the thickness of a stomatal pore, D is the temperature and pressure dependent diffusion constant of water in air, 𝐶0 is the temperature and pressure dependent saturation vapor concentration of water in air, WUE is water-use efficiency and h is the relative humidity ( (Buck, 1981) (Nobel, 1999).

<!-- b000205 | prose | pages [18] -->
5.1.4 Derivation of LMA Now we use the results in the above sections to derive LMA. One observation we

<!-- b000206 | prose | pages [18] -->
make is 𝑃𝑛≤𝐴𝑚, since 𝐴𝑚 is the peak photosynthetic rate. Therefore, we use m

<!-- b000207 | prose | pages [18, 19] -->
which accounts for environmental factor such that mPn = Am (4) . Therefore, by assumption, we can solve for LMA combining equations (1) – (4) even if the thickness of the leaf d is unknown. Then we can get the desired LMA. By applying the above method for each leaf, we will be able to get the average LMA for the tree.

<!-- b000209 | prose | pages [19] -->
5.2 Total leaf Area

<!-- b000210 | prose | pages [19] -->
We will calculate the total leaf area of a tree by the following formula: Total leaf area = Leaf Area Index(LAI) × ground area covered by the tree crown In the following sections, we will introduce the concept of LAI and the method of getting the ground area covered by the tree crown from our vector tree model.

<!-- b000211 | prose | pages [19] -->
5.2.1 Leaf Area Index

<!-- b000212 | prose | pages [19] -->
Leaf Area Index (LAI) is defined as the one sided green leaf area per unit ground area in broadleaf canopies, or as the projected needle leaf area per unit ground area in needle canopies.

<!-- b000213 | prose | pages [19] -->
It is an indispensable parameter in studying plant physiology, since vegetation surface is an important determinant of various plant functions such as photosynthesis and transpiration. Methods used for measuring LAI in hardwood forests include destructive sampling, allometric equations, litter fall, and light interception based techniques. (Vose et al, 1995)

<!-- b000214 | prose | pages [19] -->
A data set for LAI has been compiled containing 1008 records of worldwide data on leaf area index for the time period 1945-2000. (Scurlock, 2001)

<!-- b000215 | prose | pages [19] -->
5.2.2 Ground area of a tree

<!-- b000216 | prose | pages [19] -->
We can derive the ground area of a tree from the vector tree model introduced in section 2.2. By computer simulation, we project the tree crown onto the ground, and plot the margin of the projection. Hence calculate the ground surface area according to the projected polygon hull in the computer. Below is an illustration of a simulated tree and its crown projection.

<!-- b000217 | prose | pages [20] -->
Once we know the ground area coved by the tree crown, we multiply it with LAI to get the total leaf area of the tree. And then, we multiply it to the LMA ratio to get the total leaf mass.

<!-- b000218 | prose | pages [20, 21] -->
5.3 Case study: a real tree— Cinnamomum camphora We would like to test our model by studying a real tree (Cinnamomum camphora) and estimate its total leaf mass. A picture of the tree is shown above.

<!-- b000220 | prose | pages [21] -->
5.3.1 Simulation of the tree in computer

<!-- b000221 | prose | pages [21] -->
In order to simulate the branching structure of this tree, we need to know the angles (θ1, ф1, θ2, ф2) of transformation stated in model 2.2. Since there are no empirical data for these parameters, we need to conduct a field measurement. The major difficulty is to determine the direction of our imaginary x-axis and y-axis: a wrong direction of coordinates will result in wrong angles and hence a twisted shape of tree profile.

<!-- b000222 | prose | pages [21] -->
In our measurement, we first set the trunk to be z-axis, and the origin is at where the z-axis touches the ground (our xy-plane). We equally divide the ground using 32 outgoing rays. (See illustration below)

<!-- b000223 | prose | pages [21] -->
Setting each outgoing ray as x-axis, we then have 32 possible coordinate systems. In each coordinate system, we can directly measure and calculate a data set of (θ1, ф1, θ2, ф2) by measuring the angle of the branches. We simulate trees using each of these 32 data sets; compare the simulated vector tree with the real tree profile. The one that matches the real tree most closely will be chosen. The data we get from this field measurement and simulation is: θ1=π/12.5, ф1=π/3.7, θ2=－π/6, ф2=π/4.8

<!-- b000224 | prose | pages [21] -->
The total number of branches of our simulated tree is 29, and we assume that the function d(I) defined in section 2.2.3.2 which determines the spacing of leaves follows the Gaussian distribution with parameters(μ=0.1, σ=0.1).

<!-- b000225 | prose | pages [21] -->
We classify the shape of this tree leaf as Elliptic, and its average transverse diameter is around 5cm. For simplicity of calculation, we represent the leaves using rhombuses with average longer diagonal 0.25 in our computer simulation.

<!-- b000226 | prose | pages [21] -->
Following is our simulated tree.

<!-- b000227 | prose | pages [22] -->
5.3.2 Estimating the total leaf mass of the tree

<!-- b000228 | prose | pages [22] -->
Using the model introduced in section 4.1, our computer simulates the effect of light intensity on the Leaf Mass Area (LMA) of leaves in different parts of the tree crown and hence derive the average LMA of the tree to be 177.74g/m-2

<!-- b000229 | prose | pages [22] -->
The ground surface area can be calculated by the computer as introduced in section

<!-- b000230 | prose | pages [22] -->
The output of the polygon ground surface area is 150.0359. Converting it to scale of the tree, the ground surface area is calculated to be around 6m2 (actual number 6.001436). This data matches the actual ground area of this tree quite closely.

<!-- b000231 | prose | pages [22] -->
According to empirical data (Beth Ellis, 2009), Cinnamomum as evergreen broadleaved plant usually has a quite high leaf area index (LAI) above 10. We take the LAI of this tree to be 12. Hence the total leaf area of this tree is around 6×12=72m2

<!-- b000232 | prose | pages [22] -->
Therefore, the leaf mass of this tree is estimated as 177.47g/m-2×72m2=12777.84g.

<!-- b000233 | prose | pages [22] -->
5.4 Correlation between the leaf mass and the size characteristics of the tree

<!-- b000234 | prose | pages [22] -->
In this section, we investigate the correlation between leaf mass and the size characteristics of trees, specifically the height of trees.

<!-- b000235 | prose | pages [22] -->
We use our vector tree model to simulate trees with 3 different profiles (see illustration below) each at height varying from 5m to 10m (with 0.5m intervals), and calculate their total leaf area using the method introduced above.

<!-- b000236 | prose | pages [23] -->
Profile 1: Semi-sphere    Profile 2: Cone    Profile 3: Ellipsoid

<!-- b000237 | prose | pages [23] -->
We conduct a regression analysis for the total 30 data and for each of the 3 profiles separately, to study the correlation between total leaf mass and the size characteristics of trees.

<!-- b000238 | prose | pages [23] -->
Following is the plot of data General trees:                      Profile 1:

<!-- b000239 | prose | pages [23] -->
Profile 2:                           Profile 3:

<!-- b000240 | prose | pages [23] -->
Hence we may conclude that for trees in general, we can hardly say that there is obvious correlation between the leaf mass and the size characteristics of trees. However, when considering trees with similar crown profile, it appears that the leaf mass may be related with the height of the tree—the total leaf mass tends to increase cubically as tree height increases. Since we only have limited data set, the actual correlation may be determined and tested through further investigation.

<!-- b000241 | heading | pages [24] -->
6 Improving the model

<!-- b000242 | prose | pages [24] -->
6.1 Leaf classification

<!-- b000243 | prose | pages [24] -->
The basic building block of our model is the leaf model introduced in section 2.1, in which we classify leaves based on their shapes. We can improve this by taking into account other biological features of the leaves, such as their photosynthesis characteristics (e.g. C3 v.s C4 plants), transpiration patterns, or vein structure.

<!-- b000244 | prose | pages [24] -->
6.2 Exposure area of leaves

<!-- b000245 | prose | pages [24] -->
In section 3, when calculating the exposure area of leaves to the sunlight, we implement the model by discretizing the x-y plane in to small grids and determine whether the leaves block each grid. This algorithm works satisfactorily for small leaf size. However, as we have seen in the Japanese banana tree example, when leaf size is big, this algorithm tends to generate similar results for different leaf shapes. Thus, we may improve our algorithm to calculate leaf shadows for big size leafs.

<!-- b000246 | prose | pages [24] -->
6.3 Determinants of photosynthesis rate

<!-- b000247 | prose | pages [24] -->
In section 4.1, we assume that only sunlight irradiance affect the photosynthesis rate. Other factors relating to photosynthesis such as concentration of CO2, water and N2 may also be incorporated into the model.

<!-- b000248 | heading | pages [24] -->
7 Conclusion

<!-- b000249 | prose | pages [24] -->
The problem of investigating the relationship between leaf shapes and branching structures tend to be nontrivial given the biological complexity of the plant structure. Our approach tackles the problem geometrically since many previous studies in the field of plant physiology have shown geometric uniformity. This approach is proved to be appropriate and reveals the fact that the leaf shape relates with branching structure in that the shape tends to maximize sunlight exposure under the given tree profile.

<!-- b000250 | prose | pages [24] -->
The model can be extended to estimate the total leaf mass of a tree using the relationship between photosynthesis rate and leaf mass per area (LMA). Empirical test of our model on cinnamomum camphora tree has shown that the method gives realistic estimation of the leaf mass.

<!-- b000251 | heading | pages [25] -->
8 Letter to a scientific journal editor

<!-- b000252 | prose | pages [25] -->
The leaf is an important part of the plant-body plan, and it is the major organ of a plant for photosynthesis. Through our research, we proposed a geometrical model to investigate the relationship between leaf shapes and tree profiles. We developed computerized models to simulate tree structures and sunlight irradiance in tree crowns; and incorporated the model with physiological traits of trees. Case studies have been carried out and our models are proven to be viable. During our investigation, we have discovered some interesting findings.

<!-- b000253 | prose | pages [25] -->
Leaf shapes are closely related with tree profile.  We discovered that the leaves always adopts the shape which maximizes the sunlight exposure under the given tree profile. This finding may have significant importance in unfolding the mystery of the efficiency of photosynthesis. This discovery once again shows us the stunning power of natural selection.

<!-- b000254 | prose | pages [25] -->
Leaf mass are closely related to venation networks and photosynthesis rate.  Variations of leaves on a tree are considered as a crucial factor in determining the leaf mass of a tree. There is solid evidence that leaf mass per area and photosynthesis rate is strongly related to venation networks. Incorporating a model estimating leaf photosynthesis rate, we are able to derive a formula calculating the leaf mass per area of a tree.

<!-- b000255 | prose | pages [25] -->
Our approach is innovative and some of the mathematical models developed in our paper may have potential uses in the study of plant physiology.

<!-- b000256 | prose | pages [25] -->
Our tree branching simulation model is improved and revised based on some  previous branching models. We incorporate the uncertainty into the geometrical simulation of a tree. Besides, leaf budding points on branches are also determined with rules that incorporate the environmental factors and genetic uncertainty. This improvement of the branching model makes it a more realistic representation of the nature’s complexity.

<!-- b000257 | prose | pages [25] -->
We introduce the concept of Sunlight Exposure Rate (SE) as a metric studying the  level of exposure of leaves to sunlight. Given a type of leaf shape, strong correlation exists between total leaf area and total ground shade area. The quotient, which is defined as SE can be used to evaluate the relationship between leaf shape, leaf distribution, and sunlight.

<!-- b000258 | heading | pages [26] -->
Reference

<!-- b000259 | references | pages [26] -->
Benjamin BlonderViolle, Lisa Patrick Bentley and Brian J. EnquistCyrille. (2011). Venation

<!-- b000260 | references | pages [26] -->
networks and the origin of the leaf economics spectrum. Ecology Letters, 14, 91–100.

<!-- b000261 | references | pages [26] -->
Beth EllisC. Daly, Leo J. Hickey, Kirk R. Johnson, John D. Mitchell, Peter Wilf, and Scott L.

<!-- b000262 | references | pages [26] -->
WingDouglas. (2009). Manual of leaf archetecture. The New York Botanic Garden.

<!-- b000263 | references | pages [26] -->
BuckA.L. (1981). New equations for computing vapor pressure and enhancement factor. J. Appl.

<!-- b000264 | references | pages [26] -->
Meteor., 20, 1527–1532.

<!-- b000265 | references | pages [26] -->
FisherB. and Honda, HJ. (1977). Computer simulation of branching pattern and geometry in

<!-- b000266 | references | pages [26] -->
Terminalia (combretaceae), a tropical tree. Botanical Gazette, 138, 377-384.

<!-- b000267 | references | pages [26] -->
FisherB. and Honda, HJ. (1979). Branch geometry and effective leaf area: a study of

<!-- b000268 | references | pages [26] -->
Terminalia-branching pattern (ch 66).

<!-- b000269 | references | pages [26] -->
http://www.infovisual.info/01/002_en.html. .

<!-- b000270 | references | pages [26] -->
http://www.math.smith.edu/phyllo//About/Classification.html. .

<!-- b000271 | references | pages [26] -->
JohnsonH.M. Thornley and Ian R.John. (1990). Plant and Crop Modelling. Oxford Science

<!-- b000272 | references | pages [26] -->
Publications.

<!-- b000273 | references | pages [26] -->
Monsiand Saeki, TM. (1953). Uber den Lichtfaktor in den Pflanzengesellschaften und seine

<!-- b000274 | references | pages [26] -->
Bedeutung fur die Stoffproduktion. 14, 22-52.

<!-- b000275 | references | pages [26] -->
NobelP. (1999). Physicochemical and Environmental Plant Physiology.

<!-- b000276 | references | pages [26] -->
SARAH J. COOKSON1VAN LIJSEBETTENS2 & CHRISTINE GRANIERMIEKE. (2005). Correlation

<!-- b000277 | references | pages [26] -->
between leaf growth variables suggest intrinsic and early controls of leaf size in

<!-- b000278 | references | pages [26] -->
Arabidopsis thaliana. Plant, Cell and Environment, 28, 1355–1366.

<!-- b000279 | references | pages [26] -->
ScurlockM. O., G. P. Asner, and S. T. GowerJ. (2001). Worldwide Historical Estimates and

<!-- b000280 | references | pages [26] -->
Bibliography of Leaf Area Index, 1932-2000. ORNL Technical Memorandum TM-2001/268,

<!-- b000281 | references | pages [26] -->
Oak Ridge National Laboratory.

<!-- b000282 | references | pages [26] -->
TsukayaHirokazu. (2006). Mechanism of Leaf-Shape Determination. The Annual Review of Plant

<!-- b000283 | references | pages [26] -->
Biology.

<!-- b000284 | heading | pages [27] -->
Appendix: Matlab code for implementing our model

<!-- b000285 | prose | pages [27] -->
%% Geometrical Generation of Vector Tree with Bifurcations % @para %     theta1,phi1,theta2,phi2: specified angular parameters; %     n: number of generations %     start: the height of the first branching point % output %     x,y,z: coordinate of the branching points of a tree function [x y z] = treeGeneration( theta1,phi1,theta2,phi2,n,start) A=[cos(phi1) sin(phi1) 0;-cos(theta1)*sin(phi1) cos(theta1)*cos(phi1) sin(theta1);sin(theta1)*sin(phi1) -sin(theta1)*cos(phi1) cos(theta1)]; B=[cos(phi2) sin(phi2) 0;-cos(theta2)*sin(phi2) cos(theta2)*cos(phi2) sin(theta2);sin(theta2)*sin(phi2) -sin(theta2)*cos(phi2) cos(theta2)]; temp=1:2^(n); temp=dec2bin(temp); [row col]=size(temp); result=zeros(3,3,row); for p=1:row result(:,:,p)=eye(3,3); end R=zeros(3,1,row); r=zeros(3,1,row); r(:,:,1)=[0,0,start]'; R(:,:,1)=[0,0,start]'; for i=2:row temp=dec2bin(i); for j=2:length(temp) i_j=double(temp(j))-double('0'); G_j=A^(1-i_j)*B^i_j; result(:,:,i)=G_j*result(:,:,i); end r(:,:,i)=result(3,:,i)'; r(:,:,i)=normrnd(1,0.1)*r(:,:,i); R(:,:,i)=R(:,:,floor(i/2))+r(:,:,i); end;

<!-- b000286 | prose | pages [27, 28] -->
x=zeros(1,row); y=zeros(1,row); z=zeros(1,row); for p=1:row x(1,p)=R(1,1,p); y(1,p)=R(2,1,p); z(1,p)=R(3,1,p); end; end %% Calculate Orthogonal Projection Given the Direction of the Sun Ray % Note: we calculate the area by adding the areas of discrete grids on the xy-plane %       where there exists overlapping with leaves. % @para %     inx,iny,inz: coordinates of the branching points of the tree %     theta1,phi1: the direction of the sun ray with respect to the original coordinates %     dimension: the dimension of the cumulating grids % Output %     area: the area of the projected shade function area = usefulArea( inx,iny,inz,theta1,phi1,dimension ) % change of the coordination system matrix=[inx;iny;inz]; A=[cos(phi1) sin(phi1) 0;-cos(theta1)*sin(phi1) cos(theta1)*cos(phi1) sin(theta1);sin(theta1)*sin(phi1) -sin(theta1)*cos(phi1) cos(theta1)]; matrix=A\matrix; x=matrix(1,:); y=matrix(2,:); z=matrix(3,:);

<!-- b000288 | prose | pages [28, 29] -->
xmin=min(x); xmax=max(x); ymin=min(y); ymax=max(y); nx=floor((xmax-xmin)/dimension); ny=floor((ymax-ymin)/dimension); area=0; for i=1:nx lowerx=xmin+(i-1)*dimension; higherx=xmin+i*dimension; temp1=(x >= lowerx & x <= higherx); for j=1:ny lowery=ymin+(j-1)*dimension; highery=ymin+j*dimension; temp2=(y >= lowery & y <= highery); points=sum(temp1 & temp2); if(points>0) area=area+dimension^2; end end end end
