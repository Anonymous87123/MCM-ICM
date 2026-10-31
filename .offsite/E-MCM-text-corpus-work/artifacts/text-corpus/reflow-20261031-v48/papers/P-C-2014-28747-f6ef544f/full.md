# P-C-2014-28747-f6ef544f

Status: machine-draft; not source-verified.


<!-- b000001 | front_matter | pages [1] -->
Team Control Number

<!-- b000002 | front_matter | pages [1] -->
28747

<!-- b000003 | front_matter | pages [1] -->
For office use only For office use only T1 ________________ F1 ________________ T2 ________________ F2 ________________ T3 ________________ F3 ________________ Problem Chosen T4 ________________ F4 ________________

<!-- b000004 | front_matter | pages [1] -->
C

<!-- b000005 | front_matter | pages [1] -->
2014 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000006 | title | pages [1] -->
Methods of Measuring Influence Using Network Model

<!-- b000007 | heading | pages [1] -->
Summary

<!-- b000008 | prose | pages [1] -->
In this paper, we build the network model to measure the impact of researchers, papers and so on.

<!-- b000009 | prose | pages [1] -->
We first use the network model to evaluate the impact of researchers,considering researchers as the nodes, and using sides to describe collaboration among researchers. We then propose the concept of importance degree and influence degree. They are all the properties of nodes. Importance degree depicts a node’s own weight in the network, while influence degree estimates a node’s total influence that mutual impact among nodes is included. Based on the comprehensive consideration of the clustering coefficient and degree, we put forward a new idea to measure a node’s importance degree. Then combining with PageRank algorithm, we can evaluate the influence degree of every node in the network. We can find ALON, NOGA M is the most influential researcher. By analyzing the properties of nodes, we find that for a general researcher, she/he should extend its collaborative network as greatly as possible, especially partner researchers with high importance degree.

<!-- b000010 | prose | pages [1] -->
Second, imitating previous methodology, we build the model to evaluate the impact of papers. We conclude that factors determining a paper’s influence contain three indexes: the first author’s H-value, the journal’s Impact Factor and cited index which is the concept we define to depict the influence degree of a paper in the aspect of citation. Referring to the previous idea, we construct a new network reflecting citation relationship among papers, then we can obtain the cited index of every paper. After having collected the value of another two indexes, we use AHP to determine the weight of three factors, and finally evaluate the total influence of a paper successfully. We find that the paper Statistical mechanics of complex networks is most influential.

<!-- b000011 | prose | pages [1] -->
After that we view the other fields instead of the academic area to extend our model. We apply our network model measure Chinese movie stars’ influence. We select a greatly influential movie star to replace the status of Erdös, and construct the cooperating network among movie stars. Having obtained influence degree of stars, the ranking of influence of movie stars maintained a highly consistent with reality. This is proof that our model is feasible. Then we discuss our model’s application for academic, military and SNS fields roughly.

<!-- b000012 | prose | pages [1] -->
Finally, we make a sensitivity analysis for our model, and discuss the impact of the changing of nodes and the papers’ feedback of citation relationship on the results.

<!-- b000013 | prose | pages [1] -->
Through previous analysis, we can see that our model can be applied to many files, so it has a relatively high generalization.

<!-- b000014 | heading | pages [2] -->
Contents

<!-- b000015 | contents | pages [2] -->
1 Introduction

<!-- b000016 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000017 | contents | pages [2] -->
1

<!-- b000018 | contents | pages [2] -->
1.1

<!-- b000019 | contents | pages [2] -->
Background . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000020 | contents | pages [2] -->
1

<!-- b000021 | contents | pages [2] -->
1.2

<!-- b000022 | contents | pages [2] -->
Our work

<!-- b000023 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000024 | contents | pages [2] -->
1

<!-- b000025 | contents | pages [2] -->
2

<!-- b000026 | contents | pages [2] -->
Assumptions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000027 | contents | pages [2] -->
2

<!-- b000028 | contents | pages [2] -->
3 Symbol Description

<!-- b000029 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000030 | contents | pages [2] -->
3

<!-- b000031 | contents | pages [2] -->
4

<!-- b000032 | contents | pages [2] -->
The inﬂuence of researchers . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000033 | contents | pages [2] -->
3

<!-- b000034 | contents | pages [2] -->
4.1

<!-- b000035 | contents | pages [2] -->
Model one: the measurement of nodes’ importance degree model based

<!-- b000036 | contents | pages [2] -->
on network theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000037 | contents | pages [2] -->
3

<!-- b000038 | contents | pages [2] -->
4.1.1

<!-- b000039 | contents | pages [2] -->
Evaluating the importance of researchers only by Node degree .

<!-- b000040 | contents | pages [2] -->
4

<!-- b000041 | contents | pages [2] -->
4.1.2

<!-- b000042 | contents | pages [2] -->
Evaluating the importance degree of researchers using clustering

<!-- b000043 | contents | pages [2] -->
coefﬁcient . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000044 | contents | pages [2] -->
5

<!-- b000045 | contents | pages [2] -->
4.1.3

<!-- b000046 | contents | pages [2] -->
The evaluation model based on the clustering coefﬁcient and de-

<!-- b000047 | contents | pages [2] -->
gree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000048 | contents | pages [2] -->
5

<!-- b000049 | contents | pages [2] -->
4.2

<!-- b000050 | contents | pages [2] -->
Model two: the measurement of nodes’ inﬂuence degree model based

<!-- b000051 | contents | pages [2] -->
on PageRank algorithm . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000052 | contents | pages [2] -->
7

<!-- b000053 | contents | pages [2] -->
4.2.1

<!-- b000054 | contents | pages [2] -->
An introduction to PageRank . . . . . . . . . . . . . . . . . . .

<!-- b000055 | contents | pages [2] -->
8

<!-- b000056 | contents | pages [2] -->
4.2.2

<!-- b000057 | contents | pages [2] -->
The PageRank evaluation model based on the importance degree.

<!-- b000058 | contents | pages [2] -->
8

<!-- b000059 | contents | pages [2] -->
4.3

<!-- b000060 | contents | pages [2] -->
Result analysis: some interesting data

<!-- b000061 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . .

<!-- b000062 | contents | pages [2] -->
9

<!-- b000063 | contents | pages [2] -->
5

<!-- b000064 | contents | pages [2] -->
The inﬂuence of papers . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000065 | contents | pages [2] -->
11

<!-- b000066 | contents | pages [2] -->
5.1

<!-- b000067 | contents | pages [2] -->
The citing network of papers . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000068 | contents | pages [2] -->
11

<!-- b000069 | contents | pages [2] -->
5.2

<!-- b000070 | contents | pages [2] -->
Model three:comprehensive evaluation model based on AHP . . . . . .

