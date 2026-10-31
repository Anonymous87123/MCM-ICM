# q225 G1 — Summary and Introduction paragraph chains

Paper P-C-2022-2204883-34c13ed1, 2022 C, team 2204883, title "Gold Strategy
for Gold & Bitcoin traders". Source sha256
34c13ed1dc7b5668e2261ddeb1995b450f454601906cfb2e1fca4739ded12858, matching
the manifest. Summary read from proxy p01.jpg (314,730 bytes). Introduction
read from proxy p03-intro.jpg (126,027 bytes), full page, no crop. Text layer
checked against both images; where they differ the image wins and the
difference is named below.

This file records the paragraph chain only. It does not close G2 or G3.

## Summary: six blocks, two of them numberless

Six prose blocks between the sheet header and the Keywords line. The first
two carry no number of any kind. The next three are one block per task. The
last names the memorandum and never says "task 4".

Block 1, stakes, no numbers. "In today's society, with the continuous
development of the economy, more and more people try to increase their income
by means of asset investment." Opens on the society, not on the team. The
second sentence turns on "However" and ends on the reader's desire: "is what
every market trader wants to know." The desire is a list of three verbs
inside one clause: predict price movements, maximize returns, minimize risks.
The block asks nothing and answers nothing. Its job is to make the reader the
person who wants the answer.

Block 2, the client arrives, still no numbers. "A trader who only focus on
two financial products, gold and bitcoin, comes to us for help." "who only
focus" is the printed agreement; kept. The authors answer in the first person
plural and name the aim "the ambitious goal". The sentence that follows
repeats the three-verb list from block 1 but narrows it: "by analyzing the
previous price data of gold and bitcoin respectively." So block 2 does the
scoping that block 1 refused to do, and it does it by trimming the same
sentence rather than by starting a new one.

Block 3, task 1, method then two numbers then a translation. Opens "For task
1, after data preprocessing,". The method sentence names both models with the
expansion glued to the abbreviation: "LSTM(Long Short-Term Memory)" and
"MLP(Multi-objective Linear Programming)", no space before the parenthesis,
both bold. Then the error pair, joined by "while" and not shortened:
"The price prediction result of gold reaches an MAPE value of 0.007261 while
the price prediction result of bitcoin reaches an MAPE value of 0.041630."
The whole phrase "reaches an MAPE value of" is said twice. Paper 224 did this
job with "that of". Here the repetition is the choice. MAPE itself is
expanded the same way, "MAPE(Mean Absolute Percentage Error)", bold, once.
The terminal value is delivered as a transformation, not a label: "makes the
initial $1,000 investment worth $14,325.13 on September 10, 2021." Only the
dollar figure is bold; the date is not. A separate sentence then translates
it: "The net profit exceeds 13 times of the initial asset." 14325.13 / 1000
is 14.3, so "exceeds 13 times" and the number do not say the same thing. Both
kept. The translation sentence is the move worth learning: one sentence
states the value, the next sentence says what the value means, and the second
sentence is allowed to be looser than the first.

Block 4, task 2, rivals before result, no metric value. "For task 2, we
provide evidence that our model gives the best strategy by setting up 10
evaluation metrics and comparing the values of those metrics under 2 simple
investment strategies, 1 idealized investment strategy and 1 commonly used
investment strategy on the market, and the investment strategy obtained by our
model." The numerals are digits. The authors' own strategy stands last,
inside the same list, so the comparison includes itself. The payoff sentence
is "not only ... but also": "not only a high profit but also a good balance
between risk and return." The claim is carried by two counts, 10 metrics and
4 rivals, and by no measured number. That is a different quantitative role
from block 3, and it should stay different: a proof block can be written
entirely in counts.

Block 5, task 3, the paired sentence that earns its therefore. "For task 3,
We" — capital W after the comma, one instance. The method is the one-factor
rule said as a clause: "by changing the commission of one asset and keeping
the commission of the other asset unchanged alternately." Then a sentence
that counts the instruments before any finding: "We set 5 metrics to measure
the effect on strategies and 2 metrics to measure the effect on results."
This sentence is bold, and it is the only place the summary separates
behavior metrics from result metrics. The finding is one sentence split by a
semicolon, gold half then bitcoin half, each half shaped "when the commission
of X increases, ...". Gold's net profit "remains the same" and its win rate
"shows an upward trend"; bitcoin's net profit "decreases significantly" and
its win rate "shows a decreasing trend". The two halves are parallel in
syntax and opposite in direction, and that opposition is what the next
sentence points at: "Therefore, we conclude that investment strategies are
more sensitive to changes in the transaction costs of bitcoin." The
conclusion clause is bold. The "Therefore" has a sentence to point back at,
which is the whole reason the pair was built.

Block 6, the memorandum, two sentences, no "task 4". "Finally, we write a
memorandum including our strategy, model, and results for the trader. We hope
this memorandum will become a valuable reference for him or her further
investment." The trader is addressed as "him or her" rather than named. 224's
closing block named the deliverable and stopped. This one adds a hope
sentence aimed at the reader's future action. The Keywords line mixes the
expanded method names with the short topic words, and "risk and return"
echoes the task 2 payoff sentence.

