MCM/ICM

Summary Sheet

Summary

Stair wear patterns in historic buildings can provide valuable archaeological evidence regard- ing the building’s age, usage and traffic patterns throughout history. In this paper, we develop a comprehensive mathematical framework to analyze wear patterns and provide archaeologists with quatitative tools for historical interpretation.

First, we establish a non-destructive measurement methodology including physical, chemical and biological measurements. Physical measurements involve 3D scanning of stairs and monoc- ular depth estimation. Chemical measurements include isotope analysis and mineral composition testing. Biological measurements involve the study of microbial colonies. Then, we personally col- lected top-down photos of stairs from ancient buildings. Using depth map estimation methods, we drew heatmaps and obtained wear data.

Following data collection, we address the challenge of quantifying wear volume from discrete point cloud data. We employ Delaunay triangulation to transform the theoretical volume integral into a weighted summation of local triangular volumes, thus accurately calculating spatial wear volume.

Second, we build a Daily Foot Traffic Model based on the Archard equation. We take Ar- chard Adhesive Wear Model and Abrasive Wear Model both into consideration. Besides, we use Bayesian Inversion Framework to calculate the construction time to provide essential param- eter.

Third, we establish a Wear Distribution Model to determine movement patterns and simul- taneous occupancy levels. The model analyzes wear patterns to deduce whether people moved in single file or side by side, and whether there were predominant directional preferences.

For age estimation, we employ multiple approaches: C14 dating method for wooden stair- cases, weathering degree analysis for stone staircases, and Bayesian inversion.We constructed a weighted evaluation model of three representative Chemistry Weathering Indecies to evaluate the weathering condition of stone, providing information about its age.

To detect repairs or renovations, we analyze age distribution discontinuities using anomaly de- tection methods like the Z-score. We also verify the consistency of wear patterns with available historical information. For material source verification, we use the Archard Wear Model to cal- culate wear coefficients and perform chemical composition analysis to trace the origin of materials. We analyze usage patterns by examining the distribution of wear depth. By calculating the kurtosis of the distribution, we determine the usage pattern of stairs.

Finally, we perform a sensitivity analysis on the key parameters of our model to evaluate its responsiveness. The results demonstrate strong robustness.

Bayesian Inversion

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

Introduction

1 Problem Background 3 1.1 1.2 Literature Review. 3 1.3 Problem Restatement and Analysis 3 1.4 Our Work 4

Preparation 2 4 2.1 4

Notations

2.2

Assumptions

5 2.3 6 Detailed Measurement Plan .

Data collection and processing

2.4 8

Analysis and Modeling

9 3 3.1 Wear Volume Calculation . 9

Model I: Daily foot traffic model based on the Archard equation

3.2 10

Model II:Wear Distribution Modelsolving Problem 2 and 3

12 3.3

18 Estimate the Age of the Staircase 4 Estimate the Age of the Wooden Staircase With C14 Dating Method 18 4.1 Estimate the Age of the Stone Staircase Using Weathering Degree 19 4.2 20 4.3 Estimate the Age of the Staircase Using Bayesian Inversion. Verify the Age Estimate through Confidence Interval Estimation 20 4.4

20 5

5.1 Detection of Repairs or Renovations

20

5.2 Exploring the Consistency Between Wear and Information available

22

5.3 Analysis of Usage Patterns

23

Evaluation of Models

23 6 23

Sensitivity of Model I

6.1

Sensitivity of Model II

6.2 24 24 6.3

1 Introduction

1.1 Problem Background

The constant wear on stairs, especially in historic buildings, is a thought-provoking phenomenon. For example, many ancient buildings, such as temples and churches, show more wear in the center of the stairs than on the sides due to long-term use. The wear not only reflects the use of the stairs, 微信公众号：数学模型 but can also provide some important clues to archaeologists about the history of the building and how the stairs were used. The study of stair wear can help archaeologists speculate on the age of the building, the frequency of use, restoration, and past traffic patterns.

Different patterns of stair use and wear reflect people’s behavior, such as whether they walked up and down the stairs alone or with many people walking side by side. Our research aims to de- velop a mathematical model for archaeologists to better understand the history of building use and to infer information such as the frequency of using stairs, directional preference and the number of people using stairs at the same time. This process is important for the investigation and conserva- tion of historic edifices, offering a scientific foundation for archaeological endeavors and serving as a valuable reference for restoration and preservation initiatives. 微信号：MATHmodels The major problems(tasks) dealt with in this paper will be specified in Section 1.3.

1.2 Literature Review

Our research focuses on the wear on stairs caused by prolonged foot traffic. However, there is little direct research on this topic. Previous research mainly focused on material wear such as rail wear, gear wear, or some other wear in precision instruments. Previous research pointed out that wear can be categorized into five types: adhesive wear, abrasive wear, corrosive wear, erosive wear, and fretting wear [1]. We primarily focus on adhesive wear and abrasive wear, and believe that the wear on stairs mainly belongs to abrasive wear, with adhesive wear being secondary [2]. Therefore, Archard’s wear equation [3] can effectively link the wear volume to the usage conditions of the steps. Furthermore, some researchers have suggested that carbon-14 isotope dating can help determine the usage period of materials such as stone [4]. Additionally, some studies on using machine learning, specifically CNN models [5], to train data and obtain rail wear amounts have provided us with valuable insights.

