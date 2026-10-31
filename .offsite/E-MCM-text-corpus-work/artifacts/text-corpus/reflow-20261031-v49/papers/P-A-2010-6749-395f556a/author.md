Summary

Aim to determine the location of “sweet spot” and the different “sweet spot” effects of the uncorked, corked and metal bats, we employ methods in dynamics to build models and generate data of batted ball speed by simulation, which exactly match the actual data obtained from experiments.

Based on classical mechanics, we firstly develop a model to describe the collision between ball and bat, from which we obtain the distribution of batted-ball speed (BBS) as the function of the impact location. Then we successfully deduce the location of “sweet spot”, where the BBS reaches the maximum. With all possible case studies, we conclude that “sweet spot” is about 140mm from the end.

Considering the more complex structure of the corked bat, we augment our basic model by building double-spring model and adopting three empirical formulas. Then we are able to adopt the foregoing analytical method to examine the trampoline effect. We carefully analyze the “sweet spot” effect corresponding to the geometrical parameters of “corked hole” and make simulations. The results are illustrated in mesh figures and demonstrate that “sweet spot” effect of the corked bat significantly depends on the density of stuffing materials-“corking” with rubber enhances the “sweet spot” effect while with cork is the opposite.

Based on our models, we design a special metal bat exhibiting faster BBS and similar controllability compared with ordinary wood bats. From the special case, we reach a general conclusion that metal bats tends to outperform wood bats through technical parameters optimization.

What’s more, on the basis of our models, we provide technique tips and formulas for the corked or metal bat design, which will significantly enhance the “sweet spot” effect or make it easier to control. In conclusion, our model successfully achieves our goals that building a useful model both for illumination and application.

1 Introduction

The baseball game not only gains great popularity among young people, but also exerts a certain fascination on physicists. Adair, Brody, Cross, Nathan and Russell all published a number of notable papers addressing both experimental and theoretical issues involved in the ball-bat collision. Their methods range from classical mechanics model to Finite Element simulation. The “sweet spot”, the corked bat, trampoline effect, vibration and metal bats all have been studied to different extent with different approaches. However, the researchers’ work focus on explaining the physical phenomena occurring before, during and after ball-bat collision. Therefore, their research results may not be appropriate to solve the proposed problems. We need to develop a model, neglecting the transient process of collision, possess concise and clear physical meaning. What’s more, the model should be problem-oriented.

The three proposed problems are:  Problem I: Explain why the “sweet spot” is not at the end of the bat.  Problem II: Confirm the fact that “corking” enhances the “sweet spot” effect and explain why MLB prohibits “corking”.  Problem III: Predict different behavior for wood and metal bats and explain why MLB prohibits metal bats.

The bat-ball collision is complicated by the nonlinear compress behavior of the ball and the vibration behavior of the bat. With the help of the current literatures, we first expect to reasonably neglect the influences of the some factors for simplicity and build a classical mechanical model to find the location of “sweet spot” at which the maximum power is transferred to the ball in collision. We want to obtain the “sweet spot” location by solving the dynamic equation, while some more specific problems and case has to be examined. All parameters in the expression have clear physical meanings and could be easily measured. What’s more, we even expect that the expression only includes basic arithmetic operations in order to guide the exercise of baseball sport.

As for corked bats and metal bats, their differences in structure and material may result in better and worse performance compared with ordinary wood bats. So we plan to augment the basic model is to deeply examine the physical meanings of parameters and to modify these parameters in order to fully describe the corked bats and metal bats. On the basis of our model’s results, we provide the explanation for the MLB’s banning of corked bats and metal bats.

2 Assumption

1. No consideration for the failure of the bat. Our model is developed under the precondition that both the uncorked and corked bat are working well. 2. The loss of energy caused by bending vibration is neglected (except for Bending Vibration Part). 3. The uncorked bat is uniform in density and is symmetric to the parallel axis. 4. The stuffing object of the corked bat has the same perpendicular axis as the corked bat.

3 Symbols

The coefficient of restitution 𝐶𝐶𝐶𝐶𝐶𝐶

The coefficient of restitution of bat-ball 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵

The center of mass 𝐶𝐶𝐶𝐶

The moment of inertia with respects to 𝐶𝐶𝐶𝐶 𝑀𝑀𝑀𝑀𝑀𝑀

𝐵𝐵𝐵𝐵𝐵𝐵, 𝑣𝑣𝑓𝑓 The batted ball speed

𝐽𝐽, 𝐽𝐽𝐶𝐶𝐶𝐶 𝑀𝑀𝑀𝑀𝑀𝑀

The equivalent 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝑒𝑒∗

𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 The location of “sweet spot”

The swinging speed and angular speed 𝑉𝑉𝑖𝑖, 𝜔𝜔𝑖𝑖

The location of 𝐶𝐶𝐶𝐶 from the knob 𝑧𝑧𝑐𝑐𝑐𝑐, 𝑎𝑎

4 Details of the Model

4.1Model Overview

To find out the “sweet spot”, we propose a classical mechanics model without consideration for bending vibration. We derive the expression of batted-ball speed (BBS) as the function of 1)impact location, 2)ball mass, 3)ball initial speed, 4) the moment of inertia of bat, 5)the swinging bat speed and 6) the coefficient of restitution(COR). We choose a standard wood bat and employ analytical method to obtain the “sweet spot” location, in which initial speed of ball and swinging bat speed vary over meaningful and practical ranges. The “sweet spot” lies at a point about 15cm away from the end of bat.

Then we build a double-spring (DS) model to modify BBCOR by elaborating the collision on corked bat. We combined the two models to calculate the BBS considering the effects of corking on three parameters. We prove that a typical cork “corking” will weaken the “sweet spot” effect, whereas a typical rubber “corking” will enhance the “sweet spot” effect.

To predict and compare the different behavior of wood and metal bats, we first design a special aluminum bat with the same mass, outline shape, mass center and moment of inertia as that of the standard wood bat; We demonstrate that the special metal bats will have faster BBS and same controllability. Based on the special case, we reach a general conclusion that metal bats tend to have faster BBS and same controllability by optimizing technical parameters. At last, we list some possible negative effects posed by metal bats and explain MLB’s prohibitions of metal bats.

4.2 Fundamental Model

Based on the Momentum Theorem, we obtain

In which

𝐼𝐼 is a linear impulse in 𝑥𝑥 direction which the batter communicates to the ball-bat system during the period of contact, 𝑘𝑘𝑘𝑘⋅𝑚𝑚/𝑠𝑠;

𝑀𝑀 is the mass of the bat, 𝑘𝑘𝑘𝑘;

𝑉𝑉𝑓𝑓 is the velocity of the mass center of the bat at contact after collision (positive or negative), 𝑚𝑚/𝑠𝑠;

𝑉𝑉𝑖𝑖 is the velocity of the mass center of the bat at contact before collision (positive or negative), 𝑚𝑚/𝑠𝑠;

𝑚𝑚 is the mass of the ball, 𝑘𝑘𝑘𝑘;

𝑣𝑣𝑓𝑓 is the velocity of the mass center of the ball at contact after collision (positive or negative), 𝑚𝑚/𝑠𝑠;

𝑣𝑣𝑖𝑖 is the velocity of the mass center of the ball at contact before collision (positive or negative), 𝑚𝑚/𝑠𝑠;

𝜙𝜙, 𝜃𝜃 are the angles of the directions of the ball as illustrated in Figure 1.

Based on the Angular Momentum Theorem, we obtain

In which

𝐿𝐿 is a angular impulse about the direction of 𝜔𝜔 which the batter communicates to the ball-bat system during the period of contact, 𝑚𝑚;

𝑏𝑏 is the distance from the hit spot to the center of mass of the bat, 𝑚𝑚;

𝐽𝐽 is the moment of inertia of the bat about the center of the mass, 𝑘𝑘𝑘𝑘⋅𝑚𝑚2;

𝜔𝜔𝑓𝑓 is the angular velocity of the bat at contract after collision with respect to a vertical axis of rotation passing through its mass center, 𝑟𝑟𝑟𝑟𝑟𝑟/𝑠𝑠;

𝜔𝜔𝑖𝑖 is the angular velocity of the bat at contract before collision with respect to a vertical axis of rotation passing through its mass center, 𝑟𝑟𝑟𝑟𝑟𝑟/𝑠𝑠.

By definition of the coefficient of restitution, we obtain

In which 𝑒𝑒 is the coefficient of restitution with respects to ball and bat (BBCOR, in this model only dependent on materials).

These three equations are sufficient for the determination of the three primed unknowns. In particular, we find the 𝑥𝑥 component of the velocity for the departing ball

4.2.1 Velocity for the Departing Ball

Case I: eliminating the impulse 𝑰𝑰, 𝑳𝑳

With a hard ball (high 𝐶𝐶𝐶𝐶𝐶𝐶) the duration of contact is short and the impulse 𝐼𝐼 and 𝐿𝐿 is therefore small. When the collision has been initiated there is little more for the batter to do [P. Kirkpatrick 1963]. This is also supported by Howard Brody‘s experiment in which he observed the vibrations of a hand-held baseball bat [1989]. According to Howard Brody’s experiment [1989], the hand-held bat

behaves as it were a free body, in other words, the impulse 𝐼𝐼 and 𝐿𝐿 are nearly 0, which is correct in both hardball and softball (more details in Appendix II).

Case II: eliminating the linear velocity 𝝎𝝎𝒊𝒊𝒃𝒃 When the collision takes place near the mass center of the bat, as it very frequently does, all terms containing 𝑏𝑏 may be deleted [P. Kirkpatrick 1963].

Therefore, in many cases, it is quite reasonable to regard the impulse 𝐼𝐼, 𝐿𝐿 and 𝜔𝜔𝑖𝑖𝑏𝑏 as zero. As simplified by these approximations, Eq. 4 can be reduced to (1 + 𝑒𝑒)(𝑉𝑉𝑖𝑖+ 𝜔𝜔𝑖𝑖𝑏𝑏) + 𝑣𝑣𝑖𝑖𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐൬𝑚𝑚 −𝑒𝑒൰ 𝑀𝑀+ 𝑚𝑚𝑏𝑏2 𝐽𝐽 (5) 𝑣𝑣𝑓𝑓= ൬1 + 𝑚𝑚 𝐽𝐽൰𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑀𝑀+ 𝑚𝑚𝑏𝑏2

