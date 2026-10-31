# P-E-2018-88902-cefa4db9 — figure census

- layout sha `031aa0f786045e8a`, 28 pages, 39 measured regions
- accounted: 13 figures, 5 tables, 21 excluded, 0 unaccounted
- families: bar 1, composite-panel 1, flowchart-or-schematic 2, line 2, map-or-plan-view 1, node-link-network 2, other 2, scatter 2, table-grid 5

1. p4 **flowchart-or-schematic** conf=high panels=1
   bbox [144.0, 620.4, 451.2, 724.4] (?)
   cap: Figure 1: The structure of our model.
   note: The paper's only true schematic: four labelled circles - CCI, CCIC and WFSI in a row, with SOCIAL / COHESION / POLITICAL / ECONOMIC in a dashed box between CCIC and WFSI - joined by two plain arrows and one green horizontal arrow, with the multiplication 'x (1 - CCV)' printed in small italic over the CCI-to-CCIC arrow. No axes, no ticks, no legend, no unit, no 3-D. It is the figure the Strengths section leans on ('our model can be easily understood with a single graph and several lines of explanation, see Figure 1'), and it is placed at the foot of 1.2 Our Methods, i.e. at the point where the paper has finished naming the five elements - but the sentence that reads it is a page later, on p5, and that sentence is the exhibit's only prose pointer: no other exhibit in the paper is read in the page AFTER it is printed.
2. p7 **other** conf=high panels=1
   bbox [321.72, 72.24, 514.44, 264.96] (?)
   cap: Figure 2: Climate Change Index(CCI)
   note: A three-ring sunburst: an inner disc lettered 'Change / Change / (CCI)' - the word Change printed twice, the second line a duplicate, so the centre reads as a stutter rather than as 'Climate Change Index' - a middle band of eight segments labelled BI, RI, PR, TP, CE, SL, ND, AL grouped under the two radial titles 'Factor Indicator' and 'Result Indicator', and an outer ring whose near-white to navy gradient encodes a value with NO key, no legend and no colourbar. Nothing in the art says what the shading means. It is also the worst-placed exhibit in the paper: the caption 'Figure 2: Climate Change Index(CCI)' is set INLINE inside a justified paragraph rather than on its own line, so the wheel is boxed in on the left by body text and the page's lines run through the left band of the art. The paper's arithmetic (three FI and one RI) does not match the eight keys printed in the ring.
3. p8 **composite-panel** conf=high panels=5
   bbox [131.52, 173.52, 468.72, 429.36] (?)
   cap: Figure 3: Weighted Fragile State Index(WFSI)
   note: The paper's one composite: a large four-quadrant radial wheel around the label 'Weighted Fragile State Index (WFSI)' - quadrant names Social, Cohesion, Political, Economic, each over a colour gradient and under a row of clip-art pictograms (people, hand, globe) pasted on top of the segment boundaries - with FOUR satellite donuts, one per quadrant, placed at the four corners of the block. The satellites are the actual data: each prints its three sub-factor weights (e.g. EX 0.42343838, DP 0.313305939, RD 0.24450222 for Social), so the figure is a 12-number table drawn as five radial charts. The numbers are set at about 2 pt - four of the twelve (GG, SL, HF, UD) cannot be read at 2 px/pt render resolution at all, and none of them aligns to a common axis, so the weights cannot be compared by eye. No legend, no colourbar: the four quadrant gradients carry meaning that only the satellites recover. The caption prints 'Index(WFSI)' with the parenthesis welded to the previous word, as everywhere in this document.
4. p9 **flowchart-or-schematic** conf=high panels=3
   bbox [144.36, 201.36, 462.48, 284.52] (?)
   cap: Figure 4: Overview of the 2THN model.
   note: Three rounded boxes each holding a four-node graph, joined by arrows, with the first two boxes enclosed in a dashed container labelled as the template part and the third sitting OUTSIDE that container after an ellipsis - so the drawing contradicts its own key: the caption and the prose say the dashed area is what gets replicated, yet the replicated third slice is drawn outside it. Time is carried only by the labels 't', 't + 1' and 't + n' under the boxes. No axes, no ticks, no legend, no unit, no 3-D - the rounded boxes carry a soft drop shadow, which is a 2-D effect and the closest this paper comes to depth. It is the only exhibit in the paper that the region pass boxed twice (r1 vector, r2 raster, same geometry), which is why this row is anchored on r1 and carries the union area of both.
