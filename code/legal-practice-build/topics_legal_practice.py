#!/usr/bin/env python3
"""Topics + config for the legal-practice pair. Property of Justin Addam Higgins (JAH).

Educational framing only — never legal advice.
"""
import sys, os
sys.path.insert(0, os.path.expanduser("~/workspace/jah-databases/code/_pairbuild12"))

LEGAL_NOTE = "Educational information only — not legal advice. Consult a licensed attorney for personal matters."

CFG = {
    "slug": "legal-practice",
    "name_pub": "The Legal Practice Database",
    "name_sig": "Signature Legal Practice Database",
    "tagline_pub": ("Legal practice from the ground up: how the legal system works, finding and "
                    "working with lawyers, case management, legal research and writing, filings and "
                    "court procedure, evidence, and document workflows - every record carrying the "
                    "full entry taught progressively along the ladder."),
    "tagline_sig": ("The Signature system's expanded treatment of legal practice: the same real "
                    "practice knowledge carried forward, plus Signature-built case-management "
                    "models, research frameworks, and workflow systems original to this system."),
    "record_kind": "legal practice record",
    "record_kind_plural": "legal practice records",
    "prefix_pub": "JAH-LEGP-", "prefix_sig": "JAH-LEGPS-",
    "ai_pub": "JAH Legal Practice Archivist",
    "ai_sig": "JAH Signature Legal Practice Creator",
    "role_pub": ("legal practice archivist - teaching the legal system, working with lawyers, case "
                 "management, research, filings, procedure, and evidence; answers from many angles "
                 "- definition, example, process, procedure, practice - using only archive data "
                 "from this system"),
    "role_sig": ("Signature creator of legal practice systems - designing case-management models, "
                 "research frameworks, and workflow systems as original Signature works; answers "
                 "from many angles using only archive data from this system"),
    "search_ph": "Search courts, lawyers, case management, research, filings, evidence...",
    "chat_ph": "Ask about legal practice...",
    "greet_pub": ("I am the JAH Legal Practice Archivist. Ask me about the legal system, working "
                  "with lawyers, case management, research, and procedure. " + LEGAL_NOTE),
    "greet_sig": ("I am the JAH Signature Legal Practice Creator. Ask me about Signature-built "
                  "legal practice systems. " + LEGAL_NOTE),
    "gen_blurb": ("Generate clearly-labeled legal practice studies. Seeded archive records "
                  "are the authoritative entries."),
    "about_archive": ("Seeded legal practice records, marching toward one million records. "
                      "Presented in teaching-ladder order: foundations, compounded, advanced. " +
                      LEGAL_NOTE),
    "demo_kind": "legal-demo",
    "demo_title": "Legal Practice Demo",
    "health": False,
}

F = "Foundations"; C = "Compounded"; A = "Advanced"


def demo_builder(topic, edition):
    v, p = topic["demo"]
    head = '# Legal Practice Demo — %s\n# Edition: %s\n' % (topic["title"], edition)

    def fill(src, mapping):
        for k, val in mapping.items():
            src = src.replace("@@" + k + "@@", repr(val))
        return head + src

    if v == "deadline":
        return fill(
            "import datetime\n"
            "event = datetime.date(*@@EVENT@@)\ndays = @@DAYS@@\n"
            "deadline = event + datetime.timedelta(days=days)\n"
            "print('Trigger event:', event.isoformat())\n"
            "print('Rule: %d days' % days)\n"
            "print('Deadline:', deadline.isoformat(), '(%s)' % deadline.strftime('%A'))\n",
            {"EVENT": p["event"], "DAYS": p["days"]})
    if v == "conflict":
        return fill(
            "new = @@NEW@@\nexisting = @@EXIST@@\n"
            "hits = [c for c in existing if c['party'].lower() in new['parties'].lower() or new['matter'].lower() in c['matter'].lower()]\n"
            "print('New matter:', new['matter'])\n"
            "print('Parties:', new['parties'])\n"
            "print('Potential conflicts:', len(hits))\n"
            "for h in hits:\n"
            "    print(' REVIEW:', h['matter'], '-', h['party'])\n",
            {"NEW": p["new"], "EXIST": p["existing"]})
    if v == "research":
        return fill(
            "issue = @@ISSUE@@\nsources = @@SOURCES@@\n"
            "rank = {'primary': 0, 'secondary': 1}\n"
            "ordered = sorted(sources, key=lambda s: (rank[s['type']], s['title']))\n"
            "print('Research issue:', issue)\n"
            "for s in ordered:\n"
            "    print(' [%s] %s — %s' % (s['type'], s['title'], s['note']))\n",
            {"ISSUE": p["issue"], "SOURCES": p["sources"]})
    if v == "assemble":
        return fill(
            "fields = @@FIELDS@@\ntemplate = @@TMPL@@\n"
            "doc = template\n"
            "for k, val in fields.items():\n"
            "    doc = doc.replace('{{' + k + '}}', val)\n"
            "print('Assembled document:')\n"
            "print(doc)\n"
            "missing = [k for k in fields if '{{' + k + '}}' in doc]\n"
            "print('Unfilled fields:', missing if missing else 'none')\n",
            {"FIELDS": p["fields"], "TMPL": p["template"]})
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
dict(title="What Legal Practice Is", tier=F,
 desc_pub=("Legal practice is the work of lawyers and legal professionals: advising clients on "
  "rights and obligations, representing them in disputes and transactions, drafting documents, "
  "and navigating courts and agencies. It spans litigation, business law, family law, criminal "
  "defense and prosecution, real estate, estate planning, and dozens of specialties.\n"
  "The profession is regulated: lawyers are licensed by states, bound by ethics rules, and owe "
  "clients loyalty, confidentiality, and competent diligence. Non-lawyers - paralegals, legal "
  "assistants - work under lawyer supervision."),
 desc_sig=("The Signature system models legal practice as a matter lifecycle - intake, research, "
  "drafting, filing, advocacy, resolution - with each stage's work product defined, so matters "
  "are managed as engineered workflows rather than improvised efforts."),
 how_pub=("A client brings a problem; the lawyer evaluates it in a consultation, checks for "
  "conflicts, and agrees on scope and fees in writing. Work proceeds through research, drafting, "
  "negotiation or filing, and resolution - with the client informed and deciding at each major "
  "step."),
 how_sig=("Signature matter lifecycle tracking gives every case a stage, owner, and next action "
  "visible to the team."),
 keys=["Advise, represent, draft, navigate courts and agencies",
  "Litigation, business, family, criminal, real estate, estates",
  "Licensed by states; bound by ethics rules",
  "Duties: loyalty, confidentiality, diligence",
  "Paralegals work under lawyer supervision",
  "Scope and fees agreed in writing"],
 reqs=["State bar licensure",
  "Conflict-checking system",
  "Written engagement agreements"],
 stds=["ABA Model Rules of Professional Conduct (public model)",
  "State ethics rules (public)"],
 cites=["American Bar Association — Model Rules (public)",
  "Cornell Legal Information Institute — public legal resources (public)"],
 demo=("research", {"issue": "Whether a non-compete clause is enforceable",
   "sources": [{"type": "primary", "title": "State non-compete statute", "note": "binding authority"},
               {"type": "primary", "title": "Recent appellate decision", "note": "binding precedent"},
               {"type": "secondary", "title": "Treatise chapter", "note": "persuasive background"}]})),

