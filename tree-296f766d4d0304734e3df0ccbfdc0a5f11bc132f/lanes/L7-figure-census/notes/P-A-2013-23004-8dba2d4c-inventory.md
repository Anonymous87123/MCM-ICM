# P-A-2013-23004-8dba2d4c — figure census

- layout sha `42d0c093e4d5ad3a`, 21 pages, 77 measured regions
- accounted: 23 figures, 3 tables, 51 excluded, 0 unaccounted
- families: composite-panel 2, flowchart-or-schematic 2, heatmap-or-contour 3, line 2, other 10, photo-or-raster-image 1, scatter 1, surface-or-3D 2, table-grid 3

1. p4 **composite-panel** conf=high panels=2
   bbox [96.12, 70.92, 498.6, 175.08] (raster)
   cap: Fig. 1 Basic Model of Baking Pan
   note: Two different kinds of picture in one measured region: on the left a cluster of overlapping greyscale photographs of real metal and glass baking trays, tilted and unaligned; a heavy solid black arrow across the middle; and on the right an isometric wireframe drawing of a rectangular pan with a raised lip on four thin legs. The photograph cluster is photo-or-raster-image and the wireframe is un-axed line art, so the exhibit takes composite-panel rather than one label for the pair.
2. p4 **flowchart-or-schematic** conf=high panels=1
   bbox [149.76, 398.76, 444.72, 535.92] (raster)
   cap: Fig. 2 Heat Flow of the Pan
   note: Isometric line drawing of the slab pan with straight arrows entering each of the four side faces and the top face and dashed arrows rising from the bottom, plus a key at the lower right - a short horizontal line with an arrowhead labelled 'Heat flow'. No axes, no ticks, no numbers: the arrows carry the flux direction per face, which is what makes this a schematic rather than a sketch.
3. p5 **surface-or-3D** conf=high panels=1
   bbox [137.76, 543.84, 456.84, 771.84] (raster)
   cap: Fig. 3 3D - Plot of Heat Distribution of Square Baking Pan Model
   note: A MATLAB perspective surface of the square pan: two raised corners and a saddle-like dip, floor axes running -0.5 to 0.5 with only -0.5 and 0 labelled, height axis 366 to 378 by 2, a dark-red-to-yellow colour map and a vertical colour bar at the right reading 367 to 376 in steps of 1. The header line above the plot reads 'Time=10 Color: T Height: T'. One surface, no legend, no printed values.
4. p6 **line** conf=high panels=1
   bbox [108.48, 70.92, 486.48, 331.08] (raster)
   cap: Fig. 4 Temperature Curve of the Edge of the Square Pan
   note: One boxed plot, y 'Tempurature /K' from 371.5 to 376.5 by 0.5, x unlabelled from -0.5 to 0.5 with ticks only at the ends and the centre. A single thin curve, symmetric, flat at 371.5 near the centre and rising to about 376.4 at both edges - the overcooking profile the paper is built on. One legend entry ('Square') in a boxed frame inside the axes.
5. p6 **surface-or-3D** conf=high panels=1
   bbox [111.24, 412.32, 483.72, 691.8] (raster)
   cap: Fig. 5 3D - Plot of Heat Distribution of Circle Baking Pan Model
   note: The same perspective rendering for the circular pan: a shallow bowl, hot yellow rim and dark-red centre, floor axes -0.8 to 0.6 by 0.2 with only the negative labels printed, height axis 362 to 370 by 2, colour bar at the right 363 to 368 in steps of 0.5. Header 'Time=10 Color: T Height: T'; one surface, no legend, no printed values.
6. p7 **line** conf=high panels=1
   bbox [122.76, 70.92, 471.6, 306.36] (raster)
   cap: Fig. 6 Temperature Curves of Edge of the Different Polygon Pan
   note: Eight curves of one family on one pair of axes: y 'Tempurature /K' 368 to 377 by 1, x unlabelled -0.5 to 0.5. The curves nest, each symmetric with a flat minimum at the centre, the top peaking near 376.6 and the lowest at about 368.5; the legend inside the axes stacks eight entries - Square, Pentagon, Hexagon, Heptagon, Octagon, Decagon, 14-gon, 16-gon - each with a sample line in a different red tone. Eight series, one family, so the family is line and the panel count stays one.
