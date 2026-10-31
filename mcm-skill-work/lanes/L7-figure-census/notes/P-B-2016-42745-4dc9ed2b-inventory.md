# P-B-2016-42745-4dc9ed2b — figure census

- layout sha `5f74a621729554d3`, 26 pages, 43 measured regions
- accounted: 25 figures, 3 tables, 15 excluded, 0 unaccounted
- families: bar 11, heatmap-or-contour 1, histogram 1, line 2, scatter 10, table-grid 3

1. p2 **scatter** conf=high panels=1
   bbox [186.72, 420.6, 408.36, 618.96] (raster)
   cap: 
   note: A teaser on the second page of the paper, not a result: a 1000 by 1000 lattice of small grey dots with a circular void about 300 cells across at its centre and a dense black ring at a radius of roughly 700 to 800 cells, thinning outward. The only text on it is the in-plot title 'Simulation Space Debris Distribution' and the cell indices X and Y from 0 to 1000; no colour bar, no legend, no annotation, no unit. It prints three pages before the body's first figure and it is the same plot as Figure 5, printed here at 0.088 of the page against that row's 0.179, with identical box aspect (1.117). The sentence that introduces it names no exhibit - 'The simulated debris distribution is as follows:' - and it is the only exhibit in the paper that sits in an abstract.
2. p13 **histogram** conf=high panels=1
   bbox [119.15, 299.39, 303.11, 412.67] (raster)
   cap: Figure 1 [12]
   note: A stepped histogram of the catalogued population against altitude: a thick blue stair-step series across 'Altitude (km)' 200 to 1900 on an ordinate 'Spatial Density (no./km3)' running 0 to 6.5E-08, rising to a double peak near 800 and 850 km, collapsing to almost nothing by 1200 km and showing a second small cluster near 1400 to 1500 km. Three smooth curves are laid over it - black (FR + Iridium + Cosmos fragments), red (FY-1C fragments) and green (Iridium + Cosmos fragments) - keyed by a four-entry legend inside the frame at the top right, blue being 'All objects'. A red-outlined text box inside the plot area reads 'Cataloged objects only: as of January 2013'. The figure prints no title of its own, and its caption is the number plus a citation marker, 'Figure 1 [12]', with no describing word.
3. p13 **line** conf=high panels=1
   bbox [336.0, 292.32, 497.28, 413.28] (raster)
   cap: Figure 2
   note: The gamma p.d.f. the whole model is built on: one smooth black curve peaking at about 0.038 at x = 30 and decaying to zero by x = 80, against 'x' 0 to 90 and 'probability' 0 to 0.045, with the in-plot title '2D Gamma P.D.F' and a one-entry legend inside the frame at the top right reading 'gamma'. NO PARAMETER IS PRINTED ON THE FIGURE: the shape and rate parameters the text names can only be read back off the curve's peak. This is also the only exhibit cited in the lower case - 'shown in figure 2' - in a paper that otherwise capitalises.
4. p13 **scatter** conf=high panels=1
   bbox [115.6, 561.76, 270.04, 709.6] (raster)
   cap: Figure 3
   note: The three-dimensional spread of debris over a pale blue Earth: a dense black shell of points hugging the globe, thinning outward into scattered dots, with no axes, no scale, no legend and no title. A NASA credit line, '(Source: Image of the day, NASA, 2009)', prints in italic below the image and immediately above its 'Figure 3' label, so the credit belongs to the Earth picture underneath the data - it is the only exhibit in the paper that carries a source credit. The exhibit therefore mixes a borrowed raster with the paper's own point data and prints nothing that separates the two.
5. p13 **heatmap-or-contour** conf=high panels=1
   bbox [316.68, 557.64, 501.57, 709.31] (vector)
   cap: Figure 4
   note: The same p.d.f. seen from above: a colour-mapped annulus titled 'Spatial Gamma P.D.F.' on a 0 to 100 by 0 to 100 cell grid, dark blue inside a circle of radius 30 cells, a hot red band at a radius of about 45 to 55 cells, cooling outward and running into the top edge of the frame, with a colour bar on the right from 0 to 0.035 in steps of 0.005. Neither axis carries a unit - x and y are cell indices - and nothing states what the colour means beyond the title. The four image tiles the extractor measured within this figure's area are declared exclusions, not four more exhibits; the paper derives it in one sentence from the 3D p.d.f. without saying what was integrated.
