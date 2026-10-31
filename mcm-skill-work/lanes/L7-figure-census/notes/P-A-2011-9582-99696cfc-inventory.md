# P-A-2011-9582-99696cfc — figure census

- layout sha `0a972be265b937e1`, 34 pages, 68 measured regions
- accounted: 59 figures, 3 tables, 6 excluded, 0 unaccounted
- families: composite-panel 1, flowchart-or-schematic 12, heatmap-or-contour 1, line 35, surface-or-3D 7, table-as-figure 3, table-grid 3

1. p2 **flowchart-or-schematic** conf=high panels=1
   bbox [110.55, 485.05, 486.24, 610.24] (?)
   cap: Figure 1 half-pipe
   note: front and back wall of a half-pipe drawn in blue outline in profile view, each wall labelled deck, coping, vert, transition and the floor labelled flat bottom, with HALT-PIPE / VERT RAMP PROFILE VIEW set in the middle: a labelled cross-section, not a plot, so no numeric ticks and the dimension letters are the only printed data
2. p2 **flowchart-or-schematic** conf=high panels=1
   bbox [158.11, 631.94, 438.73, 728.86] (?)
   cap: Figure 2
   note: faint grey dimensioned drawing of the same cross-section with the FIS measures marked W (width), H (height), T (transition), B (flat bottom) and a V arrow at the coping; the drawing is a low-contrast scan pasted whole, which is why the region is an image block rather than vector paths
3. p4 **surface-or-3D** conf=high panels=1
   bbox [199.95, 372.5, 396.9, 519.6] (?)
   cap: Figure 3 the build of Cartesian coordinate
   note: MATLAB 3D axes box with the pipe wall drawn as a colour-mapped wire mesh graded red at the rim to blue at the floor, two red path curves lying on it, and an x/y/z triad floating inside the box: the coordinate conventions the paper uses for every later plot
4. p5 **flowchart-or-schematic** conf=high panels=1
   bbox [173.0, 104.55, 458.85, 220.35] (?)
   cap: Figure 4 shows a simplified outline of our basic model
   note: six-node flow diagram of the model in blue outline: rounded boxes for course shape and v, ellipses for f, path and Vertical Air, a diamond for snowboarder, joined by plain arrows; the only printed text is the node names, so there are no numbers or axes
5. p5 **surface-or-3D** conf=high panels=1
   bbox [173.54, 301.74, 423.69, 466.83] (?)
   cap: Figure 5 is the yield of our study in the following part of this artical. Here, we use it to help give an overview of our model.
   note: same 3D pipe mesh as Figure 3 but with the whole cycle drawn on it: red curve along the wall and floor for the ride, then a green parabola leaving the coping and a blue parabola for the airborne leg without air drag
6. p6 **composite-panel** conf=high panels=3
   bbox [186.03, 354.54, 411.05, 522.92] (?)
   cap: Figure 6 Force Analysis
   note: three panels joined by the two cyan arrows: the upper panel is the 3D pipe mesh with the force vectors N, mg and f and the velocity v drawn on the rider, and the two lower panels are zooms of the same corner in the x-y and y-z projections; the lower two are measured as their own regions and are excluded here as fragments of this exhibit
7. p9 **flowchart-or-schematic** conf=high panels=1
   bbox [182.9, 124.65, 413.52, 284.54] (?)
   cap: Figure 7 the path and force analysis of the fly
   note: side view of the airborne leg: a pale parabola from launch to landing on the slope, with the velocity resolved into Vy and Vz, gravity mg drawn downward, the air-drag arrow, the vertical air H marked by a bracket and the slope angle theta set at the landing point
8. p11 **flowchart-or-schematic** conf=high panels=1
   bbox [198.65, 76.92, 398.0, 207.47] (?)
   cap: Figure 8
   note: rider carried as a stick figure at the coping with the angular momentum Lz0 shown as the usual circled cross, the friction arrows f1 and f2 resolved at the board, mg through the mass point, and the trajectory of the mass point drawn out as a curve; the x/y/z triad sits at the right
9. p12 **flowchart-or-schematic** conf=high panels=1
   bbox [221.59, 136.37, 375.2, 288.43] (?)
   cap: Figure 9
   note: trick sketch for the beginner twist: rider as a small body on the board inside the pipe cross-section, x/y/z triad at the upper left, a long straight axis of rotation line and short arrows at the board; line art with no numeric axes
