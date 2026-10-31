# P-B-2012-13955-a0e5e63c — figure census

- layout sha `7300e686bc62129d`, 18 pages, 12 measured regions
- accounted: 7 figures, 4 tables, 1 excluded, 0 unaccounted
- families: flowchart-or-schematic 4, heatmap-or-contour 1, line 2, table-grid 4

1. p7 **flowchart-or-schematic** conf=high panels=1
   bbox [51.4, 427.56, 561.4, 502.68] (vector)
   cap: Figure 2.1: By running the scheduling algorithm we have found that furthest open campsite is campsite 6. The algorithm has found that Groups A, B and C can feasibly reach campsite 6. The priority of each group is calculated, and Group B has the highest priority; thus, we move Group B to campsite 6.
   note: State strip for campsite 6: the furthest open campsite is campsite 6, Groups A, B and C can all reach it, and the strip fills cell 6 orange and cell 2 pale blue with 'Group A P_A = 1.1', 'Group B P_B = 1.5 (moves to campsite 6)' and 'Group C P_C = .8' under the campsites. a full-width two-row strip inside a light frame: the top row prints the header cell 'Campsite #:' followed by the six numbered campsites, the bottom row prints 'Group Assigned:' and holds one text cell per campsite, two of the cells filled pale blue and orange, and a 'Downstream ->' arrow sits at the left edge. No axes and no plotted marks: every value is printed inside its cell.
2. p7 **flowchart-or-schematic** conf=high panels=1
   bbox [51.4, 600.36, 561.4, 674.52] (vector)
   cap: Figure 2.2: As the scheduling algorithm progresses past campsite 6, we find that the next furthest open campsite is campsite 5. The algorithm has calculated that Groups A and C can feasibly reach campsite 5. Since 𝑃! >𝑃! , group A is moved to campsite 5.
   note: The same strip one step later, printed at the foot of p7 with its caption opened on p8: camp 5 is now the furthest open campsite and holds 'Group A P_A = 1.1 (moves to campsite 5)', camp 1 carries the pale-blue cell, camp 6 holds Group B, and two cells read 'Open'. a full-width two-row strip inside a light frame: the top row prints the header cell 'Campsite #:' followed by the six numbered campsites, the bottom row prints 'Group Assigned:' and holds one text cell per campsite, two of the cells filled pale blue and orange, and a 'Downstream ->' arrow sits at the left edge. No axes and no plotted marks: every value is printed inside its cell.
3. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [51.4, 370.92, 579.4, 494.04] (vector)
   cap: Figure 2.3: The furthest open campsite is the campsite that is off of the river. The algorithm finds that Group 𝐷 could move there, but since Group 𝐷 has 𝑡! > 𝑑! , group 𝐷 remains on the river.
   note: The end-of-river strip: campsites 170, 171, an ellipsis, 223, 224 and 'Off the River', with 'Group D: P_D = 1.1, t_D = 12, d_D = 11 (doesn't move off the river)' under campsite 170 and the orange 'Furthest Open Camp Site' cell under 'Off the River'. Caption is the last text on p8. a full-width two-row strip inside a light frame: the top row prints the header cell 'Campsite #:' followed by the six numbered campsites, the bottom row prints 'Group Assigned:' and holds one text cell per campsite, two of the cells filled pale blue and orange, and a 'Downstream ->' arrow sits at the left edge. No axes and no plotted marks: every value is printed inside its cell.
4. p9 **flowchart-or-schematic** conf=high panels=1
   bbox [57.27, 63.6, 555.77, 679.3] (raster)
   cap: Figure 2.4: Visual depiction of scheduling algorithm.
   note: Full-page flowchart titled 'Scheduling Algorithm' with a grey 'Legend' box at the top right listing n, a, d, p, c, G. Rounded boxes run 'Simulation Starts: Start With Campsite at Final Exit' -> 'Find the (next) Empty Campsite Up River From the Input Campsite (Call It c)' -> circle 'Determine Set G' (fed by 'Groups on River' and 'Groups on Waitlist') -> 'Find Group with Highest Priority in the Set G (Call It g)' -> 'Move g to c', with a red diamond 'n = n + 1' carrying the rotated test 'If n = last day of simulation', then 'Return Simulation Results:' branching to three outcome boxes. Green, pale blue, red and grey fills; condition text on the arrows. The caption line prints above the diagram at the top of p9.
