# P-A-2012-16831-ec8f03fd

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->


<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->


<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | furniture | pages [1] -->


<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | furniture | pages [1] -->


<!-- b000011 | heading | pages [1] -->
Summary

<!-- b000012 | prose | pages [1] -->
In this article, we develop models to analyze leaves, including description and classification, their relations to overlap, distribution and branch structure, as well as leaf mass estimation.

<!-- b000013 | prose | pages [1] -->
Firstly we investigate the factors determining the diversity of leaves, and then several key parameters are chosen to describe leaves. Based on these parameters, a model for leaf classification using cluster analysis is provided, and model testing based on neural network shows the validity of the classification model.

<!-- b000014 | prose | pages [1] -->
To analyze the relation between leaf shape and overlap, we build a 3D projection analysis model with geometric method. We find that narrow leaves are generally less affected by overlap since they have a larger effective leaf area, and longer leave petioles are significant to decrease the overlap for broader leaves.

<!-- b000015 | prose | pages [1] -->
Assuming that narrowness of the leaves in a certain tree is identical, we focus on the relation between leaf size and its position within a tree crown. We figure out the light distribution in the tree, and illuminate the relation of light intensity and leaf size based on a revised Logistic model. We generally conclude that leaves on higher layers are larger than the lower ones in ideal condition, and leaves further from the trunk are larger than the central ones.

<!-- b000016 | prose | pages [1] -->
As for tree profiles, we divide branching patterns into two types: orthotropic and plagiotropic. A logistic regression model is developed and tested that demonstrates a strong relation between leaf shape and branch pattern. In detail, we use statistical method and conclude that orthotropic tree leaves are generally broader, larger and with longer petioles than that of plagiotropic trees. Reasonable explanations of the results are also provided.

<!-- b000017 | prose | pages [1] -->
Two methods are put forward to estimate total leaf mass. A volumetric model is built, and we multiply the volume of the crown by the leaf mass constant of the tree to estimate the total leaf mass. Another method involves allometric equations which describe the relations of leaf mass and tree parameters. Detailed comparison of both models show that a biological mechanism-based method, which indicates that leaf mass is a quadratic function of the diameter at breast height (DBH) of a tree, is the most accurate and convenient way to estimate leaf mass.

<!-- b000018 | prose | pages [1] -->
Sensitivity analysis of our models is provided, and a primary weakness of our work is a lack of enough data to test some of our models.

<!-- b000019 | furniture | pages [2] -->
#Team 16831

<!-- b000020 | furniture | pages [2] -->
Page 1 of 53

<!-- b000021 | furniture | pages [2] -->


<!-- b000022 | heading | pages [2] -->
Contents

<!-- b000023 | contents | pages [2] -->
1. Introduction .................................................................. 2

<!-- b000024 | contents | pages [2] -->
2. Model of Leaf Description and Classification .............. 2

<!-- b000025 | contents | pages [2] -->
2.1

<!-- b000026 | contents | pages [2] -->
Introduction .................................................................................................................. 2

<!-- b000027 | contents | pages [2] -->
2.2

<!-- b000028 | contents | pages [2] -->
Leaf Classification Model .............................................................................................. 3

<!-- b000029 | contents | pages [2] -->
2.3

<!-- b000030 | contents | pages [2] -->
Model Testing Using Neural Network ........................................................................... 6

<!-- b000031 | heading | pages [2] -->
3. Model of the Relation between Leaf Shape and

<!-- b000032 | prose | pages [2] -->
Overlapping ....................................................................... 9

<!-- b000033 | prose | pages [2] -->
3.1 Building the Model ...................................................................................................... 12 3.2 Further Discussion ....................................................................................................... 20 3.3 Overall Conclusion ....................................................................................................... 21 3.4 Sensitivity Analysis ...................................................................................................... 22

<!-- b000034 | heading | pages [2] -->
4. Model of the Relation between Leaf Shape and Leaf

<!-- b000035 | prose | pages [2] -->
Distribution ...................................................................... 22

<!-- b000036 | prose | pages [2] -->
4.1 Light Distribution ......................................................................................................... 23 4.2 Leaf Size Model ........................................................................................................... 25 4.3 Result and Analysis ...................................................................................................... 27

<!-- b000037 | heading | pages [2] -->
5. Model of the Relation between Leaf Shape and

<!-- b000038 | prose | pages [2] -->
Branching Structure ........................................................ 28

<!-- b000039 | prose | pages [2] -->
5.1 Introduction ................................................................................................................ 28 5.2 Logistic Regression Model ........................................................................................... 28 5.3 Testing of the Model ................................................................................................... 29 5.4 Relations of Leaf Shape and Branch Pattern ............................................................... 30 5.5 Conclusions and Analysis ............................................................................................ 33 6. Model of Leaf Mass Estimation .................................. 33 6.1 A Basic Volumetric Model ........................................................................................... 33 6.2 An Improvement of the Model ................................................................................... 35 6.3 Allometric Equation Model ......................................................................................... 36 6.4 Conclusions and Overall Comparison of models ......................................................... 38 7. Strength and Weakness ............................................. 38 8. Further Work ............................................................... 40 9. A letter to Scientific Journal Editor ............................. 41 10.

<!-- b000040 | prose | pages [2] -->
Reference............................................................... 42 Appendix ......................................................................... 43

<!-- b000041 | furniture | pages [2] -->


<!-- b000042 | furniture | pages [2] -->


<!-- b000043 | furniture | pages [2] -->


<!-- b000044 | furniture | pages [3] -->
#Team 16831

<!-- b000045 | furniture | pages [3] -->
Page 2 of 53

<!-- b000046 | furniture | pages [3] -->


<!-- b000047 | prose | pages [3] -->
The Secrets of Leaves

<!-- b000048 | furniture | pages [3] -->


<!-- b000049 | heading | pages [3] -->
1. Introduction

<!-- b000050 | prose | pages [3] -->
The leaves of trees are the common but essential organs to carry out photosynthesis. During the process of photosynthesis, they produce nutrition on which trees thrive. Scientific problems related to tree leaves are also drawing the attention of researchers. Such problems include the biological mechanism of leaves and so on. However, the factors that affect the shape of leaf is a problem seldom touched by previous researchers. What’s more, other valuable questions such as “Why do leaves have various shapes?”, “How can we estimate the leaf mass of a tree?” and ”How to classify leaves?” are also worth carefully studying. These are the questions we also focus on in this article.

<!-- b000051 | prose | pages [3] -->
In order to solve the questions above, we need to consult specific literature. Some of the previous work are done by Hirokazu Tsukaya on the mechanism of leaf-shape determination. Other researchers such as Akiotakenaka, Gretchen F. Sassenrath-Cole, Robin L.Chazd,ülo Niinemets and Lawren Sack have studied the relation bet between light distribution and tree structure and leaf shape. The researches on leaf classification have already been done by many researchers such as Chia-Ling Lee, Shu-Yuan Chen, B.D Ripley. Although many of the literature we refer to relates to the questions we are dealing with, none of them can generally answer our questions. Further modeling work is needed.

<!-- b000052 | prose | pages [3] -->
However, there are some tradeoffs limiting our modeling. Due to the difficulty in collecting data, our models are not fully tested by actual data, so we cannot ensure the validity when some of them are applied to all kinds of data. Besides, phenomena in biology are hard to analyze since some of them are caused by multiple factors, which affects the comprehensiveness of our models and make it nearly impossible to accurately conclude the answer. To sum up, our approaches are pretty clear: develop models on each of the problems, especially focusing on classification, leaf shape, the estimation of leaf mass and light interception of leaves. After formulating the models, we test our models making the best of the data we collect and analyze the sensitivity of our models.

<!-- b000053 | furniture | pages [3] -->


<!-- b000054 | heading | pages [3] -->
2. Model of Leaf Description

<!-- b000055 | prose | pages [3] -->
and Classification

<!-- b000056 | heading | pages [3] -->
2.1 Introduction

<!-- b000057 | prose | pages [3] -->
In order to describe and classify leaves, we firstly need to understand the causal

<!-- b000058 | furniture | pages [4] -->
#Team 16831

<!-- b000059 | furniture | pages [4] -->
Page 3 of 53

<!-- b000060 | furniture | pages [4] -->


<!-- b000061 | prose | pages [4] -->
factors that lead to the diversity of leaves shapes. We attribute the factors to the following two aspects:

<!-- b000062 | prose | pages [4] -->
 Genetype

<!-- b000063 | prose | pages [4] -->
The gene of a tree determine the shapes of leaves on a tree to a large degree. As we know, the shapes of a tree's leaves are a response to the tree species' long term ecological and evolutionary histories.

<!-- b000064 | prose | pages [4] -->
 Environment

<!-- b000065 | prose | pages [4] -->
An ecosystem's limiting factors may also modify the finished form and shape of a tree's leaves.

<!-- b000066 | prose | pages [4] -->
Considering that the genetype of a tree is also a response to the natural selection determined by the environment, we mainly focus on the impacts of environment.

<!-- b000067 | prose | pages [4] -->
Understanding of the "logic" behind the varied forms of leaves is facilitated by a firm grasp of the precise functions a leaf must accomplish: 1.  A leaf must "capture" sunlight for photosynthesis (in such a process it may also absorb a great deal of heat). 2.  A leaf must take in carbon dioxide from the surrounding air via pores (called "stomatae"). This carbon dioxide is also needed for photosynthesis. When these leaf

<!-- b000068 | prose | pages [4] -->
stomatae are open to allow the uptake of carbon dioxide, water from inside the leaf is lost to the atmosphere. 3.  Transpiration. Leaf transpiration occurs through stomata, and can be thought of as a necessary "cost" associated with the opening of the stomata to allow the diffusion of carbon dioxide gas from the air for photosynthesis. Transpiration also cools plants and enables mass flow of mineral nutrients and water from roots to shoots. The leaf, then, is affected by these balancing acts: enough sunlight and carbon dioxide to run photosynthesis and transpiration. Knowing why leaves have various shapes, our next step is to determine the parameters which might be effected by the two functions listed above of leaves and also they can describe the shapes of leaves. Our goal is to build a mathematical model to describe and classify leaves using the parameters we find.

<!-- b000069 | furniture | pages [4] -->


<!-- b000070 | heading | pages [4] -->
2.2 Leaf Classification Model

<!-- b000071 | heading | pages [4] -->
2.2.1 Leaf Description

<!-- b000072 | prose | pages [4] -->
We focus on four traditional parameters to describe the biodiversity of leaf shape: 1. Leaf index (a ratio of leaf length to leaf width), which describes the narrowness of leaf. 2. Leaf area. Here we use the product of length and width to approximate the area.

<!-- b000073 | furniture | pages [5] -->
#Team 16831

<!-- b000074 | prose | pages [5] -->
3. Non-serrated ratio(NR).

<!-- b000075 | prose | pages [5] -->


<!-- b000076 | prose | pages [5] -->
N

<!-- b000077 | furniture | pages [5] -->
Page 4 of 53

<!-- b000078 | furniture | pages [5] -->


<!-- b000079 | furniture | pages [5] -->


<!-- b000080 | prose | pages [5] -->
D Centroid Cc

<!-- b000081 | prose | pages [5] -->
(

<!-- b000082 | prose | pages [5] -->


<!-- b000083 | prose | pages [5] -->
i

<!-- b000084 | prose | pages [5] -->
1

<!-- b000085 | prose | pages [5] -->
NR

<!-- b000086 | prose | pages [5] -->


<!-- b000087 | prose | pages [5] -->
M

<!-- b000088 | prose | pages [5] -->
, ) /

<!-- b000089 | prose | pages [5] -->
N

<!-- b000090 | prose | pages [5] -->
i

<!-- b000091 | prose | pages [5] -->
eq1

<!-- b000092 | prose | pages [5] -->
D Centroid Cv

<!-- b000093 | prose | pages [5] -->
(

<!-- b000094 | prose | pages [5] -->


<!-- b000095 | prose | pages [5] -->
j

<!-- b000096 | prose | pages [5] -->
1

<!-- b000097 | prose | pages [5] -->
Where

<!-- b000098 | prose | pages [5] -->
, ) /

<!-- b000099 | prose | pages [5] -->
M

<!-- b000100 | prose | pages [5] -->
j

<!-- b000101 | prose | pages [5] -->
D X Y represents the distance between X and Y, ( , )

<!-- b000102 | prose | pages [5] -->
Centroid is the centroid of leaf.

<!-- b000103 | prose | pages [5] -->
Cc is the point on the concave part of the margin.

<!-- b000104 | prose | pages [5] -->
i

<!-- b000105 | prose | pages [5] -->
Cv is the point on the convex part of the margin.

<!-- b000106 | prose | pages [5] -->
j

<!-- b000107 | prose | pages [5] -->
Cc . N  is the total number of i

<!-- b000108 | prose | pages [5] -->
Cv . M  is the total number of j

<!-- b000109 | prose | pages [5] -->
NR can be used to determine the degree of serration of the margin, the smaller NR is, the sharper the serration is. Thus NR=1 means the leaf have smooth margin and NR=0 occures when the leaf is analogical to a maple leaf. 4. Leaf extended angle (LEA). The definitions of NR and LEA are presented visually in the figures below.

<!-- b000110 | furniture | pages [5] -->


<!-- b000111 | furniture | pages [5] -->


<!-- b000112 | caption | pages [5] -->
Figure 1. NR                                Figure 2. LEA

<!-- b000113 | furniture | pages [5] -->


<!-- b000114 | heading | pages [5] -->
2.2.2 The Process of Classification based on cluster analysis

<!-- b000115 | prose | pages [5] -->
We calculate these parameters of 32 leaves from the 55 leave images we find in the literature(Chia-Ling Lee, Shu-Yuan Chen,2006),the detailed data and images can be viewed in the appendix.

<!-- b000116 | prose | pages [5] -->
Next, we classify the 32 leaves using the parameters we have. Since we don’t have any previous knowledge about how many classifications there should be, we do cluster analysis to classify these 32 samples (using R 2.13.1, the codes are presented in the appendix).

<!-- b000117 | prose | pages [5] -->
The result of clustering is displayed in Figure3.

<!-- b000118 | furniture | pages [6] -->
#Team 16831

<!-- b000119 | furniture | pages [6] -->
Page 5 of 53

<!-- b000120 | furniture | pages [6] -->


<!-- b000121 | furniture | pages [6] -->


<!-- b000122 | furniture | pages [6] -->


<!-- b000123 | caption | pages [6] -->
Figure 3. cluster analysis

<!-- b000124 | caption | pages [6] -->
Figure 3 shows that the 32 samples can be classified into 4 clusters. Then we

<!-- b000125 | prose | pages [6] -->
match the cluster result with each of the images of leaves respectively, we obtain the classification below. Type 1

<!-- b000126 | prose | pages [6] -->
Type 2

<!-- b000127 | prose | pages [6] -->
Type 3

<!-- b000128 | prose | pages [6] -->
Type 4

<!-- b000129 | furniture | pages [6] -->


<!-- b000130 | furniture | pages [6] -->


<!-- b000131 | furniture | pages [6] -->


<!-- b000132 | furniture | pages [7] -->
#Team 16831

<!-- b000133 | furniture | pages [7] -->
Page 6 of 53

<!-- b000134 | furniture | pages [7] -->


<!-- b000135 | furniture | pages [7] -->


<!-- b000136 | furniture | pages [7] -->


<!-- b000137 | prose | pages [7] -->
The figure above gives a visual result of classification where the leaves in the same classification are fairly similar with each other.

<!-- b000138 | furniture | pages [7] -->


<!-- b000139 | heading | pages [7] -->
2.3 Model Testing Using Neural Network

<!-- b000140 | prose | pages [7] -->
Given the classification result above, now we are trying to classify the rest of the leaves in the database, that is, to determine which of the 4 types each of the rest belongs to. Such being the case, we choose randomly 8 samples from the rest to determine type of them. Based on neural network, the previous 32 samples are used as training samples and the 8 samples we just choose are used as testing samples. Next we present basic steps of formulating our neural network model.  Step 1. Data Pre-processing.

<!-- b000141 | prose | pages [7] -->
In order to obtain an effective training of neural networks, the numerical data should be scaled. This process is known as normalization. One form of suitable data normalization can be achieved using the following equation,which is known as Linear Transformation equation. The scaled variable should be within the range of 0 to 1.

<!-- b000142 | prose | pages [7] -->
 v '

<!-- b000143 | prose | pages [7] -->
Where：

<!-- b000144 | prose | pages [7] -->
 v v

<!-- b000145 | prose | pages [7] -->
min

<!-- b000146 | furniture | pages [7] -->


<!-- b000147 | prose | pages [7] -->
 v v v max min

<!-- b000148 | prose | pages [7] -->
'v   is the new feature value that has been normalized.

<!-- b000149 | prose | pages [7] -->
v is the minimum feature value in the data sample. min

<!-- b000150 | prose | pages [7] -->
v is the maximum feature value in the data sample. max

<!-- b000151 | prose | pages [7] -->
v    is the old feature value before normalization.  Step2.Building Back-Propagation Neural Network The Back-Propagation Neural Network (BPNN) is based on a supervised learning method, and is a generalization of the delta rule. It requires a teacher that knows, or can calculate, the desired output for any input in the training set. The BPNN architecture used as the classifier for this research (Figure 4) consists of four layers which are: Input Layer -- There are 4 neurons in the input layer for each predictor variable. Each of the neurons represents a parameter (either leaf index, leaf area, NR or LEA) that describes the leaf shape.

<!-- b000152 | furniture | pages [8] -->
#Team 16831

<!-- b000153 | furniture | pages [8] -->
Page 7 of 53

<!-- b000154 | furniture | pages [8] -->


<!-- b000155 | prose | pages [8] -->
Hidden Layer -- This layer has one neuron for each case in the training dataset. The neuron stores the values of the predictor variables for the case along with the target value. In this case, there are 10 neurons in this layer. Decision Layer -- This layer divides the value accumulated in the numerator summation unit by the value in the denominator summation unit and uses the result as the predicted target value.

<!-- b000156 | furniture | pages [8] -->


<!-- b000157 | caption | pages [8] -->
Figure 4. neural network

<!-- b000158 | prose | pages [8] -->
To sum up, the process of classifying new leaves using BP Neural Network can be illustrated by a simple flow chart presented below.

<!-- b000159 | furniture | pages [8] -->


<!-- b000160 | caption | pages [8] -->
Figure 5. classifying process

<!-- b000161 | furniture | pages [8] -->


<!-- b000162 | prose | pages [8] -->
In the BPNN model, some of the detailed parameters are listed below: net.trainParam.epochs=1000; net.trainParam.show=10; net.trainParam.lr=0.06; net.trainParam.goal=0.01; net.trainParam.min_grad = 1e-20;

<!-- b000163 | furniture | pages [8] -->


<!-- b000164 | prose | pages [8] -->
Before displaying our classification results, we present an extra figure output from MaLab, which shows how the final result is approached. Figure 6 and Figure 7 are final results output from MatLab.

