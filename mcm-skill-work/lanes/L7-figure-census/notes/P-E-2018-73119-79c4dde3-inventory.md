# P-E-2018-73119-79c4dde3 — figure census

- layout sha `df336c3c7544bf21`, 27 pages, 23 measured regions
- accounted: 9 figures, 9 tables, 5 excluded, 0 unaccounted
- families: flowchart-or-schematic 1, line 5, node-link-network 1, scatter 1, table-as-figure 1, table-grid 9

1. p7 **flowchart-or-schematic** conf=high panels=1
   bbox [283.44, 521.4, 510.24, 643.92] (?)
   cap: Figure 1: PSR Model
   note: The three-letter thesis of the paper as a diagram: three 3-D cylinders in a row - Pressure (blue), State (green), Response (orange) - joined by four straight arrows each carrying its own label (Pressure P-to-S, Information S-to-R, Response R-to-S, Resource S-to-P) and closed into a triangle by two curved arcs labelled Impact (P-to-R) and Response (R-to-P). No legend, no axes, no numbers: the arrow labels ARE the key, and the cylinder fill colour only repeats the label inside each node. The cylinders are icon glyphs, not a third dimension. It floats in the right column beside the body of section 3.1, so its caption prints under the artwork and to the right of the heading - the heading detector read the two as one line, '3.1 PSR Figure 1: PSR Model'. Never cited: the prose immediately below it discusses P, S and R without ever pointing at the figure that names them.
2. p8 **table-as-figure** conf=high panels=1
   bbox [83.52, 153.96, 508.68, 380.76] (?)
   cap: Figure 2: Indicators
   note: The paper's whole indicator system delivered as a TABLE wearing a figure caption: seventeen rows (one header, sixteen indicators) and five columns - Target Layer, Dimension Layer, Theme Layer, Indicator Layer, and a fifth column of +/- marks with NO header at all, so sixteen marks are unexplained. Merges run on the row axis only: 'Fragility Index' spans all sixteen indicator rows, the three dimensions span six, five and five, and the seven themes span their own blocks. Rules are not booktabs - heavy closed top, header and bottom borders with DASHED separators at every dimension and theme boundary and dashed verticals between the layer columns - and the grouping is carried by pastel colour bands rather than by shading. The same sixteen indicators are then written out as a bulleted list in the two pages that follow, so the figure and the prose say the same thing twice. Introduced only as 'we determine the indicators shown in the figure below' - no number.
3. p12 **node-link-network** conf=high panels=1
   bbox [111.96, 504.84, 480.48, 703.32] (?)
   cap: Figure 3: Relationship between indicators
   note: Directed node-link diagram of the climate chain the section argues for: a heavily thinned graph in three tiers of 3, 5 and 5 nodes - climate drivers (Temperature, Elevation, Natural Disasters) into land and water processes (Forest Cover Rate, Crop Production, Water Resource, Health, Energy Consumption) into social outcomes (GDP, Gini Coefficient, Public Service, Democracy Rate, Human Right). Edge colour encodes the SOURCE tier (blue leaves the top tier, orange the middle, green the bottom, one yellow edge leaves Temperature) and no legend explains it, so the colour carries information the reader must infer from the node fills. Several edges run upward from the social tier back into the land tier, drawing a dense X of crossings with no bundling and no arrowheads large enough to follow at page size. No edge weights, so the figure states the topology of the argument and none of its strengths - those arrive a page later as regressions in Table 2. Never cited by number: it appears under the sentence 'we are required to identify how climate change increases fragility directly and indirectly' and the two bulleted lists that follow are its caption in prose.
4. p15 **scatter** conf=high panels=1
   bbox [111.96, 230.4, 480.48, 457.2] (?)
   cap: Figure 4: Fragility Index:Blue circles represent the results of PSA, and red crosses rep-resent the results of FSI
   note: The validation exhibit: twenty numbered cases on a fragility axis, each case carrying TWO marks - a light-blue open circle for the model's PSA score and a red-orange cross for FSI's - with the case number hand-placed beside the pair. Two horizontal threshold rules cut the field at 0.6 (purple) and 0.4 (orange) and the band names are printed as red text in place of a legend, so the key lives half in the caption and half in the plot. No axis titles at all, only ticks (x 0-10, y 0.2-0.9), so the reader is told nothing about what either axis measures. The caption does the keying that a legend would: 'Blue circles represent the results of PSA, and red crosses rep-resent the results of FSI', with no space after the colon and the hyphen of a line break left in 'represent'.
