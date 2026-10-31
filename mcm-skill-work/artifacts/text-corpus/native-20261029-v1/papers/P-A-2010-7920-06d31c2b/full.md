# P-A-2010-7920-06d31c2b

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team Control Number

<!-- b000002 | title | pages [1] -->
7920

<!-- b000003 | prose | pages [1] -->
For office use only

<!-- b000004 | prose | pages [1] -->
T1 ________________

<!-- b000005 | prose | pages [1] -->
T2 ________________

<!-- b000006 | furniture | pages [1] -->


<!-- b000007 | prose | pages [1] -->
T3 ________________

<!-- b000008 | prose | pages [1] -->
For office use only

<!-- b000009 | prose | pages [1] -->
F1 ________________

<!-- b000010 | prose | pages [1] -->
F2 ________________

<!-- b000011 | prose | pages [1] -->
F3 ________________

<!-- b000012 | prose | pages [1] -->
Problem Chosen

<!-- b000013 | prose | pages [1] -->
T4 ________________

<!-- b000014 | furniture | pages [1] -->


<!-- b000015 | prose | pages [1] -->
F4 ________________

<!-- b000016 | title | pages [1] -->
A

<!-- b000017 | furniture | pages [1] -->


<!-- b000018 | furniture | pages [1] -->


<!-- b000019 | heading | pages [1] -->
2010 Mathematical Contest in Modeling (MCM) Summary Sheet

<!-- b000020 | prose | pages [1] -->
(Attach a copy of this page to each copy of your solution paper.)

<!-- b000021 | title | pages [1] -->
Brody Power Model:

<!-- b000022 | prose | pages [1] -->
An Analysis of Baseball’s Sweet Spot

<!-- b000023 | furniture | pages [1] -->


<!-- b000024 | furniture | pages [1] -->


<!-- b000025 | prose | pages [1] -->
February 22, 2010

<!-- b000026 | furniture | pages [1] -->


<!-- b000027 | prose | pages [1] -->
The sport of baseball is a web of complex interactions between numerous elements of basic physics.  The typical player, however, is more concerned with stepping into the batter’s box and striking the ball as efficiently and as far as possible.  In over 100 years of professional baseball, players have learned through experience that the optimum location to strike the ball exists in the thick portion of the barrel, a location known as the “sweet spot.”  However the concept of the sweet spot clashes with a basic tenet of physics: torque.  Torque predicts that the optimal location of contact would exist at the very end of the bat.  The driving force behind this paper is to develop a model which remedies this conflict.  In our report, we identify two models for the sweet spot, each based on a different definition: the first is based on the center of percussion, and the second is referred to as the “Brody Power Model.”  We determine the Brody Power Model is superior and use it to examine how the performance of a wooden bat is affected by “corking” it or constructing it from aluminum instead.  The model relatively accurately contrasts the performance of different bats based on a variety of parameters, including mass, angular velocity, and moment of inertia.  Testing with the Brody Model shows that corking may increase the angular velocity of the swing, but yields a negligible difference in power, while aluminum provides a clearly noticeable improvement in performance.  To test the sensitivity of our model, we examine the effects of changes in bat parameters.  While it does lack some sensitivity and is limited in its ability to precisely predict outcomes, we ultimately conclude that the Brody Model is the ideal method for an assessment of the interplay between power and sweet spot location.

<!-- b000028 | furniture | pages [2] -->
Control #7920

<!-- b000029 | furniture | pages [2] -->


<!-- b000030 | furniture | pages [2] -->
Page 1 of 23

<!-- b000031 | furniture | pages [2] -->


<!-- b000032 | furniture | pages [2] -->


<!-- b000033 | heading | pages [2] -->
Contents

<!-- b000034 | furniture | pages [2] -->


<!-- b000035 | contents | pages [2] -->
1.  Introduction .............................................................................................................................................. 2

<!-- b000036 | contents | pages [2] -->
2. The Plan .................................................................................................................................................... 2

<!-- b000037 | contents | pages [2] -->
3: Objectives ................................................................................................................................................. 3

<!-- b000038 | contents | pages [2] -->
4. Defining the “Sweet Spot” ........................................................................................................................ 4

<!-- b000039 | contents | pages [2] -->
5. Model A- Center of Percussion: Physics’ Sweet Spot .............................................................................. 5

<!-- b000040 | contents | pages [2] -->
5-b. Example I ........................................................................................................................................... 5

<!-- b000041 | contents | pages [2] -->
6. Model B: Brody Power Model .................................................................................................................. 6

<!-- b000042 | contents | pages [2] -->
6-a.  Facts and Assumptions ..................................................................................................................... 6

<!-- b000043 | contents | pages [2] -->
6-b. General Form ..................................................................................................................................... 7

<!-- b000044 | contents | pages [2] -->
6-c. Example II.......................................................................................................................................... 9

<!-- b000045 | contents | pages [2] -->
6-d. Torque ................................................................................................................................................ 9

<!-- b000046 | contents | pages [2] -->
7. Discussion ............................................................................................................................................... 10

<!-- b000047 | contents | pages [2] -->
7-a.  “Corking” ........................................................................................................................................ 10

<!-- b000048 | contents | pages [2] -->
7-b. Cork Model Augmentation .............................................................................................................. 11

<!-- b000049 | contents | pages [2] -->
7-c . Aluminum vs. Wood ....................................................................................................................... 13

<!-- b000050 | contents | pages [2] -->
7-d. Aluminum Model Augmentation ..................................................................................................... 13

<!-- b000051 | contents | pages [2] -->
8. Sensitivity Analysis ................................................................................................................................ 15

<!-- b000052 | contents | pages [2] -->
9. Conclusion .............................................................................................................................................. 19

<!-- b000053 | contents | pages [2] -->
10. References ............................................................................................................................................. 22

<!-- b000054 | furniture | pages [2] -->


<!-- b000055 | furniture | pages [2] -->


<!-- b000056 | furniture | pages [2] -->


<!-- b000057 | furniture | pages [2] -->


<!-- b000058 | furniture | pages [3] -->
Control #7920

<!-- b000059 | furniture | pages [3] -->


<!-- b000060 | furniture | pages [3] -->
Page 2 of 23

<!-- b000061 | furniture | pages [3] -->


<!-- b000062 | furniture | pages [3] -->


<!-- b000063 | heading | pages [3] -->
1.  Introduction

<!-- b000064 | furniture | pages [3] -->


<!-- b000065 | prose | pages [3] -->
Be it the crack of the bat, the roar of the crowd, or the taste of a juicy ballpark hot dog, something about the sport of baseball has had an indelible impact on the American psyche. The sport has developed its own vernacular, with pitchers “busting” hitters inside with “high cheddar,” and batters “dropping bombs” over the outfield fence. Ask a player what is meant by these phrases, or how one would go about quantifying what constitutes “cheddar,” and one would be hard pressed to form a concrete definition. A similarly obscure phenomenon is the “sweet spot” of a baseball bat, a concept intuitively understood by even the most junior players, but which is very difficult to define.

<!-- b000066 | prose | pages [3] -->
For the purposes of this paper, the sweet spot represents the spot on the thick part of the barrel where maximum power is transferred to the ball upon contact. While a simple explanation based on torque would point to the end of the barrel as the sweet spot, the empirical evidence gathered by well over a century of play clearly shows that this is not the case. Even the average youth baseball player can demonstrate from experience that the sweet spot occurs somewhere in the middle of the thick part of the barrel. The purpose of this investigation is to develop a model that explains this empirical phenomenon. Additionally, we will attempt to investigate the effects of different parameters upon a bat-ball collision, specifically how they affect location and effectiveness of the sweet spot. Included in this investigation is an examination of the utility of “corking” a bat, as well as an examination of the differences observed between the performances of wooden and aluminum bats.

<!-- b000067 | heading | pages [3] -->
2. The Plan

<!-- b000068 | prose | pages [3] -->
Our goal is to develop a model which will explain the empirical finding that the sweet spot of a baseball bat cannot be explained by a simple analysis of torque. In order to achieve this, our team must:

<!-- b000069 | prose | pages [3] -->
 Identify Objectives:

<!-- b000070 | prose | pages [3] -->
In order to evaluate our model, we must describe the criteria of a successful model as it relates to this scenario.

<!-- b000071 | furniture | pages [3] -->


<!-- b000072 | prose | pages [3] -->
 Define Terms:

<!-- b000073 | prose | pages [3] -->
The word “sweet spot” can mean different things to various camps in the baseball world. Thus we must standardize all of our terms, especially the sweet spot, in order to develop context for our model and minimize confusion.

<!-- b000074 | furniture | pages [3] -->


<!-- b000075 | heading | pages [3] -->
 State Assumptions:

<!-- b000076 | prose | pages [3] -->
The collision between bat and ball involves numerous variables. In order to develop a useable model, we will make some assumptions about the nature of minor variables in the scenario. We will revisit these assumptions as they become pertinent.

<!-- b000077 | furniture | pages [4] -->
Control #7920

