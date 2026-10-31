# P-B-2010-7947-b6007ae0 — figure census

- layout sha `c588ab8df26941eb`, 28 pages, 18 measured regions
- accounted: 8 figures, 2 tables, 8 excluded, 0 unaccounted
- families: bar 1, composite-panel 1, flowchart-or-schematic 1, heatmap-or-contour 3, line 1, map-or-plan-view 1, table-grid 2

1. p11 **flowchart-or-schematic** conf=high panels=1
   bbox [196.31, 190.85, 410.31, 363.35] (?)
   cap: Figure 1: The discretization of a square search area into sectors. In this figure k is equal to the side length of the search area divided by ∆s.
   note: a k-by-k grid of squares labelled S(i,j) with vertical ellipses between the blocks and a brace marked with the side length delta s at the left; no axes, the labels are the content
2. p16 **heatmap-or-contour** conf=high panels=2
   bbox [148.87, 142.73, 292.87, 250.73] (?)
   cap: Figure 2: Comparison of prioritized search areas of a hypothetical criminal com- mitting crimes along the unit circle given by a centralization method and a decay method.
   note: (a) is a single red core at the origin, (b) a ring of ten separated hot spots on the unit crime circle; both on a -2..2 square, colour bar outside the axes reading high to low
3. p17 **heatmap-or-contour** conf=high panels=2
   bbox [153.85, 142.73, 297.85, 250.73] (?)
   cap: Figure 3: Prioritized search area for a hypothetical serial criminal travelling east over time, as given by the exponential decay and temporal exponential decay mod- els.
   note: (a) an ellipse smeared symmetrically about the eastward path, (b) the same path with the density shifted to its eastern end by the temporal weight
4. p18 **bar** conf=high panels=1
   bbox [130.51, 137.76, 476.11, 396.96] (?)
   cap: Figure 4: Comparison of the relative performance of each of our models on all of our data sets.
   note: twelve horizontal bars on a 0..0.5 Hit Score axis with red confidence whiskers; Uniform Random is full length, all real methods sit near 0.10
5. p19 **line** conf=high panels=1
   bbox [130.51, 230.54, 476.11, 489.74] (?)
   cap: Figure 5: Hit score by number of crimes observed using a exponential decay model and 50% confidence intervals.
   note: one blue polyline with filled markers and vertical 50% confidence bars over 3..13 crimes; the bars are wider than the trend, which is the point
6. p21 **heatmap-or-contour** conf=high panels=5
   bbox [148.2, 177.67, 292.2, 285.67] (?)
   cap: Figure 6: Prioritized search areas resulting from using different weights in the aggregation model of a circle center and exponential decay for the Beltway Sniper.
   note: five panels (a)-(e) stepping the exponential-decay weight 0.00 to 1.00 against the circle-center weight 1.00 to 0.00; each keeps its own colour bar and the 48 km bar, the hot area slides between the two methods' cores
7. p23 **map-or-plan-view** conf=high panels=2
   bbox [153.85, 236.46, 297.85, 344.46] (?)
   cap: Figure 7: Standard deviation rectangles and ellipses for the murders committed by Peter Sutcliffe.
   note: the same eleven murder points on a lat/long window with a 20 km bar, once inside standard-deviation rectangles and once inside the ellipses; no colour bar, the shapes carry the message
8. p24 **composite-panel** conf=high panels=2
   bbox [209.13, 144.81, 401.13, 336.81] (?)
   cap: Figure 8: Comparison of the prioritized search area produced by the temporal exponential decay model to the map of the geographical area of murders committed by Peter Sutcliffe. This prioritized search area suggests that the Bradford area is at the highest risk of attack.
   note: (a) is a Google Static Maps base map with the murder points, (b) the probability surface on the same window; the caption then reads the result out loud, naming Bradford as the highest-risk area

## tables
1. p9 table-grid bbox [136.61, 189.16, 470.01, 612.81]
   cap: Table 1: Description of data sets with accuracy score for temporal exponential decay model.
2. p20 table-grid bbox [126.43, 137.75, 480.18, 300.74]
   cap: Table 2: Models with associated hit scores and 95% confidence intervals.

