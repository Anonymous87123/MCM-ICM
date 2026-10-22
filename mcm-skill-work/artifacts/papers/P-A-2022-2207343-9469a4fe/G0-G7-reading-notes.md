# P-A-2022-2207343-9469a4fe Reading Notes

Status: in-progress staging notes only. These notes are not canonical language,
model, audit, observation, paper-card, rule, or transaction artifacts.

## Provenance and G0

- Queue position: 62.
- Source: `2022美赛特等奖/A/2207343.pdf`.
- Manifest and live PDF SHA-256: `9469a4fe5ecc19cbbc156e71ff3bac977868f2e583619d0cc3b70dc707a1e67a`.
- Award/type evidence: outstanding paper in the primary Problem A folder.
- Physical pages: 25; paper-numbered pages: 22 plus Summary and Contents.
- Extracted text: 42,264 non-whitespace characters and 9,094 word tokens;
  coverage is 25/25 with no empty pages.
- Rendering: all 25 pages at 200 DPI. Seven contact sheets were inspected.
  No blank, clipped, overlapped, unreadable, or missing page region was found.
- Visual review covers the Summary, contents, Figures 1-23, Tables 1-11,
  numbered Equations 1-17, the unnumbered corner-speed equation marked `(*)`,
  course maps, sensitivity panels, team formations, references, and both
  RIDERMAN guidance pages.
- Extraction validator status: pass; visual review status: complete.

## Observable Paper Route

The paper follows a clear model-to-decision staircase:

`official rider/course tasks -> three-stage physiological power curve ->
remaining-energy integral -> force and Pout-v conversion -> segment and
corner classification -> piecewise nonlinear programming -> three course
strategies -> weather and execution perturbations -> team formations ->
evidence-calibrated strengths/limits -> two-page rider guidance`.

The route is stronger than a topic list because each stage emits an object
consumed later. The power-duration curve supplies `T(P)`; the energy model uses
`1/T(Pout)`; bicycle dynamics supplies section-specific `v(P)`; track
segmentation supplies the piecewise objective; course solutions supply
sensitivity baselines; headwind sensitivity supplies the team-formation
motivation; all results supply the rider-facing guidance.

## Page and Chapter Map

- Page 1, Summary: exactly seven visual paragraphs move through (1) a
  contrastive hook and modeling promise, (2) Task 1 and the three-stage rider
  curves, (3) Task 2 and the complete model-to-time chain, (4) weather
  sensitivity and its team-strategy handoff, (5) rider-deviation feasibility
  and time lag, (6) Task 5's three formations, and (7) the Directeur Sportif
  deliverable. The keywords line is not an eighth author paragraph.
- Pages 3-4, Introduction: exactly six visual paragraphs move through (1) the
  power-curve definition and shape, (2) its pacing use, (3) the complete
  official-task and audience ledger, (4) the two-parameter CP model's valid
  domain and uncovered regime, (5) the three physiological domains and their
  candidate models, and (6) the two-model work plan, tests, and team extension.
  Figure 2 redundantly visualizes the sixth paragraph's route.
- Page 5, Assumptions/Notation: three assumptions with reasons, followed by a
  compact symbol/unit table.
- Pages 5-7, Three-stage model: source-data contract, CP/W-prime estimates,
  stage thresholds, three power-duration branches, and rider-profile curves.
- Pages 7-9, Energy and dynamics: discrete-to-continuous remaining-energy
  logic, the 0.95 operational reserve, force balance, and the Pout-v interface.
- Pages 9-12, Self-designed course: Webots geometry, corner-speed bound,
  straight/ramp objective, discretization, Mathematica solution, and turn
  decisions.
- Pages 12-14, Belgium course: 32-part terrain decomposition, small-slope
  aggregation, section optimization, time results, and turn checks.
- Pages 14-17, Tokyo course: 68 segments, regular-section aggregation, two
  special road complexes, local speed/power calculations, and total times.
- Pages 17-20, Sensitivity/verification: weather scope reduction, straight and
  turn wind perturbations, random rider-deviation curves, finish feasibility,
  time lag, and comparison with actual winners.
- Pages 20-22, Team/evaluation: drafting evidence, pyramid/snake/shield stages,
  crosswind echelon, strengths, weaknesses, and conclusion.
- Pages 23-25, References and guidance: source list and a two-page stakeholder
  artifact that changes vocabulary, visual density, and action granularity.

## Positive Language Mechanisms Learned So Far

These are source-anchored candidates that still require final unit-level
occurrence reconciliation, typed slots, variants, two unrelated examples, and
the full-source anti-copy scan before G8.

