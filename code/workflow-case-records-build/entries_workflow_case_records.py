#!/usr/bin/env python3
"""Entries for the Workflow and Case Records databases (missing-115 program,
Wave 1 - operational data, Manon's #1 priority).

Verified 2026-10-17: RAW SWEEP over the full manifest plus every shard index
title in jah-databases-data-1 plus the main-repo data dir: zero
'workflow-case*' slugs/names; zero 'Workflow and Case Records' title
collisions. The two keyword near-hits are distinct capabilities:
'ai-workflows' is about AI agent/tool workflows, and 'project-workflow'
(JAH Project Workflow Database) is about project scheduling and phases -
neither carries workflow patterns, state machines, BPMN, SLA tracking,
escalation paths, case-management lifecycles, or audit trails of status
changes as its record schema. The paste's rule was applied by name/purpose/
record schema/capabilities: workflow and case operational records are a
distinct capability - BUILD NEW is the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  workflow-case-records              - The Workflow and Case Records Database
                                       (public-harvest: real, fact-checked
                                       operational workflow and case data -
                                       tasks, ownership, status transitions,
                                       deadlines, dependencies, outcomes;
                                       workflow patterns, state machines,
                                       BPMN 2.0, case-management lifecycles,
                                       SLA tracking, escalation paths,
                                       handoffs, audit trails; standard
                                       references van der Aalst et al.
                                       Workflow Patterns (MIT Press 2006);
                                       OMG BPMN 2.0; OMG CMMN 1.1; Dumas et
                                       al. Fundamentals of Business Process
                                       Management 2nd ed 2018; Weske BPM 3rd
                                       ed 2019; WfMC Workflow Reference
                                       Model; PMBOK Guide 7th ed 2021; ITIL 4
                                       2019; Little's queuing formula 1961;
                                       CPM (Kelley and Walker 1959);
                                       Swenson Adaptive Case Management 2010;
                                       Garcia-Molina and Salem Sagas 1987;
                                       and the other landmarks cited per
                                       record)
  workflow-case-records-signature    - The Workflow and Case Records Signature
                                       Database
                                       (his original Signature Operations
                                       Method: every task a sworn charge,
                                       every status a witnessed station, every
                                       handoff a sealed covenant, every audit
                                       trail an unbroken chain of testimony;
                                       src signature, titles suffixed
                                       " (Signature Edition)", never
                                       presented as authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-WFR- (public) and JAH-WFRS- (signature), verified free in
the manifest id_prefix values and in every shard index file (zero hits).

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see demos_workflow_case_records.py). Every demo prints its real
computed values, asserts tight bounds (never float exact-equality), and
ends with the OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian operational scope only - nothing about neutralizing or defeating
military or defense-grade systems.
"""

SIG_TAIL = ("Signature original - his original Signature Operations Method: "
            "every task a sworn charge, every status a witnessed station, "
            "every handoff a sealed covenant, and every audit trail an "
            "unbroken chain of testimony. Clearly labeled Signature-made, "
            "never presented as authentic public record.")

CIT_WF_PATTERNS = ("van der Aalst WMP, ter Hofstede AHM, Kiepuszewski B, "
                   "Barros AP. Workflow Patterns: The Definitive Guide. "
                   "MIT Press; 2006.")
CIT_BPMN = ("Object Management Group. Business Process Model and Notation "
            "(BPMN), Version 2.0.2. OMG Document formal/2013-12-09; 2013.")
CIT_DUMAS = ("Dumas M, La Rosa M, Mendling J, Reijers HA. Fundamentals of "
             "Business Process Management. 2nd ed. Springer; 2018.")
CIT_WESKE = ("Weske M. Business Process Management: Concepts, Languages, "
             "Architectures. 3rd ed. Springer; 2019.")
CIT_CMMN = ("Object Management Group. Case Management Model and Notation "
            "(CMMN), Version 1.1. OMG Document formal/2016-12-01; 2016.")
CIT_DMN = ("Object Management Group. Decision Model and Notation (DMN), "
           "Version 1.3. OMG Document dtc/2021-01-01; 2021.")
CIT_WFMC = ("Workflow Management Coalition. The Workflow Reference Model. "
            "WfMC-TC-1003; 1995.")
CIT_PMBOK = ("Project Management Institute. A Guide to the Project Management "
             "Body of Knowledge (PMBOK Guide). 7th ed. PMI; 2021.")
CIT_ITIL = ("AXELOS. ITIL Foundation: ITIL 4 Edition. TSO; 2019.")
CIT_LITTLE = ("Little JDC. A Proof for the Queuing Formula: L = lambda W. "
              "Operations Research. 1961;9(3):383-387.")
CIT_KELLEY = ("Kelley JE Jr, Walker MR. Critical-Path Planning and "
              "Scheduling. Proceedings of the Eastern Joint Computer "
              "Conference; 1959.")
CIT_SWENSON = ("Swenson KD. Mastering the Unpredictable: How Adaptive Case "
               "Management Will Revolutionize the Way That Knowledge Workers "
               "Get Things Done. Meghan-Kiffer Press; 2010.")
CIT_SAGA = ("Garcia-Molina H, Salem K. Sagas. Proceedings of the 1987 ACM "
            "SIGMOD International Conference on Management of Data; 1987.")
CIT_NEWMAN = ("Newman S. Building Microservices. 2nd ed. O'Reilly Media; "
              "2021.")
CIT_MINING = ("van der Aalst WMP. Process Mining: Data Science in Action. "
              "2nd ed. Springer; 2016.")
CIT_YAWL = ("ter Hofstede AHM, van der Aalst WMP. YAWL: Yet Another Workflow "
            "Language. Information Systems. 2005;30(4):245-275.")

ENTRIES = [
    {
        "key": "what_is_workflow",
        "name": "What Is a Workflow",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "A workflow is work with its path drawn: a defined sequence of "
            "tasks, decisions, and handoffs that turns an input into an "
            "outcome. Every workflow has the same anatomy - a trigger that "
            "starts it, a set of tasks performed by owners, decision points "
            "that branch the path, handoffs that move responsibility from one "
            "party to another, and a completion state that marks the work "
            "done. Drawing the path is what separates a workflow from a pile "
            "of tasks: the path makes the work repeatable, measurable, and "
            "improvable. A hiring workflow runs the same steps for every "
            "candidate; an invoice workflow pays every supplier by the same "
            "rules. This record frames the whole database: every later "
            "record is one instrument for drawing, running, measuring, or "
            "proving the path."
        ),
        "how_it_works": (
            "A workflow works by converting a case - one run through the "
            "process, like one order or one ticket - into a chain of "
            "state changes. The case is born at the trigger with a unique "
            "identifier and an initial status. Each task in the path moves "
            "the case forward when its owner completes it; each decision "
            "point reads the case data and selects which branch to take; "
            "each handoff reassigns the owner while the case keeps its "
            "identity. The workflow engine or the team follows the drawn "
            "path, and every step leaves a record: who did what, when, and "
            "what the case looked like afterward. At completion the case "
            "reaches a terminal status - fulfilled, resolved, closed - and "
            "its history becomes the evidence the process worked. The path "
            "is the asset: improve the path once and every future case "
            "benefits."
        ),
        "key_points": [
            "A workflow is work with its path drawn: trigger, tasks, decisions, handoffs, and a completion state - the path is what makes work repeatable, measurable, and improvable.",
            "A case is one run through the process; the case identifier follows the work from trigger to completion so every step can be audited.",
            "Tasks change the case, decisions branch it, handoffs move its ownership - these three moves are the vocabulary of every workflow on the ladder.",
            "Every step leaves a record of who, what, and when; the record trail is what turns activity into evidence.",
            "Improve the path once and every future case inherits the improvement - that leverage is why workflows are drawn at all.",
        ],
        "requirements": [
            "A named trigger that starts a case and the condition that fires it.",
            "A task list where every task has exactly one owner at any moment.",
            "Decision points with explicit conditions, never ambiguous forks.",
            "A defined completion state so a case can be recognized as done.",
            "A unique case identifier carried through every step and record.",
        ],
        "standards": [
            "Workflow definitions separate the model (the drawn path) from the instance (one case running) - the Workflow Management Coalition reference model makes this separation the foundation.",
            "Case identifiers are unique, stable, and never reused across cases.",
            "Completion criteria are written before the workflow runs, not invented when it ends.",
        ],
        "citations": [CIT_WFMC, CIT_DUMAS, CIT_WESKE],
        "sig_lens": (
            "The Signature read: a workflow is a sworn road, and every case "
            "is a traveler the road is sworn to deliver. Where public "
            "operations draws a path, the Signature Operations Method takes "
            "an oath on it: the trigger is the call, the owner is the "
            "sworn bearer, the decision is the witnessed fork, the handoff "
            "is the sealed covenant, and completion is the fulfilled charge."
        ),
    },
    {
        "key": "tasks_cases_processes",
        "name": "Tasks, Cases, and Processes",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Task, case, and process are the three nouns of operations, and "
            "mixing them up is the most common beginner error. A task is one "
            "unit of work with a doer, a deadline, and a done state - "
            "review the invoice, call the client, pack the box. A case is "
            "one instance of work flowing through the process - order 4471, "
            "ticket 882, application 2210 - and it carries its own data, "
            "history, and status. A process is the defined path itself - the "
            "order-to-cash process, the hiring process - which many cases run "
            "through at once. One process spawns many cases; one case holds "
            "many tasks; one task belongs to exactly one case at a time. "
            "Keeping the three levels straight is what lets a team measure "
            "the right thing: task cycle times, case outcomes, and process "
            "health are three different dashboards."
        ),
        "how_it_works": (
            "The three levels work as a hierarchy. The process definition "
            "declares the task template: what must be done, in what order, "
            "by which roles. When the trigger fires, a case is created as a "
            "container holding the case data (customer, amount, priority), "
            "the current status, and the task list instantiated from the "
            "template. Tasks are the atomic records: each has an owner, a "
            "due date, and a status that flips from open to done. As tasks "
            "complete, the case status advances; when the final task closes, "
            "the case closes. Reporting rolls upward: task durations reveal "
            "bottlenecks, case outcomes reveal effectiveness, and process "
            "metrics - throughput, error rate, average cycle time - reveal "
            "whether the path itself needs redesign. The hierarchy keeps "
            "every question at its proper altitude."
        ),
        "key_points": [
            "Task, case, and process are three levels: one task is one unit of work, one case is one run through the path, one process is the path itself.",
            "One process spawns many cases; one case holds many tasks; one task belongs to exactly one case at a time.",
            "Task metrics reveal bottlenecks, case metrics reveal outcomes, process metrics reveal whether the path needs redesign - measure at the right altitude.",
            "The case container holds the data, history, and status that every task and decision in the run reads and writes.",
            "Naming the level correctly is the first discipline: say task when you mean a unit of work, case when you mean a run, process when you mean the path.",
        ],
        "requirements": [
            "A process definition naming its task template and the roles that perform it.",
            "A case record created at each trigger with a unique identifier and initial status.",
            "Task records each with one owner, one due date, and one status.",
            "A case status that advances only through defined transitions as tasks complete.",
            "Separate task, case, and process reporting so no level's metrics pollute another's.",
        ],
        "standards": [
            "Process definitions distinguish the model from its instances, following the WfMC workflow reference model.",
            "Case data is separated from task data: case fields describe the run, task fields describe the unit of work.",
            "Statuses are drawn from a controlled vocabulary shared across the process - free-text status is a defect.",
        ],
        "citations": [CIT_WFMC, CIT_DUMAS, CIT_WESKE],
        "sig_lens": (
            "The Signature read: the process is the sworn road, the case is "
            "the traveler, and the task is each step the bearer takes. The "
            "Signature Operations Method keeps the three stations distinct - "
            "road, traveler, and step - so that no oath is sworn at the "
            "wrong altar and every station keeps its own testimony."
        ),
    },
    {
        "key": "ownership_roles",
        "name": "Ownership and Roles",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "Ownership is the answer to the question every stuck case is "
            "really asking: whose job is this right now. A workflow where "
            "every task has exactly one owner moves; a workflow where "
            "ownership is shared or vague stalls. Roles name the kinds of "
            "involvement: the owner does the work, the approver says yes, "
            "the contributor supplies input, the watcher stays informed. "
            "The RACI matrix - Responsible, Accountable, Consulted, Informed "
            "- is the classic instrument: one accountable party per task, "
            "one or more responsible doers, and explicit consult and inform "
            "lists. The discipline is transfer: ownership must be "
            "handed off, never dropped, and the record must show the "
            "current owner at every moment. A case with no owner is a case "
            "nobody is rescuing."
        ),
        "how_it_works": (
            "Ownership works by single-threaded accountability. At case "
            "creation the first task's owner is assigned - a person or a "
            "role queue, never a void. The owner works the task; when it "
            "needs another party, a handoff transfers ownership explicitly, "
            "recording the from, the to, and the timestamp. Approvers enter "
            "only at defined gates; consultants are asked before the "
            "decision and the informed are notified after. The RACI check "
            "runs over the whole process: every task must have exactly one "
            "accountable party, at least one responsible doer, and no "
            "orphans. Queues - team inboxes that own tasks before a person "
            "claims them - give the model slack: the role owns the task, a "
            "member claims it, and ownership narrows to a name. Escalation "
            "is ownership transfer with urgency: the case climbs to a role "
            "with more authority, still exactly one owner at each rung."
        ),
        "key_points": [
            "Every task has exactly one owner at every moment; shared or vague ownership is how cases stall.",
            "RACI names the four involvements: one Accountable, at least one Responsible, explicit Consulted and Informed lists.",
            "Ownership transfers by handoff, never by dropping: the record always shows from, to, and when.",
            "Role queues own tasks before a person claims them, giving single accountability with team flexibility.",
            "A case with no current owner is an emergency - the first recovery step is always to assign one.",
        ],
        "requirements": [
            "Exactly one accountable owner per task, recorded and current.",
            "At least one responsible doer who performs the work.",
            "Explicit handoff records for every ownership transfer.",
            "Role queues with claim rules so unowned tasks are visible and claimable.",
            "A periodic orphan sweep that finds tasks with no owner and assigns them.",
        ],
        "standards": [
            "RACI assignments follow the PMBOK convention: exactly one A per task, at least one R, and named C and I parties.",
            "Owner changes are logged as handoff records with timestamp and reason, never silent reassignment.",
            "Queues publish their claim rules - who may claim, how fast, and what happens to unclaimed tasks.",
        ],
        "citations": [CIT_PMBOK, CIT_ITIL, CIT_WESKE],
        "sig_lens": (
            "The Signature read: ownership is a sworn charge, and a charge "
            "is borne by one bearer at a time. The Signature Operations "
            "Method holds that a task with two owners has none - the oath "
            "passes from hand to hand by sealed covenant, and the chain of "
            "bearers is itself the testimony of the case."
        ),
    },
]

