#!/usr/bin/env python3
"""Entries for the Insurance Claims and Benefits database pair (5,000-target program).

Dedupe gate: all 68 titles checked against the WHOLE system with
code/dedupe_gate.py BEFORE writing. ID prefixes JAH-INCB- (public) and
JAH-INCBS- (signature) verified free: zero hits in manifest id_prefix values
(exact + substring) and zero hits in shard record IDs.

34 records per edition, ladder-ordered 1-34 (Foundations 1-12 / Compounded
13-23 / Advanced 24-34).
"""


def R(t, tier, rank, desc, how, kp, req, std, cit, dk, data):
    return {'t': t, 'tier': tier, 'rank': rank, 'desc': desc, 'how': how,
            'kp': kp, 'req': req, 'std': std, 'cit': cit, 'dk': dk, 'data': data}


PUB = [
R("What Insurance Is — Industry Overview", "Foundations", 1,
  "Insurance is the business of shared risk: many pay premiums into a pool, and the pool pays the losses of the few who suffer them. "
  "It lets families rebuild after fires, drivers repair after crashes, and businesses survive disasters that would otherwise ruin them. "
  "The industry spans carriers who bear risk, agents who sell, adjusters who settle claims, and reinsurers who insure the insurers.",
  "Policyholders pay premiums; the carrier invests the float and pays covered claims from the pool. "
  "Underwriters price risk by predicting losses; actuaries model them mathematically. "
  "The carrier profits when premiums plus investment income exceed claims and expenses - measured by the combined ratio.",
  ["Many pay premiums; the pool pays the few who suffer loss.",
   "Insurance makes recovery possible after catastrophe.",
   "Underwriters price risk; actuaries model it; adjusters settle it.",
   "Profit when premiums and investments exceed claims and expenses."],
  ["An insurance license for the lines written.",
   "Capital reserves meeting solvency requirements.",
   "Actuarial, underwriting, and claims capability."],
  ["Policies written plainly with covered and excluded perils stated.",
   "Claims paid promptly and fairly per the contract.",
   "Solvency monitored by regulators."],
  ["NAIC model laws and state insurance regulations (public regulations).",
   "Insurance industry financial reporting standards (public standards)."],
  "lossratio", {"losses": 62000000.0, "earned_prem": 95000000.0}),

R("The Insurance Policy — Parts and Terms", "Foundations", 2,
  "The insurance policy is the contract: the carrier's written promise to pay for covered losses in exchange for the premium. "
  "Its parts are the declarations (who, what, how much), the insuring agreement (what is covered), exclusions (what is not), conditions (duties of both sides), and endorsements (custom changes). "
  "Reading the policy before loss is the cheapest insurance education there is.",
  "The declarations name the insured, the property or liability covered, the limits, and the premium. "
  "The insuring agreement grants coverage; exclusions carve it back; conditions set duties like timely notice and cooperation. "
  "Endorsements tailor the contract - adding a driver, raising a limit, covering a new peril.",
  ["Declarations, insuring agreement, exclusions, conditions, endorsements.",
   "Limits cap what the carrier pays; deductibles are the insured's share.",
   "Exclusions carve back the granted coverage.",
   "Endorsements tailor the standard contract."],
  ["A policy issued for every coverage sold.",
   "Plain-language summaries alongside the legal text.",
   "Endorsements documented and priced."],
  ["Coverage terms delivered before or with the policy.",
   "Exclusions conspicuous, not buried.",
   "Changes endorsed in writing, never verbal-only."],
  ["NAIC policy-form readability standards (public standards).",
   "State insurance contract regulations (public regulations)."],
  "premium", {"rate": 1.85, "exposure": 240.0}),

R("Premiums — How Prices Are Set", "Foundations", 3,
  "Premiums are the price of the risk transfer, set so the pool collects enough to pay losses, cover expenses, and earn a return. "
  "Underwriters classify each risk - driver record, building construction, health history - and apply rates filed with regulators. "
  "Fair pricing charges each class its expected cost; unfair pricing is discrimination the law forbids.",
  "Actuaries analyze loss history by class to set base rates; underwriters adjust for individual risk factors within filed guidelines. "
  "Expenses and profit load are added; discounts reward lower risk - safe drivers, sprinklered buildings. "
  "Regulators review rates for adequacy, fairness, and non-discrimination before they are used.",
  ["Premium = expected losses + expenses + profit, by risk class.",
   "Classification groups similar risks for fair pricing.",
   "Discounts reward lower risk.",
   "Regulators review rates for adequacy and fairness."],
  ["Loss history credible enough to price by class.",
   "Filed rates approved before use.",
   "Underwriting guidelines applied consistently."],
  ["No unfair discrimination in rates.",
   "Rate filings supported by actuarial data.",
   "Discounts actually earned, not given away."],
  ["Actuarial Standards of Practice on ratemaking (public standards).",
   "State rate-filing regulations (public regulations)."],
  "premium", {"rate": 0.92, "exposure": 1500.0}),

R("First Notice of Loss (FNOL)", "Foundations", 4,
  "First notice of loss is the insured's call that starts everything: the moment the carrier learns of the loss and the claim is born. "
  "Fast, complete FNOL shortens the whole claim - the adjuster assigned today investigates fresher evidence than the one assigned next week. "
  "Modern FNOL arrives by phone, app, web, and agent, around the clock.",
  "The intake captures who, what, when, where, and how - plus policy verification and coverage triage. "
  "The claim is set up in the system, reserves are posted, and the right adjuster is assigned by line, severity, and jurisdiction. "
  "The insured gets a claim number, a contact name, and next steps - uncertainty is the enemy at FNOL.",
  ["FNOL is the claim's birth: fast and complete beats slow and thin.",
   "Who, what, when, where, how - plus policy and coverage triage.",
   "Reserves posted and the right adjuster assigned at setup.",
   "The insured leaves FNOL with a number, a name, and next steps."],
  ["24/7 intake: phone, app, web, agent.",
   "A claims system that sets up and routes instantly.",
   "Coverage triage at intake, not weeks later."],
  ["Claims acknowledged within mandated timeframes.",
   "No discouragement of valid claims at intake.",
   "Catastrophe plans surge intake capacity."],
  ["NAIC claims-handling model regulations (public regulations).",
   "State prompt-notice and acknowledgment rules (public regulations)."],
  "reserve", {"paid": 0.0, "case_reserve": 25000.0}),

R("The Claims Adjuster", "Foundations", 5,
  "The claims adjuster investigates the loss, determines what the policy covers, and settles the claim fairly. "
  "Adjusters are the carrier's promise made personal - the human who shows up after the fire or the crash. "
  "Good adjusting is equal parts detective, accountant, and diplomat.",
  "The adjuster inspects the damage, interviews the parties, gathers police and repair records, and reads the policy against the facts. "
  "Coverage is confirmed or denied in writing with reasons; the loss is valued - repair estimates, actual cash value, or replacement cost. "
  "Settlement is negotiated and paid; disputes go to appraisal, mediation, or suit.",
  ["Investigate, determine coverage, value the loss, settle fairly.",
   "The adjuster's work is the carrier's promise made personal.",
   "Coverage decisions in writing with reasons.",
   "Disputes have paths: appraisal, mediation, suit."],
  ["Licensed adjusters for the jurisdiction and line.",
   "Investigation resources: inspectors, experts, records access.",
   "Authority levels matching claim severity."],
  ["Settle promptly and fairly - no lowballing.",
   "Denials explained in writing with policy language.",
   "Files documented for regulatory review."],
  ["State adjuster licensing laws (public regulations).",
   "NAIC unfair claims settlement practices model (public model law)."],
  "lossratio", {"losses": 18500000.0, "earned_prem": 28000000.0}),

R("Auto Insurance Claims", "Foundations", 6,
  "Auto claims are the industry's highest volume: fender-benders to total losses, settled by the millions each year. "
  "Coverage splits into liability (harm to others), collision (your car), comprehensive (theft, weather, animals), and injury protections. "
  "Speed and fairness decide reputation - the claimant remembers this claim when renewal comes.",
  "After FNOL, the adjuster takes statements, orders the police report, and inspects the vehicle - by app photo or in person. "
  "Liability is determined by the facts and the law of the jurisdiction; damages are estimated by shops or valuation systems. "
  "Repairs are authorized or the total-loss value is paid; injuries are handled under the medical and liability coverages.",
  ["Liability, collision, comprehensive, injury: the coverage split.",
   "Liability follows the facts and the jurisdiction's law.",
   "Repairs authorized or total-loss value paid.",
   "Speed plus fairness wins the renewal."],
  ["FNOL with vehicle and injury triage.",
   "Shop networks or valuation systems for estimates.",
   "Injury adjusters for bodily-injury claims."],
  ["Total-loss values based on actual market data.",
   "Repairs to pre-loss condition with quality parts.",
   "Injury claims handled without bad-faith delay."],
  ["State auto insurance and claims regulations (public regulations).",
   "NAIC auto claims handling guidance (public guidance)."],
  "lossratio", {"losses": 41000000.0, "earned_prem": 58000000.0}),

R("Property Insurance Claims", "Foundations", 7,
  "Property claims pay for damaged buildings and belongings: fires, storms, burst pipes, theft. "
  "The adjuster's job is to measure the damage, separate covered perils from excluded ones, and get the family or business rebuilding. "
  "Catastrophe claims - hurricanes, wildfires - arrive by the thousand and test the whole operation.",
  "The adjuster inspects, documents with photos and measurements, and scopes repairs with contractors. "
  "Coverage is applied peril by peril - wind versus flood matters enormously - and payment follows the valuation method: replacement cost or actual cash value. "
  "Additional living expenses keep displaced families housed while repairs proceed.",
  ["Covered perils paid; excluded perils separated honestly.",
   "Scope the damage, value by the policy's method.",
   "Replacement cost vs. actual cash value changes the check.",
   "Catastrophes arrive by the thousand - surge capacity matters."],
  ["Field adjusters and contractor networks.",
   "Scoping and estimating systems.",
   "Catastrophe response plans with surge staffing."],
  ["Wind vs. flood and other peril splits applied per the policy.",
   "Depreciation schedules fair and documented.",
   "Living expenses paid while repairs proceed."],
  ["State property claims regulations (public regulations).",
   "Flood insurance (NFIP) rules where applicable (public regulations)."],
  "reserve", {"paid": 45000.0, "case_reserve": 120000.0}),

R("What Public Benefits Are — Overview", "Foundations", 8,
  "Public benefits are government programs that support people in need: food assistance, health coverage, cash aid, unemployment insurance, disability, and retirement. "
  "They are the social safety net - funded by taxpayers, administered by agencies, and governed by eligibility rules set in law. "
  "Unlike insurance, benefits are rights when eligible, not contracts purchased.",
  "Legislatures create programs and set eligibility; agencies write the rules, take applications, determine eligibility, and deliver benefits. "
  "Funding is federal, state, or shared; delivery runs through EBT cards, direct deposit, and provider payments. "
  "Appeals protect applicants from wrong denials - the right to be heard is built into every program.",
  ["The safety net: food, health, cash, unemployment, disability, retirement.",
   "Eligibility set in law; benefits a right when eligible.",
   "Funded by taxpayers, run by agencies.",
   "Appeals protect against wrong denials."],
  ["Statutes and regulations defining each program.",
   "An administering agency with staff and systems.",
   "Funding appropriated and accounted."],
  ["Eligibility decided by the written rules, evenly applied.",
   "Decisions in writing with appeal rights stated.",
   "Benefits delivered timely once determined."],
  ["Program statutes and federal regulations (public law).",
   "Agency policy manuals (public documents)."],
  "eligibility", {"income": 2850.0, "limit": 3200.0}),

R("Benefit Applications", "Foundations", 9,
  "The benefit application is how need becomes a case: the form - paper, online, or in-person - where the applicant states household, income, and need. "
  "A good application process is accessible to the people it serves: plain language, multiple channels, and help for those who struggle with forms. "
  "Barriers at application are denials by design, and the law forbids them.",
  "Applicants file with identity, residence, household, income, and expense information; the agency screens for completeness and requests verification. "
  "Interviews - phone or in-person - clarify the facts; the application date protects retroactive benefits. "
  "Assistance is offered: navigators, language access, and accommodations for disability.",
  ["Plain language, multiple channels, help for the struggling.",
   "Barriers at application are denials by design.",
   "The application date protects retroactive benefits.",
   "Verification requested, not assumed missing."],
  ["Accessible applications: online, paper, in-person, phone.",
   "Language access and disability accommodations.",
   "Trained intake staff and navigators."],
  ["Applications accepted without discrimination.",
   "Filing date honored for retroactive benefits.",
   "Help offered, not just forms handed over."],
  ["Federal application-accessibility rules (public regulations).",
   "Program-specific application regulations (public regulations)."],
  "eligibility", {"income": 1950.0, "limit": 2400.0}),

R("Eligibility Determination", "Foundations", 10,
  "Eligibility determination is the decision: does this applicant meet the program's rules for income, assets, household, and category. "
  "It must be accurate - wrong denials harm the needy, wrong approvals waste public funds - and timely, because need doesn't wait. "
  "Every determination is documented and appealable.",
  "The worker verifies income, assets, household composition, and categorical requirements against data sources and documents. "
  "The rules engine or manual calculation applies income limits, deductions, and asset tests; the decision issues in writing with reasons. "
  "Redeterminations recur on schedule - circumstances change, and eligibility must follow.",
  ["Accurate and timely: wrong either way harms.",
   "Verified against data and documents, not assumed.",
   "Decisions in writing with reasons.",
   "Redeterminations follow changing circumstances."],
  ["Eligibility workers trained on the program rules.",
   "Data sources: wage, asset, and household verification.",
   "A rules engine or calculation system."],
  ["Decisions within mandated timeframes.",
   "Notices plain-language with appeal rights.",
   "No eligible person denied by worker error."],
  ["Program eligibility regulations (public regulations).",
   "Due-process requirements for benefit decisions (public law)."],
  "eligibility", {"income": 3100.0, "limit": 2950.0}),

R("Case Workers and Service Delivery", "Foundations", 11,
  "Case workers are the human face of benefits: interviewing applicants, determining eligibility, and connecting families to services. "
  "Caseloads decide quality - the worker with 400 cases cannot know any of them. "
  "Service delivery is the whole chain from application to benefit in hand, and the worker is its most important link.",
  "Workers manage caseloads through interviews, verification, data entry, and ongoing case maintenance. "
  "Supervisors review samples for accuracy; training keeps workers current on rule changes. "
  "Service standards set timeframes for each step, measured and reported.",
  ["The worker is the most important link in delivery.",
   "Caseloads decide quality.",
   "Interviews, verification, maintenance: the worker's cycle.",
   "Supervision and training protect accuracy."],
  ["Enough workers for manageable caseloads.",
   "Training on rules and systems, ongoing.",
   "Supervisory review of decisions."],
  ["Caseload standards protecting quality.",
   "Decisions reviewed for accuracy and bias.",
   "Worker safety in field work."],
  ["Program administration standards (public regulations).",
   "Public-sector workforce guidance (public guidance)."],
  "caseload", {"workers": 45, "cases": 6750}),

R("Insurance Math I — Loss Ratios and Premiums", "Foundations", 12,
  "Insurance math begins with the loss ratio: losses divided by earned premium, the percentage of each premium dollar paid in claims. "
  "A 65% loss ratio means 65 cents of each dollar went to losses; add the expense ratio and you get the combined ratio. "
  "Under 100% combined means underwriting profit; over means loss.",
  "Earned premium is the portion of written premium covering elapsed time; losses include paid plus reserved. "
  "The expense ratio adds commissions, salaries, and overhead over earned premium. "
  "Investment income can rescue a combined ratio slightly over 100 - the float earns while claims develop.",
  ["Loss ratio = losses / earned premium.",
   "Combined ratio = loss ratio + expense ratio.",
   "Under 100% combined: underwriting profit.",
   "Investment income can offset a small underwriting loss."],
  ["Earned premium and incurred losses by line.",
   "Expense allocation that is honest, not creative.",
   "Reserves set by actuarial method."],
  ["Ratios computed consistently period to period.",
   "Reserves adequate - the loss ratio is only as true as the reserves.",
   "Reported per statutory accounting rules."],
  ["Statutory accounting principles (public standards).",
   "Actuarial Standards of Practice (public standards)."],
  "lossratio", {"losses": 65000000.0, "earned_prem": 100000000.0}),
]