In order to make the expression simple and easy to understand, we import new symbols:

recoil factor (6) 𝑟𝑟= 𝑚𝑚/𝑀𝑀+ 𝑚𝑚𝑏𝑏2/𝐽𝐽 collision efficiency (7) 𝑞𝑞= (𝑒𝑒−𝑟𝑟)/(1 + 𝑟𝑟) pitch speed (positive) 𝑣𝑣𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏= −𝑣𝑣𝑖𝑖 bat speed (positive) 𝑣𝑣𝑏𝑏𝑏𝑏𝑏𝑏= 𝑉𝑉𝑖𝑖+ 𝜔𝜔𝑖𝑖𝑏𝑏

𝐵𝐵𝐵𝐵𝐵𝐵= 𝑣𝑣𝑓𝑓 batted ball speed the Eq.5 becomes the following two expressions, both of which will be in later analysis.

(1 + 𝑒𝑒)(𝑉𝑉𝑖𝑖+ 𝜔𝜔𝑖𝑖𝑏𝑏) + 𝑣𝑣𝑖𝑖𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐(𝑟𝑟−𝑒𝑒) (8) 𝑣𝑣𝑓𝑓= (1 + 𝑟𝑟)𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐

𝐵𝐵𝐵𝐵𝐵𝐵= 𝑞𝑞𝑣𝑣𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐+ (1 + 𝑞𝑞)𝑣𝑣𝑏𝑏𝑏𝑏𝑏𝑏 (9) 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐

4.2.2 Find the Location of “Sweet Spot”

For the reason that the directions of velocity of ball merely affect the “sweet spot”, we only look for the expression for the location of “Sweet spot” in one simple situation in which 𝜃𝜃= 0, 𝜙𝜙= 0. If 𝜃𝜃≠0 𝑜𝑜𝑜𝑜 𝜙𝜙≠0, the expression for “Sweet spot” location can be deduced in the same way and the result has no significant difference.

Substituting 𝑚𝑚/𝑀𝑀+ 𝑚𝑚𝑏𝑏2/𝑀𝑀 for 𝑟𝑟 in Eq. 8 gives (1 + 𝑒𝑒)(𝑉𝑉𝑖𝑖+ 𝜔𝜔𝑖𝑖𝑏𝑏) + 𝑣𝑣𝑖𝑖൬𝑚𝑚 −𝑒𝑒൰ 𝑀𝑀+ 𝑚𝑚𝑏𝑏2 𝐽𝐽 (10) 𝑣𝑣𝑓𝑓= 1 + 𝑚𝑚 𝑀𝑀+ 𝑚𝑚𝑏𝑏2 𝐽𝐽

Note that when 𝜔𝜔𝑖𝑖= 0 ( the bat has no initial rotational energy), this expression is reduced to (1 + 𝑒𝑒)𝑉𝑉𝑖𝑖+ 𝑣𝑣𝑖𝑖൬𝑚𝑚 −𝑒𝑒൰ 𝑀𝑀+ 𝑚𝑚𝑏𝑏2 𝐽𝐽 (11) 𝑣𝑣𝑓𝑓= 1 + 𝑚𝑚 𝑀𝑀+ 𝑚𝑚𝑏𝑏2 𝐽𝐽

And it is clear that in this case vf will have a maximum at b = 0, which indicates that the “sweet spot” is at the center of mass (CM) when the bat is stationary before the collision.

To obtain the value of 𝑏𝑏 at which 𝑣𝑣𝑓𝑓 can reach the maximum in the general

case (the bat is not initial stationary), we differentiated the expression of 𝑣𝑣𝑓𝑓 with

respect to 𝑏𝑏, set the result be zero and get 𝜔𝜔𝑖𝑖𝑏𝑏2 −2(𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖)𝑏𝑏−𝜔𝜔𝑖𝑖(𝑀𝑀+ 𝑚𝑚)𝐽𝐽 (12) = 0. 𝑚𝑚𝑚𝑚

This equation can be solved for 𝑏𝑏:

2 𝑏𝑏= 𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 ± ඨ൬𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 + 𝐽𝐽(𝑚𝑚+ 𝑀𝑀) (13) ൰ . 𝜔𝜔𝑖𝑖 𝜔𝜔𝑖𝑖 𝑚𝑚𝑚𝑚

𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 The “+” sign will be used here because the value of 𝜔𝜔𝑖𝑖 is negative, and

thus we get 2 𝑏𝑏= 𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 + ඨ൬𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 + 𝐽𝐽(𝑚𝑚+ 𝑀𝑀) (14) ൰ . 𝜔𝜔𝑖𝑖 𝜔𝜔𝑖𝑖 𝑚𝑚𝑚𝑚

It is clearly shown in this expression that this point is not the COP location, since the value of 𝑏𝑏 is dependent upon the ball and bat velocity and the properties of the bat. Particularly, the values of 𝑚𝑚, 𝑀𝑀 and 𝐽𝐽 can be obtained experimentally and 𝑣𝑣𝑖𝑖 as well as 𝑉𝑉𝑖𝑖, 𝜔𝜔𝑖𝑖 are determined respectively by the pitcher throwing the ball and the hitter swinging the bat.

2 𝐽𝐽(𝑚𝑚+𝑀𝑀) 𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 ቃ/ ቀ 𝜔𝜔𝑖𝑖 ቁ If ቂ is less than one, then the square root can be expanded 𝑚𝑚𝑚𝑚 and the result is (𝑧𝑧+ 1)𝜔𝜔𝑖𝑖𝑘𝑘2 (15) 𝑏𝑏≅ 2(𝑉𝑉𝑖𝑖−𝑣𝑣𝑖𝑖)

Where 𝑧𝑧= 𝑀𝑀/𝑚𝑚, 𝑘𝑘= ඥ𝐽𝐽/𝑀𝑀.

4.3 Advanced Model

4.3.1 Overview of Corking

A corked bat is one which has been hollowed a cylinder on the middle of its tip. The size of the drilling hole can be 1 inch in diameter, and 6 to 10 inch deep; the removed part can be replaced with cork, rubber or Styrofoam; a cap is lastly plugged [Nathan 2003]. Since only the “one piece of solid wood bat” is permitted in the MLB [official rules], ordinary wood corked bat is considered in the following parts.

With corked structure, not only is the bat lighter, but the center of mass, or balance point, of the bat moves closer to hands. In technical physics language, the moment of inertia (MOI) of the bat about the CM is reduced which leads to easy-control. What’s more, since the thickness of bat’s shell decreases after corking, the bat’s shell may be compressed during the collision with the ball and springs back, much like a trampoline, resulting in much less loss of energy than would be the case if the ball hit a completely rigid surface. In other words, the equivalent BBCOR (in model above) has decreased.

Summarily, the physics of corked bat and ball collision can be fully identified by the parameters of model above, however, in contrast with the original bat (uncorked), the corked bat exhibits different values of specific parameters, including 𝑀𝑀𝑀𝑀𝑀𝑀, 𝑀𝑀𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 𝐶𝐶𝐶𝐶𝐶𝐶. By examining both the characteristics of the structure of corked bat and the new physical meanings of key parameters in the first model, we augment our first model on the basis of getting the equivalent BBCOR (relating to structure of corked bat) and varying values of parameters.

4.3.2 Double-Spring Model

During the collision between hollowed bat and ball, the “spring” on the bat is exited (the shell of bat is compressed) so that the trampoline effect could be observed in mini-scale. Because of the hoop structure, a radial standing wave and the mentioned bending wave add to a resultant vibration.

To both investigate the radial vibration and avoid developing a novel vibration model, we consider a most common elastic element in Physics, the springs, and use an uncorked bat with a spring attached to simulate the corked bat. What is worth mention is that the model incorporates the effects of elastic collision and energy loss completely in equivalent BBCOR; however, the advanced double spring model illuminates what new physical parameters make up equivalent BBCOR: they are 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑙𝑙, 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏, 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏.

colliding. Where 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 is the stiffness of the ball 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 is the stiffness of the bat 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 is the coefficient of restitution (COR) of the object with ball’s material ball bouncing off a stationary completely elastic object (only dependent on material) 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 is COR of the object with bat’s Corked bat material bouncing off a stationary completely elastic object (only dependent

on material)

4.3.3 Determining Equivalent BBCOR by DS Model

In a reference frame where center of mass of the system (𝐶𝐶𝑀𝑀𝐵𝐵𝐵𝐵𝐵𝐵, consisted of ball, spring and bat) remains at rest, the collision can be divided into the following four procedures: i) The ball and bat (with spring respectively) approach each other; ii) The two springs contact and compress until the velocity (in 𝐶𝐶𝑀𝑀𝐵𝐵𝐵𝐵𝐵𝐵 reference frame) of bat and ball turn to be zero; iii) The ball and bat are accelerated by the springs respectively. In procedure ii and iii, the loss of energy happens through the effect between bat (ball) and spring. iv) The two springs is no longer at contact, and the ball and bat separate each other.

By definition of the coefficient of restitution (the ratio of the differences in velocities before and after the collision) and the physical meaning in energy form, we obtain the equivalent BBCOR (with trampoline effect and material effect inside) in a reference of home frame 𝑒𝑒∗= 𝑣𝑣𝑓𝑓−𝑉𝑉𝑓𝑓 = ඨ𝐸𝐸𝑓𝑓 (16) . 𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 𝐸𝐸𝑖𝑖

Considering the conservation of momentum and the process of collision, the equivalent BBCOR in Fundamental Model is as following 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝑒𝑒∗2 = 2 (17) 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 + 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 2 , 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 where the fraction of energy restored in ball and bat (kinetic energy) 𝑒𝑒∗2 after collision;

𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 the fraction of initial energy stored in ball; 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 2 the fraction of stored energy returned to kinetic energy of ball; 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 the fraction of initial energy stored in bat; 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 the fraction of stored energy returned to kinetic energy of bat. 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 2

( Notes: Mathematical deduction see Appendix I )

4.3.4 Evaluating the “Sweet Spot” Effect

