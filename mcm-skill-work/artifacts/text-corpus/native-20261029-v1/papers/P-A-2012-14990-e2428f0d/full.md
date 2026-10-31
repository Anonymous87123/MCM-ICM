# P-A-2012-14990-e2428f0d

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #14990

<!-- b000002 | furniture | pages [1] -->


<!-- b000003 | furniture | pages [1] -->
1 / 42

<!-- b000004 | furniture | pages [1] -->


<!-- b000005 | furniture | pages [1] -->


<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | furniture | pages [1] -->


<!-- b000008 | title | pages [1] -->
A Close Look On Leaves

<!-- b000009 | furniture | pages [1] -->


<!-- b000010 | title | pages [1] -->
Team 14990

<!-- b000011 | furniture | pages [2] -->
Team #14990

<!-- b000012 | furniture | pages [2] -->


<!-- b000013 | furniture | pages [2] -->
2 / 42

<!-- b000014 | furniture | pages [2] -->


<!-- b000015 | heading | pages [2] -->
CONTENTS

<!-- b000016 | heading | pages [2] -->
1. Introduction------------------------------------------------------------------------------------3

<!-- b000017 | heading | pages [2] -->
2. Breaking Down the Problem---------------------------------------------------------------3

<!-- b000018 | heading | pages [2] -->
3. Assumptions-----------------------------------------------------------------------------------4

<!-- b000019 | heading | pages [2] -->
4. Nomenclatures--------------------------------------------------------------------------------5

<!-- b000020 | heading | pages [2] -->
5. Model One: Leaf Classification------------------------------------------------------------6

<!-- b000021 | prose | pages [2] -->
5.1 Decisive Parameters

<!-- b000022 | prose | pages [2] -->
5.2 Comparison

<!-- b000023 | prose | pages [2] -->
5.3 Model Testing

<!-- b000024 | prose | pages [2] -->
5.4 Conclusion

<!-- b000025 | heading | pages [2] -->
6. Model Two: Leaf Distribution and Leaf Shape--------------------------------------14

<!-- b000026 | prose | pages [2] -->
6.1 Introduction

<!-- b000027 | prose | pages [2] -->
6.2 Idealized Leaf Distribution Model

<!-- b000028 | prose | pages [2] -->
6.3 Analysis of Overlapping Areas

<!-- b000029 | prose | pages [2] -->
6.3.1 Solar Altitude Trending toward 90°

<!-- b000030 | prose | pages [2] -->
6.3.2 Solar Altitude Trending toward 0°

<!-- b000031 | prose | pages [2] -->
6.3.3 Solar Altitude within normal range

<!-- b000032 | prose | pages [2] -->
6.4 Model Testing

<!-- b000033 | heading | pages [2] -->
7. Model Three: Tree Profile and Leaf Shape-------------------------------------------19

<!-- b000034 | prose | pages [2] -->
7.1 Introduction

<!-- b000035 | prose | pages [2] -->
7.2 Hypothesis

<!-- b000036 | prose | pages [2] -->
7.3 Comparison of Leaf Shape and Tree Contour

<!-- b000037 | prose | pages [2] -->
7.4 Conclusion

<!-- b000038 | heading | pages [2] -->
8. Model Four: Leaf Mass--------------------------------------------------------------------27

<!-- b000039 | prose | pages [2] -->
8.1 Introduction

<!-- b000040 | prose | pages [2] -->
8.2 Leaf Mass and Tree Age

<!-- b000041 | prose | pages [2] -->
8.2.1 Leaf Mass and CO2 Sequestration

<!-- b000042 | prose | pages [2] -->
8.2.2 CO2 Sequestration and Tree Age

<!-- b000043 | prose | pages [2] -->
8.2.3 Leaf Mass and Tree Age

<!-- b000044 | prose | pages [2] -->
8.3 Tree Age and Tree Size

<!-- b000045 | prose | pages [2] -->
8.4 Leaf Mass and Tree Size

<!-- b000046 | heading | pages [2] -->
9. Strength and Weakness-------------------------------------------------------------------35

<!-- b000047 | heading | pages [2] -->
10. Reference--------------------------------------------------------------------------------------37

<!-- b000048 | heading | pages [2] -->
11. A Letter to the Science Journal Editor-------------------------------------------------38

<!-- b000049 | heading | pages [2] -->
12. Appendix--------------------------------------------------------------------------------------39

<!-- b000050 | prose | pages [2] -->
12.1 Chart of Tree Species and Growth Rate

<!-- b000051 | prose | pages [2] -->
12.2 MATLAB Program Code

<!-- b000052 | furniture | pages [3] -->
Team #14990

<!-- b000053 | furniture | pages [3] -->


<!-- b000054 | furniture | pages [3] -->
3 / 42

<!-- b000055 | furniture | pages [3] -->


<!-- b000056 | heading | pages [3] -->
1. Introduction

<!-- b000057 | prose | pages [3] -->
Leaf, which is responsible for photosynthesis and storage of food and water, is a very

<!-- b000058 | prose | pages [3] -->
important organ of a plant. Leaf has so many different and interesting shapes and

<!-- b000059 | prose | pages [3] -->
contours, which make it so catching and conspicuous in the plant kingdom. For centuries,

<!-- b000060 | prose | pages [3] -->
people have always wondered why the leaf has so many splendid shapes. Is this just a gift

<!-- b000061 | prose | pages [3] -->
from the Almighty God? Or is it the adjustment the leaf takes during its evolution and

<!-- b000062 | prose | pages [3] -->
adaptation?

<!-- b000063 | prose | pages [3] -->
Another mystery of the leaf lies in the classification of different leaf types. Can we do so

<!-- b000064 | prose | pages [3] -->
in a more reliable and scientific way instead of judging subjectively? We have tried our

<!-- b000065 | prose | pages [3] -->
best to build a model on a quantitative base to increase the accuracy and efficiency of

<!-- b000066 | prose | pages [3] -->
classifying different leaves.

<!-- b000067 | prose | pages [3] -->
The final mystery about the tree is how much the total leaf mass on a tree is. Just like

<!-- b000068 | prose | pages [3] -->
people always want to figure out how much hair a person has, human beings always have

<!-- b000069 | prose | pages [3] -->
a fancy to find out a solution from the seemingly infinity and incalculable.

<!-- b000070 | prose | pages [3] -->
We are deeply convinced that the true glamour of scientific and mathematical models is

<!-- b000071 | prose | pages [3] -->
to unveil the intriguing and the changeable of the nature. Aiming to do so, we will

<!-- b000072 | prose | pages [3] -->
generate models that can fit large quantities of data with highest accuracy within a quick

<!-- b000073 | prose | pages [3] -->
flick.

<!-- b000074 | heading | pages [3] -->
2. Breaking Down the Problem

<!-- b000075 | prose | pages [3] -->
After carefully analyzing the problem, we conclude four main sub-problems to tackle in

<!-- b000076 | prose | pages [3] -->
our paper:

<!-- b000077 | prose | pages [3] -->
1. Classification the different types of leaves

<!-- b000078 | prose | pages [3] -->
2. Relationship between the leaf distribution and leaf shape

<!-- b000079 | prose | pages [3] -->
3. Relationship between the tree profile and leaf shape

<!-- b000080 | prose | pages [3] -->
4. Calculation of the total leaf mass on a leaf

<!-- b000081 | prose | pages [3] -->
To tackle the first problem, we set a set of parameters to quantify the characters of the

<!-- b000082 | prose | pages [3] -->
leaf shape and use the leaf shape as the main standard for our classification process.

<!-- b000083 | prose | pages [3] -->
As for the second question, we want to use the overlapping area that one leaf casts on

<!-- b000084 | prose | pages [3] -->
the leaf directly under it as a medium to associate the leaf distribution and leaf shape,

<!-- b000085 | furniture | pages [4] -->
Team #14990

<!-- b000086 | furniture | pages [4] -->


<!-- b000087 | furniture | pages [4] -->
4 / 42

<!-- b000088 | furniture | pages [4] -->


<!-- b000089 | prose | pages [4] -->
since the leaf shape will affect the overlapping and we assume the leaf distribution will

<!-- b000090 | prose | pages [4] -->
try to minimize the overlapping area.

<!-- b000091 | prose | pages [4] -->
As for the third question, we want to refer to the process we take when tackling the first

<!-- b000092 | prose | pages [4] -->
problem and also set some parameters for the tree profile. After that, we will compare

<!-- b000093 | prose | pages [4] -->
their parameters and judge whether there is a relation between tree profile and leaf

<!-- b000094 | prose | pages [4] -->
shape.

<!-- b000095 | prose | pages [4] -->
To deal with the total mass of the leaves, we want to use the age to link the size of tree

<!-- b000096 | prose | pages [4] -->
and the total weight of leaves of it because the tree size has an obvious relationship with

<!-- b000097 | prose | pages [4] -->
its age and the age will affect a tree’s sequestration of carbon dioxide, which will reflect

<!-- b000098 | prose | pages [4] -->
the weight of a tree’s total leaves.

<!-- b000099 | heading | pages [4] -->
3. Assumptions

<!-- b000100 | prose | pages [4] -->
1. The trees being studied are all individual (“open grown”) trees, such as trees typically

<!-- b000101 | prose | pages [4] -->
planted along streets, in yards, and in parks. Our calculation does not apply to

<!-- b000102 | prose | pages [4] -->
densely raised trees, as in typical reforestation projects where large numbers of

<!-- b000103 | prose | pages [4] -->
trees are planted closely together.

<!-- b000104 | prose | pages [4] -->
2. Assume the shape of the leaves does not reflect special uses for the trees, such as to

<!-- b000105 | prose | pages [4] -->
resist extremely windy, cold, parched, wet or dry conditions or to catch food.

<!-- b000106 | prose | pages [4] -->
3. Assume the type of the leaf distribution to be discussed (leaf length and internode

<!-- b000107 | prose | pages [4] -->
distance relation) is only a reflection of the tree's natural tendency to sunlight.

<!-- b000108 | prose | pages [4] -->
4. Assume the tree profile we consider is the part above ground, including the trunk,

<!-- b000109 | prose | pages [4] -->
the branches and leaves.

<!-- b000110 | prose | pages [4] -->
5. Assume all parts of leaf lay on a flat surface and the thickness or protrusion of veins

<!-- b000111 | prose | pages [4] -->
are neglectable.

<!-- b000112 | prose | pages [4] -->
6. Assume leaves are the only part of the tree that reacts in photosynthesis and

<!-- b000113 | prose | pages [4] -->
respiration so that the carbon dioxide sequestration of a tree is the sum of the

<!-- b000114 | prose | pages [4] -->
sequestration of the leaves.

<!-- b000115 | prose | pages [4] -->
7. Assume the sequestration of a tree or a leaf is the net amount of CO2 fixed in a tree,

<!-- b000116 | prose | pages [4] -->
which is the difference between the CO2 released in respiration and the CO2

<!-- b000117 | prose | pages [4] -->
absorbed in photosynthesis.

<!-- b000118 | prose | pages [4] -->
8. Assume the trees are in healthy, mature and stable condition. The trees of the same

<!-- b000119 | prose | pages [4] -->
species have same characteristics.

<!-- b000120 | furniture | pages [4] -->


<!-- b000121 | furniture | pages [4] -->


<!-- b000122 | furniture | pages [5] -->
Team #14990

<!-- b000123 | heading | pages [5] -->
4. Nomenclatures

<!-- b000124 | prose | pages [5] -->
𝑅

<!-- b000125 | prose | pages [5] -->
𝐴𝑙𝑒𝑎𝑓

<!-- b000126 | prose | pages [5] -->
𝐴𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒

<!-- b000127 | prose | pages [5] -->
𝐴𝑅

<!-- b000128 | prose | pages [5] -->
𝐿𝑠𝑕𝑜𝑟𝑡

<!-- b000129 | prose | pages [5] -->
𝐿𝑙𝑜𝑛𝑔

<!-- b000130 | prose | pages [5] -->
𝐶

<!-- b000131 | prose | pages [5] -->
𝑅𝑖𝑛

<!-- b000132 | prose | pages [5] -->
𝑅𝑒𝑥

<!-- b000133 | prose | pages [5] -->
𝐹𝐹

<!-- b000134 | prose | pages [5] -->
𝑃𝑙𝑒𝑎𝑓

<!-- b000135 | prose | pages [5] -->
𝐸𝑅𝐴𝐼

<!-- b000136 | prose | pages [5] -->
𝐵𝑃𝐴

<!-- b000137 | prose | pages [5] -->
𝐸𝑅𝑃𝐼

<!-- b000138 | prose | pages [5] -->
𝐵𝑃𝑃