<!-- b000078 | furniture | pages [4] -->


<!-- b000079 | furniture | pages [4] -->
Page 3 of 23

<!-- b000080 | furniture | pages [4] -->


<!-- b000081 | furniture | pages [4] -->


<!-- b000082 | heading | pages [4] -->
 Develop Models:

<!-- b000083 | prose | pages [4] -->
The next step is to create multiple working models that can accurately explain the location and effects of the sweet spot.

<!-- b000084 | furniture | pages [4] -->


<!-- b000085 | heading | pages [4] -->
 Sensitivity Analysis:

<!-- b000086 | prose | pages [4] -->
In order to be effective and useful, a model must be consistent when parameters are varied.  To test the effect of changing assumptions, we will produce a sensitivity analysis that shows whether our model is properly sensitive to these variations.

<!-- b000087 | heading | pages [4] -->
3. Objectives

<!-- b000088 | prose | pages [4] -->
This report is produced with a baseball audience in mind. We want the average baseball enthusiast to be able to read our paper and gain some understanding of a few of baseball’s fundamental questions: the sweet spot, the effects of corking, and effects of differences between bat materials.  To guide the presentation of our model, we have focused on four primary objectives:

<!-- b000089 | heading | pages [4] -->
1. Answering the Problem

<!-- b000090 | prose | pages [4] -->
 Provide a model which explains why torque is not the determining factor for the sweet spot.

<!-- b000091 | prose | pages [4] -->
 Use this model to test the effects of corking a bat.

<!-- b000092 | prose | pages [4] -->
 Use this model to test for variations in performance between wooden and metal bats.

<!-- b000093 | heading | pages [4] -->
2. Simplicity and Clarity

<!-- b000094 | prose | pages [4] -->
 Is the material presented in the most simple and straightforward way possible?

<!-- b000095 | prose | pages [4] -->
 Could this report be included in a baseball publication and targeting a baseball audience with minimal mathematical inclination, while still providing sufficient evidence for its conclusions?

<!-- b000096 | prose | pages [4] -->
This will guide the paper in the direction of efficient reading—focusing on concise and informative presentation.

<!-- b000097 | heading | pages [4] -->
3. Applicability

<!-- b000098 | prose | pages [4] -->
 Does the model translate well to explaining real world phenomenon?  Is the data generated useful outside of a laboratory setting?

<!-- b000099 | prose | pages [4] -->
This model should not only describe the parameters which govern the sweet spot, but should also provide a relative location or zone that fits empirically recognized norms.

<!-- b000100 | heading | pages [4] -->
4. Resiliency

<!-- b000101 | prose | pages [4] -->
 Can this model accommodate reasonable fluctuation in input data?

<!-- b000102 | furniture | pages [5] -->
Control #7920

<!-- b000103 | furniture | pages [5] -->


<!-- b000104 | furniture | pages [5] -->
Page 4 of 23

<!-- b000105 | furniture | pages [5] -->


<!-- b000106 | furniture | pages [5] -->


<!-- b000107 | prose | pages [5] -->
A change in variables should not “throw our model a curve ball.” Our goal is to create a model which will be able to explain the function and effects of the sweet spot for a multitude of varying parameters.

<!-- b000108 | heading | pages [5] -->
4. Defining the “Sweet Spot”

<!-- b000109 | furniture | pages [5] -->


<!-- b000110 | prose | pages [5] -->
The concept of the sweet spot has acquired numerous definitions over the years. Many theories for baseball’s sweet spot have been proposed; occasionally definitions overlap or contradict each other.  It is important that we explain which definitions of the sweet spot we are referring to in order to minimize confusion.

<!-- b000111 | prose | pages [5] -->
 Center of Percussion (COP) The center of percussion has historically been identified with the concept of the sweet spot for implements such as baseball bats and tennis rackets. When a force is applied at the COP (in this case from the force of the bat-ball collision) no vibration is felt at the pivot point.[3] [4] Thus, the COP is often tied to the tactile feeling of the sweet spot, where the hitter feels little to no sting in his hands.[4] The COP has commonly been measured using a pivot point located 6 inches above the knob, just below the right hand of a typical batter.  However, recent research has demonstrated that the pivot point exists below the knob of the bat in the moment prior to contact, and so the usefulness of the COP as a judge of performance has been called into question.[3]

<!-- b000112 | prose | pages [5] -->
 Location of Maximum Performance An alternate definition of the sweet spot is the strike location that yields maximum performance; this depends on the definition of maximum performance itself. In past studies, the exit velocity of the ball has been used as one possible metric, forming the basis for the Ball Exit Speed Ratio (BESR) testing used to certify high school and college bats.[3]  These tests measure the velocity of the ball before and after the collision, creating a ratio of the departure speed over the impact speed.  This ratio is commonly known as the coefficient of restitution (COR).  It illustrates how much energy the ball maintains after contact with the bat—the higher the value the more efficient the collision. Ratios above a certain level are deemed illegal for sanctioned high school and NCAA competition primarily for safety reasons. Limiting the COR limits the velocity of the ball as it leaves the bat, keeping batted balls below a relatively safe ceiling.[8]    Additional techniques show that this location changes with changing parameters such as initial speed of the ball and angular speed of the bat.

<!-- b000113 | prose | pages [5] -->
As we will see, the particular definition used will have a profound effect on the ability of a model to demonstrate why torque is not the controlling factor of sweet spot location.

<!-- b000114 | furniture | pages [5] -->


<!-- b000115 | furniture | pages [6] -->
Control #7920

<!-- b000116 | furniture | pages [6] -->


<!-- b000117 | furniture | pages [6] -->


<!-- b000118 | furniture | pages [6] -->


<!-- b000119 | furniture | pages [6] -->
Page 5 of 23

<!-- b000120 | furniture | pages [6] -->


<!-- b000121 | heading | pages [6] -->
5. Model A- Center of Percussion: Physics’ Sweet Spot

<!-- b000122 | prose | pages [6] -->
The center of percussion has long been identified in physics texts as being the location of the sweet spot.  The principle behind the COP relates to the interaction of rotational and translational motion caused by a ball striking a bat.  The translational force initiated by the ball

<!-- b000123 | prose | pages [6] -->
Figure 1

<!-- b000124 | prose | pages [6] -->
cause the entire bat to attempt to move in the same direction and speed at all points (Figure 1).  When the ball hits the bat, there is also the tendency for the bat to rotate around the center of mass due to rotational force (Figure 2). This rotational force increases the tendency of the handle to move in the opposite direction of the translational force.

<!-- b000125 | prose | pages [6] -->
The relative strength of these two forces

<!-- b000126 | prose | pages [6] -->
Figure 2

<!-- b000127 | prose | pages [6] -->
Center of

<!-- b000128 | prose | pages [6] -->
Mass

<!-- b000129 | prose | pages [6] -->
determines where the sweet spot is located.  If the baseball hits the bat between the COP and the end of the bat, the rotational force is stronger than the translational force acting on the handle. This imbalance of forces results in a tug on the handle as the bat tries to rotate out of the hands of the batter.  If the ball impacts the bat surface between the center of mass and the COP, the rotational force which acts on the handle is less than that of the translational force that pushes the handle.  As a result, the translational force is felt as a vibration which stings the batter’s hands. Either way, the lack of control in the follow-through is detrimental to the flight of the ball. Alternatively, when the ball impacts at the COP, the rotational and translational forces acting on the handle cancel out.  The collision feels smooth to the batter, and the lack of shock to the hands acts as an indicator that a solid hit has been made.

<!-- b000130 | prose | pages [6] -->
In order to determine the location of the COP mathematically, the following equation is used:[17]

<!-- b000131 | prose | pages [6] -->
where:

<!-- b000132 | furniture | pages [6] -->


<!-- b000133 | prose | pages [6] -->
 d = Distance from center of mass to center of percussion

<!-- b000134 | prose | pages [6] -->
 Icm = Moment of Inertia about the center of mass

<!-- b000135 | prose | pages [6] -->
 M = Mass of the bat  x = Distance from pivot point to center of mass  L = Length of bat

<!-- b000136 | furniture | pages [6] -->


<!-- b000137 | furniture | pages [6] -->


<!-- b000138 | furniture | pages [7] -->
Control #7920

<!-- b000139 | furniture | pages [7] -->


<!-- b000140 | prose | pages [7] -->
5-b. Example I

<!-- b000141 | furniture | pages [7] -->


<!-- b000142 | furniture | pages [7] -->


<!-- b000143 | furniture | pages [7] -->
Page 6 of 23

<!-- b000144 | furniture | pages [7] -->


<!-- b000145 | prose | pages [7] -->
To provide a point of comparison for later, we will assume that:[17]

<!-- b000146 | prose | pages [7] -->
 Icm = 0.048 kg m2  M = 0.905 kg  x = 0.51 m  L = 34 in