6. p14 **scatter** conf=high panels=1
   bbox [150.24, 437.04, 466.8, 720.48] (raster)
   cap: Figure 5
   note: The debris matrix as the paper renders it: the same 1000 by 1000 cell picture as the executive summary's teaser, printed here at about twice that size (0.179 of the page) with the same frame aspect, axes 'X' and 'Y' from 0 to 1000, a grey grid, a central void and a dense ring of points at a radius of roughly 700 to 800 cells, under the in-plot title 'Simulation Space Debris Distribution'. No legend and no colour bar. Its caption is 'Figure 5', and the pointer sentence prints the label twice - '... can be vividly shown in the following Figure 5, Figure 5' - because the sentence's own trailing label is immediately followed by the printed one.
7. p16 **line** conf=high panels=1
   bbox [152.52, 136.56, 464.28, 335.04] (vector)
   cap: Figure 6 (Data Source: Space-Track.org)
   note: The historical launch record the model starts from: about fifteen round markers at annual spacing from 2001 to 2015 joined by a line, each marker printing its value above it, over 'Year' and an ordinate simply labelled 'Amount' from 0 to 300, in-plot title 'The Amount of Satellites launched', with a thin dotted straight trend drawn across the series that no legend keys. THE SERIES DOES NOT SHOW THE MODEL'S OWN ASSUMPTION: the text says 'The initially quantity of orbiting satellites is set to 110, and this number will increase by 5% each year', which would be a monotone rise, while the plotted record is the observed catalogue instead - it falls away to 40 and climbs back to 150 - so the exhibit and the sentence describe different objects, and the dotted trend matches neither. The caption's second line, '(Data Source: Space-Track.org)', is the only attribution any exhibit here gets.
8. p17 **bar** conf=high panels=1
   bbox [98.04, 228.84, 339.0, 398.52] (vector)
   cap: Figure 7
   note: A bar-and-line chart on twin ordinates: blue bars of accumulated profit per year against 'Accumulated Profits (billions)' on the left axis, -2 to 10 in steps of 2, and an orange dashed series of debris on the right axis, 11500 to 12500, which ends in a large arrowhead at year 15. The two series are keyed by an unboxed legend ABOVE the data frame, a bar swatch beside 'Accumulated Profits (billions)' and a dashed-arrow swatch beside 'Debris left'. THE TITLE AND THE AXIS NAME THE SAME SERIES DIFFERENTLY - the title reads 'The Profits v.s. the Number of Debris remaining' and the right axis reads 'Debris left' - and the right axis prints no unit at all. The first eight bars are negative, which is the net loss the prose reads off the exhibit, and the abscissa prints only 1 to 15 although the prose's window is 2016 to 2030.
9. p17 **scatter** conf=high panels=1
   bbox [339.0, 256.8, 497.28, 398.52] (raster)
   cap: Figure 8
   note: The debris matrix again, printed beside the profit chart at a quarter of Figure 5's size (0.045 of the page, the same 1.117 frame aspect): same 1000 by 1000 frame, same grey grid, same ring, same in-plot title 'Simulation Space Debris Distribution', no legend and no colour bar. Nothing on the page says which simulation year or which alternative it belongs to, and the prose names no figure - the section points at its exhibits only with 'the results are presented in the following figures'.
10. p18 **bar** conf=high panels=1
   bbox [98.04, 72.72, 339.0, 242.88] (vector)
   cap: Figure 9
   note: The same chart template for the space-based alternative: bars of accumulated profit against a left axis now running 0 to 30 in steps of 5, the same orange dashed debris series on a right axis 11500 to 13500, the same unboxed legend above the frame, the same title 'The Profits v.s. the Number of Debris remaining' and the same disagreement with its own right axis label 'Debris left'. Nothing on the exhibit distinguishes it from Figure 7 except the axis numbers, so the two alternatives are compared by a reader who has to remember which page they were on.
