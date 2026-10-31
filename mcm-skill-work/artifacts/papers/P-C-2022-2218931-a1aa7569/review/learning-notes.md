# Paper 229 — G1 Summary and Introduction

Paper: P-C-2022-2218931-a1aa7569. Team 2218931. 2022 Problem C. Title on the summary sheet: "Finding the Best Strategy with Quantitative Models".

Printed page scheme: the header reads "Page N of 25" and the contents entries land on those same physical pages, so printed page N is physical page N. The summary sheet has no page number.

## Summary (physical page 1)

Five visual paragraphs plus a keywords line. 501 words on the page, header included. No equation, no figure, no table, no citation. Numbers carried: 0.99, seven days, five days, seven days, the next day, the first ten days, 2%, 3%, 3.5%, 4.5%, $1,000, five years, $270,836.

### Paragraph 1 — stakes

"Market traders seek to maximize returns through frequent buying and selling activities. However, financial markets are complex and volatile, and it is not easy to achieve their goals by relying only on experience to determine trading strategies. Quantitative trading methods make the path to return precise and reliable by building a reasonable model."

Move: stakes, then the obstacle, then the remedy. Three sentences, and the turn sits in the second one, opened by "However". The first sentence gives the actor and the goal with no number. The second names why experience fails: markets are "complex and volatile". The third offers the method class, not the model. "the path to return" is the phrase doing the selling; nothing is quantified yet.

Voice is third person for the traders, then an impersonal claim. Present tense throughout. No hedge word: "make the path ... precise and reliable" is stated flat.

### Paragraph 2 — scope and task routing

"We constructed model I: LM-BP Neural Network Model and model II: Recurrent Decision Model. The two models are closely linked and constitute the final Quantitative Trading Decision Model, which is used to help traders determine the best decisions for a portfolio consisting of cash, gold, and bitcoin."

Move: name both models, then say how they join. The numbering is "model I" and "model II" with a colon and a capitalised name, not "For Problem n". The second sentence does the handoff: linked, then the combined name, then the user and the three assets. No number, no result.

"We constructed" is past and active. "is used to help" drops back to present passive. The portfolio contents are listed last, which is where the reader learns the scope.

### Paragraph 3 — method, model I

"For model I: We use the Levenberg-Marquardt algorithm based on numerical optimization to improve the traditional BP neural network. The model uses valid historical price data for seven days to make long-term and short-term price forecasts. Subject to trading rules, the long-term forecast for gold is five days after the day; the long-term forecast for Bitcoin is seven days after the day. Both short-term forecasts are for the next day. We tested the model with historical price data, and its R2 exceeded 0.99, and the predictions worked well."

Move: the repeated block "For model n". Inside it the order is algorithm, input window, forecast horizons, then the test result. Five sentences. The horizons are given as a pair split by a semicolon, gold first, bitcoin second, and the short horizon is pulled out into its own sentence because it is shared. The result sentence chains three clauses with "and": what was tested, the number, the plain verdict "worked well". The number replaces the adjective; "worked well" only restates it.

"We use" is present. "We tested" and "exceeded" and "worked" switch to past for the one sentence that reports a finished test. "Subject to trading rules" is the only qualifier, and it governs the horizons, not the accuracy claim.

### Paragraph 4 — method, model II

"For model II: The core idea of the circular decision model is to execute a "buy low, sell high" strategy based on the future price trend of an investment product. It consists of four stages: "Stand by", buy, hold and sell. No decisions are made for the first ten days to accumulate historical price data; buy them if there is an uptrend in the short or long term and reach a threshold. Threshold settings are related to transaction costs and expected returns. The short-term and long-term thresholds are 2% and 3% for gold and 3.5% and 4.5% for Bitcoin. We use the Sharpe ratio to measure the riskiness of a portfolio and use it to determine the purchase share of each product in the portfolio. Sell them if both short-term and long-term forecast price declines. Account funds should be updated after each transaction is completed."

