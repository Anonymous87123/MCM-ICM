T1 F1 T2 F2 Problem Chosen

T3 F3 T4 F4

Summary

A traditional bathtub cannot be reheated by itself, so users have to add hot water from time to time. Our goal is to establish a model of the temperature of bath water in space and time. Then we are expected to propose an optimal strategy for users to keep the temperature even and close to initial temperature and decrease water consumption.

To simplify modeling process, we firstly assume there is no person in the bathtub. We regard the whole bathtub as a thermodynamic system and introduce heat transfer formulas.

We establish two sub-models: adding water constantly and discontinuously. As for the former sub-model, we define the mean temperature of bath water. Introducing Newton cooling formula, we determine the heat transfer capacity. After deriving the value of parameters, we deduce formulas to derive results and simulate the change of temperature field via CFD. As for the second sub-model, we define an iteration consisting of two process: heating and standby. According to energy conservation law, we obtain the relationship of time and total heat dissipating capacity. Then we determine the mass flow and the time of adding hot water. We also use CFD to simulate the temperature field in second sub-model.

In consideration of evaporation, we correct the results of sub-models referring to some scientists’ studies. We define two evaluation criteria and compare the two sub-models. Adding water constantly is found to keep the temperature of bath water even and avoid wasting too much water, so it is recommended by us.

Then we determine the influence of some factors: radiation heat transfer, the shape and volume of the tub, the shape/volume/temperature/motions of the person, the bubbles made from bubble bath additives. We focus on the influence of those factors to heat transfer and then conduct sensitivity analysis. The results indicate smaller bathtub with less surface area, lighter personal mass, less motions and more bubbles will decrease heat transfer and save water.

Based on our model analysis and conclusions, we propose the optimal strategy for the user in a bathtub and explain the reason of uneven temperature throughout the bathtub. In addition, we make improvement for applying our model in real life.

1  Introduction

1.1  Background

Bathing in a tub is a perfect choice for those who have been worn out after a long day’s working. A traditional bathtub is a simply water containment vessel without a secondary heating system or circulating jets. Thus the temperature of water in bathtub declines noticeably as time goes by, which will influent the experience of bathing. As a result, the bathing person needs to add a constant trickle of hot water from a faucet to reheat the bathing water. This way of bathing will result in waste of water because when the capacity of the bathtub is reached, excess water overflows the tub.

An optimal bathing strategy is required for the person in a bathtub to get comfortable bathing experience while reducing the waste of water.

1.2 Literature Review

Korean physicist Gi-Beum Kim analyzed heat loss through free surface of water contained in bathtub due to conduction and evaporation [1]. He derived a relational equation based on the basic theory of heat transfer to evaluate the performance of bath tubes. The major heat loss was found to be due to evaporation. Moreover, he found out that the speed of heat loss depends more on the humidity of the bathroom than the temperature of water contained in the bathtub. So, it is best to maintain the temperature of bathtub water to be between 41 to 45 ℃ and the humidity of bathroom to be 95%.

When it comes to convective heat transfer in bathtub, many studies can be referred to. Newton's law of cooling states that the rate of heat loss of a body is proportional to the difference in temperatures between the body and its surroundings while under the effects of a breeze [2]. Claude-Louis Navier and George Gabriel Stokes described the motion of viscous fluid substances with the Navier–Stokes equations. Those equations may be used to model the weather, ocean currents, water flow in a pipe and air flow around a wing [3].

In addition, some numerical simulation software are applied in solving and analyzing problems that involve fluid flows. For example, Computational Fluid Dynamics (CFD) is a common one used to perform the calculations required to simulate the interaction of liquids and gases with surfaces defined by boundary conditions [4].

1.3 Restatement of the Problem

We are required to establish a model to determine the change of water temperature in space and time. Then we are expected to propose the best strategy for the person in the bathtub to keep the water temperature close to initial temperature and even throughout the tub. Reduction of waste of water is also needed. In addition, we have to consider the impact of different conditions on our model, such as different shapes and volumes of the bathtub, etc.

In order to solve those problems, we will proceed as follows:

 Stating assumptions. By stating our assumptions, we will narrow the focus of our approach towards the problems and provide some insight into bathtub water temperature issues.

 Making notations. We will give some notations which are important for us to clarify our models.

 Presenting our model. In order to investigate the problem deeper, we divide our model into two sub-models. One is a steady convection heat transfer sub-model in which hot water is added constantly. The other one is an unsteady convection heat transfer sub-model where hot water is added discontinuously.

 Defining evaluation criteria and comparing sub-models. We define two main criteria to evaluate our model: the mean temperature of bath water and the amount of inflow water.

 Analysis of influencing factors. In term of the impact of different factors on our model, we take those into consideration: the shape and volume of the tub, the shape/volume/temperature of the person in the bathtub, the motions made by the person in the bathtub and adding a bubble bath additive initially.

 Model testing and sensitivity analysis. With the criteria defined before, we evaluate the reliability of our model and do the sensitivity analysis.

 Further discussion. We discuss about different ways to arrange inflow faucets. Then we improve our model to apply them in reality.

 Evaluating the model. We discuss about the strengths and weaknesses of our model.

2 Assumptions and Justification

To simplify the problem and make it convenient for us to simulate real-life conditions, we make the following basic assumptions, each of which is properly justified.

 The bath water is incompressible Non-Newtonian fluid. The incompressible Non-Newtonian fluid is the basis of Navier–Stokes equations which are introduced to simulate the flow of bath water.

 All the physical properties of bath water, bathtub and air are assumed to be stable. The change of those properties like specific heat, thermal conductivity and density is rather small according to some studies [5]. It is complicated and unnecessary to consider these little change so we ignore them.

 There is no internal heat source in the system consisting of bathtub, hot water and air. Before the person lies in the bathtub, no internal heat source exist except the system components. The circumstance where the person is in the bathtub will be investigated in our later discussion.

 We ignore radiative thermal exchange. According to Stefan- Boltzmann’s law, the radiative thermal exchange can be ignored when the temperature is low. Refer to industrial standard [6], the temperature in bathroom is lower than 100℃, so it is reasonable for us to make this assumption.

 The temperature of the adding hot water from the faucet is stable.

This hypothesis can be easily achieved in reality and will simplify our process of solving the problem.

3 Notations

Symbols Definition Unit    2 W / m K h Convection heat transfer coefficient    k W / m K Thermal conductivity    pc J / kg K Specific heat 2  kg / m Density  m Thickness t K ℃、 Temperature  s min h 、 、 Time q kg/s Mass flow m  W Heat transfer power s min h 、 、 T A period of time 3 V m L 、 Volume M m 、 kg Mass 2 m A Area 3 a b c m 、、 The size of a bathtub

