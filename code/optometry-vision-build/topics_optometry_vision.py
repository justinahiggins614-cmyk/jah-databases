#!/usr/bin/env python3
"""Topics + config for the optometry-vision pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never medical advice.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "optometry-vision",
    "name_pub": "The Optometry and Vision Database",
    "name_sig": "Signature Optometry and Vision Database",
    "tagline_pub": ("Optometry and vision from the ground up: how eyes and vision work, eye exams "
                    "and vision testing, optical prescriptions, lenses and contacts, common eye "
                    "conditions, and assistive vision systems - every record carrying the full "
                    "entry taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of optometry and vision: the same "
                    "real vision knowledge carried forward, plus Signature-built testing models, "
                    "prescription systems, and assistive vision frameworks original to this system."),
    "record_kind": "optometry and vision record",
    "record_kind_plural": "optometry and vision records",
    "prefix_pub": "JAH-OPTO-", "prefix_sig": "JAH-OPTOS-",
    "ai_pub": "JAH Optometry and Vision Archivist",
    "ai_sig": "JAH Signature Optometry and Vision Creator",
    "role_pub": ("optometry and vision archivist - teaching eye anatomy, vision testing, "
                 "prescriptions, lenses, eye conditions, and assistive systems; answers from many "
                 "angles - definition, example, process, testing, correction - using only archive "
                 "data from this system"),
    "role_sig": ("Signature creator of optometry and vision systems - designing testing models, "
                 "prescription frameworks, and assistive vision systems as original Signature "
                 "works; answers from many angles using only archive data from this system"),
    "search_ph": "Search eye anatomy, exams, prescriptions, lenses, conditions...",
    "chat_ph": "Ask about optometry and vision...",
    "greet_pub": ("I am the JAH Optometry and Vision Archivist. Ask me about how vision works, "
                  "eye exams, prescriptions, lenses, and eye conditions. Educational information "
                  "only - eye care decisions belong with a qualified eye doctor."),
    "greet_sig": ("I am the JAH Signature Optometry and Vision Creator. Ask me about "
                  "Signature-built vision systems. Educational information only."),
    "gen_blurb": ("Generate clearly-labeled optometry and vision studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded optometry and vision records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. "
                      "Educational information only — not medical advice."),
    "demo_kind": "optometry-demo",
    "demo_title": "Optometry and Vision Demo",
    "health": True,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Optometry and Vision Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "rx":
        return fill(
            "rx = @@RX@@\n"
            "print('Eyeglass prescription decode:')\n"
            "for eye in ('OD', 'OS'):\n"
            "    s = rx[eye]\n"
            "    kind = 'nearsighted' if s['sph'] < 0 else 'farsighted' if s['sph'] > 0 else 'plano'\n"
            "    ast = ' with astigmatism' if s['cyl'] != 0 else ''\n"
            "    print(' %s: sphere %+.2f, cyl %+.2f x %d -> %s%s' % (eye, s['sph'], s['cyl'], s['axis'], kind, ast))\n",
            {"RX": p["rx"]})
    if v == "acuity":
        return fill(
            "tests = @@TESTS@@\n"
            "print('Visual acuity results:')\n"
            "for t in tests:\n"
            "    num, den = t['snellen'].split('/')\n"
            "    dec = int(num) / int(den)\n"
            "    level = 'normal' if dec >= 0.8 else 'reduced' if dec >= 0.3 else 'low vision'\n"
            "    print(' %s: %s (decimal %.2f) -> %s' % (t['eye'], t['snellen'], dec, level))\n",
            {"TESTS": p["tests"]})
    if v == "match":
        return fill(
            "symptom = @@SYM@@\nconds = @@CONDS@@\n"
            "print('Symptom:', symptom)\n"
            "for c in conds:\n"
            "    mark = 'POSSIBLE' if symptom in c['signs'] else '-'\n"
            "    print(' [%s] %s: %s' % (mark, c['condition'], c['action']))\n",
            {"SYM": p["symptom"], "CONDS": p["conditions"]})
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
            "print('Exam protocol:')\n"
            "for i, s in enumerate(steps, 1):\n"
            "    print(' %d. %s' % (i, s))\n",
            {"STEPS": p["steps"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Optometry Is", tier=F,
 desc_pub=("Optometry is the health-care profession for eyes and vision: examining eyes, diagnosing "
  "vision problems and eye diseases, prescribing glasses and contact lenses, managing conditions "
  "like glaucoma and dry eye, and detecting signs of systemic disease (diabetes, hypertension) in "
  "the eye. Optometrists (ODs) are primary eye-care providers; ophthalmologists (MDs) are "
  "physicians handling surgery and complex disease.\n"
  "Regular eye exams protect both sight and health - many serious conditions show no early "
  "symptoms. Children need exams before school; adults need periodic exams shifting more "
  "frequent with age."),
 desc_sig=("The Signature system models eye care as a lifelong vision-preservation pathway with "
  "risk-based exam intervals, so surveillance intensity follows individual risk."),
 how_pub=("Patients visit for comprehensive exams on a risk-based schedule. The optometrist takes "
  "history, tests vision and eye health, prescribes correction, treats manageable conditions, and "
  "refers surgical or complex disease to ophthalmology. Findings are documented with recall set."),
 how_sig=("Signature risk-based recall personalizes exam intervals from age, family history, and "
  "prior findings."),
 keys=["Eyes and vision: exams, diagnosis, prescriptions, disease management",
  "Optometrists: primary eye care; ophthalmologists: surgery/complex disease",
  "Eyes reveal systemic disease: diabetes, hypertension",
  "Many serious conditions lack early symptoms",
  "Children: exam before school",
  "Regular exams protect sight and health"],
 reqs=["Licensed optometrists",
  "Comprehensive exam equipment",
  "Referral network to ophthalmology"],
 stds=["State optometry practice acts (public)",
  "AOA exam guidelines (public)"],
 cites=["American Optometric Association — public resources (public)",
  "National Eye Institute — public information (public)"],
 demo=("protocol", {"steps": ["History and symptoms", "Visual acuity",
   "Refraction", "Eye health exam", "Prescription + plan", "Recall set"]})),

dict(title="How the Eye Works", tier=F,
 desc_pub=("The eye is a living camera: light enters through the cornea (which does most of the "
  "focusing), passes the pupil (the iris's adjustable opening), and is fine-focused by the lens "
  "onto the retina. The retina's photoreceptors - rods for dim light, cones for color and detail - "
  "convert light to signals; the optic nerve carries them to the brain, which builds the image.\n"
  "Focusing (accommodation) changes the lens shape for near vision; with age the lens stiffens "
  "(presbyopia), needing reading help. Tears keep the cornea smooth and nourished."),
 desc_sig=("The Signature vision reference pairs each structure with its failure modes and tests - "
  "turning anatomy into a diagnostic map from cornea to cortex."),
 how_pub=("Eye doctors assess each stage: cornea clarity and curvature, pupil responses, lens "
  "clarity and focusing, retinal health, optic nerve appearance, and the brain's processing via "
  "vision tests. Symptoms localize: distortion suggests retina; halos suggest pressure or lens."),
 how_sig=("Signature symptom-localization guides map complaints to structures, focusing the "
  "exam efficiently."),
 keys=["Cornea: most focusing; pupil: adjustable opening; lens: fine focus",
  "Retina: rods (dim) and cones (color/detail)",
  "Optic nerve to brain: image built there",
  "Accommodation: lens shape change for near",
  "Presbyopia: age-stiffened lens",
  "Tears nourish and smooth the cornea"],
 reqs=["Anatomy knowledge for all eye-care staff",
  "Patient education materials",
  "Structured exam covering all stages"],
 stds=["Optometric education standards (public)"],
 cites=["National Eye Institute — how eyes work (public)"],
 demo=("match", {"symptom": "straight lines look wavy",
   "conditions": [{"condition": "Macular problem", "signs": ["straight lines look wavy"], "action": "prompt dilated exam"},
                  {"condition": "Uncorrected astigmatism", "signs": [], "action": "routine refraction"},
                  {"condition": "Dry eye", "signs": [], "action": "tear assessment"}]})),

dict(title="Parts of the Eye", tier=F,
 desc_pub=("The eye's parts each do one job well: cornea (clear front window, major focusing), "
  "sclera (white protective coat), iris (colored diaphragm controlling pupil size), lens (fine "
  "focusing), vitreous (clear gel filling the eye), retina (light-sensing layer), macula/fovea "
  "(central sharp vision), optic disc (nerve exit, the blind spot), and the tear film (smooth "
  "optical surface).\n"
  "Knowing the parts lets patients understand diagnoses: a 'corneal abrasion' is a scratch on "
  "the window; 'macular degeneration' affects central sharp vision."),
 desc_sig=("Signature patient education links each part to plain-language explanations used in "
  "every diagnosis conversation."),
 how_pub=("Exams inspect each part systematically: slit lamp for cornea, lens, and front "
  "structures; dilated exam for retina, macula, and optic nerve; tear assessment for the tear "
  "film. Findings are recorded per structure."),
 how_sig=("Signature per-structure exam checklists ensure complete evaluation every time."),
 keys=["Cornea, sclera, iris, lens, vitreous, retina, macula, optic disc, tear film",
  "Each part does one job",
  "Macula: central sharp vision",
  "Tear film: smooth optical surface",
  "Parts language makes diagnoses understandable",
  "Examine systematically per structure"],
 reqs=["Slit lamp examination",
  "Dilated fundus exam capability",
  "Patient-friendly anatomy explanations"],
 stds=["Comprehensive exam components (public guidelines)"],
 cites=["National Eye Institute — eye anatomy (public)"],
 demo=("protocol", {"steps": ["Slit lamp: cornea, iris, lens", "Tear film assessment",
   "Dilated exam: retina, macula, optic nerve", "Document per structure"]})),

dict(title="How Vision Works", tier=F,
 desc_pub=("Vision is a brain process fed by the eyes: light focused on the retina becomes "
  "electrical signals; the optic nerves carry them (half crossing at the chiasm); the visual "
  "cortex interprets edges, motion, color, and depth. Two eyes give depth perception "
  "(stereopsis) and a wide field.\n"
  "Vision develops in childhood - the brain learns to see - which is why early problems "
  "(lazy eye/amblyopia) must be caught young: the brain's learning window closes. Adults rely "
  "on stable, corrected input for every task from reading to driving."),
 desc_sig=("Signature vision education emphasizes the brain's role, explaining why childhood "
  "screening windows and adult correction both matter neurologically."),
 how_pub=("Eye care tests the chain: refraction (input quality), binocular testing (two-eye "
  "teamwork), visual fields (pathway integrity), and - for children - developmentally timed "
  "screenings. Problems are localized to eye, nerve, or brain processing."),
 how_sig=("Signature chain-testing protocols localize vision problems to their stage."),
 keys=["Vision is a brain process fed by eyes",
  "Two eyes: depth perception and wide field",
  "Brain learns to see in childhood",
  "Amblyopia must be caught young",
  "Adults need stable corrected input",
  "Test the whole chain"],
 reqs=["Binocular and visual field testing",
  "Childhood screening programs",
  "Neurologic referral pathways"],
 stds=["Pediatric vision screening guidelines (public)"],
 cites=["American Optometric Association — vision development (public)",
  "National Eye Institute — amblyopia (public)"],
 demo=("acuity", {"tests": [
   {"eye": "Right", "snellen": "20/20"},
   {"eye": "Left", "snellen": "20/40"},
   {"eye": "Both", "snellen": "20/25"}]})),

dict(title="Refractive Errors", tier=F,
 desc_pub=("Refractive errors are focusing mismatches: myopia (nearsightedness - distant blur, eye "
  "too long or cornea too steep), hyperopia (farsightedness - near strain, eye too short), "
  "astigmatism (irregular cornea/lens curvature blurring all distances), and presbyopia (age-"
  "related near-focus loss after ~40).\n"
  "All are corrected with lenses that refocus light onto the retina - glasses, contacts, or "
  "surgical reshaping. Myopia is rising worldwide, especially with intensive near work and low "
  "outdoor time in childhood."),
 desc_sig=("Signature refractive management tracks progression over time with intervention "
  "thresholds, so worsening myopia triggers control strategies rather than just stronger "
  "glasses."),
 how_pub=("Refraction determines the correcting lens power per eye; the prescription (sphere, "
  "cylinder, axis) is filled as glasses or contacts. Myopia-control options (special contacts, "
  "low-dose atropine via eye doctors) are discussed for progressing children. Presbyopia gets "
  "reading or progressive lenses."),
 how_sig=("Signature progression tracking flags rapid myopia change for control discussion."),
 keys=["Myopia: distant blur; hyperopia: near strain; astigmatism: irregular blur",
  "Presbyopia: near-focus loss after ~40",
  "Lenses refocus light onto the retina",
  "Glasses, contacts, or surgery correct",
  "Myopia rising worldwide in children",
  "Control strategies for progressing myopia"],
 reqs=["Refraction capability",
  "Prescription lens dispensing",
  "Myopia-control counseling"],
 stds=["Refraction and prescribing standards (public)"],
 cites=["American Optometric Association — refractive errors (public)",
  "National Eye Institute — myopia (public)"],
 demo=("rx", {"rx": {"OD": {"sph": -2.50, "cyl": -0.75, "axis": 180},
                        "OS": {"sph": -2.25, "cyl": -0.50, "axis": 175}}})),

dict(title="The Comprehensive Eye Exam", tier=F,
 desc_pub=("The comprehensive eye exam evaluates vision and eye health together: history, visual "
  "acuity, refraction, binocular function, eye pressure (tonometry), slit-lamp exam of front "
  "structures, and dilated retinal exam. It catches refractive error, glaucoma, macular "
  "degeneration, diabetic eye disease, and cataracts - often before symptoms.\n"
  "Adults generally need exams every 1-2 years (yearly with risk factors); children before "
  "school and as recommended. Dilation temporarily blurs near vision and light-sensitizes - "
  "bring sunglasses."),
 desc_sig=("Signature exam protocols standardize the full sequence with findings documented per "
  "structure, so comprehensive truly means comprehensive."),
 how_pub=("The optometrist works through the sequence, explaining each test, then synthesizes "
  "findings into diagnoses, prescriptions, and a plan - treatment, referral, or monitoring with "
  "risk-based recall. Patients leave understanding their eyes' status."),
 how_sig=("Signature structured findings documentation makes every exam's results comparable "
  "over time."),
 keys=["Vision + eye health together",
  "Acuity, refraction, binocular, pressure, slit lamp, dilated retina",
  "Catches disease before symptoms",
  "Adults every 1-2 years; yearly with risk",
  "Dilation: temporary blur and light sensitivity",
  "Leave understanding your eyes' status"],
 reqs=["Full exam equipment set",
  "Dilation capability",
  "Risk-based recall"],
 stds=["AOA comprehensive exam guidelines (public)"],
 cites=["American Optometric Association — comprehensive exams (public)"],
 demo=("protocol", {"steps": ["History", "Acuity + refraction", "Binocular testing",
   "Tonometry", "Slit-lamp exam", "Dilated retinal exam", "Plan + recall"]})),

dict(title="Reading an Eyeglass Prescription", tier=F,
 desc_pub=("Eyeglass prescriptions read: OD (right eye), OS (left eye); SPH (sphere: overall "
  "power, minus for myopia, plus for hyperopia); CYL (cylinder: astigmatism amount); AXIS "
  "(astigmatism orientation, 1-180); ADD (reading addition for multifocals); PD (pupillary "
  "distance, for lens centering).\n"
  "Example: OD -2.50 -0.75 x 180 means moderate myopia with mild astigmatism. Prescriptions "
  "expire (usually 1-2 years) because eyes change. This record is educational; prescriptions "
  "come from eye exams."),
 desc_sig=("Signature prescription tools decode any prescription into plain language with "
  "visualization, so patients understand what their lenses do."),
 how_pub=("Opticians verify the prescription is current, measure PD and fitting heights, help "
  "choose frames and lens options (materials, coatings), and verify the made glasses against "
  "the prescription with a lensometer before dispensing."),
 how_sig=("Signature verification checks every dispensed pair against the prescription before "
  "the patient leaves."),
 keys=["OD right, OS left; SPH, CYL, AXIS, ADD, PD",
  "Minus = myopia; plus = hyperopia",
  "AXIS 1-180 orients astigmatism correction",
  "ADD powers reading zones in multifocals",
  "Prescriptions expire in 1-2 years",
  "Verify made glasses with a lensometer"],
 reqs=["Current prescription from an exam",
  "PD and fitting measurements",
  "Lensometer verification"],
 stds=["Prescription release rules (FTC Eyeglass Rule, public)"],
 cites=["Federal Trade Commission — Eyeglass Rule (public)"],
 demo=("rx", {"rx": {"OD": {"sph": 1.75, "cyl": 0.0, "axis": 0},
                        "OS": {"sph": 2.00, "cyl": -1.25, "axis": 90}}})),

dict(title="Visual Acuity Testing", tier=F,
 desc_pub=("Visual acuity measures sharpness: the Snellen chart's 20/20 means seeing at 20 feet "
  "what normal eyes see at 20 feet; 20/40 means needing twice the size. Testing is done per eye "
  "and both together, with current correction and by pinhole (which hints whether blur is "
  "refractive).\n"
  "Acuity is one measure among many - contrast sensitivity, fields, and eye health complete "
  "the picture. For driving, most states require about 20/40."),
 desc_sig=("Signature acuity tracking charts results over visits, flagging unexplained drops for "
  "prompt workup."),
 how_pub=("Patients read progressively smaller lines at standardized distance (or with calibrated "
  "digital charts), per eye and binocular. Pinhole testing separates refractive from medical "
  "causes of reduced acuity. Results guide refraction and diagnosis."),
 how_sig=("Signature trend tracking catches gradual acuity loss that single visits miss."),
 keys=["Snellen 20/20: normal sharpness reference",
  "Per eye and both together",
  "Pinhole hints at refractive vs medical cause",
  "One measure among many",
  "Driving: ~20/40 in most states",
  "Track over time"],
 reqs=["Standardized chart at calibrated distance",
  "Pinhole occluder",
  "Consistent testing protocol"],
 stds=["Visual acuity testing standards (public literature)"],
 cites=["National Eye Institute — eye exams (public)"],
 demo=("acuity", {"tests": [
   {"eye": "Right", "snellen": "20/200"},
   {"eye": "Left", "snellen": "20/30"},
   {"eye": "Both", "snellen": "20/30"}]})),

dict(title="Eye Health and Safety Habits", tier=F,
 desc_pub=("Daily habits protect vision: UV-blocking sunglasses outdoors, safety glasses for "
  "hazardous work and sports, no rubbing with dirty hands, contact-lens hygiene (never sleep in "
  "lenses unless prescribed, replace on schedule), and managing screen time with breaks (20-20-20 "
  "rule: every 20 minutes, look 20 feet away for 20 seconds).\n"
  "Diet supports eyes: leafy greens, fish, and overall healthy eating associate with lower "
  "macular degeneration risk. Smoking harms eyes - quitting helps vision too."),
 desc_sig=("Signature habit coaching personalizes protection advice to the individual's risks - "
  "sports, work hazards, screen load - making safety relevant rather than generic."),
 how_pub=("Eye doctors assess lifestyle risks at exams and counsel specifically: athletes get "
  "sports eyewear prescriptions, workers get safety eyewear guidance, contact-lens wearers get "
  "hygiene retraining when needed. Habits are reviewed at recall visits."),
 how_sig=("Signature risk-personalized counseling targets the protections each patient "
  "actually needs."),
 keys=["UV sunglasses; safety glasses for hazards/sports",
  "Contact-lens hygiene: replace on schedule",
  "20-20-20 rule for screens",
  "Leafy greens and fish support eye health",
  "Smoking harms eyes",
  "Counsel by lifestyle risk"],
 reqs=["Risk assessment at exams",
  "Safety eyewear dispensing",
  "Contact-lens hygiene education"],
 stds=["Eye safety standards (ANSI Z87.1, public)",
  "Contact-lens care guidelines (public)"],
 cites=["American Optometric Association — eye safety (public)",
  "Centers for Disease Control — contact lens health (public)"],
 demo=("outcome", {"label": "Contact-lens wearers with good hygiene", "pre": 58, "post": 87})),

dict(title="Children's Vision", tier=F,
 desc_pub=("Children's vision needs active protection: screenings at well-child visits catch "
  "amblyopia (lazy eye), strabismus (eye turn), and significant refractive error during the "
  "brain's learning window - when treatment works. Uncorrected vision problems masquerade as "
  "behavior or learning problems.\n"
  "Signs: squinting, sitting very close, eye rubbing, headaches, avoiding near work, a wandering "
  "eye. Treatment - glasses, patching, vision therapy, sometimes surgery - works best young. "
  "This record is educational."),
 desc_sig=("Signature pediatric vision pathways schedule screenings at developmental milestones "
  "with automatic referral triggers, so no child's window is missed."),
 how_pub=("Pediatricians and schools screen; optometrists examine children with child-friendly "
  "techniques. Amblyopia gets glasses plus patching/atropine of the strong eye; strabismus may "
  "need surgery; refractive error gets glasses kids will actually wear."),
 how_sig=("Signature milestone-triggered screening ensures every child is checked in the "
  "treatment window."),
 keys=["Brain's learning window: treat young",
  "Screenings catch amblyopia, strabismus, refractive error",
  "Vision problems mimic learning problems",
  "Signs: squinting, close sitting, rubbing, headaches",
  "Glasses, patching, therapy, sometimes surgery",
  "Glasses kids will wear"],
 reqs=["Childhood screening programs",
  "Pediatric exam capability",
  "Parent education on signs"],
 stds=["Pediatric vision screening guidelines (public)"],
 cites=["American Optometric Association — children's vision (public)",
  "National Eye Institute — amblyopia (public)"],
 demo=("acuity", {"tests": [
   {"eye": "Right (age 5)", "snellen": "20/30"},
   {"eye": "Left (age 5)", "snellen": "20/100"}]})),

dict(title="Vision and Aging", tier=F,
 desc_pub=("Aging changes vision: presbyopia (near-focus loss) arrives in the 40s; cataracts "
  "cloud lenses (very common by the 70s, fixable with surgery); glaucoma risk rises; macular "
  "degeneration threatens central vision; dry eye increases. Annual exams after 60 catch these "
  "early.\n"
  "Adaptations keep life full: good lighting, large-print and high-contrast materials, "
  "multifocal lenses, and low-vision aids when needed. Vision loss is not an inevitable price "
  "of aging - most causes are treatable."),
 desc_sig=("Signature aging-vision pathways intensify surveillance with age and risk, pairing "
  "each condition's early signs with prompt action plans."),
 how_pub=("Annual dilated exams after 60 (earlier with risk factors) screen for cataract, "
  "glaucoma, macular changes, and diabetic disease. Findings trigger treatment, low-vision "
  "rehabilitation, or home adaptations. Lighting and contrast counseling is routine."),
 how_sig=("Signature age-and-risk surveillance schedules ensure nothing age-related goes "
  "unwatched."),
 keys=["Presbyopia in 40s; cataracts common by 70s",
  "Glaucoma and macular risks rise with age",
  "Annual exams after 60",
  "Most age-related vision loss is treatable",
  "Adaptations: lighting, contrast, multifocals, low-vision aids",
  "Vision loss is not inevitable"],
 reqs=["Annual dilated exams for older adults",
  "Low-vision rehabilitation access",
  "Home adaptation counseling"],
 stds=["AOA adult exam guidelines (public)"],
 cites=["National Eye Institute — aging and vision (public)",
  "American Optometric Association — senior vision (public)"],
 demo=("outcome", {"label": "Adults 60+ with annual eye exams", "pre": 52, "post": 81})),

# ---------------- Compounded (12) ----------------
dict(title="Vision Testing Methods", tier=C,
 desc_pub=("Beyond acuity, vision testing includes refraction (the lens-comparison 'which is "
  "better' determining prescription), keratometry/topography (corneal curvature mapping), "
  "tonometry (eye pressure), pachymetry (corneal thickness), and binocular testing (eye teaming, "
  "depth perception).\n"
  "Each test answers a question: refraction asks 'what lens?', topography asks 'is the cornea "
  "regular?', tonometry asks 'is pressure safe?'. Together they build the complete picture "
  "behind the prescription."),
 desc_sig=("Signature testing protocols sequence tests by diagnostic yield, so the highest-value "
  "tests are never skipped under time pressure."),
 how_pub=("The optometrist selects tests by history and age, performs them in efficient "
  "sequence, and interprets patterns - e.g., irregular topography plus thinning suggests "
  "keratoconus. Results feed diagnosis, prescription, and monitoring plans."),
 how_sig=("Signature yield-ordered test sequences keep comprehensive exams truly comprehensive."),
 keys=["Refraction, keratometry/topography, tonometry, pachymetry, binocular",
  "Each test answers a specific question",
  "Topography maps corneal regularity",
  "Tonometry screens glaucoma risk",
  "Binocular testing checks eye teamwork",
  "Patterns across tests make diagnoses"],
 reqs=["Calibrated test instruments",
  "Test selection by history",
  "Interpretation across test patterns"],
 stds=["Instrument calibration standards (public)"],
 cites=["American Optometric Association — testing (public)"],
 demo=("rx", {"rx": {"OD": {"sph": -4.00, "cyl": -1.50, "axis": 10},
                        "OS": {"sph": -3.75, "cyl": -1.25, "axis": 170}}})),

dict(title="Refraction and Prescription Determination", tier=C,
 desc_pub=("Refraction finds the lens power giving best vision: autorefractors give a starting "
  "estimate; subjective refraction ('which is better, one or two?') refines it with the "
  "patient's responses; retinoscopy objectively measures by observing light reflexes - "
  "essential for children and nonverbal patients.\n"
  "The endpoint balances sharpness with comfort: maximum plus for hyperopes (relaxing focusing "
  "effort), binocular balance so both eyes work together, and near additions matched to working "
  "distance."),
 desc_sig=("Signature refraction workflows standardize endpoints and binocular balancing, so "
  "prescriptions are consistently comfortable, not just sharp on the chart."),
 how_pub=("The optometrist starts from autorefraction or retinoscopy, refines sphere/cylinder/axis "
  "subjectively, balances the two eyes, and determines near adds. The final prescription is "
  "verified for comfort before dispensing."),
 how_sig=("Signature endpoint standardization prevents over-minused prescriptions that strain "
  "eyes."),
 keys=["Autorefractor estimates; subjective refines; retinoscopy objectifies",
  "'Which is better, one or two?'",
  "Balance sharpness with comfort",
  "Binocular balance for teamwork",
  "Near adds matched to working distance",
  "Verify comfort before dispensing"],
 reqs=["Phoropter/autorefractor/retinoscope",
  "Refraction technique training",
  "Comfort verification"],
 stds=["Refraction practice standards (public literature)"],
 cites=["American Optometric Association — refraction (public)"],
 demo=("rx", {"rx": {"OD": {"sph": 0.75, "cyl": -0.25, "axis": 90},
                        "OS": {"sph": 1.00, "cyl": -0.25, "axis": 85}}})),

dict(title="Eyeglass Lenses and Coatings", tier=C,
 desc_pub=("Eyeglass lenses vary by material (plastic/CR-39, polycarbonate for impact resistance, "
  "high-index for strong prescriptions), design (single vision, bifocal, trifocal, progressive "
  "multifocals), and coatings (anti-reflective, scratch-resistant, UV, blue-light filtering).\n"
  "Progressives give seamless distance-to-near vision but need adaptation; polycarbonate is the "
  "safety standard for children and sports. Matching lens to prescription, lifestyle, and budget "
  "is the optician's craft."),
 desc_sig=("Signature lens recommendation scores options against prescription strength, "
  "lifestyle, and budget - transparent trade-offs replacing upsell pressure."),
 how_pub=("Opticians review the prescription strength, discuss visual tasks (computer, driving, "
  "sports), recommend material and design, take precise measurements (PD, heights, wrap), and "
  "verify finished lenses before dispensing with adaptation counseling."),
 how_sig=("Signature trade-off scoring makes lens selection a shared decision with visible "
  "options."),
 keys=["Materials: CR-39, polycarbonate, high-index",
  "Designs: single vision, bifocal, progressive",
  "Coatings: AR, scratch, UV, blue-light",
  "Polycarbonate: safety standard for kids/sports",
  "Progressives need adaptation",
  "Match to prescription, lifestyle, budget"],
 reqs=["Lens option knowledge",
  "Precise measurements",
  "Verification before dispensing"],
 stds=["ANSI Z80 lens standards (public)",
  "Impact-resistance requirements (public)"],
 cites=["American National Standards Institute — Z80 (public)"],
 demo=("rx", {"rx": {"OD": {"sph": -6.50, "cyl": 0.0, "axis": 0},
                        "OS": {"sph": -6.25, "cyl": -0.50, "axis": 180}}})),

dict(title="Contact Lenses", tier=C,
 desc_pub=("Contact lenses correct vision on the eye: soft daily/monthly lenses, rigid gas-"
  "permeable (sharper for astigmatism/keratoconus), toric (astigmatism), multifocal (presbyopia), "
  "and specialty scleral lenses vaulting over irregular corneas. Fitting measures curvature, "
  "diameter, and tear behavior.\n"
  "Hygiene is the safety linchpin: wash hands, rub and rinse (or use dailies), never sleep in "
  "lenses unless specifically prescribed, replace on schedule. Infections from poor hygiene can "
  "threaten sight. This record is educational; fitting is professional."),
 desc_sig=("Signature contact-lens programs pair fitting with hygiene coaching and compliance "
  "tracking, because the lens is only as safe as its care."),
 how_pub=("Fitters measure corneal curvature and evaluate tears, trial diagnostic lenses, assess "
  "fit/movement/vision, and teach insertion, removal, and care. Follow-ups check corneal health; "
  "prescriptions specify brand, parameters, and replacement schedule."),
 how_sig=("Signature compliance tracking flags risky wear patterns for re-education."),
 keys=["Soft, RGP, toric, multifocal, scleral",
  "Fitting: curvature, diameter, tears",
  "Hygiene is the safety linchpin",
  "Dailies reduce infection risk",
  "Never sleep in lenses unless prescribed",
  "Replace on schedule"],
 reqs=["Fitting sets and expertise",
  "Hygiene education",
  "Corneal health follow-up"],
 stds=["Contact lens prescribing standards (public)",
  "FTC Contact Lens Rule (public)"],
 cites=["Federal Trade Commission — Contact Lens Rule (public)",
  "Centers for Disease Control — contact lens health (public)"],
 demo=("outcome", {"label": "Wearers compliant with replacement schedule", "pre": 49, "post": 82})),

dict(title="Binocular Vision Testing", tier=C,
 desc_pub=("Binocular vision is the eyes working as a team: alignment (no strabismus), convergence "
  "(turning in for near), accommodation (focusing), and stereopsis (depth perception). Testing "
  "includes cover tests, near point of convergence, fusional ranges, and stereo tests.\n"
  "Convergence insufficiency - eyes tiring on near work - is common and treatable with vision "
  "therapy. Symptoms masquerade as attention problems: headaches, losing place reading, avoiding "
  "near work. This record is educational."),
 desc_sig=("Signature binocular assessment standardizes the test battery with normative "
  "comparisons, so teamwork deficits are quantified, not guessed."),
 how_pub=("Optometrists test alignment and teamwork at distance and near, measure convergence "
  "and focusing ranges, and assess depth perception. Deficits get prism, vision therapy, or "
  "referral; progress is re-measured against norms."),
 how_sig=("Signature quantified norms make binocular diagnoses objective and progress "
  "measurable."),
 keys=["Alignment, convergence, accommodation, stereopsis",
  "Cover tests, NPC, fusional ranges, stereo",
  "Convergence insufficiency: common, treatable",
  "Symptoms mimic attention problems",
  "Vision therapy for teamwork deficits",
  "Re-measure against norms"],
 reqs=["Binocular test battery",
  "Normative data",
  "Vision therapy referral access"],
 stds=["Binocular vision testing standards (public literature)"],
 cites=["American Optometric Association — binocular vision (public)"],
 demo=("outcome", {"label": "Convergence insufficiency resolved with therapy", "pre": 55, "post": 87})),

dict(title="Color Vision Testing", tier=C,
 desc_pub=("Color vision testing detects deficiencies (most commonly red-green, X-linked, affecting "
  "about 8% of males): Ishihara plates (numbers in dot patterns) screen quickly; Farnsworth D-15 "
  "and anomaloscopes characterize precisely.\n"
  "Most color deficiency is mild and managed with adaptations - labeling, lighting, technology - "
  "though some occupations (pilots, electricians) have standards. Testing matters for career "
  "guidance and safety."),
 desc_sig=("Signature color-vision services pair precise characterization with adaptation "
  "counseling, turning a diagnosis into a practical plan."),
 how_pub=("Screening with Ishihara plates identifies suspects; arrangement tests characterize "
  "type and severity. Counselors explain inheritance, discuss occupational implications honestly, "
  "and teach adaptations - color-naming apps, organized wiring, lighting choices."),
 how_sig=("Signature adaptation plans translate test results into daily-life strategies."),
 keys=["Red-green most common; ~8% of males",
  "Ishihara screens; D-15/anomaloscope characterize",
  "Most cases mild and adaptable",
  "Occupational standards exist for some jobs",
  "Adaptations: labeling, lighting, tech",
  "Career guidance matters"],
 reqs=["Ishihara and arrangement tests",
  "Proper lighting for testing",
  "Occupational guidance knowledge"],
 stds=["Color vision testing standards (public literature)"],
 cites=["National Eye Institute — color blindness (public)"],
 demo=("protocol", {"steps": ["Ishihara screening", "D-15 arrangement if indicated",
   "Characterize type/severity", "Explain inheritance", "Occupational counseling",
   "Teach adaptations"]})),

dict(title="Visual Field Testing", tier=C,
 desc_pub=("Visual field testing maps peripheral vision: automated perimetry (press a button when "
  "you see lights) detects glaucoma and neurological defects; confrontation fields screen "
  "quickly; Amsler grids monitor macular distortion at home.\n"
  "Glaucoma's early field loss is silent - testing catches it. Neurological patterns (like "
  "hemianopia) localize brain lesions. Reliable fields need patient attention; technicians "
  "coach and monitor."),
 desc_sig=("Signature field-testing programs schedule perimetry by risk with reliability "
  "tracking, so glaucoma progression is caught early and confidently."),
 how_pub=("Technicians explain the test, ensure correct positioning and refraction, and monitor "
  "reliability indices. Optometrists interpret patterns - arcuate defects suggest glaucoma, "
  "hemianopia suggests neurology - and compare serial fields for progression."),
 how_sig=("Signature serial-field comparison with reliability weighting makes progression "
  "decisions evidence-based."),
 keys=["Perimetry maps peripheral vision",
  "Detects glaucoma and neurological defects",
  "Amsler grids monitor macula at home",
  "Early glaucoma field loss is silent",
  "Patterns localize: eye vs brain",
  "Reliability indices validate results"],
 reqs=["Automated perimeter",
  "Trained technicians",
  "Serial comparison capability"],
 stds=["Perimetry testing standards (public literature)"],
 cites=["American Academy of Ophthalmology — visual fields (public)",
  "National Eye Institute — glaucoma (public)"],
 demo=("outcome", {"label": "Glaucoma suspects with baseline fields", "pre": 61, "post": 93})),

dict(title="Common Eye Conditions: Dry Eye and Pink Eye", tier=C,
 desc_pub=("Dry eye - insufficient or poor-quality tears - causes burning, grittiness, and "
  "fluctuating vision; it is increasingly common with screen time and aging. Treatment steps up: "
  "artificial tears, warm compresses and lid hygiene, prescription drops, punctal plugs.\n"
  "Pink eye (conjunctivitis) reddens from viral, bacterial, or allergic causes; viral is most "
  "common and contagious - hand hygiene and not sharing towels limit spread. Bacterial cases may "
  "need antibiotic drops; allergic responds to allergy treatment. This record is educational; "
  "diagnosis belongs with eye professionals."),
 desc_sig=("Signature dry-eye management stages severity with matched treatment ladders, so care "
  "escalates by evidence rather than by trial and error."),
 how_pub=("Eye doctors assess tear quality/quantity (staining, breakup time, meibomian glands) for "
  "dry eye and step treatment accordingly. For pink eye, history and exam distinguish viral, "
  "bacterial, and allergic; treatment matches cause with contagion counseling."),
 how_sig=("Signature stepped ladders make dry-eye escalation systematic."),
 keys=["Dry eye: burning, grittiness, fluctuating vision",
  "Treatment steps up: tears, hygiene, prescriptions, plugs",
  "Pink eye: viral (common/contagious), bacterial, allergic",
  "Hand hygiene limits spread",
  "Match treatment to cause",
  "Educational record; professionals diagnose"],
 reqs=["Tear assessment capability",
  "Stepped treatment protocols",
  "Contagion counseling"],
 stds=["Dry eye treatment guidelines (public literature)"],
 cites=["American Optometric Association — dry eye (public)",
  "Centers for Disease Control — conjunctivitis (public)"],
 demo=("match", {"symptom": "burning, gritty eyes worse with screens",
   "conditions": [{"condition": "Dry eye", "signs": ["burning, gritty eyes worse with screens"], "action": "tear assessment, stepped treatment"},
                  {"condition": "Bacterial conjunctivitis", "signs": [], "action": "exam for discharge"},
                  {"condition": "Allergic conjunctivitis", "signs": [], "action": "allergy history"}]})),

dict(title="Cataracts", tier=C,
 desc_pub=("Cataracts cloud the eye's lens - usually with age - causing blur, glare, halos, and "
  "fading colors. They are the world's leading cause of blindness but among the most treatable: "
  "surgery replaces the cloudy lens with an artificial intraocular lens (IOL), typically in a "
  "15-minute outpatient procedure with rapid recovery.\n"
  "Timing is personal: surgery when vision interferes with life, not by calendar. IOL options "
  "(monofocal, multifocal, toric) are chosen with the surgeon. This record is educational; "
  "surgical decisions are clinical."),
 desc_sig=("Signature cataract pathways standardize pre-op measurement, IOL counseling, and "
  "post-op review, so the commonest surgery stays reliably excellent."),
 how_pub=("Optometrists diagnose and monitor cataracts, referring when vision affects life. "
  "Surgeons measure precisely (biometry), counsel on IOL options, perform phacoemulsification "
  "with IOL implant, and manage post-op care. Optometrists resume long-term follow-up."),
 how_sig=("Signature IOL counseling tools visualize trade-offs of lens options for informed "
  "choice."),
 keys=["Clouded lens: blur, glare, halos, fading color",
  "Leading cause of blindness; highly treatable",
  "Surgery: ~15 minutes outpatient, rapid recovery",
  "Timing: when vision interferes with life",
  "IOL options: monofocal, multifocal, toric",
  "Educational record; surgeons decide"],
 reqs=["Cataract diagnosis and monitoring",
  "Biometry and surgical referral",
  "Post-op co-management"],
 stds=["Cataract surgery guidelines (public literature)"],
 cites=["American Academy of Ophthalmology — cataracts (public)",
  "National Eye Institute — cataracts (public)"],
 demo=("outcome", {"label": "Cataract patients achieving 20/40 or better", "pre": 88, "post": 97})),

dict(title="Glaucoma", tier=C,
 desc_pub=("Glaucoma damages the optic nerve - often from high eye pressure - causing silent, "
  "irreversible peripheral vision loss. It is a leading cause of irreversible blindness, and "
  "early disease has no symptoms: detection requires exams with tonometry, optic nerve "
  "evaluation, and visual fields.\n"
  "Treatment (drops, laser, surgery) lowers pressure to slow damage; lost vision does not "
  "return, so early detection is everything. Risk factors: age, family history, African ancestry, "
  "high myopia, steroid use. This record is educational."),
 desc_sig=("Signature glaucoma management runs risk-stratified surveillance with progression "
  "analysis on serial fields and nerve imaging, catching change at the earliest signal."),
 how_pub=("Eye doctors screen pressure and nerves at exams; suspects get pachymetry, gonioscopy, "
  "and baseline fields plus OCT nerve imaging. Confirmed cases start pressure-lowering "
  "treatment with target pressures; serial testing monitors for progression, escalating "
  "treatment as needed."),
 how_sig=("Signature progression analysis distinguishes real change from test noise, guiding "
  "timely escalation."),
 keys=["Optic nerve damage, often from pressure",
  "Silent early; irreversible loss",
  "Detection: tonometry, nerve exam, fields",
  "Treatment lowers pressure; lost vision stays lost",
  "Risk: age, family, ancestry, myopia, steroids",
  "Early detection is everything"],
 reqs=["Tonometry and nerve evaluation",
  "Visual fields and OCT",
  "Target-pressure management"],
 stds=["Glaucoma management guidelines (public literature)"],
 cites=["American Academy of Ophthalmology — glaucoma (public)",
  "National Eye Institute — glaucoma (public)"],
 demo=("outcome", {"label": "Glaucoma patients with controlled pressure", "pre": 68, "post": 89})),

dict(title="Macular Degeneration", tier=C,
 desc_pub=("Age-related macular degeneration (AMD) damages the macula - central sharp vision - "
  "causing wavy lines, blind spots, and reading difficulty. Dry AMD (common, slower) has no "
  "cure but AREDS2 vitamins may slow it; wet AMD (bleeding vessels) is treated urgently with "
  "anti-VEGF injections that preserve sight.\n"
  "Risk factors: age, smoking, family history. Amsler grid home monitoring catches wet-AMD "
  "conversion early - when treatment works best. This record is educational."),
 desc_sig=("Signature AMD pathways combine risk counseling, AREDS2 guidance, Amsler monitoring, "
  "and rapid wet-AMD referral - a complete surveillance system for the at-risk."),
 how_pub=("Dilated exams with macular imaging (OCT) stage AMD; dry cases get lifestyle counseling, "
  "AREDS2 discussion, and Amsler grids; wet cases are referred urgently for anti-VEGF therapy "
  "with ongoing injection schedules. Low-vision aids help advanced cases."),
 how_sig=("Signature Amsler-plus-OCT surveillance catches conversion at the treatable moment."),
 keys=["Damages central sharp vision",
  "Dry: common, slower; wet: urgent, injectable treatment",
  "AREDS2 vitamins may slow dry AMD",
  "Smoking is a modifiable risk",
  "Amsler grid catches wet conversion early",
  "Low-vision aids for advanced cases"],
 reqs=["Macular OCT imaging",
  "AREDS2 counseling",
  "Urgent wet-AMD referral pathway"],
 stds=["AMD management guidelines (public literature)"],
 cites=["American Academy of Ophthalmology — AMD (public)",
  "National Eye Institute — AMD (public)"],
 demo=("match", {"symptom": "straight lines look wavy",
   "conditions": [{"condition": "Wet AMD", "signs": ["straight lines look wavy"], "action": "urgent retinal referral"},
                  {"condition": "Dry AMD", "signs": [], "action": "AREDS2 + monitoring"},
                  {"condition": "Epiretinal membrane", "signs": [], "action": "retinal evaluation"}]})),

dict(title="Diabetic Eye Disease", tier=C,
 desc_pub=("Diabetes damages retinal vessels - diabetic retinopathy - plus raises cataract and "
  "glaucoma risk; it is a leading cause of working-age blindness. Early disease is silent; "
  "annual dilated exams catch it when treatment (laser, injections, surgery) works best.\n"
  "Blood sugar, blood pressure, and cholesterol control slow progression - eye care and diabetes "
  "care are one fight. Pregnancy with diabetes needs more frequent exams. This record is "
  "educational."),
 desc_sig=("Signature diabetic eye pathways link diabetes registries to eye-exam recall, closing "
  "the gap for patients who never get referred."),
 how_pub=("Primary care refers every diabetes patient for annual dilated exams; eye doctors grade "
  "retinopathy, image with OCT, and treat sight-threatening disease promptly while counseling on "
  "systemic control. Teleretinal screening extends reach in primary care."),
 how_sig=("Signature registry-linked recall ensures no diabetes patient misses their annual "
  "eye exam."),
 keys=["Retinopathy: leading working-age blindness cause",
  "Early disease silent; annual dilated exams",
  "Treatment: laser, injections, surgery",
  "Sugar, pressure, cholesterol control slows it",
  "Pregnancy needs more frequent exams",
  "Eye and diabetes care are one fight"],
 reqs=["Annual dilated exam program for diabetes",
  "Retinopathy grading and OCT",
  "Teleretinal screening option"],
 stds=["Diabetic retinopathy screening guidelines (public)"],
 cites=["American Diabetes Association — eye complications (public)",
  "National Eye Institute — diabetic eye disease (public)"],
 demo=("outcome", {"label": "Diabetes patients with annual dilated exams", "pre": 55, "post": 84})),

# ---------------- Advanced (11) ----------------
dict(title="Advanced Retinal Imaging", tier=A,
 desc_pub=("Advanced retinal imaging sees disease before symptoms: optical coherence tomography "
  "(OCT) shows retinal layers in cross-section; OCT-angiography maps blood flow without dye; "
  "fundus photography documents; fluorescein angiography traces circulation with dye.\n"
  "These tools transformed retina care - guiding injections, laser, and surgery with micron "
  "precision. Interpretation requires training; serial imaging tracks progression objectively. "
  "This record is educational."),
 desc_sig=("Signature retinal imaging protocols match modality to disease with serial comparison "
  "analytics, making progression decisions data-driven."),
 how_pub=("Eye doctors order imaging by indication, capture with trained technicians, interpret "
  "systematically (layers, fluid, flow, change from prior), and document. Findings drive "
  "treatment timing; serial scans measure response."),
 how_sig=("Signature serial analytics quantify change, removing guesswork from retreatment "
  "decisions."),
 keys=["OCT: cross-section layers; OCT-A: blood flow without dye",
  "Fundus photos document; fluorescein traces circulation",
  "Micron precision guides treatment",
  "Serial imaging tracks progression",
  "Interpretation requires training",
  "Match modality to disease"],
 reqs=["OCT/OCT-A capability",
  "Trained imagers and interpreters",
  "Serial comparison workflow"],
 stds=["Retinal imaging guidelines (public literature)"],
 cites=["American Academy of Ophthalmology — imaging (public)"],
 demo=("protocol", {"steps": ["Determine imaging indication", "Capture with trained tech",
   "Systematic interpretation", "Compare to prior serial", "Document findings",
   "Drive treatment timing"]})),

dict(title="Optical Coherence Tomography", tier=A,
 desc_pub=("Optical coherence tomography (OCT) is the retina's MRI: light-based cross-sections "
  "revealing individual retinal layers, fluid pockets, and nerve fiber thickness - essential for "
  "macular degeneration, diabetic edema, and glaucoma management.\n"
  "OCT turned 'watch and wait' into 'measure and act': fluid on OCT triggers treatment; "
  "resolution confirms response. Normative databases flag abnormal thinning. This record is "
  "educational."),
 desc_sig=("Signature OCT workflows embed normative comparison and change analysis in every "
  "scan review, standardizing expert-level interpretation."),
 how_pub=("Technicians capture macular and nerve scans per protocol; software segments layers and "
  "compares to norms; doctors interpret fluid, thickness, and change. Treatment decisions - "
  "inject, observe, escalate - follow the images."),
 how_sig=("Signature embedded analytics make every OCT review quantitatively rigorous."),
 keys=["Light-based retinal cross-sections",
  "Layers, fluid, nerve fiber thickness",
  "Guides AMD, diabetic edema, glaucoma",
  "'Measure and act' replaces 'watch and wait'",
  "Normative databases flag abnormality",
  "Serial change drives decisions"],
 reqs=["OCT device",
  "Scan protocols per disease",
  "Normative database software"],
 stds=["OCT imaging standards (public literature)"],
 cites=["American Academy of Ophthalmology — OCT (public)"],
 demo=("outcome", {"label": "Treatment decisions supported by OCT", "pre": 71, "post": 96})),

dict(title="Low Vision Rehabilitation", tier=A,
 desc_pub=("Low vision rehabilitation helps people with uncorrectable vision loss use remaining "
  "sight fully: magnifiers, telescopes, electronic video magnifiers, lighting and contrast "
  "optimization, eccentric viewing training (using peripheral retina), and daily-living "
  "adaptations.\n"
  "The goal is function, not acuity numbers: reading mail, cooking safely, recognizing faces. "
  "Rehabilitation is team-based - optometrists, occupational therapists, orientation and "
  "mobility specialists - and deeply personal."),
 desc_sig=("Signature low-vision rehabilitation builds task-based device prescriptions with "
  "training milestones, so each aid is mastered for the tasks that matter to the person."),
 how_pub=("Low-vision optometrists assess remaining vision and task goals, trial devices on real "
  "tasks (reading the person's own mail), prescribe the matched aids, and arrange OT and O&M "
  "training. Follow-up refines the toolkit as needs change."),
 how_sig=("Signature task-based trials ensure every prescribed aid earns its place on a real "
  "task."),
 keys=["Maximize remaining sight",
  "Magnifiers, telescopes, video magnifiers, lighting",
  "Goal: function, not acuity numbers",
  "Team: optometry, OT, orientation & mobility",
  "Trial devices on the person's real tasks",
  "Deeply personal rehabilitation"],
 reqs=["Low-vision assessment and device inventory",
  "OT and O&M partnerships",
  "Task-based trial process"],
 stds=["Low vision rehabilitation guidelines (public literature)"],
 cites=["American Optometric Association — low vision (public)",
  "National Eye Institute — low vision (public)"],
 demo=("outcome", {"label": "Clients achieving priority visual tasks", "pre": 48, "post": 82})),

dict(title="Assistive Vision Systems", tier=A,
 desc_pub=("Assistive vision systems extend beyond optical aids: screen readers and magnification "
  "software, text-to-speech apps, AI object and scene describers, smart glasses with navigation "
  "cues, and braille displays. Mainstream smartphones are now powerful assistive platforms.\n"
  "Training determines benefit more than the device. Assessment matches technology to tasks, "
  "abilities, and preferences - with ongoing support as technology evolves."),
 desc_sig=("Signature assistive-vision matching maintains a current technology catalog with "
  "task-based recommendations, keeping prescriptions modern in a fast-moving field."),
 how_pub=("Rehabilitation professionals assess tasks and abilities, trial candidate technologies, "
  "train systematically, and provide ongoing support. Mainstream tech (phone accessibility "
  "features) is configured first; specialized devices fill remaining gaps."),
 how_sig=("Signature current-catalog matching prevents outdated recommendations in a rapidly "
  "evolving field."),
 keys=["Screen readers, magnifiers, AI describers, smart glasses, braille",
  "Smartphones are powerful assistive platforms",
  "Training matters more than the device",
  "Match tech to tasks and preferences",
  "Configure mainstream tech first",
  "Ongoing support as tech evolves"],
 reqs=["Technology assessment and trial inventory",
  "Systematic training",
  "Ongoing support capacity"],
 stds=["Assistive technology service standards (public)"],
 cites=["American Foundation for the Blind — technology (public)"],
 demo=("protocol", {"steps": ["Assess tasks and abilities", "Configure phone accessibility first",
   "Trial specialized candidates", "Systematic training", "Ongoing support"]})),

dict(title="Vision Therapy", tier=A,
 desc_pub=("Vision therapy is supervised eye-exercise treatment for binocular vision problems - "
  "convergence insufficiency, accommodative dysfunction, some strabismus - using lenses, prisms, "
  "and computerized activities to retrain eye teaming and focusing. Evidence is strongest for "
  "convergence insufficiency.\n"
  "It is not a treatment for learning disabilities themselves, though it can remove visual "
  "barriers to reading. Programs run weekly in-office with home reinforcement, typically 12-24 "
  "weeks. This record is educational."),
 desc_sig=("Signature vision therapy standardizes protocols per diagnosis with progress metrics, "
  "so therapy is dosed and completed by evidence."),
 how_pub=("Optometrists diagnose binocular deficits with quantified testing, prescribe therapy "
  "protocols, and supervise weekly sessions with home activities. Progress is re-measured "
  "against norms; therapy ends when criteria are met."),
 how_sig=("Signature protocol-per-diagnosis with metric endpoints prevents endless therapy."),
 keys=["Supervised treatment for binocular problems",
  "Strongest evidence: convergence insufficiency",
  "Lenses, prisms, computerized activities",
  "Not a learning-disability treatment itself",
  "Weekly in-office + home, 12-24 weeks",
  "End when metric criteria met"],
 reqs=["Binocular diagnosis capability",
  "Therapy equipment and protocols",
  "Progress metrics"],
 stds=["Vision therapy practice guidelines (public literature)"],
 cites=["American Optometric Association — vision therapy (public)",
  "Convergence Insufficiency Treatment Trial (public research)"],
 demo=("outcome", {"label": "Convergence insufficiency normalized", "pre": 52, "post": 88})),

dict(title="Specialty Contact Lenses", tier=A,
 desc_pub=("Specialty contact lenses solve hard cases: scleral lenses vault over keratoconus and "
  "severe dry eye, orthokeratology reshapes corneas overnight for daytime freedom (and myopia "
  "control), and custom toric/multifocal designs handle complex prescriptions.\n"
  "Fitting is advanced work - topography-guided, with careful tear and corneal monitoring. "
  "These lenses restore vision where glasses cannot. This record is educational; fitting is "
  "specialist work."),
 desc_sig=("Signature specialty-lens fitting uses topography-driven design with outcome tracking, "
  "so complex fits are engineered precisely."),
 how_pub=("Specialists map corneas with topography, design or select trial lenses, evaluate fit "
  "with fluorescein patterns, and monitor corneal health closely. Patients learn specialized "
  "insertion, removal, and care."),
 how_sig=("Signature topography-driven design shortens the path to successful complex fits."),
 keys=["Scleral: vaults keratoconus, severe dry eye",
  "Ortho-k: overnight reshaping, myopia control",
  "Custom toric/multifocal for complex prescriptions",
  "Topography-guided fitting",
  "Restore vision glasses cannot",
  "Specialist work with close monitoring"],
 reqs=["Corneal topography",
  "Specialty lens inventory and lab",
  "Advanced fitting expertise"],
 stds=["Specialty lens fitting standards (public literature)"],
 cites=["Scleral Lens Education Society — public resources (public)"],
 demo=("outcome", {"label": "Keratoconus patients achieving functional vision", "pre": 41, "post": 86})),

dict(title="Myopia Control", tier=A,
 desc_pub=("Myopia control slows childhood nearsightedness progression - important because high "
  "myopia raises retinal detachment, glaucoma, and myopia-macula risks. Evidence-backed options: "
  "low-dose atropine drops, orthokeratology, multifocal contacts, and more outdoor time.\n"
  "Axial length measurement tracks eye growth objectively. Starting early in progression "
  "maximizes benefit. This record is educational; treatment decisions belong with eye doctors."),
 desc_sig=("Signature myopia management pairs axial-length monitoring with intervention "
  "thresholds, so control starts at the optimal moment for each child."),
 how_pub=("Eye doctors measure refraction and axial length, assess progression rate and risk "
  "factors, and discuss options with families. Chosen interventions are monitored with regular "
  "axial measurements; strategies adjust with growth."),
 how_sig=("Signature threshold-based initiation takes the guesswork out of when to start."),
 keys=["Slowing progression reduces lifelong risks",
  "Options: atropine, ortho-k, multifocal contacts, outdoor time",
  "Axial length tracks growth objectively",
  "Start early in progression",
  "High myopia risks: detachment, glaucoma, maculopathy",
  "Eye doctors decide with families"],
 reqs=["Axial length measurement",
  "Myopia-control option availability",
  "Family counseling"],
 stds=["Myopia management guidelines (public literature)"],
 cites=["American Optometric Association — myopia control (public)",
  "International Myopia Institute — public resources (public)"],
 demo=("outcome", {"label": "Annual myopia progression slowed (diopters)", "pre": 100, "post": 45})),

dict(title="Occupational Vision Services", tier=A,
 desc_pub=("Occupational vision services match vision to work demands: safety eyewear programs "
  "(ANSI Z87.1), computer-vision evaluations with task-specific lenses, color-vision screening "
  "for safety-critical roles, and driver vision standards.\n"
  "Computer vision syndrome - eyestrain, dryness, headaches - responds to ergonomics, breaks, "
  "and lenses tuned to screen distance. Employers benefit: comfortable workers are productive "
  "workers."),
 desc_sig=("Signature occupational vision programs audit workplace visual demands and prescribe "
  "task-matched corrections, turning vision into a productivity input."),
 how_pub=("Providers assess job visual demands, test accordingly, and prescribe safety eyewear or "
  "task lenses. Programs include injury tracking, compliance monitoring, and ergonomic "
  "counseling. Standards compliance is documented."),
 how_sig=("Signature demand-audited prescriptions match correction to the actual task."),
 keys=["Safety eyewear: ANSI Z87.1",
  "Computer lenses tuned to screen distance",
  "Color screening for safety-critical roles",
  "Computer vision syndrome: ergonomics + breaks + lenses",
  "Injury tracking and compliance",
  "Comfortable workers are productive"],
 reqs=["Safety eyewear program capability",
  "Workplace demand assessment",
  "Compliance tracking"],
 stds=["ANSI Z87.1 eye protection (public)",
  "OSHA eye protection requirements (public)"],
 cites=["Occupational Safety and Health Administration — eye protection (public)"],
 demo=("outcome", {"label": "Workplace eye injuries (lower better)", "pre": 100, "post": 38})),

dict(title="Sports Vision", tier=A,
 desc_pub=("Sports vision optimizes visual skills for athletics: dynamic acuity, eye tracking, "
  "peripheral awareness, depth perception, and reaction time - plus protective eyewear matched to "
  "each sport. Training can sharpen sport-specific visual skills.\n"
  "Protective standards matter most: polycarbonate eyewear prevents the thousands of annual "
  "sports eye injuries, especially in racket sports and basketball. This record is educational."),
 desc_sig=("Signature sports-vision programs baseline athletes' visual skills and train deficits, "
  "treating vision as a trainable performance input."),
 how_pub=("Practitioners test sport-relevant visual skills, prescribe protective eyewear, and "
  "design training drills for identified deficits. Contact-lens wearers get sport-specific "
  "guidance; post-concussion vision issues get rehabilitation referral."),
 how_sig=("Signature skill baselines make visual training measurable like physical training."),
 keys=["Dynamic acuity, tracking, peripheral awareness, depth, reaction",
  "Protective eyewear per sport",
  "Polycarbonate prevents injuries",
  "Training sharpens sport-specific skills",
  "Post-concussion vision needs rehab",
  "Vision is trainable performance input"],
 reqs=["Sports vision testing",
  "Protective eyewear dispensing",
  "Training program design"],
 stds=["Sports eye protection standards (ASTM, public)"],
 cites=["American Optometric Association — sports vision (public)"],
 demo=("outcome", {"label": "Athletes with appropriate protective eyewear", "pre": 44, "post": 89})),

dict(title="Teleoptometry", tier=A,
 desc_pub=("Teleoptometry delivers eye care remotely: triage and follow-up by video, remote "
  "refraction technologies, teleretinal screening for diabetic disease, and store-and-forward "
  "consultation. It extends access where optometrists are scarce.\n"
  "Limits are real: comprehensive dilated exams and many diagnoses still need in-person care. "
  "Responsible teleoptometry defines its scope clearly and refers appropriately."),
 desc_sig=("Signature teleoptometry defines scope-gated virtual pathways with automatic "
  "in-person escalation triggers, so remote care is safe by design."),
 how_pub=("Providers establish the technology platform, define which presentations suit virtual "
  "care, and build referral pathways for everything else. Teleretinal programs place cameras in "
  "primary care with remote grading. Quality is monitored like in-person care."),
 how_sig=("Signature escalation triggers ensure virtual care never delays needed in-person "
  "exams."),
 keys=["Video triage/follow-up, remote refraction, teleretinal screening",
  "Extends access where ODs are scarce",
  "Dilated exams still need in-person",
  "Define scope clearly; refer appropriately",
  "Teleretinal screening in primary care",
  "Monitor quality like in-person care"],
 reqs=["Telehealth platform",
  "Scope definitions and escalation triggers",
  "Teleretinal camera network option"],
 stds=["State telehealth regulations (public)"],
 cites=["American Optometric Association — telehealth (public)"],
 demo=("outcome", {"label": "Diabetes patients screened via teleretinal", "pre": 38, "post": 74})),

dict(title="The Future of Vision Care", tier=A,
 desc_pub=("Vision care's future: AI-assisted image interpretation, gene therapies for inherited "
  "retinal disease, longer-acting injections, smart contact lenses sensing health markers, and "
  "regenerative approaches to the optic nerve. Access expands through telehealth and task-"
  "sharing.\n"
  "The direction is preservation and equity: saving sight earlier and reaching everyone. "
  "This database's Signature edition prototypes the knowledge core such systems need. "
  "Educational record."),
 desc_sig=("The Signature future-state is a vision operating system: risk-based surveillance, "
  "AI-assisted detection, precision treatment, and assistive integration - with preservation as "
  "the prime directive. This database is a prototype of that system's knowledge core."),
 how_pub=("Practices adopt validated AI and imaging, participate in gene-therapy referral "
  "networks, expand telehealth access, and measure outcomes. Innovations are validated for "
  "safety and equity before scaling."),
 how_sig=("Signature's operating-system vision makes preservation the default across the "
  "continuum."),
 keys=["AI image interpretation, gene therapy, smart lenses",
  "Longer-acting treatments reduce burden",
  "Regenerative optic-nerve research",
  "Telehealth and task-sharing expand access",
  "Validate for safety and equity",
  "Direction: preservation and equity"],
 reqs=["Technology evaluation discipline",
  "Gene-therapy referral networks",
  "Equity monitoring"],
 stds=["Emerging standards for AI in eye care (public literature)"],
 cites=["National Eye Institute — research advances (public)"],
 demo=("outcome", {"label": "Preventable vision loss prevented", "pre": 58, "post": 82})),
]