<!-- b000071 | contents | pages [2] -->
12

<!-- b000072 | contents | pages [2] -->
6

<!-- b000073 | contents | pages [2] -->
Model Extension . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000074 | contents | pages [2] -->
13

<!-- b000075 | contents | pages [2] -->
6.1

<!-- b000076 | contents | pages [2] -->
Applying models to a speciﬁc area . . . . . . . . . . . . . . . . . . . .

<!-- b000077 | contents | pages [2] -->
14

<!-- b000078 | contents | pages [2] -->
6.2

<!-- b000079 | contents | pages [2] -->
Analysis of models expansibility . . . . . . . . . . . . . . . . . . . . .

<!-- b000080 | contents | pages [2] -->
15

<!-- b000081 | contents | pages [2] -->
7

<!-- b000082 | contents | pages [2] -->
Error/Sensitivity Analysis . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000083 | contents | pages [2] -->
16

<!-- b000084 | contents | pages [2] -->
7.1

<!-- b000085 | contents | pages [2] -->
Sensitivity analysis of the collaborative network . . . . . . . . . . . . .

<!-- b000086 | contents | pages [2] -->
16

<!-- b000087 | contents | pages [2] -->
7.2

<!-- b000088 | contents | pages [2] -->
Sensitivity analysis of the citing network . . . . . . . . . . . . . . . . .

<!-- b000089 | contents | pages [2] -->
17

<!-- b000090 | contents | pages [2] -->
8

<!-- b000091 | contents | pages [2] -->
Analysis of the Model . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000092 | contents | pages [2] -->
18

<!-- b000093 | contents | pages [2] -->
8.1

<!-- b000094 | contents | pages [2] -->
Strengths

<!-- b000095 | contents | pages [2] -->
. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000096 | contents | pages [2] -->
18

<!-- b000097 | contents | pages [2] -->
8.2

<!-- b000098 | contents | pages [2] -->
Weaknesses . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

<!-- b000099 | contents | pages [2] -->
18

<!-- b000100 | furniture | pages [3] -->
Team # 28747

<!-- b000101 | furniture | pages [3] -->
Page 1 of 19

<!-- b000102 | heading | pages [3] -->
1 Introduction

<!-- b000103 | heading | pages [3] -->
1.1 Background

<!-- b000104 | prose | pages [3] -->
Do you believe that everyone in the world can establish contact with anyone else by only six persons at most? Even the U.S. President and the boatman of Venice, once ﬁnd- ing the right person, they can establish connection. The famous six degrees of separation theory tells us that as long as we ﬁnd right media, we can build relationship between any two seemingly unrelated entities.

<!-- b000105 | prose | pages [3] -->
This theory is still applicable in academia. Some researchers can often complete some high-quality papers through cooperation, which is inseparable from the strong re- lations among them. In this era, interdisciplinary study is very prevalent,so the research capability of researchers and academic standards of the paper are affected by many as- pects of intricate academic network. More and more attention has been paid to how to judge the academic level and the quality of papers.

<!-- b000106 | prose | pages [3] -->
Paul Erd¨os is a legendary mathematician. In his half-century career in scientiﬁc research, he had more than 500 collaborators and published more than 1400 academic papers. There is no doubt that he is one of the most inﬂuential founders in the study of interdisciplinary. People can even deﬁne a concept called ”collaborative distance”, and use Erd¨os number to indicate direct and indirect cooperation degree. Erd¨os 0 represents Erd¨os himself, Erd¨os 1 represents the researchers who had direct cooperation with Erd¨os, Erd¨os 2 represents the researchers who had direct cooperation with Erd¨os 1, and so on.

<!-- b000107 | prose | pages [3] -->
To study the inﬂuence of researchers who had direct cooperation with Erd¨os(the persons whose Erd¨os number is one), this passage is inspired by PageRank algorithm used in Google search engine and clustering coefﬁcient which measures the importance degree of each node in the network, and establish network model based on graph theory. We give a methodology to evaluate the inﬂuence of researchers and papers, and extend this model to another aspects.

<!-- b000108 | heading | pages [3] -->
1.2 Our work

<!-- b000109 | prose | pages [3] -->
First, the inﬂuence of researchers and the importance of researchers are both a rela- tively vague concept. In order to get a clear picture of the problem, we think that three factors should be taken into consideration to measure the inﬂuence of one researcher:

<!-- b000110 | prose | pages [3] -->
• The researcher’s extensive degree in the ﬁeld of cooperation, namely the number of partners.

<!-- b000111 | prose | pages [3] -->
• The times of cooperation with other researchers who have strong inﬂuence. In this paper, it is the times of cooperation with Erd¨os.

<!-- b000112 | furniture | pages [4] -->
Team # 28747

<!-- b000113 | furniture | pages [4] -->
Page 2 of 19

<!-- b000114 | prose | pages [4] -->
• The academic level of partners who cooperate with the researcher.

<!-- b000115 | prose | pages [4] -->
The measure of the importance of a research paper should contain the following factors:

<!-- b000116 | prose | pages [4] -->
• The author’s inﬂuence of the research paper’s, we can measure it by H-index.

<!-- b000117 | prose | pages [4] -->
• The popularity of the journal which have published this research paper, we can use the journal’s Impact Factor(IF) to express.

<!-- b000118 | prose | pages [4] -->
• The number of citation by other researchers.

<!-- b000119 | prose | pages [4] -->
On the basis of above discussion, to evaluate the inﬂuence of researchers and researcher paper, and to promote it to be applied in the actual, we may boil down the tasks to the following four questions :

<!-- b000120 | prose | pages [4] -->
1. By limiting the size of network and extracting the data, build a co-author network of the 511 researchers from the ﬁle Erdos1 and analyze the properties of this net- work. Develop inﬂuence measure(s) to determine the researchers’ inﬂuence within the network, and then do evaluation and ranking for them.( Erd¨os is not there to play these roles.)

<!-- b000121 | prose | pages [4] -->
2. Change the object of study and design a model to evaluate the signiﬁcance of researcher paper. Consider how you would measure the role, inﬂuence, or impact of a speciﬁc university, department, or a journal in network science? Do ranking for the importance of research paper and compare the difference between these two methodology.

<!-- b000122 | prose | pages [4] -->
3. Collect data, and extend previous models and algorithms to other ﬁelds in the actual to examine their adaptability .

<!-- b000123 | prose | pages [4] -->
4. Discuss the science and utility of the model built before.

<!-- b000124 | heading | pages [4] -->
2 Assumptions

<!-- b000125 | prose | pages [4] -->
• If a paper was cited more than once in another paper, we regard it as once.

<!-- b000126 | prose | pages [4] -->
• The importance degree we measure is for present.