Parameters of bat analysis  Parameter affecting BBS

 Angular and linear velocity 𝜔𝜔𝑖𝑖, 𝑉𝑉𝑖𝑖 According to Eq.4, when  𝜔𝜔𝑖𝑖, 𝑉𝑉𝑖𝑖 increase, 𝐵𝐵𝐵𝐵𝐵𝐵 will increase. Considering the limit of athletes’ biological energy , 𝜔𝜔𝑖𝑖 is affected by 𝐽𝐽 and 𝑉𝑉𝑖𝑖 by 𝑀𝑀.

 Recoil factor 𝑟𝑟 According to Eq.4, the increment of  𝑟𝑟 leads to higher BBS.

 Moment of inertia and mass 𝐽𝐽, 𝑀𝑀 According to Eq. 4, when 𝐽𝐽, 𝑀𝑀 increase, 𝑟𝑟 will decrease which results in higher BBS. However, the increase of 𝐽𝐽, 𝑀𝑀 will respectively leads to the decrease of 𝜔𝜔𝑖𝑖 and 𝑉𝑉𝑖𝑖, which will make BBS decrease.

 Location of “Sweet Spot” 𝑏𝑏 According to Eq. 4, we can obtain the location of “Sweet Spot” 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠, and

using  𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 to calculate the maximum of BBS.

 Equivalent BBCOR 𝑒𝑒∗ According to Eq. 4, the increment of 𝑒𝑒∗ will leads to higher BBS. Since 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 and 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 are determined by materials, 𝑒𝑒∗ will be only determined by 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏.

For clarity, we list the above analysis results in Table 1.

EFFECTS BBS 𝑒𝑒∗ 𝜔𝜔𝑖𝑖 𝑉𝑉𝑖𝑖 𝑟𝑟

𝜔𝜔𝑖𝑖↑

𝑉𝑉𝑖𝑖↑

𝑟𝑟 ↑

+ ↓ ↓ = ? 𝐽𝐽 ↑

+ = ? 𝑀𝑀 ↑ ↓ ↓ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 ↑ ↑ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏

The independent parameters of corked bat only includes 𝑀𝑀, 𝐽𝐽, 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏, 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏, all of which are easily obtained: 𝑀𝑀, 𝐽𝐽 can be easily measured with basic experimental instruments; 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 can be obtained in the tool book, like Mechanical Design Handbook. 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏, 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 can be directly obtained through stiffness measure experiment, instead of  other complex models.

 Parameters affecting Easy Control The lighter weight (smaller 𝑀𝑀) and smaller swing weight (small 𝐽𝐽) also lead to better bat control[Nathan, 2004], which has a beneficial effect for a contact-type hitter, who is just trying to meet the ball squarely rather than get the highest batted ball speed. The batter can accelerate the bat to high speed more quickly with a corked bat, allowing the batter to react to the pitch more quickly, wait longer before committing on the swing, and more easily change in mid-swing.

 Parameters Estimation

 Swinging Angular Speed Estimated by 𝐽𝐽 As showed above, the angular velocity 𝜔𝜔𝑖𝑖 and moment of inertia 𝐽𝐽 have coupling effects on BBS. In order to determine the effect of 𝐽𝐽’s increment on BBS, we need an empirical equation illustrating the relationship between 𝜔𝜔𝑖𝑖 and 𝐽𝐽. We adopt the formula in Daniel A. Russell’s paper [Russell, 2007]. Based on the analysis of the bat swing speed data from the Crisco-Greenwald field study and data fitting done by Alan Nathan, the empirical estimation is −0.30769 𝜔𝜔𝑖𝑖= 45.3 ൬𝐽𝐽𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘 (18) 16000൰

If we know the location of center of mass, we can use the parallel axis theorem to calculate 𝐼𝐼𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘 and the conversion is roughly 𝐼𝐼𝑘𝑘𝑘𝑘𝑘𝑘𝑘𝑘= 𝐽𝐽+ 𝑀𝑀𝑎𝑎2 with units of 𝑜𝑜𝑜𝑜⋅𝑖𝑖𝑛𝑛2.

 Swinging Speed Estimation by 𝑀𝑀 Like the interrelationship between 𝜔𝜔𝑖𝑖 and 𝐽𝐽, 𝑉𝑉𝑖𝑖 and 𝑀𝑀 have the same relationship and coupling effects on BBS. So an empirical equation of 𝑉𝑉𝑖𝑖 and 𝑀𝑀 is wanted. We adopt the model of A.Terry Bahill and Miguel Morna Freitas [1995]. Based on the data for Leah, a member of the University of Arimona, NCAA National Champion softball team, Bahill and Freitas use fitting method to examine the relationship between the mass(𝑀𝑀 with unit of oz) and swinging velocity of bat(𝑉𝑉𝑖𝑖 with unit of mph), getting the following formula

(𝑀𝑀+ 70.4)(𝑉𝑉𝑖𝑖+ 5.4) = 6032. (19)  Stiffness of Hoop Spring Estimation through thickness ( 𝑡𝑡 ) The observed fundamental hoop vibration mode, which accounts for the majority of vibrant energy and is responsible for trampoline effect, has a frequency of about 1 kHz. It means that when the ball leaves the bat, taking place about 1ms after the ball touches the bat [Brody, 1985], the fundamental hoop vibration mode has not been set up. In other words, at the moment that ball exit, it has not “seen” either the knob or tip of the bat. This fact indicates us that we can view the bat as a hoop spring. The hoop stress constant 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 can be identified by an empirical relationship 3 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏∝൬𝑡𝑡 (20) 𝑅𝑅൰ ,

Where 𝑡𝑡 is the thickness of the shell, 𝑚𝑚;

𝑅𝑅 is the radius of the bat cross section, 𝑚𝑚.

Methods for Evaluating “Sweet Spot” Effects  Overview of corking effects I) Effects on parameters by corking

 Since the hallowed wood bat was filled by cork/rubber which has a smaller/larger density, the bat has smaller/larger  𝑀𝑀 and 𝐽𝐽 (in comparison with the uncorked), which leads to smaller/larger 𝑟𝑟 (recoil factor) and higher/lower 𝑉𝑉𝑖𝑖 and 𝜔𝜔𝑖𝑖.

 Since the shell has been thin, the trampoline effect of the bat will be more evident than the uncorked. Enlarging the trampoline effect will significantly increase BBS.

II) Evaluating “Sweet Spot” Effects

 Maximum of BBS Since the BBS is the function of location of hitting point, which gets the maximum in “Sweet Spot” point, we calculate the maximum BBS to estimate the “Sweet Spot” Effect of corked bats. For the reason that there are both positive and negative effects on the maximum BBS after corking, quantitative method is needed.

 Easy Control Since both 𝑀𝑀 and 𝐽𝐽 decrease, we make sure that the corked bat is better to control.

 Methods for quantitative evaluation

i) Neglect the significance of trampoline effect Through rough estimation, the effect of hoop mode of the corked wood bat could be neglected (See details of deduction in Appendix II.). This estimation was also proved by the work of Alan M. Nathan [2003], who gives the quantitative results through experiments. He pointed out that there is nearly no trampoline effect from the hollowed-out wood bat or the cork filler, for the reason that “it requires much greater force to compress such a bat than it does to compress  an aluminum bat”.

Calculating the MOI and mass of corked bat ( 𝐽𝐽𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐, 𝑀𝑀𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐) ii) Based on the definition of moment of inertia and parallel axis theorem, we obtain the MOI of the corked bat as following 2 𝐽𝐽𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐= 𝐽𝐽∗+ ቂ𝑀𝑀+ 𝜋𝜋 (21) 4 (𝜌𝜌−𝜌𝜌0)𝑑𝑑2ℎቃ൬𝑥𝑥𝐶𝐶𝐶𝐶−𝐿𝐿 2൰ ,

where

𝐽𝐽0 = 𝑀𝑀𝑀𝑀𝑀𝑀 𝑤𝑤𝑤𝑤𝑤𝑤ℎ 𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟 𝑡𝑡𝑡𝑡 𝐶𝐶𝐶𝐶 𝑜𝑜𝑜𝑜 𝑡𝑡ℎ𝑒𝑒 𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢 𝑏𝑏𝑏𝑏𝑏𝑏.

And the mass of corked bat is

iii) Measure the structure of corked bat and obtain the values of 𝐷𝐷, 𝐿𝐿, 𝑑𝑑, ℎ. Set 𝜌𝜌0 = the density of wood, 𝜌𝜌= the density of stuffed material (cork or rubber) and calculate the 𝑀𝑀𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢, 𝐿𝐿𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢𝑢, 𝑀𝑀𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐, 𝐿𝐿𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐.

Based on Eq. 4 and Eq. 14, we obtain the maximum BBS of the corked and uncorked bat, and therefore determine whether “corking” a bat enhances the “sweet spot” effect. (Calculation details in Simulation and Results)

5 Simulation and Analysis

5.1 Basic Data Used in Simulation

The uncorked wood bat is the one used by Cross in his extensive set of measurements, which is a 33 in/31 oz Louisville Slugger Model R161 [Cross 1998]. The detail data is shown in Table 2.

5.2 Solution to Problem I

5.2.1 Simulation

As we have shown that the “sweet spot” location is determined by several parameters. The values of 𝑚𝑚, 𝑀𝑀 and J are the constant properties of the baseball and the bat, while the value of 𝑣𝑣𝑖𝑖, 𝑉𝑉𝑖𝑖 and 𝜔𝜔 are determined by the pitcher and the batter. In other words, the 𝑣𝑣𝑖𝑖, 𝑉𝑉𝑖𝑖 and 𝜔𝜔 value will vary over a certain range, which will influence the “sweet spot” location. The properties of the bat we use to simulate are listed in Table 2. Herein, we do a series of calculation based on the variation of 𝑣𝑣𝑖𝑖, 𝑉𝑉𝑖𝑖 and 𝜔𝜔 to investigate the value of 𝑏𝑏.

 The effect of ball speed 𝒗𝒗𝒊𝒊 We analyze the effect of ball speed 𝑣𝑣𝑖𝑖 on the “sweet spot” location 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 in Figure 6 by assigning 𝑣𝑣𝑖𝑖 a series of values (31m/s ~ 50m/s)

and calculating 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠. We vary 𝑣𝑣𝑖𝑖 from 31m/s to 50m/s for practical

concern. The calculation shows that the value of 𝑏𝑏𝑠𝑠𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 is lowered by

increasing the ball speed 𝑣𝑣𝑖𝑖. However, the “sweet spot” location still has a distance of about 0.15m from the tip.

