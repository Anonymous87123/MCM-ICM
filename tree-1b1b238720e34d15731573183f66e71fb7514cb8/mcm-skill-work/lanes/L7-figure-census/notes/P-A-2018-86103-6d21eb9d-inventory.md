# P-A-2018-86103-6d21eb9d — figure census

- layout sha `4f863c907040dd0b`, 28 pages, 34 measured regions
- accounted: 18 figures, 6 tables, 10 excluded, 0 unaccounted
- families: bar 3, flowchart-or-schematic 5, line 4, surface-or-3D 6, table-grid 6

1. p2 **bar** conf=high panels=1
   bbox [313.9, 445.2, 500.2, 563.6] (?)
   cap: Figure 2 The relationship between the wind scale and the first reflection intensity
   note: an Excel clustered-column chart with its numeric data table burned into the same image: nine wind-scale categories on x, three series (10MHz, 20MHz, 30MHz), y 'The Strength of the First Reflection P (dBw)' from -161 to -158, a legend chip block inside the plot area at lower left, and dashed leader lines running from each bar down to a three-row value table that prints -161.2 to -167.4 under the x axis. Pasted as a screenshot with a light grey frame, so the table half is artwork, not a constructible grid. This is the same chart as the body's Figure 10, printed twice under two different numbers
2. p2 **surface-or-3D** conf=high panels=1
   bbox [103.0, 585.0, 273.7, 710.3] (?)
   cap: Figure 1 The wave situation when the wind scale is 6
   note: the abstract's three-dimensional sea surface: a faceted MATLAB surf of the Longuet-Higgins model with height colour-mapped across the mesh, x and y both 0 to 500 and a vertical axis 100 to 300, no axis titles and no colourbar. This is the exhibit the abstract text calls 'the three-dimensional simulation diagram of the waves'. It prints BELOW the abstract's Figure 2 and carries the smaller number, so the abstract page numbers its two exhibits against reading order
3. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [154.7, 71.4, 439.7, 202.6] (?)
   cap: Figure 1 HF propagation diagram
   note: a pasted illustration, not a plot: a photographic Earth globe at the lower right, a gradient sky, a satellite inset, red and blue single-hop and multi-hop ray paths between ground and an 'ionosphere' band, and concentric ground-wave arcs. No axes, no ticks, no key, no scale of any kind - the only quantitative content is the words 'ionosphere' burned into the image. It reuses the number 1 of the abstract's surface plot two pages earlier
4. p8 **flowchart-or-schematic** conf=high panels=2
   bbox [156.0, 409.3, 422.6, 553.2] (?)
   cap: Figure 2 Inner layers of ionosphere
   note: two banded frames side by side, 'Night' and 'Day', each stacking the ionospheric layers as coloured stripes labelled F, F1, F2, E, D inside the bands. Only the left frame carries a y axis, 'Height(km)' with ticks 0/100/200/300, and the shared scale is the reason the right frame prints none; the x axis is unlabelled and a centre divider reads as a frame edge. No (a)/(b) panel letters. Second reuse of a body number already spent on the abstract
5. p10 **surface-or-3D** conf=high panels=1
   bbox [164.3, 132.0, 292.3, 226.0] (?)
   cap: Figure 3 Wave situation of 5∼8 winds
   note: panel 1 of the four-frame Figure 3 grid (wind scales 5 to 8, read in reading order): the same faceted surf as the abstract's Figure 1, at a coarser grid, with x and y 0 to 500 and z 100 to 300 but no axis titles. The four frames are four separate measured regions because the export left a wide gutter between them, and no (a)-(d) labels exist anywhere - the order is implied by the caption's range '5∼8' alone
6. p10 **surface-or-3D** conf=high panels=1
   bbox [308.8, 132.2, 436.8, 226.0] (?)
   cap: Figure 3 Wave situation of 5∼8 winds
   note: panel 2 of Figure 3: same axes, same palette, one wind scale further on. The frames differ only in facet density, so a reader cannot tell which wind scale he is looking at without counting the caption's range
7. p10 **surface-or-3D** conf=high panels=1
   bbox [162.8, 261.0, 290.9, 354.7] (?)
   cap: Figure 3 Wave situation of 5∼8 winds
   note: panel 3 of Figure 3: the lower-left frame, the roughest sea of the four, with the same unlabelled 0-500 base and 100-300 height
8. p10 **surface-or-3D** conf=high panels=1
   bbox [307.3, 261.0, 435.4, 354.7] (?)
   cap: Figure 3 Wave situation of 5∼8 winds
   note: panel 4 of Figure 3: lower-right frame, closing the wind-scale range. With the caption printed once for four frames, this exhibit is the paper's only multi-panel figure that shares one caption across regions the detector measured separately