<!-- b000139 | prose | pages [5] -->
𝑃𝐼𝑖

<!-- b000140 | prose | pages [5] -->
𝐼𝐷

<!-- b000141 | prose | pages [5] -->
𝐿𝑚𝑎𝑗𝑜𝑟

<!-- b000142 | prose | pages [5] -->
Aoverlapping

<!-- b000143 | prose | pages [5] -->
α

<!-- b000144 | prose | pages [5] -->
𝑀𝑙𝑒𝑎𝑓

<!-- b000145 | prose | pages [5] -->
𝑀𝑐𝑎𝑟𝑏𝑜𝑛 𝑑𝑖𝑜𝑥𝑖𝑑𝑒

<!-- b000146 | prose | pages [5] -->
𝐴𝑠

<!-- b000147 | prose | pages [5] -->
A

<!-- b000148 | furniture | pages [5] -->


<!-- b000149 | furniture | pages [5] -->


<!-- b000150 | furniture | pages [5] -->
5 / 42

<!-- b000151 | furniture | pages [5] -->


<!-- b000152 | prose | pages [5] -->
Rectangularity

<!-- b000153 | prose | pages [5] -->
the area of leaf

<!-- b000154 | prose | pages [5] -->
the area of minimum bounding rectangle

<!-- b000155 | prose | pages [5] -->
the aspect ratio

<!-- b000156 | prose | pages [5] -->
the length of shorter side

<!-- b000157 | prose | pages [5] -->
the length of longer side

<!-- b000158 | prose | pages [5] -->
the circularity

<!-- b000159 | prose | pages [5] -->
the radius of in-circle

<!-- b000160 | prose | pages [5] -->
the radius of ex-circle

<!-- b000161 | prose | pages [5] -->
Form factor

<!-- b000162 | prose | pages [5] -->
the perimeter of leaf

<!-- b000163 | prose | pages [5] -->
the edge regularity area index

<!-- b000164 | prose | pages [5] -->
The bounding polygon area

<!-- b000165 | prose | pages [5] -->
the edge regularity perimeter index

<!-- b000166 | prose | pages [5] -->
the bounding polygon perimeter

<!-- b000167 | prose | pages [5] -->
Proportional index

<!-- b000168 | prose | pages [5] -->
the Index of Deviation

<!-- b000169 | prose | pages [5] -->
the length of major axis

<!-- b000170 | prose | pages [5] -->
the overlapping area

<!-- b000171 | prose | pages [5] -->
the solar altitude

<!-- b000172 | prose | pages [5] -->
the total mass of leaves on a tree

<!-- b000173 | prose | pages [5] -->
mass of carbon dioxide sequestered (lbs)

<!-- b000174 | prose | pages [5] -->
ability to sequester carbon dioxide (lbs/g)

<!-- b000175 | prose | pages [5] -->
the age of the tree

<!-- b000176 | furniture | pages [6] -->
Team #14990

<!-- b000177 | furniture | pages [6] -->


<!-- b000178 | furniture | pages [6] -->
6 / 42

<!-- b000179 | furniture | pages [6] -->


<!-- b000180 | heading | pages [6] -->
5. Model One: Leaf Classification

<!-- b000181 | heading | pages [6] -->
5.1 Decisive Parameters

<!-- b000182 | prose | pages [6] -->
In order to classify the shapes of the given leaf, we want to set a number of

<!-- b000183 | prose | pages [6] -->
parameters and establish a database for comparison. After carefully and

<!-- b000184 | prose | pages [6] -->
thoroughly analyzing the leaves, we develop seven most significant parameters

<!-- b000185 | prose | pages [6] -->
as shown below:

<!-- b000186 | heading | pages [6] -->
1. Rectangularity

<!-- b000187 | prose | pages [6] -->
Firstly, we define the ratio of the area of the leaf to the Minimum Bounding

<!-- b000188 | prose | pages [6] -->
Rectangle as the leaf’s Rectangularity, how much does the leaf resemble a

<!-- b000189 | prose | pages [6] -->
rectangle (refer to figure 2.1). The maximum possible value of this parameter

<!-- b000190 | prose | pages [6] -->
is 1.

<!-- b000191 | prose | pages [6] -->
R =

<!-- b000192 | prose | pages [6] -->
𝐴𝑙𝑒𝑎𝑓

<!-- b000193 | furniture | pages [6] -->


<!-- b000194 | prose | pages [6] -->
𝐴𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒

<!-- b000195 | prose | pages [6] -->
𝐴𝑙𝑒𝑎𝑓 stands for the area of leaf

<!-- b000196 | prose | pages [6] -->
𝐴𝑟𝑒𝑐𝑡𝑎𝑛𝑔𝑙𝑒 stands for the area of minimum bounding rectangle

<!-- b000197 | heading | pages [6] -->
2. Aspect ratio

<!-- b000198 | prose | pages [6] -->
After defining the rectangularity, now we define

<!-- b000199 | prose | pages [6] -->
the Aspect Ratio, which describes the

<!-- b000200 | prose | pages [6] -->
proportional relationship between the width of

<!-- b000201 | prose | pages [6] -->
and height of a leaf’s Minimum Bounding

<!-- b000202 | prose | pages [6] -->
Rectangle, as another key character to classify

<!-- b000203 | prose | pages [6] -->
general shape of a leaf. The bigger this ratio is,

<!-- b000204 | prose | pages [6] -->
the more this leaf resembles a square (refer to

<!-- b000205 | caption | pages [6] -->
figure 2.1). The maximum possible value of this

<!-- b000206 | prose | pages [6] -->
parameter is 1.

<!-- b000207 | prose | pages [6] -->
𝐿𝑠𝑕𝑜𝑟𝑡

<!-- b000208 | prose | pages [6] -->
AR =

<!-- b000209 | prose | pages [6] -->
𝐿long

<!-- b000210 | prose | pages [6] -->
Where

<!-- b000211 | prose | pages [6] -->
AR stands for the aspect ratio

<!-- b000212 | caption | pages [6] -->
Figure 2.1

<!-- b000213 | furniture | pages [7] -->
Team #14990

<!-- b000214 | furniture | pages [7] -->


<!-- b000215 | furniture | pages [7] -->
7 / 42

<!-- b000216 | furniture | pages [7] -->


<!-- b000217 | prose | pages [7] -->
𝐿𝑠𝑕𝑜𝑟𝑡 stands for the length of shorter side

<!-- b000218 | prose | pages [7] -->
𝐿long stands for the length of longer side

<!-- b000219 | heading | pages [7] -->
3. Circularity

<!-- b000220 | prose | pages [7] -->
To evaluate how roundish a leaf is, we

<!-- b000221 | prose | pages [7] -->
consider that the respective radius of

<!-- b000222 | prose | pages [7] -->
in-circle and ex-circle. The ratio of the

<!-- b000223 | prose | pages [7] -->
former to the latter, which we define as

<!-- b000224 | prose | pages [7] -->
reflect Circularity, may well this

<!-- b000225 | prose | pages [7] -->
characteristic. The greater the ratio of

<!-- b000226 | prose | pages [7] -->
Circularity is, the closer the leaf is to a

<!-- b000227 | prose | pages [7] -->
circle, (refer to figure 2.2) The

<!-- b000228 | prose | pages [7] -->
maximum possible value

<!-- b000229 | prose | pages [7] -->
parameter is 1.

<!-- b000230 | prose | pages [7] -->
Where

<!-- b000231 | prose | pages [7] -->
C stands for the circularity

<!-- b000232 | prose | pages [7] -->
of this

<!-- b000233 | caption | pages [7] -->
Figure 2.2

<!-- b000234 | prose | pages [7] -->
C = 𝑅𝑖𝑛

<!-- b000235 | furniture | pages [7] -->


<!-- b000236 | prose | pages [7] -->
𝑅𝑒𝑥

<!-- b000237 | prose | pages [7] -->
𝑅𝑖𝑛 stands for the radius of in-circle

<!-- b000238 | prose | pages [7] -->
𝑅𝑒𝑥 stands for the radius of ex-circle

<!-- b000239 | heading | pages [7] -->
4. Form factor

<!-- b000240 | prose | pages [7] -->
Form Factor, a famous shape description parameter, is another essential

<!-- b000241 | prose | pages [7] -->
indicator of leaf classification. The maximum possible value of this

<!-- b000242 | prose | pages [7] -->
parameter is 1.

<!-- b000243 | prose | pages [7] -->
Where

<!-- b000244 | prose | pages [7] -->
FF = 4𝜋𝐴𝑙𝑒𝑎𝑓

<!-- b000245 | prose | pages [7] -->
2

<!-- b000246 | prose | pages [7] -->
𝑃𝑙𝑒𝑎𝑓

<!-- b000247 | prose | pages [7] -->
𝑃𝑙𝑒𝑎𝑓 stands for the perimeter of leaf

<!-- b000248 | furniture | pages [8] -->
Team #14990

<!-- b000249 | heading | pages [8] -->
5. Edge regularity area index.

<!-- b000250 | furniture | pages [8] -->


<!-- b000251 | furniture | pages [8] -->
8 / 42

<!-- b000252 | furniture | pages [8] -->


<!-- b000253 | prose | pages [8] -->
Although the aspect ratio and the rectangularity of two leaves may resemble,

<!-- b000254 | prose | pages [8] -->
the contour or the exact shape of two leaves may vary much.

<!-- b000255 | prose | pages [8] -->
Thus, In order to take the different contour of the leaf into consideration, we

<!-- b000256 | prose | pages [8] -->
join every convex dot along the contour and develop a specific parameter,

<!-- b000257 | prose | pages [8] -->
which we call Bounding Polygon Area. The ratio between the leaf area and

<!-- b000258 | prose | pages [8] -->
this bounding polygon area is a good quantitative factor, defined as Edge

<!-- b000259 | prose | pages [8] -->
Regularity Area Index.

<!-- b000260 | furniture | pages [8] -->


<!-- b000261 | furniture | pages [8] -->


<!-- b000262 | caption | pages [8] -->
Figure 2.3

<!-- b000263 | furniture | pages [8] -->


<!-- b000264 | prose | pages [8] -->
The more this ratio is close to 1, the less jagged

<!-- b000265 | prose | pages [8] -->
and the smoother this leaf’s contour is (refer to

<!-- b000266 | caption | pages [8] -->
figure 2.3). The maximum possible value of this

<!-- b000267 | prose | pages [8] -->
parameter is 1.

<!-- b000268 | prose | pages [8] -->
ERAI = 𝐴𝑙𝑒𝑎𝑓

<!-- b000269 | prose | pages [8] -->
𝐵𝑃𝐴

<!-- b000270 | prose | pages [8] -->
Where

<!-- b000271 | prose | pages [8] -->
ERAI stands for the edge regularity area index

<!-- b000272 | prose | pages [8] -->
𝐵𝑃𝐴 stands for bounding polygon area

<!-- b000273 | heading | pages [8] -->
6. Edge regularity perimeter index

<!-- b000274 | prose | pages [8] -->
Similarly, we develop another parameter: Bounding Polygon Perimeter, the

<!-- b000275 | prose | pages [8] -->
perimeter of the polygon when we join the convex dots of a leaf. We define

<!-- b000276 | prose | pages [8] -->
the ratio of the convex dot perimeter and the perimeter of the leaf as Edge

<!-- b000277 | prose | pages [8] -->
Regularity Perimeter Index. This time, the smaller this ratio is, the more

<!-- b000278 | prose | pages [8] -->
jagged and irregular the contour of the leaf is (refer to figure 2.4). The

<!-- b000279 | prose | pages [8] -->
maximum possible value of this parameter is 1.

<!-- b000280 | prose | pages [8] -->
ERPI = 𝐵𝑃𝑃

<!-- b000281 | furniture | pages [8] -->


<!-- b000282 | prose | pages [8] -->
𝑃𝑙𝑒𝑎𝑓

<!-- b000283 | furniture | pages [9] -->
Team #14990

<!-- b000284 | prose | pages [9] -->
Where

<!-- b000285 | furniture | pages [9] -->


<!-- b000286 | furniture | pages [9] -->
9 / 42

<!-- b000287 | furniture | pages [9] -->


<!-- b000288 | prose | pages [9] -->
ERPI stands for the edge regularity perimeter

<!-- b000289 | prose | pages [9] -->
index

<!-- b000290 | prose | pages [9] -->
𝐵𝑃𝑃 stands for the bounding polygon perimeter

<!-- b000291 | heading | pages [9] -->
7. Proportional index

<!-- b000292 | prose | pages [9] -->
Since it is also highly critical to capture the spatial

<!-- b000293 | prose | pages [9] -->
distribution of different portions of a leaf along its

