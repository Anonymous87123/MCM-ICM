# q224 摘要页核对（未入库）

来源：P-C-2022-2203120-59ecfcb7，2022 年 C 题，24 页。原件 SHA-256 `59ecfcb7486b62c2f39a98de99570928bdffaa5b8f01e561f489c2247ace0978`，与 manifest 一致。文字层 34,323 字符、7,241 词，无空页，24 页全部以 200 DPI 栅格留在 `tmp/q224-extraction-v1`。`visual_review_status` 仍是 pending。本文件只记摘要页，不代表全篇读完。

## 摘要：五段，一段对应一项赛题交付

页 1 代理 `tmp/q224-g0-proxies-v1/p01-summary.jpg`，361,434 字节，四边都有白边，没有裁切。只读复核确认五个作者正文段，标题、Summary Sheet 表头、队号和 Keywords 都不算在内。

1. “It is of great significance for … gold and bitcoin in the past.” 背景段。只说交易者策略不同、收益不同，本篇要做的是基于过去金价和币价的策略。没有数字。
2. “For problem 1, the original data … $ 132089.1078 on September 10, 2021.” 美元符号和数字之间有一个空格，是印出来的。这一段把预处理、ARIMA、相关系数、动态规划、约束和终值按题目 1 的顺序压成一段。
3. “For problem 2, we prove our … model yield can resist inflation greatly.” 用泛化、稳健、收益三方面证明策略最好，再分成保险型、普通型、激进型三种交易者。
4. “For problem 3, firstly, the sensitivity … are decreases correspondingly.” 敏感度被定义成交易频率的变化率。
5. “For problem 4, we summarize the … benefits brought by different trading strategies.” 备忘录段，只预告交付形式，不给新数字。

Keywords 原文：`Keywords: quantitative investment; ARIMA model; dynamic programming`。

这个摘要的信息顺序和 q223 不同。q223 的六段按“模块怎么交接”推进，数字留到正文。这篇把四项赛题交付直接当成四段的骨架，问题 1 的终值在摘要第二段就给了。可学的是“一段只回答一项交付”，不能学的是把终值和相关系数提前写进摘要就当成已经证明。

## 三个印出来的错误，不是提取噪声

- “regular termis” 印在 “assets and risk as the regular termis is established, with the” 里。term 和 is 粘在一起。
- 相关系数那个词印的是 coeffeceents（c-o-e-f-f-e-c-e-e-n-t-s），文字层给出的 coefficeents 是提取结果，以页面为准。前后是 “the price prediction model. Correlation coeffeceents between the prediction results and”。
- “are decreases” 印在 “frequency, asset return and asset risk are decreases correspondingly.” 主谓不一致，原样保留。

另外两处在目录页文字层，还没有用页面复核：`Sensitivity Diﬁnition`、`Assetes`。目录不进作者文风样本，但印刷形式先记着。

## 摘要里的数字，全部是作者陈述

- 黄金、比特币预测与价格的相关系数 0.8592、0.9304。
- 2021-09-10 的终值 $132,089.1078。
- 三种策略的资产 $14,312.6827、$50,040.5474、$132,089.1078。激进型的数和问题 1 的终值是同一个数。
- 黄金交易成本敏感度 0.0422，比特币 0.0658。

这些数没有一个是这里复算的。激进型终值等于问题 1 终值，这个重合只记录，不解释成作者故意。

## 引言前两页已经读到的作者推理

页 3 的 1.2 把组合写成 [C, G, B]，现金、黄金、比特币三件，和题面一致，比 q223 在背景里漏掉现金要干净。1.3 选 ARIMA 的理由是“只需要内生变量、不需要外生变量”，用它不需要什么来选型，而不是宣称它最准。风险的处理在模型之前就给了：比特币波动比黄金大，所以猜它风险更大，再用价格变化的方差去描述。这是先下判断再选度量，判断本身没有检验。

Figure 1 是本队自己的金价、币价图，图注写明来源 London Bullion Market Association 和 NASDAQ，不是外借海报。Figure 2 是总结构图，还没看像素。

## 页 4–9：假设、预测模型和策略模型的文字层

这些页只读了文字层。公式 (3)–(9) 的分式和求和号在提取里是散的，不能当最终抄录，等裁剪复核。

假设五条，每条都短，作者说每条都“adequately justified”，但正文没有给理由：数据真实、投资者身心健康且没有大额贷款、不考虑通胀、交易以美元结算且佣金从支付额里扣、因为只有 1000 美元所以忽略最小交易单位。第二条是这批论文里少见的写法，把交易者的个人状况写成假设。可学的是假设条目短并且每条只限制一件事，不能学的是用“已充分证明”代替证明。

符号表的文字层是乱的，表头印着 Descripition。以页面为准，不从文字层抄符号定义。

预处理有两步。缺失值：黄金只在交易日有价，缺失的用前后两天的均值填。这一步用到了后一天的价格，和题面“只用当天及以前”直接冲突，先记在这里，等看到填补到底用在决策的哪一步再定它的影响。标准化按周期做，`x' = (x - x̄) / SD`，没有说分母为零怎么办。

3.2.1 选 ARIMA 的理由引用了 [2]，说它是过去十年里做混合模型最常用的线性模型。然后拆成三块：AR 用历史值预测自身，式 (1)；差分阶数 d，并说一般一阶就够；MA 累积误差项，式 (2)。紧接着的一句把差分阶数写成大写 D：“where p is the autoregressive term, q is the moving average term, and D is the number of differences”。同一段里 d 和 D 并存，不改。

ADF 检验的表 2 在文字层是齐的：差分前黄金 0.6734、比特币 0.9921，一阶差分后 0.0043、0.0000。作者据此说一阶差分后序列平稳。表 3 的文字层行序是乱的，ARMA 那一行没有自己的 ACF/PACF 描述，等看页面。

定阶结果：黄金 ARIMA(2,1,1)，比特币 ARIMA(2,1,2)。白噪声检验的说法需要留原文：p 值接近 0，因此“服从均值为 0 的正态分布，也就是白噪声”。p 值接近 0 通常表示残差不是白噪声，这句和检验的方向相反。不在这里改写作者的结论，只记下这句话支撑不了它自己的判断。

预测的口径：连续 30 天做训练集，后 3 天做测试集，训练集步长 3。正文把 0.8592 和 0.9304 叫黄金和比特币的“correlation coefficient R²”。摘要里同一对数字叫 correlation coeffeceents，没有 R²。两个名字对同一对数字，都留。

3.2.2 先定义决策系数 R²，式 (3) 是预测值对真实值均值的平方和比上真实值对均值的平方和，但分式线在文字层丢失。命中率 DSi 用预测涨跌方向和真实涨跌方向是否一致，式 (4)。这里 R² 被当作“越接近 1 拟合越好”的决策系数使用，和它作为相关系数的身份混在一起。

交易从 2016-11-12 开始，2016-09-11 到 2016-11-11 被定为第 0 周期，只积累经验不交易。3 天一个周期，共 588 个周期。

风险指标 Sj 是资产在最近 30 个周期上的标准差，式 (5) 文字层散掉了。现金更新式 (6) 的分支条件里出现 `Yg(i+1)` 和 `Yb(i+1)`，即下一周期的价格，用在当期现金计算里。如果这是真实价格，决策就用了未来。式 (7) 的比特币分支文字层写成 `Gi-1 + Bi × wb × (1 - αb)`，黄金的符号 G 出现在比特币的更新里，像是提取串行，必须用页面确认，不凭猜测改成 Bi-1。总资产式 (8)：`Ai = Ci + Gi × Yg(i) + Bi × Yb(i)`。目标式 (9)：`max (Aj - λ × Sj)`，约束的文字层挤成一团，其中看得见 `αg = 1%`、`αb = 2%`、`A0 = 1000`、初始持仓为零。费率用的是题面的 1% 和 2%，这一点比 q223 的扫描区间干净。

这一段的作者推进是：先定周期和预热期，再量化风险，再写现金、持仓、总资产，最后收成一个带约束的目标。顺序本身可学。未来价格是否进入决策、比特币更新是否印错符号，这两件等页面裁剪，不在文字层上做结论。

## 页 10–23：求解、证明、敏感度、结论、备忘录（文字层）

公式 (10)–(18) 和表 5–8 的分栏在文字层是挤的，数字以页面裁剪为准，下面只记文字层已经能读准的句子和作者的推进方式。

### 3.3 求解写成四步，不写成算法伪代码

step1 初始化，step2 算命中率，step3 决定是否交易，step4 决定交易数量。每一步先用一句说这一步要挡住什么，再给公式。step3 的两句挡法是“避免频繁交易带来的过高成本”和“避免交易后现金剩太少”，对应阈值和现金保留比例。这种“先说要避开的坏事，再给条件”是可学的步骤写法，比直接甩流程图干净。

