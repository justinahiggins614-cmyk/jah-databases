#!/usr/bin/env python3
"""PHASE M — crash-data-databases-signature (Signature Edition) seed entries.

Original Signature creations: his own crash causal-analysis frameworks,
investigation methods, and safety-design doctrines. src="signature".
Tuple: (key, group, title, desc, points, req, standards, citations, demo_kind, verification)
"""

ENTRIES = [
("sig-five-layer-causal", "causal-analysis-frameworks",
 "The Signature Five-Layer Causal Stack",
 "The Signature Five-Layer Causal Stack is an original Signature method for "
 "organizing crash causation: every occurrence is decomposed into five layers — "
 "trigger event, system state, human action, organizational condition, and "
 "regulatory environment. Each layer is documented independently before any "
 "cross-layer linkage is drawn, which prevents the common error of stopping at "
 "the first plausible cause. The stack produces a layered causal map in which "
 "every safety recommendation is anchored to the specific layer it addresses.",
 ("Layer 1: trigger event — the initiating occurrence",
  "Layer 2: system state — the condition of vehicle, infrastructure, and environment",
  "Layer 3: human action — decisions and performance under actual conditions",
  "Layer 4: organizational condition — maintenance, training, and safety culture",
  "Layer 5: regulatory environment — standards, oversight, and enforcement",
  "Rule: document each layer independently before drawing cross-layer links",
  "Output: a layered causal map with recommendations anchored per layer"),
 "A complete framework record requires: the five layer definitions; documentation templates per layer; "
 "the independence rule; linkage method; recommendation-anchoring rule; worked method description; source note.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: maps to ICAO Annex 13 investigation phases"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-occurrence-reconstruction", "causal-analysis-frameworks",
 "Signature Occurrence Reconstruction Method",
 "The Signature Occurrence Reconstruction Method is an original Signature "
 "procedure for rebuilding a crash sequence from fragmentary evidence: it "
 "separates established facts, inferred facts, and unknowns into three "
 "explicit columns, and no inference is promoted to fact without a cited "
 "evidence link. The method assigns each timeline entry a confidence grade, "
 "so the reconstruction honestly shows where the record is thin. It is "
 "designed for investigators and analysts who must reason rigorously from "
 "incomplete data without overstating what is known.",
 ("Three columns: established facts, inferred facts, unknowns",
  "Every inference carries an explicit evidence link",
  "Confidence grades on each timeline entry",
  "Unknowns are documented, never papered over",
  "Designed for fragmentary-evidence reasoning",
  "Output: a graded, honest reconstruction timeline"),
 "A complete framework record requires: the three-column schema; confidence-grade definitions; "
 "inference-promotion rules; timeline assembly procedure; honesty safeguards; worked method description.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: supports NTSB-style factual-report structure"),
 "Original Signature creation — Signature system (Signature Edition).",
 "timeline", None),