<!-- b000127 | prose | pages [4] -->
• The average value of measurement indexes of papers or movie stars can reﬂect their current impact.

<!-- b000128 | prose | pages [4] -->
• The number of cooperation with Erd¨os can affect a researchers inﬂuence degree, but when the number exceed a certain value, the affection would be tend to be a constant.

<!-- b000129 | prose | pages [4] -->
• To some degree, the quality of one paper is proportional to the number cited by other papers.

<!-- b000130 | furniture | pages [5] -->
Team # 28747

<!-- b000131 | furniture | pages [5] -->
Page 3 of 19

<!-- b000132 | heading | pages [5] -->
3 Symbol Description

<!-- b000133 | prose | pages [5] -->
In the section, we use some symbols for constructing the model as follows.

<!-- b000134 | prose | pages [5] -->
Description

<!-- b000135 | heading | pages [5] -->
Symbol

<!-- b000136 | prose | pages [5] -->
The researcher is importance degree in the net- pi work The researcher is inﬂuence degree in the net- qi work Hi The H-index of paper is author IFi The Impact Factor of paper is journal i Deviation Degree between the old results and Ei the new ranking results after deleting node i

<!-- b000137 | prose | pages [5] -->
P.s:Other symbols instructions will be given in the text.

<!-- b000138 | heading | pages [5] -->
4 The inﬂuence of researchers

<!-- b000139 | prose | pages [5] -->
Before modeling, to avoid ambiguity, we will deﬁne the two confusing concept.

<!-- b000140 | prose | pages [5] -->
• The importance degree of a node : the node’s inﬂuence in the network. It mea- sures a node’s ability to communicate with neighbour nodes and to build the con- nection among different nodes in the whole network.

<!-- b000141 | prose | pages [5] -->
• The inﬂuence degree of a node: Due to the connection with other nodes, the node was affected by other nodes and therefore it possesses its own comprehensive strength, namely the inﬂuence.

<!-- b000142 | heading | pages [5] -->
4.1 Model one: the measurement of nodes’ importance degree mod-

<!-- b000143 | prose | pages [5] -->
el based on network theory

<!-- b000144 | prose | pages [5] -->
In order to measure the inﬂuence degree of each researcher, according to graph theo- ry, we deﬁne the nodes as researchers and the sides as the partnership among researchers . Thus, we establish network model which can reﬂect the interrelation among the re- searchers. To facilitate understanding and further analysis, we give the schematic dia- gram of the network model , shown in Figure 1.

<!-- b000145 | prose | pages [5] -->
We can see that through small scope of cooperation, researchers promote the connec- tivity of the whole network, and contribute to the connection among seemingly unrelated ﬁelds.

<!-- b000146 | furniture | pages [6] -->
Team # 28747

<!-- b000147 | furniture | pages [6] -->
Page 4 of 19

<!-- b000148 | caption | pages [6] -->
Figure 1: The diagram which describes the

<!-- b000149 | caption | pages [6] -->
Figure 2: After deleting node 8, the con-

<!-- b000150 | prose | pages [6] -->
relation among 10 researchers nectivity of the graph has been destroyed.

<!-- b000151 | prose | pages [6] -->
To evaluate the importance degree of each researcher in the network model, we discuss its measuring method in the following section.

<!-- b000152 | heading | pages [6] -->
4.1.1 Evaluating the importance of researchers only by Node degree

<!-- b000153 | prose | pages [6] -->
Assume that network G = (V;E) is undirected and consists of |V| = N nodes and |E| = M sides. Node degree is the number of sides associated with other nodes, it can expressed as:

<!-- b000154 | prose | pages [6] -->
ki = ∑ δij j∈G  0,node i and node j are not connected (1)   where δij =  1,node i and node j are connected 

<!-- b000155 | prose | pages [6] -->
In Figure 1, node 8 has the most node degree, or k8 = 4. If delete it, as shown in Figure 2 , node7,9 and 10 become isolated, the connectivity of the network are badly affected. In contrast, its impact degree decline less if the deleted nodes degree is less. Therefore, the quantity of nodes’ degree represents the importance of researchers.

<!-- b000156 | prose | pages [6] -->
But, is the nodes which have the same number of degree have the same importance? We analyze it in the following, as is shown in Figure 3 and 4 shown:

<!-- b000157 | prose | pages [6] -->
In the picture, node 2 and 4 have the same quantities of degree. However, deleting node 2 has no effect on the connectivity of the whole network. After deleting node 4, node 5 is separated , and node 7,8,9,10 lose the connection with node 1,2,3,6. Thus it can be seen that the nodes which have the same number of degree do not always have the same impact degree.

<!-- b000158 | prose | pages [6, 7] -->
So we can conclude that node degree represents the direct connecting ability with its neighbor node, but it cannot reﬂect its inﬂuence on the connectivity of the whole after deleting node 2. after deleting node 4

<!-- b000159 | furniture | pages [7] -->
Team # 28747

<!-- b000160 | furniture | pages [7] -->
Page 5 of 19

<!-- b000161 | caption | pages [7] -->
Figure 3: The condition of connection

<!-- b000162 | caption | pages [7] -->
Figure 4: The condition of connection

<!-- b000164 | prose | pages [7] -->
network. To look for a suitable method to solve this problem, we introduce the concept of clustering coefﬁcient.

<!-- b000165 | heading | pages [7] -->
4.1.2 Evaluating the importance degree of researchers using clustering coefﬁcient

<!-- b000166 | prose | pages [7] -->
Assume the degree of node i is k, then the maximum triangle formed by the k neigh- bour nodes is C2 k, hypothesise ei represents the number of triangle formed by any two neighbor nodes, then clustering coefﬁcient [4]can be deﬁned as:

<!-- b000167 | prose | pages [7] -->
ci = ei (2) C2 k

<!-- b000168 | prose | pages [7] -->
In graph theory, a clustering coefﬁcient is a measure of the degree to which nodes in a graph tend to cluster together. And in this passage, it describes the cooperation degree between a researcher and his partners.

<!-- b000169 | prose | pages [7] -->
By analyzing the node 2 and 4 in the Figure 3 and 4, we ﬁnd because of the node degree of them are both 3, the maximum triangle formed by their neighbour nodes are 3. However, in the actual situation, the triangle number of node 2 is 2 and node 4 is 0, so c2 = 2 3, c4 = 0. The result indicates that other nodes which have cooperated with node 4 have no connection with each other. Node 4 is crucial in connecting other nodes and is more important than node 2.

<!-- b000170 | prose | pages [7] -->
However, different from degree index, clustering coefﬁcient can reﬂect the connec- tivity of neighbour nodes to some extent, but it cannot show the scale of neighbour nodes. Hence, we should evaluate the importance of nodes by considering node degree and clustering coefﬁcient synthetically.

