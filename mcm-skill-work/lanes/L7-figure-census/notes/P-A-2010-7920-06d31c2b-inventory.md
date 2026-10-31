# P-A-2010-7920-06d31c2b — figure census

- layout sha `7f42e33bc75ce524`, 24 pages, 18 measured regions
- accounted: 9 figures, 0 tables, 9 excluded, 0 unaccounted
- families: flowchart-or-schematic 3, line 5, surface-or-3D 1

1. p6 **flowchart-or-schematic** conf=high panels=1
   bbox [316.1, 116.35, 568.2, 186.25] (?)
   cap: Figure 1
   note: bat outline with five upward force arrows and the ball beneath it; the label sits under the drawing, not over it
2. p6 **flowchart-or-schematic** conf=high panels=1
   bbox [323.95, 209.77, 576.05, 288.95] (?)
   cap: Figure 2
   note: same bat outline with a large curved rotation arrow and the words Center of Mass under the barrel
3. p9 **line** conf=high panels=1
   bbox [271.05, 352.85, 528.23, 527.81] (?)
   cap: Final Speeds at Given Distance from Pivot
   note: single curve of v_f against b, peak at b about 0.55 m; title inside the frame, Graph A tag at the right edge; axis titles v_f | m/s, b | m
4. p15 **flowchart-or-schematic** conf=high panels=3
   bbox [378.0, 79.5, 537.98, 135.85] (?)
   cap: Figure 3
   note: three-frame line drawing: circle, intermediate ellipse, elongated ellipse, joined by two arrows; the quadrupole deformation sequence
5. p17 **surface-or-3D** conf=high panels=1
   bbox [145.5, 214.8, 468.34, 444.55] (?)
   cap: Sweet Spot due to Initial Velocities
   note: box-framed 3D grid: v (MPH) up the back axis, omega along the front axis, 0-60 on both; one shaded region marks the admissible combinations; no colour bar, shading is a flat fill
6. p18 **line** conf=high panels=1
   bbox [109.5, 176.0, 383.64, 361.88] (?)
   cap: Final Speed vs. Bat Mass
   note: one rising straight line, v_f 53.48-53.54 over M 0.88-0.92 kg
7. p18 **line** conf=high panels=1
   bbox [116.1, 531.32, 396.31, 715.68] (?)
   cap: Final Speed vs. Initial Bat Velocity
   note: one rising straight line, v_f 53-57 over V_i 30-45 m/s
8. p19 **line** conf=high panels=1
   bbox [109.5, 277.08, 419.5, 476.62] (?)
   cap: Final Speed vs. Moment of Inertia
   note: one near-flat rising line, v_f 53.3-53.7 over I 0.18-0.22 kg m2
9. p20 **line** conf=high panels=1
   bbox [109.5, 72.0, 425.02, 272.64] (?)
   cap: Final Speed vs. Initial Ball Velocity
   note: one rising straight line, v_f 44-52 over v_i 32-42 m/s; y origin shifted to 44 so the slope fills the frame

## excluded
- p7 not-an-exhibit bbox [249.17, 575.47, 410.83, 618.67] displayed equation, momentum, angular momentum and restitution
- p8 not-an-exhibit bbox [231.41, 412.85, 381.31, 452.83] displayed equation, solved expression for b
- p9 not-an-exhibit bbox [218.09, 195.62, 393.19, 223.94] displayed equation, v_f solved as a fraction
- p9 not-an-exhibit bbox [208.73, 636.22, 402.91, 666.58] displayed equation, derivative set to zero
- p10 not-an-exhibit bbox [231.41, 102.02, 381.31, 141.98] displayed equation, square-root form
- p10 not-an-exhibit bbox [172.22, 443.69, 440.35, 480.43] displayed equation, numeric substitution
- p12 not-an-exhibit bbox [225.29, 582.55, 385.99, 608.59] displayed equation, same form as the first v_f expression
- p13 not-an-exhibit bbox [217.49, 169.22, 393.67, 208.22] displayed equation, nested fraction
- p17 not-an-exhibit bbox [163.94, 621.43, 447.31, 674.98] displayed equation, wide bracketed fraction

## distillation fields

figure 1 p6: sec=5 Model A- Center of Percussion: Physics’ Sweet Spot [model] zone=top order=1/1 area=0.036 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=6 lead=0 count=2 read=1 gap=0 pattern=parenthetical style=['Figure 1']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p6: sec=5 Model A- Center of Percussion: Physics’ Sweet Spot [model] zone=top order=2/2 area=0.041 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=6 lead=0 count=1 read=1 gap=0 pattern=parenthetical style=['Figure 2']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p9: sec=6 Model B: Brody Power Model [model] zone=middle order=3/1 area=0.093 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=1 read=0 gap=0 pattern=direct style=['Graph A']
  caption: none words=7 sent=1 units=False vars=0 cond=True concl=False voice=none pos=above

figure 4 p15: sec=7 Discussion [evaluation] zone=top order=4/1 area=0.019 solo=False
  family=flowchart-or-schematic panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=15 lead=0 count=3 read=1 gap=0 pattern=direct style=['Figure 3']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p17: sec=8 Sensitivity Analysis [sensitivity] zone=middle order=5/1 area=0.153 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=17 lead=0 count=2 read=1 gap=0 pattern=direct style=['Graph B']
  caption: none words=6 sent=1 units=False vars=0 cond=True concl=False voice=none pos=above

figure 6 p18: sec=8 Sensitivity Analysis [sensitivity] zone=top order=6/1 area=0.105 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=1 gap=0 pattern=direct style=['Graph C']
  caption: none words=5 sent=2 units=True vars=0 cond=True concl=False voice=none pos=above

figure 7 p18: sec=8 Sensitivity Analysis [sensitivity] zone=bottom order=7/2 area=0.107 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=1 gap=0 pattern=direct style=['Graph D']
  caption: none words=6 sent=2 units=True vars=0 cond=True concl=False voice=none pos=above

figure 8 p19: sec=8 Sensitivity Analysis [sensitivity] zone=middle order=8/1 area=0.128 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=1 read=1 gap=0 pattern=direct style=['Graph E']
  caption: none words=6 sent=2 units=True vars=0 cond=True concl=False voice=none pos=above

figure 9 p20: sec=8 Sensitivity Analysis [sensitivity] zone=top order=9/1 area=0.131 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=19 lead=1 count=1 read=1 gap=0 pattern=direct style=['Graph F']
  caption: none words=6 sent=2 units=True vars=0 cond=True concl=False voice=none pos=above

