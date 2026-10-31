# L7 spot check — lane C

Sample: 30 rows drawn at stride 346 from 10397 rows in `quotes-c.jsonl`.

A row is flagged `suspect` when its ladder level is a partial match (`span`, `gapped`, `unverified`, `layout-only`, `ocr-only`, `text-gap`) or when the quote does not end on sentence punctuation. Flagged rows are the ones worth a second read.

| # | paper | chapter | block | job | level | quote |
|---|---|---|---|---|---|---|
| 1 | P-C-2010-6947-c5305f34 | abstract | 0 | interpret+close:handoff | exact clean | After mathematically analyzing and modeling the ocean problem, we would like to present our conclusions and recommendations in order to determine t… |
| 2 | P-C-2011-11325-4609137d | model-establishment | 4 | mechanism | nfkc clean | The proposed initial infrastructure investment will directly aﬀect the ini- tial conditions of the model. |
| 3 | P-C-2011-9089-838e50df | strengths-limitations | 1 | ext:claim | exact clean | 3.3 Data Envelopment Analysis We use DEA to make assessment on EV’s social effects. |
| 4 | P-C-2012-15356-6b8f0a28 | results | 1 | compute | exact clean | By iterating the iRank function 1000 times, we obtain the following results. |
| 5 | P-C-2013-21165-17e64d15 | model-establishment | 7 | select | exact clean | The BP model, however, has a major setback of slow convergence. |
| 6 | P-C-2014-28199-d39873d7 | strengths-limitations | 5 | ext:claim | exact clean | High practicability. |
| 7 | P-C-2014-31262-1f9007fa | model-establishment | 22 | define | exact clean | (5) where j is an arbitrary pair disconnected vertices in the set S. |
| 8 | P-C-2015-33900-7f8065e8 | model-establishment | 53 | define | squeezed clean | where TCall is for overall recruiting costs, Nj represents a node of level j, Nodes indicates the set of all nodes, and MTj is the median training … |
| 9 | P-C-2015-37284-dee063ba | introduction | 3 | route | exact clean | In section 3, considering the relation among people without the influence of positions, we first build a network among people and define two indice… |
| 10 | P-C-2016-42939-5fccbebc | model-establishment | 5 | derive | exact clean | As the model assumes the performance index is a linear composition of all performance indicators, all we need to do is determine the weights of the… |
| 11 | P-C-2016-50193-615bc62f | strengths-limitations | 6 | limit | exact **suspect** | Simplifying Assumptions : Simplifying assumptions had to be made in order to |
| 12 | P-C-2017-55278-a011d0e2 | conclusion | 13 | handoff | exact clean | We believe our model is useful for management of self-driving cars in the future. |
| 13 | P-C-2018-72969-f2349d15 | model-establishment | 38 | read-figure | span **suspect** | GP R Pr edic tion To predict To predict |
| 14 | P-C-2018-80560-ad2eea75 | problem-analysis | 27 | route | exact clean | Energy structure depends excessively on a stateâAZs population, economy and industry. |
| 15 | P-C-2019-1900577-7ac4ae90 | conclusion | 15 | handoff | exact clean | Begin programs to help recovering addicts, similar to the Chinese Clean Needle exchange. |
| 16 | P-C-2019-1906204-4e0a421c | model-establishment | 4 | read-figure | exact **suspect** | Figure 4: Model overview |
| 17 | P-C-2020-2002116-f6f4a15a | model-establishment | 25 | derive | exact clean | Then we change the candidate words or the seed words into probability vector representa- tions. |
| 18 | P-C-2020-2004647-771d613e | model-establishment | 15 | route | exact **suspect** | Deﬁnition of Φ—the Review-quantifying Vector |
| 19 | P-C-2020-2010638-c32c8549 | model-establishment | 10 | define | exact **suspect** | We apply the methods of correlation analysis on the percentage of helpful |
| 20 | P-C-2021-2101587-8b253851 | introduction | 9 | route | exact **suspect** | predict how the hornet may spread its colony |
| 21 | P-C-2021-2107815-45f0e8ba | results | 48 | define | exact clean | According to the established model, we define a variable 𝑅𝑛𝑜𝑤 representing the distance between the location of the new "positive ID" and the start… |
| 22 | P-C-2021-2109298-1a718172 | model-establishment | 101 | route | exact clean | probability score. |
| 23 | P-C-2022-2200688-b6248fa6 | model-establishment | 15 | derive | span **suspect** | we can define the following equation: δ= (a1, b1, ..., aI, bI)T (8) |
| 24 | P-C-2022-2208834-e1b081c3 | memo | 11 | compute | exact clean | It is found that after using our trading strategy, through the diﬀerent conversion and multiple buying and selling operations of two diﬀerent ﬁnanc… |
| 25 | P-C-2022-2229059-dacff43d | model-establishment | 4 | define | exact clean | Bitcoin is a highly volatile asset, and is subject to large jumps in price. |
| 26 | P-C-2023-2310767-2f955db2 | abstract | 3 | compare | exact clean | For task 3, we select seven additional word attributes to measure the words’ diffi- culty level, and then downscale the metrics by principal compon… |
| 27 | P-C-2023-2318036-f96be15e | data-preprocessing | 1 | compute | exact clean | We also checked the sum of the percentages of each distribution and found that the sum of question 281 ”nymph” on 2022/3/27 was 126, which is likel… |
| 28 | P-C-2024-2401445-6a882749 | appendix | 0 | define | span **suspect** | Appendix A Indicators Chosen for Training Random For- |
| 29 | P-C-2024-2425454-a27c2efc | data-preprocessing | 2 | compute | exact **suspect** | Tag Encoding of String Type Data |
| 30 | P-C-2025-2510862-925774c8 | sensitivity-analysis | 0 | check | exact **suspect** | 9.1 Tests of the stacking model |

Flagged rows: 10 of 30.