式 (10)(11) 把涨跌阈值写成当期总资产的比例：`eg(i+1) = βg × Ai`，`fg(i+1) = γg × Ai`。式 (12) 的文字层是 `qi = Ci + Gi × Ci / Yg(i) + Bi × Yb(i)`，分子用现金 Ci 而不是黄金持仓，分母是金价，这一行必须用页面确认，不改。

step4 的判断方向和摘要相反：正文说判别系数越小，模型越稳，买入比例可以加大。摘要和 3.2.2 都说 R² 越接近 1 拟合越好。同一指标，一处“大则好”，一处“小则稳”。两处都留，不合并。

式 (14)(15)(16) 三个资产更新在文字层几乎是同一组式子，标签却是 RWHg、RWLg、Rmg。其中 (15) 的标签是 RWLg，用的权重却是 wHg；(16) 的标签是 Rmg，用的权重却是 wLg，而且现金项是减不是加。三式的比特币行都是 `Bi+1 = Bi`，这一步只动黄金。作者在 6.2 自己承认“混合购买策略没有好好考虑”，和这里只动一种资产对得上。`Yg(i+1)` 被正文明确写成“(i+1) 日黄金的真实均价”，所以式 (14)–(16) 用的是已经发生的价格，不是预测。这一点比式 (6) 更硬：求解步骤里的资产重估直接吃下一期真实价格。

### 3.4 结果段先给参数，再给终值

参数一次给全：`βb = 0, βg = 0.5, γb = 0.3, γg = 0.3, wHg = 0.8, wHb = 0.4, q = 0.01`。终值写成 `$132089.11`，交易 9 次，期末 `[C,G,B] = [22.31, 0.16, 2.84]`。摘要里同一终值是 `$ 132089.1078`，多四位小数，美元符号后有空格。两处精度不同，都留。

评价段的三颗子弹几乎原样再出现在 6.1 Strengths：数据要求低、参数表可调、参数范围大所以灵活。结论段没有新句子，是把 3.4.2 的三颗子弹搬过去。这种重复不该学。评价段收束句是 “These ensures the reliability of the results.” 主谓不一致，原样留。

### 4 问题 2 的证明结构

开篇三句把“最优”拆成三件：参数一变收益就变，所以泛化好；参数小变不影响整体策略，所以稳健；比别的投资收益高。然后说“下面分别说明”。这是先给三个判据再展开，可学。不能学的是后文把“收益落在某个范围内”直接写成“因此证明策略最好”。

4.1 用文献 [7] 把交易者分成保险型、普通型、激进型，每型先写目的，再写手段，再写成败概率。保险型要的是长期稳定收入和价差，交易前要掌握足够信息。普通型要短期大利润、愿承担一些风险、靠技术分析。激进型靠运气和机会，风险很高，作者补了一句“除非急用钱、有赌徒心理或有承担风险的能力，多数人不用这种方式”。三型的区分是行为描述，不是参数推导。

表 5 的分栏在文字层串行，βg、γg、γb、wHg 的三列对不齐，等裁剪。表 6 的数字在文字层可读：总资产 14312.68、50040.55、132089.11；持仓三行；交易次数 85、58、9；SD 3861.73、15501.99、40067.35。正文却写 “Reading the data in the table 8”，表号指到备忘录里的表 8，而这里的表是表 6。同一段还说激进型“SD 很大所以风险大”，但表 6 里激进型那一列的 0.24 才是小的，3861.73 排在保险型下面。哪一个数是 SD，文字层对不齐，等页面。图 10 图注印 “traderss”，多一个 s。

4.2 稳健性先用两句定义：扰动不可避免；稳健等于在不确定扰动下仍保持某项性能。然后说扰动 wL、wH、m 后终值落在某范围内，扰动 β、γ、q 也一样，“所以证明我们给的策略是最好的”。从“落在范围内”跳到“因此最优”，中间没有比较对象。这句话是结论越级，记为不能学的收束。

4.3 收益对比先承认纸币发行常超过流通需要，所以有通胀，所以要理财。然后设存款利率 r、通胀率 I、存款额 a，给出 `A = a(1+r−I)^5`。代入 2016–2021 通胀 7%、存款利率 0.5%，1000 美元五年后实际值 $139.2436。三种策略的终值在这里写成 $14312.6827、$50040.5474、$132089.1078，和摘要一致、比 3.4 多两位。对比句是“比更保守的理财行为高出数倍，所以能抵抗通胀”。7% 和 0.5% 没有给来源。开篇这几句粘在一起，没有空格：“inflationso we need to manage money.Under different”“diverse.In reality”“gold ,bitcoin”。印刷粘连原样留。

### 5 敏感度

定义在给公式之前先设场景：α 从 α0 变 K 次（k = 1 到 10），频率从 h0 到 hk。式 (18) 文字层是十分之一乘上 `|hk − hk−1| / hk−1` 的和，再乘 100%。节标题印 “Sensitivity Diﬁnition”，f 印成 ﬁ 连字被提取拆开，目录里同一处也是这个拼法，两处一致，不当提取错误改。

四种扰动写成 a b c d 四条，每条只动一个费率、另一个不动：黄金每次降 0.1%、比特币每次降 0.2%、黄金每次升 1%、比特币每次升 2%。但图 15 的导语又说“黄金成本每次增加 0.1%”，和 c 条的 1% 矛盾。两处都留。

作者读图的三句是编号的，一句一个观察：成本升到一定程度会减少交易次数和总收益；成本升则交易变少、风险变小；三个指标同步同向。然后收成“模型没有忽视这个信号，变化方向符合现实”。这是“先列观察、再给一句判断”的读图写法，可学。判断本身没有给阈值。

表 7：保险型对黄金 0.0267、对比特币 0.2308；普通型 0.0422、0.0658；激进型对黄金 0、对比特币 0.0123。摘要只报了普通型的 0.0422 和 0.0658，没有说这是三种里的哪一种。三条结论：策略对比特币成本更敏感；保险型更敏感于比特币成本、普通型更敏感于黄金成本；激进型对成本整体不敏感。第三条把激进型印成 “radical-tupe”。

### 6 结论与 7 备忘录

6.1 的三颗子弹与 3.4.2 重复，见上。6.2 两条改进都短，一条承认黄金和比特币的混合购买没考虑好，一条承认金融知识不足所以模型未必完善。第二条是自我评价，没有指向具体公式，信息量低。

备忘录抬头：To traders，From Team #2203120，主题 “Investment model, Trading Strategy and Results of Bitcoin and Gold”，日期 February 22, 2022。正文先用一段背景（理财观念普及、虚拟货币掀起 “currency speculation fever”，投资既有收益也有风险），再把策略收成三个问题：when to trade、what kind of assets to trade、how much to trade。这三个问题比正文的 step 编号更像给读者的入口，可学。

三个小标题用的是口语而不是术语：When to trade、Deal what、How much is the deal。后两个不是规范英文，原样留。“Deal what” 一段说比较两种资产的涨跌幅度后决定买哪一种；“How much is the deal” 一段把判别系数小解释成模型稳、风险小，所以加大购买比例，和 step4 一致，和 3.2.2 的“越接近 1 越好”相反。

备忘录的 MODEL 段把黄金的 R² 写成 0.8591。摘要、3.2.1、3.4.2 三处都是 0.8592。同一指标四个位置出现三次 0.8592、一次 0.8591。比特币四处都是 0.9304。0.8591 不改成 0.8592。

备忘录重述目标函数时，风险符号写成 Si，正文式 (9) 和页 10 的说明都是 Sj。同一段还把 “proportion” 印成 “roportion”，把 “sought” 当 “sold” 用，两处都在页 10 已经出现过，备忘录是照抄。

备忘录说“改变正则项系数 λ 就能把风险分成稳健、普通、激进三种”。正文 4.1 的三种策略是靠改 β、γ、wH、wHb、q 得到的，表 5 里没有 λ。备忘录把分型归因到一个没有出现在分型表里的参数上。这是备忘录和正文的第二处口径冲突，和 R² 的 0.8591 并列记录。

表 8 与表 6 数字相同，但备忘录把它放在 RESULTS 下，省掉了 Rg2、Rb2 两行。正文 4.1 说“读表 8”，实际那一段旁边是表 6。

### 参考文献和附录

参考文献 12 条，第 2、3、4 条是 ARIMA 混合与对比，第 9 条是白噪声，第 7 条是投资者行为分类的出处。条目格式不统一：作者名后有的用句点有的用冒号，[10] 的题名用逗号接作者。不作为文风样本。

附录标题印 “Assetes”。图 17、图 18 是普通型和激进型的现金、黄金、比特币三面板，和正文图 9 的保险型凑成一套。图本身等裁剪。

