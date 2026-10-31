# P-F-2019-1905127-b4a0bea2 — figure census

- layout sha `31843655ba24da37`, 26 pages, 12 measured regions
- accounted: 6 figures, 3 tables, 3 excluded, 0 unaccounted
- families: flowchart-or-schematic 1, line 2, map-or-plan-view 1, node-link-network 1, scatter 1, table-grid 3

1. p5 **flowchart-or-schematic** conf=high panels=1
   bbox [19.4, 163.07, 575.54, 317.67] (?)
   cap: Figure 1 Overview of Our Work
   note: the paper's whole argument drawn as a bubble chart: 'Digital currency system' sits at the centre, four thick coloured arrows fan out to the four themes it displaces ('Commercial Bank', 'Risk managment' [sic], 'Monetary policy', 'Regional economic difference'), and dotted arrows drop to its three scales ('Individual', 'State', 'International') and on into a dashed 'Stability evaluation' box. Thirteen italic annotations ride leader rules into the branches ('Fisher's equation', 'DMP', 'Control measures?Tax rate', 'Optimal currency area'), so the drawing doubles as the contents page of sections 3-5. No axes, no scale, no legend, no colourbar: the two stroke weights (solid = displaced, dotted = derived) are the only encoding.
2. p9 **node-link-network** conf=high panels=1
   bbox [189.75, 88.14, 405.9, 257.68] (?)
   cap: Figure 2 Matching relation
   note: the search-and-matching triangle as ink: 'Exchange of goods' on top, the double-arrow pair down to 'Seller 1-f-d', and the two buyer groups 'Buyer f ∈ ( 0, 1 )' and 'Buyer d ∈ ( 0, 1 )' below, joined by four dotted connectors each labelled with the matching probability that runs along it (P(f-o), P(o-f), P(d-o), P(o-d)). Four boxes, eight edge labels, no axes and no legend. The figure is the only place in the paper where the four transition probabilities of equation (1) are laid out in space; the prose never names it, and the sentence after the caption explains formula (1) without ever saying 'Figure 2'.
3. p19 **map-or-plan-view** conf=high panels=1
   bbox [90.0, 87.09, 505.21, 267.39] (?)
   cap: Figure 3: World Monetary Equilibrium
   note: the 130-country acceptance result drawn as a choropleth: one categorical fill per country, four legend swatches stacked inside the map over the Pacific ('Both Currencies', 'Legal Currency Only', 'Digital Currency Only', 'Missing Data'), the Antarctic strip greyed into the missing-data colour. No axes, no scale, no colourbar, no data labels - the legend is the only key, and it sits inside the drawing because the ocean there is empty. This is the file's first caption with a colon: the caption dialect changes exactly where the paper stops arguing a model and starts reporting a computation.
4. p20 **line** conf=high panels=1
   bbox [74.05, 374.53, 508.95, 592.08] (?)
   cap: Figure 4: Market Share of Digital Currency in the United State (stable state)
   note: three polyline traces of a simulated market share over 2018-2027, told apart only by marker shape and colour (red squares, blue triangles, green triangles) and keyed by a legend inside the plot's upper right. Title above the plot ('Market Share of Digital Currency in the United State (stable state)'), y-axis 'Market Share of Digital Currency' on a 0.1-0.8 scale, x-axis 'Year'. The figure is introduced by the number the simulation produced, not by a pointer: the sentence before the caption already gives the answer ('will stabilize at about 65.21%'), so the chart is evidence shown after the verdict.
5. p21 **line** conf=high panels=1
   bbox [90.0, 72.0, 505.3, 264.1] (?)
   cap: Figure 5: Market Share of Digital Currency in the United State (Imbalance state)
   note: the same three-trace template as Figure 4 with the legend keys relabelled ('Zn=15%', 'Zn=45%', 'Zn=55%' here against '20=15%', '20=30%', '20=55%' there - the initial-condition symbol changes mid-pair), the y scale cut to 0-0.7, and one in-plot annotation block with an arrow: 'Supernational financial institution loses its regulatory capacity', pointing up-left at the 2023 peak. The sentence that introduces it is the sentence that closed Figure 4, so one line of prose serves as the read-back of the first chart and the lead-in of the second, and no pointer names either.
