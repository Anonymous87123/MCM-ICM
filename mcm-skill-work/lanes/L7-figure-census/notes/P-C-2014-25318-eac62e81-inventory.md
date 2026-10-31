# P-C-2014-25318-eac62e81 — figure census

- layout sha `d6f7cd9fc43e338d`, 21 pages, 14 measured regions
- accounted: 11 figures, 3 tables, 0 excluded, 0 unaccounted
- families: flowchart-or-schematic 2, line 2, node-link-network 4, scatter 3, table-grid 3

1. p5 **node-link-network** conf=high panels=1
   bbox [127.56, 121.76, 467.73, 391.81] (raster)
   cap: Figure 1: The co-author network of the Erdos1.
   note: raster, one embedded bitmap, undirected spring layout with no arrowheads, no axes and no frame. Nodes are circles whose diameter grows with degree - five large dark red discs carry white capitalised names inside them (PAUL ERDOS, ALON NOGA M., HARARY FRANK, FOLDES ZOLTAN, CHVATAL VASEK), mid-sized pink discs carry dark names, and the white periphery carries numeric IDs only. Edges are teal hairlines. The look is NetDraw or Pajek rather than MATLAB. Cited a page and a half AFTER it prints, from the 4.2.3 text, and by the phrase 'the top 50 Erdos1 authors' - the prose never says how many nodes the drawing holds. Small-node ID labels print near-white on white and are marginally legible
2. p8 **scatter** conf=high panels=1
   bbox [155.91, 122.26, 439.37, 344.33] (raster)
   cap: Figure 2: Measure vectors of 511 Erdos1 authors, the big red point(1,1,0) stands for the ideal vector of the most crucial one.
   note: a MATLAB 3-D scatter: about 500 small dark blue markers inside a dashed perspective box, one large red flattened marker on the floor corner labelled (1,1,0) in red bold italic, and a pale green two-line legend at the upper right ('measure vector' / 'of Erdos1 author'). Axis labels print green, rotated: 'Normalization Betweenness Centrality' on the left axis (0 to 0.8) and 'Normalization Degree Centrality' on BOTH the vertical axis (0.094 to 0.102) and the receding one (0 to 1.2) - the same string twice, so one of the three axes is mislabelled, almost certainly the vertical one, which should read closeness. The caption calls it three-dimensional and the prose calls it 'the three-dimensional graph'; the caption writes the ideal vector without a space: 'point(1,1,0)'
3. p10 **line** conf=high panels=1
   bbox [127.56, 437.16, 467.73, 653.73] (raster)
   cap: Figure 3: The degree distribution of the Erdos1 network and the approximative power-law distribution.
   note: two series in a boxed frame: a solid dark blue degree curve with markers and a red dashed approximative line, dashed black gridlines at every tick, legend inside at the upper right. Axes print 'degree(k)' 0-60 and 'P(k)' 0-0.18, both LINEAR, so the power law the caption names cannot be read off the drawing - the reference line is a fit in linear coordinates and the exponent -1.6 quoted on the page has no slope to sit on. The only figure caption in the paper set as a justified two-line paragraph across the full measure instead of a centred single line
4. p12 **node-link-network** conf=high panels=1
   bbox [155.91, 122.14, 439.37, 317.07] (raster)
   cap: Figure 4: The directed citation network with weight added to nodes.
   note: raster, the 24-paper citation network, spring layout, thin black edges with small filled arrowheads. Node radius and fill both carry the paper weight - a near-white small circle for a light paper, a saturated dark blue disc with a printed weight for the six heaviest (0.322, 31.027, 39.265, 40.664 and two that print small enough to be uncertain at 150 dpi). Node IDs 1-24 print outside the circles in grey at about 5-6 pt. Arrow direction is untraceable wherever edges cross in the centre. The caption says weight is added to NODES, which is what the drawing does
5. p14 **flowchart-or-schematic** conf=high panels=1
   bbox [87.94, 122.2, 513.14, 222.17] (raster)
   cap: Figure 5: The flow chart of iteration process
   note: raster, a two-lane Microsoft Office flow chart - orange-to-peach gradient lane bars with drop shadows, rounded boxes with bevel and shadow, blue-grey connectors. Top lane runs G -> D -> a box holding 'A=qGD+(1-q)/N' -> an UNLABELLED circle holding only a multiplication cross -> PR(0) -> 'Impact factor', tagged 'initialization'. Bottom lane runs 'PR(k)=A*PR(k-1)' -> 'Max(abs(PR(k)-PR(k-1))) <0.0001' -> 'Yes' -> 'PageRank=PR(k)' with a 'No' feedback edge. Box text prints at 7-8 pt. Never cited by number: the prose below it says 'We implement the iteration based on the equation above', so the drawing is reached by position