5. p17 **line** conf=high panels=1
   bbox [111.84, 255.24, 480.36, 464.64] (?)
   cap: Figure 5: FI of Congo
   note: Single-series time path of the DRC's fragility index, MATLAB default styling: light-green line with dark-green downward triangles at eleven annual points, title inside the frame ('Fragile Index over the past eleven years of DRC'), boxed axes with inward ticks and no grid. Axis titles present here - 'Fragile Index' and 'Year' - which the validation scatter of Figure 4 did not get. The y axis is cropped to 0.30-0.36, a sixth of a unit tall, so ordinary annual wiggle fills the frame; the sibling Figure 6 plots the same index on 0.28-0.44 and Figure 7 on 0.32-0.42, so no two charts of the same quantity share a scale. The prose introduces it as 'ten years data' and the chart titles eleven points. Never cited by number: the reading that follows is a narrative of the 2008-2010 cholera and the 2012 drought, not a pointer.
6. p18 **line** conf=high panels=1
   bbox [70.92, 63.0, 524.52, 369.72] (?)
   cap: Figure 6: Comparison of Congo’s FI with and without climate change’s effect
   note: The counterfactual: two eleven-point series on one frame - the observed index and the index recomputed with the climate indicators frozen at their 2006 values. Legend inside, upper right, boxed, two keys, both ungrammatical ('with the climate change', 'without the climate change'). Title inside the frame. Axis titles 'Fragile Index' and 'Year', boxed axes, no grid, no value labels. The paper's point - the counterfactual line rises slowly, so climate change is what makes the state fragile - is a GAP between two curves, and the axis is again cropped (0.28-0.44), which stretches that gap while cutting off how far the observed line has travelled. Cited in the sentence that decodes the colours rather than in the sentence that states the finding.
7. p19 **line** conf=high panels=1
   bbox [70.92, 63.0, 524.52, 317.76] (?)
   cap: Figure 7: FI of Bangladesh
   note: The Bangladeshi twin of Figure 5, four pages later: one dark-blue series with downward triangles, eleven annual points, title inside the frame, 'Fragile Index' and 'Year' on the axes, boxed, cropped to 0.32-0.42 - a third range for the same index. Two hairline rule fragments survive inside the measured box, one clipped above the title and one below the x axis; they are furniture, not data. Never cited by number: the prose reads it as 'As the chart above shows', the only referent in the paper that is positional rather than numbered, and one of three exhibits introduced without a number at all.
8. p20 **line** conf=high panels=1
   bbox [111.96, 165.0, 480.48, 367.56] (?)
   cap: Figure 8: Prediction of Bangladesh
   note: The forward extrapolation: about eighty annual points of GM(1,1) output from 2019 to 2088 climbing 0.395 to 0.645, markers so dense along the line that they merge into a thick stroke. Two unlabelled annotation rules carry the entire argument - a horizontal red line at 0.6 and a vertical green line at about 2074 - with no legend, no text and no value, so the crossing that the prose reports as 'BD will be stable in 60 years, namely 2076' cannot be read off the chart without knowing where 0.6 came from. Near the right edge the green vertical cuts through the 2070 and 2080 tick labels and they collide into one blob. Y axis 0.35-0.65, a fourth range for the same index.
9. p23 **line** conf=high panels=1
   bbox [111.84, 86.4, 480.36, 287.16] (?)
   cap: Figure 9: Analysis of 1
   note: The sensitivity study the paper promised, and the only chart in it with more than two series: five open-triangle lines for the five settings of the AHP weight, 2006-2016, legend boxed inside at lower right. Both the legend and the caption have LOST the Greek letter - the keys print '01 = 0.8' and the caption 'Analysis of 1' where the weight symbol should be - so the parameter this whole section varies is unnameable from either. No axis titles on this one (the only chart after Figure 4 without them), y 0.0-0.5 on a 0.1 step, five curves inside a band about 0.05 wide: the flatness is real, and it is also what a 0.5-tall axis makes of any band.

## tables
1. p13 table-grid bbox [133.56, 131.08, 459.0, 216.28]
   cap: Table 2: Examples of Relationship
2. p15 table-grid bbox [170.02, 672.55, 426.98, 759.8]
   cap: Table 3: Classification of 20 states
3. p21 table-grid bbox [99.85, 86.33, 495.0, 251.08]
   cap: 
4. p21 table-grid bbox [127.44, 646.48, 467.85, 758.14]
   cap: 
5. p22 table-grid bbox [190.02, 248.8, 403.98, 279.98]
   cap: Table 4: FI of different continents
6. p26 table-grid bbox [164.67, 303.55, 432.63, 633.36]
   cap: 
7. p26 table-grid bbox [71.15, 648.53, 553.15, 766.9]
   cap: 
8. p27 table-grid bbox [111.96, 162.36, 480.48, 355.32]
   cap: Figure 10: Climate Expenditure: 2011-2014
9. p27 table-grid bbox [111.96, 411.96, 480.48, 653.28]
   cap: Figure 11: Climate Expenditure: 2015-2017