10. p12 **flowchart-or-schematic** conf=high panels=1
   bbox [195.28, 417.96, 401.23, 552.83] (?)
   cap: Figure 10
   note: second trick sketch: the triad is centred, Lz is drawn as one arrow and the boarder as a white ball, with the axis of rotation running down to the left and the pipe profile set at the right
11. p13 **flowchart-or-schematic** conf=high panels=3
   bbox [158.15, 264.12, 438.1, 394.67] (?)
   cap: Figure 11
   note: three stacked trick sketches sharing one caption: the Flip 1 stage closes p12, and the Twist and Flip 2 stages are the two sketches on p13, with an open down-arrow chaining them; both uncaptioned stages are excluded as fragments of this exhibit, so panel_count 3 counts the sequence rather than this region
12. p14 **flowchart-or-schematic** conf=high panels=1
   bbox [228.87, 291.54, 366.44, 414.07] (?)
   cap: Figure 12
   note: cross-section of the pipe drawn with a dashed measuring grid over a colour-graded ramp outline, annotated width across the top, depth down the inside and flat along the floor, over the title Shape of ramp surface
13. p14 **heatmap-or-contour** conf=medium panels=2
   bbox [90.0, 575.04, 504.8, 723.34] (?)
   cap: Figure 13
   note: two colour-field panels joined by a hollow double arrow: the left one paints the ramp cross-section in rainbow bands under dotted axes and names ramp and path, the right one is a dense rainbow field with the red curve tau(x) drawn over it and the relation z = z(tau(x)) set inside the panel; no colour bar on either panel, which is why the family is read from the banded fields rather than from a key
14. p15 **surface-or-3D** conf=high panels=1
   bbox [209.74, 336.81, 400.19, 483.89] (?)
   cap: Figure 14 shows the output figure of numerical simulation which represents the path of the snowboarder on the ramp and in the air.
   note: numerical-simulation output: the pipe mesh in perspective with the computed trajectory drawn as a red curve on the wall that turns green once airborne; numeric ticks print on all three axes, no legend and no colour bar
15. p18 **flowchart-or-schematic** conf=high panels=2
   bbox [195.53, 93.88, 401.05, 237.18] (?)
   cap: Figure 15
   note: two stick-figure riders drawn against a thin vertical axis, arms out on the left and tucked on the right, with circular arrows over each head and a thick blue arrow labelled w between them: the posture change that adds to the initial angular momentum, drawn as a pair of sketches with no axes
16. p19 **flowchart-or-schematic** conf=medium panels=1
   bbox [60.35, 85.75, 541.2, 398.75] (?)
   cap: Figure 16 complete schema of model
   note: the whole model as one dependency diagram: about twenty ellipses for quantities (vert, shape of transition, flat, fly time, Ereach, angular momentum and so on) and four boxes for decisions (shape, practical, vertical air, total degree of rotation) joined by blue arrows, two of them edge-labelled best choice and conservation of energy; recorded as a schematic because the caption calls it a schema and the arrows carry no process order, though a node-link reading is defensible, hence medium confidence
17. p20 **surface-or-3D** conf=high panels=1
   bbox [221.95, 95.93, 430.71, 257.61] (?)
   cap: Figure 17
   note: 3D mesh of the pipe with a bright green closed loop rising well above the sheet and two red marked curves on it, one along the valley and one bending up at the right end: the search space of Analysis 1 drawn in the same MATLAB view as the earlier surfaces
18. p21 **table-as-figure** conf=high panels=1
   bbox [84.38, 103.22, 536.86, 198.86] (?)
   cap: 
   note: four-column key/value grid drawn with ruled borders and no header row: W(width) 15m and H(height) 3.5m on the first row, B(length of flat bottom) 5m and theta 18 degrees on the second, zt(location of start point of Fly) 10m and Transition Shape Standard ellipse on the third; recorded as table-as-figure because the lane's table-grid block needs a header row and this grid has none, and because the same grid recurs on p27 with the title Default Values