0.40 0.38 0.36 0.34 Distance From Mass Center b (m) 0.32 0.30 0.28 0.26 0.24 tip of the bat 0.22 0.20 0.18 0.16 0.14 0.12 0.10 the sweet spot bsweet spot 0.08 0.06 0.04 0.02 0.00 30 35 40 45 50 Ball speed vi (m/s)

50 m/s. The impact occurs on the standard wood bat, which has a CM speed of 54 mph and a rotational speed about the CM of 51 s-1.

 The effect of swinging speed 𝑽𝑽𝒊𝒊 We analyze the effect of ball speed 𝑣𝑣𝑖𝑖 on the “sweet spot” location 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 in Figure 7 by assigning 𝑉𝑉𝑖𝑖 a series of values (19m/s ~29m/s)

and calculating 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠. Considering the practical situation, we vary 𝑣𝑣𝑖𝑖

from 19m/s to 29m/s. The calculation shows that the value of 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 is

lowered by increasing the swing speed 𝑉𝑉𝑖𝑖 and the effect is smaller than that of the ball speed. In the same manner, the “sweet spot” location still has a distance of about 0.15m from the tip.

0.40 0.38 0.36 0.34 0.32 Distance From Mass Center b (m) 0.30 0.28 0.26 0.24 tip of the bat 0.22 0.20 0.18 0.16 0.14 0.12 0.10 the sweet spot bsweet spot 0.08 0.06 0.04 0.02 0.00 18 20 22 24 26 28 30 Swinging  Speed Vi (m/s)

19m/s to 29 m/s. The impact occurs on the standard wood bat, which has a CM speed of 54 mph and a rotational speed about the CM of 51 s-1.

 The effect of bat rotational speed 𝝎𝝎 We analyze the effect of ball speed 𝜔𝜔 on the “sweet spot” location 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 in Figure 8 by assigning 𝜔𝜔 a series of values (43 𝑠𝑠−1 ~ 61𝑠𝑠−1)

and calculating 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠. Considering the practical situation, we vary 𝜔𝜔from 43 𝑠𝑠−1 to 61𝑠𝑠−1. The calculation shows that the value of 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠

is raised by increasing the swing speed 𝜔𝜔. similarly, the “sweet spot” location still has a distance of about 0.15m from the tip.

0.4

Distance From Mass Center b (m) 0.3

tip of the bat 0.2

0.1 the sweet spot bsweet spot