ENTRIES.extend([
    {
        "key": "status_lifecycle",
        "name": "Status and the Status Lifecycle",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Status is the case's answer to the only question anyone ever "
            "asks about it: where is this now. A status lifecycle is the "
            "ordered set of stations a case may occupy - new, assigned, in "
            "progress, waiting, resolved, closed - plus the rules for which "
            "station may follow which. The rules matter more than the "
            "stations: a case that can jump from new straight to closed is a "
            "case whose record is fiction. Good lifecycles are small: five to "
            "eight statuses that everyone on the team can recite. Each "
            "status change is an event with a timestamp, an actor, and a "
            "reason, and the chain of these events is the case's biography. "
            "Waiting states deserve their own stations - waiting on customer, "
            "waiting on parts, waiting on approval - because a case that "
            "sits in a generic in-progress status is hiding its true age. "
            "The lifecycle is the backbone every later record - transitions, "
            "SLAs, escalations, audits - hangs on."
        ),
        "how_it_works": (
            "A status lifecycle works as a vocabulary plus a transition "
            "table. The vocabulary fixes the stations: open states where "
            "work is expected, waiting states where the case is blocked on "
            "something named, and terminal states where the case rests. The "
            "transition table fixes the legal moves: from assigned the case "
            "may go to in progress or back to new on reassignment, but never "
            "straight to closed. The system - or the team's discipline - "
            "enforces the table: an illegal transition is rejected with the "
            "reason, and the actor must route through the legal path, which "
            "usually means recording the missing work. Every legal "
            "transition appends a status-change record carrying the old "
            "status, the new status, the actor, the timestamp, and the "
            "reason. Reports read the lifecycle directly: cases by status, "
            "average dwell time per status, and the transitions that most "
            "often precede trouble."
        ),
        "key_points": [
            "Status is the case's answer to where it is now; the lifecycle is the ordered set of stations plus the rules for moving between them.",
            "The transition table matters more than the station list: a case that can jump from new to closed has a fictional record.",
            "Waiting states get their own named stations so a blocked case cannot hide inside a generic in-progress.",
            "Every status change is an event: old status, new status, actor, timestamp, reason - the chain of these events is the case biography.",
            "Keep the vocabulary small - five to eight statuses the whole team can recite - because a status nobody remembers is a status nobody sets.",
        ],
        "requirements": [
            "A controlled status vocabulary with open, waiting, and terminal stations defined.",
            "A transition table naming every legal move and forbidding the rest.",
            "A status-change record on every transition with actor, timestamp, and reason.",
            "Named waiting stations for each distinct blocker type.",
            "Enforcement of the transition table - illegal moves rejected, not silently allowed.",
        ],
        "standards": [
            "Status vocabularies are controlled lists; free-text status entry is prohibited.",
            "Transition tables are versioned with the process definition, so old cases keep their old table for audit.",
            "Dwell-time measurement starts when a status is entered and stops when it is left, including waiting stations.",
        ],
        "citations": [CIT_DUMAS, CIT_WESKE, CIT_ITIL],
        "sig_lens": (
            "The Signature read: each status is a witnessed station on the "
            "sworn road, and the transition table is the law of the road. "
            "The Signature Operations Method treats an illegal transition "
            "as a broken oath - the traveler may not appear at the far "
            "station without passing through the stations between, and "
            "every arrival is witnessed and recorded."
        ),
    },
    {
        "key": "deadlines_duedates",
        "name": "Deadlines and Due Dates",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A deadline is a promise with a date on it, and a workflow "
            "without dates is a wish list. Every task carries a due date; "
            "every case carries the commitments its tasks imply. Due dates "
            "come in flavors: the customer promise (the date the customer "
            "was told), the internal target (the date the team aims for, "
            "earlier than the promise), and the drop-dead limit (the date "
            "past which the outcome fails - a court filing, a contract "
            "expiry). The honest practice is to set all three and manage to "
            "the internal target, because a single date is always "
            "interpreted as the latest acceptable moment. Overdue is a "
            "status fact, not a moral judgment: the record says how many "
            "days past due, who owns it, and what unblocked it or did not. "
            "Deadlines only work when missing one has a consequence the "
            "team can name - an escalation, a notification, a replan - "
            "otherwise dates are decoration."
        ),
        "how_it_works": (
            "Deadlines work by arithmetic and attention. The arithmetic: "
            "lead time is the span from case start to required completion; "
            "planned duration is the span the task list needs; buffer is the "
            "difference, and the schedule is only sane when buffer is "
            "positive. Backward scheduling starts from the promise date and "
            "subtracts task durations and handoff gaps to find the latest "
            "start; forward scheduling starts from today and adds durations "
            "to find the earliest finish. The attention: due-date lists are "
            "reviewed on a cadence, and every overdue task gets its "
            "escalation or replan action, recorded. Renegotiation is legal "
            "but formal - a new promise date requires the customer's or the "
            "owner's agreement, logged in the audit trail, because a moved "
            "deadline that nobody agreed to is just a missed one with better "
            "makeup. On-time percentage - cases closed by their promise date "
            "divided by cases closed - is the headline reliability metric."
        ),
        "key_points": [
            "A deadline is a promise with a date; keep three dates - customer promise, internal target, drop-dead limit - and manage to the internal target.",
            "Lead time minus planned duration is buffer; a schedule with negative buffer is a plan to be late.",
            "Backward scheduling from the promise date finds the latest safe start; forward scheduling from today finds the earliest finish.",
            "Overdue is a status fact with an owner and an action - escalation, notification, or replan - not a moral judgment.",
            "Renegotiating a deadline is legal but formal: agreement logged in the audit trail, or the missed date stands.",
        ],
        "requirements": [
            "A due date on every task and a promise date on every case.",
            "Internal targets earlier than customer promises, with the gap explicit.",
            "A scheduled review cadence for due-date and overdue lists.",
            "A defined consequence for a missed date - escalation, notification, or replan.",
            "Formal renegotiation records when a promise date moves.",
        ],
        "standards": [
            "Dates are recorded with timezone and the precision the promise requires - a day promise needs a date, an hour promise needs a timestamp.",
            "On-time percentage is computed as cases closed by promise date over cases closed, over a fixed window.",
            "Lead-time and buffer calculations are shown in the schedule, not hidden in a planner's head.",
        ],
        "citations": [CIT_PMBOK, CIT_KELLEY, CIT_ITIL],
        "sig_lens": (
            "The Signature read: a deadline is an oath with a date, and the "
            "Signature Operations Method keeps three: the spoken promise to "
            "the customer, the earlier oath the team swears to itself, and "
            "the final limit past which the charge fails. A moved date is a "
            "re-sworn oath, witnessed and recorded, never a quiet erasure."
        ),
    },
    {
        "key": "handoffs",
        "name": "Handoffs Between People and Teams",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A handoff is the moment ownership of a case passes from one "
            "party to another, and it is where most workflows quietly lose "
            "their time. Studies of service processes keep finding the same "
            "pattern: the work itself takes hours while the waits between "
            "owners take days. A handoff has four parts - the giver, the "
            "receiver, the package (everything the receiver needs to "
            "continue), and the acknowledgment (the receiver confirming "
            "receipt and readiness). Dropped handoffs - where the giver "
            "assumes the receiver knows - are the classic failure; the "
            "receiver never got the package, the giver thinks the work "
            "moved on, and the case sits in the gap. The cure is ceremony "
            "proportionate to risk: a chat message for a simple pass, a "
            "checklist and sign-off for a critical one, and always a record."
        ),
        "how_it_works": (
            "A handoff works as a three-beat ritual. Beat one, the giver "
            "assembles the package: the case state, what was done, what "
            "remains, the gotchas, and the deadline. Beat two, the receiver "
            "acknowledges: not just received, but ready, with any questions "
            "asked now rather than discovered later. Beat three, the record "
            "updates: ownership flips, the handoff timestamp is logged, and "
            "the package is attached to the case. The queue in between is "
            "measured - handoff latency is the time from giver-release to "
            "receiver-claim, and it is the first number to attack when "
            "cycle times are too long. Team-to-team handoffs add translation: "
            "each team has its own vocabulary, so the package must be "
            "written in the receiver's terms. Shift handoffs add overlap: "
            "the outgoing shift briefs the incoming while both are present, "
            "so nothing lives only in one person's memory."
        ),
        "key_points": [
            "A handoff has four parts: giver, receiver, package, and acknowledgment - the acknowledgment is the part most teams skip and most need.",
            "Handoff latency - the gap between release and claim - is usually the largest component of cycle time and the first number to attack.",
            "Dropped handoffs happen when the giver assumes the receiver knows; the cure is ceremony proportionate to risk, always recorded.",
            "Team-to-team handoffs require translation into the receiver's vocabulary; shift handoffs require overlap so nothing lives in one memory.",
            "The handoff record carries ownership from, to, package contents, and acknowledgment timestamp - the gap is then visible, not mysterious.",
        ],
        "requirements": [
            "A handoff package template: case state, work done, work remaining, gotchas, deadline.",
            "An explicit acknowledgment step where the receiver confirms readiness.",
            "Handoff records with from, to, package, and timestamps.",
            "Handoff latency measured per path between roles or teams.",
            "Ceremony scaled to risk: message, checklist, or sign-off.",
        ],
        "standards": [
            "Ownership is never ambiguous during a handoff - the giver owns until the receiver acknowledges, then the receiver owns.",
            "Critical handoffs use a written checklist signed by both parties before the transfer completes.",
            "Handoff latency targets are published per path and reviewed with the same seriousness as task durations.",
        ],
        "citations": [CIT_WESKE, CIT_ITIL, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: a handoff is a sealed covenant between "
            "bearers, and the Signature Operations Method performs it as a "
            "three-beat ritual - the package assembled, the receipt "
            "witnessed, the record sealed. No charge is ever dropped in the "
            "gap, for the gap itself is measured and the measurement is "
            "testimony."
        ),
    },
    {
        "key": "audit_trail",
        "name": "The Audit Trail of Status Changes",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "An audit trail is the case's uneditable biography: who changed "
            "what, from what to what, when, and why. It is the difference "
            "between a story about the case and evidence of the case. Every "
            "status change, ownership transfer, deadline move, and field edit "
            "appends a record carrying the actor, the timestamp, the old "
            "value, the new value, and the reason. Append-only is the "
            "sacred property: new records are added, old ones are never "
            "altered or deleted, so the past cannot be rewritten to flatter "
            "the present. A good trail answers the hard questions without "
            "detective work - how long did approval really take, who moved "
            "the deadline, when did the customer last respond. It is also "
            "the raw material of every advanced record in this database: "
            "process mining, cycle-time analytics, and breach prediction all "
            "eat audit trails."
        ),
        "how_it_works": (
            "An audit trail works by event capture at the moment of change. "
            "When a status flips, the system writes an event record before "
            "the new state is visible: a sequence number that increments by "
            "one with no gaps, a timestamp from a trusted clock, the actor's "
            "identity, the field changed, the before value, the after value, "
            "and a reason code. The sequence numbers make tampering "
            "detectable - a missing number means a missing event - and "
            "timestamps in non-decreasing order make reordering detectable. "
            "Reading the trail reconstructs the case at any past moment: "
            "replay the events up to a timestamp and you see exactly what "
            "everyone saw then. Retention policy keeps the trail for the "
            "required span - contractual, legal, or analytical - and access "
            "control keeps the trail readable by auditors while the "
            "append-only rule keeps it honest for everyone."
        ),
        "key_points": [
            "An audit trail is the case's uneditable biography: actor, timestamp, old value, new value, reason - on every change.",
            "Append-only is the sacred property: new events are added, old ones never altered, so the past cannot be rewritten.",
            "Sequence numbers with no gaps and non-decreasing timestamps make deletion and reordering detectable.",
            "Replaying the trail reconstructs the case at any past moment - what everyone saw then, exactly.",
            "The trail is the raw material of process mining, cycle-time analytics, and breach prediction - record it well and the advanced records become possible.",
        ],
        "requirements": [
            "Event capture on every status, ownership, deadline, and field change.",
            "Append-only storage with no edit or delete path for trail records.",
            "Gap-free sequence numbers and trusted timestamps on every event.",
            "Actor identity and reason recorded on every event.",
            "A retention policy naming how long trails are kept and who may read them.",
        ],
        "standards": [
            "Trail events carry the five fields - actor, timestamp, field, before, after - plus a reason; an event missing any of them is a defect.",
            "Timestamps come from a trusted, synchronized clock, not from client devices.",
            "Retention follows the strictest applicable requirement - contract, regulation, or analytical need.",
        ],
        "citations": [CIT_MINING, CIT_DUMAS, CIT_ITIL],
        "sig_lens": (
            "The Signature read: the audit trail is the unbroken chain of "
            "testimony, and the Signature Operations Method guards it as "
            "sacred - each event a witness statement, each sequence number "
            "a link no hand may remove. What is written is written; the "
            "past stands unaltered, and the chain testifies for the case "
            "long after the bearers have moved on."
        ),
    },
    {
        "key": "outcomes_outputs",
        "name": "Outcomes Versus Outputs",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Outputs are what the workflow produced; outcomes are what "
            "changed in the world because of it. A support workflow's output "
            "is a closed ticket; its outcome is a customer whose problem "
            "stayed solved. A hiring workflow's output is a signed offer; "
            "its outcome is a productive employee a year later. Teams that "
            "manage outputs hit their numbers while missing their purpose; "
            "teams that manage outcomes ask the harder question - did the "
            "work matter. The distinction shapes measurement: outputs are "
            "counted at completion, outcomes are measured after a lag, often "
            "by a different instrument - a survey, a retention number, a "
            "reopen rate. Every workflow should name both: the outputs it "
            "promises this week and the outcomes it serves this quarter. "
            "When the two conflict - closing tickets fast versus solving "
            "problems - the outcome wins, and the workflow gets redesigned "
            "until the outputs serve it."
        ),
        "how_it_works": (
            "Outcomes work by lagging indicators tied back to the case. At "
            "design time the team names the outcome and its measure: "
            "thirty-day reopen rate for support, first-year retention for "
            "hiring, on-time payment rate for invoicing. The workflow "
            "records its outputs at completion as usual, and a separate "
            "measurement - taken after the lag, by an instrument the "
            "workflow does not control - scores the outcome. Outcome "
            "attainment is the ratio of cases achieving the outcome to cases "
            "that aimed at it. When attainment drops, the team traces "
            "backward through the audit trail to find which outputs "
            "correlated with failed outcomes - fast closures with high "
            "reopens point at rushed diagnosis, not lazy agents. The "
            "feedback loop closes when the process is redesigned: add the "
            "verification step, change the incentive, and watch the lagging "
            "indicator move. Outputs are the workflow's promises; outcomes "
            "are its report card."
        ),
        "key_points": [
            "Outputs are what the workflow produced; outcomes are what changed in the world - manage both, but let the outcome win conflicts.",
            "Outputs are counted at completion; outcomes are measured after a lag, by an instrument the workflow does not control.",
            "Outcome attainment is cases achieving the outcome over cases that aimed at it - the workflow's report card.",
            "When attainment drops, trace backward through the trail to find which outputs correlate with failed outcomes.",
            "Name the outcome and its measure at design time, or the workflow will optimize whatever is easiest to count.",
        ],
        "requirements": [
            "A named outcome and its lagging measure for every workflow.",
            "An outcome instrument independent of the workflow's own reporting.",
            "Output records at completion and outcome records after the lag.",
            "Outcome attainment tracked per period and per cohort.",
            "A redesign loop that changes the process when attainment drops.",
        ],
        "standards": [
            "Outcome measures are defined before the workflow runs - choosing the measure after seeing the data is a defect.",
            "Lag periods are fixed per workflow so cohorts are comparable.",
            "Incentives reward outcomes, or at minimum do not reward outputs that destroy outcomes.",
        ],
        "citations": [CIT_DUMAS, CIT_ITIL, CIT_PMBOK],
        "sig_lens": (
            "The Signature read: the output is the delivered parcel; the "
            "outcome is the changed world. The Signature Operations Method "
            "swears its oath to the outcome, not the parcel - the bearer is "
            "judged when the lag has passed and the independent witness "
            "has spoken, and the road is rebuilt until its parcels serve "
            "its promises."
        ),
    },
    {
        "key": "day_in_life",
        "name": "A Day in the Life of a Simple Workflow",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "The simplest real workflow is the expense report: an employee "
            "submits receipts, a manager approves, finance pays, and the "
            "case closes. One trigger, three tasks, two handoffs, one "
            "decision - and it still teaches every foundation at once. The "
            "trigger is the submission with its receipt package; ownership "
            "starts with the employee, passes to the manager, then to "
            "finance; statuses move submitted to approved to paid to "
            "closed; the decision at approval has two branches, approve and "
            "return for correction, each with its own path. The audit trail "
            "records every station; the deadlines are the pay-cycle cutoff "
            "and the reimbursement promise; the outcome is an employee paid "
            "correctly and on time, not merely a report processed. Walk one "
            "expense report through the whole ladder in your head and the "
            "abstract records become concrete: this is what a task, a case, "
            "a handoff, and a status feel like in practice."
        ),
        "how_it_works": (
            "The expense workflow works by a short, strict path. Submission "
            "creates the case with the receipt package and sets status to "
            "submitted; the owner is the employee until the submit button "
            "moves it, then the manager owns it. The manager's task carries "
            "the decision: approve moves the case to approved and hands "
            "ownership to finance, while return for correction moves it "
            "back to the employee with a reason, restarting the loop. "
            "Finance's task is pay: the payment is issued, the status moves "
            "to paid, and after the pay-cycle cutoff the case closes. Every "
            "station change appends its audit event; every handoff follows "
            "the three-beat ritual of package, acknowledgment, and record. "
            "The pay-cycle cutoff is the deadline with teeth - miss it and "
            "the reimbursement waits a full cycle, so the internal target "
            "is set days earlier. The whole run, done cleanly, takes five "
            "task-steps and two handoffs; done with a correction loop, it "
            "takes seven - and the trail shows exactly where the extra "
            "steps went."
        ),
        "key_points": [
            "One trigger, three tasks, two handoffs, one decision: the expense report teaches every foundation in a single walk-through.",
            "The approval decision has two branches - approve and return for correction - and the return branch restarts the loop with a recorded reason.",
            "Ownership passes employee to manager to finance, each transfer following the handoff ritual with its record.",
            "The pay-cycle cutoff is a deadline with teeth, so the internal target is set days earlier than the promise.",
            "A clean run takes five steps and two handoffs; a correction loop adds two more - and the trail shows exactly where.",
        ],
        "requirements": [
            "A submission package template: receipts, amounts, categories, cost center.",
            "An approval gate with approve and return branches, each with its path.",
            "Ownership transfer records at each handoff.",
            "A pay-cycle cutoff published as the drop-dead date with an earlier internal target.",
            "A correction loop that returns to the employee with a stated reason.",
        ],
        "standards": [
            "Approval decisions are recorded with the decider, the timestamp, and the reason - a silent approval is a defect.",
            "Returned reports carry the correction reason so the employee fixes the right thing the first time.",
            "Payment records tie the case to the financial transaction identifier for reconciliation.",
        ],
        "citations": [CIT_WESKE, CIT_DUMAS, CIT_ITIL],
        "sig_lens": (
            "The Signature read: follow one traveler - the expense report - "
            "down the sworn road and every foundation becomes flesh. The "
            "Signature Operations Method teaches the whole ladder through "
            "this single journey first: the call, the bearers, the "
            "witnessed fork, the sealed covenants, and the fulfilled "
            "charge at the pay-cycle gate."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "state_machines",
        "name": "State Machines and Transition Rules",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A state machine is the status lifecycle made rigorous: a set "
            "of states, a set of events, and a transition function that "
            "says, for each state and each event, which state comes next. "
            "Where the foundation record taught the lifecycle as a "
            "vocabulary, this record teaches it as mathematics. A finite "
            "state machine has no memory beyond its current state - the "
            "next move depends only on where the case is and what just "
            "happened, which is exactly how a well-run case behaves. The "
            "transition table becomes executable: feed it the current "
            "status and the incoming event and it returns the next status "
            "or rejects the event as illegal. Guards add conditions - the "
            "transition fires only if the case data satisfies a predicate, "
            "like approval granted or amount below threshold. State machines "
            "are the formal ground under BPMN, workflow engines, and every "
            "enforced lifecycle in this database."
        ),
        "how_it_works": (
            "A state machine works by table lookup with memory of one. The "
            "machine holds the current state; an event arrives - task "
            "completed, approval granted, timeout fired; the machine looks "
            "up the pair (state, event) in the transition table. If the "
            "table has an entry, any guard on that entry is evaluated "
            "against the case data; if the guard passes, the machine moves "
            "to the target state, runs any entry actions (notify, start "
            "timer), and appends the transition to the audit trail. If the "
            "table has no entry, the event is rejected and the case stays "
            "put - the rejection itself is logged, because attempted "
            "illegal moves are diagnostic gold. Reachability analysis walks "
            "the table from the start state and lists every state the case "
            "can ever reach; any state not on the list is dead design. "
            "Determinism - one target per (state, event) pair - keeps the "
            "machine predictable; where two targets are wanted, the "
            "decision belongs to a gateway, not the machine."
        ),
        "key_points": [
            "A state machine is states plus events plus a transition function: given current state and event, the next state is determined.",
            "The machine remembers only its current state; guards add case-data conditions that a transition must satisfy to fire.",
            "Illegal events are rejected and logged - attempted illegal moves are diagnostic gold about process confusion.",
            "Reachability analysis from the start state finds dead states that no case can ever occupy; dead states are dead design.",
            "Determinism keeps the machine predictable: one target per state-event pair, with branching decisions pushed to gateways.",
        ],
        "requirements": [
            "An explicit state list with a designated start state and terminal states.",
            "A transition table covering every legal state-event pair.",
            "Guards written as testable predicates on case data.",
            "Rejection logging for events with no table entry.",
            "A reachability check proving every state is reachable and every terminal state is reachable from everywhere intended.",
        ],
        "standards": [
            "Transition tables are versioned with the process; a case in flight keeps the table version it started with.",
            "Guards are pure predicates on case data - no side effects, no hidden state.",
            "Entry and exit actions are idempotent so a retried transition does not double-notify or double-charge.",
        ],
        "citations": [CIT_WESKE, CIT_DUMAS, CIT_WF_PATTERNS],
        "sig_lens": (
            "The Signature read: the state machine is the law of the road "
            "written as mathematics. The Signature Operations Method holds "
            "that a station knows only itself and the law - the traveler "
            "arrives, the law is consulted, the next station is named, and "
            "the witness writes it down. No station may be skipped, none "
            "may be invented mid-journey."
        ),
    },
    {
        "key": "basic_patterns",
        "name": "Basic Workflow Patterns: Sequence, Parallel, and Choice",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "The workflow patterns research of van der Aalst and colleagues "
            "catalogued the recurring control-flow shapes that appear in "
            "every process language - and the five basic patterns are the "
            "atoms of routing. Sequence runs tasks one after another; the "
            "case cannot start task B until task A completes. Parallel "
            "split (AND-split) launches several branches at once; "
            "synchronization (AND-join) waits until all branches finish "
            "before continuing. Exclusive choice (XOR-split) picks exactly "
            "one branch based on case data; simple merge (XOR-join) "
            "continues when whichever branch was chosen finishes, without "
            "waiting for the others. These five shapes compose into every "
            "routing structure in this database: sequence gives order, "
            "parallel gives speed, choice gives adaptability, and the joins "
            "give the discipline of waiting for exactly the right things."
        ),
        "how_it_works": (
            "The basic patterns work as token routing rules. In sequence, "
            "the completion event of task A is the start event of task B - "
            "a single thread of control passes the baton. In a parallel "
            "split, one incoming thread produces one thread per branch; the "
            "branches run concurrently, and the synchronization join "
            "consumes all branch threads and emits one, which means the "
            "join fires only when the slowest branch finishes - the case "
            "moves at the speed of its slowest parallel branch. In an "
            "exclusive choice, a data condition selects exactly one "
            "outgoing branch; the simple merge downstream fires when its "
            "single incoming thread arrives, with no synchronization "
            "because only one thread can ever arrive. The timing arithmetic "
            "follows: sequence time is the sum of task times, parallel "
            "time is the maximum of branch times, and choice time is the "
            "probability-weighted expected time of the chosen branches. "
            "Mixing a parallel split with a simple merge is the classic "
            "error - the merge fires on the first branch and the rest of "
            "the case is lost."
        ),
        "key_points": [
            "Sequence orders tasks; parallel split launches branches; synchronization waits for all of them; exclusive choice picks one branch; simple merge continues on whichever arrives.",
            "A synchronization join fires only when the slowest branch finishes - parallel paths move at the speed of their slowest branch.",
            "Timing arithmetic: sequence is the sum of task times, parallel is the maximum of branch times, choice is the probability-weighted expected time.",
            "Pair splits with their matching joins: parallel split with synchronization, exclusive choice with simple merge - crossed pairs lose cases.",
            "These five patterns are the atoms of routing; every complex structure in this database composes them.",
        ],
        "requirements": [
            "Every split paired with its matching join type.",
            "Data conditions on every exclusive-choice branch, covering all cases.",
            "A default or error branch on every choice so no case falls through.",
            "Branch time estimates so parallel-path timing can be computed.",
            "A routing review that checks no parallel split feeds a simple merge.",
        ],
        "standards": [
            "Pattern usage follows the van der Aalst pattern catalog naming so designs are comparable across languages and tools.",
            "Exclusive-choice conditions are mutually exclusive and collectively exhaustive over the case data domain.",
            "Parallel branches declare their shared resources so contention can be analyzed before it is suffered.",
        ],
        "citations": [CIT_WF_PATTERNS, CIT_BPMN, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: these five shapes are the first letters of "
            "the road's alphabet. The Signature Operations Method writes "
            "every route with them - the single file, the fanned host, the "
            "gathered host, the chosen path, the rejoined path - and forbids "
            "the crossed pairing, for a road that gathers what it fanned "
            "loses travelers in the mismatch."
        ),
    },
    {
        "key": "four_dependencies",
        "name": "The Four Dependency Types",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Dependencies say which tasks must relate to which, and the "
            "project-management tradition names four kinds. "
            "Finish-to-start is the familiar one: B cannot start until A "
            "finishes - the foundation is poured before the walls rise. "
            "Start-to-start says B cannot start until A has started: the "
            "second crew begins once the first crew is underway. "
            "Finish-to-finish says B cannot finish until A finishes: testing "
            "cannot complete until development completes. Start-to-finish is "
            "the rare one: B cannot finish until A starts, used in shift "
            "handovers where the incoming shift must be underway before the "
            "outgoing shift stands down. Each dependency carries a lag - a "
            "mandatory gap - or a lead, a permitted overlap expressed as "
            "negative lag. Choosing the wrong dependency type is a quiet "
            "schedule killer: modeling a true start-to-start as "
            "finish-to-start invents waiting time that the real work never "
            "needed."
        ),
        "how_it_works": (
            "Dependencies work as constraints on start and finish times. "
            "Finish-to-start with lag L means start(B) >= finish(A) + L; "
            "with a lead it becomes start(B) >= finish(A) - lead, an "
            "overlap. Start-to-start means start(B) >= start(A) + lag; "
            "finish-to-finish means finish(B) >= finish(A) + lag; "
            "start-to-finish means finish(B) >= start(A) + lag. Scheduling "
            "software propagates these constraints in the forward pass: "
            "each task's earliest start is the maximum over its "
            "predecessors of the constraint each dependency imposes, and "
            "the earliest finish is the earliest start plus duration. The "
            "network of dependencies is also the map the critical-path "
            "record walks: the longest chain of dependency-constrained "
            "durations sets the minimum possible finish. Leads and lags are "
            "scheduled truthfully - a lag for concrete curing is chemistry, "
            "not padding, and it belongs in the dependency, not in a "
            "padded task estimate."
        ),
        "key_points": [
            "Four dependency types: finish-to-start, start-to-start, finish-to-finish, and the rare start-to-finish for shift-style handovers.",
            "Each dependency carries a lag (mandatory gap) or a lead (permitted overlap); lags are scheduled truthfully as real constraints.",
            "The constraints are inequalities: finish-to-start means start(B) >= finish(A) + lag, and each type has its own form.",
            "A task's earliest start is the maximum over its predecessors of what each dependency demands - the tightest constraint wins.",
            "Modeling the wrong type invents phantom waiting time; the most common error is forcing finish-to-start where start-to-start is true.",
        ],
        "requirements": [
            "A dependency type named on every task relationship, not just an arrow.",
            "Lags and leads recorded with their real-world reason - chemistry, handover, review.",
            "A forward-pass schedule showing earliest starts and finishes honoring all four types.",
            "A review of every finish-to-start asking whether start-to-start is the truer model.",
            "The dependency network kept acyclic - a cycle is a schedule that can never start.",
        ],
        "standards": [
            "Dependency types follow the PMBOK precedence-diagramming conventions: FS, SS, FF, SF with signed lag values.",
            "Lags are documented with their physical or procedural cause; unexplained lag is re-estimated.",
            "Dependency networks are checked for cycles before scheduling - a cyclic network is rejected, not scheduled.",
        ],
        "citations": [CIT_PMBOK, CIT_KELLEY, CIT_WESKE],
        "sig_lens": (
            "The Signature read: dependencies are the sworn order of "
            "stations, and the Signature Operations Method names each bond "
            "truly - the finisher before the beginner, the starters "
            "together, the finishers together, the watcher relieved only "
            "when the relief has begun. A false bond invents false waiting, "
            "and false waiting is time stolen from the charge."
        ),
    },
    {
        "key": "advanced_patterns",
        "name": "Advanced Control-Flow Patterns",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Beyond the five basic patterns, the workflow patterns catalog "
            "names the shapes that real processes keep needing. The "
            "synchronizing merge (OR-join) waits for all branches that were "
            "actually started and ignores the ones that were not - the "
            "correct join when an upstream choice activated only some "
            "parallel branches. The discriminator (N-out-of-M join) fires "
            "when the first N of M branches complete and ignores the rest - "
            "the pattern behind first-response-wins routing. The "
            "multi-choice (OR-split) activates any number of branches based "
            "on conditions, paired with the synchronizing merge downstream. "
            "Arbitrary cycles loop back with an exit condition; implicit "
            "termination ends the case when nothing remains to do. Deferred "
            "choice lets the environment decide - whichever event arrives "
            "first wins the branch. These patterns are where visual "
            "modeling earns its keep: each one is easy to draw wrong and "
            "expensive to debug in production."
        ),
        "how_it_works": (
            "Advanced patterns work by counting and watching. The "
            "synchronizing merge counts how many branches the upstream "
            "OR-split activated and waits for exactly that many completions "
            "- it must know the activation set, which is why it is the "
            "tricky join to implement. The discriminator watches M running "
            "branches and fires on the Nth completion; the remaining "
            "branches are cancelled or left to finish harmlessly depending "
            "on the design. Deferred choice places no condition at the "
            "split - instead it arms event listeners on each branch, and "
            "the first event to arrive claims the case while the other "
            "listeners stand down. Arbitrary cycles route the token back to "
            "an earlier point guarded by an exit condition evaluated each "
            "lap; the loop is bounded by a maximum iteration count so a "
            "broken condition cannot spin forever. Implicit termination "
            "simply ends the case when no tokens remain active - no explicit "
            "end event required. Each pattern's correctness hinges on its "
            "join matching its split, the compounded discipline from the "
            "basic patterns, extended."
        ),
        "key_points": [
            "The synchronizing merge waits for exactly the branches an upstream multi-choice activated - it must know the activation set.",
            "The discriminator fires on the Nth of M completions and stands down the rest - the first-response-wins pattern.",
            "Deferred choice arms event listeners and lets the first arriving event claim the case - the environment decides.",
            "Arbitrary cycles loop with an exit condition and a maximum iteration bound so a broken condition cannot spin forever.",
            "Implicit termination ends the case when no tokens remain - and every advanced split still demands its matching join.",
        ],
        "requirements": [
            "The activation set recorded wherever a multi-choice feeds a synchronizing merge.",
            "N and M declared on every discriminator with the policy for late finishers.",
            "Exit conditions plus iteration bounds on every cycle.",
            "Event listeners with timeouts on every deferred choice so the case cannot wait forever.",
            "Split-join pairing verified for every advanced construct.",
        ],
        "standards": [
            "Advanced pattern usage follows the van der Aalst catalog definitions so implementations can be checked against known semantics.",
            "Cycles always carry both an exit condition and a hard iteration cap - one without the other is a defect.",
            "Discriminator late-finisher policy - cancel, ignore, or record - is declared at design time.",
        ],
        "citations": [CIT_WF_PATTERNS, CIT_YAWL, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: these are the road's advanced letters - "
            "the gathering that counts only the travelers who set out, the "
            "race where the first arrival claims the charge, the fork where "
            "the world itself chooses. The Signature Operations Method "
            "writes them carefully, for an advanced letter miswritten "
            "loses travelers in country the basic alphabet never reached."
        ),
    },
    {
        "key": "bpmn_basics",
        "name": "BPMN 2.0 Notation Basics",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "BPMN 2.0 - Business Process Model and Notation, the OMG "
            "standard - is the shared drawing language of workflows: one "
            "notation that business people, engineers, and execution "
            "engines can all read. Its vocabulary is small. Events are "
            "circles: start events (thin border) begin the case, end "
            "events (thick border) finish it, intermediate events catch or "
            "throw signals mid-flow. Activities are rounded rectangles: "
            "tasks do the work, subprocesses contain whole workflows "
            "inside. Gateways are diamonds: exclusive (X) for choice, "
            "parallel (+) for splits and joins, inclusive (O) for "
            "multi-choice, event-based for deferred choice. Sequence flows "
            "are solid arrows carrying the case forward; message flows are "
            "dashed arrows crossing pool boundaries between participants; "
            "pools and lanes show who does what. Learning to read BPMN is "
            "learning to read the drawn path itself."
        ),
        "how_it_works": (
            "BPMN works by giving every routing idea a distinct shape so "
            "the diagram cannot lie by accident. A process starts at "
            "exactly one start event per path and ends at end events; "
            "tokens - the abstract case-markers - flow along sequence "
            "flows, executing tasks and passing through gateways. The "
            "parallel gateway with a plus splits one token into many and, "
            "used as a join, waits for all of them - the AND-split and "
            "AND-join of the patterns record. The exclusive gateway routes "
            "the token down the one branch whose condition holds. Pools "
            "represent participants - the customer, the company - and "
            "message flows between pools show the conversations: order "
            "sent, invoice returned. Lanes divide a pool by role or team. "
            "The discipline of the notation is its constraints: a start "
            "event has no incoming flows, an end event has no outgoing "
            "flows, and every gateway's split type matches the join that "
            "collects it. A diagram that obeys the shapes can be executed; "
            "a diagram that breaks them is a sketch, not a model."
        ),
        "key_points": [
            "BPMN 2.0 is the OMG standard drawing language: events are circles, activities are rounded rectangles, gateways are diamonds, flows are arrows.",
            "Tokens flow along sequence flows; the parallel gateway splits and joins them, the exclusive gateway routes one token down the true branch.",
            "Pools and lanes show participants and roles; dashed message flows cross pool boundaries for the conversations between parties.",
            "Notation discipline: start events have no incoming flows, end events have no outgoing flows, and splits match their joins.",
            "A diagram obeying the shapes can be executed by an engine; a diagram breaking them is a sketch, not a model.",
        ],
        "requirements": [
            "One start event per path and end events on every terminal path.",
            "Gateway types marked explicitly - exclusive, parallel, inclusive, event-based.",
            "Pools for each participant with message flows for cross-party conversations.",
            "Lanes dividing pools by role or team where ownership matters.",
            "A notation check: no incoming flows to starts, no outgoing from ends, matched split-join pairs.",
        ],
        "standards": [
            "Diagrams conform to OMG BPMN 2.0 element semantics, not just its shapes - the picture and the meaning travel together.",
            "Exclusive gateway branches carry conditions; exactly one must hold for any case state.",
            "Message flows never cross inside a single pool - intra-party flow is always sequence flow.",
        ],
        "citations": [CIT_BPMN, CIT_DUMAS, CIT_WESKE],
        "sig_lens": (
            "The Signature read: BPMN is the cartography of the sworn road, "
            "and the Signature Operations Method reads its maps as law - "
            "circles for the call and the completion, rounded stones for "
            "the labors, diamonds for the witnessed forks, solid roads for "
            "the journey and dashed roads for the messages between "
            "realms. A map that breaks its own shapes is a rumor, not a "
            "road."
        ),
    },
    {
        "key": "critical_path",
        "name": "Critical Path and Schedule Math",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The critical path is the longest chain of dependent tasks "
            "through the workflow, and its length is the shortest time the "
            "whole case can possibly take. Every other chain has float - "
            "slack time it can slip without delaying the case - but the "
            "critical chain has none: delay any task on it by a day and the "
            "case finishes a day late. The critical path method, developed "
            "by Kelley and Walker in the 1950s, computes this with two "
            "passes. The forward pass walks the dependency network from "
            "start to finish, setting each task's earliest start and "
            "finish. The backward pass walks from finish to start, setting "
            "each task's latest start and finish without moving the end "
            "date. Float is latest minus earliest. The tasks with zero "
            "float are the critical path - the tasks that deserve the "
            "best people, the closest watching, and the first help when "
            "trouble comes."
        ),
        "how_it_works": (
            "The critical path method works by constraint propagation. "
            "List every task with its duration and its dependencies. The "
            "forward pass: a task's earliest start is the maximum over its "
            "predecessors of their earliest finish plus any lag; its "
            "earliest finish is earliest start plus duration. The project's "
            "earliest finish is the maximum earliest finish over all tasks. "
            "The backward pass: a task's latest finish is the minimum over "
            "its successors of their latest start minus lag; its latest "
            "start is latest finish minus duration. Total float for a task "
            "is latest start minus earliest start - the days it can slip "
            "safely. Tasks with zero float form the critical path; its "
            "length is the minimum case duration. Free float - the slip "
            "that does not delay any successor - guides day-to-day "
            "replanning. When the plan changes, the passes re-run: the "
            "critical path is a property of the current network, not a "
            "permanent title, and crashing - spending to shorten - is only "
            "ever spent on critical tasks."
        ),
        "key_points": [
            "The critical path is the longest dependency chain; its length is the shortest possible case duration and its tasks have zero float.",
            "The forward pass computes earliest starts and finishes; the backward pass computes latest starts and finishes; float is latest minus earliest.",
            "Delay any critical task and the case slips by the same amount - critical tasks get the best people and the closest watch.",
            "Total float is safe slip; free float is slip that delays no successor - replan with free float first.",
            "The critical path is recomputed when the network changes; crashing (paid shortening) is only ever spent on critical tasks.",
        ],
        "requirements": [
            "Every task with a duration estimate and its dependency list.",
            "Forward and backward passes computed and recorded, not eyeballed.",
            "Float values published per task with the critical path highlighted.",
            "A recompute trigger: any duration or dependency change re-runs the passes.",
            "Crashing decisions restricted to critical tasks with cost-per-day-saved shown.",
        ],
        "standards": [
            "CPM calculations follow the Kelley and Walker method: earliest/latest times from the dependency network with lags honored.",
            "Duration estimates carry their basis - measured, estimated, or quoted - so the path's confidence is visible.",
            "The published critical path is dated; an undated path is assumed stale.",
        ],
        "citations": [CIT_KELLEY, CIT_PMBOK, CIT_WESKE],
        "sig_lens": (
            "The Signature read: the critical path is the road's spine - "
            "the longest chain of sworn stations, and the charge can never "
            "outrun its spine. The Signature Operations Method walks it "
            "twice, forward to find the earliest arrival and backward to "
            "find the latest safe departure, and guards the spineless "
            "stations - those with no float - with its best bearers."
        ),
    },
    {
        "key": "sla_fundamentals",
        "name": "SLA Fundamentals and Tracking",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A service level agreement is a promise with a number: 95 "
            "percent of priority-1 cases resolved within 4 hours, 99.9 "
            "percent uptime per month, first response within 30 minutes. "
            "The SLA names the metric, the target, the measurement window, "
            "and the consequence - credits, penalties, or escalation - when "
            "the target is missed. Tracking is the discipline of knowing, "
            "at every moment, whether the promise is being kept: each case "
            "carries its SLA clock, the clock pauses or runs according to "
            "published rules, and the dashboard shows compliance percentage "
            "and remaining error budget. The error budget is the allowed "
            "failure slice - with a 99.9 percent target, 0.1 percent of the "
            "window may fail - and spending it faster than time passes is "
            "the early warning. An SLA nobody tracks is a wish; an SLA "
            "tracked honestly is a management system."
        ),
        "how_it_works": (
            "SLA tracking works by clocks and arithmetic. Each case gets "
            "an SLA clock at creation, configured with the target duration "
            "for its priority; the clock runs during business hours or "
            "around the clock per the agreement, and pauses during defined "
            "waiting states - waiting on customer is the classic pause - "
            "because the provider should not burn budget on someone else's "
            "delay. At resolution the elapsed clock time is compared to the "
            "target: inside is a hit, outside is a miss. Compliance is hits "
            "over total cases in the window. The error budget is (1 - "
            "target) times the window: for 99.9 percent over a 30-day "
            "month, the budget is about 43 minutes of downtime or the "
            "equivalent miss allowance. Burn rate - budget consumed over "
            "budget elapsed - above 1.0 means the promise will break if "
            "nothing changes. Breach consequences trigger automatically: "
            "credits applied, escalations fired, reviews scheduled. The "
            "numbers are published to both sides, because a tracked promise "
            "is a trusted promise."
        ),
        "key_points": [
            "An SLA names the metric, the target, the window, and the consequence - a promise with a number and teeth.",
            "Each case carries an SLA clock that runs per published rules and pauses in defined waiting states like waiting-on-customer.",
            "Compliance is hits over total in the window; the error budget is the allowed failure slice of the window.",
            "Burn rate above 1.0 - budget consumed faster than time passing - is the early warning that the promise will break.",
            "Breach consequences trigger automatically: credits, escalations, reviews - and the numbers are published to both sides.",
        ],
        "requirements": [
            "Written SLA terms: metric, target, window, pause rules, and consequence.",
            "An SLA clock per case with pause and resume events recorded.",
            "A live dashboard of compliance percentage and remaining error budget.",
            "Automatic breach actions - credits, escalations, reviews.",
            "Published numbers visible to both provider and customer.",
        ],
        "standards": [
            "SLA clocks use the same trusted timestamps as the audit trail; clock disputes are settled from the trail.",
            "Pause rules are exhaustive and published - an unpublished pause is not a pause.",
            "Compliance is computed over fixed windows with the denominator (total cases) shown alongside the percentage.",
        ],
        "citations": [CIT_ITIL, CIT_DUMAS, CIT_PMBOK],
        "sig_lens": (
            "The Signature read: an SLA is an oath with a number, and the "
            "Signature Operations Method keeps its clocks as sacred "
            "instruments - each case carrying its own sworn hourglass, "
            "paused only by published law, its sand measured against the "
            "promise. When the sand runs faster than the oath allows, the "
            "alarm is the oath defending itself."
        ),
    },
    {
        "key": "case_lifecycle",
        "name": "Case Management Lifecycles",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Some work refuses to be a straight path. An insurance claim, "
            "a patient treatment, a fraud investigation - the next step "
            "depends on what the last step discovered, and no diagram "
            "drawn in advance survives first contact. Case management is "
            "the discipline for this knowledge work: instead of a fixed "
            "sequence, the case carries a plan of stages, milestones, and "
            "available tasks, and the knowledge worker chooses the path as "
            "the case unfolds. Adaptive case management, described by "
            "Swenson, goes further: the worker may add tasks, stages, and "
            "even goals mid-case. CMMN - Case Management Model and Notation, "
            "the OMG standard - gives this a drawing language: stages that "
            "contain tasks, milestones that mark achievements, sentries "
            "that trigger work when conditions hold, and discretionary "
            "items the worker may or may not invoke. The lifecycle of a "
            "case is then measured by stage completion and milestone "
            "achievement, not by position on a line."
        ),
        "how_it_works": (
            "Case management works by plan plus discretion. The case plan "
            "defines stages - intake, investigation, decision, closure - "
            "each containing required tasks that must complete, optional "
            "tasks the worker may invoke, and milestones like claim "
            "validated or treatment approved. Sentries watch case data: "
            "when the fraud score crosses its threshold, the sentry "
            "activates the deep-investigation stage automatically. The "
            "knowledge worker drives: completing tasks, pulling in "
            "discretionary items, and - under adaptive rules - adding new "
            "tasks the plan never named. Milestones flip when their entry "
            "criteria are satisfied, and the case closes when its "
            "mandatory stages complete and the closing milestone is "
            "achieved. The audit trail records not only what was done but "
            "what was chosen: which discretionary items were invoked and "
            "which were skipped is the knowledge the next case inherits. "
            "Measurement follows stages: stage cycle times, milestone hit "
            "rates, and discretionary-item usage reveal where the plan "
            "helps and where it hinders."
        ),
        "key_points": [
            "Case management suits knowledge work where the next step depends on what the last step discovered - the path is chosen as the case unfolds.",
            "CMMN models stages, milestones, sentries, and discretionary items: the drawing language for non-linear work.",
            "Sentries watch case data and activate stages automatically when conditions hold, like a fraud score crossing its threshold.",
            "The trail records choices, not just actions: which discretionary items were invoked or skipped is the knowledge the next case inherits.",
            "Measure stage completion and milestone achievement, not position on a line - the line does not exist here.",
        ],
        "requirements": [
            "A case plan with stages, required tasks, discretionary items, and milestones.",
            "Sentries with explicit trigger conditions on case data.",
            "Worker authority to invoke discretionary items and, under adaptive rules, add tasks.",
            "Milestone entry criteria written before the case runs.",
            "Choice-aware audit records capturing which optional work was taken or skipped.",
        ],
        "standards": [
            "Case plans follow CMMN semantics for stages, milestones, sentries, and discretionary items.",
            "Discretionary additions by workers are recorded as plan changes with author and reason, preserving the trail.",
            "Mandatory stages and the closing milestone are non-waivable - discretion applies to the path, not the destination.",
        ],
        "citations": [CIT_CMMN, CIT_SWENSON, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: some travelers walk country no map has "
            "drawn, and the Signature Operations Method equips them as "
            "sworn scouts - a plan of camps and beacons, sentries watching "
            "the data-horizon, and the scout's sworn discretion to blaze "
            "new trail. Every choice is witnessed, so the next scout "
            "inherits the knowledge of the last."
        ),
    },
    {
        "key": "escalation_paths",
        "name": "Escalation Paths and Tiers",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Escalation is the planned way up: when a case exceeds its "
            "owner's authority, skill, or time, it climbs to a tier with "
            "more of all three. Tiers are the rungs - front line, "
            "specialists, senior engineers, duty management, executives - "
            "each with defined powers: what it may approve, what it may "
            "spend, what it may decide. Escalation triggers are the rules "
            "that start the climb: severity thresholds, SLA breach "
            "warnings, customer requests, or stuck-time limits - a case "
            "unmoved for 24 hours climbs on its own. The path names the "
            "route: who is notified, in what order, through which channel, "
            "with what package of case context. Good escalation is boring "
            "by design: the right tier arrives with the full package before "
            "anyone has to ask. Bad escalation is a pager going off with "
            "no context at 3 a.m. - the path existed on paper and nowhere "
            "else."
        ),
        "how_it_works": (
            "Escalation works by triggers, tiers, and packages. A trigger "
            "fires - the SLA clock crosses its warning threshold, the "
            "severity is raised, the stuck-timer expires - and the case is "
            "reassigned to the next tier's queue with an escalation record "
            "naming the trigger, the from-tier, and the to-tier. Each tier "
            "has a response target tighter than the last: the front line "
            "answers in an hour, specialists in thirty minutes, duty "
            "management in fifteen. The escalation package travels with "
            "the case: summary, timeline, what was tried, customer impact, "
            "and the decision needed - so the higher tier starts working, "
            "not reading. Functional escalation moves the case across "
            "teams for skill; hierarchical escalation moves it up for "
            "authority; both are recorded the same way. De-escalation is "
            "the return trip: when the crisis passes, the case descends "
            "with a summary, because a tier that never gives cases back "
            "becomes the new front line. The escalation rate - escalated "
            "cases over total - measures whether the lower tiers are "
            "equipped or drowning."
        ),
        "key_points": [
            "Escalation is the planned way up: triggers start the climb, tiers are the rungs with defined powers, the path names the route and the package.",
            "Triggers include severity thresholds, SLA warnings, customer requests, and stuck-time limits - a case unmoved for 24 hours climbs on its own.",
            "The escalation package carries summary, timeline, attempts, impact, and the decision needed - the higher tier starts working, not reading.",
            "Functional escalation moves across teams for skill; hierarchical escalation moves up for authority; both are recorded the same way.",
            "De-escalation returns the case with a summary when the crisis passes; the escalation rate reveals whether lower tiers are equipped or drowning.",
        ],
        "requirements": [
            "Defined tiers with explicit powers: approve, spend, decide.",
            "Trigger rules with thresholds, timers, and customer-request paths.",
            "An escalation package template traveling with every escalated case.",
            "Response targets per tier, tighter at each rung.",
            "De-escalation records and a tracked escalation rate.",
        ],
        "standards": [
            "Escalation triggers are automatic where measurable - SLA warnings and stuck-timers fire without human initiation.",
            "Tier powers are written and current; an escalation to a tier that cannot decide is a loop, not a path.",
            "Every escalation and de-escalation is an audit-trail event with trigger, tiers, and timestamp.",
        ],
        "citations": [CIT_ITIL, CIT_DUMAS, CIT_WESKE],
        "sig_lens": (
            "The Signature read: escalation is the sworn ladder within the "
            "road, and the Signature Operations Method builds it before it "
            "is needed - each rung bearing greater authority, each climb "
            "triggered by law rather than panic, each traveler arriving "
            "upward with the full sealed package. The higher bearer begins "
            "working, never reading, and returns the charge when the storm "
            "passes."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "triage_prioritization",
        "name": "Triage and Prioritization",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Triage is the sorting of the incoming: every new case is "
            "read, scored, and routed before real work begins. "
            "Prioritization is the ranking that decides what gets the next "
            "available hour. The classic scoring multiplies impact by "
            "urgency: a payroll outage affecting everyone today outranks a "
            "cosmetic request affecting one person someday. Priority "
            "classes - P1 through P4, or critical to low - turn the score "
            "into action: each class carries its own SLA clock, its own "
            "escalation path, and its own queue discipline. Triage must be "
            "fast and cheap relative to the work: spending an hour sorting "
            "ten-minute tasks is process theater. The discipline that "
            "matters most is re-triage: priorities decay and sharpen as "
            "cases age and facts change, so the ranking is recomputed on a "
            "cadence, not set once at birth. A queue sorted by stale "
            "priorities is a queue working on yesterday's emergencies."
        ),
        "how_it_works": (
            "Triage works as a fast scoring pipeline. The intake record "
            "captures the scoring inputs: who is affected, how many, what "
            "is blocked, the deadline pressure, and the customer's own "
            "stated urgency. The score combines impact (breadth times "
            "depth of effect) with urgency (time pressure) - commonly as a "
            "product or a weighted sum - and maps to a priority class with "
            "hard edges so similar cases land in the same class. Routing "
            "follows the class: P1 cases go to the senior queue with the "
            "tightest SLA, P4 cases to the standard queue. Queue discipline "
            "is then priority-ordered within first-in-first-out: the "
            "highest class goes first, and within a class the oldest waits "
            "least. Re-triage runs on schedule and on event: aging raises "
            "priority by rule - a P3 unmoved for five days becomes a P2 - "
            "and new facts re-score immediately. The triage log records "
            "every score and re-score, so priority inflation - everything "
            "becoming P1 - is visible and correctable."
        ),
        "key_points": [
            "Triage sorts the incoming fast and cheap; prioritization ranks the queue to decide what gets the next available hour.",
            "Score as impact times urgency: breadth and depth of effect multiplied by time pressure, mapped to priority classes with hard edges.",
            "Each priority class carries its own SLA clock, escalation path, and queue discipline - the class is a contract, not a label.",
            "Re-triage runs on cadence and on event: aging raises priority by rule and new facts re-score immediately.",
            "The triage log makes priority inflation visible - when everything becomes P1, the scoring is broken, not the world.",
        ],
        "requirements": [
            "Scoring inputs captured at intake: affected parties, blocked work, deadline pressure.",
            "A scoring formula with class boundaries published to the team.",
            "Class-specific SLA clocks, escalation paths, and queue disciplines.",
            "Aging rules that raise priority as cases wait.",
            "A triage log recording every score and re-score with reason.",
        ],
        "standards": [
            "Priority classes are mutually exclusive with documented criteria - a case in two classes is a scoring defect.",
            "Re-triage cadence is fixed and published; ad-hoc reprioritization requires a recorded reason.",
            "Triage time is measured and kept small relative to task time - sorting must not cost more than the work.",
        ],
        "citations": [CIT_ITIL, CIT_PMBOK, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: triage is the gatekeeper's sworn "
            "judgment, weighing each traveler's burden and haste on the "
            "same scales. The Signature Operations Method scores impact "
            "against urgency in the open, binds each rank to its own oath "
            "of speed, and re-weighs on schedule - for a gate that judges "
            "once judges yesterday's travelers."
        ),
    },
    {
        "key": "queues_littles_law",
        "name": "Queues and Little's Law",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Every workflow with more work than workers has queues, and "
            "queues obey laws whether the team knows them or not. Little's "
            "law - proved by John Little in 1961 - is the deepest of them: "
            "over the long run, the average number of items in a stable "
            "system equals the average arrival rate multiplied by the "
            "average time an item spends in the system. In workflow terms: "
            "work in progress equals throughput times cycle time. The law "
            "is a lever with three handles: to cut cycle time without "
            "hiring, cut work in progress; to raise throughput without "
            "speeding up, the same. Utilization - arrival rate over service "
            "rate - warns of the cliff: as utilization nears 100 percent, "
            "waiting time explodes, so a team running at 95 percent is not "
            "efficient but one bad week from collapse. Queue discipline - "
            "first-in-first-out, priority-ordered, shortest-job-first - "
            "decides who waits, but no discipline repeals the law."
        ),
        "how_it_works": (
            "Little's law works as an accounting identity over any stable "
            "window: count the average cases present (WIP), measure the "
            "average completion rate (throughput), and their ratio is the "
            "average cycle time - L = lambda * W, so W = L / lambda. A team "
            "completing 20 cases a week with 60 in flight has a 3-week "
            "cycle time, no stopwatch required. The improvement loop runs "
            "the law backward: cap WIP at 30 and cycle time falls toward "
            "1.5 weeks at the same throughput. Utilization is lambda over "
            "mu, the service rate; queuing theory's cruel curve says mean "
            "wait grows as rho/(1 - rho), so at 80 percent utilization the "
            "wait factor is 4, at 90 percent it is 9, at 95 percent it is "
            "19 - the same team, the same work, wildly different waits. "
            "The practical instruments are WIP limits per stage, explicit "
            "queue disciplines, and a utilization target with headroom - "
            "typically 70 to 80 percent - so variation is absorbed instead "
            "of amplified. Measure WIP daily; it is the cheapest vital sign "
            "a workflow has."
        ),
        "key_points": [
            "Little's law: average work in progress equals arrival rate times average cycle time - the lever with three handles.",
            "To cut cycle time without hiring, cut work in progress; the law guarantees the arithmetic.",
            "Utilization near 100 percent makes waits explode - mean wait grows as rho/(1-rho), so 95 percent utilization is a cliff, not efficiency.",
            "WIP limits per stage are the practical instrument; measure WIP daily as the cheapest vital sign a workflow has.",
            "Queue discipline decides who waits - FIFO, priority-ordered, shortest-job-first - but no discipline repeals the law.",
        ],
        "requirements": [
            "WIP counted per stage on a daily cadence.",
            "Throughput measured as completions per fixed window.",
            "WIP limits set per stage and honored - new work waits when a stage is full.",
            "Utilization tracked against a headroom target of 70 to 80 percent.",
            "A named queue discipline per queue, published to the team.",
        ],
        "standards": [
            "Cycle time is measured from case creation to case closure, including all waiting - cherry-picked active-time-only measures are rejected.",
            "Little's law checks use stable windows where arrival and completion rates are approximately equal.",
            "WIP limits are numbers, not aspirations - a limit that is routinely exceeded is re-set or the inflow is throttled.",
        ],
        "citations": [CIT_LITTLE, CIT_DUMAS, CIT_WESKE],
        "sig_lens": (
            "The Signature read: the queue is the waiting hall of the "
            "road, and Little's law is its sworn arithmetic - the crowd in "
            "the hall equals the pace of arrivals times the length of the "
            "stay. The Signature Operations Method guards the hall's "
            "capacity as law: thin the crowd and every traveler hastens; "
            "cram the hall past its oath and the waiting itself becomes "
            "the journey."
        ),
    },
    {
        "key": "multi_instance",
        "name": "Multi-Instance and Loop Patterns",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Some tasks must be done not once but many times - once per "
            "order line, once per approver, once per site. Multi-instance "
            "patterns spawn the right number of copies of a task and then "
            "gather them. The parallel multi-instance launches all copies "
            "at once: ten approvals requested simultaneously, the case "
            "waiting for all ten. The sequential multi-instance runs them "
            "one after another: each site audit completes before the next "
            "begins. The catalog distinguishes static counts - known at "
            "design time, like three required signatures - from dynamic "
            "counts determined at runtime, like one task per order line. "
            "The completion condition decides when the gathering ends: all "
            "copies, a threshold (seven of ten approvals), or the first N. "
            "Loops are the simpler cousin: the same task repeated until a "
            "condition holds, like review-and-revise cycling until the "
            "document is accepted. The timing math is honest: parallel "
            "instances finish when the slowest finishes, sequential "
            "instances sum their durations."
        ),
        "how_it_works": (
            "Multi-instance works by fan-out, tracking, and fan-in. At "
            "fan-out the engine evaluates the instance expression - a "
            "fixed number, or a count derived from case data like the "
            "number of order lines - and creates one task copy per "
            "instance, each carrying its own owner, data slice, and "
            "status. The copies run per the mode: parallel copies all "
            "active at once, sequential copies chained so each starts when "
            "the previous completes. Each completion is recorded against "
            "the instance set, and the fan-in evaluates the completion "
            "condition after every finish: all complete, N complete, or a "
            "custom predicate like approvals minus rejections reaching "
            "quorum. When the condition holds, remaining copies are "
            "cancelled per policy and the case proceeds. Loops wrap a task "
            "or subprocess with a repeat condition checked after each "
            "iteration plus a maximum iteration bound. Instance-level "
            "audit records keep each copy's history distinct - the case "
            "trail shows which approver did what, not just that approvals "
            "happened."
        ),
        "key_points": [
            "Multi-instance spawns one task copy per item - per order line, per approver, per site - then gathers them by a completion condition.",
            "Parallel instances finish when the slowest finishes; sequential instances sum their durations - the timing math is honest.",
            "Static counts are known at design time; dynamic counts are computed from case data at runtime.",
            "Completion conditions include all, threshold (seven of ten), or first N - declared at design, evaluated after every finish.",
            "Loops repeat a task until a condition holds, always with a maximum iteration bound against runaway cycling.",
        ],
        "requirements": [
            "An instance expression: fixed count or a rule deriving the count from case data.",
            "A mode declaration: parallel or sequential.",
            "A completion condition evaluated after every instance finish.",
            "A late-instance policy: cancel, ignore, or record remaining copies.",
            "Per-instance audit records distinct from the case-level trail.",
        ],
        "standards": [
            "Dynamic instance counts are computed once at fan-out and frozen, so late-arriving data cannot silently add instances mid-flight.",
            "Sequential multi-instance chains carry the handoff ritual between copies - each copy's completion hands to the next.",
            "Loop bounds are mandatory: an unbounded loop is a defect regardless of how trustworthy the exit condition looks.",
        ],
        "citations": [CIT_WF_PATTERNS, CIT_BPMN, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: the multi-instance is the sworn host "
            "fanned out - one bearer per charge, all marching at once or "
            "filing one by one, gathered when the oath's number is met. "
            "The Signature Operations Method counts its host before "
            "marching, names the gathering number in advance, and writes "
            "each bearer's deeds separately, for a host's testimony is the "
            "sum of its bearers'."
        ),
    },
    {
        "key": "cancellation_compensation",
        "name": "Cancellation, Exceptions, and Compensation",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Real workflows meet the unexpected: the customer cancels "
            "mid-order, the payment gateway times out, the supplier's "
            "shipment never arrives. Cancellation stops a case or a region "
            "of it - the pattern catalog distinguishes cancelling a single "
            "task, a whole case, or a region while the rest continues. "
            "Exceptions are the events the happy path never named: "
            "timeouts, errors, withdrawals, each needing a handler that "
            "says what happens instead. Compensation is the undoing of "
            "completed work that must now be reversed: the reserved "
            "inventory is released, the charged card is refunded, the sent "
            "notification is corrected. Compensation is not rollback - a "
            "database can roll back a transaction, but the real world "
            "cannot un-ship a box; it can only ship a return label. Every "
            "task with real-world effects needs its compensating action "
            "named at design time, because inventing the undo during the "
            "crisis is how cancellations become disasters."
        ),
        "how_it_works": (
            "Cancellation and compensation work by declared handlers. Each "
            "task declares its cancellation behavior: interruptible "
            "immediately, interruptible at safe points, or "
            "non-interruptible - a task mid-payment may need to finish "
            "before its compensation runs. Boundary events on the task "
            "catch the exception signals: a timer boundary fires on "
            "timeout, an error boundary on failure, a cancel boundary on "
            "withdrawal, each routing to its handler path. Completed tasks "
            "with external effects register their compensating actions in "
            "reverse order - the last effect undone first, like unwinding a "
            "stack - and each compensation is itself a task with an owner "
            "and a record, because compensations can fail too. The saga "
            "pattern of the advanced tier is this idea at scale: long "
            "transactions as sequences of local steps each with a declared "
            "undo. The audit trail records the exception, the handler "
            "chosen, and every compensation run - a cancelled case with a "
            "complete compensation record is a success, not a failure."
        ),
        "key_points": [
            "Cancellation stops a task, a region, or a whole case; each task declares whether it is interruptible immediately, at safe points, or not at all.",
            "Boundary events catch timeouts, errors, and withdrawals and route each to its declared handler path.",
            "Compensation undoes real-world effects in reverse order - release the inventory, refund the charge, correct the notice - and each compensation is a tracked task.",
            "Compensation is not rollback: the world cannot un-ship a box, only ship a return label - the undo must be designed, not assumed.",
            "A cancelled case with a complete compensation record is a success; name every undo at design time, never during the crisis.",
        ],
        "requirements": [
            "Interruptibility declared on every task with external effects.",
            "Boundary handlers for timeout, error, and cancellation on risky tasks.",
            "Compensating actions named at design time for every completed effect.",
            "Reverse-order compensation execution with per-compensation records.",
            "Exception events in the audit trail naming the signal, the handler, and the outcome.",
        ],
        "standards": [
            "Compensating actions are idempotent - a retried refund must not refund twice.",
            "Non-interruptible tasks carry a maximum duration so a stuck task cannot block cancellation forever.",
            "Handler paths are tested with fault injection before the workflow goes live - an untested handler is a hope, not a plan.",
        ],
        "citations": [CIT_WF_PATTERNS, CIT_BPMN, CIT_SAGA],
        "sig_lens": (
            "The Signature read: even the sworn road meets the storm, and "
            "the Signature Operations Method prepares the un-swearing in "
            "advance - each labor declares how it may be halted, each "
            "completed deed names its atonement, and the atonements are "
            "performed last-deed-first like unstacking stones. A charge "
            "cancelled with every atonement witnessed is honorably closed."
        ),
    },
    {
        "key": "handoff_protocols",
        "name": "Handoff Protocols and Acceptance Criteria",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "The foundations record taught the handoff ritual; this record "
            "teaches its engineering. A handoff protocol is the written "
            "contract between giver and receiver: what the package "
            "contains, in what format, with what quality bar, and the "
            "acceptance criteria the receiver checks before acknowledging. "
            "Acceptance criteria are the measurable gates - all fields "
            "complete, attachments present, tests passing, customer "
            "confirmed - and the receiver may reject a handoff that fails "
            "them, sending it back with the defects named. Rejection is "
            "not rudeness; it is the protocol working: accepting a broken "
            "package just moves the failure downstream where it costs "
            "more. Protocols scale with risk: a shift handoff uses a "
            "briefing checklist, a vendor handoff uses a signed acceptance "
            "document, a production deployment uses a go/no-go gate. The "
            "acceptance rate - handoffs accepted first time over total - "
            "measures the health of the boundary between two parties."
        ),
        "how_it_works": (
            "A handoff protocol works as a contract with a gate. The "
            "protocol document names the package schema: the fields, the "
            "attachments, the formats, and which items are mandatory versus "
            "optional. The giver assembles the package against a checklist "
            "and submits it; the receiver runs the acceptance criteria - "
            "completeness checks, validity checks, and any verification "
            "steps like re-running a test or calling the customer - and "
            "either acknowledges, which transfers ownership and starts the "
            "receiver's clock, or rejects with the failed criteria listed. "
            "Rejection returns ownership to the giver with the defect list "
            "attached; the retry is a new handoff attempt, recorded "
            "separately, so chronic rejection is visible. The protocol "
            "also names the timeout: if the receiver neither accepts nor "
            "rejects within the window, the handoff escalates rather than "
            "silently stalling. Acceptance rate, rejection reasons, and "
            "handoff latency are reviewed at the boundary's own cadence - "
            "the two parties improving their contract together."
        ),
        "key_points": [
            "A handoff protocol is the written contract: package schema, formats, quality bar, and the acceptance criteria the receiver checks before acknowledging.",
            "The receiver may reject a failing handoff with defects named - rejection is the protocol working, not rudeness.",
            "Ownership transfers only on acknowledgment; rejection returns it to the giver with the defect list attached.",
            "Protocols scale with risk: briefing checklist, signed acceptance document, or go/no-go gate.",
            "Acceptance rate - accepted first time over total - plus rejection reasons and latency measure the boundary's health.",
        ],
        "requirements": [
            "A package schema with mandatory versus optional items marked.",
            "Written acceptance criteria, measurable and checkable.",
            "A rejection path returning the package with failed criteria named.",
            "An acknowledgment timeout that escalates instead of stalling.",
            "Boundary reviews on a cadence with both parties present.",
        ],
        "standards": [
            "Acceptance criteria are binary and evidence-based - a criterion that requires judgment without evidence is rewritten.",
            "Rejected handoffs keep their defect lists in the audit trail; patterns of repeat defects trigger protocol revision.",
            "Go/no-go gates record the decision, the deciders, and the evidence reviewed - a silent go is a defect.",
        ],
        "citations": [CIT_ITIL, CIT_WESKE, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: the covenant between bearers deserves its "
            "written law, and the Signature Operations Method seals it - "
            "the package's contents named, the measures of worthiness "
            "written, the right of refusal honored. A bearer who accepts a "
            "broken charge inherits its dishonor; the law of the handoff "
            "protects both giver and receiver."
        ),
    },
    {
        "key": "bpmn_execution",
        "name": "BPMN 2.0 Execution Semantics",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "BPMN 2.0 is not only a drawing language; the standard defines "
            "execution semantics - precise rules for what the diagram means "
            "when a machine runs it. The semantics are token-based: a token "
            "is the abstract marker of the case's presence at a point in "
            "the diagram, and the engine moves tokens according to the "
            "element rules. A start event creates a token; a task consumes "
            "its incoming token, performs, and emits onward; an end event "
            "consumes its token and may terminate the case. Gateways are "
            "token routers: the parallel gateway splits one token into one "
            "per outgoing flow and joins by waiting for all; the exclusive "
            "gateway routes one token down the true branch; the inclusive "
            "gateway activates the true branches and its join waits for "
            "exactly those. Understanding the token game is what separates "
            "diagrams that execute as drawn from diagrams that surprise "
            "their authors in production."
        ),
        "how_it_works": (
            "Token semantics work as a small abstract machine. Each "
            "sequence flow can hold tokens; each activity instance holds "
            "one while executing. The engine's scheduler repeatedly finds "
            "elements with tokens ready: a task with an arrived token "
            "starts, and on completion consumes that token and places one "
            "on each outgoing flow. Gateways implement the patterns "
            "record: the parallel join counts arrived tokens against "
            "incoming flows and fires when all have arrived; the inclusive "
            "join is the hard one - it must determine which upstream "
            "branches were activated and wait for exactly those, which is "
            "why inclusive joins are the classic source of engine bugs and "
            "why many teams avoid them. Intermediate timer events consume "
            "their token and re-emit when the duration elapses; message "
            "events wait for the correlated message. Termination end events "
            "consume all tokens in the case - the kill switch for runaway "
            "parallel branches. A sound model - no deadlocks, no tokens "
            "left behind - can be verified before deployment, and the "
            "advanced discipline is to verify, not hope."
        ),
        "key_points": [
            "BPMN 2.0 defines execution semantics, not just shapes: tokens flow through the diagram and each element type has precise token rules.",
            "Gateways are token routers - parallel splits and joins, exclusive routes, inclusive activates-and-waits-for-the-activated.",
            "The inclusive join is the hard one: it must know which branches were activated, making it the classic source of engine surprises.",
            "Intermediate events consume and re-emit tokens on time or message; termination end events consume all tokens as the kill switch.",
            "Soundness - no deadlocks, no stranded tokens - is verifiable before deployment; verify, do not hope.",
        ],
        "requirements": [
            "Token rules understood for every element type used in the model.",
            "Inclusive joins used only where the activation set is knowable, or avoided in favor of explicit structures.",
            "Termination end events placed where runaway branches must die.",
            "A soundness check - deadlock and stranded-token analysis - before deployment.",
            "Timer and message events with correlation keys defined, not assumed.",
        ],
        "standards": [
            "Execution follows the OMG BPMN 2.0 token semantics; engine-specific deviations are documented as deviations.",
            "Models pass soundness verification - every token reaches an end event, no path deadlocks - before production use.",
            "Message correlation keys are part of the model; a message event without a defined key is incomplete.",
        ],
        "citations": [CIT_BPMN, CIT_WESKE, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: beneath the map's shapes runs the law of "
            "the tokens - the invisible travelers whose rules the "
            "Signature Operations Method learns as scripture. Each diamond "
            "routes them by its sworn arithmetic, each circle births or "
            "lays them to rest, and the wise road-builder proves the map "
            "sound before any living case walks it."
        ),
    },
    {
        "key": "orchestration_choreography",
        "name": "Orchestration Versus Choreography",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "When work spans multiple parties or services, two "
            "architectures compete. Orchestration puts one conductor in "
            "charge: a central workflow engine calls each participant, "
            "collects results, and decides the next step - the conductor "
            "sees the whole score. Choreography gives every participant "
            "the dance steps: each party knows what to do when it receives "
            "its message, with no central controller - the dancers follow "
            "the shared protocol. Orchestration is easier to observe, "
            "change, and debug: the conductor's log shows the whole case. "
            "Choreography is more decoupled and resilient: no single "
            "controller to become the bottleneck or the single point of "
            "failure. The message math favors the conductor for small "
            "ensembles - N participants need about 2N messages through the "
            "hub versus N(N-1) peer messages - but the coupling math "
            "favors the dance at scale. Most real systems blend: "
            "orchestrated inside each party's walls, choreographed between "
            "them."
        ),
        "how_it_works": (
            "Orchestration works through a central state machine: the "
            "conductor holds the case state, invokes participant A, waits, "
            "records the result, invokes participant B with A's output, "
            "and so on - every decision made with full case context, every "
            "step in one audit trail. Choreography works through events: "
            "participant A completes its step and publishes an event; "
            "participants B and C, subscribed to that event type, react "
            "per the shared protocol; no party holds the global state, and "
            "the case's story is reconstructed by correlating the event "
            "stream. Failure handling differs sharply: the conductor can "
            "retry, reroute, or compensate from its central view, while the "
            "dance needs per-participant idempotency and dead-letter "
            "handling because no one sees everything. The choice hinges on "
            "ownership: one owner of the outcome favors orchestration; "
            "independent parties that must stay autonomous favor "
            "choreography. The blended pattern - a conductor per bounded "
            "context, events between contexts - is the architecture of most "
            "large operational systems."
        ),
        "key_points": [
            "Orchestration centralizes control in one conductor with the full case state; choreography distributes control as event-driven protocol among peers.",
            "Orchestration is easier to observe, change, and debug from the conductor's single log; choreography is more decoupled and resilient.",
            "Message math: orchestration needs about 2N hub messages for N participants; choreography needs up to N(N-1) peer messages.",
            "Failure handling differs: the conductor retries and compensates centrally; the dance needs per-participant idempotency and dead letters.",
            "One owner of the outcome favors orchestration; autonomous parties favor choreography; large systems usually blend both.",
        ],
        "requirements": [
            "An explicit architecture choice per cross-party workflow with the reasoning recorded.",
            "For orchestration: a conductor with the full case state and a single audit trail.",
            "For choreography: a published event protocol with correlation keys and per-participant idempotency.",
            "Dead-letter handling wherever events can go unprocessed.",
            "A reconstructed case view from the event stream for choreographed flows.",
        ],
        "standards": [
            "Choreographed protocols version their events; subscribers declare the versions they accept.",
            "Every participant is idempotent on redelivered messages - at-least-once delivery is assumed.",
            "The architecture decision is revisited when participant count or ownership changes materially.",
        ],
        "citations": [CIT_NEWMAN, CIT_WESKE, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: the conductor's road versus the dancers' "
            "road, and the Signature Operations Method chooses with open "
            "eyes - one sworn conductor where one oath governs the outcome, "
            "the shared dance where each realm keeps its sovereignty. The "
            "message-count is counted honestly, the failures are planned "
            "for, and the blended road takes the conductor within walls "
            "and the dance between them."
        ),
    },
    {
        "key": "sagas",
        "name": "Sagas and Long-Running Transactions",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "A database transaction locks, works, and commits in "
            "milliseconds; a business case - book the flight, reserve the "
            "hotel, charge the card, send the tickets - runs for minutes or "
            "days and cannot hold locks that long. The saga pattern, "
            "introduced by Garcia-Molina and Salem in 1987, is the answer: "
            "break the long transaction into local steps, each committing "
            "independently, each with a declared compensating action. If "
            "step three fails, the saga runs the compensations of steps "
            "two and one in reverse - cancel the hotel, refund the flight. "
            "Two coordinations exist: orchestrated sagas with a central "
            "coordinator issuing step commands, and choreographed sagas "
            "where each step's completion event triggers the next. The "
            "pattern accepts a hard truth: between steps the system is "
            "inconsistent by design, and the design must tolerate the "
            "in-between states - including the failure of a compensation "
            "itself, which then needs its own retry and escalation."
        ),
        "how_it_works": (
            "A saga works as a forward march with a prepared retreat. The "
            "coordinator - or the event chain - executes step one and "
            "commits it locally, recording the step's completion and its "
            "compensation in the saga log. Step two runs the same way, and "
            "so on. On a step failure, the saga switches to compensation "
            "mode: it walks the completed steps backward, running each "
            "compensation exactly as the cancellation record prescribes, "
            "each compensation idempotent and retried until it succeeds or "
            "escalates to human handling. The saga log is the source of "
            "truth that makes crash recovery possible: after a coordinator "
            "crash, replaying the log reveals which steps completed and "
            "which compensations ran, so the march or the retreat resumes "
            "correctly. Semantic locking guards the in-between states - "
            "the reserved seat is marked reserved, not available - so "
            "concurrent sagas do not double-book the same resource. The "
            "design rule is that every step's compensation is written and "
            "tested before the step ships, because a saga whose retreat is "
            "unplanned is just a distributed way to lose data."
        ),
        "key_points": [
            "Sagas break long transactions into local steps, each committed independently, each with a declared compensating action - the 1987 answer to transactions that outlive locks.",
            "On step failure the saga compensates backward, last completed step first, unwinding the march in reverse.",
            "Between steps the system is inconsistent by design; semantic locking (reserved, not available) protects shared resources meanwhile.",
            "The saga log makes crash recovery possible: replay reveals which steps completed and which compensations ran.",
            "Compensations are idempotent, retried to success or human escalation - and written and tested before the step ships.",
        ],
        "requirements": [
            "Local steps with independent commits and declared compensations.",
            "A saga log recording step completions and compensation runs.",
            "Reverse-order compensation with idempotent, retried actions.",
            "Semantic locking on resources touched mid-saga.",
            "Crash-recovery by log replay tested before production.",
        ],
        "standards": [
            "Every saga step ships with its compensation tested - an untested undo is not a saga but a hope.",
            "Compensation failure escalates to human handling with the full saga log attached; silent compensation failure is prohibited.",
            "Choreographed sagas carry correlation identifiers on every event so the case story reconstructs from the stream.",
        ],
        "citations": [CIT_SAGA, CIT_NEWMAN, CIT_WESKE],
        "sig_lens": (
            "The Signature read: the long campaign that no single oath can "
            "span, so the Signature Operations Method marches it as a saga "
            "- each day's ground sworn and held separately, each day's "
            "retreat planned before the advance. If the campaign breaks, "
            "the host withdraws in good order, last ground first, every "
            "atonement witnessed, until the field stands as though the "
            "march never began."
        ),
    },
    {
        "key": "deadlock_detection",
        "name": "Deadlock Detection in Dependency Graphs",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "A dependency cycle is a schedule that can never start: task A "
            "waits for task B, task B waits for task C, task C waits for "
            "task A, and the case waits forever. Deadlock detection is the "
            "discipline of finding these cycles before they freeze work - "
            "or, where cycles can form at runtime through resource waits, "
            "detecting them in the live wait-for graph and breaking them. "
            "The instrument is graph theory: tasks are nodes, waits-for "
            "relationships are directed edges, and a cycle in the graph is "
            "a deadlock. Depth-first search with three-color marking - "
            "unvisited, in-progress, done - finds cycles in time "
            "proportional to nodes plus edges, cheap enough to run on "
            "every schedule change. Prevention beats detection: keeping "
            "the dependency network acyclic by construction, ordering "
            "resource acquisition, and bounding waits with timeouts so a "
            "missing cycle still cannot wait forever."
        ),
        "how_it_works": (
            "Deadlock detection works by cycle search. Build the wait-for "
            "graph: a directed edge from task X to task Y when X cannot "
            "proceed until Y completes or releases a resource. Run "
            "depth-first search, coloring each node white (unvisited), "
            "gray (on the current path), or black (fully explored). "
            "Encountering a gray node during the search means the current "
            "path has looped back on itself - a cycle, and the nodes on "
            "the gray path are the deadlocked set. Static detection runs "
            "this on the dependency network at design and schedule-change "
            "time, rejecting cyclic networks before they execute. Dynamic "
            "detection runs it on the live wait-for graph - including "
            "resource waits the static plan never named - on a cadence or "
            "when a stuck-timer fires. Breaking a detected deadlock picks "
            "a victim by policy - lowest priority, youngest, cheapest to "
            "restart - preempts its waits, and records the intervention. "
            "Timeouts on every wait are the backstop: even an undetected "
            "cycle surfaces as a timeout rather than an eternity."
        ),
        "key_points": [
            "A dependency cycle is a schedule that can never start; in the wait-for graph, a directed cycle is a deadlock.",
            "Depth-first search with white-gray-black marking finds cycles in time proportional to nodes plus edges - cheap enough to run on every schedule change.",
            "Static detection rejects cyclic dependency networks at design time; dynamic detection watches the live wait-for graph including resource waits.",
            "Breaking a deadlock preempts a victim chosen by policy - lowest priority, youngest, or cheapest to restart - and records the intervention.",
            "Timeouts on every wait are the backstop: even an undetected cycle surfaces as a timeout, never an eternity.",
        ],
        "requirements": [
            "A wait-for graph constructible from the dependency network and live resource waits.",
            "Cycle detection run at design time and on every schedule change.",
            "Dynamic detection on the live graph on a cadence or on stuck-timer fire.",
            "A victim-selection policy for breaking detected deadlocks.",
            "Timeouts on all waits as the backstop against undetected cycles.",
        ],
        "standards": [
            "Cyclic static dependency networks are rejected, not scheduled - the cycle is fixed in the plan, not worked around at runtime.",
            "Deadlock interventions are audit-trail events naming the cycle members, the victim, and the policy applied.",
            "Resource acquisition follows a declared ordering where resources are contended, preventing the classic circular wait.",
        ],
        "citations": [CIT_PMBOK, CIT_KELLEY, CIT_WESKE],
        "sig_lens": (
            "The Signature read: the circle of waiting that can never "
            "begin, and the Signature Operations Method hunts it with the "
            "three-colored search - the unvisited, the journeyed, the "
            "completed - for a road that loops upon itself is no road. "
            "The cycle is broken by sworn policy, the released traveler "
            "recorded, and every wait carries its hourglass against the "
            "circles the hunt might miss."
        ),
    },
])

