# P-C-2015-37284-dee063ba — figure census

- layout sha `681716d759a58337`, 21 pages, 25 measured regions
- accounted: 20 figures, 5 tables, 0 excluded, 0 unaccounted
- families: flowchart-or-schematic 4, line 4, node-link-network 8, other 3, scatter 1, table-grid 5

1. p3 **node-link-network** conf=high panels=1
   bbox [217.8, 504.7, 422.05, 648.7] (?)
   cap: Figure 1: The intimacy among people
   note: Twelve clipart human figures as nodes on a plain field, joined by straight undirected edges in two tones of teal. No axes, no ticks, no numbers, no legend; the two edge tones are never explained anywhere in the text. Nothing is plotted - the drawing is the graph and nothing else.
2. p4 **node-link-network** conf=high panels=1
   bbox [203.9, 423.09, 411.99, 564.54] (?)
   cap: Figure 2: The network of loyalty and intimacy
   note: Six green circles labelled 1-6 joined by undirected edges; each node carries its loyalty symbol alpha-1..alpha-6 and each edge an intimacy label such as beta-15 and beta-45. The formula symbols are printed on the drawing itself, so the figure doubles as a notation map: read it against the preceding definition text, never as a data plot.
3. p5 **flowchart-or-schematic** conf=high panels=1
   bbox [214.4, 72.0, 401.52, 182.1] (?)
   cap: Figure 3: A tree network of positions
   note: Rooted position tree: one red root circle, three green circles on the second level and five teal on the third, with the level names Senior manager / Junior manager / Experienced supervisor printed down the left as axis-like labels. Solid edges step down one level, while dashed curved arcs run from the root straight to the bottom row - the arcs are the only dashed marks and they carry promotion paths that skip levels. A row of ellipsis dots under the leaves says the tree continues.
4. p5 **node-link-network** conf=high panels=1
   bbox [242.9, 634.01, 373.1, 754.19] (?)
   cap: Figure 4: The match between employees and occupations
   note: Bipartite drawing in two vertical ellipses: five clipart employee nodes u1-u5 in the left ellipse and eight coloured position circles v1-v8 in the right, joined by straight crossing undirected edges. The column footers U and V name the two vertex sets. One edge is meant to be the chosen matching - the text calls it the blue edge - so colour is the only carrier and there is no key.
5. p6 **node-link-network** conf=high panels=2
   bbox [199.05, 368.21, 417.21, 521.56] (?)
   cap: Figure 5: A static human capital network
   note: Two networks drawn on slanted parallelogram planes side by side: the left plane holds the person network as black circles of differing size, the right plane holds the position hierarchy as a red root over yellow and green nodes, and matching edges run between the planes. The planes are drawn in perspective rather than as flat panels, so three_d is isometric even though no 3-D marks are plotted.
6. p7 **node-link-network** conf=high panels=3
   bbox [182.13, 72.0, 434.16, 227.25] (?)
   cap: Figure 6: A dynamic human capital network
   note: Three stacked time slices on a Time Stamp axis labelled t0, t1, ellipsis, tn - each slice a cyan person plane plus a magenta position tree joined by dashed colour-graded arcs, with one edge highlighted red in the last slice. The vertical stack with a printed time axis is how a static network figure becomes a time series here; only the stamp symbols print, no values.
7. p7 **node-link-network** conf=high panels=1
   bbox [219.7, 602.71, 395.92, 659.01] (?)
   cap: Figure 7: The change of loyalty when position changes
   note: Three-node directed graph: i (green) and k (yellow) feed j (red) by solid arrows labelled t_ik and t_kj, plus one dashed arc i->j labelled t_ij. The dashed arc is the non-adjacent case and the solid pair the adjacent one. All three labels are formula symbols printed on the edges; no data values, no axes.