0.0 40 45 50 55 60 65 -1) Swinging Angular Velocity ω (s

m/s. The impact occurs on the standard wood bat, which has a CM speed of 54 mph and a rotational speed about the CM of 51 s-1.

 the effect of impact location on the value 𝒗𝒗𝒇𝒇(𝑩𝑩𝑩𝑩𝑩𝑩)

Figure 6, Figure 7 and Figure 8 clearly illustrate that the optimum impact location is still far away from the tip of the bat, although the value of 𝑏𝑏𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠(the “sweet spot”) will vary with the value of 𝑣𝑣𝑖𝑖, 𝑉𝑉𝑖𝑖 and 𝜔𝜔. As the

expression of 𝑣𝑣𝑓𝑓 suggests, the impact location will influence the value of 𝑣𝑣𝑓𝑓.

It is tempting to know how big the influence will be, for example, what is the exit velocity of the ball if the collision takes place at other locations other than the “sweet spot”. Herein, We analyze the effect of impact location on 𝑡𝑡𝑡𝑡𝑡𝑡 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠𝑠 𝑣𝑣𝑓𝑓, and put results in Figure 9 by varying the impact location from 0.1m (from the knob) to 0.885m (the tip of the bat). The calculation shows that the value of 𝑣𝑣𝑓𝑓 assumes a parabola-like curve and attains the maximum at the “sweet spot” rather than the tip. This fact provides the direct evidence that the “sweet spot” is not at the tip of the bat.

0.2 0.4 0.6 0.8

50 50

40 40 the sweet spot 30 30 tip of the bat vf(BBS) (m/s) 20 20

10 10

0 0

-10 -10

0.2 0.4 0.6 0.8 distance from knob (m)

standard wood bat, which has a CM speed of 54 mph and a rotational speed about the CM of 51 s-1.

5.2.2 Where is the “Sweet Spot”?

The simulation we perform demonstrates that the “sweet spot” is about 15 cm away from the end of the bat when parameters 𝑣𝑣𝑖𝑖, 𝑉𝑉𝑖𝑖 and 𝜔𝜔 varies over the practical and meaningful ranges. So, we draw a conclusion from the above analysis that:

The “sweet spot” is not at the end of bat.

5.3 Solution to Problem II

5.3.1 BBS Formula Simulation

 The Effects of Ratio of Stiffness (𝒌𝒌𝒃𝒃𝒃𝒃𝒃𝒃𝒃𝒃/𝒌𝒌𝒃𝒃𝒃𝒃𝒃𝒃) on Maximum BBS Based on Table 1, we know that the increase of 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 leads to bigger equivalent BBCOR and therefore leads to higher maximum BBS. In order to make quantitative analysis, at first, we determine the quantitative relationship between 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 and equivalent BBCOR based on the Eq.17, as shown in Figure 10. Secondly, we deduced the relationship between 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏  and maximum BBS using Eq.4, which is illustrated in Figure 11.

𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏~𝑣𝑣𝑓𝑓,𝑚𝑚𝑚𝑚𝑚𝑚 (Figure 11), we can clearly figure out that From semi-log figure of

the increase of maximum BBS becomes quite slow, when 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 is bigger than 1. It illuminates that we should make the 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 smaller than one if we expect more significant trampoline effect which enhances the BBS.

1

0.9

The Equivalent  BBCOR e* 0.8

eball=0.6 0.7

eball=0.5 0.6 eball=0.4

0.5

0.4 -2 -1 0 1 2 10 10 10 10 10 kball/kbat 80

75

Maximum Batted Ball Speed v f,max 70

65

60

55 eball=0.4 eball=0.6 50

eball=0.5 45

40 -2 -1 0 1 2 10 10 10 10 10 kball/kbat

by 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏. The bat is corked with 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏= 0.98, whose CM speed is 24m/s and angular speed is 51rad/s.

 The Effect of Moment of Inertia ( 𝑱𝑱) on Maximum BBS From the Table 1, we may be depressed by the fact that merely qualitative analysis based on the equation of 𝐵𝐵𝐵𝐵𝐵𝐵 is unable  to conclude whether the effect of MOI’s increase on 𝐵𝐵𝐵𝐵𝐵𝐵 is positive or negative. Here, we import the data to do the precise quantitative analysis, and then determine the specific relationship between them.

The procedure to simulate is shown as following

Figure 12 𝐽𝐽 𝜔𝜔𝑖𝑖 Equation 18

Figure 13 𝑏𝑏𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 𝐽𝐽, 𝜔𝜔𝑖𝑖 Equation 14 Figure 14

Equation 4 𝐽𝐽, 𝜔𝜔𝑖𝑖, 𝑏𝑏𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 𝑣𝑣𝑓𝑓,𝑚𝑚𝑚𝑚𝑚𝑚

From Figure 14, we are able to easily make sure that the increase of 𝐽𝐽 (limited in possible field of variation) leads to higher maximum BBS, which is quite useful in comparing the “Sweet Spot” effect of the corked and uncorked bat and designing better corked bat.

37.7

37.65

Swinging Angulr Velocity ωi (rand/s) 37.6

37.55

37.5

37.45

37.4

37.35

37.3

37.25

37.2 0.036 0.038 0.04 0.042 0.044 0.046 0.048 0.05 0.052 0.054 Moment of Inertia of Bat: J (kg⋅m2)

0.125

0.12 Location of Sweet Spot bsweet spot (m) 0.115

0.11

0.105

0.1

0.095

0.09

0.085

0.08 0.036 0.038 0.04 0.042 0.044 0.046 0.048 0.05 0.052 0.054 Moment of Interia of Bat: J (kg⋅ m2)

𝑣𝑣𝑖𝑖= −40𝑚𝑚/𝑠𝑠, 𝑀𝑀= 0.885𝑘𝑘𝑘𝑘.

 The Effect of Mass ( 𝑴𝑴) on Maximum BBS

Similar to the effect of MOI, the effect of Mass on BBS cannot be determined only by qualitative analysis. We make the quantitative analysis in the same procedure as MOI, only replacing 𝜔𝜔𝑖𝑖 with 𝑉𝑉𝑖𝑖, and 𝐽𝐽 with 𝑀𝑀. From Figure 17, we easily obtain the similar result that the increase of 𝑀𝑀 (limited in possible field of variation) leads to higher maximum BBS. What’s more, Figure 17 also tells us that the increase speed of maximum BBS is getting slow with the increase of mass.

Especially, we draw the swinging bat speed 𝑉𝑉𝑖𝑖 and maximum BBS 𝑣𝑣𝑖𝑖 with respect to mass 𝑀𝑀 in the same figure, as Figure 18 shows. Comparing with Figure 4 which is drawn with experimental data [Bahill and Freitas, 1995], our data obtained from calculation of our model exactly match that experimental data, which proves the correctness of our model.

36

34

Swinging Bat Speed: Vi (m/s) 32

30

28

26

24

22 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Mass of Corked Bat: M (kg)

0.3

0.28

Location of SweetSpot: bSweetSpot 0.26

0.24

0.22

0.2

0.18

0.16

0.14

0.12 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Mass of Corked Bat: M (kg) 55

50

45

40 Maximum BBS: Vf,max 35

30

25

20

15

10

5 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Mass of Corked Bat: M (kg)

55

50

45 Batted-Ball Speed: vf 40

35 Speed (m/s) 30

25 Swinging Bat Speed: Vi 20

15

10

5 0 0.2 0.4 0.6 0.8 1 1.2 1.4 Mass of Corked Bat: M (kg)

bat mass 𝑀𝑀. This figure derived from the calculation of our model exactly matches the actual data obtained by experiments.

5.3.2 “Sweet Spot” Effects of Corking

 Simulating details The corked bat can be fully described with the shape of a hallowed cylinder (“Corked Hole”, mathematical described with 𝑑𝑑, ℎ) and the density of the stuffed materials (cork or rubber in this problem). Based on Eq.19 and Eq.18, we are able to calculate the mass and moment of inertia of a specific corked bat, and then obtain the values of maximum BBS which is the key indicator to evaluate “Sweet Spot” effect.

In Figure 19, we set the density of stuffed material 𝜌𝜌𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐= 450𝑘𝑘𝑘𝑘/𝑚𝑚3 to evaluation the “Sweet Spot” effect of different corked bats with the different “Corked Holes”, whose depth and diameter is in the actually possible field of variation (ℎ∈[0, 0.2]𝑚𝑚, 𝑑𝑑∈[0, 0.05]𝑚𝑚) [Russel, 2004].

In Figure 21, the density of stuffed material 𝜌𝜌𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟= 1100𝑘𝑘𝑘𝑘/𝑚𝑚3 to evaluation the “Sweet Spot” effect of different corked bats with the same variation of 𝑑𝑑 and ℎ.

of corked hole, the density of stuffing cork 𝜌𝜌𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐= 450𝑘𝑘𝑘𝑘/𝑚𝑚3, we determined the 𝐽𝐽, 𝑀𝑀, and then obtain maximum BBS. Notes: 𝑣𝑣𝑖𝑖= −40𝑚𝑚/𝑠𝑠, 𝐿𝐿= 840𝑚𝑚𝑚𝑚, 𝑎𝑎= 564𝑚𝑚𝑚𝑚, 𝑚𝑚= 0.145𝑘𝑘𝑘𝑘.

stuffing rubber 𝜌𝜌𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟𝑟= 1100𝑘𝑘𝑘𝑘/𝑚𝑚3, we determined the 𝐽𝐽, 𝑀𝑀, and then obtain maximum BBS. Notes: 𝑣𝑣𝑖𝑖= −40𝑚𝑚/𝑠𝑠, 𝐿𝐿= 840𝑚𝑚𝑚𝑚, 𝑎𝑎= 564𝑚𝑚𝑚𝑚, 𝑚𝑚= 0.145𝑘𝑘𝑘𝑘.

 Results

I. Whether corking enhances “Sweet Spot” effect?  The corked bat with cork stuffed (𝝆𝝆𝒄𝒄𝒄𝒄𝒄𝒄𝒄𝒄< 𝝆𝝆𝒂𝒂𝒂𝒂𝒂𝒂) I n Figure 19 or Figure 20, considering all possible values of 𝑑𝑑 and ℎ, the maximum BBS (𝑣𝑣𝑓𝑓,𝑚𝑚𝑚𝑚𝑚𝑚) of the corked bat with cork stuffed reaches the maximum at the point of 𝑑𝑑= 0, ℎ= 0. In other words, the maximum BBS of all possible corked bat with cork stuffed is lower than that of the uncorked. However, since both 𝑀𝑀 and 𝐽𝐽 decrease, the corked bat is better to control than before.

Therefore, if “Sweet Spot” effect only concerns the maximum BBS (i.e. maximum power transferred to the ball), we can evidently conclude that “corking” a bat with cork stuffed cuts down the “Sweet Spot” effect, no matter what shape of “Corked Hole” is adopted.

 The corked bat with rubber stuffed (𝝆𝝆𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓𝒓> 𝝆𝝆𝒂𝒂𝒂𝒂𝒂𝒂) In Figure 21 or Figure 22, considering all possible values of 𝑑𝑑 and ℎ, the maximum BBS (𝑣𝑣𝑓𝑓,𝑚𝑚𝑚𝑚𝑚𝑚) of the corked bat with rubber stuffed reaches the minimum at the point of 𝑑𝑑= 0, ℎ= 0. In other words, the maximum BBS of all possible corked bat with rubber stuffed is higher than that of the uncorked. However, since both 𝑀𝑀 and 𝐽𝐽 increase, the corked bat becomes more difficult to

control than before.

Therefore, if “Sweet Spot” effect only concerns the maximum BBS (i.e. maximum power transferred to the ball), we can evidently conclude that “corking” a bat with rubber stuffed enhances the “Sweet Spot” effect, no matter what shape of “Corked Hole” is adopted.

II. Why MLB prohibits “corking”

As discussed above, we know that corking the bat with high density material stuffed will significantly enhances the “Sweet Spot” effect which will lead to higher batted ball speed. However, corking the bat with low density material stuffed will leads to better control which may satisfy some part of athletes, like contact-type hitters.

If the Major League Baseball (MLB) does not prohibit “corking”, the athletes can always improve their scores by using higher quality “corking” materials and more sophisticated design of corked bat. If so, the contest is not only the contest on athletes’ baseball skills, but also on the quality of bat, in other words, the technology and money, which will definitely leads to inequality. Aimed to protect the principle of sport-equality, the MLB has to list “corking” technology into taboo.

5.3 Solution to Problem III

Metal bat (usually aluminum bat) has received great popularity for its wider range of “sweet spot”, more power, better feel, and higher performance than the wood one (usually ash bat). What factors contribute to metal bat’s better performance? Why MLB prohibits the metal (aluminum) bat? Herein, we will answer those questions based on conclusions drawn from our previous models.

5.3.1 An Illustration of a Typical Metal Bat

Figure 23 is an illustration of a typical metal bat. Generally speaking, the outer shape of a metal bat and a wood bat is much alike. However, a large amount of metal will be hollowed out to ensure it has an appropriate mass. The shell of bat is about 0.24cm in thickness, about 1/7 of that of a corked wood bat [Nathan, 2004]. It must be mentioned that the shell structure leads to trampoline effect which enhance the performance of metal bats.

enhance its performance.[Nguyen, 2004]

5.3.2 Predicting Behavior of Metal and Wood Bats

 Review of established models

We have developed two models to investigate how structural properties (𝐽𝐽𝑐𝑐𝑐𝑐, 𝑀𝑀,  𝑧𝑧𝑐𝑐𝑐𝑐, coarking) influence the performance of a bat. We picture a logic relationship corresponding to our foregoing models in Figure 24 to facilitate the prediction. In this figure, controllability and 𝐵𝐵𝐵𝐵𝐵𝐵 are introduced to describe the behavior of a bat. Figure 24. clearly shows that both metal and wood bats can be characterized by parameters 𝐽𝐽𝑐𝑐𝑐𝑐, 𝑀𝑀, 𝑧𝑧𝑐𝑐𝑐𝑐 and outer shape, which affects the bats’ controllability and 𝐵𝐵𝐵𝐵𝐵𝐵. Apart from that, metal bats generally have trampoline effect which increases BBS as proved in our DS model. To predict and compare the behavior the two kinds of bats, we first start with a special case.

Denotes Have Denotes Affect

 𝐽𝐽𝑐𝑐𝑐𝑐  𝑀𝑀  𝑧𝑧𝑐𝑐𝑐𝑐 𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐  Outer Solid wood bats shape

𝐵𝐵𝐵𝐵𝐵𝐵 Metal bats (hollowed) Trampoline effect (Force constant 𝑘𝑘)

Intermediate Contrast objectives Behavior variable

can be characterized by parameters 𝐽𝐽𝑐𝑐𝑐𝑐, 𝑀𝑀, 𝑧𝑧𝑐𝑐𝑐𝑐 and outer shape, which affects the bats’ controllability and 𝐵𝐵𝐵𝐵𝐵𝐵; Metal bats have trampoline effect which increases 𝐵𝐵𝐵𝐵𝐵𝐵.

 A special case: the same 𝑱𝑱𝒄𝒄𝒄𝒄, 𝑴𝑴,  𝒛𝒛𝒄𝒄𝒄𝒄, and outer shape  Can such a special metal bat exist?

Before the comparison and prediction, one may cast doubt on the existence of such a special metal bat meeting satisfying these conditions. We do some calculation and obtain such a special metal design parameters and graph as listed below.

Cross in his measurements. It is a 33 in/31 oz Louisville Slugger Model R161 [Cross, 1998]; and the relevant properties are also listed Solid Wood Bat Aluminum Bat same or not M yes 0.885𝑘𝑘𝑘𝑘 0.885 𝑘𝑘𝑘𝑘 𝑧𝑧𝐶𝐶𝐶𝐶 yes 0.564𝑚𝑚 0.564𝑚𝑚 0.840m 0.840m yes 𝐿𝐿 yes 𝐽𝐽𝐶𝐶𝐶𝐶 0.045𝑘𝑘𝑘𝑘⋅𝑚𝑚2 0.045𝑘𝑘𝑘𝑘⋅𝑚𝑚2 density no 670𝒌𝒌𝒌𝒌/𝒎𝒎𝟑𝟑 2700𝒌𝒌𝒌𝒌/𝒎𝒎𝟑𝟑 Outline Shape Totally same yes Trampoline Effect No Yes yes The technique to construct a required bat is stated in the part of technical tips in the paper.

 Prediction and Comparison of behavior for wood and metal bats As Figure 24 demonstrates, such a special metal bat will have the same controllability as the wood bat concerned. However, this special metal bat will have a faster 𝐵𝐵𝐵𝐵𝐵𝐵 due to the contribution of trampoline effect. In a word, our model could predict that a metal bat will outperform the wood bat with the same 𝐽𝐽𝑐𝑐𝑐𝑐, 𝑀𝑀,  𝑧𝑧𝑐𝑐𝑐𝑐, 𝐶𝐶𝐶𝐶𝐶𝐶 and outer shape.

A quantitative analysis on the trampoline effect can be got on Appendix II of this paper. We can see that 𝐵𝐵𝐵𝐵𝐵𝐵 could experience a gap from 45m/s to about 75m/s theoretically.  General cases From the special case, we can conclude that in common situation, metal bats will possess both better BBS and controllability. The reason is that a better metal bat can be manufactured through the following steps on the basis of the special bat design: 1) Reduce  𝐽𝐽𝑐𝑐𝑐𝑐 and 𝑀𝑀 by remove a certain amount of metal, thus increase the controllability. 2) Streamline the inner cavity to enhance the strength of the bat.

After the two steps, the newly-made bat still has strong trampoline effect while its controllability is raised. An experimental example We present another experimental example, in Table 4, which verifies our argument that the aluminum bat exhibit both faster BBS and better controllability.

Crisco,2002] experiment result and model calculation result.

Length Weight Swing Speed 𝑧𝑧𝑐𝑐𝑐𝑐 𝐽𝐽𝑐𝑐𝑐𝑐 BBS (mph) Bat (oz-in2) (in) (oz) (in) (mph) Wood 34 30.9 23 11516 67.9 98.6 bat Metal 33 29.2 20.7 9282 70.9 106.5 bat