<!-- b000294 | prose | pages [9] -->
vertical axis, we divide the minimum bounding

<!-- b000295 | prose | pages [9] -->
rectangle into four blocks horizontally, and

<!-- b000296 | prose | pages [9] -->
calculate the proportion of the leaf area in a

<!-- b000297 | prose | pages [9] -->
particular region to the total leaf, which we refer

<!-- b000298 | prose | pages [9] -->
to as the Proportional Index.

<!-- b000299 | caption | pages [9] -->
Figure 2.4

<!-- b000300 | prose | pages [9] -->
𝑃𝐼𝑖= 𝑎𝑟𝑒𝑎 𝑜𝑓 𝑏𝑙𝑜𝑐𝑘 𝑖

<!-- b000301 | furniture | pages [9] -->


<!-- b000302 | prose | pages [9] -->
𝐴𝑙𝑒𝑎𝑓

<!-- b000303 | prose | pages [9] -->
Now, we can develop a database of six most common leaves containing

<!-- b000304 | prose | pages [9] -->
seven parameters discussed above.

<!-- b000305 | prose | pages [9] -->
These are six most commonly seen leaf types in North America:

<!-- b000306 | furniture | pages [9] -->


<!-- b000307 | furniture | pages [9] -->


<!-- b000308 | prose | pages [9] -->
Database:

<!-- b000309 | prose | pages [9] -->
1

<!-- b000310 | prose | pages [9] -->
Rectangularity 0.6627

<!-- b000311 | prose | pages [9] -->
Aspect Ratio 0.8615

<!-- b000312 | prose | pages [9] -->
Circularity 0.8140

<!-- b000313 | prose | pages [9] -->
2 3 4 5 6

<!-- b000314 | prose | pages [9] -->
0.5902 0.6250 0.4772 0.4876 0.6576

<!-- b000315 | prose | pages [9] -->
0.6600 0.1800 0.6383 0.4792 0.3111

<!-- b000316 | prose | pages [9] -->
0.5432 0.4564 0.3454 0.3123 0.3311

<!-- b000317 | furniture | pages [10] -->
Team #14990

<!-- b000318 | prose | pages [10] -->
Form Factor 0.9139

<!-- b000319 | prose | pages [10] -->
ER Area Index 0.9322

<!-- b000320 | prose | pages [10] -->
ER Perimeter Index 0.8727

<!-- b000321 | prose | pages [10] -->
PI1 0.0649

<!-- b000322 | prose | pages [10] -->
PI2 0.2958

<!-- b000323 | prose | pages [10] -->
PI3 0.3439

<!-- b000324 | prose | pages [10] -->
PI4 0.2954

<!-- b000325 | furniture | pages [10] -->


<!-- b000326 | heading | pages [10] -->
5.2 Comparison

<!-- b000327 | furniture | pages [10] -->


<!-- b000328 | furniture | pages [10] -->
10 / 42

<!-- b000329 | furniture | pages [10] -->


<!-- b000330 | prose | pages [10] -->
0.6206 0.2823 0.2470 0.3662 0.4956

<!-- b000331 | prose | pages [10] -->
0.8780 0.9091 0.8500 0.7880 0.8895

<!-- b000332 | prose | pages [10] -->
0.8889 0.9384 0.8602 0.8231 0.9903

<!-- b000333 | prose | pages [10] -->
0.0769 0.1179 0.1909 0.1299 0.2920

<!-- b000334 | prose | pages [10] -->
0.3555 0.2208 0.3892 0.3606 0.4187

<!-- b000335 | prose | pages [10] -->
0.4243 0.4139 0.3047 0.4123 0.2677

<!-- b000336 | prose | pages [10] -->
0.1433 0.2474 0.1152 0.0970 0.0220

<!-- b000337 | prose | pages [10] -->
When given a specific leaf, we can calculate seven characteristics of it and

<!-- b000338 | prose | pages [10] -->
compare them with our database by calculating the squared deviation of each of

<!-- b000339 | prose | pages [10] -->
parameter of the given leaf from the corresponding standard parameter of each

<!-- b000340 | prose | pages [10] -->
category. We realize the fact that some of seven parameters are somehow more

<!-- b000341 | prose | pages [10] -->
important than others. So in an effort to make our model more accurate and

<!-- b000342 | prose | pages [10] -->
reliable, we induce the conception of the Index of Deviation, denoted as 𝑰𝑫,

<!-- b000343 | prose | pages [10] -->
which comes from the sum of the squared deviation between the database and

<!-- b000344 | prose | pages [10] -->
the leaf –to–be–classified times the proper weight.

<!-- b000345 | prose | pages [10] -->
7

<!-- b000346 | prose | pages [10] -->
𝐼𝐷= 𝐼𝑖∙𝑊𝑖

<!-- b000347 | prose | pages [10] -->
𝐈𝟏

<!-- b000348 | prose | pages [10] -->
𝐈𝟐

<!-- b000349 | prose | pages [10] -->
𝐈𝟑

<!-- b000350 | prose | pages [10] -->
𝐈𝟒

<!-- b000351 | prose | pages [10] -->
𝐈𝟓

<!-- b000352 | furniture | pages [10] -->


<!-- b000353 | prose | pages [10] -->
𝑖=1

<!-- b000354 | prose | pages [10] -->
(𝐑𝐧𝐞𝐰−𝐑)𝟐

<!-- b000355 | prose | pages [10] -->
(𝐀𝐑𝐧𝐞𝐰−𝐀𝐑)𝟐

<!-- b000356 | prose | pages [10] -->
(𝐂𝐧𝐞𝐰−𝐂)𝟐

<!-- b000357 | prose | pages [10] -->
(𝐅𝐅𝐧𝐞𝐰−𝐅𝐅)𝟐

<!-- b000358 | prose | pages [10] -->
(𝐄𝐑𝐀𝐈𝐧𝐞𝐰−𝐄𝐑𝐀𝐈)𝟐

<!-- b000359 | furniture | pages [11] -->
Team #14990

<!-- b000360 | prose | pages [11] -->
𝐈𝟔

<!-- b000361 | prose | pages [11] -->
𝐼7

<!-- b000362 | furniture | pages [11] -->


<!-- b000363 | furniture | pages [11] -->
11 / 42

<!-- b000364 | furniture | pages [11] -->


<!-- b000365 | prose | pages [11] -->
(𝐄𝐑𝐏𝐈𝐧𝐞𝐰−𝐄𝐑𝐏𝐈)𝟐

<!-- b000366 | prose | pages [11] -->
4

<!-- b000367 | prose | pages [11] -->
1 4 ∙ (𝑃𝐼𝑖𝑛𝑒𝑤−𝑃𝐼𝑖)2

<!-- b000368 | furniture | pages [11] -->


<!-- b000369 | prose | pages [11] -->
𝑖=1

<!-- b000370 | prose | pages [11] -->
In order to decide the respective weight more scientifically, we resort to the help

<!-- b000371 | prose | pages [11] -->
of Analytical Hierarchy Process.

<!-- b000372 | prose | pages [11] -->
AHP

<!-- b000373 | prose | pages [11] -->
First of all, we build a seven by seven matrix reciprocal matrix by pair

<!-- b000374 | prose | pages [11] -->
comparison:

<!-- b000375 | prose | pages [11] -->
R AR

<!-- b000376 | prose | pages [11] -->
Rectangularity 1 1/3

<!-- b000377 | prose | pages [11] -->
Aspect Ratio 3 1

<!-- b000378 | prose | pages [11] -->
Circularity 1 1/3

<!-- b000379 | prose | pages [11] -->
Form Factor 4 1

<!-- b000380 | prose | pages [11] -->
ER Area Index 2 1/2

<!-- b000381 | prose | pages [11] -->
ER Perimeter Index 2 1/2

<!-- b000382 | prose | pages [11] -->
Proportional Index 7 3

<!-- b000383 | prose | pages [11] -->
C C FF ERAI ERPI PI

<!-- b000384 | prose | pages [11] -->
1 1 1/4 1/2 1/2 1/7

<!-- b000385 | prose | pages [11] -->
3 3 1 2 2 1/3

<!-- b000386 | prose | pages [11] -->
1 1 1/4 1/2 1/2 1/7

<!-- b000387 | prose | pages [11] -->
4 4 1 3 3 1/2

<!-- b000388 | prose | pages [11] -->
2 2 1/3 1 1 1/4

<!-- b000389 | prose | pages [11] -->
2 2 1/3 1 1 1/4

<!-- b000390 | prose | pages [11] -->
7 7 2 4 4 1

<!-- b000391 | prose | pages [11] -->
*The number of each cell is explained in the following chart:

<!-- b000392 | prose | pages [11] -->
Intensity of Value Interpretation

<!-- b000393 | prose | pages [11] -->
Requirements i and j are of equal value. 1

<!-- b000394 | prose | pages [11] -->
Requirement i has a slightly higher value than j. 3

<!-- b000395 | prose | pages [11] -->
Requirement i has a strongly higher value than j. 5

<!-- b000396 | prose | pages [11] -->
Requirement i has a very strongly higher value than j. 7

<!-- b000397 | prose | pages [11] -->
Requirement i has an absolutely higher value than j. 9

<!-- b000398 | prose | pages [11] -->
These are intermediate scales between two adjacent judgments. 2, 4, 6, 8

<!-- b000399 | prose | pages [11] -->
If Requirement i has a lower value than j Reciprocals

<!-- b000400 | furniture | pages [11] -->


<!-- b000401 | prose | pages [11] -->
We then input Pair Ratio Matrix into computer program of MATLAB (Code

<!-- b000402 | prose | pages [11] -->
available in appendix), and get the weight of each factor (Wi).

<!-- b000403 | furniture | pages [12] -->
Team #14990

<!-- b000404 | prose | pages [12] -->
W1

<!-- b000405 | prose | pages [12] -->
W2

<!-- b000406 | prose | pages [12] -->
W3

<!-- b000407 | prose | pages [12] -->
W4

<!-- b000408 | prose | pages [12] -->
W5

<!-- b000409 | prose | pages [12] -->
W6

<!-- b000410 | prose | pages [12] -->
W7

<!-- b000411 | furniture | pages [12] -->


<!-- b000412 | furniture | pages [12] -->


<!-- b000413 | furniture | pages [12] -->
12 / 42

<!-- b000414 | furniture | pages [12] -->


<!-- b000415 | prose | pages [12] -->
0.0480

<!-- b000416 | prose | pages [12] -->
0.1583

<!-- b000417 | prose | pages [12] -->
0.0480

<!-- b000418 | prose | pages [12] -->
0.2048

<!-- b000419 | prose | pages [12] -->
0.0855

<!-- b000420 | prose | pages [12] -->
0.0855

<!-- b000421 | prose | pages [12] -->
0.3701

<!-- b000422 | prose | pages [12] -->
The following calculation is intended to test the consistency of the above AHP.

<!-- b000423 | prose | pages [12] -->
λmax = 7.0512

<!-- b000424 | prose | pages [12] -->
CI = λmax −n

<!-- b000425 | prose | pages [12] -->
= 0.0087 n −1

<!-- b000426 | prose | pages [12] -->
CR = CI

<!-- b000427 | prose | pages [12] -->
RI = 0.0064

<!-- b000428 | prose | pages [12] -->
CR < 0.01

<!-- b000429 | prose | pages [12] -->
So, the above method displays perfectly acceptable consistency and the weights

<!-- b000430 | prose | pages [12] -->
are reasonable.

<!-- b000431 | heading | pages [12] -->
5.3 Model Testing

<!-- b000432 | prose | pages [12] -->
Now we will take the maple leaf as an example to test

<!-- b000433 | prose | pages [12] -->
our leaf classification model. Before testing, we compare

<!-- b000434 | prose | pages [12] -->
this maple leaf with the six categories in our database

<!-- b000435 | prose | pages [12] -->
and find out that it resembles Category 4 most. Now we

<!-- b000436 | prose | pages [12] -->
will test our hypothesis with our model based on

<!-- b000437 | furniture | pages [13] -->
Team #14990

<!-- b000438 | prose | pages [13] -->
quantitative analysis.

<!-- b000439 | furniture | pages [13] -->


<!-- b000440 | furniture | pages [13] -->
13 / 42

<!-- b000441 | furniture | pages [13] -->


<!-- b000442 | prose | pages [13] -->
Firstly, process the image of a given maple leaf:

<!-- b000443 | prose | pages [13] -->
Then, calculate the rectangularity, aspect ratio, circularity, form factor, edge

<!-- b000444 | prose | pages [13] -->
regularity area index, edge regularity perimeter index and the proportional index

<!-- b000445 | prose | pages [13] -->
of the given leaf. In this case, the seven parameters are shown below:

<!-- b000446 | prose | pages [13] -->
Parameter

<!-- b000447 | prose | pages [13] -->
Rectangularity

<!-- b000448 | prose | pages [13] -->
Aspect Ratio

<!-- b000449 | prose | pages [13] -->
Circularity

<!-- b000450 | prose | pages [13] -->
Form Factor

<!-- b000451 | prose | pages [13] -->
ER Area Index

<!-- b000452 | prose | pages [13] -->
ER Perimeter Index

<!-- b000453 | prose | pages [13] -->
PI1

<!-- b000454 | prose | pages [13] -->
PI2

<!-- b000455 | prose | pages [13] -->
PI3

<!-- b000456 | prose | pages [13] -->
PI4

<!-- b000457 | furniture | pages [13] -->


<!-- b000458 | prose | pages [13] -->
Maple Leave

<!-- b000459 | prose | pages [13] -->
0.3554

<!-- b000460 | prose | pages [13] -->
0.9079

<!-- b000461 | prose | pages [13] -->
0.2691

<!-- b000462 | prose | pages [13] -->
0.1572

<!-- b000463 | prose | pages [13] -->
0.6248

<!-- b000464 | prose | pages [13] -->
0.3787

<!-- b000465 | prose | pages [13] -->
0.0968

<!-- b000466 | prose | pages [13] -->
0.4628

<!-- b000467 | prose | pages [13] -->
0.4311

<!-- b000468 | prose | pages [13] -->
0.0093

<!-- b000469 | prose | pages [13] -->
Finally, calculate the index of deviation by using the formula generated before.

<!-- b000470 | prose | pages [13] -->
7

<!-- b000471 | prose | pages [13] -->
𝐼𝑖∙𝑊𝑖

<!-- b000472 | furniture | pages [13] -->


<!-- b000473 | prose | pages [13] -->
𝑖=1

<!-- b000474 | prose | pages [13] -->
The six indexes of deviation after comparing the parameters of a given maple leaf

<!-- b000475 | prose | pages [13] -->
with the parameters of six categories in our database are shown below:

<!-- b000476 | prose | pages [13] -->
Maple Leave 1

<!-- b000477 | prose | pages [13] -->
I1

<!-- b000478 | prose | pages [13] -->
2 3 4 5 6

<!-- b000479 | prose | pages [13] -->
0.0026 0.0045

<!-- b000480 | prose | pages [13] -->
I2

<!-- b000481 | prose | pages [13] -->
0.0035 0.0007 0.0008 0.0044

<!-- b000482 | prose | pages [13] -->
0.0097 0.0003

<!-- b000483 | prose | pages [13] -->
I3

<!-- b000484 | prose | pages [13] -->
0.0839 0.0115 0.0291 0.0564

<!-- b000485 | prose | pages [13] -->
0.0043 0.0066

<!-- b000486 | prose | pages [13] -->
I4

<!-- b000487 | prose | pages [13] -->
0.0004 0.0001 0.0004 0.0000

<!-- b000488 | prose | pages [13] -->
0.0440 0.1173

<!-- b000489 | prose | pages [13] -->
I5

<!-- b000490 | prose | pages [13] -->
0.0032 0.0017 0.0090 0.0235

<!-- b000491 | prose | pages [13] -->
0.0055 0.0081

<!-- b000492 | prose | pages [13] -->
I6

<!-- b000493 | prose | pages [13] -->
0.0069 0.0043 0.0023 0.0060

<!-- b000494 | prose | pages [13] -->
0.0223 0.0209

<!-- b000495 | prose | pages [13] -->
I7

<!-- b000496 | prose | pages [13] -->
0.0268 0.0198 0.0169 0.0320

<!-- b000497 | prose | pages [13] -->
0.0277 0.1095

<!-- b000498 | prose | pages [13] -->
𝐈𝑫

<!-- b000499 | prose | pages [13] -->
0.1073 0.0384 0.1817 0.0619

<!-- b000500 | prose | pages [13] -->
0.1161 0.2672 0.2319 0.0765 0.2402 0.1841

<!-- b000501 | furniture | pages [14] -->
Team #14990

<!-- b000502 | furniture | pages [14] -->


<!-- b000503 | furniture | pages [14] -->
14 / 42

<!-- b000504 | furniture | pages [14] -->


<!-- b000505 | furniture | pages [14] -->


<!-- b000506 | prose | pages [14] -->
Since the index of deviation between the given maple leaf and Category 4 is

<!-- b000507 | prose | pages [14] -->
smallest, the maple leaf falls into Category 4, which is consistent with our

<!-- b000508 | prose | pages [14] -->
hypothesis.

<!-- b000509 | heading | pages [14] -->
5.4 Conclusion

<!-- b000510 | prose | pages [14] -->
So far, our model has solved the problem of classification very well based on

<!-- b000511 | prose | pages [14] -->
seven well-rounded parameters and a functional database. Through this

<!-- b000512 | prose | pages [14] -->
quantitative model, we can decide the general shape of any given leaf reliably

<!-- b000513 | prose | pages [14] -->
and scientifically. Our model is robust under reasonable conditions, which can be

<!-- b000514 | prose | pages [14] -->
seen through the testing part discussed above. However, since our database

<!-- b000515 | prose | pages [14] -->
contains only the six commonly seen leaf types in North America, the variety of

<!-- b000516 | prose | pages [14] -->
database itself still has room for improvement. With the more and more different

<!-- b000517 | prose | pages [14] -->
leaf species added to the database, our model can apply to a wider and more

<!-- b000518 | prose | pages [14] -->
geographically comprehensive scope.

<!-- b000519 | furniture | pages [14] -->


<!-- b000520 | heading | pages [14] -->
6. Model Two: Leaf Distribution and Leaf Shape

<!-- b000521 | heading | pages [14] -->
6.1 Introduction

<!-- b000522 | prose | pages [14] -->
Leaf shape varies so greatly that it still remains a mystery why leaves display such

<!-- b000523 | prose | pages [14] -->
a immense variety of shape. Leaf veins are the skeleton of a leaf, and ground

<!-- b000524 | prose | pages [14] -->
tissues the muscles. Genetic and environmental factors contribute to the

<!-- b000525 | prose | pages [14] -->
different patterns of leaf veins and ground tissue, thereby determining the leaf

<!-- b000526 | prose | pages [14] -->
shape. In this model, we narrow the big picture into how leaf distribution act as

<!-- b000527 | prose | pages [14] -->
an influence on leaf shape.

<!-- b000528 | heading | pages [14] -->
6.2 Idealized Leaf Distribution Model

<!-- b000529 | prose | pages [14] -->
To downplay the effects of miscellaneous factors that contribute to the relation

<!-- b000530 | prose | pages [14] -->
between the distribution and shape of a leaf, we construct an idealized model

<!-- b000531 | prose | pages [14] -->
that immensely simplifies the complex condition.

<!-- b000532 | prose | pages [14] -->
The tree is made up of a branch perpendicular to the ground surface and two

<!-- b000533 | prose | pages [14] -->
identical leaves grown on the branch ipsilaterally and horizontally. The leaves face

<!-- b000534 | prose | pages [14] -->
upward and point toward the sun in the sky.

<!-- b000535 | furniture | pages [15] -->
Team #14990

<!-- b000536 | furniture | pages [15] -->


<!-- b000537 | furniture | pages [15] -->
15 / 42

<!-- b000538 | furniture | pages [15] -->


<!-- b000539 | prose | pages [15] -->
We suppose the tree is placed on the latitude of L (Northern). So the greatest

<!-- b000540 | prose | pages [15] -->
average solar altitude in a year, which is attained in the noon of Vernal Equinox, is

<!-- b000541 | prose | pages [15] -->
defined as α.

<!-- b000542 | prose | pages [15] -->
The above information is explained in the following image:

<!-- b000543 | furniture | pages [15] -->


<!-- b000544 | furniture | pages [15] -->


<!-- b000545 | heading | pages [15] -->
6.3 Analysis of Overlapping Areas

<!-- b000546 | prose | pages [15] -->
Our key focus of the study is the partly shaded leaf. What proportion of the leaf

<!-- b000547 | prose | pages [15] -->
(PL) is shaded is the output of the model. The solar attitude α is a critical control

<!-- b000548 | prose | pages [15] -->
variable. According to the influence of the angle on PL, we divide α into three

<!-- b000549 | prose | pages [15] -->
scenarios.

<!-- b000550 | prose | pages [15] -->
6.3.1 Solar Altitude trending toward 90°

<!-- b000551 | prose | pages [15] -->
The situation in which α is trending toward 90°usually takes place in tropical

<!-- b000552 | prose | pages [15] -->
regions. And it is very clear through observation that, in tropical regions, leaf

<!-- b000553 | prose | pages [15] -->
shapes are typically broad and wide with the tree crowns usually containing only

<!-- b000554 | prose | pages [15] -->
one layer of leaves. This can be explained through the illustration above as the

<!-- b000555 | furniture | pages [16] -->
Team #14990

<!-- b000556 | furniture | pages [16] -->


<!-- b000557 | furniture | pages [16] -->
16 / 42

<!-- b000558 | furniture | pages [16] -->


<!-- b000559 | prose | pages [16] -->
shaded part of the lower leaf would be too big with α trending toward 90°to

<!-- b000560 | prose | pages [16] -->
supply enough solar energy for photosynthesis and the biggest absorption of

<!-- b000561 | prose | pages [16] -->
energy can be achieved by a broad leaf shape.

<!-- b000562 | prose | pages [16] -->
6.3.2 Solar Altitude trending toward 0°

<!-- b000563 | prose | pages [16] -->
The situation in which α is trending toward 0°usually takes place in frigid zones. It

<!-- b000564 | prose | pages [16] -->
is also very clear that in these regions, leaves are typically acicular with the tree

<!-- b000565 | prose | pages [16] -->
crowns containing dense layers of closely grown leaves. This can also be

<!-- b000566 | prose | pages [16] -->
explained through the illustration above as the shaded part of the lower leaf

<!-- b000567 | prose | pages [16] -->
would approach zero with α trending toward 0°, allowing a much more

<!-- b000568 | prose | pages [16] -->
concentrated distribution of leaves than in other situations. In addition, the

<!-- b000569 | prose | pages [16] -->
maximum absorption of energy can be best achieved by needle-like leaves.

<!-- b000570 | prose | pages [16] -->
6.3.3 Solar Altitude within normal range

<!-- b000571 | prose | pages [16] -->
This scenario is typical in the temperate zone on earth, where sunlight irradiates

<!-- b000572 | prose | pages [16] -->
the leaves in a tilted way. It is also the case in which our idealized model is the

<!-- b000573 | prose | pages [16] -->
most suitable. Another crucial factor that we control in this case is the distance

<!-- b000574 | prose | pages [16] -->
(h) between the two points connecting the leaves and the branch.

<!-- b000575 | prose | pages [16] -->
Our aim is to discuss the relationship between the leaf shape and the leaf

<!-- b000576 | prose | pages [16] -->
distribution. We assume a tree’s leaf distribution will try to minimize the

<!-- b000577 | prose | pages [16] -->
overlapping area between leaves, so our model will try to find out the

<!-- b000578 | prose | pages [16] -->
quantitative relationship between the overlapping area and the shape of leaf.

<!-- b000579 | prose | pages [16] -->
In order to simplify the model, we use the rhombus, with the length of major axis

<!-- b000580 | prose | pages [16] -->
denoted as Lmajor and the length of minor axis denoted as Lminor , to replace

<!-- b000581 | prose | pages [16] -->
the leaf shape. Also, we control the area of the first leaf to ensure its constant

<!-- b000582 | prose | pages [16] -->
exposure area to the sun. Since the area is fixed, now we only need to change

<!-- b000583 | prose | pages [16] -->
the length of the major axis to change the shape of the leaf. In other words,

<!-- b000584 | prose | pages [16] -->
during our later study, we will use the change of Lmajor to symbolize the change

<!-- b000585 | prose | pages [16] -->
of the leaf shape.

<!-- b000586 | furniture | pages [17] -->
Team #14990

<!-- b000587 | furniture | pages [17] -->


<!-- b000588 | furniture | pages [17] -->
17 / 42

<!-- b000589 | furniture | pages [17] -->


<!-- b000590 | furniture | pages [17] -->


<!-- b000591 | prose | pages [17] -->
Also, since we have fixed the area of the leaf and just change its shape during our

<!-- b000592 | prose | pages [17] -->
study, the smallest overlapping area, which we denote as  Aoverlapping , means

<!-- b000593 | prose | pages [17] -->
the smallest ration of E, which is defined as follows:

