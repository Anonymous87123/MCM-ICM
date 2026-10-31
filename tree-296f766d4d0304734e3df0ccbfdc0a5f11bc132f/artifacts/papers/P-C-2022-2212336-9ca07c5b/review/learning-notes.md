# q227 G1 — Summary and Introduction paragraph chains

Paper P-C-2022-2212336-9ca07c5b, 2022 C, team 2212336, title "The Queen of
Strategy: The Road to Counterattack With $1,000". Source sha256
9ca07c5ba54ada6ea33616c1d27d528e6265cb53db5a74946fb861f3b3f414f0. Summary is
physical page 1, introduction is physical page 3. Both read from the text
layer. Paragraph breaks are taken from the indented blocks separated by blank
lines, which this paper prints consistently. No page of this paper prints a
page number, so paragraphs are anchored by physical page and section, not by a
printed page. This file records the paragraph chain and the writing habits
only. It does not close G2 or G3, and it does not repair any printed number.

## Summary: six paragraphs plus a keyword line, no numbered tasks

The sheet header carries "Problem Chosen / C", "2022 / MCM/ICM / Summary
Sheet" and "Team Control Number / 2212336", then the title, then the centered
word "Summary". Six prose paragraphs follow, then one keyword line. The paper
never numbers the tasks on this page and never uses the word "task". It
sequences the work by naming the two models and by a handful of sequence words:
"Second" for paragraph 3, "Again" for paragraph 5, "Finally" for paragraph 6.
The model names do the real organizing. "Model I" and "Model II" are the spine,
and the sequence words only mark the joints.

### Paragraph 1 — stakes, then the split into two models

"Nowdays, financial activities have become an important part of people's
lives. In trading, some people end up making profits but some people lose
money. The differences between the losers and the profiteers are not only for
the choice of asset variety, but also for the trading strategy. In this paper,
we focus on the development and evaluation of strategies. For this purpose, we
designed two models to develop our strategies: Model I: Volatile Asset Price
Forecasting Model; Model II: Strategy Improvement Model."

Five sentences. The move is stakes, then a contrast, then a narrowing, then a
declaration of two models. The order is: general scene, winners against losers,
the cause named as strategy rather than asset choice, the paper's focus, the
two models listed. The contrast "not only ... but also" does the narrowing: it
pushes the cause off the asset and onto the strategy, which is exactly the
thing the paper can control. That is the whole job of the paragraph. It carries
no number.

Two habits worth keeping. First, the opening is a plain present-tense statement
about the world, not a citation and not a definition. "have become an important
part" is the kind of unadorned scene-setting this paper likes. Second, the
models are announced as a colon list with a name and a subtitle each, "Model I:
Volatile Asset Price Forecasting Model", so the reader gets the label and the
job in one line. The paper reuses "Model I" and "Model II" as shorthand from
here on.

Printed as-is, not corrected: "Nowdays" for Nowadays, and "profiteers" where
the context means the people who profit.

### Paragraph 2 — Model I, method then the one error pair

"For Model I, as a forecasting model, the accuracy of its results is relevant
to the formulation of our strategy and its returns. It is prudent to predict
only one day ahead in a single run. We first use the ARIMA model to forecast
the price and find that it can only predict well about the linear part of
bitcoin price. Second, we take the LSTM model to forecast, and just the
opposite of the ARIMA model, the LSTM model is able to capture the information
of the non-linear part of the asset price relatively well; finally, we combine
them to form ARIMA-LSTM model, and the final price prediction results almost
overlap with the real results, with RMSE and MAPE were 0.0342 and 0.36,
respectively."

One paragraph holds the whole forecasting argument. The order is: why accuracy
matters, a self-imposed limit (one day ahead), ARIMA and what it can do, LSTM
and that it does the opposite, the combination, then two error numbers. The
internal sequence is "first ... Second ... finally", three steps inside one
paragraph, and the "finally" lands on the combined model and its numbers. The
contrast between the two models is stated as "just the opposite": ARIMA takes
the linear part, LSTM the non-linear part. The paper likes this mirror. It uses
it again in the memorandum.

