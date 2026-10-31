# P-B-2010-7273-e234c9a6 — figure census

- layout sha `a28e42fff88b486f`, 19 pages, 12 measured regions
- accounted: 12 figures, 0 tables, 0 excluded, 0 unaccounted
- families: flowchart-or-schematic 1, heatmap-or-contour 6, node-link-network 3, surface-or-3D 2

1. p8 **flowchart-or-schematic** conf=high panels=1
   bbox [197.62, 124.8, 413.63, 198.66] (?)
   cap: Figure 1: The unstable behavior of a naive best fit circle.
   note: three x marks on a circle, hollow arrow, then an arc through the same marks; drawn with no axes or frame
2. p9 **node-link-network** conf=high panels=1
   bbox [197.62, 124.8, 413.62, 276.4] (?)
   cap: Figure 2: A circle in the road metric induced by the graph for the Manchester Leeds area of England. The highway system graph is black and the circle is grey.
   note: black node-link highway graph inside a grey pixel-staircase ring: the road-metric circle is drawn as grid cells, not as a curve
3. p10 **heatmap-or-contour** conf=high panels=1
   bbox [197.62, 390.61, 413.63, 545.77] (?)
   cap: Figure 3: This shows the distance from Sutcliffe’s house under the road metric with an overlay of our graph representation of the nearby highway system. Sutcliffe’s house is at the house symbol. Red corresponds to a very short distance and dark blue corresponds to a long distance.
   note: coarse rainbow raster, red core, hollow house marker, black node-link overlay; framed, no axes, no colour bar
4. p11 **heatmap-or-contour** conf=high panels=1
   bbox [197.62, 238.78, 413.63, 392.99] (?)
   cap: Figure 4: This shows the estimated probability distribution for the 20th attack knowing the first 19. The dots represent the attacks and the ‘x’ denotes the actual location of the 20th attack. Red indicates the highest probability and purple the lowest.
   note: magenta-to-red raster with the attack dots and one x; the caption states the ramp direction (red high, purple low) instead of a bar
5. p12 **node-link-network** conf=high panels=1
   bbox [197.62, 124.8, 413.63, 279.02] (?)
   cap: Figure 5: The best fit circle of the attack locations under the road metric. The circle is shown in black, the graph is shown in grey, and the kill locations are shown in red.
   note: grey road graph, black pixel ring as the fitted circle, red dots for the kill sites; three layers keyed only in the caption
6. p12 **heatmap-or-contour** conf=high panels=1
   bbox [197.62, 346.77, 413.63, 502.05] (?)
   cap: Figure 6: The probability density estimated by Rossmo’s model for the perpe- trator’s residence. Red indicates the highest probability. The actual location of Sutcliffe’s house is shown with the house symbol.
   note: same ramp as Figure 4, house symbol at the true residence, attack dots over the density
7. p13 **surface-or-3D** conf=high panels=1
   bbox [197.62, 124.8, 413.62, 324.41] (?)
   cap: Figure 7: Rossmo’s probability estimate as a surface.
   note: filled blue surface in a bare wire box: one peak, no ticks, no colour bar, axes unlabelled
8. p14 **heatmap-or-contour** conf=high panels=1
   bbox [197.62, 124.8, 413.63, 276.41] (?)
   cap: Figure 8: The distance from Wayne Williams’ residence under the road metric.
   note: rainbow distance raster with the whole road network drawn over it as a black node-link layer
9. p14 **heatmap-or-contour** conf=high panels=1
   bbox [197.62, 322.18, 413.63, 472.86] (?)
   cap: Figure 9: This shows our computed probability distribution for the 22nd attack knowing the first 21. The actual location of the 22nd attack is shown as an ‘x’.
   note: lowest-quality raster of the set: the hot cells break into separate red and orange blocks rather than one lobe
10. p15 **node-link-network** conf=high panels=1
   bbox [197.62, 124.8, 413.62, 276.24] (?)
   cap: Figure 10: The best fit circle for the Atlanta child murders data.
   note: four layers at once: grey road graph, thick highlighted edges, black square cluster, red dots; heavier than Figure 5
11. p15 **heatmap-or-contour** conf=high panels=1
   bbox [197.62, 322.02, 413.63, 473.59] (?)
   cap: Figure 11: A colorized representation of the prediction made by Rossmo’s model for the location of the criminal’s residence with the locations of the crimes overlaid. Wayne Williams’ residence is represented by the house symbol.
   note: red block at the centre, crime dots, hollow house marker
