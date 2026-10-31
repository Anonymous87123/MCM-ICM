# P-B-2012-15417-df1dd905 — figure census

- layout sha `0fa7f3db9e340b5e`, 26 pages, 12 measured regions
- accounted: 4 figures, 0 tables, 8 excluded, 0 unaccounted
- families: flowchart-or-schematic 2, line 1, scatter 1

1. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [89.09, 314.13, 288.91, 530.13] (raster)
   cap: Figure 1: Case 4: Boat D cannot find a site to land.
   note: Case 4 drawn out: boat D sits in site 4 on day k with priority 4 and next desired site 6, site 6 is already held by boat A on day k + 1, and the stray glyph to the right of the grid is D locked out of the row. A raster image of a three-column grid headed 'Site', 'Day k' and 'Day k + 1' over the six site rows; each filled cell holds a shaded raft glyph and two printed lines, 'Priority: n' and 'Next desired site: n'. No axes, no scale, no legend: the grid is the drawing.
2. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [347.45, 314.43, 502.98, 530.13] (raster)
   cap: Figure 2: Resolution of Case 4: Boat A is forced to move back, even though it has higher priority.
   note: The resolution of case 4 on the same grid: boat A (priority 1) is forced back from site 6 to site 3 on day k + 1 while D takes site 4, so a higher-priority boat yields to keep the schedule legal. A raster image of a three-column grid headed 'Site', 'Day k' and 'Day k + 1' over the six site rows; each filled cell holds a shaded raft glyph and two printed lines, 'Priority: n' and 'Next desired site: n'. No axes, no scale, no legend: the grid is the drawing.
3. p11 **scatter** conf=high panels=1
   bbox [186.16, 381.24, 425.84, 525.24] (raster)
   cap: Figure 3: Graph of Magic Numbers
   note: Rescheduling against campsite count: blue diamond markers only, no line, over light grey gridlines; two isolated points sit far above the rest near Y = 34-35 (30 and 39 rescheduled trips) and the remainder breaks into two low runs split at about Y = 42, which is the period-7 pattern the section names. Axis titles 'Number of rescheduled trips' 0-45 and 'Number of Site (Y)' 28-56. No legend.
4. p13 **line** conf=high panels=1
   bbox [171.99, 72.0, 440.01, 252.0] (raster)
   cap: Figure 4: The ratio changes, and efficiency increases more trips (because 44 is a magic number for 12 hours too) but, not enough to warrant the extra stress for the rowers and motors.
   note: Trips per year against the motor:oar ratio: blue diamond markers with a smooth fitted quadratic drawn through them and the fit printed inside the frame, 'y = -26.173x^2+66.222x+617.96', 'R^2 = 0.9968'. Axis titles 'Number of Trips per Year' 610-665 and 'Ratio of Motor boats to Oar boats' 0-1.2, gridlines on both directions, no legend. The caption line runs into the paper's own prose and is quoted up to the sentence break.

## excluded
- p5 not-an-exhibit bbox [68.61, 230.86, 543.39, 720.42] typeset Java listing under a printed 'Algorithm generateSchedule().' title bar, 127 vector paths of code text and no drawing.
- p7 not-an-exhibit bbox [68.61, 76.38, 543.39, 183.38] the tail of the same listing, lines 143-155 with their comments, above the prose that explains addBoats().
- p9 not-an-exhibit bbox [68.61, 301.95, 543.39, 715.2] typeset Java listing of addBoats(int day), 112 vector paths of code text.
- p10 not-an-exhibit bbox [68.61, 261.24, 543.39, 419.45] typeset Java listing of reschedule(Boat boat), 48 vector paths of code, quoted in the prose as the 'LinkedList implementation of reschedule()'.
- p17 not-an-exhibit bbox [68.61, 119.18, 543.39, 720.33] the appendix listing Boat.java, a full page of code text under the printed line 'Appendix: Source Code'.
- p19 not-an-exhibit bbox [68.61, 76.38, 543.39, 510.16] the tail of the appendix Boat.java listing, cut by the page footer, with the 'River.java' title line of the next listing printed under it.
- p19 not-an-exhibit bbox [68.61, 551.63, 543.39, 722.39] the opening lines of the appendix River.java listing (imports and class comment), 47 vector paths of code text.
- p26 not-an-exhibit bbox [68.61, 76.38, 543.39, 366.69] the tail of the driver listing that closes the appendix, indented one space and without its own title bar.

## distillation fields

figure 1 p8: sec=未编号标题 Representation of a Schedule [other] zone=middle order=3/1 area=0.089 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p8: sec=未编号标题 Representation of a Schedule [other] zone=middle order=4/2 area=0.069 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=19 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p11: sec=未编号标题 Magic Numbers [other] zone=middle order=7/1 area=0.071 solo=False
  family=scatter panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p13: sec=未编号标题 Error/Sensitivity Analysis [sensitivity] zone=top order=8/1 area=0.1 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=13 lead=0 count=1 read=1 gap=None pattern=parenthetical style=['Figure 4']
  caption: Figure N: words=33 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

