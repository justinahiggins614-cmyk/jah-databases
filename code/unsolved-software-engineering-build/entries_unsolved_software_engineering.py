#!/usr/bin/env python3
"""Entries for The Unsolved Software Engineering Database (unsolved-software-engineering)
and its Signature half (unsolved-software-engineering-signature).

34 famous unsolved problems in software engineering, ladder-ordered by accessibility
(rank 1 = most approachable, rank 34 = most complex/compounded).
Public half: real, fact-checked problems. Signature half: the same 34
problems through the Signature lens, with Signature-generated proposed
solutions that are ALWAYS labeled as proposals, never established science.

Honesty rule (enforced in every record): never claim proof, never imply
peer acceptance, never present speculation as settled. Signature proposals
are labeled speculation for research discussion only - never engineering
advice, never a design recommendation; no correctness guarantees.
"""

LABEL = "Signature-generated proposed solution \u2014 not established science."

SIG_TAIL = ("Signature editions carry the Signature system's proposed "
            "solution approaches to famous unsolved problems. Every "
            "solution is labeled a Signature-generated proposal, never "
            "established science, never peer-accepted, never proof, never "
            "engineering advice.")

STD_COMMON = [
    "Problem statements verified against the published software-engineering literature; open status confirmed as of 2026.",
    "Signature solution sections are labeled proposals: they state assumptions, a reasoning path, a proposed mechanism, what would confirm or kill them, and what they do not claim.",
    "Signature proposals are labeled speculation for research discussion only - never engineering advice, never a design recommendation; no correctness guarantees appear.",
]

