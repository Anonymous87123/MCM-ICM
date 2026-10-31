ABSTRACT

In this paper, we determine the sweet spot on a baseball bat. We capture the essential physics of the ball-bat impact by taking the ball to be a lossy spring and the bat to be an Euler-Bernoulli beam. In order to impart some intuition about the model we begin by presenting a rigid body model. Next, we proceed to use our full model to reconcile various correct and incorrect claims about the sweet spot found in the literature. Finally, we discuss the sweet spot and performance of corked and aluminum bats, with a particular emphasis on hoop modes.

1. INTRODUCTION

The status of baseball as the nation’s pastime makes understanding the collision of an irregularly shaped slab of wood with a ball a compelling and interesting problem. The physics of baseball encompasses much more than just the batting of the ball. The pitching of the ball and the ﬂight of the ball are examples of equally important events susceptible to physics modeling. Even limiting one’s scope to the batting of the ball yields a problem of many dimensions. A hitter might expect a model of the baseball-bat collision to yield insight into how the bat breaks, how the bat imparts spin on the ball, how best to swing the bat, and so on.1 We model only the sweet spot.

We have encountered at least two notions of what the sweet spot should be deﬁned as. The ﬁrst comes from what we suspect explains the term sweet spot. This deﬁnition equates the sweet spot with the impact location on the bat which minimizes the discomfort to the hands. We can tentatively give the second deﬁnition as the impact location which maximizes the outgoing velocity of the ball. Some players seem to implicitly identify these two deﬁnitions as the same. We do not identify the two and focus exclusively on the second deﬁnition, which we now deﬁne more carefully.

Given a baseball bat and baseball, the ﬁnal velocity of the ball is determined by the initial velocity and rotation of the ball, initial velocity and rotation of the bat, the relative position and orientation of the bat and ball, and the force over time that the hitter’s hands may apply on the handle. We assume that the ball is not rotating and that the ball’s velocity at impact is perpendicular to the length of the bat. We assume that everything occurs in a single plane and we will argue that the hand’s interaction are actually negligible. In the frame of reference of the center of mass of the bat, the initial conditions are completely speciﬁed by the angular velocity of the bat, the velocity of the ball, and the position of impact along the bat.

Fixing the properties of the bat, ball, initial velocity of the ball, and angular velocity, we can now deﬁne the sweet spot as the location of the point of impact which maximizes the ﬁnal ball velocity. In particular, the location of the sweet depends not just the bat alone, but also the pitch and swing. In order to determine the actual location of the sweet spot, we model the physical eﬀects that we ﬁnd to be most important and allow that model to make a prediction. Here we rapidly explain the features of a few models in the literature.

The simplest model predicts the sweet spot to be at the center of percussion.2 This model assumes that an impact location that minimizes discomfort to the hand also maximizes power transferred to the ball. The model assumes the ball to be a rigid body for which there are conjugate points at which an impact at one will exactly balance the angular recoil and linear recoil at the other. By gripping at one conjugate point and impacting at the other point, the center of percussion, the theory predicted that the hands would experience minimal shock and therefore the ball would exit with high velocity. This point depends heavily on the moment of inertia and the location of the hands. We cannot accept this model because it both erroneously equates the two deﬁnitions of sweet spot and furthermore assumes incorrectly that the bat is a rigid body.

Another model predicts the sweet spot to be between nodes of the two lowest natural frequencies of the bat.3 Given a free bat allowed to oscillate, it’s oscillations can be decomposed into fundamental modes of various frequencies. The intuition is much like that of xylophones or other musical instruments. Diﬀerent geometries and materials have diﬀerent natural frequencies at which they will oscillate. The resulting wave shapes suggest how one would go about exciting those modes. Plucking a string at the node of a vibrational mode will not excite that mode. It is ambiguous which deﬁnition of sweet spot this model uses. Using the ﬁrst deﬁnition, it is focusing on the uncomfortable excitations of vibrational models. Hopefully by choosing the impact location to be near nodes of important frequencies, there will be a minimum of uncomfortable vibrations set up. Using the second deﬁnition, the worry is that energy sent into vibrations of the bat will be lost. This model assumes then that the most important energies to model are those lost to vibration.

