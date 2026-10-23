# P-A-2014-25142-c5c79dc7 — figure census

- layout sha `2e4eba1193be7d94`, 34 pages, 29 measured regions
- accounted: 18 figures, 1 tables, 10 excluded, 0 unaccounted
- families: bar 9, line 8, other 1, table-grid 1

1. p11 **line** conf=high panels=1
   bbox [127.56, 376.91, 467.72, 610.45] (raster)
   cap: Figure 1: Relationship between safe-gap and velocity
   note: Two analytic curves on one frame, safe gap against velocity: Gs rising from 10 at rest on the 0.7-friction line, and the second curve for the lane-changing case (Gs = 10 + 3.4V) above it, with a dashed vertical guide drawn at the 200 km/h normal-driving ceiling and the region beyond it left as extrapolation. No legend, no gridlines, no in-plot title; the two labels V and Gs sit beside the curves themselves.
2. p12 **other** conf=high panels=1
   bbox [240.95, 121.81, 354.33, 278.81] (raster)
   cap: Figure 2: Velocity Analysis when facing emergency.
   note: A labelled velocity triangle rather than a plot: three vectors drawn head-to-tail for the overtaking vehicle, V1 along the lane, V0 before the lane change and the difference a off it, with the component ap parallel to the lane marked and the angle at which the vehicle crosses called out. No axes, no ticks, no scale, no gridlines and no legend [geometry.family].
3. p15 **line** conf=high panels=1
   bbox [155.91, 503.11, 439.37, 702.42] (raster)
   cap: Figure 3: Tempo-Spatial Distribution of Vehicles
   note: The cellular-automaton output as a tempo-spatial diagram: red trajectories for smaller cars and green for larger vehicles, each vehicle's position over time traced as a sloping line, x axis 'Time(s)' 0 to 1000 and y axis 'Distance' 0 to 1000, every third column marking one time cycle. No legend box - the colour key is in the prose paragraph above the caption, which states that red is a smaller car and green a larger one [geometry.legend]. The caption line that prints directly above the numbered one ('Figure spatiotemporal diagram of vehicles, expectation of inflow rate is 0.5 veh/s, the ratio of smaller cars to larger vehicles is 1, three-lane') carries no figure number and is part of the body text, so only the numbered line is quoted as the caption.
4. p16 **line** conf=high panels=1
   bbox [302.67, 286.08, 501.1, 425.6] (raster)
   cap: Figure 4: Average Velocity under Different
   note: Average velocity against inflow rate for the two-lane freeway, one line per rule, x axis 'E(veh/s)' and y axis 'V(m/s)', legend boxed inside the upper left ['V(m/s)' versus 'E(veh/s)']. This is the left-hand chart of the pair; the tail of its caption, printed on the following text line, reads 'Rules(2 lanes)' and belongs to this row [caption.verbatim].
5. p16 **line** conf=high panels=1
   bbox [94.18, 286.08, 292.6, 425.6] (raster)
   cap: Figure 5: Average Velocity under Different
   note: The same velocity-versus-inflow plot for the three-lane freeway, same axis titles, same boxed legend inside the upper left. Right-hand chart of the pair; the caption tail on the next text line reads 'Rules(3 lanes )' and belongs here. The two charts share a frame style but not a y scale, so the scale is read per region [geometry.shared_axes].
6. p17 **line** conf=high panels=1
   bbox [127.56, 276.55, 467.73, 515.73] (raster)
   cap: Figure 6: Average Velocity of Fast cars
   note: Average velocity of the faster cars against inflow rate in the three-lane model, one line per rule, legend boxed inside the upper left, x 'E(veh/s)' and y 'V(m/s)'. The curve dips at low inflow and then climbs through the 0-0.5 veh/s range, which is the overtaking-desire effect the prose describes.
