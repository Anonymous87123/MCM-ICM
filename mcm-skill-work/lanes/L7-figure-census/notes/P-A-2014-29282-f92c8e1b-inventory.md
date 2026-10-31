# P-A-2014-29282-f92c8e1b — figure census

- layout sha `9efbbe74b81e6d41`, 30 pages, 33 measured regions
- accounted: 22 figures, 9 tables, 2 excluded, 0 unaccounted
- families: flowchart-or-schematic 11, line 6, scatter 5, table-grid 9

1. p4 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 115.88, 510.23, 247.48] (raster)
   cap: Figure 1: The logic framework of our paper.
   note: The paper's roadmap as a left-to-right box-and-arrow tree on a raster: eleven labelled boxes in three levels, branching into the two rule options and funnelling three performance boxes into a right-hand 'simulation model' box on dashed arrows labelled 'test'. No numbers and no legend; the level labels are the only annotation [geometry.printed_numbers].
2. p7 **flowchart-or-schematic** conf=high panels=1
   bbox [99.21, 518.54, 496.06, 655.28] (raster)
   cap: Figure 2: The choice between following and overtaking(i¡j).
   note: A two-lane road strip drawn as a raster with three yellow car cells in four positions: red arrows branch upward into an overtaking path in the left lane and stay in-lane on a following path, each labelled with its probability, 'probability p(vi-vj)' and 'probability 1-p(vi-vj)', plus a 'forward direction' arrow. The caption itself is corrupted in the text layer - it prints 'overtaking(i¡j)' where the art shows the subscripts vi and vj - and the caption is recorded exactly as printed [caption.verbatim].
3. p9 **line** conf=high panels=1
   bbox [85.04, 344.45, 510.25, 590.97] (raster)
   cap: Figure 3: Proportions of cars in different states after several transitions.
   note: Three marker-and-line series on a fully dotted grid, inside a boxed legend at the upper right: state 3 climbing to 1.0, state 2 decaying from 0.5 and state 1 from 0.2, all flat by roughly the sixth transition. Axes are numbered, x 0 to 20 in steps of 2 and y 0 to 1 in steps of 0.1. The caption promises proportions 'after several transitions' while twenty transitions are plotted [geometry.printed_numbers].
4. p11 **flowchart-or-schematic** conf=high panels=1
   bbox [106.3, 115.88, 488.99, 259.81] (raster)
   cap: Figure 4: Road condition when traffic is heavy.
   note: A congested two-lane road strip: five yellow car cells labelled 'speed:v3' and 'speed:v4', with three dimension brackets each marked 'D' over the safe distance between cars. Drawn art, no photograph, and no numeric scale.
5. p12 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 540.66, 510.26, 664.54] (raster)
   cap: Figure 5: Description of the simulated freeway.
   note: The simulated freeway as a long blue-outlined rectangle split by dashed cell dividers, a hatched entrance cell at the left with an 'arriving cars / entrance' arrow, a cell width labelled 'L' and a spanning arrow above labelled 'S cells (S×L)'. Letters only, no numbers.
6. p14 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 115.88, 510.24, 254.98] (raster)
   cap: Figure 6: The “Go” process.
   note: The 'Go' process: a two-lane strip with the rear and ahead cars adjacent, a short vertical red arrow off the rear car and a red forward arrow off the lead car, and two brackets marked 'D' over the 'no car' gaps. No numbers.
7. p14 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 293.67, 510.23, 410.21] (raster)
   cap: Figure 7: The “Return” process.
   note: The 'Return' process uses the same strip and the same 'D' bracket notation as Figure 6 but mirrors the motion: the vertical red arrow points down and the brackets sit below the lanes. A near-duplicate of Figure 6, not an identical plate [geometry.panel_count].
8. p15 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 150.07, 510.26, 698.41] (raster)
   cap: Figure 8: The general process of the simulation.
   note: A tall vertical decision flowchart, about sixteen nodes in one column with a left-hand feedback loop, carrying an in-figure title 'Flowchart of simulation' at the upper left. Branch exits are lettered Y/N, and the parameter boxes print the actual settings - T=2000, S=1000, p1=0.3, p2=0.7, d=2, t=0, and 2×S - so numbers are printed in this diagram even though no axis exists [geometry.printed_numbers].
9. p16 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 211.99, 510.25, 636.49] (raster)
   cap: Figure 9: Sub flowchart of the “Go” process.
   note: The 'Go' sub-flowchart: eight decision nodes in one column with an in-figure title 'Sub flowchart of “Go” process'. Branch exits are Y/N and the condition boxes print cell expressions such as 'cells(2,i)>cells(2,j)+1' and 'j=i-D...i+D' rather than values, so no numbers are printed [geometry.printed_numbers].