Move: same "For model n" frame, but this one carries the rules instead of a test. Eight sentences. Order: the idea in one quoted phrase, the four stages, the waiting rule, the buying rule, what the thresholds depend on, the four numbers, the risk measure and what it decides, the selling rule, the bookkeeping rule.

Note the naming slip: the heading calls it "Recurrent Decision Model" and this paragraph says "circular decision model". Both stay, since the summary itself uses both.

The thresholds arrive as one sentence with two pairs, gold then bitcoin, short then long inside each pair. No derivation here; "are related to" is all the justification the summary gives. The buying and selling rules are bare imperatives with no subject: "buy them if", "Sell them if". "should be updated" is the only modal, and it is about accounting, not about the strategy.

### Paragraph 5 — results, routed by problem number

"We can draw the following conclusions after model solving, model checking, and sensitivity analysis. We input historical price data into quantitative investment decision-making models for simulated trading for problem one. The initial capital is $1,000, and after a five-year trading period, the asset value is $270,836. For problem two, the evidence that we make the best decisions is that the model's parameters have been optimized; the investment returns are also higher than simple long-term trading, short-term trading, and some high-performance investment companies. For problem three,we find that both the trading strategy and the trading results are susceptible to the Bitcoin commission payment ratio change and less sensitive to the gold commission payment ratio change."

Move: a one-sentence preamble naming the three checks, then one block per problem. Problem one gets no "For" — it is folded into "for problem one" at the end of the method clause, then its own result sentence. Problems two and three open with "For problem n". So the frame is used three times but the first instance is buried.

The result sentence is a two-clause balance: stake, then value, joined by "and". No return ratio is computed; the dollar figure stands alone. Problem two's evidence is two clauses split by a semicolon: parameters optimized, then returns higher than three named comparators. The comparators stay unnamed beyond their type. Problem three states the sensitivity direction with no number at all, and the sentence is missing its space after the comma.

"We can draw" hedges the preamble. Everything after it is indicative.

### Paragraph 6 — closing

"Finally, we wrote a memo for the trader with our models, strategies, and results. Moreover, the advantages and disadvantages of the model are analyzed."

Move: the deliverable, then the evaluation, in two sentences. "Finally" marks the last task. "Moreover" adds the evaluation as an extra rather than as part of the memo. "we wrote" is past active; "are analyzed" switches to present passive and drops the actor. The three things inside the memo are listed in the same order the summary itself used: models, strategies, results.

### Keywords line

"Keywords: LM-BP long and short term forecast circular decision quantitative investment"

Four noun phrases, no punctuation between them. Repeats the two model names and the forecast split. Not a sentence, so not a language unit.

### Summary layout

Paragraphs: 6, counting the keywords line as its own block. Sentences: 3 + 2 + 5 + 8 + 5 + 2 = 25. Equations 0, figures 0, tables 0, citations 0. Quantitative results: the R2 claim and the terminal dollar value. Rhetorical mix: one stakes paragraph, one scope paragraph, two method paragraphs, one results paragraph, one closing paragraph.

Opening routine: actor, goal, "However" obstacle, method class. Transition routine: "For model I", "For model II", then "for problem one", "For problem two", "For problem three". Closing routine: "Finally" for the memo, "Moreover" for the evaluation.

## Introduction (physical pages 3, 4, 5)

The introduction runs from the section 1 heading on page 3 to the end of section 1.4 on page 5. Page 2 is contents only and is excluded. Figure 2, announced at the end of 1.4, is printed at the top of page 6 and belongs to the flow-chart handoff, not to a new argument.

### Page 3 — 1.1 Problem Background, paragraph 1, with the quotation

A displayed quotation, attributed to "James Simons,the King of Quants": "Looking at the prices, I can see something we can study here, maybe a way to predict, mathematically or statistically. So I built some models, and models got better and better. Finally, the modal replaced the fundamental stuff."