11. p18 **scatter** conf=high panels=1
   bbox [339.0, 100.8, 497.28, 242.52] (raster)
   cap: Figure 10
   note: The debris matrix a third time, the same 0.045-of-page box as Figure 8 with the identical frame aspect, axes, grid and in-plot title. The prose beside it reads a sharp rise over the last five years off the picture, and nothing on the picture dates it or gives it a count.
12. p18 **bar** conf=high panels=1
   bbox [98.04, 571.92, 339.0, 741.96] (vector)
   cap: Figure 11
   note: The combined alternative's profit chart: the same template again, left axis labelled 'Accumulated Profits (billions)' with odd ticks from -3 to 17, the dashed debris series on a right axis 7000 to 14000, legend above the frame, and the same title/axis mismatch ('remaining' against 'left'). This is the chart whose result the paper adopts - the prose reads a net profit of nearly 16 billion at year 15 off it - and no value is printed on the bar it points at, so the 16 has to be read off the ticks.
13. p18 **scatter** conf=high panels=1
   bbox [339.0, 600.0, 497.28, 741.72] (raster)
   cap: Figure 12
   note: The debris matrix a fourth time, in the same quarter-page box as Figures 8 and 10: identical frame, identical in-plot title, no legend, no colour bar, no date and no total. Four of this paper's exhibits are the same picture at the same size, three of them on the two pages of section 6, and none of them is labelled with the simulation run it shows.
14. p19 **scatter** conf=high panels=1
   bbox [100.8, 525.12, 290.76, 695.16] (raster)
   cap: Figure 13, 4%
   note: The debris matrix as it renders at an increase rate of 4 percent: the same square template as Figure 5 - identical frame, grey grid, axes X and Y from 0 to 1000, in-plot title 'Simulation Space Debris Distribution' with an increase-rate clause appended - distinguishable only by the density of the point cloud. THE PARAMETER IS PRINTED AS A SUFFIX ON THE CAPTION AND NOWHERE ELSE that is legible: the in-plot title is too small at printed size to read, the axes carry cell indices and no count, and the prose introduces all four with 'present the corresponding figures', which names no figure. It is one of a pair printed side by side on the same page, two captions and nothing between them, so the reader is asked to compare densities by eye across two pictures that print no count, no total and no scale.
15. p19 **scatter** conf=high panels=1
   bbox [304.56, 525.12, 494.52, 695.16] (raster)
   cap: Figure 14, 3%
   note: The debris matrix as it renders at an increase rate of 3 percent: the same square template as Figure 5 - identical frame, grey grid, axes X and Y from 0 to 1000, in-plot title 'Simulation Space Debris Distribution' with an increase-rate clause appended - distinguishable only by the density of the point cloud. THE PARAMETER IS PRINTED AS A SUFFIX ON THE CAPTION AND NOWHERE ELSE that is legible: the in-plot title is too small at printed size to read, the axes carry cell indices and no count, and the prose introduces all four with 'present the corresponding figures', which names no figure. 
16. p20 **scatter** conf=high panels=1
   bbox [100.8, 72.72, 290.76, 242.88] (raster)
   cap: Figure 15, 2%
   note: The debris matrix as it renders at an increase rate of 2 percent: the same square template as Figure 5 - identical frame, grey grid, axes X and Y from 0 to 1000, in-plot title 'Simulation Space Debris Distribution' with an increase-rate clause appended - distinguishable only by the density of the point cloud. THE PARAMETER IS PRINTED AS A SUFFIX ON THE CAPTION AND NOWHERE ELSE that is legible: the in-plot title is too small at printed size to read, the axes carry cell indices and no count, and the prose introduces all four with 'present the corresponding figures', which names no figure. It is the first thing printed on its page - the figure pair sits at the very top, above all of the prose - while the discussion it belongs to began at the foot of the previous page.
