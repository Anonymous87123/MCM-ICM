#!/usr/bin/env python3
"""Create-only text-grounded language repair for D2015 38727.

Human-reviewed mechanisms below, mechanical serialization and source checks only.
Never installs, fabricates layout measurements, closes progress, edits a visual
artifact, or appends a transaction. Missing visual/layout proof remains a failure.
"""
from __future__ import annotations

import argparse
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

import stage_integrity_repair as storage
import validate_language_anticopy as anticopy
import validate_language_units as language

ROOT = storage.ROOT
PID = "P-D-2015-38727-eeb1090f"
SHA = "eeb1090fe4b2231af023d6bb25b69dc4db8eb570bb4ac2393f5caf426047aed0"
SOURCE_TERMS = ["bhutan", "bhutanese", "nigeria", "iceland", "sustainability", "refugees", "midwifery", "lateral"]


def normalized(text):
    text = unicodedata.normalize("NFKC", text).translate(str.maketrans({"’":"'", "‘":"'", "–":"-", "—":"-"}))
    return re.sub(r"\s+", " ", text).strip()


def mechanism(chapter, occurrences, function, frame, order, slots, variants, boundary, examples,
              voice="active", tense="present", modality="asserted purpose, not demonstrated efficacy", syntax="declarative", quantitative="none", pattern_target=None):
    return dict(chapter=chapter, occurrences=occurrences, function=function, frame=frame,
                order=order.split(" > "), slots=slots.split("; "), variants=variants.split("; "),
                boundary=boundary, examples=examples, voice=voice, tense=tense,
                modality=modality, syntax=syntax, quantitative=quantitative, pattern_target=pattern_target)