19. p21 **line** conf=high panels=1
   bbox [135.01, 256.34, 280.77, 370.43] (?)
   cap: Figure 18 By simulating with numerical method with W (width of ramp) varying from 10 to 25, we can find the wider the ramp is, the faster the snowboarder can speed up before the fly and, consequently, the larger “Vertical Air” is.
   note: left panel of Figure 18: blue line through nine black square markers, panel title relationship between width & VA_f, x axis width 10-25, y axis VA_f 5.5-8.5, rising and flattening; the panel titles, not letters, are what identify the two panels
20. p21 **line** conf=high panels=1
   bbox [321.62, 256.87, 467.47, 370.66] (?)
   cap: Figure 18 By simulating with numerical method with W (width of ramp) varying from 10 to 25, we can find the wider the ramp is, the faster the snowboarder can speed up before the fly and, consequently, the larger “Vertical Air” is.
   note: right panel of Figure 18: blue line through black square markers, panel title relationship between width & Eleave, x axis width 10-25, y axis Eleave 6700-7600, falling almost linearly
21. p21 **line** conf=high panels=1
   bbox [326.89, 497.54, 476.84, 612.94] (?)
   cap: Figure 19 relationship between “vertical air” vs. height (left) and velocity along y axis vs. height(right)
   note: right panel of Figure 19: blue line through black square markers, panel title relationship between height & Velocity_y, x axis height 2-20, y axis 10.5-13.5, peaking near height 15
22. p21 **line** conf=high panels=1
   bbox [135.35, 497.57, 285.54, 613.14] (?)
   cap: Figure 19 relationship between “vertical air” vs. height (left) and velocity along y axis vs. height(right)
   note: left panel of Figure 19: blue line through black square markers, panel title relationship between height & VerticalAir, x axis height 2-20, y axis 5.5-9.5, rising then flat and slightly declining after height 16
23. p22 **line** conf=high panels=1
   bbox [323.95, 120.8, 471.76, 236.55] (?)
   cap: Figure 20
   note: right panel of Figure 20: panel title relationship between flat & Eleave, x axis flat 0-6, y axis Eleave 7150-7400, straight decreasing line
24. p22 **line** conf=high panels=1
   bbox [134.96, 121.13, 282.77, 236.55] (?)
   cap: Figure 20
   note: left panel of Figure 20: panel title relationship between flat & VA_f, x axis flat 0-6, y axis VA_f 6.0-6.8, straight increasing line
25. p22 **line** conf=high panels=1
   bbox [134.96, 433.12, 282.76, 548.54] (?)
   cap: Figure 21
   note: left panel of Figure 21: panel title relationship between theta & VA_f, x axis theta 0-45, y axis VA_f 4-12, bending upward
26. p22 **line** conf=high panels=1
   bbox [323.63, 434.89, 469.56, 548.84] (?)
   cap: Figure 21
   note: right panel of Figure 21: panel title relationship between theta & Eleave, x axis theta 0-45, y axis Eleave 5000-10000, nearly straight rising line
27. p23 **line** conf=high panels=1
   bbox [115.92, 85.09, 275.79, 209.83] (?)
   cap: Figure 22 relationship between “vertical air” v.s. Zt(left) and between 𝐸𝑙𝑒𝑎𝑣𝑒 v.s. Zt (right)
   note: left panel of Figure 22: panel title relationship between zlength & VA, thick blue curve through black square markers, x axis zlength 0-15, y axis VA 4-10, peaking near zlength 2-3 then falling to 4.2
28. p23 **line** conf=high panels=1
   bbox [319.59, 88.48, 475.17, 210.32] (?)
   cap: Figure 22 relationship between “vertical air” v.s. Zt(left) and between 𝐸𝑙𝑒𝑎𝑣𝑒 v.s. Zt (right)
   note: right panel of Figure 22: panel title relationship between zlength & Eleave, x axis zlength 0-15, y axis Eleave 5000-8500, rising almost linearly
29. p24 **flowchart-or-schematic** conf=high panels=1
   bbox [91.5, 78.19, 512.49, 440.21] (?)
   cap: 
   note: unnumbered six-box method chart: Define Controling Points, Generate sampling points convex curves, Define Gene, Define Fitness-Function, Gene-Algorithm, Optimize curve, each a grey box with a white title tab and bullet lines, stacked in reading order with no connectors; the gene-algorithm design that Figure 23 then reports, printed as a body exhibit without a caption
