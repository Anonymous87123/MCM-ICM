Problem Chosen 2022

MCM/ICM

Summary Sheet

Summary

In the time trial, many factors will aﬀect the rider’s performance. To help riders achieve better results, we need to establish a model that can comprehensively consider many factors and provide a reasonable power distribution plan at diﬀerent course positions.

First, we established a Rider Ability Evaluation Model and deﬁned the rider’s power proﬁle. A power-time scatterplot is drawn from the relationship between power and the maximum duration at this power level. Then four diﬀerent exercise intensity domains were divided according to the power-time relationship. We selected the 3P-CP Model to ﬁt the scatter plot, and obtained the rider’s power-time curve, thereby obtaining the three important rider ability indicators: Maximum instantaneous power (Pmax), critical power (CP) and anaerobic energy reserve (W ′). We take multiple sets of data to evaluate the ﬁtting results. After calculation, the ﬁtting degree is stable at about 0.86, indicating good ﬁtting eﬀect.

Secondly, we built an External Factor Analysis Model to identify the potential impact of external conditions. We quantitatively evaluated the inﬂuence of weather and environment from two aspects, namely road rolling resistance and wind resistance. After that, we select actual courses for veriﬁcation and the degree of compliance exceeds 90%.

Thirdly, Power Overall Planning Model is established. After the course segmentation and dynamics analysis, the average power (AP) and normalized power (NP) are proposed, and the constraints of the power of each track are obtained, so that the problem can be transformed into a multivariate nonlinear programming problem with total time t as objective function. We use gradient descent method to gradually approach the local minimum of t and give a power distribution plan for each road section. The deviation between our results and the actual is +-10%, indicating a good agreement with the actual.

Next, we apply the Rider Apability Evaluation Model to diﬀerent types of riders and courses, and obtained the riders output power, speed at a speciﬁc position and minimum time to complete the race.

Afterwards, we performed sensitivity analysis of the model, analyzing its robustness to weather and environment and rider performance. The failure probabilities of air temperature, air pressure, altitude, and wind resistance are 0.18%, 3.97%, 0.18%, and 4.22% respectively. Air pressure and wind resistance are sensitive factors, while temperature and altitude are non-sensitive factors. We calculate the probability of failure caused by the deviation from power plan, and give the priority order of strategy execution: slope > corner > ﬂat.

Finally, we extend the model to a Team Time-Trial Power Distribution Model, and obtain the extended multivariate nonlinear programming problem. Our suggestion is: the ﬁrst 45% of the course are led by two riders with strong explosive strength, the last 15% are led by the rider with the strongest stamina, and the remaining 4 riders take turns leading in the middle.

1 Introduction

1.1 Background

"Higher, faster, stronger - more united" is the Olympic motto and the goal of every athlete. In order to show the spirit of hard work and enterprising, athletes try to achieve better results. However, many factors aﬀect a rider’s performance, including the type of event, the course and the ability of the riders. In order to help these riders to respond to diﬀerent situations and achieve better results, we are required to formulate reasonable plans.

1.2 Restatement of the Problem

1) In order to determine the relationship between the riders position on the course and the power the rider applies, we set up a model which can be applied to any type of riders and race courses.

2) Deﬁne the power proﬁles of 2 types of riders of diﬀerent genders.

3) Apply our model to various time trial courses, and design our own time trial course.

4) Determine the sensitivity of our model to weather and environment and deviations from target power.

5) Extend our model, use it for a team.

1.3 Our Work

• For question 1), we intend to propose a model to measure the diﬀerence between diﬀerent types of riders, segment the course and generalize it into several characteristics.

We can calculate the parameters by ﬁtting a curve with discrete points. We need to do dynamic analysis on diﬀerent courses. For the overall planning of power distribution, multivariate nonlinear programming method can be tried. Finally, the best plan of power distribution is obtained after the information of the rider, environment, track, etc.

is known.

• For question 2), which is the model application to diﬀerent types of riders. We measure the ability values of diﬀerent riders in various aspects and substitute them into the model.

