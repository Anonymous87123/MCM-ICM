# P-A-2012-16831-ec8f03fd

Status: machine-draft; not source-verified.


<!-- b000001 | heading | pages [1] -->
Summary

<!-- b000002 | prose | pages [1] -->
In this article, we develop models to analyze leaves, including description and classification, their relations to overlap, distribution and branch structure, as well as leaf mass estimation.

<!-- b000003 | prose | pages [1] -->
Firstly we investigate the factors determining the diversity of leaves, and then several key parameters are chosen to describe leaves. Based on these parameters, a model for leaf classification using cluster analysis is provided, and model testing based on neural network shows the validity of the classification model.

<!-- b000004 | prose | pages [1] -->
To analyze the relation between leaf shape and overlap, we build a 3D projection analysis model with geometric method. We find that narrow leaves are generally less affected by overlap since they have a larger effective leaf area, and longer leave petioles are significant to decrease the overlap for broader leaves.

<!-- b000005 | prose | pages [1] -->
Assuming that narrowness of the leaves in a certain tree is identical, we focus on the relation between leaf size and its position within a tree crown. We figure out the light distribution in the tree, and illuminate the relation of light intensity and leaf size based on a revised Logistic model. We generally conclude that leaves on higher layers are larger than the lower ones in ideal condition, and leaves further from the trunk are larger than the central ones.

<!-- b000006 | prose | pages [1] -->
As for tree profiles, we divide branching patterns into two types: orthotropic and plagiotropic. A logistic regression model is developed and tested that demonstrates a strong relation between leaf shape and branch pattern. In detail, we use statistical method and conclude that orthotropic tree leaves are generally broader, larger and with longer petioles than that of plagiotropic trees. Reasonable explanations of the results are also provided.

<!-- b000007 | prose | pages [1] -->
Two methods are put forward to estimate total leaf mass. A volumetric model is built, and we multiply the volume of the crown by the leaf mass constant of the tree to estimate the total leaf mass. Another method involves allometric equations which describe the relations of leaf mass and tree parameters. Detailed comparison of both models show that a biological mechanism-based method, which indicates that leaf mass is a quadratic function of the diameter at breast height (DBH) of a tree, is the most accurate and convenient way to estimate leaf mass.

<!-- b000008 | prose | pages [1] -->
Sensitivity analysis of our models is provided, and a primary weakness of our work is a lack of enough data to test some of our models.

<!-- b000009 | furniture | pages [2] -->
#Team 16831

<!-- b000010 | furniture | pages [2] -->
Page 1 of 53

<!-- b000011 | heading | pages [2] -->
Contents

<!-- b000012 | contents | pages [2] -->
1. Introduction .................................................................. 2

<!-- b000013 | contents | pages [2] -->
2. Model of Leaf Description and Classification .............. 2

<!-- b000014 | contents | pages [2] -->
2.1

<!-- b000015 | contents | pages [2] -->
Introduction .................................................................................................................. 2

<!-- b000016 | contents | pages [2] -->
2.2

<!-- b000017 | contents | pages [2] -->
Leaf Classification Model .............................................................................................. 3

<!-- b000018 | contents | pages [2] -->
2.3

<!-- b000019 | contents | pages [2] -->
Model Testing Using Neural Network ........................................................................... 6

<!-- b000020 | contents | pages [2] -->
3. Model of the Relation between Leaf Shape and

<!-- b000021 | contents | pages [2] -->
Overlapping ....................................................................... 9

<!-- b000022 | contents | pages [2] -->
3.1

<!-- b000023 | contents | pages [2] -->
Building the Model ...................................................................................................... 12

<!-- b000024 | contents | pages [2] -->
3.2

<!-- b000025 | contents | pages [2] -->
Further Discussion ....................................................................................................... 20

<!-- b000026 | contents | pages [2] -->
3.3

<!-- b000027 | contents | pages [2] -->
Overall Conclusion ....................................................................................................... 21

<!-- b000028 | contents | pages [2] -->
3.4

<!-- b000029 | contents | pages [2] -->
Sensitivity Analysis ...................................................................................................... 22

<!-- b000030 | contents | pages [2] -->
4. Model of the Relation between Leaf Shape and Leaf

<!-- b000031 | contents | pages [2] -->
Distribution ...................................................................... 22

<!-- b000032 | contents | pages [2] -->
4.1

<!-- b000033 | contents | pages [2] -->
Light Distribution ......................................................................................................... 23

<!-- b000034 | contents | pages [2] -->
4.2

<!-- b000035 | contents | pages [2] -->
Leaf Size Model ........................................................................................................... 25

<!-- b000036 | contents | pages [2] -->
4.3

<!-- b000037 | contents | pages [2] -->
Result and Analysis ...................................................................................................... 27

<!-- b000038 | contents | pages [2] -->
5. Model of the Relation between Leaf Shape and

<!-- b000039 | contents | pages [2] -->
Branching Structure ........................................................ 28

<!-- b000040 | contents | pages [2] -->
5.1

<!-- b000041 | contents | pages [2] -->
Introduction ................................................................................................................ 28

<!-- b000042 | contents | pages [2] -->
5.2

<!-- b000043 | contents | pages [2] -->
Logistic Regression Model ........................................................................................... 28

<!-- b000044 | contents | pages [2] -->
5.3

<!-- b000045 | contents | pages [2] -->
Testing of the Model ................................................................................................... 29

<!-- b000046 | contents | pages [2] -->
5.4

<!-- b000047 | contents | pages [2] -->
Relations of Leaf Shape and Branch Pattern ............................................................... 30

<!-- b000048 | contents | pages [2] -->
5.5

<!-- b000049 | contents | pages [2] -->
Conclusions and Analysis ............................................................................................ 33

<!-- b000050 | contents | pages [2] -->
6. Model of Leaf Mass Estimation .................................. 33

<!-- b000051 | contents | pages [2] -->
6.1

<!-- b000052 | contents | pages [2] -->
A Basic Volumetric Model ........................................................................................... 33

<!-- b000053 | contents | pages [2] -->
6.2

<!-- b000054 | contents | pages [2] -->
An Improvement of the Model ................................................................................... 35

<!-- b000055 | contents | pages [2] -->
6.3

<!-- b000056 | contents | pages [2] -->
Allometric Equation Model ......................................................................................... 36

<!-- b000057 | contents | pages [2] -->
6.4

<!-- b000058 | contents | pages [2] -->
Conclusions and Overall Comparison of models ......................................................... 38

<!-- b000059 | contents | pages [2] -->
7. Strength and Weakness ............................................. 38

<!-- b000060 | contents | pages [2] -->
8. Further Work ............................................................... 40

<!-- b000061 | contents | pages [2] -->
9. A letter to Scientific Journal Editor ............................. 41

<!-- b000062 | contents | pages [2] -->
10.

<!-- b000063 | contents | pages [2] -->
Reference............................................................... 42

<!-- b000064 | contents | pages [2] -->
Appendix ......................................................................... 43

<!-- b000065 | furniture | pages [3] -->
#Team 16831

<!-- b000066 | furniture | pages [3] -->
Page 2 of 53

<!-- b000067 | contents | pages [3] -->
The Secrets of Leaves

<!-- b000068 | heading | pages [3] -->
1. Introduction

<!-- b000069 | prose | pages [3] -->
The leaves of trees are the common but essential organs to carry out photosynthesis. During the process of photosynthesis, they produce nutrition on which trees thrive. Scientific problems related to tree leaves are also drawing the attention of researchers. Such problems include the biological mechanism of leaves and so on. However, the factors that affect the shape of leaf is a problem seldom touched by previous researchers. What’s more, other valuable questions such as “Why do leaves have various shapes?”, “How can we estimate the leaf mass of a tree?” and ”How to classify leaves?” are also worth carefully studying. These are the questions we also focus on in this article.

<!-- b000070 | prose | pages [3] -->
In order to solve the questions above, we need to consult specific literature. Some of the previous work are done by Hirokazu Tsukaya on the mechanism of leaf-shape determination. Other researchers such as Akiotakenaka, Gretchen F. Sassenrath-Cole, Robin L.Chazd,ülo Niinemets and Lawren Sack have studied the relation bet between light distribution and tree structure and leaf shape. The researches on leaf classification have already been done by many researchers such as Chia-Ling Lee, Shu-Yuan Chen, B.D Ripley. Although many of the literature we refer to relates to the questions we are dealing with, none of them can generally answer our questions. Further modeling work is needed.

<!-- b000071 | prose | pages [3] -->
However, there are some tradeoffs limiting our modeling. Due to the difficulty in collecting data, our models are not fully tested by actual data, so we cannot ensure the validity when some of them are applied to all kinds of data. Besides, phenomena in biology are hard to analyze since some of them are caused by multiple factors, which affects the comprehensiveness of our models and make it nearly impossible to accurately conclude the answer. To sum up, our approaches are pretty clear: develop models on each of the problems, especially focusing on classification, leaf shape, the estimation of leaf mass and light interception of leaves. After formulating the models, we test our models making the best of the data we collect and analyze the sensitivity of our models.

<!-- b000072 | heading | pages [3] -->
2. Model of Leaf Description

<!-- b000073 | prose | pages [3] -->
and Classification

<!-- b000074 | heading | pages [3] -->
2.1 Introduction

<!-- b000075 | prose | pages [3, 4] -->
In order to describe and classify leaves, we firstly need to understand the causal factors that lead to the diversity of leaves shapes. We attribute the factors to the following two aspects:

<!-- b000076 | furniture | pages [4] -->
#Team 16831

<!-- b000077 | furniture | pages [4] -->
Page 3 of 53

<!-- b000079 | prose | pages [4] -->
 Genetype

<!-- b000080 | prose | pages [4] -->
The gene of a tree determine the shapes of leaves on a tree to a large degree. As we know, the shapes of a tree's leaves are a response to the tree species' long term ecological and evolutionary histories.

<!-- b000081 | prose | pages [4] -->
 Environment

<!-- b000082 | prose | pages [4] -->
An ecosystem's limiting factors may also modify the finished form and shape of a tree's leaves.

<!-- b000083 | prose | pages [4] -->
Considering that the genetype of a tree is also a response to the natural selection determined by the environment, we mainly focus on the impacts of environment.

<!-- b000084 | prose | pages [4] -->
Understanding of the "logic" behind the varied forms of leaves is facilitated by a firm grasp of the precise functions a leaf must accomplish: 1.  A leaf must "capture" sunlight for photosynthesis (in such a process it may also absorb a great deal of heat). 2.  A leaf must take in carbon dioxide from the surrounding air via pores (called "stomatae"). This carbon dioxide is also needed for photosynthesis. When these leaf stomatae are open to allow the uptake of carbon dioxide, water from inside the leaf is lost to the atmosphere. 3.  Transpiration. Leaf transpiration occurs through stomata, and can be thought of as a necessary "cost" associated with the opening of the stomata to allow the diffusion of carbon dioxide gas from the air for photosynthesis. Transpiration also cools plants and enables mass flow of mineral nutrients and water from roots to shoots. The leaf, then, is affected by these balancing acts: enough sunlight and carbon dioxide to run photosynthesis and transpiration. Knowing why leaves have various shapes, our next step is to determine the parameters which might be effected by the two functions listed above of leaves and also they can describe the shapes of leaves. Our goal is to build a mathematical model to describe and classify leaves using the parameters we find.

<!-- b000085 | heading | pages [4] -->
2.2 Leaf Classification Model

<!-- b000086 | heading | pages [4] -->
2.2.1 Leaf Description

<!-- b000087 | prose | pages [4] -->
We focus on four traditional parameters to describe the biodiversity of leaf shape: 1. Leaf index (a ratio of leaf length to leaf width), which describes the narrowness of leaf. 2. Leaf area. Here we use the product of length and width to approximate the area.

<!-- b000088 | furniture | pages [5] -->
#Team 16831

<!-- b000089 | furniture | pages [5] -->
Page 4 of 53

<!-- b000090 | prose | pages [5] -->
3. Non-serrated ratio(NR).

<!-- b000091 | prose | pages [5] -->
 N D Centroid Cc ( , ) / N i  NR i 1 eq1  M D Centroid Cv ( , ) / M j  j 1 Where

<!-- b000092 | prose | pages [5] -->
D X Y represents the distance between X and Y, ( , )

<!-- b000093 | prose | pages [5] -->
Centroid is the centroid of leaf.

<!-- b000094 | prose | pages [5] -->
Cc is the point on the concave part of the margin. i

<!-- b000095 | prose | pages [5] -->
Cv is the point on the convex part of the margin. j

<!-- b000096 | prose | pages [5] -->
Cc . N  is the total number of i

<!-- b000097 | prose | pages [5] -->
Cv . M  is the total number of j