<!-- b000165 | furniture | pages [9] -->
#Team 16831

<!-- b000166 | furniture | pages [9] -->


<!-- b000167 | furniture | pages [9] -->
Page 8 of 53

<!-- b000168 | furniture | pages [9] -->


<!-- b000169 | furniture | pages [9] -->


<!-- b000170 | furniture | pages [9] -->


<!-- b000171 | caption | pages [9] -->
Figure 6                             Figure 7

<!-- b000172 | furniture | pages [9] -->


<!-- b000173 | prose | pages [9] -->
To demonstrate the results with the images of leaves, we present the classification in the form below (NOTE that the images in rectangular frame represent the new leaves that are classified by BP Neural Network and add up to 8 in total): Type 1

<!-- b000174 | prose | pages [9] -->
Type 2

<!-- b000175 | prose | pages [9] -->
Type3

<!-- b000176 | furniture | pages [9] -->


<!-- b000177 | furniture | pages [9] -->


<!-- b000178 | furniture | pages [10] -->
#Team 16831

<!-- b000179 | prose | pages [10] -->
Type 4

<!-- b000180 | furniture | pages [10] -->
Page 9 of 53

<!-- b000181 | furniture | pages [10] -->


<!-- b000182 | furniture | pages [10] -->


<!-- b000183 | furniture | pages [10] -->


<!-- b000184 | furniture | pages [10] -->


<!-- b000185 | caption | pages [10] -->
Figure 9. classifying result

<!-- b000186 | furniture | pages [10] -->


<!-- b000187 | furniture | pages [10] -->


<!-- b000188 | prose | pages [10] -->
As is shown in the results, except for the leaf in Type 3, rest of the leaves are correctly classified into the category of which the leaves are most analogical to it. Apparently, the testing results verify the validity of our model.

<!-- b000189 | furniture | pages [10] -->


<!-- b000190 | furniture | pages [10] -->


<!-- b000191 | heading | pages [10] -->
3. Model

<!-- b000192 | prose | pages [10] -->
of the Relation Leaf between Overlapping

<!-- b000193 | heading | pages [10] -->
Introduction

<!-- b000194 | prose | pages [10] -->
Shape and

<!-- b000195 | prose | pages [10] -->
In this section, we mainly discuss the factors closely related to the overlapping area of a single branch. These factors include:

<!-- b000196 | prose | pages [10] -->
solar altitude angle (SA-Angle) sunlight direction angle (SD-Angle) on horizontal plane narrowness of the leaf (Leaf index) petiole length (scaled to leaf area) leaf inclination angle (LI-Angle) internode length (scaled to leaf area). As we know, the leaf phyllotaxis (leaf pattern) describes the way how leaves are

<!-- b000197 | furniture | pages [11] -->
#Team 16831

<!-- b000198 | furniture | pages [11] -->
Page 10 of 53

<!-- b000199 | furniture | pages [11] -->


<!-- b000200 | prose | pages [11] -->
distributed along the shoot, and it has a great impact on the effectiveness of light capture efficiency of a shoot. Three representative phyllotaxes are shown below:

<!-- b000201 | furniture | pages [11] -->


<!-- b000202 | caption | pages [11] -->
Figure 10.  distichous, decussate, spiral pattern

<!-- b000203 | prose | pages [11] -->
Source:  http://en.wikipedia.org/wiki/Phyllotaxy In our leaf overlapping model, we focused on a common scenario: distichous.

<!-- b000204 | furniture | pages [11] -->


<!-- b000205 | heading | pages [11] -->
Assumptions

<!-- b000206 | prose | pages [11] -->
We simplified this pattern with some assumptions:

<!-- b000207 | prose | pages [11] -->
 Each blade has unit area, and all blades are identical.  Since most leaves are roughly symmetric, we regard the blade shape as rhombus with 2 diagonal lines, which refer to the width and length respectively. The main purpose of this approximation is to simplify the computation and consider the key factor, narrowness, the most significant coefficient of the blade shape when we discuss the leaf overlapping.  The shoot radius is relatively small to blade, so is the radius of petiole, so we can neglect the shade of them both.  The curl and thickness of the leaf are neglected, which means we can view the blade as a thin palate.  The sunlight is the main light source, so we view the light is parallel.  We assume vertical shoot in the model. The change of light direction can be used to discuss the scenarios when shoot is not vertical.

<!-- b000208 | furniture | pages [11] -->


<!-- b000209 | prose | pages [11] -->
Variable descriptions

<!-- b000210 | prose | pages [11] -->
Based on these assumptions, we build a 3D model of leaf overlapping as the figure given below.

<!-- b000211 | furniture | pages [12] -->
#Team 16831

<!-- b000212 | furniture | pages [12] -->
Page 11 of 53

<!-- b000213 | furniture | pages [12] -->


<!-- b000214 | furniture | pages [12] -->


<!-- b000215 | furniture | pages [12] -->


<!-- b000216 | caption | pages [12] -->
Figure 11. A 3D model

<!-- b000217 | prose | pages [12] -->
*Note: the figure only shows a model with no petiole, a particular condition Now we give detailed definitions about the variables to build a 3D model to analyze the factors mentioned above.

<!-- b000218 | furniture | pages [12] -->


<!-- b000219 | furniture | pages [12] -->


<!-- b000220 | caption | pages [12] -->
Figure 12. schematic figure

<!-- b000221 | furniture | pages [12] -->


<!-- b000222 | prose | pages [12] -->
The variables we define are as follow:

<!-- b000223 | caption | pages [12] -->
Table 1. variable definitions

<!-- b000224 | prose | pages [12] -->
Corresponding note Variable name SA-Angle 

<!-- b000225 | prose | pages [12] -->
 SD-Angle Value rage Physical Meaning 0°to  90° The altitude of sunlight 0°to  360° The direction of

<!-- b000226 | furniture | pages [13] -->
#Team 16831

<!-- b000227 | prose | pages [13] -->
Leaf-Index Height/Width

<!-- b000228 | prose | pages [13] -->
p-length Petiole/Leaf area

<!-- b000229 | prose | pages [13] -->
 LI-Angle

<!-- b000230 | prose | pages [13] -->
 H Inter-length /Leaf area

<!-- b000231 | furniture | pages [13] -->


<!-- b000232 | furniture | pages [13] -->
Page 12 of 53

<!-- b000233 | furniture | pages [13] -->


<!-- b000234 | furniture | pages [13] -->


<!-- b000235 | prose | pages [13] -->
sunlight Leaf-Index>0 Leaf narrowness

<!-- b000236 | prose | pages [13] -->
p-length>=0

<!-- b000237 | furniture | pages [13] -->


<!-- b000238 | prose | pages [13] -->
0°to  90° leaf inclination

<!-- b000239 | prose | pages [13] -->
Inter-length >0 Vertical distance

<!-- b000240 | prose | pages [13] -->
between two neighboring layers

<!-- b000241 | prose | pages [13] -->
*Note: With the definition of Leaf-Index and Inter-length, we can analyze leaf with different size conveniently.

<!-- b000242 | heading | pages [13] -->
3.1 Building the Model

<!-- b000243 | prose | pages [13] -->
We mainly discuss the shoot with two layers of leaves following, because of the most significant impact is given by the neighboring layer above. That means we only need to consider 4 blade, 2 on upper layer, and 2 on down layer. To give the criteria of overlapping, effective area ratio (EAR) is defined by the formula below.

<!-- b000244 | prose | pages [13] -->
EAR S  

<!-- b000245 | prose | pages [13] -->
U

<!-- b000246 | furniture | pages [13] -->


<!-- b000247 | prose | pages [13] -->
S

<!-- b000248 | prose | pages [13] -->
total

<!-- b000249 | prose | pages [13] -->
S is the total leaf area that is not shaded, namely the effective area, Where U

<!-- b000250 | prose | pages [13] -->
S and is the total leaf area. total

<!-- b000251 | prose | pages [13] -->
Under this definition, our solution should be able to calculate the shaded area

<!-- b000252 | furniture | pages [13] -->


<!-- b000253 | prose | pages [13] -->
of the two leaves in down layer. That means, we should get the relation between the shade profile in upper layer and the profile of two leaves in down layer.

<!-- b000254 | furniture | pages [13] -->


<!-- b000255 | prose | pages [13] -->
We focus on two types of blades:

<!-- b000256 | prose | pages [13] -->
 Horizontal Blade: leaves are perpendicular to branches

<!-- b000257 | prose | pages [13] -->
 Inclined blade: leaves are inclined to branches

<!-- b000258 | prose | pages [13] -->
They are showed below:

<!-- b000259 | furniture | pages [14] -->
#Team 16831

<!-- b000260 | furniture | pages [14] -->
Page 13 of 53

<!-- b000261 | furniture | pages [14] -->


<!-- b000262 | furniture | pages [14] -->


<!-- b000263 | prose | pages [14] -->
Horizontal Blade                        Inclined blade

<!-- b000264 | caption | pages [14] -->
Figure 13. schematic figure

<!-- b000265 | furniture | pages [14] -->


<!-- b000266 | prose | pages [14] -->
In each scenario, we analyze two cases:

<!-- b000267 | prose | pages [14] -->
 The leave have no petiole;  The leave have petiole;

<!-- b000268 | furniture | pages [14] -->


<!-- b000269 | heading | pages [14] -->
3.1.1 Case 1: Horizontal Blade

<!-- b000270 | prose | pages [14] -->
(1) Without petiole

<!-- b000271 | prose | pages [14] -->
To build this model, we firstly consider a certain scenario, where the LI-Angle is zero, and the SA-Angle is 90 degree. In this case the blade plane is horizontal, and the sunlight is vertical. Obviously, the leaves on down layers are totally shaded, EAR=0.5.

<!-- b000272 | prose | pages [14] -->
We assume LI-Angle and p-length are zero now, and we will discuss their influence in later part. If we assume SA-Angle is 45 degree, the SD-Angle is 0, Leaf-Index is 1 (square shape), Inter-length is 0.4, the figures below will show what will happen.

<!-- b000273 | furniture | pages [14] -->


<!-- b000274 | furniture | pages [14] -->


<!-- b000275 | furniture | pages [14] -->


<!-- b000276 | furniture | pages [14] -->


<!-- b000277 | furniture | pages [15] -->
#Team 16831

<!-- b000278 | furniture | pages [15] -->
Page 14 of 53

<!-- b000279 | furniture | pages [15] -->


<!-- b000280 | furniture | pages [15] -->


<!-- b000281 | furniture | pages [15] -->


<!-- b000282 | caption | pages [15] -->
Figure 14. A schematic figure

<!-- b000283 | prose | pages [15] -->
*Note: OL refers to overlapping area. The upper layer curve is the profile of shade on down layer plane here. Down layer curve is the leaf profile. 3 OL part is she shaded area on down layer leaves.

<!-- b000284 | prose | pages [15] -->
Apparently, the upper layer curve is a congruent of the down layer curve with a certain displacement. This enables us to find a method to calculate the OL area. We need to calculate the displacement vector at first.

<!-- b000285 | prose | pages [15] -->
In 3D Cartesian coordinate system, the projection point (X’,Y’,Z’) by the sunlight of one

<!-- b000286 | prose | pages [15] -->
certain point(X,Y,Z) on horizontal plane can be calculated as following.

<!-- b000287 | prose | pages [15] -->
     

<!-- b000288 | prose | pages [15] -->
SDAngle X

<!-- b000289 | prose | pages [15] -->
' 1 0 sin(

<!-- b000290 | prose | pages [15] -->
    

<!-- b000291 | prose | pages [15] -->
)tan(

<!-- b000292 | prose | pages [15] -->
SAAngle

<!-- b000293 | prose | pages [15] -->
)

<!-- b000294 | prose | pages [15] -->
X

<!-- b000295 | prose | pages [15] -->
 

<!-- b000296 | prose | pages [15] -->
SDAngle Y

<!-- b000297 | prose | pages [15] -->
' 0 1 cos(

<!-- b000298 | prose | pages [15] -->
     

<!-- b000299 | prose | pages [15] -->
Z

<!-- b000300 | prose | pages [15] -->
' 0 0

<!-- b000301 | prose | pages [15] -->
  

<!-- b000302 | prose | pages [15] -->
)tan(

<!-- b000303 | prose | pages [15] -->
SAAngle

<!-- b000304 | prose | pages [15] -->
)

<!-- b000305 | prose | pages [15] -->
Y

<!-- b000306 | furniture | pages [15] -->


<!-- b000307 | prose | pages [15] -->
   

<!-- b000308 | prose | pages [15] -->
0

<!-- b000309 | prose | pages [15] -->
Z

<!-- b000310 | prose | pages [15] -->
 

<!-- b000311 | prose | pages [15] -->
The proof of this formula is easy with basic geometrical theory. So we omit this part in our article.

<!-- b000312 | prose | pages [15] -->
We denote the 3X3 matrix as TFM (transform matrix). Tangent (SAAngle) here is 1 (SAAngle =45 degree), as a result, the trace of projection displacement vector can be described as：

<!-- b000313 | prose | pages [15] -->
 SDAngle X sin(

<!-- b000314 | prose | pages [15] -->


<!-- b000315 | prose | pages [15] -->
)Interlength

<!-- b000316 | furniture | pages [15] -->


<!-- b000317 | prose | pages [15] -->
SDAngle Y cos( )Interlength

<!-- b000318 | furniture | pages [15] -->


<!-- b000319 | prose | pages [15] -->
The formula shows a circle trace of the vector endpoint.

<!-- b000320 | furniture | pages [16] -->
#Team 16831

<!-- b000321 | furniture | pages [16] -->
Page 15 of 53

<!-- b000322 | furniture | pages [16] -->


<!-- b000323 | furniture | pages [16] -->


<!-- b000324 | furniture | pages [16] -->


<!-- b000325 | caption | pages [16] -->
Figure 15. a schematic figure

<!-- b000326 | caption | pages [16] -->
Figure 15 shows displacement with SDAngle=45,90,135 degree.

<!-- b000327 | prose | pages [16] -->
Noticing this phenomenon, we can calculate the OL area as following.

<!-- b000328 | furniture | pages [16] -->


<!-- b000329 | caption | pages [16] -->
Figure 16. a magnification

<!-- b000330 | furniture | pages [16] -->


<!-- b000331 | prose | pages [16] -->
We magnify the second figure to show how to caculate the OL area sidelength.

<!-- b000332 | prose | pages [16] -->
 CAB In triangle ABC, AB=displacment vector length , can be caculated with  ACB SDAngle and a certain apex angle of rhombus (determined by Leaf-Index) ,

<!-- b000333 | furniture | pages [16] -->


<!-- b000334 | prose | pages [16] -->
eqauls to (180 angle).So BC is detemined in this triangle. Thus sidelength is

<!-- b000335 | prose | pages [16] -->
determined.

<!-- b000336 | prose | pages [16] -->
Omitting other geometrical caculation steps, we give the final expression of OL

<!-- b000337 | prose | pages [16] -->
areas in common condition. The result depends on .

<!-- b000338 | prose | pages [16] -->
    0 (1) for : 0

<!-- b000339 | prose | pages [16] -->


<!-- b000340 | prose | pages [16] -->


<!-- b000341 | prose | pages [16] -->


<!-- b000342 | prose | pages [16] -->


<!-- b000343 | prose | pages [16] -->
2

<!-- b000344 | prose | pages [16] -->
sin( )

<!-- b000345 | prose | pages [16] -->
m

<!-- b000346 | prose | pages [16] -->
1

<!-- b000347 | prose | pages [16] -->


<!-- b000348 | prose | pages [16] -->


<!-- b000349 | prose | pages [16] -->
 

<!-- b000350 | prose | pages [16] -->
0

<!-- b000351 | prose | pages [16] -->
S

<!-- b000352 | prose | pages [16] -->
2sin(2 ) (

<!-- b000353 | prose | pages [16] -->
OL

<!-- b000354 | prose | pages [16] -->
0

<!-- b000355 | prose | pages [16] -->


<!-- b000356 | prose | pages [16] -->
2

<!-- b000357 | prose | pages [16] -->
m

<!-- b000358 | prose | pages [16] -->
sin(2 )

<!-- b000359 | prose | pages [16] -->
0

<!-- b000360 | prose | pages [16] -->


<!-- b000361 | prose | pages [16] -->


<!-- b000362 | prose | pages [16] -->
 

<!-- b000363 | prose | pages [16] -->


<!-- b000364 | prose | pages [16] -->


<!-- b000365 | prose | pages [16] -->
sin( )sin( ) (

<!-- b000366 | prose | pages [16] -->
 

<!-- b000367 | prose | pages [16] -->
2 0 0

<!-- b000368 | prose | pages [16] -->
h

<!-- b000369 | prose | pages [16] -->
tan )

<!-- b000370 | prose | pages [16] -->


<!-- b000371 | prose | pages [16] -->
sin(2 )

<!-- b000372 | prose | pages [16] -->
0

<!-- b000373 | prose | pages [16] -->


<!-- b000374 | prose | pages [16] -->


<!-- b000375 | prose | pages [16] -->


<!-- b000376 | prose | pages [16] -->


<!-- b000377 | prose | pages [16] -->
2

<!-- b000378 | prose | pages [16] -->
sin( )

<!-- b000379 | prose | pages [16] -->
m

<!-- b000380 | prose | pages [16] -->
1

<!-- b000381 | prose | pages [16] -->
    

<!-- b000382 | prose | pages [16] -->
0

<!-- b000383 | prose | pages [16] -->
h

<!-- b000384 | prose | pages [16] -->
tan )(

<!-- b000385 | prose | pages [16] -->
h

<!-- b000386 | prose | pages [16] -->
tan )

<!-- b000387 | prose | pages [16] -->


<!-- b000388 | prose | pages [16] -->
2

<!-- b000389 | prose | pages [16] -->
m

<!-- b000390 | prose | pages [16] -->
sin(2 )

<!-- b000391 | prose | pages [16] -->
0

<!-- b000392 | furniture | pages [17] -->
#Team 16831

<!-- b000393 | furniture | pages [17] -->


<!-- b000394 | prose | pages [17] -->
(2) for       180

<!-- b000395 | furniture | pages [17] -->


<!-- b000396 | prose | pages [17] -->
0 0

<!-- b000397 | prose | pages [17] -->
   

<!-- b000398 | prose | pages [17] -->
2

<!-- b000399 | prose | pages [17] -->
sin( )

<!-- b000400 | prose | pages [17] -->
m

<!-- b000401 | prose | pages [17] -->
1

<!-- b000402 | prose | pages [17] -->
   

<!-- b000403 | prose | pages [17] -->
0

<!-- b000404 | prose | pages [17] -->
S