where we define the main parameters while specific value of those parameters will be

given later.

4 Model Overview

In our basic model, we aim at three goals: keeping the temperature as even as possible, making it close to the initial temperature and decreasing the water consumption.

We start with the simple sub-model where hot water is added constantly. At first we introduce convection heat transfer control equations in rectangular coordinate system. Then we define the mean temperature of bath water. Afterwards, we introduce Newton cooling formula to determine heat transfer capacity. After deriving the value of parameters, we get calculating results via formula deduction and simulating results via CFD.

Secondly, we present the complicated sub-model in which hot water is added discontinuously. We define an iteration consisting of two process: heating and standby. As for heating process, we derive control equations and boundary conditions. As for standby process, considering energy conservation law, we deduce the relationship of total heat dissipating capacity and time.

Then we determine the time and amount of added hot water. After deriving the value of parameters, we get calculating results via formula deduction and simulating results via CFD.

At last, we define two criteria to evaluate those two ways of adding hot water. Then we propose optimal strategy for the user in a bathtub.

The whole modeling process can be shown as follows.

5  Sub-model I : Adding Water Continuously

We first establish the sub-model based on the condition that a person add water continuously to reheat the bathing water. Then we use Computational Fluid Dynamics (CFD) to simulate the change of water temperature in the bathtub. At last, we evaluate the model with the criteria which have been defined before.

5.1  Model Establishment

Since we try to keep the temperature of the hot water in bathtub to be even, we have to derive the amount of inflow water and the energy dissipated by the hot water into the air.

We derive the basic convection heat transfer control equations based on the former scientists’ achievement. Then, we define the mean temperature of bath water. Afterwards, we determine two types of heat transfer: the boundary heat transfer and the evaporation heat transfer. Combining thermodynamic formulas, we derive calculating results. Via Fluent software, we get simulation results.

5.1.1  Control Equations and Boundary Conditions

According to thermodynamics knowledge, we recall on basic convection heat transfer control equations in rectangular coordinate system. Those equations show the relationship of the temperature of the bathtub water in space.

We assume the hot water in the bathtub as a cube. Then we put it into a rectangular coordinate system. The length, width, and height of it is a , b and c .

In the basis of this, we introduce the following equations [5]:

 Continuity equation:

   u v w   + 0 （1）    x y z

where the first component is the change of fluid mass along the X-ray. The second component is the change of fluid mass along the Y-ray. And the third component is the change of fluid mass along the Z-ray. The sum of the change in mass along those three directions is zero.

 Moment differential equation (N-S equations):

       2 2 2 u u u p u u u         ( u v w ) ( ) （2）        2 2 2 x y z x x y z

       2 2 2 v v v p v v v         ( u v w ) ( ) （3）        2 2 2 x y z y x y z

       2 2 2 w w w p w w w         ( u v w ) g ( ) （4）        2 2 2 x y z z x y z

 Energy differential equation:

      2 2 2 t t t t t t       c u ( v + w ) ( ) （5） p       2 2 2 x y z x y z

where the left three components are convection terms while the right three components are conduction terms.

Having derived those equations, we give the boundary conditions listed as follows:

In the inflow water area

 t t （6） in

On the top surface of bath water, it transfer heat directly into air without heat conduction, so we have  t       h t t （7）  1  z The range of the area suitable for (7) is

     0 x b , 0 y a z , c （8） On the front surface in Fig.2, the water transfer heat firstly with bathtub inner surfaces and then the heat comes into air. Hence we have  t      h t t （9） 2 x  x The range of the area suitable for (9) is

     0 y a , 0 z c x , b （10）

On the right surface in Fig.2, the water also transfers heat firstly with bathtub inner surfaces and then the heat comes into air. The boundary condition here is  t      h t t （11） 3 y  y

The range of the area suitable for (11) is

     0 x b , 0 z c , y a （12）

5.1.2  Definition of the Mean Temperature

To simplify the modeling process, we assume the bathtub and hot water in it as a constant temperature system. Thus the heat is equal in value to the enthalpy difference between inflow water and outflow water.

We let the total heat dissipation to be Q and the mass flow of inflow q . Recalling on the heat balance equation, we have water to be m  q c t Q （13） m p

c is the specific heat of water which is constant according to our where p assumptions.

 is t The temperature difference of heat transfer   t t t （14） in out

int is the temperature of inflow water and t where is the temperature out of outflow water.

Although the temperature is different from area to area, the difference is rather small which has been proved by some scientists [8]. So we substitute the mean temperature in the bathtub with the mean value of the inflow water and outflow water. That is  t t  in out t （15） f 2 ft is the mean temperature in the bathtub. where

5.1.3  Determination of Heat Transfer Capacity

The real-life heat transfer process is a complicated mixed heat transfer problem which is shown as follows  1

  2 2

ft ft

 2

t t

As we can see in the above figure, the hot water in a bathtub has six radiating surfaces. On top surface transfers heat directly with air. The other surfaces transfer heat firstly with bathtub inner surfaces. Then the heat conducts through the bathtub and be transferred into air.

As for the top radiating surface, we derive the amount of radiating heat  with the aid of Newton cooling formula 1     （16） hA t t 1 f

In reality, the bathtub manufacturers tend to add some layers of thermal insulation materials to decrease the heat loss. So the boundary of a bathtub is made up by different material layers.

t t t w1 w2 w3

ft

1h

2h 1k 2k   t 1 2

Layers of thermal Outside the tub Inside the tub insulation materials

1k and k are thermal conductivity of the inner and outer layer In Fig.4, 2  and  are the thickness of the inner and of thermal insulation materials. 1 2 outer layer of thermal insulation materials. The heat transfer coefficient 1h . The heat transfer between the hot water and inner surface of the bathtub is h . t t t coefficient between air and outer surface of the bathtub is , and 2 w1 w2 w3 are the temperatures of three boundaries of the thermal insulation material layers.

According to heat conduction formula, we have  t t   = f （17） 2     1 1 1    1 2   A h k k h   1 1 2 2

Hence the total heat dissipation capacity is  （18） 1 2

5.2  Results

We first give the value of parameters based on others’ studies. Then we get the calculation results and simulating results via those data.

5.2.1  Determination of Parameters

After establishing the model, we have to determine the value of some important parameters.

As scholar Beum Kim points out, the optimal temperature for bath is between 41 and 45℃[1]. Meanwhile, according to Shimodozono’s study, 41℃ warm water bath is the perfect choice for individual health [2]. So it is reasonable for us to focus on 41℃~45℃. Because adding hot water continuously is a steady process, so the mean temperature of bath water is supposed to be constant. We value the temperature of inflow and outflow water with the maximum and minimum temperature respectively.

