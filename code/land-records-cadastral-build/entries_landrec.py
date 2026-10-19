#!/usr/bin/env python3
"""Entries for the Land Records Cadastral databases (2026-10-17).

34 land-record topics, ladder-ordered 1-34
(foundations 1-12 / compounded 13-24 / advanced 25-34).
Public = real, fact-checked domain data. Signature = Signature land
interpretation, titles suffixed " (Signature Edition)".
No website references. No Facebook.
"""


def E(name, group, rank, tier, description, how, key_points, requirements,
      standards, citations, sig_lens, demo_data, demo_key="parcel"):
    return {"name": name, "group": group, "ladder_rank": rank,
            "ladder_tier": tier, "description": description,
            "how_it_works": how, "key_points": key_points,
            "requirements": requirements, "standards": standards,
            "citations": citations, "sig_lens": sig_lens,
            "demo_key": demo_key, "demo_data": demo_data}


ENTRIES = [

# ---------------- FOUNDATIONS 1-12 ----------------

E("Parcel Identification Numbers (APN)", "Foundations", 1, "foundations",
  "A Parcel Identification Number, often called an assessor's parcel "
  "number (APN) or tax parcel number, is the unique identifier a county "
  "assigns to each piece of taxable land. It is the key that ties "
  "together the assessor's valuation, the tax collector's bill, the "
  "recorder's documents, and the GIS map. Formats vary by county — some "
  "encode map book, page, and parcel — but every system guarantees one "
  "number per parcel. When a parcel splits or merges, the old numbers "
  "retire and new ones issue, with the history preserved in the "
  "assessor's rolls. Title companies, lenders, and buyers all use the "
  "APN to pull the right records, and most counties publish APN search "
  "tools online.",
  "The assessor's office assigns the APN when a parcel is created by "
  "subdivision, deed, or survey, and maintains it through splits, "
  "combinations, and boundary adjustments. The number appears on tax "
  "bills, assessment notices, and recorded documents. GIS departments "
  "link the APN to polygon geometry so maps and records stay in sync. "
  "When ownership transfers, the APN stays with the land while the owner "
  "name changes, giving every parcel a stable identity across decades "
  "of transactions.",
  ["Unique county-level identifier for each taxable parcel.",
   "Links assessor, tax collector, recorder, and GIS records.",
   "Retired and reissued on splits and merges, with history preserved.",
   "Used by title companies, lenders, and buyers to pull records."],
  ["The assessor must assign one number per parcel under state law.",
   "Splits and merges require recorded maps or deeds before renumbering.",
   "Historical APNs must remain searchable for chain-of-title work."],
  ["IAAO Standard on Parcel Identification (International Association of Assessing Officers).",
   "State assessment manuals governing parcel numbering.",
   "FGDC Cadastral Data Content Standard (parcel identifier elements)."],
  ["International Association of Assessing Officers - Standard on Parcel Identification.",
   "County assessor parcel-numbering manuals (state-published)."],
  "In the Signature land system every parcel number is a sworn name: the "
  "land receives its number like a citizen receives a name, and the "
  "number never lies about which ground it belongs to.",
  {"acres": 0.25, "corners": 4, "example_apn": "123-45-678"}),

E("Metes and Bounds Legal Descriptions", "Foundations", 2, "foundations",
  "Metes and bounds is the oldest method of describing land in America, "
  "used in the original thirteen colonies and the states formed from "
  "them. A metes-and-bounds description traces the parcel's boundary in "
  "a narrative: starting at a point of beginning, then running stated "
  "distances and directions (the metes) along lines and natural features "
  "(the bounds) until returning to the start. It reads like a walk "
  "around the property: north 200 feet to the oak tree, then east along "
  "the creek. Because it depends on physical monuments that can vanish, "
  "old metes-and-bounds descriptions are the richest source of boundary "
  "disputes — and of surveyor detective work.",
  "A surveyor writes the description from field measurements, calling "
  "out each course by bearing and distance and each corner by its "
  "monument. The description must close mathematically back to the point "
  "of beginning. Hierarchy of calls resolves conflicts: natural "
  "monuments outrank artificial monuments, which outrank courses and "
  "distances, which outrank area. When a monument is lost, surveyors "
  "retrace the original surveyor's footsteps using the record, "
  "neighboring parcels, and evidence on the ground.",
  ["Oldest US land-description method, used in the original colonies.",
   "Traces boundaries by bearings, distances, and monuments.",
   "Must close mathematically to the point of beginning.",
   "Hierarchy of calls: natural monuments first, area last."],
  ["Descriptions must be written by or under a licensed surveyor in most states.",
   "The description must close within legal tolerance.",
   "Lost monuments require retracement evidence, not guesswork."],
  ["State surveying statutes and board rules.",
   "ALTA/NSPS Minimum Standard Detail Requirements (boundary surveys)."],
  ["Brown, C. et al. - Evidence and Procedures for Boundary Location (text).",
   "State board of licensure rules for legal descriptions."],
  "In the Signature land system a metes-and-bounds walk is a sworn "
  "circuit: every bearing a promise, every monument a witness, and the "
  "closing course the seal that the ground described is the ground "
  "meant.",
  {"acres": 5.0, "corners": 6, "closure_ft": 0.08}),

E("The Public Land Survey System (PLSS)", "Foundations", 3, "foundations",
  "The Public Land Survey System is the rectangular grid that divides "
  "most American land west of the Appalachians. Created by the Land "
  "Ordinance of 1785 and refined by later acts, it lays townships six "
  "miles square, divided into 36 one-mile sections of 640 acres each. "
  "Sections split into halves and quarters — the familiar quarter-"
  "section of 160 acres that homesteaders claimed. Meridians and base "
  "lines anchor the grid; each parcel's legal description reads like an "
  "address in the grid, for example the northeast quarter of Section "
  "12, Township 3 North, Range 4 West. About 1.5 billion acres were "
  "surveyed under the system, the largest land survey in history.",
  "Government surveyors ran the original lines with chains and compasses, "
  "setting monuments at section corners and recording field notes. Those "
  "original corners control today: modern surveyors retrace them rather "
  "than re-measuring the ideal grid. The Bureau of Land Management "
  "maintains the official records, including the General Land Office "
  "plats. Private surveyors subdivide sections for development, always "
  "tying back to the original government corners, which are the legal "
  "truth of the boundary.",
  ["Rectangular survey grid created by the Land Ordinance of 1785.",
   "Townships of 36 sections; sections of 640 acres.",
   "Original government corners legally control boundaries.",
   "Covers about 1.5 billion acres — history's largest land survey."],
  ["Original GLO corners must be retraced, not relocated by measurement.",
   "Subdivisions require licensed surveyors and recorded plats.",
   "BLM Manual of Surveying Instructions governs federal surveys."],
  ["BLM Manual of Surveying Instructions (2009).",
   "Land Ordinance of 1785 and subsequent public land acts."],
  ["Bureau of Land Management - Manual of Surveying Instructions.",
   "Land Ordinance of 1785 (Journals of the Continental Congress)."],
  "In the Signature land system the PLSS grid is the sworn lattice of "
  "the West: every section corner a fixed star of ownership, every "
  "township a covenant of order laid over wilderness.",
  {"acres": 160.0, "corners": 4, "township": "T3N R4W Sec 12"}),

E("Warranty Deeds", "Foundations", 4, "foundations",
  "A warranty deed is the strongest form of property conveyance: the "
  "seller (grantor) not only transfers ownership but guarantees the "
  "title. The deed contains covenants — seisin (the grantor owns it), "
  "right to convey, against encumbrances, quiet enjoyment, and warranty "
  "forever — promising to defend the buyer's title against lawful "
  "claims, even claims arising before the grantor owned the land. "
  "General warranty deeds cover the property's entire history; special "
  "warranty deeds cover only the grantor's period of ownership. Because "
  "of these promises, warranty deeds are the standard instrument in "
  "arm's-length residential sales, usually paired with title insurance.",
  "The grantor signs the deed before a notary, the deed is delivered to "
  "the grantee, and it is recorded with the county recorder to give "
  "public notice. If a title defect later surfaces — an old lien, a "
  "forged link in the chain — the grantee can sue the grantor on the "
  "covenants. Title companies search the chain before closing and "
  "typically require the seller to convey by warranty deed. Recording "
  "establishes priority: in most states, the first bona fide purchaser "
  "to record wins against later claimants.",
  ["Strongest deed form: transfers ownership plus title guarantees.",
   "Contains covenants of seisin, right to convey, encumbrances, quiet enjoyment, warranty.",
   "General warranty covers all history; special warranty covers grantor's period only.",
   "Standard in arm's-length sales; recorded for public notice."],
  ["Must be signed, acknowledged before a notary, and delivered.",
   "Requires a legally sufficient description of the property.",
   "Recording is needed for priority against later purchasers."],
  ["State recording acts (race, notice, or race-notice statutes).",
   "State form requirements for deeds (grantor, grantee, habendum, acknowledgment)."],
  ["State real property statutes (deed forms and covenants).",
   "American Land Title Association - deed and title guidance."],
  "In the Signature land system a warranty deed is a sworn oath of "
  "ownership: the grantor stakes their name on the title's purity, and "
  "the covenants are the seal that binds the promise to the land "
  "itself.",
  {"acres": 0.5, "corners": 4, "covenants": 5}),

E("Quitclaim Deeds", "Foundations", 5, "foundations",
  "A quitclaim deed transfers whatever interest the grantor has — which "
  "may be everything, something, or nothing — with no warranties at all. "
  "The grantor quits any claim without promising the title is good. "
  "Quitclaims are the right tool for low-risk transfers: between family "
  "members, into a trust, to clear up a name after divorce or death, or "
  "to release a possible cloud on title. They are the wrong tool for "
  "buying from a stranger, because the buyer gets no promises and little "
  "recourse if the title fails. Title insurers treat quitclaim chains "
  "with extra scrutiny.",
  "The grantor signs and acknowledges the deed, which is recorded like "
  "any conveyance. Because there are no covenants, the grantee cannot sue "
  "the grantor if the title proves defective — the deed conveyed only "
  "what the grantor had. Lawyers use quitclaims to tidy ownership: "
  "moving property into an LLC, correcting a misspelled name, or having "
  "an heir release an interest. Recording still matters for notice and "
  "priority, and transfer taxes may still apply.",
  ["Transfers whatever interest exists, with zero warranties.",
   "Right tool for family transfers, trusts, and clearing clouds.",
   "Wrong tool for arm's-length purchases from strangers.",
   "Grantee has no covenant claim against the grantor."],
  ["Must still be signed, acknowledged, and recorded.",
   "Parties should confirm no mortgage or tax lien survives the transfer.",
   "Legal advice is prudent before accepting one in a purchase."],
  ["State deed statutes (quitclaim form requirements).",
   "State transfer-tax rules."],
  ["State real property statutes.",
   "American Bar Association - real property guidance on deed types."],
  "In the Signature land system a quitclaim is an honest handoff: the "
  "grantor swears only to step aside, claiming nothing beyond what is "
  "truly theirs, and the record notes the humility of the transfer.",
  {"acres": 1.0, "corners": 4, "covenants": 0}),

E("Title Search and Chain of Title", "Foundations", 6, "foundations",
  "A title search is the detective work of property law: tracing every "
  "recorded document affecting a parcel — deeds, mortgages, liens, "
  "easements, judgments, probate records — to build the chain of title, "
  "the unbroken sequence of ownership from a root of title to the "
  "present. Searchers work backward from the current owner through the "
  "grantor-grantee indexes, then forward again to catch documents the "
  "backward pass missed. The chain reveals breaks, forgeries, "
  "unsatisfied liens, and competing claims. In most American "
  "transactions a professional search precedes every closing and every "
  "title insurance policy.",
  "The searcher starts with the legal description or parcel number, "
  "pulls the current vesting deed, then follows each prior grantor back "
  "through the index — often 40 to 60 years, sometimes to the original "
  "patent. Tax, judgment, and lien records are checked in parallel. "
  "Findings go into a title commitment listing requirements to clear "
  "and exceptions the policy will not cover. Breaks in the chain, wild "
  "deeds recorded outside it, and unreleased mortgages must be cured "
  "before closing or insured over.",
  ["Traces every recorded document affecting a parcel.",
   "Builds the unbroken chain of ownership from root to present.",
   "Reveals liens, breaks, forgeries, and competing claims.",
   "Precedes every closing and title policy."],
  ["Searches must cover grantor-grantee indexes in both directions.",
   "Tax and judgment records must be checked alongside deeds.",
   "Defects found must be cured or excepted before closing."],
  ["ALTA title search and commitment standards.",
   "State marketable title acts (root-of-title periods)."],
  ["American Land Title Association - title search best practices.",
   "State marketable title acts."],
  "In the Signature land system the chain of title is a sworn lineage: "
  "every deed a generation, every lien a scar in the record, and the "
  "search the ritual that proves the bloodline of ownership is pure.",
  {"acres": 2.0, "corners": 4, "chain_links": 14}),

E("Survey Monuments and Markers", "Foundations", 7, "foundations",
  "Survey monuments are the physical objects that mark property corners: "
  "iron rods and pipes, brass caps in concrete, stone bounds, and "
  "official government disks. In law, the monument on the ground "
  "generally controls over the measurements in the deed — the physical "
  "mark beats the paper distance. Surveyors set monuments at corners "
  "they establish and search for original monuments when retracing old "
  "boundaries. A found original monument, undisturbed, is the best "
  "evidence of where the line legally lies. Disturbing or destroying a "
  "survey monument is a crime in most states.",
  "Licensed surveyors set monuments to durable standards — typically "
  "iron rods with identifying caps — and record their locations on the "
  "survey map. When retracing, the surveyor digs for the original "
  "monument using the record description, old maps, and witness "
  "evidence like fence lines and occupation. If the original is gone, "
  "its position is re-established from the best available evidence "
  "under the hierarchy of calls. New monuments are then set and the "
  "survey recorded.",
  ["Physical markers of property corners: rods, caps, stones, disks.",
   "The monument on the ground controls over deed measurements.",
   "Found original monuments are the best boundary evidence.",
   "Destroying a monument is a crime in most states."],
  ["Only licensed surveyors may set or re-establish corners in most states.",
   "Monuments must meet state durability and identification standards.",
   "Surveys must be recorded or filed as state law requires."],
  ["State surveying practice acts.",
   "ALTA/NSPS Minimum Standard Detail Requirements."],
  ["National Society of Professional Surveyors - standards.",
   "State boards of licensure - monument requirements."],
  "In the Signature land system a monument is a sworn witness of stone "
  "and iron: it stands where the surveyor stood, speaks when papers "
  "disagree, and holds the line against time itself.",
  {"acres": 10.0, "corners": 4, "monuments_found": 3}),

E("Plat Maps and Subdivisions", "Foundations", 8, "foundations",
  "A plat map is the surveyed drawing that creates lots: it shows "
  "streets, lot lines, easements, and dedications, and when recorded it "
  "legally subdivides land. Subdivision is how raw acreage becomes a "
  "neighborhood — the developer's surveyor draws the plat, the planning "
  "authority approves it, and recording creates the individual lots with "
  "their own legal descriptions (Lot 7, Block 3 of Sunny Acres "
  "Subdivision). Plats dedicate streets and parks to the public, reserve "
  "utility easements, and note restrictions. Every lot sold afterward "
  "traces its title to that recorded plat.",
  "The subdivider hires a licensed surveyor to monument the boundary "
  "and interior lot corners and draft the plat to the jurisdiction's "
  "exacting standards. Planning staff review for zoning, access, "
  "drainage, and utilities; the planning commission or council approves. "
  "The owner signs dedications, the surveyor certifies, and the plat is "
  "recorded. From then on, conveyances reference lot and block instead "
  "of metes and bounds, and the plat controls lot dimensions.",
  ["The surveyed drawing that legally creates subdivision lots.",
   "Dedicates streets and parks; reserves utility easements.",
   "Recorded plat controls lot lines and dimensions.",
   "Later deeds reference lot and block, not metes and bounds."],
  ["Requires licensed surveyor certification and owner dedication.",
   "Needs planning approval under the subdivision ordinance.",
   "Must meet monumentation and drafting standards before recording."],
  ["State subdivision map acts.",
   "Local subdivision ordinances and improvement standards."],
  ["American Planning Association - subdivision regulation guidance.",
   "State map acts (e.g., Subdivision Map Act)."],
  "In the Signature land system a recorded plat is a sworn founding "
  "charter of a neighborhood: streets dedicated to the public, lots "
  "numbered like citizens, and every future deed a descendant of the "
  "plat.",
  {"acres": 40.0, "corners": 48, "lots": 120}),

E("Easements", "Foundations", 9, "foundations",
  "An easement is a legal right to use someone else's land for a "
  "specific purpose without owning it. The land burdened is the "
  "servient estate; the benefited party holds the dominant estate (or "
  "an easement in gross, like a utility's). Common easements: driveways "
  "crossing a neighbor's lot, utility lines, drainage, conservation, "
  "and access to landlocked parcels. Easements can be created by deed, "
  "by long use (prescription), by necessity, or by plat dedication. "
  "They run with the land — selling the property does not erase them — "
  "and they are the most common surprise in a title search.",
  "Easements are created in writing and recorded to bind future owners. "
  "Express easements are granted by deed with a defined location and "
  "purpose. Implied easements arise from prior use or necessity when "
  "land is divided. Prescriptive easements ripen from open, hostile, "
  "continuous use over the statutory period. The easement holder may "
  "use and maintain the easement area but cannot expand it; the owner "
  "keeps all other rights. Termination comes by release, merger of the "
  "estates, abandonment, or expiration.",
  ["A right to use another's land for a specific purpose.",
   "Runs with the land — survives sales.",
   "Created by deed, prescription, necessity, or plat.",
   "Most common surprise in title searches."],
  ["Express easements should be written, described, and recorded.",
   "Prescriptive claims require meeting the full statutory period.",
   "Use is limited to the easement's stated purpose and location."],
  ["State easement statutes.",
   "Restatement (Third) of Property: Servitudes."],
  ["State property law treatises on easements.",
   "Restatement (Third) of Property: Servitudes (2000)."],
  "In the Signature land system an easement is a sworn passage: the "
  "land yields a path without surrendering itself, and the recorded "
  "grant is the covenant that the way remains open.",
  {"acres": 0.1, "corners": 4, "easement_width_ft": 20}),

E("Liens on Real Property", "Foundations", 10, "foundations",
  "A lien is a legal claim against property securing a debt: the "
  "creditor can force sale of the land to get paid. Mortgages are "
  "voluntary liens the owner grants a lender. Tax liens arise by law "
  "when property taxes go unpaid and take priority over almost "
  "everything. Mechanic's liens secure contractors and suppliers who "
  "improved the property. Judgment liens attach when a court money "
  "judgment is recorded. HOA liens secure unpaid assessments. Liens "
  "must generally be recorded to bind buyers, and priority usually "
  "follows recording order — first to record, first to be paid — with "
  "property tax liens the great exception.",
  "Liens attach by agreement, statute, or judgment, and are perfected "
  "by recording in the county land records. The lienholder forecloses "
  "through court or statutory process, selling the property to satisfy "
  "the debt. Owners clear title by paying the debt and recording a "
  "release or satisfaction. Title searches hunt liens because they "
  "survive conveyances: buying land does not erase the prior owner's "
  "unpaid tax lien. Priority battles between lenders, contractors, and "
  "tax collectors are resolved by recording statutes and lien law.",
  ["A claim securing a debt against the land.",
   "Types: mortgage, tax, mechanic's, judgment, HOA liens.",
   "Priority usually follows recording order; tax liens come first.",
   "Survive conveyances — buyers inherit sellers' liens."],
  ["Most liens must be recorded to bind later buyers.",
   "Mechanic's liens have strict notice and filing deadlines.",
   "Foreclosure requires statutory or judicial process."],
  ["State lien and recording statutes.",
   "State mechanic's lien acts."],
  ["State lien statutes.",
   "American Land Title Association - lien priority guidance."],
  "In the Signature land system a lien is a sworn hold: the debt "
  "grips the land until paid, the recording is the public notice of "
  "the grip, and the release is the covenant that the hold is lifted.",
  {"acres": 1.5, "corners": 4, "lien_amount": 185000}),

E("Zoning and Land Use Controls", "Foundations", 11, "foundations",
  "Zoning is the local government's power to divide land into districts "
  "and dictate what can be built and done in each: residential here, "
  "commercial there, industrial elsewhere, with rules on height, "
  "setbacks, density, and use. Born in New York City in 1916 and "
  "upheld by the Supreme Court in Euclid v. Ambler (1926), zoning is "
  "now nearly universal in American cities. It flows from a "
  "comprehensive plan through a zoning ordinance and map; owners "
  "seeking exceptions apply for variances, conditional uses, or "
  "rezonings. Zoning shapes the value, character, and future of every "
  "parcel it touches.",
  "The planning commission recommends and the council adopts the "
  "zoning map and text. Staff issue permits for conforming uses. "
  "Owners wanting something different apply: variances for hardship "
  "from dimensional rules, conditional-use permits for listed special "
  "uses, rezonings to change the district itself — each with public "
  "hearings and findings. Nonconforming uses predating the rules may "
  "continue but not expand. Courts review zoning for constitutional "
  "validity; takings claims arise when regulation goes too far.",
  ["Local power to dictate uses, height, setbacks, and density by district.",
   "Upheld in Euclid v. Ambler (1926); flows from a comprehensive plan.",
   "Exceptions via variances, conditional uses, and rezonings.",
   "Shapes the value and future of every parcel."],
  ["Zoning must follow an adopted comprehensive plan in most states.",
   "Changes require public hearings and findings.",
   "Regulations must not effect an unconstitutional taking."],
  ["State zoning enabling acts.",
   "Local zoning ordinances and comprehensive plans."],
  ["Euclid v. Ambler Realty Co., 272 U.S. 365 (1926).",
   "American Planning Association - zoning practice guidance."],
  "In the Signature land system zoning is the sworn pattern of the "
  "city: each district a covenant of compatible neighbors, each "
  "variance a careful exception sealed by public hearing.",
  {"acres": 3.0, "corners": 4, "districts": 12}),

E("The County Recorder's Office", "Foundations", 12, "foundations",
  "The county recorder — called the register of deeds, county clerk, "
  "or clerk-recorder in some states — is the office that keeps the "
  "public land records. Every deed, mortgage, lien, easement, and plat "
  "that affects real property is recorded here, indexed by grantor and "
  "grantee names, and preserved as the permanent public memory of who "
  "owns what. The office collects recording fees and transfer taxes, "
  "maintains records stretching back a century or more, and increasingly "
  "offers them online. The integrity of the whole property system rests "
  "on this office: recording gives constructive notice to the world.",
  "Documents are presented with fees, checked for legal sufficiency "
  "(signatures, acknowledgment, description), stamped with date and "
  "time, indexed, imaged, and returned. The date-time stamp sets "
  "priority under the recording act. Modern offices scan historical "
  "books, run online search portals, and accept electronic recording "
  "from title companies. Fraud prevention — verifying identities and "
  "flagging suspicious filings — has become a core duty as deed fraud "
  "has grown. Certified copies from the recorder are the authoritative "
  "evidence of the record.",
  ["Keeps the public land records: deeds, mortgages, liens, plats.",
   "Recording gives constructive notice to the world.",
   "Date-time stamp sets priority under recording acts.",
   "Collects fees and transfer taxes; increasingly online."],
  ["Documents must meet legal sufficiency (signatures, acknowledgment).",
   "Indexing must allow reliable grantor-grantee searching.",
   "Records must be preserved permanently and kept accessible."],
  ["State recording acts.",
   "Uniform Real Property Electronic Recording Act (in adopting states)."],
  ["Property Records Industry Association - recording standards.",
   "State recorder/clerk manuals."],
  "In the Signature land system the recorder's office is the sworn "
  "memory of the land: every stamp a covenant of public notice, every "
  "index a thread in the tapestry of ownership, every preserved book a "
  "promise that the past cannot be quietly rewritten.",
  {"acres": 0.0, "corners": 0, "documents_per_year": 85000}),

# ---------------- COMPOUNDED 13-24 ----------------

E("Torrens Title Registration", "Compounded", 13, "compounded",
  "Torrens is a system of title registration in which the government "
  "itself certifies who owns land, issuing a certificate of title that "
  "is conclusive. Invented by Sir Robert Torrens in South Australia in "
  "1858 and adopted in parts of the United States — notably Minnesota, "
  "Massachusetts, and Hawaii — it replaces the American recording "
  "system's chain-of-title detective work with a single authoritative "
  "register: the certificate mirrors the title, and the mirror cannot "
  "be contradicted. Registration is voluntary where it exists in the "
  "US, and a court proceeding establishes the initial certificate. An "
  "assurance fund compensates anyone harmed by register errors.",
  "The owner petitions a court to register the land; examiners and a "
  "judicial proceeding settle all claims, and the registrar issues the "
  "certificate. Later transfers, mortgages, and liens are noted on the "
  "certificate itself — the register is the title. Buyers need only read "
  "the certificate, not search history. Adverse possession generally "
  "cannot run against registered land. Withdrawal back to the recording "
  "system is possible in some states. The system's cost and formality "
  "explain its limited American adoption.",
  ["Government-certified title: the certificate is conclusive.",
   "Invented 1858 in South Australia; used in parts of the US.",
   "Replaces chain-of-title searching with a single register.",
   "Assurance fund compensates victims of register errors."],
  ["Initial registration requires a court proceeding settling all claims.",
   "Later dealings must be memorialized on the certificate.",
   "Adverse possession generally barred against registered land."],
  ["State Torrens acts (e.g., Minnesota, Massachusetts, Hawaii statutes).",
   "Court rules for initial registration proceedings."],
  ["State Torrens registration statutes.",
   "Torrens, R. - The South Australian System of Conveyancing by Registration of Title (1859)."],
  "In the Signature land system Torrens is the sworn mirror: the "
  "government holds the reflection of ownership, and the certificate is "
  "the covenant that the reflection and the reality are one.",
  {"acres": 4.0, "corners": 4, "assurance_fund_pct": 0.1}),

E("GIS Cadastral Mapping", "Compounded", 14, "compounded",
  "GIS cadastral mapping is the digital twin of the parcel fabric: "
  "every parcel drawn as a polygon in a geographic information system, "
  "linked to its parcel number, owner, assessment, zoning, and recorded "
  "documents. County GIS departments build these layers from recorded "
  "plats, deeds, and surveys, and publish them as web maps the public "
  "uses daily. Cadastral GIS powers assessment, planning, emergency "
  "response, and utilities — but it is a representation, not the legal "
  "record: the deed and the surveyor's monuments control, not the "
  "pixels. Accuracy varies from survey-grade to tax-map sketch, and "
  "responsible systems label their accuracy.",
  "GIS staff digitize recorded plats and deeds, snapping lines to "
  "control points and aerial imagery, and maintain the fabric through "
  "daily edits as parcels split and merge. The parcel layer joins to "
  "assessor tables by parcel number. Topology rules keep polygons from "
  "overlapping or gapping. Metadata records source, date, and accuracy. "
  "Web services publish the layers to staff, other agencies, and the "
  "public, with disclaimers that the map is not a survey.",
  ["Digital twin of the parcel fabric, linked to records.",
   "Powers assessment, planning, emergency response, utilities.",
   "A representation, not the legal record — deeds control.",
   "Accuracy must be labeled, from survey-grade to sketch."],
  ["Parcel geometry must derive from recorded sources.",
   "Topology must be maintained: no gaps or overlaps.",
   "Public maps must disclaim that they are not surveys."],
  ["FGDC Cadastral Data Content Standard.",
   "NSGIC GIS inventory and metadata practices."],
  ["Federal Geographic Data Committee - Cadastral Data Content Standard.",
   "National States Geographic Information Council - guidance."],
  "In the Signature land system the cadastral GIS is the sworn mirror "
  "of the ground: every polygon a reflection of a deed, every join a "
  "covenant between map and record, every accuracy label an honest "
  "measure of the mirror's clarity.",
  {"acres": 0.0, "corners": 0, "parcels_mapped": 120000}),

E("LiDAR in Land Surveying", "Compounded", 15, "compounded",
  "LiDAR — Light Detection and Ranging — maps land by firing laser "
  "pulses and timing their return, producing dense point clouds that "
  "reveal the ground in centimeter detail, even through forest canopy. "
  "Airborne LiDAR now underpins statewide elevation programs like the "
  "USGS 3D Elevation Program; terrestrial scanners capture buildings, "
  "bridges, and construction sites; mobile systems map road corridors. "
  "For cadastral work, LiDAR generates the terrain models, planimetric "
  "features, and control networks that plats and GIS layers are built "
  "on — though boundary lines themselves still require a licensed "
  "surveyor's legal judgment.",
  "A sensor emits hundreds of thousands of pulses per second; GPS and "
  "an inertial unit record the sensor's position and attitude so each "
  "return is georeferenced. Processing classifies points — ground, "
  "vegetation, buildings — and builds digital elevation models. "
  "Surveyors extract breaklines, contours, and features, check accuracy "
  "against ground control, and deliver surfaces to engineers and GIS. "
  "Quality levels (QL0–QL2 in 3DEP) specify point density and vertical "
  "accuracy for public datasets.",
  ["Laser mapping producing centimeter-detail point clouds.",
   "Sees through canopy to the bare ground.",
   "Underpins USGS 3DEP statewide elevation data.",
   "Boundaries still require a licensed surveyor's judgment."],
  ["Data must be tied to ground control and checked for accuracy.",
   "Deliverables must state quality level and accuracy.",
   "Boundary determinations remain the surveyor's legal work."],
  ["USGS Lidar Base Specification.",
   "ASPRS Positional Accuracy Standards for Digital Geospatial Data."],
  ["U.S. Geological Survey - 3D Elevation Program specifications.",
   "American Society for Photogrammetry and Remote Sensing - accuracy standards."],
  "In the Signature land system LiDAR is the sworn eye of light: a "
  "million laser witnesses testifying to the shape of the ground, every "
  "point a covenant of measured truth.",
  {"acres": 640.0, "corners": 0, "points_per_sqm": 8}),

E("GPS and GNSS Land Surveying", "Compounded", 16, "compounded",
  "Global Navigation Satellite System surveying — GPS and its sister "
  "constellations — lets a surveyor fix a point's coordinates to "
  "centimeter precision by measuring signals from orbiting satellites. "
  "Real-time kinematic (RTK) rovers get corrections from a base station "
  "or network, delivering instant coordinates in the field; static "
  "sessions processed later reach millimeter precision for control "
  "networks. GNSS underpins modern subdivision staking, topographic "
  "surveys, machine control, and the national reference frame. It "
  "demands open sky, careful technique, and connection to the datum — "
  "a coordinate is only as good as its reference frame.",
  "The surveyor sets up on or connects to known control, initializes "
  "the rover, and collects positions with sufficient satellites, good "
  "geometry, and fixed ambiguities. RTK networks (like state CORS "
  "networks) broadcast corrections over cellular. Static baselines are "
  "post-processed against CORS stations. Results are transformed into "
  "the project datum and checked by independent observations. Metadata "
  "records the constellation, method, and estimated precision.",
  ["Centimeter precision from satellite signals.",
   "RTK gives instant field coordinates; static gives millimeter control.",
   "Underpins staking, topo surveys, and machine control.",
   "Coordinates are only as good as their datum and technique."],
  ["Work must tie to the published reference frame via control.",
   "Independent checks are required for boundary-grade work.",
   "Metadata must record method and precision."],
  ["NOAA CORS network standards.",
   "State board rules for GNSS surveying practice."],
  ["National Geodetic Survey - CORS and reference frame documentation.",
   "State surveying practice acts (GNSS provisions)."],
  "In the Signature land system GNSS is the sworn constellation: "
  "satellites as witnesses in the sky, every fixed solution a covenant "
  "that the point measured is the point marked.",
  {"acres": 20.0, "corners": 8, "precision_cm": 2}),

E("Total Station Surveying", "Compounded", 17, "compounded",
  "The total station is the surveyor's workhorse: an electronic "
  "instrument combining angle measurement, laser distance measurement, "
  "and onboard computation in one box. Set over a known point and aimed "
  "at a prism, it measures angles and distances to fix new points by "
  "traverse, radiation, or resection — the classical geometry of "
  "surveying executed with electronic precision. Robotic total stations "
  "track the prism automatically, letting one surveyor do the work of "
  "two. Every subdivision stake, building corner, and boundary monument "
  "set in the last forty years was likely placed with one.",
  "The surveyor establishes control, sets up the instrument, backsights "
  "a known point to orient, then measures to prisms held at each "
  "target. The instrument computes coordinates in real time; the data "
  "collector records them with codes. Traverses close back to control, "
  "and misclosure is distributed by rule. Calibration, temperature and "
  "pressure corrections, and redundant observations keep the work "
  "honest. The survey map reports the basis of bearings, control used, "
  "and achieved precision.",
  ["Electronic angle + distance + computation in one instrument.",
   "Fixes points by traverse, radiation, and resection.",
   "Robotic models let one surveyor work alone.",
   "Set most modern subdivision and boundary monuments."],
  ["Traverses must close within legal tolerance.",
   "Instruments require calibration and atmospheric correction.",
   "Surveys must report control, basis of bearings, and precision."],
  ["ALTA/NSPS Minimum Standard Detail Requirements.",
   "State board precision standards."],
  ["National Society of Professional Surveyors - standards.",
   "ALTA/NSPS Minimum Standard Detail Requirements (current edition)."],
  "In the Signature land system the total station is the sworn "
  "protractor: every angle a promise of exactness, every closed "
  "traverse a covenant that the geometry of the ground is true.",
  {"acres": 15.0, "corners": 12, "misclosure_ft": 0.05}),

E("Boundary Dispute Resolution", "Compounded", 18, "compounded",
  "Boundary disputes — neighbors fighting over fences, driveways, and "
  "the invisible line between lots — are resolved by evidence, not by "
  "who shouts loudest. The law ranks evidence: the original surveyor's "
  "monuments first, then calls in the deed, then possession and use. "
  "Most disputes settle through a boundary line agreement, a lot-line "
  "adjustment, or mediation; the stubborn ones go to quiet-title "
  "lawsuits where a judge fixes the line. Surveyors serve as the "
  "expert witnesses, retracing the original survey and testifying to "
  "where the legal boundary lies.",
  "Resolution starts with both sides hiring surveyors to retrace the "
  "record. If the surveys agree, the parties sign a boundary line "
  "agreement and record it. If they disagree, mediation or a joint "
  "survey may follow. Litigation — quiet title, ejectment, declaratory "
  "judgment — puts the evidence before a judge, who applies the "
  "hierarchy of calls and doctrines like acquiescence, estoppel, and "
  "adverse possession. The judgment is recorded, and a surveyor "
  "monuments the adjudicated line.",
  ["Resolved by evidence hierarchy, not argument.",
   "Original monuments outrank measurements and area.",
   "Most settle by agreement, adjustment, or mediation.",
   "Courts fix lines through quiet-title suits."],
  ["Surveyors must retrace the original survey, not impose new lines.",
   "Agreements affecting title should be written and recorded.",
   "Litigation requires expert survey testimony."],
  ["State boundary and quiet-title statutes.",
   "Rules of evidence for survey testimony."],
  ["Brown, C. et al. - Evidence and Procedures for Boundary Location.",
   "State quiet-title statutes."],
  "In the Signature land system a settled boundary is a sworn peace: "
  "the evidence weighed, the line marked in iron, and the recorded "
  "agreement a covenant that neighbors can build upon.",
  {"acres": 0.75, "corners": 4, "disputed_ft": 3.5}),

E("Adverse Possession", "Compounded", 19, "compounded",
  "Adverse possession is the doctrine by which a trespasser can become "
  "the legal owner: open, notorious, hostile, continuous, and exclusive "
  "possession of land for the full statutory period — often 10 to 21 "
  "years — can ripen into title. The doctrine punishes sleeping owners "
  "and rewards productive use; the classic case is the neighbor whose "
  "fence stood three feet over the line for decades. Some states also "
  "require payment of taxes or color of title (a flawed deed). A "
  "court quiets title in the possessor's favor, and the new title is "
  "as good as any. It cannot run against government land, and generally "
  "not against Torrens-registered land.",
  "The claimant proves each element with evidence: surveys showing the "
  "encroachment, photos of use, tax receipts, witness testimony. The "
  "owner can defeat the claim by showing permission (defeating "
  "'hostile'), interruption, or a shorter period. Courts strictly "
  "construe the elements against the claimant. Success ends in a quiet-"
  "title judgment that is recorded, giving the possessor marketable "
  "title. Title insurers and buyers treat long-standing encroachments "
  "as red flags precisely because of this doctrine.",
  ["Trespasser can gain title after the statutory period.",
   "Requires open, notorious, hostile, continuous, exclusive possession.",
   "Punishes sleeping owners; rewards productive use.",
   "Cannot run against government land."],
  ["Every element must be proved; courts construe strictly.",
   "Some states require tax payment or color of title.",
   "Title comes only through a quiet-title judgment."],
  ["State adverse possession statutes.",
   "State case law on the elements."],
  ["State adverse possession statutes.",
   "Restatement (Third) of Property: Servitudes (related doctrines)."],
  "In the Signature land system adverse possession is the sworn statute "
  "of limitations on neglect: the land itself testifies through long "
  "use, and the court's decree is the covenant that settled facts "
  "become settled title.",
  {"acres": 0.1, "corners": 4, "years_possessed": 22}),

E("Mineral Rights and Severed Estates", "Compounded", 20, "compounded",
  "Mineral rights are the ownership of what lies beneath: oil, gas, "
  "coal, metals, and stone. In much of America the mineral estate has "
  "been severed from the surface estate — one party owns the farm, "
  "another owns the minerals below it. The mineral owner generally "
  "holds the dominant right to use the surface as reasonably necessary "
  "to extract, unless the severance deed says otherwise. Oil and gas "
  "leases, royalty interests, and pooling agreements govern "
  "development. Title searches must trace the mineral chain separately, "
  "because a surface deed that says nothing about minerals may convey "
  "none of them.",
  "Severance happens by reservation or grant in a deed: 'reserving all "
  "minerals.' The mineral owner leases to operators for a bonus plus "
  "royalty, typically for a primary term extended by production. "
  "Pooling combines tracts into drilling units under state oil-and-gas "
  "commission rules. Surface owners negotiate surface-use agreements "
  "for location and damages. In split-estate conflicts, state law and "
  "the severance language decide how much surface the mineral owner "
  "may disturb.",
  ["Ownership of subsurface oil, gas, coal, and metals.",
   "Often severed from surface ownership.",
   "Mineral estate usually dominant for reasonable extraction.",
   "Title must trace the mineral chain separately."],
  ["Severances must be in writing and recorded.",
   "Oil and gas development follows state commission rules.",
   "Leases require bonus, royalty, and term provisions."],
  ["State oil and gas conservation acts.",
   "State recording statutes (mineral severances)."],
  ["State oil and gas commission regulations.",
   "Kuntz, O. - A Treatise on the Law of Oil and Gas."],
  "In the Signature land system severed minerals are a sworn depth: "
  "the surface covenant covers the soil, the mineral covenant the "
  "riches below, and the severance deed the seal between the two "
  "worlds.",
  {"acres": 320.0, "corners": 4, "royalty_pct": 12.5}),

E("Water Rights: Prior Appropriation and Riparian Doctrines", "Compounded", 21,
  "compounded",
  "American water law runs on two great doctrines. Prior appropriation — "
  "'first in time, first in right' — governs the arid West: the first "
  "to divert water and put it to beneficial use holds the senior right, "
  "and in drought seniors take their full share before juniors get a "
  "drop. Riparian rights govern the wetter East: owners of land along a "
  "waterway may make reasonable use of it, sharing shortages "
  "correlatively. Groundwater adds its own rules. Water rights are "
  "property — bought, sold, and leased — and in the West they are "
  "recorded and administered by state engineers under elaborate "
  "priority systems.",
  "Appropriators perfect rights by diverting and applying water to "
  "beneficial use, then adjudicating or permitting the right with the "
  "state. Priority dates are everything: the state engineer curtails "
  "juniors in shortage. Transfers require showing no injury to other "
  "users. Riparian owners share under reasonableness tests adjudicated "
  "by courts. Interstate compacts and federal projects overlay state "
  "law on shared rivers like the Colorado. Measurement, reporting, and "
  "enforcement keep the system honest.",
  ["Two doctrines: prior appropriation (West) and riparian (East).",
   "Prior appropriation: first in time, first in right.",
   "Riparian: reasonable shared use by waterfront owners.",
   "Water rights are transferable property."],
  ["Appropriations require diversion to beneficial use and state recognition.",
   "Transfers must show no injury to other right holders.",
   "Interstate waters follow compacts and federal law."],
  ["State water codes (e.g., prior appropriation statutes).",
   "Interstate river compacts."],
  ["State engineer / water resource department publications.",
   "Getches, D. - Water Law in a Nutshell."],
  "In the Signature land system water rights are a sworn flow: the "
  "senior's priority a covenant of first claim, the shared river a "
  "covenant of reasonable neighbors, and the state engineer's decree "
  "the seal on every drop.",
  {"acres": 80.0, "corners": 4, "acre_feet": 120}),

E("Conservation Easements", "Compounded", 22, "compounded",
  "A conservation easement is a voluntary legal agreement that "
  "permanently limits development on land to protect its conservation "
  "values — wildlife habitat, farmland, scenic views, historic "
  "character — while the owner keeps owning and using it. The owner "
  "grants the easement to a land trust or government agency, which "
  "monitors and enforces it forever; the restrictions run with the "
  "land through every future sale. Donors may claim federal tax "
  "deductions for qualified easements. Millions of acres are protected "
  "this way, making conservation easements one of America's largest "
  "private land-conservation tools.",
  "The landowner and land trust negotiate the easement's terms: what "
  "is restricted (subdivision, mining, development), what continues "
  "(farming, forestry, a homesite), and how compliance is monitored. A "
  "baseline documentation report records the property's condition. The "
  "deed is recorded, binding all future owners. The trust visits "
  "annually to verify compliance. For tax deductions, the easement must "
  "meet Internal Revenue Code requirements — qualified organization, "
  "conservation purpose, perpetuity — and be substantiated by appraisal.",
  ["Voluntary permanent limits on development for conservation.",
   "Owner keeps the land; a trust or agency enforces the easement.",
   "Runs with the land through all future sales.",
   "Donors may earn federal tax deductions."],
  ["Must be granted to a qualified organization in perpetuity.",
   "Tax deductions require appraisal and conservation-purpose findings.",
   "Baseline documentation must record pre-easement condition."],
  ["Internal Revenue Code section 170(h) (qualified conservation contributions).",
   "State conservation easement enabling acts."],
  ["Land Trust Alliance - Standards and Practices.",
   "Internal Revenue Code section 170(h)."],
  "In the Signature land system a conservation easement is a sworn "
  "promise to the future: the land's wild character sealed by covenant, "
  "the owner's generosity recorded, and the trust's annual visit the "
  "keeping of the vow.",
  {"acres": 250.0, "corners": 10, "protected_pct": 95}),

E("Eminent Domain", "Compounded", 23, "compounded",
  "Eminent domain is the government's power to take private property "
  "for public use, with just compensation — the Fifth Amendment's "
  "Takings Clause. Governments use it for highways, schools, utilities, "
  "and flood control; the Supreme Court's Kelo v. New London (2005) "
  "allowed takings for economic development as 'public use,' sparking "
  "many states to tighten their laws. The power belongs to federal, "
  "state, and local governments and to delegated utilities. Owners are "
  "entitled to fair market value, and to challenge the taking's "
  "necessity and the compensation's adequacy in court.",
  "The condemning authority appraises the property, makes an offer, "
  "and negotiates; most takings settle without trial. If no agreement, "
  "it files a condemnation action, deposits estimated compensation, and "
  "takes possession while the court decides final value. Commissioners "
  "or juries hear valuation evidence — comparable sales, income, cost "
  "approaches. Owners may claim severance damages to remaining land and "
  "relocation benefits under the Uniform Relocation Act. Appeals review "
  "public-use findings and awards.",
  ["Government power to take private property for public use.",
   "Requires just compensation under the Fifth Amendment.",
   "Kelo (2005) broadened 'public use'; many states then narrowed it.",
   "Owners may challenge necessity and compensation in court."],
  ["Taking requires a public-use finding and statutory authority.",
   "Compensation must be fair market value, judicially reviewable.",
   "Relocation assistance follows the Uniform Relocation Act."],
  ["Fifth Amendment Takings Clause.",
   "State eminent domain procedure acts."],
  ["Kelo v. City of New London, 545 U.S. 469 (2005).",
   "Uniform Relocation Assistance and Real Property Acquisition Policies Act."],
  "In the Signature land system eminent domain is the sworn taking: "
  "the public need weighed openly, the owner's loss counted honestly, "
  "and just compensation the covenant that power pays its debts.",
  {"acres": 12.0, "corners": 6, "award_usd": 2400000}),

E("Land Trusts", "Compounded", 24, "compounded",
  "Land trusts are nonprofit organizations that protect land through "
  "ownership and conservation easements. More than a thousand local, "
  "regional, and national trusts — from small community trusts to The "
  "Nature Conservancy — have conserved tens of millions of acres in the "
  "United States. They accept donated land and easements, buy threatened "
  "parcels, monitor easements annually, and defend them in court when "
  "violated. Accredited trusts follow the Land Trust Alliance's "
  "Standards and Practices, the profession's mark of permanence: a "
  "trust must be built to outlive its founders, because easements are "
  "forever.",
  "A trust works with willing landowners to craft easements or accepts "
  "fee donations, often raising funds for stewardship endowments that "
  "pay for perpetual monitoring. Staff and volunteers walk each "
  "easement yearly, documenting compliance. Violations trigger "
  "negotiation and, if needed, litigation — courts have upheld "
  "easements against violators. Accreditation reviews governance, "
  "finance, and stewardship. The trust's public benefit mission "
  "qualifies its work for charitable tax treatment.",
  ["Nonprofits protecting land via ownership and easements.",
   "1000+ trusts have conserved tens of millions of acres.",
   "Monitor easements annually; defend them in court.",
   "Accreditation marks trusts built to last forever."],
  ["Must operate as charitable organizations with public benefit.",
   "Easements require perpetual monitoring capacity.",
   "Accreditation follows Land Trust Alliance standards."],
  ["Land Trust Alliance Standards and Practices.",
   "Internal Revenue Code charitable organization rules."],
  ["Land Trust Alliance - Standards and Practices.",
   "Land Trust Alliance census data."],
  "In the Signature land system a land trust is a sworn guardian: the "
  "deed held in trust for the wild, the annual walk a covenant of "
  "vigilance, and accreditation the seal that the guardian will "
  "endure.",
  {"acres": 5000.0, "corners": 0, "easements_held": 140}),

# ---------------- ADVANCED 25-34 ----------------

E("FGDC Cadastral Data Content Standard", "Advanced", 25, "advanced",
  "The Federal Geographic Data Committee's Cadastral Data Content "
  "Standard defines the common language for parcel data across America: "
  "what a parcel record must contain, how corners and boundaries are "
  "described, and how data is exchanged between counties, states, and "
  "federal agencies. It models the cadastre as parcels, corners, "
  "boundaries, and survey control, with attributes for identifiers, "
  "area, legal description references, and accuracy. Federal land-"
  "managing agencies publish to it; states align their parcel programs "
  "to it. The standard is why a parcel dataset from Oregon can be "
  "understood in Florida — the foundation of a national parcel fabric.",
  "Data producers map their local parcel attributes to the standard's "
  "entities and publish with FGDC-compliant metadata. The standard "
  "defines parcel identifiers, corner roles (found, set, computed), "
  "boundary evidence, and lineage back to source documents. Compliance "
  "is tested through schema validation and content review. The Bureau "
  "of Land Management and the U.S. Forest Service publish national "
  "datasets to the standard, and the FGDC maintains it through public "
  "review as technology and practice evolve.",
  ["Common language for parcel data nationwide.",
   "Models parcels, corners, boundaries, and survey control.",
   "Enables a national parcel fabric across jurisdictions.",
   "Maintained by the FGDC through public review."],
  ["Published data must map to the standard's entities.",
   "Metadata must document source, accuracy, and lineage.",
   "Updates follow the FGDC public review process."],
  ["FGDC Cadastral Data Content Standard (FGDC-STD-013).",
   "FGDC metadata standards."],
  ["Federal Geographic Data Committee - Cadastral Data Content Standard.",
   "FGDC-STD-013 documentation."],
  "In the Signature land system the FGDC standard is the sworn grammar "
  "of parcels: every attribute a word with one meaning everywhere, "
  "every exchange a covenant that no county's truth is lost in "
  "translation.",
  {"acres": 0.0, "corners": 0, "entities": 4}),

E("Title Insurance and Deed Fraud", "Advanced", 26, "advanced",
  "Title insurance protects buyers and lenders against losses from "
  "title defects — forged deeds, missed liens, undisclosed heirs — that "
  "a search did not catch. Unlike other insurance it looks backward, "
  "insuring the past rather than the future: the insurer searches, "
  "clears what it can, and insures over the rest. The owner's policy "
  "protects the buyer; the lender's policy protects the mortgage. Deed "
  "fraud — forged signatures, impersonated owners, fake notarizations, "
  "increasingly powered by identity theft — is the growing threat the "
  "industry fights with verification, underwriting standards, and "
  "county fraud-alert programs. A single forged deed can cloud a "
  "title for years.",
  "At closing, the title agent searches, issues a commitment listing "
  "requirements and exceptions, clears liens and judgments, and issues "
  "policies after recording. Underwriters set standards for identity "
  "verification, notary compliance, and suspicious-transaction review. "
  "When fraud strikes, the insurer defends the title in court and pays "
  "covered losses. Counties fight back with free property-fraud alerts "
  "that notify owners of filings in their name. ALTA best practices "
  "govern settlement procedures nationwide.",
  ["Insures against past title defects the search missed.",
   "Owner's policy protects buyer; lender's policy protects mortgage.",
   "Deed fraud via forgery and impersonation is the growing threat.",
   "Insurer searches, clears, and defends the title."],
  ["Policies require a professional search and underwriter review.",
   "Closings must follow ALTA settlement best practices.",
   "Fraud suspicions must be investigated before insuring."],
  ["State title insurance rate and form regulation.",
   "ALTA Best Practices Framework."],
  ["American Land Title Association - best practices and fraud guidance.",
   "State departments of insurance - title regulation."],
  "In the Signature land system title insurance is the sworn shield: "
  "the search the watchful eye, the policy the covenant that a hidden "
  "forgery will not steal a family's home.",
  {"acres": 0.6, "corners": 4, "policy_amount": 450000}),

E("The 3D Cadastre", "Advanced", 27, "advanced",
  "The 3D cadastre records property in three dimensions: not just the "
  "lot's footprint but the air above and the earth below, divided into "
  "volumetric parcels. As cities stack condominiums, tunnels, and "
  "utility corridors through the same column of space, flat maps fail — "
  "the 3D cadastre gives each volume its own legal identity. Pioneered "
  "in the Netherlands, Queensland, and other jurisdictions, and studied "
  "by the International Federation of Surveyors, it models legal spaces "
  "as polyhedra linked to rights, restrictions, and responsibilities. "
  "American practice approaches it through condominium law, air-rights "
  "deals, and subsurface easements; the full 3D register is the "
  "frontier.",
  "A 3D cadastre is built from legal descriptions extended into the "
  "vertical: floor plans with elevations for condominiums, tunnel "
  "alignments with clearance envelopes, utility corridors with depth "
  "ranges. Surveyors capture as-built geometry with scanners and GNSS; "
  "lawyers draft volumetric descriptions; the register stores each 3D "
  "parcel with its rights. Visualization tools let the public see who "
  "owns which slice of the column. Standards work through ISO 19152 "
  "(the Land Administration Domain Model) guides implementation.",
  ["Records property as volumetric parcels, not flat lots.",
   "Gives air, surface, and subsurface each a legal identity.",
   "Needed for condos, tunnels, and utility corridors.",
   "Guided by ISO 19152 Land Administration Domain Model."],
  ["Volumetric descriptions require surveyed 3D geometry.",
   "Rights in each volume must be legally defined.",
   "Registers must link volumes to rights and restrictions."],
  ["ISO 19152:2012 Land Administration Domain Model.",
   "State condominium and air-rights statutes."],
  ["International Federation of Surveyors - 3D cadastre publications.",
   "ISO 19152:2012."],
  "In the Signature land system the 3D cadastre is the sworn column: "
  "every cubic space named and bounded, every stacked right a covenant "
  "with its neighbors above and below.",
  {"acres": 0.2, "corners": 8, "volumes": 14}),

E("General Land Office (GLO) Historical Records", "Advanced", 28, "advanced",
  "The General Land Office records are the birth certificates of "
  "American land titles: the plats, field notes, and patents documenting "
  "how the public domain passed into private hands. The GLO, created in "
  "1812, surveyed the public lands and issued patents — the federal "
  "government's original deeds — to homesteaders, railroads, miners, and "
  "states. Its surveyors' field notes describe the land as it was: "
  "prairies, forests, swamps, and the original section corners. The "
  "Bureau of Land Management now preserves these records and publishes "
  "them online; every western title search can trace back to a GLO "
  "patent, the root of the chain.",
  "Researchers and surveyors use the GLO database to find the patent "
  "that first conveyed a parcel, then pull the township plat and the "
  "surveyor's field notes. The notes reveal original corner monuments "
  "and their accessories (bearing trees, pits), which control modern "
  "boundary retracement. Historians mine the notes for ecology — "
  "witness trees map pre-settlement forests. Title examiners cite the "
  "patent as the root of title. Digitization has made millions of "
  "images searchable by legal description.",
  ["Birth certificates of American land titles.",
   "Plats, field notes, and patents from 1812 onward.",
   "Original corners described in field notes control today.",
   "Preserved and published online by the BLM."],
  ["Patents are the root of title for former public-domain land.",
   "Retracement must use original notes, not modern measurement.",
   "Records are public and permanently preserved."],
  ["Federal land patent statutes (homestead, mining, railroad acts).",
   "BLM records preservation authorities."],
  ["Bureau of Land Management - GLO Records database.",
   "General Land Office history (1812 establishment)."],
  "In the Signature land system the GLO records are the sworn genesis: "
  "every patent a first covenant between the republic and a settler, "
  "every field note a surveyor's testimony of the land as it was.",
  {"acres": 0.0, "corners": 0, "patents_issued_millions": 5}),

E("Bureau of Land Management (BLM) Land Records", "Advanced", 29, "advanced",
  "The Bureau of Land Management keeps the records for the 245 million "
  "acres of public land it administers — the nation's largest land "
  "manager. Created in 1946 by merging the General Land Office and the "
  "Grazing Service, the BLM maintains the official survey plats, master "
  "title plats showing federal ownership status, land-use plans, grazing "
  "allotments, mining claims, and oil and gas leases. Its LR2000 and "
  "successor Mineral and Land Records System track every authorization "
  "on public land. For anyone dealing with federal land — ranchers, "
  "miners, energy companies, conservationists — BLM records are the "
  "source of truth.",
  "The BLM adjudicates and records mining claims, issues grazing "
  "permits, leases minerals through competitive sales, and documents "
  "rights-of-way — each action entering the land records system with "
  "its legal description. Master title plats, updated continuously, show "
  "the current federal ownership pattern by township. Cadastral survey "
  "crews resurvey and monument federal boundaries. Records are public, "
  "and the agency publishes geospatial data to national standards. "
  "Administrative decisions can be appealed to the Interior Board of "
  "Land Appeals.",
  ["Records for 245 million acres of public land.",
   "Maintains survey plats, master title plats, claims, and leases.",
   "Tracks every authorization in its land records system.",
   "Created 1946 from the GLO and Grazing Service."],
  ["Authorizations require applications, review, and recording.",
   "Mining claims must meet location and annual filing rules.",
   "Decisions are appealable to the Interior Board of Land Appeals."],
  ["Federal Land Policy and Management Act of 1976.",
   "General Mining Law of 1872.",
   "Mineral Leasing Act of 1920."],
  ["Bureau of Land Management - land records systems.",
   "Federal Land Policy and Management Act, Pub. L. 94-579."],
  "In the Signature land system BLM records are the sworn ledger of "
  "the commons: every claim staked, every lease signed, every plat a "
  "covenant of what the nation holds for all.",
  {"acres": 245000000.0, "corners": 0, "grazing_allotments": 18000}),

E("Digital Land Registries", "Advanced", 30, "advanced",
  "Digital land registries move the recordation system from paper books "
  "to electronic systems: e-recording of deeds and mortgages, online "
  "search portals, and in the most advanced jurisdictions, fully "
  "electronic conveyancing. The Uniform Real Property Electronic "
  "Recording Act, adopted in most states, gives electronic documents "
  "the same legal standing as paper. Title companies submit documents "
  "electronically; recorders ingest, index, and return them in hours "
  "instead of weeks. The frontier — tested in Sweden, Georgia, and "
  "pilot projects elsewhere — uses distributed ledgers to make the "
  "register tamper-evident. The legal principles do not change: notice, "
  "priority, and authenticity, now at digital speed.",
  "E-recording works through trusted submitters: title companies and "
  "law firms send digitally signed documents through intermediaries to "
  "the recorder's system, which validates, stamps, indexes, and "
  "archives them. Standards like PRIA's e-recording specifications "
  "ensure interoperability. Electronic notarization and remote online "
  "notarization authenticate signers by video and credential analysis. "
  "Audit trails record every touch. Cybersecurity, backup, and "
  "disaster recovery protect the permanent record.",
  ["Electronic recording, search, and conveyancing.",
   "URPERA gives e-documents equal legal standing in most states.",
   "Turns weeks of paper handling into hours.",
   "Legal principles unchanged: notice, priority, authenticity."],
  ["E-documents must meet the same legal sufficiency as paper.",
   "Submitters must be authenticated and authorized.",
   "Systems must preserve permanent, tamper-evident archives."],
  ["Uniform Real Property Electronic Recording Act.",
   "PRIA e-recording standards.",
   "State remote online notarization statutes."],
  ["Property Records Industry Association - e-recording standards.",
   "Uniform Law Commission - URPERA."],
  "In the Signature land system the digital registry is the sworn "
  "ledger of light: every electronic stamp a covenant of instant "
  "notice, every audit trail a witness that the record was never "
  "altered.",
  {"acres": 0.0, "corners": 0, "docs_e_recorded_pct": 85}),

E("Parcel Data Accuracy Classes", "Advanced", 31, "advanced",
  "Not all parcel maps are equal: accuracy classes tell users how much "
  "to trust the lines. At the top, survey-grade parcels built from "
  "recorded plats and field surveys locate lines within centimeters. "
  "Compiled parcels from deeds and imagery may be within a few feet. "
  "Tax-map sketches can be off by tens of feet — fine for assessment, "
  "dangerous for building a fence. Responsible GIS programs classify "
  "every polygon, publish the classification in metadata, and warn "
  "users that only a survey establishes a boundary. Accuracy classes "
  "turn a pretty map into an honest one.",
  "The GIS department assigns each parcel polygon an accuracy class "
  "based on its source: recorded plat, surveyed tie, digitized deed, "
  "or photo-interpreted estimate. Metadata records the class, source "
  "date, and estimated positional accuracy per ASPRS standards. Web "
  "maps display disclaimers tied to the class. Upgrades happen as "
  "better sources arrive — a subdivision plat replaces a sketch. "
  "Contracts for GIS services specify the required class, and "
  "liability turns on whether the classification was honest.",
  ["Classify how much to trust each parcel polygon.",
   "Survey-grade: centimeters; sketches: tens of feet.",
   "Must be published in metadata with the map.",
   "Only a survey establishes a boundary."],
  ["Every polygon must carry a source-based accuracy class.",
   "Metadata must state estimated positional accuracy.",
   "Public maps must warn against boundary reliance."],
  ["ASPRS Positional Accuracy Standards for Digital Geospatial Data.",
   "FGDC metadata standards."],
  ["American Society for Photogrammetry and Remote Sensing - accuracy standards.",
   "Federal Geographic Data Committee - metadata standards."],
  "In the Signature land system accuracy classes are sworn honesty: "
  "the map confesses its own precision, the metadata bears witness, "
  "and the user is covenanted the truth about the lines.",
  {"acres": 0.0, "corners": 0, "classes": 5}),

E("Surveyor Licensing and Professional Ethics", "Advanced", 32, "advanced",
  "Land surveying is a licensed profession: only a Professional Land "
  "Surveyor may legally determine boundaries in nearly every state. "
  "Licensure typically requires an accredited degree, years of "
  "progressive experience under a licensed surveyor, and two national "
  "examinations (Fundamentals and Principles and Practice) plus a state "
  "exam. Licensees owe duties to the public, clients, and the "
  "profession: competence, honesty, confidentiality, and — uniquely — "
  "fidelity to the record, even when it hurts the client who hired them. "
  "State boards discipline misconduct and can revoke licenses. The "
  "surveyor's seal on a map is a professional oath in ink.",
  "Candidates document education and experience, pass examinations, and "
  "apply to the state board. Licensed surveyors maintain competence "
  "through continuing education. Practice rules require written "
  "contracts, field standards, monumentation, and recorded maps. Ethics "
  "codes — such as NSPS's — demand that the surveyor follow the "
  "evidence where it leads: a boundary is where the original survey put "
  "it, not where the client wishes it were. Complaints trigger board "
  "investigation, hearings, and sanctions from reprimand to revocation.",
  ["Licensed profession: only PLSs may determine boundaries.",
   "Requires degree, experience, and national plus state exams.",
   "Ethics demand fidelity to the record over client wishes.",
   "State boards license, educate, and discipline."],
  ["Boundary work requires an active state license.",
   "Continuing education is mandatory for renewal.",
   "Sealed maps carry professional liability."],
  ["State surveying practice acts.",
   "NSPS Model Law and ethics creed."],
  ["National Society of Professional Surveyors - ethics and model law.",
   "National Council of Examiners for Engineering and Surveying - exam standards."],
  "In the Signature land system the surveyor's seal is the sworn oath "
  "of the profession: competence the vow, honesty the practice, and "
  "fidelity to the original survey the covenant no client can buy.",
  {"acres": 0.0, "corners": 0, "licensed_states": 50}),

E("Datums and Coordinate Systems (NAD83, NAVD88)", "Advanced", 33, "advanced",
  "A datum is the reference frame that gives coordinates meaning: the "
  "mathematical model of the Earth and the network of control points "
  "realizing it. The North American Datum of 1983 (NAD83) underpins "
  "American horizontal surveying; the North American Vertical Datum of "
  "1988 (NAVD88) underpins elevations. Coordinates without a stated "
  "datum are ambiguous — the same point differs by meters between "
  "NAD83 and newer frames. NOAA's National Geodetic Survey maintains "
  "the datums through the CORS network of continuously operating GPS "
  "stations, and is modernizing them to time-dependent frames that "
  "account for tectonic motion.",
  "Surveyors connect their work to datum control via CORS stations or "
  "published benchmarks, transform field coordinates into the project "
  "datum, and report which realization they used (e.g., NAD83 (2011)). "
  "Transformations between datums use published models; mixing datums "
  "without transformation corrupts the work. Elevations tie to NAVD88 "
  "benchmarks or GNSS-derived orthometric heights. Metadata must state "
  "datum, epoch, and transformation path so future surveyors can "
  "reproduce the positions.",
  ["Datums give coordinates their meaning.",
   "NAD83 (horizontal) and NAVD88 (vertical) underpin US surveying.",
   "Same point differs by meters between datums.",
   "N GS modernizing to time-dependent frames."],
  ["Surveys must state datum, realization, and epoch.",
   "Transformations must use published models.",
   "Control must come from the national reference frame."],
  ["NOAA National Geodetic Survey datum definitions.",
   "Federal Geographic Data Committee geospatial positioning standards."],
  ["National Geodetic Survey - datum documentation.",
   "Federal Geographic Data Committee - positioning standards."],
  "In the Signature land system the datum is the sworn foundation of "
  "measure: every coordinate a covenant with the Earth's true shape, "
  "every stated epoch an honest witness to a moving planet.",
  {"acres": 0.0, "corners": 0, "cords_stations": 2000}),

E("Land Records Disaster Recovery", "Advanced", 34, "advanced",
  "When courthouses burn and floods drown the vaults, land records "
  "disaster recovery rebuilds the public memory of ownership. History "
  "is full of lost records — the San Francisco earthquake and fire of "
  "1906 destroyed the city's land records, forcing California to pass "
  "the McEnerney Act letting courts re-establish titles. Modern "
  "recovery rests on redundancy: microfilm and digital backups stored "
  "offsite, e-recording systems with disaster failover, and statutes "
  "authorizing courts to quiet title and reconstitute the record from "
  "secondary evidence — title company plants, abstracts, and owners' "
  "copies. A records office without a backup plan is a disaster "
  "waiting for its date.",
  "Recovery follows the plan: activate backups, assess what survived, "
  "and restore systems from offsite copies. Where records are truly "
  "lost, courts take petitions to establish title from deeds in hand, "
  "title-plant copies, tax rolls, and testimony. Legislatures pass "
  "curative acts validating imperfect records. Title insurers extend "
  "coverage over the gaps. Prevention — digitization, geographic "
  "redundancy, tested restores, and e-recording — is the standing duty; "
  "recovery is the price of its neglect.",
  ["Rebuilds ownership records after courthouse disasters.",
   "1906 San Francisco fire is the classic case; McEnerney Act followed.",
   "Modern defense: offsite backups, e-recording failover.",
   "Courts re-establish titles from secondary evidence."],
  ["Recorders must maintain offsite, tested backups.",
   "Re-established titles require court proceedings.",
   "Curative acts validate imperfect restored records."],
  ["State curative and marketable title acts.",
   "Federal and state records preservation mandates."],
  ["California McEnerney Act (1906, as amended).",
   "Property Records Industry Association - disaster planning guidance."],
  "In the Signature land system disaster recovery is the sworn "
  "resurrection of memory: the backup a covenant kept in a far vault, "
  "the court's decree the seal of restored truth, and the digitized "
  "record the promise that fire will not win twice.",
  {"acres": 0.0, "corners": 0, "backup_copies": 3}),
]