5.3.3 Reason for MLB’s Prohibition of Metal Bats

Our above analysis points out metal bats generally have faster 𝐵𝐵𝐵𝐵𝐵𝐵 and better controllability than wood bats do. This is also supported by Crisco and Greenwald Batting Cage Study[Greenwald, 2001; Crisco,2002], which shows that an average batted ball speed for wood bats is around 98.6-mph, while the average batted balls speed for metal bats lies between 100.3 mph and 106.5-mph. The faster travelling ball poses two negative effects on the athletes.

 The faster the ball travels, the less time athletes, such as the pitcher, have to react, thus resulting in injuries more easily. It is generally believed that the pitcher’s reactionary time drops from 0.4s to 0.3s when the ball is hit by a metal bat [Russell, 2008].  The faster the ball travels, the more severe injuries it tends to cause.

Apart from safety concern, we derive from our model that  the advent of the metal bat will weaken the fairness of the game;  powerful bats make athletes dependent upon the tool, not the game itself.

From the above analysis, we conclude the reason that MLB should prohibit metal bats is for concerns of safety and the nature of sport.

6 Technique Tips for Bat Design

One of the important implementation of our model is to instruct the design of a perfect bat.

6.1 Optimum Mass for Better “Sweet Spot” Effect

In order to simplify the process of estimation, we firstly simplify the Eq.4. When the collision takes place near to the mass center of the bat, as it very frequently does, all terms containing b may be deleted [P. Kirkpatrick 1963]. Therefore, 𝑟𝑟= 𝑚𝑚/𝑀𝑀 and Eq.4 becomes (1 + 𝑒𝑒)(𝑉𝑉𝑖𝑖+ 𝜔𝜔𝑖𝑖𝑏𝑏) + |𝑣𝑣𝑖𝑖|𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐(𝑟𝑟−𝑒𝑒) (23) 𝑣𝑣𝑓𝑓= . (1 + 𝑟𝑟)𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 It shows that the velocity of the batted ball speed (BBS) 𝑣𝑣𝑓𝑓 is dependent upon

the ratio of 𝑚𝑚/𝑀𝑀 or 𝑟𝑟. According to the equation, the value of 𝑣𝑣𝑓𝑓 will be raised

if we merely lower the value of 𝑀𝑀 and keep all the other parameters unchanged. However, as is often the case, the swing speed 𝑉𝑉𝑖𝑖 will be decreased when the mass of the bat 𝑀𝑀 becomes larger, which in turn leads to the decrease of 𝑣𝑣𝑓𝑓. One can anticipate that there exists an optimum bat mass on the assumption that the best bat requires that least energy input to impart a given velocity to the ball. We estimate the best mass of bat on the assumption that “that bat is best which requires the least energy input to impart a given velocity to the ball [P. Kirkpatrick 1963]”. Rearrangement of Eq.4 gives (1 + 𝑟𝑟)𝑣𝑣𝑓𝑓𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐+ (𝑒𝑒−𝑟𝑟)𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 (24) 𝑉𝑉𝑓𝑓= . 1 + 𝑒𝑒

The kinetic energy of the bat (neglecting 𝜔𝜔𝑖𝑖) is 2 (1 + 𝑟𝑟)𝑣𝑣𝑓𝑓𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐+ (𝑒𝑒−𝑟𝑟)𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣 𝑊𝑊= 1 2 = 𝑀𝑀 (25) 2 ቈ ቉ 2 𝑀𝑀𝑉𝑉𝑓𝑓 1 + 𝑒𝑒

By differentiating the expression of 𝑊𝑊and setting it to zero, we obtain the minimum of 𝑊𝑊 when 𝑟𝑟= 𝑣𝑣𝑓𝑓𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐+ 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 𝑣𝑣𝑓𝑓𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐−𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣𝑣≅𝑣𝑣𝑓𝑓+ 𝑒𝑒𝑒𝑒 𝑣𝑣𝑓𝑓−𝑣𝑣 (26)

If the 𝑣𝑣𝑓𝑓= −𝑣𝑣𝑖𝑖, then 𝑟𝑟= 1 −𝑒𝑒 (27) . 2

For example, when 𝑒𝑒∗= 0.5, then 𝑟𝑟= 0.25, 𝑀𝑀= 4𝑚𝑚.

6.2 Designing a Special Aluminum Bat

This part primarily serves as the guidance for the case study in Problem III.

The solid wood bat we choose is the one used by Cross in his extensive set of measurements. It is a 33 in/31 oz Louisville Slugger Model R161 [Cross, 1998]; and the relevant properties are listed in Table 5. The parameters of special aluminum bat we design are also listed in Table 5.

Solid Wood Bat Aluminum Bat same or not M yes 0.885𝑘𝑘𝑘𝑘 0.885 𝑘𝑘𝑘𝑘 𝑧𝑧𝐶𝐶𝐶𝐶 yes 0.564𝑚𝑚 0.564𝑚𝑚 0.840m 0.840m yes 𝐿𝐿 yes 𝐽𝐽𝐶𝐶𝐶𝐶 0.045𝑘𝑘𝑘𝑘⋅𝑚𝑚2 0.045𝑘𝑘𝑘𝑘⋅𝑚𝑚2 density no 670𝒌𝒌𝒌𝒌/𝒎𝒎𝟑𝟑 2700𝒌𝒌𝒌𝒌/𝒎𝒎𝟑𝟑 Outline Shape Totally same yes Trampoline Effect No Yes yes

To customize such a bat, we need to reconfigure the mass distribution transversely. One of the possibilities is shown in Figure 26.

𝑚𝑚(𝑧𝑧)

z

according mass distribution function.

According to Table 5 and Figure 26, we derive three constrain equations and assume that the bat is a spinning body.  The mass of the wood bat and the customized bat are equal gives 𝐿𝐿 (28) 𝑀𝑀𝑤𝑤= න𝑑𝑑𝑑𝑑(𝑧𝑧) , 0

where 𝑀𝑀𝑤𝑤 is the mass of the wood bat, 𝑘𝑘𝑘𝑘;

𝑚𝑚(𝑧𝑧) is the mass distribution function of the customized bat;

𝐿𝐿 is the length of the wood bat, 𝐿𝐿.  The mass center of the wood bat and the customized bat are the same gives 𝐿𝐿 ∫𝑧𝑧 ⋅𝑑𝑑𝑑𝑑(𝑧𝑧) (29) 0 𝑧𝑧𝑐𝑐𝑐𝑐 𝑤𝑤= , 𝑀𝑀𝑤𝑤

where 𝑧𝑧𝑐𝑐𝑐𝑐 𝑤𝑤 is the mass center of the wood bat,,𝑘𝑘𝑘𝑘.

 The moment of inertia of the wood bat and the customized bat with respect to the mass center are the same gives 𝐿𝐿 𝑤𝑤= න(𝑧𝑧−𝑧𝑧𝑐𝑐𝑐𝑐)2 ⋅𝑑𝑑𝑑𝑑(𝑧𝑧) (30) 𝐽𝐽𝑐𝑐𝑐𝑐 , 0

where 𝐽𝐽𝑐𝑐𝑐𝑐 𝑤𝑤 is the moment of inertia of the wood with respect to the mass center, 𝑘𝑘𝑘𝑘⋅𝑚𝑚2..

Any mass distribution function 𝑚𝑚(𝑧𝑧) satisfying the above three equations can be used to customize an aluminum bat.

In fact, there exists an infinite number of 𝑚𝑚(𝑧𝑧) functions, yet many of them are complicated or technical impractical. To facilitate the control test and analysis, we adopt a simple and special 𝑚𝑚(𝑧𝑧) as demonstrated by Figure 27.  Derivation of special case

Original Mass 𝑀𝑀𝑏𝑏 Removed Mass Ma

Axis of  zcm

unknown); Shadowed part and white part are distinguished to help the according theoretical derivation of mass distribution m(z) and the inner shape of bat.

We let 𝑀𝑀𝑎𝑎 be the mass of the removed part, and 𝑀𝑀𝑏𝑏 be the mass of the rest part. Because the outline shape of two bats are same, which means the two bats have the same volume if stuff the removed part 𝑀𝑀𝑎𝑎 back, we have 𝑀𝑀𝑎𝑎+ 𝑀𝑀𝑏𝑏 𝜌𝜌𝐴𝐴𝐴𝐴 = , (31) 𝑀𝑀𝑤𝑤 𝜌𝜌𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤

where 𝑀𝑀𝑤𝑤 is the mass of the wood bat,𝑘𝑘𝑘𝑘; 𝜌𝜌𝐴𝐴𝐴𝐴 is the density of aluminum, 𝑘𝑘𝑘𝑘/𝑚𝑚3; 𝜌𝜌𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤 is the density of wood,𝑘𝑘𝑘𝑘/𝑚𝑚3. For the same reason, the mass center equation and the moment of inertia equation1 , we also have 𝑀𝑀𝑎𝑎⋅𝑧𝑧𝑐𝑐𝑐𝑐,𝑎𝑎+ 𝑀𝑀𝑏𝑏⋅𝑧𝑧𝑐𝑐𝑐𝑐,𝑏𝑏= (𝑀𝑀𝑎𝑎+ 𝑀𝑀𝑏𝑏)𝑧𝑧𝑐𝑐𝑐𝑐 𝑤𝑤 (32)

1 The moment of inertia and mass center are both linear quantities in terms of density.

𝑎𝑎 𝑏𝑏 𝐽𝐽𝑐𝑐𝑐𝑐 + 𝐽𝐽𝑐𝑐𝑐𝑐 𝜌𝜌𝐴𝐴𝐴𝐴 (33) = 𝑤𝑤 𝐽𝐽𝑐𝑐𝑐𝑐 𝜌𝜌𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤

Using the three constrain equations, we can get the mechanics parameters of the removed part. 𝑀𝑀𝑏𝑏= ൬𝜌𝜌𝐴𝐴𝐴𝐴 −1൰𝑀𝑀𝑤𝑤 (34) 𝑀𝑀𝑏𝑏= 𝑀𝑀𝑤𝑤 & 𝐸𝐸𝐸𝐸. (31) ⇒ 𝜌𝜌𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤 𝑧𝑧𝑐𝑐𝑐𝑐,𝑎𝑎= 𝑧𝑧𝑐𝑐𝑐𝑐 𝑤𝑤 & 𝐸𝐸𝐸𝐸. (32) 𝑧𝑧𝑐𝑐𝑐𝑐,𝑏𝑏= 𝑧𝑧𝑐𝑐𝑐𝑐 𝑤𝑤 (35) ⇒