1.3 Problem Restatement and Analysis

Our aim is to provide some important clues to archaeologists about the history of the building and how the stairs were used. Before solving subsequent problems, we need to do undertake a preliminary step:

Find a non-destructive, low-cost, small-team, and minimal-tool measurement plan.

Then, after obtaining all the data we need, we can build mathematical models to solve the following problems: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Problem 1. The usage frequency of the stairs. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Problem 2. The tendency of movement up and down the stairs. We should figure out whether people move up as well as down the stairs at the same time or there was a predominant direction.

Problem 3. The number of people who use the stairs at the same time. Determine whether pairs of people climb the stairs side-by-side or travel single file.

Assuming that we have obtained the basic estimates of the stair wear and built the necessary mathematical model, we need to :

Problem 4. Determine if the wear is consistent with the existing information.

Problem 5. Estimate the usage time of the stairs and assess the reliability of the estimate.

Problem 6. Figure out whether the stairs have been repaired or renovated. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Problem 7. Verify if the information source is accurate. (whether it comes from the quarry m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m claimed by archaeologists; whether it matches the age and type of wood) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Problem 8. Get the information about the usage condition of the stairs. (short-term heavy use m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m or long-term light use) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

1.4 Our Work

Our paper will be organized following the structure below.

2 Preparation

2.1 Notations

The primary notations used in this paper are listed in Table 2.

关注数学模型

Symbol

Definition Unit mm3 V Wear Volume P Load Force N H Material Hardness MPa L Friction Distance m 微信公众号：数学模型 K Wear Coefficient / t Usage Time day day−1 n Daily Foot Traffic d Friction Distance Per Step m Kabr Abrasive Wear Coefficient / Angle of Abrasive Cone rad θ N0 Initial Number of Carbon-14 Atoms atom N Current Number of Carbon-14 Atoms atom T0 The Half-life of Carbon-14 year tw The Usage Time of the Wooden Stairs year 微信号：MATHmodels year−1 W0 The Initial Weathering Rate The Weathering Rate Constant / λ The Persistent Effect of Microbial Communities / β dw The Wear Depth of a Step mm The Mean Wear Depth mm µ

2.2 Assumptions

Through a complete analysis of the problem, in order to simplify our model, we make the following reasonable assumptions.

Assumption 1: The treading position on the stairs is normally distributed when a single person walks.

The deviation in walking is generally symmetric and is influenced by various random factors. As the number of steps increases, the distribution of treading positions approaches a normal distri- bution.

Assumption 2: The time spent on each step by an individual is the same.

People generally maintain a steady pace, especially when walking without significant external disturbances. In addition, the time spent on each step tends to be similar due to the coordinated rhythm of movement, particularly during continuous stair climbing.

Assumption 3: When multiple individuals walk side by side, their positions are symmet- rically distributed.

People often adjust their walking positions to avoid crowding or collisions, naturally forming a pattern in which their positions are distributed symmetrically along the walking path.

Assumption 4: All steps on the staircase have the same initial material properties, includ- m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m ing hardness and density. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Staircases are generally made from the same material or materials with very similar properties throughout the process.

Assumption 5: The steps will be renovated using the same materials as before, and the renovation will not be complete demolishing and rebuilding.

Renovation materials in regular construction are generally consistent with the original materials, and renovation is often the filling in worn areas rather than completely demolishing and rebuilding.

2.3 Detailed Measurement Plan

To analyze the wear patterns of stairs and make speculation about their usage, historical context, and traffic patterns, we propose a detailed measurement plan. The following approach integrates physical, chemical, and biological measurements to collect relevant data in a non-destructive, low-cost, small-team, and minimal-tool measurement.

2.3.1 Physical Measurements

Through physical measurements, we need to obtain the three-dimensional image of the staircase to establish the coordinate system, material hardness, wear degree and material properties.

(1) 3D Scanning of Stairs with Laser Scanner We should use a laser scanner to scan the steps, capturing precise geometric data of the stairs [6].

Data Collected:

1. Three-dimensional spatial coordinates of the stairs.

2. High-resolution surface details, including the surface roughness and micro deformation.

Tool Required: Laser scanner (could be handheld or tripod-mounted).

(2) Depth Measurement of Stairs with Monocular Depth Estimation

Take overhead photographs of the stairs from a vertical viewpoint, and then use Monocular Depth Estimation Model to calculate the wear depth at various locations on the stairs without any destruction to the material [7]. This measurement scheme perfectly meets the requirements of being non-destructive, relatively low-cost, and allowing measurements to be taken by a small team of 关注数学模型 people with minimal tools.

Data Collected: Precise wear depth at each point.

Tool Required:High-resolution camera.

