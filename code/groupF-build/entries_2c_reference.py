#!/usr/bin/env python3
"""Reference Data Registry entries 25-34 (advanced)."""

APPEND = [
dict(
name="Multi-Standard Harmonization",
group="Advanced Registry Topics", ladder_rank=25, ladder_tier="advanced",
description="""Real enterprises live under several standards at once: NAICS for US reporting, ISIC for international reporting, NACE for European reporting - three industry classifications that must reconcile. Harmonization builds the concordance layer that lets data coded in any of them translate to the others with documented fidelity. The work starts with pairwise crosswalks, then resolves the hard rows where standards slice the world differently: one standard's single category maps to another's three, or two standards draw their boundary in different places. Those rows get explicit many-to-many mappings with allocation rules (split by revenue share, by headcount, or flag as unallocatable). The harmonized layer publishes a canonical industry concept each standard maps into, so analytics can aggregate across standards without pretending the mappings are exact. Maintenance is the long game: every standards release on any side re-opens the affected rows, and the harmonization board - stewards from each standard's community - adjudicates.""",
how_it_works="""The harmonization registry defines canonical concepts independent of any single standard, then maps each standard's codes into them with relationship types and allocation rules for many-to-many rows. Translation services resolve through the canonical layer: any-to-any translation becomes any-to-canonical plus canonical-to-any. Allocation rules handle splits - by declared shares, by measured shares from reference data, or flagged unallocatable for analyst judgment. On any standard's release, affected mappings enter re-validation and the harmonization board reviews boundary changes. Coverage and fidelity metrics per standard pair show where translation is exact and where it is approximate, and consumers see the fidelity flags on translated data.""",
key_points=[
 "Harmonization maps multiple standards into shared canonical concepts.",
 "Many-to-many rows get allocation rules or unallocatable flags - never silent splits.",
 "Any-to-any translation routes through the canonical layer.",
 "Boundary differences between standards are documented, not hidden.",
 "A harmonization board adjudicates on every standards release."],
requirements=[
 "Canonical concept layer independent of individual standards.",
 "Mappings with relationship types and allocation rules.",
 "Fidelity flags on all translated data.",
 "Board governance with re-validation on releases."],
standards=[
 "W3C SKOS mapping properties.",
 "ISO/IEC 11179 for mapping metadata."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "United Nations. ISIC Rev.4 explanatory notes. UN Statistics Division."],
sig_lens="""The Signature reading: harmonization is the registry's peace treaty among rival maps of the world - each standard honored, their differences charted openly, translations flagged where the terrain is disputed. The Signature registry never fakes agreement where cartographers disagree.""",
demo_data={"lists":[
 {"name":"industry_harmony","codes":[
   {"code":"NAICS-541512","label":"harmonized: exact","status":"active"},
   {"code":"ISIC-6202","label":"harmonized: exact","status":"active"},
   {"code":"SIC-7376","label":"superseded by NAICS","status":"deprecated"}],
  "checks":["NAICS-541512","SIC-7376","XYZ-1"],"expected":["NAICS-541512:active","SIC-7376:deprecated","XYZ-1:unknown"]}]},
),
dict(
name="Semantic Mapping with SKOS and OWL",
group="Advanced Registry Topics", ladder_rank=26, ladder_tier="advanced",
description="""Beyond code-to-code translation, semantic mapping expresses how concepts relate using web standards: SKOS for vocabularies, OWL for ontologies. SKOS gives the mapping relations - exactMatch, closeMatch, broadMatch, narrowMatch, relatedMatch - with defined semantics that machines can reason over: exactMatch is transitive, so A exactMatch B and B exactMatch C implies A exactMatch C. OWL goes further, declaring classes, properties, and restrictions: a PurchaseOrder must have exactly one orderDate, a Customer is disjoint from a Product. Reasoners then check consistency - flagging a vocabulary that declares something both a Customer and a Product - and infer new facts, like classifying items under ancestor categories automatically. The registry uses SKOS for vocabulary mappings and OWL where the domain needs logical rigor (regulatory classifications, product safety categories). The investment pays off in interoperability: systems that understand SKOS/OWL can consume the registry's vocabularies without custom integration code.""",
how_it_works="""Vocabularies publish in SKOS (concepts, labels, broader/narrower/related, mappings) and, where needed, OWL ontologies (classes, properties, restrictions, disjointness). A reasoner validates each release: consistency checks catch contradictions, classification infers ancestor memberships, and the inferred triples publish alongside the asserted ones. Mapping properties carry their formal semantics - transitivity of exactMatch is exploited to compose crosswalks automatically. Consumers fetch the RDF serializations (Turtle, JSON-LD) and load them into triple stores or reason over them in application code. Ontology changes go through the same request-review-publish workflow as code lists, with the reasoner's report attached to every release.""",
key_points=[
 "SKOS mapping relations have machine-reasonable semantics (exactMatch is transitive).",
 "OWL adds classes, restrictions, and consistency checking for rigorous domains.",
 "Reasoners validate releases and infer ancestor classifications automatically.",
 "RDF serializations (Turtle, JSON-LD) make vocabularies consumable without custom code.",
 "Ontology changes carry the reasoner's report through the standard workflow."],
requirements=[
 "SKOS publication for vocabularies; OWL where logical rigor is needed.",
 "Reasoner validation on every release with published reports.",
 "RDF serializations for machine consumption.",
 "Change workflow with reasoning reports attached."],
standards=[
 "W3C SKOS, OWL 2, RDF 1.1.",
 "W3C PROV-O for mapping provenance."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "W3C. OWL 2 Web Ontology Language Document Overview. W3C Recommendation, 2012."],
sig_lens="""The Signature reading: semantic mapping is the registry teaching machines the logic of meaning - not just that these words match, but how, and what follows. The Signature registry's vocabularies can be reasoned over, and every reasoning is checked before it is published.""",
demo_data={"lists":[
 {"name":"skos_map","codes":[
   {"code":"exactMatch","label":"SKOS exact mapping relation","status":"active"},
   {"code":"broadMatch","label":"SKOS broader mapping relation","status":"active"},
   {"code":"myMatch","label":"Ad-hoc relation (use SKOS instead)","status":"deprecated"}],
  "checks":["exactMatch","myMatch","fuzzyMatch"],"expected":["exactMatch:active","myMatch:deprecated","fuzzyMatch:unknown"]}]},
),
dict(
name="Multilingual Labels",
group="Advanced Registry Topics", ladder_rank=27, ladder_tier="advanced",
description="""A global network needs every code labeled in every language its users speak: the country list in English, French, Arabic, and Pashto; product categories in the languages of each market. Multilingual labels are reference data with language tags: each label carries its BCP 47 tag, and one label per language is marked preferred. Translation is steward-reviewed, not machine-dumped - a mistranslated country name is a diplomatic incident and a mistranslated medical code is a safety incident. Scripts and direction matter: Arabic labels need right-to-left handling, and some languages need different labels by region (Spanish for Spain vs Mexico). Fallback chains handle missing translations: show the label in the user's language, else the regional variant, else English, else the code itself - never a blank. Translation memory keeps labels consistent across lists, and every label carries its translator, reviewer, and date for accountability.""",
how_it_works="""The label store holds code, language tag, label text, preferred flag, translator, reviewer, and date. Translation workflows route new codes to translators per language, then to reviewers; machine translation may draft but never publishes unreviewed. Fallback chains resolve at display time: requested language, then regional variants, then the list's default language, then the code. Right-to-left scripts get direction metadata so interfaces render correctly. Translation memory suggests consistent phrasing across lists, and glossary terms (official country names, regulated terms) are locked against free translation. Coverage dashboards show per-language label completeness per list, driving translation priorities.""",
key_points=[
 "Every label carries a BCP 47 tag; one preferred label per language.",
 "Translations are steward-reviewed; machine drafts never publish unreviewed.",
 "Fallback chains guarantee a display string: language, variant, default, code.",
 "Script direction metadata ensures correct rendering.",
 "Coverage dashboards drive translation priorities per list and language."],
requirements=[
 "Label stores with language tags, preferred flags, and translator provenance.",
 "Translation plus review workflows per language.",
 "Fallback chains with no-blank guarantees.",
 "Coverage dashboards per list and language."],
standards=[
 "BCP 47 language tags.",
 "W3C SKOS-XL for multilingual labels."],
citations=[
 "Phillips A, Davis M. BCP 47: Tags for Identifying Languages. IETF, 2009.",
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009."],
sig_lens="""The Signature reading: multilingual labels are the registry speaking every tongue with care - each translation reviewed by human eyes, each script honored, no user ever shown a blank. The Signature registry counts translation coverage the way generals count supplies.""",
demo_data={"lists":[
 {"name":"labels","codes":[
   {"code":"lbl-en","label":"English label present","status":"active"},
   {"code":"lbl-ps","label":"Pashto label present","status":"active"},
   {"code":"lbl-mt","label":"Machine draft unreviewed","status":"deprecated"}],
  "checks":["lbl-en","lbl-mt","lbl-xx"],"expected":["lbl-en:active","lbl-mt:deprecated","lbl-xx:unknown"]}]},
),
dict(
name="Reference Data Quality Metrics",
group="Advanced Registry Topics", ladder_rank=28, ladder_tier="advanced",
description="""Reference data quality is measured on its own dimensions. Definition coverage: what share of codes have real definitions (not one-word placeholders). Deprecation hygiene: are deprecated codes actually draining out of feeds, or are sources ignoring the notices? Mapping coverage: what share of local codes map to canonical? Version currency: how many consumers validate against stale versions? Translation coverage: per language, per list. Consistency: do hierarchy codes' parents all exist, do effective periods tile without gaps? Each metric has a target and a trend, reported per list and rolled up to registry health. The metrics that move decisions are the consumer-facing ones: validation rejection rates (bad codes blocked at the door), translation fallback rates (labels missing), and stale-consumer counts. A reference registry that nobody measures rots quietly; a measured one improves every quarter because the numbers point at exactly what to fix.""",
how_it_works="""Quality jobs compute the dimension metrics per list on schedules: definition coverage from text analysis, deprecation drain from feed monitoring, mapping coverage from mapping tables, version currency from consumer declarations, translation coverage from label stores, consistency from structural validators. Metrics land in a quality store with targets and alert thresholds; steward dashboards show per-list health and trends. Consumer-facing metrics - rejection rates, fallback rates, stale counts - page the responsible teams. Quarterly quality reviews retire metrics nobody acts on and promote the ones that changed behavior; the review also sets next quarter's improvement targets from the current baselines.""",
key_points=[
 "Dimensions: definition coverage, deprecation hygiene, mapping coverage, version currency, translation coverage, consistency.",
 "Consumer-facing metrics (rejections, fallbacks, stale consumers) move decisions.",
 "Targets and trends per list, rolled up to registry health.",
 "Metrics nobody acts on are retired; metrics that change behavior are promoted.",
 "Measured registries improve quarterly; unmeasured ones rot quietly."],
requirements=[
 "Scheduled quality jobs per list writing to a quality store.",
 "Targets and alert thresholds per metric with owner paging.",
 "Steward dashboards with per-list health and trends.",
 "Quarterly metric reviews with improvement targets from baselines."],
standards=[
 "ISO 8000-8 for information quality measurement.",
 "DAMA-DMBOK data quality guidance."],
citations=[
 "Olson J. Data Quality: The Accuracy Dimension. Morgan Kaufmann, 2003.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: quality metrics are the registry's annual inspection of its own armory - every definition checked, every deprecated code accounted for, every translation counted. The Signature registry inspects itself the way it inspects others: without mercy, on schedule.""",
demo_data={"lists":[
 {"name":"quality","codes":[
   {"code":"DEF-OK","label":"Definition coverage 98pct","status":"active"},
   {"code":"MAP-OK","label":"Mapping coverage 96pct","status":"active"},
   {"code":"STALE","label":"Stale metric, retired","status":"deprecated"}],
  "checks":["DEF-OK","STALE","VANITY"],"expected":["DEF-OK:active","STALE:deprecated","VANITY:unknown"]}]},
),
dict(
name="Federation of Registries",
group="Advanced Registry Topics", ladder_rank=29, ladder_tier="advanced",
description="""No single registry owns all reference data: countries maintain their own subdivision lists, industries maintain their product classifications, each database community curates its own vocabularies. Federation lets registries interoperate without centralizing: each registry stays authoritative for its lists, publishes them in standard formats (SKOS, CSV, API), and federates through a shared catalog that indexes what exists where. Cross-registry mappings link equivalent lists, and a trust framework records which registries' lists each consumer accepts. The federation's hard problems are identity (is registry A's country list the same list as registry B's, or a fork?), change propagation (when A releases v4, how do B's mappings update?), and dispute resolution (two registries define the same code differently). The federation answers with list identifiers, subscription-based change feeds, and a mapping board - the same patterns as a single registry, scaled to a network of peers.""",
how_it_works="""Each member registry publishes a feed of its lists with identifiers, versions, and checksums to the federation catalog. The catalog indexes by subject so consumers can discover lists across registries. Cross-registry mappings are authored like crosswalks, versioned against both lists' versions. Change subscriptions propagate releases: when a registry publishes, subscribed mappings enter re-validation and subscribed consumers get notified. List identifiers distinguish forks from shared lists; forks carry their lineage (forked from list X at version Y). The mapping board adjudicates definition disputes with published decisions. Trust frameworks let consumers declare accepted registries, and validation services check codes against the union of accepted lists.""",
key_points=[
 "Federation: autonomous registries, shared catalog, standard publication formats.",
 "Each registry stays authoritative for its own lists; the catalog indexes what exists where.",
 "List identifiers distinguish shared lists from forks.",
 "Change subscriptions propagate releases to mappings and consumers.",
 "Trust frameworks let consumers declare which registries they accept."],
requirements=[
 "Publication feeds with list identifiers, versions, checksums.",
 "A shared catalog with subject indexing.",
 "Cross-registry mappings with re-validation on releases.",
 "A mapping board for definition disputes."],
standards=[
 "W3C SKOS for vocabulary interchange.",
 "ISO/IEC 11179 for registry metadata."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: federation is the registry's league of sovereign vocabularies - each ruling its own lists, all discoverable in one catalog, disputes settled by published precedent. The Signature league centralizes nothing and standardizes everything that matters.""",
demo_data={"lists":[
 {"name":"federation","codes":[
   {"code":"FED-MEMBER","label":"Member registry, current","status":"active"},
   {"code":"FED-OBSERVER","label":"Observer registry","status":"active"},
   {"code":"FED-SUSPENDED","label":"Membership suspended","status":"deprecated"}],
  "checks":["FED-MEMBER","FED-SUSPENDED","FED-ROGUE"],"expected":["FED-MEMBER:active","FED-SUSPENDED:deprecated","FED-ROGUE:unknown"]}]},
),
dict(
name="Reference Data for a Million-Database Network",
group="Advanced Registry Topics", ladder_rank=30, ladder_tier="advanced",
description="""A million databases share one vocabulary problem at planetary scale: every database needs country codes, units, statuses, and languages, and they must all mean the same things. The network's reference layer answers with a global core - the few hundred lists every database needs, governed globally, distributed through edge caches - plus community extensions curated by database communities for their domains. Identity is content-based: each list version is hashed, and databases pin hashes, so a database in 2030 can prove it validated against the exact bytes of the 2026 country list. Distribution is peer-assisted: databases seed list versions to neighbors, with the registry's signed releases as the trust anchor. Local needs are honored through the extension process: a database community proposes codes, the global stewards check for collisions with the core, and approved extensions publish as namespaced community lists. The result is one vocabulary with local dialects - exactly the canonical-vs-local pattern, scaled to a million.""",
how_it_works="""The global core publishes signed, content-hashed list versions through edge caches and peer seeding. Databases declare their pinned versions per list; validation stamps the hash. Community extensions go through proposal, collision-check against the core, and publication as namespaced lists with their own stewards. Change propagation uses the subscription model: databases subscribe to their lists and receive release notifications with diffs. Offline databases operate from pinned snapshots and reconcile on reconnection, with the hash pins making divergence detectable. The federation catalog indexes community lists so databases can discover and adopt each other's extensions, and popular extensions graduate to the core by the same bar as any list.""",
key_points=[
 "Global core lists for universal needs, community extensions for domain needs.",
 "Content-hashed versions let databases prove exactly what they validated against.",
 "Signed releases anchor trust; peer seeding distributes at scale.",
 "Community extensions are namespaced, stewarded, and collision-checked.",
 "Offline databases pin snapshots and reconcile on reconnection with detectable divergence."],
requirements=[
 "Signed, content-hashed global core list versions.",
 "Edge caching plus peer-assisted distribution.",
 "Community extension process with core collision checks.",
 "Pinned-version declarations with hash verification."],
standards=[
 "W3C SKOS for interchange.",
 "ISO/IEC 11179 for registry metadata."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: the network's reference layer is one tongue for a million archives - the core vocabulary sworn globally, dialects curated locally, every edition hashed and signed. The Signature network speaks with one voice and a million accents, and proves every word.""",
demo_data={"lists":[
 {"name":"network_core","codes":[
   {"code":"CORE-COUNTRY","label":"Global core list","status":"active"},
   {"code":"COMM-MED-42","label":"Community extension, medical","status":"active"},
   {"code":"COMM-OLD-7","label":"Withdrawn community list","status":"deprecated"}],
  "checks":["CORE-COUNTRY","COMM-OLD-7","CORE-XXXX"],"expected":["CORE-COUNTRY:active","COMM-OLD-7:deprecated","CORE-XXXX:unknown"]}]},
),
dict(
name="Emergency Code Extensions",
group="Advanced Registry Topics", ladder_rank=31, ladder_tier="advanced",
description="""Sometimes the world does not wait for the release schedule: a new disease needs a code today, a currency redenominates Friday, a disaster creates new aid categories overnight. Emergency extensions add codes on an expedited path - hours, not weeks - with the same paperwork done fast: justification, definition, steward approval, provisional status, and a sunset review date. Provisional codes are namespaced or flagged so consumers know they are temporary; the sunset review either promotes them to full codes, replaces them with the proper standard's codes when those publish, or retires them with mappings to the replacements. The registry's emergency playbook names who can declare an emergency, what evidence is required, and how consumers are notified within the hour. Abuse is prevented by the sunset: every emergency code faces its review, and codes that bypassed diligence get extra scrutiny, not a free pass.""",
how_it_works="""The emergency path compresses the standard workflow: a declaration with evidence, steward approval (with a designated emergency deputy if the steward is unreachable), provisional publication with flagged status, and immediate consumer notification. Provisional codes carry sunset dates - typically 90 days - at which a review decides: promote, replace with the standard's official codes, or retire with mappings. Consumers treat provisional codes as valid but volatile: they may appear in data and must resolve, but reports flag their provisional share. The post-emergency review examines whether the emergency was genuine and whether the process held; repeated false emergencies cost the declarer their declaration rights.""",
key_points=[
 "Emergency extensions publish in hours with the same paperwork, done fast.",
 "Provisional codes are flagged and carry sunset review dates.",
 "Sunset review: promote, replace with official codes, or retire with mappings.",
 "Consumers treat provisional codes as valid but volatile.",
 "Post-emergency reviews check the process held; false emergencies have consequences."],
requirements=[
 "An emergency declaration playbook with authority and evidence rules.",
 "Provisional publication with flagged status and sunset dates.",
 "Immediate consumer notification channels.",
 "Mandatory sunset reviews with promote/replace/retire outcomes."],
standards=[
 "ISO/IEC 11179 for provisional metadata.",
 "DAMA-DMBOK data governance guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "World Health Organization. ICD emergency code procedures."],
sig_lens="""The Signature reading: emergency extensions are the registry's wartime powers - swift, flagged, and sun-setted by law. The Signature registry moves fast in crisis but never in secret, and every emergency power expires on schedule or answers for itself.""",
demo_data={"lists":[
 {"name":"emergency","codes":[
   {"code":"EMG-2026-001","label":"Provisional emergency code","status":"active"},
   {"code":"EMG-2024-014","label":"Promoted to full code","status":"active"},
   {"code":"EMG-2023-002","label":"Sunset retired","status":"deprecated"}],
  "checks":["EMG-2026-001","EMG-2023-002","EMG-9999"],"expected":["EMG-2026-001:active","EMG-2023-002:deprecated","EMG-9999:unknown"]}]},
),
dict(
name="Provenance of Reference Lists",
group="Advanced Registry Topics", ladder_rank=32, ladder_tier="advanced",
description="""Every reference list should be able to answer: where did these codes come from, who defined them, what changed and when, and why should I trust them? Provenance records the list's lineage: the source standard or authority it derives from, the extraction or authoring process, the stewards who approved each version, the change requests behind each diff, and the evidence for disputed definitions. For lists derived from external standards (ISO country codes from the ISO maintenance agency), provenance cites the source edition and the sync process. For authored lists (internal product categories), provenance records the authoring methodology and the approval chain. Provenance is what makes a list auditable: a regulator asking why this transaction validated can follow the chain from the validation verdict to the list version to the change request to the steward who approved it. Lists without provenance are rumors; lists with provenance are evidence.""",
how_it_works="""Each list carries a provenance record: origin (source standard edition or authoring methodology), derivation process, steward chain, and per-version change-request links. Sync processes log each external update with the source edition and the diff applied. Authored lists attach their methodology documents and approval records. A provenance query API answers where-did-this-code-come-from with the full chain, and validation verdicts optionally embed provenance pointers. Provenance records are immutable and versioned alongside the lists they describe; when a list is forked, the fork's provenance cites the parent list and version.""",
key_points=[
 "Provenance answers: source, authoring process, approvers, changes, trust basis.",
 "Derived lists cite source editions and sync processes; authored lists cite methodology.",
 "Validation verdicts can embed provenance pointers for auditability.",
 "Provenance makes lists evidence instead of rumors.",
 "Forks cite their parent list and version in their provenance."],
requirements=[
 "Provenance records per list: origin, process, steward chain, change links.",
 "Sync logging with source editions and applied diffs.",
 "Provenance query APIs and verdict-embedded pointers.",
 "Immutable, versioned provenance with fork lineage."],
standards=[
 "W3C PROV-O for provenance modeling.",
 "ISO/IEC 11179 for registry metadata."],
citations=[
 "W3C. PROV-O: The PROV Ontology. W3C Recommendation, 2013.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: provenance is each list's birth certificate and family record - source named, authors sworn, every change with its reason. The Signature registry accepts no anonymous words into its vocabulary.""",
demo_data={"lists":[
 {"name":"provenance","codes":[
   {"code":"PROV-SYNCED","label":"Synced from ISO edition 2024","status":"active"},
   {"code":"PROV-AUTHORED","label":"Authored, methodology attached","status":"active"},
   {"code":"PROV-RUMOR","label":"Unsourced list, do not use","status":"deprecated"}],
  "checks":["PROV-SYNCED","PROV-RUMOR","PROV-X"],"expected":["PROV-SYNCED:active","PROV-RUMOR:deprecated","PROV-X:unknown"]}]},
),
dict(
name="Audit and Compliance Reporting",
group="Advanced Registry Topics", ladder_rank=33, ladder_tier="advanced",
description="""Regulators and auditors ask hard questions about reference data: prove that this transaction validated against the approved list version; show who approved the code definition it used; demonstrate that deprecated codes are blocked for new data. The registry answers with compliance reports generated from its versioned, provenanced, logged stores: validation verdicts stamped with list versions, change-request histories, steward approval records, deprecation notices and their consumer acknowledgments, and feed-monitoring evidence that deprecated codes are draining. Reports are produced per regulation: financial reporting needs code-version pinning for the reporting period; medical coding needs definition-approval chains; data-protection audits need evidence that retention codes are enforced. The reports are themselves versioned artifacts - an auditor rerunning last year's report gets last year's numbers - because compliance evidence must be reproducible.""",
how_it_works="""Compliance report templates define the evidence per regulation: version pins, approval chains, deprecation enforcement, feed monitoring. Report jobs query the registry's versioned stores as-of the reporting period, assembling the evidence into signed report artifacts with hashes. Auditors get read access to the underlying versioned data to verify the reports independently. Consumer acknowledgment tracking records which consumers confirmed deprecation notices, closing the loop on enforcement. Report artifacts are retained per the regulation's own retention schedule, and reruns against the same as-of date reproduce byte-identical reports.""",
key_points=[
 "Compliance reports prove version pins, approvals, and deprecation enforcement.",
 "Evidence comes from versioned, provenanced, logged stores - as-of the period.",
 "Templates per regulation: financial, medical, data-protection each need different proof.",
 "Consumer acknowledgment tracking closes the deprecation enforcement loop.",
 "Reports are versioned artifacts; reruns reproduce identical evidence."],
requirements=[
 "Compliance report templates per applicable regulation.",
 "As-of querying over versioned registry stores.",
 "Signed, hash-verified report artifacts with retention.",
 "Consumer acknowledgment tracking for notices."],
standards=[
 "ISO/IEC 11179 for metadata evidence.",
 "W3C PROV-O for provenance evidence."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "ISO/IEC 27001. Information security management. ISO."],
sig_lens="""The Signature reading: compliance reports are the registry testifying under oath - version pins shown, approvers named, enforcement demonstrated, every claim reproducible. The Signature registry keeps its evidence the way courts keep exhibits: sealed, dated, and ready.""",
demo_data={"lists":[
 {"name":"compliance","codes":[
   {"code":"RPT-SIGNED","label":"Signed compliance report","status":"active"},
   {"code":"RPT-DRAFT","label":"Draft report, unsigned","status":"active"},
   {"code":"RPT-VOID","label":"Superseded report","status":"deprecated"}],
  "checks":["RPT-SIGNED","RPT-VOID","RPT-X"],"expected":["RPT-SIGNED:active","RPT-VOID:deprecated","RPT-X:unknown"]}]},
),
dict(
name="Reference Data Registry Mastery Review",
group="Advanced Registry Topics", ladder_rank=34, ladder_tier="advanced",
description="""The mastery review binds the ladder. Foundations: reference data is the shared vocabulary - code lists with defined values, controlled vocabularies with preferred terms, taxonomies with single-parent trees, hierarchical codes with structural validity; units of measure with UCUM codes and SI conversions; ISO 4217 currencies with minor-unit exponents, ISO 3166 countries with three code forms, ISO 639 languages with BCP 47 tags; date conventions with ISO 8601 and IANA zones; lifecycle status codes as governed state machines; mapping tables translating between code sets with fidelity flags. Compounded: crosswalks between standards, independent versioning with release batching, deprecation with successor chains, effective dating with as-of queries, canonical-vs-local containment, stewardship by subject experts, change requests as legislation, multi-channel publication, runtime APIs, caching with fallback discipline, and ingestion validation at the door. Advanced: multi-standard harmonization, SKOS/OWL semantic mapping, multilingual labels, quality metrics, federation of registries, the million-database network core, emergency extensions, provenance, and compliance reporting. The creed: one vocabulary, versioned always, defined everywhere, trusted by all.""",
how_it_works="""The review serves as capstone assessment and deployment checklist. As an assessment: can the team define every list, demonstrate versioning, show deprecation chains, prove validation at ingestion, and produce compliance evidence? As a checklist: catalog complete, stewards named, versions pinned, APIs serving, caches warm, fallbacks tested, metrics owned, federation joined. Gaps become the next quarter's program of work. The review repeats annually because vocabularies drift and the network grows - mastery is maintained, not achieved once.""",
key_points=[
 "Foundations: code lists, vocabularies, taxonomies, units, ISO standards, dates, statuses, mappings.",
 "Compounded: crosswalks, versioning, deprecation, effective dating, stewardship, publication, APIs, validation.",
 "Advanced: harmonization, semantics, multilinguality, metrics, federation, network core, provenance, compliance.",
 "The creed: one vocabulary, versioned always, defined everywhere, trusted by all.",
 "Annual review: mastery is maintained, not achieved once."],
requirements=[
 "Demonstrated competence at every rung before registry launch.",
 "Checklist rerun on major changes and annually.",
 "Gaps converted to funded program work."],
standards=[
 "ISO/IEC 11179 series.",
 "W3C SKOS."],
citations=[
 "ISO/IEC 11179 (series). Metadata registries. International Organization for Standardization.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: the mastery review is the registry's graduation in the science of true names. The Signature graduate can define every code, version every list, retire every word with honor, and swear the creed: one vocabulary, versioned always, defined everywhere, trusted by all.""",
demo_data={"lists":[
 {"name":"mastery","codes":[
   {"code":"RUNG-34","label":"All rungs complete","status":"active"},
   {"code":"RUNG-PARTIAL","label":"Partial completion","status":"deprecated"}],
  "checks":["RUNG-34","RUNG-PARTIAL","RUNG-X"],"expected":["RUNG-34:active","RUNG-PARTIAL:deprecated","RUNG-X:unknown"]}]},
),
]