9. p10 **flowchart-or-schematic** conf=high panels=1
   bbox [151.1, 579.0, 441.6, 716.3] (?)
   cap: Figure 4 Parts of transmission loss
   note: a left-to-right decomposition tree: a pale-blue 'Transmission loss Lb' root box with four grey boxes stacked vertically to its right (free space Lbf, ionospheric absorption La, sea surface reflection Lg, additional YP) joined by dashed curved connectors, all labels burned in. No axes, no numbers. The node labelled 'La' contradicts equation (5) printed directly above it, which decomposes Lb into Lbf + Li + Lg + YP - the diagram and the formula disagree on the ionospheric term's letter
10. p12 **line** conf=high panels=2
   bbox [149.4, 440.8, 444.5, 676.3] (?)
   cap: Figure 5 The relationship between RH , RV and incidence angle
   note: two MATLAB frames side by side, 'incident angle( ° )' on x from 0 to 90 and 'reflection coefficient' on y from 0.2 to 1 in both, blue and red traces for the two working frequencies the code sets. No key anywhere: the legend call is commented out in the appendix listing, so the colours are identified only by the caption's prose. The left frame falls monotonically and the right frame dips to a minimum near 8 degrees, the paper's only non-monotone curve
11. p13 **flowchart-or-schematic** conf=high panels=1
   bbox [112.1, 172.8, 481.8, 295.1] (?)
   cap: Figure 6 Diagram of electromagnetic wave reflection on turbulent ocean
   note: a hand-drawn ray construction: seven or eight arrow-headed rays from upper left striking a thick cyan wavy sea profile, with reflected rays leaving at matching angles and one near-vertical ray. No axes, no ticks, no key, no letters - the only annotation is the wave line itself. This is the paper's one attempt to draw the geometry that the rest of section 4.3.3 computes
12. p14 **flowchart-or-schematic** conf=high panels=1
   bbox [156.0, 71.4, 467.0, 218.8] (?)
   cap: Figure 7 Diagram of wave shadow
   note: the mechanism behind the correction coefficient: two rays grazing a cyan wave profile with the occluded pocket between wave crest and ray filled with hatching. No axes, no key, no numbers - the hatched area is the 'shaded area' that equation (17) divides by the total surface area, and the figure is the only thing that explains what s means
13. p14 **line** conf=high panels=2
   bbox [137.3, 484.4, 439.9, 720.0] (?)
   cap: Figure 8 Diagrams of correction coefficients
   note: two frames of the correction coefficient against 'wind speed(m/s)' 0 to 20: the left one keyed 10MHz/20MHz/30MHz with y 0.97 to 1, the right one keyed 1°/5°/15° with y 0.84 to 1, both keys boxed inside the lower left. The two frames hold the same three curves at different grazing angles, so the pair is a wind-speed sweep drawn twice rather than two variables - and the y ranges differ by a factor of five, which the shared 0-20 x axis hides
14. p15 **line** conf=high panels=1
   bbox [143.4, 173.5, 439.8, 409.1] (?)
   cap: Figure 9 Relation curve of reflection coefficient under different wind speed
   note: one frame, four decaying traces keyed inside at upper right as calm / level 2 / level 4 / level 6, x 'frequency(MHz)' from 0 to 30 and y 'reflection coefficient' from 0.1 to 1. The wind states are named in words, not by the sea state numbers the prose uses elsewhere, so the figure and the text do not share a vocabulary; the top trace is flat enough that the caption's 'under different wind speed' is visible only in the lower three
15. p16 **bar** conf=high panels=1
   bbox [126.4, 112.1, 467.5, 314.8] (?)
   cap: Figure 10 The strength of the first reflection P1
   note: the same Excel screenshot as the abstract's Figure 2, printed at body size with its numeric table burned in and its legend chips floating inside the plot area. Caption carries the only symbol in the paper's caption set ('P1'), and the values run -154.2 to -167.4 dBw. Because the table is pixels, none of the numbers this exhibit exists to communicate can be extracted as text
16. p18 **line** conf=high panels=2
   bbox [137.6, 297.4, 438.7, 552.4] (?)
   cap: Figure 11 Reflection coefficient relationship curves under different ground conditions
   note: the ground twin of Figure 5: two frames against 'frequency(MHz)', the left one titled 'reflection coefficient' and the right one 'sea surface reflection loss' (the y title was not updated when the ground case was cloned from the sea case), four traces keyed calm / hills / low mountains / middle mountains inside the right frame only. The left panel's traces are therefore identified by colour alone, and the right panel converts the same four curves to a negative dB scale