• For problem 3), which is the model application to diﬀerent courses, we need to control the variables to derive three diﬀerent power distributions using the same player and three sets of known course information.

• For questions 4) and 5), both questions are sensitivity analyses. We calculate the failure probabilities of diﬀerent variables and measure the sensitivity based on the idea of simulating importance sampling with subsets.

• For problem 6), we need to ﬁnd the similarities and diﬀerences between the team race and the individual race, and discuss how to give an optimal team strategy.

2 Assumptions and Justiﬁcation

In order to make better use of the data about both the riders and courses, and improve the validity of the model, we propose the following reasonable assumptions:

• Safety comes ﬁrst.The physical health and safety of athletes is the premise of everything.

We assume that riders have speed, energy and rage upper limits to prevent our model from putting them in a dangerous overdraft state.

• The inﬂuence of secondary factors is negligible. Since race results are aﬀected by so many factors while our model mainly focuses on diﬀerent types of riders, it is necessary to ignore the inﬂuence from secondary factors such as riders’ equipment.

• We divide the whole course into n sections, and each section belongs to one of the following four types: ﬂat, uphill, downhill, and sharp corner.The standard of segmen- tation is: when the continuous change of slope does not exceed 1%, it is deﬁned as the same segment of ﬂat ground; when the radius of curvature exceeds 40m, it is considered as a straight road; when it is less than 40m and the radius changes not more than 5m, it is deﬁned as the same corner.

• All participants have sportsmanship, maintain the fairness of the game, and can play their best in the game.

3 Notations

Symbols

Description Value/Unit

e e = 2.178 Basis of the natural logarithm 8.31Jmol−1K−1 R Gas constant g=9.8m/s2 g Gravitational acceleration

CP watt Critical power

MMP watt Mean maximal power output W ′ J Anaerobic capacity

ρ g/L Air density

kr Rolling resistance coeﬃcient

cd Wind resistance coeﬃcient m2 S Windward area

4 Model Preparation

To make our paper clearer and easier to understand, we will explain some nouns, data types, and data sources in this section.

4.1 Explanation of Nouns

• Normalized power output(NP) It takes the diﬀerence between steady and wave workouts into account. NP is better at quantifying the physiological "cost" of the harder "feeling" of variable eﬀort. For a highly variable workout, NP can be much higher than average power(AP), when for a very steady workout, NP and AP are almost equivalent. A relatively high NP indicates that the exercise has large ﬂuctuations and is physiologically more diﬃcult than the average power would represent.

• Average power output(AP) A rider’s average power output is the ratio of the total energy expended to the time spent completing a long race. The calculation method of AP is given below:

AP = total energy (1) total time

• Mean maximal power output(MMP) MMP is the amount of power a rider can produce for a given time eﬀort. For example, the highest average power output recorded over a 5-minute duration is the 5−minuteMMP.

Such MMP data are valuable because they can identify the energy output and duration a rider needs to produce.

• Anaerobic capacity(W ′) W ′ represents work capacity above critical power.

• Critical power(CP)

CP is the lower limit (or horizontal asymptote) of power curve. It is a physiologi- cal threshold that divides metabolic sustainable eﬀort and unsustainable eﬀort during exercise.

• Maximum instantaneous output power(Pmax) Pmax is the peak power over 1 second, which indicates the rider’s explosive strength.

• VO2max(V O2max) V O2max refers to the amount of oxygen that the body can take in during maximum intensity exercise. Since oxygen is the basis of many substance metabolism and energy metabolism activities in the body, V O2max is an important measure of rider stamina, reﬂecting the body’s aerobic exercise capacity.

be seen from the ﬁgure, the rider will arrive lactate threshold, critical power, VO2max in turn in the process of energy consumption.

4.2 Data Preparation

• Course conditions We found all the data we needed from the websites[1][2], along with the corresponding weather and environmental conditions.

• Rider type The riders are divided into ﬁve types as is given from the problem, namely time trial specialist, climber, sprinter, rouleur, and puncheur. We brieﬂy describe the ﬁve types of riders and summarize their characteristics, as shown in Table 1.

Type of Rider Description

