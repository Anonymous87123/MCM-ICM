# P-C-2011-10607-6ed4fd93 — figure census

- layout sha `643d00fa4b1dc588`, 20 pages, 17 measured regions
- accounted: 8 figures, 9 tables, 0 excluded, 0 unaccounted
- families: flowchart-or-schematic 3, line 1, node-link-network 1, scatter 3, table-grid 9

1. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [232.56, 115.28, 407.52, 257.6] (raster)
   cap: Figure 1. The coordinate plot of the point source and its polluted area
   note: z/x/y coordinate sketch of a point source and its pollutant plume; a geometric drawing with no plotted data
2. p9 **scatter** conf=high panels=1
   bbox [203.52, 323.6, 415.68, 462.08] (raster)
   cap: Figure 2. AP dispersion of CVs (gasoline)
   note: 3-D perspective point cloud inside an x/y/z box; no surface is rendered, so the family is scatter
3. p9 **scatter** conf=high panels=1
   bbox [206.4, 554.0, 412.8, 689.6] (raster)
   cap: Figure 3. AP dispersion of EVs (thermal power)
   note: the same 3-D box for EVs (thermal power), fewer and lower points
4. p10 **scatter** conf=high panels=1
   bbox [211.2, 72.08, 407.76, 213.68] (raster)
   cap: Figure 4. AP dispersion of EVs (natural gas)
   note: the same 3-D box for EVs (natural gas), the sparsest cloud of the three
5. p15 **line** conf=high panels=1
   bbox [161.52, 72.08, 433.68, 257.36] (raster)
   cap: Figure 7. The number of EVs and CVs (prediction)
   note: two curves (CVs, EVs) against year; no axis titles and no legend box, the series are named by inline text on the curves, dotted gridlines at every tick
6. p16 **flowchart-or-schematic** conf=high panels=1
   bbox [143.52, 554.0, 451.68, 631.76] (raster)
   cap: Figure 8. The energy conversion efficiency of CVs
   note: loss chain crude → gasoline/diesel → driving power, with the energy-loss arrows drawn upward between boxes
7. p16 **flowchart-or-schematic** conf=high panels=1
   bbox [114.96, 665.84, 480.24, 754.64] (raster)
   cap: Figure 9. The energy conversion efficiency of EVs
   note: the same chain for EVs: thermal/nuclear/hydro → electricity → driving power
8. p18 **node-link-network** conf=high panels=1
   bbox [89.76, 190.4, 509.28, 358.88] (raster)
   cap: Figure 10.The hierarchy diagram
   note: AHP hierarchy: goal node O, five criteria C1-C5, four alternatives P1-P4, fully connected between criteria and alternatives

## tables
1. p5 table-grid bbox [106.32, 519.2, 488.16, 664.64]
   cap: Table 1. The relevant parameters of RAV4 EV and RAV.
2. p6 table-grid bbox [104.64, 206.72, 489.6, 254.48]
   cap: Table 2. The calculated results of relevant parameters and LCC($)
3. p6 table-grid bbox [107.04, 501.2, 487.44, 546.8]
   cap: Table 3. The Sensitivity Analysis between relevant parameters and LCC
4. p8 table-grid bbox [102.0, 613.52, 492.48, 727.52]
   cap: Table 4. the comparison of emissions from different types of vehicles (kg/per car)
5. p10 table-grid bbox [155.52, 569.36, 439.68, 598.4]
   cap: Table 5. the average emissions of CVs and EVs (g/per km, per car)
6. p11 table-grid bbox [134.64, 234.8, 459.84, 280.4]
   cap: Table 7. The total number of vehicles in the world (million)
7. p12 table-grid bbox [136.56, 227.84, 458.64, 271.49]
   cap: Table 8. The noise of CVs and EVs in different speed and state (dB)
8. p18 table-grid bbox [123.84, 464.96, 470.64, 576.32]
   cap: Table 9. The O-C judging matrix
9. p19 table-grid bbox [145.2, 127.04, 449.28, 296.96]
   cap: Table 10. max j and CI j of the other judging matrixes

## distillation fields