dict(title="Sources of Law", tier=F,
 desc_pub=("U.S. law comes from several sources in a hierarchy: constitutions (federal supreme), "
  "statutes (laws passed by legislatures), regulations (agency rules implementing statutes), and "
  "case law (court decisions interpreting all of the above). Common law - judge-made principles "
  "in areas like contracts and torts - fills gaps statutes leave.\n"
  "Precedent (stare decisis) means courts generally follow earlier decisions of higher courts in "
  "their jurisdiction. Finding the controlling source for an issue is the first research skill."),
 desc_sig=("Signature legal research organizes sources by binding-vs-persuasive weight per "
  "jurisdiction, so every answer shows its authority level transparently."),
 how_pub=("Lawyers identify the jurisdiction, then search constitutions, statutes, regulations, "
  "and cases in order - checking that each source is current (not repealed or overruled) before "
  "relying on it. Secondary sources (treatises, articles) explain; primary sources control."),
 how_sig=("Signature authority-weighting labels every cited source with its binding level, "
  "preventing weak-source reliance."),
 keys=["Constitutions, statutes, regulations, case law",
  "Federal constitution supreme",
  "Common law fills statutory gaps",
  "Precedent: follow higher-court decisions",
  "Verify sources are current",
  "Primary sources control; secondary explain"],
 reqs=["Access to current legal databases",
  "Jurisdiction identification",
  "Currency verification (citators)"],
 stds=["Legal research methodology standards (public literature)"],
 cites=["Cornell Legal Information Institute (public)",
  "U.S. Government Publishing Office — govinfo (public)"],
 demo=("research", {"issue": "Statute of limitations for written contracts",
   "sources": [{"type": "secondary", "title": "Contracts treatise", "note": "background"},
               {"type": "primary", "title": "State limitations statute", "note": "controlling"},
               {"type": "primary", "title": "Appellate tolling decision", "note": "interpretive"}]})),

dict(title="The Court System", tier=F,
 desc_pub=("The U.S. has parallel court systems: federal courts (district trial courts, circuit "
  "appeals courts, the Supreme Court) handling federal issues, and state courts (trial, "
  "intermediate appellate, supreme) handling most cases. Trial courts find facts; appellate "
  "courts review legal errors.\n"
  "Jurisdiction decides which court can hear a case - by subject matter and geography. Most "
  "disputes start in state trial court; appeals move up one level at a time with strict "
  "deadlines."),
 desc_sig=("Signature court-navigation maps each matter to its proper court with filing "
  "requirements and deadlines, so cases start in the right forum."),
 how_pub=("Lawyers determine the right court by claims and parties, file the initiating papers, "
  "and litigate through trial. Losing parties may appeal on legal-error grounds within "
  "jurisdictional deadlines; appellate courts review records and briefs, rarely new evidence."),
 how_sig=("Signature forum-mapping prevents the costly error of filing in the wrong court."),
 keys=["Federal and state parallel systems",
  "Trial courts find facts; appellate review legal errors",
  "Jurisdiction: subject matter + geography",
  "Most cases start in state trial court",
  "Appeals have strict deadlines",
  "Right court first"],
 reqs=["Jurisdiction analysis",
  "Court rules for the forum",
  "Appellate deadline calendaring"],
 stds=["Federal and state rules of civil/appellate procedure (public)"],
 cites=["U.S. Courts — public resources (public)"],
 demo=("deadline", {"event": (2026, 3, 10), "days": 30})),

dict(title="Civil vs Criminal Cases", tier=F,
 desc_pub=("Civil cases resolve private disputes - contracts, injuries, family matters - with "
  "remedies like money damages or injunctions; the standard is usually preponderance of the "
  "evidence (more likely than not). Criminal cases punish offenses against the state - with "
  "liberty at stake, the standard is proof beyond a reasonable doubt, and defendants get "
  "appointed counsel if indigent.\n"
  "The same conduct can trigger both: a drunk driver faces criminal prosecution and a civil "
  "lawsuit from victims. Procedures, rights, and stakes differ fundamentally."),
 desc_sig=("Signature matter typing classifies cases at intake with the applicable standards "
  "and procedures attached, so nothing proceeds under the wrong rules."),
 how_pub=("Civil plaintiffs file complaints seeking remedies; parties exchange discovery and "
  "often settle. Criminal cases begin with charges, arraignment, plea or trial, and sentencing. "
  "Lawyers match strategy to the forum's standards and procedures from day one."),
 how_sig=("Signature intake classification routes each matter to its correct procedural "
  "track immediately."),
 keys=["Civil: private disputes; damages/injunctions; preponderance standard",
  "Criminal: state prosecution; liberty at stake; beyond reasonable doubt",
  "Same conduct can trigger both",
  "Indigent criminal defendants get appointed counsel",
  "Procedures and stakes differ fundamentally",
  "Match strategy to the forum"],
 reqs=["Forum identification at intake",
  "Applicable standard and procedure knowledge",
  "Rights advisement"],
 stds=["Federal/state civil and criminal procedure rules (public)",
  "Constitutional criminal protections (public)"],
 cites=["Cornell Legal Information Institute — civil vs criminal (public)"],
 demo=("research", {"issue": "Burden of proof in a negligence case",
   "sources": [{"type": "primary", "title": "Jury instruction on preponderance", "note": "controlling standard"},
               {"type": "secondary", "title": "Torts treatise", "note": "explanation"}]})),

dict(title="Finding and Choosing a Lawyer", tier=F,
 desc_pub=("Finding the right lawyer means matching specialty to problem: personal referrals, bar "
  "association referral services, legal aid for those who qualify, and lawyer directories. "
  "Choose by relevant experience, clear communication, fee transparency, and comfort - the "
  "relationship requires candor.\n"
  "Initial consultations (often free or low-cost) let both sides evaluate fit. Ask about "
  "experience with similar matters, likely process and timeline, fees, and who will actually do "
  "the work."),
 desc_sig=("Signature lawyer-matching structures the selection as scored criteria - specialty "
  "fit, experience, communication, fees - so choice is deliberate rather than desperate."),
 how_pub=("People identify their legal issue category, gather candidates from referrals and "
  "directories, interview 2-3 lawyers with prepared questions, compare engagement terms, and "
  "sign a written fee agreement with the chosen lawyer. Legal aid and pro bono cover those who "
  "cannot pay."),
 how_sig=("Signature scored selection criteria make lawyer choice systematic."),
 keys=["Match specialty to problem",
  "Referrals, bar services, legal aid, directories",
  "Interview 2-3 with prepared questions",
  "Ask: experience, process, timeline, fees, staffing",
  "Written fee agreement",
  "Candor requires comfort"],
 reqs=["Issue categorization",
  "Candidate sources",
  "Interview question list"],
 stds=["Bar referral service standards (public)",
  "Attorney advertising rules (public)"],
 cites=["American Bar Association — finding legal help (public)"],
 demo=("outcome", {"label": "Clients reporting good lawyer fit", "pre": 62, "post": 88})),