<!-- b000147 | prose | pages [7] -->
Inserting these values in the COP equation, we found the location of the sweet spot to be at about 26.531 inches from the knob, or approximately 7.5 inches from the free end of the bat. While this distance is close to the expected values, it falls just outside the accepted 4-7 inches from the end of the bat specified by physicist Rod Cross.[5]

<!-- b000148 | prose | pages [7] -->
While the COP model of explaining the sweet spot is supported by sound physics, it isn’t as sensitive as we require.  The location of the sweet spot according to the COP is based upon the position where the forces induced by the ball balance out, and is found by taking into account a few structural specifications of the bat.  Several problems exist with this definition of the sweet spot.  When the bat is swung, it produces rotational and translational forces which interact with those of the baseball.  The interactions of momentum and forces cause fluctuations in the location of the optimal impact point, which in turn affects the velocity at which the ball leaves the bat.  Also, since this is based on feel, there is theoretically a different position for the COP for every point that is covered by the batter’s hands.[5]

<!-- b000149 | heading | pages [7] -->
6. Model B: Brody Power Model

<!-- b000150 | prose | pages [7] -->
After investigating the COP as a possible location of maximum performance, we have determined that it is inadequate for our purposes, and another model is required. Thus, the Brody Power Model* is presented.

<!-- b000151 | heading | pages [7] -->
6-a.  Facts and Assumptions

<!-- b000152 | prose | pages [7] -->
Equations: The derivation of this model stems from a combination of the three concepts below:

<!-- b000153 | prose | pages [7] -->
Conservation of Linear Momentum: Conservation of Angular Momentum: Definition of Coefficient of Restitution:

<!-- b000154 | furniture | pages [7] -->


<!-- b000155 | furniture | pages [7] -->


<!-- b000156 | furniture | pages [7] -->


<!-- b000157 | furniture | pages [7] -->


<!-- b000158 | furniture | pages [7] -->


<!-- b000159 | furniture | pages [7] -->


<!-- b000160 | furniture | pages [7] -->


<!-- b000161 | prose | pages [7] -->
* To our knowledge, this process has not previously been named the “Brody Power Model”. It is named as such in this document to give credit to Brody as the primary source for this model.

<!-- b000162 | furniture | pages [8] -->
Control #7920

<!-- b000163 | furniture | pages [8] -->


<!-- b000164 | furniture | pages [8] -->
Page 7 of 23

<!-- b000165 | furniture | pages [8] -->


<!-- b000166 | furniture | pages [8] -->


<!-- b000167 | furniture | pages [8] -->


<!-- b000168 | prose | pages [8] -->
Definition of Variables:

<!-- b000169 | prose | pages [8] -->
 m = Mass of Ball  M = Mass of Bat  vi = Initial Velocity of Baseball  vf = Final Velocity of Baseball  ωi = Initial Angular Velocity of Bat  ωf = Final Angular Velocity of Bat  Vf = Final linear velocity of bat  I = Moment of Inertia: A measure of resistance to rotational motion.  e = Coefficient of Restitution  b = Distance from Ball Impact to Pivot Point  L = Length of bat

<!-- b000170 | heading | pages [8] -->
Simplifying Assumptions

<!-- b000171 | prose | pages [8] -->
Vf is equal to 0. 

<!-- b000172 | prose | pages [8] -->
ωf is equal to 0. 

<!-- b000173 | prose | pages [8] -->
Pivot Point is located 6 in from the bat knob 

<!-- b000174 | prose | pages [8] -->
6-b. General Form From the three given equations above, an all-encompassing equation can be derived that will allow b to be defined.  The fully derived equation comes from an essay written by physics professor H. Brody. The equation:

<!-- b000175 | furniture | pages [8] -->


<!-- b000176 | prose | pages [8] -->
is given as a method of determining how far from the center of mass a ball must impact in order to maximize the ball’s kinetic energy.  The Brody Power Equation was developed to merge the three root equations given above to yield the location that produces the maximum ball exit speed.

<!-- b000177 | furniture | pages [8] -->


<!-- b000178 | prose | pages [8] -->
The combination of these three equations is suggested by the physical nature of the problem. When a bat moves through space and comes into contact with a ball, both translational and rotational forces must be considered. As the bat is swung, it travels in an arc around a pivot point, which requires rotational motion to be taken into account.  The baseball itself travels in a straight line, causing the bat to experience a translational force on impact, and so linear velocity also comes into play. The equation for the COR is factored in because an indicator for the sweet spot is the greatest velocity of the ball following the collision relative to its initial velocity.

<!-- b000179 | furniture | pages [8] -->


<!-- b000180 | prose | pages [8] -->
The first step towards creating a model which maximizes velocity lies in combining the three preliminary equations while also isolating vf.  In order to accomplish this task, the following assumption is made, considerably easing the overall calculation:

<!-- b000181 | furniture | pages [8] -->


<!-- b000182 | furniture | pages [9] -->
Control #7920

<!-- b000183 | furniture | pages [9] -->


<!-- b000184 | furniture | pages [9] -->


<!-- b000185 | furniture | pages [9] -->


<!-- b000186 | furniture | pages [9] -->
Page 8 of 23

<!-- b000187 | furniture | pages [9] -->


<!-- b000188 | prose | pages [9] -->
 Set Vf  and ωf equal to 0 and eliminate them.  Since we are trying to maximize the movement of the ball, setting the final velocities of the bat to 0 indicates that all energy has been transferred to the ball.  While not empirically correct, the actual energy imparted to the ball does not matter for our purposes.  We are only concerned with modeling an estimated location of the sweet spot and its effectiveness relative to other bats.

<!-- b000189 | prose | pages [9] -->
Once these assumptions have been made and the given equations have been combined, the equation

<!-- b000190 | prose | pages [9] -->
Equation 1

<!-- b000191 | furniture | pages [9] -->


<!-- b000192 | prose | pages [9] -->
remains.  The next step is to manipulate Equation 1 in order to find the location on the bat that maximizes the COR, which correlates to a maximum value of vf.  To take this step, the following assumption is made:

<!-- b000193 | furniture | pages [9] -->


<!-- b000194 | prose | pages [9] -->
 The variable b is treated as the only unknown, while all other variables are treated as constants.  Later assumptions towards mass and velocity based on additional sources of data can take the place of these variables.

<!-- b000195 | furniture | pages [9] -->


<!-- b000196 | prose | pages [9] -->
This assumption is represented in

<!-- b000197 | prose | pages [9] -->
v f m s

<!-- b000198 | prose | pages [9] -->
Graph A, which plots the final velocity

<!-- b000199 | prose | pages [9] -->
53.4

<!-- b000200 | prose | pages [9] -->
of the ball against the position of the

<!-- b000201 | prose | pages [9] -->
53.2

<!-- b000202 | prose | pages [9] -->
sweet spot.  In order to find the

<!-- b000203 | prose | pages [9] -->
53.0

<!-- b000204 | prose | pages [9] -->
maximum value of the function vf, it is necessary to take the first partial

<!-- b000205 | prose | pages [9] -->
52.8

<!-- b000206 | prose | pages [9] -->
derivative with respect to b.  Taking

<!-- b000207 | prose | pages [9] -->
52.6

<!-- b000208 | prose | pages [9] -->
the derivative of a function provides

<!-- b000209 | prose | pages [9] -->
52.4

<!-- b000210 | prose | pages [9] -->
the slope of that function at any point

<!-- b000211 | prose | pages [9] -->
52.2

<!-- b000212 | prose | pages [9] -->
along the curve.  At the maximum value the graph is neither increasing

<!-- b000213 | prose | pages [9] -->
Final Speeds at Given Distance from Pivot

<!-- b000214 | prose | pages [9] -->
Graph A

<!-- b000215 | prose | pages [9] -->
b m 0.1 0.2 0.3 0.4 0.5 0.6 0.7

<!-- b000216 | prose | pages [9] -->
nor decreasing, so the first derivative will be 0.  It is then possible to find where on the bat a ball = 0, which will represent the point on the bat at which the must make contact in order to make greatest final ball velocity is found.

<!-- b000217 | furniture | pages [9] -->


<!-- b000218 | prose | pages [9] -->
Taking these assumptions into account, the first derivative of Equation 1 can be taken with respect to b so that

<!-- b000219 | furniture | pages [9] -->


<!-- b000220 | furniture | pages [9] -->


<!-- b000221 | furniture | pages [10] -->
Control #7920

<!-- b000222 | furniture | pages [10] -->


<!-- b000223 | furniture | pages [10] -->


<!-- b000224 | furniture | pages [10] -->


<!-- b000225 | furniture | pages [10] -->
Page 9 of 23

<!-- b000226 | furniture | pages [10] -->


<!-- b000227 | prose | pages [10] -->
Rearranging the variables and solving for b yields

<!-- b000228 | prose | pages [10] -->
Equation 2

<!-- b000229 | furniture | pages [10] -->


<!-- b000230 | prose | pages [10] -->
We now have the general form of an equation that can be used to find the optimum location to strike the ball.

<!-- b000231 | prose | pages [10] -->
6-c. Example II

