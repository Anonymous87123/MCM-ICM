# P-C-2016-42939-5fccbebc — figure census

- layout sha `803560792a4e36e1`, 25 pages, 14 measured regions
- accounted: 11 figures, 2 tables, 1 excluded, 0 unaccounted
- families: flowchart-or-schematic 1, line 4, map-or-plan-view 1, scatter 4, table-as-figure 1, table-grid 2

1. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [97.97, 70.86, 494.83, 778.51] (raster)
   cap: Figure 1: Flow Chart Demonstration of the Model
   note: A tall box-and-arrow pipeline, one page high and one column wide, drawn in a presentation tool: blue rounded 'Start', a filled rectangle 'addressing missing data', a decision diamond 'How is the data related to students' performance?', two branches into 'choosing performance contributing variables and determining their coefficients' and 'determining performance index', a second diamond 'Does donation amount affect the data directly?' with a 'No' arm to an oval 'Drop' and a 'Yes' arm into 'determining investment strategy', a long feedback line up the left margin labelled 'Donation amount', an 'Accounting for time duration and geographical distribution' box, and a right-hand column of four boxes from 'Fitting the relation between performance contributing variables and donation amount' to 'Maximizing ROI and determining investment strategy'. Arrow labels carry the data names - 'All data', 'Addressed data', 'Performance indicators', 'Performance index', 'Potential performance contributing variables', 'Final results For year 1', 'Final results For year 2-5'. NO AXES, no number and no value anywhere on it. TWO FEEDBACK PATHS CROSS THE FLOW WITHOUT A JUNCTION MARK: the left-margin 'Donation amount' line runs the height of the page through the same channel as the downward arrows, and the bracket from the right-hand column re-enters 'determining investment strategy' from below, so which arrow feeds which box at the crossings can only be guessed. The 'Final results' arrows converge on a single 'Finish' oval. Caption below; cited by the sentence that ends section 1.2, 'The flow chart of the whole model is presented below in Fig 1:'.
2. p9 **table-as-figure** conf=high panels=1
   bbox [99.21, 130.58, 496.06, 711.62] (raster)
   cap: 
   note: The definitions table, printed as an EMBEDDED IMAGE rather than as type: the page carries only its heading '1.3 Detailed Definitions & Assumptions' and the sub-heading '1.3.1 Detailed Definitions:', and everything under them is a bitmap, so the whole table has no text layer and no selectable cell. Three columns - a Name column, a Definition column of full sentences and a Denotation column of mathematics - over a header row and ten body rows, from 'Donation amount' (X_j) through 'ROI of the performance index (also referred as ROI for simplicity)' (ROI_j), every row ruled on all four sides in the same full grid as Table 1. NO CAPTION AND NO NUMBER: it is the only table in the paper that is never numbered, and the one that actually carries the paper's notation. The definition text is justified inside its column, which opens wide word gaps in two cells, and the denotation of 'Performance index' is a bare Greek upsilon with no subscript while its neighbours all carry one. Because it is an image, no figure or table extractor reads a cell of it, and the paper's own notation is therefore invisible to any downstream search.
3. p13 **line** conf=high panels=1
   bbox [83.79, 357.57, 509.0, 513.13] (raster)
   cap: Figure 2: LASSO path-coefficients as a function of shrinkage factor s
   note: A LASSO coefficient-path plot: about ten thin polylines, most of them dashed, radiating from the left origin against 'Shrinkage Factor s' graduated 0.0 to 1.0, on a 'Standardized Coefficients' ordinate running minus 200 to 200. Two paths rise to about plus 210 and plus 150, four fall to minus 100, minus 130, minus 160 and minus 190, and a cluster of small blue dots sits near the origin between s = 0.45 and 0.65. A SECOND, UNLABELLED AXIS RUNS ALONG THE TOP with twelve thin vertical rules and the tick numbers 0 1 2 3 4 5 7 9 12 13 15 20 at irregular spacing - the non-zero count implied by each shrinkage, never named as such, with no unit and no label. The six variable names are printed OUTSIDE the frame at the right margin, each tied to a black square marker on the frame edge by a short rule: Tuition&Fee2010, Carnegie_HighResearchActivity, Carnegie_PublicRural, StudentToFaculty_ratio, PPTUG_EF, PCTPELL. There is no legend, no title, no gridline and no marker for the shrinkage factor the paper selects; the six labels crowd each other around the zero line. Caption below. Cited on the NEXT page ('Fig 2. displays the results of LASSO procedure') and again as 'find in Fig 2 that 6 variables have nonzero coefficients' - the figure prints before the sentence that reads it.