<!-- b000594 | prose | pages [17] -->
Aoverlapping

<!-- b000595 | prose | pages [17] -->
E =

<!-- b000596 | prose | pages [17] -->
area of one leaf

<!-- b000597 | prose | pages [17] -->
Obviously, the most efficient and effective way for two leaves to distribute is to

<!-- b000598 | prose | pages [17] -->
be just totally exposed in sunlight as illustrated below, when h=h0 and E=0. Thus,

<!-- b000599 | prose | pages [17] -->
the tree can take whatever shape it wants since we control the leaf’s surface

<!-- b000600 | prose | pages [17] -->
area.

<!-- b000601 | prose | pages [17] -->
h0

<!-- b000602 | furniture | pages [18] -->
Team #14990

<!-- b000603 | furniture | pages [18] -->


<!-- b000604 | furniture | pages [18] -->
18 / 42

<!-- b000605 | furniture | pages [18] -->


<!-- b000606 | prose | pages [18] -->
Now, we want to study what if h<h0 .

<!-- b000607 | prose | pages [18] -->
If h< h0, there will be a shaded region  Aoverlapping .  The stress of the following

<!-- b000608 | prose | pages [18] -->
study is analyzing the relation between h, Lmajor and E when given a fixed

<!-- b000609 | prose | pages [18] -->
solar altitude α.

<!-- b000610 | furniture | pages [18] -->


<!-- b000611 | prose | pages [18] -->
We can easily give the relationship between these factors according to their

<!-- b000612 | prose | pages [18] -->
geometric features:

<!-- b000613 | prose | pages [18] -->
Lmajor ∙tanα −h

<!-- b000614 | prose | pages [18] -->
E = (

<!-- b000615 | prose | pages [18] -->
)2 L ∙tanα

<!-- b000616 | prose | pages [18] -->
h

<!-- b000617 | prose | pages [18] -->
Lmajor ∙tan α)2

