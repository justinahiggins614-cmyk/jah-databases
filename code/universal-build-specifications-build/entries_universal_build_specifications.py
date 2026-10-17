#!/usr/bin/env python3
"""Entries for the Universal Build Specifications databases (Build-210 #1).

Verified 2026-10-17 (Build-210 top-20 #1): NO database covers converting a
request into a complete structured build specification - objectives,
deliverables, functional and non-functional requirements, constraints,
assumptions and dependencies, acceptance criteria, verification plans -
across software, hardware, devices, and systems. The paste's rule was
applied by name/purpose/record schema/capabilities; the one keyword hit
(lego-satellite) is unrelated.

Manifest search (2,384 databases): zero 'universal-build*' slugs/names;
zero 'build-spec' slugs/names. Whole-system exact-title sweep over the
manifest PLUS all shard index 't' keys: zero collisions for all 34 planned
titles x2 editions (68 variants). NOTE: the persisted dedupe gate dir
(data/dedupe/exact) is stale for the newest fields, so the raw
manifest+shard sweep was the authoritative preflight.

So this build creates two NEW databases, 34 ladder-ordered records each:

  universal-build-specifications           - The Universal Build Specifications Database
                                             (public-harvest: real, fact-checked
                                             requirements and systems engineering -
                                             the discipline of turning requests into
                                             complete build specifications; standard
                                             references INCOSE Systems Engineering
                                             Handbook 4th ed 2015; ISO/IEC/IEEE
                                             29148:2018 Requirements Engineering;
                                             ISO/IEC/IEEE 15288:2015 Life Cycle
                                             Processes; Wiegers and Beatty Software
                                             Requirements 3rd ed 2013; Robertson and
                                             Robertson Mastering the Requirements
                                             Process 3rd ed 2012; NASA Systems
                                             Engineering Handbook SP-2016-6105 Rev 2
                                             2016; PMBOK Guide 7th ed 2021; landmark
                                             standards and papers as cited per record)
  universal-build-specifications-signature - The Universal Build Specifications
                                             Signature Database
                                             (his original Signature Build Method:
                                             every request is a commission and every
                                             specification a build contract - the
                                             objective as the destination, deliverables
                                             as the promised cargo, requirements as the
                                             load-bearing beams, acceptance as the final
                                             inspection stamp; src signature, titles
                                             suffixed " (Signature Edition)", never
                                             presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-UBS- (public) and JAH-UBSS- (signature), verified free in
the manifest and in every shard index (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds (never float exact-equality), and ends with the OK marker;
the build machine-executes all 68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature Build Method: every "
            "request is a commission and every specification a build contract - "
            "the objective as the destination, deliverables as the promised "
            "cargo, requirements as the load-bearing beams, and acceptance as "
            "the final inspection stamp. Clearly labeled Signature-made, never "
            "presented as authentic public record.")

CIT_INCOSE_HB = ("INCOSE. INCOSE-TP-2003-002-04. Systems Engineering Handbook: "
                 "A Guide for System Life Cycle Processes and Activities. 4th "
                 "ed. Wiley; 2015.")
CIT_29148 = ("ISO/IEC/IEEE 29148:2018. Systems and software engineering - "
             "Life cycle processes - Requirements engineering.")
CIT_15288 = ("ISO/IEC/IEEE 15288:2015. Systems and software engineering - "
             "System life cycle processes.")
CIT_WIEGERS = ("Wiegers K, Beatty J. Software Requirements. 3rd ed. Microsoft "
               "Press; 2013.")
CIT_ROBERTSON = ("Robertson S, Robertson J. Mastering the Requirements Process: "
                 "Getting Requirements Right. 3rd ed. Addison-Wesley; 2012.")
CIT_NASA = ("NASA. NASA Systems Engineering Handbook. NASA/SP-2016-6105 Rev 2; "
            "2016.")
CIT_PMBOK = ("Project Management Institute. A Guide to the Project Management "
             "Body of Knowledge (PMBOK Guide). 7th ed.; 2021.")
CIT_SEBOK = ("INCOSE, IEEE Computer Society, Stevens Institute of Technology. "
             "Systems Engineering Body of Knowledge (SEBoK).")
CIT_IEEE830 = ("IEEE 830-1998. IEEE Recommended Practice for Software "
               "Requirements Specifications (superseded by ISO/IEC/IEEE 29148).")
CIT_HULL = ("Hull E, Jackson K, Dick J. Requirements Engineering. 3rd ed. "
            "Springer; 2011.")
CIT_SOMMERVILLE = ("Sommerville I. Software Engineering. 10th ed. Pearson; "
                   "2016.")
CIT_ULRICH = ("Ulrich KT, Eppinger SD. Product Design and Development. 7th ed. "
              "McGraw-Hill; 2019.")
CIT_BOEHM = ("Boehm BW. Software Engineering Economics. Prentice-Hall; 1981.")
CIT_MCCONNELL = ("McConnell S. Software Estimation: Demystifying the Black "
                 "Art. Microsoft Press; 2006.")
CIT_CMMI = ("CMMI Institute. CMMI for Development, Version 2.0; 2018.")
CIT_25010 = ("ISO/IEC 25010:2011. Systems and software engineering - Systems "
             "and software Quality Requirements and Evaluation (SQuaRE) - "
             "System and software quality models.")
CIT_9001 = ("ISO 9001:2015. Quality management systems - Requirements.")
CIT_J1739 = ("SAE J1739-2021. Potential Failure Mode and Effects Analysis in "
             "Design.")
CIT_IEC61025 = ("IEC 61025:2006. Fault tree analysis (FTA).")
CIT_26262 = ("ISO 26262:2018. Road vehicles - Functional safety.")
CIT_61508 = ("IEC 61508:2010. Functional safety of electrical/electronic/"
             "programmable electronic safety-related systems.")
CIT_DO178C = ("RTCA DO-178C. Software Considerations in Airborne Systems and "
              "Equipment Certification; 2011.")
CIT_SYSML = ("Object Management Group. OMG Systems Modeling Language (OMG "
             "SysML), Version 1.6; 2019.")
CIT_INCOSE_REQ = ("INCOSE. INCOSE-TP-2010-006-03. Guide for Writing "
                  "Requirements; 2019.")
CIT_MIL882 = ("MIL-STD-882E. Department of Defense Standard Practice: System "
              "Safety; 2012.")
CIT_FAGAN = ("Fagan ME. Design and code inspections to reduce errors in program "
             "development. IBM Systems Journal. 1976;15(3):182-211.")
CIT_GILB = ("Gilb T, Graham D. Software Inspection. Addison-Wesley; 1993.")

ENTRIES = [
    {
        "key": "what_is",
        "name": "What Is a Build Specification",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A build specification is the complete, structured answer to the "
            "question 'build me this' - the written contract that turns a "
            "natural-language request into something a team can actually "
            "construct, test, and sign off. It states the objective, lists the "
            "deliverables, enumerates the requirements, names the constraints, "
            "records the assumptions and dependencies, sets the acceptance "
            "criteria, and lays out the verification plan. Without it, builders "
            "guess; with it, builders measure. The specification is the single "
            "source of truth for what gets built, how well it must perform, "
            "what it must survive, and how everyone will know it is done. "
            "Systems engineers call this requirements engineering, and it is "
            "the discipline ISO/IEC/IEEE 29148:2018 standardizes. This record "
            "frames the discipline and the ladder of records that follows: "
            "from the parts of a spec, through the craft of each part, to the "
            "advanced machinery of standards, models, and manufacturing "
            "handoff."
        ),
        "how_it_works": (
            "A build specification works by replacing ambiguity with agreement "
            "before the building starts. The requester states a need in plain "
            "language; the spec author decomposes that need into verifiable "
            "statements, each one testable, each one traced, each one owned. "
            "The objective gives the why, the deliverables give the what, the "
            "requirements give the must, the constraints give the boundaries, "
            "the acceptance criteria give the proof, and the verification plan "
            "gives the procedure. When every statement is measurable, two "
            "different builders reading the same spec build the same thing - "
            "that reproducibility is the entire point. The spec then lives as "
            "the baseline: changes are proposed against it, reviewed against "
            "it, and approved or rejected by their impact on it. Standards like "
            "the INCOSE Systems Engineering Handbook and ISO/IEC/IEEE 15288 "
            "describe this as the definition phase of the system life cycle, "
            "where stakeholder needs become a system requirements baseline "
            "that the design must satisfy."
        ),
        "key_points": [
            "A build specification = objective + deliverables + requirements + constraints + assumptions/dependencies + acceptance criteria + verification plan, all written down and agreed.",
            "The core promise: two independent builders reading the same spec must build the same thing - reproducibility is the measure of a complete spec.",
            "Every requirement must be verifiable: if you cannot test it, measure it, inspect it, or demonstrate it, it is a wish, not a requirement.",
            "The spec is a living baseline, not a dead document: changes flow through review, not through hallway conversation.",
            "Standardized by ISO/IEC/IEEE 29148:2018 for requirements engineering and ISO/IEC/IEEE 15288:2015 for the system life cycle.",
        ],
        "requirements": [
            "A written objective statement that names the problem and the intended outcome in one paragraph.",
            "An enumerated deliverables list where each item has a form (document, part, software build, test report) and a recipient.",
            "Requirements written as verifiable shall-statements with unique identifiers.",
            "Named constraints: budget ceiling, schedule deadline, regulatory, physical, and interface limits.",
            "Acceptance criteria agreed before building starts, never negotiated after the build is done.",
        ],
        "standards": [
            "Requirements use shall for mandatory, will for statements of fact, and should for goals - per the INCOSE Guide for Writing Requirements.",
            "Each requirement carries a unique identifier (e.g. REQ-001) so it can be traced to design, code, tests, and acceptance.",
            "The spec cites its standards explicitly (IEEE 29148, INCOSE Handbook, project contract) so reviewers know the rules of the game.",
        ],
        "citations": [CIT_29148, CIT_INCOSE_HB, CIT_INCOSE_REQ],
        "sig_lens": (
            "The Signature read: a request is a commission and the specification "
            "is the build contract that makes the commission real. Where public "
            "standards describe requirements engineering, the Signature Build "
            "Method treats the spec as a covenant between the asker and the "
            "builder - complete means no guessing is left to anyone."
        ),
    },
    {
        "key": "request_pipeline",
        "name": "The Request-to-Specification Pipeline",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The request-to-specification pipeline is the repeatable path from "
            "a spoken or typed request to a finished build spec. It runs in "
            "stages: capture the request verbatim, extract the intent (what "
            "problem is being solved, for whom), decompose the intent into "
            "candidate objectives, elicit the hidden requirements the asker did "
            "not state, classify every statement (objective, deliverable, "
            "requirement, constraint, assumption), draft the spec, then review "
            "it back with the asker for correction. Most failed builds do not "
            "fail at building - they fail at this pipeline, because the "
            "requester said 'a fast report generator' and the builder heard "
            "something different than the requester meant. The pipeline exists "
            "to force every such phrase through extraction, decomposition, and "
            "review until the meaning is pinned down. Wiegers and Beatty call "
            "the first stage requirements elicitation; Robertson and Robertson "
            "call the review loop requirements validation. This record is the "
            "operating procedure for the whole database: every later record "
            "describes one station of this pipeline in depth."
        ),
        "how_it_works": (
            "The pipeline works like a refinery: crude request goes in, "
            "verified specification comes out. Capture records the exact "
            "words, so nothing is lost to memory. Extraction pulls the noun "
            "phrases (the things) and verb phrases (the actions) and flags "
            "vague modifiers (fast, easy, reliable) for quantification. "
            "Decomposition splits one big ask into separable objectives, each "
            "with its own deliverables. Elicitation is the interview phase - "
            "structured questions that surface what the asker assumed you "
            "knew: users, environment, volume, failure consequences, budget. "
            "Classification sorts every extracted statement into the seven "
            "spec sections so nothing lands in the wrong place. Drafting "
            "writes each statement as a verifiable shall-statement with an ID. "
            "Validation reads the draft back to the asker, section by section, "
            "and the asker's corrections become the first formal change "
            "requests. A pipeline run is done when the asker can sign the "
            "statement 'this is what I meant' - that signature is the "
            "acceptance of the requirements baseline."
        ),
        "key_points": [
            "Stages: capture -> extract -> decompose -> elicit -> classify -> draft -> validate; a request becomes a spec only after surviving all seven.",
            "Vague modifiers (fast, easy, robust) are flagged at extraction and must be quantified before drafting - unquantified words never become requirements.",
            "Validation is a read-back with the asker, not a silent handoff: the asker signs the baseline only after correcting it.",
            "Failed builds usually fail at this pipeline: most defects trace to misunderstood, missing, or unstated requirements, not to bad implementation.",
            "The pipeline is repeatable by design - the same steps turn any request, in any domain, into a structured spec.",
        ],
        "requirements": [
            "The verbatim request text, preserved before any interpretation, so later disputes can be settled.",
            "An extraction pass that lists nouns, verbs, and every vague modifier with a flag for quantification.",
            "An elicitation question set covering users, environment, volume, constraints, failure consequences, and budget.",
            "A classification of every statement into objective, deliverable, requirement, constraint, assumption, dependency, or acceptance criterion.",
            "A validation read-back where the asker corrects the draft and the corrections are logged as the first change requests.",
        ],
        "standards": [
            "Elicitation follows structured techniques per Wiegers and Beatty: interviews, workshops, document analysis, prototyping.",
            "Validation produces a signed requirements baseline per ISO/IEC/IEEE 29148 before design begins.",
            "Every correction during validation is logged with its reason, so the spec history shows how the baseline was reached.",
        ],
        "citations": [CIT_WIEGERS, CIT_ROBERTSON, CIT_29148],
        "sig_lens": (
            "The Signature read: the pipeline is the Signature Build Method in "
            "motion - capture is hearing the commission, extraction is "
            "weighing it, and validation is the handshake that seals the "
            "contract. Nothing in the Signature method is ever built from an "
            "unexamined sentence."
        ),
    },
    {
        "key": "anatomy",
        "name": "Anatomy of a Complete Build Specification",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Every complete build specification has the same skeleton, "
            "regardless of domain: header and identification (title, version, "
            "owner, date), objective, stakeholders, deliverables, functional "
            "requirements, non-functional requirements, constraints, "
            "assumptions and dependencies, interface specifications, "
            "acceptance criteria, verification plan, risk register, glossary, "
            "and change history. The order is deliberate: readers meet the why "
            "(objective) before the what (deliverables), the what before the "
            "must (requirements), and the must before the proof "
            "(acceptance and verification). A spec missing any section is "
            "incomplete by definition - the missing section is the place where "
            "the next dispute will start. This record is the map of that "
            "skeleton: what each section contains, who writes it, who reads "
            "it, and what goes wrong when it is absent. IEEE 830-1998 gave the "
            "classic software version of this outline; ISO/IEC/IEEE 29148 "
            "generalized it across systems and software."
        ),
        "how_it_works": (
            "The anatomy works as a checklist that the spec author walks "
            "top to bottom. The header identifies the document so versions "
            "cannot be confused - title, ID, version, author, approver, date. "
            "The objective states the problem and the intended outcome in "
            "plain language that a non-engineer can judge. Stakeholders name "
            "every party with a say, so nobody discovers the build too late. "
            "Deliverables enumerate the concrete outputs, each with form and "
            "recipient. Functional requirements state what the system must "
            "do; non-functional requirements state how well, how fast, how "
            "safe, how reliably. Constraints bound the solution space. "
            "Assumptions record what is believed true; dependencies record "
            "what must exist first. Interfaces pin down every boundary the "
            "build touches. Acceptance criteria state the exact conditions for "
            "sign-off. The verification plan assigns a method - test, "
            "analysis, inspection, demonstration - to every requirement. The "
            "risk register lists what could still go wrong. The glossary "
            "defines every domain term. The change history proves the "
            "document evolved on purpose. Walk the skeleton in order and the "
            "spec writes itself; skip a bone and the body cannot stand."
        ),
        "key_points": [
            "The skeleton: header, objective, stakeholders, deliverables, functional reqs, non-functional reqs, constraints, assumptions/dependencies, interfaces, acceptance criteria, verification plan, risks, glossary, change history.",
            "Order matters: why -> what -> must -> boundaries -> proof; readers should never meet a requirement before they know the objective it serves.",
            "A missing section is a future dispute: every gap in the anatomy is a place where builders will guess and askers will disagree.",
            "Each section has a primary author and primary reader: stakeholders name people, interfaces name systems, verification names testers.",
            "The glossary and change history are not filler - they prevent term drift and prove the baseline evolved deliberately.",
        ],
        "requirements": [
            "A header block with document ID, version, author, approver, and date, unique across the project.",
            "All fourteen sections present in order, each with at least its core content or an explicit not-applicable justification.",
            "A glossary defining every domain term and acronym used anywhere in the spec.",
            "A change history table recording version, date, author, and reason for every baseline change.",
        ],
        "standards": [
            "Section layout follows the IEEE 830-1998 software requirements outline generalized by ISO/IEC/IEEE 29148.",
            "Document identification and version control follow the project configuration management plan per ISO/IEC/IEEE 15288.",
        ],
        "citations": [CIT_IEEE830, CIT_29148, CIT_15288],
        "sig_lens": (
            "The Signature read: the skeleton is the contract form itself - "
            "fourteen chambers, each one sealing a different promise. The "
            "Signature Build Method inspects the anatomy first: a request "
            "cannot become a commission until every chamber of the contract "
            "has its content."
        ),
    },
    {
        "key": "objectives",
        "name": "Writing Objectives That Mean Something",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "The objective is the one-paragraph answer to 'why are we "
            "building this' - the problem, the people it hurts, and the "
            "outcome that proves the hurt is gone. A meaningful objective is "
            "specific (names the problem and the population), measurable "
            "(names the number that must move), achievable (within the stated "
            "constraints), relevant (tied to a real stakeholder need), and "
            "time-bound (names the horizon) - the SMART test, applied to "
            "builds. 'Make reporting better' fails every letter; 'cut the "
            "monthly close report from 6 hours of manual work to under 15 "
            "minutes of automated generation by Q3, for the 40-person finance "
            "team' passes all five. The objective is written first and judged "
            "last: every requirement below it must trace upward to it, and "
            "any requirement that does not serve it is scope creep wearing a "
            "costume. This record teaches the extraction of objectives from "
            "vague requests and the SMART test that keeps them honest."
        ),
        "how_it_works": (
            "Writing objectives works by interrogation. Start from the "
            "requester's first sentence and ask: what problem does this "
            "solve, for whom, and what does the world look like when it is "
            "solved? Write the answer as a single paragraph with a number in "
            "it - time saved, cost cut, failures prevented, users served. "
            "Then run the SMART test, letter by letter: is the problem named "
            "specifically, is the target measurable, is it achievable under "
            "the stated budget and schedule, is it relevant to a named "
            "stakeholder, is the horizon dated? Each failing letter becomes a "
            "question back to the requester. When the paragraph passes all "
            "five, freeze it: the objective becomes the anchor that every "
            "later requirement must tie to. During review, read each "
            "requirement and ask 'which objective does this serve?' - orphans "
            "get cut or the objective gets amended, deliberately, in the "
            "change log. The objective never changes silently; a changed "
            "objective is a changed project."
        ),
        "key_points": [
            "A meaningful objective: the problem, the people it hurts, the measurable outcome, the horizon - in one paragraph with a number in it.",
            "SMART test: Specific, Measurable, Achievable, Relevant, Time-bound - each failing letter becomes a question back to the requester.",
            "The objective is the traceability root: every requirement must serve it; orphan requirements are scope creep.",
            "Written first, judged last: freeze the objective early, and change it only through the formal change process.",
            "One number beats ten adjectives: 'under 15 minutes by Q3' replaces 'fast' forever.",
        ],
        "requirements": [
            "One paragraph naming the problem, the affected population, and the intended outcome.",
            "At least one measurable target with a unit and a deadline (time, cost, error rate, capacity).",
            "A documented SMART self-test showing all five letters satisfied, or the open questions returned to the requester.",
            "Traceability links from the objective to every top-level requirement it spawns.",
        ],
        "standards": [
            "Objectives are validated against stakeholder needs per ISO/IEC/IEEE 15288 stakeholder requirements definition process.",
            "Measurable targets use defined units and baselines so achievement can be verified, per ISO/IEC/IEEE 29148.",
        ],
        "citations": [CIT_15288, CIT_ROBERTSON, CIT_29148],
        "sig_lens": (
            "The Signature read: the objective is the destination written on "
            "the commission - the one paragraph the whole contract serves. "
            "The Signature Build Method refuses to start from adjectives; the "
            "destination must be a number, a date, and a name, or it is not "
            "a destination."
        ),
    },
    {
        "key": "deliverables",
        "name": "Deliverables: Defining What Done Looks Like",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Deliverables are the concrete outputs the build must produce - "
            "the documents, parts, software builds, test reports, and trained "
            "artifacts that the requester can hold, run, or file. Each "
            "deliverable is defined by four things: its form (what it is), "
            "its content (what is inside), its acceptance test (how it will "
            "be judged), and its recipient (who receives it). A deliverable "
            "without an acceptance test is a hope; without a recipient it is "
            "a paperweight. The deliverables list is also the project's "
            "progress instrument: percent complete is measured against "
            "delivered and accepted items, never against hours spent. Common "
            "failure modes include listing activities as deliverables ('do "
            "testing' instead of 'test report v1.0'), listing the same item "
            "twice under different names, and promising deliverables whose "
            "acceptance tests are invented after delivery. This record sets "
            "the definition-of-done discipline that makes the deliverables "
            "list enforceable."
        ),
        "how_it_works": (
            "Deliverables work as the contract's cargo manifest. For each "
            "item, the author writes: the name, the form (PDF document, machined "
            "part, container image, signed test report), the contents (chapter "
            "list, bill of materials, feature set, test coverage), the "
            "acceptance test (which record's acceptance criteria apply), and "
            "the recipient and due date. Then the definition-of-done is "
            "applied: a deliverable is done only when it exists in its stated "
            "form, passes its acceptance test, is handed to its recipient, "
            "and is recorded in the change log. Progress is then arithmetic: "
            "delivered-and-accepted items divided by total items. Activities "
            "are struck from the list - testing is not a deliverable, the "
            "test report is. Reviews check for duplicates (same item, two "
            "names) and for orphans (a deliverable with no acceptance test "
            "borrows the criteria from its parent objective). The manifest "
            "freezes at baseline; adding a deliverable is a change request, "
            "not a hallway promise."
        ),
        "key_points": [
            "Each deliverable = form + content + acceptance test + recipient + due date; missing any one makes it unenforceable.",
            "Definition of done: exists in stated form, passes its acceptance test, handed to its recipient, logged - all four, no exceptions.",
            "Progress = accepted deliverables / total deliverables - never hours spent, never lines written.",
            "Activities are not deliverables: 'do testing' becomes 'test report v1.0 signed by the test lead'.",
            "Duplicate names and orphan deliverables (no acceptance test) are caught at review, not at delivery time.",
        ],
        "requirements": [
            "An enumerated manifest where each item states form, content summary, acceptance test reference, recipient, and due date.",
            "A written definition of done applied uniformly to every item on the manifest.",
            "No activity entries: every line on the manifest must name a thing that can be handed over.",
            "An acceptance test reference for every deliverable, traceable to the acceptance criteria section.",
        ],
        "standards": [
            "Deliverable acceptance follows the verification and validation processes of ISO/IEC/IEEE 15288.",
            "Configuration identification of each deliverable follows the project configuration management plan.",
        ],
        "citations": [CIT_15288, CIT_PMBOK, CIT_29148],
        "sig_lens": (
            "The Signature read: deliverables are the promised cargo of the "
            "build contract - named, counted, and sealed. The Signature Build "
            "Method measures progress by cargo delivered and accepted, never "
            "by effort spent; a builder is paid for cargo, not for sweat."
        ),
    },
    {
        "key": "functional_req",
        "name": "Functional Requirements: What the System Must Do",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Functional requirements state what the system must do - its "
            "behaviors, its functions, its responses to inputs. 'The system "
            "shall authenticate users with a username and password' is "
            "functional; 'the system shall authenticate in under 2 seconds' "
            "is its non-functional shadow. Each functional requirement gets a "
            "unique ID (REQ-001, REQ-002), a single shall-statement, a "
            "rationale (why it exists), a source (who asked for it), and a "
            "verification method (how it will be proven). One statement, one "
            "behavior: compound requirements ('shall sort and filter and "
            "export') are split until each ID names one testable action. The "
            "classic sins are vagueness ('shall be user-friendly'), "
            "unverifiability ('shall handle all inputs gracefully'), and "
            "design prescription disguised as a requirement ('shall use a "
            "relational database' states a solution, not a need). This record "
            "is the craft of writing functional requirements that survive "
            "contact with testers."
        ),
        "how_it_works": (
            "Functional requirements work by enumeration of behavior. The "
            "author walks each use case and writes one shall-statement per "
            "observable action: inputs named, outputs named, triggering "
            "conditions named. Each gets a unique ID in a single sequence so "
            "no two share a number and no number is skipped without a logged "
            "reason. The statement is then tested against the "
            "well-formedness rules: single subject, single verb, measurable "
            "outcome, no adjectives that a tester cannot check. Rationale is "
            "recorded in a separate field - the requirement says what, the "
            "rationale says why, and the two never mix, so that when the why "
            "changes the what can be renegotiated honestly. Source is "
            "recorded so disputes have an owner. Verification method is "
            "assigned at writing time (test, demonstration, inspection, "
            "analysis), because a requirement whose proof is unknown is a "
            "requirement that will not be proven. Reviews then hunt the sins: "
            "vague terms get quantified or cut, compound statements get "
            "split, design prescriptions get rewritten as needs."
        ),
        "key_points": [
            "One requirement = one ID + one shall-statement + one behavior; compound statements are split until each names a single testable action.",
            "Anatomy of the record: ID, shall-statement, rationale, source, verification method - what, why, who, and how it will be proven.",
            "Vague terms (fast, user-friendly, robust) and design prescriptions (use technology X) are rewritten or cut at review.",
            "Rationale lives in its own field: when the why changes, the what is renegotiated instead of silently reinterpreted.",
            "Verification method is assigned at writing time - test, demonstration, inspection, or analysis - never left for later.",
        ],
        "requirements": [
            "Unique sequential IDs (REQ-001...) with no gaps except logged deletions.",
            "Single-verb shall-statements with named inputs, outputs, and triggering conditions.",
            "Separate rationale and source fields for every requirement.",
            "A verification method assigned to every requirement at the time of writing.",
        ],
        "standards": [
            "Well-formedness rules per the INCOSE Guide for Writing Requirements: singular, verifiable, unambiguous, complete.",
            "Requirements management and traceability per ISO/IEC/IEEE 29148 and the CMMI requirements management process area.",
        ],
        "citations": [CIT_INCOSE_REQ, CIT_29148, CIT_CMMI],
        "sig_lens": (
            "The Signature read: functional requirements are the load-bearing "
            "beams of the build contract - each one carries exactly one "
            "behavior, numbered and measured. The Signature Build Method "
            "splits every compound beam until each carries a single load, "
            "because a beam carrying three loads breaks at the joint."
        ),
    },
    {
        "key": "nonfunctional_req",
        "name": "Non-Functional Requirements: How Well It Must Do It",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Non-functional requirements state how well the system must do "
            "what it does - its performance, reliability, safety, security, "
            "usability, maintainability, and portability. They are the "
            "adjectives made measurable: 'the login shall complete within 2 "
            "seconds for 95 percent of attempts under a load of 1,000 "
            "concurrent users' replaces 'the login shall be fast'. The "
            "standard taxonomy is ISO/IEC 25010, which organizes quality into "
            "eight characteristics: functional suitability, performance "
            "efficiency, compatibility, usability, reliability, security, "
            "maintainability, and portability. Every non-functional "
            "requirement needs three things the functional ones do not always "
            "need: a metric, a target value with a unit, and the conditions "
            "under which it is measured (load, environment, data volume). "
            "Without conditions, the numbers are fiction; without metrics, "
            "the adjectives return. This record covers the taxonomy, the "
            "measurement discipline, and the trade-off negotiations these "
            "requirements always trigger."
        ),
        "how_it_works": (
            "Non-functional requirements work by attaching measurable quality "
            "targets to the behaviors the functional requirements describe. "
            "For each functional requirement, the author asks the quality "
            "questions: how fast (performance efficiency), how often may it "
            "fail (reliability), who may use it and how is it protected "
            "(security), how hard is it to learn (usability), how hard is it "
            "to change (maintainability), where must it run (portability, "
            "compatibility). Each answer becomes a shall-statement with a "
            "metric, a target, and measurement conditions: 'mean time between "
            "failures shall exceed 5,000 operating hours at 40 degrees C "
            "ambient'. Conditions are negotiated with the stakeholders who "
            "will run the tests, because a target without agreed conditions "
            "is a future argument. Trade-offs are then made explicit: "
            "performance against cost, security against usability, "
            "reliability against time to market - each trade recorded with "
            "its decision and its decider. The requirements are organized by "
            "the ISO/IEC 25010 characteristics so reviewers can see which "
            "qualities are specified and which were forgotten."
        ),
        "key_points": [
            "Every non-functional requirement = metric + target with unit + measurement conditions; adjectives without numbers are not requirements.",
            "ISO/IEC 25010 taxonomy: functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability.",
            "Conditions are negotiated with whoever runs the tests: a target without agreed conditions is a future dispute.",
            "Trade-offs are recorded with the decision and the decider: performance vs cost, security vs usability, reliability vs schedule.",
            "The taxonomy doubles as a completeness check: an empty quality characteristic is a question, not an answer.",
        ],
        "requirements": [
            "Coverage of all eight ISO/IEC 25010 quality characteristics, each with at least a considered statement or an explicit not-applicable rationale.",
            "A metric, a target value with units, and measurement conditions for every non-functional requirement.",
            "Documented trade-off decisions with the decider named for every conflict between quality targets.",
        ],
        "standards": [
            "Quality characteristics per ISO/IEC 25010:2011.",
            "Security requirements aligned with the project's security policy and applicable standards.",
        ],
        "citations": [CIT_25010, CIT_29148, CIT_WIEGERS],
        "sig_lens": (
            "The Signature read: non-functional requirements are the finish "
            "and the temper of the build - the beams carry the load, but the "
            "temper decides how the structure behaves in heat, in storm, and "
            "in time. The Signature Build Method tempers every beam with a "
            "number, because untempered promises are the first to break."
        ),
    },
    {
        "key": "constraints",
        "name": "Constraints: Budget, Time, Physics, and Law",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Constraints are the boundaries the build must stay inside: the "
            "budget ceiling, the schedule deadline, the physical limits, the "
            "regulatory rules, the interface mandates, and the technology "
            "mandates. Unlike requirements, constraints are not negotiated "
            "with the design - they are given, and the design must fit. A "
            "complete constraints section names each boundary with its number "
            "('total budget shall not exceed 250,000 dollars'), its source "
            "(who set it), and its flexibility (hard limits vs negotiable "
            "targets). The five families are business constraints (budget, "
            "schedule, staffing), physical constraints (size, weight, power, "
            "environment), regulatory constraints (safety law, emissions, "
            "data rules), interface constraints (must connect to system X "
            "using protocol Y), and technology constraints (must run on the "
            "existing platform). Missing constraints are discovered by "
            "failure: the build that assumed a bigger budget, a later "
            "deadline, or a friendlier regulator. This record teaches the "
            "constraint inventory that keeps designs inside reality."
        ),
        "how_it_works": (
            "Constraints work by shrinking the solution space before design "
            "begins. The author interviews each authority that can say no: "
            "finance for the budget, the calendar for the deadline, physics "
            "for the envelope, the regulator for the law, the neighboring "
            "systems for the interfaces, and the platform team for the "
            "technology mandate. Each boundary is written as a constraint "
            "statement with a number, a unit, a source, and a flexibility "
            "tag: hard (violation kills the project), firm (violation needs "
            "executive approval), or target (violation needs a documented "
            "trade). The constraints are then checked against the objectives "
            "and requirements for consistency - an objective demanding a 3-"
            "month delivery against a 6-month constraint is a contradiction "
            "to resolve now, not a surprise to discover later. During "
            "design, every candidate solution is screened against the hard "
            "constraints first; anything outside them is discarded without "
            "further analysis. The constraints section is re-validated at "
            "each phase gate, because budgets shrink, laws change, and "
            "platforms get replaced."
        ),
        "key_points": [
            "Five families: business (budget, schedule, staffing), physical (size, weight, power, environment), regulatory (law, safety, data), interface (must connect to X via Y), technology (must run on platform Z).",
            "Each constraint = number + unit + source + flexibility tag: hard, firm, or target.",
            "Constraints are checked against objectives for contradiction before design starts - a 3-month objective against a 6-month constraint is resolved now.",
            "Design candidates are screened against hard constraints first; outside the boundary means discarded, not debated.",
            "Re-validated at every phase gate: budgets shrink, laws change, platforms get replaced.",
        ],
        "requirements": [
            "An inventory covering all five constraint families, each with number, unit, source, and flexibility tag.",
            "A consistency check between constraints and objectives, with contradictions resolved and logged.",
            "Named authorities for each constraint: who can grant an exception and at what cost.",
        ],
        "standards": [
            "Design constraints documented per ISO/IEC/IEEE 29148 as part of the system requirements specification.",
            "Regulatory constraints traced to the specific statute, regulation, or standard that imposes them.",
        ],
        "citations": [CIT_29148, CIT_NASA, CIT_15288],
        "sig_lens": (
            "The Signature read: constraints are the walls of the building "
            "site - the commission is real only inside them. The Signature "
            "Build Method walks every wall before drawing a single line, and "
            "tags each wall hard, firm, or target, because a wall mistaken "
            "for a suggestion collapses the whole contract."
        ),
    },
    {
        "key": "assumptions",
        "name": "Assumptions, Dependencies, and External Interfaces",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Assumptions are the things the spec believes true without "
            "proof: 'the warehouse Wi-Fi covers the loading dock', 'the "
            "vendor API stays at version 2', 'the user has a smartphone'. "
            "Dependencies are the things that must exist before the build "
            "can proceed: parts, data, access, decisions, other projects. "
            "External interfaces are the boundaries the build touches: APIs, "
            "file formats, hardware connectors, human handoffs. These three "
            "sections are where silent failures breed, because every "
            "unstated assumption is a bet the project did not know it "
            "placed. The discipline is simple: write every assumption down "
            "with its owner and its validation date, map every dependency "
            "with its provider and its delivery date, and specify every "
            "external interface with its owner and its version. An assumption "
            "validated is a risk retired; an assumption forgotten is a "
            "surprise with a schedule attached. This record covers the "
            "assumption log, the dependency map, and the interface register."
        ),
        "how_it_works": (
            "Assumptions, dependencies, and interfaces work as the spec's "
            "reality anchors. The author extracts them during elicitation by "
            "asking 'what are we counting on?' after every requirement. Each "
            "assumption gets an ID (ASM-001), the statement, the owner who "
            "believes it, the impact if it is wrong, and a validation date "
            "by which it must be confirmed or converted into a requirement. "
            "Each dependency gets an ID (DEP-001), the needed item, the "
            "provider, the need-by date, and the fallback if it slips. The "
            "dependency map is then checked for cycles - A waiting on B "
            "waiting on A is a deadlock to break now, not a schedule to "
            "discover later - and topologically ordered so the build sequence "
            "is visible. Each external interface gets an ID (IF-001), the "
            "boundary description, the owning party, the protocol or format "
            "with its version, and the change-notification promise. Reviews "
            "attack the lists for the dangerous kind: the assumption everyone "
            "believed so strongly that nobody wrote it down. Those get "
            "written down, owned, and dated like all the rest."
        ),
        "key_points": [
            "Assumptions: ID, statement, owner, impact-if-wrong, validation date - an assumption validated is a risk retired.",
            "Dependencies: ID, needed item, provider, need-by date, fallback - mapped and checked for cycles before scheduling.",
            "External interfaces: ID, boundary, owner, protocol/format with version, change-notification promise.",
            "The dangerous assumptions are the unwritten ones: reviews hunt for what everyone believed but nobody recorded.",
            "Dependencies are topologically ordered so the build sequence is visible and deadlocks surface early.",
        ],
        "requirements": [
            "An assumption log with owner and validation date for every material assumption.",
            "A dependency map with provider, need-by date, and fallback for every external dependency, verified cycle-free.",
            "An interface register naming every external boundary with its owner and versioned protocol or format.",
        ],
        "standards": [
            "Interface requirements specified per ISO/IEC/IEEE 29148 with both sides of each interface identified.",
            "External interface control follows the project's interface management process per ISO/IEC/IEEE 15288.",
        ],
        "citations": [CIT_29148, CIT_15288, CIT_WIEGERS],
        "sig_lens": (
            "The Signature read: assumptions are the unsealed bets of the "
            "contract, dependencies its supply lines, interfaces its property "
            "fences. The Signature Build Method seals every bet with an owner "
            "and a date, maps every supply line for deadlocks, and walks "
            "every fence with its neighbor before building."
        ),
    },
    {
        "key": "acceptance",
        "name": "Acceptance Criteria: The Rules of Sign-Off",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Acceptance criteria are the exact conditions under which the "
            "requester agrees the build is done and pays for it. They are "
            "written before building starts, in language both parties sign, "
            "and they answer the question 'how will we know?' for every "
            "deliverable and every critical requirement. Good criteria are "
            "binary (pass or fail, no partial credit), observable (a witness "
            "can see the result), and pre-agreed (negotiated before the "
            "build, not after). The classic form is given-when-then: given a "
            "stated precondition, when a stated action occurs, then a stated "
            "observable result follows. Bad criteria are subjective ('works "
            "well'), movable ('we will know it when we see it'), or invented "
            "after delivery. The acceptance section also names the acceptance "
            "process: who runs the tests, who witnesses, how failures are "
            "handled, and how many retries are allowed. This record is the "
            "sign-off discipline that turns delivery into acceptance."
        ),
        "how_it_works": (
            "Acceptance criteria work as the finish line painted before the "
            "race. For each deliverable, the author writes criteria in "
            "given-when-then form with numbers wherever the requirement has "
            "numbers: 'given 1,000 concurrent users, when the login storm "
            "runs for 10 minutes, then 95 percent of logins complete within "
            "2 seconds and zero data is lost'. Each criterion is checked for "
            "the three properties: binary (a judge can call pass or fail "
            "without debate), observable (the result can be witnessed or "
            "logged), and pre-agreed (both parties signed before building). "
            "The acceptance process is then specified: the test environment, "
            "the operators, the witnesses, the data to be recorded, the "
            "definition of a failure, the retry policy, and the escalation "
            "path for disputes. At delivery, the criteria are executed in "
            "order, results are logged against each criterion, and sign-off "
            "happens only when every criterion passes or its failure is "
            "formally waived with a recorded reason. No new criteria may be "
            "invented at acceptance time - that is renegotiation, and it "
            "goes through the change process."
        ),
        "key_points": [
            "Every criterion is binary, observable, and pre-agreed: pass or fail, witnessable, signed before building.",
            "Given-when-then form with numbers: precondition, action, observable result - no adjectives, no partial credit.",
            "The acceptance process is specified too: environment, operators, witnesses, logging, retry policy, dispute path.",
            "Sign-off requires every criterion passed or formally waived with a recorded reason.",
            "No new criteria at acceptance time: invented-after-delivery criteria are renegotiation, routed through change control.",
        ],
        "requirements": [
            "Given-when-then acceptance criteria for every deliverable and every critical requirement.",
            "A written acceptance process naming environment, operators, witnesses, failure handling, and retry policy.",
            "A sign-off record where each criterion shows pass, fail, or formal waiver with reason.",
        ],
        "standards": [
            "Acceptance criteria derived from stakeholder requirements per ISO/IEC/IEEE 15288 validation process.",
            "Testable criteria format consistent with ISO/IEC/IEEE 29148 verification requirements.",
        ],
        "citations": [CIT_15288, CIT_29148, CIT_ROBERTSON],
        "sig_lens": (
            "The Signature read: acceptance criteria are the final "
            "inspection stamp of the build contract - the exact marks the "
            "work must bear before the commission is paid. The Signature "
            "Build Method paints the finish line before the race starts, and "
            "no stamp is ever issued for a line painted after the finish."
        ),
    },
    {
        "key": "verification",
        "name": "Verification Plans: Proving the Build",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The verification plan proves the build matches the spec: every "
            "requirement gets a method (test, analysis, inspection, or "
            "demonstration), a procedure, a pass threshold, and an owner. "
            "Test means exercising the system and measuring the result; "
            "analysis means calculating or simulating it; inspection means "
            "examining the artifact against a checklist; demonstration means "
            "operating it and observing the outcome. The plan is organized "
            "as a verification matrix: rows are requirements, columns are "
            "the methods, and every row must have at least one filled "
            "column. Coverage is the headline metric: verified requirements "
            "divided by total requirements, tracked until it reaches 100 "
            "percent. Unverifiable requirements are the plan's natural "
            "enemy - each one is either rewritten until it is verifiable or "
            "cut with a logged reason. This record covers the four methods, "
            "the matrix, the coverage discipline, and the difference between "
            "verification (did we build it right) and validation (did we "
            "build the right thing)."
        ),
        "how_it_works": (
            "The verification plan works by assigning proof to every "
            "requirement at writing time. For each requirement ID, the "
            "author chooses the cheapest sufficient method: test for "
            "behavior under conditions, analysis for derived properties "
            "like stress or timing budgets, inspection for documents and "
            "code against checklists, demonstration for observable "
            "operations. The procedure is then sketched: what setup, what "
            "inputs, what measurements, what pass threshold with its "
            "numbers. Each assignment gets an owner and a phase (unit, "
            "integration, system, acceptance). The matrix is built - "
            "requirement rows, method columns - and coverage is computed: "
            "any row without a method is a gap to close, not a detail to "
            "defer. As verification executes, results are logged per "
            "requirement: pass, fail with defect ID, or waived with reason. "
            "Coverage is re-computed at each phase gate until it reads 100 "
            "percent of applicable requirements. Verification answers 'did "
            "we build it right' (against the spec); validation answers 'did "
            "we build the right thing' (against the stakeholder need) - the "
            "plan covers the first, and the acceptance criteria cover the "
            "second."
        ),
        "key_points": [
            "Four methods: test (exercise and measure), analysis (calculate or simulate), inspection (examine against a checklist), demonstration (operate and observe).",
            "The verification matrix: one row per requirement, one column per method - every row must have at least one filled cell.",
            "Coverage = verified requirements / total requirements, tracked to 100 percent at each phase gate.",
            "Verification = built it right (against the spec); validation = built the right thing (against the stakeholder need).",
            "Unverifiable requirements are rewritten or cut with a logged reason - never carried as dead weight.",
        ],
        "requirements": [
            "A verification method, procedure sketch, pass threshold, owner, and phase for every requirement.",
            "A verification matrix with zero empty rows at baseline.",
            "Coverage tracking to 100 percent of applicable requirements, recomputed at each phase gate.",
        ],
        "standards": [
            "Verification and validation processes per ISO/IEC/IEEE 15288; verification methods per ISO/IEC/IEEE 29148.",
            "Test documentation organized per IEEE 829 test documentation concepts where the project requires it.",
        ],
        "citations": [CIT_15288, CIT_29148, CIT_NASA],
        "sig_lens": (
            "The Signature read: the verification plan is the proof ledger "
            "of the build contract - every beam gets its load test, every "
            "promise its witness. The Signature Build Method assigns the "
            "proof at the moment the promise is written, because a promise "
            "with no appointed witness is a promise already broken."
        ),
    },
    {
        "key": "stakeholders",
        "name": "Stakeholder Mapping and Requirements Elicitation",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Stakeholders are everyone with a say in the build: the "
            "requester who pays, the users who operate, the operators who "
            "maintain, the regulators who approve, the neighbors the build "
            "affects, and the adversaries who will test it. Stakeholder "
            "mapping finds them all, classifies them by power and interest, "
            "and assigns each an elicitation strategy: collaborate with the "
            "high-power high-interest players, satisfy the high-power "
            "low-interest ones, keep the low-power high-interest informed, "
            "and monitor the rest. Requirements elicitation is the structured "
            "extraction of needs from these people - interviews, workshops, "
            "document analysis, observation, prototyping - chosen per "
            "stakeholder, never one-size-fits-all. The classic failure is "
            "the missing stakeholder: the build is finished, and someone "
            "with veto power appears for the first time. This record covers "
            "the map, the grid, the elicitation techniques, and the "
            "sign-off that closes elicitation."
        ),
        "how_it_works": (
            "Stakeholder mapping works by systematic discovery. The author "
            "starts from the requester and asks 'who else is affected, who "
            "else decides, who else pays, who else maintains, who else "
            "regulates' until the list stops growing, then checks the usual "
            "blind spots: operations, support, security, legal, and the "
            "people downstream of the output. Each stakeholder is placed on "
            "the power-interest grid, which dictates the engagement strategy "
            "and the elicitation technique: workshops for the collaborative "
            "quadrant, structured interviews for the powerful-but-distant, "
            "surveys and prototypes for the broad user base. Elicitation "
            "sessions are planned with objectives and questions, run with "
            "note-takers, and followed by written summaries the stakeholder "
            "corrects - the correction is the validation. Conflicts between "
            "stakeholders are surfaced deliberately in joint workshops, "
            "where the trade is negotiated and the decision recorded with "
            "its decider. Elicitation closes with a stakeholder sign-off on "
            "the extracted needs, which become the input to requirements "
            "writing. The map is revisited at each phase gate, because "
            "stakeholders change jobs, companies merge, and regulators "
            "update their rules."
        ),
        "key_points": [
            "Discovery question: who is affected, who decides, who pays, who maintains, who regulates - plus the blind spots: operations, support, security, legal, downstream users.",
            "Power-interest grid sets the strategy: collaborate, satisfy, inform, monitor - matched with the right elicitation technique per quadrant.",
            "Every elicitation session ends with a written summary the stakeholder corrects; the correction is the validation.",
            "Conflicts are surfaced in joint workshops and resolved with the trade, the decision, and the decider all recorded.",
            "Elicitation closes with stakeholder sign-off; the map is revisited at every phase gate.",
        ],
        "requirements": [
            "A stakeholder register naming every stakeholder with role, power-interest classification, and engagement strategy.",
            "Documented elicitation sessions per key stakeholder with objectives, notes, and stakeholder-corrected summaries.",
            "A conflict log recording every inter-stakeholder conflict with its resolution, trade, and decider.",
            "Stakeholder sign-off on the extracted needs before requirements writing begins.",
        ],
        "standards": [
            "Stakeholder needs and requirements definition per ISO/IEC/IEEE 15288.",
            "Elicitation techniques per Wiegers and Beatty, selected per stakeholder class.",
        ],
        "citations": [CIT_15288, CIT_WIEGERS, CIT_ROBERTSON],
        "sig_lens": (
            "The Signature read: stakeholders are the signatories of the "
            "build contract, and elicitation is taking each signature in "
            "turn. The Signature Build Method finds every signatory before "
            "the first line is drawn, because a contract signed by half its "
            "parties is a dispute with a cover page."
        ),
    },
    {
        "key": "scope",
        "name": "Scope Control: Change Requests and Creep",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Scope is the agreed boundary of the build: what is in, what is "
            "out, and what would count as a change. Scope control is the "
            "machinery that keeps that boundary honest - the change request "
            "process, the impact analysis, the approval board, and the "
            "discipline of saying no. Scope creep is the slow, friendly "
            "erosion of the boundary: each small addition seems reasonable, "
            "and together they sink the schedule. The defense is procedural: "
            "every proposed change gets a written request with its reason, "
            "an impact analysis on cost, schedule, and risk, and a decision "
            "by the named authority - approved, rejected, or deferred - all "
            "logged. The spec's out-of-scope list is as important as its "
            "requirements: explicitly excluded items cannot creep back in "
            "through misunderstanding. This record covers the change process, "
            "impact analysis, the change control board, and the psychology "
            "of the polite no."
        ),
        "how_it_works": (
            "Scope control works as a toll gate on the baseline. Anyone may "
            "propose a change, but the proposal must be written: what "
            "changes, why, and what happens if it does not. The analyst then "
            "scores the impact on the three project dimensions - cost delta, "
            "schedule delta, risk delta - plus the requirements it touches "
            "and the tests that must be re-run. The change control board, "
            "with its named members and its authority limits, reviews the "
            "scored request against the current baseline and decides: "
            "approve (the baseline moves, with the new version logged), "
            "reject (logged with the reason, so it is not proposed again "
            "next month), or defer (parked for a later phase with its "
            "impact preserved). Emergency changes follow a fast-track path "
            "with retroactive review, so urgency never becomes an excuse for "
            "anarchy. The out-of-scope list is consulted at every review: "
            "items on it are rejected by reference, quickly and without "
            "drama. Metrics are kept - request volume, approval rate, "
            "average impact - because a rising change rate is the early "
            "warning that the baseline was wrong."
        ),
        "key_points": [
            "Every change = written request + impact analysis (cost, schedule, risk) + board decision (approve, reject, defer) + log entry.",
            "Impact is scored on cost delta, schedule delta, and risk delta, plus touched requirements and re-run tests.",
            "The out-of-scope list is the fast-reject path: excluded items are refused by reference, without drama.",
            "Emergency changes use a fast-track path with retroactive review - urgency is never an excuse for anarchy.",
            "Change metrics (volume, approval rate, average impact) are the early warning that the baseline was wrong.",
        ],
        "requirements": [
            "A change request form capturing what, why, and what-if-not for every proposed change.",
            "An impact analysis scoring cost, schedule, and risk deltas before any decision.",
            "A named change control board with documented authority limits and decision records.",
            "An explicit out-of-scope list in the spec, consulted at every review.",
        ],
        "standards": [
            "Change control per the project configuration management plan, aligned with ISO/IEC/IEEE 15288.",
            "Scope management processes per the PMBOK Guide scope management knowledge area.",
        ],
        "citations": [CIT_PMBOK, CIT_15288, CIT_WIEGERS],
        "sig_lens": (
            "The Signature read: scope is the fence around the building "
            "site, and change control is the gate with its keeper. The "
            "Signature Build Method lets anyone knock, but nobody enters "
            "without the toll paid in writing - cost, schedule, and risk - "
            "because a fence with no gate is just a suggestion."
        ),
    },
    {
        "key": "traceability",
        "name": "Requirements Traceability Matrices",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A traceability matrix is the map that connects every requirement "
            "to its parents and its children: upward to the objective and "
            "stakeholder need it serves, downward to the design elements, "
            "code modules, and test cases that implement and prove it. The "
            "matrix answers the four questions that audits always ask: is "
            "every requirement implemented (forward trace), is every design "
            "element justified (backward trace), is every requirement tested "
            "(verification trace), and does every test trace to something "
            "real (no orphan tests). Orphans in either direction are defects: "
            "an untraced requirement will not be built, an unjustified design "
            "element is gold-plating. Coverage is computed in both "
            "directions and tracked to 100 percent. The matrix is built as "
            "the requirements are written - retrofitting traceability onto a "
            "finished build is archaeology, not engineering. This record "
            "covers the matrix structure, the four trace questions, orphan "
            "hunting, and coverage as a phase-gate metric."
        ),
        "how_it_works": (
            "Traceability works by linking identifiers at creation time. "
            "When a requirement is written, its upward links are recorded "
            "immediately: which objective, which stakeholder need, which "
            "parent requirement it refines. When design begins, each design "
            "element records the requirement IDs it satisfies; when code is "
            "written, modules record theirs; when tests are written, each "
            "test case records the requirement IDs it verifies. The matrix "
            "is the join of all these links, usually kept in the "
            "requirements management tool but expressible as a simple table: "
            "requirement ID rows, linked artifact columns. Analysis then "
            "runs the four queries: requirements with no design links "
            "(unimplemented), design elements with no requirement links "
            "(unjustified), requirements with no test links (unverified), "
            "tests with no requirement links (orphan). Each finding becomes "
            "a task: link it, justify it, or cut it. Coverage percentages "
            "are computed per direction and reported at each phase gate; a "
            "gate does not pass with orphans outstanding. Impact analysis "
            "rides the same links: change one requirement and the matrix "
            "names everything downstream that must be re-examined."
        ),
        "key_points": [
            "Four trace questions: every requirement implemented, every design element justified, every requirement tested, every test tied to something real.",
            "Links are recorded at creation time: requirement->objective at writing, design->requirement at design, test->requirement at test planning.",
            "Orphans in either direction are defects: untraced requirements will not be built; unjustified design is gold-plating.",
            "Coverage is computed per direction and gated at 100 percent before phase passage.",
            "The matrix powers impact analysis: change one requirement and it names everything downstream.",
        ],
        "requirements": [
            "Upward links from every requirement to its objective and stakeholder need, recorded at writing time.",
            "Downward links from design elements, code modules, and test cases to the requirement IDs they satisfy.",
            "The four orphan queries run at each phase gate with zero outstanding orphans as the pass criterion.",
        ],
        "standards": [
            "Bidirectional traceability per ISO/IEC/IEEE 29148.",
            "Traceability maintained under configuration management per ISO/IEC/IEEE 15288.",
        ],
        "citations": [CIT_29148, CIT_15288, CIT_HULL],
        "sig_lens": (
            "The Signature read: the traceability matrix is the survey map "
            "of the build contract - every beam tied to its foundation, "
            "every promise tied to its proof. The Signature Build Method "
            "surveys as it builds, because a map drawn after the city is "
            "finished is a guess, not a survey."
        ),
    },
    {
        "key": "risk",
        "name": "Risk Registers Inside the Specification",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A risk register inside the spec names everything that could "
            "still go wrong with the build: the risk, its probability, its "
            "impact in dollars and days, its owner, its trigger (the early "
            "warning sign), and its response plan. Risk exposure is the "
            "arithmetic - probability times impact - and it ranks the "
            "register so the team works the biggest exposures first. "
            "Responses come in four flavors: avoid (change the plan so the "
            "risk cannot happen), mitigate (reduce probability or impact), "
            "transfer (insurance, fixed-price contract, warranty), and "
            "accept (budget a contingency and watch the trigger). The "
            "register is not a pessimism exercise; it is the spec's immune "
            "system. Risks that materialize with a plan are incidents; risks "
            "that materialize without one are crises. The register is "
            "reviewed on a schedule, retired when the risk passes, and "
            "promoted to issues when the trigger fires. This record covers "
            "the register structure, exposure math, the four responses, and "
            "the review rhythm."
        ),
        "how_it_works": (
            "The risk register works by making the future discussable. The "
            "author brainstorms with the team using the prompt 'what could "
            "make this build fail' across categories: technical (untested "
            "technology, interface unknowns), schedule (dependency slips, "
            "resource contention), cost (price volatility, rework), and "
            "external (regulation changes, vendor failure). Each risk gets "
            "an ID (RSK-001), a plain-language statement of cause and "
            "consequence, a probability estimate (calibrated: 10, 30, 50, "
            "70, 90 percent, never false precision), an impact in dollars "
            "and schedule days, an owner, a trigger metric to watch, and a "
            "response plan with its cost. Exposure is computed as "
            "probability times impact, and the register is sorted by it - "
            "the top five get the team's attention, the rest get monitoring. "
            "Each response is one of the four: avoid, mitigate, transfer, "
            "or accept with contingency. Reviews re-score probabilities as "
            "evidence arrives; risks whose triggers fire become issues with "
            "the response plan activated; risks that age out are retired "
            "with a note. The register's total exposure is reported at "
            "phase gates as the project's quantified uncertainty."
        ),
        "key_points": [
            "Each risk = ID + cause-and-consequence statement + probability + impact in dollars and days + owner + trigger + response plan.",
            "Exposure = probability x impact; the register is sorted by exposure and the top five get the attention.",
            "Four responses: avoid, mitigate, transfer, accept-with-contingency - every risk gets exactly one.",
            "Probabilities use calibrated coarse bands (10/30/50/70/90 percent); false precision is a lie told twice.",
            "Triggers are watched on schedule: fired triggers become issues with the plan activated; aged-out risks are retired with a note.",
        ],
        "requirements": [
            "A risk register covering technical, schedule, cost, and external categories with owner and response for every entry.",
            "Exposure computed and ranked; the top exposures reviewed at each phase gate.",
            "Trigger metrics defined for every risk, with a monitoring schedule and an issue-conversion procedure.",
        ],
        "standards": [
            "Risk management process per ISO/IEC/IEEE 15288; risk documentation aligned with the PMBOK Guide risk management processes.",
            "System safety risks additionally managed per MIL-STD-882E where applicable.",
        ],
        "citations": [CIT_15288, CIT_PMBOK, CIT_MIL882],
        "sig_lens": (
            "The Signature read: the risk register is the weather chart of "
            "the build contract - every storm named, measured, and assigned "
            "a captain before it forms. The Signature Build Method never "
            "sails without one, because an unnamed storm is not bad luck; "
            "it is negligence with better lighting."
        ),
    },
    {
        "key": "interfaces",
        "name": "Interface Specifications and Control Documents",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Interface specifications define every boundary the build "
            "touches: the APIs it calls, the file formats it reads, the "
            "connectors it mates with, the protocols it speaks, the human "
            "handoffs it depends on. Each interface gets an ID, both sides "
            "named (who provides, who consumes), the data or signal or "
            "material that crosses, the format or protocol with its version, "
            "the timing and sequencing rules, the error handling, and the "
            "change-notification promise. When two teams build the two "
            "sides, the Interface Control Document (ICD) is the contract "
            "between them - signed by both, changed by neither alone. "
            "Interface failures are the classic integration surprise: both "
            "sides worked alone, neither worked together, because 'meters' "
            "met 'feet' at the boundary. This record covers interface "
            "identification, the ICD structure, compatibility checking, and "
            "the version discipline that keeps boundaries stable."
        ),
        "how_it_works": (
            "Interface specifications work by pinning both sides of every "
            "boundary in writing. The author walks the system boundary and "
            "lists every crossing: software APIs with their endpoints, "
            "request and response schemas, and versioning policy; data files "
            "with their formats, encodings, and validation rules; hardware "
            "connectors with pinouts, voltages, and mating cycles; network "
            "protocols with their versions and timeout behaviors; human "
            "handoffs with their forms and response-time promises. For "
            "each, the ICD records the provider side, the consumer side, "
            "the exact exchange (fields, units, ranges, enums), the "
            "sequencing and timing, the error and retry behavior, and the "
            "test that proves compatibility. Units are stated explicitly on "
            "both sides - the meter-foot disaster is prevented by a line in "
            "the document, not by hope. Both owning parties sign the ICD; "
            "either side may propose a change, but the change takes effect "
            "only when both sign the new version. Compatibility is verified "
            "by interface tests run against stubs before the real "
            "counterpart exists, so integration day holds no surprises."
        ),
        "key_points": [
            "Every interface = ID + provider + consumer + what crosses + format/protocol with version + timing + error handling + change promise.",
            "The ICD is a bilateral contract: signed by both sides, changed by neither alone.",
            "Units are stated explicitly on both sides of every interface - the meter-foot class of disaster is prevented by a document line.",
            "Compatibility is tested against stubs before the real counterpart exists; integration day should confirm, not discover.",
            "Version discipline: interfaces version independently, and consumers declare which versions they accept.",
        ],
        "requirements": [
            "An interface register covering software, data, hardware, network, and human interfaces with both sides named.",
            "ICDs for every two-party interface, signed by both owning parties.",
            "Explicit units, ranges, and enums on both sides of every data and signal interface.",
            "Interface compatibility tests defined and scheduled before integration.",
        ],
        "standards": [
            "Interface requirements per ISO/IEC/IEEE 29148; interface management per ISO/IEC/IEEE 15288.",
            "API versioning follows the project's declared policy (e.g. semantic versioning for the contract surface).",
        ],
        "citations": [CIT_29148, CIT_15288, CIT_NASA],
        "sig_lens": (
            "The Signature read: interfaces are the property fences of the "
            "build contract, and the ICD is the fence agreement signed by "
            "both neighbors. The Signature Build Method walks every fence "
            "with a measuring tape in both units before a single post is "
            "set, because fences measured in different units are lawsuits "
            "with landscaping."
        ),
    },
    {
        "key": "software",
        "name": "Software Build Specifications",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A software build specification turns 'build us an app' into an "
            "implementable contract: the system context and users, the "
            "functional requirements per feature, the non-functional targets "
            "(latency, throughput, availability, security), the data model "
            "and API contracts, the technology constraints (language, "
            "platform, deployment target), the integration points, the test "
            "strategy, and the acceptance criteria. It states what the "
            "software must do and how well, while leaving the internal "
            "design to the builders - specifying behavior and interfaces, "
            "not algorithms and class names, unless a design choice is "
            "genuinely mandated. The API contract section is the heart: "
            "endpoints, methods, request and response schemas, error codes, "
            "authentication, rate limits, and versioning - specified with "
            "examples that a tester can execute. This record covers the "
            "software-specific sections, the behavior-not-design line, and "
            "the API contract discipline."
        ),
        "how_it_works": (
            "A software build spec works by describing the system from the "
            "outside in. The context diagram shows the software, its users, "
            "and the external systems it talks to. Features are specified "
            "as user-visible behaviors with acceptance criteria in "
            "given-when-then form. The data model names the entities, their "
            "attributes, and their relationships; the API contract then "
            "exposes exactly what crosses the boundary, endpoint by "
            "endpoint, with request and response examples, error codes, "
            "auth scheme, rate limits, and the versioning policy. "
            "Non-functional targets attach numbers: p95 latency under load, "
            "throughput in requests per second, availability as nines, "
            "recovery time objective, security requirements (auth, "
            "encryption at rest and in transit, audit logging). Technology "
            "constraints name the mandated stack only where mandated; "
            "everything else is the builder's choice, because a spec that "
            "designs the internals is a design document wearing a spec's "
            "clothes. The test strategy maps the test pyramid - unit, "
            "integration, system, acceptance - to the requirements, and the "
            "definition of done for each release is stated before the first "
            "sprint."
        ),
        "key_points": [
            "Outside-in: context diagram, user-visible behaviors, data model, API contracts, quality targets, test strategy, acceptance criteria.",
            "Specify behavior and interfaces, not internals: mandate a design choice only when it is genuinely required.",
            "API contracts are the heart: endpoints, schemas, error codes, auth, rate limits, versioning - with executable examples.",
            "Non-functional targets carry numbers: p95 latency, throughput, availability nines, RTO, encryption and audit requirements.",
            "Definition of done per release is stated before the first sprint, not negotiated at the demo.",
        ],
        "requirements": [
            "A system context diagram naming users and external systems.",
            "Feature behaviors with given-when-then acceptance criteria.",
            "Complete API contracts with examples, error codes, auth, rate limits, and versioning policy.",
            "Numbered non-functional targets for latency, throughput, availability, and security.",
            "A test strategy mapping the test pyramid to requirements.",
        ],
        "standards": [
            "Software requirements per ISO/IEC/IEEE 29148; software life cycle processes per ISO/IEC/IEEE 12207 concepts.",
            "API design follows the project's interface standards; security requirements per the security policy.",
        ],
        "citations": [CIT_29148, CIT_SOMMERVILLE, CIT_WIEGERS],
        "sig_lens": (
            "The Signature read: a software spec is a build contract for "
            "an invisible machine - the behaviors are the rooms, the APIs "
            "are the doors, and the quality targets are the building code. "
            "The Signature Build Method specifies every door's dimensions "
            "and every room's purpose, then lets the builder choose the "
            "studs, because a contract that picks the nails is micromanage"
            "ment with a signature block."
        ),
    },
    {
        "key": "hardware",
        "name": "Hardware Build Specifications",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A hardware build specification turns 'build us a device' into "
            "a manufacturable contract: the mechanical envelope and "
            "mounting, the electrical interfaces and power budget, the "
            "environmental ratings (temperature, humidity, shock, "
            "vibration, ingress), the materials and finishes, the "
            "tolerances and the tolerance stack-up analysis, the "
            "regulatory marks required (CE, FCC, UL), the reliability "
            "target (MTBF), the serviceability requirements, and the "
            "acceptance test procedure. Hardware specs live in numbers with "
            "units and tolerances: a dimension without a tolerance is a "
            "suggestion, and a suggestion is not manufacturable. The "
            "tolerance stack-up is the characteristic analysis - worst-case "
            "and statistical (root-sum-square) - proving the assembly fits "
            "and functions when every part sits at its allowed extreme. "
            "This record covers the hardware sections, the tolerance "
            "discipline, and the environmental and regulatory gates."
        ),
        "how_it_works": (
            "A hardware build spec works by describing the physical article "
            "completely enough that a competent shop can quote it, build "
            "it, and test it. The envelope section gives overall dimensions, "
            "weight budget, mounting interfaces, and keep-out zones. The "
            "electrical section gives supply voltages with tolerances, "
            "current draw per mode, grounding and shielding rules, and "
            "connector pinouts. The environmental section states the "
            "operating and storage ranges for temperature, humidity, shock, "
            "vibration, and ingress protection (IP rating), each with the "
            "test standard that proves it. Every critical dimension carries "
            "a tolerance, and the stack-up analysis sums them two ways: "
            "worst-case (every part at its extreme - the guarantee) and "
            "root-sum-square (the statistical expectation for normal "
            "production). Materials and finishes are specified with their "
            "standards (alloy temper, plating thickness); regulatory marks "
            "list the certifications the design must earn and the test labs "
            "that will witness them. Reliability gets a target MTBF with "
            "the operating profile it assumes. Serviceability states "
            "mean-time-to-repair and the tools required. The acceptance "
            "test procedure turns all of this into a bench procedure with "
            "pass and fail limits."
        ),
        "key_points": [
            "Numbers with units and tolerances: a dimension without a tolerance is a suggestion, not a specification.",
            "Tolerance stack-up, two ways: worst-case (the guarantee) and root-sum-square (the production expectation).",
            "Environmental ratings name the range and the test standard: temperature, humidity, shock, vibration, IP ingress.",
            "Regulatory marks are design inputs, not afterthoughts: CE, FCC, UL each impose requirements the design must satisfy from day one.",
            "Reliability (MTBF with its operating profile) and serviceability (MTTR, tools) are specified, not hoped for.",
        ],
        "requirements": [
            "Envelope, weight budget, mounting, and keep-out zones with toleranced dimensions.",
            "Electrical interfaces: supply rails with tolerances, current per mode, grounding, shielding, pinouts.",
            "Environmental ranges with the proving test standard for each.",
            "Worst-case and RSS tolerance stack-up analyses for every critical assembly.",
            "Regulatory certification list with the design requirements each imposes.",
        ],
        "standards": [
            "Dimensioning and tolerancing per ASME Y14.5; drawings per the project drafting standard.",
            "Environmental test methods per MIL-STD-810 or IEC 60068 as applicable; ingress per IEC 60529 IP codes.",
        ],
        "citations": [CIT_ULRICH, CIT_NASA, CIT_29148],
        "sig_lens": (
            "The Signature read: a hardware spec is a build contract written "
            "in steel and copper - every number a promise, every tolerance "
            "the honesty margin around it. The Signature Build Method stacks "
            "the tolerances twice, worst-case and statistical, because a "
            "contract that fits only on paper is a very expensive piece of "
            "paper."
        ),
    },
    {
        "key": "embedded",
        "name": "Device and Embedded Build Specifications",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "An embedded build specification covers the device where "
            "software meets physics: the microcontroller or SoC, its "
            "peripherals and pin assignments, the firmware behaviors and "
            "timing constraints, the power budget per operating mode, the "
            "thermal budget, the sensor and actuator interfaces, the "
            "bootloader and update mechanism, and the debug and test "
            "access. The power budget is the characteristic analysis - "
            "every subsystem's draw in sleep, idle, and active modes, summed "
            "against the battery or supply capacity to prove the required "
            "runtime. Timing constraints are stated as deadlines with "
            "jitter limits, because a late answer in a control loop is a "
            "wrong answer. The update mechanism is specified up front "
            "(signed OTA, USB DFU, JTAG-only), since a device that cannot be "
            "updated safely is a liability the day after launch. This record "
            "covers the embedded sections, the power and timing budgets, "
            "and the update and debug discipline."
        ),
        "how_it_works": (
            "An embedded build spec works by budgeting the scarce resources "
            "before committing to them. The hardware section names the MCU "
            "or SoC, clock tree, memory map (flash, RAM, and their "
            "allocation), peripheral assignments pin by pin, and the sensor "
            "and actuator interfaces with their electrical characteristics. "
            "The firmware section specifies behaviors as state machines with "
            "named states, transitions, and timing deadlines - each deadline "
            "with its jitter budget, because control loops and communication "
            "protocols fail on lateness, not just on wrongness. The power "
            "budget tabulates every subsystem's draw in each mode (sleep, "
            "idle, active, transmit), multiplies by the duty cycle, and "
            "divides the battery capacity by the average draw to prove "
            "runtime with margin. The thermal budget does the same for heat: "
            "dissipation per mode against the enclosure's thermal resistance "
            "and the maximum junction temperatures. The update mechanism is "
            "specified completely - image format, signing keys and their "
            "custody, rollback policy, and the brick-recovery procedure - "
            "and the debug access (SWD, JTAG, UART console) is specified "
            "with its production disposition (disabled, locked, or retained "
            "for service)."
        ),
        "key_points": [
            "Power budget: every subsystem's draw per mode x duty cycle, summed against battery capacity to prove runtime with margin.",
            "Timing as deadlines with jitter limits: in control loops and protocols, a late answer is a wrong answer.",
            "Firmware behaviors specified as state machines: named states, transitions, and the timing each transition must meet.",
            "Update mechanism specified up front: image format, signing, key custody, rollback, brick recovery.",
            "Debug access specified with its production disposition: disabled, locked, or retained for service - decided now, not discovered later.",
        ],
        "requirements": [
            "Named MCU/SoC with clock tree, memory map, and pin-by-pin peripheral assignments.",
            "State-machine firmware behaviors with timing deadlines and jitter budgets.",
            "Power budget per mode proving the required runtime with stated margin.",
            "Complete update mechanism: format, signing, key custody, rollback, recovery.",
        ],
        "standards": [
            "Functional safety requirements per IEC 61508 or ISO 26262 where the device is safety-related.",
            "EMC requirements per the applicable emissions and immunity standards for the market.",
        ],
        "citations": [CIT_61508, CIT_26262, CIT_29148],
        "sig_lens": (
            "The Signature read: an embedded spec is a build contract for "
            "a machine that must think on a sip of power and answer before "
            "the deadline - every milliamp budgeted, every millisecond "
            "promised. The Signature Build Method budgets power and time "
            "before choosing silicon, because a device designed on hope runs "
            "exactly as long as hope lasts."
        ),
    },
    {
        "key": "integration",
        "name": "Systems Integration Specifications",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "A systems integration specification describes how separately "
            "built parts become one working system: the integration "
            "sequence (which assemblies join in which order), the "
            "integration environment and tooling, the interface verification "
            "at each step, the build-up from units to subsystems to system, "
            "and the regression discipline that keeps each new integration "
            "from breaking the last. The integration sequence is designed, "
            "not improvised: bottom-up (units first, the classic), top-down "
            "with stubs (skeleton first), or big-bang (everything at once - "
            "the method of last resort, named for the sound it makes). Each "
            "integration step names its entry criteria (what must be proven "
            "before the parts meet), its procedure, and its exit criteria "
            "(what must be proven before the next step). The pairwise "
            "interface count - n parts make n(n-1)/2 pairs - sets the scale "
            "of the job and the reason integration is planned, not hoped. "
            "This record covers the sequence design, entry and exit "
            "criteria, and the regression discipline."
        ),
        "how_it_works": (
            "Integration specifications work by turning 'plug it all "
            "together' into a choreographed sequence. The author lists the "
            "integration units (the separately built parts), counts the "
            "pairwise interfaces (n(n-1)/2 - the honest measure of the "
            "job's size), and designs the sequence: bottom-up when units "
            "are independently testable, top-down with stubs when the "
            "architecture must be proven early, sandwich when both apply. "
            "Each step gets entry criteria (unit tests passed, interface "
            "tests against stubs passed, ICD version confirmed), a "
            "procedure (the build-up order, the tooling, the environment), "
            "and exit criteria (the integrated assembly's tests passed, no "
            "regressions in the previously integrated parts). Stubs and "
            "drivers stand in for missing counterparts so interface "
            "verification never waits for the slowest part. After each "
            "step, the regression suite for everything integrated so far "
            "runs green before the next step begins - the discipline that "
            "keeps integration monotonic. The final step is system-level "
            "verification against the system requirements, which the "
            "integration sequence was designed to make anti-climactic."
        ),
        "key_points": [
            "The sequence is designed: bottom-up, top-down with stubs, or sandwich - big-bang is the method of last resort.",
            "Each step = entry criteria + procedure + exit criteria; parts meet only when the entry bar is cleared.",
            "Pairwise interface count n(n-1)/2 sets the honest scale of the integration job.",
            "Stubs and drivers let interface verification proceed without waiting for the slowest part.",
            "Regression after every step keeps integration monotonic: the suite for all integrated parts runs green before proceeding.",
        ],
        "requirements": [
            "A designed integration sequence with the strategy named and justified.",
            "Entry and exit criteria for every integration step.",
            "Interface verification against stubs scheduled before the real counterparts arrive.",
            "A regression suite covering all integrated parts, run green after each step.",
        ],
        "standards": [
            "Integration and verification processes per ISO/IEC/IEEE 15288.",
            "Interface verification per the ICDs and ISO/IEC/IEEE 29148 interface requirements.",
        ],
        "citations": [CIT_15288, CIT_NASA, CIT_29148],
        "sig_lens": (
            "The Signature read: integration is the raising of the contract "
            "- separately built walls lifted into one structure in a planned "
            "order, each joint tested before the next is set. The Signature "
            "Build Method choreographs the raising beam by beam, because a "
            "building assembled all at once is called a collapse."
        ),
    },
    {
        "key": "safety",
        "name": "Safety and Regulatory Compliance in Specifications",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Safety and regulatory sections turn 'do not hurt anyone' into "
            "specified, verifiable requirements: the hazard analysis, the "
            "safety requirements derived from it, the safety integrity "
            "levels (SIL) or automotive ASILs assigned, the regulatory "
            "certifications required with their design inputs, and the "
            "compliance evidence the build must produce. The hazard analysis "
            "(preliminary hazard list, then system hazard analysis per "
            "MIL-STD-882E) identifies what can go wrong and how badly; each "
            "hazard gets severity and likelihood, and the combination sets "
            "the risk class that drives the rigor of everything downstream. "
            "Safety requirements are then written like all requirements - "
            "shall-statements with verification methods - but they are "
            "never waived, never traded against schedule, and traced with "
            "extra care. Regulatory marks (CE, FCC, UL, FDA, automotive) are "
            "listed with the standards each imposes, because certification "
            "is a design input: a product designed without its target "
            "standards is redesigned, expensively, at the test lab. This "
            "record covers the hazard-to-requirement flow and the compliance "
            "evidence discipline."
        ),
        "how_it_works": (
            "Safety specification works from hazard to proof. The hazard "
            "analysis enumerates hazardous states - energy sources, failure "
            "modes, human errors, environmental extremes - and for each "
            "records the cause chain, the worst credible severity, and the "
            "likelihood with the designed controls in place. Severity times "
            "likelihood sets the risk class (per the project's risk matrix, "
            "aligned with MIL-STD-882E or the domain standard), and the "
            "risk class sets the required rigor: higher classes demand "
            "redundancy, diagnostics, formal verification, and independent "
            "assessment. Safety requirements are derived one per hazard "
            "control: 'the system shall detect sensor disagreement within "
            "100 ms and enter the safe state', each with its SIL or ASIL, "
            "its verification method, and its trace to the hazard. The "
            "regulatory section lists every applicable mark and standard, "
            "extracts each standard's design requirements into the spec's "
            "requirements (so they are traced and verified like all the "
            "rest), and names the certification evidence: test reports, "
            "analysis reports, process audits. Compliance is then a matter "
            "of executing the verification plan and filing the evidence - "
            "planned from day one, not assembled in panic at the lab door."
        ),
        "key_points": [
            "Hazard analysis first: enumerate hazardous states, score severity x likelihood, set the risk class that drives all downstream rigor.",
            "One safety requirement per hazard control, each with its SIL/ASIL, verification method, and hazard trace - never waived, never traded for schedule.",
            "Regulatory marks are design inputs: each target standard's requirements are extracted into the spec and traced like all the rest.",
            "Certification evidence (test reports, analyses, process audits) is planned from day one, not assembled at the lab door.",
            "Higher risk classes demand redundancy, diagnostics, formal verification, and independent assessment.",
        ],
        "requirements": [
            "A hazard analysis with severity, likelihood, and risk class per hazard.",
            "Safety requirements derived per hazard control, with SIL/ASIL, verification method, and hazard trace.",
            "A regulatory section listing every applicable mark with its extracted design requirements.",
            "A compliance evidence plan naming every report, analysis, and audit the certification needs.",
        ],
        "standards": [
            "System safety per MIL-STD-882E; functional safety per IEC 61508 or ISO 26262 as applicable.",
            "Medical, aviation, or other domain certification per the applicable authority (FDA, DO-178C, etc.).",
        ],
        "citations": [CIT_MIL882, CIT_61508, CIT_26262, CIT_DO178C],
        "sig_lens": (
            "The Signature read: safety requirements are the load limits "
            "posted on every beam of the contract - calculated from the "
            "hazards, never negotiated against the calendar. The Signature "
            "Build Method writes the hazard list before the design and "
            "proof-tests every control, because a contract that gambles "
            "with safety is not a contract but a confession."
        ),
    },
    {
        "key": "versioning",
        "name": "Specification Versioning and Baselines",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Versioning and baselines give the spec a memory: every released "
            "version is numbered, dated, and immutable, and a baseline is a "
            "version the project has formally agreed to build against. "
            "Semantic versioning (MAJOR.MINOR.PATCH) is the common scheme: "
            "MAJOR for incompatible changes, MINOR for added compatible "
            "content, PATCH for corrections. The baseline process is formal: "
            "a draft is reviewed, the review findings are dispositioned "
            "(accepted, rejected with reason, deferred), the corrected draft "
            "is approved by the named authorities, and the approved version "
            "is frozen - further changes go through change control, not "
            "editing. Typical baselines are the requirements baseline (what "
            "we agreed to build), the design baseline (how we agreed to "
            "build it), and the product baseline (what we actually built, "
            "as verified). The change history table in each version records "
            "what moved and why, so any baseline can be audited. This record "
            "covers the versioning scheme, the baseline ceremony, and the "
            "frozen-version discipline."
        ),
        "how_it_works": (
            "Versioning works by making every state of the spec addressable. "
            "The author numbers drafts (0.x) and releases (1.0.0 and up) per "
            "the declared scheme; the scheme's rules are written in the "
            "spec's front matter so reviewers know what a version bump "
            "means. Baselining is the ceremony: the draft circulates for "
            "review, reviewers file findings, the author dispositions each "
            "finding in writing, the corrected draft goes to the approval "
            "authorities named in the spec (requester, chief engineer, QA), "
            "and on approval the version is frozen - stored immutably with "
            "its approval record. From that moment, the document is "
            "read-only; every subsequent change is a change request against "
            "the baseline, producing the next version with its change "
            "history entry. The three canonical baselines mark the "
            "project's commitments: requirements (the agreed what), design "
            "(the agreed how), product (the verified as-built). Audits "
            "compare the built article against the product baseline and the "
            "product baseline against the requirements baseline - the chain "
            "of custody for the entire build."
        ),
        "key_points": [
            "Semantic versioning: MAJOR for incompatible changes, MINOR for compatible additions, PATCH for corrections - rules written in the front matter.",
            "Baseline ceremony: review -> disposition findings -> approve by named authorities -> freeze immutably with the approval record.",
            "Frozen means read-only: post-baseline changes are change requests producing new versions, never silent edits.",
            "Three canonical baselines: requirements (agreed what), design (agreed how), product (verified as-built).",
            "The change history table is the audit trail: what moved, when, by whom, and why.",
        ],
        "requirements": [
            "A declared versioning scheme with its bump rules written in the spec front matter.",
            "Named approval authorities for each baseline type.",
            "Immutable storage of every baselined version with its approval record.",
            "A change history table in every version recording all changes since the previous baseline.",
        ],
        "standards": [
            "Configuration management per ISO/IEC/IEEE 15288; document control per ISO 9001 where applicable.",
            "Baseline identification follows the project configuration management plan.",
        ],
        "citations": [CIT_15288, CIT_9001, CIT_CMMI],
        "sig_lens": (
            "The Signature read: baselines are the sealed editions of the "
            "build contract - each one signed, dated, and frozen, so the "
            "project always knows which promise it is keeping. The Signature "
            "Build Method seals the editions in ceremony and never edits a "
            "sealed page, because a contract that rewrites its own past is "
            "a rumor with a version number."
        ),
    },
    {
        "key": "cost",
        "name": "Cost Estimation and Resource Planning",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Cost estimation turns the spec into a budget: the expected cost "
            "of building what is specified, with the uncertainty stated "
            "honestly. The workhorse is the three-point estimate per work "
            "item - optimistic, most likely, pessimistic - combined by the "
            "PERT formula (expected = (O + 4M + P) / 6) with the standard "
            "deviation ((P - O) / 6) as the uncertainty. Estimates are built "
            "bottom-up from the deliverables and requirements: each item "
            "estimated, then summed, then loaded with contingency derived "
            "from the risk register's exposure - not from a flat percentage "
            "plucked from habit. Resource planning assigns the people, "
            "equipment, and facilities per phase, checking for contention "
            "(the same specialist promised to two tasks at once). The "
            "estimate is re-baselined at each phase gate as unknowns become "
            "knowns, and the variance between estimated and actual is "
            "recorded to calibrate the next estimate. This record covers "
            "three-point estimation, contingency from risk exposure, and the "
            "calibration loop."
        ),
        "how_it_works": (
            "Cost estimation works by decomposition and honest arithmetic. "
            "The estimator breaks the spec's deliverables into work items "
            "small enough to estimate (days to weeks, never months), and "
            "for each collects three numbers: the optimistic cost (everything "
            "goes right), the most likely cost (normal friction), and the "
            "pessimistic cost (the known risks bite). The PERT expected "
            "value (O + 4M + P) / 6 weights the most likely heavily, and "
            "(P - O) / 6 gives the standard deviation - the uncertainty "
            "band, stated, not hidden. Items are summed for the base "
            "estimate; then contingency is added from the risk register: "
            "each accepted or mitigated risk contributes its exposure "
            "(probability times impact) to the contingency pool, so the "
            "buffer is traceable to named risks instead of being a flat "
            "guess. Resource planning then maps the estimate to people and "
            "equipment per phase, leveling the load so no specialist is "
            "double-booked and long-lead items are ordered on time. At "
            "each phase gate the estimate is refreshed with actuals, and "
            "the estimating error is logged - over runs and under runs "
            "alike - to calibrate the team's future three-point judgments."
        ),
        "key_points": [
            "Three-point per work item: PERT expected = (O + 4M + P) / 6, uncertainty = (P - O) / 6 - stated, never hidden.",
            "Bottom-up from deliverables: items small enough to estimate (days to weeks), then summed.",
            "Contingency from the risk register's exposure, traceable to named risks - not a flat percentage from habit.",
            "Resource planning levels the load: no double-booked specialists, long-lead items ordered on time.",
            "Re-baselined at every phase gate; estimating error logged to calibrate future judgments.",
        ],
        "requirements": [
            "A work breakdown derived from the deliverables, with items sized in days to weeks.",
            "Three-point estimates with PERT expected value and standard deviation per item.",
            "Contingency derived from quantified risk exposure, traceable to the risk register.",
            "A resource plan per phase with contention checks on people and equipment.",
        ],
        "standards": [
            "Estimation rigor scaled to project class per the PMBOK Guide cost management processes.",
            "Parametric models (e.g. COCOMO-style) used only where calibrated to the organization's history.",
        ],
        "citations": [CIT_PMBOK, CIT_BOEHM, CIT_MCCONNELL],
        "sig_lens": (
            "The Signature read: the estimate is the price written on the "
            "build contract - three numbers per task, honestly combined, "
            "with the uncertainty stated instead of hidden. The Signature "
            "Build Method prices from the risk register upward, because a "
            "price that ignores the weather is a promise to pay for it "
            "later."
        ),
    },
    {
        "key": "prototypes",
        "name": "Prototypes, MVPs, and Phase Gates",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Prototypes, MVPs, and phase gates are the spec's way of buying "
            "knowledge cheaply and deciding deliberately. A prototype "
            "answers a specific technical question ('can the sensor read "
            "through the enclosure?') and is built to be thrown away; an "
            "MVP (minimum viable product) is the smallest build that "
            "delivers real value to real users and survives contact with "
            "them; a phase gate is the formal review at the end of each "
            "project phase where the project earns the right to continue. "
            "Each gate has entry criteria (what must be delivered), review "
            "criteria (scored, not vibed), and three outcomes: go, go with "
            "conditions, or stop. The spec names the prototypes (each with "
            "its question and its disposal plan), defines the MVP scope "
            "(the smallest shippable that tests the riskiest assumption), "
            "and sets the gates with their criteria before the work starts. "
            "This record covers the prototype discipline, the MVP cut, and "
            "the gate ceremony that keeps projects honest."
        ),
        "how_it_works": (
            "Prototypes work by spending a little to learn a lot. Each "
            "prototype is chartered with one question, a budget, a "
            "deadline, and a disposal plan - prototypes that linger become "
            "products without specs, which is how technical debt is born. "
            "The MVP is cut differently: it is the smallest scope that "
            "delivers genuine user value and tests the riskiest assumption, "
            "specified with the same rigor as the full product but a "
            "fraction of the content. Phase gates work as the project's "
            "toll booths: at each gate (requirements review, preliminary "
            "design review, critical design review, test readiness review, "
            "acceptance), the entry criteria name what must be delivered, "
            "the reviewers score the review criteria (completeness, "
            "consistency, risk posture, estimate health), and the board "
            "decides go, conditional go (with named conditions and a "
            "re-check date), or stop. A stop is a success of the process, "
            "not a failure of the team - it kills a bad project cheaply "
            "instead of expensively. Gate records are filed with the "
            "baseline; skipped gates are how disasters get their head "
            "start."
        ),
        "key_points": [
            "Prototype = one question + budget + deadline + disposal plan; prototypes that linger become products without specs.",
            "MVP = smallest scope delivering real user value while testing the riskiest assumption, specified with full rigor.",
            "Each gate = entry criteria + scored review criteria + three outcomes: go, conditional go, or stop.",
            "A stop is a process success: killing a bad project cheaply beats killing it expensively.",
            "Gate records are filed with the baseline; skipped gates are how disasters get their head start.",
        ],
        "requirements": [
            "A prototype charter per prototype: the question, budget, deadline, and disposal plan.",
            "An MVP scope definition naming the riskiest assumption it tests.",
            "Named phase gates with entry criteria, scored review criteria, and decision records.",
        ],
        "standards": [
            "Technical reviews per ISO/IEC/IEEE 15288 (SRR, PDR, CDR, TRR); gate criteria in the project plan.",
            "Prototype disposal and configuration control per the project configuration management plan.",
        ],
        "citations": [CIT_15288, CIT_NASA, CIT_ULRICH],
        "sig_lens": (
            "The Signature read: prototypes are the survey stakes of the "
            "build contract - driven to test the ground, then pulled. The "
            "Signature Build Method stakes the risky ground first, ships "
            "the smallest honest building, and tolls every phase, because "
            "a contract with no gates is a road with no brakes."
        ),
    },
    {
        "key": "mbse",
        "name": "Model-Based Systems Engineering Specifications",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Model-Based Systems Engineering (MBSE) replaces the "
            "document-centric spec with a system model as the authoritative "
            "source of truth: requirements, structure, behavior, and "
            "parametrics captured in a single consistent model, usually in "
            "SysML, from which documents are generated rather than the "
            "other way around. The model's requirement diagrams hold the "
            "requirements with their IDs and trace links; block definition "
            "diagrams hold the structure; activity and sequence diagrams "
            "hold the behavior; parametric diagrams hold the engineering "
            "analysis (power budgets, mass rollups, timing) that computes "
            "from the model's own values. Consistency is the payoff: change "
            "a value in one place and every diagram, table, and generated "
            "document reflects it - the end of the five-versions-of-the-"
            "truth problem. The model is configuration-managed like code, "
            "reviewed in model reviews, and baselined like any spec. This "
            "record covers the MBSE value proposition, the SysML view set, "
            "and the model-as-baseline discipline."
        ),
        "how_it_works": (
            "MBSE works by making the model the spec. The modeler builds "
            "the requirement hierarchy in requirement diagrams, each "
            "requirement carrying its ID, text, rationale, and verification "
            "method as model properties. System structure goes into block "
            "definition diagrams: blocks for each subsystem with their "
            "ports, interfaces, and value properties (mass, power, cost). "
            "Behavior goes into activity diagrams (flows), sequence "
            "diagrams (interactions), and state machines (modes). "
            "Parametric diagrams bind the value properties to constraint "
            "blocks - the engineering equations - so the model computes "
            "rollups itself: total mass, power budget, cost sum, timing "
            "margins. Traceability is then structural: allocate "
            "relationships link requirements to blocks, satisfy links to "
            "design, verify links to test cases - the matrix generated from "
            "the model, never maintained by hand. Reviews walk the model, "
            "not a document; findings are raised against model elements. "
            "Baselining freezes the model version; documents are generated "
            "views, regenerated on demand, never edited separately. The "
            "discipline that makes it work is modeling conventions - naming, "
            "diagram standards, profile usage - enforced by the modeling "
            "tool and the model review checklist."
        ),
        "key_points": [
            "The model is the authoritative source: requirements, structure, behavior, and parametrics in one consistent SysML model; documents are generated views.",
            "Parametric diagrams compute from the model's own values: mass rollups, power budgets, timing margins - analysis that cannot drift from the design.",
            "Traceability is structural: allocate, satisfy, and verify relationships generate the matrix instead of maintaining it by hand.",
            "Change a value once and every diagram, table, and generated document reflects it - the end of five-versions-of-the-truth.",
            "The model is configuration-managed, reviewed, and baselined like code; modeling conventions are enforced, not suggested.",
        ],
        "requirements": [
            "A system model containing the requirements hierarchy with IDs, text, rationale, and verification methods.",
            "Structural, behavioral, and parametric views covering the full system scope.",
            "Allocate/satisfy/verify relationships providing bidirectional traceability.",
            "Documented modeling conventions covering naming, diagrams, and profile usage.",
        ],
        "standards": [
            "Modeling language per OMG SysML; methodology per the project's selected MBSE method.",
            "Model configuration management and baselining per ISO/IEC/IEEE 15288.",
        ],
        "citations": [CIT_SYSML, CIT_15288, CIT_INCOSE_HB],
        "sig_lens": (
            "The Signature read: MBSE is the build contract drawn as a "
            "living blueprint - one model where every beam knows its load "
            "and every change redraws every view at once. The Signature "
            "Build Method keeps a single truth and generates the paperwork "
            "from it, because five versions of the truth are four lies "
            "with better formatting."
        ),
    },
    {
        "key": "standards",
        "name": "Specification Standards: IEEE 29148 and Friends",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Specification standards are the agreed rules of the game: what "
            "a requirement is, how it is written, how it is managed, and "
            "how it is verified. ISO/IEC/IEEE 29148:2018 is the center - "
            "it defines the requirements engineering processes, the "
            "characteristics of good requirements and good requirement "
            "sets, and the structure of the system and software "
            "requirements specifications. Around it sit the companions: "
            "ISO/IEC/IEEE 15288 for the system life cycle that the "
            "requirements live in, the INCOSE Guide for Writing "
            "Requirements for the sentence-level craft, the INCOSE Systems "
            "Engineering Handbook for the practitioner context, IEEE 830 "
            "as the historical software SRS outline, and domain standards "
            "(DO-178C, ISO 26262, IEC 61508) that add rigor where failure "
            "hurts. A spec declares its standards up front - in the "
            "front matter, with versions - so every reviewer judges by the "
            "same rules. This record is the standards map: which standard "
            "covers what, and how to declare and apply them."
        ),
        "how_it_works": (
            "Specification standards work as the spec's constitution, "
            "declared before writing begins. The author selects the "
            "applicable set: 29148 always (the requirements discipline "
            "itself), 15288 for the life cycle context, the INCOSE writing "
            "guide for the sentence rules, and domain standards where the "
            "build's consequences demand them. The front matter lists each "
            "with its exact version - 'ISO/IEC/IEEE 29148:2018', not 'the "
            "IEEE standard' - because versions move and audits check. The "
            "writing rules are then applied mechanically: 29148's "
            "characteristics of a good requirement (necessary, "
            "implementation-free, unambiguous, consistent, complete, "
            "singular, feasible, traceable, verifiable) become the review "
            "checklist, each requirement scored against the list. The "
            "characteristics of a good requirement set (complete, "
            "consistent, feasible, bounded, etc.) become the document-level "
            "review. Non-compliances are not silent: where the project "
            "deviates (a shall-statement the domain forbids, a process step "
            "skipped for cause), the deviation is recorded with its "
            "rationale and its approver. Auditors then verify the spec "
            "against its declared constitution - which is exactly why the "
            "declaration comes first."
        ),
        "key_points": [
            "29148 is the center: requirements processes, characteristics of good requirements and requirement sets, SRS structure.",
            "Companions: 15288 (life cycle), INCOSE writing guide (sentence craft), INCOSE Handbook (practitioner context), domain standards (rigor where failure hurts).",
            "Declared up front with exact versions in the front matter: audits judge the spec against its declared constitution.",
            "The nine characteristics of a good requirement become the mechanical review checklist for every shall-statement.",
            "Deviations are recorded with rationale and approver - never silent.",
        ],
        "requirements": [
            "A front-matter standards declaration listing each applicable standard with its exact version.",
            "Every requirement reviewed against the 29148 good-requirement characteristics checklist.",
            "The requirement set reviewed against the 29148 good-set characteristics.",
            "All deviations from declared standards recorded with rationale and approver.",
        ],
        "standards": [
            "ISO/IEC/IEEE 29148:2018 as the requirements engineering basis.",
            "ISO/IEC/IEEE 15288:2015 for life cycle context; INCOSE-TP-2010-006-03 for writing rules.",
        ],
        "citations": [CIT_29148, CIT_15288, CIT_INCOSE_REQ, CIT_INCOSE_HB],
        "sig_lens": (
            "The Signature read: standards are the building code the "
            "contract is inspected against - declared before the first "
            "beam is cut, enforced at every review. The Signature Build "
            "Method posts the code on the site fence on day one, because a "
            "contract inspected against secret rules is a trial with no "
            "defense."
        ),
    },
    {
        "key": "ai_gen",
        "name": "AI-Assisted Specification Generation and Review",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "AI assistance in specification work means using language and "
            "analysis tools to draft, check, and improve specs - never to "
            "replace the human sign-off. The legitimate uses are well "
            "bounded: expanding a request into a first-draft spec skeleton, "
            "flagging vague terms and missing sections, checking "
            "requirements against the well-formedness rules, detecting "
            "contradictions between requirements, suggesting test ideas per "
            "requirement, and summarizing long specs for reviewers. The "
            "hard boundary is authority: the AI proposes, the qualified "
            "human disposes - every AI-drafted requirement is reviewed, "
            "corrected, and approved by a person who is accountable for it. "
            "The failure modes are known: hallucinated requirements that "
            "sound right but trace to nothing, confident vagueness, and "
            "specification bloat from an AI that never says 'that is out "
            "of scope'. This record covers the legitimate uses, the human-"
            "authority boundary, and the review discipline that keeps AI "
            "output honest."
        ),
        "how_it_works": (
            "AI-assisted specification works as a supervised pipeline. The "
            "human provides the request, the context (domain, constraints, "
            "stakeholders), and the standards the spec must follow; the AI "
            "produces a draft skeleton with candidate requirements. The "
            "human then runs the mechanical checks - ideally with tooling: "
            "an ambiguity scan flags vague terms (fast, robust, user-"
            "friendly, etc.) for quantification; a completeness scan checks "
            "the fourteen-section anatomy for gaps; a contradiction scan "
            "compares requirements pairwise for conflicts; a traceability "
            "scan finds requirements with no parent objective. Each flagged "
            "item is dispositioned by the human: fix, accept with reason, "
            "or cut. AI-drafted requirements get the same review as "
            "human-drafted ones - the well-formedness checklist does not "
            "care who typed the sentence. The spec records AI assistance in "
            "its front matter or change history (which sections were "
            "AI-drafted, which model, which date), so reviewers know the "
            "provenance. Final approval is always human: the signature on "
            "the baseline is a person's, and the accountability is theirs."
        ),
        "key_points": [
            "Legitimate uses: draft skeletons, vagueness flags, well-formedness checks, contradiction detection, test suggestions, reviewer summaries.",
            "Hard boundary: the AI proposes, the accountable human disposes - every AI-drafted requirement is human-reviewed and human-approved.",
            "Mechanical checks: ambiguity scan, anatomy completeness scan, contradiction scan, traceability scan - each finding dispositioned by a person.",
            "Known failure modes: hallucinated requirements, confident vagueness, scope bloat from an AI that never says no.",
            "Provenance is recorded: which sections were AI-drafted, by which model, on which date.",
        ],
        "requirements": [
            "A declared AI-assistance policy naming the legitimate uses and the human-authority boundary.",
            "Mechanical review scans (ambiguity, completeness, contradiction, traceability) run on every AI-drafted section.",
            "Provenance records for AI-drafted content: model, date, and the human reviewer who approved it.",
            "Human signature on the baseline, with accountability explicitly assigned.",
        ],
        "standards": [
            "AI-drafted requirements held to the same ISO/IEC/IEEE 29148 well-formedness rules as human-drafted ones.",
            "Organizational AI-use policy compliance, including data handling for proprietary requirements.",
        ],
        "citations": [CIT_29148, CIT_INCOSE_REQ, CIT_SEBOK],
        "sig_lens": (
            "The Signature read: the AI is the surveyor's apprentice of "
            "the build contract - fast with the tape, tireless at flagging "
            "the crooked lines, but never the signatory. The Signature "
            "Build Method lets the apprentice draft and scan, then the "
            "master reviews every line and signs alone, because a contract "
            "signed by an apprentice is a promise with no one behind it."
        ),
    },
    {
        "key": "ml_specs",
        "name": "Specifying Machine Learning Systems",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Specifying a machine learning system means specifying what "
            "traditional specs never had to: the data, the learning "
            "objective, the performance metrics with their test protocol, "
            "the operating envelope, and the monitoring that watches the "
            "model after deployment. The data section names the sources, "
            "the labeling process and its quality bar, the train/validation/"
            "test splits, the class balance, and the known biases and gaps. "
            "The learning objective states what is optimized and what is "
            "constrained (accuracy vs latency vs fairness). Performance is "
            "specified as metrics with thresholds on a held-out test set "
            "plus the evaluation protocol that makes the numbers "
            "reproducible - seed, split, and metric definitions pinned. The "
            "operating envelope states where the model may be used (the "
            "data distribution it was validated on); outside the envelope, "
            "behavior is unspecified and the system must refuse or defer. "
            "Monitoring specifies the drift detection, the retraining "
            "triggers, and the rollback plan. This record covers the "
            "ML-specific sections that turn 'build us an AI' into a "
            "verifiable contract."
        ),
        "how_it_works": (
            "ML system specs work by pinning the four things that make "
            "models slippery. First the data: every source named, the "
            "labeling procedure with its agreement metric (inter-annotator "
            "agreement target), the split ratios, the class distribution, "
            "and the documented limitations - because a model is a "
            "compression of its training data, and unspecified data is "
            "unspecified behavior. Second the objective: the primary "
            "metric to maximize, the constraints (latency budget, model "
            "size, fairness thresholds across groups), and the trade "
            "priorities between them. Third the evaluation: metric "
            "definitions, the held-out test set construction, the minimum "
            "thresholds per metric, and the reproducibility pins (random "
            "seeds, library versions, split identifiers) so the numbers can "
            "be re-earned. Fourth the envelope and the watch: the input "
            "distribution the model was validated on, the out-of-envelope "
            "behavior (refuse, defer to human, or flag), the drift metrics "
            "with alert thresholds, the retraining trigger conditions, and "
            "the rollback procedure to the last good model. Acceptance runs "
            "the evaluation protocol on the held-out set; deployment "
            "monitors the envelope; breach of the envelope triggers the "
            "specified response, not a meeting."
        ),
        "key_points": [
            "Data specified: sources, labeling process with agreement target, splits, class balance, documented limitations - unspecified data is unspecified behavior.",
            "Objective specified: primary metric, constraints (latency, size, fairness), and the trade priorities between them.",
            "Evaluation specified: metric definitions, held-out test construction, thresholds, and reproducibility pins (seeds, versions, split IDs).",
            "Operating envelope specified: the validated input distribution, and the mandated behavior outside it (refuse, defer, or flag).",
            "Monitoring specified: drift metrics with alert thresholds, retraining triggers, and the rollback plan to the last good model.",
        ],
        "requirements": [
            "A data section naming sources, labeling quality bar, splits, class balance, and known limitations.",
            "A learning objective with primary metric, constraints, and trade priorities.",
            "An evaluation protocol with metric definitions, thresholds, and reproducibility pins.",
            "An operating envelope with specified out-of-envelope behavior and drift monitoring with triggers and rollback.",
        ],
        "standards": [
            "ML system documentation per the project's AI/ML engineering standard; data handling per applicable privacy regulation.",
            "Verification of ML performance per ISO/IEC/IEEE 29148 verification principles adapted to statistical evaluation.",
        ],
        "citations": [CIT_29148, CIT_SOMMERVILLE, CIT_SEBOK],
        "sig_lens": (
            "The Signature read: an ML spec is a build contract for a "
            "machine that learns - so the contract specifies the "
            "schooling (data), the exams (evaluation), the jurisdiction "
            "(envelope), and the parole hearings (monitoring). The "
            "Signature Build Method never commissions a learner without "
            "all four, because an unexamined model in an unmapped "
            "jurisdiction is not a product but a rumor with a GPU."
        ),
    },
    {
        "key": "cps",
        "name": "Specifying Cyber-Physical Systems",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Cyber-physical systems - robots, vehicles, industrial control, "
            "medical devices - are specified where software deadlines meet "
            "physical consequences, and the spec must cover both worlds plus "
            "their coupling. Beyond the software and hardware sections, a "
            "CPS spec adds: the physical plant model (what is being "
            "controlled, with its dynamics), the timing architecture "
            "(control loop rates, end-to-end latency budgets per path, "
            "jitter limits), the safety architecture (safe states, "
            "redundancy, diagnostics), the human-machine interface and its "
            "authority rules (who can override what, and what the system "
            "does when the human disagrees), and the environmental envelope "
            "the physical side must survive. The latency budget is the "
            "characteristic analysis: sense, compute, actuate times summed "
            "per control path against the deadline the physics demands, "
            "with margin. A late brake command is not a slow feature; it "
            "is a failed requirement. This record covers the CPS-specific "
            "sections and the timing-budget discipline."
        ),
        "how_it_works": (
            "CPS specs work by specifying the loop, not just the parts. The "
            "plant model describes the physics under control - masses, "
            "inertias, thermal constants, the equations or the identified "
            "parameters the controller was designed against - with the "
            "parameter uncertainty stated. The timing architecture then "
            "names every control path (sensor to actuator through the "
            "compute), assigns each a rate, an end-to-end deadline, and a "
            "jitter limit, and budgets the latency: sensing time plus "
            "transport plus compute plus actuation, summed against the "
            "deadline with margin, worst-case not average. The safety "
            "architecture names the safe states, the fault detection that "
            "triggers them, and the time allowed to reach them. The "
            "human-machine interface specifies the authority ladder: what "
            "the human may command, what the system may refuse, what "
            "happens on disagreement, and the handover protocol with its "
            "timing. The environmental envelope states the physical "
            "conditions the system must operate through. Verification is "
            "then layered: model-in-the-loop (controller against the plant "
            "model), software-in-the-loop, hardware-in-the-loop (real "
            "compute against simulated physics), and finally the physical "
            "system - each layer's exit criteria specified before it "
            "begins."
        ),
        "key_points": [
            "Specify the loop: plant model with parameter uncertainty, control paths with rates, deadlines, and jitter limits.",
            "Latency budget per path: sense + transport + compute + actuate, worst-case, summed against the physics deadline with margin.",
            "Safety architecture: named safe states, fault detection, and the time allowed to reach safety.",
            "Authority ladder for the human-machine interface: what the human may command, what the system may refuse, the handover protocol.",
            "Layered verification: model-, software-, hardware-in-the-loop, then the physical system - each with specified exit criteria.",
        ],
        "requirements": [
            "A plant model with dynamics and stated parameter uncertainty.",
            "Timing architecture: every control path with rate, end-to-end deadline, jitter limit, and a worst-case latency budget with margin.",
            "A safety architecture with safe states, detection, and time-to-safety.",
            "An authority ladder and handover protocol for human-machine interaction.",
        ],
        "standards": [
            "Functional safety per IEC 61508 or ISO 26262; timing analysis per the domain's real-time standard.",
            "System safety per MIL-STD-882E for the hazard analysis feeding the safety architecture.",
        ],
        "citations": [CIT_61508, CIT_26262, CIT_MIL882, CIT_29148],
        "sig_lens": (
            "The Signature read: a CPS spec is a build contract for a "
            "machine with a body - the software is the reflexes, the "
            "physics is the flesh, and the timing budget is the promise "
            "that reflex meets flesh in time. The Signature Build Method "
            "budgets every millisecond worst-case, because in a body, a "
            "late reflex is not slow; it is broken."
        ),
    },
    {
        "key": "contracts",
        "name": "Contracts and Statements of Work",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "The contract and its Statement of Work (SOW) are the build "
            "specification with legal force: the SOW states what will be "
            "built, delivered, and accepted, and the contract states the "
            "commercial terms around it - price, schedule, payment "
            "milestones, intellectual property, warranties, liabilities, "
            "and termination. The SOW's technical heart is the spec itself: "
            "objectives, deliverables, requirements, acceptance criteria - "
            "referenced or incorporated, with the version pinned, so the "
            "legal promise and the engineering promise are the same "
            "document. Payment milestones tie money to accepted "
            "deliverables, never to elapsed time: the vendor is paid for "
            "cargo, not for effort. IP clauses state who owns what is "
            "created (work for hire, license-back, background IP carve-"
            "outs); warranty clauses state what defects are fixed free and "
            "for how long; liability caps and termination terms bound the "
            "worst cases. This record covers the SOW structure, the "
            "milestone discipline, and the clauses that prevent the "
            "classic contractual disasters."
        ),
        "how_it_works": (
            "Contracts work by converting the engineering spec into an "
            "enforceable exchange. The SOW is written first, in engineering "
            "language: scope (in and out), deliverables with acceptance "
            "criteria, schedule with milestones, and the pinned spec "
            "version that defines the technical truth. The contract then "
            "wraps it commercially: fixed-price (the vendor owns the "
            "estimating risk), time-and-materials with a cap (the buyer "
            "owns it, bounded), or cost-plus (for R and D where nobody can "
            "price the unknown) - the type chosen deliberately and stated. "
            "Payment milestones are tied to accepted deliverables: each "
            "milestone names the deliverable, its acceptance criteria, and "
            "the amount released on sign-off. IP ownership is stated "
            "plainly: what the buyer owns, what the vendor retains, what "
            "third-party components are licensed and on what terms. "
            "Warranty states the defect-fix obligation and its duration; "
            "liability states the caps; termination states the off-ramps "
            "and what the buyer keeps if the road ends early. Change "
            "control is contractual too: the SOW's change clause names who "
            "may request, who approves, and how price and schedule adjust - "
            "so scope growth is priced, not absorbed."
        ),
        "key_points": [
            "The SOW is the spec with legal force: scope, deliverables, acceptance criteria, schedule, pinned spec version - the engineering and legal promises are one document.",
            "Contract type is chosen deliberately: fixed-price, T and M with cap, or cost-plus - each assigns the estimating risk differently.",
            "Payment milestones tie money to accepted deliverables, never to elapsed time: paid for cargo, not for effort.",
            "IP, warranty, liability, termination: who owns what is created, what defects are fixed free and for how long, the caps, the off-ramps.",
            "The change clause prices scope growth: who may request, who approves, how price and schedule adjust.",
        ],
        "requirements": [
            "An SOW with scope in/out, deliverables, acceptance criteria, schedule, and the pinned spec version.",
            "A declared contract type with its risk assignment understood by both parties.",
            "Payment milestones tied to accepted deliverables with amounts per milestone.",
            "IP ownership, warranty, liability, and termination clauses stated plainly.",
        ],
        "standards": [
            "Contracting practices per organizational procurement policy and applicable law; technical content per ISO/IEC/IEEE 29148.",
            "IP and data-rights clauses per the applicable government or commercial framework where relevant.",
        ],
        "citations": [CIT_29148, CIT_PMBOK, CIT_15288],
        "sig_lens": (
            "The Signature read: the contract is the build contract with "
            "the force of law behind it - the SOW the engineering promise, "
            "the clauses the commercial walls around it. The Signature "
            "Build Method ties every payment to accepted cargo and prices "
            "every change, because a contract that pays for effort instead "
            "of cargo is a subscription to disappointment."
        ),
    },
    {
        "key": "executable",
        "name": "Executable Specifications and Digital Twins",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "An executable specification is a spec that can be run: the "
            "requirements captured as models, simulations, or formal "
            "assertions that execute against candidate designs before "
            "anything is built. A digital twin is the fullest form - a "
            "live simulation of the system, fed by the spec's parameters, "
            "used to verify requirements, explore trade-offs, and later to "
            "mirror the fielded system for monitoring and prediction. The "
            "spec defines the twin's fidelity requirements (what must be "
            "modeled and how accurately), the parameter set with tolerances, "
            "the scenarios it must execute, and the pass criteria for each. "
            "Simpler executable forms include decision tables, state "
            "machines with simulators, and property-based test generators "
            "derived from the requirements. The discipline is that the "
            "executable form and the written form are kept consistent - "
            "the model is generated from the spec or the spec from the "
            "model, never maintained as two truths. This record covers the "
            "executable spectrum, twin fidelity requirements, and the "
            "single-truth discipline."
        ),
        "how_it_works": (
            "Executable specs work by turning requirements into runnable "
            "checks. The author captures each verifiable requirement in an "
            "executable form alongside its prose: a decision table for "
            "logic requirements, a state machine for behavioral ones, a "
            "parametric model for physical ones, a property-based test for "
            "invariants. The digital twin assembles these into a system "
            "simulation with the spec's parameter set - every parameter "
            "with its tolerance - and the spec names the fidelity required: "
            "which physics must be modeled, to what accuracy, validated "
            "against what reference data. Scenarios from the verification "
            "plan are executed against the twin: nominal, off-nominal, and "
            "fault-injection cases, each with pass criteria. Trade studies "
            "run on the twin before metal is cut or code is frozen - the "
            "twin earns its keep by killing bad designs cheaply. After "
            "deployment, the twin mirrors the fielded system: live data "
            "feeds the model, the model predicts remaining life and flags "
            "drift, and discrepancies between twin and reality become "
            "requirements issues, not mysteries. The single-truth rule "
            "holds throughout: the written spec and the executable model "
            "are two views of one baseline, changed together or not at all."
        ),
        "key_points": [
            "Executable forms: decision tables, simulatable state machines, parametric models, property-based tests - each requirement runnable alongside its prose.",
            "Digital twin fidelity is specified: what physics, what accuracy, validated against what reference data.",
            "Scenarios execute against the twin: nominal, off-nominal, fault-injection - each with pass criteria from the verification plan.",
            "Trade studies run on the twin before commitment: bad designs die cheaply in simulation.",
            "Single-truth rule: written spec and executable model are two views of one baseline, changed together or not at all.",
        ],
        "requirements": [
            "Executable captures for the verifiable requirements, in forms matched to their kind.",
            "Twin fidelity requirements: modeled physics, accuracy targets, and reference validation data.",
            "A scenario suite from the verification plan with pass criteria per scenario.",
            "A single-truth procedure keeping the written and executable forms consistent.",
        ],
        "standards": [
            "Modeling per OMG SysML where model-based; simulation verification per the project's modeling and simulation standard.",
            "Verification credit for simulation results per the applicable authority (domain-dependent).",
        ],
        "citations": [CIT_SYSML, CIT_15288, CIT_NASA],
        "sig_lens": (
            "The Signature read: an executable spec is a build contract "
            "that can be rehearsed - the twin a full-scale rehearsal "
            "stage where designs perform before the real build. The "
            "Signature Build Method rehearses every risky act in "
            "simulation, because a contract performed once in rehearsal "
            "rarely fails on opening night."
        ),
    },
    {
        "key": "fmea",
        "name": "Failure Analysis in Specifications: FMEA and FTA",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Failure analysis in the spec proves the design was interrogated "
            "about its deaths before it was built. FMEA (Failure Mode and "
            "Effects Analysis) works bottom-up: for each component or "
            "function, list the ways it can fail, the effect of each "
            "failure, and score severity (S), occurrence (O), and detection "
            "(D) - the Risk Priority Number RPN = S x O x D ranks the "
            "modes, and the highest get design actions. FTA (Fault Tree "
            "Analysis) works top-down: start from a feared top event (loss "
            "of braking, data corruption) and decompose through logic gates "
            "(AND, OR) to the basic events that can cause it, revealing the "
            "single points of failure and the minimal cut sets. The spec "
            "requires the analyses, names their scope and method standard "
            "(SAE J1739 for FMEA, IEC 61025 for FTA), sets the RPN action "
            "thresholds, and turns the resulting design actions into "
            "requirements - traced, like all the rest. This record covers "
            "both methods, the scoring discipline, and the action-to-"
            "requirement flow."
        ),
        "how_it_works": (
            "FMEA works as a structured interrogation of every item in "
            "scope. The team takes each component or function and asks: how "
            "can this fail (the mode), what happens then (the effect, "
            "traced to the system level), how bad is it (severity 1-10, "
            "where 9-10 means safety or regulatory impact), how likely "
            "(occurrence 1-10 from field data or judgment), and how likely "
            "are we to catch it before the customer does (detection 1-10, "
            "where 10 means undetectable). RPN = S x O x D; the spec sets "
            "action thresholds (e.g. any severity 9-10, or RPN above 100, "
            "gets a mandatory design action). Each action - add redundancy, "
            "add diagnostics, derate the part, change the design - becomes "
            "a requirement with its verification method. FTA works from "
            "the other end: the top event is stated, and the tree is built "
            "downward through AND/OR gates to basic events with their "
            "probabilities; the analysis computes the top-event probability "
            "and extracts the minimal cut sets - the smallest combinations "
            "of basic events that cause the top event. Single-event cut "
            "sets are single points of failure and get design actions by "
            "rule. Both analyses are living: they are updated when the "
            "design changes, and the spec requires the update."
        ),
        "key_points": [
            "FMEA bottom-up: per item, failure modes -> effects -> S x O x D scores -> RPN ranking -> design actions for the highest.",
            "FTA top-down: feared top event -> AND/OR decomposition -> basic events -> minimal cut sets; single-event cut sets are single points of failure.",
            "The spec sets RPN action thresholds (e.g. severity 9-10 or RPN above 100 mandates action) - thresholds are declared, not improvised.",
            "Every design action becomes a traced requirement with a verification method.",
            "Both analyses are living documents, updated on every design change - the spec requires the update.",
        ],
        "requirements": [
            "Required FMEA and FTA with declared scope, method standard, and scoring scales.",
            "Declared RPN and severity action thresholds.",
            "Design actions from both analyses converted to traced requirements.",
            "An update obligation: analyses refreshed on every design change.",
        ],
        "standards": [
            "FMEA per SAE J1739; FTA per IEC 61025.",
            "Safety-related actions per IEC 61508 / ISO 26262 / MIL-STD-882E as applicable.",
        ],
        "citations": [CIT_J1739, CIT_IEC61025, CIT_61508],
        "sig_lens": (
            "The Signature read: FMEA and FTA are the autopsy and the "
            "prophecy of the build contract - one dissects every part for "
            "its ways to die, the other traces every feared death to its "
            "causes. The Signature Build Method holds both inquests before "
            "building, because a contract that never imagined its failures "
            "will meet them unintroduced."
        ),
    },
    {
        "key": "inspections",
        "name": "Formal Specification Reviews and Inspections",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Formal reviews and inspections are the spec's quality gates: "
            "structured examinations that find defects in the specification "
            "itself before they become defects in the build. The classic is "
            "Fagan inspection - a team of reviewers (author, moderator, "
            "readers, testers) examines a small section against checklists "
            "in a time-boxed meeting, logging every defect with its severity "
            "and location; the author fixes, the moderator verifies, and "
            "the metrics (defect density, inspection rate) are recorded. "
            "Lighter forms - walkthroughs, peer reviews, checklist reviews - "
            "trade rigor for speed on lower-risk sections. The spec's "
            "review plan names which sections get which rigor, who reviews "
            "them, the entry criteria (the draft must be complete enough to "
            "review), and the exit criteria (defect thresholds met, all "
            "majors fixed). Review metrics are kept across projects: "
            "defect density found in inspection predicts defect density "
            "that would have reached the build. This record covers the "
            "inspection method, the review plan, and the metrics discipline."
        ),
        "how_it_works": (
            "Formal inspection works by ritualized reading. The moderator "
            "schedules the inspection only when the entry criteria are met "
            "(the section is complete, the checklists are ready, reviewers "
            "are assigned). Reviewers prepare individually, reading the "
            "section against the checklists - the 29148 well-formedness "
            "rules, the anatomy completeness list, the domain checks - and "
            "logging candidate defects before the meeting. The meeting "
            "itself is time-boxed (Fagan's data: about two hours, about 150 "
            "lines or the requirements equivalent per hour); the reader "
            "paraphrases the spec while the team hunts defects, which the "
            "moderator logs with severity (major: wrong or missing "
            "requirement; minor: clarity, style). No solutions are designed "
            "in the meeting - that is the author's job afterward. The "
            "author reworks, the moderator verifies the fixes, and the "
            "inspection closes only when the exit criteria hold: all majors "
            "fixed and verified, defect density below the threshold, "
            "re-inspection triggered if the defect count was high. Metrics "
            "are recorded per inspection: preparation rate, meeting rate, "
            "defects per hour, defect density per page - the data that "
            "calibrates the next project's review plan and proves, over "
            "time, that inspection pays for itself many times over."
        ),
        "key_points": [
            "Fagan inspection: moderator-led, checklist-driven, time-boxed examination of small sections; defects logged with severity and location.",
            "Preparation is individual and mandatory: reviewers arrive with candidate defects already logged.",
            "Meetings find defects; they do not design solutions - the author reworks afterward, the moderator verifies.",
            "Exit criteria: all majors fixed and verified, defect density below threshold, re-inspection on high counts.",
            "Metrics per inspection (rates, densities) calibrate future review plans and prove the return on inspection.",
        ],
        "requirements": [
            "A review plan naming the rigor level per spec section, the reviewers, and entry/exit criteria.",
            "Checklists covering well-formedness, anatomy completeness, and domain checks.",
            "Defect logging with severity, location, and fix verification.",
            "Inspection metrics recorded per session for calibration.",
        ],
        "standards": [
            "Inspection method per Fagan (IBM Systems Journal, 1976) and Gilb and Graham Software Inspection.",
            "Peer review processes per CMMI verification process area where applicable.",
        ],
        "citations": [CIT_FAGAN, CIT_GILB, CIT_CMMI],
        "sig_lens": (
            "The Signature read: inspection is the proofreading of the "
            "build contract by a jury of its readers - each line read "
            "aloud, each defect logged, each fix verified before the seal. "
            "The Signature Build Method never seals an unread contract, "
            "because a defect in the contract is a defect in everything "
            "built from it, multiplied."
        ),
    },
    {
        "key": "handoff",
        "name": "From Specification to Manufacture: The Build Handoff",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "The build handoff is the moment the specification becomes a "
            "manufacturing reality: the spec, the design, and the "
            "verification evidence are transferred to the builders - the "
            "factory, the dev team, the integration line - with everything "
            "they need and nothing they must guess. The handoff package "
            "contains the baselined spec and its change history, the design "
            "baseline (drawings, schematics, source, models), the bill of "
            "materials with approved sources, the manufacturing or build "
            "instructions, the acceptance test procedures, the tooling and "
            "fixture requirements, and the known-issues list with "
            "workarounds. The receiving party performs a handoff review: "
            "can we build this, with these tools, from these sources, to "
            "these tests? Gaps found here are cheap; gaps found on the line "
            "are expensive. First-article inspection (or the software "
            "equivalent, the first release candidate) proves the handoff "
            "worked: the first units off the line are measured against the "
            "spec in full. This record covers the handoff package, the "
            "receiving review, and the first-article proof."
        ),
        "how_it_works": (
            "The handoff works as a formal transfer with a receipt. The "
            "authoring team assembles the package: the baselined spec with "
            "its full change history, the design baseline (every drawing "
            "released, every schematic, the source at its tagged version, "
            "the models), the bill of materials where every line has an "
            "approved manufacturer and part number (no 'or equivalent' "
            "without the equivalence criteria), the build instructions at "
            "the fidelity the builders need, the acceptance test procedures "
            "with their fixtures and limits, and the known-issues list so "
            "the builders inherit knowledge, not mysteries. The receiving "
            "team reviews the package against a checklist: sourceability "
            "(can we buy every BOM line?), buildability (do our tools and "
            "processes match the instructions?), testability (can we run "
            "every acceptance test?). Findings go back as formal feedback, "
            "not as silent workarounds. On approval, the first article is "
            "built and inspected against the full spec - every requirement "
            "with an inspection or test method gets exercised on the first "
            "units. First-article approval authorizes production; "
            "first-article failure returns the package for correction. The "
            "handoff record, with its package manifest and review minutes, "
            "is filed with the product baseline - the chain of custody from "
            "request to reality, complete."
        ),
        "key_points": [
            "The handoff package: baselined spec + change history, design baseline, BOM with approved sources, build instructions, acceptance tests, tooling, known issues.",
            "BOM lines name approved manufacturers and part numbers; 'or equivalent' is allowed only with written equivalence criteria.",
            "The receiving review asks three questions: sourceable, buildable, testable - findings return as formal feedback.",
            "First-article inspection proves the handoff: the first units measured against the full spec before production is authorized.",
            "The handoff record (package manifest + review minutes) is filed with the product baseline.",
        ],
        "requirements": [
            "A handoff package manifest listing every transferred artifact with its version.",
            "A BOM with approved sources for every line and equivalence criteria where alternates are allowed.",
            "A receiving review with the sourceable/buildable/testable checklist and formal findings.",
            "First-article inspection against the full spec with approval before production.",
        ],
        "standards": [
            "First-article inspection per AS9102 concepts (or the domain equivalent); configuration control per ISO/IEC/IEEE 15288.",
            "Manufacturing documentation per the applicable quality standard (ISO 9001, AS9100, etc.).",
        ],
        "citations": [CIT_15288, CIT_9001, CIT_ULRICH],
        "sig_lens": (
            "The Signature read: the handoff is the delivery of the build "
            "contract's cargo - the sealed spec, the proven design, and "
            "the tested first article, handed over with a receipt. The "
            "Signature Build Method delivers the whole package and proves "
            "the first article, because a contract is not complete when it "
            "is signed; it is complete when the first real thing passes "
            "inspection."
        ),
    },
]
