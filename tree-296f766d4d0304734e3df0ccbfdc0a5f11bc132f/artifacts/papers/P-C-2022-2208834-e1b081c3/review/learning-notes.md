# q226 G1 — Summary and Introduction paragraph chains

Paper P-C-2022-2208834-e1b081c3, 2022 C, team 2208834, title "An Improved
Pairs Trading Strategy Based on Cointegration of Gold and Bitcoin". Source
sha256 e1b081c3cffac8544a42d2b0fde7208ba013d905b390ba27b6ea85fabd314cd2,
matching the manifest and the extraction record. Summary read from proxy
p01.jpg (198,294 bytes). Introduction read from proxy p04.jpg (173,602 bytes),
the full physical page 4, which prints "Page 3 of 24". Text layer checked
against both images. Where they differ the image wins, and each difference is
named below. This file records the paragraph chain only. It does not close G2
or G3.

## Summary: six blocks, none numbered, one of them a numbered list

The sheet header carries "Problem Chosen / C", "2022 / MCM/ICM / Summary
Sheet" and "Team Control Number / 2208834", then a rule, then the two-line
title, then the word "Summary" centered. Six prose blocks follow, then a
Keywords line. No block opens with "For task N". The paper never uses the
word "task" on this page. The work is sequenced by adverbs instead:
firstly, Secondly, Finally inside block 2, Then for block 4, In addition for
block 5, Finally again for block 6. Two "Finally"s in one summary is the
printed choice; both kept.

Block 1, the two assets, no numbers. One sentence of contrast, then one
sentence of purpose, then one sentence of claim. The contrast is carried by a
single "while" and is built as a mirror: gold is "a traditional investment",
"a safe haven asset", "stable returns", "commodity nature"; bitcoin is "an
emerging trading asset", "high volatility", "more arbitrage opportunities".
Each half gives the thing, the character, and the reason, in that order, and
the second half is shorter than the first. The purpose sentence names the
constraint inside a relative clause rather than as a condition: "a trading
model for gold and bitcoin that uses price data up to the day". "Up to the
day" is the whole no-lookahead rule, said in five words. The claim sentence
stacks three predicates on one subject with "and ... and": "that outperforms
all other strategies and is robust and has lower risk." Only "pairs trading
strategy" is bold, and it is bold on first mention, before the reader has
been told what it is. The block asserts the conclusion in its third sentence
and spends the rest of the page earning it.

Block 2, the method, three beats, then the number. "In order to get the best
trading strategy, we firstly ..." The "In order to" clause restates block 1's
purpose before any new information, which is how this paper opens almost
every block: a purpose clause, a comma, then "we" plus a verb. "firstly" is
lowercase and unbolded; "Secondly" and "Finally" are capitalized. The three
beats are observe, process, backtest, and each beat is one sentence. The
second beat names the method with the expansion before the abbreviation and
both bold: "the Modified Dollar Neutral strategy (MDN)". Then a relative
clause does the positioning: "which is an improvement of the pairs trading."
The period lands and the next sentence starts immediately: "trading.By using
MDN". No space after the period. Kept as printed. "By using MDN, we predict
the data and make a buying and selling decision" promises a prediction the
model section does not actually make; the pairs rule trades on a deviation
from an equilibrium price, not on a forecast. The sentence is kept anyway,
because the summary is what the paper claims.

The third beat is where the number lives, and it is buried at the end of a
long sentence rather than announced. "Finally, we conduct a backtest using
the data of the last five years, and the results show that after continuous
trading and asset transformation using the pairs trading strategy, the $1,000
on September 10, 2016 turn into $106,986.1 on September 10, 2021, with a
nearly 107 times year-on-year increase in net asset value and a huge return
rate." The grammar breaks twice: "turn" is not "turns", and "with a ..."
hangs off the whole clause. Both kept. The value is delivered as a
transformation, "the $1,000 ... turn into $106,986.1", with both dollar
figures bold and the dates unbolded. 106986.1 / 1000 is 106.99, so "nearly
107 times" matches this figure and not the 106686.1 printed later in sections
5.5 and 8.1.1. "year-on-year" is the wrong word for a five-year total; the
paper uses it for "over the whole period". Both the number and the misused
word are kept, and the conflict is recorded rather than repaired.

