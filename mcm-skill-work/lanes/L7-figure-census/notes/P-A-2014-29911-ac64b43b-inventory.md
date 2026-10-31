# P-A-2014-29911-ac64b43b — figure census

- layout sha `f987e52c293f06fb`, 40 pages, 53 measured regions
- accounted: 24 figures, 5 tables, 24 excluded, 0 unaccounted
- families: flowchart-or-schematic 4, line 13, scatter 4, surface-or-3D 3, table-grid 5

1. p5 **flowchart-or-schematic** conf=high panels=1
   bbox [121.56, 72.48, 472.8, 151.08] (raster)
   cap: Figure 1. Illustration of "Keep-Right-Except-To-Pass" Rule
   note: The keep-right-except-to-pass rule drawn as a two-lane cell strip, two rows of ten cells with the row labels 'Left lane' and 'Right lane' at the left, some cells filled light blue and one right-pointing arrow in the left lane. No numbers, no scale, no legend; the row labels are the only annotation [geometry.printed_numbers].
2. p6 **flowchart-or-schematic** conf=high panels=1
   bbox [189.0, 135.84, 411.6, 291.96] (raster)
   cap: Figure 2. Representation of the "Particle-Hopping" Model
   note: The same two-lane cell strip with eight blue filled circles as cars above it, a curved lane-change arrow and a straight forward arrow: the paper's particle-hopping picture. No numbers and no legend; the left/right lane row labels carry the only text.
3. p11 **line** conf=high panels=1
   bbox [163.44, 79.56, 431.64, 270.24] (raster)
   cap: Figure 3. Relationship of Traffic Flow 𝑄 and Vehicle Density 𝑛
   note: One peaked curve of traffic flow against density, single series with round markers on a solid orange line, peak near n = 0.2 and a tail to n = 0.9. Both axes are numbered (x 0 to 1 by 0.2, y 0 to 1.4 by 0.2), horizontal gridlines only, and the legend sits OUTSIDE the frame at the right with a single entry left in Chinese, '系列2', in an otherwise English figure. An in-figure title 'Traffic Flow Q against Vehicle density n' sits above the artwork [geometry.legend].
4. p12 **line** conf=high panels=1
   bbox [172.56, 92.04, 421.92, 250.68] (raster)
   cap: Figure 4. Relationship of Safety Index 𝛼𝑠𝑎𝑓𝑒 and Vehicle Density 𝑛 (lower is safer)
   note: The safety index against density: one peaked curve with round markers, peak about 0.30 near n = 0.18, x 0 to 1 by 0.2 and y 0 to 0.35 by 0.05, no gridlines, the same single Chinese legend entry outside at the right.
5. p13 **line** conf=high panels=1
   bbox [153.48, 267.96, 441.36, 442.8] (raster)
   cap: Figure 5. Relationship of Energy Consumption 𝐸0 and Vehicle Density 𝑛 (lower is better)
   note: Energy consumption against density: one monotone-rising curve that flattens after n = 0.4 with a small dip near n = 0.7, y 0 to 1000 by 100, same outside legend and same single series.
6. p14 **line** conf=high panels=1
   bbox [153.6, 403.08, 441.48, 591.6] (raster)
   cap: Figure 6. Optimal Maximum Velocity (Light Traffic)
   note: Phi against maximum velocity for light traffic: one rising series with round markers at integer Vmax from 1 to 6, saturating after Vmax = 3 at about 0.69, x 0 to 7 by 1 and y 0 to 0.8 by 0.1, faint gridlines both ways, legend INSIDE at the centre right. The artwork's own title says 'phi against maximum velocity V_max (light traffic)' - the caption's word 'optimal' is not drawn anywhere on the figure [caption.verbatim].
