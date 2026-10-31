# P-C-2022-2203120-59ecfcb7 — figure census

- layout sha `27fd1a19db20ec60`, 24 pages, 44 measured regions
- accounted: 18 figures, 8 tables, 18 excluded, 0 unaccounted
- families: composite-panel 12, flowchart-or-schematic 5, line 1, table-grid 8

1. p3 **composite-panel** conf=high panels=2
   bbox [118.13, 207.86, 259.87, 292.9] (?)
   cap: Figure 1: The prices of two assets
   note: Two area-filled price plots in rounded plates, 'GOLD DAILY PRICES' over a 1000-2200 dollar axis and 'BITCOIN DAILY PRICES' over a 0-70000 axis, sharing a date x axis from 2016 to 2021. Neither panel titles an axis or prints a currency sign, so the only unit on the plate is the printed line under the panels, '(a) Gold daily prices, U.S. dollars per troy ounce (b) Bitcoin daily prices, U.S. dollars per bitcoin', which sits between the artwork and the caption. The x tick labels are rotated 45 degrees and collide; the two panels are set in visibly different type scales.
2. p4 **flowchart-or-schematic** conf=high panels=1
   bbox [120.38, 428.12, 488.89, 612.08] (?)
   cap: Figure 2: Overall structure
   note: Block diagram of the whole paper: a blue 'Data preprocessing' to 'ARIMA model' to 'Prediction trend by cycle' stack, a salmon 'Define variable parameters' to 'Establish strategy model' stack branching down to 'Conservative strategy' and 'Risk strategy', and a green side box that feeds 'Establish strategy model' through one fat block arrow while every other connector is a thin line arrow. Four italic group labels ('Price Prediction Model', 'Strategy Model', 'Impact of transaction costs on strategy', 'Prove Optimization of the Strategy') float beside the boxes rather than titling them. No axes, no legend, no number.
3. p7 **flowchart-or-schematic** conf=high panels=1
   bbox [120.38, 73.59, 488.89, 198.09] (?)
   cap: Figure 3: Structure of ARIMA model
   note: Hub-and-spoke equation plate: oversized pale 'p', 'd' and 'q' letterforms joined by orange '+' and '=' into a blue 'ARIMA' disc, with four step callouts radiating left ('Step1: stabilization', 'Step2: selection of p and q', 'Step3: white noise test', 'Step4: prediction') and green labels 'Auto Regressive', 'Integrated', 'Moving Average' overprinted on the letters. No axes, no legend, no number, no data.
4. p8 **composite-panel** conf=high panels=2
   bbox [75.61, 73.59, 302.39, 227.54] (?)
   cap: Figure 4: ACF chart and PACF chart
   note: Two plate columns, gold and bitcoin, each stacking an 'Autocorrelation' stem plot over a 'Partial Autocorrelation' stem plot on a fixed -1.00 to 1.00 y axis with a shaded 95 percent band at every lag. The four cells print no axis titles at all, no lag unit on x, and no (a)/(b) letter: the gold-versus-bitcoin split is knowable only from the caption. The lag-0 stem is clipped by the top of the frame in all four cells.
5. p8 **composite-panel** conf=high panels=2
   bbox [75.61, 526.21, 302.39, 653.99] (?)
   cap: Figure 5: Forecast charts in one cycle
   note: Two line panels, 'Gold' and 'Bit', each overlaying 'real' in blue and 'predict' in red with the legend inside at the upper right. Independent y axes (1240-1340 and 600-740) with no y title and no currency unit; x ticks are day-month-year strings that crowd at the right end. The right panel is titled 'Bit', not 'Bitcoin', and its predicted series stays flat at the final point while the real series falls.
6. p11 **flowchart-or-schematic** conf=high panels=1
   bbox [120.38, 437.95, 488.89, 579.82] (?)
   cap: Figure 6: The process of determining whether to trade
   note: Vertical decision flowchart, four diamonds over six boxes, ending in a yellow terminal 'go to step 4(1)' and an orange terminal 'go to step 4(2)', with the loop box 'i=i+1 back to step2' collecting three separate 'no' exits. The increase-threshold box prints 'e_{g(i-1)}' where its decrease twin prints 'f_{g(i+1)}', both threshold formulas are clipped by their box borders, and the two terminal colours carry no key.
