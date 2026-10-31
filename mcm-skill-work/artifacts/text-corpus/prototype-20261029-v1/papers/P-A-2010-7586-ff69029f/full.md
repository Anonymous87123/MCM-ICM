# P-A-2010-7586-ff69029f

Status: machine-draft; not source-verified.


<!-- b000001 | furniture | pages [1] -->
Team #7586

<!-- b000002 | furniture | pages [1] -->
Page 1 of 15

<!-- b000003 | heading | pages [1] -->
The Sweet Spot: A Wave Model of Baseball Bats

<!-- b000004 | furniture | pages [1] -->
Team #7586

<!-- b000005 | prose | pages [1] -->
February 22, 2010

<!-- b000006 | heading | pages [1] -->
ABSTRACT

<!-- b000007 | prose | pages [1] -->
In this paper, we determine the sweet spot on a baseball bat. We capture the essential physics of the ball-bat impact by taking the ball to be a lossy spring and the bat to be an Euler-Bernoulli beam. In order to impart some intuition about the model we begin by presenting a rigid body model. Next, we proceed to use our full model to reconcile various correct and incorrect claims about the sweet spot found in the literature. Finally, we discuss the sweet spot and performance of corked and aluminum bats, with a particular emphasis on hoop modes.

<!-- b000008 | heading | pages [1] -->
1. INTRODUCTION

<!-- b000009 | prose | pages [1] -->
The status of baseball as the nation’s pastime makes understanding the collision of an irregularly shaped slab of wood with a ball a compelling and interesting problem. The physics of baseball encompasses much more than just the batting of the ball. The pitching of the ball and the ﬂight of the ball are examples of equally important events susceptible to physics modeling. Even limiting one’s scope to the batting of the ball yields a problem of many dimensions. A hitter might expect a model of the baseball-bat collision to yield insight into how the bat breaks, how the bat imparts spin on the ball, how best to swing the bat, and so on.1 We model only the sweet spot.

<!-- b000010 | prose | pages [1] -->
We have encountered at least two notions of what the sweet spot should be deﬁned as. The ﬁrst comes from what we suspect explains the term sweet spot. This deﬁnition equates the sweet spot with the impact location on the bat which minimizes the discomfort to the hands.

<!-- b000011 | prose | pages [1] -->
We can tentatively give the second deﬁnition as the impact location which maximizes the outgoing velocity of the ball. Some players seem to implicitly identify these two deﬁnitions as the same. We do not identify the two and focus exclusively on the second deﬁnition, which we now deﬁne more carefully.

<!-- b000012 | prose | pages [1] -->
Given a baseball bat and baseball, the ﬁnal velocity of the ball is determined by the initial velocity and rotation of the ball, initial velocity and rotation of the bat, the relative position and orientation of the bat and ball, and the force over time that the hitter’s hands may apply on the handle. We assume that the ball is not rotating and that the ball’s velocity at impact is perpendicular to the length of the bat. We assume that everything occurs in a single plane and we will argue that the hand’s interaction are actually negligible. In the frame of reference of the center of mass of the bat, the initial conditions are completely speciﬁed by the angular velocity of the bat, the velocity of the ball, and the position of impact along the bat.

<!-- b000013 | prose | pages [1] -->
Fixing the properties of the bat, ball, initial velocity of the ball, and angular velocity, we can now deﬁne the sweet spot as the location of the point of impact which maximizes the ﬁnal ball velocity. In particular, the location of the sweet depends not just the bat alone, but also the pitch and swing. In order to determine the actual location of the sweet spot, we model the physical eﬀects that we ﬁnd to be most important and allow that model to make a prediction. Here we rapidly explain the features of a few models in the literature.

<!-- b000014 | prose | pages [1] -->
The simplest model predicts the sweet spot to be at the center of percussion.2 This model assumes that an impact location that minimizes discomfort to the hand also maximizes power transferred to the ball. The model assumes the ball to be a rigid body for which there are conjugate points at which an impact at one will exactly balance the angular recoil and linear recoil at the other. By gripping at one conjugate point and impacting at the other point, the center of percussion, the theory predicted that the hands would experience minimal shock and therefore the ball would exit with high velocity.

<!-- b000015 | prose | pages [1] -->
This point depends heavily on the moment of inertia and the location of the hands. We cannot accept this model because it both erroneously equates the two deﬁnitions of sweet spot and furthermore assumes incorrectly that the bat is a rigid body.

<!-- b000016 | furniture | pages [1] -->
1

<!-- b000017 | furniture | pages [2] -->
Team #7586

<!-- b000018 | furniture | pages [2] -->
Page 2 of 15

<!-- b000019 | prose | pages [2] -->
Another model predicts the sweet spot to be between nodes of the two lowest natural frequencies of the bat.3 Given a free bat allowed to oscillate, it’s oscillations can be decomposed into fundamental modes of various frequencies. The intuition is much like that of xylophones or other musical instruments. Diﬀerent geometries and materials have diﬀerent natural frequencies at which they will oscillate. The resulting wave shapes suggest how one would go about exciting those modes. Plucking a string at the node of a vibrational mode will not excite that mode. It is ambiguous which deﬁnition of sweet spot this model uses. Using the ﬁrst deﬁnition, it is focusing on the uncomfortable excitations of vibrational models. Hopefully by choosing the impact location to be near nodes of important frequencies, there will be a minimum of uncomfortable vibrations set up. Using the second deﬁnition, the worry is that energy sent into vibrations of the bat will be lost. This model assumes then that the most important energies to model are those lost to vibration.

<!-- b000020 | prose | pages [2] -->
This model raises many questions. Which frequencies actually do get excited and why? The Fourier transform of an impulse will in general contain inﬁnitely many modes. Furthermore, wood is a viscoelastic material which quickly dissipates its energies. Is the notion of an oscillating bat even relevant to modeling such a bat? How valid is the condition that the bat is free? Ought the system be coupled with hands on the handle, or the arm’s bone structure, or possibly even the ball? What types of oscillations are relevant? A cylindrical structure can support numerous diﬀerent types of modes beyond the transverse modes usually assumed by this model.4