Counts for the summary page: 6 prose blocks, 0 equations, 0 figures, 0
tables, 0 citations. Numbers present: 0.007261, 0.041630, $1,000,
$14,325.13, September 10 2021, 13 times, 10 metrics, 2 + 1 + 1 strategies,
5 behavior metrics, 2 result metrics. Bold items: three method expansions,
one dollar figure, one counting sentence, one conclusion clause.

## Introduction: the same two blocks, trimmed, then a verb list

The introduction reprints blocks 1 and 2 and then edits them. Block 1 drops
"minimize risks" from the three-verb list, leaving "predict their price
movements and maximize returns". Block 2 drops "and minimize risks" as well,
so "maximizes returns by analyzing the previous price data". "who only focus"
is reprinted unchanged. The repetition is not padding: the introduction is
willing to repeat a paragraph and then cut it, and the cut is the new
information. What was removed is risk. Risk comes back later, inside the
third bullet, as "commissions", and inside the fifth bullet, as "sensitivity".
The opening paragraphs are allowed to be narrower than the summary.

Then one lead-in sentence, "To achieve our goal, we need to:", and six
bullets. Every bullet starts with a bare infinitive and names one deliverable:

1. "Pre-process the data provided by COMAP official."
2. "Build price prediction models for gold and bitcoin respectively."
3. "Build investment strategy model considering the predicted price of gold
   and bitcoin and their commissions for each transaction."
4. "Prove that our investment strategy is good enough by calculating strategy
   evaluation metrics and comparing the value to several other strategies."
5. "Analyze the sensitivity of our strategy to transaction costs by changing
   the commission value of gold and bitcoin."
6. "Write a memorandum including our strategy, model and results for the
   trader as a reference for his or her investment."

The order is the order of the later sections: preprocessing, prediction,
strategy, proof, sensitivity, memorandum. Bullet 4 says "good enough" where
the summary said "the best strategy". Both wordings are printed; the summary
claims more than the work plan does. Bullet 3 is the only one that names an
input from an earlier bullet, "considering the predicted price", so the
handoff from prediction to strategy is written into the list rather than left
to the reader. "his or her" reappears, matching the summary's "him or her".

The page closes with one sentence and a figure: "Our modeling framework can
be illustrated as shown in Figure 1." The sentence says "illustrated as
shown", which doubles the pointing word; printed that way. The caption is
"Figure 1: Modeling framework" and nothing more.

## Figure 1, read from the page

Four colored panels inside one dashed border, read left to right, plus a
legend of three rounded labels at the right edge marked Task 1, Task 2, Task
3. Task 4 has no color in the legend. The panels:

- Green, top left, "Data Preprocessing": "COMAP Official Data" in, "Missing
  Value Processing" inside, arrow down to the prediction panel.
- Yellow, bottom left, "Price Prediction Model": "BITCOIN-MKPRU.csv" in,
  "LSTM Model", "Choose the Optimal Parameters", arrow right.
- Orange, center, "Investment Strategy Model": "Quantify Risk and Return",
  "Multi-objective Linear Programming (Divided into 6 Cases)", "Use the Ideal
  Point Method to Solve", "Transaction Cost Limitation". This is the first
  place the paper says the model is "divided into 6 cases". The summary never
  says six.
- Blue, top right, "Strategy Evaluation": "Set up 10 Metrics for Evaluation",
  "Compare with 4 other Benchmark Strategies".
- Pink, bottom right, "Sensitivity of Transaction Costs": "Consider the
  transaction costs of gold and bitcoin separately", then two small boxes,
  "Evaluate the impact on result with 2 Metrics" and "Evaluate the impact on
  strategy with 5 Metrics".

Arrows run from preprocessing down into prediction, from prediction right
into the strategy panel, and from the strategy panel right into both
evaluation and sensitivity. The figure repeats the bullet list as a flow and
adds three facts the bullets omit: six cases, the ideal point method, and the
split between 2 result metrics and 5 strategy metrics. The last of these
matches the bold counting sentence in summary block 5, so the split is stated
twice before the body begins.

## What is reusable, and where it stops

Reusable from this paper's opening:

- Two numberless blocks before any task block: one for the reader's desire,
  one for the specific client. The second trims the first instead of
  restating it fresh.
- One block per required deliverable, opened by "For task n", with the final
  deliverable allowed to drop its number and use "Finally".
- A result stated as a transformation ("makes X worth Y on date") followed by
  a separate, looser translation sentence ("exceeds 13 times").
- A comparison block written in counts of metrics and rivals, with the team's
  own entry placed last inside the same list.
- A sensitivity finding as one semicolon sentence with parallel halves and
  opposite directions, so the "Therefore" sentence has a contrast to land on.
- A work-plan list of bare infinitives, one deliverable each, in the order
  the paper will actually proceed, with the handoff written into the bullet
  that receives it.
- Bold reserved for the method name at first mention, the single headline
  number, and the sentence that states the conclusion. Not for every number.

Not reusable, and recorded so it is not copied:

- "who only focus", "is objectively existed" elsewhere, the capital after the
  comma. These are this team's habits, not a pattern.
- "exceeds 13 times" against a 14.3-fold number. The translation sentence may
  be looser than the value sentence; it may not contradict it.
- "the best strategy" in the summary against "good enough" in the work plan.
  Pick one strength of claim and hold it.
- The missing "task 4". Dropping the number is fine only when the closing
  block still names the deliverable, which this one does.
