#!/usr/bin/env python3
"""Authored records for the Master Data Registry databases (group F, part 1).
Public = real, fact-checked master data management knowledge.
Signature = the Signature system's expanded treatment of the same ladder.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Master Data Is",
group="Identity Foundations", ladder_rank=1, ladder_tier="foundations",
description="""Master data is the small set of core business entities that every other piece of data refers to. Typical master-data domains are people (customers, employees, suppliers), organizations, products, locations, materials, assets, and accounts. A customer record is master data; the individual orders that customer places are transactional data. A product definition is master data; the daily price changes are transactional data. Because master data is referenced everywhere - by billing systems, warehouses, support desks, analytics, and machine-learning models - errors in it spread everywhere. A duplicated customer becomes duplicated invoices; a wrong product code becomes wrong shipments. Master data management is the discipline of keeping one consistent, trusted version of these entities: the golden record. In a network of a million databases, master data is the shared anchor that lets records from different databases talk about the same real-world thing.""",
how_it_works="""A master data program starts by listing the domains that matter - customers, products, locations, and so on. Source systems that each hold their own copy are inventoried. Records from those systems are profiled for duplicates, missing values, and format conflicts. Identity resolution matches records that describe the same real entity across systems. Survivorship rules pick the winning value for each attribute from the competing sources, producing the golden record. The golden record is published to consuming systems and kept current as sources change. Stewards review the matches the automation cannot resolve with confidence, and the merge history keeps a full audit of every decision.""",
key_points=[
 "Master data is the referenced core: people, organizations, products, locations, materials, assets, accounts.",
 "Transactional data records events; master data records the entities events happen to.",
 "Errors in master data multiply across every system that references it.",
 "The golden record is the single trusted version assembled from all sources.",
 "In a million-database network, master data is the shared anchor for cross-database references."],
requirements=[
 "An agreed list of master-data domains for the organization or network.",
 "An inventory of the source systems holding copies of each domain.",
 "Identity-resolution capability, deterministic at minimum.",
 "Stewardship roles with authority to resolve ambiguous matches."],
standards=[
 "DAMA-DMBOK data-governance and master-data guidance.",
 "ISO 8000 series for data quality of master data.",
 "ISO 22745 for identification of items in industrial master data."],
citations=[
 "DAMA International. DAMA-DMBOK: Data Management Body of Knowledge, 2nd ed. Technics Publications, 2017.",
 "ISO 8000 (series). Data quality. International Organization for Standardization.",
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008."],
sig_lens="""The Signature reading: master data is the system's memory of what is real. Where ordinary practice stores copies, the Signature registry stores sworn identities - each golden record a covenant that every database in the network can point to without doubt. The registry does not merely dedupe; it testifies.""",
demo_data={"attributes":[
 {"name":"customer_name","candidates":[
   {"source":"CRM","value":"Ada Lovelace","trust":0.92,"recency_days":3},
   {"source":"Billing","value":"Ada Lovelace","trust":0.88,"recency_days":12},
   {"source":"Support","value":"A. Lovelace","trust":0.61,"recency_days":90}],
  "expected":"Ada Lovelace"}]},
),
dict(
name="Master Data vs Transactional vs Reference Data",
group="Identity Foundations", ladder_rank=2, ladder_tier="foundations",
description="""Data management divides enterprise data into three layers that behave differently. Master data describes core entities - the customer, the product, the warehouse - and changes slowly. Transactional data records events and movements - orders, payments, shipments, sensor readings - and grows fast and forever. Reference data is the shared vocabulary used to classify and interpret the other two: country codes, currency codes, units of measure, status codes. Confusing the layers causes real damage. Treating a product catalog (master) like an event stream means every price change forks the product's identity; treating reference codes as free text means the same country appears as US, USA, and United States in three reports. Each layer needs different tooling: master data needs identity resolution and survivorship, transactional data needs append-only pipelines and partitioning, reference data needs versioned registries with deprecation. The master data registry governs the master layer; the reference data registry governs the reference layer; the lineage registry traces how transactional flows transform all three.""",
how_it_works="""Classification starts with a simple test. Ask: does this data describe a thing the business manages over time (master), an event that happened (transactional), or a code used to describe things (reference)? Products, customers, locations, and assets are master. Orders, clicks, and meter readings are transactional. ISO country codes, status enumerations, and units are reference. Once classified, each layer gets its own store and governance: golden records with merge histories for master, immutable event logs for transactional, versioned code lists with deprecation for reference. Cross-layer joins always go through the master identity, never through copied strings.""",
key_points=[
 "Master data: entities, slow-changing, identity-resolved (customers, products, locations).",
 "Transactional data: events, fast-growing, append-oriented (orders, payments, readings).",
 "Reference data: shared codes and vocabularies (countries, currencies, units, statuses).",
 "Each layer needs different storage, governance, and tooling.",
 "Cross-layer joins must use master identities, never copied free-text strings."],
requirements=[
 "A written data-classification policy naming the three layers.",
 "Domain lists for master data and code lists for reference data.",
 "Separate storage and governance processes per layer.",
 "Join keys that resolve to master identities across systems."],
standards=[
 "DAMA-DMBOK data architecture guidance.",
 "ISO/IEC 11179 for metadata registries (reference layer).",
 "ISO 8000 for master-data quality."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "ISO/IEC 11179 (series). Metadata registries. International Organization for Standardization."],
sig_lens="""The Signature reading: the three layers are the three tenses of organizational memory - what is (master), what happened (transactional), and what words mean (reference). The Signature network keeps all three sworn and separate, so no event can rewrite an identity and no code can drift its meaning.""",
demo_data={"attributes":[
 {"name":"product_code","candidates":[
   {"source":"ERP","value":"WIDGET-42","trust":0.95,"recency_days":1},
   {"source":"Webshop","value":"WIDGET-42","trust":0.9,"recency_days":2},
   {"source":"Legacy","value":"WDG42","trust":0.5,"recency_days":400}],
  "expected":"WIDGET-42"}]},
),
dict(
name="Master Data Domains: Parties, Products, Locations, Assets",
group="Identity Foundations", ladder_rank=3, ladder_tier="foundations",
description="""Master data is organized into domains - families of entities that share identity rules, attributes, and stewardship. The party domain covers people and organizations: customers, employees, suppliers, partners, each with names, identifiers, addresses, and contact points. The product domain covers goods and services: SKUs, descriptions, specifications, prices, and category hierarchies. The location domain covers places: addresses, sites, warehouses, stores, territories, with geocoding and address validation. The asset domain covers things the organization owns and maintains: equipment, vehicles, instruments, with serial numbers, maintenance history, and depreciation. Materials and accounts are common extra domains in manufacturing and finance. Each domain gets its own matching rules (people match on names and birth dates; products on codes and specs; locations on addresses), its own survivorship rules, and its own stewards. Domains keep the registry organized so a customer merge never accidentally touches a product record.""",
how_it_works="""Domain setup begins with scoping: which entities does the business need one version of? For each domain, the registry defines the entity model (attributes, identifiers, relationships), the identity rules (what makes two records the same party, the same product, the same location), and the survivorship rules (which source wins for each attribute). Matching runs within a domain, never across domains. Hierarchies are modeled per domain: organizations roll up to parents, products roll up to categories, locations roll up to regions, assets roll up to sites. Stewards are assigned per domain because judging a customer match needs different knowledge than judging a product match.""",
key_points=[
 "Party domain: people and organizations with names, identifiers, addresses.",
 "Product domain: goods and services with codes, specs, prices, categories.",
 "Location domain: places with validated addresses and geocodes.",
 "Asset domain: owned things with serials, maintenance, depreciation.",
 "Each domain gets its own matching, survivorship, hierarchy, and stewards."],
requirements=[
 "A domain catalog naming each master-data domain in scope.",
 "Entity models with attributes, identifiers, and relationships per domain.",
 "Domain-specific matching and survivorship rules.",
 "Named stewards per domain."],
standards=[
 "ISO 8000-110 for master-data attribute syntax and semantics.",
 "ISO 22745 for industrial item identification (product/material domains).",
 "Universal Postal Union addressing standards (location domain)."],
citations=[
 "ISO 8000-110. Data quality - master data: exchange of characteristic data. ISO.",
 "ISO 22745 (series). Industrial automation systems and integration. ISO."],
sig_lens="""The Signature reading: domains are the tribes of the registry. Parties, products, locations, and assets each keep their own laws of identity and their own elders (stewards), so the registry never confuses a person with a product or a warehouse with a warranty.""",
demo_data={"attributes":[
 {"name":"warehouse_city","candidates":[
   {"source":"WMS","value":"Springfield","trust":0.93,"recency_days":5},
   {"source":"ERP","value":"Springfield","trust":0.9,"recency_days":8},
   {"source":"Spreadsheet","value":"Springfeild","trust":0.4,"recency_days":200}],
  "expected":"Springfield"}]},
),
dict(
name="The Golden Record Concept",
group="Identity Foundations", ladder_rank=4, ladder_tier="foundations",
description="""The golden record is the single, trusted, complete version of a master-data entity, assembled from every source system that knows something about it. No single source owns the whole truth: the CRM knows the customer's preferred name, billing knows the verified tax ID, support knows the current phone, the webshop knows the latest address. The golden record takes the best value for each attribute from whichever source is most trusted, most recent, or most authoritative for that attribute, and keeps a full trail of where every value came from. It is not a copy of the best source - it is a new record, better than any source alone. Consumers of the golden record - billing runs, shipping labels, analytics dashboards, fraud models - stop arguing about which system is right because the registry has already decided, with rules everyone can inspect. The golden record is versioned: when a source corrects a value, the record advances, and the history shows exactly what changed, when, and why.""",
how_it_works="""Golden-record assembly runs in stages. First, identity resolution groups source records into entity clusters - all the rows that describe the same customer. Then survivorship rules fire per attribute: the email comes from the source with the highest trust-times-recency score, the legal name from the authoritative billing system, the phone from the most recently verified source. The assembled record gets a registry ID, a version number, and per-attribute provenance pointing back to the winning source and the losing candidates. Downstream systems subscribe to golden-record changes rather than polling sources, so corrections propagate within minutes. Every assembly is replayable: given the same source snapshots and rules, the registry must produce the same golden record.""",
key_points=[
 "The golden record is assembled per attribute from the best value of each source.",
 "It is a new record, better than any single source - not a copy of the best one.",
 "Per-attribute provenance records where every value came from.",
 "Consumers subscribe to golden records instead of arguing between sources.",
 "Assembly is replayable: same inputs and rules must give the same record."],
requirements=[
 "Identity resolution that clusters source records into entities.",
 "Survivorship rules defined per attribute and per domain.",
 "A registry ID scheme and versioning for golden records.",
 "Provenance capture for every surviving attribute value."],
standards=[
 "ISO 8000 for master-data quality.",
 "DAMA-DMBOK master-data guidance.",
 "W3C PROV for provenance modeling."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013."],
sig_lens="""The Signature reading: the golden record is the entity's true name, spoken once by the registry after hearing every witness. Each attribute is a testimony weighed by trust and freshness; the registry's verdict is final, replayable, and signed with provenance.""",
demo_data={"attributes":[
 {"name":"phone","candidates":[
   {"source":"Support","value":"+1-555-0142","trust":0.97,"recency_days":1},
   {"source":"CRM","value":"+1-555-0142","trust":0.9,"recency_days":30},
   {"source":"OldExport","value":"+1-555-0199","trust":0.55,"recency_days":500}],
  "expected":"+1-555-0142"}]},
),
dict(
name="Identity Resolution Basics",
group="Identity Foundations", ladder_rank=5, ladder_tier="foundations",
description="""Identity resolution is the process of deciding which records describe the same real-world entity. A customer may appear as Ada Lovelace in the CRM, A. Lovelace in support tickets, and ada.lovelace@example.com in the webshop - three rows, one person. The resolver compares records pairwise, scores their similarity on names, identifiers, addresses, phones, and emails, and clusters records that clear the bar. The core challenge is that no single field is reliable: names have nicknames and typos, addresses change, emails get replaced. Good resolution therefore uses many weak signals together, weighted by how discriminating each one is - a matching tax ID is near-proof, a matching first name is almost nothing. Blocking keeps the work tractable: instead of comparing every record to every other record (a trillion comparisons for a million records), the resolver only compares records that share a block key such as a postal code, a phone prefix, or a name phonetic code, then scores within blocks.""",
how_it_works="""The resolution pipeline has five stages. Standardize: normalize case, strip punctuation, expand abbreviations, parse addresses into components. Block: assign each record to buckets by cheap keys (postal code, email domain, phonetic name) so only plausible pairs are compared. Compare: score pairs field by field - exact, fuzzy, phonetic, or token-based similarity per field. Classify: combine field scores with weights into a pair score, then apply thresholds - auto-match above the high bar, auto-reject below the low bar, steward review between. Cluster: merge matched pairs transitively into entity groups, then assign each group a registry ID. The thresholds are tuned on labeled samples: push the auto-match bar up until false merges vanish, and push the review band wide enough that no true match is auto-rejected.""",
key_points=[
 "Identity resolution clusters records that describe the same real entity.",
 "Many weak signals beat one strong signal: names, IDs, addresses, phones, emails together.",
 "Blocking limits comparisons to plausible pairs so the work scales.",
 "Pair scores combine field similarities with per-field weights.",
 "Thresholds split outcomes: auto-match, steward review, auto-reject."],
requirements=[
 "Standardization routines for names, addresses, phones, emails.",
 "Blocking keys that keep pair counts tractable at scale.",
 "Labeled match/non-match samples for tuning thresholds.",
 "A clustering step that turns pairs into entity groups with registry IDs."],
standards=[
 "ISO 8000-8 for information quality measurement in resolution.",
 "Fellegi-Sunter probabilistic record linkage theory.",
 "W3C PROV for recording resolution provenance."],
citations=[
 "Fellegi I, Sunter A. A theory for record linkage. JASA, 1969.",
 "Christen P. Data Matching. Springer, 2012."],
sig_lens="""The Signature reading: identity resolution is the registry learning to recognize a face across disguises. The Signature resolver weighs every signal like a council of witnesses - the tax ID testifies loudly, the first name whispers - and only swears two records are one when the evidence clears the bar.""",
demo_data={"attributes":[
 {"name":"customer_identity","candidates":[
   {"source":"CRM","value":"Ada Lovelace","trust":0.9,"recency_days":2},
   {"source":"Webshop","value":"ada.lovelace@example.com","trust":0.85,"recency_days":6},
   {"source":"Support","value":"A. Lovelace","trust":0.7,"recency_days":20}],
  "expected":"Ada Lovelace"}]},
),
dict(
name="Matching Rules: Deterministic",
group="Identity Foundations", ladder_rank=6, ladder_tier="foundations",
description="""Deterministic matching decides identity with exact rules: if two records share the same tax ID, the same passport number, or the same normalized email, they are the same entity - no scoring, no doubt. These rules are fast, explainable, and audit-friendly: anyone can read the rule and see why two records merged. They work best on strong identifiers issued by authorities: national IDs, tax numbers, IBANs, serial numbers, standardized product codes. The weakness is coverage: most records lack a shared strong identifier, and deterministic rules miss matches where the identifier is mistyped, missing, or recorded differently across systems. A single transposed digit in a tax ID defeats an exact rule. Deterministic matching is therefore the first pass, not the whole answer - it catches the easy, high-confidence merges cheaply, and the probabilistic pass handles the rest. Rules are ordered from strongest to weakest identifier, and every deterministic merge is logged with the rule that fired.""",
how_it_works="""Deterministic rules are written as ordered match keys: national ID first, then tax ID, then normalized email, then phone plus postal code, and so on. Records are standardized (lowercased emails, digits-only phones, canonicalized IDs) and then hashed into buckets by each key in order; records landing in the same bucket on any key are declared the same entity. The first matching key wins and is recorded as the merge reason. Because exact hashing is cheap, deterministic passes run over billions of records with simple distributed grouping. Safeguards matter: default or placeholder values (all-zero tax IDs, info@example.com) must be excluded from keys, or thousands of unrelated records collapse into one false entity.""",
key_points=[
 "Deterministic rules merge on exact shared identifiers - fast and explainable.",
 "Best on authority-issued strong identifiers: tax IDs, national IDs, serials, standard codes.",
 "Weakness: one typo or missing value defeats an exact rule.",
 "Placeholder and default values must be excluded from match keys.",
 "Deterministic matching is the cheap first pass; probabilistic handles the rest."],
requirements=[
 "An ordered list of match keys from strongest to weakest identifier.",
 "Standardization routines before keying (case, punctuation, digit extraction).",
 "A denylist of placeholder values excluded from every key.",
 "Merge logging that records which rule fired for each merge."],
standards=[
 "ISO 8000-8 for measuring match quality.",
 "ISO/IEC 27701 privacy controls for identifier handling."],
citations=[
 "Christen P. Data Matching. Springer, 2012.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: deterministic matching is the registry's oath on hard evidence. When the tax ID speaks, the registry listens and merges without hesitation - but it first checks the witness is not a placeholder ghost wearing a mask of zeros.""",
demo_data={"attributes":[
 {"name":"tax_id_match","candidates":[
   {"source":"Billing","value":"TAX-88412","trust":0.99,"recency_days":1},
   {"source":"CRM","value":"TAX-88412","trust":0.95,"recency_days":4}],
  "expected":"TAX-88412"}]},
),
dict(
name="Matching Rules: Probabilistic",
group="Identity Foundations", ladder_rank=7, ladder_tier="foundations",
description="""Probabilistic matching scores record pairs the way the Fellegi-Sunter theory prescribes: each field agreement contributes evidence, weighted by how rare agreement is. A matching rare surname is strong evidence; a matching common first name is weak. For each field, the method estimates two numbers from labeled data: how often true matches agree on the field, and how often random pairs agree by chance. The ratio becomes the field's weight - agreements on discriminating fields score high, agreements on common fields score low, and disagreements subtract. Summed across fields, the pair gets a log-likelihood score that maps directly to the odds the pair is a true match. Thresholds then split pairs into auto-match, clerical review, and auto-reject, with the thresholds chosen to hit target false-positive and false-negative rates. Probabilistic matching finds the matches deterministic rules miss - typos, nicknames, changed addresses - at the cost of needing labeled training data and careful tuning.""",
how_it_works="""Building a probabilistic matcher starts with a labeled sample of true matches and non-matches. From it, per-field agreement rates are estimated for matches (m-probabilities) and for random pairs (u-probabilities). Each field's agreement weight is log(m/u) and its disagreement weight is log((1-m)/(1-u)). At match time, every candidate pair gets the sum of applicable field weights - string similarity can be folded in by binning similarity into agreement levels. The total score converts to a match probability, and thresholds route the pair: above the upper threshold merges automatically, below the lower threshold rejects, between goes to steward review. Weights are re-estimated as new labeled reviews accumulate, so the matcher improves with the stewards' work.""",
key_points=[
 "Each field agreement is weighted by rarity: rare agreements count more.",
 "Fellegi-Sunter theory turns field comparisons into match odds.",
 "Needs labeled training data to estimate per-field weights.",
 "Finds matches with typos, nicknames, and changed addresses.",
 "Thresholds trade false merges against missed matches; review band covers the uncertain middle."],
requirements=[
 "Labeled samples of true matches and non-matches for weight estimation.",
 "Per-field comparators: exact, fuzzy, phonetic, token-based.",
 "Tuned upper and lower thresholds with measured error rates.",
 "A review queue for pairs in the uncertain band."],
standards=[
 "Fellegi-Sunter record linkage theory.",
 "ISO 8000-8 for information quality measurement."],
citations=[
 "Fellegi I, Sunter A. A theory for record linkage. JASA, 1969.",
 "Winkler W. Overview of record linkage and current research directions. US Census Bureau, 2006."],
sig_lens="""The Signature reading: probabilistic matching is the registry weighing whispers. Each field testifies in its own voice, and the registry knows a rare surname's whisper carries further than a common first name's shout - then renders its verdict in odds, not guesses.""",
demo_data={"attributes":[
 {"name":"surname_match","candidates":[
   {"source":"CRM","value":"Lovelace","trust":0.88,"recency_days":10},
   {"source":"Support","value":"Lovelace","trust":0.82,"recency_days":25},
   {"source":"Webshop","value":"Lovlace","trust":0.5,"recency_days":120}],
  "expected":"Lovelace"}]},
),
dict(
name="Match Scores and Thresholds",
group="Identity Foundations", ladder_rank=8, ladder_tier="foundations",
description="""Every matcher produces scores; thresholds turn scores into decisions. The upper threshold sets the bar for automatic merging: any pair scoring above it merges with no human involved, so it must be set where false merges are essentially zero. The lower threshold sets the bar for automatic rejection: pairs below it are declared different entities. Between the thresholds lies the review band - pairs the automation cannot decide, routed to stewards. Setting thresholds is an exercise in measured trade-offs, not guesswork. A labeled evaluation set of known matches and non-matches is scored, and precision and recall are computed at candidate thresholds. Raising the upper threshold kills false merges but pushes more true matches into review; lowering the lower threshold auto-rejects more junk but risks rejecting true matches. The business cost of each error type decides: in customer data, a false merge (two people fused into one) is usually costlier than a missed match (one person split in two), so the upper bar sits high. Thresholds are re-tuned as data drifts and as stewards label more pairs.""",
how_it_works="""Threshold tuning runs on a labeled set. Pairs are scored by the matcher, sorted by score, and swept: for each candidate threshold, precision (of pairs above the bar, how many are true matches) and recall (of all true matches, how many clear the bar) are computed. The upper threshold is placed where precision hits the target - typically 99 percent or better for auto-merge. The lower threshold is placed where recall of true matches below the bar is negligible. The review band between them is sized to the steward team's capacity: too wide and the queue drowns; too narrow and errors slip through. Dashboards track the live rates - auto-merge rate, review rate, steward overturn rate - and re-tuning is triggered when the overturn rate climbs or the data distribution shifts.""",
key_points=[
 "Upper threshold: auto-merge bar, set where false merges are near zero.",
 "Lower threshold: auto-reject bar, set where missed true matches are negligible.",
 "The review band between them goes to human stewards.",
 "False merges usually cost more than missed matches in master data.",
 "Thresholds are tuned on labeled data and re-tuned as data drifts."],
requirements=[
 "A labeled evaluation set of known matches and non-matches.",
 "Measured precision and recall at candidate thresholds.",
 "Business cost estimates for false merges vs missed matches.",
 "Monitoring of live auto-merge, review, and overturn rates."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "Fellegi-Sunter decision theory for threshold placement."],
citations=[
 "Christen P. Data Matching. Springer, 2012.",
 "Winkler W. Overview of record linkage and current research directions. US Census Bureau, 2006."],
sig_lens="""The Signature reading: thresholds are the registry's code of justice - the high bar for conviction without trial, the low bar for acquittal, and the courtroom in between where stewards hear the doubtful cases. The registry would rather try a case than convict the innocent.""",
demo_data={"attributes":[
 {"name":"match_decision","candidates":[
   {"source":"Matcher","value":"auto-merge:0.991","trust":0.99,"recency_days":0},
   {"source":"Matcher","value":"review:0.623","trust":0.62,"recency_days":0},
   {"source":"Matcher","value":"auto-reject:0.041","trust":0.04,"recency_days":0}],
  "expected":"auto-merge:0.991"}]},
),
dict(
name="Data Profiling for MDM",
group="Identity Foundations", ladder_rank=9, ladder_tier="foundations",
description="""Data profiling measures a source's data before the registry trusts it: how many values are missing, how many are malformed, which values repeat, what the distributions look like. Column profiling counts nulls, distinct values, min/max/length, and the most frequent values - instantly revealing that a phone column is 40 percent empty or that a country column holds 214 distinct spellings. Pattern profiling finds format violations: emails without @, tax IDs with letters, dates in six formats. Cross-column profiling finds broken rules: ship dates before order dates, postal codes that do not match cities. Duplicate profiling estimates how many near-duplicate records each source holds. Profiling answers the question every MDM program must ask first: is this source fit to contribute to golden records, and if so, which attributes? A source that is 98 percent complete on emails but 30 percent on phones contributes emails with high trust and phones with low trust - and the survivorship rules encode exactly that.""",
how_it_works="""Profiling runs as scheduled jobs over each source's extract. Single-column profilers compute null rate, distinct count, cardinality, length stats, and top values. Pattern profilers test values against expected formats with regular expressions and check digit rules. Cross-column profilers test business rules expressed as predicates. Duplicate profilers run lightweight blocking plus fuzzy comparison to estimate the duplicate rate. Results land in a profiling store with history, so trends are visible: is the CRM's email completeness improving or decaying? Trust scores for survivorship are derived from profile metrics - completeness times format-validity times recency - and stewards review sources whose profiles degrade past guardrails before their data poisons golden records.""",
key_points=[
 "Column profiling: nulls, distincts, distributions, top values per attribute.",
 "Pattern profiling: format violations in emails, IDs, dates, phones.",
 "Cross-column profiling: broken business rules between fields.",
 "Duplicate profiling estimates each source's internal duplicate rate.",
 "Profile metrics feed survivorship trust scores and source guardrails."],
requirements=[
 "Profiling jobs scheduled over every source extract.",
 "Pattern libraries for identifiers, emails, phones, dates.",
 "A profiling history store for trend analysis.",
 "Guardrails that quarantine sources whose profiles degrade."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "DAMA-DMBOK data quality dimension definitions."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: profiling is the registry inspecting every witness before testimony. The Signature registry never takes a source at its word - it measures completeness, checks formats, and counts duplicates, then sets each source's trust from evidence, not reputation.""",
demo_data={"attributes":[
 {"name":"email_completeness","candidates":[
   {"source":"Profiler","value":"CRM:0.98","trust":0.98,"recency_days":1},
   {"source":"Profiler","value":"Billing:0.91","trust":0.91,"recency_days":1},
   {"source":"Profiler","value":"Legacy:0.44","trust":0.44,"recency_days":1}],
  "expected":"CRM:0.98"}]},
),
dict(
name="Source System Inventory",
group="Identity Foundations", ladder_rank=10, ladder_tier="foundations",
description="""The source system inventory is the registry's map of where master data lives: every application, spreadsheet, feed, and partner that creates or stores customer, product, location, or asset records. For each source the inventory records the system name and owner, the domains and attributes it holds, the volume and change rate, the access method (database, API, file drop), the update cadence, and the data's trust profile from profiling. The inventory also classifies each source's role: system of entry (where the data is first created), system of record (the authoritative home for an attribute), or downstream consumer. Without the inventory, MDM projects fail in predictable ways: a forgotten marketing spreadsheet keeps injecting duplicates, or two systems both claim to be the authority for product prices and nobody can adjudicate. The inventory is a living document - every new integration, acquisition, or shadow-IT discovery updates it - and the registry's ingestion pipelines are generated from it.""",
how_it_works="""Building the inventory starts with discovery: interviews with system owners, scans of integration middleware, and reviews of data-warehouse feeds surface candidate sources. Each candidate is assessed: which domains it touches, which attributes it can contribute, its volume and velocity, its access method, and its owner. Profiling runs against a sample to establish the trust baseline. The source is then registered with a role per attribute - entry, record, or consumer - and an ingestion connector is configured from the recorded access method. Quarterly, the inventory is re-verified: owners confirm their systems still feed the registry, dead feeds are retired, and new shadow sources found by lineage analysis are onboarded or shut down.""",
key_points=[
 "Inventory records every system holding master data: owner, domains, volume, access, cadence.",
 "Each source gets a role per attribute: system of entry, system of record, or consumer.",
 "Forgotten shadow sources are the top cause of duplicate injection.",
 "The inventory is living: updated on every integration, acquisition, or discovery.",
 "Ingestion pipelines are generated from the inventory, not hand-wired per source."],
requirements=[
 "Discovery across applications, files, feeds, and partners.",
 "Per-source, per-attribute role classification.",
 "Profiling baselines establishing initial trust per source.",
 "Quarterly re-verification and retirement of dead feeds."],
standards=[
 "DAMA-DMBOK data integration and interoperability guidance.",
 "ISO/IEC 11179 for describing source metadata."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Inmon W, Linstedt D. Data Architecture: A Primer. Technics Publications, 2014."],
sig_lens="""The Signature reading: the inventory is the registry's census of the realm. Every system that claims knowledge of a customer or product must present itself, declare its role, and submit to measurement - no shadow source rules in the dark in the Signature network.""",
demo_data={"attributes":[
 {"name":"authoritative_source","candidates":[
   {"source":"Inventory","value":"Billing:system-of-record","trust":0.96,"recency_days":2},
   {"source":"Inventory","value":"CRM:system-of-entry","trust":0.9,"recency_days":2},
   {"source":"Inventory","value":"Spreadsheet:shadow","trust":0.3,"recency_days":60}],
  "expected":"Billing:system-of-record"}]},
),
dict(
name="Trust and Recency Signals",
group="Identity Foundations", ladder_rank=11, ladder_tier="foundations",
description="""Survivorship needs a way to compare competing values, and trust and recency are the two universal signals. Trust measures how reliable a source is for an attribute: the billing system's tax IDs are trusted because they are verified at onboarding; a marketing import's emails are trusted less because they were scraped. Trust comes from profiling (completeness, validity), from process (verified at entry vs typed freehand), and from history (how often this source's values survive challenges). Recency measures how fresh the value is: a phone verified last week beats a phone verified three years ago, because people change numbers. The standard combination multiplies them with recency decay - trust divided by a decay function of age - so a highly trusted old value can still lose to a moderately trusted fresh one. Authority overrides are the exception path: for some attributes, a designated system of record always wins regardless of score, such as legal names from the billing system. Every signal used is recorded in provenance so a steward can see exactly why a value won.""",
how_it_works="""Each source-attribute pair carries a trust score between 0 and 1, seeded from profiling metrics and process knowledge, then updated from steward decisions: every time a steward overrides the automated winner, the winner's source gains trust and the loser's loses a little. Recency is computed from the value's last-verified timestamp with an exponential or hyperbolic decay - the half-life differs by attribute (phones decay fast, birth dates never decay). The survivorship score is trust times the recency factor, and the highest score wins the attribute. Authority rules are checked first: if the attribute has a designated system of record and that system has a non-null value, it wins outright. The full score breakdown is stored with the golden record so decisions are explainable.""",
key_points=[
 "Trust: how reliable a source is for an attribute, from profiling, process, and history.",
 "Recency: how fresh the value is, with per-attribute decay rates.",
 "Survivorship score combines trust and recency; highest wins.",
 "Authority overrides let designated systems of record win outright.",
 "Steward overrides feed back into trust scores, so the system learns."],
requirements=[
 "Trust scores per source-attribute pair, seeded from profiling.",
 "Last-verified timestamps on values for recency computation.",
 "Per-attribute decay rates and authority designations.",
 "Score breakdowns stored in provenance for explainability."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "W3C PROV for provenance of survivorship decisions."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013."],
sig_lens="""The Signature reading: trust and recency are the registry's scales of testimony. The Signature registry weighs each witness by proven reliability and by how recently they saw the fact - and it writes the weighing on the record, so no verdict is ever a mystery.""",
demo_data={"attributes":[
 {"name":"email","candidates":[
   {"source":"CRM","value":"ada@example.com","trust":0.92,"recency_days":3},
   {"source":"Billing","value":"ada@example.com","trust":0.88,"recency_days":12},
   {"source":"Legacy","value":"ada@oldmail.com","trust":0.55,"recency_days":400}],
  "expected":"ada@example.com"}]},
),
dict(
name="Survivorship Rules",
group="Identity Foundations", ladder_rank=12, ladder_tier="foundations",
description="""Survivorship rules decide, attribute by attribute, which source's value becomes the golden record's value. The simplest rule is most-recent-wins: the freshest non-null value takes the attribute. The most common is most-trusted-wins: the value from the highest-scoring source takes it. Real registries layer them: authority rules first (billing always wins legal name), then completeness rules (prefer the value with the most corroboration across sources), then trust-times-recency scoring, then deterministic tie-breakers (lowest source ID, so reruns are stable). Rules can also compose values rather than pick one: concatenate address lines from different sources, or take the longest non-abbreviated name. Every rule is versioned and effective-dated, because changing a rule changes golden records - and the registry must be able to explain why a customer's email changed on a given date by pointing at the rule version that was active. Rule changes are simulated against history before activation, so their blast radius is known in advance.""",
how_it_works="""Rules are authored per domain and per attribute in a rule table: attribute, priority order of rule types, parameters (decay rates, authority source, tie-breakers). The survivorship engine evaluates rules in priority order for each attribute of each entity cluster. First-match rules (authority) short-circuit; scoring rules compute trust-times-recency for every candidate and take the max; composition rules merge candidates field-wise. Before a rule change goes live, the engine replays it over a historical snapshot and reports how many golden records would change and which attributes - the blast-radius report. Approved changes are versioned with effective dates, and the golden record's provenance cites the exact rule version that produced each value.""",
key_points=[
 "Rules are per attribute: authority first, then scoring, then tie-breakers.",
 "Common rules: most-recent-wins, most-trusted-wins, most-corroborated-wins.",
 "Composition rules merge values field-wise instead of picking one winner.",
 "Rule versions are effective-dated; provenance cites the exact version.",
 "Rule changes are simulated against history to measure blast radius before activation."],
requirements=[
 "A rule table per domain and attribute with priority ordering.",
 "Versioning and effective dating for every rule.",
 "Blast-radius simulation before rule activation.",
 "Provenance linking each surviving value to its rule version."],
standards=[
 "ISO 8000 for master-data quality rules.",
 "DAMA-DMBOK data quality guidance."],
citations=[
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: survivorship rules are the registry's laws of succession - written, versioned, and applied equally to every entity. When the Signature registry changes a law, it first shows the realm what would change, then enacts, then records which law crowned each value.""",
demo_data={"attributes":[
 {"name":"legal_name","candidates":[
   {"source":"Billing","value":"Ada Lovelace","trust":0.88,"recency_days":60},
   {"source":"CRM","value":"Ada Lovelace","trust":0.97,"recency_days":2}],
  "expected":"Ada Lovelace"}]},
),
]