This model raises many questions. Which frequencies actually do get excited and why? The Fourier transform of an impulse will in general contain inﬁnitely many modes. Furthermore, wood is a viscoelastic material which quickly dissipates its energies. Is the notion of an oscillating bat even relevant to modeling such a bat? How valid is the condition that the bat is free? Ought the system be coupled with hands on the handle, or the arm’s bone structure, or possibly even the ball? What types of oscillations are relevant? A cylindrical structure can support numerous diﬀerent types of modes beyond the transverse modes usually assumed by this model.4

We discuss these models not only to point out the confusion (advantageous to marketers of fancy bats) surrounding the sweet spot but also to highlight two basic issues in modeling the sweet spot. Following the center of percussion line of reasoning, how do we model the recoil of the bat? Following the vibrational nodes line or reasoning, how do we model the vibrations of the bat? In the general theory of impact mechanics,5 these two eﬀects are the main ones assuming that the bat does not break or deform permanently. We will explain in this paper notable approaches found in the literature by Brody,2 Cross,6 and Nathan.3 Very brieﬂy, Brody ignores vibrations, Cross ignores bat rotation but studies the propagation of the impulse coupled with the ball, and Nathan attempts to emphasize the vibrational modes. Our approach reconciles the tension between these diﬀerent approaches while emphasizing the crucial role played by the time-scale of the collision.

Our main goal is to understand the sweet spot. A secondary goal is to understand the diﬀerences between the sweet spots of diﬀerent bat types. Although marketers of diﬀerent types of bats often emphasize the importance of the sweet spots, there are often other relevant factors involved: ease of swing, tendency of the bat to break, psychological eﬀects, and so on. We once again emphasize that the problem that we investigate is a restricted problem for which we arbitrarily set constant other important factors. For example, we will argue that it doesn’t matter to the collision whether or not the batter’s hands are gripping the handle ﬁrmly or if the batter follows through correctly. This does not have any bearing on the technique required to actually swing the bat or how the bat’s properties aﬀect this.

Our paper is organized as follows. First, we present the Brody rigid body model illuminating the recoil eﬀects of impact. Next we present a full computational model based on wave propagation in a Euler-Bernoulli beam coupled with the ball modeled as a lossy spring. We compare this model with other models found in the literature and explore the local nature of impact, the interaction of recoil and vibrations, and robustness to parameter changes. We adjust the parameters of the model to comment on the sweet spots of corked bats and aluminum bats. Finally, we investigate the eﬀect of hoop frequencies on aluminum bats.

2. A SIMPLE EXAMPLE

We begin by only considering the rigid recoil eﬀects of the bat-ball collision, much in the same way as Brody.2 Consider a bat swung at an incoming baseball. For simplicity of this example, we assume that the bat is perfectly rigid. Because the collision happens on such a short time scale (around 1 ms), we will treat the bat as a free body. That is to say, we are not concerned with the batter’s hands exerting some force on the bat which may be transferred into the ball.

The bat has mass M and moment of inertia I about its center of mass. From the reference frame of the center of mass of the baseball bat before the collision, the ball has velocity vi in the positive x-direction while the bat has an angular velocity of ωi. Note that in our setup, vi and ωi will have opposite signs when the batter is swinging at the ball as in Figure 1. The ball collides with the bat at a distance l from the center of mass of the bat. We assume that the collision is head-on and view the event such that all the y-component velocities are zero at the moment of the collision. After the collision, the ball will have a ﬁnal velocity vf and the bat will have a ﬁnal linear velocity of Vf and an angular velocity of ωf at the center of mass.