7. p12 **flowchart-or-schematic** conf=high panels=1
   bbox [120.38, 146.42, 488.89, 288.29] (?)
   cap: Figure 7: The process of determining the number of transactions
   note: Flowchart of the purchase decision: 'calculate decision coefficient' to the diamond 'R_i2 < R2', whose branches buy with the high or the low proportion, both merging into 'Calculate the asset distribution and total assets after the transaction' and on through 'i>n' to a green 'end'. A third orange box '(2) purchase with mi proportion' feeds the same merge with no incoming arrow, so that branch has no trigger and is unreachable; the label reads 'back to step2' with no space.
8. p13 **line** conf=high panels=1
   bbox [191.25, 117.53, 418.02, 288.95] (?)
   cap: Figure 8: The changes of total assets during the ﬁve-year period
   note: One blue total-assets line from 2017 to 2021, titled inside the plot 'Changes in total assets' with the y axis 'Dollar' and x 'date'. The direction of change is left to the reader: the curve climbs to about 180000 in 2021 without a word of comment, and the y ticks above 100000 lose their thousands separators. The only citation of this plate is the bare 'figure below', with no number.
9. p15 **composite-panel** conf=high panels=3
   bbox [76.02, 117.53, 217.75, 224.66] (?)
   cap: Figure 9: Changes of various assets of insurance-type traders
   note: Three line panels titled 'Changes in cash', 'Changes in gold' and 'Changes in bit', y titles 'Dollar', 'Ounce' and 'Ounce' and x 'Date'. The third panel plots bitcoin holdings against a y axis titled 'Ounce', which repeats the gold unit; all three traces are the same green, none carries a panel letter, and the three y ranges differ by three orders of magnitude (0-1000, 0.0-1.2, 0.000-0.014).
10. p15 **composite-panel** conf=high panels=3
   bbox [76.02, 316.62, 217.75, 423.76] (?)
   cap: Figure 10: Changes in total assets of three types of traderss
   note: Three line panels that all carry the identical in-plot title 'Changes in total assets' and all print y 'Dollar' and x 'date', so nothing on the plate says which trader type is which - the (a) Insurance-type / (b) Common-type / (c) Radical-type line between the panels and the caption belongs to the printed figure and is the only key. The y ranges 0-16000, 0-70000 and 0-175000 are independent and only the third is labelled with round numbers.
11. p16 **composite-panel** conf=high panels=2
   bbox [103.96, 252.02, 274.04, 379.58] (?)
   cap: Figure 11: The impact of wL on total assets
   note: Two panels, '(a) gold' and '(b) bitcoin', both titled 'Changes in total assets' and both on an identical 0-200000 dollar axis, so the two series that the plate is about are squeezed into a band a fortieth of the axis high. The x axis carries the raw code identifier 'down_gold_threshold' / 'down_bit_threshold' over the integers 1 to 6, in place of the parameter the caption names.
12. p16 **composite-panel** conf=high panels=2
   bbox [103.96, 453.5, 274.04, 582.07] (?)
   cap: Figure 12: The impact of wH on total assets
   note: The same two-panel template as Figure 11 in salmon: duplicate 'Changes in total assets' titles, identical 0-200000 y axes and raw identifiers 'buy_gold_more_threshold' / 'buy_bit_more_threshold' on x. Nothing but the colour and the caption distinguishes it from Figures 11 and 13.
13. p17 **composite-panel** conf=high panels=2
   bbox [103.96, 73.59, 274.04, 202.16] (?)
   cap: Figure 13: The impact of m on total assets
   note: Third copy of the two-panel template, dark green, with 'sale_gold_threshold' / sale_bit_threshold' on x and the same duplicated chart title and 0-200000 axis. It is the only one of the three robustness plates whose reading sentence follows it, and that sentence refers to 'the figure above' without a number.
14. p18 **composite-panel** conf=high panels=3
   bbox [76.02, 475.63, 217.75, 588.73] (?)
   cap: Figure 14: Change of strategy in case a
   note: Three panels titled 'Changes in the number of transactions', 'Changes in total assets' and 'Variation of variance' against 'alpha gold', y titles 'Frequency', 'Dollar' and none. All three curves are almost flat, which is the paper's point but also means the plate carries no readable variation; the third panel has no axis title and the frequency axis starts at 55 rather than 0.
15. p19 **composite-panel** conf=high panels=3
   bbox [76.02, 186.43, 217.75, 295.9] (?)
   cap: Figure 15: Change of strategy in case c
   note: The case-c twin of Figure 14: the same three panel titles and the same three y titles, against an x axis of 'alpha gold' running 0.02 to 0.10 instead of 0.002 to 0.010, so the two plates label the same quantity on two different scales. Panel 1's y ticks are printed out of order - a '46.0' closes a descent from 60.0 to 42.5 where 40.0 belongs.
