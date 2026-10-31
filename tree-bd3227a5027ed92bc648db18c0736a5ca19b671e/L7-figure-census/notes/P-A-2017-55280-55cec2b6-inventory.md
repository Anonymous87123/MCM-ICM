# P-A-2017-55280-55cec2b6 — figure census

- layout sha `0f050252008ee695`, 26 pages, 16 measured regions
- accounted: 11 figures, 1 tables, 4 excluded, 0 unaccounted
- families: flowchart-or-schematic 2, line 5, map-or-plan-view 1, photo-or-raster-image 1, scatter 1, surface-or-3D 1, table-grid 1

1. p4 **photo-or-raster-image** conf=high panels=1
   bbox [128.65, 210.23, 466.64, 404.43] (?)
   cap: Figure 1: Kariba Dam
   note: A single colour aerial photograph of the Kariba arch wall from downstream: the curved concrete face fills the lower two thirds, the reservoir and the spillway gate house sit at the left abutment, bare rock at the right. No frame, no axes, no legend, no scale bar, no north arrow, no numeric annotation of any kind. The caption is centred below the photo and fully inside the proxy. A low-resolution raster - foliage and gate structures are soft - but it carries no embedded text, so nothing is illegible. Never pointed at by the body: the section discusses the dam in prose and never names the figure.
2. p7 **surface-or-3D** conf=high panels=1
   bbox [86.4, 86.4, 508.88, 298.59] (?)
   cap: Figure 2: A Simulation of a dam with 3ds MAX
   note: A 3ds Max CAD render of the dam in oblique 3-D: a grey terrain shell cut away to show the reservoir volume and the dam wall, with the modelling grid visible as grey lines on every face. It is the paper's only true 3-D graphic - no axes, no tick labels, no legend, no colourbar. Three dimension letters are set inside the art: "d" at the upper right for the reservoir width, "h" at the lower centre for the dam height, and a dashed box for the capacity whose label "V" is too faint to read. The symbol key that explains V and Ai is a bulleted paragraph after the caption, outside the measured region, so the region carries a caption that promises definitions it does not contain.
3. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [86.4, 506.28, 508.89, 731.98] (?)
   cap: Figure 3: Overview of Integrated Model of Dams in Series
   note: A left-to-right architecture diagram, vector-crisp: a tall "Input data" box on the left feeds two grouped boxes, and everything converges on a tall "Integrated Model of Dams in Series" box at the right. Two containers organise the middle: an untitled dashed rounded box around "Risk Loss" and "Fundamental Investment", and a grey-shaded dashed box titled "Single Dam Evaluation" holding "Risk Cost Model" and "Power Supply Ability Model", with "Series Safety Model" standing outside both. The one legend entry is an arrow swatch labelled "data flow" at the lower left. No axes, no numbers, no colourbar. The connector from "Input data" into the lower branch leaves the trunk at a bare T-junction with no node dot, so the split point is ambiguous, and only one of the two containers is titled. Caption below the diagram.
4. p10 **line** conf=high panels=1
   bbox [86.4, 86.4, 508.87, 256.34] (?)
   cap: Figure 4: Given the same Xi , the function of Pf and Risk Value with different α
   note: Eleven smooth curves of Risk Cost against acceptable risk ratio Pf, one per value of alpha from 0.50 to 1.00 in steps of 0.05, in the default MATLAB colour cycle. Axes "Pf (Acceptable Risk Ratio)" 0-0.1 ticked every 0.01 and "Risk Cost / Billion" 0.5-4 ticked every 0.5, four-sided frame, no gridlines. The legend is a boxed in-axes key at the upper right with 11 entries, and a vertical double arrow outside the right spine is annotated "alpha increasing". No numeric data labels and no colourbar. Curves are so dense near Pf = 0 that the first few merge below 0.005, and adjacent pairs (0.60/0.65, 0.70/0.75) are nearly the same colour. The caption calls the ordinate "Risk Value" while the axis prints "Risk Cost / Billion", and no currency is given.
5. p13 **scatter** conf=high panels=1
   bbox [86.4, 429.1, 508.88, 654.27] (?)
   cap: Figure 5: The red curve represents the river’s elevation. X-Axis is the distance from the river’s source while Y-Axis is altitude.
   note: The elevation profile of the Zambezi as a blue scatter of several thousand samples with a red fitted curve drawn through it, one panel, both series in the same axes. Axes "x" 0-25000 (no unit) and "Altitude" -200 to 1200 (no unit), light grey gridlines in both directions, boxed frame. Legend inside the upper right with 2 entries ("Altitude vs. x" and "fit function"). No numeric data labels, no colourbar. The scatter stops near x = 22500 while the axis runs to 25000 and the fitted curve detaches from the points at both tails, so the fit is extrapolated; where the profile is a plateau around x = 8500-10500 the blue markers merge into a band and single points cannot be read.