30. p25 **line** conf=high panels=1
   bbox [114.63, 230.32, 177.74, 345.74] (?)
   cap: Figure 23 Result of optimizing transition shape using Gene Algorithm
   note: first of the four axis boxes making up panel (a) of Figure 23: the blue initial generation of curves in a V shape, x -10 to 10, y 0 to -3.5; the region is one sub-axis of the panel, whose letter (a) prints under the pair
31. p25 **line** conf=high panels=1
   bbox [197.66, 230.32, 261.1, 345.74] (?)
   cap: Figure 23 Result of optimizing transition shape using Gene Algorithm
   note: second axis box of panel (a): the fitness curve of the initial generation, x 0-100, y 0-0.1, rising then dropping at the right edge
32. p25 **line** conf=high panels=1
   bbox [303.62, 230.32, 366.73, 345.74] (?)
   cap: Figure 23 Result of optimizing transition shape using Gene Algorithm
   note: first axis box of panel (b): the same V family of curves in blue with the selected red curve among them
33. p25 **line** conf=high panels=1
   bbox [386.65, 230.32, 450.09, 345.74] (?)
   cap: Figure 23 Result of optimizing transition shape using Gene Algorithm
   note: second axis box of panel (b): the fitness readings of the finished generation, a dense bank of light-blue vertical strokes, x 0-100, y 0-0.025
34. p25 **line** conf=high panels=1
   bbox [285.04, 403.18, 467.36, 552.08] (?)
   cap: Figure 23 Result of optimizing transition shape using Gene Algorithm
   note: panel (d) of Figure 23: a raster screenshot inside an otherwise vector figure, grey background, dashed ellipse with a thick red arc and two red plus markers, x -6 to 6, y -3 to 3: the fitted curve against the ellipse
35. p25 **line** conf=high panels=1
   bbox [100.58, 452.95, 277.43, 527.47] (?)
   cap: Figure 23 Result of optimizing transition shape using Gene Algorithm
   note: panel (c) of Figure 23: the optimised pipe profile as one thin curve running along the bottom and curling up at both ends, x -6 to 6, y 0 to -0.3; the panel letter prints above the caption rather than under the plot
36. p26 **surface-or-3D** conf=high panels=1
   bbox [209.83, 170.14, 392.8, 311.69] (?)
   cap: Figure 24 global optimized result of the shape of course for largest “vertical air”
   note: panel (a) of Figure 24: 3D wire mesh of the optimised course with the red ride curve on the surface and the green airborne arch rising out of it
37. p26 **line** conf=high panels=1
   bbox [166.5, 366.35, 285.94, 460.26] (?)
   cap: Figure 24 global optimized result of the shape of course for largest “vertical air”
   note: panel (b) of Figure 24: the cross-section of the optimised course as a thin dashed U curve, x -8 to 8, y -0.5 to -3.0
38. p26 **line** conf=high panels=1
   bbox [319.71, 370.16, 434.53, 460.65] (?)
   cap: Figure 24 global optimized result of the shape of course for largest “vertical air”
   note: panel (c) of Figure 24: the optimal curve fitted with an ellipse, the dashed ellipse with the thick red arc and small red plus markers over it, panel title Ellipse Fitting of Optimal Shape of Course
39. p27 **table-as-figure** conf=high panels=1
   bbox [84.38, 312.65, 549.22, 409.73] (?)
   cap: 
   note: the Default Values grid printed again, this time with its title line: W(width) 18m is absent here, the rows are W 15m / H 3.5m, B 5m / theta 18 degrees, zt 10m / Transition Shape Standard ellipse; the measured box starts at the title and carries all three rows
40. p27 **line** conf=high panels=1
   bbox [114.66, 489.99, 261.25, 605.41] (?)
   cap: 
   note: panel (a) of Figure 25, whose caption prints on p28: panel title relationship between width & FlyTime/s, blue curve through black square markers, y axis FlyTime/s about 2.5-3.0; the x tick labels fall below the measured box
41. p27 **line** conf=high panels=1
   bbox [303.12, 489.99, 450.92, 605.41] (?)
   cap: 
   note: panel (b) of Figure 25: panel title relationship between flat & FlyTime/s, blue curve through black square markers, same y range, x ticks below the box