When the ball collides with the bat, it brieﬂy compresses and decompresses, converting kinetic energy to potential energy and back. However, some energy is lost in the process, i.e. the collision is inelastic. The ratio of the relative speeds of the bat and the ball before and after the collision is known as the coeﬃcient of restitution, designated by e. In other words e = 0 represents a perfectly inelastic collision, and e = 1 means the collision is perfectly elastic. In this basic model, we make two simplifying assumptions: e is constant along the length of the bat, and e is constant for all vi.

Given our pre-collision conditions, we can write conservation of linear momentum:

MVf = m(vi −vf)

Conservation of angular momentum:

I(ωf −ωi) = ml(vi −vf) Deﬁntion of the coeﬃcient of restitution:

e(vi −ωil) = −vf + Vf + wfl

Solving for vf gives m vf = −vi(e − M ∗) + ωil(1 + e) m 1 + M ∗ M Where M ∗= is the eﬀective mass of the bat. 1+ Ml2 I For calibration purposes, we use the following numbers which are typical of a regulation bat connecting with a fastball in Major League Baseball. The results are plotted below.

m 0.145 kg 5.1 oz M 0.83 kg 29 oz L 0.84 m 33 in 0.039 kg · m2 I vi 67 m/s 150 mph ωi -60 rad/s e 0.55

The maximum exit velocity in our example is around 26.7 m/s, and the sweet spot is 13 cm from the center of mass. Missing the sweet spot by up to 5 cm will only result in a 1 m/s diﬀerence from the maximum speed, implying a relatively wide sweet spot.

From this example, we can already see that the sweet spot is determined by a multitude of factors, including the length, mass, and shape of the baseball bat, the mass of the baseball, and the coeﬃcient of restitution between the bat and ball. Furthermore, the sweet spot is even not uniquely determined by the bat and baseball. It also depends on the incoming baseball speed and the batter’s swing speed. All these factors need to be taken into account to maximize the baseball’s exit speed.

The ﬁgure also shows intuitively why the sweet spot is located somewhere between the center of mass and the end of the barrel. As the point of collision moves outwards along the bat, the eﬀective mass of the bat goes up, so that greater fraction of the initial kinetic energy is put into the bat’s rotation, which. At the same time, the rotation in the bat means that the barrel of the bat is moving faster than center of mass (or handle). These two eﬀects work in opposite directions to give a unique sweet spot that’s not at either endpoint.

However, this model tells only part of the story. Indeed some of our starting assumptions contradict each other. We treated the bat as a free body because the collision time was so short. In essence, during the 1 ms of the collision, the ball will only “see” the local geometry of the bat. The ball will not “see” the batter’s hands on the handle of the bat. On the other hand, we assumed the bat was perfectly rigid. However, this means that the ball “sees” the entire bat. These assumptions clearly cannot both be true. We also assumed that the e was constant along the length of the bat and for diﬀerent collision velocities. Experimental evidence1 suggests that neither issue can be ignored for an accurate prediction of the location of the sweet spot. We will need a more sophisticated model to address all these shortcomings in our simple example and better understand what’s going on.

3. OUR MODEL

We have attempted to combine the best features of previous models into our model. We draw from Brody’s rigid body model as described in the previous section for intuition, but we draw our mathematics most directly from Cross’s work.6 One could accurately describe our work as an adaptation of Cross’s work to actual baseball bats. Nathan also attempted such an adaptation but he was misled by incorrect intuition about the role of vibrations. We describe Nathan’s approach and error as a way to explain Cross’s work and to motivate our work. Next, we present the equations of our model and discuss the main features of its assumptions and methodology.

3.1 Previous Models

