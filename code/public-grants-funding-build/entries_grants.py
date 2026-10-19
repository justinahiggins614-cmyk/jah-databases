#!/usr/bin/env python3
"""Entries for the Public Grants Funding databases (2026-10-17).

34 grant topics, ladder-ordered 1-34
(foundations 1-12 / compounded 13-24 / advanced 25-34).
Public = real, fact-checked domain data. Signature = Signature funding
interpretation, titles suffixed " (Signature Edition)".
No website references. No Facebook.
"""


def E(name, group, rank, tier, description, how, key_points, requirements,
      standards, citations, sig_lens, demo_data, demo_key="grant"):
    return {"name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": description,
            "how_it_works": how, "key_points": key_points,
            "requirements": requirements, "standards": standards,
            "citations": citations, "sig_lens": sig_lens,
            "demo_key": demo_key, "demo_data": demo_data}


ENTRIES = [

# ---------------- FOUNDATIONS 1-12 ----------------

E("Federal Grant Basics and Grants.gov", "Foundations", 1, "foundations",
  "Federal grants are the government's primary way of funding work it "
  "does not do itself: money awarded to states, cities, nonprofits, "
  "tribes, and researchers to carry out public purposes. Grants.gov "
  "is the single portal where federal agencies post funding "
  "opportunities and accept applications — one search across every "
  "agency, from NIH research grants to FEMA preparedness grants. "
  "Unlike contracts, grants support the recipient's work toward a "
  "public goal rather than buying goods for the government. Unlike "
  "loans, they are not repaid. The federal government awards well "
  "over half a trillion dollars in grants annually, making grants "
  "management one of the largest financial operations in the world.",
  "Agencies publish Notices of Funding Opportunity on Grants.gov "
  "with eligibility, deadlines, and review criteria. Applicants "
  "register, complete forms and narratives in the portal, and "
  "submit before the deadline — late applications are rejected "
  "without review. Agencies screen for eligibility, peer-review or "
  "panel-score the applications, and make awards. Grantees draw "
  "funds, perform the work, and report finances and results. "
  "Grants.gov's training and helpdesk support first-time "
  "applicants.",
  ["Money for public purposes to states, cities, nonprofits, researchers.",
   "Grants.gov is the single federal portal for opportunities and applications.",
   "Grants support work; contracts buy goods; loans are repaid.",
   "Federal grants exceed half a trillion dollars annually."],
  ["Applicants must meet the opportunity's eligibility rules.",
   "Registration (SAM.gov, UEI) must be complete before applying.",
   "Submissions must meet the published deadline."],
  ["Uniform Guidance (2 CFR Part 200).",
   "Federal Grant and Cooperative Agreement Act."],
  ["Grants.gov - official portal guidance.",
   "U.S. Government Accountability Office - federal grants data."],
  "In the Signature funding system a federal grant is a sworn "
  "investment: every opportunity a covenant of open competition, "
  "every award a promise that public money serves public purpose.",
  {"award": 500000, "months": 36, "match_pct": 0}),

E("State Grant Programs", "Foundations", 2, "foundations",
  "State grant programs distribute state tax dollars — and pass "
  "through federal dollars — to cities, counties, nonprofits, and "
  "businesses for state priorities: infrastructure, housing, "
  "workforce, environment, public safety. Each state runs its own "
  "portals, applications, and rules, often mirroring federal "
  "requirements with state additions. State grants fund the water "
  "plants, main streets, and training programs that federal "
  "programs miss. They also carry state policy: prevailing wage, "
  "local hiring, or climate conditions may attach. Knowing your "
  "state's grant offices is as important as knowing Grants.gov.",
  "State agencies publish opportunities on state portals and "
  "administer applications, review, and awards under state law. "
  "Many programs require local matching funds and reimburse costs "
  "rather than advancing them. Grantees sign state grant agreements "
  "with reporting, audit, and procurement terms. Legislatures "
  "appropriate the funds; agencies obligate them within statutory "
  "windows. State auditors review compliance, and clawback "
  "provisions recover misspent funds.",
  ["Distribute state dollars and pass through federal dollars.",
   "Fund infrastructure, housing, workforce, environment, safety.",
   "Mirror federal rules with state additions.",
   "Carry state policy conditions."],
  ["Applicants must meet state eligibility and match rules.",
   "Agreements bind grantees to reporting and audit terms.",
   "Funds must be obligated within statutory windows."],
  ["State grant administration statutes.",
   "State procurement and audit requirements."],
  ["State grant office program guides.",
   "National Governors Association - grants management."],
  "In the Signature funding system a state grant is a sworn "
  "partnership: every appropriation a covenant of shared "
  "priorities, every local match a promise of skin in the game.",
  {"award": 250000, "months": 24, "match_pct": 25}),

E("Formula Grants", "Foundations", 3, "foundations",
  "Formula grants allocate federal money by statute-written "
  "formulas — population, poverty, road miles — not by "
  "competition. Congress writes the formula into law; the agency "
  "does the math and sends the money to every eligible state or "
  "locality. Highway funds, Title I education aid, Community "
  "Development Block Grants, and Medicaid's federal share all "
  "flow by formula. The politics live in the formula's factors: "
  "each variable shifts millions between states. Formula grants "
  "give recipients predictable funding they can plan around, "
  "year after year.",
  "The authorizing statute defines the formula factors and "
  "weights. Agencies compute allocations from census, economic, "
  "and program data, publish the tables, and award to eligible "
  "recipients who submit required plans or applications. "
  "Recipients spend within the program's purposes and report. "
  "Reauthorizations revisit the factors — the decennial census "
  "reshuffles many formulas. Hold-harmless provisions often "
  "cushion losers from sudden drops.",
  ["Allocated by statutory formula, not competition.",
   "Factors: population, poverty, road miles, and more.",
   "Examples: highways, Title I, CDBG, Medicaid share.",
   "Predictable funding recipients can plan around."],
  ["Recipients must be eligible under the statute.",
   "Required plans or applications must be submitted.",
   "Spending must stay within program purposes."],
  ["Authorizing statutes' formula provisions.",
   "Uniform Guidance (2 CFR Part 200)."],
  ["Congressional Research Service - formula grant reports.",
   "Authorizing statutes."],
  "In the Signature funding system a formula grant is a sworn "
  "apportionment: every factor a covenant of fair measure, every "
  "published table a promise that the math is open.",
  {"award": 2000000, "months": 12, "match_pct": 20}),

E("Discretionary and Project Grants", "Foundations", 4, "foundations",
  "Discretionary grants — also called project grants — are won, "
  "not allocated: agencies score applications and fund the best. "
  "Research grants, demonstration projects, and competitive "
  "infrastructure programs work this way. A Notice of Funding "
  "Opportunity sets the criteria; peer reviewers or panels score "
  "each proposal; program officials select within budget. Winning "
  "requires a compelling need, a sound approach, capable staff, "
  "and a credible budget. Losers get feedback and can reapply. "
  "Competition concentrates money where proposals are strongest — "
  "which is both the point and the perennial equity debate.",
  "Applicants write narratives, work plans, and budgets to the "
  "NOFO's criteria. Agencies check eligibility, then route to "
  "reviewers who score independently. Panels or officials rank "
  "and select, considering scores, program balance, and "
  "priorities. Awards issue as grants or cooperative agreements "
  "— the latter with substantial agency involvement. Unsuccessful "
  "applicants may request debriefs. Performance is monitored "
  "against the approved scope.",
  ["Won by competition, not allocated by formula.",
   "Reviewers score; officials select within budget.",
   "Winning needs need, approach, capacity, budget.",
   "Feedback lets losers improve and reapply."],
  ["Applications must address all review criteria.",
   "Deadlines and page limits are strictly enforced.",
   "Budgets must be allowable and realistic."],
  ["Uniform Guidance (2 CFR Part 200).",
   "Agency-specific NOFO requirements."],
  ["Grants.gov - application guidance.",
   "Agency NOFO archives."],
  "In the Signature funding system a discretionary grant is a "
  "sworn contest of merit: every scored criterion a covenant of "
  "fair judgment, every award a promise that the best plan wins.",
  {"award": 750000, "months": 36, "match_pct": 0}),

E("Block Grants", "Foundations", 5, "foundations",
  "Block grants give states and localities broad money for broad "
  "purposes with wide discretion: the Community Development Block "
  "Grant, the Community Services Block Grant, and substance-abuse "
  "and mental-health block grants are the classic examples. "
  "Congress sets the goals and guardrails; recipients design the "
  "programs — housing rehab here, senior services there. Block "
  "grants embody devolution: Washington trusts states to know "
  "their needs. Critics note the trade-off — flexibility can "
  "dilute the original purpose, and funding often erodes over "
  "time. Reporting still tracks national goals.",
  "Recipients submit consolidated plans describing how block "
  "funds will meet statutory goals, then subaward or operate "
  "programs within the broad purposes. Federal rules set "
  "spending caps on administration, require citizen "
  "participation, and bar certain uses. Grantees report "
  "accomplishments against national objectives. Monitoring "
  "checks compliance with the broad rules rather than "
  "micromanaging choices. Reauthorizations debate the "
  "flexibility-accountability balance anew.",
  ["Broad money for broad purposes with wide discretion.",
   "Recipients design programs within statutory goals.",
   "Embody devolution: trust in state and local knowledge.",
   "Trade-off: flexibility vs. purpose dilution."],
  ["Spending must stay within statutory purposes.",
   "Citizen participation is required in planning.",
   "Administrative caps must be observed."],
  ["Authorizing statutes (e.g., Housing and Community Development Act).",
   "Uniform Guidance (2 CFR Part 200)."],
  ["Department of Housing and Urban Development - CDBG guidance.",
   "Congressional Research Service - block grant reports."],
  "In the Signature funding system a block grant is a sworn "
  "trust: broad purposes a covenant of local wisdom, every "
  "consolidated plan a promise that flexibility serves the "
  "goals.",
  {"award": 1500000, "months": 12, "match_pct": 0}),

E("Matching Requirements", "Foundations", 6, "foundations",
  "Matching requirements make grantees put their own money — or "
  "in-kind value — beside the federal dollar: a 25 percent match "
  "on a million-dollar award means the grantee provides $250,000. "
  "Match proves commitment, stretches federal funds, and tests "
  "whether the project matters locally. It can be cash or in-kind "
  "— donated space, volunteer hours valued at market rates, "
  "equipment use — but it must be documented, allowable, and not "
  "counted toward another federal match. Hardship waivers exist "
  "for distressed communities. The match is where many "
  "applications live or die.",
  "The NOFO states the match percentage and type. Applicants "
  "commit match in the budget with source documentation — "
  "letters, valuations, timesheets. During performance, grantees "
  "track match expenditures alongside federal funds, meeting "
  "proportional benchmarks. In-kind contributions need "
  "verifiable records: volunteer logs, appraisals, use logs. "
  "Shortfalls at closeout can reduce the award. Auditors test "
  "match rigorously because it is the most fudged number in "
  "grants.",
  ["Grantees contribute cash or in-kind beside federal funds.",
   "Proves commitment and stretches federal dollars.",
   "Must be documented, allowable, not double-counted.",
   "Hardship waivers exist for distressed communities."],
  ["Match must be committed with source documentation.",
   "In-kind needs verifiable records.",
   "Shortfalls can reduce the award."],
  ["Uniform Guidance 2 CFR 200.306 (cost sharing/matching).",
   "Program-specific match provisions."],
  ["2 CFR 200.306.",
   "Agency grant manuals."],
  "In the Signature funding system match is a sworn "
  "partnership: every local dollar a covenant of shared "
  "commitment, every documented hour a promise counted "
  "honestly.",
  {"award": 1000000, "months": 36, "match_pct": 25}),

E("Eligibility Determination", "Foundations", 7, "foundations",
  "Eligibility determination is the threshold question of every "
  "grant: who may apply. Statutes and NOFOs define eligible "
  "applicants — states, local governments, tribes, nonprofits, "
  "institutions of higher education, sometimes for-profits or "
  "individuals — and eligible activities, costs, and "
  "beneficiaries. Getting it wrong wastes everyone's time: "
  "ineligible applications are rejected without review. Smart "
  "applicants read the eligibility section first, verify their "
  "status — nonprofit determination letters, tribal recognition, "
  "accreditation — and confirm their project fits before writing "
  "a word.",
  "Agencies screen applications for threshold eligibility before "
  "merit review: applicant type, registration, project fit, "
  "deadline. Nonprofits prove 501(c)(3) status; governments "
  "prove jurisdiction; tribes prove federal recognition. "
  "Beneficiary rules — low-income, rural, underserved — shape "
  "project design. Some programs limit applicants per state or "
  "require partnerships. Eligibility findings are documented; "
  "rejected applicants are notified with reasons.",
  ["Threshold question: who may apply and for what.",
   "Defined by statute and NOFO.",
   "Ineligible applications rejected without review.",
   "Read eligibility first, before writing."],
  ["Applicant type must match the eligible list.",
   "Status documentation must be current.",
   "Project must fit eligible activities."],
  ["Authorizing statutes (eligibility provisions).",
   "NOFO eligibility sections."],
  ["Grants.gov - eligibility guidance.",
   "Agency NOFOs."],
  "In the Signature funding system eligibility is a sworn "
  "threshold: every defined class a covenant of intended "
  "benefit, every screened application a promise that the "
  "rules are real.",
  {"award": 300000, "months": 24, "match_pct": 10}),

E("SAM.gov Registration", "Foundations", 8, "foundations",
  "SAM.gov — the System for Award Management — is the federal "
  "government's registry of everyone who wants to do business "
  "with it: to apply for grants, bid contracts, or receive "
  "payments, an entity must register and keep the registration "
  "active. Registration captures the legal name, address, "
  "banking for electronic payment, and representations and "
  "certifications. It is free — commercial look-alikes charge "
  "for what SAM.gov does at no cost, a perennial scam warning. "
  "Lapsed registration freezes awards and payments, so renewal "
  "every year is a grants-management sacrament.",
  "The entity's administrator creates the registration with the "
  "legal business name matching tax records, designates points "
  "of contact, enters banking, and completes representations "
  "about size, ownership, and compliance. Annual renewal "
  "revalidates everything; changes update as they happen. "
  "Agencies check active status before award and payment. "
  "Exclusions — debarred entities — are listed publicly. Help "
  "comes from the Federal Service Desk, not paid middlemen.",
  ["Registry required to apply for grants and receive payment.",
   "Captures identity, banking, certifications.",
   "Free — paid look-alikes are scams.",
   "Annual renewal; lapse freezes awards and payments."],
  ["Registration must be active at application and award.",
   "Legal name must match tax records.",
   "Banking must be current for electronic payment."],
  ["2 CFR Part 25 (universal identifier and SAM requirements).",
   "Federal Acquisition Regulation (contractor registration)."],
  ["General Services Administration - SAM.gov help.",
   "2 CFR Part 25."],
  "In the Signature funding system SAM.gov is a sworn roll: "
  "every registered entity a covenant of identity, every "
  "renewal a promise of currency, every free registration a "
  "vow against the scammers.",
  {"award": 100000, "months": 12, "match_pct": 0}),

E("The Unique Entity Identifier (UEI)", "Foundations", 9, "foundations",
  "The Unique Entity Identifier is the twelve-character code that "
  "identifies every organization doing business with the federal "
  "government — the successor to the DUNS number, which GSA retired "
  "in 2022. Issued free through SAM.gov, the UEI keys every grant "
  "application, award, and payment record to the right entity. "
  "Subrecipients need UEIs too, so prime grantees must collect them "
  "down the chain. The identifier never changes, even as names and "
  "addresses do, giving the government a stable spine for its "
  "trillions in transactions.",
  "Entities receive their UEI automatically upon SAM.gov "
  "registration. Applicants enter it on every federal form; "
  "agencies validate it before award. Prime recipients collect "
  "subrecipient UEIs and report them in subaward data. Systems "
  "link the UEI to payment, audit, and performance records. "
  "Changes to entity information update in SAM.gov while the UEI "
  "persists. Help with UEI issues comes from the Federal Service "
  "Desk.",
  ["Twelve-character ID for federal business; replaced DUNS in 2022.",
   "Free through SAM.gov; never changes.",
   "Required on applications, awards, payments.",
   "Subrecipients need UEIs too."],
  ["Every applicant and subrecipient needs a UEI.",
   "UEI must validate before award.",
   "Entity data must stay current in SAM.gov."],
  ["2 CFR Part 25.",
   "GSA UEI transition guidance."],
  ["General Services Administration - UEI guidance.",
   "2 CFR Part 25."],
  "In the Signature funding system the UEI is a sworn name that "
  "never changes: every transaction keyed true, every subrecipient "
  "named, every dollar traceable to its bearer.",
  {"award": 200000, "months": 24, "match_pct": 0}),

E("Application Narratives", "Foundations", 10, "foundations",
  "The application narrative is where grants are won or lost: the "
  "written case answering the NOFO's criteria — need, approach, "
  "capacity, evaluation, budget justification — in the allowed "
  "pages. Reviewers score what the narrative proves, not what the "
  "applicant knows. Winning narratives lead with a compelling "
  "need backed by data, present a logical work plan with "
  "measurable objectives, demonstrate qualified staff and "
  "partnerships, and tie every budget line to the work. Plain "
  "language, headings mirroring the criteria, and honest "
  "evaluation plans beat jargon and padding every time.",
  "Writers dissect the NOFO's scoring rubric and outline the "
  "narrative to it, section by section. Data establishes need; "
  "logic models connect activities to outcomes; timelines show "
  "feasibility; bios and letters prove capacity. The budget "
  "narrative justifies each cost as reasonable, allocable, and "
  "necessary. Internal review — a mock panel scoring the draft "
  "— catches gaps before submission. Final checks verify page "
  "limits, fonts, and attachments.",
  ["The written case answering the NOFO's criteria.",
   "Reviewers score what the narrative proves.",
   "Winning formula: data-backed need, logical plan, capacity, justified budget.",
   "Plain language and rubric-mirroring beat jargon."],
  ["Must address every scored criterion.",
   "Must respect page, font, and attachment limits.",
   "Budget justification must tie costs to work."],
  ["NOFO application requirements.",
   "Uniform Guidance cost principles (budget basis)."],
  ["Agency NOFOs and application guides.",
   "Grants.gov - application guidance."],
  "In the Signature funding system the narrative is a sworn "
  "argument: every data point a covenant of truth, every "
  "objective a measurable promise, every budget line a vow of "
  "stewardship.",
  {"award": 450000, "months": 36, "match_pct": 15}),

E("Grant Budget Development", "Foundations", 11, "foundations",
  "Grant budget development translates the work plan into dollars: "
  "personnel, fringe, travel, equipment, supplies, contractual, "
  "and indirect costs, each estimated, justified, and totaled. "
  "The budget must be reasonable (what the work costs), allocable "
  "(benefiting the grant), and allowable (permitted by the cost "
  "principles) — the three tests of 2 CFR Part 200. Reviewers "
  "read budgets as credibility tests: inflated travel or mystery "
  "consultants sink proposals. Detailed budgets with math shown "
  "— hours times rates, units times prices — win trust.",
  "Budget builders cost each work-plan activity: salaries by "
  "effort percentage, fringe at audited rates, travel by "
  "destination, equipment quotes, supply lists. Indirect costs "
  "apply the negotiated rate to the proper base. The budget "
  "narrative shows the math and ties each line to objectives. "
  "Internal review checks allowability and reasonableness. "
  "Negotiation may trim the award; the grantee then revises "
  "scope or finds match.",
  ["Translate the work plan into justified dollars.",
   "Three tests: reasonable, allocable, allowable.",
   "Budgets are credibility tests for reviewers.",
   "Show the math: hours x rates, units x prices."],
  ["Costs must pass reasonable/allocable/allowable tests.",
   "Math must be shown and tied to objectives.",
   "Indirect costs need a negotiated rate or de minimis."],
  ["2 CFR Part 200 Subpart E (cost principles).",
   "NOFO budget requirements."],
  ["2 CFR Part 200 Subpart E.",
   "Agency budget guidance."],
  "In the Signature funding system the budget is a sworn "
  "accounting of intent: every line a covenant of necessity, "
  "every calculation a promise of honesty, every total a vow "
  "of stewardship.",
  {"award": 600000, "months": 36, "match_pct": 20}),

E("Indirect Cost Rates", "Foundations", 12, "foundations",
  "Indirect cost rates recover the overhead grants consume but "
  "cannot see: accounting, HR, facilities, utilities — the "
  "infrastructure that makes the project possible. A negotiated "
  "indirect cost rate agreement (NICRA) with the cognizant "
  "federal agency sets the percentage applied to a base, usually "
  "modified total direct costs. Organizations without a NICRA "
  "may use the 10 percent de minimis rate. Rates are negotiated "
  "from audited cost data and carry forward with adjustments. "
  "The indirect rate is where small nonprofits often leave "
  "money — and sustainability — on the table.",
  "Organizations prepare indirect cost proposals from audited "
  "financials, allocating costs to the base per 2 CFR Part 200 "
  "Appendix rules. The cognizant agency negotiates and issues "
  "the NICRA. Grantees apply the rate to each award's base and "
  "claim the dollars. Provisional and final rates true up over "
  "time. Programs may cap recovery below the negotiated rate — "
  "the difference is real subsidy the grantee absorbs.",
  ["Recover overhead: accounting, HR, facilities, utilities.",
   "NICRA sets the negotiated percentage.",
   "No NICRA? The 10 percent de minimis rate applies.",
   "Negotiated from audited cost data."],
  ["Proposals must follow 2 CFR Part 200 Appendices.",
   "Rates apply to the proper base (usually MTDC).",
   "Program caps must be honored where imposed."],
  ["2 CFR Part 200 Appendices III, IV, VII.",
   "Cognizant agency rate agreements."],
  ["2 CFR Part 200 cost principle appendices.",
   "HHS Division of Cost Allocation guidance."],
  "In the Signature funding system the indirect rate is a sworn "
  "recognition of the unseen: every audited percentage a "
  "covenant that overhead is real, every claimed dollar a "
  "promise of honest allocation.",
  {"award": 800000, "months": 48, "match_pct": 0}),

# ---------------- COMPOUNDED 13-24 ----------------

E("Cost Sharing and Match Documentation", "Compounded", 13, "compounded",
  "Cost sharing and match documentation is the proof behind the "
  "promise: the records showing the grantee actually contributed "
  "its committed share. Auditors test match ruthlessly — it is "
  "the most commonly disallowed cost in single audits. Cash match "
  "needs expenditure records; in-kind needs volunteer logs with "
  "hours and rates, donated-space valuations, and equipment use "
  "records. Every claimed dollar must be verifiable, necessary, "
  "and not counted elsewhere. Systems that track match in real "
  "time survive audits; shoeboxes of receipts do not.",
  "Grantees set up match tracking alongside grant accounting: "
  "separate codes, timesheets for donated labor, appraisals for "
  "donated property, logs for equipment use. Supervisors certify "
  "in-kind records. Finance reconciles match to budget "
  "periodically, catching shortfalls early. At closeout, the "
  "final reports certify total match delivered. Auditors sample "
  "the documentation against 2 CFR 200.306's verifiability and "
  "non-duplication rules.",
  ["Proof the grantee delivered its committed share.",
   "Most commonly disallowed cost in single audits.",
   "Cash needs records; in-kind needs logs and valuations.",
   "Real-time tracking survives; shoeboxes do not."],
  ["Match must be verifiable from records.",
   "Cannot be counted toward another federal award.",
   "Must be necessary and reasonable for the project."],
  ["2 CFR 200.306.",
   "Single audit compliance supplements."],
  ["2 CFR 200.306.",
   "AICPA audit guidance on matching."],
  "In the Signature funding system match documentation is a "
  "sworn ledger of partnership: every logged hour a covenant "
  "kept, every valuation an honest measure, every reconciled "
  "total a promise fulfilled.",
  {"award": 900000, "months": 36, "match_pct": 30}),

E("Grant Review and Scoring", "Compounded", 14, "compounded",
  "Grant review and scoring is the machinery of fair competition: "
  "how agencies turn piles of proposals into defensible awards. "
  "Peer reviewers — outside experts — or federal panels score "
  "each application against published criteria, independently "
  "and confidentially. Scores are normalized, ranked, and "
  "briefed to selecting officials who consider program balance, "
  "geography, and priorities alongside scores. Conflict-of-"
  "interest rules bar reviewers from scoring competitors or "
  "collaborators. The whole apparatus exists so a rejected "
  "applicant can be shown the process was fair.",
  "Agencies recruit qualified reviewers, train them on criteria "
  "and scoring scales, and assign applications avoiding "
  "conflicts. Reviewers read, score, and write strengths and "
  "weaknesses; panels discuss and reconcile. Staff compile "
  "rankings and funding scenarios for the selecting official, "
  "who documents the decision. Applicants receive scores and "
  "summaries. Protests are rare in grants — but documentation "
  "must withstand scrutiny.",
  ["Peer or panel scoring against published criteria.",
   "Independent, confidential review.",
   "Conflict-of-interest rules protect fairness.",
   "Documentation must withstand scrutiny."],
  ["Criteria must be published in the NOFO.",
   "Reviewers must be qualified and conflict-free.",
   "Decisions must be documented."],
  ["Agency peer review policies.",
   "Uniform Guidance (merit review expectations)."],
  ["Agency peer review manuals.",
   "NIH peer review policies (model practice)."],
  "In the Signature funding system review is a sworn judgment: "
  "every score a covenant of honest reading, every conflict "
  "screen a promise of impartiality, every documented decision "
  "a vow of defensibility.",
  {"award": 1200000, "months": 48, "match_pct": 0}),

E("Notices of Award", "Compounded", 15, "compounded",
  "The Notice of Award is the grant's birth certificate: the "
  "legally binding document obligating federal funds and stating "
  "every term — amount, period of performance, scope, budget, "
  "reporting, and special conditions. Until the NoA issues, "
  "there is no award, no matter what anyone said; costs incurred "
  "before it are at the applicant's risk. Grantees must read "
  "every line: the NoA incorporates the Uniform Guidance, "
  "program rules, and any agency-specific conditions like "
  "spending restrictions or prior approvals. Amendments modify "
  "it; the latest version governs.",
  "Grants officers issue the NoA after selection and "
  "negotiation, obligating funds in the payment system. The "
  "grantee's authorized official accepts by drawing funds or "
  "signing. Program staff review terms with the grantee: "
  "unallowable costs, prior-approval triggers, reporting "
  "calendars. Amendments — for budget revisions, extensions, "
  "or scope changes — issue as revised NoAs. The award file "
  "keeps every version.",
  ["The legally binding document obligating funds.",
   "States amount, period, scope, budget, reporting, conditions.",
   "No award exists until the NoA issues.",
   "Amendments modify; the latest version governs."],
  ["Pre-award costs are at the applicant's risk.",
   "Terms incorporate Uniform Guidance and program rules.",
   "Acceptance binds the grantee to all conditions."],
  ["2 CFR 200.211 (award information).",
   "Agency grants management manuals."],
  ["2 CFR 200.211.",
   "HHS Grants Policy Statement (model)."],
  "In the Signature funding system the Notice of Award is a "
  "sworn charter: every term a covenant of the bargain, every "
  "obligated dollar a promise backed by law.",
  {"award": 1100000, "months": 36, "match_pct": 10}),

E("Period of Performance", "Compounded", 16, "compounded",
  "The period of performance is the grant's lifespan: the start "
  "and end dates within which work must happen and costs must be "
  "incurred. Costs outside the period are unallowable, with narrow "
  "exceptions for pre-award costs the agency approves in writing. "
  "Obligation deadlines add pressure — some funds expire if not "
  "obligated in time. Extensions are possible but not automatic: "
  "no-cost extensions need justification and approval before "
  "expiry. Managing the clock — spending neither too fast nor too "
  "slow — is a core grants skill.",
  "The NoA sets the period; grantees plan spending and "
  "milestones against it. Finance tracks burn rates and flags "
  "under- or over-spending. As expiry nears, grantees request "
  "extensions with justification and revised timelines, or "
  "accelerate responsibly. Agencies approve or deny before the "
  "end date — expired awards cannot be extended. Closeout "
  "reconciles final costs to the period; late costs are "
  "disallowed.",
  ["The grant's lifespan: costs must fall within it.",
   "Pre-award costs need written approval.",
   "Extensions need justification before expiry.",
   "Managing the clock is a core skill."],
  ["Costs must be incurred within the period.",
   "Extension requests must precede expiration.",
   "Obligation deadlines must be met."],
  ["2 CFR 200.309 (period of performance).",
   "Agency extension policies."],
  ["2 CFR 200.309.",
   "Agency grants manuals."],
  "In the Signature funding system the period of performance "
  "is a sworn season: every on-time milestone a covenant kept, "
  "every justified extension an honest asking, every closed "
  "period a finished promise.",
  {"award": 700000, "months": 24, "match_pct": 0}),

E("Allowable and Unallowable Costs", "Compounded", 17, "compounded",
  "Allowable costs are what grants may pay; unallowable costs are "
  "what they must not — and the line decides audits. A cost is "
  "allowable when it is reasonable, allocable to the award, "
  "consistent with policy, and conforms to the cost principles' "
  "limits. Unallowable by nature: alcohol, entertainment, "
  "lobbying, fines, and donations top the list. Some costs need "
  "prior approval — equipment, travel deviations, participant "
  "support. Gray areas go to the grants officer before spending, "
  "because after-the-fact justification rarely persuades an "
  "auditor.",
  "Grantees build allowability into purchasing: trained staff, "
  "checklists, and approval workflows catch problems before "
  "payment. Finance codes costs to awards and reviews for "
  "reasonableness and allocability. Prior-approval requests go "
  "to the agency with justification. Auditors sample "
  "transactions against Subpart E, questioning the unallowable "
  "and disallowing the egregious. Policies document the "
  "organization's consistent treatment of similar costs.",
  ["Allowable: reasonable, allocable, consistent, within limits.",
   "Unallowable: alcohol, entertainment, lobbying, fines, donations.",
   "Some costs need prior approval.",
   "Ask before spending; auditors rarely forgive after."],
  ["Costs must meet all four allowability tests.",
   "Unallowable costs must be excluded from claims.",
   "Prior approvals must be obtained in advance."],
  ["2 CFR Part 200 Subpart E.",
   "Agency-specific cost restrictions."],
  ["2 CFR Part 200 Subpart E.",
   "AICPA not-for-profit audit guidance."],
  "In the Signature funding system allowability is a sworn "
  "boundary: every reasonable cost a covenant honored, every "
  "unallowable one a line respected, every prior approval a "
  "promise sought in time.",
  {"award": 550000, "months": 36, "match_pct": 5}),

E("Uniform Guidance: 2 CFR Part 200", "Compounded", 18, "compounded",
  "The Uniform Guidance — 2 CFR Part 200 — is the constitution of "
  "federal grants: one rulebook replacing eight agency circulars "
  "in 2014, governing how grants are made and managed "
  "government-wide. Its subparts cover definitions, pre-award "
  "requirements, post-award administration, cost principles, and "
  "audit. Every federal grant incorporates it; every grantee "
  "lives under it. Revisions — notably the 2024 update raising "
  "thresholds and the de minimis rate to 15 percent — keep it "
  "current. To work with federal money is to know Part 200.",
  "Agencies write their regulations and NOFOs within Part 200's "
  "frame; deviations need OMB approval. Grantees build policies "
  "— procurement, compensation, travel, financial management — "
  "to its standards. Auditors test compliance against its "
  "Compliance Supplement. Training programs teach it section by "
  "section. When rules conflict, Part 200's hierarchy resolves: "
  "statute first, then regulation, then agency policy, then the "
  "award terms.",
  ["The government-wide rulebook for federal grants.",
   "Replaced eight circulars in 2014.",
   "Covers pre-award, post-award, cost principles, audit.",
   "2024 update raised thresholds and de minimis to 15%."],
  ["Grantees must comply with all applicable subparts.",
   "Policies must meet Part 200 standards.",
   "Deviations need OMB approval."],
  ["2 CFR Part 200 (all subparts).",
   "OMB revisions and guidance."],
  ["Office of Management and Budget - 2 CFR Part 200.",
   "Federal Register revisions (2014, 2020, 2024)."],
  "In the Signature funding system the Uniform Guidance is a "
  "sworn constitution: every subpart a covenant of order, every "
  "threshold a promise of proportionality, every revision a vow "
  "to keep the rules worthy.",
  {"award": 1000000, "months": 36, "match_pct": 0}),

E("Procurement Standards for Grantees", "Compounded", 19, "compounded",
  "Grantees spending federal dollars must buy like the public is "
  "watching — because it is. Part 200's procurement standards "
  "require full and open competition, with method thresholds: "
  "micro-purchases up to $10,000, small purchases to $250,000 "
  "with quotes, and sealed bids or competitive proposals above. "
  "Sole-source needs documented justification. Cost and price "
  "analysis must support the decision. Grantees must avoid "
  "conflicts of interest and document every step. Procurement "
  "violations are among the most common audit findings — and "
  "the most preventable.",
  "Organizations write procurement policies to Part 200, train "
  "buyers, and run competitions with written solicitations, "
  "evaluation criteria, and award documentation. Quotes are "
  "collected for small purchases; formal bids or RFPs govern "
  "large ones. Conflict disclosures are collected; debarment "
  "is checked. Files keep the solicitation, quotes, analysis, "
  "and award decision. Auditors sample procurements for "
  "competition and documentation.",
  ["Full and open competition with threshold-based methods.",
   "Micro $10k, small to $250k, formal above.",
   "Sole-source needs documented justification.",
   "Most common — and most preventable — audit findings."],
  ["Procurements must be competitive and documented.",
   "Conflicts of interest must be avoided and disclosed.",
   "Debarment must be checked before award."],
  ["2 CFR 200.317-200.327.",
   "Organizational procurement policies."],
  ["2 CFR 200.317-200.327.",
   "OMB procurement guidance."],
  "In the Signature funding system procurement is a sworn "
  "marketplace: every competition a covenant of fairness, every "
  "documented decision a promise of integrity, every avoided "
  "conflict a vow of clean hands.",
  {"award": 850000, "months": 36, "match_pct": 0}),

E("Subrecipient Monitoring", "Compounded", 20, "compounded",
  "When grantees pass federal money to subrecipients, the "
  "responsibility follows the dollar: prime recipients must "
  "monitor subrecipients' compliance with award terms. Part "
  "200 requires risk assessments, written subaward agreements "
  "with all federal terms flowed down, ongoing monitoring — "
  "reports, site visits, audits — and enforcement for "
  "noncompliance. The prime remains liable to the federal "
  "agency for the subrecipient's failures. Pass-through entities "
  "that treat subawards as fire-and-forget learn this in "
  "audits.",
  "Primes evaluate each subrecipient's risk — newness, past "
  "findings, award size — and tailor monitoring: desk reviews "
  "for all, site visits for the risky. Subaward agreements "
  "state the federal award data, terms, and reporting duties. "
  "Monitoring reviews financial and performance reports, "
  "follows up findings, and issues management decisions on "
  "audit reports. Noncompliance brings corrective action, and "
  "if needed, funding holds or termination.",
  ["Responsibility follows the dollar to subrecipients.",
   "Requires risk assessment, flowed-down terms, monitoring.",
   "Prime remains liable for subrecipient failures.",
   "Fire-and-forget subawards fail audits."],
  ["Subawards need written agreements with federal terms.",
   "Risk assessments must drive monitoring intensity.",
   "Audit findings need management decisions."],
  ["2 CFR 200.331-200.333.",
   "Single audit subrecipient requirements."],
  ["2 CFR 200.331-200.333.",
   "AICPA guidance on pass-through responsibilities."],
  "In the Signature funding system subrecipient monitoring is "
  "a sworn chain of trust: every flowed-down term a covenant "
  "carried forward, every site visit a promise of attention, "
  "every corrected finding a vow kept down the line.",
  {"award": 2000000, "months": 48, "match_pct": 0}),

E("Payment Management and Drawdowns", "Compounded", 21, "compounded",
  "Grantees get federal cash through payment management systems "
  "— HHS's PMS, Treasury's ASAP — drawing funds as costs are "
  "incurred. The rule is simple and strict: draw only for "
  "immediate needs, minimize the time between draw and "
  "disbursement, and never draw to park cash. Advances are "
  "allowed but policed; most grantees operate on reimbursement, "
  "spending first and drawing after. Interest earned on advances "
  "must generally be remitted. Draw patterns are audited — "
  "lump-sum draws before long idle periods invite findings.",
  "Finance staff request draws tied to documented expenditures, "
  "reconciling PMS balances to the general ledger. Cash "
  "management procedures set draw frequency and approvals. "
  "Interest on advances is calculated and remitted annually. "
  "Agencies monitor draw patterns against reported "
  "expenditures; anomalies trigger review. At closeout, final "
  "draws reconcile to final reports and excess cash is "
  "returned.",
  ["Draw funds as costs are incurred, for immediate needs.",
   "Minimize time between draw and disbursement.",
   "Advances policed; interest remitted.",
   "Draw patterns audited."],
  ["Draws must tie to documented expenditures.",
   "Cash balances must be minimized.",
   "Reconciliation to the ledger required."],
  ["2 CFR 200.305 (payment).",
   "Treasury cash management rules (31 CFR 205)."],
  ["2 CFR 200.305.",
   "HHS Payment Management System guidance."],
  "In the Signature funding system drawdowns are a sworn "
  "discipline of cash: every draw a covenant of immediate need, "
  "every reconciliation a promise of exactness, every remitted "
  "interest a vow of clean hands.",
  {"award": 950000, "months": 36, "match_pct": 0}),

E("Continuation Applications", "Compounded", 22, "compounded",
  "Multi-year grants fund in budget periods — usually twelve "
  "months — with continuation applications releasing each next "
  "year's money. The non-competing continuation is not a new "
  "competition but a checkpoint: progress reports, financial "
  "status, and next year's budget proving the project earns its "
  "next installment. Agencies can reduce, restrict, or withhold "
  "continuation for poor performance or noncompliance. Grantees "
  "treat each continuation like a mini-application, because "
  "that is what it is.",
  "Grantees submit progress reports, financial reports, and "
  "next-period budgets 45-90 days before the budget period "
  "ends. Program officers review accomplishments against "
  "objectives and compliance history. Grants management "
  "verifies financial standing. The agency issues a new NoA "
  "for the next period — possibly with special conditions for "
  "troubled grantees. Carryover requests ride along when "
  "unspent funds should continue.",
  ["Annual checkpoint releasing each next year's funds.",
   "Not a new competition — a performance review.",
   "Poor performance can reduce or withhold continuation.",
   "Treat each like a mini-application."],
  ["Progress and financial reports must be current.",
   "Next-period budgets must be justified.",
   "Submissions must precede the period end."],
  ["2 CFR 200 (period and reporting provisions).",
   "Agency continuation policies."],
  ["NIH and HHS continuation guidance (model).",
   "Agency grants manuals."],
  "In the Signature funding system continuation is a sworn "
  "renewal: every progress report a covenant of earned trust, "
  "every next-year award a promise that good work continues.",
  {"award": 1500000, "months": 60, "match_pct": 0}),

E("No-Cost Extensions", "Compounded", 23, "compounded",
  "A no-cost extension gives a grantee more time without more "
  "money: the period of performance lengthens, the budget does "
  "not. Agencies grant them when work needs finishing — a "
  "delayed hire, a slow enrollment — and funds remain. The "
  "first extension is often grantee-approved under expanded "
  "authority; later ones need agency approval with strong "
  "justification. Extensions cannot cure fundamentally broken "
  "projects or fund new scope, and requests must arrive before "
  "expiry. Well-managed grants finish on time; extensions are "
  "for the honest delay, not the chronic drift.",
  "Grantees request extensions before the end date, explaining "
  "the delay, the remaining work, and the funds available. "
  "Under expanded authority, the authorized official approves "
  "the first extension and notifies the agency. Agency-approved "
  "extensions need program officer concurrence. The revised NoA "
  "sets the new end date. Work plans adjust; unobligated funds "
  "carry forward within the extension. Repeated extensions "
  "draw scrutiny.",
  ["More time without more money.",
   "For honest delays with funds remaining.",
   "First often grantee-approved; later need agency approval.",
   "Must be requested before expiry."],
  ["Justification must show remaining work and funds.",
   "Requests must precede the end date.",
   "Cannot fund new scope."],
  ["2 CFR 200.309 and agency extension policies.",
   "Expanded authority provisions."],
  ["NIH grants policy on extensions (model).",
   "Agency grants manuals."],
  "In the Signature funding system a no-cost extension is a "
  "sworn reprieve: every justified delay a covenant of "
  "honesty, every finished project a promise completed in "
  "its own good time.",
  {"award": 500000, "months": 42, "match_pct": 0}),

E("Carryover of Funds", "Compounded", 24, "compounded",
  "Carryover lets unspent funds move from one budget period to "
  "the next instead of expiring: permission to finish the work "
  "with the money already awarded. Some agencies allow it "
  "automatically under expanded authority; others require "
  "written requests showing why funds remain and how they will "
  "be used. Large unobligated balances raise questions — "
  "reviewers wonder whether the scope was too ambitious or the "
  "management too slow. Planned, justified carryover is normal; "
  "chronic carryover is a warning light.",
  "Grantees estimate unobligated balances before period end "
  "and request carryover with explanations and revised budgets. "
  "Agencies approve, reduce the next year's new funds "
  "accordingly, or deny. Finance tracks carried funds "
  "separately to preserve their identity. Auditors check that "
  "carried funds were obligated within their original period "
  "rules. Repeated large carryovers trigger program review of "
  "scope and capacity.",
  ["Move unspent funds to the next budget period.",
   "Automatic under expanded authority, or by request.",
   "Large balances raise questions about scope and management.",
   "Planned carryover normal; chronic carryover a warning."],
  ["Requests need explanations and revised budgets.",
   "Carried funds keep their original rules.",
   "Next-year funds may be offset."],
  ["Agency carryover policies.",
   "2 CFR 200 (period provisions)."],
  ["NIH carryover guidance (model).",
   "Agency grants manuals."],
  "In the Signature funding system carryover is a sworn "
  "continuance: every justified balance a covenant of "
  "unfinished work honestly named, every approved request a "
  "promise the money still serves.",
  {"award": 800000, "months": 36, "match_pct": 0}),

# ---------------- ADVANCED 25-34 ----------------

E("The Single Audit", "Advanced", 25, "advanced",
  "The Single Audit is the annual reckoning for organizations "
  "spending $750,000 or more in federal awards: one "
  "organization-wide audit replacing program-by-program chaos. "
  "Born in the Single Audit Act of 1984 and governed by 2 CFR "
  "Part 200 Subpart F, it tests financial statements, internal "
  "controls, and compliance with the requirements of each major "
  "program. Auditors follow the OMB Compliance Supplement's "
  "playbook. Findings — questioned costs, control weaknesses — "
  "go public in the Federal Audit Clearinghouse. For grantees, "
  "the Single Audit is the exam that never ends; for agencies, "
  "it is the primary window into grantee compliance.",
  "Independent auditors plan around the auditee's federal "
  "expenditures (the SEFA schedule), identify major programs by "
  "risk, and test compliance with the Supplement's fourteen "
  "requirement types. Findings are written with criteria, "
  "condition, cause, and effect. Auditees respond with "
  "corrective action plans. Reports file to the Clearinghouse "
  "within nine months of year-end. Federal agencies issue "
  "management decisions on findings and track resolution. "
  "Repeat findings escalate consequences.",
  ["Annual audit for $750k+ in federal expenditures.",
   "Tests financials, controls, and major-program compliance.",
   "Findings public in the Federal Audit Clearinghouse.",
   "The primary window into grantee compliance."],
  ["SEFA must completely and accurately report expenditures.",
   "Corrective action plans required for findings.",
   "Filing due within nine months of year-end."],
  ["Single Audit Act; 2 CFR Part 200 Subpart F.",
   "OMB Compliance Supplement."],
  ["Office of Management and Budget - Compliance Supplement.",
   "AICPA Single Audit guidance."],
  "In the Signature funding system the Single Audit is a sworn "
  "reckoning: every tested transaction a covenant examined, "
  "every finding an honest wound named, every corrective plan "
  "a promise of repair.",
  {"award": 3000000, "months": 12, "match_pct": 0}),

E("Federal Financial Reporting (SF-425)", "Advanced", 26, "advanced",
  "The SF-425 Federal Financial Report is the standard form on "
  "which grantees tell agencies what happened to the money: "
  "federal cash receipts, disbursements, unobligated balances, "
  "and recipient share, reported cumulatively. Filed quarterly, "
  "semiannually, or annually depending on the award — and finally "
  "at closeout — it reconciles the grantee's books to the "
  "agency's payment records. Discrepancies freeze funds. The "
  "form looks simple; the reconciliation behind it — tying PMS "
  "draws to the general ledger to the award — is where grants "
  "accounting proves itself.",
  "Finance staff compile cumulative receipts, disbursements, and "
  "balances from the grant accounting system, reconcile to "
  "payment-system records, and certify the report. Indirect costs "
  "claimed must match the rate agreement. Program income is "
  "reported. Certifying officials attest to accuracy under "
  "penalty. Agencies compare reports to draw patterns and flag "
  "anomalies. Late or inaccurate reports trigger holds and "
  "findings.",
  ["Standard form reporting federal cash activity.",
   "Cumulative: receipts, disbursements, balances, recipient share.",
   "Reconciles books to payment records.",
   "Discrepancies freeze funds."],
  ["Reports must be filed on schedule and certified.",
   "Figures must reconcile to the general ledger and PMS.",
   "Final reports due at closeout."],
  ["2 CFR 200.344 (closeout reporting).",
   "Agency financial reporting terms."],
  ["HHS PMS reporting guidance (model).",
   "2 CFR 200.344."],
  "In the Signature funding system the SF-425 is a sworn "
  "accounting: every cumulative figure a covenant of "
  "exactness, every reconciliation a promise that the books "
  "and the bank agree.",
  {"award": 1200000, "months": 36, "match_pct": 20}),

E("Performance Reporting", "Advanced", 27, "advanced",
  "Performance reporting answers the question money alone cannot: "
  "what did the grant achieve. Grantees report progress against "
  "the approved objectives — outputs delivered, outcomes measured, "
  "milestones met — on the agency's schedule, often with the "
  "financial reports. Good reports compare actuals to targets, "
  "explain variances, and document results with data. Agencies "
  "roll performance data into program evaluations and "
  "congressional justifications. The Government Performance and "
  "Results Act made this reporting a statutory duty: federal "
  "programs must show what the money bought.",
  "Program staff track measures defined in the application — "
  "clients served, trainings held, pollutant reduced — in "
  "performance systems. Reports compare actuals to targets, "
  "narrate variances, and attach evidence. Evaluators may "
  "validate with site visits or data audits. Agencies aggregate "
  "across grantees for program-level reporting. Poor performance "
  "triggers technical assistance or, at the extreme, funding "
  "consequences.",
  ["Report achievements against approved objectives.",
   "Compare actuals to targets; explain variances.",
   "Feed program evaluations and congressional justifications.",
   "A statutory duty under GPRA."],
  ["Measures must be defined and tracked consistently.",
   "Reports must be honest about shortfalls.",
   "Evidence must support claimed results."],
  ["Government Performance and Results Act.",
   "2 CFR 200.329 (monitoring and reporting)."],
  ["2 CFR 200.329.",
   "Agency performance reporting guides."],
  "In the Signature funding system performance reporting is a "
  "sworn accounting of results: every measured outcome a "
  "covenant of truth, every explained variance an honest "
  "reckoning, every achieved target a promise kept.",
  {"award": 900000, "months": 36, "match_pct": 0}),

E("Grant Closeout Procedures", "Advanced", 28, "advanced",
  "Closeout is the grant's dignified ending: the orderly "
  "settlement of every dollar and deliverable within 120 days "
  "of the period's end. The grantee submits final financial, "
  "performance, and invention reports; reconciles draws to "
  "expenditures; returns unspent cash; and certifies completion. "
  "The agency reviews, adjusts for disallowances, and issues "
  "the final determination. Property bought with grant funds is "
  "dispositioned. Then the file closes — though records must be "
  "kept for years, because audits can reopen the story.",
  "Grantees run closeout checklists: final SF-425, final "
  "performance report, patent and invention disclosures, "
  "equipment inventories. Finance reconciles and refunds "
  "balances. Agencies verify reports, resolve findings, and "
  "deobligate remaining funds. Closeout amendments correct the "
  "record. The grants officer issues closeout confirmation. "
  "Records retention clocks start at the final report.",
  ["Orderly settlement within 120 days of period end.",
   "Final financial, performance, invention reports.",
   "Reconcile draws; return unspent cash.",
   "Records kept for years after closing."],
  ["All final reports must be submitted.",
   "Unspent funds must be returned.",
   "Property must be dispositioned per rules."],
  ["2 CFR 200.344 (closeout).",
   "Agency closeout procedures."],
  ["2 CFR 200.344.",
   "Agency grants closeout guides."],
  "In the Signature funding system closeout is a sworn "
  "farewell: every final report a covenant of completeness, "
  "every returned dollar an honest remainder, every closed "
  "file a promise concluded with honor.",
  {"award": 750000, "months": 36, "match_pct": 10}),

E("Grant Fraud Prevention", "Advanced", 29, "advanced",
  "Grant fraud — false claims, phantom employees, diverted funds, "
  "fabricated match — steals from the public and from honest "
  "grantees. Prevention rests on internal controls: segregation "
  "of duties, documented approvals, and whistleblower channels. "
  "The False Claims Act punishes knowing false claims with "
  "treble damages; agency Inspectors General investigate and "
  "prosecute. Red flags — lavish spending, missing documentation, "
  "resistance to audits — trigger reviews. Suspension and "
  "debarment bar offenders from future awards. Integrity is the "
  "cheapest control.",
  "Organizations adopt fraud policies, train staff on red flags, "
  "and maintain hotlines. Finance enforces segregation and "
  "approval thresholds. Program staff verify subrecipient "
  "spending. OIGs run audits and investigations, referring "
  "criminal cases to Justice. Agencies suspend payments on "
  "credible fraud evidence and debar convicted entities. "
  "Recoveries return money to programs.",
  ["False claims, phantom staff, diverted funds, fabricated match.",
   "Prevention: controls, segregation, whistleblower channels.",
   "False Claims Act: treble damages.",
   "OIGs investigate; debarment bars offenders."],
  ["Internal controls must address fraud risk.",
   "Suspected fraud must be reported.",
   "Debarment checks required before subawards."],
  ["False Claims Act (31 U.S.C. 3729).",
   "2 CFR Part 180 (debarment)."],
  ["Council of the Inspectors General on Integrity and Efficiency.",
   "2 CFR Part 180."],
  "In the Signature funding system fraud prevention is a sworn "
  "vigilance: every control a covenant against theft, every "
  "hotline a promise of safe reporting, every prosecution a vow "
  "that the public's money is defended.",
  {"award": 2000000, "months": 36, "match_pct": 0}),

E("Program Income", "Advanced", 30, "advanced",
  "Program income is money a grant earns while doing its work: "
  "fees for services, conference registrations, sales of "
  "products, license royalties. Part 200's default rule adds "
  "it to the project — more resources for the mission — though "
  "agencies may deduct it from the award or let grantees keep "
  "it with approval. Grantees must track, report, and use "
  "program income per the award's terms, and it generally "
  "inherits the federal cost rules. Unreported program income "
  "is a classic audit finding: the money the project made but "
  "forgot to mention.",
  "Grantees identify income-generating activities in the "
  "application or as they arise, track gross income and related "
  "costs, and report on financial reports. The NoA states the "
  "treatment: additive, deductive, or cost-sharing. Finance "
  "applies the same allowability rules to program-income-funded "
  "costs. At closeout, unspent program income is dispositioned "
  "per terms. Agencies monitor for underreporting.",
  ["Money the grant earns doing its work.",
   "Default: added to the project.",
   "Must be tracked, reported, used per terms.",
   "Unreported income is a classic finding."],
  ["Program income must be identified and reported.",
   "Use must follow the award's treatment method.",
   "Federal cost rules apply to its expenditure."],
  ["2 CFR 200.307 (program income).",
   "Award-specific program income terms."],
  ["2 CFR 200.307.",
   "Agency program income guidance."],
  "In the Signature funding system program income is a sworn "
  "harvest: every earned dollar a covenant reported, every "
  "proper use a promise that the project's fruits feed the "
  "mission.",
  {"award": 600000, "months": 36, "match_pct": 0}),

E("Equipment Disposition", "Advanced", 31, "advanced",
  "Equipment bought with grant funds — generally items costing "
  "$5,000 or more with a useful life over a year — belongs in "
  "spirit to the project: the grantee holds title but must use "
  "it for the award, maintain it, and disposition it properly "
  "when done. While needed for any federal project, it stays. "
  "When no longer needed, the grantee may keep it by "
  "compensating the agency for its share of fair market value, "
  "sell it and share proceeds, or transfer it as directed. "
  "Inventories every two years keep track. Lost, stolen, or "
  "worn-out equipment is documented and retired.",
  "Property managers tag and inventory equipment, recording "
  "federal participation percentages. Biennial physical "
  "inventories reconcile to records. When equipment is no "
  "longer needed, the grantee requests disposition "
  "instructions; the agency directs keep, sell, or transfer. "
  "Compensation or proceeds are calculated by federal share "
  "of current value. Disposition is documented and reported "
  "at closeout.",
  ["$5,000+ items with >1 year life: title with grantee, duties to project.",
   "Use for federal work while needed; maintain it.",
   "Disposition: keep with compensation, sell and share, or transfer.",
   "Biennial inventories required."],
  ["Equipment must be used for the award while needed.",
   "Inventories required at least every two years.",
   "Disposition needs agency instructions."],
  ["2 CFR 200.313 (equipment).",
   "Agency property management terms."],
  ["2 CFR 200.313.",
   "Agency property guides."],
  "In the Signature funding system equipment disposition is a "
  "sworn settling of tools: every inventory a covenant of "
  "accountability, every proper transfer a promise that the "
  "public's instruments serve on.",
  {"award": 1100000, "months": 48, "match_pct": 0}),

E("Record Retention for Grants", "Advanced", 32, "advanced",
  "Grant records must outlive the grant: Part 200 requires "
  "retention for three years from the final expenditure report, "
  "longer if audits, litigation, or claims are pending. That "
  "means financial records, supporting documents, statistical "
  "records, and all records pertinent to the award — in "
  "whatever format, electronic or paper, with integrity "
  "protected. Litigation holds freeze destruction. When the "
  "auditor arrives in year two asking for year one's "
  "timesheets, the retention policy is what saves the "
  "organization.",
  "Organizations adopt written retention schedules mapping "
  "grant records to the three-year rule and exceptions. "
  "Electronic systems preserve integrity and retrievability; "
  "access controls protect confidentiality. Litigation or audit "
  "notices trigger holds communicated to all custodians. "
  "Destruction follows the schedule with authorization. "
  "Subrecipients' records are the prime's responsibility to "
  "ensure available.",
  ["Keep records 3 years from the final expenditure report.",
   "Longer if audits, litigation, or claims pending.",
   "Financial, supporting, statistical — all pertinent records.",
   "Electronic integrity must be protected."],
  ["Written retention schedules required.",
   "Holds must freeze destruction when triggered.",
   "Records must be retrievable for auditors."],
  ["2 CFR 200.334-200.338.",
   "Organizational records policies."],
  ["2 CFR 200.334-200.338.",
   "AICPA records guidance."],
  "In the Signature funding system retention is a sworn "
  "memory: every preserved timesheet a covenant against "
  "forgetting, every honored hold a promise that the record "
  "will speak when asked.",
  {"award": 400000, "months": 24, "match_pct": 0}),

E("Debarment and Suspension Checks", "Advanced", 33, "advanced",
  "Debarment and suspension bar bad actors from federal awards: "
  "entities and individuals excluded for fraud, poor performance, "
  "or wrongdoing are listed in SAM.gov's exclusions, and grantees "
  "must check before hiring contractors or making subawards. "
  "Doing business with an excluded party can void the costs and "
  "trigger findings. Checks are quick — a SAM.gov search — and "
  "must be documented and repeated periodically through the "
  "relationship. The exclusions list is the government's memory "
  "of who broke trust.",
  "Grantees search SAM.gov exclusions for every covered "
  "transaction — contracts and subawards over thresholds — "
  "before commitment and periodically after. Results are saved "
  "to the file with dates. Certifications from vendors supplement "
  "but do not replace the check. If an exclusion appears, the "
  "transaction stops or needs agency exception. Auditors sample "
  "files for the checks.",
  ["Excluded parties barred from federal awards.",
   "Check SAM.gov exclusions before contracts and subawards.",
   "Document and repeat checks through the relationship.",
   "Costs with excluded parties can be disallowed."],
  ["Checks required for covered transactions.",
   "Results must be documented with dates.",
   "Excluded parties must not be used without exception."],
  ["2 CFR Part 180; 2 CFR Part 200.319(b).",
   "Agency debarment regulations."],
  ["2 CFR Part 180.",
   "SAM.gov exclusions guidance."],
  "In the Signature funding system debarment checks are a sworn "
  "vetting: every search a covenant of clean partnership, every "
  "documented result a promise that trust, once broken, is not "
  "forgotten.",
  {"award": 700000, "months": 36, "match_pct": 0}),

E("Cost Principles: Direct vs Indirect", "Advanced", 34, "advanced",
  "Direct costs can be pinned to the grant — the project "
  "scientist's salary, the lab supplies, the project travel. "
  "Indirect costs cannot — the accounting department, the "
  "building's utilities, the HR office that hired the scientist. "
  "Part 200 demands consistent treatment: a cost treated as "
  "direct on one award cannot be indirect on another. The "
  "distinction decides budgets, NICRAs, and audit findings. "
  "Common tripwires: administrative salaries charged direct "
  "without justification, or the same cost claimed both ways. "
  "The cost policy statement is where organizations swear their "
  "consistency.",
  "Organizations write cost policies defining direct and "
  "indirect treatment for each cost type, applied uniformly "
  "across all funding. Budget builders classify each line; "
  "finance reviews for consistency. Direct charging of "
  "administrative costs needs the 'unlike circumstances' "
  "justification of 2 CFR 200.413. Auditors test consistency "
  "across awards. Inconsistent treatment draws findings and "
  "repayments.",
  ["Direct: pinnable to the grant. Indirect: shared overhead.",
   "Treatment must be consistent across all awards.",
   "Decides budgets, NICRAs, and findings.",
   "Admin salaries charged direct need justification."],
  ["Cost policies must define treatment consistently.",
   "Unlike-circumstances justification needed for direct admin charges.",
   "No double-counting between direct and indirect."],
  ["2 CFR 200.413 (direct costs); 200.414 (indirect).",
   "Organizational cost policy statements."],
  ["2 CFR 200.413-200.414.",
   "HHS cost allocation guidance."],
  "In the Signature funding system the direct-indirect line is "
  "a sworn boundary: every classified cost a covenant of "
  "consistency, every policy a promise that like costs are "
  "treated alike.",
  {"award": 1300000, "months": 48, "match_pct": 0}),
]
