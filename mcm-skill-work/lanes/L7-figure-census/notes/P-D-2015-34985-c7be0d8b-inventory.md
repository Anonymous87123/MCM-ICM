# P-D-2015-34985-c7be0d8b — figure census

- layout sha `6ad43d213b7e0625`, 20 pages, 14 measured regions
- accounted: 11 figures, 3 tables, 0 excluded, 0 unaccounted
- families: bar 1, composite-panel 2, heatmap-or-contour 2, line 2, map-or-plan-view 2, node-link-network 2, table-grid 3

1. p1 **node-link-network** conf=high panels=1
   bbox [170.57, 615.7, 422.68, 781.78] (raster)
   cap: 
   note: The cost-to-index function map, drawn as a bitmap: the boxed word COST at the foot of the picture, thirty arrows rising out of it through the factor boxes (Education, Health Care Expenditures, Doctors, Life Expectancy, HIV, Contraceptives, Jobs, Advertisements, Tourism, Agriculture, Availability, Wealth, Mining, Copper, Cobalt, Coal, Pollution, Non Renewable, Solar, Hydropower, Dams, Renewable, Resource Consumption) into the two sink boxes 'Socioeconomic Development Index' and 'Ecological Impact Index'. Blue arrows feed the socioeconomic index, orange the ecological one, and nothing on the sheet keys the two colours. No caption, no number, no axes, no values. This is the same map Figure 6 prints on p13, repeated on the summary sheet unnumbered and uncited - the paper never cross-references back to it.
2. p6 **map-or-plan-view** conf=high panels=1
   bbox [111.6, 91.59, 500.4, 335.53] (raster)
   cap: Figure 1: Worldwide view of country Ecological Impact Index (Di ) values
   note: A world choropleth in one raster: country shapes filled from a five-step orange-yellow-red ramp, no borders, no graticule, no projection note. The key sits INSIDE the picture at the lower left, printed 'Ecological Index' over a stepped colour bar lettered 'Low' and 'High' at its ends, so the classes carry no numbers and a reader cannot recover the index value at all. Countries with no data are left white (Europe, Russia, most of the Sahel) while the prose says they are coloured grey, and Greenland and Antarctica are solid grey. The caption is the only text the layer prints with its spaces intact; its subscript i arrives on its own line.
3. p7 **line** conf=high panels=1
   bbox [133.2, 352.66, 478.82, 530.65] (raster)
   cap: Figure 2: Graph of the theoretical income distribution I(x) and adjusted income distribution A(x)
   note: Two smooth curves, not a scatter: the red 'Theoretical Income Distribution I(x)' rising from the origin to about 0.92 at x = 0.9, and the blue 'Adjusted Income Distribution (1-x)I(x)' arching to a peak near x = 0.55 and falling back, with the red curve above the blue one everywhere but at the two ends. Each curve is named in a boxed annotation with a leader line inside the plot, so the legend is inside and carries no colour chrome. The x axis is lettered 0 to 0.9 but the ticks are printed as 0.1, 0.2 and so on with no axis title; there is NO y axis at all - no ticks, no title, no scale. The caption reaches the layer with every space dropped ('Figure2: Graphofthetheoreticalincomedistribution') and wraps its last token, 'A(x)', onto a second line, so the verbatim here is typed from the crop.
4. p8 **map-or-plan-view** conf=high panels=1
   bbox [111.6, 171.82, 500.41, 418.44] (raster)
   cap: Figure 3: Worldwide view of country Development Index (Di ) values
   note: The same world choropleth machinery as Figure 1 with a different variable: the same five-step ramp now keyed inside the lower left as 'Development Index' between 'Low' and 'High'. The geographic reading is the inverse of Figure 1 by construction - the underdeveloped Sahel and central Africa sit at the red end here and the yellow end there - which is the paper's own point. No graticule, no numbers on the key, no data-label, and the no-data countries are white here too against the prose's 'coloured grey'.