In the previous section we encountered Brody’s rigid body model which successfully predicts the existence of a sweet spot not at the end of the bat. That model suﬀers from the fact that the bat is not a rigid body and experiences vibrations. One way to account for those vibrations is to model the bat as a ﬂexible object. Beam theories of varying degrees of accuracy and complication can be used to model the ﬂexible bat. Van Zandt was the ﬁrst to carry out such an analysis modeling the beam as a Timoshenko beam. A Timoshenko beam is a fourth order theory taking into account both shear forces and tensile stresses. The equations are complicated and we will not need them so we will not record them here. His model assumes the ball to be uncoupled from the beam and simply takes the impulse of the ball as a given. The resulting vibrations of the bat are used to more accurately predict the velocity of the beam at the impact point (by summing the Brody velocity with the velocity of the displacement at the impact point due to vibrations) and therefore predict a more accurate exit velocity of the ball still from the equations of the coeﬃcient of restitution.7 The next model we draw on is Cross’s model6 of the interaction of the impact of balls with aluminum beams. His beam used the less elaborate Euler-Bernoulli equations to model the propagation of waves. In addition, he provided equations to model the dynamic coupling of the ball to the beam during the impact. After discretizing the beam spatially, he assumed the ball basically acts as a lossy spring coupled to the single component of the region of impact. Cross’s work is motivated by both the case of tennis rackets and baseball bats. One important diﬀerence in those cases is the time-scale of impact. The baseball bat’s collision only lasts approximately one millisecond in which time the propagation speed of the wave is very important. In this local view of the impact, the importance of the baseball’s coupling with the bat is increased. We will describe both the equations of the Euler-Bernoulli equations and ball’s equations in a later section.

Before continuing let us discuss the main results of the Cross model. Cross argues that the actual vibrational modes and node points are largely irrelevant since the interaction is localized on the bat. The boundary conditions only matter if vibrations reﬂect oﬀthe boundaries, so an impact close enough to the barrel end of the bat will be aﬀected by the boundary there. In particular, a pulse reﬂecting oﬀa free boundary will return with the same sign (deﬂected away from the ball, decreasing the force on the ball, decreasing the exit velocity), but a pulse reﬂecting of a ﬁxed boundary will return with the opposite sign (deﬂected towards the ball, pushing it back, increasing the exit velocity). Away from the boundary, we expect the exit velocity to be uniform along a non-rotating bat. Cross’s model predicts all of these eﬀects, and he has experimentally veriﬁed them. In our model we expect to see similar phenomenology in baseball bats. We also expect the narrowing of the barrel near the handle to act somewhat like a boundary.

Nathan’s model also attempted to combine the best features of Van Zandt and Cross.3 His theory used the full Timeshenko theory for the beam and the Cross model for the ball. He even intuitively acknowledged the local nature of impact. So where do we diverge from him? His error stems from an overemphasis on trying to separate out the ball’s interaction with each separate vibrational mode.

The ﬁrst sign of inconsistency comes when he uses the “orthogonality of the eigenstates” to determine how much a given impulse excites each mode. The eigenstates are not orthogonal. Many theories yield symmetric matrices that need to be diagonalized yielding the eigenstates, but Timeshenko’s theory does not due to the inclusion of odd-order derivatives into its equations. His story plays out beautifully if only the eigenstates were actually orthogonal, but we have numerically calculated the eigenstates, and they are not even approximately orthogonal. He uses the orthogonality to draw important conclusions. The ﬁrst is that the location of the nodes of the vibrational modes are important. The second is that high frequency eﬀects can be completely ignored. We disagree with both of these.

The correct derivation starts with the following equation of motion (with asymmetric H):

y′′(t) = H⃗y(t) +⃗F(t)

We consider solutions of the form⃗y(t) = an(t)⃗φn(t) where⃗φn is an eigenmode H⃗φn = −ω2 n⃗φn. We also let Φnk indicate the n-th component of the k-th eigenmode. Then we write the equation of motion:

nan(t)⃗φn = Fn = (Φ−1 a′′ n(t)⃗φn + ω2 nk Fk)⃗φn nan(t) = Φ−1 a′′ n(t) + ω2 nk Fk Nathan’s paper simply uses ΦknFk times some normalization constant on the right hand side.