<!-- b000171 | heading | pages [7] -->
4.1.3 The evaluation model based on the clustering coefﬁcient and degree

<!-- b000172 | prose | pages [7] -->
First, we consider node degree.

<!-- b000173 | furniture | pages [8] -->
Team # 28747

<!-- b000174 | furniture | pages [8] -->
Page 6 of 19

<!-- b000175 | prose | pages [8] -->
Assume fi is the sum degree of itself and neighbour nodes for node i, and it can be expressed as:

<!-- b000176 | prose | pages [8] -->
fi = ki + ∑ kw (3) w∈Γi

<!-- b000177 | prose | pages [8] -->
Where kw is the degree of node w, Γi is the collection of node i’s neighbour node.fi reﬂects the information between the node’s degree and its neighbour degree.

<!-- b000178 | prose | pages [8] -->
Then, we consider clustering coefﬁcient.

<!-- b000179 | prose | pages [8] -->
Assume gi be :

<!-- b000180 | prose | pages [8] -->
N j=1 {c j f j }−cj max f j gi = (4) N N j=1 {cj j=1{cj f j }− f j } max min

<!-- b000181 | prose | pages [8] -->
where ci is the clustering coefﬁcient of node i. Because clustering coefﬁcient indicate the connection degree among neighbour nodes, but cannot reﬂect their scale, so ci fi can be normalized. Shown as equation (4) [5], gi also show closeness among neighbour nodes.

<!-- b000182 | prose | pages [8] -->
Assume pi is the importance degree of node i, to evaluate the importance of nodes x √ synthetically, we deal with fi and gi by the chemotactic function [5] u(x) = ∑x2, so we get the importance degree pi [?]as:

<!-- b000183 | prose | pages [8] -->
fi gi pi = + (5) s s N N f 2 g2 ∑ ∑ j j j=1 j=1

<!-- b000184 | prose | pages [8] -->
On the other hand, consider every researcher has different times of direct cooperation with Erd¨os, and the times can reﬂect the importance of researcher to some degree. So to quantify the index, we use a piecewise function to simulate the impact of x direct cooperation with Erd¨os on the researchers’ importance, it is expressed as:

<!-- b000185 | prose | pages [8] -->
 11 0.002x 10,0 < x < 65   Pi(x) = (6)  0.2,x ≥65 

<!-- b000186 | prose | pages [8] -->
Therefore, the comprehensive importance of every researcher is:

<!-- b000187 | prose | pages [8, 9] -->
qi = Pi(x)+ pi (7) In order to simplify the calculation, we only study the co-author network of the Erd¨os 1 authors, then we get the qi of 511 researchers and list the top ten researchers as shown in Table 1.(Note that this ranking is not the researchers eventually inﬂuence ranking, but the importance in the network.)

<!-- b000188 | furniture | pages [9] -->
Team # 28747

<!-- b000189 | furniture | pages [9] -->
Page 7 of 19

<!-- b000191 | caption | pages [9] -->
Table 1: The ranking of researchers’ importance degree qi

<!-- b000192 | prose | pages [9] -->
Name q Rank Cooperation Year Times

<!-- b000193 | prose | pages [9] -->
1 ALON, NOGA M. 0.2070 1985 5 2 HARARY, FRANK* 0.1820 1965 2 3 GRAHAM, RONALD LEWIS 0.1820 1972 28 4 RODL, VOJTECH 0.1795 1983 11 5 BOLLOBAS, BELA 0.1795 1962 28 6 TUZA, ZSOLT 0.1698 1989 11 7 FUREDI, ZOLTAN 0.1698 1982 10 8 SOS, VERA TURAN 0.1623 1966 35 9 SPENCER, JOEL HAROLD 0.1522 1971 23 10 PACH, JANOS 0.1393 1980 21

<!-- b000194 | prose | pages [9] -->
By statistics, Erd¨os had cooperated 1671 times in total with the 511 researchers and the average number of collaborative time is 3. Analyzing the data according to Table 1, we ﬁnd in most cases that the top ten researchers’ importance are those who cooperated with Erd¨os frequently and their ﬁrst cooperation is very early. The reasonable explana- tion for this phenomenon is that their frequent and early cooperation help them develop and grow in the collaborative network , and their importance is irreplaceable. We call this kind of group ”old researcher”.

<!-- b000195 | prose | pages [9] -->
Compared with them, the researchers whose ﬁrst cooperation with Erd¨os is relatively late (”young researcher”) cannot build a mature network relationship. Their importance is low, but it cannot explain why they don’t possess strong scientiﬁc researcher inﬂuence. For example, if a ”young researcher” can cooperated with a ”old researcher”, she/he may make a breakthrough and improve their inﬂuence degree. Therefore, it is not the ﬁnal index to evaluate the inﬂuence. We need to establish a objective model to evaluate the impact in view of the cooperation inﬂuence on the researcher.

<!-- b000196 | heading | pages [9] -->
4.2 Model two: the measurement of nodes’ inﬂuence degree model

<!-- b000197 | prose | pages [9] -->
based on PageRank algorithm

<!-- b000198 | prose | pages [9] -->
For the sake of assessing inﬂuence of researchers reasonably, to consider researchers’ own importance degree and inﬂuence degree determined by their collaborative network, we introduce PageRank algorithm to deal with this problem.

<!-- b000199 | furniture | pages [10] -->
Team # 28747

<!-- b000200 | furniture | pages [10] -->
Page 8 of 19

<!-- b000201 | heading | pages [10] -->
4.2.1 An introduction to PageRank

<!-- b000202 | prose | pages [10] -->
Because of its powerful retrieval function and high quality retrieval serviceGoogle is one of the most popular search engines. Using its PageRank algorithm to calculate the PageRank values of each web page, Google get the rank of the web page by balancing the number of links to the search target and the quality of these links. The higher the value of PageRank is, the higher the rank has[2].

<!-- b000203 | prose | pages [10] -->
4.2.2 The PageRank evaluation model based on the importance degree.

<!-- b000204 | prose | pages [10] -->
In section 4.1, we’ve got important degree of every researchers, set ai j is the impor- tance degree of node i to node j, so we can get the adjacent matrix among nodes in the network, we use A to express:

<!-- b000205 | prose | pages [10] -->
  ··· a11 a12 a1n ··· a21 a22 a2n   A = (8) ... ... ... ...

<!-- b000206 | prose | pages [10] -->
··· an1 an2 ann

<!-- b000207 | prose | pages [10] -->
0, i and j connect   Where, aij = (9) qi, i and j don’t connect.(i, j = 0,1,2,...,511) 

<!-- b000208 | prose | pages [10] -->
To distribute the researcher’s importance equally to researchers who cooperated she/he , normalize each line of the matrix, set this new matrix be ¯A , then transpose ¯A and get the matrix of transition probability W, or:

<!-- b000209 | prose | pages [10] -->
W = ¯AT = [wi j]511×511 (10)

<!-- b000210 | prose | pages [10] -->
Assign each researcher a PageRank value xi it should be determined by his(her) partners’ importance degree qi . In a other word, one researcher’s inﬂuence degree is proportional to her/his partners’ importance.

<!-- b000211 | prose | pages [10] -->
Set the common proportionality coefﬁcient be λ, we can get the following linear equations:

<!-- b000212 | prose | pages [10] -->
N ∑ wijxj = λxi,(xi = qi,i = 1,2,...,511) (11) j=1

<!-- b000213 | prose | pages [10] -->
Let X = (x1,x2,...,x511)T be column vector formed by the effect from other re- searchers. Through matrix multiplication, equation (4.2.2) can be expressed as:

<!-- b000214 | furniture | pages [11] -->
Team # 28747

<!-- b000215 | furniture | pages [11] -->
Page 9 of 19

<!-- b000216 | prose | pages [11] -->
WX = λX (12)

<!-- b000217 | prose | pages [11] -->
Thus we can obtain the maximum positive eigenvalues of the transition probability matrix λmaxand the corresponding non-negative feature vector Xmax = (x1,x2,...,x511)T , so we get researchers’ impact x1,x2,...xn and ultimately inﬂuence rankings. We only list top ten researchers, shown in Table 2.

<!-- b000218 | caption | pages [11] -->
Table 2: The top ten researchers inﬂuence degree

<!-- b000219 | prose | pages [11] -->
Name p Rank

<!-- b000220 | prose | pages [11] -->
1 ALON, NOGA M. 0.3939 2 GRAHAM, RONALD LEWIS 0.3113 3 BOLLOBAS, BELA 0.3021 4 RODL, VOJTECH 0.2702 5 FUREDI, ZOLTAN 0.2401 6 TUZA, ZSOLT 0.2373 7 HARARY, FRANK* 0.2113 8 SOS, VERA TURAN 0.2068 9 SPENCER, JOEL HAROLD 0.1988 10 FAUDREE, RALPH JASPER, JR. 0.1798

<!-- b000221 | heading | pages [11] -->
4.3 Result analysis: some interesting data

<!-- b000222 | prose | pages [11] -->
We already know, the researchers’ importance index and inﬂuence index are two d- ifferent evaluation criterions of measuring the level of scientiﬁc researchers. The former reﬂects the researcher’s ability to contribute to the connection in the network by contact- ing other researchers, while the latter shows the researcher is affected by herself/himself and her/his partners and can change these factors into her/his overall inﬂuence.

<!-- b000223 | prose | pages [11] -->
Comparing the rank result of the two methods, we ﬁnd that the change of over 80% researchers’ ranking is within 75. In view of their difference of emphasis, it is acceptable.

<!-- b000224 | prose | pages [11] -->
However, analyzing the remaining data, we ﬁnd some interesting phenomenon,we show it in Table 3

<!-- b000225 | prose | pages [11] -->
In the above table, we deﬁne the area of yellow as stable data, the area of green as positive data and the area of red as negative data.

<!-- b000226 | prose | pages [11] -->
• Stable data: we analyze the top ﬁve inﬂuence of researchers and ﬁnd their ranking is closely to their importance ranking. We conclude the inﬂuence degree of the researchers with large importance degree is also great.

<!-- b000227 | furniture | pages [12] -->
Team # 28747

<!-- b000228 | furniture | pages [12] -->
Page 10 of 19

<!-- b000229 | caption | pages [12] -->
Table 3: The schematic diagram of researchers’ indexes

<!-- b000230 | prose | pages [12] -->
q p p−q Name Year times rank rank

<!-- b000231 | prose | pages [12] -->
1 1 0 1985 5 ALON, NOGA M 3 2 1 1972 28 GRAHAM, RONALD LEWIS 5 3 2 1962 18 BOLLOBAS, BELA 4 4 0 1983 11 RODL, VOJTECH 7 5 2 1982 10 FUREDI, ZOLTAN

<!-- b000232 | prose | pages [12] -->
362 70 292 1988 3 PYBER, LASZLO 359 80 279 1990 2 TETALI, PRASAD VARA 364 89 275 1987 2 LINIAL, NATHAN 494 143 351 1991 9 FISHBURN, PETER C 488 211 277 1981 7 TENENBAUM, GERALD

<!-- b000233 | prose | pages [12] -->
375 507 -132 1983 1 STEIN, ALAN H 377 508 -131 1990 1 SMITH, PAUL R 399 509 -110 1990 1 MAXSEIN, THOMAS* 367 510 -143 1961 1 ZIV, ABRAHAM

<!-- b000234 | prose | pages [12] -->
• Positive data: Some researchers’ inﬂuence degree ranking improve by more than 250 than their importance degree ranking, some even improve by 351. Their common feature is their ﬁrst cooperation with Erd¨os is late, so their cooperation network cannot develop maturely and their importance degree ranking is low.

<!-- b000235 | prose | pages [12] -->
However, by cooperating frequently with high inﬂuence researchers, their inﬂu- ence degree can be promoted. Take FISHBURN, PETER C as an example, not on- ly does she/he cooperated frequently with Erd¨os, but also cooperate with some re- searchers whose importance degree is high(FUREDI, ZOLTAN,GRAHAM, RON ALD LEWIS and SPENCER, JOEL HAROLD), so his inﬂuence degree ranking have greatly improved. We conclude that even with lower importance degree in the network, one can enhance its inﬂuence degree by cooperating with highly in- ﬂuential researchers.

<!-- b000236 | prose | pages [12] -->
• Negative data: We ﬁnd four researchers’ inﬂuence degree drop more than 100.

<!-- b000237 | prose | pages [12] -->
Investigating their data, we get their partners are more than 20, but over half of them don’t belong to Erd¨os 1. The result shows that the researcher who cooperate less frequently have low inﬂuence degree.

<!-- b000238 | prose | pages [12, 13] -->
So we can draw the conclusion that a researcher can improve their inﬂuence by enhanc- ing its own collaborative network, and the importance degree of its partners plays an important role in enhancing its inﬂuence.

<!-- b000239 | furniture | pages [13] -->
Team # 28747

<!-- b000240 | furniture | pages [13] -->
Page 11 of 19

<!-- b000242 | heading | pages [13] -->
5 The inﬂuence of papers

<!-- b000243 | prose | pages [13] -->
To evaluate research papers’ inﬂuence, we choose 15 research papers in appendix and use the method of the section §4. We establish a model which reﬂects the interaction among researcher papers.