7. p8 **scatter** conf=high panels=1
   bbox [138.48, 70.92, 456.24, 315.72] (raster)
   cap: Fig. 7 Curve Fitting Result
   note: Ten green filled circular markers plotted at the measured points over one straight blue line, the markers keyed 'Original' and the line 'Fitting Curve' in a boxed legend inside the upper right. x '1/m^2' from 0 to 0.07 by 0.01, y 'K' from 0 to 1.6 by 0.2, ticks on all four sides. The markers are the observations and the line is the fitted model, so the family follows the markers: scatter.
8. p9 **other** conf=high panels=5
   bbox [132.48, 70.92, 461.88, 277.44] (raster)
   cap: Fig. 8 Several 2-D Arrangement Methods
   note: The arrangement methods drawn as line art with no axes, no scale and no values: a square field split into a 2 by 2 lattice with a dot per cell, two overlapping hexagons each dot-centred, four octagons in a tight cluster with small diamond gaps, and two lower variants of three dot-centred polygons. Five drawings of one kind, so the family stays `other` with a panel count rather than composite.
9. p10 **other** conf=high panels=1
   bbox [178.2, 298.08, 416.52, 454.08] (raster)
   cap: Fig. 9 Geometric Sketch
   note: A heavy-ruled rectangle labelled L along the top edge, W down the left edge and S inside, with a smaller rectangle inset at the lower-right corner labelled l, w and A, and the ratio 'A width to length ratio: L/W' set in italics above. Line art with no axes, no ticks and no data - the sketch that defines the packing variables used from here on.
10. p10 **other** conf=high panels=1
   bbox [146.76, 630.96, 448.32, 780.96] (raster)
   cap: Fig. 10 An Arrangement of Rectangles
   note: A wall of ruled rectangles - four rows by eight columns - each face lettered A, the rightmost column visibly narrower and separated by two or three extra thin rules per cell. No axes, no labels, no values: the rectangle packing pattern read off the centre-dot matrix.
11. p11 **other** conf=high panels=1
   bbox [211.8, 287.4, 383.16, 372.48] (raster)
   cap: Fig. 11 Pattern 1 of Circle Arrangement
   note: Four staggered rows of open circles, each with a filled centre dot, alternate rows shifted by half a circle so the discs overlap slightly - the hexagonal close-packing case for round pans. Line art only, no axes, no values.
12. p11 **other** conf=high panels=1
   bbox [254.52, 400.8, 340.56, 486.96] (raster)
   cap: Fig. 12 Pattern 2 of Circle Arrangement
   note: The square-aligned alternative: a four by four array of tangent circles, rows and columns in line rather than offset, a filled dot at every centre. No axes, no values; the pair with Figure 11 is the whole circle-arrangement argument.
13. p12 **other** conf=high panels=3
   bbox [129.48, 197.52, 465.48, 284.28] (raster)
   cap: Fig. 13 Different Arrangements
   note: Three panels of equal height side by side: a four by four dotted grid inside a heavy frame, dotted hexagons with centre dots and small diamond voids at the triple junctions, and staggered hexagon rows shifted by half a cell with a partial hexagon hanging off the right edge. Three drawings of one kind, so `other` with a panel count.
14. p12 **other** conf=high panels=1
   bbox [240.48, 351.72, 354.36, 465.12] (raster)
   cap: Fig. 14 Regular Dodecagon and Circle
   note: A regular dodecagon and a circle of almost the same diameter drawn as two thin overlapping outlines, the mismatch showing at the vertices at the sides and the top - the argument that a many-sided polygon may be treated as a circle. Empty interiors, no axes, no labels.
15. p12 **other** conf=high panels=1
   bbox [214.68, 552.72, 380.28, 690.12] (raster)
   cap: Fig. 15 the Arrangement of Heptagon, etc.
   note: Roughly sixteen heptagons in four offset rows, tessellating with diamond-shaped gaps between adjacent rows and contact along alternate edges only - the odd-sided case the paper later admits its model handles badly. Line art, no axes, no values.
16. p13 **other** conf=high panels=1
   bbox [167.76, 528.6, 448.08, 708.6] (raster)
   cap: Fig. 16 Edges and Center Matrix of Octagon
   note: Two thin arrow axes with no ticks, no scale and no labels, over a plane-filling lattice of dotted octagon and hexagon outlines each with a solid centre dot, and a heavy black rectangle overlaid slightly skewed so its lower-left corner sits on the lattice. Recorded as `other`, not scatter: the marks are polygon cells, not measured points, and the axes carry no scale.