5. p9 **composite-panel** conf=high panels=2
   bbox [90.0, 133.23, 522.02, 356.55] (raster)
   cap: Figure 4: Tradeoff dynamics. A: Socioeconomic Development Index (Di vs. Ecological Impact Index Ei for any given country iB: Mean Index levels for underdeveloped vs. other nations.
   note: Two panels in one raster, marked 'A.' and 'B.' at their upper left. Panel A is a diamond scatter of the Socioeconomic Development Index (x, 0 to 1) against the Ecological Impact Index (y, 0 to 1) for about ninety countries, falling from 0.85 at x = 0.05 to 0.25 at x = 0.95, with its legend INSIDE at the lower left on a grey plate: orange 'Other Nation', blue 'Underdeveloped Nation'. Panel B is four vertical bars in two groups - Economic and Ecological - blue and orange, 32 against 70 and 77 against 49, on a y axis 0 to 100 with NO legend, so the panel's colour code is only recoverable from panel A's legend. The caption welds both panels' descriptions into one run-on line with no space between 'i' and 'B:' and never ends the A-sentence.
6. p12 **heatmap-or-contour** conf=high panels=6
   bbox [109.78, 92.13, 304.18, 323.91] (raster)
   cap: Figure 5: Comparison of two seeds: random and biased wealth distribution with even initial population distribution. For the red-blue gradients on the wealth and population automata, red indicates higher values of wealth and population while blue indicates lower values.
   note: One of the two measured halves of Figure 5, printed as its own pasted bitmap. The drawing is a three-row by two-column block of cellular-automata snapshots: 'Wealth Distribution' down the left column and 'Population Distribution' down the right, the rows lettered 'Initial', '10 Years' and '20 Years' on a vertical arrow between the columns. Cells are red for high and blue for low, with white where the cell is empty, and the class breaks are not printed anywhere. The 10-year and 20-year rows are smooth because the automaton diffuses; the initial row is fine-grained noise. No axes, no scale, no legend inside - the red-blue key exists only in the caption sentence. The half is labelled below its picture, not by the caption: '(a) Random initial wealth distribution.' on the left half and '(b) Trended initial wealth distribution.' on the right, and the main caption is set once under both. This is the (a) random half; the pair is recorded as two rows because the region pass measures each half separately and no region spans both.
7. p12 **heatmap-or-contour** conf=high panels=6
   bbox [307.82, 91.59, 502.22, 323.91] (raster)
   cap: Figure 5: Comparison of two seeds: random and biased wealth distribution with even initial population distribution. For the red-blue gradients on the wealth and population automata, red indicates higher values of wealth and population while blue indicates lower values.
   note: One of the two measured halves of Figure 5, printed as its own pasted bitmap. The drawing is a three-row by two-column block of cellular-automata snapshots: 'Wealth Distribution' down the left column and 'Population Distribution' down the right, the rows lettered 'Initial', '10 Years' and '20 Years' on a vertical arrow between the columns. Cells are red for high and blue for low, with white where the cell is empty, and the class breaks are not printed anywhere. The 10-year and 20-year rows are smooth because the automaton diffuses; the initial row is fine-grained noise. No axes, no scale, no legend inside - the red-blue key exists only in the caption sentence. The half is labelled below its picture, not by the caption: '(a) Random initial wealth distribution.' on the left half and '(b) Trended initial wealth distribution.' on the right, and the main caption is set once under both. This is the (b) half: its own subcaption prints 'Trended initial wealth distribution.' while the shared caption above calls the same seed 'biased', so the pair names one seed two ways. The trended seed starts its wealth in the lower-right corner, as the prose says, and its population begins empty outside that corner.
8. p13 **node-link-network** conf=high panels=1
   bbox [90.0, 91.59, 522.01, 376.8] (raster)
   cap: Figure 6: Di and Ei with regards to features of Zambia, in terms of cost.
   note: The Zambia function map, drawn as a pasted bitmap: the boxed word COST at the foot, twenty-five factor boxes above it joined by arrows into the two index sinks, exactly the topology of the unnumbered map on the summary sheet but with Zambia-specific factors added (Copper, Cobalt, Mining, Agriculture, Tourism, Solar, Dams, Hydropower). The two arrow colours still carry the socioeconomic and ecological split and still have no key. Despite 'in terms of cost' in the caption there is no axis, no scale and not one number on the picture, so cost is shown only as the direction of an arrow. The caption is set INSIDE a sentence: p12 ends 'we created a map of the main factors that influence the Socioeconomic' and the page resumes under the caption with 'and Ecological Indices of Zambia.', so the region also splits a paragraph.
9. p15 **line** conf=high panels=1
   bbox [90.0, 226.02, 522.01, 474.58] (raster)
   cap: Figure 7: Effect of alpha on resulting sustainability. The black line represents an example budget/investment of 1.2 billion dollars.
   note: Three curves with round markers over a near-vertical knee: sustainability against 'ICM Financial Investment' (x, printed 0 to 2E+09 with mixed notation - plain integers for the first two ticks, scientific for the rest) and 'Resulting Sustainability' (y, 0.315 to 0.35). The legend is INSIDE at the lower right, boxed, lettered in the Greek alpha ('a = 0.5', 'a = 1.0', 'a = 1.5') which the caption renders as the word 'alpha'. One vertical reference line marks 1.2 billion, the example budget the prose points at. Units are absent from both axes although the x quantity is dollars; the top of the y window is chosen so that all three alphas crowd into the last two ticks.
10. p16 **bar** conf=high panels=1
   bbox [133.2, 91.59, 478.8, 249.42] (raster)
   cap: Figure 8: Amount of money that should be invested based on the α level. Solid represents the first 10 years of the plan and striped represents the second 10 years. These numbers are based on a 1.2 billion dollar budget.
   note: Seven groups of paired vertical bars - Contraceptives, Health, Education, Agriculture, Mining, Tourism, Solar - against 'Financial Investment' on y (0 to 500000000, no unit printed) and no x axis title. The six-entry legend is INSIDE at the upper right and prints each alpha twice ('0.5', '0.5', '1', '1', '1.5', '1.5'), leaving solid against hatched as the only cue for first decade against second, which the caption alone explains. The hatched sample for 0.5 is drawn blue while the hatched bars it keys are pink, the top y tick collides with the plot border and reads as a run-on '500000000 0', and the last three groups are near zero and unreadable. Figure 7's legend prefixes the same alphas with the Greek letter; this one drops it.
11. p16 **composite-panel** conf=high panels=3
   bbox [90.0, 403.44, 522.01, 545.83] (raster)
   cap: Figure 9: Di , Ei and S trends over time, respectively. Blue represents α = 0.5, red represents α = 1, and green represents α = 1.5.
   note: Three panels side by side in one raster: three lines with markers in each, x ticked 0 to 20 in every panel, and NOTHING else - no axis titles, no y tick numbers, no subpanel letters, no per-panel title, and no legend; the caption is the only place the colours are mapped to alphas. The middle panel is scaled differently from its neighbours, so the three are not visually comparable even though the caption's word 'respectively' implies they are, and with the y magnitudes unprinted the paper's own claim that E_i falls while D_i and S rise cannot be read off the picture.

## tables
1. p5 table-grid bbox [139.36, 463.15, 472.64, 559.19]
   cap: Global Warming Potentials (IPCC 2013) [6]
2. p10 table-grid bbox [142.9, 250.33, 469.1, 427.66]
   cap: Top 10 Most Sustainable Countries
3. p20 table-grid bbox [133.27, 173.49, 478.73, 517.07]
   cap: 

## distillation fields

figure 1 p1: sec=Mathematical Contest in Modeling (MCM/ICM) Summary Sheet [model] zone=bottom order=1/1 area=0.084 solo=False
  family=node-link-network panels=1 layout=1x1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=above

figure 2 p6: sec=4 Environmental Resource Management Model > 4.1 Quantifying Pollution [model] zone=top order=2/1 area=0.196 solo=False
  family=map-or-plan-view panels=1 layout=1x1 shared=False legend=inside cbar=True 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=11 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 3 p7: sec=5 Development for Better Life Quality > 5.2 Socioeconomic Development Index [model] zone=middle order=3/1 area=0.127 solo=False
  family=line panels=1 layout=1x1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p8: sec=5 Development for Better Life Quality > 5.2 Socioeconomic Development Index [model] zone=middle order=4/1 area=0.198 solo=False
  family=map-or-plan-view panels=1 layout=1x1 shared=False legend=inside cbar=True 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=10 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 5 p9: sec=6 Ecological-Economic Trade off [model] zone=top order=5/1 area=0.199 solo=False
  family=composite-panel panels=2 layout=1x2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 4']
  caption: Figure N: words=27 sent=4 units=False vars=2 cond=False concl=False voice=none pos=below

figure 6 p12: sec=7 20-year plan for Zambia > 7.1 Population Growth and Economic Development [model] zone=top order=6/2 area=0.093 solo=False
  family=heatmap-or-contour panels=6 layout=3x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=1 count=2 read=2 gap=None pattern=direct style=['Figure 5']
  caption: Figure N: words=39 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p12: sec=7 20-year plan for Zambia > 7.1 Population Growth and Economic Development [model] zone=top order=7/1 area=0.093 solo=False
  family=heatmap-or-contour panels=6 layout=3x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=1 count=2 read=2 gap=None pattern=direct style=['Figure 5']
  caption: Figure N: words=39 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p13: sec=7 20-year plan for Zambia > 7.2 Iterated Function Map [model] zone=top order=8/1 area=0.254 solo=False
  family=node-link-network panels=1 layout=1x1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=-1 count=2 read=1 gap=None pattern=direct style=['Figure 6']
  caption: Figure N: words=15 sent=1 units=False vars=2 cond=False concl=False voice=none pos=below

figure 9 p15: sec=7 20-year plan for Zambia > 7.5 Particle Swarm Optimization [model] zone=middle order=9/1 area=0.222 solo=False
  family=line panels=1 layout=1x1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=15 lead=0 count=2 read=2 gap=None pattern=direct style=['Figure 7']
  caption: Figure N: words=19 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p16: sec=7 20-year plan for Zambia > 7.5 Particle Swarm Optimization [model] zone=top order=10/1 area=0.113 solo=False
  family=bar panels=1 layout=1x1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=39 sent=3 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p16: sec=7 20-year plan for Zambia > 7.6 Evaluating the 20-year Plan [model] zone=middle order=11/2 area=0.127 solo=False
  family=composite-panel panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 9']
  caption: Figure N: words=20 sent=2 units=False vars=3 cond=False concl=False voice=none pos=below

table 1 p5: sec=4 Environmental Resource Management Model > 4.1 Quantifying Pollution [model] zone=middle order=12/1 area=0.066 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 3x4 header=2 rules=boxed zebra=False merged=True diag=False units_hdr=False dec=False num=2 txt=2 width=full orient=portrait cont=False

table 2 p10: sec=6 Ecological-Economic Trade off [model] zone=middle order=13/1 area=0.119 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=10 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['the table']
  caption: none words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 10x4 header=2 rules=boxed zebra=False merged=True diag=False units_hdr=False dec=False num=0 txt=4 width=full orient=portrait cont=False

table 3 p20: sec=A Equations for Iterated Function Map [appendix] zone=middle order=14/1 area=0.245 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 13x4 header=1 rules=boxed zebra=False merged=False diag=False units_hdr=False dec=False num=1 txt=3 width=full orient=portrait cont=False