dict(title="Legal Fees and Billing", tier=F,
 desc_pub=("Lawyers charge by hourly rates (billed in tenths), flat fees (routine matters), "
  "contingency fees (percentage of recovery - common in injury cases), or retainers (advance "
  "deposits drawn as work is done). Ethics rules require reasonable fees communicated in "
  "writing.\n"
  "Clients should understand: what triggers billing, how costs/expenses are handled, billing "
  "frequency, and what happens if they cannot pay. Fee disputes go to bar fee-arbitration "
  "programs."),
 desc_sig=("Signature fee transparency standardizes engagement letters with worked examples, so "
  "clients understand costs before work begins."),
 how_pub=("Lawyers propose fee structures in engagement letters with examples; clients ask "
  "questions before signing. Bills itemize time and expenses; clients review promptly and raise "
  "issues early. Disputes use bar arbitration before litigation."),
 how_sig=("Signature worked-example engagement letters make fee structures concrete."),
 keys=["Hourly, flat, contingency, retainer",
  "Reasonable fees in writing (ethics rule)",
  "Understand billing triggers and expenses",
  "Review bills promptly",
  "Raise issues early",
  "Bar arbitration resolves disputes"],
 reqs=["Written engagement letters",
  "Itemized billing",
  "Fee dispute process knowledge"],
 stds=["ABA Model Rule 1.5 fees (public model)",
  "State fee rules (public)"],
 cites=["American Bar Association — Model Rule 1.5 (public)"],
 demo=("assemble", {"fields": {"client": "Jordan Ellis", "matter": "Lease review",
   "fee_type": "Flat fee", "amount": "$750", "date": "2026-04-01"},
   "template": "ENGAGEMENT LETTER\nClient: {{client}}\nMatter: {{matter}}\nFee: {{fee_type}} of {{amount}}\nDate: {{date}}\n"})),

dict(title="Attorney-Client Privilege", tier=F,
 desc_pub=("Attorney-client privilege protects confidential client-lawyer communications made for "
  "legal advice - clients can speak candidly without fear the lawyer will be forced to disclose. "
  "The client holds the privilege; only the client can waive it.\n"
  "Limits: no privilege for future crimes/frauds, and disclosure to third parties can waive it. "
  "Work product doctrine separately protects lawyers' litigation preparation. Practical rule: "
  "keep legal communications private and labeled."),
 desc_sig=("Signature privilege protection bakes confidentiality into matter workflows - access "
  "controls, labeling, and waiver warnings - so protection is structural."),
 how_pub=("Lawyers explain privilege at engagement, mark communications privileged, limit "
  "distribution, and warn before any disclosure that might waive it. Joint representations get "
  "written privilege explanations. Crime-fraud situations trigger ethics consultation."),
 how_sig=("Signature workflow-embedded privilege guards prevent accidental waiver."),
 keys=["Protects confidential legal-advice communications",
  "Client holds and waives the privilege",
  "No privilege for future crimes/frauds",
  "Third-party disclosure can waive",
  "Work product protects preparation",
  "Keep legal communications private and labeled"],
 reqs=["Privilege explanation at engagement",
  "Access controls and labeling",
  "Waiver-risk warnings"],
 stds=["Evidence rules on privilege (public)",
  "ABA Model Rules 1.6, 8.4 (public model)"],
 cites=["Cornell Legal Information Institute — privilege (public)"],
 demo=("outcome", {"label": "Matters with documented privilege briefing", "pre": 55, "post": 93})),

dict(title="Legal Ethics Basics", tier=F,
 desc_pub=("Legal ethics bind lawyers to competence, diligence, loyalty, confidentiality, and "
  "candor to courts. Key rules: no conflicts of interest without informed consent, no "
  "commingling client funds (trust accounts), no dishonesty, and supervision of non-lawyer "
  "staff.\n"
  "Violations bring bar discipline from reprimand to disbarment. Clients harmed by misconduct "
  "can complain to the state bar's disciplinary authority - a free process."),
 desc_sig=("Signature ethics compliance embeds conflict checks, trust accounting, and "
  "supervision into daily workflows, making ethical practice the path of least resistance."),
 how_pub=("Firms run conflict checks before engagement, maintain separate trust accounts with "
  "reconciliation, supervise staff work, and consult ethics counsel on close questions. "
  "Clients receive engagement letters defining the relationship's boundaries."),
 how_sig=("Signature embedded compliance makes ethical practice automatic."),
 keys=["Competence, diligence, loyalty, confidentiality, candor",
  "No conflicts without informed consent",
  "Trust accounts: never commingle",
  "Supervise non-lawyer staff",
  "Discipline: reprimand to disbarment",
  "Clients can complain to the bar"],
 reqs=["Conflict-checking system",
  "Trust account compliance",
  "Ethics consultation access"],
 stds=["ABA Model Rules (public model)",
  "State disciplinary rules (public)"],
 cites=["American Bar Association — Model Rules (public)"],
 demo=("conflict", {"new": {"matter": "Smith divorce", "parties": "Alex Smith vs Jordan Smith"},
   "existing": [{"matter": "Smith business formation", "party": "Alex Smith"},
                {"matter": "Garcia custody", "party": "Maria Garcia"}]})),

dict(title="Legal Documents Everyone Should Know", tier=F,
 desc_pub=("Core life documents: wills (distribute property, name guardians), powers of attorney "
  "(financial decisions if incapacitated), health care proxies and living wills (medical "
  "decisions), and beneficiary designations (which override wills for accounts). Businesses add "
  "contracts, operating agreements, and employment documents.\n"
  "Having these documents - current and properly executed - prevents courts from deciding for "
  "you. Review after major life events."),
 desc_sig=("Signature document planning gives every adult a completeness checklist with "
  "execution requirements per document, so nothing essential is missing or invalid."),
 how_pub=("Lawyers assess each client's needs, draft documents to state-law requirements, "
  "supervise proper execution (witnesses, notarization), and store copies accessibly. Reviews "
  "follow marriages, births, divorces, and moves."),
 how_sig=("Signature completeness checklists ensure no essential document is missing."),
 keys=["Wills, POAs, health proxies, living wills, beneficiary designations",
  "Beneficiaries override wills for accounts",
  "Proper execution: witnesses, notarization",
  "Review after life events",
  "Prevents courts deciding for you",
  "Businesses: contracts, operating agreements"],
 reqs=["State-law execution knowledge",
  "Document storage and access",
  "Life-event review triggers"],
 stds=["State estate-document statutes (public)"],
 cites=["American Bar Association — estate planning resources (public)"],
 demo=("assemble", {"fields": {"name": "Casey Morgan", "agent": "Riley Morgan",
   "date": "2026-05-01"},
   "template": "HEALTH CARE PROXY\nI, {{name}}, appoint {{agent}} as my health care agent.\nDate: {{date}}\n"})),

dict(title="Statutes of Limitations", tier=F,
 desc_pub=("Statutes of limitations set deadlines for filing lawsuits - missed deadlines usually "
  "kill claims permanently. Periods vary by claim type and state: often 2-4 years for injury, "
  "longer for contracts, with special rules for minors and delayed discovery.\n"
  "The lesson is urgency: consult a lawyer promptly after any potential claim. Tolling doctrines "
  "can pause clocks, but never rely on them without advice. Educational information only."),
 desc_sig=("Signature deadline management computes limitations periods at intake with tolling "
  "analysis, so no claim dies on a calendar error."),
 how_pub=("Lawyers identify every potential claim at intake, research its limitations period and "
  "accrual date, calendar the earliest deadline with buffers, and file or toll well before "
  "expiry. Clients are warned in writing about deadlines."),
 how_sig=("Signature auto-computed deadlines with buffers make limitations management "
  "fail-safe."),
 keys=["Deadlines for filing; missed = usually fatal",
  "Vary by claim type and state",
  "Special rules: minors, delayed discovery",
  "Consult promptly after potential claims",
  "Tolling can pause - never rely without advice",
  "Calendar with buffers"],
 reqs=["Limitations research per claim",
  "Calendaring with buffers",
  "Written client warnings"],
 stds=["State limitations statutes (public)"],
 cites=["Cornell Legal Information Institute — limitations (public)"],
 demo=("deadline", {"event": (2025, 6, 15), "days": 730})),