17. p20 **scatter** conf=high panels=1
   bbox [304.56, 72.72, 494.52, 242.88] (raster)
   cap: Figure 16, logarithm
   note: The debris matrix as it renders at a logarithmic increase rate: the same square template as Figure 5 - identical frame, grey grid, axes X and Y from 0 to 1000, in-plot title 'Simulation Space Debris Distribution' with an increase-rate clause appended - distinguishable only by the density of the point cloud. THE PARAMETER IS PRINTED AS A SUFFIX ON THE CAPTION AND NOWHERE ELSE that is legible: the in-plot title is too small at printed size to read, the axes carry cell indices and no count, and the prose introduces all four with 'present the corresponding figures', which names no figure. This is the sparsest of the four point clouds, which is the one thing that distinguishes it from its three companions and which agrees with the numbers the prose quotes for it (debris down from 6374 to 5313 across the step, the smallest of the four reductions).
18. p21 **bar** conf=high panels=1
   bbox [90.0, 78.96, 288.36, 220.68] (vector)
   cap: Figure 17
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_lifetime_3', left axis 'Profits (Billions)' with ticks -5 to 25 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 17', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. 
19. p21 **bar** conf=high panels=1
   bbox [299.4, 78.96, 497.76, 220.68] (vector)
   cap: Figure 18
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_lifetime_6', left axis 'Profits (Billions)' with ticks -5 to 25 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 18', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. 
20. p21 **bar** conf=high panels=1
   bbox [90.0, 250.56, 288.36, 392.28] (vector)
   cap: Figure 19
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_lifetime_9', left axis 'Profits (Billions)' with ticks -5 to 25 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 19', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. Same frame and same scale as its three companions, so the four lifetime runs are the first set in the paper that can be read against one another at a glance.
21. p21 **bar** conf=high panels=1
   bbox [299.4, 250.56, 497.76, 392.28] (vector)
   cap: Figure 20
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_lifetime_12', left axis 'Profits (Billions)' with ticks -5 to 25 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 20', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. The four charts of this page carry the section's whole result - the prose reads a 0.38 billion rise per extra year of lifetime off them - and none of them prints a value on a bar or a scale beyond its nine ticks.
22. p22 **bar** conf=high panels=1
   bbox [90.0, 78.96, 288.36, 220.68] (vector)
   cap: Figure 21
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_alpha_6%', left axis 'Profits (Billions)' with ticks -5 to 30 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 21', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. 
23. p22 **bar** conf=high panels=1
   bbox [299.4, 78.96, 497.76, 220.68] (vector)
   cap: Figure 22
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_alpha_5%', left axis 'Profits (Billions)' with ticks -5 to 30 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 22', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. 
24. p22 **bar** conf=high panels=1
   bbox [90.0, 266.16, 288.36, 407.88] (vector)
   cap: Figure 23
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_alpha_4%', left axis 'Profits (Billions)' with ticks -5 to 30 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 23', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. 
25. p22 **bar** conf=high panels=1
   bbox [299.4, 266.16, 497.76, 407.88] (vector)
   cap: Figure 24
   note: A column chart of accumulated profit against year, in-plot title 'Accumulated Profits_alpha_3%', left axis 'Profits (Billions)' with ticks -5 to 30 in steps of 5, abscissa 'Years' from 1 to 15, no legend, no gridline, and no value printed on any bar - the only numbers on the exhibit are the axis ticks. The caption below it is nothing but 'Figure 24', and the title is a variable name with an underscore rather than a sentence, so the parameter that distinguishes this chart from the other seven is printed inside the frame only. The alpha sweep runs downward - 6, 5, 4, 3 - while the lifetime page above runs upward, and neither page prints anything that orders its four charts but their position.

## tables
1. p8 table-grid bbox [88.56, 427.2, 506.76, 758.64]
   cap: 
2. p23 table-grid bbox [184.2, 118.8, 411.12, 255.84]
   cap: 