<!-- b000232 | prose | pages [10] -->
With the general form in mind, the parameters can now be defined:

<!-- b000233 | prose | pages [10] -->
 Mass of Bat; M = 0.88451 kg

<!-- b000234 | prose | pages [10] -->
 Mass of Ball; m = 0.14529 kg  Moment of Inertia; I = 0.20556 kg m2 around 6 in mark from knob

<!-- b000235 | prose | pages [10] -->
 Initial Velocity of Baseball; vi = -42 m/s

<!-- b000236 | prose | pages [10] -->
 Initial Angular Velocity of Bat; ωi = 35.791 rad/s

<!-- b000237 | prose | pages [10] -->
 Length of Bat; L = 34 in

<!-- b000238 | prose | pages [10] -->
 Movement towards the outfield is oriented positively

<!-- b000239 | prose | pages [10] -->
Using Equation 2, it is possible to determine where the sweet spot exists in relation to the position predicted by torque.  We begin by researching common dimensions for baseballs, bats, pitch velocity, and angular velocity of the swing, shown above, in order to use realistic parameters.[9][7]  Putting this data into the equation yields

<!-- b000240 | furniture | pages [10] -->


<!-- b000241 | prose | pages [10] -->
The output dictates that b = 0.56557 m.  Converting from meters to inches, this becomes 22.267 in.  Moving this distance away from the axis of the moment of inertia (pivot point), assumed to be 6 inches, indicates that the optimal location for hitting the ball exists 28.267 inches from the knob, which is about 5.733 inches from the free end.  This position falls within the sweet spot zone of 4-7 inches proposed by Cross.[5]  After running multiple bats through the equation, we found the Brody Power Model to be relevant and consistent with empirical findings.

<!-- b000242 | prose | pages [10] -->
6-d. Torque

<!-- b000243 | prose | pages [10] -->
The example above demonstrates how the Brody model can be used to explain why torque is not the primary factor at play during the swing.  If the final velocity of the ball was based on torque, then the location of the sweet spot should have been as far away from the pivot point as possible. Torque is defined by the equation:

<!-- b000244 | furniture | pages [10] -->


<!-- b000245 | furniture | pages [11] -->
Control #7920

<!-- b000246 | furniture | pages [11] -->


<!-- b000247 | furniture | pages [11] -->
Page 10 of 23

<!-- b000248 | furniture | pages [11] -->


<!-- b000249 | furniture | pages [11] -->


<!-- b000250 | prose | pages [11] -->
where

<!-- b000251 | prose | pages [11] -->
 = Torque  = Force applied by ball  d = Distance from pivot point to impact  = Angle between incoming direction of ball and ball

<!-- b000252 | furniture | pages [11] -->


<!-- b000253 | prose | pages [11] -->
The way to maximize torque and energy, assuming all other variables are held constant, is to maximize the distance between the force and the fulcrum.  The farthest distance possible on a 34 inch bat is 28 inches away from the fulcrum, making the assumption that the 6 in. pivot point is used as the fulcrum.  Under normal circumstances, the optimal position for the ball to impact the bat is not 28 inches from the fulcrum; in this example, the optimal position was calculated to be 22 inches away.

<!-- b000254 | prose | pages [11] -->
Torque treats the entire bat as being uniform in composition and ignores principles of momentum.  When a bat is swung, the moment of inertia influences where the mass of the bat seems to concentrate.  This position is not the end of the bat, and so the end of the bat becomes less massive in relation to another point on the bat.  Taking principles of momentum into account, the ball will experience greater force if it is hit closer to the fulcrum.  Additionally, when balls hit near the end of the bat, they set off vibrations which both feel unpleasant and waste energy.[5]

<!-- b000255 | heading | pages [11] -->
7. Discussion

<!-- b000256 | prose | pages [11] -->
The Brody Power Model can be augmented to investigate issues involving corked bats and also to examine the differences between aluminum and wooden bats.

<!-- b000257 | prose | pages [11] -->
7-a.  “Corking”

<!-- b000258 | prose | pages [11] -->
The first recorded instance of corking in Major League Baseball (MLB) was September 7, 1974 by Graig Nettles of the New York Yankees.[12]  Corking a bat is generally a straightforward process. If the thick portion of the barrel is hollowed with an approximately half inch diameter hole and filled with a less dense and more elastic material, such as cork or bouncy balls, the bat is rendered considerably lighter, which allows for a faster swing.  One of the problems with hollowing out a bat is that the structural strength becomes compromised.  Corked bats have a nasty tendency—they shatter more easily upon contact with a fast pitch.  Using a corked bat entails a risk for the player, as MLB has been known to suspend players for up to eight games for a single offence.  A high profile bat corking incident occurred in 2003 when Sammy Sosa of the Chicago Cubs broke his bat in the first inning of a game versus the Tampa Bay Devil Rays, showering the third baseline with shards of wood and pieces of cork.[12]  Sosa claimed that he only used the corked bat to “put on a show” for fans by hitting homeruns during batting practice, while others have attempted to use corked bats to intentionally increase performance during games.  The question for the player then, is, “Is it worth it?”  After

<!-- b000259 | furniture | pages [12] -->
Control #7920

<!-- b000260 | furniture | pages [12] -->


<!-- b000261 | furniture | pages [12] -->
Page 11 of 23

<!-- b000262 | furniture | pages [12] -->


<!-- b000263 | furniture | pages [12] -->


<!-- b000264 | prose | pages [12] -->
augmenting our model, we find that the difference in ball speed produced by a corked bat is negligible.  Additional empirical findings back up this conclusion.

<!-- b000265 | heading | pages [12] -->
7-b. Cork Model Augmentation

<!-- b000266 | prose | pages [12] -->
When a bat is corked, several changes take place.  First, the mass of the bat decreases at

<!-- b000267 | furniture | pages [12] -->


<!-- b000268 | prose | pages [12] -->
the free end because the material used to fill the barrel is less dense than the wood of the bat itself.  This causes the weight of the entire bat to decrease, and also means that more of the weight is located closer to the hands.  This translates into a lower moment of inertia.  The combination of a lower moment of inertia and less weight in the bat results in a faster swing, given that the same amount of force is present.

<!-- b000269 | furniture | pages [12] -->


<!-- b000270 | prose | pages [12] -->
In order to determine how the interplay of these factors influences the final velocity of the ball, we began with our previous assumptions about the properties of a wooden baseball bat and made reasonable changes to those values based off of research to reflect corking:

<!-- b000271 | prose | pages [12] -->
 Wooden Bat Mass; Mw = 0.88451 kg

<!-- b000272 | prose | pages [12] -->
 Corked Bat Mass; Mc = 0.82781 kg

<!-- b000273 | prose | pages [12] -->
 Moment of Inertia- Wooden; Iw = 0.20556 kg m2 about the point 6 in from the knob

<!-- b000274 | prose | pages [12] -->
 Moment of Inertia- Corked; Ic = 0.19101 kg m2

<!-- b000275 | prose | pages [12] -->
 Mass of Ball; m = 0.14529 kg

<!-- b000276 | prose | pages [12] -->
 Length of Bat; L = 34 in

<!-- b000277 | prose | pages [12] -->
 Final Linear Velocity of Bat; Vf = 0*

<!-- b000278 | prose | pages [12] -->
 Initial Velocity of Ball; vi = -42 m/s

<!-- b000279 | prose | pages [12] -->
 Angular Velocity-Wooden; ωwi = 35.791 rad/s

<!-- b000280 | prose | pages [12] -->
 Angular Velocity- Corked; ωci = 36.5 rad/s

<!-- b000281 | prose | pages [12] -->
 Movement towards the outfield is oriented positively

<!-- b000282 | furniture | pages [12] -->


<!-- b000283 | prose | pages [12] -->
The first step in making this determination requires us to discover how the differences in mass, moment, and speed affect the location of optimal ball exit speed.  Using Brody’s Power Model, the value for the normal wooden bat remains bw = 0.56557, while the value of the corked bat is bc = 0.53847.  Once we have the value of b, it is possible to move a step backwards in the derivation of the Brody Power Model equation.  Recalling that

<!-- b000284 | furniture | pages [12] -->


<!-- b000285 | prose | pages [12] -->
and knowing that

<!-- b000286 | furniture | pages [12] -->


<!-- b000287 | prose | pages [12] -->
* While the assumption that the velocity of the bat is zero would not actually occur in reality, as long as it remains consistent throughout the procedure the results of the final speeds of the ball for different bats can be compared to approximate the effect of other factors.

<!-- b000288 | furniture | pages [12] -->


<!-- b000289 | furniture | pages [13] -->
Control #7920

<!-- b000290 | furniture | pages [13] -->


<!-- b000291 | furniture | pages [13] -->


<!-- b000292 | furniture | pages [13] -->


<!-- b000293 | furniture | pages [13] -->
Page 12 of 23

<!-- b000294 | furniture | pages [13] -->


<!-- b000295 | furniture | pages [13] -->