# Occurrences are (physical page, printed heading, local text locator, short excerpt).
# A text witness is not a newly verified figure/table reading.
MECHANISMS = [
    mechanism("abstract", [
        (1,"Summary","opening purpose","The objective of this model is to establish a comprehensive index")],
        "Open the Summary by introducing an output through the decisions it is intended to enable.",
        "[tool] identifies [condition] so [audience] can prioritise [action].",
        "deliverable > diagnostic use > planning use > audience decision",
        "tool; audience; diagnosed condition; prioritisation decision",
        "objective-first Summary; use-oriented Introduction closure",
        "Use when the output has a named decision role; do not substitute a list of hoped-for benefits for validated usefulness.",
        ["The catalogue flags conflicting dates so archivists can direct the next review round to uncertain entries.",
         "The route register identifies disconnected entrances, allowing the maintenance team to choose where temporary access is needed."]),
    mechanism("abstract", [(1,"Summary","assumption lead-in","The model assumes that:")],
        "Expose the conditions under which the method is intended to operate before presenting its claims.",
        "The analysis assumes [comparability], [representation], and [data condition].",
        "assumption lead-in > parallel conditions > later method",
        "comparability condition; representation condition; data reliability condition",
        "compact parallel list in Summary",
        "Use to make assumptions visible; a list is not evidence that the conditions hold, and it must not replace later justification.",
        ["For this comparison, labels are treated as independent records and each identifier is assumed to refer to one item.",
         "The access calculation keeps the timetable fixed and assumes that every marked doorway remains open during the observation period."]),
    mechanism("abstract", [
        (1,"Summary","method overview","Countries are scored across indices of sustainability:"),
        (3,"The Sustainability Index","decomposition","A set of 6 indices were defined for six categories")],
        "Describe a multidimensional output, then direct the reader to its explicit construction rather than imply one opaque total.",
        "We assess [object] across [dimensions]; [method section] explains [aggregation].",
        "evaluated object > named dimensions > component construction > documentation handoff",
        "object; dimensions; data inputs; construction location",
        "named dimensions in Summary; construction-oriented Methodology opening",
        "Use for a genuinely multidimensional representation; do not erase dimension-level differences or invent an overall scalar.",
        ["We describe each collection by completeness, legibility, and consistency; the next section defines the records used for each view.",
         "Each entrance is assessed for reachability and walking time, with the route-building rules documented separately."]),
    mechanism("abstract", [(1,"Summary","data choice and limit","There is no alternate subindex evaluation in the rare cases where data is unavailable for a country of interest.")],
        "Put an availability limit beside the method's advertised data advantage.",
        "[data choice] supports [intended comparison], but [missing case] has no [fallback].",
        "data-selection reason > advertised benefit > explicit uncovered case",
        "data-selection criterion; intended use; missing case; absent fallback",
        "strength followed by a concrete exception",
        "Use when the exception is known; completeness of selected data is not proof of robustness for unobserved cases.",
        ["The review uses scans with complete accession fields, but records without an identifier cannot enter the automatic matching step.",
         "Mapped corridors support the route comparison; an unrecorded doorway is left unresolved rather than assigned an assumed connection."]),
    mechanism("abstract", [
        (1,"Summary","case-selection sentence","Bhutan was selected for the assistance of the"),
        (7,"Case Study: Bhutan","data eligibility","A complete data set was available for the Kingdom of Bhutan")],
        "Name the selected case together with substantive and practical eligibility reasons.",
        "[case] was chosen because [relevant property] and [data eligibility] permit [analysis].",
        "selected case > substantive fit > practical eligibility > intended demonstration",
        "case; relevant characteristic; data availability; intended demonstration",
        "compressed Summary rationale; expanded case-study screening",
        "Use for a deliberately selected demonstration; selection for tractability does not establish representativeness.",
        ["The eastern collection was chosen because it contains both printed and handwritten labels and has a complete accession register.",
         "We examine the library entrance first because its usage is recorded throughout the day and both adjacent paths are mapped."],
        voice="passive", tense="past", syntax="selection clause with a reason"),
    mechanism("abstract", [
        (1,"Summary","projection direction","Bhutan was predicted to maintain or even increase their overall sustainability"),
        (15,"20-year changes to the Sustainability Index","qualified close","On the whole, Bhutan is on track to remain a model nation")],
        "Express a model-based future direction with forecasting modality rather than silently convert it to an observed outcome.",
        "Under [scenario], [output] is projected to [direction] over [horizon].",
        "scenario > future horizon > projected direction > qualified implication",
        "scenario; horizon; metric; direction; qualified implication",
        "was predicted in Summary; on-track formulation in results closure",
        "Use for conditional projections; neither wording proves that the intervention caused the projected change or that another case will follow it.",
        ["With the planned indexing schedule, the unresolved queue is projected to shrink during the next review cycle.",
         "If the temporary passage stays open, the route calculation suggests that the northern blocks will retain access during construction."],
        voice="passive", tense="future-in-past", modality="prediction, not observation", syntax="qualified projection"),
    mechanism("introduction", [(2,"Introduction","resource constraint","Resources available for developing nations are limited, so a method of prioritizing the needs and goals for development is needed")],
        "Turn a resource constraint into the need for an explicit prioritisation method.",
        "Because [resources] are limited, [audience] needs [prioritisation rule].",
        "competing needs > limited resource > prioritisation need > analytical task",
        "competing needs; resource constraint; decision maker; prioritisation method",
        "constraint-to-method-need opening",
        "Use when there is a real allocation constraint; scarcity alone does not validate the chosen ranking rule.",
        ["Only two reviewers are available this week, so the archive needs a rule for choosing which conflicts to inspect first.",
         "The maintenance window covers one corridor at a time; we therefore compare the access consequences before setting the repair order."],
        modality="necessity framed by a constraint", syntax="reason-to-need relation"),
    mechanism("introduction", [(2,"What does sustainability look like?","definition sequence","The essence of sustainability is stability. It is the ability to maintain a process or activity")],
        "Unpack an abstract term first through a short equivalence and then through an operational capacity at the relevant scale.",
        "[concept] centres on [core property]; at [scale], that means being able to [capacity].",
        "short definition > capacity restatement > application scale",
        "concept; core property; capacity; scale",
        "noun definition followed by ability statement and national-scale interpretation",
        "Use to clarify an author's operational meaning; do not present a contestable equivalence as the only valid definition.",
        ["For this register, traceability means an inspectable history. At record level, a reviewer must be able to recover the source of each correction.",
         "Here, connected access means a continuous usable path. At building level, every entrance must link to at least one such path."],
        syntax="definition followed by capacity restatement"),
    mechanism("introduction", [(2,"What does sustainability look like?","trade-off","Development can bring great prosperity to a nation, but this progress often comes at the expense of sustainability.")],
        "Create the problem through a tension between a desired benefit and a potentially sacrificed property.",
        "[change] may improve [benefit] while weakening [other objective]; the design must address both.",
        "desired benefit > possible cost > balancing task",
        "change; desired benefit; competing property; balancing decision",
        "benefit-concession-balance sequence",
        "Use when the competing objectives are explicit; do not assume every gain necessarily entails the stated cost.",
        ["Automatic merging shortens the queue but can hide competing readings, so the procedure must preserve disputed fields.",
         "A direct path reduces walking distance yet may concentrate traffic at one doorway; both effects belong in the access comparison."],
        modality="can, not inevitable", syntax="contrast with a balancing consequence"),
    mechanism("model-establishment", [(3,"The Sustainability Index","comparative and temporal uses","It also allows the user to determine which factors may be the greatest hindrance")],
        "Explain distinct uses of the same output across objects and across time, including a before/after comparison.",
        "[representation] compares [objects] and tracks [changes] against [reference].",
        "diagnostic use > cross-case comparison > longitudinal use > intervention comparison",
        "representation; comparison objects; time points; intervention reference",
        "side-by-side comparison; same-case temporal comparison",
        "Use to specify the planned comparison; before/after differences alone do not identify a causal intervention effect.",
        ["The register compares unresolved fields across collections and follows each collection through successive review rounds.",
         "The route map supports comparisons between buildings and between the normal layout and the temporary closure layout."],
        modality="capability claim", syntax="parallel use statements"),
    mechanism("model-establishment", [(3,"The Sustainability Index","design constraints","The indices were defined such that:")],
        "Disclose the construction conventions needed for a comparison to have a shared interpretation.",
        "[measures] use [common scale], [direction], and [data convention].",
        "availability requirement > common scale > preferred direction > shared data convention > weighting convention",
        "scale; direction; data reference; weighting convention; admissibility condition",
        "parallel requirement bullets before component definitions",
        "Use to expose construction choices; shared scale and equal weights do not demonstrate commensurability or suitable calibration.",
        ["Every review score uses the same field checklist, and a larger count always means more unresolved entries.",
         "Walking times are calculated from one path map and one speed assumption so the reported comparisons use a consistent convention."],
        voice="passive", tense="past", syntax="parallel design-condition list"),
    mechanism("model-establishment", [(3,"The Sustainability Index","threshold pair","Scores lower than 5.0 do not automatically imply sustainability")],
        "Separate a warning trigger from the stronger conclusion that the absence of a warning proves safety or adequacy.",
        "[threshold] triggers [warning]; falling below it does not by itself establish [stronger property].",
        "warning condition > asymmetric interpretation > limited negative conclusion",
        "threshold; warning; stronger property; excluded inference",
        "positive trigger followed by a do-not-infer qualification",
        "Use for a defined screening rule; do not recast an unvalidated source cutoff as a universal decision threshold.",
        ["Three conflicting fields trigger manual review; fewer conflicts do not certify that a record is correct.",
         "A detour beyond the reporting limit flags an entrance for inspection, but a shorter route does not establish that it is accessible to every visitor."],
        modality="explicit negation of a stronger inference", syntax="threshold plus qualification", quantitative="threshold and direction, not a transferable numeric cutoff"),
    mechanism("model-establishment", [
        (3,"Institutional Stability","definition","Institutional Stability quantifies the integrity of the infrastructure systems"),
        (4,"Environmental Stability","definition","Environmental Stability is a measure of how degraded various spheres of the environment"),
        (4,"Political Stability","decision use","It is designed to both indicate the need for political reforms and intervention"),
        (5,"Social Stability","decision use","The Social stability index may also help identify social factors"),
        (6,"Economic Stability","definition","The Economic Stability Index indicate the magnitude of poverty"),
        (6,"Risk Stability","relevance","Therefore the risk a country faces from large scale risk")],
        "Introduce each indicator by the condition it represents and the planning question it can inform.",
        "[indicator] represents [condition] and helps identify [decision need].",
        "indicator name > represented condition > relevance > decision use",
        "indicator; represented condition; affected object; intended decision",
        "quantifies definition; measure-of definition; may-help decision framing; relevance justification",
        "Use for a clearly delimited indicator; correlation with a condition is not a complete causal or construct-validity argument.",
        ["The conflict count describes disagreement between transcriptions and helps identify records that need a source check.",
         "The detour measure describes the extra walking required during a closure and helps locate entrances needing an alternative path."],
        modality="mixed: represents, is designed, may help", syntax="definition-to-purpose routine"),
    mechanism("model-establishment", [(4,"Institutional Stability","cutoff provenance","This scale was based on the World Bank calculated limits for expected years of education")],
        "Explain the external basis of a chosen classification rather than leave category boundaries unexplained.",
        "The [classification] follows [source basis] for [original purpose].",
        "classification > source basis > original context",
        "classification; source; original classification purpose; transfer limit",
        "source-anchored scale explanation after a definition",
        "Use when provenance is available; a borrowed boundary does not establish validity for a new purpose or population.",
        ["The review categories follow the archive's preservation manual, which distinguishes unreadable text from missing labels.",
         "Path classes use the survey's recorded width bands; the access study retains those bands rather than inventing finer measurements."],
        voice="passive", tense="past", modality="provenance claim", syntax="basis attribution"),
    mechanism("results", [(6,"Results","comparison sample","The countries were chosen based on their diverse cultures, environmental problems, political systems and regions of the world.")],
        "State why varied comparison cases were selected and distinguish the intended demonstration from universal validation.",
        "We selected cases spanning [contrasts] to examine [comparative use].",
        "sample construction > dimensions of variation > intended comparison",
        "sample; variation dimensions; intended test; inferential scope",
        "diversity rationale followed by a comparison purpose",
        "Use for purposive comparison; deliberately varied examples do not prove universal applicability or statistical representativeness.",
        ["We selected collections with typed, handwritten, and mixed labels to examine how the reconciliation rules handle different records.",
         "The comparison covers entrances at corners, courtyards, and long corridors so the route procedure encounters several layouts."],
        voice="passive", tense="past", syntax="selection rationale"),
    mechanism("results", [(8,"Case Study: Bhutan","complicating-factor exclusion, continuation from physical p7","was felt that the last two factors would significantly hinder the efficacy of development programs")],
        "Disclose that case screening removes complicating factors, thereby bounding the conditions of the demonstration.",
        "We avoid cases with [complication] because it would obscure [intended comparison].",
        "potential complication > expected interference > selection restriction",
        "complication; interference mechanism; eligibility restriction; excluded scope",
        "passive judgement followed by an exclusion rationale",
        "Use when a restriction is explicit; do not claim the resulting method has been tested under the excluded difficulty.",
        ["We exclude records with missing identifiers because identity uncertainty would obscure the comparison between transcription rules.",
         "The initial route check omits locked buildings so that access permissions do not confound the path-connectivity test."],
        voice="passive", tense="past", modality="author judgement", syntax="restriction with reason"),
    mechanism("results", [(8,"Case Study: Bhutan","goals traceability","The primary goals are intended to ensure sustainable growth, and have been developed in response to Bhutan's performance")],
        "Tie proposed priorities jointly to the preceding diagnosis and to the case's declared priorities.",
        "The proposed [goals] respond to [diagnosis] and align with [stated priorities].",
        "proposed goals > diagnostic origin > declared-priority alignment",
        "goal set; measured problem; declared priorities; intended beneficiary",
        "intended purpose followed by two sources of justification",
        "Use when both sources can be traced; alignment is not proof that the actions will deliver the promised effects.",
        ["The review priorities respond to repeated date conflicts and to the archive's stated aim of preserving uncertain readings.",
         "The temporary access plan addresses the disconnected paths found earlier and follows the site's priority of keeping the main hall reachable."],
        voice="passive", modality="intended benefit", syntax="dual-grounded justification"),
    mechanism("results", [(8,"Bhutanese Sustainability Index","two-sided benchmarks","Iceland has been included alongside Bhutan as a benchmark of high sustainability."),
                           (8,"Bhutanese Sustainability Index","contrast case","Nigeria is included for comparison of a developing nation with very poor sustainability")],
        "Make a case result interpretable through explicitly labelled contrasting reference cases.",
        "We compare [case] with [reference A] for [role A] and [reference B] for [role B].",
        "case > first reference and role > second reference and role > contextual comparison",
        "case; first comparator; first comparator role; second comparator; second comparator role",
        "high and low benchmark pair",
        "Use to orient a comparison; labelled references are neither a calibrated confidence interval nor proof that all intermediate cases behave alike.",
        ["The target collection is compared with a fully indexed archive and an unprocessed accession batch to make its remaining review load interpretable.",
         "We compare the temporary route with the normal entrance and the fully closed layout, stating what each reference represents."],
        voice="passive", tense="present perfect and present", syntax="paired comparator statements"),
    mechanism("results", [(9,"Institutional","score decomposition","The current Institutional Index for Bhutan is 4.1."),
                           (9,"Social","score explanation","Bhutan scores somewhat poorly in the social sector (5.1) because of"),
                           (10,"Political","score explanation","Bhutan's Political Sustainability index falls near the middle of the scale (4.7) because of")],
        "Report a score and immediately identify which recorded components the authors use to explain it.",
        "[case] receives [score]; the main reported contributors are [components].",
        "score > scale-relative interpretation > component explanation > decision relevance",
        "case; score; scale; component contribution; relevant action",
        "numeric result then causes; qualitative scale position then numeric payload and explanation",
        "Use when decomposition is supported; the authors' causal language must not turn an indicator association into a verified causal effect.",
        ["The batch has twelve unresolved fields, mostly dates and accession numbers, so those fields account for most of the next review round.",
         "The eastern entrance requires an extra four minutes of walking; the blocked cross-corridor explains most of the calculated detour."],
        modality="reported interpretation", syntax="result with component explanation", quantitative="score plus scale-relative interpretation and contributors"),
    mechanism("results", [(9,"Institutional","future demand","Assuming that the population centers of Bhutan will continue to grow the future need for a sanitation system is imperative")],
        "Link an existing service shortfall to a future need under an explicit growth condition.",
        "Given [current shortfall], continued [growth] would make [capacity response] necessary.",
        "current shortfall > conditional growth > future requirement",
        "service shortfall; growth condition; future capacity; action horizon",
        "assuming lead-in before an urgency claim",
        "Use when the growth assumption is declared; do not report conditional demand as an already observed outcome.",
        ["The catalogue already has a review backlog. If new accessions continue at the current rate, another review session will be needed before the next intake.",
         "The side path is narrow at present; continued use during the main-hall closure would require a separate arrival route."],
        modality="conditional necessity", syntax="assumption-to-future-need"),
    mechanism("results", [(10,"Environmental","external cause and local opportunity","There is room for improvement within Bhutan however, in the areas of indoor air quality")],
        "Distinguish an externally driven component of a poor result from the part local action could address.",
        "Although [external driver] affects [outcome], [local component] remains an actionable opportunity.",
        "reported poor outcome > external driver > local opportunity > limited action scope",
        "outcome; external driver; controllable component; local action",
        "external explanation followed by however and an internal opportunity",
        "Use to bound agency; do not infer the relative size or effectiveness of the local action without evidence.",
        ["An inherited register causes many identifier conflicts, but newly entered labels can still be checked against the accession book.",
         "The adjacent construction site determines the main closure, while signage inside the building remains under the venue team's control."],
        modality="room for improvement, not guaranteed success", syntax="concession with actionable remainder"),
    mechanism("results", [(10,"Risk","residual hazard","There is room for improvement through adopting stricter building codes and retrofit requirements")],
        "Prevent a favourable aggregate assessment from hiding a specific remaining exposure that warrants targeted action.",
        "Despite [favourable overall assessment], [specific exposure] calls for [targeted response].",
        "broad favourable result > remaining exposure > targeted response > operational constraint",
        "overall assessment; residual hazard; targeted action; response limitation",
        "low aggregate risk followed by a specific exception and response",
        "Use when the residual exposure is named; an overall low score must not be treated as absence of every hazard.",
        ["Most catalogue fields agree, yet several ownership dates remain disputed and require checking against the original register.",
         "The building retains a usable entrance, but the courtyard route still lacks lighting and needs a separate evening-access check."],
        modality="qualified improvement opportunity", syntax="favourable assessment with a residual exception"),
    mechanism("model-improvement", [(10,"The Bhutanese 20 year Sustainable Development plan","diagnosis-to-plan handoff","To address some of the problems identified in the Sustainability Index a 20 year development program for Bhutan is proposed.")],
        "Hand the diagnostic findings into a scoped intervention programme rather than present recommendations as an unrelated list.",
        "To address [diagnosed problems], we propose [programme] over [horizon].",
        "prior diagnosis > programme purpose > intervention structure > implementation horizon",
        "diagnosed problem; programme; intervention components; horizon",
        "purpose-led transition into a multi-part plan",
        "Use when a diagnosis-to-action link exists; a programme description is not a costed or causally validated intervention model.",
        ["To resolve the identifier conflicts found earlier, the archive proposes a two-stage register check before importing the next collection.",
         "The disconnected entrances motivate a temporary access programme covering route repair, signs, and opening schedules."],
        voice="passive", modality="proposal", syntax="purpose-led programme introduction", quantitative="declared planning horizon"),
    mechanism("model-improvement", [(11,"Educational Initiative","conditional support","women who agree to work in these fields for a period of at least five years")],
        "Make a proposed support mechanism conditional on a stated recipient commitment.",
        "[recipient] receives [support] if [commitment] is met for [duration or condition].",
        "support instrument > eligible recipient > commitment > duration > intended retention effect",
        "recipient; support; commitment; duration; intended benefit",
        "conditional tuition support contrasted with loan-funded alternatives",
        "Use to expose a proposed condition; do not assume recipients comply or that the retention objective is achieved.",
        ["Volunteers receive training access if they commit to two catalogue review sessions during the exhibition period.",
         "A room may borrow the portable signs provided its steward returns the complete set after each event."],
        modality="proposed conditional entitlement", syntax="support with an eligibility clause", quantitative="commitment duration, not an observed effect"),
    mechanism("model-improvement", [(11,"Educational Initiative","components","The college will consist of four major courses of study"),
                                    (12,"The Transportation Initiative","components","The central program of the Transportation Initiative is the repaving and improvement"),
                                    (12,"The Infrastructure Initiative","components","The infrastructure initiative consists of:")],
        "Make a proposal operational by decomposing it into concrete component programmes.",
        "[initiative] comprises [components], each addressing [implementation need].",
        "initiative purpose > component enumeration > concrete delivery mechanism",
        "initiative; component actions; delivery mechanism; responsible actor",
        "will-consist future specification; central programme plus additions; consists-of bullet list",
        "Use to specify the proposed work; listing components does not demonstrate costs, feasibility, or achieved effects.",
        ["The review programme comprises identifier checks, image comparisons, and a separate queue for unresolved readings.",
         "The temporary access scheme combines a repaired walkway, entrance signs, and a stewarded opening schedule."],
        tense="present and future", modality="proposed composition", syntax="composition statement with component list"),
    mechanism("model-improvement", [(11,"Educational Initiative","purpose list","This Initiative is intended to:"),
                                    (12,"The Transportation Initiative","purpose list","This Initiative is intended to:"),
                                    (13,"The Infrastructure Initiative","purpose list","The Infrastructure Initiative is intended to:")],
        "Separate the proposed activities from a parallel list of intended outcomes.",
        "The initiative is intended to [outcome A], [outcome B], and [outcome C].",
        "specified activities > purpose lead-in > parallel intended outcomes",
        "initiative; intended outcomes; affected recipients; scope of intent",
        "same intended-to lead-in across three programmes; varying outcome lists",
        "Use to state intent, not report results; the stated benefits still need a model, measurement, or evaluation path.",
        ["The label-review sessions are intended to resolve identifier conflicts, retain competing readings, and shorten the pending queue.",
         "The temporary passage is designed to keep the hall reachable and to separate arrivals from the maintenance work."],
        voice="passive", modality="intended, not observed", syntax="parallel infinitive outcomes"),
    mechanism("model-improvement", [(12,"The Transportation Initiative","targeted components","This will include the construction of bypasses of particularly dangerous sections of the road where possible")],
        "Translate a named operational bottleneck into a targeted fix while retaining an explicit feasibility qualifier.",
        "Where feasible, [targeted action] addresses [specific bottleneck].",
        "existing bottleneck > targeted component > feasibility qualifier > intended operational benefit",
        "bottleneck; targeted action; feasibility condition; operational benefit",
        "where-possible qualification embedded in a concrete programme component",
        "Use when the repair targets the diagnosed obstacle; do not drop the feasibility qualifier or imply the repair has been completed.",
        ["Where the original register is available, the reviewers check disputed dates against that register rather than infer them from nearby entries.",
         "The access proposal adds a short bypass around the closed stairway wherever the surveyed corridor width permits it."],
        tense="future", modality="where possible", syntax="specific intervention with an embedded condition"),
    mechanism("model-improvement", [(12,"The Infrastructure Initiative","priority rule","Priority for loans shall go to towns based on their population density, and level of need.")],
        "Expose the criterion governing who receives proposed support first.",
        "Priority for [resource] goes to [recipients] according to [criteria].",
        "support instrument > recipient class > priority criteria > allocation consequence",
        "resource; eligible recipients; prioritisation criteria; allocation rule",
        "shall-go priority statement inside an implementation bullet",
        "Use to make an allocation proposal inspectable; a named priority criterion does not by itself establish an optimal or equitable ordering.",
        ["The next review slots go first to collections with unresolved ownership fields and an imminent display deadline.",
         "Portable signs are assigned first to entrances whose usual path is closed and whose alternative route lacks a visible marker."],
        modality="proposed priority rule", syntax="allocation criterion with recipient class"),
    mechanism("model-improvement", [(13,"20-year changes to sustainability sub-index parameters","fixed remainder","All values not mentioned are considered to remain constant over the 20 year period.")],
        "Declare both which inputs the scenario changes and which inputs are held fixed.",
        "We update [listed inputs] for [scenario] and hold [remainder] fixed over [horizon].",
        "scenario intervention > listed input changes > fixed remainder > horizon",
        "changed inputs; scenario; unchanged inputs; time horizon",
        "positive update scope followed by an explicit all-unmentioned-values convention",
        "Use to make a scenario reproducible; fixed values are modelling assumptions, not forecasts that the world will actually remain unchanged.",
        ["For the extra-reviewer scenario, we change the number of review sessions and keep the incoming document mix unchanged.",
         "The closure scenario removes the west doorway while retaining the same walking-speed assumption and the other recorded paths."],
        voice="passive", modality="fixed-input modelling assumption", syntax="scope rule and fixed remainder", quantitative="explicit forecast horizon; no table-cell values extracted"),
    mechanism("results", [(15,"20-year changes to the Sustainability Index","exception to improvement","The only sector not improved was the environmental sustainability score for Bhutan.")],
        "Qualify an overall favourable projection by naming the non-improving component and the authors' explanation.",
        "The scenario improves [overall result], except for [component], which remains affected by [driver].",
        "overall projected direction > named exception > reported driver > bounded overall conclusion",
        "aggregate outcome; exception; proposed explanation; scope of conclusion",
        "only-sector-not-improved exception after an overall improvement claim",
        "Use to preserve heterogeneity; do not turn the projected overall benefit into improvement in every component or a verified causal result.",
        ["The additional review sessions reduce most conflicts, but ownership fields remain unresolved where the source register is missing.",
         "The revised route shortens most detours; the courtyard entrance still requires the long path because its connecting stairway remains closed."],
        tense="past in a model-result report", modality="projected result, not observation", syntax="overall result with a named exception"),
    mechanism("strengths-limitations", [(16,"Strengths and Weaknesses of the Sustainability Index","accuracy ceiling","The model is only as accurate as the available data used to calculate the indices."),
                                        (1,"Summary","early stability assertion","The model is not sensitive to small changes in data values"),
                                        (16,"Strengths and Weaknesses of the Sustainability Index","robustness condition","assuming that the variation in values is uniform across a given data set.")],
        "Read the early stability assertion together with the input-quality ceiling and the specific condition stated later.",
        "Reliability depends on [data condition]; the stability claim applies only if [perturbation condition].",
        "early stability assertion > later data-quality ceiling > specific perturbation condition",
        "input quality; accuracy limit; perturbation condition; tested or asserted scope",
        "unqualified Summary assertion; only-as-accurate body limit; however and assuming qualification",
        "Use to retain the stated limit; conditional robustness asserted in prose is not a completed sensitivity experiment.",
        ["Agreement between transcriptions cannot exceed the legibility of the source scan; stability under reordered entries does not address unreadable text.",
         "The route comparison depends on the surveyed paths. Its ordering is stable under a common speed change, not necessarily under different speeds for different corridors."],
        modality="conditional robustness assertion", syntax="accuracy bound and conditional contrast"),
    mechanism("strengths-limitations", [(16,"Strengths and Weaknesses of the Sustainability Index","category-assignment effect","Inclusion in one subindex or another may magnify or obscure a factor's impact")],
        "Connect a representation choice to the information it may amplify or conceal.",
        "Assigning [multi-cause factor] to [category] may obscure [other mechanism].",
        "multi-cause phenomenon > category assignment > possible distortion > interpretation limit",
        "multi-cause factor; category; amplified aspect; obscured aspect",
        "cannot-be-described-by-one-index claim followed by may-magnify-or-obscure contrast",
        "Use to discuss representation limits; the direction and size of any distortion still require evidence.",
        ["Treating every disagreement as a spelling error can conceal conflicts about identity, so the review record keeps those categories separate.",
         "Grouping all detours into one building average may hide the long route faced by visitors using the courtyard entrance."],
        modality="may, not quantified effect", syntax="representation choice with paired consequences"),
    mechanism("strengths-limitations", [(16,"Strengths and Weaknesses of the Sustainability Index","score-floor qualification","This does not necessarily reflect a lack of sustainable practices within a nation.")],
        "Block an intuitive but stronger interpretation of a reported score pattern and offer the relevant contextual explanation.",
        "[observed score pattern] does not necessarily mean [naive inference], because [contextual driver].",
        "reported score pattern > rejected inference > contextual explanation",
        "score pattern; tempting inference; contextual driver; interpretation boundary",
        "does-not-necessarily qualification after a reported lower score bound",
        "Use to prevent over-interpretation; the source's reported bound is not newly verified from a plot by this text-only review.",
        ["A high conflict count does not necessarily indicate careless transcription; a collection may contain more damaged originals.",
         "A long detour does not by itself show that the entrance was poorly placed, since the comparison includes a temporary corridor closure."],
        modality="not necessarily", syntax="inference-blocking qualification"),
    mechanism("strengths-limitations", [(17,"Strengths and Weaknesses of the Sustainability Index","scale of response","Distortion of indices/subindices of sustainability due to the influence of other countries can be used as indicators"),
                                        (1,"Summary","early disclosure of external influence","The model penalizes countries for foreign influence on subindices such as air pollution")],
        "Expose the boundary of local control, then distinguish a disclosed measurement limit from a proposed wider response.",
        "[external driver] limits [local agency]; where a response is proposed, consider [wider coordination].",
        "cross-boundary driver > limit to local agency > optional wider-response implication",
        "local boundary; external driver; coordinating actors; wider response scale",
        "Summary discloses an externally imposed penalty without a remedy; body reframes the control limit as a reason for wider coordination",
        "Use when the boundary is explicit; a wider response is a proposed governance scale, not evidence that a particular cooperative arrangement will work.",
        ["Some date conflicts originate in a shared register and cannot be settled from one collection's labels alone.",
         "A route closure spanning two venues cannot be handled by signs inside one building alone, so the access plan assigns a joint boundary check."],
        modality="proposed response scale", syntax="control limitation to coordination consequence"),
    mechanism("strengths-limitations", [(17,"Strengths and Weaknesses of the Sustainability Index","future work","Continued development of the model should incorporate the addition of methods to accurately estimate missing parameters")],
        "Turn the stated limitations into a finite, targeted future-work agenda.",
        "Further work should address [missing inputs], [weighting choice], and [decision threshold].",
        "identified limitations > separate repair targets > prospective evaluation",
        "missing information; combination rule; threshold; evaluation requirement",
        "three parallel improvement targets in the final author-written paragraph",
        "Use to propose checks and extensions; do not claim any unimplemented extension improves accuracy merely because it is more elaborate.",
        ["Further review should recover missing accession dates, test the conflict-priority rule, and examine which unresolved fields justify manual escalation.",
         "A later access study should resurvey unrecorded paths, compare alternative travel assumptions, and check the detour level used to trigger inspection."],
        tense="future", modality="should, prospective", syntax="parallel targeted research agenda"),
    mechanism("introduction", [(2,"Objective","use-oriented closing bridge","Thus the index is a tool to match up policy measures and unmet needs with their effects")],
        "Close the Introduction by turning its operational definition into a policy-to-measure link before Methodology starts.",
        "The [tool] connects [unmet need] and [candidate action] through [measured consequence].",
        "operational meaning > unmet need > candidate action > measured consequence > construction handoff",
        "tool; unmet need; candidate action; measured consequence; construction section",
        "Introduction closing variant of the objective-to-use mechanism; reverse emphasis from promised deliverable to audience operation",
        "Use as a traceable handoff into construction, not as evidence of causal policy efficacy. Separate this chapter-position variant from the Summary opening.",
        ["The register therefore links a disputed field to its source check and the correction that review can justify; the next section specifies how those links are recorded.",
         "The access assessment connects an unavailable entrance to a candidate diversion and its walking-time consequence, which the following route construction will compute."],
        modality="proposed operational use", syntax="thus-style use-oriented section closure", pattern_target=1),
]