Precautions: 微信公众号：数学模型 1. To address the issue of the MDE model only returning relative depth, a standard ruler should be placed during photography to convert relative depth into absolute measurements.

2. Due to random errors, the shooting angle may not be perfectly horizontal. Gyroscope data from the device used during photography can be collected to correct the depth information.

微信号：MATHmodels

2.3.2 Chemical Measurements——Isotope Analysis and Mineral Composition Testing

Utilize non-invasive isotopic techniques (such as Carbon-14 or stable isotope analysis) to iden- tify chemical signatures in the stone or materials used to construct the stairs [8]. Additionally, measure the mineral composition related to the weathering of the material. The required mineral compositions are listed in Table 4.

Data Collected: Isotopic ratios of the stone or material used to construct the stairs, and the mineral composition associated with weathering.

Tool Required: Portable isotopic analysis and calibration tools (such as the International Ra- diocobin Database) and tools for analyzing the weathering-related mineral content.

2.3.3 Biological Measurements——Acquiring microbial colonies

Take surface samples from the stairs to analyze the microbial colonies. Swab the stair surfaces and perform microbiological analysis to study the types of microbes present and their distribution [9].

Data Collected:

1. Microbial diversity and abundance in different areas of the stairs. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m 2. Identify the impact of microbial communities on the weathering degree of the staircase. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Tool Required: m m m m m m m m m m m m m m m m m m m Microbial sampling kits, portable incubators, and analysis tools.

2.4 Data collection and processing

To address the lack of public stair wear data, we personally collected top-down photos of stairs from several old temples in China. Using depth map estimation methods, we obtained wear data for further analysis. The sampling points, stair materials, and estimated wear conditions of these stairs are summarized in the table below. In order to observe the wear patterns of each stair, the heatmaps are drawn for each sample.

Stair ID Sampling Point Stair Material Visual Assessment of Wear Condition

1 1 Cement Slight 2 1 Cement Slight 3 1 Cement Slight 4 1 Cement Moderate 5 2 Blue Slate Severe 6 2 Blue Slate Severe 7 3 Marble Slight 8 3 Marble Slight 9 3 Marble Slight 10 4 Granite Moderate 11 4 Granite Slight

Sampling Point 1 Sampling Point 2 Stair No.4 Stair No.5

Sampling Point 3 Sampling Point 4 Stair No.7 Stair No.11

关注数学模型 微信公众号：数学模型 (a) Stair No.2 (b) Stair No.3 (c) Stair No.5

微信号：MATHmodels

3 Analysis and Modeling

3.1 Wear Volume Calculation

1.Mathematical Modeling of Step Surface Wear Volume

The goal of surface wear volume calculation is to estimate the spatial volume (the concave part) beneath a three-dimensional surface. Suppose a continuous surface z = f(x,y), the concave volume can theoretically be represented as:

ZZ S |f(x,y)|dA V = (1)

where: f(x,y) is the height (or depth) function of the surface; dA is the differential area element.

However, the actual data consists of discrete point clouds without an analytical form of f(x,y), so the integral cannot be directly solved. We use the triangulation method to discretize the problem and replace the integral with a weighted summation over the areas and depths of triangles.

2. Principle of the Discrete Method

Triangulation

Data points are distributed in the plane, and through triangulation (Delaunay Triangulation), the point cloud is divided into many small triangles; Each small triangle approximates a part of the original surface [10].

Local Volume Calculation

For each triangle, we compute its area A:

A = 1 2∥⃗v1 ×⃗v2∥ (2)

where⃗v1 and⃗v2 are the two edge vectors of the triangle.

Compute the average depth h of the triangle region: h = 1 3(z1 +z2 +z3) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Compute the local volume: V = A·|h| m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Global Volume Summation

The total volume is obtained by summing the local volumes of all triangles:

Vtotal = ∑ Ai ·|hi| (3) i

3.2 Model I: Daily foot traffic model based on the Archard equation

To solve Problem 1——the usage frequency of the stairs, we only need to consider the total wear. Based on our literature review and analysis, wear can be categorized into five types [1], and we believe the wear on stairs mainly belongs to abrasive wear, with adhesive wear being secondary. Therefore, Archard’s wear equation [3] can effectively link the wear volume to the usage conditions of the steps.

3.2.1 Archard Adhesive Wear Model

The wear volume V based on the Archard Adhesive model is given by the following formula:

V = KPL (4) 3H

where: V is the wear volume, K is the wear coefficient, P is the load force, L is the Friction distance and H is the material hardness.

3.2.2 Archard Abrasive Wear Model:

In adhesive wear, K represents the probability of wear debris being generated at the contact microasperities; while in abrasive wear, Kabr represents the product of the abrasive particle geo- metric factor 2ctgθ and a proportional constant. The actual proportional constant is the fraction of π all abrasive particles that generate wear debris [11].

According to the Archard equation, the abrasive wear coefficient is given by:

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Kabr = 3tanθ m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m = 0.96tanθ ≈tanθ (5) m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m π m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Thus, the simplified abrasive wear equation can be: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

V = Kabr · L (6) 3H