7. p15 **line** conf=high panels=1
   bbox [158.88, 72.84, 434.4, 250.2] (raster)
   cap: Figure 7. Optimal Maximum Velocity (Heavy Traffic)
   note: The heavy-traffic twin: flat near 0.55 to Vmax = 2, a steep rise to about 0.90 at Vmax = 3 and a slow decline after, y 0 to 1 by 0.1. The drawn curve carries two extra vertices near Vmax 2.5 and 3.5 that have no marker, so the path is not simply the marked points joined.
8. p15 **line** conf=high panels=1
   bbox [144.0, 359.64, 443.88, 549.0] (raster)
   cap: Figure 8. Optimal Maximum Velocity (combined)
   note: The combined case: phi rising to a plateau of about 0.72 from Vmax = 3, y 0 to 0.8 by 0.1. The prose reads the optimum off this panel as Vmax = 5, which is where the plateau is first flat rather than where a maximum sits, and the combined peak (0.72) sits between the light (0.69) and heavy (0.90) panels rather than bracketing them.
9. p16 **scatter** conf=high panels=1
   bbox [131.16, 552.96, 292.8, 714.6] (raster)
   cap: Figure 9. Visualization at Low Density
   note: The left panel of the low-density visualisation: a sparse cloud of black dots forming thin diagonal streaks on white, no frame, no axes, no ticks and no labels of any kind. The text layer says the left subfigure is the left lane and the right subfigure the right lane, but the artwork carries no lane label, so the pairing is fixed by the measured x positions - this region starts at x = 165 against the other's x = 496 [geometry.panel_count].
10. p16 **scatter** conf=high panels=1
   bbox [301.8, 552.6, 463.8, 714.6] (raster)
   cap: 
   note: The right panel of Figure 9: the same dot-streak construction, visibly denser and more banded than the left panel. No axes, no legend, no printed numbers. Caption and citation are carried on the left panel only [caption.verbatim].
11. p17 **scatter** conf=high panels=1
   bbox [121.56, 84.0, 291.48, 254.04] (raster)
   cap: Figure 10. Visualization at High Density
   note: The left panel of the high-density visualisation: a near-saturated black dot field with dark streaks and thin white gaps filling the frame, no axes and no labels. Left panel fixed by x = 146 against the other's x = 496 [geometry.panel_count].
12. p17 **scatter** conf=high panels=1
   bbox [301.56, 84.0, 472.56, 255.0] (raster)
   cap: 
   note: The right panel of Figure 10: the same saturated dot texture with a different streak orientation. Caption and citation sit on the left panel [caption.verbatim].
13. p19 **line** conf=high panels=1
   bbox [172.2, 527.76, 422.76, 704.52] (raster)
   cap: Figure 11. The Relationship of Traffic Flow 𝑄 and Average Density 𝜌̅
   note: Three flow-density curves over average density, with critical points annotated in place - (rho_d1, q_d1), (rho_u1, q_u1) and the matching pair for the second lane - plus arrows on the x axis marking rho_c1, rho_c2, rho_c3 and rho_c, so `data_labels` is true. The fast lane is solid, the slow lane dashed and the average flow dash-dotted, keyed in a three-entry legend INSIDE the frame at the upper right. The x axis is 'Average density rho-bar/(veh/m)' 0 to 0.14 by 0.02 and the y axis 'Flow/(veh/s)' 0 to 0.6 by 0.1.
14. p21 **surface-or-3D** conf=high panels=2
   bbox [207.0, 81.96, 362.4, 242.04] (raster)
   cap: Figure 12. Low Density(Jam First Appeared on Fast Lane)
   note: Two stacked 3-D mesh surfaces of density against distance and time, panel (a) above panel (b), with a single diagonal jam ridge in (a). Axes: 'Density/(veh/m)' 0 to 0.10 up the vertical, 'x/km' 0 to 30 receding and 't/min' 0 to 100 to the right. The prose says (a) is the fast lane and (b) the slow lane; the panels carry only the letters [geometry.three_d].
