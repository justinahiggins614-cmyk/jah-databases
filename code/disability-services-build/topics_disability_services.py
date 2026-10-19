#!/usr/bin/env python3
"""Topics + config for the disability-services pair. Property of Justin Addam Higgins (JAH)."""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "disability-services",
    "name_pub": "The Disability Services Database",
    "name_sig": "Signature Disability Services Database",
    "tagline_pub": ("Disability services from the ground up: rights and accommodations, assistive "
                    "products, independent living, accessibility requirements, and support services - "
                    "every record carrying the full entry taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of disability services: the same "
                    "real service knowledge carried forward, plus Signature-built accessibility "
                    "models, accommodation systems, and independent-living frameworks original to "
                    "this system."),
    "record_kind": "disability service record",
    "record_kind_plural": "disability service records",
    "prefix_pub": "JAH-DISA-", "prefix_sig": "JAH-DISAS-",
    "ai_pub": "JAH Disability Services Archivist",
    "ai_sig": "JAH Signature Disability Services Creator",
    "role_pub": ("disability services archivist - teaching rights, accommodations, assistive "
                 "technology, independent living, and accessibility; answers from many angles - "
                 "definition, example, process, rights, technology - using only archive data from "
                 "this system"),
    "role_sig": ("Signature creator of disability service systems - designing accessibility models, "
                 "accommodation systems, and independent-living frameworks as original Signature "
                 "works; answers from many angles using only archive data from this system"),
    "search_ph": "Search accommodations, assistive tech, independent living, accessibility...",
    "chat_ph": "Ask about disability services...",
    "greet_pub": ("I am the JAH Disability Services Archivist. Ask me about rights, accommodations, "
                  "assistive products, independent living, and accessibility."),
    "greet_sig": ("I am the JAH Signature Disability Services Creator. Ask me about Signature-built "
                  "accessibility and accommodation systems."),
    "gen_blurb": ("Generate clearly-labeled disability service studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded disability service records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced."),
    "demo_kind": "disability-demo",
    "demo_title": "Disability Services Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Disability Services Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "audit":
        return fill(
            "items = @@ITEMS@@\n"
            "passed = [i for i in items if i['ok']]\n"
            "failed = [i for i in items if not i['ok']]\n"
            "print('Accessibility checklist: %d items' % len(items))\n"
            "print('Passed: %d  Failed: %d' % (len(passed), len(failed)))\n"
            "for i in failed:\n"
            "    print(' FIX:', i['item'])\n",
            {"ITEMS": p["items"]})
    if v == "accommodate":
        return fill(
            "need = @@NEED@@\noptions = @@OPTS@@\n"
            "print('Accommodation need:', need)\n"
            "for o in options:\n"
            "    fit = 'YES' if need in o['covers'] else 'no'\n"
            "    print(' [%s] %s — %s' % (fit, o['option'], o['note']))\n",
            {"NEED": p["need"], "OPTS": p["options"]})
    if v == "compare":
        return fill(
            "devices = @@DEVS@@\n"
            "ranked = sorted(devices, key=lambda d: d['score'], reverse=True)\n"
            "print('Assistive product comparison (score out of 10):')\n"
            "for d in ranked:\n"
            "    print(' %s: %d/10 — %s' % (d['name'], d['score'], d['note']))\n",
            {"DEVS": p["devices"]})
    if v == "plan":
        return fill(
            "goals = @@GOALS@@\n"
            "print('Person-centered plan goals:')\n"
            "for i, g in enumerate(goals, 1):\n"
            "    print(' %d. %s (support: %s)' % (i, g['goal'], g['support']))\n"
            "print('Total goals:', len(goals))\n",
            {"GOALS": p["goals"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d' % (pre, post, delta))\n"
            "print('Direction:', 'improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged')\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Disability Services Are", tier=F,
 desc_pub=("Disability services are supports that help people with disabilities live, learn, work, "
  "and participate fully in community life. They include personal assistance, assistive technology, "
  "accommodation services, independent living supports, employment services, transportation, and "
  "advocacy. Services are delivered by public agencies, centers for independent living, nonprofits, "
  "schools, employers, and health systems.\n"
  "The field is anchored in the independent living philosophy: people with disabilities are the "
  "experts on their own lives, and services should maximize choice and control. The person directs; "
  "the system supports."),
 desc_sig=("The Signature system models disability services as a control-transfer architecture: "
  "every service is designed to maximize the person's decision-making power, with supports that "
  "can be dialed up or down as needs change - assistance that adapts to the person, never the "
  "reverse."),
 how_pub=("A person identifies a barrier - at work, school, home, or in the community - and "
  "contacts a service provider. An assessment clarifies functional needs and preferences; a plan "
  "is built around the person's goals. Services are arranged - devices, personal assistance, "
  "accommodations - and reviewed regularly as needs evolve."),
 how_sig=("Signature planning tools put the person in the designer seat: interactive catalogs of "
  "supports with plain-language trade-offs, so plans reflect informed choice."),
 keys=["Supports for living, learning, working, participating",
  "Include personal assistance, assistive tech, accommodations, employment, transport",
  "Independent living philosophy: the person directs",
  "Maximize choice and control",
  "Delivered by agencies, independent living centers, schools, employers",
  "Plans evolve as needs change"],
 reqs=["Person-directed planning process",
  "Knowledge of rights and available supports",
  "Accessible communication throughout"],
 stds=["Independent living philosophy standards (public)",
  "State and federal service program rules"],
 cites=["National Council on Independent Living — public resources (public)",
  "Administration for Community Living — disability resources (public)"],
 demo=("plan", {"goals": [
   {"goal": "Use public transit independently", "support": "travel training"},
   {"goal": "Work part-time", "support": "job coach, schedule accommodation"},
   {"goal": "Manage personal care routine", "support": "personal assistant, 2 hrs/day"}]})),

dict(title="Models of Disability", tier=F,
 desc_pub=("How society understands disability shapes every service. The medical model locates the "
  "'problem' in the individual's body or mind and seeks to fix or cure it. The social model locates "
  "the problem in barriers - stairs, attitudes, inflexible systems - and seeks to remove them. The "
  "biopsychosocial model integrates both: health conditions interact with environments to produce "
  "disability.\n"
  "Modern services lean on the social model: ramps, captions, flexible work, and plain language "
  "remove barriers for everyone. Understanding the models helps workers choose interventions that "
  "empower rather than pathologize."),
 desc_sig=("Signature service design is explicitly social-model-first: every proposed intervention "
  "is scored on whether it removes an environmental barrier or merely works around one, "
  "prioritizing barrier removal."),
 how_pub=("Workers learn the models in training and apply them in assessment: alongside clinical "
  "facts, they inventory environmental barriers - physical, communication, attitudinal, policy. "
  "Service plans target barrier removal first, individual supports second, and measure participation "
  "outcomes, not just clinical change."),
 how_sig=("Signature barrier inventories are structured checklists per setting, so no assessment "
  "misses the environment's role."),
 keys=["Medical model: fix the individual",
  "Social model: remove the barriers",
  "Biopsychosocial model: integrate both",
  "Modern services lean social-model",
  "Barrier removal empowers; pathologizing disempowers",
  "Measure participation, not just clinical change"],
 reqs=["Training in disability models for all staff",
  "Barrier-inventory tools per setting",
  "Participation-focused outcome measures"],
 stds=["UN Convention on the Rights of Persons with Disabilities principles (public)",
  "Independent living philosophy (public)"],
 cites=["United Nations — Convention on the Rights of Persons with Disabilities (public)",
  "World Health Organization — ICF framework (public)"],
 demo=("audit", {"items": [
   {"item": "Entrance has step-free route", "ok": True},
   {"item": "Videos have captions", "ok": False},
   {"item": "Forms available in plain language", "ok": False},
   {"item": "Staff trained in disability etiquette", "ok": True}]})),

dict(title="Disability Rights and the ADA", tier=F,
 desc_pub=("The Americans with Disabilities Act (ADA) is the landmark U.S. civil rights law "
  "prohibiting discrimination against people with disabilities in employment (Title I), public "
  "services (Title II), public accommodations (Title III), and telecommunications (Title IV). It "
  "requires reasonable accommodations, accessible new construction, and removal of barriers where "
  "readily achievable.\n"
  "Companion laws strengthen the framework: Section 504 covers federally funded programs, the Fair "
  "Housing Act covers housing, and the Individuals with Disabilities Education Act covers schooling. "
  "Knowing these rights is the foundation of self-advocacy."),
 desc_sig=("Signature rights education turns legal protections into actionable playbooks: for each "
  "right, the steps to assert it, the evidence to gather, and where to complain - so rights become "
  "usable, not just theoretical."),
 how_pub=("When discrimination occurs, the person documents what happened, requests accommodation or "
  "remediation in writing, and - if refused - files complaints with the relevant agency (EEOC for "
  "employment, DOJ for public accommodations) or seeks legal aid. Disability rights organizations "
  "provide advocacy support throughout."),
 how_sig=("Signature complaint playbooks walk people through documentation, deadlines, and filing "
  "for each enforcement route."),
 keys=["ADA Titles I-IV: employment, public services, accommodations, telecom",
  "Requires reasonable accommodations and accessible construction",
  "Section 504, Fair Housing Act, IDEA extend protections",
  "Rights are the foundation of self-advocacy",
  "Enforcement via EEOC, DOJ, and legal aid",
  "Document everything in writing"],
 reqs=["Knowledge of applicable titles and companion laws",
  "Written accommodation-request templates",
  "Links to enforcement agencies and legal aid"],
 stds=["Americans with Disabilities Act (public law)",
  "Section 504, Fair Housing Act, IDEA (public laws)"],
 cites=["U.S. Dept. of Justice — ADA guidance (public)",
  "U.S. Equal Employment Opportunity Commission — disability guidance (public)"],
 demo=("accommodate", {"need": "wheelchair access to a public meeting",
   "options": [{"option": "Portable ramp at entrance", "covers": ["wheelchair access to a public meeting"], "note": "readily achievable"},
               {"option": "Relocate meeting to accessible room", "covers": ["wheelchair access to a public meeting"], "note": "simplest fix"},
               {"option": "Provide meeting notes afterward", "covers": [], "note": "not equal access"}]})),

dict(title="Accessibility Basics", tier=F,
 desc_pub=("Accessibility means designing environments, products, and communications that everyone "
  "can use. Physical accessibility covers step-free routes, door widths, reachable controls, and "
  "accessible restrooms. Communication accessibility covers captions, sign language interpretation, "
  "plain language, and alternative formats like braille or large print. Digital accessibility covers "
  "websites and apps usable with screen readers and keyboards.\n"
  "The curb-cut effect: accessibility features help everyone - captions help language learners, "
  "ramps help delivery workers. Accessibility is universal good design, not special treatment."),
 desc_sig=("Signature accessibility practice treats every project as born-accessible: checklists "
  "integrated into design reviews rather than audits after the fact - so accessibility is a design "
  "input, not a retrofit."),
 how_pub=("Organizations audit their facilities, communications, and digital products against "
  "accessibility standards, prioritize fixes by impact and feasibility, and build accessibility into "
  "procurement and design processes. People with disabilities test and validate the fixes - nothing "
  "about us without us."),
 how_sig=("Signature born-accessible checklists gate project milestones: designs cannot advance "
  "with known barriers unaddressed."),
 keys=["Physical, communication, and digital accessibility",
  "Curb-cut effect: helps everyone",
  "Audit, prioritize, fix, build into processes",
  "People with disabilities validate fixes",
  "Accessibility is universal good design",
  "Procurement is a leverage point"],
 reqs=["Accessibility audit tools and standards",
  "User testing by people with disabilities",
  "Procurement language requiring accessibility"],
 stds=["ADA Standards for Accessible Design (public)",
  "Web Content Accessibility Guidelines WCAG (public)"],
 cites=["U.S. Access Board — accessibility standards (public)",
  "W3C — Web Content Accessibility Guidelines (public)"],
 demo=("audit", {"items": [
   {"item": "Website keyboard navigable", "ok": False},
   {"item": "Images have alt text", "ok": True},
   {"item": "Color contrast meets 4.5:1", "ok": False},
   {"item": "Forms have labels", "ok": True},
   {"item": "Videos captioned", "ok": False}]})),

dict(title="Assistive Products Overview", tier=F,
 desc_pub=("Assistive products (assistive technology) are devices and software that maintain or "
  "improve functioning: wheelchairs and mobility aids, hearing aids and cochlear implants, screen "
  "readers and magnifiers, augmentative communication devices, adapted computer inputs, and daily-"
  "living aids. The right product, properly fitted and trained, transforms independence.\n"
  "Selection follows assessment: a professional evaluates functional needs, trials options, and "
  "fits the chosen product, with training for the user and supporters. Funding comes from insurance, "
  "vocational rehabilitation, schools, and grant programs - and abandonment usually traces to poor "
  "fit or no training, not to the device itself."),
 desc_sig=("Signature assistive-product matching pairs functional profiles against a structured "
  "product catalog with trial-outcome data, so recommendations start from what worked for similar "
  "needs."),
 how_pub=("Assessment identifies functional goals; trials compare candidate products in real "
  "tasks; the chosen product is fitted and the user trained. Funding applications cite the "
  "assessment. Follow-up checks fit, function, and satisfaction - adjusting or replacing as needs "
  "change."),
 how_sig=("Signature trial-outcome data shows which products succeeded for similar profiles, "
  "sharpening recommendations."),
 keys=["Devices and software that improve functioning",
  "Categories: mobility, hearing, vision, communication, computer access, daily living",
  "Assessment, trial, fitting, training",
  "Funding: insurance, voc rehab, schools, grants",
  "Abandonment usually means poor fit or no training",
  "Follow-up keeps products working"],
 reqs=["Qualified assessors per product category",
  "Trial equipment inventory",
  "Training and follow-up capacity"],
 stds=["Assistive Technology Act program standards (public)",
  "RESNA practice standards (public)"],
 cites=["National Institute on Disability research — assistive technology (public)",
  "RESNA — assistive technology standards (public)"],
 demo=("compare", {"devices": [
   {"name": "Screen reader A", "score": 9, "note": "strong app support"},
   {"name": "Screen reader B", "score": 7, "note": "lower cost"},
   {"name": "Magnifier C", "score": 6, "note": "for partial vision"}]})),

dict(title="Independent Living Philosophy", tier=F,
 desc_pub=("The independent living philosophy, born from the disability rights movement, holds that "
  "people with disabilities should control their own lives with the supports they choose. "
  "Independent living does not mean doing everything alone - it means self-direction: choosing "
  "where to live, who assists, and how days are structured.\n"
  "Centers for Independent Living (CILs), run by and for people with disabilities, deliver the "
  "core services: information and referral, independent living skills training, peer counseling, "
  "individual and systems advocacy, and transition support."),
 desc_sig=("Signature independent-living systems are built as control panels for the person: every "
  "support - scheduling, staffing, budgeting - is adjustable by the individual, with the system "
  "adapting to their direction."),
 how_pub=("A person contacts a CIL, meets a peer counselor or independent living specialist, and "
  "sets self-directed goals. The center provides skills training, peer support, and advocacy help; "
  "systems advocacy tackles the barriers the individual cannot remove alone. Progress is the "
  "person's own measure of control over their life."),
 how_sig=("Signature control panels give individuals direct management of their support "
  "arrangements with transparent options."),
 keys=["Self-direction, not doing everything alone",
  "People with disabilities control their own lives",
  "CILs run by and for people with disabilities",
  "Core services: info, skills, peer counseling, advocacy, transition",
  "Individual and systems advocacy together",
  "Progress measured by the person's own sense of control"],
 reqs=["Consumer-controlled governance (51%+ of board/staff)",
  "Peer counseling capacity",
  "Systems-advocacy agenda"],
 stds=["Rehabilitation Act independent living standards (public)",
  "National Council on Independent Living standards (public)"],
 cites=["National Council on Independent Living — public resources (public)",
  "Administration for Community Living — independent living (public)"],
 demo=("plan", {"goals": [
   {"goal": "Hire and direct personal assistants", "support": "employer-skills training"},
   {"goal": "Move to accessible apartment", "support": "housing search assistance"},
   {"goal": "Join community board", "support": "advocacy mentoring"}]})),

dict(title="Eligibility for Support Services", tier=F,
 desc_pub=("Support-service eligibility varies by program: Social Security disability benefits use "
  "strict medical-vocational criteria; Medicaid waiver programs use functional-need and financial "
  "criteria; vocational rehabilitation serves people whose disability is an impediment to "
  "employment; schools serve students whose disability affects learning under IDEA or Section 504.\n"
  "Applications require documentation - medical records, functional assessments, financial proof. "
  "Denials are common and appealable; many people win on appeal with better documentation or "
  "representation. Workers help assemble complete applications the first time."),
 desc_sig=("Signature eligibility mapping shows every program's criteria side by side against the "
  "person's profile, revealing the full set of options instead of one program at a time."),
 how_pub=("The worker identifies all potentially relevant programs, explains each one's criteria in "
  "plain language, and helps gather documentation. Applications are submitted complete; denials "
  "trigger review of appeal rights and deadlines. Approved services are coordinated into the "
  "person's plan."),
 how_sig=("Signature side-by-side criteria views prevent the common failure of pursuing one "
  "program while missing a better fit."),
 keys=["Criteria vary: medical-vocational, functional, financial, educational",
  "Key programs: SSDI/SSI, Medicaid waivers, voc rehab, IDEA/504",
  "Documentation decides outcomes",
  "Denials are common and appealable",
  "Complete first applications win more often",
  "Appeals often succeed with better evidence"],
 reqs=["Current criteria references per program",
  "Documentation checklists",
  "Appeals assistance"],
 stds=["Social Security disability determination rules (public)",
  "State waiver and voc rehab policies (public)"],
 cites=["Social Security Administration — disability programs (public)",
  "Centers for Medicare and Medicaid Services — waiver guidance (public)"],
 demo=("accommodate", {"need": "funding for a power wheelchair",
   "options": [{"option": "Medicaid DME coverage", "covers": ["funding for a power wheelchair"], "note": "with medical necessity"},
               {"option": "Voc rehab (employment-related)", "covers": ["funding for a power wheelchair"], "note": "if needed for work"},
               {"option": "Private fundraiser", "covers": [], "note": "last resort"}]})),

dict(title="Person-Centered Planning", tier=F,
 desc_pub=("Person-centered planning builds a life plan around the person's dreams, preferences, and "
  "strengths - not around available program slots. Tools like PATH, MAPS, and Essential Lifestyle "
  "Planning structure conversations where the person, family, friends, and allies envision a good "
  "life and work backward to the supports needed.\n"
  "The plan belongs to the person: it is written in their words, reviewed on their schedule, and "
  "changed when their vision changes. Services then flex to the plan, not the reverse."),
 desc_sig=("Signature person-centered planning uses living documents the person edits directly, "
  "with supporters contributing - so the plan is always current and always theirs."),
 how_pub=("A facilitator convenes the person's circle for a structured envisioning session. Dreams "
  "are captured, then translated into goals with concrete supports, responsible people, and "
  "timelines. The circle reconvenes regularly to celebrate progress and adjust. The person's words "
  "lead every page."),
 how_sig=("Signature living plans notify the circle when goals advance or stall, keeping support "
  "responsive between meetings."),
 keys=["Built around dreams, preferences, strengths",
  "Tools: PATH, MAPS, Essential Lifestyle Planning",
  "The person, family, friends, allies envision together",
  "Written in the person's words",
  "Services flex to the plan",
  "Reviewed on the person's schedule"],
 reqs=["Trained facilitators",
  "The person's chosen circle",
  "Authority to flex services to the plan"],
 stds=["Person-centered planning practice standards (public literature)",
  "HCBS settings-rule person-centered requirements (public regulation)"],
 cites=["Centers for Medicare and Medicaid Services — person-centered planning (public)",
  "National Center on Advancing Person-Centered Practices — resources (public)"],
 demo=("plan", {"goals": [
   {"goal": "Host monthly dinner for friends", "support": "cooking assistance, accessible kitchen"},
   {"goal": "Learn photography", "support": "adapted camera, community class"},
   {"goal": "Vote independently", "support": "accessible voting information"}]})),

dict(title="Communication Access", tier=F,
 desc_pub=("Communication access ensures everyone can send and receive information: sign language "
  "interpreters and captioning for Deaf and hard-of-hearing people, augmentative and alternative "
  "communication (AAC) devices for people with speech disabilities, plain language and easy-read "
  "formats for cognitive accessibility, and braille, large print, and screen-reader-compatible "
  "documents for blind and low-vision people.\n"
  "Effective communication is a legal requirement in health care, government, and many services - "
  "and a practical one everywhere: appointments fail when instructions cannot be understood."),
 desc_sig=("Signature communication access profiles record each person's preferred methods once, "
  "then propagate them to every service interaction automatically - so access follows the person."),
 how_pub=("Providers ask each person their preferred communication method and document it. "
  "Interpreters or captioners are booked for appointments; AAC users' devices are accommodated in "
  "every setting; documents are produced in needed formats. Staff are trained to communicate "
  "directly with the person, not around them."),
 how_sig=("Signature preference profiles auto-attach to appointments and referrals, so providers "
  "arrive prepared."),
 keys=["Interpreters, captioning, AAC, plain language, braille, large print",
  "Ask and document each person's preference",
  "Legal requirement in health care and government",
  "Communicate with the person, not around them",
  "Appointments fail without understanding",
  "Preferences should follow the person across services"],
 reqs=["Interpreter and captioning booking capacity",
  "Alternative-format production",
  "Staff communication training"],
 stds=["ADA effective-communication requirements (public)",
  "Section 508 communication standards (public)"],
 cites=["U.S. Dept. of Justice — effective communication (public)",
  "National Association of the Deaf — public resources (public)"],
 demo=("accommodate", {"need": "understand a doctor's instructions (Deaf patient)",
   "options": [{"option": "ASL interpreter in person", "covers": ["understand a doctor's instructions (Deaf patient)"], "note": "preferred by patient"},
               {"option": "Live captioning", "covers": ["understand a doctor's instructions (Deaf patient)"], "note": "backup option"},
               {"option": "Written notes only", "covers": [], "note": "insufficient for complex care"}]})),

dict(title="Reasonable Accommodations at Work", tier=F,
 desc_pub=("Reasonable accommodations are changes that let qualified workers with disabilities do "
  "their jobs: modified schedules, assistive technology, adjusted duties, accessible workspaces, "
  "remote work, or reassignment to a vacant position. Employers must provide them unless doing so "
  "causes undue hardship.\n"
  "The interactive process - employer and employee discussing what works - is the legal and "
  "practical core. Most accommodations cost little or nothing; the Job Accommodation Network (JAN) "
  "provides free expert guidance."),
 desc_sig=("Signature accommodation design treats the interactive process as a structured "
  "collaboration with a solution library, so good ideas from past cases inform new ones."),
 how_pub=("The employee discloses the need and suggests accommodations (no magic words required). "
  "Employer and employee discuss options - often with JAN or medical input - and implement the "
  "effective, reasonable choice. Effectiveness is reviewed; adjustments follow if the first try "
  "falls short."),
 how_sig=("Signature solution libraries surface accommodations that worked for similar job-need "
  "pairs, speeding the interactive process."),
 keys=["Changes enabling qualified workers to do their jobs",
  "Examples: schedules, tech, duties, workspace, remote work",
  "Required unless undue hardship",
  "Interactive process is the core",
  "Most accommodations cost little or nothing",
  "JAN provides free expert guidance"],
 reqs=["Interactive-process procedure",
  "Documentation of needs and solutions tried",
  "Knowledge of JAN resources"],
 stds=["ADA Title I reasonable-accommodation rules (public)",
  "EEOC enforcement guidance (public)"],
 cites=["U.S. Equal Employment Opportunity Commission — accommodations guidance (public)",
  "Job Accommodation Network — public resources (public)"],
 demo=("accommodate", {"need": "screen reader for data-entry job",
   "options": [{"option": "Install screen reader + training", "covers": ["screen reader for data-entry job"], "note": "effective, low cost"},
               {"option": "Reassign data entry to coworker", "covers": [], "note": "not reasonable if core duty"},
               {"option": "Provide large monitor", "covers": [], "note": "does not address need"}]})),

dict(title="Reasonable Accommodations in School", tier=F,
 desc_pub=("Students with disabilities get accommodations through two main routes: IEPs (Individualized "
  "Education Programs) under IDEA, providing specialized instruction and related services; and 504 "
  "plans under Section 504, providing accommodations for equal access. Common accommodations include "
  "extended time, assistive technology, note-takers, accessible materials, and modified "
  "presentation of content.\n"
  "Parents are partners with specific rights: to participate in meetings, to consent to evaluation, "
  "and to dispute decisions through mediation or due process. Early identification changes "
  "trajectories."),
 desc_sig=("Signature school-accommodation systems track each student's plan, service minutes, and "
  "progress in one view shared appropriately with teachers - so plans live in classrooms, not in "
  "filing cabinets."),
 how_pub=("Concerns trigger evaluation (with parent consent), assessing all suspected areas of "
  "disability. The team - parents, teachers, specialists - determines eligibility and writes the "
  "IEP or 504 plan with measurable goals and specified services. Progress is reviewed at least "
  "yearly; parents can request review anytime."),
 how_sig=("Signature plan dashboards show service delivery against the written plan, flagging gaps "
  "before annual reviews."),
 keys=["IEPs: specialized instruction under IDEA",
  "504 plans: access accommodations under Section 504",
  "Common: extended time, tech, note-takers, accessible materials",
  "Parents are partners with defined rights",
  "Evaluation requires parent consent",
  "Early identification changes trajectories"],
 reqs=["Child-find and evaluation procedures",
  "Team including parents and specialists",
  "Progress-monitoring systems"],
 stds=["Individuals with Disabilities Education Act (public law)",
  "Section 504 regulations (public)"],
 cites=["U.S. Dept. of Education — IDEA and 504 guidance (public)",
  "National Center for Learning Disabilities — public resources (public)"],
 demo=("plan", {"goals": [
   {"goal": "Read grade-level text with text-to-speech", "support": "accessible materials, AT training"},
   {"goal": "Complete tests with extended time", "support": "separate setting"},
   {"goal": "Take notes independently", "support": "note-taking app, instruction"}]})),

# ---------------- Compounded (12) ----------------
dict(title="Mobility Aids and Devices", tier=C,
 desc_pub=("Mobility aids range from canes and crutches to manual and power wheelchairs, scooters, "
  "walkers, and standing frames. Selection depends on strength, endurance, environment (door "
  "widths, terrain, transport), and the user's goals - a power chair for campus distances, a "
  "lightweight manual for an active user with upper-body strength.\n"
  "Proper fitting prevents injury: seat width, depth, and height; wheel position; pressure-relief "
  "cushions for skin protection. Training covers transfers, terrain, maintenance, and - for power "
  "chairs - safe operation in crowds and traffic."),
 desc_sig=("Signature mobility matching simulates the user's key environments against candidate "
  "devices, recommending based on modeled fit rather than showroom impression."),
 how_pub=("A seating/mobility evaluation measures the user and their environments, trials candidate "
  "devices on real routes, and prescribes the best fit with justification for funding. Delivery "
  "includes fitting adjustments and skills training; follow-up addresses pressure, pain, or "
  "changing needs."),
 how_sig=("Signature environment modeling scores devices against the user's actual doorways, "
  "transit, and terrain."),
 keys=["Range: canes, walkers, manual/power chairs, scooters, standing frames",
  "Match device to strength, environment, and goals",
  "Proper fitting prevents injury",
  "Pressure-relief seating protects skin",
  "Training: transfers, terrain, maintenance, safety",
  "Follow-up as needs change"],
 reqs=["Seating and mobility evaluations",
  "Trial device inventory",
  "Fitting and training capacity"],
 stds=["RESNA wheelchair service standards (public)",
  "FDA device classifications (public)"],
 cites=["RESNA — seating and mobility standards (public)",
  "Paralyzed Veterans of America — public resources (public)"],
 demo=("compare", {"devices": [
   {"name": "Ultralight manual chair", "score": 9, "note": "active user, strong upper body"},
   {"name": "Power chair", "score": 8, "note": "long distances, limited endurance"},
   {"name": "Scooter", "score": 5, "note": "not for full-time use"}]})),

dict(title="Hearing Assistive Technology", tier=C,
 desc_pub=("Hearing assistive technology includes hearing aids (amplifying with sophisticated "
  "processing), cochlear implants (direct neural stimulation for severe loss), assistive listening "
  "systems (FM, loop, infrared for venues and classrooms), captioned telephones, and visual/vibrating "
  "alerting devices.\n"
  "Success requires audiologic fitting to the individual's loss pattern, realistic-expectation "
  "counseling, and follow-up tuning. Technology plus communication strategies - facing the speaker, "
  "reducing background noise - outperforms technology alone."),
 desc_sig=("Signature hearing-tech fitting pairs audiologic data with the person's key listening "
  "environments, prioritizing the situations that matter most to them."),
 how_pub=("An audiologist tests hearing, discusses options across the technology range, and fits "
  "the chosen devices with verification (real-ear measures). Counseling sets expectations; "
  "follow-ups fine-tune. Venue systems and alerting devices are added for specific environments."),
 how_sig=("Signature environment-priority fitting tunes first for the user's top listening "
  "situations."),
 keys=["Hearing aids, cochlear implants, assistive listening, captioned phones, alerting devices",
  "Fitting matched to the individual's loss pattern",
  "Verification with real-ear measures",
  "Counseling sets realistic expectations",
  "Technology plus communication strategies",
  "Follow-up tuning is essential"],
 reqs=["Audiologic evaluation and fitting",
  "Verification equipment",
  "Counseling and follow-up schedule"],
 stds=["FDA hearing-aid regulations (public)",
  "Audiology best-practice guidelines (public literature)"],
 cites=["National Institute on Deafness — public information (public)",
  "Hearing Loss Association of America — public resources (public)"],
 demo=("compare", {"devices": [
   {"name": "Receiver-in-canal aids", "score": 9, "note": "mild-moderate loss"},
   {"name": "Cochlear implant", "score": 8, "note": "severe-profound loss, candidacy required"},
   {"name": "Pocket amplifier", "score": 5, "note": "situational backup only"}]})),

dict(title="Vision Assistive Technology", tier=C,
 desc_pub=("Vision assistive technology spans screen readers (JAWS, NVDA, VoiceOver), screen "
  "magnifiers, braille displays and notetakers, OCR reading systems, video magnifiers (CCTVs), and "
  "smartphone apps for navigation and object recognition.\n"
  "Training determines success more than the device: efficient screen-reader use is a learned skill "
  "taking weeks of practice. Assessment matches technology to tasks - reading, navigation, "
  "employment - and to the person's residual vision and preferences."),
 desc_sig=("Signature vision-tech training uses task-based curricula with measurable milestones, so "
  "progress from novice to fluent user is visible and coached."),
 how_pub=("A vision rehabilitation assessment maps functional needs; trials compare technologies on "
  "the person's real tasks. Training proceeds task by task - email, documents, navigation - with "
  "practice assignments. Follow-up adds advanced skills and troubleshoots."),
 how_sig=("Signature milestone-tracked training shows both learner and coach exactly which skills "
  "are fluent and which need work."),
 keys=["Screen readers, magnifiers, braille, OCR, video magnifiers, apps",
  "Training matters more than the device",
  "Screen-reader fluency takes weeks of practice",
  "Match technology to real tasks",
  "Assessment considers residual vision and preferences",
  "Follow-up builds advanced skills"],
 reqs=["Vision rehabilitation assessments",
  "Trial technology inventory",
  "Structured training curricula"],
 stds=["Vision rehabilitation practice standards (public literature)",
  "Accessible technology procurement standards (public)"],
 cites=["American Foundation for the Blind — public resources (public)",
  "National Federation of the Blind — public resources (public)"],
 demo=("accommodate", {"need": "read work documents (blind employee)",
   "options": [{"option": "Screen reader + training", "covers": ["read work documents (blind employee)"], "note": "full access"},
               {"option": "Colleague reads aloud", "covers": [], "note": "not independent or private"},
               {"option": "Large print only", "covers": [], "note": "insufficient for no usable vision"}]})),

dict(title="Cognitive and Learning Supports", tier=C,
 desc_pub=("Cognitive supports help with memory, attention, organization, and processing: smart "
  "reminders and scheduling apps, task-breakdown tools, text-to-speech, speech-to-text, graphic "
  "organizers, and simplified interfaces. Learning supports add structured literacy and math "
  "interventions, multisensory instruction, and extended practice.\n"
  "The principle is externalizing load: move demands from fragile memory to reliable systems. "
  "Supports are chosen with the person through trials in real tasks - school, work, daily life."),
 desc_sig=("Signature cognitive-support design builds personal 'external brain' systems: reminders, "
  "checklists, and simplified workflows integrated into the person's devices and routines."),
 how_pub=("Assessment identifies which cognitive demands cause failure in real tasks. Candidate "
  "supports are trialed - an app for medication reminders, text-to-speech for reading load - and "
  "the effective ones are set up with training. Support fades or grows as needs change."),
 how_sig=("Signature routine integration embeds supports into existing habits rather than adding "
  "separate systems to remember."),
 keys=["Externalize load: move demands to reliable systems",
  "Reminders, task breakdown, text-to-speech, organizers",
  "Chosen through trials in real tasks",
  "Multisensory instruction for learning",
  "Integrate into existing routines",
  "Adjust as needs change"],
 reqs=["Cognitive-task assessment",
  "Trial supports in real contexts",
  "Training and routine-building"],
 stds=["Cognitive rehabilitation practice guidance (public literature)",
  "Special education evidence standards (public)"],
 cites=["National Center for Learning Disabilities — public resources (public)",
  "Brain Injury Association — public resources (public)"],
 demo=("compare", {"devices": [
   {"name": "Smart reminder system", "score": 9, "note": "medication and appointment adherence"},
   {"name": "Text-to-speech suite", "score": 8, "note": "reading load"},
   {"name": "Paper planner", "score": 5, "note": "fails without prompting"}]})),

dict(title="Home Modifications", tier=C,
 desc_pub=("Home modifications remove barriers where people live: ramps and stairlifts, widened "
  "doorways, roll-in showers, grab bars, lowered counters, accessible kitchens, smart-home controls "
  "for lights/locks/thermostats, and emergency alert systems.\n"
  "Good modifications start with an occupational therapy home assessment mapping the person's "
  "abilities against the home's demands, prioritize by safety impact, and respect that it is the "
  "person's home - aesthetics and preference matter alongside function. Funding blends Medicaid "
  "waivers, grants, and loans."),
 desc_sig=("Signature home-modification planning uses room-by-room barrier mapping with costed "
  "options, so families choose from transparent trade-offs instead of accepting a single "
  "contractor's plan."),
 how_pub=("An OT assesses the person and home, producing prioritized recommendations. The family "
  "selects options within budget and funding; licensed contractors perform the work; the OT "
  "verifies function after completion. Smart-home additions are configured and trained."),
 how_sig=("Signature costed option sets make the budget conversation concrete from the start."),
 keys=["Ramps, roll-in showers, grab bars, widened doors, smart controls",
  "Start with OT home assessment",
  "Prioritize by safety impact",
  "Respect aesthetics and preference",
  "Funding: waivers, grants, loans",
  "Verify function after completion"],
 reqs=["OT home assessments",
  "Licensed contractors experienced in accessibility",
  "Funding navigation"],
 stds=["ADA residential guidelines where applicable (public)",
  "State waiver home-modification rules"],
 cites=["National Association of Home Builders — accessibility resources (public)",
  "Administration for Community Living — home modification guidance (public)"],
 demo=("audit", {"items": [
   {"item": "Step-free entrance", "ok": False},
   {"item": "Grab bars in bathroom", "ok": True},
   {"item": "Doorways 32in+ clear", "ok": False},
   {"item": "Emergency alert system", "ok": True}]})),

dict(title="Personal Assistance Services", tier=C,
 desc_pub=("Personal assistance services (PAS) provide help with daily activities - bathing, "
  "dressing, eating, mobility, household tasks - so people with disabilities direct their own "
  "lives in the community. Models include agency-directed (the agency employs aides) and "
  "consumer-directed (the person hires, trains, and manages their own assistants).\n"
  "Consumer direction maximizes control and satisfaction; it requires employer-skills training and "
  "fiscal intermediary support for payroll and taxes. Workforce shortages make aide recruitment and "
  "retention a constant challenge."),
 desc_sig=("Signature PAS management gives consumer-directors scheduling, payroll, and backup-"
  "coverage tools in one place - professionalizing self-direction without surrendering control."),
 how_pub=("Assessment determines authorized hours; the person chooses agency or consumer-directed "
  "model. Consumer-directors recruit (often through registries), interview, hire, and train aides "
  "with program support; fiscal intermediaries handle payroll. Backup plans cover aide absences."),
 how_sig=("Signature backup-coverage pools match trained aides to shifts when regular staff are "
  "unavailable, addressing the field's fragility point."),
 keys=["Help with daily activities; person directs their life",
  "Agency-directed vs consumer-directed models",
  "Consumer direction maximizes control",
  "Requires employer skills + fiscal intermediary",
  "Workforce shortages are the chronic challenge",
  "Backup plans for aide absences are essential"],
 reqs=["Authorized service hours via assessment",
  "Fiscal intermediary for consumer-directed payroll",
  "Aide registries and backup systems"],
 stds=["State PAS program rules (public)",
  "HCBS settings requirements (public regulation)"],
 cites=["Centers for Medicare and Medicaid Services — PAS guidance (public)",
  "National Council on Independent Living — PAS resources (public)"],
 demo=("plan", {"goals": [
   {"goal": "Morning routine with aide", "support": "consumer-directed, 1.5 hrs"},
   {"goal": "Evening meal preparation", "support": "agency aide, 1 hr"},
   {"goal": "Weekend community outings", "support": "aide + accessible transport"}]})),

dict(title="Supported Decision-Making", tier=C,
 desc_pub=("Supported decision-making (SDM) is an alternative to guardianship: the person with a "
  "disability chooses trusted supporters who help them understand options and communicate "
  "decisions - while the person retains final authority. Formalized through written agreements, "
  "SDM is recognized in a growing number of states.\n"
  "SDM preserves rights that guardianship removes: to vote, marry, choose where to live. It suits "
  "many people for whom guardianship was once the default, and states increasingly require that "
  "less-restrictive alternatives be considered first."),
 desc_sig=("Signature SDM implementation provides agreement templates, supporter training, and "
  "decision-logging tools - making the alternative to guardianship practical, not just "
  "theoretical."),
 how_pub=("The person identifies supporters and the decisions they want help with. A written "
  "agreement - often using state-recognized forms - documents the arrangement and is shared with "
  "relevant third parties (banks, doctors). Supporters are trained in their role: explain, "
  "discuss, respect the person's choice."),
 how_sig=("Signature decision logs create a record of supported choices, demonstrating capacity "
  "in action."),
 keys=["Alternative to guardianship",
  "Person retains final decision authority",
  "Supporters help understand and communicate",
  "Formalized through written agreements",
  "Preserves rights guardianship removes",
  "States increasingly require considering it first"],
 reqs=["State-recognized agreement forms",
  "Supporter identification and training",
  "Third-party acceptance (banks, providers)"],
 stds=["State SDM statutes (public)",
  "National Resource Center for SDM guidance (public)"],
 cites=["American Bar Association — SDM resources (public)",
  "National Resource Center for Supported Decision-Making (public)"],
 demo=("plan", {"goals": [
   {"goal": "Understand medical options", "support": "sister as health supporter"},
   {"goal": "Manage monthly budget", "support": "friend as financial supporter"},
   {"goal": "Choose housing", "support": "peer counselor as housing supporter"}]})),

dict(title="Inclusive Education Services", tier=C,
 desc_pub=("Inclusive education means students with disabilities learn alongside peers in general "
  "education with the supports they need: co-teaching, paraprofessional support, assistive "
  "technology, differentiated instruction, and related services delivered in the classroom where "
  "possible. The legal anchor is the least restrictive environment (LRE) requirement.\n"
  "Inclusion benefits all students - academic and social outcomes improve with well-implemented "
  "models. Success requires teacher collaboration time, training, and administrative commitment, "
  "not just placement."),
 desc_sig=("Signature inclusion design schedules co-teaching, support, and collaboration time as "
  "one system, so inclusive classrooms are engineered rather than hoped for."),
 how_pub=("IEP teams place students in general education with specified supports to the maximum "
  "extent appropriate. Schools schedule co-teaching pairs, train staff in differentiation and AT, "
  "and monitor both academic progress and social participation. Placement is reviewed yearly with "
  "LRE justification documented."),
 how_sig=("Signature scheduling tools protect co-planning time - the resource inclusion most often "
  "lacks."),
 keys=["Learn alongside peers with needed supports",
  "Co-teaching, paras, AT, differentiation",
  "Legal anchor: least restrictive environment",
  "Benefits all students when well-implemented",
  "Requires collaboration time and training",
  "Monitor academics and social participation"],
 reqs=["Co-teaching partnerships and schedules",
  "AT and differentiation training",
  "LRE documentation in IEPs"],
 stds=["IDEA least-restrictive-environment requirements (public law)",
  "State inclusion guidance"],
 cites=["U.S. Dept. of Education — inclusion guidance (public)",
  "National Center on Inclusive Education — public resources (public)"],
 demo=("outcome", {"label": "Students in general education 80%+ of day", "pre": 52, "post": 78})),

dict(title="Employment Support Services", tier=C,
 desc_pub=("Employment supports help people with disabilities get and keep jobs: vocational "
  "rehabilitation (assessment, training, placement, AT), supported employment with job coaches, "
  "customized employment (carving roles around strengths), benefits counseling, and employer "
  "disability-awareness training.\n"
  "Customized employment deserves emphasis: instead of fitting the person to an existing job, "
  "negotiate a role around what they do well - unlocking employment for people with significant "
  "disabilities. The employment-first principle holds that everyone can work with the right "
  "supports."),
 desc_sig=("Signature employment design maintains talent profiles capturing strengths and support "
  "needs, matched against employer partners' unmet needs - a two-sided matching system for "
  "inclusive hiring."),
 how_pub=("Voc rehab or employment providers assess interests and abilities, develop a plan, and "
  "provide training or place directly with coaching. Job coaches fade as the worker stabilizes; "
  "benefits counselors ensure earnings work with needed supports. Employers get accommodation "
  "guidance."),
 how_sig=("Signature two-sided matching proposes role carves where candidate strengths meet "
  "employer gaps."),
 keys=["Voc rehab, supported employment, customized employment",
  "Customized employment carves roles around strengths",
  "Employment-first: everyone can work with right supports",
  "Job coaches fade as workers stabilize",
  "Benefits counseling protects needed supports",
  "Employer training opens doors"],
 reqs=["Voc rehab eligibility and planning",
  "Job-coach capacity",
  "Employer partnerships"],
 stds=["Rehabilitation Act employment provisions (public)",
  "Customized employment practice standards (public literature)"],
 cites=["U.S. Dept. of Labor — disability employment resources (public)",
  "Association of People Supporting Employment First — public resources (public)"],
 demo=("outcome", {"label": "Job seekers placed in competitive jobs", "pre": 34, "post": 66})),

dict(title="Transportation and Paratransit", tier=C,
 desc_pub=("Transportation is independence: without it, jobs, health care, and community life are "
  "out of reach. Options include accessible fixed-route transit, ADA paratransit (door-to-door "
  "service for those who cannot use fixed routes), volunteer driver programs, ride subsidies, and "
  "travel training teaching independent transit use.\n"
  "ADA paratransit is a civil right for eligible riders where fixed-route service exists - with "
  "known pain points: advance scheduling, long ride times, and service gaps. Travel training "
  "multiplies independence for those who can learn fixed routes."),
 desc_sig=("Signature transportation coordination blends paratransit, volunteer drivers, and "
  "subsidized rides into one trip-planning view, so riders get the best option per trip."),
 how_pub=("Riders apply for paratransit eligibility through functional assessment; approved riders "
  "book trips (often a day ahead). Travel trainers assess candidates and teach routes step by "
  "step until independent. Volunteer programs fill gaps paratransit misses."),
 how_sig=("Signature trip planners compare all available options per trip - time, cost, "
  "independence - in one view."),
 keys=["Transportation is independence",
  "Fixed-route, paratransit, volunteer drivers, subsidies, travel training",
  "ADA paratransit is a civil right for eligible riders",
  "Known pain points: advance booking, long rides, gaps",
  "Travel training multiplies independence",
  "Blend options per trip"],
 reqs=["Paratransit eligibility process",
  "Travel-training capacity",
  "Volunteer driver networks"],
 stds=["ADA transportation regulations (public)",
  "FTA paratransit requirements (public)"],
 cites=["Federal Transit Administration — ADA guidance (public)",
  "National Aging and Disability Transportation Center — public resources (public)"],
 demo=("accommodate", {"need": "get to work daily (cannot drive)",
   "options": [{"option": "Travel training + fixed route", "covers": ["get to work daily (cannot drive)"], "note": "most independent"},
               {"option": "ADA paratransit", "covers": ["get to work daily (cannot drive)"], "note": "book day ahead"},
               {"option": "Rely on coworkers", "covers": [], "note": "not reliable or dignified"}]})),

dict(title="Accessible Digital Design", tier=C,
 desc_pub=("Accessible digital design makes websites, apps, and documents usable by everyone, "
  "including people using screen readers, keyboards, voice control, or magnification. Core "
  "practices: semantic HTML, keyboard operability, sufficient contrast, text alternatives, "
  "captions, resizable text, and understandable error messages.\n"
  "The business case is strong: accessibility expands audience, improves SEO and usability for "
  "all, and reduces legal risk. Testing combines automated checks with manual testing by disabled "
  "users - automation alone catches only a fraction of barriers."),
 desc_sig=("Signature digital practice embeds accessibility gates in the development pipeline - "
  "automated checks plus scheduled user testing - so products ship accessible by default."),
 how_pub=("Teams adopt WCAG as the standard, train designers and developers, and integrate checks "
  "into code review. Manual audits and user testing with disabled testers validate; remediation "
  "backlogs are prioritized and tracked. Procurement requires accessibility conformance."),
 how_sig=("Signature pipeline gates block releases with new critical barriers, making "
  "accessibility a shipping requirement."),
 keys=["Semantic HTML, keyboard access, contrast, alt text, captions",
  "Benefits everyone; expands audience; reduces legal risk",
  "Automation catches a fraction - manual testing essential",
  "Test with disabled users",
  "WCAG is the global standard",
  "Procurement requires conformance"],
 reqs=["WCAG-based standards adoption",
  "Developer and designer training",
  "User-testing panel of disabled testers"],
 stds=["WCAG 2.1/2.2 (public)",
  "Section 508 standards (public)"],
 cites=["W3C — WCAG (public)",
  "U.S. Access Board — Section 508 (public)"],
 demo=("audit", {"items": [
   {"item": "All interactive elements keyboard reachable", "ok": False},
   {"item": "Skip navigation link present", "ok": True},
   {"item": "Error messages programmatically associated", "ok": False},
   {"item": "Touch targets 24px minimum", "ok": True}]})),

dict(title="Service Animals and Their Access Rights", tier=C,
 desc_pub=("Service animals - dogs individually trained to perform tasks for people with "
  "disabilities - have broad public-access rights under the ADA: restaurants, stores, transit, and "
  "other public places must admit them. Emotional support animals, while valuable, do not have the "
  "same public-access rights (housing and air-travel rules differ).\n"
  "Businesses may ask only two questions: is this a service animal required because of a "
  "disability, and what task is it trained to perform. No vests, IDs, or demonstrations can be "
  "required. Task training - guiding, alerting, retrieving, interrupting - is what defines the "
  "role."),
 desc_sig=("Signature public-education materials give businesses the two-question rule and task "
  "examples in plain language, reducing confrontations born of confusion."),
 how_pub=("Handlers train (or obtain trained) dogs for specific tasks related to their disability. "
  "When access is challenged, handlers state their rights calmly; advocacy organizations intervene "
  "in disputes. Businesses train staff on the two questions and on not distracting working dogs."),
 how_sig=("Signature business guides put the legal standard on one page for staff training."),
 keys=["Service dogs: trained tasks, broad public-access rights",
  "Emotional support animals: different, narrower rights",
  "Businesses may ask only two questions",
  "No vests, IDs, or demos can be required",
  "Task training defines the role",
  "Housing and travel have their own rules"],
 reqs=["Task training matched to disability",
  "Handler knowledge of access rights",
  "Business staff training"],
 stds=["ADA service-animal regulations (public)",
  "Fair Housing Act assistance-animal guidance (public)"],
 cites=["U.S. Dept. of Justice — service animal guidance (public)",
  "U.S. Dept. of Housing and Urban Development — assistance animals (public)"],
 demo=("accommodate", {"need": "bring service dog into grocery store",
   "options": [{"option": "Admit the service dog", "covers": ["bring service dog into grocery store"], "note": "ADA right"},
               {"option": "Ask the two questions", "covers": ["bring service dog into grocery store"], "note": "allowed verification"},
               {"option": "Demand papers or vest", "covers": [], "note": "not permitted"}]})),

# ---------------- Advanced (11) ----------------
dict(title="Accessibility Auditing Methods", tier=A,
 desc_pub=("Accessibility auditing systematically evaluates facilities, programs, and digital "
  "products against standards. Facility audits measure routes, doors, restrooms, and signage "
  "against ADA standards. Program audits review policies and practices. Digital audits combine "
  "automated scans, manual WCAG evaluation, and user testing.\n"
  "Professional audits produce prioritized remediation plans with cost estimates - the bridge "
  "between 'we should be accessible' and budgeted action. Re-audits verify fixes."),
 desc_sig=("Signature auditing standardizes findings into a scored barrier inventory with "
  "costed remediation, so decision-makers see accessibility as a managed program, not a vague "
  "obligation."),
 how_pub=("Auditors define scope and standards, then evaluate methodically - measuring, testing, "
  "interviewing users. Findings are scored by severity and mapped to remediation actions with "
  "estimates. Reports go to leadership with a proposed timeline; re-audits confirm completion."),
 how_sig=("Signature scored inventories let organizations track accessibility debt like financial "
  "debt - visible, prioritized, shrinking."),
 keys=["Facility, program, and digital audits",
  "Measure against ADA standards and WCAG",
  "Combine automation, manual review, user testing",
  "Produce prioritized, costed remediation plans",
  "Re-audits verify fixes",
  "Bridge from intention to budgeted action"],
 reqs=["Trained auditors per domain",
  "Measurement and testing tools",
  "Leadership commitment to remediate"],
 stds=["ADA Standards for Accessible Design (public)",
  "WCAG evaluation methodology (public)"],
 cites=["U.S. Access Board — standards (public)",
  "W3C — evaluation resources (public)"],
 demo=("audit", {"items": [
   {"item": "Main entrance accessible route", "ok": True},
   {"item": "Service counters at accessible height", "ok": False},
   {"item": "Signage with braille and raised characters", "ok": False},
   {"item": "Emergency alarms visual + audible", "ok": True},
   {"item": "Website conformance claim published", "ok": False}]})),

dict(title="Universal Design in Practice", tier=A,
 desc_pub=("Universal design creates environments and products usable by all people without "
  "adaptation: entrances everyone uses, controls everyone can operate, information everyone can "
  "perceive. Its seven principles - equitable use, flexibility, simple intuitive use, perceptible "
  "information, error tolerance, low physical effort, appropriate size and space - guide design "
  "decisions.\n"
  "Universal design differs from accessibility retrofits: it starts from human diversity rather "
  "than adding accommodations later. The result serves aging populations, injured athletes, parents "
  "with strollers - everyone, at every life stage."),
 desc_sig=("Signature universal-design review scores concepts against the seven principles before "
  "detailed design begins, catching exclusion at the cheapest moment to fix it."),
 how_pub=("Design teams learn the principles, involve diverse users from concept stage, and "
  "evaluate prototypes against each principle. Decisions favor solutions serving the widest range; "
  "where trade-offs exist, they are documented with rationale. Post-occupancy evaluation confirms "
  "real-world usability."),
 how_sig=("Signature principle scoring at concept review prevents expensive late-stage "
  "accessibility failures."),
 keys=["Usable by all without adaptation",
  "Seven principles guide decisions",
  "Starts from human diversity, not retrofits",
  "Serves everyone across life stages",
  "Involve diverse users from concept stage",
  "Post-occupancy evaluation confirms usability"],
 reqs=["Design-team training in the principles",
  "Diverse user involvement from concept",
  "Evaluation against principles at reviews"],
 stds=["The Seven Principles of Universal Design (public)",
  "Related ISO usability guidance (public)"],
 cites=["Centre for Excellence in Universal Design — principles (public)",
  "U.S. Access Board — design guidance (public)"],
 demo=("audit", {"items": [
   {"item": "One entrance serves everyone", "ok": True},
   {"item": "Information in visual + tactile + audio", "ok": False},
   {"item": "Controls operable with one hand", "ok": True}]})),

dict(title="Emergency Preparedness for People with Disabilities", tier=A,
 desc_pub=("Emergencies disproportionately harm people with disabilities: warnings that cannot be "
  "heard or seen, evacuation routes that cannot be used, shelters that cannot be entered, "
  "equipment left behind. Inclusive preparedness means accessible alerts, evacuation assistance "
  "registries (voluntary), accessible shelters, and power contingency for device users.\n"
  "Personal preparedness - go-bags with medications, device chargers, communication cards - pairs "
  "with system preparedness. People with disabilities must be at the planning table, not an "
  "afterthought in the plan."),
 desc_sig=("Signature emergency planning maintains living functional-needs registries linked to "
  "alert and evacuation systems, so inclusive response is operational, not aspirational."),
 how_pub=("Emergency managers partner with disability organizations to map needs, make alerts "
  "multi-modal, designate accessible shelters, and train responders. Individuals build personal "
  "plans with support networks. Exercises include disability scenarios; after-action reviews "
  "measure inclusive performance."),
 how_sig=("Signature registry-linked alerting targets accessible warnings and assistance to "
  "those who need them."),
 keys=["Disproportionate harm without inclusive planning",
  "Accessible alerts, evacuation help, accessible shelters",
  "Power contingency for device users",
  "Personal go-bags plus system readiness",
  "Disabled people at the planning table",
  "Exercise disability scenarios"],
 reqs=["Disability organization partnerships",
  "Multi-modal alert systems",
  "Accessible shelter designations"],
 stds=["FEMA inclusive preparedness guidance (public)",
  "ADA emergency-management obligations (public)"],
 cites=["Federal Emergency Management Agency — inclusive preparedness (public)",
  "National Council on Independent Living — emergency resources (public)"],
 demo=("plan", {"goals": [
   {"goal": "Receive warnings in accessible format", "support": "multi-modal alert enrollment"},
   {"goal": "Evacuate with power chair", "support": "accessible transport plan"},
   {"goal": "72-hour independent survival", "support": "go-bag, backup power"}]})),

dict(title="Transition Services: School to Adult Life", tier=A,
 desc_pub=("Transition services bridge school to adult life for youth with disabilities: employment, "
  "postsecondary education, independent living, and community participation. IDEA requires "
  "transition planning in IEPs starting by age 16, with measurable postsecondary goals.\n"
  "Effective transition starts early, involves the youth as leader, connects to adult services "
  "(voc rehab, independent living centers) before exit, and includes real work experience during "
  "school - the strongest predictor of post-school employment."),
 desc_sig=("Signature transition management runs a countdown dashboard from age 14: milestones for "
  "work experience, adult-service connections, and benefits planning, so no youth exits to "
  "nothing."),
 how_pub=("IEP teams write transition goals with the youth leading; schools arrange work-based "
  "learning and connect to voc rehab and CILs junior year. Benefits counseling addresses the "
  "benefits-employment puzzle. Adult providers attend the final IEPs; warm handoffs replace "
  "graduation cliffs."),
 how_sig=("Signature countdown dashboards make every milestone visible to youth, family, and "
  "providers years in advance."),
 keys=["Bridge school to employment, education, independent living",
  "IDEA requires planning by age 16",
  "Youth leads their own transition",
  "Connect to adult services before exit",
  "Real work experience predicts employment",
  "Warm handoffs replace graduation cliffs"],
 reqs=["Transition-focused IEP practices",
  "Work-based learning placements",
  "Adult-service partnerships"],
 stds=["IDEA transition requirements (public law)",
  "State transition practice guidance"],
 cites=["U.S. Dept. of Education — transition guidance (public)",
  "National Technical Assistance Center on Transition — public resources (public)"],
 demo=("outcome", {"label": "Youth employed or in education one year out", "pre": 42, "post": 69})),

dict(title="Long-Term Services and Supports Financing", tier=A,
 desc_pub=("Long-term services and supports (LTSS) - help with daily life over months and years - "
  "are financed by a patchwork: Medicaid (the largest payer, via waivers and state plans), "
  "Medicare (limited post-acute), private long-term-care insurance, veterans benefits, and "
  "out-of-pocket spending. No single program covers everything.\n"
  "Financing shapes options: Medicaid's institutional bias is slowly yielding to rebalancing toward "
  "home- and community-based services, which most people prefer and which usually cost less. "
  "Planning ahead - insurance, savings, understanding programs - prevents crisis-driven decisions."),
 desc_sig=("Signature LTSS financing navigation models lifetime scenarios across payer combinations, "
  "so families choose with eyes open instead of discovering gaps mid-crisis."),
 how_pub=("Benefits counselors map the person's needs against payer rules, sequence applications "
  "(Medicaid, VA, private insurance), and build a financing plan covering services, housing, and "
  "backup. Plans are reviewed as needs and rules change."),
 how_sig=("Signature scenario modeling compares payer combinations over time, revealing the true "
  "cost of each path."),
 keys=["Patchwork: Medicaid, Medicare, private insurance, VA, out-of-pocket",
  "Medicaid is the largest LTSS payer",
  "Rebalancing toward home- and community-based services",
  "Financing shapes available options",
  "Plan ahead to avoid crisis decisions",
  "Review plans as needs and rules change"],
 reqs=["Benefits-counseling expertise across payers",
  "Current program rules",
  "Long-range planning tools"],
 stds=["Medicaid LTSS regulations (public)",
  "State rebalancing initiatives"],
 cites=["Centers for Medicare and Medicaid Services — LTSS (public)",
  "Kaiser Family Foundation — LTSS research (public)"],
 demo=("compare", {"devices": [
   {"name": "HCBS waiver path", "score": 9, "note": "community living, usually lower cost"},
   {"name": "Private pay + insurance", "score": 6, "note": "flexible but expensive"},
   {"name": "No planning (crisis)", "score": 2, "note": "worst outcomes"}]})),

dict(title="Olmstead and Community Integration", tier=A,
 desc_pub=("The 1999 Olmstead Supreme Court decision held that unjustified segregation of people "
  "with disabilities in institutions is discrimination under the ADA. States must serve people in "
  "the most integrated setting appropriate - with community services expanding ever since.\n"
  "Olmstead enforcement - through DOJ settlements and advocacy - has moved thousands from "
  "institutions and sheltered workshops into community living and competitive employment. The "
  "principle guides everything from housing to day services: integration is the default."),
 desc_sig=("Signature Olmstead implementation tracks each state's integration metrics - community "
  "placements, employment outcomes, waiting lists - making compliance visible and comparable."),
 how_pub=("Advocates identify people who want community living but are stuck in institutions, "
  "document the barriers, and press states through complaints, litigation, or settlement "
  "negotiations. Transition teams arrange housing, services, and supports; outcomes are monitored "
  "for stability and satisfaction."),
 how_sig=("Signature integration metrics let advocates and states see progress - or its absence - "
  "in near real time."),
 keys=["Unjustified segregation is ADA discrimination",
  "Most integrated setting appropriate is the standard",
  "Enforcement moved thousands to community living",
  "Integration is the default across housing, work, day services",
  "Transition teams arrange the move",
  "Monitor stability and satisfaction after"],
 reqs=["Olmstead legal knowledge",
  "Transition team capacity",
  "Community housing and service supply"],
 stds=["Olmstead decision and DOJ enforcement guidance (public)",
  "HCBS settings rule (public regulation)"],
 cites=["U.S. Dept. of Justice — Olmstead enforcement (public)",
  "Bazelon Center for Mental Health Law — public resources (public)"],
 demo=("outcome", {"label": "People transitioned to community settings", "pre": 45, "post": 82})),

dict(title="Assistive Technology Assessment Protocols", tier=A,
 desc_pub=("Formal AT assessment protocols ensure the right technology for the right person: "
  "referral and intake, functional evaluation across environments, device trials with data, "
  "recommendation with justification, funding documentation, implementation and training, and "
  "follow-up. Frameworks like SETT (Student, Environment, Tasks, Tools) structure the inquiry.\n"
  "Protocols prevent the two classic failures: prescribing from a catalog without trials, and "
  "delivering devices without training. Data from trials - speed, accuracy, independence, "
  "satisfaction - justifies both the choice and the funding."),
 desc_sig=("Signature AT protocols run as guided workflows with trial-data capture built in, so "
  "every recommendation carries its evidence automatically."),
 how_pub=("The assessor interviews the person, observes real tasks in real environments, and "
  "trials candidate tools collecting performance data. The report recommends the best fit with "
  "trial evidence, documents medical or educational necessity for funding, and sets up training "
  "and follow-up."),
 how_sig=("Signature workflow-embedded trial capture makes evidence collection effortless during "
  "the trials themselves."),
 keys=["Referral to follow-up: a complete protocol",
  "SETT framework structures the inquiry",
  "Trials with data prevent catalog prescribing",
  "Training is part of delivery, not optional",
  "Trial data justifies funding",
  "Reassess as needs change"],
 reqs=["Trained assessors per AT domain",
  "Trial equipment and data tools",
  "Funding-documentation expertise"],
 stds=["RESNA AT service standards (public)",
  "SETT framework (public)"],
 cites=["RESNA — practice standards (public)",
  "Assistive Technology Industry Association — public resources (public)"],
 demo=("compare", {"devices": [
   {"name": "Device X (trial: 95% task success)", "score": 9, "note": "trial data supports"},
   {"name": "Device Y (trial: 60% task success)", "score": 6, "note": "partial fit"},
   {"name": "Device Z (no trial)", "score": 3, "note": "never prescribe untrialed"}]})),

dict(title="Inclusive Recreation Programs", tier=A,
 desc_pub=("Inclusive recreation adapts sports, arts, camps, and fitness so people with disabilities "
  "participate alongside everyone: adapted equipment, trained staff, buddy systems, sensory-"
  "friendly options, and genuinely welcoming culture. Therapeutic recreation uses activity toward "
  "health goals; inclusive recreation centers belonging.\n"
  "Universal design applies: a sensory-friendly hour helps autistic visitors and overwhelmed "
  "toddlers alike. Programs succeed when access is designed in, staff are trained, and participants "
  "with disabilities help lead."),
 desc_sig=("Signature inclusive-recreation design scores programs on a participation ladder - from "
  "segregated to fully inclusive - guiding continuous improvement."),
 how_pub=("Providers assess barriers in their offerings, train staff in inclusion and adaptation, "
  "acquire adapted equipment, and recruit participants with disabilities as advisors and leaders. "
  "Schedules include sensory-friendly and adaptive options; feedback drives refinement."),
 how_sig=("Signature participation-ladder scoring shows programs exactly where they stand and what "
  "the next rung requires."),
 keys=["Adapted sports, arts, camps, fitness",
  "Adapted equipment, trained staff, buddy systems",
  "Sensory-friendly options help many",
  "Participants with disabilities help lead",
  "Therapeutic recreation targets health goals",
  "Design access in from the start"],
 reqs=["Staff inclusion training",
  "Adapted equipment inventory",
  "Participant advisory roles"],
 stds=["Therapeutic recreation practice standards (public)",
  "ADA recreation requirements (public)"],
 cites=["National Recreation and Park Association — inclusion resources (public)",
  "American Therapeutic Recreation Association — public resources (public)"],
 demo=("audit", {"items": [
   {"item": "Program info in accessible formats", "ok": True},
   {"item": "Staff trained in inclusion", "ok": False},
   {"item": "Adaptive equipment available", "ok": True},
   {"item": "Sensory-friendly scheduling", "ok": False}]})),

dict(title="Guardianship Alternatives", tier=A,
 desc_pub=("Guardianship removes fundamental rights and should be the last resort. Alternatives "
  "form a ladder: supported decision-making, powers of attorney, health care proxies, "
  "representative payees, advance directives, and special-needs trusts - each preserving more "
  "autonomy than guardianship.\n"
  "Courts increasingly require exploring alternatives before granting guardianship, and limited "
  "guardianship (covering only specific decisions) beats plenary guardianship when some "
  "restriction is truly needed. Restoration - ending unneeded guardianships - is an active "
  "practice area."),
 desc_sig=("Signature alternatives counseling walks families through the full ladder with "
  "fill-in-the-blank instruments for each rung, so the least-restrictive workable option is "
  "found, not just discussed."),
 how_pub=("Counselors assess which decisions truly need support, match the lightest effective "
  "alternative, and help execute the legal instruments. When guardianship exists, they evaluate "
  "whether restoration or limitation is appropriate and petition accordingly."),
 how_sig=("Signature instrument libraries make each alternative executable in a single guided "
  "session."),
 keys=["Guardianship is the last resort",
  "Ladder: SDM, POA, proxies, payees, directives, trusts",
  "Each alternative preserves more autonomy",
  "Courts increasingly require exploring alternatives",
  "Limited beats plenary when restriction is needed",
  "Restoration ends unneeded guardianships"],
 reqs=["Legal expertise in alternatives",
  "Court familiarity with SDM",
  "Supported decision-making infrastructure"],
 stds=["State guardianship statutes (public)",
  "Uniform Guardianship Act guidance (public)"],
 cites=["American Bar Association — guardianship resources (public)",
  "National Guardianship Association — standards (public)"],
 demo=("compare", {"devices": [
   {"name": "Supported decision-making", "score": 10, "note": "full rights retained"},
   {"name": "Power of attorney", "score": 8, "note": "specific domains"},
   {"name": "Plenary guardianship", "score": 3, "note": "last resort only"}]})),

dict(title="Disability Data and Outcomes Research", tier=A,
 desc_pub=("Good data drives good services: prevalence, service use, employment, health, and "
  "satisfaction - disaggregated by disability type, race, and geography. Sources include the "
  "American Community Survey, the National Health Interview Survey, and program administrative "
  "data.\n"
  "Participatory research - disabled researchers studying disability - improves both questions and "
  "answers. Outcomes that matter: employment, community participation, health equity, and "
  "self-reported quality of life - not just service counts."),
 desc_sig=("Signature disability data practice pairs administrative data with community-defined "
  "indicators, so measurement reflects what disabled people value, not only what systems count."),
 how_pub=("Researchers and agencies define questions with community input, analyze existing "
  "datasets, and field new collection where gaps exist. Findings are reported accessibly and fed "
  "into policy and program design. Data governance includes disabled people in decisions about "
  "their data."),
 how_sig=("Signature community-defined indicator sets sit alongside administrative metrics in "
  "every program dashboard."),
 keys=["Disaggregate by type, race, geography",
  "Key sources: ACS, NHIS, administrative data",
  "Participatory research improves questions and answers",
  "Outcomes: employment, participation, health equity, quality of life",
  "Report accessibly; feed into design",
  "Include disabled people in data governance"],
 reqs=["Analytic capacity and data access",
  "Community research partnerships",
  "Accessible reporting"],
 stds=["Federal disability data standards (public)",
  "Participatory research ethics (public literature)"],
 cites=["U.S. Census Bureau — disability statistics (public)",
  "National Institute on Disability research (public)"],
 demo=("outcome", {"label": "Employment rate gap vs general population (points)", "pre": 42, "post": 31})),

dict(title="The Future of Independent Living", tier=A,
 desc_pub=("The future of independent living points toward technology-amplified self-direction: "
  "smart homes that adapt to residents, AI assistants that explain and execute, exoskeletons and "
  "advanced prosthetics, brain-computer interfaces for communication, and on-demand support "
  "platforms. Policy directions include expanded self-direction in Medicaid, paid family "
  "caregiving, and stronger Olmstead enforcement.\n"
  "The constant through every innovation: control stays with the person. Technology serves "
  "self-direction; it never replaces the person's authority over their own life."),
 desc_sig=("The Signature future-state is a self-direction operating system: one personal control "
  "plane for supports, devices, schedules, and budgets - with the person as administrator. This "
  "database is a prototype of that system's knowledge core."),
 how_pub=("Systems expand consumer-directed options, invest in enabling technology with user-led "
  "design, and enforce integration. Users co-design every tool; outcomes center self-reported "
  "control and participation."),
 how_sig=("Signature's personal control plane makes self-direction the default interface for all "
  "supports."),
 keys=["Technology amplifies self-direction",
  "Smart homes, AI assistants, advanced mobility, BCIs",
  "Policy: expanded self-direction, paid caregiving, Olmstead",
  "Control stays with the person - always",
  "Users co-design every tool",
  "Outcomes: self-reported control and participation"],
 reqs=["User-led technology design",
  "Consumer-directed policy expansion",
  "Workforce to support tech-enabled living"],
 stds=["Emerging standards for assistive AI (public literature)"],
 cites=["Administration for Community Living — future directions (public)",
  "World Health Organization — assistive technology reports (public)"],
 demo=("outcome", {"label": "People directing their own support plans", "pre": 55, "post": 90})),
]