17. p19 **bar** conf=high panels=1
   bbox [97.9, 71.4, 493.2, 306.2] (?)
   cap: Figure 12 Strength of the first reflection
   note: the same chart a third time, with the axis recast for terrain: pasted Excel clustered columns, y 'The Strength of the First Reflection P (dBw)', x 'The relief degree', three series, a data table burned in under the plot and leader lines down to it. The x title is detached below the embedded table and the y title is set at roughly twice the size of the tick numerals, so the exhibit reads as a screenshot pasted at the wrong scale
18. p20 **surface-or-3D** conf=high panels=1
   bbox [119.4, 87.6, 462.2, 309.0] (?)
   cap: Figure 13 Relationships among distance, frequency and SNR
   note: the paper's only exhibit with three data axes: a MATLAB surf of SNR against 'Distances /km' (the x ticks print 00 for the leading zero) and 'Frequency /MHz', z 'SNR /dB', coloured by a jet colourbar running -50 to 100. It is also the only colourbar in the paper and the only 3-D exhibit whose vertical axis is a measured quantity rather than a surface height. No key: the colour is the fourth dimension

## tables
1. p7 table-grid bbox [94.4, 215.1, 501.6, 469.4]
   cap: 
2. p16 table-grid bbox [204.2, 381.9, 391.1, 465.3]
   cap: Table 1 Related Parameters
3. p17 table-grid bbox [129.7, 363.2, 470.6, 454.3]
   cap: Table 2 Atmospheric noise at different times in a certain area in summer
4. p18 table-grid bbox [132.0, 649.4, 463.8, 732.9]
   cap: Table 3 ε,σ in different environments
5. p20 table-grid bbox [121.0, 442.9, 474.9, 538.7]
   cap: Table 4 Maximum propagation distance r when f =15Hz, P =100w
6. p21 table-grid bbox [88.2, 289.4, 515.5, 399.1]
   cap: Table 5 Recommended emission frequency 2∼ 4 MHz Tropical frequency, small number of sunspots and transmission is good.

## excluded
- p9 not-an-exhibit bbox [212.3, 240.4, 514.4, 283.9] p9 equation (1)
- p9 not-an-exhibit bbox [191.3, 348.1, 507.0, 387.1] p9 equation (2)
- p9 not-an-exhibit bbox [182.5, 467.4, 514.0, 499.0] p9 equation (3)
- p9 not-an-exhibit bbox [139.3, 665.3, 514.3, 705.8] p9 equation (4)
- p11 not-an-exhibit bbox [104.0, 229.1, 527.0, 271.8] p11 equation (7)
- p11 not-an-exhibit bbox [125.0, 499.4, 522.5, 550.4] p11 equation (8)
- p12 not-an-exhibit bbox [242.6, 171.8, 351.4, 202.7] p12 equation (10)
- p12 not-an-exhibit bbox [176.3, 247.0, 506.5, 370.0] p12 equations (11) to (13)
- p25 not-an-exhibit bbox [87.8, 47.0, 510.3, 135.6] p25 MATLAB code band
- p27 not-an-exhibit bbox [87.8, 47.0, 510.3, 79.8] p27 MATLAB code band

## distillation fields

