# P-B-2011-9440-95f0fa40 — figure census

- layout sha `180c63c3de2aaa82`, 41 pages, 54 measured regions
- accounted: 15 figures, 10 tables, 29 excluded, 0 unaccounted
- families: flowchart-or-schematic 3, line 2, map-or-plan-view 2, node-link-network 3, photo-or-raster-image 1, scatter 4, table-grid 10

1. p7 **flowchart-or-schematic** conf=high panels=1
   bbox [175.1, 150.7, 420.25, 351.95] (raster)
   cap: Figure 1. An illustration about the reachable repeaters of u1. The circle centered at u1 is the communication of u1 with radius r.
   note: one user u1, the circle of radius r around it and the repeaters inside that circle; a geometry diagram rather than a plotted data set
2. p16 **flowchart-or-schematic** conf=high panels=1
   bbox [90.0, 337.8, 505.1, 586.2] (raster)
   cap: Figure 2: The solution consisted of 12 repeaters arranged in a cellular network. The blue circle denotes the considered area with radius 40miles, the read regular hexagons represent the cellular network, and the blue points in the centers of the regular hexagons denote the positions of repeaters.
   note: twelve repeater points on the centres of a regular hexagon grid inside the 40-mile circle; raster paste
3. p18 **flowchart-or-schematic** conf=high panels=1
   bbox [133.45, 357.1, 461.9, 664.55] (raster)
   cap: Figure 3: The solution consisted of 108 repeaters arranged in a cellular network. The blue circle denotes the considered area with radius 40miles, the red regular hexagons represent the cellular network. The repeaters are also lay in the centers of the regular hexagons (not shown).
   note: 108-repeater hexagonal cellular network as vector hexagons with the 40-mile circle inscribed; no plotted data
4. p19 **scatter** conf=high panels=1
   bbox [152.71, 153.16, 443.11, 412.52] (vector)
   cap: Figure 4: Illustration of an initial configuration with 30 repeaters. The coordinates of each repeater are generated randomly inside the considered area.
   note: 30 labelled repeater sites R1-R30 on a unitless -40..40 frame
5. p19 **map-or-plan-view** conf=medium panels=1
   bbox [150.76, 463.76, 445.17, 726.08] (vector)
   cap: Figure 5: The resulted Voronoi diagram corresponding to the configuration shown in Fig. 4.
   note: the same 30 sites with the Voronoi partition drawn as unfilled polygon edges: the ink is a planar subdivision, not a set of markers
6. p20 **scatter** conf=high panels=1
   bbox [135.16, 278.11, 460.82, 568.58] (vector)
   cap: Figure 6: The circumscribed circles of the Voronoi areas, corresponding to the ones shown in Fig. 5. The circumscribed circles are colored in green while the Voronoi areas are colored in red. Notice that, for the some repeaters close to the edge of the considered area, their Voronoi areas may contai
   note: the same configuration with the circumscribed circle of every Voronoi area and the centres marked; markers and circles over a bare coordinate frame
7. p21 **scatter** conf=medium panels=1
   bbox [115.26, 244.61, 480.79, 570.8] (vector)
   cap: Figure 7: The black asterisks stand for the locations of repeaters, the red ones represent the centers of the circumscribed circles, and the black arrows show the directions towards which the repeaters will move. This illustration corresponds to the result shown in Fig. 6.
   note: circles plus one annotation arrow per site showing the direction of movement
8. p22 **node-link-network** conf=high panels=1
   bbox [151.16, 140.11, 444.82, 394.38] (vector)
   cap: Figure 8: The red asterisks represent the repeaters while a green line connecting two repeaters if they have the chance to transmit signals (i.e., within a distance R).
   note: 21 repeater nodes Rp1-Rp21 joined by a green edge wherever two repeaters are within R; a nearly complete graph