<!-- b000098 | prose | pages [5] -->
NR can be used to determine the degree of serration of the margin, the smaller NR is, the sharper the serration is. Thus NR=1 means the leaf have smooth margin and NR=0 occures when the leaf is analogical to a maple leaf. 4. Leaf extended angle (LEA). The definitions of NR and LEA are presented visually in the figures below.

<!-- b000099 | caption | pages [5] -->
Figure 1. NR                                Figure 2. LEA

<!-- b000100 | heading | pages [5] -->
2.2.2 The Process of Classification based on cluster analysis

<!-- b000101 | prose | pages [5] -->
We calculate these parameters of 32 leaves from the 55 leave images we find in the literature(Chia-Ling Lee, Shu-Yuan Chen,2006),the detailed data and images can be viewed in the appendix.

<!-- b000102 | prose | pages [5] -->
Next, we classify the 32 leaves using the parameters we have. Since we don’t have any previous knowledge about how many classifications there should be, we do cluster analysis to classify these 32 samples (using R 2.13.1, the codes are presented in the appendix).

<!-- b000103 | prose | pages [5] -->
The result of clustering is displayed in Figure3.

<!-- b000104 | furniture | pages [6] -->
#Team 16831

<!-- b000105 | furniture | pages [6] -->
Page 5 of 53

<!-- b000106 | caption | pages [6] -->
Figure 3. cluster analysis

<!-- b000107 | caption | pages [6] -->
Figure 3 shows that the 32 samples can be classified into 4 clusters. Then we

<!-- b000108 | prose | pages [6] -->
match the cluster result with each of the images of leaves respectively, we obtain the classification below. Type 1

<!-- b000109 | prose | pages [6] -->
Type 2

<!-- b000110 | prose | pages [6] -->
Type 3

<!-- b000111 | prose | pages [6, 7] -->
Type 4 The figure above gives a visual result of classification where the leaves in the same classification are fairly similar with each other.

<!-- b000112 | furniture | pages [7] -->
#Team 16831

<!-- b000113 | furniture | pages [7] -->
Page 6 of 53

<!-- b000115 | heading | pages [7] -->
2.3 Model Testing Using Neural Network

<!-- b000116 | prose | pages [7] -->
Given the classification result above, now we are trying to classify the rest of the leaves in the database, that is, to determine which of the 4 types each of the rest belongs to. Such being the case, we choose randomly 8 samples from the rest to determine type of them. Based on neural network, the previous 32 samples are used as training samples and the 8 samples we just choose are used as testing samples. Next we present basic steps of formulating our neural network model.  Step 1. Data Pre-processing.

<!-- b000117 | prose | pages [7] -->
In order to obtain an effective training of neural networks, the numerical data should be scaled. This process is known as normalization. One form of suitable data normalization can be achieved using the following equation,which is known as Linear Transformation equation. The scaled variable should be within the range of 0 to 1.

<!-- b000118 | prose | pages [7] -->
 v v  v ' min  v v max min

<!-- b000119 | prose | pages [7] -->
Where： 'v   is the new feature value that has been normalized.

<!-- b000120 | prose | pages [7] -->
v is the minimum feature value in the data sample. min

<!-- b000121 | prose | pages [7] -->
v is the maximum feature value in the data sample. max

<!-- b000122 | prose | pages [7] -->
v    is the old feature value before normalization.  Step2.Building Back-Propagation Neural Network The Back-Propagation Neural Network (BPNN) is based on a supervised learning method, and is a generalization of the delta rule. It requires a teacher that knows, or can calculate, the desired output for any input in the training set. The BPNN architecture used as the classifier for this research (Figure 4) consists of four layers which are: Input Layer -- There are 4 neurons in the input layer for each predictor variable. Each of the neurons represents a parameter (either leaf index, leaf area, NR or LEA) that describes the leaf shape.

<!-- b000123 | furniture | pages [8] -->
#Team 16831

<!-- b000124 | furniture | pages [8] -->
Page 7 of 53

<!-- b000125 | prose | pages [8] -->
Hidden Layer -- This layer has one neuron for each case in the training dataset. The neuron stores the values of the predictor variables for the case along with the target value. In this case, there are 10 neurons in this layer. Decision Layer -- This layer divides the value accumulated in the numerator summation unit by the value in the denominator summation unit and uses the result as the predicted target value.

<!-- b000126 | caption | pages [8] -->
Figure 4. neural network

<!-- b000127 | prose | pages [8] -->
To sum up, the process of classifying new leaves using BP Neural Network can be illustrated by a simple flow chart presented below.

<!-- b000128 | caption | pages [8] -->
Figure 5. classifying process

<!-- b000129 | prose | pages [8] -->
In the BPNN model, some of the detailed parameters are listed below: net.trainParam.epochs=1000; net.trainParam.show=10; net.trainParam.lr=0.06; net.trainParam.goal=0.01; net.trainParam.min_grad = 1e-20;

<!-- b000130 | prose | pages [8] -->
Before displaying our classification results, we present an extra figure output from MaLab, which shows how the final result is approached. Figure 6 and Figure 7 are final results output from MatLab.

<!-- b000131 | furniture | pages [9] -->
#Team 16831

<!-- b000132 | furniture | pages [9] -->
Page 8 of 53

<!-- b000133 | caption | pages [9] -->
Figure 6                             Figure 7

<!-- b000134 | prose | pages [9] -->
To demonstrate the results with the images of leaves, we present the classification in the form below (NOTE that the images in rectangular frame represent the new leaves that are classified by BP Neural Network and add up to 8 in total): Type 1

<!-- b000135 | prose | pages [9] -->
Type 2

<!-- b000136 | prose | pages [9, 10] -->
Type3 Type 4

<!-- b000137 | furniture | pages [10] -->
#Team 16831

<!-- b000138 | furniture | pages [10] -->
Page 9 of 53

<!-- b000140 | caption | pages [10] -->
Figure 9. classifying result

<!-- b000141 | prose | pages [10] -->
As is shown in the results, except for the leaf in Type 3, rest of the leaves are correctly classified into the category of which the leaves are most analogical to it. Apparently, the testing results verify the validity of our model.

<!-- b000142 | heading | pages [10] -->
3. Model

<!-- b000143 | prose | pages [10] -->
of the Relation between Leaf Shape and Overlapping

<!-- b000144 | heading | pages [10] -->
Introduction

<!-- b000145 | prose | pages [10] -->
In this section, we mainly discuss the factors closely related to the overlapping area of a single branch. These factors include:

<!-- b000146 | prose | pages [10, 11] -->
solar altitude angle (SA-Angle) sunlight direction angle (SD-Angle) on horizontal plane narrowness of the leaf (Leaf index) petiole length (scaled to leaf area) leaf inclination angle (LI-Angle) internode length (scaled to leaf area). As we know, the leaf phyllotaxis (leaf pattern) describes the way how leaves are distributed along the shoot, and it has a great impact on the effectiveness of light capture efficiency of a shoot. Three representative phyllotaxes are shown below:

<!-- b000147 | furniture | pages [11] -->
#Team 16831

<!-- b000148 | furniture | pages [11] -->
Page 10 of 53

<!-- b000150 | caption | pages [11] -->
Figure 10.  distichous, decussate, spiral pattern

<!-- b000151 | prose | pages [11] -->
Source:  http://en.wikipedia.org/wiki/Phyllotaxy In our leaf overlapping model, we focused on a common scenario: distichous.

<!-- b000152 | heading | pages [11] -->
Assumptions

<!-- b000153 | prose | pages [11] -->
We simplified this pattern with some assumptions:  Each blade has unit area, and all blades are identical.  Since most leaves are roughly symmetric, we regard the blade shape as rhombus with 2 diagonal lines, which refer to the width and length respectively. The main purpose of this approximation is to simplify the computation and consider the key factor, narrowness, the most significant coefficient of the blade shape when we discuss the leaf overlapping.  The shoot radius is relatively small to blade, so is the radius of petiole, so we can neglect the shade of them both.  The curl and thickness of the leaf are neglected, which means we can view the blade as a thin palate.  The sunlight is the main light source, so we view the light is parallel.  We assume vertical shoot in the model. The change of light direction can be used to discuss the scenarios when shoot is not vertical.

<!-- b000154 | prose | pages [11] -->
Variable descriptions

<!-- b000155 | prose | pages [11] -->
Based on these assumptions, we build a 3D model of leaf overlapping as the figure given below.

<!-- b000156 | furniture | pages [12] -->
#Team 16831

<!-- b000157 | furniture | pages [12] -->
Page 11 of 53

<!-- b000158 | caption | pages [12] -->
Figure 11. A 3D model

<!-- b000159 | prose | pages [12] -->
*Note: the figure only shows a model with no petiole, a particular condition Now we give detailed definitions about the variables to build a 3D model to analyze the factors mentioned above.

<!-- b000160 | caption | pages [12] -->
Figure 12. schematic figure

<!-- b000161 | prose | pages [12] -->
The variables we define are as follow:

<!-- b000162 | caption | pages [12] -->
Table 1. variable definitions

<!-- b000163 | prose | pages [12, 13] -->
Variable name Corresponding note Value rage Physical Meaning 0°to  90° SA-Angle The altitude of  sunlight  0°to  360° SD-Angle The direction of sunlight Leaf-Index Height/Width Leaf-Index>0 Leaf narrowness

<!-- b000164 | furniture | pages [13] -->
#Team 16831

<!-- b000165 | furniture | pages [13] -->
Page 12 of 53

<!-- b000167 | prose | pages [13] -->
p-length Petiole/Leaf area p-length>=0  0°to  90° LI-Angle leaf inclination  H Inter-length /Leaf area Inter-length >0 Vertical distance between two neighboring layers

<!-- b000168 | prose | pages [13] -->
*Note: With the definition of Leaf-Index and Inter-length, we can analyze leaf with different size conveniently.

<!-- b000169 | heading | pages [13] -->
3.1 Building the Model

<!-- b000170 | prose | pages [13] -->
We mainly discuss the shoot with two layers of leaves following, because of the most significant impact is given by the neighboring layer above. That means we only need to consider 4 blade, 2 on upper layer, and 2 on down layer. To give the criteria of overlapping, effective area ratio (EAR) is defined by the formula below.

<!-- b000171 | prose | pages [13] -->
S  U EAR S total

<!-- b000172 | prose | pages [13] -->
S is the total leaf area that is not shaded, namely the effective area, Where U

<!-- b000173 | prose | pages [13] -->
S and is the total leaf area. total

<!-- b000174 | prose | pages [13] -->
Under this definition, our solution should be able to calculate the shaded area of the two leaves in down layer. That means, we should get the relation between the shade profile in upper layer and the profile of two leaves in down layer.

<!-- b000175 | prose | pages [13] -->
We focus on two types of blades:

<!-- b000176 | prose | pages [13] -->
 Horizontal Blade: leaves are perpendicular to branches

<!-- b000177 | prose | pages [13] -->
 Inclined blade: leaves are inclined to branches

<!-- b000178 | prose | pages [13] -->
They are showed below:

<!-- b000179 | furniture | pages [14] -->
#Team 16831

<!-- b000180 | furniture | pages [14] -->
Page 13 of 53

<!-- b000181 | prose | pages [14] -->
Horizontal Blade                        Inclined blade

<!-- b000182 | caption | pages [14] -->
Figure 13. schematic figure

<!-- b000183 | prose | pages [14] -->
In each scenario, we analyze two cases:

<!-- b000184 | prose | pages [14] -->
 The leave have no petiole;

<!-- b000185 | prose | pages [14] -->
 The leave have petiole;

<!-- b000186 | heading | pages [14] -->
3.1.1 Case 1: Horizontal Blade

<!-- b000187 | prose | pages [14] -->
(1) Without petiole

<!-- b000188 | prose | pages [14] -->
To build this model, we firstly consider a certain scenario, where the LI-Angle is zero, and the SA-Angle is 90 degree. In this case the blade plane is horizontal, and the sunlight is vertical. Obviously, the leaves on down layers are totally shaded, EAR=0.5.

<!-- b000189 | prose | pages [14] -->
We assume LI-Angle and p-length are zero now, and we will discuss their influence in later part. If we assume SA-Angle is 45 degree, the SD-Angle is 0, Leaf-Index is 1 (square shape), Inter-length is 0.4, the figures below will show what will happen.

<!-- b000190 | furniture | pages [15] -->
#Team 16831

<!-- b000191 | furniture | pages [15] -->
Page 14 of 53

<!-- b000192 | caption | pages [15] -->
Figure 14. A schematic figure

<!-- b000193 | prose | pages [15] -->
*Note: OL refers to overlapping area.

<!-- b000194 | prose | pages [15] -->
The upper layer curve is the profile of shade on down layer plane here. Down layer curve is the leaf profile. 3 OL part is she shaded area on down layer leaves.

