#!/usr/bin/env python3
"""Entries for The Unsolved Industrial Engineering Database
(unsolved-industrial-engineering) and its Signature half
(unsolved-industrial-engineering-signature).

34 famous unsolved problems in industrial engineering, ladder-ordered by
accessibility (rank 1 = most approachable, rank 34 = most complex).
Public half: real, fact-checked problems. Signature half: the same 34
through the Signature lens, ALWAYS labeled as proposals, never established
science.

ID prefixes JAH-USIE- / JAH-USIES- verified free in manifest id_prefix
values (exact + substring, both directions).
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

FIELD = {
 "tag": "industrial-engineering",
 "disp": "industrial engineering",
 "name": "The Unsolved Industrial Engineering Database",
 "sig_name": "The Unsolved Industrial Engineering Signature Database",
 "prefix": "JAH-USIE-",
 "sig_prefix": "JAH-USIES-",
 "ai": "JAH Unsolved Industrial Engineering Archivist",
 "tagline": ("Thirty-four famous open problems in industrial engineering, from line balancing to unified "
             "human-machine design: real, fact-checked, each with its full story and a clearly labeled "
             "Signature proposed solution."),
 "sig_tagline": ("His original Signature solution method applied to all 34 great open problems of industrial "
                 "engineering: Signature-generated proposed solutions with assumptions declared, confirm and "
                 "refute conditions stated, and limits honestly marked. Clearly labeled Signature-made, "
                 "never established science."),
 "pub_line": ("Public records - 34 famous open problems in industrial engineering, real and fact-checked: "
              "assembly line balancing, facility layout, bottleneck identification, work measurement, learning "
              "curves, equipment effectiveness, die exchange, process control for autocorrelated data, small-batch "
              "quality, tolerance allocation, and shift-work optimization - every record carrying the problem "
              "statement, background, why it matters, key points, requirements, standards, citations, and a "
              "working solution-explorer demonstration, organized in the Signature system."),
 "sig_line": ("Signature originals - his original Signature solution method: the same 34 famous unsolved "
              "industrial engineering problems approached as a covenant between the known and the unknown, each "
              "carrying the full Signature-generated proposed solution with its assumptions declared, its "
              "confirm and refute conditions stated, and its limits honestly marked. Clearly labeled "
              "Signature-made, never presented as established science or authentic public record."),
 "ladder_text": (" Records are ordered by the teaching ladder: Foundations (line balancing, facility layout, "
                 "bottlenecks, knowledge-work measurement, learning curves, equipment effectiveness, die "
                 "exchange, autocorrelated process control, small-batch quality, tolerance allocation, shift "
                 "work) -> Compounded (cellular manufacturing, flexible scheduling, predictive maintenance, "
                 "digital twins, lean against resilience, warehouse slotting, order picking, planning hierarchy, "
                 "lot sizing, human-robot collaboration, exoskeletons, safety culture) -> Advanced (cognitive "
                 "workload, injury prediction, experiments for complex systems, response surfaces, disruption "
                 "network design, theory of constraints limits, jidoka limits, resilience quantification, "
                 "material handling selection, setup sequencing, unified human-machine design)."),
 "search_ph": ("Search line balancing, facility layout, bottlenecks, predictive maintenance, digital twin, lean, "
               "warehouse, ergonomics, safety culture, resilience..."),
 "chat_ph": "Ask about the great open problems of industrial engineering...",
 "greet_pub": ("I am the JAH Unsolved Industrial Engineering Archivist. Ask me about the great open problems of "
               "industrial engineering - from line balancing, layout, and bottlenecks through predictive "
               "maintenance, digital twins, and ergonomics, to resilience quantification and unified "
               "human-machine design."),
 "greet_sig": ("I am the JAH Unsolved Industrial Engineering Archivist (Signature). Ask me about the Signature "
               "proposed solutions to the great open problems of industrial engineering - every approach labeled "
               "as a proposal, never established science."),
 "role_pub": ("unsolved industrial engineering archivist - the great open problems of industrial engineering, "
              "from line balancing, layout, and bottlenecks through predictive maintenance, digital twins, and "
              "ergonomics, to resilience quantification and unified human-machine design; teaches progressively "
              "along the ladder from foundations through compounded to advanced; answers from many angles - "
              "definition, example, analogy, application, history, math - using only archive data from this system"),
 "role_sig": ("unsolved industrial engineering archivist - Signature editions: his original Signature solution "
              "method applied to the 34 great open problems of industrial engineering, each carrying the full "
              "Signature-generated proposed solution, clearly labeled Signature-made and never presented as "
              "established science; teaches progressively along the ladder from foundations through compounded "
              "to advanced; answers from many angles - definition, example, analogy, application, history, math "
              "- using only archive data from this system"),
 "gen_desc": "Generate clearly-labeled unsolved industrial engineering studies. Seeded archive records are the authoritative entries.",
 "standards": [
  "Problem statements verified against the published literature; open status confirmed as of 2026.",
  "Quantitative claims cross-checked against standard references (Hopp and Spearman, Factory Physics; Montgomery, Introduction to Statistical Quality Control).",
  "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
 ],
 "sig_tail": ("Signature editions carry the Signature system's proposed solution approaches to famous "
              "unsolved problems. Every solution is labeled a Signature-generated proposal, never "
              "established science, never peer-accepted, never proof."),
}

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "ie-line-balancing",
 "name": "The Assembly Line Balancing Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "How should assembly tasks be assigned to workstations so the line runs at a target cycle time with minimum idle time - and why does the optimal balance stay elusive?",
 "background": "Salveson (1955) formulated the simple assembly line balancing problem (SALBP): assign tasks with precedence constraints to stations to minimize their number for a given cycle time. The problem is NP-hard, and exact methods (branch-and-bound, DP) stall on moderate instances while real lines have hundreds of tasks with stochastic times, mixed models, and worker heterogeneity. Heuristics (ranked positional weight, COMSOAL) dominate practice. The deeper gap is dynamic: real lines rebalance constantly as demand and staffing shift, but the theory is mostly static - the rebalancing problem with changeover costs is far less mapped.",
 "why_it_matters": "Assembly lines build the manufactured world. Every percent of idle time is paid labor producing nothing, and unbalanced lines starve downstream stations while choking upstream ones.",
 "sig_lens": "The Signature lens reads the line as a chain of promises: each station promises its cycle time, and the protocol must keep the promises synchronized.",
 "sig_solution": LABEL + " Assumptions: (1) exact optima are unreachable for real lines; (2) task times are stochastic and drift. Reasoning path: balance against distributions, not point estimates - assign tasks to equalize the probability of station overrun, and rebalance on measured drift. Proposed mechanism: a promise protocol that balances on stochastic task-time distributions, monitors station overrun rates in production, and triggers rebalancing when drift exceeds a threshold - pricing the changeover cost of each rebalance. Confirm: stochastic balancing cuts overrun idle time versus deterministic balancing. Kill: task-time distributions prove unestimable and the balance is fiction. Does NOT claim: optimal line balances - it keeps the promises synchronized under uncertainty.",
 "pointer": "The Signature system's proposed approach balances on task-time distributions and rebalances on measured drift; the companion Signature Edition record specifies the promise protocol.",
 "key_points": [
  "SALBP is NP-hard; exact methods stall on moderate instances.",
  "Real lines have stochastic times, mixed models, and heterogeneous workers.",
  "Heuristics dominate practice; the theory is mostly static.",
  "Rebalancing with changeover costs is far less mapped than static balancing.",
 ],
 "requirements": [
  "Stochastic task-time distributions, not point estimates.",
  "Production monitoring of station overrun rates.",
  "Rebalance triggers priced with changeover costs.",
 ],
 "citations": [
  "Salveson ME (1955) The assembly line balancing problem. Journal of Industrial Engineering 6(3).",
  "Scholl A, Becker C (2006) State-of-the-art exact and heuristic solution procedures for simple assembly line balancing. EJOR 168(3).",
 ],
 "demo": {"lam": 4.0, "mu": 6.0},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "ie-facility-layout",
 "name": "The Facility Layout Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "How should departments be arranged on a factory floor to minimize material-handling cost - and why does the quadratic assignment formulation defeat exact solution?",
 "background": "The facility layout problem is famously the quadratic assignment problem (QAP): assign facilities to locations minimizing flow-times-distance. QAP is NP-hard and brutally so - exact methods stall around n=30 while real plants have hundreds of departments. Koopmans and Beckmann (1957) gave the formulation; six decades later the QAPLIB benchmarks still have open instances. Heuristics (simulated annealing, tabu search, ant colony) find good layouts, but the gap to optimal is unmeasurable on real sizes. Dynamic layout - rearranging as product mix changes, with rearrangement costs - is even less solved.",
 "why_it_matters": "Material handling is 20 to 50 percent of manufacturing cost, and layout decides it for decades. A bad layout taxes every part that moves, forever.",
 "sig_lens": "The Signature lens reads layout as geography with rent: every adjacency is a bet on future flows, and the protocol must keep the bets revisable.",
 "sig_solution": LABEL + " Assumptions: (1) exact QAP solution is unreachable at real scale; (2) product mix drifts, dating any static layout. Reasoning path: design for revisability - optimize the layout jointly with a rearrangement policy, keeping high-flow adjacencies flexible. Proposed mechanism: a geography protocol that solves the static layout heuristically, then maintains a rearrangement option value for each department pair, triggering moves when flow drift pays for the rearrangement. Confirm: revisable layouts beat static optima on lifetime cost under mix drift. Kill: rearrangement costs dominate and the flexibility is never exercised. Does NOT claim: optimal layouts - it manages the layout as a living decision.",
 "pointer": "The Signature system's proposed approach designs layouts with priced rearrangement options; the companion Signature Edition record specifies the geography protocol.",
 "key_points": [
  "Facility layout is QAP: NP-hard, exact methods stall near n=30.",
  "QAPLIB benchmarks still have open instances after six decades.",
  "Material handling is 20 to 50 percent of manufacturing cost.",
  "Dynamic layout with rearrangement costs is far less solved.",
 ],
 "requirements": [
  "Heuristic static layouts with gap estimates where computable.",
  "Rearrangement option values maintained per department pair.",
  "Flow-drift triggers priced against rearrangement costs.",
 ],
 "citations": [
  "Koopmans TC, Beckmann M (1957) Assignment problems and the location of economic activities. Econometrica 25(1).",
 ],
 "demo": {"lam": 3.0, "mu": 5.0},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "ie-bottleneck",
 "name": "The Bottleneck Identification Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "In a complex production system, which resource truly constrains throughput - and why do the usual utilization metrics point at the wrong machine?",
 "background": "The bottleneck is the constraint that governs throughput (Goldratt, Theory of Constraints), but identifying it is surprisingly hard: the highest-utilization machine is often not the bottleneck, because starvation and blocking propagate constraints. Methods range from the active-period method (Roser et al.) to shifting-bottleneck detection via buffer analysis, yet bottlenecks shift with product mix, and momentary bottlenecks mislead improvement efforts. The fundamental difficulty is causal: throughput is a system property, and local metrics cannot identify the binding constraint without system-level analysis. Factories routinely improve non-bottlenecks - the most expensive kind of improvement.",
 "why_it_matters": "Improving a non-bottleneck improves nothing but the improvement report. Bottleneck misidentification is the most expensive mistake in operations improvement.",
 "sig_lens": "The Signature lens reads the bottleneck as the system's narrowest promise: throughput is only as fast as the slowest kept promise, and the protocol must find it, not guess it.",
 "sig_solution": LABEL + " Assumptions: (1) utilization misleads; starvation and blocking propagate the true constraint; (2) bottlenecks shift with mix. Reasoning path: identify bottlenecks by their system effect - sensitivity of throughput to each resource's capacity - measured, not inferred from local metrics. Proposed mechanism: a promise-finder protocol that continuously estimates throughput sensitivity per resource (via perturbation analysis on live data), ranks true bottlenecks by measured sensitivity, and re-ranks as mix shifts. Confirm: sensitivity-ranked improvements lift throughput more per dollar than utilization-ranked ones. Kill: sensitivity estimates are too noisy to rank reliably. Does NOT claim: a static bottleneck answer - it tracks the moving constraint.",
 "pointer": "The Signature system's proposed approach ranks bottlenecks by measured throughput sensitivity; the companion Signature Edition record specifies the promise-finder protocol.",
 "key_points": [
  "The highest-utilization machine is often not the true bottleneck.",
  "Starvation and blocking propagate constraints across the system.",
  "Bottlenecks shift with product mix; momentary ones mislead.",
  "Improving non-bottlenecks improves nothing but reports.",
 ],
 "requirements": [
  "Throughput-sensitivity estimation per resource from live data.",
  "Continuous re-ranking as product mix shifts.",
  "Improvement prioritization by measured sensitivity, not utilization.",
 ],
 "citations": [
  "Goldratt EM, Cox J (1984) The Goal. North River Press.",
  "Roser C et al. (2001) A practical bottleneck detection method. Winter Simulation Conference.",
 ],
 "demo": {"lam": 5.0, "mu": 8.0},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "ie-knowledge-work",
 "name": "The Work Measurement in Knowledge Work Problem",
 "group": "Human Factors",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Time-and-motion study tamed factory work a century ago - but how can knowledge work (design, analysis, coding) be measured without destroying what makes it valuable?",
 "background": "Taylor's scientific management measured manual work to the second; knowledge work resists every such method. Outputs are intangible and delayed, quality dominates quantity, and measurement itself distorts the work (Goodhart's law hits hardest where output is ambiguous). The field has proxies - story points, lines of code, tickets closed - each famously gameable and weakly tied to value. Work sampling and activity analysis describe time allocation but not effectiveness. The fundamental problem is ontological: nobody agrees what the unit of knowledge work is, so measurement optimizes proxies while the real work goes unmeasured - and often unrewarded.",
 "why_it_matters": "Most advanced-economy work is knowledge work. Unmeasurable work cannot be improved, staffed, or fairly compensated - so it is managed by proxy, and the proxies corrupt it.",
 "sig_lens": "The Signature lens reads knowledge work as gardening: you can measure the hours with the shears, but the protocol must judge the garden, not the clipping count.",
 "sig_solution": LABEL + " Assumptions: (1) the unit of knowledge work is undefined; proxies corrupt; (2) measurement changes the work. Reasoning path: measure outcomes and decision quality, not activity - sample the work's products for value, and keep activity metrics strictly diagnostic. Proposed mechanism: a garden protocol that evaluates knowledge work through sampled outcome reviews (peer-judged value of deliverables), uses activity data only to diagnose blockers, and forbids proxy-based incentives. Confirm: outcome-sampled teams show less gaming and better output quality. Kill: outcome sampling proves too subjective to be fair. Does NOT claim: a unit of knowledge work - it judges the garden while refusing to count clippings as flowers.",
 "pointer": "The Signature system's proposed approach measures knowledge work by sampled outcomes, never by activity proxies; the companion Signature Edition record specifies the garden protocol.",
 "key_points": [
  "Taylorist methods fail on intangible, delayed, quality-dominated outputs.",
  "Proxies (story points, tickets) are gameable and weakly tied to value.",
  "Goodhart's law strikes hardest where output is ambiguous.",
  "No agreed unit of knowledge work exists.",
 ],
 "requirements": [
  "Sampled outcome reviews judging deliverable value.",
  "Activity metrics restricted to diagnostic (never incentive) use.",
  "Prohibition of proxy-based performance incentives.",
 ],
 "citations": [
  "Drucker PF (1999) Knowledge-worker productivity: the biggest challenge. California Management Review 41(2).",
 ],
 "demo": {"lam": 2.5, "mu": 4.0},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "ie-learning-curve",
 "name": "The Learning Curve Universality Problem",
 "group": "Human Factors",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Wright's 1936 learning curve says costs fall a fixed percent with each doubling of output - but how universal is the law, and what breaks it?",
 "background": "T.P. Wright (1936) found aircraft assembly costs fell about 20 percent per doubling of cumulative production - the learning (experience) curve, later formalized by the Boston Consulting Group as a strategic law. But the curve's universality is contested: rates vary wildly across industries, forgetting and turnover flatten curves, automation changes the mechanism, and the famous BCG applications sometimes confused learning with scale economies. The plateau problem - when learning stops - has no general theory, and the forgetting curve (how fast skills decay) is far less studied than the learning one. Planners still extrapolate Wright's law into futures it was never validated for.",
 "why_it_matters": "Learning curves price new products, plan ramp-ups, and justify automation investments. A misapplied curve misprices the future by orders of magnitude.",
 "sig_lens": "The Signature lens reads learning as a depreciating asset: the curve must account for forgetting, turnover, and the plateau, not just the glorious descent.",
 "sig_solution": LABEL + " Assumptions: (1) Wright's law is a tendency, not a law; (2) forgetting and turnover are first-order effects. Reasoning path: fit learning curves with forgetting terms and plateau detection, calibrated to the specific operation's history - never borrow another industry's rate. Proposed mechanism: a depreciation-aware protocol that estimates learning rates from own-history data, models forgetting during breaks, detects plateaus statistically, and reports forecasts with bands that widen past the observed range. Confirm: depreciation-aware forecasts beat naive Wright extrapolation on ramp-up data. Kill: own-history data is too sparse to fit the richer model. Does NOT claim: a universal learning law - it prices learning per operation with honest bands.",
 "pointer": "The Signature system's proposed approach fits learning curves with forgetting and plateau detection per operation; the companion Signature Edition record specifies the depreciation-aware protocol.",
 "key_points": [
  "Wright (1936): costs fall per doubling of cumulative output; rates vary widely.",
  "Forgetting, turnover, and automation confound the classic curve.",
  "The plateau - when learning stops - has no general theory.",
  "Borrowed learning rates misprice new-product economics.",
 ],
 "requirements": [
  "Learning rates estimated from own-history data only.",
  "Forgetting terms for production breaks and turnover.",
  "Statistical plateau detection with widening forecast bands.",
 ],
 "citations": [
  "Wright TP (1936) Factors affecting the cost of airplanes. Journal of the Aeronautical Sciences 3(4).",
 ],
 "demo": {"lam": 6.0, "mu": 9.0},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "ie-oee",
 "name": "The Overall Equipment Effectiveness Decomposition Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "OEE multiplies availability, performance, and quality into one number - but what does the number actually diagnose, and why do world-class targets mislead?",
 "background": "Overall Equipment Effectiveness (Nakajima, TPM, 1988) - availability times performance times quality - is the lingua franca of manufacturing improvement, with 85 percent sold as world-class. But the single number hides everything: a 60 percent OEE can mean chronic micro-stops or one catastrophic breakdown, and the remedies differ completely. The six big losses framework helps, but loss categorization is subjective and gaming is rampant (redefining planned stops to inflate availability). Worse, maximizing OEE locally can hurt the system - running a non-bottleneck at 100 percent builds inventory, not throughput. The decomposition problem - from one number to the right action - remains unsolved in general.",
 "why_it_matters": "OEE drives improvement budgets worldwide. A metric that hides its own diagnosis misdirects those budgets systematically.",
 "sig_lens": "The Signature lens reads OEE as a fever thermometer: useful for knowing something is wrong, useless for the prescription - the protocol must take the full history, not just the temperature.",
 "sig_solution": LABEL + " Assumptions: (1) the single number hides the diagnosis; (2) local OEE maximization can harm system throughput. Reasoning path: decompose before acting - attribute losses to the six big losses with measured (not estimated) data, and gate improvement spend on bottleneck status. Proposed mechanism: a thermometer protocol that reports OEE only with its full loss decomposition, ranks losses by measured cost, and requires bottleneck verification before funding availability improvements on any machine. Confirm: decomposition-gated improvement spends less per throughput point gained. Kill: loss categorization proves too subjective to rank reliably. Does NOT claim: a universal OEE target - it replaces the number with the diagnosis.",
 "pointer": "The Signature system's proposed approach reports OEE only with measured loss decomposition and bottleneck gating; the companion Signature Edition record specifies the thermometer protocol.",
 "key_points": [
  "OEE hides distinct failure modes behind one multiplicative number.",
  "The 85 percent world-class target is folklore, not science.",
  "Loss categorization is subjective; gaming inflates reported OEE.",
  "Maximizing local OEE can damage system throughput.",
 ],
 "requirements": [
  "Measured (not estimated) six-big-losses decomposition with every OEE report.",
  "Loss ranking by measured cost impact.",
  "Bottleneck verification before funding availability improvements.",
 ],
 "citations": [
  "Nakajima S (1988) Introduction to TPM. Productivity Press.",
 ],
 "demo": {"lam": 7.0, "mu": 10.0},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "ie-smed",
 "name": "The Single Minute Die Exchange Limit Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Shigeo Shingo's SMED cut changeovers from hours to minutes - but what is the theoretical limit of changeover reduction, and what stands in its way?",
 "background": "Shingo's Single-Minute Exchange of Die (SMED), developed at Toyota, separates internal setup (machine stopped) from external setup (done while running) and converts the former to the latter - achieving single-digit-minute changeovers that enabled just-in-time production. But the method is a craft, not a science: the limit of changeover time for a given machine is unknown, the internal-external classification is judgmental, and the economic question - when is further reduction worth it - has no general answer. The EOQ logic says setup reduction enables smaller lots, but the marginal value of the next minute saved is rarely computed. Most plants stop improving changeovers long before any theoretical limit, for reasons nobody has formalized.",
 "why_it_matters": "Changeover time sets the economic lot size: long changeovers force large batches, large batches force inventory, inventory hides problems. The unmapped limit is unmapped money.",
 "sig_lens": "The Signature lens reads changeover as a tax on variety: every minute of setup taxes the product mix, and the protocol must show the tax bill.",
 "sig_solution": LABEL + " Assumptions: (1) SMED is craft; the theoretical limit per machine is unknown; (2) the marginal value of setup reduction is rarely computed. Reasoning path: compute the marginal economics - the lot-size and inventory value of each minute saved - and improve changeovers in marginal-value order until the value falls below the improvement cost. Proposed mechanism: a tax-bill protocol that values each changeover minute via its EOQ and flexibility effects, ranks setup-reduction projects by marginal return, and stops investment where marginal value crosses marginal cost. Confirm: marginal-ranked SMED programs beat blanket changeover drives on ROI. Kill: the marginal values prove too uncertain to rank on. Does NOT claim: the theoretical changeover limit - it invests where the return is measured.",
 "pointer": "The Signature system's proposed approach ranks changeover reduction by marginal economic value; the companion Signature Edition record specifies the tax-bill protocol.",
 "key_points": [
  "SMED separates internal from external setup and converts the former.",
  "Single-digit-minute changeovers enabled just-in-time production.",
  "The theoretical limit per machine is unknown; the method is craft.",
  "The marginal value of the next minute saved is rarely computed.",
 ],
 "requirements": [
  "Marginal economic valuation of each changeover minute.",
  "Project ranking by marginal return on setup reduction.",
  "Investment stopping rules at marginal-value crossover.",
 ],
 "citations": [
  "Shingo S (1985) A Revolution in Manufacturing: The SMED System. Productivity Press.",
 ],
 "demo": {"lam": 3.5, "mu": 7.0},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "ie-spc-autocorrelated",
 "name": "The Statistical Process Control for Autocorrelated Data Problem",
 "group": "Quality Engineering",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Classical control charts assume independent observations - but real process data is autocorrelated, so how can out-of-control signals be distinguished from natural persistence?",
 "background": "Shewhart control charts - the foundation of statistical quality control - assume independent, identically distributed observations. Real processes (chemical, continuous manufacturing) produce autocorrelated data where today's value predicts tomorrow's, and applying Shewhart charts directly gives false alarm rates far above nominal. The standard fixes - residual charts (fit ARIMA, chart residuals), EWMA/ST charts with adjusted limits - each have failure modes: model misspecification in the ARIMA step, or limits that assume the autocorrelation structure is stable. When the autocorrelation itself shifts, the chart cannot tell a process change from a dynamics change - the deepest version of the problem, still open.",
 "why_it_matters": "False alarms shut down processes; missed signals ship defects. Autocorrelated processes with misapplied charts get both failures at once.",
 "sig_lens": "The Signature lens reads autocorrelation as memory: the chart must remember what the process remembers, and the protocol must separate a change of mind from a change of memory.",
 "sig_solution": LABEL + " Assumptions: (1) Shewhart independence assumptions fail on real processes; (2) autocorrelation structure itself can shift. Reasoning path: monitor the process and its memory separately - chart residuals for level shifts and monitor the autocorrelation structure for dynamics shifts. Proposed mechanism: a two-memory protocol that fits the time-series model adaptively, charts residuals with honest limits, and runs a parallel monitor on the autocorrelation parameters to distinguish process changes from dynamics changes. Confirm: two-memory charting cuts false alarms versus naive Shewhart on autocorrelated processes. Kill: adaptive fitting chases noise and destabilizes the limits. Does NOT claim: a universal autocorrelated chart - it separates the two kinds of change.",
 "pointer": "The Signature system's proposed approach monitors process level and memory structure separately; the companion Signature Edition record specifies the two-memory protocol.",
 "key_points": [
  "Shewhart charts assume independence; real process data is autocorrelated.",
  "Naive application gives false alarm rates far above nominal.",
  "Residual charts depend on correct ARIMA specification.",
  "Shifts in autocorrelation structure are indistinguishable from process shifts.",
 ],
 "requirements": [
  "Adaptive time-series modeling with residual charting.",
  "Parallel monitoring of autocorrelation structure.",
  "Honest control limits accounting for estimation uncertainty.",
 ],
 "citations": [
  "Montgomery DC (2019) Introduction to Statistical Quality Control, 8th ed. Wiley.",
 ],
 "demo": {"lam": 8.0, "mu": 12.0},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "ie-small-batch-qc",
 "name": "The Small Batch Quality Control Problem",
 "group": "Quality Engineering",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "Statistical quality control needs samples - but high-mix, low-volume production has no samples to spare, so how can quality be assured batch by batch?",
 "background": "Classical SQC - control charts, acceptance sampling (MIL-STD-105) - assumes long production runs generating the samples statistics needs. High-mix low-volume production (aerospace, custom machinery, job shops) runs batches of ten, where n=30 control limits are fantasy and OC curves cannot be drawn. The field's answers - short-run charts (standardized deviations), pre-control, Bayesian updating across similar jobs - are partial: short-run charts assume the standardized process is stable across jobs, which is exactly what needs proving. The fundamental tension is statistical: small batches cannot support the inference that quality assurance wants to make.",
 "why_it_matters": "Aerospace and medical devices are small-batch by nature and cannot tolerate defects. The statistical tools of mass production do not transfer - and the gap is where escapes happen.",
 "sig_lens": "The Signature lens reads small batches as short testimonies: each batch testifies briefly, and the protocol must combine testimonies without pretending any one of them is conclusive.",
 "sig_solution": LABEL + " Assumptions: (1) classical SQC sample sizes are unavailable; (2) cross-job standardization assumes what needs proving. Reasoning path: borrow strength hierarchically - model jobs as draws from a family, update the family with each batch, and certify each batch against the family posterior. Proposed mechanism: a testimony protocol using hierarchical Bayesian models across job families, with each small batch updating the family parameters and receiving a batch-specific quality certificate with honest uncertainty. Confirm: hierarchical certification catches shifts that per-batch charts miss. Kill: job families prove too heterogeneous and the borrowing misleads. Does NOT claim: classical SQC guarantees at small n - it borrows strength with the borrowing made explicit.",
 "pointer": "The Signature system's proposed approach certifies small batches via hierarchical family models; the companion Signature Edition record specifies the testimony protocol.",
 "key_points": [
  "Classical SQC needs sample sizes small-batch production cannot provide.",
  "Short-run charts assume cross-job stability that needs proving.",
  "Acceptance sampling OC curves cannot be drawn for batches of ten.",
  "The tension is fundamental: small n cannot support the desired inference.",
 ],
 "requirements": [
  "Hierarchical models borrowing strength across job families.",
  "Per-batch certificates with honest uncertainty bands.",
  "Heterogeneity monitoring to detect when borrowing breaks down.",
 ],
 "citations": [
  "Montgomery DC (2019) Introduction to Statistical Quality Control, 8th ed. Wiley.",
 ],
 "demo": {"lam": 2.0, "mu": 3.5},
},
# ----------------------------------------------------------------- rank 10
{
 "key": "ie-tolerance",
 "name": "The Tolerance Allocation Problem",
 "group": "Quality Engineering",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "How tight should each component tolerance be so the assembly works - and how can the cost of tightness be traded against the cost of failure?",
 "background": "Tolerance allocation distributes the assembly's allowable variation among components: worst-case (arithmetic) stacking is safe but brutally expensive; statistical (RSS) stacking is cheaper but assumes normality and independence that rarely hold. The cost-tolerance functions are usually guessed, process capabilities shift, and the allocation interacts with the design itself (robust design, Taguchi methods). The optimization - minimize cost subject to assembly yield - is nonconvex with unreliable inputs. Real practice allocates by rule of thumb and absorbs the warranty costs; the gap between the thumb and the optimum is unmeasured.",
 "why_it_matters": "Tolerances are money: every tightened tolerance raises manufacturing cost, every loosened one raises failure risk. The unoptimized middle is where margins leak.",
 "sig_lens": "The Signature lens reads tolerances as a budget of variation: the assembly has so much slop to spend, and the protocol must spend it where it buys the most yield per dollar.",
 "sig_solution": LABEL + " Assumptions: (1) cost-tolerance functions are usually guessed; (2) worst-case stacking overbuys safety. Reasoning path: measure the real cost-tolerance curves and capability distributions, then allocate the variation budget by marginal yield-per-dollar. Proposed mechanism: a variation-budget protocol that estimates cost-tolerance functions from process data, allocates tolerances by marginal analysis, validates the assembly yield by Monte Carlo on measured distributions, and re-allocates as capabilities drift. Confirm: budget-allocated tolerances beat rule-of-thumb on cost-plus-warranty. Kill: the cost functions prove unmeasurable and the allocation is guesswork. Does NOT claim: optimal tolerances under true costs - it spends the measured budget where it pays.",
 "pointer": "The Signature system's proposed approach allocates the variation budget by marginal yield-per-dollar; the companion Signature Edition record specifies the variation-budget protocol.",
 "key_points": [
  "Worst-case stacking is safe but brutally expensive.",
  "Statistical stacking assumes normality and independence that rarely hold.",
  "Cost-tolerance functions are usually guessed, not measured.",
  "Practice allocates by rule of thumb; the optimality gap is unmeasured.",
 ],
 "requirements": [
  "Measured cost-tolerance functions from process data.",
  "Marginal yield-per-dollar allocation of the variation budget.",
  "Monte Carlo assembly-yield validation on measured distributions.",
 ],
 "citations": [
  "Chase KW, Parkinson AR (1991) A survey of research in the application of tolerance analysis. J. Manufacturing Systems 10(1).",
 ],
 "demo": {"lam": 4.5, "mu": 6.5},
},
# ----------------------------------------------------------------- rank 11
{
 "key": "ie-shift-work",
 "name": "The Shift Work Circadian Optimization Problem",
 "group": "Human Factors",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Night shifts damage health and degrade performance - so what shift schedule minimizes the harm while keeping the plant running around the clock?",
 "background": "Shift work is a circadian assault: night workers show elevated risks of cardiovascular disease, metabolic disorders, and accidents (Folkard and Tucker, 2003). The ergonomics literature offers principles - forward rotation, limited consecutive nights, adequate recovery - but the optimization problem (assign workers to shifts minimizing health cost subject to coverage and preferences) lacks a validated health-cost function. Individual chronotypes differ enormously, fatigue models (SAFTE, FAID) predict alertness but not long-term health, and the economic question - what the health damage costs versus the production value - is barely asked. Schedules are negotiated politically, not optimized scientifically.",
 "why_it_matters": "A fifth of the workforce does shift work, paying with their health for round-the-clock production. Unoptimized schedules are a public health problem wearing an operations costume.",
 "sig_lens": "The Signature lens reads shifts as a health ledger: every night hour is borrowed from the worker's body, and the protocol must show the repayment terms.",
 "sig_solution": LABEL + " Assumptions: (1) no validated health-cost function exists for schedules; (2) chronotypes differ enormously. Reasoning path: build the best available harm model from the literature, personalize by chronotype, and optimize schedules against it with coverage constraints. Proposed mechanism: a health-ledger protocol that scores candidate schedules on circadian disruption (using published risk models), personalizes by chronotype where data exists, and requires the harm score on every posted schedule alongside the labor cost. Confirm: ledger-scored schedules reduce fatigue incidents versus negotiated ones. Kill: the harm models prove too crude to guide scheduling. Does NOT claim: a validated health-cost function - it uses the best available science transparently.",
 "pointer": "The Signature system's proposed approach scores schedules on circadian harm and personalizes by chronotype; the companion Signature Edition record specifies the health-ledger protocol.",
 "key_points": [
  "Night shift work elevates cardiovascular, metabolic, and accident risks.",
  "Forward rotation and limited consecutive nights are established principles.",
  "No validated health-cost function exists for schedule optimization.",
  "Fatigue models predict alertness, not long-term health.",
 ],
 "requirements": [
  "Circadian-harm scoring of every candidate schedule.",
  "Chronotype personalization where data exists.",
  "Harm scores published alongside labor costs on posted schedules.",
 ],
 "citations": [
  "Folkard S, Tucker P (2003) Shift work, safety and productivity. Occupational Medicine 53(2).",
 ],
 "demo": {"lam": 5.5, "mu": 7.5},
},
# ----------------------------------------------------------------- rank 12
{
 "key": "ie-cellular",
 "name": "The Cellular Manufacturing Design Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "How should machines be grouped into cells and parts into families so each family flows through its cell - and what is the true cost of the exceptional parts that do not fit?",
 "background": "Group technology (Mitrofanov; Burbidge) promises the efficiency of flow lines with the flexibility of job shops: form machine cells serving part families. The cell formation problem - cluster the machine-part incidence matrix - is NP-hard, and the exceptional elements (parts needing machines outside their cell) create intercell flows that erode the benefit. The design interacts with layout (intracell and intercell), scheduling, and labor (cell workers need multiple skills). The literature optimizes formation in isolation; the integrated design - formation plus layout plus staffing - is far less solved, and the dynamic version (families evolve) barely exists.",
 "why_it_matters": "Cellular manufacturing is the middle path between job shop chaos and line rigidity. Bad cell design pays for both systems' weaknesses and gets neither's strengths.",
 "sig_lens": "The Signature lens reads cells as neighborhoods: the protocol must draw boundaries where the traffic is naturally local, and price the bridges for the rest.",
 "sig_solution": LABEL + " Assumptions: (1) exceptional elements are the true cost driver; (2) formation, layout, and staffing interact. Reasoning path: design cells to minimize priced intercell flow, then staff for the skill breadth the cells demand. Proposed mechanism: a neighborhood protocol that forms cells minimizing intercell-flow cost (not just exceptional counts), lays out cells for the residual flows, and cross-trains workers to the cell skill profiles - re-forming when family mix drifts. Confirm: flow-priced cell designs beat count-based ones on material-handling cost. Kill: family mix drifts faster than re-forming pays for. Does NOT claim: optimal cell designs - it prices the exceptions and designs around them.",
 "pointer": "The Signature system's proposed approach forms cells on priced intercell flow and re-forms on mix drift; the companion Signature Edition record specifies the neighborhood protocol.",
 "key_points": [
  "Cell formation is NP-hard; exceptional elements create eroding intercell flows.",
  "Formation, layout, and staffing interact but are optimized in isolation.",
  "Cell workers need multi-machine skills - a labor constraint, not just a layout one.",
  "Dynamic re-forming as families evolve barely exists in the literature.",
 ],
 "requirements": [
  "Cell formation minimizing priced intercell flow.",
  "Integrated layout and cross-training plans per design.",
  "Re-formation triggers on measured family-mix drift.",
 ],
 "citations": [
  "Burbidge JL (1975) The Introduction of Group Technology. Heinemann.",
 ],
 "demo": {"lam": 6.5, "mu": 8.5},
},
# ----------------------------------------------------------------- rank 13
{
 "key": "ie-flexible-scheduling",
 "name": "The Flexible Manufacturing Scheduling Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Flexible manufacturing systems can route any part to any capable machine - but how should that routing freedom be scheduled in real time without drowning in choices?",
 "background": "Flexible manufacturing systems (FMS) - CNC machines, automated handling, computer control - offer routing flexibility that is both the promise and the problem: the scheduling space explodes with every alternative route. The flexibility must be managed (which alternative to use when), and the control architectures (hierarchical, heterarchical, agent-based) each have failure modes. Real-time scheduling under machine breakdowns, tool wear, and rush orders needs policies, not plans - but the policy design problem (which dispatching logic for which flexibility type) is poorly mapped. The literature optimizes static schedules for systems whose value is dynamic response.",
 "why_it_matters": "FMS installations cost tens of millions; their flexibility is the return on that investment. Unscheduled flexibility is expensive chaos with computer control.",
 "sig_lens": "The Signature lens reads flexibility as options: the protocol must value each routing option like a financial option and exercise them by rule, not by hope.",
 "sig_solution": LABEL + " Assumptions: (1) routing flexibility explodes the scheduling space; (2) static schedules waste dynamic capability. Reasoning path: schedule by policy - precompute decision rules for routing choices keyed on system state, and value the flexibility options explicitly. Proposed mechanism: an options protocol that characterizes each flexibility type's value via simulation, installs state-dependent routing policies (not fixed schedules), and re-values the options as the mix changes. Confirm: policy-scheduled FMS beats static-schedule FMS on throughput under disruptions. Kill: the state space defeats policy design and rules misfire. Does NOT claim: optimal FMS control - it manages flexibility as priced options.",
 "pointer": "The Signature system's proposed approach schedules FMS by state-dependent routing policies with priced flexibility; the companion Signature Edition record specifies the options protocol.",
 "key_points": [
  "Routing flexibility explodes the scheduling space combinatorially.",
  "Control architectures (hierarchical, agent-based) each have failure modes.",
  "Real-time response needs policies, but policy design is poorly mapped.",
  "Literature optimizes static schedules for dynamic systems.",
 ],
 "requirements": [
  "Simulation-valued flexibility options per routing alternative.",
  "State-dependent routing policies installed, not fixed schedules.",
  "Re-valuation of options as product mix changes.",
 ],
 "citations": [
  "Stecke KE (1983) Formulation and solution of nonlinear integer production planning problems for flexible manufacturing systems. Management Science 29(3).",
 ],
 "demo": {"lam": 9.0, "mu": 11.0},
},
# ----------------------------------------------------------------- rank 14
{
 "key": "ie-predictive-maintenance",
 "name": "The Predictive Maintenance Remaining Life Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Given sensor streams from degrading equipment, how much useful life remains - and how can the prediction be trusted enough to schedule maintenance on?",
 "background": "Prognostics and health management (PHM) predicts remaining useful life (RUL) from sensor data, and the PHM Society's data challenges made it a sport. But the jump from challenge winner to trusted maintenance trigger is unmade: RUL models need run-to-failure data that industry will not generate (nobody runs machines to destruction for data), the predictions lack calibrated uncertainty, and the maintenance decision needs cost-optimal thresholds, not just RUL numbers. Transfer across machines (fleet prognostics) mostly fails - each machine's degradation is its own story. The field predicts well on curated datasets and hesitates on real shop floors.",
 "why_it_matters": "Unplanned downtime costs industry hundreds of billions; unnecessary preventive maintenance wastes nearly as much. Trusted RUL predictions would thread the needle - but trust is exactly what is missing.",
 "sig_lens": "The Signature lens reads RUL as a forecast that must carry its weather warning: the protocol ships the prediction with its uncertainty, and acts only where the warning allows.",
 "sig_solution": LABEL + " Assumptions: (1) run-to-failure data is unavailable; models train on censored histories; (2) RUL without calibrated uncertainty cannot trigger maintenance. Reasoning path: predict distributions, not points - and set maintenance thresholds on the cost-optimal quantile of the RUL distribution. Proposed mechanism: a weather-warning protocol that outputs full RUL distributions with calibration checks, converts them to maintenance triggers via cost models (failure cost versus preventive cost), and refuses to trigger where uncertainty exceeds the decision's value. Confirm: distribution-triggered maintenance beats point-triggered on cost. Kill: the RUL distributions miscalibrate and triggers misfire. Does NOT claim: true remaining life - it acts on honest uncertainty.",
 "pointer": "The Signature system's proposed approach predicts RUL distributions and triggers maintenance on cost-optimal quantiles; the companion Signature Edition record specifies the weather-warning protocol.",
 "key_points": [
  "RUL models need run-to-failure data that industry will not generate.",
  "Predictions lack calibrated uncertainty for maintenance decisions.",
  "Fleet transfer of prognostics mostly fails across machines.",
  "Challenge-winning accuracy does not transfer to shop-floor trust.",
 ],
 "requirements": [
  "Full RUL distributions with calibration checks, not point predictions.",
  "Cost-model-derived maintenance trigger thresholds.",
  "No-trigger rules where uncertainty exceeds decision value.",
 ],
 "citations": [
  "Lee J et al. (2014) Prognostics and health management design for rotary machinery systems. Springer.",
 ],
 "demo": {"lam": 4.0, "mu": 9.0},
},
# ----------------------------------------------------------------- rank 15
{
 "key": "ie-digital-twin",
 "name": "The Digital Twin Fidelity Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "A digital twin promises a live virtual replica of the physical system - but how faithful must it be for each decision, and how is fidelity measured?",
 "background": "Digital twins (Grieves, 2002; NASA, 2010) couple physical systems to live simulation models, promising what-if analysis and predictive control. But fidelity is the unanswered question: a twin detailed enough for control design is overkill for throughput planning, and the mapping from decision to required fidelity has no theory. Validation is ad hoc - twins are declared valid by demonstration, not by measurement - and the synchronization problem (keeping the twin's state aligned with a drifting physical system) is barely formalized. The result is expensive twins whose decision value is asserted, not shown, and cheap twins trusted beyond their fidelity.",
 "why_it_matters": "Digital twins consume serious modeling investment. Without fidelity discipline, the money buys either overkill detail or dangerous overconfidence - sometimes both in the same twin.",
 "sig_lens": "The Signature lens reads the twin as a map: the protocol must state the map's scale and refresh rate, and forbid navigation beyond them.",
 "sig_solution": LABEL + " Assumptions: (1) required fidelity depends on the decision, and the mapping is unmapped; (2) twins drift from their physical counterparts. Reasoning path: certify twins per decision - measure the twin's prediction error on the decisions it will support, and gate each decision type on its measured fidelity. Proposed mechanism: a map-scale protocol that validates twins against decision-specific error metrics, monitors synchronization drift continuously, and licenses decisions only within the validated fidelity envelope - with the envelope printed on every twin dashboard. Confirm: envelope-gated twins support better decisions than unvalidated ones. Kill: validation metrics miss the decisions that matter and the envelope misleads. Does NOT claim: a fidelity theory - it measures and gates per decision.",
 "pointer": "The Signature system's proposed approach certifies digital twins per decision with monitored fidelity envelopes; the companion Signature Edition record specifies the map-scale protocol.",
 "key_points": [
  "No theory maps decisions to required twin fidelity.",
  "Twin validation is by demonstration, not measurement.",
  "Synchronization drift between twin and physical system is barely formalized.",
  "Twins are over-trusted beyond their fidelity and over-built beyond need.",
 ],
 "requirements": [
  "Decision-specific fidelity validation metrics.",
  "Continuous synchronization-drift monitoring.",
  "Fidelity envelopes licensing each decision type, printed on dashboards.",
 ],
 "citations": [
  "Grieves M (2014) Digital twin: manufacturing excellence through virtual factory replication. White paper.",
 ],
 "demo": {"lam": 7.5, "mu": 10.5},
},
# ----------------------------------------------------------------- rank 16
{
 "key": "ie-lean-resilience",
 "name": "The Lean Against Resilience Tradeoff Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "Lean eliminates waste - including the buffers that absorb shocks - so how much leanness can a system afford before it becomes fragile?",
 "background": "Lean (Womack and Jones, building on Toyota) made waste elimination the creed: inventory is waste, and just-in-time exposes problems by removing buffers. Then the shocks came - 2011 tsunami, pandemic, chip shortage - and bufferless supply chains snapped spectacularly. The resilience literature (Sheffi; Simchi-Levi) argues for strategic redundancy, but the tradeoff has no general theory: how much buffer buys how much resilience at what cost is unquantified, the lean accounting (inventory carrying cost) is precise while the resilience value is hand-waving, and the two camps talk past each other. Every firm now wants to be lean and resilient - a contradiction nobody has priced.",
 "why_it_matters": "The leanness-resilience frontier is the central strategic question in operations: the last decade's disruptions were billed to bufferless systems, and the next decade's margins will be set by whoever prices the tradeoff.",
 "sig_lens": "The Signature lens reads buffers as insurance: leanness is the premium saved, resilience the coverage bought - the protocol must show both sides of the policy.",
 "sig_solution": LABEL + " Assumptions: (1) the tradeoff is real and unpriced; (2) disruption probabilities are deeply uncertain. Reasoning path: price both sides - compute the carrying cost of buffers and the expected disruption cost without them under explicit scenarios, then choose the frontier point deliberately. Proposed mechanism: an insurance-ledger protocol that maintains disruption scenarios with stated (uncertain) probabilities, computes the efficient frontier of buffer cost versus expected disruption loss, and requires the chosen point to be signed off with its scenario assumptions visible. Confirm: frontier-chosen buffer levels outperform rules of thumb across disruption histories. Kill: scenario probabilities prove meaningless and the frontier is fiction. Does NOT claim: optimal leanness - it makes the tradeoff explicit and revisable.",
 "pointer": "The Signature system's proposed approach prices the lean-resilience frontier on explicit disruption scenarios; the companion Signature Edition record specifies the insurance-ledger protocol.",
 "key_points": [
  "Lean's buffer elimination created spectacular fragility in recent disruptions.",
  "The buffer-versus-resilience tradeoff has no general quantitative theory.",
  "Lean accounting is precise; resilience value is hand-waving.",
  "Firms want both leanness and resilience - the contradiction is unpriced.",
 ],
 "requirements": [
  "Explicit disruption scenarios with stated probability assumptions.",
  "Efficient frontiers of buffer cost versus expected disruption loss.",
  "Signed-off frontier choices with visible scenario assumptions.",
 ],
 "citations": [
  "Sheffi Y (2005) The Resilient Enterprise. MIT Press.",
 ],
 "demo": {"lam": 5.0, "mu": 6.0},
},
# ----------------------------------------------------------------- rank 17
{
 "key": "ie-slotting",
 "name": "The Warehouse Slotting Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Which SKUs should live in which warehouse locations so pickers travel least - and how often should the slotting be redone as demand shifts?",
 "background": "Slotting assigns SKUs to storage locations: fast movers near the dock, correlated items together, heavy items at ergonomic heights. The static problem is a generalized assignment with correlation structure; the dynamic problem - re-slotting as demand shifts - adds the cost of moving inventory to the travel savings, and the re-slotting frequency question is genuinely open. Class-based storage (ABC zones) is the industry standard, but the class boundaries are rules of thumb, and the interaction with order batching, routing, and automation (goods-to-person) complicates every answer. E-commerce's SKU proliferation and demand volatility make static slotting decay fast.",
 "why_it_matters": "Picker travel is the dominant warehouse labor cost, and labor is the dominant warehouse cost. Slotting decides how far every picker walks, every day, for years.",
 "sig_lens": "The Signature lens reads slotting as urban planning: put the busy shops downtown, and rezone when the city's traffic patterns change.",
 "sig_solution": LABEL + " Assumptions: (1) static slotting decays as demand shifts; (2) re-slotting costs are real and usually ignored. Reasoning path: slot dynamically on measured velocity and correlation, and re-slot only when the travel savings pay for the moves. Proposed mechanism: an urban-planning protocol that scores locations by pick density, assigns SKUs by velocity-correlation-ergonomics, and triggers re-slotting when the projected travel savings exceed move costs by a margin - with the trigger computed, not scheduled. Confirm: trigger-based re-slotting beats calendar re-slotting on labor cost. Kill: demand shifts faster than re-slotting can pay for itself. Does NOT claim: optimal slotting - it keeps the city rezoned as traffic moves.",
 "pointer": "The Signature system's proposed approach re-slots warehouses on computed savings-versus-move-cost triggers; the companion Signature Edition record specifies the urban-planning protocol.",
 "key_points": [
  "Picker travel dominates warehouse labor cost.",
  "Static slotting decays under demand volatility; re-slotting frequency is open.",
  "ABC class boundaries are rules of thumb, not optima.",
  "Interaction with batching, routing, and automation complicates answers.",
 ],
 "requirements": [
  "SKU scoring on velocity, correlation, and ergonomics.",
  "Re-slotting triggers computed from savings versus move costs.",
  "Measured pick-density maps guiding location values.",
 ],
 "citations": [
  "Bartholdi JJ, Hackman ST (2019) Warehouse and Distribution Science. Georgia Tech.",
 ],
 "demo": {"lam": 8.5, "mu": 10.0},
},
# ----------------------------------------------------------------- rank 18
{
 "key": "ie-order-picking",
 "name": "The Order Picking Routing Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "In what sequence should a picker visit locations to fill an order - and how does the answer change when pickers, robots, and batching interact?",
 "background": "Order picking is the warehouse's core: the picker routing problem is a TSP in the aisles, solvable near-optimally for single pickers (Ratliff and Rosenthal, 1983, for standard layouts). But reality layers on: order batching (which orders ride together), picker blocking in narrow aisles, zone picking hand-offs, and now robot collaboration (goods-to-person, AMR fleets). Each layer has its own literature; the integrated problem - batch, assign, route, and coordinate humans and robots jointly - is far less solved. The picker-blocking problem alone (two pickers, one aisle) shows how interaction defeats decomposition.",
 "why_it_matters": "Order picking is over half of warehouse operating cost. The routing-batching-coordination stack decides whether e-commerce fulfillment makes or loses money.",
 "sig_lens": "The Signature lens reads the warehouse as a dance floor: the protocol must choreograph pickers and robots so nobody steps on anyone's route.",
 "sig_solution": LABEL + " Assumptions: (1) single-picker routing is solved; interaction is the hard part; (2) batching, routing, and coordination interact. Reasoning path: optimize the stack jointly on a rolling horizon - batch orders, route pickers, and deconflict in one loop rather than three silos. Proposed mechanism: a choreography protocol that batches by route-compatibility, routes with blocking-aware sequencing, and coordinates human-robot hand-offs through shared state - re-optimizing as orders arrive. Confirm: joint-stack optimization beats siloed batch-then-route on throughput. Kill: the joint problem proves too slow for real-time use. Does NOT claim: optimal warehouse orchestration - it choreographs the interactions the silos miss.",
 "pointer": "The Signature system's proposed approach jointly optimizes batching, routing, and human-robot coordination; the companion Signature Edition record specifies the choreography protocol.",
 "key_points": [
  "Single-picker routing in standard layouts is near-optimally solvable.",
  "Batching, blocking, zoning, and robots each add a literature of complexity.",
  "The integrated batch-assign-route-coordinate problem is far less solved.",
  "Picker blocking shows how interaction defeats decomposition.",
 ],
 "requirements": [
  "Route-compatibility-based order batching.",
  "Blocking-aware picker sequencing.",
  "Shared-state coordination for human-robot hand-offs.",
 ],
 "citations": [
  "Ratliff HD, Rosenthal AS (1983) Order-picking in a rectangular warehouse. Operations Research 31(3).",
 ],
 "demo": {"lam": 6.0, "mu": 7.0},
},
# ----------------------------------------------------------------- rank 19
{
 "key": "ie-planning-hierarchy",
 "name": "The Production Planning Hierarchy Integration Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Production planning runs in layers - aggregate planning, MPS, MRP, shop scheduling - but how can the layers be consistent when each optimizes with different granularity?",
 "background": "Hax and Meal's hierarchical production planning separates decisions by horizon: aggregate plans set capacities, the master schedule sets end-item timing, MRP explodes components, scheduling sequences operations. The architecture is brilliant and leaky: each layer's plan is infeasible for the layer below (aggregate plans ignore sequencing; MRP assumes infinite capacity), and the feedback loops that should reconcile them are ad hoc. Capacitated planning (CLSP at the aggregate level, finite-capacity scheduling below) helps but the consistency problem - plans that are simultaneously good at every layer - remains open. ERP systems implement the hierarchy's plumbing while the integration logic stays human.",
 "why_it_matters": "Every factory plans hierarchically; inconsistent layers mean the master schedule promises what the shop cannot deliver - the planning version of the bullwhip.",
 "sig_lens": "The Signature lens reads the hierarchy as a chain of command: each level must issue orders the next level can actually execute, and the protocol must verify executability downward.",
 "sig_solution": LABEL + " Assumptions: (1) layer plans are routinely infeasible below; (2) feedback loops are ad hoc. Reasoning path: verify downward - require each layer's plan to pass a feasibility check against the layer below's constraints before release, iterating until consistent. Proposed mechanism: a chain-of-command protocol where aggregate plans carry capacity reservations the master schedule must respect, MRP runs against finite-capacity profiles, and each layer's release requires a feasibility certificate from below. Confirm: certified hierarchies show fewer shop-floor infeasibilities. Kill: feasibility checking costs more than the infeasibilities it prevents. Does NOT claim: globally optimal hierarchical plans - it enforces executability down the chain.",
 "pointer": "The Signature system's proposed approach certifies each planning layer's feasibility against the layer below; the companion Signature Edition record specifies the chain-of-command protocol.",
 "key_points": [
  "Hierarchical planning separates horizons but leaks feasibility between layers.",
  "Aggregate plans ignore sequencing; MRP assumes infinite capacity.",
  "Feedback loops reconciling layers are ad hoc.",
  "ERP implements plumbing; integration logic stays human.",
 ],
 "requirements": [
  "Downward feasibility certificates before each layer's plan release.",
  "Capacity reservations flowing from aggregate to detailed plans.",
  "Iterative reconciliation until all layers are consistent.",
 ],
 "citations": [
  "Hax AC, Meal HC (1975) Hierarchical integration of production planning and scheduling. Sloan Management Review 16(3).",
 ],
 "demo": {"lam": 4.2, "mu": 5.8},
},
# ----------------------------------------------------------------- rank 20
{
 "key": "ie-lot-sizing",
 "name": "The Capacitated Lot Sizing Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "How much should be produced each period when setups cost, capacity binds, and demand is known - and why does adding capacity make the easy problem hard?",
 "background": "The uncapacitated Wagner-Whitin lot-sizing problem solves by dynamic programming; adding capacity constraints (CLSP) makes it NP-hard, and multi-item, multi-level capacitated versions defeat exact methods at industrial scale. The problem is the beating heart of MRP systems: every planned order is a lot-sizing decision. Heuristics (Silver-Meal, part-period balancing, Lagrangian relaxations) abound, but the gap to optimal on real instances is unmeasured - the plans run the factory while their suboptimality is unknown. Setup carryover, overtime options, and rolling horizons each add realistic complexity the theory handles partially.",
 "why_it_matters": "Lot sizes set inventory and setup costs across manufacturing. The unmeasured gap between heuristic lots and optimal ones is a standing tax on production.",
 "sig_lens": "The Signature lens reads lot sizing as a rhythm: the protocol must find the production rhythm that the capacity can actually dance to.",
 "sig_solution": LABEL + " Assumptions: (1) capacity makes the easy problem NP-hard; (2) heuristic gaps are unmeasured in practice. Reasoning path: measure the gap where it matters - compute lower bounds on the real instances and focus exact effort on the periods where the bound shows money. Proposed mechanism: a rhythm protocol that solves the Lagrangian relaxation for a valid lower bound on each planning run, reports the heuristic-to-bound gap, and escalates to exact methods only where the gap is material. Confirm: gap-escalated lot-sizing closes more cost than blanket heuristics. Kill: the bounds prove too weak to guide escalation. Does NOT claim: optimal capacitated lots - it finds the rhythm the capacity can dance to and prices the rest.",
 "pointer": "The Signature system's proposed approach bounds the lot-sizing gap and escalates exact methods where it is material; the companion Signature Edition record specifies the rhythm protocol.",
 "key_points": [
  "Uncapacitated lot-sizing is polynomial; capacitated is NP-hard.",
  "CLSP is the heart of MRP; its heuristic gaps are unmeasured.",
  "Multi-item multi-level versions defeat exact methods at scale.",
  "Setup carryover and overtime add partially-handled complexity.",
 ],
 "requirements": [
  "Lagrangian lower bounds computed on every planning run.",
  "Heuristic-to-bound gap reporting.",
  "Exact-method escalation only where gaps are material.",
 ],
 "citations": [
  "Wagner HM, Whitin TM (1958) Dynamic version of the economic lot size model. Management Science 5(1).",
 ],
 "demo": {"lam": 7.2, "mu": 9.8},
},
# ----------------------------------------------------------------- rank 21
{
 "key": "ie-hrc-safety",
 "name": "The Human Robot Collaboration Safety Problem",
 "group": "Human Factors",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "How can humans and robots share a workspace productively when the safety standards were written for caged robots and the collaboration modes keep evolving?",
 "background": "ISO/TS 15066 gives biomechanical force and pressure limits for collaborative robots, but the standard covers quasi-static contact - the real risks are dynamic: a moving robot striking a moving human, with relative velocities the standard barely addresses. Power-and-force limiting, speed-and-separation monitoring, and hand-guiding each have gaps, and the productivity-safety tradeoff is unmapped: slower robots are safer and uneconomical. The deeper problem is human unpredictability - workers adapt, shortcut, and habituate around cobots in ways no risk assessment predicts. Standards evolve slower than deployments.",
 "why_it_matters": "Collaborative robots are the fastest-growing automation segment. Safety standards that miss the real risks invite injuries; over-conservative ones kill the business case.",
 "sig_lens": "The Signature lens reads collaboration as a dance with a partner who cannot feel: the protocol must choreograph separation and contact, and watch the human partner's improvisations.",
 "sig_solution": LABEL + " Assumptions: (1) standards cover quasi-static contact; dynamic risks are under-addressed; (2) humans adapt around cobots unpredictably. Reasoning path: monitor the actual human-robot interaction envelope in deployment and adapt the safety parameters to observed behavior - not just the standard's assumptions. Proposed mechanism: a dance protocol that instruments the shared workspace, measures actual separation distances and contact events, adapts speed limits to observed human behavior patterns, and reports the productivity-safety frontier being operated on. Confirm: behavior-adapted cells show fewer near-misses at equal throughput. Kill: instrumentation misses the critical events and adaptation is blind. Does NOT claim: a complete safety guarantee - it watches the dance and tightens the choreography.",
 "pointer": "The Signature system's proposed approach instruments shared workspaces and adapts safety parameters to observed behavior; the companion Signature Edition record specifies the dance protocol.",
 "key_points": [
  "ISO/TS 15066 covers quasi-static contact; dynamic collision risks are under-addressed.",
  "The productivity-safety tradeoff for cobots is unmapped.",
  "Workers habituate and shortcut around cobots unpredictably.",
  "Standards evolve slower than deployments.",
 ],
 "requirements": [
  "Workspace instrumentation measuring actual separations and contacts.",
  "Behavior-adapted speed and separation parameters.",
  "Reported productivity-safety frontier per cell.",
 ],
 "citations": [
  "ISO/TS 15066:2016 Robots and robotic devices - Collaborative robots.",
 ],
 "demo": {"lam": 3.0, "mu": 4.5},
},
# ----------------------------------------------------------------- rank 22
{
 "key": "ie-exoskeleton",
 "name": "The Exoskeleton Effectiveness Problem",
 "group": "Human Factors",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Workplace exoskeletons promise to cut musculoskeletal injuries - but do they work in real jobs, and what do they cost in comfort, mobility, and new risks?",
 "background": "Passive and active exoskeletons for overhead work, lifting, and bending are deploying across automotive, logistics, and construction, driven by the enormous cost of musculoskeletal disorders. Lab studies show reduced muscle activation; field effectiveness is far less clear - adoption drops when devices chafe, overheat, or slow workers, and the injury-reduction evidence is mostly short-term and self-reported. The unanswered questions compound: do exoskeletons shift load to unprotected joints, does long-term use weaken muscles, and which tasks genuinely benefit versus which just look good in demos. The evaluation science lags the marketing by years.",
 "why_it_matters": "Musculoskeletal disorders are the costliest workplace injury category. Exoskeletons that work would prevent real suffering; ones that do not waste money and breed cynicism about ergonomics.",
 "sig_lens": "The Signature lens reads exoskeletons as braces: the protocol must verify the brace helps the joint it claims to, and check the joints it does not mention.",
 "sig_solution": LABEL + " Assumptions: (1) lab muscle-activation reductions do not imply field injury reductions; (2) adoption and comfort decide real effectiveness. Reasoning path: evaluate exoskeletons on the full ledger - injury rates, comfort, mobility, adoption, and load-shifting - in real jobs over real durations. Proposed mechanism: a brace protocol requiring field trials measuring injury incidence (not just EMG), comfort and adoption tracking, and screening for load-shifting to unprotected joints - with deployment gated on the full ledger, not the lab demo. Confirm: ledger-gated deployments show sustained injury reduction. Kill: field injury effects prove too slow to measure and trials never complete. Does NOT claim: a verdict on exoskeletons generally - it keeps the full books per device per task.",
 "pointer": "The Signature system's proposed approach evaluates exoskeletons on full field ledgers including load-shifting; the companion Signature Edition record specifies the brace protocol.",
 "key_points": [
  "Lab studies show reduced muscle activation; field injury evidence is weak.",
  "Adoption collapses on comfort, heat, and mobility problems.",
  "Load-shifting to unprotected joints is under-studied.",
  "Long-term muscle-weakening effects are unknown.",
 ],
 "requirements": [
  "Field trials measuring injury incidence over real durations.",
  "Comfort, mobility, and adoption tracking alongside biomechanics.",
  "Load-shifting screening for unprotected joints.",
 ],
 "citations": [
  "de Looze MP et al. (2016) Exoskeletons for industrial application and their potential effects. Ergonomics 59(5).",
 ],
 "demo": {"lam": 5.8, "mu": 8.2},
},
# ----------------------------------------------------------------- rank 23
{
 "key": "ie-safety-culture",
 "name": "The Safety Culture Measurement Problem",
 "group": "Human Factors",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Everyone agrees safety culture prevents accidents - but what is it, how is it measured, and do the measurements predict anything?",
 "background": "Since Chernobyl's inquiry named safety culture (INSAG, 1986), the concept has organized safety science: shared values and practices around risk. But measurement is stuck on climate surveys - questionnaires asking workers if they feel safe reporting - which measure espoused values, not practiced ones, and correlate weakly with accident rates. The leading-indicator quest (near-miss reporting rates, safety observations) fares little better: reporting rises with trust, which is the thing being measured. The construct validity problem is fundamental - nobody agrees what safety culture is - so the instruments cannot be validated against it. Yet regulators and firms manage by these numbers.",
 "why_it_matters": "Safety culture scores steer real safety budgets. Invalid measurements do not just waste money - they manufacture assurance where none exists, the precondition of every major accident.",
 "sig_lens": "The Signature lens reads safety culture as practiced, not professed: the protocol must measure what people do under pressure, not what they tell surveys.",
 "sig_solution": LABEL + " Assumptions: (1) surveys measure espoused values; (2) construct validity is unresolved. Reasoning path: measure behavior under pressure - stop-work authority usage, near-miss reporting quality, resource allocation to safety - and treat surveys as secondary. Proposed mechanism: a practiced-values protocol tracking behavioral indicators (stop-work invocations and their outcomes, reporting latency, safety budget defense in downturns), triangulated with surveys but never led by them. Confirm: behavioral indicators predict incident rates better than survey scores. Kill: behavioral indicators prove as gameable as surveys. Does NOT claim: a validated safety-culture construct - it measures the practices and lets the construct debate continue.",
 "pointer": "The Signature system's proposed approach measures safety through pressured behavior, not surveys; the companion Signature Edition record specifies the practiced-values protocol.",
 "key_points": [
  "Safety culture was named after Chernobyl; measurement never caught up.",
  "Climate surveys measure espoused values and correlate weakly with accidents.",
  "Leading indicators (near-miss rates) confound trust with safety.",
  "Construct validity is unresolved; instruments cannot be validated.",
 ],
 "requirements": [
  "Behavioral indicators: stop-work usage, reporting quality, budget defense.",
  "Survey data triangulated but never leading.",
  "Incident-rate prediction testing of every metric used.",
 ],
 "citations": [
  "Guldenmund FW (2000) The nature of safety culture: a review of theory and research. Safety Science 34(1-3).",
 ],
 "demo": {"lam": 6.8, "mu": 9.5},
},
# ----------------------------------------------------------------- rank 24
{
 "key": "ie-cognitive-workload",
 "name": "The Cognitive Workload Quantification Problem",
 "group": "Human Factors",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Mental workload decides whether operators cope or collapse - but how can it be measured continuously without interrupting the work it measures?",
 "background": "NASA-TLX (Hart and Staveland, 1988) made workload measurable by questionnaire - after the fact, subjectively, and interruptively. The operational need is real-time, objective, non-intrusive measurement: air traffic controllers, pilots, surgeons, and control-room operators all work near cognitive limits where overload kills. Physiological candidates (pupillometry, EEG, heart-rate variability) correlate with workload in labs but are confounded in the field by emotion, fatigue, and movement; performance-based inference is circular (workload is inferred from the errors it is meant to predict). The ground-truth problem is fundamental: there is no independent meter for mental workload to calibrate against.",
 "why_it_matters": "Overload causes the accidents that postmortems call human error. An honest workload meter would staff, schedule, and automate around human limits instead of discovering them in wreckage.",
 "sig_lens": "The Signature lens reads workload as a fuel gauge with no sensor: the protocol must triangulate from every available signal and never trust any single one.",
 "sig_solution": LABEL + " Assumptions: (1) no ground-truth workload meter exists; (2) every signal is confounded. Reasoning path: fuse multiple weak signals (task demand models, physiological streams, performance drift) into a workload estimate with honest uncertainty, and act on the lower confidence bound. Proposed mechanism: a fuel-gauge protocol combining analytic task-demand models with calibrated physiological and performance signals, reporting workload with uncertainty bands, and triggering automation support or staffing changes when the lower band crosses safe limits. Confirm: fused estimates predict overload incidents better than any single signal. Kill: the fusion inherits every confound and the gauge is noise. Does NOT claim: a true workload measurement - it triangulates with the uncertainty shown.",
 "pointer": "The Signature system's proposed approach fuses workload signals with honest uncertainty bands; the companion Signature Edition record specifies the fuel-gauge protocol.",
 "key_points": [
  "NASA-TLX measures workload subjectively, retrospectively, interruptively.",
  "Physiological signals correlate in labs but confound in the field.",
  "Performance-based inference is circular.",
  "No independent ground truth exists for calibration.",
 ],
 "requirements": [
  "Multi-signal fusion: task models, physiology, performance drift.",
  "Uncertainty bands on every workload estimate.",
  "Automation triggers on the lower confidence bound, not the point estimate.",
 ],
 "citations": [
  "Hart SG, Staveland LE (1988) Development of NASA-TLX. In Human Mental Workload. North-Holland.",
 ],
 "demo": {"lam": 4.8, "mu": 6.2},
},
# ----------------------------------------------------------------- rank 25
{
 "key": "ie-injury-prediction",
 "name": "The Ergonomic Injury Prediction Problem",
 "group": "Human Factors",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Can musculoskeletal injury risk be predicted for a specific worker doing a specific job - before the injury happens?",
 "background": "Ergonomic assessment tools (REBA, RULA, NIOSH lifting equation, Liberty Mutual tables) score job demands against population thresholds, but individual prediction remains out of reach: two workers doing the same job differ in anthropometry, conditioning, history, and technique, and the tools ignore most of it. Wearable sensors now capture kinematics continuously, and machine learning finds patterns - but the patterns predict reported discomfort better than actual injury, the labels (injury reports) are confounded by reporting culture, and the individual risk factors interact nonlinearly. The ethical dimension sharpens the technical one: individual predictions invite discrimination, so even a working predictor faces deployment barriers.",
 "why_it_matters": "Musculoskeletal injuries cost employers tens of billions yearly and workers their livelihoods. Prediction would move ergonomics from job design to personal prevention.",
 "sig_lens": "The Signature lens reads injury risk as weather for one person: the protocol must forecast the storm for the individual while protecting them from the forecast's misuse.",
 "sig_solution": LABEL + " Assumptions: (1) population tools cannot predict individuals; (2) individual predictions invite discrimination. Reasoning path: predict at the job-task level with individual modifiers kept private to the worker, and use predictions only to redesign work - never to select workers. Proposed mechanism: a personal-weather protocol that fuses job-demand assessment with voluntary individual data (kept worker-private), outputs task-redesign priorities, and contractually bars the predictions from employment decisions. Confirm: redesign-prioritized interventions cut injury rates more than threshold-based ones. Kill: individual modifiers prove unmeasurable and the personalization is noise. Does NOT claim: individual injury prediction as a solved product - it forecasts to redesign, with misuse bars.",
 "pointer": "The Signature system's proposed approach predicts injury risk to redesign work, with predictions barred from employment use; the companion Signature Edition record specifies the personal-weather protocol.",
 "key_points": [
  "Assessment tools score jobs against population thresholds, not individuals.",
  "Wearables capture kinematics but predict discomfort better than injury.",
  "Injury labels are confounded by reporting culture.",
  "Individual predictions raise discrimination risks that block deployment.",
 ],
 "requirements": [
  "Job-task-level prediction with worker-private individual modifiers.",
  "Predictions used only for work redesign, never worker selection.",
  "Contractual bars on employment use of risk scores.",
 ],
 "citations": [
  "Waters TR et al. (1993) Revised NIOSH equation for the design and evaluation of manual lifting tasks. Ergonomics 36(7).",
 ],
 "demo": {"lam": 3.8, "mu": 5.5},
},
# ----------------------------------------------------------------- rank 26
{
 "key": "ie-doe-complex",
 "name": "The Design of Experiments for Complex Systems Problem",
 "group": "Quality Engineering",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Classical DOE assumes a handful of controllable factors - but how should experiments be designed when the system has hundreds of inputs, simulations replace benches, and time is the budget?",
 "background": "Fisher's DOE - randomization, blocking, factorial designs - tamed agricultural and industrial experiments with few factors. Modern systems break every assumption: hundreds of inputs (screening problem), deterministic computer simulations (no random error, so replication is pointless), and sequential decision-making where each experiment's result shapes the next. Space-filling designs (Latin hypercubes), Bayesian optimization, and active learning fill parts of the gap, but the integrated problem - designing an experimental campaign across physical and virtual experiments with a time budget - has no general theory. Practitioners either over-experiment cheaply (wasting time) or under-experiment critically (missing interactions).",
 "why_it_matters": "Experiments are how engineering learns: badly designed campaigns waste the scarcest resource (time) while missing the interactions that matter.",
 "sig_lens": "The Signature lens reads experiments as questions with price tags: the protocol must buy the most informative questions first and stop when the answers stop being worth the price.",
 "sig_solution": LABEL + " Assumptions: (1) classical DOE assumptions fail on modern systems; (2) physical and virtual experiments must be designed jointly. Reasoning path: design campaigns by value of information - rank candidate experiments by expected learning per unit time and cost, across physical and simulation experiments. Proposed mechanism: a question-pricing protocol that maintains a surrogate model of the system, prices each candidate experiment by expected information gain per cost, runs the winners, and stops the campaign when marginal gain falls below the time's value. Confirm: priced campaigns learn more per experiment-dollar than factorial defaults. Kill: the surrogate misprices and the campaign chases noise. Does NOT claim: optimal experimental design in general - it buys information where it is cheapest.",
 "pointer": "The Signature system's proposed approach designs experimental campaigns by value-of-information pricing; the companion Signature Edition record specifies the question-pricing protocol.",
 "key_points": [
  "Classical DOE assumes few factors and random error; modern systems break both.",
  "Deterministic simulations make replication pointless - a conceptual break.",
  "Space-filling and Bayesian methods cover parts of the gap.",
  "Joint physical-virtual campaign design has no general theory.",
 ],
 "requirements": [
  "Surrogate models maintained across the campaign.",
  "Per-experiment information-gain-per-cost pricing.",
  "Stopping rules on marginal information value.",
 ],
 "citations": [
  "Santner TJ, Williams BJ, Notz WI (2018) The Design and Analysis of Computer Experiments, 2nd ed. Springer.",
 ],
 "demo": {"lam": 5.2, "mu": 7.8},
},
# ----------------------------------------------------------------- rank 27
{
 "key": "ie-response-surface",
 "name": "The Response Surface Global Optimization Problem",
 "group": "Quality Engineering",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Response surface methodology climbs to local optima efficiently - but how can the global optimum be found when the surface is multimodal and each evaluation is expensive?",
 "background": "Box and Wilson's response surface methodology (1951) - fit a local model, step uphill, repeat - is the workhorse of empirical optimization, but it converges to local optima. Global optimization of expensive black boxes is the domain of Bayesian optimization (Jones et al., EGO, 1998), which balances exploration and exploitation via acquisition functions - yet its guarantees are asymptotic, its Gaussian-process models strain past dozens of dimensions, and the exploration-exploitation tradeoff has no finite-time optimality theory. The practical question - how many evaluations to budget before declaring victory - is answered by exhaustion, not theory.",
 "why_it_matters": "Tuning processes, formulations, and designs means optimizing expensive black boxes. Local optima found confidently are the most expensive kind of wrong answer.",
 "sig_lens": "The Signature lens reads the surface as terrain in fog: the protocol must map enough to avoid the foothills being mistaken for the peak.",
 "sig_solution": LABEL + " Assumptions: (1) RSM finds local optima; Bayesian optimization has asymptotic-only guarantees; (2) evaluation budgets are finite and binding. Reasoning path: budget the search explicitly - allocate evaluations between global exploration and local refinement by the remaining budget, and report the global-optimality gap honestly. Proposed mechanism: a terrain protocol that runs Bayesian optimization with a budget-aware acquisition schedule (exploration-heavy early, refinement late), tracks the best-known global gap via Lipschitz or GP bounds, and reports the gap with the answer. Confirm: budget-aware schedules beat fixed strategies on benchmark suites. Kill: the gap bounds prove too loose to inform stopping. Does NOT claim: global optima - it maps the fog and reports how much remains.",
 "pointer": "The Signature system's proposed approach runs budget-aware global search with honest gap reporting; the companion Signature Edition record specifies the terrain protocol.",
 "key_points": [
  "RSM climbs efficiently to local optima only.",
  "Bayesian optimization guarantees are asymptotic; GPs strain in high dimensions.",
  "No finite-time theory governs the exploration-exploitation tradeoff.",
  "Evaluation budgets are set by exhaustion, not theory.",
 ],
 "requirements": [
  "Budget-aware acquisition schedules (explore early, refine late).",
  "Global-optimality gap tracking via available bounds.",
  "Honest gap reporting with every reported optimum.",
 ],
 "citations": [
  "Jones DR et al. (1998) Efficient global optimization of expensive black-box functions. J. Global Optimization 13(4).",
 ],
 "demo": {"lam": 6.3, "mu": 8.8},
},
# ----------------------------------------------------------------- rank 28
{
 "key": "ie-disruption-network",
 "name": "The Supply Chain Network Design Under Disruption Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "How should a supply network be designed when facilities can fail - and how can the design hedge against disruptions whose probabilities are unknown?",
 "background": "Classical network design optimizes for the sunny day; disruption-aware design (Snyder and Daskin, reliability models) adds facility failure scenarios - but the failure probabilities are the problem. Historical disruption data is sparse, failures correlate (a hurricane hits a region, not a dice roll), and deep uncertainty (unknown unknowns) resists probabilistic modeling entirely. Robust and distributionally robust formulations hedge without probabilities but pay conservatism. The dynamic version - networks that reconfigure as disruptions unfold - is barely modeled. Practice designs for cost and hopes for luck.",
 "why_it_matters": "Supply networks are decade-scale commitments. Designing them for the sunny day and hoping is how the last decade's disruptions became catastrophes.",
 "sig_lens": "The Signature lens reads the network as a bridge system: the protocol must design for the storm season, not the weather report - with the storm probabilities honestly labeled as guesses.",
 "sig_solution": LABEL + " Assumptions: (1) disruption probabilities are deeply uncertain; (2) failures correlate geographically. Reasoning path: design for graceful degradation - optimize the network's performance across a stress-test ensemble rather than for expected cost under guessed probabilities. Proposed mechanism: a storm-season protocol that stress-tests candidate networks against disruption ensembles (historical, synthetic, adversarial), selects designs by worst-regret across the ensemble, and builds reconfiguration options (backup suppliers, flexible capacity) into the design. Confirm: ensemble-designed networks degrade more gracefully in real disruptions. Kill: the ensemble misses the true disruption mode and the design is mis-hedged. Does NOT claim: optimal disruption hedging - it designs for the storm season with honest probability labels.",
 "pointer": "The Signature system's proposed approach stress-tests networks on disruption ensembles and designs for graceful degradation; the companion Signature Edition record specifies the storm-season protocol.",
 "key_points": [
  "Classical design optimizes the sunny day; disruption probabilities are unknown.",
  "Failures correlate geographically; independent-failure models mislead.",
  "Robust formulations hedge but pay unpriced conservatism.",
  "Dynamic reconfiguration during disruptions is barely modeled.",
 ],
 "requirements": [
  "Disruption ensembles: historical, synthetic, and adversarial scenarios.",
  "Worst-regret selection across the ensemble.",
  "Reconfiguration options built into the network design.",
 ],
 "citations": [
  "Snyder LV, Daskin MS (2005) Reliability models for facility location. Transportation Science 39(4).",
 ],
 "demo": {"lam": 4.6, "mu": 6.9},
},
# ----------------------------------------------------------------- rank 29
{
 "key": "ie-toc-limits",
 "name": "The Theory of Constraints Throughput Limit Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "The Theory of Constraints says throughput is set by the constraint - but what are the theory's own limits, and where does it break down?",
 "background": "Goldratt's Theory of Constraints (TOC) - identify the constraint, exploit it, subordinate everything, elevate it, repeat - transformed operations thinking, and drum-buffer-rope scheduling operationalizes it. But the theory's limits are under-examined: with multiple interacting constraints the five focusing steps cycle without converging, the constraint in services and knowledge work is rarely a physical resource, and the throughput-accounting measures (T, I, OE) have known paradoxes. The critical-chain project management offshoot shows mixed empirical results. TOC is a powerful lens that its own literature rarely turns on itself.",
 "why_it_matters": "TOC guides improvement programs worldwide. A theory applied past its limits misidentifies constraints and subordinates the wrong things - organized, confident error.",
 "sig_lens": "The Signature lens reads TOC as a compass, not a map: the protocol must check the terrain before marching, and know where compasses spin.",
 "sig_solution": LABEL + " Assumptions: (1) TOC's five steps assume a stable dominant constraint; (2) interacting constraints defeat the method. Reasoning path: test the theory's preconditions before applying it - verify constraint stability and dominance, and switch methods where they fail. Proposed mechanism: a compass-check protocol that measures constraint stability over time, applies TOC only where a dominant stable constraint exists, and routes multi-constraint or shifting-constraint systems to alternative methods - with the routing decision documented. Confirm: precondition-checked TOC applications outperform blanket ones. Kill: the preconditions prove unmeasurable in practice. Does NOT claim: a replacement theory - it maps where the compass works.",
 "pointer": "The Signature system's proposed approach checks TOC preconditions and routes unsuitable systems elsewhere; the companion Signature Edition record specifies the compass-check protocol.",
 "key_points": [
  "TOC's five focusing steps assume a stable, dominant constraint.",
  "Multiple interacting constraints defeat the method's convergence.",
  "Throughput accounting has known paradoxes.",
  "Critical chain shows mixed empirical results.",
 ],
 "requirements": [
  "Constraint-stability measurement before TOC application.",
  "Documented routing decisions for unsuitable systems.",
  "Alternative methods for multi-constraint environments.",
 ],
 "citations": [
  "Goldratt EM (1990) Theory of Constraints. North River Press.",
 ],
 "demo": {"lam": 7.8, "mu": 10.2},
},
# ----------------------------------------------------------------- rank 30
{
 "key": "ie-jidoka",
 "name": "The Jidoka Automation Limit Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Jidoka - automation with a human touch, machines that stop on abnormality - is lean canon, but where are its limits, and what breaks when everything stops?",
 "background": "Jidoka (Sakichi Toyoda's loom that stopped on thread break; systematized at Toyota) means building quality into the process: detect the abnormality, stop, fix the root cause. Andon cords empower every worker to stop the line. But the limits are real: in high-speed continuous processes, stopping is enormously expensive; false stops from oversensitive detection destroy flow; and the root-cause discipline the philosophy demands is the first casualty of production pressure. The automation frontier - deciding what abnormalities machines detect versus what needs human judgment - has no general theory. Plants implement the rituals (andon cords nobody pulls) without the substance.",
 "why_it_matters": "Jidoka is the quality philosophy behind lean's success. Ritual jidoka - cords nobody pulls, stops nobody honors - is quality theater that hides defects instead of exposing them.",
 "sig_lens": "The Signature lens reads jidoka as an alarm system: the protocol must tune the alarms so real fires get a response and false alarms do not teach everyone to ignore them.",
 "sig_solution": LABEL + " Assumptions: (1) stop discipline decays under production pressure; (2) false stops teach workers to ignore alarms. Reasoning path: engineer the stop economics - make true stops cheap and informative, false stops rare, and root-cause follow-through mandatory and measured. Proposed mechanism: an alarm protocol that tunes detection thresholds on measured false-stop rates, tracks stop-to-root-cause closure rates, prices the stop (lost production versus defect escape), and audits andon-pull rates as the health metric of the culture. Confirm: tuned jidoka systems show higher pull rates and lower escape rates. Kill: production pressure overrides the protocol and pulls decay anyway. Does NOT claim: a general theory of automation limits - it keeps the alarms honest.",
 "pointer": "The Signature system's proposed approach tunes jidoka alarms on measured false-stop rates and audits pull rates; the companion Signature Edition record specifies the alarm protocol.",
 "key_points": [
  "Jidoka means stop-on-abnormality with root-cause discipline.",
  "False stops destroy flow and teach workers to ignore alarms.",
  "Production pressure is the first killer of stop discipline.",
  "The machine-versus-human detection frontier has no general theory.",
 ],
 "requirements": [
  "Detection thresholds tuned on measured false-stop rates.",
  "Stop-to-root-cause closure tracking.",
  "Andon-pull rates audited as the culture health metric.",
 ],
 "citations": [
  "Ohno T (1988) Toyota Production System. Productivity Press.",
 ],
 "demo": {"lam": 5.6, "mu": 8.4},
},
# ----------------------------------------------------------------- rank 31
{
 "key": "ie-resilience-quant",
 "name": "The Resilience Engineering Quantification Problem",
 "group": "Human Factors",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Resilience engineering studies how systems succeed under pressure - but how can the capacity to adapt be measured before the crisis tests it?",
 "background": "Resilience engineering (Hollnagel, Woods, Leveson) inverted safety science: instead of studying failures, study how everyday work succeeds despite pressure - the Safety-II program. The concepts (adaptive capacity, graceful extensibility, margin) are powerful and nearly unmeasured: nobody knows how to quantify a system's adaptive capacity before it is needed, the metrics proposed (buffer sizes, response repertoires) are proxies, and the validation problem is circular (resilient systems are identified by surviving, which is the thing to predict). Regulators and firms want resilience scores; the science offers case studies.",
 "why_it_matters": "The next accident will happen to a system whose resilience was asserted, not measured. Unmeasured adaptive capacity is a hope, not a property.",
 "sig_lens": "The Signature lens reads resilience as muscle: the protocol must exercise it in drills and measure the strain, not admire it in the mirror.",
 "sig_solution": LABEL + " Assumptions: (1) adaptive capacity is real and currently unmeasured; (2) validation is circular if based on survival. Reasoning path: measure resilience in exercises - inject controlled disruptions in drills and measure detection, response, and recovery - and treat drill performance as the metric. Proposed mechanism: a muscle protocol of regular resilience drills with measured scenarios, scoring detection latency, coordination quality, and recovery completeness - tracked over time as the resilience index, with the index's limits (drill versus real) stated. Confirm: drill-measured indices predict real disruption performance better than proxy metrics. Kill: drills fail to reproduce real-crisis dynamics and the index misleads. Does NOT claim: a true measure of adaptive capacity - it exercises the muscle and records the strain.",
 "pointer": "The Signature system's proposed approach measures resilience through scored disruption drills; the companion Signature Edition record specifies the muscle protocol.",
 "key_points": [
  "Safety-II studies success under pressure instead of failure.",
  "Adaptive capacity has no validated pre-crisis measure.",
  "Proposed metrics are proxies; validation is circular.",
  "Regulators want scores; science offers case studies.",
 ],
 "requirements": [
  "Regular controlled-disruption drills with measured scenarios.",
  "Scoring of detection, coordination, and recovery.",
  "Tracked resilience indices with stated drill-versus-real limits.",
 ],
 "citations": [
  "Hollnagel E, Woods DD, Leveson N (2006) Resilience Engineering. Ashgate.",
 ],
 "demo": {"lam": 8.2, "mu": 11.5},
},
# ----------------------------------------------------------------- rank 32
{
 "key": "ie-material-handling",
 "name": "The Material Handling System Selection Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Conveyors, AGVs, AMRs, forklifts - how should the material handling system be chosen when the options multiply and the decision locks in for a decade?",
 "background": "Material handling equipment selection is a multi-decade commitment made under deep uncertainty: conveyors are fixed and efficient, AGVs follow fixed paths, AMRs navigate freely, forklifts flex with labor. The selection methods (scoring models, AHP, simulation) compare options on today's flows, but flows change, technology evolves (AMR capabilities are moving fast), and the flexibility value of mobile systems resists quantification. The equipment interacts with layout, storage, and labor in ways selection models simplify away. Wrong choices strand capital for decades; the selection science has not kept pace with the option explosion.",
 "why_it_matters": "Material handling is the circulatory system of the factory and a major capital decision. A wrong system choice taxes every move for a decade.",
 "sig_lens": "The Signature lens reads handling systems as commitments with different escape hatches: the protocol must price the flexibility of each option, not just its efficiency today.",
 "sig_solution": LABEL + " Assumptions: (1) flows will change over the equipment lifetime; (2) flexibility value resists standard quantification. Reasoning path: value options explicitly - model the handling choice as a real-options problem where mobile systems carry reconfiguration options fixed systems lack. Proposed mechanism: a circulatory protocol that evaluates handling alternatives on total cost across flow scenarios (not just today's), prices reconfiguration options via scenario analysis, and stages the investment (pilot fleets before full deployment) to buy information. Confirm: options-valued selections outperform static scoring on lifetime cost. Kill: the scenario probabilities mislead and the options are mispriced. Does NOT claim: the right handling system in general - it prices flexibility alongside efficiency.",
 "pointer": "The Signature system's proposed approach values handling systems as real options across flow scenarios; the companion Signature Edition record specifies the circulatory protocol.",
 "key_points": [
  "Handling choices lock in for a decade under deep flow uncertainty.",
  "Conveyors, AGVs, AMRs, and forklifts trade efficiency against flexibility.",
  "Flexibility value resists standard selection-model quantification.",
  "Selection science lags the AMR-driven option explosion.",
 ],
 "requirements": [
  "Total-cost evaluation across flow scenarios, not point forecasts.",
  "Real-options pricing of reconfiguration flexibility.",
  "Staged investment: pilot fleets before full deployment.",
 ],
 "citations": [
  "Tompkins JA et al. (2010) Facilities Planning, 4th ed. Wiley.",
 ],
 "demo": {"lam": 6.6, "mu": 9.2},
},
# ----------------------------------------------------------------- rank 33
{
 "key": "ie-setup-sequencing",
 "name": "The Sequencing With Setup Times Problem",
 "group": "Manufacturing Systems",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "When switching products costs time that depends on the sequence - paint shops, food processing - what production sequence minimizes total setup, and how close can practice get?",
 "background": "Sequence-dependent setups turn scheduling into a TSP-like problem on every machine: the setup from product A to B differs from B to A (color sequencing dark-to-light, allergen cleaning). The problem is NP-hard even on single machines, and the setup times themselves are often estimated, not measured - the data foundation is soft. Heuristics (nearest neighbor, insertion, tabu search) find good sequences, but the interaction with lot sizing (sequence and batch size jointly determine cost) is the deeper unsolved coupling: the literature treats them separately while practice decides them together. Real shops sequence by tribal knowledge that outperforms the models nobody runs.",
 "why_it_matters": "Setup time is pure waste between value-adding runs. In process industries it dominates the schedule - and tribal knowledge currently beats the science.",
 "sig_lens": "The Signature lens reads setups as tolls between products: the protocol must map the tolls accurately and route production to pay the least.",
 "sig_solution": LABEL + " Assumptions: (1) sequence-dependent setups make scheduling TSP-hard per machine; (2) setup times are often estimated, not measured. Reasoning path: measure the tolls first - time actual changeovers - then sequence on measured data, coupling the sequence with lot sizing. Proposed mechanism: a toll-map protocol that measures setup times empirically, solves the sequencing problem on the measured matrix with heuristics plus lower bounds, and jointly adjusts lot sizes where the sequence shows savings - capturing the tribal knowledge in the model. Confirm: measured-toll sequencing beats tribal knowledge on setup cost. Kill: setup times prove too variable to measure usefully. Does NOT claim: optimal sequences - it maps the tolls and routes on the map.",
 "pointer": "The Signature system's proposed approach measures setup tolls empirically and sequences on the measured map; the companion Signature Edition record specifies the toll-map protocol.",
 "key_points": [
  "Sequence-dependent setups are NP-hard even on single machines.",
  "Setup times are usually estimated, not measured - soft data foundations.",
  "Sequencing interacts with lot sizing; the literature treats them separately.",
  "Tribal knowledge often beats the models in practice.",
 ],
 "requirements": [
  "Empirically measured setup-time matrices.",
  "Heuristic sequencing with lower-bound gap reporting.",
  "Joint sequence and lot-size adjustment.",
 ],
 "citations": [
  "Allahverdi A et al. (2008) A survey of scheduling problems with setup times. EJOR 187(3).",
 ],
 "demo": {"lam": 4.4, "mu": 7.6},
},
# ----------------------------------------------------------------- rank 34
{
 "key": "ie-unified-human-machine",
 "name": "The Unified Human Machine System Design Problem",
 "group": "Human Factors",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Humans and machines are designed separately and integrated hopefully - is there a unified science for designing the joint cognitive system?",
 "background": "Human factors designs the human side, automation designs the machine side, and the integration - the joint cognitive system (Hollnagel and Woods) - is where accidents live: mode confusion, automation surprise, deskilling, and the ironies of automation (Bainbridge, 1983: automation shifts humans to supervisory roles they perform worse). Function allocation (Fitts' list: humans are better at, machines are better at) is static folklore; dynamic allocation that shifts with workload and situation is the aspiration without a science. The levels-of-automation framework (Parasuraman, Sheridan, Wickens) describes options but does not prescribe choices. Nobody designs the human-machine system as one system.",
 "why_it_matters": "Aviation, medicine, and autonomous systems are joint cognitive systems. Designing the halves separately and hoping the whole works is how automation surprises are manufactured.",
 "sig_lens": "The Signature lens reads the human-machine pair as one mind with two substrates: the protocol must design the thinking of the pair, not the parts.",
 "sig_solution": LABEL + " Assumptions: (1) separate design plus hopeful integration manufactures automation surprise; (2) static function allocation is folklore. Reasoning path: design the joint system first - specify who does what under which conditions, with dynamic reallocation rules - then design each half to its joint role. Proposed mechanism: a one-mind protocol that starts every automation project with a joint-cognitive design (task allocation across workload states, handover protocols, surprise audits), validates the pair in simulation before building either half, and monitors automation surprise incidents in deployment. Confirm: joint-designed systems show fewer automation surprises. Kill: the joint design proves too abstract to guide engineering. Does NOT claim: a unified science of human-machine systems - it designs the pair's thinking as one problem.",
 "pointer": "The Signature system's proposed approach designs the human-machine pair as one cognitive system; the companion Signature Edition record specifies the one-mind protocol.",
 "key_points": [
  "Integration failures (mode confusion, automation surprise) cause accidents.",
  "Bainbridge ironies: automation creates supervisory roles humans perform worse.",
  "Fitts-style static allocation is folklore; dynamic allocation lacks a science.",
  "Levels-of-automation describes options without prescribing choices.",
 ],
 "requirements": [
  "Joint-cognitive designs preceding half-designs.",
  "Dynamic reallocation rules across workload states.",
  "Automation-surprise monitoring in deployment.",
 ],
 "citations": [
  "Bainbridge L (1983) Ironies of automation. Automatica 19(6).",
  "Hollnagel E, Woods DD (2005) Joint Cognitive Systems. CRC Press.",
 ],
 "demo": {"lam": 7.0, "mu": 9.0},
},
]