42. p28 **line** conf=high panels=1
   bbox [113.98, 89.93, 261.92, 205.35] (?)
   cap: Figure 25 Effects on “air time” by width(a), flat length(b), 𝑍𝑡 points before fly(c), height(d) and gradient angle 𝜃 (e)
   note: panel (c) of Figure 25: panel title relationship between zlength & FlyTime/s, blue curve through markers, x axis zlength 0-15, peaking near zlength 4 then falling to 2.58
43. p28 **line** conf=high panels=1
   bbox [303.14, 89.93, 451.08, 205.35] (?)
   cap: Figure 25 Effects on “air time” by width(a), flat length(b), 𝑍𝑡 points before fly(c), height(d) and gradient angle 𝜃 (e)
   note: panel (d) of Figure 25: panel title relationship between height & FlyTime/s, x axis height 2-6, rising monotonically
44. p28 **line** conf=high panels=1
   bbox [114.48, 260.36, 264.83, 378.35] (?)
   cap: Figure 25 Effects on “air time” by width(a), flat length(b), 𝑍𝑡 points before fly(c), height(d) and gradient angle 𝜃 (e)
   note: panel (e) of Figure 25: panel title relationship between theta & FlyTime/s, x axis theta 0-45, y axis 2.0-4.5, convex rising curve
45. p29 **table-as-figure** conf=high panels=1
   bbox [84.38, 196.82, 551.02, 276.89] (?)
   cap: 
   note: the same key/value grid for the recommended course, rows W(width) 18m / H(height) 3.5m, B 5m / theta 18 degrees, zt 10m / Transition Shape To Be Optimized; the measured box starts below the title and the first row, so the table is taller than the region the geometry pass found
46. p29 **line** conf=high panels=1
   bbox [114.63, 337.4, 261.07, 460.98] (?)
   cap: Figure 26 The optimized shape of ramp cross-section for angular momentum (left) and fitting the shape with 2nd order curve (right)
   note: left panel of Figure 26: the optimised cross-section for angular momentum as a thin dashed U curve, x -8 to 8, y 0 to -3.5
47. p29 **line** conf=high panels=1
   bbox [302.98, 340.87, 449.91, 461.39] (?)
   cap: Figure 26 The optimized shape of ramp cross-section for angular momentum (left) and fitting the shape with 2nd order curve (right)
   note: right panel of Figure 26: panel title Ellipse Fitting of Optimal Shape of Course for Angular Momentum, dashed ellipse with a thick red arc and one red plus marker; the panel title says ellipse while the caption says second order curve
48. p30 **surface-or-3D** conf=high panels=1
   bbox [301.25, 136.4, 451.75, 252.81] (?)
   cap: Figure 27 The optimized shape of ramp cross-section for total degree of rotation (left) and the course of optimal pipe and the path of snowboarder (right)
   note: right panel of Figure 27: the 3D course mesh with the green airborne arch and the red ride curve, the same MATLAB rendering as Figure 24 panel (a)
49. p30 **line** conf=high panels=1
   bbox [114.29, 136.73, 261.07, 252.14] (?)
   cap: Figure 27 The optimized shape of ramp cross-section for total degree of rotation (left) and the course of optimal pipe and the path of snowboarder (right)
   note: left panel of Figure 27: the optimised cross-section for total degree of rotation as a thin dashed U curve with no panel title, x -8 to 8, y 0 to -3.5
50. p30 **line** conf=high panels=1
   bbox [227.92, 356.15, 367.89, 466.29] (?)
   cap: Figure 28 fitting the result with 2nd order curve
   note: single plot titled Ellipse Fitting of Optimal Shape of Course for Total Degree of Rotation: faint dashed ellipse, thick red arc and one red plus marker over it, plus a short blue segment along the floor, x -8 to 4, y -4 to 3
51. p31 **surface-or-3D** conf=high panels=1
   bbox [118.16, 228.16, 309.21, 367.59] (?)
   cap: Figure 29 global eclectically optimal results
   note: panel (a) of Figure 29: 3D wire mesh of the hybrid optimum with the green arch and the red ride curve, ticks -10 to -50 on one floor axis and -5 to 5 on the other