5. p11 **line** conf=high panels=1
   bbox [126.52, 63.48, 522.52, 298.92] (vector)
   cap: Figure 3.2: Movement of groups down the river based on Figure 3.1. Groups reach the end of the river on different nights due to varying trip duration parameters. Priority Priority (Figure 3.1) 4.5 4 3.5 3 P1 2.5 2 P2 1.5 P3 1 0.5 P4 0 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 Night Figure 3.
   note: 'Group locations (Figure 3.1)' plot: four thick coloured step polylines, one per group, rising in stairs across Night 0-19 on a printed 0-50 campsite axis with light grey gridlines at every five units; a right-hand legend keys Group 1-4 by colour; axis titles 'Campsite Number' and 'Night'. No markers on the lines.
6. p11 **line** conf=high panels=1
   bbox [128.77, 381.89, 519.52, 606.14] (vector)
   cap: Figure 3.3: Priority values of groups over the course of each trip. Values converge to 𝑃 = 1 due to the algorithm’s attempt to keep groups on schedule.
   note: 'Priority (Figure 3.1)' plot: four thin coloured polylines of priority against Night 0-19, spiky rather than smooth, P1-P4 keyed by a right-hand legend; y axis prints 0 to 4.5 in steps of 0.5 with grey gridlines, axis titles 'Priority' and 'Night'. Values are said to converge to p = 1.
7. p14 **heatmap-or-contour** conf=high panels=1
   bbox [95.02, 63.6, 517.77, 482.19] (raster)
   cap: Figure 4.3: Contour diagram of the best fit surface for data points in Figure 4.2, where contour lines represent peak carrying capacity of the river (M). Notice that the surface has a ridge running along the vertical line R=1:1.
   note: Filled contour plot of the fitted surface: a smooth wash in five colour bands from cream at the top to purple at the bottom, overlaid with five thin grey contour curves labelled 3500, 3000, 2500, 2000 and 1500 at their crests. Y axis prints 100-300 campsites, x axis the five ratio categories 1:4 … 4:1. No legend and no colour bar; the caption names the ridge along R = 1:1.

## tables
1. p10 table-grid bbox [79.0, 248.76, 534.04, 556.2]
   cap: Figure 3.1: Shows each group’s campsite number and priority value for each night spent on the river.
2. p12 table-grid bbox [76.36, 371.88, 536.68, 557.64]
   cap: Figure 4.1: We predict that a maximum of 18 groups can be sent down the river each day. Over the course of the six month season, this amounts to nearly 3000 trips.
3. p13 table-grid bbox [68.68, 334.92, 544.36, 450.84]
   cap: Figure 4.2: Peak carrying capacity with respect to the number of campsites on the river and the ratio of oar powered river rafts to motorized boats launched each day.
4. p15 table-grid bbox [91.24, 229.08, 522.04, 343.8]
   cap: Figure 4.4: Peak carrying capacity of river, M, with respect to D and R.

## excluded
- p16 not-an-exhibit bbox [55.72, 183.24, 557.32, 270.6] measured block holding only the 6.1 heading and one paragraph of running prose about carrying-capacity overestimation; no graphic on it.

## distillation fields

figure 1 p7: sec=2 Methods > 2.2 Priority [other] zone=middle order=1/1 area=0.079 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=54 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p7: sec=2 Methods > 2.2 Priority [other] zone=bottom order=2/2 area=0.078 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=43 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p8: sec=2 Methods > 2.3 Priorities & Other Considerations [other] zone=middle order=3/1 area=0.134 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=32 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p9: sec=2 Methods > 2.3 Priorities & Other Considerations [other] zone=middle order=4/1 area=0.633 solo=True
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p11: sec=3 Scheduling Simulation [solution] zone=top order=6/1 area=0.192 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=94 sent=4 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p11: sec=3 Scheduling Simulation [solution] zone=middle order=7/2 area=0.181 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=27 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p14: sec=4 Case Study > 4.2 Sensitivity Analysis of Carrying Capacity With Respect to R and Y [sensitivity] zone=middle order=10/1 area=0.365 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=13 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 4.3']
  caption: Figure N: words=41 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p10: sec=3 Scheduling Simulation [solution] zone=middle order=5/1 area=0.289 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=18 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 20x9 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=5 width=full orient=portrait cont=False

table 2 p12: sec=4 Case Study > 4.1 The Grand Canyon [other] zone=middle order=8/1 area=0.176 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=32 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 11x5 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 3 p13: sec=4 Case Study > 4.2 Sensitivity Analysis of Carrying Capacity With Respect to R and Y [sensitivity] zone=middle order=9/1 area=0.114 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=13 lead=0 count=2 read=2 gap=None pattern=direct style=['Figure 4.2']
  caption: Figure N: words=29 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x6 header=2 rules=boxed zebra=False merged=True diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 4 p15: sec=4 Case Study > 4.3 Sensitivity Analysis of Carrying Capacity With Respect to R and D [sensitivity] zone=middle order=11/1 area=0.102 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=15 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 4.4']
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x5 header=2 rules=vertical-rules zebra=False merged=True diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