10. p17 **scatter** conf=high panels=1
   bbox [100.52, 379.52, 291.02, 517.52] (raster)
   cap: Figure 10: Danger index vs. λ.
   note: Blue data dots with a red fitted curve: the danger index rises to a hump near 1.45 around λ = 0.15 and then decays to about 0.6. The x axis is 'lambda(vehicles per second)' and the y axis 'Danger index(times per vehicle)', with the legend boxed inside at the upper right. A raster paste, so the dots are pixels rather than vector marks [geometry.family].
11. p17 **scatter** conf=high panels=1
   bbox [304.26, 379.52, 494.76, 517.52] (raster)
   cap: Figure 11: Average traffic speed vs. λ.
   note: The same construction for average speed: blue dots along a red fit decaying from about 4.0 at the low end to an asymptote near 3.33, x 'lambda(vehicles per second)', y 'Average traffic speed(m/s)', legend inside at the upper right.
12. p17 **scatter** conf=high panels=1
   bbox [100.52, 572.15, 291.02, 710.15] (raster)
   cap: Figure 12: Traffic flow vs. λ.
   note: Traffic flow against arrival rate: blue dots tracking a red fit that rises almost linearly from about 0.25 to 1.55, x 'lambda(vehicles per second)', y 'Traffic flow(vehicles per second)', legend inside at the upper left.
13. p17 **scatter** conf=high panels=1
   bbox [304.26, 572.15, 494.76, 710.15] (raster)
   cap: Figure 13: OSL effect vs. λ.
   note: The OSL effect on a red fit that climbs almost straight from about 0.4 to 2.75, y axis titled 'OSL_effect' with the underscore printed literally, legend inside at the upper left.
14. p18 **scatter** conf=high panels=1
   bbox [202.39, 115.88, 392.89, 253.88] (raster)
   cap: Figure 14: USL effect vs. λ.
   note: The USL effect on a red fit rising steadily from about 0.2 to 1.5, y axis 'USL_effect'. This is the only one of the five plots whose caption sits on page 18 with its art, while Figures 10 to 13 are captioned on the same page but drawn a page earlier [mention.lead_pages].
15. p19 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 115.88, 510.24, 215.3] (raster)
   cap: Figure 15: A printscreen of simulation in light traffic, green lines represent cars.
   note: Captioned as a 'printscreen' but drawn as art: a sparse two-lane strip with thin green car bars, nearly all of them in the lower lane, and a red 'forward direction' arrow. No axes, no legend, no numbers [geometry.legend].
16. p19 **flowchart-or-schematic** conf=high panels=1
   bbox [85.04, 344.8, 510.26, 444.9] (raster)
   cap: Figure 16: A printscreen of simulation in heavy traffic, green lines represent cars.
   note: The same strip under heavy traffic: long green car bars packed into both lanes, again with the red 'forward direction' arrow at the right and no axes or legend.
17. p23 **line** conf=high panels=1
   bbox [141.73, 234.96, 453.55, 437.55] (raster)
   cap: Figure 17: A view of evaluation indexes for each traffic rule.
   note: The four rules compared as four closed polylines on a five-spoke radar. No rectilinear axes exist, so the row is recorded under the closest family the lane has - `line`, the same call made for the radar on page 9 of P-A-2022-2209466-5952dd05 - and the radar construction is stated in `other_note` instead of being invented as a family [geometry.family].
18. p26 **flowchart-or-schematic** conf=high panels=2
   bbox [85.04, 530.86, 510.25, 671.68] (raster)
   cap: Figure 18: RHT and LHT traffic systems.
   note: Two four-lane diagrams side by side, drawn as raster art: yellow car boxes with red centre dots and up and down arrows, sub-labelled 'New Rule 2 in LHT' and 'New Rule 2 in RHT', with a four-way direction cross labelled forward/backward/left/right between them instead of a legend. The caption promises 'RHT and LHT traffic systems' and the art illustrates only New Rule 2, with the left-hand panel printed first [geometry.panel_count].
19. p28 **line** conf=high panels=1
   bbox [100.52, 240.78, 291.02, 378.78] (raster)
   cap: Figure 19: Comparison in traffic flow.
   note: Two straight lines comparing the intelligent-driver system against the plain system: blue solid and red dashed, the dashed one slightly higher, ending near 1.58 against 1.50. Axes 'lambda(vehicles per second)' and 'Traffic flow(vehicles per second)', legend inside at the upper left.