7. p18 **bar** conf=high panels=1
   bbox [302.67, 236.54, 501.1, 376.06] (raster)
   cap: Figure 7: Density of Traffic in Each Lanes(2
   note: Per-lane traffic density on the two-lane freeway under keep-right: vertical columns grouped by inflow rate, two series ('left lane' black, 'right lane' red) with a boxed legend inside the upper left, x 'E(veh/s)' on the tick set 0.1, 0.3, 0.5, 0.7, 1.0, 1.4, 1.8, 2.5, 3.0 and y 'D (veh/m)' labelled 0.00 to 0.08 by 0.02 up to an axis top near 0.10. No gridlines, no in-plot title. Left-hand chart of the first pair; the caption tail on the next line reads 'lanes, keep-right)' [caption.verbatim].
8. p18 **bar** conf=high panels=1
   bbox [94.18, 236.54, 292.6, 376.06] (raster)
   cap: Figure 8: Density of Traffic in Each Lanes(2
   note: The same grouped column construction for the two-lane unrestricted case, same axis titles and the same nine x ticks and the same inside-upper-left legend, but this chart labels every 0.01 tick up to 0.10 where its neighbour labels 0.02 steps, so the two panels of the pair are not interchangeable. Right-hand chart of the first pair; caption tail 'lanes, unrestricted)'.
9. p18 **bar** conf=high panels=1
   bbox [94.18, 432.18, 292.6, 568.59] (raster)
   cap: Figure 9: Density of Traffic in Each Lanes(3
   note: Density per lane on the three-lane freeway under keep-right: three series ('left lane' black, 'middle lane' red, 'right lane' blue) with the boxed legend inside the upper left, y 'D (veh/m)' 0.000 to 0.095 in 0.005 steps and the same nine x ticks. This is the panel that shows the unbalanced load the prose reports, the keep-right column in the right lane running far above the other two. Left-hand chart of the second pair; caption tail 'lanes, keep-right)'. The top edge of the crop carries a stray mark from the caption line above it, not chart content.
10. p18 **bar** conf=high panels=1
   bbox [302.67, 429.08, 501.1, 568.59] (raster)
   cap: Figure 10: Density of Traffic in Each Lanes(3
   note: Density per lane on the three-lane freeway under the unrestricted rule, three series, legend inside the upper left, y 'D (veh/m)' 0.00 to 0.07 by 0.01 - a narrower range than its left-hand neighbour. Right-hand chart of the second pair; caption tail 'lanes, unrestricted)'.
11. p19 **bar** conf=high panels=1
   bbox [127.56, 196.77, 467.73, 435.57] (raster)
   cap: Figure 11: Passing Events With Different Rules(3 lanes, 300s)
   note: Passing events counted over five simulated minutes: stacked vertical columns, one column per inflow rate, three series stacked bottom to top in yellow, red and blue ('unrestricted(left)', 'unrestricted(right)', 'keep-right'), with a single horizontal legend row inside the upper left of the frame. x 'E(veh/s)' on the tick set 0.1, 0.3, 0.5, 0.7, 1.0, 1.4, 1.8, 2.5, 3.0, 3.6; the y axis carries no title at all, only ticks 0 to 25000 by 5000, and there are no gridlines. The only stacked column chart on the paper.
12. p20 **bar** conf=high panels=1
   bbox [94.18, 123.95, 292.61, 261.33] (raster)
   cap: Figure 12: Danger Index under Differen-
   note: Danger index on the two-lane freeway: grouped columns, two series ('unstrict' black, 'keep-right' red) with the boxed legend inside the upper RIGHT - the only panel in this group that puts it there - over y 'Danger Index' 0 to 700 by 100 and x 'E(veh/s)'. No gridlines, no title. Left-hand chart of the first pair; the caption is broken mid-word in both columns and the tail printed on the next line reads 't Rules(2 lanes)' [caption.verbatim].
13. p20 **bar** conf=high panels=1
   bbox [302.67, 121.81, 501.1, 261.33] (raster)
   cap: Figure 13: Danger Index under Differen-
   note: The same danger-index comparison for three lanes, two series, legend inside the upper left, y 'Danger Index' 0 to about 900 in 200 steps and the same x tick set. Right-hand chart of the first pair; caption tail 't Rules(3 lanes)'.
14. p20 **line** conf=high panels=1
   bbox [94.18, 518.24, 292.6, 657.75] (raster)
   cap: Figure 14: Average Velocity under Different
   note: Average velocity under three upper speed limits on the keep-right three-lane freeway: polylines, legend inside the upper right naming 'Speed limits 29m/s' (black squares), '32m/s' (red circles) and '38m/s' (blue triangles), y 'V(m/s)' 10 to 32 by 2 and x 'E(veh/s)' 0.0 to 4.0 by 0.5. The printed legend says 29m/s where the prose says the limits were changed from 32 to 28 and 36, so the panel's own key contradicts the sentence. Left-hand chart of the second pair; caption tail 'Speed Limits(3 lanes, keep-right)'.
15. p20 **line** conf=high panels=1
   bbox [302.67, 518.24, 501.1, 657.75] (raster)
   cap: Figure 15: Average Velocity under Different
   note: The same velocity-versus-inflow plot under the unrestricted rule, legend inside the upper right naming 28m/s, 32m/s and 36m/s, y 'V(m/s)' 8 to 30 by 2, x 0.0 to 4.0 by 0.5. This is the panel whose key matches the prose. Right-hand chart of the second pair; its caption tail prints as 'Speed Limits(3 lanes, unrestricted' with the closing parenthesis missing from the text layer, so the quote stops at the fragment carrying the number.
16. p21 **bar** conf=high panels=1
   bbox [94.18, 121.81, 292.6, 261.33] (raster)
   cap: Figure 16: Danger Index under Differen-
   note: Danger index under the three speed limits, keep-right three-lane freeway: grouped columns, three series keyed inside the upper left as 'Speed limits 28m/s', '32m/s' and '36m/s', y 'Danger Index' 0 to 700 by 100, x 'E(veh/s)'. No gridlines. Left-hand chart of the pair; the caption breaks mid-word and the tail on the next line reads 't Speed Limits(3 lanes, keep-right)'.
17. p21 **bar** conf=high panels=1
   bbox [302.67, 121.81, 501.1, 261.33] (raster)
   cap: Figure 17: Danger Index under Differen-
   note: The same three-limit danger-index comparison under the unrestricted rule, three series, legend inside the upper left, but on a y axis that runs 0 to 1000 by 100 instead of 0 to 700 - the wider range is the only difference in the frame. Right-hand chart of the pair; caption tail 't Speed Limits(3 lanes, unrestricted)'.
18. p24 **line** conf=high panels=1
   bbox [127.56, 121.81, 467.73, 360.99] (raster)
   cap: Figure 18: Average Velocity under Different Rules in an Intelligent System
   note: Average velocity under the new intelligent-system rule against inflow rate, lines keyed by rule with the legend inside the frame, x 'E(veh/s)' and y 'V(m/s)'. The caption is the only one in the paper that names a whole drawing in words rather than a comparison, and it prints on one line with no tail.

## tables
1. p5 table-grid bbox [87.94, 142.14, 511.49, 428.94]
   cap: Table 1: Notation

## excluded
- p27 not-an-exhibit bbox [87.94, 391.6, 507.33, 427.57] A typed MATLAB listing band under the heading 'Simulating different inflow rates function:' - the driver, savefile and speedmax assignments. Code, not an exhibit: no number, no caption.
- p29 not-an-exhibit bbox [87.94, 102.09, 507.33, 130.58] A second typed listing band, the lane/xdistance explanation block (v=road1(lane,xdistance,1)). Code, not an exhibit.
- p30 not-an-exhibit bbox [87.94, 499.2, 507.33, 535.16] The 'Inflow:' listing band: the poissrnd call and the road re-initialisation. Code, not an exhibit.
- p31 not-an-exhibit bbox [87.94, 236.18, 507.33, 272.15] The 'Acceleration:' listing band. Code, not an exhibit.
- p31 not-an-exhibit bbox [87.94, 421.99, 507.33, 457.95] The 'Deceleration:' listing band. Code, not an exhibit.
- p31 not-an-exhibit bbox [87.94, 607.79, 507.33, 643.76] The 'Deal with urgent deceleration:' listing band. Code, not an exhibit.
- p32 not-an-exhibit bbox [87.94, 248.14, 507.33, 283.36] The 'Judge whether to overtake:' listing band. Code, not an exhibit.
- p32 not-an-exhibit bbox [87.94, 612.52, 507.33, 647.74] The 'Free-driving style:' listing band, carrying the A and B probability matrices as typed source text. Code, not an exhibit.
- p33 not-an-exhibit bbox [87.94, 415.51, 507.33, 449.54] The 'Count the traffic flow:' listing band. Code, not an exhibit.
- p34 not-an-exhibit bbox [87.94, 102.09, 507.33, 418.5] The largest listing band of the appendix, the body of the function [Xd,density]= Xdensity(...) with its summary comment. Code, not an exhibit: it is six vector paths of monospaced source text and carries no number and no caption.

## distillation fields

figure 1 p11: sec=2.4.3 Danger Index [other] zone=middle order=2/1 area=0.159 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p12: sec=2.4.3 Danger Index [other] zone=top order=3/1 area=0.036 solo=False
  family=other panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=12 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['figure 2']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p15: sec=4 Model Implementation with Computer [model] zone=bottom order=4/1 area=0.113 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p16: sec=5 Data Analysis and Model Validation > 5.1 Average Velocity [test] zone=middle order=5/1 area=0.055 solo=False
  family=line panels=1 layout=left of pair shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=2 read=1 gap=None pattern=as-shown-in style=['figure 4']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p16: sec=5 Data Analysis and Model Validation > 5.1 Average Velocity [test] zone=middle order=6/2 area=0.055 solo=False
  family=line panels=1 layout=right of pair shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=2 read=1 gap=None pattern=as-shown-in style=['figure 5', 'figure 4 and 5']
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p17: sec=5 Data Analysis and Model Validation > 5.2 Average Velocity of Fast Cars [test] zone=middle order=7/1 area=0.162 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p18: sec=5 Data Analysis and Model Validation > 5.3 Density [test] zone=middle order=8/1 area=0.055 solo=False
  family=bar panels=1 layout=left of row 1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p18: sec=5 Data Analysis and Model Validation > 5.3 Density [test] zone=middle order=9/2 area=0.055 solo=False
  family=bar panels=1 layout=right of row 1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p18: sec=5 Data Analysis and Model Validation > 5.3 Density [test] zone=middle order=10/3 area=0.054 solo=False
  family=bar panels=1 layout=left of row 2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p18: sec=5 Data Analysis and Model Validation > 5.3 Density [test] zone=middle order=11/4 area=0.055 solo=False
  family=bar panels=1 layout=right of row 2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p19: sec=5 Data Analysis and Model Validation > 5.4 Overtaking Rate [test] zone=middle order=12/1 area=0.162 solo=False
  family=bar panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 12 p20: sec=5 Data Analysis and Model Validation > 5.5 Danger Index [test] zone=top order=13/1 area=0.054 solo=False
  family=bar panels=1 layout=left of row 1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 13 p20: sec=5 Data Analysis and Model Validation > 5.5 Danger Index [test] zone=top order=14/2 area=0.055 solo=False
  family=bar panels=1 layout=right of row 1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 14 p20: sec=6 Sensitivity Evaluation of the Model under Differ- [evaluation] zone=bottom order=15/3 area=0.055 solo=False
  family=line panels=1 layout=left of row 2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p20: sec=6 Sensitivity Evaluation of the Model under Differ- [evaluation] zone=bottom order=16/4 area=0.055 solo=False
  family=line panels=1 layout=right of row 2 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p21: sec=6 Sensitivity Evaluation of the Model under Differ- [evaluation] zone=top order=17/1 area=0.055 solo=False
  family=bar panels=1 layout=left of pair shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 17 p21: sec=6 Sensitivity Evaluation of the Model under Differ- [evaluation] zone=top order=18/2 area=0.055 solo=False
  family=bar panels=1 layout=right of pair shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p24: sec=8 Transportation under Intelligent System > 8.3 Result of Intelligent System [result] zone=top order=19/1 area=0.162 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p5: sec=1.1 Terminology [symbols] zone=top order=1/1 area=0.242 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Table N: words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 19x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