8. p8 **flowchart-or-schematic** conf=high panels=3
   bbox [176.15, 84.82, 439.7, 223.52] (?)
   cap: Figure 8: The intimacy changes in different situations
   note: Three side-by-side columns under one vertical Level arrow, headed Shorten, Enlarge and Unchanged and separated by dashed grey dividers. Inside each column short green and magenta bars mark two people's levels and orange arrows link them, so each case is drawn rather than plotted. The three column headings mirror the three numbered cases in the text.
9. p9 **node-link-network** conf=high panels=1
   bbox [199.93, 246.46, 395.38, 376.06] (?)
   cap: Figure 9: The calculation of loyalty when promoted
   note: Four numbered circles 1-4 coloured by state (red top, two yellow, one green) with directed arrows 2->1, 3->1, 4->2 solid and 4->1 dashed, sitting above rounded boxes that hold their level numbers. This figure does print values: edge labels 1.05, 1.02, 1.03 and 1.07, plus 0.95 and 0.92 beside nodes, so printed_numbers is true even with no axis anywhere.
10. p10 **flowchart-or-schematic** conf=high panels=1
   bbox [164.9, 244.69, 450.7, 608.44] (?)
   cap: Figure 10: Dynamic process of the change of human capital network
   note: Single-column flowchart: hexagon Simulation Start, then rectangular steps for churn to personal reasons and churn following staff with the P_i formula printed inside the box, then the position-adjustment box drawn dashed with a dashed HR adjustment arrow entering from the right, then the loyalty update, and a Time goes box closing the loop upward. Dashed means the optional HR action, solid the monthly step.
11. p12 **other** conf=high panels=1
   bbox [155.15, 359.3, 460.89, 444.4] (?)
   cap: Figure 11: The chromosome we defined
   note: A printed chromosome string 201N34026314D2031D52140N312531 ... with thin red leader lines running from individual characters out to blue callout labels such as No Position, Departure and The 9th person is a Senior manager. The nodes are characters and the edges are leader lines; no boxes, no plot.
12. p13 **other** conf=high panels=1
   bbox [213.4, 103.85, 406.25, 291.65] (?)
   cap: Figure 12: Genetic operators
   note: Three labelled column groups - chromosomes, mutation, crossover - separated by dashed vertical rules, each holding two vertical symbol stacks for individuals A and B. Mutation and crossover are shown by swapping single symbols and the exchanged pair is ringed with a red ellipse. Signs only: no axes and no numbered values, so it reads as an operator schematic.
13. p13 **flowchart-or-schematic** conf=high panels=1
   bbox [218.55, 451.05, 397.75, 702.7] (?)
   cap: Figure 13: The flowchart of termination
   note: Vertical flowchart with one decision diamond: hexagon start, initialization with the generation number, i=0, selection, genetic operators, i++, then the diamond i>=k, then end. The No branch loops left and up into selection while the Yes branch falls through to termination; both branch labels print on the edges.
14. p14 **other** conf=high panels=1
   bbox [190.4, 136.08, 425.3, 359.56] (?)
   cap: Figure 14: The pie of the whole model
   note: Pie of the three model components - Computer Simulation, Transformation, Genetic Algorithm - with three outlined annotation boxes laid over the slices (staff churn, loyalty and intimacy change, position assignment) and thick magenta arrows converging on the centre under the words TIME GOES. No slice carries a percentage or a count, so the pie only says which parts the model has, never how big they are.
15. p16 **line** conf=high panels=1
   bbox [172.88, 439.82, 432.22, 588.17] (?)
   cap: Figure 15: The line chart of total cost
   note: Single light-blue line with no markers, churn rate(%) 21-39 against cost(sigma) 450-650, horizontal gridlines. The one-entry legend sits outside-right and repeats the panel title 'total cost', so it adds nothing the axes do not already say.
16. p17 **line** conf=high panels=1
   bbox [176.08, 72.0, 440.23, 217.23] (?)
   cap: Figure 16: The line chart of indirect cost
   note: Same construction as Figure 15 for the indirect cost: one steel-blue smooth line, no markers, churn rate(%) 21-39 against cost(sigma) 0-200, one-entry legend outside-right repeating the title. The two cost figures are a matched pair drawn as separate charts, not as one two-series chart.