The quantitative payload is exactly two numbers, RMSE 0.0342 and MAPE 0.36,
placed at the end of the paragraph where the claim "almost overlap with the
real results" would otherwise be bare. The numbers replace the adjective. Note
the grammar is left rough: "with RMSE and MAPE were 0.0342 and 0.36" mixes
"with" and "were". Kept as printed. The same two numbers reappear in Table 1 on
page 9, so the summary and the table agree here.

### Paragraph 3 — the dynamic-programming strategy and its dollar result

"Second, to develop the strategy, we used the dynamic programming method to
split the five-year-long investment strategy problem into smaller problems of
daily investment decisions. After programming using MATLAB, we calculated the
value of the initial money as $374,563.25 on 9/10/21 and discounted this value
to five years ago to obtain $360,595.32, which means that the value of
$374,563.25 on 9/10/21 is equivalent to the value of $360,595.32 on 9/10/16.
This results in a return of 37456.33%."

The move is method, tool, then three numbers. "Second" ties it back to Model I
even though the model was not numbered in paragraph 1. The order inside: the
method and what it does (split a long problem into daily ones), the tool
(MATLAB), the terminal dollar value, the discounted dollar value, a sentence
that restates the discount in words, then the percentage. The habit is to give
the dollar figure twice, once as a result and once translated into a date, so
the reader sees which number belongs to which day. The percentage comes last,
as the punch line.

The numbers conflict with themselves and this is recorded, not fixed. 374,563.25
divided by 1,000 is 374.56, so a return near 37,356% would follow from the
dollars, but the paragraph prints 37456.33%. Page 11 prints the same result as
3745.63%. Neither percentage equals the dollar ratio. Both are kept.

### Paragraph 4 — Model II, the four genes, then its dollar result

"For Model II, we decided to use genetic algorithm to improve the original
strategy as we found many opportunities were missing. We created 4 genes,
namely trading portfolio, trading frequency, buying strategy, and selling
strategy, hoping to improve our strategy from these four dimensions. After
MATLAB solving, we learned that the initial capital was valued at $442,697.25
on 9/10/21 and after discounting it was $426,188.16, creating a total yield of
44269.73%, an annualized return of 338.08%."

Parallel to paragraph 3, which is the point. Model I got method then dollars;
Model II gets reason, then the four genes named, then dollars, then two
percentages. The opening gives the motive in a subordinate clause, "as we found
many opportunities were missing", so the improvement is justified before it is
described. The four genes are given as a "namely" list of four, and the
paragraph immediately says "these four dimensions", tying the list to a count.
The tool is named the same way as in paragraph 3, "After MATLAB solving", a
short clause that signals the result is coming.

The same number conflict appears. 442,697.25 divided by 1,000 is 442.70, so the
dollars say about 442 times, but the paragraph prints a total yield of
44269.73% and an annualized return of 338.08%. Page 15 prints the five-year
total return as 44,169.70% with the same 338.08% annualized. The percentage and
the dollars disagree by roughly a hundred times. Kept as printed. Also kept:
the stray space in "44269.73% ,an".

### Paragraph 5 — optimality shown two ways

"Again, we demonstrate that our strategy is optimal in two ways, one by
changing the strategy itself and the other by observing different market
environments. To change the strategy, we reset gene4 in the genetic algorithm.
After running the results, we found that the yield after the change was reduced
to 273%. To observe the strategy performance in different market environments,
we extracted the bull, bear and oscillator markets that existed in five years,
using bitcoin trading as an example. Comparing the strategy performance and the
market performance during the periods respectively, we again find that the
strategy outperforms the market performance by a wide margin."

The move is a claim of optimality, then two proofs in the order just announced.
"in two ways, one by ... and the other by ..." is the frame, and the paragraph
then spends one or two sentences on each way, in the same order. This
announce-then-follow order is the paper's steadiest habit. The first proof is a
single number: resetting gene4 drops the yield to 273%. The second proof has no
number; it names the three market types and ends on a qualitative comparison,
"outperforms the market performance by a wide margin". So one proof is a
number and the other is a judgment, and the paragraph does not pretend
otherwise.

"Again" at the start and "we again find" near the end echo each other. The
paper uses "again" to mean the conclusion was reached a second time, not as an
empty filler. Printed as-is: "oscillator markets" where the definitions section
says "oscillating market", and the 273% that is never reconciled with the
44269.73% yield. Page 17 to 18 prints the same drop as "reduced from 442% is
reduced to 273%".

