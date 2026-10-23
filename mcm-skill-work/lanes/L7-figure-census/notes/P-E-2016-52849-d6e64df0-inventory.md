# P-E-2016-52849-d6e64df0 — figure census

- layout sha `c1b279593d5f2fba`, 32 pages, 12 measured regions
- accounted: 10 figures, 2 tables, 0 excluded, 0 unaccounted
- families: bar 5, flowchart-or-schematic 2, line 1, map-or-plan-view 1, node-link-network 1, table-grid 2

1. p4 **map-or-plan-view** conf=high panels=2
   bbox [177.2, 228.0, 434.8, 441.6] (?)
   cap: Figure 1: A) The UNEP characterized multiple regions in Haiti as moderately exploited or over- exploited based on Water Stress Indicators (WSI) in 2004. (5) B) According to the UNEP, “This 2008 update of the ‘Vital Water Graphics’ is aimed at giving an overview of the state of water resources in the
   note: two UNEP choropleth maps pasted side by side and labelled A and B in their own corners: the left map shades the Caribbean with a five-step Water Stress Indicator ramp (0, 0.3, 0.5, 0.7, 1 and more, legend inside at its foot reading Slightly exploited / Moderately exploited / Heavily exploited / over-exploited) and marks five island states with oversized coloured circles of differing radius; the right map is the western hemisphere with a percentage-access ramp (more than 95 %, 83 to 95 %, 65 to 83 %, less than 65 %, No data, plus a "World average" rule) and circles Haiti and one other state; both legends sit inside the artwork, no axes and no gridlines, and the second panel carries an in-art credit line; the caption prints below the pair and does the panel work the art does not - its A) and B) sentences are the only panel labels, since neither map repeats "A" or "B" in text.
2. p5 **flowchart-or-schematic** conf=high panels=1
   bbox [80.1, 365.12, 531.9, 582.92] (?)
   cap: Figure 2: We created a systems model for water usage systems using Vensim software (3). Global water systems involve agriculture, industry, and residential water usage, with adjustable rates based on inputted variables. This model can be customized to ﬁt any region.
   note: the Vensim stock-and-flow diagram of the systems-network model: eight labelled rectangles (locked, available, potable, external, agriculture, industrial, residential, elite) joined by bold direction arrows, with twelve valve markers carrying lowercase labels (waste, contamination, more runoff, runoff, funnel, unlock, filter, transportation, personal filtration, transport, donate, corruption); no axes, no numeric scale and no legend box - the box labels are the only key; the "waste" label is detached from its valve and floats well below the top feed line, the return lines from agriculture and industrial cross the feed lines with no overpass marks so link direction has to be inferred, and the "locked" stock is drawn much larger than the others with nothing explaining the size; the caption prints below the artwork.
3. p9 **flowchart-or-schematic** conf=high panels=1
   bbox [104.4, 493.02, 507.6, 572.32] (?)
   cap: Figure 3: Logic Diagram of Groundwater Flow Algorithm
   note: a three-box horizontal flowchart of the groundwater algorithm, no axes, no legend and no numeric values: box 1 "color -> hydraulic head (n_H)", box 2 a large frame holding "n_i - n_0" above an inset plus-shaped cluster of cells n1/n2/n3/n4 around the centre cell n0, box 3 "n_0 += K*value", with plain arrows box1 to box2 to box3; the cell-cross inset is never explained in the art and the small n-labels are barely legible at print size; the caption prints below the diagram and is the shortest in the paper, four words plus the number.
4. p13 **node-link-network** conf=high panels=1
   bbox [140.5, 299.07, 471.5, 537.57] (?)
   cap: Figure 4: The user interface and structure of the Haitian speciﬁc agent based networks model
   note: a NetLogo interface screenshot pasted as a single raster: the left control column carries the buttons setup and go, a source chooser set to "elite" and six sliders with their current values printed (avg-degree 8, common-demand 0.5, elite-demand 2.0, gang-demand 5.0, number-of-nodes 100, water-given 30), and the right half is the black world view with roughly a hundred white circular nodes on grey edges plus a handful of coloured typed nodes labelled elite, distributor and healthcenter; no axes and no legend, and the node labels are small, low contrast and in places overprinted on each other, so the network topology it is meant to evidence cannot be read off the page; the caption prints below the screenshot and is the only place the model is described.
5. p15 **bar** conf=high panels=1
   bbox [187.2, 57.6, 424.8, 232.2] (?)
   cap: Figure 5: We simulated 100 runs of the model for each factor, with no population growth, 17% population growth (as predicted for Haiti), and 25% population growth (as an overestimate to measure robustness), with the currently used elite distribution method.
   note: single-panel vertical bar chart titled inside the art "Mean Water vs Population Size with Elite Distribution": three bars (grey, navy, crimson) over the categories None, 17 %, 25 % on x "Population Growth", y "Mean Water / L/person" printed as a three-line stacked title with NO numeric ticks and no scale at all, so the only magnitudes are the printed value labels 0.081, 0.067 and 0.062 above the bars; no legend names the three colours even though colour is the only encoder of the factor level; the caption prints below the chart. This is the template that Figures 10 and both p16 panels reuse.
6. p16 **bar** conf=high panels=1
   bbox [57.6, 75.33, 301.04, 280.22] (?)
   cap: Figure 7: In the ﬁgure on the left, the mean waters received are compared between distribution method A, the current method, and distribution method B, our proposed method. The higher mean water is indicative of a more favorable solution. As seen on the right, distribution method B also does a bette
   note: left panel of the Figure 7 pair, a two-bar chart titled "Mean Water versus Distribution Method": crimson and navy bars over ticks A and B on x "Distribution Method", y "Mean Water / L/person" stacked in three lines with no numeric ticks, value labels 0.08 and 0.3 printed above the bars, and the key set as bare wrapped text to the right of the plot rather than in a keyed legend, splitting the word mid-way as "distributi" / "on centers" and clipping at the plot edge; this is the "figure on the left" the shared caption refers to, and the caption prints below the pair on the page.