Block 3, the proof, rivals named before the result. "For the purpose of
proving that our strategy is the best strategy" — "best" is asserted as the
thing to be proved, not as a conclusion. The rivals are "random trading
strategy and machine learning strategy LSTM and XGBoost respectively", three
of them, listed in one noun phrase with "respectively" doing no work because
nothing is being matched. Then one sentence carries three comparisons, each
shaped "X is A-B times that of other trading strategies": Sharpe ratio
1.53-2.32, excess return 1.49-3.17, geometric return 1.63-3.25. The metric
name and the multiplier are bold; "times that of other trading strategies"
is roman and repeated in full three times. The paper does not reach for "that
of" as a shortener. It rewrites the whole tail every time, and the bold
marks only the part that changes. The closing participial phrase, "indicating
that pairs trading strategy has higher profitability and lower risk",
translates the three ranges into the same two-word claim block 1 already
made. So the block's job is not to inform but to attach numbers to a claim
the reader has already been given.

The ranges themselves are checkable against Table 2, and they check. Sharpe
1.46 over 0.63 is 2.32 and over 0.95 is 1.54, which the paper rounds to the
printed 1.53. The range is the worst rival and the best rival, said as one
interval. That is a move worth keeping: when a strategy beats several
baselines, report the multiplier as a range from the nearest rival to the
furthest, not as a single "up to".

Block 4, the cost, a lead sentence plus two numbered findings. "Then, we
analyze the sensitivity of this strategy to transaction costs." Singular
"this strategy", after a page of "the pairs trading strategy". Then "The
results show that:" and a lowercase roman list, "i." and "ii.", set inside
the paragraph rather than as bullets. Finding one: "There is a negative
exponential relationship between transaction cost and return." The whole
clause is bold. The support sentence gives the zero-cost endpoint and nothing
else: "When the transaction cost is 0, the theoretical return can reach
$120000." No comma in 120000, no cents, and "theoretical" is the word that
licenses a number the backtest never produced. Finding two flips the bold:
"Transaction cost is positively correlated with the number of transactions."
is bold, and its support sentence is half bold — "When the commission ratio
is 0.5%, the total return will approach 0 after 500 simulated transactions."
The condition is roman, the consequence is bold. A final unbolded sentence
certifies both findings at once: "The experimental results are in good
agreement with our mathematical derivation." Two findings, two shapes of
bold, one certification sentence. The certification claims an agreement the
reader cannot see yet, since no derivation has been shown.

Block 5, the risk, three sentences, no number. "In addition" marks it as an
extra rather than a main result. Sentence one announces the topic, sentence
two names the split and bolds both halves: "price risk and reinvestment
risk". Sentence three does all the work and sags badly. It runs "explore the
non-investable interval ..., and then set parameters: risk aversion
coefficient (λ) is used to discuss ..." — the colon does not introduce a
list, it introduces a fresh clause with a new subject. The bold runs from
"non-investable interval" through "(λ)", so the parameter and the concept it
serves are bolded together. "as a supplement to the matching strategy" is the
positioning clause, and "matching" is the paper's own synonym for pairs
trading, used nowhere else on the page. Section 6.1.2 later calls the same
object a "non-trading interval". The summary's word and the section's word
differ; both kept.

Block 6, the memorandum, one sentence. "Finally, we write a memo for traders
based on the results of the pairs trading strategy, the strength and the
possible improvements of the model comparison, and the results of the
sensitivity analysis to make our results more scientific and practical."
"a memo", not "a memorandum", though the document itself is headed as a
memorandum. The sentence names three inputs joined by "and" and then a
purpose infinitive, "to make our results more scientific and practical",
which claims two virtues the reader is asked to take on trust. Nothing is
bold. This is the only block on the page with no bold span, and it is the
block that points at the required communication artifact.

The Keywords line is roman, four items separated by semicolons, ending with
no period: "Modified Dollar Neutral Strategy; Cointegration; Pairs Trading;
Risk Evaluation". "Risk Evaluation" does not appear as a heading anywhere in
the paper. The keyword names the topic the authors wish they had a section
for.

Counts for the summary page: 6 prose blocks, 0 equations, 0 figures, 0
tables, 0 citations. Bold spans: "pairs trading strategy" once, "Modified
Dollar Neutral strategy (MDN)" once, "$1,000" and "$106,986.1", then "Sharpe
ratio", "1.53-2.32 times", "excess return", "1.49-3.17 times", "geometric
return", "1.63-3.25 times", then the negative-exponential clause, the
positive-correlation clause, the 0.5% consequence, then "price risk and
reinvestment risk" and "non-investable interval ... coefficient (λ)".

## Introduction: three background paragraphs, one method paragraph, four bullets

Physical page 4 prints "Page 3 of 24" and holds section 1, the head of
section 2, and nothing else. The introduction does not reprint the summary.
Where paper 225's introduction repeated its summary and then cut it, this
one starts over with different nouns and a looser claim.