15. p21 **surface-or-3D** conf=high panels=2
   bbox [219.48, 282.0, 375.48, 443.28] (raster)
   cap: Figure 13. Low Density(Jam First Appeared on Slow Lane)
   note: The same pair of 3-D meshes for the mirror case: (a) carries a mild local disturbance at low x and (b) stays nearly flat, the same three axes and the same absence of a legend.
16. p21 **surface-or-3D** conf=high panels=2
   bbox [216.48, 590.76, 378.36, 762.0] (raster)
   cap: Figure 14. Normal or Higher Density
   note: The third of the continuum triple: both panels show strong periodic stop-and-go waves. This is the exhibit whose caption does not print with it - 'Figure 14. Normal or Higher Density' opens p22 - so the art sits on p21 and the caption a page later [caption.position].
17. p24 **line** conf=high panels=1
   bbox [155.28, 217.44, 439.8, 398.28] (raster)
   cap: Figure 15. Traffic Flow under Different Traffic Rules
   note: Traffic flow against density for the three rules: three marker-and-line series in blue, orange and grey, keyed inside at the right middle as 'free driving & free overtaking', 'keep-right-except-to-pass' and 'slow-cars-to-right', converging near density 0.25. x 0 to 0.35 by 0.05, y 0 to 1.4 by 0.2, in-figure title above the artwork.
18. p25 **line** conf=high panels=1
   bbox [162.48, 95.4, 432.48, 267.12] (raster)
   cap: Figure 16. Safety Index under Different Traffic Rules (lower is safer)
   note: The same three rules for the safety index: three colour-coded curves peaking around density 0.2, x 0 to 0.35, y 0 to 0.35 by 0.05, legend inside right.
19. p25 **line** conf=high panels=1
   bbox [153.0, 522.6, 440.4, 722.76] (raster)
   cap: Figure 17. Average Energy Consumption under Different Traffic Rules (lower is better)
   note: The same three rules for energy consumption: three well-separated rising curves at high density, x 0 to 0.35, y 0 to 1800 by 200, legend inside right. This panel's y axis tops out at 1800 where the later Figure 21 uses 2000, a typesetting difference between the two comparison sets rather than a contradiction in the data.
20. p27 **flowchart-or-schematic** conf=high panels=1
   bbox [181.24, 209.62, 416.81, 506.31] (vector)
   cap: Figure 18. "Median" Illustration
   note: The 'Median' rule as a decision flowchart: a start box 'Determine the speed of the kth car', a diamond 'V(k)=Vmedian?', two further diamonds ('Generate a random number in [0, 1]' and 'V(k)>Vmedian'), two action boxes ('Stay on left lane except blocked...' and 'Stay on right lane except blocked...') and 'End', with the branch conditions <0.5 and >0.5 printed on the connectors. The layout pass returns six further regions on p27 that are the individual label blocks of this same drawing, so the flowchart is one row here and those six are excluded `fragment-of-other` [geometry.panel_count].
21. p28 **line** conf=high panels=1
   bbox [160.2, 81.96, 433.8, 252.0] (vector)
   cap: Figure 19. Relationship of Traffic Flow and Vehicle Density
   note: Traffic flow against density with the median optimisation switched on and off: two nearly overlapping curves, 'Equipped' in blue and 'Not Equipped' in dark red, x 0 to 0.4 by 0.1 and y 0 to 1.5 by 0.5, legend inside right. The in-figure title wraps over two lines where the p24 and p25 titles do not.
22. p28 **line** conf=high panels=1
   bbox [152.52, 312.96, 440.52, 492.96] (vector)
   cap: Figure 20. Relationship of Safety Index and Vehicle Density (lower is safer)
   note: The safety-index pair: 'Not Equipped' lying above 'Equipped' and the two converging near density 0.1, x 0 to 0.4 and y 0 to 0.35 by 0.05, legend inside right.