<!-- b000021 | prose | pages [2] -->
We discuss these models not only to point out the confusion (advantageous to marketers of fancy bats) surrounding the sweet spot but also to highlight two basic issues in modeling the sweet spot. Following the center of percussion line of reasoning, how do we model the recoil of the bat? Following the vibrational nodes line or reasoning, how do we model the vibrations of the bat? In the general theory of impact mechanics,5

<!-- b000022 | prose | pages [2] -->
these two eﬀects are the main ones assuming that the bat does not break or deform permanently. We will explain in this paper notable approaches found in the literature by Brody,2 Cross,6 and Nathan.3 Very brieﬂy, Brody ignores vibrations, Cross ignores bat rotation but studies the propagation of the impulse coupled with the ball, and Nathan attempts to emphasize the vibrational modes. Our approach reconciles the tension between these diﬀerent approaches while emphasizing the crucial role played by the time-scale of the collision.

<!-- b000023 | prose | pages [2] -->
Our main goal is to understand the sweet spot. A secondary goal is to understand the diﬀerences between the sweet spots of diﬀerent bat types. Although marketers of diﬀerent types of bats often emphasize the importance of the sweet spots, there are often other relevant factors involved: ease of swing, tendency of the bat to break, psychological eﬀects, and so on. We once again emphasize that the problem that we investigate is a restricted problem for which we arbitrarily set constant other important factors. For example, we will argue that it doesn’t matter to the collision whether or not the batter’s hands are gripping the handle ﬁrmly or if the batter follows through correctly. This does not have any bearing on the technique required to actually swing the bat or how the bat’s properties aﬀect this.

<!-- b000024 | prose | pages [2] -->
Our paper is organized as follows. First, we present the Brody rigid body model illuminating the recoil eﬀects of impact. Next we present a full computational model based on wave propagation in a Euler-Bernoulli beam coupled with the ball modeled as a lossy spring. We compare this model with other models found in the literature and explore the local nature of impact, the interaction of recoil and vibrations, and robustness to parameter changes. We adjust the parameters of the model to comment on the sweet spots of corked bats and aluminum bats. Finally, we investigate the eﬀect of hoop frequencies on aluminum bats.

<!-- b000025 | heading | pages [2] -->
2. A SIMPLE EXAMPLE

<!-- b000026 | prose | pages [2] -->
We begin by only considering the rigid recoil eﬀects of the bat-ball collision, much in the same way as Brody.2

<!-- b000027 | prose | pages [2] -->
Consider a bat swung at an incoming baseball. For simplicity of this example, we assume that the bat is perfectly rigid. Because the collision happens on such a short time scale (around 1 ms), we will treat the bat as a free body. That is to say, we are not concerned with the batter’s hands exerting some force on the bat which may be transferred into the ball.

<!-- b000028 | furniture | pages [2] -->
2

<!-- b000029 | furniture | pages [3] -->
Team #7586

<!-- b000030 | furniture | pages [3] -->
Page 3 of 15

<!-- b000031 | caption | pages [3] -->
Figure 1: Arrows point in the positive direction for the corresponding parameter.

<!-- b000032 | prose | pages [3] -->
The bat has mass M and moment of inertia I about its center of mass. From the reference frame of the center of mass of the baseball bat before the collision, the ball has velocity vi in the positive x-direction while the bat has an angular velocity of ωi. Note that in our setup, vi and ωi will have opposite signs when the batter is swinging at the ball as in Figure 1. The ball collides with the bat at a distance l from the center of mass of the bat. We assume that the collision is head-on and view the event such that all the y-component velocities are zero at the moment of the collision. After the collision, the ball will have a ﬁnal velocity vf and the bat will have a ﬁnal linear velocity of Vf and an angular velocity of ωf at the center of mass.

<!-- b000033 | prose | pages [3] -->
When the ball collides with the bat, it brieﬂy compresses and decompresses, converting kinetic energy to potential energy and back. However, some energy is lost in the process, i.e. the collision is inelastic. The ratio of the relative speeds of the bat and the ball before and after the collision is known as the coeﬃcient of restitution, designated by e. In other words e = 0 represents a perfectly inelastic collision, and e = 1 means the collision is perfectly elastic. In this basic model, we make two simplifying assumptions: e is constant along the length of the bat, and e is constant for all vi.

<!-- b000034 | prose | pages [3] -->
Given our pre-collision conditions, we can write conservation of linear momentum:

<!-- b000035 | prose | pages [3] -->
MVf = m(vi −vf)

<!-- b000036 | prose | pages [3] -->
Conservation of angular momentum:

<!-- b000037 | prose | pages [3] -->
I(ωf −ωi) = ml(vi −vf)

<!-- b000038 | furniture | pages [3] -->
3

<!-- b000039 | furniture | pages [4] -->
Team #7586

<!-- b000040 | prose | pages [4] -->
Deﬁntion of the coeﬃcient of restitution:

<!-- b000041 | furniture | pages [4] -->
Page 4 of 15

<!-- b000042 | prose | pages [4] -->
e(vi −ωil) = −vf + Vf + wfl

<!-- b000043 | prose | pages [4] -->
Solving for vf gives

<!-- b000044 | prose | pages [4] -->
vf = −vi(e −

<!-- b000045 | prose | pages [4] -->
M Where M ∗= is the eﬀective mass of the bat. 1+ Ml2 I

<!-- b000046 | prose | pages [4] -->
m m M ∗) + ωil(1 + e)

<!-- b000047 | prose | pages [4] -->
m 1 + M ∗

<!-- b000048 | prose | pages [4] -->
For calibration purposes, we use the following numbers which are typical of a regulation bat connecting with a fastball in Major League Baseball. The results are plotted below.

<!-- b000049 | prose | pages [4] -->
m 0.145 kg M 0.83 kg L 0.84 m 5.1 oz 29 oz 33 in 0.039 kg · m2 I