dict(title="Access to Justice and Legal Aid", tier=F,
 desc_pub=("Most legal needs go unmet: legal aid societies, pro bono programs, law school "
  "clinics, and court self-help centers serve those who cannot afford lawyers. Legal Aid "
  "funding (LSC) supports civil aid nationwide; criminal defendants get public defenders.\n"
  "Self-represented litigants can use court forms and self-help centers, though complex matters "
  "need counsel. Unbundled services (hiring a lawyer for part of a case) stretch limited "
  "budgets."),
 desc_sig=("Signature access design triages legal needs to the right resource tier - self-help, "
  "unbundled, full representation - maximizing justice per dollar."),
 how_pub=("People contact legal aid intake for eligibility screening, use self-help centers for "
  "forms and procedure, and seek pro bono through bar programs. Lawyers offer unbundled "
  "services where rules allow. Courts simplify processes for the self-represented."),
 how_sig=("Signature needs-triaging routes each person to the highest-value help they can "
  "access."),
 keys=["Most legal needs go unmet",
  "Legal aid, pro bono, clinics, self-help centers",
  "LSC funds civil aid; public defenders for criminal",
  "Court forms for the self-represented",
  "Unbundled services stretch budgets",
  "Complex matters need counsel"],
 reqs=["Legal aid intake knowledge",
  "Self-help resource familiarity",
  "Pro bono program links"],
 stds=["LSC program standards (public)",
  "State pro bono rules"],
 cites=["Legal Services Corporation — public resources (public)",
  "American Bar Association — pro bono (public)"],
 demo=("outcome", {"label": "Eligible clients connected to aid", "pre": 48, "post": 79})),

# ---------------- Compounded (12) ----------------
dict(title="Case Intake and Conflict Checks", tier=C,
 desc_pub=("Case intake evaluates potential matters: the facts, the legal issues, the client's "
  "goals, the fee arrangement, and - critically - conflicts of interest. Lawyers must check "
  "every new matter against current and former clients before engagement.\n"
  "Conflicts can be consentable (informed written consent cures some) or non-consentable (no "
  "amount of consent fixes others, like directly adverse litigation). Imputed conflicts spread "
  "one lawyer's conflict to the whole firm."),
 desc_sig=("Signature intake runs automated conflict searches across parties, affiliates, and "
  "adverse parties before any engagement letter issues - conflicts caught by system, not "
  "memory."),
 how_pub=("Intake staff gather parties and facts; the firm searches its conflict database "
  "(names, affiliates, adverse parties); lawyers evaluate consentability; engagement letters "
  "document the decision. Former-client conflicts get special analysis."),
 how_sig=("Signature automated searches make conflict clearance fast and complete."),
 keys=["Intake: facts, issues, goals, fees, conflicts",
  "Check every matter before engagement",
  "Consentable vs non-consentable conflicts",
  "Imputed: one lawyer's conflict binds the firm",
  "Search parties, affiliates, adversaries",
  "Document decisions in engagement letters"],
 reqs=["Conflict database",
  "Intake questionnaire",
  "Consentability analysis"],
 stds=["ABA Model Rules 1.7-1.10 (public model)"],
 cites=["American Bar Association — conflicts guidance (public)"],
 demo=("conflict", {"new": {"matter": "Acme merger", "parties": "Acme Corp acquiring Beta Inc"},
   "existing": [{"matter": "Beta employment dispute", "party": "Beta Inc"},
                {"matter": "Acme trademark", "party": "Acme Corp"}]})),

dict(title="Case Management Systems", tier=C,
 desc_pub=("Case management systems organize matters: contacts, calendars, documents, time "
  "tracking, billing, and tasks in one place. Good systems prevent the classic failures - missed "
  "deadlines, lost documents, unbilled time - through structure rather than memory.\n"
  "Selection criteria: conflict checking, calendaring reliability, document management, "
  "security and ethics compliance (cloud providers must meet confidentiality duties), and "
  "usability lawyers will actually adopt."),
 desc_sig=("Signature matter management unifies the lifecycle - intake to resolution - with "
  "deadline computation, document assembly, and task tracking in one engineered workflow."),
 how_pub=("Firms select systems meeting ethics duties, migrate matters with clean data, train "
  "all users, and enforce usage (calendaring rules, naming conventions). Deadlines get "
  "redundant calendaring; documents get version control."),
 how_sig=("Signature unified lifecycle workflows make best practice the default, not the "
  "exception."),
 keys=["Contacts, calendars, documents, time, billing, tasks",
  "Prevent missed deadlines, lost documents, unbilled time",
  "Cloud must meet confidentiality duties",
  "Usability determines adoption",
  "Redundant calendaring for deadlines",
  "Enforce conventions"],
 reqs=["Ethics-compliant system selection",
  "Data migration and training",
  "Usage enforcement"],
 stds=["ABA tech competence guidance (public model)",
  "State cloud ethics opinions (public)"],
 cites=["American Bar Association — law practice resources (public)"],
 demo=("deadline", {"event": (2026, 7, 1), "days": 21})),

dict(title="Legal Research Methods", tier=C,
 desc_pub=("Legal research answers questions with authority: define the issue, find controlling "
  "primary sources (statutes, cases), verify currency with citators (Shepard's/KeyCite), and "
  "organize findings into a memo. Secondary sources orient; primary sources decide.\n"
  "Method prevents the classic errors: relying on overruled cases, missing the controlling "
  "statute, or citing out-of-jurisdiction law. Research logs document the path for review."),
 desc_sig=("Signature research workflows structure issue-spotting, source gathering, currency "
  "verification, and memo drafting as one traceable process."),
 how_pub=("Researchers frame precise issues, search databases with terms-and-connectors or "
  "natural language, filter by jurisdiction and date, validate every key source's currency, and "
  "write memos with question, brief answer, analysis, and conclusion (IRAC/CREAC)."),
 how_sig=("Signature traceable research logs make every memo's foundation auditable."),
 keys=["Define issue; find controlling sources; verify currency",
  "Secondary orients; primary decides",
  "Citators catch overruled law",
  "Jurisdiction filters everything",
  "IRAC/CREAC structures memos",
  "Log the research path"],
 reqs=["Legal database access",
  "Citator verification",
  "Memo-writing standards"],
 stds=["Legal research pedagogy standards (public literature)"],
 cites=["Cornell Legal Information Institute (public)"],
 demo=("research", {"issue": "Admissibility of text messages at trial",
   "sources": [{"type": "primary", "title": "Rules of evidence (hearsay)", "note": "controlling framework"},
               {"type": "primary", "title": "Appellate text-message decision", "note": "application"},
               {"type": "secondary", "title": "Evidence treatise", "note": "background"}]})),

dict(title="Legal Writing", tier=C,
 desc_pub=("Legal writing persuades through clarity: plain language, short sentences, active "
  "voice, and structure that puts conclusions first. Briefs argue; memos analyze; letters "
  "advise - each with conventions serving its reader.\n"
  "Citations (Bluebook/ALWD) let readers verify every claim. The discipline: every assertion "
  "supported, every argument honest about weaknesses, every document proofread - courts notice "
  "sloppiness."),
 desc_sig=("Signature legal drafting pairs structural templates with citation verification, so "
  "documents are clear, supported, and honest by construction."),
 how_pub=("Writers outline (issue, rule, application, conclusion), draft with the reader's "
  "needs first, cite every legal assertion, address counterarguments candidly, and revise for "
  "clarity and correctness. Colleagues review high-stakes briefs."),
 how_sig=("Signature template-plus-verification drafting makes quality systematic."),
 keys=["Clarity persuades: plain language, short sentences",
  "Conclusions first",
  "Briefs argue; memos analyze; letters advise",
  "Cite every legal assertion",
  "Address weaknesses honestly",
  "Proofread - courts notice sloppiness"],
 reqs=["Writing standards and templates",
  "Citation manual compliance",
  "Review process for high-stakes work"],
 stds=["Bluebook/ALWD citation (public)",
  "Plain language guidelines (public)"],
 cites=["The Bluebook (public citation system)"],
 demo=("outcome", {"label": "Briefs passing internal review first pass", "pre": 64, "post": 90})),