1. Page 1 Summary hook: a domain anecdote is used only long enough to name the
   decision problem, then the paper immediately promises a mathematical model.
   Reusable order: accessible surprise -> domain stakes -> modeling promise.
   Boundary: use for a real, relevant bridge; do not replace task reconstruction
   with decorative storytelling.
2. Page 1 Summary task staircase: each Task paragraph names the upstream model,
   the new transformation, the downstream output, and a numerical or visual
   result. Reusable order: task label -> inherited input -> operation -> output
   -> implication.
3. Page 1 Summary evidence calibration: the completion-time table precedes the
   statement that the model lags the champion within 6 percent. The reusable
   mechanism is comparator -> metric -> bounded claim, not the source wording.
4. Page 1 Summary sensitivity split: weather and rider execution are handled in
   separate paragraphs so their perturbation variables and decision meanings
   are not conflated.
5. Page 1 Summary extension close: the headwind result is explicitly used to
   motivate team formation, and the paper ends by naming the receiving
   Directeur Sportif. This is result -> extension trigger -> stakeholder.
6. Page 3 problem context: the paper defines the power curve by function before
   listing its applications. Reusable order: object definition -> qualitative
   shape -> operational use -> task need.
7. Pages 3-4 task ledger: the official tasks retain rider types, genders, three
   tracks, weather, execution deviation, six-rider/fourth-finisher logic, and
   the two-page guidance audience. The list acts as a coverage contract.
8. Page 4 literature contrast: a two-parameter CP model is named, its valid
   exercise domain is bounded, the uncovered domain is identified, and this
   gap motivates a three-stage portfolio. Reusable order: prior model -> valid
   scope -> omitted regime -> selection consequence.
9. Page 4 workflow close: the prose previews two core models, validation on
   riders/tracks, and a team extension before Figure 2 visualizes the same
   route. Prose and figure provide redundant navigation.
10. Page 5 assumptions: every assumption is followed by a physical, seasonal,
    literature, or drivetrain reason. The transferable form is assumption ->
    reason -> affected interface, with the transfer boundary made explicit.
11. Page 5 notation handoff: the notation sentence is deliberately short; the
    table then binds symbol, definition, and unit before any equation chain.
12. Pages 5-6 data-to-parameter passage: source durations and rider categories
    are named before CP, W-prime, and threshold parameters are calculated.
    This is data inventory -> calculation method -> typed parameter table.
13. Page 6 equation introduction: CP and W-prime are defined semantically and
    physically before Equations 1-2 appear; the following `where` clause ties
    P3/P12 to measured durations and mass.
14. Page 7 regime table: Extreme, Severe, and Heavy are aligned in one table with
    model family, equation, and valid time range. This makes model selection a
    visible conditional contract rather than a prose-only choice.
15. Page 7 result interpretation: the authors read Figure 3 in a fixed sequence:
    gender ordering -> short-burst specialization -> middle/long-distance
    specialization. The mechanism is visual pattern -> comparison -> decision
    meaning, with no claim of causal physiology beyond the source data.
16. Page 8 discrete-to-continuous derivation: a schematic first shows discrete
    rectangles; prose then replaces the sum by an integral and names the
    inverse-function interface. Reusable order: discrete intuition -> limiting
    operation -> continuous equation -> symbol meaning.
17. Page 8 practical reserve: after stating the mathematical equality, the paper
    explains why strict adherence is unrealistic and changes 1.00 to 0.95.
    Reusable order: ideal constraint -> execution failure mode -> conservative
    operational margin.
18. Pages 8-9 dynamics handoff: the force ledger is introduced before its
    components are expanded; only then is `m Pout = Ftotal v` used to create the
    power-speed conversion. Reusable order: total balance -> component laws ->
    calibrated constants -> interface output.
19. Pages 9-10 synthetic-course rationale: the self-designed course is framed
    as a controlled library of road conditions whose strategies will later be
    reused on real tracks. This is test environment -> mechanism isolation ->
    transfer target.
20. Page 10 corner analysis: expected behavior is stated first, geometry and
    force relations second, the maximum-speed bound third, and approximation
    boundaries last.
21. Pages 10-11 optimization statement: section types and counts are defined
    before the objective and energy constraint. Discretization is justified by
    computation and by the rider-facing need for a landscape-indexed Pout plot.
22. Page 11 table comparison: Table 5 gives straight/ramp decisions, Table 6
    gives turn decisions, and the prose identifies which turns require
    deceleration and why.
23. Pages 12-13 Belgium transfer: observed terrain statistics justify reusing
    the synthetic-course model; small slopes are grouped only after the paper
    explains the convergence problem and approximate linearity.
