# P-A-2010-7586-ff69029f — figure census

- layout sha `f53cc299891841c0`, 15 pages, 23 measured regions
- accounted: 15 figures, 0 tables, 8 excluded, 0 unaccounted
- families: composite-panel 1, flowchart-or-schematic 1, line 13

1. p3 **flowchart-or-schematic** conf=high panels=1
   bbox [189.0, 107.86, 423.01, 458.88] (?)
   cap: Figure 1: Arrows point in the positive direction for the corresponding parameter.
   note: bat drawn as a black rod with three coloured annotation arrows (initial velocity, initial rotation, distance from center of mass)
2. p4 **line** conf=high panels=1
   bbox [165.6, 359.01, 446.41, 546.38] (?)
   cap: Figure 2: vf as a function of l.
   note: one axes, three keys under the x-axis: final velocity / effective mass / swing speed against l
3. p7 **composite-panel** conf=high panels=2
   bbox [74.19, 530.08, 303.51, 702.07] (?)
   cap: Figure 3: Left: An image of a ball hitting a rigid wall.8 The compression is easily visible. Right: A hysteresis curve used in our modeling. The maximum compression here is a very significant 1 cm.
   note: left is a grayscale photo of the ball against the wall, right is the hysteresis loop Force(N) vs Compression(m); the loop is the only figure in the paper with a labelled y-axis at the top right
4. p8 **line** conf=high panels=2
   bbox [92.91, 448.81, 303.51, 568.15] (?)
   cap: Figure 4: Left: The force between the ball and the bat as a function of time. We see that the impulse lasts about 1.4 ms. Right: The waveform of the y10 (t) when the bat is struck at 60 cm. The impulse reaches this chunk at around 0.4 ms, but it does not start moving significantly until later.
   note: left force spike vs time (about 1.4 ms), right bat displacement waveform vs time at the 60 cm strike
5. p9 **line** conf=high panels=2
   bbox [92.91, 107.87, 303.51, 230.86] (?)
   cap: Figure 5: Left: Exit velocity vs. impact position for a free boundary (solid line) and fixed boundary (dashed line). Notice that we are fixing the barrel end and leaving the handle end free in both cases. Right: The same graph for a free 110 cm bat.
   note: left free vs fixed barrel end, right the same sweep for a 110 cm bat; both panels keep their own axes, so the flat zone shows as a rescaled curve rather than a shared-axis continuation
6. p9 **line** conf=high panels=1
   bbox [72.0, 400.33, 540.02, 665.1] (?)
   cap: Figure 6: Exit velocity vs. impact position at various initial angular velocities of the bat. Our model predicts the solid curves, while the dashed lines represent the simple model. The dots are at the points where Brody’s solution is maximized.
   note: seven-ish solid model curves with square markers over descending dotted simple-model curves; two Brody maximum dots sit off the band
7. p10 **line** conf=high panels=2
   bbox [92.91, 203.48, 303.51, 312.99] (?)
   cap: Figure 7: Left: Exit velocity minus impact velocity vs. impact position at various initial angular velocities of the bat. Left: Near the center of mass, higher angular velocity gives higher excess exit velocity, but towards the sweet spot the lines cross and higher angular velocity gives lower exces
   note: excess exit velocity over impact position; left with hysteresis, right without, where the crossing of the curves disappears
8. p10 **line** conf=high panels=1
   bbox [152.52, 413.29, 456.73, 580.61] (?)
   cap: Figure 8: Optimal impact position vs. angular velocity. The line is the rigid-body prediction, while the points are our model’s prediction.
   note: stepped rigid-body line plus square markers for the model optimum, both rising with angular velocity
9. p10 **line** conf=medium panels=1
   bbox [165.6, 647.38, 446.4, 675.46] (?)
   cap: Figure 9: The profile of our bat.
   note: 28 pt tall strip: the bat outline plotted as upper and lower profile curves over 0.84 m, knob wiggle at the left; axes print 0.03 and -0.03, so it is a plotted profile, not a drawing
10. p11 **line** conf=high panels=2
   bbox [92.91, 245.16, 303.51, 383.21] (?)
   cap: Figure 10: Exit velocity vs. impact position for various densities. The solid line is the original ρ = 649 kg/m3 . Left: Dotted is 700, dashed is 1000. Right: Dotted is 640, dashed is 500.
   note: density sweep; solid is the original rho, left panel sweeps up (700 dotted, 1000 dashed), right panel sweeps down (640, 500)