Then: "With the continuous development of deep learning and artificial intelligence, quantitative trading strategies have gradually become mature and accepted by traders. Quantitative trading has gradually emerged since the 1970s. Sharpe's Capital Asset Pricing Model and Ross's Arbitrage Pricing Theory have promoted its prosperity extensively. Although the impact of the financial crisis has not been avoided and there are still model failures, quantitative investment is still necessary and practical. After all, the Medallion Fund operated by Simons has an average annual return of 35%!"

Move: an authority's own words, then a history in four beats, then a concession, then a number. The quotation does the "from prices to a model" jump in the speaker's voice, including the climb "better and better" and the slip "modal" for "model", which is printed as is. The prose after it starts broad — deep learning and acceptance — then dates the field to the 1970s, then names two theories and their authors, then concedes the crisis and the failures with "Although", then answers with "still necessary and practical". The last sentence is the proof, opened by "After all", and it is the only number on the page: 35%, with an exclamation mark. One number, spent on someone else's fund, not on this paper's result.

Tense is present perfect for the development and past for the emergence and the promotion. "has not been avoided" and "there are still" keep the concession in the present.

### Page 3 — 1.1, paragraph 2

"Compared with traditional investment methods that rely on investment experience or analysis of financial data, establishing a suitable forecasting model based on the historical price data of the investment object and quantifying the decision-making method of an effective trading strategy can help traders make trading decisions more conveniently while obtaining higher returns."

Move: contrast, then the proposed method, then the two payoffs. One sentence. "Compared with" fronts the thing being replaced, and the replacement is two gerunds, "establishing" and "quantifying", before the reader reaches the verb "can help". The payoffs are paired by "while": convenience and higher returns. No number. This is the bridge from the field's history to this paper's job, and it names both halves of the later model: a forecasting model, and a quantified decision.

### Page 3 — 1.2 Restatement, preamble

"Through in-depth analysis and research on the background of the problem, combined with topic-specific constraints and requirements given, the restate of the problem can be expressed as follows:"

Move: a one-sentence frame announcing bullets. "Through ... combined with" gives two sources for the restatement, the background and the given constraints. "can be expressed" is passive and modal, and "the restate of the problem" is the printed wording. Nothing follows but the list.

### Page 3 — 1.2, bullet 1

"Develop a Quantitative Trading Decision Model based on the historical price data of gold and bitcoin over the past five years, constrained by trading rules and providing the best daily trading strategy. Note that the model can only be built using the given price data on and before the trading day. That is, when making daily trading strategies, we do not know the future prices of gold and bitcoin."

Move: the task, then a constraint, then the constraint said again in plain words. Three sentences. "Note that" flags the rule, and "That is" restates it without adding anything: the second sentence says which data may be used, the third says the same thing from the trader's side. The repetition is the point — the no-lookahead rule is the one constraint the authors want read twice. Imperative "Develop", then "can only be built", then "we do not know".

### Page 3 — 1.2, bullet 2

"Beginning on September 11, 2016, traders used an initial capital of $1,000 to adjust the investment portfolio consisting of U.S. dollars, troy ounces, and bitcoins according to the decisions given by the Quantitative Trading Decision Model and calculate the investment income after a five-year trading period."

Move: the scenario in one sentence. Order: start date, stake, the three holdings with their units, the model as the source of decisions, the output. "used ... and calculate" mixes past and bare infinitive, printed as is. This is the only bullet that carries numbers, and it carries both of them.

### Page 3 — 1.2, bullet 3

"Present evidence that the parameters in the established model are optimal, and the obtained strategy is the optimal strategy of the model. Prove that our strategy can achieve higher returns than other strategies."

Move: two imperatives, two different claims. The first demands evidence about parameters and about the strategy, joined by "and". The second, "Prove that", demands a comparison and names no comparator. "can achieve" is the only softening. This bullet is what section 5 later answers with the grid search and the five control groups.

### Page 3 — 1.2, bullet 4

"Considering the results obtained above, prepare one to two pages of memorandum to communicate the model and strategy to the trader."