24. Pages 14-16 Tokyo exception routing: regular segments use the shared model,
    while two named special complexes are removed and solved separately. This
    is default rule -> exception detector -> local model -> reintegration.
25. Pages 17-18 sensitivity scoping: temperature, humidity, and rain are bounded
    before wind is selected; straight and turning regimes then receive separate
    perturbation interpretations.
26. Pages 19-20 execution sensitivity: ideal discrete output -> spline
    interpolation -> bounded random sine disturbance -> three executions ->
    energy feasibility -> time-lag metric -> practical recommendation.
27. Page 20 validation wording: model and champion times are shown before the
    explanation that average-rider inputs may account for the gap. The valid
    claim is scenario agreement, not proof that the strategy creates champion
    performance.
28. Pages 20-21 team extension: literature drag ratios -> candidate formations
    -> three stages with distinct goals -> selection by average resistance and
    role constraints -> team/individual comparison.
29. Page 22 evaluation list: each strength names a mechanism or test, but its
    evidence strength must be audited separately. The reusable form is claim ->
    supporting artifact -> bounded consequence.
30. Pages 24-25 audience switch: technical terms are reduced to track classes,
    power adjustments, tables, and a fill-in turning formula. The stakeholder
    version preserves conditions and rider-type distinctions rather than merely
    simplifying vocabulary.

## Model and Equation Retention Map

1. Pages 6-7, rider-parameter layer: Equations 1-2 estimate CP and W-prime from
   P3 and P12; Equation 3 defines a stage threshold; Table 4 supplies the three
   piecewise power-duration branches and thresholds MAPTTF/CPTTF.
2. Pages 8-9, energy layer: Equation 4 is the discrete remaining-energy ratio;
   Equation 5 is its continuous integral; Equation 6 imposes finish-line energy
   use before the practical 0.95 reserve is substituted.
3. Pages 8-9, bicycle dynamics: Equation 7 is total force divided by efficiency;
   Equations 8-11 define rolling, slope, inertial, and wind forces; the text
   combines them with `m Pout = Ftotal v` to obtain section-specific `v(P)`.
4. Page 10, corner model: the unnumbered `(*)` equation maps friction, slope,
   road width, inner radius, and turning angle to maximum speed.
5. Pages 10-11, synthetic course optimizer: Equation 12 minimizes total section
   time subject to the integral energy budget after Pout discretization.
6. Pages 13-14, Belgium optimizer: Equation 13 reuses the objective; Equations
   14-15 aggregate selected small slopes by length weights; Equation 16 adds the
   integrated slope group to the piecewise objective.
7. Page 15, Tokyo regular-section optimizer: Equation 17 extends the objective
   with separately grouped two-degree and four-degree slope classes.
8. Pages 16-17, special sections: local geometry, turning speed, power, and
   acceleration/deceleration timing are calculated outside Equation 17 and then
   reintegrated into total course time.
9. Pages 18-20, perturbation models: wind changes the power-speed interface;
   rider execution is represented by a four-term bounded random sine series
   added to a spline interpolation of the ideal Pout curve.
10. Pages 20-21, team formation layer: literature-derived drag multipliers and
    stage shares select pyramid, long snake, shield, and diagonal formations.
    No complete team optimization equation is printed, so this interface must
    be marked partial rather than silently reconstructed as a formal solver.

## Important Visuals and Their Analytical Jobs

- Figure 1: intuitive power-duration shape before the formal model.
- Figure 2: global dependency map linking power profile, optimization,
  sensitivity, team strategy, and the Directeur Sportif.
- Figure 3: aligned rider-type/gender power curves over three time windows.
- Figures 4-5: discrete-to-continuous energy and force-to-power-speed mechanism.
- Figures 6-8: controlled course geometry, section classification, and final
  section power trace.
- Figures 9-12: Belgium source map, terrain division, local detail, optimized
  rider traces, and turn feasibility overlay.
- Figures 13-17: actual-output bridge, Tokyo division, regular-section power
  traces, and the two special road complexes.
- Figures 18-21: wind and execution sensitivity, including ideal/actual curves,
  energy feasibility, and time lag.
- Figures 22-23: formation drag heat maps, stage allocation, and crosswind
  diagonal formation with a real-race comparator image.
- Tables 1-4: notation, input rider data, derived parameters, and conditional
  model selection.
- Tables 5-10: synthetic, Belgium, and Tokyo decisions and results.
- Table 11: model-to-champion time comparison.
- Pages 24-25: stakeholder artifact with track classification, action tables,
  power curves, and a fill-in corner-speed calculation.