<!-- b000405 | prose | pages [17] -->
2sin(2 ) ( OL

<!-- b000406 | prose | pages [17] -->
0

<!-- b000407 | prose | pages [17] -->


<!-- b000408 | prose | pages [17] -->
2

<!-- b000409 | prose | pages [17] -->
m

<!-- b000410 | prose | pages [17] -->
sin(2 )

<!-- b000411 | prose | pages [17] -->
0

<!-- b000412 | prose | pages [17] -->
     (3) for 180 180

<!-- b000413 | furniture | pages [17] -->


<!-- b000414 | prose | pages [17] -->
0

<!-- b000415 | prose | pages [17] -->


<!-- b000416 | prose | pages [17] -->


<!-- b000417 | prose | pages [17] -->


<!-- b000418 | prose | pages [17] -->
 

<!-- b000419 | prose | pages [17] -->
2

<!-- b000420 | prose | pages [17] -->
sin( 180 )

<!-- b000421 | prose | pages [17] -->
m

<!-- b000422 | prose | pages [17] -->
1

<!-- b000423 | prose | pages [17] -->


<!-- b000424 | prose | pages [17] -->


<!-- b000425 | prose | pages [17] -->
 

<!-- b000426 | prose | pages [17] -->
0

<!-- b000427 | prose | pages [17] -->
S

<!-- b000428 | prose | pages [17] -->
2sin(2 ) (

<!-- b000429 | prose | pages [17] -->
OL

<!-- b000430 | prose | pages [17] -->
0

<!-- b000431 | prose | pages [17] -->


<!-- b000432 | prose | pages [17] -->
2

<!-- b000433 | prose | pages [17] -->
m

<!-- b000434 | prose | pages [17] -->
sin(2 )

<!-- b000435 | prose | pages [17] -->
0

<!-- b000436 | prose | pages [17] -->


<!-- b000437 | prose | pages [17] -->


<!-- b000438 | prose | pages [17] -->


<!-- b000439 | prose | pages [17] -->


<!-- b000440 | prose | pages [17] -->


<!-- b000441 | prose | pages [17] -->


<!-- b000442 | prose | pages [17] -->


<!-- b000443 | prose | pages [17] -->


<!-- b000444 | prose | pages [17] -->
sin( 180 )sin( 180 ) (

<!-- b000445 | prose | pages [17] -->
 

<!-- b000446 | prose | pages [17] -->
0 0

<!-- b000447 | furniture | pages [17] -->
Page 16 of 53

<!-- b000448 | furniture | pages [17] -->


<!-- b000449 | furniture | pages [17] -->


<!-- b000450 | prose | pages [17] -->
   

<!-- b000451 | prose | pages [17] -->
2

<!-- b000452 | prose | pages [17] -->
sin( )

<!-- b000453 | prose | pages [17] -->
m

<!-- b000454 | prose | pages [17] -->
1

<!-- b000455 | prose | pages [17] -->
    

<!-- b000456 | prose | pages [17] -->
0

<!-- b000457 | prose | pages [17] -->
h

<!-- b000458 | prose | pages [17] -->
tan )(

<!-- b000459 | prose | pages [17] -->
h

<!-- b000460 | prose | pages [17] -->
tan )

<!-- b000461 | prose | pages [17] -->


<!-- b000462 | prose | pages [17] -->
2

<!-- b000463 | prose | pages [17] -->
m

<!-- b000464 | prose | pages [17] -->
sin(2 )

<!-- b000465 | prose | pages [17] -->
0

<!-- b000466 | furniture | pages [17] -->


<!-- b000467 | furniture | pages [17] -->


<!-- b000468 | prose | pages [17] -->


<!-- b000469 | prose | pages [17] -->


<!-- b000470 | prose | pages [17] -->


<!-- b000471 | prose | pages [17] -->
 

<!-- b000472 | prose | pages [17] -->
2

<!-- b000473 | prose | pages [17] -->
sin( 180 )

<!-- b000474 | prose | pages [17] -->
m

<!-- b000475 | prose | pages [17] -->
1

<!-- b000476 | prose | pages [17] -->
    

<!-- b000477 | prose | pages [17] -->
0

<!-- b000478 | prose | pages [17] -->
h

<!-- b000479 | prose | pages [17] -->
tan )(

<!-- b000480 | prose | pages [17] -->
h

<!-- b000481 | prose | pages [17] -->
tan )

<!-- b000482 | prose | pages [17] -->


<!-- b000483 | prose | pages [17] -->
2

<!-- b000484 | prose | pages [17] -->
m

<!-- b000485 | prose | pages [17] -->
sin(2 )

<!-- b000486 | prose | pages [17] -->
0

<!-- b000487 | prose | pages [17] -->
 

<!-- b000488 | prose | pages [17] -->
2

<!-- b000489 | prose | pages [17] -->
tan )

<!-- b000490 | prose | pages [17] -->
h

<!-- b000491 | prose | pages [17] -->


<!-- b000492 | prose | pages [17] -->
sin(2 )

<!-- b000493 | prose | pages [17] -->
0

<!-- b000494 | prose | pages [17] -->
Where m=LeafIndex

<!-- b000495 | prose | pages [17] -->
 =90 SAAngle

<!-- b000496 | furniture | pages [17] -->


<!-- b000497 | prose | pages [17] -->
= Interlength h

<!-- b000498 | furniture | pages [17] -->


<!-- b000499 | furniture | pages [17] -->


<!-- b000500 | prose | pages [17] -->
=acrtan (1/m) is the critical angle when OL3 part is diminished. 0

<!-- b000501 | furniture | pages [17] -->


<!-- b000502 | heading | pages [17] -->
Results and analysis:

<!-- b000503 | prose | pages [17] -->
S (unshaded area) —SAAngle curves with different Leaf-Index in We plot U

<!-- b000504 | prose | pages [17] -->
Matlab as following.

<!-- b000505 | furniture | pages [18] -->
#Team 16831

<!-- b000506 | furniture | pages [18] -->
Page 17 of 53

<!-- b000507 | furniture | pages [18] -->


<!-- b000508 | furniture | pages [18] -->


<!-- b000509 | prose | pages [18] -->
S (unshaded area)—SAAngle curves

<!-- b000510 | caption | pages [18] -->
Figure 17.

<!-- b000511 | prose | pages [18] -->
U

<!-- b000512 | prose | pages [18] -->
S value and some S , mean U U The max

<!-- b000513 | prose | pages [18] -->
are provided in the diagram below.

<!-- b000514 | prose | pages [18] -->
S values with particular SD-Angle U

<!-- b000515 | caption | pages [18] -->
Table 2. Result

<!-- b000516 | prose | pages [18] -->
Leaf Max value

<!-- b000517 | heading | pages [18] -->
45 degree

<!-- b000518 | prose | pages [18] -->
1:1 2.9714 2.8000

<!-- b000519 | prose | pages [18] -->
2:1 3.2800 3.0114

<!-- b000520 | prose | pages [18] -->
8:1 3.9200 3.6327

<!-- b000521 | furniture | pages [18] -->


<!-- b000522 | heading | pages [18] -->
0 degree

<!-- b000523 | prose | pages [18] -->
Mean value

<!-- b000524 | prose | pages [18] -->
2.8914 2.8913

<!-- b000525 | prose | pages [18] -->
2.6800 2.9799

<!-- b000526 | prose | pages [18] -->
2.3700 3.4198

<!-- b000527 | prose | pages [18] -->
The mean value ratio of case 1:1 to case 8:1 is 0.845. The maximal ratio of case 1:1 to case 8:1 is 0.758.

<!-- b000528 | furniture | pages [18] -->


<!-- b000529 | heading | pages [18] -->
conclusions

<!-- b000530 | prose | pages [18] -->
From the figure and result above we can conclude:

<!-- b000531 | prose | pages [18] -->
S varies with Sunlight direction, and the maximum points lie when SAAngle is  U

<!-- b000532 | prose | pages [18] -->
0 or 90 degree.

<!-- b000533 | prose | pages [18] -->
S varies with different narrowness ratio significantly.  The maximum of U

<!-- b000534 | prose | pages [18] -->
Narrow leaves get a higher effective area both in maximum value and mean value than broader leaves.

<!-- b000535 | furniture | pages [18] -->


<!-- b000536 | prose | pages [18] -->
(2) With petiole

<!-- b000537 | prose | pages [18] -->
The similar model is used to discuss the petiole length impact on effective area, with a slightly modification. S3 area in figure is largely determined by petiole length.

<!-- b000538 | prose | pages [18] -->
With a longer petiole length, the leaves can be more dispersive, thus a smaller shade will be projected on down layers. If we regard branch with leaves as a cylinder, then a longer petiole length means a lager radius of Cross-sectional circle.

<!-- b000539 | heading | pages [18] -->
Result and analysis

<!-- b000540 | prose | pages [18] -->
S We modified the expression (given in appendix) of OL areas, then plot a U

<!-- b000541 | prose | pages [18] -->
(unshaded area) —SAAngle curves with plength=0.2 as follow:

<!-- b000542 | furniture | pages [19] -->
#Team 16831

<!-- b000543 | furniture | pages [19] -->
Page 18 of 53

<!-- b000544 | furniture | pages [19] -->


<!-- b000545 | furniture | pages [19] -->


<!-- b000546 | prose | pages [19] -->
S (unshaded area)—SAAngle curves

<!-- b000547 | caption | pages [19] -->
Figure 17.

<!-- b000548 | prose | pages [19] -->
U

<!-- b000549 | prose | pages [19] -->
S , mean S and some The max U U

<!-- b000550 | prose | pages [19] -->
provided in the diagram below.

<!-- b000551 | prose | pages [19] -->
S values with particular SD-Angle are U

<!-- b000552 | caption | pages [19] -->
Table 3. Result

<!-- b000553 | prose | pages [19] -->
Leaf Max value

<!-- b000554 | heading | pages [19] -->
45 degree

<!-- b000555 | prose | pages [19] -->
1:1 2.9714 2.8000

<!-- b000556 | prose | pages [19] -->
2:1 3.2800 3.0114

<!-- b000557 | prose | pages [19] -->
8:1 3.9200 3.6327

<!-- b000558 | heading | pages [19] -->
Conclusions:

<!-- b000559 | heading | pages [19] -->
0 degree

<!-- b000560 | prose | pages [19] -->
Mean value

<!-- b000561 | prose | pages [19] -->
2.9714 2.9169

<!-- b000562 | prose | pages [19] -->
2.7200 2.9877

<!-- b000563 | prose | pages [19] -->
2.3800 3.4204

<!-- b000564 | prose | pages [19] -->
We can get several conclusions from the result above when compared with no petiole case.

<!-- b000565 | prose | pages [19] -->
 The broaden leaves are more sensitive to the petiole length, showing a higher

<!-- b000566 | prose | pages [19] -->
S in intervals around 0 and 180 degree, while the narrow leaves roughly U

<!-- b000567 | prose | pages [19] -->
remain unchanged with petiole length.

<!-- b000568 | prose | pages [19] -->
S value of broaden leaves increase faster than narrow leaves.  The mean U

<!-- b000569 | prose | pages [19] -->
Although the change is only 1 percent, the increasing speed will be much higher if we consider multi-layer leaves.

<!-- b000570 | furniture | pages [19] -->


<!-- b000571 | heading | pages [19] -->
3.1.2 Case 2: Inclined Leaf Blade

<!-- b000572 | prose | pages [19] -->
The basic model is given in part1, due to a lack of professional 3D simulation

<!-- b000573 | furniture | pages [20] -->
#Team 16831

<!-- b000574 | furniture | pages [20] -->
Page 19 of 53

<!-- b000575 | furniture | pages [20] -->


<!-- b000576 | furniture | pages [20] -->


<!-- b000577 | prose | pages [20] -->
environment, it’s not practical to get the unshaded area directly. We mainly focused on getting the shade profiles of both layers, and approximate the areas from the shade profiles, using this ‘shade overlapping area ratio’ to approximately present the effective area on blades.

<!-- b000578 | prose | pages [20] -->
We firstly get all apexes coordinate from our 3D model, using coefficient of LI-Angle, Leaf-Index, SD-Angle, Inter-length to express the apex position. Using transform matrix we defined above, finally get the shade profile of two layers on horizontal plane.

<!-- b000579 | prose | pages [20] -->
We compared Leaf-Index of 8:1(Left row) with 1:1(Right row). (1)  SDAngle is 0:

<!-- b000580 | furniture | pages [20] -->


<!-- b000581 | caption | pages [20] -->
Figure 18. SDAngle is 0

<!-- b000582 | prose | pages [20] -->
(2) SDAngle is 45 degree:

<!-- b000583 | furniture | pages [20] -->


<!-- b000584 | caption | pages [20] -->
Figure 18. SDAngle is 45 degree

<!-- b000585 | furniture | pages [20] -->


<!-- b000586 | prose | pages [20] -->
(3)  SDAngle is 90 degree:

<!-- b000587 | furniture | pages [20] -->


<!-- b000588 | furniture | pages [21] -->
#Team 16831

<!-- b000589 | furniture | pages [21] -->
Page 20 of 53

<!-- b000590 | furniture | pages [21] -->


<!-- b000591 | furniture | pages [21] -->


<!-- b000592 | caption | pages [21] -->
Figure 19. SDAngle is 90 degree

<!-- b000593 | furniture | pages [21] -->


<!-- b000594 | heading | pages [21] -->
Result and analysis:

<!-- b000595 | prose | pages [21] -->
S in each case: The diagram below shows the U

<!-- b000596 | caption | pages [21] -->
Table 4. Result

<!-- b000597 | prose | pages [21] -->
SD-Angle in degree 0 Leaf-Index=1 2.379 Leaf-Index=8 2.294

<!-- b000598 | furniture | pages [21] -->


<!-- b000599 | prose | pages [21] -->
45 90 2.871 2.894 3.512 3.793

<!-- b000600 | prose | pages [21] -->
Compare with the Table 2, we find that a 30 degree inclination angle will lead to

<!-- b000601 | prose | pages [21] -->
S in two cases where Leaf-Index=1 and a 2.6% and 3.2% decline of the max U

<!-- b000602 | prose | pages [21] -->
Leaf-Index=8. We use the summation of 3 results in each case above to estimate the mean value ratio. Based on the tendency of the curves we plot, we generally assume the max value is reached when SD-Angle is 90 degree.

<!-- b000603 | prose | pages [21] -->
The approximate mean value ratio of case 1:1 to case 8:1 is 0.848. The max value ratio of case 1:1 to case 8:1 is 0.764.

<!-- b000604 | heading | pages [21] -->
Conclusions:

<!-- b000605 | prose | pages [21] -->
S with 2.6% and 3.2%  The 30 degree inclined leaf blade will get a smaller U

<!-- b000606 | prose | pages [21] -->
decline in two cases, which means inclined leaves has a less effective area ratio.  The mean value ratio of case 1:1 to case 8:1 and the max value ratio of case 1:1

<!-- b000607 | prose | pages [21] -->
to case 8:1 are roughly stay the same despite the 30 degree inclination angle.

<!-- b000608 | furniture | pages [21] -->


<!-- b000609 | prose | pages [21] -->
That shows the narrow leaves are still more effective than the broaden leaves, the ratio of the two scenarios is not changed. They all declined with the inclination angle.

<!-- b000610 | furniture | pages [21] -->


<!-- b000611 | heading | pages [21] -->
3.2 Further Discussion

<!-- b000612 | prose | pages [21] -->
Based on the overlapping analysis model we built before, we show a certain

<!-- b000613 | prose | pages [21] -->
case of muti-layers leaf. We can see the total effective areas can be approximate by considering only one coefficient, the radius of the cylinder, if we only wish to make a rough estimation.

<!-- b000614 | furniture | pages [22] -->
#Team 16831

<!-- b000615 | furniture | pages [22] -->
Page 21 of 53

<!-- b000616 | furniture | pages [22] -->


<!-- b000617 | furniture | pages [22] -->


<!-- b000618 | caption | pages [22] -->
Figure 19. a common case

<!-- b000619 | prose | pages [22] -->
The figure shows the projection of effective blade area can be estimate by using rectangular d x h, which can be calculated by the equivalent cylinder. Therefore, the petiole length, narrowness are positive factors to the effective radius of the equivalent cylinder.

<!-- b000620 | furniture | pages [22] -->


<!-- b000621 | heading | pages [22] -->
3.3 Overall Conclusion

<!-- b000622 | prose | pages [22] -->
The shape of leaves is closely related to the overlapping shadow. Narrow leaf is more effective in maximizing the exposure to sunlight, and it always works whether with or without petiole, blade inclination.

<!-- b000623 | furniture | pages [22] -->


<!-- b000624 | prose | pages [22] -->
The broaden leaves tend to maximizing their light capture by extending their petiole.

<!-- b000625 | furniture | pages [22] -->


<!-- b000626 | prose | pages [22] -->
However, it is still not easy to answer the question, “Do the shapes ‘minimize’ overlapping individual shadows that are cast, so as to maximize exposure?” Because the complication in ecosystem is far more than you can imagine, the leaf shape is determined by a great deal of factors, and the key factor is always different in different places.

<!-- b000627 | furniture | pages [22] -->


<!-- b000628 | prose | pages [22] -->
So we give our final answer to the question as:  In areas where sunlight is the most important factor for trees to live, especially

<!-- b000629 | prose | pages [22] -->
when sunlight is insufficient, they tend to minimize their overlapping shadow by generating a narrow leaf blade or a long petiole.  In areas where other factors (e.g. water) are more important than sunlight, they

<!-- b000630 | prose | pages [22] -->
may not shape their leaves to minimize overlapping shadows.

<!-- b000631 | furniture | pages [22] -->


<!-- b000632 | furniture | pages [22] -->


<!-- b000633 | furniture | pages [23] -->
#Team 16831

<!-- b000634 | heading | pages [23] -->
3.4 Sensitivity Analysis

<!-- b000635 | furniture | pages [23] -->
Page 22 of 53

<!-- b000636 | furniture | pages [23] -->


<!-- b000637 | furniture | pages [23] -->


<!-- b000638 | prose | pages [23] -->
(1) In horizontal blade case, We make comparisons of Su of the leaves with petioles

<!-- b000639 | prose | pages [23] -->
and the leaves without petioles. The result is as follows: Case 1:1: The max value is unchanged and the mean value increases by 1% Case 2:1 and Case 8:1: The max value is unchanged and the mean value increases by less than 0.3%

<!-- b000640 | prose | pages [23] -->
S variance with inclination angle, petiole (2) In our model, we mainly discuss U U

<!-- b000641 | prose | pages [23] -->
S is not so U length and leaf index, the relation between these 3 factors with

<!-- b000642 | prose | pages [23] -->
“self-evident”. Now we discuss the max S in one of the most representative U

<!-- b000643 | prose | pages [23] -->
scenario, where SAAngle=45 degree, SDAngle=90 degree, Interlength=0.4, Leaf-index=1, petiolelength=0. If SAAngle, SDAngle, Interlength, Leaf-index increase 5% respectively,

<!-- b000644 | prose | pages [23] -->
petiolength increase 0.05, The diagram below shows the variance ratio of each parameter. parameter