def build(output):
    output.mkdir(parents=True, exist_ok=False)
    recipe = Path(__file__).read_bytes()
    storage.put_new(output / "recipe.py", recipe)
    manifest_path = ROOT / "artifacts/corpus/manifest.jsonl"
    manifest = language.find_manifest_record(manifest_path, PID)
    source = ROOT.parent / "MCM-ICM-master" / manifest["relative_path"]
    if manifest["sha256"] != SHA or storage.digest(source.read_bytes()) != SHA or manifest["page_count"] != 19:
        raise ValueError("source identity changed")
    input_paths = [manifest_path, source, ROOT / "artifacts/transactions/history.jsonl", ROOT / "artifacts/progress.jsonl"]
    input_paths += [ROOT / f"artifacts/{kind}/{PID}.{ext}" for kind, ext in [
        ("paper-cards","json"),("language-units","json"),("model-units","json"),
        ("learning-audits","json"),("observations","jsonl")]]
    input_paths.append(ROOT / f"artifacts/papers/{PID}/extraction.json")
    page_paths = [ROOT / f"artifacts/papers/{PID}/text/pages/page-{i:04d}.txt" for i in range(1,20)]
    input_paths += page_paths
    frozen = {str(p): storage.digest(p.read_bytes()) for p in input_paths}
    for kind,ext in [("language-units","json"),("paper-cards","json"),("learning-audits","json"),("model-units","json"),("observations","jsonl")]:
        storage.put_new(output / "before" / f"{kind}.{ext}", (ROOT / f"artifacts/{kind}/{PID}.{ext}").read_bytes())
    pages = {i: p.read_text(encoding="utf-8") for i,p in enumerate(page_paths,1)}
    units = []
    for index, spec in enumerate(MECHANISMS,1):
        occurrences = []
        for page,heading,locator,excerpt in spec["occurrences"]:
            if normalized(excerpt) not in normalized(pages[page]):
                raise ValueError(f"unconfirmed source excerpt: unit {index}, p{page}: {excerpt}")
            occurrences.append({"page":page,"printed_page":None if page == 1 else page-1,
                                "section":heading,"locator":locator,"source_excerpt":excerpt})
        locations = [f"physical p{o['page']}, {o['section']}, {o['locator']}" for o in occurrences]
        first = occurrences[0]
        pattern_index = spec["pattern_target"] or index
        if not 1 <= pattern_index <= index:
            raise ValueError("in-draft pattern reference must refer to a preceding mechanism")
        pattern = f"CP-D-2015-38727-REPAIR-{pattern_index:02d}"
        unit = {
            "language_unit_id":f"LU-D-2015-38727-REPAIR-{index:03d}",
            "paper_id":PID,"problem_type":"D","chapter":spec["chapter"],"paper_chapter":spec["chapter"],
            "page":first["page"],"printed_page":first["printed_page"],"section":first["section"],"printed_section":first["section"],
            "granularity":"paragraph","source_excerpt":first["source_excerpt"],
            "function":spec["function"],"rhetorical_move":spec["function"],"reusable_pattern":spec["frame"],
            "information_order":spec["order"],"candidate_pattern_ids":[pattern],"occurrences":occurrences,
            "reusable_elements":["occurrences: "+"; ".join(locations),"stable function: "+spec["function"],
                                 "order: "+" > ".join(spec["order"]),"slots: "+"; ".join(spec["slots"]),
                                 "variants: "+"; ".join(spec["variants"]),"cross-paper support: none established"],
            "prohibited_generalizations":["boundary: "+spec["boundary"],
                "Do not copy source clauses, source-specific facts, or any unique run of eight consecutive source content words."],
            "features":{"voice":spec["voice"],"tense":spec["tense"],"modality":spec["modality"],
                        "clause_structure":spec["syntax"],"quantitative_role":spec["quantitative"],
                        "transition":" > ".join(spec["order"]),"original_instantiations":spec["examples"]},
            "g3":{"occurrences":locations,"stable_function":spec["function"],"order":spec["order"],
                  "slots":spec["slots"],"variants":spec["variants"],"boundary":[spec["boundary"]],
                  "cross_paper_support":[],"cross_paper_support_count":0,"disposition":pattern},
            "disposition":("supports existing in-draft candidate: " if spec["pattern_target"] else "opens candidate: ")+pattern+"; single-paper, not promoted or saturated",
        }
        units.append(unit)
    record = {"schema_version":3,"paper_id":PID,"problem_type":"D","year":"2015","source_sha256":SHA,
              "review_status":"draft","available_chapters":list(dict.fromkeys(u["chapter"] for u in units)),"units":units,
              "source_specific_terms":SOURCE_TERMS,"layout_review_status":"pending",
              "draft_scope":"Text-grounded language repair; quantitative visual layouts intentionally absent, no G0-G8 completion claim."}
    record_path = output / "language-units.draft.json"
    storage.put_new(record_path,storage.encoded(record))
    text = "\n\f\n".join(pages.values())
    profile = anticopy.build_source_profile(text,8)
    scans = [anticopy.scan_unit_with_profile(u,profile,8,set(SOURCE_TERMS)) for u in units]
    unit_errors = [e for i,u in enumerate(units,1) for e in language.validate_unit(u,"D",19,None,i)]
    record_errors = language.validate_record(record,None,manifest)
    changed = [p for p,h in frozen.items() if storage.digest(Path(p).read_bytes()) != h]
    if changed:
        raise ValueError("live input changed during build")
    report = {"paper_id":PID,"status":"draft-incomplete-not-committable","unit_count":len(units),
              "chapter_counts":dict(Counter(u["chapter"] for u in units)),"original_example_count":sum(s["example_count"] for s in scans),
              "source_witnesses":sum(len(u["occurrences"]) for u in units),
              "distinct_candidate_patterns":len({p for u in units for p in u["candidate_pattern_ids"]}),
              "frozen_recipe_sha256":storage.digest(recipe),"unit_structure_errors":unit_errors,
              "anticopy_failures":[s for s in scans if s["result"]!="pass"],
              "maximum_shared_content_run":max(s["maximum_shared_content_run"] for s in scans),
              "full_record_errors_retained":record_errors,"input_sha256":frozen,
              "candidate_sha256":storage.digest(record_path.read_bytes()),"anticopy_results":scans,
              "unresolved":["Visual layout measurements and exact paragraph segmentation unverified while figure/chart work is paused.",
                            "G2 final saturation not yet certified; cross-paper catalogue integration not performed.",
                            "Original closure transaction missing; no historical event or present-time closure has been fabricated.",
                            "Existing model/visual retention is not certified by a language repair."]}
    storage.put_new(output / "validation.json",storage.encoded(report))
    if unit_errors or report["anticopy_failures"]:
        raise ValueError("candidate unit structure or anti-copy failed; diagnostic retained")
    print(json.dumps({k:v for k,v in report.items() if k not in ["input_sha256","anticopy_results","anticopy_failures"]}),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    build(args.output.resolve())


if __name__ == "__main__":
    main()