The values of all parameters needed are shown as follows:

Parameters Values Unit int ℃ 45 t ℃ 41 out ft ℃ 43 t ℃ 25 1 mm 0.64  mm 30 2  2 1h W / (m K) 10  2 1h W / (m K) 300  1k W / (m K) 0.19  2k W / (m K) 0.036  c J / (kg K) 4174 p  0.85 None 3  kg / m 992 M kg 320 3 m a b c * * 1.8*0.9*0.64 3 m V 0.32

5.2.2  Calculating Results

Putting the above value of parameters into the equations we derived before, we can get the some data as follows

Variables Values Unit 2 m 1A 1.05 2 m A 2.24 2  W 189.00 1  W 43.47 2  W 232.47 g/s q 0.014 m

In this table, we find the whole amount of radiating heat of the bathtub is 232.47 W. Based on industrial standards, the bathtub we chose has capacity of 320L. The temperature of inflow and outflow water is designed to be 45 and 41℃, the mass flow turns out to be 0.014 g/s (that is 0.84 kg/min ). Only this condition is satisfied can the temperature throughout the bathtub be kept as even as possible.

5.2.3  Simulating Results

It is quite unrealistic for us to compute the equations (1)-(5) because the N- S equation is coupled to the energy equation. In order to derive the temperature field, the velocity field is needed. Then introduce the boundary conditions, the temperature field is worked out. However, this method is so difficult that The Clay Mathematics Institute of Cambridge, Massachusetts (CMI) even sets prize to inspire people to solve it. So we have to employ Computational Fluid Dynamics (CFD) to simulate the temperature field based on those equations.

We will proceed as follows:

 Step 1: Via Gambit software, we establish the three-dimensional model and

divide meshes. Then we define the boundary type.

 Step 2: Using Fluent software to read and examine the meshes.

 Step 3: Defining solving model. We introduce Laminar Model to simulate the N-S equation and Energy Model to simulate the energy equation.

 Step 4: Defining the materials and correcting the corresponding physical property parameters.

 Step 5: Defining the boundary conditions.

 Step 6: Solving initialization.

 Step 7: Setting number of iterations.

 Step 8: The results are derived when the convergence conditions are met.

Applying the above steps in our first sub-model, the results turn out to be satisfying.

First of all, we divide meshes with the aid of Gambit software, which is shown in the following figure.

As is shown in Fig.5, we divide the hot water into 129600 meshes. Then we export the Mesh file then import it into Fluent and make corresponding settings. Afterwards, we begin to compute it by iteration. When the iteration is conducted for 379 times, the problem is nearly convergent. The curve of residual is shown in Fig.5.

Combining specific boundary conditions, we have the temperature field throughout the bathtub. In reality, there are various ways of water inflow and outflow. We design the water to flow into the bathtub from left side and out of the bathtub from the right side.

We take the temperature field of two surfaces as examples.

where ‘the bottom surface’ means the x-O-y surface while ‘the side surface’ is the y-O-z

surface of the water cube in Fig2. The temperature shown in the legend is presented in

Kelvin scale and the data should be expended to 100 times.

As we can see in the figures, the temperature in the bathtub is different from area to area, which decreases along the direction of water flow. However, the temperature fluctuates between 43 to 45 ℃(316-318 K). The highest temperature is that of inflow area because the adding water is the hottest. In addition, due to the stability of this model when a person adds hot water continually, the temperature of each area remains stable.

In conclusion, the temperature is not strictly even throughout the bathtub. It differs according to boundary conditions. However, the mean temperature of the whole water in the bathtub is stable.

By the way, because of the shortage of Fluent software in simulating small water flow, the temperature marked by different colors may differ a little. For example, in the legend, 44℃(317 K) corresponds with colors ranging from blue to orange. Actually, each color represents a different temperature  between 44- 45 ℃(317-318K). The changing tendency of colors strictly represents the changing tendency of the temperature.

6  Sub-model II: Adding Water Discontinuously

In order to establish the unsteady sub-model, we recall on the working principle of air conditioners. The heating performance of air conditions consist of two processes: heating and standby. After the user set a temperature, the air conditioner will begin to heat until the expected temperature is reached. Then it will go standby. When the temperature get below the expected temperature, the air conditioner begin to work again. As it works in this circle, the temperature remains the expected one.

Inspired by this, we divide the bathtub working into two processes: adding hot water until the expected temperature is reached, then keeping this condition for a while unless the temperature is lower than a specific value. Iterating this circle ceaselessly will ensure the temperature kept relatively stable.

6.1  Heating Model

6.1.1  Control Equations and Boundary Conditions

We focus on heating process at first. During this process, the hot water flows throughout the bathtub so we need to use N-S equation. We also have to introduce energy equation considering there is convective heat transfer in the flow.

Adding an unsteady term into basic N-S equation [3], we have

        2 2 2 u u u u p u u u          ( u v w ) ( ) （19）          2 2 2 x y z x x y z

The above equation is established along x-axis. The other two equations along y-axis and z-axis can be easily deduced so we omit them.

Similarly, we add unsteady term into energy equation and get

       2 2 2 t t t t t t t        c ( u v + w ) ( ) （20） p         2 2 2 x y z x y z

As for the boundary conditions, (6)-(12) are also suitable for this model. Except those, there are two other conditions:

  （21） when 0 t t ， f

    （22） when , t t 0 f min

t where is the minimum of mean temperature of bath water. min

6.1.2  Determination of Inflow Time and Amount

The bathtub can be simplified as a water containment vessel, so the amount of inflow and outflow is the equal in value. Hence the mass of the bath water in a bathtub is constant. That is

 （23） q q = q m in out

t  and the We let initial mean temperature of bath water to be f1 int . Frequently, the mean temperature will temperature of inflow water to be rise as hot water added, which leads the temperature of outflow to rise. We let t the final temperature of outflow to be . out2 t and t Both are functions of time. f1 out2       t f , t g （24） f out

We assume the bath water in bathtub as a control volume, so the energy stored in bathtub is the difference between the energy of inflow and outflow. This can be seen in the following figure.

The total heat dissipating capacity turns out to be

     Q out = d （25） T 1 We also derive that  t t         （26） t hA t t f  f 1 f     1 1 1    1 2   A h k k h   2 1 1 2 2

As the temperature of inflow water is higher than that of bath water in the bathtub, so the inflow will transfer heat into the bath water. The energy that bath water gets is equal in value to the enthalpy difference between inflow and outflow. Hence     mc t t （27） in p f 2 f1 Referring to formula (15), we have

 t t in out2 t f 2= （28） 2 The enthalpy difference between inflow and outflow is very the energy added into bath water. That is

     d Q q c t t （29） m p in out T 1 According to energy conservation principle, it follows that

  Q Q Q （30） in out