### 这一段新增的、不能并掉的印刷事实

- 式 (14)(15)(16) 标签和所用权重错位，求解用的是下一期真实金价。
- R²：摘要和正文说越接近 1 越好，step4 和备忘录说越小越稳。
- 黄金相关系数：三处 0.8592，备忘录一处 0.8591。
- 终值精度：3.4 写 $132089.11，摘要和 4.3 写 $132089.1078。
- 表号：4.1 正文写 table 8，该处的表是表 6。
- 敏感度：c 条写黄金每次升 1%，图 15 导语写每次升 0.1%。
- 分型归因：正文靠 β、γ、w、q，备忘录归因到 λ。
- 粘连和错词：inflationso、Diﬁnition、traderss、radical-tupe、Assetes、roportion、sought、These ensures。

以上都按印面保留，不在记录时修正。公式分式、表 5 至表 8 的列对齐、全部图，等裁剪后再定。

## 公式印面（裁剪复核，2026-10-13）

六张裁剪都在 450KB 以下，由只读复核逐张读。印面和文字层有出入的，以印面为准，文字层的读法作废。式 (17) 这次没裁到，见下。

式 (3) 印面是
`R_i^2 = Σ_{j=1}^{t}(x_{i,j} − Y_{(i)})^2 / Σ_{j=1}^{t}(y_{i,j} − Y_{(i)})^2`。
分子是预测值对真实均值的平方和，分母是真实值对真实均值的平方和。这不是相关系数，是残差平方和比总平方和，数值上等于 1 减拟合优度。正文却写“越接近 1，拟合越好”。按这个式子，越接近 1 代表残差越大、拟合越差。作者把分子分母的含义用反了，句子方向也反了。不改式子，也不改那句。`Y_{(i)}` 的括号是下标的一部分。where 子句印成 “cycle iand”，i 和 and 之间没有空格。

式 (4) 印面：`DS_i = (1/t) Σ_{j=1}^{t} d_j × 100%`，`d_j` 在预测涨跌与真实涨跌同号时为 1，否则为 0，`j = 1, 2, 3` 写在括号右侧。`100%` 在求和内部，所以 `DS_i` 是百分数，又被 `1/t` 平均。where 子句把 `d_j` 写成 `d_i`，下标不一致。

式 (5) 印面比文字层更明确，也更错：
`S_j = sqrt( Σ_{j=i−30}^{i−1}(A_i − (Σ_{j=i−30}^{i−1} A_i)/30 )^2 / 30 )`。
求和指标是 j，求和项却是 `A_i`，i 不随 j 变化。内层求和把同一个 `A_i` 加 30 次再除以 30，结果还是 `A_i`，括号里是 0。所以这个式子按印面恒等于 0。左端下标是 j，右端没有任何 j。这是印出来的，不改成 `A_j`。

式 (6) 只编号了黄金那一组。黄金：买入分支 `C_{i−1} − G_i × w_g`，条件 `X_{g(i)} − Y_{g(i−1)} > β_g × A_{i−1}`；卖出分支 `C_{i−1} + G_i × m_g × (1 − α_g) × Y_{g(i+1)}`，条件 `Y_{g(i−1)} − X_{g(i)} > γ_g × A_{i−1}`。卖出分支用 `Y_{g(i+1)}`，即后一周期价格。比特币那一组没有编号，结构相同，但卖出条件印成 `Y_{b(i−1)} − X_{b(i−1)} > γ_b × A_{i−1}`，减数是 `X_{b(i−1)}` 而不是 `X_{b(i)}`，和黄金分支不对称。两组都没有 else。

式 (7) 只编号了黄金。黄金两个分支：`G_{i−1} + C_i × w_g × (1 − α_g)` 和 `G_{i−1} − G_{i−1} × m_g`，没有条件。比特币那一组没有编号，两个分支都用 `G_{i−1}` 开头：`G_{i−1} + B_i × w_b × (1 − α_b)` 和 `G_{i−1} − G_{i−1} × m_b`。文字层里怀疑是提取串行的地方，印面确实印的是 G。不改成 B。

式 (8)：`A_i = C_i + G_i × Y_{g(i)} + B_i × Y_{b(i)}`，和文字层一致。

式 (9) 的约束印面是五条，文字层挤成一团的读法作废：
`C_j, G_j, B_j, A_j ≥ 0`；`DS_j ≥ 0.5`；`C_j ≥ A_j × q`；`α_g = 1%, α_b = 2%`；`A_0 = 1000, C_0 = C_1 = 1000, G_0 = G_1 = B_0 = B_1 = 0`。
目标 `max_{w_j, m_j}(A_j − λ × S_j)`。前三条用下标 j。页 10 的散文把第一条说成“所有资产为正”，和 `≥ 0` 的印面差一个等号。

式 (12) 的印面和文字层完全不同。印面是一个分式：
`q_i = C_i / (C_i + G_i × Y_{g(i)} + B_i × Y_{b(i)})`。
这是现金占总资产的比例，分母正好是式 (8) 的 `A_i`。文字层把分子分母串成了连加，那一版作废。

图 6 的判断用的下标和式 (6) 也不一样：菱形印 `X_{g(i+1)} − Y_{gi} > 0`，`Y` 的下标是 `gi`，没有括号；绝对值那一步印 `|X_g − Y_g| > f_{g(i+1)}`，下标只剩 g。同一页里 i、i+1、gi 三种下标并存。

式 (13)：`A_{i+1} = C_{i+1} + G_{i+1} × Y_{g(i+1)} + B_{i+1} × Y_{b(i+1)}`。

式 (14)(15)(16) 印面确认了标签和权重错位，而且比文字层多出一个分母。三式现金都是减、黄金都是加、比特币都不变：

- 标签 `R_{W_{Hg}}`，内部用的是 `w_{Lg}`：`C_{i+1} = C_i − C_i × w_{Lg}`，`G_{i+1} = G_i + C_i × w_{Lg} × (1 − α_g) / Y_{g(i+1)}`。
- 标签 `R_{W_{Lg}}`，内部用的是 `w_{Hg}`。
- 标签 `R_{m_g}`，内部用的是 `w_{Lg}`，不是 `m_g`。
文字层没看出分母 `Y_{g(i+1)}`，印面有。散文明确写 `Y_{g(i+1)}` 是第 i+1 日黄金的真实均价，所以这三式用已发生的价格重估资产。图 7 的菱形印成 `R^i < R^i`，两侧相同，这个判断恒真或恒假，印面如此。

式 (18) 没有左端、没有等号。印面是
`( Σ_{k=1}^{10} |h_k − h_{k−1}| / h_{k−1} × 100% ) / 10`。
`100%` 在求和内部。节标题印 “Sensitivity Difinition”。`h_0` 后面先空格再句号，`h_k.Sensitivity` 之间没有空格。

式 (17) 不在这次裁剪里。p17 的裁剪底边停在 “Then the actual value of the deposit after five years is”，公式在下一行，没拍到。文字层的 `A = a(1+r−I)^5` 暂不作数，等补裁。表 5、表 6、表 7、符号表的裁剪还没读。

## 摘要与引言的段落动作（G1，文字层，图还没看像素）

### 摘要：五段，一段一项交付

| 段 | 主导动作 | 信息顺序 | 数字 |
|---|---|---|---|
| 1 | 背景加范围 | 交易者策略不同所以收益不同，本文研究谁的策略 | 无 |
| 2 | 问题 1 的方法加结果 | 预处理、ARIMA、相关系数、动态规划、约束、求解、终值 | 0.8592、0.9304、$ 132089.1078 |
| 3 | 问题 2 的证明加结果 | 三个判据、三种交易者、沿用问题 1 的解法、扰动、三个终值、抵抗通胀 | 14312.6827、50040.5474、132089.1078 |
| 4 | 问题 3 的定义加比较 | 先定义敏感度、再报两个数、再比较、再补方向 | 0.0422、0.0658 |
| 5 | 问题 4 的交付预告 | 总结前三问、以备忘录交给交易者 | 无 |

可复用的骨架是 “For problem n，先做什么，再得到什么数”。数字只出现在段 2、3、4，每段的数字都在该段后半，不在开头。段 1 和段 5 故意不给数。

段内的序数不统一，这是变体不是噪声：段 2 用 firstly、Following、Thirdly、Lastly 四拍，但 secondly 没出现，第二拍用 Following the processed data 顶上。段 3 用 By、Furthermore、Finally。段 4 只用 firstly、Secondly。同一篇摘要里三套序数并存，抄的时候不能假设作者会把 Firstly 到 Finally 用全。

段 2 有一处和正文冲突，先记：摘要说缺失值 “filling the missing value by the daily price of gold in the past”，只用过去的价格。正文 3.1 说用前后两天的均值，用了后一天。摘要的口径比正文保守，两处都留。