1.1 paragraph 1, two sentences, the widest possible opening. "Market trading
usually involves buying and selling risk assets." Defines the activity by its
two verbs. "Investors want to limit their trading risk while maximizing
returns, and this can be achieve by invest wisely in a variety of assets."
Two errors in one clause, "be achieve" and "by invest", both kept. The
sentence pairs the two aims with "while" exactly as block 1 of the summary
paired the two assets, so "while" is this paper's contrast word in both
places. No number, no gold, no bitcoin. The paragraph's only job is to name
the trade-off.

1.1 paragraph 2, the two camps. "Serious gold investors (gold bugs) love gold
because ..." The parenthetical nickname is doing characterization, not
definition; a definition would not be affectionate. The reason is doubled:
"its ability to store value during tumultuous times and its use as an
inflation hedge." "tumultuous" is the one ornate adjective on the page, and
it sits inside a stock phrase, so it reads as borrowed vocabulary rather than
as the author's own register. The bitcoin sentence opens with "however" and
concedes before it claims: "bitcoin offers the same level of protection but
is superior due to its ease of storage and transfer." The concession is the
move. The authors give gold its full due and then hand the advantage to
bitcoin on a practical point, which lets them look even-handed while ranking
the two assets anyway.

1.1 paragraph 3, from the contrast to the problem. "Under the same initial
capital conditions" is the ceteris paribus phrase, placed first so the
comparison that follows is already qualified. "different portfolios will bring
different returns and associated risks" restates paragraph 1's trade-off with
"portfolio" now in it. "so it is necessary to study" is the paper's way of
saying "therefore we study" without using the first person — the first person
has not appeared yet and does not appear until 1.2. The problem is then
named twice, once loosely and once precisely, joined by "that is to say":
"the best way to balance portfolio, that is to say, the appropriate
proportions of gold and bitcoin in the portfolio." The second naming is the
one that constrains. This two-naming pattern, loose then precise with "that
is to say" between them, is the move worth keeping.

1.2 paragraph 1, six sentences, the whole method in one block. The opening
"In order to facilitate the evaluation of the trading model, we build a
backtesting system(See the appendix)." has no space before the parenthesis,
kept. The parenthetical is an imperative with a capitalized verb, "(See the
appendix).", which is a different register from the rest of the sentence and
the only imperative in the introduction. Sentence two certifies the tool
before it is used: "All of our models (the best model and the three baseline
models) are easily estimated using this system." The parenthesis quietly
spends the conclusion — "the best model" — before any comparison exists.
Sentence three states the build. Sentence four states what the simulation
returns and breaks: "we can the trading results of any model". The missing
verb is kept. The parenthesis that follows gives the deliverable as a
question rather than as a noun: "(how much is the initial $1000 investment
worth on 9/10/2021)". Note the form. The summary writes "$1,000" and
"September 10, 2021"; the introduction writes "$1000" and "9/10/2021". Same
quantity, two notations, and the introduction picks the shorter one inside a
parenthesis. Sentence five is the comparison claim and sentence six is the
rest of the pipeline in one breath: "Then we test the robustness of the model
and the sensitivity to transaction costs, and finally convey our model,
strategy and results to traders through memos." Robustness, sensitivity and
the memo are one sentence, in the order the paper will do them, and "memos"
is plural though one memo is produced.

Then the lead-in, "To solve these problems, our team will do the following:",
and four bullets. "our team will" is future tense, the only future in the
section; everything above it is present. The bullets are not parallel, and
the non-parallelism is the content:

Bullet 1 starts "As preparation," and uses present tense: explore, test,
clean, select, normalize. Five verbs for the data stage, which tells the
reader the data work has five parts before section 3 has been seen.

Bullet 2 starts "We consider" and narrates a result rather than a plan: "and
find that they passed the cointegration test." The test is reported as
already passed, inside a list of future work. "On this basis" is the handoff
phrase, and "so as to obtain the trading mode and trading strategy" doubles
the noun at the end. "trading mode and trading strategy" are not
distinguished anywhere later.

Bullet 3 is the long one and does three jobs. It names the three baselines
with "namely", and it lowers the case: "xgboost strategy" against the
summary's "XGBoost". It ranks their pedigree in a subordinate clause, "based
on current mainstream machine learning or time series analysis models", which
praises the rivals before the comparison — the same move as paragraph 2's
concession to gold. Then it lists the metrics in running text with the
parentheses glued to the noun, no space: "returns(arithmetic return,
geometric time weighted return, Jensen alpha)", "risk indicators (Sharpe
ratio)" with a space, "other indicators(information ratio, tracking error)"
without one. Two of the three parentheses have no space. Kept. The list is
grouped by what the metric measures, not alphabetically, and the grouping
words "returns", "risk indicators", "other indicators" are the paper's own
taxonomy. The bullet ends with the robustness method as its own sentence:
"By disturbing our model's parameters, we test the robustness of the model to
its own parameters." "disturbing" for "perturbing" is the printed word, and
the sentence says "parameters" twice because the method and the object are
the same thing.