<!-- b000050 | prose | pages [4] -->
vi 67 m/s ωi -60 rad/s e 0.55 150 mph

<!-- b000051 | caption | pages [4] -->
Figure 2: vf as a function of l.

<!-- b000052 | prose | pages [4] -->
The maximum exit velocity in our example is around 26.7 m/s, and the sweet spot is 13 cm from the center of mass. Missing the sweet spot by up to 5 cm will only result in a 1 m/s diﬀerence from the maximum speed, implying a relatively wide sweet spot.

<!-- b000053 | prose | pages [4] -->
From this example, we can already see that the sweet spot is determined by a multitude of factors, including the length, mass, and shape of the baseball bat, the mass of the baseball, and the coeﬃcient of restitution between the bat and ball. Furthermore, the sweet spot is even not uniquely determined by the bat and baseball. It also depends on the incoming baseball speed and the batter’s swing speed. All these factors need to be taken into account to maximize the baseball’s exit speed.

<!-- b000054 | prose | pages [4] -->
The ﬁgure also shows intuitively why the sweet spot is located somewhere between the center of mass and the end of the barrel. As the point of collision moves outwards along the bat, the eﬀective mass of the bat goes up, so that greater fraction of the initial kinetic energy is put into the bat’s rotation, which. At the same time, the rotation in the bat means that the barrel of the bat is moving faster than center of mass

<!-- b000055 | furniture | pages [4] -->
4

<!-- b000056 | furniture | pages [4] -->
4

<!-- b000057 | furniture | pages [5] -->
Team #7586

<!-- b000058 | furniture | pages [5] -->
Page 5 of 15

<!-- b000059 | prose | pages [5] -->
(or handle). These two eﬀects work in opposite directions to give a unique sweet spot that’s not at either endpoint.

<!-- b000060 | prose | pages [5] -->
However, this model tells only part of the story. Indeed some of our starting assumptions contradict each other. We treated the bat as a free body because the collision time was so short. In essence, during the 1 ms of the collision, the ball will only “see” the local geometry of the bat. The ball will not “see” the batter’s hands on the handle of the bat. On the other hand, we assumed the bat was perfectly rigid. However, this means that the ball “sees” the entire bat. These assumptions clearly cannot both be true. We also assumed that the e was constant along the length of the bat and for diﬀerent collision velocities. Experimental evidence1 suggests that neither issue can be ignored for an accurate prediction of the location of the sweet spot. We will need a more sophisticated model to address all these shortcomings in our simple example and better understand what’s going on.

<!-- b000061 | heading | pages [5] -->
3. OUR MODEL

<!-- b000062 | prose | pages [5] -->
We have attempted to combine the best features of previous models into our model. We draw from Brody’s rigid body model as described in the previous section for intuition, but we draw our mathematics most directly from Cross’s work.6 One could accurately describe our work as an adaptation of Cross’s work to actual baseball bats. Nathan also attempted such an adaptation but he was misled by incorrect intuition about the role of vibrations. We describe Nathan’s approach and error as a way to explain Cross’s work and to motivate our work. Next, we present the equations of our model and discuss the main features of its assumptions and methodology.

<!-- b000063 | heading | pages [5] -->
3.1 Previous Models

<!-- b000064 | prose | pages [5] -->
In the previous section we encountered Brody’s rigid body model which successfully predicts the existence of a sweet spot not at the end of the bat. That model suﬀers from the fact that the bat is not a rigid body and experiences vibrations. One way to account for those vibrations is to model the bat as a ﬂexible object. Beam theories of varying degrees of accuracy and complication can be used to model the ﬂexible bat. Van Zandt was the ﬁrst to carry out such an analysis modeling the beam as a Timoshenko beam. A Timoshenko beam is a fourth order theory taking into account both shear forces and tensile stresses. The equations are complicated and we will not need them so we will not record them here. His model assumes the ball to be uncoupled from the beam and simply takes the impulse of the ball as a given. The resulting vibrations of the bat are used to more accurately predict the velocity of the beam at the impact point (by summing the Brody velocity with the velocity of the displacement at the impact point due to vibrations) and therefore predict a more accurate exit velocity of the ball still from the equations of the coeﬃcient of restitution.7

<!-- b000065 | prose | pages [5] -->
The next model we draw on is Cross’s model6 of the interaction of the impact of balls with aluminum beams. His beam used the less elaborate Euler-Bernoulli equations to model the propagation of waves. In addition, he provided equations to model the dynamic coupling of the ball to the beam during the impact. After discretizing the beam spatially, he assumed the ball basically acts as a lossy spring coupled to the single component of the region of impact. Cross’s work is motivated by both the case of tennis rackets and baseball bats. One important diﬀerence in those cases is the time-scale of impact. The baseball bat’s collision only lasts approximately one millisecond in which time the propagation speed of the wave is very important. In this local view of the impact, the importance of the baseball’s coupling with the bat is increased. We will describe both the equations of the Euler-Bernoulli equations and ball’s equations in a later section.

<!-- b000066 | prose | pages [5] -->
Before continuing let us discuss the main results of the Cross model.

<!-- b000067 | prose | pages [5] -->
Cross argues that the actual vibrational modes and node points are largely irrelevant since the interaction is localized on the bat. The boundary conditions only matter if vibrations reﬂect oﬀthe boundaries, so an impact close enough to the barrel end of the bat will be aﬀected by the boundary there. In particular, a pulse reﬂecting oﬀa free boundary will return with the same sign (deﬂected away from the ball, decreasing the force on the ball, decreasing the exit velocity), but a pulse reﬂecting of a ﬁxed boundary will return with the opposite sign (deﬂected towards the ball, pushing it back, increasing the exit velocity). Away from the boundary, we expect the exit velocity to be uniform along a non-rotating bat. Cross’s model predicts all of these eﬀects,

<!-- b000068 | furniture | pages [5] -->
5

<!-- b000069 | furniture | pages [6] -->
Team #7586

<!-- b000070 | furniture | pages [6] -->
Page 6 of 15