("sig-failure-path-atlas", "causal-analysis-frameworks",
 "The Signature Failure-Path Atlas",
 "The Signature Failure-Path Atlas is an original Signature technique for "
 "mapping every path by which a system can reach a crash state: starting from "
 "the crash state, analysts work backward through each protective barrier that "
 "failed or was absent, producing a branching atlas of failure paths. Each "
 "path is scored for how many barriers stood between normal operation and the "
 "crash — the barrier count becomes the system's measured safety depth. The "
 "atlas makes 'single-point failure' claims testable: a true single-point "
 "failure shows exactly one barrier on every path.",
 ("Backward mapping from the crash state through failed or absent barriers",
  "Barrier count per path = measured safety depth",
  "Single-point-failure claims become testable",
  "Branching atlas shows alternative paths to the same outcome",
  "Each barrier annotated: designed, degraded, defeated, or absent",
  "Output: a scored atlas of all failure paths"),
 "A complete framework record requires: backward-mapping procedure; barrier taxonomy; "
 "safety-depth scoring rule; single-point test; annotation schema; worked method description.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: aligns with system-safety barrier analysis"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-human-factors-integration", "causal-analysis-frameworks",
 "Signature Human-Factors Integration Model",
 "The Signature Human-Factors Integration Model is an original Signature "
 "framework that treats human performance as a designed system component rather "
 "than a residual cause: for every human action in a crash sequence, the model "
 "requires documenting the information available, the time available, the "
 "workload, and the training for that exact situation. A human 'error' is only "
 "recorded after these four conditions are scored — the model routinely shows "
 "that the same action was the predictable product of the conditions. It "
 "redirects recommendations from retraining individuals to redesigning "
 "conditions.",
 ("Four scored conditions: information, time, workload, training-for-the-situation",
  "Human error recorded only after conditions are scored",
  "Predictable-action test: would the conditions produce this action in most operators?",
  "Redirects fixes from individuals to conditions",
  "Applies to pilots, drivers, controllers, and maintainers alike",
  "Output: a scored human-performance profile per critical action"),
 "A complete framework record requires: the four condition definitions; scoring scales; "
 "the predictable-action test; redirection rule; application notes per operator role.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: consistent with modern human-factors investigation practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-energy-exchange", "causal-analysis-frameworks",
 "The Signature Energy-Exchange Crash Model",
 "The Signature Energy-Exchange Crash Model is an original Signature physics "
 "framework for crash analysis: every crash is modeled as an uncontrolled "
 "exchange of kinetic energy between bodies, and survivability is modeled as "
 "the management of deceleration over distance and time. The model defines the "
 "survivable envelope for occupants in terms of energy to be absorbed, crush "
 "distance available, and restraint coupling — which explains in one framework "
 "why speed, mass mismatch, and restraint use dominate real-world outcomes. It "
 "gives analysts a common language spanning aviation, road, and rail crashes.",
 ("Crash modeled as uncontrolled kinetic-energy exchange",
  "Survivability modeled as deceleration managed over distance and time",
  "Three variables: energy to absorb, crush distance, restraint coupling",
  "Explains speed, mass mismatch, and restraint effects in one framework",
  "Common language across aviation, road, and rail analysis",
  "Output: an energy budget and survivability assessment per crash"),
 "A complete framework record requires: the energy-exchange formulation; the three-variable "
 "survivability model; worked reasoning examples per transport mode; limits of the model.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: consistent with crashworthiness engineering principles"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-maintenance-drift", "causal-analysis-frameworks",
 "Signature Maintenance-Drift Detection Framework",
 "The Signature Maintenance-Drift Detection Framework is an original Signature "
 "method for finding the slow degradation of maintenance quality that precedes "
 "many crashes: it tracks leading indicators — deferred items, interval "
 "extensions, repeat discrepancies, and audit findings — as a drift index over "
 "time, rather than judging any single maintenance action. When the drift index "
 "crosses its threshold, the framework triggers a deep review before a failure "
 "occurs. It converts maintenance oversight from reactive finding-fixing into "
 "trend-based prevention.",
 ("Leading indicators: deferrals, interval extensions, repeat discrepancies, audit findings",
  "Drift index tracked over time — trends, not single events",
  "Threshold crossing triggers deep review before failure",
  "Converts oversight from reactive to trend-based",
  "Applies to fleets, workshops, and infrastructure maintainers",
  "Output: a drift index with review thresholds"),
 "A complete framework record requires: indicator definitions; drift-index construction; "
 "threshold-setting method; review trigger procedure; worked trend description.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: supports reliability-centered maintenance programs"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-checklist-discipline", "causal-analysis-frameworks",
 "The Signature Checklist-Discipline Protocol",
 "The Signature Checklist-Discipline Protocol is an original Signature "
 "operational method for making checklists actually work: it distinguishes "
 "read-and-do, challenge-and-response, and flow-then-verify patterns and assigns "
 "each procedure the pattern that fits its risk; it requires that any skipped "
 "or deferred item be explicitly logged with a reason; and it mandates "
 "periodic observed-compliance audits. The protocol treats checklist "
 "non-compliance as a system signal — evidence about workload, design, or "
 "culture — rather than merely a personnel failure.",
 ("Three patterns: read-and-do, challenge-and-response, flow-then-verify",
  "Skipped items logged explicitly with reasons",
  "Observed-compliance audits on a schedule",
  "Non-compliance treated as a system signal",
  "Pattern assigned by risk, not by habit",
  "Output: a checklist system with measured compliance"),
 "A complete framework record requires: pattern definitions and selection rules; "
 "skip-logging procedure; audit method; signal-interpretation guidance.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: consistent with crew resource management principles"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-weather-decision-matrix", "causal-analysis-frameworks",
 "Signature Weather-Encounter Decision Matrix",
 "The Signature Weather-Encounter Decision Matrix is an original Signature "
 "decision tool for operators facing hazardous weather: it scores the weather "
 "threat, the escape options, the cost of delay or diversion, and the pressure "
 "to continue — and requires the decision to be logged before entering the "
 "threat area. By making the continuation pressure explicit and scorable, the "
 "matrix counteracts plan-continuation bias, the documented tendency to press "
 "on into deteriorating conditions. It applies to pilots approaching storms, "
 "drivers in severe weather, and mariners facing heavy seas.",
 ("Four scored inputs: threat, escape options, cost of delay, pressure to continue",
  "Decision logged before entering the threat area",
  "Makes continuation pressure explicit and scorable",
  "Counteracts plan-continuation bias",
  "Applies across aviation, road, and maritime operations",
  "Output: a scored go/divert/delay decision with rationale"),
 "A complete framework record requires: the four input definitions; scoring scales; "
 "logging procedure; bias-counteraction rationale; application notes per domain.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: supports threat-and-error management"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-redundancy-depth", "causal-analysis-frameworks",
 "The Signature Redundancy Depth Scale",
 "The Signature Redundancy Depth Scale is an original Signature measurement "
 "for how many independent protections stand between normal operation and a "
 "crash: depth 0 means a single failure causes the crash; each additional "
 "independent barrier adds a level. The scale distinguishes true independence "
 "(different failure modes, different maintenance, different operators) from "
 "decorative redundancy (backups sharing the same failure mode). Crash "
 "investigations using the scale routinely find claimed depth 3 systems that "
 "measure depth 1 — which is where the real recommendation belongs.",
 ("Depth 0: single failure reaches the crash state",
  "True independence requires different failure modes, maintenance, and operators",
  "Decorative redundancy: backups sharing one failure mode",
  "Measured depth often lower than claimed depth",
  "Each level must be independently verifiable",
  "Output: a measured redundancy depth for the system"),
 "A complete framework record requires: depth-level definitions; independence criteria; "
 "decorative-redundancy tests; measurement procedure; worked assessment description.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: aligns with fault-tolerance engineering"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-learning-loop", "causal-analysis-frameworks",
 "Signature Post-Occurrence Learning Loop",
 "The Signature Post-Occurrence Learning Loop is an original Signature "
 "organizational method for ensuring crashes actually change systems: every "
 "recommendation is registered with an owner, a deadline, and a verification "
 "method; implementation is tracked to closure; and effectiveness is reviewed "
 "after a defined interval by checking whether the targeted failure path has "
 "recurred. Recommendations without owners, deadlines, or verification are "
 "classified as open by definition. The loop closes the gap between "
 "investigation reports and real-world change.",
 ("Every recommendation: owner, deadline, verification method",
  "Tracked to closure — no silent expiration",
  "Effectiveness review: has the failure path recurred?",
  "Ownerless recommendations classified as open by definition",
  "Periodic portfolio review of all open items",
  "Output: a living recommendation register with closure evidence"),
 "A complete framework record requires: registration schema; tracking procedure; "
 "verification methods; effectiveness-review protocol; portfolio review cadence.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: supports safety-management-system assurance"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-normalization-deviance", "causal-analysis-frameworks",
 "Signature Normalization-of-Deviance Detector",
 "The Signature Normalization-of-Deviance Detector is an original Signature "
 "method for catching the drift in which rule-bending becomes routine: it "
 "samples actual practice against written procedure on a schedule, scores the "
 "gap, and traces each gap to its incentive — schedule pressure, convenience, "
 "or design friction. Gaps with strong incentives are flagged as systemic "
 "rather than individual. The detector is aimed at the exact pattern that "
 "preceded several landmark crashes: everyone knew the shortcut, nobody wrote "
 "it down, and the system learned to depend on it.",
 ("Scheduled sampling of actual practice versus written procedure",
  "Each gap traced to its incentive: pressure, convenience, or friction",
  "Incentive-backed gaps flagged as systemic",
  "Targets the 'everyone knew the shortcut' pattern",
  "Findings feed redesign, not punishment",
  "Output: a scored practice-procedure gap register"),
 "A complete framework record requires: sampling method; gap-scoring scale; incentive taxonomy; "
 "systemic-flagging rule; remediation routing.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: consistent with safety-culture assessment practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-evidence-triage", "causal-analysis-frameworks",
 "Signature Evidence Triage Protocol",
 "The Signature Evidence Triage Protocol is an original Signature procedure for "
 "the first hours after a crash: it prioritizes perishable evidence — "
 "recordings, witness memory, environmental conditions, system states — ahead "
 "of durable evidence, and assigns each evidence class a custodian and a "
 "collection deadline measured in hours. The protocol prevents the common loss "
 "in which the most time-sensitive evidence degrades while attention goes to "
 "the obvious wreckage. It includes a chain-of-custody log from the first "
 "contact with every item.",
 ("Perishable evidence first: recordings, memory, conditions, system states",
  "Each evidence class: a custodian and an hour-scale deadline",
  "Chain-of-custody log from first contact",
  "Prevents time-sensitive evidence loss",
  "Scales from single-vehicle crashes to major occurrences",
  "Output: a triaged, custodied evidence set"),
 "A complete framework record requires: evidence perishability classes; custodian assignment; "
 "deadline schedule; custody-log schema; scale-up procedure.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: supports ICAO Annex 13 evidence-protection duties"),
 "Original Signature creation — Signature system (Signature Edition).",
 "timeline", None),