Additional visual-reading boundaries:

- Figure 12's caption says "maximum rate" while the adjacent prose and plotted
  quantity mean maximum turning power; the visual record must retain the
  terminology conflict instead of silently renaming the source.
- Figure 18's output curve appears to span roughly -27 percent to +34 percent
  under a +/-1 percent input-axis perturbation, which does not visually support
  the prose's undefined "10 percent" deviation without a separate metric.
- Figure 20 reaches roughly +1.7 percent and -2.2 percent in its two response
  panels, conflicting with the prose's 0.1 percent and 0.01 percent orders of
  magnitude.
- The two guidance pages rely heavily on red/green discrimination and use very
  small curve labels. They are deployable in structure but require redundant
  symbols, larger type, unit checks, and safety margins before operational use.

## Numerical Results to Bind to Conditions

- Self-designed course times (minutes): male/female sprinter 47.53/48.58;
  male/female time-trial specialist 46.48/48.20.
- Belgium times: 58.15/59.62 for sprinters and 53.03/54.05 for specialists.
- Tokyo times: 62.68/56.03 for sprinters and 40.97/33.63 for specialists.
- Wind conclusion: roughly 10 percent straight/headwind sensitivity versus
  reported 0.1 percent direction and 0.01 percent speed effects in turns.
- Rider disturbances: all three perturbed executions remain energy-feasible;
  time lag is reported below 2.5 percent.
- Actual winner comparison: model 56.03/34.63 minutes versus 55.08/30.22.
  This is not the same pair printed in all earlier tables and needs exact
  reconciliation before a final observation is accepted.
- Team straight: 24.8-minute individual versus 21.2-minute team; stage shares
  48/27/25 percent; modeled speed 56.6 km/h versus cited 56.1 km/h.

## G7 Warning Candidates

Warnings remain unopened as formal observations until positive G1-G6 records
are complete. These are source-anchored candidates for the final warning pass.

1. Page 1 says the model lags the champion within 6 percent, page 22 concludes
   about 8 percent for Belgium and 6 percent for Tokyo, while Table 11 values
   imply different gender-specific errors. Denominators and pairings need an
   exact arithmetic audit.
2. The Summary says crosswind sensitivity is within 1 percent and headwind
   impact is 10 percent; pages 18-19 report 0.1 percent and 0.01 percent effects
   in turns. Regime, perturbation magnitude, and output metric must be kept
   separate.
3. Assumption 1 selects narrow temperature/humidity ranges from event timing,
   but no venue observations, dates, distributions, or uncertainty are shown.
4. Assumption 2 equates energy use for equal power/time across physical states;
   the cited lactic/ATP discussion does not establish rider-state invariance.
5. Assumption 3 calls a 5 percent drivetrain loss an energy loss by cyclists;
   physiological reserve and mechanical efficiency are different interfaces.
6. Equation 1's dimensions and the definition of P12/P3 need checking; Equation
   2 multiplies by `0.24s` without explaining the duration conversion.
7. Equation 3 is poorly typeset and its threshold symbols are not fully defined;
   Table 3 units for W-prime and threshold times are incomplete.
8. Table 4 adopts `k=0.7` and `A=0.1` from continuity without showing the
   equations, units, fit residuals, or uncertainty that determine them.
9. Figure 3 interpretation treats gender curve ordering as consistent with
   general strength without source-sample size, matching, or uncertainty.
10. The energy model sums fractions of maximal holding time, which assumes
    linear additive depletion across variable power. Recovery below CP and
    path dependence are omitted.
11. Equation 6 states complete energy use but the implementation changes the
    target to 0.95. This is an operational safety margin, not a derived optimum.
12. The total-force equation divides a sum of forces by efficiency and then
    combines it with rider mass-normalized power; mass, bicycle mass, and force
    conventions require a dimensional closure audit.
13. Wind resistance uses `vwind^2` while the prose sets `vwind=vbike` in no wind;
    the variable appears to mean relative air speed in one place and ambient
    wind in another. Only frontal incident flow is supported.
14. The corner equation uses road/turn geometry whose diameter/radius notation
    is inconsistent; later Tables 8-9 contain zero or near-zero lengths/radii
    and mislabeled `km`, `m`, and degree columns.
15. The synthetic-course solver omits raw track geometry, all decision bounds,
    solver options, starting values, tolerances, and convergence evidence.
16. Acceleration/deceleration time is ignored even though the model later gives
    explicit 20 m braking and reacceleration instructions for Tokyo turns.
17. Belgium slope aggregation relies on an approximate linearity statement but
    does not report aggregation error or compare optimized decisions before and
    after grouping.
