#!/usr/bin/env python3
"""Histology field entries for JAH Databases (field #35, taxonomy order).

Verified 2026-10-17: NO database covers histology as a discipline.
Manifest search (2,370 databases): zero 'histol*' slugs/names. Whole-system
exact-title sweep over all 769 shard indexes (the 't' key): zero collisions
for all 34 planned titles. Near-neighbors confirmed different disciplines:
'anatomy' (gross anatomy), 'cell-biology' (cell biology as a field),
'cytology' (single-cell diagnostics), 'pathology' (disease mechanisms) -
none is the microscopic study of tissues with fixation, sectioning,
staining, microscopy, and organ/system histology. ZERO full-record
discipline coverage anywhere.

So this build creates two NEW databases, 34 ladder-ordered records each:

  histology                 - The Histology Database
                             (public-harvest: real, fact-checked
                             histology; standard references Ross &
                             Pawlina 'Histology: A Text and Atlas'
                             8th ed 2019; Mescher 'Junqueira's Basic
                             Histology' 16th ed 2021; Gartner & Hiatt
                             'Color Textbook of Histology'; Eroschenko
                             'diFiore's Atlas of Histology';
                             Young/O'Dowd/Woodford 'Wheater's Functional
                             Histology'; Kierszenbaum & Tres 'Histology
                             and Cell Biology'; Bancroft & Gamble
                             'Theory and Practice of Histological
                             Techniques'; Kiernan 'Histological and
                             Histochemical Methods')
  histology-signature       - The Histology Signature Database
                             (his original Signature interpretation of
                             histology as the microscopic reading of
                             the body; src signature, titles suffixed
                             " (Signature Edition)", never presented as
                             authentic public record)

34 records each, ordered by the teaching ladder (ladder_rank 1-10,
ladder_tier foundations/compounded/advanced); the shard index is written in
ladder order so pages present simple -> compounded -> complex.

Subtitle disambiguation (fields #13-34 pattern): specialty titles carry
teaching-focused subtitles rather than bare cards, e.g. "Epithelial
Tissue: Covering Surfaces and Forming Glands".

Numerical cores: all hand-computed 2026-10-17, machine-verified by the
demos (see build.py). Every demo prints its real computed values, asserts
tight bounds, and ends with the OK marker; the build machine-executes all
68 demos before commit.

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

SIG_TAIL = ("Signature original - his original Signature interpretation of "
            "histology as the microscopic reading of the body: tissues read "
            "as engineered systems, clearly labeled Signature-made and never "
            "presented as authentic public record.")

ENTRIES = [
{
"key": "what_is",
"name": "What Is Histology: The Microscopic Study of Tissues",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Histology is the study of the microscopic structure of tissues - the "
"level of organization between the cell and the organ. Where anatomy "
"describes what the eye can see and cytology examines single cells, "
"histology reads the architecture: how cells arrange into sheets, "
"cords, networks, and fibers, and how that arrangement produces "
"function. A liver lobule, a kidney nephron, the layered wall of an "
"artery - none of these can be understood from a single cell or from "
"gross dissection alone; they reveal themselves only in thin sections "
"under the microscope. The four basic tissue types - epithelial, "
"connective, muscle, and nervous - combine in every organ of the body, "
"so histology is the common language of anatomy, physiology, and "
"pathology. This record maps the whole discipline: its questions, its "
"tools, and the ladder of records that follows."),
"how_it_works": (
"A histology investigation follows a fixed chain. First, tissue is "
"collected and fixed so its structure survives death. Second, it is "
"embedded, sectioned thinner than a cell is wide (typically 5 "
"micrometers), and mounted on glass. Third, it is stained so that "
"different structures take different colors. Fourth, it is examined "
"under the microscope, from low power (the architecture of the organ) "
"to high power (the details of individual cells). Fifth, what is seen "
"is named with a controlled vocabulary - tissue type, cell type, "
"layer, orientation - and interpreted: normal structure, or disease. "
"The demo works the optical arithmetic that bounds the whole "
"discipline: the resolving power of the light microscope from the "
"Rayleigh criterion, and the useful magnification ceiling that keeps "
"empty magnification honest."),
"key_points": [
"Histology = the microscopic structure of tissues: the level between cell and organ.",
"Four basic tissue types - epithelial, connective, muscle, nervous - build every organ.",
"The chain is fixed: fix, embed, section, stain, examine, name, interpret.",
"Light microscopy resolves ~0.24 um (Rayleigh, 550 nm, NA 1.4); useful magnification tops out near 1000xNA.",
"Histology is the shared language of anatomy, physiology, and pathology.",
"Distinct from gross anatomy (whole organs) and cytology (single cells)."],
"requirements": [
"A tissue sample collected and fixed promptly to prevent autolysis.",
"A microtome section thin enough to transmit light (about 5 um for paraffin).",
"A stain that gives different tissue components different colors.",
"A light microscope with objectives from 4x to 100x and a 10x eyepiece."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas: With Correlated Cell and Molecular Biology. 8th ed. Wolters Kluwer; 2019 - the discipline's standard text.",
"Mescher AL. Junqueira's Basic Histology: Text and Atlas. 16th ed. McGraw-Hill; 2021 - compact standard reference."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas: With Correlated Cell and Molecular Biology. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology: Text and Atlas. 16th ed. McGraw-Hill; 2021.",
"Young B, O'Dowd G, Woodford P. Wheater's Functional Histology: A Text and Colour Atlas. 6th ed. Elsevier; 2013."],
"sig_lens": (
"Signature lens: read every tissue as an engineered system whose "
"blueprint is visible only at the right scale. The Signature reading "
"of histology asks what each structure is FOR before naming what it "
"is - function first, vocabulary second - and treats the stain as an "
"instrument that asks the tissue a question in color.")},
{
"key": "cells",
"name": "Cells and Cell Ultrastructure: Building Blocks of Tissues",
"group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
"description": (
"Every tissue is an arrangement of cells plus what the cells make "
"around themselves. The histologist reads cells by their parts: the "
"nucleus with its chromatin pattern (euchromatin for active genes, "
"heterochromatin for silent ones), the nucleolus where ribosomes are "
"built, and the cytoplasm with its organelles - mitochondria for "
"energy, rough endoplasmic reticulum for protein export, Golgi for "
"packaging, lysosomes for digestion, and the cytoskeleton of "
"microtubules, actin, and intermediate filaments that gives the cell "
"its shape and moves its cargo. Cell shape is a functional "
"announcement: squamous cells spread thin for diffusion, cuboidal "
"cells sit square for secretion, columnar cells stand tall for "
"absorption, and stellate cells reach through matrix. Surface to "
"volume ratio governs what a cell can exchange with its surroundings: "
"a 10-micrometer sphere has twice the exchange surface per unit "
"volume of a 20-micrometer sphere, which is why exchange tissues are "
"built from small or flattened cells."),
"how_it_works": (
"Reading a cell starts at the nucleus. Size, shape, chromatin texture, "
"and nucleolar prominence identify the cell type and its activity: a "
"plasma cell shows clock-face chromatin and a pale Golgi zone, a "
"fibroblast shows an oval euchromatic nucleus, a lymphocyte shows a "
"dense round nucleus with a thin cytoplasmic rim. The cytoplasm is "
"read next: basophilia (blue, from RNA-rich rough ER and free "
"ribosomes) marks protein factories; eosinophilia (pink, from "
"mitochondria and secretory granules) marks energy and export. The "
"demo computes the exchange arithmetic that constrains cell design: "
"surface-to-volume ratios of spherical cells at 10 and 20 micrometers, "
"and the cell count packed into one cubic centimeter of tissue at 10 "
"micrometers per cell."),
"key_points": [
"Read the nucleus first: chromatin pattern and nucleolus reveal cell type and activity.",
"Basophilic cytoplasm = RNA and protein synthesis; eosinophilic = mitochondria and secretion.",
"Cell shape announces function: squamous for diffusion, columnar for absorption, stellate for matrix.",
"A 10 um sphere has 0.6 um^-1 surface-to-volume; a 20 um sphere has 0.3 - small cells exchange faster.",
"One cubic centimeter of tissue at 10 um per cell holds about one billion cells.",
"Organelles are the cell's departments: ER, Golgi, mitochondria, lysosomes, cytoskeleton."],
"requirements": [
"A stained section thin enough to resolve individual cells (5 um or less).",
"Knowledge of nuclear features: chromatin, nucleolus, nuclear shape.",
"Knowledge of cytoplasmic staining: basophilia vs eosinophilia and what each means.",
"The exchange arithmetic: surface-to-volume ratio as a function of cell size."],
"standards": [
"Alberts B et al. Molecular Biology of the Cell. 6th ed. Garland Science; 2014 - cell ultrastructure authority.",
"Kierszenbaum AL, Tres LL. Histology and Cell Biology: An Introduction to Pathology. 5th ed. Elsevier; 2019."],
"citations": [
"Alberts B et al. Molecular Biology of the Cell. 6th ed. Garland Science; 2014.",
"Kierszenbaum AL, Tres LL. Histology and Cell Biology: An Introduction to Pathology. 5th ed. Elsevier; 2019.",
"Palade GE. A small particulate component of the cytoplasm. J Biophys Biochem Cytol. 1955;1:59-68."],
"sig_lens": (
"Signature lens: treat the cell as a factory whose floor plan is "
"drawn by its work. The Signature reading sizes every organelle "
"against its job - ribosomes where export happens, mitochondria "
"where energy is spent - and reads surface-to-volume ratio as the "
"budget line no cell design can cross.")},
{
"key": "four_tissues",
"name": "The Four Basic Tissue Types: A Map of the Microscopic Body",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"All the complexity of the body's microscopic anatomy reduces to four "
"basic tissue types, and every organ is a combination of them. "
"Epithelial tissue is sheets of tightly joined cells that cover "
"surfaces, line cavities, and form glands - the body's interface "
"with the world. Connective tissue is cells scattered in a matrix "
"they secrete - fibers and ground substance - binding, supporting, "
"and connecting everything; bone, blood, fat, cartilage, and tendon "
"are all connective tissues. Muscle tissue is cells specialized to "
"contract: skeletal for voluntary movement, cardiac for the heartbeat, "
"smooth for the slow squeeze of hollow organs. Nervous tissue is "
"neurons that carry electrical signals plus glial cells that support "
"them. Learn to recognize these four at a glance - cellularity, "
"matrix, fiber direction, nuclear shape - and every organ section "
"becomes readable, because every organ is just these four arranged "
"with intent."),
"how_it_works": (
"Identifying a tissue type is a decision tree on four questions. How "
"cellular is it - are cells touching, or separated by matrix? Is there "
"an extracellular matrix, and is it fibrous, fluid, or mineralized? "
"Are the cells elongated in one direction (muscle, nerve, tendon) or "
"polygonal in sheets (epithelium)? What do the nuclei look like - "
"round and central, flattened, peripheral, or multiple? Epithelium "
"answers: cells touching, no matrix, sheet arrangement, often a free "
"surface. Connective tissue answers: cells separated by abundant "
"matrix. Muscle answers: elongated cells full of contractile protein, "
"pink cytoplasm. Nervous tissue answers: large cell bodies with "
"processes plus small dark glial nuclei. The demo encodes the "
"epithelial branch of this tree as a classifier: layers times shape "
"plus the two special cases, and it resolves all eight classical "
"epithelial types while rejecting impossible combinations."),
"key_points": [
"Four types build everything: epithelial (coverings/glands), connective (matrix/support), muscle (contraction), nervous (signaling).",
"Cellularity is the first branch: touching cells = epithelium or muscle; separated cells = connective tissue.",
"Bone, blood, fat, cartilage, tendon are all connective tissues - matrix defines the family.",
"Nuclear shape and position confirm the call: central oval, peripheral flat, multiple, or tiny dark.",
"The epithelial classifier resolves 8 classical types from layers x shape plus pseudostratified and transitional.",
"Every organ section is these four arranged with intent - learn the four and the organs read themselves."],
"requirements": [
"Low-power orientation: find the free surface, the lumen, or the organ capsule first.",
"The four-question decision tree: cellularity, matrix, cell shape, nuclear features.",
"A reference set of the eight epithelial types for the classifier branch.",
"Stained sections at multiple magnifications (4x for architecture, 40x for cells)."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 4-7, the four tissue types.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 4-7."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Gartner LP, Hiatt JL. Color Textbook of Histology. 4th ed. Elsevier; 2017."],
"sig_lens": (
"Signature lens: treat the four tissues as four engineering "
"materials with distinct specifications. Epithelium is the "
"interface material, connective tissue the structural composite, "
"muscle the actuator, nervous tissue the wiring - and every organ "
"is an assembly drawing combining exactly these four parts.")},
{
"key": "epithelium",
"name": "Epithelial Tissue: Covering Surfaces and Forming Glands",
"group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
"description": (
"Epithelial tissue is the body's boundary material: continuous sheets "
"of cells with almost no matrix between them, sitting on a basement "
"membrane, with one face free to a surface or lumen. Covering and "
"lining epithelia are named by a two-word code - layers, then cell "
"shape. Simple (one layer) squamous lines blood vessels and air sacs "
"where diffusion must be fast; simple cuboidal lines kidney tubules "
"and small ducts; simple columnar with goblet cells lines the gut for "
"absorption; stratified squamous armors skin and esophagus against "
"abrasion; transitional (urothelium) stretches in the bladder. "
"Pseudostratified columnar, with cilia, sweeps the airways. Glandular "
"epithelium folds inward to make exocrine glands (with ducts: sweat, "
"salivary, pancreas) or loses its ducts to make endocrine glands "
"(ductless: thyroid, pituitary, adrenal), releasing hormones into "
"blood. Polarity is the epithelial signature: an apical face with "
"microvilli, cilia, or stereocilia; lateral faces with junctions; a "
"basal face anchored to the basement membrane."),
"how_it_works": (
"Classifying an epithelium means answering three questions in order: "
"how many layers (simple, stratified, pseudostratified), what cell "
"shape at the surface (squamous, cuboidal, columnar), and whether a "
"special case applies (transitional in urinary tract, ciliated "
"pseudostratified in airways). Glands are classified separately: "
"exocrine versus endocrine first, then for exocrine glands the duct "
"system (simple unbranched versus compound branched) crossed with the "
"secretory unit (tubular, acinar/alveolar, or tubuloacinar) - seven "
"classical combinations, each with textbook examples. Secretion mode "
"adds a third axis: merocrine (exocytosis, e.g. salivary), apocrine "
"(apical budding, e.g. mammary), holocrine (whole-cell, e.g. "
"sebaceous). The demo enumerates the gland-classification matrix "
"programmatically and verifies the seven classical exocrine "
"combinations with their examples."),
"key_points": [
"Epithelium = cell sheets on a basement membrane with a free surface; polarity is its signature.",
"Naming code: layers (simple/stratified/pseudostratified) + surface cell shape (squamous/cuboidal/columnar).",
"Eight classical types: simple squamous/cuboidal/columnar, stratified squamous/cuboidal/columnar, pseudostratified, transitional.",
"Exocrine glands: simple vs compound ducts x tubular/acinar/tubuloacinar units = 7 classical combinations.",
"Endocrine glands are ductless and release hormones into blood.",
"Secretion modes: merocrine (salivary), apocrine (mammary), holocrine (sebaceous)."],
"requirements": [
"A section cut perpendicular to the surface so layers are countable.",
"Identification of the basement membrane and the free (apical) surface.",
"The two-word naming code applied in order: layers first, then shape.",
"Gland classification: exocrine/endocrine, duct branching, secretory unit shape."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 5, epithelia and glands.",
"Eroschenko VP. diFiore's Atlas of Histology with Functional Correlations. 13th ed. Wolters Kluwer; 2017."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Eroschenko VP. diFiore's Atlas of Histology with Functional Correlations. 13th ed. Wolters Kluwer; 2017.",
"Farquhar MG, Palade GE. Junctional complexes in various epithelia. J Cell Biol. 1963;17:375-412."],
"sig_lens": (
"Signature lens: read epithelium as interface engineering. Every "
"epithelial choice - layers for armor, squamous for speed, cilia for "
"sweeping, glands for export - is a design answer to what crosses "
"the boundary and what must not.")},
{
"key": "connective",
"name": "Connective Tissue: Fibers, Cells, and Ground Substance",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Connective tissue is the body's structural composite: relatively few "
"cells scattered through an abundant extracellular matrix that the "
"cells themselves secrete. The matrix has two parts - fibers and "
"ground substance. Collagen fibers (type I in tendon, skin, bone) "
"resist pulling; elastic fibers (elastin) stretch and recoil in "
"arteries, lungs, and skin; reticular fibers (type III collagen) form "
"the delicate scaffolding of lymphoid organs and liver. Ground "
"substance is the hydrated gel of glycosaminoglycans and "
"proteoglycans that resists compression and bathes the cells. The "
"resident cells are fibroblasts (fiber factories), with macrophages, "
"mast cells, plasma cells, and adipocytes as regular tenants. "
"Connective tissue proper divides by fiber arrangement: loose "
"(areolar) under epithelia, dense irregular in dermis, dense regular "
"in tendon where collagen runs in parallel cables. Specialized "
"members of the family - cartilage, bone, blood, adipose - are "
"connective tissues whose matrix took a different path: rubbery, "
"mineralized, fluid, or fatty."),
"how_it_works": (
"Reading connective tissue means inventorying the matrix. First the "
"fibers: are they thick pink wavy cables (collagen), thin dark "
"branching threads needing special stain (elastic, reticular)? "
"Second the arrangement: random weave (dense irregular), parallel "
"cables (dense regular, tendon), or sparse in clear space (loose "
"areolar). Third the cells: spindle fibroblasts between fibers, "
"signet-ring adipocytes, or wandering immune cells. Special stains "
"settle close calls: Masson trichrome turns collagen blue-green, "
"Verhoeff stains elastin black, silver impregnation reveals "
"reticulin. The demo works the packing arithmetic of tendon: at 70 "
"percent area fraction of 100-nanometer collagen fibrils, one square "
"millimeter of tendon cross-section holds on the order of 89 million "
"fibrils - the quantitative reason tendon is a cable, not a sheet."),
"key_points": [
"Connective tissue = few cells in abundant self-made matrix: fibers + ground substance.",
"Collagen resists tension, elastin recoils, reticulin scaffolds delicate organs.",
"Dense regular (tendon) vs dense irregular (dermis) vs loose areolar - arrangement is the diagnosis.",
"Cells: fibroblasts make matrix; macrophages, mast cells, plasma cells, adipocytes reside in it.",
"Specialized connective tissues: cartilage (rubbery), bone (mineralized), blood (fluid), fat (lipid).",
"One mm2 of tendon at 70% fibril packing holds ~89 million 100-nm collagen fibrils."],
"requirements": [
"Fiber identification: collagen (pink, wavy), elastic (thin, dark, branching), reticular (silver-positive).",
"Arrangement reading: parallel vs woven vs sparse.",
"Cell census: fibroblast vs adipocyte vs immune residents.",
"A special stain (trichrome, Verhoeff, or silver) for close calls."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 6, connective tissue.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 5."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Stevens A, Lowe J. Human Histology. 4th ed. Mosby Elsevier; 2015."],
"sig_lens": (
"Signature lens: read connective tissue as composite materials "
"science. Collagen is the tension cable, elastin the spring, ground "
"substance the hydraulic gel - and every arrangement from tendon to "
"dermis is a layup schedule optimized for the loads it carries.")},
{
"key": "muscle",
"name": "Muscle Tissue: Skeletal, Cardiac, and Smooth",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Muscle tissue converts chemical energy into mechanical pull, and its "
"three types are unmistakable once learned. Skeletal muscle is long "
"cylindrical multinucleated fibers with peripheral nuclei and bold "
"cross-striations - voluntary, powerful, fast to fatigue. Cardiac "
"muscle is branching uninucleate (sometimes binucleate) cells joined "
"end to end by intercalated discs, with central nuclei and fainter "
"striations - involuntary, rhythmic, fatigue-proof. Smooth muscle is "
"spindle-shaped uninucleate cells with no striations, arranged in "
"sheets around hollow organs - involuntary, slow, sustained. The "
"striations of skeletal and cardiac muscle are sarcomeres: Z disc to "
"Z disc, about 2.2 micrometers at rest, sliding actin past myosin to "
"shorten toward 1.6 micrometers in contraction. Because sarcomeres "
"sit in series along the fiber, their small individual shortenings "
"add: a 10-centimeter fiber with some 45,000 sarcomeres in series "
"shortens by nearly 3 centimeters when each sarcomere contracts "
"fully."),
"how_it_works": (
"The sliding-filament mechanism is read directly from the band "
"pattern. The A band (myosin) stays constant in width while the I "
"band (actin-only) and H zone narrow as Z discs draw together - the "
"classic proof that filaments slide rather than shorten. Skeletal "
"fibers are identified by peripheral nuclei plus strong striations; "
"cardiac by branching, central nuclei, and intercalated discs (the "
"step-like junctions carrying gap junctions and desmosomes); smooth "
"by spindle cells, central nuclei, and absent striations in "
"perpendicular bundles. The demo computes the series-summation "
"arithmetic: resting sarcomere 2.2 um contracting to 1.6 um gives "
"27.3 percent shortening per sarcomere, and 45,455 sarcomeres in "
"series along a 10 cm fiber convert that into 2.73 cm of total "
"excursion."),
"key_points": [
"Skeletal: multinucleated, peripheral nuclei, strong striations, voluntary.",
"Cardiac: branching cells, central nuclei, intercalated discs, involuntary and rhythmic.",
"Smooth: spindle cells, no striations, sheets around hollow organs, slow and sustained.",
"Sarcomere 2.2 um rest to 1.6 um contracted = 27.3% shortening; A band constant, I band narrows.",
"Sarcomeres in series sum: a 10 cm fiber shortens ~2.73 cm on full contraction.",
"Intercalated discs couple cardiac cells electrically (gap junctions) and mechanically (desmosomes)."],
"requirements": [
"Nuclear position and number: peripheral multiple vs central single.",
"Striation check at high power plus branching check at low power.",
"Intercalated disc identification for cardiac muscle.",
"The series-summation arithmetic linking sarcomere to fiber excursion."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 7, muscle tissue.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 7."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Huxley HE, Hanson J. Changes in the cross-striations of muscle during contraction and stretch and their structural interpretation. Nature. 1954;173:973-976."],
"sig_lens": (
"Signature lens: read muscle as actuator engineering. Sarcomeres "
"are linear motors wired in series for excursion and in parallel "
"for force; the three muscle types are three actuator "
"specifications - fast voluntary, rhythmic fatigue-proof, and slow "
"sustained - each matched to its load.")},
{
"key": "nervous",
"name": "Nervous Tissue: Neurons, Glia, and the Synapse",
"group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
"description": (
"Nervous tissue carries information as electricity and chemistry. "
"The neuron is its signaling cell: dendrites receive, the cell body "
"(perikaryon) integrates, the axon transmits, and the synaptic "
"terminal talks to the next cell. Nissl substance - rough ER studding "
"the cell body and dendrites - marks the protein factory that "
"sustains the enormous axon; the axon hillock, free of Nissl, is where "
"the action potential begins. Glial cells outnumber support: "
"astrocytes feed neurons and seal the blood-brain barrier, "
"oligodendrocytes (central) and Schwann cells (peripheral) wrap axons "
"in myelin, microglia patrol as resident immune cells, and ependymal "
"cells line the ventricles. Myelin is the speed technology: a 10-"
"micrometer myelinated fiber conducts near 60 meters per second by "
"saltatory jumping between nodes of Ranvier, while a 1-micrometer "
"unmyelinated fiber manages under 2 meters per second - so the same "
"one-meter signal arrives in 17 milliseconds myelinated versus nearly "
"600 milliseconds unmyelinated."),
"how_it_works": (
"Reading nervous tissue means finding the cell bodies and following "
"the processes. Large pale nuclei with prominent nucleoli in a "
"basket of cytoplasm mark neurons; tiny dark round nuclei scattered "
"between them are glia. Silver stains (Golgi, Bielschowsky) blacken "
"whole neurons including their arbors; myelin stains outline the "
"white matter tracts; Nissl stains (cresyl violet) show every cell "
"body's protein factory. In peripheral nerve cross-section, each "
"axon with its myelin sheath is one dark ring; fascicles bundle in "
"perineurium, the whole nerve in epineurium. The demo computes the "
"conduction arithmetic: myelinated velocity 6 m/s per micrometer of "
"diameter, unmyelinated 1.7 times the square root of diameter, and "
"the transit times over one meter that make myelin the difference "
"between reflex and delay."),
"key_points": [
"Neuron = dendrites (receive) + perikaryon (integrate) + axon (transmit) + terminal (signal).",
"Nissl substance marks the protein factory; the Nissl-free axon hillock fires the spike.",
"Glia: astrocytes (support/barrier), oligodendrocytes/Schwann (myelin), microglia (immune), ependymal (lining).",
"Myelinated 10 um fiber: ~60 m/s; unmyelinated 1 um fiber: ~1.7 m/s - a 35-fold speed gap.",
"Nodes of Ranvier enable saltatory conduction - the signal jumps, it does not crawl.",
"Silver stains show arbors; myelin stains show tracts; Nissl shows cell bodies."],
"requirements": [
"Neuron vs glia identification by nuclear size, nucleolus, and cytoplasm.",
"Myelin assessment: sheath presence, node spacing, fascicle organization.",
"Stain selection: Nissl for cell bodies, silver for processes, myelin stains for tracts.",
"The conduction-velocity arithmetic for myelinated vs unmyelinated fibers."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 9, nervous tissue.",
"Kierszenbaum AL, Tres LL. Histology and Cell Biology. 5th ed. Elsevier; 2019 - ch. 9."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Kandel ER, Schwartz JH, Jessell TM. Principles of Neural Science. 5th ed. McGraw-Hill; 2012.",
"Cajal SR. Histologie du systeme nerveux de l'homme et des vertebres. Maloine; 1909-1911."],
"sig_lens": (
"Signature lens: read nervous tissue as a communications network. "
"Neurons are the nodes, myelin is the bandwidth upgrade, synapses "
"are the routers - and the glia are the operations crew that powers, "
"cools, and maintains the entire installation.")},
{
"key": "membranes",
"name": "Membranes: Mucous, Serous, Cutaneous, and Synovial",
"group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
"description": (
"Four membranes line the body's compartments, each pairing an "
"epithelium with its supporting connective tissue. Mucous membranes "
"line tracts open to the outside - gut, airways, urinary, genital - "
"with epithelium suited to each tract over lamina propria; many "
"secrete mucus from goblet cells or glands. Serous membranes line "
"closed body cavities - pleura, pericardium, peritoneum - with simple "
"squamous mesothelium over thin connective tissue, secreting a "
"lubricating serous fluid so organs glide. The cutaneous membrane is "
"skin: keratinized stratified squamous epithelium over dermis, the "
"dry armor. Synovial membranes line joint cavities with a specialized "
"connective tissue (no true epithelium) that secretes hyaluronan-rich "
"synovial fluid. Scale matters in membranes: skin covers about 1.8 "
"square meters, the alveolar surface of the lungs about 70, and the "
"small intestine on the order of 30 - the exchange membranes dwarf "
"the armor, because exchange is the expensive job."),
"how_it_works": (
"Identifying a membrane means naming its epithelium and its cavity. "
"A wet tract open to the exterior with goblet cells or glands is "
"mucous; a closed cavity with glistening simple squamous lining is "
"serous (parietal on the wall, visceral on the organ); dry keratinized "
"surface is cutaneous; a joint cavity with villous connective tissue "
"and no epithelium is synovial. Function follows the pairing: mucous "
"membranes absorb, secrete, and defend; serous membranes lubricate; "
"skin waterproofs and armors; synovial membranes feed cartilage and "
"lubricate motion. The demo works the area arithmetic that explains "
"membrane design: skin 1.8 m2, alveolar surface 70 m2, small intestine "
"~30 m2, peritoneum ~1.7 m2, and each expressed as a multiple of skin "
"area so the exchange burden is visible as a number."),
"key_points": [
"Four membranes: mucous (open tracts), serous (closed cavities), cutaneous (skin), synovial (joints).",
"Mucous = epithelium + lamina propria, often with mucus glands; serous = mesothelium + thin connective tissue.",
"Serous fluid lubricates: pleura, pericardium, peritoneum - parietal lines the wall, visceral coats the organ.",
"Synovial membrane has no true epithelium; it secretes hyaluronan-rich fluid into the joint.",
"Area tells the story: alveolar 70 m2 and intestinal ~30 m2 dwarf skin 1.8 m2 - exchange is the costly job.",
"Membrane identity = epithelium type + cavity type; name both to name the membrane."],
"requirements": [
"Epithelium identification on the membrane surface.",
"Cavity classification: open to exterior vs closed vs joint space.",
"Fluid check: mucus, serous fluid, or synovial fluid - each has its source tissue.",
"The area comparisons that explain why exchange membranes are vast."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 5, membranes.",
"Young B, O'Dowd G, Woodford P. Wheater's Functional Histology. 6th ed. Elsevier; 2013."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Young B, O'Dowd G, Woodford P. Wheater's Functional Histology. 6th ed. Elsevier; 2013.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021."],
"sig_lens": (
"Signature lens: read membranes as the body's compartment seals. "
"Each membrane is specified by what it must let through and what it "
"must hold back - mucus for the open tracts, serum for the sliding "
"cavities, keratin for the dry exterior - and its area is budgeted "
"against the work it does.")},
{
"key": "fixation",
"name": "Fixation: Preserving Tissue for the Microscope",
"group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
"description": (
"Fixation freezes tissue in time: it stops autolysis and bacterial "
"decay, preserves structure as close to life as possible, and hardens "
"the tissue so it can be cut thin. The workhorse is 10 percent neutral "
"buffered formalin - about 4 percent formaldehyde gas in water - which "
"cross-links proteins by forming methylene bridges between amino "
"groups, locking the protein architecture in place. The rules are "
"quantitative: use at least ten volumes of fixative per volume of "
"tissue, keep pieces small (no more than about 5 millimeters thick), "
"and allow enough time - formalin penetrates roughly 1 millimeter per "
"hour, so a 10-millimeter block fixed from both faces needs about 5 "
"hours to reach the center, and routine fixation runs 6 to 24 hours. "
"Under-fix and the center rots; over-fix and antigens mask so badly "
"that immunostains fail. Glutaraldehyde cross-links faster and "
"preserves ultrastructure for electron microscopy but autofluoresces "
"and penetrates slowly; alcohol fixatives coagulate proteins and "
"preserve nucleic acids well. Every artifact-free slide begins with "
"fixation done right - it is the least glamorous and most decisive "
"step in histology."),
"how_it_works": (
"Formaldehyde in water exists mostly as methylene glycol; it "
"dehydrates to reactive formaldehyde, which attacks lysine side "
"chains and forms methylene bridges to nearby nitrogens - a mesh of "
"covalent cross-links through the protein fabric. Buffering to pH 7 "
"matters because unbuffered formalin oxidizes to formic acid, which "
"reacts with blood to deposit brown formalin pigment (removable with "
"picric acid or preventable by buffering). Fixation is diffusion-"
"limited: the front advances at roughly 1 mm per hour, so sectioning "
"a block too thick guarantees a fixed rind around a rotting core. "
"The demo computes the fixation arithmetic: the 10:1 fixative volume "
"for a 1 cm3 block (10 mL), the penetration time to the center of a "
"10 mm block fixed from both faces (5 hours at 1 mm/hr), and the "
"routine 6-24 hour window expressed as penetration depths."),
"key_points": [
"Fixation stops decay, preserves structure, and hardens tissue for sectioning.",
"10% neutral buffered formalin cross-links proteins via methylene bridges; buffer prevents formalin pigment.",
"Three quantitative rules: 10:1 fixative volume, pieces under ~5 mm thick, 6-24 hours.",
"Formalin penetrates ~1 mm/hr: a 10 mm block needs ~5 hr to fix its center from both faces.",
"Under-fixation rots the center; over-fixation masks antigens for immunostains.",
"Glutaraldehyde for electron microscopy; alcohols for nucleic acids; formalin for routine work."],
"requirements": [
"Fresh tissue into fixative immediately - minutes matter against autolysis.",
"The 10:1 volume ratio and the sub-5-mm thickness rule.",
"pH 7 buffering to prevent formic acid and formalin pigment.",
"Timing matched to penetration: 1 mm/hr, 6-24 hr routine."],
"standards": [
"Bancroft JD, Gamble M, eds. Theory and Practice of Histological Techniques. 6th ed. Churchill Livingstone Elsevier; 2008 - ch. 3, fixation.",
"Kiernan JA. Histological and Histochemical Methods: Theory and Practice. 5th ed. Scion; 2015."],
"citations": [
"Bancroft JD, Gamble M, eds. Theory and Practice of Histological Techniques. 6th ed. Churchill Livingstone Elsevier; 2008.",
"Kiernan JA. Histological and Histochemical Methods: Theory and Practice. 5th ed. Scion; 2015.",
"Karnovsky MJ. A formaldehyde-glutaraldehyde fixative of high osmolality for use in electron microscopy. J Cell Biol. 1965;27:137A-138A."],
"sig_lens": (
"Signature lens: treat fixation as arresting a system mid-operation "
"without corrupting the evidence. The Signature reading prices every "
"fixative by three numbers - penetration rate, cross-link density, "
"and antigen cost - and picks the fixative whose chemistry preserves "
"exactly what the downstream question needs.")},
{
"key": "sectioning",
"name": "Embedding, Sectioning, and the Microtome",
"group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
"description": (
"Fixed tissue is mostly water and far too soft to cut at 5 "
"micrometers, so it must be infiltrated with a solid support medium. "
"The paraffin route is the standard: dehydrate through graded "
"alcohols, clear in xylene (which is miscible with both alcohol and "
"paraffin), infiltrate with molten paraffin at about 60 C, and cool "
"into a block. The block is clamped in a microtome and advanced "
"against a steel or disposable blade in 5-micrometer steps; "
"consecutive sections stick edge to edge into a ribbon, which is "
"floated on warm water to flatten and picked up on a glass slide. "
"The numbers reward care: a block trimmed to 4 millimeters thick "
"yields 800 sections at 5 micrometers each, and a ribbon of 800 "
"sections each 20 millimeters long stretches 16 meters - a serial "
"section series through an entire small organ from one block. "
"Frozen section skips paraffin: tissue is snap-frozen, cut at 5 to "
"10 micrometers in a cryostat, and stained in minutes for rapid "
"diagnosis during surgery. Orientation is everything - a tube cut "
"across is a ring, cut lengthwise a channel, cut obliquely a "
"confusing ellipse - so blocks are oriented deliberately before "
"embedding."),
"how_it_works": (
"The microtome is a precision feed mechanism: each stroke advances "
"the block toward the knife by exactly the set thickness, and the "
"clearance angle of the blade peels a section whose compression is "
"minimized by a slow steady stroke. Paraffin sections cut at 4-5 um "
"for routine H&E; thinner (2-3 um) for kidney and skin where nuclear "
"detail matters; frozen sections at 5-10 um for speed. On the water "
"bath (a few degrees below paraffin's melting point) surface tension "
"flattens compression wrinkles before the section is lifted on a "
"charged or albumin-coated slide and dried overnight so it survives "
"staining. The demo computes the serial-section yield: 800 sections "
"from a 4 mm block at 5 um, the 16-meter ribbon, and the frozen-"
"section thickness trade (5-10 um) that buys minutes at the cost of "
"morphology."),
"key_points": [
"Paraffin route: dehydrate, clear in xylene, infiltrate at ~60 C, cool into a block.",
"Routine sections 4-5 um; kidney/skin 2-3 um for nuclear detail; frozen 5-10 um for speed.",
"A 4 mm block at 5 um yields 800 sections; an 800-section ribbon at 20 mm each runs 16 meters.",
"Float ribbons on warm water to erase compression wrinkles before pickup.",
"Orientation before embedding decides everything: cross, longitudinal, or oblique.",
"Frozen section trades morphology for minutes - the intraoperative diagnosis tool."],
"requirements": [
"Complete dehydration and clearing - water left behind blocks paraffin infiltration.",
"A sharp blade with correct clearance angle and steady stroke.",
"The water bath just below paraffin melting point for flattening.",
"Deliberate block orientation matched to the structure being read."],
"standards": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018 - ch. 4-6, processing and microtomy.",
"Kiernan JA. Histological and Histochemical Methods. 5th ed. Scion; 2015."],
"citations": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018.",
"Kiernan JA. Histological and Histochemical Methods: Theory and Practice. 5th ed. Scion; 2015.",
"Bancroft JD, Gamble M, eds. Theory and Practice of Histological Techniques. 6th ed. Churchill Livingstone Elsevier; 2008."],
"sig_lens": (
"Signature lens: treat embedding and sectioning as sample "
"preparation for a measurement instrument. The Signature reading "
"specifies the section thickness from the question - 2 um where "
"nuclei decide, 10 um where speed decides - and orients the block "
"so the plane of section answers rather than confuses.")},
{
"key": "he_stain",
"name": "H&E Staining: Reading Pink and Blue",
"group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
"description": (
"Hematoxylin and eosin - H&E - is the universal stain of histology: "
"if a slide exists, it is probably H&E. Hematoxylin itself is not a "
"dye until oxidized to hematein and complexed with a mordant metal "
"(usually aluminum); the resulting basic dye binds nucleic acids, so "
"nuclei stain deep blue-purple. Eosin is an acidic dye that binds "
"basic proteins, so cytoplasm, collagen, and muscle stain shades of "
"pink. The whole of diagnostic reading starts here: blue nuclei "
"against pink cytoplasm, chromatin texture visible, nucleoli "
"apparent, tissue architecture laid out in two colors. Contrast is "
"quantitative - a nucleus at optical density 0.8 transmits about 16 "
"percent of the light while cytoplasm at 0.5 transmits about 32 "
"percent, a clean 2:1 contrast that the eye reads effortlessly. "
"Staining is a timed chemistry: over-stain blue and everything is "
"nuclei; over-differentiate and the nuclei wash out; eosin too long "
"and the pinks merge. Every special stain and every immunostain is "
"interpreted against the H&E baseline - learn pink and blue first, "
"and the rest of histology is commentary."),
"how_it_works": (
"The H&E sequence is deparaffinize, hydrate, stain nuclei with "
"hematoxylin, differentiate (usually a quick acid-alcohol dip that "
"pulls dye from everything but nuclei), blue in alkaline water "
"(which converts the red-brown hematein complex to blue), counterstain "
"cytoplasm and matrix with eosin, dehydrate, clear, and mount. "
"Hematoxylin is regressive - stain dark, then differentiate back - "
"which gives crisp nuclear detail; progressive formulations stain to "
"endpoint without differentiation. Eosin comes in alcoholic (Eosin Y) "
"formulations that stain cytoplasm, red cells, and collagen in "
"distinguishable pinks. The demo applies the Beer-Lambert law to "
"the stained section: from optical densities 0.8 (nucleus) and 0.5 "
"(cytoplasm) it computes transmittances 15.8 and 31.6 percent and "
"the 2:1 contrast ratio that makes H&E readable at a glance."),
"key_points": [
"H&E is the universal baseline stain: hematoxylin (basic) stains nuclei blue; eosin (acidic) stains cytoplasm/matrix pink.",
"Hematein needs an aluminum mordant; bluing in alkaline water sets the nuclear color.",
"Regressive staining: overstain then differentiate back for crisp nuclear detail.",
"Nucleus OD 0.8 vs cytoplasm OD 0.5 gives ~2:1 optical contrast - readable at a glance.",
"Timing is the chemistry: differentiation and eosin time decide the slide.",
"Every special stain and immunostain is read against the H&E baseline."],
"requirements": [
"Complete deparaffinization and hydration before staining.",
"Controlled differentiation - the step that decides nuclear crispness.",
"Alkaline bluing to set the hematoxylin color.",
"Dehydration, clearing, and permanent mounting for an archival slide."],
"standards": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018 - ch. 9, H&E.",
"Kiernan JA. Histological and Histochemical Methods. 5th ed. Scion; 2015."],
"citations": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018.",
"Kiernan JA. Histological and Histochemical Methods: Theory and Practice. 5th ed. Scion; 2015.",
"Bancroft JD, Gamble M, eds. Theory and Practice of Histological Techniques. 6th ed. Churchill Livingstone Elsevier; 2008."],
"sig_lens": (
"Signature lens: treat H&E as the default instrument calibration. "
"The Signature reading standardizes the timing so the pink-blue "
"contrast is reproducible slide to slide - because a measurement "
"that drifts with the technician's wristwatch is not a measurement "
"at all.")},
{
"key": "special_stains",
"name": "Special Stains: PAS, Trichrome, Silver, and Reticulin",
"group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
"description": (
"When H&E cannot answer, special stains ask sharper chemical "
"questions. PAS (periodic acid-Schiff) oxidizes sugars to aldehydes "
"and stains them magenta: basement membranes, glycogen, mucin, and "
"fungal walls light up. Masson trichrome paints the connective "
"tissue question in three colors - nuclei dark, muscle and "
"cytoplasm red, collagen blue or green - so fibrosis is measured, "
"not guessed. Silver impregnation blackens reticular fibers (type "
"III collagen) and neurofibrils, revealing the scaffolding of liver, "
"lymphoid organs, and nerve. Verhoeff-Van Gieson turns elastic "
"fibers black against pink collagen and yellow muscle. Congo red "
"with polarized light finds amyloid by its apple-green "
"birefringence; Perls Prussian blue finds iron; von Kossa finds "
"calcium. Staining chemistry is pH chemistry: trichrome baths run "
"near pH 2.5 (hydrogen ion concentration about 3.2 millimolar), and "
"buffer recipes follow Henderson-Hasselbalch - an acetate buffer at "
"equal acid and conjugate base sits exactly at its pKa of 4.76. The "
"rule of special stains: each answers one chemical question well, "
"and the pathologist orders the stain that matches the question."),
"how_it_works": (
"Each special stain is a designed chemical reaction on the section. "
"PAS: periodic acid oxidizes 1,2-glycols to dialdehydes, Schiff "
"reagent couples to give magenta - diastase digestion beforehand "
"distinguishes glycogen (digested away) from other PAS-positive "
"material. Trichrome: small dyes penetrate dense collagen while "
"large dyes are excluded, after phosphotungstic/phosphomolybdic acid "
"mordanting at low pH - the color sort is by molecular size. Silver: "
"reduction of silver nitrate to metallic silver on argyrophilic "
"fibers. Iron (Perls): ferrocyanide plus ferric iron gives Prussian "
"blue. The demo works the pH arithmetic behind the baths: "
"hydrogen-ion concentration at pH 2.5 (3.16 mM), and the "
"Henderson-Hasselbalch pH of a 1:1 acetate buffer (4.76, the pKa), "
"with the ratio needed to hit pH 5.5 computed explicitly."),
"key_points": [
"PAS (magenta) answers the sugar question: basement membranes, glycogen, mucin, fungi.",
"Masson trichrome (red/blue) measures fibrosis: collagen vs muscle in contrasting colors.",
"Silver blackens reticulin and neurofibrils - the scaffolding stains.",
"Verhoeff (black) for elastin; Perls (blue) for iron; von Kossa (black) for calcium; Congo red for amyloid.",
"Stain baths are pH instruments: trichrome near pH 2.5; buffers set by Henderson-Hasselbalch.",
"Each special stain answers one chemical question - order the stain that matches the question."],
"requirements": [
"The chemical question stated before the stain is chosen.",
"pH control of staining baths (meters, not guesses).",
"Positive control sections run alongside - a stain without controls is an opinion.",
"Diastase digestion controls for PAS when glycogen is the question."],
"standards": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018 - ch. 10-14, special stains.",
"Kiernan JA. Histological and Histochemical Methods. 5th ed. Scion; 2015."],
"citations": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018.",
"Kiernan JA. Histological and Histochemical Methods: Theory and Practice. 5th ed. Scion; 2015.",
"McManus JFA. Histological and histochemical uses of periodic acid. Stain Technol. 1948;23:99-108."],
"sig_lens": (
"Signature lens: treat each special stain as a single-question "
"instrument with a specified analyte. The Signature reading logs "
"the pH, the timing, and the control result with the image - "
"because a magenta basement membrane without its controls is "
"decoration, not data.")},
{
"key": "ihc",
"name": "Immunohistochemistry: Antibodies as Stains",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Immunohistochemistry (IHC) stains proteins by name: an antibody "
"finds its antigen in the section and a visible label reports where "
"it bound. The direct method labels the primary antibody itself; the "
"indirect method - the workhorse - uses an unlabeled primary plus a "
"labeled secondary antibody against it, amplifying the signal because "
"several secondaries bind each primary. Labels are enzymes "
"(horseradish peroxidase with brown DAB, alkaline phosphatase with "
"red) or fluorophores for immunofluorescence. Because formalin "
"cross-linking hides antigens, sections usually need antigen "
"retrieval - heat in citrate or EDTA buffer - to unmask the binding "
"sites. IHC names the otherwise anonymous: cytokeratins mark "
"epithelium, vimentin marks mesenchyme, CD markers classify "
"lymphocytes, HER2 and hormone receptors guide breast cancer "
"therapy. Dilution is quantitative benchcraft: a 1 mg/mL stock "
"diluted 1:200 gives a 5 ug/mL working solution, so 10 mL needs 50 "
"uL of stock; a 2-fold serial dilution across 8 wells from 1:100 "
"runs 1:100 down to 1:12,800. Controls are non-negotiable - positive "
"tissue, negative tissue, and no-primary-antibody sections - because "
"antibodies lie convincingly without them."),
"how_it_works": (
"An IHC run is a sandwich built on the slide: block endogenous "
"peroxidase and nonspecific binding, incubate primary antibody "
"(the specificity step), wash, incubate labeled secondary (the "
"amplification step), wash, develop chromogen, counterstain nuclei "
"with hematoxylin, mount. Antigen retrieval - typically 20 minutes "
"near boiling in pH 6 citrate - breaks enough methylene cross-links "
"to reopen epitopes without destroying morphology. Scoring turns "
"color into data: nuclear stains (ER, Ki-67) score by percent "
"positive nuclei; membranous stains (HER2) score 0 to 3+ by "
"completeness and intensity. The demo computes the dilution bench "
"arithmetic: the 1:200 working dilution from 1 mg/mL stock (5 ug/mL, "
"50 uL per 10 mL) and the full 8-well 2-fold serial dilution series "
"from 1:100, verifying each well's concentration."),
"key_points": [
"IHC = antibody specificity plus visible label: proteins stained by name.",
"Indirect method dominates: unlabeled primary + labeled secondary = built-in amplification.",
"Antigen retrieval (heat + citrate/EDTA) unmasks formalin-hidden epitopes.",
"Labels: HRP/DAB (brown), alkaline phosphatase (red), fluorophores (immunofluorescence).",
"Dilution is arithmetic: 1 mg/mL stock at 1:200 = 5 ug/mL; 50 uL per 10 mL.",
"Controls decide truth: positive tissue, negative tissue, no-primary - every run."],
"requirements": [
"Properly fixed tissue - over-fixation without retrieval kills staining.",
"Antigen retrieval matched to the antibody datasheet.",
"Validated primary antibody at titrated dilution with full controls.",
"A scoring system (percent, 0-3+) applied blind to the diagnosis."],
"standards": [
"Ramos-Vara JA. Technical aspects of immunohistochemistry. Vet Pathol. 2005;42(4):405-426 - the methods standard.",
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018 - ch. 18, IHC."],
"citations": [
"Ramos-Vara JA. Technical aspects of immunohistochemistry. Vet Pathol. 2005;42(4):405-426.",
"Coons AH, Creech HJ, Jones RN. Immunological properties of an antibody containing a fluorescent group. Proc Soc Exp Biol Med. 1941;47:200-202.",
"Taylor CR, Levenson RM. Quantification of immunohistochemistry - issues concerning methods, utility and semiquantitative assessment II. Histopathology. 2006;49:411-424."],
"sig_lens": (
"Signature lens: treat IHC as a named-protein measurement "
"instrument, not a coloring book. The Signature reading specifies "
"the antibody clone, the dilution, the retrieval, and the scoring "
"rule with every image - because a brown nucleus without that "
"metadata is an anecdote.")},
{
"key": "microscopy",
"name": "The Microscope: Light, Phase-Contrast, and Electron",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"The microscope is histology's instrument, and each optical mode "
"answers a different question. Brightfield - the routine mode - "
"images stained sections with transmitted light; total "
"magnification is objective times eyepiece, so 4x, 10x, 20x, 40x, "
"and 100x objectives with a 10x eyepiece give 40x to 1000x. "
"Phase-contrast converts invisible phase shifts into brightness, "
"revealing unstained living cells. Fluorescence excites "
"fluorophores and collects their emission, the basis of "
"immunofluorescence and modern multiplex imaging. The transmission "
"electron microscope fires electrons through ultrathin sections: "
"at 100 kilovolts the electron wavelength is about 3.7 picometers, "
"and practical resolution reaches fractions of a nanometer - "
"enough to see membranes, ribosomes, and viruses. The scanning "
"electron microscope images surfaces in three-dimensional-"
"looking detail. Field of view shrinks as magnification grows: "
"with a field number 22 eyepiece, the 40x objective shows a 0.55 "
"mm field, and depth of field at NA 0.65 is about 0.65 um - focus "
"is a thin slice even in light microscopy."),
"how_it_works": (
"Resolution is set by diffraction, not by magnification: the "
"Rayleigh criterion gives 0.61 times wavelength over numerical "
"aperture, about 0.24 um for green light at NA 1.4. Magnifying "
"beyond about 1000 times the NA is empty magnification - bigger "
"but no sharper. Kohler illumination aligns the light path so the "
"field is evenly lit and the full NA is used; skipping it is the "
"commonest cause of bad images. For EM, the electron wavelength "
"comes from de Broglie: at 100 kV it is ~3.7 pm, and magnetic "
"lenses focus the beam through sections under 100 nm thick cut "
"with diamond knives. The demo computes the working microscopist's "
"table: total magnifications for all five standard objectives, the "
"0.55 mm field at 40x with FN 22, the 0.65 um depth of field at NA "
"0.65, and the 3.7 pm electron wavelength at 100 kV."),
"key_points": [
"Total magnification = objective x eyepiece: 40x to 1000x across the standard set.",
"Resolution is diffraction-limited (~0.24 um light); beyond ~1000xNA is empty magnification.",
"Phase-contrast shows living unstained cells; fluorescence enables immunofluorescence.",
"TEM at 100 kV: electron wavelength ~3.7 pm, resolution to fractions of a nanometer.",
"Field at 40x with FN 22 = 0.55 mm; depth of field at NA 0.65 ~0.65 um.",
"Kohler illumination first - uneven light wastes the finest objective."],
"requirements": [
"Kohler-aligned illumination before any critical work.",
"Objective selection matched to the question: 4x architecture, 40x cells, 100x oil detail.",
"Ultrathin sections (<100 nm, diamond knife) and vacuum for electron microscopy.",
"Fluorophore-matched filter sets for fluorescence modes."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 1-2, microscopy.",
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Ruska E. The development of the electron microscope and of electron microscopy. Biosci Rep. 1987;7:77-85.",
"Zernike F. Phase contrast, a new method for the microscopic observation of transparent objects. Physica. 1942;9:686-698."],
"sig_lens": (
"Signature lens: treat each microscope mode as a sensor with a "
"specified resolution, contrast mechanism, and sample cost. The "
"Signature reading picks the cheapest mode that resolves the "
"question - brightfield for architecture, EM only when nanometers "
"decide - and logs the NA with the image.")},
{
"key": "junctions",
"name": "Cell Junctions and the Basement Membrane",
"group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
"description": (
"Epithelial sheets hold together and seal themselves with a "
"junctional complex, read from apical to basal: the tight junction "
"(zonula occludens) fuses neighboring membranes and seals the "
"paracellular path; the adherens junction (zonula adherens) links "
"actin belts cell to cell; desmosomes (maculae adherentes) spot-weld "
"intermediate filaments across cells for mechanical strength; gap "
"junctions (connexons) are channels that pass ions and small "
"molecules directly between cytoplasms. Tight-junction leakiness is "
"measured as transepithelial electrical resistance: leaky epithelia "
"(proximal kidney tubule) read around 100 ohm-cm2, tight epithelia "
"(bladder, distal nephron) near 10,000 - a hundredfold range in "
"paracellular conductance set by claudin composition. Below it all "
"lies the basement membrane: basal lamina (lamina lucida plus lamina "
"densa, type IV collagen and laminin, made by the epithelium) fused "
"with the reticular lamina (type III collagen, made by connective "
"tissue). Hemidesmosomes rivet the cell to the basement membrane. "
"When junctions fail, barriers fail - blistering diseases attack "
"desmosomes and hemidesmosomes, and leaky tight junctions underlie "
"edema and diarrhea."),
"how_it_works": (
"The junctional complex is mapped by electron microscopy: tight "
"junctions as membrane kissing points, adherens junctions with "
"their actin insertion plaques, desmosomes with dense cytoplasmic "
"plaques and intermediate filament loops, gap junctions as 2-nm "
"intercellular gaps bridged by connexons. Functionally, tight "
"junctions gate the paracellular route - the fence function keeps "
"apical proteins apical - while gap junctions synchronize: cardiac "
"myocytes beat as one through them. The basement membrane is the "
"filtration and anchorage plane: the glomerular basement membrane "
"plus podocyte slit diaphragms form the kidney's filter. The demo "
"computes the barrier arithmetic: TER 100 vs 10,000 ohm-cm2 gives "
"conductances 10 vs 0.1 mS/cm2 - a 100:1 paracellular flux ratio "
"set by junction composition, not by thickness."),
"key_points": [
"Junctional complex, apical to basal: tight junction, adherens junction, desmosome, gap junction.",
"Tight junctions seal the paracellular path; claudin mix sets leakiness over a 100:1 range.",
"Desmosomes + hemidesmosomes are the mechanical rivets; their failure blisters skin.",
"Gap junctions (connexons) pass ions directly - electrical coupling, e.g. heart.",
"Basement membrane = basal lamina (type IV collagen, laminin) + reticular lamina (type III collagen).",
"TER: ~100 ohm-cm2 leaky vs ~10,000 tight - conductance ratio 100:1."],
"requirements": [
"Apical-to-basal ordering when describing the complex.",
"TER or tracer data to grade tight-junction function, not just morphology.",
"Basement membrane layer identification: lamina lucida, densa, reticularis.",
"Knowledge of which junction fails in which blistering disease."],
"standards": [
"Farquhar MG, Palade GE. Junctional complexes in various epithelia. J Cell Biol. 1963;17:375-412 - the defining study.",
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 5."],
"citations": [
"Farquhar MG, Palade GE. Junctional complexes in various epithelia. J Cell Biol. 1963;17:375-412.",
"Tsukita S, Furuse M, Itoh M. Multifunctional strands in tight junctions. Nat Rev Mol Cell Biol. 2001;2:285-293.",
"Yurchenco PD. Basement membranes: cell scaffoldings and signaling platforms. Cold Spring Harb Perspect Biol. 2011;3:a004911."],
"sig_lens": (
"Signature lens: read junctions as the gasket and fastener schedule "
"of the epithelial assembly. The Signature reading specifies the "
"seal rating (TER), the mechanical rating (desmosome density), and "
"the anchorage (hemidesmosomes to basement membrane) - because a "
"barrier is only as specified as its weakest joint.")},
{
"key": "blood",
"name": "Blood: The Fluid Connective Tissue",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Blood is connective tissue whose matrix is fluid: plasma carrying "
"formed elements. Erythrocytes - 5 million per microliter in men, "
"4.5 in women - are biconcave discs without nuclei or organelles, "
"packed with hemoglobin, living about 120 days. Platelets - "
"150,000 to 400,000 per microliter - are megakaryocyte fragments "
"that plug vessel breaks. Leukocytes - 4,500 to 11,000 per "
"microliter - divide into granulocytes (neutrophils with "
"multilobed nuclei, eosinophils with red granules, basophils with "
"dark blue granules) and agranulocytes (lymphocytes with dense "
"round nuclei and thin cytoplasmic rims, monocytes with kidney-"
"bean nuclei). The differential is read as absolute counts, not "
"just percentages: at 7,000 leukocytes per microliter with 60 "
"percent neutrophils, the absolute neutrophil count is 4,200 per "
"microliter - and neutropenia is defined on that absolute number. "
"Hematocrit, the packed red-cell fraction, is predicted by cell "
"count times cell volume: 5.0 million red cells per microliter at "
"90 femtoliters mean corpuscular volume gives 45 percent - the "
"arithmetic that ties the Coulter counter to the centrifuge."),
"how_it_works": (
"A blood smear is read in the monolayer zone where cells lie flat "
"without touching: red cell size, shape, and central pallor first "
"(pallor over one-third of the diameter suggests iron deficiency), "
"then the 100-cell differential, then platelets per field. "
"Absolute counts come from multiplying the differential percentage "
"by the total leukocyte count - the step that converts a pretty "
"pattern into clinical numbers. Mean corpuscular volume, mean "
"corpuscular hemoglobin, and red-cell distribution width extend the "
"reading into anemia classification. The demo performs the core "
"hematology arithmetic: absolute differential counts from 7,000 "
"WBC/uL (neutrophils 4,200; lymphocytes 2,100; monocytes 420; "
"eosinophils 210; basophils 70) and hematocrit from RBC count times "
"MCV (5.0e6 x 90 fL = 45%)."),
"key_points": [
"Blood = plasma matrix + erythrocytes, platelets, leukocytes: a fluid connective tissue.",
"Read absolute counts, not percentages: 7,000 WBC x 60% neutrophils = 4,200/uL.",
"Granulocytes (neutrophil/eosinophil/basophil) vs agranulocytes (lymphocyte/monocyte) by granules and nuclei.",
"Hematocrit = RBC count x MCV: 5.0e6/uL x 90 fL = 45%.",
"Smear reading order: red cells (size, pallor), differential, platelets - in the monolayer zone.",
"Erythrocytes: anucleate biconcave discs, ~120-day lifespan, hemoglobin-packed."],
"requirements": [
"A well-made smear read in the monolayer zone.",
"The 100-cell differential converted to absolute counts.",
"Red-cell indices (MCV, MCH, RDW) for anemia classification.",
"Reference ranges applied to absolute numbers, not percentages."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 10, blood.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 12."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Hoffbrand AV, Moss PAH. Hoffbrand's Essential Haematology. 8th ed. Wiley; 2019."],
"sig_lens": (
"Signature lens: read blood as a circulating sensor network with "
"published packet rates. The Signature reading converts every "
"smear pattern into absolute counts and indices - because the "
"diagnosis lives in the numbers, and percentages without totals "
"are decoration.")},
{
"key": "hemopoiesis",
"name": "Hemopoiesis: Where Blood Cells Are Born",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Blood cells are manufactured, not born in blood: hemopoiesis is "
"the production line, and in adults it runs in red bone marrow. The "
"pluripotent hematopoietic stem cell divides into myeloid and "
"lymphoid progenitors; the myeloid line yields erythrocytes, "
"platelets, granulocytes, and monocytes, while the lymphoid line "
"yields lymphocytes (finished in lymphoid organs). Erythropoiesis is "
"visible as a maturation series: proerythroblast to basophilic, "
"polychromatophilic, and orthochromatophilic erythroblasts, then "
"ejection of the nucleus to become a reticulocyte and finally the "
"biconcave erythrocyte - cytoplasm shifting blue to pink as "
"hemoglobin accumulates and the nucleus condenses and leaves. "
"Granulopoiesis runs myeloblast to promyelocyte to myelocyte to "
"metamyelocyte to band to segmented neutrophil. The scale of "
"manufacture is industrial: about 200 billion erythrocytes and 100 "
"billion platelets every day - roughly 2.3 million red cells and 1.2 "
"million platelets every second. Erythropoietin from the kidney "
"throttles red-cell production to oxygen need; thrombopoietin from "
"the liver sets platelet output."),
"how_it_works": (
"Marrow is read by lineage and maturation stage. Erythroid islands "
"cluster around a central macrophage that nurses developing red "
"cells and eats their ejected nuclei; megakaryocytes - giant "
"polyploid cells - shed platelets from their cytoplasmic fringes; "
"granulocytic precursors show progressively condensing, indenting "
"nuclei with lineage-specific granules appearing at the myelocyte "
"stage. The myeloid-to-erythroid (M:E) ratio in normal marrow is "
"about 3:1, shifting in disease. Fetal hemopoiesis migrates: yolk "
"sac to liver and spleen to bone marrow, which is why newborn "
"liver sections still show blood islands. The demo computes the "
"production-line rates: 2e11 red cells per day is 2.31 million per "
"second; 1e11 platelets per day is 1.16 million per second - the "
"marrow as a factory with published throughput."),
"key_points": [
"Adult hemopoiesis runs in red bone marrow from pluripotent stem cells via myeloid and lymphoid lines.",
"Erythropoiesis: proerythroblast -> basophilic -> polychromatophilic -> orthochromatophilic -> reticulocyte -> erythrocyte.",
"Granulopoiesis: myeloblast -> promyelocyte -> myelocyte -> metamyelocyte -> band -> segmented.",
"Throughput: ~2.3 million red cells and ~1.2 million platelets manufactured every second.",
"Erythroid islands nurse on central macrophages; megakaryocytes shed platelets.",
"Regulators: erythropoietin (kidney, red cells), thrombopoietin (liver, platelets)."],
"requirements": [
"Lineage identification by granules and nuclear maturation pattern.",
"The M:E ratio (~3:1 normal) as the marrow's balance sheet.",
"Recognition of erythroid islands and megakaryocytes.",
"The production-rate arithmetic that sets the scale of the system."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 10, hemopoiesis.",
"Kierszenbaum AL, Tres LL. Histology and Cell Biology. 5th ed. Elsevier; 2019 - ch. 12."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Orkin SH, Zon LI. Hematopoiesis: an evolving paradigm for stem cell biology. Cell. 2008;132:631-644.",
"Till JE, McCulloch EA. A direct measurement of the radiation sensitivity of normal mouse bone marrow cells. Radiat Res. 1961;14:213-222."],
"sig_lens": (
"Signature lens: read marrow as a manufacturing plant with "
"measured throughput. The Signature reading tracks each lineage "
"as a production line - inputs (stem cells, growth factors), "
"work-in-progress (blast stages), yield per second - and reads "
"the M:E ratio as the plant's balance sheet.")},
{
"key": "skin",
"name": "Skin: Epidermis, Dermis, and Appendages",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"Skin is the cutaneous membrane: keratinized stratified squamous "
"epithelium (epidermis) over dense connective tissue (dermis), with "
"appendages - hair follicles, sebaceous and sweat glands, nails - "
"built from the same two layers. The epidermis is a conveyor belt of "
"keratinocytes: stratum basale (mitotic stem cells on the basement "
"membrane), spinosum (desmosome-spiny cells), granulosum (keratohyalin "
"granules), lucidum (in thick skin), corneum (dead keratin scales). "
"Transit from basal layer to shedding takes about 28 days, so the "
"~15-cell-thick epidermis replaces roughly half a cell layer per day. "
"Melanocytes in the basal layer donate melanin to neighbors; "
"Langerhans cells patrol as immune sentinels; Merkel cells touch "
"nerve endings for fine touch. The dermis is dense irregular "
"connective tissue with papillae interlocking the epidermis; below "
"lies hypodermis fat. Thick skin (palms, soles) shows all five "
"strata and no hair; thin skin shows four strata and carries the "
"appendages."),
"how_it_works": (
"Reading skin starts with thick versus thin: five strata and no "
"follicles means palm or sole; hair follicles mean thin skin. The "
"epidermal strata are read basal to apical, checking the conveyor: "
"mitoses confined to the basale, orderly maturation upward, a "
"basket-weave corneum. Dermal papillae depth and collagen bundle "
"pattern separate papillary from reticular dermis. Appendages are "
"identified by structure: hair follicle with bulb, papilla, and "
"shaft; sebaceous glands as holocrine clusters emptying into "
"follicles; eccrine sweat glands as coiled dark tubules deep in "
"dermis. The demo computes the conveyor arithmetic: 28-day transit "
"over ~15 cell layers gives 0.54 layers replaced per day, and the "
"corneum - about 14 days of the journey - turns over roughly every "
"two weeks."),
"key_points": [
"Skin = keratinized stratified squamous epidermis + dense irregular dermis + appendages.",
"Strata basal to apical: basale, spinosum, granulosum, lucidum (thick skin), corneum.",
"Basal-to-shed transit ~28 days; ~15 layers replaced at ~0.54 layers/day.",
"Melanocytes (pigment), Langerhans (immune), Merkel (touch) live among keratinocytes.",
"Thick skin: 5 strata, no hair; thin skin: 4 strata plus follicles and glands.",
"Appendages: hair follicles, sebaceous (holocrine), eccrine/apocrine sweat glands, nails."],
"requirements": [
"Thick-vs-thin call from strata count and follicle presence.",
"Basal-to-apical stratum reading with maturation order checked.",
"Dermal papillae and collagen pattern for papillary vs reticular dermis.",
"Appendage identification by structure, not guesswork."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 15, skin.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 18."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Montagna W, Parakkal PF. The Structure and Function of Skin. 3rd ed. Academic Press; 1974."],
"sig_lens": (
"Signature lens: read skin as a self-renewing armor system with a "
"specified replacement rate. The Signature reading times the "
"conveyor - 28 days basal to shed - and specs each stratum as a "
"layer in the laminate, from living factory floor to dead "
"protective shell.")},
{
"key": "gi_tract",
"name": "The Digestive Tract: The Four-Layer Plan",
"group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
"description": (
"From esophagus to rectum, the digestive tube repeats one four-layer "
"plan: mucosa (epithelium plus lamina propria plus muscularis "
"mucosae), submucosa (dense connective tissue with vessels and the "
"submucosal nerve plexus), muscularis externa (inner circular and "
"outer longitudinal smooth muscle with the myenteric plexus between), "
"and serosa or adventitia outside. The epithelium changes with the "
"job: stratified squamous in esophagus (abrasion), simple columnar "
"with goblet cells in stomach and intestines (secretion/absorption). "
"The stomach adds oblique muscle and gastric glands; the small "
"intestine amplifies its absorptive surface in three stages - "
"plicae (3x), villi (10x), microvilli (20x) - for a 600-fold gain "
"over a smooth tube; the large intestine trades villi for straight "
"crypts packed with goblet cells. A 6-meter small intestine, 2.5 cm "
"in diameter, has about 0.47 square meters of smooth-tube area; "
"times 600 that is roughly 280 square meters of absorptive surface "
"- the arithmetic of why the gut can feed the body."),
"how_it_works": (
"Reading any gut section means naming the four layers and then the "
"regional specializations. Find the lumen, identify the epithelium, "
"trace the muscularis mucosae (the thin muscle line that bounds the "
"mucosa), read the submucosa for glands (esophageal, duodenal "
"Brunner glands) and plexuses, then the two muscle coats and their "
"myenteric plexus. Villi (with lacteal cores) mean small intestine; "
"straight crypts with abundant goblet cells mean large intestine; "
"gastric pits and glands mean stomach; keratin-free stratified "
"squamous means esophagus. Enteric neurons in the two plexuses run "
"peristalsis locally. The demo computes the amplification chain: "
"3 x 10 x 20 = 600, applied to the smooth cylinder area of the "
"small intestine (pi x 0.025 m x 6 m = 0.47 m2) to give ~283 m2 "
"of functional absorptive surface."),
"key_points": [
"Four-layer plan everywhere: mucosa, submucosa, muscularis externa, serosa/adventitia.",
"Epithelium matches the job: stratified squamous (esophagus) vs simple columnar (stomach, intestines).",
"Surface amplification 3 x 10 x 20 = 600x: plicae, villi, microvilli.",
"Small intestine ~283 m2 functional area from a 0.47 m2 smooth tube.",
"Two nerve plexuses run the tube: submucosal (secretion) and myenteric (motility).",
"Regional tells: villi = small bowel, straight crypts = large bowel, gastric pits = stomach."],
"requirements": [
"The four layers named in order from the lumen outward.",
"Epithelial type matched to region and function.",
"Villi/crypt/gland pattern for regional identification.",
"The amplification arithmetic linking gross length to absorptive area."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 17, digestive tract.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 15-16."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Helander HF, Fandriks L. Surface area of the digestive tract - revisited. Scand J Gastroenterol. 2014;49:681-689."],
"sig_lens": (
"Signature lens: read the gut as a processing pipeline with "
"specified stage gains. The Signature reading assigns each layer "
"and each amplification stage its factor - 3, 10, 20, product 600 "
"- and treats the two nerve plexuses as the embedded control "
"system running secretion and motility.")},
{
"key": "liver_pancreas",
"name": "Liver and Pancreas: Digestive Glands",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"The liver and pancreas are the gut's great accessory glands, and "
"both are dual organs. The liver's hepatocytes arrange in plates "
"one cell thick, bathed on both faces by sinusoidal blood flowing "
"from portal triads (bile duct, portal venule, hepatic arteriole) "
"to the central vein; bile flows the opposite way, from hepatocyte "
"to portal bile duct. The classic lobule is a hexagon about 1 mm "
"across centered on the central vein; the portal lobule and the "
"hepatic acinus are the same tissue re-centered on bile flow and "
"blood supply respectively. A 1-mm lobule in cross-section covers "
"about 0.65 square millimeters; at 20 micrometers per hepatocyte "
"that is roughly 1,600 cells per section, and over a 2-mm lobule "
"length about 160,000 hepatocytes per lobule. Kupffer cells patrol "
"the sinusoids; stellate cells store vitamin A and make scar in "
"disease. The pancreas pairs an exocrine acinar factory - "
"serous acini draining through intercalated ducts into the "
"duodenum - with the endocrine islets of Langerhans (alpha "
"glucagon, beta insulin, delta somatostatin) releasing hormones "
"to blood."),
"how_it_works": (
"Liver sections are read by flow: find portal triads and central "
"veins, then trace the hepatocyte plates between them. Sinusoids "
"lined by fenestrated endothelium plus Kupffer cells carry mixed "
"portal and arterial blood; the space of Disse between endothelium "
"and hepatocytes holds plasma and stellate cells. Zonation matters: "
"periportal zone 1 gets the richest blood, centrilobular zone 3 "
"the poorest - so ischemia necroses zone 3 first. Pancreas is read "
"as two tissues interleaved: basophilic basal cytoplasm and apical "
"zymogen granules mark exocrine acini; pale islets stand out among "
"them, with beta cells central and alpha/delta peripheral. The "
"demo computes the lobule cell census: hexagon area 0.65 mm2 at "
"1 mm diameter, ~1,624 hepatocytes per cross-section at 20 um per "
"cell, ~162,000 per 2-mm lobule."),
"key_points": [
"Liver: hepatocyte plates between portal triads and central veins; blood and bile flow opposite.",
"Three lobule models, one tissue: classic (central vein), portal (bile duct), acinus (blood supply).",
"~162,000 hepatocytes per 1-mm classic lobule; zonation 1->3 sets ischemia vulnerability.",
"Kupffer cells (macrophages) patrol sinusoids; stellate cells store vitamin A, scar in disease.",
"Pancreas = exocrine serous acini (zymogen granules, ductal drainage) + endocrine islets (alpha/beta/delta).",
"Islet layout: beta cells central (insulin), alpha and delta peripheral."],
"requirements": [
"Portal triad vs central vein identification to orient flow.",
"Zonation reading: periportal to centrilobular gradients.",
"Acinar vs islet distinction in pancreas by staining and granularity.",
"The lobule census arithmetic for scale."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 18, liver and pancreas.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 16."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Rappaport AM. The microcirculatory hepatic unit and the pathophysiology of the liver. Microvasc Res. 1973;6:212-228.",
"Orci L. The islet of Langerhans: a brief historical review. Diabetologia. 1982;22:133-137."],
"sig_lens": (
"Signature lens: read liver and pancreas as counter-flow chemical "
"plants. The Signature reading traces both flows - blood in, bile "
"out, enzymes to the gut, hormones to the blood - and treats "
"zonation as the plant's gradient map, with each zone's oxygen "
"budget published per position.")},
{
"key": "respiratory",
"name": "The Respiratory Tract: From Trachea to Alveolus",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"The respiratory tract is a conducting system ending in an exchange "
"surface. The trachea and bronchi are held open by C-shaped "
"hyaline cartilage, lined by ciliated pseudostratified columnar "
"epithelium with goblet cells - the mucociliary escalator sweeping "
"debris upward. As airways branch through 23 generations, cartilage "
"plates shrink to nothing, glands vanish, epithelium simplifies to "
"cuboidal then squamous, and smooth muscle takes over wall tone - "
"bronchioles have no cartilage at all. The alveolar ducts and "
"alveoli are the exchange zone: type I pneumocytes are paper-thin "
"squamous cells sharing a fused basal lamina with capillary "
"endothelium (the blood-air barrier, about 0.5 um); type II "
"pneumocytes secrete surfactant and divide to repair; alveolar "
"macrophages patrol the airspaces. The numbers are the physiology: "
"some 480 million alveoli provide about 70 square meters of "
"exchange surface, each alveolus about 0.15 square millimeters - a "
"sphere about 0.2 millimeters across - and the whole surface is "
"perfused by the densest capillary bed in the body."),
"how_it_works": (
"Airway sections are identified by their wall components: cartilage "
"plus glands means bronchus; smooth muscle with folded mucosa and "
"no cartilage means bronchiole; thin septa with capillary loops "
"means alveoli. Epithelial height tracks generation: tall "
"ciliated pseudostratified proximally, low cuboidal in terminal "
"bronchioles (with club/Clara cells), squamous type I cells "
"distally. Surfactant from type II cells lowers surface tension so "
"small alveoli do not collapse into large ones (Laplace's law "
"managed by chemistry). The blood-air barrier - type I cell, fused "
"basal lamina, endothelium - is crossed by diffusion alone. The "
"demo computes the alveolar census: 70 m2 over 480 million alveoli "
"gives 0.146 mm2 each, equivalent to a 0.22 mm sphere - matching "
"the measured alveolar diameter of 0.2-0.3 mm."),
"key_points": [
"Conducting zone: cartilage, glands, ciliated pseudostratified epithelium - decreasing with each generation.",
"23 airway generations from trachea to alveolar sacs; bronchioles have no cartilage.",
"Blood-air barrier ~0.5 um: type I pneumocyte + fused basal lamina + endothelium.",
"Type II pneumocytes make surfactant (anti-collapse) and regenerate type I cells.",
"480 million alveoli x 0.146 mm2 each = 70 m2 of exchange surface.",
"Alveolar macrophages patrol the airspaces - the lung's resident cleanup crew."],
"requirements": [
"Airway identification by wall components: cartilage, glands, muscle, epithelium.",
"Epithelial height tracked against airway generation.",
"Blood-air barrier layer count on electron microscopy.",
"The alveolar census arithmetic tying count to surface."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 19, respiratory system.",
"Weibel ER. The Pathway for Oxygen. Harvard University Press; 1984 - morphometry of the lung."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Weibel ER. The Pathway for Oxygen: Structure and Function in the Mammalian Respiratory System. Harvard University Press; 1984.",
"Ochs M et al. The number of alveoli in the human lung. Am J Respir Crit Care Med. 2004;169:120-124."],
"sig_lens": (
"Signature lens: read the lung as a gas-exchange plant with a "
"published surface budget. The Signature reading specs the "
"conducting zone as ductwork, the alveoli as 480 million parallel "
"exchange units, and the 0.5-um barrier as the thinnest wall that "
"still holds blood on one side and air on the other.")},
{
"key": "urinary",
"name": "The Urinary System: Nephrons and Filtration",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"The kidney filters blood and tunes the filtrate into urine, and "
"its functional unit - the nephron - is a masterpiece of tubular "
"engineering. The renal corpuscle (glomerulus plus Bowman capsule) "
"filters: fenestrated endothelium, glomerular basement membrane, "
"and podocyte slit diaphragms form a three-layer sieve passing "
"water and small solutes while holding back cells and most "
"protein. The tubule then rewrites the filtrate: proximal "
"convoluted tubule reabsorbs the bulk (brush border microvilli, "
"eosinophilic cytoplasm), loop of Henle builds the medullary "
"gradient, distal tubule and collecting duct fine-tune sodium, "
"potassium, and water under hormonal control. The scale: "
"glomerular filtration rate about 125 mL per minute means 180 "
"liters filtered per day - the entire plasma volume filtered some "
"60 times daily. With about 2 million nephrons across both "
"kidneys, each nephron filters about 62.5 nanoliters per minute - "
"the single-nephron GFR that the whole organ's output divides "
"into."),
"how_it_works": (
"Kidney cortex is read by corpuscle and tubule: round glomerular "
"tufts in Bowman capsules mark the cortex; proximal tubules show "
"brush borders and eosinophilic cytoplasm; distal tubules are "
"paler with distinct cell borders and macula densa plaques where "
"they touch their own glomerulus. Medulla shows loops of Henle "
"and collecting ducts in parallel bundles plus the vasa recta. "
"The filtration barrier is an EM diagnosis: endothelium (70-100 "
"nm fenestrae), GBM (type IV collagen, laminin, negative charge), "
"podocyte foot processes with slit diaphragms - effacement of "
"foot processes means proteinuria. The demo computes the "
"filtration arithmetic: 125 mL/min x 1440 min = 180 L/day, "
"divided by 2 million nephrons = 62.5 nL/min per nephron."),
"key_points": [
"Nephron = renal corpuscle (filter) + tubule (reprocessor): PCT, loop of Henle, DCT, collecting duct.",
"Filtration barrier: fenestrated endothelium + GBM + podocyte slit diaphragm.",
"GFR 125 mL/min = 180 L/day filtered - plasma turned over ~60x daily.",
"Single-nephron GFR: 180 L/day / 2 million nephrons = 62.5 nL/min each.",
"Tubule ID: brush border + eosinophilia = proximal; pale + macula densa = distal.",
"Podocyte foot-process effacement on EM = the structural correlate of proteinuria."],
"requirements": [
"Corpuscle vs tubule vs medullary ray identification in cortex.",
"Proximal/distal distinction by brush border, staining, and macula densa.",
"Filtration barrier layers on electron microscopy.",
"The GFR-to-single-nephron division that sets the scale."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 20, urinary system.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 19."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Brenner BM, Rector FC. The Kidney. 7th ed. Saunders; 2004."],
"sig_lens": (
"Signature lens: read the nephron as a filtration plant with a "
"published mass balance. The Signature reading tracks 180 liters "
"a day in, ~1.5 liters out, and prices every tubule segment by "
"what fraction of the filtrate it reclaims - because the kidney "
"is the body's water and salt accountant.")},
{
"key": "cardiovascular",
"name": "The Cardiovascular System: Vessels and Heart",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Every blood vessel repeats the three-tunic plan: tunica intima "
"(endothelium plus subendothelial connective tissue), tunica media "
"(smooth muscle and elastin), tunica adventitia (connective tissue). "
"Arteries carry pressure: elastic arteries (aorta) have media "
"layered with elastic lamellae to smooth the pulse; muscular "
"arteries distribute with a thick smooth-muscle media; arterioles - "
"the resistance vessels - are mostly media around a tiny lumen. "
"Capillaries are endothelium plus basal lamina: continuous (muscle, "
"lung), fenestrated (gut, kidney), sinusoidal (liver, marrow) - "
"permeability matched to tissue. Veins return at low pressure with "
"thin walls and valves. The heart wall is three layers with muscle "
"in the middle: endocardium, myocardium (spiral bundles of cardiac "
"muscle), epicardium. The pump arithmetic closes the loop: 70 beats "
"per minute times 70 mL stroke volume gives 4.9 liters per minute "
"cardiac output, and against a 5-liter blood volume the entire "
"circulation turns over about once a minute."),
"how_it_works": (
"Vessel identification is wall reading: prominent elastic lamellae "
"mean elastic artery; thick media with a visible internal elastic "
"lamina means muscular artery; media of 1-2 smooth-muscle layers "
"means arteriole; endothelium-only means capillary; thin wall with "
"wide lumen (often collapsed) means vein. Verhoeff stain settles "
"elastic questions. Capillary type is an EM call: continuous with "
"tight junctions, fenestrated with diaphragmed pores, sinusoidal "
"with gaps and incomplete basal lamina. Heart muscle is recognized "
"by branching fibers, central nuclei, and intercalated discs in a "
"spiral three-layer wall. The demo computes the circulation "
"arithmetic: cardiac output 70 x 70 mL = 4.9 L/min, and 5 L blood "
"volume divided by 4.9 L/min = 1.02 min per full circuit."),
"key_points": [
"Three tunics everywhere: intima (endothelium), media (muscle/elastin), adventitia (connective tissue).",
"Elastic arteries smooth the pulse; muscular arteries distribute; arterioles set resistance.",
"Capillaries: continuous, fenestrated, sinusoidal - permeability matched to tissue need.",
"Veins: thin walls, wide lumens, valves - low-pressure return.",
"Heart wall: endocardium, spiral myocardium, epicardium; cardiac muscle with intercalated discs.",
"70 bpm x 70 mL = 4.9 L/min output; 5 L volume turns over ~once per minute."],
"requirements": [
"Wall-component reading to name the vessel class.",
"Elastic lamina check (Verhoeff) for artery typing.",
"Capillary type by endothelium and basal lamina on EM.",
"The cardiac-output-to-circulation-time division."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 11, cardiovascular system.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 11."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Rhodin JAG. Ultrastructure of mammalian venous capillaries, venules, and small collecting veins. J Ultrastruct Res. 1968;25:452-500."],
"sig_lens": (
"Signature lens: read the vasculature as a pressure-rated piping "
"network. The Signature reading specs each vessel class by wall "
"construction against its pressure duty - elastic for surge, "
"muscular for distribution, capillary for exchange - and closes "
"the loop with the pump arithmetic.")},
{
"key": "lymphoid",
"name": "Lymphoid Tissue: Nodes, Spleen, and Thymus",
"group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
"description": (
"Lymphoid tissue is the immune system's architecture: lymphocytes "
"organized for surveillance. Lymph nodes filter lymph: afferent "
"vessels enter the convex surface, lymph percolates through "
"subcapsular, cortical, and medullary sinuses past macrophage-"
"lined cords, and exits via the hilum - cortex with B-cell "
"follicles (germinal centers when active), paracortex with T "
"cells, medulla with cords and sinuses. The spleen filters blood "
"instead: white pulp (periarteriolar lymphoid sheaths and "
"follicles) around central arterioles, red pulp of cords and "
"sinuses where macrophages cull old red cells. The thymus schools "
"T cells: cortex packed with developing thymocytes, medulla with "
"Hassall corpuscles, all behind a blood-thymus barrier - and it "
"involutes after puberty. MALT (tonsils, Peyer patches, appendix) "
"guards the mucosae. The throughput is real: the thoracic duct "
"returns about 100 mL of lymph per hour - 2.4 liters a day - and "
"with some 600 nodes in the body, each node filters on the order "
"of 4 mL of lymph daily."),
"how_it_works": (
"Lymphoid organs are read by compartment: follicles (B zones, "
"germinal centers pale with tingible-body macrophages when "
"active), paracortex (T zone), sinuses (macrophage-lined "
"channels), and the capsule/hilum plumbing. Node versus spleen is "
"a fluid question - lymph sinuses versus blood sinuses - plus the "
"capsule: nodes have afferent vessels through the capsule, the "
"spleen has trabeculae carrying vessels inward. Thymus is cortex-"
"medulla with Hassall corpuscles and no follicles. IHC sharpens "
"the zones: CD20 for B cells, CD3 for T cells, Ki-67 for germinal "
"center proliferation. The demo computes the lymph throughput: "
"100 mL/hr x 24 = 2.4 L/day through the thoracic duct, divided "
"over ~600 nodes = ~4 mL per node per day."),
"key_points": [
"Lymph nodes filter LYMPH: cortex (B follicles), paracortex (T cells), medullary cords and sinuses.",
"Spleen filters BLOOD: white pulp (lymphoid) around arterioles, red pulp (cords/sinuses) culling red cells.",
"Thymus schools T cells behind a blood-thymus barrier; Hassall corpuscles mark the medulla.",
"MALT (tonsils, Peyer patches) guards mucosal surfaces.",
"Thoracic duct: ~100 mL/hr = 2.4 L/day; ~600 nodes share ~4 mL each per day.",
"IHC zones the tissue: CD20 (B), CD3 (T), Ki-67 (proliferation)."],
"requirements": [
"Compartment reading: follicle, paracortex/T zone, sinus, capsule.",
"Lymph-vs-blood filtration to separate node from spleen.",
"Hassall corpuscles for thymus; germinal centers for active follicles.",
"The throughput division across the node population."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 14, lymphoid system.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 14."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Willard-Mack CL. Normal structure, function, and histology of lymph nodes. Toxicol Pathol. 2006;34:409-424."],
"sig_lens": (
"Signature lens: read lymphoid tissue as a distributed screening "
"network with published flow rates. The Signature reading assigns "
"each organ its fluid - lymph, blood, or neither - and prices the "
"surveillance by throughput: 2.4 liters a day through 600 screening "
"stations.")},
{
"key": "endocrine",
"name": "Endocrine Glands: Pituitary, Thyroid, and Adrenal",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Endocrine glands are ductless: they release hormones into "
"bloodstream capillaries, usually as cords or follicles of cells "
"wrapped around sinusoids. The pituitary (hypophysis) is two glands "
"in one: anterior (adenohypophysis) with acidophils, basophils, and "
"chromophobes secreting GH, prolactin, TSH, ACTH, LH, FSH; posterior "
"(neurohypophysis) storing hypothalamic oxytocin and ADH in Herring "
"bodies. The thyroid stores its product extracellularly - colloid-"
"filled follicles of thyroglobulin ringed by follicular cells, with "
"parafollicular C cells secreting calcitonin. The adrenal cortex is "
"three zones with three products: glomerulosa (aldosterone), "
"fasciculata (cortisol), reticularis (androgens); the medulla is "
"modified sympathetic ganglion secreting epinephrine. Feedback "
"closes the loop: thyroid hormone suppresses TSH, cortisol "
"suppresses ACTH. A minimal feedback model - TSH driven by "
"10/(1+T4/4), T4 produced at 2xTSH and cleared at 0.5/day - settles "
"to T4 ~10.8 units, the steady state where production exactly "
"balances clearance and the loop holds itself stable."),
"how_it_works": (
"Endocrine histology is cell-and-pattern reading: cords of cells "
"around sinusoids (pituitary, adrenal, pancreatic islets), follicles "
"with colloid (thyroid), or zona patterns (adrenal cortex "
"glomerulosa/fasciculata/reticularis read outer to inner). IHC names "
"the cell: GH, prolactin, TSH, ACTH, LH/FSH in pituitary acidophils "
"and basophils; thyroglobulin and calcitonin in thyroid; "
"chromogranin in medulla. Function is inferred from structure plus "
"feedback logic: a hyperplastic basophil population with adrenal "
"cortical hypertrophy reads as chronic ACTH drive. The demo "
"simulates the negative-feedback loop numerically: Euler integration "
"of T4 with TSH = 10/(1+T4/4), production 2*TSH, clearance 0.5*T4, "
"converging to the analytic steady state T4 = 10.806 - the loop "
"holding itself stable without any controller but its own wiring."),
"key_points": [
"Endocrine = ductless: cords or follicles of cells around sinusoids, hormones to blood.",
"Pituitary: anterior (6 hormones, acidophils/basophils/chromophobes) + posterior (oxytocin/ADH storage).",
"Thyroid: colloid follicles (thyroglobulin) + C cells (calcitonin).",
"Adrenal cortex: glomerulosa (aldosterone) / fasciculata (cortisol) / reticularis (androgens); medulla (epinephrine).",
"Feedback closes every loop: T4 suppresses TSH, cortisol suppresses ACTH.",
"Model steady state T4 ~10.8: production 2*TSH exactly balances clearance 0.5*T4."],
"requirements": [
"Cord/follicle/zona pattern recognition per gland.",
"IHC cell typing where H&E leaves cells anonymous.",
"Feedback-loop logic: which hormone suppresses which driver.",
"The steady-state computation showing the loop is self-stabilizing."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 21, endocrine system.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 20."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Melmed S et al. Williams Textbook of Endocrinology. 14th ed. Elsevier; 2019."],
"sig_lens": (
"Signature lens: read endocrine glands as control systems with "
"the wiring visible. The Signature reading draws each feedback "
"loop - sensor, signal, actuator, setpoint - and verifies the "
"loop is stable by simulation before trusting the anatomy "
"alone.")},
{
"key": "bone",
"name": "Bone: Osteons, Remodeling, and Growth",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"Bone is connective tissue with a mineralized matrix: type I "
"collagen scaffolding stiffened by hydroxyapatite crystals, built "
"and maintained by three cell types - osteoblasts (builders, "
"cuboidal on bone surfaces), osteocytes (entombed former "
"osteoblasts networked through canaliculi), osteoclasts (multinucleated "
"resorbers in Howship lacunae). Compact bone is organized into "
"osteons (Haversian systems): concentric lamellae around a central "
"canal carrying vessels and nerve, cemented to neighbors by "
"cement lines. An osteon 200 um across with a 50-um central canal "
"has a 75-um wall; at 5 um per lamella that is 15 concentric "
"lamellae. Spongy bone is trabeculae aligned to stress lines. "
"Growth runs at the epiphyseal plate: zones of reserve, "
"proliferation, hypertrophy, calcification, and ossification turn "
"cartilage into length. Remodeling never stops: osteoclasts tunnel, "
"osteoblasts refill, replacing about 10 percent of the skeleton "
"per year - the whole skeleton renewed roughly every decade."),
"how_it_works": (
"Bone sections are read by organization and cell: lamellar versus "
"woven (woven is fetal/fracture, random fibers), osteon cross-"
"sections with central canals versus interstitial lamellae, "
"osteoblast seams versus osteoclast pits. Polarized light reveals "
"lamellar alternation; tetracycline labels show mineralization "
"fronts as fluorescent bands. The growth plate is read zone by "
"zone - disruption of the hypertrophic zone shortens bone. "
"Remodeling is quantified by histomorphometry: osteoid seam "
"width, mineral apposition rate, eroded surface. The demo "
"computes the osteon lamella count (200-um osteon, 50-um canal: "
"75-um wall / 5-um lamellae = 15 lamellae) and the remodeling "
"budget (10%/year -> full skeleton turnover in ~10 years)."),
"key_points": [
"Bone = mineralized type I collagen matrix + osteoblasts, osteocytes, osteoclasts.",
"Osteon: 200-um system, 50-um central canal, 15 lamellae at 5 um each, cement lines between.",
"Growth plate zones: reserve, proliferation, hypertrophy, calcification, ossification.",
"Remodeling: ~10%/year - the skeleton is rebuilt about every 10 years.",
"Woven bone (random) = fetal or repair; lamellar bone (ordered) = mature.",
"Osteoclasts resorb in Howship lacunae; osteoblasts lay osteoid that mineralizes."],
"requirements": [
"Osteon vs interstitial lamellae vs trabeculae identification.",
"Cell census: osteoblast (surface cuboidal), osteocyte (lacunae), osteoclast (multinucleated pit).",
"Growth-plate zone reading for length-growth assessment.",
"The remodeling-rate arithmetic for turnover time."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 8, bone.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 8."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Parfitt AM. The cellular basis of bone remodeling: the quantum concept reexamined in light of recent advances in cell biology. Calcif Tissue Int. 1984;36:S37-S45.",
"Frost HM. The Laws of Bone Structure. Charles C Thomas; 1964."],
"sig_lens": (
"Signature lens: read bone as a living structure under continuous "
"renovation. The Signature reading specs the osteon as a pressure "
"vessel with counted lamellae, the growth plate as a length-"
"manufacturing line with five stations, and remodeling as a "
"maintenance budget: 10 percent per year, no exceptions.")},
{
"key": "male_repro",
"name": "The Male Reproductive System: Testis and Spermatogenesis",
"group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
"description": (
"The testis manufactures sperm and testosterone in two "
"compartments. Seminiferous tubules - coiled loops packed in "
"lobules - run spermatogenesis: spermatogonia on the basement "
"membrane divide into primary spermatocytes (meiosis I), secondary "
"spermatocytes (meiosis II), spermatids, and finally spermatozoa "
"released into the lumen - a 74-day journey from stem cell to "
"swimmer. Sertoli cells nurse the developing germ cells, form the "
"blood-testis barrier with tight junctions, and secrete androgen-"
"binding protein and inhibin. Between tubules, Leydig cells make "
"testosterone. The epididymis matures and stores sperm (stereocilia "
"here are absorptive, not motile); the vas deferens propels with "
"thick smooth muscle; accessory glands (seminal vesicles, prostate, "
"bulbourethral) contribute the seminal fluid. Daily output runs "
"100 to 200 million sperm - about 1,160 new sperm every second at "
"100 million per day, manufactured continuously from puberty on."),
"how_it_works": (
"Testis sections are read by tubule stage: the seminiferous "
"epithelium shows the full maturation stack from basement "
"membrane to lumen, and experienced readers stage the tubule by "
"which germ-cell generations are present. Sertoli nuclei are "
"pale and irregular among the germ cells; Leydig cells are "
"eosinophilic polyhedral clusters in the interstitium, often with "
"Reinke crystals. Sperm morphology is assessed on smears: head, "
"midpiece, tail, with strict criteria for normal forms. "
"Obstruction versus production failure is the clinical branch "
"point that histology helps settle. The demo computes the "
"production rate: 100 million sperm per day divided by 86,400 "
"seconds = 1,157 sperm per second, sustained every second of "
"every day."),
"key_points": [
"Seminiferous tubules: spermatogonia -> spermatocytes -> spermatids -> spermatozoa over 74 days.",
"Sertoli cells nurse germ cells and form the blood-testis barrier; Leydig cells make testosterone.",
"Epididymis matures/stores (stereocilia = absorptive); vas deferens propels; accessory glands add fluid.",
"100-200 million sperm/day = ~1,157 new sperm every second, continuously from puberty.",
"Leydig cells: eosinophilic interstitial clusters, sometimes with Reinke crystals.",
"Tubule staging by germ-cell generations present, basement membrane to lumen."],
"requirements": [
"Seminiferous epithelium staging: which generations are present.",
"Sertoli vs germ cell vs Leydig identification.",
"Blood-testis barrier understanding: Sertoli tight junctions.",
"The production-rate arithmetic for scale."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 22, male reproductive system.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 21."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Amann RP. The cycle of the seminiferous epithelium in humans: a need to revisit? J Androl. 2008;29:469-487."],
"sig_lens": (
"Signature lens: read the testis as a continuous-flow production "
"line with two products. The Signature reading tracks the 74-day "
"pipeline stage by stage - stem cell in, swimmer out, 1,157 per "
"second - with Sertoli cells as the line operators and Leydig "
"cells as the utilities plant.")},
{
"key": "female_repro",
"name": "The Female Reproductive System: Ovary and Endometrium",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"The ovary rations its lifetime supply: about 1.5 million follicles "
"at birth, some 400 ever ovulated - 99.97 percent lost to atresia. "
"Follicles mature in stages: primordial (oocyte plus flat granulosa), "
"primary, secondary (antrum forming), Graafian (mature, pre-ovulatory) "
"- with theca interna cells making androgens and granulosa cells "
"converting them to estrogen. After ovulation the follicle becomes "
"the corpus luteum, secreting progesterone, then regresses to corpus "
"albicans without pregnancy. The endometrium answers the hormones: "
"proliferative phase (estrogen) rebuilds glands and stroma; "
"secretory phase (progesterone) coils the glands and fills them "
"with glycogen; menstruation sheds the functionalis when hormones "
"fall. The uterine tube catches the oocyte with ciliated fimbriae; "
"the placenta - chorionic villi of fetal trophoblast bathed in "
"maternal blood - is the fetomaternal exchange organ built fresh "
"for each pregnancy."),
"how_it_works": (
"Ovarian sections are staged by follicle: count the granulosa "
"layers, check for antrum, theca layers, and atresia (the fate of "
"almost all). Corpus luteum is recognized by large pale luteinized "
"cells; corpus albicans by its collagen scar. Endometrium is dated "
"by gland shape and stromal change: straight glands (proliferative), "
"coiled secretory glands with subnuclear vacuoles then supranuclear "
"(secretory), stromal breakdown (menstrual) - the dating criteria "
"used in fertility workups. Placental villi are read by "
"gestational age: cytotrophoblast prominence early, thin "
"syncytiotrophoblast with vasculosyncytial membranes at term. The "
"demo computes the attrition: (1,500,000 - 400)/1,500,000 = 99.973% "
"atresia - the ovary as a rationing system."),
"key_points": [
"~1.5 million follicles at birth, ~400 ovulated: 99.973% lost to atresia.",
"Follicle stages: primordial -> primary -> secondary -> Graafian -> corpus luteum -> albicans.",
"Theca interna makes androgens; granulosa converts to estrogen; corpus luteum makes progesterone.",
"Endometrium: proliferative (estrogen) -> secretory (progesterone) -> menstrual (withdrawal).",
"Uterine tube fimbriae catch the oocyte; cilia move it toward the uterus.",
"Placenta: fetal chorionic villi bathed in maternal blood - built fresh each pregnancy."],
"requirements": [
"Follicle staging by granulosa layers, antrum, and theca.",
"Corpus luteum vs albicans identification.",
"Endometrial dating: gland shape and stromal phase matched to cycle day.",
"The attrition arithmetic framing the ovary as a rationing system."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 23, female reproductive system.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 22."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021.",
"Noyes RW, Hertig AT, Rock J. Dating the endometrial biopsy. Fertil Steril. 1950;1:3-25."],
"sig_lens": (
"Signature lens: read the ovary as a lifetime inventory managed "
"by attrition. The Signature reading counts the stock (1.5 "
"million), the issues (400), and the shrinkage (99.97%) - and "
"reads the endometrium as the monthly-built receiving dock, "
"constructed, stocked, and demolished on hormonal schedule.")},
{
"key": "cns",
"name": "The Central Nervous System: Brain and Spinal Cord",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"The central nervous system organizes neurons into gray matter "
"(cell bodies) and white matter (myelinated axons). The cerebral "
"cortex is a 2.5-mm sheet of six layers: molecular, external "
"granular, external pyramidal, internal granular, internal "
"pyramidal (giant Betz cells), and multiform - about 0.4 mm per "
"layer on average, with 16 billion neurons in cortex alone of the "
"brain's 86 billion. The cerebellar cortex folds into folia with "
"three layers: molecular, Purkinje (single row of giant flask "
"cells), granular - Purkinje cells being the sole output. The "
"spinal cord shows the butterfly: dorsal horns (sensory in), "
"ventral horns (motor out), surrounding white-matter columns. "
"Meninges wrap it all: dura, arachnoid, pia. Glia nearly match "
"neurons one-for-one (~85 billion): astrocytes with perivascular "
"feet sealing the blood-brain barrier, oligodendrocytes myelinating "
"central axons, microglia patrolling, ependyma lining ventricles. "
"Choroid plexus - ependymal cells over vascular cores - makes "
"cerebrospinal fluid."),
"how_it_works": (
"CNS sections are read by layer and region: six cortical layers "
"identified by cell size and packing (granular = small, pyramidal "
"= triangular), cerebellar three layers with the unmistakable "
"Purkéinje row, spinal cord horns and columns in cross-section. "
"Myelin stains (Luxol fast blue) map white matter; Nissl stains "
"map cell bodies; silver stains trace processes; IHC names cell "
"types (GFAP astrocytes, Olig2 oligodendrocytes, Iba1 microglia, "
"NeuN neurons). The blood-brain barrier is an EM and functional "
"call: endothelial tight junctions plus astrocyte feet plus "
"pericytes. The demo computes the cortical layer budget: 2.5 mm "
"over 6 layers = 0.417 mm per layer, and the cell census (86B "
"neurons, ~85B glia, 16B cortical) that sets the scale of the "
"network."),
"key_points": [
"Gray matter = cell bodies; white matter = myelinated axons - the first branch of every CNS reading.",
"Cerebral cortex: 6 layers in 2.5 mm (~0.42 mm/layer); 16B of the brain's 86B neurons.",
"Cerebellar cortex: molecular / Purkinje / granular - Purkinje cells are the sole output.",
"Spinal cord: dorsal horns sensory-in, ventral horns motor-out, white columns around.",
"Glia ~85B: astrocytes (barrier), oligodendrocytes (myelin), microglia (immune), ependyma (lining).",
"Choroid plexus makes CSF; meninges (dura/arachnoid/pia) wrap the system."],
"requirements": [
"Cortical layer identification by cell size and packing density.",
"Region recognition: cerebrum vs cerebellum vs spinal cord by architecture.",
"Stain selection: myelin (Luxol), cell bodies (Nissl), processes (silver), cell type (IHC).",
"The layer-budget and cell-census arithmetic for scale."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 12, nervous system.",
"Kierszenbaum AL, Tres LL. Histology and Cell Biology. 5th ed. Elsevier; 2019 - ch. 9."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Herculano-Houzel S. The human brain in numbers: a linearly scaled-up primate brain. Front Hum Neurosci. 2009;3:31.",
"Brodmann K. Vergleichende Lokalisationslehre der Grosshirnrinde. Barth; 1909."],
"sig_lens": (
"Signature lens: read the CNS as a layered compute fabric with "
"a published bill of materials. The Signature reading budgets "
"the cortex by layer (0.42 mm each), counts the nodes (86 "
"billion) and the support crew (85 billion glia), and treats the "
"blood-brain barrier as the facility's access control.")},
{
"key": "eye",
"name": "The Eye: Retina and the Layers of Vision",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"The eye is nervous tissue extended to the surface, and the retina "
"is brain laid out in ten layers: from the vitreous inward - "
"internal limiting membrane, nerve fiber layer, ganglion cell "
"layer, inner plexiform, inner nuclear, outer plexiform, outer "
"nuclear, external limiting membrane, photoreceptor layer (rods "
"and cones), retinal pigment epithelium. Light crosses all ten "
"before reaching the photoreceptors - the retina is wired "
"backwards, with the fovea's pit shoving inner layers aside for a "
"clear path. Photoreceptor census: about 120 million rods for "
"night vision and 6 million cones for color and detail - a 20:1 "
"ratio. The fovea, 1.5 mm across, packs cones at 200,000 per "
"square millimeter: pi times 0.75 squared times 200,000 gives "
"about 353,000 foveal cones - the high-resolution sensor. The "
"cornea (five layers, avascular, transparent) and lens (crystallin "
"fibers, no organelles) form the optics; the choroid feeds the "
"outer retina; the optic nerve carries ganglion axons to the "
"brain, creating the blind spot where they exit."),
"how_it_works": (
"Retinal sections are read layer by layer from vitreous to "
"choroid, counting the ten: nuclear layers (cell bodies, dark) "
"alternate with plexiform layers (synapses, pale). Rods and cones "
"are distinguished by outer-segment shape and by position - "
"cones concentrated centrally, rods peripherally. The fovea is "
"recognized by the pit, the absence of inner layers, and dense "
"cone packing; the optic disc by the nerve-fiber exit and absent "
"photoreceptors. Corneal transparency is a structural call: "
"regular collagen lamellae, no vessels, dehydrated stroma. The "
"demo computes the sensor census: 120M rods to 6M cones (20:1), "
"and the foveal cone count from density times foveal area - "
"353,429 cones in the 1.5-mm high-acuity zone."),
"key_points": [
"Retina = 10 layers, read vitreous to choroid; light crosses all ten to reach photoreceptors.",
"120 million rods (night) : 6 million cones (color/detail) = 20:1.",
"Fovea 1.5 mm at 200,000 cones/mm2 = ~353,000 cones - the high-resolution sensor.",
"Cornea: 5 layers, avascular, regular collagen = transparent; lens: crystallin fibers, no organelles.",
"RPE (layer 10) nourishes photoreceptors and absorbs stray light.",
"Optic disc = nerve exit = blind spot; foveal pit clears inner layers from the light path."],
"requirements": [
"Ten-layer retinal reading in order, vitreous to choroid.",
"Rod vs cone identification by outer segment and retinal position.",
"Fovea vs optic disc recognition by pit/packing vs nerve exit.",
"The photoreceptor census arithmetic for sensor scale."],
"standards": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019 - ch. 24, eye.",
"Mescher AL. Junqueira's Basic Histology. 16th ed. McGraw-Hill; 2021 - ch. 23."],
"citations": [
"Ross MH, Pawlina W. Histology: A Text and Atlas. 8th ed. Wolters Kluwer; 2019.",
"Hogan MJ, Alvarado JA, Weddell JE. Histology of the Human Eye. Saunders; 1971.",
"Curcio CA et al. Human photoreceptor topography. J Comp Neurol. 1990;292:497-523."],
"sig_lens": (
"Signature lens: read the eye as an imaging sensor with "
"published pixel counts. The Signature reading specs the optics "
"(cornea, lens), the sensor array (120M rods, 6M cones), the "
"high-density region (353K foveal cones), and the wiring "
"(ganglion axons out the blind spot).")},
{
"key": "histopathology",
"name": "Histopathology: Reading Disease in Tissue",
"group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
"description": (
"Histopathology is histology turned diagnostic: the same stains "
"and sections, read for disease. The pathologist's vocabulary is "
"the vocabulary of deviation - hyperplasia (more cells), "
"hypertrophy (bigger cells), atrophy, metaplasia (one mature type "
"replacing another), dysplasia (disordered growth), neoplasia "
"(uncontrolled growth). Malignancy is read from architecture and "
"cytology: loss of polarity, nuclear pleomorphism, hyperchromasia, "
"prominent nucleoli, abnormal mitoses, invasion through basement "
"membranes. Grading and counting make it quantitative: mitotic "
"count per 10 high-power fields (each ~0.2 mm2, so 2 mm2 total - "
"25 mitoses means 12.5 per mm2), Ki-67 proliferation index (300 "
"positive of 1,000 nuclei = 30%), tumor margins in millimeters. "
"Inflammation is patterned: acute (neutrophils, edema), chronic "
"(lymphocytes, macrophages, fibrosis), granulomatous (epithelioid "
"macrophages, giant cells). Every diagnosis is an H&E reading "
"first, sharpened by special stains and IHC, and signed with the "
"understanding that the slide is a sample - the block, the gross, "
"and the clinical story complete it."),
"how_it_works": (
"The diagnostic workflow is fixed: verify the tissue and stain "
"quality, read at low power for architecture (is the normal "
"pattern preserved, expanded, or destroyed?), then high power for "
"cytology (nuclei, mitoses, differentiation). Compare against "
"normal histology of the same organ - the entire preceding ladder "
"is the reference library. Ancillary studies follow the question: "
"special stains for organisms and deposits, IHC panels for lineage "
"(cytokeratin vs vimentin vs S100 vs CD45 sorts most tumors into "
"carcinoma, sarcoma, melanoma, lymphoma), molecular tests for "
"therapeutic targets. The demo computes the counting metrics: "
"mitotic density from 25 mitoses per 10 HPF (2 mm2 -> 12.5/mm2) "
"and Ki-67 index from 300/1000 positive nuclei (30%) - the "
"numbers that grade tumors."),
"key_points": [
"Diagnosis = deviation from normal: hyperplasia, hypertrophy, metaplasia, dysplasia, neoplasia.",
"Malignancy criteria: lost polarity, pleomorphism, hyperchromasia, abnormal mitoses, invasion.",
"Mitotic count: 25 per 10 HPF (2 mm2) = 12.5/mm2; Ki-67: 300/1000 = 30% proliferation index.",
"Inflammation patterns: acute (neutrophils), chronic (lymphocytes/fibrosis), granulomatous (giant cells).",
"IHC lineage panels sort tumors: cytokeratin, vimentin, S100, CD45.",
"H&E first, always - ancillary stains sharpen the H&E reading, never replace it."],
"requirements": [
"Normal histology of the organ as the reference library.",
"Low-power architecture reading before high-power cytology.",
"Quantitative metrics: mitotic count, Ki-67, margins in mm.",
"Correlation with gross findings and clinical story."],
"standards": [
"Rosai J. Rosai and Ackerman's Surgical Pathology. 11th ed. Elsevier; 2017 - diagnostic standard.",
"Kumar V, Abbas AK, Aster JC. Robbins Basic Pathology. 10th ed. Elsevier; 2017."],
"citations": [
"Rosai J. Rosai and Ackerman's Surgical Pathology. 11th ed. Elsevier; 2017.",
"Kumar V, Abbas AK, Aster JC. Robbins and Cotran Pathologic Basis of Disease. 9th ed. Elsevier; 2014.",
"Elston CW, Ellis IO. Pathological prognostic factors in breast cancer I. Histopathology. 1991;19:403-410."],
"sig_lens": (
"Signature lens: treat diagnosis as anomaly detection against a "
"specified baseline. The Signature reading requires the normal "
"reference (this ladder), the deviation named in the controlled "
"vocabulary, and the counts that grade it - because a diagnosis "
"without numbers is an impression, and impressions do not "
"treat patients.")},
{
"key": "artifacts",
"name": "Artifacts: What the Slide Gets Wrong",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Every slide lies a little: artifacts are structures created by "
"processing, not by biology, and the skilled histologist "
"subtracts them before reading. Formalin pigment is brown "
"granular deposit from unbuffered fixative plus blood - prevent "
"with buffering, remove with picric acid. Shrinkage: tissues "
"lose 10-15 percent of linear dimension through processing, so "
"a 10-mm fresh biopsy measures about 8.7 mm on the slide - "
"margins and tumor sizes must be read with that correction. "
"Section compression shortens the section ~10 percent in the "
"cutting direction (a 5-um section effectively 4.5 um). Chatter "
"(vibration lines), knife nicks (parallel scratches), folds and "
"wrinkles, air bubbles under the coverslip, and cautery artifact "
"(charred crushed cells at surgical margins) each have a "
"signature. Floaters - foreign tissue fragments from the water "
"bath - are the classic false positive, caught by checking that "
"every fragment matches the case. The rule: know the artifact "
"catalog cold, so nothing processing-made is ever diagnosed."),
"how_it_works": (
"Artifact identification is pattern matching against the known "
"catalog: regular parallel lines mean knife or chatter (fix the "
"blade/angle); brown granules in bloody tissue mean formalin "
"pigment (buffer next time); tissue that does not belong means "
"floater (check the water bath protocol); crushed dark cells at "
"a margin mean cautery (read past it, note it). Shrinkage is "
"corrected arithmetically: measured size divided by 0.87 restores "
"the fresh dimension for margin assessment. Compression is "
"minimized by slow cutting and erased on the warm water bath. "
"The demo computes the corrections: 10 mm fresh at 13% "
"shrinkage -> 8.7 mm on slide; 5-um section at 10% compression "
"-> 4.5 um effective; and the inverse correction restoring "
"slide measurements to fresh dimensions."),
"key_points": [
"Artifacts are processing-made structures: know the catalog, diagnose none of them.",
"Formalin pigment (brown, bloody tissue): prevent by buffering, remove with picric acid.",
"Shrinkage ~13%: 10 mm fresh -> 8.7 mm on slide; correct margins by dividing by 0.87.",
"Section compression ~10%: 5 um cut -> 4.5 um effective; flatten on the warm bath.",
"Knife nicks, chatter, folds, bubbles, cautery crush - each has a signature pattern.",
"Floaters (foreign fragments from the water bath) are the classic false positive."],
"requirements": [
"The artifact catalog memorized: pigment, shrinkage, compression, chatter, folds, floaters, cautery.",
"Shrinkage correction applied to every measured margin.",
"Water-bath hygiene to prevent floaters.",
"Cautery artifact noted and read past, never diagnosed."],
"standards": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018 - ch. on artifacts.",
"Kiernan JA. Histological and Histochemical Methods. 5th ed. Scion; 2015."],
"citations": [
"Suvarna SK, Layton C, Bancroft JD, eds. Bancroft's Theory and Practice of Histological Techniques. 8th ed. Elsevier; 2018.",
"Kiernan JA. Histological and Histochemical Methods: Theory and Practice. 5th ed. Scion; 2015.",
"Werner M et al. Effect of formalin tissue fixation and processing on immunohistochemistry. Am J Surg Pathol. 2000;24:1016-1019."],
"sig_lens": (
"Signature lens: treat every slide as a measurement with a "
"known error budget. The Signature reading lists the artifacts "
"subtracted, applies the shrinkage correction to every "
"dimension, and never lets a processing signature enter the "
"diagnosis.")},
{
"key": "histomorphometry",
"name": "Histomorphometry: Measuring the Microscopic World",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Histomorphometry turns pictures into numbers: unbiased estimates "
"of volume, surface, length, and number from sections. The "
"foundation is Delesse's principle (1847): the area fraction of a "
"phase on a random section equals its volume fraction in the "
"tissue. Point counting implements it: overlay a grid, count hits "
"on the structure of interest, divide by total points - 23 hits "
"on 100 points means 23 percent volume fraction, no tracing "
"required. The Cavalieri estimator sums section areas times "
"section spacing for unbiased volumes; the disector counts "
"particles in a known volume for unbiased numbers; line "
"intercepts estimate surface area. Bone histomorphometry is the "
"mature clinical application: mineral apposition rate, osteoid "
"seam width, eroded surface - the dynamic indices of remodeling "
"that static slides cannot give. Stereology's power is its "
"unbiasedness: with systematic random sampling, the estimate is "
"correct on average regardless of the structure's shape - the "
"reason regulators and journals trust it."),
"how_it_works": (
"A stereology study starts with systematic random sampling: a "
"random start, then every nth section, so every part of the "
"organ has equal selection probability. Point grids (coarse for "
"volume, fine for surface) are applied with forbidden-line rules "
"at edges; the disector uses paired sections a known distance "
"apart and counts particle tops appearing in one but not the "
"other. Precision is designed, not hoped for: the coefficient of "
"error is predicted from the point and section counts, and the "
"study is sized to reach it. Modern practice is digital - whole-"
"slide images with software grids - but the estimators are "
"unchanged since Weibel. The demo performs a point count: a "
"10x10 grid with 23 hits on the phase of interest gives volume "
"fraction 0.23, with the binomial standard error sqrt(0.23*0.77/"
"100) = 0.042 computed alongside - the estimate plus its "
"honesty interval."),
"key_points": [
"Delesse principle: area fraction on random sections = volume fraction in tissue.",
"Point counting: 23 hits / 100 points = 23% volume fraction - no tracing needed.",
"Cavalieri (volumes), disector (numbers), line intercepts (surfaces) - the estimator toolkit.",
"Systematic random sampling makes estimates unbiased regardless of structure shape.",
"Bone histomorphometry: mineral apposition rate, osteoid seams, eroded surface - remodeling in numbers.",
"Report the coefficient of error with every estimate: 0.23 +/- 0.042 in the worked example."],
"requirements": [
"Systematic random sampling: random start, fixed interval through the organ.",
"The right estimator for the quantity: points for volume, disector for number.",
"Forbidden-line rules at counting-frame edges.",
"A designed coefficient of error, reported with the result."],
"standards": [
"Weibel ER. Stereological Methods. Vol. 1-2. Academic Press; 1979-1980 - the methods canon.",
"Howard CV, Reed MG. Unbiased Stereology. 3rd ed. Garland Science; 2010."],
"citations": [
"Weibel ER. Stereological Methods. Vol. 1: Practical Methods for Biological Morphometry. Academic Press; 1979.",
"Elias H, Hennig A, Schwartz DE. Stereology: applications to biomedical research. Physiol Rev. 1971;51:158-200.",
"Gundersen HJG et al. The new stereological tools: disector, fractionator, nucleator and point sampled intercepts. APMIS. 1988;96:857-881."],
"sig_lens": (
"Signature lens: treat stereology as the honest-measurement "
"discipline of histology. The Signature reading specifies the "
"sampling scheme, the estimator, and the coefficient of error "
"before the first point is counted - because a volume without "
"its error bar is a rumor with units.")},
{
"key": "digital",
"name": "Digital Histology: Whole-Slide Imaging and AI",
"group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
"description": (
"Whole-slide imaging digitizes the glass slide into a navigable "
"image pyramid: the scanner tiles the section at 0.25 micrometers "
"per pixel (40x equivalent) and stacks zoom levels so the "
"pathologist pans and zooms like a map. The files are enormous: "
"a 15 x 15 mm section at 0.25 um/px is 60,000 x 60,000 pixels - "
"3.6 billion pixels, 10.8 gigabytes at 3 bytes per pixel raw, "
"compressed ~30:1 to roughly 360 MB for storage and streaming. "
"Digital slides enable what glass cannot: instant consultation "
"across the world, quantitative image analysis (nuclear counts, "
"stain deconvolution, area fractions computed, not estimated), "
"and AI assistance - algorithms that pre-screen, count mitoses, "
"score IHC, and flag regions of interest for the pathologist. "
"The FDA has cleared whole-slide imaging for primary diagnosis, "
"and validation studies require the digital read to match the "
"glass read. The discipline's caution is encoded in the workflow: "
"AI proposes, the pathologist disposes - the signature on the "
"diagnosis remains human, and every algorithm is validated "
"against the H&E-read ground truth of this ladder."),
"how_it_works": (
"A scanning pipeline is specified end to end: barcode tracking "
"from block to slide to image, focus mapping (tissue-detection "
"plus focus points, since a 0.65-um depth of field forgives "
"nothing), 40x tile acquisition with overlap, stitching and "
"pyramid building, color calibration against a standard slide, "
"and archival storage with checksums. Image analysis pipelines "
"deconvolve stains (separating hematoxylin from DAB by color "
"vectors), segment nuclei by watershed or learning, and compute "
"features per object. AI models train on pathologist-annotated "
"regions with strict train/validation/test splits and site-"
"external validation - stain variation between labs being the "
"classic generalization failure. The demo computes the storage "
"budget: 60,000^2 px = 3.6e9 px, x3 bytes = 10.8 GB raw, /30 "
"compression = 360 MB per slide - the number every digital "
"pathology business plan starts from."),
"key_points": [
"Whole-slide imaging: 0.25 um/px tiles into a zoomable pyramid - the slide as a map.",
"15x15 mm at 0.25 um/px = 3.6 billion px = 10.8 GB raw ~ 360 MB compressed.",
"Digital enables teleconsultation, quantitative analysis, and AI assistance.",
"AI proposes, pathologist disposes: the diagnosis signature stays human.",
"Validation: digital read must match glass read; algorithms validated against H&E ground truth.",
"Pipeline spec: tracking, focus mapping, stitching, color calibration, checksummed archive."],
"requirements": [
"Focus mapping matched to the 0.65-um depth of field - focus is unforgiving.",
"Color calibration so stains read identically across scanners and sites.",
"Annotated ground truth with external validation for any AI claim.",
"Storage and bandwidth budgeted from the per-slide megabyte math."],
"standards": [
"Zarella MD et al. An overview of whole slide imaging. Clin Lab Med. 2018 - WSI practice.",
"FDA. Technical performance assessment of digital pathology whole slide imaging devices: guidance for industry. 2016."],
"citations": [
"Pantanowitz L et al. Validating whole slide imaging for diagnostic purposes in pathology. Arch Pathol Lab Med. 2013;137:1710-1722.",
"Mukhopadhyay S et al. Whole slide imaging versus microscopy for primary diagnosis in surgical pathology. Am J Surg Pathol. 2018;42:39-52.",
"Camp RL, Chung GG, Rimm DL. Automated subcellular localization and quantification of protein expression in tissue microarrays. Nat Med. 2002;8:1323-1327."],
"sig_lens": (
"Signature lens: treat the digital slide as a measurement "
"dataset with a specified acquisition chain. The Signature "
"reading logs focus map, color calibration, and compression "
"with the pixels - and treats every AI output as a proposal "
"requiring the human signature, validated against the glass "
"truth this ladder teaches.")}
]
