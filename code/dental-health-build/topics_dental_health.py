#!/usr/bin/env python3
"""Topics + config for the dental-health pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never medical advice. No dosages, no cure claims.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "dental-health",
    "name_pub": "The Dental Health Database",
    "name_sig": "Signature Dental Health Database",
    "tagline_pub": ("Dental health from the ground up: tooth anatomy, diagnostics and imaging, "
                    "restorative materials, procedures from fillings to implants, dental equipment, "
                    "and oral health outcomes - every record carrying the full entry taught "
                    "progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of dental health: the same real "
                    "dental knowledge carried forward, plus Signature-built diagnostic models, "
                    "treatment-planning frameworks, and outcome systems original to this system."),
    "record_kind": "dental health record",
    "record_kind_plural": "dental health records",
    "prefix_pub": "JAH-DENT-", "prefix_sig": "JAH-DENTS-",
    "ai_pub": "JAH Dental Health Archivist",
    "ai_sig": "JAH Signature Dental Health Creator",
    "role_pub": ("dental health archivist - teaching anatomy, diagnostics, materials, procedures, "
                 "equipment, and outcomes; answers from many angles - definition, example, "
                 "process, procedure, outcome - using only archive data from this system"),
    "role_sig": ("Signature creator of dental health systems - designing diagnostic models, "
                 "treatment frameworks, and outcome systems as original Signature works; answers "
                 "from many angles using only archive data from this system"),
    "search_ph": "Search anatomy, diagnostics, materials, procedures, equipment...",
    "chat_ph": "Ask about dental health...",
    "greet_pub": ("I am the JAH Dental Health Archivist. Ask me about tooth anatomy, diagnostics, "
                  "materials, procedures, and equipment. Educational information only - personal "
                  "dental decisions belong with a qualified dentist."),
    "greet_sig": ("I am the JAH Signature Dental Health Creator. Ask me about Signature-built "
                  "dental systems. Educational information only."),
    "gen_blurb": ("Generate clearly-labeled dental health studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded dental health records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. "
                      "Educational information only — not medical advice."),
    "demo_kind": "dental-demo",
    "demo_title": "Dental Health Demo",
    "health": True,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Dental Health Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "chart":
        return fill(
            "teeth = @@TEETH@@\n"
            "print('Dental chart (Universal numbering):')\n"
            "for t in teeth:\n"
            "    print(' Tooth %s: %s — %s' % (t['num'], t['name'], t['status']))\n"
            "issues = [t for t in teeth if t['status'] != 'healthy']\n"
            "print('Teeth needing attention:', len(issues))\n",
            {"TEETH": p["teeth"]})
    if v == "risk":
        return fill(
            "factors = @@FACTORS@@\n"
            "score = sum(f['weight'] for f in factors if f['present'])\n"
            "level = 'low' if score < 3 else 'moderate' if score < 6 else 'high'\n"
            "print('Caries risk factors assessed:', len(factors))\n"
            "print('Risk score:', score, '->', level, 'risk')\n"
            "for f in factors:\n"
            "    if f['present']:\n"
            "        print(' RISK FACTOR:', f['factor'])\n",
            {"FACTORS": p["factors"]})
    if v == "material":
        return fill(
            "mats = @@MATS@@\n"
            "ranked = sorted(mats, key=lambda m: m['score'], reverse=True)\n"
            "print('Restorative material comparison:')\n"
            "for m in ranked:\n"
            "    print(' %s: %d/10 — %s' % (m['name'], m['score'], m['note']))\n",
            {"MATS": p["materials"]})
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
            "print('Clinical protocol:')\n"
            "for i, s in enumerate(steps, 1):\n"
            "    print(' %d. %s' % (i, s))\n",
            {"STEPS": p["steps"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Dental Health Is", tier=F,
 desc_pub=("Dental health (oral health) is the state of the teeth, gums, and mouth that lets people "
  "eat, speak, and socialize without pain or embarrassment. It covers prevention (brushing, "
  "flossing, fluoride, diet), diagnosis (exams, x-rays), and treatment (fillings, crowns, root "
  "canals, gum therapy, orthodontics, implants).\n"
  "Oral health connects to whole-body health: gum disease associates with diabetes and heart "
  "disease, and dental infections can become serious. Care is delivered by dentists, hygienists, "
  "assistants, and specialists in offices, clinics, schools, and mobile units."),
 desc_sig=("The Signature system models oral health as a lifelong prevention-to-restoration "
  "continuum with risk-based recall intervals, so care intensity follows individual risk rather "
  "than one-size-fits-all schedules."),
 how_pub=("People maintain daily hygiene at home and visit dental professionals for exams and "
  "cleanings on a schedule matched to risk. Problems found are diagnosed with clinical exam and "
  "imaging, then treated from least to most invasive. Prevention counseling runs through every "
  "visit."),
 how_sig=("Signature risk-based recall assigns cleaning and exam intervals from individual risk "
  "scores, focusing resources where disease is likeliest."),
 keys=["Teeth, gums, mouth: eat, speak, socialize without pain",
  "Prevention, diagnosis, treatment",
  "Links to whole-body health",
  "Team: dentists, hygienists, assistants, specialists",
  "Daily home care + professional visits",
  "Prevention counseling at every visit"],
 reqs=["Daily oral hygiene routine",
  "Regular professional exams and cleanings",
  "Access to restorative care when needed"],
 stds=["ADA prevention guidelines (public)",
  "State dental practice acts"],
 cites=["American Dental Association — public resources (public)",
  "Centers for Disease Control — oral health (public)"],
 demo=("risk", {"factors": [
   {"factor": "Frequent sugary snacks", "weight": 2, "present": True},
   {"factor": "No fluoride exposure", "weight": 2, "present": False},
   {"factor": "Dry mouth", "weight": 1, "present": True},
   {"factor": "Previous cavities", "weight": 2, "present": True}]})),

dict(title="Tooth Anatomy", tier=F,
 desc_pub=("Each tooth has a crown (visible part) covered by enamel - the hardest substance in the "
  "body - and roots anchored in the jawbone. Beneath enamel lies dentin (softer, sensitive), and "
  "at the core the pulp holds nerves and blood vessels. Cementum covers roots; the periodontal "
  "ligament suspends each tooth in its socket.\n"
  "Adults typically have 32 teeth: 8 incisors (cutting), 4 canines (tearing), 8 premolars "
  "(crushing), 12 molars (grinding, including wisdom teeth). Children have 20 primary teeth, "
  "lost as permanent teeth erupt from about age 6."),
 desc_sig=("The Signature anatomy reference pairs each structure with its clinical significance - "
  "what fails, how it presents, how it is treated - turning anatomy into a diagnostic map."),
 how_pub=("Dentists use anatomy knowledge in every exam: enamel condition, dentin exposure, pulp "
  "symptoms (hot/cold sensitivity, lingering pain), and supporting structures. Charting records "
  "each tooth's surfaces and condition using standard numbering."),
 how_sig=("Signature charting links each anatomical finding to likely diagnoses and treatment "
  "options automatically."),
 keys=["Crown, enamel, dentin, pulp, cementum, ligament, bone",
  "Enamel: hardest substance in the body",
  "32 permanent teeth; 20 primary teeth",
  "Incisors cut, canines tear, premolars crush, molars grind",
  "Pulp holds nerves and vessels",
  "Anatomy guides every diagnosis"],
 reqs=["Anatomy knowledge for all dental staff",
  "Standard tooth-numbering system",
  "Charting at every exam"],
 stds=["Dental anatomy education standards (public)",
  "Universal/FDI numbering conventions (public)"],
 cites=["American Dental Association — tooth anatomy (public)"],
 demo=("chart", {"teeth": [
   {"num": "3", "name": "Upper right first molar", "status": "healthy"},
   {"num": "14", "name": "Upper left first molar", "status": "filling present"},
   {"num": "19", "name": "Lower left first molar", "status": "cavity - treatment planned"},
   {"num": "30", "name": "Lower right first molar", "status": "healthy"}]})),

dict(title="The Oral Cavity and Supporting Structures", tier=F,
 desc_pub=("Beyond teeth, the oral cavity includes gums (gingiva), the tongue, palate, cheeks, "
  "lips, salivary glands, and the jawbones with their temporomandibular joints (TMJ). Healthy "
  "gums are pink, firm, and do not bleed; saliva protects teeth by buffering acids and "
  "remineralizing enamel.\n"
  "Exams cover all of it: soft-tissue screening for oral cancer, gum measurements, bite "
  "assessment, and TMJ function. Problems here cause as much suffering as tooth decay itself."),
 desc_sig=("Signature comprehensive exams use a structured soft-tissue and function checklist, so "
  "nothing beyond the teeth is skipped under time pressure."),
 how_pub=("Each exam includes visual and tactile screening of all soft tissues, periodontal "
  "probing measuring gum attachment, bite and TMJ evaluation, and saliva assessment. Findings "
  "are charted; abnormalities trigger imaging, referral, or treatment."),
 how_sig=("Signature checklist-driven exams ensure soft tissue, gums, bite, and TMJ are "
  "assessed every time."),
 keys=["Gums, tongue, palate, cheeks, lips, salivary glands, jawbones, TMJ",
  "Healthy gums: pink, firm, no bleeding",
  "Saliva buffers acids and remineralizes",
  "Soft-tissue screening catches oral cancer",
  "Gum measurements track periodontal health",
  "Bite and TMJ affect comfort and function"],
 reqs=["Comprehensive exam protocol",
  "Periodontal probing at intervals",
  "Oral cancer screening training"],
 stds=["ADA comprehensive exam guidelines (public)",
  "Oral cancer screening recommendations (public)"],
 cites=["American Dental Association — exams (public)",
  "National Institute of Dental Research — public information (public)"],
 demo=("protocol", {"steps": ["Medical history review", "Extraoral exam",
   "Soft-tissue screening", "Periodontal probing", "Tooth-by-tooth charting",
   "Bite and TMJ check", "Radiographs as indicated"]})),

dict(title="How Cavities Form", tier=F,
 desc_pub=("Cavities (dental caries) form when mouth bacteria feed on sugars and produce acids that "
  "dissolve enamel - demineralization. Repeated acid attacks without remineralization (from "
  "saliva and fluoride) create white spots, then holes. It is the most common chronic disease of "
  "childhood and highly prevalent in adults.\n"
  "The process is reversible early: fluoride and saliva can remineralize white spots before they "
  "cavitate. Once a hole forms, restoration is needed. Prevention - less sugar frequency, fluoride, "
  "sealants, hygiene - stops the cycle."),
 desc_sig=("Signature caries management stages every lesion - sound, white spot, cavitated - with "
  "matched interventions, so early lesions get remineralization instead of premature drilling."),
 how_pub=("Exams detect white spots and cavities visually, with explorers and radiographs. Early "
  "lesions get fluoride varnish and counseling; cavitated lesions are cleaned of decay and "
  "restored. Risk assessment tailors prevention intensity to the individual's caries activity."),
 how_sig=("Signature lesion staging directs each lesion to remineralization or restoration by "
  "evidence, not habit."),
 keys=["Bacteria + sugar = acid = demineralization",
  "Most common chronic disease of childhood",
  "Early white spots are reversible",
  "Fluoride and saliva remineralize",
  "Cavitated lesions need restoration",
  "Prevention: sugar frequency, fluoride, sealants, hygiene"],
 reqs=["Caries detection at every exam",
  "Fluoride varnish availability",
  "Risk-based prevention plans"],
 stds=["ADA caries management guidelines (public)",
  "CAMBRA risk-assessment protocols (public literature)"],
 cites=["American Dental Association — caries resources (public)",
  "Centers for Disease Control — dental caries (public)"],
 demo=("risk", {"factors": [
   {"factor": "Sugary drinks daily", "weight": 2, "present": True},
   {"factor": "Brushes twice daily with fluoride", "weight": -2, "present": False},
   {"factor": "Dental visits yearly", "weight": -1, "present": True},
   {"factor": "Visible plaque", "weight": 2, "present": True}]})),

dict(title="Gum Disease Basics", tier=F,
 desc_pub=("Gum disease starts as gingivitis - red, bleeding gums from plaque - which is reversible "
  "with cleaning and hygiene. Left untreated it can advance to periodontitis: gums pull away, "
  "bone is lost, teeth loosen. Nearly half of U.S. adults over 30 show some periodontitis.\n"
  "Risk factors include smoking, diabetes, poor hygiene, and genetics. Treatment scales with "
  "severity: deep cleaning (scaling and root planing), then surgery for advanced cases. Daily "
  "flossing-equivalent cleaning between teeth is the home front."),
 desc_sig=("Signature periodontal care stages disease precisely with probing data mapped per "
  "tooth, so treatment intensity matches measured severity."),
 how_pub=("Hygienists measure gum pockets with a probe; depths over 3-4mm with bleeding signal "
  "disease. Gingivitis gets professional cleaning plus hygiene coaching. Periodontitis gets "
  "scaling and root planing under anesthesia, then maintenance cleanings every 3-4 months."),
 how_sig=("Signature per-tooth probing maps make disease distribution visible, guiding targeted "
  "treatment."),
 keys=["Gingivitis: reversible with cleaning",
  "Periodontitis: bone loss, tooth loosening",
  "Nearly half of adults 30+ affected",
  "Risks: smoking, diabetes, hygiene, genetics",
  "Treatment scales with severity",
  "Clean between teeth daily"],
 reqs=["Periodontal probing at exams",
  "Scaling/root planing capability",
  "3-4 month maintenance for periodontitis"],
 stds=["AAP periodontal classification (public)",
  "ADA gum disease guidelines (public)"],
 cites=["American Academy of Periodontology — public resources (public)",
  "Centers for Disease Control — periodontal disease (public)"],
 demo=("outcome", {"label": "Patients with bleeding gums (lower better)", "pre": 47, "post": 18})),

dict(title="Daily Oral Hygiene", tier=F,
 desc_pub=("Daily hygiene is the foundation: brush twice daily for two minutes with fluoride "
  "toothpaste, clean between teeth once daily (floss, picks, or interdental brushes), and limit "
  "sugary snacks and drinks - frequency matters more than quantity. Technique beats force: "
  "gentle circles at the gumline, not scrubbing.\n"
  "Electric toothbrushes help many people clean better; interdental brushes often beat floss for "
  "larger gaps. Replace brushes every 3-4 months. Children need supervision until they can tie "
  "shoes - roughly the dexterity needed for effective brushing."),
 desc_sig=("Signature hygiene coaching personalizes technique to the individual's problem areas "
  "shown by disclosing solution, turning generic advice into targeted skill-building."),
 how_pub=("Dental teams demonstrate technique, use disclosing agents to reveal missed plaque, and "
  "recommend specific tools per mouth. Follow-up visits check improvement in plaque scores and "
  "bleeding. Counseling addresses diet frequency and tobacco."),
 how_sig=("Signature plaque-mapping shows each patient exactly where their technique fails, "
  "focusing practice where it counts."),
 keys=["Brush twice daily, 2 minutes, fluoride toothpaste",
  "Clean between teeth daily",
  "Sugar frequency matters more than quantity",
  "Technique beats force",
  "Supervise children's brushing",
  "Replace brushes every 3-4 months"],
 reqs=["Fluoride toothpaste and appropriate tools",
  "Technique demonstration",
  "Diet counseling"],
 stds=["ADA home-care recommendations (public)"],
 cites=["American Dental Association — home care (public)"],
 demo=("outcome", {"label": "Patients with good plaque scores", "pre": 52, "post": 84})),

dict(title="Fluoride and Prevention", tier=F,
 desc_pub=("Fluoride prevents cavities by remineralizing enamel and inhibiting bacterial acid "
  "production. Sources: fluoridated water (the great public-health success), toothpaste, "
  "mouth rinses, and professional varnish applications. Community water fluoridation reduces "
  "decay across whole populations at minimal cost.\n"
  "Sealants - plastic coatings on molar chewing surfaces - block the pits where most childhood "
  "cavities start. Together, fluoride plus sealants plus hygiene form the prevention triad."),
 desc_sig=("Signature prevention planning assigns fluoride and sealant interventions by "
  "individual risk, maximizing population benefit within program budgets."),
 how_pub=("Dentists assess fluoride exposure and caries risk, apply varnish to high-risk patients "
  "(especially children), place sealants on susceptible molars, and counsel on water and "
  "toothpaste. School programs extend varnish and sealants to underserved children."),
 how_sig=("Signature risk-based assignment targets varnish and sealants to those who benefit "
  "most."),
 keys=["Remineralizes enamel; inhibits acid",
  "Water fluoridation: great public-health success",
  "Varnish for high-risk patients",
  "Sealants block molar pits",
  "Prevention triad: fluoride + sealants + hygiene",
  "School programs reach underserved kids"],
 reqs=["Fluoride varnish supply",
  "Sealant placement capability",
  "Risk assessment"],
 stds=["ADA fluoride guidelines (public)",
  "CDC community prevention guidance (public)"],
 cites=["Centers for Disease Control — fluoridation (public)",
  "American Dental Association — sealants (public)"],
 demo=("outcome", {"label": "Children cavity-free at age 8", "pre": 55, "post": 79})),

dict(title="The Dental Checkup", tier=F,
 desc_pub=("The checkup (periodic exam) combines professional cleaning with comprehensive "
  "evaluation: medical history update, soft-tissue screening, gum measurements, tooth charting, "
  "bite check, and radiographs as indicated. Intervals are risk-based - 6 months is common but "
  "not universal; low-risk adults may go longer, high-risk patients come quarterly.\n"
  "The checkup's hidden value is early detection: small problems found early cost little; the "
  "same problems found late cost teeth. Consistent attendance is the single best predictor of "
  "keeping one's teeth for life."),
 desc_sig=("Signature recall scheduling computes each patient's optimal interval from risk "
  "factors, replacing the universal six-month default with personalized timing."),
 how_pub=("Hygienists clean above and below the gumline, polish, and apply fluoride; dentists "
  "examine comprehensively and review radiographs. Findings become a treatment plan prioritized "
  "by urgency, with costs explained. The next recall is set by risk."),
 how_sig=("Signature risk-computed recall intervals personalize the most basic rhythm of dental "
  "care."),
 keys=["Cleaning + comprehensive evaluation",
  "Intervals are risk-based, not universal",
  "Early detection: small problems, small costs",
  "Consistent attendance predicts keeping teeth",
  "Treatment plans prioritized by urgency",
  "Costs explained up front"],
 reqs=["Hygiene and exam capacity",
  "Radiographic capability",
  "Risk-based recall system"],
 stds=["ADA exam and recall guidelines (public)"],
 cites=["American Dental Association — checkups (public)"],
 demo=("protocol", {"steps": ["Update medical history", "Professional cleaning",
   "Soft-tissue screening", "Periodontal check", "Tooth charting",
   "Radiographs as indicated", "Treatment plan + recall set"]})),

dict(title="Dental X-rays and Imaging", tier=F,
 desc_pub=("Dental imaging sees what eyes cannot: decay between teeth, bone loss, abscesses, "
  "impacted teeth, and implant sites. Bitewings show crowns of back teeth; periapicals show whole "
  "teeth with roots; panoramic images survey the full mouth; cone-beam CT gives 3D detail for "
  "implants and surgery.\n"
  "Digital sensors cut radiation dramatically versus film; a set of bitewings exposes less than "
  "a day of natural background radiation. ALARA (as low as reasonably achievable) governs use: "
  "images when they change decisions, not by routine alone."),
 desc_sig=("Signature imaging protocols match image type to diagnostic question with dose "
  "tracking, so every exposure is justified and minimal."),
 how_pub=("Dentists prescribe images based on exam findings and risk, following ADA/FDA selection "
  "guidelines. Staff position sensors, capture images, and dentists interpret - documenting "
  "findings in the record. Images are compared over time to track change."),
 how_sig=("Signature dose tracking and indication-checking keep imaging justified and minimal."),
 keys=["Bitewings, periapicals, panoramic, cone-beam CT",
  "See between teeth, bone, abscesses, impactions",
  "Digital sensors cut radiation dramatically",
  "ALARA: as low as reasonably achievable",
  "Image when it changes decisions",
  "Compare over time"],
 reqs=["Digital radiography equipment",
  "Selection-criteria guidelines",
  "Interpretation and documentation"],
 stds=["ADA/FDA image selection guidelines (public)",
  "State radiography regulations"],
 cites=["American Dental Association — x-rays (public)",
  "U.S. Food and Drug Administration — dental radiography (public)"],
 demo=("protocol", {"steps": ["Determine indication per guidelines", "Explain to patient",
   "Position sensor with ALARA technique", "Capture and review quality",
   "Interpret and document", "Compare with prior images"]})),

dict(title="The Dental Care Team", tier=F,
 desc_pub=("The dental team multiplies what any one clinician could do: dentists diagnose and "
  "perform complex treatment; hygienists clean, screen, and educate; assistants prepare, assist, "
  "and manage flow; office staff schedule, bill, and coordinate; specialists (orthodontists, "
  "oral surgeons, periodontists, endodontists, pediatric dentists) handle advanced care.\n"
  "Expanded-function roles let trained auxiliaries place fillings or take final impressions in "
  "many states - extending access. Team huddles and clear roles keep the day smooth and safe."),
 desc_sig=("Signature team design defines role-based task lists with cross-training matrices, so "
  "coverage never depends on one person's presence."),
 how_pub=("Practices define each role's scope per state law, cross-train for coverage, and run "
  "morning huddles reviewing the day's patients and needs. Delegation follows training and "
  "legal scope; supervision matches requirements."),
 how_sig=("Signature cross-training matrices make coverage resilient to absences."),
 keys=["Dentists, hygienists, assistants, office staff, specialists",
  "Hygienists: clean, screen, educate",
  "Expanded functions extend access",
  "Specialists handle advanced care",
  "Huddles and clear roles keep days smooth",
  "Delegation follows training and law"],
 reqs=["Licensed staff per state scope",
  "Role definitions and huddles",
  "Specialist referral network"],
 stds=["State dental practice acts (public)",
  "CODA accreditation standards (public)"],
 cites=["American Dental Association — dental team (public)"],
 demo=("outcome", {"label": "On-time appointment starts", "pre": 71, "post": 92})),

dict(title="Paying for Dental Care", tier=F,
 desc_pub=("Dental financing is a patchwork: employer dental insurance (usually with annual "
  "maximums around $1,000-$2,000), Medicaid (comprehensive for children via EPSDT, variable for "
  "adults by state), discount plans, and out-of-pocket payment. Many adults lack any dental "
  "coverage.\n"
  "Practices help with estimates, payment plans, and phased treatment - doing urgent work now "
  "and scheduling the rest. Community clinics, dental schools, and charitable programs (like "
  "Mission of Mercy events) fill gaps for the underserved."),
 desc_sig=("Signature treatment financing presents phased plans with transparent costs per phase, "
  "so patients choose with full information rather than sticker shock."),
 how_pub=("Treatment plans include written cost estimates; staff verify benefits and explain "
  "patient portions before work begins. Urgent care is prioritized; elective work is phased. "
  "Uninsured patients are directed to clinics, schools, and charitable programs."),
 how_sig=("Signature phased cost transparency lets patients plan across months, not guess."),
 keys=["Insurance often caps at $1,000-$2,000 yearly",
  "Medicaid: comprehensive for kids, variable for adults",
  "Many adults lack coverage",
  "Written estimates before treatment",
  "Phase treatment: urgent now, rest scheduled",
  "Clinics, schools, charities fill gaps"],
 reqs=["Benefits verification",
  "Written estimates and payment plans",
  "Referral knowledge for low-cost options"],
 stds=["State insurance regulations (public)",
  "Medicaid dental program rules"],
 cites=["Centers for Medicare and Medicaid Services — dental coverage (public)",
  "American Dental Association — financing resources (public)"],
 demo=("outcome", {"label": "Patients completing phased treatment plans", "pre": 48, "post": 76})),

# ---------------- Compounded (12) ----------------
dict(title="Dental Diagnostics", tier=C,
 desc_pub=("Dental diagnostics turn symptoms and signs into named problems with causes: visual and "
  "tactile exam, radiographic interpretation, pulp vitality testing (cold, electric), periodontal "
  "charting, occlusal analysis, and caries-detection aids (laser fluorescence, transillumination).\n"
  "Differential diagnosis is the skill: lingering hot pain suggests irreversible pulpitis; pain "
  "on biting suggests a cracked tooth; generalized bleeding suggests systemic factors. Accurate "
  "diagnosis precedes all good treatment - treating the wrong diagnosis fails twice."),
 desc_sig=("Signature diagnostic workups structure findings into ranked differential diagnoses "
  "with confirmatory tests, making clinical reasoning explicit and teachable."),
 how_pub=("The dentist gathers history (onset, triggers, duration), examines clinically, orders "
  "targeted images, and performs vitality and percussion tests. Findings converge on a diagnosis "
  "with alternatives ruled out; the diagnosis drives the treatment plan, which the patient "
  "approves."),
 how_sig=("Signature ranked differentials with confirmatory-test prompts standardize thorough "
  "diagnosis."),
 keys=["Exam, imaging, vitality testing, perio charting, occlusal analysis",
  "Differential diagnosis is the core skill",
  "Match symptoms to causes precisely",
  "Accurate diagnosis precedes good treatment",
  "Rule out alternatives",
  "Diagnosis drives the plan"],
 reqs=["Diagnostic instruments and tests",
  "Radiographic interpretation skill",
  "Time for thorough workup"],
 stds=["Diagnostic terminology standards (public literature)"],
 cites=["American Association of Endodontists — diagnostic guidance (public)"],
 demo=("chart", {"teeth": [
   {"num": "8", "name": "Upper right central incisor", "status": "cold lingering pain - pulpitis suspected"},
   {"num": "15", "name": "Upper left second molar", "status": "pain on biting - crack suspected"},
   {"num": "24", "name": "Lower left central incisor", "status": "healthy"}]})),

dict(title="Restorative Materials", tier=C,
 desc_pub=("Restorative materials rebuild teeth: amalgam (durable, inexpensive, mercury-containing, "
  "declining in use), composite resin (tooth-colored, bonded, versatile), glass ionomer (fluoride-"
  "releasing, good for children and root surfaces), ceramics/porcelain (esthetic, for crowns and "
  "veneers), and gold (exceptionally durable, expensive).\n"
  "Selection balances esthetics, strength, location, moisture control, cost, and patient "
  "preference. No material is perfect; the art is matching material to tooth, bite forces, and "
  "patient values."),
 desc_sig=("Signature material selection scores options against the clinical situation - load, "
  "esthetics, moisture, longevity data - presenting the trade-offs transparently."),
 how_pub=("The dentist assesses the defect size, location, bite forces, and esthetic demands, "
  "discusses options with the patient including longevity and cost, and selects the material. "
  "Technique - isolation, bonding protocols - determines success as much as the material."),
 how_sig=("Signature trade-off scoring makes material choice a shared, informed decision."),
 keys=["Amalgam, composite, glass ionomer, ceramic, gold",
  "Balance esthetics, strength, location, cost",
  "Composite: tooth-colored and bonded",
  "Glass ionomer releases fluoride",
  "Technique matters as much as material",
  "Match material to tooth and patient values"],
 reqs=["Material inventory per indication",
  "Isolation and bonding technique",
  "Patient counseling on options"],
 stds=["ISO dental material standards (public)",
  "ADA material acceptance guidance (public)"],
 cites=["American Dental Association — materials science (public)"],
 demo=("material", {"materials": [
   {"name": "Composite resin", "score": 9, "note": "esthetic, bonded, versatile"},
   {"name": "Ceramic", "score": 8, "note": "best esthetics for crowns"},
   {"name": "Amalgam", "score": 5, "note": "durable but declining use"},
   {"name": "Gold", "score": 7, "note": "durable, expensive, non-esthetic"}]})),

dict(title="Fillings and Restorations", tier=C,
 desc_pub=("Fillings repair decayed or damaged teeth: remove decay, shape the cavity, place and "
  "finish the material. Direct restorations (composite or amalgam placed in one visit) suit "
  "small-to-medium defects; indirect restorations (inlays, onlays made in a lab) suit larger "
  "ones.\n"
  "Success factors: complete decay removal, good isolation (rubber dam), proper bonding technique, "
  "correct bite adjustment, and polished margins. Well-done composites last many years; failures "
  "usually trace to technique or recurrent decay at margins."),
 desc_sig=("Signature restorative quality tracks restoration survival by operator, material, and "
  "tooth - feeding technique coaching that extends the life of every filling placed."),
 how_pub=("After anesthesia, the dentist removes decay, verifies clean margins, isolates with "
  "rubber dam, applies bonding per protocol, places composite in layers curing each, shapes "
  "anatomy, checks bite with articulating paper, and polishes. Post-op instructions cover "
  "sensitivity expectations."),
 how_sig=("Signature survival tracking turns every restoration into data improving the next "
  "one."),
 keys=["Direct (one visit) vs indirect (lab-made)",
  "Remove all decay; verify clean margins",
  "Isolation and bonding technique decide success",
  "Bite adjustment and polish finish the job",
  "Well-done composites last many years",
  "Recurrent decay at margins is the common failure"],
 reqs=["Anesthesia and isolation equipment",
  "Bonding materials and curing lights",
  "Occlusal adjustment instruments"],
 stds=["Operative dentistry technique standards (public literature)"],
 cites=["American Dental Association — restorations (public)"],
 demo=("protocol", {"steps": ["Anesthesia", "Decay removal", "Verify clean margins",
   "Rubber dam isolation", "Bonding protocol", "Layered composite placement",
   "Anatomy shaping", "Bite check", "Polish", "Post-op instructions"]})),

dict(title="Root Canal Treatment", tier=C,
 desc_pub=("Root canal treatment saves teeth whose pulp is irreversibly inflamed or infected: the "
  "dentist removes the pulp, cleans and shapes the canals, fills them with gutta-percha, and "
  "seals the tooth - usually followed by a crown for back teeth. Modern rotary instruments and "
  "microscopes made the procedure efficient and comfortable.\n"
  "Signs: lingering hot/cold pain, spontaneous throbbing, abscess. Contrary to reputation, "
  "with anesthesia the procedure feels like getting a filling. This record is educational; "
  "treatment decisions belong with a dentist or endodontist."),
 desc_sig=("Signature endodontic planning maps canal anatomy from imaging before treatment, so "
  "complex cases are identified and referred appropriately rather than discovered mid-"
  "procedure."),
 how_pub=("Diagnosis confirms irreversible pulpitis or necrosis via vitality testing and "
  "radiographs. Under rubber dam, the dentist accesses the pulp chamber, locates all canals, "
  "cleans and shapes with rotary files, disinfects, fills with gutta-percha, and seals. A crown "
  "usually follows for molars."),
 how_sig=("Signature canal mapping from imaging flags complex anatomy before treatment begins."),
 keys=["Removes infected pulp; cleans, fills, seals canals",
  "Saves teeth that would otherwise be extracted",
  "Signs: lingering pain, spontaneous throbbing, abscess",
  "Feels like a filling with anesthesia",
  "Back teeth usually need crowns after",
  "Endodontists handle complex cases"],
 reqs=["Rotary endodontic instruments",
  "Rubber dam isolation",
  "Radiographic working-length determination"],
 stds=["AAE treatment standards (public)",
  "Endodontic diagnosis guidelines (public)"],
 cites=["American Association of Endodontists — public resources (public)"],
 demo=("outcome", {"label": "Root canals successful at 5 years", "pre": 82, "post": 93})),

dict(title="Crowns and Bridges", tier=C,
 desc_pub=("Crowns cap damaged teeth - after root canals, large fractures, or heavy decay - "
  "restoring shape, strength, and appearance in ceramic, porcelain-fused-metal, or gold. Bridges "
  "replace missing teeth by anchoring artificial teeth to crowns on neighbors.\n"
  "The process: prepare the tooth, take impressions (or digital scans), place a temporary, and "
  "cement the lab-made restoration. Same-day CAD/CAM crowns compress this into one visit. Good "
  "margins and bite are the quality markers."),
 desc_sig=("Signature crown-and-bridge workflows use digital scans with margin-verification "
  "checklists, cutting remakes and improving fit."),
 how_pub=("The dentist prepares the tooth with proper taper and margin design, captures the "
  "impression or scan, and designs shade and shape with the patient. The lab fabricates; the "
  "dentist tries in, checks margins and bite, and cements. Bridges follow the same path across "
  "multiple teeth."),
 how_sig=("Signature margin-verification checklists catch fit problems before cementation."),
 keys=["Crowns cap damaged teeth; bridges replace missing ones",
  "Materials: ceramic, PFM, gold",
  "Prepare, impress/scan, temporary, cement",
  "Same-day CAD/CAM compresses to one visit",
  "Quality: margins and bite",
  "Shade and shape designed with patient"],
 reqs=["Preparation and impression/scan capability",
  "Lab partnership or CAD/CAM",
  "Temporization materials"],
 stds=["Fixed prosthodontic technique standards (public literature)"],
 cites=["American College of Prosthodontists — public resources (public)"],
 demo=("protocol", {"steps": ["Tooth preparation", "Impression or digital scan",
   "Shade selection", "Temporary crown", "Lab fabrication",
   "Try-in: margins and bite", "Cementation", "Post-op check"]})),

dict(title="Dental Implants", tier=C,
 desc_pub=("Dental implants replace missing teeth with titanium posts fused to jawbone "
  "(osseointegration), topped by abutments and crowns. They preserve bone, feel like natural "
  "teeth, and avoid cutting down neighbors as bridges do. Success rates exceed 95% in healthy "
  "patients.\n"
  "The process spans months: assessment and 3D planning, surgical placement, healing/integration, "
  "abutment, and crown. Requirements: adequate bone (grafting if not), good health, no smoking "
  "(smoking sharply raises failure). This record is educational; implant decisions are clinical."),
 desc_sig=("Signature implant planning uses 3D-guided surgery plans with prosthetic-driven "
  "positioning, so the implant serves the final tooth from the start."),
 how_pub=("Cone-beam imaging and planning software position the implant prosthetically. Surgery "
  "places the fixture; months of integration follow; the abutment and crown complete the "
  "restoration. Maintenance - hygiene and regular checks - protects the investment."),
 how_sig=("Signature prosthetic-driven planning starts from the desired crown and works "
  "backward to implant position."),
 keys=["Titanium posts fused to bone",
  "Preserve bone; feel natural; spare neighbors",
  "Success exceeds 95% in healthy patients",
  "Months-long process: plan, place, integrate, restore",
  "Needs adequate bone; smoking raises failure",
  "Maintenance protects the investment"],
 reqs=["3D imaging and planning",
  "Surgical capability or referral",
  "Maintenance program"],
 stds=["Implant placement guidelines (public literature)",
  "AAOMS/ITI guidance (public)"],
 cites=["American Academy of Implant Dentistry — public resources (public)"],
 demo=("outcome", {"label": "Implants surviving at 10 years", "pre": 90, "post": 96})),

dict(title="Orthodontics Basics", tier=C,
 desc_pub=("Orthodontics corrects misaligned teeth and jaws: braces (metal, ceramic), clear "
  "aligners, and functional appliances for growing children. Beyond appearance, alignment improves "
  "cleaning, bite function, and jaw comfort.\n"
  "Treatment starts with records - photos, x-rays, models/scans - and a plan; active treatment "
  "runs months to years with regular adjustments; retention (retainers) preserves results for "
  "life. Early evaluation around age 7 catches problems when growth can help."),
 desc_sig=("Signature orthodontic planning uses digital treatment simulation showing predicted "
  "outcomes, so patients consent to a visible future."),
 how_pub=("Orthodontists take records, diagnose malocclusion, and present options with timelines "
  "and costs. Braces or aligners move teeth per plan with periodic adjustments; retention "
  "follows. Growth-phase patients may get interceptive appliances first."),
 how_sig=("Signature outcome simulation makes the treatment goal concrete before brackets go "
  "on."),
 keys=["Braces, clear aligners, functional appliances",
  "Improves cleaning, bite, comfort - not just looks",
  "Records, plan, active treatment, retention",
  "Retention preserves results for life",
  "Early evaluation around age 7",
  "Treatment runs months to years"],
 reqs=["Orthodontic records capability",
  "Treatment planning expertise",
  "Retention protocol"],
 stds=["AAO treatment standards (public)",
  "Orthodontic records guidelines (public literature)"],
 cites=["American Association of Orthodontists — public resources (public)"],
 demo=("outcome", {"label": "Patients satisfied with alignment results", "pre": 78, "post": 94})),

dict(title="Periodontal Treatment", tier=C,
 desc_pub=("Periodontal treatment fights gum disease in stages: non-surgical scaling and root "
  "planing (deep cleaning under anesthesia) for mild-moderate disease; surgical options - flap "
  "surgery, bone grafts, guided tissue regeneration - for advanced cases; then lifelong "
  "maintenance every 3-4 months.\n"
  "Lasers and antimicrobials adjunct, but mechanical cleaning remains the core. Smoking cessation "
  "and diabetes control multiply treatment success. This record is educational."),
 desc_sig=("Signature periodontal programs track probing depths per site over time, making "
  "treatment response visible tooth by tooth."),
 how_pub=("After full perio charting and radiographs, the dentist or periodontist stages disease "
  "and plans treatment. Scaling/root planing is done by quadrant; re-evaluation in 4-6 weeks "
  "decides whether surgery is needed. Maintenance cleanings continue indefinitely."),
 how_sig=("Signature site-level tracking shows exactly which areas respond and which need "
  "escalation."),
 keys=["Scaling/root planing for mild-moderate",
  "Surgery, grafts for advanced",
  "Lifelong 3-4 month maintenance",
  "Mechanical cleaning is the core",
  "Smoking cessation and diabetes control multiply success",
  "Re-evaluate before escalating"],
 reqs=["Perio charting and radiographs",
  "Scaling/root planing instrumentation",
  "Surgical referral network"],
 stds=["AAP treatment guidelines (public)"],
 cites=["American Academy of Periodontology — treatment (public)"],
 demo=("outcome", {"label": "Pockets reduced to maintainable depths", "pre": 55, "post": 83})),

dict(title="Oral Surgery Procedures", tier=C,
 desc_pub=("Oral surgery covers extractions (including impacted wisdom teeth), implant placement, "
  "bone grafting, corrective jaw surgery, and biopsy of suspicious lesions. Most extractions are "
  "routine; surgical extractions section impacted teeth for removal.\n"
  "Preparation includes medical review, imaging, informed consent, and anesthesia planning (local, "
  "sedation, or general). Post-op keys: bleeding control, clot protection (no smoking, no straws "
  "- dry socket prevention), and infection watch. This record is educational."),
 desc_sig=("Signature surgical planning uses 3D imaging assessment with risk stratification - "
  "nerve proximity, sinus involvement - so complex cases get specialist care by plan, not by "
  "surprise."),
 how_pub=("Assessment and imaging determine approach; consent covers risks including nerve injury "
  "and dry socket. Surgery follows sterile protocol with appropriate anesthesia. Post-op "
  "instructions are written and verbal; follow-up checks healing."),
 how_sig=("Signature risk stratification routes high-risk extractions to specialists "
  "proactively."),
 keys=["Extractions, implants, grafts, jaw surgery, biopsies",
  "Surgical extractions section impacted teeth",
  "Anesthesia: local, sedation, general",
  "Protect the clot: no smoking, no straws",
  "Watch for infection",
  "Written + verbal post-op instructions"],
 reqs=["Surgical instrumentation and imaging",
  "Anesthesia capability per scope",
  "Emergency preparedness"],
 stds=["AAOMS parameters of care (public)"],
 cites=["American Association of Oral and Maxillofacial Surgeons — public resources (public)"],
 demo=("protocol", {"steps": ["Medical review and imaging", "Informed consent",
   "Anesthesia plan", "Sterile surgical protocol", "Hemostasis verified",
   "Written post-op instructions", "Follow-up healing check"]})),

dict(title="Pediatric Dentistry", tier=C,
 desc_pub=("Pediatric dentistry adapts everything for children: tell-show-do communication, "
  "short appointments, preventive focus (fluoride, sealants), habit counseling (thumb, pacifier), "
  "and interceptive orthodontics. The goal is a lifetime of comfort with dental care - first "
  "visits by age one.\n"
  "Behavior guidance ranges from positive reinforcement to sedation for the highly anxious, "
  "always with parent consent and safety monitoring. Treating baby teeth matters: they hold "
  "space, guide eruption, and affect health and confidence."),
 desc_sig=("Signature pediatric design makes every visit a positive-skills-building experience "
  "with progress visible to parents, turning dental visits into health habits."),
 how_pub=("Visits start with acclimation and counting teeth; prevention (cleaning, fluoride, "
  "sealants) dominates early years. Cavities get child-sized restorations; space maintainers "
  "hold spots after early loss. Parents receive coaching on home care and diet."),
 how_sig=("Signature parent-visible progress tracking turns each visit into shared health "
  "education."),
 keys=["Tell-show-do; short appointments",
  "First visit by age one",
  "Prevention dominates: fluoride, sealants",
  "Baby teeth matter: space, guidance, health",
  "Behavior guidance with parent consent",
  "Goal: lifetime comfort with dental care"],
 reqs=["Child-sized equipment",
  "Behavior-guidance training",
  "Parent coaching materials"],
 stds=["AAPD guidelines (public)"],
 cites=["American Academy of Pediatric Dentistry — public resources (public)"],
 demo=("outcome", {"label": "Children with positive dental attitudes", "pre": 62, "post": 88})),

dict(title="Dental Equipment and Operatories", tier=C,
 desc_pub=("The dental operatory is a precision workstation: patient chair, delivery unit "
  "(handpieces, suction, air-water syringe), operating light, intraoral x-ray, and computer for "
  "charting and imaging. Handpieces spin at 400,000+ RPM for cutting; ultrasonic scalers vibrate "
  "for cleaning.\n"
  "Ergonomics and infection control shape the layout: smooth disinfectable surfaces, instrument "
  "cassettes, and workflows separating clean from contaminated. Equipment maintenance - handpiece "
  "lubrication, suction cleaning, x-ray calibration - is daily discipline."),
 desc_sig=("Signature operatory design standardizes ergonomic, infection-safe layouts with "
  "maintenance tracking, so equipment reliability never limits care."),
 how_pub=("Practices design operatories around workflow - dentist, assistant, patient triangle - "
  "with infection-control surfaces and traffic patterns. Daily, weekly, and monthly maintenance "
  "schedules cover every device; logs prove compliance."),
 how_sig=("Signature maintenance tracking schedules and verifies every device's care."),
 keys=["Chair, delivery unit, light, x-ray, computer",
  "Handpieces: 400,000+ RPM",
  "Ergonomics + infection control shape layout",
  "Separate clean from contaminated workflows",
  "Maintenance is daily discipline",
  "Logs prove compliance"],
 reqs=["Operatory design per workflow",
  "Maintenance schedules and logs",
  "Infection-control surfaces"],
 stds=["OSHA dental requirements (public)",
  "CDC dental infection-control guidelines (public)"],
 cites=["Centers for Disease Control — dental infection control (public)"],
 demo=("protocol", {"steps": ["Morning equipment check", "Handpiece lubrication",
   "Suction line cleaning", "X-ray calibration check", "Log all maintenance",
   "Evening shutdown protocol"]})),

dict(title="Infection Control in Dentistry", tier=C,
 desc_pub=("Dental infection control protects patients and staff from bloodborne and airborne "
  "risks: hand hygiene, gloves/masks/eyewear, instrument sterilization (autoclaves with "
  "biological monitoring), surface disinfection, single-use disposables, sharps safety, and "
  "dental unit waterline treatment.\n"
  "The CDC's dental guidelines are the standard; OSHA enforces worker protection. Sterilization "
  "is verified, not assumed - spore tests prove the autoclave works."),
 desc_sig=("Signature infection control runs sterilization verification and compliance audits on "
  "schedule with digital logs, making safety provable."),
 how_pub=("Offices follow the full protocol chain: PPE for every patient, instrument processing "
  "(clean, package, sterilize, store), surface barriers and disinfection between patients, "
  "weekly spore testing, waterline shock treatments, and sharps containers. Audits verify "
  "compliance."),
 how_sig=("Signature digital logs make every sterilization cycle and audit traceable."),
 keys=["Hand hygiene, PPE, sterilization, disinfection, sharps, waterlines",
  "Autoclaves with biological (spore) monitoring",
  "Sterilization verified, not assumed",
  "CDC guidelines; OSHA enforcement",
  "Single-use where appropriate",
  "Audit compliance regularly"],
 reqs=["Autoclave with spore testing",
  "PPE and surface barriers",
  "Waterline treatment protocol"],
 stds=["CDC dental infection-control guidelines (public)",
  "OSHA bloodborne pathogens standard (public)"],
 cites=["Centers for Disease Control — dental infection control (public)",
  "Occupational Safety and Health Administration — dental guidance (public)"],
 demo=("outcome", {"label": "Spore tests passing", "pre": 97, "post": 100})),

# ---------------- Advanced (11) ----------------
dict(title="Digital Dentistry: CAD/CAM", tier=A,
 desc_pub=("CAD/CAM dentistry designs and mills restorations digitally: intraoral scanners capture "
  "the preparation, software designs the crown, and a mill carves it from ceramic in-office - "
  "often in a single visit. No goopy impressions, no temporaries, no second appointment.\n"
  "Accuracy now rivals conventional impressions for single crowns. The economics favor busy "
  "practices; the patient experience - one visit, no temporary - favors everyone."),
 desc_sig=("Signature digital workflows integrate scanning, design, and milling with quality "
  "checkpoints, so same-day dentistry is reliably excellent, not just fast."),
 how_pub=("The dentist prepares the tooth, scans with an intraoral scanner, designs the "
  "restoration in software (margins, contacts, occlusion), mills from a ceramic block, stains "
  "and glazes, then tries in and cements - all in one appointment."),
 how_sig=("Signature quality checkpoints at scan, design, and mill stages prevent same-day "
  "remakes."),
 keys=["Scan, design, mill - often single visit",
  "No conventional impressions or temporaries",
  "Accuracy rivals conventional for single crowns",
  "Ceramic milled in-office",
  "Patient experience: one visit",
  "Economics favor busy practices"],
 reqs=["Intraoral scanner and mill",
  "Design software training",
  "Ceramic materials inventory"],
 stds=["Digital workflow accuracy literature (public)"],
 cites=["American Dental Association — digital dentistry (public)"],
 demo=("protocol", {"steps": ["Tooth preparation", "Intraoral scan",
   "Digital design (margins, occlusion)", "Mill from ceramic block",
   "Stain and glaze", "Try-in and cement"]})),

dict(title="3D Imaging and Cone-Beam CT", tier=A,
 desc_pub=("Cone-beam computed tomography gives dentists 3D views: implant planning with nerve "
  "and sinus mapping, impacted-tooth localization, endodontic complexity, airway assessment, and "
  "pathology evaluation. It reveals what 2D images hide.\n"
  "Dose is higher than 2D - justified only when 3D changes the plan. Interpretation requires "
  "training; findings outside the dentist's scope get radiologist over-read. This record is "
  "educational."),
 desc_sig=("Signature 3D imaging protocols define exactly which cases warrant cone-beam scans, "
  "with dose optimization per indication - powerful imaging used precisely."),
 how_pub=("The dentist determines 3D indication per guidelines, captures a focused field of view "
  "(smallest adequate), interprets systematically (teeth, bone, airway, pathology), documents "
  "findings, and refers out-of-scope findings for radiology review."),
 how_sig=("Signature indication-gated protocols ensure cone-beam is used where 3D changes "
  "decisions."),
 keys=["3D for implants, impactions, endo complexity, pathology",
  "Reveals what 2D hides",
  "Higher dose - justify by changed plans",
  "Smallest adequate field of view",
  "Systematic interpretation",
  "Radiologist over-read for out-of-scope findings"],
 reqs=["Cone-beam unit",
  "3D interpretation training",
  "Radiology referral pathway"],
 stds=["AAOMR use guidelines (public)",
  "ALARA applied to 3D"],
 cites=["American Academy of Oral and Maxillofacial Radiology — public resources (public)"],
 demo=("protocol", {"steps": ["Confirm 3D indication", "Select smallest field of view",
   "Capture scan", "Systematic interpretation", "Document findings",
   "Refer out-of-scope findings"]})),

dict(title="Laser Dentistry", tier=A,
 desc_pub=("Dental lasers cut soft tissue with light: gum reshaping, frenectomies, canker-sore "
  "relief, and bacterial reduction in periodontal pockets - often with less bleeding and faster "
  "healing than scalpels. Hard-tissue lasers can prepare small cavities with less anesthesia.\n"
  "Evidence supports specific uses; marketing often outruns science. Training and safety "
  "protocols (eye protection, plume evacuation) are mandatory. This record is educational."),
 desc_sig=("Signature laser integration limits use to evidence-backed indications with "
  "competency verification, keeping technology honest."),
 how_pub=("Dentists train and credential in laser use, select evidence-backed indications, apply "
  "strict safety (wavelength-specific eyewear, plume suction), and document outcomes. Patients "
  "are counseled on realistic benefits versus conventional methods."),
 how_sig=("Signature indication-gated laser use prevents technology-driven overtreatment."),
 keys=["Soft-tissue: reshaping, frenectomy, lesion relief",
  "Less bleeding, faster healing in supported uses",
  "Hard-tissue lasers for small cavities",
  "Evidence supports specific uses",
  "Safety: eyewear, plume evacuation",
  "Training and credentialing mandatory"],
 reqs=["Laser unit with safety systems",
  "Credentialed operators",
  "Indication protocols"],
 stds=["Laser safety standards (ANSI Z136, public)",
  "State laser-use regulations"],
 cites=["Academy of Laser Dentistry — public resources (public)"],
 demo=("material", {"materials": [
   {"name": "Diode laser (soft tissue)", "score": 8, "note": "hemostasis, healing"},
   {"name": "Erbium laser (hard tissue)", "score": 6, "note": "selective, technique-sensitive"},
   {"name": "Scalpel (conventional)", "score": 7, "note": "proven, versatile"}]})),

dict(title="Dental Anesthesia and Sedation", tier=A,
 desc_pub=("Dental anesthesia spans local anesthesia (numbing the area), nitrous oxide (relaxing "
  "gas), oral sedation, IV sedation, and general anesthesia - matched to procedure invasiveness "
  "and patient anxiety. Profound local anesthesia is the foundation; everything else builds on "
  "it.\n"
  "Safety is paramount: medical history review, ASA classification, monitoring (pulse oximetry "
  "minimum), emergency preparedness, and appropriate permits per sedation depth. This record is "
  "educational; anesthesia decisions are clinical."),
 desc_sig=("Signature anesthesia safety standardizes pre-op assessment, monitoring, and "
  "emergency readiness by sedation depth, so comfort never compromises safety."),
 how_pub=("The dentist reviews medical history, assigns ASA class, obtains consent, and selects "
  "the minimal effective modality. Monitoring matches depth; emergency drugs and equipment are "
  "checked before every sedated case. Recovery is supervised with written discharge instructions "
  "and an escort for deeper sedation."),
 how_sig=("Signature depth-matched safety checklists make anesthesia safety systematic."),
 keys=["Local, nitrous, oral, IV, general - matched to need",
  "Profound local anesthesia is the foundation",
  "Medical history and ASA classification first",
  "Monitoring: pulse oximetry minimum",
  "Emergency preparedness every sedated case",
  "Permits required by sedation depth"],
 reqs=["Sedation permits per state",
  "Monitoring equipment",
  "Emergency drugs and training"],
 stds=["ADA sedation guidelines (public)",
  "State anesthesia permits (public)"],
 cites=["American Dental Association — sedation guidelines (public)"],
 demo=("protocol", {"steps": ["Medical history + ASA class", "Informed consent",
   "Select minimal effective modality", "Verify emergency readiness",
   "Depth-appropriate monitoring", "Supervised recovery + escort"]})),

dict(title="Managing Dental Emergencies", tier=A,
 desc_pub=("Dental emergencies - knocked-out teeth, severe toothache, abscess with swelling, broken "
  "teeth, lost crowns - need prompt, structured response. Knocked-out permanent teeth: hold by "
  "the crown, rinse briefly, reimplant or keep in milk, and see a dentist within the hour - "
  "minutes matter.\n"
  "Practices reserve emergency slots daily; after-hours protocols direct true emergencies to "
  "on-call care. Facial swelling with fever or trouble swallowing/breathing is a medical "
  "emergency - go to the emergency department. Educational record; real emergencies need "
  "professionals."),
 desc_sig=("Signature emergency triage gives every caller a structured urgency assessment with "
  "home-care instructions, so true emergencies are seen today and others safely scheduled."),
 how_pub=("Call-takers triage by symptoms using protocol questions, give home-care instructions "
  "(save the tooth fragment, cold compress), and schedule same-day for urgent cases. Dentists "
  "diagnose and stabilize: reimplant, drain, medicate, or temporize - with definitive treatment "
  "planned."),
 how_sig=("Signature caller triage protocols standardize urgency decisions across staff."),
 keys=["Knocked-out tooth: minutes matter, keep in milk",
  "Abscess with swelling/fever: urgent",
  "Facial swelling + breathing trouble: ED immediately",
  "Reserve daily emergency slots",
  "After-hours on-call protocols",
  "Home-care instructions while waiting"],
 reqs=["Emergency triage protocol",
  "Daily reserved slots",
  "After-hours coverage"],
 stds=["Dental trauma guidelines (IADT, public)"],
 cites=["International Association of Dental Traumatology — guidelines (public)"],
 demo=("protocol", {"steps": ["Triage call by symptoms", "Give home-care instructions",
   "Same-day slot for urgent", "Diagnose and stabilize", "Plan definitive treatment"]})),

dict(title="Oral Health and Whole-Body Health", tier=A,
 desc_pub=("The mouth-body connection is increasingly documented: periodontal disease associates "
  "with diabetes (bidirectionally - each worsens the other), cardiovascular disease, adverse "
  "pregnancy outcomes, and respiratory infections. Dental infections can spread to become "
  "life-threatening.\n"
  "Integration follows: diabetes programs include periodontal screening, prenatal care includes "
  "oral health counseling (dental care is safe in pregnancy), and hospitals screen oral health "
  "before cardiac surgery. The mouth is part of the body - care should act like it."),
 desc_sig=("Signature medical-dental integration embeds oral screening in chronic-disease "
  "workflows with closed-loop referrals, so the mouth-body connection changes practice, not "
  "just textbooks."),
 how_pub=("Medical and dental teams establish referral pathways: diabetes educators screen gums, "
  "dentists screen HbA1c risk, OB practices counsel on pregnancy-safe dental care. Shared "
  "records carry the relevant findings both ways."),
 how_sig=("Signature closed-loop medical-dental referrals make integration operational."),
 keys=["Perio-diabetes: bidirectional link",
  "Associates with cardiovascular disease, pregnancy outcomes",
  "Dental infections can become life-threatening",
  "Dental care is safe in pregnancy",
  "Screen oral health before cardiac surgery",
  "The mouth is part of the body"],
 reqs=["Medical-dental referral pathways",
  "Cross-screening protocols",
  "Shared record elements"],
 stds=["Clinical guidelines on perio-systemic links (public literature)"],
 cites=["American Academy of Periodontology — systemic links (public)",
  "American Diabetes Association — oral health (public)"],
 demo=("outcome", {"label": "Diabetes patients receiving perio screening", "pre": 34, "post": 71})),

dict(title="Geriatric Dentistry", tier=A,
 desc_pub=("Geriatric dentistry adapts care for aging mouths and bodies: root caries (exposed "
  "roots decay fast), dry mouth from medications, denture care, implant maintenance, and "
  "coordination with medical conditions. Cognitive impairment demands adapted communication and "
  "caregiver involvement.\n"
  "Access is the crisis: frail elders in facilities often go years without dental care. Mobile "
  "dentistry, teledentistry screening, and nursing-facility partnerships bring care to those "
  "who cannot reach offices."),
 desc_sig=("Signature geriatric dental design brings preventive care into facilities on "
  "schedule with caregiver-integrated plans, ending the years-without-care gap."),
 how_pub=("Providers adapt appointments (shorter, morning), use portable equipment for facility "
  "visits, train caregivers in daily mouth care, and coordinate with physicians on dry mouth "
  "and medication issues. Prevention - fluoride, hygiene coaching - dominates."),
 how_sig=("Signature facility-based preventive schedules keep frail elders in continuous "
  "care."),
 keys=["Root caries, dry mouth, denture care",
  "Adapt for cognition and frailty",
  "Access crisis for facility residents",
  "Mobile dentistry and teledentistry screening",
  "Train caregivers in daily mouth care",
  "Prevention dominates"],
 reqs=["Portable dental equipment",
  "Facility partnerships",
  "Caregiver training materials"],
 stds=["Geriatric dental care guidelines (public literature)"],
 cites=["American Dental Association — aging and oral health (public)",
  "Special Care Dentistry Association — public resources (public)"],
 demo=("outcome", {"label": "Facility residents receiving annual dental care", "pre": 28, "post": 66})),
dict(title="Special-Needs Dental Care", tier=A,
 desc_pub=("Special-needs dentistry serves patients whose medical, physical, or cognitive "
  "conditions complicate standard care: adapted positioning, desensitization visits, sedation "
  "options, hospital dentistry for complex cases, and coordination with medical teams.\n"
  "The core skill is individualized accommodation: sensory-friendly scheduling, communication "
  "matched to the patient, and caregivers as partners. Everyone deserves a dental home."),
 desc_sig=("Signature special-needs design builds accommodation profiles per patient - sensory, "
  "communication, medical - applied automatically to every visit."),
 how_pub=("Practices gather detailed accommodation needs at intake, plan visits accordingly "
  "(first appointments, quiet rooms, extra time), use desensitization sequences for anxious "
  "patients, and arrange sedation or hospital settings when needed. Caregivers participate "
  "throughout."),
 how_sig=("Signature accommodation profiles make every visit correctly adapted without "
  "re-explaining needs."),
 keys=["Adapted for medical, physical, cognitive complexity",
  "Sensory-friendly scheduling and environments",
  "Desensitization visits build tolerance",
  "Sedation to hospital dentistry as needed",
  "Caregivers as partners",
  "Everyone deserves a dental home"],
 reqs=["Accommodation intake process",
  "Flexible scheduling and environments",
  "Sedation/hospital pathways"],
 stds=["Special Care Dentistry guidelines (public literature)"],
 cites=["Special Care Dentistry Association — public resources (public)"],
 demo=("protocol", {"steps": ["Detailed accommodation intake", "Plan visit adaptations",
   "Desensitization sequence if needed", "Adapted treatment delivery",
   "Caregiver coaching", "Document what worked"]})),

dict(title="Dental Public Health Programs", tier=A,
 desc_pub=("Dental public health prevents disease at population scale: community water "
  "fluoridation, school sealant and varnish programs, mobile clinics, teledentistry screening, "
  "and workforce innovations (dental therapists) extending care to underserved areas.\n"
  "Surveillance (like NHANES oral health data) tracks disparities and targets resources. The "
  "field's ethic: the greatest benefit to those with the least access."),
 desc_sig=("Signature public-health dentistry uses surveillance data to target interventions "
  "geographically, maximizing prevented disease per dollar."),
 how_pub=("Health departments assess community needs, deploy school and mobile programs, advocate "
  "for fluoridation, and build therapist and teledentistry capacity. Programs measure sealant "
  "retention, caries trends, and access gains."),
 how_sig=("Signature geographic targeting directs prevention resources to highest-need areas "
  "first."),
 keys=["Fluoridation, school programs, mobile clinics, teledentistry",
  "Dental therapists extend access",
  "Surveillance tracks disparities",
  "Target resources by need",
  "Greatest benefit to least access",
  "Measure caries trends and access gains"],
 reqs=["Community needs assessment",
  "School/mobile program capacity",
  "Surveillance data access"],
 stds=["ASTDD best practices (public)",
  "Healthy People oral health objectives (public)"],
 cites=["Association of State and Territorial Dental Directors (public)",
  "U.S. Dept. of Health and Human Services — Healthy People (public)"],
 demo=("outcome", {"label": "High-need schools with sealant programs", "pre": 41, "post": 78})),

dict(title="Measuring Oral Health Outcomes", tier=A,
 desc_pub=("Oral health outcomes span clinical (DMFT caries index, periodontal status, tooth "
  "retention), patient-reported (OHIP - oral health impact profile: pain, function, "
  "psychosocial), and access measures. Value-based programs increasingly tie payment to "
  "outcomes rather than procedures.\n"
  "What matters to patients - no pain, chew comfortably, smile confidently - belongs at the "
  "center alongside clinical indices. Measuring both keeps dentistry honest about its purpose."),
 desc_sig=("Signature outcome systems pair clinical indices with patient-reported measures in "
  "every treatment plan, so success is defined by patients and clinicians together."),
 how_pub=("Practices select outcome sets (clinical + OHIP), collect at baseline and follow-up, "
  "and review trends per provider and practice. Payers pilot value-based contracts on "
  "prevention outcomes like caries incidence in children."),
 how_sig=("Signature dual outcome tracking makes patient-defined success visible alongside "
  "clinical metrics."),
 keys=["Clinical: DMFT, perio status, tooth retention",
  "Patient-reported: OHIP - pain, function, psychosocial",
  "Access measures complete the picture",
  "Value-based payment ties to outcomes",
  "Patient priorities at the center",
  "Measure both clinical and lived outcomes"],
 reqs=["Outcome measure set",
  "Baseline and follow-up collection",
  "Review and improvement routines"],
 stds=["Dental quality measure sets (DQA, public)"],
 cites=["Dental Quality Alliance — measures (public)"],
 demo=("outcome", {"label": "Patients reporting no oral pain", "pre": 68, "post": 91})),

dict(title="The Future of Dental Care", tier=A,
 desc_pub=("Dental care's future: AI-assisted radiograph interpretation, 3D-printed restorations "
  "and dentures, bioactive materials that heal tooth structure, caries vaccines in research, "
  "teledentistry triage, and minimally invasive dentistry preserving maximum tooth.\n"
  "The direction is preservation over replacement and access over exclusivity: better tools "
  "saving more teeth for more people. Prevention remains the highest-value intervention - "
  "no technology beats not getting the disease."),
 desc_sig=("The Signature future-state is an oral-health operating system: risk-based prevention, "
  "AI-assisted diagnosis, digital restoration, and outcome accountability - with preservation "
  "as the prime directive. This database is a prototype of that system's knowledge core."),
 how_pub=("Practices adopt validated AI and digital tools, shift toward minimally invasive "
  "techniques, expand teledentistry access, and participate in outcome measurement. Research "
  "translation - bioactive materials, vaccines - is monitored for practice readiness."),
 how_sig=("Signature's operating-system vision makes preservation the default across the "
  "continuum."),
 keys=["AI radiograph interpretation, 3D printing, bioactive materials",
  "Minimally invasive: preserve maximum tooth",
  "Teledentistry triage expands access",
  "Caries vaccines in research",
  "Prevention remains highest value",
  "Validate tools before adopting"],
 reqs=["Technology evaluation discipline",
  "Minimally invasive training",
  "Outcome measurement participation"],
 stds=["Emerging standards for dental AI (public literature)"],
 cites=["American Dental Association — innovation resources (public)",
  "National Institute of Dental Research — research (public)"],
 demo=("outcome", {"label": "Teeth preserved vs extracted (ratio)", "pre": 72, "post": 89})),
]