dict(title="Pleadings and Motions", tier=C,
 desc_pub=("Pleadings frame the lawsuit: complaints state claims and facts; answers admit or deny "
  "and raise defenses; counterclaims strike back. Motions ask courts for orders - to dismiss, "
  "for summary judgment, to compel discovery - supported by briefs and evidence.\n"
  "Standards matter: complaints must state plausible claims (Twombly/Iqbal federally); summary "
  "judgment needs no genuine dispute of material fact. Precision in pleading shapes everything "
  "after."),
 desc_sig=("Signature pleading workflows assemble complaints from element checklists per claim, "
  "ensuring every element is alleged with supporting facts."),
 how_pub=("Lawyers investigate facts, research claims' elements, draft pleadings alleging each "
  "element, file and serve per rules, and respond to opponents' pleadings on deadline. Motions "
  "follow with briefs, evidence, and oral argument."),
 how_sig=("Signature element-checklist pleading ensures claims are completely alleged."),
 keys=["Complaints state claims; answers respond; motions request orders",
  "Plausibility standard for complaints",
  "Summary judgment: no genuine material dispute",
  "Precision shapes everything after",
  "Deadlines govern responses",
  "Serve per rules"],
 reqs=["Claim-element knowledge",
  "Pleading standards per forum",
  "Deadline management"],
 stds=["Federal Rules of Civil Procedure (public)",
  "State pleading rules (public)"],
 cites=["Cornell Legal Information Institute — FRCP (public)"],
 demo=("deadline", {"event": (2026, 2, 15), "days": 21})),

dict(title="Discovery", tier=C,
 desc_pub=("Discovery is pretrial fact exchange: interrogatories (written questions), document "
  "requests, requests for admission, depositions (oral testimony under oath), and subpoenas to "
  "third parties. Its purposes: learn opponents' evidence, lock in testimony, and narrow "
  "disputes.\n"
  "Scope is broad (relevant, proportional) but bounded by privilege and proportionality. "
  "Abuses - hiding documents, evasive answers - draw sanctions. Most cases settle during or "
  "after discovery."),
 desc_sig=("Signature discovery management tracks every request, response, and deadline with "
  "privilege logging built in, so large discovery stays controlled."),
 how_pub=("Lawyers plan discovery to their proof needs, serve proportional requests, review "
  "productions for privilege before producing, log withheld documents, and meet-and-confer on "
  "disputes before seeking court intervention. Depositions lock in key testimony."),
 how_sig=("Signature request-tracking with privilege logging keeps discovery organized at "
  "scale."),
 keys=["Interrogatories, documents, admissions, depositions, subpoenas",
  "Learn evidence; lock testimony; narrow disputes",
  "Broad but bounded: relevance, proportionality, privilege",
  "Abuses draw sanctions",
  "Most cases settle in/after discovery",
  "Meet-and-confer before court fights"],
 reqs=["Discovery plan per case",
  "Privilege review process",
  "Deadline tracking"],
 stds=["FRCP discovery rules (public)",
  "State discovery rules (public)"],
 cites=["Federal Judicial Center — discovery resources (public)"],
 demo=("deadline", {"event": (2026, 4, 20), "days": 30})),

dict(title="Depositions", tier=C,
 desc_pub=("Depositions are pretrial oral examinations under oath: lawyers question parties and "
  "witnesses with a court reporter recording every word. They lock in testimony, assess "
  "credibility, and gather admissions for trial or settlement.\n"
  "Skills: open-ended questions for information, leading questions for admissions, patience "
  "through evasive answers, and knowing when to stop. Defending depositions means protecting "
  "witnesses with proper objections without coaching."),
 desc_sig=("Signature deposition preparation builds outline banks per witness type with exhibit "
  "tracking, so examinations are thorough and organized."),
 how_pub=("Lawyers prepare outlines and exhibits, notice depositions per rules, question "
  "strategically (background, then substance, then admissions), and review transcripts for "
  "impeachment material and summary-judgment support. Defending counsel objects properly and "
  "prepares witnesses ethically."),
 how_sig=("Signature outline banks with exhibit tracking standardize thorough preparation."),
 keys=["Oral testimony under oath, recorded",
  "Lock testimony; assess credibility; gather admissions",
  "Open-ended for info; leading for admissions",
  "Defend with objections, not coaching",
  "Transcripts fuel impeachment and motions",
  "Know when to stop"],
 reqs=["Deposition outline preparation",
  "Court reporter scheduling",
  "Exhibit management"],
 stds=["FRCP deposition rules (public)",
  "Ethics of witness preparation (public)"],
 cites=["American Bar Association — litigation resources (public)"],
 demo=("outcome", {"label": "Depositions yielding key admissions", "pre": 58, "post": 84})),

dict(title="Evidence Basics", tier=C,
 desc_pub=("Evidence law governs what fact-finders may consider: relevance (does it make a fact "
  "more likely?), authentication, hearsay (out-of-court statements for truth - generally "
  "excluded with many exceptions), character evidence limits, and privileges.\n"
  "Trial lawyers think in foundations: every exhibit needs authentication and a hearsay answer "
  "before admission. Objections must be timely and specific. This record is educational."),
 desc_sig=("Signature evidence preparation builds foundation checklists per exhibit with hearsay "
  "analysis, so trial admission is planned, not hoped for."),
 how_pub=("Lawyers inventory proof, match each item to an admissible path (exception or "
  "exemption), prepare authenticating witnesses, and brief objections and responses. Motions in "
  "limine resolve big fights before trial."),
 how_sig=("Signature per-exhibit foundation checklists make admission systematic."),
 keys=["Relevance, authentication, hearsay, character limits, privileges",
  "Hearsay generally excluded; many exceptions",
  "Every exhibit needs a foundation",
  "Objections: timely and specific",
  "Motions in limine pre-resolve fights",
  "Educational record"],
 reqs=["Evidence rules knowledge",
  "Exhibit inventory with foundations",
  "Objection preparation"],
 stds=["Federal Rules of Evidence (public)",
  "State evidence codes (public)"],
 cites=["Cornell Legal Information Institute — FRE (public)"],
 demo=("research", {"issue": "Hearsay exception for business records",
   "sources": [{"type": "primary", "title": "FRE 803(6)", "note": "controlling exception"},
               {"type": "primary", "title": "Appellate foundation decision", "note": "requirements"},
               {"type": "secondary", "title": "Evidence treatise", "note": "background"}]})),