t , the heating process is When the temperature of bath water reaches f 2 stopped. Based on these above relationships, we derive the time of adding hot 1T and the corresponding amount of inflow q . water m

6.2  Standby Model

6.2.1  Process Analysis

After the heating process is finished, the mean temperature of bath water t . In standby process, it is assumed to be put in a space of which the is f 2 temperature is t and transfer heat into the space. Finally, the temperature f1t and the next iteration begins. During decreases to a specific temperature ft the standby process, the mean temperature of bath water is expressed by which is a function of time.

6.2.2  Calculation of Parameters

Throughout the whole process of cooling, the bath water transfer heat to the surroundings via convection or other ways. So that its internal energy is reduced as time goes by.

We take the whole bath water as a control volume and derive the energy balance equation:

dt       c V hA t t （31）  p  d The initial conditions are

  when =0 t t （32） ， f2

   when t t （33） ， 

According to before discussion and based on the surfaces of the control volume, we have

1   hA hA （34） 1     1 1 1    1 2   A h k k h   2 1 1 2 2

Then we integrating t over  in formula (31) and get   hA       c V    t t t t exp （35）     f 2    p

f1t , the time of standby process turns When the temperature decreases to out to be  pc V  t t   T ln f1 （36） 2  hA t t  f 2

The whole heat transfer capacity is     hA            Q c V t t 1 exp T （37）      p f 2 2  c V     p

6.3  Results

6.3.1  Determination of Parameters

One of our goals is to keep the temperature even throughout the bathtub. So we firstly have to determine the value of corresponding parameters such as the initial temperature of inflow and outflow.

According to the data we use in the first sub-model, the temperature in the bathtub ranges between 41 to 45 ℃. In this sub-model, we still set the int 445 ℃. In order to give the user temperature of inflow water to be comfortable experience, we set the change of the mean temperature less than t f1=42 1℃.thus the lowest mean temperature ℃.While the highest mean t f 2=43 at ℃. The expected mean temperature turns out to be temperature 442.5℃. In that way, the maximum change of the mean temperature is only 0.5℃.

The other parameters will change over time. The change value cannot be expressed by specific functions. So we need to analyze them according to our model. We first focus on the different temperatures during the heating process. The temperature of inflow remains stable. The temperature of outflow is stable for a while but begins to rise as hot water added. Meanwhile, the mean temperature also rises when the user adds hot water into the bathtub. The changing trend is shown as follows:

From the above picture, we can see that the mean temperature remains rising. After the added hot water arrives at the outflow side, the temperature of cT to represent the time between outflow begins to be influenced. We let adding hot water and the temperature of outflow beginning to rise. This process can be divided into two parts:

 When the time is shorter than cT , the temperature of outflow remains stable.

 When the time is longer than cT , the temperature of outflow begins to rise.

1T is Then we need to determine whether the time of adding hot water cT . Recalling on the first sub-model, we derive that the longer or shorter than temperature of inflow is 45℃ while the temperature of outflow is 41℃. Under such circumstance, the mean temperature turns out to remain 43℃.

We assume the area that added hot water covers is in stable state. If we  T T firstly suppose , the whole hot water is in stable state. This is alike the 1 c first sub-model where the mean temperature is 43℃.However the expected 1T is longer mean temperature is 42.5℃, higher than 43℃. That means before cT , the mean temperature has reached 42.5℃. So it is untrue for us to than   T T T T suppose . That is to say . Based on that, the initial temperature of 1 c 1 c outflow is equal to the value of the lowest mean temperature  t t f1=42 ℃.Still, it is convenient for us to compute. out The value of corresponding parameters is listed in the following table.

Parameters Value Unit

int ℃ 45 t ℃ 42 f1 t ℃ 43 f 2 at ℃ 42.5 ft ℃ 43 t ℃ 42 out

6.3.2  Calculating Results

q and the time of adding hot water The relationship between mass flow m 1T is    12522 Tq 232 T 1333008 0 （38） 1 m 1

Commonly, it will be better if the time of adding hot water is shorter.

T  3min According to some data from the Internet, we make . From formula 1 q 40.61kg/s. Putting these data into formulas (38)，we compute the mass flow m T 45914s (approximately 1.64h). (31)-(36), we find 2

Parameters Value Unit

1T 3 min T 1.64 h 2 T 101.4 min q 0.61 kg/s m where T is the total time of an iteration.

6.3.3  Simulating Results

Because this sub-model is a three-dimensional problem, it is hard for us to simulate it by Fluent. The hot water of constant temperature flows into the bathtub and is mixed with the bath water, causing fluid convection. The temperature field is symmetric so that we can simplify it as a two-dimensional problem. Although there are heat insulating materials around the bathtub, the heat transfer coefficient of forced convection of water is much larger than that of natural convection of air and water. So it is reasonable for us to simplify the problem as a two-dimensional one.

Considering the simulating by a computer takes too much time, we set the mass flow of the inflow water to be 0.04m/s. The residual curve of simulation is shown as follows.

The change of temperature field is present in the following four pictures.

（a）=1s

(b) t=2s                     (c) t=10s (d) t=20s                      (e) t=30s

where the picture (a) is the complete representation of the temperature field while

pictures (b)-(e) are partial representation of the temperature field. The temperature in the

legend is presented in Kelvin scale and the data should be expended to 100 times.

From the figure of the residual curve of simulation, we can find that the residual changes periodically and the change is small, which indicates the stability of the simulating results. Limited to time, we simulate situations which only last for 30s.

The four pictures in Fig.11 shows the change of temperature field after the hot water is added. Because the water flows in specific velocity, it influences mainly the area in front of it. However, the area beside it is hardly affected and remains the primary temperature. As more hot water is added, the convective surface becomes larger and moves towards the exit. We can also find there is an obvious interface between the added hot water and the initial bath water. That indicates the difference of temperature of added water and bath water is supposed to be small.

In the standby process, the bath water is put in a space, cooling freely. Recalling on our calculating results before, it takes about 1.64h for the temperature of the whole bath water to decrease by 1℃. Since it is impossible for out computer to simulate the change over such long time, we shrink the size of bathtub. The boundary conditions remain unchanged. Shrinking the size to 1/100, we get the temperature field as following.

(a) t=3s

(b) t=15s