20. p28 **line** conf=high panels=1
   bbox [304.26, 240.78, 494.76, 378.78] (raster)
   cap: Figure 20: Comparison in ATS.
   note: The same pair for average speed: two decaying curves, the red dashed above the blue, flattening near 3.45 and 3.32, y axis 'Average traffic speed(m/s)'.
21. p28 **line** conf=high panels=1
   bbox [100.52, 433.41, 291.02, 571.41] (raster)
   cap: Figure 21: Comparison in USL effect.
   note: The USL effect pair: two widely separated straight lines, the red dashed running from about 0.5 to 2.75 well above the blue from 0.18 to 1.5 - the widest gap of the four comparisons.
22. p28 **line** conf=high panels=1
   bbox [304.26, 433.41, 494.76, 571.41] (raster)
   cap: Figure 22: Comparison in OSL effect.
   note: The OSL effect pair: two nearly coincident straight lines from about 0.45 to 2.7, the red dashed only marginally above the blue, which is the closeness the prose remarks on.

## tables
1. p17 table-grid bbox [191.55, 193.12, 399.82, 282.19]
   cap: Table 1: Simulation results.
2. p19 table-grid bbox [116.09, 658.91, 479.18, 746.78]
   cap: Table 2: Sensitivity analysis of the parameter p1 .
3. p20 table-grid bbox [113.16, 137.66, 482.11, 225.53]
   cap: Table 3: Sensitivity analysis of the parameter p2 .
4. p20 table-grid bbox [119.98, 259.47, 475.3, 347.34]
   cap: Table 4: Sensitivity analysis of the parameter d.
5. p21 table-grid bbox [90.63, 637.0, 500.75, 724.47]
   cap: Table 5: Evaluation of the new rules.
6. p23 table-grid bbox [133.14, 135.34, 458.23, 222.81]
   cap: Table 6: Values of the five normalized evaluation indexes.
7. p24 table-grid bbox [114.18, 137.66, 477.19, 254.03]
   cap: Table 7: The meaning of Saaty’s scale for AHP preference.
8. p24 table-grid bbox [117.48, 674.65, 473.89, 704.34]
   cap: Table 8: Values of weights.
9. p25 table-grid bbox [122.98, 137.66, 468.39, 167.35]
   cap: Table 9: Values of the comprehensive evaluation index.

## excluded
- p1 not-an-exhibit bbox [87.74, 72.0, 507.7, 220.3] The summary-sheet form: the 'Team Control Number / For office use only' grid and the 29282 entry in 159 vector paths. A contest-office form, not a paper exhibit, so it carries no caption and no figure number.
- p1 not-an-exhibit bbox [88.58, 241.47, 506.85, 272.57] The summary-sheet title band - the contest name, the team number and the one-line summary heading printed in two vector paths. A ruling line, not an exhibit.

## distillation fields