16. p21 **flowchart-or-schematic** conf=high panels=1
   bbox [92.04, 73.6, 517.24, 152.71] (?)
   cap: Figure 16: Structure of transaction strategy model
   note: Three blue filled ellipses joined left to right by thin arrows - 'When to trade', 'Trading bitcoin or gold', 'How much is the specific transaction' - in the clip-art style of an office diagram rather than the drawn flowcharts of section 3. The chain has no branch and no decision diamond, so the structure it claims to show is a straight line with three stops. The caption is printed above the artwork, which is the memo page's only figure.
17. p24 **composite-panel** conf=high panels=3
   bbox [76.02, 155.4, 217.75, 262.54] (?)
   cap: Figure 17: Changes of various assets of common-type traders
   note: Three step-shaped panels titled 'Changes in cash', 'Changes in gold' and 'Changes in bit', y titles 'Dollar', 'Ounce' and 'Pieces' with x 'Date' from 2017 to 2021. The bitcoin holdings rise past the top tick of their own 0-1.0 axis (about 1.05), and the gold and bitcoin panels use the same 0-1.0 scale for ounces and coins, so the two are drawn as if comparable.
18. p24 **composite-panel** conf=high panels=3
   bbox [76.02, 330.09, 217.75, 437.23] (?)
   cap: Figure 18: Changes of various assets of radical-type traders
   note: The radical-trader twin of Figure 17, with the identical three panel titles and the identical unit titles, but magnitudes two orders apart: cash peaks near 640 against 4000, gold near 0.16 ounce against 1.0, bitcoin near 2.8 against 1.0. Nothing inside either plate says which trader type it belongs to; only the captions and the (a)/(b)/(c) line above each plate distinguish them.

## tables
1. p5 table-grid bbox [80.63, 415.7, 531.37, 601.6]
   cap: Table 1: Notations
2. p7 table-grid bbox [103.82, 366.41, 508.18, 422.13]
   cap: Table 2: P value of gold and bitcoin time series before and after diﬀerence
3. p7 table-grid bbox [79.87, 558.09, 532.13, 607.62]
   cap: Table 3: Conﬁrmation method of p value and q value
4. p9 table-grid bbox [89.44, 176.72, 522.56, 290.21]
   cap: Table 4: Variable parameters
5. p14 table-grid bbox [97.84, 563.31, 514.16, 670.62]
   cap: Table 5: Adjustment of variable parameters
6. p15 table-grid bbox [72.85, 534.05, 539.15, 627.09]
   cap: Table 6: Results of three types of strategies
7. p19 table-grid bbox [97.84, 443.84, 514.16, 478.92]
   cap: Table 7: The sensitivity of three types of strategies to two costs
8. p22 table-grid bbox [72.85, 361.8, 539.15, 425.77]
   cap: Table 8: Results of three types of strategies

## excluded
- p3 fragment-of-other bbox [353.93, 207.86, 495.66, 292.9] Panel (b) of Figure 1, the bitcoin daily-price area, returned as its own region inside the plate.
- p8 fragment-of-other bbox [311.41, 73.59, 538.18, 227.54] The bitcoin column of Figure 4, its ACF-over-PACF pair, returned as its own region.
- p8 fragment-of-other bbox [311.41, 526.21, 538.18, 653.99] Panel (b) of Figure 5, the bitcoin forecast panel.
- p15 fragment-of-other bbox [228.77, 117.53, 370.5, 224.66] Panel (b) of Figure 9, the gold-holdings panel.
- p15 fragment-of-other bbox [381.52, 117.53, 523.25, 224.66] Panel (c) of Figure 9, the bitcoin-holdings panel.
- p15 fragment-of-other bbox [228.77, 316.62, 370.5, 423.76] Panel (b) of Figure 10, the common-type total-assets panel.
- p15 fragment-of-other bbox [381.52, 316.62, 523.25, 423.76] Panel (c) of Figure 10, the radical-type total-assets panel.
- p16 fragment-of-other bbox [339.75, 252.02, 509.83, 379.58] Panel (b) of Figure 11, the bitcoin wL panel.
- p16 fragment-of-other bbox [339.75, 453.5, 509.83, 582.07] Panel (b) of Figure 12, the bitcoin wH panel.
- p17 fragment-of-other bbox [339.75, 73.59, 509.83, 202.16] Panel (b) of Figure 13, the bitcoin m panel.
- p18 fragment-of-other bbox [228.77, 475.63, 370.5, 588.73] Panel (b) of Figure 14, the total-assets panel of case a.
- p18 fragment-of-other bbox [381.52, 475.63, 523.25, 588.73] Panel (c) of Figure 14, the variance panel of case a.
- p19 fragment-of-other bbox [228.77, 186.43, 370.5, 295.9] Panel (b) of Figure 15, the total-assets panel of case c.
- p19 fragment-of-other bbox [381.52, 186.43, 523.25, 295.9] Panel (c) of Figure 15, the variance panel of case c.
- p24 fragment-of-other bbox [228.77, 155.4, 370.5, 262.54] Panel (b) of Figure 17, the gold-holdings panel of the common-type appendix plate.
- p24 fragment-of-other bbox [381.52, 155.4, 523.25, 262.54] Panel (c) of Figure 17, the bitcoin-holdings panel of the same plate.
- p24 fragment-of-other bbox [228.77, 330.09, 370.5, 437.23] Panel (b) of Figure 18, the gold-holdings panel of the radical-type appendix plate.
- p24 fragment-of-other bbox [381.52, 330.09, 523.25, 437.23] Panel (c) of Figure 18, the bitcoin-holdings panel of the same plate.