6. p15 **scatter** conf=high panels=1
   bbox [141.73, 357.27, 453.55, 595.54] (raster)
   cap: Figure 6: Authority-Popularity Diagram for the citation network
   note: MATLAB axes holding 24 dark red upward triangles, boxed frame, ticks inward on all four spines, no gridlines and no legend: x prints 'cited quantities/year' 0.5-4.5 and y prints 'PageRank' 2.6-4.2, both linear, and neither tick value is the quantity its own axis title names: the page above sets log10 of a multiple of PR(k) as ordinate and log10 of ten times the cited quantities per year as abscissa, so the ticks carry the LOGARITHMS. Four rounded white quadrant labels were pasted on top of the plot - 'High authority / More popular' at the upper right, 'Low authority / More popular' at the lower right, 'High authority / Less popular' and 'Low authority / Less popular' on the left - with one strong dashed vertical at 2.5 and a horizontal divider near 3.4 that prints faint enough to vanish in reproduction. An orange callout box at the upper left names 'No.14: Watts,D. and Strogatz.S. / Collective dynamics of 'small-world' networks' and a thick curved arrow links it to the node ringed in open green at about (3.9, 4.12); the arrowhead sits at the BOX end, so it points away from the node. Second by-number citation on the same page ('we divided Figure 6 into four regions'), the only exhibit the prose reads back by number
7. p16 **node-link-network** conf=high panels=1
   bbox [127.56, 379.62, 467.73, 544.27] (raster)
   cap: Figure 7: The directed citation network with weight added to links.
   note: raster, NetDraw-style directed network of 15 film stars plus one blue square at the centre that carries NO label, so 16 nodes. All nodes are identical small blue squares with dark borders - neither size nor colour encodes anything, unlike Figure 4 - and grey labels sit outside them. Edges are thin grey arcs with small arrowheads, most of them carrying a grey numeric weight (7.4, 8.6, 5.3, 8.9, 4.9 ...). The caption is copied verbatim from Figure 4 two sections earlier and still says 'directed citation network', while the page addresses a co-star network of actors - the caption is wrong about its own subject. Labels stack on top of one another and on top of the arcs where edges converge (Brad Pitt, Angelina Jolie, Tom Hanks), and the 'Toby Maguire' label misspells Tobey
8. p17 **flowchart-or-schematic** conf=high panels=2
   bbox [155.91, 121.97, 439.37, 248.18] (raster)
   cap: Figure 8: The diagram for modified algorithm.
   note: raster, two panels side by side, Office drawing shapes: three filled blue ellipses lettered i, k and n with thick black arrows i->k and i->n, 'PageRank=1' printed under node i in both panels. The left panel labels both arrows 0.5; the right panel replaces them with stacked fractions 3/(3+4) x1 and 4/(3+4) x1, and a large blue block arrow between the panels carries the word 'improve'. Two panels of the SAME family, so one row with panel_count 2 rather than two rows. Stroke weights differ from arrow to arrow within one panel: the right-hand i->n arrow prints visibly heavier than its i->k neighbour. 'PageRank=1' prints with no spaces around the equals sign
9. p18 **scatter** conf=high panels=1
   bbox [170.08, 352.79, 425.2, 561.62] (raster)
   cap: Figure 9: Authority-Popularity Diagram for the co-star network
   note: raster, Excel-style axes with outward ticks and a full box frame, navy asterisk markers on white: x prints 'Results of Google Search' on a LOG scale with only three ticks, 10^6, 10^7 and 10^8, and y prints 'PageRank' linear from 0 to 0.15. The caption calls it an authority-popularity diagram and the body gives it no units; the abscissa is the raw search count in millions, not its log10, even though the prose above promises the logarithm. Two dashed black reference dividers, horizontal near 0.076 and vertical near 1.5e7, sit under four bevel-textured green quadrant boxes - 'High authority / More popular', 'High authority / Less popular', 'Low authority / More popular', 'Low authority / Less popular' - exactly as Figure 6 does. FOURTEEN markers print against the FIFTEEN rows of Table 7 on the same page: the point for 238 million searches (Tom Cruise, PR 0.117486) is absent, and two of the fourteen are clipped by the right frame. One point is labelled 'Angelina Jolie' in red with an arrow to the top-right marker - the only printed data label in the paper
