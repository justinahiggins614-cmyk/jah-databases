#!/usr/bin/env python3
"""Entries for the Asset and Equipment Registry databases (missing-115 #54).

Wave 1 (operational data): identifiers, configuration, location, operating
condition, warranty, maintenance history - asset tagging and identification,
CMDB-style configuration records, depreciation schedules, lifecycle states,
warranty tracking, calibration/maintenance linkage.

Verified 2026-10-17 (missing-115 program, Wave 1): RAW SWEEP over the full
manifest PLUS every shard index title in jah-databases-data-1 PLUS the
main-repo data dir: zero 'asset-equipment*' slugs/names; zero
'asset and equipment registry' title collisions. Near-hits: an IT
asset-management slice inside broader IT operations databases (no dedicated
registry record schema with tags, CMDB configuration records, depreciation
schedules, lifecycle states, warranty tracking, and calibration linkage), and
a fixed-assets accounting slice inside finance databases (no physical
identification, condition ratings, location tracking, or maintenance
history). The paste's rule was applied by name/purpose/record schema/
capabilities: a dedicated registry database with the full asset-record
schema - identifiers, configuration, location, operating condition,
warranty, maintenance history - is a distinct capability, so BUILD NEW is
the verdict.

So this build creates two NEW databases, 34 ladder-ordered records each:

  asset-equipment-registry           - The Asset and Equipment Registry Database
                                       (public-harvest: real, fact-checked
                                       asset and equipment registry practice -
                                       identifiers, configuration records,
                                       location, operating condition,
                                       warranty, maintenance history -
                                       every record carrying the full
                                       registry anatomy, the working method,
                                       key points, requirements, standards,
                                       real citations, and a working
                                       demonstration program; standard
                                       references ISO 55000:2014 (revised
                                       2024), ISO 55001:2014 (revised 2024),
                                       ISO 55002:2018, ISO/IEC 19770-1:2017,
                                       ASC 360, IRS Publication 946, GASB 34,
                                       ITIL 4 configuration management, NIST
                                       SP 800-88 Rev. 1, NFPA 70B:2023,
                                       GS1 General Specifications, the SMRP
                                       metric definitions, the Institute of
                                       Asset Management Anatomy v4, and IEEE
                                       Std 493-2007, cited per record)
  asset-equipment-registry-signature - The Asset and Equipment Registry
                                       Signature Database
                                       (his original Signature Registry
                                       Method: every asset a trust placed in
                                       the steward's hands, the registry the
                                       ledger of entrusted work, the tag the
                                       asset's true name, condition the
                                       testimony of care, maintenance the
                                       keeping of the covenant, and disposal
                                       the honorable discharge; src
                                       signature, titles suffixed " (Signature
                                       Edition)", never presented as
                                       authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

ID prefixes: JAH-AREG- (public) and JAH-AREGS- (signature), verified free in
the manifest (exact-prefix check both directions, zero collisions; JAH-AST-
belongs to the unrelated space-astro/astrophysics databases) and zero hits
in every shard index of jah-databases-data-1.

Numerical cores: all hand-computed 2026-10-17, machine-verified by the demos
(see demos_asset_equipment_registry.py). Every demo prints its real computed
values, asserts tight bounds (never float exact-equality), and ends with the
OK marker; the build machine-executes all 68 demos.

Never the words "bat belt" anywhere. No website references. No Facebook.
Civilian operational scope only.
"""

SIG_TAIL = ("Signature original - his original Signature Registry Method: "
            "every asset a trust placed in the steward's hands, the registry "
            "the ledger of entrusted work, the tag the asset's true name, "
            "condition the testimony of care, maintenance the keeping of the "
            "covenant, and disposal the honorable discharge. Clearly labeled "
            "Signature-made, never presented as authentic public record.")

CIT_ISO55000 = ("ISO 55000:2014. Asset management - Overview, principles and "
                "terminology. International Organization for Standardization; "
                "2014. (Revised as ISO 55000:2024.)")
CIT_ISO55001 = ("ISO 55001:2014. Asset management - Management systems - "
                "Requirements. International Organization for "
                "Standardization; 2014. (Revised as ISO 55001:2024.)")
CIT_ISO55002 = ("ISO 55002:2018. Asset management - Management systems - "
                "Guidelines for the application of ISO 55001. International "
                "Organization for Standardization; 2018.")
CIT_ISO19770 = ("ISO/IEC 19770-1:2017. Information technology - IT asset "
                "management - Part 1: IT asset management systems - "
                "Requirements; 2017.")
CIT_ASC360 = ("ASC 360. Property, Plant, and Equipment. Financial Accounting "
              "Standards Board, Accounting Standards Codification.")
CIT_IRS946 = ("Internal Revenue Service. Publication 946: How To Depreciate "
              "Property. U.S. Department of the Treasury.")
CIT_GASB34 = ("Governmental Accounting Standards Board. Statement No. 34: "
              "Basic Financial Statements - and Management's Discussion and "
              "Analysis - for State and Local Governments; 1999. (Capital "
              "asset reporting requirements.)")
CIT_ITIL4 = ("Axelos. ITIL Foundation: ITIL 4 Edition. TSO (The Stationery "
             "Office); 2019. (Configuration management practice.)")
CIT_NIST888 = ("National Institute of Standards and Technology. NIST SP "
               "800-88 Rev. 1: Guidelines for Media Sanitization; 2014.")
CIT_NFPA70B = ("NFPA 70B:2023. Recommended Practice for Electrical Equipment "
               "Maintenance. National Fire Protection Association; 2023.")
CIT_GS1 = ("GS1 General Specifications. Global standards for automatic "
           "identification and data capture (barcodes, EPC/RFID). GS1 AISBL.")
CIT_SMRP = ("Society for Maintenance and Reliability Professionals (SMRP). "
            "Best Practices: standard definitions for MTBF, MTTR, and "
            "availability metrics.")
CIT_IAM = ("Institute of Asset Management. Asset Management - An Anatomy. "
           "Version 4; 2024.")
CIT_IEEE493 = ("IEEE Std 493-2007 (Gold Book). Recommended Practice for the "
               "Design of Reliable Industrial and Commercial Power Systems; "
               "2007.")