<!-- b000071 | prose | pages [6] -->
and he has experimentally veriﬁed them. In our model we expect to see similar phenomenology in baseball bats. We also expect the narrowing of the barrel near the handle to act somewhat like a boundary.

<!-- b000072 | prose | pages [6] -->
Nathan’s model also attempted to combine the best features of Van Zandt and Cross.3 His theory used the full Timeshenko theory for the beam and the Cross model for the ball. He even intuitively acknowledged the local nature of impact. So where do we diverge from him? His error stems from an overemphasis on trying to separate out the ball’s interaction with each separate vibrational mode.

<!-- b000073 | prose | pages [6] -->
The ﬁrst sign of inconsistency comes when he uses the “orthogonality of the eigenstates” to determine how much a given impulse excites each mode. The eigenstates are not orthogonal. Many theories yield symmetric matrices that need to be diagonalized yielding the eigenstates, but Timeshenko’s theory does not due to the inclusion of odd-order derivatives into its equations. His story plays out beautifully if only the eigenstates were actually orthogonal, but we have numerically calculated the eigenstates, and they are not even approximately orthogonal. He uses the orthogonality to draw important conclusions. The ﬁrst is that the location of the nodes of the vibrational modes are important. The second is that high frequency eﬀects can be completely ignored. We disagree with both of these.

<!-- b000074 | prose | pages [6] -->
The correct derivation starts with the following equation of motion (with asymmetric H):

<!-- b000075 | prose | pages [6] -->
y′′(t) = H⃗y(t) +⃗F(t)

<!-- b000076 | heading | pages [6] -->
We consider solutions of the form⃗y(t) = an(t)⃗φn(t) where⃗φn is an eigenmode H⃗φn = −ω2

<!-- b000077 | prose | pages [6] -->
n⃗φn. We also let Φnk indicate the n-th component of the k-th eigenmode. Then we write the equation of motion:

<!-- b000078 | prose | pages [6] -->
nan(t)⃗φn = Fn = (Φ−1

<!-- b000079 | prose | pages [6] -->
a′′

<!-- b000080 | prose | pages [6] -->
n(t)⃗φn + ω2

<!-- b000081 | prose | pages [6] -->
nk Fk)⃗φn

<!-- b000082 | prose | pages [6] -->
nan(t) = Φ−1

<!-- b000083 | prose | pages [6] -->
a′′

<!-- b000084 | prose | pages [6] -->
n(t) + ω2

<!-- b000085 | prose | pages [6] -->
nk Fk

<!-- b000086 | prose | pages [6] -->
Nathan’s paper simply uses ΦknFk times some normalization constant on the right hand side.

<!-- b000087 | prose | pages [6] -->
At ﬁrst glance, this seems like a minor technical detail, but the physics here is important. We can calculate that the Φ−1

<!-- b000088 | prose | pages [6] -->
nk Fk terms stay fairly large for even high values of n corresponding to the high frequency modes (k is just the position of the impact.) This means there are signiﬁcant high frequency components, at least at ﬁrst. In fact the high frequency modes are necessary for the impulse to propagate slowly as a wavepacket. In Nathan’s model, only the lowest standing modes are excited, so the entire bat starts vibrating as soon as the ball hits. This contradicts his earlier belief (that we agree with): the collision is over so quickly that the ball only “sees” part of the bat (the collision is local). Nathan’s paper also claims that the sweet spot is related to the nodes of the lowest mode. This also contradicts with locality; the location of the lowest order nodes depends on the geometry of the entire bat, including the boundary conditions at the handle.

<!-- b000089 | prose | pages [6] -->
While the inconsistencies in the Nathan model may well cancel out, we prefer to build our model on For simplicity, we will use the Euler-Bernoulli equations rather than the full a more rigorous footing.

<!-- b000090 | prose | pages [6] -->
The diﬀerence is that the Euler-Bernoulli equations ignores shear forces. Timoshenko equations.

<!-- b000091 | prose | pages [6] -->
This should be acceptable; Nathan points out that his model is largely insensitive to the shear modulus. We will also solve the diﬀerential equations directly after discretizing in space rather than decomposing into modes. In these ways we are following the work of Cross.6

<!-- b000092 | prose | pages [6] -->
On the other hand our model extends Cross’s work in several key ways. First, we will examine parameters much closer to those relevant to baseball (Cross’s model focused on tennis). Cross’s models involved an aluminum beam of width 0.6 cm being hit with a ball of 42 g at around 1 m/s. In our case, we will have an aluminum or wood bat of radius approximately 3 cm being hit with a ball of 145 g traveling at 40 m/s ∗.

<!-- b000093 | prose | pages [6] -->
Second, we will allow for varying cross sectional area, an important feature of a real baseball bat. Third, we will allow the bat to have some initial angular velocity. This will let us scrutinize the rigid body model prediction that higher angular velocities lead to the maximum power point moving further up the barrel.

<!-- b000094 | prose | pages [6] -->
∗This is around 5000 as much impact energy. At one point we changed the ball parameters without changing the bat from Cross’s model, and saw our model predict the bat being knocked out of the way as the ball continued in its original direction.

<!-- b000095 | furniture | pages [6] -->
6

<!-- b000096 | furniture | pages [6] -->
6

<!-- b000097 | furniture | pages [7] -->
Team #7586

<!-- b000098 | furniture | pages [7] -->
Page 7 of 15

<!-- b000099 | prose | pages [7] -->
To reiterate, the main features of our model are an emphasis on ball coupling with the bat, ﬁnite speed of wave propagation in short time-scale, and adaptation to realistic bats. This is a natural outgrowth of the approaches found in the literature.

<!-- b000100 | heading | pages [7] -->
3.2 Mathematics of Our Model

<!-- b000101 | prose | pages [7] -->
Our equations are a discretized version of the Euler-Bernoulli equations:

<!-- b000102 | prose | pages [7] -->
= F(z, t) + ∂2

<!-- b000103 | prose | pages [7] -->
ρ∂2y(z, t)

<!-- b000104 | prose | pages [7] -->
∂t2