Move: the deliverable, conditioned on the earlier results. "Considering" ties it to bullets 1 to 3. Length is specified as a range, "one to two pages", and the audience and the contents are both named. Imperative, no number.

### Page 4 — 1.3 Literature Review, preamble

"In order to determine the best daily trading strategy, the prices of gold and Bitcoin can be predicted step by step and then combined with the existing investment portfolio strategies to determine the appropriate trading method and establish a quantitative trading decision-making model. The relevant research of the following scholars is for us Provides ideas:"

Move: the plan, then the credit. Two sentences. "In order to" plus the goal, then three verbs in a chain: predicted, combined, establish. The second sentence is the frame for the bullets and is ungrammatical as printed: "is for us Provides ideas". The authors put the citations after a purpose statement rather than before it, so the reading list is justified before it is given.

### Page 4 — 1.3, bullet 1, gold

"The price of gold has the characteristics of dynamic, nonlinear and time-varying. The prediction of the gold price by traditional methods relies on the linear relationship between its prices, which has obvious limitations and low prediction accuracy. Zeng Lian et al. (2010) [1] and Zhang Jundong et al. (2010) [2] used an improved neural network model to achieve high-precision simulation of gold price forecasting. Lin Yu et al. (2010) [3] and Jing Zhigang and Shi Guoliang (2017) [4] adopted an improved ARIMA model, which has higher prediction accuracy than a single prediction model. In recent years, the price prediction model based on LSTM has attracted the attention of scholars. Yuan Dongfang (2021) [5] predicted the price of gold futures based on the CEEMDAN-PCA-LSTM model."

Move: property, then the weakness of the old method, then three waves of cited fixes. Six sentences. The citations come in pairs of the same year first, [1] with [2], [3] with [4], each pair given one shared verdict, and the newest, [5], stands alone after "In recent years". The verdicts escalate: high-precision simulation, higher accuracy than a single model, then mere attention. No number anywhere. The trait list "dynamic, nonlinear and time-varying" is the phrase section 4.1 reuses to justify the neural network.

### Page 4 — 1.3, bullet 2, bitcoin

"Muzammal(2019) [6] found that bitcoin prices are highly volatile, and Wong's(2014) [7] economic analysis shows that the returns are incredibly high. Katsiampa(2017), Selin(2020), Duan(2020) [8–10] forecast Bitcoin price and volatility using traditional time series forecasting methods. Compared with traditional linear statistical models, artificial intelligence methods can better capture the high volatility of Bitcoin prices. Marendra(2018) [11] compared the ARIMA model with the LSTM deep learning model and found that the mean absolute error of the LSTM model was significantly lower. Ciaian(2016) [12] further compared the deep learning model, the autoregressive ensemble model, and the ARIMA model and concluded that the deep learning model performed better in classification prediction."

Move: two facts with citations, then the old method, then the contrast, then two head-to-head comparisons. Five sentences. "Compared with" again fronts the loser. "further compared" marks the second comparison as a continuation of the first. The range citation [8–10] bundles three papers into one sentence, so the bullet spends citations faster than the gold bullet. Still no number; "significantly lower" and "performed better" carry the results.

### Page 4 — 1.3, bullet 3, portfolio decisions

"Quantitative trading relies on computers to configure investment portfolios, which is more scientific and rational than traditional trading decisions. Its quantitative models can be roughly divided into two categories. One is the model based on statistical theory. For example, Zhang Peng (2008) [13] studied the mean-variance and mean-VaR portfolio models when short selling is not allowed and verified the algorithm's effectiveness through empirical research. The other category relies on the development of artificial intelligence technology, such as trading algorithms based on deep reinforcement learning. Xiong Lidong (2019) [14] and Fan Xiaoyu (2021) [15] studied it. They found that the strategy does not rely on complex expert experience, nor does it need to make explicit predictions about the market environment, and can directly output trading strategies its effectiveness."