## distillation fields

figure 1 p3: sec=1 Introduction > 1.1 Problem Background [introduction] zone=top order=1/1 area=0.025 solo=False
  family=composite-panel panels=2 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=3 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['Figure 1']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 2 p4: sec=1 Introduction > 1.3 Problem Analysis [introduction] zone=middle order=2/1 area=0.14 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 3 p7: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.2 Model Establishment of Problem 1 > 3.2.1 Price Prediction Model [model] zone=top order=4/1 area=0.095 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 4 p8: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.2 Model Establishment of Problem 1 > 3.2.1 Price Prediction Model [model] zone=top order=7/1 area=0.072 solo=False
  family=composite-panel panels=2 layout=2 columns, ACF over PACF in each shared=False legend=none cbar=False 3d=no printed=True
  mention: first=7 lead=1 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 4']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 5 p8: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.2 Model Establishment of Problem 1 > 3.2.1 Price Prediction Model [model] zone=bottom order=8/2 area=0.06 solo=False
  family=composite-panel panels=2 layout=side-by-side shared=False legend=inside cbar=False 3d=no printed=True
  mention: first=8 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the ﬁgure 5']
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 6 p11: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.3 Model Solving: Finding Strategies [model] zone=middle order=10/1 area=0.108 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=11 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the ﬁgure 6']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 7 p12: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.3 Model Solving: Finding Strategies [model] zone=top order=11/1 area=0.108 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=12 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the ﬁgure 7']
  caption: Figure N: words=10 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 8 p13: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.4 Results and Model Evaluation > 3.4.1 Model Results [model] zone=top order=12/1 area=0.08 solo=False
  family=line panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=True
  mention: first=13 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['ﬁgure below']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 9 p15: sec=4 Problem 2: Prove Optimization of the Strategy > 4.1 Generalization Ability of the Model [model] zone=top order=14/1 area=0.031 solo=False
  family=composite-panel panels=3 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=15 lead=0 count=1 read=0 gap=None pattern=figure-n-shows style=['The ﬁgure 9']
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 10 p15: sec=4 Problem 2: Prove Optimization of the Strategy > 4.1 Generalization Ability of the Model [model] zone=middle order=15/2 area=0.031 solo=False
  family=composite-panel panels=3 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=15 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the ﬁgure 10']
  caption: Figure N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 11 p16: sec=4 Problem 2: Prove Optimization of the Strategy > 4.2 Robustness of the Model [model] zone=middle order=17/1 area=0.045 solo=False
  family=composite-panel panels=2 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the ﬁgure 11', 'ﬁgure 12', 'ﬁgure 13']
  caption: Figure N: words=9 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 12 p16: sec=4 Problem 2: Prove Optimization of the Strategy > 4.2 Robustness of the Model [model] zone=middle order=18/2 area=0.045 solo=False
  family=composite-panel panels=2 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the ﬁgure 11', 'ﬁgure 12', 'ﬁgure 13']
  caption: Figure N: words=9 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 13 p17: sec=4 Problem 2: Prove Optimization of the Strategy > 4.2 Robustness of the Model [model] zone=top order=19/1 area=0.045 solo=False
  family=composite-panel panels=2 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=16 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['the ﬁgure 11', 'ﬁgure 12', 'ﬁgure 13']
  caption: Figure N: words=9 sent=1 units=False vars=1 cond=False concl=False voice=none pos=below