23. p28 **line** conf=high panels=1
   bbox [138.48, 552.0, 453.96, 724.44] (vector)
   cap: Figure 21. Relationship of Average Energy Consumption and Vehicle Density (lower is better)
   note: The energy-consumption pair, effectively superimposed and rising to about 1600, y 0 to 2000 by 500 with the axis label wrapped over three lines - the only panel in the paper whose ordinate label needs three.
24. p29 **flowchart-or-schematic** conf=high panels=1
   bbox [151.56, 363.0, 442.56, 441.6] (raster)
   cap: Figure 22. Illustration of Online Algorithm
   note: A horizontal strip of equal cells with a few filled light blue, an ellipsis at each end and a single arrow pointing down into one cell - the gapless car flow the prose points at. The measured region catches the occupancy band only: the crop is cut off at its top edge, so the illustration extends beyond what the layout pass measured, and no cell carries a label or a number [geometry.printed_numbers].

## tables
1. p6 table-grid bbox [83.9, 402.65, 510.45, 765.94]
   cap: Table 1. Definition of Notation in "Particle-Hopping" Model
2. p7 table-grid bbox [83.9, 583.39, 510.45, 623.62]
   cap: Table 2. The Rule of Acceleration and Deceleration
3. p8 table-grid bbox [83.9, 72.0, 510.45, 335.21]
   cap: Table 3. The Basic Rules
4. p8 table-grid bbox [83.9, 374.21, 500.26, 432.05]
   cap: Table 4. The Rule of Lane Changing corresponding to the “rightmost” rule
5. p8 table-grid bbox [83.9, 717.34, 500.49, 757.54]
   cap: Table 5. Monte Carlo Procedures

