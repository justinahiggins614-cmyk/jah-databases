#!/usr/bin/env python3
"""Topics + config for the mental-health-services pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never medical advice, no dosages, no cure claims.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "mental-health-services",
    "name_pub": "The Mental Health Services Database",
    "name_sig": "Signature Mental Health Services Database",
    "tagline_pub": ("Mental health services from the ground up: levels of care, how to access help, "
                    "evidence-based care approaches, crisis services, community programs, and how "
                    "treatment outcomes are measured - every record carrying the full entry taught "
                    "progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of mental health services: the same "
                    "real service knowledge carried forward, plus Signature-built care-pathway models, "
                    "access designs, and outcome frameworks original to this system."),
    "record_kind": "mental health service record",
    "record_kind_plural": "mental health service records",
    "prefix_pub": "JAH-MHS-", "prefix_sig": "JAH-MHSS-",
    "ai_pub": "JAH Mental Health Services Archivist",
    "ai_sig": "JAH Signature Mental Health Services Creator",
    "role_pub": ("mental health services archivist - teaching levels of care, access pathways, "
                 "evidence-based approaches, crisis services, and outcome measurement; answers from "
                 "many angles - definition, example, process, access, outcomes - using only archive "
                 "data from this system"),
    "role_sig": ("Signature creator of mental health service systems - designing care pathways, "
                 "access models, and outcome frameworks as original Signature works; answers from "
                 "many angles using only archive data from this system"),
    "search_ph": "Search levels of care, therapies, crisis services, access, outcomes...",
    "chat_ph": "Ask about mental health services...",
    "greet_pub": ("I am the JAH Mental Health Services Archivist. Ask me about levels of care, "
                  "accessing help, evidence-based approaches, crisis services, and outcomes. "
                  "I share educational information, not medical advice."),
    "greet_sig": ("I am the JAH Signature Mental Health Services Creator. Ask me about "
                  "Signature-built care pathways and service designs. Educational information only."),
    "gen_blurb": ("Generate clearly-labeled mental health service studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded mental health service records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. "
                      "Educational information only — not medical advice."),
    "demo_kind": "mental-health-demo",
    "demo_title": "Mental Health Services Demo",
    "health": True,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Mental Health Services Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "pathway":
        return fill(
            "steps = @@STEPS@@\n"
            "print('Care pathway:')\n"
            "for i, s in enumerate(steps, 1):\n"
            "    print(' Step %d: %s' % (i, s))\n"
            "print('Total steps:', len(steps))\n", {"STEPS": p["steps"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d' % (pre, post, delta))\n"
            "print('Direction:', 'improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged')\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    if v == "screen":
        return fill(
            "items = @@ITEMS@@\n"
            "total = sum(items)\n"
            "band = 'low' if total <= 4 else 'moderate' if total <= 9 else 'high'\n"
            "print('Screening items:', len(items))\n"
            "print('Total score:', total, '->', band, 'range')\n"
            "print('Note: screening is not diagnosis; follow up with a professional.')\n",
            {"ITEMS": p["items"]})
    if v == "match":
        return fill(
            "need = @@NEED@@\nlevels = @@LEVELS@@\n"
            "print('Presenting need:', need)\n"
            "for lv in levels:\n"
            "    mark = '>>' if need in lv['fits'] else '  '\n"
            "    print('%s %s: %s' % (mark, lv['level'], lv['example']))\n",
            {"NEED": p["need"], "LEVELS": p["levels"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Mental Health Services Are", tier=F,
 desc_pub=("Mental health services are organized supports that help people understand, manage, and "
  "recover from mental health challenges. They include counseling and psychotherapy, psychiatric "
  "evaluation and medication management, crisis services, peer support, case management, and "
  "community programs. Services are delivered in clinics, hospitals, schools, workplaces, homes, "
  "and by phone or video.\n"
  "The field rests on a recovery orientation: the goal is a full, meaningful life as defined by the "
  "person, not merely the absence of symptoms. Services are voluntary in most settings, confidential "
  "within legal limits, and increasingly built around the person's own goals and preferences."),
 desc_sig=("The Signature system models mental health services as pathways with defined stages - "
  "access, engagement, active care, maintenance - each with entry criteria, expected activities, and "
  "exit measures. This pathway framing lets services be designed and compared as journeys rather "
  "than isolated appointments."),
 how_pub=("A person reaches out - directly, through a referral, or via a crisis line - and completes "
  "an intake with screening and assessment. Together with a clinician they set goals and choose "
  "services: therapy, medication evaluation, peer support, or a combination. Progress is reviewed "
  "regularly with standardized measures, and the plan adjusts until goals are met."),
 how_sig=("Signature pathway tracking attaches stage markers to every case, so both client and team "
  "can see where they are in the journey and what comes next."),
 keys=["Include therapy, psychiatric care, crisis services, peer support, case management",
  "Delivered in clinics, hospitals, schools, workplaces, homes, and remotely",
  "Recovery orientation: a full meaningful life as the person defines it",
  "Most services are voluntary and confidential within legal limits",
  "Care is built around the person's own goals",
  "Progress reviewed with standardized measures"],
 reqs=["Licensed or credentialed clinical staff",
  "Confidential intake, assessment, and record systems",
  "Crisis-response capacity or partnership"],
 stds=["SAMHSA recovery-oriented practice guidance (public)",
  "State licensing laws for mental health professionals"],
 cites=["Substance Abuse and Mental Health Services Administration — recovery resources (public)",
  "National Institute of Mental Health — public information (public)"],
 demo=("pathway", {"steps": ["Reach out or referral", "Intake and screening",
   "Assessment and goal setting", "Active care (therapy, supports)",
   "Progress review", "Maintenance and closure"]})),

dict(title="Levels of Care in Mental Health", tier=F,
 desc_pub=("Levels of care describe how intensive services are, from least to most: self-help and "
  "peer support, outpatient counseling (weekly sessions), intensive outpatient programs (several "
  "hours, several days a week), partial hospitalization (daytime treatment, home at night), "
  "residential treatment, and inpatient hospitalization for acute crises.\n"
  "Matching intensity to need is the central skill: too little care leaves people unsafe, too much "
  "disrupts life unnecessarily. People commonly step up to more intensive care during crises and "
  "step down as they stabilize - movement between levels should be smooth, not a cliff."),
 desc_sig=("The Signature system treats levels of care as a step-care ladder with explicit "
  "step-up and step-down criteria, so transitions are planned events with handoffs rather than "
  "abrupt discharges."),
 how_pub=("Assessment determines severity, safety, functioning, and supports. The clinician "
  "recommends the least intensive level likely to be safe and effective, explains the options, and "
  "the client chooses. Regular re-assessment moves people between levels; crisis plans name what "
  "triggers a step up."),
 how_sig=("Signature step criteria are written into every care plan, so everyone knows in advance "
  "what would prompt more or less intensive care."),
 keys=["Least to most intensive: self-help, outpatient, intensive outpatient, partial, residential, inpatient",
  "Match intensity to assessed need",
  "Step up in crisis, step down with stability",
  "Transitions should be smooth handoffs",
  "Least intensive safe option is preferred",
  "Re-assessment drives movement between levels"],
 reqs=["Assessment tools that rate severity and safety",
  "Access to each level (directly or by referral)",
  "Transition and handoff protocols"],
 stds=["Level-of-care placement criteria (public clinical literature)",
  "Accreditation standards for each program type"],
 cites=["Substance Abuse and Mental Health Services Administration — levels of care (public)",
  "American Psychiatric Association — public resources (public)"],
 demo=("match", {"need": "weekly support while working full-time",
   "levels": [{"level": "Outpatient counseling", "fits": ["weekly support while working full-time"], "example": "weekly 50-minute sessions"},
              {"level": "Intensive outpatient", "fits": [], "example": "9+ hours/week"},
              {"level": "Inpatient", "fits": [], "example": "24-hour hospital care"}]})),

dict(title="Accessing Care: First Steps", tier=F,
 desc_pub=("The first steps into care are often the hardest: recognizing a need, finding a provider, "
  "affording it, and making the call. Common entry points include primary-care doctors (who can "
  "screen and refer), community mental health centers, school counselors, employee assistance "
  "programs, crisis lines, and insurer provider directories.\n"
  "Practical barriers - cost, waitlists, transportation, language, stigma - are real and widely "
  "shared. Naming them helps: many clinics offer sliding-scale fees, telehealth removes distance, "
  "and peer specialists can accompany a nervous first-timer through intake."),
 desc_sig=("Signature access design treats the first contact as a product to be engineered: one "
  "number, plain-language triage, same-week options, and barrier screening at hello - so the "
  "hardest step gets the most design attention."),
 how_pub=("The person (or someone helping them) identifies what kind of help fits - counseling, "
  "crisis support, peer support - then contacts an entry point. Intake gathers history and needs; "
  "screening tools clarify severity. The clinic proposes options with costs and waits explained, "
  "and the person chooses. A follow-up call after the first visit cements engagement."),
 how_sig=("Signature barrier screening at first contact asks about cost, transport, language, and "
  "schedule - solving logistics before they become dropouts."),
 keys=["Entry points: primary care, community centers, schools, EAPs, crisis lines, directories",
  "Common barriers: cost, waits, transport, language, stigma",
  "Sliding-scale fees and telehealth widen access",
  "Peer specialists can bridge the first visit",
  "Costs and waits should be explained up front",
  "Follow-up after visit one cements engagement"],
 reqs=["Multiple advertised entry points",
  "Plain-language information on cost and waits",
  "Barrier screening at first contact"],
 stds=["SAMHSA access standards for community programs (public)",
  "Parity requirements for insurance coverage (public law)"],
 cites=["Substance Abuse and Mental Health Services Administration — find treatment resources (public)",
  "U.S. Dept. of Labor — mental health parity guidance (public)"],
 demo=("pathway", {"steps": ["Recognize the need", "Pick an entry point",
   "Complete intake and screening", "Review options and costs", "Begin care", "Follow-up check-in"]})),

dict(title="Screening and Assessment Tools", tier=F,
 desc_pub=("Screening tools are brief questionnaires that flag possible concerns; assessment goes "
  "deeper to characterize them. Widely used screens include the PHQ-9 for depression, GAD-7 for "
  "anxiety, and the Columbia protocol for suicide risk - each a short set of scored items with "
  "validated cutoffs.\n"
  "Screens are not diagnoses: a high score means 'assess further,' not 'you have this disorder.' "
  "Used well, they standardize detection, track change over time, and give clients concrete numbers "
  "for progress. Used badly - as labels - they harm."),
 desc_sig=("The Signature measurement system pairs every screen with a plain-language interpretation "
  "guide and a re-screen schedule, so scores become a shared progress language between client and "
  "clinician rather than a one-time label."),
 how_pub=("The client completes the questionnaire at intake and at intervals during care. The "
  "clinician scores it, discusses what the score means and does not mean, and uses change over time "
  "to judge whether the plan is working. Scores live in the record alongside the client's own words."),
 how_sig=("Signature re-screen scheduling is automatic - the system prompts at clinically sensible "
  "intervals and charts the trend for both parties to see."),
 keys=["Screens flag concerns; assessment characterizes them",
  "PHQ-9, GAD-7, Columbia protocol are widely used public tools",
  "A high score means assess further, not a diagnosis",
  "Track change over time to judge progress",
  "Scores complement the client's own words",
  "Never use a screen as a label"],
 reqs=["Validated instruments appropriate to the population",
  "Staff trained in administration and interpretation",
  "Re-screening schedule in the care plan"],
 stds=["Instrument publishers' administration guidelines (public)",
  "Clinical guidelines on measurement-based care (public literature)"],
 cites=["National Institute of Mental Health — screening information (public)",
  "Agency for Healthcare Research and Quality — measurement-based care (public)"],
 demo=("screen", {"items": [1, 2, 0, 3, 1, 2, 1, 0, 2]})),

dict(title="Evidence-Based Psychotherapies", tier=F,
 desc_pub=("Evidence-based psychotherapies are talk therapies tested in research and shown to help "
  "specific problems. The best-known include cognitive behavioral therapy (CBT), which targets the "
  "links between thoughts, feelings, and behaviors; interpersonal therapy, focused on relationships "
  "and role changes; and behavioral activation, which rebuilds engagement in rewarding activities.\n"
  "What they share: a clear rationale, structured sessions, skills the client practices between "
  "sessions, and measurement of progress. 'Evidence-based' does not mean one-size-fits-all - "
  "therapists adapt the approach to the person's culture, preferences, and life context."),
 desc_sig=("The Signature therapy framework maps each approach to its change mechanisms, practice "
  "elements, and progress markers, so training, supervision, and fidelity checks all reference the "
  "same model."),
 how_pub=("After assessment, therapist and client agree on an approach fitting the problem and the "
  "person's preferences. Sessions follow a structure - agenda, skills practice, homework review - "
  "over a planned number of weeks. Progress measures show whether symptoms and functioning improve; "
  "the plan adapts if they do not."),
 how_sig=("Signature fidelity checklists let supervisors verify the active ingredients are present "
  "without micromanaging style."),
 keys=["Tested in research for specific problems",
  "CBT, interpersonal therapy, behavioral activation are prominent examples",
  "Structured sessions with between-session practice",
  "Progress measured, plans adapted",
  "Adapted to culture, preferences, context",
  "Evidence-based is not one-size-fits-all"],
 reqs=["Therapists trained and supervised in the model",
  "Session structure and progress measures",
  "Cultural adaptation capacity"],
 stds=["Clinical practice guidelines recommending specific therapies (public)",
  "Training and fidelity standards per model (public literature)"],
 cites=["American Psychological Association — therapy evidence resources (public)",
  "National Institute of Mental Health — psychotherapy information (public)"],
 demo=("pathway", {"steps": ["Agree on approach", "Learn the model", "Practice skills in session",
   "Apply between sessions", "Measure progress", "Consolidate gains"]})),

dict(title="Medication Management Services", tier=F,
 desc_pub=("Medication management services cover psychiatric evaluation, prescribing, monitoring, "
  "and education about psychiatric medications. A prescriber - usually a psychiatrist, psychiatric "
  "nurse practitioner, or primary-care clinician - evaluates symptoms and history, discusses "
  "benefits and risks, and starts medication when appropriate.\n"
  "Management is ongoing: follow-up visits check effectiveness and side effects, doses adjust, and "
  "education covers what to expect and when to call. Decisions are shared - the client's experience "
  "of benefits and side effects weighs as heavily as symptom scores. This record is educational; "
  "medication decisions belong with qualified prescribers."),
 desc_sig=("Signature medication management pairs the clinical workflow with a client-facing "
  "education and tracking companion, so the person's daily experience informs every prescriber "
  "decision."),
 how_pub=("Evaluation leads to a shared decision about whether to try medication. If yes, the "
  "prescriber starts conservatively, schedules close follow-up, and teaches the client what to "
  "watch for. At each visit, effectiveness and side effects are reviewed and the plan adjusts - "
  "continue, adjust, switch, or taper - always with the client's informed participation."),
 how_sig=("Signature visit prep summarizes the client's tracked experience since the last visit, "
  "making reviews data-informed."),
 keys=["Covers evaluation, prescribing, monitoring, education",
  "Prescribers: psychiatrists, psychiatric NPs, primary-care clinicians",
  "Decisions are shared with the client",
  "Follow-up checks effectiveness and side effects",
  "Education covers what to expect and when to call",
  "Medication decisions belong with qualified prescribers"],
 reqs=["Qualified prescribers with follow-up capacity",
  "Side-effect monitoring protocols",
  "Client education materials"],
 stds=["Prescribing scope-of-practice laws (public)",
  "Clinical guidelines for specific conditions (public literature)"],
 cites=["National Institute of Mental Health — medication information (public)",
  "U.S. Food and Drug Administration — medication guides (public)"],
 demo=("outcome", {"label": "Clients reporting treatment plan understanding", "pre": 58, "post": 91})),

dict(title="Crisis Services and Hotlines", tier=F,
 desc_pub=("Crisis services provide immediate help when someone is in acute distress: 24-hour hotlines "
  "and text lines, mobile crisis teams that respond in person, crisis stabilization units, and "
  "emergency department partnerships. In the United States, 988 is the national Suicide and Crisis "
  "Lifeline, reachable by call or text around the clock.\n"
  "The model is stabilize, assess, plan, and connect: de-escalate the immediate crisis, assess "
  "safety, build a short-term safety plan, and link to ongoing care with follow-up. Reaching out is "
  "a sign of strength, and these services exist precisely for moments when coping alone is not enough."),
 desc_sig=("Signature crisis design closes the loop by protocol: every crisis contact generates a "
  "follow-up task and a connection check, so the moment of courage in reaching out reliably becomes "
  "an on-ramp to care."),
 how_pub=("The person calls, texts, or walks in; a trained counselor listens, assesses safety, and "
  "helps de-escalate. Together they build a safety plan - warning signs, coping strategies, people "
  "and resources to contact. Mobile teams or stabilization units engage when in-person help is "
  "needed. Follow-up within days confirms connection to ongoing support."),
 how_sig=("Signature follow-up tasks are created at contact time and tracked until the connection "
  "is confirmed."),
 keys=["Hotlines, text lines, mobile teams, stabilization units",
  "988 is the U.S. national Suicide and Crisis Lifeline",
  "Model: stabilize, assess, plan, connect",
  "Safety planning is the core intervention",
  "Follow-up converts contact into ongoing care",
  "Reaching out is a sign of strength"],
 reqs=["24-hour trained staffing",
  "Risk-assessment and safety-planning protocols",
  "Linkages to ongoing care providers"],
 stds=["988 Lifeline service standards (public)",
  "SAMHSA crisis-service guidelines (public)"],
 cites=["988 Suicide and Crisis Lifeline — public information (public)",
  "Substance Abuse and Mental Health Services Administration — crisis services (public)"],
 demo=("outcome", {"label": "Crisis callers linked to follow-up care", "pre": 52, "post": 87})),

dict(title="Peer Support Services", tier=F,
 desc_pub=("Peer support services are delivered by people with lived experience of mental health "
  "challenges who are trained and often certified to help others. Peer specialists share hope "
  "through example, coach self-advocacy and coping skills, accompany people to appointments, and "
  "bridge the gap between clinical services and daily life.\n"
  "Research shows peer support improves engagement, hope, and self-management. Because the helper "
  "has 'been there,' the relationship carries a credibility that purely professional roles cannot "
  "replicate - while remaining a complement to, not a replacement for, clinical care."),
 desc_sig=("Signature peer programs define the peer role with the same rigor as clinical roles - "
  "competencies, supervision, and outcome tracking - so lived experience is deployed as a designed "
  "service, not an informal add-on."),
 how_pub=("Agencies hire and certify peer specialists, then integrate them into teams with clear "
  "roles: outreach, engagement, coaching, accompaniment, and group facilitation. Peers receive "
  "supervision attuned to the role's unique boundary questions. Clients choose peer support as part "
  "of their plan."),
 how_sig=("Signature role definitions spell out peer competencies and supervision, protecting both "
  "the peer's recovery and the client's care."),
 keys=["Delivered by people with lived experience, trained and certified",
  "Builds hope, self-advocacy, coping, engagement",
  "Bridges clinical care and daily life",
  "Complements clinical care; does not replace it",
  "Credibility of shared experience",
  "Needs role-appropriate supervision"],
 reqs=["Certified peer specialists",
  "Clear role definitions within teams",
  "Supervision attuned to peer-specific boundaries"],
 stds=["State peer-certification standards (public)",
  "SAMHSA peer-support guidance (public)"],
 cites=["Substance Abuse and Mental Health Services Administration — peer support (public)",
  "National Association of Peer Supporters — standards (public)"],
 demo=("outcome", {"label": "Clients engaged at 90 days", "pre": 61, "post": 84})),

dict(title="Community Mental Health Centers", tier=F,
 desc_pub=("Community mental health centers (CMHCs) are local hubs offering outpatient therapy, "
  "psychiatric care, crisis response, case management, and often substance use services under one "
  "roof - usually with sliding-scale fees and a mandate to serve everyone regardless of ability to "
  "pay. They grew from the 1963 Community Mental Health Act's vision of care in communities rather "
  "than distant institutions.\n"
  "A center's value is comprehensiveness: one intake can open therapy, medication management, peer "
  "support, and benefits help together. Many also run outreach, school partnerships, and jail "
  "diversion programs."),
 desc_sig=("Signature center design organizes the hub around pathways rather than departments: a "
  "client's journey team draws from every service as needed, with one plan and one record."),
 how_pub=("A resident contacts the center, completes intake and screening, and is matched to "
  "services by need and preference. Care teams coordinate across the center's programs; case "
  "managers link to outside resources like housing and employment. Sliding fees are set at intake "
  "so cost never blocks the door."),
 how_sig=("Signature journey teams replace departmental handoffs with one accountable team per "
  "client."),
 keys=["Local hubs: therapy, psychiatric care, crisis, case management, substance use",
  "Sliding-scale fees; serve regardless of ability to pay",
  "Roots in the 1963 Community Mental Health Act",
  "One intake can open multiple services",
  "Often run outreach, school, and diversion programs",
  "Comprehensiveness is the core value"],
 reqs=["Multidisciplinary staffing across core services",
  "Sliding-fee and charity-care policies",
  "Community governance or advisory input"],
 stds=["State CMHC certification standards (public)",
  "Accreditation standards (e.g., CARF, Joint Commission - public)"],
 cites=["Substance Abuse and Mental Health Services Administration — CMHC resources (public)",
  "National Council for Mental Wellbeing — public resources (public)"],
 demo=("match", {"need": "therapy plus medication management in one place",
   "levels": [{"level": "Community mental health center", "fits": ["therapy plus medication management in one place"], "example": "one intake, full team"},
              {"level": "Solo private practice", "fits": [], "example": "therapy only"}]})),

dict(title="School and Workplace Programs", tier=F,
 desc_pub=("Schools and workplaces are where people spend their days, so both host mental health "
  "supports. Schools offer counselors, social workers, psychologists, prevention curricula, and "
  "referral to community care. Workplaces offer employee assistance programs (EAPs) - confidential "
  "short-term counseling and referral, usually free to employees - plus manager training and "
  "wellness initiatives.\n"
  "These programs work by proximity and normalization: help is nearby, confidential, and framed as "
  "a normal resource rather than a last resort. Early identification in these settings prevents "
  "small problems from becoming crises."),
 desc_sig=("Signature setting-based design embeds brief screening, self-help tools, and warm referral "
  "paths directly into school and workplace routines, so support finds people instead of waiting to "
  "be found."),
 how_pub=("Schools identify needs through staff referral, screening, or student self-referral, then "
  "provide brief counseling or refer outward. Workplaces promote the EAP, train managers to notice "
  "and refer supportively, and connect employees to confidential assessment with referral to "
  "ongoing care when needed."),
 how_sig=("Signature warm-referral paths carry context with consent, so the receiving provider "
  "starts informed."),
 keys=["Schools: counselors, psychologists, prevention, referral",
  "Workplaces: EAPs - confidential, short-term, usually free",
  "Proximity and normalization drive use",
  "Early identification prevents escalation",
  "Manager and teacher training matters",
  "Confidentiality protections encourage uptake"],
 reqs=["On-site or contracted counseling capacity",
  "Confidential referral processes",
  "Staff training on noticing and referring"],
 stds=["School counseling practice standards (public)",
  "EAP industry standards (public literature)"],
 cites=["U.S. Dept. of Education — school mental health guidance (public)",
  "Employee Assistance Professionals Association — standards (public)"],
 demo=("outcome", {"label": "EAP users connected to ongoing care when needed", "pre": 49, "post": 78})),

dict(title="Paying for Care: Insurance and Parity", tier=F,
 desc_pub=("Mental health parity laws require most insurance plans to cover mental health and "
  "substance use care comparably to medical care - no stricter visit limits or higher cost-sharing "
  "without justification. In practice, coverage varies: deductibles, copays, prior authorization, "
  "and narrow networks still create barriers.\n"
  "For the uninsured, options include community centers with sliding scales, federally qualified "
  "health centers, university training clinics, and crisis services that are free to all. Benefits "
  "navigators and clinic billing staff help people understand costs before care begins."),
 desc_sig=("Signature coverage navigation pre-checks benefits, estimates out-of-pocket cost, and "
  "flags parity violations for appeal - turning insurance from a maze into a computed answer."),
 how_pub=("Before starting care, the person or clinic verifies benefits: covered services, cost-"
  "sharing, authorization rules, and in-network providers. The clinic explains expected costs in "
  "plain language. If coverage is denied unfairly, parity law provides appeal rights; navigators "
  "help file them."),
 how_sig=("Signature benefit checks run before the first appointment, so cost surprises never "
  "ambush a new client."),
 keys=["Parity law requires comparable coverage for mental health care",
  "Barriers persist: deductibles, authorization, narrow networks",
  "Uninsured options: CMHCs, FQHCs, training clinics, free crisis lines",
  "Verify benefits before care begins",
  "Denials can be appealed under parity rights",
  "Navigators help with coverage puzzles"],
 reqs=["Benefits-verification workflow",
  "Plain-language cost estimates",
  "Appeals assistance capacity"],
 stds=["Mental Health Parity and Addiction Equity Act (public law)",
  "State parity enforcement rules"],
 cites=["U.S. Dept. of Labor — parity guidance (public)",
  "Centers for Medicare and Medicaid Services — coverage rules (public)"],
 demo=("outcome", {"label": "Clients with verified coverage before visit one", "pre": 44, "post": 89})),

# ---------------- Compounded (12) ----------------
dict(title="Cognitive Behavioral Therapy in Practice", tier=C,
 desc_pub=("Cognitive behavioral therapy (CBT) is a structured, time-limited therapy built on the "
  "insight that thoughts, feelings, and behaviors influence each other. Clients learn to notice "
  "unhelpful thought patterns, test them against evidence, and change behaviors that maintain "
  "distress - for example, gradually re-engaging with avoided activities.\n"
  "Sessions follow an agenda: review practice from last time, learn and rehearse a skill, plan "
  "between-session practice. Decades of trials support CBT for depression, anxiety disorders, PTSD, "
  "and more. This record is educational; therapy itself happens with a qualified clinician."),
 desc_sig=("The Signature CBT framework decomposes the therapy into teachable modules - thought "
  "records, behavioral experiments, exposure hierarchies - each with practice guides and progress "
  "markers, so training and fidelity stay anchored to the active ingredients."),
 how_pub=("Therapist and client map the problem into thought-feeling-behavior cycles, set concrete "
  "goals, and work through skills week by week: cognitive restructuring, behavioral activation, "
  "exposure, problem-solving. Homework applies skills in real life. Progress measures track symptom "
  "change; the final sessions consolidate gains and plan for setbacks."),
 how_sig=("Signature module guides give therapists session-ready materials for each skill, keeping "
  "delivery consistent without scripting the relationship."),
 keys=["Thoughts, feelings, and behaviors influence each other",
  "Skills: cognitive restructuring, behavioral activation, exposure, problem-solving",
  "Structured sessions with between-session practice",
  "Time-limited with measurable goals",
  "Strong trial evidence for depression, anxiety, PTSD",
  "Educational record; therapy with qualified clinicians"],
 reqs=["CBT-trained therapists with supervision",
  "Session materials and practice guides",
  "Progress-measure routine"],
 stds=["Clinical guidelines recommending CBT for specific conditions (public)",
  "CBT training and certification standards (public literature)"],
 cites=["American Psychological Association — CBT evidence resources (public)",
  "National Institute for Health and Care Excellence — guidelines (public)"],
 demo=("pathway", {"steps": ["Map thought-feeling-behavior cycles", "Set concrete goals",
   "Learn restructuring skills", "Practice between sessions", "Add behavioral experiments",
   "Measure change", "Consolidate and relapse-plan"]})),

dict(title="Trauma-Focused Care Approaches", tier=C,
 desc_pub=("Trauma-focused approaches help people process traumatic experiences and rebuild a sense "
  "of safety. They share a phased structure: first stabilization and coping skills, then trauma "
  "processing (telling and reworking the trauma story in approaches like trauma-focused CBT or EMDR), "
  "then consolidation and reconnection with life.\n"
  "Safety and pacing are paramount: processing never begins before the person has coping resources "
  "and a stable-enough life situation. These are specialist therapies delivered by trained "
  "clinicians; this record describes the service landscape educationally."),
 desc_sig=("Signature trauma-care design adds phase-gate criteria between stabilization, processing, "
  "and consolidation, so advancement is a clinical decision with observable markers rather than a "
  "guess."),
 how_pub=("Assessment maps trauma history, current symptoms, and resources. Phase one builds safety "
  "and coping skills. Phase two processes traumatic memories with a trained clinician using an "
  "evidence-based method. Phase three consolidates gains and reconnects the person with work, "
  "relationships, and community. Progress and safety are monitored throughout."),
 how_sig=("Signature phase-gate checklists make readiness for processing an explicit, reviewable "
  "decision."),
 keys=["Phased: stabilization, processing, consolidation",
  "Processing methods include trauma-focused CBT and EMDR",
  "Safety and coping come before trauma processing",
  "Pacing follows the client's readiness",
  "Specialist clinicians deliver these therapies",
  "Educational record; care with trained professionals"],
 reqs=["Trauma-trained clinicians with model-specific training",
  "Phase-gate readiness criteria",
  "Safety monitoring throughout"],
 stds=["Clinical guidelines for PTSD treatment (public)",
  "Model-specific training standards (public literature)"],
 cites=["National Child Traumatic Stress Network — treatments (public)",
  "U.S. Dept. of Veterans Affairs — PTSD treatment guidance (public)"],
 demo=("screen", {"items": [2, 1, 3, 2, 1]})),

dict(title="Services for Children and Adolescents", tier=C,
 desc_pub=("Youth services adapt care to developing minds: play-based and family-involved therapies "
  "for young children, skills groups for teens, school coordination, and parent training programs "
  "with strong evidence (like parent-child interaction therapy for young children). Systems of care "
  "wrap services around the youth and family with one team and one plan.\n"
  "Family involvement is usually essential - parents learn the same skills the child practices - and "
  "consent involves both youth assent and parent permission, with confidentiality calibrated to age "
  "and safety."),
 desc_sig=("Signature youth-service design centers the family team: one shared plan visible to "
  "family, school, and providers, with developmentally matched materials for each age band."),
 how_pub=("Referral - from parents, schools, or pediatricians - leads to family-inclusive "
  "assessment. The team builds a plan mixing therapy, skills groups, school supports, and parent "
  "training. Care coordinators keep school and providers aligned. Progress is measured with "
  "youth-appropriate tools and family feedback."),
 how_sig=("Signature shared plans give schools and providers the same goals with role-specific "
  "tasks, ending contradictory instructions to families."),
 keys=["Developmentally matched: play-based, family-involved, skills groups",
  "Parent training programs carry strong evidence",
  "Systems of care: one team, one plan",
  "Family involvement is usually essential",
  "Consent balances youth assent, parent permission, safety",
  "School coordination is part of treatment"],
 reqs=["Child-trained clinicians",
  "Family engagement and parent-training capacity",
  "School partnership agreements"],
 stds=["Systems-of-care values and principles (public)",
  "Clinical guidelines for youth conditions (public)"],
 cites=["Substance Abuse and Mental Health Services Administration — systems of care (public)",
  "American Academy of Child and Adolescent Psychiatry — public resources (public)"],
 demo=("outcome", {"label": "Youth meeting treatment goals", "pre": 57, "post": 83})),

dict(title="Services for Older Adults", tier=C,
 desc_pub=("Older adults face distinct mental health needs: late-life depression (often missed because "
  "it looks like 'just aging'), anxiety, grief, cognitive changes, and isolation. Services adapt "
  "accordingly - in-home and telehealth options for limited mobility, coordination with primary "
  "care and aging services, and caregiver support.\n"
  "Depression in later life is treatable, not inevitable. Programs like PEARLS (home-based "
  "counseling for older adults) show that adapted, accessible care works. Screening in primary care "
  "catches what specialty clinics never see."),
 desc_sig=("Signature older-adult design co-locates mental health with aging services - one "
  "assessment feeding both the care plan and the benefits plan - so elders are not shuttled between "
  "silos."),
 how_pub=("Primary care or aging-service referrals trigger assessment adapted for sensory, cognitive, "
  "and mobility needs. Care may be home-based, by video, or in senior-friendly clinics, coordinated "
  "with medical providers and family caregivers. Progress measures use age-appropriate tools."),
 how_sig=("Signature co-assessment produces one plan covering mental health, daily-living supports, "
  "and caregiver needs together."),
 keys=["Late-life depression is treatable, not inevitable aging",
  "Adapt for mobility, sensory, cognitive needs",
  "Home-based and telehealth options widen reach",
  "Coordinate with primary care and aging services",
  "Caregiver support is part of the plan",
  "Primary-care screening catches hidden cases"],
 reqs=["Geriatric-competent clinicians",
  "Home-visit and telehealth capacity",
  "Aging-service partnerships"],
 stds=["Clinical guidelines for late-life depression (public)",
  "Older Americans Act service coordination (public law)"],
 cites=["National Institute on Aging — public information (public)",
  "Administration for Community Living — aging resources (public)"],
 demo=("match", {"need": "counseling at home for limited mobility",
   "levels": [{"level": "Home-based counseling", "fits": ["counseling at home for limited mobility"], "example": "clinician visits the home"},
              {"level": "Clinic-only program", "fits": [], "example": "requires travel"}]})),

dict(title="Substance Use and Co-occurring Care", tier=C,
 desc_pub=("Many people experience mental health and substance use challenges together - co-occurring "
  "disorders. Integrated care treats both at once with one team and one plan, which outperforms "
  "sequential or parallel treatment. Services span screening, withdrawal management, outpatient and "
  "residential treatment, medications for opioid and alcohol use disorders, and peer recovery support.\n"
  "The chronic-care view applies: these are long-term health conditions managed over time, with "
  "relapse signaling plan adjustment rather than failure. This record is educational; treatment "
  "decisions belong with qualified professionals."),
 desc_sig=("Signature co-occurring design runs a single integrated pathway with stage markers for "
  "both conditions, so neither the mental health nor the substance use side of the plan goes "
  "untracked."),
 how_pub=("Screening identifies both conditions; one team assesses severity and builds an "
  "integrated plan - therapy addressing both, medication evaluation, peer support, housing and "
  "employment linkages. Engagement is assertive and nonjudgmental; setbacks trigger plan review, "
  "not discharge."),
 how_sig=("Signature dual stage-tracking keeps both conditions visible on one dashboard, preventing "
  "the common failure of treating one while ignoring the other."),
 keys=["Co-occurring disorders are common; integrated care works best",
  "One team, one plan for both conditions",
  "Continuum: screening, withdrawal management, outpatient, residential, medications, peers",
  "Chronic-care view: manage over time",
  "Setbacks trigger plan review, not discharge",
  "Educational record; professionals guide treatment"],
 reqs=["Dually trained staff or integrated teams",
  "Access to the full continuum",
  "Confidentiality compliance (42 CFR Part 2)"],
 stds=["SAMHSA co-occurring disorders guidance (public)",
  "42 CFR Part 2 confidentiality (public regulation)"],
 cites=["Substance Abuse and Mental Health Services Administration — co-occurring resources (public)"],
 demo=("pathway", {"steps": ["Screen for both conditions", "Integrated assessment",
   "One team, one plan", "Therapy plus supports", "Peer recovery linkage",
   "Monitor both conditions", "Adjust on setbacks"]})),

dict(title="Assertive Community Treatment", tier=C,
 desc_pub=("Assertive Community Treatment (ACT) is an intensive team model for people with serious "
  "mental illness who have not engaged well with office-based care. A multidisciplinary team - "
  "psychiatrist, nurses, social workers, peer specialists, employment specialists - shares a small "
  "caseload (about 1 staff to 10 clients) and delivers most services in the community: homes, "
  "parks, shelters.\n"
  "ACT is among the most evidence-backed models in mental health, reducing hospitalization and "
  "homelessness. Fidelity to the model - low caseloads, 24-hour availability, in-vivo work - "
  "predicts results."),
 desc_sig=("Signature ACT operations add a fidelity-and-outcome dashboard per team, so programs see "
  "whether they are delivering real ACT or ACT in name only."),
 how_pub=("Referral and assessment confirm fit. The team engages assertively - meeting people where "
  "they are, persistently - and provides medication management, therapy, daily-living support, "
  "housing and employment help, and crisis response around the clock. Daily team meetings coordinate "
  "who does what today."),
 how_sig=("Signature team coordination tools keep the shared caseload visible with today's tasks "
  "assigned, preserving the daily-huddle discipline at scale."),
 keys=["For serious mental illness with poor office-care engagement",
  "Multidisciplinary team, ~1:10 staffing ratio",
  "Most services delivered in the community",
  "24-hour crisis availability",
  "Among the most evidence-backed models",
  "Fidelity predicts results"],
 reqs=["Full multidisciplinary team",
  "Low caseloads and 24-hour coverage",
  "Fidelity measurement"],
 stds=["ACT fidelity standards (public literature)",
  "State ACT program certification rules"],
 cites=["Substance Abuse and Mental Health Services Administration — ACT resources (public)"],
 demo=("outcome", {"label": "Hospital days per client per year", "pre": 48, "post": 19})),

dict(title="Supported Employment and Education", tier=C,
 desc_pub=("Supported employment helps people with mental health conditions get and keep competitive "
  "jobs; supported education does the same for schooling. The Individual Placement and Support "
  "(IPS) model - rapid job search, integrated with treatment, based on client preference, with "
  "ongoing supports - has the strongest evidence in psychiatric rehabilitation.\n"
  "Work is recovery: employment predicts better symptoms, housing stability, and quality of life. "
  "Programs honor client choice of job type and provide benefits counseling so earnings do not "
  "unexpectedly jeopardize needed supports."),
 desc_sig=("Signature IPS operations pair the employment specialist with the treatment team on one "
  "shared record, so job supports and clinical care reinforce rather than ignore each other."),
 how_pub=("The employment specialist joins the treatment team, learns the client's job preferences, "
  "and begins rapid job search - applications within weeks, not months of prevocational training. "
  "Once hired, the specialist provides on-the-job coaching and problem-solving indefinitely, "
  "coordinated with the clinical team."),
 how_sig=("Signature shared records let employment and clinical staff see the same goals and "
  "early-warning signs."),
 keys=["IPS model: rapid search, integrated, preference-based, ongoing supports",
  "Strongest evidence in psychiatric rehabilitation",
  "Work predicts better symptoms, stability, quality of life",
  "Client choice of job type is central",
  "Benefits counseling prevents earnings surprises",
  "Supports continue after hiring"],
 reqs=["IPS-trained employment specialists embedded in teams",
  "Employer partnerships",
  "Benefits-counseling capacity"],
 stds=["IPS fidelity standards (public literature)",
  "State vocational rehabilitation coordination rules"],
 cites=["IPS Employment Center — model resources (public)",
  "Substance Abuse and Mental Health Services Administration — supported employment (public)"],
 demo=("outcome", {"label": "Clients in competitive employment", "pre": 23, "post": 61})),

dict(title="Housing-First Supportive Services", tier=C,
 desc_pub=("Housing First provides stable housing to people experiencing homelessness without "
  "requiring sobriety or treatment participation first, then wraps voluntary supportive services "
  "- case management, health care, peer support - around the housed person. Trials show it ends "
  "homelessness for most participants and reduces costly crisis-service use.\n"
  "Supportive services are the 'supportive' in supportive housing: eviction prevention, daily-living "
  "skills, health linkage, community building. Participation is voluntary; housing is not "
  "contingent on compliance."),
 desc_sig=("Signature supportive-housing design tracks housing stability and service engagement on "
  "one tenancy dashboard, so property management and support teams coordinate instead of working "
  "at cross purposes."),
 how_pub=("Coordinated entry prioritizes households by vulnerability; housing navigators secure units "
  "and negotiate with landlords. Once housed, case managers visit regularly, link health and "
  "benefits services, and intervene early on tenancy risks. Services flex with the tenant's goals."),
 how_sig=("Signature tenancy dashboards give support teams early warning of rent, behavior, or "
  "health risks before eviction processes start."),
 keys=["Housing without preconditions, then voluntary services",
  "Ends homelessness for most participants in trials",
  "Reduces crisis-service costs",
  "Services: case management, health linkage, daily-living skills",
  "Participation voluntary; housing not contingent",
  "Eviction prevention protects the investment"],
 reqs=["Housing stock and landlord partnerships",
  "Mobile support teams",
  "Coordinated-entry prioritization"],
 stds=["HUD housing-first guidance (public)",
  "Supportive-housing fidelity standards (public literature)"],
 cites=["U.S. Dept. of Housing and Urban Development — Housing First (public)",
  "National Alliance to End Homelessness — research (public)"],
 demo=("outcome", {"label": "Tenants stably housed at 24 months", "pre": 41, "post": 85})),

dict(title="Telehealth Counseling Services", tier=C,
 desc_pub=("Telehealth counseling delivers therapy and psychiatric care by video or phone, expanding "
  "access for rural residents, people with limited mobility, and those with tight schedules. "
  "Research finds it effective for many conditions when delivered by qualified clinicians with "
  "proper technology.\n"
  "Quality telehealth requires private settings on both ends, reliable connections, emergency "
  "protocols for the client's location, and licensing compliance across state lines. It complements "
  "in-person care; some situations still need a room."),
 desc_sig=("Signature telehealth design standardizes the virtual care pathway - tech checks, safety "
  "protocols, engagement tactics - so remote sessions match in-person quality by design rather than "
  "by improvisation."),
 how_pub=("The client needs a private space and a device; the clinic verifies identity, consent, and "
  "the client's physical location for emergency purposes. Sessions run like in-person ones with "
  "adapted engagement techniques. Outcomes are measured the same way, and hybrid models mix remote "
  "and in-person visits."),
 how_sig=("Signature pre-session tech and safety checks run automatically, so sessions start on "
  "time and safely."),
 keys=["Expands access: rural, mobility-limited, tight schedules",
  "Effective for many conditions with qualified clinicians",
  "Private settings required on both ends",
  "Emergency protocols tied to client location",
  "Licensing rules govern cross-state practice",
  "Complements in-person care"],
 reqs=["Secure video platform and consent workflows",
  "Location-based emergency protocols",
  "Clinician telehealth training"],
 stds=["State telehealth practice rules (public)",
  "APA telepsychology guidelines (public)"],
 cites=["American Psychological Association — telehealth guidance (public)",
  "Federal Communications Commission — telehealth resources (public)"],
 demo=("outcome", {"label": "Clients attending scheduled sessions", "pre": 66, "post": 88})),

dict(title="Group Therapy Models", tier=C,
 desc_pub=("Group therapy treats several clients together with one or two facilitators, using shared "
  "experience as a therapeutic force. Models include skills groups (teaching coping skills), support "
  "groups (mutual aid for shared challenges), process groups (exploring patterns in relationships), "
  "and psychoeducation groups (teaching about conditions and management).\n"
  "Groups reduce isolation, normalize struggles, and let members learn from each other - often at "
  "lower cost than individual therapy. Skilled facilitation keeps groups safe, focused, and "
  "confidential."),
 desc_sig=("Signature group design standardizes curricula, screening for group fit, and outcome "
  "tracking per cohort, so group therapy is a designed service with measured results."),
 how_pub=("Clients are screened for readiness and fit, then join a closed or open group with clear "
  "ground rules - confidentiality, respect, attendance. Sessions follow the model's structure: "
  "check-in, skills or discussion, practice planning. Progress is reviewed individually alongside "
  "group participation."),
 how_sig=("Signature cohort tracking measures each group's outcomes, informing facilitator coaching "
  "and curriculum refinement."),
 keys=["Skills, support, process, and psychoeducation models",
  "Shared experience is a therapeutic force",
  "Reduces isolation and normalizes struggles",
  "Screening for fit protects the group",
  "Ground rules: confidentiality, respect, attendance",
  "Often lower cost than individual therapy"],
 reqs=["Trained group facilitators",
  "Screening and ground-rule processes",
  "Appropriately sized private meeting space"],
 stds=["Group-therapy practice guidelines (public literature)",
  "Agency confidentiality policies for groups"],
 cites=["American Group Psychotherapy Association — public resources (public)"],
 demo=("outcome", {"label": "Group members completing the curriculum", "pre": 58, "post": 82})),

dict(title="Family Involvement in Care", tier=C,
 desc_pub=("Families are often the primary support system, and involving them - with the client's "
  "consent - improves outcomes. Family psychoeducation teaches relatives about conditions, "
  "communication skills, and crisis response; family therapy addresses patterns affecting everyone.\n"
  "Involvement is calibrated: adults choose how much family participates, while youth care "
  "typically requires it. Programs like Family-to-Family (peer-led family education) show that "
  "informed families cope better and support recovery more effectively."),
 desc_sig=("Signature family-involvement design gives families - with consent - a structured role in "
  "the care plan with their own education track and communication channel, replacing ad-hoc updates "
  "with designed partnership."),
 how_pub=("With client consent, clinicians invite family to education sessions and care-planning "
  "meetings, teach communication and crisis skills, and establish how information will be shared "
  "ongoing. Boundaries the client sets are respected and revisited as relationships evolve."),
 how_sig=("Signature family portals share consented updates and education, keeping families "
  "informed without burdening clinicians."),
 keys=["Family involvement improves outcomes with client consent",
  "Psychoeducation: conditions, communication, crisis response",
  "Adults choose their family's level of involvement",
  "Youth care typically requires family participation",
  "Peer-led family programs build coping",
  "Boundaries are set by the client and revisited"],
 reqs=["Consent workflows for family participation",
  "Family education curricula",
  "Clinician skill in family dynamics"],
 stds=["Family psychoeducation model standards (public literature)",
  "Confidentiality rules for adult clients (public law)"],
 cites=["National Alliance on Mental Illness — Family-to-Family (public)",
  "Substance Abuse and Mental Health Services Administration — family resources (public)"],
 demo=("outcome", {"label": "Families completing psychoeducation", "pre": 47, "post": 79})),

dict(title="Measuring Treatment Outcomes", tier=C,
 desc_pub=("Outcome measurement in mental health tracks whether clients get better: symptom scores "
  "(PHQ-9, GAD-7), functioning (work, school, relationships), and personal recovery goals. "
  "Measurement-based care - systematically tracking and using these numbers - improves results "
  "compared to clinical impression alone.\n"
  "Programs aggregate de-identified outcomes to evaluate services, satisfy funders, and drive "
  "improvement. The client's own definition of progress belongs at the center: numbers serve the "
  "person, not the reverse."),
 desc_sig=("Signature outcome systems make measurement ambient: brief check-ins via the client's "
  "preferred channel feed live dashboards for client, clinician, and program - turning measurement "
  "from paperwork into a shared compass."),
 how_pub=("Clinics select a small set of valid measures, collect them at intake and intervals, and "
  "review trends with the client to guide plan adjustments. Aggregated data is reported to funders "
  "and quality committees, which target improvement where outcomes lag."),
 how_sig=("Signature ambient collection - brief digital check-ins between visits - gives clinicians "
  "trend data without consuming session time."),
 keys=["Track symptoms, functioning, and personal recovery goals",
  "Measurement-based care beats impression alone",
  "Review trends with the client to guide plans",
  "Aggregate data evaluates programs and satisfies funders",
  "A few valid measures beat many weak ones",
  "Numbers serve the person, not the reverse"],
 reqs=["Selected valid measures and collection schedule",
  "Review-with-client workflow",
  "Aggregation and reporting capacity"],
 stds=["Joint Commission outcome-measurement expectations (public)",
  "Funder performance-measure requirements"],
 cites=["Agency for Healthcare Research and Quality — measurement-based care (public)",
  "The Joint Commission — behavioral health standards (public)"],
 demo=("outcome", {"label": "Clients showing reliable improvement", "pre": 52, "post": 76})),

# ---------------- Advanced (11) ----------------
dict(title="Clinical Practice Guidelines in Use", tier=A,
 desc_pub=("Clinical practice guidelines distill research into recommendations for assessment and "
  "treatment of specific conditions - which therapies and medications have the best evidence, in "
  "what sequence, with what monitoring. Major developers include NICE (UK), the APA, and the VA/DoD.\n"
  "Guidelines inform but do not dictate: clinicians adapt recommendations to the individual, "
  "considering comorbidity, preferences, culture, and prior treatment response. Services implement "
  "guidelines through training, decision supports, and fidelity monitoring - closing the gap "
  "between what research supports and what clients receive."),
 desc_sig=("Signature guideline implementation encodes recommendations as pathway decision supports "
  "with documented adaptation reasons, so fidelity and personalization coexist visibly."),
 how_pub=("Services adopt guidelines for their key conditions, train staff, and build reminders into "
  "workflows - assessment checklists, treatment algorithms, monitoring schedules. Clinicians "
  "document when they diverge from guidelines and why. Quality review tracks concordance and "
  "outcomes."),
 how_sig=("Signature decision supports present guideline-concordant options at the point of care, "
  "with one-click documentation of clinical adaptations."),
 keys=["Distill research into assessment and treatment recommendations",
  "Developers: NICE, APA, VA/DoD, others",
  "Inform but do not dictate - adapt to the individual",
  "Implementation via training, decision supports, fidelity monitoring",
  "Document and justify divergences",
  "Close the research-to-practice gap"],
 reqs=["Adopted guidelines for key conditions",
  "Workflow-embedded decision supports",
  "Concordance and outcome monitoring"],
 stds=["Guideline developer methodology standards (public)",
  "AGREE II appraisal criteria (public)"],
 cites=["National Institute for Health and Care Excellence — guidelines (public)",
  "American Psychological Association — clinical practice guidelines (public)"],
 demo=("outcome", {"label": "Cases concordant with guidelines", "pre": 55, "post": 84})),

dict(title="Stepped Care Models", tier=A,
 desc_pub=("Stepped care organizes services as a ladder: everyone starts with the least intensive "
  "effective option (self-help, brief counseling), and steps up only if needed - with systematic "
  "monitoring deciding when. It reserves scarce specialist time for those who need it while giving "
  "most people prompt, lighter-touch help.\n"
  "The model's engine is monitoring: without scheduled re-assessment, people stall on failing "
  "steps. Done well, stepped care expands access dramatically at sustainable cost."),
 desc_sig=("Signature stepped care automates the engine: monitoring prompts, step-up criteria, and "
  "capacity-aware scheduling run as one system, so the ladder works at population scale."),
 how_pub=("Services define steps with entry criteria, deliver step-one interventions broadly, and "
  "monitor with standardized measures on a schedule. Non-responders step up to more intensive care "
  "through a defined handoff; responders step down to maintenance. Capacity is managed across steps."),
 how_sig=("Signature capacity management balances flow across steps so step-ups never dead-end on "
  "waitlists."),
 keys=["Start least-intensive; step up only if needed",
  "Monitoring is the engine - scheduled re-assessment",
  "Reserves specialists for those who need them",
  "Expands access at sustainable cost",
  "Defined handoffs between steps",
  "Responders step down to maintenance"],
 reqs=["Defined steps with entry and step-up criteria",
  "Monitoring schedule and measures",
  "Cross-step capacity management"],
 stds=["Stepped-care implementation guidance (public literature)",
  "NICE depression and anxiety pathways (public)"],
 cites=["National Institute for Health and Care Excellence — stepped care pathways (public)"],
 demo=("pathway", {"steps": ["Step 1: self-help and brief support", "Monitor at 4 weeks",
   "Step 2: structured therapy if needed", "Monitor at 8 weeks",
   "Step 3: intensive or specialist care", "Step down to maintenance"]})),

dict(title="Integrated Primary and Behavioral Care", tier=A,
 desc_pub=("Integrated care embeds behavioral health in primary-care settings - the place most people "
  "already go. Models range from co-located therapists to the Collaborative Care Model: a care "
  "manager, psychiatric consultant, and primary-care clinician working from a shared registry with "
  "measurement-driven adjustments.\n"
  "Integration catches conditions primary care would otherwise miss, treats them where patients "
  "are, and reduces stigma. The registry - tracking every enrolled patient's measures - is what "
  "makes it systematic rather than merely co-located."),
 desc_sig=("Signature integration runs the registry as a population-health engine: risk stratification, "
  "outreach lists, and caseload review cadences keep no enrolled patient invisible."),
 how_pub=("Clinics hire care managers and contract psychiatric consultants, build the patient "
  "registry, and train primary-care teams in warm handoffs. Care managers deliver brief "
  "interventions, track measures, and bring non-improving cases to consultant review. The primary-"
  "care clinician remains the hub."),
 how_sig=("Signature registry automation surfaces the right patients for review at the right time."),
 keys=["Behavioral health where patients already go",
  "Collaborative Care Model: manager, consultant, PCP, shared registry",
  "Catches what primary care would miss",
  "Reduces stigma through normalization",
  "Registry makes it systematic",
  "Measurement drives adjustments"],
 reqs=["Care managers and psychiatric consultation",
  "Shared registry with measures",
  "Warm-handoff workflows"],
 stds=["Collaborative Care Model fidelity criteria (public literature)",
  "CMS integration billing codes (public)"],
 cites=["University of Washington AIMS Center — collaborative care (public)",
  "Agency for Healthcare Research and Quality — integration resources (public)"],
 demo=("outcome", {"label": "Enrolled patients reaching remission", "pre": 34, "post": 62})),

dict(title="Cultural Adaptation of Therapies", tier=A,
 desc_pub=("Cultural adaptation modifies evidence-based therapies to fit clients' languages, values, "
  "and worldviews - without losing the active ingredients. Adaptations range from translated "
  "materials and culturally matched examples to deeper changes in metaphors, family involvement, "
  "and explanations of distress.\n"
  "Adaptation is done with communities, not to them: community input guides changes, and adapted "
  "versions are tested. The goal is care that feels respectful and relevant, which improves "
  "engagement and outcomes."),
 desc_sig=("Signature adaptation maintains a library of vetted cultural modifications per therapy "
  "module, so clinicians start from tested adaptations rather than improvising."),
 how_pub=("Programs partner with community members to identify needed adaptations, modify materials "
  "and examples while preserving core mechanisms, train clinicians in the adapted version, and "
  "evaluate engagement and outcomes against the standard version."),
 how_sig=("Signature adaptation libraries version each modification with its evidence, so practice "
  "stays both culturally responsive and evidence-anchored."),
 keys=["Fit language, values, worldviews - keep active ingredients",
  "Adapt with communities, not to them",
  "Ranges from translation to deeper metaphor changes",
  "Test adapted versions",
  "Respectful, relevant care improves engagement",
  "Preserve core mechanisms"],
 reqs=["Community partnership for adaptation",
  "Bilingual/bicultural clinical capacity",
  "Evaluation comparing adapted vs standard"],
 stds=["Cultural adaptation frameworks (public literature)",
  "CLAS standards for culturally appropriate services (public)"],
 cites=["U.S. Dept. of Health and Human Services — CLAS standards (public)",
  "American Psychological Association — multicultural guidelines (public)"],
 demo=("outcome", {"label": "Engagement among adapted-program clients", "pre": 58, "post": 86})),

dict(title="Suicide Prevention Service Systems", tier=A,
 desc_pub=("Suicide prevention works as a system, not a single service: universal awareness, "
  "screening in health settings, safety planning, lethal-means counseling, crisis response, and "
  "postvention support after a loss. The Zero Suicide framework commits health systems to safer "
  "care through leadership, training, screening, and continuous improvement.\n"
  "Means matter: reducing access to lethal means during high-risk periods saves lives because "
  "crises are often brief. Every contact - primary care, ER, crisis line - is a prevention "
  "opportunity. If you or someone you know is in crisis, contact 988 (US) or local emergency "
  "services immediately."),
 desc_sig=("Signature prevention systems wire every setting's screening into one risk-response "
  "protocol with follow-up tracking, so no identified risk is left without a next step."),
 how_pub=("Systems train all staff in risk identification, screen routinely in health settings, and "
  "respond to positive screens with full assessment, safety planning, and lethal-means counseling. "
  "Crisis lines and mobile teams provide immediate response; follow-up contacts sustain connection. "
  "Deaths and attempts are reviewed for system learning."),
 how_sig=("Signature risk-response tracking ensures every positive screen gets assessment, plan, "
  "and follow-up - verified, not assumed."),
 keys=["A system: awareness, screening, safety planning, means counseling, crisis, postvention",
  "Zero Suicide framework for health systems",
  "Reducing lethal-means access saves lives",
  "Crises are often brief - timing matters",
  "Every health contact is a prevention opportunity",
  "Review incidents for system learning"],
 reqs=["Universal staff training in risk identification",
  "Screening-to-response protocols in all settings",
  "Follow-up contact capacity"],
 stds=["Zero Suicide framework elements (public)",
  "Joint Commission suicide-prevention standards (public)"],
 cites=["Suicide Prevention Resource Center — public resources (public)",
  "988 Suicide and Crisis Lifeline — public information (public)"],
 demo=("pathway", {"steps": ["Routine screening", "Full risk assessment", "Safety planning",
   "Lethal-means counseling", "Crisis linkage", "Caring follow-up contacts"]})),

dict(title="Early Psychosis Intervention Programs", tier=A,
 desc_pub=("Early psychosis programs intervene in the first years of psychotic symptoms, when "
  "treatment changes trajectories most. Coordinated specialty care (CSC) teams provide medication "
  "management, therapy, family education, supported employment/education, and case management with "
  "small caseloads.\n"
  "Duration of untreated psychosis predicts outcomes - so these programs prioritize rapid access "
  "and outreach to schools and primary care. Recovery rates are substantially better than with "
  "usual care. This record is educational; evaluation belongs with qualified specialists."),
 desc_sig=("Signature early-psychosis design adds a rapid-access guarantee - assessment within days "
  "of referral - with outreach pipelines from schools and primary care feeding it."),
 how_pub=("Referrals flow from schools, primary care, and crisis services into rapid assessment. "
  "Eligible youth join a CSC team with a shared recovery plan spanning medication, therapy, family "
  "work, and school/work supports. Teams stay involved for about two years, tapering as recovery "
  "solidifies."),
 how_sig=("Signature rapid-access tracking measures days from referral to assessment, keeping the "
  "program honest about its core promise."),
 keys=["Intervene in the first years - timing changes trajectories",
  "Coordinated specialty care: meds, therapy, family, work/school, case management",
  "Shorter untreated duration predicts better outcomes",
  "Outreach to schools and primary care",
  "Small caseloads, team-based",
  "Better recovery rates than usual care"],
 reqs=["CSC-trained multidisciplinary teams",
  "Rapid-access assessment capacity",
  "School and primary-care referral pipelines"],
 stds=["CSC fidelity standards (public literature)",
  "State early-psychosis program standards"],
 cites=["National Institute of Mental Health — RAISE studies (public)",
  "Substance Abuse and Mental Health Services Administration — early psychosis (public)"],
 demo=("outcome", {"label": "Participants in school or work at 24 months", "pre": 38, "post": 71})),

dict(title="Forensic Mental Health Services", tier=A,
 desc_pub=("Forensic mental health services sit at the intersection of mental health and the legal "
  "system: competency evaluations, jail-based treatment, mental health courts, and reentry "
  "planning. The aim is appropriate care and fair process - treatment rather than punishment where "
  "illness drives behavior, with public safety held in view.\n"
  "Mental health courts divert eligible defendants into supervised treatment; reentry programs "
  "connect releasing individuals to care, housing, and benefits before release day. These are "
  "specialized, legally entangled services requiring cross-system fluency."),
 desc_sig=("Signature forensic design builds the intercept map - every point where justice and "
  "health systems meet - with a designed response at each, so diversion is systematic rather than "
  "accidental."),
 how_pub=("Courts, jails, and attorneys refer for evaluation and diversion screening. Eligible "
  "individuals enter treatment courts or jail-based programs with court-monitored plans. Reentry "
  "planners arrange care, housing, and benefits to start at release. Outcomes tracked include "
  "recidivism, hospitalization, and housing stability."),
 how_sig=("Signature intercept dashboards show flow and outcomes at each justice-health touchpoint, "
  "guiding where to invest."),
 keys=["Intersection of mental health and legal systems",
  "Competency evaluation, jail treatment, mental health courts, reentry",
  "Diversion into supervised treatment where appropriate",
  "Reentry planning starts before release",
  "Requires cross-system fluency",
  "Outcomes: recidivism, hospitalization, housing"],
 reqs=["Forensic-trained evaluators and clinicians",
  "Court and corrections partnerships",
  "Reentry benefit and housing linkages"],
 stds=["Forensic evaluation practice guidelines (public literature)",
  "Mental health court best-practice standards (public)"],
 cites=["Substance Abuse and Mental Health Services Administration — criminal justice resources (public)",
  "Council of State Governments Justice Center — public resources (public)"],
 demo=("outcome", {"label": "Participants stably housed post-release", "pre": 33, "post": 68})),

dict(title="Quality Improvement in Clinics", tier=A,
 desc_pub=("Quality improvement (QI) is the disciplined habit of making care better: pick a problem "
  "(no-show rates, wait times, outcome gaps), understand its causes, test a change on a small "
  "scale, measure, and spread what works. Methods like Plan-Do-Study-Act cycles and Lean structure "
  "the experimentation.\n"
  "QI differs from research: the goal is better care here, now - rapid cycles, local data, staff-"
  "led. Sustained programs build QI into routines: dashboards, improvement teams, and leadership "
  "that protects time for it."),
 desc_sig=("Signature QI infrastructure provides every clinic with live outcome and operations "
  "dashboards plus a change-testing toolkit, making improvement a default capability rather than a "
  "special project."),
 how_pub=("Clinics choose an aim, form a small team, and map the current process. They test one "
  "change at a time on a small scale, study the data, and either adopt, adapt, or abandon. Wins "
  "spread across the organization; dashboards keep gains visible."),
 how_sig=("Signature change-testing toolkits standardize the experiment cycle so teams spend energy "
  "on ideas, not on inventing method."),
 keys=["Pick a problem, test a change small, measure, spread",
  "Plan-Do-Study-Act cycles structure experimentation",
  "Goal: better care here and now",
  "Staff-led with leadership protection of time",
  "Dashboards keep gains visible",
  "QI is a routine, not a project"],
 reqs=["Aim-setting and team structure",
  "Data for rapid-cycle measurement",
  "Leadership sponsorship and protected time"],
 stds=["Institute for Healthcare Improvement methods (public)",
  "Accreditation QI expectations (public)"],
 cites=["Institute for Healthcare Improvement — QI resources (public)",
  "Agency for Healthcare Research and Quality — QI guidance (public)"],
 demo=("outcome", {"label": "No-show rate", "pre": 28, "post": 12})),

dict(title="Workforce Training and Supervision", tier=A,
 desc_pub=("A capable workforce needs pipelines and support: university partnerships, internships, "
  "certification programs (including peer certification), ongoing training in evidence-based "
  "practices, and reflective supervision. Burnout - driven by high caseloads, trauma exposure, and "
  "administrative burden - is the field's chronic workforce threat.\n"
  "Retention strategies that work: manageable caseloads, quality supervision, competitive "
  "compensation, career ladders, and cultures that treat staff well-being as a clinical asset. "
  "Workforce data - vacancy, turnover, time-to-fill - belongs on leadership dashboards."),
 desc_sig=("Signature workforce systems forecast demand by service line and track training "
  "pipelines against it, so shortages are addressed before they become access crises."),
 how_pub=("Organizations map workforce needs, build training pipelines with academic partners, and "
  "deliver onboarding plus ongoing evidence-based-practice training. Supervisors provide reflective, "
  "skills-focused supervision. Leaders review workforce metrics quarterly and act on retention "
  "signals."),
 how_sig=("Signature demand forecasting links service growth plans to hiring and training timelines."),
 keys=["Pipelines: universities, internships, certification, peer certification",
  "Ongoing training in evidence-based practices",
  "Reflective supervision as a retention tool",
  "Burnout drivers: caseloads, trauma exposure, admin burden",
  "Retention: caseloads, pay, supervision, ladders, culture",
  "Workforce metrics on leadership dashboards"],
 reqs=["Academic and training partnerships",
  "Qualified supervisors with protected time",
  "Workforce data tracking"],
 stds=["State licensure supervision requirements (public)",
  "Accreditation training expectations (public)"],
 cites=["Substance Abuse and Mental Health Services Administration — workforce resources (public)",
  "Health Resources and Services Administration — behavioral health workforce (public)"],
 demo=("outcome", {"label": "Annual clinician retention", "pre": 71, "post": 88})),

dict(title="Digital Therapeutics and Apps", tier=A,
 desc_pub=("Digital therapeutics are software-based interventions - apps and online programs "
  "delivering structured therapy content, sometimes FDA-authorized for specific conditions. They "
  "extend care between visits, reach the reluctant, and scale where clinicians are scarce.\n"
  "Quality varies wildly: thousands of wellness apps make unproven claims. Responsible use means "
  "choosing tools with evidence, integrating them into a care plan with human oversight, and "
  "protecting data privacy. Apps augment care; they do not replace relationships."),
 desc_sig=("Signature digital integration prescribes apps the way clinicians prescribe homework: "
  "matched to the treatment plan, monitored for use and benefit, and reviewed at visits."),
 how_pub=("Clinicians select evidence-backed tools fitting the client's plan and tech access, "
  "onboard the client, and review app data at sessions to guide care. Privacy policies are "
  "checked; clients are told what data the app collects. Outcomes determine whether the tool stays."),
 how_sig=("Signature app formularies list vetted tools by condition with evidence ratings, so "
  "selection is quick and defensible."),
 keys=["Software delivering structured therapeutic content",
  "Some are FDA-authorized for specific conditions",
  "Extend care between visits; reach the reluctant",
  "Quality varies - choose tools with evidence",
  "Integrate with human oversight",
  "Protect data privacy; augment, don't replace"],
 reqs=["Vetted app formulary with evidence ratings",
  "Client tech access and onboarding",
  "Privacy review of data practices"],
 stds=["FDA digital-health guidance (public)",
  "App evaluation frameworks (public literature, e.g., APA app evaluation)"],
 cites=["U.S. Food and Drug Administration — digital health (public)",
  "American Psychiatric Association — app evaluation resources (public)"],
 demo=("outcome", {"label": "Clients actively using prescribed tool at 8 weeks", "pre": 41, "post": 67})),

dict(title="The Future of Accessible Care", tier=A,
 desc_pub=("The future of mental health care points toward access without friction: same-week "
  "options everywhere, seamless step-up and step-down, care embedded in primary care/schools/"
  "workplaces, digital tools extending human care, and payment rewarding outcomes rather than "
  "visits. Predictive outreach may flag risk early - with fairness safeguards.\n"
  "The through-line is dignity at scale: systems that meet people where they are, honor their "
  "goals, and prove they help. This database's Signature edition prototypes the knowledge core "
  "such systems need."),
 desc_sig=("The Signature future-state is a mental-health operating system: one access front door, "
  "one pathway engine, one outcome spine - on which every provider and client collaborates. This "
  "database is a prototype of that system's knowledge core."),
 how_pub=("Systems consolidate access points, deploy collaborative and stepped models broadly, "
  "integrate digital tools with human oversight, and shift contracts toward outcomes. Equity "
  "monitoring ensures innovations reach marginalized groups first, not last."),
 how_sig=("Signature's operating-system vision makes today's advanced practices - pathways, "
  "governed sharing, outcome accountability - the default infrastructure."),
 keys=["Same-week access everywhere",
  "Care embedded where people already are",
  "Digital tools extending human care",
  "Payment rewarding outcomes",
  "Predictive outreach with fairness safeguards",
  "Equity: innovations reach marginalized groups first"],
 reqs=["Consolidated access infrastructure",
  "Outcome-based payment models",
  "Equity monitoring of innovations"],
 stds=["Emerging standards for ethical AI in mental health (public literature)"],
 cites=["National Institute of Mental Health — strategic priorities (public)",
  "World Health Organization — mental health action plan (public)"],
 demo=("outcome", {"label": "People receiving needed care within 7 days", "pre": 36, "post": 79})),
]