10. p19 **line** conf=high panels=1
   bbox [141.73, 222.5, 453.55, 430.15] (raster)
   cap: Figure 10: Sensitivity to Damp Coefficient q
   note: raster, one thick black polyline with filled red triangle markers and dotted gridlines at every major tick in both directions: x prints 'Damp Coefficient q' from 0.2 to 1 and y prints 'Similarity' from 0.4 to 1, both linear, no legend, no fitted line and no printed data labels. Thirteen markers at q = 0.30, 0.40, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80, 0.85, 0.90, 0.95 and 1.00, drawn against the frame with no scale given anywhere: the curve sits near 0.40 at q 0.3, dips to about 0.74 at q 0.6, plateaus at the top frame for q 0.80-0.85 and settles back near 0.74. The q 0.30 marker and both plateau markers are clipped by the frame, and the rotated y title is squeezed into the tick-label gutter at 5-6 pt. The prose reads a 'slow change' off a curve whose plateau touches 1.0
11. p21 **node-link-network** conf=high panels=1
   bbox [184.25, 122.14, 411.02, 345.41] (raster)
   cap: Figure 11: The shortcut to boost influence
   note: raster, a PowerPoint-style concentric diagram rather than a graph-tool export: pale blue gradient rings draw a bullseye and about 40 circles sit on it in four classes - small white discs at the rim, periwinkle mid, saturated blue inner, and one small navy hub at the centre - so radius from the hub and fill both carry the same variable, with no node labels and no legend. Edges are 0.5 pt straight lines with no arrowheads except two short maroon stubs at the hub. A thick orange arrow labelled 'The shortcut' enters from outside the right frame into a blue node one ring off the centre. The art prints at the TOP of the reference page, so the unnumbered 'References' heading and the whole bibliography sit BELOW it; its section is the numbered 6 on p20, whose unnumbered sub-heading 'Shortcut to boost influence' asks the question. Never cited by number - the prose points at it with 'The solution we propose by our model is shown as below:' followed by three bullets

## tables
1. p13 table-grid bbox [142.07, 397.79, 453.21, 496.38]
   cap: Table 4: ID of papers and their Weight
2. p14 table-grid bbox [114.06, 432.82, 481.21, 564.14]
   cap: Table 5: The rank of papers by the stable PageRank value.
3. p15 table-grid bbox [125.08, 146.69, 470.19, 295.08]
   cap: Table 6: Cited quantities per year of each paper.

## distillation fields

figure 1 p5: sec=4.2.2 Methodology [model] zone=top order=1/1 area=0.183 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=7 lead=-2 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 1']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p8: sec=4.2.3 Results and Analysis [result] zone=top order=2/1 area=0.126 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=isometric printed=True
  mention: first=7 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 2']
  caption: Figure N: words=22 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p10: sec=4.4 Properties of the Erdos1 network [other] zone=middle order=3/1 area=0.147 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=10 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 3']
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p12: sec=5.2 Authority-Popularity Evaluation Model based on the revised [evaluation] zone=top order=4/1 area=0.11 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 4']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p14: sec=5.2 Authority-Popularity Evaluation Model based on the revised [evaluation] zone=top order=6/1 area=0.085 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p15: sec=5.2 Authority-Popularity Evaluation Model based on the revised [evaluation] zone=middle order=9/2 area=0.148 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=14 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 6']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p16: sec=5.3 The Co-star Network for Requirement 4 [other] zone=middle order=10/1 area=0.112 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=16 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 7']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p17: sec=5.4 Sensitivity Analysis [sensitivity] zone=top order=11/1 area=0.071 solo=False
  family=flowchart-or-schematic panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=16 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 8']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p18: sec=5.4 Sensitivity Analysis [sensitivity] zone=middle order=12/1 area=0.106 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=17 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 9']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p19: sec=5.5 Strengths and Weaknesses [evaluation] zone=middle order=13/1 area=0.129 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Figure 10']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p21: sec=6 The philosophy of the scale-free network [other] zone=top order=14/1 area=0.101 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p13: sec=5.2 Authority-Popularity Evaluation Model based on the revised [evaluation] zone=middle order=5/1 area=0.061 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Table 4']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x8 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=8 txt=0 width=full orient=portrait cont=False

table 2 p14: sec=5.2 Authority-Popularity Evaluation Model based on the revised [evaluation] zone=middle order=7/2 area=0.096 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=14 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['Table 5']
  caption: Table N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 25x6 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=2 width=full orient=portrait cont=False

table 3 p15: sec=5.2 Authority-Popularity Evaluation Model based on the revised [evaluation] zone=top order=8/1 area=0.102 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=14 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['Table 6']
  caption: Table N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 13x4 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=2 width=full orient=portrait cont=False