5. p11 **node-link-network** conf=high panels=1
   bbox [132.96, 61.56, 462.24, 186.84] (?)
   cap: Figure 5: The inner structure of 2THN.
   note: Five plain rectangles - Social, Cohesion, Economic, CCIC, Political - joined by four plain lines with NO arrowheads, which is what makes it a Markov network rather than a Bayesian one: two of the four edges (Social to Cohesion, Social to Economic) are dashed and two (Cohesion to Political, Economic to CCIC) are solid, and nothing in the caption or the prose explains the distinction - for a reader who does not already know that this is a pairwise Markov random field, the dashed strokes look like an unknown and undocumented convention. The prose describes seven factors; the drawing shows four edges. Hand-drawn box weight and the red Chinese resale banner immediately above it are the only defects; no axes, no legend, no unit.
6. p11 **node-link-network** conf=high panels=3
   bbox [130.2, 601.08, 434.4, 747.12] (?)
   cap: Figure 6: The intra structure of 2THN.
   note: The same five variables three times over, primed and double-primed - CCIC, Economic, Political, Cohesion, Social inside the t slice, the same set with ' inside t+1 and '' inside t+2 - joined by inter-slice arrows and by vertical intra-slice arrows. Two things break it: the t slice's five boxes are drawn with NO internal arrows at all while the two later slices carry them, so the present state is visually inert; and the Economic-to-Economic' link is drawn TWICE, two near-parallel strokes at every transition, an edge the prose never mentions. Each slice is enclosed in a thin rounded frame as the repeated template, the frames are the only enclosure, and the continuation ellipsis floats far right of the third frame with no leader line. No axes, no legend, no unit, no 3-D.
7. p16 **line** conf=high panels=1
   bbox [336.48, 566.16, 482.64, 716.76] (?)
   cap: Figure 7: Posterior mean analysis for CCIC.
   note: Four monotone marker curves - Cohesion, Political, Social and Economic, each keyed by a hollow dot in a legend titled 'Variables' set INSIDE the plot area at the top right - against x ticks 0.10 to 1.00 and y ticks 0.130 to 0.240 in 0.010 steps. The red Economic curve is the lowest and steepest, and the prose reads exactly that ('the red outlier line'), so this paper at least reads its own extreme. Two defects of the pasted image: a thick grey hatched bar runs along the x axis with a small grey filled square pasted on it - chart-border debris, not data - and the chart's left edge overlaps the body text column, so a line of prose runs under the x-axis title. No colourbar, no unit, no 3-D. The row is anchored on the raster region; the layout pass did not box the axis labels, so the recorded area is the plot only.
8. p17 **scatter** conf=high panels=4
   bbox [141.6, 150.0, 296.28, 322.44] (?)
   cap: Figure 8: Posterior mean analysis for the 4 indicators.
   note: Four panels in a 2x2 grid, titled Cohesion Mean, Economic Mean, Political Mean and Social Mean, each plotting four series against x ticks 0.00 to 1.00 in steps of 0.10 with the x title 'Variable Means' and each carrying its own legend inside the plot at the top right. Nothing is lettered: the panels are identified only by their titles, so a pointer cannot name a panel and the prose never does - it says 'the results of the four indicators are rather similar' and leaves the reader to find which panel is which. The similarity claim is not supported by the axes: the four y windows are 0.10-0.80, 0.20-0.80, 0.10-0.90 and 0.15-0.70, the tick step is 0.05 in three panels and 0.10 in the Political panel, and the top-right box is a fifth narrower than its neighbours - four separately produced images dropped into a grid, not one figure with shared limits. Worse, the colour-to-indicator mapping is not global: the legend order rotates panel by panel (Social/Political/Economic/CCIC, then CCIC/Political/Cohesion/Social, then Economic/Cohesion/CCIC/Social, then Cohesion/CCIC/Political/Economic), so red means Social in one panel and Economic in the next. CCIC is the one series drawn in a washed-out tint in every panel and the flat line the argument is about. The layout pass boxed all four panels TWICE - two overlapping crops per panel, four genuine drawings and eight regions - which is why this row is anchored on the first region with the whole grid's union as its area.