<!-- b000105 | prose | pages [7] -->
Y I ∂2y(z, t)

<!-- b000106 | prose | pages [7] -->


<!-- b000107 | prose | pages [7] -->


<!-- b000108 | prose | pages [7] -->
∂z2

<!-- b000109 | prose | pages [7] -->
∂z2

<!-- b000110 | prose | pages [7] -->
In the above equation, ρ is the mass density, y(z, t) is the displacement, F(z, t) is the external force (in our case applied by the ball), Y is the material’s Young’s modulus (a constant), and I is the second moment of area (πR4/4 for a solid disc). We will discretize z in steps of ∆. The only force will be from the ball, which applies a force in the negative direction to the k-th segment. Our discretized equation is:

<!-- b000111 | prose | pages [7] -->
ρA∆d2yi

<!-- b000112 | prose | pages [7] -->
dt2 = −δikF(u(t), u′(t))−Y

<!-- b000113 | prose | pages [7] -->
∆3 (Ii−1(yi−2 −2yi−1 + yi) −2Ii(yi−1 −2yi + yi+1) + Ii+1(yi −2yi+1 + yi+2))

<!-- b000114 | prose | pages [7] -->
Our dynamical variables are y1 through yN. For a ﬁxed left end we pretend y−1 = y0 = 0. For a free left end we pretend y1 −y0 = y0 −y−1 = y−1 −y−2. The conditions on the right end are analogous. These are the same conditions Cross uses.

<!-- b000115 | prose | pages [7] -->
Finally, we have an additional variable for the ball’s position (relative to some constant) w(t). Initially w(t) is positive and w′(t) is negative, so the ball is moving towards the negative from the positive direction. Let u(t) = w(t) −yk(t). This variable will represent the compression of the ball, and we will replace F(t) with F(u(t), u′(t)). Initially u(t) = 0 and u′(t) = −vball. The force between the ball and the bat will take the form of hysteresis curves such as the ones shown in Figure 3b. The higher curve will be taken when u′(t) < 0 (compression) and the lower curve when u′(t) > 0 (expansion). When u(t) > 0 the force is zero. The equation of motion for the ball can then be written:

<!-- b000116 | prose | pages [7] -->
w′′(t) = u′′(t) + y′′

<!-- b000117 | prose | pages [7] -->
We have eliminated the variable w.

<!-- b000118 | prose | pages [7] -->
k(t) = F(u(t), u′(t))

<!-- b000119 | prose | pages [7] -->
As we can see in videos,8 the ball does not act We have yet to specify the function F(u(t), u′(t)). like a rigid object in collisions and instead compresses signiﬁcantly (often more than a centimeter.) This compression and decompression is lossy. We could model this loss by just subtracting some fraction of the ball’s energy after the collision. This is good enough for many purposes, but we will instead follow Nathan and model this as a non-linear spring with hysteresis.

<!-- b000120 | caption | pages [7] -->
Figure 3: Left: An image of a ball hitting a rigid wall.8 The compression is easily visible. Right: A hysteresis

<!-- b000121 | prose | pages [7] -->
curve used in our modeling. The maximum compression here is a very signiﬁcant 1 cm.

<!-- b000122 | furniture | pages [7] -->
7

<!-- b000123 | furniture | pages [7] -->
7

<!-- b000124 | furniture | pages [8] -->
Team #7586

<!-- b000125 | furniture | pages [8] -->
Page 8 of 15

<!-- b000126 | prose | pages [8] -->
R

<!-- b000127 | prose | pages [8] -->
Since W =

<!-- b000128 | prose | pages [8] -->
Fdx the total energy lost is the area between the two curves in Figure 3b. A problem with creating these hysteresis curves is that one does not know the maximum compression (i.e. where to start drawing the bottom curve) until after solving the equations of motion until u′(t) = 0. In practice, we solve the equation in two steps.

<!-- b000129 | prose | pages [8] -->
The main assumptions of our model derive from the main assumptions of each equation. The ﬁrst is the exact form of the hysteresis curve of the ball. It has been argued 6 that the exact form of the hysteresis curve is not very important as long as the duration of impact, magnitude of impulse, maximum compression of the ball, and energy loss are roughly correct. Secondly, both the Timeshenko and Euler-Bernoulli theories ignore azimuthal and longitudinal waves. This is a fundamental assumption built into all of the approaches described so far in the literature. Given that the impact of the ball is transverse and ball does not rotate, the assumption is theoretically justiﬁed. In general, the assumptions of our models are the same as those found in the literature and so even if we cannot carry out experiments, our assumptions are veriﬁed by the literature’s experiments.

<!-- b000130 | heading | pages [8] -->
4. SIMULATION AND ANALYSIS

<!-- b000131 | heading | pages [8] -->
4.1 Simulation Results

<!-- b000132 | prose | pages [8] -->
Our model’s two main features are wave propagation in the bat and the non-linear compression and decom- pression of the ball. The latter is illustrated by the asymmetry of the plot in Figure 4a. This plot also reveals the time-scale of the collision: the ball leaves the bat 1.4 ms after impact. During and after the collision shock waves propagate throughout the bat. In this example the bat was struck 60 cm from the handle. What does the collision look like from 10 cm from the handle? Figure 4b shows the answer: the other end of the bat does not feel anything until about 0.4 ms, and does not feel signiﬁcant forces until about 1.0 ms. By the time that portion of the bat swings back (almost 2.0 ms) the ball has already left contact with the bat. This illuminates an important point: we are only concerned with forces on the ball that act within the 1.4ms time-frame of the collision. Thus, any waves taking longer than that time to return to the impact location do not aﬀect the exit velocity.

<!-- b000133 | caption | pages [8] -->
Figure 4: Left: The force between the ball and the bat as a function of time. We see that the impulse lasts

<!-- b000134 | prose | pages [8] -->
about 1.4 ms. Right: The waveform of the y10(t) when the bat is struck at 60 cm. The impulse reaches this chunk at around 0.4 ms, but it does not start moving signiﬁcantly until later.