<!-- b000296 | prose | pages [13] -->
We assume that Vf = 0, so substituting the value of the coefficient of restitution (e) for this equation yields Equation 3.

<!-- b000297 | furniture | pages [13] -->


<!-- b000298 | furniture | pages [13] -->


<!-- b000299 | prose | pages [13] -->
Equation 3

<!-- b000300 | furniture | pages [13] -->


<!-- b000301 | prose | pages [13] -->
Now the only remaining unknown is vf.  Once we have the equation for vf set up, we simply have to use a calculating utility to substitute all of the known values into the relationship, solving for vf.  For the normal wooden bat we find a final ball speed of 53.502 m/s, while the corked bat had a ball speed of 53.810 m/s.  The nature of our assumptions precludes the results from being completely accurate under real world conditions.

<!-- b000302 | prose | pages [13] -->
The 0.31 m/s difference between the exit speeds can be explained by restrictions on the model.  The bat is treated as a solid mass that undergoes a perfect elastic collision with the ball. However, when corking a baseball bat, a certain amount of energy is lost to the material encased inside the wood.  This energy loss is not included within the model, and so more energy is attributed to the rebounding ball than would normally be seen.

<!-- b000303 | prose | pages [13] -->
In any case, the results of comparison seem to indicate that, contrary to the prevailing view, corking a bat does not have a significant effect upon the exit speed of the ball.  Based on these conclusions, in the case of his pregame power displays Sammy Sosa may have actually been decreasing his ability to hit homeruns by corking his bat.

<!-- b000304 | prose | pages [13] -->
Examining the phenomenon of bat corking from a purely sweet spot performance point of view does not adequately explain why Major League Baseball prohibits their use. If corking provides no discernable increase in final ball velocity, and may actually decrease the velocity of batted balls, then there appears to be no reason to prohibit their use[13]. This is because our model focuses only on the velocity of the batted ball, and leaves out other potential factors. The league’s problem with bat corking likely exists for a different reason.[13] As described above, corking the bat lowers the mass of the bat slightly, and also shifts the weight closer to the hitter’s hands. This allows the bat to be swung more easily and with a higher velocity. If a batter is concerned about contact, and not necessarily about launching balls over the centerfield wall, then it is conceivable that being able to swing a bat more easily would increase the ability to put the ball in play. The decreased time required to swing gives the experienced batter more time to decide whether or not to swing, and to adjust for unexpected ball trajectory. This is considered to be an unfair advantage in the eyes of Major League Baseball.

<!-- b000305 | furniture | pages [13] -->


<!-- b000306 | furniture | pages [14] -->
Control #7920

<!-- b000307 | furniture | pages [14] -->


<!-- b000308 | furniture | pages [14] -->
Page 13 of 23

<!-- b000309 | furniture | pages [14] -->


<!-- b000310 | furniture | pages [14] -->


<!-- b000311 | prose | pages [14] -->
7-c. Aluminum vs. Wood

<!-- b000312 | prose | pages [14] -->
Professional baseball has been around since the late 1800’s, with Major League Baseball receiving its genesis in 1903 from the combination of the American and National Leagues and the creation of the World Series.[11]  During this period wooden bats have been the only legal hitting instrument. Aluminum bats are a relatively new invention, having existed for roughly the past 40 years.[10] The prohibition of metal bats has a number of underlying causes.

<!-- b000313 | heading | pages [14] -->
7-d. Aluminum Model Augmentation

<!-- b000314 | prose | pages [14] -->
The difference between aluminum and wooden bats is modeled under the Brody Power Model following the same logic as our investigation of corking. We begin with our assumptions of the specific parameters for an aluminum bat:

<!-- b000315 | prose | pages [14] -->
 Mass of Bat; Ma = .89018 kg

<!-- b000316 | prose | pages [14] -->
 Moment of Inertia of Bat; Ia = 0.17055 kg m2

<!-- b000317 | prose | pages [14] -->
 Angular velocity of batωai = 38 rad/s

<!-- b000318 | prose | pages [14] -->
Substituting these values into Equation 2 causes an output value of ba = 0.50317. Turning next to Equation 3, used to find the final velocity for the cork augmentation, we substituted the above parameters and ended up with a final speed of vf = 54.258 m/s. This can be contrasted with the final ball speed off a regular wooden bat calculated at vf = 53.502 m/s during the original Brody example.  The difference between the wooden bat and the aluminum bat exit speeds in this example is about .756 m/s.  In English units, this is equivalent to 2.5 ft/s (1.7 MPH), enough extra speed to be more dangerous to a pitcher standing in the path of an oncoming ball.

<!-- b000319 | prose | pages [14] -->
It is worth briefly noting why the aluminum bat appears to be more effective than the corked bat in improving ball speed.  The difference stems from the corking process; when the wooden bat was corked, it lost mass in the free end and therefore lowered its moment of inertia. The aluminum bat is able to maintain the same weight as the unaltered wooden bat while also lowering its moment of inertia.  For both bats, the lower moment of inertia increases the angular speed at which it can be swung.  While the aluminum bat is indeed heavier than the corked bat, the it has a significantly lower moment of inertia. This allows the aluminum bat to swing more mass at a higher speed, which in turn contributes more force to the collision, increasing the velocity of the batted ball.

<!-- b000320 | furniture | pages [14] -->


<!-- b000321 | prose | pages [14] -->
While the Brody Power Model indicates that the aluminum bat has elevated performance at its position of maximum power, it does not accurately depict the degree to which this performance increases.  This is due to the fact that, while the model is sensitive to the masses of the objects involved in the collision, the speeds at which they are traveling, and the moment of inertia of the bat, it does not take into account a unique behavior exhibited by aluminum bats known as the trampoline effect.[14]

<!-- b000322 | furniture | pages [15] -->
Control #7920

<!-- b000323 | furniture | pages [15] -->


<!-- b000324 | furniture | pages [15] -->
Page 14 of 23

<!-- b000325 | furniture | pages [15] -->


<!-- b000326 | furniture | pages [15] -->


<!-- b000327 | furniture | pages [15] -->


<!-- b000328 | prose | pages [15] -->
The difference in behavior stems from the fact that the metal bat is malleable and hollow with a relatively thin shell, while the wooden bat is solid.  Taken together, this makes it possible for the metal bat to deform when struck by

<!-- b000329 | prose | pages [15] -->
Figure 3

<!-- b000330 | prose | pages [15] -->
a baseball that impinges upon it.  The resulting deformation takes the pattern of a quadrupole, meaning that it includes two sets of dipolar moments (Figure 3).[14]

<!-- b000331 | furniture | pages [15] -->


<!-- b000332 | prose | pages [15] -->
When the ball strikes the bat and causes this deformation, a transfer of energy takes place.  Kinetic energy from the ball is stored in the bat as an elastic potential energy when the bat morphs into the elongated oval shown in the second frame of Figure 3.  As the bat then moves to its next dipole that stored energy is transferred back to the ball as kinetic energy.  This extra push can return up to 20% of the energy contained by the ball prior to the collision.[15]  Combined with the energy delivered to the ball from the momentum of the bat, the ball is able to attain significantly higher speeds than conservation of momentum alone predicts. The Brody Power Model only accounts for the momentum portion of this dynamic. As a result, it is likely that the aluminum bat would produce an even higher ball exit velocity than is modeled here.

<!-- b000333 | furniture | pages [15] -->


<!-- b000334 | prose | pages [15] -->
The data produced by our model, in addition to the information on the trampoline effect, sheds light on the reasoning of Major League Baseball in prohibiting the use of the aluminum bat. We have identified two primary concerns:

<!-- b000335 | prose | pages [15] -->
 Safety: As discussed above, the aluminum bat imparts a higher exit velocity for the ball as it leaves the bat.  Wielded in the hands of today’s top athletes, this could pose an even greater risk to pitchers and corner infielders than already exists with wooden bats.

<!-- b000336 | furniture | pages [15] -->


<!-- b000337 | prose | pages [15] -->
 Tradition: Greater exit velocity for batted balls would impact the tradition and legacy of the game. A ball hit with an aluminum bat would be more likely to travel further than a ball hit with a wooden bat under the same conditions. This could lead to an inflation of home runs and extra base hits. The dimensions of Major League ballparks would likely be rendered inadequate, and the cherished achievements of Hall of Famers like Babe Ruth and Joe DiMaggio would be overshadowed by modern displays of technology. The damage to the integrity of the game surrounding the modern steroid scandal would likely pale in comparison to a change to aluminum bats.

<!-- b000338 | furniture | pages [15] -->


<!-- b000339 | furniture | pages [15] -->


<!-- b000340 | furniture | pages [15] -->


<!-- b000341 | furniture | pages [16] -->
Control #7920

<!-- b000342 | furniture | pages [16] -->


<!-- b000343 | furniture | pages [16] -->
Page 15 of 23

<!-- b000344 | furniture | pages [16] -->


<!-- b000345 | furniture | pages [16] -->


<!-- b000346 | heading | pages [16] -->
8. Sensitivity Analysis

<!-- b000347 | furniture | pages [16] -->