4. p13 **line** conf=high panels=1
   bbox [83.79, 549.27, 509.0, 733.47] (raster)
   cap: Figure 3: Cross-validated MSE
   note: The cross-validation panel of the same LASSO run: about thirty open markers with vertical error bars and NO CONNECTING LINE, one tall bar at s near 0.02 reaching 135, a steep descent through 55, 35 and 25 by s near 0.05, then a flat run at about 40 out to s = 1.0, against 'Cross-Validated MSE' graduated 40 to 140 and 'Shrinkage Factor s' graduated 0.0 to 1.0. No gridline, no title, no legend and NO MARKER AT THE CHOSEN SHRINKAGE: the prose says 'the cross-validated MSE reaches minimum with shrinkage factor between 0.4-0.8. We choose 0.6', but the plotted trace is FLAT AT ABOUT 40 FROM 0.1 TO 1.0, so the flat region the sentence describes as a minimum between 0.4 and 0.8 is indistinguishable from every other s past 0.1, and the choice of 0.6 cannot be read off the exhibit at all. The leftmost bars are compressed into a few pixels, so their error extents are unreadable. Caption below; cited by the same next-page sentence as Figure 2.
5. p15 **scatter** conf=high panels=1
   bbox [70.87, 346.11, 524.42, 640.35] (raster)
   cap: Figure 4: GAM Approximation
   note: A dense point cloud - thousands of small black diamond markers on a pale grey panel - with a single blue GAM curve over it and a grey confidence ribbon following the curve: the fitted PCTPELL against 'Donation' on an abscissa graduated 0e+00, 3e+08, 6e+08, 9e+08, and an ordinate graduated 0.25, 0.50, 0.75, 1.00 whose 'PCTPELL' label is printed ONE LETTER PER LINE down the left margin. The in-frame title is 'GAM estimation of PCTPELL vs Donation'. No legend, no data label and no printed value; the curve starts near 0.37 at zero donation, dips to about 0.23 near 5e8 and recovers to about 0.26. THE POINTS ARE NOT READABLE AS A DISTRIBUTION: the overplotting is total near zero donation, where most institutions sit, so the cloud is a solid black mass across the first third of the abscissa and the shape the fit is drawn through cannot be checked by eye. The caption 'Figure 4: GAM Approximation' prints below, and the citing sentence adds '(see the other two fitted curves in Appendix)' - which is where Figures 9 and 10 are, on the last page.
6. p16 **scatter** conf=high panels=1
   bbox [70.87, 197.69, 524.42, 491.92] (raster)
   cap: Figure 5: Demonstration of f ROI1
   note: THE SAME PICTURE AS FIGURE 4 - the same diamond cloud, the same blue GAM curve, the same ribbon, the same axes 0e+00 to 9e+08 and 0.25 to 1.00, the same title 'GAM estimation of PCTPELL vs Donation', the same one-character-per-line 'PCTPELL' margin label - with THREE ANNOTATIONS ADDED OVER IT: an orange segment marking a local bump on the curve with the label delta-h, an orange vertical tick, and a green bracket carrying the labels delta-x and delta-f together with a caret over the bump. The caption 'Figure 5: Demonstration of f ROI1' and the prose that follows it define fitted ROI as delta-f over delta-x, so the exhibit is a definition drawn on a plot the paper has already printed: the second printing exists to carry three glyphs, and it carries no caption text that says so. NO SENTENCE NAMES FIGURE 5 - the definition it illustrates is written in the body text, and the only pointer to any exhibit in the section is the 'Fig 4' sentence on the previous page. The added labels are set small and in low contrast, so at print size the distinction the figure exists to make is the least legible thing on it.
7. p17 **line** conf=high panels=1
   bbox [126.31, 552.35, 466.48, 704.22] (raster)
   cap: Figure 6: Function from Deviation to Pi
   note: A single smooth curve on a fine grey grid, drawn by a mathematics package rather than a statistics one: roughly sinusoidal, dipping to about 0.35 near x = minus 1.3 and peaking at about 1.6 near x = 0.9, with axes through the origin and ticks minus 3 to 3 in halves on the abscissa and 2, 1, minus 1, minus 2 on the ordinate. THE AXES ARE NOT NAMED ANYWHERE: the prose says 'deviation is on the x-axis while Pi is on the y-axis', and the reader is expected to carry that in from the paragraph. The ordinate labels are drawn to the RIGHT of the y axis, inside the plot area, rather than in the left margin. Two small red circular markers sit ON the x axis at 0 and at 1, unexplained by the prose, the caption or the curve. No legend, no title, no value printed anywhere; the caption 'Figure 6: Function from Deviation to Pi' prints below, and the exhibit is cited three times on its own page ('the function has the shape shown in Fig 6', 'The shape of the function is as shown in Fig 6', 'the function mapping deviation to Pi is similar to Fig 6') - more citations than any other exhibit in the paper, for a sketch the text itself calls an assumption.