<!-- b000135 | prose | pages [8] -->
Having demonstrated the basic features of our model, we will now replicate some of Cross’s results, except with baseball-like parameters. In Figure 5a we show the eﬀects of ﬁxed versus free boundary conditions to be in agreement with Cross’s model. As we expected, ﬁxed boundaries enhanced the exit velocity and free boundaries reduced them. From this we see the eﬀect of the shape of the bat. The handle does indeed act like a free boundary. The distance between the boundaries is too small to get a ﬂat zone in the exit velocity vs. position curve. If we extend the barrel by 26 cm we see a ﬂat zone develop in Figure 5b (notice the change in axes). Intuitively, this ﬂat zone exists because the ball only “sees” the local geometry of the bat and the boundaries are too far away to have a substantial eﬀect.

<!-- b000136 | furniture | pages [8] -->
8

<!-- b000137 | furniture | pages [9] -->
Team #7586

<!-- b000138 | furniture | pages [9] -->
Page 9 of 15

<!-- b000139 | caption | pages [9] -->
Figure 5: Left: Exit velocity vs. impact position for a free boundary (solid line) and ﬁxed boundary (dashed

<!-- b000140 | prose | pages [9] -->
line). Notice that we are ﬁxing the barrel end and leaving the handle end free in both cases. Right: The same graph for a free 110 cm bat.

<!-- b000141 | prose | pages [9] -->
From now on we will use a 84 cm bat that is free on both ends, where position zero denotes the handle end. In this base case the sweet spot is 70 cm. We now investigate the dependence on the exit speed on initial angular velocity. According to rigid body models, the sweet spot is exactly at the center of mass if the bat has no angular velocity. In Figure 6 we present the results of changing angular velocity. Our results contrast greatly with the simple example presented earlier. While the angular rotation eﬀect is still there, the eﬀective mass plays only a negligible role in determining the exit speed in our model. In other words, the bat is not a rigid body because the entire bat does not react instantly. The dominating eﬀect is from the boundaries: the end of the barrel and where the barrel tapers oﬀ. These free ends cause a signiﬁcant drop in exit velocity.

<!-- b000142 | caption | pages [9] -->
Figure 6: Exit velocity vs. impact position at various initial angular velocities of the bat. Our model predicts

<!-- b000143 | prose | pages [9] -->
the solid curves, while the dashed lines represent the simple model. The dots are at the points where Brody’s solution is maximized.

<!-- b000144 | prose | pages [9] -->
Increasing the angular velocity of the bat increases the exit velocity. Of course, much of this is just

<!-- b000145 | furniture | pages [9] -->
9

<!-- b000146 | furniture | pages [10] -->
Team #7586

<!-- b000147 | furniture | pages [10] -->
Page 10 of 15

<!-- b000148 | prose | pages [10] -->
because the impact velocity is greater (by a factor of ωi(z −zcm).) In Figure 7a we show that near the sweet spot, angular velocity actually decreases the excess exit velocity (relative to the impact velocity). We should expect this, since at higher impact velocity, more energy is lost to the ball’s compression and decompression. To conﬁrm this, we also recreated the plot in Figure 7b without the hysteresis curve, where this eﬀect disappears. This example is one of the few places where the hysteresis curve makes a diﬀerence. This conﬁrms experimental evidence91 that the coeﬃcient of restitution decreases with increasing impact velocity.

<!-- b000149 | caption | pages [10] -->
Figure 7: Left: Exit velocity minus impact velocity vs. impact position at various initial angular velocities of

<!-- b000150 | prose | pages [10] -->
the bat. Left: Near the center of mass, higher angular velocity gives higher excess exit velocity, but towards the sweet spot the lines cross and higher angular velocity gives lower excess exit velocity. Right: The same plot without a hysteresis curve. The eﬀect disappears.

<!-- b000151 | prose | pages [10] -->
The results for angular velocity contrast with the simple model. As evident from Figure 6, the rigid-body model greatly overestimates this eﬀect for large angular velocities.

<!-- b000152 | prose | pages [10] -->
,

<!-- b000153 | caption | pages [10] -->
Figure 8: Optimal impact position vs. angular velocity. The line is the rigid-body prediction, while the

<!-- b000154 | prose | pages [10] -->
points are our model’s prediction.

<!-- b000155 | heading | pages [10] -->
4.2 Parameter Space Study

<!-- b000156 | caption | pages [10] -->
Figure 9: The proﬁle of our bat.

<!-- b000157 | prose | pages [10] -->
There are various adjustable parameters in our model. We use ρ = 649 kg/m3 and Y = 1.814 × 1010 N/m2. These values, as well as our bat proﬁle (Figure 9) were taken from Nathan as typical values for a wooden

<!-- b000158 | furniture | pages [10] -->
10

<!-- b000159 | furniture | pages [11] -->
Team #7586

<!-- b000160 | furniture | pages [11] -->
Page 11 of 15

<!-- b000161 | prose | pages [11] -->
bat. While these numbers are in good agreement with other sources, we will see that these numbers are fairly special. As a result of our bat proﬁle, the mass came out to 0.831 kg and the moment of inertia around the center of mass (at 59.3 cm from the handle of our 84 cm bat) was 0.039 kg · m2. We let the 145 g ball’s initial velocity be 40 m/s, and set up our hysteresis curve so that the compression phase was linear with spring constant 7 × 105 N/m.