9. p19 **scatter** conf=high panels=4
   bbox [153.84, 56.88, 288.36, 306.12] (?)
   cap: Figure 9: K-Means Model Results
   note: Four three-dimensional scatter boxes in a 2x2 grid, each titled with the three indicators it plots - Cohesion-Economic-Policy, Cohesion-Economic-Social, Cohesion-Policy-Social, Economic-Policy-Social - so the paper shows all four three-way combinations of its four indicators and none of the pairs. Every panel draws an extruded grid box with three named axes, five divisions per axis and NO numeric tick label anywhere: the reader is given a shape and no scale. The three K-Means clusters are colour-coded dark violet, teal and olive with no legend, no cluster centre marker, no boundary and no caption key, so the classification the section is about cannot be read off the figure at all. It is also the one place where the paper's own justification is visible - 'four dimensions, which can't be shown in only one figure' - and the solution it picks is four 3-D boxes on a 2-D page.
10. p19 **bar** conf=high panels=4
   bbox [127.2, 436.2, 297.24, 653.76] (?)
   cap: Figure 10: Impact of CCIC.
   note: Four grouped bar panels - COHESION, ECONOMIC, POLITICAL, SOCIAL, each printed as its own coloured heading - two series each (Original dark, Post-Evidence the pale tint of the same hue) over ten category bins carrying the cluster boundaries, from '<=0.129' to '>0.849'. This is the figure that actually carries the Sudan argument, and it is the most honest one in the paper: percentage ticks with the sign on every label, one legend per panel placed BELOW the category row, and the bin edges printed so the reader can see what the bars are over. What it still does not do: no axis titles at all, the last bin is a duplicate value ('<=0.849' then '>0.849'), and the four panels use two different windows (0-35% for COHESION and SOCIAL, 0-45% for ECONOMIC and POLITICAL), so the 'especially economic' reading the prose draws is a reading of bar heights against two different y scales.
11. p21 **line** conf=high panels=1
   bbox [223.44, 71.64, 364.44, 174.24] (?)
   cap: Figure 12: WFSI for Greece from 2008 to 2017
   note: One line chart, four unmarked series (CI blue, EI orange, PI green, SI red) over annual points 2008 to 2017, keyed by a boxed legend inside the axes at the upper left. No axis titles, no chart title, no markers, no gridlines; y ticks 0.20 to 0.45 in 0.05 steps and x ticks only every second year (2008, 2010, 2012, 2014, 2016) while the data runs one year past the last tick to 2017, so the final point - the one the fragile-state conclusion rests on - sits outside the ticked range. The caption is printed BELOW the plot even though the text layer reads it first, which is worth remembering: reading order is not caption side. The one defect of substance is that the caption says '2008 to 2017' while the body text on p19 says the scores are shown 'from 2008 to 2012' - the same words describing a figure of five years and a figure of ten.
12. p20 **other** conf=high panels=5
   bbox [84.96, 96.0, 511.68, 181.44] (?)
   cap: Figure 11: WFSI and CCIC for Greece from 2008 to 2012
   note: Five radar roses on a single grey card, one per year from 2008 to 2012, keyed by a year legend printed inside the card at the top centre; each rose has five spokes - CI, EI, PI, SI and CCIC - and the ring labels run 0.10 to 0.35, which is the boundary the prose explains ('the changes between years are small, so we set the radar chart boundary to 0.35'). It is the one exhibit in the paper that states its own axis limit and then labels it, and the one place a reader can compare five years of two indices at a glance. What it costs: the spoke and ring labels are set at about 5 pt, the CCIC spoke sits on the same 0-0.35 scale as the four 0.2-0.4 index spokes so its values are visually crushed against the centre, and the grey card is pasted over the page with its own shadow. No colourbar, no 3-D. The caption carries no terminal period - 'from 2008 to 2012' runs straight into the body sentence that follows it.
