#!/usr/bin/env python3
"""Topics + config for the social-work-services pair. Property of Justin Addam Higgins (JAH)."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "social-work-services",
    "name_pub": "The Social Work Services Database",
    "name_sig": "Signature Social Work Services Database",
    "tagline_pub": ("Social work services from the ground up: what services exist, who is eligible, "
                    "how care is coordinated across agencies, how community needs are assessed, "
                    "how referrals flow, and how program outcomes are measured - every record carrying "
                    "the full entry taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of social work services: the same "
                    "real service knowledge carried forward, plus Signature-built coordination models, "
                    "referral-system designs, and outcome frameworks original to this system."),
    "record_kind": "social work service record",
    "record_kind_plural": "social work service records",
    "prefix_pub": "JAH-SWS-", "prefix_sig": "JAH-SWSS-",
    "ai_pub": "JAH Social Work Services Archivist",
    "ai_sig": "JAH Signature Social Work Services Creator",
    "role_pub": ("social work services archivist - teaching what services exist, who is eligible, "
                 "how care is coordinated, how referrals flow, and how outcomes are measured; "
                 "answers from many angles - definition, example, process, eligibility, coordination - "
                 "using only archive data from this system"),
    "role_sig": ("Signature creator of social work service systems - designing coordination models, "
                 "referral architectures, and outcome frameworks as original Signature works; "
                 "answers from many angles using only archive data from this system"),
    "search_ph": "Search services, eligibility, referrals, care coordination, outcomes...",
    "chat_ph": "Ask about social work services...",
    "greet_pub": ("I am the JAH Social Work Services Archivist. Ask me about services, eligibility, "
                  "care coordination, referrals, community needs, and program outcomes."),
    "greet_sig": ("I am the JAH Signature Social Work Services Creator. Ask me about Signature-built "
                  "service coordination models, referral designs, and outcome frameworks."),
    "gen_blurb": ("Generate clearly-labeled social work service studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded social work service records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced."),
    "demo_kind": "social-work-demo",
    "demo_title": "Social Work Services Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = ('# Social Work Services Demo — %s\n# Edition: %s\n' % (topic["title"], edition))

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "eligibility":
        return fill(
            "needs = @@NEEDS@@\ncriteria = @@CRIT@@\n"
            "matches = [c for c in criteria if any(n in c['covers'] for n in needs)]\n"
            "print('Client needs:', ', '.join(needs))\n"
            "print('Programs checked:', len(criteria))\n"
            "for m in matches:\n"
            "    print('ELIGIBLE:', m['program'], '| covers:', ', '.join(m['covers']))\n"
            "print('Eligible programs:', len(matches))\n",
            {"NEEDS": p["needs"], "CRIT": p["criteria"]})
    if v == "referral":
        return fill(
            "needs = @@NEEDS@@\nagencies = @@AGS@@\n"
            "plan = {}\n"
            "for need in needs:\n"
            "    cands = [a for a in agencies if need in a['serves']]\n"
            "    plan[need] = cands[0]['name'] if cands else 'NO MATCH - escalate'\n"
            "print('Referral plan:')\n"
            "for need, ag in plan.items():\n"
            "    print(' ', need, '->', ag)\n"
            "unmatched = [n for n, a in plan.items() if a.startswith('NO MATCH')]\n"
            "print('Unmatched needs:', len(unmatched))\n",
            {"NEEDS": p["needs"], "AGS": p["agencies"]})
    if v == "caseload":
        return fill(
            "cases = @@CASES@@\n"
            "by_status = {}\n"
            "for c in cases:\n"
            "    by_status[c['status']] = by_status.get(c['status'], 0) + 1\n"
            "open_cases = [c for c in cases if c['status'] == 'open']\n"
            "avg_needs = sum(len(c['needs']) for c in cases) / len(cases)\n"
            "print('Caseload size:', len(cases))\n"
            "print('By status:', by_status)\n"
            "print('Open cases:', len(open_cases))\n"
            "print('Average needs per case: %.2f' % avg_needs)\n",
            {"CASES": p["cases"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "pct = 100.0 * delta / pre if pre else 0.0\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d (%+.1f%%)' % (pre, post, delta, pct))\n"
            "print('Direction:', 'improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged')\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    if v == "priority":
        return fill(
            "items = @@ITEMS@@\n"
            "ranked = sorted(items, key=lambda x: x['severity'] * x['reach'], reverse=True)\n"
            "print('Community needs ranked by severity x reach:')\n"
            "for i, it in enumerate(ranked, 1):\n"
            "    score = it['severity'] * it['reach']\n"
            "    print(' %d. %s (score %d)' % (i, it['need'], score))\n",
            {"ITEMS": p["items"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
# ---------------- Foundations (11) ----------------
dict(title="What Social Work Services Are", tier=F,
 desc_pub=("Social work services are organized helping services delivered by trained social workers "
  "and allied staff to individuals, families, groups, and communities. They span child welfare, "
  "health care, mental health, schools, aging, housing, and community development. The unifying "
  "purpose is to help people solve problems in living, strengthen their capacity to cope, and connect "
  "them with resources and opportunities.\n"
  "Services are delivered through public agencies, nonprofit organizations, hospitals, schools, and "
  "private practice. A social worker's core tools are assessment, counseling, case management, "
  "advocacy, and community organizing. Services are voluntary in most settings, confidential within "
  "legal limits, and grounded in respect for each person's dignity and right to self-determination."),
 desc_sig=("The Signature system treats social work services as a coordination science: every service "
  "is modeled as a node in a help network, with defined inputs (referrals), processes (interventions), "
  "and outputs (measurable outcomes). This Signature framing lets the whole service array be designed, "
  "tested, and improved as one system rather than a patchwork of programs."),
 how_pub=("A person or family contacts a service agency, often through a referral, a helpline, or a "
  "walk-in. A social worker conducts an intake interview, assesses needs and strengths, and together "
  "with the client builds a service plan with concrete goals. The worker then delivers or brokers "
  "services - counseling, benefits assistance, referrals - and follows up to check progress, adjusting "
  "the plan until goals are met or the case closes."),
 how_sig=("In the Signature model the same flow is instrumented end to end: intake data, plan milestones, "
  "referral handoffs, and outcome scores all feed one case record, so coordination gaps become visible "
  "and fixable instead of invisible."),
 keys=["Serve individuals, families, groups, and whole communities",
  "Core methods: assessment, counseling, case management, advocacy, organizing",
  "Delivered by public agencies, nonprofits, hospitals, schools, private practice",
  "Grounded in dignity, self-determination, and social justice",
  "Most services are voluntary and confidential within legal limits",
  "Goal: solve problems in living and connect people to resources"],
 reqs=["Trained social work staff (typically BSW or MSW prepared)",
  "Clear intake and eligibility procedures",
  "Confidential record-keeping systems",
  "Supervision and ethical oversight"],
 stds=["NASW Code of Ethics (public professional standard)",
  "Council on Social Work Education accreditation expectations",
  "Agency licensing and program standards in each jurisdiction"],
 cites=["National Association of Social Workers — Code of Ethics (public standard)",
  "Council on Social Work Education — accreditation standards (public)",
  "U.S. Bureau of Labor Statistics — Occupational Outlook: Social Workers (public)"],
 demo=("referral", {"needs": ["counseling", "food assistance"],
   "agencies": [{"name": "Family Counseling Center", "serves": ["counseling"]},
                {"name": "Community Food Bank", "serves": ["food assistance"]}]})),

dict(title="Fields of Social Work Practice", tier=F,
 desc_pub=("Social work practice is organized into fields, each a cluster of settings serving a "
  "population or problem area. Major fields include child and family welfare, school social work, "
  "health and hospital social work, mental health and substance use, aging and gerontology, housing "
  "and homelessness, domestic violence, corrections, military and veterans services, and community "
  "development. Each field has its own knowledge base, laws, and partner agencies.\n"
  "Workers often specialize: a hospital social worker masters discharge planning and insurance "
  "navigation, while a school social worker masters special-education law and truancy intervention. "
  "Fields overlap constantly - a single family may touch child welfare, housing, and health services "
  "at once - which is why coordination across fields is a central professional skill."),
 desc_sig=("The Signature system maps every field onto one shared service ontology - populations, "
  "settings, interventions, and outcomes use the same vocabulary everywhere - so a case crossing "
  "fields never gets lost in translation between agency jargons."),
 how_pub=("A client enters through one field's door - say, a hospital - and the social worker "
  "assesses needs that spill into other fields, such as housing or food. The worker refers, "
  "coordinates, and follows up across field boundaries, keeping one coherent plan. Specialists in "
  "each field contribute their setting's tools while the lead worker holds the whole picture."),
 how_sig=("Signature field-crossing uses a single shared plan document with field-tagged tasks, so "
  "every specialist sees the same goals and their own part in them."),
 keys=["Major fields: child/family, schools, health, mental health, aging, housing, corrections",
  "Each field has distinct laws, agencies, and practice knowledge",
  "Specialists master their setting's tools and rules",
  "Real cases routinely cross field boundaries",
  "Coordination across fields is a core professional skill",
  "Community development works at the neighborhood and policy level"],
 reqs=["Field-specific training and supervised experience",
  "Knowledge of the field's governing laws and programs",
  "Directory of partner agencies in the field"],
 stds=["Field-specific practice standards published by professional associations",
  "State licensing laws defining scope of practice"],
 cites=["National Association of Social Workers — practice standards by field (public)",
  "U.S. Bureau of Labor Statistics — social worker work settings (public)"],
 demo=("caseload", {"cases": [
   {"id": "C-101", "status": "open", "needs": ["housing", "counseling"]},
   {"id": "C-102", "status": "open", "needs": ["food assistance"]},
   {"id": "C-103", "status": "monitoring", "needs": ["employment", "childcare"]},
   {"id": "C-104", "status": "closed", "needs": ["benefits"]}]})),

dict(title="The Social Work Helping Process", tier=F,
 desc_pub=("The helping process is the profession's standard problem-solving sequence: engagement, "
  "assessment, planning, intervention, evaluation, and termination. Engagement builds trust and a "
  "working relationship. Assessment gathers facts about the person, their environment, and the "
  "problem. Planning turns assessment into measurable goals with agreed actions. Intervention carries "
  "out the plan. Evaluation checks whether goals were met. Termination closes the relationship "
  "deliberately, with referrals if further help is needed.\n"
  "The process is a loop, not a straight line: evaluation often sends the worker back to "
  "re-assessment and a revised plan. What makes it professional rather than casual helping is that "
  "each phase is documented, supervised, and tied to the client's own stated goals."),
 desc_sig=("Signature practice instruments each phase with checkable artifacts - engagement notes, "
  "assessment scores, plan milestones, intervention logs, outcome deltas, closure summaries - so the "
  "helping process becomes auditable and improvable, not just well-intentioned."),
 how_pub=("The worker meets the client, listens, and contracts for work together. They assess "
  "strengths and needs using interviews and standardized tools, then draft a plan the client "
  "approves. Services are delivered over weeks or months with regular check-ins measuring progress "
  "against the goals. When goals are met, worker and client review gains, plan for setbacks, and "
  "close the case."),
 how_sig=("Signature tracking attaches a milestone checklist to every plan, so both worker and client "
  "can see at a glance which goals are on track and which need a new approach."),
 keys=["Six phases: engagement, assessment, planning, intervention, evaluation, termination",
  "The process loops back when evaluation shows the plan is not working",
  "Goals are set with the client, not for the client",
  "Each phase is documented and supervised",
  "Strengths are assessed alongside problems",
  "Termination is planned, not abrupt"],
 reqs=["A contracted working relationship with the client",
  "Assessment tools appropriate to the setting",
  "A written service plan with measurable goals"],
 stds=["NASW Code of Ethics — client self-determination and informed consent",
  "Agency case-documentation standards"],
 cites=["National Association of Social Workers — Code of Ethics (public)",
  "Council on Social Work Education — practice competencies (public)"],
 demo=("outcome", {"label": "Client goal attainment score", "pre": 42, "post": 78})),

dict(title="Client Intake and Assessment", tier=F,
 desc_pub=("Intake is the structured first contact where an agency learns who the client is, what "
  "they need, and whether the agency can help. It collects identifying information, the presenting "
  "problem, safety concerns, household composition, income and benefits, health and mental health "
  "history, and consent forms. Assessment goes deeper: the worker analyzes how personal, family, and "
  "environmental factors interact to produce the problem, and what strengths can be mobilized.\n"
  "Good intake is brief but complete - long enough to route the client correctly, short enough not to "
  "exhaust them. Standardized screening tools (for depression, substance use, domestic violence, fall "
  "risk) are often embedded in intake so nothing critical is missed at the door."),
 desc_sig=("The Signature intake model is a decision tree: each answer routes to the next most "
  "informative question, so assessments finish faster and every completed intake carries a structured "
  "risk-and-needs profile usable by every downstream service."),
 how_pub=("The client provides information in person, by phone, or online. The worker verifies "
  "eligibility, screens for safety issues first, and administers brief standardized screens. Findings "
  "are summarized into a needs-and-strengths profile, which determines the service plan or a referral "
  "elsewhere. The client signs consent and privacy notices before anything is shared."),
 how_sig=("Signature intake software scores the profile instantly and suggests the three most "
  "relevant programs, which the worker confirms or overrides with documented reasons."),
 keys=["Intake collects identity, problem, safety, household, income, health history",
  "Safety screening always comes first",
  "Standardized screens catch depression, substance use, violence risk",
  "Assessment analyzes person-in-environment, not just symptoms",
  "Strengths are inventoried alongside needs",
  "Consent and privacy notices precede any information sharing"],
 reqs=["Private interview space and intake forms",
  "Validated screening instruments for the population served",
  "Eligibility rules for the agency's programs"],
 stds=["NASW standards for confidentiality and informed consent",
  "HIPAA privacy requirements where health data is involved"],
 cites=["Substance Abuse and Mental Health Services Administration — screening tools (public)",
  "U.S. Dept. of Health and Human Services — HIPAA privacy guidance (public)"],
 demo=("eligibility", {"needs": ["counseling", "rental assistance"],
   "criteria": [{"program": "Emergency Aid Fund", "covers": ["rental assistance", "utilities"]},
                {"program": "Counseling Scholarship", "covers": ["counseling"]},
                {"program": "Job Training Grant", "covers": ["employment"]}]})),

dict(title="Service Eligibility Basics", tier=F,
 desc_pub=("Eligibility rules decide who can receive a service. Public programs typically test "
  "residency, household size, income against a threshold (often a percentage of the federal poverty "
  "level), and categorical factors such as age, disability, veteran status, or having minor children. "
  "Nonprofit programs set their own criteria - a shelter may serve unaccompanied youth ages 16-24, a "
  "food pantry may serve anyone in its zip codes.\n"
  "Eligibility is verified with documents: ID, proof of address, pay stubs, benefit letters. Workers "
  "help clients assemble paperwork, request verifications, and appeal denials. Because rules change "
  "yearly, keeping an updated eligibility reference is a core agency function."),
 desc_sig=("The Signature eligibility engine encodes program rules as checkable logic, so a worker "
  "enters client facts once and instantly sees every program the client qualifies for, with the exact "
  "documents still needed for each."),
 how_pub=("The worker identifies programs matching the client's needs, compares client facts to each "
  "program's written criteria, and lists what is missing. The client gathers documents with the "
  "worker's help; the worker submits the application and tracks its decision. Denials trigger a review "
  "of appeal rights and deadlines, and the worker files the appeal or finds an alternative."),
 how_sig=("Signature rule-encoding turns eligibility from memory work into computation: one profile, "
  "all programs, instant matches, document checklists generated automatically."),
 keys=["Common tests: residency, household size, income, age, disability, veteran status",
  "Income thresholds usually tie to the federal poverty level",
  "Verification uses ID, address proof, pay stubs, benefit letters",
  "Denials carry appeal rights and deadlines",
  "Rules change yearly - references must stay current",
  "Workers bridge the paperwork gap for clients"],
 reqs=["Current written eligibility criteria for each program",
  "Document checklists and appeal procedures",
  "Secure storage for client verification documents"],
 stds=["Program statutes and regulations defining eligibility",
  "Agency verification and anti-fraud procedures"],
 cites=["U.S. Dept. of Health and Human Services — federal poverty guidelines (public)",
  "Social Security Administration — program eligibility rules (public)"],
 demo=("eligibility", {"needs": ["food assistance", "health coverage"],
   "criteria": [{"program": "SNAP", "covers": ["food assistance"]},
                {"program": "Medicaid", "covers": ["health coverage"]},
                {"program": "WIC", "covers": ["food assistance", "nutrition"]}]})),

dict(title="Case Management Fundamentals", tier=F,
 desc_pub=("Case management is the organizing service: one worker (or team) holds the whole picture "
  "of a client's needs, plans services across providers, monitors delivery, and advocates when "
  "systems stall. Core functions are assessment, planning, linking clients to services, monitoring, "
  "and advocacy. It is the difference between a client navigating five agencies alone and having a "
  "guide who knows all five.\n"
  "Models vary by intensity. Brokerage models mainly refer and check in. Intensive models - assertive "
  "community treatment, wraparound - carry small caseloads with frequent contact. Caseload size, "
  "contact frequency, and documentation standards are set by the model and the funder."),
 desc_sig=("Signature case management is built around a living service plan: every linked provider "
  "updates the same plan, milestones are visible to all, and stalled referrals trigger automatic "
  "follow-up tasks so no client falls through the cracks between agencies."),
 how_pub=("The case manager assesses, writes a plan with the client, and makes referrals with warm "
  "handoffs - introductions, shared information (with consent), and scheduled follow-ups. They "
  "monitor whether services were received and helped, troubleshoot barriers like transportation or "
  "missed appointments, and reconvene the plan team when needs change."),
 how_sig=("In the Signature model the plan is a shared digital workspace: referrals are tasks with "
  "owners and due dates, and the case manager sees real-time status across every provider."),
 keys=["Functions: assess, plan, link, monitor, advocate",
  "Brokerage vs intensive models differ in contact frequency",
  "Warm handoffs beat cold referrals",
  "The case manager holds the whole picture across providers",
  "Caseload size is set by model and funder",
  "Documentation proves services were delivered and effective"],
 reqs=["A manageable caseload ratio for the model used",
  "Release-of-information forms for each provider",
  "A tracking system for referrals and follow-ups"],
 stds=["Case Management Society of America — standards of practice (public)",
  "Funder-specific caseload and contact standards"],
 cites=["Case Management Society of America — Standards of Practice (public)",
  "Substance Abuse and Mental Health Services Administration — case management models (public)"],
 demo=("caseload", {"cases": [
   {"id": "K-201", "status": "open", "needs": ["housing", "benefits", "counseling"]},
   {"id": "K-202", "status": "open", "needs": ["employment"]},
   {"id": "K-203", "status": "monitoring", "needs": ["healthcare", "transportation"]},
   {"id": "K-204", "status": "open", "needs": ["childcare", "food assistance"]},
   {"id": "K-205", "status": "closed", "needs": ["legal aid"]}]})),

dict(title="Confidentiality and Client Rights", tier=F,
 desc_pub=("Clients have the right to privacy, to be informed about services, to participate in "
  "decisions, to refuse services, and to complain without retaliation. Confidentiality means client "
  "information is shared only with informed written consent, except where law requires disclosure: "
  "suspected child or elder abuse, imminent danger to self or others, and court orders.\n"
  "Workers explain these limits at the start - before the client discloses - so consent is truly "
  "informed. Records are stored securely, accessed on a need-to-know basis, and clients generally "
  "have the right to see their own records and request corrections."),
 desc_sig=("The Signature rights framework bakes consent into the data layer: every shared field "
  "carries its consent record, and disclosures outside consent are blocked by the system, not just "
  "by policy."),
 how_pub=("At intake the worker reviews a rights-and-limits statement with the client and gets a "
  "signature. Before each referral the worker explains what will be shared, with whom, and why, and "
  "obtains a specific release. Mandatory reports (abuse, imminent danger) are made promptly and the "
  "client is told what was reported, to the extent the law allows."),
 how_sig=("Signature consent management issues machine-readable releases per provider and purpose, "
  "with automatic expiry - so old permissions cannot be reused indefinitely."),
 keys=["Rights: privacy, information, participation, refusal, complaint without retaliation",
  "Confidentiality has legal exceptions: abuse, imminent danger, court orders",
  "Limits are explained before disclosure, not after",
  "Releases are specific: what, with whom, why, for how long",
  "Records are need-to-know and securely stored",
  "Clients can usually access and correct their records"],
 reqs=["Written rights-and-limits statement in plain language",
  "Release-of-information forms per provider",
  "Secure record storage with access controls"],
 stds=["NASW Code of Ethics — privacy and confidentiality",
  "State mandatory-reporting statutes",
  "HIPAA and 42 CFR Part 2 where applicable"],
 cites=["National Association of Social Workers — Code of Ethics (public)",
  "U.S. Dept. of Health and Human Services — HIPAA guidance (public)"],
 demo=("referral", {"needs": ["counseling"],
   "agencies": [{"name": "Licensed Counseling Practice (consent on file)", "serves": ["counseling"]}]})),

dict(title="Community Needs Assessment", tier=F,
 desc_pub=("A community needs assessment systematically identifies what a population needs and what "
  "assets already exist. Methods include surveys, focus groups, key-informant interviews, analysis of "
  "census and agency data, and asset mapping. The product is a ranked list of needs with evidence - "
  "not impressions - behind each ranking.\n"
  "Assessments drive planning: funders require them before awarding grants, agencies use them to set "
  "priorities, and coalitions use them to divide labor. Repeating the assessment every few years "
  "shows whether needs are shrinking or shifting."),
 desc_sig=("Signature needs assessment fuses survey, administrative, and geospatial data into living "
  "need maps that update as new data arrives, replacing the static every-five-years report with a "
  "continuously current picture."),
 how_pub=("Planners define the community and questions, gather existing data (census, 211 call logs, "
  "agency intake stats), then collect new data through surveys and focus groups with residents. Gaps "
  "between needs and current services are scored by severity and reach, producing a ranked agenda "
  "that is published and used to guide funding and program design."),
 how_sig=("In the Signature model the ranking is a computed score - severity times reach times service "
  "gap - so priorities are transparent and re-computable when facts change."),
 keys=["Methods: surveys, focus groups, interviews, census and agency data, asset mapping",
  "Product: evidence-ranked list of needs",
  "Funders require assessments before grants",
  "Asset mapping inventories existing strengths, not just deficits",
  "Residents participate as informants, not just subjects",
  "Repeated assessments track change over time"],
 reqs=["A defined community boundary and study questions",
  "Access to census and local administrative data",
  "Resident participation channels"],
 stds=["Community needs-assessment methodology standards (public planning literature)",
  "Funder-specific assessment requirements"],
 cites=["U.S. Census Bureau — American Community Survey data (public)",
  "Centers for Disease Control — community health assessment guidance (public)"],
 demo=("priority", {"items": [
   {"need": "Affordable childcare", "severity": 9, "reach": 8},
   {"need": "Evening bus service", "severity": 6, "reach": 7},
   {"need": "Youth recreation", "severity": 7, "reach": 6},
   {"need": "Senior home repair", "severity": 8, "reach": 4}]})),

dict(title="Resource Mapping", tier=F,
 desc_pub=("Resource mapping inventories every helping resource in a community - agencies, programs, "
  "eligibility rules, capacity, contact points - and organizes them so workers and residents can "
  "find help fast. A good map covers food, housing, health, mental health, substance use, employment, "
  "childcare, transportation, legal aid, and crisis lines, with hours, languages, and access notes.\n"
  "Maps go stale quickly: programs open, close, and change criteria. The professional standard is a "
  "living directory with named owners who verify each entry on a schedule, plus a public-facing "
  "version (often through 211 systems) so residents can search directly."),
 desc_sig=("Signature resource mapping is a structured, versioned dataset - every entry has an owner, "
  "a verification date, and machine-readable eligibility - so referral engines can match clients to "
  "currently-valid resources automatically."),
 how_pub=("Mappers list service categories, then identify providers through directories, 211 data, "
  "and field outreach. Each entry is verified by phone or visit: services, eligibility, capacity, "
  "waitlists, languages. The map is published as a searchable directory and a worker reference, with "
  "a re-verification calendar keeping it alive."),
 how_sig=("Signature entries carry expiry dates; the system nudges owners to re-verify and flags "
  "stale entries to workers before a referral is made."),
 keys=["Covers all major service categories with access details",
  "Each entry verified by direct contact, not just web scraping",
  "Living directories beat one-time maps",
  "211 systems are the public backbone in many regions",
  "Named owners keep entries current",
  "Worker and public versions serve different needs"],
 reqs=["A service taxonomy covering local need categories",
  "Verification schedule and entry owners",
  "Searchable public and worker-facing formats"],
 stds=["211 data standards (public)",
  "Agency directory-accuracy expectations"],
 cites=["211.org — community resource directory standards (public)",
  "U.S. Dept. of Health and Human Services — community resource guidance (public)"],
 demo=("referral", {"needs": ["food assistance", "legal aid", "transportation"],
   "agencies": [{"name": "Community Food Bank", "serves": ["food assistance"]},
                {"name": "Legal Aid Society", "serves": ["legal aid"]},
                {"name": "Senior Ride Program", "serves": ["transportation"]}]})),

dict(title="Referral Systems", tier=F,
 desc_pub=("A referral system is the machinery that moves clients between services: how needs are "
  "identified, how matches are found, how introductions happen, and how follow-up confirms the "
  "client actually connected. Systems range from a paper directory and phone calls to integrated "
  "electronic referral platforms shared across a coalition.\n"
  "What separates a system from ad-hoc referring is closed-loop follow-up: the referring worker "
  "learns whether the appointment happened and what resulted. Closed loops typically double the "
  "rate at which referrals turn into received services compared to handing a client a phone number."),
 desc_sig=("The Signature referral system is fully closed-loop by design: referrals are tracked tasks "
  "with owners and deadlines, outcomes flow back to the referrer automatically, and unmatched needs "
  "escalate instead of evaporating."),
 how_pub=("The worker identifies the need, finds matching providers using the resource map, and makes "
  "a warm handoff - calling ahead, sharing relevant information with consent, and scheduling the "
  "appointment. The worker then follows up with both client and provider: did contact happen, was "
  "the service delivered, what is next. Failures trigger a new attempt or an alternative."),
 how_sig=("Signature referrals carry structured need data with consent, so receiving agencies get "
  "complete intake packets instead of vague phone messages."),
 keys=["Components: identification, matching, handoff, follow-up",
  "Warm handoffs outperform cold referrals",
  "Closed-loop follow-up confirms services were received",
  "Electronic platforms scale what phones and paper cannot",
  "Consent governs every information transfer",
  "Failed referrals get a second attempt, not a shrug"],
 reqs=["An up-to-date provider directory",
  "Consent and information-sharing agreements",
  "A follow-up tracking method"],
 stds=["Coalition referral-protocol agreements",
  "Privacy rules for inter-agency sharing"],
 cites=["Substance Abuse and Mental Health Services Administration — referral best practices (public)",
  "Health Resources and Services Administration — care coordination guidance (public)"],
 demo=("referral", {"needs": ["housing", "counseling", "employment"],
   "agencies": [{"name": "Housing First Program", "serves": ["housing"]},
                {"name": "Community Counseling", "serves": ["counseling"]}]})),

dict(title="Documentation and Case Notes", tier=F,
 desc_pub=("Documentation is the written record of what happened, what was decided, and why. Case "
  "notes typically follow a structure such as SOAP (Subjective, Objective, Assessment, Plan) or DAP "
  "(Data, Assessment, Plan). Good notes are factual, concise, timely - written within a day or two - "
  "and focused on clinically relevant information.\n"
  "Notes serve the client (continuity when workers change), the agency (proof of services for "
  "funders and auditors), and the worker (memory and supervision). They must avoid jargon, judgment, "
  "and speculation, because clients can read them and courts can subpoena them."),
 desc_sig=("Signature documentation pairs human notes with structured data capture - goals, "
  "interventions, and outcome scores as fields, narrative as text - so records are both human-readable "
  "and machine-analyzable."),
 how_pub=("After each contact the worker records what the client reported, what the worker observed, "
  "the worker's professional assessment, and the plan with next steps. Notes are signed, dated, and "
  "filed in the case record. Supervisors review samples for quality, and audits check timeliness and "
  "completeness."),
 how_sig=("Signature templates prompt for the structured fields at note time, cutting after-hours "
  "charting while improving data quality."),
 keys=["Common formats: SOAP, DAP, and narrative with plan",
  "Factual, concise, timely - within 24 to 48 hours",
  "Serves continuity, accountability, and supervision",
  "Avoid jargon, judgment, and speculation",
  "Clients may read notes; courts may subpoena them",
  "Supervisors audit samples for quality"],
 reqs=["A standard note format used by all staff",
  "Secure case-record system with audit trails",
  "Timeliness expectations (e.g., 48-hour rule)"],
 stds=["Agency documentation policies",
  "Funder and licensing documentation requirements"],
 cites=["National Association of Social Workers — documentation standards (public)"],
 demo=("outcome", {"label": "Notes completed within 48 hours", "pre": 61, "post": 94})),

# ---------------- Compounded (12) ----------------
dict(title="Care Coordination Across Agencies", tier=C,
 desc_pub=("Care coordination is the deliberate organization of services among multiple providers so "
  "the client experiences one coherent plan instead of fragmented appointments. The coordinator "
  "maintains the shared care plan, schedules across agencies, reconciles conflicting instructions, "
  "and ensures information flows with consent. It is most critical for clients with complex, "
  "overlapping needs - serious mental illness, multiple chronic conditions, or child welfare "
  "involvement.\n"
  "Evidence consistently shows coordinated care reduces emergency visits, hospital readmissions, and "
  "duplicated tests while improving client satisfaction. The coordinator role can sit in a health "
  "plan, a hospital, a community agency, or a dedicated coordination organization."),
 desc_sig=("Signature coordination runs on a shared plan ledger: every provider's tasks, appointments, "
  "and notes post to one timeline visible to the whole team, with the client holding viewing rights - "
  "fragmentation becomes structurally difficult rather than merely discouraged."),
 how_pub=("With client consent, the coordinator convenes the providers, drafts a single shared plan "
  "with assigned tasks, and sets a communication rhythm - case conferences, shared notes, or a "
  "coordination platform. They track referrals to completion, resolve conflicts between providers, "
  "and measure whether the client's goals advance."),
 how_sig=("The Signature ledger auto-flags stalled tasks and conflicting orders, pushing resolution "
  "work to the coordinator before the client feels the gap."),
 keys=["One shared plan across all providers",
  "Coordinator tracks referrals to completion",
  "Conflicting instructions get reconciled, not stacked",
  "Consent-based information sharing",
  "Reduces ER visits, readmissions, duplicated services",
  "Essential for complex, multi-need clients"],
 reqs=["Inter-agency information-sharing agreements",
  "A designated coordinator with authority to convene",
  "Shared plan accessible to all team members"],
 stds=["Agency for Healthcare Research and Quality — care coordination measures (public)",
  "National Quality Forum — care coordination standards (public)"],
 cites=["Agency for Healthcare Research and Quality — Care Coordination (public)",
  "National Quality Forum — care coordination measures (public)"],
 demo=("caseload", {"cases": [
   {"id": "X-301", "status": "open", "needs": ["primary care", "mental health", "housing"]},
   {"id": "X-302", "status": "open", "needs": ["specialty care", "transportation"]},
   {"id": "X-303", "status": "monitoring", "needs": ["home health", "meals"]}]})),

dict(title="Eligibility Determination in Practice", tier=C,
 desc_pub=("Determining eligibility in practice means applying written program rules to real, messy "
  "client situations: irregular income, mixed households, missing documents, and overlapping "
  "programs with conflicting definitions of 'household' or 'income'. Skilled workers know which "
  "verifications each program accepts, how to document special circumstances, and when to request "
  "supervisor overrides or good-cause exceptions.\n"
  "The highest-value skill is sequencing: applying for programs in an order that maximizes approvals "
  "- for example, securing one benefit whose award letter then verifies income for the next. Workers "
  "also calendar redeterminations so clients do not lose benefits to missed paperwork."),
 desc_sig=("Signature sequencing computes the optimal application order from program rules and the "
  "client's facts, and calendars every redetermination automatically - the worker executes a plan "
  "instead of reconstructing one from memory each time."),
 how_pub=("The worker inventories all potentially relevant programs, gathers the client's facts once, "
  "and works through each program's checklist, documenting where the client meets, misses, or is "
  "borderline on criteria. Applications go in priority order; denials are reviewed for appeal; "
  "approvals are logged with renewal dates. The client gets a plain-language summary of what was "
  "approved, denied, and pending."),
 how_sig=("With rules encoded, the Signature engine produces the sequence, the document checklist per "
  "program, and the renewal calendar from a single client profile."),
 keys=["Real cases are messy: irregular income, mixed households, missing papers",
  "Know each program's accepted verifications",
  "Sequence applications to maximize approvals",
  "Calendar redeterminations to prevent benefit loss",
  "Document borderline cases and request overrides where allowed",
  "Give clients a plain-language approval/denial/pending summary"],
 reqs=["Program manuals with current rules",
  "A sequencing worksheet or engine",
  "A tickler system for renewals and appeals"],
 stds=["Program regulations on verification and good cause",
  "Agency quality-review standards for eligibility work"],
 cites=["Social Security Administration — program operations guidance (public)",
  "U.S. Dept. of Agriculture — SNAP eligibility policy (public)"],
 demo=("eligibility", {"needs": ["cash assistance", "childcare", "health coverage"],
   "criteria": [{"program": "TANF", "covers": ["cash assistance"]},
                {"program": "Child Care Subsidy", "covers": ["childcare"]},
                {"program": "Medicaid", "covers": ["health coverage"]},
                {"program": "SNAP", "covers": ["food assistance"]}]})),

dict(title="Benefits Navigation: SNAP, Housing, and Medicaid", tier=C,
 desc_pub=("Benefits navigation helps clients obtain and keep the big three stability programs. SNAP "
  "(Supplemental Nutrition Assistance Program) provides monthly food funds to low-income households; "
  "eligibility hinges on gross and net income tests and asset limits that vary by household "
  "composition. Housing assistance includes public housing, Housing Choice Vouchers (Section 8), and "
  "emergency rental aid - all with long waitlists navigated by priority preferences. Medicaid covers "
  "health care for low-income children, pregnant people, older adults, people with disabilities, and "
  "in expansion states, low-income adults.\n"
  "Navigators do what the programs' own systems make hard: complete applications correctly the first "
  "time, assemble verifications, respond to requests for information within deadlines, and appeal "
  "wrongful denials. First-time approval rates rise dramatically with navigator help."),
 desc_sig=("Signature benefits navigation pre-fills applications from the client profile, generates "
  "the verification packet per program, and tracks every deadline - turning a bureaucratic marathon "
  "into an executed checklist."),
 how_pub=("The navigator screens for all three programs at once, completes applications with the "
  "client, and submits verifications before deadlines. They monitor case status, respond to agency "
  "requests within the required window, and file appeals when denials look wrong. After approval, "
  "they calendar renewals and report changes that affect eligibility."),
 how_sig=("The Signature tracker watches case status and nudges the navigator the moment an agency "
  "requests information, so deadlines are never missed."),
 keys=["SNAP: food funds; income and asset tests",
  "Housing aid: public housing, vouchers, emergency rental aid; long waitlists",
  "Medicaid: health coverage; eligibility varies by state expansion status",
  "Navigator help sharply raises first-time approval rates",
  "Deadlines for verifications and appeals are strict",
  "Renewals must be calendared to avoid coverage gaps"],
 reqs=["Current program rules for the state and county",
  "Application and appeal deadline tracking",
  "Client authorization to act on their behalf where needed"],
 stds=["Federal program regulations (SNAP, Medicaid, housing programs)",
  "State plan amendments and waivers"],
 cites=["U.S. Dept. of Agriculture — SNAP policy (public)",
  "Centers for Medicare and Medicaid Services — Medicaid eligibility (public)",
  "U.S. Dept. of Housing and Urban Development — housing assistance (public)"],
 demo=("eligibility", {"needs": ["food assistance", "rental assistance", "health coverage"],
   "criteria": [{"program": "SNAP", "covers": ["food assistance"]},
                {"program": "Emergency Rental Aid", "covers": ["rental assistance"]},
                {"program": "Medicaid", "covers": ["health coverage"]}]})),

dict(title="Crisis Intervention Services", tier=C,
 desc_pub=("Crisis intervention services respond to acute situations - suicidal thoughts, psychotic "
  "episodes, domestic violence, child safety emergencies, natural disasters. The core model is "
  "immediate stabilization: ensure safety, reduce distress, assess risk, and connect to ongoing help. "
  "Services include 24-hour hotlines (such as 988 in the United States), mobile crisis teams that go "
  "to the person, crisis stabilization units, and emergency department partnerships.\n"
  "Effective crisis response follows a protocol: answer quickly, assess lethality and safety, "
  "de-escalate, develop a safety plan, and follow up within 24 to 72 hours. Follow-up is what "
  "converts a single crisis contact into a path toward stable care."),
 desc_sig=("Signature crisis response adds a learning loop: every crisis contact's risk factors, "
  "interventions, and 72-hour outcomes feed a protocol review, so the system's playbook improves with "
  "every incident while keeping each response human-led."),
 how_pub=("A call, walk-in, or dispatch triggers the protocol. The worker assesses immediate danger "
  "first - to self, to others, from others - then de-escalates and problem-solves the precipitating "
  "situation. A safety plan names warning signs, coping steps, and people to call. The worker "
  "arranges next-step care and calls back within one to three days to confirm connection."),
 how_sig=("Signature follow-up is scheduled at contact time and tracked to completion; missed "
  "follow-ups escalate to a supervisor automatically."),
 keys=["Goal: immediate stabilization, not long-term therapy",
  "Safety assessment always comes first",
  "988 provides 24-hour crisis access in the U.S.",
  "Mobile teams bring response to the person",
  "Safety plans name warning signs, coping steps, contacts",
  "Follow-up within 24-72 hours converts contact into care"],
 reqs=["24-hour availability (hotline, mobile team, or on-call)",
  "Written crisis protocols and risk-assessment tools",
  "Partnerships with emergency departments and law enforcement"],
 stds=["SAMHSA crisis-service best-practice guidelines (public)",
  "State crisis-system certification standards"],
 cites=["Substance Abuse and Mental Health Services Administration — crisis services (public)",
  "988 Suicide and Crisis Lifeline — service standards (public)"],
 demo=("outcome", {"label": "Callers connected to follow-up care", "pre": 55, "post": 89})),

dict(title="Child and Family Services", tier=C,
 desc_pub=("Child and family services protect children and strengthen families. The continuum runs "
  "from prevention (parenting programs, home visiting) through in-home services and foster care to "
  "adoption and independent-living support for older youth. Child protective services investigate "
  "abuse and neglect reports, assess safety, and - when children cannot remain safely home - arrange "
  "temporary out-of-home care with a legal mandate to pursue permanency.\n"
  "Modern practice favors keeping families together with intensive supports whenever safety allows, "
  "placing with relatives first when removal is necessary, and moving quickly toward a permanent "
  "home - reunification, guardianship, or adoption - because long foster-care drift harms children."),
 desc_sig=("Signature family-service design centers on a permanency clock: every case carries visible "
  "timelines toward reunification or an alternative permanent plan, with the services needed to meet "
  "each milestone attached - so drift is visible early."),
 how_pub=("A report triggers screening, then investigation with safety assessment. If risk is "
  "manageable, the family gets in-home services and a safety plan. If not, the child is placed - "
  "preferably with kin - while parents receive services aimed at reunification. Courts review "
  "progress on statutory timelines; if reunification fails, the plan shifts to guardianship or "
  "adoption."),
 how_sig=("The Signature permanency dashboard shows every child's timeline status to the whole team, "
  "flagging cases approaching statutory deadlines."),
 keys=["Continuum: prevention, in-home, foster care, adoption, independent living",
  "Safety assessment drives every placement decision",
  "Kinship placement is preferred when removal is necessary",
  "Permanency timelines are set by law",
  "Family preservation with intensive supports is the first choice when safe",
  "Older youth need independent-living preparation"],
 reqs=["Mandated-reporter and investigation protocols",
  "Licensed foster and kinship homes",
  "Court partnership for permanency timelines"],
 stds=["Child Abuse Prevention and Treatment Act requirements (public law)",
  "State child-welfare practice standards"],
 cites=["Children's Bureau, U.S. Dept. of Health and Human Services — child welfare guidance (public)",
  "Child Welfare Information Gateway — practice publications (public)"],
 demo=("caseload", {"cases": [
   {"id": "F-401", "status": "open", "needs": ["parenting support", "housing"]},
   {"id": "F-402", "status": "monitoring", "needs": ["substance use treatment"]},
   {"id": "F-403", "status": "open", "needs": ["kinship placement", "school stability"]},
   {"id": "F-404", "status": "closed", "needs": ["reunification aftercare"]}]})),

dict(title="School-Based Social Work", tier=C,
 desc_pub=("School social workers connect students' home lives with their school success. They "
  "address truancy, behavior problems, trauma, family crises, and special-education needs, working "
  "with teachers, counselors, administrators, and families. A large part of the role is navigating "
  "special-education law: evaluations, Individualized Education Programs (IEPs), and 504 plans for "
  "students whose disabilities affect learning.\n"
  "Services include individual and group counseling, crisis response, home visits, attendance "
  "intervention plans, and linking families to community resources. The measure that matters is "
  "educational: attendance, behavior, and academic progress."),
 desc_sig=("Signature school practice links the student's support plan to live attendance and grade "
  "signals, so interventions trigger on early warning signs instead of waiting for failure."),
 how_pub=("A referral - from a teacher, parent, or the student - starts assessment of barriers to "
  "learning. The worker delivers school-based counseling or groups, coordinates with community "
  "providers, participates in IEP and 504 processes, and conducts home visits when engagement breaks "
  "down. Progress is tracked against attendance and academic goals."),
 how_sig=("Signature early-warning dashboards surface attendance dips and grade drops to the social "
  "worker before they become truancy cases."),
 keys=["Links home life to school success",
  "Navigates special-education law: IEPs and 504 plans",
  "Services: counseling, groups, crisis response, home visits",
  "Attendance intervention is a core function",
  "Works with teachers, families, and community providers",
  "Success is measured in attendance, behavior, academics"],
 reqs=["Knowledge of IDEA and Section 504",
  "Crisis-response capacity during school hours",
  "Family engagement channels"],
 stds=["Individuals with Disabilities Education Act (public law)",
  "School Social Work Association practice standards (public)"],
 cites=["U.S. Dept. of Education — IDEA guidance (public)",
  "School Social Work Association of America — practice model (public)"],
 demo=("outcome", {"label": "Students meeting attendance goals", "pre": 68, "post": 87})),

dict(title="Medical and Hospital Social Work", tier=C,
 desc_pub=("Hospital social workers handle the human side of medical care: discharge planning, "
  "insurance and benefits navigation, counseling for new diagnoses, advance directives, and "
  "connecting patients to home health, rehab, or long-term care. They assess psychosocial barriers - "
  "no ride home, no one to help with medications, unsafe housing - that would undo medical treatment.\n"
  "Discharge planning is the signature task: starting at admission, the worker arranges what the "
  "patient needs after leaving - equipment, home services, follow-up appointments, medication access "
  "- because a discharge to nowhere becomes a readmission."),
 desc_sig=("Signature discharge planning runs a readiness checklist against live bed, transport, and "
  "home-service availability, so discharge dates are set from confirmed arrangements rather than "
  "hope."),
 how_pub=("At admission the worker screens for discharge risks and insurance coverage. During the "
  "stay they counsel, arrange family meetings, and complete advance-directive documents. Before "
  "discharge they confirm the destination, services, equipment, medications, and follow-up visits, "
  "then call after discharge to verify the plan held."),
 how_sig=("Signature post-discharge check-ins are scheduled tasks with outcome logging, feeding "
  "readmission-risk review."),
 keys=["Signature task: discharge planning from admission onward",
  "Addresses psychosocial barriers to medical recovery",
  "Navigates insurance, benefits, and charity care",
  "Advance directives and goals-of-care conversations",
  "Links to home health, rehab, long-term care",
  "Post-discharge follow-up prevents readmissions"],
 reqs=["Access to admission and discharge workflows",
  "Benefits and community-resource knowledge",
  "Authority to order equipment and home services"],
 stds=["Hospital conditions of participation — discharge planning (public regulation)",
  "NASW standards for hospital social work (public)"],
 cites=["Centers for Medicare and Medicaid Services — discharge planning rules (public)",
  "National Association of Social Workers — health practice standards (public)"],
 demo=("referral", {"needs": ["home health", "medical equipment", "transportation"],
   "agencies": [{"name": "Visiting Nurse Service", "serves": ["home health"]},
                {"name": "Medical Equipment Lenders", "serves": ["medical equipment"]},
                {"name": "Medical Ride Program", "serves": ["transportation"]}]})),

dict(title="Substance Use Services Coordination", tier=C,
 desc_pub=("Coordinating substance use services means guiding clients through a continuum: "
  "screening and brief intervention, withdrawal management (detox), residential and outpatient "
  "treatment, medications for opioid and alcohol use disorders, peer recovery support, and "
  "recovery housing. Coordinators match intensity to need, arrange transportation and childcare "
  "that make treatment attendable, and sustain engagement through relapses.\n"
  "The evidence-backed stance is that substance use disorders are chronic health conditions: "
  "relapse is a signal to adjust the plan, not to discharge the client. Coordinators keep the door "
  "open and the plan current."),
 desc_sig=("Signature recovery coordination treats the continuum as a pipeline with stage gates - "
  "screening, engagement, stabilization, maintenance - and tracks each client's stage, so the system "
  "sees where people stall and redesigns those handoffs."),
 how_pub=("Screening identifies severity; the coordinator refers to the right level of care with a "
  "warm handoff, arranges practical supports, and checks in frequently during early treatment. If "
  "the client drops out or relapses, the coordinator re-engages without judgment, adjusts the plan, "
  "and connects to peer and housing supports that sustain recovery."),
 how_sig=("Signature stage tracking alerts the coordinator the moment engagement drops, prompting "
  "outreach before the client is lost."),
 keys=["Continuum: screening, detox, residential, outpatient, medications, peer support, housing",
  "Match intensity to assessed need",
  "Practical supports (rides, childcare) make treatment attendable",
  "Relapse signals plan adjustment, not discharge",
  "Peer recovery coaches improve engagement",
  "Coordination sustains contact across episodes"],
 reqs=["Knowledge of local treatment capacity and waitlists",
  "Confidentiality compliance (42 CFR Part 2)",
  "Peer support partnerships"],
 stds=["SAMHSA treatment improvement protocols (public)",
  "42 CFR Part 2 — substance use confidentiality (public regulation)"],
 cites=["Substance Abuse and Mental Health Services Administration — treatment locators and TIPs (public)"],
 demo=("caseload", {"cases": [
   {"id": "R-501", "status": "open", "needs": ["outpatient treatment", "transportation"]},
   {"id": "R-502", "status": "open", "needs": ["recovery housing", "peer support"]},
   {"id": "R-503", "status": "monitoring", "needs": ["medication management"]}]})),

dict(title="Housing and Homelessness Services", tier=C,
 desc_pub=("Housing services span homelessness prevention (emergency rental aid, mediation), emergency "
  "shelter, transitional housing, rapid re-housing, permanent supportive housing, and Housing Choice "
  "Vouchers. The evidence-backed Housing First model provides stable housing without requiring "
  "sobriety or treatment compliance first - then wraps services around the housed person.\n"
  "Coordinated entry systems assess every homeless household with a standard tool and match them to "
  "the right intervention by vulnerability and need, replacing first-come-first-served chaos with "
  "prioritized placement."),
 desc_sig=("Signature housing coordination runs coordinated entry as a transparent matching engine: "
  "vulnerability scores, available units, and waitlist positions are visible, so placements are "
  "explainable and prioritized by need."),
 how_pub=("Outreach or self-referral leads to a coordinated-entry assessment scoring vulnerability. "
  "The household is matched to prevention aid, shelter, rapid re-housing, or permanent supportive "
  "housing. Case managers help with documents, landlord negotiation, and move-in, then provide "
  "ongoing supports that keep the housing stable."),
 how_sig=("Signature matching recomputes placements as units open, so no vacancy sits while a "
  "matched household waits unnoticed."),
 keys=["Continuum: prevention, shelter, transitional, rapid re-housing, permanent supportive",
  "Housing First: housing before compliance preconditions",
  "Coordinated entry prioritizes by vulnerability",
  "Case management sustains tenancies",
  "Landlord partnerships expand available units",
  "Prevention is cheaper than rehousing"],
 reqs=["Coordinated-entry assessment tool",
  "Landlord and housing-authority partnerships",
  "Document-assistance capacity"],
 stds=["HUD coordinated-entry requirements (public)",
  "Housing First fidelity standards (public literature)"],
 cites=["U.S. Dept. of Housing and Urban Development — coordinated entry (public)",
  "National Alliance to End Homelessness — Housing First research (public)"],
 demo=("priority", {"items": [
   {"need": "Veteran, chronic homelessness, health conditions", "severity": 10, "reach": 6},
   {"need": "Family with children, eviction notice", "severity": 9, "reach": 7},
   {"need": "Youth aging out of foster care", "severity": 8, "reach": 5},
   {"need": "Single adult, recently employed", "severity": 5, "reach": 5}]})),

dict(title="Domestic Violence Support Services", tier=C,
 desc_pub=("Domestic violence services center survivor safety and autonomy: 24-hour hotlines, "
  "emergency shelter, safety planning, legal advocacy (protection orders, custody), counseling, and "
  "transitional housing. Services are voluntary and confidential, with heightened security because "
  "abusers may monitor communications.\n"
  "Safety planning is the core intervention: mapping risks, identifying safe contacts and escape "
  "routes, securing documents and funds, and planning for technology safety. Workers never pressure "
  "survivors to leave; they support informed decisions at the survivor's pace."),
 desc_sig=("Signature survivor-support design adds a safety-by-default layer: communications "
  "protections, confidential location handling, and risk-reassessment at every contact - so the "
  "service system itself never becomes a new vulnerability."),
 how_pub=("Contact - by hotline, walk-in, or referral - triggers immediate safety assessment and "
  "planning. The worker arranges shelter if needed, accompanies the survivor through legal options "
  "without directing the choice, and provides counseling and case management toward stable housing "
  "and independence. Children's safety is assessed in parallel."),
 how_sig=("Signature risk-reassessment prompts at each contact keep safety plans current as "
  "situations change."),
 keys=["Safety and survivor autonomy come first",
  "Services: hotline, shelter, safety planning, legal advocacy, counseling, housing",
  "Heightened confidentiality and technology safety",
  "Workers support decisions; they do not direct them",
  "Children's safety assessed alongside the adult survivor",
  "Culturally specific services reach underserved survivors"],
 reqs=["Secure shelter and hotline capacity",
  "Legal-advocacy partnerships",
  "Trauma-informed, survivor-centered training"],
 stds=["Violence Against Women Act service standards (public law)",
  "State domestic-violence coalition standards"],
 cites=["National Domestic Violence Hotline — service model (public)",
  "National Coalition Against Domestic Violence — resources (public)"],
 demo=("referral", {"needs": ["emergency shelter", "legal advocacy", "counseling"],
   "agencies": [{"name": "Safe Haven Shelter", "serves": ["emergency shelter"]},
                {"name": "Survivor Legal Project", "serves": ["legal advocacy"]},
                {"name": "Trauma Counseling Center", "serves": ["counseling"]}]})),

dict(title="Aging and Disability Service Linkage", tier=C,
 desc_pub=("Linking older adults and people with disabilities to services means navigating aging "
  "and disability resource centers (ADRCs), options counseling, home- and community-based waiver "
  "programs, personal care, home modifications, and caregiver supports. The goal is community living: "
  "the right mix of services that lets people stay in their homes rather than institutions.\n"
  "Options counseling is the signature service: a structured conversation laying out all available "
  "choices - public, private, and informal - so the person decides with full information rather than "
  "discovering options by accident."),
 desc_sig=("Signature options counseling is backed by a complete service catalog with eligibility "
  "pre-screening, so the counselor's conversation starts from the person's actual choices instead of "
  "a generic brochure."),
 how_pub=("A call to the ADRC or a referral triggers options counseling: needs, preferences, finances, "
  "and informal supports are mapped, then matched to programs. The counselor helps apply, arranges "
  "assessments for waiver programs, and follows up to confirm services started. Caregivers are "
  "connected to respite and training in parallel."),
 how_sig=("Signature catalog matching pre-scores every program against the person's profile, making "
  "the counseling session concrete from the first minute."),
 keys=["Goal: community living over institutional placement",
  "ADRCs are the no-wrong-door entry point",
  "Options counseling lays out all choices with full information",
  "Waiver programs fund home- and community-based services",
  "Caregiver supports are part of the plan",
  "Person-centered: preferences drive the mix"],
 reqs=["ADRC or equivalent single-entry partnership",
  "Current catalog of aging/disability programs",
  "Waiver-program assessment capacity"],
 stds=["Older Americans Act service standards (public law)",
  "State waiver program requirements"],
 cites=["Administration for Community Living — ADRC guidance (public)",
  "National Council on Aging — benefits resources (public)"],
 demo=("eligibility", {"needs": ["personal care", "home modifications", "respite care"],
   "criteria": [{"program": "HCBS Waiver", "covers": ["personal care", "respite care"]},
                {"program": "Home Modification Grant", "covers": ["home modifications"]},
                {"program": "Senior Center", "covers": ["meals", "socialization"]}]})),

dict(title="Program Outcome Measurement", tier=C,
 desc_pub=("Outcome measurement asks whether services actually changed lives: are clients housed, "
  "employed, stable, safe? Outputs count activities (bed-nights, counseling hours); outcomes measure "
  "results (housing retention at 12 months, employment at 90 days). Funders increasingly pay for "
  "outcomes, not just outputs.\n"
  "Good measurement starts with a logic model - inputs, activities, outputs, outcomes - then picks a "
  "few valid indicators per outcome, collects baseline and follow-up data, and reports honestly, "
  "including what did not work. Comparison groups or pre-post designs separate program effects from "
  "background change."),
 desc_sig=("Signature outcome measurement standardizes indicators across programs - housing "
  "retention, income change, stability scores - so different services' results can be compared and "
  "the whole system's impact summed, not just reported program by program."),
 how_pub=("Planners draft the logic model with stakeholders, select indicators and data sources, and "
  "build collection into service workflows so measurement is not extra work. Baselines are captured "
  "at intake; follow-ups at set intervals. Results are analyzed, reported to funders and the "
  "community, and fed back into program redesign."),
 how_sig=("Signature indicator libraries let new programs adopt proven measures in days instead of "
  "inventing their own."),
 keys=["Outcomes measure life changes; outputs count activities",
  "Logic models link inputs to outcomes",
  "Baselines at intake, follow-ups at intervals",
  "A few valid indicators beat dozens of weak ones",
  "Report failures honestly - they drive improvement",
  "Funders increasingly tie payment to outcomes"],
 reqs=["A logic model per program",
  "Baseline and follow-up data collection in workflows",
  "Analysis and reporting capacity"],
 stds=["Funder performance-measure requirements",
  "Evaluation methodology standards (public literature)"],
 cites=["Urban Institute — outcome measurement guidance (public)",
  "Annie E. Casey Foundation — evaluation resources (public)"],
 demo=("outcome", {"label": "Households stably housed at 12 months", "pre": 58, "post": 81})),

# ---------------- Advanced (11) ----------------
dict(title="Systems Navigation for Complex Cases", tier=A,
 desc_pub=("Some clients touch a dozen systems at once - child welfare, criminal justice, health, "
  "housing, benefits - with conflicting requirements and timelines. Systems navigation is intensive "
  "case management for these cases: mapping every involved system, sequencing requirements, "
  "attending hearings and appointments alongside the client, and resolving inter-system conflicts.\n"
  "Navigators need authority to convene: the ability to call a meeting of everyone involved and get "
  "decisions. Without that authority, navigation is just advice. Successful programs give navigators "
  "small caseloads, flexible funds for emergencies, and direct lines to decision-makers."),
 desc_sig=("Signature complex-case navigation uses a system map per client - every agency, deadline, "
  "and dependency on one visual - with conflict detection that flags incompatible requirements "
  "before the client fails one of them."),
 how_pub=("The navigator inventories every system touching the client, builds a master timeline of "
  "requirements and deadlines, and identifies conflicts (a court date vs. a treatment intake). They "
  "convene the parties, negotiate sequencing, accompany the client to critical appointments, and use "
  "flexible funds to remove small barriers that would cascade into big failures."),
 how_sig=("The Signature system map recomputes the critical path whenever a date moves, keeping the "
  "whole team on the current plan."),
 keys=["For clients touching many systems simultaneously",
  "Map every system, requirement, and deadline",
  "Navigators need convening authority, not just advice",
  "Small caseloads and flexible emergency funds",
  "Resolve inter-system conflicts proactively",
  "Accompany clients to the appointments that matter most"],
 reqs=["Inter-agency agreements granting convening authority",
  "Flexible emergency assistance funds",
  "Master-timeline tracking tools"],
 stds=["Wraparound and systems-of-care fidelity standards (public)",
  "Funder requirements for intensive models"],
 cites=["National Wraparound Initiative — model standards (public)",
  "Substance Abuse and Mental Health Services Administration — systems of care (public)"],
 demo=("caseload", {"cases": [
   {"id": "Z-601", "status": "open", "needs": ["court compliance", "treatment", "housing", "benefits"]},
   {"id": "Z-602", "status": "open", "needs": ["child welfare plan", "employment", "childcare"]}]})),

dict(title="Wraparound Service Models", tier=A,
 desc_pub=("Wraparound is a team-based planning process for youth with complex needs and their "
  "families. A facilitator convenes the family, natural supports (relatives, mentors, coaches), and "
  "professionals into one team that builds a single plan driven by family voice and choice. Plans "
  "blend formal services with natural supports and are reviewed frequently.\n"
  "The ten principles - family voice, team-based, natural supports, collaboration, community-based, "
  "culturally competent, individualized, strengths-based, persistent, outcomes-based - distinguish "
  "real wraparound from merely holding meetings. Fidelity to the model predicts results."),
 desc_sig=("Signature wraparound operations run on a fidelity dashboard: each principle has observable "
  "indicators scored per team, so programs know whether they are doing wraparound or just meeting "
  "about youth."),
 how_pub=("The facilitator engages the family, maps strengths and needs across life domains, and "
  "convenes the team. The team brainstorms strategies mixing services and natural supports, assigns "
  "tasks, and meets regularly to review progress. When outcomes stall, the team redesigns rather "
  "than blaming the family. Transition planning starts early so gains survive the program's end."),
 how_sig=("Signature plan workspaces give every team member - including natural supports - the same "
  "live plan with their tasks visible."),
 keys=["Team: family, natural supports, professionals",
  "Family voice and choice drive the plan",
  "Blends formal services with natural supports",
  "Ten principles define fidelity",
  "Frequent review and redesign, not blame",
  "Transition planning protects gains"],
 reqs=["Trained facilitators with small caseloads",
  "Fidelity measurement tools",
  "Flexible funds for individualized strategies"],
 stds=["National Wraparound Initiative — fidelity standards (public)",
  "State wraparound program requirements"],
 cites=["National Wraparound Initiative — model description (public)"],
 demo=("outcome", {"label": "Youth remaining in home/community setting", "pre": 64, "post": 88})),

dict(title="Interagency Data Sharing and Privacy", tier=A,
 desc_pub=("Coordinated care requires sharing client data across agencies - and privacy law requires "
  "protecting it. The solution is governed sharing: data-sharing agreements defining what is shared, "
  "with whom, for what purpose, under what consent, with audit trails and breach procedures. "
  "Frameworks like HIPAA, 42 CFR Part 2, FERPA, and state laws each set different rules for health, "
  "substance use, education, and child welfare data.\n"
  "Best practice is minimum-necessary sharing with role-based access: each worker sees only what "
  "their role needs. Clients are told in plain language what is shared and can often opt out of "
  "non-required sharing."),
 desc_sig=("Signature governed sharing implements consent as executable policy: data requests are "
  "checked against consent records and role permissions automatically, with every access logged - "
  "privacy enforced by architecture, not just by training."),
 how_pub=("Agencies negotiate a data-sharing agreement with legal review, map which data elements "
  "each partner may see, and implement consent workflows at intake. Technical controls enforce "
  "role-based access; audits review who looked at what. Breach procedures and client notification "
  "plans are agreed before the first record moves."),
 how_sig=("Signature consent records travel with the data, so downstream systems inherit the same "
  "restrictions automatically."),
 keys=["Governed sharing: agreements, consent, audit trails",
  "Different laws govern health, substance use, education, child welfare data",
  "Minimum-necessary and role-based access",
  "Clients get plain-language explanations and opt-out choices",
  "Breach procedures agreed in advance",
  "Audit who accessed what, regularly"],
 reqs=["Legally reviewed data-sharing agreements",
  "Consent workflows at intake",
  "Role-based technical access controls"],
 stds=["HIPAA, 42 CFR Part 2, FERPA (public laws)",
  "State inter-agency sharing statutes"],
 cites=["U.S. Dept. of Health and Human Services — HIPAA guidance (public)",
  "U.S. Dept. of Education — FERPA guidance (public)"],
 demo=("referral", {"needs": ["data sharing consent"],
   "agencies": [{"name": "Privacy Office (governed-sharing desk)", "serves": ["data sharing consent"]}]})),

dict(title="Grant-Funded Program Design", tier=A,
 desc_pub=("Most social service programs live on grants, and grant design is a discipline: needs "
  "statement with data, measurable objectives, evidence-based methods, a staffing and management "
  "plan, an evaluation plan, a budget that ties dollars to activities, and sustainability planning "
  "for when the grant ends. Reviewers score clarity, evidence, feasibility, and fit with the "
  "funder's priorities.\n"
  "Strong proposals start from the community needs assessment, choose interventions with research "
  "support, and set objectives that are specific, measurable, and time-bound. Budgets must be "
  "auditable; every line traces to an activity in the narrative."),
 desc_sig=("Signature grant design maintains a library of evidence-rated interventions, logic models, "
  "and budget templates, so new proposals assemble from proven components instead of starting blank - "
  "while every claim remains tied to its source data."),
 how_pub=("Planners review the funder's priorities and requirements, pull needs data, and select "
  "evidence-based interventions. They draft objectives, staffing, timelines, and evaluation, then "
  "build the budget line by line from the narrative. After internal review, the proposal is "
  "submitted; if funded, the evaluation plan activates immediately."),
 how_sig=("Signature proposal assembly links each narrative claim to its data source, making "
  "reviewer verification trivial."),
 keys=["Needs data, measurable objectives, evidence-based methods",
  "Objectives: specific, measurable, time-bound",
  "Budget lines trace to narrative activities",
  "Evaluation plan activates at award, not at report time",
  "Sustainability planning for post-grant life",
  "Fit with funder priorities decides competitiveness"],
 reqs=["Community needs data",
  "Evidence base for chosen interventions",
  "Financial systems that support auditable budgets"],
 stds=["Federal grant regulations (Uniform Guidance, public)",
  "Funder-specific application requirements"],
 cites=["Grants.gov — federal grant guidance (public)",
  "U.S. Office of Management and Budget — Uniform Guidance (public)"],
 demo=("outcome", {"label": "Grant objectives met on time", "pre": 70, "post": 92})),

dict(title="Evaluating Service Equity", tier=A,
 desc_pub=("Equity evaluation asks whether services reach and help all groups fairly - by race, "
  "language, disability, geography, and income. It disaggregates access, service, and outcome data, "
  "tests for disparities, investigates root causes (eligibility rules, locations, hours, language "
  "access, bias), and redesigns accordingly.\n"
  "The discipline requires looking beyond averages: a program with good overall outcomes can still "
  "fail specific communities. Community members participate in interpreting findings - they know "
  "context the data lacks - and in designing fixes."),
 desc_sig=("Signature equity evaluation runs disparity screens continuously on live service data, so "
  "inequities surface in weeks rather than in the next five-year study - with community review built "
  "into every finding before action."),
 how_pub=("Analysts disaggregate data by demographic and geographic groups, compute disparity ratios "
  "on access and outcomes, and investigate causes through record review and community input. "
  "Findings go to a community review panel; redesigns target the causes (new sites, extended hours, "
  "translated materials, rule changes). Re-measurement confirms the gap closed."),
 how_sig=("Signature disparity dashboards update with each data refresh, keeping equity visible "
  "between formal evaluations."),
 keys=["Disaggregate by race, language, disability, geography, income",
  "Averages can hide group-level failure",
  "Investigate root causes, not just gaps",
  "Community members interpret findings and design fixes",
  "Redesign targets causes: access, rules, language, bias",
  "Re-measure to confirm gaps closed"],
 reqs=["Demographic and geographic data capture",
  "Community review partnerships",
  "Authority to change rules and operations"],
 stds=["Funder equity-reporting requirements",
  "Evaluation standards for culturally responsive practice (public literature)"],
 cites=["Annie E. Casey Foundation — race equity evaluation (public)",
  "Urban Institute — equity measurement (public)"],
 demo=("outcome", {"label": "Service access parity index", "pre": 72, "post": 95})),

dict(title="Policy Advocacy and Community Organizing", tier=A,
 desc_pub=("When individual cases reveal systemic barriers, social workers move upstream: policy "
  "advocacy and community organizing. Advocacy includes documenting the problem, building coalitions, "
  "drafting policy proposals, testifying, and mobilizing constituents. Organizing builds resident "
  "power - leadership development, campaigns with winnable demands, and accountability actions.\n"
  "Effective efforts pair stories with data: one family's eviction story plus the statistic that "
  "thousands face the same. Nonprofits must respect lobbying limits tied to their tax status while "
  "unlimited non-lobbying advocacy (education, organizing) remains available."),
 desc_sig=("Signature advocacy infrastructure maintains living issue briefs - problem data, affected "
  "populations, policy options, coalition maps - so campaigns launch from current intelligence "
  "instead of rebuilding research each time."),
 how_pub=("Organizers listen to residents, identify shared issues, and develop leaders. The coalition "
  "researches the problem and decision-makers, sets demands, and runs a campaign: meetings, "
  "testimony, media, voter engagement. Wins are implemented and monitored; losses become the next "
  "campaign's foundation."),
 how_sig=("Signature issue briefs keep the evidence base current across campaigns, compounding "
  "organizational knowledge."),
 keys=["Move upstream from cases to systems",
  "Pair stories with data",
  "Organizing builds resident power and leadership",
  "Campaigns need winnable demands and decision-maker targets",
  "Respect nonprofit lobbying limits",
  "Monitor implementation after the win"],
 reqs=["Constituent base and leadership pipeline",
  "Research capacity for problem and policy analysis",
  "Coalition partnerships"],
 stds=["IRS lobbying rules for nonprofits (public)",
  "NASW policy-advocacy guidance (public)"],
 cites=["National Association of Social Workers — advocacy resources (public)",
  "Internal Revenue Service — lobbying limits guidance (public)"],
 demo=("priority", {"items": [
   {"need": "Eviction defense funding", "severity": 9, "reach": 8},
   {"need": "Bus route restoration", "severity": 7, "reach": 7},
   {"need": "Park renovation", "severity": 5, "reach": 6}]})),

dict(title="Supervision and Workforce Development", tier=A,
 desc_pub=("Clinical and administrative supervision is how agencies protect clients and grow workers. "
  "Good supervision blends case review, skills coaching, ethical guidance, and emotional support - "
  "especially in trauma-exposed roles where burnout and secondary traumatic stress are occupational "
  "hazards. Workforce development adds training pipelines, career ladders, and retention strategies.\n"
  "The workforce crisis is real: turnover in child welfare and community mental health routinely "
  "exceeds 30 percent annually. Agencies that retain staff invest in manageable caseloads, reflective "
  "supervision, competitive pay, and clear advancement."),
 desc_sig=("Signature workforce systems track supervision quality, caseload health, and early "
  "burnout signals across the agency, letting leaders intervene with support before resignation "
  "letters - treating retention as a measurable system output."),
 how_pub=("Supervisors meet workers regularly for case review and coaching, observe practice, and "
  "guide ethical dilemmas. Agencies run onboarding academies, ongoing training tied to practice "
  "models, and peer support structures. Workforce data - turnover, vacancy, time-to-fill - is "
  "reviewed quarterly with retention plans."),
 how_sig=("Signature caseload-health dashboards flag overload patterns early, prompting rebalancing "
  "before quality or retention suffers."),
 keys=["Supervision: case review, coaching, ethics, emotional support",
  "Burnout and secondary traumatic stress are occupational hazards",
  "Turnover above 30 percent is common in high-stress fields",
  "Retention levers: caseloads, pay, supervision quality, advancement",
  "Training must tie to the agency's practice model",
  "Workforce data reviewed quarterly"],
 reqs=["Qualified supervisors with protected supervision time",
  "Training tied to practice models",
  "Workforce metrics and retention plans"],
 stds=["NASW supervision standards (public)",
  "State supervision requirements for licensure"],
 cites=["National Association of Social Workers — supervision standards (public)",
  "Annie E. Casey Foundation — child welfare workforce research (public)"],
 demo=("outcome", {"label": "Annual staff retention rate", "pre": 68, "post": 86})),

dict(title="Trauma-Informed Service Systems", tier=A,
 desc_pub=("Trauma-informed systems recognize that most clients - and many staff - carry trauma "
  "histories, and they redesign every interaction accordingly. The principles: safety, "
  "trustworthiness, peer support, collaboration, empowerment, and cultural humility. In practice "
  "this means calm welcoming spaces, transparent processes, client choice wherever possible, and "
  "staff trained to avoid re-traumatization.\n"
  "Becoming trauma-informed is organizational change, not a training day: policies, physical "
  "environments, hiring, and supervision all shift. Measurement tracks both client experience and "
  "staff well-being."),
 desc_sig=("Signature trauma-informed design audits every client touchpoint - intake, waiting, "
  "interview, referral - against the six principles, producing a remediation backlog that turns "
  "philosophy into facility and workflow changes."),
 how_pub=("Leadership commits and assesses current state with staff and client input. Work teams "
  "redesign spaces, forms, and workflows around the principles; all staff receive foundational "
  "training plus role-specific coaching. Policies are rewritten, supervision addresses secondary "
  "trauma, and client-experience measures track the change."),
 how_sig=("Signature touchpoint audits make the abstract concrete: each interaction gets a "
  "principle-by-principle score and a fix list."),
 keys=["Six principles: safety, trustworthiness, peer support, collaboration, empowerment, cultural humility",
  "Most clients carry trauma histories - design for it",
  "Avoid re-traumatization in every process",
  "Organizational change, not a single training",
  "Staff secondary trauma addressed in supervision",
  "Measure client experience and staff well-being"],
 reqs=["Leadership commitment and assessment",
  "All-staff foundational training",
  "Policy and environment redesign authority"],
 stds=["SAMHSA trauma-informed care principles (public)",
  "State trauma-informed certification standards where they exist"],
 cites=["Substance Abuse and Mental Health Services Administration — trauma-informed approach (public)",
  "National Child Traumatic Stress Network — resources (public)"],
 demo=("outcome", {"label": "Client-reported sense of safety", "pre": 71, "post": 93})),

dict(title="Rural Service Delivery Models", tier=A,
 desc_pub=("Rural communities face provider shortages, long distances, limited broadband, and thin "
  "agency infrastructure - while needs match or exceed urban levels. Effective rural models include "
  "mobile units, telehealth, itinerant workers covering multi-county circuits, co-located services "
  "in schools and clinics, and strong informal networks through faith and civic groups.\n"
  "Transportation is often the binding constraint: services clients cannot reach might as well not "
  "exist. Successful programs budget for mileage, volunteer driver networks, and services that "
  "travel to clients rather than requiring the reverse."),
 desc_sig=("Signature rural design optimizes circuit routes, mobile-unit schedules, and telehealth "
  "slots against population maps, so scarce worker hours cover the most need-miles per week."),
 how_pub=("Planners map needs against provider locations and transport options, then choose the mix: "
  "which services go mobile, which go virtual, which anchor at co-located sites. Circuits are "
  "scheduled reliably so residents can plan; telehealth fills gaps where broadband allows; "
  "transportation assistance closes the last mile."),
 how_sig=("Signature coverage optimization recomputes circuits as demand shifts, keeping reach "
  "maximal within fixed staff hours."),
 keys=["Barriers: shortages, distance, broadband gaps, thin infrastructure",
  "Models: mobile units, telehealth, circuits, co-location",
  "Transportation is often the binding constraint",
  "Services should travel to clients where possible",
  "Informal networks amplify formal services",
  "Reliable schedules let residents plan"],
 reqs=["Transportation budget and driver networks",
  "Telehealth-capable connectivity",
  "Multi-county coordination agreements"],
 stds=["Federal rural-health program requirements (public)",
  "Telehealth practice standards (public)"],
 cites=["Federal Office of Rural Health Policy — resources (public)",
  "Rural Health Information Hub — service models (public)"],
 demo=("referral", {"needs": ["counseling", "transportation"],
   "agencies": [{"name": "Mobile Counseling Unit (circuit)", "serves": ["counseling"]},
                {"name": "Volunteer Driver Network", "serves": ["transportation"]}]})),

dict(title="Disaster Response Social Services", tier=A,
 desc_pub=("After disasters, social services handle what emergency response does not: crisis "
  "counseling, disaster case management, benefits for the displaced, unmet-needs coordination, and "
  "long-term recovery support. FEMA's crisis counseling and disaster case management programs fund "
  "much of this work; voluntary organizations (VOAD members) deliver much of the rest.\n"
  "The sequence is response then recovery: immediate safety and stabilization, then months of case "
  "management helping households navigate insurance, FEMA aid, SBA loans, and rebuilding. Unmet-needs "
  "committees match remaining gaps to donated resources."),
 desc_sig=("Signature disaster social-service design pre-builds the recovery playbook - agency roles, "
  "data-sharing agreements, unmet-needs workflows - so coordination starts on day one instead of "
  "being invented mid-crisis."),
 how_pub=("Agencies activate emergency plans, stand up hotlines and mobile teams, and begin crisis "
  "counseling. As response stabilizes, disaster case managers take households through recovery "
  "planning: documenting losses, applying for aid, appealing denials, and sequencing rebuilding "
  "funds. Long-term recovery groups coordinate donated resources for unmet needs."),
 how_sig=("Signature pre-signed data agreements let case managers see across agencies from the first "
  "week, instead of negotiating sharing during the crisis."),
 keys=["Crisis counseling, disaster case management, unmet-needs coordination",
  "FEMA funds much of the work; voluntary agencies deliver much of it",
  "Response is weeks; recovery is months to years",
  "Case managers navigate insurance, FEMA, SBA, rebuilding funds",
  "Unmet-needs committees match gaps to donations",
  "Pre-built playbooks beat invented-mid-crisis coordination"],
 reqs=["Emergency operations plans with social-service roles",
  "Pre-negotiated data-sharing agreements",
  "Long-term recovery group partnerships"],
 stds=["FEMA crisis counseling and case management program rules (public)",
  "National VOAD coordination standards (public)"],
 cites=["Federal Emergency Management Agency — disaster assistance guidance (public)",
  "National Voluntary Organizations Active in Disaster — standards (public)"],
 demo=("caseload", {"cases": [
   {"id": "D-701", "status": "open", "needs": ["temporary housing", "FEMA aid"]},
   {"id": "D-702", "status": "open", "needs": ["crisis counseling", "document replacement"]},
   {"id": "D-703", "status": "monitoring", "needs": ["rebuilding funds"]}]})),

dict(title="The Future of Coordinated Care", tier=A,
 desc_pub=("Coordinated care is moving toward predictive, person-driven, and platform-based models. "
  "Predictive analytics flag clients at risk of homelessness, hospitalization, or child-welfare "
  "involvement before crisis - enabling prevention. Person-driven planning gives clients digital "
  "access to their own plans, providers, and records. Platform models let any authorized provider "
  "join a client's team with shared tools.\n"
  "The through-line is integration without consolidation: many independent agencies acting as one "
  "team through shared plans, governed data, and outcome accountability - preserving community "
  "roots while ending fragmentation."),
 desc_sig=("The Signature future-state is a coordination operating system for human services: one "
  "consent layer, one plan ledger, one outcome spine - on which every agency, worker, and client "
  "collaborates. This database's Signature edition is a prototype of that operating system's "
  "knowledge core."),
 how_pub=("Systems adopt shared assessment and planning tools, negotiate governed data sharing, and "
  "stand up coordination platforms. Predictive models are validated for fairness before deployment. "
  "Clients get portal access to their plans. Payment shifts toward outcomes, rewarding coordination "
  "that keeps people stable."),
 how_sig=("Signature's operating-system vision makes today's advanced practices - shared plans, "
  "governed sharing, outcome accountability - the default infrastructure for every community."),
 keys=["Predictive analytics enable prevention before crisis",
  "Person-driven: clients access their own plans and records",
  "Platforms let any authorized provider join the team",
  "Integration without consolidation preserves community roots",
  "Payment shifts toward outcomes",
  "Fairness validation precedes predictive deployment"],
 reqs=["Validated, fairness-checked predictive models",
  "Client-facing plan portals",
  "Outcome-based payment arrangements"],
 stds=["Emerging standards for ethical predictive analytics in human services (public literature)"],
 cites=["Chapin Hall — predictive analytics in human services (public)",
  "Urban Institute — integrated data systems (public)"],
 demo=("outcome", {"label": "Clients with a single shared care plan", "pre": 38, "post": 84})),
]