figure 1 p2: sec=Summary [abstract] zone=middle order=1/1 area=0.044 solo=False
  family=bar panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=2 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 2']
  caption: Figure N words=13 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p2: sec=Summary [abstract] zone=bottom order=2/2 area=0.0427 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=2 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 1']
  caption: Figure N words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p8: sec=4 Radio propagation on sea surface model > 4.1 Introduction to HF propagation > 4.1.2 Structure of ionosphere [model] zone=top order=4/1 area=0.0746 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 1']
  caption: Figure N words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p8: sec=4 Radio propagation on sea surface model > 4.1 Introduction to HF propagation > 4.1.2 Structure of ionosphere [model] zone=middle order=5/2 area=0.0765 solo=False
  family=flowchart-or-schematic panels=2 layout=1x2 shared=True legend=none cbar=False 3d=no printed=True
  mention: first=8 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 2']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p10: sec=4 Radio propagation on sea surface model > 4.2 Wave model > 4.2.3 Model simulation [model] zone=top order=6/1 area=0.024 solo=False
  family=surface-or-3D panels=1 layout=2x2 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 3']
  caption: Figure N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p10: sec=4 Radio propagation on sea surface model > 4.2 Wave model > 4.2.3 Model simulation [model] zone=top order=7/2 area=0.0239 solo=False
  family=surface-or-3D panels=1 layout=2x2 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 3']
  caption: Figure N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p10: sec=4 Radio propagation on sea surface model > 4.2 Wave model > 4.2.3 Model simulation [model] zone=middle order=8/3 area=0.0239 solo=False
  family=surface-or-3D panels=1 layout=2x2 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 3']
  caption: Figure N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p10: sec=4 Radio propagation on sea surface model > 4.2 Wave model > 4.2.3 Model simulation [model] zone=middle order=9/4 area=0.0239 solo=False
  family=surface-or-3D panels=1 layout=2x2 shared=False legend=none cbar=False 3d=surface-mesh printed=True
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 3']
  caption: Figure N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p10: sec=4 Radio propagation on sea surface model > 4.3 Transmission loss of HF radio waves Lb [model] zone=bottom order=10/5 area=0.0795 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 4']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p12: sec=4 Radio propagation on sea surface model > 4.3 Transmission loss of HF radio waves Lb > 4.3.3 Sea surface reflection loss Lg [model] zone=middle order=11/1 area=0.1386 solo=False
  family=line panels=2 layout=1x2 shared=True legend=none cbar=False 3d=no printed=True
  mention: first=12 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 5']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p13: sec=4 Radio propagation on sea surface model > 4.3 Transmission loss of HF radio waves Lb > 4.3.3 Sea surface reflection loss Lg [model] zone=top order=12/1 area=0.0902 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 6']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p14: sec=4 Radio propagation on sea surface model > 4.3 Transmission loss of HF radio waves Lb > 4.3.3 Sea surface reflection loss Lg [model] zone=top order=13/1 area=0.0914 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 7']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p14: sec=4 Radio propagation on sea surface model > 4.3 Transmission loss of HF radio waves Lb > 4.3.3 Sea surface reflection loss Lg [model] zone=bottom order=14/2 area=0.1422 solo=False
  family=line panels=2 layout=1x2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=14 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 8']
  caption: Figure N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p15: sec=4 Radio propagation on sea surface model > 4.3 Transmission loss of HF radio waves Lb > 4.3.3 Sea surface reflection loss Lg [model] zone=middle order=15/1 area=0.1393 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=15 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 9']
  caption: Figure N words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p16: sec=4 Radio propagation on sea surface model > 4.4 First reflection intensity [result] zone=top order=16/1 area=0.1379 solo=False
  family=bar panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 10']
  caption: Figure N words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p18: sec=5 Comparison between sea surface model and ground surface [evaluation] zone=middle order=19/1 area=0.1531 solo=False
  family=line panels=2 layout=1x2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 11']
  caption: Figure N words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p19: sec=5 Comparison between sea surface model and ground surface [evaluation] zone=top order=21/1 area=0.1851 solo=False
  family=bar panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=19 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 12']
  caption: Figure N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p20: sec=6.1 Maximum time(tmax) using the same multi-hop path [result] zone=top order=22/1 area=0.1514 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=True 3d=surface-mesh printed=True
  mention: first=20 lead=0 count=1 read=0 gap=0 pattern=none style=['Figure 13']
  caption: Figure N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p7: sec=3 Notation [symbols] zone=middle order=3/1 area=0.2065 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 16x2 header=1 rules=booktabs zebra=True merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 2 p16: sec=4 Radio propagation on sea surface model > 4.4 First reflection intensity [result] zone=middle order=17/2 area=0.0311 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=16 lead=0 count=0 read=0 gap=0 pattern=none style=['Table 1']
  caption: Table N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 5x3 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=True dec=False num=2 txt=1 width=full orient=portrait cont=False

table 3 p17: sec=4 Radio propagation on sea surface model > 4.5 Calculation of SNR > 4.5.2 Field intensity of atmospheric noise [model] zone=middle order=18/1 area=0.0619 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=17 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 2']
  caption: Table N words=13 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 4x10 header=3 rules=boxed zebra=False merged=True diag=True units_hdr=False dec=False num=9 txt=1 width=full orient=portrait cont=False

table 4 p18: sec=5 Comparison between sea surface model and ground surface [evaluation] zone=bottom order=20/2 area=0.0553 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=18 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 3']
  caption: Table N words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 4x5 header=2 rules=boxed zebra=False merged=True diag=False units_hdr=True dec=False num=4 txt=1 width=full orient=portrait cont=False

table 5 p20: sec=6.1 Maximum time(tmax) using the same multi-hop path [result] zone=middle order=23/2 area=0.0676 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=20 lead=0 count=0 read=0 gap=0 pattern=none style=['Table 4']
  caption: Table N words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x3 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=True dec=False num=3 txt=0 width=full orient=portrait cont=False

table 6 p21: sec=6.2 Suggestions on frequency selection of transmitter [result] zone=middle order=24/1 area=0.0935 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=21 lead=0 count=1 read=0 gap=0 pattern=none style=['Table 5']
  caption: Table N words=18 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 5x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

