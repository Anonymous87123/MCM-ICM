# P-B-2011-11759-ee4be862 — figure census

- layout sha `dc651add67a9b17a`, 51 pages, 27 measured regions
- accounted: 22 figures, 5 tables, 0 excluded, 0 unaccounted
- families: flowchart-or-schematic 2, map-or-plan-view 16, node-link-network 4, table-grid 5

1. p6 **flowchart-or-schematic** conf=high panels=1
   bbox [221.05, 355.91, 390.95, 640.91] (?)
   cap: Figure 1 describes this model without reclustering.
   note: rounded boxes joined by arrows: Create and Score Clusters, then Place 1st Repeater (Open), then the decision Enough Users & Channels? whose yes branch reaches End of Method and whose no branch reaches Enough Channels?; a yes there goes to Find Optimal Direction and Place New Repeater (Open) back into the first decision, a no goes to Add Repeater (PL) and back up the left side. Decision nodes are drawn as diamonds, so the shape is a flow chart and not a network
2. p11 **flowchart-or-schematic** conf=high panels=1
   bbox [221.05, 213.35, 390.95, 507.23] (?)
   cap: Figure 2 describes the creation of the backbone and branches.
   note: the branching model's flow chart in the same box-and-diamond style: Create and Score Clusters, Create Backbone Network (Open), Recreate and Rescore Clusters, Connect Highest Score Cluster, then Enough Users? with a no branch looping back to Recreate and Rescore Clusters through Recreate; Enough Channels? ends the method on yes and adds a repeater on no
3. p16 **map-or-plan-view** conf=high panels=1
   bbox [147.6, 366.54, 464.4, 610.95] (?)
   cap: Figure 4: Repeater Placement (Snaking Model)
   note: snaking-model repeater placement over a grey -40..40 mile field: hundreds of small white squares for potential users, red dots for open repeaters, green dots for CTCSS repeaters, black open triangles for k-means cluster points and green solid plus red dashed circles for coverage footprints; the four-entry legend sits inside the bottom of the frame. The frame is geographic (both axes titled Miles), which is why the family is map-or-plan-view and not scatter
4. p17 **node-link-network** conf=high panels=1
   bbox [216.07, 79.32, 387.98, 254.66] (?)
   cap: Figure 5: Repeater Parity (Snaking Model)
   note: repeater parity for the snaking model: eight white circles on a bare white ground, each bearing a plus or a minus, joined by thin straight links into a ring with one interior link; no axes, no frame, no legend, no labels beyond the signs
5. p17 **map-or-plan-view** conf=high panels=1
   bbox [167.4, 386.54, 444.6, 600.74] (?)
   cap: Figure 6: Repeater Placement (Branching Model)
   note: branching-model placement in the same geographic format as Figure 4, but here the repeaters are joined by thin solid black edges that draw the branching tree itself across the grey field; user squares are faint, red dashed coverage circles sit round each open repeater
6. p18 **map-or-plan-view** conf=high panels=1
   bbox [167.4, 74.49, 444.6, 288.69] (?)
   cap: Figure 7: CTCSS Line Placement (Branching Model)
   note: CTCSS line placement for the branching model: the green repeaters carry small printed index numbers (1 to 8) and two families of coverage circles are drawn, red solid and blue solid, to show the shared subaudible channels; the legend sits inside the bottom of the frame
7. p18 **node-link-network** conf=high panels=1
   bbox [241.09, 438.74, 368.24, 582.01] (?)
   cap: Figure 8: Repeater Parity (Branching Model)
   note: branching-model parity, same bare diagram as Figure 5: eight signed circles joined by thin links, here arranged as a long vertical chain with two horizontal runs, no axes and no legend
8. p20 **map-or-plan-view** conf=high panels=1
   bbox [147.6, 74.49, 464.4, 319.29] (?)
   cap: Figure 10: Repeater Placement (Snaking Model)
   note: rural-case snaking placement: the user cloud is grouped into visible clumps, cluster points are marked with black open triangles, and the coverage circles mostly overlap inside the disc; the legend box sits at the bottom left of the frame and overlaps the axis line
9. p20 **node-link-network** conf=high panels=1
   bbox [249.77, 453.18, 363.25, 601.74] (?)
   cap: Figure 11: Repeater Parity (Snaking Model)
   note: rural-case parity for the snaking model: nine signed circles in a ring with one chord, again with no axes, frame or legend