### 引言：1.1 到 1.3

1.1 一段。动作是给资产和数据来源。顺序：交易者频繁买卖、每次有佣金、两种资产、时间区间、图 1、两个来源各一句。黄金来源 London Bullion Market Association，比特币来源 NASDAQ。句 “Two such assets are gold and bitcoin.The” 句号后没有空格。

1.2 两段加四颗子弹。第一段复述委托：只用截至当天的价格决定买、持有或卖，起点 2016-09-11 的 1000 美元，区间到 2021-09-10，组合写成 [C, G, B] 并注明单位美元、金衡盎司、枚。收束句 “We should only use these data to solve the following problems”。四颗子弹是四项交付，每颗一个要求，不带方法。这一节是范围，不是方案。

1.3 四段，一段对应一个问题，和摘要同构，但这一节不给终值。

- 问题 1 第一段先说策略的前提是预测价格，所以要先建预测模型。然后列了 LSTM、BP、RNN、encoder-decoder，再用 “In view of the simplicity and efficiency of ARIMA model, which only needs endogenous variables rather than other exogenous variables” 选出 ARIMA。选型句的结构是“鉴于某模型的某个优点，而它不需要另一样东西，我们选用它”。被放弃的四个模型只点名，不比较。
- 问题 1 第二段从预测跳到策略：先按指标建策略模型，再算终值。风险的处理是“直觉上比特币波动远大于黄金，所以猜它风险更大，于是用价格变化的方差描述风险”。这是先下判断再选度量。然后一句 “This is essentially a dynamic programming problem” 把问题归类，再把收益和风险量化、以最大收益做目标、找约束、建模型。
- 问题 2 一段把“最优”先拆成泛化、稳健、收益三方面，再各用一句话定义。泛化等于改参数就能得到不同策略，所以分成三型。稳健等于参数小变不影响整体策略。收益一句用 “It also shows that” 接上，但这三个判据之间没有 “also” 的关系，这是顺手的连接词，不承载逻辑。
- 问题 3 一段先给直觉：佣金升则交易应减少，佣金降则交易可增加，目标仍是最大化收益。然后说沿用第一问的模型，改 α，观察交易频率、收益、风险三者的变化。直觉在方法之前。

图 2 放在 1.3 末尾，图注只有 “Overall structure”，没有解释句。工作计划没有单独成段，而是靠这四段各预告一节。

1.3 的段首大小写不统一：“For problem 1, The”“With regard to problem 2, The”“As for problem 3, It”，逗号后都是大写。三句的起法也不同：For、With regard to、As for。这是同一功能的三个变体，记为一个套路的三种起手，不记成三个套路。

### 第 3 节开头的承接

第 3 节第一段把 1.3 的预告落成做法：“In this section, based on the existing data, we use ARIMA model to predict the price trend of gold and bitcoin in the future, so as to establish a model and give the best daily trading strategy.” 一句里先说依据（已有数据），再说手段（ARIMA），再用 so as to 接目的（建模型、给策略）。这种“依据、手段、目的”三拍是章节开头的可复用框架。下一句单独交代动态规划用来估算 2021-09-10 的终值。

### 这一节和第 3 节以后的口径冲突（只记录，不裁决）

- 缺失值：摘要说用过去的金价，正文说用前后两天均值。
- R² 方向：摘要和 3.2.2 说越接近 1 越好，step4 和备忘录说越小越稳。
- 黄金相关系数：三处 0.8592，备忘录 0.8591。
- 终值精度：摘要和 4.3 写 $132089.1078，3.4 写 $132089.11。
- 三种策略的来源：1.3 和 4.1 说靠改 β、γ、w、q，备忘录说靠改 λ。

图 1、图 2 的像素还没看。符号表的文字层列是串的，等裁剪。

## 第二批裁剪（表与式 17）

这次五张里只有表 5 和式 (17) 切中目标。表 1、表 6、表 7 的裁剪没落到表体上，那三张作废，重裁。

式 (17) 印面是 `A = a^{(1+r−I)^5}`，指数写在 a 的右上角，不是 `a(1+r−I)^5`。文字层把指数读成了普通乘法，作废。按印面，底数是存款额 a，指数是 `(1+r−I)` 的五次方。代入 a = 1000、r = 0.5%、I = 7% 时，指数约等于 0.866，1000 的 0.866 次方约是 397，而正文给出的结果是 $139.2436。两个读法都对不上 139.2436：普通复利 `(1+0.005−0.07)^5 × 1000` 约是 714，印面的指数式约是 397。作者报的 139.2436 和他自己印的式子对不上。式子、代入值、结果三个都按印面留，不互相修正。where 句印 “I,deposit”，逗号后无空格，Then 大写。

表 5 印面，列对齐清楚，文字层的串行作废：

| 参数 | 保险型 | 普通型 | 激进型 |
|---|---|---|---|
| βb | 0.35 | 0.10 | 0 |
| βg | 0.50 | 0.50 | 0.50 |
| γg | 0.10 | 0.20 | 0.30 |
| γb | 0.10 | 0.20 | 0.30 |
| wHg | 0.95 | 0.80 | 0.80 |
| wHb | 0.15 | 0.30 | 0.40 |
| q | 0.15 | 0.05 | 0.01 |

βg 三列都是 0.50，黄金的上涨阈值不随交易者类型变化。激进型的 βb = 0，即比特币上涨阈值是 0，任何上涨都触发。3.4 给出的那组参数是 `βb = 0, βg = 0.5, γb = 0.3, γg = 0.3, wHg = 0.8, wHb = 0.4, q = 0.01`，和表 5 的激进型一列完全相同。所以问题 1 的主结果就是激进型的结果，这也解释了摘要里激进型终值等于问题 1 终值。前面只记了这个重合，现在有了参数上的对应。

顺带读到的图注确认了两处印刷：图 10 “traderss”，图 15 三面板是 transaction frequency、return、risk。

同一张 p06 裁剪没有切到符号表，但切到了式 (1) 和标准化式，印面与文字层一致：`y_t = α_0 + α_1 y_{t−1} + … + α_p y_{t−p} + ε_t`，`x' = (x − x̄) / SD`。标准化式的分子带括号、分母是 SD，没有说明 SD 为零时怎么办。

## 3.1 与 3.2.1 的写法（文字层）

3.1 开头一句单独成段：“Before data analysis, the availability of data must be guaranteed.” 先说数据必须可用，再列两条处理。这是预处理节的可复用起手，一句只立规矩，不带做法。

两条处理各是“名称加一句理由加一句做法”。缺失值：先对比特币每日交易、黄金只在交易日交易，所以数据不连续，再用 “For the convenience of subsequent modeling” 引出填补。标准化：先说标准化让各特征值权重相等，再说因为按周期预测所以按周期处理。理由在做法之前。

缺失值的做法印的是 “filled with the mean value before and after the day”，用了后一天。摘要写的是 “by the daily price of gold in the past”，只用过去。同一件事两个口径，都留。

3.2.1 的开篇段几乎是文献综述的口吻，引用 [2]：先说提高预测精度是决策者面对的重要而困难的任务，再说 ARIMA 是过去十年里做混合模型最常用的线性模型之一。这段没有本队的数据，只用来把模型请出来。可学的是“先说任务难，再把选用的模型放进一个已有位置”，不能学的是用文献的评价代替自己的比较。

拆模型用三颗子弹，每颗一个组成部分：AR、I、MA。每颗的结构是“名称、做什么、阶数记为什么、公式”。AR 的 where 子句印成 “where, and α is the coefficient”，where 后面直接接 and，前面缺了主语。MA 的 where 把 `ε_t` 说成 “the white noise process of variance”，variance 后面没有给出具体值。两处都按印面留。

I 这一颗没有公式，只有一句 “Generally, first order is enough.” 用 Generally 把一阶差分说成通常足够，没有给本数据的证据。证据在后面的表 2，这一句本身是先断言。

收束段把模型写成 ARIMA(p, d, q)，但紧接着 “where p is the autoregressive term, q is the moving average term, and D is the number of differences”。d 和 D 在同一段里并存。图的引用印成 “the figure3”，figure 和 3 之间没有空格。最后一句 “We will follow the steps listed below to build and solve our model.” 是把读者交到下一步的交接句，本身不带内容。

这两节的可复用框架：预处理节用“一句规矩加若干条理由在前做法在后”；模型节用“一段文献定位加若干颗子弹拆组成部分加一句交接”。where 子句缺词、d 与 D 并存，是这篇的印刷事实，不进框架。

## 表 1、表 6、表 7 印面（第三批裁剪）

三张表这次都完整入画。

### 表 1 符号