3. p23 table-grid bbox [184.2, 380.64, 411.12, 517.56]
   cap: 

## excluded
- p6 not-an-exhibit bbox [88.56, 124.8, 506.76, 271.2] a block of the Introduction's prose that the extractor boxed because its text lines are drawn as paths: the words are the discussion of the land-based methods and of the laser broom, with no picture, rule, caption or number in it
- p6 not-an-exhibit bbox [88.56, 298.8, 506.76, 361.2] a block of the Introduction's prose that the extractor boxed because its text lines are drawn as paths: the words are the discussion of the land-based methods and of the laser broom, with no picture, rule, caption or number in it
- p6 not-an-exhibit bbox [88.56, 375.24, 506.76, 515.64] a block of the Introduction's prose that the extractor boxed because its text lines are drawn as paths: the words are the discussion of the land-based methods and of the laser broom, with no picture, rule, caption or number in it
- p6 not-an-exhibit bbox [90.0, 663.36, 505.32, 723.12] a block of the Introduction's prose that the extractor boxed because its text lines are drawn as paths: the words are the discussion of the land-based methods and of the laser broom, with no picture, rule, caption or number in it
- p6 not-an-exhibit bbox [90.0, 741.36, 505.32, 769.92] a block of the Introduction's prose that the extractor boxed because its text lines are drawn as paths: the words are the discussion of the land-based methods and of the laser broom, with no picture, rule, caption or number in it
- p7 not-an-exhibit bbox [90.0, 73.32, 505.32, 101.88] the same kind of boxed prose, here the discussion of Huff-and-Puff, snagging and nets - body text, not an exhibit
- p7 not-an-exhibit bbox [90.0, 120.12, 505.32, 211.08] the same kind of boxed prose, here the discussion of Huff-and-Puff, snagging and nets - body text, not an exhibit
- p7 not-an-exhibit bbox [90.0, 229.32, 505.32, 304.68] the same kind of boxed prose, here the discussion of Huff-and-Puff, snagging and nets - body text, not an exhibit
- p7 not-an-exhibit bbox [89.88, 354.12, 505.32, 413.88] the same kind of boxed prose, here the discussion of Huff-and-Puff, snagging and nets - body text, not an exhibit
- p7 not-an-exhibit bbox [89.88, 432.12, 505.32, 507.48] the same kind of boxed prose, here the discussion of Huff-and-Puff, snagging and nets - body text, not an exhibit
- p13 fragment-of-other bbox [316.68, 563.77, 405.41, 636.63] one of the four image tiles that make up Figure 4's own picture: the exhibit is recorded once on the figure's own region above it, so this tile is a fragment of that exhibit and not a fifth figure
- p13 fragment-of-other bbox [405.41, 563.77, 494.17, 636.63] one of the four image tiles that make up Figure 4's own picture: the exhibit is recorded once on the figure's own region above it, so this tile is a fragment of that exhibit and not a fifth figure
- p13 fragment-of-other bbox [316.68, 636.63, 405.41, 709.5] one of the four image tiles that make up Figure 4's own picture: the exhibit is recorded once on the figure's own region above it, so this tile is a fragment of that exhibit and not a fifth figure
- p13 fragment-of-other bbox [405.41, 636.63, 494.17, 709.5] one of the four image tiles that make up Figure 4's own picture: the exhibit is recorded once on the figure's own region above it, so this tile is a fragment of that exhibit and not a fifth figure
- p25 not-an-exhibit bbox [90.0, 240.84, 499.8, 289.08] the References block: a citation list whose hanging indents and rules counted as drawn paths; it is apparatus, not an exhibit

## distillation fields