<!-- b000348 | prose | pages [16] -->
An examination of our processes and assumptions through a sensitivity analysis will allow us to gauge how well we have met the criteria of resiliency and applicability.

<!-- b000349 | prose | pages [16] -->
Is our data valid and realistic?

<!-- b000350 | furniture | pages [16] -->


<!-- b000351 | prose | pages [16] -->
The first step which must be taken in the analysis of our models is to determine the validity of the assumptions we used.

<!-- b000352 | prose | pages [16] -->
 Masses and Respective Moments of Inertia of Bats:

<!-- b000353 | prose | pages [16] -->
We referenced a table for the wood and aluminum bats, which included relevant specifications for our equations.[9]  Since mass and moment of inertia are interconnected, this ensured that combinations of the two variables reflect true properties of the different bats.  In the case of the corked bat, we researched sources which identified the reduction of mass by 2 oz when a bat is corked.[19]   We then made reasonable assumptions about the resulting change in the moment of inertia.

<!-- b000354 | prose | pages [16] -->
 Mass and Velocity of Ball:

<!-- b000355 | prose | pages [16] -->
MLB has very strict guidelines on the mass of the ball.  It must be between 5 and 5.25 oz.[18]  We therefore used an average ball mass of 5.125 oz. The velocity of the ball was determined by finding the average speed of a fastball, which we estimated around 93 mph.  The fastball is the best choice because a ball at this speed has the most kinetic energy and therefore potential for outgoing velocity.  In addition, this pitch type comes closest to a straight-line path; we used it as a consistent baseline for our models.

<!-- b000356 | furniture | pages [16] -->


<!-- b000357 | prose | pages [16] -->
 Velocity of Bat:

<!-- b000358 | prose | pages [16] -->
Much like mass and moment of inertia, we found empirical data that stated that the average bat swing is approximately 30 m/s.[7]  We set this as a baseline attached to the speed which a wooden bat would be swung at.  When the moment of inertia dropped during the change from wood to aluminum, we estimated that there would be a significant change in the speed with which the bat could be swung of roughly 4 MPH.[20] Since the corked bat had an intermediate moment of inertia, which leaned towards that of the wooden bat, we placed the velocity of the corked bat between the aluminum and wooden bats, slightly closer to that of the wooden bat.

<!-- b000359 | furniture | pages [16] -->


<!-- b000360 | prose | pages [16] -->
With the reasoning behind our assumptions in mind, we can now examine the sensitivity of the model to each variable.  The only variables not included in this section are the mass of the ball and the location of optimal ball exit speed.  The ball mass is not included because the range of possible masses is so narrow that for our purposes it does not vary.  The value for the distance is not included because distance is completely dependent on the interplay of the other values.

<!-- b000361 | furniture | pages [16] -->


<!-- b000362 | prose | pages [16] -->
First, we decided to determine under what conditions our model would be useful.  Using the specifications of the wooden bat as a baseline, we plotted a three-dimensional graph of the

<!-- b000363 | furniture | pages [17] -->
Control #7920

<!-- b000364 | furniture | pages [17] -->


<!-- b000365 | furniture | pages [17] -->


<!-- b000366 | furniture | pages [17] -->


<!-- b000367 | furniture | pages [17] -->
Page 16 of 23

<!-- b000368 | furniture | pages [17] -->


<!-- b000369 | prose | pages [17] -->
location on a bat that would be produced for a wide range of initial ball velocities and angular bat speeds.  We then created a second plot which used the same model but added two constraints:

<!-- b000370 | prose | pages [17] -->
 The ball speed must be between 67 and 97 MPH, covering the vast majority of pitch velocities.

<!-- b000371 | prose | pages [17] -->
 The value for b must be between 21 and 24 inches, which is the generally accepted location of the range of sweet spots.

<!-- b000372 | prose | pages [17] -->
The graph is shown below:

<!-- b000373 | prose | pages [17] -->
Graph B

<!-- b000374 | furniture | pages [17] -->


<!-- b000375 | prose | pages [17] -->
Graph B shows where on the wooden bat the optimal location for final ball velocity is located based on the initial velocities of ball and bat.  However, since it is unrealistic to believe that the ball should optimally be hit just above the hands or on the tapered part of the bat, we set up the 4-7 inch constraint.  The constraint on initial ball speed was set by considering the fact that only a select group of pitchers throw any faster than 97 MPH, and pitchers typically don’t throw any less than 67 MPH.  The darker area of Graph B represents the portion of combinations that would make the model applicable in reality.

<!-- b000376 | prose | pages [17] -->
In order to test the sensitivity of our model to changes in its variables we first substituted Equation 2 into Equation 3 for the variable b and found:

<!-- b000377 | furniture | pages [17] -->


<!-- b000378 | furniture | pages [18] -->
Control #7920

<!-- b000379 | furniture | pages [18] -->


<!-- b000380 | furniture | pages [18] -->


<!-- b000381 | furniture | pages [18] -->


<!-- b000382 | furniture | pages [18] -->
Page 17 of 23

<!-- b000383 | furniture | pages [18] -->


<!-- b000384 | prose | pages [18] -->
Using this equation, we were able to define all of the variables that were used with the assumptions from our normal wooden bat model.  We then replaced each of the values one at a time with a variable to see how the final velocity changed as that variable changed.

<!-- b000385 | prose | pages [18] -->
 Mass of Bat When the final velocity was tested against the mass of the bat, the following graph was produced:

<!-- b000386 | prose | pages [18] -->
Final Speed vs. Bat Mass

<!-- b000387 | prose | pages [18] -->
v f m s

<!-- b000388 | prose | pages [18] -->
53.54

<!-- b000389 | prose | pages [18] -->
53.52

<!-- b000390 | prose | pages [18] -->
53.50

<!-- b000391 | prose | pages [18] -->
53.48

<!-- b000392 | prose | pages [18] -->
0.88 0.90

<!-- b000393 | prose | pages [18] -->
Graph C

<!-- b000394 | prose | pages [18] -->
M kg

<!-- b000395 | furniture | pages [18] -->


<!-- b000396 | prose | pages [18] -->
0.92 0.92

<!-- b000397 | prose | pages [18] -->
As the mass of the bat increases, so does the final speed of the ball. This is fairly easy to explain in terms of inertia. If a bat with a larger mass is swung with the same velocity, it will produce a greater final ball velocity upon contact. This graph may be misleading, however, in that the final speed is not very sensitive to the mass of the bat.  This is only the case when the mass changes independent of the other variables, which is rarely the case.

<!-- b000398 | prose | pages [18] -->
 Initial Velocity of Bat When the final velocity was tested against the initial velocity of the bat, the following graph was produced:

<!-- b000399 | furniture | pages [18] -->


<!-- b000400 | prose | pages [18] -->
Final Speed vs. Initial Bat Velocity

<!-- b000401 | prose | pages [18] -->
v f m s

<!-- b000402 | prose | pages [18] -->
57

<!-- b000403 | prose | pages [18] -->
56

<!-- b000404 | prose | pages [18] -->
55

<!-- b000405 | prose | pages [18] -->
54

<!-- b000406 | prose | pages [18] -->
53

<!-- b000407 | furniture | pages [18] -->


<!-- b000408 | prose | pages [18] -->
30 35 40

<!-- b000409 | prose | pages [18] -->
Graph D

<!-- b000410 | prose | pages [18] -->
Vi m s

<!-- b000411 | furniture | pages [18] -->


<!-- b000412 | prose | pages [18] -->
45

<!-- b000413 | furniture | pages [19] -->
Control #7920

<!-- b000414 | furniture | pages [19] -->


<!-- b000415 | furniture | pages [19] -->


<!-- b000416 | furniture | pages [19] -->


<!-- b000417 | furniture | pages [19] -->
Page 18 of 23

<!-- b000418 | furniture | pages [19] -->


<!-- b000419 | prose | pages [19] -->
As the initial bat velocity is increased, the final ball speed increases as well, as long as all other variables remain constant.  This graph indicates a high sensitivity of the model to the initial velocity of the bat.  This is most easily explained by conservation of momentum—since the bat is many times more massive than the ball, a change within the range of expected bat speed values would have a strong impact on the final velocity of the less massive ball.  The bat speed usually is not increased in isolation from the weight of the bat or manipulating the moment of inertia, so the ball speed may be even more sensitive to a changing bat speed.

<!-- b000420 | furniture | pages [19] -->


<!-- b000421 | prose | pages [19] -->
 Moment of Inertia When the final velocity was tested against the moment of inertia of the bat, the following graph was produced:

<!-- b000422 | furniture | pages [19] -->


<!-- b000423 | prose | pages [19] -->
Final Speed vs. Moment of Inertia

<!-- b000424 | prose | pages [19] -->
v f m s

<!-- b000425 | prose | pages [19] -->
53.7

<!-- b000426 | prose | pages [19] -->
53.6

<!-- b000427 | prose | pages [19] -->
53.5

<!-- b000428 | prose | pages [19] -->
53.4