<!-- b000618 | prose | pages [18] -->
Namely                    E = (1 −

<!-- b000619 | furniture | pages [18] -->


<!-- b000620 | prose | pages [18] -->
Where tanα is a constant.

<!-- b000621 | prose | pages [18] -->
When we fix the value of h and give α a particular value, we can get the

<!-- b000622 | prose | pages [18] -->
relationship between the length of leaf and the overlapping area:

<!-- b000623 | furniture | pages [19] -->
Team #14990

<!-- b000624 | prose | pages [19] -->
*x-axis refers to Lmajor

<!-- b000625 | prose | pages [19] -->
y-axis refers to  Aoverlapping

<!-- b000626 | furniture | pages [19] -->


<!-- b000627 | furniture | pages [19] -->
19 / 42

<!-- b000628 | furniture | pages [19] -->


<!-- b000629 | prose | pages [19] -->
We discover from the function above that the closer the  Lmajor approaches L ∙

<!-- b000630 | prose | pages [19] -->
tanα, which is equal to h0, the smaller the overlapping area will be.

<!-- b000631 | prose | pages [19] -->
So far, we have considered the both situations when h=h0 and h<h0. From what

<!-- b000632 | prose | pages [19] -->
we discussed above, the best leaf distribution of the leaf occurs when h=h0,

<!-- b000633 | prose | pages [19] -->
which means

<!-- b000634 | prose | pages [19] -->
h = Lmajor ∙tanα

<!-- b000635 | furniture | pages [19] -->


<!-- b000636 | prose | pages [19] -->
6.4

<!-- b000637 | heading | pages [19] -->
Model Testing

<!-- b000638 | prose | pages [19] -->
Now, we need to test whether this correlation between the leaf distribution and

<!-- b000639 | prose | pages [19] -->
leaf shape is right.  We collect the data of the length (Lmajor ) and internode (h)

<!-- b000640 | prose | pages [19] -->
of a variety of trees and use our formula to calculate the respective solar altitude

<!-- b000641 | prose | pages [19] -->
of the trees. By converting the solar altitude into latitude, we can predict the

<!-- b000642 | prose | pages [19] -->
origin of this particular tree.  We choose   Ligustrum quihoui Carr, Osmanthus

<!-- b000643 | prose | pages [19] -->
fragrans and Camellia japonica as our test objects and here is the result of our

<!-- b000644 | prose | pages [19] -->
testing:

<!-- b000645 | prose | pages [19] -->
Lmajor Test Object Ligustrum quihoui Carr.

<!-- b000646 | prose | pages [19] -->
2 2.5 tanα h h Predicted Latitude True Lattitude 1.25 38.65 35~35 18.5 Osmanthus fragrans 10 Camellia japonica 6

<!-- b000647 | furniture | pages [19] -->


<!-- b000648 | prose | pages [19] -->
1.85 28.39 23~29 9 9 1.50 33.69 32~36

<!-- b000649 | prose | pages [19] -->
From the table, we can see that our predicted latitude of origin is always within the range of its true latitude, so it is safe to say that the correlation between leaf distribution and leaf shape generated by our model is reliable and correct. In other words, there does exist a relationship between the leaf distribution and leaf shape.

<!-- b000650 | furniture | pages [19] -->


<!-- b000651 | heading | pages [19] -->
7. Model Three: Tree Profile and Leaf Shape

<!-- b000652 | heading | pages [19] -->
7.1 Introduction

<!-- b000653 | prose | pages [19] -->
In this part of our paper, we will explore the correlation between the tree profile

<!-- b000654 | prose | pages [19] -->
and the leaf shape. When we classify the leaf in model one, we define a set of

<!-- b000655 | prose | pages [19] -->
parameters to better understand the shape of leaf on a quantitative base.

<!-- b000656 | furniture | pages [20] -->
Team #14990

<!-- b000657 | furniture | pages [20] -->


<!-- b000658 | furniture | pages [20] -->
20 / 42

<!-- b000659 | furniture | pages [20] -->


<!-- b000660 | prose | pages [20] -->
Similarly, we will apply this method to explore the profile of tree.

<!-- b000661 | heading | pages [20] -->
7.2 Hypothesis

<!-- b000662 | prose | pages [20] -->
Since the vein structure determines the leaf shape and the branch structure

<!-- b000663 | prose | pages [20] -->
determines the tree profile and, to some degree, the leaf veins resemble the

<!-- b000664 | prose | pages [20] -->
branches（refer to figure 3.1）,we have a wild hypothesis that, leaf shape be a

<!-- b000665 | prose | pages [20] -->
two-dimensional mimic of the tree profile. In other words, there does exist a

<!-- b000666 | prose | pages [20] -->
correlation between the leaf shape and the tree profile.

<!-- b000667 | furniture | pages [20] -->


<!-- b000668 | furniture | pages [20] -->


<!-- b000669 | heading | pages [20] -->
7.3 Comparison of Leaf Shape and Tree Contour

<!-- b000670 | prose | pages [20] -->
In an effort to judge whether our hypothesis is true or not, our model’s general

<!-- b000671 | prose | pages [20] -->
idea is to compare some specific parameters between the tree profile and the

<!-- b000672 | prose | pages [20] -->
leaf shape, thus determine whether a relation exists.

<!-- b000673 | prose | pages [20] -->
The leaf shape is two-dimensional, so it is relatively easy to study its parameters.

<!-- b000674 | prose | pages [20] -->
However, the tree profile is three dimensional, so it is important to find out a

<!-- b000675 | prose | pages [20] -->
two-dimensional characteristic of a tree to study its parameters. Since the

<!-- b000676 | prose | pages [20] -->
longitudinal section of a particular tree reflects the general size characteristics of

<!-- b000677 | prose | pages [20] -->
a grown tree, we choose to focus on it in our later study and analysis.

<!-- b000678 | prose | pages [20] -->
7.3.1 Tree Profile Classification

<!-- b000679 | furniture | pages [21] -->
Team #14990

<!-- b000680 | furniture | pages [21] -->


<!-- b000681 | furniture | pages [21] -->
21 / 42

<!-- b000682 | furniture | pages [21] -->


<!-- b000683 | prose | pages [21] -->
In the leaf classification model, there are 6 general classes of leaves.

<!-- b000684 | prose | pages [21] -->
Since we only compare the general resemblance between leaf and tree,

<!-- b000685 | prose | pages [21] -->
class five (elliptic leaf with serrated margin) is incorporated into class two.

<!-- b000686 | prose | pages [21] -->
As a result, we get 5 classes of leaves and 5 respective types of trees.

<!-- b000687 | prose | pages [21] -->
Class 1 Cordate (Texas Redbud):

<!-- b000688 | furniture | pages [21] -->


<!-- b000689 | furniture | pages [21] -->


<!-- b000690 | prose | pages [21] -->
Class 2 Elliptic (Camphor Tree):

<!-- b000691 | furniture | pages [21] -->


<!-- b000692 | furniture | pages [21] -->


<!-- b000693 | furniture | pages [22] -->
Team #14990

<!-- b000694 | furniture | pages [22] -->


<!-- b000695 | furniture | pages [22] -->


<!-- b000696 | furniture | pages [22] -->
22 / 42

<!-- b000697 | furniture | pages [22] -->


<!-- b000698 | prose | pages [22] -->
Class 3 Subulate (Pine Tree)：

<!-- b000699 | furniture | pages [22] -->


<!-- b000700 | furniture | pages [22] -->


<!-- b000701 | furniture | pages [22] -->


<!-- b000702 | prose | pages [22] -->
Class 4 Palmate (Oak Tree)：

<!-- b000703 | furniture | pages [22] -->


<!-- b000704 | furniture | pages [22] -->


<!-- b000705 | furniture | pages [22] -->


<!-- b000706 | furniture | pages [23] -->
Team #14990

<!-- b000707 | furniture | pages [23] -->


<!-- b000708 | furniture | pages [23] -->
23 / 42

<!-- b000709 | furniture | pages [23] -->


<!-- b000710 | prose | pages [23] -->
Class 5 Obovate (Mockernut Hickory)：

<!-- b000711 | prose | pages [23] -->
7.3.2 Parameters of the tree

<!-- b000712 | furniture | pages [23] -->


<!-- b000713 | prose | pages [23] -->
According to the data we get and referring to the parameters we set for

<!-- b000714 | prose | pages [23] -->
the leaf, this time we appoint 3 parameters for the longitudinal section

<!-- b000715 | prose | pages [23] -->
that can be compared with those of the leaf shape, namely the

<!-- b000716 | prose | pages [23] -->
rectangularity, the aspect ratio and circularity. Since we have discussed

<!-- b000717 | prose | pages [23] -->
these three parameters in detail before, we will just briefly go through

<!-- b000718 | prose | pages [23] -->
them.

<!-- b000719 | prose | pages [23] -->
A. Rectangularity

<!-- b000720 | prose | pages [23] -->
Rectangularity is defined as the ratio between the longitudinal section

<!-- b000721 | prose | pages [23] -->
area of a tree and the area of the smallest bounding rectangle area.

<!-- b000722 | prose | pages [23] -->
First we compare the rectangularity of the tree profile with that of leaf

<!-- b000723 | prose | pages [23] -->
we calculated in model 1 in the following chart.

<!-- b000724 | prose | pages [23] -->
Class

<!-- b000725 | prose | pages [23] -->
1

<!-- b000726 | prose | pages [23] -->
2

<!-- b000727 | prose | pages [23] -->
3

<!-- b000728 | prose | pages [23] -->
4

<!-- b000729 | prose | pages [23] -->
5

<!-- b000730 | furniture | pages [23] -->


<!-- b000731 | prose | pages [23] -->
Leaf Tree

<!-- b000732 | prose | pages [23] -->
0.6627 0.6281

<!-- b000733 | prose | pages [23] -->
0.5902 0.6846

<!-- b000734 | prose | pages [23] -->
0.6250 0.5180

<!-- b000735 | prose | pages [23] -->
0.4772 0.5292

<!-- b000736 | prose | pages [23] -->
0.6576 0.6238

<!-- b000737 | furniture | pages [24] -->
Team #14990

<!-- b000738 | furniture | pages [24] -->


<!-- b000739 | furniture | pages [24] -->
24 / 42

<!-- b000740 | furniture | pages [24] -->


<!-- b000741 | prose | pages [24] -->
Second, we draw a scatter plot with the independent variable of leaf and

<!-- b000742 | prose | pages [24] -->
the dependent variable of tree and use MATLAB to construct the linear

<!-- b000743 | prose | pages [24] -->
regression of the data. The following plot shows the fitting relationship

<!-- b000744 | prose | pages [24] -->
of the data.

<!-- b000745 | furniture | pages [24] -->


<!-- b000746 | prose | pages [24] -->
Y = 0.3905x + 0.3614

<!-- b000747 | prose | pages [24] -->
Also, we use F-test to test the significance of the linear regression:

<!-- b000748 | prose | pages [24] -->
r^2=0.1783

<!-- b000749 | prose | pages [24] -->
F=0.63

<!-- b000750 | prose | pages [24] -->
P=0.4850

<!-- b000751 | prose | pages [24] -->
Obviously, the test shows that the linear relationship between the

<!-- b000752 | prose | pages [24] -->
rectangularity of leaf and rectangularity of tree is insignificant.

<!-- b000753 | prose | pages [24] -->
B. Aspect ratio

<!-- b000754 | prose | pages [24] -->
Aspect ratio is defined as the ration between the short side and the long

<!-- b000755 | prose | pages [24] -->
side of the smallest bounding rectangle area.

<!-- b000756 | prose | pages [24] -->
The comparison chart is shown below.

<!-- b000757 | furniture | pages [25] -->
Team #14990

<!-- b000758 | prose | pages [25] -->
Class

<!-- b000759 | prose | pages [25] -->
1

<!-- b000760 | prose | pages [25] -->
2

<!-- b000761 | prose | pages [25] -->
3

<!-- b000762 | prose | pages [25] -->
4

<!-- b000763 | prose | pages [25] -->
5

<!-- b000764 | furniture | pages [25] -->


<!-- b000765 | furniture | pages [25] -->


<!-- b000766 | furniture | pages [25] -->
25 / 42

<!-- b000767 | furniture | pages [25] -->


<!-- b000768 | prose | pages [25] -->
Leaf Tree

<!-- b000769 | prose | pages [25] -->
0.8615 0.7914

<!-- b000770 | prose | pages [25] -->
0.6600 0.7243

<!-- b000771 | prose | pages [25] -->
0.1800 0.6601

<!-- b000772 | prose | pages [25] -->
0.6383 0.7980

<!-- b000773 | prose | pages [25] -->
0.3111 0.6750

<!-- b000774 | prose | pages [25] -->
Using the same statistical method, we construct the following plot.

<!-- b000775 | furniture | pages [25] -->


<!-- b000776 | furniture | pages [25] -->


<!-- b000777 | prose | pages [25] -->
Y = 0.2055x + 0.6208

<!-- b000778 | prose | pages [25] -->
This time the result of statistical inference is as follows:

<!-- b000779 | prose | pages [25] -->
r^2=0.7985

<!-- b000780 | prose | pages [25] -->
F=11.8857

<!-- b000781 | prose | pages [25] -->
P=0.041<0.05

<!-- b000782 | prose | pages [25] -->
As P value is within acceptance range, the linear relationship between

<!-- b000783 | prose | pages [25] -->
Aspect Ratio of leaf and that of tree.

<!-- b000784 | furniture | pages [26] -->
Team #14990

<!-- b000785 | prose | pages [26] -->
C. Circularity

<!-- b000786 | furniture | pages [26] -->


<!-- b000787 | furniture | pages [26] -->
26 / 42

<!-- b000788 | furniture | pages [26] -->


<!-- b000789 | prose | pages [26] -->
Circularity is defined as the ratio between the radius of in-circle and

<!-- b000790 | prose | pages [26] -->
ex-circle of the area of interest.

<!-- b000791 | prose | pages [26] -->
Class 1 2 3 4 5 Leaf Tree 0.6396  0.5800 0.5698  0.5928 0.1834  0.2895 0.3069  0.4070 0.2889  0.3866

<!-- b000792 | prose | pages [26] -->
Using Matlab, we construct the following plot.

<!-- b000793 | prose | pages [26] -->
Y= 0.6567x + 0.1900

<!-- b000794 | prose | pages [26] -->
The F-test shows the following.

<!-- b000795 | prose | pages [26] -->
r^2=0.9645

<!-- b000796 | prose | pages [26] -->
F=81.5595

<!-- b000797 | prose | pages [26] -->
P=0.0029<0.05

<!-- b000798 | prose | pages [26] -->
The P value small enough for us to say that there exists a linear

<!-- b000799 | prose | pages [26] -->
relationship between the circularity of the tree and the leaf.

<!-- b000800 | furniture | pages [27] -->
Team #14990

<!-- b000801 | furniture | pages [27] -->


<!-- b000802 | furniture | pages [27] -->
27 / 42

<!-- b000803 | furniture | pages [27] -->


<!-- b000804 | heading | pages [27] -->
7.4 Conclusion

<!-- b000805 | prose | pages [27] -->
From the test of the above three parameters, we may conclude that leaf shape

<!-- b000806 | prose | pages [27] -->
and tree profile have a possibly relationship between each other. Although the

<!-- b000807 | prose | pages [27] -->
test of rectangularity does not support our hypothesis, the test of aspect ratio

<!-- b000808 | prose | pages [27] -->
and the test of circularity well corroborate the theory that leaf shape is a

<!-- b000809 | prose | pages [27] -->
two-dimensional mimic of the tree contour. Since, the tree shape and leaf shape

<!-- b000810 | prose | pages [27] -->
both are affected by an great deal of genetic and environmental factors, the

<!-- b000811 | prose | pages [27] -->
shape characteristics of tree may not well reflect the tree shape. But as far as we

<!-- b000812 | prose | pages [27] -->
know, the shape of leaf resembles the shape of tree to some extent.

<!-- b000813 | furniture | pages [27] -->


<!-- b000814 | heading | pages [27] -->
8. Model Four: Leaf Mass

<!-- b000815 | heading | pages [27] -->
8.1 Introduction

<!-- b000816 | prose | pages [27] -->
In order to estimate the mass of the leaves of a certain tree when given the size

<!-- b000817 | prose | pages [27] -->
characteristics, we have developed a model based on a database.

<!-- b000818 | prose | pages [27] -->
One simple way to calculate the total leaf mass of a tree is to simply multiply the

<!-- b000819 | prose | pages [27] -->
number of the leaves on a tree and the mass of a single leaf. Our method is more

<!-- b000820 | prose | pages [27] -->
accurate and less demanding in that our model is independent of these two

<!-- b000821 | prose | pages [27] -->
factors, namely the number of leaves and the net weight of one single leaf, but

<!-- b000822 | prose | pages [27] -->
dependent on one more reliable factor of a grown tree --- photosynthesis.

<!-- b000823 | prose | pages [27] -->
Our methodology of estimating the leave mass of a tree is based on three

<!-- b000824 | prose | pages [27] -->
variables: tree age and growth rate, which is determined by tree species, and

<!-- b000825 | prose | pages [27] -->
general type (Hardwood or conifer). In other words, given the age and type of a

<!-- b000826 | prose | pages [27] -->
tree, we are able to estimate the total mass of leaves. In this model, CO2 is used

<!-- b000827 | prose | pages [27] -->
as a calculating media.

<!-- b000828 | prose | pages [27] -->
After the explanation of the model, we try to study if there is a correlation

<!-- b000829 | prose | pages [27] -->
between leaf mass size characteristics of a tree. The answer is positive, which we

<!-- b000830 | prose | pages [27] -->
use tree age as a link to prove.

<!-- b000831 | heading | pages [27] -->
8.2 Leaf Mass and Tree Age

<!-- b000832 | prose | pages [27] -->
8.2.1 Leaf Mass and CO2 Sequestration

<!-- b000833 | prose | pages [27] -->
First of all, according to the information we acquired from the past

<!-- b000834 | prose | pages [27] -->
researches, we divide the tree into two main types based on their

<!-- b000835 | prose | pages [27] -->
different ability of sequestering carbon dioxide from the atmosphere.

<!-- b000836 | furniture | pages [28] -->
Team #14990

<!-- b000837 | furniture | pages [28] -->


<!-- b000838 | furniture | pages [28] -->
28 / 42

<!-- b000839 | furniture | pages [28] -->


<!-- b000840 | prose | pages [28] -->
These two types and their respective ability are shown below:

<!-- b000841 | furniture | pages [28] -->


<!-- b000842 | prose | pages [28] -->
Hardwood Conifer

<!-- b000843 | prose | pages [28] -->
Ability to sequester Carbon 0.00250 0.00165 Dioxide  ( lbs of CO2/g of leaf)

<!-- b000844 | furniture | pages [28] -->


<!-- b000845 | prose | pages [28] -->
**A tree’s ability to sequester the carbon dioxide is different from its

<!-- b000846 | prose | pages [28] -->
ability to absorb it since the tree also releases CO2 into the atmosphere

<!-- b000847 | prose | pages [28] -->
all day round because of the respiration. In other words, CO2

<!-- b000848 | prose | pages [28] -->
sequestration = CO2 absorption – CO2 release.

<!-- b000849 | prose | pages [28] -->
Now we only need to decide the weight of carbon dioxide sequestered by

<!-- b000850 | prose | pages [28] -->
the tree and use the converting method below to calculate the total mass

<!-- b000851 | prose | pages [28] -->
of leaves of that tree.

<!-- b000852 | prose | pages [28] -->
𝑀𝑙𝑒𝑎𝑓= 𝑀𝑐𝑎𝑟𝑏𝑜𝑛 𝑑𝑖𝑜𝑥𝑖𝑑𝑒

<!-- b000853 | prose | pages [28] -->
In which,

<!-- b000854 | furniture | pages [28] -->


<!-- b000855 | prose | pages [28] -->
𝐴𝑠

<!-- b000856 | prose | pages [28] -->
𝑀𝑙𝑒𝑎𝑓:total mass of leaves (g)

<!-- b000857 | prose | pages [28] -->
𝑀𝑐𝑎𝑟𝑏𝑜𝑛 𝑑𝑖𝑜𝑥𝑖𝑑𝑒:mass of carbon dioxide sequestered (lbs)

<!-- b000858 | prose | pages [28] -->
𝐴𝑠:ability to sequester carbon dioxide (lbs/g)

<!-- b000859 | prose | pages [28] -->
8.2.2 CO2 Sequestration and Tree Age

<!-- b000860 | prose | pages [28] -->
The relationship between the amount of CO2 sequestered, the age of a

<!-- b000861 | prose | pages [28] -->
tree and the type of tree is shown in a study published by U.S.

<!-- b000862 | prose | pages [28] -->
Department of Energy in April 1998. The study below divided the growth

<!-- b000863 | prose | pages [28] -->
rate of a certain tree into three categories: fast, moderate and slow. The

<!-- b000864 | prose | pages [28] -->
corresponding chart that categorizes different tree species into 3 grow

<!-- b000865 | prose | pages [28] -->
rates is enclosed in the Appendix 1.

<!-- b000866 | furniture | pages [28] -->


<!-- b000867 | furniture | pages [28] -->


<!-- b000868 | furniture | pages [28] -->


<!-- b000869 | furniture | pages [28] -->


<!-- b000870 | furniture | pages [28] -->


<!-- b000871 | furniture | pages [28] -->


<!-- b000872 | furniture | pages [29] -->
Team #14990

<!-- b000873 | furniture | pages [29] -->


<!-- b000874 | furniture | pages [29] -->
29 / 42

<!-- b000875 | furniture | pages [29] -->


<!-- b000876 | furniture | pages [29] -->


<!-- b000877 | furniture | pages [29] -->


<!-- b000878 | furniture | pages [29] -->


<!-- b000879 | furniture | pages [29] -->


<!-- b000880 | furniture | pages [29] -->


<!-- b000881 | furniture | pages [29] -->


<!-- b000882 | furniture | pages [29] -->


<!-- b000883 | furniture | pages [29] -->


<!-- b000884 | furniture | pages [30] -->
Team #14990

<!-- b000885 | furniture | pages [30] -->


<!-- b000886 | furniture | pages [30] -->
30 / 42

<!-- b000887 | furniture | pages [30] -->


<!-- b000888 | furniture | pages [30] -->


<!-- b000889 | furniture | pages [30] -->


<!-- b000890 | furniture | pages [30] -->


<!-- b000891 | prose | pages [30] -->
From the chart, we can discover an obvious positive relationship

<!-- b000892 | prose | pages [30] -->
between the age of the tree and the amount of CO2 sequestered if we fix

<!-- b000893 | prose | pages [30] -->
the growth rate and the type of the tree. We fit the data into a set of

<!-- b000894 | prose | pages [30] -->
quadratic regression functions shown below:

<!-- b000895 | furniture | pages [30] -->


<!-- b000896 | furniture | pages [31] -->
Team #14990

<!-- b000897 | furniture | pages [31] -->


<!-- b000898 | furniture | pages [31] -->
31 / 42

<!-- b000899 | furniture | pages [31] -->


<!-- b000900 | furniture | pages [31] -->


<!-- b000901 | furniture | pages [31] -->


<!-- b000902 | prose | pages [31] -->
In each function next to the curve, such as y=0.0073x^2+0.9690x+1.0953,

<!-- b000903 | prose | pages [31] -->
which describes Annual Sequestration Rate for fast-growing Hardwood, y

<!-- b000904 | prose | pages [31] -->
is the sequestration rate and x is the tree age.

<!-- b000905 | prose | pages [31] -->
After fitting the data and conduct the statistical inference, we surprisingly

<!-- b000906 | prose | pages [31] -->
find that the fitting curve can actually fit the data perfectly. With the

<!-- b000907 | prose | pages [31] -->
fitting curve and the functions, we can easily estimate the CO2

<!-- b000908 | prose | pages [31] -->
sequestered when given the age of a certain tree.

<!-- b000909 | furniture | pages [32] -->
Team #14990

<!-- b000910 | prose | pages [32] -->
8.2.3 Leaf Mass and Tree Age

<!-- b000911 | furniture | pages [32] -->


<!-- b000912 | furniture | pages [32] -->
32 / 42

<!-- b000913 | furniture | pages [32] -->


<!-- b000914 | prose | pages [32] -->
Since we have known the converting relation between the mass of leaves

<!-- b000915 | prose | pages [32] -->
and the CO2 sequestered, now we can derive the correlation between

<!-- b000916 | prose | pages [32] -->
the age of a tree and the total mass of leaves on that tree by using the

<!-- b000917 | prose | pages [32] -->
CO2 sequestered as a media. After processing the data by the formula in

<!-- b000918 | prose | pages [32] -->
8.2.1, we get the corresponding relation table shown below. Each cell of

<!-- b000919 | prose | pages [32] -->
the table is the leaf mass of a tree of a certain age, type and growth rate.

<!-- b000920 | prose | pages [32] -->
Hardwood Year Age Slow Moderate 0 520 760 1 640 1080 2 800 1400 3 960 1720 4 1120 2080 5 1280 2440 6 1480 2840 7 1640 3240 8 1840 3640 9 2000 4080 10 2200 4480 11 2400 4920 12 2600 5400 13 2800 5840 14 3000 6320 15 3240 6760 16 3440 7240 17 3640 7760 18 3880 8240 19 4080 8760 20 4320 9280 21 4560 9760 22 4800 10320 23 5000 10840 24 5240 11360 25 5480 11920 26 5720 12480 27 6000 13000 28 6240 13560 29 6480 14120 30 6720 14720 31 7000 15280 Conifer Fast Slow Moderate Fast 1080 424 606 848 1600 545 909 1333 2160 667 1212 1879 2760 848 1515 2485 3400 970 1879 3152 4040 1152 2242 3879 4720 1333 2667 4606 5440 1515 3091 5394 6200 1697 3515 6182 6960 1879 4000 7091 7720 2121 4485 8000 8520 2303 4970 8909 9320 2545 5515 9879 10160 2788 6000 10848 11000 2970 6545 11879 11880 3212 7152 12970 12760 3455 7697 14061 13640 3697 8303 15152 14520 4000 8909 16303 15440 4242 9515 17455 16400 4485 10121 18667 17320 4788 10788 19879 18280 5030 11455 21152 19240 5333 12121 22424 20240 5576 12788 23697 21240 5879 13455 25030 22240 6182 14182 26364 23240 6485 14909 27697 24280 6788 15636 29091 25320 7091 16364 30485 26360 7394 17091 31939 27400 7697 17879 33394

<!-- b000921 | furniture | pages [33] -->
Team #14990

<!-- b000922 | prose | pages [33] -->
32 7240 15880 33 7480 16440 34 7760 17040 35 8000 17640 36 8280 18240 37 8560 18840 38 8800 19440 39 9080 20080 40 9360 20680 41 9640 21320 42 9920 21920 43 10160 22560 44 10440 23200 45 10720 23840 46 11040 24480 47 11320 25120 48 11600 25800 49 11880 26440 50 12160 27120 51 12440 27760 52 12760 28440 53 13040 29120 54 13360 29800 55 13640 30480 56 13920 31160 57 14240 31840 58 14520 32520 59 14840 33200

<!-- b000923 | furniture | pages [33] -->


<!-- b000924 | heading | pages [33] -->
8.3 Tree Age and Tree Size

<!-- b000925 | furniture | pages [33] -->


<!-- b000926 | furniture | pages [33] -->
33 / 42

<!-- b000927 | furniture | pages [33] -->


<!-- b000928 | prose | pages [33] -->
28480 8061 18606 34848 29520 8364 19394 36303 30600 8667 20182 37818 31720 9030 21030 39333 32800 9394 21818 40909 33920 9697 22606 42485 35040 10061 23455 44061 36160 10424 24303 45636 37280 10727 25152 47273 38440 11091 26000 48909 39600 11455 26848 50545 40760 11818 27758 52242 41920 12182 28606 53939 43080 12545 29515 55636 44280 12909 30424 57394 45440 13333 31333 59091 46640 13697 32242 60848 47840 14061 33212 62667 49080 14485 34121 64424 50280 14848 35091 66242 51520 15273 36000 68061 52720 15636 36970 69939 53960 16061 37939 71758 55200 16485 38909 73636 56480 16848 39939 75515 57720 17273 40909 77455 59000 17697 41939 79333 60240 18121 42909 81273

<!-- b000929 | prose | pages [33] -->
As stated above, we utilize the age of a tree as a link between the two variables,

<!-- b000930 | prose | pages [33] -->
leaf mass and the size characteristics of trees. Since we have found out the

<!-- b000931 | prose | pages [33] -->
correlation between the age of tree and the total leaf mass on it, now we only

<!-- b000932 | prose | pages [33] -->
need to work out the relation between the age of the tree and the size

<!-- b000933 | prose | pages [33] -->
characteristics of it.

<!-- b000934 | prose | pages [33] -->
Tree size is the accumulation of growth, which is a biological phenomenon of

<!-- b000935 | prose | pages [33] -->
increase with time. According the life cycle of a tree, it experiences the following

<!-- b000936 | prose | pages [33] -->
phases:

<!-- b000937 | furniture | pages [33] -->


<!-- b000938 | furniture | pages [34] -->
Team #14990

<!-- b000939 | furniture | pages [34] -->


<!-- b000940 | furniture | pages [34] -->
34 / 42

<!-- b000941 | furniture | pages [34] -->


<!-- b000942 | prose | pages [34] -->
Juvenile phase (youth) - accelerating rate of growth.

<!-- b000943 | furniture | pages [34] -->


<!-- b000944 | prose | pages [34] -->
Full vigor phase (maturity) - constant rate of growth.

<!-- b000945 | furniture | pages [34] -->


<!-- b000946 | prose | pages [34] -->
Senescent phase - decelerating rate of growth.

<!-- b000947 | furniture | pages [34] -->


<!-- b000948 | prose | pages [34] -->
As shown above, the cumulative growth curve, whose pattern is characteristic for

<!-- b000949 | prose | pages [34] -->
the life span of an organism, resembles logistic growth function. Thus we

<!-- b000950 | prose | pages [34] -->
construct the following model

<!-- b000951 | prose | pages [34] -->
P = 𝑘1 ∙(1 −𝑒𝑘2∙𝐴)𝑘3

<!-- b000952 | prose | pages [34] -->
Transformation leads to the following

<!-- b000953 | prose | pages [34] -->
A = 𝑘4 ∙ln(1 −𝑘5 ∙𝑃𝑘6)

<!-- b000954 | prose | pages [34] -->
Where,

<!-- b000955 | prose | pages [34] -->
P is the general profile of a tree(volume, height, mass, diameter).

<!-- b000956 | prose | pages [34] -->
A is the age of the tree.

<!-- b000957 | prose | pages [34] -->
k1, k2, k3, k4, k5 and k6 are constants.

<!-- b000958 | prose | pages [34] -->
It is important to note that P, the general profile of a tree, is a variable to describe

<!-- b000959 | prose | pages [34] -->
the size characteristics of a tree, which vary greatly in different species of trees.

<!-- b000960 | furniture | pages [35] -->
Team #14990

<!-- b000961 | furniture | pages [35] -->


<!-- b000962 | furniture | pages [35] -->
35 / 42

<!-- b000963 | furniture | pages [35] -->


<!-- b000964 | prose | pages [35] -->
Therefore it is not possible to work out an exact set of constants in the model

<!-- b000965 | prose | pages [35] -->
that suits all kinds of trees. This correlation between the size characters and age

<!-- b000966 | prose | pages [35] -->
is primarily qualitative.

<!-- b000967 | heading | pages [35] -->
8.4 Leaf Mass and Tree Size

<!-- b000968 | prose | pages [35] -->
Finally, we get to answer the question whether there exists a correlation

<!-- b000969 | prose | pages [35] -->
between leaf mass and tree size characteristics.

<!-- b000970 | prose | pages [35] -->
According to our study in X.2, leaf mass and tree age are related with each other

<!-- b000971 | prose | pages [35] -->
mathematically linked by CO2 Sequestration. Our model in X.3 determines a

<!-- b000972 | prose | pages [35] -->
function between tree age and tree size. Through this relationship map shown

<!-- b000973 | prose | pages [35] -->
below, it is clear that there must exist a correlation between leaf mass and tree

<!-- b000974 | prose | pages [35] -->
size.

<!-- b000975 | heading | pages [35] -->
9. Strengths and Weaknesses

<!-- b000976 | prose | pages [35] -->
Now we will analyze the strengths and weaknesses of each sub-model in our

<!-- b000977 | prose | pages [35] -->
paper:

<!-- b000978 | furniture | pages [35] -->


<!-- b000979 | furniture | pages [36] -->
Team #14990

<!-- b000980 | furniture | pages [36] -->


<!-- b000981 | furniture | pages [36] -->
36 / 42

<!-- b000982 | furniture | pages [36] -->


<!-- b000983 | heading | pages [36] -->
Model 1

<!-- b000984 | prose | pages [36] -->
Strength:

<!-- b000985 | prose | pages [36] -->
1.

<!-- b000986 | prose | pages [36] -->
Our model is based on quantitative analysis, so the classification process is

<!-- b000987 | prose | pages [36] -->
both objective and efficient;

<!-- b000988 | prose | pages [36] -->
2.

<!-- b000989 | prose | pages [36] -->
Our model chooses leaf types that are most typical and common as the

<!-- b000990 | prose | pages [36] -->
categories.

<!-- b000991 | prose | pages [36] -->
Weakness:

<!-- b000992 | prose | pages [36] -->
1.  Because of the limit of time and access to information, we only create six

<!-- b000993 | prose | pages [36] -->
categories, which may not cover all the leaf types.

<!-- b000994 | heading | pages [36] -->
Model 2

<!-- b000995 | prose | pages [36] -->
Strength:

<!-- b000996 | prose | pages [36] -->
1.

<!-- b000997 | prose | pages [36] -->
We have taken into consideration three conditions: tropical zone,

<!-- b000998 | prose | pages [36] -->
temperate zone and frigid zone when discussing the relationship between

<!-- b000999 | prose | pages [36] -->
the leaf distribution and the leaf shape;

<!-- b001000 | prose | pages [36] -->
2.

<!-- b001001 | prose | pages [36] -->
The result of our model conforms to our observation and the data we found.

<!-- b001002 | prose | pages [36] -->
Weakness:

<!-- b001003 | prose | pages [36] -->
1.

<!-- b001004 | prose | pages [36] -->
We consider the leaves distribution on a single branch, but have not

<!-- b001005 | prose | pages [36] -->
considered the inner-influence between different leaves of different

<!-- b001006 | prose | pages [36] -->
branches.

<!-- b001007 | heading | pages [36] -->
Model 3

<!-- b001008 | prose | pages [36] -->
Strength:

<!-- b001009 | prose | pages [36] -->
1.

<!-- b001010 | prose | pages [36] -->
The whole process use data and quantitative analysis as foundations, so the

<!-- b001011 | prose | pages [36] -->
output is objective and reasonable.

<!-- b001012 | prose | pages [36] -->
Weakness:

<!-- b001013 | prose | pages [36] -->
1.

<!-- b001014 | prose | pages [36] -->
We have limited categories of tree profiles, so our data to fit the curve is not

<!-- b001015 | prose | pages [36] -->
plenty enough.

<!-- b001016 | furniture | pages [36] -->


<!-- b001017 | furniture | pages [37] -->
Team #14990

<!-- b001018 | furniture | pages [37] -->


<!-- b001019 | furniture | pages [37] -->
37 / 42

<!-- b001020 | furniture | pages [37] -->


<!-- b001021 | heading | pages [37] -->
Model 4

<!-- b001022 | prose | pages [37] -->
Strength:

<!-- b001023 | prose | pages [37] -->
1.

<!-- b001024 | prose | pages [37] -->
We use the carbon sequestration rate and age as the mediums to calculate

<!-- b001025 | prose | pages [37] -->
the mass of total laves, which are far more scientific than estimating the

<!-- b001026 | prose | pages [37] -->
number of leaves and weight of each leaf.

<!-- b001027 | prose | pages [37] -->
Weakness:

<!-- b001028 | prose | pages [37] -->
1.

<!-- b001029 | prose | pages [37] -->
Since the data we get are from the statistics a little bit outdated, the

<!-- b001030 | prose | pages [37] -->
accuracy of our output may need some slight adjustment.

<!-- b001031 | furniture | pages [37] -->


<!-- b001032 | heading | pages [37] -->
10. Reference

<!-- b001033 | prose | pages [37] -->
[1]  David Knight, James Painter and Matthew Potter from Stanford University, department of electrical engineering, "Automatic Plant Leaf Classification for a Mobile Field Guide" .

<!-- b001034 | furniture | pages [37] -->


<!-- b001035 | prose | pages [37] -->
[2]  Z. Wang, Z. Chi, and D. Feng, “Shape based leaf image retrieval,” IEEE Proceedings: Vision, Image, and Signal Processing, vol. 150-1, pp. 34-43, February 2003.

<!-- b001036 | furniture | pages [37] -->


<!-- b001037 | prose | pages [37] -->
[3]   J. Du, X. Wang, and G. Zhang, “Leaf shape based plant species recognition,” Applied Mathematics and Computation, vol. 185-2, pp.883-893, February 2007.

<!-- b001038 | furniture | pages [37] -->


<!-- b001039 | prose | pages [37] -->
[4]  C. Im, H. Nishida, and T.L. Kunil, “Recognizing plant species by leaf shapes—a case study of the acer family,” in Proceedings of 1998 IEEE International Conference on Pattern Recognition, Brisbane, August 1998.

<!-- b001040 | furniture | pages [37] -->


<!-- b001041 | prose | pages [37] -->
[5]  Hirokazu Tsukaya Graduate School of Science, University of Tokyo, "Mechanism of Leaf-Shape Determination," in Annu. Rev. Plant Biol. 2006.57:477-496.

<!-- b001042 | furniture | pages [37] -->


<!-- b001043 | prose | pages [37] -->
[6]   U.S. Department of Energy Energy Information Administration, "Method for Calculating Carbon Sequestration by Trees in Urban and Suburban Settings," April 1998

<!-- b001044 | furniture | pages [37] -->


<!-- b001045 | furniture | pages [37] -->


<!-- b001046 | furniture | pages [37] -->


<!-- b001047 | furniture | pages [37] -->


<!-- b001048 | furniture | pages [38] -->
Team #14990

<!-- b001049 | furniture | pages [38] -->


<!-- b001050 | furniture | pages [38] -->
38 / 42

<!-- b001051 | furniture | pages [38] -->


<!-- b001052 | heading | pages [38] -->
11. A Letter to the Science Journal Editor

<!-- b001053 | prose | pages [38] -->
Dear editor,

<!-- b001054 | prose | pages [38] -->
From the very ancient times, leaves have been an important part of human life as they were weaved into clothes, used as containers of water, and most of all, relied upon as the main converter of carbon dioxide into oxygen. However, due to the variety and large quantity of leaves, there have always remained a lot of questions and mysteries of them, such as the reason behind their different shapes and distribution pattern as well as the relationship between leaf shape, leaf mass and tree profile. So, out of the interest in discovering the wonders of the nature and exploring the potential practical use of the natural phenomena, we, a group of high school students from Shanghai, have done some researches and now we are very glad to present to you our key findings:

<!-- b001055 | prose | pages [38] -->
We first focus on the possible influence of leaf distribution on leaf shape. We discover that for survival reasons, the trees develop an optimal leaf distribution and shape pattern to best adjust to the specific region of its origin by maximizing the exposure area to sunshine, thereby gaining the most nutrients for photosynthesis. And after testing our findings, we are convinced there does exist a mathematical relationship between the solar altitude, leaf shape and leaf distribution. With the above finding, we may be able to determine the best location for replanting or assisted-migration of a tree species by observing its leaf distribution.

<!-- b001056 | prose | pages [38] -->
Our second key finding is a rough correlation between the tree profile and leaves growing on that tree. In fact, we make a hypothesis that a leaf be a two-dimensional mimic of the tree. After we set up the database and compare the shape of leaf and the contour of tree carefully, some similarities between certain characteristics have surfaced. This finding suggests that the natural world might contain many examples of self-similarity, mathematical concept which means that an object is approximately similar to a part of itself, such as the famous Koch Snowflake and Mandelbrot Set.

<!-- b001057 | prose | pages [38] -->
The third part of our study deals with the relationship between the tree size characteristics and the total mass of the leaves. The two ends are linked by two calculating mediums, the CO2 sequestration rates and the age of the tree. Therefore, we are able to estimate the total mass of the leaves given some profiles of a tree such as its height, diameter, volume, age and type, and vice versa. This finding might have great potential for agricultural and environmental uses, such as a new method to estimate tea production or wood production, or estimation of CO2 sequestration effect of a leaf, a tree and, most importantly, a forest, which is a great alleviator of global warming.

<!-- b001058 | prose | pages [38] -->
In hope of publishing our research in your outstanding science journal, we’ve enclosed our research paper for you to examine and judge. We are convinced that our research on leaves is promising to contribute to a variety of areas.

<!-- b001059 | furniture | pages [38] -->


<!-- b001060 | prose | pages [38] -->
Yours faithfully

<!-- b001061 | furniture | pages [39] -->
Team #14990

<!-- b001062 | heading | pages [39] -->
12. Appendix

<!-- b001063 | furniture | pages [39] -->


<!-- b001064 | furniture | pages [39] -->
39 / 42

<!-- b001065 | furniture | pages [39] -->


<!-- b001066 | heading | pages [39] -->
12.1 Chart of Tree Species and Growth Rate

<!-- b001067 | prose | pages [39] -->
12.2 MATLAB Program Code

<!-- b001068 | furniture | pages [39] -->


<!-- b001069 | furniture | pages [39] -->


<!-- b001070 | furniture | pages [39] -->


<!-- b001071 | furniture | pages [39] -->


<!-- b001072 | furniture | pages [39] -->


<!-- b001073 | furniture | pages [39] -->


<!-- b001074 | furniture | pages [39] -->


<!-- b001075 | furniture | pages [39] -->


<!-- b001076 | furniture | pages [39] -->


<!-- b001077 | furniture | pages [39] -->


<!-- b001078 | furniture | pages [39] -->


<!-- b001079 | furniture | pages [39] -->


<!-- b001080 | furniture | pages [39] -->


<!-- b001081 | furniture | pages [39] -->


<!-- b001082 | furniture | pages [39] -->


<!-- b001083 | furniture | pages [39] -->


<!-- b001084 | furniture | pages [39] -->


<!-- b001085 | furniture | pages [39] -->


<!-- b001086 | furniture | pages [39] -->


<!-- b001087 | furniture | pages [39] -->


<!-- b001088 | furniture | pages [39] -->


<!-- b001089 | furniture | pages [39] -->


<!-- b001090 | furniture | pages [39] -->


<!-- b001091 | furniture | pages [39] -->


<!-- b001092 | furniture | pages [39] -->


<!-- b001093 | prose | pages [39] -->
How to use MATLAB to realize AHP A=input('A='); [n,n]=size(A);

<!-- b001094 | prose | pages [39] -->
%Input the pair ratio matrix as “A”. x=ones(n,100); y=ones(n,100); m=zeros(1,100);

<!-- b001095 | prose | pages [39] -->
m(1)=max(x(:,1)); y(:,1)=x(:,1); x(:,2)=A*y(:,1);

<!-- b001096 | furniture | pages [40] -->
Team #14990

<!-- b001097 | furniture | pages [40] -->


<!-- b001098 | furniture | pages [40] -->
40 / 42

<!-- b001099 | furniture | pages [40] -->


<!-- b001100 | prose | pages [40] -->
m(2)=max(x(:,2)); y(:,2)=x(:,2)/m(2); p=0.0001;i=2;k=abs(m(2)-m(1));

<!-- b001101 | prose | pages [40] -->
while k>p i=i+1; x(:,i)=A*y(:,i-1); m(i)=max(x(:,i));

<!-- b001102 | prose | pages [40] -->
y(:,i)=x(:,i)/m(i); k=abs(m(i)-m(i-1)); end a=sum(y(:,i)); w=y(:,i)/a;

<!-- b001103 | prose | pages [40] -->
%Find the Eigen Vector t=m(i); disp('EigenVector Wi='); disp(w); disp('LamdaMax=');

<!-- b001104 | prose | pages [40] -->
disp(t); CI=(t-n)/(n-1); %Calculate the Consistency Index (CI) RI=[0 0 0.52 0.89 1.12 1.26 1.36 1.41 1.46 1.49 1.52

<!-- b001105 | prose | pages [40] -->
1.54 1.56 1.58 1.59]; %Random Consistency Index (RI) disp('CI=');disp(CI); disp('RI=');disp(RI(n)); if RI(n)>0

<!-- b001106 | prose | pages [40] -->
CR=CI/RI(n); %Calculate the consistency ratio according to the formula disp('CR=');disp(CR); if CR<0.10

<!-- b001107 | prose | pages [40] -->
disp('Consistency Acceptable'); else disp('Consistency Inacceptable'); end

<!-- b001108 | prose | pages [40] -->
%Consistency Check end if RI(n)<=0

<!-- b001109 | furniture | pages [41] -->
Team #14990

<!-- b001110 | furniture | pages [41] -->


<!-- b001111 | furniture | pages [41] -->
41 / 42

<!-- b001112 | furniture | pages [41] -->


<!-- b001113 | prose | pages [41] -->
disp('Consistency Acceptable'); %Consistency Check end

<!-- b001114 | furniture | pages [41] -->


<!-- b001115 | prose | pages [41] -->
How to calculate the area of a leaf l=imread('leaftype1.jpg'); imshow(l);

<!-- b001116 | prose | pages [41] -->
%Import the picture m=ginput; %Pick the points on the perimeter of the figure and record the coordinates into “m” x(1,:)=m(:,1);

<!-- b001117 | prose | pages [41] -->
y(1,:)=m(:,2); x=[x x(1)]; y=[y y(1)]; N=length(x); t=1:N;

<!-- b001118 | prose | pages [41] -->
ti=1:(N-1)/100000:N; xi=spline(t,x,ti); yi=spline(t,y,ti); area=polyarea(xi,yi);

<!-- b001119 | prose | pages [41] -->
%calculate the area of the figure points=[x;y]; fnplt(cscvn(points));axis equal %draw the estimated function and check the accuracy; save the figure as „1-1.jpg‟ for further use

<!-- b001120 | furniture | pages [41] -->


<!-- b001121 | prose | pages [41] -->
How to calculate the perimeter of a leaf k=imread('1-1.jpg'); BW=im2bw(k); %turn the picture into binary form

<!-- b001122 | prose | pages [41] -->
STATS=regionprops(BW,'Perimeter'); %calculate the perimeter of the binary figure STATS.Perimeter; %print the perimeter

<!-- b001123 | furniture | pages [41] -->


<!-- b001124 | prose | pages [41] -->
Linear Regression with significance test x=input('Input x');

<!-- b001125 | furniture | pages [42] -->
Team #14990

<!-- b001126 | furniture | pages [42] -->


<!-- b001127 | furniture | pages [42] -->
42 / 42

<!-- b001128 | furniture | pages [42] -->


<!-- b001129 | prose | pages [42] -->
% Input the parameters of the leaves as x coordinates y=input('Input y');

<!-- b001130 | prose | pages [42] -->
% Input the parameters of the trees as y coordinates c=length(x); xi=0:0.1:1; a=polyfit(x,y,1);

<!-- b001131 | prose | pages [42] -->
% Find the coefficients of the fitting curve of the points yi=polyval(a,xi); % Calculate the y coordinates of the fitting curve hold on;

<!-- b001132 | prose | pages [42] -->
plot(x,y,'go','MarkerEdgeColor','k','MarkerFace Color','g','MarkerSize',5); % Draw the original input data plot(xi,yi,'linewidth',2,'markersize',7); % Draw the fitting curve

<!-- b001133 | prose | pages [42] -->
hold off; x=x'; y=y'; x=[ones(c,1),x];

<!-- b001134 | prose | pages [42] -->
[b,bint,r,rint,stats]=regress(y,x); % Significance test

<!-- b001135 | furniture | pages [42] -->