Compared to initial bathtub, although the size changes, the heat transfer remains the same. As is shown in the picture (a), when the time is short, the change of temperature of middle areas is small. That is because the main convection happens in boundary areas. As time goes by, the cooler areas spread towards the middle area, as is presented in picture (b). So that the temperature of other areas besides the middle begins to change. However, the change is small, most of which is less than 2℃. The lowest temperature occurs in four corners, being 40℃ approximately. After the mean temperature is lower than the expected value, the bathtub user needs to add hot water into the bathtub to reheat the water. This simulating result corresponds to the calculating result we derived before.

6.4  Conclusion

According to calculation and simulation, we basically determine the time of an iteration. The heating process lasts for 3 min while the mass flow is 0.61kg/s. the standby process lasts for 1.64h while the mean temperature decreases by 1℃. By simulating the two situations, we proof the validity of our model and explain why it is so slow for the temperature of bath water to decrease.

7  Correction and Contrast of Sub-Models

After establishing two basic sub-models, we have to correct them in consideration of evaporation heat transfer. Then we define two evaluation criteria to compare the two sub-models in order to determine the optimal bath strategy.

7.1  Correction with Evaporation Heat Transfer

Someone may confuse about the above results: why the mass flow in the first sub-model is so small? Why the standby time is so long? Actually, the above two sub-models are based on ideal conditions without consideration of the change of boundary conditions, the motions made by the person in bathtub and the evaporation of bath water, etc. The influence of personal motions will be discussed later. Here we introducing the evaporation of bath water to correct sub-models.

7.1.1  Correction Principle

According to Gi-Beum Kim’s studies, the heat transfer capacity is relative not only with boundary mixed heat transfer, but also with evaporation heat transfer. More importantly, the major heat loss is found to be due to evaporation [1]. In order to clarify our correction process more clearly, we briefly introduce his achievement and findings.

The evaporation heat transfer is related to the temperature of the bath water, the air humidity of the bathroom, the total thermal resistance, material properties and so on. The relationship is given as follows:

 Mc t  p   EA L dt （39）   f  t t kA t 0  0

where k is the thermal resistance. A is the area of heat transfer. L is the latent heat of evaporation.  is the thickness of materials. fA is the area of free surface. E is the evaporation capacity.

The experimental formula that Gi-Beum Kim gives is    0.88   0.88      t /22.009 E 0.37 0.0041 v 0.0041 e 0.004 1 （40）

where v is the mean temperature of air and  is the air humidity.

The experimental formula for the latent heat of evaporation L is   t   0.174 L t 273.15 3.484 （41）

 and the convection We let the evaporation heat transfer capacity to be s . Then the total heat loss is heat transfer capacity to be q   = （42） t s q

Plugging the above formulas into sub-models, we obtain the precise results after being corrected.

7.1.2  Correction Results

Considering the model established by Gi-Beum Kim is similar with ours, so we can refer to his results to correct our sub-models. In his experiment, the bathtub has a capacity of 250L, which is close to the capacity of our bathtub. When the air humidity remains stable, he finds the change of mean temperature over time as follows [1]:

As is vividly shown in Fig.14, the air humidity affects the mean temperature of bath water heavily. The more air humidity is, the smaller evaporation capacity will be, so that the main heat transfer comes from boundary convection heat transfer.

Commonly, the air humidity is high in bathroom but the air temperature is low. According to Fig.14 , we assume it takes 0.75 h (45 min ) for the temperature of bath water to decrease by 1℃.

Since we have obtained the convection capacity in before calculation, we can compute the evaporation capacity based on energy conservation. Then the total heat transfer capacity can be derived and the correction is to be conduct. The corrected results in listed in the following table.

Parameters Value Unit  261.24 W s  232.47 W q  522.71 W t q 0.03 kg/s m 1 q kg/s 0.63 m 2 1T 3 min T 45 min 2 T 48 min Let us analyze the corrected results. The mean temperature in the first sub- model mainly depends on convective heat transfer capacity because it is in steady state. As for the second sub-model, the convection heat transfer hardly affects the heating process because the specific heat is large. The standby process is similar with the first sub-model, so it is affected by evaporation heat transfer.

7.2  Contrast of Two Sub-Models

Firstly we define two evaluation criteria. Then we contrast the two sub- models via these two criteria. Thus we can derive the best strategy for the person in the bathtub to adopt.

7.2.1  Evaluation Criteria

We aim at three goals: keeping the temperature as even as possible, making it close to the initial temperature and decreasing the water consumption. Considering that, we define two criteria to evaluate the sub-models:

 The average temperature of the water in bathtub. It is difficult to keep the temperature strictly even throughout the bathtub because convective heat transfer is an unsteady process. However, the difference in temperature of diverse area is rather small so we can use the average temperature to substitute the temperature of whole bathtub. With the aid of Gi-Beum Kim’s study, the optimal temperature ranges from 41 to 45℃[1].

 Water consumption during a bath. According to data from the internet, the water consumption of bathing in a bathtub is four times as many as bathing with a shower [7]. So it is necessary for the bathtub users to decrease water consumption, not only for lower cost of bath but also for the responsibility to the environment.

7.2.2  Determination of Water Consumption

In the before discussion, we have derived the mass flow in the two sub- models. Giving the bath time, it is easy to compute the total water consumption. Considering the bathtub is filled with same water capacity, the difference of water consumption is added hot water. So we only have to calculate the amount of added water in order to compare the sub-models.

bT . Since the hot water is added consistently, We let the bath time to be the mass flow is a constant over time. So the total amount of added water is  m T q （43） 1 b m 1

As for the second sub-model, the hot water is only added during the heating process. So the mass flow in heating process is constant while that in standby process is zero. Then we have the total amount of added water in second sub-model

  T   b m 1 T q （44）   2 1 m 2 T  

bT may not where we use Gauss integral function. Because the bath time be any multiple of the iteration time T , we have to round the figure. No matter what period adding hot water reaches, we assume it as a complete iteration so that the actual iteration times need to be plus one.

bT  48min To simplify our calculation, we set the bath time to be , which is very an iteration time. Thus we find the amount of added water consumption m  86.4 kg in the first sub-model to be , while that in the second sub-model to 1 m  113.4 kg be . 2

7.2.3  Conclusion

In terms of the mean temperature of bath water, the temperature of the first sub-model is 43℃ while that of the second sub-model ranges from 42 to 43℃. According to common sense, a person can hardly feel 1℃change of temperature. So both strategies of adding water are optimal for the person in a bathtub.

As the water consumption of the first sub-model is 84.6 kg, while that of the second sub-model is 113.4 kg. Considering our goal to decrease water consumption, it is obviously wise to choose adding hot water continually instead of adding water discontinuously.

In conclusion, we recommend the person in the bathtub to add hot water continually with mass flow being 0.03 kg/s. This strategy can not only ensure comfortable bath experience but also avoid wasting too much water.