17. p17 **scatter** conf=high panels=1
   bbox [89.85, 359.5, 497.99, 535.4] (?)
   cap: Figure 17: Situations of different churn and recruitment rates
   note: Feasibility map: three filled diagonal bands (red Feasible Region, yellow Subordinate Feasible Region, cyan Unfeasible Region) with three marker types for the solved cases (open circle, open square, cross), axes Churn Rate(%) and Recruitment Rate(%) both 0-40. This is the paper's only six-entry legend and it sits outside-right.
18. p19 **line** conf=high panels=1
   bbox [194.9, 72.0, 420.85, 218.49] (?)
   cap: Figure 18: Iteration times to get the optimal solution
   note: Bare black line on arrow axes: Cost(sigma) against Iteration Times (k), with only 5.88 on the y axis and 1000 and 2000 on the x axis printed. Two grey dashed vertical guides drop from the curve to mark the chosen iteration counts, so the guides - not any printed value - carry the argument.
19. p19 **line** conf=high panels=1
   bbox [187.95, 309.08, 428.3, 461.58] (?)
   cap: Figure 19: The fluctuate of mutation and crossover rate
   note: Two solid black lines - Crossover Rate and Mutation Rate - identified by text printed inside the plot at the right instead of by a legend, axes Rate (0, 0.1, 0.4) and Iteration Times (k) with one printed 1000. Two faint reddish dashed guides stand at the rates 0.1 and 0.4 that the text picks.
20. p20 **node-link-network** conf=high panels=3
   bbox [191.9, 72.0, 424.15, 205.0] (?)
   cap: Figure 20: Multi-layers network
   note: Three skewed parallelogram panels side by side labelled Information Network, Relationship Network and Position Network, joined by inter-layer edges in red, green and yellow while intra-layer edges stay black. The panels are slanted to suggest layers but they are laid out left to right rather than stacked, so three_d stays no - unlike Figure 6's vertical stack.

## tables
1. p8 table-grid bbox [193.82, 492.91, 401.71, 573.79]
   cap: Table 1: The levels of positions
2. p12 table-grid bbox [155.66, 273.86, 439.75, 331.85]
   cap: Table 2: The meanings of indexes
3. p15 table-grid bbox [84.26, 161.78, 511.18, 534.31]
   cap: Table 3: The data of simulation
4. p16 table-grid bbox [129.98, 97.7, 465.46, 401.21]
   cap: Table 4: The change of cost following the churn rate
5. p18 table-grid bbox [84.26, 97.7, 515.5, 240.62]
   cap: Table 5: Numbers of employees of different positions

## distillation fields

