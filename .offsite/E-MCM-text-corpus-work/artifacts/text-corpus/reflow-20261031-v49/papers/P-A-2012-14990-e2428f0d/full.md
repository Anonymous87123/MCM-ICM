# P-A-2012-14990-e2428f0d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #14990

<!-- b000002 | furniture | pages [1] -->
1 / 42

<!-- b000003 | title | pages [1] -->
A Close Look On Leaves

<!-- b000004 | title | pages [1] -->
Team 14990

<!-- b000005 | furniture | pages [2] -->
Team #14990

<!-- b000006 | furniture | pages [2] -->
2 / 42

<!-- b000007 | heading | pages [2] -->
CONTENTS

<!-- b000008 | contents | pages [2] -->
1. Introduction------------------------------------------------------------------------------------3

<!-- b000009 | contents | pages [2] -->
2. Breaking Down the Problem---------------------------------------------------------------3

<!-- b000010 | contents | pages [2] -->
3. Assumptions-----------------------------------------------------------------------------------4

<!-- b000011 | contents | pages [2] -->
4. Nomenclatures--------------------------------------------------------------------------------5

<!-- b000012 | contents | pages [2] -->
5. Model One: Leaf Classification------------------------------------------------------------6

<!-- b000013 | contents | pages [2] -->
5.1 Decisive Parameters

<!-- b000014 | contents | pages [2] -->
5.2 Comparison

<!-- b000015 | contents | pages [2] -->
5.3 Model Testing

<!-- b000016 | contents | pages [2] -->
5.4 Conclusion

<!-- b000017 | contents | pages [2] -->
6. Model Two: Leaf Distribution and Leaf Shape--------------------------------------14

<!-- b000018 | contents | pages [2] -->
6.1 Introduction

<!-- b000019 | contents | pages [2] -->
6.2 Idealized Leaf Distribution Model

<!-- b000020 | contents | pages [2] -->
6.3 Analysis of Overlapping Areas

<!-- b000021 | contents | pages [2] -->
6.3.1

<!-- b000022 | contents | pages [2] -->
Solar Altitude Trending toward 90°

<!-- b000023 | contents | pages [2] -->
6.3.2

<!-- b000024 | contents | pages [2] -->
Solar Altitude Trending toward 0°

<!-- b000025 | contents | pages [2] -->
6.3.3

<!-- b000026 | contents | pages [2] -->
Solar Altitude within normal range

<!-- b000027 | contents | pages [2] -->
6.4 Model Testing

<!-- b000028 | contents | pages [2] -->
7. Model Three: Tree Profile and Leaf Shape-------------------------------------------19

<!-- b000029 | contents | pages [2] -->
7.1 Introduction

<!-- b000030 | contents | pages [2] -->
7.2 Hypothesis

<!-- b000031 | contents | pages [2] -->
7.3 Comparison of Leaf Shape and Tree Contour

<!-- b000032 | contents | pages [2] -->
7.4 Conclusion

<!-- b000033 | contents | pages [2] -->
8. Model Four: Leaf Mass--------------------------------------------------------------------27

<!-- b000034 | contents | pages [2] -->
8.1 Introduction

<!-- b000035 | contents | pages [2] -->
8.2 Leaf Mass and Tree Age

<!-- b000036 | contents | pages [2] -->
8.2.1

<!-- b000037 | contents | pages [2] -->
Leaf Mass and CO2 Sequestration

<!-- b000038 | contents | pages [2] -->
8.2.2

<!-- b000039 | contents | pages [2] -->
CO2 Sequestration and Tree Age

<!-- b000040 | contents | pages [2] -->
8.2.3

<!-- b000041 | contents | pages [2] -->
Leaf Mass and Tree Age

<!-- b000042 | contents | pages [2] -->
8.3 Tree Age and Tree Size

<!-- b000043 | contents | pages [2] -->
8.4 Leaf Mass and Tree Size

<!-- b000044 | contents | pages [2] -->
9. Strength and Weakness-------------------------------------------------------------------35

<!-- b000045 | contents | pages [2] -->
10. Reference--------------------------------------------------------------------------------------37

<!-- b000046 | contents | pages [2] -->
11. A Letter to the Science Journal Editor-------------------------------------------------38

<!-- b000047 | contents | pages [2] -->
12. Appendix--------------------------------------------------------------------------------------39

<!-- b000048 | contents | pages [2] -->
12.1 Chart of Tree Species and Growth Rate

<!-- b000049 | contents | pages [2] -->
12.2 MATLAB Program Code

<!-- b000050 | furniture | pages [3] -->
Team #14990

<!-- b000051 | furniture | pages [3] -->
3 / 42

<!-- b000052 | heading | pages [3] -->
1. Introduction

<!-- b000053 | prose | pages [3] -->
Leaf, which is responsible for photosynthesis and storage of food and water, is a very important organ of a plant. Leaf has so many different and interesting shapes and contours, which make it so catching and conspicuous in the plant kingdom. For centuries, people have always wondered why the leaf has so many splendid shapes. Is this just a gift from the Almighty God? Or is it the adjustment the leaf takes during its evolution and adaptation?

<!-- b000054 | prose | pages [3] -->
Another mystery of the leaf lies in the classification of different leaf types. Can we do so in a more reliable and scientific way instead of judging subjectively? We have tried our best to build a model on a quantitative base to increase the accuracy and efficiency of classifying different leaves.

<!-- b000055 | prose | pages [3] -->
The final mystery about the tree is how much the total leaf mass on a tree is. Just like people always want to figure out how much hair a person has, human beings always have a fancy to find out a solution from the seemingly infinity and incalculable.

<!-- b000056 | prose | pages [3] -->
We are deeply convinced that the true glamour of scientific and mathematical models is to unveil the intriguing and the changeable of the nature. Aiming to do so, we will generate models that can fit large quantities of data with highest accuracy within a quick flick.

<!-- b000057 | heading | pages [3] -->
2. Breaking Down the Problem

<!-- b000058 | prose | pages [3] -->
After carefully analyzing the problem, we conclude four main sub-problems to tackle in our paper:

<!-- b000059 | prose | pages [3] -->
1. Classification the different types of leaves

<!-- b000060 | prose | pages [3] -->
2. Relationship between the leaf distribution and leaf shape

<!-- b000061 | prose | pages [3] -->
3. Relationship between the tree profile and leaf shape

<!-- b000062 | prose | pages [3] -->
4. Calculation of the total leaf mass on a leaf

<!-- b000063 | prose | pages [3] -->
To tackle the first problem, we set a set of parameters to quantify the characters of the leaf shape and use the leaf shape as the main standard for our classification process.

<!-- b000064 | prose | pages [3, 4] -->
As for the second question, we want to use the overlapping area that one leaf casts on the leaf directly under it as a medium to associate the leaf distribution and leaf shape, since the leaf shape will affect the overlapping and we assume the leaf distribution will try to minimize the overlapping area.

<!-- b000065 | furniture | pages [4] -->
Team #14990

<!-- b000066 | furniture | pages [4] -->
4 / 42

<!-- b000068 | prose | pages [4] -->
As for the third question, we want to refer to the process we take when tackling the first problem and also set some parameters for the tree profile. After that, we will compare their parameters and judge whether there is a relation between tree profile and leaf shape.

<!-- b000069 | prose | pages [4] -->
To deal with the total mass of the leaves, we want to use the age to link the size of tree and the total weight of leaves of it because the tree size has an obvious relationship with its age and the age will affect a tree’s sequestration of carbon dioxide, which will reflect the weight of a tree’s total leaves.

<!-- b000070 | heading | pages [4] -->
3. Assumptions

<!-- b000071 | prose | pages [4] -->
1. The trees being studied are all individual (“open grown”) trees, such as trees typically planted along streets, in yards, and in parks. Our calculation does not apply to densely raised trees, as in typical reforestation projects where large numbers of trees are planted closely together. 2. Assume the shape of the leaves does not reflect special uses for the trees, such as to resist extremely windy, cold, parched, wet or dry conditions or to catch food. 3. Assume the type of the leaf distribution to be discussed (leaf length and internode distance relation) is only a reflection of the tree's natural tendency to sunlight. 4. Assume the tree profile we consider is the part above ground, including the trunk, the branches and leaves. 5. Assume all parts of leaf lay on a flat surface and the thickness or protrusion of veins are neglectable. 6. Assume leaves are the only part of the tree that reacts in photosynthesis and respiration so that the carbon dioxide sequestration of a tree is the sum of the sequestration of the leaves. 7. Assume the sequestration of a tree or a leaf is the net amount of CO2 fixed in a tree, which is the difference between the CO2 released in respiration and the CO2 absorbed in photosynthesis. 8. Assume the trees are in healthy, mature and stable condition. The trees of the same species have same characteristics.

<!-- b000072 | furniture | pages [5] -->
Team #14990

<!-- b000073 | furniture | pages [5] -->
5 / 42

<!-- b000074 | heading | pages [5] -->
4. Nomenclatures

<!-- b000075 | prose | pages [5] -->
𝑅 Rectangularity

<!-- b000076 | prose | pages [5] -->
𝐴𝑙𝑒𝑎𝑓 the area of leaf