PUB += [
R("Claims Investigation", "Compounded", 13,
  "Claims investigation finds the facts: what happened, what the policy covers, and what the loss is worth. "
  "Most claims are straightforward; investigation deepens with size, complexity, and red flags. "
  "The investigator's duty is to the truth, not to the outcome - facts first, then coverage.",
  "Adjusters and investigators take recorded statements, inspect scenes and damage, and collect records: police, medical, repair, financial. "
  "Experts are engaged for cause and origin, engineering, or medical questions; examinations under oath compel testimony when needed. "
  "Findings are documented in the file - the investigation must be reconstructable years later.",
  ["Facts first, then coverage: duty to the truth.",
   "Depth follows size, complexity, and red flags.",
   "Statements, inspections, records, experts.",
   "Files documented to be reconstructable years later."],
  ["Licensed investigators and adjusters.",
   "Access to records and expert disciplines.",
   "Examination-under-oath authority in the policy."],
  ["Investigations reasonable, not harassing.",
   "Surveillance only where justified and lawful.",
   "Findings kept; files audit-ready."],
  ["State claims investigation regulations (public regulations).",
   "NAIC unfair practices model provisions (public model law)."],
  "reserve", {"paid": 12000.0, "case_reserve": 88000.0}),

R("Setting Claim Reserves", "Compounded", 14,
  "Reserves are the carrier's honest estimate of what open claims will ultimately cost - the balance sheet's largest liability. "
  "Each open claim carries a case reserve; actuaries add bulk reserves for incurred-but-not-reported losses. "
  "Under-reserving flatters today and bankrupts tomorrow.",
  "Adjusters set case reserves from the facts: damages known, exposure estimated, jurisdiction considered. "
  "Reserves are reviewed as claims develop - raised when surgery is scheduled, lowered when the claimant recovers. "
  "Actuaries test the aggregate with triangles and development factors; auditors and regulators review.",
  ["Case reserves per claim; bulk reserves for IBNR.",
   "Reserves the balance sheet's largest liability.",
   "Reviewed as claims develop - up and down.",
   "Under-reserving flatters today, bankrupts tomorrow."],
  ["Adjusters trained in reserving discipline.",
   "Actuarial review of the aggregate.",
   "Claims data credible by line and year."],
  ["Reserves adequate and documented.",
   "No manipulation to smooth earnings.",
   "Regulatory and audit review."],
  ["Actuarial Standards of Practice on reserving (public standards).",
   "Statutory accounting reserve rules (public standards)."],
  "reserve", {"paid": 250000.0, "case_reserve": 1750000.0}),

R("Settlement Negotiation", "Compounded", 15,
  "Settlement negotiation resolves the claim without trial: the adjuster and the claimant (or attorney) bargaining toward the claim's fair value. "
  "Most claims settle - trials are expensive for everyone. "
  "Fair settlement values the loss honestly; lowballing buys litigation.",
  "The adjuster evaluates liability and damages, sets authority within granted limits, and makes offers anchored in the file's evidence. "
  "Negotiation proceeds through demands and counters; mediation breaks deadlocks. "
  "Releases are drafted to truly release; payment follows promptly.",
  ["Most claims settle; trials are expensive for everyone.",
   "Fair value honestly evaluated, authority respected.",
   "Offers anchored in the file's evidence.",
   "Releases drafted to truly release."],
  ["Adjusters with negotiation training and authority.",
   "Evaluation tools: verdict data, damage models.",
   "Mediation access for deadlocks."],
  ["Settlements fair - no exploitation of unrepresented claimants.",
   "Authority limits honored.",
   "Payments prompt after agreement."],
  ["State settlement-practice regulations (public regulations).",
   "Ethics standards for claims professionals (public standards)."],
  "combined", {"loss_ratio": 0.68, "expense_ratio": 0.29}),

R("Subrogation and Recovery Operations", "Compounded", 16,
  "Subrogation is the carrier's recovery right: after paying its insured, the carrier steps into the insured's shoes against the at-fault party. "
  "The driver hit by a red-light runner gets paid by his carrier, and his carrier collects from the runner's carrier. "
  "Good subrogation returns billions to the pool and holds the at-fault accountable.",
  "The carrier identifies recovery potential at FNOL - liable third parties, their insurers, product defects. "
  "Demands go to the responsible party; arbitration between carriers resolves disputes; litigation follows when needed. "
  "Recoveries are credited against the loss, and the insured's deductible is refunded from recoveries first in many jurisdictions.",
  ["Pay the insured, then pursue the at-fault.",
   "Recovery potential identified at FNOL.",
   "Arbitration between carriers; suit when needed.",
   "Deductibles refunded from recoveries first, where required."],
  ["Subrogation staff or vendors by line.",
   "Inter-company arbitration membership.",
   "Lien and recovery tracking systems."],
  ["Insureds made whole before the carrier profits.",
   "Deductible refunds per jurisdiction rules.",
   "Statutes of limitation watched."],
  ["State subrogation and made-whole rules (public regulations).",
   "Inter-company arbitration agreements (public agreements)."],
  "subro", {"paid": 42000.0, "recovered": 31500.0}),

R("Fraud Detection — SIU", "Compounded", 17,
  "Insurance fraud steals from every policyholder: staged crashes, inflated repairs, phantom injuries, arson for profit. "
  "The Special Investigations Unit hunts it - investigators trained in fraud indicators, working with law enforcement and industry databases. "
  "Detection must be precise: the honest claimant wrongly accused is a second victim.",
  "Claims are scored for fraud indicators at intake and during handling; SIU investigates the flagged - statements, surveillance where justified, records analysis. "
  "Industry databases share fraud intelligence across carriers; NICB coordinates with law enforcement. "
  "Proven fraud is denied and referred for prosecution; the file must support every step.",
  ["Fraud steals from every policyholder.",
   "SIU: indicators, investigation, referral.",
   "Scored at intake; investigated when flagged.",
   "The wrongly accused honest claimant is a second victim."],
  ["An SIU with trained investigators.",
   "Fraud-indicator scoring in the claims system.",
   "Industry database participation and law-enforcement liaison."],
  ["Investigations lawful and proportionate.",
   "Denials supported by the file.",
   "Referrals to prosecutors where warranted."],
  ["State insurance fraud statutes (public law).",
   "NAIC fraud-prevention model provisions (public model law)."],
  "fraudrate", {"claims": 50000, "flagged": 1250}),

R("Liability Claims", "Compounded", 18,
  "Liability claims allege the insured harmed someone: the slip in the store, the dog bite, the professional's error. "
  "The carrier owes two duties: defend the insured and pay covered damages. "
  "Liability turns on negligence - duty, breach, causation, damages - argued claim by claim.",
  "The adjuster investigates the incident, the injuries, and the insured's fault under the jurisdiction's negligence law. "
  "Coverage is confirmed - the policy's liability grants and exclusions applied. "
  "Defense counsel is assigned when suit comes; settlement weighs verdict risk against the offer.",
  ["Defend the insured; pay covered damages.",
   "Negligence: duty, breach, causation, damages.",
   "Coverage applied grant by grant, exclusion by exclusion.",
   "Settlement weighs verdict risk."],
  ["Liability adjusters versed in negligence law.",
   "Defense counsel panels by jurisdiction.",
   "Verdict and settlement data for evaluation."],
  ["Defense provided when the duty triggers.",
   "Settlements within policy limits pursued in good faith.",
   "No bad-faith exposure of the insured."],
  ["State liability and tort law (public law).",
   "Bad-faith doctrines by jurisdiction (public law)."],
  "lossratio", {"losses": 33000000.0, "earned_prem": 47000000.0}),

R("Workers' Compensation Claims", "Compounded", 19,
  "Workers' compensation is the grand bargain: injured workers get medical care and wage benefits without proving fault, and employers get immunity from most lawsuits. "
  "Every state mandates it; the claim starts with the injury report and the employer's notice to the carrier. "
  "Return to work - healed and accommodated - is the system's true measure.",
  "The adjuster verifies employment and that the injury arose from the job, authorizes medical care, and pays wage-loss benefits per the statutory formula. "
  "Nurse case managers coordinate treatment; disputes go to the workers' comp board. "
  "Permanent impairment is rated by the jurisdiction's schedule when healing plateaus.",
  ["The grand bargain: benefits without fault, immunity from suit.",
   "Medical care authorized; wage benefits per statute.",
   "Return to work is the true measure.",
   "Disputes to the comp board."],
  ["Comp adjusters expert in the state's statute.",
   "Medical networks and nurse case management.",
   "Return-to-work coordination with employers."],
  ["Benefits paid per the statutory formula, timely.",
   "Medical care not unreasonably denied.",
   "Retaliation for filing forbidden."],
  ["State workers' compensation statutes (public law).",
   "Federal employer reporting rules (public regulations)."],
  "combined", {"loss_ratio": 0.72, "expense_ratio": 0.26}),

R("Health Claims Adjudication", "Compounded", 20,
  "Health claims adjudication decides what the plan pays for each medical service: the bill arrives, the system checks eligibility, coverage, and medical necessity, and the payment goes out. "
  "Millions of claims a day flow through auto-adjudication; the exceptions get human eyes. "
  "Accuracy here is measured in both dollars and denied care.",
  "Claims arrive electronically with diagnosis and procedure codes; edits check eligibility, coding validity, and coverage rules. "
  "Contracted rates price the service; the member owes deductible, copay, or coinsurance per the plan. "
  "Denials issue with reasons and appeal rights; medical-necessity disputes get clinical review.",
  ["Eligibility, coverage, medical necessity: the three checks.",
   "Auto-adjudication for the routine; humans for the exceptions.",
   "Contracted rates price the service.",
   "Denials with reasons and appeal rights."],
  ["Electronic claims intake with coding edits.",
   "Provider contracts with fee schedules.",
   "Clinical review for medical-necessity disputes."],
  ["Clean claims paid within mandated timeframes.",
   "Denials explained with appeal rights.",
   "Mental-health parity honored."],
  ["Federal claims-procedure rules (public regulations).",
   "State prompt-pay laws (public regulations)."],
  "adjudication", {"billed": 2400.0, "allowed": 1450.0}),

R("SNAP — Food Assistance Operations", "Compounded", 21,
  "SNAP (food assistance) puts groceries on the tables of low-income households: monthly benefits on EBT cards, spent at authorized retailers. "
  "It is the nation's largest nutrition program - tens of millions served, benefits scaled to household size and income. "
  "Operations are eligibility accuracy at scale plus retailer integrity.",
  "States take applications, determine eligibility under federal rules, and issue monthly allotments to EBT accounts. "
  "Households report changes; recertifications recur; quality-control samples measure payment accuracy. "
  "Retailers are authorized and monitored - trafficking benefits for cash is fraud, prosecuted.",
  ["Monthly food benefits on EBT, scaled to household and income.",
   "Eligibility under federal rules, run by states.",
   "Payment accuracy measured by quality control.",
   "Retailer integrity policed."],
  ["State eligibility systems and trained workers.",
   "EBT issuance and retailer authorization.",
   "Quality-control sampling operations."],
  ["Applications processed within federal timeframes.",
   "Allotments accurate to the household's circumstances.",
   "Trafficking investigated and prosecuted."],
  ["Food and Nutrition Act and SNAP regulations (public law).",
   "Federal payment-accuracy rules (public regulations)."],
  "benefit", {"base": 281.0, "household": 3.0}),

R("Medicaid Operations", "Compounded", 22,
  "Medicaid is health coverage for low-income Americans: jointly funded by federal and state governments, run by states within federal rules. "
  "It covers children, pregnant women, the elderly, and people with disabilities - tens of millions. "
  "Operations are eligibility at scale plus managed-care oversight plus provider payment.",
  "States determine eligibility - increasingly through streamlined data-driven renewals - and enroll members in managed-care plans or fee-for-service. "
  "Plans are paid per-member rates; providers bill for services; states oversee quality and access. "
  "Eligibility redeterminations keep the rolls accurate as circumstances change.",
  ["Joint federal-state funding; states run within federal rules.",
   "Eligibility at scale; managed-care oversight; provider payment.",
   "Covers children, pregnant women, elderly, disabled.",
   "Redeterminations keep rolls accurate."],
  ["Eligibility systems with data-driven renewals.",
   "Managed-care contracts and rate-setting.",
   "Provider networks meeting access standards."],
  ["Eligible people enrolled; renewals not wrongly terminated.",
   "Access standards met: providers available.",
   "Rates actuarially sound."],
  ["Social Security Act Title XIX (public law).",
   "Federal Medicaid managed-care rules (public regulations)."],
  "benefit", {"base": 6200.0, "household": 1.0}),

R("Unemployment Insurance", "Compounded", 23,
  "Unemployment insurance replaces part of lost wages for workers laid off through no fault of their own - the economy's automatic stabilizer. "
  "Employers fund it through payroll taxes; states run the programs within federal framework law. "
  "Weekly claims certify the worker is able, available, and seeking work.",
  "Employers report wages quarterly; when layoffs come, workers file initial claims and the agency determines monetary eligibility. "
  "Weekly certifications confirm continued eligibility; benefits pay for a statutory duration, extended in recessions. "
  "Appeals resolve disputes over separations - quit versus fired matters.",
  ["Wage replacement for the laid-off, through no fault of their own.",
   "Employer-funded; state-run within federal framework.",
   "Weekly certifications: able, available, seeking.",
   "Extended in recessions."],
  ["Wage-record systems from employer reports.",
   "Initial-claims and weekly-certification processing.",
   "Appeals tribunals for separation disputes."],
  ["Claims decided within timeliness standards.",
   "Benefits paid for the statutory duration.",
   "Fraud - working while collecting - detected."],
  ["Federal Unemployment Tax Act and state UI laws (public law).",
   "Federal timeliness and payment-accuracy standards (public standards)."],
  "benefit", {"base": 420.0, "household": 1.0}),
]

