# D2015 38727：可迁移的写作机制草稿

这是纠偏后的文字蒸馏笔记，不是已安装的 skill，也不证明整篇论文通过。完整证据与限制见 `pattern-registry.draft.json`；41个单元映射到40个模式，独立论文支持数始终为1。下列例句来自已经检查过的原创例句库，不是原论文句子的改写。

## 1. 先交代分析输出将怎样被使用

Summary 的开头不是单纯宣布“建立了模型”，而是把输出接到诊断、排序和资源分配。Introduction 的结尾再从需求、行动和可计算后果把读者交给方法部分。这是同一功能的两个章节位置变体，不能算成两份独立支持。对应模式01、单元001/036。

可迁移的顺序是“输出对象 -> 预期操作 -> 使用者的决定”，不是强制使用 objective 或 thus。写作者应能说明谁据此做什么，后文也应给出相应输出。

> The catalogue flags conflicting dates so archivists can direct the next review round to uncertain entries.

适用于确有使用者和后续选择的工作；这条链本身不证明工具有效，更不证明政策因果效果。

## 2. 用定义、方向和判读规则给指标一个工作岗位

六个子指标的共同动作是先说它代表什么，再说它能提示哪类规划需要。共同量尺与分数方向另外声明，触发警告的阈值与“没有警告便已合格”也被分开。对应模式11、12、13；公式的精确保真仍需单独验收。

读者因此能从一个量的名字走到它在决策链中的用途，而不是只记住一个符号或范围。

> Three conflicting fields trigger manual review; fewer conflicts do not certify that a record is correct.

不可把同量尺当成同含义，也不可把筛查阴性写成全面安全的证明。原文数字不随修辞机制迁移。

## 3. 让诊断真正进入方案，而不是在建议章重新起炉灶

案例部分的优先事项同时回指前面的诊断和当地声明的目标；发展计划再把它们拆成可指认的行动。对应模式17、23、25。这里可学的是前后交接的可追溯性，不是认领作者的历史政策主张。

> To resolve the identifier conflicts found earlier, the archive proposes a two-stage register check before importing the next collection.

一份组件清单并不等于成本模型。应把“做哪些事”与下一条的“希望带来什么”分开。

## 4. 重复的 intended-to 列表有明确任务

教育、交通、基础设施三处采用相同的预期结果引导语。重复稳定了“行动 -> 意图”的读法，不能因为表面公式化就删掉，也不能给每项收益各造一个模式。对应模式26。

> The label-review sessions are intended to resolve identifier conflicts, retain competing readings, and shorten the pending queue.

这里的 intended 不是装饰性弱化词，而是在区分目标和测得结果。没有评价环节时，不能把清单中的意图改写成已经实现的效果。

## 5. 写出支持条件、分配准则和执行伙伴

方案的操作性不仅来自动作名，还来自谁能获得支持、需要承担何种承诺、谁优先、由哪些伙伴实施。原文分别出现服务承诺、配套筹资、贷款优先准则和执行伙伴。对应模式24、28、39；未给出的配套比例不能补造。

> The label-review sessions will be coordinated by the collections office with accession clerks and volunteer transcribers.

这能把文字从“希望改善”推进到“拟如何交付”，但不能代替伙伴同意、预算和执行能力的证据。

## 6. 先界定情景，再报告方向和例外

作者在情景输入前声明哪些量更新、其余哪些量保持固定，然后给出总体向好的判断，同时保留环境分项不改善的例外。另有“若不行动则难以改善”的文字基线，不能把它冒充计算过的反事实。对应模式29、30、38。

> For the extra-reviewer scenario, we change the number of review sessions and keep the incoming document mix unchanged.

> The additional review sessions reduce most conflicts, but ownership fields remain unresolved where the source register is missing.

固定不变的是模型设置，不是世界将保持不变的事实；总体方向也不等于每个分项都改善。

## 7. 把好结果、可控范围和剩余问题放在一起

低总风险仍可有值得处理的具体暴露；外来影响也不排除本地仍能做的事。写法分别是“总体判断 -> 残余问题 -> 针对行动”和“外部约束 -> 本地机会 -> 行动边界”。对应模式21、22、34。

> The adjacent construction site determines the main closure, while signage inside the building remains under the venue team's control.

这是行动范围的划分，不是对本地措施效果大小的估计。区域协调同样只是可能需要的响应尺度，不能凭提及协调就宣告某种治理安排有效。

## 8. 把前文的强断言与后文条件一起读

Summary 的稳定性断言应与后文的数据质量上限、统一扰动条件并读。写作者可以学习“可靠性依赖什么、稳定性针对哪类变化”的限定方式，而不是机械增加 may 或 robust。对应模式31。后文将缺失输入、权重、阈值和关键分项条件分别转成后续研究事项，对应模式35、41。

> The route comparison depends on the surveyed paths. Its ordering is stable under a common speed change, not necessarily under different speeds for different corridors.

上述语言没有把文字断言升级成已经运行过的敏感性实验。需要真正的实验或计算时，仍应回到相应验证记录。

## 使用状态

模式注册表、41条观察、40条 seed/low 候选规则与41条映射均保留在本目录，未写入正式 D 分支。句框占位符已经逐项赋予语义类型，所有变体的原始信息顺序、边界和82条例句都保留。具体词汇、连接词、主动/被动语态要服从信息任务，不作为人类文风的替代指标。

这些是单论文、文字范围内的可用候选。跨论文证据、版面统计、完整公式/视觉保真与正式事务尚未通过，不能宣称已交付最终 master skill。
