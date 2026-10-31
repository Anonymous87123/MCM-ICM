# P-C-2022-2229059-dacff43d — figure census

- layout sha `728ee6e422a77968`, 24 pages, 13 measured regions
- accounted: 9 figures, 0 tables, 4 excluded, 0 unaccounted
- families: bar 1, flowchart-or-schematic 1, line 7

1. p7 **line** conf=high panels=2
   bbox [86.4, 128.2, 297.64, 292.27] (?)
   cap: Figure 1: Plots of bitcoin and gold
   note: Recorded bbox is the left panel region only; the right panel is measured region p7 r2 and is excluded as a fragment of the same plate. The group caption prints at y321, between the panel row (y128-292) and Figure 2's region (y354), so position is below. Only the p7 spelling can be held in style (the checker looks at the exhibit's page and neighbours); the four later citations use the sub-panel letters in lower case - 'comparing figure 1a and 1b' on p12, 'Compare figure 1a' on p12, '(compare figure 1a)' on p16 and 'Compare to figure 1a' on p16 - and the paper never writes a bare 'figure 1'.
2. p7 **line** conf=high panels=1
   bbox [127.56, 354.38, 467.72, 615.68] (?)
   cap: Figure 2: Bitcoin Price from 9/11/2016 to 9/10/2021
   note: Caption states the data window as its only content, which is what conditions marks here.
3. p9 **flowchart-or-schematic** conf=high panels=1
   bbox [127.56, 86.4, 467.74, 243.46] (?)
   cap: Figure 3: Flow Chart Describing our buy logic.
   note: Announced on p8, one page before it prints. The paragraph including the announcing line has the heading '3.3 Calculating Profitability' welded onto the same print line, so the lead quote begins at the sentence.
4. p12 **line** conf=high panels=1
   bbox [86.4, 158.1, 511.6, 394.06] (?)
   cap: Figure 4: Our results.
   note: The paper's summary result plate. Nothing on the plate is annotated; every figure the prose quotes ($220,486 total, 21,948% return, 194% annualised) is printed in the text, not on the artwork.
5. p13 **bar** conf=medium panels=1
   bbox [170.08, 124.3, 425.2, 342.07] (?)
   cap: Figure 5: The weight factor normalizing the magnitude of the signals.
   note: Family is bar, not line, because the marks are vertical bars off a baseline over most of the width; the single blue polyline is an unlabelled overlay. Caption names two plotted quantities ('weight factor', 'signals'), which is what variable_count counts.
6. p13 **line** conf=high panels=1
   bbox [170.08, 569.91, 425.19, 730.8] (?)
   cap: Figure 6: Results under different combinations.
   note: Caption is word-for-word identical to Figure 7's ('Results under different combinations.'), so the two plates are told apart only by their page and their number. Cited first on p14, one page after it prints, so lead_pages is negative. The third citation sits on p18, six pages later, outside the quote window: 'Despite this, figure 6 shows that for small variations in parameters the fall-off is not massive.' The recorded trail is the p14 reading sentence that follows the plate on its own page.
7. p15 **line** conf=high panels=1
   bbox [127.56, 159.07, 467.72, 352.05] (?)
   cap: Figure 7: Results under different combinations.
   note: Caption duplicates Figure 6's exactly. The prose points at the plate only after the grid below it, in the phrase 'the disparity seen in figure 7 and accompanying chart', so the grid is cited as part of the figure.
8. p16 **line** conf=high panels=1
   bbox [155.91, 195.19, 439.39, 407.8] (?)
   cap: Figure 8: Buy (RED) and Sell (BLUE) orders for bitcoin between 1610 and 1760 days.
   note: Legend 'none' is a real finding, not a miss: colour is carried by the caption and by one body sentence instead of a key.
9. p17 **line** conf=high panels=1
   bbox [155.91, 86.4, 439.39, 299.01] (?)
   cap: Figure 9: Buy (RED) and Sell (BLUE) orders for gold between 460 and 560 days.
   note: Announced at the foot of p16 and printed at the top of p17, so lead_pages is 1. The caption/body/axis disagreement on the window is declared in other_note rather than repaired.

## excluded
- p7 fragment-of-other bbox [297.64, 131.05, 508.87, 289.41] Right panel of Figure 1's plate (gold price curve, 298-509 x 131-289); the left panel is the recorded region for the row.
- p20 not-an-exhibit bbox [86.6, 110.96, 508.68, 744.48] Memorandum body: a single justified prose column under the DATE/TO/FROM/SUBJECT block. No rules, no columns, no artwork - the measurer boxed the text column because of its straight edges.
- p21 not-an-exhibit bbox [86.4, 86.4, 508.88, 401.07] Continuation of the memorandum prose ending in 'Thank you for supporting this endeavor.' and a 'Sincerely, Modeling Team' signature block inside a ruled outline. Page furniture, not an exhibit.
- p24 not-an-exhibit bbox [86.4, 64.18, 508.88, 164.91] Appendix pseudocode listing ('if extreme market conditions are active:' and indented sub-steps) in a monospaced box inside a ruled border. A code block, not a figure or a grid.

## distillation fields

figure 1 p7: sec=2 Analysis of the Problem [model] zone=top order=1/1 area=0.069 solo=False
  family=line panels=2 layout=1x2 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=7 lead=0 count=5 read=1 gap=None pattern=figure-n-shows style=['Figures 1a and 1b']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p7: sec=2 Analysis of the Problem [model] zone=middle order=2/2 area=0.177 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=7 lead=0 count=2 read=1 gap=None pattern=figure-n-shows style=['figure 2']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 3 p9: sec=3 Calculating and Simplifying the Model > 3.3 Calculating Profitability [model] zone=top order=3/1 area=0.107 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=1 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 3']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p12: sec=4 The Model Results > 4.1 General Result [result] zone=top order=4/1 area=0.2 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=12 lead=0 count=2 read=1 gap=None pattern=figure-n-shows style=['figure 4']
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p13: sec=4 The Model Results > 4.2 Weight Factor [result] zone=top order=5/1 area=0.111 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 5']
  caption: Figure N: words=11 sent=1 units=False vars=2 cond=False concl=False voice=none pos=below

figure 6 p13: sec=4 The Model Results > 4.3 Parameter Optimization [sensitivity] zone=bottom order=6/2 area=0.082 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=14 lead=-1 count=3 read=1 gap=None pattern=figure-n-shows style=['figure 6']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p15: sec=4 The Model Results > 4.4 Changes in Transaction Fees [sensitivity] zone=top order=7/1 area=0.131 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=15 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['figure 7']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p16: sec=5 Validating the Model > 5.1 Bitcoin Buy/Sell [test] zone=middle order=8/1 area=0.12 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=16 lead=0 count=3 read=1 gap=None pattern=figure-n-shows style=['figure 8']
  caption: Figure N: words=15 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 9 p17: sec=5 Validating the Model > 5.2 Gold Buy/Sell [test] zone=top order=9/1 area=0.12 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=16 lead=1 count=2 read=1 gap=None pattern=figure-n-shows style=['Figure 9']
  caption: Figure N: words=15 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