dict(title="Court Filings and E-Filing", tier=C,
 desc_pub=("Court filings submit documents to the court record: complaints, motions, briefs, and "
  "proposed orders - now overwhelmingly electronic. E-filing systems (federal CM/ECF, state "
  "portals) impose technical rules: PDF standards, size limits, text-searchability, and "
  "electronic signatures.\n"
  "Deadlines are jurisdictional and technical: a 11:59 PM e-filing deadline means filed, not "
  "started, by then. Redaction rules protect privacy (SSNs, financial accounts, minors' "
  "names)."),
 desc_sig=("Signature filing workflows validate documents against court technical rules before "
  "submission, with deadline computation and redaction checks built in."),
 how_pub=("Staff prepare filings per court rules (margins, fonts, page limits), redact protected "
  "information, convert to compliant PDFs, and file through the proper portal well before "
  "deadlines. Confirmations are saved; service on opponents follows."),
 how_sig=("Signature pre-submission validation catches technical rejections before they cost "
  "deadlines."),
 keys=["Electronic filing is the norm",
  "Technical rules: PDF, size, searchability, signatures",
  "Deadlines: filed by, not started by",
  "Redact SSNs, accounts, minors' names",
  "Save confirmations",
  "Serve opponents after filing"],
 reqs=["E-filing accounts per court",
  "Technical compliance checking",
  "Redaction procedures"],
 stds=["Court e-filing rules (public)",
  "Privacy redaction rules (public)"],
 cites=["U.S. Courts — CM/ECF resources (public)"],
 demo=("deadline", {"event": (2026, 8, 5), "days": 14})),

dict(title="Calendaring and Deadlines", tier=C,
 desc_pub=("Calendaring is malpractice prevention: every deadline - statutes of limitations, "
  "discovery cutoffs, motion dates, appeal periods - computed from triggering events under the "
  "correct rules (which count differently: calendar days vs business days, plus mailing days).\n"
  "Best practice: redundant calendaring (two systems), ticklers before deadlines, and a "
  "culture where everyone calendars everything. Missed deadlines are the leading malpractice "
  "claim."),
 desc_sig=("Signature deadline computation derives every date from rules plus trigger events "
  "automatically, with redundant ticklers - calendaring as engineered reliability."),
 how_pub=("Staff identify trigger events, compute deadlines under applicable rules (verifying "
  "day-counting conventions), enter them redundantly with advance ticklers, and review "
  "upcoming deadlines in regular meetings. Changes re-trigger computation."),
 how_sig=("Signature rule-based computation eliminates manual date-counting errors."),
 keys=["Every deadline from trigger events under correct rules",
  "Day-counting conventions vary",
  "Redundant calendaring",
  "Ticklers before deadlines",
  "Missed deadlines = leading malpractice claim",
  "Review upcoming deadlines regularly"],
 reqs=["Deadline computation knowledge",
  "Redundant calendar systems",
  "Tickler discipline"],
 stds=["Court computation rules (e.g., FRCP 6) (public)"],
 cites=["Cornell Legal Information Institute — FRCP 6 (public)"],
 demo=("deadline", {"event": (2026, 9, 12), "days": 60})),

dict(title="Client Communication", tier=C,
 desc_pub=("Client communication is an ethics duty and a satisfaction driver: keep clients "
  "reasonably informed, explain matters so they can decide, respond promptly, and confirm "
  "important advice in writing. Most bar complaints trace to communication failures, not legal "
  "errors.\n"
  "Systems help: intake expectations, status-update schedules, documented advice letters, and "
  "secure client portals. Bad news delivered early and honestly preserves trust."),
 desc_sig=("Signature client communication runs on scheduled updates and documented advice, so "
  "no client wonders what is happening with their matter."),
 how_pub=("Lawyers set communication expectations at engagement, send scheduled status updates, "
  "confirm advice and decisions in writing, and respond within promised timeframes. Portals "
  "give clients 24/7 matter visibility."),
 how_sig=("Signature scheduled-update discipline makes communication proactive."),
 keys=["Ethics duty + satisfaction driver",
  "Inform, explain, respond promptly",
  "Confirm advice in writing",
  "Most complaints trace to communication",
  "Set expectations at engagement",
  "Bad news early and honestly"],
 reqs=["Communication expectations at intake",
  "Status-update schedule",
  "Secure communication channels"],
 stds=["ABA Model Rule 1.4 communication (public model)"],
 cites=["American Bar Association — client communication guidance (public)"],
 demo=("outcome", {"label": "Clients rating communication excellent", "pre": 66, "post": 91})),

dict(title="Document Workflows and Assembly", tier=C,
 desc_pub=("Document workflows turn expertise into efficient production: templates for recurring "
  "documents, assembly questionnaires gathering client facts, clause libraries for variations, "
  "and review checkpoints before execution. Automation handles routine drafting; lawyers focus "
  "judgment where it matters.\n"
  "Quality controls: template versioning, logic testing (every answer path produces correct "
  "documents), and attorney review of assembled drafts. Garbage in, gospel out is the risk - "
  "validate inputs."),
 desc_sig=("Signature document assembly runs versioned templates with tested logic and "
  "attorney-review gates, so automation multiplies expertise without multiplying errors."),
 how_pub=("Firms identify high-volume documents, build templates with conditional logic, test "
  "every path, and train staff on questionnaires. Assembled drafts go through attorney review "
  "before clients see them; templates version with law changes."),
 how_sig=("Signature tested-logic templates with review gates make automation safe."),
 keys=["Templates + questionnaires + clause libraries",
  "Automate routine; lawyer judgment where it matters",
  "Version templates with law changes",
  "Test every logic path",
  "Attorney review before clients",
  "Validate inputs"],
 reqs=["Template library",
  "Logic testing",
  "Review checkpoints"],
 stds=["Document automation best practices (public literature)"],
 cites=["American Bar Association — practice technology (public)"],
 demo=("assemble", {"fields": {"party_a": "Northwind Traders", "party_b": "Acme Corp",
   "amount": "$25,000", "date": "2026-10-01"},
   "template": "SETTLEMENT AGREEMENT\nBetween {{party_a}} and {{party_b}}\nAmount: {{amount}}\nEffective: {{date}}\n"})),

# ---------------- Advanced (11) ----------------
dict(title="Trial Preparation", tier=A,
 desc_pub=("Trial preparation turns a case file into a persuasive story: theory of the case, "
  "exhibit lists with foundations, witness preparation (ethical - no coaching testimony), "
  "demonstratives, opening and closing drafts, and motions in limine resolving evidence fights "
  "early.\n"
  "Preparation is where trials are won: organized exhibits, prepared witnesses, and practiced "
  "examinations beat improvisation. Checklists ensure nothing - subpoenas, originals, tech "
  "checks - is forgotten."),
 desc_sig=("Signature trial preparation runs matters through a readiness checklist with exhibit "
  "foundations verified and witness prep documented, so trial day holds no surprises."),
 how_pub=("Teams develop the theory, finalize exhibit and witness lists with foundations, "
  "prepare witnesses ethically, draft openings/closings, file motions in limine, and rehearse "
  "with technology checks. War rooms organize everything for instant access at trial."),
 how_sig=("Signature readiness scoring shows exactly what remains before a matter is "
  "trial-ready."),
 keys=["Theory of the case first",
  "Exhibits with foundations; witnesses prepared ethically",
  "Motions in limine resolve fights early",
  "Preparation wins trials",
  "Checklists prevent forgotten essentials",
  "Rehearse with technology"],
 reqs=["Trial checklist",
  "Exhibit and witness management",
  "War-room organization"],
 stds=["Trial practice standards (public literature)"],
 cites=["American Bar Association — trial resources (public)"],
 demo=("outcome", {"label": "Trial-ready checklists complete", "pre": 58, "post": 95})),