8  Model Analysis and Sensitivity Analysis

The results of the model we establish before correspond with literature to huge extent. However, the model is based on an ideal situation that there is no person in bathtub. Still, the bathtub in our model is simplified as a cube.

In reality, things are quite different. The bathtub can be designed into various shapes and volumes and there is undoubtedly one person or more in the bathtub. The person in bathtub may have various shapes, volume and temperature. He / She is likely to make mangy motions during bath time. In addition, people tend to use a bubble bath additive while initially filling the bathtub to assist in cleansing, which may affect our model’s results as well.

So here we will conduct sensitivity analysis to determine the extent to which our model depends upon those influencing factors

8.1  The Influence of Different Bathtubs

Definitely, the difference in shape and volume of the tub affects the convection heat transfer. Examining the relationship between them can help people choose optimal bathtubs.

8.1.1  Different Volumes of Bathtubs

In reality, a cup of water will be cooled down rapidly. However, it takes quite long time for a bucket of water to become cool. That is because their volume is different and the specific heat of water is very large. So that the decrease of temperature is not obvious if the volume of water is huge. That also explains why it takes 45 min for 320 L water to be cooled by 1℃.

In order to examine the influence of volume, we analyze our sub-models by conducting sensitivity Analysis to them.

  5% 8% We assume the initial volume to be 280 L and change it by , ,   12% 15% and . With the aid of sub-models we established before, the variation of some parameters turns out to be as follows

 2A T q q V 1A 2 m 1 m 2 q

-15.00% -5.06% -9.31% -12.67% -2.67% -14.14% -5.80%

-12.00% -4.04% -7.43% -10.09% -2.13% -11.31% -4.63%

-8.00% -2.68% -4.94% -6.68% -1.41% -7.54% -3.07%

-5.00% -1.67% -3.08% -4.16% -0.88% -4.71% -1.92%

-2.00% -0.67% -1.23% -1.65% -0.35% -1.89% -0.76%

0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00%

2.00% 0.67% 1.22% 1.64% 0.35% 1.89% 0.76%

5.00% 1.66% 3.05% 4.09% 0.87% 4.71% 1.90%

8.00% 2.65% 4.87% 6.51% 1.40% 7.54% 3.03%

12.00% 3.96% 7.28% 9.71% 2.09% 11.31% 4.54%

15.00% 4.94% 9.08% 12.08% 2.60% 14.14% 5.66% To show the relationship of different parameters and volume, we put the data in the following pictures.

 over volume T and

2 q

q q

and over volume m 1 m 2

From the above figures, we can find when the bathtub volume is small, the volume of other parameters is small too. For example, as the volume decreases, the heat loss becomes less so that the mass flow of added water decreases correspondingly in the two sub-models.

In conclusion, smaller bathtub is a better choice for people in terms of saving more water resource. This can not only decrease the initial water consumption to fill the bathtub but also avoid adding too much hot water afterwards. Of course, it is unwise for taller or fatter people to choose a small bathtub.

8.1.2  Different Shapes of Bathtubs

When the volume is constant, different shapes of bathtub mainly affect surface area of bath water, influencing heat transfer consequently. So we convert the change of shapes into that of surface area.

Usually, there are bathtubs in shapes of round, ellipse, rectangular, heart- shaped, rounded rectangle and so on [18]. We let the perimeter of the section of the bathtub to be C . The area of top surface and other surfaces is 1A and A . 2 The parameters of different shapes of bathtubs are listed as follows.

1A A Shapes Sketches 2

  2 V A  2r Round 1 A 1

2V a     b A ab Rectangle 1 A 1

4V  A 2 a Square 1 A 1

V C Rounded  A   2r ab 1 A rectangle 1

Recalling on the average inequality, we have

  2 A     2 A 4 A 2 a 1 （45）   1 1  a  So the perimeter of rectangle is the largest while that of square being smaller and that of circle being the smallest. We assume the volume to be 280L A  2 1.05m and the area of the top surface . The value of other parameters are 1 shown in the following table.

 A q q 2T Shapes Size/m 2 m1 m2 q r  0.578 Round 2.02 0.0293 0.5565 227.7 39.76   a 1.5, b 0.7 Rectangle I 2.22 0.0295 0.5568 231.5 39.45 1 1   a 1.7, b 0.62 Rectangle II 2.29 0.0296 0.5569 232.8 39.34 2 2 a  1.025 Square 2.14 0.0294 0.5567 230.0 39.57    a 1.2, b 0.7, r 0.05 Rounded rectangle 2.15 0.0294 0.5567 230.2 39.56

As the rounded rectangle is the most commonly shape of bathtubs, we choose it as the basic bathtub. Comparing it with other shapes, we derive the variation as follows.

Rounded rectangle Shapes Rectangle I Rectangle II Square Round

A 0.00% 3.26% 6.39% -0.47% -6.05% 2  0.00% 0.58% 1.14% -0.08% -1.08% q q 0.00% 0.34% 0.68% 0.00% -0.34% m1 q 0.00% 0.02% 0.04% 0.00% -0.04% m2 2T 0.00% -0.27% -0.53% 0.04% 0.51%

and 2T of tubs in different shapes

q 1A and From the above data, we conclude when the area of top surface volume V are given, the area of side surface A in round bathtub is the smallest 2 among different shapes. So the heat loss of bathtubs in round shape is the smallest. On the contrary, the area of side surface and heat loss of rectangle bathtubs are a b / the largest. As for rectangle bathtubs, if the ratio of length to width becomes lager, the area of side surface will consequently increase, leading to the rise of heat loss. So that square bathtub is better than rectangle one in consideration of heat loss.

In conclusion, with regard to heat transfer, the round bathtub is best to choose while the square and rounded rectangle bathtub is less recommended. The rectangle bathtub is the least to choose.

In reality, however, the rounded rectangle bathtubs are more common instead of round bathtubs. That is because of the shape of human body and space of the bathroom. A round bathtub will cover more area in a bathroom.

8.2  The Influence of Person in Bathtub

To some extent, our model may be affected by the difference of people in a bathtub and motions they make. So it is necessary for us to investigate their influence further.

In consideration of our goal to avoid wasting too much water, we assume the bathtub is not completely filled with hot water before the person comes into it.

8.2.1  When the Person Remains Static in a Bathtub

Recalling on our biologic knowledge, human beings are warm-blooded animals whose average temperature remains around 37℃. The change of 1℃ of average temperature means lot to a person. For example, when the temperature rises to 38℃, the person is diagnosed to have a fever. As for skin of human beings, it is made up of three layers: epidermal, dermis and hypodermis. The epidermal layer contacts directly to surroundings, so its temperature is close to the temperature of the surroundings. However, the temperature inside skins commonly remain around 37℃.