<!-- b000162 | prose | pages [11] -->
We began by varying the density of the bat, and saw that the current density occupied a narrow region that gave peaked curved exit velocity curves (see Figure 10. We also varied the Young’s modulus and shape of bat to similar eﬀect (see Figure 11.) The fact that varying any of Nathan’s parameters makes the resulting exit velocity versus location plot less peaked means baseball bats are specially designed to have the shape shown in Figure 6 (or the parameters were picked in a special way).

<!-- b000163 | caption | pages [11] -->
Figure 10: Exit velocity vs. impact position for various densities. The solid line is the original ρ = 649 kg/m3.

<!-- b000164 | prose | pages [11] -->
Left: Dotted is 700, dashed is 1000. Right: Dotted is 640, dashed is 500.

<!-- b000165 | caption | pages [11] -->
Figure 11: Left: Varying the value of Y. Solid is Y = 1.1814 × 1010 N/m2. Dashed is 1.25 times as much.

<!-- b000166 | prose | pages [11] -->
Dotted is 0.8 times. Right: Varying the shape of the bat. Solid is the original shape. Dashed has a thicker handle region while dotted has a narrower handle region.

<!-- b000167 | prose | pages [11] -->
Finally we varied the velocity of the ball (see Figure 12. The exit velocity simply scales with the input velocity as expected.

<!-- b000168 | furniture | pages [11] -->
11

<!-- b000169 | furniture | pages [12] -->
Team #7586

<!-- b000170 | furniture | pages [12] -->
Page 12 of 15

<!-- b000171 | caption | pages [12] -->
Figure 12: Varying the velocity of the ball. Solid is the original 40 m/s. Dashed is 50 m/s while dotted is

<!-- b000172 | prose | pages [12] -->
30 m/s.

<!-- b000173 | heading | pages [12] -->
4.3 Alternatives to Wooden Bats

<!-- b000174 | prose | pages [12] -->
Having checked the stability of our model for small parameter changes, we will now change the parameters drastically to model corked and aluminum bats.

<!-- b000175 | prose | pages [12] -->
We modeled a corked bat as a wood bat with the barrel hollowed out, leaving a shell 1 cm or 1.5 cm thick. The result is shown in Figure 13a. The exit velocities are higher, but this diﬀerence is too small to be taken seriously. This result agrees with the literature: the only advantage of a corked bat is the change in mass and moment of inertia.

<!-- b000176 | caption | pages [12] -->
Figure 13: Left: Corked Bat Right: aluminum bat.

<!-- b000177 | prose | pages [12] -->
We modeled an aluminum bat as a 0.3 cm thick shell with density 2700 kg/m3 and Young’s modulus 6.9 × 1010 N/m2. From the exit velocity graph we see that it performs much better than the wood bat (see Figure 13b). It has the same sweet spot (70 cm) and similar sweet spot performance, but the exit velocity falls oﬀmore gradually away from the sweet spot. To gain more insight into the aluminum bat, we animated the displacement of the bats vs. time, and presented two frames of the animation in Figure 14. We can see that the aluminum bat is displaced less (absorbing less energy). More importantly, in the second diagram the curve for the wood bat is still moving down and left, the aluminum bat’s curve is moving left pushing the ball back up. The pulse in the aluminum bat traveled faster and returned in time to give energy back to the ball. By the time the pulse for the wood bat returned to the impact location, the ball had already left the bat.

<!-- b000178 | furniture | pages [12] -->
12

<!-- b000179 | furniture | pages [13] -->
Team #7586

<!-- b000180 | furniture | pages [13] -->
Page 13 of 15

<!-- b000181 | caption | pages [13] -->
Figure 14: Plots of the displacement of an aluminum bat (dashed) and wood bat (solid) being hit by a

<!-- b000182 | prose | pages [13] -->
ball 60 cm from the handle end. The second diagram shows two frames superimposed (t = 1.05 ms and t = 1.10 ms) to show the motion. The rigid translation and rotation has been removed from the diagrams.

<!-- b000183 | prose | pages [13] -->
In the literature the performance of aluminum bats is often attributed to the “trampoline eﬀect” where the bat compresses on impact and then springs back before the end of the collision.10 This would improve The trampoline eﬀect involves exciting so-called “hoop modes,” or aluminum bat performance further. modes with an azimuthal dependence, which our model can not simulate directly. For an aluminum bat one could conceivably use wave equations for a cylindrical sheet (adjusting for the changing radius), and then solve the resulting partial diﬀerential equations in three variables. We started with the equations given by Graﬀ,4 modiﬁed them for a varying radius, and eliminated the torsional components v. The resulting equations are (where R′ = dR/dz):

<!-- b000184 | prose | pages [13] -->
∂2u

<!-- b000185 | prose | pages [13] -->
∂z + ∂2v

<!-- b000186 | prose | pages [13] -->
∂w

<!-- b000187 | prose | pages [13] -->


<!-- b000188 | prose | pages [13] -->
+ 1 −ν

<!-- b000189 | prose | pages [13] -->
∂z2 + ν

<!-- b000190 | prose | pages [13] -->
R

<!-- b000191 | prose | pages [13] -->
∂z∂θ

<!-- b000192 | prose | pages [13] -->
2R

<!-- b000193 | prose | pages [13] -->
w

<!-- b000194 | prose | pages [13] -->


<!-- b000195 | prose | pages [13] -->


<!-- b000196 | prose | pages [13] -->
∂u

<!-- b000197 | prose | pages [13] -->


<!-- b000198 | prose | pages [13] -->
−1

<!-- b000199 | prose | pages [13] -->
R + ∂v

<!-- b000200 | prose | pages [13] -->
R∂θ + ν ∂u

<!-- b000201 | prose | pages [13] -->
+ ∂

<!-- b000202 | prose | pages [13] -->
∂z + ν

<!-- b000203 | prose | pages [13] -->
w + ∂v

<!-- b000204 | prose | pages [13] -->
R′

<!-- b000205 | prose | pages [13] -->
R

<!-- b000206 | prose | pages [13] -->
∂z

<!-- b000207 | prose | pages [13] -->
∂z

<!-- b000208 | prose | pages [13] -->
R

<!-- b000209 | prose | pages [13] -->
∂θ

<!-- b000210 | prose | pages [13] -->
 ∂2v

<!-- b000211 | prose | pages [13] -->
∂θ∂x + ∂2u

<!-- b000212 | prose | pages [13] -->
= ρ(1 −ν2)

<!-- b000213 | prose | pages [13] -->
∂2u

<!-- b000214 | prose | pages [13] -->


<!-- b000215 | prose | pages [13] -->
R∂θ2

<!-- b000216 | prose | pages [13] -->
∂t2

<!-- b000217 | prose | pages [13] -->
E

<!-- b000218 | prose | pages [13] -->
 R′

<!-- b000219 | prose | pages [13] -->
R +1 −ν2

<!-- b000220 | prose | pages [13] -->
Eh q = ρ1 −ν2

<!-- b000221 | prose | pages [13] -->
∂2w

<!-- b000222 | prose | pages [13] -->


<!-- b000223 | prose | pages [13] -->
∂v

<!-- b000224 | prose | pages [13] -->
+1 −ν

<!-- b000225 | prose | pages [13] -->
∂z + ∂u

<!-- b000226 | prose | pages [13] -->
∂

<!-- b000227 | prose | pages [13] -->
∂t2

<!-- b000228 | prose | pages [13] -->
2 ∂θ

<!-- b000229 | prose | pages [13] -->
R∂θ

<!-- b000230 | prose | pages [13] -->
E

<!-- b000231 | prose | pages [13] -->
In order to solve these equations, we would probably write the solution as P

<!-- b000232 | prose | pages [13] -->
n an(z, t) cos(nθ)+bn(z, t) cos(nθ) and then discretize along the z direction. We would keep only the lowest few values of n and then numerically solve the resulting coupled ordinary diﬀerential equations. Analysis of such a complex system of equations is beyond the scope of this paper.

<!-- b000233 | prose | pages [13] -->
Instead we will artiﬁcially insert a hoop mode by hanging a mass from a spring from the spot of the We expect the important modes to be the ones with periods near the collision time bat the ball hits.

<!-- b000234 | prose | pages [13] -->
We ﬁnd that this mode does aﬀect the sweet spot, although the exact change (1.4 ms = 1/(714 Hz)). depending on the frequency does not seem to follow a simple relationship. Our results, as shown in Figure 15 show that hoop modes around 700 Hz do enhance the exit velocity. They not only make the sweet spot wider but also shift the sweet spot slightly towards the barrel end of the bat.

<!-- b000235 | furniture | pages [13] -->
13

<!-- b000236 | furniture | pages [13] -->
13

<!-- b000237 | furniture | pages [14] -->
Team #7586

<!-- b000238 | furniture | pages [14] -->
Page 14 of 15

<!-- b000239 | caption | pages [14] -->
Figure 15: Exit velocity vs. impact position at diﬀerent hoop frequencies. The lines from bottom to top at

<!-- b000240 | prose | pages [14] -->
the left edge (color) are: (blue, starts oﬀthe chart) wood bat, (red) no hoop mode, (gray) 2000 Hz, (black) 500 Hz, (green) 300 Hz, (brown) 800 Hz, and (purple) 1250 Hz.

<!-- b000241 | heading | pages [14] -->
5. CONCLUSION

<!-- b000242 | prose | pages [14] -->
We have modeled a ball-bat collision by using Euler-Bernoulli equations for the bat and hysteresis curves for the baseball. Doing so has allowed us to reconcile the existing literature by emphasizing the role the time-scale of the collision and how the ball only “sees” a local region of the bat because of the ﬁnite speed of wave propagation. As a result, the sweet spot is farther out in our model than the rigid body recoil model predicts. We’re able vary the input parameters and show that the eﬀects are in line with intuition and key results in previous experimental work. Finally, we show that aluminum bats have wider sweet spots than wooden bats.

<!-- b000243 | prose | pages [14] -->
However, our model is far from comprehensive, and we oﬀer several suggestions for improvements and extensions.

<!-- b000244 | prose | pages [14] -->
• The ball is assumed to be non-rotating, and the impact is assumed to be head on. These assumptions are commonly violated in real life. However, rotating balls and oﬀ-center collisions will excite torsional modes in the bat which we entirely ignore. These changes would make the problem non-planar.

<!-- b000245 | prose | pages [14] -->
• We neglect the shear forces in the bat.

<!-- b000246 | prose | pages [14] -->
Future work could incorporate the shear eﬀect by using Timoshenko beam equations.

<!-- b000247 | prose | pages [14] -->
• Our analysis of hoop modes was rather cursory and was tacked on rather than integrated into our main model.

<!-- b000248 | prose | pages [14] -->
Despite these shortcomings, we hope our model is a valuable contribution to the literature.

<!-- b000249 | heading | pages [14] -->
REFERENCES

<!-- b000250 | references | pages [14] -->
[1] R. K. Adair, The Physics of Baseball, 2nd ed. (Harper-Collins, 1994).

<!-- b000251 | references | pages [14] -->
[2] H. Brody, American Journal of Physics 54, 640 (1986).

<!-- b000252 | references | pages [14] -->
[3] A. M. Nathan, American Journal of Physics 68, 979 (2000).

<!-- b000253 | references | pages [14] -->
[4] K. F. Graﬀ, Wave Motion in Elastic Solids, 1st ed. (Dover Publications, Inc., 1975).

<!-- b000254 | references | pages [14] -->
[5] W. Goldsmith, Impact, 1st ed. (Edward Arnold Publishers Ltd., 1960).

<!-- b000255 | references | pages [14] -->
[6] R. Cross, American Journal of Physics 67, 692 (1999).

<!-- b000256 | references | pages [14] -->
[7] L. L. V. Zandt, American Journal of Physics 60, 172 (1992).

<!-- b000257 | furniture | pages [14] -->
14

<!-- b000258 | furniture | pages [15] -->
Team #7586

<!-- b000259 | furniture | pages [15] -->
Page 15 of 15

<!-- b000260 | references | pages [15] -->
[8] A. M. Nathan, http://webusers.npl.illinois.edu/ a-nathan/pob/video.html.

<!-- b000261 | references | pages [15] -->
[9] A. M. Nathan, American Journal of Physics 71, 134 (2003).

<!-- b000262 | references | pages [15] -->
[10] D. A. Russell, http://paws.kettering.edu/ drussell/bats-new/batvibes.html.

<!-- b000263 | furniture | pages [15] -->
15