11. p11 **line** conf=high panels=2
   bbox [92.91, 432.03, 303.51, 570.09] (?)
   cap: Figure 11: Left: Varying the value of Y. Solid is Y = 1.1814 × 1010 N/m2 . Dashed is 1.25 times as much. Dotted is 0.8 times. Right: Varying the shape of the bat. Solid is the original shape. Dashed has a thicker handle region while dotted has a narrower handle region.
   note: left Young's modulus at 0.8x/1x/1.25x, right handle thickness varied; same 0.3-0.8 m impact window in both
12. p12 **line** conf=high panels=1
   bbox [165.6, 107.87, 446.4, 287.27] (?)
   cap: Figure 12: Varying the velocity of the ball. Solid is the original 40 m/s. Dashed is 50 m/s while dotted is 30 m/s.
   note: single panel, three curves for 30/40/50 m/s ball speed keyed only in the caption; the measured layout has one region here, so the 'Left:' reading is a caption artefact, not a second panel
13. p12 **line** conf=high panels=2
   bbox [74.19, 429.36, 303.51, 579.7] (?)
   cap: Figure 13: Left: Corked Bat Right: aluminum bat.
   note: left corked bat, right aluminum bat; both plots, two curves each, separate y-axes
14. p13 **line** conf=high panels=2
   bbox [74.19, 107.86, 303.51, 249.13] (?)
   cap: Figure 14: Plots of the displacement of an aluminum bat (dashed) and wood bat (solid) being hit by a ball 60 cm from the handle end. The second diagram shows two frames superimposed (t = 1.05 ms and t = 1.10 ms) to show the motion. The rigid translation and rotation has been removed from the diagram
   note: two animation frames side by side, t=0.5 ms and t=1.05 ms printed inside each panel; aluminum dashed, wood solid
15. p14 **line** conf=high panels=1
   bbox [72.0, 107.87, 540.02, 284.54] (?)
   cap: Figure 15: Exit velocity vs. impact position at different hoop frequencies. The lines from bottom to top at the left edge (color) are: (blue, starts off the chart) wood bat, (red) no hoop mode, (gray) 2000 Hz, (black) 500 Hz, (green) 300 Hz, (brown) 800 Hz, and (purple) 1250 Hz.
   note: seven curves keyed by colour only, no legend box; the caption reads the stack from bottom to top at the left edge

## excluded
- p7 fragment-of-other bbox [308.49, 577.85, 537.81, 702.07] hysteresis loop, right half of Figure 3
- p8 fragment-of-other bbox [308.49, 453.49, 519.09, 568.15] displacement waveform, right half of Figure 4
- p9 fragment-of-other bbox [308.49, 111.24, 519.09, 230.86] 110 cm bat panel, right half of Figure 5
- p10 fragment-of-other bbox [308.49, 203.48, 519.09, 312.99] no-hysteresis panel, right half of Figure 7
- p11 fragment-of-other bbox [308.49, 245.16, 519.09, 383.21] downward density sweep, right half of Figure 10
- p11 fragment-of-other bbox [308.49, 432.03, 519.09, 570.09] bat-shape sweep, right half of Figure 11
- p12 fragment-of-other bbox [308.49, 429.36, 537.81, 579.7] aluminum bat, right half of Figure 13
- p13 fragment-of-other bbox [308.49, 107.86, 537.82, 249.13] t=1.05 ms frame, right half of Figure 14

## distillation fields

figure 1 p3: sec=2 A SIMPLE EXAMPLE [other] zone=middle order=1/1 area=0.169 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=3 lead=0 count=1 read=1 gap=0 pattern=as-shown-in style=['Figure 1']
  caption: Figure N: words=12 sent=1 units=False vars=0 cond=False concl=False voice=active pos=below

figure 2 p4: sec=2 A SIMPLE EXAMPLE [other] zone=middle order=2/1 area=0.109 solo=False
  family=line panels=1 layout=1 shared=False legend=below cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=1 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=2 cond=True concl=False voice=none pos=below

