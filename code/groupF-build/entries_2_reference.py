#!/usr/bin/env python3
"""Authored records for the Reference Data Registry databases (group F, part 1).
Public = real, fact-checked reference-data knowledge (ISO code lists, controlled
vocabularies, units, classifications). Signature = expanded Signature treatment.
Property of Justin Addam Higgins (JAH)."""

SIG_TAIL = ("Signature interpretation - original Signature-system treatment "
            "by Justin Addam Higgins; clearly labeled Signature-made, never "
            "presented as authentic public record.")

ENTRIES = [
dict(
name="What Reference Data Is",
group="Code Lists and Vocabularies", ladder_rank=1, ladder_tier="foundations",
description="""Reference data is the shared vocabulary an organization uses to classify, describe, and interpret everything else: country codes, currency codes, units of measure, status enumerations, product categories, language codes. Unlike master data, which describes specific entities (this customer, that product), reference data describes the allowed values - the menu everything else picks from. Unlike transactional data, it changes rarely and deliberately: adding a currency code is a governance event, not a daily occurrence. Reference data's power is standardization: when every system uses ISO 4217 currency codes, reports agree, integrations do not need translation tables, and analytics can aggregate across systems. Its danger is drift: when each system keeps its own copy of the country list, the copies diverge - one has 249 entries, another 241 - and nobody can say which is right. The reference data registry fixes one authoritative, versioned copy of every list and distributes it to all consumers.""",
how_it_works="""The registry catalogs every reference list in scope: codes, labels, definitions, hierarchies, effective dates, owning stewards. Each list is versioned; changes go through a request-review-approve-publish workflow rather than silent edits. Consumers fetch lists from the registry API or subscribe to change feeds instead of maintaining private copies. Validation services check incoming data against the registry - a transaction with currency code XXX is rejected or quarantined at the door. Mappings translate between the registry's canonical codes and legacy local codes during migration, with the mappings themselves versioned and governed. Deprecation retires codes gracefully: deprecated codes stay resolvable (so history still reads) but are blocked for new data.""",
key_points=[
 "Reference data is the allowed-values vocabulary: codes, units, statuses, categories.",
 "It changes rarely and deliberately; every change is a governance event.",
 "One authoritative versioned copy per list, distributed to all consumers.",
 "Validation at ingestion rejects or quarantines non-registry codes.",
 "Deprecation retires codes gracefully: resolvable for history, blocked for new data."],
requirements=[
 "A catalog of in-scope reference lists with owners and stewards.",
 "Versioning and change workflow per list.",
 "Distribution APIs and change feeds for consumers.",
 "Ingestion-time validation against the registry."],
standards=[
 "ISO/IEC 11179 for metadata registries.",
 "ISO 3166 (countries), ISO 4217 (currencies), ISO 639 (languages)."],
citations=[
 "ISO/IEC 11179 (series). Metadata registries. International Organization for Standardization.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: reference data is the registry of true names - the canonical words the whole network agrees to use. The Signature registry guards these names like a dictionary guards a language: versioned, deliberate, and the same for everyone.""",
demo_data={"lists":[
 {"name":"country","codes":[
   {"code":"US","label":"United States","status":"active"},
   {"code":"DE","label":"Germany","status":"active"},
   {"code":"SU","label":"Soviet Union","status":"deprecated"}],
  "checks":["US","XX","SU"],"expected":["US:active","XX:unknown","SU:deprecated"]}]},
),
dict(
name="Code Lists and Code Values",
group="Code Lists and Vocabularies", ladder_rank=2, ladder_tier="foundations",
description="""A code list is a finite, governed set of codes with defined meanings: order statuses (NEW, PAID, SHIPPED, DELIVERED, RETURNED), ticket priorities, claim types, marital statuses. Each code value carries a code (the machine key), a label (the human display), a definition (what it means, precisely), and metadata: sort order, effective dates, status (active, deprecated, retired), and owning steward. Good code lists are exhaustive within their purpose - every real case maps to exactly one code - and mutually exclusive, so classifiers never hesitate between two. They are also stable: codes never change meaning; when meaning must change, the old code is deprecated and a new one issued, so historical data keeps its interpretation. Code lists fail in familiar ways: the OTHER bucket grows until it is the largest code, definitions are missing so two teams use the same code differently, or local extensions proliferate until the standard list is fiction. The registry prevents all three with definitions, governance, and controlled extension processes.""",
how_it_works="""Authoring a code list starts from the real cases: enumerate what must be classified, draft candidate codes with definitions, test them against historical data (does every old record map cleanly?), and publish with effective dates. Consumers validate incoming values against the list; unknown values quarantine. The OTHER code is monitored - when it passes a threshold share, the list is reviewed for missing codes. Local extensions are allowed only through the registry: a team requests a code, the steward checks for overlap with existing codes, and the approved extension ships with a namespace prefix so local codes never collide with canonical ones. Deprecation moves a code to deprecated status with a successor pointer; retired codes stay resolvable forever.""",
key_points=[
 "Code values carry code, label, definition, sort order, effective dates, status, steward.",
 "Lists must be exhaustive and mutually exclusive within their purpose.",
 "Codes never change meaning; meaning changes get new codes with deprecation.",
 "The OTHER bucket is monitored as a missing-code detector.",
 "Local extensions go through the registry with namespace prefixes."],
requirements=[
 "Definitions for every code value, tested against historical data.",
 "Exhaustiveness and exclusivity checks at authoring.",
 "OTHER-bucket monitoring with review thresholds.",
 "A governed extension process with namespaced local codes."],
standards=[
 "ISO/IEC 11179 for code value metadata.",
 "DAMA-DMBOK reference-data guidance."],
citations=[
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO.",
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017."],
sig_lens="""The Signature reading: a code list is a sworn vocabulary - every word defined, every meaning fixed, no word allowed to secretly change its mind. The Signature registry writes each code's definition in stone and dates every stone.""",
demo_data={"lists":[
 {"name":"order_status","codes":[
   {"code":"NEW","label":"New order","status":"active"},
   {"code":"PAID","label":"Paid","status":"active"},
   {"code":"SHIPPED","label":"Shipped","status":"active"},
   {"code":"CANCELLED","label":"Cancelled","status":"deprecated"}],
  "checks":["NEW","CANCELLED","LOST"],"expected":["NEW:active","CANCELLED:deprecated","LOST:unknown"]}]},
),
dict(
name="Controlled Vocabularies",
group="Code Lists and Vocabularies", ladder_rank=3, ladder_tier="foundations",
description="""A controlled vocabulary is an organized list of authorized terms used for indexing, tagging, and retrieval: subject headings, skill tags, diagnosis keywords, product attributes. Control means authorization: taggers pick from the list instead of inventing terms, so the same concept is always tagged the same way and searches find everything. A good vocabulary distinguishes preferred terms from variants - use myocardial infarction, not heart attack, with heart attack recorded as a non-preferred synonym that redirects. It records relationships: broader terms (cardiology is broader than arrhythmia), narrower terms, and related terms, so browsers can navigate and searchers can expand or narrow. Vocabularies grow by proposal: anyone can suggest a term, but a vocabulary steward checks for duplicates, places it in the hierarchy, writes the scope note, and publishes it. Without control, tagging vocabularies decay into folksonomies where twelve spellings of the same skill make candidate search useless.""",
how_it_works="""Building a controlled vocabulary starts by harvesting the terms actually in use, clustering variants, and choosing preferred terms with written scope notes. Each term gets an identifier, preferred and variant labels, broader/narrower/related links, and status. Tagging tools integrate the vocabulary as type-ahead: users pick authorized terms, and variant entries redirect to preferred terms automatically. Governance runs a term proposal queue - suggested terms are checked against existing ones for duplication and placed correctly before approval. Usage analytics show which terms are actually applied; unused terms are candidates for deprecation, and overused vague terms are candidates for splitting into narrower terms. The vocabulary publishes in SKOS format so it interoperates with other systems' vocabularies.""",
key_points=[
 "Controlled vocabularies authorize terms so the same concept is always tagged the same way.",
 "Preferred terms, variant synonyms, and broader/narrower/related links structure the vocabulary.",
 "Scope notes define exactly what each term covers.",
 "Growth is by proposal with steward review, placement, and publication.",
 "Usage analytics drive deprecation of unused terms and splitting of vague ones."],
requirements=[
 "Term identifiers with preferred/variant labels and relationship links.",
 "Scope notes for every term.",
 "Type-ahead tagging integration that enforces authorized terms.",
 "A proposal queue with steward review and SKOS publication."],
standards=[
 "W3C SKOS (Simple Knowledge Organization System).",
 "ISO 25964 for thesauri and interoperability."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "ISO 25964-1. Thesauri and interoperability with other vocabularies. ISO, 2011."],
sig_lens="""The Signature reading: a controlled vocabulary is the network's agreed tongue - one true name per concept, with all the folk names recorded as aliases that bow to it. The Signature registry lets anyone propose a word, but only the stewards may crown it.""",
demo_data={"lists":[
 {"name":"skills","codes":[
   {"code":"SQL","label":"Structured Query Language","status":"active"},
   {"code":"SEQUEL","label":"Sequel (variant of SQL)","status":"deprecated"},
   {"code":"NOSQL","label":"NoSQL databases","status":"active"}],
  "checks":["SQL","SEQUEL","COBOL"],"expected":["SQL:active","SEQUEL:deprecated","COBOL:unknown"]}]},
),
dict(
name="Taxonomies",
group="Code Lists and Vocabularies", ladder_rank=4, ladder_tier="foundations",
description="""A taxonomy is a hierarchical classification: each concept sits under exactly one parent, forming a tree from the general to the specific. Product catalogs (Electronics > Computers > Laptops), organizational charts, document classifications, and industry codes like NAICS are taxonomies. The single-parent rule is what separates a taxonomy from looser structures: it guarantees that rollups are unambiguous - every laptop rolls up to exactly one Computers node, so category totals never double-count. Building a taxonomy means deciding the branching logic at each level (by what attribute do we split?), keeping sibling categories mutually exclusive, and limiting depth - beyond five or six levels, classifiers cannot place items reliably and browsers cannot navigate. Taxonomies need maintenance: new products force new leaves, dead categories accumulate, and reorganizations move subtrees. Versioned taxonomy releases with change notes let consumers adapt, and mapping tables translate between the old and new trees.""",
how_it_works="""Taxonomy design starts with the top-level facets - the few big buckets that partition the domain - then branches each by its most discriminating attribute, testing at every level that siblings are mutually exclusive and jointly exhaustive. Items are classified by walking from the root, choosing at each level, with an explicit rule for items that fit nowhere (escalate, do not force). The taxonomy publishes as a versioned tree with identifiers per node, definitions, and change notes per release. Reorganizations move subtrees with mapping tables from old node IDs to new ones, so historical classifications stay interpretable. Usage metrics per node - item counts, search refinements - reveal dead branches to prune and overloaded nodes to split.""",
key_points=[
 "Taxonomies are single-parent hierarchies: unambiguous rollups, no double-counting.",
 "Branching logic at each level must make siblings mutually exclusive and exhaustive.",
 "Depth beyond five or six levels breaks reliable classification.",
 "Versioned releases with change notes let consumers adapt to reorganizations.",
 "Node usage metrics reveal dead branches to prune and overloaded nodes to split."],
requirements=[
 "Documented branching logic per level with exclusivity tests.",
 "Node identifiers, definitions, and versioned releases.",
 "Subtree-move mappings preserving historical interpretation.",
 "Usage metrics per node driving pruning and splitting."],
standards=[
 "ISO 25964 for thesaurus and taxonomy structure.",
 "W3C SKOS for taxonomy publication."],
citations=[
 "ISO 25964-1. Thesauri and interoperability with other vocabularies. ISO, 2011.",
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009."],
sig_lens="""The Signature reading: a taxonomy is the registry's tree of kinds - every thing in its one true place, every branch a clean cut. The Signature registry prunes dead branches and grafts new ones by versioned decree, never by silent habit.""",
demo_data={"lists":[
 {"name":"product_taxonomy","codes":[
   {"code":"ELEC","label":"Electronics","status":"active"},
   {"code":"ELEC-COMP","label":"Computers","status":"active"},
   {"code":"ELEC-COMP-LAP","label":"Laptops","status":"active"},
   {"code":"ELEC-TUBE","label":"Tube TVs","status":"deprecated"}],
  "checks":["ELEC-COMP-LAP","ELEC-TUBE","ELEC-PHONE"],"expected":["ELEC-COMP-LAP:active","ELEC-TUBE:deprecated","ELEC-PHONE:unknown"]}]},
),
dict(
name="Hierarchies and Parent-Child Codes",
group="Code Lists and Vocabularies", ladder_rank=5, ladder_tier="foundations",
description="""Many code lists are hierarchical: the code itself encodes its ancestry. In the Dewey Decimal system, 641.5 sits under 641; in NAICS, 541512 sits under 54151; in ICD-10, J45.0 sits under J45. Parent-child coding makes rollups mechanical - truncate the code to roll up - and makes validation structural: a code is valid only if its parent exists. The design decisions are the code's anatomy: fixed segment lengths or dotted notation, how many levels, and whether the hierarchy is strict (every code has exactly one parent) or allows multiple parents. Strict hierarchies keep rollups unambiguous; multi-parent structures (a product in two categories) need separate relationship tables because the code can only name one parent. Hierarchy-aware tooling validates parent existence on insert, cascades deprecation (deprecating a parent flags its children for review), and publishes the tree for browsers. When hierarchies reorganize, code changes are the expensive kind - every stored code must be remapped - so hierarchy design deserves the same care as database schema design.""",
how_it_works="""Hierarchical codes are designed with explicit segment rules: segment lengths, separators, maximum depth, and the single-parent constraint. The registry stores parent-child relationships alongside the codes and validates every insert: the parent must exist and be active. Rollup queries truncate or join up the parent chain; drill-down queries walk children. Deprecation cascades: deprecating a parent generates review tasks for all descendants. Reorganizations are planned as code-remap projects with old-to-new mapping tables, dual publishing during transition, and a cutover date after which only new codes validate. Browsers render the tree from the parent-child table, and APIs offer ancestors and descendants endpoints for navigation.""",
key_points=[
 "Hierarchical codes encode ancestry; truncation rolls up mechanically.",
 "A code is valid only if its parent exists - validation is structural.",
 "Strict single-parent hierarchies keep rollups unambiguous.",
 "Deprecation cascades: retiring a parent flags all descendants for review.",
 "Reorganizations are code-remap projects with mapping tables and cutover dates."],
requirements=[
 "Documented segment rules: lengths, separators, depth, parent constraint.",
 "Parent-child relationship storage with insert-time parent validation.",
 "Deprecation cascade to descendants.",
 "Remap projects with dual publishing for reorganizations."],
standards=[
 "ISO/IEC 11179 for code metadata.",
 "W3C SKOS broader/narrower relations."],
citations=[
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO.",
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009."],
sig_lens="""The Signature reading: hierarchical codes are ancestry written into the name itself - every code carrying its lineage on its face. The Signature registry honors ancestry strictly: no child without a parent, no parent retired without its children's future settled.""",
demo_data={"lists":[
 {"name":"naics_like","codes":[
   {"code":"54","label":"Professional Services","status":"active"},
   {"code":"5415","label":"Computer Systems Design","status":"active"},
   {"code":"54151","label":"Computer Systems Design","status":"active"},
   {"code":"519","label":"Other Information Services","status":"deprecated"}],
  "checks":["54151","519","99999"],"expected":["54151:active","519:deprecated","99999:unknown"]}]},
),
dict(
name="Units of Measure",
group="Measures and Standards", ladder_rank=6, ladder_tier="foundations",
description="""Units of measure are reference data with physics behind them: every quantity in the system needs a unit, and the unit must be unambiguous. The SI system provides the base - meter, kilogram, second, ampere, kelvin, mole, candela - with prefixes (milli, kilo, mega) scaling them. Real systems also need the customary units commerce actually uses: inches, pounds, gallons, Fahrenheit - each defined by exact conversion to SI. UCUM (Unified Code for Units of Measure) gives every unit a case-sensitive code (m, kg, [in_i], Cel) so systems exchange quantities without ambiguity. The classic failures are unit mismatches: a Mars orbiter lost because one team used pound-seconds and another newton-seconds; drug doses confused between milligrams and micrograms. The registry's unit list defines each unit once with its UCUM code, its dimension (length, mass, time), and exact conversion factors, and quantity fields always store value-plus-unit, never bare numbers.""",
how_it_works="""The unit registry lists each unit with its UCUM code, dimension, and conversion factor to the canonical SI unit of that dimension. Quantity fields in every database store value and unit code together; bare numbers are rejected at validation. Conversion services translate between units using the registry's factors, with dimensional analysis blocking nonsense (meters to kilograms is refused). UCUM codes are case-sensitive and must be reproduced exactly - M is mega, m is milli, and confusing them is a thousandfold error. Compound units (kg/m2, mL/min) are built from base codes with the registry's grammar. The registry versions conversion factors (definitions occasionally refine, as the kilogram's did in 2019) with effective dates.""",
key_points=[
 "SI base units plus exact conversions for customary units - every unit defined once.",
 "UCUM codes give every unit an unambiguous, case-sensitive machine name.",
 "Quantities store value-plus-unit together; bare numbers are rejected.",
 "Dimensional analysis blocks invalid conversions (meters to kilograms).",
 "Conversion factors are versioned with effective dates."],
requirements=[
 "A unit list with UCUM codes, dimensions, and SI conversion factors.",
 "Value-plus-unit storage enforced at validation.",
 "Conversion services with dimensional checking.",
 "Versioned factors with effective dates."],
standards=[
 "UCUM (Unified Code for Units of Measure).",
 "SI Brochure (BIPM); ISO 80000 for quantities and units."],
citations=[
 "Schadow G, McDonald CJ. The Unified Code for Units of Measure. Regenstrief Institute.",
 "BIPM. The International System of Units (SI Brochure), 9th ed. 2019."],
sig_lens="""The Signature reading: units are the registry's sworn measures - each defined once, exactly, against the world's standards. The Signature registry never lets a bare number masquerade as a quantity, and never confuses a milli with a mega.""",
demo_data={"lists":[
 {"name":"units","codes":[
   {"code":"m","label":"meter","status":"active"},
   {"code":"kg","label":"kilogram","status":"active"},
   {"code":"[in_i]","label":"inch","status":"active"},
   {"code":"lb_av","label":"pound (avoirdupois)","status":"deprecated"}],
  "checks":["m","[in_i]","lb_av","furlong"],"expected":["m:active","[in_i]:active","lb_av:deprecated","furlong:unknown"]}]},
),
dict(
name="Currency Codes: ISO 4217",
group="Measures and Standards", ladder_rank=7, ladder_tier="foundations",
description="""ISO 4217 assigns every currency a three-letter code (USD, EUR, JPY), a three-digit numeric code (840, 978, 392), and a minor-unit exponent (2 for dollars-and-cents, 0 for yen, 3 for dinars). Money fields must always pair amount with currency code - an amount without a currency is meaningless, and the minor-unit exponent tells systems how to interpret integer amounts (100 in JPY is one hundred yen; 100 in USD-minor-units is one dollar). The standard also defines funds codes (XAU for gold, XDR for IMF special drawing rights) and the supranational euro. Currency lists change: countries redenominate, join or leave currency unions, and codes are withdrawn - the registry tracks effective dates and successor codes so historical amounts keep their meaning. The classic failure is assuming two decimals for all currencies, which silently corrupts yen and dinar amounts; the registry's currency table makes the exponent a required lookup, not a guess.""",
how_it_works="""The registry holds the ISO 4217 table: alpha code, numeric code, minor-unit exponent, currency name, issuing countries, status, effective dates, successor codes for withdrawn currencies. Money fields store amount, currency code, and optionally the exponent snapshot; validation requires the code to be active on the transaction date. Conversion and rounding services read the exponent from the registry - never hardcoded - and apply each currency's rounding rules. Withdrawn currencies stay resolvable with their successor mapping for historical reporting. The registry syncs with the ISO maintenance feed and publishes change events when codes are added or withdrawn.""",
key_points=[
 "ISO 4217: three-letter code, numeric code, minor-unit exponent per currency.",
 "Amounts always pair with currency codes; the exponent defines integer-amount meaning.",
 "Never assume two decimals - yen uses 0, dinars use 3.",
 "Withdrawn currencies stay resolvable with successor mappings.",
 "Validation requires the code to be active on the transaction date."],
requirements=[
 "The ISO 4217 table with exponents, statuses, effective dates, successors.",
 "Amount-plus-currency storage enforced at validation.",
 "Rounding services reading exponents from the registry.",
 "Sync with the ISO maintenance feed for additions and withdrawals."],
standards=[
 "ISO 4217. Codes for the representation of currencies.",
 "ISO 20022 for financial messaging currency usage."],
citations=[
 "ISO 4217. Codes for the representation of currencies. International Organization for Standardization.",
 "SIX Group. ISO 4217 currency code maintenance data."],
sig_lens="""The Signature reading: currency codes are the registry's sworn coinage - each coin named, each denomination exact, each retired coin remembered with its heir. The Signature registry never lets money travel without its name attached.""",
demo_data={"lists":[
 {"name":"currency","codes":[
   {"code":"USD","label":"US Dollar (840, exp 2)","status":"active"},
   {"code":"JPY","label":"Japanese Yen (392, exp 0)","status":"active"},
   {"code":"EUR","label":"Euro (978, exp 2)","status":"active"},
   {"code":"DEM","label":"German Mark (withdrawn)","status":"deprecated"}],
  "checks":["USD","JPY","DEM","XYZ"],"expected":["USD:active","JPY:active","DEM:deprecated","XYZ:unknown"]}]},
),
dict(
name="Country Codes: ISO 3166",
group="Measures and Standards", ladder_rank=8, ladder_tier="foundations",
description="""ISO 3166 gives every country and territory three identifiers: the two-letter alpha-2 code (US, DE, JP) used in domains, shipping, and most integrations; the three-letter alpha-3 code (USA, DEU, JPN) used where readability matters; and the three-digit numeric code (840, 276, 392) used where scripts are not Latin. The standard's maintenance agency adds codes for new states and withdraws codes for dissolved ones - the Soviet Union's SU, Yugoslavia's YU, Czechoslovakia's CS - and withdrawn codes must stay resolvable so historical records keep their meaning. The common failure is inventing local country codes (UK instead of GB, EL instead of GR) and then discovering integrations reject them; the registry forbids local invention and maps legacy codes to canonical ones. Subdivisions get their own part: ISO 3166-2 codes like US-CA and DE-BY identify states and provinces, essential for tax, shipping, and regulation.""",
how_it_works="""The registry holds all three parts: alpha-2, alpha-3, numeric, official names, subdivision codes (ISO 3166-2), status, effective dates, and successor mappings for withdrawn codes. Address and jurisdiction fields validate against the list active on the record's date. Legacy local codes (UK, EL) are stored as mappings to canonical codes, used only at ingestion boundaries and never stored as canonical values. Withdrawn codes resolve through successor mappings for historical queries. The registry syncs with the ISO maintenance agency feed and publishes change events; subdivision tables update with the same workflow when regions reorganize.""",
key_points=[
 "ISO 3166: alpha-2, alpha-3, and numeric codes per country/territory.",
 "ISO 3166-2 covers subdivisions: states, provinces, regions.",
 "Withdrawn codes (SU, YU, CS) stay resolvable via successor mappings.",
 "Local inventions (UK for GB) are mapped at ingestion, never stored canonical.",
 "Validation uses the list active on the record's date."],
requirements=[
 "All three 3166 parts with statuses, dates, and successor mappings.",
 "Subdivision tables for operational regions.",
 "Legacy-code mappings confined to ingestion boundaries.",
 "Sync with the ISO maintenance feed."],
standards=[
 "ISO 3166-1, ISO 3166-2, ISO 3166-3.",
 "W3C country-code usage in internationalization."],
citations=[
 "ISO 3166. Codes for the representation of names of countries. International Organization for Standardization.",
 "ISO Online Browsing Platform. Country code maintenance data."],
sig_lens="""The Signature reading: country codes are the registry's atlas of nations - every land named three ways, every fallen state's code kept in honorable retirement with its successor named. The Signature registry never invents a country and never forgets one.""",
demo_data={"lists":[
 {"name":"country3166","codes":[
   {"code":"US","label":"United States of America","status":"active"},
   {"code":"DE","label":"Germany","status":"active"},
   {"code":"SU","label":"USSR (withdrawn)","status":"deprecated"}],
  "checks":["US","SU","UK"],"expected":["US:active","SU:deprecated","UK:unknown"]}]},
),
dict(
name="Language Codes: ISO 639",
group="Measures and Standards", ladder_rank=9, ladder_tier="foundations",
description="""ISO 639 identifies the world's languages so content, interfaces, and data can declare what tongue they speak. ISO 639-1 gives major languages two-letter codes (en, es, ps for Pashto); ISO 639-3 covers over seven thousand languages with three-letter codes (eng, spa, pus). BCP 47 builds practical language tags from these parts plus script and region: en-US, zh-Hant-HK, ps-Arab-AF. Getting language codes right matters for search (stemmers and analyzers are per-language), for text-to-speech (the wrong code reads Pashto with English phonetics), for sorting (collation is language-specific), and for compliance (content must be available in required languages). The registry's language table holds the codes, names (English and autonym), script defaults, and text direction, so every database in the network tags its content consistently and every AI in the network knows which language it is reading.""",
how_it_works="""The registry holds ISO 639-1 and 639-3 tables with names, autonyms, script defaults, and direction (left-to-right or right-to-left). Content fields carry BCP 47 tags validated against the registry: language subtag must exist, script and region subtags must be valid where present. Ingestion normalizes variant tags (iw to he, in to id) to canonical forms. Search and AI services read the tag to select analyzers, voices, and collation. Macrolanguage mappings (639-3 to 639-1 where they exist) let systems aggregate dialect content under its macrolanguage for reporting. The registry syncs with the ISO 639-3 registrar (SIL) for additions and retirements.""",
key_points=[
 "ISO 639-1 (two-letter, major languages) and 639-3 (three-letter, 7000+ languages).",
 "BCP 47 tags combine language, script, region: en-US, ps-Arab-AF.",
 "Language tags drive search analyzers, TTS voices, collation, compliance.",
 "Variant tags normalize to canonical forms at ingestion.",
 "Macrolanguage mappings aggregate dialects for reporting."],
requirements=[
 "639-1 and 639-3 tables with names, autonyms, scripts, direction.",
 "BCP 47 validation on content language tags.",
 "Variant-to-canonical normalization at ingestion.",
 "Sync with the 639-3 registrar for changes."],
standards=[
 "ISO 639-1, ISO 639-2, ISO 639-3.",
 "BCP 47 (RFC 5646/4647) language tags."],
citations=[
 "ISO 639. Codes for the representation of names of languages. International Organization for Standardization.",
 "Phillips A, Davis M. BCP 47: Tags for Identifying Languages. IETF, 2009."],
sig_lens="""The Signature reading: language codes are the registry's census of tongues - seven thousand languages, each named and known. The Signature registry gives every language its true code, so no archive ever mishears what tongue its records speak.""",
demo_data={"lists":[
 {"name":"language","codes":[
   {"code":"en","label":"English","status":"active"},
   {"code":"ps","label":"Pashto","status":"active"},
   {"code":"iw","label":"Hebrew (old code for he)","status":"deprecated"}],
  "checks":["en","ps","iw","xx"],"expected":["en:active","ps:active","iw:deprecated","xx:unknown"]}]},
),
dict(
name="Date, Time, and Calendar Conventions",
group="Measures and Standards", ladder_rank=10, ladder_tier="foundations",
description="""Dates and times are reference data because every system must interpret them identically. ISO 8601 is the canonical interchange format: 2026-10-17 for dates, 2026-10-17T21:33:00-04:00 for timestamps with offsets, durations as P1Y2M3D. Time zones are named from the IANA database (America/New_York), never as bare offsets, because offsets change with daylight saving and history: the same offset means different zones at different dates. Timestamps stored without zone information are ambiguous and must be quarantined. Calendars need care too: most business uses the Gregorian calendar, but fiscal calendars, ISO week dates (2026-W42), and non-Gregorian calendars (Hijri, Hebrew, Chinese) appear in real data and must be tagged with their calendar system. The registry's date conventions define the canonical formats, the required zone tagging, the calendar tags, and the parsing rules - so October 17 means October 17 in every database.""",
how_it_works="""The registry publishes date conventions: ISO 8601 for interchange, IANA names for zones, mandatory offset-or-zone on timestamps, calendar tags on non-Gregorian dates. Ingestion parsers accept a documented set of legacy formats and normalize to canonical form; ambiguous inputs (01/02/03, zone-less timestamps) are quarantined or rejected per policy. Storage keeps instants in UTC plus the original zone for display. Date arithmetic uses calendar-aware libraries - adding a month means calendar months, not 30 days. Fiscal calendars are defined as reference data with year-start rules and period tables. The conventions are versioned; when the IANA database updates zone rules, the registry publishes the change and re-validates affected schedules.""",
key_points=[
 "ISO 8601 canonical formats for dates, times, durations, week dates.",
 "IANA zone names, never bare offsets; zone-less timestamps are ambiguous.",
 "UTC storage for instants plus original zone for display.",
 "Calendar tags for non-Gregorian and fiscal calendars.",
 "Legacy formats normalize at ingestion; ambiguous inputs quarantine."],
requirements=[
 "Published date conventions with canonical formats and zone rules.",
 "Ingestion parsers with a documented legacy-format list.",
 "Calendar-aware arithmetic in all date logic.",
 "Fiscal calendar definitions as versioned reference data."],
standards=[
 "ISO 8601. Date and time format.",
 "IANA Time Zone Database."],
citations=[
 "ISO 8601. Date and time format - ISO 8601. International Organization for Standardization.",
 "IANA. Time Zone Database. Internet Assigned Numbers Authority."],
sig_lens="""The Signature reading: dates are the registry's sworn calendar - every instant named once, in UTC, with its zone remembered. The Signature registry never lets 01/02/03 mean three different days in three different databases.""",
demo_data={"lists":[
 {"name":"timezone","codes":[
   {"code":"America/New_York","label":"Eastern Time (IANA)","status":"active"},
   {"code":"UTC","label":"Coordinated Universal Time","status":"active"},
   {"code":"EST5EDT","label":"POSIX-style (discouraged)","status":"deprecated"}],
  "checks":["UTC","America/New_York","EST5EDT","Mars/Olympus"],"expected":["UTC:active","America/New_York:active","EST5EDT:deprecated","Mars/Olympus:unknown"]}]},
),
dict(
name="Status and Lifecycle Codes",
group="Code Lists and Vocabularies", ladder_rank=11, ladder_tier="foundations",
description="""Status codes track where an entity is in its lifecycle: a lead is NEW, CONTACTED, QUALIFIED, or LOST; an order is PLACED, PAID, SHIPPED, DELIVERED, or RETURNED; a ticket is OPEN, IN_PROGRESS, RESOLVED, or CLOSED. Lifecycle codes differ from freeform status flags because transitions are governed: the registry defines the allowed transition graph - which statuses can move to which - and rejects impossible jumps like DELIVERED back to NEW. Each status carries its meaning, its allowed next statuses, whether it is terminal, and what it implies for reporting (is a CANCELLED order counted in revenue?). Terminal statuses are the commitment points: once reached, the entity's lifecycle is over and only reversal workflows (not casual edits) can move it. Status history is kept as an event log, so the full journey of every entity is replayable. Bad status design - too many statuses, overlapping meanings, no transition rules - is one of the most common sources of unreportable data.""",
how_it_works="""Each lifecycle gets a state machine definition: states with definitions, allowed transitions, terminal states, and guards (who may trigger each transition, what conditions must hold). The registry enforces transitions at write time: a transition not in the graph is rejected with the valid options listed. Status changes write events with actor, timestamp, and reason, building the entity's lifecycle history. Terminal states lock the record against casual edits; reversals go through defined reversal transitions with their own approvals. Reporting reads the history for funnel analysis (how many leads reach QUALIFIED?) and for aging (how long do tickets sit IN_PROGRESS?). State machine versions are effective-dated so old histories interpret under the rules that were live.""",
key_points=[
 "Status codes form governed state machines, not freeform flags.",
 "Allowed transition graphs reject impossible jumps.",
 "Terminal statuses lock records; reversals need defined workflows.",
 "Status history is an event log enabling funnel and aging analysis.",
 "Too many overlapping statuses is a classic unreportable-data trap."],
requirements=[
 "State machine definitions per lifecycle: states, transitions, terminals, guards.",
 "Write-time transition enforcement with helpful rejection messages.",
 "Status-change event history per entity.",
 "Versioned state machines with effective dates."],
standards=[
 "ISO/IEC 11179 for status metadata.",
 "DAMA-DMBOK reference-data guidance."],
citations=[
 "DAMA International. DAMA-DMBOK, 2nd ed. Technics Publications, 2017.",
 "Harel D. Statecharts: a visual formalism for complex systems. Science of Computer Programming, 1987."],
sig_lens="""The Signature reading: lifecycle codes are the registry's book of passages - every entity's journey written as lawful transitions, no teleportation allowed. The Signature registry records each passage with its witness and reason, so every arrival has a road behind it.""",
demo_data={"lists":[
 {"name":"ticket_status","codes":[
   {"code":"OPEN","label":"Open","status":"active"},
   {"code":"IN_PROGRESS","label":"In progress","status":"active"},
   {"code":"RESOLVED","label":"Resolved","status":"active"},
   {"code":"WONTFIX","label":"Will not fix (retired)","status":"deprecated"}],
  "checks":["OPEN","WONTFIX","ARCHIVED"],"expected":["OPEN:active","WONTFIX:deprecated","ARCHIVED:unknown"]}]},
),
dict(
name="Mapping Tables Between Code Sets",
group="Code Lists and Vocabularies", ladder_rank=12, ladder_tier="foundations",
description="""When two systems use different codes for the same concepts - one system's order status SHIPPED is another's DISPATCHED, one country's industry codes must report in another's - mapping tables translate between them. A mapping row links a source code to a target code with a relationship type: exact (fully equivalent), broader (source is more specific), narrower (source is more general), or related (overlapping but inexact). Inexact mappings carry warnings because they lose or distort meaning: mapping a detailed local diagnosis code to a broader standard code is lossy, and downstream users must know. Mappings are versioned on both sides: when either code list releases a new version, the mapping is re-validated, because a new code may have no mapping and a deprecated code's mapping may now point at a retired target. Unmapped codes are the metric that matters - the mapping coverage report shows what share of real data translates cleanly, and gaps become mapping work or list-extension proposals.""",
how_it_works="""Mapping tables are authored per code-list pair and direction: source list version, target list version, and rows of source code, target code, relationship type, confidence, author, and effective dates. Exact mappings translate automatically; inexact mappings translate with a loss flag that downstream consumers can inspect. Validation jobs check both ends: every active source code should have a mapping (coverage), and every target code should exist in the target list's current version (validity). On either list's new release, affected mappings enter re-validation; unmapped new codes queue for mapping work. Translation services apply mappings at integration boundaries, stamping translated records with the mapping version used so translations stay auditable.""",
key_points=[
 "Mapping rows carry source, target, relationship type (exact/broader/narrower/related), confidence.",
 "Inexact mappings translate with loss flags downstream can inspect.",
 "Mappings version against both lists' versions and re-validate on new releases.",
 "Mapping coverage (share of real data translating cleanly) is the key metric.",
 "Translated records stamp the mapping version used for auditability."],
requirements=[
 "Mapping tables per code-list pair with relationship types and confidence.",
 "Coverage and validity checks on both ends.",
 "Re-validation workflow on either list's new release.",
 "Mapping-version stamping on translated records."],
standards=[
 "ISO/IEC 11179 for mapping metadata.",
 "W3C SKOS mapping properties (exactMatch, broadMatch, narrowMatch, relatedMatch)."],
citations=[
 "W3C. SKOS Simple Knowledge Organization System Reference. W3C Recommendation, 2009.",
 "ISO/IEC 11179-3. Metadata registries: registry metamodel. ISO."],
sig_lens="""The Signature reading: mapping tables are the registry's treaties between vocabularies - each translation sworn with its exact degree of fidelity. The Signature registry never pretends a lossy translation is exact; it marks the loss plainly for all downstream to see.""",
demo_data={"lists":[
 {"name":"status_map","codes":[
   {"code":"SHIPPED","label":"maps exact to DISPATCHED","status":"active"},
   {"code":"PAID","label":"maps exact to SETTLED","status":"active"},
   {"code":"HOLD","label":"no target mapping","status":"deprecated"}],
  "checks":["SHIPPED","HOLD","REFUNDED"],"expected":["SHIPPED:active","HOLD:deprecated","REFUNDED:unknown"]}]},
),
]