PUB += [
R("Combined Ratio and Underwriting Profit", "Advanced", 24,
  "The combined ratio is the underwriter's bottom line: loss ratio plus expense ratio, the percentage of premium consumed by claims and costs. "
  "Below 100%, the carrier profits on underwriting; above, it loses - rescued or sunk by investment income. "
  "Every line of business lives or dies by this number.",
  "Losses incurred over earned premium gives the loss ratio; underwriting expenses over earned premium gives the expense ratio. "
  "Management watches the ratio by line, state, and year - cutting unprofitable classes, repricing, tightening underwriting. "
  "Analysts and rating agencies judge carriers on sustained combined ratios under 100.",
  ["Loss ratio + expense ratio = combined ratio.",
   "Under 100%: underwriting profit; over: loss.",
   "Watched by line, state, and year.",
   "Investment income can offset, not excuse, underwriting."],
  ["Credible loss and expense data by segment.",
   "Management willing to exit unprofitable classes.",
   "Actuarial support for repricing."],
  ["Ratios reported honestly per statutory accounting.",
   "Expense allocation consistent over time.",
   "Reserve adequacy behind every loss ratio."],
  ["Statutory accounting principles (public standards).",
   "Rating-agency underwriting metrics (public methodologies)."],
  "combined", {"loss_ratio": 0.63, "expense_ratio": 0.28}),

R("Reinsurance Treaties and Programs", "Advanced", 25,
  "Reinsurance is insurance for insurers: carriers cede part of their risk to reinsurers, protecting against catastrophes and smoothing results. "
  "Treaty reinsurance covers whole portfolios; facultative covers single large risks. "
  "Without reinsurance, one hurricane could sink a regional carrier.",
  "The carrier analyzes its peak exposures and buys layers: working layers for frequency, catastrophe layers for the big one. "
  "Reinsurers price on modeled loss and diversify globally - the Japanese typhoon offsets the Florida hurricane. "
  "Claims flow up: the carrier pays its insured, then collects from the reinsurer per the treaty.",
  ["Carriers cede risk; reinsurers diversify globally.",
   "Treaty for portfolios; facultative for single risks.",
   "Catastrophe layers protect against the big one.",
   "One hurricane must never sink the carrier."],
  ["Exposure modeling: probable maximum loss by peril.",
   "Reinsurance brokers and treaty drafting.",
   "Collateral for reinsurer credit risk."],
  ["Reinsurance contracts honored on the big losses.",
   "Credit risk of reinsurers monitored.",
   "Disclosures of reinsurance dependence."],
  ["NAIC reinsurance credit regulations (public regulations).",
   "Reinsurance contract law (public law)."],
  "combined", {"loss_ratio": 0.58, "expense_ratio": 0.24}),

R("Catastrophe Claims Operations", "Advanced", 26,
  "Catastrophe claims operations activate when disaster strikes: thousands of claims in days, and the carrier's promise tested at scale. "
  "Hurricanes, wildfires, hailstorms - the CAT plan turns the ordinary claims department into a surge machine. "
  "Speed here is compassion; accuracy is solvency.",
  "The CAT plan pre-assigns roles: aerial imagery orders, adjuster deployment, contractor networks, mobile claim centers. "
  "Drones and satellite imagery triage damage across whole neighborhoods; adjusters settle by the hundreds. "
  "Reinsurance notices go out; regulators get catastrophe data calls; fraud watches for the disaster-chasers.",
  ["Thousands of claims in days: the promise tested at scale.",
   "Pre-assigned roles: imagery, deployment, contractors, centers.",
   "Drones and satellites triage whole neighborhoods.",
   "Speed is compassion; accuracy is solvency."],
  ["A written, drilled catastrophe plan.",
   "Surge adjusters, contractors, and imagery contracts.",
   "Mobile claim centers and policyholder communications."],
  ["Claims handled in catastrophe-timeframe regulations.",
   "No taking advantage of disaster victims.",
   "Fraud detection active amid the surge."],
  ["State catastrophe claims regulations (public regulations).",
   "NAIC catastrophe data-call requirements (public requirements)."],
  "lossratio", {"losses": 890000000.0, "earned_prem": 1200000000.0}),

R("The Appeals Process", "Advanced", 27,
  "The appeals process is the applicant's second chance: when benefits are denied or cut, the appeal reheats the case before an impartial reviewer. "
  "Due process requires notice, reasons, and the opportunity to be heard - in insurance and in public benefits alike. "
  "A system without fair appeals is a system without justice.",
  "The appellant files within the deadline; the agency or carrier reviews - first internally, then before an administrative judge or external reviewer. "
  "Evidence is taken, witnesses heard, the record reviewed; the decision issues in writing. "
  "Aid paid pending appeal in many benefit programs protects against wrongful termination during the wait.",
  ["Notice, reasons, opportunity to be heard: due process.",
   "Internal review, then impartial adjudication.",
   "Aid pending appeal protects during the wait.",
   "No fair appeals, no justice."],
  ["Appeals tribunals independent of the initial deciders.",
   "Plain-language notices stating appeal rights and deadlines.",
   "Continued benefits during appeal where required."],
  ["Decisions within mandated timeframes.",
   "Impartial adjudicators - no stake in the outcome.",
   "Decisions implemented when appeals succeed."],
  ["Goldberg v. Kelly due-process requirements (public law).",
   "Program-specific appeals regulations (public regulations)."],
  "appealrate", {"appeals": 12000, "overturned": 3600}),

R("Social Security Administration", "Advanced", 28,
  "Social Security is the nation's retirement, disability, and survivors insurance: workers pay in through payroll taxes and earn benefits. "
  "The Social Security Administration runs the largest benefit operation in the country - tens of millions of checks monthly. "
  "Its disability determination process is among the most complex adjudications in government.",
  "Workers earn quarters of coverage; benefits compute from lifetime indexed earnings at retirement, disability, or death. "
  "Disability claims pass through state DDS agencies applying the five-step sequential evaluation. "
  "Field offices and teleservice centers serve the public; the trust funds' solvency is projected annually.",
  ["Retirement, disability, survivors: earned through work.",
   "Payroll taxes in; monthly benefits out.",
   "Disability by the five-step sequential evaluation.",
   "Trust-fund solvency projected annually."],
  ["Field offices, teleservice, and online services.",
   "State DDS agencies for disability adjudication.",
   "Earnings records accurate over lifetimes."],
  ["Benefits paid accurately and timely.",
   "Disability decisions consistent and appealable.",
   "Trust-fund projections published honestly."],
  ["Social Security Act (public law).",
   "SSA regulations and rulings (public regulations)."],
  "benefit", {"base": 1975.0, "household": 1.0}),

R("Benefit Delivery — EBT and Payments", "Advanced", 29,
  "Benefit delivery puts the benefit in hand: EBT cards for food assistance, direct deposit for cash benefits, provider payments for health coverage. "
  "Delivery must be reliable - the family counts on the deposit date - and secure against theft and skimming. "
  "The last mile of the safety net is a payment system.",
  "EBT systems load monthly allotments to household accounts, spent at authorized retailers through POS terminals. "
  "Cash benefits flow by direct deposit or prepaid cards; provider claims pay through fiscal agents. "
  "Lost cards are replaced; skimming is fought with chip technology and transaction monitoring.",
  ["EBT for food; direct deposit for cash; providers paid for health.",
   "Reliable on the deposit date - families count on it.",
   "Secure against theft and skimming.",
   "The last mile is a payment system."],
  ["EBT processing with retailer POS networks.",
   "Direct-deposit and prepaid-card issuance.",
   "Replacement and fraud-monitoring operations."],
  ["Benefits available on the scheduled date.",
   "Stolen benefits replaced per program rules.",
   "Recipient data protected."],
  ["Federal EBT regulations (public regulations).",
   "Treasury payment rules (public regulations)."],
  "benefit", {"base": 281.0, "household": 4.0}),

R("Program Integrity", "Advanced", 30,
  "Program integrity protects benefits from fraud, waste, and abuse: the honest applicant's shield and the taxpayer's. "
  "It spans prevention (eligibility verification), detection (data matching, investigations), and recovery (overpayment collection). "
  "Integrity done wrongly harasses the needy; done rightly it sustains the programs.",
  "Eligibility systems verify income and identity against data sources; anomaly detection flags suspicious patterns. "
  "Investigators pursue recipient fraud and provider fraud; quality control measures payment accuracy. "
  "Overpayments are established with notice and appeal rights, then collected - with hardship waivers where just.",
  ["Prevention, detection, recovery: the integrity triad.",
   "The honest applicant's shield and the taxpayer's.",
   "Data matching and investigation find the fraud.",
   "Overpayments with notice, appeal, and hardship waivers."],
  ["Data-matching with wage and identity sources.",
   "Investigators for recipient and provider fraud.",
   "Quality-control measurement of accuracy."],
  ["Investigations fair - no fishing expeditions against the poor.",
   "Overpayments with due process.",
   "Provider fraud prosecuted; billing abuses excluded."],
  ["Federal program-integrity regulations (public regulations).",
   "Improper Payments laws (public law)."],
  "fraudrate", {"claims": 200000, "flagged": 3200}),

R("Call Centers and Field Offices", "Advanced", 31,
  "Call centers and field offices are where the public meets the program: questions answered, applications taken, problems solved. "
  "They set the citizen's whole impression of government - the wait time, the answer's accuracy, the worker's respect. "
  "Service quality here is democracy's customer service.",
  "Call centers forecast volume, staff to service levels, and train agents on program rules and systems. "
  "Field offices take walk-ins, hold interviews, and verify documents; appointments cut waits. "
  "Quality monitoring scores calls for accuracy and courtesy; callbacks and online accounts deflect routine volume.",
  ["The public's whole impression of the program.",
   "Forecast, staff, train, monitor: the call-center cycle.",
   "Field offices: walk-ins, interviews, verification.",
   "Wait time, accuracy, respect: the service measures."],
  ["Call-center capacity to service-level standards.",
   "Field offices accessible by transit and hours.",
   "Knowledge bases keeping answers current."],
  ["Service levels published and met.",
   "Language access on every channel.",
   "Complaints tracked and resolved."],
  ["Federal customer-service standards (public standards).",
   "Program access regulations (public regulations)."],
  "caseload", {"workers": 120, "cases": 9600}),

R("Disability Determinations", "Advanced", 32,
  "Disability determinations decide who cannot work: among the hardest calls in benefits, weighing medical evidence against work capacity. "
  "Social Security, VA, and private disability each run their own process, but all ask the same core question - can this person sustain work. "
  "Accuracy demands both medical rigor and vocational realism.",
  "Adjudicators gather medical records, order consultative exams where thin, and assess residual functional capacity. "
  "The sequential evaluation tests work activity, severity, listings, past work, and other work. "
  "Denials issue with reasons and appeal rights; hearings before judges rehear the close cases.",
  ["Can this person sustain work: the core question.",
   "Medical rigor plus vocational realism.",
   "Sequential evaluation: five steps.",
   "Close cases reheard by judges."],
  ["Trained disability adjudicators and medical consultants.",
   "Records-gathering and consultative-exam capacity.",
   "Hearing offices for appeals."],
  ["Decisions on the full medical record.",
   "Processing times within standards.",
   "Backlogs not cleared by rubber-stamping denials."],
  ["SSA disability regulations (public regulations).",
   "VA disability rating schedule (public schedule)."],
  "eligibility", {"income": 1450.0, "limit": 1620.0}),

R("The Actuarial Function in Insurance", "Advanced", 33,
  "Actuarial science is insurance's mathematics: modeling uncertain future losses with probability, statistics, and finance. "
  "Actuaries price policies, set reserves, and guard solvency - the profession that keeps promises measurable. "
  "Their credential - years of exams - marks one of the most rigorous in business.",
  "Actuaries build loss models from historical data, trend and develop them, and load for expenses, profit, and risk. "
  "Reserving actuaries estimate unpaid claims; pricing actuaries set rates; valuation actuaries attest to balance-sheet adequacy. "
  "Professional standards bind their methods; regulators and auditors rely on their opinions.",
  ["Uncertain futures modeled mathematically.",
   "Pricing, reserving, solvency: the actuarial three.",
   "Promises kept measurable.",
   "Methods bound by professional standards."],
  ["Credible data and modeling capability.",
   "Credentialed actuaries signing opinions.",
   "Peer review of major analyses."],
  ["Actuarial Standards of Practice followed.",
   "Opinions honest - no shading for management.",
   "Methods disclosed and reproducible."],
  ["Actuarial Standards of Practice (public standards).",
   "NAIC actuarial opinion requirements (public regulations)."],
  "combined", {"loss_ratio": 0.66, "expense_ratio": 0.27}),

R("Insurance and Benefits Mastery Review — Running the Whole System", "Advanced", 34,
  "The mastery review binds the ladder: insurance and benefits as one protection system - private risk pools and public safety nets serving the same human need for security. "
  "Each earlier record was a discipline; this is the leader's mind, running the whole operation. "
  "A master pays claims fairly, determines eligibility accurately, guards the funds honestly, and never forgets the person behind the file number.",
  "Start from the protected person and work outward: the policy or program that covers them, the intake that opens the case, the investigation or verification that finds the facts, the decision that applies the rules, the payment that delivers, the appeal that corrects errors. "
  "Run the operation's rhythms - daily claims and cases, monthly financials, annual rate and budget cycles - and watch the vital signs: loss and combined ratios, payment accuracy, timeliness, appeal overturn rates, fraud losses. "
  "Every metric is a person: the ratio is reserves for real claims, the accuracy rate is families fed or denied.",
  ["One protection system: private pools and public nets.",
   "Work outward from the protected person.",
   "The operation's rhythms: daily, monthly, annual.",
   "Every metric is a person behind the file number."],
  ["Fluency in every record of this database, foundations through advanced.",
   "Leadership that audits itself.",
   "Metrics reviewed together, honestly."],
  ["Claims paid fairly; benefits determined accurately.",
   "Funds guarded honestly; fraud fought fairly.",
   "The person never lost behind the file number."],
  ["NAIC and program regulatory frameworks (public regulations).",
   "Professional ethics for claims and benefits administration (public standards)."],
  "combined", {"loss_ratio": 0.65, "expense_ratio": 0.28}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# Loss-ratio structural sample calculator (insurance)\\n"
   + "losses, prem = 650000.0, 1000000.0\\n"
   + "lr = losses/prem\\n"
   + "print('sample losses:', losses, 'earned premium:', prem)\\n"
   + "print('sample loss ratio:', round(lr,3))\\n"
   + "assert 0 <= lr <= 3\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""


SIG = [
R("The Shared Shield — The Signature View", "Foundations", 1,
  "The Signature view sees insurance and benefits as the shared shield: the many guarding the few, the strong season funding the hard. "
  "The pools, the prices, and the payments are the same as the public edition's; the difference is the vow - every claim a sworn accounting, every benefit a kept promise, every appeal a reheard case. "
  "This edition reframes the full ladder as Signature science, labeled Signature-made throughout.",
  "Where the public edition teaches the mechanics, the Signature edition teaches the keeping: underwriting as honest pricing, adjusting as fair judgment, determination as careful mercy. "
  "Each record pairs the operational truth with its Signature seal - the practice that makes protection worthy of the protected. "
  "Nothing here is presented as public record; it is his original method.",
  ["The shared shield: the many guarding the few.",
   "Every claim a sworn accounting; every benefit a kept promise.",
   "Each discipline carrying its Signature seal.",
   "Signature-made throughout: an original method, never public record."],
  ["Willingness to hold fairness, accuracy, and mercy as sworn.",
   "The public edition alongside for the mechanics.",
   "An operation where the method can be practiced."],
  ["No Signature claim presented as public or official record.",
   "The protected person above every ratio.",
   "The method taught as his original system, plainly labeled."],
  ["The public edition of this database, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "lossratio", {"losses": 62000000.0, "earned_prem": 95000000.0}),

R("The Written Promise — Signature Policy", "Foundations", 2,
  "The Signature method writes the promise plainly: declarations, grants, carve-backs, duties, and tailorings - every term known before the loss. "
  "The cheapest protection education is reading the policy in peacetime. "
  "No exclusion buried; no change by word of mouth alone.",
  "The declarations name the shielded, the covered, the limits, and the price. "
  "Grants give; exclusions trim; conditions bind both sides to duties like prompt notice. "
  "Tailorings fit the standard contract to the life it protects.",
  ["The promise written plainly, read in peacetime.",
   "Known before the loss: who, what, how much.",
   "No exclusion buried.",
   "Changes in writing."],
  ["A policy for every coverage.",
   "Plain summaries beside the legal text.",
   "Tailorings documented and priced."],
  ["Terms delivered with the policy.",
   "Exclusions conspicuous.",
   "Changes endorsed, never verbal-only."],
  ["NAIC readability standards (public standards).",
   "The public edition policy record, for the mechanics (this system)."],
  "premium", {"rate": 1.85, "exposure": 240.0}),

R("The Honest Price — Signature Premiums", "Foundations", 3,
  "The Signature method prices honestly: each class paying its expected cost, no more, no less - fairness as arithmetic. "
  "History is studied, classes are grouped, discounts reward the careful. "
  "Discrimination is theft by formula, and the method forbids it.",
  "Loss histories are studied class by class; rates are filed and approved before use. "
  "Underwriters weigh the individual within the filed bounds; expenses and a fair return are loaded. "
  "The careful - safe drivers, guarded buildings - pay less, for they cost less.",
  ["Each class its expected cost: fairness as arithmetic.",
   "History studied; rates filed before use.",
   "Discounts rewarding the careful.",
   "Discrimination forbidden."],
  ["Histories credible by class.",
   "Rates filed and approved.",
   "Guidelines applied evenly."],
  ["No unfair discrimination.",
   "Filings backed by data.",
   "Discounts truly earned."],
  ["Actuarial ratemaking standards (public standards).",
   "The public edition premiums record, for the mechanics (this system)."],
  "premium", {"rate": 0.92, "exposure": 1500.0}),

R("The First Call — Signature FNOL", "Foundations", 4,
  "The Signature method answers the first call as the claim's birth: swiftly, completely, around the clock - for the adjuster assigned today finds fresher truth than next week's. "
  "Who, what, when, where, how - and the insured leaves with a number, a name, and next steps. "
  "Uncertainty is the enemy at the first call.",
  "Intake gathers the five facts, verifies the policy, and triages coverage at once. "
  "The claim is opened, reserves posted, and the fitting adjuster assigned by line and severity. "
  "Surge plans stand ready for the disaster days.",
  ["The first call the claim's birth.",
   "Swift, complete, around the clock.",
   "A number, a name, next steps.",
   "Uncertainty the enemy."],
  ["Intake on every channel, day and night.",
   "Systems opening and routing at once.",
   "Triage at intake."],
  ["Acknowledged within the mandated hours.",
   "No discouraging of valid claims.",
   "Surge ready for catastrophes."],
  ["NAIC claims-handling models (public regulations).",
   "The public edition FNOL record, for the mechanics (this system)."],
  "reserve", {"paid": 0.0, "case_reserve": 25000.0}),

R("The Fair Judge — Signature Adjuster", "Foundations", 5,
  "The Signature method sets the fair judge over the loss: investigating like a detective, reckoning like an accountant, settling like a diplomat. "
  "The adjuster is the promise made personal - the human who arrives after the fire. "
  "Coverage is decided in writing, with reasons; disputes have their roads.",
  "Damage is inspected, parties interviewed, records gathered, policy read against the facts. "
  "Losses are valued - repair, cash value, replacement - and settlements negotiated fairly. "
  "Files are kept so the decision can be rebuilt years hence.",
  ["Detective, accountant, diplomat.",
   "The promise made personal.",
   "Decisions in writing, with reasons.",
   "Files rebuildable years hence."],
  ["Licensed judges of loss.",
   "Investigative resources.",
   "Authority fit to severity."],
  ["Settled promptly and fairly.",
   "Denials explained.",
   "Files audit-ready."],
  ["State licensing laws (public regulations).",
   "The public edition adjuster record, for the mechanics (this system)."],
  "lossratio", {"losses": 18500000.0, "earned_prem": 28000000.0}),

R("The Road's Reckoning — Signature Auto Claims", "Foundations", 6,
  "The Signature method reckons the road's losses by the million: liability for harms to others, collision and comprehensive for the car, injury coverages for the hurt. "
  "Fault follows the facts and the land's law; repairs restore; totals are valued by the market's truth. "
  "Speed with fairness wins the renewal.",
  "Statements are taken, reports ordered, vehicles seen by eye or by photo. "
  "Liability is weighed; damages estimated by shops or systems. "
  "The injured are handled without bad-faith delay.",
  ["Liability, collision, comprehensive, injury.",
   "Fault following facts and law.",
   "Repairs restoring; totals market-valued.",
   "Speed with fairness."],
  ["Intake with vehicle and injury triage.",
   "Shops or systems for estimates.",
   "Injury adjusters."],
  ["Values from true market data.",
   "Repairs to pre-loss state.",
   "No bad-faith delay on injuries."],
  ["State auto regulations (public regulations).",
   "The public edition auto record, for the mechanics (this system)."],
  "lossratio", {"losses": 41000000.0, "earned_prem": 58000000.0}),

R("The Rebuilding — Signature Property Claims", "Foundations", 7,
  "The Signature method rebuilds: measuring the damage, parting covered perils from excluded, getting families and businesses rising again. "
  "Wind is not flood; the policy's words decide. "
  "Displaced families are housed while the hammers swing.",
  "Adjusters document and scope with contractors; valuation follows the policy's method. "
  "Catastrophes summon the surge - thousands of claims, one plan. "
  "Living expenses flow while repairs proceed.",
  ["Measuring, parting perils, rebuilding.",
   "The policy's words deciding.",
   "Families housed while hammers swing.",
   "Catastrophes summoning the surge."],
  ["Field adjusters and contractors.",
   "Scoping systems.",
   "Surge plans drilled."],
  ["Peril splits per the policy.",
   "Depreciation fair and shown.",
   "Living expenses paid."],
  ["State property regulations (public regulations).",
   "The public edition property record, for the mechanics (this system)."],
  "reserve", {"paid": 45000.0, "case_reserve": 120000.0}),

R("The Safety Net — Signature Benefits View", "Foundations", 8,
  "The Signature method sees the safety net: food, health, cash, work-insurance, disability, retirement - the people's shared promise to the vulnerable. "
  "Eligibility is set in law; the benefit is a right when earned by need. "
  "Appeals guard against the wrong denial.",
  "Laws create; agencies administer - applications, determinations, delivery. "
  "Taxpayers fund; EBT, deposits, and providers deliver. "
  "Every program carries the right to be heard.",
  ["The shared promise to the vulnerable.",
   "Eligibility in law; benefit a right when met.",
   "Funded by all; delivered to the needy.",
   "The right to be heard in every program."],
  ["Statutes and rules per program.",
   "Agencies staffed and systemed.",
   "Funds appropriated and accounted."],
  ["Rules applied evenly.",
   "Decisions written, appealable.",
   "Benefits timely once determined."],
  ["Program statutes (public law).",
   "The public edition benefits record, for the mechanics (this system)."],
  "eligibility", {"income": 2850.0, "limit": 3200.0}),

R("The Open Door — Signature Applications", "Foundations", 9,
  "The Signature method keeps the door open: plain words, many channels, help for the struggling - for barriers at the door are denials by design. "
  "The filing date guards retroactive benefits. "
  "Navigators, languages, and accommodations welcome all.",
  "Household, income, and need are stated; completeness is screened; verification is requested, not assumed absent. "
  "Interviews clarify; the date is honored. "
  "Help is offered, not merely forms handed over.",
  ["The door open: plain words, many channels.",
   "Barriers at the door are denials by design.",
   "The filing date guarding retroactive benefits.",
   "Help offered."],
  ["Applications on every channel.",
   "Languages and accommodations.",
   "Trained intake hands."],
  ["No discrimination at the door.",
   "Filing dates honored.",
   "Help, not just forms."],
  ["Federal accessibility rules (public regulations).",
   "The public edition applications record, for the mechanics (this system)."],
  "eligibility", {"income": 1950.0, "limit": 2400.0}),

R("The Careful Weighing — Signature Determination", "Foundations", 10,
  "The Signature method weighs carefully: income, assets, household, category - decided accurately and timely, for need does not wait and error harms both ways. "
  "Verified, not assumed; written, with reasons; appealable. "
  "Changing lives are reweighed on schedule.",
  "Data and documents are checked; limits, deductions, and asset tests applied. "
  "The decision issues plainly. "
  "Redeterminations follow life's changes.",
  ["Accurate and timely: error harms both ways.",
   "Verified, not assumed.",
   "Written with reasons; appealable.",
   "Reweighed as lives change."],
  ["Workers trained in the rules.",
   "Data for verification.",
   "Rules engines true."],
  ["Decided within mandated days.",
   "Notices plain, rights stated.",
   "No eligible denied by error."],
  ["Program regulations (public regulations).",
   "The public edition determination record, for the mechanics (this system)."],
  "eligibility", {"income": 3100.0, "limit": 2950.0}),

R("The Human Link — Signature Case Work", "Foundations", 11,
  "The Signature method honors the human link: the worker who knows the cases, interviews with care, and connects families to help. "
  "Caseloads decide quality - the many-cased worker knows none. "
  "Supervision and training guard the accuracy.",
  "Interviews, verification, entry, maintenance: the worker's cycle. "
  "Samples are reviewed; rule changes are taught. "
  "Each step is timed, measured, reported.",
  ["The worker the most important link.",
   "Caseloads deciding quality.",
   "Interviewed with care.",
   "Supervised and trained."],
  ["Workers enough for knowing.",
   "Training ongoing.",
   "Review of decisions."],
  ["Caseloads guarding quality.",
   "Accuracy and bias reviewed.",
   "Field workers kept safe."],
  ["Administration standards (public regulations).",
   "The public edition case-work record, for the mechanics (this system)."],
  "caseload", {"workers": 45, "cases": 6750}),

R("The First Reckoning — Signature Insurance Math", "Foundations", 12,
  "The Signature method reckons first: losses over earned premium - the cents per dollar paid in claims. "
  "Add expenses for the combined; under a hundred is profit. "
  "The ratio is only as true as the reserves beneath it.",
  "Earned premium counts elapsed time; losses count paid plus reserved. "
  "Expenses - commissions, salaries, overhead - join over earned premium. "
  "The float's earnings may rescue a narrow loss.",
  ["Losses over earned premium.",
   "Combined: losses plus expenses.",
   "Under a hundred: profit.",
   "True as the reserves beneath."],
  ["Earned premium and incurred losses.",
   "Honest expense allocation.",
   "Actuarial reserves."],
  ["Computed consistently.",
   "Reserves adequate.",
   "Per statutory accounting."],
  ["Statutory accounting (public standards).",
   "The public edition math record, for the mechanics (this system)."],
  "lossratio", {"losses": 65000000.0, "earned_prem": 100000000.0}),
]

SIG += [
R("The Truth-Finding — Signature Investigation", "Compounded", 13,
  "The Signature method finds truth: what happened, what is covered, what it is worth - depth following size and red flags. "
  "The duty is to the facts, not the outcome. "
  "Files are kept rebuildable for the years ahead.",
  "Statements recorded, scenes seen, records gathered - police, medical, repair, financial. "
  "Experts answer the hard questions; oaths compel testimony when needed. "
  "Every step is written down.",
  ["Truth first, coverage second.",
   "Depth following size and flags.",
   "Statements, scenes, records, experts.",
   "Rebuildable files."],
  ["Licensed investigators.",
   "Records and experts.",
   "Oath authority in the policy."],
  ["Reasonable, not harassing.",
   "Surveillance only where justified.",
   "Files audit-ready."],
  ["State regulations (public regulations).",
   "The public edition investigation record, for the mechanics (this system)."],
  "reserve", {"paid": 12000.0, "case_reserve": 88000.0}),

R("The Honest Estimate — Signature Reserves", "Compounded", 14,
  "The Signature method estimates honestly: every open claim carrying its true expected cost - the balance sheet's greatest liability, never flattered. "
  "Case reserves per claim; bulk for the unreported. "
  "Under-reserving flatters today and bankrupts tomorrow.",
  "Adjusters set from the facts - damages known, exposure weighed, jurisdiction considered. "
  "Development is watched: raised for the scheduled surgery, lowered for the healed. "
  "Actuaries test the whole; auditors review.",
  ["Honest estimates, never flattered.",
   "Per claim and in bulk.",
   "Watched as claims develop.",
   "Flattery today, ruin tomorrow."],
  ["Disciplined adjusters.",
   "Actuarial review.",
   "Credible data."],
  ["Adequate and documented.",
   "No smoothing of earnings.",
   "Reviewed by regulators."],
  ["Actuarial reserving standards (public standards).",
   "The public edition reserves record, for the mechanics (this system)."],
  "reserve", {"paid": 250000.0, "case_reserve": 1750000.0}),

R("The Fair Bargain — Signature Settlement", "Compounded", 15,
  "The Signature method bargains fairly: valuing the loss honestly and settling within authority - for most claims end here, and trials cost all. "
  "Lowballing buys litigation; fairness buys peace. "
  "Releases are drafted to truly release.",
  "Liability and damages are weighed; offers anchored in the file's evidence. "
  "Demands and counters proceed; mediation breaks the deadlocked. "
  "Payment follows promptly.",
  ["Valued honestly; settled fairly.",
   "Most claims ending here.",
   "Offers anchored in evidence.",
   "Releases truly releasing."],
  ["Trained negotiators with authority.",
   "Verdict and damage data.",
   "Mediators for deadlocks."],
  ["No exploiting the unrepresented.",
   "Authority honored.",
   "Prompt payment."],
  ["State settlement regulations (public regulations).",
   "The public edition settlement record, for the mechanics (this system)."],
  "combined", {"loss_ratio": 0.68, "expense_ratio": 0.29}),

R("The Recovery — Signature Subrogation", "Compounded", 16,
  "The Signature method recovers: having paid its own, the carrier steps into their shoes against the at-fault - billions returned to the pool, the careless held to account. "
  "Recovery is sought at the first notice. "
  "The insured is made whole before the carrier profits.",
  "Liable parties and their insurers are named early; demands go out; arbitration settles carrier disputes. "
  "Recoveries credit the loss; deductibles return to insureds first where the law says. "
  "Limitations are watched like hawks.",
  ["Paid its own, then pursuing the at-fault.",
   "Sought at first notice.",
   "Billions returned; the careless accountable.",
   "The insured whole first."],
  ["Recovery staff.",
   "Arbitration membership.",
   "Lien tracking."],
  ["Insureds whole before profit.",
   "Deductible refunds per law.",
   "Limitations watched."],
  ["State subrogation rules (public regulations).",
   "The public edition subrogation record, for the mechanics (this system)."],
  "subro", {"paid": 42000.0, "recovered": 31500.0}),

R("The Watchers — Signature Fraud Detection", "Compounded", 17,
  "The Signature method watches for thieves: staged wrecks, swollen repairs, phantom hurts, fires for profit - all stealing from every honest policyholder. "
  "Scored at intake, investigated when flagged, prosecuted when proven. "
  "And the honest wrongly accused is a second victim - precision is mercy.",
  "Indicators are scored; the flagged are investigated - statements, justified surveillance, records. "
  "Intelligence is shared across carriers; law enforcement is partnered. "
  "Proven fraud is denied and referred; every step file-backed.",
  ["Watching for thieves of the pool.",
   "Scored at intake; investigated when flagged.",
   "Shared intelligence; partnered law.",
   "Precision is mercy."],
  ["Trained investigators.",
   "Scoring in the system.",
   "Database and liaison."],
  ["Lawful and proportionate.",
   "Denials file-backed.",
   "Prosecution where warranted."],
  ["State fraud statutes (public law).",
   "The public edition fraud record, for the mechanics (this system)."],
  "fraudrate", {"claims": 50000, "flagged": 1250}),

R("The Neighbor's Harm — Signature Liability", "Compounded", 18,
  "The Signature method answers the neighbor's harm: defending the insured and paying the covered - negligence weighed duty, breach, causation, damages, claim by claim. "
  "Counsel is assigned when suits come; settlements weigh the verdict's risk. "
  "The insured is never exposed by bad faith.",
  "Incidents, injuries, and fault are investigated under the land's negligence law. "
  "Grants and exclusions are applied line by line. "
  "Good-faith settlements within limits are pursued.",
  ["Defending; paying the covered.",
   "Negligence weighed claim by claim.",
   "Grants and exclusions line by line.",
   "Never exposed by bad faith."],
  ["Adjusters versed in negligence.",
   "Counsel panels.",
   "Verdict data."],
  ["Defense when duty triggers.",
   "Good-faith settlements.",
   "No bad-faith exposure."],
  ["State tort law (public law).",
   "The public edition liability record, for the mechanics (this system)."],
  "lossratio", {"losses": 33000000.0, "earned_prem": 47000000.0}),

R("The Worker's Bargain — Signature Workers' Comp", "Compounded", 19,
  "The Signature method keeps the worker's bargain: care and wages without fault's proof, lawsuits traded for certainty. "
  "Employment verified, injuries work-born, care authorized, wages paid by statute's formula. "
  "Healed and accommodated back to work - that is the measure.",
  "Nurses coordinate treatment; boards hear disputes; impairments are rated when healing plateaus. "
  "Return-to-work is coordinated with employers. "
  "Retaliation for filing is forbidden.",
  ["Care and wages without fault's proof.",
   "Verified, authorized, paid by statute.",
   "Return to work the measure.",
   "Retaliation forbidden."],
  ["Adjusters expert in the statute.",
   "Medical networks and nurses.",
   "Return-to-work coordination."],
  ["Benefits timely per formula.",
   "Care not unreasonably denied.",
   "No retaliation."],
  ["State comp statutes (public law).",
   "The public edition comp record, for the mechanics (this system)."],
  "combined", {"loss_ratio": 0.72, "expense_ratio": 0.26}),

R("The Careful Payment — Signature Health Adjudication", "Compounded", 20,
  "The Signature method pays carefully: eligibility, coverage, necessity - three checks on every medical bill, millions daily, the routine by machine and the exceptions by human eyes. "
  "Denials carry reasons and appeal rights; necessity disputes get clinical review. "
  "Accuracy is dollars and denied care both.",
  "Codes are checked, rates contracted, member shares computed. "
  "Clean claims pay within mandated days. "
  "Parity for mental health is honored.",
  ["Three checks on every bill.",
   "Machines for routine; humans for exceptions.",
   "Denials with reasons and rights.",
   "Dollars and denied care."],
  ["Electronic intake with edits.",
   "Contracted fee schedules.",
   "Clinical review."],
  ["Clean claims timely.",
   "Denials explained, appealable.",
   "Parity honored."],
  ["Federal claims rules (public regulations).",
   "The public edition adjudication record, for the mechanics (this system)."],
  "adjudication", {"billed": 2400.0, "allowed": 1450.0}),

R("The Full Table — Signature Food Assistance", "Compounded", 21,
  "The Signature method fills the table: monthly food benefits on EBT, scaled to household and income, spent at honest retailers. "
  "Eligibility accurate at scale; retailers policed. "
  "Trafficking is theft from the hungry.",
  "States apply federal rules, issue allotments, and recheck on schedule. "
  "Changes are reported; quality samples measure accuracy. "
  "Retailers are authorized and watched.",
  ["The table filled monthly.",
   "Scaled to household and income.",
   "Accurate at scale.",
   "Trafficking theft from the hungry."],
  ["Eligibility systems and workers.",
   "EBT and retailer authorization.",
   "Quality sampling."],
  ["Timely per federal frames.",
   "Allotments true to circumstances.",
   "Trafficking prosecuted."],
  ["Food and Nutrition Act (public law).",
   "The public edition SNAP record, for the mechanics (this system)."],
  "benefit", {"base": 281.0, "household": 3.0}),

R("The Healing Coverage — Signature Medicaid", "Compounded", 22,
  "The Signature method covers healing: federal and state funds joined, states running within federal law, for children, mothers, the aged, the disabled. "
  "Eligibility at scale, managed care overseen, providers paid. "
  "Rolls kept accurate as lives change.",
  "Data-driven renewals enroll the eligible; plans are paid per member; access is overseen. "
  "Rates are actuarially sound. "
  "No eligible wrongly turned away at renewal.",
  ["Funds joined; states running.",
   "The vulnerable covered.",
   "Overseen care; sound rates.",
   "Rolls accurate."],
  ["Eligibility systems with renewals.",
   "Managed-care contracts.",
   "Access standards."],
  ["Eligible enrolled.",
   "Access met.",
   "Rates sound."],
  ["Title XIX (public law).",
   "The public edition Medicaid record, for the mechanics (this system)."],
  "benefit", {"base": 6200.0, "household": 1.0}),

R("The Bridge Between Jobs — Signature Unemployment", "Compounded", 23,
  "The Signature method bridges between jobs: part of lost wages for the laid-off through no fault - the economy's stabilizer. "
  "Employers fund; states run; weekly the worker certifies able, available, seeking. "
  "Recessions extend the bridge.",
  "Wages are reported quarterly; claims filed at layoff; eligibility determined monetarily. "
  "Separations are adjudicated - quit versus fired matters. "
  "Working while collecting is fraud.",
  ["The bridge between jobs.",
   "Funded by employers; run by states.",
   "Weekly: able, available, seeking.",
   "Extended in recessions."],
  ["Wage records.",
   "Claims and certification processing.",
   "Appeal tribunals."],
  ["Timely decisions.",
   "Statutory duration paid.",
   "Fraud detected."],
  ["FUTA and state laws (public law).",
   "The public edition UI record, for the mechanics (this system)."],
  "benefit", {"base": 420.0, "household": 1.0}),
]

SIG += [
R("The Bottom Line — Signature Combined Ratio", "Advanced", 24,
  "The Signature method reads the bottom line: losses plus expenses over premium - under a hundred, profit; over, loss. "
  "Watched by line, state, and year; the unprofitable cut or repriced. "
  "Investment may offset, never excuse.",
  "Losses incurred over earned premium; expenses over earned premium; the two summed. Management watches by line, state, and year - cutting or repricing the unprofitable. Analysts and rating agencies judge sustained ratios under a hundred.",
  ["Losses plus expenses over premium.",
   "Under a hundred: profit.",
   "Watched everywhere.",
   "Offset, never excuse."],
  ["Credible data by segment.",
   "Will to exit the unprofitable.",
   "Actuarial repricing."],
  ["Honestly reported.",
   "Consistent allocation.",
   "Reserves adequate."],
  ["Statutory accounting (public standards).",
   "The public edition combined-ratio record, for the mechanics (this system)."],
  "combined", {"loss_ratio": 0.63, "expense_ratio": 0.28}),

R("The Insurer's Shield — Signature Reinsurance", "Advanced", 25,
  "The Signature method shields the insurer: risk ceded upward, catastrophes layered, the globe diversifying - no single storm sinking the house. "
  "Treaties for portfolios; facultative for the great single risks. "
  "The carrier pays its own, then collects per the treaty.",
  "Peak exposures are modeled; layers are bought - working layers for frequency, catastrophe layers for the great one. Reinsurers diversify across the globe. The carrier pays its insured first, then collects from the reinsurer per the treaty.",
  ["Risk ceded upward.",
   "Catastrophes layered.",
   "The globe diversifying.",
   "No storm sinking the house."],
  ["Modeled peak exposures.",
   "Brokers and treaty craft.",
   "Collateral for credit risk."],
  ["Contracts honored on the big losses.",
   "Credit watched.",
   "Dependence disclosed."],
  ["NAIC credit rules (public regulations).",
   "The public edition reinsurance record, for the mechanics (this system)."],
  "combined", {"loss_ratio": 0.58, "expense_ratio": 0.24}),

R("The Surge — Signature Catastrophe Response", "Advanced", 26,
  "The Signature method surges when disaster strikes: thousands of claims in days, the promise tested at scale - speed as compassion, accuracy as solvency. "
  "Roles pre-assigned, imagery ordered, adjusters deployed, centers opened. "
  "The disaster-chasers are watched while the victims are served.",
  "The plan pre-assigns roles: imagery ordered, adjusters deployed, contractors called, mobile centers opened. Drones and satellites triage whole neighborhoods; adjusters settle by the hundred. Reinsurance is noticed; regulators get their data calls.",
  ["Thousands in days.",
   "Speed compassion; accuracy solvency.",
   "Roles pre-assigned; centers opened.",
   "Victims served; chasers watched."],
  ["A written, drilled plan.",
   "Surge hands and imagery.",
   "Mobile centers."],
  ["Catastrophe timeframes kept.",
   "No exploiting victims.",
   "Fraud watched amid surge."],
  ["State CAT regulations (public regulations).",
   "The public edition CAT record, for the mechanics (this system)."],
  "lossratio", {"losses": 890000000.0, "earned_prem": 1200000000.0}),

R("The Second Hearing — Signature Appeals", "Advanced", 27,
  "The Signature method grants the second hearing: notice, reasons, and the chance to be heard - for insurance and benefits alike. "
  "Internal review, then the impartial judge; aid continuing through the wait where the law says. "
  "No fair appeals, no justice.",
  "The appellant files within the deadline; the case is reviewed - first inside, then before an impartial judge. Evidence is taken, the record reviewed, the decision written. Aid continues through the wait where the law commands it.",
  ["Notice, reasons, hearing.",
   "Internal, then impartial.",
   "Aid through the wait.",
   "Justice requires appeal."],
  ["Tribunals independent.",
   "Plain notices with deadlines.",
   "Continued aid where required."],
  ["Timely decisions.",
   "Impartial judges.",
   "Wins implemented."],
  ["Due-process law (public law).",
   "The public edition appeals record, for the mechanics (this system)."],
  "appealrate", {"appeals": 12000, "overturned": 3600}),

R("The Earned Rest — Signature Social Security", "Advanced", 28,
  "The Signature method honors the earned rest: payroll taxes in through working years, monthly benefits out in retirement, disability, or loss. "
  "Quarters earned; benefits from lifetime earnings. "
  "Disability weighed by five steps; solvency projected yearly.",
  "Quarters of coverage are earned; benefits compute from lifetime indexed earnings. Disability claims pass through state agencies and the five-step evaluation. Field offices and teleservice serve; trust-fund solvency is projected yearly.",
  ["Taxes in; benefits out.",
   "Earned through work.",
   "Disability by five steps.",
   "Solvency projected."],
  ["Offices, phones, online.",
   "Disability adjudicators.",
   "Lifetime earnings records."],
  ["Accurate and timely.",
   "Decisions appealable.",
   "Projections honest."],
  ["Social Security Act (public law).",
   "The public edition SSA record, for the mechanics (this system)."],
  "benefit", {"base": 1975.0, "household": 1.0}),

R("The Last Mile — Signature Benefit Delivery", "Advanced", 29,
  "The Signature method walks the last mile: EBT loaded monthly, deposits landing on the date, providers paid - reliable, for families count on the day. "
  "Secured against theft and skimming; lost cards replaced. "
  "The payment system is the safety net's hand.",
  "Monthly allotments load to EBT accounts, spent at authorized retailers through POS. Cash flows by deposit or card; providers are paid through fiscal agents. Lost cards are replaced; skimming fought with chips and monitoring.",
  ["Loaded monthly; landing on the date.",
   "Reliable: families count on it.",
   "Secured against theft.",
   "The net's hand."],
  ["EBT and POS networks.",
   "Deposit and card issuance.",
   "Fraud monitoring."],
  ["Available on schedule.",
   "Stolen replaced per rules.",
   "Data protected."],
  ["Federal EBT rules (public regulations).",
   "The public edition delivery record, for the mechanics (this system)."],
  "benefit", {"base": 281.0, "household": 4.0}),

R("The Guarded Purse — Signature Program Integrity", "Advanced", 30,
  "The Signature method guards the purse: prevention, detection, recovery - the honest applicant's shield and the taxpayer's. "
  "Verified at entry, matched in data, investigated with cause. "
  "Wrongly done it harasses the needy; rightly done it sustains all.",
  "Systems verify income and identity against data; anomalies are flagged; investigators pursue recipient and provider fraud. Quality control measures accuracy. Overpayments are established with notice and appeal, collected with hardship waivers where just.",
  ["Prevention, detection, recovery.",
   "Shield of honest and taxpayer.",
   "Verified, matched, investigated.",
   "Sustaining all."],
  ["Data matching.",
   "Investigators.",
   "Quality measurement."],
  ["Fair investigations.",
   "Due process on overpayments.",
   "Fraud prosecuted."],
  ["Federal integrity rules (public regulations).",
   "The public edition integrity record, for the mechanics (this system)."],
  "fraudrate", {"claims": 200000, "flagged": 3200}),

R("The Public's Door — Signature Service Centers", "Advanced", 31,
  "The Signature method opens the public's door: calls answered, walk-ins welcomed, questions resolved - the citizen's whole impression of the promise. "
  "Forecast and staff; train and monitor. "
  "Wait time, accuracy, respect: the measures.",
  "Volume is forecast, staff set to service levels, agents trained on rules and systems. Field offices take walk-ins and verify documents; appointments cut waits. Calls are scored for accuracy and courtesy; routine volume deflects online.",
  ["Calls answered; walk-ins welcomed.",
   "The whole impression.",
   "Forecast, staff, train, monitor.",
   "Respect the measure."],
  ["Capacity to standard.",
   "Accessible offices.",
   "Current knowledge."],
  ["Levels published and met.",
   "Every language served.",
   "Complaints resolved."],
  ["Federal service standards (public standards).",
   "The public edition service record, for the mechanics (this system)."],
  "caseload", {"workers": 120, "cases": 9600}),

R("The Hardest Call — Signature Disability", "Advanced", 32,
  "The Signature method makes the hardest call: weighing medical truth against work capacity - can this person sustain work. "
  "Records gathered, exams ordered where thin, capacity assessed. "
  "Five steps; close cases reheard; backlogs never cleared by rubber stamps.",
  "Medical records are gathered; consultative exams ordered where thin; residual capacity assessed. The five steps test work activity, severity, listings, past work, other work. Denials carry reasons and rights; judges rehear the close cases.",
  ["The hardest call.",
   "Medical truth, work capacity.",
   "Five steps.",
   "Close cases reheard."],
  ["Trained adjudicators.",
   "Records and exams.",
   "Hearing offices."],
  ["Full records decided.",
   "Timely processing.",
   "No rubber stamps."],
  ["SSA regulations (public regulations).",
   "The public edition disability record, for the mechanics (this system)."],
  "eligibility", {"income": 1450.0, "limit": 1620.0}),

R("The Measurers — Signature Actuarial Science", "Advanced", 33,
  "The Signature method measures the uncertain: probability, statistics, finance - pricing policies, setting reserves, guarding solvency. "
  "Promises made measurable. "
  "Standards binding; opinions honest.",
  "Loss models rise from historical data, trended and developed, loaded for expense, profit, and risk. Reserving actuaries estimate the unpaid; pricing actuaries set rates; valuation actuaries attest adequacy. Standards bind the methods.",
  ["The uncertain measured.",
   "Pricing, reserving, solvency.",
   "Promises measurable.",
   "Opinions honest."],
  ["Credible data and models.",
   "Credentialed signers.",
   "Peer review."],
  ["Standards followed.",
   "No shading for management.",
   "Methods reproducible."],
  ["Actuarial Standards (public standards).",
   "The public edition actuarial record, for the mechanics (this system)."],
  "combined", {"loss_ratio": 0.66, "expense_ratio": 0.27}),

R("The Steward's Ledger — Signature Mastery", "Advanced", 34,
  "The steward's ledger closes the ladder: private pools and public nets as one protection system, the person behind every file number. "
  "From the covered outward - policy, intake, facts, decision, payment, appeal. "
  "Rhythms run daily, monthly, yearly; gauges read together: ratios, accuracy, timeliness, overturns, fraud. "
  "Every metric a person: reserves for real claims, accuracy for fed families.",
  "From the protected person outward: the policy or program, the intake, the facts, the decision, the payment, the appeal. Daily claims, monthly financials, annual rates and budgets - gauges read together: ratios, accuracy, timeliness, overturns, fraud. Every metric a person.",
  ["One protection system.",
   "Outward from the person.",
   "Rhythms daily, monthly, yearly.",
   "Every metric a person."],
  ["The full ladder fluent.",
   "Self-auditing leadership.",
   "Gauges read together."],
  ["Fair claims; accurate benefits.",
   "Honest funds; fair fraud-fighting.",
   "The person never lost."],
  ["The public edition mastery record, for the mechanics (this system).",
   "Signature system governance on original works (this system)."],
  "combined", {"loss_ratio": 0.65, "expense_ratio": 0.28}),
]

GEN_DEMOFN = """function demoProgram(topic,field){
  var safe=String(topic).replace(/\\\\/g,'\\\\\\\\').replace(/"/g,"'");
  return "#!/usr/bin/env python3\\n"
   + "# "+safe+" -- structural sample demo. Property of Justin Addam Higgins (JAH).\\n"
   + "# Loss-ratio structural sample calculator (insurance)\\n"
   + "losses, prem = 650000.0, 1000000.0\\n"
   + "lr = losses/prem\\n"
   + "print('sample losses:', losses, 'earned premium:', prem)\\n"
   + "print('sample loss ratio:', round(lr,3))\\n"
   + "assert 0 <= lr <= 3\\n"
   + "print('OK: structural sample demo ran')\\n";
}
"""