8. p18 **line** conf=high panels=1
   bbox [126.31, 262.12, 466.47, 437.45] (raster)
   cap: Figure 7: Approximated Function from Deviation to Pi
   note: The piecewise-linear replacement for Figure 6: a dark-blue polyline through small red circular markers at seven breakpoints, zigzagging down, up and down again, on the same fine grid, with the same unnamed axes and the same right-side ordinate labels (2, 1, minus 1, minus 2) and abscissa ticks minus 1, minus 0.5, 0.5, 1.5. Red markers are also drawn ON the x axis at 0, 0.5 and 1.0 with one magenta marker at 1.5, which nothing explains. NO LEGEND, NO TITLE, NO AXIS NAMES and no value printed. The list of endpoints the prose supplies for this very polyline DISAGREES WITH ITSELF: it gives '(The minimum of deviations of all institutions, 2)', then halves, quarters and zero, then quarters and halves of the maximum with the value written '2/4' where its mirror image on the left is '4/3', and closes with '(The minimum of deviations of all institutions, 0)' where the maximum is obviously meant - so the two ends of the approximation are described by the same phrase, one value in the list is typed as an unreduced fraction of the wrong pair, and the curve drawn cannot be checked against the endpoints that define it. Caption below; cited by 'as is shown in Fig 7' on the same page.
9. p20 **map-or-plan-view** conf=high panels=1
   bbox [70.87, 70.87, 524.41, 304.16] (raster)
   cap: Figure 8: Geographical Distribution of Selected Institutions
   note: A screenshot of a mapping tool, not a chart: a light green and blue US base map with state outlines and state names set in grey capitals, city dots labelled Seattle, San Francisco, Las Vegas, Los Angeles, San Diego, Houston, New York, Chicago, Toronto and Ottawa, and FIFTEEN RED PINS with text callouts naming the selected institutions - University of Minnesota, The State University of..., United States Merchant..., Truman State University, Wabash Valley College, Virginia State Univers..., Illinois College, Institute of American..., East San Gabriel Valle..., Western Texas College, Marion Military Instit..., Louisiana State Univer..., New College of Florida, AVTEC. NO AXES, no graticule, no scale bar, no projection statement and no legend: the pins carry no magnitude, so the map shows WHERE the chosen institutions are and nothing about how much each receives - the amounts are in Table 4, which has no measured region. The callouts are TRUNCATED WITH ELLIPSES by their own tool, two of them collide ('SUNY at FredoniaBoston'), one white box near the top right obscures map content, and the Alaska inset and the north-east corner carry labels cut by the frame. The caption 'Figure 8: Geographical Distribution of Selected Institutions' prints below; cited only by the joint sentence 'the results for year 1 and geographical distribution of selected institutions are presented below in Table 4 and Fig 8'.
10. p25 **scatter** conf=high panels=1
   bbox [97.97, 110.22, 494.82, 367.67] (raster)
   cap: Figure 9: GAM Approximation of Share of Students Who Are Part-time vs Donation Amount
   note: The third GAM panel, on the appendix page: a diamond point cloud crowded at zero donation and sparse to the right, a blue curve falling from about 0.40 to a minimum near 0.03 between 5e8 and 6e8 and rising to about 0.08, a grey ribbon that WIDENS TO THE RIGHT AND DROPS BELOW ZERO at the frame edge, against 'Donation' 0e+00 to 9e+08 and an ordinate 0.00 to 1.00 labelled 'PPTUG_EF' vertically. In-frame title 'GAM estimation of PPTUG_EF vs Donation'. No legend, no value, no title beyond the in-frame one. The 'URL of the axis label sits in the same column as the tick numbers and the tick '0.50' collides with it, so the ordinate's own scale is damaged at its middle tick. The ribbon crossing below zero is a proportion that cannot be negative. The caption 'Figure 9: GAM Approximation of Share of Students Who Are Part-time vs Donation Amount' prints below; NO SENTENCE NAMES IT, and the only pointer to the appendix pair is the parenthesis '(see the other two fitted curves in Appendix)' attached to Figure 4, twelve pages earlier. The page carries the heading 'Appendix' and nothing else.