<!-- b000645 | prose | pages [23] -->
SAAngle SDAngle Interlength Leaf-index petiolelength

<!-- b000646 | prose | pages [23] -->
*Note: petiolelength effect mean value of

<!-- b000647 | prose | pages [23] -->
S U Variance of Max

<!-- b000648 | prose | pages [23] -->
2.5% -0.0167% 1.35% 0.0153% 0 0

<!-- b000649 | prose | pages [23] -->
S U

<!-- b000650 | prose | pages [23] -->
The sensitivity analysis above is quite different and the most significant 2 factors

<!-- b000651 | prose | pages [23] -->
are SAAngle and interlength. Effective area are relatively insensitive to other factors.

<!-- b000652 | furniture | pages [23] -->


<!-- b000653 | furniture | pages [23] -->


<!-- b000654 | heading | pages [23] -->
4. Model

<!-- b000655 | prose | pages [23] -->
of the Relation between Leaf Shape and Leaf Distribution

<!-- b000656 | heading | pages [23] -->
Introduction

<!-- b000657 | prose | pages [23] -->
Since leaves on one tree are always analogical to each other due to the genetical reasons, in this section we neglect other parameters of the shape of leaves and only focus on the leaf blade area, namely the leaf size, variation due to spatial distribution of them.

<!-- b000658 | furniture | pages [24] -->
#Team 16831

<!-- b000659 | furniture | pages [24] -->
Page 23 of 53

<!-- b000660 | furniture | pages [24] -->


<!-- b000661 | furniture | pages [24] -->


<!-- b000662 | prose | pages [24] -->
However, the contributing factors to the leaf size of the same species is too many in natural environment, such as water supply, sunlight, wind, insects, branch angle, soil fertilize condition and so on. The spatial distribution of these factors is complicated and tough to make a comprehensively quantitative analysis. So we focused on the illumination distribution which is closely related to the leaf position in different part in the tree canopy. Therefore we are trying to find following relations: 1. The relation between layers of the canopy (the height of different layers) and illumination intensity. 2. The relation between horizontal position of leaf and illumination intensity. 3. The relation between leaf blade area and illumination intensity.

<!-- b000663 | furniture | pages [24] -->


<!-- b000664 | prose | pages [24] -->
Combining these relations, we finally find the relation between leaf area and the distribution of leaf where distribution refers to both the horizontal and vertical position of leaves.

<!-- b000665 | furniture | pages [24] -->


<!-- b000666 | heading | pages [24] -->
Assumptions

<!-- b000667 | prose | pages [24] -->
1. The illumination intensity on the same layer of canopy is only determined by the leaf height and the distance from the trunk. 2. When considering the factors to determine the leaf size, other external factors such as water and density of carbon dioxide are abundant for the survival of leaves. 3. The maximum leaf size exist which is determined by the tree species traits. We assume it to be a constant. 4. Leaf has a living and constructional energy cost.

<!-- b000668 | furniture | pages [24] -->


<!-- b000669 | prose | pages [24] -->
Based on assumptions above, we build a light distribution model and a leaf size model.

<!-- b000670 | furniture | pages [24] -->


<!-- b000671 | heading | pages [24] -->
4.1 Light Distribution

<!-- b000672 | heading | pages [24] -->
 Jackson’s model

<!-- b000673 | prose | pages [24] -->
In 1995, Jackson [15] built a model of the distribution of illumination intensity within the tree canopy, which is thought to be effective, shown as:

<!-- b000674 | prose | pages [24] -->
 

<!-- b000675 | heading | pages [24] -->
0 exp(

<!-- b000676 | prose | pages [24] -->
I I kl )

<!-- b000677 | furniture | pages [24] -->


<!-- b000678 | prose | pages [24] -->
0I is the light intensity above the tree canopy; k is so-called light Where

<!-- b000679 | prose | pages [24] -->
absorption coefficient, which is determined by the tree characters including factors such as leaf optical traits the leaf inclination angle, branch structure and leaf density;

<!-- b000680 | prose | pages [24] -->
l here refers to the vertical depths start from the top of canopy.

<!-- b000681 | furniture | pages [24] -->


<!-- b000682 | furniture | pages [25] -->
#Team 16831

<!-- b000683 | furniture | pages [25] -->
Page 24 of 53

<!-- b000684 | furniture | pages [25] -->


<!-- b000685 | furniture | pages [25] -->


<!-- b000686 | prose | pages [25] -->
The formula clearly showed an exponentially declination of illumination intensity through vertical direction.

<!-- b000687 | furniture | pages [25] -->


<!-- b000688 | heading | pages [25] -->
 Our model

<!-- b000689 | prose | pages [25] -->
If we consider the difference of illumination intensity on horizontal plane, which is significant in actual condition, the Jackson’s model apparently cannot show this factor.

<!-- b000690 | furniture | pages [25] -->


<!-- b000691 | prose | pages [25] -->
Based on the model build by Jackson, we add a horizontal declination term to the equation. In consideration of the actual scenario, the declination speed in horizontal direction is much slower in compared with the vertical declination, since the light reflectance by leaf is always much greater than penetration. Therefore, we add a linear term and get an improved illumination intensity distribution as follows:

<!-- b000692 | prose | pages [25] -->
   I I 0(1  D )exp( kl )

<!-- b000693 | furniture | pages [25] -->


<!-- b000694 | prose | pages [25] -->
Where is the horizontal declination coefficient determined by the tree; D is the distance from the trunk of the tree canopy.

<!-- b000695 | furniture | pages [25] -->


<!-- b000696 | caption | pages [25] -->
Figure 20. variable definition

<!-- b000697 | prose | pages [25] -->
The figure above shows the variables in the equation.

<!-- b000698 | furniture | pages [25] -->


<!-- b000699 | prose | pages [25] -->
Coefficients,  and k , can be estimated by the actual illumination intensity in certain position, the center of top layer, on top layer surface, on bottom layer surface.

<!-- b000700 | prose | pages [25] -->
We simulate the distribution of light in Matlab, and get a surface of light distribution showing below.

<!-- b000701 | furniture | pages [26] -->
#Team 16831

<!-- b000702 | furniture | pages [26] -->
Page 25 of 53

<!-- b000703 | furniture | pages [26] -->


<!-- b000704 | furniture | pages [26] -->


<!-- b000705 | furniture | pages [26] -->


<!-- b000706 | caption | pages [26] -->
Figure 21. light distribution within a tree

<!-- b000707 | heading | pages [26] -->
Result Analysis

<!-- b000708 | prose | pages [26] -->
We compare the tendency of the tree distribution with a series data of an apple tree in SUN’s paper [16]. The curve tendency matches pretty well. Considering the location of the tree, an orchard, where it is well irrigated, well fertilized and grown up with sufficient sunlight, we assume our model assumptions about the living condition is eligible. So we believe our model is well built.

<!-- b000709 | furniture | pages [26] -->


<!-- b000710 | heading | pages [26] -->
4.2 Leaf Size Model

<!-- b000711 | heading | pages [26] -->
Analysis before modeling

<!-- b000712 | prose | pages [26] -->
It’s easy to know that leaf blade area increases when illumination strengthens since the process of photosynthesis becomes intensive and more nutrition is produced which will help the growth of leaf. However, the size of leaf cannot be infinitely large, that is, many limitations lying in environment condition (e.g. the density of carbon dioxide) and genetic factors may cause the termination of growing even if illumination intensity keeps strengthening.

<!-- b000713 | furniture | pages [26] -->


<!-- b000714 | heading | pages [26] -->
Details of the model

<!-- b000715 | prose | pages [26] -->
Thus we consider using modified Logistic Model (Pierre Verhulst ,1838)  to analyze the relation between leaf area and illumination intensity. We give the modified equation and explain why we modify it. The leaf size is described by the differential equation:

<!-- b000716 | prose | pages [26] -->
dS  r I dI S  0 (1 )

<!-- b000717 | furniture | pages [26] -->


<!-- b000718 | prose | pages [26] -->
K

<!-- b000719 | furniture | pages [27] -->
#Team 16831

<!-- b000720 | prose | pages [27] -->
Where:

<!-- b000721 | prose | pages [27] -->
S refers to leaf blade area. I refers to illumination intensity.

<!-- b000722 | furniture | pages [27] -->
Page 26 of 53

<!-- b000723 | furniture | pages [27] -->


<!-- b000724 | furniture | pages [27] -->


<!-- b000725 | prose | pages [27] -->
K refers to the upper limit of leaf blade area.

<!-- b000726 | prose | pages [27] -->
0r  refers to the size growth rate in the absence of external and internal limitations.

<!-- b000727 | prose | pages [27] -->
To show the relation between leaf size and light supply, we modified 2 terms in the equation, replacing S by I in describing the increasing rate, and replacing the temporal variable t by I. After the modification, the equation can describe the increasing rate, which is proportional to the product of light intensity and the 1 minus normalized size. This present the mechanism we discussed in Analysis part. The differential equation can be solved by integration of I and S respectively and simultaneously.

<!-- b000728 | furniture | pages [27] -->


<!-- b000729 | prose | pages [27] -->
The equation has the following solution:

<!-- b000730 | prose | pages [27] -->


<!-- b000731 | prose | pages [27] -->
S

<!-- b000732 | prose | pages [27] -->
 

<!-- b000733 | prose | pages [27] -->
0

<!-- b000734 | prose | pages [27] -->
K

<!-- b000735 | prose | pages [27] -->
[1 (1 )exp(

<!-- b000736 | prose | pages [27] -->
 

<!-- b000737 | prose | pages [27] -->
S I

<!-- b000738 | prose | pages [27] -->
( )

<!-- b000739 | prose | pages [27] -->
K

<!-- b000740 | prose | pages [27] -->
 

<!-- b000741 | prose | pages [27] -->
1 1

<!-- b000742 | prose | pages [27] -->
  

<!-- b000743 | prose | pages [27] -->
2 2

<!-- b000744 | prose | pages [27] -->
r I r I

<!-- b000745 | prose | pages [27] -->
)](

<!-- b000746 | prose | pages [27] -->
I I

<!-- b000747 | prose | pages [27] -->
)

<!-- b000748 | prose | pages [27] -->
0 0 0 0

<!-- b000749 | prose | pages [27] -->
2 2

<!-- b000750 | furniture | pages [27] -->


<!-- b000751 | prose | pages [27] -->


<!-- b000752 | prose | pages [27] -->
0(

<!-- b000753 | prose | pages [27] -->
I I

<!-- b000754 | prose | pages [27] -->
)

<!-- b000755 | prose | pages [27] -->
0

<!-- b000756 | prose | pages [27] -->
Considering that leaves are not able to survive when the initial illumination

<!-- b000757 | prose | pages [27] -->
0I and 0S , referring to the critical intensity is too small, we give them initial value,

<!-- b000758 | prose | pages [27] -->
scenario when minimum leaf size possible. The curve of the solution is presented below.

<!-- b000759 | furniture | pages [27] -->


<!-- b000760 | caption | pages [27] -->
Figure 21. relation of leaf blade area and light intensity

<!-- b000761 | prose | pages [27] -->
In the figure above，we can see leaves cannot live in a weak-lighted area. If the light get stronger than the min light needed, the leaf blade area shows an approximately linear increasing, and when the leaf is approaching the maximum size

<!-- b000762 | furniture | pages [28] -->
#Team 16831

<!-- b000763 | furniture | pages [28] -->
Page 27 of 53

<!-- b000764 | furniture | pages [28] -->


<!-- b000765 | furniture | pages [28] -->


<!-- b000766 | prose | pages [28] -->
possible, they show a slower increasing speed with a certain light increasing. This curve agrees with our common sense, in places where stronger sunlight can be seen, leaves are larger when they are matured, and leaf cannot live in dim light areas (e.g. under the bottom a canopy).The saturated light intensity can be seen in researches of photosynthesis.

<!-- b000767 | heading | pages [28] -->
4.3 Result and Analysis

<!-- b000768 | furniture | pages [28] -->


<!-- b000769 | furniture | pages [28] -->


<!-- b000770 | prose | pages [28] -->
The overall relation of leaf blade area and leaf distribution is as follows:

<!-- b000771 | prose | pages [28] -->


<!-- b000772 | prose | pages [28] -->
S

<!-- b000773 | prose | pages [28] -->
 

<!-- b000774 | prose | pages [28] -->
0

<!-- b000775 | prose | pages [28] -->
1 1

<!-- b000776 | prose | pages [28] -->
  

<!-- b000777 | prose | pages [28] -->
2 2