<!-- b000195 | prose | pages [15] -->
Apparently, the upper layer curve is a congruent of the down layer curve with a certain displacement. This enables us to find a method to calculate the OL area. We need to calculate the displacement vector at first.

<!-- b000196 | prose | pages [15] -->
In 3D Cartesian coordinate system, the projection point (X’,Y’,Z’) by the sunlight of one certain point(X,Y,Z) on horizontal plane can be calculated as following.

<!-- b000197 | prose | pages [15] -->
      X ' 1 0 sin( SDAngle )tan( SAAngle ) X        Y ' 0 1 cos( SDAngle )tan( SAAngle ) Y           Z ' 0 0 0 Z     

<!-- b000198 | prose | pages [15] -->
The proof of this formula is easy with basic geometrical theory. So we omit this part in our article.

<!-- b000199 | prose | pages [15] -->
We denote the 3X3 matrix as TFM (transform matrix).

<!-- b000200 | prose | pages [15] -->
Tangent (SAAngle) here is 1 (SAAngle =45 degree), as a result, the trace of projection displacement vector can be described as： 

<!-- b000201 | heading | pages [15] -->
X SDAngle

<!-- b000202 | prose | pages [15] -->
sin( )Interlength

<!-- b000203 | prose | pages [15] -->
 Y cos( SDAngle )Interlength

<!-- b000204 | prose | pages [15] -->
The formula shows a circle trace of the vector endpoint.

<!-- b000205 | furniture | pages [16] -->
#Team 16831

<!-- b000206 | furniture | pages [16] -->
Page 15 of 53

<!-- b000207 | caption | pages [16] -->
Figure 15. a schematic figure

<!-- b000208 | caption | pages [16] -->
Figure 15 shows displacement with SDAngle=45,90,135 degree.

<!-- b000209 | prose | pages [16] -->
Noticing this phenomenon, we can calculate the OL area as following.

<!-- b000210 | caption | pages [16] -->
Figure 16. a magnification

<!-- b000211 | prose | pages [16] -->
We magnify the second figure to show how to caculate the OL area sidelength.

<!-- b000212 | prose | pages [16] -->
 CAB In triangle ABC, AB=displacment vector length , can be caculated with  ACB SDAngle and a certain apex angle of rhombus (determined by Leaf-Index) ,

<!-- b000213 | prose | pages [16] -->
eqauls to (180 angle).So BC is detemined in this triangle. Thus sidelength is

<!-- b000214 | prose | pages [16] -->
determined.

<!-- b000215 | prose | pages [16] -->
Omitting other geometrical caculation steps, we give the final expression of OL areas in common condition. The result depends on .

<!-- b000216 | prose | pages [16] -->
    0 (1) for : 0

<!-- b000217 | prose | pages [16, 17] -->
        2 2 sin( ) sin( ) m 1 m 1          0 0 S 2sin(2 ) ( h tan )( h tan ) OL 0   2 m sin(2 ) 2 m sin(2 ) 0 0       sin( )sin( ) (   2 0 0 h tan )  sin(2 ) 0 (2) for       180 0 0

<!-- b000218 | furniture | pages [17] -->
#Team 16831

<!-- b000219 | furniture | pages [17] -->
Page 16 of 53

<!-- b000221 | prose | pages [17] -->
        2 2 sin( ) sin( ) m 1 m 1          0 0 S 2sin(2 ) ( h tan )( h tan ) OL 0   2 m sin(2 ) 2 m sin(2 ) 0 0

<!-- b000222 | prose | pages [17] -->
     (3) for 180 180 0

<!-- b000223 | prose | pages [17] -->
          2 2 sin( 180 ) sin( 180 ) m 1 m 1          S 2sin(2 ) ( 0 h tan )( 0 h tan ) OL 0   2 m sin(2 ) 2 m sin(2 ) 0 0         sin( 180 )sin( 180 ) (    2 0 0 h tan )  sin(2 ) 0

<!-- b000224 | prose | pages [17] -->
Where m=LeafIndex

<!-- b000225 | prose | pages [17] -->
 =90 SAAngle

<!-- b000226 | prose | pages [17] -->
= Interlength h

<!-- b000227 | prose | pages [17] -->
=acrtan (1/m) is the critical angle when OL3 part is diminished. 0

<!-- b000228 | heading | pages [17] -->
Results and analysis:

<!-- b000229 | prose | pages [17] -->
S (unshaded area) —SAAngle curves with different Leaf-Index in We plot U

<!-- b000230 | prose | pages [17] -->
Matlab as following.

<!-- b000231 | furniture | pages [18] -->
#Team 16831

<!-- b000232 | furniture | pages [18] -->
Page 17 of 53

<!-- b000233 | prose | pages [18] -->
S (unshaded area)—SAAngle curves

<!-- b000234 | caption | pages [18] -->
Figure 17.

<!-- b000235 | prose | pages [18] -->
U

<!-- b000236 | prose | pages [18] -->
S , mean S value and some S values with particular SD-Angle U U U The max

<!-- b000237 | prose | pages [18] -->
are provided in the diagram below.

<!-- b000238 | caption | pages [18] -->
Table 2. Result

<!-- b000239 | prose | pages [18] -->
Leaf Max value 45 degree 0 degree Mean value

<!-- b000240 | prose | pages [18] -->
1:1 2.9714 2.8000 2.8914 2.8913

<!-- b000241 | prose | pages [18] -->
2:1 3.2800 3.0114 2.6800 2.9799

<!-- b000242 | prose | pages [18] -->
8:1 3.9200 3.6327 2.3700 3.4198

<!-- b000243 | prose | pages [18] -->
The mean value ratio of case 1:1 to case 8:1 is 0.845.

<!-- b000244 | prose | pages [18] -->
The maximal ratio of case 1:1 to case 8:1 is 0.758.

<!-- b000245 | heading | pages [18] -->
conclusions

<!-- b000246 | prose | pages [18] -->
From the figure and result above we can conclude:

<!-- b000247 | prose | pages [18] -->
S varies with Sunlight direction, and the maximum points lie when SAAngle is  U

<!-- b000248 | prose | pages [18] -->
0 or 90 degree.

<!-- b000249 | prose | pages [18] -->
S varies with different narrowness ratio significantly.  The maximum of U

<!-- b000250 | prose | pages [18] -->
Narrow leaves get a higher effective area both in maximum value and mean value than broader leaves.

<!-- b000251 | prose | pages [18] -->
(2) With petiole

<!-- b000252 | prose | pages [18] -->
The similar model is used to discuss the petiole length impact on effective area, with a slightly modification. S3 area in figure is largely determined by petiole length.

<!-- b000253 | prose | pages [18] -->
With a longer petiole length, the leaves can be more dispersive, thus a smaller shade will be projected on down layers. If we regard branch with leaves as a cylinder, then a longer petiole length means a lager radius of Cross-sectional circle.

<!-- b000254 | heading | pages [18] -->
Result and analysis

<!-- b000255 | prose | pages [18] -->
S We modified the expression (given in appendix) of OL areas, then plot a U

<!-- b000256 | prose | pages [18] -->
(unshaded area) —SAAngle curves with plength=0.2 as follow:

<!-- b000257 | furniture | pages [19] -->
#Team 16831

<!-- b000258 | furniture | pages [19] -->
Page 18 of 53

<!-- b000259 | prose | pages [19] -->
S (unshaded area)—SAAngle curves

<!-- b000260 | caption | pages [19] -->
Figure 17.

<!-- b000261 | prose | pages [19] -->
U

<!-- b000262 | prose | pages [19] -->
S , mean S and some S values with particular SD-Angle are The max U U U

<!-- b000263 | prose | pages [19] -->
provided in the diagram below.

<!-- b000264 | caption | pages [19] -->
Table 3. Result

<!-- b000265 | prose | pages [19] -->
Leaf Max value 45 degree 0 degree Mean value

<!-- b000266 | prose | pages [19] -->
1:1 2.9714 2.8000 2.9714 2.9169

<!-- b000267 | prose | pages [19] -->
2:1 3.2800 3.0114 2.7200 2.9877

<!-- b000268 | prose | pages [19] -->
8:1 3.9200 3.6327 2.3800 3.4204

<!-- b000269 | heading | pages [19] -->
Conclusions:

<!-- b000270 | prose | pages [19] -->
We can get several conclusions from the result above when compared with no petiole case.

<!-- b000271 | prose | pages [19] -->
 The broaden leaves are more sensitive to the petiole length, showing a higher

<!-- b000272 | prose | pages [19] -->
S in intervals around 0 and 180 degree, while the narrow leaves roughly U

<!-- b000273 | prose | pages [19] -->
remain unchanged with petiole length.

<!-- b000274 | prose | pages [19] -->
S value of broaden leaves increase faster than narrow leaves.  The mean U

<!-- b000275 | prose | pages [19] -->
Although the change is only 1 percent, the increasing speed will be much higher if we consider multi-layer leaves.

<!-- b000276 | heading | pages [19] -->
3.1.2 Case 2: Inclined Leaf Blade

<!-- b000277 | prose | pages [19, 20] -->
The basic model is given in part1, due to a lack of professional 3D simulation environment, it’s not practical to get the unshaded area directly. We mainly focused on getting the shade profiles of both layers, and approximate the areas from the shade profiles, using this ‘shade overlapping area ratio’ to approximately present the effective area on blades.

<!-- b000278 | furniture | pages [20] -->
#Team 16831

<!-- b000279 | furniture | pages [20] -->
Page 19 of 53

<!-- b000281 | prose | pages [20] -->
We firstly get all apexes coordinate from our 3D model, using coefficient of LI-Angle, Leaf-Index, SD-Angle, Inter-length to express the apex position. Using transform matrix we defined above, finally get the shade profile of two layers on horizontal plane.

<!-- b000282 | prose | pages [20] -->
We compared Leaf-Index of 8:1(Left row) with 1:1(Right row).

<!-- b000283 | prose | pages [20] -->
(1)  SDAngle is 0:

<!-- b000284 | caption | pages [20] -->
Figure 18. SDAngle is 0

<!-- b000285 | prose | pages [20] -->
(2) SDAngle is 45 degree:

<!-- b000286 | caption | pages [20] -->
Figure 18. SDAngle is 45 degree

<!-- b000287 | prose | pages [20] -->
(3)  SDAngle is 90 degree:

<!-- b000288 | furniture | pages [21] -->
#Team 16831

<!-- b000289 | furniture | pages [21] -->
Page 20 of 53

<!-- b000290 | caption | pages [21] -->
Figure 19. SDAngle is 90 degree

<!-- b000291 | heading | pages [21] -->
Result and analysis:

<!-- b000292 | prose | pages [21] -->
S in each case: The diagram below shows the U

<!-- b000293 | caption | pages [21] -->
Table 4. Result

<!-- b000294 | prose | pages [21] -->
SD-Angle in degree 0 45 90 Leaf-Index=1 2.379 2.871 2.894 Leaf-Index=8 2.294 3.512 3.793

<!-- b000295 | prose | pages [21] -->
Compare with the Table 2, we find that a 30 degree inclination angle will lead to

<!-- b000296 | prose | pages [21] -->
S in two cases where Leaf-Index=1 and a 2.6% and 3.2% decline of the max U

<!-- b000297 | prose | pages [21] -->
Leaf-Index=8. We use the summation of 3 results in each case above to estimate the mean value ratio. Based on the tendency of the curves we plot, we generally assume the max value is reached when SD-Angle is 90 degree.

<!-- b000298 | prose | pages [21] -->
The approximate mean value ratio of case 1:1 to case 8:1 is 0.848.

<!-- b000299 | prose | pages [21] -->
The max value ratio of case 1:1 to case 8:1 is 0.764.

<!-- b000300 | heading | pages [21] -->
Conclusions:

<!-- b000301 | prose | pages [21] -->
S with 2.6% and 3.2%  The 30 degree inclined leaf blade will get a smaller U

<!-- b000302 | prose | pages [21] -->
decline in two cases, which means inclined leaves has a less effective area ratio.  The mean value ratio of case 1:1 to case 8:1 and the max value ratio of case 1:1 to case 8:1 are roughly stay the same despite the 30 degree inclination angle.

<!-- b000303 | prose | pages [21] -->
That shows the narrow leaves are still more effective than the broaden leaves, the ratio of the two scenarios is not changed. They all declined with the inclination angle.

<!-- b000304 | heading | pages [21] -->
3.2 Further Discussion

<!-- b000305 | prose | pages [21] -->
Based on the overlapping analysis model we built before, we show a certain case of muti-layers leaf. We can see the total effective areas can be approximate by considering only one coefficient, the radius of the cylinder, if we only wish to make a rough estimation.

<!-- b000306 | furniture | pages [22] -->
#Team 16831

<!-- b000307 | furniture | pages [22] -->
Page 21 of 53

<!-- b000308 | caption | pages [22] -->
Figure 19. a common case