17. p14 **other** conf=high panels=1
   bbox [146.04, 219.12, 448.92, 381.48] (raster)
   cap: Fig. 17 Special Condition of Hexagon
   note: The same dotted hexagon lattice and bare arrow axes as Figure 16, with two heavy rectangles crossing at right angles - the rack before and after a ninety-degree rotation. The special case the flowchart's hexagonal branch is written for. No axes scale, no values.
18. p14 **flowchart-or-schematic** conf=high panels=1
   bbox [58.3, 454.59, 534.29, 761.7] (vector)
   cap: Fig. 18 Algorithm Flowchart for 2-D Arrangement Based on Center Dot Matrix
   note: The full algorithm as a flowchart: rounded Start and End terminals, two parallelograms (input boundary equations; output N), four decision diamonds ('Select a dot', 'The dot within boundaries?', 'Dot meets the arranging conditions?') and four process rectangles (initialise N = 0, build the centre-dot matrix, calculate distances, N = N + 1), joined by arrows labelled Yes and No, with a bracketed two-item note at the right about the least distance and the inscribed radius. A bold in-figure title block duplicates the printed caption. Its eight text boxes return as separate measured rasters on the same page and are excluded as parts of it.
19. p15 **photo-or-raster-image** conf=high panels=3
   bbox [96.48, 146.4, 497.88, 263.4] (raster)
   cap: Fig. 19 Testing Oven and Baking Pan
   note: Three catalogue photographs side by side on white: a black countertop toaster oven seen at three-quarter view with three knobs and bakes visible through the glass; an overlapping scatter of wire cooling racks and two black pans; and a tray of finished bakes. The caption names the source URL in the line above. No axes, no numbers - a photograph set, not a plot.
20. p16 **heatmap-or-contour** conf=high panels=1
   bbox [161.76, 426.36, 433.08, 620.16] (raster)
   cap: Fig. 20 Best Arrangement for Test One
   note: A black rectangular plate holding four staggered rows of five hexagons, each hexagon filled with a smooth radial greyscale gradient - pale at the rim, darker toward the centre - and dark high-temperature wedges at the shared corners. The temperature field is rendered straight onto the pan cells: no axes, no ticks, no colour bar, no legend, no printed values. The parameter line above gives m = 6, a = 3.3981 cm.
21. p17 **heatmap-or-contour** conf=high panels=1
   bbox [149.76, 70.92, 462.84, 288.0] (raster)
   cap: Fig. 21 Best Arrangement for Test Two
   note: The same plate rendering for the octagon: three rows of five octagons in a gap-bridging honeycomb arrangement, each filled with the radial greyscale field and dark contact wedges at the corners. No axes, no colour bar, no legend, no printed values.
22. p17 **heatmap-or-contour** conf=high panels=1
   bbox [137.04, 476.04, 457.32, 696.24] (raster)
   cap: Fig. 22 Best Arrangement for Test Three
   note: The third plate: four rows of five octagons, rows two and four offset in a staggered brick packing, same radial greyscale fill and dark corner wedges. Parameter line above reads m = 8, a = 2.4926 cm. No axes, no colour bar, no printed values.
23. p19 **composite-panel** conf=high panels=3
   bbox [95.76, 70.92, 498.96, 318.72] (raster)
   cap: Fig. 23 Changes on Round Corners
   note: A measured region holding two kinds of artwork: a top strip of line art - a plain hollow square, a heavy right arrow and a hollow square with rounded corners, no axes and no labels - and below it two side-by-side 3-D surface plots titled 'Time=10 Color: T Height: T', z 366 to 378 and 366 to 376, floor axes -1 to 1, red-to-yellow surfaces with two corner peaks, each with its own colour bar at the right. Schematic plus two surfaces, so composite-panel with three panels.

## tables
1. p7 table-grid bbox [56.64, 509.83, 538.3, 669.7]
   cap: Table 3 the Deviation of Temperature of Different polygons
2. p15 table-grid bbox [57.0, 498.91, 538.17, 785.5]
   cap: Table 4 All the Arrangements for Optimization (1)
3. p16 table-grid bbox [56.28, 104.54, 538.17, 211.34]
   cap: Table 5 All the Arrangements for Optimization (2)