13. p22 **map-or-plan-view** conf=high panels=2
   bbox [62.64, 357.96, 287.52, 474.12] (?)
   cap: Figure 13: Results with continents.
   note: Two world choropleths side by side - (a) Climate Change Index by Country and (b) Weighted Fragile Continent Index - each a raster with its own vertical colour bar at its right edge, printed 'High' and 'Low' with end numbers too small to read at render resolution, so the two maps' scales cannot be compared and nothing states whether they share one. Grey marks no-data countries, which the pointer sentence does explain. The panel titles print ABOVE the maps, between Table 5 and the caption. The substance defect: panel (b) is captioned as a CONTINENT index, yet it is shaded country by country, and the very next sentences admit the reading fails ('please find Australia in both graphs... The modeling result is not very ideal'). This is the paper's only exhibit that argues against itself. The row is anchored on the left map region with the union of both regions as its area; the right region is excluded as the sibling panel.

## tables
1. p18 table-grid bbox [128.52, 56.95, 467.68, 154.53]
   cap: Table 1: Overall metrics.
2. p18 table-grid bbox [128.16, 191.4, 467.39, 259.54]
   cap: Table 2: Metrics for node-node relationship.
3. p20 table-grid bbox [95.3, 255.28, 500.55, 347.68]
   cap: Table 3: WFSI and CCIC for Greece from 2008 to 2012.
4. p20 table-grid bbox [118.65, 648.66, 476.9, 740.43]
   cap: Table 4: WFSI C for Greece from 2013 to 2017.
5. p22 table-grid bbox [127.6, 56.85, 468.35, 312.59]
   cap: Table 5: Proposed solutions to Sudan’s case.

## excluded
- p22 fragment-of-other bbox [301.68, 358.2, 526.56, 474.0] 
- p5 not-an-exhibit bbox [57.05, 334.18, 555.05, 534.58] 
- p9 duplicate bbox [132.55, 195.25, 303.65, 307.6] 
- p10 not-an-exhibit bbox [253.44, 71.16, 476.16, 115.44] 
- p11 not-an-exhibit bbox [216.36, 232.56, 409.08, 282.12] 
- p12 not-an-exhibit bbox [220.92, 168.12, 373.92, 215.4] 
- p12 not-an-exhibit bbox [200.52, 431.64, 430.68, 509.64] 
- p12 not-an-exhibit bbox [237.36, 637.08, 472.08, 737.64] 
- p13 not-an-exhibit bbox [179.52, 399.0, 432.24, 474.72] 
- p13 not-an-exhibit bbox [184.44, 632.04, 478.44, 734.76] 
- p15 not-an-exhibit bbox [213.24, 384.0, 399.24, 423.72] 
- p16 not-an-exhibit bbox [195.96, 184.44, 416.4, 228.0] 
- p17 fragment-of-other bbox [314.4, 150.6, 469.08, 321.84] 
- p17 duplicate bbox [140.76, 159.36, 281.52, 307.32] 
- p17 duplicate bbox [313.56, 159.72, 457.44, 307.32] 
- p17 fragment-of-other bbox [315.12, 323.4, 469.08, 493.56] 
- p17 fragment-of-other bbox [143.64, 324.72, 296.28, 492.24] 
- p17 duplicate bbox [314.16, 331.32, 457.44, 482.04] 
- p17 duplicate bbox [142.68, 333.36, 280.68, 478.32] 
- p19 fragment-of-other bbox [326.64, 56.88, 460.32, 306.12] 
- p19 fragment-of-other bbox [300.0, 436.44, 469.92, 653.04] 

## distillation fields