<!-- b000309 | prose | pages [22] -->
The figure shows the projection of effective blade area can be estimate by using rectangular d x h, which can be calculated by the equivalent cylinder. Therefore, the petiole length, narrowness are positive factors to the effective radius of the equivalent cylinder.

<!-- b000310 | heading | pages [22] -->
3.3 Overall Conclusion

<!-- b000311 | prose | pages [22] -->
The shape of leaves is closely related to the overlapping shadow. Narrow leaf is more effective in maximizing the exposure to sunlight, and it always works whether with or without petiole, blade inclination.

<!-- b000312 | prose | pages [22] -->
The broaden leaves tend to maximizing their light capture by extending their petiole.

<!-- b000313 | prose | pages [22] -->
However, it is still not easy to answer the question, “Do the shapes ‘minimize’ overlapping individual shadows that are cast, so as to maximize exposure?” Because the complication in ecosystem is far more than you can imagine, the leaf shape is determined by a great deal of factors, and the key factor is always different in different places.

<!-- b000314 | prose | pages [22] -->
So we give our final answer to the question as:  In areas where sunlight is the most important factor for trees to live, especially when sunlight is insufficient, they tend to minimize their overlapping shadow by generating a narrow leaf blade or a long petiole.  In areas where other factors (e.g. water) are more important than sunlight, they may not shape their leaves to minimize overlapping shadows.

<!-- b000315 | furniture | pages [23] -->
#Team 16831

<!-- b000316 | furniture | pages [23] -->
Page 22 of 53

<!-- b000317 | heading | pages [23] -->
3.4 Sensitivity Analysis

<!-- b000318 | prose | pages [23] -->
(1) In horizontal blade case, We make comparisons of Su of the leaves with petioles and the leaves without petioles. The result is as follows:

<!-- b000319 | prose | pages [23] -->
Case 1:1:

<!-- b000320 | prose | pages [23] -->
The max value is unchanged and the mean value increases by 1% Case 2:1 and Case 8:1:

<!-- b000321 | prose | pages [23] -->
The max value is unchanged and the mean value increases by less than 0.3% S variance with inclination angle, petiole (2) In our model, we mainly discuss U

<!-- b000322 | prose | pages [23] -->
S is not so U length and leaf index, the relation between these 3 factors with

<!-- b000323 | prose | pages [23] -->
S in one of the most representative U “self-evident”. Now we discuss the max

<!-- b000324 | prose | pages [23] -->
scenario, where SAAngle=45 degree, SDAngle=90 degree, Interlength=0.4, Leaf-index=1, petiolelength=0. If SAAngle, SDAngle, Interlength, Leaf-index increase 5% respectively, petiolength increase 0.05, The diagram below shows the variance ratio of each parameter. parameter S U Variance of Max

<!-- b000325 | prose | pages [23] -->
SAAngle 2.5% SDAngle -0.0167% Interlength 1.35% Leaf-index 0.0153% petiolelength 0

<!-- b000326 | prose | pages [23] -->
S U *Note: petiolelength effect mean value of

<!-- b000327 | prose | pages [23] -->
The sensitivity analysis above is quite different and the most significant 2 factors are SAAngle and interlength. Effective area are relatively insensitive to other factors.

<!-- b000328 | heading | pages [23] -->
4. Model

<!-- b000329 | prose | pages [23] -->
of the Relation between Leaf Shape and Leaf Distribution

<!-- b000330 | heading | pages [23] -->
Introduction

<!-- b000331 | prose | pages [23] -->
Since leaves on one tree are always analogical to each other due to the genetical reasons, in this section we neglect other parameters of the shape of leaves and only focus on the leaf blade area, namely the leaf size, variation due to spatial distribution of them.

<!-- b000332 | furniture | pages [24] -->
#Team 16831

<!-- b000333 | furniture | pages [24] -->
Page 23 of 53

<!-- b000334 | prose | pages [24] -->
However, the contributing factors to the leaf size of the same species is too many in natural environment, such as water supply, sunlight, wind, insects, branch angle, soil fertilize condition and so on. The spatial distribution of these factors is complicated and tough to make a comprehensively quantitative analysis. So we focused on the illumination distribution which is closely related to the leaf position in different part in the tree canopy. Therefore we are trying to find following relations: 1. The relation between layers of the canopy (the height of different layers) and illumination intensity. 2. The relation between horizontal position of leaf and illumination intensity. 3. The relation between leaf blade area and illumination intensity.

<!-- b000335 | prose | pages [24] -->
Combining these relations, we finally find the relation between leaf area and the distribution of leaf where distribution refers to both the horizontal and vertical position of leaves.

<!-- b000336 | heading | pages [24] -->
Assumptions

<!-- b000337 | prose | pages [24] -->
1. The illumination intensity on the same layer of canopy is only determined by the leaf height and the distance from the trunk. 2. When considering the factors to determine the leaf size, other external factors such as water and density of carbon dioxide are abundant for the survival of leaves. 3. The maximum leaf size exist which is determined by the tree species traits. We assume it to be a constant. 4. Leaf has a living and constructional energy cost.

<!-- b000338 | prose | pages [24] -->
Based on assumptions above, we build a light distribution model and a leaf size model.

<!-- b000339 | heading | pages [24] -->
4.1 Light Distribution

<!-- b000340 | heading | pages [24] -->
 Jackson’s model

<!-- b000341 | prose | pages [24] -->
In 1995, Jackson [15] built a model of the distribution of illumination intensity within the tree canopy, which is thought to be effective, shown as:

<!-- b000342 | prose | pages [24] -->
 

<!-- b000343 | heading | pages [24] -->
I I

<!-- b000344 | prose | pages [24] -->
0 exp( kl )

<!-- b000345 | prose | pages [24] -->
0I is the light intensity above the tree canopy; k is so-called light Where

<!-- b000346 | prose | pages [24] -->
absorption coefficient, which is determined by the tree characters including factors such as leaf optical traits the leaf inclination angle, branch structure and leaf density; l here refers to the vertical depths start from the top of canopy.

<!-- b000347 | furniture | pages [25] -->
#Team 16831

<!-- b000348 | furniture | pages [25] -->
Page 24 of 53

<!-- b000349 | prose | pages [25] -->
The formula clearly showed an exponentially declination of illumination intensity through vertical direction.

<!-- b000350 | heading | pages [25] -->
 Our model

<!-- b000351 | prose | pages [25] -->
If we consider the difference of illumination intensity on horizontal plane, which is significant in actual condition, the Jackson’s model apparently cannot show this factor.

<!-- b000352 | prose | pages [25] -->
Based on the model build by Jackson, we add a horizontal declination term to the equation. In consideration of the actual scenario, the declination speed in horizontal direction is much slower in compared with the vertical declination, since the light reflectance by leaf is always much greater than penetration. Therefore, we add a linear term and get an improved illumination intensity distribution as follows:

<!-- b000353 | prose | pages [25] -->
   

<!-- b000354 | heading | pages [25] -->
I I

<!-- b000355 | prose | pages [25] -->
0(1 D )exp( kl )

<!-- b000356 | prose | pages [25] -->
Where is the horizontal declination coefficient determined by the tree; D is the distance from the trunk of the tree canopy.

<!-- b000357 | caption | pages [25] -->
Figure 20. variable definition

<!-- b000358 | prose | pages [25] -->
The figure above shows the variables in the equation.

<!-- b000359 | prose | pages [25] -->
Coefficients,  and k , can be estimated by the actual illumination intensity in certain position, the center of top layer, on top layer surface, on bottom layer surface.

<!-- b000360 | prose | pages [25] -->
We simulate the distribution of light in Matlab, and get a surface of light distribution showing below.

<!-- b000361 | furniture | pages [26] -->
#Team 16831

<!-- b000362 | furniture | pages [26] -->
Page 25 of 53

<!-- b000363 | caption | pages [26] -->
Figure 21. light distribution within a tree

<!-- b000364 | heading | pages [26] -->
Result Analysis

<!-- b000365 | prose | pages [26] -->
We compare the tendency of the tree distribution with a series data of an apple tree in SUN’s paper [16]. The curve tendency matches pretty well. Considering the location of the tree, an orchard, where it is well irrigated, well fertilized and grown up with sufficient sunlight, we assume our model assumptions about the living condition is eligible. So we believe our model is well built.

<!-- b000366 | heading | pages [26] -->
4.2 Leaf Size Model

<!-- b000367 | heading | pages [26] -->
Analysis before modeling

<!-- b000368 | prose | pages [26] -->
It’s easy to know that leaf blade area increases when illumination strengthens since the process of photosynthesis becomes intensive and more nutrition is produced which will help the growth of leaf. However, the size of leaf cannot be infinitely large, that is, many limitations lying in environment condition (e.g. the density of carbon dioxide) and genetic factors may cause the termination of growing even if illumination intensity keeps strengthening.

<!-- b000369 | heading | pages [26] -->
Details of the model

<!-- b000370 | prose | pages [26] -->
Thus we consider using modified Logistic Model (Pierre Verhulst ,1838)  to analyze the relation between leaf area and illumination intensity. We give the modified equation and explain why we modify it. The leaf size is described by the differential equation:

<!-- b000371 | prose | pages [26, 27] -->
dS S   r I 0 (1 ) dI K Where: S refers to leaf blade area. I refers to illumination intensity. K refers to the upper limit of leaf blade area.

<!-- b000372 | furniture | pages [27] -->
#Team 16831

<!-- b000373 | furniture | pages [27] -->
Page 26 of 53

<!-- b000375 | prose | pages [27] -->
0r  refers to the size growth rate in the absence of external and internal limitations.

<!-- b000376 | prose | pages [27] -->
To show the relation between leaf size and light supply, we modified 2 terms in the equation, replacing S by I in describing the increasing rate, and replacing the temporal variable t by I. After the modification, the equation can describe the increasing rate, which is proportional to the product of light intensity and the 1 minus normalized size. This present the mechanism we discussed in Analysis part. The differential equation can be solved by integration of I and S respectively and simultaneously.

<!-- b000377 | prose | pages [27] -->
The equation has the following solution:

<!-- b000378 | prose | pages [27] -->
 S 1 1      2 2 0 K [1 (1 )exp( r I r I )]( I I )   0 0 0 0 S I ( ) K 2 2   0( I I )  0

<!-- b000379 | prose | pages [27] -->
Considering that leaves are not able to survive when the initial illumination

<!-- b000380 | prose | pages [27] -->
0I and 0S , referring to the critical intensity is too small, we give them initial value,

<!-- b000381 | prose | pages [27] -->
scenario when minimum leaf size possible. The curve of the solution is presented below.

<!-- b000382 | caption | pages [27] -->
Figure 21. relation of leaf blade area and light intensity

<!-- b000383 | prose | pages [27, 28] -->
In the figure above，we can see leaves cannot live in a weak-lighted area. If the light get stronger than the min light needed, the leaf blade area shows an approximately linear increasing, and when the leaf is approaching the maximum size possible, they show a slower increasing speed with a certain light increasing. This curve agrees with our common sense, in places where stronger sunlight can be seen, leaves are larger when they are matured, and leaf cannot live in dim light areas (e.g. under the bottom a canopy).The saturated light intensity can be seen in researches of photosynthesis.

<!-- b000384 | furniture | pages [28] -->
#Team 16831

<!-- b000385 | furniture | pages [28] -->
Page 27 of 53

<!-- b000387 | heading | pages [28] -->
4.3 Result and Analysis

<!-- b000388 | prose | pages [28] -->
The overall relation of leaf blade area and leaf distribution is as follows:

<!-- b000389 | prose | pages [28] -->
 S 1 1      2 2 0 K [1 (1 )exp( r I r I )]( I I )   0 0 0 0 S I ( ) K 2 2   0( I I )  0

<!-- b000390 | prose | pages [28] -->
Where    

<!-- b000391 | heading | pages [28] -->
I I

<!-- b000392 | prose | pages [28] -->
0(1 D )exp( kl )

<!-- b000393 | prose | pages [28] -->
D and l describe the position of the leaf. According to these two equations, we plot a surface to see how the leaves are distributed within a tree. We give the surface in following figure to show size distribution. According to these two models, we plot a surface to see how the leaves are distributed within the canopy of a tree. We give the surface in the following figure.

<!-- b000394 | caption | pages [28] -->
Figure 22. leaf area distribution

<!-- b000395 | prose | pages [28] -->
The figure above shows the leaf size distribution along vertical (height) and horizontal (radius) direction, the higher the larger, the closer to the truck the larger the larger is the leaf size.

<!-- b000396 | prose | pages [28] -->
From this figure we also find out that leaf size is more sensitive in vertical direction than horizontal. As a result the leaf size distribution is generally seen in the way that higher leaves are more possible to be larger.

<!-- b000397 | furniture | pages [29] -->
#Team 16831

