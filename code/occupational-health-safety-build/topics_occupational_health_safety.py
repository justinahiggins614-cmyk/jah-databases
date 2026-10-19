#!/usr/bin/env python3
"""Topics + config for the occupational-health-safety pair. Property of Justin Addam Higgins (JAH)."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "occupational-health-safety",
    "name_pub": "The Occupational Health and Safety Database",
    "name_sig": "Signature Occupational Health and Safety Database",
    "tagline_pub": ("Occupational health and safety from the ground up: workplace hazards and "
                    "exposure, ergonomics and industrial hygiene, the hierarchy of controls, "
                    "incident reporting and investigation, and prevention systems - every record "
                    "carrying the full entry taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of occupational health and safety: "
                    "the same real safety knowledge carried forward, plus Signature-built hazard "
                    "models, prevention systems, and safety-management frameworks original to "
                    "this system."),
    "record_kind": "occupational health and safety record",
    "record_kind_plural": "occupational health and safety records",
    "prefix_pub": "JAH-OHS-", "prefix_sig": "JAH-OHSS-",
    "ai_pub": "JAH Occupational Health and Safety Archivist",
    "ai_sig": "JAH Signature Occupational Health and Safety Creator",
    "role_pub": ("occupational health and safety archivist - teaching hazards, exposure, "
                 "ergonomics, industrial hygiene, incident reporting, and prevention; answers from "
                 "many angles - definition, example, process, control, system - using only archive "
                 "data from this system"),
    "role_sig": ("Signature creator of occupational health and safety systems - designing hazard "
                 "models, prevention frameworks, and safety-management systems as original "
                 "Signature works; answers from many angles using only archive data from this "
                 "system"),
    "search_ph": "Search hazards, exposure, ergonomics, hygiene, incidents, prevention...",
    "chat_ph": "Ask about occupational health and safety...",
    "greet_pub": ("I am the JAH Occupational Health and Safety Archivist. Ask me about hazards, "
                  "exposure, ergonomics, industrial hygiene, incident reporting, and prevention."),
    "greet_sig": ("I am the JAH Signature Occupational Health and Safety Creator. Ask me about "
                  "Signature-built safety systems."),
    "gen_blurb": ("Generate clearly-labeled occupational health and safety studies. Seeded archive "
                  "records are the authoritative entries."),
    "about_archive": ("Seeded occupational health and safety records, marching toward one million "
                      "records. Presented in teaching-ladder order: foundations, compounded, "
                      "advanced."),
    "demo_kind": "ohs-demo",
    "demo_title": "Occupational Health and Safety Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Occupational Health and Safety Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "risk":
        return fill(
            "hazards = @@HAZ@@\n"
            "ranked = sorted(hazards, key=lambda h: h['likelihood'] * h['severity'], reverse=True)\n"
            "print('Hazard risk ranking (likelihood x severity):')\n"
            "for h in ranked:\n"
            "    score = h['likelihood'] * h['severity']\n"
            "    band = 'HIGH' if score >= 15 else 'MED' if score >= 8 else 'LOW'\n"
            "    print(' [%s] %s (score %d)' % (band, h['hazard'], score))\n",
            {"HAZ": p["hazards"]})
    if v == "controls":
        return fill(
            "hazard = @@HAZ@@\ncontrols = @@CTRLS@@\n"
            "order = ['elimination', 'substitution', 'engineering', 'administrative', 'ppe']\n"
            "print('Hierarchy of controls for:', hazard)\n"
            "for c in sorted(controls, key=lambda x: order.index(x['level'])):\n"
            "    print(' %d. [%s] %s' % (order.index(c['level']) + 1, c['level'], c['measure']))\n",
            {"HAZ": p["hazard"], "CTRLS": p["controls"]})
    if v == "rate":
        return fill(
            "incidents = @@INC@@\nhours = @@HRS@@\n"
            "trir = incidents * 200000 / hours if hours else 0\n"
            "print('Recordable incidents:', incidents)\n"
            "print('Hours worked:', hours)\n"
            "print('TRIR (per 200,000 hrs): %.2f' % trir)\n",
            {"INC": p["incidents"], "HRS": p["hours"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d' % (pre, post, delta))\n"
            "print('Direction:', 'improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged')\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    if v == "protocol":
        return fill(
            "steps = @@STEPS@@\n"
            "print('Safety protocol:')\n"
            "for i, s in enumerate(steps, 1):\n"
            "    print(' %d. %s' % (i, s))\n",
            {"STEPS": p["steps"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Occupational Health and Safety Is", tier=F,
 desc_pub=("Occupational health and safety (OHS) is the discipline of preventing work-related "
  "injury, illness, and death. It covers hazard identification, exposure assessment, engineering "
  "and administrative controls, personal protective equipment, training, incident investigation, "
  "and health surveillance - applied in every industry from offices to mines.\n"
  "The field's moral and economic case is one: safe workplaces save lives and money. In the U.S., "
  "OSHA sets and enforces standards; employers hold the primary duty to provide workplaces free "
  "from recognized hazards."),
 desc_sig=("The Signature system models workplace safety as a layered defense architecture - "
  "hazards identified, controls layered by hierarchy, residual risk monitored - so safety is "
  "engineered as a system rather than pursued as a slogan."),
 how_pub=("Organizations identify hazards through inspections, job analyses, and worker input; "
  "assess risks; apply controls in hierarchy order; train workers; and investigate incidents to "
  "prevent recurrence. Management commitment and worker participation power the whole cycle."),
 how_sig=("Signature layered-defense tracking scores each hazard's control layers, exposing thin "
  "defenses before incidents do."),
 keys=["Preventing work-related injury, illness, death",
  "Hazards, exposure, controls, PPE, training, investigation",
  "Every industry from offices to mines",
  "OSHA sets and enforces U.S. standards",
  "Employers: workplaces free from recognized hazards",
  "Management commitment + worker participation"],
 reqs=["Hazard identification process",
  "Control implementation",
  "Incident investigation"],
 stds=["OSHA standards (public)",
  "ISO 45001 occupational health and safety (public)"],
 cites=["Occupational Safety and Health Administration — public resources (public)",
  "National Institute for Occupational Safety and Health — NIOSH (public)"],
 demo=("risk", {"hazards": [
   {"hazard": "Unguarded conveyor", "likelihood": 4, "severity": 5},
   {"hazard": "Office trip hazard", "likelihood": 3, "severity": 2},
   {"hazard": "Chemical splash", "likelihood": 2, "severity": 4}]})),

dict(title="Worker Rights and Employer Duties", tier=F,
 desc_pub=("U.S. workers hold OSHA rights: to a safe workplace, to safety training in a language "
  "they understand, to review injury records, to file confidential complaints, to refuse "
  "imminently dangerous work, and to be free from retaliation for exercising these rights.\n"
  "Employers must comply with standards, inform workers of hazards (HazCom), provide required "
  "PPE at no cost, record injuries, and not retaliate. The general duty clause covers recognized "
  "hazards even without a specific standard."),
 desc_sig=("Signature rights education turns legal protections into workplace playbooks: how to "
  "report, what to document, where to complain - so rights are usable on the shop floor."),
 how_pub=("Workers raise concerns first with supervisors or safety committees; unresolved issues "
  "go to OSHA as confidential complaints triggering inspection. Retaliation complaints go to "
  "OSHA's whistleblower program within strict deadlines. Documentation decides cases."),
 how_sig=("Signature documentation templates help workers build complete, timestamped records."),
 keys=["Rights: safe workplace, training, records, complaints, refusal, no retaliation",
  "Duties: comply, inform, provide PPE, record, no retaliation",
  "General duty clause covers recognized hazards",
  "Complaints can be confidential",
  "Retaliation complaints have strict deadlines",
  "Documentation decides cases"],
 reqs=["Posted worker rights",
  "Complaint and anti-retaliation procedures",
  "Hazard communication program"],
 stds=["OSH Act worker rights (public law)",
  "OSHA whistleblower statutes (public)"],
 cites=["Occupational Safety and Health Administration — worker rights (public)"],
 demo=("protocol", {"steps": ["Raise concern with supervisor", "Document in writing",
   "Escalate to safety committee", "File confidential OSHA complaint if unresolved",
   "Document any retaliation immediately"]})),

dict(title="Common Workplace Hazards", tier=F,
 desc_pub=("Workplace hazards fall into families: safety hazards (falls, struck-by, caught-in, "
  "electrical), chemical (solvents, dusts, fumes), biological (bloodborne pathogens, mold), "
  "physical (noise, vibration, radiation, temperature), ergonomic (lifting, repetition, posture), "
  "and psychosocial (violence, stress, fatigue).\n"
  "Recognition starts with looking: walkarounds, worker interviews, injury-record review, and "
  "safety data sheets. You cannot control what you have not identified."),
 desc_sig=("Signature hazard identification uses structured walkaround checklists per industry, "
  "so recognition is systematic rather than dependent on individual vigilance."),
 how_pub=("Safety staff and workers conduct scheduled inspections with checklists, interview "
  "workers about near-misses and discomfort, review OSHA 300 logs for patterns, and inventory "
  "chemicals via SDS. Findings enter a hazard register with assigned controls."),
 how_sig=("Signature structured checklists ensure every walkaround covers every hazard family."),
 keys=["Safety, chemical, biological, physical, ergonomic, psychosocial",
  "Recognition: walkarounds, interviews, records, SDS",
  "Near-misses predict future injuries",
  "Injury logs reveal patterns",
  "Cannot control unidentified hazards",
  "Hazard register tracks findings to controls"],
 reqs=["Inspection schedules and checklists",
  "SDS inventory",
  "Hazard register"],
 stds=["OSHA inspection expectations (public)",
  "Hazard identification guidance (public literature)"],
 cites=["Occupational Safety and Health Administration — hazard identification (public)",
  "National Institute for Occupational Safety and Health — hazards (public)"],
 demo=("risk", {"hazards": [
   {"hazard": "Forklift-pedestrian interaction", "likelihood": 3, "severity": 5},
   {"hazard": "Repetitive packing motion", "likelihood": 5, "severity": 3},
   {"hazard": "Wet floor", "likelihood": 4, "severity": 2},
   {"hazard": "Silica dust", "likelihood": 3, "severity": 4}]})),

dict(title="The Hierarchy of Controls", tier=F,
 desc_pub=("The hierarchy of controls ranks hazard controls by effectiveness: elimination (remove "
  "the hazard), substitution (replace with safer), engineering controls (isolate or ventilate), "
  "administrative controls (procedures, training, scheduling), and PPE (last resort - protects "
  "the worker, not the hazard).\n"
  "The discipline: always prefer higher levels. PPE is necessary but weakest - it fails when "
  "forgotten, ill-fitting, or degraded. Lasting safety is engineered, not worn."),
 desc_sig=("Signature control design requires documenting why higher hierarchy levels were not "
  "feasible before accepting lower ones - making the hierarchy a decision record, not a "
  "poster."),
 how_pub=("For each significant hazard, teams work down the hierarchy: can we eliminate? "
  "substitute? engineer it out? Only then do procedures and PPE complete the defense. The "
  "chosen controls are implemented, workers trained, and effectiveness verified."),
 how_sig=("Signature hierarchy decision records justify control choices transparently."),
 keys=["Elimination, substitution, engineering, administrative, PPE",
  "Higher is more effective",
  "PPE is last resort",
  "Engineer safety; don't just wear it",
  "Document why higher levels weren't feasible",
  "Verify control effectiveness"],
 reqs=["Hierarchy-based control selection",
  "Implementation and training",
  "Effectiveness verification"],
 stds=["NIOSH hierarchy of controls (public)",
  "ANSI/ASSP Z10 (public)"],
 cites=["National Institute for Occupational Safety and Health — hierarchy (public)"],
 demo=("controls", {"hazard": "Welding fumes",
   "controls": [{"level": "ppe", "measure": "Respirators for welders"},
                {"level": "engineering", "measure": "Local exhaust ventilation at stations"},
                {"level": "substitution", "measure": "Low-fume welding wire"},
                {"level": "administrative", "measure": "Rotate welders to limit exposure"}]})),

dict(title="Personal Protective Equipment", tier=F,
 desc_pub=("PPE - hard hats, eye and face protection, gloves, respirators, hearing protection, "
  "high-visibility clothing, fall harnesses - is the last line of defense. Employers must assess "
  "hazards, select appropriate PPE, provide it free, train workers, and enforce use.\n"
  "Fit is function: respirators need fit-testing; harnesses need correct adjustment; gloves "
  "must suit the chemical. PPE programs fail on fit, maintenance, and consistent use - the "
  "human factors the hierarchy warns about."),
 desc_sig=("Signature PPE programs track issuance, fit-testing, and inspection digitally per "
  "worker, so the last line of defense is actually maintained."),
 how_pub=("Hazard assessments determine required PPE per task; employers procure, fit-test "
  "(respirators), and train. Supervisors enforce use; damaged PPE is replaced; programs are "
  "reviewed when hazards or tasks change."),
 how_sig=("Signature per-worker PPE tracking ensures fit-testing and replacement never lapse."),
 keys=["Last line of defense",
  "Employers: assess, select, provide free, train, enforce",
  "Fit is function: fit-test respirators",
  "Match PPE to the specific hazard",
  "Maintain and replace",
  "Human factors are the failure mode"],
 reqs=["PPE hazard assessment",
  "Fit-testing program",
  "Training and enforcement"],
 stds=["OSHA PPE standards (public)",
  "ANSI/ISEA equipment standards (public)"],
 cites=["Occupational Safety and Health Administration — PPE (public)"],
 demo=("controls", {"hazard": "Falling objects on construction site",
   "controls": [{"level": "ppe", "measure": "Hard hats, ANSI-rated"},
                {"level": "engineering", "measure": "Toe boards and debris nets"},
                {"level": "administrative", "measure": "Exclusion zones below work"}]})),

dict(title="Safety Training Basics", tier=F,
 desc_pub=("Safety training gives workers the knowledge to work without getting hurt: hazard "
  "recognition, safe procedures, PPE use, emergency response, and their rights. OSHA requires "
  "training for specific hazards (HazCom, lockout/tagout, fall protection, respirators) and "
  "effective training is in a language and literacy level workers understand.\n"
  "Training must be verified, not just delivered: demonstration, quizzes, and observed practice "
  "prove competence. Refresher training follows schedule or incident triggers."),
 desc_sig=("Signature training systems verify competence per worker per topic with digital "
  "records, so qualification is provable at any audit."),
 how_pub=("Employers identify required training by hazard, deliver it before exposure (and in "
  "understandable language), verify competence through demonstration or testing, document "
  "everything, and refresh on schedule or after incidents."),
 how_sig=("Signature competence verification replaces attendance sheets with demonstrated "
  "ability."),
 keys=["Hazard recognition, procedures, PPE, emergency, rights",
  "Required for specific hazards by OSHA",
  "Language and literacy workers understand",
  "Verify competence, don't just deliver",
  "Document everything",
  "Refresh on schedule or after incidents"],
 reqs=["Training needs analysis",
  "Competent trainers",
  "Documentation system"],
 stds=["OSHA training requirements (public)",
  "ANSI/ASSP Z490 training criteria (public)"],
 cites=["Occupational Safety and Health Administration — training (public)"],
 demo=("outcome", {"label": "Workers passing competency verification", "pre": 72, "post": 96})),

dict(title="Hazard Communication", tier=F,
 desc_pub=("Hazard Communication (HazCom/GHS) ensures workers know the chemicals they face: "
  "container labels with pictograms and signal words, Safety Data Sheets (SDS) with 16 sections "
  "of detail, and training on reading both. Every chemical in the workplace must be inventoried "
  "with its SDS accessible.\n"
  "The Globally Harmonized System standardized the pictograms - skull, flame, corrosion - so "
  "warnings read the same worldwide. Unknown chemicals get treated as hazardous until "
  "identified."),
 desc_sig=("Signature chemical management maintains a live SDS library linked to container "
  "labels and training records, so HazCom compliance is continuous."),
 how_pub=("Employers inventory chemicals, obtain SDS for each, label all containers per GHS, and "
  "train workers on the specific chemicals they may encounter. SDS are accessible during all "
  "shifts; new chemicals trigger training before use."),
 how_sig=("Signature live SDS libraries keep every sheet current and accessible."),
 keys=["Labels + SDS + training",
  "GHS pictograms standardized worldwide",
  "16-section SDS format",
  "Inventory every chemical",
  "SDS accessible all shifts",
  "Train before new chemical use"],
 reqs=["Chemical inventory",
  "SDS library",
  "GHS labeling and training"],
 stds=["OSHA HazCom standard (public)",
  "GHS (UN, public)"],
 cites=["Occupational Safety and Health Administration — HazCom (public)"],
 demo=("protocol", {"steps": ["Inventory all chemicals", "Obtain SDS for each",
   "Label containers per GHS", "Train workers on their chemicals",
   "Keep SDS accessible all shifts", "Train before new chemicals"]})),

dict(title="Incident Reporting Basics", tier=F,
 desc_pub=("Incident reporting captures injuries, illnesses, near-misses, and hazardous conditions "
  "so they can be fixed. OSHA requires recording qualifying injuries on the 300 log and reporting "
  "fatalities within 8 hours and hospitalizations within 24 hours. Near-miss reporting - no "
  "injury, but could have been - is the leading indicator goldmine.\n"
  "Blame-free reporting cultures get the data; punitive ones get silence. Every report deserves "
  "timely investigation and feedback to the reporter."),
 desc_sig=("Signature incident systems make reporting frictionless (mobile, multilingual) with "
  "automatic investigation assignment, so every report becomes action."),
 how_pub=("Workers report immediately to supervisors; supervisors ensure care and secure the "
  "scene; safety staff log, classify, and investigate. OSHA-recordable cases enter the 300 log; "
  "severe cases are reported to OSHA within deadlines. Reporters get feedback on actions taken."),
 how_sig=("Signature automatic investigation assignment ensures no report sits unexamined."),
 keys=["Report injuries, illnesses, near-misses, hazards",
  "OSHA 300 log for recordables",
  "Fatalities 8 hrs; hospitalizations 24 hrs",
  "Near-misses are leading indicators",
  "Blame-free cultures get data",
  "Feedback to every reporter"],
 reqs=["Reporting procedure and forms",
  "OSHA recording criteria knowledge",
  "Investigation capacity"],
 stds=["OSHA recordkeeping and reporting (public)"],
 cites=["Occupational Safety and Health Administration — recordkeeping (public)"],
 demo=("rate", {"incidents": 7, "hours": 480000})),

dict(title="Emergency Action Plans", tier=F,
 desc_pub=("Emergency action plans prepare workplaces for fires, chemical releases, severe "
  "weather, and violence: alarm systems, evacuation routes and assembly points, shutdown "
  "procedures, rescue and medical duties, and employee headcounts. OSHA requires written plans "
  "for most employers.\n"
  "Plans work only if practiced: drills reveal blocked routes, confusing alarms, and "
  "unaccounted visitors. Assign roles - floor wardens, first-aiders - before the emergency."),
 desc_sig=("Signature emergency planning pairs written plans with drill performance tracking, so "
  "readiness is measured, not assumed."),
 how_pub=("Employers assess site hazards, write the plan with routes and roles, train all "
  "employees, and drill (evacuation at least annually). Drills are evaluated; deficiencies "
  "correct the plan. Visitors and contractors are covered too."),
 how_sig=("Signature drill scoring turns each exercise into quantified readiness data."),
 keys=["Alarms, routes, assembly, shutdown, rescue, headcount",
  "Written plans required for most employers",
  "Drills reveal what paper hides",
  "Assign roles before emergencies",
  "Cover visitors and contractors",
  "Evaluate and correct after drills"],
 reqs=["Written emergency action plan",
  "Alarm and communication systems",
  "Drill program"],
 stds=["OSHA emergency action plan standard (public)",
  "NFPA 101 life safety (public)"],
 cites=["Occupational Safety and Health Administration — emergency plans (public)"],
 demo=("protocol", {"steps": ["Assess site hazards", "Write plan: routes, roles, alarms",
   "Train all employees", "Drill evacuation", "Evaluate and correct",
   "Cover visitors/contractors"]})),

dict(title="First Aid in the Workplace", tier=F,
 desc_pub=("Workplace first aid covers the minutes before professionals arrive: bleeding control "
  "(direct pressure, tourniquets for life-threatening limb bleeding), CPR and AED use, choking "
  "relief, burn cooling, and eye flushing for chemical splashes. OSHA requires adequate first-"
  "aid supplies and trained providers where emergency care is not near.\n"
  "Training through recognized providers with hands-on practice is the standard; skills decay "
  "without refreshers. Good Samaritan protections generally cover trained workplace responders."),
 desc_sig=("Signature first-aid readiness tracks trained responders per shift and kit "
  "completeness, so coverage never has gaps."),
 how_pub=("Employers assess first-aid needs by hazards and distance from emergency care, train "
  "adequate responders per shift, stock kits to the hazard, and post emergency numbers. "
  "Refresher training keeps skills current."),
 how_sig=("Signature per-shift responder tracking guarantees coverage on every shift."),
 keys=["Bleeding control, CPR/AED, choking, burns, eye flush",
  "Minutes before professionals arrive",
  "Adequate supplies + trained providers",
  "Hands-on training; refresh regularly",
  "Tourniquets for life-threatening limb bleeding",
  "Good Samaritan protections generally apply"],
 reqs=["First-aid needs assessment",
  "Trained responders per shift",
  "Stocked kits and AEDs"],
 stds=["OSHA first-aid requirements (public)",
  "ANSI Z308.1 first-aid kits (public)"],
 cites=["Occupational Safety and Health Administration — first aid (public)",
  "American Red Cross — first aid training (public)"],
 demo=("outcome", {"label": "Shifts with trained first-aid coverage", "pre": 64, "post": 98})),

dict(title="Safety Culture", tier=F,
 desc_pub=("Safety culture is what people do when nobody is watching: reporting hazards without "
  "fear, stopping unsafe work, looking out for coworkers. It is built by leadership actions - "
  "funding safety, praising reporting, disciplining retaliation - not by slogans.\n"
  "Culture is measurable: survey it, track reporting rates and safety participation, and watch "
  "whether bad news travels up. Just culture distinguishes honest mistakes (coach) from "
  "recklessness (discipline) - fairly and consistently."),
 desc_sig=("Signature culture measurement runs regular safety-climate surveys with transparent "
  "results and action plans, making culture a managed metric."),
 how_pub=("Leaders visibly prioritize safety in decisions and budgets, recognize safe behavior "
  "and reporting, and respond to bad news with fixes not punishment. Organizations survey "
  "climate, share results, and act on them. Just-culture principles guide discipline."),
 how_sig=("Signature transparent survey-action cycles prove to workers that their input "
  "changes things."),
 keys=["What people do when nobody watches",
  "Built by leadership actions, not slogans",
  "Report without fear; stop unsafe work",
  "Just culture: coach mistakes, discipline recklessness",
  "Measurable via surveys and reporting rates",
  "Bad news must travel up"],
 reqs=["Leadership commitment behaviors",
  "Climate survey process",
  "Just-culture discipline framework"],
 stds=["Safety culture guidance (public literature, e.g., NSC)"],
 cites=["National Safety Council — safety culture (public)",
  "Center for Chemical Process Safety — culture guidance (public)"],
 demo=("outcome", {"label": "Workers agreeing 'safety is valued here'", "pre": 58, "post": 86})),

# ---------------- Compounded (12) ----------------
dict(title="Chemical Hazards and Exposure", tier=C,
 desc_pub=("Chemical hazards injure through inhalation, skin contact, ingestion, or injection: "
  "solvents damaging livers and nerves, silica scarring lungs, isocyanates sensitizing airways, "
  "corrosives burning tissue. Exposure depends on concentration, duration, and route.\n"
  "Control follows the hierarchy: substitute safer chemicals, ventilate (local exhaust beats "
  "dilution), enclose processes, then respirators and protective clothing as needed. Air "
  "monitoring proves controls work."),
 desc_sig=("Signature chemical management inventories every substance with its hazards and "
  "controls in one system, with exposure monitoring scheduled by risk."),
 how_pub=("Industrial hygienists inventory chemicals, review SDS and toxicology, and assess "
  "exposure via air sampling and biological monitoring. Controls are selected by hierarchy, "
  "implemented, and verified by repeat monitoring. Medical surveillance tracks exposed workers."),
 how_sig=("Signature risk-scheduled monitoring ensures high-risk exposures are re-verified, not "
  "assumed controlled."),
 keys=["Routes: inhalation, skin, ingestion, injection",
  "Examples: solvents, silica, isocyanates, corrosives",
  "Exposure = concentration x duration x route",
  "Hierarchy: substitute, ventilate, enclose, then PPE",
  "Air monitoring proves controls work",
  "Medical surveillance for exposed workers"],
 reqs=["Chemical inventory with SDS",
  "Exposure assessment capability",
  "Medical surveillance program"],
 stds=["OSHA PELs; NIOSH RELs; ACGIH TLVs (public)",
  "Substance-specific OSHA standards (public)"],
 cites=["Occupational Safety and Health Administration — chemical hazards (public)",
  "National Institute for Occupational Safety and Health — pocket guide (public)"],
 demo=("risk", {"hazards": [
   {"hazard": "Silica dust (no controls)", "likelihood": 4, "severity": 5},
   {"hazard": "Solvent vapors (LEV installed)", "likelihood": 2, "severity": 4},
   {"hazard": "Corrosive splash (goggles worn)", "likelihood": 2, "severity": 3}]})),

dict(title="Occupational Exposure Limits", tier=C,
 desc_pub=("Occupational exposure limits (OELs) cap airborne chemical concentrations: OSHA PELs "
  "(legal, often dated), NIOSH RELs (recommended), and ACGIH TLVs (consensus best practice, "
  "updated yearly). Expressed as 8-hour TWAs, short-term limits, and ceiling values.\n"
  "Best practice follows the most protective current limit, not merely the legal minimum. "
  "Limits assume healthy adult workers - sensitive individuals may need more protection."),
 desc_sig=("Signature exposure management tracks against the most protective current limits with "
  "automatic updates, so protection never lags behind science."),
 how_pub=("Hygienists compare monitoring results to applicable OELs, investigate exceedances, and "
  "upgrade controls until exposures are below limits with margin. Programs document the limit "
  "basis used and review when ACGIH updates."),
 how_sig=("Signature automatic limit updates keep assessments current with evolving science."),
 keys=["PELs (legal), RELs (NIOSH), TLVs (ACGIH)",
  "TWA, STEL, ceiling expressions",
  "Follow most protective current limit",
  "Limits assume healthy adults",
  "Investigate every exceedance",
  "Document the basis used"],
 reqs=["Current OEL references",
  "Monitoring vs limits comparison",
  "Exceedance response procedure"],
 stds=["OSHA PELs (public)", "ACGIH TLVs (public)"],
 cites=["American Conference of Governmental Industrial Hygienists — TLVs (public)",
  "National Institute for Occupational Safety and Health — RELs (public)"],
 demo=("rate", {"incidents": 3, "hours": 520000})),

dict(title="Industrial Hygiene Monitoring", tier=C,
 desc_pub=("Industrial hygiene monitoring measures exposures to prove controls work: personal air "
  "sampling (pumps on workers' breathing zones), area sampling, noise dosimetry, wipe sampling "
  "for surface contamination, and direct-reading instruments for screening.\n"
  "Strategy matters more than gadgets: sample the highest-exposed workers on worst-case days, "
  "use accredited labs, and interpret against OELs with statistics. Monitoring without action "
  "on results is theater."),
 desc_sig=("Signature monitoring programs run on risk-based sampling schedules with automatic "
  "exceedance alerts, turning measurements into managed protection."),
 how_pub=("Hygienists plan sampling strategy (who, when, what), calibrate equipment, collect "
  "samples with chain of custody, and analyze via accredited labs. Results are communicated to "
  "workers, compared to OELs, and drive control upgrades where needed."),
 how_sig=("Signature automatic exceedance alerts ensure results trigger action, not filing."),
 keys=["Personal air sampling in breathing zones",
  "Sample highest-exposed on worst-case days",
  "Accredited labs; statistics vs OELs",
  "Direct-reading instruments for screening",
  "Communicate results to workers",
  "Monitoring without action is theater"],
 reqs=["Sampling strategy and equipment",
  "Accredited laboratory",
  "Worker notification process"],
 stds=["NIOSH sampling methods (public)",
  "AIHA lab accreditation (public)"],
 cites=["National Institute for Occupational Safety and Health — methods (public)"],
 demo=("outcome", {"label": "Exposures below OELs", "pre": 78, "post": 97})),

dict(title="Noise and Hearing Conservation", tier=C,
 desc_pub=("Noise-induced hearing loss is permanent and preventable. OSHA requires hearing "
  "conservation programs at 85 dBA (8-hr TWA): monitoring, audiometric testing, hearing "
  "protection, training, and recordkeeping. Engineering controls - quieter equipment, enclosures "
  "- beat earplugs in the hierarchy.\n"
  "Audiograms detect early shifts before workers notice loss; standard threshold shifts trigger "
  "follow-up. Buy-quiet procurement prevents the problem at purchase."),
 desc_sig=("Signature hearing conservation tracks audiograms and noise maps together, targeting "
  "engineering fixes where protection alone is failing."),
 how_pub=("Employers monitor noise, identify exposed workers, establish baseline audiograms, and "
  "provide protection with training and fit. Annual audiograms catch shifts; engineers pursue "
  "quieter equipment; buy-quiet policies guide purchases."),
 how_sig=("Signature noise-map plus audiogram integration directs engineering dollars where "
  "they prevent the most loss."),
 keys=["Hearing loss: permanent and preventable",
  "85 dBA triggers conservation programs",
  "Engineering beats earplugs",
  "Audiograms catch early shifts",
  "Buy-quiet procurement",
  "Standard threshold shifts trigger follow-up"],
 reqs=["Noise monitoring",
  "Audiometric testing program",
  "Hearing protection + training"],
 stds=["OSHA noise standard (public)",
  "NIOSH hearing loss prevention (public)"],
 cites=["Occupational Safety and Health Administration — noise (public)",
  "National Institute for Occupational Safety and Health — hearing (public)"],
 demo=("controls", {"hazard": "Stamping press noise (95 dBA)",
   "controls": [{"level": "ppe", "measure": "Earplugs + earmuffs, fit-checked"},
                {"level": "engineering", "measure": "Acoustic enclosure on press"},
                {"level": "substitution", "measure": "Quieter servo press at replacement"},
                {"level": "administrative", "measure": "Limit time in press area"}]})),

dict(title="Ergonomics and Musculoskeletal Health", tier=C,
 desc_pub=("Ergonomics fits work to people, preventing musculoskeletal disorders (MSDs) - back "
  "injuries, carpal tunnel, tendonitis - the commonest workplace injuries. Risk factors: force, "
  "repetition, awkward posture, vibration, and duration.\n"
  "Solutions redesign work: adjustable workstations, lift assists, tool redesign, job rotation, "
  "and micro-breaks. Office ergonomics (monitor height, chair, keyboard) matters as much as "
  "factory lifting."),
 desc_sig=("Signature ergonomics programs score jobs with validated risk tools and track "
  "redesign projects to completion, making MSD prevention systematic."),
 how_pub=("Teams assess jobs with tools like REBA, NIOSH lifting equation, or HAL-TLV, "
  "prioritize by risk, and implement engineering fixes first. Workers participate in design; "
  "early-reporting programs catch symptoms before disability. Metrics: MSD rates and severity."),
 how_sig=("Signature risk-scored job inventories ensure the worst jobs get fixed first."),
 keys=["MSDs: commonest workplace injuries",
  "Risks: force, repetition, posture, vibration, duration",
  "Redesign work: lifts, tools, rotation, breaks",
  "Office ergonomics matters too",
  "Early reporting catches symptoms early",
  "Workers participate in design"],
 reqs=["Ergonomic assessment tools",
  "Redesign project capacity",
  "Early-reporting program"],
 stds=["OSHA ergonomic guidelines (public)",
  "ANSI Z365 (public, in development reference)"],
 cites=["Occupational Safety and Health Administration — ergonomics (public)",
  "National Institute for Occupational Safety and Health — ergonomics (public)"],
 demo=("risk", {"hazards": [
   {"hazard": "Manual 50-lb lifting", "likelihood": 5, "severity": 4},
   {"hazard": "Repetitive assembly (redesigned)", "likelihood": 2, "severity": 3},
   {"hazard": "Poor monitor setup", "likelihood": 4, "severity": 2}]})),

dict(title="Heat and Cold Stress", tier=C,
 desc_pub=("Heat stress kills: heat stroke is a medical emergency. Prevention means water, rest, "
  "shade (or cool areas), acclimatization for new workers, and monitoring (buddy systems, "
  "supervisor checks). OSHA's heat emphasis and state standards (like California's) drive "
  "program requirements.\n"
  "Cold stress brings frostbite and hypothermia: layered clothing, warm shelters, work/warm-up "
  "schedules, and watching for the 'umbles' (stumbles, mumbles, fumbles). Both demand emergency "
  "plans."),
 desc_sig=("Signature thermal-stress programs pair weather monitoring with automatic work/rest "
  "adjustments, so protection scales with conditions."),
 how_pub=("Employers monitor heat index/wind chill, implement water-rest-shade protocols, "
  "acclimatize new workers gradually, train on symptom recognition, and empower anyone to call "
  "for help. Emergency procedures cover heat stroke and hypothermia response."),
 how_sig=("Signature weather-triggered protocols adjust protections automatically with "
  "conditions."),
 keys=["Heat stroke is a medical emergency",
  "Water, rest, shade; acclimatize new workers",
  "Buddy systems and supervisor checks",
  "Cold: layers, shelters, warm-up schedules",
  "Watch for the 'umbles'",
  "Anyone can call for help"],
 reqs=["Heat/cold illness prevention plan",
  "Water, shade, shelter provisions",
  "Symptom training and emergency procedures"],
 stds=["OSHA heat guidance; CA heat standard (public)",
  "NIOSH heat criteria (public)"],
 cites=["Occupational Safety and Health Administration — heat (public)",
  "National Institute for Occupational Safety and Health — heat (public)"],
 demo=("protocol", {"steps": ["Monitor heat index/wind chill", "Provide water/rest/shade",
   "Acclimatize new workers", "Train symptom recognition",
   "Buddy system checks", "Emergency response ready"]})),

dict(title="Electrical Safety", tier=C,
 desc_pub=("Electricity kills through shock, arc flash, and fire. Core protections: qualified "
  "workers only for electrical tasks, lockout/tagout before servicing, insulated tools and PPE "
  "(arc-rated clothing), ground-fault protection, and maintaining approach boundaries.\n"
  "Arc flash - explosive energy release - demands hazard analysis and labeled equipment. "
  "Overhead power lines kill regularly: maintain clearance, use spotters, assume all lines are "
  "energized."),
 desc_sig=("Signature electrical safety programs track qualified-worker authorizations, LOTO "
  "compliance, and arc-flash labeling in one system."),
 how_pub=("Employers qualify electrical workers, implement LOTO procedures with verification, "
  "provide arc-rated PPE per incident-energy analysis, label equipment, and train on power-line "
  "clearances. Audits verify LOTO discipline."),
 how_sig=("Signature authorization tracking ensures only qualified workers touch electrical "
  "systems."),
 keys=["Shock, arc flash, fire",
  "Qualified workers only",
  "Lockout/tagout before servicing",
  "Arc-rated PPE per analysis",
  "Assume all lines energized",
  "Maintain approach boundaries"],
 reqs=["Qualified electrical workers",
  "LOTO program",
  "Arc-flash analysis and labeling"],
 stds=["OSHA electrical standards (public)",
  "NFPA 70E (public)"],
 cites=["Occupational Safety and Health Administration — electrical (public)",
  "National Fire Protection Association — 70E (public)"],
 demo=("controls", {"hazard": "Servicing energized panel",
   "controls": [{"level": "ppe", "measure": "Arc-rated suit, insulated gloves"},
                {"level": "engineering", "measure": "De-energize via LOTO (preferred)"},
                {"level": "administrative", "measure": "Energized work permit + standby"}]})),

dict(title="Machine Guarding", tier=C,
 desc_pub=("Machines crush, cut, and amputate where guards are missing: rotating parts, nip "
  "points, and flying chips need fixed guards, interlocks, or presence-sensing devices. OSHA's "
  "machine guarding standard is among the most cited - because missing guards maim predictably.\n"
  "Safeguarding hierarchy: eliminate the hazard by design, then guards, then devices, then "
  "procedures. Bypassing guards for convenience is a firing offense in strong programs - and a "
  "fatal habit everywhere."),
 desc_sig=("Signature machine safety inventories every machine's safeguards with inspection "
  "schedules, so missing guards are found by system, not by injury."),
 how_pub=("Employers inventory machines, assess each point of operation and power transmission, "
  "install appropriate guards/devices, and inspect regularly. Workers are trained never to "
  "bypass; bypassing is disciplined. New equipment is purchased guarded."),
 how_sig=("Signature safeguard inventories with inspection tracking prevent guard erosion."),
 keys=["Guards for rotation, nip points, flying chips",
  "Most-cited OSHA standard - missing guards maim",
  "Hierarchy: design, guards, devices, procedures",
  "Never bypass guards",
  "Inspect regularly",
  "Purchase guarded equipment"],
 reqs=["Machine inventory and assessment",
  "Guard installation",
  "Inspection and no-bypass enforcement"],
 stds=["OSHA machine guarding (public)",
  "ANSI B11 series (public)"],
 cites=["Occupational Safety and Health Administration — machine guarding (public)"],
 demo=("risk", {"hazards": [
   {"hazard": "Unguarded press nip point", "likelihood": 4, "severity": 5},
   {"hazard": "Guarded lathe (interlocked)", "likelihood": 1, "severity": 4},
   {"hazard": "Grinder without eye guard", "likelihood": 3, "severity": 3}]})),

dict(title="Fall Protection", tier=C,
 desc_pub=("Falls are the leading killer in construction. OSHA requires protection at 6 feet in "
  "construction (4 feet general industry): guardrails, safety nets, or personal fall arrest "
  "systems - with harnesses, anchored lifelines, and rescue plans (suspension trauma kills "
  "rescued-too-late workers).\n"
  "Prevention hierarchy: eliminate work at height, then passive protection (rails), then active "
  "(harnesses). Competent persons inspect systems; workers are trained before exposure."),
 desc_sig=("Signature fall-protection programs track anchor certifications, harness inspections, "
  "and rescue-plan drills per site."),
 how_pub=("Employers plan fall protection per task before work begins, install rails or nets "
  "where feasible, issue inspected harnesses with engineered anchors otherwise, and drill "
  "rescue. Daily inspections precede use; incidents trigger re-planning."),
 how_sig=("Signature pre-task fall planning makes protection designed, not improvised."),
 keys=["Leading killer in construction",
  "6 ft construction / 4 ft general industry triggers",
  "Rails, nets, or personal fall arrest",
  "Rescue plans: suspension trauma kills",
  "Plan before work begins",
  "Inspect daily; train before exposure"],
 reqs=["Fall protection plan per task",
  "Engineered anchors and inspected harnesses",
  "Rescue plan and drills"],
 stds=["OSHA fall protection standards (public)",
  "ANSI/ASSP Z359 (public)"],
 cites=["Occupational Safety and Health Administration — fall protection (public)"],
 demo=("controls", {"hazard": "Roof work at 20 feet",
   "controls": [{"level": "ppe", "measure": "Harness + anchored lifeline + rescue plan"},
                {"level": "engineering", "measure": "Guardrails at roof edge (preferred)"},
                {"level": "elimination", "measure": "Do work from lift instead of roof"}]})),

dict(title="Confined Spaces", tier=C,
 desc_pub=("Confined spaces - tanks, silos, sewers, pits - kill through atmospheric hazards "
  "(oxygen deficiency, toxics, flammables) and engulfment. OSHA's permit-required confined space "
  "standard mandates: atmospheric testing, ventilation, attendants, rescue plans, and permits.\n"
  "The classic tragedy: would-be rescuers dying attempting rescue without equipment. "
  "Non-entry rescue (tripods, winches) is the rule; entry rescue requires trained teams on "
  "standby."),
 desc_sig=("Signature confined-space programs manage permits, atmospheric test records, and "
  "rescue-team readiness digitally per entry."),
 how_pub=("Employers identify all confined spaces, classify permit-required ones, and implement "
  "the entry program: pre-entry testing and continuous monitoring, ventilation, attendant posted, "
  "rescue equipment ready, permit signed. No permit, no entry."),
 how_sig=("Signature digital permits enforce every prerequisite before authorizing entry."),
 keys=["Atmospheric hazards + engulfment kill",
  "Permit-required: test, ventilate, attendant, rescue plan",
  "Would-be rescuers are classic victims",
  "Non-entry rescue is the rule",
  "Continuous atmospheric monitoring",
  "No permit, no entry"],
 reqs=["Confined space inventory and classification",
  "Testing and ventilation equipment",
  "Rescue capability"],
 stds=["OSHA confined space standard (public)",
  "ANSI/ASSP Z117.1 (public)"],
 cites=["Occupational Safety and Health Administration — confined spaces (public)"],
 demo=("protocol", {"steps": ["Classify the space", "Issue permit",
   "Test atmosphere pre-entry", "Ventilate continuously", "Post attendant",
   "Stage non-entry rescue gear", "Monitor atmosphere continuously"]})),

dict(title="Respiratory Protection", tier=C,
 desc_pub=("Respirators protect where engineering cannot: dust masks (N95) for particulates, half-"
  "and full-face elastomerics with cartridges for gases/vapors, PAPRs for higher protection, "
  "SCBAs for oxygen-deficient atmospheres. OSHA requires a written program: medical evaluation, "
  "fit-testing, training, and maintenance.\n"
  "The protection factor is only real with fit and discipline: facial hair breaks seals, and "
  "wrong cartridges give false confidence. Voluntary use has lighter requirements but still "
  "needs information."),
 desc_sig=("Signature respiratory programs track medical clearances, fit-tests, and cartridge "
  "change schedules per worker, so protection is real, not assumed."),
 how_pub=("Employers assess respiratory hazards, select NIOSH-approved respirators, arrange "
  "medical evaluations and fit-testing, train on use and limits, and maintain equipment. "
  "Change schedules are enforced; program effectiveness is evaluated yearly."),
 how_sig=("Signature per-worker tracking ensures no one wears an unfit-tested respirator."),
 keys=["N95, elastomeric, PAPR, SCBA - matched to hazard",
  "Written program: medical, fit-test, training, maintenance",
  "Fit is protection: facial hair breaks seals",
  "Right cartridge for the contaminant",
  "Enforce change schedules",
  "Evaluate program yearly"],
 reqs=["NIOSH-approved respirators",
  "Medical evaluation + fit-testing",
  "Training and maintenance"],
 stds=["OSHA respiratory protection (public)",
  "NIOSH respirator approvals (public)"],
 cites=["Occupational Safety and Health Administration — respirators (public)"],
 demo=("controls", {"hazard": "Isocyanate paint vapors",
   "controls": [{"level": "ppe", "measure": "Supplied-air respirator, fit-tested"},
                {"level": "engineering", "measure": "Spray booth ventilation (preferred)"},
                {"level": "substitution", "measure": "Water-based coating where feasible"}]})),

dict(title="Incident Investigation", tier=C,
 desc_pub=("Incident investigation finds system causes, not culprits: secure the scene, collect "
  "facts (who, what, when, where, how), interview witnesses promptly, analyze with methods like "
  "'5 whys' or fishbone diagrams, and fix root causes - not just symptoms.\n"
  "The test of a good investigation is whether the corrective actions would prevent recurrence "
  "if the same people made the same honest mistake. Blame stops learning; systems thinking "
  "starts it."),
 desc_sig=("Signature investigations run structured root-cause workflows with corrective-action "
  "tracking to verification, so investigations reliably prevent recurrence."),
 how_pub=("Teams respond immediately (care, secure scene), gather evidence within 24 hours, "
  "interview witnesses separately, analyze to root causes, and assign corrective actions with "
  "owners and deadlines. Effectiveness is verified later - did the fix hold?"),
 how_sig=("Signature corrective-action tracking to verification closes the investigation "
  "loop."),
 keys=["Find system causes, not culprits",
  "Secure scene; collect facts fast",
  "5 whys / fishbone for root causes",
  "Fix root causes, not symptoms",
  "Blame stops learning",
  "Verify fixes held"],
 reqs=["Investigation procedure and team",
  "Root-cause method training",
  "Corrective-action tracking"],
 stds=["Incident investigation guidance (public literature, e.g., CCPS)"],
 cites=["National Safety Council — investigation resources (public)",
  "Center for Chemical Process Safety — investigation (public)"],
 demo=("protocol", {"steps": ["Secure scene, care for injured", "Collect facts within 24 hrs",
   "Interview witnesses separately", "Analyze to root causes",
   "Assign corrective actions with owners", "Verify fixes held"]})),

# ---------------- Advanced (11) ----------------
dict(title="Process Safety Management", tier=A,
 desc_pub=("Process Safety Management (PSM) prevents catastrophic chemical releases: OSHA's "
  "standard requires process hazard analyses, operating procedures, management of change, "
  "pre-startup reviews, mechanical integrity, and incident investigation for covered highly "
  "hazardous processes.\n"
  "PSM is systems thinking at scale - the difference between managing safety and managing "
  "catastrophe risk. Major incidents (Bhopal, Texas City) wrote these requirements in "
  "consequence."),
 desc_sig=("Signature PSM operations digitize every element - PHAs, MOC, mechanical integrity - "
  "with action tracking, so process safety is continuously managed, not periodically "
  "documented."),
 how_pub=("Facilities compile process safety information, conduct PHAs with action resolution, "
  "write operating procedures, control changes through MOC, verify mechanical integrity on "
  "schedule, and audit compliance every three years. Every element has tracked actions."),
 how_sig=("Signature element-digitization makes PSM a living system with visible action "
  "closure."),
 keys=["Prevents catastrophic chemical releases",
  "PHA, procedures, MOC, pre-startup, mechanical integrity",
  "Systems thinking at scale",
  "Audit every 3 years",
  "Track every action to closure",
  "Consequence wrote these requirements"],
 reqs=["Covered process determination",
  "PHA team capability",
  "MOC and integrity programs"],
 stds=["OSHA PSM standard (public)",
  "EPA RMP rule (public)"],
 cites=["Occupational Safety and Health Administration — PSM (public)",
  "Center for Chemical Process Safety — guidelines (public)"],
 demo=("protocol", {"steps": ["Compile process safety information", "Conduct PHA",
   "Resolve PHA actions", "Write operating procedures", "Implement MOC",
   "Verify mechanical integrity", "Audit every 3 years"]})),

dict(title="Safety Management Systems", tier=A,
 desc_pub=("Safety management systems (SMS) organize all safety activity into a managed whole: "
  "ISO 45001 and ANSI/ASSP Z10 structure policy, planning, implementation, checking, and "
  "management review in a Plan-Do-Check-Act cycle. An SMS turns scattered safety tasks into a "
  "system that improves itself.\n"
  "Certification audits verify the system works, not just that documents exist. Leadership "
  "accountability and worker participation are the standard's backbone."),
 desc_sig=("Signature SMS implementations run the PDCA cycle on digital rails with metric "
  "dashboards per element, making systematic improvement the default."),
 how_pub=("Organizations adopt the standard, assess gaps, and build each element with assigned "
  "owners. Internal audits check effectiveness; management reviews steer resources; "
  "certification audits validate. The cycle repeats - improvement is the product."),
 how_sig=("Signature element dashboards make SMS health visible continuously."),
 keys=["Policy, planning, implementation, checking, review",
  "Plan-Do-Check-Act cycle",
  "ISO 45001 / ANSI Z10",
  "System that improves itself",
  "Audits verify it works",
  "Leadership + worker participation backbone"],
 reqs=["Standard adoption decision",
  "Element owners",
  "Audit and review cadence"],
 stds=["ISO 45001 (public)", "ANSI/ASSP Z10 (public)"],
 cites=["International Organization for Standardization — 45001 (public)"],
 demo=("outcome", {"label": "SMS element audit scores", "pre": 68, "post": 91})),

dict(title="Job Hazard Analysis", tier=A,
 desc_pub=("Job hazard analysis (JHA, also JSA) breaks jobs into steps, identifies each step's "
  "hazards, and defines controls - creating the safe procedure before work starts. It is the "
  "bridge between hazard identification and safe work instructions.\n"
  "Done with the workers doing the job, JHAs capture practical knowledge procedures miss. "
  "Review triggers: new equipment, incidents, or periodic refresh."),
 desc_sig=("Signature JHA libraries make analyses reusable across similar jobs with version "
  "control, so knowledge compounds instead of being reinvented."),
 how_pub=("Teams list job steps with experienced workers, identify hazards per step, select "
  "controls by hierarchy, and write the safe procedure. Workers are trained on it; supervisors "
  "observe compliance; JHAs are reviewed on trigger events."),
 how_sig=("Signature versioned JHA libraries turn each analysis into reusable organizational "
  "knowledge."),
 keys=["Steps, hazards per step, controls",
  "Creates safe procedure before work",
  "Done with workers doing the job",
  "Bridge from identification to instruction",
  "Review on new equipment, incidents, schedule",
  "Observe compliance"],
 reqs=["JHA procedure and forms",
  "Worker involvement",
  "Review triggers"],
 stds=["JHA guidance (public literature, e.g., OSHA)"],
 cites=["Occupational Safety and Health Administration — JHA (public)"],
 demo=("risk", {"hazards": [
   {"hazard": "Step 3: unguarded blade exposure", "likelihood": 3, "severity": 5},
   {"hazard": "Step 5: awkward lift", "likelihood": 4, "severity": 3},
   {"hazard": "Step 1: slip on oil (controlled)", "likelihood": 1, "severity": 2}]})),

dict(title="Leading and Lagging Indicators", tier=A,
 desc_pub=("Lagging indicators (injury rates, TRIR, workers' comp costs) measure past harm; "
  "leading indicators (near-miss reports, training completion, audit scores, safety meeting "
  "attendance) measure current safety activity and predict future performance.\n"
  "Mature programs manage by leading indicators - steering by the windshield, not the rearview "
  "mirror. Both are needed: leading for action, lagging for validation."),
 desc_sig=("Signature safety analytics blend leading and lagging indicators into predictive "
  "dashboards, so intervention precedes injury."),
 how_pub=("Organizations select a balanced metric set, build data collection into operations, "
  "review dashboards monthly with action assignments, and validate that leading-indicator "
  "improvements actually move lagging results."),
 how_sig=("Signature predictive dashboards link leading actions to lagging outcomes "
  "visibly."),
 keys=["Lagging: past harm (TRIR, costs)",
  "Leading: current activity (near-misses, training, audits)",
  "Manage by leading; validate by lagging",
  "Windshield vs rearview mirror",
  "Balanced metric sets",
  "Prove leading moves lagging"],
 reqs=["Balanced indicator set",
  "Data collection in operations",
  "Monthly review with actions"],
 stds=["Safety metrics guidance (public literature, e.g., Campbell Institute)"],
 cites=["National Safety Council — metrics (public)"],
 demo=("rate", {"incidents": 4, "hours": 500000})),

dict(title="Behavior-Based Safety", tier=A,
 desc_pub=("Behavior-based safety (BBS) improves safety through observation and feedback: trained "
  "observers watch work, note safe and at-risk behaviors, and give immediate constructive "
  "feedback. Data reveals patterns driving targeted fixes.\n"
  "Done well it builds engagement; done as blame surveillance it destroys trust. Best practice "
  "pairs BBS with robust hazard controls - behavior programs never substitute for engineering."),
 desc_sig=("Signature BBS design anonymizes observation data and ties it to system fixes, keeping "
  "the focus on conditions rather than individuals."),
 how_pub=("Organizations train observers, define critical behaviors, and run observation rounds "
  "with feedback. Data is analyzed for patterns; systemic fixes follow. Participation is "
  "voluntary and non-punitive by design."),
 how_sig=("Signature anonymized pattern analysis keeps BBS about systems, not surveillance."),
 keys=["Observe work; feedback on behaviors",
  "Data reveals patterns for fixes",
  "Builds engagement when done well",
  "Never substitutes for engineering controls",
  "Voluntary and non-punitive",
  "Focus on conditions, not individuals"],
 reqs=["Observer training",
  "Critical behavior definitions",
  "Non-punitive design"],
 stds=["BBS practice guidance (public literature)"],
 cites=["Cambridge Center for Behavioral Studies — BBS (public)"],
 demo=("outcome", {"label": "Safe behaviors observed", "pre": 71, "post": 93})),

dict(title="Occupational Health Surveillance", tier=A,
 desc_pub=("Health surveillance tracks worker health to catch work-related disease early: "
  "audiograms for noise, spirometry for respiratory hazards, blood lead levels, medical "
  "exams for respirator users. Surveillance finds problems exposure monitoring misses - in "
  "people, not air.\n"
  "Results trigger individual follow-up and program review; trends across workers reveal "
  "failing controls. Confidentiality protects workers while aggregated data guides prevention."),
 desc_sig=("Signature health surveillance links exposure and health data per worker cohort, so "
  "control failures surface from either side."),
 how_pub=("Programs define surveillance by hazard, schedule testing, use qualified providers, and "
  "follow up abnormal results promptly. Aggregated trends are reviewed with exposure data; "
  "controls improve where health effects appear."),
 how_sig=("Signature exposure-health linkage catches control failures from both measurements."),
 keys=["Audiograms, spirometry, blood lead, respirator exams",
  "Finds problems in people, not air",
  "Triggers individual follow-up",
  "Trends reveal failing controls",
  "Confidentiality for workers",
  "Aggregates guide prevention"],
 reqs=["Hazard-based surveillance protocols",
  "Qualified medical providers",
  "Trend review process"],
 stds=["OSHA medical surveillance requirements (public)",
  "NIOSH surveillance guidance (public)"],
 cites=["National Institute for Occupational Safety and Health — surveillance (public)"],
 demo=("outcome", {"label": "Surveillance participants with follow-up completed", "pre": 69, "post": 95})),

dict(title="Return-to-Work Programs", tier=A,
 desc_pub=("Return-to-work programs bring injured workers back safely and sooner: transitional "
  "duty matching medical restrictions, graduated schedules, and coordination among worker, "
  "supervisor, and medical provider. Early return - to real, accommodated work - heals better "
  "than prolonged absence.\n"
  "Success needs pre-identified light-duty options and a culture that welcomes returners. "
  "Workers' comp costs fall as durations shrink."),
 desc_sig=("Signature return-to-work coordination matches restrictions to a bank of transitional "
  "tasks automatically, removing the 'no light duty available' bottleneck."),
 how_pub=("Employers build transitional-duty banks before injuries, train supervisors in "
  "accommodation, and coordinate each case: restrictions from the provider, matched tasks, "
  "check-ins, and progression to full duty. Outcomes tracked: durations and re-injury."),
 how_sig=("Signature restriction-to-task matching automates the hardest coordination step."),
 keys=["Transitional duty matching restrictions",
  "Early return heals better than absence",
  "Pre-identified light-duty banks",
  "Coordinate worker, supervisor, provider",
  "Welcoming culture for returners",
  "Track durations and re-injury"],
 reqs=["Transitional-duty task bank",
  "Supervisor training",
  "Case coordination"],
 stds=["Return-to-work best practices (public literature)"],
 cites=["American College of Occupational Medicine — return to work (public)"],
 demo=("outcome", {"label": "Average lost workdays per injury (lower better)", "pre": 24, "post": 11})),

dict(title="Contractor Safety Management", tier=A,
 desc_pub=("Contractors bring unfamiliar workers into your hazards - contractor safety management "
  "qualifies them before they arrive: prequalification (safety records, programs), site-specific "
  "orientation, work permits, and oversight with stop-work authority.\n"
  "Host employers retain responsibility for site hazards; contractors for their workers' safety. "
  "Multi-employer citation policy means OSHA can cite hosts for contractor exposures they "
  "controlled."),
 desc_sig=("Signature contractor management runs prequalification, orientation, and permit "
  "tracking on one platform, so no unvetted contractor works unobserved."),
 how_pub=("Hosts prequalify contractors on safety performance, orient them to site hazards and "
  "rules, issue permits for hazardous work, and monitor with stop-work authority. Performance "
  "is reviewed; poor performers are removed."),
 how_sig=("Signature unified tracking ensures qualification precedes every contractor's first "
  "day."),
 keys=["Prequalify before they arrive",
  "Site-specific orientation",
  "Permits for hazardous work",
  "Stop-work authority",
  "Hosts own site hazards",
  "Review performance; remove poor performers"],
 reqs=["Prequalification criteria",
  "Orientation program",
  "Oversight with stop-work authority"],
 stds=["OSHA multi-employer policy (public)",
  "Contractor management guidance (public literature)"],
 cites=["Occupational Safety and Health Administration — multi-employer (public)"],
 demo=("outcome", {"label": "Contractors meeting prequalification bar", "pre": 62, "post": 94})),

dict(title="Audits and Inspections", tier=A,
 desc_pub=("Audits and inspections verify safety systematically: inspections find physical "
  "hazards; audits evaluate the management system. Both need trained auditors, clear criteria, "
  "scored findings, tracked corrective actions, and management review.\n"
  "The audit cycle - plan, conduct, report, correct, verify - is where findings become "
  "improvements. Third-party audits add independence; internal audits add frequency."),
 desc_sig=("Signature audit management schedules, scores, and tracks every finding to verified "
  "closure, making assurance continuous."),
 how_pub=("Organizations set audit schedules by risk, train auditors, and conduct with standard "
  "protocols. Findings are scored and assigned; corrective actions track to verification; "
  "management reviews trends and resources the fixes."),
 how_sig=("Signature finding-to-closure tracking makes audit value measurable."),
 keys=["Inspections find hazards; audits evaluate systems",
  "Trained auditors, clear criteria",
  "Score findings; track corrections",
  "Verify fixes held",
  "Third-party: independence; internal: frequency",
  "Management reviews trends"],
 reqs=["Audit schedule by risk",
  "Trained auditors",
  "Corrective-action tracking"],
 stds=["Safety audit standards (public literature, e.g., ISO 45001 audits)"],
 cites=["American Society of Safety Professionals — audit resources (public)"],
 demo=("outcome", {"label": "Audit findings closed on time", "pre": 66, "post": 92})),

dict(title="Emergency Preparedness and Drills", tier=A,
 desc_pub=("Workplace emergency preparedness readies for fires, chemical releases, severe weather, "
  "and violence: plans, alarms, evacuation, shutdown, rescue, headcounts - proven by drills. "
  "Drills must test reality: unannounced timing, blocked-route scenarios, accountability checks.\n"
  "After-action reviews convert each drill into improvements. Coordination with local "
  "responders - pre-incident tours, joint exercises - pays off when seconds count."),
 desc_sig=("Signature drill programs score performance per scenario with improvement tracking, "
  "turning exercises into measured readiness gains."),
 how_pub=("Employers write all-hazard plans, assign roles, install alarms, and drill at least "
  "annually with varied scenarios. Responders tour the site; joint exercises test coordination. "
  "After-actions drive plan updates."),
 how_sig=("Signature scenario-scored drills quantify readiness instead of assuming it."),
 keys=["Plans + alarms + roles + drills",
  "Test reality: unannounced, blocked routes",
  "Accountability checks",
  "After-actions drive improvements",
  "Coordinate with local responders",
  "Pre-incident tours pay off"],
 reqs=["All-hazard emergency plan",
  "Drill program with scenarios",
  "Responder coordination"],
 stds=["OSHA emergency standards (public)",
  "NFPA 1600 (public)"],
 cites=["Federal Emergency Management Agency — preparedness (public)"],
 demo=("outcome", {"label": "Successful full evacuations in drills", "pre": 71, "post": 97})),

dict(title="The Future of Workplace Safety", tier=A,
 desc_pub=("Workplace safety's future: wearable sensors detecting fatigue and heat strain, "
  "computer vision spotting missing PPE, AI-assisted hazard recognition, exoskeletons reducing "
  "strain, and predictive analytics forecasting incidents from leading indicators.\n"
  "The through-line is augmentation, not replacement: technology extending human vigilance "
  "while the hierarchy of controls and safety culture remain the foundation. Privacy and "
  "worker trust must be designed in, not bolted on."),
 desc_sig=("The Signature future-state is a safety operating system: sensed hazards, "
  "AI-assisted recognition, predictive intervention, and outcome accountability - with worker "
  "trust as a design requirement. This database is a prototype of that system's knowledge "
  "core."),
 how_pub=("Organizations pilot sensing and AI tools with worker involvement, validate that "
  "predictions actually prevent harm, protect privacy by design, and keep engineering controls "
  "primary. Culture work continues - technology never substitutes for it."),
 how_sig=("Signature's operating-system vision keeps the hierarchy and culture as the "
  "foundation technology serves."),
 keys=["Wearables, vision AI, exoskeletons, predictive analytics",
  "Augmentation, not replacement",
  "Hierarchy and culture remain the foundation",
  "Privacy and trust designed in",
  "Validate predictions prevent harm",
  "Worker involvement in pilots"],
 reqs=["Pilot evaluation discipline",
  "Privacy-by-design",
  "Culture investment alongside tech"],
 stds=["Emerging standards for safety AI (public literature)"],
 cites=["National Safety Council — future of safety (public)",
  "National Institute for Occupational Safety and Health — future of work (public)"],
 demo=("outcome", {"label": "Incidents predicted and prevented", "pre": 18, "post": 52})),
]