9. p22 **node-link-network** conf=high panels=2
   bbox [90.02, 446.56, 495.77, 618.37] (vector)
   cap: Figure 9: Illustration of the maximum spanning tree (a) and the minimum spanning tree (b) of G The red lines are the edges in the spanning trees and green lines are the other edges in the graph G.
   note: panels (a) maximum spanning tree and (b) minimum spanning tree of the same graph, each labelled on its own -40..40 frame
10. p23 **node-link-network** conf=high panels=2
   bbox [90.06, 434.36, 487.85, 583.71] (vector)
   cap: Figure 10: The resulted routes after the removal of edges, corresponding to the spanning tree in Fig 9. The red dashed lines represent the removed edges, while the blue solid lines are the reserved ones. The repeaters on the same blue line share the same tone.
   note: panels (a) and (b) show the signal routes left in the maximum and the minimum spanning tree: blue reserved edges and red dashed removed edges over the graph
11. p24 **scatter** conf=medium panels=1
   bbox [90.0, 464.3, 505.1, 693.7] (raster)
   cap: Figure 11: The solution consisted of 11 repeaters obtained by our algorithm. The blue circle denotes the considered area with radius 40miles, the red small circles represent the ability of receiving signals from users, and the blue points in the centers of the small red circles denote the positions 
   note: 11-repeater solution pasted as a raster: repeater points and the small red circles of their receiving range inside the 40-mile circle
12. p26 **map-or-plan-view** conf=high panels=1
   bbox [90.06, 75.3, 505.76, 397.07] (vector)
   cap: Figure 12: The solution consisted of 104 repeaters obtained by our algorithm. The blue circle denotes the considered area with radius 40miles, the red areas are the corresponding Voronoi areas and the blue points denote the positions of repeaters.
   note: 104-site Voronoi tessellation of the disc, sites unlabelled, cells drawn as red polygon walls inside the blue boundary
13. p33 **line** conf=high panels=1
   bbox [133.1, 261.0, 462.1, 491.3] (raster)
   cap: Figure 13: The Comparison between the least numbers of required repeaters obtained by the proposed algorithm and the Naï ve solution. The largest coverable circle in naï ve solution 1 is centered at the center of the central hexagon, while the largest coverable circle in naïve solution 2 is centered
   note: three series (proposed algorithm, naïve solution 1, naïve solution 2): least number of repeaters against the number of users
14. p34 **line** conf=high panels=1
   bbox [130.3, 157.7, 465.0, 391.9] (raster)
   cap: Figure 14: The Comparison between the least numbers of required repeaters obtained by the ve solution.
   note: normalised repeater count M/max M against the user communication range r, one curve for N=1000 and one for N=10000
15. p35 **photo-or-raster-image** conf=high panels=1
   bbox [90.5, 453.7, 504.85, 751.1] (raster)
   cap: Figure 15: An illustration about how a signal can be transmitted from a hollow area to a distant place with the help of a hierarchically organized relay network.
   note: aerial raster of mountain ridges and a valley settlement with four tower icons and red line-of-sight arrows drawn over it; caption printed at the top of p36