At ﬁrst glance, this seems like a minor technical detail, but the physics here is important. We can calculate that the Φ−1 nk Fk terms stay fairly large for even high values of n corresponding to the high frequency modes (k is just the position of the impact.) This means there are signiﬁcant high frequency components, at least at ﬁrst. In fact the high frequency modes are necessary for the impulse to propagate slowly as a wavepacket. In Nathan’s model, only the lowest standing modes are excited, so the entire bat starts vibrating as soon as the ball hits. This contradicts his earlier belief (that we agree with): the collision is over so quickly that the ball only “sees” part of the bat (the collision is local). Nathan’s paper also claims that the sweet spot is related to the nodes of the lowest mode. This also contradicts with locality; the location of the lowest order nodes depends on the geometry of the entire bat, including the boundary conditions at the handle.

While the inconsistencies in the Nathan model may well cancel out, we prefer to build our model on a more rigorous footing. For simplicity, we will use the Euler-Bernoulli equations rather than the full Timoshenko equations. The diﬀerence is that the Euler-Bernoulli equations ignores shear forces. This should be acceptable; Nathan points out that his model is largely insensitive to the shear modulus. We will also solve the diﬀerential equations directly after discretizing in space rather than decomposing into modes. In these ways we are following the work of Cross.6 On the other hand our model extends Cross’s work in several key ways. First, we will examine parameters much closer to those relevant to baseball (Cross’s model focused on tennis). Cross’s models involved an aluminum beam of width 0.6 cm being hit with a ball of 42 g at around 1 m/s. In our case, we will have an aluminum or wood bat of radius approximately 3 cm being hit with a ball of 145 g traveling at 40 m/s ∗.

Second, we will allow for varying cross sectional area, an important feature of a real baseball bat. Third, we will allow the bat to have some initial angular velocity. This will let us scrutinize the rigid body model prediction that higher angular velocities lead to the maximum power point moving further up the barrel.

∗This is around 5000 as much impact energy. At one point we changed the ball parameters without changing the bat from Cross’s model, and saw our model predict the bat being knocked out of the way as the ball continued in its original direction.

To reiterate, the main features of our model are an emphasis on ball coupling with the bat, ﬁnite speed of wave propagation in short time-scale, and adaptation to realistic bats. This is a natural outgrowth of the approaches found in the literature.

3.2 Mathematics of Our Model

Our equations are a discretized version of the Euler-Bernoulli equations:

ρ∂2y(z, t) = F(z, t) + ∂2 Y I ∂2y(z, t)   ∂t2 ∂z2 ∂z2

In the above equation, ρ is the mass density, y(z, t) is the displacement, F(z, t) is the external force (in our case applied by the ball), Y is the material’s Young’s modulus (a constant), and I is the second moment of area (πR4/4 for a solid disc). We will discretize z in steps of ∆. The only force will be from the ball, which applies a force in the negative direction to the k-th segment. Our discretized equation is:

ρA∆d2yi dt2 = −δikF(u(t), u′(t))−Y ∆3 (Ii−1(yi−2 −2yi−1 + yi) −2Ii(yi−1 −2yi + yi+1) + Ii+1(yi −2yi+1 + yi+2)) Our dynamical variables are y1 through yN. For a ﬁxed left end we pretend y−1 = y0 = 0. For a free left end we pretend y1 −y0 = y0 −y−1 = y−1 −y−2. The conditions on the right end are analogous. These are the same conditions Cross uses.

Finally, we have an additional variable for the ball’s position (relative to some constant) w(t). Initially w(t) is positive and w′(t) is negative, so the ball is moving towards the negative from the positive direction. Let u(t) = w(t) −yk(t). This variable will represent the compression of the ball, and we will replace F(t) with F(u(t), u′(t)). Initially u(t) = 0 and u′(t) = −vball. The force between the ball and the bat will take the form of hysteresis curves such as the ones shown in Figure 3b. The higher curve will be taken when u′(t) < 0 (compression) and the lower curve when u′(t) > 0 (expansion). When u(t) > 0 the force is zero. The equation of motion for the ball can then be written:

w′′(t) = u′′(t) + y′′ k(t) = F(u(t), u′(t))

We have eliminated the variable w.

As we can see in videos,8 the ball does not act We have yet to specify the function F(u(t), u′(t)). like a rigid object in collisions and instead compresses signiﬁcantly (often more than a centimeter.) This compression and decompression is lossy. We could model this loss by just subtracting some fraction of the ball’s energy after the collision. This is good enough for many purposes, but we will instead follow Nathan and model this as a non-linear spring with hysteresis.

curve used in our modeling. The maximum compression here is a very signiﬁcant 1 cm.

R Since W = Fdx the total energy lost is the area between the two curves in Figure 3b. A problem with creating these hysteresis curves is that one does not know the maximum compression (i.e. where to start drawing the bottom curve) until after solving the equations of motion until u′(t) = 0. In practice, we solve the equation in two steps.

The main assumptions of our model derive from the main assumptions of each equation. The ﬁrst is the exact form of the hysteresis curve of the ball. It has been argued 6 that the exact form of the hysteresis curve is not very important as long as the duration of impact, magnitude of impulse, maximum compression of the ball, and energy loss are roughly correct. Secondly, both the Timeshenko and Euler-Bernoulli theories ignore azimuthal and longitudinal waves. This is a fundamental assumption built into all of the approaches described so far in the literature. Given that the impact of the ball is transverse and ball does not rotate, the assumption is theoretically justiﬁed. In general, the assumptions of our models are the same as those found in the literature and so even if we cannot carry out experiments, our assumptions are veriﬁed by the literature’s experiments.

4. SIMULATION AND ANALYSIS

4.1 Simulation Results

Our model’s two main features are wave propagation in the bat and the non-linear compression and decom- pression of the ball. The latter is illustrated by the asymmetry of the plot in Figure 4a. This plot also reveals the time-scale of the collision: the ball leaves the bat 1.4 ms after impact. During and after the collision shock waves propagate throughout the bat. In this example the bat was struck 60 cm from the handle. What does the collision look like from 10 cm from the handle? Figure 4b shows the answer: the other end of the bat does not feel anything until about 0.4 ms, and does not feel signiﬁcant forces until about 1.0 ms. By the time that portion of the bat swings back (almost 2.0 ms) the ball has already left contact with the bat. This illuminates an important point: we are only concerned with forces on the ball that act within the 1.4ms time-frame of the collision. Thus, any waves taking longer than that time to return to the impact location do not aﬀect the exit velocity.

about 1.4 ms. Right: The waveform of the y10(t) when the bat is struck at 60 cm. The impulse reaches this chunk at around 0.4 ms, but it does not start moving signiﬁcantly until later.

Having demonstrated the basic features of our model, we will now replicate some of Cross’s results, except with baseball-like parameters. In Figure 5a we show the eﬀects of ﬁxed versus free boundary conditions to be in agreement with Cross’s model. As we expected, ﬁxed boundaries enhanced the exit velocity and free boundaries reduced them. From this we see the eﬀect of the shape of the bat. The handle does indeed act like a free boundary. The distance between the boundaries is too small to get a ﬂat zone in the exit velocity vs. position curve. If we extend the barrel by 26 cm we see a ﬂat zone develop in Figure 5b (notice the change in axes). Intuitively, this ﬂat zone exists because the ball only “sees” the local geometry of the bat and the boundaries are too far away to have a substantial eﬀect.

line). Notice that we are ﬁxing the barrel end and leaving the handle end free in both cases. Right: The same graph for a free 110 cm bat.

From now on we will use a 84 cm bat that is free on both ends, where position zero denotes the handle end. In this base case the sweet spot is 70 cm. We now investigate the dependence on the exit speed on initial angular velocity. According to rigid body models, the sweet spot is exactly at the center of mass if the bat has no angular velocity. In Figure 6 we present the results of changing angular velocity. Our results contrast greatly with the simple example presented earlier. While the angular rotation eﬀect is still there, the eﬀective mass plays only a negligible role in determining the exit speed in our model. In other words, the bat is not a rigid body because the entire bat does not react instantly. The dominating eﬀect is from the boundaries: the end of the barrel and where the barrel tapers oﬀ. These free ends cause a signiﬁcant drop in exit velocity.