表头印 “Descripition”。符号和释义的配对如下，多数是对齐的：

- `t1 = 3, t2 = 3`：黄金交易周期（含节假日）、比特币交易周期。
- `n`：五年内的周期数。
- `DSgi, DSbi`：训练预测模型的命中率，i = 2, 3, …, n。
- `Ri = [Ci Gi Bi]`：第 i 周期的资产分布，`R0 = [1000 0 0]`。
- `Ai`：第 i 周期总资产，`A0 = 1000`。
- `qi`：第 i 周期现金占总资产的比例。
- `ei, fi`：第 i 周期涨跌阈值。
- `Xg(i), Xb(i)`：第 i 周期的预测均价。
- `αg, αb`：每笔交易佣金占交易额的比例。
- `R²gi, R²bi`：第 i 周期训练模型的决策系数。

错位的一行是 `Yg(i), Yb(i)`，释义只写了 “real average price of gold in the i-th cycle”。两个符号共用一句只提黄金的释义，比特币没有自己的释义。这是印出来的，不补一句比特币的。

`qi` 在表里是“现金占总资产的比例”，和式 (12) 的印面一致。表 4 把 q 说成 “cash retention ratio”。同一个 q，一处是比例，一处是保留比例，两处都留。

### 表 6 三种策略的结果

行标签在最左列，三列是保险型、普通型、激进型：

| 行 | 保险型 | 普通型 | 激进型 |
|---|---|---|---|
| 总资产 | 14312.68 | 50040.55 | 132089.11 |
| [C, G, B] | [11474.39, 1.59, 1.07] | [421.14, 0.61, 1.05] | [22.31, 0.16, 2.84] |
| 交易次数 | 85 | 58 | 9 |
| SD | 3861.73 | 15501.99 | 40067.35 |
| R²g | 0.94 | 0.27 | 0.24 |
| R²b | 0.41 | 0.98 | 0.99 |

表注：`R²g / R²b` 表示黄金或比特币的购买与实际波动的相关，SD 表示五年资产的标准差。

正文 4.1 写“激进型收益更多，但 SD 很大，所以资产变化大、要承担相应风险”。表里激进型的 SD 是 40067.35，确实是三列里最大的。前面文字层把 0.24 读到激进型名下，那是串行，作废。0.24 是激进型的 `R²g`，不是 SD。

保险型的 85 次交易、激进型的 9 次，和正文“越激进交易越少”一致。激进型期末现金只剩 22.31，黄金 0.16，比特币 2.84，资产几乎全在比特币上。保险型现金 11474.39，占大头。

`R²g` 从保险型的 0.94 降到激进型的 0.24，`R²b` 从 0.41 升到 0.99。正文据此说越激进越买比特币、黄金代表稳健。这个方向和表一致。但表注把这两个数定义成“购买与实际波动的相关”，3.2.2 把 R² 定义成预测值对真实值的残差比。同一个符号两套定义，都留。

### 表 7 敏感度

| 费率 | 保险型 | 普通型 | 激进型 |
|---|---|---|---|
| αg | 0.0267 | 0.0422 | 0 |
| αb | 0.2308 | 0.0658 | 0.0123 |

摘要只报了 0.0422 和 0.0658，正好是普通型这一列，摘要没有说明取的是哪一型。激进型对黄金成本的敏感度印成 0。保险型对比特币成本 0.2308，是全表最大的一格，和正文“保险型更敏感于比特币成本”一致。

### 到这里为止，印面已核对的和还没核对的

已按印面核对：式 (1)、式 (3)、式 (4)、式 (5)、式 (6)、式 (7)、式 (8)、式 (9) 及五条约束、式 (12)、式 (13)、式 (14)、式 (15)、式 (16)、式 (17)、式 (18)，表 1、表 5、表 6、表 7。

还没看像素：表 3 的后两行、表 4 的 q 行、图 1 到图 18。文字层对这几处的读法暂且留用，等裁剪推翻或确认。

## 第四批裁剪：式 (2)、式 (10)、式 (11)、表 2、表 4

式 (2) 印面与文字层一致：`y_t = c + ε_t + θ_1 ε_{t−1} + … + θ_q ε_{t−q}`。where 子句印 “ε_t is the white noise process of variance”，variance 后没有数值。

式 (10)、式 (11) 印面与文字层一致：`e_{g(i+1)} = β_g × A_i`，`f_{g(i+1)} = γ_g × A_i`。同一张裁剪又确认了式 (12) 的分式，和上一批一致。后面那句 “β_g, γ_g represents” 主谓不一致，原样留。

表 2 印面与文字层一致。表头左上角是空的，没有行标签的列名。黄金差分前 0.6734、差分后 0.0043。比特币差分前 0.9921、差分后 0.0000。

表 4 印面比文字层干净，列没有串：

| 符号 | 释义 |
|---|---|
| β, γ | 涨跌比例 |
| DS | 命中率 |
| wH, wL | 购买比例，H 高 L 低 |
| m | 卖出比例 |
| R² | 决策系数 R_i² 的阈值 |

表头同样印 “Descripition”。q 那一行在这次裁剪的底边之外，没拍到。R² 的释义是“阈值”，但 3.2.2 把 R² 定义成拟合指标，step4 又把 R² 小当成模型稳。同一个符号在表 4 里是阈值，在正文里是拟合指标，两处都留。

表 3 只拍到表头和 AR(P) 一行：ACF “attenuation tends to 0”，PACF “truncation after p-order”。MA 和 ARMA 两行在底边之外。AR 的阶数印成大写 P，和正文的 p 并存。

到这里，18 个公式里只剩表 3 的两行和表 4 的 q 行没看像素。图 1、2、4、5、8 已看像素，图 3 底边被切，其余图还没看。

## 图 1、2、4、5、8 的印面

图 1 两面板，图注 “Figure 1: The prices of two assets”。左面板标题 “GOLD DAILY PRICES”，纵轴 1000 到 2200，横轴 Date，从 2016-12-30 到 2021-08-17。右面板 “BITCOIN DAILY PRICES”，纵轴 0 到 70000，横轴从 2016-11-20 到 2021-07-08。子图注写明单位：黄金美元每金衡盎司，比特币美元每枚。两条都是蓝底上的白色填充序列。这是本队自己的价格图，来源在正文里，不在图内。

图 2 是总结构图，没有坐标轴。左列三框：Data preprocessing、ARIMA model、Prediction trend by cycle，下面标 “Price Prediction Model”。粗箭头指向橙色框 “Establish strategy model”，这个框还接收 “Define variable parameters” 的向下箭头，以及一个绿色圆角框的向左箭头，绿框写 “Adjust alpha to explore the impact on insurance-type, common-type , radical-type”，common-type 和逗号之间有空格。从策略框分出 “Conservative strategy” 和 “Risk strategy”。黄色框列 “Generalization Ability、Robustness、Yield”，箭头向上指回策略。图用颜色和箭头方向区分四块：预测、策略、证明、成本影响。正文 1.3 把策略分成保险、普通、激进三型，图里却是 Conservative 和 Risk 两支。图和正文的分型数量不一致，都留。

图 4 四面板，2×2。每个纵轴从 −1.00 到 1.00，横轴 0 到 20。左列是黄金的 ACF 和 PACF，右列是比特币的。蓝色茎，零附近有阴影带。图本身没有标出正文说的“黄金 ACF 2 阶、PACF 1 阶截尾”。截尾阶数只在正文里，不在图上。

图 5 两面板。左 “Gold”，图例 real 蓝、predict 红，纵轴 1240 到 1340，横轴 2016-09-15 到 2016-11-08。右 “Bit”，纵轴 600 到 740，横轴日期相同。两个轴都没有轴标题。子图注 “(a) Forecast chart of gold in one cycle”“(b) Forecast chart of bitcoin in one cycle”。图上方的正文印 “correlation coefficient R² of gold is 0.8592 and that of bitcoin is 0.9304”，和摘要一致。图只覆盖一个周期、约两个月，正文用这一窗的两条曲线支撑“预测成功、可以使用”。

图 8 单面板，标题 “Changes in total assets”，图注 “Figure 8: The changes of total assets during the five-year period”。纵轴 “Dollar”，0 到 175000，横轴 “date”，2017 到 2021。一条蓝线，2018 附近有一次尖峰，2020 前大多在 35000 以下，2021 陡升，终点低于峰值。图上方印 “[C,G,B]=[22.31, 0.16, 2.84]”，和表 6 激进型的持仓一致。终值 132089 落在 125000 和 150000 之间，和曲线终点位置相符。图没有标出 9 次交易的位置。

图 3 的第一张裁剪切掉了底边，已重裁，等读。看得见的是 “Auto Regressive + Integrated + Moving Average = ARIMA”，背后大字母 p、d、q，以及 Step1 stabilization、Step2 selection of p and q、Step3 white noise test 三个框。