<!-- b000429 | prose | pages [19] -->
53.3

<!-- b000430 | prose | pages [19] -->
0.18 0.20

<!-- b000431 | prose | pages [19] -->
Graph E

<!-- b000432 | prose | pages [19] -->
I kg m2

<!-- b000433 | furniture | pages [19] -->


<!-- b000434 | prose | pages [19] -->
0.22

<!-- b000435 | prose | pages [19] -->
This plot indicates a weak sensitivity of the model to changes in the moment of inertia, however, it is not as simple a determination as this plot assumes. Changing the moment of inertia shifts the distribution of the weight closer to the hitter’s hands. As this happens the hitter would then be able to swing the bat at a higher velocity, which we determined to have a strong positive effect on final velocity.  Since the relation of bat speed to final ball speed is stronger than that of moment of inertia, the slight increase in speed caused by increasing the moment of inertia would be masked by the resulting decrease in swing speed.  By only isolating one variable at a time, we are unable to discover which variable is more important towards increasing final ball speed.

<!-- b000436 | furniture | pages [19] -->


<!-- b000437 | prose | pages [19] -->
 Initial Velocity of Ball When the final velocity was tested against the initial velocity of the ball, the following graph was produced:

<!-- b000438 | furniture | pages [20] -->
Control #7920

<!-- b000439 | furniture | pages [20] -->


<!-- b000440 | furniture | pages [20] -->


<!-- b000441 | furniture | pages [20] -->


<!-- b000442 | furniture | pages [20] -->
Page 19 of 23

<!-- b000443 | furniture | pages [20] -->


<!-- b000444 | prose | pages [20] -->
Final Speed vs. Initial Ball Velocity

<!-- b000445 | prose | pages [20] -->
v f m s

<!-- b000446 | prose | pages [20] -->
52

<!-- b000447 | prose | pages [20] -->
50

<!-- b000448 | prose | pages [20] -->
48

<!-- b000449 | prose | pages [20] -->
46

<!-- b000450 | prose | pages [20] -->
44

<!-- b000451 | prose | pages [20] -->
32 34 36 38

<!-- b000452 | prose | pages [20] -->
Graph F

<!-- b000453 | prose | pages [20] -->
vi m s

<!-- b000454 | furniture | pages [20] -->


<!-- b000455 | prose | pages [20] -->
40 42

<!-- b000456 | prose | pages [20] -->
It appears that the final velocity of the ball is highly sensitive to its initial velocity.  The concept represented here is fairly intuitive: as velocity of the pitch increases, the speed of the batted ball increases as well.

<!-- b000457 | heading | pages [20] -->
9. Conclusion

<!-- b000458 | furniture | pages [20] -->


<!-- b000459 | prose | pages [20] -->
Before producing our model, we laid out a set of four primary objectives which we intended to use to guide and bracket our investigation, presented in section two:

<!-- b000460 | prose | pages [20] -->
 Answering the Problem

<!-- b000461 | prose | pages [20] -->
 Simplicity and Clarity

<!-- b000462 | prose | pages [20] -->
 Applicability

<!-- b000463 | prose | pages [20] -->
 Resiliency

<!-- b000464 | prose | pages [20] -->
With the completion of our sensitivity analysis a number of conclusions can now be drawn about the model as a whole, in light of these original objectives. While the COP has traditionally been identified as a marker of the sweet spot of a baseball bat, it proved inadequate for the purposes of this problem. Example I shows that the COP is capable of predicting the sweet spot in terms of “feel,” but is unable to document the sweet spot in terms of maximum performance.  Instead, we were forced to draw on the Brody Power Model in order to optimize this variable.  The Brody model is capable of making this optimization on account of its construction from conservation principles and the coefficient of restitution.  Despite their differences, both the COP and the Brody model do provide an explanation for the empirical observation that the sweet spot is located on the middle portion of the bat barrel and not the extreme end as torque would predict.

<!-- b000465 | furniture | pages [21] -->
Control #7920

<!-- b000466 | furniture | pages [21] -->


<!-- b000467 | furniture | pages [21] -->
Page 20 of 23

<!-- b000468 | furniture | pages [21] -->


<!-- b000469 | furniture | pages [21] -->


<!-- b000470 | prose | pages [21] -->
We then augmented our assumptions in the Brody model in order to test for the effects of corked and aluminum bats.  Example II demonstrates that the Brody model is capable of estimating the location of the sweet spot.  For our baseline wooden bat, this was 5.733 inches from the free end of the barrel. When the assumptions are varied to predict the outcome of using a corked bat, a .31 m/s increase in ball exit speed is yielded. This constitutes a negligible enhancement of the sweet spot effect, and is subject to factors that might further mitigate this increase. It appears that increased performance, at least in terms of ball exit velocity, does not merit the prohibition of corked bats instituted by Major League Baseball. Our discussion identified other possible explanations for this prohibition.

<!-- b000471 | prose | pages [21] -->
Finally, we varied our assumptions to model the effects of an aluminum bat in comparison to the original wooden bat. This model predicts a .76 m/s increase in ball exit speed, over two times the corked bat increase.  While this improvement in speed of 145% can be viewed as more significant, it is not as significant as empirical tests have shown.  It is evident then that there are other factors which come into play for aluminum bats which the model does not take into account, for instance, the trampoline effect.  Our results do support the conclusion that different materials used in construction matter, and offers support to Major League Baseball’s metal bat prohibition for reasons of both safety and tradition.

<!-- b000472 | prose | pages [21] -->
We feel our model adequately achieves our goals of simplicity and clarity.  Referencing the guiding intent presented in section 2, our model and explanations would be understandable to a baseball audience while still providing sufficient technical detail to present solid justification for our conclusions.

<!-- b000473 | furniture | pages [21] -->


<!-- b000474 | prose | pages [21] -->
In terms of applicability and resiliency, our sensitivity analysis has given us some valuable feedback about our assumptions and our model as a whole. When isolating each variable, we found that the model was relatively insensitive to changes to the mass or moment of inertia.  However, there was a much stronger sensitivity of the final velocity of the ball to the speed of the bat. Since changes to the mass affect moment of inertia, and both in turn affect the speed at which the bat can be swung, small changes in a structural parameter could be amplified in angular velocity.  Because changes in each variable were evaluated separately, however, we are unable to tell which variables carry a stronger correlation with changes in batted ball performance.  Although the variables cannot be isolated, the model is able to take a given set of circumstances and predict the relative performances of two bats.

<!-- b000475 | heading | pages [21] -->
Positive aspects of our model include:

<!-- b000476 | prose | pages [21] -->
 Mass, weight distribution, and relative momentums are taken into account.

<!-- b000477 | prose | pages [21] -->
 The comparative results seem to reflect fairly accurate representations of whether bats are improved or harmed by changes to their specifications.

<!-- b000478 | furniture | pages [21] -->


<!-- b000479 | furniture | pages [22] -->
Control #7920

<!-- b000480 | furniture | pages [22] -->


<!-- b000481 | furniture | pages [22] -->
Page 21 of 23

<!-- b000482 | furniture | pages [22] -->


<!-- b000483 | furniture | pages [22] -->


<!-- b000484 | heading | pages [22] -->
Limitations to our model include:

<!-- b000485 | prose | pages [22] -->
 Because many of the parameters are estimated, our model contains a significant possibility for error.

<!-- b000486 | prose | pages [22] -->
 It does not take vibration, angles, or lateral movement into account.

<!-- b000487 | heading | pages [22] -->
Additional research could improve the functionality of our model:

<!-- b000488 | prose | pages [22] -->
 Currently the model only measures relative changes in ball performance between bats, and it cannot produce an accurate measure of what the final ball velocity will be in reality.  A more complete model which takes into account final velocity of the bat would be difficult to design but more useful.

<!-- b000489 | prose | pages [22] -->
 The model could be expanded to take into account other factors which have been identified as interfering with the amount of energy which a ball departs with, for instance the harmonic vibrations experienced upon impact.

<!-- b000490 | prose | pages [22] -->
 Laboratory research which produced empirical data for use specifically as our parameters would provide us with more accurate inputs, instead of relying on our assumptions.

<!-- b000491 | prose | pages [22] -->
 Laboratory research would help to confirm the results of our model’s predictions to provide feedback in improving the model.

<!-- b000492 | furniture | pages [22] -->


<!-- b000493 | furniture | pages [22] -->


<!-- b000494 | furniture | pages [22] -->


<!-- b000495 | furniture | pages [22] -->


<!-- b000496 | furniture | pages [22] -->


<!-- b000497 | furniture | pages [22] -->


<!-- b000498 | furniture | pages [22] -->


<!-- b000499 | furniture | pages [22] -->


<!-- b000500 | furniture | pages [22] -->


<!-- b000501 | furniture | pages [23] -->
Control #7920

<!-- b000502 | furniture | pages [23] -->


<!-- b000503 | furniture | pages [23] -->
Page 22 of 23

<!-- b000504 | furniture | pages [23] -->