figure 1 p4: sec=1 Introduction > 1.2 Our Methods [introduction] zone=bottom order=1/1 area=0.0637 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=4 lead=0 count=2 read=1 gap=0 pattern=none style=['Figure 1']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p7: sec=4 Model > 4.1 Climate Change Index by Country(CCIC) > 4.1.1 Climate Change Index(CCI) [model] zone=top order=2/1 area=0.0741 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=7 lead=0 count=1 read=1 gap=0 pattern=as-shown-in style=['Figure 2']
  caption: Figure N: words=5 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 3 p8: sec=4 Model > 4.2 Weighted Fragile State Index(WFSI) [model] zone=middle order=3/1 area=0.1721 solo=False
  family=composite-panel panels=5 layout=1+4 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=6 lead=2 count=1 read=1 gap=2 pattern=as-shown-in style=['Figure 3']
  caption: Figure N: words=6 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 4 p9: sec=4 Model > 4.3.1 Overview [model] zone=top order=4/1 area=0.0739 solo=False
  family=flowchart-or-schematic panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=1 count=1 read=1 gap=1 pattern=direct style=['figure 4']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p11: sec=4 Model > 4.3.4 Inner Structure - Markov Network [model] zone=top order=5/1 area=0.0823 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 5']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p11: sec=4 Model > 4.3.5 Intra Structure - Bayesian Network [model] zone=bottom order=6/2 area=0.0886 solo=False
  family=node-link-network panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=0 count=2 read=1 gap=0 pattern=as-shown-in style=['Figure 6']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p16: sec=6 Analysis > 6.2 Posterior Mean Value Analysis [result] zone=bottom order=7/1 area=0.0439 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=17 lead=-1 count=1 read=1 gap=1 pattern=direct style=['Figure 7']
  caption: Figure N: words=7 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 8 p17: sec=6 Analysis > 6.2 Posterior Mean Value Analysis [result] zone=top order=8/1 area=0.225 solo=False
  family=scatter panels=4 layout=2x2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=16 lead=1 count=1 read=1 gap=1 pattern=parenthetical style=['Figure 8']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p19: sec=7 Task 1: Models and Standard Lines > 7.1 Determine the standard line by K-Means Clustering Algorithm [result] zone=top order=11/1 area=0.1523 solo=False
  family=scatter panels=4 layout=2x2 shared=False legend=none cbar=False 3d=perspective-bars printed=False
  mention: first=18 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Figure 9']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p19: sec=8 Task 2: Case Study - Sudan [result] zone=middle order=12/2 area=0.1487 solo=False
  family=bar panels=4 layout=2x2 shared=False legend=below cbar=False 3d=no printed=True
  mention: first=18 lead=1 count=1 read=1 gap=1 pattern=parenthetical style=['Figure 10']
  caption: Figure N: words=5 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 11 p21: sec=9 Task 3: Case Study - Greece > 9.2 Prediction for Greece [result] zone=top order=16/1 area=0.0289 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=20 lead=1 count=1 read=1 gap=1 pattern=direct style=['Figure 12']
  caption: Figure N: words=9 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 12 p20: sec=9 Task 3: Case Study - Greece > 9.1 WFSI and CCIC for Greece [result] zone=top order=13/1 area=0.0727 solo=False
  family=other panels=5 layout=1x5 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=19 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Figure 11']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p22: sec=11 Task 5: Scalability Analysis [result] zone=middle order=18/2 area=0.1075 solo=False
  family=map-or-plan-view panels=2 layout=1x2 shared=False legend=none cbar=True 3d=no printed=False
  mention: first=21 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Figure 13']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p18: sec=6 Analysis > 6.3 Other Analysis [result] zone=top order=9/1 area=0.066 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=17 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Table 1']
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 2 p18: sec=6 Analysis > 6.3 Other Analysis [result] zone=top order=10/2 area=0.0461 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=17 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Table 2']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x11 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=9 txt=2 width=full orient=portrait cont=False

table 3 p20: sec=9 Task 3: Case Study - Greece > 9.1 WFSI and CCIC for Greece [result] zone=middle order=14/2 area=0.0747 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=20 lead=0 count=1 read=1 gap=0 pattern=as-shown-in style=['Table 3']
  caption: Table N: words=11 sent=1 units=False vars=2 cond=False concl=False voice=none pos=below
  table: 6x7 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=5 txt=2 width=full orient=portrait cont=False

table 4 p20: sec=9 Task 3: Case Study - Greece > 9.2 Prediction for Greece [result] zone=bottom order=15/3 area=0.0656 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=20 lead=0 count=2 read=1 gap=0 pattern=as-shown-in style=['Table 4']
  caption: Table N: words=10 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below
  table: 6x6 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=2 width=full orient=portrait cont=False

table 5 p22: sec=11 Task 5: Scalability Analysis [result] zone=top order=17/1 area=0.1738 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=21 lead=1 count=1 read=1 gap=1 pattern=direct style=['Table 5']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x4 header=1 rules=vertical-rules zebra=True merged=False diag=False units_hdr=False dec=False num=1 txt=3 width=full orient=portrait cont=False