<!-- b000077 | prose | pages [5] -->
𝐴𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒 the area of minimum bounding rectangle

<!-- b000078 | prose | pages [5] -->
𝐴𝑅 the aspect ratio

<!-- b000079 | prose | pages [5] -->
𝐿𝑠𝑕𝑜𝑟𝑡 the length of shorter side

<!-- b000080 | prose | pages [5] -->
𝐿𝑙𝑜𝑛𝑔 the length of longer side

<!-- b000081 | prose | pages [5] -->
𝐶 the circularity

<!-- b000082 | prose | pages [5] -->
𝑅𝑖𝑛 the radius of in-circle

<!-- b000083 | prose | pages [5] -->
𝑅𝑒𝑥 the radius of ex-circle

<!-- b000084 | prose | pages [5] -->
𝐹𝐹 Form factor

<!-- b000085 | prose | pages [5] -->
𝑃𝑙𝑒𝑎𝑓 the perimeter of leaf

<!-- b000086 | prose | pages [5] -->
𝐸𝑅𝐴𝐼 the edge regularity area index

<!-- b000087 | prose | pages [5] -->
𝐵𝑃𝐴 The bounding polygon area

<!-- b000088 | prose | pages [5] -->
𝐸𝑅𝑃𝐼 the edge regularity perimeter index

<!-- b000089 | prose | pages [5] -->
𝐵𝑃𝑃 the bounding polygon perimeter

<!-- b000090 | prose | pages [5] -->
𝑃𝐼𝑖 Proportional index

<!-- b000091 | prose | pages [5] -->
𝐼𝐷 the Index of Deviation

<!-- b000092 | prose | pages [5] -->
the length of major axis 𝐿𝑚𝑎𝑗𝑜𝑟

<!-- b000093 | prose | pages [5] -->
Aoverlapping the overlapping area

<!-- b000094 | prose | pages [5] -->
α the solar altitude

<!-- b000095 | prose | pages [5] -->
𝑀𝑙𝑒𝑎𝑓 the total mass of leaves on a tree

<!-- b000096 | prose | pages [5] -->
𝑀𝑐𝑎𝑟𝑏𝑜𝑛 𝑑𝑖𝑜𝑥𝑖𝑑𝑒 mass of carbon dioxide sequestered (lbs)

<!-- b000097 | prose | pages [5] -->
𝐴𝑠 ability to sequester carbon dioxide (lbs/g)

<!-- b000098 | prose | pages [5] -->
A the age of the tree

<!-- b000099 | furniture | pages [6] -->
Team #14990

<!-- b000100 | furniture | pages [6] -->
6 / 42

<!-- b000101 | heading | pages [6] -->
5. Model One: Leaf Classification

<!-- b000102 | heading | pages [6] -->
5.1 Decisive Parameters

<!-- b000103 | prose | pages [6] -->
In order to classify the shapes of the given leaf, we want to set a number of parameters and establish a database for comparison. After carefully and thoroughly analyzing the leaves, we develop seven most significant parameters as shown below:

<!-- b000104 | heading | pages [6] -->
1. Rectangularity

<!-- b000105 | prose | pages [6] -->
Firstly, we define the ratio of the area of the leaf to the Minimum Bounding Rectangle as the leaf’s Rectangularity, how much does the leaf resemble a rectangle (refer to figure 2.1). The maximum possible value of this parameter is 1.

<!-- b000106 | prose | pages [6] -->
𝐴𝑙𝑒𝑎𝑓 R = 𝐴𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒

<!-- b000107 | prose | pages [6] -->
𝐴𝑙𝑒𝑎𝑓 stands for the area of leaf

<!-- b000108 | prose | pages [6] -->
𝐴𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒 stands for the area of minimum bounding rectangle

<!-- b000109 | heading | pages [6] -->
2. Aspect ratio

<!-- b000110 | prose | pages [6] -->
After defining the rectangularity, now we define the Aspect Ratio, which describes the proportional relationship between the width of and height of a leaf’s Minimum Bounding Rectangle, as another key character to classify general shape of a leaf. The bigger this ratio is, the more this leaf resembles a square (refer to

<!-- b000111 | caption | pages [6] -->
figure 2.1). The maximum possible value of this

<!-- b000112 | prose | pages [6] -->
parameter is 1.

<!-- b000113 | prose | pages [6] -->
𝐿𝑠𝑕𝑜𝑟𝑡 AR = 𝐿long

<!-- b000114 | caption | pages [6] -->
Figure 2.1

<!-- b000115 | prose | pages [6] -->
Where

<!-- b000116 | prose | pages [6, 7] -->
AR stands for the aspect ratio 𝐿𝑠𝑕𝑜𝑟𝑡 stands for the length of shorter side

<!-- b000117 | furniture | pages [7] -->
Team #14990

<!-- b000118 | furniture | pages [7] -->
7 / 42

<!-- b000120 | prose | pages [7] -->
𝐿long stands for the length of longer side

<!-- b000121 | heading | pages [7] -->
3. Circularity

<!-- b000122 | prose | pages [7] -->
To evaluate how roundish a leaf is, we

<!-- b000123 | prose | pages [7] -->
consider that the respective radius of

<!-- b000124 | prose | pages [7] -->
in-circle and ex-circle. The ratio of the

<!-- b000125 | prose | pages [7] -->
former to the latter, which we define as

<!-- b000126 | prose | pages [7] -->
Circularity, may well reflect this

<!-- b000127 | prose | pages [7] -->
characteristic. The greater the ratio of

<!-- b000128 | prose | pages [7] -->
Circularity is, the closer the leaf is to a

<!-- b000129 | prose | pages [7] -->
circle, (refer to figure 2.2) The

<!-- b000130 | prose | pages [7] -->
maximum possible value of this

<!-- b000131 | prose | pages [7] -->
parameter is 1.

<!-- b000132 | caption | pages [7] -->
Figure 2.2

<!-- b000133 | prose | pages [7] -->
C = 𝑅𝑖𝑛 𝑅𝑒𝑥

<!-- b000134 | prose | pages [7] -->
Where

<!-- b000135 | prose | pages [7] -->
C stands for the circularity

<!-- b000136 | prose | pages [7] -->
𝑅𝑖𝑛 stands for the radius of in-circle

<!-- b000137 | prose | pages [7] -->
𝑅𝑒𝑥 stands for the radius of ex-circle

<!-- b000138 | heading | pages [7] -->
4. Form factor

<!-- b000139 | prose | pages [7] -->
Form Factor, a famous shape description parameter, is another essential

<!-- b000140 | prose | pages [7] -->
indicator of leaf classification. The maximum possible value of this

<!-- b000141 | prose | pages [7] -->
parameter is 1.

<!-- b000142 | prose | pages [7] -->
FF = 4𝜋𝐴𝑙𝑒𝑎𝑓 2 𝑃𝑙𝑒𝑎𝑓

<!-- b000143 | prose | pages [7] -->
Where

<!-- b000144 | prose | pages [7] -->
𝑃𝑙𝑒𝑎𝑓 stands for the perimeter of leaf

<!-- b000145 | furniture | pages [8] -->
Team #14990

<!-- b000146 | furniture | pages [8] -->
8 / 42

<!-- b000147 | heading | pages [8] -->
5. Edge regularity area index.

<!-- b000148 | prose | pages [8] -->
Although the aspect ratio and the rectangularity of two leaves may resemble, the contour or the exact shape of two leaves may vary much.

<!-- b000149 | prose | pages [8] -->
Thus, In order to take the different contour of the leaf into consideration, we join every convex dot along the contour and develop a specific parameter, which we call Bounding Polygon Area. The ratio between the leaf area and this bounding polygon area is a good quantitative factor, defined as Edge Regularity Area Index.

<!-- b000150 | prose | pages [8] -->
The more this ratio is close to 1, the less jagged and the smoother this leaf’s contour is (refer to

<!-- b000151 | caption | pages [8] -->
figure 2.3). The maximum possible value of this

<!-- b000152 | prose | pages [8] -->
parameter is 1.

<!-- b000153 | prose | pages [8] -->
ERAI = 𝐴𝑙𝑒𝑎𝑓 𝐵𝑃𝐴

<!-- b000154 | prose | pages [8] -->
Where

<!-- b000155 | caption | pages [8] -->
Figure 2.3

<!-- b000156 | prose | pages [8] -->
ERAI stands for the edge regularity area index

<!-- b000157 | prose | pages [8] -->
𝐵𝑃𝐴 stands for bounding polygon area

<!-- b000158 | heading | pages [8] -->
6. Edge regularity perimeter index

<!-- b000159 | prose | pages [8] -->
Similarly, we develop another parameter: Bounding Polygon Perimeter, the perimeter of the polygon when we join the convex dots of a leaf. We define the ratio of the convex dot perimeter and the perimeter of the leaf as Edge Regularity Perimeter Index. This time, the smaller this ratio is, the more jagged and irregular the contour of the leaf is (refer to figure 2.4). The maximum possible value of this parameter is 1.

<!-- b000160 | prose | pages [8, 9] -->
ERPI = 𝐵𝑃𝑃 𝑃𝑙𝑒𝑎𝑓 Where

