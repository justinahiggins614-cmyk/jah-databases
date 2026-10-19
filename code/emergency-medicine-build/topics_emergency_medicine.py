#!/usr/bin/env python3
"""Topics + config for the emergency-medicine pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never medical advice. No dosages.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "emergency-medicine",
    "name_pub": "The Emergency Medicine Database",
    "name_sig": "Signature Emergency Medicine Database",
    "tagline_pub": ("Emergency medicine from the ground up: dispatch and triage, ambulance "
                    "operations, emergency protocols, trauma and cardiac response, mass-casualty "
                    "operations, and continuity of care - every record carrying the full entry "
                    "taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of emergency medicine: the same "
                    "real emergency-care knowledge carried forward, plus Signature-built response "
                    "models, triage systems, and continuity frameworks original to this system."),
    "record_kind": "emergency medicine record",
    "record_kind_plural": "emergency medicine records",
    "prefix_pub": "JAH-EMED-", "prefix_sig": "JAH-EMEDS-",
    "ai_pub": "JAH Emergency Medicine Archivist",
    "ai_sig": "JAH Signature Emergency Medicine Creator",
    "role_pub": ("emergency medicine archivist - teaching dispatch, triage, ambulance operations, "
                 "emergency protocols, and continuity of care; answers from many angles - "
                 "definition, example, process, protocol, system - using only archive data from "
                 "this system"),
    "role_sig": ("Signature creator of emergency medicine systems - designing response models, "
                 "triage frameworks, and continuity systems as original Signature works; answers "
                 "from many angles using only archive data from this system"),
    "search_ph": "Search dispatch, triage, ambulance, protocols, trauma, continuity...",
    "chat_ph": "Ask about emergency medicine...",
    "greet_pub": ("I am the JAH Emergency Medicine Archivist. Ask me about dispatch, triage, "
                  "ambulance operations, protocols, and continuity of care. Educational "
                  "information only - in a real emergency, call your local emergency number."),
    "greet_sig": ("I am the JAH Signature Emergency Medicine Creator. Ask me about "
                  "Signature-built emergency response systems. Educational information only."),
    "gen_blurb": ("Generate clearly-labeled emergency medicine studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded emergency medicine records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. "
                      "Educational information only — not medical advice. In a real emergency, call "
                      "your local emergency number."),
    "demo_kind": "emergency-demo",
    "demo_title": "Emergency Medicine Demo",
    "health": True,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Emergency Medicine Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "triage":
        return fill(
            "patients = @@PTS@@\n"
            "order = {'immediate': 0, 'urgent': 1, 'delayed': 2, 'minor': 3}\n"
            "ranked = sorted(patients, key=lambda x: order[x['priority']])\n"
            "print('Triage order (most urgent first):')\n"
            "for i, pt in enumerate(ranked, 1):\n"
            "    print(' %d. %s — %s' % (i, pt['id'], pt['priority']))\n",
            {"PTS": p["patients"]})
    if v == "dispatch":
        return fill(
            "calls = @@CALLS@@\n"
            "units = @@UNITS@@\n"
            "rank = {'P1': 0, 'P2': 1, 'P3': 2}\n"
            "calls_sorted = sorted(calls, key=lambda c: rank[c['priority']])\n"
            "print('Dispatch order:')\n"
            "for i, c in enumerate(calls_sorted):\n"
            "    unit = units[i % len(units)] if units else 'NO UNIT'\n"
            "    print(' %s (%s) -> %s' % (c['id'], c['priority'], unit))\n",
            {"CALLS": p["calls"], "UNITS": p["units"]})
    if v == "protocol":
        return fill(
            "steps = @@STEPS@@\n"
            "print('Protocol steps:')\n"
            "for i, s in enumerate(steps, 1):\n"
            "    print(' %d. %s' % (i, s))\n"
            "print('Steps:', len(steps))\n",
            {"STEPS": p["steps"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d' % (pre, post, delta))\n"
            "print('Direction:', 'improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged')\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    if v == "response_time":
        return fill(
            "times = @@TIMES@@\n"
            "avg = sum(times) / len(times)\n"
            "under8 = sum(1 for t in times if t <= 8)\n"
            "print('Responses:', len(times))\n"
            "print('Average response: %.1f min' % avg)\n"
            "print('Within 8 min: %d/%d (%.0f%%)' % (under8, len(times), 100.0 * under8 / len(times)))\n",
            {"TIMES": p["times"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Emergency Medicine Is", tier=F,
 desc_pub=("Emergency medicine is the specialty devoted to immediate care for acute illness and "
  "injury: heart attacks, strokes, trauma, breathing emergencies, overdoses, and anything that "
  "cannot wait. It spans the 911 call, field care by paramedics and EMTs, and hospital emergency "
  "departments - a chain where every link must work.\n"
  "The specialty's ethic is universality: emergency departments evaluate everyone who comes, "
  "regardless of ability to pay (a U.S. requirement under EMTALA). Speed, prioritization, and "
  "teamwork under pressure define the practice."),
 desc_sig=("The Signature system models emergency care as a time-critical service chain - call, "
  "dispatch, field care, transport, ED, handoff - with each link's performance measured and "
  "improved as one system rather than separate fiefdoms."),
 how_pub=("A person calls the emergency number; dispatchers triage the call and send the right "
  "resources. Field crews assess, stabilize, and transport to the appropriate hospital. The ED "
  "team triages, diagnoses, treats, and then admits, observes, or discharges with follow-up. "
  "Information handoffs connect each link."),
 how_sig=("Signature chain measurement tracks times and handoffs across all links, exposing the "
  "weakest link for targeted improvement."),
 keys=["Immediate care for acute illness and injury",
  "Chain: call, dispatch, field care, transport, ED, handoff",
  "Everyone evaluated regardless of ability to pay (EMTALA)",
  "Speed, prioritization, teamwork under pressure",
  "Every link must work",
  "Educational record; real emergencies need professionals"],
 reqs=["Emergency access number and dispatch",
  "Field EMS and receiving EDs",
  "Handoff protocols between links"],
 stds=["EMTALA (public law)",
  "State EMS system regulations"],
 cites=["American College of Emergency Physicians — public resources (public)",
  "National Highway Traffic Safety Administration — EMS (public)"],
 demo=("protocol", {"steps": ["Call answered and located", "Dispatcher triage",
   "Right resources sent", "Field assessment and stabilization",
   "Transport to appropriate hospital", "ED triage and treatment", "Handoff to next care"]})),

dict(title="When to Call Emergency Services", tier=F,
 desc_pub=("Call emergency services for signs of serious trouble: chest pain or pressure, trouble "
  "breathing, stroke signs (face droop, arm weakness, speech difficulty - act FAST), severe "
  "bleeding, head injury with confusion, seizures, severe allergic reaction, overdose, suicidal "
  "crisis, or any situation where someone might die without rapid help.\n"
  "When in doubt, call: dispatchers would rather triage a non-emergency than miss a real one. "
  "Teach children the local emergency number early, and post it where caregivers can see it."),
 desc_sig=("Signature public education pairs the warning-sign list with a simple decision aid - "
  "call, urgent care, or routine - so hesitation never costs critical minutes."),
 how_pub=("The caller dials the emergency number, stays on the line, and answers the dispatcher's "
  "questions: location first, then what is happening. They follow instructions (including "
  "dispatcher-guided CPR), keep the phone free, and send someone to flag down responders if "
  "possible."),
 how_sig=("Signature decision aids shorten the hesitate-or-call dilemma with plain criteria."),
 keys=["Chest pain, breathing trouble, stroke signs, severe bleeding, overdose",
  "Act FAST for stroke: Face, Arms, Speech, Time",
  "When in doubt, call",
  "Location first, then what is happening",
  "Follow dispatcher instructions",
  "Teach children the number early"],
 reqs=["Knowledge of warning signs",
  "Posted emergency numbers",
  "Willingness to call when unsure"],
 stds=["Public education standards for emergency recognition (public literature)"],
 cites=["American Heart Association — warning signs (public)",
  "Centers for Disease Control — emergency preparedness (public)"],
 demo=("triage", {"patients": [
   {"id": "Caller A: chest pain", "priority": "immediate"},
   {"id": "Caller B: sprained ankle", "priority": "minor"},
   {"id": "Caller C: stroke signs", "priority": "immediate"},
   {"id": "Caller D: fever, stable", "priority": "delayed"}]})),

dict(title="The Emergency Call and Dispatch", tier=F,
 desc_pub=("Emergency dispatch is the system's front door and brain: call-takers gather location, "
  "nature of the emergency, and hazards; dispatchers choose and send police, fire, or EMS "
  "resources by priority. Modern centers use emergency medical dispatch (EMD) protocols - "
  "scripted questions that determine response priority and give pre-arrival instructions like CPR "
  "or choking relief.\n"
  "Location technology (including phone-based location) and text-to-911 expand access. The "
  "dispatcher's calm, structured questioning saves lives before any unit arrives."),
 desc_sig=("Signature dispatch design pairs protocol scripts with decision-support scoring, so "
  "priority assignment is consistent across call-takers and shift changes."),
 how_pub=("The call-taker answers, confirms location, and runs the EMD protocol: key questions "
  "determine the priority level. The dispatcher assigns the closest appropriate units; the "
  "call-taker stays on the line giving instructions until help arrives. All of it is recorded "
  "and reviewed for quality."),
 how_sig=("Signature protocol adherence is measured per call, with coaching closing gaps - "
  "consistency engineered, not hoped for."),
 keys=["Call-takers gather; dispatchers send",
  "EMD protocols script questions and priorities",
  "Pre-arrival instructions: CPR, choking, bleeding control",
  "Location first, always",
  "Text-to-911 expands access",
  "Calls recorded and quality-reviewed"],
 reqs=["EMD protocol system",
  "Location technology",
  "Quality-review program"],
 stds=["State 911 and EMD standards (public)",
  "APCO/NENA standards (public)"],
 cites=["National Emergency Number Association — standards (public)",
  "Federal Communications Commission — 911 resources (public)"],
 demo=("dispatch", {"calls": [
   {"id": "Call-101 cardiac arrest", "priority": "P1"},
   {"id": "Call-102 fall, minor", "priority": "P3"},
   {"id": "Call-103 breathing difficulty", "priority": "P1"},
   {"id": "Call-104 lift assist", "priority": "P3"}],
  "units": ["Medic-1", "Medic-2"]})),

dict(title="Emergency Medical Services Levels", tier=F,
 desc_pub=("EMS providers train to defined levels: Emergency Medical Responders (basic first "
  "response), EMTs (basic life support - assessment, CPR, bleeding control, some medications), "
  "Advanced EMTs (additional skills including IVs), and Paramedics (advanced life support - "
  "cardiac monitoring, advanced airway, many medications).\n"
  "Systems dispatch the right level to the call's severity and transport patients to the right "
  "hospital - trauma centers, stroke centers, cardiac centers - because the right destination "
  "matters as much as speed."),
 desc_sig=("Signature EMS design matches crew level and hospital destination to call severity by "
  "protocol, so the sickest patients reliably get the highest capability."),
 how_pub=("Dispatch protocols assign BLS or ALS resources by call type. Crews assess on scene, "
  "deliver care within their scope, and choose destination by protocol - trauma to trauma "
  "centers, strokes to stroke centers. Patient care reports document everything for the "
  "receiving team and quality review."),
 how_sig=("Signature destination protocols are audited per transport, keeping the right-patient/"
  "right-hospital match high."),
 keys=["EMR, EMT, Advanced EMT, Paramedic - increasing scope",
  "BLS vs ALS matched to call severity",
  "Right hospital matters as much as speed",
  "Trauma, stroke, cardiac centers by protocol",
  "Patient care reports document everything",
  "Educational record; field care by professionals"],
 reqs=["State EMS licensure per level",
  "Scope-of-practice protocols",
  "Destination protocols with specialty centers"],
 stds=["National EMS Scope of Practice Model (public)",
  "State EMS regulations"],
 cites=["National Highway Traffic Safety Administration — EMS scope (public)",
  "National Registry of EMTs — certification levels (public)"],
 demo=("dispatch", {"calls": [
   {"id": "Call-201 chest pain", "priority": "P1"},
   {"id": "Call-202 interfacility transfer", "priority": "P3"}],
  "units": ["ALS Medic-3", "BLS Ambulance-7"]})),

dict(title="The Emergency Department Team", tier=F,
 desc_pub=("The ED team is built for parallel work under pressure: emergency physicians lead "
  "diagnosis and resuscitation; nurses triage, medicate, and monitor; techs and scribes handle "
  "tasks and documentation; respiratory therapists manage airways; pharmacists verify high-risk "
  "medications; social workers and case managers arrange follow-up.\n"
  "Teamwork is trained, not assumed: closed-loop communication, defined roles in resuscitations, "
  "and briefings before and debriefings after critical cases keep the team sharp."),
 desc_sig=("Signature ED teamwork standardizes role cards and communication protocols for "
  "resuscitations, so any assembled team performs like a practiced one."),
 how_pub=("Patients are triaged on arrival and assigned by acuity. Physicians and nurses work in "
  "pods or zones; critical patients get full team resuscitation with defined roles. The team "
  "reassesses continuously, consults specialists, and dispositions each patient: admit, observe, "
  "or discharge with instructions and follow-up."),
 how_sig=("Signature resuscitation role cards assign every position before the patient arrives."),
 keys=["Physicians, nurses, techs, respiratory, pharmacy, social work",
  "Parallel work under pressure",
  "Closed-loop communication",
  "Defined resuscitation roles",
  "Brief before, debrief after",
  "Disposition: admit, observe, discharge with follow-up"],
 reqs=["24-hour physician and nursing coverage",
  "Resuscitation equipment and defined roles",
  "Specialist consultation access"],
 stds=["EMTALA evaluation requirements (public law)",
  "Trauma/stroke/cardiac center standards where designated"],
 cites=["American College of Emergency Physicians — public resources (public)",
  "Emergency Nurses Association — public resources (public)"],
 demo=("triage", {"patients": [
   {"id": "Patient 1: cardiac arrest", "priority": "immediate"},
   {"id": "Patient 2: broken arm", "priority": "delayed"},
   {"id": "Patient 3: severe asthma", "priority": "urgent"}]})),

dict(title="Triage Basics", tier=F,
 desc_pub=("Triage sorts patients by urgency so the sickest are seen first. In EDs, the Emergency "
  "Severity Index (ESI) assigns levels 1 (immediate, life-threatening) through 5 (minor, few "
  "resources needed) based on acuity and expected resource needs. In mass-casualty field triage, "
  "START sorts into immediate, delayed, minor, and expectant.\n"
  "Triage is dynamic: patients are re-triaged as conditions change. Under-triage kills; over-"
  "triage wastes scarce capacity. Good triage is the ED's most leveraged skill."),
 desc_sig=("Signature triage support embeds the ESI and START algorithms in the workflow with "
  "re-triage timers, so sorting stays accurate as conditions evolve."),
 how_pub=("A triage nurse assesses each arrival: vital signs, chief complaint, pain, risk factors. "
  "The ESI level is assigned, documented, and communicated; waiting patients are re-checked on a "
  "schedule. In field mass-casualty, responders tag patients by START category and transport by "
  "priority."),
 how_sig=("Signature re-triage timers prompt reassessment before deterioration goes unnoticed in "
  "the waiting room."),
 keys=["Sort by urgency: sickest first",
  "ESI levels 1-5 in the ED",
  "START categories in field mass-casualty",
  "Triage is dynamic - re-assess",
  "Under-triage kills; over-triage wastes",
  "Most leveraged skill in the ED"],
 reqs=["Trained triage nurses",
  "Triage protocol (ESI/START)",
  "Re-triage schedule for waiting patients"],
 stds=["ESI implementation handbook (public, AHRQ)",
  "START triage protocol (public)"],
 cites=["Agency for Healthcare Research and Quality — ESI handbook (public)",
  "U.S. Dept. of Homeland Security — START guidance (public)"],
 demo=("triage", {"patients": [
   {"id": "P-A: unresponsive", "priority": "immediate"},
   {"id": "P-B: deep laceration, stable", "priority": "urgent"},
   {"id": "P-C: ankle sprain", "priority": "minor"},
   {"id": "P-D: abdominal pain, stable vitals", "priority": "delayed"}]})),

dict(title="Patient Assessment in the Field", tier=F,
 desc_pub=("Field assessment follows a disciplined sequence: scene safety first, then the primary "
  "survey - airway, breathing, circulation, disability (neurologic), exposure - fixing "
  "life threats as found. The secondary survey takes history (SAMPLE: signs, allergies, meds, "
  "past history, last intake, events) and performs a head-to-toe exam.\n"
  "The discipline prevents fixation: treat the airway before admiring the fracture. Reassessment "
  "en route catches deterioration. This record is educational; assessment is professional "
  "practice."),
 desc_sig=("Signature field assessment runs as a checklist workflow on the crew's device, with "
  "abnormal findings auto-flagged for the receiving hospital."),
 how_pub=("Crews secure the scene, run the primary survey with immediate interventions, then the "
  "secondary survey with SAMPLE history and full exam. Findings drive treatment and destination "
  "decisions; vitals and reassessment continue en route; the radio report prepares the ED."),
 how_sig=("Signature checklist workflows ensure no step is skipped under pressure, and findings "
  "flow to the hospital before arrival."),
 keys=["Scene safety first",
  "Primary survey: ABCDE, fix as you go",
  "Secondary: SAMPLE history, head-to-toe",
  "Treat life threats before details",
  "Reassess en route",
  "Radio report prepares the ED"],
 reqs=["Assessment protocol training",
  "Equipment for full survey",
  "Reassessment discipline"],
 stds=["National EMS education standards (public)",
  "PHTLS/ITLS assessment frameworks (public)"],
 cites=["National Association of EMTs — PHTLS resources (public)"],
 demo=("protocol", {"steps": ["Scene safety", "Primary survey ABCDE",
   "Immediate life-threat interventions", "SAMPLE history", "Secondary head-to-toe exam",
   "Treatment and destination decision", "Reassessment en route", "Radio report to ED"]})),

dict(title="Ambulance Equipment", tier=F,
 desc_pub=("Ambulances are rolling emergency rooms carrying airway equipment, oxygen, cardiac "
  "monitors and defibrillators, bleeding-control supplies, splints, stretchers, medications "
  "(scope-dependent), and communications gear. ALS units add advanced airway tools, IV supplies, "
  "and a wider drug box.\n"
  "Readiness is the discipline: rig checks at shift start verify every item present, functional, "
  "and unexpired. An ambulance with a dead defibrillator battery is just a van."),
 desc_sig=("Signature fleet readiness tracks every unit's checks, expirations, and deficiencies "
  "digitally, so no rig rolls with unknown gaps."),
 how_pub=("Crews complete standardized rig checks at shift start - testing monitors, counting "
  "medications, checking expirations. Deficiencies are fixed before the unit goes in service; "
  "usage during calls triggers restocking. Supervisors audit checks regularly."),
 how_sig=("Signature digital checklists with expiration tracking prevent the dead-battery "
  "ambulance."),
 keys=["Airway, oxygen, monitors, defibrillation, bleeding control, splints, meds",
  "ALS adds advanced airway, IVs, wider drug box",
  "Rig checks every shift start",
  "Verify present, functional, unexpired",
  "Restock after every use",
  "Audit checks regularly"],
 reqs=["Standardized rig-check lists",
  "Equipment per scope of service",
  "Restocking and maintenance program"],
 stds=["State ambulance equipment requirements (public)",
  "CAAS accreditation standards (public)"],
 cites=["Commission on Accreditation of Ambulance Services — standards (public)"],
 demo=("protocol", {"steps": ["Exterior and fuel check", "Test cardiac monitor/defibrillator",
   "Verify airway kit complete", "Count and check medications/expirations",
   "Check oxygen levels", "Test communications", "Document and correct deficiencies"]})),

dict(title="Communication During Emergencies", tier=F,
 desc_pub=("Emergency communication has three audiences: the patient and family (clear, calm, "
  "honest updates), the team (closed-loop, structured handoffs like SBAR: Situation, Background, "
  "Assessment, Recommendation), and the public (accurate information during disasters).\n"
  "With patients, the principles are plain language, frequent updates during waits, and "
  "compassionate delivery of bad news. With teams, structure prevents the misunderstandings that "
  "harm patients."),
 desc_sig=("Signature emergency communication standardizes handoff tools across the whole chain - "
  "field to ED to inpatient - so information survives every transfer intact."),
 how_pub=("Crews use SBAR for radio reports and bedside handoffs; ED teams brief before "
  "resuscitations and debrief after. Staff update waiting patients and families on a schedule. "
  "Public information officers handle disaster messaging with verified facts."),
 how_sig=("Signature chain-wide handoff standards make every transfer - dispatch to field to ED "
  "to floor - equally reliable."),
 keys=["Three audiences: patient/family, team, public",
  "SBAR structures clinical handoffs",
  "Closed-loop communication in teams",
  "Plain language and frequent updates for families",
  "Compassionate bad-news delivery",
  "Verified facts for public messaging"],
 reqs=["Handoff protocol training",
  "Family-update routines",
  "Public information procedures"],
 stds=["Patient-safety communication standards (public literature)",
  "NIMS public information guidance (public)"],
 cites=["Agency for Healthcare Research and Quality — TeamSTEPPS (public)",
  "Federal Emergency Management Agency — NIMS (public)"],
 demo=("protocol", {"steps": ["Situation: who and what", "Background: relevant history",
   "Assessment: current findings", "Recommendation: what is needed",
   "Read-back confirmation"]})),

dict(title="Patient Rights in Emergencies (EMTALA)", tier=F,
 desc_pub=("EMTALA - the Emergency Medical Treatment and Labor Act - requires hospital emergency "
  "departments to provide a medical screening exam to everyone who comes, and to stabilize "
  "emergency conditions regardless of ability to pay or insurance status. Hospitals may not turn "
  "away or delay screening for financial reasons.\n"
  "Patients also retain rights to informed consent (to the extent possible), to have family "
  "notified, to refuse treatment, and to receive care without discrimination. Knowing these rights "
  "matters most for the vulnerable."),
 desc_sig=("Signature rights protection embeds EMTALA compliance checks into triage and registration "
  "workflows, so financial processes can never precede or delay screening."),
 how_pub=("On arrival, patients receive screening without financial pre-conditions; registration "
  "for payment follows the medical exam. Staff explain what is happening and obtain consent where "
  "possible. Concerns about violations can be reported to CMS or the hospital's compliance office."),
 how_sig=("Signature workflow ordering guarantees screening before any financial discussion, by "
  "system design."),
 keys=["Screening exam for everyone who comes",
  "Stabilize emergencies regardless of ability to pay",
  "No financial screening before medical screening",
  "Informed consent, family notification, refusal rights",
  "Care without discrimination",
  "Violations reportable to CMS"],
 reqs=["EMTALA-compliant triage and registration workflows",
  "Staff training on obligations",
  "Compliance reporting channel"],
 stds=["EMTALA statute and CMS interpretive guidance (public law)"],
 cites=["Centers for Medicare and Medicaid Services — EMTALA guidance (public)"],
 demo=("protocol", {"steps": ["Medical screening exam first", "Stabilize emergency conditions",
   "Financial registration only after screening", "Document consent and decisions",
   "Report concerns to compliance"]})),

dict(title="After the Emergency: Follow-up Care", tier=F,
 desc_pub=("Emergency care ends; recovery continues. Follow-up includes understanding discharge "
  "instructions (diagnosis, medications, warning signs, return precautions), filling prescriptions, "
  "seeing primary care or specialists, completing referrals, and watching for complications.\n"
  "The highest-risk moment is the transition: unclear instructions cause half of post-ED "
  "problems. Teach-back - asking patients to explain instructions in their own words - catches "
  "misunderstanding before discharge."),
 desc_sig=("Signature discharge design pairs plain-language instructions with teach-back "
  "verification and automated follow-up scheduling, closing the transition gap."),
 how_pub=("Before discharge, staff deliver written and verbal instructions, use teach-back to "
  "verify understanding, fill or e-prescribe medications, and schedule follow-up appointments. "
  "High-risk patients get follow-up calls within days; all get clear return precautions."),
 how_sig=("Signature teach-back verification is a required discharge step, not an optional "
  "nicety."),
 keys=["Discharge instructions: diagnosis, meds, warnings, return precautions",
  "Transitions are the highest-risk moment",
  "Teach-back verifies understanding",
  "Fill prescriptions before leaving if possible",
  "Schedule follow-up before discharge",
  "Follow-up calls for high-risk patients"],
 reqs=["Plain-language discharge materials",
  "Teach-back protocol",
  "Follow-up scheduling before discharge"],
 stds=["Discharge-planning best practices (public literature)"],
 cites=["Agency for Healthcare Research and Quality — discharge resources (public)"],
 demo=("outcome", {"label": "Patients understanding discharge instructions", "pre": 58, "post": 90})),

# ---------------- Compounded (12) ----------------
dict(title="Dispatch Operations and Protocols", tier=C,
 desc_pub=("Dispatch centers operate 24/7 with redundant systems: call-taking, radio dispatch, "
  "mapping and AVL (automatic vehicle location), and EMD protocols. Staffing, training, and "
  "quality assurance determine performance - along with technology for location accuracy and "
  "interoperability.\n"
  "Key metrics: time to answer, time to dispatch, EMD protocol compliance, and pre-arrival "
  "instruction rates. Accreditation (e.g., ACE - Accredited Center of Excellence) marks mature "
  "operations."),
 desc_sig=("Signature dispatch operations integrate call, location, unit, and protocol data on "
  "one screen with performance dashboards, so supervisors manage by evidence in real time."),
 how_pub=("Calls flow to trained call-takers running EMD protocols; dispatchers assign units by "
  "proximity, capability, and priority. Supervisors monitor queues and surge staffing for major "
  "incidents. Every call is recorded; random samples are scored for protocol compliance with "
  "feedback to staff."),
 how_sig=("Signature real-time dashboards show queue, compliance, and unit status together, "
  "enabling evidence-based supervision."),
 keys=["24/7 with redundant systems",
  "Call-taking, radio, AVL, EMD protocols",
  "Metrics: answer time, dispatch time, compliance",
  "Quality assurance on recorded calls",
  "Accreditation marks maturity",
  "Surge staffing for major incidents"],
 reqs=["EMD-certified staff",
  "Redundant communications and power",
  "QA program with feedback"],
 stds=["NENA/APCO operational standards (public)",
  "IAED Accredited Center of Excellence criteria (public)"],
 cites=["International Academies of Emergency Dispatch — standards (public)"],
 demo=("response_time", {"times": [4.2, 6.1, 5.5, 7.8, 3.9, 8.4, 5.1, 6.7]})),

dict(title="Triage Systems: ESI and START", tier=C,
 desc_pub=("The Emergency Severity Index (ESI) sorts ED patients into five levels using acuity plus "
  "expected resource needs: level 1 needs immediate life-saving intervention; level 2 is high-"
  "risk; levels 3-5 need decreasing resources. It predicts flow as well as urgency.\n"
  "START (Simple Triage and Rapid Treatment) sorts mass-casualty field patients in under a minute "
  "each: respirations, perfusion, mental status determine immediate (red), delayed (yellow), minor "
  "(green), or expectant (black) tags. JumpSTART adapts it for children."),
 desc_sig=("Signature triage tooling embeds both algorithms with timers and prompts, keeping "
  "sorting fast, consistent, and re-checked."),
 how_pub=("ED triage nurses apply the ESI decision algorithm at arrival and document the level; "
  "charge nurses use levels to manage flow. In mass casualty, first responders apply START rapidly "
  "down the line of patients, tagging and moving on - treatment comes after sorting."),
 how_sig=("Signature embedded algorithms with re-triage prompts keep both systems accurate under "
  "load."),
 keys=["ESI: 5 levels, acuity + resource needs",
  "Level 1 immediate; level 5 minor",
  "START: under-a-minute field sorting",
  "Red/yellow/green/black tags",
  "JumpSTART for children",
  "Sort first, treat after (mass casualty)"],
 reqs=["ESI-trained triage nurses",
  "START-trained field responders",
  "Triage tags and documentation"],
 stds=["AHRQ ESI handbook (public)",
  "START/JumpSTART protocols (public)"],
 cites=["Agency for Healthcare Research and Quality — ESI (public)"],
 demo=("triage", {"patients": [
   {"id": "T-1: not breathing after airway opened", "priority": "immediate"},
   {"id": "T-2: breathing 28, radial pulse present", "priority": "urgent"},
   {"id": "T-3: walking wounded", "priority": "minor"},
   {"id": "T-4: stable fracture", "priority": "delayed"}]})),

dict(title="Ambulance Operations and Fleet", tier=C,
 desc_pub=("Ambulance operations balance coverage, readiness, and cost: station placement for "
  "response-time targets, dynamic deployment (moving units to predicted demand), fleet maintenance, "
  "and crew scheduling that manages fatigue. System status management repositions ambulances as "
  "calls deplete coverage.\n"
  "Response-time standards (often 8:59 for life-threatening calls in urban areas) drive design. "
  "Data - call volumes by hour and zone - optimizes stationing far better than tradition."),
 desc_sig=("Signature fleet operations use demand forecasting to pre-position units, turning "
  "response-time performance from reactive to predictive."),
 how_pub=("Planners analyze call data to site stations and schedule crews; dispatchers deploy by "
  "proximity and system-status plans. Fleet managers maintain vehicles on preventive schedules; "
  "operations chiefs review response times, unit-hour utilization, and crew fatigue metrics "
  "weekly."),
 how_sig=("Signature demand forecasting pre-positions units before the predicted surge, not "
  "after."),
 keys=["Coverage, readiness, cost in balance",
  "Dynamic deployment to predicted demand",
  "Response-time standards drive design",
  "Data beats tradition for stationing",
  "Fatigue management is safety management",
  "Preventive fleet maintenance"],
 reqs=["Call-data analysis capability",
  "System status plans",
  "Fatigue-aware scheduling"],
 stds=["CAAS accreditation standards (public)",
  "NFPA 1710 response-time objectives (public)"],
 cites=["Commission on Accreditation of Ambulance Services (public)",
  "National Fire Protection Association — 1710 (public)"],
 demo=("response_time", {"times": [7.2, 8.8, 6.5, 9.4, 7.9, 8.1, 6.8, 10.2]})),

dict(title="Air Medical Transport", tier=C,
 desc_pub=("Helicopter and fixed-wing air ambulances serve time-critical patients far from "
  "specialty care: severe trauma, stroke, heart attack, high-risk obstetrics, and neonatal "
  "emergencies. Crews - typically flight nurse/paramedic with advanced scope - deliver ICU-level "
  "care en route.\n"
  "Appropriate use is the discipline: air transport helps when it meaningfully shortens time to "
  "definitive care or brings capability ground units lack. Weather, safety, and cost demand "
  "careful triage of flights themselves."),
 desc_sig=("Signature air-medical dispatch uses time-benefit calculation - ground time vs flight "
  "time to definitive care - so launch decisions are evidence-based."),
 how_pub=("Field or hospital providers request air transport by protocol; dispatch checks weather, "
  "aircraft availability, and landing zones. Flight crews assess, stabilize with advanced "
  "interventions, and deliver directly to specialty centers with in-flight handoff reports."),
 how_sig=("Signature time-benefit calculators make the fly-or-drive decision transparent and "
  "consistent."),
 keys=["Time-critical patients far from specialty care",
  "Flight nurse/paramedic crews, ICU-level en route",
  "Helps when it shortens time to definitive care",
  "Weather and safety gate every flight",
  "Appropriate use is the discipline",
  "Direct delivery to specialty centers"],
 reqs=["Aircraft with medical configuration",
  "Flight-crew advanced scope protocols",
  "Landing-zone and weather procedures"],
 stds=["CAMTS accreditation standards (public)",
  "State air-medical regulations"],
 cites=["Commission on Accreditation of Medical Transport Systems (public)"],
 demo=("outcome", {"label": "Scene-to-specialty-center time, minutes (lower better)", "pre": 78, "post": 41})),

dict(title="Cardiac Emergency Protocols", tier=C,
 desc_pub=("Cardiac emergency protocols choreograph the response to chest pain, heart attack, and "
  "cardiac arrest. For ST-elevation heart attacks, the goal is balloon (door-to-balloon) within 90 "
  "minutes - via prehospital ECG transmission and cardiac-team activation before arrival. For "
  "cardiac arrest, high-quality CPR with minimal interruptions and early defibrillation save "
  "lives.\n"
  "Systems of care - dispatcher-guided CPR, public AEDs, rapid EMS, cath-lab readiness - multiply "
  "survival. This record is educational; cardiac emergencies need immediate professional "
  "response - call emergency services."),
 desc_sig=("Signature cardiac systems wire prehospital ECG directly to cath-lab activation with "
  "time tracking at every step, squeezing each minute from the chain."),
 how_pub=("Dispatchers give CPR instructions immediately for arrest calls. EMS acquires 12-lead "
  "ECGs, transmits them, and activates cath labs en route for heart attacks. EDs confirm and move "
  "to intervention; post-arrest care includes targeted temperature management per protocol."),
 how_sig=("Signature step-time tracking exposes exactly where minutes are lost in the cardiac "
  "chain."),
 keys=["Door-to-balloon within 90 minutes for STEMI",
  "Prehospital ECG + pre-arrival activation",
  "High-quality CPR, minimal interruptions, early defibrillation",
  "Dispatcher-guided CPR saves lives",
  "Public AEDs multiply survival",
  "Systems of care, not solo heroes"],
 reqs=["12-lead ECG and transmission capability",
  "Cath-lab activation protocols",
  "Community CPR/AED programs"],
 stds=["AHA guidelines for CPR and cardiac care (public)",
  "Mission: Lifeline system standards (public)"],
 cites=["American Heart Association — guidelines (public)"],
 demo=("protocol", {"steps": ["Dispatcher CPR instructions", "EMS 12-lead ECG",
   "Transmit ECG, activate cath lab", "ED confirmation", "Door-to-balloon intervention",
   "Post-arrest protocol care"]})),

dict(title="Stroke Recognition and Response", tier=C,
 desc_pub=("Stroke response is a race against brain loss: 'time is brain.' Recognition uses FAST "
  "(Face drooping, Arm weakness, Speech difficulty, Time to call) plus balance and vision changes. "
  "Ischemic strokes may be treated with clot-busting drugs or thrombectomy within narrow time "
  "windows - making rapid transport to stroke centers critical.\n"
  "Prehospital stroke scales (like RACE or LAMS) help EMS identify large-vessel strokes for direct "
  "transport to thrombectomy-capable centers. This record is educational; suspected stroke needs "
  "immediate emergency response."),
 desc_sig=("Signature stroke systems use severity-scale routing with prenotification, so "
  "thrombectomy teams are ready before the patient arrives."),
 how_pub=("Bystanders recognize FAST signs and call immediately. EMS applies a stroke scale, "
  "records last-known-well time, prenotifies the stroke center, and transports directly to the "
  "appropriate level. Hospitals run code-stroke protocols with door-to-needle and door-to-"
  "puncture time goals."),
 how_sig=("Signature last-known-well capture at first contact protects eligibility for "
  "time-limited treatments."),
 keys=["Time is brain",
  "FAST + balance/vision changes",
  "Record last-known-well time immediately",
  "Prehospital scales route large-vessel strokes",
  "Direct transport to stroke centers",
  "Code-stroke protocols with time goals"],
 reqs=["Public FAST education",
  "Prehospital stroke scales",
  "Stroke-center destination protocols"],
 stds=["AHA/ASA stroke guidelines (public)",
  "Stroke center certification standards"],
 cites=["American Stroke Association — guidelines (public)"],
 demo=("protocol", {"steps": ["Recognize FAST signs", "Call immediately",
   "EMS stroke scale + last-known-well", "Prenotify stroke center",
   "Direct transport", "Code stroke on arrival"]})),

dict(title="Trauma Care Systems", tier=C,
 desc_pub=("Trauma systems organize care for severe injury across a region: prevention, field "
  "triage, transport to designated trauma centers (Level I most comprehensive), and "
  "rehabilitation. Field triage schemes route the severely injured past closer hospitals to "
  "trauma centers - because trauma surgery capability saves lives.\n"
  "In the ED, trauma resuscitation follows ATLS principles: primary survey with immediate "
  "interventions, massive transfusion protocols for hemorrhage, and rapid movement to operating "
  "room or ICU. This record is educational."),
 desc_sig=("Signature trauma systems track the full injury chain - triage accuracy, transport "
  "times, resuscitation performance - as one regional dashboard."),
 how_pub=("EMS applies field triage criteria (physiology, anatomy, mechanism) and transports to "
  "the designated level. Trauma teams assemble before arrival; resuscitation follows the primary "
  "survey with hemorrhage control first. Registries collect data driving prevention and system "
  "improvement."),
 how_sig=("Signature regional dashboards show triage accuracy and outcomes together, guiding "
  "system tuning."),
 keys=["Regional systems: prevention to rehabilitation",
  "Trauma center levels; Level I most comprehensive",
  "Field triage routes severe injury to trauma centers",
  "Hemorrhage control first",
  "Trauma registries drive improvement",
  "Educational record"],
 reqs=["Designated trauma centers",
  "Field triage scheme",
  "Trauma registry"],
 stds=["ACS trauma center verification criteria (public)",
  "CDC field triage guidelines (public)"],
 cites=["American College of Surgeons — trauma resources (public)",
  "Centers for Disease Control — field triage (public)"],
 demo=("triage", {"patients": [
   {"id": "M-1: hypotensive, pelvic fracture", "priority": "immediate"},
   {"id": "M-2: isolated wrist fracture", "priority": "delayed"},
   {"id": "M-3: chest trauma, unstable", "priority": "immediate"}]})),

dict(title="Pediatric Emergency Protocols", tier=C,
 desc_pub=("Children are not small adults in emergencies: different vital-sign ranges, weight-based "
  "dosing, distinct injury patterns, and the need for family-centered care. Broselow tapes and "
  "apps give weight-based equipment sizes and doses by length.\n"
  "Pediatric readiness - right equipment, trained staff, weight-based references - varies widely "
  "among EDs and predicts outcomes. Keeping families present during resuscitation, when they "
  "choose, is now standard. This record is educational."),
 desc_sig=("Signature pediatric readiness standardizes weight-based references and equipment "
  "checks across every ED and ambulance, so children get the same readiness everywhere."),
 how_pub=("Systems stock pediatric equipment and references on every unit; staff train in "
  "pediatric assessment. Doses and equipment sizes come from weight (Broselow or app), double-"
  "checked. Families stay involved; child-life specialists ease fear where available."),
 how_sig=("Signature readiness verification makes pediatric capability a checked item, not an "
  "assumption."),
 keys=["Different vitals, weight-based dosing, distinct injuries",
  "Broselow tapes/apps for equipment and doses",
  "Family-centered care",
  "Pediatric readiness predicts outcomes",
  "Families present during resuscitation if they choose",
  "Double-check pediatric doses"],
 reqs=["Pediatric equipment and references everywhere",
  "Staff pediatric training",
  "Family-presence policies"],
 stds=["AAP pediatric readiness guidelines (public)",
  "ENPC/PALS training standards (public)"],
 cites=["American Academy of Pediatrics — emergency readiness (public)"],
 demo=("protocol", {"steps": ["Pediatric assessment triangle", "Weight via Broselow/app",
   "Weight-based equipment and doses", "Double-check calculations",
   "Family-centered communication", "Reassess frequently"]})),

dict(title="Behavioral Health Emergencies", tier=C,
 desc_pub=("Behavioral health emergencies - suicidal crisis, psychosis, severe agitation - need "
  "medical-emergency seriousness with psychiatric skill. Best practice: de-escalation first, "
  "medical screening for organic causes, least-restrictive setting, and connection to ongoing "
  "care.\n"
  "Dedicated psychiatric emergency services and crisis stabilization units outperform boarding "
  "psychiatric patients in medical EDs. If you or someone you know is in crisis, contact 988 "
  "(US) or local emergency services."),
 desc_sig=("Signature behavioral-emergency design routes crises to purpose-built settings with "
  "follow-up tracking, ending the boarding of psychiatric patients in medical ED hallways."),
 how_pub=("Responders ensure safety, de-escalate verbally, and screen medically. Psychiatric "
  "emergency teams evaluate, stabilize, and arrange the least-restrictive disposition - crisis "
  "unit, intensive outpatient, or inpatient when needed - with follow-up contact scheduled."),
 how_sig=("Signature disposition tracking confirms every behavioral emergency connects to next "
  "care, verified."),
 keys=["De-escalation first",
  "Medical screening for organic causes",
  "Least-restrictive setting",
  "Dedicated psych emergency services outperform boarding",
  "Connect to ongoing care with follow-up",
  "988 for crisis (US)"],
 reqs=["De-escalation training",
  "Psychiatric emergency capacity",
  "Follow-up linkage"],
 stds=["Psychiatric emergency service standards (public literature)",
  "EMTALA applies to psychiatric emergencies too"],
 cites=["American Association for Emergency Psychiatry — public resources (public)",
  "988 Suicide and Crisis Lifeline (public)"],
 demo=("triage", {"patients": [
   {"id": "B-1: suicidal with plan", "priority": "immediate"},
   {"id": "B-2: anxious, no safety risk", "priority": "delayed"},
   {"id": "B-3: psychotic, agitated, unsafe", "priority": "urgent"}]})),

dict(title="Mass Casualty Incident Response", tier=C,
 desc_pub=("Mass casualty incidents (MCIs) - when patient numbers overwhelm resources - demand a "
  "different logic: do the most good for the most people. Incident command (ICS/NIMS) organizes "
  "the chaos; START triage sorts rapidly; hospitals activate surge plans.\n"
  "Preparation is everything: drills, mutual-aid agreements, stockpiled supplies, and hospital "
  "surge capacity. The first minutes belong to whoever is there - bystander bleeding control "
  "(Stop the Bleed) saves lives before responders arrive."),
 desc_sig=("Signature MCI design pre-computes surge playbooks per hazard type with resource "
  "checklists, so incident command starts from a plan rather than a blank board."),
 how_pub=("First units establish command, declare MCI, and request resources. Responders triage "
  "with START, treat the immediate, and transport by priority. Hospitals clear EDs, call in "
  "staff, and track patients for family reunification. After-action reviews improve the next "
  "response."),
 how_sig=("Signature hazard playbooks give incident commanders starting checklists matched to "
  "the event type."),
 keys=["Do the most good for the most people",
  "Incident command organizes chaos",
  "START triage sorts rapidly",
  "Hospital surge plans activate",
  "Bystander bleeding control saves lives early",
  "Drills and mutual aid are preparation"],
 reqs=["ICS/NIMS training",
  "MCI protocols and triage tags",
  "Hospital surge plans and mutual aid"],
 stds=["NIMS incident command (public)",
  "State MCI plan requirements"],
 cites=["Federal Emergency Management Agency — NIMS (public)",
  "U.S. Dept. of Homeland Security — Stop the Bleed (public)"],
 demo=("dispatch", {"calls": [
   {"id": "MCI: 12 patients reported", "priority": "P1"},
   {"id": "MCI: request 5 ambulances", "priority": "P1"},
   {"id": "Routine transport", "priority": "P3"}],
  "units": ["Medic-1", "Medic-2", "Medic-3", "Medic-4", "Medic-5"]})),

dict(title="Hazardous Materials Response", tier=C,
 desc_pub=("Hazmat incidents add contamination to injury: responders must identify the substance "
  "(placards, shipping papers, ERG guidebook), isolate the area, protect themselves with proper "
  "PPE levels, decontaminate patients before hospital entry, and treat exposures.\n"
  "Hospitals need decontamination capability and lockdown procedures - a contaminated patient "
  "walking into the ED endangers everyone. Regional hazmat teams bring specialized equipment and "
  "expertise. This record is educational."),
 desc_sig=("Signature hazmat design pre-plans facility decontamination workflows with supply "
  "tracking, so hospitals are ready before the contaminated patient arrives."),
 how_pub=("Dispatch gathers hazmat clues and sends hazmat teams with EMS staged upwind. Responders "
  "identify the material via ERG, establish hot/warm/cold zones, and decontaminate patients before "
  "transport. Hospitals activate decon teams for arrivals; poison control advises treatment."),
 how_sig=("Signature decon workflow tracking ensures every exposed patient is processed before "
  "ED entry."),
 keys=["Identify: placards, papers, ERG guidebook",
  "Isolate and zone: hot/warm/cold",
  "PPE levels matched to hazard",
  "Decontaminate before hospital entry",
  "Hospitals need decon capability",
  "Poison control advises treatment"],
 reqs=["Hazmat team access",
  "ERG guidebooks and detection",
  "Hospital decon capability"],
 stds=["OSHA hazmat standards (public)",
  "NFPA 470 hazmat response (public)"],
 cites=["U.S. Dept. of Transportation — Emergency Response Guidebook (public)",
  "Poison Control — 1-800-222-1222 (public)"],
 demo=("protocol", {"steps": ["Identify material (ERG)", "Isolate and deny entry",
   "Establish hot/warm/cold zones", "Don appropriate PPE",
   "Decontaminate patients", "Treat exposures per poison control"]})),

dict(title="Continuity of Care and Handoffs", tier=C,
 desc_pub=("Continuity of care means the patient's story and plan survive every transfer: field to "
  "ED, ED to floor, hospital to home or rehab. Structured handoffs (SBAR, I-PASS), reconciled "
  "medication lists, and scheduled follow-up prevent the errors that cluster at transitions.\n"
  "The data is stark: most serious adverse events involve communication failure at handoff. "
  "Continuity is a safety intervention, not paperwork."),
 desc_sig=("Signature continuity design makes the patient story a structured, cumulative record "
  "that each team extends - so handoffs transfer understanding, not just data."),
 how_pub=("Every transfer uses a structured handoff with read-back; medication lists are "
  "reconciled; pending tests and follow-ups are explicitly assigned. Discharge planners schedule "
  "follow-up before departure; high-risk patients get post-discharge calls. Primary care receives "
  "summaries promptly."),
 how_sig=("Signature cumulative records let each team see the full story and add their chapter, "
  "ending the game of telephone."),
 keys=["Story and plan survive every transfer",
  "Structured handoffs: SBAR, I-PASS with read-back",
  "Reconcile medications at every transition",
  "Most serious events involve handoff failure",
  "Schedule follow-up before discharge",
  "Continuity is a safety intervention"],
 reqs=["Handoff protocol training",
  "Medication reconciliation process",
  "Post-discharge follow-up for high-risk"],
 stds=["Joint Commission handoff standards (public)",
  "I-PASS handoff framework (public)"],
 cites=["The Joint Commission — handoff guidance (public)",
  "Institute for Healthcare Improvement — I-PASS (public)"],
 demo=("outcome", {"label": "Handoffs with read-back completed", "pre": 63, "post": 94})),

# ---------------- Advanced (11) ----------------
dict(title="Emergency Department Operations", tier=A,
 desc_pub=("ED operations manage flow through input (arrivals), throughput (evaluation and "
  "treatment), and output (admission or discharge). Crowding - the central operational disease - "
  "stems mostly from output block: admitted patients boarding in the ED for lack of inpatient "
  "beds.\n"
  "Levers include triage redesign, fast tracks for minor complaints, results-pending areas, "
  "bedside registration, and above all hospital-wide flow coordination. What gets measured - "
  "door-to-provider, length of stay, left-without-being-seen - gets managed."),
 desc_sig=("Signature ED operations run a live flow dashboard with predictive boarding alerts, so "
  "the hospital acts on output block before the ED drowns."),
 how_pub=("Leaders map flow, measure each stage's times, and attack constraints: fast tracks, "
  "provider-in-triage, inpatient discharge before noon to free beds. Daily huddles review "
  "yesterday's flow; improvement projects target the worst bottleneck."),
 how_sig=("Signature predictive boarding alerts trigger inpatient flow actions hours before ED "
  "gridlock."),
 keys=["Input, throughput, output",
  "Crowding stems mostly from output block",
  "Boarding: admitted patients stuck in ED",
  "Levers: fast track, provider-in-triage, flow coordination",
  "Measure: door-to-provider, LOS, LWBS",
  "Hospital-wide problem, not just ED's"],
 reqs=["Flow measurement at each stage",
  "Fast-track and triage redesign capacity",
  "Hospital-wide flow governance"],
 stds=["ED operational benchmarks (public literature)",
  "CMS ED throughput measures (public)"],
 cites=["American College of Emergency Physicians — crowding resources (public)",
  "Institute for Healthcare Improvement — flow guidance (public)"],
 demo=("outcome", {"label": "Median door-to-provider, minutes (lower better)", "pre": 42, "post": 21})),

dict(title="Crowding and Patient Flow", tier=A,
 desc_pub=("ED crowding harms patients: delayed antibiotics, missed heart attacks, higher "
  "mortality. It is a hospital problem manifesting in the ED - caused by inpatient capacity, "
  "discharge timing, and elective-surgery scheduling as much as by ED demand.\n"
  "Solutions are system-level: smoothing elective admissions, discharging inpatients before noon, "
  "inpatient hallway or discharge-lounge boarding alternatives, and full-capacity protocols that "
  "distribute boarding across the hospital instead of concentrating it in the ED."),
 desc_sig=("Signature flow management treats the hospital as one system with the ED as its "
  "canary: inpatient actions trigger on ED crowding scores automatically."),
 how_pub=("Hospitals adopt full-capacity protocols with ED crowding triggers, smooth elective "
  "schedules, and move discharges earlier. EDs split flow by acuity and use hallway care spaces "
  "as a last resort. Leaders review crowding metrics with the whole hospital, not just the ED."),
 how_sig=("Signature automatic triggers convert ED crowding scores into hospital-wide actions "
  "without waiting for meetings."),
 keys=["Crowding harms: delays, misses, higher mortality",
  "Hospital problem manifesting in the ED",
  "Causes: capacity, discharge timing, elective scheduling",
  "Full-capacity protocols distribute boarding",
  "Smooth electives; discharge before noon",
  "ED is the canary, not the cause"],
 reqs=["Hospital-wide flow governance",
  "Full-capacity protocol with triggers",
  "Crowding metrics reviewed broadly"],
 stds=["ACEP crowding policy (public)",
  "Joint Commission flow standards (public)"],
 cites=["American College of Emergency Physicians — crowding (public)"],
 demo=("outcome", {"label": "Boarding hours per 100 ED visits (lower better)", "pre": 38, "post": 17})),

dict(title="Telemedicine in Emergency Care", tier=A,
 desc_pub=("Telemedicine extends emergency expertise: telestroke brings neurologists to small EDs "
  "in minutes, telepsychiatry covers behavioral emergencies, and tele-EMS lets physicians guide "
  "field crews. During disasters, telemedicine sustains specialist access when transport fails.\n"
  "Success requires reliable connectivity, credentialed remote clinicians, and workflows that "
  "make the virtual consultant feel like part of the team - not a phone call from nowhere."),
 desc_sig=("Signature tele-emergency design embeds remote specialists in the resuscitation "
  "workflow with shared video and data, making distance expertise feel present."),
 how_pub=("Hospitals contract tele-specialty services, install carts with high-quality video, and "
  "train ED staff in activation criteria. Remote clinicians join resuscitations virtually with "
  "access to monitors and imaging. Performance is tracked like any clinical service."),
 how_sig=("Signature shared-data integration gives remote specialists the same monitors and "
  "images the bedside team sees."),
 keys=["Telestroke, telepsychiatry, tele-EMS",
  "Brings specialists to small EDs in minutes",
  "Sustains access in disasters",
  "Needs reliable connectivity and credentialing",
  "Workflows must integrate the remote clinician",
  "Track performance like any service"],
 reqs=["Tele-specialty contracts",
  "Video carts and connectivity",
  "Activation criteria and training"],
 stds=["State telemedicine regulations (public)",
  "Specialty telehealth guidelines (public literature)"],
 cites=["American Telemedicine Association — public resources (public)"],
 demo=("outcome", {"label": "Door-to-needle minutes, telestroke sites (lower better)", "pre": 74, "post": 52})),

dict(title="Community Paramedicine", tier=A,
 desc_pub=("Community paramedicine (mobile integrated health) sends paramedics beyond 911: home "
  "visits for frequent callers, post-discharge check-ins, chronic-disease monitoring, and "
  "vaccination or screening outreach. It addresses the reality that many 911 calls reflect unmet "
  "primary-care and social needs.\n"
  "Programs reduce ED visits and hospitalizations while connecting vulnerable people to ongoing "
  "care. Success needs medical oversight, defined protocols, and integration with primary care "
  "and social services."),
 desc_sig=("Signature community paramedicine runs on risk-stratified visit lists with protocol "
  "playbooks, turning reactive 911 response into proactive population health."),
 how_pub=("Medical directors authorize expanded-scope protocols; programs identify frequent "
  "callers and high-risk discharges for enrollment. Paramedics visit on schedule, assess, treat "
  "within protocol, and refer to primary care and social services. Outcomes tracked: ED visits, "
  "admissions, connection to care."),
 how_sig=("Signature risk-stratified lists ensure visits go to those who benefit most."),
 keys=["Paramedics beyond 911: home visits, check-ins, monitoring",
  "Addresses unmet primary-care and social needs",
  "Reduces ED visits and hospitalizations",
  "Needs medical oversight and protocols",
  "Integrate with primary care and social services",
  "Proactive population health"],
 reqs=["Expanded-scope authorization",
  "Risk-stratification data",
  "Primary-care and social-service partnerships"],
 stds=["State community-paramedicine regulations (public)",
  "Medical oversight requirements"],
 cites=["National Association of EMTs — mobile integrated health (public)"],
 demo=("outcome", {"label": "ED visits among enrolled frequent callers (lower better)", "pre": 100, "post": 58})),

dict(title="Disaster Medical Response Teams", tier=A,
 desc_pub=("Disaster medical teams - DMATs, hospital strike teams, Medical Reserve Corps volunteers "
  "- deploy to hurricanes, earthquakes, pandemics, and mass gatherings. They bring self-sufficient "
  "medical capability: triage, treatment, and stabilization where infrastructure failed.\n"
  "Readiness is continuous: credentialing, equipment caches, deployment drills, and integration "
  "with incident command. Volunteers need liability protection and just-in-time training to be "
  "assets rather than burdens."),
 desc_sig=("Signature disaster medical readiness maintains living rosters with verified "
  "credentials and equipment status, so deployment is a decision, not a scramble."),
 how_pub=("Teams maintain rosters, caches, and training; when disaster strikes, incident command "
  "requests them through emergency management channels. Teams deploy self-sufficient for 72 "
  "hours, integrate into the medical branch, and demobilize with after-action review."),
 how_sig=("Signature living rosters show deployable capability in real time."),
 keys=["DMATs, strike teams, Medical Reserve Corps",
  "Self-sufficient for 72 hours",
  "Triage and stabilization where infrastructure failed",
  "Credentialing and drills are readiness",
  "Integrate with incident command",
  "Volunteers need liability protection"],
 reqs=["Credentialed rosters",
  "Equipment caches",
  "Emergency-management integration"],
 stds=["National Disaster Medical System standards (public)",
  "State volunteer health practitioner laws"],
 cites=["U.S. Dept. of Health and Human Services — NDMS (public)",
  "Medical Reserve Corps — public resources (public)"],
 demo=("protocol", {"steps": ["Roster and credential check", "Equipment cache verified",
   "Deploy via emergency management", "Integrate into medical branch",
   "Operate 72-hour self-sufficient", "Demobilize and after-action review"]})),

dict(title="Emergency Preparedness Planning", tier=A,
 desc_pub=("Emergency preparedness planning readies health systems for disasters: hazard "
  "vulnerability analysis, emergency operations plans, surge capacity, supply stockpiles, "
  "communications redundancy, staff recall, and exercises testing it all. CMS requires emergency "
  "preparedness programs for participating providers.\n"
  "Plans fail at the seams - between organizations - so coalitions (healthcare coalitions) "
  "coordinate hospitals, EMS, public health, and emergency management regionally."),
 desc_sig=("Signature preparedness maintains the plan as a living system - roles, contacts, "
  "supplies, playbooks - continuously verified rather than annually dusted off."),
 how_pub=("Facilities conduct hazard analyses, write all-hazards plans with annexes per threat, "
  "stockpile per plans, and exercise twice yearly including full-scale. Healthcare coalitions "
  "align members' plans, run regional exercises, and coordinate real responses."),
 how_sig=("Signature continuous verification keeps contacts, supplies, and roles current between "
  "exercises."),
 keys=["Hazard analysis, operations plans, surge, stockpiles, comms, recall",
  "CMS requires preparedness programs",
  "Plans fail at organizational seams",
  "Healthcare coalitions coordinate regionally",
  "Exercise twice yearly minimum",
  "Living plans, not binders"],
 reqs=["All-hazards plan with annexes",
  "Exercise program",
  "Coalition membership"],
 stds=["CMS emergency preparedness rule (public regulation)",
  "Joint Commission emergency management standards (public)"],
 cites=["Centers for Medicare and Medicaid Services — preparedness rule (public)",
  "Federal Emergency Management Agency — planning guidance (public)"],
 demo=("protocol", {"steps": ["Hazard vulnerability analysis", "Write all-hazards plan + annexes",
   "Stockpile per plan", "Train staff on roles", "Exercise (tabletop + full-scale)",
   "After-action improvement"]})),

dict(title="Quality Metrics in Emergency Care", tier=A,
 desc_pub=("Emergency care quality is measured in time-sensitive outcomes: door-to-balloon, door-"
  "to-needle, sepsis bundle compliance, left-without-being-seen rates, 72-hour returns, and "
  "mortality for key conditions. Process measures (triage accuracy, pain reassessment) complement "
  "outcome measures.\n"
  "Public reporting and accreditation tie reputation and revenue to performance. The improvement "
  "discipline: measure, feed back to clinicians, redesign workflows, re-measure."),
 desc_sig=("Signature emergency quality runs real-time metric dashboards with case-level drill-"
  "down, so clinicians see their own performance and improve continuously."),
 how_pub=("EDs select core measures, build data capture into workflows, and review dashboards in "
  "quality meetings. Outliers trigger case review; patterns trigger redesign. Results feed "
  "accreditation and public reporting."),
 how_sig=("Signature case-level drill-down turns aggregate metrics into learnable individual "
  "cases."),
 keys=["Time-sensitive outcomes: balloon, needle, sepsis bundles",
  "LWBS, 72-hour returns, condition mortality",
  "Process + outcome measures",
  "Public reporting ties reputation to performance",
  "Measure, feedback, redesign, re-measure",
  "Data capture built into workflows"],
 reqs=["Core measure set",
  "Workflow-embedded data capture",
  "Case-review process"],
 stds=["CMS ED measures (public)",
  "Accreditation quality expectations"],
 cites=["Centers for Medicare and Medicaid Services — quality measures (public)"],
 demo=("outcome", {"label": "Sepsis bundle compliance", "pre": 58, "post": 89})),

dict(title="Resuscitation Science Updates", tier=A,
 desc_pub=("Resuscitation science advances through ILCOR's continuous evidence review, translated "
  "into AHA guidelines: high-quality CPR (rate, depth, recoil, minimal interruptions), early "
  "defibrillation, epinephrine timing, post-arrest temperature management, and ECPR (ECMO during "
  "arrest) for selected patients.\n"
  "Systems improve survival through dispatcher-guided CPR, public AED placement, mechanical CPR "
  "quality, and post-arrest care bundles. Every link's performance is measurable - and "
  "improvable. Educational record; resuscitation is professional practice."),
 desc_sig=("Signature resuscitation systems measure every link - bystander CPR rate, EMS CPR "
  "quality, hospital post-arrest care - as one survival chain."),
 how_pub=("Systems train dispatchers in CPR instructions, place AEDs strategically, monitor CPR "
  "quality with feedback devices, and run post-arrest bundles in ICUs. Registries (like CARES) "
  "benchmark survival and drive improvement."),
 how_sig=("Signature chain measurement shows exactly which link limits survival locally."),
 keys=["High-quality CPR: rate, depth, recoil, minimal pauses",
  "Early defibrillation",
  "Dispatcher-guided CPR + public AEDs",
  "Post-arrest bundles",
  "Registries benchmark survival",
  "Every link measurable and improvable"],
 reqs=["CPR quality feedback devices",
  "AED placement program",
  "Post-arrest protocol"],
 stds=["AHA guidelines (public)",
  "ILCOR consensus on science (public)"],
 cites=["American Heart Association — resuscitation guidelines (public)",
  "Cardiac Arrest Registry to Enhance Survival — CARES (public)"],
 demo=("outcome", {"label": "Survival to discharge, witnessed VF arrest", "pre": 24, "post": 43})),

dict(title="Rural Emergency Service Models", tier=A,
 desc_pub=("Rural emergency care faces distance, low volumes, and workforce shortages: long "
  "transport times, volunteer EMS staffing, and small hospitals without specialists. Models that "
  "work include regionalized systems (stabilize-and-transfer networks), telemedicine specialty "
  "support, community paramedicine, and cross-trained workforces.\n"
  "Helicopter transport, tele-stroke, and strong transfer agreements shrink the distance penalty. "
  "Funding models must recognize that low volume does not mean low readiness cost."),
 desc_sig=("Signature rural design optimizes the stabilize-and-transfer network with telemedicine "
  "at every node, so geography stops determining outcomes."),
 how_pub=("Regions designate levels among small hospitals, build transfer agreements with "
  "protocols, deploy telemedicine for stroke/trauma/psychiatry, and sustain volunteer EMS with "
  "training and stipends. Data tracks transport times and outcomes by zone."),
 how_sig=("Signature network optimization places capabilities where transport-time math says "
  "they save the most lives."),
 keys=["Distance, low volume, workforce shortages",
  "Regionalize: stabilize-and-transfer networks",
  "Telemedicine for stroke, trauma, psychiatry",
  "Community paramedicine fills gaps",
  "Sustain volunteer EMS",
  "Fund readiness, not just volume"],
 reqs=["Transfer agreements and protocols",
  "Telemedicine specialty coverage",
  "Volunteer workforce support"],
 stds=["State rural EMS provisions (public)",
  "Critical access hospital rules (public)"],
 cites=["Federal Office of Rural Health Policy (public)",
  "Rural Health Information Hub (public)"],
 demo=("response_time", {"times": [14.2, 18.5, 12.8, 22.1, 16.4, 19.7]})),

dict(title="Interfacility Transport", tier=A,
 desc_pub=("Interfacility transport moves patients between hospitals - to higher care, back to "
  "community hospitals, or for specialty procedures. Levels range from BLS ambulances for stable "
  "patients to critical-care transport teams (nurse/paramedic or nurse/respiratory) managing "
  "ventilators, drips, and balloon pumps en route.\n"
  "Appropriate level, complete handoff, and acceptance confirmed before wheels roll: the "
  "discipline that prevents transport disasters. EMTALA governs transfers, requiring "
  "stabilization and acceptance."),
 desc_sig=("Signature transport coordination matches vehicle, crew, and equipment to patient "
  "acuity by protocol, with handoff checklists enforced digitally."),
 how_pub=("Sending physicians determine needed level and confirm acceptance; transport teams "
  "receive full handoff (SBAR plus drips, vents, risks). En route monitoring continues ICU-level "
  "vigilance; receiving teams get prenotification. Documentation covers the entire interval."),
 how_sig=("Signature acuity-matched dispatch ensures no under-crewed critical transport."),
 keys=["Between hospitals: up, down, or specialty",
  "BLS to critical-care teams by acuity",
  "Acceptance confirmed before departure",
  "Complete handoff with drips, vents, risks",
  "EMTALA governs transfers",
  "Document the entire interval"],
 reqs=["Tiered transport capability",
  "Acceptance and handoff protocols",
  "EMTALA-compliant transfer process"],
 stds=["EMTALA transfer requirements (public law)",
  "CAMTS standards for critical care (public)"],
 cites=["Centers for Medicare and Medicaid Services — EMTALA (public)"],
 demo=("protocol", {"steps": ["Determine required transport level", "Confirm receiving acceptance",
   "Full handoff: SBAR + devices + risks", "En route ICU-level monitoring",
   "Prenotify receiving team", "Document entire interval"]})),

dict(title="The Future of Emergency Care", tier=A,
 desc_pub=("Emergency care's future: predictive dispatch anticipating demand, AI-assisted triage "
  "with clinician oversight, hospital-at-home diverting admissions, drones delivering AEDs and "
  "medications, and fully integrated regional systems where data flows from 911 to rehab.\n"
  "The constant: emergencies remain human crises needing skilled, compassionate responders. "
  "Technology should speed the right care to the right patient - never replace the judgment and "
  "humanity at the core."),
 desc_sig=("The Signature future-state is an emergency-care operating system: predictive "
  "positioning, protocol-driven response, seamless data across the chain, and outcome "
  "accountability - with human responders augmented, never replaced. This database is a "
  "prototype of that system's knowledge core."),
 how_pub=("Systems adopt demand forecasting, integrate data across the chain, deploy hospital-at-"
  "home and community paramedicine to bend demand, and validate AI tools for fairness and safety "
  "before trusting them with triage."),
 how_sig=("Signature's operating-system vision makes today's advanced practices the default "
  "infrastructure of emergency care."),
 keys=["Predictive dispatch and AI-assisted triage (with oversight)",
  "Hospital-at-home diverts admissions",
  "Drones for AEDs and medications",
  "Integrated regional data: 911 to rehab",
  "Validate AI for fairness and safety",
  "Human judgment and compassion remain central"],
 reqs=["Data integration across the chain",
  "AI validation frameworks",
  "Hospital-at-home capability"],
 stds=["Emerging standards for AI in emergency care (public literature)"],
 cites=["National Highway Traffic Safety Administration — EMS future (public)"],
 demo=("outcome", {"label": "Low-acuity 911 calls safely diverted", "pre": 12, "post": 34})),
]
