#!/usr/bin/env python3
"""Authored records for the Dataset Acquisition Licensing databases (group F, part 1).
Public = real, fact-checked knowledge (collection methods, CC/ODC licenses,
redistribution rights). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Dataset Acquisition Is",
group="Acquisition", ladder_rank=1, ladder_tier="foundations",
description="""Dataset acquisition is the disciplined intake of external data: finding sources, evaluating them, negotiating access, ingesting the data, and managing the relationship for as long as the data is used. Acquisition covers the full spectrum: open government portals, commercial data vendors, partner feeds, web APIs, licensed compilations, and web scraping where lawful. Each source is evaluated on fitness (does it have what we need?), quality (is it accurate and current?), licensing (may we use it this way?), cost (what is the total cost of ownership?), and risk (what happens if it disappears or sues?). The acquisition registry records every source: what it is, how it is collected, under what license, at what cost, with what renewal dates - because data without a recorded license is a lawsuit waiting for discovery, and data without a recorded renewal date is an outage waiting for expiry. Acquisition is the supply chain of the data estate, managed with supply-chain discipline.""",
how_it_works="""Acquisition workflows run per source: discovery and fitness evaluation, quality assessment on samples, license review with legal, cost modeling, risk assessment, then contracting and technical onboarding. The source registry records collection method, access conditions, license terms, costs, renewal dates, and owners. Ingestion pipelines are built to the source's access terms (rate limits, attribution). Relationship management tracks renewals, quality trends, and vendor health. Source reviews on schedule reassess fitness, cost, and risk; underperforming sources are renegotiated or replaced.""",
key_points=[
 "Acquisition: find, evaluate, negotiate, ingest, and manage data sources.",
 "Evaluated on fitness, quality, licensing, cost, and risk.",
 "The source registry records method, license, cost, renewals, owners.",
 "Unlicensed data is a lawsuit waiting; unrenewed data is an outage waiting.",
 "Supply-chain discipline: reviews, renegotiation, replacement."],