<!-- b000161 | furniture | pages [9] -->
Team #14990

<!-- b000162 | furniture | pages [9] -->
9 / 42

<!-- b000164 | prose | pages [9] -->
ERPI stands for the edge regularity perimeter

<!-- b000165 | prose | pages [9] -->
index

<!-- b000166 | prose | pages [9] -->
𝐵𝑃𝑃 stands for the bounding polygon perimeter

<!-- b000167 | heading | pages [9] -->
7. Proportional index

<!-- b000168 | prose | pages [9] -->
Since it is also highly critical to capture the spatial

<!-- b000169 | prose | pages [9] -->
distribution of different portions of a leaf along its

<!-- b000170 | prose | pages [9] -->
vertical axis, we divide the minimum bounding

<!-- b000171 | prose | pages [9] -->
rectangle into four blocks horizontally, and

<!-- b000172 | prose | pages [9] -->
calculate the proportion of the leaf area in a

<!-- b000173 | prose | pages [9] -->
particular region to the total leaf, which we refer

<!-- b000174 | prose | pages [9] -->
to as the Proportional Index.

<!-- b000175 | caption | pages [9] -->
Figure 2.4

<!-- b000176 | prose | pages [9] -->
𝑃𝐼𝑖= 𝑎𝑟𝑒𝑎 𝑜𝑓 𝑏𝑙𝑜𝑐𝑘 𝑖 𝐴𝑙𝑒𝑎𝑓

<!-- b000177 | prose | pages [9] -->
Now, we can develop a database of six most common leaves containing

<!-- b000178 | prose | pages [9] -->
seven parameters discussed above.

<!-- b000179 | prose | pages [9] -->
These are six most commonly seen leaf types in North America:

<!-- b000180 | prose | pages [9] -->
Database:

<!-- b000181 | prose | pages [9] -->
1 2 3 4 5 6

<!-- b000182 | prose | pages [9] -->
Rectangularity 0.6627 0.5902 0.6250 0.4772 0.4876 0.6576

<!-- b000183 | prose | pages [9] -->
Aspect Ratio 0.8615 0.6600 0.1800 0.6383 0.4792 0.3111

<!-- b000184 | prose | pages [9, 10] -->
Circularity 0.8140 0.5432 0.4564 0.3454 0.3123 0.3311 Form Factor 0.9139 0.6206 0.2823 0.2470 0.3662 0.4956 ER Area Index 0.9322 0.8780 0.9091 0.8500 0.7880 0.8895

<!-- b000185 | furniture | pages [10] -->
Team #14990

<!-- b000186 | furniture | pages [10] -->
10 / 42

<!-- b000188 | prose | pages [10] -->
ER Perimeter Index 0.8727 0.8889 0.9384 0.8602 0.8231 0.9903 PI1 0.0649 0.0769 0.1179 0.1909 0.1299 0.2920 PI2 0.2958 0.3555 0.2208 0.3892 0.3606 0.4187 PI3 0.3439 0.4243 0.4139 0.3047 0.4123 0.2677 PI4 0.2954 0.1433 0.2474 0.1152 0.0970 0.0220

<!-- b000189 | heading | pages [10] -->
5.2 Comparison

<!-- b000190 | prose | pages [10] -->
When given a specific leaf, we can calculate seven characteristics of it and compare them with our database by calculating the squared deviation of each of parameter of the given leaf from the corresponding standard parameter of each category. We realize the fact that some of seven parameters are somehow more important than others. So in an effort to make our model more accurate and reliable, we induce the conception of the Index of Deviation, denoted as 𝑰𝑫, which comes from the sum of the squared deviation between the database and the leaf –to–be–classified times the proper weight.

<!-- b000191 | prose | pages [10] -->
7 𝐼𝐷= 𝐼𝑖∙𝑊𝑖 𝑖=1

<!-- b000192 | prose | pages [10] -->
(𝐑𝐧𝐞𝐰−𝐑)𝟐 𝐈𝟏

<!-- b000193 | prose | pages [10] -->
(𝐀𝐑𝐧𝐞𝐰−𝐀𝐑)𝟐 𝐈𝟐

<!-- b000194 | prose | pages [10] -->
(𝐂𝐧𝐞𝐰−𝐂)𝟐 𝐈𝟑

<!-- b000195 | prose | pages [10] -->
(𝐅𝐅𝐧𝐞𝐰−𝐅𝐅)𝟐 𝐈𝟒

<!-- b000196 | prose | pages [10, 11] -->
(𝐄𝐑𝐀𝐈𝐧𝐞𝐰−𝐄𝐑𝐀𝐈)𝟐 𝐈𝟓 (𝐄𝐑𝐏𝐈𝐧𝐞𝐰−𝐄𝐑𝐏𝐈)𝟐 𝐈𝟔

<!-- b000197 | furniture | pages [11] -->
Team #14990

<!-- b000198 | furniture | pages [11] -->
11 / 42

<!-- b000200 | prose | pages [11] -->
4 1 4 ∙ (𝑃𝐼𝑖𝑛𝑒𝑤−𝑃𝐼𝑖)2 𝐼7 𝑖=1

<!-- b000201 | prose | pages [11] -->
In order to decide the respective weight more scientifically, we resort to the help

<!-- b000202 | prose | pages [11] -->
of Analytical Hierarchy Process.

<!-- b000203 | prose | pages [11] -->
AHP

<!-- b000204 | prose | pages [11] -->
First of all, we build a seven by seven matrix reciprocal matrix by pair

<!-- b000205 | prose | pages [11] -->
comparison:

<!-- b000206 | prose | pages [11] -->
R AR

<!-- b000207 | heading | pages [11] -->
C FF

<!-- b000208 | prose | pages [11] -->
ERAI ERPI PI

<!-- b000209 | prose | pages [11] -->
Rectangularity 1 1/3 1 1/4 1/2 1/2 1/7

<!-- b000210 | prose | pages [11] -->
Aspect Ratio 3 1 3 1 2 2 1/3

<!-- b000211 | prose | pages [11] -->
Circularity 1 1/3 1 1/4 1/2 1/2 1/7

<!-- b000212 | prose | pages [11] -->
Form Factor 4 1 4 1 3 3 1/2

<!-- b000213 | prose | pages [11] -->
ER Area Index 2 1/2 2 1/3 1 1 1/4

<!-- b000214 | prose | pages [11] -->
ER Perimeter Index 2 1/2 2 1/3 1 1 1/4

<!-- b000215 | prose | pages [11] -->
Proportional Index 7 3 7 2 4 4 1

<!-- b000216 | prose | pages [11] -->
*The number of each cell is explained in the following chart:

<!-- b000217 | prose | pages [11] -->
Intensity of Value Interpretation

<!-- b000218 | prose | pages [11] -->
1 Requirements i and j are of equal value.

<!-- b000219 | prose | pages [11] -->
3 Requirement i has a slightly higher value than j.

<!-- b000220 | prose | pages [11] -->
5 Requirement i has a strongly higher value than j.

<!-- b000221 | prose | pages [11] -->
7 Requirement i has a very strongly higher value than j.

<!-- b000222 | prose | pages [11] -->
9 Requirement i has an absolutely higher value than j.

<!-- b000223 | prose | pages [11] -->
2, 4, 6, 8 These are intermediate scales between two adjacent judgments.

<!-- b000224 | prose | pages [11] -->
Reciprocals If Requirement i has a lower value than j

<!-- b000225 | prose | pages [11] -->
We then input Pair Ratio Matrix into computer program of MATLAB (Code available in appendix), and get the weight of each factor (Wi).

<!-- b000226 | furniture | pages [12] -->
Team #14990

<!-- b000227 | furniture | pages [12] -->
12 / 42

<!-- b000228 | prose | pages [12] -->
W1 0.0480

<!-- b000229 | prose | pages [12] -->
W2 0.1583

<!-- b000230 | prose | pages [12] -->
W3 0.0480

<!-- b000231 | prose | pages [12] -->
W4 0.2048

<!-- b000232 | prose | pages [12] -->
W5 0.0855

<!-- b000233 | prose | pages [12] -->
W6 0.0855

<!-- b000234 | prose | pages [12] -->
W7 0.3701

<!-- b000235 | prose | pages [12] -->
The following calculation is intended to test the consistency of the above AHP.

<!-- b000236 | prose | pages [12] -->
λmax = 7.0512

<!-- b000237 | prose | pages [12] -->
CI = λmax −n = 0.0087 n −1

<!-- b000238 | prose | pages [12] -->
CR = CI RI = 0.0064

<!-- b000239 | prose | pages [12] -->
CR < 0.01

<!-- b000240 | prose | pages [12] -->
So, the above method displays perfectly acceptable consistency and the weights

<!-- b000241 | prose | pages [12] -->
are reasonable.

<!-- b000242 | heading | pages [12] -->
5.3 Model Testing

<!-- b000243 | prose | pages [12] -->
Now we will take the maple leaf as an example to test

<!-- b000244 | prose | pages [12] -->
our leaf classification model. Before testing, we compare