Move: the claim, the split into two categories, one example each. "One is" and "The other category" is the frame. Each half gets its citation and its virtue: the statistical one "verified ... through empirical research", the learning one "does not rely ... nor does it need ... and can directly output". The last clause, "its effectiveness", is left hanging as printed. The "when short selling is not allowed" detail is the one the authors' own assumption 4 later echoes.

### Page 4 — 1.3, closing

"To more intuitively reflect the research situation of scholars in the field of quantitative trading, we draw Figure 1 based on the content of the literature review."

Move: the figure announcement. "To more intuitively reflect" gives the reason, "we draw" the action, "based on the content of the literature review" the source. One sentence, and it points backward at the three bullets rather than adding a claim. Figure 1 itself is printed at the top of page 5.

### Page 5 — 1.4 Our Work, preamble

"The problem requires building a quantitative trading decision model to achieve the best trading strategy. Our work mainly includes the following:"

Move: restate the requirement, then announce the list. Two short sentences. "The problem requires" puts the demand outside the authors; "Our work mainly includes" brings it back. "mainly" is the hedge.

### Page 5 — 1.4, item 1

"Based on the price data of gold and bitcoin, the LM-BP Neural Network Model is constructed. Use the model's output of the predicted price to build a Recurrent Decision Model. The two constitute a Quantitative Trading Decision Model together, providing the best daily trading strategy."

Move: the pipeline in three sentences. Data, then the first model, then its output feeding the second, then the two joined and what they provide. The handoff is explicit: "Use the model's output ... to build". Voice slides from passive "is constructed" to a bare imperative "Use" to present "constitute". This is the work-plan sentence the later chapters follow: section 4.1 builds the first, section 4.2 builds the second.

### Page 5 — 1.4, item 2

"We prove that our strategy is optimal by optimizing parameters and setting a control group."

Move: the claim and the two methods, in one sentence. "by optimizing ... and setting" names exactly the two moves section 5 makes. No number, no result.

### Page 5 — 1.4, item 3

"Change the commission ratio for gold and bitcoin, and analyze the impact of transaction costs on strategies and results."

Move: two imperatives, the action and the analysis. Names both assets and both things affected, "strategies and results". This is the section 6 preview, and unlike the summary it states no direction and no finding.

### Page 5 — 1.4, item 4 and the figure sentence

"Wrote a memo for traders with our models, strategies and results. In order to avoid complicated description, intuitively reflect our work process, the flow chart is shown in Figure 2:"

Move: the deliverable, then the reason for the figure. "Wrote" is a bare past with no subject. The figure sentence gives two reasons, "avoid complicated description" and "intuitively reflect our work process", then the passive "is shown". Same contents list as the summary's closing: models, strategies, results.

### Introduction layout

Pages 3 to 5. Visual paragraphs and blocks: quotation plus two background paragraphs, one restatement preamble and four bullets, one literature preamble and three bullets and a closing sentence, one work-plan preamble and four items plus the figure sentence. Citations: [1] through [15], all on page 4. Numbers in the whole introduction: 35%, the five years, $1,000, and the dates. One figure announced (Figure 1), one deferred to the next page (Figure 2).

Background moves: quotation, field history, concession with "Although", single-number proof with "After all", then "Compared with" into the proposed method. Restatement moves: frame sentence, then task, scenario, evidence, deliverable, each as its own bullet, with the no-lookahead rule said twice. Literature moves: purpose first, then one bullet per object, each bullet running property, weakness, cited remedy. Work-plan moves: requirement, then four items in the order the paper actually proceeds — forecast model, decision model, optimality proof, cost sensitivity, memo — and a figure to spare the reader the prose.

## Handoff

Section 2 on page 6 takes over with assumptions, each one paired with an explanation. The introduction has already fixed the two model names, the order they are built in, the $1,000 stake, the no-lookahead rule, and the four jobs. Nothing in the introduction states a commission rate or a threshold; those arrive in sections 4.2 and 6.