requirements=[
 "Acquisition workflows with evaluation criteria.",
 "Source registry with license and renewal tracking.",
 "Ingestion honoring access terms (rate limits, attribution).",
 "Scheduled source reviews with renegotiation paths."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data licensing."],
sig_lens="""The Signature reading: acquisition is the registry's provisioning - every source vetted, licensed, and recorded before its data enters the house. The Signature quartermaster buys no unlicensed goods and lets no contract lapse unnoticed.""",
demo_data={"licenses":[
 {"name":"open-gov-portal","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"vendor-feed","commercial":True,"redistribute":False,"expires":"2020-01-01","expected":"expired"},
 {"name":"partner-nc","commercial":False,"redistribute":False,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Source Identification",
group="Acquisition", ladder_rank=2, ladder_tier="foundations",
description="""Source identification is the hunt for data worth acquiring: systematically surveying what exists against what the organization needs. The methods: needs analysis (what questions must we answer? what data would answer them?), landscape scanning (portals, vendors, partners, public datasets mapped by domain), and gap analysis (needs minus holdings equals acquisition targets). Each candidate source gets a fitness scorecard: coverage (does it have the entities, geography, time range?), granularity (the right level of detail?), freshness (updated how often?), quality signals (documented methodology? known issues?), and accessibility (open, licensed, or walled?). The identification register keeps the long list - including sources rejected with reasons, so the same dead ends are not re-explored yearly. Prioritization weighs value against cost and risk: the high-value, low-cost, low-risk sources first. Identification never truly ends: new sources appear, needs evolve, and the register's watch list tracks candidates maturing toward fitness.""",
how_it_works="""Needs analyses produce data requirements per domain; landscape scans map candidate sources; gap analyses yield acquisition targets. Scorecards rate candidates on coverage, granularity, freshness, quality, accessibility. The register records candidates, scores, decisions, and rejection reasons. Prioritization sequences acquisitions by value-cost-risk. Watch lists track immature candidates with re-evaluation triggers. Identification reviews refresh the landscape on schedule.""",
key_points=[
 "Identification: needs analysis, landscape scanning, gap analysis.",
 "Fitness scorecards: coverage, granularity, freshness, quality, accessibility.",
 "Rejected sources recorded with reasons - no yearly re-exploration.",
 "Prioritized by value against cost and risk.",
 "Watch lists track candidates maturing toward fitness."],
requirements=[
 "Needs analyses with data requirements per domain.",
 "Candidate scorecards with fitness dimensions.",
 "Identification register with decisions and reasons.",
 "Prioritization and watch-list processes."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on finding data."],
sig_lens="""The Signature reading: source identification is the registry's scouting - surveying the lands for worthy provisions, scoring each honestly, remembering the dead ends. The Signature scouts prioritize the rich, cheap, safe sources first.""",
demo_data={"licenses":[
 {"name":"census-open","commercial":True,"redistribute":True,"expires":"2030-06-01","expected":"ok"},
 {"name":"trial-vendor","commercial":True,"redistribute":True,"expires":"2024-01-01","expected":"expired"}]},
),
dict(
name="Collection Methods: APIs, Scraping, Feeds, Partnerships",
group="Acquisition", ladder_rank=3, ladder_tier="foundations",
description="""Data is collected four ways, each with its own rules. APIs: structured access under terms of service - rate limits, authentication, usage tiers; the cleanest method when the terms permit the use. Web scraping: extracting from websites - lawful only where terms allow, robots.txt respected, and copyright considered; the method of last resort with legal review. Feeds and dumps: bulk deliveries (SFTP drops, data dumps, streaming feeds) under data sharing agreements - the workhorse for large volumes. Partnerships: bilateral data sharing with mutual terms - the richest method, with negotiated quality, support, and evolution. The collection choice follows the hierarchy: use the official API or feed where available; partner where the relationship warrants; scrape only with legal clearance and technical restraint (rate limits, caching, attribution). Every method's terms are recorded in the source registry - the collection method determines the obligations.""",
how_it_works="""Collection planning selects the method per source per the hierarchy, documenting the choice rationale. API integrations implement to terms: authentication, rate limits, usage tiers, attribution. Scraping (where cleared) implements restraint: robots.txt compliance, polite rates, caching, user-agent identification. Feed integrations handle bulk formats with validation and reconciliation. Partnerships negotiate mutual terms with SLAs. All methods record their terms in the registry; compliance monitors verify adherence (rate limits respected, attribution rendered).""",
key_points=[
 "Four methods: APIs (terms-governed), scraping (lawful-only), feeds (bulk agreements), partnerships (negotiated).",
 "Hierarchy: official API/feed first, partnership where warranted, scraping only with clearance.",
 "Scraping restraint: robots.txt, polite rates, caching, identification.",
 "Every method's terms recorded; compliance monitored.",
 "Collection method determines obligations."],
requirements=[
 "Collection method selection with documented rationale.",
 "Terms-compliant implementations per method.",
 "Scraping restraint standards with legal clearance.",
 "Compliance monitoring of collection terms."],
standards=[
 "Robots Exclusion Protocol (RFC 9309)."],
citations=[
 "Koster M et al. RFC 9309: Robots Exclusion Protocol. IETF, 2022.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: collection methods are the registry's four roads to provisions - the king's highway (APIs), the bulk wagons (feeds), the allied granaries (partnerships), and the last-resort paths (scraping) walked only with leave and lightly. Every road's tolls are recorded.""",
demo_data={"licenses":[
 {"name":"api-public","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"scrape-tos-ban","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Web Scraping Rules: Terms, Robots, Copyright",
group="Acquisition", ladder_rank=4, ladder_tier="foundations",
description="""Web scraping is lawful only within bounds: the site's terms of service (do they prohibit scraping?), robots.txt (does it disallow the paths?), copyright (is the content protected expression or facts?), and applicable law (the CFAA's scope, database rights in the EU, trespass doctrines). The compliance posture is conservative: scrape only with legal review, respect robots.txt as the site's stated wishes, honor rate limits and access controls (circumventing technical measures is the bright red line), take only what is needed, and attribute where required. Facts generally are not copyrightable but their creative expression and compilation may be - the scraper of prices is safer than the scraper of articles. Court decisions vary by jurisdiction and evolve; the program tracks them. Scraped data's licensing is often the murkiest: the site's terms may claim rights over scraped content, limiting redistribution regardless of copyright. When in doubt, the program seeks the API, the feed, or the partnership instead.""",
how_it_works="""Legal review clears each scraping program: terms analysis, robots.txt check, copyright assessment, jurisdictional risk. Cleared scrapers implement restraint: robots compliance, polite rates, no circumvention, minimal collection, attribution. Programs re-clear on terms changes and legal developments. Scraped datasets carry their legal basis and limits in metadata, constraining redistribution. Monitoring watches for blocking (the site's answer to unwanted scraping) with backoff and review. Court decision tracking updates the program's risk guidance.""",
key_points=[
 "Bounds: terms of service, robots.txt, copyright, applicable law.",
 "Never circumvent technical measures - the bright red line.",
 "Facts safer than expression; compilations may be protected.",
 "Legal review per program; re-clear on terms or law changes.",
 "When in doubt: API, feed, or partnership instead."],
requirements=[
 "Legal clearance per scraping program.",
 "Restraint implementation: robots, rates, no circumvention.",
 "Legal-basis metadata constraining redistribution.",
 "Court decision tracking with guidance updates."],
standards=[
 "RFC 9309 (robots.txt)."],
citations=[
 "Koster M et al. RFC 9309: Robots Exclusion Protocol. IETF, 2022.",
 "hiQ Labs v. LinkedIn (legal precedent, US)."],
sig_lens="""The Signature reading: scraping rules are the registry's code for the last-resort roads - leave granted, wishes respected, measures never breached, takings minimal. The Signature traveler prefers the highway and walks the wild paths only with leave.""",
demo_data={"licenses":[
 {"name":"facts-feed","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"terms-ban-feed","commercial":False,"redistribute":False,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="API Terms of Service",
group="Acquisition", ladder_rank=5, ladder_tier="foundations",
description="""API terms of service are the contract governing programmatic access: what you may access, how much, how fast, for what purposes, with what attribution, and what happens on violation. The terms that matter: rate limits and quotas (requests per minute, per day - with overage pricing), permitted uses (commercial use often tiered or restricted), data rights (may you store, redistribute, or create derivatives?), attribution requirements (powered-by notices, links), and termination (the provider may cut access with notice - or without, for violations). The compliance program reads terms before integrating, implements to them mechanically (rate limiters, quota dashboards, attribution rendering), and monitors for changes - providers update terms, and continued use constitutes acceptance. Terms violations risk the ultimate penalty: API access revoked, sometimes with the data already integrated. The registry records each API's terms version with the integration, so the obligations are traceable.""",
how_it_works="""Legal and engineering review API terms before integration: limits, uses, rights, attribution, termination. Implementations enforce mechanically: client-side rate limiting, quota monitoring with alerts, attribution in products. Terms monitoring watches for updates; changes trigger re-review with migration or exit planning. The registry links integrations to terms versions. Violation response procedures handle rate-limit breaches (backoff, apologies) and terms disputes. Exit planning keeps alternatives warm for critical APIs.""",
key_points=[
 "Terms govern: limits, quotas, permitted uses, data rights, attribution, termination.",
 "Read before integrating; implement mechanically (limiters, dashboards, attribution).",
 "Providers update terms; continued use is acceptance - monitor changes.",
 "Violations risk access revocation - the ultimate penalty.",
 "Registry links integrations to terms versions."],
requirements=[
 "Terms review before integration with legal and engineering.",
 "Mechanical enforcement: rate limiters, quota alerts, attribution.",
 "Terms change monitoring with re-review.",
 "Exit planning for critical API dependencies."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on API licensing."],
sig_lens="""The Signature reading: API terms are the toll charters of the king's highways - read before traveling, obeyed in motion, watched for amendment. The Signature traveler keeps the charter's edition and plans alternate roads.""",
demo_data={"licenses":[
 {"name":"api-tier-paid","commercial":True,"redistribute":False,"expires":"2030-03-01","expected":"ok"},
 {"name":"api-free-tier","commercial":False,"redistribute":False,"expires":"2030-03-01","expected":"no-commercial"}]},
),
dict(
name="Public Datasets and Portals",
group="Acquisition", ladder_rank=6, ladder_tier="foundations",
description="""Public datasets - government open data portals, scientific repositories, statistical agencies - are the acquisition program's best value: authoritative, free, and licensed for reuse. The major sources: national portals (data.gov, EU data portal, national statistics offices), scientific repositories (GenBank, arXiv-adjacent data, climate archives), and international bodies (World Bank, UN, WHO datasets). Each portal has its own license - many use CC BY or national open licenses, some have custom terms with restrictions worth reading. The acquisition discipline: verify the license (open does not always mean unrestricted), check freshness and methodology (is this dataset maintained? how was it collected?), assess fitness for the purpose, and plan for the portal's reliability (portals go down, formats change, datasets get deprecated). Mirroring strategies keep local copies with provenance: the portal's dataset, version, retrieval date, and license recorded - because the portal may change what open meant.""",
how_it_works="""Portal surveys map relevant datasets with licenses, freshness, methodology, and reliability. License verification confirms reuse rights for the intended purpose (commercial included?). Fitness assessment checks coverage and quality on samples. Mirroring pipelines fetch on schedule with provenance recording (source, version, date, license). Portal monitoring watches for deprecations, format changes, and outages with fallback plans. License changes trigger re-verification - open licenses can be replaced.""",
key_points=[
 "Public portals: authoritative, free, reuse-licensed - the best acquisition value.",
 "Verify licenses: open does not always mean unrestricted.",
 "Assess freshness, methodology, and portal reliability.",
 "Mirror with provenance: source, version, date, license recorded.",
 "Monitor for deprecations and license changes."],
requirements=[
 "Portal surveys with license and quality assessment.",
 "License verification for intended purposes.",
 "Mirroring pipelines with provenance.",
 "Deprecation and license-change monitoring."],
standards=[
 "Open Definition; DCAT for dataset metadata."],
citations=[
 "Open Knowledge Foundation. The Open Definition.",
 "W3C. Data Catalog Vocabulary (DCAT)."],
sig_lens="""The Signature reading: public portals are the commons' granaries - free to the diligent, each sack labeled with its license. The Signature steward verifies the label, records the harvest, and watches the granary's doors.""",
demo_data={"licenses":[
 {"name":"data-gov-census","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"portal-custom-nc","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Commercial Data Vendors",
group="Acquisition", ladder_rank=7, ladder_tier="foundations",
description="""Commercial data vendors sell what open portals lack: depth, freshness, support, and liability - firmographic data, credit data, geolocation, contact databases, market feeds. Vendor selection weighs coverage and accuracy (test on samples against ground truth), freshness (update cadence vs need), licensing (what uses are permitted? redistribution? derivatives? model training?), total cost (license plus integration plus the switching cost later), and vendor viability (will they exist in three years? what happens to the data if not?). Contracts negotiate the terms that matter: permitted uses enumerated, redistribution boundaries, audit rights on usage metering, SLAs on freshness and support, price protections, and exit terms (what data may be kept post-termination?). Vendor management continues after signing: quality monitoring against the contracted bars, relationship reviews, and the ever-present build-vs-buy reassessment. Vendor lock-in is the strategic risk: the deeper the integration, the harder the exit - architected with abstraction layers from day one.""",
how_it_works="""Vendor evaluations score candidates on coverage, accuracy (sampled vs ground truth), freshness, licensing, cost, viability. Contracts negotiate uses, redistribution, metering audit, SLAs, pricing, exit terms. Onboarding integrates with usage metering. Quality monitoring verifies contracted bars; reviews assess the relationship; build-vs-buy reassesses periodically. Abstraction layers isolate vendor specifics for exit readiness. Exit executions follow the contracted terms with data disposition verified.""",
key_points=[
 "Vendors sell depth, freshness, support, liability - selected on coverage, accuracy, license, cost, viability.",
 "Contracts enumerate uses, redistribution, metering audit, SLAs, exit terms.",
 "Quality monitored against contracted bars; relationships reviewed.",
 "Lock-in is the strategic risk - abstraction layers from day one.",
 "Build-vs-buy reassessed periodically."],
requirements=[
 "Vendor evaluation with sampled accuracy testing.",
 "Contract negotiation covering uses through exit terms.",
 "Quality monitoring with relationship reviews.",
 "Abstraction layers for exit readiness."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: vendors are the market's provisioners - judged by sample, bound by contract, watched in delivery. The Signature buyer tastes before buying, writes the terms plainly, and keeps the back door unlocked.""",
demo_data={"licenses":[
 {"name":"vendor-firmographic","commercial":True,"redistribute":False,"expires":"2027-01-01","expected":"ok"},
 {"name":"vendor-expired","commercial":True,"redistribute":False,"expires":"2023-01-01","expected":"expired"}]},
),
dict(
name="Data Partnerships",
group="Acquisition", ladder_rank=8, ladder_tier="foundations",
description="""Data partnerships exchange data bilaterally: two organizations sharing what each has for mutual benefit - the retailer sharing transactions for the bank's fraud signals, the city sharing sensors for the university's research. Partnerships are governed by data sharing agreements covering: what each party provides (with quality bars), permitted uses (and prohibitions), privacy and security duties, intellectual property in derivatives, liability and indemnification, term and termination (with data disposition), and governance (joint reviews, change procedures). The partnership's value must be mutual and measured - one-sided partnerships decay into resentment. Privacy is the usual hard part: shared personal data needs lawful bases, data sharing agreements with the right terms, and often privacy-enhancing technologies (aggregation, differential privacy, clean rooms) to share value without sharing identities. Partnership reviews assess the exchange balance, quality, and compliance on schedule.""",
how_it_works="""Partnership development identifies mutual value with measured exchange balance. Agreements cover provision, uses, privacy, IP, liability, term, governance. Privacy architectures implement the agreed protections: clean rooms, aggregation, PETs. Quality bars on provided data are monitored like vendor SLAs. Reviews assess balance, quality, compliance; imbalances renegotiate. Termination executes data disposition per the agreement with verification.""",
key_points=[
 "Partnerships exchange data bilaterally under sharing agreements.",
 "Agreements cover provision, uses, privacy, IP, liability, term, governance.",
 "Value must be mutual and measured - one-sided partnerships decay.",
 "Privacy via lawful bases, agreement terms, and privacy-enhancing technologies.",
 "Termination executes data disposition with verification."],
requirements=[
 "Partnership value assessment with measured balance.",
 "Data sharing agreements with full term coverage.",
 "Privacy architectures per agreement.",
 "Scheduled reviews with renegotiation paths."],
standards=[
 "ISO/IEC 27701; DAMA-DMBOK."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data sharing."],
sig_lens="""The Signature reading: partnerships are sworn exchanges between houses - each giving value, each bound by charter, the balance weighed openly. The Signature compact measures the trade and parts cleanly when it ends.""",
demo_data={"licenses":[
 {"name":"partner-bank","commercial":True,"redistribute":False,"expires":"2028-06-01","expected":"ok"},
 {"name":"partner-lapsed","commercial":True,"redistribute":False,"expires":"2022-06-01","expected":"expired"}]},
),
dict(
name="License Types Overview",
group="Licenses", ladder_rank=9, ladder_tier="foundations",
description="""Data licenses fall into families with distinct freedoms. Public domain (CC0): do anything, no permission needed - the freest. Permissive open (CC BY, ODC-By): use freely with attribution. Copyleft open (CC BY-SA, ODbL): use freely, share derivatives alike - the share-alike obligation travels downstream. Non-commercial (CC BY-NC variants): no commercial use - the most misunderstood (what counts as commercial?); avoided where commercial use is conceivable. Proprietary: use per negotiated terms - the vendor's license with its specific permissions and prohibitions. Government open licenses (UK OGL, French Licence Ouverte): permissive with attribution, sometimes with compatibility quirks. Custom terms: API terms, portal terms - read carefully, they vary wildly. The license determines everything downstream: what products may be built, whether derivatives may be sold, what attribution is owed, and whether the data may train models. License identification is therefore the first acquisition step, and incompatible licenses are disqualifying regardless of data quality.""",
how_it_works="""License identification classifies each source into its family with the specific terms recorded. Compatibility analysis checks the intended uses against the license: commercial use, redistribution, derivatives, model training - each verified. Incompatible licenses disqualify regardless of quality. Multi-source combinations check license compatibility across the mix (copyleft plus proprietary usually fails). License records version with the source; re-licensing triggers re-verification. Legal review covers the ambiguous cases (NC scope, custom terms).""",
key_points=[
 "Families: public domain, permissive, copyleft, non-commercial, proprietary, government, custom.",
 "License determines products, derivatives, attribution, model training rights.",
 "Incompatible licenses disqualify regardless of data quality.",
 "Multi-source mixes need cross-license compatibility.",
 "NC licenses avoided where commercial use is conceivable."],
requirements=[
 "License identification with family and terms recorded.",
 "Use-case compatibility verification per license.",
 "Multi-source compatibility analysis.",
 "Legal review for ambiguous licenses."],
standards=[
 "Creative Commons licenses; Open Data Commons licenses."],
citations=[
 "Creative Commons. License suite documentation.",
 "Open Data Commons. ODC licenses."],
sig_lens="""The Signature reading: license families are the charters of reuse - from the free commons to the guarded vaults, each with its freedoms and duties. The Signature registrar reads every charter before admitting its goods.""",
demo_data={"licenses":[
 {"name":"cc0-data","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"cc-by-nc-data","commercial":False,"redistribute":True,"expires":"2030-01-01","expected":"no-commercial"}]},
),
dict(
name="Open Licenses: CC and ODC",
group="Licenses", ladder_rank=10, ladder_tier="foundations",
description="""Creative Commons and Open Data Commons licenses are the standard open instruments. CC0 dedicates to the public domain - no rights reserved, no attribution required (though given by custom). CC BY requires attribution - the workhorse for open data. CC BY-SA adds share-alike: derivatives must carry the same license - the copyleft that keeps improvements open. CC BY-NC and variants restrict commercial use. For databases specifically, the ODC licenses matter: ODbL (share-alike for databases, used by OpenStreetMap), ODC-By (attribution for databases), and PDDL (public domain for databases) - because database rights (the EU sui generis right) need licensing that CC's copyright-focused licenses address less directly. License compliance for open data means: attribute as required (title, author, source, license with link), share alike where required (derivatives under the same terms), and respect NC where present. Version matters: CC 4.0 is international and database-aware; earlier versions have porting quirks.""",
how_it_works="""License selection matches the source's terms: record the exact license and version. Compliance implements attribution (TASL: title, author, source, license), share-alike propagation to derivatives, and NC respect. Derivative works carry forward the license obligations - the share-alike chain is tracked. Version quirks handled: pre-4.0 ported licenses checked for local adaptations. Compliance audits verify attribution rendering and share-alike propagation. Re-licensing by the source triggers re-verification of all uses.""",
key_points=[
 "CC0 public domain; CC BY attribution; CC BY-SA share-alike; CC BY-NC non-commercial.",
 "ODC licenses (ODbL, ODC-By, PDDL) address database rights directly.",
 "Compliance: attribute (TASL), share alike, respect NC.",
 "Share-alike obligations propagate to derivatives - tracked as chains.",
 "CC 4.0 international and database-aware; earlier versions have quirks."],
requirements=[
 "Exact license and version recording per source.",
 "Attribution implementation (TASL) in products.",
 "Share-alike chain tracking for derivatives.",
 "Compliance audits on attribution and propagation."],
standards=[
 "Creative Commons 4.0; Open Data Commons licenses."],
citations=[
 "Creative Commons. CC 4.0 license texts.",
 "Open Data Commons. ODbL 1.0."],
sig_lens="""The Signature reading: open licenses are the commons' charters - the free, the attributed, the share-alike, each with its sworn duties. The Signature commoner attributes faithfully and passes share-alike forward.""",
demo_data={"licenses":[
 {"name":"odbl-map","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"cc-by-data","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
dict(
name="Proprietary Licenses",
group="Licenses", ladder_rank=11, ladder_tier="foundations",
description="""Proprietary licenses are negotiated instruments: each vendor's terms, each partnership's agreement, each with its own permissions and prohibitions. The terms that matter most: scope of use (which products, which users, which geographies?), data rights (store? cache? derive? redistribute? train models?), restrictions (no reverse engineering of the data? no competitive use? no combining with certain sources?), term and renewal (how long? auto-renew? price changes?), audit rights (can the vendor meter your usage?), and termination (what must be deleted? what may be kept?). Negotiation focuses on the future: the uses you will need in three years, not just today's - because the license that forbids model training becomes a crisis when the ML team needs the data. The registry abstracts proprietary terms into a standard rights model (use, store, derive, redistribute, train - each yes/no/conditional) so compliance can be checked uniformly across vendors' varied legalese.""",
how_it_works="""Legal review extracts the key terms into the standard rights model per license. Negotiation targets future uses with fallback positions. The rights model enables uniform compliance checking across vendors. Usage monitoring verifies the actual uses match the licensed rights. Renewal workflows start early with renegotiation of inadequate terms. Termination executes the disposition terms with verification. Rights model versions track license amendments.""",
key_points=[
 "Proprietary licenses: negotiated terms, each vendor's own legalese.",
 "Key terms: scope, data rights, restrictions, term, audit, termination.",
 "Negotiate for future uses, not just today's.",
 "Standard rights model abstracts varied legalese for uniform compliance.",
 "Usage monitored against licensed rights; renewals renegotiate gaps."],
requirements=[
 "Legal extraction into standard rights models.",
 "Future-use negotiation with fallback positions.",
 "Usage monitoring against rights.",
 "Renewal workflows with renegotiation."],
standards=[
 "DAMA-DMBOK data integration guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Open Data Institute. Guidance on data procurement."],
sig_lens="""The Signature reading: proprietary licenses are bespoke charters - each negotiated, each abstracted to the common rights tongue. The Signature negotiator bargains for tomorrow's needs and watches today's uses.""",
demo_data={"licenses":[
 {"name":"vendor-prop","commercial":True,"redistribute":False,"expires":"2027-09-01","expected":"ok"},
 {"name":"vendor-no-train","commercial":True,"redistribute":False,"expires":"2027-09-01","expected":"ok"}]},
),
dict(
name="Government Open Data Licenses",
group="Licenses", ladder_rank=12, ladder_tier="foundations",
description="""Governments publish under their own open licenses: the UK Open Government Licence (permissive, attribution, compatible with CC BY), the French Licence Ouverte, the US public domain tradition (federal works), and many national variants. These licenses are generally permissive - use commercially, redistribute, derive - with attribution to the source. The quirks to watch: compatibility (is this national license compatible with CC BY for combined works?), personal data exclusions (the license does not override privacy law - the open dataset with personal data is still regulated), and version changes (governments update licenses; the dataset's license version governs). Some government data carries additional restrictions: national security classifications, statistical confidentiality (census microdata), or cost-recovery charging for premium access. The acquisition program treats government licenses as first-class: recorded exactly, compatibility checked for combinations, privacy duties layered independently of the license's permissiveness.""",
how_it_works="""Government licenses recorded exactly with version; compatibility checked for multi-source combinations. Privacy duties applied independently - the license's permissiveness never overrides data protection. Restriction flags (security, statistical confidentiality, charging) honored. Version monitoring watches for license updates with re-verification. Attribution rendered per the license's requirements.""",
key_points=[
 "Government licenses generally permissive with attribution (UK OGL, Licence Ouverte, US PD).",
 "Compatibility checked for combined works across national licenses.",
 "Licenses do not override privacy law - personal data stays regulated.",
 "Watch restrictions: security, statistical confidentiality, premium charging.",
 "Versions monitored; the dataset's license version governs."],
requirements=[
 "Exact government license recording with versions.",
 "Cross-license compatibility analysis.",
 "Independent privacy duty application.",
 "License version monitoring."],
standards=[
 "UK Open Government Licence v3.0."],
citations=[
 "UK National Archives. Open Government Licence v3.0.",
 "Etalab. Licence Ouverte 2.0."],
sig_lens="""The Signature reading: government licenses are the crown's gifts to the commons - generous, attributed, but never overriding the privacy of subjects. The Signature steward records each gift exactly and honors its conditions.""",
demo_data={"licenses":[
 {"name":"uk-ogl-data","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"},
 {"name":"us-pd-data","commercial":True,"redistribute":True,"expires":"2030-01-01","expected":"ok"}]},
),
]
