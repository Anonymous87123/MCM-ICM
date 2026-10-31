# P-C-2011-11422-caf513f2 — figure census

- layout sha `d9826a078e4e5668`, 20 pages, 19 measured regions
- accounted: 9 figures, 9 tables, 1 excluded, 0 unaccounted
- families: line 7, other 1, photo-or-raster-image 1, table-grid 9

1. p6 **line** conf=high panels=1
   bbox [144.97, 389.5, 466.27, 602.35] (raster)
   cap: 
   note: three coupled series over t_n; the keys E_n, G_n and C(n) sit left of the frame and the x axis is labelled t_n, no axis title on y
2. p7 **line** conf=high panels=1
   bbox [144.97, 124.8, 466.27, 337.65] (raster)
   cap: 
   note: the same three series with a larger seeding proportion: C(n) climbs past G_n before t_n = 70
3. p9 **photo-or-raster-image** conf=high panels=1
   bbox [153.18, 171.63, 458.07, 337.9] (raster)
   cap: 
   note: screenshot of the cellular-automaton grid with the viewer chrome still visible at the top; the ink is a raster image, not paths
4. p9 **line** conf=high panels=1
   bbox [133.77, 338.89, 495.77, 529.39] (raster)
   cap: Cellular Automata Model of Spreading of Electric Cars Based on Initial Seeding
   note: six series (5% to 30% seeding) rising to 2060, title and key both baked into the image raster; y axis 'Percentage of Total Cars the are Electric'
5. p10 **other** conf=high panels=1
   bbox [133.77, 531.64, 358.27, 694.64] (raster)
   cap: 
   note: five sectors (Petroleum, Natural Gas, Coal, Renewable Energy, Nuclear Energy) with the key right of the circle
6. p15 **line** conf=high panels=1
   bbox [133.77, 124.8, 452.77, 329.8] (raster)
   cap: 
   note: six colour series against the alpha value, square and diamond markers joined by thin lines, y axis 'Quadrillion BTUs'
7. p15 **line** conf=high panels=1
   bbox [133.77, 330.79, 469.77, 536.79] (raster)
   cap: 
   note: one series: total cost against the alpha value, y axis 'Cost ($)'; the curve is a flat run, one step, then a straight rise
8. p16 **line** conf=high panels=1
   bbox [133.77, 225.88, 482.97, 462.88] (raster)
   cap: 
   note: one series of cost against alpha with a red annotation arrow marking the worked example at alpha = 37500; no legend and no gridlines
9. p17 **line** conf=high panels=1
   bbox [133.77, 124.8, 513.17, 376.8] (raster)
   cap: 
   note: five series (Petroleum, Natural Gas, Coal, Renewable, Nuclear) in quadrillion BTUs against alpha, key boxed inside the bottom-right corner, dashed horizontal gridlines

## tables
1. p7 table-grid bbox [190.13, 338.85, 421.12, 435.29]
   cap: 
2. p11 table-grid bbox [145.52, 395.08, 465.73, 483.55]
   cap: 
3. p11 table-grid bbox [188.96, 534.7, 422.28, 623.16]
   cap: 
4. p13 table-grid bbox [133.77, 373.06, 511.03, 449.17]
   cap: 
5. p18 table-grid bbox [165.95, 325.24, 445.3, 422.01]
   cap: 
6. p18 table-grid bbox [165.95, 449.2, 445.3, 545.64]
   cap: 
7. p18 table-grid bbox [165.95, 572.83, 445.3, 669.26]
   cap: 
8. p19 table-grid bbox [165.95, 125.0, 445.3, 221.44]
   cap: 
9. p19 table-grid bbox [212.32, 368.73, 398.93, 441.26]
   cap: 

## excluded
- p15 fragment-of-other bbox [454.98, 242.3, 507.48, 329.8] legend box of the p15 multi-series chart; it sits beyond the right edge of the axes and the extractor measured it as its own region

## distillation fields

figure 1 p6: sec=6 Microeconomic Model > 6.1 Global Influence Model [model] zone=middle order=1/1 area=0.141 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-left cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p7: sec=6 Microeconomic Model > 6.1 Global Influence Model [model] zone=top order=2/1 area=0.141 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-left cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p9: sec=6 Microeconomic Model > 6.2 Localized Behavior > 6.2.1 Cellular automata [model] zone=top order=4/1 area=0.105 solo=False
  family=photo-or-raster-image panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p9: sec=6 Microeconomic Model > 6.2 Localized Behavior > 6.2.1 Cellular automata [model] zone=middle order=5/2 area=0.142 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p10: sec=7 Macroeconomic Model: Meeting the Energy > 7.1 Current Energy Source and Demand [other] zone=bottom order=6/1 area=0.075 solo=False
  family=other panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p15: sec=7 Macroeconomic Model: Meeting the Energy > 7.7 Using Alpha to Determine Cost, and Vice Versa [solution] zone=top order=10/1 area=0.135 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p15: sec=7 Macroeconomic Model: Meeting the Energy > 7.7 Using Alpha to Determine Cost, and Vice Versa [solution] zone=middle order=11/2 area=0.143 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p16: sec=7 Macroeconomic Model: Meeting the Energy > 7.8 Example Calculation [solution] zone=middle order=12/1 area=0.171 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p17: sec=7 Macroeconomic Model: Meeting the Energy > 7.9 Fossil Fuels Saved [result] zone=top order=13/1 area=0.197 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p7: sec=6 Microeconomic Model > 6.1 Global Influence Model [model] zone=middle order=3/2 area=0.046 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x3 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=False

table 2 p11: sec=7 Macroeconomic Model: Meeting the Energy > 7.2 Current Pollution rates [other] zone=middle order=7/1 area=0.058 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 3 p11: sec=7 Macroeconomic Model: Meeting the Energy > 7.2 Current Pollution rates [other] zone=bottom order=8/2 area=0.043 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 7x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=1 txt=1 width=full orient=portrait cont=False

table 4 p13: sec=7 Macroeconomic Model: Meeting the Energy > 7.4 Quantizing Cost [model] zone=middle order=9/1 area=0.059 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 6x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 5 p18: sec=8 Meshing the Micro and Macro Models [result] zone=middle order=14/1 area=0.056 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 6 p18: sec=8 Meshing the Micro and Macro Models [result] zone=middle order=15/2 area=0.056 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 7 p18: sec=8 Meshing the Micro and Macro Models [result] zone=bottom order=16/3 area=0.056 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 8 p19: sec=8 Meshing the Micro and Macro Models [result] zone=top order=17/1 area=0.056 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 8x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 9 p19: sec=8 Meshing the Micro and Macro Models [result] zone=middle order=18/2 area=0.028 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 6x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=1 txt=1 width=full orient=portrait cont=False