<!-- b000244 | prose | pages [13] -->
Undoubtedly, the best way to evaluate the inﬂuence degree of a research paper is examining the quality of the content. However, there doesn’t exist a great and direct method for it. Therefore, we need to look for indexes to evaluate indirectly. By anal- ysis, we think the factors that affect the inﬂuence degree of research papers is mainly manifested in two aspects.

<!-- b000245 | prose | pages [13] -->
External inﬂuence degree: the citing of a paper is an important index to measure its inﬂuence. By analyzing the relation of the mutual citing of these 15 papers, we can build a citing network similar to model one, and use PageRank algorithm to evaluate every paper’s inﬂuence degree.

<!-- b000246 | prose | pages [13] -->
Internal inﬂuence degree: It is also affected by its ﬁrst author’s level of scientiﬁc research, namely H index, and the inﬂuence of the journal, namely Impact Factor(IF).

<!-- b000247 | prose | pages [13] -->
So we choose the above three indexes to evaluate papers’ inﬂuence degree.

<!-- b000248 | heading | pages [13] -->
5.1 The citing network of papers

<!-- b000249 | prose | pages [13] -->
First of all, different from network relationship of researchers, one research paper can only cite the paper published before it and there is no relationship of cooperation between them. Nevertheless, once cited, it indicates this research paper gets the afﬁrmation from other researchers. The more the researcher paper is cited, the higher inﬂuence of this researcher paper will have. Meanwhile, the quoter can also beneﬁt from it and improve his(her) paper impact. Hence, we can establish feedback relationship like researchers. We establish the network relationship graph among research papers. The nodes represent research papers and the sides represent the feedback relationship among research papers (we assume that the effects of interaction of two papers exist citing relation are equal), shown in the Figure 5.

<!-- b000250 | prose | pages [13] -->
Using the PageRank algorithm in model two, we can get the inﬂuence degree in the network, we call it paper cited index, set it be r, which measures its cited inﬂuence.

<!-- b000251 | prose | pages [13] -->
By collecting data from authoritative website( such as SCI ,Google Scholar), we use the number cited by others as the index to measure the importance degree q of every node.

<!-- b000252 | furniture | pages [14] -->
Team # 28747

<!-- b000253 | furniture | pages [14] -->
Page 12 of 19

<!-- b000254 | caption | pages [14] -->
Figure 5: The citation network among papers

<!-- b000255 | prose | pages [14] -->
Set the adjacency matrix of the nodes in the network be A:

<!-- b000256 | prose | pages [14] -->
  ··· a11 a12 a1n ··· a21 a22 a2n   A = (13) ... ... ... ...

<!-- b000257 | prose | pages [14] -->
··· an1 an2 ann

<!-- b000258 | prose | pages [14] -->
0, i and j connect   Thereinto, aij = (14) qi, i and j don’t connect 

<!-- b000259 | prose | pages [14] -->
Normalize A and use equation (11), we can get r of these 15 research papers.

<!-- b000260 | heading | pages [14] -->
5.2 Model three:comprehensive evaluation model based on AHP

<!-- b000261 | prose | pages [14] -->
r can only reﬂect the effect from eternal element. To evaluate a research paper over- all, we are determined to use AHP and calculate the weight of IF, H index and r.

<!-- b000262 | prose | pages [14] -->
We think that in the progress of measuring a research paper, the ﬁrst author shouldn’t be considered too much. Except that, the contribution of internal factor is greater than external factor . So we set the size of relationship of the three factors: IF > r > H.

<!-- b000263 | prose | pages [14] -->
By this principle, we give Pairwise comparison matrix:

<!-- b000264 | prose | pages [14, 15] -->
IF H r IF 1 4 2   1 1 H 1   (15) 4 4     1   r 4 1 2 We then input the matrix into YAAHP and calculate the weight of each factor:αIF = 0.5469,αH = 0.1085,αr = 0.3445.

<!-- b000265 | furniture | pages [15] -->
Team # 28747

<!-- b000266 | furniture | pages [15] -->
Page 13 of 19

<!-- b000268 | prose | pages [15] -->
The ﬁnal expression of evaluating one paper’s inﬂuence degree is:

<!-- b000269 | prose | pages [15] -->
Ti = αIFIFi +αHHi +αrri (16)

<!-- b000270 | prose | pages [15] -->
In the following ,we test the consistency of the AHP.

<!-- b000271 | prose | pages [15] -->
1. The consistency index CI = λmax−n should be close to 0;we get CI = 0.0516 n−1

<!-- b000272 | prose | pages [15] -->
2. The consistency ratio CR = CI CR should be less than 0.1;We get CR = 0.02. Hence, our decision method displays perfectly acceptable consistency and weights are reasonable.

<!-- b000273 | prose | pages [15] -->
List the top ﬁve inﬂuence degree, shown in Table 4:

<!-- b000274 | caption | pages [15] -->
Table 4: The schematic diagram of papers’ indexes

<!-- b000275 | prose | pages [15] -->
rank Paper’s number H IF r

<!-- b000276 | prose | pages [15] -->
1 2 39 44.982 1.4547 2 4 102 31.853 1.9397 3 13 39 32.182 1.5764 4 12 39 31.853 -0.6369 5 7 25 32.182 -0.6139

<!-- b000277 | prose | pages [15] -->
In the ﬁrst three tasks, we have solved the problem of measuring the inﬂuence degree of researchers and papers. If we are able to get enough information about research papers and researchers, we can create a research database. If we want to evaluate the research strength of a university or a department in a certain ﬁeld, we need to look for the researchers and the research papers in recent years of this organization ,then inquire their inﬂuence in the database. Finally we can determine the strength of it by choosing a suitable evaluation (such as TOPSIS).

<!-- b000278 | heading | pages [15] -->
6 Model Extension

<!-- b000279 | prose | pages [15] -->
In model one and model two, using the network model, we quantify the inﬂuence of researchers and papers, showing the strong ability of our model to evaluate academic index. As a matter of a fact, our models can be applied in various ﬁelds seemingly have nothing to do with science. So in the following section, we will employ our network model to evaluate the inﬂuence of Chinese movie stars, and consider its extension widely.

<!-- b000280 | furniture | pages [16] -->
Team # 28747

<!-- b000281 | furniture | pages [16] -->
Page 14 of 19

<!-- b000282 | heading | pages [16] -->
6.1 Applying models to a speciﬁc area

<!-- b000283 | prose | pages [16] -->
The cinema of Hong Kong is one of the three major threads in the history of Chi- nese language cinema, alongside the cinema of China, and the cinema of Taiwan. For decades, Hong Kong was the third largest motion picture industry in the world and the second largest exporter. So it is obvious that the industry of Hong Kong’s cinema plays such a predominate role in China and even the whole world that it has greatly prompt- ed the development of the cinema industry in Taiwan and Chinese mainland. There are some illuminated movie stars from Hong Kong, such as Jackie Chan, Tony leung chiu wai, Andy Lau and so on who also have a great reputation around the world.[6]