11. p25 **scatter** conf=high panels=1
   bbox [97.97, 419.16, 494.82, 676.61] (raster)
   cap: Figure 10: GAM Approximation of Student-to-faculty Ratio vs Donation Amount
   note: The fourth GAM panel, same template, same page: diamond points stacked in near-vertical bands at low donation and thinning rightward, two outliers high at about 59 and 38, a blue curve declining gently from about 21 to about 17.5, and a grey ribbon widening to span roughly 11 to 25 at the right edge, against the same 'Donation' axis 0e+00 to 9e+08 and an ordinate graduated 20, 40, 60 labelled 'Student/Faculty Ratio'. In-frame title 'GAM estimation of Student/Faculty Ratio vs Donation'. No legend, no value printed. THE FOUR PANELS OF THIS FAMILY ARE NOT DRAWN ON A COMMON SCALE: Figures 4, 5 and 9 use an ordinate of 0.00 to 1.00, this one 0 to 60, and all four share the same 'Donation' abscissa while the fitting relation is the thing compared - so the four fits cannot be laid against each other by eye, which is the only use a four-panel appendix has. The vertical banding of the points is an artefact of the integer variables being plotted against a continuous donation amount. Caption below; named by no sentence.

## tables
1. p7 table-grid bbox [157.96, 387.06, 437.31, 458.79]
   cap: Table 1: Data Source
2. p12 table-grid bbox [114.64, 256.17, 480.63, 419.55]
   cap: Table 2: The Top 10 Institutions in Terms of Performance Index

## excluded
- p4 background bbox [70.87, 70.86, 524.43, 273.39] The measured region on the title page renders as PURE WHITE: a raster of uniform 255 across the whole crop, with no ink, no box, no rule and no glyph. It sits above the title text 'An Optimal Strategy of Donation for Educational Purpose Control Number: #42939 February , 2016', so either an empty image was placed on the title page or the title block's image is white on white. Nothing can be counted in it, so it is excluded as background rather than recorded as an exhibit.

## distillation fields

figure 1 p8: sec=1 Introduction > 1.2 Baseline Model [model] zone=middle order=2/1 area=0.56 solo=True
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=7 lead=1 count=1 read=1 gap=None pattern=direct style=['Fig 1']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p9: sec=1.3 Detailed Definitions & Assumptions > 1.3.1 Detailed Definitions: [assumption] zone=middle order=3/1 area=0.46 solo=False
  family=table-as-figure panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: none words=0 sent=0 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p13: sec=4 Identifying Performance Contributing Variables via post-LASSO [model] zone=middle order=5/1 area=0.132 solo=False
  family=line panels=1 layout=1 shared=False legend=outside-right cbar=False 3d=no printed=False
  mention: first=14 lead=-1 count=2 read=1 gap=None pattern=direct style=['Fig 2']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p13: sec=4 Identifying Performance Contributing Variables via post-LASSO [model] zone=bottom order=6/2 area=0.156 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=-1 count=1 read=1 gap=None pattern=direct style=['Fig 3']
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p15: sec=5 Determining Investment Strategy based on ROI > 5.1 Fitted Curve between Performance Contributing Variables and Donation Amount [model] zone=middle order=7/1 area=0.266 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=15 lead=0 count=1 read=1 gap=None pattern=direct style=['Fig 4']
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p16: sec=5 Determining Investment Strategy based on ROI > 5.2.1 Model of Fitted ROIs of Performance Contributing Variables f ROIi [model] zone=middle order=8/2 area=0.266 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 7 p17: sec=5 Determining Investment Strategy based on ROI > 5.2.2 Model of the tuning parameter Pi [model] zone=bottom order=9/1 area=0.103 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=17 lead=0 count=3 read=1 gap=None pattern=direct style=['Fig 6']
  caption: Figure N: words=7 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 8 p18: sec=5 Determining Investment Strategy based on ROI > 5.2.3 Calculation of ROI [model] zone=middle order=10/1 area=0.119 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=18 lead=0 count=1 read=1 gap=None pattern=direct style=['Fig 7']
  caption: Figure N: words=8 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 9 p20: sec=5 Determining Investment Strategy based on ROI > 5.3 School Selection & Investment Strategy [solution] zone=top order=11/1 area=0.211 solo=False
  family=map-or-plan-view panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=19 lead=1 count=1 read=1 gap=None pattern=direct style=['Fig 8']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p25: sec=Appendix [appendix] zone=top order=12/1 area=0.204 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=14 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p25: sec=Appendix [appendix] zone=middle order=13/2 area=0.204 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p7: sec=1 Introduction > 1.2 Baseline Model [model] zone=middle order=1/1 area=0.04 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 4x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=half orient=portrait cont=False

table 2 p12: sec=3 Determining the Performance Index > 3.2 Performance Index via Principal-Component Factors [result] zone=middle order=4/1 area=0.119 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=12 lead=0 count=1 read=1 gap=None pattern=direct style=['Table 2']
  caption: Table N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 10x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=1 txt=1 width=full orient=portrait cont=False