ENTRIES = [
# ------------------------------------------------------------------ rank 1
{
 "key": "bug-free-software",
 "name": "Bug-Free Software: The Correctness Dream",
 "group": "Correctness",
 "ladder_rank": 1, "ladder_tier": "foundations",
 "problem": "Software ships with bugs - can any realistic process produce truly bug-free software?",
 "description": "Bug-free software - the aspiration of zero-defect code - is achieved only in tiny verified kernels (seL4); but mainstream software ships with thousands of known bugs. Whether formal verification can scale to real systems is the open question.",
 "background": "The software crisis (1968 NATO) named the problem; formal verification (Hoare, Dijkstra) offered the theory; seL4 (2009) proved a kernel correct. As of 2026 verification is practical for small critical code only.",
 "why_it_matters": "Bug-free software would end crashes, breaches, and recalls: the correctness that computing promised.",
 "sig_pointer": "The Signature system's proposed approach scales verification to real systems, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that correctness scales through compositional verification: the verified components composed - with proofs carrying through. "
  "Assumptions: (1) composition preserves proof; (2) components are verifiable; (3) scale follows. "
  "Reasoning path: a composition model explains seL4's isolation and predicts verified systems. "
  "Proposed mechanism: 'compositionally-verified' software - proof-carrying components. "
  "What would confirm it: large verified systems in production. "
  "What would kill it: evidence that verification inherently doesn't scale. "
  "What this does not claim: it does not claim bug-free software exists, offers no engineering advice, and does not constitute a development recommendation."),
 "sig_lens": "The Signature lens reads verification as unscaled proof, and asks what composition would carry.",
 "how_it_works": "Researchers study correctness through seL4-style verification, compositional methods, and proof engineering.",
 "key_points": [
  "seL4 proved a kernel correct.",
  "Mainstream software ships with known bugs.",
  "Verification is practical for small code only.",
  "Composition is the scaling question.",
  "The software crisis named this in 1968.",
 ],
 "requirements": [
  "Compositional verification methods.",
  "Large verified systems in production.",
  "Proof engineering at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Klein G et al. seL4 verification. Various; 2009-2014.",
  "Hoare CAR. Axiomatic basis. Various; 1969-1978.",
  "Dijkstra EW. Correctness writings. Various; 1968-1976.",
  "Appel AW et al. Verification reviews. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("verified lines of code, seL4 (approx)", 10000.0),
               "b": ("lines in a modern OS, millions (approx)", 50.0), "bounds": (150.0, 250.0),
               "step1": "ten thousand verified lines against fifty million shipped - the proof's scale gap",
               "confirm": "large verified systems in production",
               "refute": "verification proves inherently unscalable"},
},
# ------------------------------------------------------------------ rank 2
{
 "key": "software-estimation",
 "name": "Software Estimation: The Scheduling Problem",
 "group": "Process",
 "ladder_rank": 2, "ladder_tier": "foundations",
 "problem": "Software projects overrun chronically - can estimation ever be accurate?",
 "description": "Software estimation - predicting cost and schedule - fails systematically: Brooks' Law, the planning fallacy, and Hofstadter's Law describe the chronic overrun. Agile improved adaptation but not prediction; estimation accuracy hasn't fundamentally improved.",
 "background": "Brooks (1975, The Mythical Man-Month) diagnosed the disease; COCOMO (Boehm, 1981) modeled costs; agile (2001) adapted instead of predicting. As of 2026 projects still overrun.",
 "why_it_matters": "Accurate estimation would make software plannable: the end of the death march.",
 "sig_pointer": "The Signature system's proposed approach makes estimation accurate, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that estimation needs reference-class data: the predictions calibrated on historical actuals - with uncertainty quantified. "
  "Assumptions: (1) historical data predicts; (2) calibration works; (3) uncertainty is honest. "
  "Reasoning path: a calibration model explains chronic overrun and predicts accurate estimates. "
  "Proposed mechanism: 'reference-calibrated' estimation - data-driven predictions. "
  "What would confirm it: calibrated estimates beating expert judgment. "
  "What would kill it: evidence that software is inherently unpredictable. "
  "What this does not claim: it does not claim accurate estimation exists, offers no engineering advice, and does not constitute a management recommendation."),
 "sig_lens": "The Signature lens reads estimation as uncalibrated optimism, and asks what data would calibrate.",
 "how_it_works": "Researchers study estimation through COCOMO successors, reference-class forecasting, and agile metrics.",
 "key_points": [
  "Projects overrun chronically.",
  "Brooks' Law describes the disease.",
  "Agile adapted instead of predicting.",
  "Estimation accuracy hasn't improved fundamentally.",
  "The planning fallacy is systematic.",
 ],
 "requirements": [
  "Reference-class calibration.",
  "Quantified uncertainty.",
  "Estimates beating expert judgment.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brooks FP. The Mythical Man-Month. Various; 1975-1995.",
  "Boehm BW. COCOMO. Various; 1981-2000.",
  "Flyvbjerg B et al. Reference-class forecasting. Various; 2006-2021.",
  "Jørgensen M et al. Estimation reviews. Various; 2007-2020.",
 ],
 "demo_data": {"a": ("software projects overrunning, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.6, 0.8),
               "step1": "seven in ten projects overrun - the chronic misprediction",
               "confirm": "calibrated estimates beat expert judgment",
               "refute": "software proves inherently unpredictable"},
},
# ------------------------------------------------------------------ rank 3
{
 "key": "technical-debt",
 "name": "Technical Debt: The Compounding Burden",
 "group": "Process",
 "ladder_rank": 3, "ladder_tier": "foundations",
 "problem": "Technical debt compounds - can it be measured, managed, and paid down systematically?",
 "description": "Technical debt - the future cost of expedient choices - is universally acknowledged but poorly measured: no standard metric exists; interest is unquantified; and organizations pay it down unsystematically.",
 "background": "Cunningham (1992) coined the metaphor; the field developed debt taxonomies; but measurement remains ad hoc. As of 2026 debt is managed by judgment, not science.",
 "why_it_matters": "Measured debt would make software maintainable: the accounting of code quality.",
 "sig_pointer": "The Signature system's proposed approach measures and manages technical debt scientifically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that debt needs measurement science: the principal and interest quantified - with paydown optimized. "
  "Assumptions: (1) debt is measurable; (2) interest is quantifiable; (3) optimization works. "
  "Reasoning path: a measurement model explains unsystematic paydown and predicts managed debt. "
  "Proposed mechanism: 'scientifically-measured' technical debt - quantified management. "
  "What would confirm it: measured debt guiding successful paydown. "
  "What would kill it: evidence that debt resists measurement. "
  "What this does not claim: it does not claim debt measurement exists, offers no engineering advice, and does not constitute a management recommendation."),
 "sig_lens": "The Signature lens reads debt as unmeasured metaphor, and asks what science would quantify.",
 "how_it_works": "Researchers study technical debt through measurement research, taxonomy development, and paydown studies.",
 "key_points": [
  "Technical debt is universally acknowledged.",
  "No standard metric exists.",
  "Interest is unquantified.",
  "Paydown is unsystematic.",
  "The metaphor dates to 1992.",
 ],
 "requirements": [
  "Standard debt metrics.",
  "Quantified interest.",
  "Optimized paydown proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Cunningham W. Technical debt metaphor. 1992.",
  "Kruchten P et al. Debt taxonomy. Various; 2012-2019.",
  "Avgeriou P et al. Debt reviews. Various; 2016-2021.",
  "Li Z et al. Debt measurement. Various; 2015-2020.",
 ],
 "demo_data": {"a": ("developers reporting debt as a major problem, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.7, 0.9),
               "step1": "four in five developers drowning in it - the unmeasured burden",
               "confirm": "measured debt guides successful paydown",
               "refute": "debt proves to resist measurement"},
},
# ------------------------------------------------------------------ rank 4
{
 "key": "concurrency",
 "name": "Concurrency: The Parallel Programming Problem",
 "group": "Correctness",
 "ladder_rank": 4, "ladder_tier": "foundations",
 "problem": "Multicore demands parallelism - but concurrent programming is error-prone. Can it be made safe and easy?",
 "description": "Concurrency - correct parallel programming - defeats most developers: race conditions, deadlocks, and non-determinism are hard to reason about. Rust's ownership, actors, and transactional memory each help; none solved it generally.",
 "background": "The free lunch ended (Sutter, 2005); multicore forced parallelism; Rust (2010s) made memory-safe concurrency mainstream. As of 2026 concurrency is safer but not easy.",
 "why_it_matters": "Easy concurrency would unlock multicore: the performance the hardware already offers.",
 "sig_pointer": "The Signature system's proposed approach makes concurrency safe and easy, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that concurrency needs safe-by-default models: the programming models where races are impossible - with performance preserved. "
  "Assumptions: (1) safe models exist; (2) they perform; (3) developers adopt. "
  "Reasoning path: a models approach explains persistent difficulty and predicts easy parallelism. "
  "Proposed mechanism: 'safe-by-default' concurrency - race-impossible models. "
  "What would confirm it: mainstream safe concurrent programming. "
  "What would kill it: evidence that concurrency is inherently hard. "
  "What this does not claim: it does not claim easy concurrency exists, offers no engineering advice, and does not constitute a language recommendation."),
 "sig_lens": "The Signature lens reads concurrency as unsafe-by-default, and asks what models would make safe.",
 "how_it_works": "Researchers study concurrency through Rust adoption, actor models, and transactional-memory research.",
 "key_points": [
  "Race conditions defeat most developers.",
  "The free lunch ended in 2005.",
  "Rust made memory-safe concurrency mainstream.",
  "Actors and STM help partially.",
  "Concurrency is safer but not easy.",
 ],
 "requirements": [
  "Safe-by-default concurrency models.",
  "Performance-preserving safety.",
  "Mainstream adoption.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Sutter H. The free lunch is over. 2005.",
  "Lee EA. The problem with threads. Various; 2006-2012.",
  "Rust language. Concurrency model. Various; 2010 onward.",
  "Harris T et al. Transactional memory. Various; 2005-2015.",
 ],
 "demo_data": {"a": ("developers comfortable with concurrency, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "one in five comfortable - the parallelism most can't program",
               "confirm": "mainstream safe concurrent programming",
               "refute": "concurrency proves inherently hard"},
},
# ------------------------------------------------------------------ rank 5
{
 "key": "requirements-engineering",
 "name": "Requirements: Knowing What to Build",
 "group": "Process",
 "ladder_rank": 5, "ladder_tier": "foundations",
 "problem": "Most software failures are requirements failures - can we ever know what to build before building it?",
 "description": "Requirements engineering - discovering what software should do - fails chronically: users don't know what they want; requirements change; and the cost of getting them wrong dominates project failure. Agile iterates; but the fundamental problem persists.",
 "background": "Requirements engineering (1970s-80s, Ross, Boehm) formalized the discipline; agile (2001) embraced change; but failure analyses still blame requirements. As of 2026 knowing-what-to-build is still the hardest part.",
 "why_it_matters": "Solved requirements would end the biggest cause of project failure: building the right thing.",
 "sig_pointer": "The Signature system's proposed approach discovers true requirements, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that requirements need discovery science: the methods that surface true needs - with change anticipated. "
  "Assumptions: (1) true needs are discoverable; (2) methods exist; (3) change is manageable. "
  "Reasoning path: a discovery model explains chronic failure and predicts correct requirements. "
  "Proposed mechanism: 'discovery-driven' requirements - surfaced true needs. "
  "What would confirm it: discovered requirements reducing failure rates. "
  "What would kill it: evidence that requirements are inherently unknowable. "
  "What this does not claim: it does not claim requirements discovery works, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads requirements as undiscovered needs, and asks what science would surface.",
 "how_it_works": "Researchers study requirements through discovery methods, failure analyses, and agile research.",
 "key_points": [
  "Most failures are requirements failures.",
  "Users don't know what they want.",
  "Requirements change constantly.",
  "Agile iterates but doesn't solve.",
  "Knowing-what-to-build is the hardest part.",
 ],
 "requirements": [
  "Discovery methods proven.",
  "Reduced failure rates.",
  "Change-anticipating processes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boehm BW et al. Requirements economics. Various; 1981-2001.",
  "Standish Group. CHAOS reports. Various; 1994-2020.",
  "Nuseibeh B et al. Requirements reviews. Various; 2000-2015.",
  "Zave P et al. Requirements research. Various; 1997-2010.",
 ],
 "demo_data": {"a": ("project failures blamed on requirements, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.5, 0.72),
               "step1": "three in five failures start here - the unknowable specification",
               "confirm": "discovered requirements reduce failure rates",
               "refute": "requirements prove inherently unknowable"},
},
# ------------------------------------------------------------------ rank 6
{
 "key": "software-testing",
 "name": "Testing: The Completeness Problem",
 "group": "Correctness",
 "ladder_rank": 6, "ladder_tier": "foundations",
 "problem": "Testing can't prove absence of bugs - can it ever be complete enough?",
 "description": "Software testing - the completeness problem: Dijkstra noted testing shows presence, not absence, of bugs. Coverage metrics, fuzzing, and property-based testing improve; but the question of 'enough testing' has no principled answer.",
 "background": "Testing theory (1970s-80s, Myers, Beizer) established the limits; coverage became standard; fuzzing (1990s-2010s) found real bugs. As of 2026 testing is better but still incomplete.",
 "why_it_matters": "Complete-enough testing would make releases trustworthy: the confidence to ship.",
 "sig_pointer": "The Signature system's proposed approach defines testing completeness, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that testing needs completeness criteria: the principled definitions of 'enough' - with risk-quantified coverage. "
  "Assumptions: (1) completeness is definable; (2) risk is quantifiable; (3) criteria are practical. "
  "Reasoning path: a criteria model explains the confidence gap and predicts trustworthy testing. "
  "Proposed mechanism: 'criteria-defined' testing completeness - principled enough. "
  "What would confirm it: completeness criteria adopted with fewer escapes. "
  "What would kill it: evidence that testing completeness is undefinable. "
  "What this does not claim: it does not claim complete testing exists, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads testing as undefined enough, and asks what criteria would complete.",
 "how_it_works": "Researchers study testing through coverage research, fuzzing advances, and risk-based methods.",
 "key_points": [
  "Testing shows presence, not absence, of bugs.",
  "Coverage metrics are imperfect proxies.",
  "Fuzzing finds real bugs at scale.",
  "No principled 'enough' exists.",
  "Testing is better but incomplete.",
 ],
 "requirements": [
  "Principled completeness criteria.",
  "Risk-quantified coverage.",
  "Adopted criteria with fewer escapes.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Dijkstra EW. Testing notes. Various; 1969-1972.",
  "Myers GJ. The Art of Software Testing. Various; 1979-2011.",
  "Zalewski M et al. Fuzzing. Various; 2014-2020.",
  "Orso A et al. Testing reviews. Various; 2014-2021.",
 ],
 "demo_data": {"a": ("production bugs escaping test suites, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "three in ten bugs escape - the incomplete net",
               "confirm": "completeness criteria adopted with fewer escapes",
               "refute": "testing completeness proves undefinable"},
},
# ------------------------------------------------------------------ rank 7
{
 "key": "legacy-modernization",
 "name": "Legacy Modernization: The Rewrite Trap",
 "group": "Process",
 "ladder_rank": 7, "ladder_tier": "foundations",
 "problem": "Legacy systems run the world but can't be rewritten safely - can modernization be systematic?",
 "description": "Legacy modernization - the rewrite trap: rewrites fail (Netscape); strangler patterns help; but no systematic method modernizes large legacy systems safely. Trillions of lines of COBOL still run banking.",
 "background": "Netscape's rewrite (1998-2000) was the cautionary tale; the strangler pattern (Fowler, 2004) offered a path; but large modernizations still fail. As of 2026 legacy runs the world.",
 "why_it_matters": "Systematic modernization would free the world's critical systems: the safe path off legacy.",
 "sig_pointer": "The Signature system's proposed approach systematizes legacy modernization, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that modernization needs systematic methods: the behavior-preserving transformations - with risk managed. "
  "Assumptions: (1) behavior is preservable; (2) transformation is systematic; (3) risk is manageable. "
  "Reasoning path: a transformation model explains rewrite failures and predicts safe modernization. "
  "Proposed mechanism: 'behavior-preserving' modernization - systematic transformation. "
  "What would confirm it: systematic modernizations succeeding at scale. "
  "What would kill it: evidence that legacy can't be systematically transformed. "
  "What this does not claim: it does not claim systematic modernization exists, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads legacy as untouchable risk, and asks what transformation would make safe.",
 "how_it_works": "Researchers study modernization through strangler-pattern research, transformation tools, and case studies.",
 "key_points": [
  "Netscape's rewrite was the cautionary tale.",
  "Trillions of COBOL lines run banking.",
  "The strangler pattern helps incrementally.",
  "No systematic method exists.",
  "Large modernizations still fail.",
 ],
 "requirements": [
  "Systematic transformation methods.",
  "Behavior preservation proven.",
  "Modernizations succeeding at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fowler M. Strangler pattern. 2004.",
  "Netscape rewrite history. Various; 1998-2000.",
  "Seacord RC et al. Modernization reviews. Various; 2003-2015.",
  "Comella-Dorda S et al. Legacy studies. Various; 2000-2010.",
 ],
 "demo_data": {"a": ("large rewrites failing, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.58, 0.8),
               "step1": "seven in ten large rewrites fail - the trap that keeps the world on COBOL",
               "confirm": "systematic modernizations succeed at scale",
               "refute": "legacy proves unable to be systematically transformed"},
},
# ------------------------------------------------------------------ rank 8
{
 "key": "dependency-security",
 "name": "Dependency Security: The Supply-Chain Problem",
 "group": "Security",
 "ladder_rank": 8, "ladder_tier": "foundations",
 "problem": "Software depends on thousands of packages - can the supply chain be secured?",
 "description": "Dependency security - the supply-chain problem: Log4Shell (2021), SolarWinds (2020), and npm incidents showed the fragility. SBOMs, signing, and vetting help; but the attack surface of transitive dependencies is vast.",
 "background": "Open-source dependencies exploded (2010s); major incidents (2020-2021) forced attention; SBOM mandates (US EO 14028) pushed transparency. As of 2026 the supply chain is mapped but not secured.",
 "why_it_matters": "Secured supply chains would end the breach-via-dependency: the trust in the transitive.",
 "sig_pointer": "The Signature system's proposed approach secures the software supply chain, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that supply chains need verifiable trust: the signed, vetted, minimal dependencies - with compromise detected. "
  "Assumptions: (1) trust is verifiable; (2) vetting scales; (3) detection works. "
  "Reasoning path: a trust model explains incident persistence and predicts secured chains. "
  "Proposed mechanism: 'verifiably-trusted' supply chains - signed minimal dependencies. "
  "What would confirm it: supply-chain attacks declining measurably. "
  "What would kill it: evidence that transitive trust is impossible. "
  "What this does not claim: it does not claim secured supply chains exist, offers no engineering advice, and does not constitute a security recommendation."),
 "sig_lens": "The Signature lens reads dependencies as unverified trust, and asks what verification would secure.",
 "how_it_works": "Researchers study supply-chain security through SBOM adoption, signing infrastructure, and incident analyses.",
 "key_points": [
  "Log4Shell and SolarWinds showed the fragility.",
  "Transitive dependencies are vast.",
  "SBOMs map but don't secure.",
  "Signing and vetting help partially.",
  "The attack surface is enormous.",
 ],
 "requirements": [
  "Verifiable dependency trust.",
  "Scaled vetting and signing.",
  "Measurably declining attacks.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Log4Shell incident. 2021.",
  "SolarWinds incident. 2020.",
  "US EO 14028 SBOM mandate. 2021.",
  "Ladisa P et al. Supply-chain reviews. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("dependencies in a typical app, hundreds (approx)", 10.0),
               "b": ("dependencies vetted, hundreds (approx)", 2.0), "bounds": (4.0, 6.5),
               "step1": "a thousand dependencies, two hundred vetted - the unverified transitive",
               "confirm": "supply-chain attacks decline measurably",
               "refute": "transitive trust proves impossible"},
},
# ------------------------------------------------------------------ rank 9
{
 "key": "api-design",
 "name": "API Design: The Interface Problem",
 "group": "Design",
 "ladder_rank": 9, "ladder_tier": "foundations",
 "problem": "APIs are forever - can interface design be made scientific rather than artful?",
 "description": "API design - the interface problem: bad APIs persist for decades because deprecation is painful and users depend on every quirk; but no science of API design exists, so interfaces are shaped by taste and experience. Usability studies offer partial guidance, versioning strategies evolved, yet the field remains craft - and every regretted method signature becomes a permanent tax on everyone who builds on it.",
 "background": "API usability research (2000s-2010s, Stylos, Myers) studied the problem; versioning strategies evolved; but design remains art. As of 2026 APIs are designed by taste.",
 "why_it_matters": "Scientific API design would make software composable: the interfaces that last.",
 "sig_pointer": "The Signature system's proposed approach makes API design scientific, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that API design needs usability science: the empirically-validated principles - with evolution managed. "
  "Assumptions: (1) principles are discoverable; (2) they validate; (3) evolution is manageable. "
  "Reasoning path: a science model explains craft-status and predicts designed interfaces. "
  "Proposed mechanism: 'scientifically-designed' APIs - empirically-validated interfaces. "
  "What would confirm it: validated principles producing better APIs. "
  "What would kill it: evidence that API design is irreducibly art. "
  "What this does not claim: it does not claim scientific API design exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads APIs as artful craft, and asks what science would design.",
 "how_it_works": "Researchers study API design through usability studies, evolution research, and principle validation.",
 "key_points": [
  "Bad APIs persist for decades.",
  "Deprecation is painful.",
  "No science of API design exists.",
  "Usability studies help partially.",
  "Design remains craft.",
 ],
 "requirements": [
  "Empirically-validated principles.",
  "Better APIs from principles.",
  "Managed evolution.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Stylos J et al. API usability. Various; 2006-2012.",
  "Myers BA et al. API research. Various; 2016-2020.",
  "Bloch J. API design. Various; 2006-2018.",
  "Henning M et al. Versioning. Various; 2007-2009.",
 ],
 "demo_data": {"a": ("APIs regretted by their designers, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.48, 0.72),
               "step1": "three in five APIs regretted - the forever interface designed by taste",
               "confirm": "validated principles produce better APIs",
               "refute": "API design proves irreducibly art"},
},
# ------------------------------------------------------------------ rank 10
{
 "key": "documentation",
 "name": "Documentation: The Knowledge Problem",
 "group": "Process",
 "ladder_rank": 10, "ladder_tier": "foundations",
 "problem": "Documentation rots - can software knowledge be kept alive automatically?",
 "description": "Documentation - the knowledge problem: docs rot as code changes, developers avoid writing them, and auto-generated references capture signatures without understanding. Knuth's literate programming proposed the ideal of code as literature, wikis and doc generators helped at the margins, yet documentation remains the first casualty of every deadline - and whether living documentation that stays accurate automatically is achievable is still open.",
 "background": "Literate programming (Knuth, 1980s) proposed the ideal; wikis and auto-docs helped; but rot persists. As of 2026 documentation is still the first casualty.",
 "why_it_matters": "Living documentation would preserve software knowledge: the memory that doesn't rot.",
 "sig_pointer": "The Signature system's proposed approach keeps documentation alive, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that documentation needs living generation: the docs derived from code and intent - with rot detected. "
  "Assumptions: (1) generation captures intent; (2) rot is detectable; (3) docs stay alive. "
  "Reasoning path: a generation model explains persistent rot and predicts living docs. "
  "Proposed mechanism: 'livingly-generated' documentation - rot-detected knowledge. "
  "What would confirm it: documentation staying accurate automatically. "
  "What would kill it: evidence that docs inherently rot. "
  "What this does not claim: it does not claim living docs exist, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads docs as rotting knowledge, and asks what generation would keep alive.",
 "how_it_works": "Researchers study documentation through generation research, rot detection, and knowledge-management studies.",
 "key_points": [
  "Documentation rots as code changes.",
  "Developers don't write docs.",
  "Auto-generated docs lack understanding.",
  "Literate programming proposed the ideal.",
  "Docs are the first casualty.",
 ],
 "requirements": [
  "Intent-capturing generation.",
  "Rot detection proven.",
  "Automatically-accurate docs.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Knuth DE. Literate programming. Various; 1984-1992.",
  "Forward A et al. Documentation surveys. Various; 2002-2010.",
  "Zhi J et al. Doc-rot research. Various; 2015-2020.",
  "Aghajani E et al. Documentation reviews. Various; 2019-2021.",
 ],
 "demo_data": {"a": ("codebases with up-to-date docs, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "one in five codebases documented - the rotting memory",
               "confirm": "documentation stays accurate automatically",
               "refute": "docs prove to inherently rot"},
},
# ------------------------------------------------------------------ rank 11
{
 "key": "code-review",
 "name": "Code Review: The Human Bottleneck",
 "group": "Process",
 "ladder_rank": 11, "ladder_tier": "foundations",
 "problem": "Code review catches bugs - but it's slow and inconsistent. Can review be made effective and scalable?",
 "description": "Code review - the human bottleneck: reviews catch real defects but consume expensive senior time, effectiveness varies wildly between reviewers and teams, and AI review assistants are only beginning to emerge. Fagan inspections formalized review in 1976, pull requests made it ubiquitous in the 2010s, yet review remains universal but uneven - and whether it can scale in quality without scaling in cost is the open question.",
 "background": "Fagan inspections (1976) formalized review; GitHub pull requests (2010s) made it ubiquitous; AI review assistants (2020s) are emerging. As of 2026 review is universal but uneven.",
 "why_it_matters": "Effective scalable review would make quality routine: the gate that doesn't bottleneck.",
 "sig_pointer": "The Signature system's proposed approach makes review effective and scalable, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that review needs effectiveness science: the practices that catch defects - with AI assistance proven. "
  "Assumptions: (1) effectiveness is measurable; (2) practices optimize; (3) AI helps. "
  "Reasoning path: an effectiveness model explains uneven review and predicts scalable quality. "
  "Proposed mechanism: 'effectiveness-optimized' code review - proven practices plus AI. "
  "What would confirm it: optimized reviews catching more with less time. "
  "What would kill it: evidence that review is inherently bottlenecked. "
  "What this does not claim: it does not claim optimized review exists, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads review as uneven gatekeeping, and asks what science would optimize.",
 "how_it_works": "Researchers study code review through effectiveness research, AI-assistant trials, and practice studies.",
 "key_points": [
  "Reviews catch defects but consume senior time.",
  "Effectiveness varies widely.",
  "Pull requests made review ubiquitous.",
  "AI reviewers are emerging.",
  "Review is universal but uneven.",
 ],
 "requirements": [
  "Measured effective practices.",
  "AI assistance proven.",
  "More defects caught with less time.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Fagan ME. Inspections. Various; 1976-1986.",
  "Bacchelli A et al. Modern review. Various; 2013-2020.",
  "Sadowski C et al. Google review. Various; 2018-2022.",
  "Tufano R et al. AI review. Various; 2021-2024.",
 ],
 "demo_data": {"a": ("defects caught by review, percent (approx)", 60.0),
               "b": ("percent scale", 100.0), "bounds": (0.48, 0.72),
               "step1": "three in five caught - the uneven gate",
               "confirm": "optimized reviews catch more with less time",
               "refute": "review proves inherently bottlenecked"},
},
# ------------------------------------------------------------------ rank 12
{
 "key": "debugging",
 "name": "Debugging: The Science That Isn't",
 "group": "Correctness",
 "ladder_rank": 12, "ladder_tier": "compounded",
 "problem": "Debugging consumes half of development time - can it become a science rather than an art?",
 "description": "Debugging - the unscientific half of programming: developers spend ~50% of time debugging; but debugging has no theory; tools (debuggers, profilers) help little with understanding. Automated debugging is emerging.",
 "background": "Debugging was recognized as the cost center early; delta debugging (Zeller, 2000s) automated narrowing; but the practice remains art. As of 2026 debugging is still the expensive half.",
 "why_it_matters": "Scientific debugging would halve development cost: the theory of finding faults.",
 "sig_pointer": "The Signature system's proposed approach makes debugging scientific, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that debugging needs fault theory: the systematic methods that locate causes - with automation proven. "
  "Assumptions: (1) fault location is systematic; (2) automation works; (3) time falls. "
  "Reasoning path: a theory model explains the cost center and predicts scientific debugging. "
  "Proposed mechanism: 'theoretically-grounded' debugging - systematic fault location. "
  "What would confirm it: debugging time measurably halved. "
  "What would kill it: evidence that debugging is inherently art. "
  "What this does not claim: it does not claim scientific debugging exists, offers no engineering advice, and does not constitute a tool recommendation."),
 "sig_lens": "The Signature lens reads debugging as atheoretical cost, and asks what theory would halve.",
 "how_it_works": "Researchers study debugging through fault-localization research, delta debugging, and practice studies.",
 "key_points": [
  "Debugging consumes ~50% of development time.",
  "No theory of debugging exists.",
  "Tools help little with understanding.",
  "Delta debugging automated narrowing.",
  "The practice remains art.",
 ],
 "requirements": [
  "Systematic fault-location methods.",
  "Automated debugging proven.",
  "Measurably halved debugging time.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Zeller A. Delta debugging. Various; 1999-2009.",
  "Eisenstadt M et al. Debugging psychology. Various; 1997-2005.",
  "Wong WE et al. Fault localization. Various; 2016-2021.",
  "Perscheid M et al. Debugging practice. Various; 2017-2022.",
 ],
 "demo_data": {"a": ("development time spent debugging, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.38, 0.62),
               "step1": "half of all development - the expensive art",
               "confirm": "debugging time measurably halved",
               "refute": "debugging proves inherently art"},
},
# ------------------------------------------------------------------ rank 13
{
 "key": "distributed-systems",
 "name": "Distributed Systems: The Fallacies",
 "group": "Systems",
 "ladder_rank": 13, "ladder_tier": "compounded",
 "problem": "Distributed systems fail in ways single machines don't - can they be made as reliable as local computation?",
 "description": "Distributed systems - the fallacies of distributed computing: networks partition, clocks skew, and partial failure is the norm. Consensus (Paxos, Raft), CRDTs, and formal methods help; but building correct distributed systems remains expert work.",
 "background": "The fallacies (Deutsch, 1990s) framed the problem; Paxos (Lamport, 1998) solved consensus; Raft (2014) made it understandable; Jepsen (2010s) exposed bugs. As of 2026 distributed correctness is still hard.",
 "why_it_matters": "Reliable distributed systems would make the cloud trustworthy: correctness at planetary scale.",
 "sig_pointer": "The Signature system's proposed approach makes distributed systems reliably correct, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that distributed correctness needs verified protocols: the consensus and replication with machine-checked proofs - with tooling for developers. "
  "Assumptions: (1) protocols are verifiable; (2) proofs compose; (3) tooling democratizes. "
  "Reasoning path: a verification model explains expert-only status and predicts reliable distribution. "
  "Proposed mechanism: 'verified-protocol' distributed systems - proven correctness. "
  "What would confirm it: verified distributed systems in production. "
  "What would kill it: evidence that distribution resists verification. "
  "What this does not claim: it does not claim verified distributed systems exist at scale, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads distribution as unverified complexity, and asks what proofs would make reliable.",
 "how_it_works": "Researchers study distributed systems through protocol verification, Jepsen testing, and CRDT research.",
 "key_points": [
  "Partial failure is the norm.",
  "Paxos and Raft solved consensus.",
  "Jepsen exposed real-world bugs.",
  "Correct systems remain expert work.",
  "The fallacies still apply.",
 ],
 "requirements": [
  "Machine-checked protocol proofs.",
  "Verified systems in production.",
  "Democratized tooling.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lamport L. Paxos. Various; 1998-2006.",
  "Ongaro D et al. Raft. Various; 2014-2015.",
  "Deutsch P. Fallacies. 1990s.",
  "Kingsbury K. Jepsen analyses. Various; 2013-2023.",
 ],
 "demo_data": {"a": ("distributed-systems bugs found by Jepsen (approx)", 50.0),
               "b": ("systems tested (approx)", 100.0), "bounds": (0.35, 0.65),
               "step1": "half the systems tested had bugs - the unverified planetary scale",
               "confirm": "verified distributed systems in production",
               "refute": "distribution proves to resist verification"},
},
# ------------------------------------------------------------------ rank 14
{
 "key": "software-architecture",
 "name": "Software Architecture: The Science of Structure",
 "group": "Design",
 "ladder_rank": 14, "ladder_tier": "compounded",
 "problem": "Architecture decisions shape everything - but architectural knowledge is tacit. Can architecture become a science?",
 "description": "Software architecture - the science of structure: decisions are made by experience; evaluation is ad hoc; and architectural erosion is inevitable. Whether architecture can be principled rather than intuitive is open.",
 "background": "Software architecture (1990s, Shaw, Garlan) became a discipline; evaluation methods (ATAM) were developed; but practice remains intuitive. As of 2026 architecture is still craft.",
 "why_it_matters": "Scientific architecture would make structure reliable: the engineering of the large.",
 "sig_pointer": "The Signature system's proposed approach makes architecture scientific, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that architecture needs decision science: the tradeoffs quantified - with erosion detected. "
  "Assumptions: (1) tradeoffs are quantifiable; (2) decisions are evaluable; (3) erosion is detectable. "
  "Reasoning path: a decision model explains craft-status and predicts scientific architecture. "
  "Proposed mechanism: 'decision-scientific' architecture - quantified tradeoffs. "
  "What would confirm it: quantified decisions producing better architectures. "
  "What would kill it: evidence that architecture is irreducibly intuitive. "
  "What this does not claim: it does not claim scientific architecture exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads architecture as intuitive craft, and asks what science would structure.",
 "how_it_works": "Researchers study architecture through decision research, erosion detection, and evaluation methods.",
 "key_points": [
  "Architecture decisions shape everything.",
  "Knowledge is tacit and experiential.",
  "Evaluation is ad hoc.",
  "Erosion is treated as inevitable.",
  "Practice remains craft.",
 ],
 "requirements": [
  "Quantified architectural tradeoffs.",
  "Erosion detection proven.",
  "Better architectures from decisions.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shaw M, Garlan D. Software Architecture. Various; 1996-2010.",
  "Kazman R et al. ATAM. Various; 2000-2012.",
  "Taylor RN et al. Architecture reviews. Various; 2009-2021.",
  "Schmerl B et al. Erosion research. Various; 2006-2016.",
 ],
 "demo_data": {"a": ("architectures eroding within 5 years, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.58, 0.8),
               "step1": "seven in ten erode - the structure that doesn't hold",
               "confirm": "quantified decisions produce better architectures",
               "refute": "architecture proves irreducibly intuitive"},
},
# ------------------------------------------------------------------ rank 15
{
 "key": "formal-methods-adoption",
 "name": "Formal Methods: The Adoption Problem",
 "group": "Correctness",
 "ladder_rank": 15, "ladder_tier": "compounded",
 "problem": "Formal methods work - but almost nobody uses them. What blocks adoption?",
 "description": "Formal methods - mathematically proven software - succeed where applied (seL4, CompCert, AWS); but adoption is tiny: the learning curve, cost, and cultural resistance block it. The methods work; the industry doesn't use them.",
 "background": "Formal methods (1960s-70s) proved their worth; industrial successes (2000s-2020s) accumulated; but mainstream adoption never came. As of 2026 the methods are proven and unused.",
 "why_it_matters": "Adopted formal methods would make critical software trustworthy: the proof the industry ignores.",
 "sig_pointer": "The Signature system's proposed approach drives formal-methods adoption, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that adoption needs usability: the methods integrated into developer workflows - with cost justified. "
  "Assumptions: (1) usability is achievable; (2) integration works; (3) cost-benefit convinces. "
  "Reasoning path: an adoption model explains proven-but-unused and predicts mainstream proof. "
  "Proposed mechanism: 'workflow-integrated' formal methods - usable verification. "
  "What would confirm it: formal methods in mainstream development. "
  "What would kill it: evidence that developers will never adopt proof. "
  "What this does not claim: it does not claim mainstream adoption exists, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads formal methods as proven-but-unused, and asks what usability would adopt.",
 "how_it_works": "Researchers study adoption through usability research, industrial case studies, and cost-benefit analyses.",
 "key_points": [
  "Formal methods succeed where applied.",
  "Adoption is tiny.",
  "Learning curve and cost block it.",
  "Industrial successes accumulated.",
  "The methods are proven and unused.",
 ],
 "requirements": [
  "Workflow-integrated methods.",
  "Mainstream developer adoption.",
  "Justified cost-benefit.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Leroy X et al. CompCert. Various; 2006-2021.",
  "Newcombe C et al. AWS TLA+. Various; 2015-2020.",
  "Woodcock J et al. Adoption surveys. Various; 2009-2019.",
  "Bjørner D et al. Methods reviews. Various; 2014-2020.",
 ],
 "demo_data": {"a": ("developers using formal methods, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty uses them - the proven method the industry ignores",
               "confirm": "formal methods in mainstream development",
               "refute": "developers prove never to adopt proof"},
},
# ------------------------------------------------------------------ rank 16
{
 "key": "ai-code",
 "name": "AI-Generated Code: The Correctness Question",
 "group": "AI",
 "ladder_rank": 16, "ladder_tier": "compounded",
 "problem": "AI writes code - but is it correct, secure, and maintainable? Can AI-generated code be trusted?",
 "description": "AI-generated code - Copilot, ChatGPT, agents - writes substantial code; but correctness is unverified; security vulnerabilities appear; and the maintenance burden is unknown. Whether AI code is trustworthy is the open question.",
 "background": "Copilot (2021) launched the era; LLMs (2022-2024) improved; agents (2024-2026) write larger systems. As of 2026 AI code is ubiquitous and unverified.",
 "why_it_matters": "Trustworthy AI code would multiply developer productivity: the pair programmer that never sleeps.",
 "sig_pointer": "The Signature system's proposed approach makes AI code trustworthy, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that AI code needs verification: the generated code checked - with tests, proofs, and review. "
  "Assumptions: (1) verification is automatable; (2) it catches defects; (3) trust follows. "
  "Reasoning path: a verification model explains ubiquitous-but-unverified and predicts trusted AI code. "
  "Proposed mechanism: 'verification-gated' AI code - checked generation. "
  "What would confirm it: verified AI code in production systems. "
  "What would kill it: evidence that AI code is inherently untrustworthy. "
  "What this does not claim: it does not claim trustworthy AI code exists, offers no engineering advice, and does not constitute a tool recommendation."),
 "sig_lens": "The Signature lens reads AI code as unverified ubiquity, and asks what checking would make trusted.",
 "how_it_works": "Researchers study AI code through correctness studies, vulnerability analyses, and verification research.",
 "key_points": [
  "AI writes substantial code.",
  "Correctness is unverified.",
  "Security vulnerabilities appear.",
  "Maintenance burden is unknown.",
  "AI code is ubiquitous and unverified.",
 ],
 "requirements": [
  "Automated verification of generated code.",
  "Verified AI code in production.",
  "Measured trustworthiness.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "GitHub Copilot. Various; 2021 onward.",
  "Pearce H et al. AI-code security. Various; 2022-2023.",
  "Vaithilingam P et al. Copilot studies. Various; 2022-2023.",
  "Jiang E et al. Verification research. Various; 2023-2024.",
 ],
 "demo_data": {"a": ("AI-generated code with vulnerabilities, percent (approx)", 40.0),
               "b": ("percent scale", 100.0), "bounds": (0.28, 0.52),
               "step1": "two in five snippets vulnerable - the unverified ubiquity",
               "confirm": "verified AI code in production systems",
               "refute": "AI code proves inherently untrustworthy"},
},
# ------------------------------------------------------------------ rank 17
{
 "key": "software-maintenance",
 "name": "Software Maintenance: The 80% Problem",
 "group": "Process",
 "ladder_rank": 17, "ladder_tier": "compounded",
 "problem": "Maintenance consumes most software budgets - can it be reduced systematically?",
 "description": "Software maintenance - the 80% problem: most lifecycle cost is maintenance, not development; but maintenance is understudied; and no systematic method reduces it. The field builds; it doesn't maintain.",
 "background": "Maintenance costs were quantified (1970s-80s, Lientz, Swanson); Lehman's laws (1980s) described evolution; but research favors construction. As of 2026 maintenance is still the expensive majority.",
 "why_it_matters": "Reduced maintenance would free most software budgets: the cost that eats the industry.",
 "sig_pointer": "The Signature system's proposed approach reduces maintenance systematically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that maintenance needs reduction science: the drivers identified - with designs that minimize them. "
  "Assumptions: (1) drivers are identifiable; (2) designs reduce them; (3) savings are real. "
  "Reasoning path: a drivers model explains the 80% and predicts reduced maintenance. "
  "Proposed mechanism: 'driver-reduced' software maintenance - designed maintainability. "
  "What would confirm it: measurably reduced maintenance costs. "
  "What would kill it: evidence that maintenance is irreducible. "
  "What this does not claim: it does not claim reduced maintenance exists, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads maintenance as unstudied majority, and asks what science would reduce.",
 "how_it_works": "Researchers study maintenance through Lehman's laws, driver analyses, and maintainability research.",
 "key_points": [
  "Maintenance is ~80% of lifecycle cost.",
  "It is understudied versus construction.",
  "No systematic reduction method exists.",
  "Lehman's laws describe evolution.",
  "The field builds; it doesn't maintain.",
 ],
 "requirements": [
  "Identified maintenance drivers.",
  "Designed maintainability.",
  "Measurably reduced costs.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Lientz BP et al. Maintenance costs. Various; 1978-1983.",
  "Lehman MM et al. Laws of evolution. Various; 1980-2001.",
  "Bennett KH et al. Maintenance reviews. Various; 2000-2010.",
  "Pigoski TM et al. Practical maintenance. Various; 1996-2016.",
 ],
 "demo_data": {"a": ("lifecycle cost from maintenance, percent (approx)", 80.0),
               "b": ("percent scale", 100.0), "bounds": (0.7, 0.9),
               "step1": "four of every five dollars - the cost the field won't study",
               "confirm": "measurably reduced maintenance costs",
               "refute": "maintenance proves irreducible"},
},
# ------------------------------------------------------------------ rank 18
{
 "key": "programming-languages",
 "name": "Programming Languages: The Perfect Language",
 "group": "Design",
 "ladder_rank": 18, "ladder_tier": "compounded",
 "problem": "Hundreds of languages exist - is there a better design, or is language choice inherently fashion?",
 "description": "Programming languages - the perfect language question: new languages (Rust, Go, Swift) improve on predecessors; but no design ends the debate; and the field wonders whether progress is real or fashion.",
 "background": "Language evolution (1950s onward) brought real advances; Rust (2010s) solved memory safety; but fragmentation continues. As of 2026 the perfect language is still debated.",
 "why_it_matters": "Better languages would make all software better: the tool that shapes the thought.",
 "sig_pointer": "The Signature system's proposed approach advances language design scientifically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that language design needs empirical science: the designs tested against human performance - with progress measured. "
  "Assumptions: (1) designs are testable; (2) performance is measurable; (3) progress is real. "
  "Reasoning path: an empirical model explains fashion-cycles and predicts designed languages. "
  "Proposed mechanism: 'empirically-designed' languages - human-tested advances. "
  "What would confirm it: measured language improvements in practice. "
  "What would kill it: evidence that language choice is pure fashion. "
  "What this does not claim: it does not claim the perfect language exists, offers no engineering advice, and does not constitute a language recommendation."),
 "sig_lens": "The Signature lens reads languages as fashion cycles, and asks what empiricism would design.",
 "how_it_works": "Researchers study languages through usability experiments, Rust's safety proof, and design research.",
 "key_points": [
  "Hundreds of languages exist.",
  "Rust solved memory safety practically.",
  "No design ends the debate.",
  "Progress versus fashion is questioned.",
  "Design remains partly aesthetic.",
 ],
 "requirements": [
  "Empirically-tested designs.",
  "Measured human-performance gains.",
  "Real language progress.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Rust language. Various; 2010 onward.",
  "Stefik A et al. Language usability. Various; 2011-2017.",
  "Nanz S et al. Language studies. Various; 2010-2015.",
  "Tratt L et al. Language design. Various; 2019-2023.",
 ],
 "demo_data": {"a": ("memory-safety bugs in C/C++ codebases, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.58, 0.8),
               "step1": "seven in ten bugs are memory bugs - the problem one language solved",
               "confirm": "measured language improvements in practice",
               "refute": "language choice proves pure fashion"},
},
# ------------------------------------------------------------------ rank 19
{
 "key": "software-metrics",
 "name": "Software Metrics: Measuring the Unmeasurable",
 "group": "Process",
 "ladder_rank": 19, "ladder_tier": "compounded",
 "problem": "Software productivity and quality resist measurement - can they be measured meaningfully?",
 "description": "Software metrics - measuring the unmeasurable: lines of code mislead; story points are gamed; DORA metrics help; but no metric captures true productivity or quality. Goodhart's Law haunts every measure.",
 "background": "Metrics debates (1970s-80s) established the pitfalls; DORA (2010s-2020s, Forsgren) found predictive metrics; but gaming persists. As of 2026 measurement is still contested.",
 "why_it_matters": "Meaningful metrics would make software manageable: the measurement that doesn't distort.",
 "sig_pointer": "The Signature system's proposed approach measures software meaningfully, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that metrics need validity science: the measures validated against outcomes - with gaming resisted. "
  "Assumptions: (1) validity is achievable; (2) gaming is resistible; (3) metrics guide. "
  "Reasoning path: a validity model explains Goodhart failures and predicts meaningful measurement. "
  "Proposed mechanism: 'validity-proven' software metrics - outcome-validated measures. "
  "What would confirm it: metrics predicting outcomes without distortion. "
  "What would kill it: evidence that software resists meaningful measurement. "
  "What this does not claim: it does not claim meaningful metrics exist, offers no engineering advice, and does not constitute a management recommendation."),
 "sig_lens": "The Signature lens reads metrics as gamed proxies, and asks what validity would measure.",
 "how_it_works": "Researchers study metrics through DORA research, validity studies, and gaming analyses.",
 "key_points": [
  "Lines of code mislead.",
  "Story points are gamed.",
  "DORA metrics predict performance.",
  "Goodhart's Law haunts measurement.",
  "Measurement is still contested.",
 ],
 "requirements": [
  "Outcome-validated metrics.",
  "Gaming-resistant measures.",
  "Metrics predicting without distortion.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Forsgren N et al. DORA/Accelerate. Various; 2018-2021.",
  "Fenton NE et al. Metrics pitfalls. Various; 1997-2014.",
  "Goodhart's Law applications. Various.",
  "Herbsleb JD et al. Measurement reviews. Various; 2005-2015.",
 ],
 "demo_data": {"a": ("organizations trusting their metrics, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten distrust their own numbers - the unmeasurable measured badly",
               "confirm": "metrics predict outcomes without distortion",
               "refute": "software proves to resist meaningful measurement"},
},
# ------------------------------------------------------------------ rank 20
{
 "key": "self-healing-software",
 "name": "Self-Healing Software",
 "group": "Systems",
 "ladder_rank": 20, "ladder_tier": "compounded",
 "problem": "Software fails at 3 AM - can systems heal themselves without human intervention?",
 "description": "Self-healing software - autonomic recovery: restart strategies, redundancy, and ML-based remediation help; but true self-healing (diagnosing and fixing root causes) is aspirational; most 'healing' is just restarting.",
 "background": "Autonomic computing (IBM, 2001) proposed the vision; chaos engineering (2010s) tested resilience; but self-healing remains shallow. As of 2026 systems restart; they don't heal.",
 "why_it_matters": "Self-healing software would end the 3 AM page: the system that fixes itself.",
 "sig_pointer": "The Signature system's proposed approach builds truly self-healing software, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that self-healing needs causal diagnosis: the systems that find root causes - with verified fixes. "
  "Assumptions: (1) causes are diagnosable; (2) fixes are verifiable; (3) healing is safe. "
  "Reasoning path: a causal model explains restart-shallow healing and predicts true recovery. "
  "Proposed mechanism: 'causally-diagnosing' self-healing - root-cause recovery. "
  "What would confirm it: systems healing novel failures autonomously. "
  "What would kill it: evidence that healing requires human understanding. "
  "What this does not claim: it does not claim self-healing exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads healing as shallow restarts, and asks what causality would make true.",
 "how_it_works": "Researchers study self-healing through autonomic research, chaos engineering, and remediation ML.",
 "key_points": [
  "Most 'healing' is just restarting.",
  "True self-healing is aspirational.",
  "Autonomic computing proposed the vision.",
  "Chaos engineering tests resilience.",
  "Systems restart; they don't heal.",
 ],
 "requirements": [
  "Causal root-cause diagnosis.",
  "Verified autonomous fixes.",
  "Novel-failure healing proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "IBM. Autonomic computing manifesto. 2001.",
  "Ghosh D et al. Self-healing reviews. Various; 2007-2015.",
  "Chaos engineering literature. Various; 2015-2022.",
  "Monperrus M et al. Automated repair. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("incidents resolved without humans, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five incidents need humans - the unhealed system",
               "confirm": "systems heal novel failures autonomously",
               "refute": "healing proves to require human understanding"},
},
# ------------------------------------------------------------------ rank 21
{
 "key": "software-reuse",
 "name": "Software Reuse: The Component Dream",
 "group": "Design",
 "ladder_rank": 21, "ladder_tier": "compounded",
 "problem": "Reuse was promised for decades - can software components ever be truly reusable?",
 "description": "Software reuse - the component dream: libraries and packages are reused; but true component-based engineering (plug-and-play verified components) never arrived; integration costs often exceed reuse savings.",
 "background": "Reuse was promised (1968, McIlroy); open source (2000s-2010s) delivered library reuse; but component engineering stalled. As of 2026 reuse is library-deep.",
 "why_it_matters": "True reuse would make software compositional: building from certified parts.",
 "sig_pointer": "The Signature system's proposed approach achieves true software reuse, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that reuse needs certified components: the verified, specified parts - with composition guaranteed. "
  "Assumptions: (1) components are certifiable; (2) composition is guaranteed; (3) economics work. "
  "Reasoning path: a certification model explains library-only reuse and predicts component engineering. "
  "Proposed mechanism: 'certified-component' reuse - verified composable parts. "
  "What would confirm it: certified components composed at scale. "
  "What would kill it: evidence that integration inherently defeats reuse. "
  "What this does not claim: it does not claim true reuse exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads reuse as library-shallow, and asks what certification would make component.",
 "how_it_works": "Researchers study reuse through component models, certification research, and economics analyses.",
 "key_points": [
  "Libraries are reused; components aren't.",
  "McIlroy promised this in 1968.",
  "Integration costs often exceed savings.",
  "Component engineering stalled.",
  "Reuse is library-deep.",
 ],
 "requirements": [
  "Certified verified components.",
  "Guaranteed composition.",
  "Component reuse at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "McIlroy MD. Mass-produced software. 1968.",
  "Szyperski C et al. Component software. Various; 1998-2002.",
  "Frakes WB et al. Reuse reviews. Various; 2005-2015.",
  "Ravichandran T et al. Reuse economics. Various; 1999-2005.",
 ],
 "demo_data": {"a": ("code that is reused components, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten lines are bespoke - the uncomposed software",
               "confirm": "certified components composed at scale",
               "refute": "integration proves to inherently defeat reuse"},
},
# ------------------------------------------------------------------ rank 22
{
 "key": "quantum-software",
 "name": "Quantum Software Engineering",
 "group": "Systems",
 "ladder_rank": 22, "ladder_tier": "compounded",
 "problem": "Quantum computers need software - but quantum programming is barely a discipline. Can it be engineered?",
 "description": "Quantum software engineering - programming quantum computers: the languages (Q#, Qiskit), debugging, and testing are primitive; no software-engineering discipline exists for quantum; the field is pre-methodology.",
 "background": "Quantum programming (1990s-2000s) was theoretical; Qiskit/Q# (2010s) made it practical; but engineering discipline is absent. As of 2026 quantum software is hand-crafted.",
 "why_it_matters": "Quantum software engineering would make quantum computing usable: the discipline for the new machine.",
 "sig_pointer": "The Signature system's proposed approach engineers quantum software, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that quantum software needs engineering discipline: the methods, testing, and tooling - adapted to quantum. "
  "Assumptions: (1) classical methods adapt; (2) quantum needs are learnable; (3) discipline emerges. "
  "Reasoning path: a discipline model explains hand-crafted status and predicts quantum SE. "
  "Proposed mechanism: 'disciplined' quantum software engineering - adapted methods. "
  "What would confirm it: engineered quantum software at scale. "
  "What would kill it: evidence that quantum resists engineering. "
  "What this does not claim: it does not claim quantum SE exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads quantum code as hand-crafted, and asks what discipline would engineer.",
 "how_it_works": "Researchers study quantum SE through language research, testing methods, and methodology development.",
 "key_points": [
  "Quantum programming is barely a discipline.",
  "Languages and tools are primitive.",
  "No testing methodology exists.",
  "The field is pre-methodology.",
  "Quantum software is hand-crafted.",
 ],
 "requirements": [
  "Quantum-adapted SE methods.",
  "Testing and debugging for quantum.",
  "Engineered quantum software at scale.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Qiskit / Q#. Various; 2017 onward.",
  "Zhao J et al. Quantum SE reviews. Various; 2020-2023.",
  "Piattini M et al. Quantum software. Various; 2021-2024.",
  "Murillo-Morales T et al. Testing quantum. Various; 2021-2023.",
 ],
 "demo_data": {"a": ("quantum programs built with SE methods, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten hand-crafted - the undisciplined quantum",
               "confirm": "engineered quantum software at scale",
               "refute": "quantum proves to resist engineering"},
},
# ------------------------------------------------------------------ rank 23
{
 "key": "software-ethics",
 "name": "Software Ethics: Engineering Responsibility",
 "group": "Process",
 "ladder_rank": 23, "ladder_tier": "compounded",
 "problem": "Software shapes society - can engineering ethics be made effective rather than decorative?",
 "description": "Software ethics - engineering responsibility: codes of ethics exist (ACM); but they rarely constrain practice; algorithmic harm continues; and the field debates whether ethics can be engineered into process.",
 "background": "ACM ethics codes (1970s onward) were aspirational; algorithmic accountability (2010s-2020s) grew; but enforcement is absent. As of 2026 ethics is still decorative.",
 "why_it_matters": "Effective ethics would make software responsible: the conscience engineered in.",
 "sig_pointer": "The Signature system's proposed approach makes software ethics effective, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that ethics needs process integration: the ethical checks embedded in engineering - with accountability. "
  "Assumptions: (1) ethics is processable; (2) integration works; (3) accountability follows. "
  "Reasoning path: an integration model explains decorative status and predicts effective ethics. "
  "Proposed mechanism: 'process-integrated' software ethics - embedded accountability. "
  "What would confirm it: ethics constraining real engineering decisions. "
  "What would kill it: evidence that ethics can't be engineered. "
  "What this does not claim: it takes no moral positions, offers no engineering advice, and does not constitute a policy recommendation."),
 "sig_lens": "The Signature lens reads ethics as decorative codes, and asks what integration would make effective.",
 "how_it_works": "Researchers study software ethics through accountability research, process studies, and case analyses.",
 "key_points": [
  "Codes of ethics rarely constrain practice.",
  "Algorithmic harm continues.",
  "Enforcement is absent.",
  "Accountability research is growing.",
  "Ethics is still decorative.",
 ],
 "requirements": [
  "Process-embedded ethical checks.",
  "Ethics constraining decisions.",
  "Accountable engineering practice.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "ACM Code of Ethics. Various; 1972-2018.",
  "Mittelstadt B et al. Algorithmic ethics. Various; 2016-2021.",
  "Gotterbarn D et al. Ethics enforcement. Various; 2000-2015.",
  "Floridi L et al. AI ethics. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("engineering decisions constrained by ethics codes, percent (approx)", 10.0),
               "b": ("percent scale", 100.0), "bounds": (0.05, 0.18),
               "step1": "nine in ten decisions unbound - the decorative conscience",
               "confirm": "ethics constrains real engineering decisions",
               "refute": "ethics proves unable to be engineered"},
},
# ------------------------------------------------------------------ rank 24
{
 "key": "program-synthesis",
 "name": "Program Synthesis: Writing Programs from Specs",
 "group": "AI",
 "ladder_rank": 24, "ladder_tier": "advanced",
 "problem": "Can programs be synthesized from specifications - the machine writing correct code from intent?",
 "description": "Program synthesis - generating programs from specifications: the dream of correct-by-construction code; but specifications are as hard as code; synthesis scales poorly; and LLMs changed the game without solving it.",
 "background": "Synthesis research (1970s-80s, Manna, Waldinger) was foundational; SyGuS (2010s) formalized the competition; LLMs (2020s) made informal synthesis practical. As of 2026 synthesis is useful but not correct-by-construction.",
 "why_it_matters": "True synthesis would end coding: intent in, correct program out.",
 "sig_pointer": "The Signature system's proposed approach achieves correct-by-construction synthesis, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that synthesis needs verifiable specs: the specifications checked - with synthesized code proven. "
  "Assumptions: (1) specs are writable; (2) synthesis scales; (3) proofs carry. "
  "Reasoning path: a specs model explains the synthesis gap and predicts correct construction. "
  "Proposed mechanism: 'spec-verified' program synthesis - proven generation. "
  "What would confirm it: synthesized programs with proofs in production. "
  "What would kill it: evidence that specs are as hard as code. "
  "What this does not claim: it does not claim true synthesis exists, offers no engineering advice, and does not constitute a tool recommendation."),
 "sig_lens": "The Signature lens reads synthesis as spec-limited, and asks what verification would make correct.",
 "how_it_works": "Researchers study synthesis through SyGuS competitions, LLM synthesis, and verification research.",
 "key_points": [
  "Specifications are as hard as code.",
  "Synthesis scales poorly.",
  "LLMs made informal synthesis practical.",
  "Correct-by-construction is unachieved.",
  "The dream dates to the 1970s.",
 ],
 "requirements": [
  "Writable verifiable specifications.",
  "Scaled synthesis with proofs.",
  "Synthesized programs in production.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Manna Z et al. Synthesis foundations. Various; 1970s-1980s.",
  "SyGuS competition. Various; 2013 onward.",
  "Gulwani S et al. Synthesis reviews. Various; 2017-2022.",
  "LLM synthesis literature. Various; 2022-2024.",
 ],
 "demo_data": {"a": ("synthesized programs with proofs, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty synthesized with proof - the unproven generation",
               "confirm": "synthesized programs with proofs in production",
               "refute": "specs prove as hard as code"},
},
# ------------------------------------------------------------------ rank 25
{
 "key": "software-verification-scale",
 "name": "Verification at Scale: The Million-Line Proof",
 "group": "Correctness",
 "ladder_rank": 25, "ladder_tier": "advanced",
 "problem": "Verification works for kernels - can it scale to million-line systems?",
 "description": "Verification at scale - the million-line proof: seL4 verified 10k lines; but real systems are millions; the proof engineering doesn't scale linearly; and whether full-system verification is feasible is open.",
 "background": "seL4 (2009) was the landmark; larger verifications (CompCert, IronFleet) pushed scale; but the million-line proof is unachieved. As of 2026 verification is kernel-scale.",
 "why_it_matters": "Scaled verification would make whole systems trustworthy: the proof of the million lines.",
 "sig_pointer": "The Signature system's proposed approach scales verification to millions of lines, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that verification scales through automation: the proof engineering automated - with composition carrying. "
  "Assumptions: (1) automation works; (2) composition scales; (3) million lines are reachable. "
  "Reasoning path: an automation model explains kernel-scale limits and predicts million-line proofs. "
  "Proposed mechanism: 'automation-scaled' verification - machine-built proofs. "
  "What would confirm it: million-line verified systems. "
  "What would kill it: evidence that proof doesn't scale. "
  "What this does not claim: it does not claim million-line proofs exist, offers no engineering advice, and does not constitute a research recommendation."),
 "sig_lens": "The Signature lens reads verification as kernel-bound, and asks what automation would scale.",
 "how_it_works": "Researchers study verification scale through IronFleet, proof automation, and compositional research.",
 "key_points": [
  "seL4 verified ~10k lines.",
  "Real systems are millions of lines.",
  "Proof engineering doesn't scale linearly.",
  "IronFleet pushed distribution scale.",
  "The million-line proof is unachieved.",
 ],
 "requirements": [
  "Automated proof engineering.",
  "Million-line verified systems.",
  "Compositional scale proven.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Klein G et al. seL4. Various; 2009-2014.",
  "Hawblitzel C et al. IronFleet. Various; 2015-2017.",
  "Leroy X et al. CompCert scale. Various; 2006-2021.",
  "Appel AW et al. Scale reviews. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("largest verified system, thousands of lines (approx)", 100.0),
               "b": ("typical OS, millions of lines (approx)", 50.0), "bounds": (1.5, 2.8),
               "step1": "a hundred thousand verified against fifty million - the proof's five-hundred-fold gap",
               "confirm": "million-line verified systems",
               "refute": "proof proves unable to scale"},
},
# ------------------------------------------------------------------ rank 26
{
 "key": "secure-by-design",
 "name": "Secure by Design: The Vulnerability-Free System",
 "group": "Security",
 "ladder_rank": 26, "ladder_tier": "advanced",
 "problem": "Vulnerabilities are endemic - can systems be designed to be secure rather than patched?",
 "description": "Secure by design - the vulnerability-free system: memory-safe languages, capability systems, and formal methods promise it; but the installed base is insecure; and whether security can be designed in (not bolted on) at scale is open.",
 "background": "Security engineering (Anderson, 2000s) framed the discipline; memory-safe languages (Rust) removed bug classes; CISA's secure-by-design (2023) pushed the principle. As of 2026 design is improving but vulnerabilities persist.",
 "why_it_matters": "Secure-by-design would end the vulnerability treadmill: the system that's safe from the start.",
 "sig_pointer": "The Signature system's proposed approach designs security in, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that security is designable: the languages, architectures, and methods that eliminate vulnerability classes - with adoption. "
  "Assumptions: (1) classes are eliminable; (2) designs exist; (3) industry adopts. "
  "Reasoning path: a design model explains vulnerability persistence and predicts secure systems. "
  "Proposed mechanism: 'class-eliminating' secure design - designed-in security. "
  "What would confirm it: vulnerability classes eliminated at scale. "
  "What would kill it: evidence that vulnerabilities are inherent. "
  "What this does not claim: it does not claim secure-by-design exists at scale, offers no engineering advice, and does not constitute a security recommendation."),
 "sig_lens": "The Signature lens reads security as patched-on, and asks what design would eliminate.",
 "how_it_works": "Researchers study secure design through memory-safe adoption, capability systems, and CISA initiatives.",
 "key_points": [
  "Vulnerabilities are endemic.",
  "Memory-safe languages remove bug classes.",
  "The installed base is insecure.",
  "CISA pushed secure-by-design.",
  "Design-in versus bolt-on is the question.",
 ],
 "requirements": [
  "Eliminated vulnerability classes.",
  "Designed-in security at scale.",
  "Measurably fewer vulnerabilities.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Anderson RJ. Security Engineering. Various; 2001-2020.",
  "CISA. Secure by Design. 2023 onward.",
  "Rust memory safety. Various; 2010 onward.",
  "Langsec / capability literature. Various; 2012-2022.",
 ],
 "demo_data": {"a": ("vulnerabilities from memory unsafety, percent (approx)", 70.0),
               "b": ("percent scale", 100.0), "bounds": (0.58, 0.8),
               "step1": "seven in ten from one eliminable class - the designed-in failure",
               "confirm": "vulnerability classes eliminated at scale",
               "refute": "vulnerabilities prove inherent"},
},
# ------------------------------------------------------------------ rank 27
{
 "key": "software-economics",
 "name": "Software Economics: The Value Problem",
 "group": "Process",
 "ladder_rank": 27, "ladder_tier": "advanced",
 "problem": "Software's value is intangible - can its economics be made rigorous?",
 "description": "Software economics - the value problem: pricing, ROI, and the economics of open source are poorly understood; technical debt has no balance sheet; and whether software economics can be rigorous is open.",
 "background": "Software economics (Boehm, 1980s) began the field; open-source economics (2000s-2010s) puzzled; but rigor is lacking. As of 2026 software value is still hand-waved.",
 "why_it_matters": "Rigorous software economics would make decisions rational: the value made visible.",
 "sig_pointer": "The Signature system's proposed approach makes software economics rigorous, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that software value is measurable: the ROI, debt, and open-source economics quantified - with decisions guided. "
  "Assumptions: (1) value is quantifiable; (2) models work; (3) decisions improve. "
  "Reasoning path: a value model explains hand-waving and predicts rigorous economics. "
  "Proposed mechanism: 'value-quantified' software economics - rigorous models. "
  "What would confirm it: quantified software decisions outperforming. "
  "What would kill it: evidence that software value resists quantification. "
  "What this does not claim: it does not claim rigorous economics exists, offers no engineering advice, and does not constitute a business recommendation."),
 "sig_lens": "The Signature lens reads software value as hand-waved, and asks what quantification would make rigorous.",
 "how_it_works": "Researchers study software economics through ROI research, debt quantification, and open-source economics.",
 "key_points": [
  "Software value is intangible.",
  "Technical debt has no balance sheet.",
  "Open-source economics puzzled.",
  "Pricing is poorly understood.",
  "Value is still hand-waved.",
 ],
 "requirements": [
  "Quantified software value.",
  "Rigorous economic models.",
  "Better decisions from quantification.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Boehm BW. Software economics. Various; 1981-2000.",
  "Nagle F et al. Open-source economics. Various; 2020-2024.",
  "Erdogmus H et al. Value research. Various; 2005-2015.",
  "Rönkkö M et al. Software business. Various; 2010-2020.",
 ],
 "demo_data": {"a": ("software decisions backed by quantified value, percent (approx)", 20.0),
               "b": ("percent scale", 100.0), "bounds": (0.12, 0.3),
               "step1": "four in five decisions unquantified - the invisible value",
               "confirm": "quantified software decisions outperform",
               "refute": "software value proves to resist quantification"},
},
# ------------------------------------------------------------------ rank 28
{
 "key": "human-computer-interaction",
 "name": "HCI: The Usability Science",
 "group": "Design",
 "ladder_rank": 28, "ladder_tier": "advanced",
 "problem": "Software is still hard to use - can usability become a predictive science?",
 "description": "Human-computer interaction - the usability science: interfaces improved; but software remains hard; and HCI is descriptive more than predictive. Whether usability can be engineered scientifically is open.",
 "background": "HCI (1980s-90s, Card, Moran, Newell) sought science; usability methods spread; but prediction is weak. As of 2026 usability is still craft.",
 "why_it_matters": "Predictive usability would make software usable: the science of the interface.",
 "sig_pointer": "The Signature system's proposed approach makes usability predictive, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that usability is predictable: the models forecasting user performance - with designs optimized. "
  "Assumptions: (1) behavior is modelable; (2) models predict; (3) designs optimize. "
  "Reasoning path: a predictive model explains craft-status and predicts scientific HCI. "
  "Proposed mechanism: 'predictively-modeled' usability - forecasted interfaces. "
  "What would confirm it: predicted usability matching measured. "
  "What would kill it: evidence that usability resists prediction. "
  "What this does not claim: it does not claim predictive usability exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads HCI as descriptive craft, and asks what models would predict.",
 "how_it_works": "Researchers study HCI through predictive modeling, usability experiments, and design research.",
 "key_points": [
  "Software remains hard to use.",
  "HCI is descriptive more than predictive.",
  "Usability methods spread widely.",
  "Prediction of usability is weak.",
  "The field sought science since the 1980s.",
 ],
 "requirements": [
  "Predictive usability models.",
  "Predicted matching measured usability.",
  "Optimized interface designs.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Card SK et al. Psychology of HCI. Various; 1983-2018.",
  "Nielsen J et al. Usability methods. Various; 1993-2012.",
  "Oulasvirta A et al. Predictive HCI. Various; 2020-2024.",
  "Shneiderman B et al. Design reviews. Various; 2016-2022.",
 ],
 "demo_data": {"a": ("usability problems predicted before testing, percent (approx)", 30.0),
               "b": ("percent scale", 100.0), "bounds": (0.2, 0.42),
               "step1": "seven in ten found only by testing - the unpredicted interface",
               "confirm": "predicted usability matches measured",
               "refute": "usability proves to resist prediction"},
},
# ------------------------------------------------------------------ rank 29
{
 "key": "distributed-trust",
 "name": "Distributed Trust: Beyond Blockchain",
 "group": "Systems",
 "ladder_rank": 29, "ladder_tier": "advanced",
 "problem": "Blockchain promised trust without trust - but can distributed trust be efficient and useful?",
 "description": "Distributed trust - beyond blockchain: the technology promised trust without trusted third parties, but it remains inefficient, smart contracts are notoriously buggy, and the genuinely useful applications are still debated. Bitcoin launched the idea in 2008 and smart contracts expanded it in the 2010s, yet efficiency and bug problems limited adoption - and whether distributed trust has a killer application beyond speculation is still an open question.",
 "background": "Bitcoin (2008) launched the idea; smart contracts (2010s) expanded it; but efficiency and bugs limited it. As of 2026 distributed trust is still seeking its use.",
 "why_it_matters": "Useful distributed trust would reshape institutions: trust without the trusted third party.",
 "sig_pointer": "The Signature system's proposed approach finds distributed trust's real uses, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that distributed trust needs useful applications: the efficient protocols with proven value - beyond speculation. "
  "Assumptions: (1) efficiency is achievable; (2) applications exist; (3) value is proven. "
  "Reasoning path: an applications model explains the killer-app gap and predicts useful trust. "
  "Proposed mechanism: 'usefully-applied' distributed trust - efficient valued protocols. "
  "What would confirm it: distributed-trust applications with proven value. "
  "What would kill it: evidence that distributed trust has no use. "
  "What this does not claim: it takes no position on cryptocurrencies, offers no engineering advice, and does not constitute a technology recommendation."),
 "sig_lens": "The Signature lens reads blockchain as solution-seeking-problem, and asks what uses would justify.",
 "how_it_works": "Researchers study distributed trust through protocol research, application studies, and efficiency analyses.",
 "key_points": [
  "Blockchain is inefficient.",
  "Smart contracts are buggy.",
  "Useful applications are debated.",
  "The killer app is unproven.",
  "Trust without third parties is the promise.",
 ],
 "requirements": [
  "Efficient trust protocols.",
  "Proven-value applications.",
  "Beyond-speculation usefulness.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Nakamoto S. Bitcoin. 2008.",
  "Buterin V et al. Smart contracts. Various; 2013-2020.",
  "Bonneau J et al. Cryptocurrency reviews. Various; 2015-2020.",
  "Narayanan A et al. Trust research. Various; 2016-2021.",
 ],
 "demo_data": {"a": ("blockchain apps with proven non-speculative value (approx)", 5.0),
               "b": ("blockchain apps launched (approx)", 1000.0), "bounds": (0.002, 0.01),
               "step1": "five useful of a thousand launched - the trust still seeking its use",
               "confirm": "distributed-trust applications with proven value",
               "refute": "distributed trust proves to have no use"},
},
# ------------------------------------------------------------------ rank 30
{
 "key": "software-sustainability",
 "name": "Sustainable Software: The Carbon Code",
 "group": "Systems",
 "ladder_rank": 30, "ladder_tier": "advanced",
 "problem": "Software consumes growing energy - can code be engineered for carbon efficiency?",
 "description": "Sustainable software - the carbon code: data centers consume roughly one percent of global electricity, software efficiency is rarely optimized or even measured, and carbon-aware engineering is still in its infancy. Green computing raised awareness in the 2000s and the Green Software Foundation organized the field in 2021, but efficiency is almost never a project requirement - and whether green software engineering can matter at planetary scale remains open.",
 "background": "Green computing (2000s-2010s) raised awareness; the Green Software Foundation (2021) organized; but carbon-aware engineering is early. As of 2026 efficiency is rarely a requirement.",
 "why_it_matters": "Carbon-efficient software would cut computing's footprint: the code that cools the planet.",
 "sig_pointer": "The Signature system's proposed approach engineers carbon-efficient software, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that software carbon is engineerable: the efficiency measured and optimized - with carbon as a requirement. "
  "Assumptions: (1) carbon is measurable; (2) optimization works; (3) requirements stick. "
  "Reasoning path: a measurement model explains the efficiency gap and predicts green software. "
  "Proposed mechanism: 'carbon-optimized' software engineering - measured efficiency. "
  "What would confirm it: measurably lower-carbon software at scale. "
  "What would kill it: evidence that software carbon is negligible or irreducible. "
  "What this does not claim: it does not claim green software exists at scale, offers no engineering advice, and does not constitute a process recommendation."),
 "sig_lens": "The Signature lens reads code as carbon-blind, and asks what measurement would green.",
 "how_it_works": "Researchers study sustainable software through carbon measurement, efficiency research, and foundation standards.",
 "key_points": [
  "Data centers consume ~1% of electricity.",
  "Software efficiency is rarely optimized.",
  "The Green Software Foundation organized.",
  "Carbon-aware engineering is early.",
  "Efficiency is rarely a requirement.",
 ],
 "requirements": [
  "Measured software carbon.",
  "Optimized carbon efficiency.",
  "Carbon as a standard requirement.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Green Software Foundation. Various; 2021 onward.",
  "Masanet E et al. Data-center energy. Various; 2020-2022.",
  "Patterson D et al. ML carbon. Various; 2021-2022.",
  "Kern E et al. Green software. Various; 2018-2023.",
 ],
 "demo_data": {"a": ("projects with carbon requirements, percent (approx)", 5.0),
               "b": ("percent scale", 100.0), "bounds": (0.03, 0.08),
               "step1": "one in twenty considers carbon - the blind code",
               "confirm": "measurably lower-carbon software at scale",
               "refute": "software carbon proves negligible or irreducible"},
},
# ------------------------------------------------------------------ rank 31
{
 "key": "software-consciousness",
 "name": "Software and Mind: The Consciousness Question",
 "group": "Theory",
 "ladder_rank": 31, "ladder_tier": "advanced",
 "problem": "Could software ever be conscious - and would engineers know?",
 "description": "Software consciousness - the philosophical engineering question: if AI systems ever credibly claimed consciousness, software engineering would need tests to assess the claim, but no accepted test exists and the field largely avoids the question. The consciousness debate from philosophy collided with AI progress in the 2020s, criteria are debated without resolution, and no engineering methodology exists for what may become the most consequential question the field ever faces.",
 "background": "The consciousness debate (philosophy) met AI (2020s); engineers were asked to assess claims; but no methodology exists. As of 2026 the question is unaddressed.",
 "why_it_matters": "Conscious software would transform engineering ethics: the mind in the machine.",
 "sig_pointer": "The Signature system's proposed approach addresses machine consciousness methodologically, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that machine consciousness needs engineering methodology: the tests and criteria - with honest uncertainty. "
  "Assumptions: (1) criteria are formulable; (2) tests are possible; (3) uncertainty is honest. "
  "Reasoning path: a methodology model explains the avoidance and predicts addressed questions. "
  "Proposed mechanism: 'methodologically-addressed' machine consciousness - tested criteria. "
  "What would confirm it: accepted tests for machine consciousness. "
  "What would kill it: evidence that the question is untestable. "
  "What this does not claim: it takes no position on machine consciousness, offers no engineering advice, and does not constitute a philosophical claim."),
 "sig_lens": "The Signature lens reads consciousness as the avoided question, and asks what methodology would address.",
 "how_it_works": "Researchers study machine consciousness through test proposals, criteria debates, and philosophical analyses.",
 "key_points": [
  "No test for machine consciousness exists.",
  "Engineers may face consciousness claims.",
  "The field avoids the question.",
  "Criteria are debated philosophically.",
  "Methodology is absent.",
 ],
 "requirements": [
  "Formulated test criteria.",
  "Accepted consciousness tests.",
  "Honest uncertainty maintained.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Chalmers DJ et al. Consciousness and AI. Various; 2023-2024.",
  "Butlin P et al. Consciousness tests. Various; 2023-2024.",
  "Schneider S et al. AI consciousness. Various; 2019-2023.",
  "Long R et al. Methodology debates. Various; 2024-2025.",
 ],
 "demo_data": {"a": ("accepted tests for machine consciousness (approx)", 1.0),
               "b": ("proposed tests (approx)", 20.0), "bounds": (0.02, 0.1),
               "step1": "one accepted of twenty proposed - the untested question",
               "confirm": "accepted tests for machine consciousness",
               "refute": "the question proves untestable"},
},
# ------------------------------------------------------------------ rank 32
{
 "key": "software-complexity",
 "name": "Taming Complexity: The Essential Difficulty",
 "group": "Theory",
 "ladder_rank": 32, "ladder_tier": "advanced",
 "problem": "Brooks called complexity essential - can software's inherent complexity ever be tamed?",
 "description": "Software complexity - the essential difficulty: Brooks (1986, No Silver Bullet) argued complexity is inherent; decades of silver bullets failed; but whether complexity is truly essential or just unmanaged is still debated.",
 "background": "Brooks (1986) declared no silver bullet; each decade's bullet (objects, agile, AI) disappointed; but the essential-versus-accidental debate continues. As of 2026 complexity is still the enemy.",
 "why_it_matters": "Tamed complexity would make software tractable: the end of the essential difficulty.",
 "sig_pointer": "The Signature system's proposed approach tames software complexity, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that complexity is manageable: the essential separated from accidental - with the accidental eliminated. "
  "Assumptions: (1) the distinction holds; (2) accidental is eliminable; (3) essential is manageable. "
  "Reasoning path: a distinction model explains bullet failures and predicts tamed complexity. "
  "Proposed mechanism: 'distinction-managed' complexity - accidental eliminated. "
  "What would confirm it: measurably simpler systems at scale. "
  "What would kill it: evidence that all complexity is essential. "
  "What this does not claim: it does not claim tamed complexity exists, offers no engineering advice, and does not constitute a design recommendation."),
 "sig_lens": "The Signature lens reads complexity as unmanaged essential, and asks what distinction would tame.",
 "how_it_works": "Researchers study complexity through Brooks' framework, simplicity research, and measurement studies.",
 "key_points": [
  "Brooks declared no silver bullet (1986).",
  "Each decade's bullet disappointed.",
  "Essential vs accidental is debated.",
  "Complexity is still the enemy.",
  "The question is whether it's tamable.",
 ],
 "requirements": [
  "Separated essential and accidental.",
  "Eliminated accidental complexity.",
  "Measurably simpler systems.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Brooks FP. No Silver Bullet. Various; 1986-1995.",
  "Parnas DL et al. Complexity writings. Various; 1972-2010.",
  "Moseley B et al. Out of the tar pit. Various; 2006-2012.",
  "Hickey R et al. Simplicity. Various; 2011-2020.",
 ],
 "demo_data": {"a": ("complexity attributed to accidental causes, percent (approx)", 50.0),
               "b": ("percent scale", 100.0), "bounds": (0.35, 0.65),
               "step1": "half the complexity is accidental - the tamable half",
               "confirm": "measurably simpler systems at scale",
               "refute": "all complexity proves essential"},
},
# ------------------------------------------------------------------ rank 33
{
 "key": "software-future",
 "name": "The Future of Software: A Century Ahead",
 "group": "Theory",
 "ladder_rank": 33, "ladder_tier": "advanced",
 "problem": "What will software engineering become? The field extrapolates poorly - can its future be foreseen?",
 "description": "Software futurology - predicting the field's century - is speculative: past predictions (automatic programming by 2000) partially arrived via LLMs; but structured foresight is absent; whether futures work improves decisions is the meta-question.",
 "background": "Software predictions have a mixed record; LLMs surprised the field; scenario methods are unused. As of 2026 the future is debated without discipline.",
 "why_it_matters": "Long-horizon decisions (education, research) need foresight: the discipline of software futures.",
 "sig_pointer": "The Signature system's proposed approach builds disciplined software foresight, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that software futures need disciplined foresight: the scenario methods and roadmaps - with track records. "
  "Assumptions: (1) foresight is improvable; (2) methods exist; (3) they guide decisions. "
  "Reasoning path: a foresight model explains surprise and predicts better futures work. "
  "Proposed mechanism: 'disciplined' software foresight - tracked scenario methods. "
  "What would confirm it: foresight with validated track records. "
  "What would kill it: evidence that software futures are unforeseeable. "
  "What this does not claim: it does not claim any future, offers no engineering advice, and does not constitute a prediction."),
 "sig_lens": "The Signature lens reads software futures as undisciplined speculation, and asks what methods would foresee.",
 "how_it_works": "Researchers study software futures through scenario methods, technology roadmapping, and prediction tracking.",
 "key_points": [
  "Software predictions have a mixed record.",
  "LLMs surprised the field.",
  "Scenario methods are unused.",
  "Long-horizon decisions need foresight.",
  "The discipline is undeveloped.",
 ],
 "requirements": [
  "Validated foresight methods.",
  "Track records for predictions.",
  "Decisions guided by foresight.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Glass RL et al. Prediction histories. Various; 2006-2015.",
  "Johnson P et al. Software futures. Various; 2018-2022.",
  "Foresight methodology literature. Various.",
  "Brooks FP et al. Field reflections. Various; 1995-2015.",
 ],
 "demo_data": {"a": ("software predictions with validated track records (approx)", 5.0),
               "b": ("software predictions made (approx)", 200.0), "bounds": (0.015, 0.04),
               "step1": "five tracked of two hundred made - the foresight without a record",
               "confirm": "foresight with validated track records",
               "refute": "software futures prove unforeseeable"},
},
# ------------------------------------------------------------------ rank 34
{
 "key": "software-science",
 "name": "Software Engineering as Science",
 "group": "Theory",
 "ladder_rank": 34, "ladder_tier": "advanced",
 "problem": "Is software engineering a science, a craft, or an art - and can it become a true engineering science?",
 "description": "Software engineering's scientific status - the field's identity question: is it science, craft, or art? Evidence is weak; replication is rare; and whether SE can become a true engineering science (like civil engineering) is the deepest open question.",
 "background": "The science debate (1968 onward) never resolved; empirical SE (2000s-2010s) grew; but the field still lacks the predictive power of true engineering sciences. As of 2026 the identity is unresolved.",
 "why_it_matters": "Scientific software engineering would make building reliable: the discipline grown up.",
 "sig_pointer": "The Signature system's proposed approach makes software engineering scientific, explored in the companion Signature Edition record.",
 "sig_full": ("The Signature system proposes that SE becomes scientific through evidence: the replicated studies, predictive theories, and validated methods - with engineering discipline. "
  "Assumptions: (1) evidence accumulates; (2) theories predict; (3) the field matures. "
  "Reasoning path: an evidence model explains the identity crisis and predicts scientific SE. "
  "Proposed mechanism: 'evidence-built' software science - replicated predictive discipline. "
  "What would confirm it: predictive theories guiding practice. "
  "What would kill it: evidence that software resists science. "
  "What this does not claim: it does not claim SE is a science, offers no engineering advice, and does not constitute a disciplinary claim."),
 "sig_lens": "The Signature lens reads SE as identity-unresolved, and asks what evidence would make scientific.",
 "how_it_works": "Researchers study SE science through replication studies, theory building, and empirical research.",
 "key_points": [
  "SE's scientific status is debated.",
  "Evidence is weak; replication is rare.",
  "Empirical SE grew in the 2000s-2010s.",
  "Predictive power is lacking.",
  "The identity question is the deepest.",
 ],
 "requirements": [
  "Replicated empirical studies.",
  "Predictive theories.",
  "Validated methods guiding practice.",
 ],
 "standards": STD_COMMON,
 "citations": [
  "Shaw M et al. SE science debates. Various; 1990-2015.",
  "Sjøberg DIK et al. Theory building. Various; 2008-2015.",
  "Wohlin C et al. Empirical SE. Various; 2012-2021.",
  "Stol KJ et al. Replication. Various; 2018-2022.",
 ],
 "demo_data": {"a": ("SE studies replicated (approx)", 10.0),
               "b": ("SE studies published (approx)", 1000.0), "bounds": (0.005, 0.018),
               "step1": "ten replicated of a thousand published - the unscientific science",
               "confirm": "predictive theories guide practice",
               "refute": "software proves to resist science"},
},
]