figure 1 p2: sec=Executive Summary [abstract] zone=middle order=1/1 area=0.088 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p13: sec=5 Model Two – A Model to Determine 𝑷𝑷𝑷𝑷(𝒕𝒕) > 5.2 Some Thoughts [other] zone=middle order=3/1 area=0.042 solo=False
  family=histogram panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=2 read=1 gap=None pattern=figure-n-shows style=['Figure 1']
  caption: Figure N words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p13: sec=5 Model Two – A Model to Determine 𝑷𝑷𝑷𝑷(𝒕𝒕) > 5.2 Some Thoughts [other] zone=middle order=4/2 area=0.039 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=2 read=1 gap=None pattern=parenthetical style=['figure 2']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p13: sec=5 Model Two – A Model to Determine 𝑷𝑷𝑷𝑷(𝒕𝒕) > 5.2 Some Thoughts [other] zone=bottom order=5/3 area=0.046 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 3']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p13: sec=5 Model Two – A Model to Determine 𝑷𝑷𝑷𝑷(𝒕𝒕) > 5.2 Some Thoughts [other] zone=bottom order=6/4 area=0.056 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=True 3d=no printed=False
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 4']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p14: sec=5 Model Two – A Model to Determine 𝑷𝑷𝑷𝑷(𝒕𝒕) > 5.3 Establishing the Debris Distribution Model [model] zone=bottom order=7/1 area=0.179 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=0 count=1 read=1 gap=None pattern=direct style=['Figure 5']
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p16: sec=5 Model Two – A Model to Determine 𝑷𝑷𝑷𝑷(𝒕𝒕) > 5.6 Satellites Launching and Crashing [model] zone=top order=8/1 area=0.123 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p17: sec=6 Results > 6.1 Land-Based Removal Alternative alone [result] zone=middle order=9/1 area=0.082 solo=False
  family=bar panels=1 layout=1 shared=False legend=above cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p17: sec=6 Results > 6.1 Land-Based Removal Alternative alone [result] zone=middle order=10/2 area=0.045 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p18: sec=6 Results > 6.2 Space-based Removal Alternative alone [result] zone=top order=11/1 area=0.082 solo=False
  family=bar panels=1 layout=1 shared=False legend=above cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p18: sec=6 Results > 6.2 Space-based Removal Alternative alone [result] zone=top order=12/2 area=0.045 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p18: sec=6 Results > 6.3 The Combination of the two alternatives [result] zone=bottom order=13/3 area=0.082 solo=False
  family=bar panels=1 layout=1 shared=False legend=above cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p18: sec=6 Results > 6.3 The Combination of the two alternatives [result] zone=bottom order=14/4 area=0.045 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p19: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.1 Scenario 1: New Industrial Standards toward Design and Procedures [sensitivity] zone=bottom order=15/1 area=0.064 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p19: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.1 Scenario 1: New Industrial Standards toward Design and Procedures [sensitivity] zone=bottom order=16/2 area=0.064 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p20: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.1 Scenario 1: New Industrial Standards toward Design and Procedures [sensitivity] zone=top order=17/1 area=0.064 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p20: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.1 Scenario 1: New Industrial Standards toward Design and Procedures [sensitivity] zone=top order=18/2 area=0.064 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p21: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=top order=19/1 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p21: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=top order=20/2 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 20 p21: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=middle order=21/3 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 21 p21: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=middle order=22/4 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 22 p22: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=top order=23/1 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 23 p22: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=top order=24/2 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 24 p22: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=middle order=25/3 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 25 p22: sec=7 Some ‘What if’ Scenarios and Sensitivity Analysis > 7.2 Scenario 2: Recyclable Rocket [sensitivity] zone=middle order=26/4 area=0.056 solo=False
  family=bar panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N words=2 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p8: sec=3 Terminologies and Notations > 3.2 Notations Table [symbols] zone=bottom order=2/1 area=0.277 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 16x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 2 p23: sec=8 A Game Theory Perspective [other] zone=top order=27/1 area=0.062 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x4 header=1 rules=vertical-rules zebra=False merged=False diag=True units_hdr=False dec=False num=3 txt=1 width=half orient=landscape cont=False

table 3 p23: sec=8 A Game Theory Perspective [other] zone=middle order=28/2 area=0.062 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below
  table: 4x4 header=1 rules=vertical-rules zebra=False merged=False diag=True units_hdr=False dec=False num=3 txt=1 width=half orient=landscape cont=False

