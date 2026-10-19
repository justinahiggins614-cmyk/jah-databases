#!/usr/bin/env python3
"""Dataset Acquisition Licensing entries 13-24 (compounded)."""

APPEND = [
dict(
name="License Terms Anatomy",
group="Terms and Renewal", ladder_rank=13, ladder_tier="compounded",
description="""Every license, open or proprietary, is dissected the same way: the grant (what rights are given - use, reproduce, distribute, derive, publicly display?), the scope (who may exercise them - which entities, users, geographies?), the conditions (attribution? share-alike? non-commercial? notice?), the term (how long? perpetual? subscription?), the fees (what cost? what overages?), the warranties (does the licensor warrant anything about the data?), the liability (caps? indemnification?), and termination (what ends it? what survives?). The anatomy turns legalese into checkable structure: the rights model records each element as data, enabling uniform compliance queries (show me all licenses permitting redistribution) and conflict detection (this license forbids what that one requires). Term extraction is legal work assisted by tooling: clause libraries recognize standard language, lawyers confirm the edge cases. The anatomy versions with the license - amendments re-extracted, never hand-edited over.""",
how_it_works="""Legal extraction maps each license to the anatomy: grant, scope, conditions, term, fees, warranties, liability, termination. Clause libraries assist with standard language; lawyers confirm edge cases. The rights model stores the anatomy as data enabling uniform queries and conflict detection. Amendments trigger re-extraction with versioning. Compliance checks query the model: permitted uses per dataset per purpose.""",
key_points=[
 "Anatomy: grant, scope, conditions, term, fees, warranties, liability, termination.",
 "Turns legalese into checkable structured data.",
 "Enables uniform compliance queries and conflict detection.",
 "Extraction assisted by clause libraries, confirmed by lawyers.",
 "Amendments re-extracted with versioning."],
requirements=[
 "License anatomy extraction per license.",
 "Standard rights model storage.",
 "Compliance querying against the model.",
 "Amendment re-extraction with versioning."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Creative Commons. License suite documentation."],
sig_lens="""The Signature reading: license anatomy is the registry's dissection of every charter - grant, scope, conditions, term, each element laid bare as data. The Signature anatomist's tables let any use be checked against any charter.""",
demo_data={"licenses":[
 {"name":"anatomy-ok","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"anatomy-nc","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Attribution Requirements",
group="Terms and Renewal", ladder_rank=14, ladder_tier="compounded",
description="""Attribution is the price of open data: credit the source as the license requires - typically title, author, source link, and license with link (TASL). The requirements vary: CC BY wants reasonable attribution; ODbL wants attribution on produced works; government licenses want source acknowledgment; some require attribution in specific forms (the map tile's corner credit). Implementation weaves attribution through products: about pages listing sources with links, metadata embedded in datasets, credits in publications and models' documentation. The common failures are attribution erosion: the dataset reused three times downstream with the credit dropped at each hop - solved by attribution metadata traveling with the data. Attribution stacking is the scaling problem: a product built on fifty sources needs fifty credits - managed by consolidated attribution pages, not fifty footnotes. Compliance audits verify attribution renders where the license requires; missing attribution is a license breach like any other.""",
how_it_works="""Attribution requirements extracted per license (TASL elements, specific forms). Products implement attribution pages, embedded metadata, and documentation credits. Attribution metadata travels with datasets through pipelines preventing erosion. Consolidated pages handle stacking. Audits verify rendering per license; gaps remediate. License changes re-verify attribution requirements.""",
key_points=[
 "Attribution typically: title, author, source, license (TASL).",
 "Woven through products: about pages, embedded metadata, documentation.",
 "Attribution metadata travels with data preventing erosion downstream.",
 "Stacking managed via consolidated attribution pages.",
 "Missing attribution is a license breach - audited like any term."],
requirements=[
 "Per-license attribution requirement extraction.",
 "Attribution implementation in products and metadata.",
 "Traveling attribution metadata.",
 "Attribution audits with remediation."],
standards=[
 "Creative Commons attribution guidance."],
citations=[
 "Creative Commons. Best practices for attribution.",
 "Open Data Commons. ODbL 1.0."],
sig_lens="""The Signature reading: attribution is the honest debt paid to every source - credited by name, carried through every reuse. The Signature debtor's credits travel with the goods and are audited like coin.""",
demo_data={"licenses":[
 {"name":"attr-cc-by","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"attr-odbl","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Share-Alike Obligations",
group="Terms and Renewal", ladder_rank=15, ladder_tier="compounded",
description="""Share-alike (copyleft) obligates derivatives to carry the same freedoms: adapt CC BY-SA data and the adaptation must be BY-SA; build on ODbL data and the produced database must be ODbL. The obligation's boundaries matter: what counts as a derivative (the adapted dataset yes; the collective work merely aggregating it, maybe not - the license texts define), and how far it travels (the produced work from the database, not necessarily the application built on top - ODbL's produced-work distinction). Share-alike creates the license compatibility puzzle: BY-SA derivatives cannot add NC restrictions, ODbL data cannot mix with proprietary data in one database. The compliance program tracks share-alike chains: every derivative records its source licenses, and the chain is verified before publication - because publishing a proprietary product on share-alike data is the expensive mistake. Some organizations avoid share-alike data for commercial products entirely; others embrace it with clean separation architectures.""",
how_it_works="""Share-alike obligations identified per source license with boundary analysis (derivative vs collective, produced work scope). Derivative tracking records source licenses per derived dataset forming chains. Pre-publication verification checks chain compatibility against the product's licensing. Separation architectures isolate share-alike data where commercial products must stay proprietary. Legal review covers boundary ambiguities.""",
key_points=[
 "Share-alike: derivatives must carry the same license freedoms.",
 "Boundaries: derivative vs collective, produced-work scope - defined per license.",
 "Creates compatibility puzzles: SA cannot mix with NC or proprietary.",
 "Chains tracked per derivative; verified before publication.",
 "Avoid or architecturally separate for commercial products."],
requirements=[
 "Share-alike identification with boundary analysis.",
 "Derivative chain tracking.",
 "Pre-publication compatibility verification.",
 "Separation architectures where needed."],
standards=[
 "CC BY-SA 4.0; ODbL 1.0."],
citations=[
 "Creative Commons. CC BY-SA 4.0 legal code.",
 "Open Data Commons. ODbL 1.0."],
sig_lens="""The Signature reading: share-alike is the commons' covenant of return - improvements given back as freely as received, the chain unbroken. The Signature keeper tracks every link and never breaks the chain for profit.""",
demo_data={"licenses":[
 {"name":"sa-data","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"sa-mixed","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Redistribution Rights",
group="Terms and Renewal", ladder_rank=16, ladder_tier="compounded",
description="""Redistribution rights decide whether acquired data may be passed on: to customers in products, to partners in feeds, to the public in open datasets. The spectrum: full redistribution permitted (CC0, CC BY, ODC-By), redistribution with conditions (share-alike, attribution), redistribution prohibited (most proprietary vendor licenses - use it, do not resell it), and redistribution of derivatives only (use the vendor's data to build your product, but do not resell the raw feed). The business impact is direct: a product built on non-redistributable data cannot ship that data to customers - the architecture must separate licensed inputs from shippable outputs. Compliance verifies redistribution paths: every outbound data flow checked against the source licenses' redistribution terms. Violations are among the costliest license breaches - vendors audit redistribution aggressively. The registry models redistribution per license as a structured right (allowed, conditional, prohibited, derivatives-only) enabling mechanical checks on every outbound flow.""",
how_it_works="""Redistribution rights modeled per license in the rights model. Architecture separates licensed inputs from shippable outputs where redistribution is limited. Outbound flow checks verify against source licenses mechanically. Vendor audits supported with redistribution evidence. Violations remediated with legal involvement; repeated violations trigger source replacement.""",
key_points=[
 "Spectrum: full, conditional, prohibited, derivatives-only redistribution.",
 "Non-redistributable inputs cannot ship to customers - architect separation.",
 "Every outbound flow checked against source licenses mechanically.",
 "Vendors audit redistribution aggressively; violations are costly.",
 "Rights modeled structurally enabling mechanical checks."],
requirements=[
 "Redistribution rights in the license rights model.",
 "Architectural separation of licensed inputs.",
 "Mechanical outbound flow verification.",
 "Audit evidence for vendor reviews."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Creative Commons. License suite documentation."],
sig_lens="""The Signature reading: redistribution rights are the charters' rules of resale - what may pass onward, under what conditions, what must stay. The Signature merchant checks every outbound cargo against its charters.""",
demo_data={"licenses":[
 {"name":"redist-ok","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"redist-no","commercial":True,"redistribute":False,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Derivative Works Rights",
group="Terms and Renewal", ladder_rank=17, ladder_tier="compounded",
description="""Derivative rights govern what may be built from licensed data: cleaned versions, enriched merges, aggregated summaries, trained models. The license spectrum: full derivative rights (most open licenses, many vendor licenses for internal use), derivatives permitted but not redistributable (build your product's intelligence, keep the raw data home), derivatives restricted (no modification - use as-is), and model-training as a special derivative (some licenses explicitly permit or forbid ML training - the frontier of licensing disputes). The derivative chain matters for compliance: each transformation should record its source licenses, because the derivative's permitted uses are the intersection of its sources' rights. Model training deserves special attention: training on licensed data creates models whose weights may be considered derivatives - the license's derivative terms apply, and vendors increasingly price training rights separately. The program's rule: know the derivative rights before building, not after.""",
how_it_works="""Derivative rights extracted per license including model-training positions. Build planning verifies rights before construction. Derivative chains record source licenses per transformation; permitted uses computed as the intersection. Model training gets explicit rights verification with vendor pricing where applicable. Publication checks verify derivative compliance. Training-rights monitoring tracks the evolving legal landscape.""",
key_points=[
 "Derivatives: cleaned, enriched, aggregated, trained models - rights vary by license.",
 "Common pattern: build freely, redistribute derivatives only.",
 "Derivative permitted uses are the intersection of sources' rights.",
 "Model training is a special derivative - verify rights explicitly.",
 "Know derivative rights before building, not after."],
requirements=[
 "Derivative rights extraction including training positions.",
 "Pre-build rights verification.",
 "Derivative chain tracking with intersection computation.",
 "Training-rights monitoring."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Creative Commons. License suite documentation."],
sig_lens="""The Signature reading: derivative rights are the charters' rules of making - what may be built, what may travel, what the making owes. The Signature maker checks the charter before the workshop, especially for thinking machines.""",
demo_data={"licenses":[
 {"name":"deriv-ok","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"deriv-internal","commercial":True,"redistribute":False,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Commercial Use Rights",
group="Terms and Renewal", ladder_rank=18, ladder_tier="compounded",
description="""Commercial use rights decide whether licensed data may serve revenue: in products sold, in services charged, in advertising-supported offerings. The NC (non-commercial) licenses forbid it - and NC's boundary is notoriously fuzzy: is the nonprofit's sponsored research commercial? The ad-supported free app? The internal tool at a for-profit company? Conservative programs treat any revenue-adjacent use as commercial and avoid NC data where commercial use is conceivable. Proprietary licenses define commercial rights precisely: which products, what revenue share or fees, what happens at scale. The compliance check runs per use case: this product's revenue model against each source's commercial terms. Mixed commercial/non-commercial sourcing needs architectural separation: the NC data feeds the research prototype, never the production product. Commercial-rights audits verify the separation; violations of NC terms are willful-looking breaches that licensors pursue.""",
how_it_works="""Commercial terms extracted per license with NC boundary guidance. Use-case verification checks each product's revenue model against source terms. Architectural separation isolates NC data from commercial products. Audits verify separation and terms compliance. NC ambiguity resolved conservatively or by legal opinion. License upgrades (NC to commercial terms) negotiated where the data proves valuable.""",
key_points=[
 "NC forbids commercial use; its boundary is fuzzy - treat revenue-adjacent as commercial.",
 "Proprietary licenses define commercial rights precisely per product and scale.",
 "Verify per use case: revenue model against source terms.",
 "Architectural separation keeps NC data out of commercial products.",
 "NC violations look willful; licensors pursue them."],
requirements=[
 "Commercial terms extraction with NC guidance.",
 "Per-use-case commercial verification.",
 "Architectural separation for mixed sourcing.",
 "Commercial-rights audits."],
standards=[
 "Creative Commons NC guidance."],
citations=[
 "Creative Commons. NonCommercial interpretation guidance.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: commercial rights are the charters' rules of profit - what may earn, what may not, the fuzzy borders judged conservatively. The Signature merchant keeps the non-commercial goods out of the market stalls.""",
demo_data={"licenses":[
 {"name":"comm-ok","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"comm-nc","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Renewal Dates and Terms",
group="Terms and Renewal", ladder_rank=19, ladder_tier="compounded",
description="""Renewal dates are the acquisition program's ticking clocks: every subscription license, vendor contract, and API agreement expires, and expiry without renewal means the data stops - or worse, the right to use already-ingested data lapses. The renewal register tracks every date with the terms: auto-renewal clauses, price change caps, notice periods for non-renewal, and what happens to historical data on termination. Renewal workflows start early (180/90/30 days): assess the source's continued fitness and cost, renegotiate inadequate terms, secure budget approval, execute the renewal. Lapsed renewals are incidents: the feed stops, the license's post-termination rights govern already-held data, and emergency re-procurement begins. The registry's renewal discipline is what separates professional acquisition from accidental: no source expires by surprise, no renewal is rubber-stamped without reassessment, and every renewal decision is recorded with its rationale.""",
how_it_works="""The renewal register tracks dates, auto-renewals, price caps, notice periods, post-termination rights. Workflows trigger at 180/90/30 days: fitness reassessment, renegotiation, budget approval, execution. Lapses trigger incident response with post-termination rights analysis. Decisions record with rationale; rubber-stamping is blocked by required reassessment evidence. Calendar integration ensures no date is missed; escalation fires on stalled renewals.""",
key_points=[
 "Every subscription expires; expiry without renewal stops data or lapses rights.",
 "Register tracks dates, auto-renewals, price caps, notice periods, post-termination rights.",
 "Workflows at 180/90/30 days: reassess, renegotiate, approve, execute.",
 "Lapses are incidents with post-termination rights analysis.",
 "No surprise expiries; no rubber-stamped renewals."],
requirements=[
 "Renewal register with full terms per source.",
 "Early renewal workflows with reassessment.",
 "Lapse incident response procedures.",
 "Decision recording with rationale."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: renewals are the registry's ticking clocks - every charter's expiry watched, every renewal earned by reassessment. The Signature steward lets no clock run out unheeded and stamps no renewal unread.""",
demo_data={"licenses":[
 {"name":"renew-ok","commercial":True,"redistribute":True,"expires":"2028-01-01","expected":"ok"},
 {"name":"renew-lapsed","commercial":True,"redistribute":True,"expires":"2021-01-01","expected":"expired"}]},
),
dict(
name="Access Conditions",
group="Terms and Renewal", ladder_rank=20, ladder_tier="compounded",
description="""Access conditions are the practical terms of getting the data: authentication methods, rate limits, quota tiers, allowed client types, geographic restrictions on access, and support channels. Conditions protect the provider's infrastructure and business: the API that allows 1000 requests daily, the feed available only from registered IPs, the premium tier with SLAs versus the free tier best-effort. Compliance implements conditions mechanically: API clients with backoff and quota tracking, IP allow-listing where required, geographic routing respecting access regions. Condition changes (quota reductions, new authentication) are monitored like terms changes - the provider that silently halves quotas breaks integrations as surely as a license change. Access conditions also cover the human side: support SLAs, escalation paths, and status communication. The registry records conditions per source with the integration, so operations knows the rules of each road.""",
how_it_works="""Access conditions recorded per source: auth, limits, quotas, client rules, geo restrictions, support. Integrations implement mechanically with quota tracking and backoff. Condition monitoring watches for changes with re-implementation workflows. Support SLAs tracked; escalations follow the provider's paths. Registry links conditions to integrations for operations reference.""",
key_points=[
 "Conditions: auth, rate limits, quotas, client types, geo restrictions, support.",
 "Implemented mechanically: limiters, quota tracking, allow-listing.",
 "Condition changes monitored like terms changes.",
 "Support SLAs and escalation paths recorded.",
 "Registry links conditions to integrations."],
requirements=[
 "Access condition recording per source.",
 "Mechanical implementation with monitoring.",
 "Change monitoring with re-implementation.",
 "Support tracking per provider."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on API licensing."],
sig_lens="""The Signature reading: access conditions are the road rules of each source - speeds, tolls, permitted vehicles, posted plainly. The Signature traveler obeys every road's rules and watches for changed signs.""",
demo_data={"licenses":[
 {"name":"access-ok","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"access-quota","commercial":True,"redistribute":False,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Rate Limits and Quotas",
group="Registry Operations", ladder_rank=21, ladder_tier="compounded",
description="""Rate limits and quotas are the provider's throttles: N requests per second, M per day, G gigabytes per month - with overage fees or hard stops beyond. Engineering to limits means: client-side throttling (token buckets matching the provider's), quota dashboards with burn-rate alerts, request efficiency (caching, batching, incremental sync instead of full pulls), and prioritization (the critical sync gets quota first). Quota exhaustion is an operational incident with a playbook: shed low-priority load, request temporary increases, fail over to cached or alternative sources. The economics matter: quota tiers price access, and the efficient client buys less quota - engineering efficiency directly reduces acquisition cost. Providers change quotas; monitoring catches it. The registry tracks quota entitlements per source with utilization trends informing tier decisions at renewal.""",
how_it_works="""Quota entitlements recorded per source; clients implement token-bucket throttling matching provider limits. Dashboards track utilization with burn-rate alerts. Efficiency engineering: caching, batching, incremental sync. Exhaustion playbooks: shed load, request increases, failover. Utilization trends inform tier selection at renewal. Provider quota changes monitored with re-engineering as needed.""",
key_points=[
 "Limits: per-second, per-day, per-month - with overage fees or hard stops.",
 "Client-side throttling matching provider limits; quota dashboards with alerts.",
 "Efficiency (caching, batching, incremental) directly reduces cost.",
 "Exhaustion playbooks: shed, request, failover.",
 "Utilization trends inform tier decisions at renewal."],
requirements=[
 "Quota entitlement recording per source.",
 "Client throttling with burn-rate alerting.",
 "Efficiency engineering standards.",
 "Exhaustion playbooks with failover."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Beyer B et al. Site Reliability Engineering. O'Reilly, 2016."],
sig_lens="""The Signature reading: quotas are the measured rations of each road - traveled efficiently, watched closely, never exceeded. The Signature quartermaster rations wisely and buys only the tier the journey needs.""",
demo_data={"licenses":[
 {"name":"quota-ok","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"quota-tight","commercial":True,"redistribute":False,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Cost and Budgeting",
group="Registry Operations", ladder_rank=22, ladder_tier="compounded",
description="""Acquisition budgeting covers the total cost of ownership: license fees, overage charges, integration engineering, ongoing operations, renewal uplifts, and the exit cost if the source is replaced. Budgeting discipline starts with cost visibility: every source's full cost tracked in the registry, allocated to the consuming products. Value assessment weighs cost against the data's contribution: revenue enabled, costs avoided, risks reduced - the sources that cannot show value are renegotiated or retired. Renewal uplifts get special scrutiny: the 20 percent annual increase compounds into a crisis - negotiated caps and competitive alternatives keep pricing honest. Hidden costs get hunted: the free API whose integration took six engineer-months, the cheap feed requiring constant cleansing. Budget reviews compare sources providing similar data; redundancy is either eliminated or justified explicitly. The acquisition budget is managed like any portfolio: diversified, measured, pruned.""",
how_it_works="""Cost tracking per source captures fees, overages, engineering, operations, uplifts. Allocation attributes costs to consuming products. Value assessments weigh contribution against cost on schedule. Renewal negotiations target caps using competitive alternatives. Hidden-cost audits find the expensive free sources. Portfolio reviews compare redundant sources; pruning or explicit justification follows. Budget dashboards show cost per value delivered.""",
key_points=[
 "Total cost: fees, overages, integration, operations, uplifts, exit costs.",
 "Cost visibility per source allocated to consuming products.",
 "Value assessed against contribution; valueless sources renegotiated or retired.",
 "Renewal uplifts scrutinized with caps and alternatives.",
 "Portfolio managed: diversified, measured, pruned."],
requirements=[
 "Full cost tracking per source with product allocation.",
 "Value assessments on schedule.",
 "Renewal uplift controls with competitive leverage.",
 "Portfolio reviews with pruning."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: acquisition budgeting is the quartermaster's ledger - every source's full cost weighed against its worth, uplifts challenged, redundancies pruned. The Signature ledger shows cost per value and tolerates no freeloaders.""",
demo_data={"licenses":[
 {"name":"budget-ok","commercial":True,"redistribute":True,"expires":"2029-01-01","expected":"ok"},
 {"name":"budget-cut","commercial":True,"redistribute":False,"expires":"2029-01-01","expected":"ok"}]},
),
dict(
name="License Compatibility",
group="Registry Operations", ladder_rank=23, ladder_tier="compounded",
description="""License compatibility decides which sources may be combined: the dataset mixing CC BY-SA data with proprietary vendor data is a violation waiting to happen - share-alike demands openness the proprietary license forbids. The compatibility matrix maps license pairs to verdicts: compatible (combine freely), compatible-with-conditions (combine with attribution stacking), incompatible (do not combine). The analysis runs per combination, not per source: each derived dataset's source set is checked as a whole. Common incompatibilities: copyleft with proprietary, NC with commercial products, conflicting attribution requirements, and jurisdiction-specific database rights. The compliance workflow checks compatibility at build planning (before the combination exists) and at publication (before the product ships). Incompatibilities resolve by substitution (find a compatibly licensed alternative), separation (keep the incompatible sources in separate products), or re-licensing (negotiate compatible terms). The registry's compatibility engine makes the check mechanical.""",
how_it_works="""The compatibility matrix encodes pair verdicts with conditions. Build planning submits source sets for compatibility checking before construction. Publication re-verifies. Incompatibilities resolve via substitution, separation, or re-licensing with legal involvement. The engine versions with license updates; new licenses enter the matrix through legal analysis. Combination records persist with their compatibility verdicts.""",
key_points=[
 "Compatibility checked per combination, not per source.",
 "Matrix verdicts: compatible, conditional, incompatible.",
 "Common clashes: copyleft vs proprietary, NC vs commercial, conflicting attribution.",
 "Checked at build planning and at publication.",
 "Resolved by substitution, separation, or re-licensing."],
requirements=[
 "License compatibility matrix with legal analysis.",
 "Combination checking at planning and publication.",
 "Resolution workflows with legal involvement.",
 "Combination records with verdicts."],
standards=[
 "Creative Commons compatibility guidance."],
citations=[
 "Creative Commons. License compatibility documentation.",
 "Open Data Commons. ODbL 1.0."],
sig_lens="""The Signature reading: compatibility is the registry's chemistry of charters - which may mix, which explode on contact. The Signature chemist tests every mixture before brewing and keeps the incompatibles apart.""",
demo_data={"licenses":[
 {"name":"compat-a","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"compat-b","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="License Conflict Resolution",
group="Registry Operations", ladder_rank=24, ladder_tier="compounded",
description="""License conflicts surface where terms collide: the vendor license forbids redistribution but the product needs it; the share-alike source demands openness the partnership forbids; two sources' attribution requirements conflict in form. Resolution follows an escalation: interpret (do the terms truly conflict? lawyers read closely - apparent conflicts often dissolve), negotiate (ask the licensor for the needed right - many vendors sell redistribution as an add-on), substitute (find an alternatively licensed source), separate (architect the conflict away), or decline (do not build this combination). Each resolution is documented with the legal reasoning - the conflict file becomes precedent for the next similar case. Conflicts discovered late (in a shipping product) are incidents: the product's data lineage identifies the conflicting sources, remediation options are weighed by cost and time, and leadership decides with eyes open. The program's goal is early detection: conflicts found in planning are puzzles; conflicts found in production are crises.""",
how_it_works="""Conflict intake documents the colliding terms with the product context. Legal interpretation first: apparent vs real conflicts. Negotiation, substitution, separation, or decline per the resolution ladder. Resolutions documented as precedent. Late-discovered conflicts trigger incident response with lineage-based source identification. Detection metrics track planning-vs-production discovery rates; the program optimizes for early.""",
key_points=[
 "Resolution ladder: interpret, negotiate, substitute, separate, decline.",
 "Apparent conflicts often dissolve under close legal reading.",
 "Documented resolutions become precedent.",
 "Late conflicts are incidents; lineage identifies the sources.",
 "Optimize for planning-stage detection."],
requirements=[
 "Conflict intake with legal interpretation.",
 "Resolution ladder with documented outcomes.",
 "Precedent library for repeat conflicts.",
 "Detection-timing metrics."],
standards=[
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Creative Commons. License suite documentation."],
sig_lens="""The Signature reading: conflict resolution is the registry's diplomacy between charters - interpret first, negotiate second, part ways cleanly when irreconcilable. The Signature diplomat records every treaty for the next dispute.""",
demo_data={"licenses":[
 {"name":"conflict-a","commercial":True,"redistribute":False,"expires":"2030-01-01","expected":"ok"},
 {"name":"conflict-b","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
]