<!-- b000284 | prose | pages [16] -->
For the fact that Tony leung chiu wai has a very magniﬁcent cinema career, including being awarded the Golden Horse best actor nomination more than once, we decide to replace the Erd¨os in the previous network model with him, and then qualify the range of time and the region, in ordering that we can construct a new network model based on the Model 1 which can be used to assess a movie star’s inﬂuence degree.

<!-- b000285 | prose | pages [16] -->
For the fact that Tony leung chiu wai has a very magniﬁcent cinema career, including being awarded the Golden Horse best actor nomination more than once, we decide to replace the Erd¨os in the previous network model with him, and then qualify the range of time and the region, in ordering that we can construct a new network model based on the Model 1 which can be used to assess a movie star’s inﬂuence degree.

<!-- b000286 | prose | pages [16] -->
Besides that, we also need an index to assess each actor’s effect on the Chinese mainland’s box-ofﬁce, and the index can be considered as the importance degree of Model 1 as a balance of a actor’s strength. We normalize the average of the box-ofﬁce of movies where each actor has participated in recent ﬁve years as the number of this box-ofﬁce’s inﬂuence.

<!-- b000287 | caption | pages [16] -->
Table 5: The indexes of the movie starts

<!-- b000288 | prose | pages [16] -->
Name rank degrees inﬂuence degree box-ofﬁce

<!-- b000289 | prose | pages [16, 17] -->
1 11 Zhou Xun 0.4213 0.9128 2 9 Zhao Wei 0.3612 0.9578 3 11 Takeshi Kaneshiro 0.3488 0.6770 4 16 Andy Lau 0.3443 0.6058 5 15 Zhang Ziyi 0.3122 0.5697 6 11 Shu Qi 0.2789 0.6422 7 8 Jet Li 0.2633 0.7619 8 9 Donnie Yen 0.2315 0.5731 9 8 Jackie Chan 0.2183 0.9323 10 8 Louis Koo 0.1319 0.3273 Putting the number into the matrix depicting the cooperated relationship between different actors, we can get the numerical data of the 31 actors inﬂuence degree using the PageRank algorithm. Ranking the stars by the inﬂuence degree, we can get the Top ten shown in the chart:

<!-- b000290 | furniture | pages [17] -->
Team # 28747

<!-- b000291 | furniture | pages [17] -->
Page 15 of 19

<!-- b000293 | prose | pages [17] -->
Analyzing the Table 5, we can ﬁnd out that the box-ofﬁce indicating the actors strength has some contribution on the stars inﬂuence, but the actors cooperating rela- tionship network also is an unignorable factor. Taking Zhang Ziyi as an example, while she has a inferior box-ofﬁce than other stars, we just ﬁnd the corresponding node has a higher degree, that is ,she has many more cooperated stars than others, which results in her higher inﬂuence degree. However, the Jackie Chan is an odd case, he mainly partici- pated in the action movies, adding his lack of cooperation with mainland actors, thus his overall inﬂuence is not that superior despite of his strong box-ofﬁce.

<!-- b000294 | prose | pages [17] -->
What’s more, the current top ten stars on inﬂuence almost have a worldwide reputa- tion, such as Jackie Chan, Jet Li, Zhang Ziyi, Zhou Xun and so on. On the other side, some inferior-reputation stars are located in the relatively low position in the inﬂuence ranking. In conclusion, using the network model to assess the inﬂuence degree of stars is appropriate and practicable.

<!-- b000295 | prose | pages [17] -->
Finally ,we just use the Tony leung chiu wai as a core to construct the stars’ cooper- ation network, which is absolutely not practicable for all of Chinese actors in the same way. This is our work’s limitation. However, we can still ﬁnd out the extensive prospect of our network model.

<!-- b000296 | heading | pages [17] -->
6.2 Analysis of models expansibility

<!-- b000297 | prose | pages [17] -->
In fact, our network model is valuable in the area that as long as the connection and interaction exist. In the following sections, we discuss the utility of network model into the ﬁelds of academic, military and social networks etc. Using model one and model two in one subject, we can evaluate the inﬂuence of researchers and papers. Assume the network is big enough to record the vast majority of papers and researchers within one subject in it, and then we can establish a database to evaluate the inﬂuence of researchers and papers within the subject. Its signiﬁcance is self-evident as section 5.2 mentioned before, we can use a network model as a standard to judge the inﬂuence of a certain dis- cipline in a scientiﬁc research institution for the students who seeking master for further study to provide reliable reference. By adding virtual edge in the network, a researchers inﬂuential change can be simulated that he working with different colleagues. Thus it helps young scholars to plan their academic impact as soon as possible. But unfortu- nately, due to the measurement of research indexes (such as H index, IF etc.) for various disciplines is different. How to create a research database that contains various disci- plines requires people to further study.

<!-- b000298 | prose | pages [17, 18] -->
Assume each node represents a particular city and edge represents the relationship between cities and transportation, considering economic, transportation and other index- es to measure the importance of every city, we can build a network model available to evaluate the inﬂuence of the city. For example, when forces attacked a certain area, as a commander, he can use this network model to ﬁnd the one of the most inﬂuential city in a certain area to destroy prior in order to weaken the enemy forces.

<!-- b000299 | furniture | pages [18] -->
Team # 28747

<!-- b000300 | furniture | pages [18] -->
Page 16 of 19

<!-- b000302 | prose | pages [18] -->
In addition, we can generalize the use of this model into social networking sites, such as Twitter and Facebook. Network users could be seen as nodes in the network and the friendship between network users represent the edge in the network. Algorithm of model 1 and model 2 can be used to identify each user’s inﬂuence in the social network. We can simulate the useful or junk information transmission in the Internet by mapping the users inﬂuence into the probability that one person forward its friends short blogs. Thus, it helps researchers to further study on this aspect.

<!-- b000303 | prose | pages [18] -->
Thus it can be seen that our network model in the treatment of the relationship and mutual inﬂuence of this kind of problem has a wide range of application scope, and generally can give effective solutions. Thus, our model posses science, understanding and utility.

<!-- b000304 | heading | pages [18] -->
7 Error/Sensitivity Analysis

<!-- b000305 | heading | pages [18] -->
7.1 Sensitivity analysis of the collaborative network

<!-- b000306 | prose | pages [18] -->
In model one, we build the network model describing relative collaboration among researchers. In the network, the importance degree of a node reﬂects its ability to com- municate with others and make different nodes connect with each other. Actually, it is the index to measure whether the researcher’s collaborative network is vast. We then discuss the value on the result of model calculation.