12. p16 **surface-or-3D** conf=high panels=1
   bbox [197.62, 124.8, 413.63, 336.0] (?)
   cap: Figure 12: Rossmo’s probability estimate as a surface.
   note: same box as Figure 7 but flatter, with a small left ridge; the surface stops in ragged triangles where the data end

## distillation fields

figure 1 p8: sec=4 Best Fit Circle and Rossmo’s Model 7 > 4.3 Application to Rossmo’s Model [model] zone=top order=1/1 area=0.033 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=7 lead=1 count=1 read=1 gap=1 pattern=direct style=['Figure 1']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=True voice=none pos=below

figure 2 p9: sec=4 Best Fit Circle and Rossmo’s Model 7 > 4.3 Application to Rossmo’s Model [model] zone=top order=2/1 area=0.068 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=1 count=1 read=1 gap=0 pattern=direct style=['Figure 2']
  caption: Figure N: words=30 sent=2 units=False vars=0 cond=True concl=False voice=passive pos=below

figure 3 p10: sec=5 Case Studies > 5.1 Yorkshire Ripper > 5.1.1 Map and Metric [other] zone=middle order=3/1 area=0.069 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=10 lead=0 count=1 read=0 gap=0 pattern=figure-n-shows style=['Figure 3']
  caption: Figure N: words=49 sent=3 units=False vars=0 cond=True concl=False voice=active pos=below

figure 4 p11: sec=5 Case Studies > 5.1 Yorkshire Ripper > 5.1.4 Assessment of Results [evaluation] zone=middle order=4/1 area=0.069 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=0 count=1 read=0 gap=0 pattern=as-shown-in style=['Figure 4']
  caption: Figure N: words=41 sent=3 units=False vars=0 cond=True concl=False voice=active pos=below

figure 5 p12: sec=5 Case Studies > 5.1 Yorkshire Ripper > 5.1.4 Assessment of Results [evaluation] zone=top order=5/1 area=0.069 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Figure 5']
  caption: Figure N: words=34 sent=2 units=False vars=0 cond=False concl=False voice=passive pos=below

figure 6 p12: sec=5 Case Studies > 5.1 Yorkshire Ripper > 5.1.4 Assessment of Results [evaluation] zone=middle order=6/2 area=0.069 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Figure 6']
  caption: Figure N: words=34 sent=3 units=False vars=0 cond=False concl=False voice=passive pos=below

figure 7 p13: sec=5 Case Studies > 5.2 Atlanta Child Murders > 5.2.3 Application to Rossmo’s Method [model] zone=top order=7/1 area=0.089 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=False
  mention: first=11 lead=2 count=1 read=0 gap=2 pattern=as-shown-in style=['Figure 7']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p14: sec=5 Case Studies > 5.2 Atlanta Child Murders > 5.2.4 Assessment of Results [evaluation] zone=top order=8/1 area=0.068 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=1 count=1 read=0 gap=1 pattern=as-shown-in style=['Figure 8']
  caption: Figure N: words=12 sent=1 units=False vars=0 cond=True concl=False voice=none pos=below

figure 9 p14: sec=5 Case Studies > 5.2 Atlanta Child Murders > 5.2.4 Assessment of Results [evaluation] zone=middle order=9/2 area=0.067 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=1 count=1 read=0 gap=1 pattern=as-shown-in style=['figure 9']
  caption: Figure N: words=28 sent=2 units=False vars=0 cond=True concl=False voice=active pos=below

figure 10 p15: sec=5 Case Studies > 5.2 Atlanta Child Murders > 5.2.4 Assessment of Results [evaluation] zone=top order=10/1 area=0.067 solo=False
  family=node-link-network panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=13 lead=2 count=1 read=0 gap=2 pattern=as-shown-in style=['Figure 10']
  caption: Figure N: words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p15: sec=5 Case Studies > 5.2 Atlanta Child Murders > 5.2.4 Assessment of Results [evaluation] zone=middle order=11/2 area=0.068 solo=False
  family=heatmap-or-contour panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=14 lead=1 count=1 read=0 gap=1 pattern=as-shown-in style=['Figure 11']
  caption: Figure N: words=37 sent=2 units=False vars=0 cond=False concl=False voice=passive pos=below

figure 12 p16: sec=6 Improving the Model > 6.2 Profiling Potential Victims [model] zone=top order=12/1 area=0.094 solo=False
  family=surface-or-3D panels=1 layout=1 shared=False legend=none cbar=False 3d=surface-mesh printed=False
  mention: first=14 lead=2 count=1 read=0 gap=2 pattern=as-shown-in style=['Figure 12']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