= ൬𝜌𝜌𝐴𝐴𝐴𝐴 𝑏𝑏 −1൰𝐽𝐽𝑐𝑐𝑐𝑐 𝐽𝐽𝑐𝑐𝑐𝑐 𝑤𝑤 𝑏𝑏 (36) ⇒ 𝐽𝐽𝑐𝑐𝑐𝑐 = 𝐽𝐽𝑐𝑐𝑐𝑐 𝑤𝑤 & 𝐸𝐸𝐸𝐸. (33) 𝜌𝜌𝑤𝑤𝑤𝑤𝑤𝑤𝑤𝑤

Through calculation we obtain a diagram of the demo bat in Figure 25.

7 Discussion and Conclusion

We develop two models to elaborate the ball-bat collision. It has been shown that the models’ simulation well match the empirical data and well explain some phenomena. It seems that some physical issues including the vibration of the bat and the nonlinear compress behavior of ball have been neglected in our paper. However it’s not that case. We will validate our concise model in the following part.

7.1 Model Validation

Literature review indicates that some researchers have developed more complicated models (see Figure 28) to show the dynamic features and vibrant features. With advanced models, such phenomena as bending vibration, hoop vibration, and so on. As listed four models in Figure 28, the latter two, #3 and #4 do no good to answer the proposed problems. The energy stored in the wave on the bat after the collision is a part of consuming energy considered in modification of parameter, 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵, in the first two models.

Such a technique is quite useful in practice, because we can do experiment to determine 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵.

7.2 Bending Vibration

In the fundamental model, we treat the bat as a rigid body and neglect the potential vibration excited by the collision. Actually, during and after collision, the baseball bat might exhibit several flexural bending modes of vibration, and the energy stored in the vibration movement is dependent on impact location. It is possible that at the “sweet spot” obtained in the fundamental modal will shift if intensive vibration consuming a large amount of energy is excited. Therefore it is worthwhile to enhance the fundamental model by taking into account the influence of the potential vibration on the performance of the bat.

It is natural that the existence of the bending vibration will give rise to the change of 𝑣𝑣𝑓𝑓 , which is determined by the properties of the bat and the baseball and the characteristics of the collision. According to the research work of Alan M. Nathan [2000], the expression of 𝑣𝑣𝑓𝑓 can be modified by replacing 𝑒𝑒 with 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒, as stated below:

𝑣𝑣𝑓𝑓= ቂ𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒−𝑟𝑟 1 + 𝑟𝑟ቃ𝑣𝑣𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ ൤𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒+ 1 (37) 1 + 𝑟𝑟൨𝑣𝑣𝑏𝑏𝑏𝑏𝑏𝑏.

In this equation, 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 is an effective coefficient of restitution for the collision of the ball with a flexible bat, contains all the dynamical information about the collision and has the desired properties that it reduces to 𝑒𝑒 in the limit that vibration are neglected[Alan M. Nathan 2000]. It has been shown that 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 depends strongly on the impact location yet weakly on the impact speed in Nathan’s [2000] work.

Nathan investigated the baseball-bat collision from the perspective of vibration, two important results in his work are cited below:  the vibration energy fraction as a function of impact location 30

25

% Vibration Energy 20

15

10

5

0 40 50 60 70 80 Distance From Knob (cm)

bat, which has a CM speed of 54 mph and a rotational speed about the CM of 51 s-1.

 the value of 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 as a function of impact location

0.55

0.50

0.45

0.40

0.35 eeff 0.30

0.25

0.20

0.15

40 50 60 70 80 Distance From Knob (cm) speed of 54 mph and a rotational speed about the CM of 51 s-1.

From the two figures, we can draw a conclusion that in the region 68-74 𝑐𝑐𝑐𝑐 the vibration energy is small and 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 is relatively large. This conclusion also enhances the reasonability of the fundamental model that does not consider the possible bending vibration effect, since the vibration energy is about 5% of the total energy when collision occur at the “sweet spot”. It is quite clear that the “sweet spot” is not on the bat end.

7.3 Problems Review

The three proposed problems have been well answered in our model simulation and results part.  Where is the “sweet spot”?

We find out that the “sweet spot” is located at a point about 15 cm from the end of the tip, which supports the empirical finding.  How about the “corking” effects?

We find out that the “corking” effect mainly depends on the shape hollowed cylinder and the filing material density. Corking rubber (density larger than ash) enhances the “sweet spot” effect, while corking cork (density smaller than ash) weakens the “sweet spot” effect. For the same corking material, the enhancing/weakening effect is dependent upon the shape of the hollowed cylinder. This model explains the penalty MLB gave to some players using specially-corked bat.  How about metal bats?

We find out that a well-designed metal bat will possesses good qualities of faster 𝐵𝐵𝐵𝐵𝐵𝐵 and better controllability than that of the wood one (usually ash bat). Our analysis exhibits the reason that MLB prohibits metal bats.

7.4 Strengths

 Our concise model is in good agreement with the experiment data. That’s to say our model is practical to some extent, especially the model possess clear mode.  We have well analyzed the performance of a bat, and controllability along with “sweet spot” effect is separately analyzed. Thus the analysis of the calculation results will be closer to the actuality.  Our model has been developed to show the interrelationship of geometrical attributes, mechanical attributes and the performance. This can help the design of bat, and simultaneously, we have a in-depth understanding on the ball-bat interaction.

7.5 Weaknesses

 We haven’t elaborately modeled the transverse wave and hoop vibration; the error introduced is about 5% (see details in the foregoing bending mode part).  We have used three empirical formulas and each has its own limitation and error.

Appendix I

Mathematical Process for deducing equivalent BBCOR In a reference frame where center of mass of the system (𝐶𝐶𝑀𝑀𝐵𝐵𝐵𝐵𝐵𝐵, consisted of ball, spring and bat) remains at rest, we define new symbols 𝑣𝑣𝑖𝑖 𝑐𝑐= 𝑣𝑣𝑖𝑖−𝑣𝑣𝑐𝑐   𝑣𝑣𝑓𝑓 𝑐𝑐= 𝑣𝑣𝑓𝑓−𝑣𝑣𝑐𝑐

𝑉𝑉𝑖𝑖 𝑐𝑐= 𝑉𝑉𝑖𝑖−𝑣𝑣𝑐𝑐   𝑉𝑉𝑓𝑓 𝑐𝑐= 𝑉𝑉𝑓𝑓−𝑣𝑣𝑐𝑐

in which the speed of the center of mass of the system 𝑣𝑣𝑐𝑐= 𝑚𝑚𝑣𝑣𝑖𝑖+ 𝑀𝑀𝑉𝑉𝑖𝑖 . 𝑚𝑚+ 𝑀𝑀

The collision in 𝐶𝐶𝑀𝑀𝐵𝐵𝐵𝐵𝐵𝐵 reference frame can be divided into the following four procedures: v) The ball and bat (with spring respectively) approach each other; vi) The two springs contact and compress until the velocity (in 𝐶𝐶𝑀𝑀𝐵𝐵𝐵𝐵𝐵𝐵 reference frame) of bat and ball turn to be zero; vii) The ball and bat are accelerated by the springs respectively. In procedure ii and iii, the loss of energy happens through the effect between bat (ball) and spring. viii) The two springs is no longer at contact, and the ball and bat separate each other.

By definition of the coefficient of restitution (the ratio of the differences in velocities before and after the collision), we obtain the equivalent BBCOR (with trampoline effect and material effect inside) in a reference of home frame 𝑒𝑒∗= 𝑣𝑣𝑓𝑓−𝑉𝑉𝑓𝑓 𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖

Considering the conservation of momentum, we obtain 𝑐𝑐= −𝑚𝑚 𝑐𝑐= −𝑚𝑚 𝑚𝑚𝑣𝑣𝑖𝑖 𝑐𝑐+ 𝑀𝑀𝑉𝑉𝑖𝑖 𝑐𝑐= 𝑚𝑚𝑣𝑣𝑓𝑓 𝑐𝑐+ 𝑀𝑀𝑉𝑉𝑓𝑓 𝑐𝑐= 0 ⇒𝑉𝑉𝑓𝑓 𝑀𝑀𝑣𝑣𝑓𝑓 𝑐𝑐, 𝑉𝑉𝑖𝑖 𝑀𝑀𝑣𝑣𝑖𝑖 𝑐𝑐.

Then the equivalent BBCOR becomes 𝑐𝑐+ 𝑚𝑚 𝑐𝑐 𝑐𝑐 𝑐𝑐 𝑣𝑣𝑓𝑓 𝑀𝑀𝑣𝑣𝑓𝑓 𝑣𝑣𝑓𝑓 𝑐𝑐−𝑉𝑉𝑓𝑓 𝑣𝑣𝑓𝑓 𝑒𝑒∗= 𝑣𝑣𝑓𝑓−𝑉𝑉𝑓𝑓 = 𝑐𝑐= 𝑐𝑐= 𝑐𝑐. 𝑐𝑐+ 𝑚𝑚 𝑣𝑣𝑖𝑖−𝑉𝑉𝑖𝑖 𝑣𝑣𝑖𝑖 𝑐𝑐−𝑉𝑉𝑖𝑖 𝑣𝑣𝑖𝑖 𝑣𝑣𝑖𝑖 𝑀𝑀𝑣𝑣𝑖𝑖

We may also understand the physical meaning of BBCOR in the way of energy as following:

∵𝐸𝐸𝑖𝑖= 1 𝑐𝑐)2 + 1 𝑐𝑐)2 = 1 𝑐𝑐)2(1 + 𝑚𝑚 2 𝑚𝑚(𝑣𝑣𝑖𝑖 2 𝑀𝑀(𝑉𝑉𝑖𝑖 2 𝑚𝑚(𝑣𝑣𝑖𝑖 𝑀𝑀)

𝐸𝐸𝑓𝑓= 1 2 = 1 2 𝑚𝑚൫𝑣𝑣𝑓𝑓 𝑐𝑐൯ 2 𝑀𝑀൫𝑉𝑉𝑓𝑓 𝑐𝑐൯ 2 𝑚𝑚൫𝑣𝑣𝑓𝑓 𝑐𝑐൯ 2 + 1 2(1 + 𝑚𝑚 𝑀𝑀)

𝐸𝐸𝑓𝑓 ∴𝑒𝑒∗2 = 𝐸𝐸𝑖𝑖 means that the 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝑅𝑅2 is the fraction of energy restored in system

after collision.

The total energy in the BSB system at contact before collision is 𝐸𝐸𝑖𝑖. If no loss of energy happens when the kinetic energy transfers to the spring, the total energy fully converts to the potential energy in spring at the end of procedure ii. Since the total momentum remains zero all times, the point where two springs contact remains at rest in BSB reference frame. Therefore, if no loss of energy happens, 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 ⎧Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏= Δ𝑥𝑥 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 ൜𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏= 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑡𝑡  ⇒  Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏= Δ𝑥𝑥 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 ⎨ Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏= Δ𝑥𝑥 ⎩ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏

the energy stored in the spring attached on ball is 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏= 1 = 1 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 2 2 ൬ 𝐸𝐸𝑖𝑖 2 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 2 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 (𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏)2൰

𝑏𝑏𝑏𝑏𝑏𝑏= 1 = 1 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 2 2 ൬ 𝐸𝐸𝑖𝑖 2 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏 2 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏Δ𝑥𝑥𝑏𝑏𝑏𝑏𝑏𝑏 (𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏)2൰

Considering conservation of total energy 𝐸𝐸𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝐸𝐸𝑏𝑏𝑏𝑏𝑏𝑏= 𝐸𝐸 and the physical meaning of BBCOR in energy perspective 𝑒𝑒2 = 𝐸𝐸𝑓𝑓/𝐸𝐸, we obtain 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 2 2 𝐸𝐸𝑓𝑓 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏= 𝐸𝐸𝑖𝑖 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 = 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝐸𝐸 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏

𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 2 𝐸𝐸𝑓𝑓 𝑏𝑏𝑏𝑏𝑏𝑏= 𝐸𝐸𝑖𝑖 𝑏𝑏𝑏𝑏𝑏𝑏𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 = 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 2 𝐸𝐸 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏

Therefore, in the collision of ball and corked bat, the different part of Eq. 16 is as following 𝑏𝑏𝑏𝑏𝑏𝑏 𝐸𝐸𝑓𝑓 𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝐸𝐸𝑓𝑓 𝑒𝑒∗2 = 𝐸𝐸𝑓𝑓 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 2 = = 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 + 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 2 . 𝐸𝐸𝑖𝑖 𝐸𝐸𝑖𝑖 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑎𝑎𝑎𝑎𝑎𝑎+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 where

the fraction of energy restored in ball and bat (kinetic energy) 𝑒𝑒∗2 after collision; 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 the fraction of initial energy stored in ball; 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 2 the fraction of stored energy returned to kinetic energy of ball; 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏 the fraction of initial energy stored in bat; 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏+ 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 the fraction of stored energy returned to kinetic energy of bat. 𝑒𝑒𝑏𝑏𝑏𝑏𝑏𝑏 2

Appendix II

The Stiffness of the Corked Bat’s Shell Trampoline effect can be observed in the hollowed bat [Russell, 2004]. We have augmented our model from fundamental model to DS model, by which we know how the relative stiffness between ball and bat "𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏" influences the values of  𝐵𝐵𝐵𝐵𝐵𝐵 and 𝑣𝑣𝑓𝑓. However, going a further step, we will discuss, to what extent

does hollowing affects "𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏𝑏𝑏/𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏", and then 𝑡𝑡ℎ𝑒𝑒 𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒𝑒 𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵𝐵 𝑒𝑒∗, as well as the “sweet spot” effect.

 Hoop Spring The observed fundamental hoop vibration mode, which accounts for the majority of vibrant energy and is responsible for trampoline effect, has a frequency of about 1 kHz. It means that when the ball leaves the bat, taking place about 1 ms after the ball touches the bat [H. Brody, 1985], the fundamental hoop vibration mode has not been set up. In other words, at the moment that ball exit, it has not “seen” either the knob or tip of the bat. This fact indicates us that we can view the bat as a hoop spring. The hoop stress constant 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 can be identified by an empirical relationship 3 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏∝൬𝑡𝑡 𝑅𝑅൰ , Where 𝑡𝑡 is the thickness of the shell;

𝑅𝑅 is the radius of the bat cross section;  Calculation of an Instance A typical wood bat has a cross section diameter of 2.3 in, and the removed cylinder has a diameter of 1 in; accordingly, the maximum and minimum 𝑘𝑘𝑏𝑏𝑏𝑏𝑏𝑏 proportion can be estimated by:

3 3 𝑘𝑘𝑚𝑚𝑚𝑚𝑚𝑚 𝑘𝑘𝑚𝑚𝑚𝑚𝑚𝑚= ൬𝑡𝑡𝑚𝑚𝑚𝑚𝑚𝑚 = ൬2.3 ൰ 1.3൰ ≈5.5 𝑡𝑡𝑚𝑚𝑚𝑚𝑚𝑚

3 𝑊𝑊 𝑊𝑊 3 𝑘𝑘𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 𝑡𝑡𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 = ൬2.3 ቇ 1.3൰ = ቆ ≈5.5 𝑊𝑊 𝑊𝑊 𝑘𝑘𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐 𝑡𝑡𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐𝑐

A typical aluminum bat can be extremely hollowed; practically, the rest hoop thickness of aluminum bat can be 1/7 of that of the wood one [Nathan, 2004]; accordingly, the maximum and minimum 𝑘𝑘ℎ𝑜𝑜𝑜𝑜𝑜𝑜 proportion can be estimated by:

3 3 𝑘𝑘𝑚𝑚𝑚𝑚𝑚𝑚 𝑘𝑘𝑚𝑚𝑚𝑚𝑚𝑚= ൬𝑡𝑡𝑚𝑚𝑚𝑚𝑚𝑚 = ൬2.3 ൰ 1.3 × 7൰ ≈1886.5 𝑡𝑡𝑚𝑚𝑚𝑚𝑚𝑚

3 𝑀𝑀 𝑀𝑀 3 𝑘𝑘𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 𝑡𝑡𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 = ൬2.3 ቇ 1.3 × 7൰ = ቆ ≈1886.5 𝑀𝑀 𝑀𝑀 𝑘𝑘ℎ𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜 𝑡𝑡ℎ𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑜𝑒𝑒𝑒𝑒

80

1886.5 75

5.5 Maximum Batted Ball Speed v f,max 70

65

60

55 eball=0.4 eball=0.6 50

eball=0.5 45

40 -2 -1 0 1 2 10 10 10 10 10 kball/kbat

Based on the figure above, we can figure out that the trampoline effect of thin metal shell bat is quite significant while wood corked bat not.

Appendix III

Codes for MATLAB % *********************************************** % codes for drawing mesh and contour figures % *********************************************** [h,R]=meshgrid(0:0.0005:0.2); R = R/10; % ****************************** d=R*2; L=.84; a=.564; M=.885; rho1=450;rho2=1100; % ****************************** J1=0.045+pi/48.*(rho1-670).*(d.^2.*h).*(.75*d.^2+h.^2)+pi/4.*(rho1-67 0).*d.^2.*h.*(L-a-h/2).^2+(M+pi/4.*(rho1-670).*d.^2.*h).*((M.*(L-a)+p i/8.*(rho1-670).*d.^2.*h.^2)./(M+pi/4.*(rho1-670).*d.^2.*h)-L+a).^2; J2=0.045+pi/48.*(rho2-670).*(d.^2.*h).*(.75*d.^2+h.^2)+pi/4.*(rho2-67 0).*d.^2.*h.*(L-a-h/2).^2+(M+pi/4.*(rho2-670).*d.^2.*h).*((M.*(L-a)+p i/8.*(rho2-670).*d.^2.*h.^2)./(M+pi/4.*(rho2-670).*d.^2.*h)-L+a).^2; % ******************************* %J5=-1/12*(3*670^2*h.^2*3.14^2.*R.^6+10*h.^4*670^2*3.14^2.*R.^4-12*h. ^3*0.274*670^2*3.14^2.*R.^4-3*R.^4*0.885*670.*h.*3.14-13*h.^3*0.885*6 70*3.14.*R.^2+24*0.274*0.885*h.^2*670*3.14.*R.^2-12*R.^2*0.045*670.*h .*3.14-12*0.274^2*0.885*670*h.*3.14.*R.^2+12*0.045*0.885)./(-0.885+67 0*h.*3.14.*R.^2); M1 = 0.885+(rho1 - 670)* 3.14* h.* R.^2; M2 = 0.885+(rho2 - 670)* 3.14* h.* R.^2; vi1=(6032./(M1./0.02835+70.4)-5.4).*0.447; vi2=(6032./(M2./0.02835+70.4)-5.4).*0.447; JJ1=(J1+0.885*0.564).*54674.7; JJ2=(J1+0.885*0.564).*54674.7; w1=45.3.*(JJ1/16000).^-0.30769; w2=45.3.*(JJ2/16000).^-0.30769; b1=-(vi1+40)./w1+(((vi1+40)./w1).^2+J1.*(0.145+M1)./(0.145.*M1)).^0.5 ; b2=-(vi2+40)./w2+(((vi2+40)./w2).^2+J2.*(0.145+M2)./(0.145.*M2)).^0.5 ; vmax1=((1+0.564).*(vi1+w1.*b1)-40.*(0.145./M1+0.145.*b1.^2./J1-0.564) )./(1+0.145./M1+0.145.*b1.^2./J1); vmax2=((1+0.564).*(vi2+w2.*b2)-40.*(0.145./M2+0.145.*b2.^2./J2-0.564) )./(1+0.145./M2+0.145.*b2.^2./J2); % drawing 1 figure(1); meshc(h,R,vmax1);

figure(2); %ma=max(max(vmax1)); %mi=min(min(vmax1)); C1=contour(h,R,vmax1,10); clabel(C1); % drawing 2 figure(3); meshc(h,R,vmax2); figure(4); %ma=max(max(vmax2)); %mi=min(min(vmax2)); C2=contour(h,R,vmax2,10); clabel(C2);
