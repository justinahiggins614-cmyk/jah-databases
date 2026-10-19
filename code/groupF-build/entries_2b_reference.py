#!/usr/bin/env python3
"""Reference Data Registry entries 13-34 (compounded + advanced)."""

APPEND = [
dict(
name="Crosswalks Between Standards",
group="Registry Governance", ladder_rank=13, ladder_tier="compounded",
description="""A crosswalk is a published, governed mapping between two standards: ICD-10 to SNOMED CT for diagnoses, NAICS to ISIC for industries, UNSPSC to eCl@ss for product categories. Crosswalks differ from ad-hoc mapping tables in their authority and maintenance: they are published artifacts with versions, stewards, documented methodology, and change logs, often maintained by the standards bodies themselves or by recognized authorities. Using an authoritative crosswalk beats building your own - the methodology has been reviewed, edge cases documented, and updates ship with each standards release. Crosswalks carry the same relationship discipline as mappings: exact, broader, narrower, related, with confidence and notes on the tricky rows. The registry curates the crosswalks its network needs, versions them against both standards' releases, and publishes translation services over them - so a hospital coding in ICD-10 and a research database in SNOMED CT can share data without either side maintaining a private translation.""",
how_it_works="""The registry's crosswalk catalog lists each crosswalk with its source and target standards and versions, publisher, methodology notes, and update cadence. Crosswalk rows are ingested with relationship types and confidence; translation services expose them as APIs (translate this code, list candidates with confidence, explain the tricky rows). On either standard's new release, the crosswalk enters re-validation: new codes need rows, retired codes need successor handling, and confidence is rechecked. Consumers declare which crosswalk version they translate with, and translated records carry that version. Where no authoritative crosswalk exists, the registry charters one: methodology review, dual-author mapping, sampled validation, then publication as a versioned artifact.""",
key_points=[
 "Crosswalks are authoritative, published, versioned mappings between standards.",
 "Prefer authoritative crosswalks over private ad-hoc mappings.",
 "Relationship types and confidence on every row; tricky rows documented.",
 "Re-validated on each standards release on either side.",
 "Translated records declare the crosswalk version used."],
requirements=[
 "A crosswalk catalog with publisher, methodology, and cadence per crosswalk.",
 "Translation APIs with confidence and explanation.",
 "Re-validation workflow on standards releases.",
 "Chartering process for crosswalks that do not exist yet."],
standards=[
 "W3C SKOS mapping properties.",
 "ISO/IEC 11179 for mapping metadata."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "National Library of Medicine. UMLS Metathesaurus crosswalk documentation."],
sig_lens="""The Signature reading: crosswalks are the registry's sworn bridges between kingdoms of meaning - built by recognized engineers, inspected on every standards release, each plank labeled with its load rating. The Signature registry builds bridges once, well, for all to cross.""",
demo_data={"lists":[
 {"name":"icd_snomed","codes":[
   {"code":"J45.0","label":"maps to SNOMED 195967001","status":"active"},
   {"code":"E11","label":"maps to SNOMED 44054006","status":"active"},
   {"code":"799.9","label":"ICD-9 legacy, no direct map","status":"deprecated"}],
  "checks":["J45.0","799.9","Z99.9"],"expected":["J45.0:active","799.9:deprecated","Z99.9:unknown"]}]},
),
dict(
name="Versioning Reference Data",
group="Registry Governance", ladder_rank=14, ladder_tier="compounded",
description="""Reference data versions so consumers know exactly which list they validated against. The registry versions each list independently with semantic-style numbers: major for breaking changes (codes removed or redefined), minor for additions, patch for definition clarifications. Every version carries its effective date, its change log, and its predecessor link, forming a chain back to the list's first publication. Consumers declare the version they use - a 2024 tax filing validates against the 2024 country list even in 2026 - and the registry serves any published version on demand, so historical validation is reproducible. Version diffs are first-class: added codes, removed codes, redefined codes, moved hierarchy nodes, each with migration notes. The discipline that makes versioning work is release batching: changes accumulate in a draft and publish as one version on a schedule, instead of trickling out as silent edits that leave consumers validating against a moving target.""",
how_it_works="""Each list has a version chain: version number, effective date, change log, predecessor pointer, and the full code snapshot. Draft changes accumulate in a staging area; on the release schedule, the steward reviews the draft, the registry computes the diff against the current version, assigns the next number by change severity, and publishes. Consumers fetch lists by version or by as-of date; validation services stamp records with the version used. Diff reports show added/removed/redefined/moved codes with migration notes, and consumers subscribe to release notifications for the lists they depend on. Emergency patches follow the same pipeline on an expedited schedule - never as silent edits.""",
key_points=[
 "Independent semantic-style versioning per list: major/minor/patch by change severity.",
 "Every version: effective date, change log, predecessor link, full snapshot.",
 "Consumers declare versions; the registry serves any published version for reproducibility.",
 "Version diffs with migration notes are first-class artifacts.",
 "Changes batch into scheduled releases; silent edits are forbidden."],
requirements=[
 "Version chains with snapshots, changelogs, and predecessor links.",
 "Release schedules with draft staging and steward review.",
 "As-of-date and by-version retrieval for consumers.",
 "Diff reports with migration notes per release."],
standards=[
 "Semantic Versioning 2.0.0 (adapted).",
 "ISO/IEC 11179 for version metadata."],
citations=[
 "Preston-Werner T. Semantic Versioning 2.0.0.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: versioning is the registry's dated archive of every vocabulary - each edition complete, chained to its predecessor, servable forever. The Signature registry never edits a published word in place; it publishes a new edition and keeps the old.""",
demo_data={"lists":[
 {"name":"currency_v","codes":[
   {"code":"USD","label":"v3.2 active","status":"active"},
   {"code":"SLE","label":"v3.0 added (Sierra Leone redenomination)","status":"active"},
   {"code":"STD","label":"v2.0 replaced by STN","status":"deprecated"}],
  "checks":["USD","STD","SLE"],"expected":["USD:active","STD:deprecated","SLE:active"]}]},
),
dict(
name="Deprecation and Supersession",
group="Registry Governance", ladder_rank=15, ladder_tier="compounded",
description="""Deprecation retires a code without erasing it. A deprecated code stays in the registry with its definition, its history, and - crucially - its successor pointer: code SU is deprecated, superseded by RU, BY, and fifteen others. This is what lets historical data keep its meaning while new data uses the replacement. The deprecation lifecycle has stages: announced (the retirement is published with a date), deprecated (new uses are blocked, old uses still resolve), and eventually retired-from-active-lists while remaining resolvable in the archive. Supersession chains handle multi-hop history: A was superseded by B, B by C - the registry resolves the full chain so a 1990 record coded A is interpretable today. The common failure is hard deletion: removing the code breaks every historical record and report that used it. The registry's rule is absolute - codes are never deleted, only retired with successors named.""",
how_it_works="""Deprecation proposals name the code, the reason, the successor code(s), and the effective date. After steward approval and an announcement period, the code's status flips to deprecated: validation blocks it for new records (with a message naming the successor) while resolution services keep translating it. Successor chains are stored as linked pointers and resolved transitively. Consumers get deprecation notices for codes they use, with migration guidance and deadlines. Periodic reports show deprecated-code usage in incoming data - a source still sending deprecated codes past the deadline gets quarantined. The archive tier keeps every retired code resolvable permanently.""",
key_points=[
 "Deprecated codes stay defined and resolvable; only new uses are blocked.",
 "Successor pointers (possibly chains) preserve historical meaning.",
 "Lifecycle: announced, deprecated, archived - never hard-deleted.",
 "Validation blocks deprecated codes for new data with successor guidance.",
 "Deprecated-code usage in feeds is monitored with quarantine past deadlines."],
requirements=[
 "Deprecation workflow: proposal, announcement, status flip, notices.",
 "Successor chains with transitive resolution.",
 "Validation rules distinguishing new-data blocking from historical resolution.",
 "Usage monitoring with deadlines and quarantine."],
standards=[
 "ISO/IEC 11179 for status metadata.",
 "W3C SKOS history notes."],
citations=[
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO.",
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009."],
sig_lens="""The Signature reading: deprecation is the registry's honorable retirement - the old code keeps its rank, its history, and its named heir, and is never struck from the rolls. The Signature registry retires codes the way republics retire flags: with ceremony, not with fire.""",
demo_data={"lists":[
 {"name":"deprecation","codes":[
   {"code":"CS","label":"Czechoslovakia -> CZ, SK","status":"deprecated"},
   {"code":"YU","label":"Yugoslavia -> successor states","status":"deprecated"},
   {"code":"CZ","label":"Czechia","status":"active"}],
  "checks":["CZ","CS","XX"],"expected":["CZ:active","CS:deprecated","XX:unknown"]}]},
),
dict(
name="Effective Dating",
group="Registry Governance", ladder_rank=16, ladder_tier="compounded",
description="""Effective dating answers when a code, definition, or mapping was true. A tax jurisdiction code might be valid from January 1 to June 30, replaced on July 1 by a reorganized district; a currency code is active from its introduction date; a deprecation takes effect on its announced date, not the day someone remembered to flip the flag. Every registry entry carries effective-from and effective-to dates, and queries are as-of: validate this 2023 transaction against the codes effective in 2023, not today's. Without effective dating, backdated corrections are impossible and historical reports silently change meaning when lists update. The discipline extends to future-dated entries: announced changes (a new code effective next quarter) publish early with future effective dates, so consumers can prepare. Gaps and overlaps in effective periods are validation errors - at any date, exactly one version of each code's definition must be effective.""",
how_it_works="""Registry rows carry effective-from/effective-to pairs; updates end-date the current row and insert the successor, never overwriting. As-of queries filter to the row effective on the requested date. Future-dated rows publish with status announced and become effective automatically on their date, with notifications to subscribed consumers. A continuity validator runs on every change: for each code, the effective periods must tile without gaps or overlaps. Backdated corrections insert rows into the past with an audit note, preserving the previous timeline as superseded rather than rewriting it. Reporting snapshots pin the effective date, so a rerun next year reproduces the same results.""",
key_points=[
 "Every entry carries effective-from/effective-to; queries are as-of a date.",
 "Future-dated changes publish early so consumers can prepare.",
 "Effective periods must tile without gaps or overlaps per code.",
 "Backdated corrections insert into the past as superseded rows, never rewrites.",
 "Report snapshots pin effective dates for reproducibility."],
requirements=[
 "Effective dating on all registry rows with as-of query support.",
 "Continuity validation: no gaps or overlaps per code.",
 "Future-dated publication with consumer notifications.",
 "Superseded-row preservation for backdated corrections."],
standards=[
 "ISO/IEC 11179 for temporal metadata.",
 "W3C PROV for change provenance."],
citations=[
 "Snodgrass R. Developing Time-Oriented Database Applications in SQL. Morgan Kaufmann, 1999.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: effective dating is the registry's honest calendar - every code true in its season, no season rewritten. The Signature registry lets the future be announced and the past be corrected, but never lets either be forged.""",
demo_data={"lists":[
 {"name":"tax_jurisdiction","codes":[
   {"code":"J-1042","label":"District 1042 (eff 2024-07-01)","status":"active"},
   {"code":"J-1041","label":"District 1041 (until 2024-06-30)","status":"deprecated"},
   {"code":"J-9999","label":"Proposed district (eff 2027-01-01)","status":"active"}],
  "checks":["J-1042","J-1041","J-0000"],"expected":["J-1042:active","J-1041:deprecated","J-0000:unknown"]}]},
),
dict(
name="Canonical vs Local Codes",
group="Registry Governance", ladder_rank=17, ladder_tier="compounded",
description="""Every organization accumulates local codes: the warehouse's own product categories, the legacy system's country abbreviations, the region's custom ticket priorities. Canonical codes are the registry's standard versions; local codes are the dialects. The registry's policy is pragmatic: local codes are acknowledged, mapped to canonical codes, and contained - never allowed to leak into canonical fields. Each local code gets a mapping row to its canonical equivalent (or a flag that no equivalent exists, which becomes an extension proposal), and ingestion translates local to canonical at the boundary. What the registry forbids is local codes stored as if canonical: a report joining on a mix of canonical and local codes silently drops rows. Namespaces keep local codes identifiable - WHS-ELEC vs ELEC - so anyone seeing a namespaced code knows it is dialect, not standard. Over time, the healthiest local codes graduate: proposed, reviewed, and adopted as canonical extensions.""",
how_it_works="""Local code sets are registered with their owning system, namespace prefix, and mapping table to canonical codes. Ingestion pipelines translate namespaced local codes to canonical at the boundary, stamping the translation. Unmapped local codes quarantine with a mapping task, not a silent drop. Canonical fields carry a constraint: values must come from the canonical list - a namespaced code failing this check is rejected, catching leaks. Quarterly reviews examine the most-used local codes: those with clean canonical equivalents stay mapped; those filling real gaps are proposed as canonical extensions; those that are just misspellings are fixed at the source. Graduated codes keep their local mapping as an alias forever.""",
key_points=[
 "Local codes are mapped to canonical codes and translated at ingestion boundaries.",
 "Namespaces mark local codes as dialect, never standard.",
 "Canonical fields reject local codes; leaks are caught by constraint checks.",
 "Unmapped local codes quarantine into mapping work.",
 "Healthy local codes graduate to canonical through the extension process."],
requirements=[
 "Registered local code sets with namespaces and mapping tables.",
 "Boundary translation with stamped translations.",
 "Canonical-field constraints rejecting local codes.",
 "Quarterly review promoting healthy locals to canonical."],
standards=[
 "ISO/IEC 11179 for code metadata.",
 "DAMA-DMBOK reference-data guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: canonical and local codes are the registry's high tongue and its dialects - both honored, never confused. The Signature registry translates dialects at the border, guards the high tongue's purity, and lets worthy dialect words earn citizenship.""",
demo_data={"lists":[
 {"name":"canonical_local","codes":[
   {"code":"ELEC","label":"Electronics (canonical)","status":"active"},
   {"code":"WHS-ELEC","label":"Warehouse dialect for ELEC","status":"deprecated"},
   {"code":"GB","label":"United Kingdom (canonical)","status":"active"}],
  "checks":["ELEC","WHS-ELEC","UK"],"expected":["ELEC:active","WHS-ELEC:deprecated","UK:unknown"]}]},
),
dict(
name="Reference Data Stewardship",
group="Registry Governance", ladder_rank=18, ladder_tier="compounded",
description="""Every reference list has a steward - a named human accountable for its correctness. The steward approves additions, writes definitions, adjudicates disputes (is a hot dog a sandwich for the product taxonomy?), schedules reviews, and signs off releases. Stewardship is organized by subject expertise, not by IT: the tax team stewards tax codes, the logistics team stewards shipping codes, the medical board stewards diagnosis lists. The steward's tools are the proposal queue (suggested codes with justification), the definition editor, the release checklist, and the usage dashboard showing which codes are actually used. Stewards are measured on list health: definition coverage (every code defined), deprecation hygiene (no zombie codes), release cadence, and dispute resolution time. When stewardship is missing, lists rot - definitions go unwritten, duplicates creep in, and consumers stop trusting the registry. The registry therefore tracks steward assignment as a first-class health metric: every list, a named steward, no exceptions.""",
how_it_works="""The registry assigns each list a steward and a backup, recorded with their authority scope. Proposed changes enter the steward's queue with justification and evidence; the steward approves, edits, or rejects with reasons, and approvals flow to release staging. Stewards run periodic list reviews - sampling codes for definition quality, checking the OTHER bucket, retiring zombies - on a cadence set by the list's volatility. Disputes escalate from the steward to a domain council with a documented decision that becomes precedent. Steward dashboards show queue depth, list health scores, and release history; lists without an active steward trigger governance alerts until one is named.""",
key_points=[
 "Every list has a named steward accountable for correctness - no exceptions.",
 "Stewards come from subject expertise (tax team stewards tax codes), not IT.",
 "Tools: proposal queue, definition editor, release checklist, usage dashboard.",
 "Measured on definition coverage, deprecation hygiene, cadence, dispute time.",
 "Missing stewardship is tracked as a first-class health metric with alerts."],
requirements=[
 "Named steward plus backup per list with recorded authority scope.",
 "Proposal queues with approve/edit/reject and reasons.",
 "Periodic list reviews on volatility-set cadences.",
 "Dispute escalation to domain councils with precedent documentation."],
standards=[
 "DAMA-DMBOK data governance guidance.",
 "ISO 8000 for data quality accountability."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Loshin D. Master Data Management. Morgan Kaufmann, 2008."],
sig_lens="""The Signature reading: stewards are the registry's wardens of words - each list under a named guardian's oath. The Signature registry leaves no vocabulary orphaned and measures each warden by the health of their words.""",
demo_data={"lists":[
 {"name":"stewardship","codes":[
   {"code":"TAX-OWNED","label":"Tax codes: steward Tax Team","status":"active"},
   {"code":"SHIP-OWNED","label":"Shipping codes: steward Logistics","status":"active"},
   {"code":"MISC-ORPHAN","label":"Misc codes: no steward assigned","status":"deprecated"}],
  "checks":["TAX-OWNED","MISC-ORPHAN","ZZZ"],"expected":["TAX-OWNED:active","MISC-ORPHAN:deprecated","ZZZ:unknown"]}]},
),
dict(
name="Change Requests and Approval",
group="Registry Governance", ladder_rank=19, ladder_tier="compounded",
description="""Reference data changes through requests, not edits. Anyone who needs a new code, a definition fix, or a deprecation files a change request with the justification, the proposed values, the affected consumers, and the desired effective date. The request routes to the list's steward, who checks for duplicates and overlap, assesses impact via the consumer subscription list, and approves, amends, or rejects with reasons. High-impact changes - redefining a code, deprecating a widely used one - require broader approval: affected consumer sign-off or domain council review. Approved requests enter release staging with their effective dates; rejected requests stay on record with reasons, so the same bad idea is not re-proposed quarterly. Emergency changes (a currency redenomination announced Friday) follow an expedited path with the same paperwork, just faster - the paperwork is what keeps emergencies from becoming silent edits. The request log is the list's legislative history: every change traceable to a who, a why, and a when.""",
how_it_works="""The change-request form captures requester, list, change type (add, amend, deprecate, remap), proposed values, justification, affected consumers, and effective date. Workflow routes to the steward; impact analysis lists subscribed consumers and recent usage counts of affected codes. Standard changes approve in one steward step; high-impact changes add consumer sign-off or council review. Approved requests stage into the next release (or the emergency release) with their effective dates; the release pipeline validates, diffs, and publishes. Every request - approved, rejected, withdrawn - persists with its full trail, forming the legislative history auditors and future stewards consult.""",
key_points=[
 "All changes arrive as requests with justification, values, consumers, effective date.",
 "Stewards check duplicates and assess impact via subscription lists.",
 "High-impact changes need consumer sign-off or council review.",
 "Emergency changes use an expedited path with the same paperwork.",
 "The request log is the list's legislative history: who, why, when."],
requirements=[
 "A change-request form capturing all required fields.",
 "Impact analysis from consumer subscriptions and usage counts.",
 "Tiered approval: steward for standard, council for high-impact.",
 "Persistent request history including rejections."],
standards=[
 "DAMA-DMBOK data governance guidance.",
 "ISO 10007 for configuration management (adapted)."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "ISO 10007. Quality management - guidelines for configuration management. ISO."],
sig_lens="""The Signature reading: change requests are the registry's legislation - proposed openly, debated by the affected, enacted on schedule, and recorded forever. The Signature registry governs its words the way free cities govern: no secret edits, no unrecorded laws.""",
demo_data={"lists":[
 {"name":"change_req","codes":[
   {"code":"CR-APPROVED","label":"Addition approved, staged","status":"active"},
   {"code":"CR-PENDING","label":"Awaiting steward review","status":"active"},
   {"code":"CR-REJECTED","label":"Duplicate of existing code","status":"deprecated"}],
  "checks":["CR-APPROVED","CR-REJECTED","CR-XXXX"],"expected":["CR-APPROVED:active","CR-REJECTED:deprecated","CR-XXXX:unknown"]}]},
),
dict(
name="Publication and Distribution",
group="Registry Governance", ladder_rank=20, ladder_tier="compounded",
description="""A reference list nobody can fetch might as well not exist. Publication makes each list available through the channels consumers actually use: a REST API for operational lookups, bulk downloads for data warehouses, change feeds for event-driven consumers, and human-readable pages for stewards and auditors. Distribution honors versioning: consumers pin the version they need, subscribe to release notifications, and get diffs to update efficiently. Availability targets are real - validation services that check every transaction against the registry cannot tolerate downtime - so lists are cached at the edge with versioned cache keys and served from replicas. Publication also means discoverability: a searchable catalog where a team wondering does a standard code for this exist? can find the list, read its definitions, see its steward, and subscribe. The registry measures distribution health: how many consumers are on stale versions, how fast new releases propagate, which lists nobody has fetched in a year.""",
how_it_works="""The publishing pipeline takes each released version and renders it to all channels: API endpoints (by version and as-of date), bulk files (CSV, JSON), change feeds (added/changed/deprecated events), and catalog pages. Edge caches hold versioned copies with cache keys including the version, so updates never serve stale-mixed content. Consumers declare versions and subscribe to notifications; the registry tracks each consumer's version lag and nudges the stale. Health metrics - release propagation time, stale-consumer counts, unfetched lists - feed steward dashboards. Disaster recovery keeps the last N versions restorable, because a bad release must be rollback-able in minutes.""",
key_points=[
 "Publish to every channel consumers use: API, bulk, feeds, human pages.",
 "Consumers pin versions and subscribe to release notifications.",
 "Edge caching with versioned keys keeps validation services fast and correct.",
 "The catalog makes lists discoverable with definitions, stewards, subscriptions.",
 "Distribution health: stale consumers, propagation time, unfetched lists."],
requirements=[
 "Multi-channel publishing from each released version.",
 "Version pinning and release notifications for consumers.",
 "Versioned edge caching for high-availability lookups.",
 "A searchable catalog with subscription management."],
standards=[
 "OpenAPI Specification for registry APIs.",
 "W3C SKOS for vocabulary publication."],
citations=[
 "OpenAPI Initiative. OpenAPI Specification v3.1.",
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009."],
sig_lens="""The Signature reading: publication is the registry's proclamation - every list cried aloud in every tongue consumers speak, versioned and cached at the gates. The Signature registry measures its own voice: who heard the new edition, who still listens to the old.""",
demo_data={"lists":[
 {"name":"distribution","codes":[
   {"code":"API-V3","label":"Current API channel","status":"active"},
   {"code":"BULK-CSV","label":"Bulk download channel","status":"active"},
   {"code":"FTP-LEGACY","label":"Retired distribution channel","status":"deprecated"}],
  "checks":["API-V3","FTP-LEGACY","CARRIER-PIGEON"],"expected":["API-V3:active","FTP-LEGACY:deprecated","CARRIER-PIGEON:unknown"]}]},
),
dict(
name="Reference Data APIs",
group="Registry Governance", ladder_rank=21, ladder_tier="compounded",
description="""Reference data APIs let systems validate and translate at runtime: is this currency code active today? What is the successor of this deprecated country code? Translate this local code to canonical. The API surface is small and stable: lookup (code to full entry), validate (code plus date to verdict), search (find codes by label), translate (map across lists via crosswalks), and versions (list available versions and diffs). Design rules keep the APIs dependable: responses include the list version and as-of date so callers can audit what they validated against; validation endpoints are idempotent and cacheable; bulk endpoints handle the warehouse-sized requests; and rate limits protect the registry while quotas are generous enough that nobody caches stale copies to dodge limits. Every response carries provenance - which list version, which crosswalk version - because a validation verdict is only as good as the list behind it.""",
how_it_works="""The API gateway exposes the five endpoints over versioned paths, backed by the registry's versioned stores. Lookup and validate hit edge caches keyed by list, version, and code for millisecond responses; search uses the vocabulary index; translate walks crosswalk rows with confidence; versions serves snapshots and diffs. Responses stamp list version, as-of date, and crosswalk version on every verdict. Bulk validate accepts batches for ETL pre-checks. Rate limiting is per consumer with quotas sized to real validation volumes; quota dashboards warn before throttling. Client libraries in major languages wrap the endpoints with local versioned caches and automatic refresh on new releases.""",
key_points=[
 "Five endpoints: lookup, validate, search, translate, versions.",
 "Responses stamp list version and as-of date for auditability.",
 "Validate is idempotent and cacheable for millisecond checks.",
 "Bulk validate serves ETL pre-checks at warehouse scale.",
 "Quotas sized to real volumes so nobody hoards stale caches."],
requirements=[
 "Versioned API paths over versioned registry stores.",
 "Edge caching for lookup/validate with versioned keys.",
 "Response stamping: list version, as-of date, crosswalk version.",
 "Client libraries with local caches and auto-refresh."],
standards=[
 "OpenAPI Specification.",
 "ISO/IEC 11179 for metadata in responses."],
citations=[
 "OpenAPI Initiative. OpenAPI Specification v3.1.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: the APIs are the registry's answering oracles - asked is this code true today, they answer in milliseconds, citing the edition they consulted. The Signature oracle never answers without naming its source.""",
demo_data={"lists":[
 {"name":"api_surface","codes":[
   {"code":"LOOKUP","label":"/lookup endpoint","status":"active"},
   {"code":"VALIDATE","label":"/validate endpoint","status":"active"},
   {"code":"V1-RPC","label":"Retired v1 RPC endpoint","status":"deprecated"}],
  "checks":["LOOKUP","V1-RPC","TELEPATHY"],"expected":["LOOKUP:active","V1-RPC:deprecated","TELEPATHY:unknown"]}]},
),
dict(
name="Caching and Fallback Copies",
group="Registry Governance", ladder_rank=22, ladder_tier="compounded",
description="""Reference data must survive outages: caches hold local copies with the edition and retrieval time stamped, fallbacks serve the last-good copy when the registry is unreachable, and staleness budgets bound how old a fallback may be. The caching policy per list states the refresh cadence (daily for country codes, hourly for volatile lists), the staleness budget (serve cache up to 24 hours old, then fail loudly rather than silently), and the fallback rules (read-only degraded mode: lookups allowed, updates queued). Cache invalidation keys on version publication - the new edition's event busts caches rather than waiting for TTL. Fallback copies are labeled conspicuously: every value served from fallback carries its edition and age, so downstream logic knows it is reading history, not truth. The discipline prevents the classic failure: the registry outage that becomes a data outage because every consumer cached nothing.""",
how_it_works="""Caching policies per list define refresh cadence, staleness budgets, and fallback rules. Consumers cache with edition and retrieval timestamps; version-publication events invalidate. Outages trigger fallback mode: serve last-good copies labeled with edition and age, queue updates, fail loudly past the staleness budget. Health checks monitor registry reachability; fallback drills verify the degraded path. Post-outage reconciliation replays queued updates.""",
key_points=[
 "Caches hold edition-stamped copies; fallbacks serve last-good when unreachable.",
 "Staleness budgets bound fallback age - fail loudly, not silently.",
 "Invalidation keys on version publication, not TTL expiry.",
 "Fallback values labeled with edition and age.",
 "Degraded mode: lookups allowed, updates queued, reconciliation after."],
requirements=[
 "Per-list caching policies with staleness budgets.",
 "Version-event cache invalidation.",
 "Fallback mode with labeling and update queuing.",
 "Fallback drills with reconciliation procedures."],
standards=[
 "OpenAPI Specification (caching headers); ISO/IEC 11179."],
citations=[
 "OpenAPI Initiative. OpenAPI Specification v3.1.",
 "Fielding R. Architectural Styles (REST caching). 2000."],
sig_lens="""The Signature reading: caching is the registry's memory of truth - kept fresh, honestly dated, serving in the master's absence with its age declared. The Signature fallback never pretends old truth is new.""",
demo_data={"lists":[
 {"name":"cache_country","codes":[
   {"code":"US","label":"United States","status":"active"},
   {"code":"DE","label":"Germany","status":"active"},
   {"code":"SU","label":"Soviet Union","status":"deprecated"}],
  "checks":["US","SU","XX"],"expected":["US:active","SU:deprecated","XX:unknown"]}]},
),
dict(
name="Reference Data Quality Monitoring",
group="Registry Governance", ladder_rank=23, ladder_tier="compounded",
description="""Reference data quality is monitored like production data: completeness (every code has a label and definition), validity (codes match their patterns), uniqueness (no duplicate codes), consistency (crosswalks agree), timeliness (editions published on schedule), and usage (orphan codes nothing references). Quality dashboards per list track these dimensions with thresholds and alerts; the steward gets the morning quality digest. Anomaly detection watches for the characteristic failures: the bulk import that duplicated codes, the mapping that drifted, the edition published with empty labels. Quality issues route by severity: the invalid code blocking transactions is an incident; the missing definition is a work item. Trend analysis shows whether quality is improving or rotting - the list whose exceptions grow monthly needs ownership attention, not just fixes. Quality metrics feed the steward's scorecard and the network spine's registry health view.""",
how_it_works="""Quality jobs per list measure completeness, validity, uniqueness, consistency, timeliness, usage against thresholds. Dashboards show per-list quality with alerts; stewards get digests. Issues route by severity with incident handling for blocking defects. Trend analysis flags rotting lists for ownership review. Metrics feed scorecards and the network health view.""",
key_points=[
 "Monitored dimensions: completeness, validity, uniqueness, consistency, timeliness, usage.",
 "Dashboards with thresholds, alerts, and steward digests.",
 "Issues routed by severity; blocking defects are incidents.",
 "Trend analysis catches rotting lists before they fail.",
 "Metrics feed scorecards and network health views."],
requirements=[
 "Per-list quality measurement jobs.",
 "Dashboards with alerting thresholds.",
 "Severity-routed issue workflows.",
 "Trend analysis with ownership escalation."],
standards=[
 "ISO 8000 (data quality); ISO/IEC 11179."],
citations=[
 "ISO 8000. Data quality. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: quality monitoring is the registry's daily inspection of its own ledgers - every code counted, every label read, every rot spotted early. The Signature inspector's digest never lets a ledger rot quietly.""",
demo_data={"lists":[
 {"name":"quality_status","codes":[
   {"code":"OK","label":"Passing","status":"active"},
   {"code":"WARN","label":"Warning","status":"active"},
   {"code":"OLD","label":"Retired check","status":"deprecated"}],
  "checks":["OK","OLD","MISSING"],"expected":["OK:active","OLD:deprecated","MISSING:unknown"]}]},
),
dict(
name="Multilingual Reference Data",
group="Registry Governance", ladder_rank=24, ladder_tier="compounded",
description="""Reference data in a global network speaks many languages: labels translated per locale, definitions localized, and the code itself staying language-neutral (US means the same in every tongue). The multilingual model separates the invariant (code, status, relationships) from the localized (labels, definitions, sort orders per locale). Translation workflows track coverage per locale - the country list fully translated, the new product taxonomy pending - with fallback rules (show the default-locale label where the translation is missing, marked as fallback). Locale-specific lists handle the genuinely local: administrative divisions, local holidays, regional classifications that have no global form. Right-to-left and script rendering are presentation concerns kept out of the registry; the registry stores Unicode text, consumers render. Translation quality matters: the mistranslated medical code is a safety issue, so critical lists use professional translation with review, not machine translation unchecked.""",
how_it_works="""The registry stores language-neutral codes with per-locale label/definition tables. Translation workflows track coverage with fallback rules (default locale marked as fallback). Locale-specific lists carry their scope metadata. Critical lists use professional translation with review; routine lists may use machine translation with human spot-checks. Consumers request by locale with fallback chains.""",
key_points=[
 "Codes language-neutral; labels and definitions localized per locale.",
 "Coverage tracked per locale with marked fallback rules.",
 "Locale-specific lists carry scope metadata.",
 "Critical lists: professional translation with review.",
 "Registry stores Unicode; rendering is the consumer's concern."],
requirements=[
 "Per-locale label/definition tables.",
 "Translation coverage tracking with fallbacks.",
 "Tiered translation quality by criticality.",
 "Locale-scoped list metadata."],
standards=[
 "Unicode Standard; ISO 639 (language codes); BCP 47."],
citations=[
 "The Unicode Consortium. The Unicode Standard.",
 "Phillips A, Davis M. BCP 47: Tags for Identifying Languages. IETF."],
sig_lens="""The Signature reading: multilingual reference data is the registry speaking in many tongues with one code - the invariant beneath, the localized above, every fallback honestly marked. The Signature registry's critical words are translated by masters, never machines alone.""",
demo_data={"lists":[
 {"name":"locale_country","codes":[
   {"code":"US","label":"United States","status":"active"},
   {"code":"JP","label":"Japan","status":"active"},
   {"code":"YU","label":"Yugoslavia","status":"deprecated"}],
  "checks":["JP","YU","ZZ"],"expected":["JP:active","YU:deprecated","ZZ:unknown"]}]},
),
]