An experienced and capable time trial rider.

Large lactate threshold, great muscle endurance, generally large FTP value, Time trial specialist great at maximizing the utilization of physical energy (physical ﬁtness assessment and allocation), and great endurance.

Riders specialize in long hill race. Climber Light weight, great endurance and limb strength.

Riders who specialize in producing extreme power in a short amount of time. Sprinter High explosive power, low endurance.

All-rounder for a variety of terrains. Rouleur Various indicators are relatively balanced, but not the top.

Riders who specialize in races including many short, steep climbs or sharp accelerations. Puncheur Heavy weight, strong leg strength, strong endurance, moderate explosive power, low waist strength.

The more power a rider produces, the less time the rider can maintain that power before having to recover. We use the tmaintain-p image to describe this physical diﬀerence of riders.

ﬁgure). P is the sustained level of power to the pedals. T −maintain is the time a rider takes to consume all his energy while maintaining his current power level.

• Power curve Riders are asked to do 3-5 full-power outputs of diﬀerent durations and record the riders’ power. The recovery between each full output should be set to at least 1 hour to ensure that the rider is getting enough recovery time. As an example, we got a scatterplot of the rider’s MMP for diﬀerent durations of full power output.The purpose of this is to perform ﬁtting and regression analysis on metrics such as critical power (CP).

5 Power Overall Planning Model

5.1 Model Overview

The rider ability and other external factors (including road conditions, weather conditions, etc.) are model’s input parameters, and rider’s power output in diﬀerent road sections as the output parameters. The model helps the rider to ride the course using a least amount of time, we need two steps. Step 1: Evaluate a rider ’s ability, using our Rider Ability Evaluation Model. Step 2: Segment the course, classify diﬀerent road sections, and analyze each of them. Then the relationship between the power and the time of each road section that aﬀects the rider’s ﬁnal performance is obtained.

5.2 Sub-Model 1: Rider Ability Evaluation Model

5.2.1 Overview of sub-model 1

We use power as our primary measure of rider ability. Through multiple tests of diﬀerent durations, a scatter plot describing the relationship of a rider’s maximum sustained power and maximum duration can be drawn, which we consider ﬁtting to a smooth curve. Why can the ﬁtted curve be smooth? Due to the continuous series of physiological responses in our body, the power-duration curve is inherently smooth. Since only a part of the ﬁtted curve is in good agreement with the actual situation, we conduct the exercise intensity domain division to clearly describe which part of the curve is closer to the actual situation.

5.2.2 Exercise intensity domain division

According to Burnley and Jones’ study in 2007[4],from a physiological perspective, the power-duration relationship is comprised of four distinct exercise intensity domains, namely, moderate, heavy, severe, and extreme. The basis for this division is that, for each exercise intensity domain, its power-duration curve has a relatively obvious diﬀerence.

In the ﬁgure, four exercise intensity domains are divided according to the power output and represented by diﬀerent colors.

5.2.3 Three-parameter critical power model

We choose the three-parameter critical power model as the Rider Ability Evaluation Model. In a paper by Peter Leo [3], ﬁve models describing the power-time relationship were compared, in which the 3-P CP model’s (Three-parameter critical power model) results in severe and extreme exercise intensity domains best match the actual situation. Thus the power output in the severe and extreme exercise intensity domains is more important in predicting the rider performance, so we decided to use the 3-P CP model as the power-time relationship model to ﬁt the test data. From the ﬁtted curve we can obtain the power curve of the rider, as well as the rider ability indicators.

Ability type

Symbol

Description

Rider’s standing height, the unit is meter(m). h Body height

The unit is kilogram(kg). m Body weight

The mean maximal power (MMP) that a rider can output within a given 5s is used to measure the explosive strength of Pmax Explosive strength a rider, in watts.

We measure a rider’s stamina by anaerobic capacity, namely the W Stamina amount of energy stored without oxygen.

We use critical power(CP) to represent a rider’s oxygen uptake capacity, and CP represents the theoretical asymptote of power, CP Oxygen uptake ability indicating that a given power output is sustainable all the time.