figure 14 p18: sec=5 Problem 3: Sensitivity of Strategy to Transaction Cost > 5.2 Impact of Transaction Costs on Strategy [sensitivity] zone=bottom order=20/1 area=0.033 solo=False
  family=composite-panel panels=3 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=0 count=1 read=1 gap=None pattern=figure-n-shows style=['Figure 14']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 15 p19: sec=5 Problem 3: Sensitivity of Strategy to Transaction Cost > 5.2 Impact of Transaction Costs on Strategy [sensitivity] zone=top order=21/1 area=0.032 solo=False
  family=composite-panel panels=3 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=18 lead=1 count=1 read=1 gap=None pattern=as-shown-in style=['the ﬁgure 15']
  caption: Figure N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 16 p21: sec=未编号标题：MODEL [model] zone=top order=23/1 area=0.069 solo=False
  family=flowchart-or-schematic panels=1 layout=1 shared=False legend=none cbar=False 3d=no printed=False
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=7 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above

figure 17 p24: sec=Appendices > Appendix A Changes of Various Types of Traders’ Assetes [appendix] zone=top order=25/1 area=0.031 solo=False
  family=composite-panel panels=3 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

figure 18 p24: sec=Appendices > Appendix A Changes of Various Types of Traders’ Assetes [appendix] zone=middle order=26/2 area=0.031 solo=False
  family=composite-panel panels=3 layout=side-by-side shared=False legend=none cbar=False 3d=no printed=True
  mention: first=None lead=None count=0 read=0 gap=None pattern=none style=[]
  caption: Figure N: words=9 sent=1 units=False vars=0 cond=False concl=False voice=none pos=below

table 1 p5: sec=2 General Assumptions and Notations > 2.2 Notations [symbols] zone=middle order=3/1 area=0.173 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=5 lead=0 count=1 read=0 gap=None pattern=direct style=['Table 1']
  caption: Table N: words=3 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 11x2 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 2 p7: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.2 Model Establishment of Problem 1 > 3.2.1 Price Prediction Model [model] zone=middle order=5/2 area=0.046 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=7 lead=0 count=1 read=1 gap=None pattern=as-shown-in style=['table 2']
  caption: Table N: words=15 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 2x3 header=1 rules=booktabs zebra=False merged=False diag=False units_hdr=False dec=True num=2 txt=1 width=full orient=portrait cont=False

table 3 p7: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.2 Model Establishment of Problem 1 > 3.2.1 Price Prediction Model [model] zone=bottom order=6/3 area=0.046 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=7 lead=0 count=1 read=0 gap=None pattern=direct style=['table 3']
  caption: Table N: words=11 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 3x3 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=3 width=full orient=portrait cont=False

table 4 p9: sec=3 Problem 1: Prediction and Strategy in the Investment > 3.2 Model Establishment of Problem 1 > 3.2.2 Trading Strategy Model [model] zone=top order=9/1 area=0.101 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=9 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['table 4']
  caption: Table N: words=4 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x2 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=0 txt=2 width=full orient=portrait cont=False

table 5 p14: sec=4 Problem 2: Prove Optimization of the Strategy > 4.1 Generalization Ability of the Model [model] zone=bottom order=13/1 area=0.092 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=14 lead=0 count=1 read=0 gap=None pattern=as-shown-in style=['the table 5']
  caption: Table N: words=6 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 7x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=True num=3 txt=1 width=full orient=landscape cont=False

table 6 p15: sec=4 Problem 2: Prove Optimization of the Strategy > 4.1 Generalization Ability of the Model [model] zone=bottom order=16/3 area=0.09 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=15 lead=0 count=1 read=0 gap=None pattern=direct style=['table 8']
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 6x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=True num=3 txt=1 width=full orient=portrait cont=False

table 7 p19: sec=5 Problem 3: Sensitivity of Strategy to Transaction Cost > 5.2 Impact of Transaction Costs on Strategy [sensitivity] zone=middle order=22/2 area=0.03 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=19 lead=0 count=1 read=1 gap=None pattern=direct style=['Table 7']
  caption: Table N: words=12 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 2x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=True num=3 txt=1 width=full orient=landscape cont=False

table 8 p22: sec=未编号标题：RESULTS [result] zone=middle order=24/1 area=0.062 solo=False
  family=table-grid panels=1 layout=- shared=- legend=- cbar=- 3d=- printed=-
  mention: first=None lead=None count=0 read=1 gap=None pattern=as-shown-in style=[]
  caption: Table N: words=8 sent=1 units=False vars=0 cond=False concl=False voice=none pos=above
  table: 4x4 header=1 rules=vertical-rules zebra=False merged=False diag=False units_hdr=False dec=False num=3 txt=1 width=full orient=landscape cont=False