### Paragraph 6 — the memorandum, a promise of contents

"Finally, we wrote a memorandum to investors detailing our modeling process,
introducing our strategy, analyzing the strategy results, and informing about
the risks and shortcomings of the strategy."

One sentence, four participles in a row: detailing, introducing, analyzing,
informing. The move is to close the summary by pointing at the communication
artifact and listing what it contains, in the order the memorandum itself will
follow. No numbers. "Finally" is the only sequence word in this paragraph, and
it closes the page.

### Keyword line

"Keywords: ARIMA-LSTM Model, Dynamic Programming, Genetic Algorithm". Three
items, which are the three methods, not the two model names. The keywords name
the techniques; the paragraphs named the models. Both are kept.

### What the summary teaches about the writing

The page runs on a repeated block even though it never writes "For task N".
The block is: model name, what it does, the tool, the dollar result, the
percentage. Paragraphs 3 and 4 are the same block twice. Paragraph 2 is a
variant that ends in error numbers instead of dollars. The sequence words are
few and plain, "Second", "Again", "Finally", and the model labels carry the
structure. Results are given as dollars first and a percentage last, with the
discount explained in a "which means" clause so the reader can match each
dollar to a date. Where the prose would be an unsupported adjective, a number
is put in its place, as in paragraph 2. Where there is no number, the paragraph
says so by staying qualitative, as in the second half of paragraph 5.

## Introduction

Physical page 3. Three numbered subsections, 1.1, 1.2, 1.3. The subsection
titles do the organizing: background, restatement, our work.

### 1.1 Problem Background — three paragraphs

Paragraph 1. "In real world of finance, all buying and selling behaviors are
based on people's expectations for the future, so how to predict the future
price of assets as accurately as possible has become one of the most important
research contents in finance. The more accurate the investor's prediction of
asset prices, the easier it is to achieve higher expected returns."

Two sentences. The move is background that arrives at the paper's topic. The
first sentence has the shape "scene, so question", where the "so" turns a fact
about behavior into the research problem. The second sentence is a "the more
..., the easier ..." pair that states why the problem is worth solving. No
citation, no number. The habit is to derive the research question from a stated
fact with "so", rather than announce it.

Paragraph 2. "Of course, it is rogue to talk about returns without risk.
Theoretically, in the market, varieties with higher risk tend to have greater
profit. In order to adapt to people's different risk preferences, a wealth of
financial products have emerged. Among them, Bitcoin is favored by investors
due to its limited total amount, safety, free transaction, wide circulation
range and so on. However, due to high price volatility of bitcoin, gold, which
is considered as a safe-haven capital, is paired with it to form an investment
portfolio."

Five sentences. The move is a concession, then the two assets and why they are
paired. "Of course" concedes the obvious objection, that return without risk is
meaningless, and "it is rogue to" is a blunt colloquial judgment the paper is
willing to print. Then "Theoretically" lifts the next sentence into a general
rule. "In order to" gives the reason the products exist. "Among them" narrows
from all products to Bitcoin, with a list of reasons ending "and so on", an
open list rather than a closed one. "However" turns to the drawback, volatility,
and answers it by pairing gold, "a safe-haven capital". The order is objection,
rule, reason, the risky asset, its flaw, the hedge. The "However" does real
work: it introduces the second asset as the remedy for the first asset's flaw.

Paragraph 3. "The 'best daily trading strategy' described in the subject must
have a specific measurement. It is often said in finance that if investor A is
a risk averter and investor B is a risk seeker, we cannot consider investor B's
strategy to be superior one even if investor A's return is lower than B's
return. Therefore, in this question, our strategy must be based on a given risk
preference so that our strategy comparable."

Three sentences. The move is to pin down what "best" means, and it does it with
a saying, then a conclusion. "It is often said in finance that" introduces a
set piece, the risk-averter against the risk-seeker, used to show that a higher
return does not by itself make a better strategy. "Therefore" draws the
consequence: the strategy needs a fixed risk preference. This paragraph is the
bridge to Assumption 1 on page 4, which chooses the risk-seeker. The writing
habit is to state a proverb-like example with "it is often said", then cash it
out with "Therefore". Printed as-is: "superior one" and "so that our strategy
comparable", both missing words, both kept.