<!-- b000398 | furniture | pages [29] -->
Page 28 of 53

<!-- b000399 | prose | pages [29] -->
However, in this figure, the down critical point of the weak light effect is not marked because of cumbersome calculation problems.

<!-- b000400 | heading | pages [29] -->
5. Model

<!-- b000401 | prose | pages [29] -->
of the Relation between Leaf Shape and Branching Structure

<!-- b000402 | heading | pages [29] -->
5.1 Introduction

<!-- b000403 | prose | pages [29] -->
The branching patterns of understory saplings and exposed canopy trees were classified as (David. A King et al 1999):

<!-- b000404 | prose | pages [29] -->
 Orthotropic: three-dimensional arrangements of leaves about ascending twigs

<!-- b000405 | prose | pages [29] -->
 Plagiotropic: leaves arranged in planes, usually along the sides of horizontal twigs

<!-- b000406 | prose | pages [29] -->
Orthotropic                           Plagiotropic

<!-- b000407 | caption | pages [29] -->
Figure 23. Orthotropic and Plagiotropic trees

<!-- b000408 | prose | pages [29] -->
In this section, we use these two categories to describe the branching structure of trees and each of them has its own unique characteristics in branching structures. In orthotropic branching, the axes are upwardly inclined and the leaves are arranged around them in more or less radial symmetry, whereas in plagiotropic branching, planes of foliage are formed from leaves arranged along the sides of nearly horizontal twigs (HalleÂ et al. 1978; Givnish 1984). Next, we will formulate a model to analyze the dependence of branching structures on three leaf parameters. And through this model, we can evaluate whether branching structures will effect leaf shape.

<!-- b000409 | heading | pages [29] -->
5.2 Logistic Regression Model

<!-- b000410 | prose | pages [29] -->
Discriminant analysis was used to determine the function that best separated the orthotropic and plagiotropic species in terms of the three measured leaf dimensions. The analysis was based on logistic regression (Ripley 1996), with the discriminant function taking the form:

<!-- b000411 | prose | pages [29, 30] -->
    d a b log( PL ) b log( BL ) b log( BW ) i i 1 2 3 Where: PL refers to petiole length of leaves BL refers to blade length of leaves BW refers to blade width of leaves i   refers to site and the leaf dimensions have been logarithmically transformed to make the distributions of the two architectural groups more nearly normal.

<!-- b000412 | furniture | pages [30] -->
#Team 16831

<!-- b000413 | furniture | pages [30] -->
Page 29 of 53

<!-- b000415 | prose | pages [30] -->
ia is a variable determined by latitude, and 1b , 2b , 3b are constants.

<!-- b000416 | prose | pages [30] -->
id  0 Orthotropy is expected for species for Which , and plagiotropy when

<!-- b000417 | prose | pages [30] -->
id  0 , with the

<!-- b000418 | prose | pages [30] -->
probability of orthotropy for a randomly selected species given as:

<!-- b000419 | prose | pages [30] -->
  d d ip e / (1 e ) i i

<!-- b000420 | prose | pages [30] -->
This discrimination function provides a convenient way to relate the branch pattern of a tree to its leaf shapes and a method to classify branch patterns according to the parameters of leaves.

<!-- b000421 | heading | pages [30] -->
5.3 Testing of the Model

<!-- b000422 | prose | pages [30] -->
By the work of David A. King [1999], the coefficients of the discriminant function are estimated, and the equation can be rewritten as:

<!-- b000423 | prose | pages [30] -->
     id 7.0 0.19 latitude 6.30log( PL ) 6.80log( BL ) 6.80log( BW )

<!-- b000424 | prose | pages [30] -->
    id 7.0 0.19 latitude 6.30log( PL ) 6.80log( BL BW / ) or

<!-- b000425 | prose | pages [30] -->
Using data from King [1999] who has collected the leaves and their parameters in five areas, we test the accuracy of the model and the result is as follows:

<!-- b000426 | caption | pages [30] -->
Table 5. classification result

<!-- b000427 | prose | pages [30] -->
Region 1 2 3 4 Total Total species 127 109 102 118 456 Correct-classified 126 93 90 105 414 species accuracy 0.99 0.85 0.88 0.89 0.91

<!-- b000428 | prose | pages [30] -->
Clear to see, this model has quite high accuracy and can be used to classify branch patterns according to the leaf parameters. On the other hand, the correctness of the model has demonstrated that the leaf shapes (blade length, blade width and petiole length) of trees are strongly related to the branch structure of trees. It is these three parameters that determine the branch pattern of a tree synthetically.

<!-- b000429 | furniture | pages [31] -->
#Team 16831

<!-- b000430 | furniture | pages [31] -->
Page 30 of 53

<!-- b000431 | heading | pages [31] -->
5.4 Relations of Leaf Shape and Branch Pattern

<!-- b000432 | prose | pages [31] -->
Having justified the close relation between leaf shapes and branch patterns, next we analyze the relation in detail. As we know, the blade length and petiole length are important indicators of leaf shapes. In the following figures we show the difference between the two branch patterns in these two parameters in the four regions.

<!-- b000433 | caption | pages [31] -->
Figure 23. differences of Orthotropic and Plagiotropic trees

<!-- b000434 | prose | pages [31] -->
For trees of the two patterns in the four areas, we investigate the relation of branch pattern and each of the leaf shape parameter individually. The parameters of leaves include:

<!-- b000435 | prose | pages [31] -->
 Petiole length

<!-- b000436 | prose | pages [31] -->
 Blade length

<!-- b000437 | prose | pages [31] -->
 Length-width ratio (leaf index)

<!-- b000438 | prose | pages [31] -->
 Simple or compound leaf

<!-- b000439 | prose | pages [31] -->
For the first three parameters, we use t-test to determine the relation between each parameter and the two branching patterns; a linear fitting is also shown to better demonstrate the relation between petiole length and Length-width ratio for orthotropy trees.

<!-- b000440 | furniture | pages [32] -->
#Team 16831

<!-- b000441 | furniture | pages [32] -->
Page 31 of 53

<!-- b000442 | prose | pages [32] -->
 petiole length The t-test result is as follows:

<!-- b000443 | caption | pages [32] -->
Table 6. petiole length

<!-- b000444 | prose | pages [32] -->
Mean log ( petiole length/cm) of species Rigion Plagiotropic orthotropic P 0.16±0.08 0.58±0.04 1 6.644e-16 0.23±0.03 0.47±0.03 2 2.836e-08 -0.16±0.02 0.32±0.04 3 5.596e-05 -0.04±0.01 0.24±0.02 4 4.106e-09

<!-- b000445 | prose | pages [32] -->
It can be easily seen from the table that Plagiotropic and orthotropic species differ sub-stantially in petiole length. Generally, the petiole length of orthotropic trees is notably larger than that of plagiotropic trees, and further explanation of this result will be provided hereinafter.

<!-- b000446 | prose | pages [32] -->
 blade length The t-test result is as follows:

<!-- b000447 | caption | pages [32] -->
Table 7. blade length

<!-- b000448 | prose | pages [32] -->
Mean log ( blade length/cm) of species Rigion Plagiotropic orthotropic P 1.29±0.04 1.39±0.02 1 3.621e-04 1.21±0.03 1.33±0.03 2 1.545e-03 1.21±0.02 1.31±0.04 3 4.322e-02 1.23±0.01 1.30±0.02 4 3.056e-03

<!-- b000449 | prose | pages [32] -->
The P-Value again shows that there exists true difference in mean between the blade length of plagiotropic and orthotropic trees. From the mean value we can see that from both the 4 regions the mean blade length of orthotropic trees is higher than plagiotropic trees, but not as notable as the comparison of petiole length.

<!-- b000450 | prose | pages [32] -->
 Length-width ratio (leaf index) The t-test result is as follows:

<!-- b000451 | caption | pages [32] -->
Table 8. leaf index

<!-- b000452 | prose | pages [32] -->
Mean log ( blade length/cm) of species Rigion Plagiotropic orthotropic P 2.39±0.15 1.87±0.09 1 6.261e-02 3.43±0.28 2.42±0.11 2 3.243e-04 3.56±0.14 2.21±0.06 3 1.275e-08 2.64±0.06 1.68±0.03 4 4.136e-06

<!-- b000453 | prose | pages [32, 33] -->
As we can see, the length-width ratio, which determine the narrowness of a leaf, differs significantly in the two branching patterns. Generally, the length-width ratio of orthotropic trees is smaller than plagiotropic trees, meaning that orthotropic tree leaves are relatively broader than plagiotropic trees. Meanwhile, considering the longer petiole of orthotropic trees, we try to find the relationship between these two characteristics. The figure below shows the relation of them for orthotropic trees.

<!-- b000454 | furniture | pages [33] -->
#Team 16831

<!-- b000455 | furniture | pages [33] -->
Page 32 of 53

<!-- b000457 | caption | pages [33] -->
Figure 23. relation of petiole length and length-width ratio

<!-- b000458 | prose | pages [33] -->
The figure shows a strong correlation between the petiole length and the length-width ratio of leaves. R2=0.86, demonstrating the accuracy of linear fitting. It means that when the length-width ratio of leaves increase, the petiole length grows accordingly.

<!-- b000459 | prose | pages [33] -->
 Simple or compound leaf We analyze the relation between whether a specie has simple or compound leaves and its branching pattern. Using data from King [1999], we get the proportion of these two types of leaves in the two branching patterns, respectively. The following figure shows the proportion in the 4 areas, and a total proportion is also considered.

<!-- b000460 | prose | pages [33] -->
250 100 Simple-leaved species 80 200 Compound-leaved 60 Simple-leaved 150 species species 40 100 Compound- 20 leaved species 50 0 SA-P CR-P NQ-O PA-P PA-O SA-O CR-O NQ-P 0 plagiotropic orthotropic

<!-- b000461 | caption | pages [33] -->
Figure 24. statistics in 4 areas            figure 25. total statistics

<!-- b000462 | prose | pages [33] -->
*Note: SA, PA, CR and NQ stand for four areas, and P, O stand for plagiotropic and orthotropic trees.

<!-- b000463 | furniture | pages [34] -->
#Team 16831

<!-- b000464 | furniture | pages [34] -->
Page 33 of 53

<!-- b000465 | prose | pages [34] -->
From the total statistics above we can figure out that for plagiotropic trees, simple-leaved species are in priority and reach a proportion of over 70%, while for orthotropic trees there is no significant difference between the amounts of these two kinds of species.

<!-- b000466 | heading | pages [34] -->
5.5 Conclusions and Analysis

<!-- b000467 | prose | pages [34] -->
From the statistical analysis above, we can get the following conclusions:  The branch patterns are strongly related to leaf shapes, including their petiole length, blade length, length-width ratio (leaf index), and it is a synthetic effect of all of them.  The petioles of orthotropic trees are generally longer than plagiotropic trees.  The length-width ratios (leaf index) of orthotropic trees are generally smaller than plagiotropic trees, meaning that the former have broader leaves than the latter.  The blade of orthotropic trees are generally longer than plagiotropic trees. Along with the point above, we can conclude that the leaf size of orthotropic trees are larger.  There is significant positive correlation between the length-width ratios and petiole length for orthotropic trees.  A majority of plagiotropic trees are simple-leaved while for orthotropic trees there are no notable differences.

<!-- b000468 | prose | pages [34] -->
As is discussed above, the major differences in leaf shapes for plagiotropic and orthotropic trees are that orthotropic trees have broader leaves and longer petioles. This can be explained by the overlap and photosynthesis efficiency of leaves. For plagiotropic trees, the effect of overlap is much smaller, so the petiole needn’t be long, whereas orthotropic species with orthotropic trees which have more steeply angled branches require longer petioles to avoid self-shading. It explains the positive correlation between the petiole length and length-width ratio for orthotropic trees, and more importantly, it is consistent with our model in Part II as well as previous literature such as the models of light interception in relation to leaf shape and phyllotaxis (Niklas 1988 and Takenaka 1994).

<!-- b000469 | heading | pages [34] -->
6. Model

<!-- b000470 | prose | pages [34] -->
of Leaf Mass Estimation

<!-- b000471 | heading | pages [34] -->
6.1 A Basic Volumetric Model

<!-- b000472 | prose | pages [34] -->
We use a volumetric method to estimate the leaf mass (LM) . Based on the idea of past studies, we use six geometric solids to approximate the tree crown shapes defined by their crown heights and mean crown radiuses: cylinder, vertical ellipsoid, paraboloid, cone, sphere, pyramid.

<!-- b000473 | furniture | pages [35] -->
#Team 16831

<!-- b000474 | furniture | pages [35] -->
Page 34 of 53

<!-- b000475 | prose | pages [35] -->
h

<!-- b000476 | prose | pages [35] -->
r

<!-- b000477 | caption | pages [35] -->
Figure 26. volumetric model