## tables
1. p10 table-grid bbox [112.34, 306.05, 483.1, 684.94]
   cap: Table 1: Effective radiated powers of repeaters in Utah (http://www.ussc.com/~uvhfs/rptr.html)
2. p14 table-grid bbox [97.46, 384.07, 498.0, 718.68]
   cap: Table 2: The cellular networks that can cover the largest circle. The third column lists the radiuses of the corresponding circles. Given the number of cells M, sometimes, the cellular networks are not unique, and then we only draw one of them as a representative.
3. p17 table-grid bbox [84.14, 87.62, 511.32, 321.29]
   cap: Table 3: The coordinates, frequencies and PL tones of the solution shown in Fig. 2.
4. p17 table-grid bbox [84.62, 431.47, 276.07, 479.35]
   cap: Table 4: Analytical results for two particular cases. In the left side the largest covered circle is centered at the center of the central hexagon, while in the right side the largest covered circle is centered at the intersection of the three more central hexagons.
5. p25 table-grid bbox [84.14, 87.62, 511.32, 304.73]
   cap: Table 5: The coordinates, frequencies and PL tones of the solution shown in Fig. 11.
6. p26 table-grid bbox [84.14, 477.67, 511.32, 761.16]
   cap: Table 6: The coordinates, frequencies and PL tones of the solution shown in Fig. 12.
7. p29 table-grid bbox [84.14, 329.69, 511.32, 546.7]
   cap: Table 7: The coordinates, frequencies and PL tones of the solution shown in Fig. 11.
8. p30 table-grid bbox [84.14, 87.62, 511.32, 769.56]
   cap: Table 8: The coordinates, frequencies and PL tones of the solution shown in Fig. 12.
9. p38 table-grid bbox [84.38, 212.42, 511.08, 768.96]
   cap: Table 9: Parameters appeared in this paper.
10. p39 table-grid bbox [161.54, 372.41, 433.9, 754.44]
   cap: Table 10: Mathematical symbols appeared in this paper.

## excluded
- p14 fragment-of-other bbox [239.9, 472.3, 303.7, 520.1] hexagon thumbnail pasted into the diagram column of Table 2 (region p14 r1), not a separate exhibit
- p14 fragment-of-other bbox [247.1, 596.65, 296.5, 649.3] hexagon thumbnail pasted into the diagram column of Table 2 (region p14 r1), not a separate exhibit
- p14 fragment-of-other bbox [242.9, 661.45, 300.7, 711.25] hexagon thumbnail pasted into the diagram column of Table 2 (region p14 r1), not a separate exhibit
- p15 split-across-pages bbox [97.46, 72.0, 498.0, 595.9] rows 6-13 of Table 2; the header and rows 1-5 are region p14 r1
- p15 fragment-of-other bbox [245.75, 73.8, 297.85, 134.5] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [246.25, 136.45, 297.5, 198.7] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [242.75, 206.9, 300.85, 270.7] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [242.65, 284.05, 301.1, 335.75] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [244.45, 345.25, 299.15, 401.65] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [244.45, 413.3, 299.15, 460.2] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [246.0, 473.15, 297.7, 527.05] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p15 fragment-of-other bbox [245.5, 534.7, 298.1, 592.45] hexagon thumbnail inside the Table 2 continuation (region p15 r1)
- p17 split-across-pages bbox [290.23, 431.47, 484.06, 479.35] Table 4 body rows; the column headings and first row are region p17 r2
- p17 split-across-pages bbox [290.23, 490.03, 484.06, 557.38] Table 4 body rows; the column headings and first row are region p17 r2
- p17 split-across-pages bbox [84.62, 510.55, 276.07, 557.38] Table 4 body rows; the column headings and first row are region p17 r2
- p17 split-across-pages bbox [84.62, 588.58, 276.07, 635.38] Table 4 body rows; the column headings and first row are region p17 r2
- p17 split-across-pages bbox [290.23, 588.58, 484.06, 635.38] Table 4 body rows; the column headings and first row are region p17 r2
- p17 split-across-pages bbox [290.23, 646.02, 484.06, 713.4] Table 4 body rows; the column headings and first row are region p17 r2
- p17 split-across-pages bbox [84.62, 666.58, 276.07, 713.4] Table 4 body rows; the column headings and first row are region p17 r2
- p18 split-across-pages bbox [84.62, 72.0, 484.06, 119.78] last Table 4 body rows, continuing the p17 fragments
- p18 split-across-pages bbox [83.9, 130.53, 484.06, 183.26] last Table 4 body rows, continuing the p17 fragments
- p27 split-across-pages bbox [84.14, 72.0, 511.32, 753.72] Table 6, repeater rows 16-56
- p28 split-across-pages bbox [84.14, 72.0, 511.32, 753.72] Table 6, repeater rows 57-97
- p29 split-across-pages bbox [84.14, 72.0, 511.32, 189.26] Table 6, repeater rows 98-104
- p31 split-across-pages bbox [84.14, 72.0, 511.32, 753.72] Table 8, repeater rows 40-80
- p32 split-across-pages bbox [84.14, 72.0, 511.32, 471.43] Table 8, repeater rows 81-104
- p39 split-across-pages bbox [84.38, 72.0, 511.08, 263.21] Table 9 parameter rows P_u,out to P_r,in; same three-column grid as region p38 r1
- p40 split-across-pages bbox [161.54, 72.0, 433.9, 232.49] Table 10 symbol rows after item 13
- p34 not-an-exhibit bbox [238.56, 687.32, 318.94, 720.64] typeset display formula (a square root in N, S_v and Phi) split out of the surrounding paragraph; an equation, not a figure

## distillation fields

figure 1 p7: sec=3 Model [model] zone=top order=1/1 area=0.098 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=7 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 1']
  caption: Figure N. words=23 sent=3 units=False vars=0 cond=True concl=False voice=none pos=below

figure 2 p16: sec=4 Analysis > 4.4 Naïve Solution [solution] zone=middle order=4/1 area=0.206 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=3 read=0 gap=0 pattern=none style=['Fig. 2', 'Figure 2']
  caption: Figure N: words=47 sent=2 units=False vars=0 cond=True concl=False voice=none pos=below

figure 3 p18: sec=4 Analysis > 4.4 Naïve Solution [solution] zone=middle order=7/1 area=0.201 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=2 read=1 gap=0 pattern=figure-n-shows style=['Figure 3']
  caption: Figure N: words=45 sent=3 units=False vars=0 cond=True concl=False voice=none pos=below

figure 4 p19: sec=5 Algorithm [solution] zone=top order=8/1 area=0.15 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=3 read=0 gap=0 pattern=none style=['Fig. 4', 'Figure 4']
  caption: Figure N: words=22 sent=2 units=False vars=0 cond=True concl=False voice=none pos=below

figure 5 p19: sec=5 Algorithm [solution] zone=bottom order=9/2 area=0.154 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=4 read=0 gap=0 pattern=none style=['Fig. 5', 'Figure 5']
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p20: sec=5 Algorithm [solution] zone=middle order=10/1 area=0.189 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=20 lead=0 count=3 read=0 gap=0 pattern=none style=['Fig. 6', 'Figure 6']
  caption: Figure N: words=60 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p21: sec=5 Algorithm [solution] zone=middle order=11/1 area=0.238 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=20 lead=1 count=2 read=0 gap=1 pattern=none style=['Figure 7', 'figure 7']
  caption: Figure N: words=44 sent=2 units=False vars=0 cond=False concl=True voice=none pos=below

figure 8 p22: sec=5 Algorithm [solution] zone=top order=12/1 area=0.149 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=2 read=0 gap=0 pattern=none style=['Fig. 8', 'Figure 8']
  caption: Figure N: words=28 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p22: sec=5 Algorithm [solution] zone=middle order=13/2 area=0.139 solo=False
  family=node-link-network panels=2 layout=1x2 shared=True legend=none cbar=False 3d=no printed=True
  mention: first=22 lead=0 count=3 read=0 gap=0 pattern=none style=['Fig 9', 'Fig. 9', 'Figure 9']
  caption: Figure N: words=38 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p23: sec=5 Algorithm [solution] zone=middle order=14/1 area=0.119 solo=False
  family=node-link-network panels=2 layout=1x2 shared=True legend=none cbar=False 3d=no printed=True
  mention: first=23 lead=0 count=2 read=0 gap=0 pattern=none style=['Fig. 10', 'Figure 10']
  caption: Figure N: words=46 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p24: sec=6 Simulation Results [solution] zone=bottom order=15/1 area=0.19 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=24 lead=0 count=4 read=0 gap=0 pattern=none style=['Fig. 11', 'Figure 11']
  caption: Figure N: words=51 sent=2 units=False vars=0 cond=True concl=False voice=none pos=below

figure 12 p26: sec=6 Simulation Results [solution] zone=top order=17/1 area=0.267 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=25 lead=1 count=4 read=0 gap=1 pattern=none style=['Fig. 12', 'Figure 12']
  caption: Figure N: words=39 sent=2 units=False vars=0 cond=True concl=False voice=none pos=below

figure 13 p33: sec=7 Sensitivity Analysis > 7.1 Sensitivity of Parameters [sensitivity] zone=middle order=21/1 area=0.151 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=33 lead=0 count=2 read=1 gap=0 pattern=figure-n-shows style=['Figure 13']
  caption: Figure N: words=60 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p34: sec=7 Sensitivity Analysis > 7.2 User Density Fluctuation [other] zone=top order=22/1 area=0.156 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=34 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 14']
  caption: Figure N: words=16 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p35: sec=7 Sensitivity Analysis > 7.3 Effects of Landscape: Discussing the Mountainous Areas [other] zone=bottom order=23/1 area=0.246 solo=False
  family=photo-or-raster-image panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=36 lead=-1 count=2 read=0 gap=1 pattern=none style=['Fig. 15', 'Figure 15']
  caption: Figure N: words=28 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

table 1 p10: sec=4 Analysis > 4.1 Communication Radius [other] zone=middle order=2/1 area=0.28 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=10 lead=0 count=2 read=1 gap=0 pattern=direct style=['Table 1']
  caption: Table N: words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 23x6 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=3 width=full orient=portrait cont=False

table 2 p14: sec=4 Analysis > 4.4 Naïve Solution [solution] zone=middle order=3/1 area=0.267 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=14 lead=0 count=6 read=1 gap=0 pattern=direct style=['Table 2']
  caption: Table N: words=45 sent=3 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 14x3 header=1 rules=boxed zebra=True merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=True

table 3 p17: sec=4 Analysis > 4.4 Naïve Solution [solution] zone=top order=5/1 area=0.199 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=16 lead=1 count=2 read=0 gap=1 pattern=none style=['Table 3']
  caption: Table N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 13x6 header=1 rules=boxed zebra=True merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 4 p17: sec=4 Analysis > 4.4 Naïve Solution [solution] zone=middle order=6/2 area=0.018 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=17 lead=0 count=2 read=1 gap=0 pattern=direct style=['Table 4']
  caption: Table N: words=45 sent=2 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 13x4 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=4 txt=0 width=full orient=portrait cont=True

table 5 p25: sec=6 Simulation Results [solution] zone=top order=16/1 area=0.185 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=24 lead=1 count=4 read=0 gap=1 pattern=none style=['Table 5']
  caption: Table N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 12x6 header=1 rules=boxed zebra=True merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 6 p26: sec=6 Simulation Results [solution] zone=bottom order=18/2 area=0.242 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=25 lead=1 count=2 read=0 gap=1 pattern=none style=['Table 6']
  caption: Table N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 105x6 header=1 rules=boxed zebra=True merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=True

table 7 p29: sec=6 Simulation Results > 6.3 N=1000, R=40 [other] zone=middle order=19/1 area=0.185 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=29 lead=0 count=2 read=0 gap=0 pattern=none style=['Table 7']
  caption: Table N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 12x6 header=1 rules=boxed zebra=True merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 8 p30: sec=6 Simulation Results > 6.4 N=10000, R=40 [other] zone=middle order=20/1 area=0.581 solo=True
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=29 lead=1 count=3 read=1 gap=1 pattern=direct style=['Table 8']
  caption: Table N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 105x6 header=1 rules=boxed zebra=True merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=True

table 9 p38: sec=8 Conclusion and Discussion [evaluation] zone=middle order=24/1 area=0.474 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=38 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 9']
  caption: Table N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 27x3 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=True

table 10 p39: sec=8 Conclusion and Discussion [evaluation] zone=middle order=25/1 area=0.208 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=39 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 10']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 22x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=half orient=portrait cont=True