("sig-survivability-audit", "causal-analysis-frameworks",
 "Signature Survivability Audit",
 "The Signature Survivability Audit is an original Signature method that "
 "separates crash prevention from crash survival in every investigation: even "
 "when the cause is clear, the audit asks what determined who lived — "
 "restraint use, seating position, evacuation paths, fire behavior, rescue "
 "timing — and scores each factor's contribution. The audit routinely finds "
 "survivability improvements that are independent of the cause, which means "
 "every crash teaches two lessons: how to prevent it and how to survive it. "
 "It keeps investigations from stopping at causation.",
 ("Separates prevention analysis from survival analysis",
  "Factors scored: restraints, seating, evacuation, fire, rescue timing",
  "Finds cause-independent survivability improvements",
  "Every crash teaches two lessons: prevent and survive",
  "Applies to any transport mode",
  "Output: a scored survivability factor profile"),
 "A complete framework record requires: survivability factor taxonomy; scoring method; "
 "cause-independence rule; dual-lesson reporting format.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: consistent with crashworthiness investigation practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-interface-mismatch", "causal-analysis-frameworks",
 "Signature Interface-Mismatch Analysis",
 "The Signature Interface-Mismatch Analysis is an original Signature method for "
 "crashes at system boundaries — where automation meets operator, where one "
 "organization's equipment meets another's procedures, where old infrastructure "
 "meets new vehicles. The method maps each interface, documents what each side "
 "assumes about the other, and flags untested assumptions. Many landmark "
 "crashes resolve, under this analysis, into an assumption one side never knew "
 "the other was making. The fix is always to make the assumption explicit and "
 "testable.",
 ("Maps every interface in the occurrence",
  "Documents each side's assumptions about the other",
  "Flags untested assumptions as prime suspects",
  "Assumption failures explain many boundary crashes",
  "Fix rule: make the assumption explicit and testable",
  "Output: an assumption register with test status"),
 "A complete framework record requires: interface-mapping procedure; assumption-elicitation method; "
 "test-status schema; fix rule; worked boundary-crash reasoning.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: aligns with systems-theoretic accident analysis"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-recurrence-pattern", "causal-analysis-frameworks",
 "Signature Recurrence-Pattern Miner",
 "The Signature Recurrence-Pattern Miner is an original Signature analytical "
 "method for finding the crash that has happened before: it encodes each "
 "occurrence as a pattern of trigger, system state, human action, and "
 "organizational condition, then searches the archive for prior occurrences "
 "with matching patterns. When a match is found, the method pulls the prior "
 "recommendations and checks their implementation status — the most damning "
 "and most useful finding in investigation is 'we recommended this before.' "
 "It makes organizational memory searchable and accountable.",
 ("Occurrences encoded as trigger-state-action-condition patterns",
  "Archive searched for matching prior patterns",
  "Prior recommendations pulled and implementation-checked",
  "'We recommended this before' made systematic",
  "Organizational memory becomes searchable",
  "Output: prior-pattern matches with recommendation status"),
 "A complete framework record requires: pattern-encoding schema; matching method; "
 "recommendation linkage; implementation-check procedure; accountability reporting.",
 ("Signature causal-analysis canon — original Signature method",
  "Compatibility: supports safety-management-system hazard tracking"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

# ---------------- safety-design frameworks (15) ----------------
("sig-crumple-doctrine", "safety-design-frameworks",
 "Signature Vehicle Crumple-Zone Design Doctrine",
 "The Signature Vehicle Crumple-Zone Design Doctrine is an original Signature "
 "engineering doctrine for crash energy management in road vehicles: the "
 "vehicle's front and rear structures are sacrificial energy absorbers with a "
 "defined crush-force profile, while the occupant cell is a rigid survival "
 "space that must not intrude. The doctrine specifies the stiffness gradient — "
 "soft nose, progressively stiffer rails, rigid cell — and requires that the "
 "restraint system be tuned to the same crash pulse the structure produces. "
 "Structure and restraints are designed as one system, never separately.",
 ("Sacrificial crush zones with defined force profiles",
  "Rigid occupant cell — no intrusion permitted",
  "Stiffness gradient: soft nose to rigid cell",
  "Restraints tuned to the structure's crash pulse",
  "Structure and restraints designed as one system",
  "Doctrine output: a matched structure-restraint design"),
 "A complete doctrine record requires: crush-force profile specification; cell rigidity criteria; "
 "gradient design rules; restraint-tuning procedure; validation method.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with crashworthiness engineering"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-occupant-envelope", "safety-design-frameworks",
 "The Signature Occupant-Protection Envelope",
 "The Signature Occupant-Protection Envelope is an original Signature design "
 "framework defining the complete protection around each occupant: restraints "
 "that couple the occupant to the vehicle's deceleration, interior surfaces "
 "that manage contact, and post-crash provisions for evacuation and rescue. "
 "The envelope is specified as a performance budget — maximum occupant "
 "deceleration, maximum intrusion, minimum survival space — rather than as a "
 "parts list, so any technology meeting the budget qualifies. It applies the "
 "same envelope logic to cars, buses, trains, and aircraft cabins.",
 ("Performance budget, not a parts list",
  "Three elements: coupling restraints, managed contact surfaces, post-crash provisions",
  "Budget terms: max deceleration, max intrusion, minimum survival space",
  "Any technology meeting the budget qualifies",
  "One envelope logic across cars, buses, trains, aircraft",
  "Output: a specified protection envelope per seating position"),
 "A complete framework record requires: budget parameter definitions; the three element specifications; "
 "measurement methods; cross-mode application notes.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with occupant-protection standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-active-safety-ladder", "safety-design-frameworks",
 "Signature Active-Safety Priority Ladder",
 "The Signature Active-Safety Priority Ladder is an original Signature "
 "framework that ranks crash-avoidance technologies by the crash energy they "
 "remove: at the top are systems that prevent the crash entirely, then systems "
 "that reduce speed before impact, then systems that optimize the impact "
 "configuration, and finally systems that only warn. Investment and regulation "
 "should climb the ladder from the top — a warning that arrives too late to "
 "act on is the bottom rung. The ladder gives policymakers and designers a "
 "principled order for adopting assistance technologies.",
 ("Rung 1: prevent the crash entirely",
  "Rung 2: reduce speed before impact",
  "Rung 3: optimize the impact configuration",
  "Rung 4: warn (lowest — only if actionable in time)",
  "Climb from the top in investment and regulation",
  "Output: a ranked adoption order for assistance technologies"),
 "A complete framework record requires: rung definitions; energy-removed metric; "
 "ranking procedure; policy-application guidance.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with crash-avoidance research"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-roadway-forgiveness", "safety-design-frameworks",
 "The Signature Roadway Forgiveness Standard",
 "The Signature Roadway Forgiveness Standard is an original Signature "
 "infrastructure doctrine: roads should be designed so that ordinary driver "
 "errors do not become fatal crashes. The standard specifies clear zones free "
 "of rigid hazards, barrier protection where hazards cannot be removed, "
 "median separation on high-speed roads, and intersection designs that manage "
 "conflict energy. It inverts the traditional assignment of blame — the road "
 "is the engineered system, the driver is the known-fallible component — and "
 "measures every design by the errors it forgives.",
 ("Clear zones free of rigid roadside hazards",
  "Barriers where hazards cannot be removed",
  "Median separation on high-speed roads",
  "Intersection designs that manage conflict energy",
  "The road is engineered; the driver is known-fallible",
  "Output: a forgiveness-scored road design"),
 "A complete framework record requires: forgiveness criteria per road element; "
 "hazard-removal hierarchy; scoring method; retrofit prioritization.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with Safe System road-design principles"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-driver-attention-arch", "safety-design-frameworks",
 "Signature Driver-Attention Architecture",
 "The Signature Driver-Attention Architecture is an original Signature design "
 "framework for vehicles with partial automation: it defines the driver's "
 "role explicitly for every automation state, requires the system to monitor "
 "whether the driver is fulfilling that role, and mandates a graduated "
 "escalation — reminder, warning, controlled slowdown — when attention lapses. "
 "The architecture forbids the 'attentive passenger' fiction: if the system "
 "needs the driver, the system must verify the driver. It was formulated as "
 "the direct design answer to automation-overreliance crashes.",
 ("Driver role defined explicitly per automation state",
  "System must monitor role fulfillment",
  "Graduated escalation: reminder, warning, controlled slowdown",
  "Forbids the 'attentive passenger' fiction",
  "Direct design answer to automation-overreliance crashes",
  "Output: a specified attention-management design"),
 "A complete framework record requires: role-definition schema; monitoring requirements; "
 "escalation design; verification methods; state-transition rules.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with driver-monitoring research"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-cockpit-gradient", "safety-design-frameworks",
 "Signature Cockpit Authority Gradient",
 "The Signature Cockpit Authority Gradient is an original Signature crew "
 "coordination doctrine: it defines how authority flows in the cockpit so that "
 "the pilot flying can be challenged without undermining command — a "
 "structured gradient from inquiry to advocacy to intervention, with explicit "
 "trigger phrases at each level. The doctrine requires that every crew member "
 "be trained and assessed on upward communication, and that captains be "
 "assessed on receiving it. It operationalizes crew resource management into "
 "practiced, graded behaviors rather than slogans.",
 ("Graded challenge: inquiry, advocacy, intervention",
  "Explicit trigger phrases at each level",
  "All crew assessed on upward communication",
  "Captains assessed on receiving challenge",
  "CRM operationalized as practiced behavior",
  "Output: a trained and assessed coordination doctrine"),
 "A complete framework record requires: gradient-level definitions; trigger-phrase sets; "
 "training syllabus; assessment criteria for givers and receivers.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with crew resource management standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),

("sig-maintenance-access", "safety-design-frameworks",
 "Signature Maintainability-by-Design Standard",
 "The Signature Maintainability-by-Design Standard is an original Signature "
 "engineering doctrine: safety-critical components must be inspectable, "
 "measurable, and replaceable without heroic effort — because maintenance "
 "that is difficult will eventually be deferred, and deferred maintenance has "
 "caused crashes. The standard requires inspection access designed in from "
 "the start, wear measurable with standard tools, and replacement procedures "
 "validated by technicians before certification. It treats the maintainer as a "
 "design stakeholder equal to the operator.",
 ("Safety-critical parts: inspectable, measurable, replaceable",
  "Difficult maintenance will be deferred — design against it",
  "Inspection access designed in from the start",
  "Wear measurable with standard tools",
  "Replacement validated by technicians before certification",
  "Output: a maintainability-scored design"),
 "A complete framework record requires: inspectability criteria; measurement standards; "
 "access design rules; technician-validation procedure; scoring method.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with reliability-centered maintenance"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-warning-hierarchy", "safety-design-frameworks",
 "Signature Warning Hierarchy",
 "The Signature Warning Hierarchy is an original Signature human-interface "
 "doctrine for safety alerts: warnings are ranked by required response time — "
 "immediate action, prompt action, awareness — and each rank has a mandated "
 "modality, persistence, and silence-ability. The hierarchy forbids "
 "same-sounding alerts for different urgencies and requires that the highest "
 "rank cannot be silenced without resolving the condition. It addresses the "
 "documented pattern in which crews missed or mis-prioritized warnings among "
 "alert clutter.",
 ("Three ranks: immediate action, prompt action, awareness",
  "Each rank: mandated modality, persistence, silence rules",
  "No same-sounding alerts across urgencies",
  "Highest rank cannot be silenced without resolving the condition",
  "Addresses alert-clutter mis-prioritization",
  "Output: a ranked, specified alert design"),
 "A complete framework record requires: rank definitions; modality specifications; "
 "persistence and silencing rules; clutter-audit procedure.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with alerting-system human-factors guidance"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-evacuation-design", "safety-design-frameworks",
 "Signature Evacuation Design Doctrine",
 "The Signature Evacuation Design Doctrine is an original Signature framework "
 "for getting everyone out: it specifies evacuation as a timed performance "
 "requirement — full occupant egress within the demonstrated survivability "
 "window — and designs exits, lighting, signage, and crew procedures backward "
 "from that time. The doctrine requires evacuation demonstration under "
 "realistic degraded conditions (darkness, blocked exits, smoke) rather than "
 "ideal ones, and treats carry-on retrieval behavior as a design input to be "
 "managed, not merely a passenger failing to be scolded.",
 ("Evacuation as a timed performance requirement",
  "Designed backward from the survivability window",
  "Demonstrated in degraded conditions: dark, blocked exits, smoke",
  "Carry-on retrieval treated as a design input",
  "Exits, lighting, signage, procedures as one system",
  "Output: a demonstrated evacuation-time budget"),
 "A complete framework record requires: time-budget method; degraded-condition test matrix; "
 "behavioral design inputs; demonstration protocol.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with emergency-evacuation certification practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "timeline", None),

("sig-fire-containment", "safety-design-frameworks",
 "Signature Fire Containment Doctrine",
 "The Signature Fire Containment Doctrine is an original Signature framework "
 "for post-crash and in-flight fire: it layers prevention (eliminate ignition "
 "sources), detection (earliest reliable sensing), suppression (automatic "
 "where crew cannot reach), and containment (materials and barriers that buy "
 "evacuation time). Each layer is specified with a time budget — how many "
 "minutes of tenability it must provide — because fire safety is measured in "
 "time, not in equipment lists. The doctrine applies to aircraft cabins, "
 "vehicle interiors, and buildings alike.",
 ("Four layers: prevention, detection, suppression, containment",
  "Each layer specified with a tenability time budget",
  "Fire safety measured in time, not equipment lists",
  "Automatic suppression where crew cannot reach",
  "Containment materials buy evacuation time",
  "Output: a time-budgeted fire-safety design"),
 "A complete framework record requires: layer definitions; time-budget method; "
 "detection and suppression specifications; material containment criteria.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with fire-protection engineering"),
 "Original Signature creation — Signature system (Signature Edition).",
 "stats", None),

("sig-rail-crashworthiness", "safety-design-frameworks",
 "Signature Rail Crashworthiness Doctrine",
 "The Signature Rail Crashworthiness Doctrine is an original Signature "
 "framework for train collision survival: it specifies crash energy management "
 "at the train level — pushback couplers, anti-climb features, and designated "
 "deformation zones in end cars — so that the passenger volumes preserve "
 "survival space. The doctrine addresses override, the deadly mechanism in "
 "which one car climbs over another, as the primary design enemy. It requires "
 "full-train collision simulation as part of certification, not just "
 "component testing.",
 ("Train-level crash energy management",
  "Anti-climb features defeat override — the primary design enemy",
  "Deformation zones in end cars; preserved survival space elsewhere",
  "Full-train collision simulation required",
  "Passenger volumes protected as survival spaces",
  "Output: a simulated and specified crashworthy train"),
 "A complete framework record requires: energy-management specification; anti-climb criteria; "
 "survival-space definitions; simulation requirements; validation method.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with rail crashworthiness standards"),
 "Original Signature creation — Signature system (Signature Edition).",
 "causetree", None),

("sig-maritime-damage-stability", "safety-design-frameworks",
 "Signature Maritime Damage-Stability Doctrine",
 "The Signature Maritime Damage-Stability Doctrine is an original Signature "
 "framework for ships that must survive hull breaches: it requires damage "
 "scenarios to be simulated across the operating envelope — including the "
 "actual loading condition, not just the design condition — and mandates that "
 "stability after damage be demonstrated for realistic breach sizes and "
 "locations. The doctrine treats watertight integrity as an operational "
 "discipline (doors, drills, loading) as much as a design property, because "
 "ships have been lost with adequate design but defeated discipline.",
 ("Damage scenarios simulated across the operating envelope",
  "Actual loading conditions, not just design conditions",
  "Demonstrated stability for realistic breach sizes and locations",
  "Watertight integrity as operational discipline",
  "Design plus discipline — both required",
  "Output: a demonstrated damage-stability case"),
 "A complete framework record requires: scenario-simulation method; loading-condition rules; "
 "demonstration criteria; operational-discipline checklist.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with SOLAS damage-stability requirements"),
 "Original Signature creation — Signature system (Signature Edition).",
 "investigation", None),

("sig-pipeline-integrity", "safety-design-frameworks",
 "Signature Pipeline Integrity Doctrine",
 "The Signature Pipeline Integrity Doctrine is an original Signature framework "
 "for preventing pipeline failures: it requires baseline assessment of every "
 "segment, threat-specific inspection intervals (corrosion, cracking, third-party "
 "damage, geohazards), and a maximum allowable operating pressure derived from "
 "the weakest credible condition — not the nameplate rating. The doctrine "
 "mandates that records be traceable, verifiable, and complete for every mile, "
 "because investigations have repeatedly found that missing records were the "
 "real failure. Integrity management is treated as a data discipline first.",
 ("Baseline assessment of every segment",
  "Threat-specific inspection intervals",
  "Operating pressure from the weakest credible condition",
  "Records traceable, verifiable, complete — every mile",
  "Integrity management as a data discipline first",
  "Output: a documented integrity case per segment"),
 "A complete framework record requires: assessment methods per threat; interval-setting rules; "
 "pressure-derivation method; records standard; verification procedure.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with pipeline integrity management regulations"),
 "Original Signature creation — Signature system (Signature Edition).",
 "reclog", None),