<!-- b000478 | prose | pages [35] -->
Then the leaf mass can be calculated:

<!-- b000479 | prose | pages [35] -->
Leaf mass= volume of geometric solids * leaf mass constant

<!-- b000480 | prose | pages [35] -->
The leaf mass constant (LMC) can be found in the literature. For example, for oak trees the value is approximately 280g/cm3 (). Then we need to calculate the volume of the geometric solids using the crown heights (CH) and mean crown radiuses (CR). If we use a cone to approximate the crown, the leaf mass for an oak tree can be calculated as follows:

<!-- b000481 | prose | pages [35] -->
1      2 LM V LMC r h 280 3 The following table shows the results using this model to estimate the leaf mass of 14 oak trees, and the measured leaf mass is also included:

<!-- b000482 | caption | pages [35] -->
Table 9. leaf mass estimation using volumetric model

<!-- b000483 | prose | pages [35, 36] -->
fraction to measured leaf mass tree CH(m) CR(m) Cylinder Vertical Paraboloid Cone Sphere Pyramid measured ellipsoid LM(g) 1 4.4 1.1 1.34 0.89 0.77 0.45 1.96 1.92 3500 2 4.1 2.0 1.48 0.99 0.85 0.49 3.95 0.64 9750 3 3.2 1.1 1.54 1.03 0.89 0.51 2.26 2.21 2210 4 6.3 1.4 2.08 1.38 1.19 0.69 3.88 1.84 5230 5 4.5 1.8 1.89 1.26 1.09 0.63 4.53 1.01 6790 6 4.5 1.2 2.92 1.25 1.68 0.97 4.68 3.52 1950 7 5.6 1.1 1.35 0.99 0.78 0.45 1.98 1.93 4420 8 5.0 1.5 1.84 1.23 1.06 0.61 3.68 1.42 5380 9 7.5 3.6 2.92 1.95 1.68 0.97 14.01 0.39 29300 10 2.8 1.1 1.63 1.09 0.94 0.54 2.39 2.33 1830 11 4.5 1.5 1.70 1.21 0.98 0.57 3.41 1.31 5230 12 4.6 1.2 2.65 1.37 1.32 0.88 4.24 3.19 2200 13 5.5 1.8 1.73 1.26 1.00 0.58 4.16 0.93 9040 14 2.0 2.1 1.31 0.87 0.75 0.44 3.66 0.51 5930

<!-- b000484 | furniture | pages [36] -->
#Team 16831

<!-- b000485 | furniture | pages [36] -->
Page 35 of 53

<!-- b000487 | prose | pages [36] -->
According to the result, the mean fraction for the respective six solids is as follows:

<!-- b000488 | caption | pages [36] -->
Table 10. a comparision

<!-- b000489 | prose | pages [36] -->
Cylinder Vertical Paraboloi Cone Sphere pyramid ellipsoid d mean fraction 1.80 1.18 1.09 0.60 3.44 1.75 to MLM

<!-- b000490 | prose | pages [36] -->
Clear to see, for paraboloid and vertical ellipsoid, mean fraction (also defined as the total leaf mass estimates factor) is 1.09 and 1.18 of the measured, respectively. Therefore, these two solids give estimates of total leaf mass within 12 percent of the measured, justifying that this model works well to give a relatively accurate estimate of leaf mass.

<!-- b000491 | heading | pages [36] -->
6.2 An Improvement of the Model

<!-- b000492 | prose | pages [36] -->
In the previous discussion we define the leaf-mass constant as a real “constant”, while this is not the actual case. As a tree grows up, the leaf-mass constant (namely, the ratio of leaf mass to crown volume) will decrease, because the outer surface of the crown tend to move up and out as the branches grow, so crown volume increases as the cube of the distance from the outer leave to the center of the tree. Thus, it is not hard to see that LMC will decrease as a tree grows (its crown volume increases). A notable example is the 9th tree in the table 1. When the crown volume V reaches a larger value, the fraction of both paraboloid and vertical ellipsoid is a little bit abnormal and inaccurate. On the other hand, it is easy to see that for the two best solids, paraboloid and vertical ellipsoid, the model both overestimate the actual LM. Thus, a decrease must be also needed to make up. For the two reasons above, we multiply an attenuation factor related to the crown volume to the previous equation:

<!-- b000493 | heading | pages [36] -->
V LMC e 

<!-- b000494 | prose | pages [36] -->
    V LM

<!-- b000495 | prose | pages [36] -->
λ=0.01 in the model. When crown volume V is small, the impact of H on LM is little and can be

<!-- b000496 | prose | pages [36] -->
e   V neglected. However, when crown volume V grows the impact of cannot be

<!-- b000497 | prose | pages [36] -->
overlooked. Using the improved model, we calculate the leaf mass above again (choosing the paraboloid and vertical ellipsoid models) and get the revised leaf mass. The result is as follows:

<!-- b000498 | caption | pages [36] -->
Table 11. two better estimation methods

<!-- b000499 | prose | pages [36] -->
vertical ellipsoid paraboloid

<!-- b000500 | furniture | pages [37] -->
#Team 16831

<!-- b000501 | furniture | pages [37] -->
Page 36 of 53

<!-- b000502 | heading | pages [37] -->
Basic model

<!-- b000503 | prose | pages [37] -->
1.18 1.09

<!-- b000504 | heading | pages [37] -->
Improved model

<!-- b000505 | prose | pages [37] -->
1.08 1.02

<!-- b000506 | prose | pages [37] -->
We can see that the revised model has truly improved the estimation and finally get highly accurate result.

<!-- b000507 | heading | pages [37] -->
6.3 Allometric Equation Model

<!-- b000508 | prose | pages [37] -->
In this model, we use a commonly used and conveniently measured parameter of a tree to estimate the leaf mass: the diameter at breast height (DBH). An equation is needed to relate DBH to the leaf mass of a tree.

<!-- b000509 | heading | pages [37] -->
6.3.1 A previous method

<!-- b000510 | prose | pages [37] -->
According to Nowak [1996], there is an allometric equation between these two variables:

<!-- b000511 | prose | pages [37] -->
  ln Y 7.6109 0.0643 X (equation 1)

<!-- b000512 | prose | pages [37] -->
Y is the leaf mass and X is DBH. It provides a relatively accurate and convenient method to approximate the leaf mass, but it overlooks the inner mechanism of the life of a tree and the result just comes from data fitting method.

<!-- b000513 | heading | pages [37] -->
6.3.2 A more accurate model considering the biological mechanism

<!-- b000514 | prose | pages [37] -->
of trees

<!-- b000515 | prose | pages [37] -->
We analyze the biological mechanism of trees to determine the relation between  LM and DBH. As we know, the mass of leaf is depended on its capacity to carry materials (mainly water), which is determined by the vascular system. The area of vascular system is proportional to the intersection area of the stem, which is proportional to the square of diameter or circumference. Thus, a second order equation can be used to describe the relation between DBH and LM:

<!-- b000516 | prose | pages [37] -->
(equation 2)    2 Y aX bX c

<!-- b000517 | prose | pages [37] -->
We use this equation to couple the data from Table 9 and get the following fitting result:

<!-- b000518 | furniture | pages [38] -->
#Team 16831

<!-- b000519 | furniture | pages [38] -->
Page 37 of 53

<!-- b000520 | caption | pages [38] -->
Figure 27. fitting of leaf mass and DBH

<!-- b000521 | prose | pages [38] -->
R2=0.98, showing a very accurate fitting result.

<!-- b000522 | prose | pages [38] -->
Using the data above, we can also plot the relation between DBH and LM using equation 1 and equation 2 and get the following result. The measured LM is also included in the figure.

<!-- b000523 | caption | pages [38] -->
Figure 28. a comparison of two allometric models

<!-- b000524 | prose | pages [38, 39] -->
It can be easily seen that the second model (two order allometric model) is better than the previous one in the literature, so we choose equation2 to estimate leaf mass of trees.

<!-- b000525 | furniture | pages [39] -->
#Team 16831

<!-- b000526 | furniture | pages [39] -->
Page 38 of 53

<!-- b000528 | heading | pages [39] -->
6.4 Conclusions and Overall Comparison of models

<!-- b000529 | prose | pages [39] -->
As is discussed above, we can get the following conclusions:

<!-- b000530 | prose | pages [39] -->
 For volumetric model, paraboloid and vertical ellipsoid solids are the best to approximate the crown profiles. Crown height and crown radius are used in the model, and for relatively higher trees, the tree height is also useful to get more accurate estimation.

<!-- b000531 | prose | pages [39] -->
 For allometric equation model, a second order equation related to DBH of trees is better and more convenient for estimation.

<!-- b000532 | prose | pages [39] -->
Using data from Table 9, we make a comparison of volumetric model and allometric model, the result shows that the mean fractions to measured LM using these two models are 0.93 and 1.03, respectively. Both of two models show high accuracy. However, considering that using AEM, we only need to measure DBH of a tree, which of quite convenient, so eventually we view the allometric equation model as the best to solve this problem.

<!-- b000533 | heading | pages [39] -->
7. Strength and Weakness

<!-- b000534 | heading | pages [39] -->
 Model of leaf shape description and classification

<!-- b000535 | heading | pages [39] -->
Strength

<!-- b000536 | prose | pages [39] -->
1. Since our model is built based on cluster analysis, the result of classification is approached completely by mathematical calculation which ensures there will be no subjective factors involved in the result.

<!-- b000537 | prose | pages [39] -->
2. The only inputs of our model are 4 parameters, no extra information needed to be provided.

<!-- b000538 | prose | pages [39] -->
3. According to the testing result, the validity of our model is verified.

<!-- b000539 | prose | pages [39] -->
4. This model can be used not only in leaves classification, but also any classification problems.

<!-- b000540 | heading | pages [39] -->
Weakness

<!-- b000541 | prose | pages [39] -->
1. This model is highly feasible when it is used to classify not too many leaves, once the amount of leaves gets too large, the amount of computation will be so excessive that it will take too much time finishing the classification.

<!-- b000542 | prose | pages [39] -->
2. The process of cluster may lack specialized support in botany.

<!-- b000543 | heading | pages [39] -->
 Model of the relation of leaf shape and overlap

<!-- b000544 | furniture | pages [40] -->
#Team 16831

<!-- b000545 | furniture | pages [40] -->
Page 39 of 53

<!-- b000546 | heading | pages [40] -->
Strength

<!-- b000547 | prose | pages [40] -->
1. A universal used method to calculate overlapping area in different cases 2. Clearly analytical expression is obtained, and the results are statistically characterized 3. Discuss all the 5 different variables sensitivity

<!-- b000548 | heading | pages [40] -->
Weakness

<!-- b000549 | prose | pages [40] -->
1. We only focused on leaves on one branch, failed to consider the impact by neighboring branches 2. Other complex factors (e.g. leaf flatness, unparalleled light), which may be significant as well, are not taken into consideration.

<!-- b000550 | heading | pages [40] -->
 Model of the relation of leaf shape and distribution

<!-- b000551 | heading | pages [40] -->
Strength

<!-- b000552 | prose | pages [40] -->
1. We build models from the mechanism of light intensity distribution which make sense reasonably 2. We find a simple but effective way to describe the leaf size and the light intensity 3. We neglected the detail structure within the tree, making it more generally applicable to different structures.

<!-- b000553 | heading | pages [40] -->
Weakness

<!-- b000554 | prose | pages [40] -->
1. The ideal assumptions about environment are somewhat too radical, maybe only few areas can fit it well 2. We need more data to test and revise our model 3. The coefficients are needed to be determined in either experimental way or empirical way to get a higher precise level

<!-- b000555 | heading | pages [40] -->
 Model of the relation of leaf shape and branching structure

<!-- b000556 | heading | pages [40] -->
Strength

<!-- b000557 | prose | pages [40] -->
1. We figure out the light intensity distribution in a tree based on the experiment data of previous researchers, and this simplified our model. 2. We successfully derived the relation between light intensity and leaf blade area based on Logistic model. 3. We draw the distribution figure so that the result is shown more clearly.

<!-- b000558 | heading | pages [40] -->
Weakness

<!-- b000559 | prose | pages [40] -->
1. We only focus on the leaf blade area, while did not consider the other leaf parameters to simplify the model. 2. We lack enough data to test our model.

<!-- b000560 | furniture | pages [41] -->
#Team 16831

<!-- b000561 | furniture | pages [41] -->
Page 40 of 53

<!-- b000562 | heading | pages [41] -->
 Model of leaf mass estimation

<!-- b000563 | heading | pages [41] -->
Strength

<!-- b000564 | prose | pages [41] -->
1. We build several models and make detailed comparison among them. 2. The volumetric method is quite easy to understand and calculate. 3. Our optimal method only needs the data of diameter at the breast height, which is convenient to measure, and the method has high accuracy.

<!-- b000565 | heading | pages [41] -->
Weakness

