#!/usr/bin/env python3
"""Topics + config for the elder-care pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never medical advice.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

CFG = {
    "slug": "elder-care",
    "name_pub": "The Elder Care Database",
    "name_sig": "Signature Elder Care Database",
    "tagline_pub": ("Elder care from the ground up: care models and settings, choosing and paying "
                    "for care, mobility and safety, staffing, service quality, and support for "
                    "family caregivers - every record carrying the full entry taught progressively "
                    "along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of elder care: the same real care "
                    "knowledge carried forward, plus Signature-built care models, quality systems, "
                    "and staffing designs original to this system."),
    "record_kind": "elder care record",
    "record_kind_plural": "elder care records",
    "prefix_pub": "JAH-ELDC-", "prefix_sig": "JAH-ELDCS-",
    "ai_pub": "JAH Elder Care Archivist",
    "ai_sig": "JAH Signature Elder Care Creator",
    "role_pub": ("elder care archivist - teaching care models, settings, paying for care, mobility, "
                 "safety, staffing, and quality; answers from many angles - definition, example, "
                 "process, choice, quality - using only archive data from this system"),
    "role_sig": ("Signature creator of elder care systems - designing care models, quality "
                 "frameworks, and staffing systems as original Signature works; answers from many "
                 "angles using only archive data from this system"),
    "search_ph": "Search care models, settings, mobility, staffing, safety, quality...",
    "chat_ph": "Ask about elder care...",
    "greet_pub": ("I am the JAH Elder Care Archivist. Ask me about care models, choosing care, "
                  "mobility, safety, staffing, and quality. I share educational information, not "
                  "medical advice."),
    "greet_sig": ("I am the JAH Signature Elder Care Creator. Ask me about Signature-built care "
                  "models and quality systems. Educational information only."),
    "gen_blurb": ("Generate clearly-labeled elder care studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded elder care records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. "
                      "Educational information only — not medical advice."),
    "demo_kind": "elder-care-demo",
    "demo_title": "Elder Care Demo",
    "health": True,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Elder Care Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "adl":
        return fill(
            "adls = @@ADLS@@\n"
            "indep = [a for a in adls if a['independent']]\n"
            "needs = [a for a in adls if not a['independent']]\n"
            "print('ADL assessment: %d activities' % len(adls))\n"
            "print('Independent:', len(indep), ' Needs help:', len(needs))\n"
            "for a in needs:\n"
            "    print(' SUPPORT:', a['activity'])\n",
            {"ADLS": p["adls"]})
    if v == "staffing":
        return fill(
            "residents = @@RES@@\nstaff = @@STAFF@@\n"
            "ratio = residents / staff if staff else 0\n"
            "print('Residents:', residents, ' Direct-care staff on shift:', staff)\n"
            "print('Residents per staff: %.1f' % ratio)\n"
            "print('Status:', 'OK' if ratio <= @@MAXR@@ else 'UNDERSTAFFED - add staff')\n",
            {"RES": p["residents"], "STAFF": p["staff"], "MAXR": p["max_ratio"]})
    if v == "safety":
        return fill(
            "items = @@ITEMS@@\n"
            "fails = [i for i in items if not i['ok']]\n"
            "print('Safety check: %d items, %d need action' % (len(items), len(fails)))\n"
            "for i in fails:\n"
            "    print(' ACTION:', i['item'])\n",
            {"ITEMS": p["items"]})
    if v == "outcome":
        return fill(
            "label = @@LABEL@@\npre = @@PRE@@\npost = @@POST@@\n"
            "delta = post - pre\n"
            "print('Outcome:', label)\n"
            "print('Before: %d  After: %d  Change: %+d' % (pre, post, delta))\n"
            "print('Direction:', 'improved' if delta > 0 else 'declined' if delta < 0 else 'unchanged')\n",
            {"LABEL": p["label"], "PRE": p["pre"], "POST": p["post"]})
    if v == "compare":
        return fill(
            "options = @@OPTS@@\n"
            "ranked = sorted(options, key=lambda o: o['score'], reverse=True)\n"
            "print('Care setting comparison:')\n"
            "for o in ranked:\n"
            "    print(' %s: %d/10 — %s' % (o['name'], o['score'], o['note']))\n",
            {"OPTS": p["options"]})
    raise ValueError("unknown demo variant " + v)


TOPICS = [
dict(title="What Elder Care Is", tier=F,
 desc_pub=("Elder care (long-term care) is the range of services supporting older adults who need "
  "help with daily life: personal care, health monitoring, meals, housekeeping, transportation, "
  "and companionship. It spans home care, adult day programs, assisted living, nursing facilities, "
  "and hospice - delivered by family caregivers, paid aides, nurses, and interdisciplinary teams.\n"
  "The guiding value is aging with dignity: supporting independence as fully as possible while "
  "providing safety and comfort where independence fades. Good elder care adapts to the person - "
  "their history, preferences, culture, and goals - rather than processing them through routines."),
 desc_sig=("The Signature system models elder care as a dignity-preserving support gradient: "
  "assistance scales precisely to need in each life domain, reviewed continuously, so no one "
  "receives less help than they need or more control-loss than necessary."),
 how_pub=("Needs are assessed across daily activities, health, cognition, home safety, and "
  "caregiver capacity. A plan matches services to needs - starting with the least restrictive "
  "setting that is safe. Services begin, are monitored for quality and fit, and adjust as needs "
  "change. The older adult's voice leads every decision they can participate in."),
 how_sig=("Signature support gradients make the 'right amount of help' computable per domain, "
  "with reviews triggered by change rather than by calendar."),
 keys=["Services supporting older adults with daily life",
  "Spans home care, adult day, assisted living, nursing, hospice",
  "Delivered by family, aides, nurses, teams",
  "Guiding value: aging with dignity",
  "Least restrictive safe setting first",
  "The older adult's voice leads"],
 reqs=["Needs assessment across life domains",
  "A spectrum of service options",
  "Quality monitoring and adjustment"],
 stds=["State licensing for care settings (public)",
  "CMS conditions of participation for certified providers (public)"],
 cites=["Administration for Community Living — aging resources (public)",
  "National Institute on Aging — public information (public)"],
 demo=("compare", {"options": [
   {"name": "Home care", "score": 9, "note": "familiar setting, flexible"},
   {"name": "Assisted living", "score": 7, "note": "social, some support"},
   {"name": "Nursing facility", "score": 5, "note": "for 24-hour skilled need"}]})),

dict(title="Aging in Place", tier=F,
 desc_pub=("Aging in place means living safely and independently in one's own home and community as "
  "one ages. It requires three supports: a safe, accessible home; in-home services (personal "
  "care, meals, health monitoring); and community connection (transportation, social engagement, "
  "nearby help in emergencies).\n"
  "Most older adults prefer it, and it usually costs less than facility care. Success is planned: "
  "home assessments, modifications, service arrangements, and emergency plans made before crisis "
  "forces decisions."),
 desc_sig=("Signature aging-in-place design treats the home as a care platform: sensor-supported "
  "safety monitoring, on-demand services, and social connection woven into one plan the older "
  "adult controls."),
 how_pub=("An assessment maps the person's abilities against their home and community. Modifications "
  "remove hazards; services fill gaps in daily activities; transportation and social options are "
  "lined up. Emergency plans name who responds and how. Regular check-ins catch new needs early."),
 how_sig=("Signature home-as-platform plans integrate monitoring, services, and social connection "
  "with the resident's preferences governing."),
 keys=["Live safely and independently at home as one ages",
  "Requires: safe home, in-home services, community connection",
  "Most older adults prefer it; usually costs less",
  "Success is planned before crisis",
  "Home assessments and modifications",
  "Emergency plans name responders"],
 reqs=["Home safety assessment",
  "In-home service availability",
  "Emergency response plan"],
 stds=["State home-care licensing (public)",
  "Home modification best practices (public literature)"],
 cites=["National Institute on Aging — aging in place (public)",
  "AARP — livability resources (public)"],
 demo=("safety", {"items": [
   {"item": "Grab bars in bathroom", "ok": True},
   {"item": "Adequate lighting on stairs", "ok": False},
   {"item": "Emergency contact list posted", "ok": True},
   {"item": "Smoke/CO detectors working", "ok": True}]})),

dict(title="Activities of Daily Living", tier=F,
 desc_pub=("Activities of daily living (ADLs) are the basic self-care tasks: bathing, dressing, "
  "eating, toileting, continence, and transferring (moving between bed, chair, standing). "
  "Instrumental ADLs (IADLs) are the complex tasks of independent life: cooking, housekeeping, "
  "managing medications and money, shopping, transportation, and using the phone.\n"
  "ADL assessment is the universal language of care need: how many ADLs need help determines "
  "eligibility for programs, staffing plans, and care settings. IADL difficulty usually appears "
  "first and signals early intervention opportunities."),
 desc_sig=("Signature ADL tracking uses standardized, repeatable assessments feeding a support "
  "gradient - so changes in function automatically prompt plan review instead of waiting for a "
  "crisis or a calendar."),
 how_pub=("A nurse or assessor observes or interviews about each ADL and IADL, scoring "
  "independence. The profile determines service hours, setting appropriateness, and program "
  "eligibility. Re-assessment on a schedule - or after events like hospitalization - keeps the "
  "plan matched to reality."),
 how_sig=("Signature change-triggered re-assessment prompts review the moment function shifts, "
  "not months later."),
 keys=["ADLs: bathing, dressing, eating, toileting, continence, transferring",
  "IADLs: cooking, meds, money, shopping, transport, phone",
  "ADL counts determine eligibility, staffing, settings",
  "IADL difficulty appears first - early signal",
  "Universal language of care need",
  "Re-assess after health events"],
 reqs=["Standardized ADL/IADL instruments",
  "Trained assessors",
  "Re-assessment triggers"],
 stds=["CMS assessment requirements (public)",
  "State program eligibility rules using ADL counts"],
 cites=["Centers for Medicare and Medicaid Services — assessment guidance (public)",
  "National Institute on Aging — daily functioning (public)"],
 demo=("adl", {"adls": [
   {"activity": "Bathing", "independent": False},
   {"activity": "Dressing", "independent": True},
   {"activity": "Eating", "independent": True},
   {"activity": "Toileting", "independent": True},
   {"activity": "Transferring", "independent": False},
   {"activity": "Medication management", "independent": False}]})),

dict(title="Levels of Long-Term Care", tier=F,
 desc_pub=("Long-term care forms a spectrum: informal family care; home care (aide visits); adult "
  "day programs; assisted living (housing plus personal care and meals); memory care (secured "
  "dementia settings); nursing facilities (24-hour skilled nursing); and hospice (comfort care at "
  "life's end). Each step adds supervision and clinical capacity.\n"
  "Matching level to need avoids both under-care (unsafe gaps) and over-care (unnecessary "
  "restriction and cost). People often use several levels over time as needs evolve."),
 desc_sig=("Signature level-matching uses the support gradient to recommend the least restrictive "
  "setting that safely meets the assessed profile - with transparent reasoning families can "
  "understand and question."),
 how_pub=("Assessment produces an ADL/IADL and clinical profile; a counselor or care manager maps "
  "it to levels, tours options with the family, and arranges admission. Transitions - hospital to "
  "rehab to home - are coordinated with handoffs. Levels are re-matched as needs change."),
 how_sig=("Signature transparent matching shows families exactly which needs drive the "
  "recommendation."),
 keys=["Spectrum: family care, home care, adult day, assisted living, memory care, nursing, hospice",
  "Each step adds supervision and clinical capacity",
  "Match level to need: avoid under-care and over-care",
  "People use several levels over time",
  "Transitions need coordinated handoffs",
  "Re-match as needs change"],
 reqs=["Assessment across function and clinical need",
  "Knowledge of local options at each level",
  "Transition coordination"],
 stds=["State licensing per level (public)",
  "CMS certification requirements (public)"],
 cites=["Centers for Medicare and Medicaid Services — care options (public)",
  "National Institute on Aging — long-term care (public)"],
 demo=("compare", {"options": [
   {"name": "Adult day program", "score": 8, "note": "daytime supervision, caregiver respite"},
   {"name": "Assisted living", "score": 7, "note": "housing + personal care"},
   {"name": "Nursing facility", "score": 6, "note": "24-hour skilled need"}]})),

dict(title="Choosing a Care Setting", tier=F,
 desc_pub=("Choosing a care setting is among the most consequential family decisions. The process: "
  "clarify needs and budget, identify candidate settings, tour (observing staff-resident "
  "interactions, cleanliness, odors, activity), check inspection reports and ratings (CMS Care "
  "Compare for nursing homes), interview administrators about staffing and turnover, and talk to "
  "residents and families.\n"
  "Red flags: high turnover, frequent leadership change, poor inspection history, evasive answers, "
  "unhappy residents. Green flags: stable staff who know residents by name, engaging activities, "
  "transparent leadership, family councils."),
 desc_sig=("Signature setting selection structures the search as a scored comparison - needs match, "
  "quality indicators, cost, location, culture fit - so emotion and marketing do not override "
  "evidence."),
 how_pub=("Families list must-haves (dementia expertise, location near family), gather candidates "
  "from referrals and directories, tour with a checklist, review public quality data, and compare "
  "notes before deciding. A trial respite stay can test fit before commitment."),
 how_sig=("Signature scored comparisons weight what matters most to the family, keeping decisions "
  "anchored to their values."),
 keys=["Clarify needs and budget first",
  "Tour with eyes open: staff interactions, cleanliness, activity",
  "Check CMS Care Compare and inspection reports",
  "Ask about staffing ratios and turnover",
  "Red flags: turnover, poor inspections, evasive answers",
  "Trial stays test fit"],
 reqs=["Needs and budget clarity",
  "Tour checklist",
  "Access to public quality data"],
 stds=["CMS Care Compare public reporting (public)",
  "State inspection and disclosure rules"],
 cites=["Centers for Medicare and Medicaid Services — Care Compare (public)",
  "National Institute on Aging — choosing care (public)"],
 demo=("compare", {"options": [
   {"name": "Sunrise Gardens (tour)", "score": 8, "note": "stable staff, good activities"},
   {"name": "Maple Court (tour)", "score": 5, "note": "high turnover noted"},
   {"name": "Elm House (tour)", "score": 7, "note": "strong inspection history"}]})),

dict(title="Home Care Services", tier=F,
 desc_pub=("Home care brings help to the older adult's door: personal care aides (bathing, dressing, "
  "meals), homemakers (cleaning, laundry), home health nurses (wound care, injections, monitoring), "
  "and therapists (physical, occupational, speech). Non-medical home care focuses on daily living; "
  "home health adds skilled clinical services, often after hospitalization.\n"
  "Advantages: familiar surroundings, personalized one-on-one attention, family involvement. "
  "Challenges: worker reliability, supervision at a distance, and cost for extensive hours - "
  "24-hour home care can exceed facility costs."),
 desc_sig=("Signature home-care coordination schedules visits, tracks task completion, and alerts "
  "families to missed visits - bringing facility-grade oversight to the home setting."),
 how_pub=("Assessment sets authorized tasks and hours; agencies match aides to clients considering "
  "skills, language, and personality. Care plans list exact duties; supervisors visit periodically. "
  "Families monitor quality and report concerns; plans adjust as needs change."),
 how_sig=("Signature visit verification and family alerts close the supervision gap of home-based "
  "care."),
 keys=["Personal care, homemaking, home health nursing, therapies",
  "Non-medical vs skilled home health",
  "Advantages: familiar setting, one-on-one, family involved",
  "Challenges: reliability, distant supervision, cost at high hours",
  "Care plans list exact duties",
  "Family monitoring matters"],
 reqs=["Licensed agencies (where required)",
  "Care plans with specific tasks",
  "Supervisory visits and backup coverage"],
 stds=["State home-care licensing (public)",
  "Medicare home health conditions of participation (public)"],
 cites=["Centers for Medicare and Medicaid Services — home health (public)",
  "National Association for Home Care — public resources (public)"],
 demo=("staffing", {"residents": 1, "staff": 1, "max_ratio": 1})),

dict(title="Adult Day Programs", tier=F,
 desc_pub=("Adult day programs provide daytime supervision, meals, activities, and often health "
  "monitoring in a community setting - giving family caregivers respite while engaging the older "
  "adult socially. Specialized programs serve people with dementia with tailored activities and "
  "higher staffing.\n"
  "Benefits are two-sided: participants gain structure, social contact, and stimulation; caregivers "
  "gain reliable hours for work, rest, or errands. Programs are far less costly than full-time "
  "facility care."),
 desc_sig=("Signature day-program design personalizes activity schedules to each participant's "
  "abilities and interests, tracked against engagement measures - so days are meaningful, not "
  "merely supervised."),
 how_pub=("Families tour programs, checking activities, staffing, health services, and dementia "
  "capability. Enrollment includes health assessment and a care plan; transportation is often "
  "provided. Staff communicate daily with families about the participant's day."),
 how_sig=("Signature engagement tracking shows families what their loved one actually did and "
  "enjoyed each day."),
 keys=["Daytime supervision, meals, activities, health monitoring",
  "Dementia-specialized programs available",
  "Two-sided benefit: participant engagement + caregiver respite",
  "Far less costly than facility care",
  "Transportation often included",
  "Daily family communication"],
 reqs=["Appropriate staffing ratios",
  "Activity programming capacity",
  "Health-monitoring capability"],
 stds=["State adult day licensing (public)",
  "National Adult Day Services Association standards (public)"],
 cites=["National Adult Day Services Association — public resources (public)"],
 demo=("outcome", {"label": "Caregiver stress scores (lower better)", "pre": 72, "post": 48})),

dict(title="Assisted Living Basics", tier=F,
 desc_pub=("Assisted living combines housing, meals, personal care, medication management, and "
  "social activities for older adults who need daily support but not 24-hour nursing. Residents "
  "typically have private apartments with staff available around the clock.\n"
  "Assisted living is primarily private-pay, with costs varying widely by region and care level. "
  "Regulation is state-based (no federal certification like nursing homes), so quality varies - "
  "making inspection-history review and careful touring essential."),
 desc_sig=("Signature assisted-living evaluation scores communities on staffing stability, "
  "inspection history, and resident-engagement indicators - the factors research links to "
  "resident well-being."),
 how_pub=("Families assess needs, tour communities, review state inspection reports, and compare "
  "contracts (what is included vs. à la carte). Move-in includes health assessment and a service "
  "plan; care levels - and fees - adjust as needs change. Residents retain significant autonomy."),
 how_sig=("Signature contract comparison tools make included-vs-extra costs transparent before "
  "signing."),
 keys=["Housing + meals + personal care + meds + activities",
  "Private apartments, 24-hour staff availability",
  "Primarily private-pay; costs vary widely",
  "State-regulated; quality varies",
  "Review inspection history carefully",
  "Residents retain autonomy"],
 reqs=["State license in good standing",
  "Service plan with adjustable care levels",
  "Transparent fee structure"],
 stds=["State assisted-living regulations (public)"],
 cites=["National Center for Assisted Living — public resources (public)"],
 demo=("compare", {"options": [
   {"name": "Community A", "score": 8, "note": "clean inspections, stable staff"},
   {"name": "Community B", "score": 6, "note": "good activities, newer"},
   {"name": "Community C", "score": 4, "note": "inspection concerns"}]})),

dict(title="Nursing Facility Care", tier=F,
 desc_pub=("Nursing facilities (nursing homes) provide 24-hour skilled nursing, rehabilitation, and "
  "personal care for people with complex medical needs or severe functional impairment. They are "
  "federally certified (if accepting Medicare/Medicaid), inspected regularly, and publicly rated "
  "on CMS Care Compare.\n"
  "Quality varies enormously and staffing is the key driver: more RN hours per resident-day "
  "predicts better outcomes. Residents have strong federal rights - to dignity, choice, "
  "visitation, and freedom from restraints and abuse."),
 desc_sig=("Signature nursing-facility evaluation weights staffing metrics above all - RN hours, "
  "turnover, weekend coverage - because research consistently shows staffing is the quality "
  "lever that matters most."),
 how_pub=("Admission follows hospital discharge or community assessment; the facility completes a "
  "comprehensive assessment (MDS) and builds a care plan with resident and family. Care is "
  "delivered by nursing, therapy, dietary, and activities staff; care-plan meetings review "
  "progress. Families monitor via visits, councils, and ombudsman programs."),
 how_sig=("Signature staffing-first scoring directs families to the facilities where residents "
  "do best."),
 keys=["24-hour skilled nursing and rehab",
  "Federally certified; inspected; publicly rated",
  "Staffing levels drive quality",
  "Strong federal resident rights",
  "Care plans built with resident and family",
  "Ombudsmen advocate for residents"],
 reqs=["CMS certification and acceptable inspection history",
  "Adequate RN and aide staffing",
  "Resident and family councils"],
 stds=["CMS Requirements of Participation (public regulation)",
  "Federal nursing home resident rights (public law)"],
 cites=["Centers for Medicare and Medicaid Services — nursing home quality (public)",
  "National Consumer Voice for Quality Long-Term Care — public resources (public)"],
 demo=("staffing", {"residents": 40, "staff": 8, "max_ratio": 8})),

dict(title="Paying for Long-Term Care", tier=F,
 desc_pub=("Long-term care is expensive and poorly covered: Medicare covers only short skilled "
  "stays, not ongoing personal care. Medicaid covers long-term care for those with limited income "
  "and assets - the largest payer nationally. Private long-term-care insurance helps if bought "
  "early; most families pay out-of-pocket, spend down, and then qualify for Medicaid.\n"
  "Planning ahead matters enormously: understanding options at 60 beats crisis decisions at 85. "
  "Elder-law attorneys help with asset planning within the rules; benefits counselors explain "
  "program specifics."),
 desc_sig=("Signature financing navigation models the spend-down trajectory under different care "
  "scenarios, so families see the financial path years ahead instead of discovering it in "
  "crisis."),
 how_pub=("Families inventory resources - income, savings, insurance, home equity - and get "
  "counseling on program rules. They choose care settings with costs modeled over years, apply "
  "for benefits when eligible, and consult elder-law attorneys for compliant planning. Plans are "
  "revisited as needs and rules change."),
 how_sig=("Signature multi-year cost modeling compares settings on total trajectory, not just "
  "monthly sticker price."),
 keys=["Medicare: short skilled stays only, not ongoing care",
  "Medicaid: largest payer, for limited income/assets",
  "Private LTC insurance helps if bought early",
  "Most families: out-of-pocket then spend-down",
  "Plan at 60, not in crisis at 85",
  "Elder-law attorneys and benefits counselors help"],
 reqs=["Resource inventory",
  "Benefits counseling",
  "Elder-law guidance for compliant planning"],
 stds=["Medicaid eligibility rules (public)",
  "State partnership program rules where they exist"],
 cites=["Centers for Medicare and Medicaid Services — paying for care (public)",
  "National Academy of Elder Law Attorneys — public resources (public)"],
 demo=("outcome", {"label": "Families with a written financing plan", "pre": 28, "post": 74})),

dict(title="Family Caregiver Support", tier=F,
 desc_pub=("Family caregivers - spouses, adult children, relatives - provide the majority of "
  "long-term care in every country. The work is meaningful and often overwhelming: caregivers face "
  "higher rates of depression, chronic illness, and financial strain. Supporting them is both humane "
  "and practical - caregiver collapse precipitates facility placement.\n"
  "Effective supports: respite care (someone else covers while the caregiver rests), training in "
  "care tasks, support groups, counseling, and flexible workplace policies. Caregiver assessment - "
  "asking what the caregiver needs - should accompany every care plan."),
 desc_sig=("Signature caregiver support treats the caregiver as a second client: assessed needs, "
  "a support plan, and regular check-ins - because the care system's stability depends on theirs."),
 how_pub=("Care plans include caregiver assessment alongside the older adult's. Respite is "
  "scheduled regularly, not just in crisis; training covers transfers, medications, and dementia "
  "communication. Support groups and counseling address emotional load; employers are engaged on "
  "flexibility."),
 how_sig=("Signature dual-client planning gives caregivers their own goals and supports in the "
  "record, not just a mention."),
 keys=["Families provide most long-term care",
  "Caregivers face health and financial strain",
  "Support the caregiver or risk placement",
  "Respite, training, groups, counseling, workplace flexibility",
  "Assess caregiver needs with every care plan",
  "Scheduled respite, not crisis-only"],
 reqs=["Caregiver assessment tools",
  "Respite capacity",
  "Training and support-group offerings"],
 stds=["National Family Caregiver Support Program standards (public law)",
  "State respite program rules"],
 cites=["Administration for Community Living — caregiver supports (public)",
  "AARP — caregiving resources (public)"],
 demo=("outcome", {"label": "Caregivers reporting manageable stress", "pre": 44, "post": 78})),

# ---------------- Compounded (12) ----------------
dict(title="Comprehensive Geriatric Assessment", tier=C,
 desc_pub=("Comprehensive geriatric assessment (CGA) is the gold-standard evaluation for frail older "
  "adults: a multidisciplinary review of medical, functional, cognitive, psychological, social, "
  "and environmental status. Teams - geriatrician, nurse, social worker, pharmacist, therapists - "
  "identify all treatable problems and build one coordinated plan.\n"
  "CGA reduces hospitalization and nursing-home placement in trials. It exemplifies geriatric "
  "wisdom: in complex older patients, the whole picture - medications, falls, cognition, support - "
  "matters more than any single diagnosis. This record is educational; assessment is clinical work."),
 desc_sig=("Signature CGA operations run the multidisciplinary review as a structured workflow with "
  "domain checklists, so no assessment misses medications, cognition, function, or home safety."),
 how_pub=("Referral triggers team evaluation across all domains - often in a dedicated geriatrics "
  "clinic or via home visit. The team meets, reconciles findings, and produces one plan addressing "
  "medical, functional, and social needs with assigned owners. Follow-up tracks implementation."),
 how_sig=("Signature domain checklists ensure every CGA covers medications, falls, cognition, "
  "mood, function, nutrition, and home safety."),
 keys=["Multidisciplinary review: medical, functional, cognitive, social, environmental",
  "Team: geriatrician, nurse, social worker, pharmacist, therapists",
  "One coordinated plan from all findings",
  "Reduces hospitalization and placement in trials",
  "Whole picture beats single diagnosis",
  "Educational record; clinical work by professionals"],
 reqs=["Geriatrics-trained multidisciplinary team",
  "Structured domain assessment tools",
  "Care-plan coordination"],
 stds=["CGA practice standards (public literature)",
  "Geriatrics accreditation expectations"],
 cites=["American Geriatrics Society — public resources (public)",
  "National Institute on Aging — geriatric assessment (public)"],
 demo=("adl", {"adls": [
   {"activity": "Bathing", "independent": True},
   {"activity": "Medication management", "independent": False},
   {"activity": "Cooking", "independent": False},
   {"activity": "Transportation", "independent": False},
   {"activity": "Housekeeping", "independent": False}]})),

dict(title="Mobility Support and Fall Prevention", tier=C,
 desc_pub=("Falls are the leading cause of injury in older adults - and largely preventable. "
  "Evidence-based prevention includes strength and balance exercise (Tai Chi, PT programs), home "
  "hazard removal, vision correction, medication review (some drugs increase fall risk), proper "
  "footwear, and assistive devices fitted correctly.\n"
  "Programs like STEADI (CDC) give clinicians a fall-risk screening and intervention workflow. "
  "After a fall, assessment must find the cause - it is never 'just old age' - and intervene "
  "before the next one."),
 desc_sig=("Signature fall-prevention systems combine risk screening, home-hazard mapping, and "
  "exercise adherence tracking into one prevention plan per at-risk elder."),
 how_pub=("Clinicians screen for fall risk yearly (STEADI protocol): history, gait, medications. "
  "At-risk elders get PT for strength and balance, home safety evaluation, vision referral, and "
  "medication review. Progress is re-screened; falls trigger root-cause review."),
 how_sig=("Signature prevention plans link the screen, the interventions, and adherence tracking "
  "in one view."),
 keys=["Falls: leading injury cause, largely preventable",
  "Exercise, hazard removal, vision, meds review, footwear, devices",
  "STEADI gives clinicians a screening workflow",
  "Every fall gets root-cause review",
  "Never 'just old age'",
  "Re-screen to track progress"],
 reqs=["Fall-risk screening protocol",
  "PT and home-safety capacity",
  "Medication review process"],
 stds=["CDC STEADI toolkit (public)",
  "Fall-prevention clinical guidelines (public literature)"],
 cites=["Centers for Disease Control — STEADI (public)",
  "National Council on Aging — falls prevention (public)"],
 demo=("safety", {"items": [
   {"item": "Annual fall-risk screen completed", "ok": True},
   {"item": "Home hazards removed", "ok": False},
   {"item": "Vision checked this year", "ok": True},
   {"item": "Balance exercise routine active", "ok": False}]})),

dict(title="Medication Management for Older Adults", tier=C,
 desc_pub=("Older adults often take many medications - polypharmacy - raising risks of interactions, "
  "side effects, and falls. Good medication management means regular brown-bag reviews (bring all "
  "bottles), deprescribing what no longer helps, checking against Beers Criteria (drugs risky for "
  "elders), and simplifying regimens.\n"
  "Pharmacist-led reviews catch what busy visits miss. This record is educational: medication "
  "changes belong with the prescriber and pharmacist, never self-directed."),
 desc_sig=("Signature medication management maintains a live medication list shared across "
  "prescribers, with interaction and Beers-criteria screening on every change."),
 how_pub=("At least yearly - and after every hospitalization - the clinician or pharmacist reviews "
  "every medication against current conditions, applying Beers Criteria and interaction checks. "
  "Unneeded drugs are tapered with monitoring; regimens are simplified (fewer doses, combination "
  "pills where appropriate); the updated list goes to all providers and the patient."),
 how_sig=("Signature shared medication lists prevent the common failure of each prescriber seeing "
  "only their own prescriptions."),
 keys=["Polypharmacy raises interaction and fall risks",
  "Brown-bag reviews: bring every bottle",
  "Beers Criteria flag drugs risky for elders",
  "Deprescribe what no longer helps",
  "Pharmacist-led reviews catch hidden problems",
  "Changes with prescribers, never self-directed"],
 reqs=["Complete medication lists across prescribers",
  "Beers Criteria and interaction screening",
  "Pharmacist review capacity"],
 stds=["Beers Criteria (public clinical standard)",
  "CMS medication-review requirements"],
 cites=["American Geriatrics Society — Beers Criteria (public)",
  "U.S. Food and Drug Administration — medication safety (public)"],
 demo=("outcome", {"label": "High-risk medications discontinued", "pre": 31, "post": 68})),

dict(title="Nutrition and Meal Services", tier=C,
 desc_pub=("Good nutrition protects health, healing, and independence - yet many older adults face "
  "food insecurity, chewing or swallowing difficulties, or the apathy of eating alone. Services "
  "include home-delivered meals (Meals on Wheels), congregate meals at senior centers, medically "
  "tailored meals for conditions like diabetes, and nutrition counseling.\n"
  "Meal programs do double duty: the daily delivery is also a wellness check, catching problems "
  "early. Malnutrition screening belongs in every geriatric assessment."),
 desc_sig=("Signature nutrition services pair meal delivery with wellness-check protocols and "
  "malnutrition screening, so every meal is also a safety contact."),
 how_pub=("Assessment screens for food insecurity, chewing/swallowing issues, and malnutrition "
  "risk. Eligible elders enroll in home-delivered or congregate meals; dietitians tailor for "
  "medical needs. Drivers and site staff are trained to notice and report concerns."),
 how_sig=("Signature wellness-check protocols turn drivers into an early-warning network with "
  "clear escalation paths."),
 keys=["Nutrition protects health, healing, independence",
  "Home-delivered, congregate, medically tailored meals",
  "Delivery doubles as a wellness check",
  "Screen for insecurity, chewing, malnutrition",
  "Eating alone reduces intake - social meals help",
  "Dietitians tailor for medical conditions"],
 reqs=["Meal program enrollment and eligibility",
  "Dietitian access",
  "Wellness-check training for delivery staff"],
 stds=["Older Americans Act nutrition program standards (public law)",
  "Dietary Guidelines for Americans (public)"],
 cites=["Administration for Community Living — nutrition programs (public)",
  "Meals on Wheels America — public resources (public)"],
 demo=("outcome", {"label": "Participants at healthy weight/nutrition", "pre": 62, "post": 84})),

dict(title="Dementia Care Approaches", tier=C,
 desc_pub=("Dementia care centers the person behind the symptoms: knowing their history, "
  "preferences, and remaining abilities, then shaping the environment and interactions to reduce "
  "confusion and distress. Evidence-backed approaches include consistent routines, simplified "
  "choices, meaningful activities matched to ability, and communication that validates feelings "
  "rather than arguing facts.\n"
  "Behavioral expressions - agitation, wandering, resistance - usually signal unmet needs: pain, "
  "fear, boredom, overstimulation. Skilled caregivers investigate the need behind the behavior. "
  "This record is educational; diagnosis and treatment are clinical."),
 desc_sig=("Signature dementia care builds a life-story profile for each person - history, "
  "preferences, triggers, soothers - accessible to every caregiver, so care is personal even "
  "with rotating staff."),
 how_pub=("Assessment maps cognitive abilities, behavioral patterns, and life history. Care plans "
  "specify routines, communication approaches, and meaningful activities; environments are "
  "simplified and secured. Staff are trained in validation and de-escalation; families learn the "
  "same approaches. Plans evolve as the disease progresses."),
 how_sig=("Signature life-story profiles keep personal knowledge alive across staff changes - the "
  "most common point of failure in dementia care."),
 keys=["Center the person behind the symptoms",
  "Know history, preferences, remaining abilities",
  "Behaviors signal unmet needs - investigate",
  "Validate feelings; don't argue facts",
  "Routines, simplified choices, meaningful activities",
  "Train families in the same approaches"],
 reqs=["Dementia-capable staff training",
  "Life-history assessment",
  "Safe, simplified environments"],
 stds=["Alzheimer's Association dementia care practice recommendations (public)",
  "State dementia-training requirements"],
 cites=["Alzheimer's Association — care resources (public)",
  "National Institute on Aging — dementia information (public)"],
 demo=("safety", {"items": [
   {"item": "Wandering-safe environment", "ok": True},
   {"item": "Staff trained in validation", "ok": False},
   {"item": "Life-history profile completed", "ok": True},
   {"item": "Meaningful activity plan", "ok": False}]})),

dict(title="Staffing Models in Care Facilities", tier=C,
 desc_pub=("Staffing is the quality engine of care facilities: registered nurses, licensed "
  "practical nurses, and certified nursing assistants in ratios that allow real care. Research "
  "links higher staffing - especially RN hours - to fewer pressure injuries, infections, and "
  "hospitalizations.\n"
  "Models include team nursing, primary nursing (one nurse owns a resident group), and consistent "
  "assignment (same aides with same residents - strongly linked to quality). Chronic understaffing "
  "and turnover are the industry's central quality problem."),
 desc_sig=("Signature staffing management optimizes schedules for consistent assignment and "
  "adequate ratios simultaneously, treating both as quality inputs to be maximized, not costs to "
  "be minimized."),
 how_pub=("Administrators set target ratios by acuity, recruit and retain with competitive pay and "
  "supportive culture, and schedule for consistent assignment. Staffing data is reported (Payroll "
  "Based Journal for nursing homes) and monitored against targets; gaps trigger agency use or "
  "census adjustments - never silent understaffing."),
 how_sig=("Signature scheduling optimization balances consistency, ratios, and staff well-being "
  "in one model."),
 keys=["RNs, LPNs, CNAs in ratios allowing real care",
  "Higher staffing predicts better outcomes",
  "Consistent assignment strongly linked to quality",
  "Understaffing and turnover are the central problem",
  "Staffing data publicly reported for nursing homes",
  "Never silently understaff"],
 reqs=["Acuity-based staffing targets",
  "Recruitment and retention investment",
  "Consistent-assignment scheduling"],
 stds=["CMS staffing reporting (PBJ) (public)",
  "State minimum staffing rules"],
 cites=["Centers for Medicare and Medicaid Services — staffing data (public)",
  "National Academies — nursing home workforce research (public)"],
 demo=("staffing", {"residents": 60, "staff": 9, "max_ratio": 8})),

dict(title="Safety Systems and Monitoring", tier=C,
 desc_pub=("Safety systems protect vulnerable elders: fall-detection sensors, wander-management "
  "for dementia units, emergency call systems, medication dispensers with alerts, stove shut-offs, "
  "and remote monitoring for those living alone. The ethical line is clear: safety technology "
  "supports independence; it must not become surveillance that strips privacy or replaces human "
  "contact.\n"
  "Best practice pairs technology with consent - the older adult (or their representative) "
  "chooses what is monitored - and with human response: alerts must reach someone who acts."),
 desc_sig=("Signature safety design starts from consent profiles: what is monitored, who is "
  "alerted, and when - configured with the older adult, keeping safety technology firmly in "
  "service of autonomy."),
 how_pub=("Assessment identifies risks - falls, wandering, medication errors - and matches "
  "technology with the person's consent. Systems are installed, tested, and explained; alert "
  "chains name responders and backup. Regular review ensures technology still fits and still has "
  "consent."),
 how_sig=("Signature consent profiles make the ethical line operational: monitoring exists only "
  "where the person agreed it should."),
 keys=["Fall detection, wander management, call systems, med dispensers",
  "Technology supports independence; not surveillance",
  "Consent governs what is monitored",
  "Alerts must reach someone who acts",
  "Pair tech with human contact, not replacement",
  "Review fit and consent regularly"],
 reqs=["Risk assessment per person",
  "Consent documentation",
  "Tested alert chains with responders"],
 stds=["Device safety standards (public)",
  "Privacy expectations for monitoring"],
 cites=["National Institute on Aging — home safety technology (public)"],
 demo=("safety", {"items": [
   {"item": "Emergency call system tested", "ok": True},
   {"item": "Alert chain has backup responder", "ok": False},
   {"item": "Consent documented for monitoring", "ok": True},
   {"item": "Medication dispenser alerts active", "ok": True}]})),

dict(title="Infection Control in Facilities", tier=C,
 desc_pub=("Infection control in elder-care facilities protects a highly vulnerable population: "
  "hand hygiene, personal protective equipment, isolation protocols, vaccination programs, "
  "environmental cleaning, and antibiotic stewardship. COVID-19 revealed how quickly infections "
  "move through congregate settings - and how much disciplined practice matters.\n"
  "Programs need a designated infection preventionist, surveillance for outbreaks, and a culture "
  "where any worker can stop an unsafe practice. Families deserve transparent outbreak "
  "communication."),
 desc_sig=("Signature infection control runs continuous surveillance dashboards - symptoms, "
  "testing, staffing illness - so outbreaks are caught in hours, not weeks."),
 how_pub=("Facilities appoint an infection preventionist, train all staff in hand hygiene and PPE, "
  "and run surveillance for clusters. Outbreak protocols isolate, test, cohort staff, and notify "
  "families and health departments. Vaccination clinics cover residents and staff yearly."),
 how_sig=("Signature surveillance dashboards flag symptom clusters automatically, triggering "
  "protocol before spread."),
 keys=["Hand hygiene, PPE, isolation, vaccination, cleaning, stewardship",
  "Designated infection preventionist",
  "Surveillance catches outbreaks early",
  "Culture where anyone can stop unsafe practice",
  "Transparent family communication",
  "COVID-19 proved disciplined practice matters"],
 reqs=["Infection preventionist role",
  "PPE supply and training",
  "Outbreak response protocols"],
 stds=["CDC infection-control guidance for long-term care (public)",
  "CMS infection-control requirements (public regulation)"],
 cites=["Centers for Disease Control — long-term care infection control (public)",
  "Centers for Medicare and Medicaid Services — requirements (public)"],
 demo=("outcome", {"label": "Staff hand-hygiene compliance", "pre": 64, "post": 93})),

dict(title="Resident Rights and Advocacy", tier=C,
 desc_pub=("Residents of care facilities hold strong rights: to dignity and respect, to participate "
  "in care decisions, to voice grievances without retaliation, to visitors of their choosing, to "
  "manage their own money, and to be free from abuse, neglect, and restraints. Federal nursing "
  "home law codifies these; states extend similar protections to assisted living.\n"
  "Long-term care ombudsmen investigate complaints and advocate for residents - a free, "
  "confidential resource in every state. Family councils amplify resident voices collectively."),
 desc_sig=("Signature rights protection makes rights visible: posted plainly, reviewed at "
  "admission and regularly after, with grievance tracking that proves complaints lead to "
  "action."),
 how_pub=("Facilities inform residents of rights at admission and post them plainly. Grievances "
  "are logged, investigated promptly, and resolved with the resident's participation. Ombudsmen "
  "visit, investigate complaints, and mediate. Family councils meet with administration "
  "regularly."),
 how_sig=("Signature grievance tracking shows every complaint's status and resolution, making "
  "accountability visible."),
 keys=["Dignity, choice, grievances without retaliation, visitors, funds control",
  "Freedom from abuse, neglect, restraints",
  "Federal law for nursing homes; state laws vary for assisted living",
  "Ombudsmen: free, confidential advocates in every state",
  "Family councils amplify voices",
  "Rights posted plainly and reviewed regularly"],
 reqs=["Rights notification at admission",
  "Grievance logging and resolution process",
  "Ombudsman access"],
 stds=["Federal nursing home resident rights (public law)",
  "Older Americans Act ombudsman program (public law)"],
 cites=["National Consumer Voice for Quality Long-Term Care — public resources (public)",
  "Administration for Community Living — ombudsman program (public)"],
 demo=("safety", {"items": [
   {"item": "Rights posted in plain language", "ok": True},
   {"item": "Grievance log reviewed monthly", "ok": False},
   {"item": "Ombudsman contact posted", "ok": True},
   {"item": "Family council meets quarterly", "ok": True}]})),

dict(title="Hospice and Palliative Services", tier=C,
 desc_pub=("Palliative care relieves suffering for serious illness at any stage; hospice is "
  "palliative care focused on comfort in the final months of life. Both use interdisciplinary "
  "teams - doctors, nurses, social workers, chaplains, aides, volunteers - addressing pain, "
  "symptoms, emotional and spiritual needs, and family support.\n"
  "Hospice is a Medicare benefit for those with a prognosis of six months or less who choose "
  "comfort over curative treatment - yet most enroll far too late to benefit fully. Earlier "
  "referral means better quality of remaining life."),
 desc_sig=("Signature serious-illness design triggers goals-of-care conversations at diagnosis of "
  "serious illness rather than in crisis, so palliative and hospice referrals happen when they "
  "can help most."),
 how_pub=("A prognosis or goals-of-care conversation leads to referral; the team assesses symptoms, "
  "values, and family needs, then delivers comfort-focused care wherever the person lives. "
  "Bereavement support continues for families after death - typically thirteen months in hospice."),
 how_sig=("Signature conversation triggers ensure serious-illness discussions happen upstream, not "
  "in the emergency department."),
 keys=["Palliative: relief at any stage; hospice: comfort in final months",
  "Interdisciplinary teams: medical, social, spiritual, volunteer",
  "Hospice is a Medicare benefit (6-month prognosis)",
  "Most enroll too late - earlier is better",
  "Bereavement support for families after",
  "Comfort chosen over curative treatment"],
 reqs=["Goals-of-care conversation capacity",
  "Interdisciplinary team",
  "Bereavement program"],
 stds=["Medicare hospice conditions of participation (public)",
  "National Consensus Project palliative guidelines (public)"],
 cites=["Centers for Medicare and Medicaid Services — hospice benefit (public)",
  "National Hospice and Palliative Care Organization — public resources (public)"],
 demo=("outcome", {"label": "Families rating end-of-life care excellent", "pre": 68, "post": 89})),

dict(title="Transportation for Older Adults", tier=C,
 desc_pub=("Losing the ability to drive threatens independence - yet driving must stop when it "
  "becomes unsafe. Older-adult transportation options include senior transit, volunteer driver "
  "programs, ride subsidies, ADA paratransit, and non-emergency medical transportation.\n"
  "Driving retirement deserves planning, not crisis: assessments of fitness to drive, gradual "
  "transition plans, and alternative transportation lined up before keys are surrendered. "
  "Mobility managers in many communities coordinate the options."),
 desc_sig=("Signature transportation coordination gives each non-driving elder a personal mobility "
  "plan - medical rides, social trips, errands - booked through one interface."),
 how_pub=("Families and clinicians watch for warning signs and arrange driving evaluations when "
  "needed. Mobility managers or counselors map alternatives - transit, volunteers, subsidies - and "
  "build a weekly transportation plan covering medical, shopping, and social trips. Plans are "
  "tested before driving stops."),
 how_sig=("Signature personal mobility plans cover the full week of trips, not just medical "
  "rides."),
 keys=["Driving cessation threatens independence; plan the transition",
  "Options: senior transit, volunteers, subsidies, paratransit, NEMT",
  "Assess fitness to drive objectively",
  "Line up alternatives before keys are surrendered",
  "Mobility managers coordinate options",
  "Cover social trips, not just medical"],
 reqs=["Driving evaluation access",
  "Mobility management or counseling",
  "Weekly transportation planning"],
 stds=["State driver licensing medical review rules (public)",
  "FTA senior transportation program rules (public)"],
 cites=["National Aging and Disability Transportation Center — public resources (public)",
  "American Occupational Therapy Association — driving resources (public)"],
 demo=("compare", {"options": [
   {"name": "Volunteer driver program", "score": 8, "note": "door-through-door help"},
   {"name": "Senior transit", "score": 7, "note": "scheduled routes"},
   {"name": "Family only", "score": 4, "note": "fragile, burdensome"}]})),

dict(title="Measuring Service Quality", tier=C,
 desc_pub=("Elder-care quality is measured across clinical outcomes (pressure injuries, falls with "
  "injury, infections), resident experience (satisfaction, dignity, choice), staffing (ratios, "
  "turnover), and process compliance (care plans current, assessments timely). Public reporting - "
  "CMS Care Compare star ratings - lets families compare.\n"
  "The balanced view matters: a facility can ace paperwork while residents feel invisible. "
  "Resident and family voice - councils, surveys, ombudsman data - belongs at the center of "
  "every quality system."),
 desc_sig=("Signature quality systems fuse clinical, staffing, and experience data into one "
  "resident-centered scorecard per setting, so improvement targets what residents actually "
  "experience."),
 how_pub=("Providers select measures across the domains, collect data routinely, and review "
  "dashboards in quality meetings. Gaps trigger improvement projects with assigned owners. "
  "Results are shared with residents, families, and (where required) public reporting systems."),
 how_sig=("Signature fused scorecards prevent the paperwork-excellent / experience-poor split by "
  "weighting resident voice heavily."),
 keys=["Clinical outcomes, experience, staffing, process compliance",
  "CMS Care Compare star ratings are public",
  "Balance paperwork metrics with lived experience",
  "Resident and family voice at the center",
  "Gaps trigger owned improvement projects",
  "Share results transparently"],
 reqs=["Measure set across domains",
  "Routine data collection and dashboards",
  "Improvement project discipline"],
 stds=["CMS quality reporting requirements (public)",
  "State quality program rules"],
 cites=["Centers for Medicare and Medicaid Services — quality measures (public)",
  "National Consumer Voice — quality resources (public)"],
 demo=("outcome", {"label": "Residents rating care good or excellent", "pre": 71, "post": 90})),

# ---------------- Advanced (11) ----------------
dict(title="Memory Care Unit Operations", tier=A,
 desc_pub=("Memory care units are secured settings designed for people with dementia: small scale, "
  "consistent staff, structured days, wander-safe layouts, and staff trained deeply in dementia "
  "communication. The environment does therapeutic work - clear sightlines, familiar cues, reduced "
  "noise, outdoor access.\n"
  "Quality markers: low staff turnover, high training hours, individualized activity, family "
  "partnership, and minimal use of antipsychotics for behavioral expression. This record is "
  "educational; placement decisions are clinical and personal."),
 desc_sig=("Signature memory-care operations standardize the therapeutic environment checklist and "
  "staff-dementia-competency verification, so quality is built into operations rather than "
  "depending on heroic individuals."),
 how_pub=("Assessment confirms dementia-care need; families tour units checking staffing, training, "
  "activity, and safety. Move-in includes life-history intake feeding the care plan. Daily "
  "operations run structured, flexible days; families are partners with regular communication. "
  "Antipsychotic use is reviewed against strict criteria."),
 how_sig=("Signature environment and competency checklists make therapeutic operations auditable."),
 keys=["Secured, small-scale, dementia-designed settings",
  "Environment does therapeutic work",
  "Consistent, deeply trained staff",
  "Individualized meaningful activity",
  "Minimal antipsychotic use for behaviors",
  "Family as partner"],
 reqs=["Dementia-specific licensing (where required)",
  "High training hours and low turnover",
  "Wander-safe physical design"],
 stds=["State memory-care regulations (public)",
  "Alzheimer's Association practice recommendations (public)"],
 cites=["Alzheimer's Association — memory care guidance (public)"],
 demo=("safety", {"items": [
   {"item": "Secured exits with wander paths", "ok": True},
   {"item": "All direct staff dementia-certified", "ok": False},
   {"item": "Individual activity plans current", "ok": True},
   {"item": "Antipsychotic use reviewed quarterly", "ok": True}]})),

dict(title="Person-Centered Dementia Care Plans", tier=A,
 desc_pub=("Person-centered dementia care plans translate life history into daily practice: the "
  "person's routines, preferences, triggers, soothing strategies, and remaining abilities become "
  "specific instructions for every caregiver. 'Mrs. Alvarez becomes anxious at sundown; familiar "
  "boleros and a walk to the garden calm her' beats 'manage agitation.'\n"
  "Plans are living documents updated as dementia progresses, with families contributing knowledge "
  "staff cannot observe in a facility. Consistency across caregivers is the mechanism - the plan "
  "only works if everyone follows it."),
 desc_sig=("Signature dementia care plans are structured, searchable, and pushed to caregivers' "
  "daily task views - so personal knowledge survives shift changes and staff turnover."),
 how_pub=("Life-history interviews with family produce the profile; the interdisciplinary team "
  "writes specific, actionable guidance per routine and situation. Caregivers are trained on the "
  "plan; adherence is observed. Families review and update regularly as abilities change."),
 how_sig=("Signature plan-to-task integration puts personal guidance where caregivers actually "
  "look: their daily assignments."),
 keys=["Life history becomes daily practice",
  "Specific instructions beat vague labels",
  "Update as dementia progresses",
  "Families contribute irreplaceable knowledge",
  "Consistency across caregivers is the mechanism",
  "Living documents, not filed paperwork"],
 reqs=["Life-history interview process",
  "Interdisciplinary plan authorship",
  "Adherence observation"],
 stds=["Person-centered dementia care standards (public literature)"],
 cites=["Alzheimer's Association — care planning (public)"],
 demo=("outcome", {"label": "Caregivers following plan consistently", "pre": 58, "post": 91})),

dict(title="Staff Training and Retention", tier=A,
 desc_pub=("Direct-care workers - CNAs, home health aides - do the intimate work of elder care for "
  "low wages and thin recognition, and turnover often exceeds 50 percent annually. Training and "
  "retention are therefore quality strategies, not HR niceties.\n"
  "What works: thorough onboarding, dementia and communication skills training, career ladders "
  "(CNA to med-tech to LPN), consistent assignment, recognition, competitive pay and benefits, "
  "and supervisors who coach rather than merely schedule."),
 desc_sig=("Signature workforce systems track training completion, competency verification, and "
  "early-turnover signals per team, letting leaders invest where retention is won or lost."),
 how_pub=("Organizations build onboarding academies, deliver ongoing skills training tied to "
  "resident needs, create advancement pathways, and measure turnover by unit monthly. Stay "
  "interviews surface issues before exit interviews do. Wages and benefits are benchmarked "
  "competitively."),
 how_sig=("Signature unit-level turnover dashboards make retention a managed metric, not a "
  "surprise."),
 keys=["Turnover often exceeds 50 percent - a quality crisis",
  "Training and retention are quality strategies",
  "Onboarding, dementia skills, career ladders",
  "Consistent assignment aids retention and care",
  "Stay interviews beat exit interviews",
  "Benchmark pay competitively"],
 reqs=["Onboarding and ongoing training programs",
  "Career ladder pathways",
  "Unit-level turnover tracking"],
 stds=["State training-hour requirements (public)",
  "CMS training expectations"],
 cites=["Paraprofessional Healthcare Institute — workforce research (public)"],
 demo=("outcome", {"label": "Annual direct-care retention", "pre": 52, "post": 76})),

dict(title="Regulatory Surveys and Compliance", tier=A,
 desc_pub=("Care settings face regular inspections - surveys - checking compliance with hundreds "
  "of federal and state requirements. Nursing homes get unannounced annual surveys plus complaint "
  "investigations; deficiencies are graded by scope and severity, with serious ones triggering "
  "penalties and public reporting.\n"
  "Compliance as culture beats compliance as panic: continuous readiness - audits, drills, "
  "plan-of-correction discipline - produces better surveys and better care than cramming. "
  "Transparency matters: families should read survey reports before choosing."),
 desc_sig=("Signature compliance operations run continuous mock-survey cycles with deficiency "
  "tracking, so readiness is a steady state rather than a pre-inspection scramble."),
 how_pub=("Quality teams run internal audits against the survey protocol, fix gaps with tracked "
  "plans of correction, and drill emergency and clinical procedures. When surveyors arrive, staff "
  "answer from practiced knowledge. Deficiencies get root-cause correction, not just paperwork."),
 how_sig=("Signature continuous-readiness tracking keeps every requirement's evidence current."),
 keys=["Unannounced surveys check hundreds of requirements",
  "Deficiencies graded by scope and severity",
  "Continuous readiness beats pre-inspection panic",
  "Plans of correction need root-cause discipline",
  "Families should read survey reports",
  "Compliance culture is care culture"],
 reqs=["Internal audit against survey protocol",
  "Plan-of-correction tracking",
  "Staff survey-readiness training"],
 stds=["CMS State Operations Manual (public)",
  "State survey protocols"],
 cites=["Centers for Medicare and Medicaid Services — survey guidance (public)"],
 demo=("outcome", {"label": "Deficiency-free surveys", "pre": 61, "post": 85})),

dict(title="Technology in Elder Care", tier=A,
 desc_pub=("Technology is reshaping elder care: telehealth for rural access, remote monitoring for "
  "safety, medication dispensers, socially assistive robots for engagement, AI-assisted fall "
  "detection, and family communication platforms. Done well, technology extends independence and "
  "eases workforce strain.\n"
  "The guardrails: consent, privacy, human contact preserved, and design with older adults - not "
  "imposed on them. Technology that confuses its users fails no matter how clever its engineering."),
 desc_sig=("Signature elder-care technology assessment scores tools on usability with older "
  "adults, privacy, and workforce impact - admitting only technology that serves dignity."),
 how_pub=("Organizations assess needs technology could address, pilot with willing users, measure "
  "usability and outcomes, and scale what works. Training covers both staff and older adults; "
  "privacy reviews precede deployment. Human contact metrics guard against substitution."),
 how_sig=("Signature usability-first evaluation keeps older adults as the judges of elder-care "
  "technology."),
 keys=["Telehealth, monitoring, dispensers, engagement tech, family platforms",
  "Extends independence; eases workforce strain",
  "Guardrails: consent, privacy, human contact",
  "Design with older adults, not for them",
  "Pilot, measure, then scale",
  "Confusing technology fails regardless of cleverness"],
 reqs=["Needs assessment for technology fit",
  "Pilot and usability measurement",
  "Privacy review process"],
 stds=["Emerging health-AI guidance (public literature)",
  "Accessibility standards for older users"],
 cites=["National Institute on Aging — technology research (public)"],
 demo=("compare", {"options": [
   {"name": "Video visit platform (simple UI)", "score": 9, "note": "older-adult tested"},
   {"name": "Fall-detection sensors", "score": 8, "note": "consented monitoring"},
   {"name": "Complex app (no training)", "score": 3, "note": "usability failure"}]})),

dict(title="Intergenerational Programs", tier=A,
 desc_pub=("Intergenerational programs bring older adults and young people together - shared sites "
  "(preschool in a nursing home), mentoring, oral-history projects, tech tutoring both ways. "
  "Evidence shows benefits both directions: elders gain purpose and cognitive engagement; youth "
  "gain empathy and perspective.\n"
  "Good programs are designed, not just co-located: shared activities with real roles for both "
  "generations, trained facilitators, and attention to safety and developmental fit."),
 desc_sig=("Signature intergenerational design builds activity curricula with genuine reciprocal "
  "roles, measured on engagement for both generations."),
 how_pub=("Organizations partner across generations - schools with senior centers - and design "
  "activities where each group contributes. Facilitators are trained in both age groups' needs; "
  "schedules are reliable; outcomes track well-being and attitudes on both sides."),
 how_sig=("Signature reciprocal-role design ensures neither generation is merely an audience."),
 keys=["Shared sites, mentoring, history projects, mutual tutoring",
  "Benefits flow both directions",
  "Designed programs, not mere co-location",
  "Real roles for both generations",
  "Trained facilitators",
  "Measure outcomes on both sides"],
 reqs=["Cross-generation partnerships",
  "Facilitator training",
  "Safety and fit planning"],
 stds=["Intergenerational practice standards (public literature)"],
 cites=["Generations United — public resources (public)"],
 demo=("outcome", {"label": "Participants reporting meaningful connection", "pre": 55, "post": 89})),

dict(title="Elder Abuse Prevention and Response", tier=A,
 desc_pub=("Elder abuse - physical, emotional, sexual, financial exploitation, neglect, "
  "abandonment - affects millions of older adults, most often by family members or trusted "
  "others. Prevention includes caregiver support (reducing the stress that precipitates abuse), "
  "financial safeguards, social connection (isolation enables abuse), and professional training "
  "in recognition.\n"
  "Response: every state has adult protective services (APS) investigating reports; many have "
  "mandatory reporting laws for professionals. If someone is in immediate danger, call emergency "
  "services."),
 desc_sig=("Signature elder-justice design links APS, law enforcement, financial institutions, "
  "and health providers in coordinated response teams, so exploitation cases get the "
  "multidisciplinary response they need."),
 how_pub=("Professionals are trained to recognize signs - bruises, fear, sudden financial changes, "
  "neglect - and report to APS or law enforcement per state law. APS investigates, assesses "
  "risk, and arranges protective services with the adult's participation to the extent possible. "
  "Multidisciplinary teams coordinate complex cases."),
 how_sig=("Signature coordinated response teams give financial-exploitation cases the joint "
  "attention they require."),
 keys=["Forms: physical, emotional, sexual, financial, neglect, abandonment",
  "Most often by family or trusted others",
  "Prevention: caregiver support, safeguards, connection, training",
  "APS investigates in every state",
  "Mandatory reporting for professionals in many states",
  "Immediate danger: call emergency services"],
 reqs=["Recognition training for all elder-care staff",
  "APS reporting knowledge",
  "Multidisciplinary team partnerships"],
 stds=["State APS statutes (public)",
  "Elder Justice Act provisions (public law)"],
 cites=["National Center on Elder Abuse — public resources (public)",
  "Administration for Community Living — elder justice (public)"],
 demo=("safety", {"items": [
   {"item": "All staff trained in abuse recognition", "ok": False},
   {"item": "APS reporting procedure posted", "ok": True},
   {"item": "Financial-exploitation safeguards", "ok": False},
   {"item": "Isolation-risk screening", "ok": True}]})),

dict(title="Continuing Care Retirement Communities", tier=A,
 desc_pub=("Continuing care retirement communities (CCRCs) bundle independent living, assisted "
  "living, and nursing care on one campus with a contract promising care as needs grow. Entry "
  "typically requires a large entrance fee plus monthly charges - buying peace of mind about "
  "future care.\n"
  "Contracts vary enormously (all-inclusive vs. fee-for-service), and financial scrutiny is "
  "essential: the promise spans decades, so the community's fiscal health matters as much as its "
  "dining room. State regulations require disclosures; some states mandate actuarial reviews."),
 desc_sig=("Signature CCRC evaluation scores contract fairness, fee transparency, and long-term "
  "financial viability side by side - the three factors that determine whether the promise "
  "holds."),
 how_pub=("Prospective residents compare contract types, tour all care levels, review audited "
  "financials and disclosure documents, and consult elder-law attorneys and financial advisors. "
  "Residents move between levels on the same campus as needs change, with care coordinated "
  "internally."),
 how_sig=("Signature contract-viability scoring makes the decades-long promise legible before "
  "signing."),
 keys=["Independent + assisted + nursing on one campus",
  "Entrance fee + monthly charges",
  "Contract types vary: all-inclusive to fee-for-service",
  "Financial viability matters as much as amenities",
  "Review audited financials and disclosures",
  "Consult elder-law and financial advisors"],
 reqs=["State CCRC disclosure compliance",
  "Audited financial statements",
  "Independent legal and financial advice"],
 stds=["State CCRC regulations (public)"],
 cites=["State insurance/aging department CCRC guides (public)"],
 demo=("compare", {"options": [
   {"name": "Type A (all-inclusive)", "score": 8, "note": "predictable, higher entry fee"},
   {"name": "Type B (modified)", "score": 7, "note": "some included care"},
   {"name": "Type C (fee-for-service)", "score": 5, "note": "lower entry, pay as needs grow"}]})),

dict(title="PACE and Integrated Care Models", tier=A,
 desc_pub=("PACE (Program of All-Inclusive Care for the Elderly) fully integrates medical and "
  "long-term care for frail elders who qualify for nursing-home level care but live in the "
  "community. One interdisciplinary team manages everything - primary care, therapies, day "
  "center, home care, hospital, nursing home - under a fixed monthly payment.\n"
  "The integration eliminates the fragmentation that harms complex patients: one team, one "
  "record, aligned incentives to keep people healthy at home. Outcomes include lower "
  "hospitalization and high satisfaction."),
 desc_sig=("Signature integrated-care design extends the PACE logic - one team, aligned "
  "incentives, full accountability - as the template for all complex elder care."),
 how_pub=("Eligible elders enroll through a PACE organization; the team assesses comprehensively "
  "and builds one plan covering all needs. Day centers provide medical, therapy, and social "
  "services; home care fills gaps. The team coordinates every hospitalization and transition."),
 how_sig=("Signature single-accountability models make one team answerable for the whole "
  "person's outcomes."),
 keys=["Fully integrates medical + long-term care",
  "For nursing-home-eligible elders living in community",
  "One team manages everything",
  "Fixed monthly payment aligns incentives",
  "Eliminates fragmentation",
  "Lower hospitalization, high satisfaction"],
 reqs=["PACE organization certification",
  "Interdisciplinary team with full scope",
  "Day center and home-care capacity"],
 stds=["CMS PACE regulations (public)"],
 cites=["Centers for Medicare and Medicaid Services — PACE (public)",
  "National PACE Association — public resources (public)"],
 demo=("outcome", {"label": "Participants avoiding hospitalization (annual)", "pre": 62, "post": 81})),

dict(title="End-of-Life Planning Services", tier=A,
 desc_pub=("End-of-life planning services help people document wishes while they can: advance "
  "directives (living wills, health care proxies), POLST/MOLST orders for serious illness, "
  "financial powers of attorney, wills and trusts, and funeral planning. Conversations matter as "
  "much as documents - families need to hear values and priorities directly.\n"
  "Clinicians, social workers, attorneys, and faith leaders each play roles. The tragedy to avoid "
  "is the ICU family meeting where no one knows what the person wanted."),
 desc_sig=("Signature advance-care planning treats wishes as structured, shareable records - "
  "updated over time, accessible to every care setting - so documented wishes actually guide "
  "care in the moment."),
 how_pub=("Trained facilitators - in clinics, aging agencies, or community workshops - guide "
  "conversations about values, then help complete legal documents. Copies go to proxies, "
  "clinicians, and the record; reviews happen yearly or after health changes. POLST orders are "
  "completed with clinicians for the seriously ill."),
 how_sig=("Signature shareable advance-care records ensure wishes are visible wherever care "
  "happens."),
 keys=["Advance directives, POLST, powers of attorney, wills, funeral plans",
  "Conversations matter as much as documents",
  "Document while decision-capable",
  "Share with proxies, clinicians, records",
  "Review yearly or after health changes",
  "Avoid the ICU meeting where no one knows"],
 reqs=["Trained facilitators",
  "Legally valid document templates per state",
  "Sharing with care teams"],
 stds=["State advance-directive statutes (public)",
  "POLST paradigm standards (public)"],
 cites=["National Hospice and Palliative Care Organization — planning resources (public)",
  "American Bar Association — advance directives toolkit (public)"],
 demo=("outcome", {"label": "Adults with documented advance directives", "pre": 37, "post": 72})),

dict(title="The Future of Aging Services", tier=A,
 desc_pub=("Aging services face a demographic wave: by 2034, older adults will outnumber children "
  "in the U.S. for the first time. The future points toward home-first systems, dementia-capable "
  "communities, age-friendly health systems (the 4Ms: What Matters, Medication, Mentation, "
  "Mobility), technology-supported independence, and a professionalized, well-paid direct-care "
  "workforce.\n"
  "The through-line is preference: systems built around what older adults want - independence, "
  "connection, purpose - rather than around institutional convenience."),
 desc_sig=("The Signature future-state is an aging operating system: one preference-driven plan, "
  "one coordinated team, one quality spine across home and facility - with the older adult as "
  "the system's purpose and director. This database is a prototype of that system's knowledge "
  "core."),
 how_pub=("Systems invest in home- and community-based capacity, adopt age-friendly frameworks, "
  "deploy supportive technology with consent, and professionalize the workforce with better pay "
  "and ladders. Older adults co-design every innovation; outcomes center what matters to them."),
 how_sig=("Signature's preference-driven operating vision makes the older adult the system's "
  "director by design."),
 keys=["Demographic wave: elders outnumber children by 2034 (U.S.)",
  "Home-first systems and dementia-capable communities",
  "Age-friendly health systems: the 4Ms",
  "Technology with consent",
  "Professionalized, well-paid workforce",
  "Built around older adults' preferences"],
 reqs=["Home- and community-based capacity investment",
  "Age-friendly framework adoption",
  "Workforce professionalization"],
 stds=["Age-Friendly Health Systems framework (public)",
  "WHO age-friendly cities guidance (public)"],
 cites=["Institute for Healthcare Improvement — Age-Friendly Health Systems (public)",
  "World Health Organization — ageing resources (public)"],
 demo=("outcome", {"label": "Older adults aging in preferred setting", "pre": 58, "post": 83})),
]