figure 1 p4: sec=1 Introduction [introduction] zone=top order=1/1 area=0.112 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=3 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 1']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p7: sec=3 The Keep-Right-Except-To-Pass Rule > 3.2 Performance In Light Traffic > 3.2.2 A State Transition Approach [result] zone=bottom order=2/1 area=0.108 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=7 lead=0 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 2']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p9: sec=3 The Keep-Right-Except-To-Pass Rule > 3.2 Performance In Light Traffic > 3.2.3 A Numerical Test And Conclusion [result] zone=middle order=3/1 area=0.209 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 3']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p11: sec=3 The Keep-Right-Except-To-Pass Rule > 3.3 Performance In Heavy Traffic [result] zone=top order=4/1 area=0.11 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=10 lead=1 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 4']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p12: sec=4 A Simulation Model: Cellular Automation > 4.2 Notations [model] zone=bottom order=5/1 area=0.105 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=12 lead=0 count=1 read=1 gap=None pattern=parenthetical style=['Figure 5']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p14: sec=4 A Simulation Model: Cellular Automation > 4.3 Algorithm Descriptions [model] zone=top order=6/1 area=0.118 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 6']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p14: sec=4 A Simulation Model: Cellular Automation > 4.3 Algorithm Descriptions [model] zone=middle order=7/2 area=0.099 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=1 count=1 read=1 gap=None pattern=parenthetical style=['Figure 7']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p15: sec=4 A Simulation Model: Cellular Automation > 4.3 Algorithm Descriptions [model] zone=middle order=8/1 area=0.465 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=13 lead=2 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 8']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p16: sec=4 A Simulation Model: Cellular Automation > 4.3 Algorithm Descriptions [model] zone=middle order=9/1 area=0.36 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=2 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 9']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p17: sec=4 A Simulation Model: Cellular Automation > 4.4 Calculation And Results [result] zone=middle order=11/2 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=-1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 10']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p17: sec=4 A Simulation Model: Cellular Automation > 4.4 Calculation And Results [result] zone=middle order=12/3 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=-1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 11']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p17: sec=4 A Simulation Model: Cellular Automation > 4.4 Calculation And Results [result] zone=bottom order=13/4 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=-1 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 12']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p17: sec=4 A Simulation Model: Cellular Automation > 4.4 Calculation And Results [result] zone=bottom order=14/5 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=-1 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 13', 'Figure 14']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p18: sec=4 A Simulation Model: Cellular Automation > 4.4 Calculation And Results [result] zone=top order=15/1 area=0.052 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 14']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p19: sec=4 A Simulation Model: Cellular Automation > 4.5 Small Conclusion [result] zone=top order=16/1 area=0.084 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=18 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 15']
  caption: Figure N: words=13 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p19: sec=4 A Simulation Model: Cellular Automation > 4.5 Small Conclusion [result] zone=middle order=17/2 area=0.085 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=19 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 16']
  caption: Figure N: words=13 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p23: sec=5 A New Traffic Rule > 5.3 Comparison [evaluation] zone=middle order=23/2 area=0.126 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=22 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 17']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p26: sec=6 Further Topics > 6.1 Applicability In Left-Hand Traffic Countries [result] zone=bottom order=27/1 area=0.119 solo=False
  family=flowchart-or-schematic panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=26 lead=0 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 18']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p28: sec=6 Further Topics > 6.2 Intelligent Traffic > 6.2.2 Simulation And Results [result] zone=middle order=28/1 area=0.052 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 19']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 20 p28: sec=6 Further Topics > 6.2 Intelligent Traffic > 6.2.2 Simulation And Results [result] zone=middle order=29/2 area=0.052 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 20']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 21 p28: sec=6 Further Topics > 6.2 Intelligent Traffic > 6.2.2 Simulation And Results [result] zone=middle order=30/3 area=0.052 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 21']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 22 p28: sec=6 Further Topics > 6.2 Intelligent Traffic > 6.2.2 Simulation And Results [result] zone=middle order=31/4 area=0.052 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=28 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 22']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p17: sec=4 A Simulation Model: Cellular Automation > 4.4 Calculation And Results [result] zone=top order=10/1 area=0.037 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=17 lead=0 count=1 read=1 gap=None pattern=direct style=['Table 1']
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x3 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=False

table 2 p19: sec=4 A Simulation Model: Cellular Automation > 4.6 Sensitivity Analysis [sensitivity] zone=bottom order=18/3 area=0.064 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=0 count=0 read=1 gap=None pattern=direct style=[]
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x6 header=1 rules=booktabs zebra=False merged=True diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 3 p20: sec=4 A Simulation Model: Cellular Automation > 4.6 Sensitivity Analysis [sensitivity] zone=top order=19/1 area=0.065 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=1 count=0 read=1 gap=None pattern=direct style=[]
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x6 header=1 rules=booktabs zebra=False merged=True diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 4 p20: sec=4 A Simulation Model: Cellular Automation > 4.6 Sensitivity Analysis [sensitivity] zone=middle order=20/2 area=0.062 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=1 count=0 read=1 gap=None pattern=direct style=[]
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x6 header=1 rules=booktabs zebra=False merged=True diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 5 p21: sec=5 A New Traffic Rule > 5.2 Simulation Results [result] zone=bottom order=21/1 area=0.072 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=21 lead=0 count=1 read=1 gap=None pattern=direct style=['Table 5']
  caption: Table N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x5 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 6 p23: sec=5 A New Traffic Rule > 5.3 Comparison [evaluation] zone=top order=22/1 area=0.057 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=22 lead=1 count=1 read=1 gap=None pattern=direct style=['Table 6']
  caption: Table N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x5 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 7 p24: sec=5 A New Traffic Rule > 5.3 Comparison [evaluation] zone=top order=24/1 area=0.084 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=23 lead=1 count=1 read=1 gap=None pattern=direct style=['Table 7']
  caption: Table N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 8x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 8 p24: sec=5 A New Traffic Rule > 5.3 Comparison [evaluation] zone=bottom order=25/2 area=0.021 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=24 lead=0 count=1 read=1 gap=None pattern=figure-n-shows style=['Table 8']
  caption: Table N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 2x6 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 9 p25: sec=5 A New Traffic Rule > 5.3 Comparison [evaluation] zone=top order=26/1 area=0.02 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=24 lead=1 count=1 read=1 gap=None pattern=direct style=['Table 9']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 2x5 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