figure 1 p3: sec=3 The human capital network > 3.1 The network among people [other] zone=bottom order=1/1 area=0.059 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=['Figure 1']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p4: sec=3 The human capital network > 3.2 The network among position [other] zone=middle order=2/1 area=0.059 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=4 lead=0 count=2 read=1 gap=0 pattern=as-shown-in style=['Figure 2']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p5: sec=3.2 The network among position [other] zone=top order=3/1 area=0.041 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=['Figure 3']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p5: sec=3 The human capital network > 3.3 The bipartite graph between people and positions [other] zone=bottom order=4/2 area=0.031 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=5 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 4']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p6: sec=4 The dynamic human capital network > 4.1 The frame of the model [model] zone=middle order=5/1 area=0.067 solo=False
  family=node-link-network panels=2 layout=1x2 shared=False legend=none cbar=False 3d=isometric printed=False
  mention: first=6 lead=0 count=1 read=1 gap=0 pattern=none style=['Figure 5']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p7: sec=4 The dynamic human capital network > 4.1 The frame of the model [model] zone=top order=6/1 area=0.078 solo=False
  family=node-link-network panels=3 layout=column of 3 shared=False legend=none cbar=False 3d=isometric printed=False
  mention: first=6 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['figure 6']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p7: sec=4 The dynamic human capital network > 4.1 The frame of the model [model] zone=bottom order=7/2 area=0.02 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=['Figure 7']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p8: sec=4 The dynamic human capital network > 4.3 The calculation of loyalty [solution] zone=top order=8/1 area=0.073 solo=False
  family=flowchart-or-schematic panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=0 count=1 read=1 gap=0 pattern=none style=['Figure 8']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p9: sec=4 The dynamic human capital network > 4.4 Organizational churn in dynamic process [other] zone=middle order=10/1 area=0.051 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=1 read=1 gap=0 pattern=none style=['Figure 9']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p10: sec=4 The dynamic human capital network > 4.5 The productivity and cost > 4.5.1 Productivity [other] zone=middle order=11/1 area=0.207 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=direct style=['figure 10']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p12: sec=4 The dynamic human capital network > 4.6 Optimize the management of human capital [other] zone=middle order=13/2 area=0.052 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=['Figure 11']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p13: sec=4 The dynamic human capital network > 4.6 Optimize the management of human capital [other] zone=top order=14/1 area=0.072 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=1 read=1 gap=0 pattern=none style=['Figure 12']
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p13: sec=4 The dynamic human capital network > 4.6 Optimize the management of human capital [other] zone=bottom order=15/2 area=0.09 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=1 read=1 gap=0 pattern=none style=['Figure 13']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p14: sec=5 Application of the Model > 5.1 The organization’s budget requirements [model] zone=top order=16/1 area=0.105 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 14']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p16: sec=5 Application of the Model > 5.2.2 Indirect cost [model] zone=middle order=19/2 area=0.077 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=16 lead=0 count=1 read=1 gap=None pattern=none style=['Figure 15']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p17: sec=5 Application of the Model > 5.3 The HR health of the organization [model] zone=top order=20/1 area=0.077 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=17 lead=0 count=1 read=1 gap=None pattern=none style=['Figure 16']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p17: sec=5 Application of the Model > 5.3 The HR health of the organization [model] zone=middle order=21/2 area=0.143 solo=False
  family=scatter panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=17 lead=0 count=1 read=1 gap=0 pattern=none style=['Figure 17']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p19: sec=7 Team Science and Multi-layer Networks [other] zone=top order=23/1 area=0.066 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=19 lead=0 count=1 read=1 gap=None pattern=none style=['Figure 18']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p19: sec=7 Team Science and Multi-layer Networks [other] zone=middle order=24/2 area=0.073 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=19 lead=0 count=1 read=1 gap=None pattern=none style=['Figure 19']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 20 p20: sec=9 Strengths and Weaknesses > 9.2 Weaknesses [evaluation] zone=top order=25/1 area=0.062 solo=False
  family=node-link-network panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=20 lead=0 count=1 read=1 gap=None pattern=none style=['Figure 20']
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p8: sec=4 The dynamic human capital network > 4.3 The calculation of loyalty [solution] zone=middle order=9/2 area=0.034 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=8 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 1']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 7x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=1 txt=1 width=half orient=portrait cont=False

table 2 p12: sec=4 The dynamic human capital network > 4.6 Optimize the management of human capital [other] zone=middle order=12/1 area=0.033 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=12 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 2']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=half orient=portrait cont=False

table 3 p15: sec=5 Application of the Model > 5.2.1 Direct cost [model] zone=middle order=17/1 area=0.317 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=15 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 3']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 26x6 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 4 p16: sec=5 Application of the Model > 5.2.2 Indirect cost [model] zone=top order=18/1 area=0.203 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=['Table 4']
  caption: Table N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 21x5 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=5 txt=0 width=full orient=portrait cont=False

table 5 p18: sec=6 The Analysis of Parameter [result] zone=top order=22/1 area=0.123 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=['Table 5']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 8x7 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=6 txt=1 width=full orient=portrait cont=False