<!-- b000566 | prose | pages [41] -->
1. Some of the allometric equations are based on statistic method and lack theoretical support. 2. We haven’t thoroughly figure out the biological mechanism that determines leaf mass, and only a simplified biological analysis is considered

<!-- b000567 | heading | pages [41] -->
8. Further Work

<!-- b000568 | prose | pages [41] -->
Since ecological phenomena are multi-factor determined, we can do a lot of jobs about the leaves of a tree. Here we mention 2 important directions: 1. Consider the relation between water supply and mechanism of transpiration, and estimate its impact on the leaf shape and leaf mass. 2. Search more detailed data to clarify the cases where our models cannot be used

<!-- b000569 | furniture | pages [42] -->
#Team 16831

<!-- b000570 | furniture | pages [42] -->
Page 41 of 53

<!-- b000571 | heading | pages [42] -->
9. A letter to Scientific Journal

<!-- b000572 | prose | pages [42] -->
Editor Dear editor, In the contest, we developed models to analyze leaves, including description and classification, their relations with overlap, distribution and branching structure, as well as leaf mass estimation. We solved a series of problems on leaf shapes and leaf mass, and here are our key findings on these problems as listed below, and hopefully they have scientific value. 1. There are two main factors leading to the diversity of leaves—genetic and environmental factors. Genetic factor is determined by genes while environmental factor is dominated by three sub factors: sunlight, carbon dioxide and temperature. 2. Cluster analysis can be an effective method to classify leaves as long as we have the specific data on 4 parameters of leaves which refer to leaf index, leaf area, concave ratio and leaf extended angle. 3. The shape of leaves is closely related to the overlapping shadow. Narrow leaves tend to be more effective in maximizing the exposure to sunlight, and this conclusion always works whether petiole and blade inclination exist or not. Longer leaf petiole is significant to decrease the overlap for broader leaves. 4. Leaves on higher layers are generally larger than the lower ones in ideal condition, and leaves further from the trunk are larger than the central ones. 5. Branching patterns of trees are strongly related to leaf shapes, including their petiole length, blade length, length-width ratio (leaf index), and it is a synthetic effect of all of them. 6. Orthotropic tree leaves are generally broader, larger and with longer petioles than that of trees. 7. A majority of plagiotropic trees are simple-leaved while for orthotropic trees there are no notable differences on whether the leaves are simple or compound. 8. We can get the total leaf mass of a tree by multiplying the crown volume and leaf mass constant, and paraboloid is the optimal geometric solid to approximate the crown for crown volume calculation. 9. The total leaf mass is statistically related to the size characteristics of a tree. A biological mechanism-based method, which shows that leaf mass is a quadratic function of the diameter at breast height (DBH) of a tree, is the most accurate and convenient way to estimate leaf mass.

<!-- b000573 | prose | pages [42] -->
Since our findings are gained through both mathematical analysis and biological mechanism analysis, we really hope they will benefit the science research on tree leaves. Finally, thanks for your time.

<!-- b000574 | prose | pages [42] -->
BestRegards,

<!-- b000575 | furniture | pages [42] -->
Team # 16831

<!-- b000576 | furniture | pages [43] -->
#Team 16831

<!-- b000577 | furniture | pages [43] -->
Page 42 of 53

<!-- b000578 | heading | pages [43] -->
10. Reference

<!-- b000579 | references | pages [43] -->
[1]http://www.psu.edu/dept/nkbiology/naturetrail/leaves.htm

<!-- b000580 | references | pages [43] -->
[2]Zalikha Zulkifli  Puteh Saad  Itaza Afiani Mohtar  Plant Leaf Identification using Moment

<!-- b000581 | references | pages [43] -->
Invariants & General Regression Neural Network

<!-- b000582 | references | pages [43] -->
[3]Hirokazu Tsukaya  Mechanism of Leaf-Shape Determination  Annu. Rev. Plant Biol.2006.

<!-- b000583 | references | pages [43] -->
57:477–96

<!-- b000584 | references | pages [43] -->
[4]Ülo Niinemets and Lawren Sack   Structural determinants of leaf light-harvesting

<!-- b000585 | references | pages [43] -->
capacity and photosynthetic potentials

<!-- b000586 | references | pages [43] -->
Progress in Botany, Vol. 67 Springer-Verlag Berlin Heidelberg 2006

<!-- b000587 | references | pages [43] -->
[5]AKIO TAKENAKA ,Effects of leaf blade narrowness and petiole length on

<!-- b000588 | references | pages [43] -->
the light capture efficiency of a shoot , Ecological Research (1994) 9, 109-114

<!-- b000589 | references | pages [43] -->
[6]Chia-Ling Lee, Shu-Yuan Chen, Classification of Leaf Images, under grant NSC-95–2745-E-155–

<!-- b000590 | references | pages [43] -->
008-URD, 2006 Wiley Periodicals, Inc.

<!-- b000591 | references | pages [43] -->
[7]C. Faloutsos, R. Barber, M. Flickner, J. Hafner, W. Niblack, D. Petkovic,and W. Equitz, Efficient

<!-- b000592 | references | pages [43] -->
and effective querying by image content, J IntellInform Syst 3 (1994), 231–262

<!-- b000593 | references | pages [43] -->
[8]Zalikha Zulkifli, Puteh, SaadItaza, Afiani Mohtar

<!-- b000594 | references | pages [43] -->
Plant Leaf Identification using Moment Invariants & General Regression Neural Network

<!-- b000595 | references | pages [43] -->
978-1-4577-2152-6/11/$26.00_c 2011 IEEE

<!-- b000596 | references | pages [43] -->
[9]Akio Takenaka,  A Simulation Model of Tree Architecture Development

<!-- b000597 | references | pages [43] -->
Based on Growth Response to Local Light Environment

<!-- b000598 | references | pages [43] -->
Journal of Plant Research by The Botanical Society of Japan 1994

<!-- b000599 | references | pages [43] -->
[10]Daniel S. Falster and Mark Westoby , Leaf size and angle vary widely across species:

<!-- b000600 | references | pages [43] -->
what consequences for light interception

<!-- b000601 | references | pages [43] -->
New Phytologist(2003)158: 509–525   www.newphytologist.com

<!-- b000602 | references | pages [43] -->
[11]Magali Willaume . Pierre-Éric Lauri . Hervé Sinoquet, Light interception in apple trees

<!-- b000603 | references | pages [43] -->
influenced by canopy architecture manipulation Received: 5 November 2003 / Accepted: 24 June

<!-- b000604 | references | pages [43] -->
2004 / Published online: 29 July 2004  Springer-Verlag 2004

<!-- b000605 | references | pages [43] -->
[12]Aluru MR, Bae H,Wu D, Rodermel SR. 2001. The Arabidopsis immutans mutation affects

<!-- b000606 | references | pages [43] -->
plastid differentiation and the morphogenesis of white and green sectors in variegated

<!-- b000607 | references | pages [43] -->
plants. Plant Physiol. 127:67–77

<!-- b000608 | furniture | pages [44] -->
#Team 16831

<!-- b000609 | furniture | pages [44] -->
Page 43 of 53

<!-- b000610 | references | pages [44] -->
[13]Beerling DJ, Osborne CP, Chaloner WG. 2001. Evolution of leaf-form in land plants

<!-- b000611 | references | pages [44] -->
linked to atmospheric CO2 decline in the Late Palaeozoic era. Nature 410:352–54

<!-- b000612 | references | pages [44] -->
[14]Barritt B H. Vertical aris training seen as alternative for apple [J].

<!-- b000613 | references | pages [44] -->
Good Fruit Grower, 1998, 39 (3): 24-26.

<!-- b000614 | references | pages [44] -->
[15]Jackson J E. Theory of modeling by model hedgerow ordards in relation to latitude, time of

<!-- b000615 | references | pages [44] -->
the year and hedgerow configuration and orientation. J Apple Ecol, 1980, 9: 341-357.

<!-- b000616 | references | pages [44] -->
[16]SUN Zhi- hong1, WEI Qin- ping2*, YANG Chao- xuan3, SUN Zhong- fu4, WANG Xiao- wei2

<!-- b000617 | references | pages [44] -->
Relationships between distribution of r elative light intensity and shoots

<!-- b000618 | references | pages [44] -->
and foliage in different tier of canopy of Red Fuji apple trees with modified

<!-- b000619 | references | pages [44] -->
open centre tree shape

<!-- b000620 | references | pages [44] -->
[17]DAVID A. KING* and JOHN H. MAINDONALD, Tree architecture in relation to leaf dimensions

<!-- b000621 | references | pages [44] -->
and tree stature in temperate and tropical rain forests

<!-- b000622 | references | pages [44] -->
Journal of Ecology 1999,

<!-- b000623 | references | pages [44] -->
87, 1012±1024

<!-- b000624 | heading | pages [44] -->
Appendix

<!-- b000625 | prose | pages [44] -->
Appendix1:

<!-- b000626 | prose | pages [44] -->
The data extracted from the leaf images

<!-- b000627 | prose | pages [44, 45] -->
width length(in pixel)  Leaf index approximated area concave-ratio leaf extend  angle(roughly) Class1 101 108 1.069306931 5454 1 90 Class2 83 105 1.265060241 4357.5 1 180 Class3 146 47 0.321917808 3431 0.97 270 Class4 140 60 0.428571429 4200 0.3642 180 Class5  127 105 0.826771654 6667.5 1 180 Class6 141 74 0.524822695 5217 1 240 Class7 131 94 0.717557252 6157 0.2367 240 Class8 80 110 1.375 4400 1 60 Class9 73 106 1.452054795 3869 0.1781 60 Class10 87 104 1.195402299 4524 1 90 Class11 84 106 1.261904762 4452 1 120 Class12 56 104 1.857142857 2912 1 60 Class13 30 110 3.666666667 1650 1 120 Class14 69 102 1.47826087 3519 0.9333 120 Class15 100 93 0.93 4650 0.9 90 Class16 113 100 0.884955752 5650 1 180 Class17 90 94 1.044444444 4230 0.8333 150 Class18 50 106 2.12 2650 1 30 Class19 138 92 0.666666667 6348 0 360 Class22 44 94 2.136363636 2068 1 30 Class23 136 73 0.536764706 4964 0.3888 240 Class29 104 99 0.951923077 5148 1 180 Class31 51 106 2.078431373 2703 1 120 Class36 25 102 4.08 1275 1 30 Class38 114 108 0.947368421 6156 1 120 Class40 100 104 1.04 5200 0.95 180 Class47 117 98 0.837606838 5733 0.7614 180 Class48 81 95 1.172839506 3847.5 0.1852 90 Class50 111 76 0.684684685 4218 0 270 Class52 117 62 0.52991453 3627 0 360 Class53 101 60 0.594059406 3030 0.539 270 Class60 140 80 0.571428571 5600 0.84 240

<!-- b000628 | furniture | pages [45] -->
#Team 16831

<!-- b000629 | furniture | pages [45] -->
Page 44 of 53

<!-- b000631 | prose | pages [45] -->
cluster analysis code

<!-- b000632 | prose | pages [45] -->
R Code > rt2<-read.table("sj2.txt",head=T) > X<-scale(rt2,center=T,scale=T) > D2<-dist(X) > hc2<-hclust(D2,"ward") > plot(hc2,hang=-1,main="ward method") > rect.hclust(hc2,k=4)

<!-- b000633 | heading | pages [45] -->
Classification result of cluster analysis

<!-- b000634 | prose | pages [45, 46] -->
Name type Class1 3 Class2 4 Class3 1 Class4 1 Class5  3 Class6 1 Class7 1 Class8 4 Class9 4 Class10 4 Class11 4 Class12 2 Class13 2 Class14 4 Class15 4 Class16 3 Class17 4 Class18 2 Class19 1 Class22 2 Class23 1 Class29 3 Class31 2 Class36 2 Class38 3 Class40 3 Class47 3 Class48 4 Class50 1 Class52 1 Class53 1 Class60 1

<!-- b000635 | furniture | pages [46] -->
#Team 16831

<!-- b000636 | furniture | pages [46] -->
Page 45 of 53

<!-- b000638 | prose | pages [46] -->
Appendix2:

<!-- b000639 | prose | pages [46] -->
Neural Network simulation code in Task 1:

<!-- b000640 | prose | pages [46, 47] -->
clc ; clear; close all; %% loading data P0=load('trainning.txt'); P1=P0'; T0 = load('trainresult.txt'); T1=T0'; Ptem=load('testdata.txt'); P2 =Ptem'; PN1=P1; PN2=P2; net=newff(minmax(PN1),[10 1],{'tansig','purelin'},'trainlm'); net.trainParam.epochs=1000; net.trainParam.show=10; net.trainParam.lr=0.06; net.trainParam.goal=0.01; net.trainParam.min_grad = 1e-20; net=train(net,PN1,T1); %% simulation testing T_sim=sim(net,P2); %decision  process for i=1:length(T_sim) if T_sim(i)<=1.5 T_sim(i)=1; else if T_sim(i)>1.5&&T_sim(i)<=2.5 T_sim(i)=2; else if T_sim(i)>2.5&&T_sim(i)<=3.5 T_sim(i)=3; else T_sim(i)=4; end end end end disp('The type of the testing leaves:'); disp(T_sim);