the solid curves, while the dashed lines represent the simple model. The dots are at the points where Brody’s solution is maximized.

Increasing the angular velocity of the bat increases the exit velocity. Of course, much of this is just because the impact velocity is greater (by a factor of ωi(z −zcm).) In Figure 7a we show that near the sweet spot, angular velocity actually decreases the excess exit velocity (relative to the impact velocity). We should expect this, since at higher impact velocity, more energy is lost to the ball’s compression and decompression. To conﬁrm this, we also recreated the plot in Figure 7b without the hysteresis curve, where this eﬀect disappears. This example is one of the few places where the hysteresis curve makes a diﬀerence. This conﬁrms experimental evidence91 that the coeﬃcient of restitution decreases with increasing impact velocity.

the bat. Left: Near the center of mass, higher angular velocity gives higher excess exit velocity, but towards the sweet spot the lines cross and higher angular velocity gives lower excess exit velocity. Right: The same plot without a hysteresis curve. The eﬀect disappears.

The results for angular velocity contrast with the simple model. As evident from Figure 6, the rigid-body model greatly overestimates this eﬀect for large angular velocities.

,

points are our model’s prediction.

4.2 Parameter Space Study

There are various adjustable parameters in our model. We use ρ = 649 kg/m3 and Y = 1.814 × 1010 N/m2. These values, as well as our bat proﬁle (Figure 9) were taken from Nathan as typical values for a wooden bat. While these numbers are in good agreement with other sources, we will see that these numbers are fairly special. As a result of our bat proﬁle, the mass came out to 0.831 kg and the moment of inertia around the center of mass (at 59.3 cm from the handle of our 84 cm bat) was 0.039 kg · m2. We let the 145 g ball’s initial velocity be 40 m/s, and set up our hysteresis curve so that the compression phase was linear with spring constant 7 × 105 N/m.