## excluded
- p16 fragment-of-other bbox [313.74, 142.73, 457.74, 250.73] right panel (b) of Figure 2
- p17 fragment-of-other bbox [308.76, 142.73, 452.76, 250.73] right panel (b) of Figure 3
- p21 fragment-of-other bbox [318.05, 177.67, 462.05, 285.67] panel (b) of the Figure 6 weight sweep
- p21 fragment-of-other bbox [148.2, 322.88, 292.2, 430.88] panel (c) of the Figure 6 weight sweep
- p21 fragment-of-other bbox [318.05, 322.88, 462.05, 430.88] panel (d) of the Figure 6 weight sweep
- p21 fragment-of-other bbox [231.31, 468.09, 375.31, 576.09] panel (e) of the Figure 6 weight sweep
- p23 fragment-of-other bbox [308.76, 236.46, 452.76, 344.46] right panel (b) of Figure 7, the ellipse overlay
- p24 fragment-of-other bbox [171.76, 374.52, 459.76, 590.52] right panel (b) of Figure 8, the probability surface

## distillation fields

figure 1 p11: sec=3 Constructing a Model > 3.3 Model Performance Metric [model] zone=middle order=2/1 area=0.076 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=10 lead=1 count=1 read=0 gap=1 pattern=direct style=['Figure 1']
  caption: Figure N: words=28 sent=2 units=False vars=2 cond=False concl=False voice=none pos=below

figure 2 p16: sec=4 Individual Models > 4.2 Spatiotemporal Models [model] zone=top order=3/1 area=0.032 solo=False
  family=heatmap-or-contour panels=2 layout=1x2 shared=True legend=none cbar=True 3d=no printed=True
  mention: first=15 lead=1 count=1 read=1 gap=1 pattern=direct style=['Figure 2']
  caption: Figure N: words=27 sent=1 units=False vars=0 cond=True concl=False voice=passive pos=below

figure 3 p17: sec=4 Individual Models > 4.2 Spatiotemporal Models [model] zone=top order=5/1 area=0.032 solo=False
  family=heatmap-or-contour panels=2 layout=1x2 shared=True legend=none cbar=True 3d=no printed=True
  mention: first=16 lead=1 count=1 read=1 gap=1 pattern=direct style=['Figure 3']
  caption: Figure N: words=26 sent=1 units=False vars=0 cond=True concl=False voice=passive pos=below

figure 4 p18: sec=4 Individual Models > 4.3 Individual Model Results [model] zone=top order=7/1 area=0.185 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=1 gap=0 pattern=direct style=['Figure 4']
  caption: Figure N: words=18 sent=1 units=False vars=0 cond=False concl=False voice=passive pos=below

figure 5 p19: sec=5 Aggregation Models [model] zone=middle order=8/1 area=0.185 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=1 read=1 gap=0 pattern=as-shown-in style=['Figure 5']
  caption: Figure N: words=18 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 6 p21: sec=5 Aggregation Models [model] zone=top order=10/1 area=0.032 solo=False
  family=heatmap-or-contour panels=5 layout=3x2 shared=True legend=none cbar=True 3d=no printed=True
  mention: first=20 lead=1 count=1 read=1 gap=3 pattern=direct style=['Figure 6']
  caption: Figure N: words=25 sent=1 units=False vars=0 cond=True concl=False voice=passive pos=below

figure 7 p23: sec=7 Conclusions [evaluation] zone=middle order=15/1 area=0.032 solo=False
  family=map-or-plan-view panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=14 lead=9 count=2 read=1 gap=1 pattern=direct style=['Figure 7']
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p24: sec=7 Conclusions [evaluation] zone=top order=17/1 area=0.076 solo=False
  family=composite-panel panels=2 layout=1x2 shared=False legend=none cbar=True 3d=no printed=True
  mention: first=23 lead=1 count=2 read=1 gap=2 pattern=direct style=['Figure 8(a)', 'Figure 8']
  caption: Figure N: words=44 sent=2 units=False vars=0 cond=True concl=True voice=passive pos=below

table 1 p9: sec=2 Problem Background > 2.3 Collection of Data [introduction] zone=middle order=1/1 area=0.291 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=9 lead=0 count=2 read=1 gap=0 pattern=direct style=['Table 1']
  caption: Table N: words=14 sent=1 units=False vars=0 cond=True concl=False voice=none pos=above
  table: 10x3 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=column orient=portrait cont=False

table 2 p20: sec=5 Aggregation Models [model] zone=top order=9/1 area=0.119 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=18 lead=2 count=1 read=1 gap=2 pattern=direct style=['Table 2']
  caption: Table N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 12x3 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=column orient=portrait cont=False