("sig-workplace-energy-isolation", "safety-design-frameworks",
 "Signature Workplace Energy-Isolation Doctrine",
 "The Signature Workplace Energy-Isolation Doctrine is an original Signature "
 "framework for industrial accident prevention: every hazardous energy source — "
 "electrical, mechanical, pressure, thermal, chemical, gravitational — must be "
 "identified, isolable, lockable, and verifiable at zero energy before work "
 "begins. The doctrine requires try-start verification (attempting to operate "
 "the equipment after lockout) and group-lockout procedures for multi-craft "
 "work. It treats 'the equipment was off' as a claim requiring proof, never "
 "an assumption.",
 ("All hazardous energy sources identified per task",
  "Isolation must be lockable and verifiable at zero energy",
  "Try-start verification required after lockout",
  "Group-lockout procedures for multi-craft work",
  "'Off' is a claim requiring proof, never an assumption",
  "Output: a verified energy-isolation plan per job"),
 "A complete framework record requires: energy-source taxonomy; isolation device standards; "
 "verification procedure; group-lockout rules; proof documentation.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with lockout/tagout practice"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),
("sig-vulnerable-road-user", "safety-design-frameworks",
 "Signature Vulnerable-Road-User Protection Doctrine",
 "The Signature Vulnerable-Road-User Protection Doctrine is an original "
 "Signature framework for protecting pedestrians, cyclists, and motorcyclists — "
 "the road users with no crash structure around them. The doctrine ranks "
 "protection measures by effectiveness: separation in space or time first, "
 "then speed reduction to survivable levels, then vehicle front-end design "
 "that manages impact, and finally detection systems. It sets the design rule "
 "that no street carrying vulnerable users should depend on driver perfection, "
 "and requires every road project to score its vulnerable-user protection "
 "explicitly before approval.",
 ("Separation in space or time — the top protection measure",
  "Speed reduction to survivable levels where separation is impossible",
  "Vehicle front-end design that manages pedestrian impact",
  "Detection systems as a supplement, never the plan",
  "No street depends on driver perfection",
  "Every project scores vulnerable-user protection before approval",
  "Output: a scored protection case per road project"),
 "A complete doctrine record requires: the protection hierarchy; separation design rules; "
 "survivable-speed criteria; front-end design guidance; project scoring method.",
 ("Signature safety-design canon — original Signature doctrine",
  "Compatibility: consistent with Safe System vulnerable-user principles"),
 "Original Signature creation — Signature system (Signature Edition).",
 "verify", None),
]