52. p31 **line** conf=high panels=1
   bbox [363.16, 231.74, 520.58, 362.55] (?)
   cap: Figure 29 global eclectically optimal results
   note: panel (b) of Figure 29: the optimal cross-section judged by the eclectic score, a single thin dashed U curve on ruled gridlines, x -8 to 8, y 0 to -3.5
53. p31 **line** conf=high panels=1
   bbox [157.54, 416.44, 479.76, 588.17] (?)
   cap: Figure 29 global eclectically optimal results
   note: panel (c) of Figure 29: the four optimal curves overplotted in one frame with the legend box inside at the upper right keying Vertical Air, Total Degree, Hybrid Scoring, Fit 1 and Fit 2, axes x -8 to 6, y -4 to 3; this is the only figure in the paper with a legend
54. p32 **line** conf=high panels=1
   bbox [143.21, 570.55, 283.7, 721.02] (?)
   cap: 
   note: width pair, left half: panel title width Vs Ereach, x axis width 13-18, y axis Ereach 1.32-1.39 with a x10^4 exponent tag, straight decreasing line; the caption Figure 30 prints under the p33 half of this six-panel exhibit, not here
55. p32 **line** conf=high panels=1
   bbox [326.2, 570.55, 466.37, 720.7] (?)
   cap: 
   note: width pair, right half: panel title width Vs VerticalAir, x axis width 13-18, y axis 9.0-9.9, straight increasing line; no panel letters anywhere in Figure 30
56. p33 **line** conf=high panels=1
   bbox [147.43, 90.35, 283.7, 234.68] (?)
   cap: Figure 30
   note: height pair, left half of the 2x2 block: panel title height Vs Ereach, x axis height 1-6, y axis 1.30-1.44 with the x10^4 tag, decreasing straight line
57. p33 **line** conf=high panels=1
   bbox [330.43, 90.35, 466.37, 234.68] (?)
   cap: Figure 30
   note: height pair, right half: panel title height Vs VerticalAir, x axis height 1-6, y axis 8.2-10.2, increasing curve through markers
58. p33 **line** conf=high panels=1
   bbox [147.43, 274.48, 283.7, 424.62] (?)
   cap: Figure 30
   note: flat pair, left half: panel title flat Vs Ereach, x axis flat 0-6, y axis 1.355-1.405 with the x10^4 tag, decreasing straight line
59. p33 **line** conf=high panels=1
   bbox [330.43, 274.48, 466.37, 424.62] (?)
   cap: Figure 30
   note: flat pair, right half: panel title flat Vs VerticalAir, x axis flat 0-6, y axis 9.0-9.45, increasing straight line

## tables
1. p3 table-grid bbox [61.44, 633.7, 529.9, 760.54]
   cap: 
2. p15 table-grid bbox [84.38, 627.58, 529.78, 742.78]
   cap: 
3. p16 table-grid bbox [84.38, 274.85, 511.06, 372.41]
   cap: 

## excluded
- p4 split-across-pages bbox [61.44, 72.0, 529.9, 322.13] continuation of the Parameters table begun on p3: the force and energy symbols N, f, m, theta, delta-h, Elost, Hf, Whuman, WG, alpha, beta, rho and the xt family, in the same four-column grid with no repeated header row; counted once, at p3
- p6 fragment-of-other bbox [366.3, 556.0, 440.0, 734.9] right-hand zoom of the Figure 6 corner in the y-z projection, counted as the third panel of that exhibit
- p6 fragment-of-other bbox [122.0, 557.1, 247.3, 715.05] left-hand zoom of the Figure 6 corner in the x-y projection, counted as the second panel of that exhibit
- p12 fragment-of-other bbox [189.32, 638.52, 407.47, 769.07] Flip 1 stage of the three-sketch Figure 11 sequence, whose caption prints under the second sketch on p13; counted as panel 1 of that exhibit
- p13 fragment-of-other bbox [168.38, 105.7, 428.43, 225.5] Twist stage of the Figure 11 sequence that the caption below it covers; counted as panel 2 of that exhibit
- p27 not-an-exhibit bbox [88.58, 274.85, 506.85, 301.37] single line of bold body text, 1) Optimize total duration of fly, measured only because it is set in a wide boxed run; a numbered sub-heading of the results section, not a figure or a formula block

## distillation fields

