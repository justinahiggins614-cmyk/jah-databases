#!/usr/bin/env python3
"""Topics + config for the dispute-resolution pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never legal advice.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

LEGAL_NOTE = "Educational information only — not legal advice. Consult a licensed attorney for personal matters."

CFG = {
    "slug": "dispute-resolution",
    "name_pub": "The Dispute Resolution Database",
    "name_sig": "Signature Dispute Resolution Database",
    "tagline_pub": ("Dispute resolution from the ground up: negotiation, mediation, arbitration, "
                    "and other paths - procedures step by step, decisions and enforceability, "
                    "jurisdiction by jurisdiction - every record carrying the full entry taught "
                    "progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of dispute resolution: the same "
                    "real resolution knowledge carried forward, plus Signature-built procedure "
                    "models, enforceability frameworks, and system designs original to this "
                    "system."),
    "record_kind": "dispute resolution record",
    "record_kind_plural": "dispute resolution records",
    "prefix_pub": "JAH-DISPR-", "prefix_sig": "JAH-DISPRS-",
    "ai_pub": "JAH Dispute Resolution Archivist",
    "ai_sig": "JAH Signature Dispute Resolution Creator",
    "role_pub": ("dispute resolution archivist - teaching resolution paths, procedures, "
                 "mediation approaches, decisions, and enforceability; answers from many angles - "
                 "definition, example, process, procedure, enforcement - using only archive data "
                 "from this system"),
    "role_sig": ("Signature creator of dispute resolution systems - designing procedure models, "
                 "enforceability frameworks, and resolution systems as original Signature works; "
                 "answers from many angles using only archive data from this system"),
    "search_ph": "Search mediation, arbitration, negotiation, enforceability, jurisdictions...",
    "chat_ph": "Ask about dispute resolution...",
    "greet_pub": ("I am the JAH Dispute Resolution Archivist. Ask me about resolution paths, "
                  "procedures, mediation approaches, and enforceability. " + LEGAL_NOTE),
    "greet_sig": ("I am the JAH Signature Dispute Resolution Creator. Ask me about "
                  "Signature-built resolution systems. " + LEGAL_NOTE),
    "gen_blurb": ("Generate clearly-labeled dispute resolution studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded dispute resolution records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. " +
                      LEGAL_NOTE),
    "demo_kind": "dispute-demo",
    "demo_title": "Dispute Resolution Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Dispute Resolution Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "pathway":
        return fill(
            "dispute = @@DISP@@\npaths = @@PATHS@@\n"
            "print('Dispute:', dispute)\n"
            "rank = {'court': 3, 'arbitration': 2, 'mediation': 1, 'negotiation': 0}\n"
            "ordered = sorted(paths, key=lambda x: rank.get(x['path'], 9))\n"
            "print('Paths from least to most formal:')\n"
            "for x in ordered:\n"
            "    print(' - %s: %s' % (x['path'], x['note']))\n",
            {"DISP": p["dispute"], "PATHS": p["paths"]})
    if v == "timeline":
        return fill(
            "stages = @@STAGES@@\n"
            "total = sum(s['days'] for s in stages)\n"
            "print('Procedure timeline:')\n"
            "for s in stages:\n"
            "    print(' - %s: ~%d days' % (s['stage'], s['days']))\n"
            "print('Estimated total: ~%d days' % total)\n",
            {"STAGES": p["stages"]})
    if v == "enforce":
        return fill(
            "award = @@AWARD@@\njuris = @@JURIS@@\n"
            "print('Award:', award)\n"
            "ok = [j for j in juris if j['enforceable']]\n"
            "print('Enforceable in %d/%d jurisdictions:' % (len(ok), len(juris)))\n"
            "for j in juris:\n"
            "    print(' [%s] %s: %s' % ('YES' if j['enforceable'] else 'NO', j['jurisdiction'], j['basis']))\n",
            {"AWARD": p["award"], "JURIS": p["jurisdictions"]})
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
dict(title="What Dispute Resolution Is", tier=F,
 desc_pub=("Dispute resolution is the set of processes for settling disagreements: negotiation "
  "(parties talk directly), mediation (a neutral helps them agree), arbitration (a neutral "
  "decides), and litigation (courts decide) - plus hybrids like med-arb and ombuds programs. "
  "Alternative dispute resolution (ADR) covers everything outside courts.\n"
  "The field's promise: faster, cheaper, more private, and more relationship-preserving than "
  "litigation - when matched to the right dispute. Choosing the path is itself a strategic "
  "decision."),
 desc_sig=("The Signature system models dispute resolution as a path-selection engine: dispute "
  "characteristics scored against each process's strengths, recommending the fitting path "
  "transparently."),
 how_pub=("Parties (or their lawyers) assess the dispute - stakes, relationship, power balance, "
  "need for precedent - and choose a path. Many contracts pre-select arbitration or mediation. "
  "Courts increasingly require mediation attempts before trial."),
 how_sig=("Signature path-selection scoring makes the choice explicit and reviewable."),
 keys=["Negotiation, mediation, arbitration, litigation, hybrids",
  "ADR: everything outside courts",
  "Promise: faster, cheaper, private, relationship-preserving",
  "Match process to dispute",
  "Contracts often pre-select paths",
  "Courts often require mediation first"],
 reqs=["Dispute characterization",
  "Knowledge of each path's mechanics",
  "Neutral rosters where needed"],
 stds=["ADR practice standards (public literature)",
  "Court ADR program rules (public)"],
 cites=["American Arbitration Association — public resources (public)",
  "American Bar Association — dispute resolution (public)"],
 demo=("pathway", {"dispute": "Contract payment disagreement, ongoing business relationship",
   "paths": [{"path": "negotiation", "note": "direct, preserves relationship"},
             {"path": "mediation", "note": "neutral helps; still collaborative"},
             {"path": "arbitration", "note": "binding decision, private"},
             {"path": "court", "note": "public, precedent, slowest"}]})),

dict(title="Types of Disputes", tier=F,
 desc_pub=("Disputes sort by subject: commercial (contracts, partnerships), consumer (products, "
  "services), employment (wages, discrimination, termination), family (divorce, custody), "
  "property and construction, personal injury, and public/international disputes.\n"
  "Each type has typical paths: family disputes favor mediation (relationships continue), "
  "consumer disputes favor ombuds and small claims (low stakes), complex commercial disputes "
  "favor arbitration (expertise, privacy). Typing guides path choice."),
 desc_sig=("Signature dispute typing attaches path recommendations and typical timelines per "
  "type, so parties start with realistic expectations."),
 how_pub=("Intake classifies the dispute by subject, stakes, parties, and relationship future. "
  "The classification suggests paths; parties choose with advice. Specialized programs "
  "(family mediation, construction boards) exist for high-volume types."),
 how_sig=("Signature typed recommendations give parties realistic path and timeline "
  "expectations at intake."),
 keys=["Commercial, consumer, employment, family, property, injury, public",
  "Family: mediation (relationships continue)",
  "Consumer: ombuds, small claims",
  "Complex commercial: arbitration",
  "Typing guides path choice",
  "Specialized programs for high-volume types"],
 reqs=["Dispute classification",
  "Path knowledge per type",
  "Specialized program referrals"],
 stds=["Court jurisdictional limits (public)"],
 cites=["American Bar Association — dispute types (public)"],
 demo=("pathway", {"dispute": "Divorce with children, co-parenting future",
   "paths": [{"path": "negotiation", "note": "direct talks"},
             {"path": "mediation", "note": "best fit: preserves co-parenting"},
             {"path": "court", "note": "for impasse or safety issues"}]})),

dict(title="Negotiation Basics", tier=F,
 desc_pub=("Negotiation is direct deal-making between parties: prepare (interests, alternatives, "
  "walk-away), exchange information and offers, problem-solve around interests, and close with "
  "clear agreement. Principled negotiation (Getting to Yes) separates people from problems and "
  "invents options before dividing value.\n"
  "Your BATNA (best alternative to negotiated agreement) is your power: the better your walk-"
  "away, the better your deal. Most disputes settle in negotiation - skill here pays "
  "everywhere."),
 desc_sig=("Signature negotiation preparation builds structured briefs - interests, BATNA, "
  "options, concessions planned - so negotiators enter prepared, not improvising."),
 how_pub=("Negotiators prepare interests and BATNAs, open with information exchange, explore "
  "options satisfying both sides' interests, trade concessions strategically, and document "
  "agreements precisely. Lawyers advise; clients decide."),
 how_sig=("Signature structured briefs make preparation systematic and complete."),
 keys=["Prepare, exchange, problem-solve, close",
  "Separate people from problems",
  "BATNA is your power",
  "Interests unlock options; positions divide value",
  "Most disputes settle here",
  "Document agreements precisely"],
 reqs=["Preparation discipline",
  "BATNA development",
  "Agreement documentation"],
 stds=["Negotiation practice literature (public, e.g., Getting to Yes framework)"],
 cites=["Harvard Program on Negotiation — public resources (public)"],
 demo=("outcome", {"label": "Disputes resolved in negotiation", "pre": 55, "post": 82})),

dict(title="When to Seek Help with a Dispute", tier=F,
 desc_pub=("Seek help when stakes exceed your comfort, power is imbalanced, emotions block "
  "progress, legal rights are unclear, or safety is at stake. Options escalate: advice "
  "consultation, negotiation coaching, mediation, arbitration, then litigation.\n"
  "Early help is cheaper: a one-hour legal consultation can prevent a five-figure mistake. "
  "Legal aid and bar referrals serve those who cannot pay. Educational information only."),
 desc_sig=("Signature triage routes disputes to the right help tier by stakes and complexity, "
  "so small problems get light help and big ones get full counsel."),
 how_pub=("People assess stakes and complexity, get an initial consultation to understand "
  "rights and options, and choose the lightest effective help. Community mediation centers "
  "offer low-cost neutrals; legal aid covers qualifying cases."),
 how_sig=("Signature tiered triage matches help intensity to dispute weight."),
 keys=["Stakes, imbalance, emotion, unclear rights, safety",
  "Escalate: advice, coaching, mediation, arbitration, litigation",
  "Early help is cheaper",
  "Consultations prevent costly mistakes",
  "Legal aid for those who qualify",
  "Educational information only"],
 reqs=["Self-assessment of stakes",
  "Consultation access",
  "Referral knowledge"],
 stds=["Bar referral standards (public)"],
 cites=["American Bar Association — finding help (public)"],
 demo=("pathway", {"dispute": "Neighbor fence disagreement, $800 at stake",
   "paths": [{"path": "negotiation", "note": "try direct first"},
             {"path": "mediation", "note": "community mediation, low cost"},
             {"path": "court", "note": "small claims if needed"}]})),

dict(title="The Role of a Neutral Third Party", tier=F,
 desc_pub=("Neutrals - mediators, arbitrators, ombuds, judges - bring impartiality, process "
  "expertise, and (in arbitration/adjudication) decision authority. Mediators facilitate "
  "agreement without deciding; arbitrators hear evidence and issue binding awards; ombuds "
  "investigate and recommend within organizations.\n"
  "Neutrality is the asset: conflicts of interest disqualify, and parties must trust the "
  "process. Selection - by agreement, institutional appointment, or court roster - shapes "
  "outcomes."),
 desc_sig=("Signature neutral management maintains vetted rosters with expertise tags and "
  "conflict checks, so the right neutral is found fast."),
 how_pub=("Parties select neutrals by agreement or institutional rules, disclose conflicts, and "
  "define the neutral's authority in writing (facilitate vs decide). Neutrals manage process "
  "fairly; parties participate in good faith."),
 how_sig=("Signature vetted rosters with expertise matching improve neutral selection."),
 keys=["Mediators facilitate; arbitrators decide; ombuds investigate",
  "Neutrality is the asset",
  "Conflicts disqualify",
  "Authority defined in writing",
  "Selection shapes outcomes",
  "Good-faith participation required"],
 reqs=["Neutral qualification standards",
  "Conflict disclosure",
  "Authority agreements"],
 stds=["Model Standards of Conduct for Mediators (public)",
  "Arbitrator ethics codes (public)"],
 cites=["American Arbitration Association — neutral standards (public)"],
 demo=("outcome", {"label": "Parties trusting the neutral's impartiality", "pre": 68, "post": 91})),

dict(title="Good-Faith Participation", tier=F,
 desc_pub=("Good-faith participation means engaging honestly: attending, sharing relevant "
  "information, considering proposals seriously, and honoring agreements. Many mediation "
  "programs and court rules require it; bad faith - stonewalling, no-show authority - can draw "
  "sanctions.\n"
  "Good faith does not mean surrendering: parties may firmly reject proposals while still "
  "participating constructively. The line is between hard bargaining and process abuse."),
 desc_sig=("Signature participation standards define good-faith behaviors explicitly per "
  "process, so expectations are clear to all."),
 how_pub=("Neutrals set expectations at the outset, monitor participation, and address bad "
  "faith privately then formally. Courts sanction egregious abuse. Agreements reached are "
  "documented before anyone leaves."),
 how_sig=("Signature explicit standards make good faith enforceable rather than aspirational."),
 keys=["Attend, share, consider, honor",
  "Required by many programs and courts",
  "Bad faith can draw sanctions",
  "Hard bargaining is allowed; abuse is not",
  "Document agreements before leaving",
  "Expectations set at outset"],
 reqs=["Participation standards",
  "Neutral authority to address abuse",
  "Agreement documentation"],
 stds=["Court ADR good-faith rules (public)"],
 cites=["American Bar Association — mediation guidance (public)"],
 demo=("outcome", {"label": "Mediations with full good-faith participation", "pre": 71, "post": 93})),

dict(title="Confidentiality in Resolution Processes", tier=F,
 desc_pub=("Confidentiality encourages candor: mediation communications are generally privileged "
  "and inadmissible, settlement negotiations are protected (FRE 408), and arbitration can be "
  "private by agreement. Exceptions exist - threats, crimes, and court-ordered disclosures.\n"
  "Parties should confirm confidentiality terms in writing before disclosing sensitive "
  "information. Private process is a major ADR advantage over public courts."),
 desc_sig=("Signature confidentiality management documents protections per process in the "
  "engagement terms, so parties disclose with confidence."),
 how_pub=("Neutrals explain confidentiality and its limits at the start; agreements confirm "
  "terms in writing. Caucus (private) sessions stay private from the other side. Breaches are "
  "addressed under the agreed terms and applicable law."),
 how_sig=("Signature written confidentiality terms precede sensitive disclosures."),
 keys=["Mediation privilege; FRE 408 for negotiations",
  "Encourages candor",
  "Exceptions: threats, crimes, court orders",
  "Confirm terms in writing first",
  "Caucuses stay private",
  "Privacy is a major ADR advantage"],
 reqs=["Confidentiality explanation at outset",
  "Written terms",
  "Caucus discipline"],
 stds=["Uniform Mediation Act (public model)",
  "FRE 408 (public)"],
 cites=["Cornell Legal Information Institute — FRE 408 (public)"],
 demo=("outcome", {"label": "Parties confident in confidentiality", "pre": 66, "post": 92})),

dict(title="Enforceability Basics", tier=F,
 desc_pub=("A resolution is only as good as its enforceability: mediated settlements become "
  "enforceable as contracts (and can be entered as court judgments); arbitration awards are "
  "enforced under statutes like the Federal Arbitration Act with very limited court review; "
  "court judgments enforce through liens, garnishment, and execution.\n"
  "Drafting for enforceability means clear obligations, deadlines, consequences, and the right "
  "formalities (signatures, notarization where needed). Educational information only."),
 desc_sig=("Signature enforceability review checks every agreement against enforcement "
  "requirements before signing, so resolutions hold up."),
 how_pub=("Neutrals and lawyers draft settlements with precise terms, enforcement mechanisms, "
  "and proper execution; arbitration awards follow statutory requirements; judgments are "
  "domesticated across jurisdictions as needed. Collection follows legal process."),
 how_sig=("Signature pre-signing enforceability checklists prevent hollow agreements."),
 keys=["Settlements enforce as contracts/judgments",
  "Arbitration awards: statutory enforcement, limited review",
  "Judgments: liens, garnishment, execution",
  "Draft clear obligations and consequences",
  "Proper formalities matter",
  "Educational information only"],
 reqs=["Enforceable drafting standards",
  "Statutory knowledge per path",
  "Collection process knowledge"],
 stds=["Federal Arbitration Act (public law)",
  "State enforcement statutes (public)"],
 cites=["Cornell Legal Information Institute — FAA (public)"],
 demo=("enforce", {"award": "Commercial arbitration award, $120,000",
   "jurisdictions": [{"jurisdiction": "U.S. federal court", "enforceable": True, "basis": "FAA"},
                     {"jurisdiction": "New York Convention state", "enforceable": True, "basis": "Convention"},
                     {"jurisdiction": "Non-signatory state", "enforceable": False, "basis": "no treaty"}]})),

dict(title="Choosing a Resolution Path", tier=F,
 desc_pub=("Choose paths by criteria: relationship future (mediate if ongoing), need for binding "
  "decision (arbitrate/litigate), privacy needs, cost and speed, power balance, precedent value, "
  "and enforceability across borders. No path is best always - fit decides.\n"
  "Multi-tier clauses sequence paths: negotiate, then mediate, then arbitrate - escalating only "
  "as needed. This 'stepped' design resolves most disputes at the cheapest tier."),
 desc_sig=("Signature path recommendation scores disputes against weighted criteria, producing "
  "a ranked path suggestion with reasoning."),
 how_pub=("Advisors score the dispute on the criteria with the parties, recommend a path or "
  "tiered sequence, and draft or invoke the appropriate clause or agreement. Choices are "
  "revisited if circumstances change."),
 how_sig=("Signature weighted scoring makes path choice transparent and defensible."),
 keys=["Criteria: relationship, binding need, privacy, cost, power, precedent",
  "No universally best path",
  "Multi-tier clauses escalate as needed",
  "Most resolve at the cheapest tier",
  "Fit decides",
  "Revisit if circumstances change"],
 reqs=["Path criteria knowledge",
  "Clause drafting or invocation",
  "Neutral access"],
 stds=["ADR clause drafting guidance (public literature)"],
 cites=["American Arbitration Association — clause drafting (public)"],
 demo=("pathway", {"dispute": "Software licensing dispute, $2M, ongoing vendor relationship",
   "paths": [{"path": "negotiation", "note": "executive talks first"},
             {"path": "mediation", "note": "preserve relationship"},
             {"path": "arbitration", "note": "binding, expert neutral"},
             {"path": "court", "note": "last resort"}]})),

dict(title="Costs and Timelines", tier=F,
 desc_pub=("Resolution economics: negotiation costs least (time only); mediation typically runs "
  "hundreds to low thousands per party per day; arbitration ranges from thousands to six "
  "figures for complex cases; litigation is usually costliest and slowest (1-3+ years).\n"
  "Timelines follow: mediation in weeks, arbitration in months, litigation in years. Fee-shifting "
  "clauses and cost rules affect strategy. Realistic budgeting prevents process abandonment "
  "midway."),
 desc_sig=("Signature cost modeling estimates each path's likely cost and duration from case "
  "characteristics, so parties choose with eyes open."),
 how_pub=("Advisors estimate costs per path, explain fee structures (hourly, fixed, split "
  "neutrals), and budget with contingencies. Parties compare expected value: likely outcome "
  "minus cost and time. Funding options (legal finance) exist for strong claims."),
 how_sig=("Signature expected-value modeling informs rational path choice."),
 keys=["Negotiation cheapest; litigation costliest/slowest",
  "Mediation: weeks; arbitration: months; litigation: years",
  "Fee structures vary per path",
  "Budget with contingencies",
  "Expected value: outcome minus cost/time",
  "Realistic budgets prevent mid-process abandonment"],
 reqs=["Cost estimation per path",
  "Fee structure knowledge",
  "Budget discipline"],
 stds=["Institutional fee schedules (public)"],
 cites=["American Arbitration Association — fee schedules (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Mediation scheduling to session", "days": 21},
   {"stage": "Session(s)", "days": 2},
   {"stage": "Agreement drafting", "days": 7}]})),

dict(title="Cultural Considerations", tier=F,
 desc_pub=("Culture shapes disputes: communication styles (direct vs indirect), attitudes toward "
  "authority and confrontation, concepts of face and honor, and decision-making norms all affect "
  "process design. Effective neutrals adapt - caucus-heavy mediation for face-sensitive "
  "cultures, for example.\n"
  "In cross-border disputes, language, legal traditions, and enforcement realities compound. "
  "Cultural competence is a neutral selection criterion, not a nicety."),
 desc_sig=("Signature cross-cultural protocols adapt process design to parties' norms, with "
  "culture-informed neutral matching."),
 how_pub=("Neutrals learn parties' backgrounds, adapt communication and process structure, use "
  "qualified interpreters (never family for sensitive matters), and check understanding "
  "explicitly. Institutions maintain diverse neutral rosters."),
 how_sig=("Signature culture-informed matching pairs neutrals to parties' needs."),
 keys=["Communication styles affect process",
  "Face and honor shape acceptable outcomes",
  "Adapt: caucus-heavy for face-sensitive cultures",
  "Qualified interpreters, never family",
  "Cross-border compounds complexity",
  "Cultural competence in neutral selection"],
 reqs=["Cultural competence training",
  "Diverse neutral rosters",
  "Interpreter access"],
 stds=["Cross-cultural mediation guidance (public literature)"],
 cites=["International Mediation Institute — public resources (public)"],
 demo=("outcome", {"label": "Cross-cultural parties satisfied with process", "pre": 58, "post": 86})),

# ---------------- Compounded (12) ----------------
dict(title="Mediation Process Step by Step", tier=C,
 desc_pub=("Mediation follows a structured flow: preparation (statements, authority check), "
  "opening (neutral explains process, ground rules), uninterrupted party statements, agenda "
  "setting, joint exploration, private caucuses (reality-testing, option generation), "
  "negotiation, and agreement drafting.\n"
  "The mediator controls process, not outcome: asking questions, reframing, testing reality, "
  "and carrying offers. Sessions run hours to days; complex cases use multiple sessions."),
 desc_sig=("Signature mediation management tracks agenda items, caucus insights (confidential), "
  "and agreement terms in structured workflows, so complex mediations stay organized."),
 how_pub=("Parties submit pre-mediation statements; the mediator opens with process explanation "
  "and confidentiality; parties tell their stories; the mediator builds the agenda and shuttles "
  "between joint sessions and caucuses, drafting the agreement when parties converge."),
 how_sig=("Signature structured workflows keep multi-session mediations coherent."),
 keys=["Prepare, open, statements, agenda, explore, caucus, negotiate, agree",
  "Mediator controls process, not outcome",
  "Caucuses: reality-testing and option generation",
  "Authority to settle must be present",
  "Hours to days; complex cases multi-session",
  "Agreement drafted before leaving"],
 reqs=["Pre-mediation statements",
  "Authority verification",
  "Agreement drafting capability"],
 stds=["Model Standards of Conduct for Mediators (public)"],
 cites=["American Bar Association — mediation (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Preparation and statements", "days": 14},
   {"stage": "Mediation session", "days": 1},
   {"stage": "Follow-up session if needed", "days": 14},
   {"stage": "Agreement finalization", "days": 7}]})),

dict(title="Mediation Approaches", tier=C,
 desc_pub=("Mediators work in styles: facilitative (guides communication, parties own the "
  "outcome), evaluative (assesses strengths/weaknesses, predicts court outcomes), and "
  "transformative (focuses on empowerment and recognition between parties). Most mediators "
  "blend, shifting with the dispute's needs.\n"
  "Matching style to dispute matters: evaluative helps when parties misjudge their cases; "
  "facilitative suits relationship preservation; transformative fits identity-laden conflicts."),
 desc_sig=("Signature mediator matching pairs dispute characteristics with mediator style "
  "profiles, improving fit."),
 how_pub=("Parties (or institutions) select mediators by style reputation and dispute fit; "
  "mediators disclose their approach at the outset and adapt transparently. Evaluative input "
  "is offered, not imposed, in most modern practice."),
 how_sig=("Signature style-profile matching improves mediator selection."),
 keys=["Facilitative: guide communication",
  "Evaluative: assess and predict",
  "Transformative: empowerment and recognition",
  "Most blend styles",
  "Match style to dispute",
  "Disclose approach at outset"],
 reqs=["Style knowledge for selection",
  "Mediator approach disclosure",
  "Adaptability"],
 stds=["Mediator style literature (public)",
  "Model Standards (public)"],
 cites=["Association for Conflict Resolution — public resources (public)"],
 demo=("pathway", {"dispute": "Partners misjudge case values, need reality check",
   "paths": [{"path": "negotiation", "note": "tried, stalled on valuation"},
             {"path": "mediation", "note": "evaluative mediator: reality-test values"},
             {"path": "court", "note": "expensive valuation lesson"}]})),

dict(title="Preparing for Mediation", tier=C,
 desc_pub=("Mediation preparation wins settlements: know your interests and BATNA, organize key "
  "documents, prepare a concise mediation statement, ensure decision-makers attend (or are "
  "reachable), and plan concessions strategically.\n"
  "The mediation statement educates the mediator (not the opponent): facts, issues, "
  "strengths/weaknesses honestly assessed, and settlement history. Authority gaps kill "
  "mediations - verify before the day."),
 desc_sig=("Signature mediation preparation builds structured briefs with authority "
  "verification checklists, so parties arrive ready."),
 how_pub=("Lawyers draft statements, assemble document bundles, brief clients on process and "
  "strategy, confirm authority holders' attendance, and plan opening remarks. Logistics - "
  "rooms, caucus space, technology - are confirmed."),
 how_sig=("Signature preparation checklists ensure nothing arrives half-ready."),
 keys=["Know interests, BATNA, walk-away",
  "Concise mediation statement",
  "Decision-makers must attend",
  "Plan concessions strategically",
  "Authority gaps kill mediations",
  "Confirm logistics"],
 reqs=["Mediation statement",
  "Document bundle",
  "Authority confirmation"],
 stds=["Mediation preparation guidance (public literature)"],
 cites=["American Bar Association — mediation prep (public)"],
 demo=("outcome", {"label": "Mediations settling (prepared parties)", "pre": 68, "post": 89})),

dict(title="Arbitration Process", tier=C,
 desc_pub=("Arbitration is private adjudication: parties agree (by clause or submission) to "
  "submit disputes to neutral arbitrator(s) who hear evidence and issue binding awards. It "
  "follows structured stages: initiation, arbitrator selection, preliminary hearing, discovery "
  "(limited), hearing, and award.\n"
  "Advantages: expertise, privacy, speed, finality, cross-border enforceability. Trade-offs: "
  "limited appeal, costs for complex cases, and arbitrator selection stakes."),
 desc_sig=("Signature arbitration management tracks each stage's deadlines and deliverables, so "
  "private adjudication stays efficient."),
 how_pub=("Claimants file demands per institutional rules; parties select arbitrators (lists, "
  "strikes, or appointment); preliminary conferences set schedules; limited discovery proceeds; "
  "hearings present evidence like streamlined trials; arbitrators issue reasoned awards."),
 how_sig=("Signature stage-tracked arbitration keeps private cases on schedule."),
 keys=["Private adjudication, binding awards",
  "Stages: initiation to award",
  "Advantages: expertise, privacy, speed, finality",
  "Trade-offs: limited appeal, costs, selection stakes",
  "Discovery limited vs litigation",
  "Institutional rules govern"],
 reqs=["Arbitration agreement or clause",
  "Institutional rules selection",
  "Arbitrator selection process"],
 stds=["AAA/ICC/LCIA rules (public)",
  "Federal Arbitration Act (public law)"],
 cites=["American Arbitration Association — rules (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Demand and arbitrator selection", "days": 45},
   {"stage": "Preliminary hearing and schedule", "days": 30},
   {"stage": "Discovery (limited)", "days": 90},
   {"stage": "Hearing", "days": 10},
   {"stage": "Award", "days": 30}]})),

dict(title="Arbitration Agreements and Clauses", tier=C,
 desc_pub=("Arbitration clauses in contracts decide disputes' forum before they arise: scope "
  "(which disputes), seat (legal home), rules (AAA, ICC), arbitrator number and selection, "
  "language, and cost allocation. Drafting defects - vague scope, unconscionable terms - invite "
  "court fights.\n"
  "Consumer and employment clauses face fairness scrutiny; some jurisdictions restrict them. "
  "Well-drafted clauses are specific, balanced, and mutual. Educational information only."),
 desc_sig=("Signature clause drafting uses tested templates per transaction type with fairness "
  "review, so clauses hold up."),
 how_pub=("Drafters define scope clearly, choose seat and rules deliberately, specify arbitrator "
  "qualifications and selection, allocate costs fairly, and ensure mutuality. Parties review "
  "clauses before signing - not after disputes arise."),
 how_sig=("Signature template-plus-fairness-review drafting prevents defective clauses."),
 keys=["Scope, seat, rules, arbitrators, language, costs",
  "Draft before disputes arise",
  "Vague scope invites court fights",
  "Fairness scrutiny for consumer/employment",
  "Specific, balanced, mutual",
  "Review before signing"],
 reqs=["Clause drafting expertise",
  "Institutional rule knowledge",
  "Fairness review"],
 stds=["Institutional model clauses (public)"],
 cites=["American Arbitration Association — clause drafting (public)"],
 demo=("outcome", {"label": "Clauses surviving enforcement challenges", "pre": 74, "post": 96})),

dict(title="Presenting a Case in Arbitration", tier=C,
 desc_pub=("Arbitration hearings resemble streamlined trials: opening statements, witness "
  "testimony (direct and cross), exhibits, and closings - before one or three arbitrators. "
  "Procedures flex by agreement: documents-only arbitration for small claims, video hearings "
  "for distance.\n"
  "Persuasion targets sophisticated decision-makers: lead with the contract and the story, "
  "organize exhibits for instant retrieval, and prepare witnesses for arbitrator questions "
  "(arbitrators question more actively than juries)."),
 desc_sig=("Signature hearing preparation builds exhibit-linked outlines with arbitrator-"
  "question anticipation, so presentations are tight."),
 how_pub=("Lawyers prepare hearing bundles with indexed exhibits, outline examinations around "
  "the contract's key provisions, brief witnesses on arbitrator questioning style, and "
  "deliver focused openings/closings. Post-hearing briefs follow where ordered."),
 how_sig=("Signature exhibit-linked outlines keep hearings efficient and persuasive."),
 keys=["Streamlined trial before arbitrators",
  "Openings, testimony, exhibits, closings",
  "Documents-only for small claims",
  "Lead with contract and story",
  "Arbitrators question actively",
  "Organize exhibits for instant retrieval"],
 reqs=["Hearing bundle preparation",
  "Witness preparation",
  "Arbitrator-style adaptation"],
 stds=["Institutional hearing procedures (public)"],
 cites=["International Chamber of Commerce — arbitration (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Pre-hearing briefs and bundles", "days": 21},
   {"stage": "Hearing days", "days": 5},
   {"stage": "Post-hearing briefs", "days": 30}]})),

dict(title="Arbitration Decisions: Awards", tier=C,
 desc_pub=("Arbitration awards are the arbitrators' binding decisions: reasoned (explaining "
  "conclusions) or unreasoned, covering liability, damages, costs, and interest. Awards are "
  "final with extremely limited court review - vacatur only for corruption, bias, excess of "
  "authority, or similar narrow grounds.\n"
  "Parties can seek correction of clerical errors; substantive reconsideration is generally "
  "unavailable. Finality is the feature - and the risk."),
 desc_sig=("Signature award review checks awards against enforcement requirements before "
  "delivery, ensuring they are complete and enforceable."),
 how_pub=("Arbitrators deliberate, draft awards addressing all submitted issues with reasons "
  "(where required), and issue through the institution. Parties review for errors warranting "
  "correction; enforcement follows statutory procedures."),
 how_sig=("Signature pre-delivery award checks catch completeness issues early."),
 keys=["Binding decisions; reasoned or unreasoned",
  "Cover liability, damages, costs, interest",
  "Extremely limited court review",
  "Vacatur: corruption, bias, excess authority",
  "Clerical correction available",
  "Finality is feature and risk"],
 reqs=["Award drafting per rules",
  "Issue completeness",
  "Enforcement procedure knowledge"],
 stds=["Institutional award requirements (public)",
  "FAA vacatur grounds (public law)"],
 cites=["Federal Arbitration Act — award provisions (public)"],
 demo=("enforce", {"award": "Domestic arbitration award, reasoned",
   "jurisdictions": [{"jurisdiction": "U.S. state court", "enforceable": True, "basis": "FAA/state law"},
                     {"jurisdiction": "EU member state", "enforceable": True, "basis": "New York Convention"}]})),

dict(title="Enforceability of Arbitration Awards", tier=C,
 desc_pub=("Arbitration awards enforce through statutes: the Federal Arbitration Act (and state "
  "analogues) domestically, the New York Convention internationally (170+ states). Courts "
  "confirm awards routinely; refusal grounds are narrow (invalid agreement, due process "
  "violations, public policy).\n"
  "Strategy: draft awards with enforcement in mind (clear orders, proper formalities), and "
  "consider the debtor's assets' location before choosing the forum. Educational information "
  "only."),
 desc_sig=("Signature enforcement planning maps award, assets, and jurisdictions at the "
  "outset, so winning is followed by collecting."),
 how_pub=("Winners petition for confirmation in a proper court, serve per rules, and convert to "
  "judgment; collection uses judgment-enforcement tools. Cross-border winners invoke the New "
  "York Convention in the assets' jurisdiction."),
 how_sig=("Signature asset-jurisdiction mapping at case start prevents pyrrhic victories."),
 keys=["FAA domestically; New York Convention (170+ states)",
  "Confirmation routinely granted",
  "Narrow refusal grounds",
  "Draft awards for enforceability",
  "Consider assets' location early",
  "Collection via judgment tools"],
 reqs=["Confirmation procedure knowledge",
  "Convention jurisdiction analysis",
  "Asset location intelligence"],
 stds=["New York Convention (public treaty)",
  "FAA Chapter 2 (public law)"],
 cites=["UNCITRAL — New York Convention (public)"],
 demo=("enforce", {"award": "ICC award, $4.2M, debtor assets in 3 countries",
   "jurisdictions": [{"jurisdiction": "France", "enforceable": True, "basis": "New York Convention"},
                     {"jurisdiction": "Singapore", "enforceable": True, "basis": "New York Convention"},
                     {"jurisdiction": "Non-convention state", "enforceable": False, "basis": "no treaty"}]})),

dict(title="Small Claims Procedures", tier=C,
 desc_pub=("Small claims courts resolve modest disputes (limits typically $5,000-$10,000 by "
  "state) quickly and cheaply: simplified forms, relaxed evidence rules, usually no lawyers "
  "required, hearings in weeks to months.\n"
  "Preparation wins: organized documents, clear timelines, and focused testimony. Collecting "
  "judgments is a separate skill - winning is step one. Educational information only."),
 desc_sig=("Signature small-claims preparation builds evidence packets with timelines, so "
  "self-represented parties present like professionals."),
 how_pub=("Claimants file simple forms and pay small fees; defendants are served; both bring "
  "organized evidence to informal hearings. Judges decide promptly; winners enforce via "
  "established collection procedures."),
 how_sig=("Signature evidence-packet templates level the playing field for self-represented "
  "parties."),
 keys=["Modest disputes; simplified procedures",
  "Usually no lawyers needed",
  "Hearings in weeks to months",
  "Preparation wins: documents, timelines",
  "Collecting is a separate skill",
  "Educational information only"],
 reqs=["Filing forms and fees",
  "Organized evidence",
  "Collection knowledge"],
 stds=["State small claims rules (public)"],
 cites=["State court self-help resources (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Filing to hearing", "days": 45},
   {"stage": "Hearing", "days": 1},
   {"stage": "Judgment to collection", "days": 60}]})),

dict(title="Ombuds Programs", tier=C,
 desc_pub=("Ombuds are confidential, independent dispute resolvers inside organizations: they "
  "listen, explain options, mediate informally, and spot systemic patterns - without keeping "
  "records that identify visitors (the IOA standards: independence, neutrality, "
  "confidentiality, informality).\n"
  "Organizational ombuds serve workplaces and universities; classical ombuds investigate "
  "citizen complaints against government. Their systemic feedback prevents future disputes."),
 desc_sig=("Signature ombuds design pairs confidential casework with aggregated pattern "
  "reporting, so individual help and systemic improvement reinforce each other."),
 how_pub=("Organizations charter ombuds to IOA standards, publicize the resource, and protect "
  "its independence. Ombuds track issue patterns (anonymized) and recommend systemic fixes to "
  "leadership."),
 how_sig=("Signature pattern-reporting turns confidential casework into organizational "
  "learning."),
 keys=["Confidential, independent, informal",
  "Listen, explain options, mediate, spot patterns",
  "IOA standards: independence, neutrality, confidentiality, informality",
  "No identifying records",
  "Organizational and classical models",
  "Systemic feedback prevents disputes"],
 reqs=["IOA-standard charter",
  "Independence protections",
  "Pattern reporting"],
 stds=["IOA Standards of Practice (public)"],
 cites=["International Ombuds Association — standards (public)"],
 demo=("outcome", {"label": "Visitors reporting issue resolved", "pre": 62, "post": 85})),

dict(title="Online Dispute Resolution", tier=C,
 desc_pub=("Online dispute resolution (ODR) moves processes online: negotiation platforms, video "
  "mediation, and algorithmic triage - pioneered by e-commerce (eBay/PayPal resolved millions) "
  "and now spreading to courts for small claims, traffic, and family matters.\n"
  "Design principles: accessible, fair, transparent, with human escalation. ODR expands access "
  "dramatically where courts are distant or backlogged - while the digital divide demands "
  "alternatives."),
 desc_sig=("Signature ODR design builds accessible platforms with human escalation paths, so "
  "technology expands justice rather than rationing it."),
 how_pub=("Courts and providers deploy platforms with guided intake, document exchange, "
  "asynchronous negotiation, and video hearings. Users get plain-language guidance; neutrals "
  "work online-native. Outcomes and satisfaction are measured like in-person processes."),
 how_sig=("Signature human-escalation design ensures technology serves access."),
 keys=["Negotiation platforms, video mediation, algorithmic triage",
  "E-commerce pioneered at scale",
  "Courts adopt for small claims, traffic, family",
  "Accessible, fair, transparent, human escalation",
  "Expands access where courts are distant",
  "Mind the digital divide"],
 reqs=["ODR platform",
  "Plain-language user guidance",
  "Human escalation paths"],
 stds=["ODR standards (public literature, e.g., NCTDR)"],
 cites=["National Center for Technology and Dispute Resolution (public)"],
 demo=("outcome", {"label": "ODR users resolving without travel", "pre": 45, "post": 88})),

dict(title="Restorative Practices", tier=C,
 desc_pub=("Restorative practices repair harm through dialogue: victim-offender mediation, family "
  "group conferences, and peacemaking circles bring together those affected to acknowledge "
  "harm, make amends, and reintegrate. Used in criminal justice, schools, and communities.\n"
  "The focus shifts from punishment to repair: what happened, who was affected, what is needed "
  "to make things right. Participation is voluntary; preparation ensures safety."),
 desc_sig=("Signature restorative design structures preparation, dialogue, and agreement "
  "follow-up, so repair is real rather than ritual."),
 how_pub=("Facilitators prepare each party separately, convene structured dialogues, guide "
  "toward concrete amends agreements, and follow up on completion. Programs coordinate with "
  "justice systems where cases are diverted."),
 how_sig=("Signature follow-up tracking ensures amends agreements are completed."),
 keys=["Repair harm through dialogue",
  "Victim-offender mediation, conferences, circles",
  "Focus: what happened, who affected, how to repair",
  "Voluntary participation",
  "Preparation ensures safety",
  "Follow up on agreements"],
 reqs=["Trained restorative facilitators",
  "Voluntary participation",
  "Justice-system coordination where diverted"],
 stds=["Restorative justice standards (public literature)"],
 cites=["Centre for Justice and Reconciliation — public resources (public)"],
 demo=("outcome", {"label": "Agreements completed", "pre": 58, "post": 87})),

# ---------------- Advanced (11) ----------------
dict(title="Multi-Party Mediation", tier=A,
 desc_pub=("Multi-party mediation handles disputes with many stakeholders - construction "
  "defects, environmental conflicts, class-action settlements: stakeholder mapping, "
  "representative structures, phased agendas, and coalition dynamics management.\n"
  "The mediator becomes a process architect: sequencing bilateral and plenary sessions, "
  "managing information flow, and building agreements coalition by coalition. Complexity "
  "demands preparation proportional to parties."),
 desc_sig=("Signature multi-party design uses stakeholder mapping and phased process plans, so "
  "complex mediations are architected, not improvised."),
 how_pub=("Mediators map stakeholders and interests, design representative structures, run "
  "phased processes (bilaterals then plenaries), and build agreement incrementally with "
  "coalition management. Documentation tracks who agreed to what."),
 how_sig=("Signature stakeholder mapping makes multi-party dynamics visible and manageable."),
 keys=["Many stakeholders, complex dynamics",
  "Stakeholder mapping first",
  "Representative structures",
  "Phased: bilaterals then plenaries",
  "Mediator as process architect",
  "Build agreement coalition by coalition"],
 reqs=["Stakeholder analysis",
  "Process architecture skill",
  "Agreement tracking"],
 stds=["Multi-party mediation guidance (public literature)"],
 cites=["Consensus Building Institute — public resources (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Stakeholder mapping and design", "days": 30},
   {"stage": "Bilateral sessions", "days": 45},
   {"stage": "Plenary negotiations", "days": 30},
   {"stage": "Agreement drafting", "days": 21}]})),

dict(title="Cross-Border Dispute Resolution", tier=A,
 desc_pub=("Cross-border disputes add jurisdiction, language, legal tradition, and enforcement "
  "complexity: which law applies, which forum decides, and where the award enforces. "
  "International arbitration (ICC, SIAC, LCIA) is the dominant solution - neutral forum, "
  "expert neutrals, New York Convention enforcement.\n"
  "Clause drafting decides everything: seat, rules, language, governing law. Without good "
  "clauses, parties litigate about litigating. Educational information only."),
 desc_sig=("Signature cross-border design standardizes clause packages per trade corridor, so "
  "international deals start dispute-ready."),
 how_pub=("Lawyers analyze conflicts of law, select neutral seats and institutions, draft "
  "comprehensive clauses, and manage proceedings across time zones and languages. Enforcement "
  "strategy considers assets' jurisdictions from the start."),
 how_sig=("Signature corridor-standard clauses reduce cross-border dispute friction."),
 keys=["Jurisdiction, language, tradition, enforcement complexity",
  "International arbitration dominates",
  "Clause drafting decides everything",
  "Seat, rules, language, governing law",
  "Enforcement strategy from the start",
  "Educational information only"],
 reqs=["Conflicts-of-law analysis",
  "Institutional knowledge (ICC, SIAC, LCIA)",
  "Cross-border enforcement strategy"],
 stds=["Institutional international rules (public)",
  "New York Convention (public treaty)"],
 cites=["International Chamber of Commerce — arbitration (public)",
  "UNCITRAL — public resources (public)"],
 demo=("enforce", {"award": "SIAC award, enforcement across Asia",
   "jurisdictions": [{"jurisdiction": "Singapore", "enforceable": True, "basis": "New York Convention"},
                     {"jurisdiction": "Japan", "enforceable": True, "basis": "New York Convention"},
                     {"jurisdiction": "Seat court (set-aside risk)", "enforceable": True, "basis": "review standards"}]})),

dict(title="Enforceability by Jurisdiction", tier=A,
 desc_pub=("Enforceability varies by jurisdiction: domestic awards enforce under national "
  "statutes; foreign awards under the New York Convention (with local quirks); mediated "
  "settlements under contract law (or the Singapore Convention for cross-border mediated "
  "settlements); court judgments under comity or treaties like the Hague Judgments Convention.\n"
  "Local counsel is essential: refusal grounds, limitation periods, and asset-attachment rules "
  "differ everywhere. Map enforcement before you need it. Educational information only."),
 desc_sig=("Signature jurisdiction mapping maintains enforceability profiles per country per "
  "instrument, so strategy rests on current local reality."),
 how_pub=("Lawyers identify the enforcement jurisdictions, consult local counsel on refusal "
  "grounds and procedures, and structure awards/settlements for local requirements. Assets are "
  "traced in parallel with merits proceedings."),
 how_sig=("Signature enforceability profiles keep strategy grounded in local law."),
 keys=["Domestic statutes; New York Convention; Singapore Convention; Hague Judgments",
  "Local quirks matter everywhere",
  "Local counsel essential",
  "Refusal grounds differ",
  "Map enforcement before needing it",
  "Trace assets in parallel"],
 reqs=["Jurisdiction-by-jurisdiction analysis",
  "Local counsel network",
  "Asset tracing"],
 stds=["New York, Singapore Conventions (public treaties)"],
 cites=["UNCITRAL — conventions (public)"],
 demo=("enforce", {"award": "Mediated settlement, cross-border",
   "jurisdictions": [{"jurisdiction": "Singapore Convention state", "enforceable": True, "basis": "Singapore Convention"},
                     {"jurisdiction": "Non-signatory", "enforceable": False, "basis": "contract action needed"}]})),

dict(title="The New York Convention", tier=A,
 desc_pub=("The 1958 New York Convention on foreign arbitral awards - ratified by 170+ states - "
  "is the backbone of international commerce dispute resolution: courts must recognize "
  "arbitration agreements and enforce foreign awards, refusing only on narrow grounds "
  "(invalid agreement, due-process denial, excess of scope, public policy).\n"
  "Its genius is pro-enforcement bias: the burden falls on the resisting party, and courts "
  "interpret exceptions narrowly. Understanding it is essential for any cross-border deal."),
 desc_sig=("Signature Convention practice builds enforcement checklists per jurisdiction, "
  "operationalizing the treaty's pro-enforcement design."),
 how_pub=("Lawyers draft arbitration agreements to Convention standards, conduct arbitrations "
  "with due process rigor, and enforce awards by petitioning courts in asset jurisdictions "
  "with Convention-compliant documentation."),
 how_sig=("Signature jurisdiction checklists make Convention enforcement routine."),
 keys=["1958; 170+ states",
  "Recognize agreements; enforce awards",
  "Narrow refusal grounds",
  "Pro-enforcement bias",
  "Burden on resisting party",
  "Backbone of international commerce"],
 reqs=["Convention-compliant drafting",
  "Due-process rigor in proceedings",
  "Enforcement documentation"],
 stds=["New York Convention text (public treaty)"],
 cites=["UNCITRAL — New York Convention (public)"],
 demo=("outcome", {"label": "Convention enforcement success rate", "pre": 88, "post": 96})),

dict(title="Investor-State Dispute Settlement", tier=A,
 desc_pub=("Investor-state dispute settlement (ISDS) lets foreign investors arbitrate against host "
  "states under investment treaties (ICSID, UNCITRAL rules): claims of expropriation, unfair "
  "treatment, or discrimination. Awards enforce like commercial awards.\n"
  "ISDS is controversial - critics cite regulatory chill; defenders cite rule of law for "
  "investment. Reform efforts (UNCITRAL Working Group III) debate appellate mechanisms and "
  "standing courts. Educational record."),
 desc_sig=("Signature ISDS analysis tracks reform developments with clause-design implications, "
  "keeping investment structuring current."),
 how_pub=("Investors structure investments through treaty-protected routes, monitor host-state "
  "measures, and - when disputes arise - trigger treaty cooling-off and arbitration. States "
  "defend with specialized counsel; proceedings are increasingly transparent."),
 how_sig=("Signature reform tracking translates ISDS developments into drafting guidance."),
 keys=["Investors vs states under treaties",
  "ICSID, UNCITRAL rules",
  "Expropriation, unfair treatment claims",
  "Controversial: regulatory chill debate",
  "Reform: appellate, standing court proposals",
  "Increasing transparency"],
 reqs=["Treaty network analysis",
  "Investment structuring",
  "Specialized counsel"],
 stds=["ICSID Convention (public treaty)",
  "UNCITRAL WG III reform (public)"],
 cites=["ICSID — public resources (public)",
  "UNCITRAL — WG III (public)"],
 demo=("timeline", {"stages": [
   {"stage": "Cooling-off and notice", "days": 180},
   {"stage": "Tribunal constitution", "days": 120},
   {"stage": "Written phases", "days": 365},
   {"stage": "Hearing and award", "days": 240}]})),

dict(title="Construction Dispute Boards", tier=A,
 desc_pub=("Dispute boards resolve construction conflicts in real time: standing panels (dispute "
  "adjudication boards) visit sites regularly and decide disputes within weeks - before they "
  "fester into project-killing litigation. FIDIC contracts standardize the model globally.\n"
  "Boards prevent disputes as much as resolve them: regular presence builds trust and catches "
  "issues early. Decisions are typically binding unless challenged in arbitration."),
 desc_sig=("Signature dispute-board practice standardizes board procedures per contract form, "
  "making real-time resolution reliable."),
 how_pub=("Contracts establish boards at project start; members visit regularly, hear disputes "
  "with site knowledge, and issue prompt decisions. Parties comply pending any arbitration "
  "challenge; the project continues."),
 how_sig=("Signature standardized board procedures keep decisions prompt and respected."),
 keys=["Real-time resolution on live projects",
  "Standing panels with site knowledge",
  "Decide within weeks",
  "FIDIC standardizes globally",
  "Prevent as much as resolve",
  "Binding unless challenged"],
 reqs=["Board appointment at project start",
  "Site-knowledgeable members",
  "Prompt decision procedures"],
 stds=["FIDIC dispute board provisions (public)",
  "Dispute Board Federation guidance (public)"],
 cites=["International Federation of Consulting Engineers — FIDIC (public)"],
 demo=("outcome", {"label": "Disputes resolved without arbitration", "pre": 62, "post": 89})),

dict(title="Family Dispute Resolution", tier=A,
 desc_pub=("Family disputes - divorce, custody, support, property - need processes protecting "
  "children and preserving co-parenting: mediation (the norm), collaborative law (lawyers "
  "commit to settlement, disqualified if it fails), parenting coordination (implementing "
  "custody orders), and arbitration for discrete issues.\n"
  "Children's interests govern: courts apply best-interests standards, and processes shield "
  "children from conflict. Safety exceptions (domestic violence) require specialized "
  "protocols. Educational information only."),
 desc_sig=("Signature family resolution design centers children's interests with safety "
  "screening built into every process, so protection is structural."),
 how_pub=("Families choose processes by conflict level and safety; neutrals screen for "
  "violence and adapt (shuttle mediation, separate sessions); agreements address parenting "
  "time, support, and property comprehensively; courts review for children's interests."),
 how_sig=("Signature built-in safety screening protects vulnerable family members."),
 keys=["Mediation norm; collaborative law; parenting coordination",
  "Children's best interests govern",
  "Shield children from conflict",
  "Safety screening for violence",
  "Agreements: parenting, support, property",
  "Courts review for children"],
 reqs=["Family mediation training",
  "Violence screening protocols",
  "Child-focused practice"],
 stds=["Family mediation standards (public)",
  "Collaborative law protocols (public)"],
 cites=["Association of Family and Conciliation Courts (public)"],
 demo=("outcome", {"label": "Parenting agreements reached", "pre": 64, "post": 88})),

dict(title="Workplace Dispute Systems", tier=A,
 desc_pub=("Workplace dispute systems handle grievances, harassment claims, and conflicts: "
  "multi-step procedures (supervisor, HR, mediation, arbitration), peer review panels, and "
  "ombuds - designed for early, low-level resolution.\n"
  "Effective systems are trusted: confidential, anti-retaliation, and visibly fair. Metrics - "
  "usage rates, resolution times, satisfaction - prove the system works or reveal it doesn't."),
 desc_sig=("Signature workplace systems design multi-tier resolution with trust metrics, so "
  "organizations know their systems work."),
 how_pub=("Organizations design step procedures with employee input, train managers in early "
  "resolution, publicize the system, and track metrics. Retaliation is prohibited and "
  "punished; systemic patterns trigger policy fixes."),
 how_sig=("Signature trust-metric dashboards make system effectiveness visible."),
 keys=["Multi-step: supervisor, HR, mediation, arbitration",
  "Peer review and ombuds options",
  "Early, low-level resolution",
  "Trusted: confidential, anti-retaliation, fair",
  "Metrics prove effectiveness",
  "Systemic patterns trigger fixes"],
 reqs=["Designed procedures with input",
  "Manager training",
  "Anti-retaliation enforcement"],
 stds=["Employment dispute system standards (public literature)"],
 cites=["American Arbitration Association — employment (public)"],
 demo=("outcome", {"label": "Grievances resolved at lowest tier", "pre": 52, "post": 79})),

dict(title="Court-Annexed ADR Programs", tier=A,
 desc_pub=("Courts run ADR programs to clear dockets and serve parties: mandatory mediation for "
  "civil cases, settlement conferences with judges, arbitration for smaller civil claims, and "
  "parenting programs for family cases. Participation is often required; settlement remains "
  "voluntary.\n"
  "Quality varies: good programs use trained neutrals, screen appropriately, and measure "
  "outcomes. Access concerns - costs, power imbalances - need program design attention."),
 desc_sig=("Signature court-ADR design pairs mandatory participation with quality neutrals and "
  "outcome measurement, so dockets clear justly."),
 how_pub=("Courts order parties into programs at case milestones, appoint or approve neutrals, "
  "and track settlement rates and satisfaction. Parties prepare as for private ADR; judges "
  "enforce participation but not settlement."),
 how_sig=("Signature quality-paired mandatory programs make court ADR effective and fair."),
 keys=["Mandatory mediation, settlement conferences, arbitration",
  "Clear dockets; serve parties",
  "Participation required; settlement voluntary",
  "Trained neutrals and screening",
  "Measure outcomes",
  "Design for access and power balance"],
 reqs=["Court ADR rules",
  "Qualified neutral rosters",
  "Outcome measurement"],
 stds=["State court ADR rules (public)"],
 cites=["National Center for State Courts — ADR (public)"],
 demo=("outcome", {"label": "Court-referred cases settling", "pre": 58, "post": 76})),

dict(title="Ethics for Neutrals", tier=A,
 desc_pub=("Neutrals hold special ethical duties: impartiality (no bias or interest), "
  "confidentiality, informed consent to process, competence, and - for mediators - party "
  "self-determination (the parties decide). Arbitrators must disclose conflicts and decide on "
  "the evidence.\n"
  "Gifts, ex parte contacts, and undisclosed interests destroy trust and can vacate awards. "
  "Institutional rosters enforce standards through qualification and removal."),
 desc_sig=("Signature neutral ethics embeds disclosure and conduct standards in every "
  "engagement, making integrity verifiable."),
 how_pub=("Neutrals disclose conflicts before appointment, explain their role's limits, protect "
  "confidences, avoid ex parte substantive contact (in mediation, caucuses are the structured "
  "exception), and decide (arbitrators) only on the record."),
 how_sig=("Signature engagement-embedded ethics make neutral integrity systematic."),
 keys=["Impartiality, confidentiality, consent, competence",
  "Mediators: party self-determination",
  "Arbitrators: decide on the evidence",
  "Disclose conflicts",
  "No gifts or improper ex parte contact",
  "Rosters enforce standards"],
 reqs=["Ethics training for neutrals",
  "Disclosure procedures",
  "Roster qualification standards"],
 stds=["Model Standards of Conduct for Mediators (public)",
  "AAA/ABA Code of Ethics for Arbitrators (public)"],
 cites=["American Bar Association — neutral ethics (public)"],
 demo=("outcome", {"label": "Neutrals with clean ethics records", "pre": 94, "post": 99})),

dict(title="The Future of Dispute Resolution", tier=A,
 desc_pub=("Dispute resolution's future: ODR at court scale, AI-assisted triage and drafting "
  "(with human neutrals deciding), embedded resolution in platforms and contracts, and "
  "expanding access for the underserved. The Singapore Convention may do for mediation what "
  "New York did for arbitration.\n"
  "The through-line is access to justice: resolving more disputes fairly with fewer barriers. "
  "Human judgment remains central - technology assists, neutrals decide. Educational record."),
 desc_sig=("The Signature future-state is a resolution operating system: triage, path "
  "selection, online processes, and enforceability - with human neutrals at the center. This "
  "database is a prototype of that system's knowledge core."),
 how_pub=("Institutions deploy ODR with human escalation, validate AI tools for fairness, "
  "expand low-cost options, and measure access gains. Treaties and rules evolve; training "
  "keeps neutrals current."),
 how_sig=("Signature's operating-system vision keeps human neutrals central in automated "
  "resolution."),
 keys=["ODR at court scale",
  "AI-assisted, human-decided",
  "Embedded resolution in platforms",
  "Singapore Convention's potential",
  "Through-line: access to justice",
  "Validate AI for fairness"],
 reqs=["ODR deployment with escalation",
  "AI validation",
  "Access measurement"],
 stds=["Emerging ODR/AI standards (public literature)"],
 cites=["UNCITRAL — ODR and mediation (public)"],
 demo=("outcome", {"label": "Disputes resolved without courts", "pre": 48, "post": 71})),
]
