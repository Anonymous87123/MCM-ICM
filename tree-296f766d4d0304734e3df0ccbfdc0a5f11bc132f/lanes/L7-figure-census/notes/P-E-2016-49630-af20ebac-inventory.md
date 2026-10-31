# P-E-2016-49630-af20ebac — figure census

- layout sha `f375cecad160fabc`, 23 pages, 15 measured regions
- accounted: 6 figures, 9 tables, 0 excluded, 0 unaccounted
- families: flowchart-or-schematic 1, line 3, map-or-plan-view 1, scatter 1, table-grid 9

1. p9 **flowchart-or-schematic** conf=high panels=1
   bbox [116.22, 70.87, 479.07, 254.89] (?)
   cap: Figure 1: Main Factors of ESM
   note: pasted raster tree in rounded light-blue boxes with thin double-headed edges: the root "Economic Scarcity Metric(ESM)" branches to "Technology & Infrastructure" and "Human factor", which carry three leaves (Irrigation efficiency, GERD rate, Access to improved water) and two leaves (Urbanization rate, Primary enrollment rate) respectively; five leaves against two branches, no numbers and no axis anywhere, and the edges are drawn with arrowheads at both ends, so the diagram does not say which way the aggregation runs; GERD is never expanded, here or in any table.
2. p12 **scatter** conf=high panels=1
   bbox [161.57, 70.87, 433.71, 250.41] (?)
   cap: Figure 2: PSM and ESM Results for 83 Countries
   note: pasted Excel dot plot with no legend and no in-art title: 83 countries as small blue dots on discrete PSM levels 1, 2, 3 and 4 against ESM from 0 to 1 in steps of 0.2; eight dots are labelled in place (Israel, Tunisia, Pakistan, Sudan, Belgium, Kenya, Japan, Mozambique) and those eight are the ones Figure 4 re-plots; the y-axis title is clipped at the plot edge, printing "PSM" and a stray ")" glyph in the left margin, and the dots overlap densely along PSM=1, so the count of 83 cannot be verified from the artwork.
3. p12 **map-or-plan-view** conf=high panels=1
   bbox [161.57, 285.88, 433.71, 424.78] (?)
   cap: Figure 3: UN Water Scarcity Map.Source:UNEP Website.
   note: third-party UNEP choropleth of the world, pasted as raster and the only exhibit that is not the team's own drawing: five colour bands from pale yellow to dark red keyed by an in-art legend "Water stress indicator (WSI) in major basins:" running 0, 0.3, 0.5, 0.7, 1 and more under the labels Slightly / Moderately / Heavily / over-exploited; a "Sources: Smakhtin, Revenga and Doll, 2004." line sits at the lower left and a Pacific Institute credit at the lower right, both inside the image; no country names are printed, so the body's reading of it ("countries printed blue and yellow") rests on the reader's geography.
4. p13 **line** conf=high panels=1
   bbox [116.22, 70.87, 479.07, 289.48] (?)
   cap: Figure 4: Sensitivity Analysis of α Using Data from 8 Countries
   note: Excel line chart with round markers, eight country series and no in-art title: Mozambique, Belgium, Kenya, Israel, Tunisia, Pakistan, Sudan and Japan plotted over α from 0.4 to 1.6 with ticks every 0.2; y runs 0 to 1 in steps of 0.1 but its axis title is clipped to a bare "ability" at the left edge, so the quantity being plotted is never printed; the legend sits below the plot area inside a framed art box, two rows of four; Sudan alone sits near 0.9 across the whole range while Japan stays near 0.16; the caption says the α range is 0.5 to 1.5 and the axis says 0.4 to 1.6.
5. p17 **line** conf=high panels=1
   bbox [116.22, 164.6, 479.08, 380.91] (?)
   cap: Figure 5: Sensitivity Analysis in TSM Forecasting
   note: Excel line chart with round markers, two series and no in-art title: "now" (blue) starts at 0.505 and falls slowly, "15 years later" (red) starts at 0.34 and rises to meet it, and the two converge at about 0.45 by α=2; x α from 0 to 2 in steps of 0.5, y TSM 0 to 0.6 in steps of 0.1, legend below the plot area, no grid; the y quantity is labelled only by the axis title "TSM", which the paper never expands at this point.
6. p20 **line** conf=high panels=1
   bbox [161.57, 376.6, 433.71, 576.73] (?)
   cap: Figure 6: Sensitivity Analysis in TSM with and without Our Plan
   note: Excel line chart with round markers, two series, legend below the plot area inside a framed art box and no in-art title: "without measures" (blue) runs from 0.335 to 0.45 and "taking measures" (red) from 0.315 to 0.41 over α from 0 to 2, so the two curves rise in parallel and the plan shifts the level down by about 0.03 without changing the slope; y TSM 0 to 0.5 in steps of 0.05, x ticks every 0.5; the pair is the same two-curve form as Figure 5 but with a different comparison in the legend.

## tables
1. p4 table-grid bbox [109.49, 318.01, 485.78, 610.91]
   cap: Table 1: Variable Description
2. p5 table-grid bbox [122.01, 433.39, 473.27, 503.13]
   cap: Table 2: The Falkenmark Indicator.
3. p6 table-grid bbox [133.26, 467.16, 462.01, 536.5]
   cap: Table 3: CI Value.
4. p8 table-grid bbox [133.87, 388.58, 461.41, 457.92]
   cap: Table 4: CI Value.
5. p11 table-grid bbox [118.33, 516.31, 476.94, 598.4]
   cap: Table 5: The Weights of Factors
