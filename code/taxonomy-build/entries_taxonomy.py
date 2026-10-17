#!/usr/bin/env python3
"""Seed entries for the Taxonomy field build (field #7, taxonomy order).

Verified 2026-10-17: manifest "taxonomy" slugs are all technology-field
taxonomies (software-labs-taxonomy, core-engine-taxonomy,
storage-repository-taxonomy, network-interconnect-taxonomy,
hardware-fabrication-taxonomy). Keyword hits 'ai-types'
("Russell and Norvig's agent taxonomy") and 'system-logs' ("error
taxonomy") are spurious. NO database covers biological taxonomy as a
science. So this build creates two NEW databases:

  taxonomy              — The Taxonomy Database (public-harvest: real,
                          fact-checked taxonomy science — Linnaean system,
                          ranks, binomial nomenclature, type specimens,
                          nomenclature codes ICZN/ICNafp/ICNP, synonymy,
                          phylogenetics, cladistics, molecular systematics,
                          DNA barcoding, taxonomic revisions, biodiversity
                          informatics)
  taxonomy-signature    — The Taxonomy Signature Database (his original
                          Signature interpretation; src signature, titles
                          suffixed " (Signature Edition)", never presented
                          as authentic public record)

36 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable,
stdlib-only Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation constants (standard taxonomy literature)
CIT_LINNAEUS = ("Linnaeus, C. (1758). 'Systema Naturae', 10th ed. "
                "Laurentius Salvius, Stockholm.")
CIT_DARWIN = ("Darwin, C. (1859). 'On the Origin of Species'. John Murray, "
              "London.")
CIT_MAYR = ("Mayr, E. (1942). 'Systematics and the Origin of Species'. "
            "Columbia University Press.")
CIT_HENNIG = ("Hennig, W. (1966). 'Phylogenetic Systematics'. University of "
              "Illinois Press.")
CIT_HEBERT = ("Hebert, P. D. N., Cywinska, A., Ball, S. L. & deWaard, J. R. "
              "(2003). 'Biological identifications through DNA barcodes.' "
              "Proceedings of the Royal Society B 270: 313-321.")
CIT_WOESE = ("Woese, C. R., Kandler, O. & Wheelis, M. L. (1990). 'Towards a "
             "natural system of organisms: proposal for the domains Archaea, "
             "Bacteria, and Eucarya.' PNAS 87: 4576-4579.")
CIT_WHITTAKER = ("Whittaker, R. H. (1969). 'New concepts of kingdoms of "
                 "organisms.' Science 163: 150-160.")
CIT_ICZN = ("International Commission on Zoological Nomenclature (1999). "
            "'International Code of Zoological Nomenclature', 4th ed.")
CIT_ICNAFP = ("Turland, N. J. et al. (eds.) (2018). 'International Code of "
              "Nomenclature for algae, fungi, and plants (Shenzhen Code)'.")
CIT_MORA = ("Mora, C., Tittensor, D. P., Adl, S., Simpson, A. G. B. & Worm, "
            "B. (2011). 'How many species are there on Earth and in the "
            "ocean?' PLoS Biology 9: e1001127.")
CIT_FELSENSTEIN = ("Felsenstein, J. (1981). 'Evolutionary trees from DNA "
                   "sequences: a maximum likelihood approach.' Journal of "
                   "Molecular Evolution 17: 368-376.")
CIT_SAITOU = ("Saitou, N. & Nei, M. (1987). 'The neighbor-joining method: a "
              "new method for reconstructing phylogenetic trees.' Molecular "
              "Biology and Evolution 4: 406-425.")
CIT_CRACRAFT = ("Cracraft, J. (1983). 'Species concepts and speciation "
                "analysis.' Current Ornithology 1: 159-187.")
CIT_ZUCKERKANDL = ("Zuckerkandl, E. & Pauling, L. (1965). 'Evolutionary "
                   "divergence and convergence in proteins.' In Bryson, V. & "
                   "Vogel, H. J. (eds.), 'Evolving Genes and Proteins'.")
CIT_SIMPSON = ("Simpson, G. G. (1961). 'Principles of Animal Taxonomy'. "
               "Columbia University Press.")
CIT_STD = ("Standard taxonomy literature (peer-reviewed textbooks and "
           "journals).")
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "taxonomy, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-taxonomy", "name": "What Is Taxonomy: The Science of Naming and Classifying Life",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Taxonomy is the science of naming, defining, and classifying organisms — "
  "the filing system of all biology. Every species gets a unique scientific "
  "name and a place in a hierarchy that reflects evolutionary relationships, "
  "so a researcher in Tokyo and one in Nairobi mean exactly the same organism "
  "when they write a name. About two million species have been formally "
  "described, yet estimates of the true total run near 8.7 million "
  "eukaryotes alone (Mora et al., 2011), meaning roughly three quarters of "
  "species are still unknown to science. Taxonomy has three jobs: "
  "classification (grouping organisms), nomenclature (naming them by formal "
  "rules), and identification (recognizing them in practice). Without it, "
  "biology has no shared vocabulary — no way to say which organism a drug "
  "came from, which pest eats a crop, or which species a law protects."),
 "how_it_works": (
  "Taxonomy works by comparing organisms and sorting them into nested groups "
  "based on shared characteristics inherited from common ancestors. A "
  "taxonomist collects specimens, studies their anatomy, DNA, behavior, and "
  "geography, then decides where each population fits in the hierarchy — "
  "species inside genera, genera inside families, and so on up to domains. "
  "New names are published with a formal description, a diagnosis stating "
  "how the organism differs from its relatives, and a designated type "
  "specimen that permanently anchors the name. International codes of "
  "nomenclature govern how names are formed, which name wins when two exist "
  "for one organism, and how names change when new evidence regroups "
  "species. Modern taxonomy layers DNA evidence over morphology, so trees "
  "built from genes test and refine the groups built from bodies."),
 "key_points": [
  "Taxonomy: the science of naming, defining, and classifying organisms — biology's shared filing system",
  "About 2 million species described; an estimated 8.7 million eukaryotes exist — roughly 75% still unknown",
  "Three jobs: classification (grouping), nomenclature (naming by rules), identification (recognizing)",
  "Every name sits in a nested hierarchy reflecting evolutionary relationships",
  "New names require a published description, a diagnosis, and a designated type specimen",
  "DNA evidence now tests and refines groups first built from anatomy",
 ],
 "requirements": [
  "Curiosity about how living things are organized and named",
  "A field guide or species list to practice recognizing named organisms",
  "Willingness to learn the Latin-style two-part naming convention",
 ],
 "standards": [
  "Names follow the international nomenclature codes (ICZN for animals, ICNafp for algae/fungi/plants)",
  "Species counts per Mora et al. (2011) and the Catalogue of Life conventions",
 ],
 "citations": [CIT_MORA, CIT_SIMPSON],
 "sig_lens": (
  "Signature reading: taxonomy is the original information architecture — "
  "every living thing filed, keyed, and retrievable by name. Manon's "
  "Signature take treats the taxonomic hierarchy as the master index of "
  "the living world: learn the ranks first, then every database, museum "
  "drawer, and DNA sequence in the system snaps into its slot."),
 "demo_kind": "taxonomy_scale",
},
{
 "key": "taxonomic-ranks", "name": "The Taxonomic Ranks: From Domain to Subspecies",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "The taxonomic hierarchy is a ladder of nested ranks: Domain, Kingdom, "
  "Phylum, Class, Order, Family, Genus, and Species, with subspecies below "
  "species and optional intermediate ranks (subfamily, superorder, tribe) "
  "where needed. Each rank contains the one below it: the genus Panthera "
  "holds lions, tigers, leopards, jaguars, and snow leopards; the family "
  "Felidae holds Panthera plus all other cat genera; the order Carnivora "
  "holds Felidae plus dogs, bears, and seals. Humans file as Eukarya "
  "(domain), Animalia (kingdom), Chordata (phylum), Mammalia (class), "
  "Primates (order), Hominidae (family), Homo (genus), Homo sapiens "
  "(species). The ranks are human conveniences — evolution produced a "
  "branching tree, and ranks are the labeled shelves we hang on its "
  "branches — but they let any biologist instantly gauge how closely two "
  "organisms are related by the lowest rank they share."),
 "how_it_works": (
  "Ranks work by nesting: an organism belongs to exactly one taxon at each "
  "rank, and each taxon belongs to exactly one taxon at the rank above. To "
  "classify an organism, a taxonomist places it in a genus, and the genus's "
  "position determines every rank above it automatically. Relatedness is "
  "read off the hierarchy: two species in the same genus are closer "
  "relatives than two species merely in the same family. When phylogenetic "
  "evidence shows a group is misplaced, taxonomists move it — the ranks "
  "stay, but the occupants change, which is why classifications get "
  "revised. Intermediate ranks (subfamily, infraorder, tribe) are inserted "
  "when a branch needs finer shelves. The domain rank, added in 1990, sits "
  "above kingdom and splits all cellular life into Bacteria, Archaea, and "
  "Eukarya."),
 "key_points": [
  "Nested ranks: Domain > Kingdom > Phylum > Class > Order > Family > Genus > Species (> Subspecies)",
  "Each organism belongs to exactly one taxon per rank; each taxon nests in one taxon above",
  "Relatedness is read from the lowest rank two organisms share",
  "Humans: Eukarya, Animalia, Chordata, Mammalia, Primates, Hominidae, Homo, Homo sapiens",
  "Ranks are human shelves on evolution's branching tree; occupants move as evidence improves",
  "Intermediate ranks (tribe, subfamily, superorder) add finer shelves where needed",
 ],
 "requirements": [
  "Memorize the eight principal ranks in order",
  "Practice filing two familiar organisms (e.g., human and house cat) through all ranks",
  "A reference classification to check placements against",
 ],
 "standards": [
  "Rank names and endings per the nomenclature codes (e.g., -idae for animal families, -aceae for plant families)",
  "Domain-level classification per Woese, Kandler & Wheelis (1990)",
 ],
 "citations": [CIT_WOESE, CIT_SIMPSON],
 "sig_lens": (
  "Signature reading: the ranks are a compression algorithm — eight labels "
  "that locate any of millions of species. Manon's Signature take treats "
  "each rank as a zoom level on the tree of life: master the zoom levels "
  "and you can navigate from a single bacterium to the whole biosphere "
  "without getting lost."),
 "demo_kind": "rank_ladder",
},
{
 "key": "binomial-nomenclature", "name": "Binomial Nomenclature: The Two-Name Rule",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Binomial nomenclature gives every species a unique two-part Latin-style "
  "name: the genus name (capitalized) followed by the species epithet "
  "(lowercase), both italicized — Homo sapiens, Panthera leo, Escherichia "
  "coli. Introduced by Carl Linnaeus in the 1750s and still the global "
  "standard, the system guarantees that one species has exactly one "
  "correct scientific name at a time, recognized in every language. The "
  "genus groups close relatives; the epithet distinguishes the species "
  "within it. An author citation often follows — Homo sapiens Linnaeus, "
  "1758 — crediting the describer and dating the name, and parentheses "
  "around the author mean the species has since been moved to a different "
  "genus. Because common names vary by language and region (a puma is also "
  "a cougar and a mountain lion), the binomial is the only name that "
  "travels intact across all of science, law, medicine, and trade."),
 "how_it_works": (
  "A binomial is formed by pairing a genus name with a species epithet that "
  "is unique within that genus. The genus is always capitalized, the "
  "epithet always lowercase, and the whole name is italicized (or "
  "underlined in handwriting); in plain text it is often written _Homo "
  "sapiens_. After first mention, the genus may be abbreviated — H. "
  "sapiens. The author and year append the naming history: 'Linnaeus, 1758' "
  "means Linnaeus described it in 1758 under its current genus, while "
  "'(Linnaeus, 1758)' in parentheses means he described it in a different "
  "genus and someone later moved it. The codes enforce uniqueness: no two "
  "animal genera may share a name, and within a genus no two species may "
  "share an epithet. If two names turn out to denote one species, the "
  "older (senior) name wins by priority and the younger becomes a junior "
  "synonym."),
 "key_points": [
  "Two parts: Genus (capitalized) + species epithet (lowercase), both italicized — e.g., Panthera leo",
  "Linnaeus's 1750s system; still the single global standard across all languages",
  "Author + year credit the describer; parentheses mean the species was moved to a new genus",
  "Genus may be abbreviated after first use: P. leo",
  "One species, one correct name at a time — enforced by the nomenclature codes",
  "The binomial survives where common names fail: puma = cougar = mountain lion = Puma concolor",
 ],
 "requirements": [
  "Practice writing binomials with correct capitalization and italics",
  "Learn to expand and abbreviate genus names correctly",
  "A nomenclature code summary for author-citation rules",
 ],
 "standards": [
  "Binomial formation per ICZN Article 5 (animals) and ICNafp (plants/algae/fungi)",
  "Author citation format per ICZN Articles 50-51",
 ],
 "citations": [CIT_LINNAEUS, CIT_ICZN],
 "sig_lens": (
  "Signature reading: the binomial is the original unique identifier — a "
  "two-word primary key invented 250 years before databases. Manon's "
  "Signature take treats every scientific name as a permanent address: "
  "genus is the street, epithet the house number, author the surveyor's "
  "stamp."),
 "demo_kind": "binomial_check",
},
{
 "key": "linnaeus-legacy", "name": "Carl Linnaeus and the Systema Naturae",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Carl Linnaeus (1707-1778), the Swedish naturalist, built the naming "
  "system all of biology still uses. His 'Species Plantarum' (1753) named "
  "thousands of plants with consistent two-part names, and the 10th edition "
  "of 'Systema Naturae' (1758) did the same for animals — the two works are "
  "the legal starting points of botanical and zoological nomenclature, "
  "meaning no name published before them counts. Linnaeus personally "
  "described about 7,700 plant species and some 4,400 animal species, "
  "including Homo sapiens. His hierarchy of class, order, genus, and "
  "species gave every organism an address, and his insistence on short, "
  "standardized descriptions replaced rambling paragraph-long names with "
  "crisp binomials. Though he believed species were fixed creations — "
  "evolution would come a century later with Darwin — his system was "
  "designed so well that it absorbed evolution without breaking: the ranks "
  "simply became branches of a tree instead of shelves in a cabinet."),
 "how_it_works": (
  "Linnaeus's method was ruthless standardization. Every species got a "
  "genus plus a one-word differentia — the distinguishing epithet — "
  "replacing the long descriptive phrases naturalists had used. He sorted "
  "plants by the number and arrangement of stamens and pistils (his "
  "'sexual system'), which was artificial but brilliantly usable, and "
  "animals by teeth, feet, and other hard anatomy. Students he trained — "
  "the 'apostles' — carried the method worldwide, shipping specimens back "
  "to Uppsala for naming. The 1753 and 1758 starting points work as legal "
  "cutoffs: a name counts for priority only if published on or after the "
  "starting date for its group. Modern taxonomists still cite 'L.' "
  "(Linnaeus) as author on thousands of plant names, the most-cited author "
  "in all of nomenclature."),
 "key_points": [
  "Carl Linnaeus (1707-1778): architect of the modern naming system",
  "'Species Plantarum' (1753) and 'Systema Naturae' 10th ed. (1758) are the legal starting points of nomenclature",
  "Personally described ~7,700 plants and ~4,400 animals, including Homo sapiens",
  "Replaced paragraph-long descriptive names with crisp two-word binomials",
  "His hierarchy absorbed Darwinian evolution without breaking: shelves became branches",
  "'L.' remains the most-cited author abbreviation in botanical nomenclature",
 ],
 "requirements": [
  "A timeline of Linnaeus's major publications",
  "Examples of pre-Linnaean polynomial names vs their binomial replacements",
  "Access to digitized pages of Systema Naturae for historical context",
 ],
 "standards": [
  "Nomenclature starting points: 1 May 1753 (most plants), 1 January 1758 (animals)",
  "Author abbreviation 'L.' per the standard author lists",
 ],
 "citations": [CIT_LINNAEUS, CIT_DARWIN],
 "sig_lens": (
  "Signature reading: Linnaeus shipped the first global standard — one "
  "format, every species, worldwide adoption. Manon's Signature take: "
  "study how one man's formatting decision outlasted empires, then apply "
  "the lesson — the best system wins not by being perfect but by being "
  "usable on day one."),
 "demo_kind": "linnaeus_counts",
},
{
 "key": "kingdoms-domains", "name": "Kingdoms and Domains: The Deepest Branches",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "The deepest split in the tree of life is the domain: all cellular life "
  "belongs to Bacteria, Archaea, or Eukarya, a three-domain system proposed "
  "by Carl Woese and colleagues in 1990 from ribosomal RNA sequences. "
  "Before that, R. H. Whittaker's 1969 five-kingdom system — Monera, "
  "Protista, Plantae, Fungi, Animalia — ruled textbooks for decades, "
  "notably recognizing fungi as their own kingdom rather than odd plants. "
  "The shock of the three-domain tree was that Archaea, though "
  "bacteria-like under the microscope, are genetically closer to eukaryotes "
  "— including us — than to true bacteria. Eukarya then divides into the "
  "familiar kingdoms: animals, plants, fungi, and the great grab-bag of "
  "protists (a paraphyletic group taxonomists are still reorganizing into "
  "natural lineages like SAR, Archaeplastida, and Excavata). Every new "
  "organism a taxonomist meets first gets filed at this deepest level, "
  "because the domain determines which nomenclature code and which biology "
  "apply."),
 "how_it_works": (
  "Domain assignment is now done with molecules: the sequence of the small "
  "ribosomal subunit RNA (16S in prokaryotes, 18S in eukaryotes) places any "
  "cellular organism into one of the three domains, because this molecule "
  "evolves slowly and exists in every cell. Within Eukarya, kingdoms are "
  "defined by fundamental body plans and nutrition: animals ingest food, "
  "plants photosynthesize with chloroplasts, fungi digest externally and "
  "absorb, and protists are eukaryotes that are none of the above. "
  "Whittaker's five kingdoms improved on the old plant/animal split by "
  "giving fungi and single-celled life their due, but DNA showed 'Protista' "
  "and even 'Monera' were unnatural grab-bags, which is why the domain "
  "level was added above them. Modern deep classification keeps splitting "
  "protists into monophyletic supergroups as genomes accumulate."),
 "key_points": [
  "Three domains (Woese et al., 1990): Bacteria, Archaea, Eukarya — from ribosomal RNA",
  "Whittaker's 1969 five kingdoms: Monera, Protista, Plantae, Fungi, Animalia",
  "Fungi won their own kingdom: external digestion + absorption, not photosynthesis",
  "Archaea look like bacteria but are genetically closer to eukaryotes",
  "'Protista' is a paraphyletic grab-bag being reorganized into natural supergroups",
  "Domain assignment uses 16S/18S ribosomal RNA — present in every cell, slow-evolving",
 ],
 "requirements": [
  "A diagram of the three-domain tree with the major eukaryotic supergroups",
  "Understanding of ribosomal RNA as a universal molecular marker",
  "Comparison chart: five kingdoms vs three domains",
 ],
 "standards": [
  "Domain definitions per Woese, Kandler & Wheelis (1990)",
  "Kingdom circumscriptions per current phylogenetic consensus",
 ],
 "citations": [CIT_WOESE, CIT_WHITTAKER],
 "sig_lens": (
  "Signature reading: the deepest branches show that looks deceive — "
  "Archaea wear bacterial bodies over eukaryotic code. Manon's Signature "
  "take: never classify by surface; the three-domain revolution is the "
  "proof that the hidden layer (the molecule) outranks the visible layer "
  "(the shape)."),
 "demo_kind": "kingdom_map",
},
{
 "key": "type-specimens", "name": "Type Specimens: The Physical Anchor of a Name",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A type specimen is the physical specimen that permanently anchors a "
  "scientific name — the ultimate reference that says 'this name means this "
  "organism.' When a taxonomist describes a new species, they designate a "
  "holotype (the single name-bearing specimen) plus paratypes (additional "
  "specimens cited in the description). If the original author named no "
  "holotype, a later worker may designate a lectotype from the original "
  "material; if all original material is lost, a neotype can be designated "
  "as replacement. Genera have type species and families have type genera, "
  "so the anchoring runs up the whole hierarchy. Types live in museum "
  "collections, curated for centuries, because any future dispute about "
  "what a name means is settled by examining the type — not by arguing "
  "about the description's words. DNA is now routinely sequenced from "
  "century-old types, letting modern phylogenies plug directly into "
  "historical names."),
 "how_it_works": (
  "Type designation happens at publication: the describing author states "
  "'holotype' and gives the museum and catalog number where it is "
  "deposited, which fixes the name to that physical object forever. Later "
  "taxonomists who suspect two names denote one species compare the types "
  "side by side (or their DNA); if the types match, the names are "
  "synonyms. When no holotype was designated, the code allows a lectotype "
  "to be chosen from the syntype series, and when everything is lost, a "
  "neotype restores the anchor — each step documented in print so the "
  "chain of custody is public. Museums treat types as their crown jewels: "
  "separate storage, restricted loans, and increasingly, high-resolution "
  "imaging and DNA barcodes published online. A name without a traceable "
  "type is a weak name, vulnerable to reinterpretation."),
 "key_points": [
  "Holotype: the single name-bearing specimen designated at description",
  "Paratypes: additional cited specimens; lectotype: later-chosen from original material",
  "Neotype: replacement designated when all original material is lost",
  "Genera have type species; families have type genera — anchoring runs up the hierarchy",
  "Name disputes are settled by examining types, not by debating description text",
  "Types are museum crown jewels: imaged, barcoded, and curated for centuries",
 ],
 "requirements": [
  "A museum catalog showing how type specimens are labeled and stored",
  "Understanding of holotype/paratype/lectotype/neotype distinctions",
  "One published species description showing the type designation paragraph",
 ],
 "standards": [
  "Type designation rules per ICZN Articles 72-75 (animals) and ICNafp Articles 7-10",
  "Type deposition in a recognized public collection",
 ],
 "citations": [CIT_ICZN, CIT_ICNAFP],
 "sig_lens": (
  "Signature reading: the type is the ground truth object — every claim "
  "about a name resolves to one physical specimen. Manon's Signature take "
  "treats types as the original checksums of biology: when records "
  "conflict, hash back to the anchor, not to anyone's opinion."),
 "demo_kind": "type_registry",
},
{
 "key": "synonymy-priority", "name": "Synonymy and Priority: One Name to Rule Them",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Synonymy happens when two or more names turn out to denote the same "
  "taxon — usually because two workers described the same species "
  "independently, or a revision merged two species into one. The Principle "
  "of Priority resolves it: the oldest validly published name (the senior "
  "synonym) is the correct one, and younger names become junior synonyms. "
  "The domestic cat was described as Felis catus by Linnaeus in 1758 and "
  "later as Felis domestica by others; priority keeps Felis catus. "
  "Homonymy is the mirror problem — the same name accidentally given to "
  "two different taxa — and the younger homonym must be replaced. Priority "
  "is what keeps nomenclature stable across centuries of independent work: "
  "without it, every redescription would spawn a competing name and "
  "biology's vocabulary would fragment. The codes do allow rare exceptions, "
  "conserving a younger, widely used name over an obscure older one when "
  "strict priority would cause chaos."),
 "how_it_works": (
  "When synonymy is suspected, the taxonomist compares the type specimens "
  "of both names; if they represent the same taxon, the names are formally "
  "synonymized in a publication, with the older name declared senior. "
  "Priority is judged by publication date (and, for ties, page order), "
  "counting only names that satisfy the code's validity rules — a name in "
  "an unpublished manuscript or a suppressed work does not compete. "
  "Objective synonyms share the same type specimen (a pure renaming); "
  "subjective synonyms have different types that a taxonomist judges to be "
  "the same taxon (a matter of opinion, reversible by later workers). For "
  "homonyms, the junior name — published later — is permanently invalid "
  "and needs a replacement name. Databases track the full synonymy of "
  "every accepted name so old literature remains searchable under new "
  "names."),
 "key_points": [
  "Synonymy: two+ names, one taxon; priority gives the win to the oldest valid name",
  "Senior synonym = correct name; junior synonyms = retired but recorded",
  "Example: Felis catus Linnaeus, 1758 beats the younger Felis domestica",
  "Homonymy: one name accidentally used for two taxa — the younger must be replaced",
  "Objective synonyms share a type; subjective synonyms reflect a taxonomist's judgment",
  "Full synonymies are tracked so old literature stays searchable under current names",
 ],
 "requirements": [
  "Two synonymous names with publication dates to practice applying priority",
  "Understanding of senior/junior and objective/subjective synonym distinctions",
  "A synonymy list from a recent revision to see the format",
 ],
 "standards": [
  "Principle of Priority per ICZN Article 23 (animals) and ICNafp Principle III",
  "Conserved names handled per ICZN Article 81 / ICNafp conserved-name lists",
 ],
 "citations": [CIT_ICZN, CIT_ICNAFP],
 "sig_lens": (
  "Signature reading: priority is first-to-file for names — the oldest "
  "valid claim wins, forever. Manon's Signature take: timestamp everything; "
  "in nomenclature as in invention, the dated record beats the louder "
  "voice."),
 "demo_kind": "priority_rule",
},
{
 "key": "read-scientific-name", "name": "How to Read a Scientific Name",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A full scientific name is a small data packet: genus, epithet, author, "
  "and year — 'Panthera leo (Linnaeus, 1758)' tells you the lion's genus "
  "(Panthera), its species epithet (leo), who described it (Linnaeus), when "
  "(1758), and — via the parentheses — that Linnaeus originally placed it "
  "in a different genus (he called it Felis leo). Subspecies add a third "
  "name: Panthera leo leo. Botanical names work the same way but cite "
  "authors differently ('Quercus alba L.') and use 'ex' and 'in' for "
  "complex authorship chains. Abbreviations compress the packet: after "
  "first mention, 'P. leo'; 'sp.' means an unidentified species of the "
  "genus ('Panthera sp.'), 'spp.' several species, 'cf.' compares "
  "('Panthera cf. leo' = looks like a lion, not certain), and 'aff.' marks "
  "affinity to a species. Reading the packet correctly lets you extract "
  "genus, species, authority, date, and taxonomic history at a glance — "
  "the basic literacy of biodiversity."),
 "how_it_works": (
  "Parse left to right: the first capitalized word is the genus, the second "
  "lowercase word the epithet; anything after is the authority. Parentheses "
  "around the author signal a genus transfer since the original "
  "description; no parentheses mean the species still sits in its original "
  "genus. A comma separates author from year. For plants, the author "
  "follows similar logic with standard abbreviations ('L.' for Linnaeus), "
  "and 'ex' credits the publishing author when the describing author never "
  "validly published. Qualifiers modify certainty: 'cf.' (confer, compare) "
  "marks a tentative identification, 'aff.' (affinis) marks a close but "
  "distinct relative, and 'sp.' holds the place of an undetermined species. "
  "Cultivar and hybrid symbols ('x' for hybrids, single quotes for "
  "cultivars) extend the packet for domesticated and crossed organisms."),
 "key_points": [
  "Full packet: Genus + epithet + author + year — e.g., Panthera leo (Linnaeus, 1758)",
  "Parentheses around the author = the species was moved to a different genus since description",
  "Subspecies add a third name; botanical authors use standard abbreviations like 'L.'",
  "'sp.' = unidentified species, 'cf.' = compare with, 'aff.' = related to",
  "Genus abbreviates after first mention: P. leo",
  "Reading the packet yields genus, species, authority, date, and nomenclatural history",
 ],
 "requirements": [
  "Ten full scientific names with authors to practice parsing",
  "A list of standard author abbreviations",
  "Understanding of parentheses, cf., aff., sp., and hybrid symbols",
 ],
 "standards": [
  "Author citation per ICZN Articles 50-51 and ICNafp Articles 46-50",
  "Standard author abbreviations per IPNI (plants) and zoological convention",
 ],
 "citations": [CIT_ICZN, CIT_ICNAFP],
 "sig_lens": (
  "Signature reading: a scientific name is a compressed file — unpack it "
  "and you get identity, history, and custody in one line. Manon's "
  "Signature take: learn to read the packet cold; every database record "
  "in the system is just this packet, expanded."),
 "demo_kind": "name_parser",
},
{
 "key": "monographs-floras", "name": "Monographs, Floras, and Faunas: The Reference Shelf",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "A monograph is the definitive scholarly treatment of a taxonomic group — "
  "every known species described, keyed, illustrated, mapped, and placed in "
  "a classification, often the life's work of its author. Floras do the "
  "same for the plants of a region, faunas for its animals. These works are "
  "taxonomy's infrastructure: field biologists identify specimens with "
  "their keys, conservationists take species lists from their checklists, "
  "and later revisers start from their synonymies. Great monographs run to "
  "hundreds of pages per group — the 'Flora of North America' spans dozens "
  "of volumes — and each species account follows a strict template: "
  "accepted name, synonymy, description, distribution, habitat, specimens "
  "examined, and notes. Because a monograph synthesizes all prior "
  "literature on its group, publishing one instantly becomes the baseline "
  "everyone cites, and revising one is how taxonomy advances group by "
  "group."),
 "how_it_works": (
  "Writing a monograph means examining every relevant specimen in the "
  "world's museums, reading every prior description, resolving every "
  "synonym, and producing identification keys that actually work on real "
  "material. The author visits major collections, borrows types, measures "
  "series of specimens to capture variation, and maps every verified "
  "locality. Species accounts are written to a template so readers can "
  "compare any two species field by field. Keys are built as dichotomous "
  "decision trees tested against the specimens. Modern monographs add DNA "
  "barcodes, distribution models, and online specimen databases, and many "
  "are now born-digital so keys and maps stay current. A flora or fauna "
  "does the same work geographically: every species known from the region, "
  "whether native or introduced, keyed for the local user."),
 "key_points": [
  "Monograph: the definitive treatment of a taxonomic group — described, keyed, mapped, classified",
  "Floras cover a region's plants; faunas cover its animals",
  "Species accounts follow strict templates: name, synonymy, description, distribution, specimens",
  "Monographs synthesize all prior literature and become the cited baseline",
  "Keys are tested decision trees built from examined specimens",
  "Modern monographs add DNA barcodes, models, and living online databases",
 ],
 "requirements": [
  "One classic monograph or flora volume to study the account template",
  "Understanding of dichotomous keys before reading monographic keys",
  "Access to a major collection catalog for the 'specimens examined' concept",
 ],
 "standards": [
  "Species-account completeness per monographic convention (name, synonymy, description, distribution)",
  "Keys tested against voucher specimens, not compiled from literature alone",
 ],
 "citations": [CIT_SIMPSON, CIT_STD],
 "sig_lens": (
  "Signature reading: a monograph is a group fully conquered — nothing "
  "known left unsorted. Manon's Signature take treats monographs as the "
  "gold standard of completeness: when his system claims a subject "
  "covered, it should mean monograph-covered."),
 "demo_kind": "monograph_scale",
},
{
 "key": "natural-history-museums", "name": "Natural History Museums: The Archives of Life",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Natural history museums are the physical archives of taxonomy, holding "
  "hundreds of millions of specimens — the Natural History Museum in "
  "London curates around 80 million, the Smithsonian's National Museum of "
  "Natural History more than 140 million. Each specimen is a time-stamped, "
  "place-stamped data point: what lived where, when. Type specimens live "
  "here, and every revision, redescription, and DNA study starts with "
  "museum drawers. Mass digitization is turning these archives into global "
  "databases — imaged, georeferenced, and DNA-barcoded — so a researcher "
  "anywhere can examine a type without travel. Museums also run the field "
  "expeditions that fill the gaps: most new species are discovered not in "
  "remote jungles alone but in museum drawers, where unidentified backlog "
  "material waits for an expert eye. Without collections, taxonomy would "
  "have no evidence locker and no memory."),
 "how_it_works": (
  "Museums work as permanent, citable repositories: collectors deposit "
  "voucher specimens with locality, date, and habitat data; curators "
  "catalog, preserve (pinned, in ethanol, frozen tissue), and loan them to "
  "researchers worldwide. Taxonomists revising a group request loans of "
  "all relevant material, including types, and return determinations — "
  "updated identifications — that improve the collection. Digitization "
  "pipelines photograph drawers, transcribe labels, and publish records "
  "to aggregators, multiplying each specimen's reach. Tissue collections "
  "stored ultra-cold feed DNA barcoding and phylogenomics, linking "
  "century-old names to modern trees. Field programs target under-sampled "
  "regions and taxa, and every expedition's specimens become the raw "
  "material of future monographs."),
 "key_points": [
  "Museums hold hundreds of millions of specimens — time-stamped, place-stamped data points",
  "Type specimens and revision material live here; every redescription starts in the drawers",
  "Digitization (images, georeferences, barcodes) makes types globally examinable",
  "Many 'new' species are found in backlog drawers, not in the field",
  "Voucher specimens make identifications checkable and science repeatable",
  "Tissue banks link historical names to modern DNA phylogenies",
 ],
 "requirements": [
  "A visit (physical or virtual) to a major collection's database",
  "Understanding of voucher specimens and catalog numbers",
  "Knowledge of preservation methods: pinned, fluid, frozen tissue",
 ],
 "standards": [
  "Type deposition in recognized public collections per the codes",
  "Digitization metadata per Darwin Core and institutional best practice",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: museums are cold storage for the tree of life — the "
  "evidence locker behind every name. Manon's Signature take: his "
  "databases should work like a great museum — every record a voucher, "
  "every claim traceable to a specimen."),
 "demo_kind": "museum_growth",
},
{
 "key": "common-vs-scientific", "name": "Common Names vs Scientific Names",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Common names are the everyday words people use for organisms — robin, "
  "oak, shark — and they are wonderfully human and completely unreliable. "
  "One species can carry dozens of common names across languages and "
  "regions (Puma concolor is puma, cougar, mountain lion, panther, and "
  "catamount), while one common name can denote many species ('robin' "
  "means a thrush in Europe, a different thrush in North America, and "
  "unrelated flycatchers in Australia). Common names change with fashion, "
  "carry no authority, and cannot be looked up unambiguously. Scientific "
  "names exist precisely to fix this: one species, one name, worldwide, "
  "stable across languages and centuries. Taxonomists still record common "
  "names — they matter for conservation outreach, legislation, and public "
  "databases — but every serious record keys on the scientific name, with "
  "common names attached as searchable aliases, never as identifiers."),
 "how_it_works": (
  "In practice, databases store the scientific name as the primary key and "
  "attach common names as secondary labels, often many-to-one in both "
  "directions. Legislation and trade lists cite scientific names to avoid "
  "ambiguity, then add familiar common names for readability. When a "
  "species is split by taxonomic revision, its common name may follow one "
  "daughter species or need new coinages — another reason the scientific "
  "name leads. Standardized common-name lists (for birds, fishes, and "
  "some plant groups) assign one official English name per species, which "
  "helps the public while the binomial does the precise work. Field guides "
  "index both, but the index entry that never lies is the Latin one."),
 "key_points": [
  "One species, many common names: Puma concolor has 40+ English names alone",
  "One common name, many species: 'robin' denotes unrelated birds on three continents",
  "Scientific names are the unambiguous primary key; common names are aliases",
  "Laws, trade lists, and databases cite the binomial to avoid ambiguity",
  "Splits and revisions break common names; the binomial absorbs the change",
  "Standardized lists give one official common name per species where they exist",
 ],
 "requirements": [
  "Examples of one-to-many and many-to-one common/scientific mappings",
  "A database showing scientific name as primary key with common-name aliases",
  "Awareness that common names vary by language, region, and era",
 ],
 "standards": [
  "Scientific names per the nomenclature codes; common names per standardized lists where available",
  "Database records keyed on scientific name, never on common name alone",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: common names are nicknames; the binomial is the "
  "legal name. Manon's Signature take: in any system he builds, the "
  "machine-readable identifier leads and the human nickname follows — "
  "never the reverse."),
 "demo_kind": "common_name_map",
},
# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "phylogenetics-intro", "name": "Phylogenetics: Trees from Data",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Phylogenetics reconstructs the evolutionary tree of life from data — "
  "inferring who is related to whom, and in what branching order, from "
  "the characters organisms carry. Darwin sketched the first evolutionary "
  "tree in 'On the Origin of Species' (1859); modern phylogenetics turns "
  "that sketch into a testable hypothesis built from DNA sequences, "
  "anatomy, or both. A phylogenetic tree's branches represent lineages, "
  "its nodes represent common ancestors, and its branching order — the "
  "topology — is the claim being tested. Trees are how taxonomy stopped "
  "being a filing cabinet and became a science of history: every "
  "classification today is expected to reflect a phylogenetic tree, "
  "grouping only organisms that share a common ancestor exclusive to "
  "them. Phylogenies power everything from tracing pandemics to dating "
  "the origin of flowers, and they are the backbone that modern "
  "classifications hang on."),
 "how_it_works": (
  "A phylogenetic analysis starts with a character matrix — taxa as rows, "
  "characters (DNA positions, anatomical traits) as columns — then "
  "searches among possible trees for the one that best explains the "
  "data under an optimality criterion: fewest evolutionary changes "
  "(parsimony), highest probability of the data (likelihood), or highest "
  "posterior probability (Bayesian inference). Because the number of "
  "possible trees explodes with taxa, heuristic searches sample tree "
  "space rather than exhausting it. Support values — bootstrap "
  "percentages, posterior probabilities — report how strongly the data "
  "back each branch. The resulting tree is then translated into "
  "classification: each named group should correspond to a clade, a "
  "complete branch of the tree. When a traditional group turns out not "
  "to be a clade, taxonomy revises it — the tree is the arbiter."),
 "key_points": [
  "Phylogenetics infers evolutionary trees from character data (DNA, anatomy, or both)",
  "Branches = lineages, nodes = common ancestors, topology = the testable claim",
  "Optimality criteria: parsimony (fewest changes), likelihood, Bayesian inference",
  "Support values (bootstrap, posterior probability) measure branch confidence",
  "Modern classifications must reflect trees: every named group should be a clade",
  "Trees arbitrate taxonomy: non-clade groups get revised to match the phylogeny",
 ],
 "requirements": [
  "A character matrix (taxa x characters) to see the raw input",
  "Understanding of nodes, branches, clades, and rooted vs unrooted trees",
  "Tree-viewing literacy: reading branching order off a diagram",
 ],
 "standards": [
  "Trees reported with support values and the inference method named",
  "Alignments and trees deposited in public repositories (e.g., TreeBASE conventions)",
 ],
 "citations": [CIT_DARWIN, CIT_HENNIG, CIT_FELSENSTEIN],
 "sig_lens": (
  "Signature reading: a phylogeny is a history recovered from evidence — "
  "the past reconstructed, branch by branch. Manon's Signature take: "
  "this is forensic science at planetary scale; learn to read a tree and "
  "you can read the biography of any lineage."),
 "demo_kind": "newick_tree",
},
{
 "key": "cladistics", "name": "Cladistics: Shared Derived Characters",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Cladistics, founded by Willi Hennig (1950, in English 1966), is the "
  "method of grouping organisms strictly by shared derived characters — "
  "synapomorphies. A derived character is an evolutionary novelty "
  "inherited from a common ancestor: feathers unite birds, hair unites "
  "mammals, flowers unite angiosperms. Crucially, only shared *derived* "
  "traits count as evidence of relationship; shared *primitive* traits "
  "(symplesiomorphies) — like having five toes, retained from ancient "
  "tetrapods — group organisms by what they have not changed, which "
  "misleads. Hennig's rule rebuilt taxonomy on a single principle: "
  "classify by recency of common ancestry, and let only novelties reveal "
  "it. Every modern phylogenetic method is cladistic at heart, because "
  "every tree is a hypothesis about which shared traits are homologies "
  "inherited from common ancestors versus convergences evolved "
  "independently."),
 "how_it_works": (
  "A cladistic analysis codes each character's states as ancestral (0) or "
  "derived (1) using an outgroup — a close relative outside the study "
  "group — to polarize the characters: the outgroup's state is taken as "
  "ancestral. Taxa sharing derived states are hypothesized to form a "
  "clade, and the tree requiring the fewest independent origins of those "
  "states (the most parsimonious tree) is preferred. Conflicts — "
  "characters that disagree — are resolved by congruence: the tree "
  "supported by the most characters wins, and conflicting characters are "
  "interpreted as homoplasy (convergence or reversal). The result is a "
  "cladogram: a branching diagram where each node is defined by the "
  "synapomorphies its descendants share. Taxonomy then names the clades, "
  "turning the tree into a classification."),
 "key_points": [
  "Hennig (1966): group only by shared derived characters (synapomorphies)",
  "Shared primitive traits (symplesiomorphies) mislead — they reflect no recent ancestry",
  "Outgroups polarize characters: outgroup state = ancestral",
  "Most parsimonious tree = fewest independent origins of derived states",
  "Conflicting characters are resolved by congruence; losers are homoplasy",
  "Each clade node is defined by the synapomorphies uniting its members",
 ],
 "requirements": [
  "A small character matrix with an outgroup to practice polarization",
  "Understanding of homology vs homoplasy",
  "Ability to map character changes onto a candidate tree",
 ],
 "standards": [
  "Character coding documented per Hennig's auxiliary principle (assume homology first)",
  "Outgroup selection justified as the sister group of the ingroup",
 ],
 "citations": [CIT_HENNIG, CIT_SIMPSON],
 "sig_lens": (
  "Signature reading: cladistics is signal-vs-noise discipline — only "
  "novelties count as evidence. Manon's Signature take: apply Hennig's "
  "rule to everything — in data as in anatomy, shared *new* traits reveal "
  "true kinship; shared *old* traits reveal nothing."),
 "demo_kind": "character_matrix",
},
{
 "key": "mono-para-poly", "name": "Monophyly, Paraphyly, Polyphyly: The Three Kinds of Groups",
 "group": "Compounded", "ladder_rank": 4, "ladder_tier": "compounded",
 "description": (
  "Every taxonomic group is one of three things. A monophyletic group "
  "(clade) contains a common ancestor and *all* of its descendants — "
  "mammals, birds, angiosperms. A paraphyletic group contains a common "
  "ancestor but *not all* descendants — 'reptiles' excluding birds, or "
  "'protists' excluding the kingdoms that evolved from them. A "
  "polyphyletic group contains organisms from different branches without "
  "their common ancestor — 'flying animals' (birds + bats + insects), or "
  "the old 'worms'. Modern taxonomy accepts only monophyletic groups as "
  "formal taxa, because only clades correspond to real branches of "
  "evolutionary history. Paraphyletic leftovers are the classic sign of a "
  "classification built on primitive traits or grades of organization, "
  "and phylogenetics keeps finding them: each one triggers a revision "
  "that either expands the group to include the missing descendants or "
  "splits it into clades."),
 "how_it_works": (
  "To classify a group, take the phylogenetic tree, mark the group's "
  "members, and find their most recent common ancestor. If every "
  "descendant of that ancestor is in the group, it is monophyletic. If "
  "some descendants are excluded — usually the most derived ones, like "
  "birds excluded from 'reptiles' — it is paraphyletic. If the members' "
  "common ancestor is not in the group at all (their lineages converge "
  "from separate branches), it is polyphyletic. Taxonomists test every "
  "traditional group this way against molecular trees; paraphyletic "
  "groups are either completed (birds folded into reptiles as Dinosauria "
  "sensu lato, or 'reptiles' abandoned for clade names) or dismantled "
  "into monophyletic pieces. Polyphyletic groups are always dismantled — "
  "they reflect convergence, not kinship."),
 "key_points": [
  "Monophyletic (clade): ancestor + ALL descendants — the only valid formal taxon",
  "Paraphyletic: ancestor + some descendants — e.g., 'reptiles' excluding birds",
  "Polyphyletic: members from separate branches — e.g., 'flying animals', 'worms'",
  "Test: mark members on the tree, find their most recent common ancestor, check completeness",
  "Paraphyletic groups get completed or split; polyphyletic groups get dismantled",
  "Phylogenetics keeps exposing paraphyletic leftovers built on primitive traits",
 ],
 "requirements": [
  "A phylogenetic tree and three candidate groups to classify",
  "Understanding of most-recent-common-ancestor logic",
  "Examples of famous revisions: birds-in-reptiles, fungi-out-of-plants",
 ],
 "standards": [
  "Only monophyletic groups recognized as formal taxa in phylogenetic classification",
  "Group tests documented against an explicit published tree",
 ],
 "citations": [CIT_HENNIG, CIT_STD],
 "sig_lens": (
  "Signature reading: monophyly is the completeness test — a real group "
  "leaves no descendant behind. Manon's Signature take: audit any "
  "category this way; paraphyletic buckets are where the interesting "
  "members got excluded, and polyphyletic ones are where convergence "
  "fooled the filer."),
 "demo_kind": "clade_classifier",
},
{
 "key": "morphology-systematics", "name": "Morphology-Based Systematics: Reading Bodies",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "For two centuries morphology — the form and structure of organisms — "
  "was taxonomy's only evidence, and it remains indispensable. "
  "Morphological systematics compares anatomy across taxa: skull shapes, "
  "leaf venation, genitalia (often the most species-diagnostic structures "
  "in insects), pollen sculpture, and bone proportions. The core skill is "
  "distinguishing homology (similarity from common ancestry, like a bat's "
  "wing and a human's hand) from analogy (similarity from convergence, "
  "like a bat's wing and an insect's wing). Measurements become "
  "morphometric data — ratios and landmark coordinates analyzed "
  "statistically — letting taxonomists separate cryptic lookalikes and "
  "quantify variation within species. Fossils can only be placed by "
  "morphology, so paleontology keeps the discipline central, and every "
  "species description still requires a morphological diagnosis no matter "
  "how much DNA is sequenced."),
 "how_it_works": (
  "The morphologist dissects, clears, stains, and images specimens, then "
  "codes discrete characters (present/absent, counts, shapes) and measures "
  "continuous ones (lengths, angles, landmark positions). Homology is "
  "assessed by position, development, and detailed similarity — a feather "
  "is a feather by its follicle development, not just its look. "
  "Morphometric analyses (principal components, discriminant functions) "
  "find the measurement combinations that separate species. Characters "
  "feed the same phylogenetic machinery as DNA, and morphology-only trees "
  "still anchor fossil placements. In descriptions, the diagnosis distills "
  "morphology to the minimum trait set that distinguishes the new species "
  "from its closest relatives — the part of the paper other taxonomists "
  "actually use with specimens in hand."),
 "key_points": [
  "Morphology was taxonomy's sole evidence for 200 years and remains required in every description",
  "Core skill: homology (common ancestry) vs analogy (convergence)",
  "Genitalia, pollen, and bone proportions are often the most diagnostic structures",
  "Morphometrics turns measurements into statistical species separation",
  "Fossils can only be classified by morphology — paleontology depends on it",
  "The diagnosis distills morphology to the minimum distinguishing trait set",
 ],
 "requirements": [
  "Dissection and microscopy basics for the study group",
  "Understanding of homology criteria: position, development, detail",
  "Basic statistics for morphometric comparisons",
 ],
 "standards": [
  "Character homology assessed by Remane's criteria (position, special quality, continuity)",
  "Measurements reported with sample sizes and ranges, not single values",
 ],
 "citations": [CIT_SIMPSON, CIT_STD],
 "sig_lens": (
  "Signature reading: morphology is reading the hardware — the body as "
  "engineered evidence. Manon's Signature take: never skip the physical "
  "inspection; DNA tells you the code version, but only the body shows "
  "what the machine does."),
 "demo_kind": "morpho_distance",
},
{
 "key": "molecular-systematics", "name": "Molecular Systematics: DNA Tells the Tree",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Molecular systematics reconstructs relationships from DNA and protein "
  "sequences, and it has rewritten the tree of life. Because DNA accumulates "
  "mutations roughly clocklike in many genes, the number of differences "
  "between two species' sequences measures their divergence: closely "
  "related species differ at few positions, distant ones at many. "
  "Standard marker genes serve different depths — fast-evolving "
  "mitochondrial COI separates close species, slow ribosomal genes resolve "
  "deep branches. The molecular revolution exposed spectacular errors in "
  "morphology-based trees: falcons turned out closer to parrots than to "
  "hawks, whales nested inside hoofed mammals next to hippos, and fungi "
  "left the plants for their own kingdom. DNA also works where morphology "
  "cannot — from fragmentary tissue, museum skins, and environmental "
  "samples — making it the great verifier and corrector of classification."),
 "how_it_works": (
  "The workflow: extract DNA, amplify target genes with PCR (or sequence "
  "whole genomes), align the sequences so homologous positions line up, "
  "then infer the tree. Raw difference counts (p-distances) give a first "
  "approximation, but models of sequence evolution correct for multiple "
  "hits at the same position — transitions vs transversions, rate "
  "variation among sites — before tree inference. Gene choice matches the "
  "question's depth: mitochondrial genes for species and populations, "
  "nuclear ribosomal genes for deep phyla, hundreds of loci for "
  "phylogenomics. Congruence between independent genes builds confidence; "
  "conflict flags hybridization, incomplete lineage sorting, or bad "
  "alignments. The tree then tests the classification: traditional groups "
  "that are not clades get revised, and the molecules usually win."),
 "key_points": [
  "Sequence differences measure divergence: fewer differences = closer relationship",
  "Marker genes match the question depth: COI for species, ribosomal genes for deep branches",
  "Molecular trees corrected famous errors: falcons with parrots, whales with hippos",
  "Evolution models correct raw distances for multiple hits and rate variation",
  "DNA works from fragments, museum skins, and environmental samples",
  "Congruent genes build confidence; conflicting genes flag hybridization or sorting artifacts",
 ],
 "requirements": [
  "Understanding of DNA sequence alignment and homology of positions",
  "Basic genetics: transitions, transversions, mitochondrial vs nuclear inheritance",
  "A sequence alignment to practice distance calculation",
 ],
 "standards": [
  "Sequences deposited in public archives with voucher links",
  "Alignment and model choice documented and reproducible",
 ],
 "citations": [CIT_FELSENSTEIN, CIT_SAITOU, CIT_HEBERT],
 "sig_lens": (
  "Signature reading: DNA is the source code diff — line-by-line proof of "
  "who forked from whom. Manon's Signature take: when the body and the "
  "code disagree, trust the code's testimony but verify with the body's "
  "behavior; the wins came from letting molecules audit anatomy."),
 "demo_kind": "sequence_distance",
},
{
 "key": "dna-barcoding", "name": "DNA Barcoding: A Scanner for Species",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "DNA barcoding identifies species from a short standardized gene region "
  "— for animals, a 648-base-pair stretch of the mitochondrial COI gene — "
  "the way a supermarket scanner reads a UPC. Proposed by Paul Hebert "
  "and colleagues in 2003, the method works because individuals of one "
  "species differ at only a few barcode positions while different species "
  "differ at many: the 'barcode gap' between within-species and "
  "between-species variation. A sequence from an unknown specimen — a "
  "larva, a fragment, a stomach content, a customs seizure — is compared "
  "against the BOLD (Barcode of Life Data System) reference library, and "
  "the closest match names it. Plants use rbcL + matK, fungi the ITS "
  "region, each kingdom with its own standard. Barcoding has exposed "
  "rampant cryptic species, policed food fraud and illegal wildlife "
  "trade, and let non-specialists identify specimens that once required "
  "a world expert."),
 "how_it_works": (
  "The barcode pipeline: extract DNA from tissue (even degraded or "
  "processed material), PCR-amplify the standard region with universal "
  "primers, sequence it, and query the reference library. Identification "
  "is by sequence similarity — typically a 97-99% match threshold for "
  "animals — backed by a neighbor-joining tree showing where the query "
  "lands among references. Building the library is the real work: "
  "expert-identified voucher specimens, each with a photo, locality, and "
  "museum deposition, sequenced to create trustworthy references. The "
  "barcode gap is validated per group: if within-species variation "
  "overlaps between-species divergence, the barcode fails for that group "
  "and more genes are needed. Quality control flags pseudogenes "
  "(NUMTs), contamination, and misidentified vouchers that would poison "
  "the library."),
 "key_points": [
  "Animal barcode: ~648 bp of mitochondrial COI (Hebert et al., 2003); plants rbcL+matK; fungi ITS",
  "The barcode gap: within-species variation << between-species divergence",
  "BOLD reference library: vouchered, expert-identified, imaged, georeferenced",
  "Identifies larvae, fragments, gut contents, and trade seizures non-specialists cannot",
  "Exposes cryptic species and polices food fraud and wildlife trafficking",
  "Fails where the gap closes — then more genes are required",
 ],
 "requirements": [
  "A barcode sequence and access to the BOLD identification engine concept",
  "Understanding of PCR, universal primers, and sequence similarity thresholds",
  "Knowledge of voucher discipline: no reference without a specimen",
 ],
 "standards": [
  "Barcode regions per kingdom standard (COI / rbcL+matK / ITS)",
  "Reference records carry voucher specimen, image, and locality data",
 ],
 "citations": [CIT_HEBERT],
 "sig_lens": (
  "Signature reading: barcoding is a universal product scanner for life — "
  "one read, one ID. Manon's Signature take: standardize the read, "
  "voucher the reference, and identification becomes infrastructure "
  "instead of expertise."),
 "demo_kind": "barcode_gap",
},
{
 "key": "nomenclature-codes", "name": "The Nomenclature Codes: ICZN, ICNafp, ICNP",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Biological nomenclature runs on legal codes, one per kingdom-group. "
  "The ICZN (International Code of Zoological Nomenclature, 4th ed. 1999) "
  "governs animals from 1 January 1758; the ICNafp (algae, fungi, plants; "
  "Shenzhen Code 2018) governs plants and allies from 1 May 1753; the "
  "ICNP governs prokaryotes; and the ICTV code governs viruses (which "
  "adopted binomial species names in 2021). Each code defines what counts "
  "as valid publication, how names are formed, how priority resolves "
  "conflicts, and how types anchor names — independently, so the same "
  "genus name can legally exist in zoology and botany at once (a "
  "hemihomonym). The codes are maintained by international commissions "
  "and congresses, amended by vote, and interpreted through published "
  "Opinions on hard cases. They are deliberately conservative: stability "
  "of names matters more than perfection, because millions of records, "
  "laws, and databases key on them."),
 "how_it_works": (
  "A name becomes available under a code only when published in a way the "
  "code recognizes: printed or registered electronic publication, with a "
  "description or diagnosis, explicit type designation, and (since the "
  "ICZN's 2012 amendment) ZooBank registration for electronic-only works. "
  "Each code sets formation rules — Latinized, correctly suffixed ranks "
  "(-idae for animal families, -aceae for plant families), no tautonyms "
  "in botany (repeating the genus name is banned; zoology allows them). "
  "Priority, homonymy, and synonymy rules then referee conflicts, with "
  "commissions empowered to conserve widely used names against obscure "
  "seniors via plenary power. Hemihomonyms across codes are legal but "
  "tracked to avoid confusion. Taxonomists cite the code edition and "
  "article numbers in nomenclatural acts so every decision is auditable."),
 "key_points": [
  "ICZN (animals, from 1758), ICNafp (algae/fungi/plants, from 1753), ICNP (prokaryotes), ICTV (viruses)",
  "Each code independently defines valid publication, formation, priority, and types",
  "Hemihomonyms: the same genus name can legally exist under two codes",
  "Electronic publication requires ZooBank registration (ICZN amendment 2012)",
  "Commissions conserve widely used names against obscure seniors to protect stability",
  "Stability outranks perfection: millions of records key on these names",
 ],
 "requirements": [
  "The relevant code's key articles (publication, priority, types, homonymy)",
  "Understanding of starting dates: 1753 for most plants, 1758 for animals",
  "Familiarity with ZooBank registration for electronic works",
 ],
 "standards": [
  "Nomenclatural acts cite code edition and article numbers",
  "New names registered in ZooBank / IPNI / approved prokaryotic lists as applicable",
 ],
 "citations": [CIT_ICZN, CIT_ICNAFP],
 "sig_lens": (
  "Signature reading: the codes are the constitution of biological "
  "naming — independent jurisdictions, amendable, stability-first. "
  "Manon's Signature take: good governance for names looks like good "
  "governance for anything — written rules, public registry, appeal "
  "process, and a bias toward not breaking what works."),
 "demo_kind": "code_rules",
},
{
 "key": "taxonomic-revisions", "name": "Taxonomic Revisions: Splits, Lumps, and Moves",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A taxonomic revision re-examines a whole group with new evidence and "
  "rebuilds its classification: splitting one species into several, lumping "
  "several into one, or moving species between genera. Splits happen when "
  "cryptic diversity surfaces — DNA or song or ecology showing that one "
  "'species' is really three. Lumps happen when supposed differences "
  "collapse into variation within one interbreeding population. Moves "
  "happen when phylogenies relocate a species to its true genus. Revisions "
  "are taxonomy's engine of progress and its public-relations problem: "
  "every split or lump renames organisms in field guides, laws, and "
  "databases, which is why the codes favor stability and demand published "
  "evidence. A good revision examines all types, samples across the whole "
  "range, uses multiple lines of evidence, and leaves a synonymy trail so "
  "every old name maps to its new home."),
 "how_it_works": (
  "The reviser gathers every name ever applied to the group, locates and "
  "examines the type specimens, samples populations across the full "
  "geographic and ecological range, and analyzes morphology plus DNA. "
  "Species limits are tested against an explicit species concept: do the "
  "populations interbreed, do they form distinct genetic clusters, do "
  "diagnostic characters hold? Splits require demonstrating discontinuity "
  "— gaps in variation, reciprocal monophyly, or reproductive isolation — "
  "not just finding differences. Lumps require showing the 'differences' "
  "are clinal or individual variation. The revision publishes new "
  "circumscriptions, full synonymies mapping old names to new taxa, "
  "redesigned keys, and updated distributions. Databases then propagate "
  "the changes, retiring old combinations into synonymy lists."),
 "key_points": [
  "Splits: one species becomes several (cryptic diversity revealed)",
  "Lumps: several names collapse into one interbreeding population",
  "Moves: phylogenies relocate species to their true genera",
  "Splits need demonstrated discontinuity, not just detected difference",
  "Every revision publishes full synonymies mapping old names to new taxa",
  "Revisions advance taxonomy but rename organisms in guides, laws, and databases",
 ],
 "requirements": [
  "All type specimens and prior literature for the group",
  "Range-wide sampling: morphology + DNA across the full distribution",
  "An explicit species concept stated before testing limits",
 ],
 "standards": [
  "Revisions examine types, sample range-wide, and use multiple evidence lines",
  "New combinations published with basionym citations per the codes",
 ],
 "citations": [CIT_MAYR, CIT_CRACRAFT],
 "sig_lens": (
  "Signature reading: revision is refactoring the classification — split "
  "what merged wrongly, merge what split wrongly, move what filed "
  "wrongly. Manon's Signature take: never fear the refactor when the "
  "evidence demands it, but always ship the migration map (the "
  "synonymy) with it."),
 "demo_kind": "revision_tracker",
},
{
 "key": "species-concepts", "name": "Species Concepts: What Counts as a Species",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "'Species' is the most argued word in biology, because several "
  "definitions compete. The Biological Species Concept (Mayr, 1942): "
  "groups of actually or potentially interbreeding populations, "
  "reproductively isolated from others — powerful for sexual animals, "
  "useless for asexuals and fossils. The Morphological Species Concept: "
  "groups distinguished by consistent physical differences — practical "
  "everywhere, fooled by cryptic species. The Phylogenetic Species "
  "Concept (Cracraft, 1983): the smallest diagnosable monophyletic "
  "group — precise and DNA-friendly, but it splits aggressively. The "
  "Evolutionary Species Concept (Simpson, 1961): a lineage evolving "
  "separately with its own trajectory. De Queiroz's general lineage "
  "concept unifies them: all concepts are just different criteria for "
  "detecting separately evolving lineages. In practice taxonomists use "
  "integrative judgment — and the choice of concept measurably changes "
  "how many species get recognized."),
 "how_it_works": (
  "Applying a concept means running its test. BSC: do the populations "
  "interbreed where they meet, or do hybrids fail? (hybrid zones, "
  "breeding experiments, gene flow estimates). MSC: are there consistent, "
  "non-overlapping diagnostic differences? (morphometrics, character "
  "gaps). PSC: do the populations form exclusive, diagnosable genetic "
  "clusters? (reciprocal monophyly, fixed DNA differences). ESC: does the "
  "fossil or living lineage show its own evolutionary trajectory through "
  "time? Taxonomists increasingly require agreement across concepts — "
  "morphology, molecules, ecology, geography — before splitting, which "
  "is integrative taxonomy in action. The concept must be stated in the "
  "paper, because readers cannot evaluate a split without knowing the "
  "rules used."),
 "key_points": [
  "Biological (Mayr 1942): interbreeding populations, reproductively isolated",
  "Morphological: consistent diagnosable physical differences",
  "Phylogenetic (Cracraft 1983): smallest diagnosable monophyletic group",
  "Evolutionary (Simpson 1961): a lineage with its own trajectory",
  "General lineage concept: all definitions detect separately evolving lineages",
  "The chosen concept changes the species count — it must be stated explicitly",
 ],
 "requirements": [
  "Population samples across contact zones for interbreeding tests",
  "Genetic clustering analysis for phylogenetic concept tests",
  "Explicit statement of the applied concept in every taxonomic decision",
 ],
 "standards": [
  "Species hypotheses tested against a named, published species concept",
  "Integrative decisions cite morphology, molecules, ecology, and geography",
 ],
 "citations": [CIT_MAYR, CIT_CRACRAFT, CIT_SIMPSON],
 "sig_lens": (
  "Signature reading: a species concept is a decision rule — same data, "
  "different rule, different count. Manon's Signature take: always name "
  "your decision rule before deciding; hidden rules are how counts get "
  "gamed."),
 "demo_kind": "species_concept_decider",
},
{
 "key": "dichotomous-keys", "name": "Dichotomous Keys: Identification by Decision Tree",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "A dichotomous key identifies an unknown organism as a series of "
  "either-or choices: '1a. Wings present -> go to 2; 1b. Wings absent -> "
  "go to 17.' Each answer eliminates half the possibilities until one "
  "species remains. Good keys use characters visible on real specimens "
  "(not requiring dissection or DNA), ordered from obvious to subtle, "
  "with each couplet's alternatives mutually exclusive. Keys are "
  "taxonomy's user interface — the tool that turns classification into "
  "identification for field biologists, students, customs officers, and "
  "pest controllers. Digital keys now add photos at every couplet, allow "
  "skipping unknown characters (multi-access keys), and run on phones in "
  "the field. But a key is only as good as its testing: untested keys "
  "strand users at couplets their specimen does not match, which is why "
  "monograph keys are validated against series of real specimens."),
 "how_it_works": (
  "Using a key: start at couplet 1, compare your specimen against both "
  "alternatives, choose the match, and follow its pointer to the next "
  "couplet; repeat until a taxon name appears, then verify against the "
  "description and illustrations. Building a key: list the taxa, tabulate "
  "their characters, then recursively split the set with the most "
  "reliable distinguishing character, writing couplets where each lead "
  "describes a real state. Test the draft key against identified "
  "specimens including juveniles, damaged individuals, and geographic "
  "variants — the cases that break naive keys. Multi-access (matrix) keys "
  "let users enter any characters they can observe and compute the "
  "shortlist, tolerating missing data. Every key states its coverage "
  "(which taxa, which region, which life stages) so users know its "
  "limits."),
 "key_points": [
  "Dichotomous key: a chain of either-or couplets narrowing to one taxon",
  "Good couplets use visible characters, mutually exclusive alternatives, obvious-to-subtle order",
  "Keys are taxonomy's user interface: classification turned into identification",
  "Digital multi-access keys tolerate missing data and add photos per couplet",
  "Keys must be tested against real specimens including juveniles and variants",
  "Every key states its coverage limits: taxa, region, life stages",
 ],
 "requirements": [
  "A specimen (or detailed photos) and a key covering its group and region",
  "Patience to verify the endpoint against the full description",
  "Understanding that ambiguous couplets mean backing up, not forcing ahead",
 ],
 "standards": [
  "Keys validated against voucher specimens across the covered variation",
  "Coverage, authorship, and date stated on every published key",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: a key is a decision tree compiled from expertise — "
  "expert judgment, executable by anyone. Manon's Signature take: this "
  "is the pattern for all his systems — compress mastery into a "
  "branching procedure a beginner can run."),
 "demo_kind": "dichotomous_key",
},
{
 "key": "biodiversity-informatics", "name": "Biodiversity Informatics: GBIF, Darwin Core, and the Data Layer",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Biodiversity informatics is the data infrastructure of taxonomy: the "
  "standards and aggregators that make hundreds of millions of specimen "
  "and observation records interoperable. The Global Biodiversity "
  "Information Facility (GBIF) aggregates billions of occurrence records "
  "— what was found where, when — from museums, surveys, and citizen "
  "science into one searchable index. Darwin Core, maintained by TDWG, "
  "is the shared vocabulary: standard field names like scientificName, "
  "eventDate, decimalLatitude, and basisOfRecord so a record from any "
  "museum parses in any database. The Catalogue of Life assembles an "
  "authoritative species checklist; the Encyclopedia of Life gathers a "
  "page per species. This layer turned taxonomy from scattered cabinets "
  "into queryable big data: distribution models, extinction-risk "
  "assessments, and invasion tracking all run on it. Its garbage-in "
  "problem is misidentifications, which is why records link back to "
  "vouchers and identifications carry the identifier's name."),
 "how_it_works": (
  "Publishers map their collection databases to Darwin Core terms and "
  "push standardized records to aggregators, which index, deduplicate, "
  "and serve them through APIs and portals. Each record carries the "
  "scientific name plus the identification history (who identified it, "
  "when, with what references), the voucher or evidence (specimen "
  "catalog number, photo, DNA barcode), and event metadata (date, "
  "coordinates, uncertainty). Quality pipelines flag impossible "
  "coordinates, swapped lat/long, and names missing from taxonomic "
  "backbones. Researchers query by taxon, place, and time to build "
  "distribution maps, model ranges under climate change, and detect "
  "population trends. Annotations flow back: a taxonomist's redetermination "
  "updates the record at the source, propagating corrections network-wide."),
 "key_points": [
  "GBIF aggregates billions of occurrence records into one searchable index",
  "Darwin Core (TDWG) is the shared vocabulary: scientificName, eventDate, coordinates, basisOfRecord",
  "Catalogue of Life = authoritative checklist; Encyclopedia of Life = a page per species",
  "Records link to vouchers and name the identifier — the defense against misidentification",
  "Quality pipelines flag bad coordinates and names missing from taxonomic backbones",
  "Corrections propagate: redeterminations update records at the source",
 ],
 "requirements": [
  "A Darwin Core field reference for mapping collection data",
  "Understanding of occurrence vs checklist vs taxonomic data",
  "Awareness of coordinate uncertainty and identification confidence",
 ],
 "standards": [
  "Records published in Darwin Core with required identification and event fields",
  "Taxonomic backbone alignment so names resolve to accepted taxa",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: biodiversity informatics is taxonomy's API layer — "
  "every specimen queryable, every name resolvable. Manon's Signature "
  "take: data that cannot be queried might as well not exist; the "
  "standard vocabulary (Darwin Core) is what turns cabinets into a "
  "network."),
 "demo_kind": "dwc_validator",
},
{
 "key": "reading-trees", "name": "Reading Phylogenetic Trees: Nodes, Branches, and Roots",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Reading a phylogenetic tree correctly is a core taxonomic literacy, "
  "and most misreadings are predictable. The branching order (topology) "
  "is the information; the left-right order of tips is meaningless — "
  "rotating a node changes nothing. Branch lengths may represent genetic "
  "change or time (phylograms and chronograms) or may carry no meaning "
  "at all (cladograms) — the legend says which. The root marks the "
  "common ancestor of everything shown; unrooted trees display "
  "relationships without direction. The most recent common ancestor of "
  "any two tips is found by tracing both down to their meeting node, "
  "and the path length between them (patristic distance) measures their "
  "divergence. A polytomy — one node splitting into three or more "
  "branches — means the data could not resolve the order, not that "
  "three lineages appeared at once. Internal nodes are hypotheses, tips "
  "are data: never read a living species as the ancestor of another "
  "living species."),
 "how_it_works": (
  "To read a tree: locate the root (or note the tree is unrooted), then "
  "read nested clades — each node defines the clade of everything above "
  "it. Sister groups are the two clades sharing a node; they are each "
  "other's closest relatives regardless of how different they look. "
  "Trace any pair of tips to their common node to find their MRCA; sum "
  "the branch lengths along the path for their patristic distance. Check "
  "the scale bar and legend before interpreting branch lengths, and check "
  "support values before trusting a node — low-support nodes may collapse "
  "into polytomies. Rotate nodes mentally to test whether two drawings "
  "show the same tree: if the nested sets match, they do. When comparing "
  "a classification to a tree, verify each named group corresponds to "
  "exactly one node — that is the monophyly check."),
 "key_points": [
  "Topology is the information; tip order is meaningless — nodes rotate freely",
  "Branch lengths mean change or time only if the legend says so (phylogram/chronogram vs cladogram)",
  "Root = common ancestor of all shown; unrooted trees have no direction",
  "MRCA of two tips: trace both down to their meeting node",
  "Polytomy = unresolved order, not simultaneous splitting",
  "Never read a living tip as another living tip's ancestor",
 ],
 "requirements": [
  "Practice trees with labeled nodes, branch lengths, and support values",
  "Ability to rotate nodes mentally and recognize identical topologies",
  "Understanding of rooted vs unrooted representations",
 ],
 "standards": [
  "Published trees state rooting method, branch-length meaning, and support measures",
  "Node support reported (bootstrap/posterior) before taxonomic conclusions",
 ],
 "citations": [CIT_HENNIG, CIT_FELSENSTEIN],
 "sig_lens": (
  "Signature reading: a tree diagram is a nested-set machine — learn the "
  "three misreadings (tip order, branch meaning, ancestor confusion) and "
  "you will read trees cleaner than most graduates. Manon's Signature "
  "take: master the diagram type and every phylogeny in the system "
  "becomes legible."),
 "demo_kind": "patristic_distance",
},
{
 "key": "inference-methods", "name": "Tree Inference: Parsimony, Likelihood, and Bayesian Methods",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Three optimality criteria dominate tree inference. Maximum parsimony "
  "chooses the tree requiring the fewest evolutionary changes — "
  "Occam's razor formalized, counting steps character by character. "
  "Maximum likelihood (Felsenstein, 1981) chooses the tree maximizing "
  "the probability of the observed data under an explicit model of "
  "sequence evolution. Bayesian inference (e.g., MrBayes, 2003) samples "
  "trees in proportion to their posterior probability, reporting the "
  "probability that each clade is true given data, model, and priors. "
  "Parsimony is fast and model-free but vulnerable to long-branch "
  "attraction, where fast-evolving lineages falsely group together. "
  "Likelihood and Bayesian methods model the evolutionary process "
  "— rate variation, base frequencies — and generally outperform "
  "parsimony on molecular data, at the cost of computation. In practice, "
  "taxonomists run model-based analyses and report parsimony as a "
  "cross-check; congruence across methods is the strongest signal the "
  "tree is right."),
 "how_it_works": (
  "The analyst aligns sequences, selects a substitution model (often via "
  "model-testing software comparing fit), then searches tree space: "
  "heuristic rearrangements (nearest-neighbor interchange, subtree "
  "pruning-regrafting) for parsimony and likelihood, Markov chain Monte "
  "Carlo sampling for Bayesian analysis. Likelihood computes, for each "
  "candidate tree, the probability of the alignment given the tree and "
  "model, optimizing branch lengths; the best tree wins. Bayesian MCMC "
  "walks through tree space visiting trees proportionally to their "
  "posterior probability, and clade frequencies in the sampled trees "
  "become posterior probabilities. Support is assessed by bootstrapping "
  "(resampling characters) for parsimony/likelihood. Long-branch "
  "attraction is diagnosed by adding taxa to break long branches or "
  "switching to better-fitting models."),
 "key_points": [
  "Parsimony: fewest changes wins — fast, model-free, prone to long-branch attraction",
  "Maximum likelihood (Felsenstein 1981): highest data-probability tree under an evolution model",
  "Bayesian: posterior probabilities via MCMC sampling of tree space",
  "Long-branch attraction: fast lineages falsely group; broken by denser taxon sampling",
  "Model choice (substitution model, rate variation) measurably changes results",
  "Congruence across methods is the strongest signal a tree is correct",
 ],
 "requirements": [
  "An alignment and tree software (conceptual understanding suffices for the demo)",
  "Understanding of substitution models and rate heterogeneity",
  "Knowledge of bootstrap vs posterior probability interpretation",
 ],
 "standards": [
  "Model selection documented; alignment and trees archived reproducibly",
  "Support values reported for every taxonomically consequential node",
 ],
 "citations": [CIT_FELSENSTEIN, CIT_SAITOU],
 "sig_lens": (
  "Signature reading: three engines, one question — which history best "
  "explains the data. Manon's Signature take: never trust a single "
  "method's answer on consequential branches; run the parsimony "
  "cross-check and demand congruence before renaming anything."),
 "demo_kind": "parsimony_score",
},
# ------------------------------------------------------------------ ADVANCED
{
 "key": "phylogenomics", "name": "Phylogenomics: Trees from Hundreds of Genes",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Phylogenomics infers trees from genome-scale data — hundreds to "
  "thousands of genes instead of a handful — and it has resolved "
  "branches that single genes never could. Two strategies compete: "
  "concatenation (supermatrix), which glues all genes into one giant "
  "alignment, and coalescent methods, which infer each gene's tree and "
  "then reconcile them into a species tree. Concatenation is powerful "
  "but can be confidently wrong when genes genuinely disagree due to "
  "incomplete lineage sorting; coalescent methods model that "
  "disagreement explicitly. Phylogenomics settled deep controversies — "
  "the root of the animal tree, the radiation of flowering plants — while "
  "revealing that different parts of the genome can tell different "
  "stories through hybridization and introgression. The cost is "
  "computation and missing data: no species has every gene sequenced, "
  "so supermatrices are mostly gaps, and handling them honestly is part "
  "of the craft."),
 "how_it_works": (
  "The pipeline: sequence genomes or transcriptomes (or capture hundreds "
  "of target loci), identify orthologous genes across species, align each "
  "gene separately, filter badly aligned regions, then either concatenate "
  "into a supermatrix with partition-specific models or infer gene trees "
  "and feed them to a coalescent summary method. Missing data is "
  "quantified per taxon and per gene; rogue taxa that jump around the "
  "tree are tested by removal. Gene-tree conflict is visualized (not "
  "hidden) to distinguish incomplete lineage sorting from hybridization. "
  "The species tree updates classification at the deepest levels — "
  "orders, classes, phyla — where morphology ran out of characters. "
  "Results are only as good as orthology: paralogs mistaken for "
  "orthologs corrupt everything downstream."),
 "key_points": [
  "Genome-scale data: hundreds to thousands of genes vs a handful",
  "Concatenation (supermatrix) vs coalescent (gene trees reconciled) strategies",
  "Incomplete lineage sorting makes genes disagree; coalescent methods model it",
  "Resolved deep controversies: animal root, flowering-plant radiation",
  "Missing data is normal; rogue taxa and paralogs must be filtered",
  "Gene-tree conflict is visualized and interpreted, never hidden",
 ],
 "requirements": [
  "Genome or target-capture data and orthology inference",
  "Compute resources for partitioned model analysis",
  "Understanding of incomplete lineage sorting and gene-tree/species-tree discordance",
 ],
 "standards": [
  "Orthology, alignment filtering, and missing-data levels documented",
  "Gene-tree conflict reported alongside the species tree",
 ],
 "citations": [CIT_FELSENSTEIN, CIT_STD],
 "sig_lens": (
  "Signature reading: phylogenomics is the full-audit version of tree "
  "building — every gene gets a vote, disagreements get modeled. "
  "Manon's Signature take: when the stakes are deep branches, sample "
  "the whole genome and let the discordant genes speak; the truth is "
  "in the disagreement pattern."),
 "demo_kind": "concat_stats",
},
{
 "key": "molecular-clock", "name": "The Molecular Clock: Dating the Tree",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "The molecular clock (Zuckerkandl & Pauling, 1965) turns genetic "
  "distance into time: if mutations accumulate at a roughly steady "
  "rate, the number of differences between two lineages measures how "
  "long ago they diverged. Calibrated with fossils of known age — a "
  "fossil that must postdate a split sets a minimum age — the clock "
  "dates every node on the tree, producing a chronogram. Strict clocks "
  "assume one rate everywhere; relaxed clocks let rates vary across "
  "branches, which fits real data better since generation time, body "
  "size, and metabolism all bend the rate. Clock dating rewrote "
  "evolutionary timelines: it pushed the origin of modern birds past "
  "the dinosaur extinction debate, dated the flowering-plant radiation, "
  "and times pandemics to the month. The clock is only as good as its "
  "calibrations — misdated fossils or misapplied rates shift every "
  "estimate — so credible studies report uncertainty intervals, not "
  "single dates."),
 "how_it_works": (
  "Dating starts with a phylogeny with branch lengths in substitutions "
  "per site. Fossil calibrations are placed as priors on nodes: a fossil "
  "belonging to a clade sets a hard minimum age for that node, sometimes "
  "with a soft maximum from older fossil-free strata. A clock model "
  "(strict or relaxed, e.g., uncorrelated lognormal) converts branch "
  "lengths to time in a Bayesian framework, co-estimating the tree, "
  "rates, and dates. Multiple calibrations across the tree stabilize "
  "estimates; cross-validation drops each calibration in turn to test "
  "consistency. Results are reported as chronograms with credibility "
  "intervals on node ages. Sanity checks compare clock dates against "
  "independent fossils and biogeographic events (continental splits, "
  "island ages)."),
 "key_points": [
  "Genetic distance / rate = time since divergence (Zuckerkandl & Pauling, 1965)",
  "Fossils calibrate: a clade's fossil sets a hard minimum node age",
  "Strict clock: one rate; relaxed clock: rates vary by branch (fits reality better)",
  "Bayesian co-estimation yields chronograms with credibility intervals",
  "Multiple calibrations + cross-validation stabilize dates",
  "Report uncertainty intervals, never single-point dates",
 ],
 "requirements": [
  "A phylogeny with branch lengths and reliably identified fossil calibrations",
  "Understanding of strict vs relaxed clock models",
  "Bayesian dating literacy: priors, posteriors, credibility intervals",
 ],
 "standards": [
  "Calibrations justified with fossil specimen citations and phylogenetic placement",
  "Node ages reported with credibility intervals and the clock model named",
 ],
 "citations": [CIT_ZUCKERKANDL, CIT_FELSENSTEIN],
 "sig_lens": (
  "Signature reading: the clock converts difference into duration — "
  "mutations as a metronome. Manon's Signature take: calibrate against "
  "hard anchors (fossils), allow the rate to breathe (relaxed clock), "
  "and always quote the interval; false precision is the enemy."),
 "demo_kind": "molecular_clock",
},
{
 "key": "cryptic-species", "name": "Cryptic Species: Hidden Diversity in Plain Sight",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Cryptic species are distinct evolutionary lineages that look identical "
  "(or near-identical) to human eyes — one 'species' that DNA reveals as "
  "five. DNA barcoding keeps finding them: a widespread butterfly splits "
  "into ten genetic clusters, a 'single' frog into a complex of "
  "lookalikes, each with its own range, ecology, and conservation needs. "
  "Cryptic diversity matters enormously: a pest-control program targeting "
  "'one species' may face several with different resistances; a "
  "conservation plan protecting 'one frog' may let four unrecognized "
  "relatives go extinct. Discovery follows a pattern — barcode the "
  "widespread morphospecies, find deep genetic splits, then re-examine "
  "specimens for the subtle traits (genitalia, song, chemistry, ecology) "
  "that were overlooked. Integrative follow-up is mandatory: DNA alone "
  "flags candidates, but formal description still requires diagnosable "
  "differences and named types."),
 "how_it_works": (
  "Detection starts with dense geographic sampling of the morphospecies "
  "and barcode sequencing. Clustering analyses and barcode-gap statistics "
  "flag deep splits — divergences far exceeding within-population "
  "variation. Each candidate lineage is then tested integratively: "
  "morphometrics for subtle shape differences, bioacoustics for song "
  "divergence, ecological niche models for habitat separation, and "
  "nuclear genes to rule out mitochondrial artifacts (introgression, "
  "Wolbachia). Lineages passing multiple tests are formally described "
  "with diagnoses, types, and names; the old name stays with the "
  "population containing its type specimen. Databases update the "
  "one-to-many mapping so historical records can be re-attributed by "
  "locality where possible."),
 "key_points": [
  "Cryptic species: genetically distinct lineages, morphologically near-identical",
  "Barcoding keeps exposing them inside 'widespread' morphospecies",
  "Hidden diversity breaks pest control and conservation plans built on one name",
  "Discovery pattern: barcode broadly -> find deep splits -> re-examine for subtle traits",
  "Nuclear genes rule out mitochondrial artifacts before splitting",
  "Formal description still requires diagnoses, types, and names",
 ],
 "requirements": [
  "Dense range-wide sampling, not a few convenient specimens",
  "Barcode data plus at least one independent evidence line",
  "Type-specimen discipline: the old name follows its type's population",
 ],
 "standards": [
  "Candidate splits tested with nuclear loci and non-molecular evidence",
  "New descriptions include diagnoses distinguishing all daughter species",
 ],
 "citations": [CIT_HEBERT, CIT_CRACRAFT],
 "sig_lens": (
  "Signature reading: cryptic species are the system's hidden rows — "
  "same label, different entities. Manon's Signature take: never assume "
  "one label means one thing; barcode the inventory and let the deep "
  "splits declare themselves."),
 "demo_kind": "cryptic_split",
},
{
 "key": "splitting-conservation", "name": "Taxonomic Splits and Conservation: Counting What Counts",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Taxonomic decisions have direct conservation consequences. When one "
  "widespread species is split into several narrow endemics, each daughter "
  "species has a smaller range and population — and small-range species "
  "qualify as threatened far more easily. This 'taxonomic inflation' "
  "debate asks whether splits manufacture endangered species: critics "
  "note that phylogenetic species concepts can double recognized species "
  "counts, diluting conservation funding; supporters reply that the "
  "diversity was always there and ignoring it lets real lineages vanish "
  "unnamed. Red List assessments, protected-area laws, and trade bans "
  "all key on species names, so a revision can move organisms onto or "
  "off legal protection overnight. Responsible practice pairs splits "
  "with immediate conservation assessment of the daughters, so no newly "
  "recognized species waits years for its status to be evaluated."),
 "how_it_works": (
  "The mechanism is arithmetic plus criteria: IUCN Red List criteria "
  "weigh range size, population size, and decline rate. A parent species "
  "with a continental range assessed as Least Concern can yield daughters "
  "each confined to one mountain range — each now meeting Endangered "
  "thresholds on range alone. Conservation taxonomists therefore run "
  "the assessment pipeline in parallel with the revision: as daughters "
  "are delimited, their extent of occurrence, area of occupancy, and "
  "threats are compiled from the same specimens and localities. Legal "
  "lists are updated with explicit synonymy crosswalks so enforcement "
  "does not lose track of renamed taxa. Funding bodies increasingly "
  "require this coupling: no split published without the daughters' "
  "status assessed."),
 "key_points": [
  "Splits shrink ranges: daughters of a Least Concern parent can each be Endangered",
  "'Taxonomic inflation' debate: do splits manufacture endangered species or reveal them?",
  "Red List criteria (range, population, decline) interact directly with species limits",
  "Revisions can move organisms onto or off legal protection overnight",
  "Responsible splits ship with immediate conservation assessments of daughters",
  "Synonymy crosswalks keep enforcement tracking renamed taxa",
 ],
 "requirements": [
  "Range and population data for every daughter lineage at split time",
  "Understanding of IUCN Red List criteria thresholds",
  "Coordination with legal-list authorities before publication",
 ],
 "standards": [
  "Newly split species assessed against Red List criteria at publication",
  "Nomenclatural crosswalks supplied to legal and database authorities",
 ],
 "citations": [CIT_CRACRAFT, CIT_STD],
 "sig_lens": (
  "Signature reading: names are legal instruments — a split redraws the "
  "map of what the law protects. Manon's Signature take: wield the "
  "naming power responsibly; every split is also a conservation act, "
  "so assess the daughters before you publish."),
 "demo_kind": "split_conservation",
},
{
 "key": "integrative-taxonomy", "name": "Integrative Taxonomy: Many Lines of Evidence",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Integrative taxonomy delimits species using multiple independent lines "
  "of evidence — morphology, DNA, ecology, behavior, geography — instead "
  "of any single one. The logic is congruence: when genetics, anatomy, "
  "song, and habitat all draw the same boundary, the species hypothesis "
  "is strong; when they disagree, the disagreement itself is informative "
  "(recent divergence, hybridization, or plasticity). This approach tamed "
  "the excesses of single-evidence splitting: a barcode cluster with no "
  "morphological, ecological, or geographic distinction is a candidate, "
  "not a species. Modern revisions score each evidence line explicitly "
  "and require a threshold of agreement before naming. Integrative "
  "taxonomy is slower than barcode-only description, but its species "
  "survive re-testing — which is why it is now the expected standard "
  "for formal species delimitation."),
 "how_it_works": (
  "The workflow assembles parallel datasets for the same populations: "
  "morphometric measurements, one or more DNA loci (mitochondrial plus "
  "nuclear), ecological niche data, behavioral traits like song, and "
  "geographic distributions. Each line is analyzed independently — "
  "genetic clustering, morphological discriminant analysis, niche "
  "overlap tests — then the boundaries are compared. Full congruence "
  "justifies description; partial congruence triggers deeper sampling "
  "(maybe a hybrid zone explains the mismatch); single-line signals are "
  "held as hypotheses. The publication documents every line, weights "
  "them transparently, and states the decision rule in advance. "
  "Reproducibility requires archiving all datasets with the paper so "
  "later workers can re-run the integration."),
 "key_points": [
  "Multiple independent evidence lines: morphology, DNA, ecology, behavior, geography",
  "Congruence across lines = strong species hypothesis; disagreement = informative",
  "Single-evidence splits are candidates, not conclusions",
  "Each line analyzed independently, then boundaries compared",
  "Decision rule and evidence weights stated transparently in advance",
  "All datasets archived so the integration can be re-run",
 ],
 "requirements": [
  "Parallel datasets on the same populations across at least three evidence lines",
  "Independent analysis per line before comparing boundaries",
  "Pre-stated decision rule for what counts as sufficient agreement",
 ],
 "standards": [
  "Species descriptions cite morphology, molecules, ecology, and geography",
  "All underlying datasets deposited in public archives",
 ],
 "citations": [CIT_CRACRAFT, CIT_HEBERT],
 "sig_lens": (
  "Signature reading: integration is triangulation — one bearing can "
  "lie, three rarely do. Manon's Signature take: demand independent "
  "confirmation before promoting any candidate to a name; the system "
  "should make single-evidence claims visible as provisional."),
 "demo_kind": "integrative_score",
},
{
 "key": "zoobank-registration", "name": "ZooBank and Digital Registration: Names on the Record",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "ZooBank is the official online registry of zoological nomenclature: "
  "every new animal name published electronically must be registered "
  "there before publication (a requirement since the ICZN's 2012 "
  "amendment), receiving a permanent Life Science Identifier (LSID) — "
  "a globally unique, resolvable code like "
  "urn:lsid:zoobank.org:act:XXXX. Registration makes names machine-"
  "findable from birth: databases, journals, and aggregators harvest "
  "ZooBank records instead of scraping PDFs. Plants use the International "
  "Plant Names Index (IPNI) as their registry; prokaryotes have official "
  "notification lists. Registration closes the old loophole where names "
  "published in obscure outlets vanished from science — now the act of "
  "naming is itself a database transaction, timestamped and permanent. "
  "For taxonomists, the practical rule is simple: no registration, no "
  "name — an unregistered electronic name is nomenclaturally "
  "unavailable, as if never published."),
 "how_it_works": (
  "Before publishing a new animal name electronically, the author creates "
  "a ZooBank record with the name, authorship, publication details, and "
  "type information, and receives LSIDs for the publication and each "
  "nomenclatural act. The published work must cite the ZooBank "
  "registration (proving pre-publication registration) and be archived "
  "in a permanent digital repository. LSIDs resolve through standard "
  "services to the name's metadata, letting machines trace any name to "
  "its original act. IPNI works analogously for plants, assigning stable "
  "identifiers harvested by checklists worldwide. Registration data feeds "
  "directly into the Catalogue of Life and GBIF backbones, so a name "
  "registered today is searchable globally tomorrow — the latency "
  "between naming and indexing has collapsed from years to days."),
 "key_points": [
  "ZooBank: official registry of zoological names; registration mandatory for electronic publication (ICZN 2012 amendment)",
  "LSIDs: permanent, globally unique, resolvable identifiers for nomenclatural acts",
  "No registration = no name: unregistered electronic names are nomenclaturally unavailable",
  "IPNI serves plants; prokaryotes have official notification lists",
  "Registration feeds Catalogue of Life and GBIF — names become searchable in days",
  "The naming act is now a timestamped database transaction",
 ],
 "requirements": [
  "A ZooBank account and the publication's bibliographic details before submission",
  "LSIDs cited in the published work as proof of registration",
  "Archiving of the electronic work in a permanent repository",
 ],
 "standards": [
  "ICZN Article 8.5: electronic works registered in ZooBank prior to publication",
  "LSID format urn:lsid:zoobank.org:<type>:<uuid>",
 ],
 "citations": [CIT_ICZN],
 "sig_lens": (
  "Signature reading: registration turned naming into a ledger — every "
  "act timestamped, signed, and resolvable. Manon's Signature take: "
  "this is how his system should treat every record — registered at "
  "birth, permanently resolvable, never orphaned."),
 "demo_kind": "lsid_check",
},
{
 "key": "describing-new-species", "name": "Describing a New Species: Alpha Taxonomy in Practice",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Alpha taxonomy — the description of new species — is where taxonomy "
  "meets discovery, and it follows a strict ritual. The taxonomist "
  "confirms the organism is truly undescribed (checking types and "
  "literature, not just databases), assembles a series of specimens "
  "showing variation, and writes a description with five mandatory "
  "parts: a diagnosis (how it differs from relatives), a full "
  "description, designation of a holotype with its museum depository, "
  "etymology (the story of the name), and distribution plus ecology. "
  "The name itself must satisfy the code — Latinized, correctly formed, "
  "not a homonym — and electronic publication requires ZooBank "
  "registration. Peer review checks the novelty claim hardest: is this "
  "really new, or a variant, a hybrid, or a synonym resurrected by "
  "mistake? Thousands of species are still described yearly, each "
  "paper a small permanent addition to the catalog of life."),
 "how_it_works": (
  "The describer first rules out existing names by examining types of "
  "all similar described species — most 'new species' die at this step, "
  "revealed as synonyms. Surviving candidates get measured, photographed, "
  "DNA-barcoded, and compared against relatives character by character. "
  "The holotype is selected (the best adult specimen, ideally), its "
  "catalog number and museum recorded, paratypes designated. The "
  "manuscript's diagnosis is written as a differential — 'differs from "
  "X by ...' — because that is what future identifiers need. Etymology "
  "explains the epithet (morphology, locality, or an honoree). After "
  "peer review and registration, publication makes the name available; "
  "the author then notifies aggregators so the name enters global "
  "checklists. The specimens, not the paper, remain the ultimate "
  "evidence."),
 "key_points": [
  "Alpha taxonomy: the formal description of new species, still thousands per year",
  "Mandatory parts: diagnosis, description, holotype + depository, etymology, distribution/ecology",
  "Most candidates die at the synonymy check — types of similar species examined first",
  "The diagnosis is written differentially: 'differs from X by ...'",
  "Names must satisfy the code; electronic names need ZooBank registration",
  "The specimens remain the ultimate evidence, not the paper",
 ],
 "requirements": [
  "A specimen series showing the variation within the candidate species",
  "Access to types and literature of all similar described species",
  "A museum willing to accession the holotype permanently",
 ],
 "standards": [
  "Descriptions satisfy ICZN Articles 13/16 (animals) or ICNafp Articles 32-45",
  "Holotype deposited in a recognized public collection with catalog number cited",
 ],
 "citations": [CIT_ICZN, CIT_ICNAFP],
 "sig_lens": (
  "Signature reading: describing a species is minting a permanent record "
  "— diagnosis, anchor, provenance, story. Manon's Signature take: "
  "every record his system mints should meet this bar — distinguishable, "
  "anchored, sourced, and built to outlive its author."),
 "demo_kind": "description_checklist",
},
{
 "key": "taxonomic-impediment", "name": "The Taxonomic Impediment: Too Few Taxonomists, Too Many Species",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The taxonomic impediment is the global shortage of taxonomic expertise "
  "relative to the undescribed majority of life: millions of species "
  "await description while the number of working taxonomists shrinks, "
  "museum positions go unfilled, and university courses in systematics "
  "disappear. At roughly 15,000-20,000 new species described per year "
  "against millions undescribed, simple arithmetic says centuries of "
  "backlog — and extinction may erase species before they are ever "
  "named. The impediment bites hardest where diversity is highest: "
  "tropical insects, mites, nematodes, fungi, and marine invertebrates "
  "have few or no specialists. Responses include accelerated "
  "'turbo-taxonomy' (large multi-author papers describing hundreds of "
  "species with DNA + minimal morphology), DNA-based candidate "
  "flagging, parataxonomist training programs, and machine-vision "
  "identification — but none replace the expert revision that turns "
  "candidates into reliable names. The bottleneck is human judgment, "
  "and it is not scaling with the data."),
 "how_it_works": (
  "Backlog arithmetic drives the field: undescribed species divided by "
  "annual description rate equals centuries. Turbo-taxonomy attacks the "
  "rate side — teams barcode bulk samples, cluster sequences into "
  "candidate species, photograph and minimally diagnose each, and publish "
  "hundreds of descriptions in one paper with data archived for later "
  "revision. Capacity-building attacks the taxonomist side: training "
  "parataxonomists for sorting and imaging, funding early-career "
  "systematists, and digitizing types so one expert can work globally. "
  "Prioritization triages effort toward threatened habitats and "
  "economically critical groups (pests, disease vectors, pollinators). "
  "Funders increasingly demand that big biodiversity surveys budget "
  "taxonomy explicitly, because samples without names are data without "
  "addresses."),
 "key_points": [
  "Millions undescribed vs ~15,000-20,000 described per year = centuries of backlog",
  "Expertise is scarcest where diversity is highest: tropical insects, mites, fungi, marine invertebrates",
  "Extinction may erase species before description — the race against loss",
  "Turbo-taxonomy: bulk barcoding + minimal diagnoses, hundreds of species per paper",
  "Parataxonomists, digitized types, and targeted funding attack the capacity side",
  "Bottleneck is expert judgment — data scales faster than the humans who name it",
 ],
 "requirements": [
  "Backlog estimates for the target group to size the problem",
  "Funding and positions for taxonomic training, not just sequencing",
  "Digitized types so experts can work without travel",
 ],
 "standards": [
  "Description rates and backlog reported per major group for planning",
  "Survey budgets include explicit taxonomy line items",
 ],
 "citations": [CIT_MORA, CIT_STD],
 "sig_lens": (
  "Signature reading: the impediment is a throughput crisis — data "
  "arrives by the terabyte, names by the expert-hour. Manon's Signature "
  "take: engineer the pipeline (turbo-taxonomy, machine vision, "
  "parataxonomists) but never pretend the expert check is optional; "
  "throughput without judgment is just faster error."),
 "demo_kind": "impediment_math",
},
{
 "key": "machine-vision-id", "name": "Automated Identification: Machine Vision for Taxonomy",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Machine vision now identifies organisms from photos: convolutional "
  "neural networks trained on millions of expert-identified images "
  "suggest species for a new photo in seconds, the engine behind "
  "citizen-science identification apps. For well-photographed groups "
  "(birds, butterflies, flowering plants) top suggestions are right "
  "most of the time; for obscure taxa with few training images, "
  "accuracy collapses — the same long tail that haunts human "
  "expertise. Automated identification attacks the taxonomic impediment "
  "at the identification step (not the description step): sorting bulk "
  "samples, triaging citizen observations, and flagging likely novelties "
  "for experts. Its failure modes are instructive — confident errors on "
  "out-of-distribution images, bias toward common species — which is "
  "why serious deployments report confusion matrices and keep a human "
  "in the loop. The trajectory is clear: vision handles the routine "
  "identifications, freeing taxonomists for the revisions and "
  "descriptions only humans can do."),
 "how_it_works": (
  "A classifier is trained on vouchered, expert-identified images with "
  "clean taxonomic labels; the training set's label quality caps the "
  "model's accuracy — misidentified training photos teach errors. At "
  "inference, the model outputs ranked species suggestions with "
  "confidence scores; deployments set thresholds (high confidence = "
  "auto-accept for common species, low = route to experts). Performance "
  "is measured with confusion matrices: precision (of the photos called "
  "species X, how many were X) and recall (of the true X photos, how "
  "many were found). Active learning loops feed expert corrections back "
  "into training, steadily covering the long tail. For specimens rather "
  "than photos, robotic imaging + vision pipelines sort bulk trap "
  "samples into morphospecies bins for barcoding — the turbo-taxonomy "
  "front end."),
 "key_points": [
  "Neural networks trained on expert-identified images suggest species in seconds",
  "Best on well-photographed groups; collapses on long-tail taxa with few images",
  "Attacks identification (not description): sorting, triage, novelty flagging",
  "Label quality caps accuracy — misidentified training photos teach errors",
  "Confusion matrices (precision, recall) measure real performance; humans stay in the loop",
  "Vision handles routine IDs; taxonomists keep revisions and descriptions",
 ],
 "requirements": [
  "Large, vouchered, expert-labeled image sets for training",
  "Confidence thresholds and expert-review routing for low-confidence calls",
  "Ongoing active-learning loops feeding corrections back to training",
 ],
 "standards": [
  "Performance reported as precision/recall per species, not just top-1 accuracy",
  "Training labels traceable to voucher specimens or expert identifications",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: machine vision is the apprentice identifier — "
  "fast on the common, humble on the rare. Manon's Signature take: "
  "deploy it as triage with measured precision, never as authority; "
  "the expert remains the final key."),
 "demo_kind": "classifier_metrics",
},
{
 "key": "edna-metagenomics", "name": "eDNA and Metagenomics: Taxonomy Without Specimens",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Environmental DNA (eDNA) detects organisms from the DNA they shed "
  "into water, soil, or air — no specimen required. Filter a liter of "
  "stream water, sequence the barcodes in it, and the species list "
  "emerges: fish upstream, amphibians on the banks, mammals that drank "
  "there. Metabarcoding amplifies standard barcode regions from the "
  "whole mixture; metagenomics sequences everything and sorts it "
  "computationally. The method revolutionized surveys of elusive, rare, "
  "or dangerous taxa and powers early detection of invasive species "
  "and pathogens. Its statistics are detection statistics: a species "
  "present but missed is a false negative, governed by shedding rates, "
  "degradation, and sampling effort — occupancy models separate 'absent' "
  "from 'missed'. Reference-library gaps are the limit: eDNA can only "
  "name what barcoding has already described, so the taxonomic "
  "impediment echoes here too."),
 "how_it_works": (
  "Field teams collect water or soil with contamination controls "
  "(blanks at every step, because PCR amplifies contaminants as "
  "happily as targets), filter and extract DNA, then amplify barcode "
  "markers with broad primers or shotgun-sequence the extract. Reads "
  "are quality-filtered, clustered into operational taxonomic units or "
  "exact sequence variants, and matched against reference libraries; "
  "unmatched clusters are flagged as unknowns, not named. Detection "
  "probability is modeled per species per sample: with per-sample "
  "detection probability p, n samples give 1-(1-p)^n cumulative "
  "detection, which sizes survey effort. Positive detections of "
  "high-consequence species (invasives, pathogens) trigger confirmatory "
  "resampling before action. Quantitative interpretation stays cautious: "
  "read counts correlate loosely with biomass, not precisely."),
 "key_points": [
  "eDNA: species detected from shed DNA in water, soil, or air — no specimen needed",
  "Metabarcoding amplifies barcode regions from mixtures; metagenomics sequences everything",
  "Early detection of invasives, pathogens, and elusive rare species",
  "Occupancy models separate 'absent' from 'present but missed'",
  "Contamination controls are mandatory: PCR amplifies contaminants too",
  "Can only name what reference libraries contain — the impediment echoes",
 ],
 "requirements": [
  "Contamination-controlled sampling: blanks at collection, extraction, and PCR",
  "A curated reference barcode library for the target group and region",
  "Occupancy-model literacy for effort sizing and false-negative accounting",
 ],
 "standards": [
  "Negative controls sequenced and reported with every batch",
  "Detections below threshold confirmed by resampling before management action",
 ],
 "citations": [CIT_HEBERT, CIT_STD],
 "sig_lens": (
  "Signature reading: eDNA is presence-detection at a distance — the "
  "environment as a witness. Manon's Signature take: treat every "
  "detection as probabilistic, control contamination like a crime lab, "
  "and never let an unnamed read masquerade as an identified species."),
 "demo_kind": "edna_detection",
},
{
 "key": "phylocode", "name": "The PhyloCode: Naming Clades Instead of Ranks",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "The PhyloCode (International Code of Phylogenetic Nomenclature, "
  "first published 2020) is a parallel naming system that defines "
  "taxon names by ancestry instead of ranks. Rather than 'the family "
  "Felidae', a PhyloCode name is defined as a clade: node-based ('the "
  "least inclusive clade containing the lion and the house cat'), "
  "branch-based ('the most inclusive clade containing the lion but not "
  "the hyena'), or apomorphy-based ('the clade stemming from the first "
  "organism with retractable claws'). Because definitions reference "
  "specifier species and tree topology rather than rank endings, names "
  "survive re-rankings that would force renames under the traditional "
  "codes. The PhyloCode does not replace the ICZN/ICNafp — species "
  "names still follow those codes — it governs clade names above the "
  "species level for workers who want rank-free classification. Its "
  "registry, RegNum, records definitions permanently. Adoption remains "
  "limited but intellectually influential: it forced traditional "
  "taxonomy to confront what ranks are actually for."),
 "how_it_works": (
  "To establish a PhyloCode name, the author publishes a definition of "
  "one of the three types with specifier species (or specimens, or "
  "apomorphies), cites a reference phylogeny, and registers the name in "
  "RegNum. Node-based definitions capture crown clades; branch-based "
  "(stem-based) definitions capture total groups including extinct stem "
  "relatives; apomorphy-based definitions tie the name to the origin of "
  "a trait. Because the definition is topological, the name's content "
  "tracks the tree: if new phylogenies rearrange branches, the defined "
  "clade's membership updates automatically while the name stays "
  "fixed. Conversion of traditional names requires choosing specifiers "
  "carefully so the defined clade matches historical usage as closely "
  "as the tree allows."),
 "key_points": [
  "PhyloCode (2020): names defined by ancestry, not ranks",
  "Three definition types: node-based, branch-based (stem-based), apomorphy-based",
  "Definitions use specifier species + a reference phylogeny",
  "Names survive re-rankings: content tracks the tree, the name stays fixed",
  "Governs clade names; species names still follow ICZN/ICNafp",
  "RegNum registry records definitions permanently",
 ],
 "requirements": [
  "A well-supported reference phylogeny for the group",
  "Carefully chosen specifiers so the defined clade matches historical usage",
  "Understanding of crown vs total groups for stem-based definitions",
 ],
 "standards": [
  "Definitions published with specifiers, reference phylogeny, and RegNum registration",
  "Definition type stated explicitly (node/branch/apomorphy-based)",
 ],
 "citations": [CIT_STD],
 "sig_lens": (
  "Signature reading: the PhyloCode names the branch, not the shelf — "
  "definitions that survive rearrangement. Manon's Signature take: "
  "define things by what they *are* (ancestry) rather than where they "
  "sit (rank); content-addressed naming outlasts every reorganization."),
 "demo_kind": "phylocode_define",
},
{
 "key": "taxonomic-database-standards", "name": "Building Taxonomic Databases: Standards and Schemas",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "A taxonomic database is only as good as its schema: the field "
  "definitions, identifiers, and versioning that let names, specimens, "
  "and trees interoperate. Core design rules: every name record carries "
  "its nomenclatural status (accepted, synonym, homonym), its authority "
  "and year, its type information, and links to protologue and "
  "registration (ZooBank/LSID, IPNI); every occurrence record follows "
  "Darwin Core; every taxon concept is versioned, because revisions "
  "change circumscriptions and old identifications must remain "
  "interpretable. Persistent identifiers (LSIDs, DOIs, catalog numbers) "
  "replace fragile text matching. Synonymy tables map every historical "
  "name to its current accepted taxon so legacy literature stays "
  "searchable. Change logs record every split, lump, and move with "
  "citations, making the database's taxonomy reproducible. Done right, "
  "the database becomes infrastructure: checklists, field guides, laws, "
  "and other databases all consume its API — which is exactly what this "
  "database you are reading is built to be."),
 "how_it_works": (
  "Schema design starts from the entities: names, taxon concepts, "
  "specimens, occurrences, references, and trees, each with a primary "
  "key that is a persistent identifier, never a text string. Name "
  "records store the full nomenclatural packet (name, author, year, "
  "status, basionym, type, registration ID). Taxon concepts version "
  "circumscriptions ('Panthera leo sec. Smith 2020') so identifications "
  "cite the concept used, not just the name. Occurrence tables use "
  "Darwin Core terms verbatim for aggregator compatibility. A synonymy "
  "service resolves any historical name to the current accepted taxon. "
  "Every taxonomic change writes a dated, cited change-log entry; API "
  "consumers can diff versions. Validation runs on ingest: name "
  "formation rules, coordinate sanity, required fields, backbone "
  "alignment — rejecting or flagging bad records before they pollute "
  "the index."),
 "key_points": [
  "Schema entities: names, taxon concepts, specimens, occurrences, references, trees",
  "Persistent identifiers (LSID, DOI, catalog numbers) as primary keys — never bare text",
  "Taxon concepts versioned ('sec.' citations) so old identifications stay interpretable",
  "Darwin Core terms verbatim for occurrence interoperability",
  "Synonymy service maps every historical name to the current accepted taxon",
  "Change logs make the taxonomy reproducible; validation runs on ingest",
 ],
 "requirements": [
  "A data model separating names from taxon concepts (they change independently)",
  "Persistent identifier minting for every entity",
  "Ingest validation: formation rules, coordinates, required fields, backbone alignment",
 ],
 "standards": [
  "Darwin Core for occurrences; nomenclatural fields per the relevant code",
  "Versioned taxon concepts with dated, cited change logs",
 ],
 "citations": [CIT_ICZN, CIT_STD],
 "sig_lens": (
  "Signature reading: this record describes the machine you are reading "
  "it on — the schema discipline behind every database in the system. "
  "Manon's Signature take: build the schema once, to this standard, "
  "and every future database inherits names that resolve, concepts "
  "that version, and changes that audit."),
 "demo_kind": "schema_validate",
},
]