6. p14 **map-or-plan-view** conf=high panels=2
   bbox [86.4, 141.67, 297.63, 236.2] (?)
   cap: Figure 6: Zambezi River’s mean annual river flow. The violet, pink, and yellow bands represents the upstream, midstream, and downstream, respectively. Width of each band measures the value of mean annual river flow.
   note: A two-panel composite under one figure number: panel (a) on the left is a 2-D map of southern Africa with the Zambezi drawn as three colour-coded segments and a red "Kariba Dam" callout arrow, labelled with Kitwe, Lusaka, Bulawayo, Harare, Lilongwe, Beira and the country names; panel (b) on the right is a 3-D line plot of the same course in x/y/elevation with the path colour-graded blue to magenta to yellow, axes "x /km" 0-140, "y /km" 20-100 and "Z/m" 0-1000. Each panel carries its own subcaption - (a) "2D version. It includes surrounding coun-tries and cities." and (b) "3D version. It includes the river's elevation changes." - and the single "Figure 6:" caption sits below both. No legend in either panel: the three river colours are never keyed, so only the figure caption's prose says violet/pink/yellow mean upstream/midstream/downstream. No scale bar, no north arrow, no graticule. This row is detector region 2, the (a) panel; region 1 is the (b) panel and is excluded as its fragment, because the layout pass cuts the composite at x = 297.
7. p15 **line** conf=high panels=1
   bbox [86.4, 86.4, 508.87, 290.38] (?)
   cap: Figure 7: Best placement of new dams with different quantity of dams in Figure.4
   note: Eleven overlaid bands of bed altitude against distance, one per dam count n = 10 to 20, with marker overlays for the chosen dam positions (stars at n = 13). Axes "altitude/m" 0-1500 and "x/km" 0-2250, ticks every 500. The legend is a block of 22 entries ABOVE the plot in three rows - 11 filled swatches plus 11 marker glyphs under the same n labels - so every series appears twice and the key is taller than the plot it explains. No numeric data labels, no colourbar, no gridlines. Bands overlap so heavily that individual n values cannot be discriminated, and the two axis labels disagree on units ("altitude/m" against "x/km").
8. p16 **line** conf=high panels=1
   bbox [86.4, 86.4, 508.89, 403.27] (?)
   cap: Figure 8: Trend of Final Value with n increasing lower.
   note: Three evaluation curves against the number of dams n from 10 to 20: "Risk Cost", "Power Supply" and the blend "0.5Cost+0.5Supply". Axes "Evaluation" 0.30-0.75 ticked every 0.05 and "n" integer ticked, boxed frame, no gridlines. Legend boxed inside the upper right, 3 entries. Two pink dot markers single out n = 13 on the blue and the yellow curve - the orange curve gets no marker - and an in-plot white text box reads "n=13 is the best solution", overlapping the blue curve. No numeric data labels and no colourbar. The caption is split across two printed lines and the second one is a single word, "lower.", left over from the sentence; the region cuts it off.
9. p17 **flowchart-or-schematic** conf=high panels=1
   bbox [86.4, 86.4, 508.87, 257.38] (?)
   cap: Figure 9: Placement of 13(optimal quantity) dams along the Zambezi River. Each dam is labelled with its height. The blue areas are each dam’s corresponding reservoirs.
   note: A longitudinal-profile schematic: the river bed drawn as a black curve from left to right with two vertical drops, 13 blue trapezoids sitting in it as dams, and sky-blue wedges behind each trapezoid for the impounded reservoir. Every dam is labelled with its height (27.7m, 29.2m, 30.3m, 32.1m, 38.2m, 40m, 42m, 37.9m, 27.6m, 26.1m, 25.8m, 25.4m, 24.6m) and beneath each a coordinate pair ((228,1160) through (2098,195)) that repeats Table 3 on p15 with the decimals dropped. It is the only figure in the paper that prints its data values as labels. Neither axis is titled, ticked, or given a unit - the x coordinate is a distance and the y coordinate an elevation, but the reader has to infer both from the numbers - and the first five coordinate pairs collide with the trapezoids. No legend, no colourbar, L-shaped frame.
10. p20 **line** conf=high panels=1
   bbox [86.4, 278.19, 508.88, 503.37] (?)
   cap: Figure 10: Given the same Xi , the function of Pf and Risk Value with different N
   note: Six curves of Risk Cost against Pf, one per planned working life N = 50, 60, 70, 80, 90, 100. Axes "Pf (Acceptable Risk Ratio)" 0-0.1 ticked every 0.01 and "Risk Cost / billion" 0-3 ticked every 0.5, four-sided frame, no gridlines. Legend boxed inside the upper right, 6 entries listed in descending curve order. No numeric data labels, no colourbar. All six curves dip near Pf = 0.004 and then rise monotonically and converge at about 2.65, so the ordinate is not monotone and the parameter only shifts the height. The y title wraps its unit onto a second line.