<!-- b000245 | prose | pages [12] -->
this maple leaf with the six categories in our database

<!-- b000246 | prose | pages [12] -->
and find out that it resembles Category 4 most. Now we

<!-- b000247 | prose | pages [12, 13] -->
will test our hypothesis with our model based on quantitative analysis.

<!-- b000248 | furniture | pages [13] -->
Team #14990

<!-- b000249 | furniture | pages [13] -->
13 / 42

<!-- b000251 | prose | pages [13] -->
Firstly, process the image of a given maple leaf:

<!-- b000252 | prose | pages [13] -->
Then, calculate the rectangularity, aspect ratio, circularity, form factor, edge

<!-- b000253 | prose | pages [13] -->
regularity area index, edge regularity perimeter index and the proportional index

<!-- b000254 | prose | pages [13] -->
of the given leaf. In this case, the seven parameters are shown below:

<!-- b000255 | prose | pages [13] -->
Parameter Maple Leave

<!-- b000256 | prose | pages [13] -->
Rectangularity 0.3554

<!-- b000257 | prose | pages [13] -->
Aspect Ratio 0.9079

<!-- b000258 | prose | pages [13] -->
Circularity 0.2691

<!-- b000259 | prose | pages [13] -->
Form Factor 0.1572

<!-- b000260 | prose | pages [13] -->
ER Area Index 0.6248

<!-- b000261 | prose | pages [13] -->
ER Perimeter Index 0.3787 PI1 0.0968 PI2 0.4628 PI3 0.4311 PI4 0.0093

<!-- b000262 | prose | pages [13] -->
Finally, calculate the index of deviation by using the formula generated before.

<!-- b000263 | prose | pages [13] -->
7 𝐼𝑖∙𝑊𝑖 𝑖=1

<!-- b000264 | prose | pages [13] -->
The six indexes of deviation after comparing the parameters of a given maple leaf

<!-- b000265 | prose | pages [13] -->
with the parameters of six categories in our database are shown below:

<!-- b000266 | prose | pages [13, 14] -->
Maple Leave 1 2 3 4 5 6 I1 0.0045 0.0026 0.0035 0.0007 0.0008 0.0044 I2 0.0003 0.0097 0.0839 0.0115 0.0291 0.0564 I3 0.0066 0.0043 0.0004 0.0001 0.0004 0.0000 I4 0.1173 0.0440 0.0032 0.0017 0.0090 0.0235 I5 0.0081 0.0055 0.0069 0.0043 0.0023 0.0060 I6 0.0209 0.0223 0.0268 0.0198 0.0169 0.0320 I7 0.1095 0.0277 0.1073 0.0384 0.1817 0.0619 𝐈𝑫 0.2672 0.1161 0.2319 0.0765 0.2402 0.1841 Since the index of deviation between the given maple leaf and Category 4 is smallest, the maple leaf falls into Category 4, which is consistent with our hypothesis.

<!-- b000267 | furniture | pages [14] -->
Team #14990

<!-- b000268 | furniture | pages [14] -->
14 / 42

<!-- b000270 | heading | pages [14] -->
5.4 Conclusion

<!-- b000271 | prose | pages [14] -->
So far, our model has solved the problem of classification very well based on seven well-rounded parameters and a functional database. Through this quantitative model, we can decide the general shape of any given leaf reliably and scientifically. Our model is robust under reasonable conditions, which can be seen through the testing part discussed above. However, since our database contains only the six commonly seen leaf types in North America, the variety of database itself still has room for improvement. With the more and more different leaf species added to the database, our model can apply to a wider and more geographically comprehensive scope.

<!-- b000272 | heading | pages [14] -->
6. Model Two: Leaf Distribution and Leaf Shape

<!-- b000273 | heading | pages [14] -->
6.1 Introduction

<!-- b000274 | prose | pages [14] -->
Leaf shape varies so greatly that it still remains a mystery why leaves display such a immense variety of shape. Leaf veins are the skeleton of a leaf, and ground tissues the muscles. Genetic and environmental factors contribute to the different patterns of leaf veins and ground tissue, thereby determining the leaf shape. In this model, we narrow the big picture into how leaf distribution act as an influence on leaf shape.

<!-- b000275 | heading | pages [14] -->
6.2 Idealized Leaf Distribution Model

<!-- b000276 | prose | pages [14] -->
To downplay the effects of miscellaneous factors that contribute to the relation between the distribution and shape of a leaf, we construct an idealized model that immensely simplifies the complex condition.

<!-- b000277 | prose | pages [14] -->
The tree is made up of a branch perpendicular to the ground surface and two identical leaves grown on the branch ipsilaterally and horizontally. The leaves face upward and point toward the sun in the sky.

<!-- b000278 | furniture | pages [15] -->
Team #14990

<!-- b000279 | furniture | pages [15] -->
15 / 42

<!-- b000280 | prose | pages [15] -->
We suppose the tree is placed on the latitude of L (Northern). So the greatest

<!-- b000281 | prose | pages [15] -->
average solar altitude in a year, which is attained in the noon of Vernal Equinox, is defined as α.

<!-- b000282 | prose | pages [15] -->
The above information is explained in the following image:

<!-- b000283 | heading | pages [15] -->
6.3 Analysis of Overlapping Areas

<!-- b000284 | prose | pages [15] -->
Our key focus of the study is the partly shaded leaf. What proportion of the leaf (PL) is shaded is the output of the model. The solar attitude α is a critical control variable. According to the influence of the angle on PL, we divide α into three

<!-- b000285 | prose | pages [15] -->
scenarios.

<!-- b000286 | prose | pages [15] -->
6.3.1 Solar Altitude trending toward 90°

<!-- b000287 | prose | pages [15] -->
The situation in which α is trending toward 90°usually takes place in tropical

<!-- b000288 | prose | pages [15] -->
regions. And it is very clear through observation that, in tropical regions, leaf

<!-- b000289 | prose | pages [15] -->
shapes are typically broad and wide with the tree crowns usually containing only

<!-- b000290 | prose | pages [15, 16] -->
one layer of leaves. This can be explained through the illustration above as the shaded part of the lower leaf would be too big with α trending toward 90°to supply enough solar energy for photosynthesis and the biggest absorption of energy can be achieved by a broad leaf shape.

<!-- b000291 | furniture | pages [16] -->
Team #14990

<!-- b000292 | furniture | pages [16] -->
16 / 42

<!-- b000294 | prose | pages [16] -->
6.3.2 Solar Altitude trending toward 0°

<!-- b000295 | prose | pages [16] -->
The situation in which α is trending toward 0°usually takes place in frigid zones. It is also very clear that in these regions, leaves are typically acicular with the tree crowns containing dense layers of closely grown leaves. This can also be explained through the illustration above as the shaded part of the lower leaf would approach zero with α trending toward 0°, allowing a much more concentrated distribution of leaves than in other situations. In addition, the maximum absorption of energy can be best achieved by needle-like leaves.

<!-- b000296 | prose | pages [16] -->
6.3.3 Solar Altitude within normal range

<!-- b000297 | prose | pages [16] -->
This scenario is typical in the temperate zone on earth, where sunlight irradiates the leaves in a tilted way. It is also the case in which our idealized model is the most suitable. Another crucial factor that we control in this case is the distance (h) between the two points connecting the leaves and the branch.

<!-- b000298 | prose | pages [16] -->
Our aim is to discuss the relationship between the leaf shape and the leaf distribution. We assume a tree’s leaf distribution will try to minimize the overlapping area between leaves, so our model will try to find out the quantitative relationship between the overlapping area and the shape of leaf.

<!-- b000299 | prose | pages [16] -->
In order to simplify the model, we use the rhombus, with the length of major axis denoted as Lmajor and the length of minor axis denoted as Lminor , to replace the leaf shape. Also, we control the area of the first leaf to ensure its constant exposure area to the sun. Since the area is fixed, now we only need to change the length of the major axis to change the shape of the leaf. In other words, during our later study, we will use the change of Lmajor to symbolize the change of the leaf shape.

<!-- b000300 | furniture | pages [17] -->
Team #14990

<!-- b000301 | furniture | pages [17] -->
17 / 42

<!-- b000302 | prose | pages [17] -->
Also, since we have fixed the area of the leaf and just change its shape during our study, the smallest overlapping area, which we denote as  Aoverlapping , means the smallest ration of E, which is defined as follows:

<!-- b000303 | prose | pages [17] -->
Aoverlapping E = area of one leaf

<!-- b000304 | prose | pages [17] -->
Obviously, the most efficient and effective way for two leaves to distribute is to be just totally exposed in sunlight as illustrated below, when h=h0 and E=0. Thus, the tree can take whatever shape it wants since we control the leaf’s surface

<!-- b000305 | prose | pages [17] -->
area.

<!-- b000306 | prose | pages [17, 18] -->
h0 Now, we want to study what if h<h0 .

<!-- b000307 | furniture | pages [18] -->
Team #14990

<!-- b000308 | furniture | pages [18] -->
18 / 42

<!-- b000310 | prose | pages [18] -->
If h< h0, there will be a shaded region  Aoverlapping .  The stress of the following study is analyzing the relation between h, Lmajor and E when given a fixed solar altitude α.