6. p25 **scatter** conf=high panels=1
   bbox [90.0, 113.12, 504.6, 305.12] (?)
   cap: 
   note: an uncaptioned MATLAB output plate: blue '+' observations of total US trade volume against year 1990-2030 with a red straight fit laid over them, title in the plot 'Total Trade Volume of the United State' (the heading above it repeats the same words), y-axis 'Trade Volume' with a x10^5 multiplier, x-axis 'Year'. No legend, no colourbar, no caption, and no panel letter - the object is identified only by the appendix heading and by its own axis titles. It is printed ABOVE the code that draws it ('2. Fitting code' and the load/polyfit block follow the plot), so the heading '1 Total Trade Volume of the United State' - a numbered list item, not a numbered section - is what files it.

## tables
1. p5 table-grid bbox [111.02, 596.23, 511.78, 752.86]
   cap: Table 1 Parameter List
2. p16 table-grid bbox [90.02, 368.81, 505.42, 515.35]
   cap: Table 2 Estimation parameter interpretation
3. p18 table-grid bbox [89.54, 423.29, 505.18, 484.63]
   cap: Table 3 Regression results

## excluded
- p4 not-an-exhibit bbox [90.02, 127.22, 505.41, 290.33] p4's upper block is body prose, not an exhibit: the opening paragraph of 1.1 Background ('Ever since Cong Nakamoto has released Bitcoin in 2009 …'), set as a plain column with no frame, rule, tint or caption. The layout pass measured it only because its column is dense enough to look like a block; the crop shows ragged right line ends and no bounding rule of any kind.
- p4 not-an-exhibit bbox [90.02, 330.53, 505.42, 418.13] p4's lower block is the second paragraph of the same prose run (1.2 Restatement of the Problem: 'Our team will measure the impact of digital currencies on the legal tender and financial markets at the individual, national and global level …'), again unframed, uncaptioned and unnumbered, with no axes, grid, nodes or image content. Two prose blocks on one page are one page of text, not two exhibits.
- p6 split-across-pages bbox [111.02, 72.0, 511.78, 352.97] the body of Table 1 carried over to the top of p6: eleven more parameter rows, no caption, no number and no repeated 'Parameter | Description' header, opening at the first rule and closing with the heavy foot rule. Table 1 is one exhibit spanning p5-p6, recorded once on p5 with `continued`, so this region is the continuation rather than a second table.

## distillation fields

figure 1 p5: sec=1 Introduction > 1.3 Overview of Our Work [other] zone=top order=1/1 area=0.1715 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p9: sec=3 Analysis and Model Building > 3.1.2 Search and Matching Model under Dual Monetary System > 3.1.2.2 Equilibrium State of the Model [model] zone=top order=3/1 area=0.0731 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=1 gap=None pattern=none style=[]
  caption: Figure N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p19: sec=4 Empirical Model based on Algebraic Operation > 4.1 Empirical Study Based on Micro-model > 4.1.4 The Final Results of the Empirical Model [result] zone=top order=6/1 area=0.1494 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=18 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['figure below']
  caption: Figure N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p20: sec=4 Empirical Model based on Algebraic Operation > 4.2 Empirical Study Based on Macro-model [model] zone=middle order=7/1 area=0.1888 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=13 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 5 p21: sec=4 Empirical Model based on Algebraic Operation > 4.2 Empirical Study Based on Macro-model [model] zone=top order=8/1 area=0.1592 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=13 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 6 p25: sec=Appendix > 1 Total Trade Volume of the United State [appendix] zone=top order=9/1 area=0.1588 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p5: sec=2 General Assumptions and Justifications > 2.2 Variable Description [symbols] zone=bottom order=2/2 area=0.1252 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 7x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=True

table 2 p16: sec=4 Empirical Model based on Algebraic Operation > 4.1 Empirical Study Based on Micro-model > 4.1.2 Parameter Estimation and Result Solution [solution] zone=middle order=4/1 area=0.1215 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=16 lead=0 count=1 read=1 gap=0 pattern=as-shown-in style=['shown as follow']
  caption: Table N words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 8x2 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 3 p18: sec=4 Empirical Model based on Algebraic Operation > 4.1 Empirical Study Based on Micro-model > 4.1.3 Empirical Model Based on Econometric Methods [result] zone=middle order=5/1 area=0.0509 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=18 lead=0 count=1 read=1 gap=0 pattern=as-shown-in style=['as follows']
  caption: Table N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 4x9 header=1 rules=booktabs zebra=False merged=True diag=False units_hdr=False dec=False num=8 txt=1 width=full orient=portrait cont=False