ENTRIES = [
    {
        "key": "what_is_asset",
        "name": "What Is an Asset: Property, Equipment, and Inventory",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "An asset is anything an organization owns or controls that has "
            "value and a useful life longer than one accounting period: a "
            "laptop, a delivery van, a drill press, a building. Equipment is "
            "the working subset of assets - the machines, tools, vehicles, "
            "and devices that do the organization's work. Inventory is what "
            "gets consumed or sold: parts, materials, supplies, finished "
            "goods. The dividing lines matter because they decide how a "
            "thing is tracked and accounted for. A laptop above the "
            "capitalization threshold becomes a fixed asset on the balance "
            "sheet, depreciated over its useful life; the box of printer "
            "toner is an expense the month it is bought. Consumables are "
            "tracked by quantity, equipment by identity - one drill press is "
            "not interchangeable with another once it has a maintenance "
            "history. ISO 55000 defines an asset simply as an item, thing, or "
            "entity that has potential or actual value to an organization, "
            "which is why the registry starts with a decision: is this thing "
            "worth tracking as an individual, or only as a quantity. This "
            "record teaches the three-way split - asset, equipment, "
            "inventory - and the capitalization threshold that turns a "
            "purchase into a registry entry."
        ),
        "how_it_works": (
            "Classification works by asking four questions in order. First, "
            "does the item have a useful life beyond one year and stand "
            "alone as a unit - if yes it is an asset candidate, if it is "
            "consumed in use it is inventory or supplies. Second, does it "
            "meet the capitalization threshold the organization set (often "
            "2,500 to 5,000 dollars for businesses, lower for governments) - "
            "above the line it is capitalized on the balance sheet, below "
            "the line it is expensed but may still be tracked for control. "
            "Third, is it equipment - does it perform work, need "
            "maintenance, and carry operating risk - which earns it the full "
            "registry treatment: tag, condition, location, maintenance "
            "history. Fourth, what family does it belong to, which sets its "
            "depreciation life and maintenance regime. A 3,200 dollar air "
            "compressor passes all four gates and enters the registry as a "
            "capitalized equipment asset; a 40 dollar wrench fails the "
            "threshold but may be tracked as controlled tooling; a case of "
            "oil filters is inventory. The registry records the answers, not "
            "just the conclusion, so an auditor can re-walk the decision "
            "years later."
        ),
        "key_points": [
            "Assets have multi-year useful lives and are tracked by identity; inventory is consumed or sold and tracked by quantity.",
            "Equipment is the working subset of assets - machines, tools, vehicles, devices that need maintenance and carry operating risk.",
            "The capitalization threshold (commonly 2,500 to 5,000 dollars) decides whether a purchase becomes a balance-sheet asset or an expense.",
            "Items below the threshold can still be tracked for control (tools, laptops) without being capitalized - tracked is not the same as capitalized.",
            "ISO 55000 frames the whole discipline: an asset is anything with potential or actual value to the organization.",
        ],
        "requirements": [
            "A written capitalization policy stating the dollar threshold, the useful-life test, and who may approve exceptions.",
            "A decision record for each item near the threshold: why it was capitalized or expensed, dated and signed.",
            "A category assignment at entry: equipment, property, IT asset, vehicle, tooling, or inventory - driving depreciation and maintenance rules.",
            "Separation of the accounting decision (capitalize or expense) from the control decision (track individually or not).",
            "Periodic review of the threshold itself as prices and the organization's size change.",
        ],
        "standards": [
            "Asset definition follows ISO 55000:2014 (revised 2024): an item, thing, or entity with potential or actual value to an organization.",
            "Capitalization of property, plant, and equipment follows ASC 360 under U.S. GAAP.",
            "Governmental organizations report capital assets under GASB Statement 34.",
        ],
        "citations": [CIT_ISO55000, CIT_ASC360, CIT_GASB34],
        "sig_lens": (
            "The Signature read: an asset is a trust placed in the steward's "
            "hands - metal and wire entrusted to human care. Where public "
            "practice asks 'does it clear the threshold,' the Signature "
            "Registry Method asks 'was it entrusted to us' - and whatever "
            "was entrusted gets a name, a record, and a watch kept over it, "
            "whether or not the accountants capitalize it."
        ),
    },
    {
        "key": "register_anatomy",
        "name": "The Asset Register: What Every Record Carries",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "The asset register is the master list - one row per asset, "
            "holding everything the organization needs to know about it. A "
            "complete record carries six families of information. Identity: "
            "the asset tag number, serial number, manufacturer, model, and "
            "any government or fleet numbers. Classification: category, "
            "subcategory, and the depreciation class it belongs to. "
            "Location: the site, building, room, or GPS coordinate where it "
            "lives, plus who has custody of it. Condition: the current "
            "condition rating and the date it was last assessed. Financials: "
            "acquisition cost, acquisition date, depreciation method and "
            "life, and current book value. History: warranty terms and "
            "expiry, maintenance events, calibration dates, and the full "
            "chain of custody. The register is a living document: identity "
            "fields are written once, condition and location are updated on "
            "every touch, financials roll forward every period, and history "
            "only ever grows. A register missing any one family can answer "
            "only part of the question - an asset with no location is lost, "
            "one with no condition is a gamble, one with no history is a "
            "stranger. This record teaches the six-family anatomy that every "
            "later record in the database builds on."
        ),
        "how_it_works": (
            "A register record works as the single source of truth because "
            "every fact about the asset points back to it. The tag number is "
            "the primary key - every work order, warranty claim, calibration "
            "certificate, and disposal form references it. Identity fields "
            "are captured at receiving, when the box is open and the "
            "nameplate is readable; getting them wrong at this stage "
            "poisons every downstream record. Location and custody update "
            "whenever the asset moves, through a transfer form or a scan at "
            "the new site. Condition updates on inspection. Financials "
            "update on the depreciation schedule each period. Maintenance "
            "history appends from the work-order system. When the finance "
            "team asks 'what do we own,' the register answers from identity "
            "plus financials; when operations asks 'what can we use,' it "
            "answers from location plus condition; when the auditor asks "
            "'prove it,' it answers from history. The register earns trust "
            "one verified field at a time, and loses it the first time two "
            "systems disagree about where something is."
        ),
        "key_points": [
            "Every record carries six families: identity, classification, location, condition, financials, and history.",
            "The asset tag number is the primary key - every work order, claim, and certificate references it.",
            "Identity is written once at receiving; condition and location update on every touch; history only grows.",
            "The same register answers three masters: finance (what we own), operations (what we can use), audit (prove it).",
            "A register is trusted field by field - one disagreement between systems about an asset's location erodes all of it.",
        ],
        "requirements": [
            "A unique tag number on every tracked asset, physically affixed before the asset leaves receiving.",
            "All six field families present for capitalized equipment; at minimum identity, location, and custody for controlled items.",
            "A named owner for register accuracy - one person or team accountable when the register and reality disagree.",
            "Update discipline: location and custody on every move, condition on every inspection, financials every period.",
            "A change log on the register itself, so corrections are visible and auditable.",
        ],
        "standards": [
            "Register structure aligns with the asset information requirements of ISO 55001:2014 (revised 2024), clause 7.5.",
            "IT asset records follow the identification requirements of ISO/IEC 19770-1:2017.",
            "Financial fields follow ASC 360 property, plant, and equipment recognition and measurement.",
        ],
        "citations": [CIT_ISO55001, CIT_ISO19770, CIT_ASC360],
        "sig_lens": (
            "The Signature read: the register is the ledger of entrusted "
            "work - the book in which every trust is written down. Six "
            "families of facts because a trust has six faces: what it is, "
            "what kind it is, where it stands, how it fares, what it cost, "
            "and what it has endured. An incomplete record is an incomplete "
            "promise."
        ),
    },
    {
        "key": "asset_tags",
        "name": "Asset Tags and Physical Identification",
        "group": "Foundations",
        "ladder_rank": 1,
        "ladder_tier": "foundations",
        "description": (
            "An asset tag is the physical nameplate that ties the object in "
            "the world to the row in the register. It carries the asset "
            "number - usually a barcode, QR code, or RFID encoding of the "
            "tag ID - plus human-readable text with the number, and often "
            "the organization name and a 'property of' line. Tags are chosen "
            "for the environment: polyester or anodized aluminum labels for "
            "offices, metalphoto plates for harsh shops, high-temperature "
            "labels for ovens and engines, tamper-evident seals where theft "
            "is a risk. Placement is a discipline of its own: visible "
            "without disassembly, away from heat and abrasion, consistent "
            "across the fleet so auditors know where to look. The tag number "
            "itself is usually meaningless - a sequential or structured code "
            "like AST-2026-00417 - because meaning embedded in numbers rots "
            "when the organization reorganizes; the meaning lives in the "
            "register, the tag only points at it. When the tag is damaged or "
            "missing, the asset becomes anonymous: its history unreachable, "
            "its warranty unclaimable, its audit unverifiable. Tagging is "
            "the cheapest control in the whole registry program, and the "
            "one whose absence is felt first."
        ),
        "how_it_works": (
            "Tagging works as a closed loop between the physical and the "
            "digital. At receiving, the registrar generates the next tag "
            "number, prints or encodes the label, and affixes it to the "
            "asset before it leaves the dock - no tag, no entry to service. "
            "The tag number becomes the key in the register, and every later "
            "event is recorded against it by scanning or typing the number. "
            "During an audit, the auditor scans the tag and the register "
            "answers with the asset's identity, location, and condition; "
            "during a move, the mover scans at origin and destination and "
            "the register updates custody. If a tag is damaged, the "
            "registrar issues a replacement with the same number - the "
            "number is the identity, the label is just its voice - and logs "
            "the replacement so the chain of identity stays unbroken. "
            "Tamper-evident tags add a physical alarm: a peeled tag "
            "fractures, announcing that someone tried to move the name. The "
            "loop holds as long as the discipline holds: tag at receiving, "
            "scan at every touch, replace on damage, never reuse a number."
        ),
        "key_points": [
            "The tag ties the physical object to the register row - without it the asset is anonymous and its history unreachable.",
            "Tag numbers stay meaningless (sequential or structured codes); meaning lives in the register, not in the digits.",
            "Tag material must match the environment: polyester for offices, metalphoto for harsh shops, high-temp labels for heat.",
            "Tag at receiving before the asset enters service; scan at every move, inspection, and audit.",
            "A damaged tag gets a replacement with the same number - the number is the identity, the label is just its voice.",
        ],
        "requirements": [
            "A tag on every tracked asset, affixed before it leaves receiving and placed consistently across the fleet.",
            "Tag stock matched to the environment: temperature, chemicals, abrasion, and UV exposure of each asset class.",
            "Human-readable number alongside any barcode, QR, or RFID, so the asset stays identifiable when scanners fail.",
            "A re-tag procedure that preserves the original number and logs the replacement.",
            "Never reuse a retired tag number - retired numbers stay retired, so history can never point at the wrong asset.",
        ],
        "standards": [
            "Barcode symbologies and data capture follow the GS1 General Specifications.",
            "RFID asset identification follows the ISO/IEC 18000 series air-interface standards.",
            "IT asset identification tagging aligns with ISO/IEC 19770-1:2017 identification requirements.",
        ],
        "citations": [CIT_GS1, CIT_ISO19770, CIT_ISO55001],
        "sig_lens": (
            "The Signature read: the tag is the asset's true name, spoken "
            "aloud in metal and ink. To name a thing is to take "
            "responsibility for it - the unnamed asset is the unkept "
            "promise. The Signature method tags at the threshold of "
            "receiving, the way a name is given at birth: before the asset "
            "does a single hour of work, it is known."
        ),
    },
    {
        "key": "categories",
        "name": "Asset Categories and Classification",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Classification is the shelving system of the registry: it puts "
            "every asset on a shelf with its own kind, so depreciation, "
            "maintenance, and reporting rules can be applied by the shelf "
            "instead of one asset at a time. A typical hierarchy runs three "
            "to four levels: category (Facilities Equipment), subcategory "
            "(HVAC), class (Rooftop Units), and sometimes type (Packaged "
            "Rooftop Unit, 10-ton). The classification does real work. It "
            "assigns the depreciation life - computers 3 to 5 years, "
            "vehicles 5 to 7, buildings 27.5 to 39 under MACRS - through the "
            "asset class. It assigns the maintenance regime - rotating "
            "machinery gets vibration routes, electrical gear gets infrared "
            "surveys. It assigns the condition scale and the criticality "
            "model. And it drives every report the organization runs: "
            "capital spend by category, maintenance cost per class, fleet "
            "age by family. The classic failure is a flat list of ten "
            "thousand assets with no shelves - searchable but not "
            "manageable, because no rule can be aimed at a flat list. "
            "Classification is designed once, deliberately, and changed "
            "rarely, because every change rewrites history's filing."
        ),
        "how_it_works": (
            "Classification works by inheritance: rules written at the class "
            "level flow down to every asset on the shelf. The team builds "
            "the hierarchy from the organization's real fleet - listing "
            "what it actually owns, grouping by shared maintenance and "
            "depreciation behavior, and naming each level plainly. Each "
            "class gets its defaults: depreciation method and useful life, "
            "condition rating scale, preventive maintenance template, "
            "criticality factors, and warranty expectations. When a new "
            "asset arrives, the registrar picks its class and the record "
            "inherits all of it - the depreciation schedule proposes "
            "itself, the PM template attaches itself, the condition scale "
            "is ready. Reports then aggregate upward: class totals roll to "
            "subcategory, subcategory to category, category to the "
            "portfolio. If an asset is misclassified - a server filed as "
            "office furniture - it inherits the wrong life and the wrong "
            "maintenance, and the error compounds silently for years. So "
            "classification carries a review gate: new classes need "
            "approval, and reclassification is a logged event with a "
            "reason."
        ),
        "key_points": [
            "Classification lets rules be written once per shelf - depreciation life, maintenance regime, condition scale - and inherited by every asset on it.",
            "A flat list of assets is searchable but not manageable; the hierarchy is what makes fleet-level decisions possible.",
            "Misclassification compounds silently: the wrong shelf means the wrong depreciation life and the wrong maintenance for years.",
            "Class drives reporting: capital spend by category, maintenance cost per class, fleet age by family.",
            "The hierarchy is designed once and changed rarely - every change rewrites how history is filed.",
        ],
        "requirements": [
            "A documented hierarchy of three to four levels covering the organization's actual fleet, with plain names.",
            "Per-class defaults: depreciation method and life, PM template, condition scale, and criticality factors.",
            "A classification gate at receiving: every new asset gets its class before it enters service.",
            "An approval process for new classes and a logged reason for every reclassification.",
            "A periodic review that the classes still match the fleet - new technology creates new shelves.",
        ],
        "standards": [
            "Asset grouping and hierarchy design follows ISO 55000:2014 asset management principles (revised 2024).",
            "Depreciation lives by class follow IRS Publication 946 MACRS property classes for tax reporting.",
            "IT asset classification follows ISO/IEC 19770-1:2017 asset type conventions.",
        ],
        "citations": [CIT_ISO55000, CIT_IRS946, CIT_ISO19770],
        "sig_lens": (
            "The Signature read: classification is the seating of the "
            "household - every asset given its proper place at the table. "
            "The Signature method shelves by kinship of care: things that "
            "are tended the same way sit together, so the steward's rounds "
            "follow the shelves and no asset is visited by the wrong "
            "ritual."
        ),
    },
    {
        "key": "naming_taxonomy",
        "name": "Naming Conventions and Asset Taxonomy",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "A naming convention is the grammar of the registry: the rules "
            "for what an asset is called in every system, so the same "
            "compressor is never 'AC-3' in maintenance, 'Compressor #3' in "
            "finance, and 'RTU3' in the building automation system. Good "
            "names are structured but readable - SITE-SYSTEM-SEQUENCE is the "
            "classic pattern, giving names like HQ-HVAC-014 that a human "
            "can parse at a glance. The taxonomy is the controlled "
            "vocabulary underneath: the official list of allowed words for "
            "sites, systems, and equipment types, so nobody invents 'chiller "
            "plant,' 'chlr plt,' and 'central cooling' for the same thing. "
            "Naming discipline pays off in the unglamorous moments: merging "
            "two spreadsheets, searching during an outage, handing the "
            "register to a new technician. The rule is one name, spelled one "
            "way, everywhere - the register is the dictionary, and every "
            "other system quotes it. This record teaches the SITE-SYSTEM-"
            "SEQUENCE pattern, the controlled vocabulary, and the "
            "governance that keeps both clean."
        ),
        "how_it_works": (
            "The convention works by construction and by enforcement. "
            "Construction: the registrar assembles each name from taxonomy "
            "segments - a site code from the official site list, a system "
            "code from the official system list, and the next sequence "
            "number for that site-system pair. HQ-HVAC-014 is the fourteenth "
            "HVAC asset at headquarters, and the name can be parsed back "
            "into its segments without a lookup. Enforcement: the "
            "controlled vocabulary lives in the registry as dropdown lists, "
            "not free text, so 'chiller' cannot be typed three ways. "
            "Aliases are handled, not forbidden - the old name 'Compressor "
            "#3' is recorded as an alias pointing at HQ-HVAC-014, so old "
            "paperwork still resolves. When two organizations merge, the "
            "taxonomy team maps both vocabularies into one and renames in a "
            "planned cutover, with aliases preserving the old references. "
            "The test of a naming convention is the midnight search: a "
            "technician woken at 2 a.m. should find the asset on the first "
            "try, by the name on the work order, with no guessing."
        ),
        "key_points": [
            "One asset, one name, spelled one way in every system - the register is the dictionary every other system quotes.",
            "The SITE-SYSTEM-SEQUENCE pattern builds names a human can parse: HQ-HVAC-014 is the 14th HVAC asset at headquarters.",
            "The taxonomy is a controlled vocabulary - dropdown lists, not free text - so the same thing cannot be named three ways.",
            "Old names survive as aliases pointing at the official name, so legacy paperwork still resolves.",
            "The midnight-search test: a technician at 2 a.m. finds the asset on the first try by the name on the work order.",
        ],
        "requirements": [
            "A published naming convention with the segment pattern, segment lengths, and examples, before the first asset is named.",
            "A controlled vocabulary: official lists of site codes, system codes, and equipment-type terms, maintained centrally.",
            "Name construction at receiving from taxonomy segments plus the next sequence number - never invented freehand.",
            "An alias table mapping legacy and colloquial names to the official name.",
            "A rename procedure with cutover planning for mergers, site renames, and taxonomy revisions.",
        ],
        "standards": [
            "Taxonomy design follows ISO 55000:2014 principles for consistent asset identification (revised 2024).",
            "IT asset naming aligns with ISO/IEC 19770-1:2017 identification conventions.",
            "Site and equipment coding practices follow the Institute of Asset Management Anatomy v4 guidance on asset information.",
        ],
        "citations": [CIT_ISO55000, CIT_ISO19770, CIT_IAM],
        "sig_lens": (
            "The Signature read: a name is a covenant of recognition. The "
            "Signature method names every asset once, truly, and everywhere "
            "the same - because a thing called three different names is a "
            "thing nobody is fully responsible for. The taxonomy is the "
            "household's language, and the registry speaks it without "
            "accent."
        ),
    },
    {
        "key": "acquisition_cap",
        "name": "Acquisition and Capitalization",
        "group": "Foundations",
        "ladder_rank": 2,
        "ladder_tier": "foundations",
        "description": (
            "Acquisition is the birth of an asset in the organization: the "
            "purchase, build, donation, or transfer that brings it under "
            "control. Capitalization is the accounting decision made at "
            "birth - whether the cost lands on the balance sheet as an "
            "asset or on the income statement as an expense. The "
            "capitalization test has three gates: the cost meets the "
            "threshold, the useful life exceeds one year, and the item is a "
            "standalone unit rather than a repair part. Capitalized cost is "
            "not just the sticker price - it includes freight, installation, "
            "and the labor to place the asset in service, everything spent "
            "to make it ready for its intended use. The placed-in-service "
            "date starts the depreciation clock. Donated assets are recorded "
            "at fair value on the date of the gift; self-constructed assets "
            "accumulate their build costs in a construction account until "
            "completion. The registry captures all of it at receiving - "
            "purchase order, invoice, total capitalized cost, funding "
            "source, and the in-service date - because reconstructing "
            "acquisition facts years later, during an audit or a sale, is "
            "expensive guesswork. This record teaches the three gates, the "
            "true cost of acquisition, and the in-service moment that "
            "starts every clock."
        ),
        "how_it_works": (
            "Capitalization works as a documented decision at receiving. "
            "The receiver matches the delivery to the purchase order, "
            "records the full cost - price plus freight plus installation "
            "plus setup labor - and runs the three gates: threshold, "
            "useful life, standalone unit. Pass all three and the registrar "
            "creates the capitalized record: tag number, full cost basis, "
            "in-service date, depreciation class, and funding source. Fail "
            "any gate and the item is expensed - but still tagged and "
            "tracked if it is controlled equipment. The in-service date is "
            "the date the asset is ready for its intended use, not the "
            "delivery date and not the invoice date; a machine delivered in "
            "December but commissioned in February starts depreciating in "
            "February. For built assets, costs accumulate in construction in "
            "progress and transfer to the asset account at completion. For "
            "donations, a fair-value appraisal sets the basis. Every step "
            "leaves paper: PO, invoice, receiving report, commissioning "
            "sign-off - the audit trail that proves the birth facts when "
            "the asset is sold, audited, or retired."
        ),
        "key_points": [
            "Capitalization has three gates: cost meets the threshold, useful life exceeds one year, and the item is a standalone unit.",
            "Capitalized cost includes everything to place the asset in service - freight, installation, setup labor - not just the purchase price.",
            "The in-service date starts the depreciation clock: the date the asset is ready for use, not the delivery or invoice date.",
            "Donated assets enter at fair value; self-built assets accumulate cost in construction in progress until completion.",
            "Capture the birth facts at receiving - PO, invoice, cost basis, funding source - because reconstructing them years later is guesswork.",
        ],
        "requirements": [
            "A receiving procedure that matches delivery to PO, verifies condition, and records full cost before the asset leaves the dock.",
            "The three-gate capitalization decision documented per asset: threshold, life, standalone unit.",
            "An in-service date set by commissioning sign-off, distinct from delivery and invoice dates.",
            "Fair-value documentation for donations and cost accumulation records for self-constructed assets.",
            "Retention of the birth paperwork - PO, invoice, receiving report, commissioning sign-off - for the asset's life plus the retention period.",
        ],
        "standards": [
            "Capitalization and cost basis follow ASC 360, Property, Plant, and Equipment.",
            "Tax depreciation treatment follows IRS Publication 946 (MACRS).",
            "Governmental capital asset acquisition reporting follows GASB Statement 34.",
        ],
        "citations": [CIT_ASC360, CIT_IRS946, CIT_GASB34],
        "sig_lens": (
            "The Signature read: acquisition is the welcoming of the trust "
            "- the moment the organization takes the asset into its keeping. "
            "The Signature method records the welcoming completely: what it "
            "cost in full, when it truly began its service, and by whose "
            "hand it was received. A trust welcomed carelessly is a trust "
            "already half-lost."
        ),
    },
    {
        "key": "assignment_custody",
        "name": "Assignment and Custody",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Assignment answers the human question of the registry: who is "
            "responsible for this asset right now. Custody is the formal "
            "version - the named person or role accountable for the asset's "
            "care, security, and return. Every asset has exactly one "
            "custodian at a time; shared custody is no custody, because "
            "when everyone owns it, nobody maintains it. Assignment takes "
            "three common forms: personal issue (a laptop to an employee), "
            "location assignment (a compressor to a plant), and pool or "
            "fleet assignment (vehicles to a motor pool). The custody "
            "record is a chain, not a snapshot: assigned to Alvarez on "
            "March 3, transferred to the Denver site on June 11, returned "
            "to the pool on September 2. Gaps in the chain are where assets "
            "disappear - the laptop returned to nobody, the tool borrowed "
            "without a form. Strong custody programs make transfer a "
            "two-signature event: the giver signs it out, the receiver "
            "signs it in, and the register updates the same day. This "
            "record teaches the chain-of-custody discipline that keeps "
            "assets from evaporating between assignments."
        ),
        "how_it_works": (
            "Custody works as an unbroken chain of named responsibility. At "
            "assignment, the custodian acknowledges receipt - signing that "
            "they have the asset, understand its care requirements, and "
            "accept responsibility for its return. The register records the "
            "custodian, the assignment date, the expected return or review "
            "date, and the condition at handover. Transfer repeats the "
            "ritual: the current custodian releases, the new custodian "
            "accepts, both sign, the register updates the chain the same "
            "day. Return closes the loop with a condition check - damage "
            "found at return is charged to the custody period that caused "
            "it. The register flags the danger states automatically: assets "
            "with no custodian, assignments past their review date, "
            "custodians who have left the organization while assets still "
            "show assigned to them. The exit interview is the last line of "
            "defense: no departing employee clears HR until the register "
            "shows zero assets in their custody. The chain holds because "
            "every link is a named human who signed."
        ),
        "key_points": [
            "Every asset has exactly one custodian at a time - shared custody is no custody.",
            "Custody is a chain, not a snapshot: every assignment, transfer, and return is dated and signed.",
            "Transfer is a two-signature event - the giver signs out, the receiver signs in, the register updates the same day.",
            "Gaps in the chain are where assets disappear; the register must flag unassigned assets and stale assignments.",
            "The exit interview closes the loop: no one clears HR while the register still shows assets in their name.",
        ],
        "requirements": [
            "A named custodian for every tracked asset - person or role, never a department alone.",
            "Signed acknowledgment at assignment: receipt, care requirements understood, return responsibility accepted.",
            "Two-signature transfers with same-day register updates and condition noted at handover.",
            "Automatic flags for unassigned assets, overdue reviews, and custodians who have separated.",
            "An HR exit checklist tied to the register: zero assigned assets before clearance.",
        ],
        "standards": [
            "Custody and accountability practices align with ISO 55001:2014 asset management responsibilities (revised 2024).",
            "IT asset custody follows ISO/IEC 19770-1:2017 responsible-party identification.",
            "Chain-of-custody documentation practices follow the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_ISO55001, CIT_ISO19770, CIT_IAM],
        "sig_lens": (
            "The Signature read: custody is the personal face of the "
            "covenant. The registry may be the ledger, but the custodian is "
            "the keeper - a named human who looked the trust in the eye and "
            "signed. The Signature method never lets an asset belong to "
            "'everyone,' because everyone is no one, and no one keeps a "
            "covenant."
        ),
    },
    {
        "key": "condition_ratings",
        "name": "Asset Condition Ratings",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "A condition rating is the registry's honest answer to 'how is "
            "it doing' - a standardized score, usually 1 to 5, that turns a "
            "technician's judgment into comparable data. The classic five-"
            "point scale runs: 1 Excellent (like new, no defects), 2 Good "
            "(minor wear, fully serviceable), 3 Fair (moderate wear, "
            "serviceable with monitoring), 4 Poor (significant "
            "deterioration, repair or increased monitoring needed), 5 Failed "
            "or Critical (not serviceable, immediate action required). The "
            "scale only works with written criteria per class - what 'Fair' "
            "means for a rooftop HVAC unit must be spelled out in observable "
            "terms (fin condition, refrigerant pressures, amp draws), or "
            "two inspectors will score the same machine differently. "
            "Condition is assessed on inspection, after maintenance, and at "
            "assignment and return; the rating history becomes the asset's "
            "health biography. Rolled up, condition data runs the capital "
            "plan: the percentage of the fleet at 4 or 5 is the backlog "
            "quantified, and the trend of average condition tells leadership "
            "whether the maintenance program is winning or losing. This "
            "record teaches the five-point scale, the criteria that make it "
            "repeatable, and the roll-up that turns ratings into decisions."
        ),
        "how_it_works": (
            "Condition rating works by structured observation against "
            "written criteria. The inspector opens the class checklist - "
            "for a pump, say: casing, seals, bearings (vibration), motor "
            "amps versus nameplate, base and alignment - and scores each "
            "element, then the overall rating follows the worst significant "
            "element, not the average, because one failed seal defines the "
            "pump's reality. The rating is entered with the date, the "
            "inspector's name, and notes on the defects found; photos of "
            "the worst defects make the rating auditable years later. The "
            "register keeps every rating, so the asset's biography reads as "
            "a trend: 2, 2, 3, 3, 4 - a slow decline that predicts the "
            "failure before it happens, unlike a single snapshot. At the "
            "fleet level, the distribution is the story: a fleet drifting "
            "from 2s toward 4s is under-maintained or aging out, and the "
            "capital plan funds replacements starting with the 5s. "
            "Calibration of the inspectors matters as much as calibration "
            "of instruments - periodic side-by-side inspections keep two "
            "raters' 3s meaning the same thing."
        ),
        "key_points": [
            "The five-point scale (Excellent to Failed) turns judgment into comparable, reportable data.",
            "Written per-class criteria make the rating repeatable - two inspectors must score the same asset the same way.",
            "The overall rating follows the worst significant element, not the average - one failed seal defines the pump.",
            "Rating history is a health biography: the trend 2-2-3-3-4 predicts failure better than any snapshot.",
            "Fleet condition distribution runs the capital plan - fund replacements starting with the 5s.",
        ],
        "requirements": [
            "A published 1-to-5 scale with observable, per-class criteria for each level.",
            "Ratings recorded with date, inspector name, defect notes, and photos of significant defects.",
            "Assessment triggers: on inspection, after major maintenance, at assignment and return.",
            "Full rating history retained per asset - never overwrite, only append.",
            "Inspector calibration: periodic side-by-side inspections to keep ratings consistent across raters.",
        ],
        "standards": [
            "Condition assessment practices align with ISO 55002:2018 guidance on asset performance evaluation.",
            "Electrical equipment condition criteria follow NFPA 70B:2023 maintenance and testing recommendations.",
            "Facility condition assessment follows the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_ISO55002, CIT_NFPA70B, CIT_IAM],
        "sig_lens": (
            "The Signature read: condition is the testimony of care - the "
            "asset speaking honestly about how it has been kept. The "
            "Signature method listens on a fixed scale with written "
            "criteria, because testimony must be comparable to be just, and "
            "it keeps every testimony ever given, because the trend of "
            "testimonies is the prophecy."
        ),
    },
    {
        "key": "location_tracking",
        "name": "Asset Location and Site Tracking",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Location tracking answers the simplest registry question and "
            "the one most often wrong: where is it. The location hierarchy "
            "typically runs site, building, floor or area, room or zone, and "
            "sometimes a precise spot - Site Denver, Building B, Production "
            "Floor, Line 3, Station 7. Each level is a controlled list, so "
            "'Denver,' 'DEN,' and 'Denver site' cannot all exist. For mobile "
            "assets - vehicles, tools, shared equipment - location is "
            "custody plus last-known position, updated on every move. "
            "Fixed assets get verified in place; the location is part of "
            "their identity. Location data does quiet heavy lifting: it "
            "scopes audits (audit Building B this quarter), scopes "
            "maintenance routes (all Line 3 assets on Tuesday), allocates "
            "costs to cost centers, and proves physical existence to "
            "auditors. The failure mode is the stale location - the asset "
            "moved three years ago and the register still shows the old "
            "room, so the auditor finds an empty spot and the asset is "
            "written off as missing while it works happily across town. "
            "This record teaches the location hierarchy, the move "
            "discipline, and the verification that keeps 'where' honest."
        ),
        "how_it_works": (
            "Location tracking works as a hierarchy of controlled lists plus "
            "move discipline. The site list, building list, and room list "
            "are maintained centrally; the registrar picks from them, never "
            "types freehand. Every move generates a transfer: the mover "
            "records the asset, the from-location, the to-location, the "
            "date, and their name - on a form, a scan, or a mobile app - "
            "and the register updates the same day. Bulk moves (a lab "
            "relocation, a site consolidation) are planned as move lists, "
            "executed against the list, and reconciled the same week. "
            "Verification closes the loop: cycle counts check a sample of "
            "locations monthly, and wall-to-wall audits verify every "
            "location on a rotation. The register also tracks location "
            "history, because 'where has it been' explains wear patterns "
            "and cost allocations. For auditors, the location is the proof "
            "of existence: pick an asset from the register, walk to the "
            "room, touch the tag. When that walk succeeds ninety-eight "
            "times out of a hundred, the register is believed; when it "
            "fails, nothing in the register is believed."
        ),
        "key_points": [
            "Location is a hierarchy of controlled lists - site, building, area, room - never freehand text.",
            "Every move is a recorded transfer: asset, from, to, date, mover - updated the same day.",
            "Stale locations are the classic failure: the asset works across town while the register shows an empty room.",
            "Location scopes everything: audits, maintenance routes, cost-center allocation, and audit proof of existence.",
            "The auditor's walk - register to room to tag - is the trust test; it must succeed nearly every time.",
        ],
        "requirements": [
            "A location hierarchy with centrally maintained lists at each level.",
            "A transfer record for every move, including bulk moves executed against planned move lists.",
            "Same-day register updates on moves; no batching moves into month-end.",
            "Cycle counts monthly on a sample of locations; wall-to-wall verification on rotation.",
            "Location history retained per asset to explain wear and allocate costs.",
        ],
        "standards": [
            "Location and site identification practices align with ISO 55001:2014 asset information requirements (revised 2024).",
            "IT asset location tracking follows ISO/IEC 19770-1:2017.",
            "Physical inventory verification practices follow the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_ISO55001, CIT_ISO19770, CIT_IAM],
        "sig_lens": (
            "The Signature read: location is where the trust stands its "
            "watch. The Signature method knows the ground under every "
            "asset's feet, and when an asset moves, the ledger moves with "
            "it that same day - because a steward who does not know where "
            "the entrusted thing stands is a steward in name only."
        ),
    },
]
ENTRIES.extend([
    {
        "key": "lifecycle_states",
        "name": "Asset Lifecycle States",
        "group": "Foundations",
        "ladder_rank": 3,
        "ladder_tier": "foundations",
        "description": (
            "Every asset travels the same road: planned, acquired, in "
            "service, and finally retired - with detours through "
            "maintenance, storage, and transfer along the way. Lifecycle "
            "states name the stops on that road so the whole organization "
            "means the same thing by 'active' or 'retired.' A practical "
            "state model runs: Planned (approved, not yet bought), Ordered "
            "(purchased, not received), In Service (working and available), "
            "In Maintenance (temporarily out for repair), In Storage "
            "(serviceable but idle), Transferred (moved between sites or "
            "owners), Retired (permanently out of service), and Disposed "
            "(sold, recycled, or destroyed). States are the traffic lights "
            "of the register: only In Service assets count toward available "
            "capacity, only Retired assets can be disposed, and an asset "
            "cannot jump from Ordered to Disposed without passing through "
            "the states in between. State history is the asset's biography "
            "in one line - Planned 2021, In Service 2021-2025, In "
            "Maintenance twice, Retired 2026. Reports lean on states "
            "constantly: fleet availability, average age of In Service "
            "assets, value sitting In Storage. This record teaches the "
            "eight-state model and the transition rules that keep the road "
            "honest."
        ),
        "how_it_works": (
            "Lifecycle states work as a state machine with guarded "
            "transitions. Each state has entry rules: an asset enters In "
            "Service only through commissioning sign-off, enters Retired "
            "only through a retirement approval, enters Disposed only with "
            "a disposal certificate. Each state has allowed exits: In "
            "Maintenance can return to In Service or go to Retired, but "
            "Retired can never return to In Service - retirement is a "
            "one-way door, which prevents 'retired' assets from quietly "
            "re-entering the fleet without re-commissioning. The register "
            "enforces the transitions: it rejects a jump from Ordered to "
            "Disposed, demands the approval for Retired, and timestamps "
            "every change with the actor's name. State drives behavior "
            "elsewhere: work orders can only open against In Service or In "
            "Maintenance assets, depreciation runs only for states between "
            "acquisition and retirement, and insurance schedules pull only "
            "In Service and In Storage. The state history, kept forever, "
            "lets an analyst reconstruct any asset's life and lets the "
            "organization compute true lifecycle costs from birth to "
            "disposal."
        ),
        "key_points": [
            "The eight states - Planned, Ordered, In Service, In Maintenance, In Storage, Transferred, Retired, Disposed - name every stop on the asset's road.",
            "States are a guarded state machine: retirement is a one-way door, and skipped states are rejected.",
            "State drives everything else: work orders, depreciation, insurance, and availability all key off the current state.",
            "Every transition is timestamped with the actor's name - the biography writes itself.",
            "State history kept forever enables true lifecycle cost analysis from birth to disposal.",
        ],
        "requirements": [
            "A published state model with definitions, entry rules, and allowed transitions.",
            "Register enforcement of transitions: illegal jumps rejected, approvals required for Retired and Disposed.",
            "Commissioning sign-off as the only gate into In Service; disposal certificate as the only gate into Disposed.",
            "Timestamped, attributed state history retained for the asset's life plus retention.",
            "Downstream systems keyed to state: work orders, depreciation, and insurance all read the current state.",
        ],
        "standards": [
            "Lifecycle stage concepts align with ISO 55000:2014 asset lifecycle principles (revised 2024).",
            "Lifecycle costing follows ISO 55002:2018 guidance on life-cycle value realization.",
            "IT asset lifecycle stages follow ISO/IEC 19770-1:2017.",
        ],
        "citations": [CIT_ISO55000, CIT_ISO55002, CIT_ISO19770],
        "sig_lens": (
            "The Signature read: the lifecycle is the asset's mortal journey "
            "- welcomed, put to work, tended in sickness, rested, and at "
            "last honorably discharged. The Signature method walks the whole "
            "road with the asset and never lets it vanish mid-journey: "
            "every state is witnessed, every transition signed, and "
            "retirement is a door that opens only outward, into honor."
        ),
    },
    {
        "key": "tag_technologies",
        "name": "Tag Technologies: Barcode, QR Code, and RFID",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Three technologies carry the asset number from the tag to the "
            "scanner, and the choice shapes the whole identification "
            "program. The 1D barcode (Code 128, Code 39) is the workhorse: "
            "pennies per label, readable by every scanner ever made, "
            "line-of-sight only, one asset per scan, and damaged easily by "
            "abrasion. The QR code carries far more data - the asset number "
            "plus a URL to the register record - readable by any phone "
            "camera, still line-of-sight, still one at a time, but tougher "
            "against damage thanks to error correction. RFID is the step "
            "change: a passive UHF tag costs dimes to dollars, needs no "
            "line of sight, and a handheld reader inventories a whole room "
            "in seconds - dozens of tags per second, through dust and at "
            "arm's length. The price is infrastructure: readers, "
            "placement engineering (metal and liquid detune tags), and "
            "data hygiene for the flood of reads. The honest selection "
            "rule: barcode where humans scan deliberately and budgets are "
            "thin, QR where phones are the scanners and a link to the "
            "record helps, RFID where audit speed matters - wall-to-wall "
            "counts of thousands of assets, tool cribs, and IT closets. "
            "Many programs mix: barcode on the asset, RFID on the high-"
            "value or high-count classes. This record teaches the three "
            "technologies, their economics, and the selection rule."
        ),
        "how_it_works": (
            "Selection works by matching the technology to the touch "
            "pattern. Count the touches: how many assets, how often "
            "scanned, by whom, in what environment. A thousand office "
            "laptops scanned at assignment and return: barcode wins, "
            "because the touch count is low and humans do the scanning. "
            "Five thousand tools in a crib checked in and out daily: RFID "
            "wins, because the time saved per transaction pays for the "
            "readers in months - a thirty-second barcode queue becomes a "
            "two-second walk-through. Field equipment in rain and mud: QR "
            "or rugged barcode, because phones are already in pockets and "
            "RFID readers add kit to carry. The pilot proves it: tag one "
            "hundred assets with each candidate, run a month of real "
            "touches, and measure scan success rate, seconds per "
            "transaction, and tag survival. Encoding discipline matters "
            "regardless of technology: the tag carries the asset number "
            "only, never the description - descriptions change, numbers do "
            "not. And every technology needs the human-readable number "
            "printed alongside, because scanners break, batteries die, and "
            "the audit goes on."
        ),
        "key_points": [
            "Barcode: cheapest, universal, line-of-sight, one scan at a time - wins where touches are few and deliberate.",
            "QR code: phone-readable, carries a link to the register record, tougher against damage - wins where phones are the scanners.",
            "RFID: no line of sight, dozens of reads per second, whole-room audits in seconds - wins where audit speed pays for readers.",
            "The tag encodes the asset number only, never the description - descriptions change, numbers do not.",
            "Always print the human-readable number alongside any code - the audit continues when the scanner breaks.",
        ],
        "requirements": [
            "A touch-pattern analysis before selection: asset counts, scan frequency, who scans, and the environment.",
            "A pilot of each candidate technology on real assets for a real month, measuring success rate and seconds per transaction.",
            "Encoding discipline: asset number only on the tag; all meaning lives in the register.",
            "Human-readable number on every tag regardless of technology.",
            "An RFID placement plan where used: tag selection for metal and liquid environments, reader coverage, read-data hygiene.",
        ],
        "standards": [
            "Barcode symbologies follow the GS1 General Specifications.",
            "UHF RFID air interface follows ISO/IEC 18000-63; item-level tagging follows ISO/IEC 17364.",
            "QR code symbology follows ISO/IEC 18004.",
        ],
        "citations": [CIT_GS1, CIT_ISO19770, CIT_ISO55001],
        "sig_lens": (
            "The Signature read: the technology is the voice the name "
            "speaks with - a whisper for the barcode, a clear word for the "
            "QR, a chorus for the RFID room. The Signature method chooses "
            "the voice that fits the keeping: the quiet tag for the quiet "
            "asset, the chorus where a thousand trusts must be counted "
            "before lunch. The name stays the same in every voice."
        ),
    },
    {
        "key": "depreciation",
        "name": "Depreciation Schedules: Straight-Line and Declining Balance",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "Depreciation is the systematic spreading of an asset's cost "
            "over its useful life - the accounting recognition that the "
            "machine is consumed a little every year it works. The "
            "straight-line method is the honest workhorse: (cost minus "
            "salvage value) divided by useful life, the same expense every "
            "year. A 50,000 dollar press with 5,000 salvage and a 10-year "
            "life expenses 4,500 dollars a year, every year, until the "
            "book value reaches salvage. The declining-balance method "
            "front-loads the expense: each year takes a fixed percentage "
            "(often double the straight-line rate) of the remaining book "
            "value, so early years expense more - matching assets that lose "
            "value fastest when new, like vehicles and computers. The units-"
            "of-production method ties expense to use: cost per hour or per "
            "mile times actual usage, the fairest method for machines whose "
            "wear follows the meter. Book value is cost minus accumulated "
            "depreciation - the carrying amount on the balance sheet, not "
            "the market value. The schedule is set at acquisition from the "
            "asset's class and rarely changes; changing it mid-life is a "
            "restatement event. This record teaches the three methods, the "
            "book-value arithmetic, and why the schedule is a promise kept "
            "year after year."
        ),
        "how_it_works": (
            "A depreciation schedule works as a clockwork table built once "
            "at acquisition. The inputs: capitalized cost, salvage value "
            "(what it will be worth at the end - often zero for tax, "
            "sometimes real for resale), useful life in years or units, and "
            "the method the class dictates. Straight-line: annual expense "
            "equals (cost minus salvage) over life, booked each period like "
            "clockwork. Double-declining balance: rate equals 2 over life; "
            "each year's expense equals rate times beginning book value, "
            "switching to straight-line in the later years so the book "
            "value lands exactly on salvage - the crossover is the part "
            "spreadsheets get wrong by hand. Units of production: rate per "
            "unit equals (cost minus salvage) over lifetime units; expense "
            "equals rate times units used that period, read from the meter. "
            "Each period the register posts the expense, accumulates it, "
            "and reports the new book value. Mid-life changes - a life "
            "extension after a rebuild, an impairment after damage - are "
            "prospective events with documentation, never silent edits to "
            "history. The schedule's integrity is what lets the balance "
            "sheet be believed."
        ),
        "key_points": [
            "Straight-line: (cost minus salvage) over life, the same expense every year - the honest workhorse.",
            "Double-declining balance front-loads expense at 2/life of remaining book value, switching to straight-line to land on salvage.",
            "Units of production ties expense to the meter - fairest for machines whose wear follows hours or miles.",
            "Book value is cost minus accumulated depreciation: the carrying amount, not the market value.",
            "The schedule is set at acquisition and kept like a promise; mid-life changes are documented prospective events.",
        ],
        "requirements": [
            "Capitalized cost, salvage value, useful life, and method recorded per asset at acquisition.",
            "Method assigned by asset class per policy, not per-asset improvisation.",
            "Period-end posting discipline: expense booked, accumulated depreciation rolled, book value reported.",
            "The DDB-to-straight-line crossover computed so book value lands exactly on salvage.",
            "Documented, prospective treatment of life changes and impairments - never silent edits to posted history.",
        ],
        "standards": [
            "Book depreciation follows ASC 360, Property, Plant, and Equipment.",
            "Tax depreciation follows IRS Publication 946 (MACRS property classes and tables).",
            "Governmental depreciation reporting follows GASB Statement 34.",
        ],
        "citations": [CIT_ASC360, CIT_IRS946, CIT_GASB34],
        "sig_lens": (
            "The Signature read: depreciation is the honest accounting of "
            "the asset's slow giving of itself - year by year, the trust "
            "spent in service. The Signature method keeps the schedule as "
            "a vow: the same measure every period, the crossover computed "
            "true, the salvage honored at the end. What was entrusted is "
            "accounted for to the last dollar of its working life."
        ),
    },
    {
        "key": "cmdb_records",
        "name": "CMDB-Style Configuration Records",
        "group": "Compounded",
        "ladder_rank": 4,
        "ladder_tier": "compounded",
        "description": (
            "A configuration record treats an asset not as an isolated "
            "object but as a node in a web: this server runs that "
            "application, depends on that switch, sits in that rack, and "
            "is covered by that support contract. CMDB - configuration "
            "management database - is the IT world's name for this web, "
            "and the pattern applies far beyond IT: a production line's "
            "assets relate to each other the same way. Each configuration "
            "item (CI) carries its attributes - the usual register fields "
            "plus configuration specifics like firmware version, IP "
            "address, or calibration due date - and its relationships: "
            "runs-on, depends-on, connects-to, contains, supports. The "
            "relationships are the payoff. When the core switch needs an "
            "outage window, the CI web answers 'what breaks' in seconds. "
            "When a server fails, the web shows which business services "
            "lose their footing. When a firmware update is planned, the "
            "web lists every CI carrying that firmware. Building the web "
            "is the hard part - relationships must be discovered or "
            "declared and then maintained, because a CMDB that drifts from "
            "reality becomes a map of a country that no longer exists. "
            "This record teaches CIs, relationship types, and the "
            "discipline that keeps the web true."
        ),
        "how_it_works": (
            "Configuration records work by separating the item from its "
            "connections. The CI record holds attributes - identity, "
            "configuration state (firmware, version, settings baseline), "
            "ownership, and status. Relationship records hold the edges: "
            "CI-A depends-on CI-B, CI-C runs-on CI-D, each typed, dated, "
            "and sourced (declared by an engineer or discovered by a "
            "scanner). Queries walk the web: impact analysis walks "
            "downstream from a CI to find everything that depends on it; "
            "root-cause analysis walks upstream to find what a failing CI "
            "depends on. The web stays true through three feeds: "
            "authorized change (every approved change updates the affected "
            "CIs as part of the change), automated discovery (scanners "
            "reconcile the actual network against the web on a schedule), "
            "and audit (samples of CIs verified by hand). Drift is "
            "detected as disagreement - discovery finds a switch the web "
            "does not know, or a CI the web claims is live answers no "
            "ping - and each disagreement becomes a task, not a shrug. "
            "The golden rule: no change without a CI update, no CI update "
            "without an authorized change or a verified discovery."
        ),
        "key_points": [
            "A configuration item is a node; relationships (depends-on, runs-on, connects-to, contains) are the edges - the web is the payoff.",
            "Impact analysis walks downstream ('what breaks'); root-cause walks upstream ('what does it depend on').",
            "The web stays true through three feeds: authorized changes, automated discovery, and hand audits.",
            "Disagreement between discovery and the web is a task, not a shrug - drift detected is drift assigned.",
            "Golden rule: no change without a CI update, no CI update without an authorized change or verified discovery.",
        ],
        "requirements": [
            "A CI record per managed asset with configuration-state attributes (versions, settings baseline) beyond the register basics.",
            "Typed, dated, sourced relationship records - declared or discovered, never assumed.",
            "Authorized-change integration: every change updates affected CIs as a formal change task.",
            "Scheduled automated discovery reconciled against the web, with disagreements worked as tasks.",
            "Periodic hand audits of CI samples to calibrate both the web and the discovery tools.",
        ],
        "standards": [
            "Configuration management practice follows ITIL 4 (Axelos, 2019).",
            "CI identification and control aligns with ISO/IEC 19770-1:2017.",
            "Asset information integrity follows ISO 55001:2014 clause 7.5 (revised 2024).",
        ],
        "citations": [CIT_ITIL4, CIT_ISO19770, CIT_ISO55001],
        "sig_lens": (
            "The Signature read: the configuration web is the map of "
            "fellowship among the entrusted things - which leans on which, "
            "which serves which. The Signature method charts the "
            "fellowship because no asset labors alone, and to tend one "
            "without knowing its fellows is to tend blindly. The web is "
            "kept true as a vow: every change recorded, every discovery "
            "reconciled."
        ),
    },
    {
        "key": "work_orders",
        "name": "Maintenance History and Work Orders",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "The work order is the unit of maintenance: a documented job "
            "against an asset, carrying what was wrong, what was done, who "
            "did it, what parts were used, how long it took, and what it "
            "cost. Stacked over years, work orders become the asset's "
            "medical file - the complete maintenance history that tells "
            "whether this pump is a reliable workhorse or a chronic "
            "patient. History separates the two great maintenance "
            "strategies: reactive history (failures and their repairs) "
            "feeds reliability analysis - MTBF, bad actors, failure modes - "
            "while preventive history (scheduled services completed) proves "
            "the program is being executed. A work order done well has "
            "seven parts: the asset and its tag, the problem or task "
            "description, the priority, the plan (craft, estimated hours, "
            "parts, safety permits), the execution notes (what was actually "
            "found and done), the measurements taken, and the closeout "
            "(actual hours, parts consumed, total cost, follow-up needed). "
            "The failure-mode field is the gold: 'bearing seized due to "
            "lubrication starvation' teaches; 'fixed pump' teaches nothing. "
            "This record teaches the seven-part work order and the history "
            "discipline that turns repairs into knowledge."
        ),
        "how_it_works": (
            "Maintenance history works by accumulation with structure. "
            "Every job opens a work order against the asset's tag before "
            "work begins - no tag, no history, which is why emergency "
            "repairs get their orders written the same shift, not the "
            "next week. The technician records the as-found condition "
            "(the failure mode in specific terms), the as-left condition "
            "(what was done, measurements proving it), parts consumed "
            "(linked to the spares inventory), and actual hours by craft. "
            "Closeout is a gate, not a formality: the supervisor reviews "
            "for completeness, the cost posts to the asset's history, and "
            "any follow-up spawns its own order. Analysis then mines the "
            "accumulation: failure codes rolled up reveal the bad actors "
            "(the 10 percent of assets eating 50 percent of the budget), "
            "MTBF computed per class sets PM intervals honestly, and "
            "repeat failure modes trigger root-cause work. The register "
            "links every order to the asset, so the full file is one "
            "click: birth, every illness, every treatment, total cost of "
            "care. An asset with a thick, specific history is manageable; "
            "an asset with 'fixed pump' times forty is a mystery with a "
            "maintenance budget."
        ),
        "key_points": [
            "The work order is the unit of maintenance - seven parts: asset, problem, priority, plan, execution notes, measurements, closeout.",
            "The failure-mode field is the gold: specific as-found/as-left notes teach; 'fixed pump' teaches nothing.",
            "History accumulates into reliability intelligence: bad actors, MTBF per class, repeat failure modes.",
            "Emergency repairs get their orders written the same shift - no tag, no history.",
            "Closeout is a gate: supervisor review, cost posted to the asset, follow-up spawned as its own order.",
        ],
        "requirements": [
            "A work order opened against the asset tag for every job, including emergencies (same shift).",
            "As-found and as-left documentation with specific failure modes and proving measurements.",
            "Parts consumed linked to spares inventory; actual hours recorded by craft.",
            "Supervisor closeout review before cost posts to the asset's history.",
            "Failure-code taxonomy maintained centrally so roll-up analysis compares like with like.",
        ],
        "standards": [
            "Maintenance documentation practices follow NFPA 70B:2023 for electrical equipment.",
            "Reliability metric definitions (MTBF and related) follow SMRP Best Practices.",
            "Work management processes align with ISO 55002:2018 guidance on operations and maintenance.",
        ],
        "citations": [CIT_NFPA70B, CIT_SMRP, CIT_ISO55002],
        "sig_lens": (
            "The Signature read: the work order is the physician's note in "
            "the asset's medical file - every illness witnessed, every "
            "treatment recorded, in specific and honest terms. The "
            "Signature method writes the file as if the asset itself will "
            "read it one day, because the file is how the next keeper "
            "learns what the last keeper learned in the dark."
        ),
    },
    {
        "key": "pm_scheduling",
        "name": "Preventive and Predictive Maintenance Scheduling",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "Preventive maintenance (PM) services assets on a schedule - "
            "every 90 days, every 500 hours - to prevent failures. "
            "Predictive maintenance (PdM) services them on condition - "
            "when vibration, temperature, or oil analysis says the failure "
            "is coming. PM is calendar honesty: the manufacturer's "
            "recommended intervals, adjusted by experience, executed "
            "whether the asset looks needy or not. Its weakness is "
            "waste - servicing healthy assets, and worse, introducing "
            "failures during the service (the maintenance-induced "
            "failure). PdM is instrument honesty: the bearing gets "
            "changed when vibration trend crosses the alarm, not before, "
            "not after. Its price is instrumentation and expertise - "
            "sensors, routes, analysts who can read a spectrum. The mature "
            "program blends them: PM for the simple and cheap (filters, "
            "lubrication, inspections), PdM for the critical and expensive "
            "(large motors, compressors, turbines), and run-to-failure "
            "deliberately for the non-critical and cheap (a 20 dollar fan "
            "in a non-critical spot). Scheduling is the operational art: "
            "PMs grouped by asset and area into routes, balanced across "
            "weeks so the crew is never crushed, coordinated with "
            "production windows. This record teaches the three strategies, "
            "the blend rule, and the scheduling discipline."
        ),
        "how_it_works": (
            "PM scheduling works as a living calendar fed by three "
            "sources. The PM master holds every task: the asset class it "
            "applies to, the interval (calendar, runtime hours, or "
            "cycles), the procedure, the craft and estimated hours, and "
            "the parts kit. The scheduler generates work orders ahead - "
            "due dates computed from last completion plus interval, with "
            "runtime-hour intervals read from meters - and balances them "
            "across the crew's capacity by week. PdM adds the condition "
            "feed: routes collect vibration, infrared, ultrasound, and oil "
            "samples on their own cadence; the analyst trends each point "
            "and raises the alarm at the warning threshold, which spawns "
            "a corrective work order while there is still time to plan. "
            "Compliance is the metric that matters: PMs completed on time "
            "divided by PMs due - below 90 percent the program is theater. "
            "Intervals are tuned by history: a PM that never finds anything "
            "in three years gets its interval extended; a failure between "
            "PMs gets the interval shortened or a PdM technique added. "
            "The schedule is a promise to the assets, kept in public on "
            "the board, measured every month."
        ),
        "key_points": [
            "PM services on schedule, PdM services on condition, run-to-failure is a deliberate choice for the non-critical and cheap.",
            "The blend rule: PM for simple/cheap, PdM for critical/expensive, run-to-failure for trivial - chosen per asset, not per plant.",
            "PM compliance (done on time over due) below 90 percent means the program is theater.",
            "Intervals are tuned by history: PMs that never find anything get extended; failures between PMs get shortened intervals or PdM added.",
            "PdM alarms must spawn planned corrective work while there is still time - prediction without planning is just worry.",
        ],
        "requirements": [
            "A PM master per asset class: task, interval basis, procedure, craft, hours, and parts kit.",
            "Due-date computation from last completion plus interval, with meter-based intervals read from actual meters.",
            "Weekly capacity balancing so the crew load is level and production windows are respected.",
            "A PdM route structure with trending and alarm thresholds per measurement point.",
            "Monthly compliance measurement and interval tuning driven by the work-order history.",
        ],
        "standards": [
            "Preventive maintenance practices for electrical equipment follow NFPA 70B:2023.",
            "PdM technique application follows ISO 55002:2018 operations guidance.",
            "Reliability-centered task selection aligns with the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_NFPA70B, CIT_ISO55002, CIT_IAM],
        "sig_lens": (
            "The Signature read: preventive care is the keeping of the "
            "covenant on schedule, predictive care the listening for the "
            "asset's early warnings. The Signature method tends before "
            "the breaking where tending is cheap, listens with instruments "
            "where the asset is precious, and lets the trivial go with a "
            "clear conscience - each asset kept according to its worth, "
            "none neglected, none fussed over."
        ),
    },
    {
        "key": "warranty",
        "name": "Warranty Tracking and Claims",
        "group": "Compounded",
        "ladder_rank": 5,
        "ladder_tier": "compounded",
        "description": (
            "A warranty is a manufacturer's promise with an expiration "
            "date, and untracked warranties are promises left to rot - "
            "industry studies routinely find organizations paying for "
            "repairs that were covered, because nobody knew the coverage "
            "existed. Warranty tracking records, per asset: the provider, "
            "the coverage terms (parts, labor, on-site, advance "
            "replacement), the start date (often the in-service date, not "
            "the purchase date), the duration, and the claim procedure "
            "with its phone number and portal. The register computes days "
            "remaining and raises the flag at ninety, sixty, and thirty "
            "days before expiry - the last service window, when a thorough "
            "inspection can surface covered defects while they are still "
            "free to fix. The claim discipline is its own art: report "
            "promptly (late notice voids claims), document the failure "
            "with the as-found evidence, follow the provider's process "
            "exactly, and never let a third party open the unit first if "
            "the terms forbid it. Extended warranties and service "
            "contracts get the same tracking - they are warranties with a "
            "price tag, and their renewal decision needs the failure "
            "history to be rational. This record teaches the coverage "
            "record, the expiry countdown, and the claim discipline that "
            "turns paper promises into free repairs."
        ),
        "how_it_works": (
            "Warranty tracking works as a countdown with teeth. At "
            "acquisition, the registrar records the warranty terms from "
            "the contract - not the salesman's summary - including what "
            "is covered, what voids it, the start trigger, and the exact "
            "claim channel. The register computes expiry and watches it: "
            "at ninety days out, the asset gets a pre-expiry inspection "
            "task; any defect found becomes a claim filed immediately, "
            "with the inspection report as evidence. When a failure "
            "occurs inside coverage, the work order checks the warranty "
            "flag first - the procedure branches: covered failures follow "
            "the claim process (provider authorization before work, "
            "provider parts, documented labor), non-covered failures "
            "follow normal maintenance. Every claim is logged with its "
            "outcome and recovery amount, building the data for the "
            "extended-warranty renewal decision: if three years of claims "
            "recovered twice the contract price, renew; if the asset never "
            "failed, self-insure. The register's warranty report, run "
            "monthly, lists expiring coverage, open claims, and lifetime "
            "recovery per asset - the proof that the promises are being "
            "collected."
        ),
        "key_points": [
            "Untracked warranties are paid-for repairs left unclaimed - the register must know every coverage and its expiry.",
            "Record terms from the contract, not the sales summary: what is covered, what voids it, the start trigger, the claim channel.",
            "The ninety-day pre-expiry inspection turns the last covered window into free repairs for defects found in time.",
            "Covered failures branch the work order into the claim process: provider authorization before work, documented everything.",
            "Claim history drives the extended-warranty renewal decision with arithmetic, not anxiety.",
        ],
        "requirements": [
            "Per-asset warranty record: provider, terms, start date and trigger, duration, exclusions, claim procedure.",
            "Automated expiry countdown with inspection tasks at ninety, sixty, and thirty days.",
            "Work-order branching: warranty check before any repair on a covered asset.",
            "Claim logging with outcome and recovery amount per asset.",
            "Monthly warranty report: expiring coverage, open claims, lifetime recovery.",
        ],
        "standards": [
            "Warranty record-keeping aligns with ISO 55001:2014 asset information requirements (revised 2024).",
            "Contract warranty terms reference the Uniform Commercial Code provisions on express warranty where applicable.",
            "IT warranty and support tracking aligns with ISO/IEC 19770-1:2017.",
        ],
        "citations": [CIT_ISO55001, CIT_ISO19770, CIT_ISO55002],
        "sig_lens": (
            "The Signature read: a warranty is another's promise laid "
            "alongside your own keeping - and a promise unclaimed is a "
            "gift refused. The Signature method watches every promise's "
            "horizon, inspects before the sun sets on it, and claims what "
            "is owed promptly and with full documentation. Honor the "
            "maker's word by holding him to it."
        ),
    },
    {
        "key": "calibration",
        "name": "Calibration Management and Traceability",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Calibration is the proof that a measuring instrument tells the "
            "truth: the comparison of its readings against a known standard, "
            "with adjustments or corrections documented. Every measurement "
            "the organization relies on - torque wrenches, pressure gauges, "
            "multimeters, scales, dimensional tools - stands on calibration, "
            "and an uncalibrated instrument's readings are opinions, not "
            "data. The calibration record carries: the instrument's tag, "
            "the required accuracy, the interval (often annual, shorter for "
            "harsh use), the standard it was compared against, the as-found "
            "and as-left readings, the pass/fail verdict, the date, and the "
            "technician. Traceability is the chain upward: this gauge was "
            "compared to that lab standard, which was compared to a "
            "national standard - an unbroken chain to the SI units, each "
            "link documented. The critical discipline is the out-of-"
            "tolerance response: when an instrument fails calibration, "
            "every measurement it made since its last good calibration is "
            "suspect, and the organization must assess the impact - which "
            "products, which acceptances, which safety checks are now in "
            "doubt. This record teaches the calibration record, the "
            "traceability chain, and the out-of-tolerance reckoning."
        ),
        "how_it_works": (
            "Calibration management works as a recall system with a memory. "
            "The register holds every measuring instrument with its "
            "interval; the system generates calibration work orders ahead "
            "of due dates, and instruments past due are flagged - and in "
            "strict programs, physically tagged out of service until "
            "calibrated. The calibration itself compares the instrument "
            "against a standard at multiple points across its range; the "
            "as-found readings show how it arrived (the truth about the "
            "last interval), adjustments are made, and the as-left "
            "readings prove how it leaves. The certificate records the "
            "standard's own ID and due date - the next link in the "
            "traceability chain - plus uncertainty figures. If as-found is "
            "out of tolerance, the out-of-tolerance procedure fires: the "
            "instrument is quarantined, the usage log is pulled, and every "
            "measurement since the last good calibration is reviewed for "
            "impact - product held, tests repeated, customers notified if "
            "required. Intervals are tuned by as-found history: instruments "
            "always in tolerance earn longer intervals; chronic drifters "
            "get shorter ones or retirement."
        ),
        "key_points": [
            "An uncalibrated instrument produces opinions, not data - every relied-upon measurement stands on calibration.",
            "The record carries as-found and as-left readings: how it arrived is the truth about the last interval; how it leaves is the promise for the next.",
            "Traceability is an unbroken documented chain from the instrument up through lab standards to the SI units.",
            "Out-of-tolerance findings trigger a reckoning: every measurement since the last good calibration is suspect until assessed.",
            "Intervals are tuned by as-found history - steady instruments earn longer intervals, drifters get shorter ones.",
        ],
        "requirements": [
            "A calibration record per measuring instrument: required accuracy, interval, standard used, as-found/as-left, verdict, date, technician.",
            "Recall scheduling ahead of due dates; past-due instruments flagged and, in strict programs, removed from service.",
            "Documented traceability chain: each standard's ID, its own calibration date, and uncertainty.",
            "An out-of-tolerance procedure: quarantine, usage-log pull, impact assessment on prior measurements.",
            "Interval tuning driven by as-found history, with justification recorded.",
        ],
        "standards": [
            "Calibration laboratory competence follows ISO/IEC 17025:2017.",
            "Measurement traceability concepts follow the International Vocabulary of Metrology (VIM).",
            "Electrical test equipment calibration intervals follow manufacturer guidance cross-checked with NFPA 70B:2023.",
        ],
        "citations": [CIT_ISO55001, CIT_NFPA70B, CIT_ISO55002],
        "sig_lens": (
            "The Signature read: calibration is the keeping of true "
            "measure - the vow that when the steward says 'this much,' it "
            "is this much. The Signature method chains every measure to "
            "the unchanging standards above it, link by link, and when a "
            "measure is found false, it reckons honestly with everything "
            "the false measure touched. Truth in measurement is truth in "
            "stewardship."
        ),
    },
    {
        "key": "audits",
        "name": "Asset Audits and Physical Verification",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "An asset audit is the confrontation between the register and "
            "reality: go look, touch the tag, and confirm the asset exists, "
            "is where the register says, and is in the condition the "
            "register claims. Three audit styles cover the need. The "
            "wall-to-wall audit verifies everything - the full "
            "confrontation, done annually or biennially, the gold standard "
            "that auditors and insurers respect. Cycle counting verifies a "
            "rotating sample continuously - Building B in January, the "
            "vehicle fleet in February - so the whole register is touched "
            "over the year without the operational shock of a full "
            "shutdown count. The targeted audit verifies a slice: all "
            "laptops after a reorganization, all assets at a closing site. "
            "Every audit produces the same three numbers: found as recorded "
            "(the match rate - the register's truth score), found but wrong "
            "(location or condition errors to correct), and not found "
            "(the ghosts - missing assets that trigger investigation). "
            "There is a fourth number the honest audit captures: found but "
            "not recorded - the orphans, assets with no register row, "
            "which reveal purchases that bypassed receiving. This record "
            "teaches the three styles, the four numbers, and the "
            "reconciliation that follows."
        ),
        "how_it_works": (
            "An audit works as a planned sweep with independent eyes. "
            "Planning picks the style and scope, freezes a snapshot of the "
            "register for the audit area, and assigns auditors who do not "
            "own the assets they count - independence is what makes the "
            "numbers believable. Execution is physical: the auditor walks "
            "the area with the list, scans or reads each tag, and records "
            "found, location, and observed condition; then walks the area "
            "again looking for tagged assets not on the list - the "
            "orphan hunt. Reconciliation sorts every asset into the four "
            "buckets: matched, found-with-errors (register corrected on "
            "the spot), not found (investigation opened: transferred "
            "without paperwork, stolen, scrapped without a form, or "
            "simply in the wrong room), and unrecorded (register row "
            "created, and the bypass of receiving investigated). The match "
            "rate is reported - 98 percent matched is a healthy register; "
            "below 90 percent is a register nobody should trust - and "
            "every correction is logged so the audit improves the register "
            "instead of just judging it. Findings feed prevention: repeat "
            "ghosts from one department mean its transfer discipline is "
            "broken, and the fix is aimed there."
        ),
        "key_points": [
            "Three styles: wall-to-wall (everything, annually), cycle counting (rotating samples, continuous), targeted (a slice, on events).",
            "Four numbers: matched, found-with-errors, not found (ghosts), found-but-unrecorded (orphans).",
            "Auditors must not own what they count - independence makes the numbers believable.",
            "Match rate is the register's truth score: 98 percent is healthy, below 90 percent is untrustworthy.",
            "Every correction is logged and findings feed prevention - the audit improves the register, not just judges it.",
        ],
        "requirements": [
            "An audit calendar: wall-to-wall on rotation, cycle counts monthly, targeted audits on reorganizations and site events.",
            "A frozen register snapshot per audit scope, so the count is judged against a fixed list.",
            "Independent auditors - never the custodians of the assets being counted.",
            "Reconciliation of all four buckets with investigations opened for ghosts and receiving-bypasses for orphans.",
            "Match-rate reporting with logged corrections and preventive actions aimed at repeat failure points.",
        ],
        "standards": [
            "Physical inventory verification aligns with ISO 55001:2014 asset information requirements (revised 2024).",
            "Governmental inventory practices follow GASB Statement 34 capital asset inventory guidance.",
            "IT asset verification follows ISO/IEC 19770-1:2017 inventory requirements.",
        ],
        "citations": [CIT_ISO55001, CIT_GASB34, CIT_ISO19770],
        "sig_lens": (
            "The Signature read: the audit is the day of reckoning, when "
            "the ledger is laid beside the world and the two are asked to "
            "agree. The Signature method welcomes the reckoning - walks "
            "every room, touches every tag, counts the ghosts honestly "
            "and names the orphans. A ledger afraid of the audit is a "
            "ledger already false."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "utilization",
        "name": "Asset Utilization and Performance Metrics",
        "group": "Compounded",
        "ladder_rank": 6,
        "ladder_tier": "compounded",
        "description": (
            "Utilization is the fraction of available time an asset "
            "actually works - a press running 6 hours of an 8-hour shift "
            "is at 75 percent. It is the simplest performance metric and "
            "the most politically charged, because low utilization asks "
            "whether the asset should exist at all. Measured honestly, "
            "utilization separates three stories: the asset is "
            "underutilized (bought too big, demand fell, or it sits idle "
            "while a twin is rented), the asset is overutilized (running "
            "past its design duty, burning its life early, with no "
            "maintenance window), or the asset is right-sized. The honest "
            "measurement excludes planned downtime - utilization is "
            "operating hours over available hours, not over calendar "
            "hours - and it needs a real meter: hour meters, telematics, "
            "badge logs, production counts. Utilization drives the "
            "hardest decisions: consolidate two half-used machines into "
            "one, sell the idle, rent instead of own the rarely-needed, "
            "and add capacity where utilization is pinned at 95 percent "
            "with overtime. Paired with cost per operating hour, it "
            "answers the value question: this asset costs 180 dollars per "
            "hour it actually works - is the work worth it. This record "
            "teaches the measurement, the three stories, and the "
            "decisions each one demands."
        ),
        "how_it_works": (
            "Utilization works by metering, baselining, and acting. "
            "Metering: each asset class gets its honest counter - hour "
            "meters on equipment, odometers and engine hours on vehicles, "
            "logins or transaction counts on IT assets, production counts "
            "on machines. Baselining: available hours are defined per "
            "asset (two shifts, five days, minus planned maintenance "
            "windows), and utilization equals operating hours divided by "
            "available hours. Acting: the fleet is sorted into bands - "
            "below 30 percent is the challenge list (justify, share, sell, "
            "or rent-out), 30 to 85 percent is the healthy band, above 85 "
            "percent sustained is the capacity warning (add, relieve, or "
            "accept the overtime and wear). Cost per operating hour "
            "sharpens the picture: total annual cost (depreciation, "
            "maintenance, energy, insurance) divided by operating hours "
            "shows which assets are expensive per unit of work. The "
            "trends matter more than snapshots: utilization climbing year "
            "over year signals coming capacity pain; falling signals "
            "surplus to harvest. The register holds the meters and the "
            "bands, and the quarterly utilization review is where the "
            "fleet gets right-sized."
        ),
        "key_points": [
            "Utilization is operating hours over available hours - planned downtime is excluded, and it needs a real meter.",
            "Three stories: underutilized (too big or idle), overutilized (burning life early), right-sized.",
            "Below 30 percent is the challenge list; above 85 percent sustained is the capacity warning.",
            "Cost per operating hour answers the value question: total annual cost divided by hours actually worked.",
            "Trends beat snapshots: climbing utilization warns of capacity pain, falling utilization signals surplus to harvest.",
        ],
        "requirements": [
            "An honest operating counter per asset class: hour meters, odometers, logins, production counts.",
            "Defined available hours per asset (shifts minus planned maintenance) as the denominator.",
            "Utilization bands with assigned actions: challenge, healthy, capacity warning.",
            "Cost-per-operating-hour computed annually per asset from full cost.",
            "A quarterly utilization review that right-sizes the fleet: consolidate, sell, rent, or add.",
        ],
        "standards": [
            "Performance measurement practices align with ISO 55001:2014 clause 9.1 monitoring and measurement (revised 2024).",
            "Equipment effectiveness concepts align with SMRP Best Practices metric definitions.",
            "Fleet utilization reporting follows the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_ISO55001, CIT_SMRP, CIT_IAM],
        "sig_lens": (
            "The Signature read: utilization is the accounting of the "
            "asset's days - how many were spent in service and how many "
            "in idleness. The Signature method counts the days honestly, "
            "challenges the idle without cruelty, relieves the "
            "overburdened without delay, and never asks an asset to "
            "justify its existence without first asking whether the "
            "steward gave it work worthy of it."
        ),
    },
    {
        "key": "spare_parts",
        "name": "Spare Parts Linkage and Inventory",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A spare part is an asset's future repair, bought in advance: "
            "the bearing, seal kit, belt, or board that will be needed "
            "when the asset fails. Spare parts linkage ties each part in "
            "the storeroom to the assets that consume it - this seal kit "
            "fits pumps P-101 through P-108 - so a work order can reserve "
            "the right part and the storeroom knows why it stocks what it "
            "stocks. The discipline balances two costs: the carrying cost "
            "of inventory (capital tied up, space, obsolescence, "
            "typically 20 to 30 percent of inventory value per year) "
            "against the stockout cost (downtime while waiting for the "
            "part - thousands per hour on a critical line). The linkage "
            "makes the balance rational: critical spares for critical "
            "assets with long lead times are stocked; non-critical parts "
            "with next-day availability are not. Each stocked part gets a "
            "reorder point (order when stock hits this level) and an order "
            "quantity, computed from usage rate and lead time. Parts are "
            "classified too - critical, insurance, and routine - because "
            "a 40,000 dollar insurance spare for a turbine gets different "
            "treatment than a box of fuses. This record teaches the "
            "asset-to-part linkage, the carrying-versus-stockout balance, "
            "and the reorder arithmetic."
        ),
        "how_it_works": (
            "Spare parts linkage works as a bill of materials in reverse. "
            "For each asset class, the bill of spares lists the parts the "
            "asset consumes: part number, description, quantity per asset, "
            "and the assets it fits. The storeroom record adds: on-hand "
            "quantity, unit cost, supplier and lead time, reorder point, "
            "and order quantity. The reorder point equals daily usage times "
            "lead time in days, plus safety stock (usage variability times "
            "a service factor) - when on-hand falls to the point, the "
            "system raises the order. Usage history tunes the numbers: "
            "the seal kit that moves four times a year with a 30-day lead "
            "time earns a reorder point of one plus safety; the fuse that "
            "moves twice a decade with next-day supply earns a point of "
            "zero - buy on demand. Criticality overrides the math where "
            "it must: the insurance spare with a 26-week lead time for a "
            "critical compressor is stocked at one regardless of usage, "
            "because the stockout cost dwarfs the carrying cost. Work "
            "orders consume against the linkage - parts issued to the "
            "asset's tag - so usage history stays honest and the next "
            "reorder point computes from truth."
        ),
        "key_points": [
            "Linkage ties each stocked part to the assets that consume it - the storeroom knows why it stocks what it stocks.",
            "The balance is carrying cost (20-30 percent of inventory value yearly) against stockout cost (downtime per hour).",
            "Reorder point equals daily usage times lead time plus safety stock - the arithmetic of never running out.",
            "Criticality overrides the math: long-lead insurance spares for critical assets are stocked regardless of usage.",
            "Work orders consume parts against the asset tag, keeping usage history honest for the next computation.",
        ],
        "requirements": [
            "A bill of spares per asset class: part number, fitment list, quantity per asset.",
            "Per-part storeroom data: on-hand, unit cost, supplier, lead time, reorder point, order quantity.",
            "Criticality classification per part: critical, insurance, or routine, driving stocking policy.",
            "Work-order parts issue against the asset tag, not against the ether.",
            "Annual review of reorder points against actual usage and lead-time changes.",
        ],
        "standards": [
            "Materials management practices align with ISO 55002:2018 guidance on resource provision.",
            "Inventory record accuracy practices follow the Institute of Asset Management Anatomy v4.",
            "IT spare parts tracking aligns with ISO/IEC 19770-1:2017.",
        ],
        "citations": [CIT_ISO55002, CIT_IAM, CIT_ISO19770],
        "sig_lens": (
            "The Signature read: the spare is providence - the repair "
            "bought before the breaking, mercy stocked on the shelf. The "
            "Signature method links every spare to the assets it will one "
            "day heal, balances the cost of readiness against the cost of "
            "waiting, and never lets a critical asset's future hang on a "
            "part with a half-year lead time and an empty bin."
        ),
    },
    {
        "key": "criticality",
        "name": "Asset Risk and Criticality Assessment",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "Criticality is the ranking of assets by the consequences of "
            "their failure - because not every asset deserves the same "
            "care, and pretending they do spreads maintenance thin where "
            "it matters and thick where it does not. The assessment scores "
            "each asset on consequence factors: safety impact (could "
            "failure hurt someone), environmental impact, production or "
            "service impact (how much stops, for how long), repair cost, "
            "and redundancy (is there a standby). Each factor gets a "
            "1-to-5 score against written criteria; the weighted sum is "
            "the criticality rank - often A (critical), B (important), or "
            "C (routine). The rank then rations everything: A assets get "
            "PdM routes, stocked spares, and priority scheduling; C assets "
            "get basic PM and run-to-failure where sensible. Risk is "
            "criticality times likelihood - a critical asset with a "
            "well-controlled failure mode is less risky than a critical "
            "asset with an unmanaged one - and the risk register holds the "
            "pairs: asset, failure mode, consequence, likelihood, "
            "controls, residual risk. Reassessment is scheduled - annually, "
            "and after any significant change - because criticality drifts "
            "as processes change. This record teaches the scoring, the "
            "A-B-C rationing, and the risk pairing."
        ),
        "how_it_works": (
            "Criticality assessment works as a facilitated scoring with "
            "consequences. A cross-functional team - operations, "
            "maintenance, safety, engineering - scores each asset class "
            "against the consequence criteria, debating to consensus; the "
            "facilitator's job is preventing the two classic distortions, "
            "everything-is-critical and nothing-is-critical. Scores are "
            "weighted (safety typically heaviest) and summed into the "
            "A-B-C rank, which is recorded on the asset and inherited by "
            "new assets of the class. The rank drives the maintenance "
            "strategy matrix: A means condition monitoring, stocked "
            "critical spares, priority parts and labor, and inclusion in "
            "the bad-actor review; B means standard PM and planned "
            "corrective; C means basic care and deliberate run-to-failure "
            "where economic. Risk pairing adds likelihood: for each "
            "credible failure mode of A and B assets, the team scores "
            "likelihood, lists existing controls, and computes residual "
            "risk - the unacceptable residuals become projects. The "
            "assessment is revisited annually and after process changes, "
            "MOC events, or significant incidents, because the plant of "
            "2026 is not the plant of 2024."
        ),
        "key_points": [
            "Criticality ranks assets by failure consequences - the rationing key for all maintenance resources.",
            "Scored 1-5 on safety, environmental, production, cost, and redundancy against written criteria, weighted with safety heaviest.",
            "A-B-C ranks drive strategy: A gets PdM and stocked spares, C gets basic care and deliberate run-to-failure.",
            "Risk is criticality times likelihood per failure mode; unacceptable residual risk becomes a project.",
            "Reassess annually and after changes - criticality drifts as the operation changes.",
        ],
        "requirements": [
            "Written consequence criteria per factor with 1-to-5 scales, and documented weights.",
            "Cross-functional facilitated scoring to consensus, guarded against everything-critical and nothing-critical distortions.",
            "The A-B-C rank recorded on every asset and inherited by class.",
            "A maintenance strategy matrix mapping each rank to monitoring, spares, and scheduling treatment.",
            "A risk register pairing critical assets with failure modes, likelihood, controls, and residual risk.",
        ],
        "standards": [
            "Risk assessment concepts align with ISO 31000:2018 risk management principles.",
            "Criticality practices align with ISO 55002:2018 guidance on risk-based decision-making.",
            "Safety consequence scoring follows the organization's process safety criteria, consistent with NFPA 70B:2023.",
        ],
        "citations": [CIT_ISO55002, CIT_NFPA70B, CIT_IAM],
        "sig_lens": (
            "The Signature read: criticality is the honest weighing of "
            "what each trust's breaking would cost - in safety, in "
            "livelihood, in the work of others. The Signature method "
            "weighs without flinching and without exaggeration, then "
            "keeps each asset according to its weight: the heaviest "
            "trusts watched closest, the lightest released to their "
            "simple fate. Care rationed by truth is care multiplied."
        ),
    },
    {
        "key": "baselines",
        "name": "Configuration Baselines and Change Control",
        "group": "Compounded",
        "ladder_rank": 7,
        "ladder_tier": "compounded",
        "description": (
            "A configuration baseline is the recorded 'known-good' state "
            "of an asset or system at a point in time - firmware versions, "
            "settings, installed components, calibration values - the "
            "reference against which all later states are compared. "
            "Change control is the gate that guards the baseline: no "
            "change without a request, a risk review, an approval, and a "
            "recorded update to the baseline. Together they answer the "
            "two questions every incident eventually asks: 'what changed' "
            "and 'what was it supposed to be.' Baselines are captured at "
            "commissioning, after major maintenance, and after every "
            "approved change; the capture is a snapshot - version numbers, "
            "configuration files, setpoints, parts lists - stored with "
            "the date and the authorizing change. Drift detection compares "
            "the live state to the baseline on a schedule: the unauthorized "
            "firmware update, the setpoint someone 'temporarily' changed "
            "three years ago, the component substituted without a form. "
            "Each drift is either authorized retroactively (with review) "
            "or remediated back to baseline. Emergency changes follow the "
            "same gate at speed - documented after the fact within 24 "
            "hours, never exempted. This record teaches the baseline "
            "snapshot, the change gate, and the drift hunt."
        ),
        "how_it_works": (
            "Baselines and change control work as a loop: capture, guard, "
            "compare, reconcile. Capture: at commissioning and after each "
            "approved change, the technician records the full "
            "configuration state - for a PLC, the program revision, "
            "firmware versions, I/O configuration, and setpoints; for a "
            "server, the OS build, application versions, and security "
            "settings - and the register stores it as the current "
            "baseline with the change record attached. Guard: every "
            "proposed change enters the gate as a request with reason, "
            "risk assessment, backout plan, and approval signature; "
            "emergency changes may proceed on verbal approval but the "
            "paperwork lands within 24 hours. Compare: on a schedule "
            "(and after every incident), the live state is read back and "
            "diffed against the baseline - automated where the asset "
            "supports it, manual checklist where it does not. Reconcile: "
            "every difference is dispositioned - authorized and baselined, "
            "or unauthorized and remediated - and the disposition is "
            "recorded. The loop's product is the change history: the "
            "complete, dated story of what the asset was and became, "
            "which is what the 2 a.m. troubleshooter reads first."
        ),
        "key_points": [
            "The baseline is the recorded known-good state - firmware, settings, components, setpoints - the reference for all comparison.",
            "Change control gates every change: request, risk review, approval, backout plan, baseline update.",
            "Drift detection diffs live state against baseline on schedule; every difference is authorized or remediated.",
            "Emergency changes get speed, not exemption - paperwork within 24 hours.",
            "The change history is the 2 a.m. troubleshooter's first read: what it was, what it became, when, and why.",
        ],
        "requirements": [
            "A baseline capture at commissioning and after every approved change, with date and authorizing change attached.",
            "A change gate with request, risk assessment, approval signature, and backout plan - including the emergency path.",
            "Scheduled live-versus-baseline comparison, automated where the asset supports it.",
            "Disposition of every drift: authorized-and-baselined or unauthorized-and-remediated, recorded.",
            "A complete change history per asset, readable as the story of its configuration life.",
        ],
        "standards": [
            "Change control practice follows ITIL 4 change enablement (Axelos, 2019).",
            "Configuration baseline management aligns with ISO/IEC 19770-1:2017.",
            "Baseline integrity practices follow ISO 55001:2014 clause 7.5 (revised 2024).",
        ],
        "citations": [CIT_ITIL4, CIT_ISO19770, CIT_ISO55001],
        "sig_lens": (
            "The Signature read: the baseline is the remembered face of "
            "the asset - how it looked when it was whole and true. The "
            "Signature method photographs the face at every keeping, "
            "guards it against unrecorded change, and hunts the drift "
            "that time and hands introduce. What changed, and was the "
            "changing authorized - the two questions of every reckoning, "
            "answered from the ledger."
        ),
    },
    {
        "key": "reliability",
        "name": "Reliability Metrics: MTBF, MTTR, and Availability",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "Three numbers tell the reliability story of any asset. MTBF - "
            "mean time between failures - is total operating time divided "
            "by failure count: a pump running 8,000 hours with 4 failures "
            "has a 2,000-hour MTBF. MTTR - mean time to repair - is total "
            "repair downtime divided by failure count: those 4 failures "
            "cost 40 hours, so MTTR is 10 hours. Availability is uptime "
            "over total time: 8,000 operating hours out of 8,040 total "
            "(8,000 up plus 40 down) is 99.5 percent - or equivalently "
            "MTBF divided by (MTBF plus MTTR). The numbers are only honest "
            "with definitions nailed down: what counts as a failure "
            "(functional failure, not every work order), what counts as "
            "operating time, whether planned downtime is excluded. MTBF "
            "predicts spares and staffing - a fleet of 50 pumps at "
            "2,000-hour MTBF suffers about 200 failures per 8,000-hour "
            "year, which sizes the crew and the seal kits. Availability is "
            "the contract number - the SLA, the production promise - and "
            "improving it means raising MTBF (fewer failures, through PM "
            "and PdM) or cutting MTTR (faster recovery, through spares, "
            "procedures, and training). This record teaches the three "
            "metrics, the definitions that keep them honest, and the two "
            "levers that move availability."
        ),
        "how_it_works": (
            "Reliability metrics work by disciplined counting from the "
            "work-order history. The analyst defines the rules first: a "
            "failure is a functional failure (the asset cannot perform its "
            "required function), not a PM finding; operating time is meter "
            "hours; planned maintenance downtime is excluded from "
            "availability's denominator. Then the history is mined: for "
            "the asset or class, sum operating hours, count functional "
            "failures, sum repair downtimes. MTBF equals operating hours "
            "over failures; MTTR equals repair downtime over failures; "
            "availability equals operating hours over (operating hours "
            "plus repair downtime). Small samples lie - an MTBF from two "
            "failures is a rumor - so the metrics are computed per class "
            "across the fleet and trended over rolling twelve-month "
            "windows. The levers are then aimed: falling MTBF triggers "
            "failure-mode analysis and PM/PdM upgrades; high MTTR "
            "triggers spares reviews, procedure writing, and crew "
            "training. Targets are set per criticality - A assets at 99.5 "
            "percent availability, C assets lower - and the monthly "
            "reliability report shows each class against its target, "
            "with the gap named and owned."
        ),
        "key_points": [
            "MTBF is operating hours over failure count; MTTR is repair downtime over failure count; availability is MTBF over (MTBF plus MTTR).",
            "Definitions keep the numbers honest: functional failures only, meter hours, planned downtime excluded.",
            "Small samples lie - compute per class across the fleet on rolling twelve-month windows.",
            "MTBF sizes the future: crew, spares, and PM intervals all derive from the failure rate.",
            "Availability moves on two levers: raise MTBF (fewer failures) or cut MTTR (faster recovery).",
        ],
        "requirements": [
            "Written failure, operating-time, and downtime definitions before the first metric is computed.",
            "Functional-failure coding in work orders so the history mines cleanly.",
            "Class-level computation on rolling twelve-month windows; asset-level only with sufficient history.",
            "Availability targets per criticality rank, reported monthly against actuals.",
            "Named ownership of each gap: falling MTBF gets failure analysis, high MTTR gets spares and procedures.",
        ],
        "standards": [
            "MTBF, MTTR, and availability definitions follow SMRP Best Practices.",
            "Reliability data collection aligns with IEEE Std 493-2007 (Gold Book) methods.",
            "Performance evaluation follows ISO 55001:2014 clause 9.1 (revised 2024).",
        ],
        "citations": [CIT_SMRP, CIT_IEEE493, CIT_ISO55001],
        "sig_lens": (
            "The Signature read: the metrics are the biography reduced to "
            "three honest numbers - how long between stumblings, how swift "
            "the rising, how present the asset stood at its post. The "
            "Signature method counts without flattery and without despair, "
            "trends the numbers like a physician trends a pulse, and "
            "works the two levers - fewer falls, swifter risings - as the "
            "keeping of the covenant demands."
        ),
    },
    {
        "key": "tco",
        "name": "Total Cost of Ownership Modeling",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "The purchase price is the smallest honest number in an "
            "asset's life. Total cost of ownership (TCO) adds every "
            "dollar the asset will consume: acquisition, installation, "
            "energy, consumables, maintenance labor and parts, downtime "
            "cost, training, insurance, and end-of-life disposal or "
            "recovery - minus any residual value. The classic iceberg: a "
            "100,000 dollar compressor with 8,000 dollars a year in "
            "energy, 5,000 in maintenance, and 3,000 in downtime risk "
            "costs 260,000 over ten years - the price was 38 percent of "
            "the truth. TCO models compare alternatives honestly: the "
            "cheap machine with expensive parts versus the premium "
            "machine with a ten-year parts guarantee; keeping the old "
            "asset (rising maintenance, no capital outlay) versus "
            "replacing (capital outlay, warranty, efficiency gains). The "
            "model runs year by year - each year's cost in its year, "
            "because a dollar next year is cheaper than a dollar today "
            "at the discount rate - and the comparison that matters is "
            "usually cost per unit of output: dollars per operating "
            "hour, per mile, per part produced. This record teaches the "
            "cost anatomy, the year-by-year model, and the "
            "keep-versus-replace decision."
        ),
        "how_it_works": (
            "TCO modeling works as a year-by-year ledger for each "
            "alternative. The analyst lists every cost family per year: "
            "year zero holds acquisition and installation; years one "
            "through N hold energy (from metered or nameplate data), "
            "consumables, maintenance (labor plus parts from history or "
            "manufacturer estimates), downtime cost (failure rate times "
            "MTTR times cost per hour), insurance, and training "
            "amortized; the final year subtracts residual value or adds "
            "disposal cost. Future years are discounted to present value "
            "at the organization's rate - the time value of money is not "
            "optional in a ten-year comparison. The alternatives are then "
            "compared on equal terms: same horizon, same output basis, "
            "same discount rate. For keep-versus-replace, the old asset's "
            "remaining TCO (its rising maintenance curve, its efficiency "
            "penalty) faces the new asset's full TCO; replacement wins "
            "when the new machine's annual savings pay back its capital "
            "within the policy window. Sensitivity analysis flexes the "
            "uncertain inputs - energy price, failure rate, utilization - "
            "to check whether the decision survives bad news. The model "
            "is documented assumption by assumption, because a TCO "
            "comparison is only as honest as its inputs."
        ),
        "key_points": [
            "Purchase price is the tip of the iceberg - energy, maintenance, downtime, and disposal usually dwarf it over the life.",
            "The model is year-by-year: every cost family in its year, future years discounted to present value.",
            "Compare alternatives on equal terms: same horizon, same output basis, same discount rate.",
            "Keep-versus-replace pits the old asset's rising maintenance curve against the new asset's capital plus efficiency.",
            "Sensitivity analysis flexes energy price, failure rate, and utilization - the decision must survive bad news.",
        ],
        "requirements": [
            "All cost families per alternative: acquisition, install, energy, consumables, maintenance, downtime, insurance, training, end-of-life.",
            "Year-by-year modeling with present-value discounting at the organization's rate.",
            "Documented assumptions for every input, with sources: metered data, history, or manufacturer figures.",
            "Comparison on a per-output basis (per hour, per mile, per unit) alongside total TCO.",
            "Sensitivity analysis on the three most uncertain inputs before the decision is presented.",
        ],
        "standards": [
            "Life-cycle costing concepts align with ISO 55002:2018 guidance on value realization over the life cycle.",
            "Present-value methods follow standard engineering economics practice.",
            "Cost data integrity follows ISO 55001:2014 asset information requirements (revised 2024).",
        ],
        "citations": [CIT_ISO55002, CIT_ISO55001, CIT_IAM],
        "sig_lens": (
            "The Signature read: total cost is the full weight of the "
            "trust, carried across all its years - not the welcoming "
            "price but the keeping price. The Signature method counts "
            "every cost the asset will ask: its hunger for energy, its "
            "need of tending, its hours of rest, its final disposition. "
            "Only the whole weight, honestly summed and discounted, can "
            "say whether the trust was wisely taken."
        ),
    },
    {
        "key": "iso55000",
        "name": "The ISO 55000 Asset Management Framework",
        "group": "Advanced",
        "ladder_rank": 8,
        "ladder_tier": "advanced",
        "description": (
            "ISO 55000 is the international standard family that turns "
            "asset tracking into asset management - from 'we know what we "
            "own' to 'we extract the most value from what we own over its "
            "whole life.' The family has three parts: ISO 55000 gives the "
            "overview, principles, and terminology - the shared language "
            "(revised in 2024). ISO 55001 states the requirements for an "
            "asset management system: leadership commitment, asset "
            "management policy and objectives, risk-based planning, "
            "support (resources, competence, information), operation, "
            "performance evaluation, and continual improvement - the "
            "management-system clauses an organization can be certified "
            "against (also revised 2024). ISO 55002 gives the guidance "
            "for applying 55001, clause by clause, with examples. The "
            "framework's core logic is the line of sight: organizational "
            "objectives flow down into the asset management policy, into "
            "the strategic asset management plan, into asset management "
            "plans per asset class - and performance flows back up. Risk "
            "is the organizing principle: decisions balance cost, risk, "
            "and performance over the life cycle. Maturity is assessed on "
            "a 0-to-5 scale per clause, and certification audits test "
            "whether the system is real or paper. This record teaches "
            "the three standards, the line of sight, and the maturity "
            "ladder."
        ),
        "how_it_works": (
            "The framework works by cascading intent into action and "
            "evidence back up. Leadership sets organizational objectives "
            "(safety, service levels, financial targets) and signs the "
            "asset management policy - the promise that assets will be "
            "managed for life-cycle value. The strategic asset management "
            "plan (SAMP) translates the policy into long-term direction: "
            "the portfolio's future, funding envelopes, risk appetite. "
            "Asset management plans per class turn direction into work: "
            "the pump fleet's maintenance strategy, renewal forecast, and "
            "resource needs for the next decade. Execution runs through "
            "the registry, work orders, and projects; performance "
            "evaluation measures - condition trends, reliability metrics, "
            "cost versus plan, risk reduction - and management review "
            "asks whether the system is working. Improvement closes the "
            "loop: nonconformities get root cause and correction, and the "
            "plans update. Maturity assessment scores each clause 0 "
            "(absent) to 5 (optimized), usually by facilitated "
            "self-assessment with evidence; the gaps become the "
            "improvement program. Certification, where pursued, is an "
            "external audit against ISO 55001 - and the certificate is "
            "worth exactly what the system's daily reality supports."
        ),
        "key_points": [
            "Three parts: 55000 (language), 55001 (requirements, certifiable), 55002 (guidance) - revised 55000/55001 in 2024.",
            "Line of sight: organizational objectives cascade to policy to strategic plan to per-class plans; performance flows back up.",
            "Risk is the organizing principle: every decision balances cost, risk, and performance over the life cycle.",
            "Maturity is scored 0-5 per clause with evidence; the gaps become the improvement program.",
            "Certification audits test whether the system is real or paper - the certificate is worth what daily reality supports.",
        ],
        "requirements": [
            "A signed asset management policy flowing from organizational objectives.",
            "A strategic asset management plan (SAMP) with long-term portfolio direction and funding envelopes.",
            "Per-class asset management plans: strategy, renewal forecast, resource needs.",
            "Performance evaluation: condition, reliability, cost, and risk metrics reviewed by leadership.",
            "A maturity assessment with evidence per clause and a gap-driven improvement program.",
        ],
        "standards": [
            "ISO 55000:2024. Asset management - Overview, principles and terminology.",
            "ISO 55001:2024. Asset management - Management systems - Requirements.",
            "ISO 55002:2018. Asset management - Management systems - Guidelines for the application of ISO 55001.",
        ],
        "citations": [CIT_ISO55000, CIT_ISO55001, CIT_ISO55002],
        "sig_lens": (
            "The Signature read: the standard is the codified wisdom of "
            "stewards worldwide - the collected answer to 'how shall we "
            "keep what is entrusted.' The Signature method honors the "
            "framework's line of sight as its own: the highest purpose "
            "flowing down to the humblest asset's plan, and the humblest "
            "asset's truth flowing back up. Cost, risk, and performance "
            "held in balance across the whole life - this is stewardship "
            "with its eyes open."
        ),
    },
    {
        "key": "lease_vs_buy",
        "name": "Asset Finance: Leasing Versus Buying",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Leasing versus buying is the financing face of the registry: "
            "two ways to put an asset to work, with different cash flows, "
            "different risks, and different balance-sheet footprints. "
            "Buying means capital outlay now, ownership, depreciation, and "
            "residual risk and reward at the end - the asset is yours to "
            "keep, sell, or run into the ground. Leasing means periodic "
            "payments for the right to use: operating leases (short, "
            "off-balance-sheet under old rules, the lessor keeps residual "
            "risk) and finance or capital leases (long, effectively "
            "purchases with payments, now largely on-balance-sheet under "
            "ASC 842). The honest comparison is net present value of all "
            "cash flows: purchase price and resale versus lease payments, "
            "each with its maintenance, tax, and end-of-term shape. "
            "Leasing wins where technology churns fast (IT equipment), "
            "where the lessor's scale cuts maintenance cost (fleet "
            "vehicles), or where capital is constrained; buying wins where "
            "the asset lives long, holds value, and the organization runs "
            "it well. The registry must track leased assets with the same "
            "discipline as owned - plus lease-specific fields: lessor, "
            "term, payment, end-of-term options (return, renew, buy out), "
            "and return conditions. This record teaches the NPV "
            "comparison and the lease-aware registry."
        ),
        "how_it_works": (
            "The comparison works as a discounted cash-flow duel. The "
            "analyst builds both timelines: buy means outflow of purchase "
            "price and installation at year zero, annual maintenance and "
            "operating costs, tax shield from depreciation, and inflow of "
            "residual value at the horizon; lease means annual lease "
            "payments, any maintenance included or excluded per terms, tax "
            "shield from payments, and end-of-term cost (return fees, "
            "buyout, or renewal). Every future flow is discounted at the "
            "organization's cost of capital to present value, and the "
            "lower NPV wins - with qualitative factors noted alongside: "
            "flexibility (leases end cleanly), technology risk (lessor "
            "absorbs obsolescence in fair-market leases), and balance-"
            "sheet treatment under ASC 842. The registry side runs in "
            "parallel: leased assets get tag, condition, location, and "
            "maintenance like owned ones, plus the lease record - lessor, "
            "contract, term dates, payment schedule, mileage or usage "
            "limits, return-condition standards, and end-of-term options "
            "with decision dates. The system raises the end-of-term "
            "decision a year out: return, renew, or buy out - each priced "
            "from the contract, none left to the last month's panic."
        ),
        "key_points": [
            "The honest comparison is NPV of all cash flows - purchase and resale versus lease payments - each with its maintenance, tax, and end shape.",
            "Leasing wins on churn, scale maintenance, or constrained capital; buying wins on long life, retained value, and operational excellence.",
            "ASC 842 put most leases on the balance sheet - the old off-balance-sheet motive is largely gone; decide on economics.",
            "Leased assets get full registry discipline plus lease fields: lessor, term, payments, return conditions, end-of-term options.",
            "The end-of-term decision (return, renew, buy out) is raised a year out - never left to the last month's panic.",
        ],
        "requirements": [
            "A discounted cash-flow model for both alternatives at the organization's cost of capital, with documented assumptions.",
            "Qualitative factors recorded alongside the NPV: flexibility, technology risk, and operational fit.",
            "Lease accounting treatment per ASC 842 (right-of-use asset and lease liability).",
            "Lease-specific registry fields: lessor, contract, term, payments, usage limits, return standards, end-of-term options.",
            "An end-of-term decision workflow triggered twelve months before lease end.",
        ],
        "standards": [
            "Lease accounting follows ASC 842, Leases (FASB).",
            "Cash-flow comparison methods follow standard engineering economics practice.",
            "Leased-asset information management aligns with ISO 55001:2014 (revised 2024).",
        ],
        "citations": [CIT_ISO55001, CIT_ASC360, CIT_ISO55002],
        "sig_lens": (
            "The Signature read: lease or buy is the question of how the "
            "trust is held - owned outright or borrowed for a season. The "
            "Signature method decides by honest arithmetic of all the "
            "years, keeps borrowed trusts with the same care as owned "
            "ones, and meets the end of every term prepared - returning "
            "what was borrowed in the condition promised, or keeping it "
            "by the contract's own terms."
        ),
    },
])
ENTRIES.extend([
    {
        "key": "health_scoring",
        "name": "Asset Health Scoring and Predictive Replacement",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Asset health scoring compresses everything known about an "
            "asset - age, condition ratings, failure history, maintenance "
            "cost trend, criticality, parts availability - into a single "
            "0-to-100 score that answers 'how much life is left and how "
            "confident are we.' The score is a weighted blend: condition "
            "trend might carry 30 percent, failure and cost history 25, "
            "age versus expected life 20, criticality 15, and parts or "
            "support risk 10 - the weights set by the organization's "
            "experience, documented, and applied uniformly. Bands turn "
            "scores into action: 80-100 is healthy (normal care), 60-79 "
            "is watch (increased monitoring, plan the renewal), 40-59 is "
            "at risk (detailed assessment, renewal funded), below 40 is "
            "replace or rebuild now. Predictive replacement uses the "
            "score's trajectory: when the maintenance cost curve crosses "
            "the annualized replacement cost - the economic life point - "
            "keeping the asset costs more than replacing it, and the "
            "capital plan should already hold its successor. The honest "
            "score is back-tested: last year's 45s should be this year's "
            "failures and replacements; if they are not, the weights are "
            "wrong. This record teaches the weighted score, the action "
            "bands, and the economic-life crossing."
        ),
        "how_it_works": (
            "Health scoring works as a transparent formula run on "
            "schedule. Each input is normalized to 0-100: condition maps "
            "from the 1-5 rating, age maps against expected life (a "
            "12-year-old pump with a 15-year life scores 20 on age), "
            "failure history maps from MTBF versus class average, cost "
            "trend maps from maintenance cost per year versus replacement "
            "annuity, parts risk maps from lead time and obsolescence "
            "flags. The weighted sum is the score, published with its "
            "components - never a black box, because a score nobody can "
            "explain is a score nobody will fund. The fleet is ranked "
            "worst-first, and the capital plan works the list from the "
            "bottom: each candidate gets a replacement business case "
            "comparing remaining-life cost (projected maintenance plus "
            "downtime risk) against replacement cost (capital minus "
            "efficiency gains). The economic-life rule decides timing: "
            "replace when the next year's projected keeping cost exceeds "
            "the annualized cost of the replacement. Scores refresh "
            "quarterly or on major events (a failure, a rebuild), and the "
            "weights are recalibrated annually against what actually "
            "failed - the model learns from the fleet's own history."
        ),
        "key_points": [
            "Health score is a weighted 0-100 blend of condition, age, failure history, cost trend, criticality, and parts risk - transparent, never a black box.",
            "Bands drive action: 80+ healthy, 60-79 watch, 40-59 at risk with renewal funded, below 40 replace or rebuild.",
            "The economic-life point - when keeping costs more per year than replacing - sets replacement timing.",
            "Back-test the model: last year's low scorers should be this year's failures; if not, fix the weights.",
            "The fleet ranks worst-first and the capital plan works the list from the bottom with business cases.",
        ],
        "requirements": [
            "Documented weights and normalization rules for each input, applied uniformly across the fleet.",
            "Score components published alongside the score - explainability is mandatory.",
            "Action bands with assigned responses and funding paths per band.",
            "Quarterly refresh cadence plus event-driven rescoring on failures and rebuilds.",
            "Annual recalibration of weights against actual failure and replacement outcomes.",
        ],
        "standards": [
            "Health assessment practices align with ISO 55002:2018 guidance on asset performance and risk.",
            "Condition inputs follow the organization's rated criteria, consistent with NFPA 70B:2023 where applicable.",
            "Economic-life methods follow standard engineering economics practice.",
        ],
        "citations": [CIT_ISO55002, CIT_NFPA70B, CIT_IAM],
        "sig_lens": (
            "The Signature read: the health score is the physician's "
            "summary after the full examination - one number carrying "
            "the weight of all the testimony. The Signature method scores "
            "in the open, every weight declared, every component shown, "
            "and replaces at the economic crossing without sentimentality "
            "and without delay: to keep a dying asset past its time is "
            "not loyalty, it is neglect of the work it can no longer do."
        ),
    },
    {
        "key": "disposal",
        "name": "Disposal, Decommissioning, and Data Sanitization",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "Disposal is the honorable discharge of the asset: the "
            "planned, documented end that closes every open thread - "
            "financial, legal, environmental, and data. The disposal "
            "path depends on the asset: resale or auction (recovering "
            "value - net recovery equals sale price minus selling costs), "
            "redeployment (transfer to another site, a lifecycle state "
            "change rather than a disposal), donation (fair-value "
            "receipt), recycling (materials recovery with environmental "
            "chain of custody), or destruction (for the obsolete, the "
            "contaminated, or the data-bearing). Decommissioning is the "
            "technical retirement: safe shutdown, disconnection, fluid "
            "and refrigerant recovery, and clearance that the asset holds "
            "no hazard. Data sanitization is the non-negotiable step for "
            "anything that stored information - servers, laptops, phones, "
            "copiers, instruments with memory: NIST SP 800-88 defines "
            "clear, purge, and destroy, matched to the data's "
            "confidentiality. The disposal certificate closes the "
            "register: method, date, proceeds or cost, sanitization "
            "evidence, environmental manifests, and the authorizing "
            "signature. An asset is not gone when it leaves the building; "
            "it is gone when the certificate is filed and the register "
            "state reads Disposed. This record teaches the paths, the "
            "decommissioning sequence, and the sanitization standard."
        ),
        "how_it_works": (
            "Disposal works as a gated workflow that leaves nothing "
            "dangling. Retirement approval opens the case: the asset's "
            "state moves to Retired, and the disposal plan is written - "
            "path selected, data classification checked, environmental "
            "requirements identified, value estimated. Decommissioning "
            "executes first: the asset is safely shut down, disconnected, "
            "drained of fluids and refrigerants by licensed handlers, and "
            "surveyed for hazards (asbestos, PCBs, refrigerants each have "
            "their own rules and manifests). Data-bearing assets go "
            "through sanitization per their classification: clear for "
            "low-risk resale, purge (firmware-level or degauss) for "
            "sensitive, destroy (crush, shred, incinerate) for the "
            "highest - each with a certificate from the process. The "
            "asset then follows its path: auction with proceeds recorded, "
            "recycler with weight tickets and environmental manifests, "
            "donation with the acknowledgment letter. Finance retires the "
            "book value, recognizing gain or loss against proceeds. The "
            "disposal certificate - method, date, proceeds or cost, "
            "sanitization evidence, manifests, signature - is filed to "
            "the asset's history, the state becomes Disposed, and the tag "
            "number retires forever. The audit trail outlives the asset."
        ),
        "key_points": [
            "Five paths: resale, redeployment, donation, recycling, destruction - chosen by value, hazard, and data content.",
            "Decommissioning comes first: safe shutdown, disconnection, fluid recovery, hazard clearance by licensed handlers.",
            "Data sanitization is non-negotiable: NIST SP 800-88 clear, purge, or destroy matched to data confidentiality, each certificated.",
            "The disposal certificate closes the register: method, date, proceeds or cost, sanitization evidence, manifests, signature.",
            "An asset is gone when the certificate is filed and the state reads Disposed - not when it leaves the building.",
        ],
        "requirements": [
            "A retirement approval gate opening every disposal case, with the disposal plan written before work begins.",
            "Decommissioning by qualified personnel with environmental manifests for regulated materials.",
            "Sanitization per NIST SP 800-88 matched to data classification, with certificates retained.",
            "Financial retirement: book value removed, gain or loss recognized against proceeds.",
            "The disposal certificate filed to the asset history; the tag number retired permanently.",
        ],
        "standards": [
            "Media sanitization follows NIST SP 800-88 Rev. 1: Guidelines for Media Sanitization.",
            "Environmental handling follows applicable EPA and jurisdictional hazardous-material regulations.",
            "Asset retirement accounting follows ASC 360; governmental reporting follows GASB 34.",
        ],
        "citations": [CIT_NIST888, CIT_ASC360, CIT_GASB34],
        "sig_lens": (
            "The Signature read: disposal is the honorable discharge - "
            "the trust released with the same care it was received with. "
            "The Signature method shuts down safely, wipes the memory "
            "clean as a final courtesy, accounts for the last dollar, and "
            "files the certificate: the asset's service complete, its "
            "record closed, its name retired with honor. Nothing entrusted "
            "is abandoned; everything is discharged."
        ),
    },
    {
        "key": "federation_discovery",
        "name": "CMDB Federation and Automated Discovery",
        "group": "Advanced",
        "ladder_rank": 9,
        "ladder_tier": "advanced",
        "description": (
            "No single database sees every asset. The network team has "
            "its monitor, security has its scanner, the cloud console "
            "has its inventory, finance has its ledger - and the CMDB "
            "must reconcile them all. Federation is the architecture for "
            "this: instead of one mega-database, authoritative sources "
            "keep their own data and the CMDB federates - linking to "
            "them, reconciling identities, and presenting one coherent "
            "web. Automated discovery is the federation's eyes: scanners "
            "that walk the network, the cloud accounts, and the "
            "endpoints, reporting what actually exists - IP addresses, "
            "MACs, serial numbers, installed software, open ports. The "
            "reconciliation is where truth is made: discovery finds a "
            "server the CMDB never heard of (unauthorized or "
            "forgotten - either way a task), the CMDB claims a laptop "
            "that discovery cannot find (lost, off-network, or retired "
            "without paperwork - a task), and attributes disagree "
            "(discovery says the firmware is 4.1, the CMDB says 3.9 - a "
            "task). Identity resolution is the hard engineering: "
            "matching the scanner's serial number to the register's tag "
            "number to finance's asset ID, with rules for conflicts and "
            "a manual queue for the ambiguous. This record teaches "
            "federation, discovery, and the reconciliation discipline."
        ),
        "how_it_works": (
            "Federation and discovery work as a scheduled truth cycle. "
            "Each source is registered with its authority: the network "
            "scanner is authoritative for IP and MAC, the endpoint agent "
            "for installed software, the register for tag and custody, "
            "finance for cost - when sources disagree, the authority "
            "wins, and the disagreement is still logged. Discovery runs "
            "on its cadence (continuous for networks, daily for cloud, "
            "weekly for endpoints) and lands in a staging area, never "
            "directly into the CMDB. Reconciliation matches staged "
            "findings to CIs by identity rules - serial number first, "
            "then MAC, then hostname with human review - and sorts the "
            "results: matched (attributes updated from the authoritative "
            "source), new (unauthorized-or-forgotten asset, task opened), "
            "missing (expected but unseen, task opened), conflict "
            "(manual queue). The tasks are worked like any other: "
            "investigated, dispositioned, and fed back - an unauthorized "
            "server becomes an authorized CI or gets removed from the "
            "network; a missing laptop becomes a loss report. The "
            "reconciliation report is the CMDB's truth score, published "
            "like the audit match rate, because a federated CMDB is "
            "believed exactly to the degree its reconciliations are "
            "clean."
        ),
        "key_points": [
            "Federation links authoritative sources instead of building one mega-database - each source owns its truth.",
            "Discovery is the eyes: network, cloud, and endpoint scanners reporting what actually exists.",
            "Reconciliation sorts findings into matched, new, missing, and conflict - each a task, not a shrug.",
            "Identity resolution matches scanner serials to register tags to finance IDs, with a manual queue for ambiguity.",
            "The reconciliation report is the CMDB's truth score - believed exactly to the degree it is clean.",
        ],
        "requirements": [
            "Registered sources with declared authority per attribute; authority wins conflicts, disagreements still logged.",
            "Discovery staging: findings land in staging, never directly into the CMDB.",
            "Identity-resolution rules (serial, MAC, hostname) with a manual review queue.",
            "Task workflow for new, missing, and conflict findings with disposition tracking.",
            "A published reconciliation report on cadence, treated as the CMDB's truth score.",
        ],
        "standards": [
            "Discovery and reconciliation practices align with ISO/IEC 19770-1:2017.",
            "Configuration management follows ITIL 4 (Axelos, 2019).",
            "Federated data integrity follows ISO 55001:2014 clause 7.5 (revised 2024).",
        ],
        "citations": [CIT_ISO19770, CIT_ITIL4, CIT_ISO55001],
        "sig_lens": (
            "The Signature read: federation is the council of witnesses - "
            "each keeper testifying to what it sees, the ledger weighing "
            "the testimonies into one truth. The Signature method gives "
            "each witness its proper authority, stages every new "
            "testimony for examination, and works every disagreement as "
            "a task - because truth about the entrusted things is too "
            "important to be voted on loosely."
        ),
    },
    {
        "key": "insurance",
        "name": "Asset Insurance and Loss Coverage",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Insurance is the financial backstop of the registry: when "
            "fire, theft, flood, or failure destroys value faster than "
            "maintenance can protect it, coverage pays to rebuild. The "
            "registry feeds insurance three things: the schedule of "
            "values (what is covered and for how much - replacement cost "
            "versus actual cash value, the two great valuation choices), "
            "the proof of existence and condition (the register plus "
            "audit match rates plus photos), and the loss history (what "
            "has happened, which prices the risk). Replacement cost pays "
            "what a new equivalent costs today; actual cash value pays "
            "replacement minus depreciation - cheaper premiums, painful "
            "settlements on old assets. Deductibles are the self-insured "
            "slice: a 25,000 dollar deductible on a 10 million dollar "
            "schedule means the organization eats the small losses, which "
            "is rational only if small losses are actually tracked and "
            "budgeted. The claim discipline mirrors warranty: prompt "
            "notice, documented damage (photos before cleanup), "
            "preservation of evidence, and the register's history as the "
            "proof of value and maintenance. Underinsurance is the silent "
            "killer - the schedule of values drifting years behind "
            "replacement costs, so the settlement rebuilds half the "
            "plant. This record teaches the schedule of values, the "
            "valuation choice, and the claim discipline."
        ),
        "how_it_works": (
            "Insurance works as a valued schedule kept current. Each year "
            "(and after major acquisitions), the schedule of values is "
            "rebuilt from the register: every covered asset with its "
            "replacement cost - not book value, which depreciation has "
            "shrunk below reality - summed by location and class. The "
            "broker markets the schedule; underwriters price it from the "
            "values, the loss history, and the risk controls the "
            "organization can evidence (sprinklers, security, maintenance "
            "program, audit match rates - every control documented is "
            "premium reduced). Coverage is chosen per class: buildings at "
            "replacement cost, equipment at replacement cost with "
            "agreed-value endorsements for the irreplaceable, vehicles on "
            "fleet policies, valuable papers and data with their own "
            "riders. Deductibles are set where the organization's loss "
            "history says small losses are affordable and the premium "
            "savings are real. When loss strikes, the claim file opens "
            "from the register: the asset's record proves existence and "
            "value, the maintenance history proves care (contesting any "
            "neglect exclusion), photos prove condition before and "
            "damage after. Settlement funds the replacement, the new "
            "asset enters the register, and the loss history updates - "
            "feeding next year's pricing."
        ),
        "key_points": [
            "The schedule of values - every covered asset at replacement cost, rebuilt yearly - is what the underwriter prices.",
            "Replacement cost versus actual cash value is the fundamental choice: full rebuild versus depreciated settlement.",
            "Documented risk controls (sprinklers, security, maintenance, audit match rates) reduce premiums - evidence pays.",
            "Deductibles are the self-insured slice: rational only if small losses are tracked and budgeted.",
            "The register is the claim's proof: existence, value, maintenance history, and photos - before and after.",
        ],
        "requirements": [
            "A schedule of values rebuilt annually from the register at replacement cost, by location and class.",
            "A documented valuation choice per class: replacement cost, actual cash value, or agreed value.",
            "Evidence files for risk controls: inspection reports, maintenance compliance, audit match rates, security measures.",
            "A claim procedure: prompt notice, photo documentation before cleanup, evidence preservation, register-sourced proof of value.",
            "Loss history maintained per asset and per class, feeding renewal negotiations.",
        ],
        "standards": [
            "Valuation practices align with standard property insurance appraisal methodology.",
            "Risk control documentation follows ISO 55001:2014 risk-based planning (revised 2024).",
            "Governmental risk pooling follows GASB Statement 34 risk-financing disclosure guidance.",
        ],
        "citations": [CIT_ISO55001, CIT_GASB34, CIT_IAM],
        "sig_lens": (
            "The Signature read: insurance is the covenant's backstop - "
            "the promise that if calamity outruns all keeping, the trust "
            "can be rebuilt. The Signature method keeps the schedule of "
            "values as honestly as the register itself, evidences every "
            "control, and claims promptly and fully when loss strikes - "
            "because the backstop only holds if it was honestly built."
        ),
    },
    {
        "key": "data_quality",
        "name": "Registry Data Quality and Governance",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "A registry is only as good as its data, and data quality is "
            "measured, not hoped for. Five dimensions carry the "
            "measurement: completeness (are the required fields filled - "
            "what fraction of assets lack a location), accuracy (are the "
            "filled fields true - verified by audit sample), uniqueness "
            "(is each asset one row - duplicate detection on serial "
            "numbers and tags), consistency (do related fields agree - "
            "the state says In Service but the location is the disposal "
            "vendor), and timeliness (how fresh is the data - moves "
            "recorded same-day versus three months late). Governance is "
            "who keeps it clean: a data owner per domain (the registrar "
            "owns identity, maintenance owns history), stewards who fix "
            "and prevent, written rules (required fields, formats, value "
            "lists), and a quality scorecard published monthly. The "
            "scorecard is the behavior-changer: when the Denver site sees "
            "its completeness at 61 percent next to Austin's 97, the "
            "competition does what memos cannot. Prevention beats "
            "correction by orders of magnitude: dropdowns instead of free "
            "text, required fields at entry, format validation on serials, "
            "and duplicate warnings at creation cost pennies; cleansing a "
            "decade of free-text locations costs a project. This record "
            "teaches the five dimensions, the governance roles, and the "
            "prevention-first program."
        ),
        "how_it_works": (
            "Data quality works as a measured loop: define, measure, fix, "
            "prevent. Define: each field gets its rule - required or "
            "optional, format, allowed values, and the dimension it "
            "serves; the rules live in the data dictionary, versioned "
            "like code. Measure: monthly jobs score each dimension - "
            "completeness as filled-required over total, accuracy from "
            "the audit sample's verified-true rate, uniqueness from "
            "duplicate scans on tag and serial, consistency from "
            "cross-field rule checks (state-location, custodian-active, "
            "warranty-date logic), timeliness from event-to-entry lag. "
            "The scorecard publishes per site and per domain, with trends "
            "- the trend is the management signal. Fix: data-cleansing "
            "sprints attack the worst dimensions with root-cause notes, "
            "because dirty data has a source - usually a process gap or "
            "a training gap, and fixing the source prevents recurrence. "
            "Prevent: every root cause becomes a control - a required "
            "field, a dropdown, a validation, a same-day rule - and the "
            "controls are tested like software. Governance runs the loop: "
            "the owner sets the targets, stewards work the fixes, and "
            "the monthly review holds both accountable. Quality compounds "
            "like interest; neglect compounds like debt."
        ),
        "key_points": [
            "Five dimensions: completeness, accuracy, uniqueness, consistency, timeliness - measured monthly, never hoped for.",
            "The scorecard per site and domain changes behavior: published comparison does what memos cannot.",
            "Prevention beats correction by orders of magnitude: dropdowns and validations cost pennies, cleansing costs projects.",
            "Every dirty-data root cause becomes a control - fix the source process, not just the rows.",
            "Governance is roles with teeth: owners set targets, stewards fix and prevent, monthly review holds both accountable.",
        ],
        "requirements": [
            "A versioned data dictionary: every field's rule, format, allowed values, and dimension served.",
            "Monthly quality jobs scoring all five dimensions, per site and per domain, with trends.",
            "Duplicate detection on tag and serial numbers at creation and in batch.",
            "Cross-field consistency rules checked automatically: state-location, custodian-active, date logic.",
            "Root-cause analysis for the worst dimensions, with each cause converted to a preventive control.",
        ],
        "standards": [
            "Data quality dimensions align with ISO 8000 (data quality) concepts.",
            "Asset information quality follows ISO 55001:2014 clause 7.5 (revised 2024).",
            "IT asset data quality follows ISO/IEC 19770-1:2017 information requirements.",
        ],
        "citations": [CIT_ISO55001, CIT_ISO19770, CIT_ISO55002],
        "sig_lens": (
            "The Signature read: data quality is the honesty of the "
            "ledger, measured in five dimensions and kept by named "
            "keepers. The Signature method measures what it claims, "
            "publishes the scores without flinching, fixes the source "
            "and not just the symptom, and prevents with the same "
            "seriousness it corrects - because a ledger half-true is a "
            "covenant half-kept."
        ),
    },
    {
        "key": "analytics_kpi",
        "name": "Registry Analytics and Key Performance Indicators",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Analytics turns the registry from a filing cabinet into an "
            "instrument panel: the KPIs that tell leadership whether the "
            "asset base is healthy, the maintenance program is working, "
            "and the money is well spent. The essential panel has twelve "
            "dials. Portfolio: total asset count, total replacement value, "
            "total book value, average age versus expected life. Health: "
            "fleet condition distribution, percentage of A-critical assets "
            "with current condition data, audit match rate. Maintenance: "
            "PM compliance, reactive-versus-planned work ratio, maintenance "
            "cost as a percentage of replacement value (the classic 2-4 "
            "percent benchmark for facilities), MTBF trend per class. "
            "Financial: capital spend versus plan, cost per operating hour "
            "trend, warranty recovery dollars. Each KPI needs its "
            "definition, its target, its trend, and its owner - a number "
            "without a target is trivia, without a trend is noise, "
            "without an owner is nobody's problem. The dashboard serves "
            "three altitudes: the executive view (six numbers, monthly), "
            "the manager view (the twelve dials, weekly), and the analyst "
            "view (drill to the asset, anytime). This record teaches the "
            "twelve dials, the definition-target-trend-owner discipline, "
            "and the three altitudes."
        ),
        "how_it_works": (
            "Analytics works as a pipeline from register to decision. "
            "Extraction pulls the facts on schedule - nightly for "
            "operational dials, monthly for financial ones - from the "
            "register, work orders, and finance. Transformation applies "
            "the KPI definitions exactly as written: PM compliance equals "
            "PMs completed on time over PMs due; reactive ratio equals "
            "emergency hours over total hours; maintenance cost percent "
            "equals annual maintenance spend over total replacement "
            "value. The definitions are versioned and published, because "
            "a KPI whose formula changed silently is a lie with a chart. "
            "Presentation layers the altitudes: executives get the six "
            "numbers with red-amber-green against target and a one-line "
            "narrative each; managers get the twelve dials with trends "
            "and the worst-ten asset lists behind each red dial; analysts "
            "get full drill-down to the asset and work order. Review "
            "closes the loop on cadence: monthly KPI review with owners "
            "present, each red dial carrying a named action with a date. "
            "The pipeline's integrity rule is lineage: any number on the "
            "dashboard traces back to the register rows and work orders "
            "that produced it, so a challenged number can be defended "
            "field by field."
        ),
        "key_points": [
            "Twelve dials: portfolio value and age, fleet health, PM compliance, reactive ratio, maintenance cost percent, MTBF trends, capital versus plan, warranty recovery.",
            "Every KPI carries definition, target, trend, and owner - without all four it is trivia, noise, or nobody's problem.",
            "Definitions are versioned and published; a silently changed formula is a lie with a chart.",
            "Three altitudes: executive (six numbers monthly), manager (twelve dials weekly), analyst (full drill-down anytime).",
            "Lineage is the integrity rule: any dashboard number traces back to the register rows that produced it.",
        ],
        "requirements": [
            "A KPI dictionary: exact formula, data sources, target, and named owner per indicator.",
            "Scheduled extraction and transformation with versioned definitions.",
            "Three presentation altitudes served from the same definitions.",
            "A monthly KPI review with owners present; every red dial gets a named action with a date.",
            "Full lineage from dashboard number to source rows, defensible field by field.",
        ],
        "standards": [
            "Performance evaluation and KPI practice follow ISO 55001:2014 clause 9.1 (revised 2024).",
            "Maintenance KPI definitions follow SMRP Best Practices.",
            "Asset management reporting aligns with the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_ISO55001, CIT_SMRP, CIT_IAM],
        "sig_lens": (
            "The Signature read: the dashboard is the steward's watchtower "
            "- twelve dials telling whether the keeping is true. The "
            "Signature method defines every dial in writing, aims each at "
            "a target, watches the trend and not just the moment, names "
            "an owner for every number, and traces each back to the "
            "ledger rows that bore it. What is measured honestly can be "
            "kept honestly."
        ),
    },
    {
        "key": "fleet",
        "name": "Fleet Management and Multi-Site Consolidation",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Fleet management runs assets that move or multiply: vehicles, "
            "mobile equipment, and standardized equipment classes spread "
            "across sites. The fleet lens adds what single-site "
            "management lacks: pooled visibility (all 400 vehicles in one "
            "view, not forty site spreadsheets), standardized specs (one "
            "approved sedan, one approved pickup - which collapses parts, "
            "training, and resale), lifecycle policies by class (sedans "
            "replaced at 120,000 miles or 7 years, whichever first), and "
            "telematics truth (real mileage, idle time, harsh events, "
            "location). Multi-site consolidation harvests the economies: "
            "centralized procurement (volume pricing on the standard "
            "spec), shared spares pools (one bearing stock serving five "
            "plants instead of five stocks), mobile maintenance crews "
            "routed across sites by the PM calendar, and reallocation - "
            "the underutilized asset at Site A moved to the capacity-"
            "starved Site B instead of Site B buying new. The governance "
            "is the delicate part: sites keep operational control while "
            "fleet standards set the guardrails, and the register is the "
            "shared truth both sides read. Chargeback or showback "
            "accounting - sites seeing the true cost of the assets they "
            "hold - is what makes consolidation stick. This record "
            "teaches the fleet lens, the consolidation harvests, and the "
            "governance that holds them."
        ),
        "how_it_works": (
            "Fleet management works as standards plus visibility plus "
            "reallocation. Standards: the fleet council approves one spec "
            "per class - the vehicle trims, the laptop models, the pump "
            "frame sizes - and all procurement buys to spec; exceptions "
            "need written justification. Visibility: telematics and "
            "meters feed the register continuously, so the fleet view "
            "shows every asset's location, utilization, condition, and "
            "cost in one pane, comparable across sites. Lifecycle policy "
            "per class sets the replacement trigger (miles, hours, or "
            "age) and the disposal path, so replacement is a conveyor, "
            "not a crisis. Reallocation is the quarterly harvest: the "
            "utilization review flags Site A's 22-percent-utilized loader "
            "and Site B's rental spend on the same class; the transfer "
            "moves the asset, updates custody and cost center, and both "
            "sites' numbers improve. Shared services consolidate the "
            "rest: one spares pool with inter-site transfer, one PM crew "
            "routing across nearby sites, one fuel or energy contract. "
            "Chargeback posts each asset's full cost - depreciation, "
            "maintenance, insurance, overhead - to its holding site "
            "monthly, so hoarding idle assets has a visible price and "
            "releasing them has a visible reward."
        ),
        "key_points": [
            "One approved spec per class collapses parts, training, procurement leverage, and resale value.",
            "Telematics plus the register gives one fleet view: location, utilization, condition, cost - comparable across sites.",
            "Lifecycle policy per class (miles, hours, or age trigger) makes replacement a conveyor, not a crisis.",
            "Reallocation is the quarterly harvest: move the idle asset to the starved site instead of buying new.",
            "Chargeback posts each asset's full monthly cost to its site - hoarding idle assets gets a visible price.",
        ],
        "requirements": [
            "A fleet council with approved standard specs per class and a written exception process.",
            "Telematics or metering feeding the register for mobile and high-value assets.",
            "Lifecycle replacement triggers and disposal paths per class, published and followed.",
            "A quarterly reallocation review matching idle assets to unmet needs across sites.",
            "Monthly chargeback of full asset cost to holding sites, with shared spares and crew pools where geography allows.",
        ],
        "standards": [
            "Fleet lifecycle practices align with ISO 55002:2018 life-cycle management guidance.",
            "Vehicle fleet data practices follow standard fleet management methodology.",
            "Multi-site asset information follows ISO 55001:2014 clause 7.5 (revised 2024).",
        ],
        "citations": [CIT_ISO55002, CIT_ISO55001, CIT_IAM],
        "sig_lens": (
            "The Signature read: the fleet is the household grown large - "
            "many roofs, one keeping. The Signature method holds the "
            "standards as the household rules, sees all the trusts in one "
            "view, moves the idle to where the need is, and charges each "
            "roof the true cost of what it holds. Many sites, one ledger, "
            "one standard of care."
        ),
    },
    {
        "key": "registry_program",
        "name": "Building an Asset Registry Program",
        "group": "Advanced",
        "ladder_rank": 10,
        "ladder_tier": "advanced",
        "description": (
            "Building the registry program is the capstone: turning "
            "thirty-three records of practice into a working system. It "
            "is built in phases, because big-bang registry projects fail "
            "on data cleansing and change fatigue. Phase one - foundation "
            "(months 1-3): charter and policy, the classification and "
            "naming standards, the register platform chosen, and the "
            "pilot scope (one site, one asset class, 500 assets). Phase "
            "two - pilot (months 4-6): tag and record the pilot assets, "
            "run the first audit, prove the match rate above 95 percent, "
            "and fix the process gaps the pilot exposes. Phase three - "
            "rollout (months 7-12): site by site, class by class, with "
            "trained registrars and the audit discipline traveling with "
            "the rollout. Phase four - operation (year two onward): the "
            "PM program, warranty tracking, calibration recall, and "
            "analytics come online against the now-trustworthy register, "
            "and the maturity assessment sets the improvement agenda. The "
            "program needs four roles: the sponsor (an executive who "
            "protects funding and attention), the registrar team (who "
            "owns the data), the custodians (who own the assets), and "
            "the auditors (who keep everyone honest). Success is measured "
            "in the only currency that matters: audit match rate, PM "
            "compliance, maintenance cost trend, and capital decisions "
            "made from register data. This record is the roadmap that "
            "assembles everything the database teaches."
        ),
        "how_it_works": (
            "The program works as a phased build with gates between "
            "phases. The charter opens it: scope, objectives, the "
            "sponsor's signature, and the success metrics (match rate, "
            "compliance, cost trend) written before a dollar is spent. "
            "Foundation builds the standards first - classification, "
            "naming, capitalization policy, state model - because data "
            "without standards is just expensive typing. The pilot is "
            "deliberately small and deliberately real: one site's pump "
            "fleet or one building's assets, tagged, recorded, and "
            "audited, with the gate criterion published in advance "
            "(match rate at or above 95 percent, or the process is fixed "
            "before rollout). Rollout moves in waves, each wave with a "
            "trained registrar, a cutover plan for legacy data, and an "
            "audit at its end; waves do not start until the previous "
            "wave's audit passes. Operation layers the advanced practices "
            "onto the trusted base: PM masters, warranty countdowns, "
            "calibration recall, health scoring, and the KPI dashboard - "
            "each switched on only when its input data is trustworthy. "
            "Governance runs throughout: monthly program review against "
            "the charter metrics, an annual maturity assessment, and a "
            "standing improvement backlog. The program succeeds when the "
            "register becomes the place decisions start - the day the "
            "capital plan is built from register data, the program has "
            "won."
        ),
        "key_points": [
            "Four phases: foundation (standards and charter), pilot (500 assets, prove 95 percent match), rollout (waves with audits), operation (advanced practices on trusted data).",
            "Gates between phases: the pilot gate and each wave's audit gate stop bad data from compounding.",
            "Standards before records: classification, naming, and policy are built before the first asset is entered.",
            "Four roles: sponsor (funding and attention), registrars (the data), custodians (the assets), auditors (the honesty).",
            "Victory condition: the capital plan is built from register data - the day decisions start at the register, the program has won.",
        ],
        "requirements": [
            "A signed charter with scope, objectives, sponsor, and success metrics before spending begins.",
            "Foundation standards complete before pilot data entry: classification, naming, capitalization, states.",
            "A real pilot (one site, one class, ~500 assets) with a published 95-percent match-rate gate.",
            "Wave-based rollout with trained registrars, legacy-data cutover plans, and end-of-wave audits.",
            "Monthly program review against charter metrics and an annual maturity assessment feeding the improvement backlog.",
        ],
        "standards": [
            "Program structure aligns with ISO 55001:2014 asset management system establishment (revised 2024).",
            "Implementation guidance follows ISO 55002:2018.",
            "Maturity assessment follows the Institute of Asset Management Anatomy v4.",
        ],
        "citations": [CIT_ISO55001, CIT_ISO55002, CIT_IAM],
        "sig_lens": (
            "The Signature read: the program is the founding of the "
            "keeping - the deliberate building of the household's memory "
            "and discipline. The Signature method founds in phases, "
            "proves each phase before the next, names the keepers and "
            "the watchers, and counts victory only when the ledger "
            "guides the hand that spends. A registry built this way is "
            "not a database; it is an institution of trust."
        ),
    },
])