18. Tokyo grouping thresholds and sets are printed, but full segment arrays and
    reconstructable membership/length/slope data are absent.
19. Wind sensitivity uses different stated perturbations (1 percent, 10 percent,
    1-4 m/s, and plus/minus 2 m/s) without one common baseline or effect-size
    definition. Stochastic optimizer variation is not separated from wind.
20. Rider disturbance uses only three experiments; the random-number
    distribution, seed, phase, amplitude sampling, spline rule, and matched
    comparison protocol are not supplied.
21. Calling finish feasibility `excellent stability` and sub-2.5-percent lag
    low sensitivity is stronger than three unreported random realizations can
    establish.
22. The paper says the strategy brings average riders close to champion results,
    but this comparison is not a held-out causal validation and uses different
    rider/time pairs across tables.
23. Team drafting coefficients are drawn from literature and heat-map figures,
    but the coefficient table, formation geometry, rider rotation, energy
    updates, collision/safety constraints, and fourth-finisher objective are not
    reproduced as a complete executable model.
24. Stage shares 48/27/25 and the 21.2-minute result have no printed objective,
    search method, parameter values, sensitivity, or uncertainty.
25. The speed comparison to the 2018 Tour de France BMC team is a contextual
    comparator, not validation of equal distance, weather, formation, terrain,
    rider ability, or timing rules.
26. Strength claims of accuracy, universality, stability, and high fault
    tolerance exceed the evidence unless each is bound to its specific
    scenario, internal check, and missing external tests.
27. The guidance uses hard percentages and track thresholds that are not all
    traceable to a displayed sensitivity/optimization result, and it introduces
    different RIDERMAN/RIDEMAN/RIDERMEN spellings.
28. No appendix or code listing publishes rider source rows, track arrays,
    Webots geometry, Mathematica notebook, Python scripts, random seeds,
    formation coefficients, or plotted data. End-to-end reproduction is not
    possible from the paper alone.

29. Figure 21's worst run is 54.38 minutes against a 53.03-minute baseline,
    so the relative lag is about 2.55 percent. This slightly exceeds the
    prose's "within 2.5 percent" boundary and also differs from the Summary's
    "within 2 percent" statement.
30. Table 10 prints Tokyo specialist times of 40.97 and 33.63 minutes, whereas
    Table 11 uses 56.03 and 34.63. The former 56.03 belongs to the female
    sprinter row in Table 10, and 34.63 does not match 33.63. These values
    cannot be combined into one validation chain.
31. Table 11's model/champion pairs imply approximately 1.7 percent and 14.6
    percent relative differences, not a common approximately 6 percent error.
    The claimed Tokyo accuracy therefore cannot be reproduced from the printed
    table.
32. The team discussion announces a 1 km straight on page 20 but formulates
    and reports a 20 km exercise on page 21. The stage shares 48/27/25 and the
    21.2-minute result have no printed objective, search derivation, or
    formation-switch cost.
33. Table 9 contains malformed labels and fields: rows appear as #55km/#56km,
    lengths as 0.2m/approximately 0m, and radius/angle values under mismatched
    headings. It must remain a diagnostic visual, not a trusted parameter table.
34. The page-24 claim connecting Anna van der Breggen, the Tokyo individual
    time-trial champion, mathematics, and a Cambridge PhD requires external
    verification. It is excluded from reusable factual evidence here.
35. RIDERMAN, RIDEMAN, and RIDERMEN name the same intended guidance system on
    adjacent pages; the naming inconsistency must be resolved before packaging
    a stakeholder artifact.

## Remaining G1-G8 Work

1. Preserve the reconciled 7-paragraph Summary and 6-paragraph Introduction
   chains in the formal audit and link every paragraph to positive units.
2. Measure all normalized chapter layouts with source-line exclusions.
3. Complete at least two positive-language passes per chapter and record the
   final zero-new-move pass without padding repeated variants.
4. Convert accepted language mechanisms into explicit schema-v3 records with
   occurrences, function, order, typed slots, variants, boundary, two unrelated
   examples, and full-source anti-copy results.
5. Retain every displayed numbered equation exactly once and decide how to
   represent Table 4 branches, the `(*)` equation, random disturbance, and team
   formation interfaces without inventing source equations.
6. Build exact model dependencies, visual dispositions, section contracts, and
   main argument chains before opening formal G7 warnings.
7. Select only genuinely applicable existing A rules and stage the evidence
   append before any canonical type-branch update.
8. Run all validators, prospective history/progress/compliance/rolling checks,
   freeze hashes, append once, update live derived reports, and only then select
   queue 63.