10. p21 **map-or-plan-view** conf=high panels=1
   bbox [147.6, 161.87, 464.4, 405.3] (?)
   cap: Figure 12: Repeater Placement (Branching Model)
   note: rural-case branching placement: branching tree edges drawn over the clumped user field, red dashed and green solid coverage circles, cluster-point triangles; the legend spans nearly the whole frame width along the bottom
11. p21 **map-or-plan-view** conf=high panels=1
   bbox [147.6, 446.26, 464.4, 691.06] (?)
   cap: Figure 13: CTCSS Line Placement (Branching Model)
   note: the CTCSS arrangement for that same branching plan, printed under it: green repeaters numbered 1, 5, 6, 7, 8 with three overlapping families of thin circles (red, blue, orange) marking which repeaters share a channel; one label is overprinted by a circle stroke
12. p22 **node-link-network** conf=high panels=1
   bbox [228.6, 249.12, 395.59, 391.57] (?)
   cap: Figure 14: Repeater Parity (Branching Model)
   note: rural-case branching parity: eight signed circles joined by links, no axes and no legend; the smallest of the four parity diagrams
13. p23 **map-or-plan-view** conf=high panels=1
   bbox [147.6, 74.49, 464.4, 319.29] (?)
   cap: Figure 15: Results for 10,000 Simultaneous Users
   note: the 10,000-user run: the same snaking placement format with a far denser user field, so the white squares fill most of the grey field and the green and red coverage circles are heavily overplotted; no legend is drawn on this figure
14. p24 **map-or-plan-view** conf=high panels=2
   bbox [104.1, 208.09, 507.9, 361.09] (?)
   cap: Figure 16: “Bender” Snaking Model Cluster Point Sensitivity Rural Case
   note: cluster-point sensitivity, two plots side by side, each with its own title: "Bender" Snaking Method Repeater Placement (k=10) on the left and (k=20) on the right. Both panels are the same geographic format, and neither carries a legend inside the region
15. p25 **map-or-plan-view** conf=high panels=2
   bbox [104.1, 84.45, 507.9, 237.45] (?)
   cap: Figure 17: Branching Model Seperation Distance Sensitivity Rural Case
   note: separation-distance sensitivity, two plots side by side titled Branching Method Repeater Placement (d=10) and (d=20): the same grey mile field, red and green repeaters, red dashed circles, but no tree edges and no legend
16. p29 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 116.45, 662.4, 666.37] (?)
   cap: Figure 18: Repeater Placement (Snaking Model)
   note: Appendix A full-page reprint of Figure 4's snaking placement, drawn to the whole page with the same -40..40 mile frame and the four-entry legend along the bottom inside the frame; the artwork repeats Figure 4 but the page carries its own Figure 18 caption, so it is recorded as its own exhibit
17. p30 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 110.88, 662.4, 661.68] (?)
   cap: Figure 19: Repeater Placement (Branching Model)
   note: Appendix A reprint of Figure 6's branching placement, full page, tree edges over the grey user field, legend inside the bottom of the frame
18. p31 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 110.88, 662.4, 661.68] (?)
   cap: Figure 20: CTCSS Line Placement (Branching Model)
   note: Appendix A reprint of Figure 7's CTCSS arrangement, full page: numbered green repeaters and red, blue and orange channel circles; the printed title spells CTCSS as CTCOSS, and two repeaters both carry the label 1
19. p32 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 110.88, 662.4, 661.68] (?)
   cap: Figure 21: Repeater Placement (Snaking Model)
   note: Appendix A reprint of the rural snaking placement (Figure 10), full page: clumped user field, cluster triangles, orange and green circles plus red dashed ones, legend along the bottom
20. p33 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 113.96, 662.4, 661.68] (?)
   cap: Figure 22: Repeater Placement (Branching Model)
   note: Appendix A reprint of the rural branching placement (Figure 12), full page: a long near-vertical tree edge through the middle, green dotted and red dashed circles, legend along the bottom
21. p34 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 110.88, 662.4, 661.68] (?)
   cap: Figure 23: CTCSS Line Placement (Branching Model)
   note: Appendix A reprint of the CTCSS arrangement (Figure 13), full page: numbered green repeaters with thin red, blue and orange circles; the printed title again reads CTCOSS, and the label 1 is printed on four different repeaters