We began by varying the density of the bat, and saw that the current density occupied a narrow region that gave peaked curved exit velocity curves (see Figure 10. We also varied the Young’s modulus and shape of bat to similar eﬀect (see Figure 11.) The fact that varying any of Nathan’s parameters makes the resulting exit velocity versus location plot less peaked means baseball bats are specially designed to have the shape shown in Figure 6 (or the parameters were picked in a special way).

Left: Dotted is 700, dashed is 1000. Right: Dotted is 640, dashed is 500.

Dotted is 0.8 times. Right: Varying the shape of the bat. Solid is the original shape. Dashed has a thicker handle region while dotted has a narrower handle region.

Finally we varied the velocity of the ball (see Figure 12. The exit velocity simply scales with the input velocity as expected.

30 m/s.

4.3 Alternatives to Wooden Bats

Having checked the stability of our model for small parameter changes, we will now change the parameters drastically to model corked and aluminum bats.

We modeled a corked bat as a wood bat with the barrel hollowed out, leaving a shell 1 cm or 1.5 cm thick. The result is shown in Figure 13a. The exit velocities are higher, but this diﬀerence is too small to be taken seriously. This result agrees with the literature: the only advantage of a corked bat is the change in mass and moment of inertia.

We modeled an aluminum bat as a 0.3 cm thick shell with density 2700 kg/m3 and Young’s modulus 6.9 × 1010 N/m2. From the exit velocity graph we see that it performs much better than the wood bat (see Figure 13b). It has the same sweet spot (70 cm) and similar sweet spot performance, but the exit velocity falls oﬀmore gradually away from the sweet spot. To gain more insight into the aluminum bat, we animated the displacement of the bats vs. time, and presented two frames of the animation in Figure 14. We can see that the aluminum bat is displaced less (absorbing less energy). More importantly, in the second diagram the curve for the wood bat is still moving down and left, the aluminum bat’s curve is moving left pushing the ball back up. The pulse in the aluminum bat traveled faster and returned in time to give energy back to the ball. By the time the pulse for the wood bat returned to the impact location, the ball had already left the bat.

ball 60 cm from the handle end. The second diagram shows two frames superimposed (t = 1.05 ms and t = 1.10 ms) to show the motion. The rigid translation and rotation has been removed from the diagrams.

In the literature the performance of aluminum bats is often attributed to the “trampoline eﬀect” where the bat compresses on impact and then springs back before the end of the collision.10 This would improve aluminum bat performance further. The trampoline eﬀect involves exciting so-called “hoop modes,” or modes with an azimuthal dependence, which our model can not simulate directly. For an aluminum bat one could conceivably use wave equations for a cylindrical sheet (adjusting for the changing radius), and then solve the resulting partial diﬀerential equations in three variables. We started with the equations given by Graﬀ,4 modiﬁed them for a varying radius, and eliminated the torsional components v. The resulting equations are (where R′ = dR/dz):

 ∂2v ∂2u ∂z + ∂2v ∂θ∂x + ∂2u = ρ(1 −ν2) ∂2u ∂w  + 1 −ν  ∂z2 + ν R∂θ2 ∂t2 R ∂z∂θ 2R E  R′ R +1 −ν2 Eh q = ρ1 −ν2 ∂2w w   ∂u   +1 −ν ∂v −1 R + ∂v R∂θ + ν ∂u + ∂ ∂z + ν w + ∂v ∂ ∂z + ∂u R′ ∂t2 R ∂z ∂z R ∂θ 2 ∂θ R∂θ E

In order to solve these equations, we would probably write the solution as P n an(z, t) cos(nθ)+bn(z, t) cos(nθ) and then discretize along the z direction. We would keep only the lowest few values of n and then numerically solve the resulting coupled ordinary diﬀerential equations. Analysis of such a complex system of equations is beyond the scope of this paper.

Instead we will artiﬁcially insert a hoop mode by hanging a mass from a spring from the spot of the bat the ball hits. We expect the important modes to be the ones with periods near the collision time (1.4 ms = 1/(714 Hz)). We ﬁnd that this mode does aﬀect the sweet spot, although the exact change depending on the frequency does not seem to follow a simple relationship. Our results, as shown in Figure 15 show that hoop modes around 700 Hz do enhance the exit velocity. They not only make the sweet spot wider but also shift the sweet spot slightly towards the barrel end of the bat.

the left edge (color) are: (blue, starts oﬀthe chart) wood bat, (red) no hoop mode, (gray) 2000 Hz, (black) 500 Hz, (green) 300 Hz, (brown) 800 Hz, and (purple) 1250 Hz.

5. CONCLUSION

We have modeled a ball-bat collision by using Euler-Bernoulli equations for the bat and hysteresis curves for the baseball. Doing so has allowed us to reconcile the existing literature by emphasizing the role the time-scale of the collision and how the ball only “sees” a local region of the bat because of the ﬁnite speed of wave propagation. As a result, the sweet spot is farther out in our model than the rigid body recoil model predicts. We’re able vary the input parameters and show that the eﬀects are in line with intuition and key results in previous experimental work. Finally, we show that aluminum bats have wider sweet spots than wooden bats.

However, our model is far from comprehensive, and we oﬀer several suggestions for improvements and extensions.

• The ball is assumed to be non-rotating, and the impact is assumed to be head on. These assumptions are commonly violated in real life. However, rotating balls and oﬀ-center collisions will excite torsional modes in the bat which we entirely ignore. These changes would make the problem non-planar.

• We neglect the shear forces in the bat. Future work could incorporate the shear eﬀect by using Timoshenko beam equations.

• Our analysis of hoop modes was rather cursory and was tacked on rather than integrated into our main model.

Despite these shortcomings, we hope our model is a valuable contribution to the literature.