ENTRIES.extend([
    {
        "key": "sla_prediction",
        "name": "SLA Breach Prediction",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "SLA tracking knows when the promise broke; breach prediction "
            "knows it will break while there is still time to act. The "
            "instrument is burn-rate forecasting: compare budget consumed "
            "against budget elapsed, project the trajectory, and raise the "
            "alarm when the projection crosses the target before the "
            "window ends. A case that has burned 60 percent of its SLA "
            "clock with the hard work still ahead is a predicted breach, "
            "and the prediction triggers the same machinery as an "
            "escalation - more hands, narrowed scope, or a renegotiated "
            "promise. Prediction models range from simple linear "
            "extrapolation of elapsed-versus-remaining work to learned "
            "models trained on the audit trail: cases with this pattern of "
            "status dwell times breached 80 percent of the time. The "
            "discipline is calibration: predictions are scored against "
            "outcomes, the model is retuned, and the team learns which "
            "early signals actually precede breaches. A prediction nobody "
            "acts on is just anxiety with arithmetic."
        ),
        "how_it_works": (
            "Breach prediction works by projecting the case's trajectory "
            "against its clock. The simple forecaster computes burn rate - "
            "clock consumed over clock elapsed - and remaining work "
            "estimated from the task list; predicted finish is now plus "
            "remaining work at the observed pace, and if that lands past "
            "the SLA target, the case is flagged. The statistical "
            "forecaster does better: it mines the audit trail for the "
            "dwell-time distributions of each status, simulates the "
            "remaining path Monte Carlo style, and reports the breach "
            "probability - flagging cases above a threshold like 70 "
            "percent. The learned forecaster trains on historical cases: "
            "features like current status age, owner workload, priority, "
            "and day-of-week feed a classifier whose output is breach "
            "probability. Every prediction carries its confidence and its "
            "reasons - the top contributing factors - so the responder "
            "knows what to attack. The feedback loop scores predictions: "
            "precision (flagged cases that breached) and recall (breached "
            "cases that were flagged) are tracked, and the threshold and "
            "model are retuned until the alarms are worth their "
            "interruptions."
        ),
        "key_points": [
            "Breach prediction projects the case trajectory against its SLA clock while there is still time to act - tracking reports the past, prediction defends the future.",
            "The simple forecaster extrapolates burn rate and remaining work; the statistical forecaster simulates remaining dwell times; the learned forecaster classifies on trail features.",
            "Every prediction carries its confidence and its top contributing factors so responders know what to attack.",
            "Predictions trigger real machinery - more hands, narrowed scope, renegotiated promise - or they are anxiety with arithmetic.",
            "Calibration is the discipline: precision and recall of predictions are tracked and the model retuned until the alarms earn their interruptions.",
        ],
        "requirements": [
            "A trajectory forecaster - linear, statistical, or learned - running over open cases.",
            "Breach-probability thresholds that trigger escalation actions.",
            "Prediction explanations: confidence plus contributing factors.",
            "Action machinery wired to predictions: staffing, scope, renegotiation.",
            "Precision and recall tracking on predictions with retuning cadence.",
        ],
        "standards": [
            "Predictions are computed from the same audit-trail timestamps as tracking - no second, shadow clock.",
            "Thresholds are set from measured precision-recall tradeoffs, not from round numbers.",
            "Prediction features exclude protected attributes; the model predicts breach risk from work patterns, not from who the customer is.",
        ],
        "citations": [CIT_ITIL, CIT_MINING, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: the oath's hourglass can be read before "
            "it empties, and the Signature Operations Method reads it - "
            "the sand spent against the sand remaining, the road ahead "
            "weighed by the journeys of ten thousand travelers past. When "
            "the reading says the oath will break, the alarm is raised "
            "while hands can still save it, and every alarm names its "
            "reasons."
        ),
    },
    {
        "key": "hash_chained_audit",
        "name": "Hash-Chained Audit Trails",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Append-only storage says the past must not change; "
            "hash-chaining proves it did not. Each audit event carries the "
            "cryptographic hash of the previous event's record, forming a "
            "chain where every link testifies to all the links before it. "
            "Alter one historical event - change a timestamp, delete a "
            "status change - and its hash changes, breaking the chain at "
            "that point and every point after; verification recomputes the "
            "hashes and the break is found mechanically. This is the same "
            "principle that secures blockchains and version-control "
            "histories, applied to the case biography. The chain does not "
            "prevent tampering by someone with write access to the store - "
            "it makes tampering detectable, which is the stronger property "
            "in practice: a trail whose integrity can be verified on "
            "demand is evidence, while a trail that merely promises "
            "append-only is an assertion. Periodic anchoring - publishing "
            "the latest chain hash to an independent store - extends the "
            "guarantee against even the store's own administrator."
        ),
        "how_it_works": (
            "Hash-chaining works by binding each event to its predecessor. "
            "When event N is appended, the writer computes H(N) = "
            "hash(serialized event N concatenated with H(N-1)), using a "
            "collision-resistant hash like SHA-256, and stores H(N) in the "
            "event record. The genesis event uses a fixed initialization "
            "value. Verification walks the chain from genesis: recompute "
            "each hash from the stored event data and the previous hash, "
            "and compare with the stored value - the first mismatch marks "
            "the tamper point, and everything after it is suspect. Because "
            "each hash covers all prior events transitively, verifying the "
            "latest hash verifies the whole history. Anchoring publishes "
            "periodic chain heads - daily, or every thousand events - to "
            "an independent system: an auditor comparing the anchored head "
            "with the recomputed head detects any rewrite of history, even "
            "by a privileged insider. The cost is one hash per event and "
            "one verification pass per audit - trivial against the value "
            "of provable integrity."
        ),
        "key_points": [
            "Each audit event carries the hash of the previous event's record, so every link testifies to all links before it - altering history breaks the chain mechanically.",
            "Verification recomputes the hashes from genesis; the first mismatch marks the tamper point and everything after it is suspect.",
            "Hash-chaining makes tampering detectable, which is stronger in practice than merely promising append-only.",
            "Periodic anchoring publishes chain heads to an independent store, extending the guarantee even against the store's own administrator.",
            "The cost is one SHA-256 per event and one verification pass per audit - trivial against provable integrity.",
        ],
        "requirements": [
            "A collision-resistant hash (SHA-256 or stronger) computed over each event plus the previous hash.",
            "The previous hash stored in every event record, genesis anchored to a fixed value.",
            "A verification routine that recomputes the chain from genesis on demand.",
            "Periodic anchoring of chain heads to an independent store.",
            "Tamper-detection alerts wired to verification failures.",
        ],
        "standards": [
            "Hash inputs use a canonical serialization - field order and encoding fixed - so verification reproduces the writer's hash exactly.",
            "Anchoring cadence is published and the anchor store is outside the trail writer's administrative control.",
            "Verification failures are security events, investigated before the trail is trusted again.",
        ],
        "citations": [CIT_MINING, CIT_ITIL, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: the chain of testimony is sealed link by "
            "link, each witness statement bearing the seal of the last, "
            "and the Signature Operations Method treats the seal as sacred "
            "arithmetic - alter one word of the past and every seal after "
            "it cries out. The chain's head is published abroad, so even "
            "the keeper of the archive cannot rewrite what the witnesses "
            "swore."
        ),
    },
    {
        "key": "cycle_time_analytics",
        "name": "Cycle Time and Flow Analytics",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Cycle time - birth to closure of a case - is the master vital "
            "sign of a workflow, and flow analytics is the practice of "
            "reading it well. Averages lie: one catastrophic case drags "
            "the mean while the typical case is fine, so the discipline "
            "reports percentiles - p50, the median case; p90 and p95, the "
            "tail the promises must survive. The cumulative flow diagram "
            "stacks cases by status over time: parallel bands mean smooth "
            "flow, a widening band means a growing queue, a band that "
            "never narrows is a bottleneck wearing a disguise. Aging "
            "charts show how long currently-open cases have waited, "
            "bucketed by age, exposing the forgotten. Throughput trends "
            "show completions per window against arrivals - when arrivals "
            "outrun completions for weeks, the backlog is not a blip but a "
            "structural deficit. Together these instruments turn the audit "
            "trail from a record of the past into a dashboard for the "
            "present."
        ),
        "how_it_works": (
            "Flow analytics works by aggregating the trail's timestamps. "
            "Cycle time per case is closure timestamp minus creation "
            "timestamp; the distribution over a window yields percentiles "
            "by sorting - p50 is the middle value, p90 the value exceeded "
            "by only ten percent. Status dwell times come from consecutive "
            "status-change events: entered at T1, left at T2, dwell is "
            "T2 minus T1. The cumulative flow diagram samples, per day, "
            "how many cases sit in each status and stacks them; the slope "
            "of the top edge is throughput, the vertical distance between "
            "the arrived and departed edges is WIP, and by Little's law "
            "their ratio is cycle time - three views of one truth. The "
            "aging chart buckets open cases by current age: 0-7 days, 8-14, "
            "15-30, over 30. Control limits on the p50 and p90 - set from "
            "history - fire when the process drifts: a p90 crossing its "
            "upper limit is the process telling the team it has changed "
            "before any customer complains."
        ),
        "key_points": [
            "Report percentiles, not averages: p50 for the typical case, p90 and p95 for the tail the promises must survive.",
            "The cumulative flow diagram stacks cases by status over time; a widening band is a growing queue, parallel bands are smooth flow.",
            "Aging charts bucket open cases by current wait, exposing the forgotten; throughput-versus-arrivals reveals structural backlog deficits.",
            "Dwell times come from consecutive status-change events; the CFD's edges encode throughput, WIP, and - by Little's law - cycle time.",
            "Control limits on p50 and p90 fire when the process drifts, letting the numbers complain before the customers do.",
        ],
        "requirements": [
            "Cycle-time percentiles (p50, p90, p95) computed per fixed window.",
            "A cumulative flow diagram refreshed at least daily.",
            "An aging chart of open cases by current wait bucket.",
            "Throughput versus arrival trends over the same windows.",
            "Control limits on key percentiles with drift alerts.",
        ],
        "standards": [
            "Cycle time is measured end to end, creation to closure, including all waiting - partial measures are labeled partial.",
            "Percentile windows are fixed and published so periods compare honestly.",
            "Drill-down from any aggregate point reaches the underlying cases - an aggregate that cannot be unpacked is decoration.",
        ],
        "citations": [CIT_MINING, CIT_DUMAS, CIT_LITTLE],
        "sig_lens": (
            "The Signature read: the road's pulse is taken in percentiles, "
            "not averages, and the Signature Operations Method reads the "
            "flow as a physician reads a patient - the stacked bands of "
            "the journey, the aging of those still traveling, the pace of "
            "arrivals against departures. When the pulse drifts, the "
            "numbers speak before any traveler cries out."
        ),
    },
    {
        "key": "versioning",
        "name": "Versioning Running Workflow Instances",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Processes change while cases are in flight: the approval step "
            "gains a new check, the SLA tightens, a task is split in two. "
            "Versioning is the discipline of changing the road while "
            "travelers walk it. The naive options both fail: freezing the "
            "old definition forever means improvements never reach live "
            "cases, while rewriting the definition under running cases "
            "corrupts their state. The working strategies are three. "
            "Version coexistence runs old cases on the old definition and "
            "new cases on the new - simple, but the old version lives until "
            "its last case closes. Instance migration moves running cases "
            "to the new definition, which requires a mapping for every "
            "in-flight state - safe only when the change is compatible. "
            "Change regions mark parts of the new definition where running "
            "cases may cross over and parts where they may not. The "
            "compatibility test decides: additive changes (new optional "
            "task, loosened guard) migrate safely; breaking changes "
            "(removed task, reordered states) do not."
        ),
        "how_it_works": (
            "Versioning works by classifying the change and choosing the "
            "strategy per case. Each process definition carries a version; "
            "each case records the version it started with. When version N+1 "
            "deploys, the migrator evaluates every in-flight case: it maps "
            "the case's current state in version N to the corresponding "
            "state in version N+1 using the declared state mapping. If the "
            "mapping covers the state and the change classification is "
            "additive or the state is unaffected, the case migrates - its "
            "version pointer updates and its next step follows the new "
            "definition, with the migration itself an audit-trail event. "
            "If the state has no mapping or the change is breaking for "
            "that state, the case stays on version N under coexistence. "
            "The version registry tracks which versions are live, which "
            "are deprecated (no new cases), and which are retired (no cases "
            "at all). Rollback is the reverse migration, supported only "
            "where the state mapping is bidirectional - another reason to "
            "keep changes additive. The dashboard shows cases per version "
            "so a deprecated version with a long tail of ancient cases is "
            "visible, not forgotten."
        ),
        "key_points": [
            "Three strategies: version coexistence (old cases finish on the old definition), instance migration (running cases move), and change regions (cross over only where safe).",
            "The compatibility test decides: additive changes migrate safely; breaking changes keep their cases on the old version.",
            "Migration maps each in-flight state to the new definition and records the move as an audit-trail event.",
            "The version registry tracks live, deprecated, and retired versions; rollback needs a bidirectional state mapping.",
            "Cases per version are dashboarded so a deprecated version's long tail of ancient cases stays visible.",
        ],
        "requirements": [
            "Version numbers on every process definition and a version pointer on every case.",
            "A change classification - additive or breaking - for every new version.",
            "A state mapping from old to new for migratable states.",
            "Migration recorded as an audit-trail event per case.",
            "A version registry with live, deprecated, and retired states and a cases-per-version view.",
        ],
        "standards": [
            "Breaking changes never migrate in-flight cases silently - affected cases stay on their version by rule.",
            "State mappings are reviewed like code: an unmapped state is an explicit decision, not an oversight.",
            "Deprecated versions carry a retirement plan with a date; a version without one is not deprecated, it is abandoned.",
        ],
        "citations": [CIT_WESKE, CIT_DUMAS, CIT_BPMN],
        "sig_lens": (
            "The Signature read: the road is rebuilt while travelers walk "
            "it, and the Signature Operations Method rebuilds lawfully - "
            "each road bearing its version, each traveler marked with the "
            "road of their setting-out, each crossing to the new road "
            "mapped station by station and witnessed. Where the new road "
            "breaks the old stations, the old travelers finish their "
            "journey on the road they swore to."
        ),
    },
    {
        "key": "dynamic_escalation",
        "name": "Dynamic Escalation Routing",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Static escalation paths name a fixed ladder; dynamic "
            "escalation routing chooses the rung at the moment of need. "
            "The insight is that the best tier for a case depends on live "
            "conditions: the specialist queue with twelve waiting cases "
            "is not the best tier right now, even if the org chart says "
            "it is. Dynamic routing weighs tier capability (can this tier "
            "decide this case), tier load (queue length and oldest wait), "
            "case affinity (has this tier seen this case before), and "
            "time-of-day coverage (who is actually staffed) - then routes "
            "to the best-scoring available tier. The routing policy is "
            "explicit and auditable: the factors, their weights, and the "
            "tie-breakers are published, because a routing decision nobody "
            "can explain is a grievance waiting to happen. Guards keep the "
            "dynamism honest: a case never routes below its severity's "
            "minimum tier, never bounces between tiers more than twice "
            "without human review, and every routing decision is an "
            "audit-trail event with the scores shown."
        ),
        "how_it_works": (
            "Dynamic routing works as scored selection over eligible "
            "tiers. On trigger, the router lists tiers whose capability "
            "covers the case's needs and whose minimum-severity rule the "
            "case satisfies. For each eligible tier it computes a score: "
            "capability match, minus a load penalty proportional to queue "
            "length and oldest wait, plus an affinity bonus if the tier "
            "handled the case before, gated by current staffing. The "
            "highest score wins; ties break toward the lower tier to "
            "preserve senior capacity. The decision record carries the "
            "scores, so a questioned routing can be replayed. Anti-flapping "
            "rules prevent oscillation: a case routed to tier B stays "
            "there for a minimum dwell unless severity rises, and the "
            "two-bounce limit forces human review instead of a third "
            "bounce. Load shedding is the emergency mode: when all tiers "
            "exceed their thresholds, the router degrades gracefully - "
            "lower-severity cases queue with published expectations rather "
            "than all cases degrading silently. The routing weights are "
            "tuned from the trail: if affinity-bonus routings resolve "
            "faster, the bonus grows."
        ),
        "key_points": [
            "Dynamic routing scores eligible tiers on capability, live load, case affinity, and staffing - then routes to the best score at the moment of need.",
            "The routing policy is published: factors, weights, tie-breakers - a routing nobody can explain is a grievance waiting to happen.",
            "Guards keep it honest: never below the severity's minimum tier, never more than two bounces without human review.",
            "Every routing decision is an audit event with the scores shown, replayable when questioned.",
            "Emergency mode sheds load gracefully: lower-severity cases queue with published expectations instead of everything degrading silently.",
        ],
        "requirements": [
            "Eligibility rules per tier: capability coverage and minimum severity.",
            "Live load signals per tier: queue length, oldest wait, staffing.",
            "A published scoring policy with factors, weights, and tie-breakers.",
            "Anti-flapping rules: minimum dwell per routing and a two-bounce human-review limit.",
            "Routing decision records with scores, replayable from the trail.",
        ],
        "standards": [
            "Routing factors exclude protected attributes; scores are computed from work signals only.",
            "Weight changes are versioned and announced - silent retuning of who gets help first is prohibited.",
            "Emergency degradation thresholds are published in advance so degraded service is expected, not discovered.",
        ],
        "citations": [CIT_ITIL, CIT_DUMAS, CIT_MINING],
        "sig_lens": (
            "The Signature read: the ladder that chooses its own rung, and "
            "the Signature Operations Method lets it choose - by sworn, "
            "published arithmetic of strength, burden, memory, and watch. "
            "No charge descends below its peril's rank, none is bounced "
            "like a stone, and every choosing is witnessed with its "
            "numbers, so the ladder's judgment can always be called to "
            "account."
        ),
    },
    {
        "key": "workflow_engines",
        "name": "Workflow Engines and Durable Execution",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A workflow engine is the machine that runs the drawn path: it "
            "creates cases, routes tokens, assigns tasks, fires timers, "
            "and writes the audit trail. Durable execution is the engine's "
            "hardest promise: a case that runs for weeks must survive "
            "crashes, restarts, and deployments without losing its place "
            "or repeating its effects. The architecture that delivers it "
            "is event sourcing: the case's state is not stored as a row "
            "to be overwritten but derived by replaying its event log from "
            "the beginning - the log is the truth, the state is a cache. "
            "Effects on the world go through the outbox pattern: the "
            "engine writes the intent (send the email, charge the card) "
            "to the log first, then a dispatcher performs it, so a crash "
            "between intent and action replays to exactly-once effect "
            "rather than zero or two. Timers are durable too: a timer is a "
            "log entry with a fire time, and the scheduler replays pending "
            "timers after every restart. The engine is thus a log with a "
            "scheduler and a dispatcher - simple parts, composed into "
            "immortality for the case."
        ),
        "how_it_works": (
            "Durable execution works by making the log the system of "
            "record. Every state change - case created, task completed, "
            "timer set, message sent - is appended as an event before it "
            "takes effect; the engine's in-memory case state is rebuilt "
            "by folding the events in order. On crash, the engine restarts, "
            "replays each case's log to reconstruct exact state, and "
            "resumes: pending timers are rescheduled from their log "
            "entries, unacknowledged dispatches are retried by the "
            "outbox dispatcher. Exactly-once effects come from "
            "idempotency keys carried in the log: the dispatcher records "
            "the key with the completed action, so a replayed dispatch "
            "with the same key is acknowledged without re-performing. "
            "Snapshots bound the replay cost: every N events the engine "
            "stores the folded state, and recovery replays only from the "
            "latest snapshot. Deployments are just planned crashes: drain "
            "the schedulers, persist, restart on the new version, replay, "
            "resume. A case can thus outlive every machine it ever ran on "
            "- which is precisely the point, because business cases "
            "routinely outlive servers."
        ),
        "key_points": [
            "Durable execution means a weeks-long case survives crashes, restarts, and deployments without losing its place or repeating its effects.",
            "Event sourcing makes the log the truth and the state a cache: recovery replays the log to rebuild exact case state.",
            "The outbox pattern writes intent to the log before acting, so a crash between intent and action replays to exactly-once effect.",
            "Idempotency keys in the log let a replayed dispatch be acknowledged without re-performing the action.",
            "Snapshots bound replay cost; deployments are planned crashes - drain, persist, restart, replay, resume.",
        ],
        "requirements": [
            "An append-only event log as the system of record for case state.",
            "Outbox dispatch for every world-changing effect with idempotency keys.",
            "Durable timers as log entries with fire times, rescheduled on recovery.",
            "Snapshots bounding replay length with a published interval.",
            "Crash-recovery drills proving replay reconstructs exact state.",
        ],
        "standards": [
            "No case state lives only in memory; everything needed for recovery is in the log or a snapshot.",
            "Idempotency keys are unique per intended effect and retained for the dispute window.",
            "Recovery time objectives are measured by drill, not estimated - a recovery plan that was never rehearsed is fiction.",
        ],
        "citations": [CIT_WESKE, CIT_NEWMAN, CIT_DUMAS],
        "sig_lens": (
            "The Signature read: the engine that cannot die, and the "
            "Signature Operations Method builds it from the log-as-truth - "
            "every station's arrival written before it is felt, every deed "
            "upon the world intended in writing before it is done. Though "
            "the machine fall and rise again, the case remembers itself "
            "perfectly, for its memory is the unbroken testimony, not the "
            "fleeting mind."
        ),
    },
    {
        "key": "case_records_at_scale",
        "name": "Case Records at Scale",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Everything in this database assumes cases can be found, read, "
            "and counted - at a million cases, that assumption needs "
            "engineering. Case records at scale rest on four pillars. "
            "Partitioning divides the case store - by time, by region, by "
            "case type - so no single store holds everything and queries "
            "touch only relevant partitions. Indexing answers the common "
            "questions - by status, by owner, by SLA risk - without "
            "scanning: the index is the map, the scan is the wilderness. "
            "Archival moves closed cases to cheaper, slower storage on a "
            "schedule, keeping the hot store for live work while the full "
            "history remains retrievable. Aggregation precomputes the "
            "dashboards: the counts, percentiles, and flow diagrams are "
            "maintained incrementally as events arrive rather than "
            "recomputed over the whole trail on every page load. The "
            "capacity math is honest: a million cases with a thousand "
            "events each is a billion events, and the architecture is "
            "chosen for the billion, not the thousand. Scale is a design "
            "constraint, not a later optimization."
        ),
        "how_it_works": (
            "Scale works by dividing and precomputing. The case store is "
            "partitioned - typically by creation month plus case type - so "
            "a query for this month's open P1 cases opens one partition, "
            "not the archive; partition keys are part of every query by "
            "convention. Secondary indexes on status, owner, and SLA-risk "
            "flag make the operational queries logarithmic rather than "
            "linear: finding one case among a million costs about twenty "
            "comparisons, not a million. The hot-warm-cold lifecycle "
            "moves cases automatically: open cases in hot storage, "
            "recently closed in warm, older than the retention window in "
            "cold archival - with the retrieval path identical and only "
            "the latency differing. Stream aggregation maintains the "
            "dashboard numbers: each appended event updates running counts "
            "and percentile sketches, so the p90 is always current without "
            "a full recompute. Backpressure protects the pipeline: when "
            "ingest exceeds processing, the system sheds or queues by "
            "policy instead of collapsing. Load tests prove the numbers "
            "before the users do."
        ),
        "key_points": [
            "Four pillars at scale: partitioning, indexing, archival, and precomputed aggregation - scale is a design constraint, not a later optimization.",
            "Partition by time and case type so queries touch one partition; index status, owner, and SLA risk so lookups are logarithmic.",
            "The hot-warm-cold lifecycle moves closed cases to cheaper storage automatically while the retrieval path stays identical.",
            "Stream aggregation maintains dashboard numbers incrementally as events arrive - the p90 is always current without full recomputes.",
            "Backpressure sheds or queues by policy when ingest exceeds processing; load tests prove the numbers before the users do.",
        ],
        "requirements": [
            "A partition scheme with the partition key in every query by convention.",
            "Secondary indexes on status, owner, and SLA-risk flag.",
            "A hot-warm-cold lifecycle with automatic movement and identical retrieval paths.",
            "Incremental aggregation for all dashboard metrics.",
            "Backpressure policy and load tests at the target scale.",
        ],
        "standards": [
            "Capacity planning uses the billion-event math - a million cases times a thousand events - not the demo-sized numbers.",
            "Archival never deletes: cold storage is retrievable, with retrieval latency published.",
            "Index definitions are versioned with the schema; a query plan that ignores the index is a defect to fix, not a cost to accept.",
        ],
        "citations": [CIT_MINING, CIT_WESKE, CIT_NEWMAN],
        "sig_lens": (
            "The Signature read: the archive that must hold a million "
            "travelers' testimonies, and the Signature Operations Method "
            "raises it on four pillars - the divided halls, the maps of "
            "indexes, the cold vaults for the closed journeys, and the "
            "ever-current tallies. The billion-event arithmetic is faced "
            "at the founding, for a hall built for a thousand collapses "
            "under a million."
        ),
    },
])