22. p35 **map-or-plan-view** conf=high panels=1
   bbox [-50.4, 110.88, 662.4, 661.68] (?)
   cap: Figure 24: Results for 10,000 Simultaneous Users
   note: Appendix A reprint of the 10,000-user run (Figure 15), full page: the densest user field in the paper with red and green dots almost coincident and circles cut by all four frame edges; unlike the other reprints this one carries no legend, which is why the legend is recorded as none

## tables
1. p7 table-grid bbox [126.6, 450.66, 485.4, 554.57]
   cap: 
2. p12 table-grid bbox [126.6, 246.11, 485.4, 379.71]
   cap: 
3. p16 table-grid bbox [125.25, 111.27, 486.75, 246.86]
   cap: 
4. p24 table-grid bbox [223.52, 613.39, 388.48, 672.77]
   cap: 
5. p25 table-grid bbox [240.43, 437.79, 371.57, 497.17]
   cap: 

## distillation fields

figure 1 p6: sec=4 The “Bender” Snake Model [model] zone=middle order=1/1 area=0.1 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=6 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 1']
  caption: Figure N words=7 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 2 p11: sec=5 The Branching Model [model] zone=middle order=3/1 area=0.103 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=11 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 2']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p16: sec=7 Case Studies > 7.1 City Distribution [other] zone=middle order=6/2 area=0.16 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 4']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p17: sec=7 Case Studies > 7.1 City Distribution [other] zone=top order=7/1 area=0.062 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=17 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 5']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p17: sec=7 Case Studies > 7.1 City Distribution [other] zone=middle order=8/2 area=0.122 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=17 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 6']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p18: sec=7 Case Studies > 7.1 City Distribution [other] zone=top order=9/1 area=0.122 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 7']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p18: sec=7 Case Studies > 7.1 City Distribution [other] zone=middle order=10/2 area=0.038 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 8']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p20: sec=7 Case Studies > 7.2 Rural Distrubition [other] zone=top order=11/1 area=0.16 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=20 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 10']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p20: sec=7 Case Studies > 7.2 Rural Distrubition [other] zone=middle order=12/2 area=0.035 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=20 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 11']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p21: sec=7 Case Studies > 7.2 Rural Distrubition [other] zone=middle order=13/1 area=0.159 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=21 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 12']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p21: sec=7 Case Studies > 7.2 Rural Distrubition [other] zone=bottom order=14/2 area=0.16 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=21 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 13']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p22: sec=7 Case Studies > 7.2 Rural Distrubition [other] zone=middle order=15/1 area=0.049 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 14']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p23: sec=7 Case Studies > 7.2 Rural Distrubition [other] zone=top order=16/1 area=0.16 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=23 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 15']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p24: sec=9 Mountainous Terrain [other] zone=middle order=17/1 area=0.127 solo=False
  family=map-or-plan-view panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=24 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 16']
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p25: sec=10 Sensitivity to Parameters [sensitivity] zone=top order=19/1 area=0.127 solo=False
  family=map-or-plan-view panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 17']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p29: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=21/1 area=0.809 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=29 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 18']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p30: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=22/1 area=0.81 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=30 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 19']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p31: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=23/1 area=0.81 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=31 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 20']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p32: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=24/1 area=0.81 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=32 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 21']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 20 p33: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=25/1 area=0.805 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=33 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 22']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 21 p34: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=26/1 area=0.81 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=34 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 23']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 22 p35: sec=13 Appendix A: Full-Page Plots [appendix] zone=middle order=27/1 area=0.81 solo=True
  family=map-or-plan-view panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=35 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 24']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p7: sec=4 The “Bender” Snake Model > 4.2 Mathematical Interpretation [other] zone=middle order=2/1 area=0.077 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=column orient=portrait cont=False

table 2 p12: sec=5 The Branching Model > 5.2 Mathematical Intepretation [other] zone=middle order=4/1 area=0.099 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 9x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=column orient=portrait cont=False

table 3 p16: sec=7 Case Studies > 7.1 City Distribution [other] zone=top order=5/1 area=0.101 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 9x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=column orient=portrait cont=False

table 4 p24: sec=9 Mountainous Terrain [other] zone=bottom order=18/2 area=0.02 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x3 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=half orient=portrait cont=False

table 5 p25: sec=10 Sensitivity to Parameters [sensitivity] zone=middle order=20/2 area=0.016 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x3 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=half orient=portrait cont=False