figure 1 p8: sec=4.1.1.2 Simulation of Gaussian Plume Model [model] zone=top order=4/1 area=0.05 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=8 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 1']
  caption: Figure N. words=13 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p9: sec=4.1.1.3 Results and Discussions of the Simulation [evaluation] zone=middle order=6/1 area=0.059 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=2 read=1 gap=0 pattern=direct style=['Figure 2']
  caption: Figure N. words=7 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p9: sec=4.1.1.3 Results and Discussions of the Simulation [evaluation] zone=bottom order=7/2 area=0.056 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=9 lead=0 count=2 read=0 gap=0 pattern=none style=['Figure 3']
  caption: Figure N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p10: sec=4.1.1.3 Results and Discussions of the Simulation [evaluation] zone=top order=8/1 area=0.056 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=10 lead=0 count=2 read=0 gap=0 pattern=none style=['Figure 4']
  caption: Figure N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p15: sec=6.3 Results and Conclusion [evaluation] zone=top order=12/1 area=0.101 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=14 lead=1 count=3 read=1 gap=1 pattern=direct style=['Figure 7']
  caption: Figure N. words=9 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p16: sec=8.1 The Comparison of the Energy Efficiency [other] zone=bottom order=13/1 area=0.048 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=3 read=1 gap=0 pattern=direct style=['Figure 8']
  caption: Figure N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p16: sec=8.1 The Comparison of the Energy Efficiency [other] zone=bottom order=14/2 area=0.065 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=3 read=1 gap=0 pattern=direct style=['Figure 9']
  caption: Figure N. words=8 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p18: sec=未编号标题 IX.Determining the Weight of Different Electricity Generation [model] zone=top order=15/1 area=0.141 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=2 read=0 gap=0 pattern=none style=['Figure 10']
  caption: Figure N. words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p5: sec=3.2 Data Collection [other] zone=bottom order=1/1 area=0.111 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=5 lead=0 count=2 read=0 gap=0 pattern=none style=['Table 1']
  caption: Table N. words=10 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 9x3 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=True dec=False num=2 txt=1 width=full orient=portrait cont=False

table 2 p6: sec=3.3 Results of the Calculation [solution] zone=top order=2/1 area=0.037 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=6 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 2']
  caption: Table N. words=10 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 3x10 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=9 txt=1 width=full orient=portrait cont=False

table 3 p6: sec=3.3 Results of the Calculation > 3.4 Sensitivity Analysis [sensitivity] zone=middle order=3/2 area=0.035 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=6 lead=0 count=2 read=1 gap=0 pattern=direct style=['Table 3']
  caption: Table N. words=10 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 3x5 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 4 p8: sec=4.1.1.2 Simulation of Gaussian Plume Model [model] zone=bottom order=5/2 area=0.089 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=8 lead=0 count=4 read=1 gap=0 pattern=direct style=['Table 4']
  caption: Table N. words=13 sent=1 units=True vars=0 cond=False concl=False voice=none pos=below
  table: 7x4 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=portrait cont=False

table 5 p10: sec=4.1.1.3 Results and Discussions of the Simulation > 4.1.3 The Statistical Prediction of the Amount of Emissions [other] zone=bottom order=9/2 area=0.016 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=10 lead=0 count=2 read=0 gap=0 pattern=none style=['Table 5']
  caption: Table N. words=13 sent=1 units=True vars=0 cond=False concl=False voice=none pos=below
  table: 3x3 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=2 txt=1 width=full orient=portrait cont=False

table 6 p11: sec=4.1.3 The Statistical Prediction of the Amount of Emissions [other] zone=top order=10/1 area=0.03 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=11 lead=0 count=2 read=1 gap=0 pattern=direct style=['Table 7']
  caption: Table N. words=11 sent=2 units=True vars=0 cond=False concl=False voice=none pos=below
  table: 2x7 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=6 txt=1 width=full orient=portrait cont=False

table 7 p12: sec=4.2.1 Noise Pollution [other] zone=top order=11/1 area=0.028 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=12 lead=0 count=3 read=1 gap=0 pattern=direct style=['Table 8']
  caption: Table N. words=14 sent=2 units=True vars=0 cond=False concl=False voice=none pos=below
  table: 6x6 header=2 rules=booktabs zebra=True merged=True diag=False units_hdr=False dec=False num=4 txt=2 width=full orient=portrait cont=False

table 8 p18: sec=未编号标题 IX.Determining the Weight of Different Electricity Generation [model] zone=middle order=16/2 area=0.077 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=18 lead=0 count=2 read=1 gap=0 pattern=direct style=['Table 9']
  caption: Table N. words=6 sent=2 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 6x6 header=1 rules=vertical-rules zebra=True merged=False diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

table 9 p19: sec=未编号标题 IX.Determining the Weight of Different Electricity Generation [model] zone=top order=17/1 area=0.103 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=0 count=3 read=0 gap=0 pattern=none style=['Table 10']
  caption: Table N. words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 9x6 header=2 rules=vertical-rules zebra=True merged=True diag=False units_hdr=False dec=False num=5 txt=1 width=full orient=portrait cont=False