Based on the theoretical calculations, the values of tanθ and KP show little difference in the theoretical results of the stair wear model. Therefore, we can simplify the model and use formula (1) to solve the problem.

From the Archard model, we can estimate the wear volume by calculating the total friction distance. The total friction distance L is given by the formula: 关注数学模型 L = n·d ·t (7)

where: n is the daily foot traffic , d is the friction distance of an average person, t is the total time.

According to the analysis,the theoretical value of d is 0.01 m, and P is 650 N.

Combining the equations above, we get:

n = 3·V ·H (8) K ·P·d ·t 微信公众号：数学模型 Applying this formula to our 11 staircase samples, we calculated the estimated average daily pedestrian flow, as shown in the table below. The values of H and K used in the estimation were referenced from relevant literature on staircase materials, while t was estimated based on publicly available information about the building:

n (day−1) V (mm3) t (day) Stair ID Wear Condition

1 9100 3796.5 Slight 1925.5 2 9100 2395 Slight 1214.7 3 9100 3833 Slight 1944.0 微信号：MATHmodels 4 9100 6277 Moderate 3183.6 5 29200 10617 Severe 8390.6 6 29200 13495 Severe 6399.1 7 5470 4024.5 Slight 5093.5 8 5470 3598 Slight 4553.7 9 5470 2351.5 Slight 5952.3 10 14600 7496.5 Moderate 4739.6 11 14600 5753.5 Slight 3637.6

3.2.3 Bayesian Inversion Framework

To estimate the daily foot traffic n and usage time t, a Bayesian inversion framework is em- ployed. This approach combines prior knowledge with observed data to infer the posterior distri- bution of the parameters.

The prior distribution represents our initial knowledge about the parameters. For usage time t, a uniform distribution is assumed:

t ∼U (tmin,tmax), (9)

where tmin = 50 years and tmax = 200 years.

The likelihood function quantifies the agreement between the observed wear volume Vobs and the model prediction Vmodel. It is defined as:

−(Vmodel(t)−Vobs)2   L (t|Vobs) = exp , (10) 2σ2 where:

Vmodel(t) is the wear volume predicted by the Archard model for a given t, σ is the standard deviation of the observation error.

Posterior distribution combines the prior distribution and the likelihood function using Bayes’ theorem:

P(t|Vobs) ∝L (t|Vobs)·P(t). (11)

The posterior distribution is estimated using a grid search over the range t ∈[tmin,tmax].

The maximum a posteriori (MAP) estimate of t is obtained by maximizing the posterior dis- tribution:

P(t|Vobs). tMAP = argmax (12) t Once tMAP is determined, the daily foot traffic n is calculated using:

3·Vobs ·H n = . (13) K ·P·d ·tMAP

3.3 Model II:Wear Distribution Model——solving Problem 2 and 3

The solution of Problem 2

1. Preliminary analysis

We establish a two-dimensional coordinate system, with the midpoint of the step edge as the origin. Take the step’s horizontal length as the x-axis and the vertical width as the y-axis.

The difference between ascending and descending mainly lies in the different force points on the steps, reflected in the y-coordinate. This problem doesn’t consider the lateral wear differences.

2. Analysis of Stair Wear Locations

When moving upstairs, the force is primarily applied to the front edge and the sides of the step. As the foot pushes upward, the pressure is focused on the front part of the stair, which leads to more wear on the front edge of the step.

In contrast, when moving downstairs, the body’s weight shifts downward, causing more pres- sure to be applied to the central and rear parts of the step. This results in greater wear on the middle and rear edges of the stair. The force analysis diagrams of these two processes will be shown below.

关注数学模型 According to the analysis of movement differences and the force analysis diagram, it can be seen that:

Upward movement causes wear primarily on the front edge and the edges of the stairs.

Downward movement causes wear mainly on the central part and the rear edge of the steps [12]. 微信公众号：数学模型 Based on the actual data and the model, it can be established that:

Upward movement: Wear is assumed to follow a "truncated" normal distribution, which means the wear at the front edge and the stair edges gradually decreases as we move along the stairs, with the highest wear occurring at the front part.

Downward movement: Wear follows a normal distribution, meaning the wear is most sig- nificant in a certain region on the central part of the stairs, and the distribution is typically more symmetrical.

If both upward and downward movements occur: Wear depth will exhibit a bimodal dis- 微信号：MATHmodels tribution, which is the combination of two normal distributions — one representing the wear from upward movement and the other representing the wear from downward movement.

3. Mathematical Modeling

To solve this problem, we can establish a mathematical model through the following steps:

3.1 Establishing the 2D Coordinate System

- Set up a 2D coordinate system, with the midpoint of the stair edge as the origin.

- The y-coordinate represents the position along the stair from the front edge to the rear edge.

3.2 Wear Depth Function h(y)

Based on the wear distribution types, we define the average wear depth function h(y) at position y. According to the given assumptions, if we only consider upward or downward movement, the wear depth can be modeled using normal distributions.

Upward movement:

Assuming the wear depth for upward movement follows a "truncated" normal distribution, we can model it as: −(y−µup)2   1 √ y ≥0 hup(y) = , 2π exp (14) 2σ2 σ where µup is the mean position of the wear for upward movement, and σ is the standard deviation.

Downward movement: The wear for downward movement typically follows a normal distri- bution, so we can represent it as:

−(y−µdown)2   1 √ hdown(y) = 2π exp (15) 2σ2 σdown down

where µdown is the mean position of the wear for downward movement, and σdown is the standard deviation.

Both upward and downward movements: If both upward and downward movements occur, the wear depth will exhibit a bimodal distribution, which can be represented by the sum of two normal distributions:

htotal(y) = α ·hup(y)+(1−α)·hdown(y) (16) where α is a weight coefficient representing the proportion of upward movement, and 1 – α repre- sents the proportion of downward movement.

3.3 Computer Simulation of Several Typical Wear Patterns.

After considering all the above factors, we wrote a Python program using the Monte Carlo method to simulate stair wear based on some hypothetical data. The program generates surface plots of the stair tread and wear depth heatmaps corresponding to the three typical wear patterns, which are shown below:

(c) Both Upstairs and Downstairs (a) Single File Upstairs (b) Single File Downstairs

3.4 Hypothesis Testing

Based on the wear depth data obtained, we can perform hypothesis testing.

Null Hypothesis (H0): The wear depth follows a normal distribution or truncated normal dis- tribution.

Alternative Hypothesis (H1): The wear depth doesn't follow a normal distribution or truncated normal distribution.

We have obtained a set of stair wear depth data representing the wear at various positions y.

The Shapiro-Wilk test involves the following steps:

1. Calculate the sample mean h:

n 1 h = ∑ (17) hi 一 n i=1 where n is the sample size and h is the individual wear depth value.

2. Sort the data h(1) , h(2), . . . , h(n), which means ordering the wear depths in increasing order.

3. Calculate the Shapiro-Wilk statistic W: The statistic W is calculated using the formula:

(Σi=1aih(i)2 W = (18) z(y−}y)[=13

where a is a set of constants calculated based on the sample size n, h(i) are the ordered data points, and  is the sample mean.

4. Comparing the Statistic with Critical Values

ORO

Wilk critical value table to obtain the critical value Wcrit. If the computed W ater thanthe critical value Wcrit, you fail to reject the null hypothesis, indicating that the data follows a normal distribution. If W is smaller than the critical value, you reject the null hypothesis, indicating that the data does not follow a normal distribution.

3.5 Interval Estimation

If the hypothesis testing results support the normal distribution assumption, we can perform interval estimation for the mean µ. Using the sample mean ¯y and standard deviation s, we can estimate the confidence interval for µ using the following formula:

微信公众号：数学模型   ¯y−tα/2 · s √n, ¯y+tα/2 · s √n µ ∈ (19)

where tα/2 is the critical value from the t-distribution, and n is the sample size.

4. Considering "Edge Effect" in Wear

Wear is expected to be more significant at the edges of the stairs than at the center. Therefore, we need to account for this factor in our model. This can be done by adding an adjustment factor kedge for the edge region, such that wear is higher near the edges. Specifically, we can modify the wear depth function as follows:

微信号：MATHmodels       1+kedge ·|y| · α ·hup(y)+(1−α)·hdown(y) htotal(y) = (20)

where kedge is a constant representing the intensity of the edge effect, and |y| is the absolute distance from the center.

5. Analysis on Stair Samples

To demonstrate the variation in wear extent along the y-axis, we developed a Python program that bins the y-axis into an appropriate number of equally spaced intervals. The maximum wear depth within each bin was then extracted, and a projection curve of wear depth distribution along the y-axis was plotted. It can be observed that they align with the patterns we previously analyzed, as several typical cases are shown below:

(a) Both Upstairs and Downstairs (b) Downstairs Primarily (c) Upstairs Primarily

The solution of Problem 3:

1. Initial Analysis

Regarding the number of people using the stairs simultaneously and whether they climb side- by-side or in single file, we can extend the concepts discussed in Problem 2.

When multiple people are involved, the wear distribution changes:

Side-by-side movement results in a multi-peak distribution of wear, which covers the front edge of the stairs (for upward movement) or the central part of the stairs (for downward movement). The peaks represent the locations where each person steps, and the number of peaks indicates how many people are moving simultaneously.

Single-file movement produces a single peak at the location of one person's step, with the intensity of wear varying along the length of the stairs.

Height of Worn Step Distribution Height of Worn Step Distribution

Wor Single Step Model Wor Single Step Model (Pairs of People Upstairs) (Pairs of People Downstairs)

2.0 2.0 (4P) A 1.8 1.8 1.6 (as) z 1.6 (Iegahl z 14 1.4 12 12 1.0 10 0.8 0.8

10 10 10 25 20 25 X (Length) 20 x (Length) 10 × (Length) 25 25 30 1.850 1.965 1.995 2.025 1.550 1.625 1.700 1.775 1.925 1.785 1.815 1.845 1.875 1.905 1.935 2.000 1.475 He w  taep de e  eed

(a) Pairs of People Upstairs (b) Pairs of People Downstairs

2. Mathematical Modeling of Multiple People Moving

If people are moving in side-by-side formation, the wear distribution can be represented as the sum of several normal distributions, with each peak corresponding to a person's position.

For upward movement, the wear can be modeled as:

(y − µup,i)2 N 1 hside-by-side up(y) = ∑ (21) exp 2σ{p iσup√2π i=1

where: N is the number of people moving side-by-side, μup,i is the mean position of the i-the person's step, σup is the standard deviation representing the spread of wear.

The same applies to downward movement.

If multiple people are moving both upward and downward simultaneously, the total wear depth distribution will be a multimodal distribution, representing the superposition of upward and downward movements.

As in Problem 2, we plotted the projection of wear depth along the x-axis for some staircase samples. In the following, three typical cases are presented.

关注数学模型 Wear Curve by X-axis (Stair No.4) Wear Curve by X-axis (Stair No.6) Wear Curve by X-axis (Stair No.5) 0.00000 0.030000 0.00000

-0.000025 -0.000025 -0.00005 -0.000050 -0.000050 -0.00075 -0.00010 -0.000075 afe -0.0010 -0.000100 -0.00015 -0.000125 -0.000125 -0.00150 -0.00020 -0.000150 -0.000175 -0.000175 -0.00025 -0.000200 -0.0006 -0.0004 -0.0002 0.0000 0.0002 0.0004 -0.0008 -0.0006 -0.0004 -0.0002 0.0002 0.0004 -0.0008 -0.0006 0.0000 0.0002 0.0004 0.0006 0.0000 0.0006 -0.0004 -0.0002 0.0008 -0.0008 0.0006

(b) Double Files (a) Single File (c) Double Files

3. Dealing with Two-Way Traffic If the stairs allow for simultaneous upward and downward movement (two-way traffic), two different scenarios arise:

3.1 Automatic two-way traffic:

If one side of the stairs is used for upward movement and the other side for downward move- ment (e.g., left side for up, right side for down), the wear distribution will show two distinct sets of peaks—one representing the upward movement and the other representing the downward move- ment.

The peak locations for the upward and downward movement will be distinct along the y-axis, and we can analyze these to determine the direction of movement.

3.2 Mixed two-way traffic:

If both upward and downward movements occur in the same region of the stairs, the wear distribution will be a multi-modal distribution (similar to the single-file or side-by-side cases), but with overlapping peaks. The distribution will reflect both upward and downward movement, and by analyzing the relative positioning of the peaks, we can estimate the number of people moving in both directions.

Height of Worn Step Distribution Height of Worn Step Distribution

Wom Single Step Model Worn Single Step Model (Left Downstäirs, Right Upstairs) (Pairs of People Upstairs and Downstairs)

2.0 2.0 1.8 1.8 1.6 ( z 1.6 14 1.4 12 12 1.0 1.0 0.8 0.8

10 10 10 25 15 25 X (Length) 20 20 20 X (Length) X (Length) 25 25 30 1.74 1.77 1.80 1.83 1.86 1.89 1.92 1.95 1.98 2.01 1.785 1.815 1.845 1.875 1.905 1.935 1.965 1.995 2.025 Her w r wtep Height of Worm Step

(b) Left Downstairs, Right Upstairs (a) Pairs of People Upstairs and Downstairs

4. Hypothesis Testing and Estimation

Using hypothesis testing, we can assess whether the observed wear distribution fits the expected patterns (normal or truncated normal distributions). For the wear data collected, we perform the Shapiro-Wilk test as described in Problem 2 to confirm the distribution type.

4 Estimate the Age of the Staircase

In this part, we will figure out the estimation of the age of the stairs. The reason for dedicating a separate section to it is that the C14 dating method, weathering degree model, and Bayesian inversion method used here have an insightful role in solving the subsequent problems.

For wooden stairs, the construction year can be inferred using the radiocarbon dating method (Carbon-14 dating).

For stone stairs, the construction year can be inferred by analyzing the degree of weathering. By selecting parts of the stairs that are less likely to be directly affected by foot traffic, such as the riser, stringer, or lightly worn areas of the step tread, and examining the degree of weathering, the construction year of the stone stairs can be accurately estimated.

Then, we use Bayesian inversion method to compare observed and theoretical values, and the maximum a posteriori (MAP) estimation method is used to find the most probable age t given the data.

With all the methods above, we finally assess the reliability of the age estimate through the calculation of a confidence interval.

4.1 Estimate the Age of the Wooden Staircase With C14 Dating Method

Carbon-14 dating is a method based on the half-life of carbon-14 to estimate the age of an object. By measuring the current carbon-14 content in a wood sample, we can estimate the age of the wood, i.e.,the usage time of the wooden stairs [13].

The carbon-14 decay process follows an exponential decay law, represented by the formula:

N = e−tw T0 ln2 (22) N0

where: N0: The initial number of carbon-14 atoms in the wood when it was cut. N: The current number of carbon-14 atoms in the sample. T0 = 5730 years: The half-life of carbon-14.

tw: the age of the wood, i.e.,the usage time of the wooden stairs.

Rearranging the equation, we get:

−T0 ln N N0 tw = (23) ln2

关注数学模型

4.2 Estimate the Age of the Stone Staircase Using Weathering Degree

微信公众号：数学模型 When estimating the age of stone stairs, one effective method is to analyze the degree of weath- ering, which is influenced by the exposure to environmental factors such as humidity, temperature, and microbial activities. Therefore, we will select parts of the stairs that are rarely touched by feet, such as the riser, stringer, or the least worn areas of the step tread, to examine their weathering level, in order to eliminate the influence of wear on the degree of weathering.

It is assumed that the weathering process occurs gradually and affects the surface of the stone in a regular pattern year by year. A common weathering rate model is the exponential decay model.

W(t) = W0e−λt +β 微信号：MATHmodels (24)

where: W(t) is the degree of weathering at time t, W0 is the initial weathering rate, λ is the weathering rate constant and β is the persistent effect of microbial communities Due to the inherent variability in the chemical composition of rocks, it is difficult to char- acterize weathering conditions through changes in a single chemical component. The academic community generally uses chemical weathering indices to represent weathering conditions. Re- search has shown that the following three chemical weathering indices—WI, PI, and LOI—exhibit clear monotonicity and sensitivity to changes in weathering degree and time [14]. These indices can be used as the primary basis for evaluating the degree of rock weathering and determining weath- ering depth. Their calculation methods are as follows, in which all chemical formulas represent the amount of substance:

Chemical Weathering Index Formula

IWeather/IFresh, WI K2O + Na2O + CaO - H2O SiO2 + Al2O3 + Fe2O3 + TiO2 + CaO + MgO + Na2O + K2O ×100% I = Si2O Si2O+Ti2O+Fe2O3+Al2O3 ×100% IWeather/IFresh, I = PI IWeather/IFresh, I = m(H2O) ×100% LOI m

Therefore, we use these three indices to construct a weighted evaluation model for comprehen- sively assessing the weathering degree W(t) of the stone, namely:

W(t) = w1(WT)+w2(PI)+w3(LOI) (25)

w1, w2, w3 represent the weights of the three chemical weathering indices, satisfying w1 +w2 + w3 = 1. The sensitivity of different chemical weathering indices to different types of rocks varies, so the weights can be dynamically adjusted according to the rock type.

By obtaining the degree of weathering W(t0) at a specific time t = t0 and the current degree of weathering Wcurrent, we can estimate the construction age:

  W0 t0 = 1 λ ln (26) Wcurrent −β m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

4.3 Estimate the Age of the Staircase Using Bayesian Inversion

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m The posterior distribution of t is estimated using a uniform prior t ∼U (50,200) and a Gaussian likelihood:

! −(Vobs −Vtheory)2 L (t|Vobs) = exp . (27) 2σ2

The maximum a posteriori (MAP) estimate of t is obtained by maximizing the posterior distribu- tion.

4.4 Verify the Age Estimate through Confidence Interval Estimation

To assess the reliability of the estimate, we can calculate a confidence interval for the estimated age using the uncertainty in the measurement of Wcurrent, λ, and β.

Using propagation of uncertainty, we can estimate the uncertainty in t0. The general propagation formula for a function f(x1,x2,...,xn) with independent variables x1,x2,...,xn is:

s ∂f  ∂f  ∂f 2 2 2 σ f = + +...+ (28) σx1 σx2 σxn ∂x1 ∂x2 ∂xn

  W0 For the age estimation formula t0 = 1 λ ln , we compute partial derivatives with re- Wcurrent−β spect to each parameter (such as Wcurrent, λ, and β) and then calculate the uncertainty σt0.

Once the uncertainty in t0 is determined, we use this to construct a confidence interval. With a normal distribution assumption, the 95% confidence interval for t0 is:

(t0 −1.96·σt0,t0 +1.96·σt0) (29)

5 Further exploration

5.1 Detection of Repairs or Renovations

To detect whether the stairwell has undergone repairs or renovations, we primarily use the aforementioned estimation of the staircase age with an anomaly detection method applied to the age data.

Let S represent the staircase, and P1,P2,...,Pn be the set of distinct sampling points on the staircase. These points are chosen from locations less affected by foot traffic. The set of these points can be expressed as:

P = {P1,P2,...,Pn} (30)

For each sampling point Pi, the measured value is denoted as Vi. The set of all measurements is then: 关注数学模型 V = {V1,V2,...,Vn} (31)

Anomaly Detection in Staircase Age Estimation

To determine whether a staircase has been renovated or maintained, we can compare the esti- mated ages with each other to identify whether renovations or repairs have occurred and approxi- mate the year of renovation.

With Carbon-14 dating, the age of the wood (tw) is calculated as:

微信公众号：数学模型   N −T0 ln N0 tw = (32) ln2 Using weathering degree model, the construction age t0 can then be estimated using:

  W0 t0 = 1 λ ln (33) Wcurrent −β

We use the Z-score method to identify the sampling points with t significantly different from the local average: 微信号：MATHmodels z = dw −µ , (34) σ where: dw is the wear depth of a step, µ is the mean wear depth, σ is the standard deviation of wear depths.

Steps with |z| > 2.0 are flagged as anomalies, indicating potential repairs or renovations.

If one or more of the estimated ages from the different methods significantly differ from the others, it could suggest that the staircase was renovated or replaced at some point.

The estimated age and the associated uncertainty in the age can help pinpoint the likely time frame when renovations or repairs occurred.

(a) Repair Conducted (b) Repair Not Conducted m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

5.2 Exploring the Consistency Between Wear and Information available

Both Problem 4 and 7 explore whether the stair wear is consistent with the available background information. Problem 7 is more specific, as it focuses on whether the wear can be used to verify the source of the materials used.

5.2.1 Daily Foot Traffic

Using Model 1, the daily foot traffic n of an ancient building can be calculated:

n = 3·V ·H (35) K ·P·d ·t

n can then be compared with the known daily foot traffic of the building. If the calculated foot traffic falls within a certain confidence interval, the result is considered reasonable. The confidence interval can be estimated as:

(nobs −1.96·σn,nobs +1.96·σn) (36)

5.2.2 The Construction Year

For wooden and stone stairs, the construction year can be estimated using C14 Dating and Weathering Degree Models respectively.

the age of the wooden stairs tw is:

−T0 ln N N0 tw = (37) ln2

the age of the stone stairs tw is:

  W0 t0 = 1 λ ln (38) Wcurrent −β

The reliability of the construction year can be verified through this confidence estimation:

(t0 −z·σt0,t0 +z·σt0) (39)

5.2.3 Verifying Material Source

There are two methods to verify the material source:

m m m m m m m m m m m m m m m m m m m m m m

Wear Coefficient Verification

m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m Using the Archard Wear Model, the expression for the wear coefficient K is: m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m K = 3VH m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m (40) m m m m m m m m m m m m m m m m m m 关注数学模型 m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m PL m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m This formula can be used to calculate the wear coefficient K, as the values for wear volume V, material hardness H, load force P, and friction distance L are known. 微信公众号：数学模型 We can compare it to the known wear coefficient of the material source. If the measured wear coefficient matches the expected value, the material can be traced back to its original source.

Chemical Analysis Verification

The material’s chemical composition can be analyzed to determine its source. For wood, the species can be identified, and for stone, mineral composition can be analyzed. By comparing these results with known material properties from a claimed source, the material’s origin can be verified.

5.3 Analysis of Usage Patterns

微信号：MATHmodels If there is a small number of people walking over a long period, it can generally be assumed that people will follow the distribution of single-file walking and occasional walking side by side, which leads to localized deeper wear on the stairs.

However, if a large number of people use the stairs over a short period, they will have to walk side-by-side, following a distribution pattern for multiple people walking together,which results in a flatter distribution.

Therefore, we can determine the type of walking pattern and assess the density of foot traffic over a short time based on the distribution.

The kurtosis of the wear depth distribution is calculated to determine whether the stairwell experienced short-term high-intensity usage or long-term low-intensity usage:

Kurtosis = µ4 σ4 −3, (41)

where: µ4 is the fourth central moment, σ is the standard deviation.

A high kurtosis (> 3) indicates long-term low-intensity usage, while a low kurtosis (≤3) indi- cates short-term high-intensity usage.

6 Evaluation of Models

6.1 Sensitivity of Model I

In the stair wear model, sensitivity is calculated using:

Sensitivity = ∆n/n ∆θ/θ , (42)

where:∆n is the change in the output, ∆θ is the change in the input parameter.

The Lord Force (P) shows high sensitivity. The Material hardness H and Wear coefficient K has medium sensitivity while the friction distance per step (d) exhibits low sensitivity. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m As analyzed, the change in variables has little effect on the results, indicating that the model m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m has good generalization ability. m m m m m m m m m m m m m m m m m m m

6.2 Sensitivity of Model II

Model II focuses on wear depth based on movement patterns.The sensitivity of the wear depth m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m function depends largely on parameters such as σ, µ and pup. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m As analyzed, our results indicate that the models are robust for typical parameter ranges. m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m m

(c) Parameter: pup (a) Parameter: µ (b) Parameter: σ

6.3 Strength and Weakness

6.3.1 Strength

• Innovativeness: Our model fully incorporates physical, chemical, and biological data from the staircase, employing cross-validation with multiple data sources to boost reliability.

• High Practical Application Value: We collected a large amount of real and fresh data. By using actual measurements and 3D modeling, we applied the model to real data and tested the effectiveness.

6.3.2 Weakness

• First, some common destructive factors, such as knife marks, acid rain corrosion, etc. may have a certain impact on the results of the model.

• Secondly, the accuracy of the collected data is limited, and the actual walking trajectories of people may be random.

关注数学模型