## excluded
- p5 not-an-exhibit bbox [56.64, 120.26, 538.3, 163.82] A nine-path vector band laid over one line of running body text ('temperature of the air. The boundary condition is Neumann boundary condition...') - a text-run wrapper, not an exhibit. Table 2, whose caption prints on this page, returns no region of its own and is a declared gap.
- p14 fragment-of-other bbox [294.0, 471.0, 390.0, 521.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the decision diamond 'Select a dot / dot within ranges ?'.
- p14 fragment-of-other bbox [58.0, 508.0, 226.0, 549.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the parallelogram 'Input Boundary equations and the shapes of polygon'.
- p14 fragment-of-other bbox [417.0, 510.0, 534.0, 538.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the parallelogram 'Output N as the result'.
- p14 fragment-of-other bbox [294.0, 540.0, 390.0, 589.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the decision diamond 'The dot within boundaries ?'.
- p14 fragment-of-other bbox [100.0, 566.0, 184.0, 607.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the rectangle 'Build the center dot matrix of an arrangement'.
- p14 fragment-of-other bbox [284.0, 608.0, 399.0, 649.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the rectangle 'Calculate the distance between the dot and all the boundaries'.
- p14 fragment-of-other bbox [91.0, 623.0, 193.0, 677.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the rectangle 'Initialize the Number of polygon in this arrangement N = 0'.
- p14 fragment-of-other bbox [298.0, 668.0, 385.0, 712.0] One of the eight text boxes printed inside Figure 18 - part of the flowchart, joined to the rest by its arrows, not an exhibit of its own. Carries the decision diamond 'Dot meets the arranging conditions ?'.
- p15 fragment-of-other bbox [214.8, 515.64, 333.48, 574.68] The arrangement thumbnail printed in the Rectangle, pattern 1 cell of Table 4 - a raster inside the table, counted with the table, not a figure.
- p15 fragment-of-other bbox [424.56, 516.6, 481.32, 573.36] The arrangement thumbnail printed in the Rectangle, pattern 2 cell of Table 4 - a raster inside the table, counted with the table, not a figure.
- p15 fragment-of-other bbox [373.56, 588.48, 532.2, 673.56] The arrangement thumbnail printed in the Regular hexagon, pattern 1 cell of Table 4 - a raster inside the table, counted with the table, not a figure.
- p15 fragment-of-other bbox [187.08, 589.2, 361.32, 673.2] The arrangement thumbnail printed in the Regular hexagon, pattern 2 cell of Table 4 - a raster inside the table, counted with the table, not a figure.
- p15 fragment-of-other bbox [188.52, 674.04, 359.76, 783.96] The arrangement thumbnail printed in the Regular octagon, pattern 1 cell of Table 4 - a raster inside the table, counted with the table, not a figure.
- p15 fragment-of-other bbox [373.44, 674.16, 532.68, 783.0] The arrangement thumbnail printed in the Regular octagon, pattern 2 cell of Table 4 - a raster inside the table, counted with the table, not a figure.
- p16 fragment-of-other bbox [190.68, 121.32, 367.68, 209.04] The arrangement thumbnail printed in the Circle, pattern 1 cell of Table 5 - a raster inside the table, counted with the table, not a figure.
- p16 fragment-of-other bbox [413.28, 123.24, 497.88, 207.84] The arrangement thumbnail printed in the Circle, pattern 2 cell of Table 5 - a raster inside the table, counted with the table, not a figure.
- p20 background bbox [34.56, 50.64, 560.16, 756.24] The page-filling vector panel of the first advertising sheet - the printed border and gold banner that carry the folio and the display title. A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 background bbox [19.8, 28.2, 574.2, 762.6] The page-filling vector frame of the second advertising sheet, carrying the running head 'THE ULTIMATE BROWNIE PAN | TEAM # 23004 | PAGE 20 OF 20'. A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [21.0, 27.84, 575.52, 287.28] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [20.64, 29.16, 574.2, 286.08] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [33.48, 85.8, 558.96, 172.2] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [33.48, 173.16, 558.96, 212.64] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [19.92, 225.24, 258.48, 400.08] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [159.04, 254.25, 404.76, 457.82] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [390.0, 283.68, 575.16, 315.96] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [385.0, 287.0, 573.0, 764.0] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [404.52, 324.84, 544.92, 414.36] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [383.16, 402.84, 575.28, 709.68] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [27.48, 432.84, 366.48, 492.84] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [27.48, 471.36, 362.64, 620.52] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [398.52, 628.2, 568.8, 760.68] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [263.28, 655.56, 377.76, 762.72] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [143.16, 655.92, 260.28, 772.44] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [38.16, 656.16, 139.08, 765.6] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p20 not-an-exhibit bbox [397.44, 691.44, 583.92, 763.44] A text band or a picture of the first advertising sheet ('The Ultimate Brownie Pan', the picnic photograph, the 'How it works' column, the 'Why?' panel with its two recoloured heat fields). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [22.44, 78.6, 567.12, 108.6] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [285.48, 114.6, 557.52, 186.6] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [22.44, 121.56, 274.44, 268.32] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [266.64, 186.6, 567.96, 211.8] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [270.96, 213.24, 567.96, 341.76] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [25.8, 273.24, 264.84, 423.36] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [268.44, 350.4, 565.68, 375.6] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [270.96, 377.76, 572.64, 453.12] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [25.8, 447.24, 323.16, 472.44] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [330.96, 455.76, 569.76, 593.76] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [26.76, 473.76, 305.28, 582.12] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [25.8, 588.6, 323.16, 613.8] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [315.48, 611.76, 567.0, 754.32] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [24.96, 673.44, 322.32, 698.64] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.
- p21 not-an-exhibit bbox [28.44, 698.28, 325.44, 753.0] A text band or a product rendering of the second advertising sheet ('Pick From Four Choices or Customize Your Own': rectangular, hexagon, octagon and circle pan renderings with sales copy). A region of the advertising sheets the paper announces on p19 ('See advertising Sheets on Next Two Pages') - the team's own brochure, printed live over its artwork, with no figure number, no table number and no caption line anywhere on the page.

## distillation fields

figure 1 p4: sec=未编号标题 Introduction > 未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=top order=1/1 area=0.084 solo=False
  family=composite-panel panels=2 layout=1x2 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p4: sec=未编号标题 Introduction > 未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=middle order=2/2 area=0.081 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p5: sec=未编号标题 Introduction > 未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=bottom order=3/1 area=0.145 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=True 3d=surface-mesh printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p6: sec=未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=top order=4/1 area=0.196 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p6: sec=未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=middle order=5/2 area=0.208 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=True 3d=surface-mesh printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p7: sec=未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=top order=6/1 area=0.164 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p8: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=top order=8/1 area=0.155 solo=False
  family=scatter panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=5 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p9: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=top order=9/1 area=0.136 solo=False
  family=other panels=5 layout=5 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p10: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=middle order=10/1 area=0.074 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p10: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=bottom order=11/2 area=0.09 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p11: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=middle order=12/1 area=0.029 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p11: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=middle order=13/2 area=0.015 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p12: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=top order=14/1 area=0.058 solo=False
  family=other panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p12: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=middle order=15/2 area=0.026 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p12: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=bottom order=16/3 area=0.045 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p13: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=bottom order=17/1 area=0.101 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p14: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=middle order=18/1 area=0.098 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p14: sec=未编号标题 Model 2: Baking Pan Optimization Design Model [model] zone=bottom order=19/2 area=0.292 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 19 p15: sec=未编号标题 Model test [test] zone=top order=20/1 area=0.094 solo=False
  family=photo-or-raster-image panels=3 layout=1x3 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 20 p16: sec=未编号标题 Model test [test] zone=middle order=23/2 area=0.105 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 21 p17: sec=未编号标题 Model test [test] zone=top order=24/1 area=0.136 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 22 p17: sec=未编号标题 Model test [test] zone=bottom order=25/2 area=0.141 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 23 p19: sec=未编号标题 Strengths and Weaknesses [evaluation] zone=top order=26/1 area=0.199 solo=False
  family=composite-panel panels=3 layout=1x3 shared=False legend=none cbar=True 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Fig. N words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p7: sec=未编号标题 Model 1: The Distribution of Heat at the Edges of Polygon [model] zone=bottom order=7/2 area=0.154 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 10x5 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=4 txt=1 width=full orient=portrait cont=False

table 2 p15: sec=未编号标题 Model test [test] zone=bottom order=21/2 area=0.275 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 4x3 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=3 width=full orient=portrait cont=False

table 3 p16: sec=未编号标题 Model test [test] zone=top order=22/1 area=0.103 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 2x3 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=3 width=full orient=portrait cont=False