To simplify the problem, we firstly assume the person in the bathtub remains stable without any motions. Under this circumstance, the skin transfer heat with bath water. According to convection heat transfer formula, we have  t t f p  = （46） p    1 1  3   A k h   3 3 3  is the heat transfer capacity and A is the average area of where p 3  is the thickness of skin. 3h is the convection heat transfer human skin. 3 pt is the average 3k  is the thermal conductivity of skin. coefficient. temperature of human beings, which is commonly 37℃.

pt

ft

where the orange curve represents the temperature trend.

The total heat transfer capacity is   = （47） t s q p

Because the person remains static, so the value of is unchanged. As the bathtub is not completely full of hot water, the surface area of bath water will be creased after the person comes into the tub. We let the mass of the person to  and the volume to be m , the density of the person to be V . It is easy be 3 3 3 . V after knowing m and to calculate 3 3 3 With the aid of formulas we get on the above, we can assume the volume to change and then correct it with surface area. Through this we can get the corrected results.

8.2.2  When the Person Moves in a Bathtub

Theoretically, the motions made by the person obviously affect heat transfer. When the person moves, the hot water will be stirred. So that the natural convection transfers into forced convection where the convection heat transfer coefficient will rise a lot. Meanwhile, the motion of bath water will increase the surface area of convection, leading to more heat loss. According to heat transfer theory, the influence of motion caused by the person can be determined.

8.2.3  Results Analysis and Sensitivity Analysis

Professor Anand Mani sums up other scientists’ research outcome in his essay [10]. We choose some values from the data in his essay which are listed as follows.

Parameters Range Value Unit 2 A m 1.5~2 [11] 1.8 3  mm 2~3 [12] 2.5 3    pc J/ kg K 3300,3800,4200,3300 [13-16] 3800 3    W/ m K 3k 0.3,0.21,0.5*,0.543 [17] 0.3  3 kg / m 1040,1050,1000,1100 1050 3

* Combined Conductivity for dermal and epidermal layers.

The heat transfer coefficient differs a lot in natural convection and forced convection. We list those coefficients as follows.

Types Coefficients Ranges /Values Unit

Coefficient of air 1~10

Coefficient of water 200~1000 Natural    2 1h W/ m K 10 convection 2h 300 3h 300

Coefficient of air 20~100

Coefficient of water 1000~1500 Forced    2 W/ m K 1h 60 convection 2h 1100 3h 1100

Putting those data into the sub-models, we derive the following results.

Parameters Static Moving Unit  261.24 261.24 W s  238.95 1222.4 W q  925.71 1168.5 W p  1425.9 2652.1 W t q 0.0854 0.1588 kg/s m 1 q kg/s 0.6314 0.7293 m 2 1T 3 3 min T 13.63 7.33 min 2 T 16.63 10.33 min

The sub-models are heavily affected in consideration of person. The mass flow rises because more hot water is needed. The time of iteration becomes shorter, wasting more water resource. When the person moves in the bathtub, his /her motions will lead to forced convection. This will decrease the thermal resistance so that more heat will be lost. In conclusion, the more frequent and fiercer the motions are, the more hot water will be wasted.

Then we conduct sensitivity analysis to determine the relationship between the convection heat transfer coefficient and individual motions. Still, the relationship of volume of the person and the convection heat transfer area.

At first, we assume the personal mass to be 60 kg and the volume of the     2% 5% 8% 12% bathtub to be 320 L. Changing the mass by , , , and  15% , we can get the variation as follows.

 m 2T q q 3 q m 1 m 2 -15.00% -0.22% 0.18% -0.18% -0.03% -12.00% -0.17% 0.14% -0.14% -0.03% -8.00% -0.12% 0.09% -0.09% -0.02% -5.00% -0.07% 0.06% -0.06% -0.01% -2.00% -0.03% 0.02% -0.02% 0.00% 0.00% 0.00% 0.00% 0.00% 0.00% 2.00% 0.03% -0.02% 0.02% 0.00% 5.00% 0.07% -0.06% 0.06% 0.01% 8.00% 0.12% -0.09% 0.09% 0.02% 12.00% 0.17% -0.14% 0.14% 0.03% 15.00% 0.22% -0.18% 0.18% 0.03% From the above figure, we find the heat transfer capacity and mass flow of added water are both in proportion to the personal mass. That is to say, those two parameters are positively correlated to personal volume while the volume of added water is negatively correlated to personal volume.

To show the relationship more vividly, we draw the variations in the following figure.

and 2T

q

q q

and m 1 m 2

We can find the change of those parameters to be relatively small, which indicates the personal volume affects minutely to the model. However, we ignore one factor: the contact area of the person and bath water. In order to conduct sensitivity analyze, we assume the contact area as a constant. Due to the limit of time, we do not investigate its influence further. But we deduce the area is positively correlated to personal volume.

In conclusion, if the personal mas and volume are small, the water consumption is small.

At last, we analyze the influence of personal motions. Because the motions   2% 5% mainly affect convection heat transfer coefficient, we change it by , ,    8% 12% 15% , and . The results is listed as follows.

 3h 2T q q m 1 m 2 q

-15.00% -8.21% 8.00% -7.40% -2.15%

-12.00% -6.55% 6.27% -5.90% -1.71%

-8.00% -4.35% 4.08% -3.92% -1.14%

-5.00% -2.71% 2.51% -2.44% -0.71%

-2.00% -1.08% 0.98% -0.98% -0.28%

0.00% 0.00% 0.00% 0.00% 0.00%

2.00% 1.08% -0.96% 0.97% 0.28%

5.00% 2.69% -2.37% 2.42% 0.70%

8.00% 4.29% -3.73% 3.87% 1.12%

12.00% 6.42% -5.47% 5.79% 1.68%

15.00% 8.01% -6.74% 7.22% 2.10%

From the above data, we conclude the convection heat transfer coefficient affects the model heavily, especially for the first sub-model. This indicates the stability of the second sub-model is better with less change based on the surroundings. Like before, we list the variation of parameters as follows.

and 2T

q

q q

and m 1 m 2

We find the mass flow in two sub-models is positively correlated to heat transfer coefficient. The mass flow of added water in the first sub-model is affected minutely by the change of heat transfer coefficient. However, the mass flow in the second sub-model is affected heavily by the change. So we deduce if the person in a bathtub moves more fiercely, he/she will have to add more hot water to reheat the bath water.

8.3  The Influence of Bubble Bath Additives