## excluded
- p7 split-across-pages bbox [83.9, 72.0, 510.45, 195.98] The last four rows of Table 1 (Pd, Pc, n, N) continuing from p6 with no header repeat and closing with the table's bottom rule. Counted as part of Table 1, not as a second table.
- p9 split-across-pages bbox [84.62, 123.26, 500.5, 170.06] One band of Table 5 on p9: the remainder of the Input cell, the Output row and Steps 1 to 18 of the Monte Carlo procedure. Counted as part of Table 5, which is recorded once on its p8 region.
- p9 split-across-pages bbox [84.62, 240.98, 500.5, 272.21] One band of Table 5 on p9: the remainder of the Input cell, the Output row and Steps 1 to 18 of the Monte Carlo procedure. Counted as part of Table 5, which is recorded once on its p8 region.
- p9 split-across-pages bbox [84.62, 409.85, 500.5, 456.67] One band of Table 5 on p9: the remainder of the Input cell, the Output row and Steps 1 to 18 of the Monte Carlo procedure. Counted as part of Table 5, which is recorded once on its p8 region.
- p9 split-across-pages bbox [84.62, 476.47, 500.5, 523.27] One band of Table 5 on p9: the remainder of the Input cell, the Output row and Steps 1 to 18 of the Monte Carlo procedure. Counted as part of Table 5, which is recorded once on its p8 region.
- p9 split-across-pages bbox [84.62, 582.79, 500.5, 613.99] One band of Table 5 on p9: the remainder of the Input cell, the Output row and Steps 1 to 18 of the Monte Carlo procedure. Counted as part of Table 5, which is recorded once on its p8 region.
- p27 fragment-of-other bbox [260.64, 208.02, 342.96, 248.37] A single label block of the Figure 18 flowchart - the start terminal, the 'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' comparison, or one of the two 'Apply rule' boxes. The complete drawing is the one vector region on p27 that Figure 18 is recorded from.
- p27 fragment-of-other bbox [263.95, 258.81, 339.65, 299.16] A single label block of the Figure 18 flowchart - the start terminal, the 'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' comparison, or one of the two 'Apply rule' boxes. The complete drawing is the one vector region on p27 that Figure 18 is recorded from.
- p27 fragment-of-other bbox [198.19, 291.56, 280.98, 344.73] A single label block of the Figure 18 flowchart - the start terminal, the 'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' comparison, or one of the two 'Apply rule' boxes. The complete drawing is the one vector region on p27 that Figure 18 is recorded from.
- p27 fragment-of-other bbox [319.78, 292.99, 405.41, 345.21] A single label block of the Figure 18 flowchart - the start terminal, the 'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' comparison, or one of the two 'Apply rule' boxes. The complete drawing is the one vector region on p27 that Figure 18 is recorded from.
- p27 fragment-of-other bbox [182.1, 386.51, 297.07, 464.83] A single label block of the Figure 18 flowchart - the start terminal, the 'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' comparison, or one of the two 'Apply rule' boxes. The complete drawing is the one vector region on p27 that Figure 18 is recorded from.
- p27 fragment-of-other bbox [304.64, 386.51, 420.08, 464.83] A single label block of the Figure 18 flowchart - the start terminal, the 'V(k)=Vmedian?' diamond, the random-draw diamond, the 'V(k)>Vmedian' comparison, or one of the two 'Apply rule' boxes. The complete drawing is the one vector region on p27 that Figure 18 is recorded from.
- p32 not-an-exhibit bbox [84.38, 520.63, 510.7, 755.74] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p33 not-an-exhibit bbox [84.38, 72.0, 510.7, 416.21] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p33 not-an-exhibit bbox [84.38, 431.81, 510.7, 698.14] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p33 not-an-exhibit bbox [84.38, 729.34, 510.7, 761.5] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p34 not-an-exhibit bbox [84.38, 72.0, 510.7, 759.46] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p35 not-an-exhibit bbox [84.38, 72.0, 510.7, 759.46] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p36 not-an-exhibit bbox [84.38, 72.0, 510.7, 494.23] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p36 not-an-exhibit bbox [84.38, 509.83, 510.7, 760.54] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p37 not-an-exhibit bbox [84.38, 72.0, 510.7, 759.46] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p38 not-an-exhibit bbox [84.38, 72.0, 510.7, 759.46] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p39 not-an-exhibit bbox [84.38, 72.0, 510.7, 759.46] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.
- p40 not-an-exhibit bbox [84.38, 72.0, 510.7, 665.86] A band of the appendix C++ source listing (gen.h, SaveBMP.h, lane.h, CA.cpp and the driver). Typed code, not an exhibit: no caption, no figure or table number and no artwork.

## distillation fields