### 1.2 Restatement of the Problem — one lead sentence, four bullets

"Considering the background information and restricted conditions identified in
the problem statement, we need to solve the following problems:"

Then four bullets, each a task:

- "If you have $1000 on 9/10/2016, with known historical prices of the asset,
  create a model to make an optimal strategy, calculate how much is it worth on
  9/10/2021."
- "Prove that your strategy is optimal in different situations."
- "Perform a sensitivity analysis of strategy results between trading costs and
  derive how trading costs affect strategy and investment results."
- "Writing a letter with traders to summarize your strategy, model, and trading
  results."

The lead sentence credits the problem statement and then announces a list. The
four bullets are the four required outputs, in the order background, optimality,
sensitivity, letter. They are not parallel in grammar: the first three are
imperatives (create, prove, perform) and the fourth slips into a gerund,
"Writing a letter". The paper does not smooth this. The first bullet is the
only one with numbers, the two dates and the 1000 dollars, because it is the
only task that states the scenario. The other three name an action and an
object. This is the task routing for the whole paper: section 5 and 6 answer
the first, section 7 the second, section 8 the third, section 9 the fourth.

### 1.3 Our Work — one sentence and a figure

"The flow chart of our idea is shown in Figure 1."

One sentence. The move is to hand the reader to a figure instead of describing
the plan in prose. The subsection promises "our work" and delivers a picture.
There is no preview of later chapters in words. The figure carries the work
plan, and the sentence only points at it.

## Habits gathered here, for reuse

These are the routines this paper actually uses in its summary and
introduction, named so they can be applied later without copying the sentences.

- Scene, then "so", then the research question. A fact about the world is
  turned into the problem by a single "so", with no citation. Seen in 1.1
  paragraph 1.
- Concession first. "Of course" plus a blunt judgment grants the objection,
  then the paragraph answers it. Seen in 1.1 paragraph 2.
- "However" as a remedy, not a contradiction. It introduces the second asset as
  the fix for the first asset's stated flaw.
- A proverb cashed out. "It is often said ... that" sets up an example, and
  "Therefore" states what follows for this paper. Seen in 1.1 paragraph 3.
- Announce, then follow in the same order. "in two ways, one by ... and the
  other by ..." and then one sentence block per way, in that order. Seen in
  summary paragraph 5.
- The model block. Model name, what it does, the tool, the dollar result, the
  percentage last. Used twice in the summary, once per model.
- Dollars before percentage, with a "which means" clause that ties each dollar
  to a date, so the discount is explained rather than left as a bare second
  number.
- A number where an adjective would be unsupported. "almost overlap" is
  followed at once by RMSE and MAPE. Where no number exists, the sentence stays
  qualitative instead of inventing one.
- A short tool clause as a hinge. "After programming using MATLAB" and "After
  MATLAB solving" sit between the method and the result.
- An open list. Reasons for an asset end with "and so on" rather than a closed
  count.
- Sequence words are few and plain: first, Second, finally inside a paragraph,
  and Second, Again, Finally across paragraphs. The labels "Model I" and
  "Model II" do more organizing than the sequence words.
- A closing that points outward. The last summary paragraph is four participles
  listing what the memorandum contains, and the last introduction subsection is
  one sentence pointing to a figure.

## Printed defects kept, not fixed

Recorded here so later gates do not silently repair them.

- "Nowdays" and "profiteers" in summary paragraph 1.
- "with RMSE and MAPE were 0.0342 and 0.36" in summary paragraph 2.
- The dynamic-programming return is 37456.33% in the summary and 3745.63% on
  page 11, and neither matches the dollar ratio of 374,563.25 to 1,000.
- The genetic-algorithm total yield is 44269.73% in the summary and 44,169.70%
  on page 15, against a dollar ratio near 442.70, with the annualized return
  338.08% in both places.
- The optimality drop is "reduced to 273%" in the summary and "reduced from
  442% is reduced to 273%" across pages 17 and 18.
- "oscillator markets" in the summary against "oscillating market" in the
  definitions.
- "superior one" and "so that our strategy comparable" in 1.1 paragraph 3.
- The fourth task bullet is a gerund, "Writing a letter", against three
  imperatives.