<!-- b000778 | prose | pages [28] -->
)exp(

<!-- b000779 | prose | pages [28] -->
K

<!-- b000780 | prose | pages [28] -->
[1 (1

<!-- b000781 | prose | pages [28] -->
 

<!-- b000782 | prose | pages [28] -->
S I

<!-- b000783 | prose | pages [28] -->
( )

<!-- b000784 | prose | pages [28] -->
K

<!-- b000785 | prose | pages [28] -->
 

<!-- b000786 | prose | pages [28] -->
Where

<!-- b000787 | prose | pages [28] -->
   I I 0(1

<!-- b000788 | prose | pages [28] -->
r I r I

<!-- b000789 | prose | pages [28] -->
)](

<!-- b000790 | prose | pages [28] -->
I I

<!-- b000791 | prose | pages [28] -->
)

<!-- b000792 | prose | pages [28] -->
0 0 0 0

<!-- b000793 | prose | pages [28] -->
2 2

<!-- b000794 | prose | pages [28] -->


<!-- b000795 | prose | pages [28] -->
0(

<!-- b000796 | prose | pages [28] -->
I I

<!-- b000797 | prose | pages [28] -->
)

<!-- b000798 | prose | pages [28] -->
0

<!-- b000799 | furniture | pages [28] -->


<!-- b000800 | prose | pages [28] -->
 D )exp( kl )

<!-- b000801 | furniture | pages [28] -->


<!-- b000802 | prose | pages [28] -->
D and l describe the position of the leaf. According to these two equations, we plot a surface to see how the leaves are distributed within a tree. We give the surface in following figure to show size distribution. According to these two models, we plot a surface to see how the leaves are distributed within the canopy of a tree. We give the surface in the following figure.

<!-- b000803 | furniture | pages [28] -->


<!-- b000804 | caption | pages [28] -->
Figure 22. leaf area distribution

<!-- b000805 | prose | pages [28] -->
The figure above shows the leaf size distribution along vertical (height) and horizontal (radius) direction, the higher the larger, the closer to the truck the larger the larger is the leaf size.

<!-- b000806 | prose | pages [28] -->
From this figure we also find out that leaf size is more sensitive in vertical direction than horizontal. As a result the leaf size distribution is generally seen in the way that higher leaves are more possible to be larger.

<!-- b000807 | furniture | pages [29] -->
#Team 16831

<!-- b000808 | furniture | pages [29] -->
Page 28 of 53

<!-- b000809 | furniture | pages [29] -->


<!-- b000810 | furniture | pages [29] -->


<!-- b000811 | prose | pages [29] -->
However, in this figure, the down critical point of the weak light effect is not marked because of cumbersome calculation problems.

<!-- b000812 | furniture | pages [29] -->


<!-- b000813 | heading | pages [29] -->
5. Model

<!-- b000814 | prose | pages [29] -->
of the Relation Leaf between Shape and Branching Structure

<!-- b000815 | heading | pages [29] -->
5.1 Introduction

<!-- b000816 | prose | pages [29] -->
The branching patterns of understory saplings and exposed canopy trees were classified as (David. A King et al 1999):  Orthotropic: three-dimensional arrangements of leaves about ascending twigs  Plagiotropic: leaves arranged in planes, usually along the sides of horizontal

<!-- b000817 | prose | pages [29] -->
twigs

<!-- b000818 | furniture | pages [29] -->


<!-- b000819 | furniture | pages [29] -->


<!-- b000820 | prose | pages [29] -->
Orthotropic                           Plagiotropic

<!-- b000821 | caption | pages [29] -->
Figure 23. Orthotropic and Plagiotropic trees

<!-- b000822 | furniture | pages [29] -->


<!-- b000823 | prose | pages [29] -->
In this section, we use these two categories to describe the branching structure of trees and each of them has its own unique characteristics in branching structures. In orthotropic branching, the axes are upwardly inclined and the leaves are arranged around them in more or less radial symmetry, whereas in plagiotropic branching, planes of foliage are formed from leaves arranged along the sides of nearly horizontal twigs (HalleÂ et al. 1978; Givnish 1984). Next, we will formulate a model to analyze the dependence of branching structures on three leaf parameters. And through this model, we can evaluate whether branching structures will effect leaf shape.

<!-- b000824 | furniture | pages [29] -->


<!-- b000825 | heading | pages [29] -->
5.2 Logistic Regression Model

<!-- b000826 | prose | pages [29] -->
Discriminant analysis was used to determine the function that best separated the orthotropic and plagiotropic species in terms of the three measured leaf dimensions. The analysis was based on logistic regression (Ripley 1996), with the discriminant function taking the form:

<!-- b000827 | prose | pages [29] -->
   d a b log( PL ) i i 1  b b log( BL ) b log( BW )

<!-- b000828 | furniture | pages [29] -->


<!-- b000829 | prose | pages [29] -->
2 2 3

<!-- b000830 | furniture | pages [30] -->
#Team 16831

<!-- b000831 | prose | pages [30] -->
Where:

<!-- b000832 | prose | pages [30] -->
PL refers to petiole length of leaves BL refers to blade length of leaves BW refers to blade width of leaves

<!-- b000833 | furniture | pages [30] -->
Page 29 of 53

<!-- b000834 | furniture | pages [30] -->


<!-- b000835 | furniture | pages [30] -->


<!-- b000836 | prose | pages [30] -->
i   refers to site and the leaf dimensions have been logarithmically transformed to make the distributions of the two architectural groups more nearly normal.

<!-- b000837 | prose | pages [30] -->
ia is a variable determined by latitude, and 1b , 2b , 3b are constants.

<!-- b000838 | prose | pages [30] -->
id  0 Orthotropy is expected for species for Which

<!-- b000839 | prose | pages [30] -->
id  0 , with the

<!-- b000840 | prose | pages [30] -->
, and plagiotropy when

<!-- b000841 | prose | pages [30] -->
probability of orthotropy for a randomly selected species given as:

<!-- b000842 | prose | pages [30] -->
 d ip e  d / (1 e )

<!-- b000843 | furniture | pages [30] -->


<!-- b000844 | prose | pages [30] -->
i i i

<!-- b000845 | prose | pages [30] -->
This discrimination function provides a convenient way to relate the branch pattern of a tree to its leaf shapes and a method to classify branch patterns according to the parameters of leaves.

<!-- b000846 | furniture | pages [30] -->


<!-- b000847 | heading | pages [30] -->
5.3 Testing of the Model

<!-- b000848 | prose | pages [30] -->
By the work of David A. King [1999], the coefficients of the discriminant function are estimated, and the equation can be rewritten as:

<!-- b000849 | prose | pages [30] -->
   id 7.0 0.19 latitude 6.30log(

<!-- b000850 | prose | pages [30] -->
   id 7.0 0.19 latitude or

<!-- b000851 | prose | pages [30] -->
  PL ) 6.80log( BL ) 6.80log( BW )

<!-- b000852 | furniture | pages [30] -->


<!-- b000853 | prose | pages [30] -->
 6.30log( PL ) 6.80log( BL BW / )

<!-- b000854 | furniture | pages [30] -->


<!-- b000855 | prose | pages [30] -->
Using data from King [1999] who has collected the leaves and their parameters in five areas, we test the accuracy of the model and the result is as follows:

<!-- b000856 | caption | pages [30] -->
Table 5. classification result

<!-- b000857 | furniture | pages [30] -->


<!-- b000858 | furniture | pages [30] -->


<!-- b000859 | furniture | pages [30] -->


<!-- b000860 | furniture | pages [30] -->


<!-- b000861 | prose | pages [30] -->
1 2 Total species 127 109 Correct-classified

<!-- b000862 | prose | pages [30] -->
126 93

<!-- b000863 | prose | pages [30] -->
species

<!-- b000864 | prose | pages [30] -->
accuracy 0.99 0.85

<!-- b000865 | furniture | pages [30] -->


<!-- b000866 | prose | pages [30] -->
Region

<!-- b000867 | furniture | pages [30] -->


<!-- b000868 | furniture | pages [30] -->


<!-- b000869 | prose | pages [30] -->
3 4 Total 102 118 456

<!-- b000870 | prose | pages [30] -->
90 105 414

<!-- b000871 | prose | pages [30] -->
0.88 0.89 0.91

<!-- b000872 | prose | pages [30] -->
Clear to see, this model has quite high accuracy and can be used to classify branch patterns according to the leaf parameters. On the other hand, the correctness of the model has demonstrated that the leaf shapes (blade length, blade width and petiole length) of trees are strongly related to the branch structure of trees. It is these three parameters that determine the branch pattern of a tree synthetically.

<!-- b000873 | furniture | pages [30] -->


<!-- b000874 | furniture | pages [30] -->


<!-- b000875 | furniture | pages [31] -->
#Team 16831

<!-- b000876 | furniture | pages [31] -->
Page 30 of 53

<!-- b000877 | furniture | pages [31] -->


<!-- b000878 | heading | pages [31] -->
5.4 Relations of Leaf Shape and Branch Pattern

<!-- b000879 | prose | pages [31] -->
Having justified the close relation between leaf shapes and branch patterns, next we analyze the relation in detail. As we know, the blade length and petiole length are important indicators of leaf shapes. In the following figures we show the difference between the two branch patterns in these two parameters in the four regions.

<!-- b000880 | furniture | pages [31] -->


<!-- b000881 | furniture | pages [31] -->


<!-- b000882 | furniture | pages [31] -->


<!-- b000883 | caption | pages [31] -->
Figure 23. differences of Orthotropic and Plagiotropic trees

<!-- b000884 | prose | pages [31] -->
For trees of the two patterns in the four areas, we investigate the relation of branch pattern and each of the leaf shape parameter individually. The parameters of leaves include:  Petiole length  Blade length  Length-width ratio (leaf index)  Simple or compound leaf

<!-- b000885 | furniture | pages [31] -->


<!-- b000886 | prose | pages [31] -->
For the first three parameters, we use t-test to determine the relation between each parameter and the two branching patterns; a linear fitting is also shown to better demonstrate the relation between petiole length and Length-width ratio for orthotropy trees.

<!-- b000887 | furniture | pages [32] -->
#Team 16831

<!-- b000888 | furniture | pages [32] -->


<!-- b000889 | prose | pages [32] -->
 petiole length The t-test result is as follows:

<!-- b000890 | furniture | pages [32] -->
Page 31 of 53

<!-- b000891 | furniture | pages [32] -->


<!-- b000892 | furniture | pages [32] -->


<!-- b000893 | caption | pages [32] -->
Table 6. petiole length

<!-- b000894 | prose | pages [32] -->
Mean log ( petiole length/cm) of species Rigion Plagiotropic 0.16±0.08 1 0.23±0.03 2 -0.16±0.02 3 -0.04±0.01 4

<!-- b000895 | furniture | pages [32] -->


<!-- b000896 | prose | pages [32] -->
orthotropic P 0.58±0.04 6.644e-16 0.47±0.03 2.836e-08 0.32±0.04 5.596e-05 0.24±0.02 4.106e-09

<!-- b000897 | prose | pages [32] -->
It can be easily seen from the table that Plagiotropic and orthotropic species differ sub-stantially in petiole length. Generally, the petiole length of orthotropic trees is notably larger than that of plagiotropic trees, and further explanation of this result will be provided hereinafter.

<!-- b000898 | furniture | pages [32] -->


<!-- b000899 | prose | pages [32] -->
 blade length

<!-- b000900 | prose | pages [32] -->
The t-test result is as follows:

<!-- b000901 | furniture | pages [32] -->


<!-- b000902 | caption | pages [32] -->
Table 7. blade length

<!-- b000903 | prose | pages [32] -->
Mean log ( blade length/cm) of species Rigion Plagiotropic 1.29±0.04 1 1.21±0.03 2 1.21±0.02 3 1.23±0.01 4

<!-- b000904 | furniture | pages [32] -->


<!-- b000905 | prose | pages [32] -->
orthotropic P 1.39±0.02 3.621e-04 1.33±0.03 1.545e-03 1.31±0.04 4.322e-02 1.30±0.02 3.056e-03

<!-- b000906 | prose | pages [32] -->
The P-Value again shows that there exists true difference in mean between the blade length of plagiotropic and orthotropic trees. From the mean value we can see that from both the 4 regions the mean blade length of orthotropic trees is higher than plagiotropic trees, but not as notable as the comparison of petiole length.

<!-- b000907 | furniture | pages [32] -->


<!-- b000908 | prose | pages [32] -->
 Length-width ratio (leaf index) The t-test result is as follows:

<!-- b000909 | caption | pages [32] -->
Table 8. leaf index

<!-- b000910 | prose | pages [32] -->
Mean log ( blade length/cm) of species Rigion Plagiotropic 2.39±0.15 1 3.43±0.28 2 3.56±0.14 3 2.64±0.06 4

<!-- b000911 | furniture | pages [32] -->


<!-- b000912 | prose | pages [32] -->
orthotropic P 1.87±0.09 6.261e-02 2.42±0.11 3.243e-04 2.21±0.06 1.275e-08 1.68±0.03 4.136e-06

<!-- b000913 | prose | pages [32] -->
As we can see, the length-width ratio, which determine the narrowness of a leaf, differs significantly in the two branching patterns. Generally, the length-width ratio of

<!-- b000914 | furniture | pages [33] -->
#Team 16831

<!-- b000915 | furniture | pages [33] -->
Page 32 of 53

<!-- b000916 | furniture | pages [33] -->


<!-- b000917 | furniture | pages [33] -->


<!-- b000918 | prose | pages [33] -->
orthotropic trees is smaller than plagiotropic trees, meaning that orthotropic tree leaves are relatively broader than plagiotropic trees. Meanwhile, considering the longer petiole of orthotropic trees, we try to find the relationship between these two characteristics. The figure below shows the relation of them for orthotropic trees.

<!-- b000919 | furniture | pages [33] -->


<!-- b000920 | caption | pages [33] -->
Figure 23. relation of petiole length and length-width ratio

<!-- b000921 | prose | pages [33] -->
The figure shows a strong correlation between the petiole length and the length-width ratio of leaves. R2=0.86, demonstrating the accuracy of linear fitting. It means that when the length-width ratio of leaves increase, the petiole length grows accordingly.

<!-- b000922 | furniture | pages [33] -->


<!-- b000923 | prose | pages [33] -->
 Simple or compound leaf

<!-- b000924 | prose | pages [33] -->
We analyze the relation between whether a specie has simple or compound leaves and its branching pattern. Using data from King [1999], we get the proportion of these two types of leaves in the two branching patterns, respectively. The following figure shows the proportion in the 4 areas, and a total proportion is also considered.

<!-- b000925 | furniture | pages [33] -->


<!-- b000926 | prose | pages [33] -->
100

<!-- b000927 | prose | pages [33] -->
80

<!-- b000928 | prose | pages [33] -->
60

<!-- b000929 | prose | pages [33] -->
Simple-leaved species

<!-- b000930 | prose | pages [33] -->
40

<!-- b000931 | prose | pages [33] -->
Compound-

<!-- b000932 | prose | pages [33] -->
20

<!-- b000933 | prose | pages [33] -->
leaved species

<!-- b000934 | prose | pages [33] -->
0

<!-- b000935 | prose | pages [33] -->
SA-P

<!-- b000936 | prose | pages [33] -->
CR-P

<!-- b000937 | prose | pages [33] -->
NQ-O

<!-- b000938 | prose | pages [33] -->
PA-O

<!-- b000939 | prose | pages [33] -->
PA-P

<!-- b000940 | prose | pages [33] -->
SA-O

<!-- b000941 | prose | pages [33] -->
CR-O

<!-- b000942 | prose | pages [33] -->
NQ-P

<!-- b000943 | prose | pages [33] -->
250

<!-- b000944 | prose | pages [33] -->
Simple-leaved species

<!-- b000945 | prose | pages [33] -->
200

<!-- b000946 | prose | pages [33] -->
Compound-leaved

<!-- b000947 | prose | pages [33] -->
150

<!-- b000948 | prose | pages [33] -->
species

<!-- b000949 | prose | pages [33] -->
100

<!-- b000950 | prose | pages [33] -->
50

<!-- b000951 | prose | pages [33] -->
0

<!-- b000952 | prose | pages [33] -->
plagiotropic orthotropic

<!-- b000953 | furniture | pages [33] -->


<!-- b000954 | caption | pages [33] -->
Figure 24. statistics in 4 areas            figure 25. total statistics

<!-- b000955 | prose | pages [33] -->
*Note: SA, PA, CR and NQ stand for four areas, and P, O stand for plagiotropic and orthotropic trees.

<!-- b000956 | furniture | pages [33] -->


<!-- b000957 | furniture | pages [34] -->
#Team 16831

<!-- b000958 | furniture | pages [34] -->
Page 33 of 53

<!-- b000959 | furniture | pages [34] -->


<!-- b000960 | prose | pages [34] -->
From the total statistics above we can figure out that for plagiotropic trees, simple-leaved species are in priority and reach a proportion of over 70%, while for orthotropic trees there is no significant difference between the amounts of these two kinds of species.

<!-- b000961 | furniture | pages [34] -->


<!-- b000962 | heading | pages [34] -->
5.5 Conclusions and Analysis

<!-- b000963 | prose | pages [34] -->
From the statistical analysis above, we can get the following conclusions:  The branch patterns are strongly related to leaf shapes, including their petiole

<!-- b000964 | prose | pages [34] -->
length, blade length, length-width ratio (leaf index), and it is a synthetic effect of all of them.  The petioles of orthotropic trees are generally longer than plagiotropic trees.  The length-width ratios (leaf index) of orthotropic trees are generally smaller

<!-- b000965 | prose | pages [34] -->
than plagiotropic trees, meaning that the former have broader leaves than the latter.  The blade of orthotropic trees are generally longer than plagiotropic trees. Along

<!-- b000966 | prose | pages [34] -->
with the point above, we can conclude that the leaf size of orthotropic trees are larger.  There is significant positive correlation between the length-width ratios and

<!-- b000967 | prose | pages [34] -->
petiole length for orthotropic trees.  A majority of plagiotropic trees are simple-leaved while for orthotropic trees

<!-- b000968 | prose | pages [34] -->
there are no notable differences.

<!-- b000969 | prose | pages [34] -->
As is discussed above, the major differences in leaf shapes for plagiotropic and orthotropic trees are that orthotropic trees have broader leaves and longer petioles. This can be explained by the overlap and photosynthesis efficiency of leaves. For plagiotropic trees, the effect of overlap is much smaller, so the petiole needn’t be long, whereas orthotropic species with orthotropic trees which have more steeply angled branches require longer petioles to avoid self-shading. It explains the positive correlation between the petiole length and length-width ratio for orthotropic trees, and more importantly, it is consistent with our model in Part II as well as previous literature such as the models of light interception in relation to leaf shape and phyllotaxis (Niklas 1988 and Takenaka 1994).

<!-- b000970 | furniture | pages [34] -->


<!-- b000971 | furniture | pages [34] -->


<!-- b000972 | heading | pages [34] -->
6. Model

<!-- b000973 | prose | pages [34] -->
of Leaf Mass Estimation

<!-- b000974 | heading | pages [34] -->
6.1 A Basic Volumetric Model

<!-- b000975 | prose | pages [34] -->
We use a volumetric method to estimate the leaf mass (LM) . Based on the idea of past studies, we use six geometric solids to approximate the tree crown shapes defined by their crown heights and mean crown radiuses: cylinder, vertical ellipsoid, paraboloid, cone, sphere, pyramid.

<!-- b000976 | furniture | pages [35] -->
#Team 16831

<!-- b000977 | furniture | pages [35] -->
Page 34 of 53

<!-- b000978 | furniture | pages [35] -->


<!-- b000979 | furniture | pages [35] -->


<!-- b000980 | prose | pages [35] -->
h

<!-- b000981 | prose | pages [35] -->
r

<!-- b000982 | furniture | pages [35] -->


<!-- b000983 | caption | pages [35] -->
Figure 26. volumetric model

<!-- b000984 | prose | pages [35] -->
Then the leaf mass can be calculated:

<!-- b000985 | prose | pages [35] -->
Leaf mass= volume of geometric solids * leaf mass constant

<!-- b000986 | prose | pages [35] -->
The leaf mass constant (LMC) can be found in the literature. For example, for oak trees the value is approximately 280g/cm3 (). Then we need to calculate the volume of the geometric solids using the crown heights (CH) and mean crown radiuses (CR). If we use a cone to approximate the crown, the leaf mass for an oak tree can be calculated as follows:

<!-- b000987 | prose | pages [35] -->
  LM V LMC 1    2 r h 280

<!-- b000988 | furniture | pages [35] -->


<!-- b000989 | prose | pages [35] -->
3

<!-- b000990 | prose | pages [35] -->
The following table shows the results using this model to estimate the leaf mass of 14 oak trees, and the measured leaf mass is also included:

<!-- b000991 | caption | pages [35] -->
Table 9. leaf mass estimation using volumetric model

<!-- b000992 | prose | pages [35] -->
fraction to measured leaf mass

<!-- b000993 | furniture | pages [35] -->


<!-- b000994 | furniture | pages [35] -->


<!-- b000995 | furniture | pages [35] -->


<!-- b000996 | prose | pages [35] -->
tree CH(m) CR(m) Cylinder Vertical ellipsoid

<!-- b000997 | prose | pages [35] -->
1 4.4 1.1 1.34 0.89

<!-- b000998 | prose | pages [35] -->
2 4.1 2.0 1.48 0.99 3 3.2 1.1 1.54 1.03 4 6.3 1.4 2.08 1.38 5 4.5 1.8 1.89 1.26 6 4.5 1.2 2.92 1.25 7 5.6 1.1 1.35 0.99 8 5.0 1.5 1.84 1.23 9 7.5 3.6 2.92 1.95 10 2.8 1.1 1.63 1.09 11 4.5 1.5 1.70 1.21 12 4.6 1.2 2.65 1.37 13 5.5 1.8 1.73 1.26

<!-- b000999 | furniture | pages [35] -->


<!-- b001000 | prose | pages [35] -->
Paraboloid Cone Sphere Pyramid measured

<!-- b001001 | prose | pages [35] -->
LM(g)

<!-- b001002 | prose | pages [35] -->
0.77 0.45 1.96 1.92 3500

<!-- b001003 | prose | pages [35] -->
0.85 0.49 3.95 0.64

<!-- b001004 | prose | pages [35] -->
9750

<!-- b001005 | prose | pages [35] -->
0.89 0.51 2.26 2.21

<!-- b001006 | prose | pages [35] -->
2210

<!-- b001007 | prose | pages [35] -->
1.19 0.69 3.88 1.84

<!-- b001008 | prose | pages [35] -->
5230

<!-- b001009 | prose | pages [35] -->
1.09 0.63 4.53 1.01

<!-- b001010 | prose | pages [35] -->
6790

<!-- b001011 | prose | pages [35] -->
1.68 0.97 4.68 3.52

<!-- b001012 | prose | pages [35] -->
1950

<!-- b001013 | prose | pages [35] -->
0.78 0.45 1.98 1.93

<!-- b001014 | prose | pages [35] -->
4420

<!-- b001015 | prose | pages [35] -->
1.06 0.61 3.68 1.42

<!-- b001016 | prose | pages [35] -->
5380

<!-- b001017 | prose | pages [35] -->
1.68 0.97 14.01 0.39

<!-- b001018 | prose | pages [35] -->
29300

<!-- b001019 | prose | pages [35] -->
0.94 0.54 2.39 2.33

<!-- b001020 | prose | pages [35] -->
1830

<!-- b001021 | prose | pages [35] -->
0.98 0.57 3.41 1.31

<!-- b001022 | prose | pages [35] -->
5230

<!-- b001023 | prose | pages [35] -->
1.32 0.88 4.24 3.19

<!-- b001024 | prose | pages [35] -->
2200

<!-- b001025 | prose | pages [35] -->
1.00 0.58 4.16 0.93

<!-- b001026 | prose | pages [35] -->
9040

<!-- b001027 | furniture | pages [36] -->
#Team 16831

<!-- b001028 | prose | pages [36] -->
14 2.0 2.1 1.31 0.87

<!-- b001029 | furniture | pages [36] -->
Page 35 of 53

<!-- b001030 | furniture | pages [36] -->


<!-- b001031 | furniture | pages [36] -->


<!-- b001032 | prose | pages [36] -->
0.75 0.44 3.66 0.51 5930

<!-- b001033 | furniture | pages [36] -->


<!-- b001034 | furniture | pages [36] -->


<!-- b001035 | prose | pages [36] -->
According to the result, the mean fraction for the respective six solids is as follows:

<!-- b001036 | caption | pages [36] -->
Table 10. a comparision

<!-- b001037 | furniture | pages [36] -->


<!-- b001038 | prose | pages [36] -->
Cylinder Vertical ellipsoid

<!-- b001039 | prose | pages [36] -->
mean fraction

<!-- b001040 | prose | pages [36] -->
1.80 1.18

<!-- b001041 | prose | pages [36] -->
to MLM

<!-- b001042 | furniture | pages [36] -->


<!-- b001043 | prose | pages [36] -->
Paraboloi

<!-- b001044 | prose | pages [36] -->
Cone Sphere pyramid

<!-- b001045 | prose | pages [36] -->
d

<!-- b001046 | prose | pages [36] -->
1.09 0.60 3.44 1.75

<!-- b001047 | prose | pages [36] -->
Clear to see, for paraboloid and vertical ellipsoid, mean fraction (also defined as the total leaf mass estimates factor) is 1.09 and 1.18 of the measured, respectively. Therefore, these two solids give estimates of total leaf mass within 12 percent of the measured, justifying that this model works well to give a relatively accurate estimate of leaf mass.

<!-- b001048 | furniture | pages [36] -->


<!-- b001049 | heading | pages [36] -->
6.2 An Improvement of the Model

<!-- b001050 | prose | pages [36] -->
In the previous discussion we define the leaf-mass constant as a real “constant”, while this is not the actual case. As a tree grows up, the leaf-mass constant (namely, the ratio of leaf mass to crown volume) will decrease, because the outer surface of the crown tend to move up and out as the branches grow, so crown volume increases as the cube of the distance from the outer leave to the center of the tree. Thus, it is not hard to see that LMC will decrease as a tree grows (its crown volume increases). A notable example is the 9th tree in the table 1. When the crown volume V reaches a larger value, the fraction of both paraboloid and vertical ellipsoid is a little bit abnormal and inaccurate. On the other hand, it is easy to see that for the two best solids, paraboloid and vertical ellipsoid, the model both overestimate the actual LM. Thus, a decrease must be also needed to make up. For the two reasons above, we multiply an attenuation factor related to the crown volume to the previous equation:

<!-- b001051 | prose | pages [36] -->
V LMC e    LM

<!-- b001052 | prose | pages [36] -->
λ=0.01 in the model.

<!-- b001053 | prose | pages [36] -->
  V

<!-- b001054 | furniture | pages [36] -->


<!-- b001055 | prose | pages [36] -->
When crown volume V is small, the impact of H on LM is little and can be

<!-- b001056 | prose | pages [36] -->
e   V neglected. However, when crown volume V grows the impact of cannot be

<!-- b001057 | prose | pages [36] -->
overlooked. Using the improved model, we calculate the leaf mass above again (choosing the paraboloid and vertical ellipsoid models) and get the revised leaf mass. The result is as follows:

<!-- b001058 | furniture | pages [36] -->


<!-- b001059 | caption | pages [36] -->
Table 11. two better estimation methods

<!-- b001060 | prose | pages [36] -->
vertical ellipsoid

<!-- b001061 | furniture | pages [36] -->


<!-- b001062 | prose | pages [36] -->
paraboloid

<!-- b001063 | furniture | pages [37] -->
#Team 16831

<!-- b001064 | heading | pages [37] -->
Basic model

<!-- b001065 | prose | pages [37] -->
1.18

<!-- b001066 | heading | pages [37] -->
Improved model

<!-- b001067 | prose | pages [37] -->
1.08

<!-- b001068 | furniture | pages [37] -->


<!-- b001069 | furniture | pages [37] -->
Page 36 of 53

<!-- b001070 | furniture | pages [37] -->


<!-- b001071 | furniture | pages [37] -->


<!-- b001072 | prose | pages [37] -->
1.09 1.02

<!-- b001073 | prose | pages [37] -->
We can see that the revised model has truly improved the estimation and finally get highly accurate result.

<!-- b001074 | furniture | pages [37] -->


<!-- b001075 | heading | pages [37] -->
6.3 Allometric Equation Model

<!-- b001076 | prose | pages [37] -->
In this model, we use a commonly used and conveniently measured parameter of a tree to estimate the leaf mass: the diameter at breast height (DBH). An equation is needed to relate DBH to the leaf mass of a tree.

<!-- b001077 | furniture | pages [37] -->


<!-- b001078 | heading | pages [37] -->
6.3.1 A previous method

<!-- b001079 | prose | pages [37] -->
According to Nowak [1996], there is an allometric equation between these two variables:

<!-- b001080 | prose | pages [37] -->
  ln Y 7.6109 0.0643 X (equation 1)

<!-- b001081 | prose | pages [37] -->
Y is the leaf mass and X is DBH. It provides a relatively accurate and convenient method to approximate the leaf mass, but it overlooks the inner mechanism of the life of a tree and the result just comes from data fitting method.

<!-- b001082 | furniture | pages [37] -->


<!-- b001083 | heading | pages [37] -->
6.3.2 A more accurate model considering the biological mechanism

<!-- b001084 | prose | pages [37] -->
of trees

<!-- b001085 | prose | pages [37] -->
We analyze the biological mechanism of trees to determine the relation between  LM and DBH. As we know, the mass of leaf is depended on its capacity to carry materials (mainly water), which is determined by the vascular system. The area of vascular system is proportional to the intersection area of the stem, which is proportional to the square of diameter or circumference. Thus, a second order equation can be used to describe the relation between DBH and LM:

<!-- b001086 | prose | pages [37] -->
   2 Y aX bX c

<!-- b001087 | furniture | pages [37] -->


<!-- b001088 | furniture | pages [37] -->


<!-- b001089 | furniture | pages [37] -->


<!-- b001090 | furniture | pages [37] -->


<!-- b001091 | furniture | pages [37] -->


<!-- b001092 | prose | pages [37] -->
(equation 2)

<!-- b001093 | prose | pages [37] -->
We use this equation to couple the data from Table 9 and get the following fitting result:

<!-- b001094 | furniture | pages [37] -->


<!-- b001095 | furniture | pages [38] -->
#Team 16831

<!-- b001096 | furniture | pages [38] -->
Page 37 of 53

<!-- b001097 | furniture | pages [38] -->


<!-- b001098 | furniture | pages [38] -->


<!-- b001099 | furniture | pages [38] -->


<!-- b001100 | caption | pages [38] -->
Figure 27. fitting of leaf mass and DBH

<!-- b001101 | furniture | pages [38] -->


<!-- b001102 | furniture | pages [38] -->


<!-- b001103 | prose | pages [38] -->
R2=0.98, showing a very accurate fitting result.

<!-- b001104 | furniture | pages [38] -->


<!-- b001105 | furniture | pages [38] -->


<!-- b001106 | prose | pages [38] -->
Using the data above, we can also plot the relation between DBH and LM using equation 1 and equation 2 and get the following result. The measured LM is also included in the figure.

<!-- b001107 | furniture | pages [38] -->


<!-- b001108 | caption | pages [38] -->
Figure 28. a comparison of two allometric models

<!-- b001109 | furniture | pages [38] -->


<!-- b001110 | prose | pages [38] -->
It can be easily seen that the second model (two order allometric model) is better than the previous one in the literature, so we choose equation2 to estimate

<!-- b001111 | furniture | pages [39] -->
#Team 16831

<!-- b001112 | furniture | pages [39] -->
Page 38 of 53

<!-- b001113 | furniture | pages [39] -->


<!-- b001114 | prose | pages [39] -->
leaf mass of trees.

<!-- b001115 | furniture | pages [39] -->


<!-- b001116 | heading | pages [39] -->
6.4 Conclusions and Overall Comparison of models

<!-- b001117 | prose | pages [39] -->
As is discussed above, we can get the following conclusions:  For volumetric model, paraboloid and vertical ellipsoid solids are the best to

<!-- b001118 | prose | pages [39] -->
approximate the crown profiles. Crown height and crown radius are used in the model, and for relatively higher trees, the tree height is also useful to get more accurate estimation.  For allometric equation model, a second order equation related to DBH of trees

<!-- b001119 | prose | pages [39] -->
is better and more convenient for estimation.

<!-- b001120 | furniture | pages [39] -->


<!-- b001121 | prose | pages [39] -->
Using data from Table 9, we make a comparison of volumetric model and

<!-- b001122 | prose | pages [39] -->
allometric model, the result shows that the mean fractions to measured LM using these two models are 0.93 and 1.03, respectively. Both of two models show high accuracy. However, considering that using AEM, we only need to measure DBH of a tree, which of quite convenient, so eventually we view the allometric equation model as the best to solve this problem.

<!-- b001123 | furniture | pages [39] -->


<!-- b001124 | furniture | pages [39] -->


<!-- b001125 | furniture | pages [39] -->


<!-- b001126 | heading | pages [39] -->
7. Strength and Weakness

<!-- b001127 | heading | pages [39] -->
 Model of leaf shape description and classification

<!-- b001128 | heading | pages [39] -->
Strength

<!-- b001129 | prose | pages [39] -->
1. Since our model is built based on cluster analysis, the result of classification is approached completely by mathematical calculation which ensures there will be no subjective factors involved in the result. 2. The only inputs of our model are 4 parameters, no extra information needed to be provided. 3. According to the testing result, the validity of our model is verified. 4. This model can be used not only in leaves classification, but also any classification problems.

<!-- b001130 | heading | pages [39] -->
Weakness

<!-- b001131 | prose | pages [39] -->
1. This model is highly feasible when it is used to classify not too many leaves, once the amount of leaves gets too large, the amount of computation will be so excessive that it will take too much time finishing the classification. 2. The process of cluster may lack specialized support in botany.

<!-- b001132 | furniture | pages [39] -->


<!-- b001133 | heading | pages [39] -->
 Model of the relation of leaf shape and overlap

<!-- b001134 | furniture | pages [40] -->
#Team 16831

<!-- b001135 | furniture | pages [40] -->
Page 39 of 53

<!-- b001136 | furniture | pages [40] -->


<!-- b001137 | heading | pages [40] -->
Strength

<!-- b001138 | prose | pages [40] -->
1. A universal used method to calculate overlapping area in different cases 2. Clearly analytical expression is obtained, and the results are statistically characterized 3. Discuss all the 5 different variables sensitivity

<!-- b001139 | furniture | pages [40] -->


<!-- b001140 | heading | pages [40] -->
Weakness

<!-- b001141 | prose | pages [40] -->
1. We only focused on leaves on one branch, failed to consider the impact by neighboring branches 2. Other complex factors (e.g. leaf flatness, unparalleled light), which may be significant as well, are not taken into consideration.

<!-- b001142 | heading | pages [40] -->
 Model of the relation of leaf shape and distribution

<!-- b001143 | heading | pages [40] -->
Strength

<!-- b001144 | prose | pages [40] -->
1. We build models from the mechanism of light intensity distribution which make sense reasonably 2. We find a simple but effective way to describe the leaf size and the light intensity 3. We neglected the detail structure within the tree, making it more generally applicable to different structures.

<!-- b001145 | heading | pages [40] -->
Weakness

<!-- b001146 | prose | pages [40] -->
1. The ideal assumptions about environment are somewhat too radical, maybe only few areas can fit it well 2. We need more data to test and revise our model 3. The coefficients are needed to be determined in either experimental way or empirical way to get a higher precise level

<!-- b001147 | heading | pages [40] -->
 Model of the relation of leaf shape and branching structure

<!-- b001148 | heading | pages [40] -->
Strength

<!-- b001149 | prose | pages [40] -->
1. We figure out the light intensity distribution in a tree based on the experiment data of previous researchers, and this simplified our model. 2. We successfully derived the relation between light intensity and leaf blade area based on Logistic model. 3. We draw the distribution figure so that the result is shown more clearly.

<!-- b001150 | heading | pages [40] -->
Weakness

<!-- b001151 | prose | pages [40] -->
1. We only focus on the leaf blade area, while did not consider the other leaf parameters to simplify the model. 2. We lack enough data to test our model.

<!-- b001152 | furniture | pages [40] -->


<!-- b001153 | furniture | pages [41] -->
#Team 16831

<!-- b001154 | furniture | pages [41] -->
Page 40 of 53

<!-- b001155 | furniture | pages [41] -->


<!-- b001156 | heading | pages [41] -->
 Model of leaf mass estimation

<!-- b001157 | heading | pages [41] -->
Strength

<!-- b001158 | prose | pages [41] -->
1. We build several models and make detailed comparison among them. 2. The volumetric method is quite easy to understand and calculate. 3. Our optimal method only needs the data of diameter at the breast height, which is convenient to measure, and the method has high accuracy.

<!-- b001159 | heading | pages [41] -->
Weakness

<!-- b001160 | prose | pages [41] -->
1. Some of the allometric equations are based on statistic method and lack theoretical support. 2. We haven’t thoroughly figure out the biological mechanism that determines leaf mass, and only a simplified biological analysis is considered

<!-- b001161 | furniture | pages [41] -->


<!-- b001162 | heading | pages [41] -->
8. Further Work

<!-- b001163 | prose | pages [41] -->
Since ecological phenomena are multi-factor determined, we can do a lot of jobs about the leaves of a tree. Here we mention 2 important directions: 1.

<!-- b001164 | prose | pages [41] -->
Consider the relation between water supply and mechanism of transpiration,

<!-- b001165 | prose | pages [41] -->
and estimate its impact on the leaf shape and leaf mass. 2.

<!-- b001166 | prose | pages [41] -->
Search more detailed data to clarify the cases where our models cannot be

<!-- b001167 | prose | pages [41] -->
used

<!-- b001168 | furniture | pages [41] -->


<!-- b001169 | furniture | pages [41] -->


<!-- b001170 | furniture | pages [41] -->


<!-- b001171 | furniture | pages [41] -->


<!-- b001172 | furniture | pages [41] -->


<!-- b001173 | furniture | pages [41] -->


<!-- b001174 | furniture | pages [41] -->


<!-- b001175 | furniture | pages [41] -->


<!-- b001176 | furniture | pages [41] -->


<!-- b001177 | furniture | pages [41] -->


<!-- b001178 | furniture | pages [42] -->
#Team 16831

<!-- b001179 | furniture | pages [42] -->
Page 41 of 53

<!-- b001180 | furniture | pages [42] -->


<!-- b001181 | furniture | pages [42] -->


<!-- b001182 | heading | pages [42] -->
9. A letter to Scientific Journal

<!-- b001183 | prose | pages [42] -->
Editor

<!-- b001184 | prose | pages [42] -->
Dear editor, In the contest, we developed models to analyze leaves, including description and classification, their relations with overlap, distribution and branching structure, as well as leaf mass estimation. We solved a series of problems on leaf shapes and leaf mass, and here are our key findings on these problems as listed below, and hopefully they have scientific value. 1. There are two main factors leading to the diversity of leaves—genetic and environmental factors. Genetic factor is determined by genes while environmental factor is dominated by three sub factors: sunlight, carbon dioxide and temperature. 2. Cluster analysis can be an effective method to classify leaves as long as we have the specific data on 4 parameters of leaves which refer to leaf index, leaf area, concave ratio and leaf extended angle. 3. The shape of leaves is closely related to the overlapping shadow. Narrow leaves tend to be more effective in maximizing the exposure to sunlight, and this conclusion always works whether petiole and blade inclination exist or not. Longer leaf petiole is significant to decrease the overlap for broader leaves. 4. Leaves on higher layers are generally larger than the lower ones in ideal condition, and leaves further from the trunk are larger than the central ones. 5. Branching patterns of trees are strongly related to leaf shapes, including their petiole length, blade length, length-width ratio (leaf index), and it is a synthetic effect of all of them. 6. Orthotropic tree leaves are generally broader, larger and with longer petioles than that of trees. 7. A majority of plagiotropic trees are simple-leaved while for orthotropic trees there are no notable differences on whether the leaves are simple or compound. 8. We can get the total leaf mass of a tree by multiplying the crown volume and leaf mass constant, and paraboloid is the optimal geometric solid to approximate the crown for crown volume calculation. 9. The total leaf mass is statistically related to the size characteristics of a tree. A biological mechanism-based method, which shows that leaf mass is a quadratic function of the diameter at breast height (DBH) of a tree, is the most accurate and convenient way to estimate leaf mass.

<!-- b001185 | furniture | pages [42] -->


<!-- b001186 | prose | pages [42] -->
Since our findings are gained through both mathematical analysis and biological mechanism analysis, we really hope they will benefit the science research on tree leaves. Finally, thanks for your time.

<!-- b001187 | furniture | pages [42] -->


<!-- b001188 | furniture | pages [42] -->


<!-- b001189 | prose | pages [42] -->
BestRegards,

<!-- b001190 | furniture | pages [42] -->
Team # 16831

<!-- b001191 | furniture | pages [43] -->
#Team 16831

<!-- b001192 | furniture | pages [43] -->
Page 42 of 53

<!-- b001193 | furniture | pages [43] -->


<!-- b001194 | heading | pages [43] -->
10. Reference

<!-- b001195 | furniture | pages [43] -->


<!-- b001196 | prose | pages [43] -->
[1]http://www.psu.edu/dept/nkbiology/naturetrail/leaves.htm

<!-- b001197 | furniture | pages [43] -->


<!-- b001198 | prose | pages [43] -->
[2]Zalikha Zulkifli  Puteh Saad  Itaza Afiani Mohtar  Plant Leaf Identification using Moment Invariants & General Regression Neural Network

<!-- b001199 | furniture | pages [43] -->


<!-- b001200 | prose | pages [43] -->
[3]Hirokazu Tsukaya  Mechanism of Leaf-Shape Determination  Annu. Rev. Plant Biol.2006. 57:477–96

<!-- b001201 | furniture | pages [43] -->


<!-- b001202 | prose | pages [43] -->
[4]Ülo Niinemets and Lawren Sack   Structural determinants of leaf light-harvesting capacity and photosynthetic potentials Progress in Botany, Vol. 67 Springer-Verlag Berlin Heidelberg 2006

<!-- b001203 | furniture | pages [43] -->


<!-- b001204 | prose | pages [43] -->
[5]AKIO TAKENAKA ,Effects of leaf blade narrowness and petiole length on the light capture efficiency of a shoot , Ecological Research (1994) 9, 109-114

<!-- b001205 | furniture | pages [43] -->


<!-- b001206 | prose | pages [43] -->
[6]Chia-Ling Lee, Shu-Yuan Chen, Classification of Leaf Images, under grant NSC-95–2745-E-155– 008-URD, 2006 Wiley Periodicals, Inc.

<!-- b001207 | furniture | pages [43] -->


<!-- b001208 | prose | pages [43] -->
[7]C. Faloutsos, R. Barber, M. Flickner, J. Hafner, W. Niblack, D. Petkovic,and W. Equitz, Efficient and effective querying by image content, J IntellInform Syst 3 (1994), 231–262

<!-- b001209 | furniture | pages [43] -->


<!-- b001210 | prose | pages [43] -->
[8]Zalikha Zulkifli, Puteh, SaadItaza, Afiani Mohtar Plant Leaf Identification using Moment Invariants & General Regression Neural Network 978-1-4577-2152-6/11/$26.00_c 2011 IEEE

<!-- b001211 | furniture | pages [43] -->


<!-- b001212 | prose | pages [43] -->
[9]Akio Takenaka,  A Simulation Model of Tree Architecture Development Based on Growth Response to Local Light Environment Journal of Plant Research by The Botanical Society of Japan 1994

<!-- b001213 | furniture | pages [43] -->


<!-- b001214 | prose | pages [43] -->
[10]Daniel S. Falster and Mark Westoby , Leaf size and angle vary widely across species: what consequences for light interception New Phytologist(2003)158: 509–525   www.newphytologist.com

<!-- b001215 | furniture | pages [43] -->


<!-- b001216 | prose | pages [43] -->
[11]Magali Willaume . Pierre-Éric Lauri . Hervé Sinoquet, Light interception in apple trees influenced by canopy architecture manipulation Received: 5 November 2003 / Accepted: 24 June 2004 / Published online: 29 July 2004  Springer-Verlag 2004

<!-- b001217 | furniture | pages [43] -->


<!-- b001218 | prose | pages [43] -->
[12]Aluru MR, Bae H,Wu D, Rodermel SR. 2001. The Arabidopsis immutans mutation affects plastid differentiation and the morphogenesis of white and green sectors in variegated plants. Plant Physiol. 127:67–77

<!-- b001219 | furniture | pages [43] -->


<!-- b001220 | furniture | pages [44] -->
#Team 16831

<!-- b001221 | furniture | pages [44] -->
Page 43 of 53

<!-- b001222 | furniture | pages [44] -->


<!-- b001223 | furniture | pages [44] -->


<!-- b001224 | prose | pages [44] -->
[13]Beerling DJ, Osborne CP, Chaloner WG. 2001. Evolution of leaf-form in land plants linked to atmospheric CO2 decline in the Late Palaeozoic era. Nature 410:352–54

<!-- b001225 | furniture | pages [44] -->


<!-- b001226 | prose | pages [44] -->
[14]Barritt B H. Vertical aris training seen as alternative for apple [J]. Good Fruit Grower, 1998, 39 (3): 24-26.

<!-- b001227 | furniture | pages [44] -->


<!-- b001228 | prose | pages [44] -->
[15]Jackson J E. Theory of modeling by model hedgerow ordards in relation to latitude, time of the year and hedgerow configuration and orientation. J Apple Ecol, 1980, 9: 341-357.

<!-- b001229 | furniture | pages [44] -->


<!-- b001230 | prose | pages [44] -->
[16]SUN Zhi- hong1, WEI Qin- ping2*, YANG Chao- xuan3, SUN Zhong- fu4, WANG Xiao- wei2 Relationships between distribution of r elative light intensity and shoots and foliage in different tier of canopy of Red Fuji apple trees with modified open centre tree shape

<!-- b001231 | furniture | pages [44] -->


<!-- b001232 | prose | pages [44] -->
[17]DAVID A. KING* and JOHN H. MAINDONALD, Tree architecture in relation to leaf dimensions and tree stature in temperate and tropical rain forests Journal of Ecology 1999, 87, 1012±1024

<!-- b001233 | heading | pages [44] -->
Appendix

<!-- b001234 | prose | pages [44] -->
Appendix1:

<!-- b001235 | prose | pages [44] -->
The data extracted from the leaf images

<!-- b001236 | furniture | pages [44] -->


<!-- b001237 | prose | pages [44] -->
approximated area width length(in pixel)  Leaf index extend  angle(roughly) Class1 101 108 1.069306931 5454 concave-ratio leaf

<!-- b001238 | prose | pages [44] -->
1

<!-- b001239 | furniture | pages [44] -->


<!-- b001240 | prose | pages [44] -->
90 4357.5 1 Class2 83 105 1.265060241 Class3 146 47 0.321917808 3431 Class4 140 60 0.428571429 4200

<!-- b001241 | furniture | pages [44] -->


<!-- b001242 | prose | pages [44] -->
180 0.97

<!-- b001243 | furniture | pages [44] -->


<!-- b001244 | prose | pages [44] -->
270 0.3642 180 6667.5 1 Class5  127 105 0.826771654 Class6 141 74 0.524822695 5217 Class7 131 94 0.717557252 6157 Class8 80 110 1.375 4400 1

<!-- b001245 | furniture | pages [44] -->


<!-- b001246 | prose | pages [44] -->
Class9 73 106 1.452054795 3869 Class10 87 104 1.195402299 4524 Class11 84 106 1.261904762 4452 Class12 56 104 1.857142857 2912 Class13 30 110 3.666666667 1650

<!-- b001247 | furniture | pages [44] -->


<!-- b001248 | prose | pages [44] -->
180 1

<!-- b001249 | furniture | pages [44] -->


<!-- b001250 | prose | pages [44] -->
240 0.2367 240 60 0.1781 60 1

<!-- b001251 | furniture | pages [44] -->


<!-- b001252 | prose | pages [44] -->
90 1

<!-- b001253 | furniture | pages [44] -->


<!-- b001254 | prose | pages [44] -->
120 1

<!-- b001255 | furniture | pages [44] -->


<!-- b001256 | prose | pages [44] -->
60 1

<!-- b001257 | furniture | pages [44] -->


<!-- b001258 | prose | pages [44] -->
120 0.9333 Class14 69 102 1.47826087 3519 Class15 100 93 0.93 4650 0.9 Class16 113 100 0.884955752 5650 Class17 90 94 1.044444444 4230 Class18 50 106 2.12 2650 1

<!-- b001259 | furniture | pages [44] -->


<!-- b001260 | prose | pages [44] -->
120 90 1

<!-- b001261 | furniture | pages [44] -->


<!-- b001262 | prose | pages [44] -->
180 0.8333 150 30

<!-- b001263 | furniture | pages [45] -->
#Team 16831

<!-- b001264 | prose | pages [45] -->
Class19 138 92 0.666666667 6348 Class22 44 94 2.136363636 2068 Class23 136 73 0.536764706 4964 Class29 104 99 0.951923077 5148 Class31 51 106 2.078431373 2703 Class36 25 102 4.08 1275 1

<!-- b001265 | furniture | pages [45] -->


<!-- b001266 | prose | pages [45] -->
Class38 114 108 0.947368421 6156 Class40 100 104 1.04 5200 0.95 Class47 117 98 0.837606838 5733

<!-- b001267 | furniture | pages [45] -->
Page 44 of 53

<!-- b001268 | furniture | pages [45] -->


<!-- b001269 | furniture | pages [45] -->


<!-- b001270 | prose | pages [45] -->
0

<!-- b001271 | furniture | pages [45] -->


<!-- b001272 | prose | pages [45] -->
360 1

<!-- b001273 | furniture | pages [45] -->


<!-- b001274 | prose | pages [45] -->
30 0.3888 240 1

<!-- b001275 | furniture | pages [45] -->


<!-- b001276 | prose | pages [45] -->
180 1

<!-- b001277 | furniture | pages [45] -->


<!-- b001278 | prose | pages [45] -->
120 30 1

<!-- b001279 | furniture | pages [45] -->


<!-- b001280 | prose | pages [45] -->
120

<!-- b001281 | furniture | pages [45] -->


<!-- b001282 | furniture | pages [45] -->


<!-- b001283 | prose | pages [45] -->
180 0.7614 180 3847.5 0.1852 Class48 81 95 1.172839506 Class50 111 76 0.684684685 4218 Class52 117 62 0.52991453 3627 0 Class53 101 60 0.594059406 3030 Class60 140 80 0.571428571 5600

<!-- b001284 | furniture | pages [45] -->


<!-- b001285 | prose | pages [45] -->
cluster analysis code

<!-- b001286 | furniture | pages [45] -->


<!-- b001287 | prose | pages [45] -->
R Code > rt2<-read.table("sj2.txt",head=T) > X<-scale(rt2,center=T,scale=T) > D2<-dist(X) > hc2<-hclust(D2,"ward") > plot(hc2,hang=-1,main="ward method") > rect.hclust(hc2,k=4)

<!-- b001288 | furniture | pages [45] -->


<!-- b001289 | furniture | pages [45] -->


<!-- b001290 | heading | pages [45] -->
Classification result of cluster analysis

<!-- b001291 | prose | pages [45] -->
Name type Class1 3 Class2 4 Class3 1 Class4 1 Class5  3 Class6 1 Class7 1 Class8 4 Class9 4 Class10 4 Class11 4 Class12 2 Class13 2 Class14 4 Class15 4 Class16 3 90 0

<!-- b001292 | furniture | pages [45] -->


<!-- b001293 | prose | pages [45] -->
270

<!-- b001294 | furniture | pages [45] -->


<!-- b001295 | furniture | pages [45] -->


<!-- b001296 | prose | pages [45] -->
360 0.539

<!-- b001297 | furniture | pages [45] -->


<!-- b001298 | prose | pages [45] -->
270 0.84

<!-- b001299 | furniture | pages [45] -->


<!-- b001300 | prose | pages [45] -->
240

<!-- b001301 | furniture | pages [46] -->
#Team 16831

<!-- b001302 | furniture | pages [46] -->
Page 45 of 53

<!-- b001303 | furniture | pages [46] -->


<!-- b001304 | prose | pages [46] -->
Class17 4 Class18 2 Class19 1 Class22 2 Class23 1 Class29 3 Class31 2 Class36 2 Class38 3 Class40 3 Class47 3 Class48 4 Class50 1 Class52 1 Class53 1 Class60 1

<!-- b001305 | furniture | pages [46] -->


<!-- b001306 | furniture | pages [46] -->


<!-- b001307 | prose | pages [46] -->
Appendix2:

<!-- b001308 | prose | pages [46] -->
Neural Network simulation code in Task 1:

<!-- b001309 | furniture | pages [46] -->


<!-- b001310 | furniture | pages [46] -->


<!-- b001311 | prose | pages [46] -->
clc ;

<!-- b001312 | prose | pages [46] -->
clear;

<!-- b001313 | prose | pages [46] -->
close all;

<!-- b001314 | prose | pages [46] -->
%% loading data

<!-- b001315 | prose | pages [46] -->
P0=load('trainning.txt');

<!-- b001316 | prose | pages [46] -->
P1=P0';

<!-- b001317 | prose | pages [46] -->
T0 = load('trainresult.txt');

<!-- b001318 | prose | pages [46] -->
T1=T0';

<!-- b001319 | prose | pages [46] -->
Ptem=load('testdata.txt');

<!-- b001320 | prose | pages [46] -->
P2 =Ptem';

<!-- b001321 | prose | pages [46] -->
PN1=P1;

<!-- b001322 | prose | pages [46] -->
PN2=P2;

<!-- b001323 | prose | pages [46] -->
net=newff(minmax(PN1),[10 1],{'tansig','purelin'},'trainlm');

<!-- b001324 | prose | pages [46] -->
net.trainParam.epochs=1000;

<!-- b001325 | prose | pages [46] -->
net.trainParam.show=10;

<!-- b001326 | prose | pages [46] -->
net.trainParam.lr=0.06;

<!-- b001327 | prose | pages [46] -->
net.trainParam.goal=0.01;

<!-- b001328 | prose | pages [46] -->
net.trainParam.min_grad = 1e-20;

<!-- b001329 | prose | pages [46] -->
net=train(net,PN1,T1);

<!-- b001330 | prose | pages [46] -->
%% simulation testing

<!-- b001331 | furniture | pages [47] -->
#Team 16831

<!-- b001332 | prose | pages [47] -->
T_sim=sim(net,P2);

<!-- b001333 | prose | pages [47] -->
%decision  process

<!-- b001334 | prose | pages [47] -->
for i=1:length(T_sim)

<!-- b001335 | prose | pages [47] -->
if T_sim(i)<=1.5

<!-- b001336 | prose | pages [47] -->
T_sim(i)=1;

<!-- b001337 | furniture | pages [47] -->
Page 46 of 53

<!-- b001338 | furniture | pages [47] -->


<!-- b001339 | furniture | pages [47] -->


<!-- b001340 | prose | pages [47] -->
else if T_sim(i)>1.5&&T_sim(i)<=2.5

<!-- b001341 | prose | pages [47] -->
T_sim(i)=2;

<!-- b001342 | prose | pages [47] -->
else if T_sim(i)>2.5&&T_sim(i)<=3.5

<!-- b001343 | prose | pages [47] -->
T_sim(i)=3;

<!-- b001344 | prose | pages [47] -->
else

<!-- b001345 | prose | pages [47] -->
T_sim(i)=4;

<!-- b001346 | prose | pages [47] -->
end

<!-- b001347 | prose | pages [47] -->
end

<!-- b001348 | prose | pages [47] -->
end

<!-- b001349 | prose | pages [47] -->
end

<!-- b001350 | prose | pages [47] -->
disp('The type of the testing leaves:');

<!-- b001351 | prose | pages [47] -->
disp(T_sim);

<!-- b001352 | furniture | pages [47] -->


<!-- b001353 | prose | pages [47] -->
Testing data extracted from leaf images:

<!-- b001354 | prose | pages [47] -->
approximated area

<!-- b001355 | furniture | pages [47] -->


<!-- b001356 | prose | pages [47] -->
width length Leaf index angle(roughly)

<!-- b001357 | furniture | pages [47] -->


<!-- b001358 | prose | pages [47] -->
concave ratio leaf extend

<!-- b001359 | prose | pages [47] -->
4147.5 1 Class21 79 105 1.329113924 Class24 58 106 1.827586207 3074 Class39 42 107 2.547619048 2247 Class51 49 66 1.346938776 1617 Class54 143 84 0.587412587 6006 Class55 58 98 1.689655172 2842 120 1 90 1 90 1 150 0.7889 240 1 90 2320.5 0.8627 60 Class57 51 91 1.784313725 Class59 68 98 1.441176471 3332

<!-- b001360 | furniture | pages [47] -->


<!-- b001361 | prose | pages [47] -->
Appendix3:

<!-- b001362 | furniture | pages [47] -->


<!-- b001363 | prose | pages [47] -->
Overlapping analysis without petiole

<!-- b001364 | furniture | pages [47] -->


<!-- b001365 | prose | pages [47] -->
clf;clc;

<!-- b001366 | prose | pages [47] -->
x=0:pi/360:pi;

<!-- b001367 | prose | pages [47] -->
for i=1:91;

<!-- b001368 | furniture | pages [47] -->


<!-- b001369 | furniture | pages [47] -->


<!-- b001370 | prose | pages [47] -->
0.9471 60

<!-- b001371 | prose | pages [47] -->
y(i)=2*(1-0.4*sin(pi/4-x(i))).*(1-0.4*cos(pi/4-x(i)))+0.4*sin(pi/4-x(

<!-- b001372 | prose | pages [47] -->
i)).*0.4*cos(pi/4-x(i));

<!-- b001373 | prose | pages [47] -->
end

<!-- b001374 | furniture | pages [48] -->
#Team 16831

<!-- b001375 | furniture | pages [48] -->
Page 47 of 53

<!-- b001376 | furniture | pages [48] -->


<!-- b001377 | prose | pages [48] -->
for i=92:271

<!-- b001378 | prose | pages [48] -->
y(i)=2*(1-0.4*sin(x(i)-pi/4)).*(1-0.4*cos(x(i)-pi/4));

<!-- b001379 | prose | pages [48] -->
end

<!-- b001380 | prose | pages [48] -->
for i=272:361

<!-- b001381 | furniture | pages [48] -->


<!-- b001382 | prose | pages [48] -->
y(i)=2*(1-0.4*sin(-3*pi/4+x(i))).*(1-0.4*cos(-3*pi/4+x(i)))+0.4*sin(-

<!-- b001383 | prose | pages [48] -->
3*pi/4+x(i)).*0.4*cos(-3*pi/4+x(i));

<!-- b001384 | prose | pages [48] -->
end

<!-- b001385 | furniture | pages [48] -->


<!-- b001386 | prose | pages [48] -->
plot(x/pi,4-y);

<!-- b001387 | prose | pages [48] -->
hold on;

<!-- b001388 | prose | pages [48] -->
crit=26.565*pi/180;

<!-- b001389 | prose | pages [48] -->
si=sin(pi-2*crit);

<!-- b001390 | prose | pages [48] -->
si2=sin(2*crit);

<!-- b001391 | prose | pages [48] -->
t=0:0.1*pi/180:pi;

<!-- b001392 | prose | pages [48] -->
for i=1:266

<!-- b001393 | furniture | pages [48] -->


<!-- b001394 | prose | pages [48] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-t(i))/si).*(0.5*sqrt(5)-0.4*sin(

<!-- b001395 | prose | pages [48] -->
t(i)+crit)/si)+0.4*0.8*(sin(crit-t(i))/si).*0.4*(sin(t(i)+crit)/si);