figure 1 p2: sec=未编号标题 Summary [other] zone=middle order=1/1 area=0.094 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=2 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 1']
  caption: Figure N words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p2: sec=未编号标题 Summary [other] zone=bottom order=2/2 area=0.054 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=2 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 2']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p4: sec=未编号标题 Assumptions [other] zone=middle order=3/1 area=0.058 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=4 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 3']
  caption: Figure N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p5: sec=未编号标题 Assumptions [other] zone=top order=4/1 area=0.066 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=5 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 4']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p5: sec=未编号标题 Assumptions [other] zone=middle order=5/2 area=0.082 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=5 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 5']
  caption: Figure N words=27 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p6: sec=未编号标题 Assumptions [other] zone=middle order=6/1 area=0.076 solo=False
  family=composite-panel panels=3 layout=1+2 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=6 lead=0 count=2 read=1 gap=0 pattern=parenthetical style=['Figure 6', 'figure 6']
  caption: Figure N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p9: sec=未编号标题 Assumptions [other] zone=top order=7/1 area=0.074 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=1 count=2 read=1 gap=1 pattern=direct style=['Figure 7']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p11: sec=未编号标题 Assumptions [other] zone=top order=8/1 area=0.052 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=0 count=3 read=1 gap=0 pattern=direct style=['Figure 8', 'figure 8']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p12: sec=未编号标题 Assumptions [other] zone=top order=9/1 area=0.047 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=12 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 9']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p12: sec=未编号标题 Assumptions [other] zone=middle order=10/2 area=0.055 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=12 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 10']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p13: sec=未编号标题 Assumptions [other] zone=middle order=11/1 area=0.073 solo=False
  family=flowchart-or-schematic panels=3 layout=column of 3 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=13 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 11']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p14: sec=未编号标题 Assumptions [other] zone=middle order=12/1 area=0.034 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p14: sec=未编号标题 Assumptions [other] zone=bottom order=13/2 area=0.123 solo=False
  family=heatmap-or-contour panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p15: sec=未编号标题 Assumptions [other] zone=middle order=14/1 area=0.056 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=23 sent=1 units=False vars=0 cond=False concl=True voice=none pos=below

figure 15 p18: sec=2 Total degree of rotation 𝚯 [other] zone=top order=15/1 area=0.059 solo=False
  family=flowchart-or-schematic panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=17 lead=1 count=1 read=1 gap=1 pattern=direct style=['Figure 15']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p19: sec=2 Total degree of rotation 𝚯 [other] zone=top order=16/1 area=0.3 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=19 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 16']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p20: sec=2 Total degree of rotation 𝚯 [other] zone=top order=17/1 area=0.067 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=20 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 17']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p21: sec=7 Eleave 7200 [other] zone=top order=18/1 area=0.086 solo=False
  family=table-as-figure panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p21: sec=7 Eleave 7200 [other] zone=middle order=19/2 area=0.033 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=21 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 18']
  caption: Figure N words=42 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 20 p21: sec=7 Eleave 7200 [other] zone=middle order=20/3 area=0.033 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=21 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 18']
  caption: Figure N words=42 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 21 p21: sec=7 Eleave 7200 [other] zone=middle order=21/4 area=0.035 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=21 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 19']
  caption: Figure N words=16 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 22 p21: sec=7 Eleave 7200 [other] zone=middle order=22/5 area=0.035 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=21 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 19']
  caption: Figure N words=16 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 23 p22: sec=7 Eleave 7200 [other] zone=top order=23/1 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 20']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 24 p22: sec=7 Eleave 7200 [other] zone=top order=24/2 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 20']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 25 p22: sec=7 Eleave 7200 [other] zone=middle order=25/3 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 21']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 26 p22: sec=7 Eleave 7200 [other] zone=middle order=26/4 area=0.033 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 21']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 27 p23: sec=7 Eleave 7200 [other] zone=top order=27/1 area=0.04 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=23 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 22']
  caption: Figure N words=13 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 28 p23: sec=7 Eleave 7200 [other] zone=top order=28/2 area=0.038 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=23 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 22']
  caption: Figure N words=13 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 29 p24: sec=7 Eleave 7200 [other] zone=top order=29/1 area=0.304 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 30 p25: sec=7 Eleave 7200 [other] zone=middle order=33/1 area=0.015 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 23']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 31 p25: sec=7 Eleave 7200 [other] zone=middle order=33/2 area=0.015 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 23']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 32 p25: sec=7 Eleave 7200 [other] zone=middle order=33/3 area=0.015 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 23']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 33 p25: sec=7 Eleave 7200 [other] zone=middle order=33/4 area=0.015 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 23']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 34 p25: sec=7 Eleave 7200 [other] zone=middle order=34/5 area=0.054 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 23']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 35 p25: sec=7 Eleave 7200 [other] zone=middle order=35/6 area=0.026 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 23']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 36 p26: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=top order=36/1 area=0.052 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=26 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 24']
  caption: Figure N words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 37 p26: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=37/2 area=0.022 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=26 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 24']
  caption: Figure N words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 38 p26: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=38/3 area=0.021 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=26 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 24']
  caption: Figure N words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 39 p27: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=39/1 area=0.09 solo=False
  family=table-as-figure panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 40 p27: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=41/2 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=28 lead=-1 count=1 read=1 gap=1 pattern=direct style=['Figure 25']
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 41 p27: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=41/3 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=28 lead=-1 count=1 read=1 gap=1 pattern=direct style=['Figure 25']
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 42 p28: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=top order=43/1 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 25']
  caption: Figure N words=18 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 43 p28: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=top order=43/2 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 25']
  caption: Figure N words=18 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 44 p28: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=44/3 area=0.035 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 25']
  caption: Figure N words=18 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 45 p29: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=top order=45/1 area=0.075 solo=False
  family=table-as-figure panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 46 p29: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=46/2 area=0.036 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=29 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 26']
  caption: Figure N words=21 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 47 p29: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=47/3 area=0.035 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=29 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 26']
  caption: Figure N words=21 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 48 p30: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=top order=48/1 area=0.035 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=30 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 27']
  caption: Figure N words=26 sent=1 units=True vars=0 cond=False concl=False voice=none pos=below