dict(title="Jury Selection", tier=A,
 desc_pub=("Jury selection (voir dire) seats a fair, favorable jury: questionnaires screen "
  "backgrounds, attorneys question for bias, challenges for cause remove the biased, and "
  "peremptory strikes (limited number, no discriminatory use under Batson) shape the panel.\n"
  "The goal is not a friendly jury but a fair one open to your case - identifying leaders, "
  "hidden biases, and life experiences that color evidence reception. This record is "
  "educational."),
 desc_sig=("Signature jury-selection preparation structures juror research and questioning plans "
  "per case theme, so selection is strategic rather than instinctual."),
 how_pub=("Lawyers review questionnaires, research jurors where allowed, plan voir dire around "
  "case themes, exercise cause challenges with records made, and use peremptories strategically "
  "while documenting race/gender-neutral reasons."),
 how_sig=("Signature theme-based questioning plans keep voir dire focused on what matters."),
 keys=["Voir dire: question for bias",
  "Challenges for cause remove biased jurors",
  "Peremptories: limited, no discriminatory use",
  "Goal: fair and open, not friendly",
  "Identify leaders and hidden biases",
  "Document neutral reasons"],
 reqs=["Voir dire planning",
  "Juror research (where permitted)",
  "Batson-compliant strike documentation"],
 stds=["Jury selection rules (public)",
  "Batson v. Kentucky (public case law)"],
 cites=["Cornell Legal Information Institute — Batson (public)"],
 demo=("outcome", {"label": "Jurors seated without cause reversals", "pre": 82, "post": 97})),

dict(title="Expert Witnesses", tier=A,
 desc_pub=("Expert witnesses translate technical subjects for fact-finders: retained for opinions "
  "(paid, disclosed, Daubert-scrutinized) or fact witnesses with expertise. Admissibility "
  "requires qualified experts using reliable methods applied reliably.\n"
  "Selection criteria: credentials, communication skill, independence, and litigation "
  "temperament. Preparation is extensive - reports, depositions, and trial testimony must align. "
  "This record is educational."),
 desc_sig=("Signature expert management tracks credentials, prior testimony, and Daubert history, "
  "so selection is evidence-based."),
 how_pub=("Lawyers identify needed expertise early, vet candidates (publications, prior "
  "testimony, bias checks), retain with clear scope, prepare reports meeting rule requirements, "
  "and ready experts for deposition and trial. Opponents' experts are challenged via Daubert "
  "where warranted."),
 how_sig=("Signature expert dossiers compile credentials, testimony history, and challenge "
  "outcomes for informed selection."),
 keys=["Translate technical subjects",
  "Retained experts: disclosed, Daubert-scrutinized",
  "Qualified + reliable methods + reliable application",
  "Select: credentials, communication, independence",
  "Reports, depositions, trial must align",
  "Challenge opponents' experts where warranted"],
 reqs=["Expert identification and vetting",
  "Report drafting per rules",
  "Daubert challenge capability"],
 stds=["FRE 702; Daubert standard (public)",
  "FRCP 26 expert disclosure (public)"],
 cites=["Cornell Legal Information Institute — FRE 702 (public)"],
 demo=("research", {"issue": "Daubert challenge to expert methodology",
   "sources": [{"type": "primary", "title": "FRE 702", "note": "controlling standard"},
               {"type": "primary", "title": "Daubert v. Merrell Dow", "note": "framework"},
               {"type": "secondary", "title": "Expert evidence treatise", "note": "factors"}]})),

dict(title="Evidence Management at Scale", tier=A,
 desc_pub=("Large cases generate terabytes: evidence management systems ingest, process, search, "
  "and produce documents with chain-of-custody tracking. Litigation holds preserve everything "
  "when litigation is anticipated - spoliation draws severe sanctions.\n"
  "Protocols govern collection (forensically sound), processing (deduplication, threading), "
  "review (predictive coding for large sets), and production (agreed formats). Project "
  "management discipline keeps costs controlled."),
 desc_sig=("Signature evidence platforms unify hold, collection, processing, review, and "
  "production with defensible workflows, making scale manageable."),
 how_pub=("Teams issue litigation holds immediately, plan collection with IT and forensics, "
  "process into review platforms, staff review with protocols and QC sampling, and produce per "
  "agreements. Costs are budgeted and tracked against phases."),
 how_sig=("Signature unified evidence workflows make large-case management defensible and "
  "efficient."),
 keys=["Terabytes need systems, not folders",
  "Litigation holds: preserve when anticipated",
  "Spoliation draws severe sanctions",
  "Forensically sound collection",
  "Predictive coding for large review",
  "Budget and track by phase"],
 reqs=["Litigation hold procedure",
  "Review platform",
  "Forensic collection capability"],
 stds=["Sedona Principles (public)",
  "FRCP e-discovery rules (public)"],
 cites=["The Sedona Conference — principles (public)"],
 demo=("outcome", {"label": "Review accuracy (QC sampling)", "pre": 88, "post": 97})),

dict(title="E-Discovery", tier=A,
 desc_pub=("E-discovery is discovery of electronically stored information: the EDRM framework "
  "(identification, preservation, collection, processing, review, production) structures it. "
  "Cooperation and proportionality - per FRCP 26 - bound the scope; technology-assisted review "
  "handles volume.\n"
  "Competence in e-discovery is now an ethics expectation. Early case assessment and "
  "meet-and-confer agreements on scope and format prevent the cost explosions that define bad "
  "e-discovery."),
 desc_sig=("Signature e-discovery playbooks standardize EDRM workflows with cost controls per "
  "phase, so electronic discovery is managed rather than endured."),
 how_pub=("Lawyers identify custodians and systems, issue holds, negotiate ESI protocols with "
  "opponents, collect forensically, process and review (with TAR for large sets), and produce "
  "in agreed formats with privilege logs. Costs are managed per phase."),
 how_sig=("Signature phase-costed playbooks keep e-discovery budgets predictable."),
 keys=["EDRM: identify to produce",
  "Cooperation and proportionality bound scope",
  "TAR handles volume",
  "Competence is an ethics expectation",
  "ESI protocols prevent cost explosions",
  "Privilege logs for withheld ESI"],
 reqs=["ESI protocol negotiation",
  "Forensic collection",
  "Review platform with TAR"],
 stds=["FRCP e-discovery amendments (public)",
  "Sedona Principles (public)"],
 cites=["The Sedona Conference (public)"],
 demo=("outcome", {"label": "E-discovery phases on budget", "pre": 52, "post": 85})),

dict(title="Appeals", tier=A,
 desc_pub=("Appeals ask higher courts to correct legal errors: notices of appeal within "
  "jurisdictional deadlines, records assembled, briefs arguing error with record citations, and "
  "oral argument. Appellate courts defer to trial courts on facts; they decide law.\n"
  "Standards of review decide cases: de novo for pure law, abuse of discretion for "
  "discretionary calls, clear error for facts. Preservation - objecting below - is prerequisite; "
  "unpreserved errors face plain-error review. This record is educational."),
 desc_sig=("Signature appellate practice structures issue selection by standard of review with "
  "preservation verification, focusing briefs on winnable error."),
 how_pub=("Lawyers calendar appeal deadlines immediately, order transcripts, designate the "
  "record, research standards of review, and brief the strongest preserved errors with record "
  "support. Oral argument distills to judges' questions."),
 how_sig=("Signature standard-of-review-driven issue selection focuses appellate resources."),
 keys=["Correct legal errors; defer on facts",
  "Jurisdictional deadlines",
  "Standards: de novo, abuse of discretion, clear error",
  "Preservation prerequisite",
  "Brief strongest preserved errors",
  "Record citations throughout"],
 reqs=["Appellate deadline calendaring",
  "Record assembly",
  "Standard-of-review analysis"],
 stds=["Federal/state appellate procedure rules (public)"],
 cites=["U.S. Courts — appellate resources (public)"],
 demo=("deadline", {"event": (2026, 5, 20), "days": 30})),