<!-- b001396 | prose | pages [48] -->
end

<!-- b001397 | prose | pages [48] -->
for i=267:1535

<!-- b001398 | furniture | pages [48] -->


<!-- b001399 | prose | pages [48] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(t(i)-crit)/si).*(0.5*sqrt(5)-0.4*sin(

<!-- b001400 | prose | pages [48] -->
pi-t(i)-crit)/si);

<!-- b001401 | prose | pages [48] -->
end

<!-- b001402 | prose | pages [48] -->
for i=1536:1801

<!-- b001403 | furniture | pages [48] -->


<!-- b001404 | prose | pages [48] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-pi+t(i))/si).*(0.5*sqrt(5)-0.4*s

<!-- b001405 | prose | pages [48] -->
in(pi-t(i)+crit)/si)+0.4*0.8*(sin(crit-pi+t(i))/si).*0.4*(sin(pi-t(i)

<!-- b001406 | prose | pages [48] -->
+crit)/si);

<!-- b001407 | prose | pages [48] -->
end

<!-- b001408 | furniture | pages [48] -->


<!-- b001409 | prose | pages [48] -->
plot(t/pi,4-z,'r');

<!-- b001410 | furniture | pages [48] -->


<!-- b001411 | prose | pages [48] -->
hold on;

<!-- b001412 | prose | pages [48] -->
crit=7.125*pi/180;