## 图 9 到图 18 的印面

图 9 三面板，保险型，绿色。现金纵轴 Dollar 0 到 1000，黄金 Ounce 0 到 1.2，比特币 Pieces 0 到 0.014，横轴都是 2017 到 2021。比特币面板的纵轴上限只有 0.014 枚，和表 6 里保险型期末比特币 1.07 对不上：1.07 远高于 0.014。要么纵轴只覆盖了曲线的一部分，要么读到的刻度有误。这一处先标成未定，等把图 9 的比特币面板单独再裁一次确认，不在这里下结论。

图 10 三面板，图注印 “traderss”。保险型绿色，纵轴 0 到 16000；普通型红色，0 到 70000；激进型蓝色，0 到 175000。横轴都是 date，2017 到 2021。三型用了三种颜色和三套纵轴刻度，终值 14312、50040、132089 各自落在对应面板的刻度范围内。

图 11、12、13 是稳健性的三对面板，每对左黄金右比特币，横轴刻度都是 1 到 6，纵轴 dollar 0 到 200000。横轴标签印的是变量名而不是符号：图 11 是 down_gold_threshold、down_bit_threshold，图 12 是 buy_gold_more_threshold、buy_bit_more_threshold，图 13 是 sale_gold_threshold、sale_bit_threshold。正文把这三张叫 wL、wH、m 的扰动。图上的名字和正文的符号没有在图内对照。三张纵轴上限都是 200000，而主结果只有 132089，所以这三张的纵轴留了主结果以上的空间。

图 14 三面板，案例 a，横轴 alpha gold，刻度 0.002 到 0.010。交易次数纵轴 frequency 55 到 61，收益 Dollar 0 到 100000，风险纵轴 10000 到 20000，面板标题 “Variation of variance”。正文说黄金成本的小变动不影响决策。横轴从 0.002 到 0.010，步长约 0.002，和 c 条说的每次降 0.1% 即 0.001 不完全同刻度。

图 15 三面板，案例 c，横轴 alpha gold 0.02 到 0.10。交易次数纵轴 40 到 60，收益 0 到 100000，风险 10000 到 20000。横轴刻度是 0.02 一档，对应每次升 1 个百分点，和 c 条 “rise 1% each time” 一致，和导语 “每次增加 0.1%” 不一致。图支持 c 条，不支持导语。

图 16 三个蓝色椭圆，箭头向右：When to trade、Trading bitcoin or gold、How much is the specific transaction。图注 “Figure 16: Structure of transaction strategy model”。备忘录正文的三个小标题是 When to trade、Deal what、How much is the deal。图的第二、第三个标签比正文规范，正文用的是口语。图和正文说的是同一组三个问题，用词不同。

图 17 普通型，红色。现金 0 到 4000 美元，黄金 0 到 1.0 盎司，比特币 0 到 1.0 枚。图 18 激进型，蓝色。现金 0 到 600，黄金 0 到 0.16 盎司，比特币 1.4 到 2.8 枚。表 6 的期末持仓：普通型 [421.14, 0.61, 1.05]，激进型 [22.31, 0.16, 2.84]。普通型的比特币 1.05 略高于图 17 的纵轴上限 1.0，激进型的黄金 0.16 正好压在图 18 的上限上，激进型的比特币 2.84 压在上限上。图 17 的比特币面板和图 9 的比特币面板一样，终值落在纵轴之外或贴边，这是第二处。

附录标题印面是 “Appendix A Changes of Various Types of Traders' Assets”，Assets 拼写正确。文字层读成 Assetes 是提取错误，作废。

### 图里新出现的、和正文不一致的地方

- 图 2 把策略分成 Conservative 和 Risk 两支，正文 1.3 和 4.1 分成保险、普通、激进三型。
- 图 9 比特币纵轴上限 0.014，表 6 保险型期末比特币 1.07。待单独重裁确认。
- 图 15 的横轴支持 “每次升 1%”，不支持导语 “每次升 0.1%”。
- 图 16 的三个标签和备忘录正文的三个小标题用词不同。
- 附录标题拼写正确，文字层的 Assetes 作废。

## 图 3、表 3、表 4 收尾

图 3 重裁后完整，图注 “Figure 3: Structure of ARIMA model”。左到右：大字母 p、d、q，上面分别是 Auto Regressive、Integrated、Moving Average，橙色加号和等号，蓝色圆圈里 ARIMA。四个框用灰线连到圆圈，没有箭头：Step1 stabilization、Step2 selection of p and q、Step3 white noise test、Step4 prediction。正文的四步和这四个框对应。第一张裁剪漏掉的是 Step4。

表 3 三行都完整：

| 模型 | ACF | PACF |
|---|---|---|
| AR(P) | 趋于 0 | p 阶后截尾 |
| MA(q) | q 阶后截尾 | 趋于 0 |
| ARMA(p, q) | q 阶后趋于 0 | p 阶后趋于 0 |

AR 的阶数印成大写 P，MA 和 ARMA 用小写。文字层把三行串成两行，作废。表下 NOTE 说截尾指落在置信区间内，95% 的点符合规则。

表 4 六行都完整，q 行在：β、γ 是涨跌比例，DS 是命中率，wH、wL 是购买比例，m 是卖出比例，R² 是决策系数的阈值，q 是现金保留比例。q 的这句释义和表 1 里 qi 的“现金占总资产比例”用词不同，一个说保留比例，一个说占比。

到这里，18 个公式和 7 张表全部按印面核对过。

图 9 比特币面板单独重裁确认：纵轴 Pieces，刻度从上到下 0.014、0.012、0.010、0.008、0.006、0.004、0.002、0.000。绿色线大部分在框内，2018 刻度之后有一根细尖刺顶到上边框被截断。所以这张图的纵轴确实只到 0.014 枚，而表 6 给保险型的期末比特币是 1.07 枚。图的刻度装不下表的终值，尖刺被截掉的部分看不到数值。两处都按印面留，不把图的纵轴改读成 1.4，也不把表的 1.07 改小。

## G0 视觉核对的缺口

已按印面核对：式 (1) 到式 (18)，表 1 到表 7，图 1 到图 18。图 6 和图 7 的文字是从公式裁剪里读到的，流程图的框和箭头没有单独核过像素。目录页的拼写（Sensitivity Difinition）只在文字层见过。这两处不影响公式和结果表，留到 G6 再补像素。

文字层被印面推翻的有：式 (5) 的求和项是 A_i 不是 A_j，式 (12) 是分式不是连加，式 (17) 是指数式，表 3 是三行，表 5 的列，表 6 的 SD 行，附录标题 Assets。这些以印面为准。

## G2 第二遍：假设到备忘录的句式

这一遍不重复前面的内容记录。每条只留一件可复用的修辞工作，并写明什么时候不能用。摘句按印面，错词留在摘句里，不进可复用骨架。

### 假设节的起手和子弹

起手是一句，两拍：“To simplify our problems, we make the following basic assumptions, each of which is adequately justified.” 前半拍给假设的目的（简化问题），后半拍预先宣布每条都已充分证明。五条子弹没有一条给出证明。所以这句的前半拍可学，后半拍不能学：目的可以预告，证明必须跟在条目后面，不能用一个定语从句把证明一次性宣布完。

五条子弹各只限一件事，这是可学的粒度。第二条把交易者写成“身心健康、没有大额贷款”，是把人的状况写成模型假设。可学的是一条假设只限一个因素。不能学的是把无法检验的个人状况写进来充数。

第五条的信息顺序是“Since [金额很小]，[忽略最小交易单位]，for [模型的普遍性]”。理由在前，限制在中，目的在尾。这个顺序可学。但这条的理由（只有 1000 美元）和目的（普遍性）是拧的：金额小恰恰说明模型不普遍。骨架可以留，这条的填充不能留。

### 符号节的两句

“In this work, we use the nomenclature in Table 1 in the model construction. Other none-frequent-used symbols will be introduced once they are used.” 第一句告诉读者主符号在哪张表。第二句预告冷门符号在第一次使用时再定义。这是符号节的标准收法：主表加一条延期定义的承诺。印面 “none-frequent-used” 少了连字符位置，骨架里写成 “less-used”，不照抄错词。

### 预处理节的起手

“Before data analysis, the availability of data must be guaranteed.” 一句只立规矩，下一行才开始列做法。可复用的是把规矩和做法分成两层，规矩用 must，做法用具体动词。不能把规矩句写成做法的摘要，这句里没有任何填补或标准化的字。

两条做法都是“名称。理由。做法。” 缺失值那条先对比特币和黄金的交易日差异，再用 “For the convenience of subsequent modeling” 过渡到填补。这个过渡短语只说明“为了后面好建模”，不说明填补方法为什么合理。可学的是理由在做法之前。不能学的是用 convenience 代替方法理由。