figure 49 p30: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=top order=49/2 area=0.034 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=30 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 27']
  caption: Figure N words=26 sent=1 units=True vars=0 cond=False concl=False voice=none pos=below

figure 50 p30: sec=0 Ellipse Fitting for Optimal Shape of Course [other] zone=middle order=50/3 area=0.031 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=30 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 28']
  caption: Figure N words=9 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 51 p31: sec=2 Hybrid Scoring [other] zone=middle order=51/1 area=0.053 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=31 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 29']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 52 p31: sec=2 Hybrid Scoring [other] zone=middle order=52/2 area=0.041 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=31 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 29']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 53 p31: sec=2 Hybrid Scoring [other] zone=middle order=53/3 area=0.11 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=31 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 29']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 54 p32: sec=2 Hybrid Scoring [other] zone=bottom order=55/1 area=0.042 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=32 lead=0 count=2 read=1 gap=0 pattern=as-shown-in style=['Figure 30']
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 55 p32: sec=2 Hybrid Scoring [other] zone=bottom order=55/2 area=0.042 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=32 lead=0 count=2 read=1 gap=0 pattern=as-shown-in style=['Figure 30']
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 56 p33: sec=2 Hybrid Scoring [other] zone=top order=57/1 area=0.039 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=32 lead=1 count=2 read=1 gap=1 pattern=as-shown-in style=['Figure 30']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 57 p33: sec=2 Hybrid Scoring [other] zone=top order=57/2 area=0.039 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=32 lead=1 count=2 read=1 gap=1 pattern=as-shown-in style=['Figure 30']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 58 p33: sec=2 Hybrid Scoring [other] zone=middle order=59/3 area=0.041 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=32 lead=1 count=2 read=1 gap=1 pattern=as-shown-in style=['Figure 30']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 59 p33: sec=2 Hybrid Scoring [other] zone=middle order=59/4 area=0.041 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=32 lead=1 count=2 read=1 gap=1 pattern=as-shown-in style=['Figure 30']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p3: sec=未编号标题 Assumptions [other] zone=bottom order=60/1 area=0.119 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=4 width=full orient=portrait cont=True

table 2 p15: sec=未编号标题 Assumptions [other] zone=bottom order=60/2 area=0.102 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x6 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 3 p16: sec=1 The direction of velocity [other] zone=middle order=60/1 area=0.083 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x5 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