figure 1 p5: sec=1 Introduction [introduction] zone=top order=1/1 area=0.055 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=4 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 1']
  caption: Figure N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p6: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.1 Model Establishment [model] zone=top order=2/1 area=0.069 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=6 lead=0 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 2']
  caption: Figure N. words=7 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p11: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=top order=8/1 area=0.102 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=11 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 3']
  caption: Figure N. words=9 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p12: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=top order=9/1 area=0.079 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=11 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 4']
  caption: Figure N. words=12 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p13: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=middle order=10/1 area=0.1 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 5']
  caption: Figure N. words=13 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p14: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=middle order=11/1 area=0.108 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=14 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 6', 'Figure 7']
  caption: Figure N. words=7 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p15: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=top order=12/1 area=0.098 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=14 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 7']
  caption: Figure N. words=7 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p15: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=middle order=13/2 area=0.113 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=15 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 8']
  caption: Figure N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p16: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=bottom order=14/1 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=16 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 9', 'Figure 10']
  caption: Figure N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p16: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=bottom order=15/2 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 9', 'Figure 10']
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p17: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=top order=16/1 area=0.058 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=16 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 10']
  caption: Figure N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p17: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.3 Model Solution and Analysis [model] zone=top order=17/2 area=0.058 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 10']
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p19: sec=3 Modeling for Right-Most Rule > 3.2 Continuum Modeling for Right-Most Rule > 3.2.2 Model Solution and Analysis [model] zone=bottom order=18/1 area=0.088 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 11']
  caption: Figure N. words=10 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p21: sec=3 Modeling for Right-Most Rule > 3.2 Continuum Modeling for Right-Most Rule > 3.2.2 Model Solution and Analysis [model] zone=top order=19/1 area=0.05 solo=False
  family=surface-or-3D panels=2 layout=2x1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=20 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 12']
  caption: Figure N. words=9 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p21: sec=3 Modeling for Right-Most Rule > 3.2 Continuum Modeling for Right-Most Rule > 3.2.2 Model Solution and Analysis [model] zone=middle order=20/2 area=0.05 solo=False
  family=surface-or-3D panels=2 layout=2x1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=20 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 13']
  caption: Figure N. words=9 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p21: sec=3 Modeling for Right-Most Rule > 3.2 Continuum Modeling for Right-Most Rule > 3.2.2 Model Solution and Analysis [model] zone=bottom order=21/3 area=0.055 solo=False
  family=surface-or-3D panels=2 layout=2x1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=21 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 14']
  caption: Figure N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p24: sec=4 Modeling for Alternative Freeway Traffic Rules > 4.3 Comparison of Different Traffic Rules [other] zone=middle order=22/1 area=0.103 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=24 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 15']
  caption: Figure N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p25: sec=4 Modeling for Alternative Freeway Traffic Rules > 4.3 Comparison of Different Traffic Rules [other] zone=top order=23/1 area=0.093 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=24 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 16']
  caption: Figure N. words=11 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p25: sec=4 Modeling for Alternative Freeway Traffic Rules > 4.3 Comparison of Different Traffic Rules [other] zone=bottom order=24/2 area=0.115 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 17']
  caption: Figure N. words=12 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 20 p27: sec=5 Modeling for Intelligent-System Control [model] zone=middle order=25/1 area=0.14 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=27 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 18']
  caption: Figure N. words=4 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 21 p28: sec=5 Modeling for Intelligent-System Control [model] zone=top order=26/1 area=0.093 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=27 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 19']
  caption: Figure N. words=9 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 22 p28: sec=5 Modeling for Intelligent-System Control [model] zone=middle order=27/2 area=0.103 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=27 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 20']
  caption: Figure N. words=12 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 23 p28: sec=5 Modeling for Intelligent-System Control [model] zone=bottom order=28/3 area=0.109 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=27 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 21']
  caption: Figure N. words=13 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 24 p29: sec=5 Modeling for Intelligent-System Control > 5.2 Possible Further Improvements [other] zone=middle order=29/1 area=0.046 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=29 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 22']
  caption: Figure N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p6: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.1 Model Establishment [model] zone=bottom order=3/2 area=0.309 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=6 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Table 1']
  caption: Table N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 16x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=True

table 2 p7: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.1 Model Establishment [model] zone=bottom order=4/1 area=0.034 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=7 lead=0 count=0 read=1 gap=None pattern=direct style=[]
  caption: Table N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 2x1 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=1 width=full orient=portrait cont=False

table 3 p8: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.1 Model Establishment [model] zone=top order=5/1 area=0.224 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=7 lead=1 count=0 read=1 gap=None pattern=direct style=[]
  caption: Table N. words=5 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x3 header=1 rules=vertical-rules zebra=False merged=True diag=False units_hdr=False dec=False num=0 txt=3 width=full orient=portrait cont=False

table 4 p8: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.1 Model Establishment [model] zone=middle order=6/2 area=0.048 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=7 lead=1 count=0 read=1 gap=None pattern=direct style=[]
  caption: Table N. words=12 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 3x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 5 p8: sec=3 Modeling for Right-Most Rule > 3.1 Discrete Modeling for Right-Most Rule > 3.1.1 Model Establishment [model] zone=bottom order=7/3 area=0.033 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=8 lead=0 count=1 read=1 gap=None pattern=direct style=['Table 5']
  caption: Table N. words=5 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 20x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=True