<!-- b000311 | prose | pages [18] -->
We can easily give the relationship between these factors according to their

<!-- b000312 | prose | pages [18] -->
geometric features:

<!-- b000313 | prose | pages [18] -->
Lmajor ∙tanα −h )2 E = ( L ∙tanα

<!-- b000314 | prose | pages [18] -->
h Lmajor ∙tan α)2 Namely                    E = (1 −

<!-- b000315 | prose | pages [18] -->
Where tanα is a constant.

<!-- b000316 | prose | pages [18] -->
When we fix the value of h and give α a particular value, we can get the

<!-- b000317 | prose | pages [18] -->
relationship between the length of leaf and the overlapping area:

<!-- b000318 | furniture | pages [19] -->
Team #14990

<!-- b000319 | furniture | pages [19] -->
19 / 42

<!-- b000320 | prose | pages [19] -->
*x-axis refers to Lmajor

<!-- b000321 | prose | pages [19] -->
y-axis refers to  Aoverlapping

<!-- b000322 | prose | pages [19] -->
We discover from the function above that the closer the  Lmajor approaches L ∙ tanα, which is equal to h0, the smaller the overlapping area will be.

<!-- b000323 | prose | pages [19] -->
So far, we have considered the both situations when h=h0 and h<h0. From what we discussed above, the best leaf distribution of the leaf occurs when h=h0, which means

<!-- b000324 | prose | pages [19] -->
h = Lmajor ∙tanα

<!-- b000325 | prose | pages [19] -->
6.4

<!-- b000326 | heading | pages [19] -->
Model Testing

<!-- b000327 | prose | pages [19] -->
Now, we need to test whether this correlation between the leaf distribution and leaf shape is right.  We collect the data of the length (Lmajor ) and internode (h) of a variety of trees and use our formula to calculate the respective solar altitude

<!-- b000328 | prose | pages [19] -->
of the trees. By converting the solar altitude into latitude, we can predict the

<!-- b000329 | prose | pages [19] -->
origin of this particular tree.  We choose   Ligustrum quihoui Carr, Osmanthus

<!-- b000330 | prose | pages [19] -->
fragrans and Camellia japonica as our test objects and here is the result of our

<!-- b000331 | prose | pages [19] -->
testing:

<!-- b000332 | prose | pages [19] -->
Lmajor tanα Test Object h Predicted Latitude True Lattitude Ligustrum quihoui Carr. 2 2.5 1.25 38.65 35~35 Osmanthus fragrans 10 18.5 1.85 28.39 23~29 Camellia japonica 6 9 1.50 33.69 32~36

<!-- b000333 | prose | pages [19] -->
From the table, we can see that our predicted latitude of origin is always within the range of its true latitude, so it is safe to say that the correlation between leaf distribution and leaf shape generated by our model is reliable and correct. In other words, there does exist a relationship between the leaf distribution and leaf shape.

<!-- b000334 | heading | pages [19] -->
7. Model Three: Tree Profile and Leaf Shape

<!-- b000335 | heading | pages [19] -->
7.1 Introduction

<!-- b000336 | prose | pages [19] -->
In this part of our paper, we will explore the correlation between the tree profile

<!-- b000337 | prose | pages [19] -->
and the leaf shape. When we classify the leaf in model one, we define a set of

<!-- b000338 | prose | pages [19] -->
parameters to better understand the shape of leaf on a quantitative base.

<!-- b000339 | furniture | pages [20] -->
Team #14990

<!-- b000340 | furniture | pages [20] -->
20 / 42

<!-- b000341 | prose | pages [20] -->
Similarly, we will apply this method to explore the profile of tree.

<!-- b000342 | heading | pages [20] -->
7.2 Hypothesis

<!-- b000343 | prose | pages [20] -->
Since the vein structure determines the leaf shape and the branch structure determines the tree profile and, to some degree, the leaf veins resemble the branches（refer to figure 3.1）,we have a wild hypothesis that, leaf shape be a two-dimensional mimic of the tree profile. In other words, there does exist a correlation between the leaf shape and the tree profile.

<!-- b000344 | heading | pages [20] -->
7.3 Comparison of Leaf Shape and Tree Contour

<!-- b000345 | prose | pages [20] -->
In an effort to judge whether our hypothesis is true or not, our model’s general idea is to compare some specific parameters between the tree profile and the leaf shape, thus determine whether a relation exists.

<!-- b000346 | prose | pages [20] -->
The leaf shape is two-dimensional, so it is relatively easy to study its parameters.

<!-- b000347 | prose | pages [20] -->
However, the tree profile is three dimensional, so it is important to find out a two-dimensional characteristic of a tree to study its parameters. Since the longitudinal section of a particular tree reflects the general size characteristics of a grown tree, we choose to focus on it in our later study and analysis.

<!-- b000348 | prose | pages [20, 21] -->
7.3.1 Tree Profile Classification In the leaf classification model, there are 6 general classes of leaves.

<!-- b000349 | furniture | pages [21] -->
Team #14990

<!-- b000350 | furniture | pages [21] -->
21 / 42

<!-- b000352 | prose | pages [21] -->
Since we only compare the general resemblance between leaf and tree,

<!-- b000353 | prose | pages [21] -->
class five (elliptic leaf with serrated margin) is incorporated into class two.

<!-- b000354 | prose | pages [21] -->
As a result, we get 5 classes of leaves and 5 respective types of trees.

<!-- b000355 | prose | pages [21] -->
Class 1 Cordate (Texas Redbud):

<!-- b000356 | prose | pages [21] -->
Class 2 Elliptic (Camphor Tree):

<!-- b000357 | furniture | pages [22] -->
Team #14990

<!-- b000358 | furniture | pages [22] -->
22 / 42

<!-- b000359 | prose | pages [22] -->
Class 3 Subulate (Pine Tree)：

<!-- b000360 | prose | pages [22, 23] -->
Class 4 Palmate (Oak Tree)： Class 5 Obovate (Mockernut Hickory)：

<!-- b000361 | furniture | pages [23] -->
Team #14990

<!-- b000362 | furniture | pages [23] -->
23 / 42

<!-- b000364 | prose | pages [23] -->
7.3.2 Parameters of the tree

<!-- b000365 | prose | pages [23] -->
According to the data we get and referring to the parameters we set for the leaf, this time we appoint 3 parameters for the longitudinal section that can be compared with those of the leaf shape, namely the rectangularity, the aspect ratio and circularity. Since we have discussed these three parameters in detail before, we will just briefly go through them.

<!-- b000366 | prose | pages [23] -->
A. Rectangularity

<!-- b000367 | prose | pages [23] -->
Rectangularity is defined as the ratio between the longitudinal section area of a tree and the area of the smallest bounding rectangle area.

<!-- b000368 | prose | pages [23] -->
First we compare the rectangularity of the tree profile with that of leaf we calculated in model 1 in the following chart.

<!-- b000369 | prose | pages [23, 24] -->
Class Leaf Tree 1 0.6627 0.6281 2 0.5902 0.6846 3 0.6250 0.5180 4 0.4772 0.5292 5 0.6576 0.6238 Second, we draw a scatter plot with the independent variable of leaf and

<!-- b000370 | furniture | pages [24] -->
Team #14990

<!-- b000371 | furniture | pages [24] -->
24 / 42

<!-- b000373 | prose | pages [24] -->
the dependent variable of tree and use MATLAB to construct the linear

<!-- b000374 | prose | pages [24] -->
regression of the data. The following plot shows the fitting relationship

<!-- b000375 | prose | pages [24] -->
of the data.

<!-- b000376 | prose | pages [24] -->
Y = 0.3905x + 0.3614

<!-- b000377 | prose | pages [24] -->
Also, we use F-test to test the significance of the linear regression:

<!-- b000378 | prose | pages [24] -->
r^2=0.1783

<!-- b000379 | prose | pages [24] -->
F=0.63

<!-- b000380 | prose | pages [24] -->
P=0.4850

<!-- b000381 | prose | pages [24] -->
Obviously, the test shows that the linear relationship between the

<!-- b000382 | prose | pages [24] -->
rectangularity of leaf and rectangularity of tree is insignificant.

<!-- b000383 | prose | pages [24] -->
B. Aspect ratio

<!-- b000384 | prose | pages [24] -->
Aspect ratio is defined as the ration between the short side and the long

<!-- b000385 | prose | pages [24] -->
side of the smallest bounding rectangle area.

<!-- b000386 | prose | pages [24] -->
The comparison chart is shown below.

<!-- b000387 | furniture | pages [25] -->
Team #14990

<!-- b000388 | furniture | pages [25] -->
25 / 42

<!-- b000389 | prose | pages [25] -->
Class Leaf Tree

<!-- b000390 | prose | pages [25] -->
1 0.8615 0.7914

<!-- b000391 | prose | pages [25] -->
2 0.6600 0.7243

<!-- b000392 | prose | pages [25] -->
3 0.1800 0.6601

<!-- b000393 | prose | pages [25] -->
4 0.6383 0.7980

<!-- b000394 | prose | pages [25] -->
5 0.3111 0.6750

<!-- b000395 | prose | pages [25] -->
Using the same statistical method, we construct the following plot.

<!-- b000396 | prose | pages [25] -->
Y = 0.2055x + 0.6208

<!-- b000397 | prose | pages [25] -->
This time the result of statistical inference is as follows:

<!-- b000398 | prose | pages [25] -->
r^2=0.7985

<!-- b000399 | prose | pages [25] -->
F=11.8857

<!-- b000400 | prose | pages [25] -->
P=0.041<0.05

<!-- b000401 | prose | pages [25] -->
As P value is within acceptance range, the linear relationship between

<!-- b000402 | prose | pages [25] -->
Aspect Ratio of leaf and that of tree.

<!-- b000403 | furniture | pages [26] -->
Team #14990

<!-- b000404 | furniture | pages [26] -->
26 / 42

<!-- b000405 | prose | pages [26] -->
C. Circularity

<!-- b000406 | prose | pages [26] -->
Circularity is defined as the ratio between the radius of in-circle and

<!-- b000407 | prose | pages [26] -->
ex-circle of the area of interest.

<!-- b000408 | prose | pages [26] -->
Class Leaf Tree 1 0.6396  0.5800 2 0.5698  0.5928 3 0.1834  0.2895 4 0.3069  0.4070 5 0.2889  0.3866

<!-- b000409 | prose | pages [26] -->
Using Matlab, we construct the following plot.

<!-- b000410 | prose | pages [26] -->
Y= 0.6567x + 0.1900

<!-- b000411 | prose | pages [26] -->
The F-test shows the following.

<!-- b000412 | prose | pages [26] -->
r^2=0.9645

<!-- b000413 | prose | pages [26] -->
F=81.5595

<!-- b000414 | prose | pages [26] -->
P=0.0029<0.05

<!-- b000415 | prose | pages [26] -->
The P value small enough for us to say that there exists a linear

<!-- b000416 | prose | pages [26] -->
relationship between the circularity of the tree and the leaf.

<!-- b000417 | furniture | pages [27] -->
Team #14990

<!-- b000418 | furniture | pages [27] -->
27 / 42

<!-- b000419 | heading | pages [27] -->
7.4 Conclusion

<!-- b000420 | prose | pages [27] -->
From the test of the above three parameters, we may conclude that leaf shape and tree profile have a possibly relationship between each other. Although the test of rectangularity does not support our hypothesis, the test of aspect ratio and the test of circularity well corroborate the theory that leaf shape is a two-dimensional mimic of the tree contour. Since, the tree shape and leaf shape both are affected by an great deal of genetic and environmental factors, the shape characteristics of tree may not well reflect the tree shape. But as far as we know, the shape of leaf resembles the shape of tree to some extent.

<!-- b000421 | heading | pages [27] -->
8. Model Four: Leaf Mass

<!-- b000422 | heading | pages [27] -->
8.1 Introduction

<!-- b000423 | prose | pages [27] -->
In order to estimate the mass of the leaves of a certain tree when given the size characteristics, we have developed a model based on a database.

<!-- b000424 | prose | pages [27] -->
One simple way to calculate the total leaf mass of a tree is to simply multiply the number of the leaves on a tree and the mass of a single leaf. Our method is more accurate and less demanding in that our model is independent of these two factors, namely the number of leaves and the net weight of one single leaf, but dependent on one more reliable factor of a grown tree --- photosynthesis.

<!-- b000425 | prose | pages [27] -->
Our methodology of estimating the leave mass of a tree is based on three variables: tree age and growth rate, which is determined by tree species, and general type (Hardwood or conifer). In other words, given the age and type of a tree, we are able to estimate the total mass of leaves. In this model, CO2 is used as a calculating media.

<!-- b000426 | prose | pages [27] -->
After the explanation of the model, we try to study if there is a correlation between leaf mass size characteristics of a tree. The answer is positive, which we use tree age as a link to prove.

<!-- b000427 | heading | pages [27] -->
8.2 Leaf Mass and Tree Age

<!-- b000428 | prose | pages [27] -->
8.2.1 Leaf Mass and CO2 Sequestration First of all, according to the information we acquired from the past researches, we divide the tree into two main types based on their different ability of sequestering carbon dioxide from the atmosphere.

<!-- b000429 | furniture | pages [28] -->
Team #14990

<!-- b000430 | furniture | pages [28] -->
28 / 42

<!-- b000431 | prose | pages [28] -->
These two types and their respective ability are shown below:

<!-- b000432 | prose | pages [28] -->
Hardwood Conifer Ability to sequester Carbon 0.00250 0.00165 Dioxide  ( lbs of CO2/g of leaf)

<!-- b000433 | prose | pages [28] -->
**A tree’s ability to sequester the carbon dioxide is different from its ability to absorb it since the tree also releases CO2 into the atmosphere all day round because of the respiration. In other words, CO2 sequestration = CO2 absorption – CO2 release.

<!-- b000434 | prose | pages [28] -->
Now we only need to decide the weight of carbon dioxide sequestered by the tree and use the converting method below to calculate the total mass of leaves of that tree.

<!-- b000435 | prose | pages [28] -->
𝑀𝑙𝑒𝑎𝑓= 𝑀𝑐𝑎𝑟𝑏𝑜𝑛 𝑑𝑖𝑜𝑥𝑖𝑑𝑒 𝐴𝑠

<!-- b000436 | prose | pages [28] -->
In which,

<!-- b000437 | prose | pages [28] -->
𝑀𝑙𝑒𝑎𝑓:total mass of leaves (g)

<!-- b000438 | prose | pages [28] -->
𝑀𝑐𝑎𝑟𝑏𝑜𝑛 𝑑𝑖𝑜𝑥𝑖𝑑𝑒:mass of carbon dioxide sequestered (lbs)

<!-- b000439 | prose | pages [28] -->
𝐴𝑠:ability to sequester carbon dioxide (lbs/g)

<!-- b000440 | prose | pages [28] -->
8.2.2 CO2 Sequestration and Tree Age The relationship between the amount of CO2 sequestered, the age of a tree and the type of tree is shown in a study published by U.S.

<!-- b000441 | prose | pages [28] -->
Department of Energy in April 1998. The study below divided the growth rate of a certain tree into three categories: fast, moderate and slow. The corresponding chart that categorizes different tree species into 3 grow rates is enclosed in the Appendix 1.

<!-- b000442 | furniture | pages [29] -->
Team #14990

<!-- b000443 | furniture | pages [29] -->
29 / 42

<!-- b000444 | furniture | pages [30] -->
Team #14990

<!-- b000445 | furniture | pages [30] -->
30 / 42

<!-- b000446 | prose | pages [30] -->
From the chart, we can discover an obvious positive relationship

<!-- b000447 | prose | pages [30] -->
between the age of the tree and the amount of CO2 sequestered if we fix

<!-- b000448 | prose | pages [30] -->
the growth rate and the type of the tree. We fit the data into a set of

<!-- b000449 | prose | pages [30] -->
quadratic regression functions shown below:

<!-- b000450 | furniture | pages [31] -->
Team #14990

<!-- b000451 | furniture | pages [31] -->
31 / 42

<!-- b000452 | prose | pages [31] -->
In each function next to the curve, such as y=0.0073x^2+0.9690x+1.0953,

<!-- b000453 | prose | pages [31] -->
which describes Annual Sequestration Rate for fast-growing Hardwood, y

<!-- b000454 | prose | pages [31] -->
is the sequestration rate and x is the tree age.

<!-- b000455 | prose | pages [31] -->
After fitting the data and conduct the statistical inference, we surprisingly

<!-- b000456 | prose | pages [31] -->
find that the fitting curve can actually fit the data perfectly. With the

<!-- b000457 | prose | pages [31] -->
fitting curve and the functions, we can easily estimate the CO2

<!-- b000458 | prose | pages [31] -->
sequestered when given the age of a certain tree.

<!-- b000459 | furniture | pages [32] -->
Team #14990

<!-- b000460 | furniture | pages [32] -->
32 / 42

<!-- b000461 | prose | pages [32] -->
8.2.3 Leaf Mass and Tree Age Since we have known the converting relation between the mass of leaves and the CO2 sequestered, now we can derive the correlation between the age of a tree and the total mass of leaves on that tree by using the CO2 sequestered as a media. After processing the data by the formula in 8.2.1, we get the corresponding relation table shown below. Each cell of the table is the leaf mass of a tree of a certain age, type and growth rate.

<!-- b000462 | prose | pages [32, 33] -->
Hardwood Conifer Year Age Slow Moderate Fast Slow Moderate Fast 0 520 760 1080 424 606 848 1 640 1080 1600 545 909 1333 2 800 1400 2160 667 1212 1879 3 960 1720 2760 848 1515 2485 4 1120 2080 3400 970 1879 3152 5 1280 2440 4040 1152 2242 3879 6 1480 2840 4720 1333 2667 4606 7 1640 3240 5440 1515 3091 5394 8 1840 3640 6200 1697 3515 6182 9 2000 4080 6960 1879 4000 7091 10 2200 4480 7720 2121 4485 8000 11 2400 4920 8520 2303 4970 8909 12 2600 5400 9320 2545 5515 9879 13 2800 5840 10160 2788 6000 10848 14 3000 6320 11000 2970 6545 11879 15 3240 6760 11880 3212 7152 12970 16 3440 7240 12760 3455 7697 14061 17 3640 7760 13640 3697 8303 15152 18 3880 8240 14520 4000 8909 16303 19 4080 8760 15440 4242 9515 17455 20 4320 9280 16400 4485 10121 18667 21 4560 9760 17320 4788 10788 19879 22 4800 10320 18280 5030 11455 21152 23 5000 10840 19240 5333 12121 22424 24 5240 11360 20240 5576 12788 23697 25 5480 11920 21240 5879 13455 25030 26 5720 12480 22240 6182 14182 26364 27 6000 13000 23240 6485 14909 27697 28 6240 13560 24280 6788 15636 29091 29 6480 14120 25320 7091 16364 30485 30 6720 14720 26360 7394 17091 31939 31 7000 15280 27400 7697 17879 33394 32 7240 15880 28480 8061 18606 34848 33 7480 16440 29520 8364 19394 36303 34 7760 17040 30600 8667 20182 37818 35 8000 17640 31720 9030 21030 39333 36 8280 18240 32800 9394 21818 40909 37 8560 18840 33920 9697 22606 42485 38 8800 19440 35040 10061 23455 44061 39 9080 20080 36160 10424 24303 45636 40 9360 20680 37280 10727 25152 47273 41 9640 21320 38440 11091 26000 48909 42 9920 21920 39600 11455 26848 50545 43 10160 22560 40760 11818 27758 52242 44 10440 23200 41920 12182 28606 53939 45 10720 23840 43080 12545 29515 55636 46 11040 24480 44280 12909 30424 57394 47 11320 25120 45440 13333 31333 59091 48 11600 25800 46640 13697 32242 60848 49 11880 26440 47840 14061 33212 62667 50 12160 27120 49080 14485 34121 64424 51 12440 27760 50280 14848 35091 66242 52 12760 28440 51520 15273 36000 68061 53 13040 29120 52720 15636 36970 69939 54 13360 29800 53960 16061 37939 71758 55 13640 30480 55200 16485 38909 73636 56 13920 31160 56480 16848 39939 75515 57 14240 31840 57720 17273 40909 77455 58 14520 32520 59000 17697 41939 79333 59 14840 33200 60240 18121 42909 81273

<!-- b000463 | furniture | pages [33] -->
Team #14990

<!-- b000464 | furniture | pages [33] -->
33 / 42

<!-- b000466 | heading | pages [33] -->
8.3 Tree Age and Tree Size

<!-- b000467 | prose | pages [33] -->
As stated above, we utilize the age of a tree as a link between the two variables,

<!-- b000468 | prose | pages [33] -->
leaf mass and the size characteristics of trees. Since we have found out the

<!-- b000469 | prose | pages [33] -->
correlation between the age of tree and the total leaf mass on it, now we only

<!-- b000470 | prose | pages [33] -->
need to work out the relation between the age of the tree and the size

<!-- b000471 | prose | pages [33] -->
characteristics of it.

<!-- b000472 | prose | pages [33] -->
Tree size is the accumulation of growth, which is a biological phenomenon of

<!-- b000473 | prose | pages [33] -->
increase with time. According the life cycle of a tree, it experiences the following

<!-- b000474 | prose | pages [33] -->
phases:

<!-- b000475 | furniture | pages [34] -->
Team #14990

<!-- b000476 | furniture | pages [34] -->
34 / 42

<!-- b000477 | prose | pages [34] -->
Juvenile phase (youth) - accelerating rate of growth.

<!-- b000478 | prose | pages [34] -->
Full vigor phase (maturity) - constant rate of growth.

<!-- b000479 | prose | pages [34] -->
Senescent phase - decelerating rate of growth.

<!-- b000480 | prose | pages [34] -->
As shown above, the cumulative growth curve, whose pattern is characteristic for

<!-- b000481 | prose | pages [34] -->
the life span of an organism, resembles logistic growth function. Thus we

<!-- b000482 | prose | pages [34] -->
construct the following model

<!-- b000483 | prose | pages [34] -->
P = 𝑘1 ∙(1 −𝑒𝑘2∙𝐴)𝑘3

<!-- b000484 | prose | pages [34] -->
Transformation leads to the following

<!-- b000485 | prose | pages [34] -->
A = 𝑘4 ∙ln(1 −𝑘5 ∙𝑃𝑘6)

<!-- b000486 | prose | pages [34] -->
Where,

<!-- b000487 | prose | pages [34] -->
P is the general profile of a tree(volume, height, mass, diameter).

<!-- b000488 | prose | pages [34] -->
A is the age of the tree.

<!-- b000489 | prose | pages [34] -->
k1, k2, k3, k4, k5 and k6 are constants.

<!-- b000490 | prose | pages [34] -->
It is important to note that P, the general profile of a tree, is a variable to describe

<!-- b000491 | prose | pages [34] -->
the size characteristics of a tree, which vary greatly in different species of trees.

<!-- b000492 | furniture | pages [35] -->
Team #14990

<!-- b000493 | furniture | pages [35] -->
35 / 42

<!-- b000494 | prose | pages [35] -->
Therefore it is not possible to work out an exact set of constants in the model that suits all kinds of trees. This correlation between the size characters and age is primarily qualitative.

<!-- b000495 | heading | pages [35] -->
8.4 Leaf Mass and Tree Size

<!-- b000496 | prose | pages [35] -->
Finally, we get to answer the question whether there exists a correlation between leaf mass and tree size characteristics.

<!-- b000497 | prose | pages [35] -->
According to our study in X.2, leaf mass and tree age are related with each other mathematically linked by CO2 Sequestration. Our model in X.3 determines a function between tree age and tree size. Through this relationship map shown below, it is clear that there must exist a correlation between leaf mass and tree size.

<!-- b000498 | heading | pages [35] -->
9. Strengths and Weaknesses

<!-- b000499 | prose | pages [35] -->
Now we will analyze the strengths and weaknesses of each sub-model in our paper:

<!-- b000500 | furniture | pages [36] -->
Team #14990

<!-- b000501 | furniture | pages [36] -->
36 / 42

<!-- b000502 | heading | pages [36] -->
Model 1

<!-- b000503 | prose | pages [36] -->
Strength:

<!-- b000504 | prose | pages [36] -->
1. Our model is based on quantitative analysis, so the classification process is

<!-- b000505 | prose | pages [36] -->
both objective and efficient; 2. Our model chooses leaf types that are most typical and common as the

<!-- b000506 | prose | pages [36] -->
categories.

<!-- b000507 | prose | pages [36] -->
Weakness:

<!-- b000508 | prose | pages [36] -->
1.  Because of the limit of time and access to information, we only create six

<!-- b000509 | prose | pages [36] -->
categories, which may not cover all the leaf types.

<!-- b000510 | heading | pages [36] -->
Model 2

<!-- b000511 | prose | pages [36] -->
Strength:

<!-- b000512 | prose | pages [36] -->
1. We have taken into consideration three conditions: tropical zone,

<!-- b000513 | prose | pages [36] -->
temperate zone and frigid zone when discussing the relationship between

<!-- b000514 | prose | pages [36] -->
the leaf distribution and the leaf shape; 2. The result of our model conforms to our observation and the data we found.

<!-- b000515 | prose | pages [36] -->
Weakness:

<!-- b000516 | prose | pages [36] -->
1. We consider the leaves distribution on a single branch, but have not

<!-- b000517 | prose | pages [36] -->
considered the inner-influence between different leaves of different

<!-- b000518 | prose | pages [36] -->
branches.

<!-- b000519 | heading | pages [36] -->
Model 3

<!-- b000520 | prose | pages [36] -->
Strength:

<!-- b000521 | prose | pages [36] -->
1. The whole process use data and quantitative analysis as foundations, so the

<!-- b000522 | prose | pages [36] -->
output is objective and reasonable.

<!-- b000523 | prose | pages [36] -->
Weakness:

<!-- b000524 | prose | pages [36] -->
1. We have limited categories of tree profiles, so our data to fit the curve is not

<!-- b000525 | prose | pages [36] -->
plenty enough.

<!-- b000526 | furniture | pages [37] -->
Team #14990

<!-- b000527 | furniture | pages [37] -->
37 / 42

<!-- b000528 | heading | pages [37] -->
Model 4

<!-- b000529 | prose | pages [37] -->
Strength:

<!-- b000530 | prose | pages [37] -->
1. We use the carbon sequestration rate and age as the mediums to calculate

<!-- b000531 | prose | pages [37] -->
the mass of total laves, which are far more scientific than estimating the

<!-- b000532 | prose | pages [37] -->
number of leaves and weight of each leaf.

<!-- b000533 | prose | pages [37] -->
Weakness:

<!-- b000534 | prose | pages [37] -->
1. Since the data we get are from the statistics a little bit outdated, the

<!-- b000535 | prose | pages [37] -->
accuracy of our output may need some slight adjustment.

<!-- b000536 | heading | pages [37] -->
10. Reference

<!-- b000537 | references | pages [37] -->
[1]  David Knight, James Painter and Matthew Potter from Stanford University,

<!-- b000538 | references | pages [37] -->
department of electrical engineering, "Automatic Plant Leaf Classification for a Mobile

<!-- b000539 | references | pages [37] -->
Field Guide" .

<!-- b000540 | references | pages [37] -->
[2]  Z. Wang, Z. Chi, and D. Feng, “Shape based leaf image retrieval,” IEEE

<!-- b000541 | references | pages [37] -->
Proceedings: Vision, Image, and Signal Processing, vol. 150-1, pp. 34-43, February 2003.

<!-- b000542 | references | pages [37] -->
[3]   J. Du, X. Wang, and G. Zhang, “Leaf shape based plant species recognition,”

<!-- b000543 | references | pages [37] -->
Applied Mathematics and Computation, vol. 185-2, pp.883-893, February 2007.

<!-- b000544 | references | pages [37] -->
[4]  C. Im, H. Nishida, and T.L. Kunil, “Recognizing plant species by leaf shapes—a

<!-- b000545 | references | pages [37] -->
case study of the acer family,” in Proceedings of 1998 IEEE International Conference on

<!-- b000546 | references | pages [37] -->
Pattern Recognition, Brisbane, August 1998.

<!-- b000547 | references | pages [37] -->
[5]  Hirokazu Tsukaya Graduate School of Science, University of Tokyo,

<!-- b000548 | references | pages [37] -->
"Mechanism of Leaf-Shape Determination," in Annu. Rev. Plant Biol. 2006.57:477-496.

<!-- b000549 | references | pages [37] -->
[6]   U.S. Department of Energy Energy Information Administration, "Method for

<!-- b000550 | references | pages [37] -->
Calculating Carbon Sequestration by Trees in Urban and Suburban Settings," April 1998

<!-- b000551 | furniture | pages [38] -->
Team #14990

<!-- b000552 | furniture | pages [38] -->
38 / 42

<!-- b000553 | heading | pages [38] -->
11. A Letter to the Science Journal Editor

<!-- b000554 | prose | pages [38] -->
Dear editor,

<!-- b000555 | prose | pages [38] -->
From the very ancient times, leaves have been an important part of human life as they were weaved into clothes, used as containers of water, and most of all, relied upon as the main converter of carbon dioxide into oxygen. However, due to the variety and large quantity of leaves, there have always remained a lot of questions and mysteries of them, such as the reason behind their different shapes and distribution pattern as well as the relationship between leaf shape, leaf mass and tree profile. So, out of the interest in discovering the wonders of the nature and exploring the potential practical use of the natural phenomena, we, a group of high school students from Shanghai, have done some researches and now we are very glad to present to you our key findings:

<!-- b000556 | prose | pages [38] -->
We first focus on the possible influence of leaf distribution on leaf shape. We discover that for survival reasons, the trees develop an optimal leaf distribution and shape pattern to best adjust to the specific region of its origin by maximizing the exposure area to sunshine, thereby gaining the most nutrients for photosynthesis. And after testing our findings, we are convinced there does exist a mathematical relationship between the solar altitude, leaf shape and leaf distribution. With the above finding, we may be able to determine the best location for replanting or assisted-migration of a tree species by observing its leaf distribution.

<!-- b000557 | prose | pages [38] -->
Our second key finding is a rough correlation between the tree profile and leaves growing on that tree. In fact, we make a hypothesis that a leaf be a two-dimensional mimic of the tree. After we set up the database and compare the shape of leaf and the contour of tree carefully, some similarities between certain characteristics have surfaced. This finding suggests that the natural world might contain many examples of self-similarity, mathematical concept which means that an object is approximately similar to a part of itself, such as the famous Koch Snowflake and Mandelbrot Set.

<!-- b000558 | prose | pages [38] -->
The third part of our study deals with the relationship between the tree size characteristics and the total mass of the leaves. The two ends are linked by two calculating mediums, the CO2 sequestration rates and the age of the tree. Therefore, we are able to estimate the total mass of the leaves given some profiles of a tree such as its height, diameter, volume, age and type, and vice versa. This finding might have great potential for agricultural and environmental uses, such as a new method to estimate tea production or wood production, or estimation of CO2 sequestration effect of a leaf, a tree and, most importantly, a forest, which is a great alleviator of global warming.

<!-- b000559 | prose | pages [38] -->
In hope of publishing our research in your outstanding science journal, we’ve enclosed our research paper for you to examine and judge. We are convinced that our research on leaves is promising to contribute to a variety of areas.

<!-- b000560 | prose | pages [38] -->
Yours faithfully

<!-- b000561 | furniture | pages [39] -->
Team #14990

<!-- b000562 | furniture | pages [39] -->
39 / 42

<!-- b000563 | heading | pages [39] -->
12. Appendix

<!-- b000564 | heading | pages [39] -->
12.1 Chart of Tree Species and Growth Rate

<!-- b000565 | prose | pages [39] -->
12.2 MATLAB Program Code How to use MATLAB to realize AHP A=input('A=');

<!-- b000566 | prose | pages [39] -->
[n,n]=size(A);

<!-- b000567 | prose | pages [39] -->
%Input the pair ratio matrix as “A”.

<!-- b000568 | prose | pages [39] -->
x=ones(n,100);

<!-- b000569 | prose | pages [39] -->
y=ones(n,100);

<!-- b000570 | prose | pages [39] -->
m=zeros(1,100);

<!-- b000571 | prose | pages [39] -->
m(1)=max(x(:,1));

<!-- b000572 | prose | pages [39] -->
y(:,1)=x(:,1);

<!-- b000573 | prose | pages [39] -->
x(:,2)=A*y(:,1);

<!-- b000574 | furniture | pages [40] -->
Team #14990

<!-- b000575 | furniture | pages [40] -->
40 / 42

<!-- b000576 | prose | pages [40, 41] -->
m(2)=max(x(:,2)); y(:,2)=x(:,2)/m(2); p=0.0001;i=2;k=abs(m(2)-m(1)); while k>p i=i+1; x(:,i)=A*y(:,i-1); m(i)=max(x(:,i)); y(:,i)=x(:,i)/m(i); k=abs(m(i)-m(i-1)); end a=sum(y(:,i)); w=y(:,i)/a; %Find the Eigen Vector t=m(i); disp('EigenVector Wi='); disp(w); disp('LamdaMax='); disp(t); CI=(t-n)/(n-1); %Calculate the Consistency Index (CI) RI=[0 0 0.52 0.89 1.12 1.26 1.36 1.41 1.46 1.49 1.52 1.54 1.56 1.58 1.59]; %Random Consistency Index (RI) disp('CI=');disp(CI); disp('RI=');disp(RI(n)); if RI(n)>0 CR=CI/RI(n); %Calculate the consistency ratio according to the formula disp('CR=');disp(CR); if CR<0.10 disp('Consistency Acceptable'); else disp('Consistency Inacceptable'); end %Consistency Check end if RI(n)<=0 disp('Consistency Acceptable'); %Consistency Check end

<!-- b000577 | furniture | pages [41] -->
Team #14990

<!-- b000578 | furniture | pages [41] -->
41 / 42

<!-- b000580 | prose | pages [41] -->
How to calculate the area of a leaf l=imread('leaftype1.jpg'); imshow(l); %Import the picture m=ginput; %Pick the points on the perimeter of the figure and record the coordinates into “m” x(1,:)=m(:,1); y(1,:)=m(:,2); x=[x x(1)]; y=[y y(1)]; N=length(x); t=1:N; ti=1:(N-1)/100000:N; xi=spline(t,x,ti); yi=spline(t,y,ti); area=polyarea(xi,yi); %calculate the area of the figure points=[x;y]; fnplt(cscvn(points));axis equal %draw the estimated function and check the accuracy; save the figure as „1-1.jpg‟ for further use

<!-- b000581 | prose | pages [41] -->
How to calculate the perimeter of a leaf k=imread('1-1.jpg'); BW=im2bw(k); %turn the picture into binary form STATS=regionprops(BW,'Perimeter'); %calculate the perimeter of the binary figure STATS.Perimeter; %print the perimeter

<!-- b000582 | prose | pages [41] -->
Linear Regression with significance test x=input('Input x');

<!-- b000583 | furniture | pages [42] -->
Team #14990

<!-- b000584 | furniture | pages [42] -->
42 / 42

<!-- b000585 | prose | pages [42] -->
% Input the parameters of the leaves as x coordinates y=input('Input y'); % Input the parameters of the trees as y coordinates c=length(x); xi=0:0.1:1; a=polyfit(x,y,1); % Find the coefficients of the fitting curve of the points yi=polyval(a,xi); % Calculate the y coordinates of the fitting curve hold on; plot(x,y,'go','MarkerEdgeColor','k','MarkerFace Color','g','MarkerSize',5); % Draw the original input data plot(xi,yi,'linewidth',2,'markersize',7); % Draw the fitting curve hold off; x=x'; y=y'; x=[ones(c,1),x]; [b,bint,r,rint,stats]=regress(y,x); % Significance test