11. p22 **line** conf=high panels=1
   bbox [192.02, 326.16, 403.26, 444.78] (?)
   cap: Figure 11: A Dam’s Failure Rate
   note: A single pale-blue curve of failure rate against year, flat at about 0.028 to year 50 and then rising exponentially to about 0.13 at year 60 - the plot form of the piecewise failure function printed above it. Axes "year" 0-60 ticked every 10 and "rate of failure" 0-0.14 ticked every 0.02, L-shaped axes only (no top or right spine, unlike Figures 4, 5, 8 and 10), light grey gridlines both ways. No legend, no numeric data labels, no colourbar. The plot is inset with wide white margins and its fonts are markedly smaller than the fonts of Figure 10, consistent with a scaled-in screenshot. The region top edge clips the tail of the display equation, so fragments of its bracket sit just above the plot.

## tables
1. p6 table-grid bbox [140.31, 110.11, 454.97, 327.7]
   cap: Table 1: Nomenclature

## excluded
- p14 fragment-of-other bbox [297.64, 86.4, 508.88, 236.2] the (b) panel of Figure 6 - the 3-D x/y/elevation plot of the Zambezi course - cut from its (a) partner by the layout pass at x = 297; its left edge still carries a sliver of the (a) map and its subcaption runs into the (a) subcaption on the same print line. Counted once, as region 2 of page 14.
- p25 not-an-exhibit bbox [86.4, 61.69, 508.88, 159.9] Appendix A "Implemented Genetic Algorithm": page running head, the appendix heading and the first two lines of MATLAB listings. No frame, no box, no line-number gutter and no shading - the only drawing primitives are the full-measure rules under the running head and under the appendix heading, which the detector reads as a banded box.
- p25 not-an-exhibit bbox [86.4, 341.62, 508.88, 404.9] the tail of Appendix A and the head of Appendix B "Fitness Function", again bounded only by the two full-measure section rules. Neither listing is an exhibit and the paper gives them no caption or number.
- p26 not-an-exhibit bbox [86.4, 61.69, 508.88, 158.63] the remaining body of the Appendix B fitness function at the top of the last page, closed by the page-separator rule. Same listing, no frame, no caption; the code continues from region 2 of page 25.

## distillation fields

figure 1 p4: sec=1 Introduction > 1.1 Problem Background [introduction] zone=middle order=1/1 area=0.131 solo=False
  family=photo-or-raster-image panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p7: sec=4 Statement of our Model > 4.2 Analysis of A Single Dam [result] zone=top order=3/1 area=0.179 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=6 lead=1 count=2 read=2 gap=None pattern=direct style=['Figure 2']
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p8: sec=4 Statement of our Model > 4.3.1 Prerequisites [other] zone=bottom order=4/1 area=0.19 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=8 lead=0 count=2 read=2 gap=None pattern=direct style=['Figure 3']
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p10: sec=4 Statement of our Model > 4.3.3 Series Safety Model [model] zone=top order=5/1 area=0.143 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=9 lead=1 count=2 read=2 gap=None pattern=direct style=['Figure 4']
  caption: Figure N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p13: sec=5 Implementation > 5.1 Data [other] zone=middle order=6/1 area=0.19 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 5']
  caption: Figure N: words=23 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p14: sec=5 Implementation > 5.1 Data [other] zone=top order=7/1 area=0.04 solo=False
  family=map-or-plan-view panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=1 count=1 read=1 gap=None pattern=direct style=['Fig- ure.6(a)', 'Figure.6(b)']
  caption: Figure N: words=34 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p15: sec=5 Implementation > 5.2 Number and placement of the new dams > 5.2.2 Determining the number and placement by genetic algorithm [solution] zone=top order=8/1 area=0.172 solo=False
  family=line panels=1 layout=1 shared=False legend=above cbar=False 3d=no printed=False
  mention: first=15 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 7']
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p16: sec=5 Implementation > 5.2 Number and placement of the new dams > 5.2.3 Determining the height of each dam [other] zone=top order=9/1 area=0.267 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=15 lead=1 count=1 read=1 gap=None pattern=direct style=['Figure 8']
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p17: sec=6 Strategies > 6.1 A Balance Between Safety and Costs [other] zone=top order=10/1 area=0.144 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=17 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 9']
  caption: Figure N: words=27 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p20: sec=7 Model Analysis > 7.1 Sensitivity Analysis > 7.1.1 Impact of Planned Working Years N for a Dam [sensitivity] zone=middle order=11/1 area=0.19 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=20 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 10']
  caption: Figure N: words=16 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p22: sec=8 Conclusion [evaluation] zone=middle order=12/1 area=0.05 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=22 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 11']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p6: sec=3 Nomenclature [symbols] zone=top order=2/1 area=0.137 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=5 lead=1 count=1 read=1 gap=None pattern=direct style=['Table 1']
  caption: Table N: words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 15x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