<!-- b001413 | prose | pages [48] -->
si=sin(pi-2*crit);

<!-- b001414 | prose | pages [48] -->
si2=sin(2*crit);

<!-- b001415 | prose | pages [48] -->
t=0:0.1*pi/180:pi;

<!-- b001416 | prose | pages [48] -->
for i=1:72

<!-- b001417 | furniture | pages [48] -->


<!-- b001418 | prose | pages [48] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-t(i))/si).*(0.25*sqrt(65)-0.4*

<!-- b001419 | prose | pages [48] -->
sin(t(i)+crit)/si)+0.4*si2*(sin(crit-t(i))/si).*0.4*(sin(t(i)+crit)/s

<!-- b001420 | prose | pages [48] -->
i);

<!-- b001421 | furniture | pages [49] -->
#Team 16831

<!-- b001422 | furniture | pages [49] -->
Page 48 of 53

<!-- b001423 | furniture | pages [49] -->


<!-- b001424 | prose | pages [49] -->
end

<!-- b001425 | prose | pages [49] -->
for i=73:1729

<!-- b001426 | furniture | pages [49] -->


<!-- b001427 | prose | pages [49] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(t(i)-crit)/si).*(0.25*sqrt(65)-0.4*

<!-- b001428 | prose | pages [49] -->
sin(pi-t(i)-crit)/si);

