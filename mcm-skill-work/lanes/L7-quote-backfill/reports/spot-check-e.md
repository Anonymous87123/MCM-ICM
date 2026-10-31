# L7 spot check — lane E

Sample: 30 rows drawn at stride 167 from 5024 rows in `quotes-e.jsonl`.

A row is flagged `suspect` when its ladder level is a partial match (`span`, `gapped`, `unverified`, `layout-only`, `ocr-only`, `text-gap`) or when the quote does not end on sentence punctuation. Flagged rows are the ones worth a second read.

| # | paper | chapter | block | job | level | quote |
|---|---|---|---|---|---|---|
| 1 | P-E-2016-43443-82025ab9 | abstract | 0 | route | exact clean | In this paper, we formulate an “excess water ratio” (EWR) metric for water scarcity that improves upon currently used metrics such as the Water Str… |
| 2 | P-E-2016-49630-af20ebac | results | 32 | mechanism | exact clean | 1. |
| 3 | P-E-2016-52849-d6e64df0 | references | 0 | source | exact **suspect** | “Wicked Problems Demand Adaptive Responses: How Does the Murray |
| 4 | P-E-2017-61502-f0a50d47 | conclusion | 0 | interpret | exact clean | In order to support the growth of a 50% increase in population, initiatives focus on the development of amenities for citizens. |
| 5 | P-E-2017-67171-0a99e096 | model-establishment | 5 | interpret | exact clean | This term represents whether the direction of current growth is close to smart growth or not. |
| 6 | P-E-2017-68242-753e0037 | results | 48 | interpret | exact clean | The planning department will prefer to make full use of land and develop more ways of public transportation. |
| 7 | P-E-2018-72968-5f2ee223 | model-establishment | 44 | source | exact clean | We prioritize the indicators and employ AHP to get the coefficients for every indicator. |
| 8 | P-E-2018-74971-2b1f503a | problem-restatement | 5 | route | exact clean | Sensitivity analysis and model evaluation. |
| 9 | P-E-2018-78511-395a90c3 | model-establishment | 49 | derive | exact clean | The stability only relates to the migration of people and completeness of the law, which is similar to what we have discussed for the security. |
| 10 | P-E-2018-88902-cefa4db9 | model-establishment | 64 | define | exact clean | which means to simply sum over all the variables not involved in the query. |
| 11 | P-E-2018-93840-dffa6997 | model-establishment | 9 | route | exact clean | Next step, we de ne all parameters and the techniques of processing relevant data. |
| 12 | P-E-2019-1902029-f44b44ca | results | 43 | define | exact clean | Where:I(∇Ak > 0) and I(∇Ak < 0) are characteristic functions of ∇Ak. |
| 13 | P-E-2019-1902917-3fb00373 | results | 7 | compute | exact clean | After consulting the data, we learn that the construction cost of a small paper mill is about 2 million yuan and the average production cost of pap… |
| 14 | P-E-2019-1903455-a52f7980 | results | 30 | read-figure | exact clean | Figure.12 The curve of benefit-cost ratio over time of four project. |
| 15 | P-E-2020-2008521-e040e3b4 | model-establishment | 24 | define | exact clean | Air Condition is evaluated based on two aspects: contributions to global warming and emission of noxious gas. |
| 16 | P-E-2020-2010035-cf1cc4f2 | model-establishment | 56 | derive | exact **suspect** | We assume the growth rate of removal to be linear and their equations. bocean, bland in Equation 20 are constants that describe the exact growth ra… |
| 17 | P-E-2020-2016287-6ed5334f | results | 8 | define | exact **suspect** | More specifically, we consider humans to be on the top of n food chains with |
| 18 | P-E-2020-2021103-996a6655 | model-establishment | 2 | limit | exact clean | Assumption: Seabird population S(t) is a useful proxy for estimating global marine envi- ronmental health at time t. |
| 19 | P-E-2021-2102057-3e6906e7 | results | 7 | read-figure | exact **suspect** | 10.3 Conclusions for Finnish Food System |
| 20 | P-E-2022-2202171-2ac7357e | abstract | 6 | handoff | exact clean | In addition, we explore the transition strategy of extending the logging interval by 10 years to ensure the growth of the forest and meet the deman… |
| 21 | P-E-2022-2202838-75410db9 | results | 7 | compute | exact **suspect** | According to the problem restatement, we will allow logging for 10 years longer than the current practice, that is to add 10 to the |
| 22 | P-E-2022-2216618-127926c7 | notation | 1 | define | span **suspect** | Primary recovery rate of the wood material of the ith product Weighted factor of carbon sequestra- tion within products Deforestation rate/Proporti… |
| 23 | P-E-2022-2220714-2e6b46c5 | conclusion | 1 | interpret | exact clean | We combine the ecological, economic and tourism values of forests, and establish an evaluation model of forest value utilization rate on the basis … |
| 24 | P-E-2023-2301428-46c8d86f | introduction | 6 | compare | squeezed clean | ♦Finally, the effects of light pollution on biological populations have both macroscopic and microscopic dimensions. |
| 25 | P-E-2023-2307336-5797f8da | model-establishment | 15 | derive | exact clean | After the development of new lamps, they will replace fluorescent lamps. |
| 26 | P-E-2023-2314354-42336b14 | abstract | 1 | define | exact **suspect** | First, we identified four primary indicators: traffic, ecology, energy and society, and set several |
| 27 | P-E-2023-2320131-a457a41e | model-establishment | 12 | source | exact **suspect** | is determined by the type of region that is in the |
| 28 | P-E-2024-2401102-4ea16839 | results | 10 | interpret | exact clean | In the case of Australia, the model opts for the lowest-risk option, WA, over VIC, which exhibits significantly higher risk compared to other areas. |
| 29 | P-E-2024-2410578-d7df14d8 | model-improvement | 2 | derive | exact **suspect** | In the MDI model, based on the analysis above, property developer decisions |
| 30 | P-E-2025-2502355-f89a99dc | model-establishment | 1 | define | exact **suspect** | Where, R : Growth rate of the producer; K : Environmental carrying capacity of the pro- |

Flagged rows: 10 of 30.
