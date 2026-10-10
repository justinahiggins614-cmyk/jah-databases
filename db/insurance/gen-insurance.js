/* JAH Insurance Database generator — jahdb-insurance-1.0. Property of Justin Addam Higgins (JAH).
   Deterministic: seed -> full insurance entry. 1,000,000 address space (seed % 1M).
   Records are either sourced (real, verifiable insurance knowledge) or Signature-generated
   (homegrown guides/scenarios), labeled in `origin`. Never fabricates real-world facts.
   Educational content only \u2014 not financial advice; consult a licensed professional. */
(function () {
'use strict';
function prng(seed) { var a = (seed >>> 0) || 1; return function () { a |= 0; a = (a + 0x6D2B79F5) | 0; var t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
function pick(a, r) { return a[(r() * a.length) | 0]; }
function ri(r, a, b) { return a + ((r() * (b - a + 1)) | 0); }
function shuffle(a, r) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = (r() * (i + 1)) | 0; var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
function interleave(lists) { var out = [], i = 0, more = true; while (more) { more = false; for (var k = 0; k < lists.length; k++) { if (i < lists[k].length) { out.push(lists[k][i]); more = true; } } i++; } return out; }

var SLUG = 'insurance';
var PREFIX = 'JAH-INS-';
var VERSION = 'jahdb-insurance-1.0';
var RECORD_KIND = 'insurance entry';
var CATS = ['insurance-type', 'policy-term', 'coverage-guide', 'claims-process'];

/* ================= REAL (sourced) data: [title, key_points, body] ================= */
var REAL_TYPES = [
['Term life insurance', 'Pure protection for a set period (10, 20, 30 years); pays the death benefit only if death occurs during the term', 'Term life is the simplest life insurance: choose a term length and a death benefit, pay level premiums, and the policy pays if you die within the term. It builds no cash value, which keeps premiums far lower than permanent insurance. Most financial educators recommend term for income replacement during working years.'],
['Whole life insurance', 'Permanent coverage with level premiums, a cash value that grows, and dividends possible from mutual insurers', 'Whole life covers you for life as long as premiums are paid. Part of each premium funds the death benefit; part builds cash value that grows tax-deferred and can be borrowed against. Premiums are much higher than term for the same death benefit.'],
['Universal life insurance', 'Flexible permanent insurance: adjustable premiums and death benefit around a cash-value account', 'Universal life separates the insurance cost from the savings element, letting policyholders adjust payments within limits. Interest credited to the cash value varies with market rates, so performance \u2014 and the risk of lapse \u2014 depends on funding discipline.'],
['Health insurance', 'Covers medical costs in exchange for premiums; cost-sharing through deductibles, copays, and coinsurance', 'Health insurance pays for covered medical services after cost-sharing. Plans differ in networks, premiums, and out-of-pocket limits. In the US, major sources are employer plans, marketplace plans, and public programs like Medicare and Medicaid.'],
['Auto liability insurance', 'Pays for injuries and damage you cause to others; required in nearly every US state', 'Liability has two parts: bodily injury (medical costs of others) and property damage (their vehicle or property). State minimums are often far below what a serious crash costs, so higher limits are widely recommended.'],
['Collision coverage', 'Pays to repair your own car after a collision, minus your deductible', 'Collision covers your vehicle when you hit something \u2014 another car, a pole, a guardrail. Lenders usually require it on financed cars. Weigh the premium against the car\u2019s value on older vehicles.'],
['Comprehensive coverage', 'Pays for non-collision damage: theft, hail, flood, fire, falling objects, animal strikes', 'Comprehensive handles the \u201cacts of nature and mischief\u201d side of auto risk. Like collision, it carries a deductible and is typically required by lenders.'],
['Uninsured/underinsured motorist coverage', 'Protects you when the at-fault driver has too little or no insurance', 'If a hit-and-run or uninsured driver injures you, this coverage steps in for medical bills and sometimes property damage. In many states a meaningful share of drivers carry no insurance, making this coverage cheap protection.'],
['Homeowners insurance (HO-3)', 'Covers the dwelling, other structures, belongings, and liability against named perils', 'The standard HO-3 policy insures the home against all perils except listed exclusions, and belongings against named perils. It includes liability and loss-of-use coverage. Flood and earthquake are typically excluded and need separate policies.'],
['Renters insurance (HO-4)', 'Covers a renter\u2019s belongings and liability; the landlord\u2019s policy does not', 'Renters insurance protects personal property against theft, fire, and other perils, plus liability if someone is injured in your unit. It is inexpensive \u2014 often under twenty dollars a month \u2014 and many landlords require it.'],
['Condo insurance (HO-6)', 'Covers what the condo association\u2019s master policy does not: interiors, belongings, liability', 'The HO-6 \u201cwalls-in\u201d policy covers interior finishes, personal property, and liability, coordinating with the association\u2019s master policy. Read the master policy first to find the gaps.'],
['Flood insurance', 'Covers flood damage excluded from homeowners policies; available via the NFIP and private insurers', 'Standard homeowners insurance excludes flooding. The National Flood Insurance Program sells policies in participating communities, with waiting periods before coverage starts. Even homes outside high-risk zones flood \u2014 a large share of claims come from moderate-risk areas.'],
['Earthquake insurance', 'Covers shaking damage excluded from homeowners policies; high deductibles are typical', 'Earthquake policies carry deductibles as a percentage of the dwelling limit \u2014 often 10\u201320% \u2014 so they suit catastrophic loss, not minor cracks. Availability concentrates in seismic states.'],
['Umbrella insurance', 'Extra liability above auto and home limits, typically in million-dollar increments', 'Umbrella policies add $1M+ of liability protection over underlying auto and homeowners policies, plus broader claims like libel. They are surprisingly affordable for the limits and suit anyone with assets or risk exposure to protect.'],
['Disability insurance (long-term)', 'Replaces income if illness or injury prevents working; your most valuable asset is earning power', 'Long-term disability typically replaces about 60% of income after a waiting period. Employer coverage is a start; private own-occupation policies offer stronger definitions of disability for professionals.'],
['Short-term disability insurance', 'Replaces part of income for weeks to months after illness, injury, or childbirth', 'Short-term disability bridges the gap before long-term coverage begins, often through employers. Benefit periods run from weeks to about a year.'],
['Long-term care insurance', 'Pays for nursing homes, assisted living, and home aides when you cannot perform daily activities', 'Long-term care policies trigger when you need help with activities of daily living or have severe cognitive impairment. Bought in your 50s\u201360s, they protect retirement savings from care costs that can exceed six figures yearly.'],
['Pet insurance', 'Reimburses veterinary costs for accidents and illness, minus deductible and copay', 'Pet policies typically reimburse 70\u201390% of covered vet bills after a deductible. Accident-only plans cost less; comprehensive plans cover illness too. Pre-existing conditions are generally excluded.'],
['Travel insurance', 'Covers trip cancellation, medical emergencies abroad, and lost baggage', 'Travel policies bundle cancellation (reimbursing prepaid costs), emergency medical (vital where your health plan doesn\u2019t reach), and baggage coverage. Buy soon after booking for full cancellation benefits.'],
['Life insurance for business: key person', 'Protects a company against the death of a critical employee or founder', 'Key-person policies pay the business, funding the search for a replacement and cushioning lost revenue. Buy-sell agreements often pair with life insurance to fund ownership transfers.'],
['Professional liability (E&O)', 'Covers claims that your professional work caused financial harm', 'Errors-and-omissions policies protect consultants, agents, designers, and other professionals against negligence claims. Many contracts require it.'],
['General business liability', 'Covers third-party injury, property damage, and advertising injury for businesses', 'Commercial general liability is the baseline business policy, often bundled with property coverage in a Business Owner\u2019s Policy (BOP).'],
['Workers\u2019 compensation', 'Pays medical costs and lost wages for work injuries; required in most states', 'Workers\u2019 comp is no-fault: injured employees get care and wage replacement without suing. Employers in most states must carry it, with rates varying by industry risk.'],
['Cyber liability insurance', 'Covers data breaches, ransomware, and digital liability', 'Cyber policies fund breach response \u2014 forensics, notification, credit monitoring \u2014 plus liability and business interruption. Insurers increasingly require baseline security controls.'],
['Title insurance', 'Protects against ownership disputes and liens on real estate', 'A one-time premium at purchase insures against hidden title defects \u2014 old liens, recording errors, undisclosed heirs. Lenders require a lender\u2019s policy; owners should buy their own.'],
['Mortgage insurance (PMI)', 'Protects the lender \u2014 not you \u2014 when down payments are small', 'Private mortgage insurance lets buyers purchase with less than 20% down by insuring the lender against default. It drops off once equity thresholds are met; FHA loans use their own mortgage insurance premiums.'],
['Annuities', 'Contracts converting a lump sum into guaranteed income streams', 'Fixed, variable, and indexed annuities trade a lump sum for income, often for life. They insure against outliving savings \u2014 longevity insurance \u2014 but fees and complexity demand careful comparison.']
];
var REAL_TERMS = [
['Premium', 'The price of insurance, paid monthly, quarterly, or annually', 'The premium is what you pay the insurer to keep coverage in force. It reflects risk, coverage limits, deductibles, and discounts. Missing payments can lapse the policy.'],
['Deductible', 'What you pay out of pocket before insurance starts paying', 'A $1,000 deductible means you cover the first $1,000 of a covered loss. Higher deductibles lower premiums \u2014 a direct trade of risk for price. Choose a deductible you could actually pay tomorrow.'],
['Copayment (copay)', 'A fixed fee per service, common in health insurance', 'A copay is the flat amount you pay for a doctor visit or prescription \u2014 say $25 \u2014 with insurance covering the rest of the allowed amount.'],
['Coinsurance', 'Your percentage share of costs after the deductible', '80/20 coinsurance means insurance pays 80% and you pay 20% of covered costs after the deductible, until you hit the out-of-pocket maximum.'],
['Out-of-pocket maximum', 'The most you pay in a plan year; then insurance pays 100%', 'Once deductibles, copays, and coinsurance total the out-of-pocket max, the plan pays all covered costs for the rest of the year. It is the true worst-case number of a health plan.'],
['Coverage limit', 'The maximum the insurer will pay', 'Limits cap payouts per occurrence, per person, or per policy period. Underinsuring saves premium but leaves the rest of a big loss on you.'],
['Exclusion', 'What the policy does not cover, listed explicitly', 'Exclusions define the policy\u2019s boundaries \u2014 floods in homeowners, cosmetic surgery in health plans. Read them before you need them.'],
['Rider / endorsement', 'An add-on modifying coverage', 'Riders customize policies: a scheduled-jewelry rider, a waiver-of-premium rider, an inflation-guard rider. They cost extra and close specific gaps.'],
['Beneficiary', 'Who receives the payout', 'Beneficiaries get the death benefit or proceeds. Name primary and contingent beneficiaries and review them after marriages, divorces, and births \u2014 beneficiary designations override wills.'],
['Claim', 'A formal request for the insurer to pay a covered loss', 'Filing a claim starts the insurer\u2019s duty to investigate and pay covered losses. Prompt, documented claims settle fastest.'],
['Adjuster', 'The insurer\u2019s investigator who evaluates the claim', 'Adjusters inspect damage, review coverage, and recommend payment. You may also hire a public adjuster to advocate for you on large claims.'],
['Underwriting', 'How insurers evaluate risk and set price', 'Underwriters review applications, inspections, and data to decide whether to insure you and at what price. Better risk profiles earn better rates.'],
['Actuarial science', 'The math of risk: predicting losses across large pools', 'Actuaries use statistics to price policies so premiums cover expected claims plus expenses. Insurance is applied probability at scale.'],
['Risk pool', 'The group whose premiums fund one another\u2019s claims', 'Insurance works because many pay in while few claim at once. Bigger, more diverse pools are more stable \u2014 which is why mandates and auto-enrollment matter.'],
['Grace period', 'Extra days to pay before coverage lapses', 'Most policies give 30 days (often 31 for life insurance) to catch up on premiums. Pay within the grace period and coverage continues uninterrupted.'],
['Lapse', 'Coverage ending for nonpayment', 'A lapsed policy pays nothing. Some life policies can be reinstated within a window by paying back premiums and proving insurability.'],
['Cash value', 'The savings component inside permanent life insurance', 'Part of each permanent-life premium builds cash value that grows tax-deferred. You can borrow against it or surrender the policy for it \u2014 usually with consequences.'],
['Death benefit (face amount)', 'What the life policy pays beneficiaries', 'The face amount is the headline number \u2014 $500,000 of term, for example. Loans against cash value can reduce what beneficiaries receive.'],
['Peril', 'A specific cause of loss, like fire or theft', 'Policies list covered perils (named-peril) or cover everything except exclusions (open-peril). Know which kind you hold.'],
['Indemnity', 'Restoring you to the pre-loss financial position \u2014 no more', 'Insurance indemnifies; it does not enrich. You cannot profit from a claim, and insurers may only pay actual loss.'],
['Subrogation', 'The insurer\u2019s right to recover from the at-fault party after paying you', 'After paying your claim, your insurer can pursue the responsible party to recover. It is why your rates don\u2019t always rise after a not-at-fault accident.'],
['Declarations page', 'The policy summary: who, what, how much, how long', 'The dec page lists the insured, coverages, limits, deductibles, and term at a glance. Check it every renewal.'],
['Effective date', 'When coverage begins', 'Coverage applies to losses on or after the effective date \u2014 never before, no matter when you applied.'],
['Binder', 'Temporary proof of coverage before the policy issues', 'A binder gives immediate evidence of insurance \u2014 useful at a car dealership or closing table \u2014 until the formal policy arrives.'],
['Cancellation vs nonrenewal', 'Mid-term ending vs end-of-term refusal to continue', 'Cancellation ends a policy mid-term (with notice and reason); nonrenewal means the insurer declines the next term. Both trigger shop-around time.'],
['HMO', 'Health plan with a primary-care gatekeeper and a closed network', 'HMOs charge lower premiums but require referrals and cover only in-network care (except emergencies).'],
['PPO', 'Health plan with a broad network and out-of-network coverage', 'PPOs cost more but let you see specialists without referrals and cover out-of-network care at lower rates.'],
['High-deductible health plan (HDHP)', 'Low premiums, high deductible; pairs with a Health Savings Account', 'HDHPs trade premium savings for a high deductible. Paired with an HSA \u2014 triple tax-advantaged \u2014 they suit healthy savers who can fund the account.'],
['Coinsurance vs copay', 'Percentage sharing vs flat fees \u2014 both are cost-sharing, applied differently', 'Copays are flat fees per visit; coinsurance is a percentage of the bill after the deductible. Plans mix both.'],
['Waiting period', 'Time before certain coverages begin', 'Waiting periods \u2014 30 days for flood insurance, months for some dental work \u2014 prevent buying coverage only when loss is imminent.'],
['Pre-existing condition', 'A health issue predating coverage', 'Modern health plans cannot deny or surcharge for pre-existing conditions; other insurance types (pet, some supplemental) still can.']
];
var REAL_GUIDES = [
['How much life insurance do you need?', 'Rules of thumb: 10\u201312x income, plus debts, minus assets; a needs analysis beats any rule', 'Start with the DIME method: Debts, Income replacement (years \u00d7 income), Mortgage, Education. Subtract liquid assets. Then sanity-check affordability \u2014 the best policy is one you keep paying. Revisit after marriages, births, and mortgages.'],
['Choosing a health plan', 'Compare total cost: premium + expected out-of-pocket, not premium alone', 'Estimate your care use for the year. Add each plan\u2019s premium to its likely out-of-pocket costs. Check that your doctors and drugs are covered. The cheapest premium often loses on total cost for regular care users.'],
['Auto insurance limits that make sense', 'State minimums are floors, not recommendations; 100/300/100 is a common sensible baseline', 'Liability limits read as per-person/per-accident/property: 100/300/100 means $100k per person, $300k per accident, $100k property. Match umbrella requirements. Raise deductibles to afford the liability you actually need.'],
['Insuring a new home', 'Insure replacement cost, not market value or purchase price', 'Replacement cost is what rebuilding costs \u2014 often very different from market value. Get an extended-replacement endorsement, document belongings with video, and price flood and earthquake separately.'],
['Renters: what to document', 'A home inventory makes claims fast and full', 'Video every room, narrate valuables, and store the file offsite. Keep receipts for big items. Update yearly. Claims without documentation settle slower and smaller.'],
['Umbrella: who needs it?', 'Assets, income, and risk exposure decide \u2014 not just wealth', 'Own a home, have savings, drive, host guests, own a dog, or have teen drivers? An umbrella\u2019s million-dollar increments are cheap catastrophic-liability protection.'],
['Disability insurance shopping', 'Own-occupation definition, non-cancelable terms, and adequate benefit matter most', 'Prioritize the definition of disability (own-occupation is strongest), then benefit amount (~60% of income), waiting period, and benefit length. Group coverage through work is a foundation, rarely the whole house.'],
['Travel insurance timing', 'Buy within 14\u201321 days of first booking for cancel-for-any-reason options', 'Early purchase unlocks the broadest cancellation benefits and pre-existing condition waivers. Compare medical limits for international trips \u2014 your health plan may not travel with you.'],
['Flood insurance: do you need it?', 'A quarter or more of flood claims come from outside high-risk zones', 'Check your flood map, but remember maps lag development and climate. With a typical 30-day wait, buy before storm season, not during it.'],
['Pet insurance math', 'Compare lifetime premiums against one big emergency', 'A single surgery can cost several thousand dollars. If you couldn\u2019t comfortably cover that, insurance\u2019s monthly cost buys peace of mind \u2014 especially for accident-prone breeds.'],
['Small business insurance stack', 'BOP + workers\u2019 comp + professional liability covers most small firms\u2019 basics', 'Start with a Business Owner\u2019s Policy (property + general liability), add workers\u2019 comp where required, then professional liability or cyber as your exposures dictate. Review yearly as you grow.'],
['Insurance at every life stage', 'Coverage needs evolve: single, married, kids, empty nest, retirement', 'Single: renters + disability. Married: add term life. Kids: raise life and umbrella. Empty nest: shift toward long-term care planning. Annual reviews beat set-and-forget.']
];
var REAL_CLAIMS = [
['Filing an auto claim', 'Safety first, document everything, notify promptly, never admit fault at the scene', 'Move to safety and call 911 if anyone is hurt. Photograph vehicles, plates, and the scene. Exchange information without debating fault. Notify your insurer promptly \u2014 delays complicate claims.'],
['Filing a homeowners claim', 'Mitigate further damage, document the loss, file promptly', 'Stop the bleeding: tarp the roof, shut the water \u2014 insurers require mitigation. Document: photos, video, and a written inventory before cleanup. File: report promptly and keep every receipt; additional living expenses may be covered.'],
['Filing a health insurance claim', 'Most claims file automatically; appeals have deadlines \u2014 calendar them', 'Providers usually bill insurers directly. Review every Explanation of Benefits for errors. If denied, appeal: internal appeal first, then external review. Deadlines are strict \u2014 often 180 days.'],
['What a claims adjuster does', 'Investigates, verifies coverage, estimates damage, and recommends payment', 'The adjuster inspects, interviews, and reviews your documentation against the policy. Cooperate fully but know your rights \u2014 including hiring your own public adjuster on large losses.'],
['Appealing a denied claim', 'Denials can be wrong: request the reason in writing and appeal with evidence', 'Get the denial reason in writing and the policy language cited. Gather counter-evidence: photos, expert opinions, independent estimates. Appeal internally, then to regulators or external review where available.'],
['The appraisal clause', 'A built-in arbitration for disagreements over the amount of loss', 'When you and the insurer disagree on value, the appraisal clause lets each side hire an appraiser, with an umpire deciding. It resolves valuation disputes without lawsuits.'],
['Diminution of value claims', 'Your repaired car is worth less; some states let you claim the difference', 'After a not-at-fault accident, the repaired vehicle\u2019s market value drops. Diminished-value claims seek that difference \u2014 documentation and state law decide.'],
['Claim timelines', 'Insurers must acknowledge, investigate, and decide within regulated timeframes', 'States set deadlines \u2014 often 15 days to acknowledge and 30\u201345 to decide. Track every communication in writing. Unreasonable delay can itself violate insurance regulations.']
];

/* ================= Signature-generation pools ================= */
var GUIDE_TOPICS = [
['Insuring a home-based business','coverage-guide','Your homeowners policy barely covers business gear; a small endorsement or BOP closes the gap.','Inventory: list business equipment and its value. Check: read the homeowners business-property sublimit \u2014 often tiny. Add: a home-business endorsement or small BOP. Review: update as revenue and gear grow.'],
['Insurance for gig workers','coverage-guide','Rideshare, delivery, and freelance work create gaps personal policies don\u2019t cover.','Map the gaps: when are you \u201con the app\u201d vs covered? Add: rideshare endorsements or commercial policies where needed. Protect income: disability matters more when no employer provides it. Document: mileage and earnings logs support claims.'],
['Insuring a classic car','coverage-guide','Agreed-value coverage protects classics that standard policies undervalue.','Value: get a professional appraisal. Cover: agreed-value or stated-value policies, not actual cash value. Limit use: pleasure-use terms keep premiums sane. Store: garaging requirements are real \u2014 honor them.'],
['Insurance for landlords','coverage-guide','A dwelling-fire policy plus liability and loss-of-rents beats a homeowners policy.','Convert: homeowners won\u2019t cover rentals \u2014 switch to dwelling fire (DP-3). Add: liability and loss-of-rental-income coverage. Require: tenant renters insurance in the lease. Umbrella: layer it over everything.'],
['Insuring a wedding','coverage-guide','Event insurance covers the deposits and disasters, not the cold feet.','Cover: cancellation/postponement for venue and vendor failure. Add: liability if the venue requires it. Time: buy when deposits go down. Read: communicable-disease and weather terms vary.'],
['Cyber hygiene for lower cyber premiums','coverage-guide','Insurers discount cyber policies for MFA, backups, and patching.','Enforce MFA everywhere. Back up immutably and test restores. Patch on schedule. Train against phishing \u2014 then document it all for the underwriter.'],
['Insuring a new teen driver','coverage-guide','Teens spike premiums; good-student and telematics discounts blunt the blow.','Shop: compare before adding the teen. Discount: good-student, driver\u2019s-ed, and telematics programs. Choose: liability-first on older cars; full coverage on the new one. Coach: the real risk reducer is supervised practice.'],
['Flood prep for renters','coverage-guide','Renters can buy contents-only flood insurance cheaply.','Know: your landlord\u2019s policy covers the building, not your stuff. Buy: NFIP contents policies for renters are inexpensive. Document: inventory before storm season. Elevate: keep valuables off the floor in flood zones.'],
['Insurance for a food truck','coverage-guide','A food truck needs commercial auto, general liability, and spoilage coverage.','Auto: commercial auto for the truck itself. Liability: general liability for customers. Spoilage: coverage for inventory lost to breakdown. Events: certificates of insurance for every festival.'],
['Insuring expensive jewelry','coverage-guide','A scheduled personal-property rider covers what homeowners sublimits won\u2019t.','Appraise: current retail replacement value. Schedule: list each piece on a rider. Cover: mysterious disappearance, not just theft. Update: reappraise every few years.'],
['Disability insurance for freelancers','coverage-guide','No employer plan means building your own safety net.','Buy: private long-term disability with own-occupation terms. Fund: an emergency reserve covering the waiting period. Layer: business-overhead policies protect the practice too. Review: raise benefits as income grows.'],
['Insuring a short-term rental','coverage-guide','Airbnb-style hosting needs commercial or STR-specific coverage.','Disclose: tell your insurer \u2014 undisclosed STR use can void claims. Add: STR endorsements or commercial policies. Require: guest damage deposits and house rules. Umbrella: raise liability for guest injuries.'],
['Pet insurance for exotic pets','coverage-guide','Birds and reptiles need specialty exotic-pet policies.','Find: few insurers cover exotics \u2014 specialty carriers do. Compare: accident vs illness coverage and exclusions. Budget: exotic vet care runs high; price accordingly. Document: health records from acquisition.'],
['Insurance after a claim','coverage-guide','A claim changes your profile; shop strategically at renewal.','Understand: surcharges typically last 3\u20135 years. Shop: compare before renewal \u2014 loyalty rarely pays. Mitigate: fix the underlying risk (alarm, roof). Ask: about accident-forgiveness and diminishing deductibles.'],
['Coordinating two health plans','coverage-guide','Dual coverage has a coordination-of-benefits order that decides who pays first.','Order: the birthday rule usually decides primary for kids. File: bill primary first, then secondary. Watch: secondary rarely pays what primary didn\u2019t \u2014 do the math before paying two premiums.'],
['Insurance for a nonprofit','coverage-guide','Nonprofits need D&O, general liability, and volunteer coverage.','Directors: D&O protects board members personally. Events: special-event liability for fundraisers. Volunteers: volunteer accident policies fill workers\u2019-comp gaps. Review: yearly with growth.']
];
var TERM_TOPICS = [
['Actual cash value vs replacement cost','policy-term','ACV subtracts depreciation; replacement cost pays to rebuild or replace new.','ACV: pays what the item was worth used. Replacement: pays what new costs. Premium: replacement costs more and pays more. Choose: replacement for homes; ACV can suit older cars.'],
['Occurrence vs claims-made','policy-term','Occurrence covers incidents during the term; claims-made covers claims filed during the term.','Occurrence: the incident date rules \u2014 simpler. Claims-made: needs continuous coverage plus tail. Watch: switching claims-made carriers needs tail coverage.'],
['Scheduled vs unscheduled property','policy-term','Scheduled items are listed and fully covered; unscheduled falls under blanket limits.','Schedule: jewelry, art, and instruments by appraisal. Blanket: everything else under the contents limit. Gap: blanket sublimits for valuables are low \u2014 schedule the treasures.'],
['Primary vs excess coverage','policy-term','Primary pays first; excess pays after primary exhausts.','Layer: auto/home are primary; umbrella is excess. Coordinate: excess requires minimum underlying limits. Mind: gaps between layers are your problem.'],
['Admitted vs non-admitted insurers','policy-term','Admitted carriers are state-licensed and guaranty-backed; non-admitted (surplus lines) cover unusual risks.','Standard: admitted for ordinary needs. Surplus: for hard-to-place risks. Backstop: guaranty funds protect admitted policyholders if carriers fail.'],
['Captive insurance','policy-term','Large companies insure themselves through their own licensed insurer.','Form: a licensed subsidiary writes the parent\u2019s coverage. Why: control, cost, and access to reinsurance. Scale: only viable for large, sophisticated risk portfolios.'],
['Reinsurance','policy-term','Insurance for insurers: spreading catastrophic risk globally.','Cede: primary insurers pass chunks of risk to reinsurers. Protect: against hurricanes, earthquakes, and pandemics. Price: reinsurance costs flow into your premiums.'],
['Risk retention groups','policy-term','Liability insurers owned by their members in an industry.','Join: professionals in one field pool liability risk. Benefit: tailored coverage and potential dividends. Limit: liability lines only, by federal law.'],
['Self-insured retention','policy-term','Like a deductible, but you handle claims below it yourself.','Set: the amount you pay per claim before coverage. Manage: you adjust small claims in-house. Suit: large organizations with steady cash flow.'],
['Experience modification factor','policy-term','Your workers\u2019-comp premium modifier based on claim history.','Compute: past claims vs expected for your industry. Improve: safety programs lower the mod over time. Shop: a high mod follows you between carriers.']
];
var SCENARIOS = [
['The fender-bender with an uninsured driver','claims-process','A hit-and-run tests your uninsured-motorist coverage.','Call police and file a report \u2014 hit-and-run needs documentation. Notify your insurer and invoke uninsured-motorist coverage. Document injuries promptly; some appear days later. Track every medical visit for the claim file.'],
['The burst pipe at 2 a.m.','claims-process','A water loss tests your mitigation duties and documentation.','Shut the water main immediately. Call a plumber and a mitigation company \u2014 insurers require prompt mitigation. Photograph everything before cleanup. Keep every receipt; emergency repairs are covered when reasonable.'],
['The denied health claim','claims-process','A $4,000 bill denied as \u201cnot medically necessary.\u201d','Request the denial in writing with the exact policy language. Ask the provider for a letter of medical necessity. File the internal appeal before the deadline. Escalate to external review if denied again.'],
['The totaled car valuation fight','claims-process','The insurer\u2019s total-loss offer is $3,000 below market.','Pull comparable listings for your exact trim and mileage. Present the comps in writing with a counter-offer. Invoke the appraisal clause if talks stall. Never accept the first offer reflexively.'],
['The roof claim after hail','claims-process','A storm damages the roof; the adjuster\u2019s scope looks thin.','Get a contractor\u2019s inspection and written scope first. Meet the adjuster on the roof with your contractor present. Compare line items, not just totals. Supplement: legitimate missed items can be added.'],
['The stolen laptop with client data','claims-process','Theft plus a potential cyber incident in one event.','File a police report immediately. Notify your cyber carrier as well as property \u2014 breach duties have clocks. Preserve evidence: don\u2019t wipe the backup. Document the hardware value and the data response costs separately.'],
['The contractor who damaged the kitchen','claims-process','A renovation gone wrong: whose insurance pays?','Document the damage before anyone repairs it. Demand the contractor\u2019s certificate of insurance. File with their general liability carrier first. Your homeowners may cover gaps \u2014 with your deductible.'],
['The dog bite liability claim','claims-process','Your dog injures a guest; liability and medical payments respond.','Get the person medical care immediately. Report to your homeowners insurer \u2014 don\u2019t promise payments yourself. Know your breed and bite-history exclusions. Consider an umbrella before the next incident.'],
['The travel cancellation','claims-process','A hurricane warning scuttles the prepaid trip.','Read the policy\u2019s covered reasons \u2014 warnings vs watches matter. Gather proof: bookings, receipts, and the official warning. File promptly with complete documentation. Appeal with the warning text if initially denied.'],
['The disability claim paperwork','claims-process','A back injury keeps you out of work; the claim needs airtight records.','File within days \u2014 late filing invites denial. Get the physician\u2019s statement detailed and consistent. Keep a symptom and treatment diary. Respond to every insurer request before deadlines.']
];
var TYPE_CONCEPTS = [
['Parametric heat-wave coverage','insurance-type','Pays a fixed benefit when temperatures exceed a threshold for set days \u2014 no adjuster visit.','Trigger: satellite-verified heat index over the threshold. Payout: fixed sums per qualifying day, fast. Use: outdoor workers, event vendors, and cities funding cooling centers. Note: a concept sketch, not a marketed product.'],
['Creator income protection','insurance-type','Disability-style income protection designed for freelancers and creators.','Cover: own-occupation disability plus platform-demonetization riders. Benefit: a percentage of documented average income. Waiting: 90-day elimination keeps premiums reachable. Note: a concept sketch, not a marketed product.'],
['Parametric flight-delay coverage','insurance-type','Automatic payout when your flight is delayed past a set threshold.','Trigger: official flight-status data feeds. Payout: fixed sums at 2, 4, and 6+ hours. Buy: bundled at booking or standalone. Note: a concept sketch, not a marketed product.'],
['Community solar performance insurance','insurance-type','Guarantees minimum output for shared solar arrays.','Cover: shortfalls below modeled generation. Term: aligned to financing horizons. Data: production meters settle claims automatically. Note: a concept sketch, not a marketed product.'],
['Cyber-bullying response coverage','insurance-type','Funds crisis response for severe online harassment of minors.','Cover: digital forensics, takedown services, and counseling. Trigger: documented severe incidents. Limit: annual aggregate per family. Note: a concept sketch, not a marketed product.'],
['Home battery backup insurance','insurance-type','Covers spoilage and hotel costs during extended outages for battery owners.','Cover: food spoilage and alternative lodging past 24 hours. Proof: battery telemetry plus outage maps. Pair: sold alongside battery installs. Note: a concept sketch, not a marketed product.'],
['Gig-platform liability top-up','insurance-type','Extra liability for gig workers between platform coverage windows.','Cover: the gaps when the app is on but no job is active. Limit: $1M per occurrence. Price: pay-per-active-hour. Note: a concept sketch, not a marketed product.'],
['Parametric rainfall insurance for farms','insurance-type','Pays when rainfall at the nearest station misses the band the crop needs.','Trigger: station data vs the policy\u2019s rainfall band. Speed: payouts in days, not months. Basis risk: your field may differ from the station \u2014 the known trade-off. Note: a concept sketch, not a marketed product.'],
['Elder-care navigation benefit','insurance-type','Funds a professional care navigator plus respite hours when care needs begin.','Trigger: assessment of daily-living needs. Benefit: navigator hours plus a respite budget. Goal: better decisions, less family burnout. Note: a concept sketch, not a marketed product.'],
['E-bike theft and damage coverage','insurance-type','Scheduled coverage for high-value e-bikes that homeowners sublimits ignore.','Cover: theft, crash damage, and battery fire. Require: quality lock standards. Price: a fraction of the bike yearly. Note: a concept sketch, not a marketed product.']
];
var REAL = interleave([
  REAL_TYPES.map(function (e) { return { k: 't', e: e }; }),
  REAL_TERMS.map(function (e) { return { k: 'm', e: e }; }),
  REAL_GUIDES.map(function (e) { return { k: 'g', e: e }; }),
  REAL_CLAIMS.map(function (e) { return { k: 'c', e: e }; })
]);
function realRecord(e, id, seed, cat) {
  var secs = [
    { heading: 'Key points', body: e[0] + '. ' + e[1] + '.' },
    { heading: 'In depth', body: e[2] + ' Educational content only \u2014 not financial advice. Consult a licensed insurance professional for your situation.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: e[0], category: cat, record_kind: RECORD_KIND, origin: 'sourced', summary: e[1] + '.', details: { key_points: e[1].split('; ') }, sections: secs, record_text: text, source_note: 'Sourced: standard insurance knowledge; educational only, not financial advice.', related: [], _seed: seed };
}
function sigGuide(r, id, seed, topic) {
  var t = topic || pick(GUIDE_TOPICS, r);
  var secs = [
    { heading: 'The guide', body: t[0] + ' (' + t[1] + '). ' + t[2] },
    { heading: 'Steps', body: t[3] },
    { heading: 'Keep in mind', body: 'Insurance rules vary by state and country, and products change yearly. Use this guide to ask sharper questions \u2014 then verify specifics with a licensed professional. Educational content only, not financial advice.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature guide', category: t[1], record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { area: t[1], key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown coverage guide; educational only.', related: [], _seed: seed };
}
function sigTerm(r, id, seed, topic) {
  var t = topic || pick(TERM_TOPICS, r);
  var secs = [
    { heading: 'The term', body: t[0] + '. ' + t[1] },
    { heading: 'In practice', body: t[2] },
    { heading: 'Why it matters', body: 'Insurance vocabulary is the fine print made readable: knowing the term lets you compare policies on equal footing and spot what a quote is really offering. When in doubt, ask the agent to define it in writing.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature explainer', category: 'policy-term', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[1], details: { area: 'policy-term' }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown glossary explainer; educational only.', related: [], _seed: seed };
}
function sigScenario(r, id, seed, topic) {
  var t = topic || pick(SCENARIOS, r);
  var secs = [
    { heading: 'The scenario', body: t[0] + ' (' + t[1] + '). ' + t[2] },
    { heading: 'Working it', body: t[3] },
    { heading: 'Lesson', body: 'Every scenario here is a rehearsal: the households that fare best are the ones that read their policies before the loss, not after.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature walkthrough', category: t[1], record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { area: t[1] }, sections: secs, record_text: text, source_note: 'Signature-generated: a homegrown claims walkthrough; educational only.', related: [], _seed: seed };
}
function sigType(r, id, seed, topic) {
  var t = topic || pick(TYPE_CONCEPTS, r);
  var secs = [
    { heading: 'CONCEPT \u2014 not a marketed product', body: t[0] + '. ' + t[2] },
    { heading: 'How it would work', body: t[3] },
    { heading: 'Keep in mind', body: 'This is a Signature concept sketch for exploring coverage ideas \u2014 not a real policy you can buy. Educational content only, not financial advice.' }
  ];
  var text = secs.map(function (s) { return s.heading + '.\n' + s.body; }).join('\n\n');
  return { id: id, title: t[0] + ' \u2014 Signature concept', category: 'insurance-type', record_kind: RECORD_KIND, origin: 'signature-generated', summary: t[2], details: { key_points: t[2].split('. ') }, sections: secs, record_text: text, source_note: 'Signature-generated concept sketch; not a real insurance product.', related: [], _seed: seed };
}
var CATMAP = { t: 'insurance-type', m: 'policy-term', g: 'coverage-guide', c: 'claims-process' };
function generate(seed, opts, rnd) {
  opts = opts || {}; rnd = rnd || prng(seed);
  var idx = ((seed % 1000000) + 1000000) % 1000000;
  var id = PREFIX + String(idx + 1).padStart(7, '0');
  if (idx < REAL.length) {
    var re = REAL[idx];
    if (!opts.category || CATMAP[re.k] === opts.category) return realRecord(re.e, id, seed, CATMAP[re.k]);
  }
  var cat = opts.category || pick(CATS, rnd);
  if (cat === 'insurance-type') return sigType(rnd, id, seed);
  if (cat === 'coverage-guide') { var p1 = GUIDE_TOPICS.filter(function (x) { return x[1] === 'coverage-guide'; }); return sigGuide(rnd, id, seed, pick(p1, rnd)); }
  if (cat === 'policy-term') return sigTerm(rnd, id, seed);
  var p3 = SCENARIOS.filter(function (x) { return x[1] === 'claims-process'; });
  return sigScenario(rnd, id, seed, pick(p3, rnd));
}
var REQUIRED = ['id', 'title', 'category', 'record_kind', 'origin', 'summary', 'details', 'sections', 'record_text', 'source_note'];
function validate(rec) {
  var errors = [];
  if (!rec || typeof rec !== 'object') return { ok: false, errors: ['not an object'] };
  REQUIRED.forEach(function (k) { if (rec[k] === undefined || rec[k] === null || rec[k] === '') errors.push('missing ' + k); });
  if (rec.id && !/^JAH-INS-\d{7}$/.test(rec.id)) errors.push('bad id format');
  if (rec.category && CATS.indexOf(rec.category) < 0) errors.push('bad category');
  if (rec.origin && ['sourced', 'signature-generated'].indexOf(rec.origin) < 0) errors.push('bad origin');
  if (rec.sections && (!Array.isArray(rec.sections) || !rec.sections.length)) errors.push('sections empty');
  if (rec.record_text && rec.record_text.length < 120) errors.push('record_text too short');
  return { ok: errors.length === 0, errors: errors };
}
function driftCheck(rec, sample) {
  var errors = [];
  for (var i = 0; i < sample.length; i++) {
    if (sample[i] && sample[i].t === rec.title && sample[i].id !== rec.id) { errors.push('duplicate title in archive sample'); break; }
  }
  return { ok: errors.length === 0, errors: errors };
}
var GEN = { version: VERSION, generate: generate, validate: validate, driftCheck: driftCheck, slug: SLUG, prefix: PREFIX, categories: CATS, record_kind: RECORD_KIND, realCount: REAL.length };
if (typeof JAHDB !== 'undefined' && JAHDB.registerGenerator) JAHDB.registerGenerator(SLUG, GEN);
if (typeof module !== 'undefined' && module.exports) module.exports = GEN;
})();
