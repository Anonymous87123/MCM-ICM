# L7 spot check — lane D

Sample: 30 rows drawn at stride 176 from 5308 rows in `quotes-d.jsonl`.

A row is flagged `suspect` when its ladder level is a partial match (`span`, `gapped`, `unverified`, `layout-only`, `ocr-only`, `text-gap`) or when the quote does not end on sentence punctuation. Flagged rows are the ones worth a second read.

| # | paper | chapter | block | job | level | quote |
|---|---|---|---|---|---|---|
| 1 | P-D-2015-34985-c7be0d8b | abstract | 0 | define | exact clean | Our team’s objective was to find a way to model sustainability of a country, and then use our model and research to create a 20year sustainable dev… |
| 2 | P-D-2016-44173-aa1c9913 | results | 0 | check | exact **suspect** | 5.3 Sensitivity Analysis and Model Validation |
| 3 | P-D-2017-55295-9001b6d9 | model-improvement | 15 | check | exact clean | The robustness of the queueing networks improves when suspicious passengers pass the system. |
| 4 | P-D-2017-67316-f37f83c8 | model-improvement | 21 | interpret | exact clean | We ﬁnd the partial priority discipline is also eﬀective in raising passenger satisfaction. |
| 5 | P-D-2018-73156-1a30e830 | model-establishment | 30 | derive | exact clean | The biggest difference between destination charging (DC) and supercharging (SC) lies in the charging efficiency. |
| 6 | P-D-2018-78826-ed3ee7b7 | model-improvement | 3 | mechanism | exact clean | Second, we consider the impact of autonomous vehicles. |
| 7 | P-D-2018-81402-e1ca1921 | model-establishment | 17 | define | exact clean | We need to do is find the best profit between two situations : more EV and more charging piles. |
| 8 | P-D-2018-82504-6cc63169 | results | 31 | mechanism | exact clean | As Ona Egbue and Suzanna Long stated in their article, "Consumer accep- tance is important as it is key to the commercial success (or failure) of E… |
| 9 | P-D-2018-82794-47f05792 | results | 20 | read-figure | exact **suspect** | urban areas suburban areas rural areas destination charging stations 0.7 0.2 0.1 |
| 10 | P-D-2019-1902407-b8153b5d | model-establishment | 1 | define | unverified **suspect** | Set all exhibition halls, node are S{S1, S2, S3, S4 ... }; |
| 11 | P-D-2019-1908810-3e19ea18 | model-establishment | 49 | define | squeezed clean | The non-negativity function, n(ρu) is a function such that nu(0) = 0 and nu(1) = 1 with 0 ≤n(ρu) ≤1. |
| 12 | P-D-2019-1922748-25e53f6c | conclusion | 0 | limit | exact clean | Firstly, the Ford-Fulkerson algorithm has certain limitations. |
| 13 | P-D-2020-2003723-28f692ff | results | 6 | compute | exact clean | Of the 76 data, only 3 were predicted incorrectly, with an accuracy of 96.1%, which also proves the validity of the model. |
| 14 | P-D-2020-2013140-d02fd0c3 | abstract | 5 | ext:claim | exact clean | Finally, we extended the model to other real-life team collaboration scenarios. |
| 15 | P-D-2020-2013245-e4e7ae08 | results | 6 | route | exact clean | Performance indicator is often valuable in a whole soccer game. |
| 16 | P-D-2020-2022868-71331b90 | conclusion | 3 | interpret | exact clean | The metrics that may still be worth considering include largest eigenvalue of the network, closeness centrality, and network centralization. |
| 17 | P-D-2021-2100242-a505be5b | model-establishment | 19 | check | exact clean | In order to make the data of music vector can be compared, we need to normalize the data. |
| 18 | P-D-2021-2101855-c4682962 | results | 27 | read-figure | exact **suspect** | Figure 7: Total Similarity between Pop/Rock and Other Genres |
| 19 | P-D-2021-2106028-e54d016e | conclusion | 0 | interpret | exact clean | Fifth, we observe revolutionary in the 1960s and discover that Nat King Cole and The Beatles represents this revolutionary. |
| 20 | P-D-2021-2121604-9d9314bb | data-preprocessing | 0 | derive | exact clean | To smooth the modelling process, we remove all artists who could not be located in a certain category in the data set inﬂuence_data. |
| 21 | P-D-2021-2124497-1be43b7c | results | 21 | read-figure | gapped **suspect** | Amplitude of the FFT result (b) Phase of the FFT result |
| 22 | P-D-2022-2208928-f4cfe761 | assumptions | 1 | define | exact clean | Assuption: The data we collect is precise. |
| 23 | P-D-2022-2215444-cd948920 | algorithm | 3 | define | exact clean | Different index values correspond to different maturity levels, that is, three influencing factors and one affected factor. |
| 24 | P-D-2022-2224178-5906c8e3 | model-improvement | 0 | route | exact **suspect** | I1, I5, T4, T7, A2, A7 5 Model 3: Stochastic Petri Net for the Port Logistics Optimiza- |
| 25 | P-D-2023-2303967-354e9177 | model-establishment | 3 | mechanism | exact clean | In the SDG Network, all goal nodes are interconnected. |
| 26 | P-D-2024-2417004-a737e95b | abstract | 3 | ext:claim | exact **suspect** | First, a basic network model connecting the five lakes was established to |
| 27 | P-D-2024-2417831-f399a6df | model-establishment | 50 | define | exact clean | It means they deploy proportional control based on the difference between the Lake Superior water level and the target level. |
| 28 | P-D-2024-2419588-1cc62ede | sensitivity-analysis | 1 | interpret | span **suspect** | precipitation, adjusting outflows to mitigate potential flooding. However, the reaction time to sudden, heavy rainfall events highlighted a need fo… |
| 29 | P-D-2025-2504188-db12259e | model-improvement | 1 | define | squeezed **suspect** | 푑represents the service radius of the bus station, which is 0.3 km here. 푆푠푒푟푣푖푐푒 |
| 30 | P-D-2025-2516219-17e4e820 | data-preprocessing | 1 | select | exact **suspect** | Due to data collection reasons, there are definitely outliers and missing values |

Flagged rows: 10 of 30.