6. p16 table-grid bbox [130.66, 71.07, 464.61, 154.75]
   cap: Table 6: Factor Prediction Results in ESM Model
7. p16 table-grid bbox [160.56, 480.64, 434.72, 592.22]
   cap: Table 7: Factor Prediction Results in PSM Model
8. p19 table-grid bbox [70.87, 539.19, 557.95, 650.77]
   cap: Table 8: Summary of The Estimation
9. p20 table-grid bbox [70.87, 71.07, 565.26, 153.96]
   cap: Table 9: Impact of Factor Settings

## distillation fields

figure 1 p9: sec=3 Total Scarcity Metric Model > 3.3 Construction of ESM [model] zone=top order=5/1 area=0.133 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=1 count=2 read=1 gap=None pattern=parenthetical style=['Figure 1']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p12: sec=3 Total Scarcity Metric Model > 3.5 Veriﬁcation and Sensitivity Analysis [sensitivity] zone=top order=7/1 area=0.097 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=1 count=5 read=1 gap=None pattern=parenthetical style=['Figure 2']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p12: sec=3 Total Scarcity Metric Model > 3.5 Veriﬁcation and Sensitivity Analysis [sensitivity] zone=middle order=8/2 area=0.075 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=12 lead=0 count=5 read=1 gap=None pattern=parenthetical style=['Figure 3']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p13: sec=3 Total Scarcity Metric Model > 3.5 Veriﬁcation and Sensitivity Analysis [sensitivity] zone=top order=9/1 area=0.158 solo=False
  family=line panels=1 layout=1 shared=False legend=below cbar=False 3d=no printed=False
  mention: first=12 lead=1 count=2 read=1 gap=None pattern=parenthetical style=['Figure 4']
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p17: sec=4 Water Situation in Pakistan > 4.2 Forecasting the future situation > 4.2.4 Forecasting Results [result] zone=top order=12/1 area=0.157 solo=False
  family=line panels=1 layout=1 shared=False legend=below cbar=False 3d=no printed=False
  mention: first=17 lead=0 count=1 read=1 gap=None pattern=parenthetical style=['Figure 5']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p20: sec=5 Our Plan for Pakistan > 5.2 How Our Plan Changes Water Scarcity > 5.2.3 Sensitivity Analysis [sensitivity] zone=middle order=15/2 area=0.109 solo=False
  family=line panels=1 layout=1 shared=False legend=below cbar=False 3d=no printed=False
  mention: first=20 lead=0 count=2 read=1 gap=None pattern=parenthetical style=['Figure 6']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p4: sec=2 General Assumptions and Variable Description > 2.2 Variable Description [other] zone=middle order=1/1 area=0.22 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 20x3 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=1 txt=2 width=full orient=portrait cont=False

table 2 p5: sec=3 Total Scarcity Metric Model > 3.1 Review of Literatures [test] zone=middle order=2/1 area=0.049 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=5 lead=0 count=1 read=1 gap=None pattern=parenthetical style=['Table 2']
  caption: Table N: words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x3 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=False

table 3 p6: sec=3 Total Scarcity Metric Model > 3.1 Review of Literatures [test] zone=middle order=3/1 area=0.045 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=6 lead=0 count=1 read=1 gap=None pattern=parenthetical style=['Table 3']
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 3x5 header=2 rules=boxed zebra=False merged=False diag=False units_hdr=True dec=False num=4 txt=1 width=full orient=portrait cont=False

table 4 p8: sec=3 Total Scarcity Metric Model > 3.2 Construction of PSM [model] zone=middle order=4/1 area=0.045 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=8 lead=0 count=2 read=1 gap=None pattern=parenthetical style=['Table 4']
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 3x5 header=2 rules=boxed zebra=False merged=False diag=False units_hdr=True dec=False num=4 txt=1 width=full orient=portrait cont=False

table 5 p11: sec=3 Total Scarcity Metric Model > 3.4 Construction of TSM [model] zone=middle order=6/1 area=0.059 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=11 lead=0 count=1 read=1 gap=None pattern=parenthetical style=['Table 5']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=True num=2 txt=2 width=full orient=portrait cont=False

table 6 p16: sec=4 Water Situation in Pakistan > 4.2 Forecasting the future situation > 4.2.2 Grey Forecasting Model [model] zone=top order=10/1 area=0.056 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=15 lead=1 count=3 read=1 gap=None pattern=parenthetical style=['Table 6']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=True dec=False num=3 txt=1 width=full orient=portrait cont=False

table 7 p16: sec=4 Water Situation in Pakistan > 4.2 Forecasting the future situation > 4.2.3 Regression Analysis [result] zone=middle order=11/2 area=0.061 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=16 lead=0 count=3 read=1 gap=None pattern=parenthetical style=['Table 7']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x3 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=False

table 8 p19: sec=5 Our Plan for Pakistan > 5.2 How Our Plan Changes Water Scarcity > 5.2.2 The Performance [other] zone=bottom order=13/1 area=0.108 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=0 count=2 read=1 gap=None pattern=parenthetical style=['Table 8']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x5 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 9 p20: sec=5 Our Plan for Pakistan > 5.2 How Our Plan Changes Water Scarcity > 5.2.2 The Performance [other] zone=top order=14/1 area=0.082 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=1 count=1 read=1 gap=None pattern=parenthetical style=['Table 9']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 5x6 header=1 rules=boxed zebra=False merged=True diag=False units_hdr=False dec=False num=4 txt=2 width=full orient=portrait cont=False