<!-- b001429 | prose | pages [49] -->
end

<!-- b001430 | prose | pages [49] -->
for i=1730:1801

<!-- b001431 | furniture | pages [49] -->


<!-- b001432 | prose | pages [49] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-pi+t(i))/si).*(0.25*sqrt(65)-0

<!-- b001433 | prose | pages [49] -->
.4*sin(pi-t(i)+crit)/si)+0.4*si2*(sin(crit-pi+t(i))/si).*0.4*(sin(pi-

<!-- b001434 | prose | pages [49] -->
t(i)+crit)/si);

<!-- b001435 | prose | pages [49] -->
end

<!-- b001436 | prose | pages [49] -->
maxvalue(1)=4-min(y);

<!-- b001437 | prose | pages [49] -->
maxvalue(2)=4-min(z);

<!-- b001438 | prose | pages [49] -->
maxvalue(3)=4-min(g);

<!-- b001439 | prose | pages [49] -->
disp('maxvalue');

<!-- b001440 | prose | pages [49] -->
disp(maxvalue);

<!-- b001441 | prose | pages [49] -->
degree(1)=4-y(91);

<!-- b001442 | prose | pages [49] -->
degree(2)=4-z(451);

<!-- b001443 | prose | pages [49] -->
degree(3)=4-g(451);

<!-- b001444 | prose | pages [49] -->
disp('45 degree');

<!-- b001445 | prose | pages [49] -->
disp(degree);

<!-- b001446 | prose | pages [49] -->
degree(1)=4-y(1);

<!-- b001447 | prose | pages [49] -->
degree(2)=4-z(1);

<!-- b001448 | prose | pages [49] -->
degree(3)=4-g(1);

<!-- b001449 | prose | pages [49] -->
disp('0 degree');

<!-- b001450 | prose | pages [49] -->
disp(degree);

<!-- b001451 | prose | pages [49] -->
meanvalue(1)=4-mean(y);

<!-- b001452 | prose | pages [49] -->
meanvalue(2)=4-mean(z);

<!-- b001453 | prose | pages [49] -->
meanvalue(3)=4-mean(g);

<!-- b001454 | prose | pages [49] -->
disp('meanvalue');

<!-- b001455 | prose | pages [49] -->
disp(meanvalue);

<!-- b001456 | prose | pages [49] -->
plot(t/pi,4-g,'g');

<!-- b001457 | furniture | pages [49] -->


<!-- b001458 | furniture | pages [49] -->


<!-- b001459 | prose | pages [49] -->
Overlapping analysis with petiole

<!-- b001460 | furniture | pages [49] -->


<!-- b001461 | prose | pages [49] -->
clf;clc;

<!-- b001462 | prose | pages [49] -->
x=0:pi/360:pi;

<!-- b001463 | prose | pages [49] -->
for i=1:91;

<!-- b001464 | furniture | pages [49] -->


<!-- b001465 | prose | pages [49] -->
y(i)=2*(1-0.4*sin(pi/4-x(i))).*(1-0.4*cos(pi/4-x(i)));

<!-- b001466 | prose | pages [49] -->
end

<!-- b001467 | prose | pages [49] -->
for i=92:271

<!-- b001468 | furniture | pages [50] -->
#Team 16831

<!-- b001469 | furniture | pages [50] -->
Page 49 of 53

<!-- b001470 | furniture | pages [50] -->


<!-- b001471 | prose | pages [50] -->
y(i)=2*(1-0.4*sin(x(i)-pi/4)).*(1-0.4*cos(x(i)-pi/4));

<!-- b001472 | prose | pages [50] -->
end

<!-- b001473 | prose | pages [50] -->
for i=272:361

<!-- b001474 | prose | pages [50] -->
y(i)=2*(1-0.4*sin(-3*pi/4+x(i))).*(1-0.4*cos(-3*pi/4+x(i)));

<!-- b001475 | prose | pages [50] -->
end

<!-- b001476 | prose | pages [50] -->
figure(3);

<!-- b001477 | prose | pages [50] -->
plot(x/pi,4-y);

<!-- b001478 | prose | pages [50] -->
hold on;

<!-- b001479 | prose | pages [50] -->
crit=26.565*pi/180;

<!-- b001480 | prose | pages [50] -->
si=sin(pi-2*crit);

<!-- b001481 | prose | pages [50] -->
si2=sin(2*crit);

<!-- b001482 | prose | pages [50] -->
t=0:0.1*pi/180:pi;

<!-- b001483 | prose | pages [50] -->
for i=1:266

<!-- b001484 | furniture | pages [50] -->


<!-- b001485 | prose | pages [50] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-t(i))/si).*(0.5*sqrt(5)-0.4*sin(

<!-- b001486 | prose | pages [50] -->
t(i)+crit)/si);

<!-- b001487 | prose | pages [50] -->
end

<!-- b001488 | prose | pages [50] -->
for i=267:1535

<!-- b001489 | furniture | pages [50] -->


<!-- b001490 | prose | pages [50] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(t(i)-crit)/si).*(0.5*sqrt(5)-0.4*sin(

<!-- b001491 | prose | pages [50] -->
pi-t(i)-crit)/si);

<!-- b001492 | prose | pages [50] -->
end

<!-- b001493 | prose | pages [50] -->
for i=1536:1801

<!-- b001494 | furniture | pages [50] -->


<!-- b001495 | prose | pages [50] -->
z(i)=2*0.8*(0.5*sqrt(5)-0.4*sin(crit-pi+t(i))/si).*(0.5*sqrt(5)-0.4*s

<!-- b001496 | prose | pages [50] -->
in(pi-t(i)+crit)/si);

<!-- b001497 | prose | pages [50] -->
end

<!-- b001498 | prose | pages [50] -->
plot(t/pi,4-z,'r');

<!-- b001499 | furniture | pages [50] -->


<!-- b001500 | prose | pages [50] -->
hold on;

<!-- b001501 | prose | pages [50] -->
crit=7.125*pi/180;

<!-- b001502 | prose | pages [50] -->
si=sin(pi-2*crit);

<!-- b001503 | prose | pages [50] -->
si2=sin(2*crit);

<!-- b001504 | prose | pages [50] -->
t=0:0.1*pi/180:pi;

<!-- b001505 | prose | pages [50] -->
for i=1:72

<!-- b001506 | furniture | pages [50] -->


<!-- b001507 | prose | pages [50] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-t(i))/si).*(0.25*sqrt(65)-0.4*

<!-- b001508 | prose | pages [50] -->
sin(t(i)+crit)/si);

<!-- b001509 | prose | pages [50] -->
end

<!-- b001510 | prose | pages [50] -->
for i=73:1729

<!-- b001511 | furniture | pages [50] -->


<!-- b001512 | prose | pages [50] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(t(i)-crit)/si).*(0.25*sqrt(65)-0.4*

<!-- b001513 | prose | pages [50] -->
sin(pi-t(i)-crit)/si);

<!-- b001514 | prose | pages [50] -->
end

<!-- b001515 | furniture | pages [51] -->
#Team 16831

<!-- b001516 | furniture | pages [51] -->
Page 50 of 53

<!-- b001517 | furniture | pages [51] -->


<!-- b001518 | prose | pages [51] -->
for i=1730:1801

<!-- b001519 | furniture | pages [51] -->


<!-- b001520 | prose | pages [51] -->
g(i)=2*si2*(0.25*sqrt(65)-0.4*sin(crit-pi+t(i))/si).*(0.25*sqrt(65)-0

<!-- b001521 | prose | pages [51] -->
.4*sin(pi-t(i)+crit)/si);

<!-- b001522 | prose | pages [51] -->
end

<!-- b001523 | prose | pages [51] -->
plot(t/pi,4-g,'g');

<!-- b001524 | prose | pages [51] -->
maxvalue(1)=4-min(y);

<!-- b001525 | prose | pages [51] -->
maxvalue(2)=4-min(z);

<!-- b001526 | prose | pages [51] -->
maxvalue(3)=4-min(g);

<!-- b001527 | prose | pages [51] -->
disp('maxvalue');

<!-- b001528 | prose | pages [51] -->
disp(maxvalue);

<!-- b001529 | prose | pages [51] -->
degree(1)=4-y(91);

<!-- b001530 | prose | pages [51] -->
degree(2)=4-z(451);

<!-- b001531 | prose | pages [51] -->
degree(3)=4-g(451);

<!-- b001532 | prose | pages [51] -->
disp('45 degree');

<!-- b001533 | prose | pages [51] -->
disp(degree);

<!-- b001534 | prose | pages [51] -->
degree(1)=4-y(1);

<!-- b001535 | prose | pages [51] -->
degree(2)=4-z(1);

<!-- b001536 | prose | pages [51] -->
degree(3)=4-g(1);

<!-- b001537 | prose | pages [51] -->
disp('0 degree');

<!-- b001538 | prose | pages [51] -->
disp(degree);

<!-- b001539 | prose | pages [51] -->
meanvalue(1)=4-mean(y);

<!-- b001540 | prose | pages [51] -->
meanvalue(2)=4-mean(z);

<!-- b001541 | prose | pages [51] -->
meanvalue(3)=4-mean(g);

<!-- b001542 | prose | pages [51] -->
disp('meanvalue');

<!-- b001543 | prose | pages [51] -->
disp(meanvalue);

<!-- b001544 | furniture | pages [51] -->


<!-- b001545 | furniture | pages [51] -->


<!-- b001546 | prose | pages [51] -->
Overlapping plotting with 30 degree inclination

<!-- b001547 | furniture | pages [51] -->


<!-- b001548 | prose | pages [51] -->
clf;

<!-- b001549 | prose | pages [51] -->
h=0.4; %%internode length ,can be revised

<!-- b001550 | prose | pages [51] -->
incang=pi/6; %%inclination angle, can be revised

<!-- b001551 | prose | pages [51] -->
sunang=pi/2; %%sun direction angle, can be revised

<!-- b001552 | furniture | pages [51] -->


<!-- b001553 | prose | pages [51] -->
m=8; %%leaf index, can be revised

<!-- b001554 | furniture | pages [51] -->


<!-- b001555 | prose | pages [51] -->
b=sqrt(2*m);

<!-- b001556 | prose | pages [51] -->
a=sqrt(2/m);

<!-- b001557 | prose | pages [51] -->
Transform_matrix=[1,0,-sin(sunang);0,1,-cos(sunang);0,0,0];

<!-- b001558 | prose | pages [51] -->
A=[0;0;h];

<!-- b001559 | prose | pages [51] -->
B=[a;cos(incang)*b;h+sin(incang)*b];

<!-- b001560 | prose | pages [51] -->
C=[0;2*cos(incang)*b;h+sin(incang)*2*b];

<!-- b001561 | prose | pages [51] -->
D=[-a;cos(incang)*b;h+sin(incang)*b];

<!-- b001562 | furniture | pages [52] -->
#Team 16831

<!-- b001563 | furniture | pages [52] -->
Page 51 of 53

<!-- b001564 | furniture | pages [52] -->


<!-- b001565 | prose | pages [52] -->
E=[a;-cos(incang)*b;h+sin(incang)*b];

<!-- b001566 | prose | pages [52] -->
F=[0;-2*cos(incang)*b;h+sin(incang)*2*b];

<!-- b001567 | prose | pages [52] -->
G=[-a;-cos(incang)*b;h+sin(incang)*b];

<!-- b001568 | prose | pages [52] -->
A2=Transform_matrix*A

<!-- b001569 | prose | pages [52] -->
B2=Transform_matrix*B

<!-- b001570 | prose | pages [52] -->
C2=Transform_matrix*C

<!-- b001571 | prose | pages [52] -->
D2=Transform_matrix*D

<!-- b001572 | prose | pages [52] -->
E2=Transform_matrix*E

<!-- b001573 | prose | pages [52] -->
F2=Transform_matrix*F

<!-- b001574 | prose | pages [52] -->
G2=Transform_matrix*G

<!-- b001575 | prose | pages [52] -->
points=[A2,B2,C2,D2,A2,E2,F2,G2,A2];

<!-- b001576 | prose | pages [52] -->
x=points(1,:);

<!-- b001577 | prose | pages [52] -->
y=points(2,:);

<!-- b001578 | prose | pages [52] -->
z=[0,0,0,0,0,0,0,0,0];

<!-- b001579 | prose | pages [52] -->
plot3(x,y,z);

<!-- b001580 | prose | pages [52] -->
grid;

<!-- b001581 | furniture | pages [52] -->


<!-- b001582 | furniture | pages [52] -->


<!-- b001583 | prose | pages [52] -->
h=0.0;

<!-- b001584 | prose | pages [52] -->
A=[0;0;h];

<!-- b001585 | prose | pages [52] -->
B=[a;cos(incang)*b;h+sin(incang)*b];

<!-- b001586 | prose | pages [52] -->
C=[0;2*cos(incang)*b;h+sin(incang)*2*b];

<!-- b001587 | prose | pages [52] -->
D=[-a;cos(incang)*b;h+sin(incang)*b];

<!-- b001588 | prose | pages [52] -->
E=[a;-cos(incang)*b;h+sin(incang)*b];

<!-- b001589 | prose | pages [52] -->
F=[0;-2*cos(incang)*b;h+sin(incang)*2*b];

<!-- b001590 | prose | pages [52] -->
G=[-a;-cos(incang)*b;h+sin(incang)*b];

<!-- b001591 | prose | pages [52] -->
A2=Transform_matrix*A

<!-- b001592 | prose | pages [52] -->
B2=Transform_matrix*B

<!-- b001593 | prose | pages [52] -->
C2=Transform_matrix*C

<!-- b001594 | prose | pages [52] -->
D2=Transform_matrix*D

<!-- b001595 | prose | pages [52] -->
E2=Transform_matrix*E

<!-- b001596 | prose | pages [52] -->
F2=Transform_matrix*F

<!-- b001597 | prose | pages [52] -->
G2=Transform_matrix*G

<!-- b001598 | prose | pages [52] -->
points=[A2,B2,C2,D2,A2,E2,F2,G2,A2];

<!-- b001599 | furniture | pages [52] -->


<!-- b001600 | prose | pages [52] -->
x=points(1,:);

<!-- b001601 | prose | pages [52] -->
y=points(2,:);

<!-- b001602 | furniture | pages [52] -->


<!-- b001603 | prose | pages [52] -->
z=[0,0,0,0,0,0,0,0,0];

<!-- b001604 | prose | pages [52] -->
hold on;

<!-- b001605 | prose | pages [52] -->
plot3(x,y,z,'r');

<!-- b001606 | prose | pages [52] -->
xlabel('X');

<!-- b001607 | prose | pages [52] -->
ylabel('Y');

<!-- b001608 | furniture | pages [52] -->


<!-- b001609 | furniture | pages [53] -->
#Team 16831

<!-- b001610 | furniture | pages [53] -->
Page 52 of 53

<!-- b001611 | furniture | pages [53] -->


<!-- b001612 | prose | pages [53] -->
Appendix3:

<!-- b001613 | prose | pages [53] -->
Surface of distribution plotting codes

<!-- b001614 | furniture | pages [53] -->


<!-- b001615 | prose | pages [53] -->
% illumination intensity distribution

<!-- b001616 | prose | pages [53] -->
a=0.02;

<!-- b001617 | prose | pages [53] -->
b=0.8;

<!-- b001618 | prose | pages [53] -->
c=0.1;

<!-- b001619 | prose | pages [53] -->
r=linspace(0, 10, 25);

<!-- b001620 | prose | pages [53] -->
h=linspace(0, 10, 25);

<!-- b001621 | prose | pages [53] -->
[r1,h1]=meshgrid(r, h);

<!-- b001622 | prose | pages [53] -->
L=(a*r1+b).*exp(-c*(10-h1));

<!-- b001623 | prose | pages [53] -->
surf(r1, h1, L);

<!-- b001624 | prose | pages [53] -->
xlabel('radius');

<!-- b001625 | prose | pages [53] -->
ylabel('height');

<!-- b001626 | prose | pages [53] -->
zlabel('relative illumination intensity');

<!-- b001627 | prose | pages [53] -->
title('light distribustion within a tree');

<!-- b001628 | furniture | pages [53] -->


<!-- b001629 | furniture | pages [53] -->


<!-- b001630 | prose | pages [53] -->
% blade area distribution

<!-- b001631 | prose | pages [53] -->
a=0.04;

<!-- b001632 | prose | pages [53] -->
b=0.8;

<!-- b001633 | prose | pages [53] -->
c=0.1;

<!-- b001634 | prose | pages [53] -->
S0=40;

<!-- b001635 | prose | pages [53] -->
Sm=500;

<!-- b001636 | prose | pages [53] -->
k=0.4;

<!-- b001637 | prose | pages [53] -->
r=linspace(0, 10, 25);

<!-- b001638 | prose | pages [53] -->
h=linspace(0, 10, 25);

<!-- b001639 | prose | pages [53] -->
[r1,h1]=meshgrid(r, h);

<!-- b001640 | prose | pages [53] -->
L=(a*r1+b).*exp(-c*(10-h1));

<!-- b001641 | prose | pages [53] -->
S=S0*Sm./(S0+(Sm-S0).*exp(-k.*L));

<!-- b001642 | prose | pages [53] -->
surf(r1,h1,S); % »-³öÁ¢ÌåÇúÃæÍ¼

<!-- b001643 | prose | pages [53] -->
xlabel('radius(m)');

<!-- b001644 | prose | pages [53] -->
ylabel('height(m)');

<!-- b001645 | prose | pages [53] -->
zlabel('area(mm2)');

<!-- b001646 | prose | pages [53] -->
title('leaf area distribution');

<!-- b001647 | furniture | pages [53] -->


<!-- b001648 | prose | pages [53] -->
Curve of light intensity with blade area plotting code I=0:0.05:35;

<!-- b001649 | prose | pages [53] -->
for i=1:101

<!-- b001650 | prose | pages [53] -->
S(i)=0;

<!-- b001651 | prose | pages [53] -->
end

<!-- b001652 | prose | pages [53] -->
for i=102:701

<!-- b001653 | furniture | pages [53] -->


<!-- b001654 | furniture | pages [54] -->
#Team 16831

<!-- b001655 | furniture | pages [54] -->
Page 53 of 53

<!-- b001656 | furniture | pages [54] -->


<!-- b001657 | prose | pages [54] -->
S(i)=(1-(0.8)*exp(-0.012*I(i).^2+0.012*5.^2));

<!-- b001658 | prose | pages [54] -->
end

<!-- b001659 | prose | pages [54] -->
plot(I,S);

<!-- b001660 | prose | pages [54] -->
xlabel('illumination intensity');

<!-- b001661 | prose | pages [54] -->
ylabel('leaf blade area');

<!-- b001662 | furniture | pages [54] -->


<!-- b001663 | furniture | pages [54] -->


<!-- b001664 | furniture | pages [54] -->


<!-- b001665 | furniture | pages [54] -->