dict(title="Settlement Negotiation", tier=A,
 desc_pub=("Most cases settle: negotiation resolves disputes by agreement, saving cost, time, and "
  "risk. Preparation means knowing your case's value (verdict research, strengths/weaknesses), "
  "your walk-away point, and the other side's interests - positions vs interests unlocks "
  "creative deals.\n"
  "Ethics require communicating all settlement offers to clients; the client decides. "
  "Mediation often catalyzes settlement when direct talks stall."),
 desc_sig=("Signature settlement preparation builds case-valuation models with authority "
  "tracking, so negotiation positions rest on analysis."),
 how_pub=("Lawyers value cases, get client authority with walk-away points, exchange demands and "
  "offers strategically, and document agreements precisely (releases, payment terms, "
  "confidentiality). Every offer is communicated promptly to the client."),
 how_sig=("Signature valuation models with authority logs keep negotiation disciplined."),
 keys=["Most cases settle",
  "Know value, walk-away, their interests",
  "Positions vs interests unlocks deals",
  "Communicate every offer to clients",
  "Client decides",
  "Document agreements precisely"],
 reqs=["Case valuation",
  "Client authority process",
  "Settlement documentation standards"],
 stds=["ABA Model Rule 1.4 (offers), 8.4 (public model)"],
 cites=["American Bar Association — negotiation resources (public)"],
 demo=("outcome", {"label": "Cases settling before trial", "pre": 78, "post": 92})),

dict(title="Law Firm Operations", tier=A,
 desc_pub=("Law firm operations keep the practice viable: financial management (trust accounting, "
  "billing, collections), human resources, marketing within ethics rules, technology, and "
  "facilities. Profitability metrics - realization, utilization, collection rates - guide "
  "decisions.\n"
  "Solo and small firms face the same operational demands as large ones with fewer hands: "
  "systems and outsourcing fill the gap. Succession planning protects clients when lawyers "
  "retire or die."),
 desc_sig=("Signature firm operations run on integrated dashboards - financial, matter, people - "
  "so small firms get big-firm operational visibility."),
 how_pub=("Firms implement accounting and practice systems, track KPIs monthly, market ethically, "
  "develop staff, and plan succession. Regular financial review catches problems early; "
  "technology multiplies small teams."),
 how_sig=("Signature integrated dashboards give every firm operational clarity."),
 keys=["Finance, HR, marketing, tech, facilities",
  "Metrics: realization, utilization, collection",
  "Trust accounting is sacred",
  "Small firms: systems + outsourcing",
  "Succession planning protects clients",
  "Review financials monthly"],
 reqs=["Accounting and practice systems",
  "KPI tracking",
  "Succession plans"],
 stds=["Trust accounting rules (public)",
  "Attorney advertising rules (public)"],
 cites=["American Bar Association — law practice management (public)"],
 demo=("outcome", {"label": "Collection rate", "pre": 82, "post": 94})),

dict(title="Legal Project Management", tier=A,
 desc_pub=("Legal project management (LPM) applies project discipline to matters: scope "
  "definition, phased budgets, task assignment, milestone tracking, and client communication "
  "rhythms. It answers the client's question - what will this cost, and when - with evidence.\n"
  "Alternative fee arrangements pair naturally with LPM: fixed fees need scoped, managed work. "
  "After-action reviews improve estimates over time."),
 desc_sig=("Signature LPM embeds scoping, budgeting, and tracking in the matter workflow, making "
  "predictable legal work the norm."),
 how_pub=("Lawyers scope matters with clients, build phased budgets, assign tasks with "
  "deadlines, track progress against plan, and communicate proactively. Variances trigger "
  "re-scoping conversations before they become disputes."),
 how_sig=("Signature embedded LPM makes every matter a managed project by default."),
 keys=["Scope, budget, tasks, milestones, communication",
  "Answers: cost and timing with evidence",
  "Pairs with alternative fees",
  "Track progress vs plan",
  "Re-scope before disputes",
  "After-actions improve estimates"],
 reqs=["Scoping and budgeting method",
  "Matter tracking",
  "Client communication rhythm"],
 stds=["LPM practice standards (public literature)"],
 cites=["American Bar Association — legal project management (public)"],
 demo=("outcome", {"label": "Matters on budget", "pre": 61, "post": 87})),

dict(title="Technology Competence for Lawyers", tier=A,
 desc_pub=("Technology competence is now an ethics duty: lawyers must understand the benefits and "
  "risks of relevant technology - e-discovery tools, case management, cybersecurity, AI "
  "assistants. Comment 8 to Model Rule 1.1 (adopted widely) makes it explicit.\n"
  "Core competencies: secure communication, competent e-discovery, cloud confidentiality, and "
  "critical evaluation of AI outputs (which hallucinate citations). CLE keeps skills current."),
 desc_sig=("Signature technology governance gives firms vetted tool standards with risk "
  "assessments, so competence is organizational, not individual."),
 how_pub=("Firms adopt technology policies, train lawyers on tools they use, vet vendors for "
  "confidentiality, and verify AI outputs against primary sources. CLE plans include "
  "technology annually."),
 how_sig=("Signature vetted-tool standards make firm-wide competence achievable."),
 keys=["Ethics duty: understand tech benefits and risks",
  "Secure comms, e-discovery, cloud, AI evaluation",
  "Verify AI outputs - they hallucinate",
  "Vendor confidentiality vetting",
  "CLE includes technology",
  "Competence is organizational"],
 reqs=["Technology policies",
  "Training program",
  "Vendor vetting"],
 stds=["ABA Model Rule 1.1 cmt 8 (public model)",
  "State tech-CLE rules"],
 cites=["American Bar Association — tech competence (public)"],
 demo=("outcome", {"label": "Lawyers completing tech training", "pre": 55, "post": 90})),

dict(title="The Future of Legal Practice", tier=A,
 desc_pub=("Legal practice's future: AI-assisted research and drafting (with verification), "
  "alternative business structures expanding access, unbundled and subscription services, "
  "online dispute resolution, and regulatory reform debates over non-lawyer ownership.\n"
  "The through-line is access: technology lowering cost while lawyers focus judgment where it "
  "matters most. Ethics evolve with the tools - competence, confidentiality, and supervision "
  "apply to AI as to people. Educational record."),
 desc_sig=("The Signature future-state is a legal operating system: matter lifecycle automation, "
  "verified AI assistance, and outcome accountability - with lawyer judgment governing. This "
  "database is a prototype of that system's knowledge core."),
 how_pub=("Firms adopt verified AI tools, experiment with service models, and engage bar "
  "innovation programs. Regulators pilot reforms; the profession measures access gains."),
 how_sig=("Signature's operating-system vision keeps lawyer judgment at the center of automated "
  "practice."),
 keys=["AI-assisted research/drafting (verified)",
  "Alternative structures and unbundled services",
  "Online dispute resolution grows",
  "Regulatory reform debates continue",
  "Through-line: access",
  "Ethics apply to AI as to people"],
 reqs=["AI verification discipline",
  "Service-model experimentation",
  "Access measurement"],
 stds=["Emerging AI ethics guidance (public)"],
 cites=["American Bar Association — AI resources (public)"],
 demo=("outcome", {"label": "Routine tasks automated safely", "pre": 35, "post": 68})),
]