<!-- b000505 | furniture | pages [23] -->


<!-- b000506 | heading | pages [23] -->
10. References

<!-- b000507 | furniture | pages [23] -->


<!-- b000508 | heading | pages [23] -->
References

<!-- b000509 | references | pages [23] -->
[1] AP. "Unsplendid Splinter." Sports Illustrated. Time Warner Inc., 4 June 2003. Web.

<!-- b000510 | furniture | pages [23] -->


<!-- b000511 | references | pages [23] -->
19 Feb.2010.

<!-- b000512 | references | pages [23] -->
[2] Brody, H. “The Sweet Spot of a Baseball Bat”. American Journal of Physics. Volume 54,

<!-- b000513 | references | pages [23] -->
Issue 7: pp. 640-643. Issue Date: July 1986

<!-- b000514 | references | pages [23] -->
[3] Russel, Daniel A. "What is the COP and Does it Matter?" Physics and Acoustics of Baseball

<!-- b000515 | references | pages [23] -->
and Softball Bats. Kettering University, 16 June 2005. Web. 19 Feb. 2010.

<!-- b000516 | references | pages [23] -->
<http://paws.kettering.edu/~drussell/bats-new/cop.html>.

<!-- b000517 | references | pages [23] -->
[4] Russel, Daniel A. "What(and where) is the Sweet Spot of a Baseball/Softball Bat?" Physics

<!-- b000518 | references | pages [23] -->
and Acoustics of Baseball and Softball Bats. Kettering University, 2004. Web. 19 Feb. 2010.

<!-- b000519 | references | pages [23] -->
<http://paws.kettering.edu/~drussell/bats-new/sweetspot.html>.

<!-- b000520 | references | pages [23] -->
[5] Cross, Rod. "The Sweet Spot of a Baseball Bat." American Journal of Physics. Volume  66,

<!-- b000521 | references | pages [23] -->
Issue 9 (1998): 772-79. University of Sydney, 2006. Web. 19 Feb. 2010.

<!-- b000522 | references | pages [23] -->
<http://www.physics.usyd.edu.au/~cross/PUBLICATIONS/3.%20BatSweetSpot.pdf>.

<!-- b000523 | references | pages [23] -->
[6] Cross, Rod. "Center of Percussion of Handheld Instruments." American Journal of Physics

<!-- b000524 | references | pages [23] -->
72.5 (2004): 622-30. University of Sydney, 2004. Web. 19 Feb. 2010.

<!-- b000525 | references | pages [23] -->
<http://www.physics.usyd.edu.au/~cross/PUBLICATIONS/26.%20COPHandHeld.PDF>.

<!-- b000526 | references | pages [23] -->
[7] Stronge, William J., Mont Hubbard, and Gregory S. Sawicki. "How to Hit Home Runs:

<!-- b000527 | references | pages [23] -->
Optimum Baseball Bat Swing Parameters." American Journal of Physics . Volume 71, Issue 11

<!-- b000528 | references | pages [23] -->
(2003): 1152-162. 2004. Web. 19 Feb. 2010. <http://webusers.npl.illinois.edu/~a-

<!-- b000529 | references | pages [23] -->
nathan/pob/AJP-Nov03.pdf>.

<!-- b000530 | references | pages [23] -->
[8] "BESR Certification." JustBats.com. 2000-2010. Web. 19 Feb. 2010.

<!-- b000531 | references | pages [23] -->
<http://www.justbats.com/bat.care.aspx?c=5>.

<!-- b000532 | references | pages [23] -->
[9] Russel, Dan. "Swing Weights of Baseball and Softball Bats." Kettering University, 2009.

<!-- b000533 | references | pages [23] -->
Web. 19 Feb. 2010. <http://paws.kettering.edu/~drussell/Publications/TPT-SwingWeight.pdf>.

<!-- b000534 | references | pages [23] -->
[10] "Baseball Bat History - A Full Overview of the History of Baseball Bats." Baseball Bats -

<!-- b000535 | references | pages [23] -->
the ultimate baseball & softball bat resource! Baseball-Bats.net, 2008. Web. 20 Feb. 2010.

<!-- b000536 | references | pages [23] -->
<http://www.baseball-bats.net/baseball-bats/baseball-bat-history/index.html>.

<!-- b000537 | references | pages [23] -->
[11] Flading, John. "History of Baseball." Web log post. SwingAway Instrunctional Blod.

<!-- b000538 | references | pages [23] -->
SwingAway Sports Products, 10 June 2009. Web. 20 Feb. 2010.

<!-- b000539 | references | pages [23] -->
<http://www.swingawayblog.com/2009/06/10/history-of-baseball/>.

<!-- b000540 | references | pages [23] -->
[12] Muskat, Carrie. "Sosa Gets Eight Games, Appeals." MLB.com. Major League Baseball, 6

<!-- b000541 | references | pages [23] -->
June 2003. Web. 20 Feb. 2010.

<!-- b000542 | references | pages [23] -->
<http://mlb.mlb.com/news/article.jsp?ymd=20030606&content_id=358688&vkey=news_mlb&f

<!-- b000543 | references | pages [23] -->
ext=.jsp&c_id=null>.

<!-- b000544 | furniture | pages [24] -->
Control #7920

<!-- b000545 | furniture | pages [24] -->


<!-- b000546 | furniture | pages [24] -->
Page 23 of 23

<!-- b000547 | furniture | pages [24] -->


<!-- b000548 | furniture | pages [24] -->


<!-- b000549 | references | pages [24] -->
[13] Russel, Daniel A. "What about corked bats?" Physics and Acoustics of Baseball and Softball

<!-- b000550 | references | pages [24] -->
Bats. Kettering University, 7 October 2004. Web. 20 Feb. 2010.

<!-- b000551 | references | pages [24] -->
<http://paws.kettering.edu/~drussell/bats-new/cop.html>.

<!-- b000552 | references | pages [24] -->
[14] Russel, Daniel A. " Vibrational Modes of a Baseball Bat

<!-- b000553 | references | pages [24] -->
" Physics and Acoustics of Baseball and Softball Bats. Kettering University, 2003. Web. 20 Feb.

<!-- b000554 | references | pages [24] -->
2010. <http://paws.kettering.edu/~drussell/bats-new/cop.html>.

<!-- b000555 | references | pages [24] -->
[15] Nathan, Alan. "Baseball: It's Not Nuclear Physics (or is it?!)." Physics of Baseball.

<!-- b000556 | references | pages [24] -->
University of Illinois, 5 Feb. 1999. Web. 20 Feb. 2010. <http://74.125.95.132/search?q=cache:a-

<!-- b000557 | references | pages [24] -->
RntmFp-iYJ:webusers.npl.illinois.edu/~a-

<!-- b000558 | references | pages [24] -->
nathan/pob/ppt/parkland.ppt+Alan+Nathan+Powerpoint+(parkland.ppt)&cd=1&hl=en&ct=clnk

<!-- b000559 | references | pages [24] -->
&gl=us>.

<!-- b000560 | references | pages [24] -->
[16] Nathan, Alan M., Daniel A. Russell, and Lloyd V. Smith. "The Physics of the Trampoline

<!-- b000561 | references | pages [24] -->
Effect in Baseball and Softball Bats." The Physics of Baseball. University of Illionois. Web. 20

<!-- b000562 | references | pages [24] -->
Feb. 2010. <http://webusers.npl.illinois.edu/~a-nathan/pob/trampoline-v6.pdf>.

<!-- b000563 | references | pages [24] -->
[17] Bahill, Terry. "Systems Engineering." University of Arizona, 2009. Web. 20 Feb. 2010.

<!-- b000564 | references | pages [24] -->
<http://www.sie.arizona.edu/sysengr/slides/baseballBat.ppt>.

<!-- b000565 | references | pages [24] -->
[18] "Official Rules | MLB.com: Official info." The Official Site of Major League Baseball |

<!-- b000566 | references | pages [24] -->
MLB.com: Homepage. Major League Baseball, 2009. Web. 22 Feb. 2010.

<!-- b000567 | references | pages [24] -->
<http://mlb.mlb.com/mlb/official_info/official_rules/objectives_1.jsp>.

<!-- b000568 | references | pages [24] -->
[19] Nathan, Alan M., Daniel A. Russell, and Lloyd V. Smith. " Some Remarks on Corked

<!-- b000569 | references | pages [24] -->
Bats." The Physics of Baseball. University of Illionois. Web. 20 Feb. 2010.

<!-- b000570 | references | pages [24] -->
[20] Russel, Daniel A. "Why Aluminum Bats Can Perform Better than Wood Bats?" Physics and

<!-- b000571 | references | pages [24] -->
Acoustics of Baseball and Softball Bats. Kettering University, 18 October 2006. Web. 19 Feb.

<!-- b000572 | references | pages [24] -->
2010. <http://paws.kettering.edu/~drussell/bats-new/alumwood.html>.

<!-- b000573 | furniture | pages [24] -->


<!-- b000574 | furniture | pages [24] -->