<!-- b000307 | prose | pages [18] -->
Through the analysis in section 4.1.3, we can get the rank list of all the nodes’ q value. Considering the researcher of ALON, NOGA M with the maximum q value, CONWAY, JOHN HORTON with the middle q value, GUNDERSON, DAVID SHANE with the minimum q value, we delete respectively these nodes which they represent in the network. Then, we use model one and model two to calculate the inﬂuence degree of every node in the total network, and get the new rank list of p.

<!-- b000308 | prose | pages [18] -->
Set the ranking of node j before deleting node i is oi j, and the ranking of node j after deleting node i is mij. Then we can deﬁne the Deviation Degree between the old results and the new ranking results after deleting node i as Ei.

<!-- b000309 | prose | pages [18] -->
i.e. n |oi j −mi j| ∑ j Ei = (17) n The results as shown in Table 6:

<!-- b000310 | furniture | pages [19] -->
Team # 28747

<!-- b000311 | furniture | pages [19] -->
Page 17 of 19

<!-- b000312 | caption | pages [19] -->
Table 6: Deviation Degree of results

<!-- b000313 | prose | pages [19] -->
Name E q

<!-- b000314 | prose | pages [19] -->
ALON, NOGA M 41.5730 0.2070 CONWAY, JOHN HORTON 14.8052 0.0794 GUNDERSON, DAVID SHANE 8.0745 0.0484

<!-- b000315 | prose | pages [19] -->
According to the above data, we can see that for a certain node, the bigger of q value, the stronger of the researcher’s communication with each other, then the more inﬂuential contribution of the node to the calculation results in the total networks. That is to say, if we delete the nodes with large values of the importance degree, the inﬂuence degree of other nodes in the network may even have colossal changing! In addition, for some nodes with small q values, due to their less contact with other nodes, even though we delete them from the network, it doesn’t have a great inﬂuence on the ﬁnal results.

<!-- b000316 | heading | pages [19] -->
7.2 Sensitivity analysis of the citing network

<!-- b000317 | prose | pages [19] -->
In the section §5.1, we build the relational network based on the condition of citing among the 15 papers. We analyzed that there exists the feedback in the citing relation among papers, and assumed that the effect of the interaction is equal between two nodes which have citing relation.

<!-- b000318 | prose | pages [19] -->
It is unquestionable that the feedback of citing is subsistent. Note that assume paper A cites paper B, the inﬂuence of paper A would affect paper B obviously, but the impact which B inﬂuences on A is not always equal to the effect of A to B. Under the circum- stances, we call A as the citing paper, and B as the cited paper. Then we set the impact ratio of B to A and A to B as u. Having assumed the value of u is 1 in the section 5, now we try to change the value and observe the variation of results.

<!-- b000319 | caption | pages [19] -->
Figure 6: The schematic diagram reﬂects citation relation of A and B

<!-- b000320 | prose | pages [19] -->
Similarity, we deﬁne E as the index to measure Deviation Degree of the results. But the difference is that we consider the Deviation Degree between the new ranking result and the old one has been calculated in section 5.1.

<!-- b000321 | furniture | pages [20] -->
Team # 28747

<!-- b000322 | furniture | pages [20] -->
Page 18 of 19

<!-- b000323 | prose | pages [20] -->
The following Figure 7 reﬂects the E along with the changes of the u.

<!-- b000324 | caption | pages [20] -->
Figure 7: The changing of the Deviation Degree along with u

<!-- b000325 | prose | pages [20] -->
For a evaluation model, we hope that it can be stable as much as possible, and will not vary greatly because of some small changes in the parameters. Observing this ﬁgure, we can ﬁnd that the calculation results on the whole will produce certain change along with the different values of u. However, when u gets in the interval of [0.7,1], the variation of the results is relatively small, so it’s appropriate that we put u into this interval.

<!-- b000326 | heading | pages [20] -->
8 Analysis of the Model

<!-- b000327 | heading | pages [20] -->
8.1 Strengths

<!-- b000328 | prose | pages [20] -->
• In model one, we not only consider the degree of nodes, but also consider the nodes’ clustering coefﬁcient.

<!-- b000329 | prose | pages [20] -->
• In model two, we use PageRank algorithm to evaluate the connection among re- searches, reﬂecting the mutual inﬂuence of nodes in the network.

<!-- b000330 | prose | pages [20] -->
• In model three, we successfully quantify various indicators and consider the exter- nal factors and internal factors at the same time. So our results are comprehensive and objective.

<!-- b000331 | prose | pages [20] -->
• Our models are sensitive and show a great adaptability , and can be applied in various aspects.

<!-- b000332 | heading | pages [20] -->
8.2 Weaknesses

<!-- b000333 | prose | pages [20] -->
• Because the lack of data, we only choose a small part of papers to analyze.

<!-- b000334 | prose | pages [20] -->
• In model three, the weight is calculated by AHP. So our results exist subjectivity.

<!-- b000335 | prose | pages [20] -->
• When extending our model, we only choose 32 actors to build the network rela- tionship. The scale is relative small.

<!-- b000336 | furniture | pages [21] -->
Team # 28747

<!-- b000337 | furniture | pages [21] -->
Page 19 of 19

<!-- b000338 | heading | pages [21] -->
References

<!-- b000339 | references | pages [21] -->
[1] Ren Zhuoming;Shao Feng;Liu Jianguo;Guo Qiang;Wang Binghong,Node importance measurement

<!-- b000340 | references | pages [21] -->
based on the degree and clustering coefﬁcient information,Acta Phys.Sin. Vol.62,No.12(2013)

<!-- b000341 | references | pages [21] -->
[2] Zhao Guo; Song Jiancheng, The mathematical model and its application of Google’s search. Journal

<!-- b000342 | references | pages [21] -->
of Southwest Universities Nature Science Edition,May 2010

<!-- b000343 | references | pages [21] -->
[3] Shao Jingjing;Feng Bo;Li Bo,PageRank algorithm ranking of the new technology,JOURNAL OF

<!-- b000344 | references | pages [21] -->
HUAZHONG NORMAL UNIVERSITY(Nat. Sci.),Vol.42 No.4,Dec 2008

<!-- b000345 | references | pages [21] -->
[4] Watts D J, Strogatz S H, Nature 393 440,1998

<!-- b000346 | references | pages [21] -->
[5] Codd E F,Commun. ACM 13 37,1970

<!-- b000347 | references | pages [21] -->
[6] Cinema of Hong Kong

<!-- b000348 | references | pages [21] -->
http://en.wikipedia.org/wiki/Hong Kong movie scholar.google.com

<!-- b000349 | references | pages [21] -->
[7] web of science

<!-- b000350 | references | pages [21] -->
http://www.medsci.cn/sci/