<!-- b000641 | furniture | pages [47] -->
#Team 16831

<!-- b000642 | furniture | pages [47] -->
Page 46 of 53

<!-- b000644 | prose | pages [47] -->
Testing data extracted from leaf images:

<!-- b000645 | prose | pages [47] -->
width length Leaf index approximated area concave ratio leaf extend angle(roughly)

<!-- b000646 | prose | pages [47] -->
Class21 79 105 1.329113924 4147.5 1 120 Class24 58 106 1.827586207 3074 1 90 Class39 42 107 2.547619048 2247 1 90 Class51 49 66 1.346938776 1617 1 150 Class54 143 84 0.587412587 6006 0.7889 240 Class55 58 98 1.689655172 2842 1 90 Class57 51 91 1.784313725 2320.5 0.8627 60 Class59 68 98 1.441176471 3332 0.9471 60

<!-- b000647 | prose | pages [47] -->
Appendix3:

<!-- b000648 | prose | pages [47] -->
Overlapping analysis without petiole

<!-- b000649 | prose | pages [47] -->
clf;clc; x=0:pi/360:pi; for i=1:91;

<!-- b000650 | prose | pages [47, 48] -->
y(i)=2*(1-0.4*sin(pi/4-x(i))).*(1-0.4*cos(pi/4-x(i)))+0.4*sin(pi/4-x( i)).*0.4*cos(pi/4-x(i)); end for i=92:271 y(i)=2*(1-0.4*sin(x(i)-pi/4)).*(1-0.4*cos(x(i)-pi/4)); end for i=272:361

<!-- b000651 | furniture | pages [48] -->
#Team 16831

<!-- b000652 | furniture | pages [48] -->
Page 47 of 53

<!-- b000654 | prose | pages [48] -->
y(i)=2*(1-0.4*sin(-3*pi/4+x(i))).*(1-0.4*cos(-3*pi/4+x(i)))+0.4*sin(- 3*pi/4+x(i)).*0.4*cos(-3*pi/4+x(i)); end

<!-- b000655 | prose | pages [48] -->
plot(x/pi,4-y); hold on; crit=26.565*pi/180; si=sin(pi-2*crit); si2=sin(2*crit); t=0:0.1*pi/180:pi; for i=1:266

<!-- b000656 | prose | pages [48] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-t(i))/si).*(0.5*sqrt(5)-0.4*sin( t(i)+crit)/si)+0.4*0.8*(sin(crit-t(i))/si).*0.4*(sin(t(i)+crit)/si); end for i=267:1535

<!-- b000657 | prose | pages [48] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(t(i)-crit)/si).*(0.5*sqrt(5)-0.4*sin( pi-t(i)-crit)/si); end for i=1536:1801

<!-- b000658 | prose | pages [48] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-pi+t(i))/si).*(0.5*sqrt(5)-0.4*s in(pi-t(i)+crit)/si)+0.4*0.8*(sin(crit-pi+t(i))/si).*0.4*(sin(pi-t(i) +crit)/si); end

<!-- b000659 | prose | pages [48] -->
plot(t/pi,4-z,'r');

<!-- b000660 | prose | pages [48] -->
hold on; crit=7.125*pi/180; si=sin(pi-2*crit); si2=sin(2*crit); t=0:0.1*pi/180:pi; for i=1:72

<!-- b000661 | prose | pages [48] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-t(i))/si).*(0.25*sqrt(65)-0.4* sin(t(i)+crit)/si)+0.4*si2*(sin(crit-t(i))/si).*0.4*(sin(t(i)+crit)/s i);

<!-- b000662 | furniture | pages [49] -->
#Team 16831

<!-- b000663 | furniture | pages [49] -->
Page 48 of 53

<!-- b000664 | prose | pages [49] -->
end for i=73:1729

<!-- b000665 | prose | pages [49] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(t(i)-crit)/si).*(0.25*sqrt(65)-0.4* sin(pi-t(i)-crit)/si); end for i=1730:1801

<!-- b000666 | prose | pages [49] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-pi+t(i))/si).*(0.25*sqrt(65)-0 .4*sin(pi-t(i)+crit)/si)+0.4*si2*(sin(crit-pi+t(i))/si).*0.4*(sin(pi- t(i)+crit)/si); end maxvalue(1)=4-min(y); maxvalue(2)=4-min(z); maxvalue(3)=4-min(g); disp('maxvalue'); disp(maxvalue); degree(1)=4-y(91); degree(2)=4-z(451); degree(3)=4-g(451); disp('45 degree'); disp(degree); degree(1)=4-y(1); degree(2)=4-z(1); degree(3)=4-g(1); disp('0 degree'); disp(degree); meanvalue(1)=4-mean(y); meanvalue(2)=4-mean(z); meanvalue(3)=4-mean(g); disp('meanvalue'); disp(meanvalue); plot(t/pi,4-g,'g');

<!-- b000667 | prose | pages [49] -->
Overlapping analysis with petiole

<!-- b000668 | prose | pages [49] -->
clf;clc; x=0:pi/360:pi; for i=1:91;

<!-- b000669 | prose | pages [49, 50] -->
y(i)=2*(1-0.4*sin(pi/4-x(i))).*(1-0.4*cos(pi/4-x(i))); end for i=92:271 y(i)=2*(1-0.4*sin(x(i)-pi/4)).*(1-0.4*cos(x(i)-pi/4)); end for i=272:361 y(i)=2*(1-0.4*sin(-3*pi/4+x(i))).*(1-0.4*cos(-3*pi/4+x(i))); end figure(3); plot(x/pi,4-y); hold on; crit=26.565*pi/180; si=sin(pi-2*crit); si2=sin(2*crit); t=0:0.1*pi/180:pi; for i=1:266

<!-- b000670 | furniture | pages [50] -->
#Team 16831

<!-- b000671 | furniture | pages [50] -->
Page 49 of 53

<!-- b000673 | prose | pages [50] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-t(i))/si).*(0.5*sqrt(5)-0.4*sin( t(i)+crit)/si); end for i=267:1535

<!-- b000674 | prose | pages [50] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(t(i)-crit)/si).*(0.5*sqrt(5)-0.4*sin( pi-t(i)-crit)/si); end for i=1536:1801

<!-- b000675 | prose | pages [50] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-pi+t(i))/si).*(0.5*sqrt(5)-0.4*s in(pi-t(i)+crit)/si); end plot(t/pi,4-z,'r');

<!-- b000676 | prose | pages [50] -->
hold on; crit=7.125*pi/180; si=sin(pi-2*crit); si2=sin(2*crit); t=0:0.1*pi/180:pi; for i=1:72

<!-- b000677 | prose | pages [50] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-t(i))/si).*(0.25*sqrt(65)-0.4* sin(t(i)+crit)/si); end for i=73:1729

<!-- b000678 | prose | pages [50, 51] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(t(i)-crit)/si).*(0.25*sqrt(65)-0.4* sin(pi-t(i)-crit)/si); end for i=1730:1801

<!-- b000679 | furniture | pages [51] -->
#Team 16831

<!-- b000680 | furniture | pages [51] -->
Page 50 of 53

<!-- b000682 | prose | pages [51] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-pi+t(i))/si).*(0.25*sqrt(65)-0 .4*sin(pi-t(i)+crit)/si); end plot(t/pi,4-g,'g'); maxvalue(1)=4-min(y); maxvalue(2)=4-min(z); maxvalue(3)=4-min(g); disp('maxvalue'); disp(maxvalue); degree(1)=4-y(91); degree(2)=4-z(451); degree(3)=4-g(451); disp('45 degree'); disp(degree); degree(1)=4-y(1); degree(2)=4-z(1); degree(3)=4-g(1); disp('0 degree'); disp(degree); meanvalue(1)=4-mean(y); meanvalue(2)=4-mean(z); meanvalue(3)=4-mean(g); disp('meanvalue'); disp(meanvalue);

<!-- b000683 | prose | pages [51] -->
Overlapping plotting with 30 degree inclination

<!-- b000684 | prose | pages [51] -->
clf; h=0.4; %%internode length ,can be revised incang=pi/6; %%inclination angle, can be revised sunang=pi/2; %%sun direction angle, can be revised

<!-- b000685 | prose | pages [51] -->
m=8; %%leaf index, can be revised

<!-- b000686 | prose | pages [51] -->
b=sqrt(2*m); a=sqrt(2/m); Transform_matrix=[1,0,-sin(sunang);0,1,-cos(sunang);0,0,0]; A=[0;0;h]; B=[a;cos(incang)*b;h+sin(incang)*b]; C=[0;2*cos(incang)*b;h+sin(incang)*2*b]; D=[-a;cos(incang)*b;h+sin(incang)*b];

<!-- b000687 | furniture | pages [52] -->
#Team 16831

<!-- b000688 | furniture | pages [52] -->
Page 51 of 53

<!-- b000689 | prose | pages [52] -->
E=[a;-cos(incang)*b;h+sin(incang)*b]; F=[0;-2*cos(incang)*b;h+sin(incang)*2*b]; G=[-a;-cos(incang)*b;h+sin(incang)*b]; A2=Transform_matrix*A B2=Transform_matrix*B C2=Transform_matrix*C D2=Transform_matrix*D E2=Transform_matrix*E F2=Transform_matrix*F G2=Transform_matrix*G points=[A2,B2,C2,D2,A2,E2,F2,G2,A2]; x=points(1,:); y=points(2,:); z=[0,0,0,0,0,0,0,0,0]; plot3(x,y,z); grid;

<!-- b000690 | prose | pages [52] -->
h=0.0; A=[0;0;h]; B=[a;cos(incang)*b;h+sin(incang)*b]; C=[0;2*cos(incang)*b;h+sin(incang)*2*b]; D=[-a;cos(incang)*b;h+sin(incang)*b]; E=[a;-cos(incang)*b;h+sin(incang)*b]; F=[0;-2*cos(incang)*b;h+sin(incang)*2*b]; G=[-a;-cos(incang)*b;h+sin(incang)*b]; A2=Transform_matrix*A B2=Transform_matrix*B C2=Transform_matrix*C D2=Transform_matrix*D E2=Transform_matrix*E F2=Transform_matrix*F G2=Transform_matrix*G points=[A2,B2,C2,D2,A2,E2,F2,G2,A2];

<!-- b000691 | prose | pages [52] -->
x=points(1,:); y=points(2,:);

<!-- b000692 | prose | pages [52] -->
z=[0,0,0,0,0,0,0,0,0]; hold on; plot3(x,y,z,'r'); xlabel('X'); ylabel('Y');

<!-- b000693 | furniture | pages [53] -->
#Team 16831

<!-- b000694 | furniture | pages [53] -->
Page 52 of 53

<!-- b000695 | prose | pages [53] -->
Appendix3:

<!-- b000696 | prose | pages [53] -->
Surface of distribution plotting codes

<!-- b000697 | prose | pages [53] -->
% illumination intensity distribution a=0.02; b=0.8; c=0.1; r=linspace(0, 10, 25); h=linspace(0, 10, 25); [r1,h1]=meshgrid(r, h); L=(a*r1+b).*exp(-c*(10-h1)); surf(r1, h1, L); xlabel('radius'); ylabel('height'); zlabel('relative illumination intensity'); title('light distribustion within a tree');

<!-- b000698 | prose | pages [53] -->
% blade area distribution a=0.04; b=0.8; c=0.1; S0=40; Sm=500; k=0.4; r=linspace(0, 10, 25); h=linspace(0, 10, 25); [r1,h1]=meshgrid(r, h); L=(a*r1+b).*exp(-c*(10-h1)); S=S0*Sm./(S0+(Sm-S0).*exp(-k.*L)); surf(r1,h1,S); % »-³öÁ¢ÌåÇúÃæÍ¼ xlabel('radius(m)'); ylabel('height(m)'); zlabel('area(mm2)'); title('leaf area distribution');

<!-- b000699 | prose | pages [53, 54] -->
Curve of light intensity with blade area plotting code I=0:0.05:35; for i=1:101 S(i)=0; end for i=102:701 S(i)=(1-(0.8)*exp(-0.012*I(i).^2+0.012*5.^2)); end plot(I,S); xlabel('illumination intensity'); ylabel('leaf blade area');

<!-- b000700 | furniture | pages [54] -->
#Team 16831

<!-- b000701 | furniture | pages [54] -->
Page 53 of 53