### 模型节的文献定位

“Improving forecasting especially time series forecasting accuracy is an important yet often difficult task facing decision makers in many areas.” 这句没有本队的数据，用来把 ARIMA 放进一个已有的位置。骨架是“[任务] is an important yet often difficult task facing [谁]”。紧接着用 “which have been widely applied … during the past decade [2]” 把选用说成文献里的常用，而不是本队比过别的模型。可学的是先把模型放进一个已有位置。不能学的是用 “widely applied” 代替自己的比较。1.3 里放弃 LSTM、BP、RNN 时也只点名，两处是同一个习惯：被放弃的模型不比较。

拆模型的三颗子弹，每颗是“名称。做什么。阶数记为某值。公式。” AR 那条的 where 印成 “where, and α is the coefficient”，where 后缺了被解释的对象。骨架 “where, [符号] is [角色]” 可学，这条的 and 是印刷事故，不进骨架。

I 那条没有公式，用 “Generally, first order is enough.” 把一阶差分说成通常足够。Generally 在这里是先断言，证据在后面的表 2。可学的是短句给一个默认选择。不能学的是 Generally 后面不接本数据的证据。

交接句 “We will follow the steps listed below to build and solve our model.” 本身没有内容，只把读者交到下一步。这种空交接可以留，但一步里只能有一句，不能连用。

### 求解节的“先说要避开什么”

step3 的两句是这篇最清楚的步骤句式。“Firstly, due to the cost in the transaction, in order to avoid excessive cost caused by frequent transaction, the transaction is carried out only when the increase and decrease reach a certain threshold.” 四拍：Firstly、due to [成本]、in order to avoid [坏事]、[动作] only when [阈值]。第二句把 due to 省掉，只留 “in order to avoid [另一件坏事]，[动作] only when [条件]”。同一个节里，完整四拍和省略版并列。抄的时候第一拍给全，后面的拍可以省 due to，但不能省 “要避开的坏事”。

step4 的判断句是 “The smaller the variable, the more stable the model is, and the proportion of buying gold during trading can be increased.” “The smaller … the more …” 是比例句式。可学的是用它连接一个指标和一笔交易决策。这条的填充和 3.2.2 的 “The closer the index value is to 1, the higher the fitting performance” 方向相反，骨架相同、填充相反，两处都留，不能并成一条。

### 评价节和结论节是同一组子弹

3.4.2 的三颗子弹和 6.1 几乎逐句相同：数据要求低、参数表可调所以将来能做成软件、参数范围大所以灵活。结论节没有新句子。可学的不是这三句的内容，而是一个反面边界：优势节如果只是把前面的评价再贴一次，就不要单独成节。真正可复用的是 3.4.2 里 “By changing the parameters in the list, we can achieve different income results.” 这句把参数表说成一个可以拨动的清单。骨架 “By changing [参数清单], we can achieve [不同结果]”。

收束句 “These ensures the reliability of the results.” 主谓不一致。骨架若要留，只能留 “This ensures …”，而且这句没有说出保证了什么，边界是：收束句必须点明保证的是哪一项，不能用 these 笼统收。

### 问题 2 的三个判据

开篇把“最优”拆开：“so the model has good generalization ability. At the same time, the small change of parameters will not affect the overall strategy, and the model is robust. Compared with other investments, our strategy has a better rate of return. The following will explain …” 三句一个判据，最后一句预告下文。At the same time 连接的是两件独立的事，不是同时发生的事。可学的是一句一个判据再加一句预告。不能学的是用 at the same time 把并列装成同时。

4.1 三型交易者，每型都是“目的。手段。成败概率。” 激进型多一句让步：“Unless they need money urgently, have the psychology of gamblers or have the ability to take risks, most people will not use this investment method.” Unless [三种例外]，most people will not。这个让步句式可学，用来给一个不推荐的选项留出例外。不能学的是例外里并列了三个互不相干的原因（急用钱、赌徒心理、有能力承担），读者无法判断哪个才算数。

4.2 的定义用了两次 means：“The good robustness of the model means that the model has strong anti-interference ability, which means that the system has the ability to maintain a certain performance under the disturbance of uncertainty.” 第一次 means 把稳健换成抗干扰，第二次 means 把抗干扰换成在扰动下保持某项性能。两级改写，第二级才是可操作的定义。可学的是最后那级“在 [扰动] 下保持 [某项性能]”。不能学的是连用两次 means，第一级没有增加信息。

读图的起手是 “As can be seen from the figure above”。图 11、12、13 三张一起引：“As shown in the figure 11, figure 12, figure 13, they show …” 数词和 they 重复指同一组图。骨架 “As shown in Figure N” 可学，一次引三张时用 and 连接，不用 they 再指一次。

收束 “The model has good robustness, so it is proved that the strategy we give is the best.” 从“落在某范围内”跳到“因此证明最优”，中间没有比较对象。这是这篇最典型的越级收束。边界写死：so it is proved that 前面必须有一个比过的对象，否则这句不能用。

### 收益对比的代入句

“It can be seen from the data, from 2016 to 2021, the inflation rate was 7%, the bank deposit interest rate was 0.5%, so the actual value of $1000 after five years is $139.2436.” 一句里塞了来源（from the data，但没给来源）、两个代入值、一个结果。骨架若要留，应拆成两句：一句给来源和两个比率，一句给结果。这篇把它们粘在一句里，而且 7% 和 0.5% 没有出处。对比句 “The results obtained by our model are several times higher than the more conservative financial behavior, so our model has higher income and can resist inflation.” several times 没有给倍数。可学的是和一项更保守的做法比。不能学的是用 several times 代替算出来的倍数。

### 敏感度节

定义之前先搭场景：“Set initial variable α by α0, the initial transaction frequency h is h0. After changing K times, the variable α by αk.” 先给初始，再给变动后。这是定义句的可复用铺垫，比直接甩公式清楚。印面 “h0 .” 句号前有空格，“hk.Sensitivity” 句号后没有空格，都是印刷，不进骨架。

四种扰动写成 a b c d，每条只动一个费率、另一个不动。这个“一次只动一个”的列举可学。c 条写 “rise 1% each time”，图 15 的横轴是 0.02 到 0.10，和 1% 一档相符；同页导语又写每次增加 0.1%。列举本身可学，同一页里两个步长不能同时进骨架。

读图三句是编号的，一句一个观察，然后收成 “our model has not ignored, keenly felt this signal, and the change direction is in line with the reality.” 三拍：没有忽视、感觉到了、方向符合现实。第二拍 keenly felt 是把模型写成有感觉的人。可学的是“变化方向符合现实”这种把方向说出来的收法。不能学的是把模型写成会感觉的主体。

表后三条发现，每条一个比较：对比特币成本更敏感、保险型更敏感于比特币而普通型更敏感于黄金、激进型整体不敏感。骨架 “The sensitivity of [策略] to [甲] is higher than that to [乙]”。higher than that to 这个 that 指代 sensitivity，可学。

### 备忘录

抬头四行：To、From、Subject、Date。Subject 用名词并列 “Investment model, Trading Strategy and Results of Bitcoin and Gold”，不是句子。可学的是备忘录主题用名词并列，不写成一句口号。

正文第一段是背景，收在 “to help you better invest”。you 是这篇里唯一直接对读者说话的地方，正文其他地方都用 we。备忘录可以把 we 换成 you，正文不要。

三个问题的小标题是口语：When to trade、Deal what、How much is the deal。图 16 的椭圆用的是 “When to trade、Trading bitcoin or gold、How much is the specific transaction”。同一组三个问题，图上用短语，备忘录用口语。可学的是把策略收成三个问题。不能学的是 Deal what 这种不完整的问句，图上的短语更可用。

“On the contrary, if the trading conditions are not met, wait until the next cycle for judgment.” On the contrary 后面接的是条件不满足时的等待，不是相反的结论。这个连接词用错了地方。骨架里等待应该用 otherwise 或 if not，不用 on the contrary。

MODEL 段的选型句和 1.3 是同一句的改写：“In view of the simplicity and efficiency of ARIMA model, which only needs endogenous variables rather than other exogenous variables, we choose ARIMA model.” 1.3 用 “we choose to use”，备忘录用 “we choose … as the price prediction model”。同一个理由句出现两次。这是稳定句式，不是凑字数：鉴于 [优点]，which only needs [甲] rather than [乙]，we choose [模型]。rather than 用来写模型不需要什么，这是这篇选型的习惯，和“比别的模型更准”不是一种说法。

RESULTS 段 “Through the training of parameters, we have obtained models for three different populations.” populations 把三种交易者说成三个人群。可学的是“通过调整参数得到面向不同对象的模型”。这篇的对象是风险偏好，不是人群，populations 这个词不能照搬。

