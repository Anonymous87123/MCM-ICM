# P-E-2018-93840-dffa6997 — figure census

- layout sha `2fda805d3fc4c061`, 24 pages, 13 measured regions
- accounted: 7 figures, 0 tables, 6 excluded, 0 unaccounted
- families: line 7

1. p8 **line** conf=high panels=1
   bbox [72.0, 227.28, 540.0, 518.04] (?)
   cap: Figure 1: This figure shows the equilibriums corresponding to different values of r and k. The black curve represents x/(1+x2) and the gray lines represents r(1 - x/k) with different r values.
   note: The paper's key figure and its only caption that is not in the text layer: the curve x/(1+x2) against three straight lines r(1 - x/k) at r1, r2 and r3, with the tangency case marked. Two sentences, and it names both parameters it varies - against every later caption, which names none.
2. p10 **line** conf=high panels=1
   bbox [72.0, 86.4, 540.0, 366.0] (?)
   cap: Figure 2: This gure depicts the relationship between dMdt = dMdt and M . The equilibriums occur when 0, which are the intersects on x-axis.
   note: Three solution curves of dM/dt against M, labelled in the plot as Stable, Vulnerable and Fragile Status. No legend, no printed tick numbers, and the status names are set as floating text inside the axes - the paper's habit from here on: annotate the curves in place instead of keying them.
3. p12 **line** conf=high panels=1
   bbox [72.0, 86.4, 540.0, 365.4] (?)
   cap: Figure 3: This gure is a parametric plot of (s; r), where s and r are expressed as a function of t. The s r curve represents the occurrence of a saddle-node bifurcation.
   note: The paper's operational chart: two boundary curves in (s, r) space with the three state regions named in place and one red marker annotated 's=5.2, r=0.65' for a specific country. It is the ONLY figure in the paper with printed tick numbers, and its title contradicts its axes - the title reads 'Plot of s vs t' while the two axes are s and r.
4. p13 **line** conf=high panels=1
   bbox [239.76, 394.2, 490.8, 592.56] (?)
   cap: Figure 4: This gure shows the fragility assessment of Syria and its current status in d M dt plot. The model predicts that Syria would have a negative growth rate and become more fragile.
   note: Syria's fragility assessment: a solid current-state curve, a dotted projected curve with climate change, a black dot for each stable equilibrium and a red dot for the unstable one, keyed by a four-row legend INSIDE the plot. No printed tick numbers, so the 'negative growth rate' the caption claims cannot be read off the axes at all.
5. p15 **line** conf=high panels=1
   bbox [179.4, 268.08, 432.6, 466.44] (?)
   cap: Figure 5: This gure shows the fragility assessment of Cuba and its current status in M dMdt plot. The model predicts that Cuba would maintain a high growth rate.
   note: Cuba's copy of Figure 4 with a five-row legend inside the plot: it adds a 'Current Position' key that Figure 4 did not have, and the current position is marked with a red dot. No printed tick numbers again, so the 'slight upward shift of the curve' the body prose describes has to be taken on trust.
6. p16 **line** conf=high panels=1
   bbox [118.8, 233.16, 493.2, 527.88] (?)
   cap: Figure 6: This bifurcation plot positioned three countries at their current states and shows the potential change of position.
   note: The bifurcation chart applied: the two Figure-3 boundary curves with the three countries planted inside it as blue dots on red stems, each labelled by name in place. No legend and no printed tick numbers, and the title is the section's own name ('Country Analysis') rather than a description of the chart.
7. p18 **line** conf=high panels=1
   bbox [72.0, 86.4, 540.0, 294.84] (?)
   cap: Figure 7: This gure shows the fragility assessment of New Zealand and its current status in M dMdt plot. The model shows that New Zealand is slowly approaching its equilibrium.
   note: New Zealand: a single dotted curve with one red dot for the current state and a two-row legend inside the plot, one row of which misspells its own key ('Equillbrum'). By this point the template has been reused three times with the legend shrinking each time - four keys for Syria, five for Cuba, two here.

## excluded
- p1 not-an-exhibit bbox [72.0, 81.96, 540.0, 302.04] 
- p4 not-an-exhibit bbox [90.0, 450.72, 558.0, 516.6] 
- p7 not-an-exhibit bbox [129.24, 527.52, 321.96, 585.24] 
- p8 not-an-exhibit bbox [236.28, 164.16, 375.0, 211.44] 
- p8 not-an-exhibit bbox [72.0, 527.52, 539.52, 560.88] 
- p11 not-an-exhibit bbox [201.72, 213.12, 410.16, 302.4] 

## distillation fields

figure 1 p8: sec=5 Equilibrium and Tipping Points [other] zone=middle order=1/1 area=0.2807 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=8 lead=0 count=1 read=1 gap=0 pattern=figure-n-shows style=['Figure 1']
  caption: Figure N: words=32 sent=2 units=False vars=2 cond=False concl=False voice=active pos=below

figure 2 p10: sec=5 Equilibrium and Tipping Points [other] zone=top order=2/1 area=0.27 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=9 lead=1 count=1 read=1 gap=1 pattern=as-shown-in style=['Figure 2']
  caption: Figure N: words=23 sent=2 units=False vars=2 cond=False concl=False voice=active pos=below

figure 3 p12: sec=5 Equilibrium and Tipping Points [other] zone=top order=3/1 area=0.2694 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=33 sent=2 units=False vars=3 cond=False concl=False voice=active pos=below

figure 4 p13: sec=6 Country Analysis > 6.1 Syria [other] zone=middle order=4/1 area=0.1027 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=34 sent=2 units=False vars=0 cond=False concl=True voice=active pos=below

figure 5 p15: sec=6 Country Analysis > 6.2 Cuba [other] zone=middle order=5/1 area=0.1036 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=29 sent=2 units=False vars=0 cond=False concl=True voice=active pos=below

figure 6 p16: sec=6 Country Analysis > 6.2 Cuba [other] zone=middle order=6/1 area=0.2277 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=19 sent=1 units=False vars=0 cond=False concl=False voice=active pos=below

figure 7 p18: sec=6 Country Analysis > 6.3 New Zealand [other] zone=top order=7/1 area=0.2013 solo=False
  family=line panels=1 layout=1 shared=False legend=inside cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=30 sent=2 units=False vars=0 cond=False concl=True voice=active pos=below