figure 3 p7: sec=3 OUR MODEL > 3.2 Mathematics of Our Model [model] zone=bottom order=3/1 area=0.081 solo=False
  family=composite-panel panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=7 lead=0 count=2 read=1 gap=1 pattern=as-shown-in style=['Figure 3b']
  caption: Figure N: words=35 sent=3 units=True vars=0 cond=False concl=True voice=passive pos=below

figure 4 p8: sec=4 SIMULATION AND ANALYSIS > 4.1 Simulation Results [solution] zone=middle order=4/1 area=0.052 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=8 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 4a', 'Figure 4b']
  caption: Figure N: words=58 sent=4 units=True vars=1 cond=True concl=True voice=active pos=below

figure 5 p9: sec=4 SIMULATION AND ANALYSIS > 4.1 Simulation Results [solution] zone=top order=5/1 area=0.053 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=8 lead=1 count=2 read=1 gap=1 pattern=direct style=['Figure 5a', 'Figure 5b']
  caption: Figure N: words=46 sent=3 units=True vars=0 cond=True concl=False voice=active pos=below

figure 6 p9: sec=4 SIMULATION AND ANALYSIS > 4.1 Simulation Results [solution] zone=bottom order=6/2 area=0.256 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=3 read=1 gap=0 pattern=direct style=['Figure 6']
  caption: Figure N: words=41 sent=3 units=False vars=0 cond=True concl=False voice=active pos=below

figure 7 p10: sec=4 SIMULATION AND ANALYSIS > 4.2 Parameter Space Study [solution] zone=top order=7/1 area=0.048 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=10 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 7a', 'Figure 7b']
  caption: Figure N: words=61 sent=4 units=False vars=0 cond=True concl=True voice=active pos=below

figure 8 p10: sec=4 SIMULATION AND ANALYSIS > 4.2 Parameter Space Study [solution] zone=middle order=8/2 area=0.105 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=22 sent=2 units=False vars=0 cond=True concl=False voice=active pos=below

figure 9 p10: sec=4 SIMULATION AND ANALYSIS > 4.2 Parameter Space Study [solution] zone=bottom order=9/3 area=0.016 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=parenthetical style=['Figure 9']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p11: sec=4 SIMULATION AND ANALYSIS > 4.2 Parameter Space Study [solution] zone=middle order=10/1 area=0.06 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=11 lead=0 count=1 read=0 gap=0 pattern=parenthetical style=['Figure 10']
  caption: Figure N: words=32 sent=4 units=True vars=1 cond=True concl=False voice=active pos=below

figure 11 p11: sec=4 SIMULATION AND ANALYSIS > 4.2 Parameter Space Study [solution] zone=middle order=11/2 area=0.06 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=11 lead=0 count=1 read=1 gap=0 pattern=parenthetical style=['Figure 11']
  caption: Figure N: words=49 sent=7 units=True vars=1 cond=True concl=False voice=active pos=below

figure 12 p12: sec=4 SIMULATION AND ANALYSIS > 4.3 Alternatives to Wooden Bats [solution] zone=top order=12/1 area=0.104 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=11 lead=1 count=1 read=0 gap=0 pattern=parenthetical style=['Figure 12']
  caption: Figure N: words=23 sent=3 units=True vars=0 cond=True concl=False voice=active pos=below

figure 13 p12: sec=4 SIMULATION AND ANALYSIS > 4.3 Alternatives to Wooden Bats [solution] zone=middle order=13/2 area=0.071 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=12 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 13a', 'Figure 13b']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p13: sec=4 SIMULATION AND ANALYSIS > 4.3 Alternatives to Wooden Bats [solution] zone=top order=14/1 area=0.067 solo=False
  family=line panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=12 lead=1 count=1 read=0 gap=0 pattern=direct style=['Figure 14']
  caption: Figure N: words=55 sent=3 units=True vars=1 cond=True concl=False voice=passive pos=below

figure 15 p14: sec=4 SIMULATION AND ANALYSIS > 4.3 Alternatives to Wooden Bats [solution] zone=top order=15/1 area=0.171 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=13 lead=1 count=1 read=0 gap=0 pattern=as-shown-in style=['Figure 15']
  caption: Figure N: words=50 sent=2 units=True vars=0 cond=True concl=False voice=active pos=below