### 这一遍新定下来的骨架和边界

下面这些是这一遍才收束的。每一条都写了不能用的情况。

1. 假设起手只留“为了简化，作如下假设”。不要加“每条都已充分证明”，除非每条后面真有证明。
2. 符号节用“主符号见表 N，其余在首次使用时定义”。
3. 预处理用“先一句规矩，再逐条理由在前、做法在后”。convenience 不能代替方法理由。
4. 选型用“鉴于 [优点]，它只需要 [甲] 而不需要 [乙]，所以选用”。不要用 widely applied 代替自己的比较。
5. 步骤用“为了避开 [坏事]，仅当 [阈值] 才 [动作]”。第一拍给全，后面可以省 due to。
6. The smaller / The closer 这种比例句式可以连接指标和决策，但同一指标的两个方向不能并成一条。
7. 优势节如果和评价节是同一组子弹，就不要再写一遍。
8. 收束 “so it is proved that” 前面必须有比过的对象。
9. 敏感度用“一次只动一个量”的 a b c d 列举，同一页不能有两个步长。
10. 备忘录把策略收成三个问题，用短语，不用不完整的问句。对读者说话只用在备忘录里。

第三遍要专门找这一遍没覆盖的：定量结果句（“is 0.8592 and that of … is 0.9304” 这种并列报数）、图的引导句（“The specific process is shown in the figure N”）、以及 where 子句的全部出现位置。

## G2 第三遍：where、报数、引导句

这一遍把全文里 where、It can be seen、as shown、respectively、Therefore、indicates that、is as follows、according to 的全部出现位置对过一遍。下面只记稳定的功能和变体，不重复第二遍已经收的骨架。

### where 子句有两种用法，不能并

全文 where 出现十处，分成两种功能。

第一种是给符号释义，九处。骨架是 “where, [符号] represents 或 is [对象]”，多个符号用逗号或 and 接成一串。出现位置：式 (2) 后（c、ε_t、θ 三个），式 (3) 后（x、y、Y 三个），式 (4) 后（d 一个），式 (9) 后（W_j、m_j、A_j、λ、S_j 五个），式 (17) 后（A 一个），备忘录里把式 (9) 的 where 又抄了一遍。另外两处 where 不在公式后面，而在句子中间：ARIMA(p, d, q) 那句用 “where p is …, q is …, and D is …”，图 6 下面先单独写一个 “where,” 再给式 (10)(11)(12)。

变体有三个。一是动词：represents、is、stands for 三个词都在用，同一篇里不固定。二是逗号：多数印成 “where,”，式 (3) 式 (4) 印成 “where” 不带逗号。三是破句：式 (1) 的 where 印成 “where, and α is the coefficient”，where 和 and 之间缺了被解释的符号。

第二种只有一处，功能完全不同。式 (13) 前的 “Where, the formula for total assets is” 用 Where 开头引出下一组公式，不是在解释符号。这个 Where 是段落起手，不进释义骨架。

边界：释义 where 必须紧跟在它解释的那条公式后面，一个 where 串完这条公式的全部新符号，不把上一条公式的符号混进来。备忘录把式 (9) 的 where 原样再抄一次，属于重复，不增加覆盖。

### It can be seen 六处，来源不同

六处都是 “It can be seen … that [判断]”，差别在 from 后面接什么。

- from the table 2：表 2 显示一阶差分后序列平稳。
- from the comparison：摘要里比较两个敏感度后下的判断。
- from the data：4.3 里接通胀率和利率。
- from the figure：图 14 后接“小变动不影响决策”。
- 不带来源，直接 that：摘要里“收益能抵抗通胀”，5.2 里“面对黄金成本持续上升”，备忘录里“策略能抵抗通胀”。

可复用的是带 from 的四句：判断前面点明它来自哪张表、哪张图、哪次比较。不带来源的三句把判断说成显而易见，但判断本身（抵抗通胀、感觉到信号）并不是读表就能直接看到的。骨架只留 “It can be seen from [表或图或比较] that [这个来源确实显示的判断]”。that 后面的判断必须是来源里真有的，不能用来源没有的结论。

### 报数的两种并列

成对的数用 “that of” 避开重复指标名。[指标] of gold is [数] and that of bitcoin is [数]。摘要、3.2.1、3.4.2 三处用 0.8592 和 0.9304，备忘录把黄金那个写成 0.8591。骨架可留，备忘录的 0.8591 是同一骨架的一次走样，不另立一条。

三个数用 respectively 收尾：are [甲], [乙] and [丙] respectively。摘要和 4.3 都这样报三种策略的终值。respectively 还被挪去干别的活：1.2 用它收三个单位（美元、金衡盎司、枚），3.2.1 用它收 p 和 q 两个值，4.2 用它收三张图各自扰动的参数。所以 respectively 在这篇里有两个功能，报一组平行的数，和提醒前面几项一一对应。两个功能都可留，但不能把 respectively 当成只用于数字。

### Therefore 连接的是已经说过的理由

Therefore 出现八处。每处前面都有一个理由，后面是一个动作或结论：因为要预测所以要建预测模型，因为猜风险更大所以用方差描述，因为改参数能得到不同策略所以分成三型，因为要量化策略所以定义参数，因为只需要理解参数所以模型简单（这句在 3.4.2 和 6.1 各一次），备忘录里因为判断系数小所以可以加大购买比例，因为要兼顾风险所以建立目标函数。

骨架 “Therefore, [动作]” 前面必须有一句读者已经读到的理由。这篇没有一处 Therefore 前面是空的。6.1 那一处的理由和 3.4.2 是同一句，所以结论节的这个 Therefore 不提供新理由。

### indicates that 按序号走过约束

式 (9) 后的散文把五条约束里的前三条逐条解释：“The first constraint indicates that …, the second constraint indicates that …, the third constraint indicates that …”。骨架是 “[序数] constraint indicates that [这条约束在限制什么]”。这篇只解释了前三条，后两条（费率、初始值）没有 indicates that。可复用的是逐条解释，边界是解释的条数要和约束的条数一致，不能解释三条就停，剩下的让读者自己看。

### The formula is as follows

式 (1) 和式 (2) 前各有一句 “The formula is as follows”。式 (13) 前换成 “Where, the formula for total assets is”。三处都是把公式交出来之前的一句提示。骨架留 “The formula is as follows”，紧跟公式，中间不插别的句子。式 (13) 那种用 Where 起手的变体不推荐，因为它和释义 where 撞车。

### according to 五处，都在指一个来源

“according to the established indicators”“according to the forecast”“according to the model”“According to the reference materials[7]”“according to different parameters adjustments”。五处的功能一样：下一个动作是依照某个已经存在的东西做的。骨架 “according to [指标、预测、模型、文献或参数]”。文献那处给了编号 [7]，其余四处不给编号。边界是 according to 后面必须是读者能找到的东西，不能接一个没有定义的判断。

### 只出现一次、不单立的

“Successful investment comes from two factors: one is …, and the other is …”。one is 配 the other is，把一件事拆成两个因素。只出现一次，但骨架完整。先记为候选，不并进别的条。

“it is 1, on the contrary, it is 0” 在命中率的定义里。这里 on the contrary 连接的是两个互相排斥的结果，用得对。备忘录里同一短语接的是“条件不满足就等待”，用得不对。同一短语，配对排斥结果时可用，接一个退路动作时不用。这是第二遍那条边界的一个正例，不另立。

“In addition, we make the following assumptions”“Next, establish a trading strategy model”“It is known that the transaction cost is the Commission” 各只出现一次，而且只是把读者带到下一句，没有自己的信息。不立为骨架。

## G2 第四遍：零新增

第四遍把 Firstly、Secondly、Finally、Furthermore、In contrast、In order to、Based on、Generally、Intuitively、On the contrary、In addition、Next、It is known that 全部再查了一遍。每一处都能归进前面三遍已经收的骨架：序数归摘要的三套序数，In order to avoid 归求解节的四拍，Based on 归章节开头的“依据、手段、目的”，Generally 归一阶差分那条，Intuitively 归 1.3 的先下判断，On the contrary 归备忘录那条及其正例，In contrast 归收益对比。

In addition、Next、It is known that 三处只有连接功能，没有稳定的信息顺序，按“只有连接词、没有稳定语义工作就不算套路”处理，不新增。

这一遍没有新的可复用动作。假设、符号、预处理、模型、求解、评价、问题 2、收益、敏感度、结论、备忘录这些章的语言饱和到此为止。references 章只有条目、没有本队写的分析句，不抽语言单元，这条在入库时记成无作者语言。appendix 只有图和标题，语言只剩标题本身，不另抽。