## excluded
- p10 not-an-exhibit bbox [181.8, 245.28, 303.36, 286.56] 
- p10 not-an-exhibit bbox [242.04, 502.68, 353.04, 591.96] 
- p12 not-an-exhibit bbox [71.04, 207.6, 283.92, 240.84] 
- p15 not-an-exhibit bbox [106.32, 48.6, 491.04, 118.32] 
- p16 split-across-pages bbox [170.02, 48.65, 426.98, 79.66] 

## distillation fields

figure 1 p7: sec=3 Model PSA > 3.1 PSR Figure 1: PSR Model [model] zone=bottom order=1/1 area=0.0555 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p8: sec=3.2 PSA > 3.2.1 Identify indicators [symbols] zone=top order=2/1 area=0.1925 solo=False
  family=table-as-figure panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p12: sec=3.3 Analyze direct and indirect impacts of climate change [model] zone=bottom order=3/1 area=0.146 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p15: sec=3.4 Test PSA [test] zone=middle order=5/1 area=0.1669 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=15 lead=0 count=1 read=2 gap=0 pattern=direct style=['Figure 4']
  caption: Figure N: words=19 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p17: sec=4 Case Study > 4.1 Study 1: Democratic Republic Of the Congo > 4.1.1 Climate change effects of Congo [result] zone=middle order=7/1 area=0.154 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p18: sec=4 Case Study > 4.1 Study 1: Democratic Republic Of the Congo > 4.1.2 The FI without climate change effects [result] zone=top order=8/1 area=0.2777 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=3 gap=0 pattern=direct style=['Figure 6']
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p19: sec=4 Case Study > 4.2 Study 2: People’s Republic of Bangladesh > 4.2.1 Climate change effects of Bangladesh [result] zone=top order=9/1 area=0.2307 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p20: sec=4 Case Study > 4.2 Study 2: People’s Republic of Bangladesh > 4.2.2 Prediction [result] zone=top order=10/1 area=0.149 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=20 lead=0 count=1 read=1 gap=0 pattern=figure-n-shows style=['Figure 8']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p23: sec=6 Sensitivity Analysis [sensitivity] zone=top order=14/1 area=0.1477 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=23 lead=0 count=1 read=1 gap=0 pattern=figure-n-shows style=['Figure 9']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p13: sec=3.3 Analyze direct and indirect impacts of climate change [model] zone=top order=4/1 area=0.0554 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=13 lead=0 count=1 read=0 gap=0 pattern=direct style=['Table 2']
  caption: Table N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 3x2 header=1 rules=booktabs zebra=False merged=True diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 2 p15: sec=3.4 Test PSA [test] zone=bottom order=6/2 area=0.0448 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=16 lead=-1 count=1 read=0 gap=1 pattern=direct style=['Table 3']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 8x2 header=2 rules=boxed zebra=False merged=True diag=False units_hdr=False dec=False num=0 txt=2 width=half orient=portrait cont=True

table 3 p21: sec=4 Case Study > 4.2 Study 2: People’s Republic of Bangladesh > 4.2.3 Effect of Human Intervention [model] zone=top order=11/1 area=0.13 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 4 p21: sec=4 Case Study > 4.2 Study 2: People’s Republic of Bangladesh > 4.2.4 Total cost [result] zone=bottom order=12/2 area=0.0759 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x5 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 5 p22: sec=5 Further Exploration [result] zone=top order=13/1 area=0.0133 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=22 lead=0 count=1 read=0 gap=0 pattern=direct style=['Table 4']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 2x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=half orient=portrait cont=False

table 6 p26: sec=未编号标题：Appendices > 未编号标题：Appendix A FI of Country [appendix] zone=middle order=15/1 area=0.1764 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 21x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=2 width=half orient=portrait cont=False

table 7 p26: sec=未编号标题：Appendices > 未编号标题：Appendix A FI of Country [appendix] zone=bottom order=16/2 area=0.1139 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x11 header=1 rules=no-rules zebra=False merged=False diag=False units_hdr=False dec=False num=10 txt=1 width=full orient=portrait cont=False

table 8 p27: sec=未编号标题：Appendices > 未编号标题：Appendix B Climate expenditure of Bangladesh [appendix] zone=top order=17/1 area=0.142 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 11x13 header=3 rules=boxed zebra=False merged=True diag=False units_hdr=False dec=False num=12 txt=1 width=full orient=portrait cont=False

table 9 p27: sec=未编号标题：Appendices > 未编号标题：Appendix B Climate expenditure of Bangladesh [appendix] zone=middle order=18/2 area=0.1775 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 22x5 header=2 rules=boxed zebra=False merged=True diag=False units_hdr=True dec=False num=4 txt=1 width=full orient=portrait cont=False