According to thermodynamics knowledge, a factor can influence heat transfer in two opposite ways: adding heat transfer or decreasing heat transfer. The bubbles made by a bubble bath additive often float on the bath water.

Because the thermal conductivity of bubbles is little, those bubbles can be seen as a thermal insulation layer added between bath water and air. This layer restricts the direct convection of air and bath water so it brings about heat preservation. That indicates we can add bubble bath additives to decrease the amount of added hot water.

, the thermal conductivity We let the thickness of layer of bubbles to be 4 4k , the convection heat transfer coefficient of the top surface of bubbles to be h of bubbles and air to be and that of the bottom of bubbles and bath water 4L h to be . This analysis can be better understood by the following figure. 4H

Here we analyze from two points: on one hand, the bubbles restrict the evaporation heat transfer. We assume the evaporation heat transfer decrease to 10%. On the other hand, adding bubbles adds a heat transfer process between the air and hot water. Recalling on our before analysis, the top surface is the main surface to lose heat. So covering bubbles on the top surface will decrease the heat loss heavily.

Based on thermodynamic knowledge, the convection heat transfer capacity is  t t   = f （48） 4    1 1 1   4   A h k h   4 4 L 4 4 H

Then we correct the heat transfer capacity and then put corrected results into sub-models. We derive the value of parameters listed in the following table.

Parameters Value Unit ft ℃ 43 t ℃ 25 s  23.2 W 2 4A m 1.05  0.03 m 2    2 h W/ m K 300,1100 4L    2 h W/ m K 10,60 4H    4k W/ m K 0.3

In consideration of the person in bathtub, we correct the above data. To show the influence of bubbles vividly, we compare the results with and without adding bubbles.

Natural convection Forced convection Parameters Change Change Adding No Adding No bubbles bubbles bubbles bubbles  1061.8 1164.7 8.83% 1376.7 2390.9 42.42% q 2T 17.87 13.63 -31.11% 13.86 7.33 -89.09% q 0.065 0.085 23.53% 0.084 0.159 47.17% m 1 q 0.604 0.631 4.28% 0.630 0.729 13.58% m 2

From the above table, we find bubbles affect heat transfer heavily. They can not only decrease the heat transfer capacity, but also save hot water. Comparing the two sub-models, the change of parameters in the second sub- model is larger. That indicates the second sub-model is more sensitive to bubbles.

In conclusion, adding bubble bath additives can slow down the process of bath water becoming cooler and avoid wasting too much water.

8.4  The Influence of Radiation Heat Transfer

In our before discussion, we ignore the influence of radiation heat transfer because we assume it to be very small to simplify our model. Now it is time for us to investigate the validity of this assumption.

According to Stefan-Boltzmann law, we have   4 4       t 273.15 t 273.15     AC f   （49）     0 1 0  100   100     

Because only the top surface of bath water contacts directly with air, so we just take the top surface into consideration. Putting the parameters into formula  70W (49), we derive the approximate value . In reality, when a person takes bath in a bathtub, the total heat transfer capacity is 2652W. the variation of radiation heat transfer is merely 2.64% so that it can be ignored. That indicates the rationality of our assumption.

8.5  Conclusion

After having corrected our model and determined the influence of possible influencing factors, we finally propose our strategy for the user of bathtub to adopt. From point of

q T Situation Sub-model Water consumption* m 2

I 0.014 85.18 Ideal 1.64h II 0.61 109.8 I 0.03 86.40 Evaporation 45min II 0.63 113.4 I 0.029 74.40 Shape 39.76min II 0.557 100.3 I 0.0854 85.21 Static 13.63min II 0.6314 113.6 I 0.1588 98.42 Moving 7.33min II 0.7293 131.3 I 0.084 84.97 Bubbles 13.86min II 0.630 113.4

* water consumption is the amount of water during an iteration.

9  Further Discussion

In this part, we will focus on different distribution of inflow faucets. Then we discuss about the real-life application of our model.

9.1  Different Distribution of Inflow Faucets

In our before discussion, we assume there being just one entrance of inflow.

From the simulating outcome, we find the temperature of bath water is hardly even. So we come up with the idea of adding more entrances.

The simulation turns out to be as follows

(a) One entrance                (b) Two entrance

(c) Five entrance        (d) The whole side as entrance

From the above figure, the more the entrances are, the evener the temperature will be. Recalling on the before simulation outcome, when there is only one entrance for inflow, the temperature of corners is quietly lower than the middle area.

In conclusion, if we design more entrances, it will be easier to realize the goal to keep temperature even throughout the bathtub.

9.2  Model Application

Our before discussion is based on ideal assumptions. In reality, we have to make some corrections and improvement.

 Adding hot water continually with the mass flow of 0.16 kg/s. This way can ensure even mean temperature throughout the bathtub and waste less water.

 The manufacturers can design an intelligent control system to monitor the temperature so that users can get more enjoyable bath experience.

 We recommend users to add bubble additives to slow down the water being cooler and help cleanse. The additives with lower thermal conductivity are optimal.

 The study method of our establishing model can be applied in other area relative to convection heat transfer, such as air conditioners.

10  Strength and Weakness

10.1  Strength

 We analyze the problem based on thermodynamic formulas and laws, so that the model we established is of great validity.

 Our model is fairly robust due to our careful corrections in consideration of real-life situations and detailed sensitivity analysis.

 Via Fluent software, we simulate the time field of different areas throughout the bathtub. The outcome is vivid for us to understand the changing process.

 We come up with various criteria to compare different situations, like water consumption and the time of adding hot water. Hence an overall comparison can be made according to these criteria.

 Besides common factors, we still consider other factors, such as evaporation and radiation heat transfer. The evaporation turns out to be the main reason of heat loss, which corresponds with other scientist’s experimental outcome.

10.2  Weakness

 Having knowing the range of some parameters from others’ essays, we choose a value from them to apply in our model. Those values may not be reasonable in reality.

 Although we investigate a lot in the influence of personal motions, they are so complicated that need to be studied further.

 Limited to time, we do not conduct sensitivity analysis for the influence of personal surface area.

Report

Suggestions

In order to enjoy a comfortable bath with even temperature of bath water and without wasting too much water, we propose the following suggestions.

Adding hot water consistently

Using smaller bathtub if possible

Decreasing motions during bath

Using bubble bath additives

Decreasing motions during bath Arranging more faucets of inflow

From simulation results of

real-life situations, we find it takes

a period of time for the inflow hot

water to spread throughout the

bathtub. During this process, the

bath water continues transferring

heat into air, bathtub and the

person in bathtub. The difference

between heat transfer capacity

makes the temperature of various

areas to be different. So that it is

difficult to get an evenly main-

tained temperature throughout the

bath water.