Bullet 4 starts "Based on the previous research," and splits the risk exactly
as summary block 5 does, but changes the capitals: "price risk and
Reinvestment risk". One capital R, kept. "take personal risk preference into
account" is the introduction's version of the risk aversion coefficient, said
without the symbol. The bullet promises an analysis of "their impact on the
choice of trading strategy" and does not promise a number.

Section 2 opens at the bottom of the page with one sentence: "In order to
simplify the above problems, we make the following reasonable assumptions:"
"reasonable" is the author's adjective applied to their own assumptions,
before any assumption has been stated. The four assumptions themselves sit on
the next page and are out of scope for this gate.

Counts for the introduction page: section 1 has 4 paragraphs plus 4 bullets,
section 2 contributes 1 lead sentence, 0 equations, 0 figures, 0 tables, 0
citations. The only number is "$1000" and "9/10/2021", inside a parenthesis,
in shorter notation than the summary.

## What this paper's prose does that is worth reusing

The purpose clause before the first person. Blocks 2 and 4 of the summary and
both paragraphs of 1.2 open "In order to X, we verb". The purpose is a
subordinate clause and the action is the main clause, so the sentence states
why before what. It is wordier than "We X to Y" and that wordiness is the
habit, not a fault to edit out.

The contrast carried by one "while". Summary block 1 and introduction
paragraph 1 both put two opposed things in a single sentence with "while"
between them, and both put the reason inside the same sentence rather than in
a following one. Gold gets its reason ("due to its commodity nature"), the
investor gets theirs ("while maximizing returns"). The opposition and its
justification arrive together.

The claim said first and numbered later. Block 1 states "outperforms all
other strategies and is robust and has lower risk" with nothing to point at.
Block 3 restates it as "higher profitability and lower risk" and only then
supplies the three ranges. The number does not introduce the claim. It
confirms a claim the reader already holds. Writing the number first and the
interpretation second would reverse this paper's order.

The repeated tail instead of "that of". Block 3 writes "times that of other
trading strategies" three times in one sentence. The part that changes, the
metric and the range, is bold; the part that stays is roman and is written
out in full every time. The repetition is what makes the three ranges read as
one parallel series.

The range instead of the maximum. "1.53-2.32 times" reports the nearest rival
and the furthest rival as one interval. A single "up to 2.32 times" would
hide how close the best rival gets. The interval is the more honest form and
it is the one this paper chose.

The loose name then the precise name. "the best way to balance portfolio,
that is to say, the appropriate proportions of gold and bitcoin" says the
problem twice, vague then exact, with "that is to say" as the hinge. The
second naming is the one that can be tested.

The concession before the advantage. The gold sentence gives gold its full
case, and the bitcoin sentence begins from that concession ("the same level
of protection but is superior due to"). The baseline bullet does the same
thing by praising the rival models as "current mainstream" methods before
claiming to beat them. The praise costs nothing and makes the later claim
read as earned.

The certification sentence after a list of findings. Block 4 ends "The
experimental results are in good agreement with our mathematical derivation."
It does not add a finding. It tells the reader what to think of the two
findings just given, and it does it in one unbolded sentence after a run of
bold ones, so the typography drops exactly where the rhetoric steps back to
judge.

The deliverable stated as a question in parentheses. "(how much is the initial
$1000 investment worth on 9/10/2021)" puts the required output inside the
method sentence as a question, not as a noun phrase like "the terminal value".
The question form remembers that the output is an answer to something the
problem asked.

## Printed defects kept on these two pages

"trading.By" with no space after the period, summary block 2. "the $1,000 ...
turn into" with a plural verb, summary block 2. "this can be achieve by invest
wisely", introduction paragraph 1, two bare stems. "we can the trading results
of any model", introduction 1.2, missing verb. "system(See the appendix)" with
no space and a capitalized imperative inside the parenthesis. "returns(..."
and "indicators(..." with no space before the parenthesis, against "risk
indicators (Sharpe ratio)" which has one. "xgboost" lowercase in the bullet
against "XGBoost" in the summary. "Reinvestment risk" with one capital in the
fourth bullet against "reinvestment risk" lowercase in summary block 5.
"$120000" with no thousands separator against "$106,986.1" and "$1,000" which
have them. "$1000" and "9/10/2021" in the introduction against "$1,000" and
"September 10, 2021" in the summary. None of these are corrected. Each one is
a place where the paper's own hand is visible, and smoothing them would
replace the author with an editor.