The stronger the bike control ability, the higher the rider’s BC Bike control ability maximum speed and upper limit of aggression.

Predictive trials of less than 2 minutes do not guarantee V O2max (ie, they are not in the severe intensity range). Recent work proposes that CP better estimates maximal metabolic homeostasis, i.e. the highest power output at which oxygen uptake homeostasis (V O2) responses are observed despite increased blood lactate values.

Power-Time Relationship Model

The relationship between power and time is shown as the equation below:

W ′ W ′ t = P −CP + (2) CP −Pmax where t is the duration; P is the maximum continuous power; W ′ is the anaerobic energy; CP is the critical power; Pmax is the maximum instantaneous power.

The ﬁtting of the model is achieved by using the ﬁtting tool for custom parameter functions in the MATLAB ﬁtting toolbox, and the ﬁtting result will be shown in the next part. In practice, if the actual conditions are not enough to obtain more power-time scatter values, the three parameters of the power-time curve can be measured by a simpliﬁed experiment, so that the power-time curve can also be obtained. CP can be measured by measuring the AP of the last 30s of a three-minute full-power output power curve, and Pmax can be obtained by measuring the average of the 5s full-power output power. After CP is measured, MMP and t can be obtained through a speciﬁc output power duration test. At this time, W ′ can be expressed by the following formula: W ′ = (MMP −CP) × t (3) It is worth noting that although it is simpler, the power-time curve measured by the above method will have a larger error than the ﬁtted result.

5.2.4 Evaluation of ﬁtting result

In order to evaluate the ﬁtting, we ﬁt a scatter plot drawn with data from multiple tests of an athlete, and the ﬁtting results are shown in Figure 5. The Goodness of Fit is 0.864, which is close to the perfect 1, so the ﬁtting is good and the model has practical signiﬁcance.

We can obtain the expression of the smooth curve after curve ﬁtting, and each parameter in the expression is the rider ability indicator.

5.3 Sub-Model 2: External Factors Analysis Model

5.3.1 Weather and environmental factors

The inﬂuence of weather and environment on the race is complex, as is shown in Figure 6:

The resistance to the rider mainly comes from the ground rolling resistance and wind resistance, and the rider often has to pay 40% of the full power to overcome these two resistances. Therefore, we consider the inﬂuence of weather and environmental factors from two aspects: road conditions and wind resistance.

• Road conditions The rolling resistance is mainly determined by the elastic force of the ground and the rolling resistance coeﬃcient, and its expression is:

Fr = kr × F (4)

where Fr is the rolling resistance, F is the elastic force of the ground, kr is the rolling resistance coeﬃcient which is related to the type of road surface, the tire structure, etc.

• Wind resistance

– Wind strength and wind direction. Wind resistance is the component of the wind force in the riding direction generated during high-speed riding, which is mainly related to the wind speed and wind direction.

When there is no wind, the formula for calculating wind resistance is:

Fw = 1 2 × cd × S × ρ × v2 (5)

where v is the riders speed, , cd is wind resistance coeﬃcient, S is the windward area.

When there is wind, it is assumed that the wind speed and wind direction are ﬁxed in a short time, and the angle between the wind direction and the riding direction is θ. When the wind is used as the reference frame, the rider is in a state of no wind, and the speed of the rider(vr) is

vr = v −vw × cos θ (6)

where vw is the wind speed. Then the wind resistance is:

Fw = 1 2 2 × cd × S × ρ × vr (7)

Considering the direction of the wind, then wind resistance > 0(0◦< θ < 90◦), wind resistance < 0(90◦<< 180◦), then the ﬁnal wind resistance expression is:

2 × cd × S × ρ × vr3 Fw = 1 (8) |vr| – Air density Air density ρ It is related to temperature and air pressure, and its calculation formula is:

ρ = pM (9) RT

where p is the air pressure, M is the molar mass of the gas, R is the proportionality constant (a constant value for any ideal gas), and T is the air temperature. Since air pressure is often not easy to measure directly, we convert changes in air pressure into changes in elevation. Their relationship is as follows:

Hs = H0 + R g × Tm × ln P0 (10) Ps

where H0 is the altitude, Hs is the altitude of the standard isobaric surface, P0 is the air pressure on the ground, Ps is the average height of the air column, and R and g are constants.

– Wind resistance coeﬃcient The drag coeﬃcient is determined only by the rider’s riding position. Based on the assumptions, we consider this parameter to remain unchanged. For cyclists, we consider cd = 0.23.

– Windward area According to Stevenson formula, the windward area is related to height and weight, and the expression is:

{ 1 4(0.0057h + 0.0121m + 0.0882), male rider maximum windward area = 1 4(0.0073h + 0.0127m −0.0099), female rider (11)

5.3.2 Time trial course factors

Our model also needs to be applied to any type of courses. Therefore, in order to make the course can be quantitatively analyzed, we need to summarize their characteristics. Then we divide all the course sections into four types: corner, uphill, downhill, and ﬂat ground, as is shown in Figure 7.

5.4 Establish the Power Overall Planning Model

5.4.1 Dynamic analysis on the course

We use parameters to measure four types of course sections: ﬂat ground(parameter: distance, speed and power), uphill (parameters: distance, slope, speed and power), downhill (parameters:

distance, slope, speed and power), corner (parameters: distance,radius of curvature, speed and power) and they are discussed separately below.

(a) Flat ground force diagram (c) Downhill force diagram (b) Uphill force diagram

• Flat ground P = (Fw + Fr) × v (12) = mg × kr × v + 1 2 × cd × S × ρ × v3 where Fw is the wind resistance(aerodynamic drag in the ﬁgure), Fr is the rolling resistance.

• Uphill P = F × v = (Fr + Fg + Fw) × V (13) = (kr × mg × cos θ + mg × sin θ) v + 1 2 × cd × S × ρ × v3 where Fg is the rider’s gravity(gravity in the ﬁgure), and angle θ > 0.

• Downhill We deﬁne a downhill as a road segment with a slope of more than 2%. Due to the similarity between downhill and uphill road sections, when going uphill, θ > 0 , and when going downhill, θ < 0. So only the uphill force formula is given here as the downhill force formula is similar.

• Corner  ( ) √  F 2 r −F 2 × v P = Fw +  c (14) Fc = m × v2   r

where Fc is the centripetal force.

5.4.2 Power output evaluation throughout the race

When analyzing a rider’s performance in a race, we use the indicators shown in the table below to evaluate the rider’s overall power output during the race.

Indicator

Symbol

Formula Description

[∑(P 4 ] 1 Average power is the total work in the entire ride i ×ti) 4 AP divided by the total ride time, which has a strong Average power t correlation with speed and force.

The results obtained after smoothing the power points that are too low and too high, and increasing ∑Pi×ti NP the proportion of the high power output section, Normalized power t describe the entire movement better than the average power.

The product of the average power and the total time. It is used to reﬂect only the work done AP × t Wt Total work when moving, and does not consider the extra work consumption caused by power changes.

Normalized work is the product of normalized power and total time, which is used to reﬂect the NP × t Wn actual work done in the race, including the extra Normalized work work consumption caused by power changes.

Usually greater than the total work.

It reﬂects the upper limit of the output power of the rider in the race. This upper limit should Maximum not be too diﬀerent from the average power, Pmax instantaneous power otherwise the optimal situation will not be achieved due to the extra power consumption caused by the power change.

The disadvantage of the average power is that if the power ﬂuctuates greatly during the ride, the arithmetic average power is not enough to reﬂect the entire riding intensity. For example, whileAP of high-intensity sprint training is too low to reﬂect its high intensity, normalized power NP is better.

If a rider’s power output keeps changing during the race, he will consume additional work. Therefore, if it is not necessary to keep changing for reasons such as psychological strategy, we do not recommend that since it is not conducive to the rider’s good results.

5.4.3 Multivariate nonlinear programming

After the above analysis, our problem is transformed into a multivariate nonlinear program- ming problem, the objective function is the total time t, and t needs to be minimized. Its mathematical expression is:

n n ∑ ∑ di mint = ti = vi i=1 i=1  1.15MMP (ti) > Pi > 0     NP ⩽MMP(t)     CP ⩽MMP(t)  (15)   1 MMP (ti) = CP + t 1 S.t. W ′ − 4√∑n CP −Pmax   i=1 P 4 i ti  NP =   t  ∑n   i=1 Piti AP =   t  Pi ⩾0, ti > 0

This problem is a typical multivariate nonlinear programming problem. The optimal output power Pi of each segment is solved to achieve the minimum total time min(t).

5.5 Model Solving and Evaluation

5.5.1 Model Solution

Since it is diﬃcult to ﬁnd the exact minimum solution for the multivariate nonlinear pro- gramming problem, we consider using the gradient descent method to gradually approach the local optimal solution to ﬁnd the optimal solution. After comparing multiple local optimal solutions, an approximate global optimal solution, that is, a better solution, can be obtained. It is solved by using the minimize function in python’s optimize toolbox.

It is worth noting that we cannot determine whether the next local optimum is what we are looking for, so we usually set a number of loops, and stop searching for the optimal solution after reaching the set number of times. The minimum value in the current most local minimum value is global optimal value.

5.5.2 Model Solution Method Evaluation

The minimize function in python’s optimize toolbox gives a variety of methods for solv- ing multivariate nonlinear programming, including ’SLSQP’, ’Nelder-Mead’, ’Powell’ ’CG’ ’BFGS’, ’Newton-CG’, ’L-BFGS-B’, etc. By comparing diﬀerent methods, we found that ’SLSQP’ solves faster, i.e. has less time complexity, so we choose the ’SLSQP’ method.

6 Application of the Model: Rider and Course

6.1 Rider: Diﬀerent Gender and Type

abilities of time trial specialist and puncheur, diﬀerence between genders is shown in the central diagram, the right diagram indicates the ability of four types of riders.

6.2 Course: Three Time Trial Courses

For diﬀerent time trial courses, we adopt control variates when applying our model, that is, our model only studies the optimal power distribution strategy of the same rider when racing on diﬀerent courses. We also only looked at the course conditions of the womens individual time trial. And this rider’s information is given in Table 4.

Gender Height Weight

Explosive strength

Stamina Oxygen uptake Bike control W ′ =550J 165cm 55kg Pmax =990W CP =230W female 0.87

2021 Olympic Time Trial course in Tokyo, Japan

The time trial courses are exactly the same for the both the men’s and women’s races despite from the diﬀerent distances. And we analyze and segment the course from two aspects, namely corners and slopes. After calculating the data, the results can be obtained(Table 7).

Temperature Air pressure Average altitude Wind direction

Wind strength

Air humidity 15.7 ◦C 15◦west of north 560m 7.5m/s 0.96 atm 60% Rolling resistance coeﬃcient kr Air density ρ Wind resistance coeﬃcient cd 1.2kg/m3 0.015 0.23

• Sharp corner

The black numbers next to the corners represent the radius of curvature, and the green numbers represent the length of the corner.

• Slope

slope, and the slope and length of each section are marked with the same color.

Length km Output power W Speed km/h time min Number Slope

1 -2.5% 2 181.34 32.36 3.68 2 -5.5% 1.7 157.35 44.84 2.27 3 6.5% 0.3 200.10 34.42 0.52 4 -4.5% 0.85 161.91 36.20 1.41 5 4% 5.45 193.21 24.48 13.3 6 -3.5% 4.15 158.85 34.19 10.29 7 0% 1.15 183.63 31.95 2.15 8 5% 1.8 223.97 26.49 4.07 9 -2.2% 2.6 189.63 33.28 4.68 10 3% 2.1 190.28 32.77 3.84 After solving, the shortest time is 46.21 min, the total length of the track is 22.1 km(13.7 mi), the average slope of the track is 3.5%, and the slope is relatively large, which puts forward higher requirements for the rider’s continuous output power, so climber will be more advantageous because the critical power (CP) and anaerobic energy (W ′) of the climber are larger. The obtained results are visualized in Figure 13. When we divide the course into shorter sections, we get Figure 14.

the three curves in diﬀerent colors represent power(watts), speed(km/h), and elevation(ft) respectively.

It can be seen that, in order to minimize the total time, the power distributed to the road sections with smaller slopes should be lower; the power distributed to road sections with higher slopes should be higher. The time reduction brought by the use of high output power when going uphill is greater than that when going downhill, so a larger output power is required when going uphill than when going downhill.

2021 UCI World Championship time trial course in Flanders, Belgium

Temperature Air pressure Average altitude Wind direction

Wind strength

Air humidity 28 ◦C 10◦east by south 10m 11m/s 1.013 atm 87%

Rolling resistance coeﬃcient kr Air density ρ Wind resistance coeﬃcient cd 1.23kg/m3 0.012 0.241 • Sharp corner

• Slope

Length km Output power W Speed km/h time min Number Slope

1 0.3% 1.65 204.58 27.34 3.62 2 -0.5% 1.55 127.93 32.96 2.82 3 -1.35% 0.8 100.04 47.00 1.02 4 0% 7.15 165.97 31.83 13.47 5 1% 0.85 209.77 22.19 2.29 6 -0.45% 2.00 131.45 36.82 3.25 7 0% 8.10 167.90 33.01 14.68 8 0.15% 7.2 184.38 27.65 16.26

After solving, the shortest time is 57.41 min, the total length of the track is 29.3 km(18.2 mi), the average slope of the course is 0.17%. The slope is extremely gentle, and the sprinter has more explosive power (Pmax), so it has an advantage on this course. Since there are no steep uphills, the sprinter can use all its power for fast sprints on relatively ﬂat roads, and the power output is evenly distributed.

The obtained results are visualized as follows:

6.2.1 Self designed course

Temperature Air pressure Average altitude Wind direction

Wind strength

Air humidity 15 ◦C 25◦east by south 345m 7.5m/s 0.91 atm 55%

Rolling resistance coeﬃcient kr Air density ρ Wind resistance coeﬃcient cd 1.17kg/m3 0.019 0.23 Our self-designed track has a total length of 13.78 km (8.56 mi) and is characterized by extreme steepness and ruggedness, with a maximum gradient of 25% and an average gradient of 11%. On this type of track, it is easy for a climber to get rid of his opponent on the climbing circuit. The calculated shortest time is 24.58 min.

7 Model Sensitivity Analysis

7.1 Sensitivity to Weather and Environment

In 5.4, for the inﬂuence of weather and environmental factors, we use the External Factors Analysis Model to summarize these inﬂuencing factors: air temperature (x1), air pressure (x2), altitude (x3), wind resistance (x4), and the ﬁnal target is to minimize the time t to complete the race.

Based on the idea of simulating importance sampling with subsets, we transform the sensitivity into the partial derivative of the conditional failure probability with respect to the underlying variable. This method has high computational eﬃciency and precision. As the number of samples in the data set increases, the failure probability will gradually approach a stable value.

Number Exact Estimation COV Error rate ∂t −1.8921 × 10−7 −18886 × 10−7 0.0187 0.18% ∂x1 ∂t −1.3748 × 10−7 −1.4294 × 10−7 0.248 3.97% ∂x2 ∂t -0.002215 -0.2219 0.010 0.18% ∂x3 ∂t −6.1065 × 10−7 −5.8486 × 10−7 0.046 4.22% ∂x4 ∂t 1.4345 × 10−7 1.4687 × 10−7 0.015 2.38% ∂x5

Cov is the coeﬃcient of variation of the estimated value commonly used in statistics, which reﬂects the convergence of the estimated value. Error(%) is the failure probability of the estimated value. The larger the error rate, the higher the sensitivity of the corresponding xi. From the results of the sensitivity analysis, it can be concluded that with 1 as the dividing line, air pressure and wind resistance are sensitive factors, while temperature and altitude are insensitive factors. Therefore, air pressure and wind resistance are relatively more inﬂuential indicators for our model.

7.2 Sensitivity to Deviations from Target Power

In a real race, although the rider will try his best to implement the power distribution plan formulated by the model, the accumulated rage value and energy consumption may aﬀect the rider’s judgment of the situation on the course, thus disrupting the rider’s power distribution on diﬀerent course sections.

The same player uses four strategies: the recommended strategy of the Power Overall Planning Model, start fast, start slow, and keep changing. The time of three diﬀerent track segments is used as the objective function to calculate the sensitivity.

Slope t1 Flat ground t2 Corner t3

Recommended strategy 0.42 0.23 0.33 Start fast 3.31 1.81 2.60 Start slow 1.54 0.84 1.21 Keep changing 5.57 3.05 4.38

Therefore, to improve rider performance, we supplemented the Power Overall Distribution Model by prioritizing the four strategies and ranking the importance of executing strategies for diﬀerent track segments: recommended strategy > start slow > start fast > keep changing, slope > corner > ﬂat ground.

8 Model Extension to Team Time Trial

In an individual Time Trial (TT), riders tend to target a steady pace at or around their Functional Threshold Power. But in a TTT, each rider will take turns pulling the group at signiﬁcantly higher power for a short period of time. The goal is to keep the teams speed consistent, but higher than any individual rider could ride alone.

The best strategy is: ﬁrst, the six riders are connected in a straight line, and the riding direction of the team is parallel to the wind direction, which can ensure that the rider at the head of the team bears most of the wind resistance. Secondly, in the ﬁrst a% of the track section, the two riders with the most explosive power and the lack of endurance lead the slopes and corners respectively, and the rest of the riders are not aﬀected by wind resistance in this track section. In the back a% to b% of the track, the two players whose physical strength was severely weakened due to the wind resistance of the entire team can slowly lag behind the team, and the other four players with more physical strength take turns at the head of the team to resist the wind resistance. Each rider trails behind the team after leading for 1 min, but still has to follow the team closely, so that each rider has a rest time of about 3 min per round with low power output.

In addition, the speed of the whole team should be consistent. What should the output power of the team leader(Pleader) be equal to? Obviously, Pleader must be greater than the output power of each track in the individual time trial(PITT). So we deﬁne: Pleader = c × Pleader. In order to reﬂect the diﬀerence between diﬀerent team members, the Rider Ability Evaluation Model was used ﬁrst, and the ability indicators of each rider were calculated by curve ﬁtting.

i) If the rider is not in the lead position on a track segment, our model needs to be changed accordingly: make a change in the force analysis diagram (remove the eﬀect of AERODYNAMIC DRAG), and ignore the formula (9). ii) In other cases, use the Power Overall Planning Model without modiﬁcation. In this way, a multivariate nonlinear programming problem with variables a, b, and c is obtained. The same algorithm is used to solve the problem, and the average value is calculated. A is about 45%, b is about 85%, and c is about 130%.

Therefore, we can get the team strategy of the six-person team: i)in the ﬁrst 45% of the track section, let two riders with strong explosive power and relatively weak comprehensive strength take turns to lead the ride, each leading for 5 min, and their output power is 130% based on the ITT model; ii)in the 45% to 85% track section, the two leading riders at the beginning gradually choose to fall behind, and the remaining four riders with stronger stamina each take turns to lead at 130% output power for 1 min. iii)In the last 15% of the track, the rider with the strongest comprehensive ability such as stamina is always in the lead until the end of the race.

9 Strength and Weakness

9.1 Strength

• Innovativeness. Our model uses 6 separate indicators to measure rider ability, which nicely captures the diﬀerences between riders, making the model relatively reliable and comprehensive. The selected indicators are in line with the latest research in related ﬁelds.

• High practical application value. To solve diﬀerent problems, we nest diﬀerent models to make the analysis of each problem more convincing.

• Vivid visualizations. Our model shows the power distribution method with many graphs, which is intuitive and clear.

9.2 Weakness

• Some data may not be accurate. We have made many assumptions, some of which are more diﬃcult to implement.

• The algorithm has too many variables, although it can comprehensively consider the problem, resulting in high time complexity.