7. p16 **bar** conf=high panels=1
   bbox [310.96, 57.6, 554.41, 280.22] (?)
   cap: 
   note: right panel of the same Figure 7 row, a two-bar chart titled "Standardized Need vs Distribution Method": crimson and navy bars over A and B, y "Stand. / Need" with no numeric ticks, value labels 0.041 and 0.035, and bare key text outside the plot on the right reading "A) Elites" and "B) Distribution centers"; it carries no figure number and no caption of its own - it is the second half of Figure 7, whose single caption is printed once under the row - so it records caption_source none; its bar colours and its missing y scale match the panel to its left, but the quantity plotted (standardized need) is the lower-is-better counterpart, which only the caption explains.
8. p16 **bar** conf=high panels=1
   bbox [57.6, 505.38, 301.03, 683.82] (?)
   cap: Figure 9: Comparison of resistance to population growth among the two methods The results indicate that, while both methods are sensitive to population growth with each
   note: left panel of the Figure 9 pair, a three-bar chart titled "Mean Water vs Population Size with Center Distribution": grey, navy and crimson bars over None, 17 %, 25 % on x "Population Growth", y "Mean Water / L/person" with no numeric ticks, value labels 0.3, 0.26 and 0.24; no legend, and the "None" tick label is printed in grey rather than black; the rotated y title of the neighbouring right-hand chart crowds against this raster's edge; the shared caption prints below the row, and it is the same three-bar template as Figure 5 with the distribution method swapped.
9. p16 **line** conf=high panels=1
   bbox [310.96, 543.16, 554.4, 683.82] (?)
   cap: 
   note: right panel of the Figure 9 row, and the only line chart in the paper: an Excel-default plot with a light frame and horizontal gridlines, titled across two lines "Mean Water versus Population Size by Distribution Method", y "Mean Water (L/person)" with ticks 0 to 0.35 at 0.05 and x "% Population Growth" with ticks 0 % to 30 % at 5 %; two marker series (Elite Distribution blue, Center Distribution orange) drawn at only three x positions on a continuous 0-30 axis, with the key set outside the plot on the right and no per-point value labels; it prints no number and no caption of its own - it is the second half of Figure 9 - so caption_source none; its whole styling, and its readable numeric y axis, break with the hand-styled bar charts it is printed beside.
10. p17 **bar** conf=high panels=1
   bbox [175.5, 314.18, 436.5, 504.38] (?)
   cap: Figure 10: We simulated 100 runs of the model for each ??ﬁll what we ran for degrees
   note: the last exhibit, a single three-bar chart titled "Mean Water versus Average Degree with Elite Distribution": grey, navy and crimson bars over Average Degree categories 2, 5 and 10, y "Mean Water / L/person" with no numeric ticks, value labels 0.008, 0.0642 and 0.0897 above the bars, no legend; it is the Figure 5 template with the factor on x swapped, and its caption is the only caption in the paper that was never finished: it prints "We simulated 100 runs of the model for each ??fill what we ran for degrees", the literal "??" placeholder marker surviving into the printed PDF, followed by an unfinished clause and no closing full stop.

## tables
1. p3 table-grid bbox [91.96, 57.8, 520.04, 276.88]
   cap: 
2. p5 table-grid bbox [57.6, 155.47, 570.34, 273.83]
   cap: 

## distillation fields

figure 1 p4: sec=2 Haiti: A Case of Extreme Economic Water Scarcity > 2.2 Current Situation [other] zone=middle order=2/1 area=0.114 solo=False
  family=map-or-plan-view panels=2 layout=1x2 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=79 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p5: sec=3 Models > 3.1 Systems-Network Model [model] zone=middle order=4/2 area=0.203 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=6 lead=-1 count=0 read=1 gap=None pattern=direct style=[]
  caption: Figure N: words=41 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p9: sec=3 Models > 3.2 Algorithmic Approach > 3.2.2 Physical Scarcity Analysis [model] zone=bottom order=5/1 area=0.066 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p13: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.1 Applied to Haiti [model] zone=middle order=6/1 area=0.163 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=0 read=1 gap=None pattern=direct style=[]
  caption: Figure N: words=16 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p15: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.1 Applied to Haiti [result] zone=top order=7/1 area=0.086 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=40 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p16: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.2 Intervention Plan [result] zone=top order=9/1 area=0.103 solo=False
  family=bar panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=59 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p16: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.2 Intervention Plan [result] zone=top order=8/2 area=0.112 solo=False
  family=bar panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p16: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.2 Intervention Plan [result] zone=bottom order=10/3 area=0.09 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=26 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p16: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.2 Intervention Plan [result] zone=bottom order=11/4 area=0.071 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p17: sec=3 Models > 3.3 Agent-Based Networks Approach > 3.3.3 Sensitivity Analysis [result] zone=middle order=12/1 area=0.102 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=17 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p3: sec=1 Introduction > 1.2 Analysis of the Problem [other] zone=top order=1/1 area=0.193 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=2 lead=1 count=0 read=1 gap=None pattern=direct style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 5x2 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 2 p5: sec=2 Haiti: A Case of Extreme Economic Water Scarcity > 2.2 Current Situation > 2.2.1 Comparison of Current Common Interventions in Haiti (2) [evaluation] zone=top order=3/1 area=0.125 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x6 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=6 width=full orient=portrait cont=False

