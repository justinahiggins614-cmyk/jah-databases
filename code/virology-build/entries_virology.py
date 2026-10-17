#!/usr/bin/env python3
"""Seed entries for the Virology field build (field #3, taxonomy order).

Public database `virology`: "The Virology Database" — real, fact-checked
virology: virus structure and classification (Baltimore), replication cycles,
bacteriophages, plant/animal/human viruses, emerging viruses,
vaccines/antivirals, diagnostic methods, epidemiology of viral disease, and lab
techniques (src public-harvest).

Signature database `virology-signature`: "The Virology Signature Database" —
his original Signature take on virology (src signature, titles suffixed
" (Signature Edition)", never presented as authentic public record).

Every record carries ladder_rank (1-10) + ladder_tier
(foundations/compounded/advanced); pages render in ladder order (simple ->
compounded -> complex).

Every record: description + how-it-works + key points + requirements +
standards + citations + working demonstration code (real, runnable, stdlib-only
Python; machine-executed OK).

Never the words "bat belt" anywhere. No website references. No Facebook.
"""

# Shared citation tails
CIT_PRINCIPLES = ("Flint, J., Racaniello, V. R., Rall, G. F., & Skalka, A. M. "
                  "(2020). 'Principles of Virology', 5th ed. ASM Press.")
CIT_FIELDS = ("Knipe, D. M. & Howley, P. M. (2022). 'Fields Virology', 7th ed. "
              "Wolters Kluwer.")
CIT_CANN = ("Cann, A. (2016). 'Principles of Molecular Virology', 6th ed. "
            "Academic Press.")
CIT_BALTIMORE = ("Baltimore, D. (1971). 'Expression of animal virus genomes.' "
                 "Bacteriological Reviews, 35(3), 235-241.")
CIT_ICTV = ("International Committee on Taxonomy of Viruses (ICTV). Current "
            "virus taxonomy release, ictv.global.")
CIT_CDC = "U.S. Centers for Disease Control and Prevention (CDC). Viral disease fact sheets."
CIT_WHO = "World Health Organization (WHO). Viral disease fact sheets."
CIT_STD = "Standard virology literature (peer-reviewed textbooks and journals)."
SIG_TAIL = ("Signature editions are original Signature interpretations of "
            "virology, written in the Signature system — clearly labeled "
            "Signature-made, never presented as authentic public records.")

ENTRIES = [
# ------------------------------------------------------------------ FOUNDATIONS
{
 "key": "what-is-virus", "name": "What Is a Virus: The Minimal Infectious Agent",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "A virus is the smallest known infectious agent: a package of genetic "
  "instructions — DNA or RNA — wrapped in a protein shell, and sometimes a "
  "lipid envelope, with no machinery of its own for making energy or building "
  "proteins. Viruses cannot reproduce by themselves. They must enter a living "
  "cell, hijack its protein-making and energy systems, and force it to build "
  "new virus particles. They are not cells, they are not alive by the usual "
  "biological definition, and they are far smaller than bacteria — most are "
  "20 to 300 nanometers across, invisible to ordinary light microscopes. Yet "
  "they are the most abundant biological entities on Earth: an estimated ten "
  "nonillion (10^31) virus particles exist in the oceans, soils, and "
  "atmosphere, and they infect every known form of cellular life — bacteria, "
  "archaea, fungi, plants, and animals."),
 "how_it_works": (
  "A virus works by delivering its genome into a host cell and exploiting the "
  "cell's own molecular machinery. The protein shell (capsid) protects the "
  "genome outside the cell and often carries the docking proteins that "
  "recognize the host. Once inside, the genome is read by the cell's "
  "ribosomes or by virus-carried enzymes to make viral proteins; those "
  "proteins copy the genome and assemble new shells around the copies. New "
  "particles then exit — either by bursting the cell or by budding through "
  "its membrane — and go on to infect more cells. Because viruses borrow the "
  "cell's machinery, they carry very little of their own: some viral genomes "
  "encode as few as three or four proteins."),
 "key_points": [
  "A virus is nucleic acid (DNA or RNA) in a protein coat — no ribosomes, no energy metabolism of its own.",
  "Viruses reproduce only inside living host cells; outside a host they are inert particles.",
  "Most viruses are 20-300 nanometers across — far smaller than bacteria.",
  "Viruses infect every domain of cellular life: bacteria, archaea, and eukaryotes.",
  "An estimated 10^31 virus particles exist on Earth, making them the most abundant biological entities known."],
 "requirements": [
  "No prior biology needed — this is the starting point of the ladder.",
  "Comfort with very small scales (nanometers) helps.",
  "Later tiers use high-school biology and basic algebra."],
 "standards": ["ICTV nomenclature for virus names", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_CANN],
 "demo_kind": "virus_scale",
 "sig_lens": (
  "The Signature reading treats the virus as the minimal engineered machine: "
  "a payload of instructions in a protective container, built to find a host "
  "factory and commandeer it. Every Signature virology record keeps that "
  "engineering discipline — payload, container, docking, factory takeover — "
  "while staying clearly labeled as his original interpretation."),
},
{
 "key": "virus-structure", "name": "Virus Structure: Capsids, Envelopes, and Genomes",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Every virus is built from the same three-part kit: a genome, a capsid, and "
  "optionally an envelope. The genome is the instruction set — DNA or RNA, "
  "single- or double-stranded, linear or circular. The capsid is the protein "
  "shell that protects it, assembled from repeating protein subunits called "
  "capsomers. Capsids come in two classic architectures: helical (subunits "
  "wound in a spiral around the genome, like tobacco mosaic virus) and "
  "icosahedral (twenty triangular faces forming a near-sphere, like "
  "adenovirus). An icosahedral capsid built with triangulation number T "
  "contains exactly 60 times T subunits. Some viruses add an envelope — a "
  "lipid membrane stolen from the host cell, studded with viral spike "
  "proteins that dock onto new host cells. Enveloped viruses include "
  "influenza, coronaviruses, and HIV; non-enveloped viruses include "
  "norovirus, poliovirus, and adenovirus."),
 "how_it_works": (
  "Structure serves function at every level. The capsid shields the genome "
  "from enzymes and the environment while presenting the docking proteins "
  "that recognize host-cell receptors — shape determines target. Because "
  "capsids are built from many copies of one or a few proteins, the virus "
  "genome stays small: it encodes the subunit once and the cell makes it "
  "thousands of times. Icosahedral geometry is the most economical way to "
  "enclose a volume with identical subunits, which is why it evolved "
  "repeatedly. The envelope, where present, is picked up as the new particle "
  "buds through a host membrane; its spike proteins then act as the keys "
  "that unlock the next cell. Destroy the envelope — with soap or alcohol — "
  "and most enveloped viruses fall apart."),
 "key_points": [
  "Three parts: genome (DNA or RNA), capsid (protein shell), and sometimes an envelope (lipid membrane).",
  "Capsids are helical (spiral) or icosahedral (20-faced); icosahedral capsids hold 60T subunits.",
  "The genome can be DNA or RNA, single- or double-stranded — this choice defines the Baltimore class.",
  "Enveloped viruses (flu, coronaviruses, HIV) bud through host membranes; non-enveloped ones (norovirus, polio) do not.",
  "Spike proteins on the surface are the docking keys that recognize host-cell receptors."],
 "requirements": [
  "The 'What Is a Virus' record above.",
  "Basic idea of proteins and membranes (high-school biology level)."],
 "standards": ["ICTV nomenclature for virus names", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_FIELDS],
 "demo_kind": "capsid_geometry",
 "sig_lens": (
  "The Signature reading treats the capsid as a container engineered for "
  "economy: one protein design, mass-produced, self-assembling into the "
  "strongest shape for the least genetic cost. Signature virology studies "
  "the container the way an engineer studies a pressure vessel."),
},
{
 "key": "virus-vs-cells", "name": "Viruses Are Not Cells: Viruses vs Bacteria vs Living Cells",
 "group": "Foundations", "ladder_rank": 1, "ladder_tier": "foundations",
 "description": (
  "Viruses are routinely confused with bacteria, but the two are built on "
  "opposite plans. A bacterium is a complete living cell: it has its own "
  "ribosomes, makes its own proteins, generates its own energy, and divides "
  "in two to reproduce. A virus has none of these — no ribosomes, no energy "
  "metabolism, no cell division. Antibiotics kill bacteria by attacking "
  "bacterial machinery (cell walls, bacterial ribosomes), which is why "
  "antibiotics do nothing against viruses: the targets simply are not "
  "there. Size tells the same story: a typical bacterium is about 2,000 "
  "nanometers long, while most viruses are 20 to 300 nanometers — small "
  "enough that many pass through filters that trap bacteria. Because "
  "viruses lack the machinery of life, biologists debate whether they are "
  "'alive' at all; they are best described as infectious agents that borrow "
  "life from their hosts."),
 "how_it_works": (
  "The difference shows up in every test. Put bacteria in nutrient broth and "
  "they grow and divide on their own; put viruses in the same broth and "
  "nothing happens — they need living host cells to multiply. A 0.22-micron "
  "laboratory filter sterilizes liquid of bacteria but lets most viruses "
  "through, which is how early virologists first proved viruses existed: "
  "the infectious agent passed through bacteria-proof filters. Treatment "
  "follows the same divide: antibiotics target bacterial structures, so "
  "they cannot touch viruses, while antivirals target virus-specific steps "
  "like genome copying or cell entry. Diagnosis also differs — bacterial "
  "infections can often be grown in culture dishes, while viruses must be "
  "grown in living cells, eggs, or detected by their genetic material."),
 "key_points": [
  "Bacteria are living cells with ribosomes and metabolism; viruses have neither.",
  "Antibiotics target bacterial machinery, so they are useless against viruses.",
  "Bacteria are ~2,000 nm; most viruses are 20-300 nm and pass bacteria-proof filters.",
  "Bacteria reproduce by dividing; viruses reproduce only by hijacking a host cell.",
  "Whether viruses count as 'alive' is debated — they borrow life from their hosts."],
 "requirements": [
  "The two records above.",
  "No mathematics needed for this record."],
 "standards": ["ICTV nomenclature for virus names", "SI units throughout"],
 "citations": [CIT_CANN, CIT_STD],
 "demo_kind": "size_filter",
 "sig_lens": (
  "The Signature reading frames the virus-versus-cell divide as hardware "
  "versus software: the cell is the computer, the virus is a program that "
  "needs a computer to run. Signature virology keeps the analogy honest — "
  "it is a teaching tool, not a claim about nature."),
},
{
 "key": "genome-types", "name": "Viral Genomes: DNA, RNA, Single and Double Stranded",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "A virus's genome — its complete instruction set — comes in more forms "
  "than any cellular genome. It can be DNA or RNA; single-stranded or "
  "double-stranded; linear or circular; one continuous piece or split into "
  "segments. Human and bacterial genomes are always double-stranded DNA, "
  "but viruses use all four combinations: double-stranded DNA (herpesviruses, "
  "smallpox), single-stranded DNA (parvoviruses), double-stranded RNA "
  "(rotaviruses), and single-stranded RNA (influenza, coronaviruses, HIV). "
  "RNA genomes are further divided into positive-sense (readable directly "
  "as messenger RNA, like coronaviruses) and negative-sense (the mirror "
  "image, which must first be copied into readable form, like influenza and "
  "Ebola). Genome size varies wildly: the smallest viral genomes are under "
  "2,000 letters long, while giant viruses carry over 2.5 million — larger "
  "than some bacterial genomes."),
 "how_it_works": (
  "The genome type dictates the virus's entire replication strategy, which "
  "is why David Baltimore's 1971 classification is organized around it. "
  "Every virus must produce messenger RNA that the host ribosome can read, "
  "because proteins can only be built from readable messages. A "
  "double-stranded DNA virus can use the cell's own machinery almost "
  "directly. A positive-sense RNA virus arrives already readable. But a "
  "negative-sense RNA virus must carry its own copying enzyme into the "
  "cell, since no cell owns an enzyme that reads negative-sense RNA. "
  "Single-stranded genomes are copied into double-stranded intermediates "
  "first; segmented genomes (like influenza's eight segments) allow whole "
  "segments to be swapped between strains, driving rapid evolution."),
 "key_points": [
  "Viral genomes can be DNA or RNA, single- or double-stranded, linear or circular, segmented or whole.",
  "Positive-sense RNA is directly readable by ribosomes; negative-sense RNA must be copied first.",
  "Genome type determines the replication strategy — the basis of the Baltimore classification.",
  "Segmented genomes (influenza's 8 segments) allow segment-swapping between strains.",
  "Viral genomes range from under 2,000 to over 2,500,000 letters long."],
 "requirements": [
  "Virus structure record above.",
  "Basic idea of DNA/RNA as instruction molecules."],
 "standards": ["ICTV nomenclature for virus names", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_BALTIMORE],
 "demo_kind": "genome_stats",
 "sig_lens": (
  "The Signature reading treats each genome type as a different storage "
  "format for the same job — deliver build instructions. Signature virology "
  "catalogues the formats the way an engineer catalogues file formats: "
  "what each one costs, what reader it needs, and what it enables."),
},
{
 "key": "baltimore", "name": "The Baltimore Classification: Seven Ways to Be a Virus",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "In 1971, David Baltimore proposed organizing all viruses not by what "
  "they look like or whom they infect, but by how they produce messenger "
  "RNA — the one step every virus must complete to make proteins. The "
  "result is seven classes. Class I: double-stranded DNA (herpesviruses, "
  "smallpox, adenoviruses). Class II: single-stranded DNA (parvoviruses). "
  "Class III: double-stranded RNA (rotaviruses). Class IV: positive-sense "
  "single-stranded RNA (coronaviruses, poliovirus, hepatitis C). Class V: "
  "negative-sense single-stranded RNA (influenza, Ebola, rabies, measles). "
  "Class VI: single-stranded RNA that reverse-transcribes into DNA "
  "(retroviruses, including HIV). Class VII: double-stranded DNA viruses "
  "that replicate through an RNA intermediate (hepadnaviruses, including "
  "hepatitis B). The classification predicts the enzymes a virus must "
  "carry and the drugs that can stop it — reverse transcriptase inhibitors, "
  "for example, work precisely against Class VI."),
 "how_it_works": (
  "The classification works because the path from genome to messenger RNA "
  "is the narrowest bottleneck in every viral life cycle. Host cells can "
  "read double-stranded DNA and positive-sense RNA directly, so Class I and "
  "IV viruses need the least extra equipment. Classes III and V must bring "
  "their own RNA-copying enzyme (RNA-dependent RNA polymerase) because "
  "cells have no enzyme that reads those templates. Classes VI and VII "
  "must bring reverse transcriptase, an enzyme no cell normally uses to "
  "copy RNA into DNA. Once you know a virus's class, you can predict its "
  "replication steps, which enzymes are drug targets, and which laboratory "
  "tricks will detect it. Modern taxonomy (ICTV) organizes viruses by "
  "evolutionary relationships, but the Baltimore classes remain the "
  "standard functional map taught in every virology course."),
 "key_points": [
  "Seven classes organized by the path each genome takes to messenger RNA.",
  "Class I dsDNA, II ssDNA, III dsRNA, IV +ssRNA, V -ssRNA, VI ssRNA-RT, VII dsDNA-RT.",
  "Classes III and V must carry their own RNA-copying enzyme; classes VI and VII carry reverse transcriptase.",
  "The class predicts drug targets — e.g. reverse transcriptase inhibitors hit Class VI.",
  "Baltimore (1971) remains the standard functional map alongside ICTV evolutionary taxonomy."],
 "requirements": [
  "Viral genomes record above.",
  "Basic idea of messenger RNA as a readable instruction."],
 "standards": ["Baltimore class notation (I-VII)", "ICTV nomenclature"],
 "citations": [CIT_BALTIMORE, CIT_PRINCIPLES],
 "demo_kind": "baltimore_lookup",
 "sig_lens": (
  "The Signature reading treats the seven Baltimore classes as seven "
  "machine architectures for one job — get the factory to read your "
  "instructions. Signature virology studies each architecture's cost: "
  "what the virus must pack, what it can borrow, and where it is "
  "vulnerable."),
},
{
 "key": "measuring-viruses", "name": "Measuring Viruses: Size, Scale, and Microscopy",
 "group": "Foundations", "ladder_rank": 2, "ladder_tier": "foundations",
 "description": (
  "Viruses live below the resolving power of light microscopes, and that "
  "single fact shaped the entire history of virology. A light microscope "
  "cannot distinguish details smaller than about 200 nanometers — the Abbe "
  "diffraction limit for visible light — while most viruses span 20 to 300 "
  "nanometers. Early virologists therefore studied viruses indirectly: by "
  "their ability to pass bacteria-proof filters, by the diseases they "
  "caused, and by their effects on cells. The electron microscope, which "
  "uses electrons with wavelengths thousands of times shorter than visible "
  "light, finally let scientists see viruses directly, resolving details "
  "below one nanometer. Today, cryo-electron microscopy freezes viruses in "
  "vitrified ice and reconstructs their three-dimensional structures at "
  "near-atomic resolution, revealing exactly how spike proteins dock onto "
  "cell receptors. X-ray crystallography has solved the atomic structures "
  "of many small viruses, and modern light-based super-resolution methods "
  "can track single virus particles inside living cells."),
 "how_it_works": (
  "Resolution is set by wavelength: the smallest resolvable detail is "
  "roughly the wavelength divided by twice the numerical aperture (Abbe's "
  "law). Visible light at 550 nanometers with the best oil-immersion lens "
  "bottoms out near 200 nanometers — larger than a poliovirus. Electrons "
  "accelerated through 100,000 volts have wavelengths around 0.004 "
  "nanometers, so electron microscopes resolve virus particles easily, "
  "though samples must be stained, frozen, or dried and viewed in vacuum. "
  "Cryo-electron microscopy improves on this by flash-freezing viruses in "
  "a thin layer of glass-like ice, preserving their natural shape; "
  "thousands of particle images are then computationally averaged into a "
  "3D map. The resulting structures guide vaccine design (showing "
  "antibodies exactly what the spike looks like) and drug design (showing "
  "where inhibitors can jam the machinery)."),
 "key_points": [
  "Light microscopes resolve ~200 nm; most viruses are 20-300 nm, so they were first studied indirectly.",
  "The electron microscope (electron wavelength ~0.004 nm) made viruses directly visible.",
  "Cryo-electron microscopy now resolves virus structures at near-atomic detail.",
  "Abbe's law sets the limit: resolution ~ wavelength / (2 x numerical aperture).",
  "Atomic structures of spikes guide vaccines and antiviral drug design."],
 "requirements": [
  "Virus structure record above.",
  "Basic algebra (dividing wavelengths)."],
 "standards": ["SI units throughout", "Abbe diffraction formalism"],
 "citations": [CIT_FIELDS, CIT_STD],
 "demo_kind": "microscope_resolution",
 "sig_lens": (
  "The Signature reading treats imaging as metrology: you cannot engineer "
  "what you cannot measure. Signature virology respects the instrument "
  "chain — filter, electron beam, frozen particle, computed map — as the "
  "ladder that made the invisible buildable."),
},
{
 "key": "virus-taxonomy", "name": "Virus Taxonomy: The ICTV Orders and Families",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "The International Committee on Taxonomy of Viruses (ICTV) maintains the "
  "official classification of viruses, organized by evolutionary "
  "relationships like the taxonomy of living things: realm, kingdom, "
  "phylum, class, order, family, genus, species. Most familiar viruses sit "
  "in a handful of orders and families. Coronaviruses belong to the order "
  "Nidovirales and family Coronaviridae. Influenza viruses are family "
  "Orthomyxoviridae. Herpesviruses are order Herpesvirales. Retroviruses "
  "(including HIV) are family Retroviridae. Filoviruses (Ebola, Marburg) "
  "are order Mononegavirales. Bacteriophages that infect bacteria dominate "
  "the class Caudoviricetes — the tailed phages. Unlike cellular taxonomy, "
  "virus taxonomy is still being rewritten rapidly as metagenomic "
  "sequencing discovers thousands of new viruses, and many newly found "
  "viruses are known only from their sequences. Species names are now "
  "written in binomial form (e.g. the species containing SARS-CoV-2 is "
  "Betacoronavirus pandemicum)."),
 "how_it_works": (
  "ICTV taxonomy is built from genome sequences and shared gene sets: "
  "viruses that share core replication genes and genome organization are "
  "grouped together, regardless of whom they infect. This is why "
  "bacteriophages, plant viruses, and animal viruses can sit in related "
  "families — the classification tracks the virus's ancestry, not its "
  "host. The Baltimore classes cut across ICTV taxonomy: they describe "
  "function (how the genome becomes messenger RNA) while ICTV describes "
  "evolution (who is related to whom). In practice, virologists use both: "
  "the family name tells you a virus's relatives and typical traits, while "
  "the Baltimore class tells you how it replicates and what drugs might "
  "work. Databases of viral sequences (such as GenBank) annotate every "
  "entry with both systems."),
 "key_points": [
  "The ICTV classifies viruses by evolutionary relationships: realm down to species.",
  "Familiar families: Coronaviridae, Orthomyxoviridae, Herpesviridae, Retroviridae, Filoviridae.",
  "Tailed bacteriophages dominate the class Caudoviricetes.",
  "Baltimore classes describe function; ICTV describes ancestry — virologists use both.",
  "Metagenomic sequencing is rapidly rewriting the taxonomy with sequence-only discoveries."],
 "requirements": [
  "Baltimore classification record above.",
  "Basic idea of biological classification (family, genus, species)."],
 "standards": ["ICTV taxonomy release", "Binomial species nomenclature"],
 "citations": [CIT_ICTV, CIT_PRINCIPLES],
 "demo_kind": "taxonomy_tree",
 "sig_lens": (
  "The Signature reading treats taxonomy as a parts catalog: know the "
  "family and you know the platform — its genome format, its replication "
  "habits, its weak points. Signature virology keeps the catalog current "
  "because a misfiled part is an engineering error."),
},
{
 "key": "tropism", "name": "Host Range and Tropism: Why Viruses Infect What They Infect",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Tropism is the rule that each virus infects only certain hosts, certain "
  "tissues, and certain cell types — and it is decided almost entirely at "
  "the cell surface. A virus can only enter a cell that carries the right "
  "receptor protein, the molecular lock its spike protein key fits. HIV's "
  "spike recognizes CD4 plus a co-receptor, which is why it infects helper "
  "T cells. SARS-CoV-2's spike recognizes ACE2, abundant in airway and "
  "other tissues. Influenza's hemagglutinin recognizes sialic acids, and "
  "the exact linkage (alpha-2,6 in human upper airways versus alpha-2,3 in "
  "bird guts) is a major reason bird flu strains infect humans poorly. "
  "Receptor distribution explains tissue tropism: rhinoviruses prefer the "
  "cooler nasal passages, poliovirus targets motor neurons, hepatitis "
  "viruses target liver cells. Host range can expand when mutations alter "
  "the spike's fit — the central event in zoonotic spillover."),
 "how_it_works": (
  "Entry is a molecular handshake with measurable strength. The spike "
  "protein and receptor bind with an affinity described by the dissociation "
  "constant Kd: a smaller Kd means tighter binding. At receptor "
  "concentrations near Kd, about half the spikes are bound; far above Kd, "
  "nearly all are. After binding, many viruses need a second trigger — a "
  "co-receptor, or the acidic interior of an endosome — to fuse membranes "
  "and release the genome. Tropism can also be set after entry: even if a "
  "virus gets inside the wrong cell, it may fail because the cell lacks a "
  "needed factor or carries a restriction factor that blocks it. "
  "Laboratory host-range studies map these locks systematically, which is "
  "how scientists assess whether an animal virus could plausibly infect "
  "human cells."),
 "key_points": [
  "Tropism is set mainly by receptor match: spike protein key must fit the cell's receptor lock.",
  "HIV uses CD4; SARS-CoV-2 uses ACE2; influenza uses sialic acids — the linkage type sets host range.",
  "Receptor distribution across tissues explains which organs a virus attacks.",
  "Binding strength is quantified by Kd; co-receptors and pH triggers add further specificity.",
  "Spike mutations that improve fit to human receptors drive zoonotic spillover."],
 "requirements": [
  "Virus structure record (spike proteins).",
  "Basic idea of proteins binding (lock and key)."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_PRINCIPLES],
 "demo_kind": "binding_affinity",
 "sig_lens": (
  "The Signature reading treats tropism as an addressing system: every "
  "virus carries a destination address written in protein, and only cells "
  "broadcasting the matching address can receive it. Signature virology "
  "maps the address space because misaddressed delivery is how pandemics "
  "begin."),
},
{
 "key": "transmission", "name": "How Viruses Spread: Transmission Routes",
 "group": "Foundations", "ladder_rank": 3, "ladder_tier": "foundations",
 "description": (
  "Between hosts, viruses travel by a small set of well-studied routes. "
  "Respiratory transmission moves viruses in droplets and aerosols expelled "
  "by coughing, sneezing, talking, and breathing (influenza, SARS-CoV-2, "
  "rhinoviruses). Fecal-oral transmission moves gut viruses through "
  "contaminated water, food, or hands (norovirus, poliovirus, hepatitis A "
  "and E). Blood-borne transmission moves viruses through transfusions, "
  "shared needles, or needlesticks (HIV, hepatitis B and C). Sexual "
  "transmission moves viruses through intimate contact (HIV, herpesviruses, "
  "HPV). Vector-borne transmission uses arthropods — mosquitoes and ticks "
  "— as flying syringes (Zika, dengue, yellow fever, West Nile). Vertical "
  "transmission passes virus from mother to child during pregnancy, birth, "
  "or breastfeeding (rubella, Zika, HIV without treatment). Fomites — "
  "contaminated surfaces — play a supporting role for hardy non-enveloped "
  "viruses like norovirus, while enveloped viruses generally survive "
  "poorly on surfaces. Every control measure in public health — masks, "
  "handwashing, safe water, condoms, bed nets, screening blood — targets "
  "one of these routes."),
 "how_it_works": (
  "Each route is a chain with breakable links: shedding from the infected "
  "host, survival in the environment, and successful entry into the next "
  "host. Respiratory viruses optimize for shedding in airway secretions and "
  "survive best in cool, dry air; this is why temperate flu seasons peak in "
  "winter. Gut viruses optimize for environmental toughness — non-enveloped "
  "capsids that survive stomach acid and persist on surfaces. Blood-borne "
  "viruses must reach high concentrations in blood and survive outside the "
  "body briefly in a needle or transfusion bag. Vector-borne viruses must "
  "replicate inside the mosquito itself before the bite becomes infectious, "
  "which is why their geography follows the mosquito's. Epidemiologists "
  "quantify each route's contribution so interventions can be aimed where "
  "they break the most chains per dollar."),
 "key_points": [
  "Six main routes: respiratory, fecal-oral, blood-borne, sexual, vector-borne, and vertical (mother-to-child).",
  "Enveloped viruses are fragile outside the body; non-enveloped gut viruses persist on surfaces.",
  "Every public-health control targets a route: masks, handwashing, safe water, condoms, bed nets, blood screening.",
  "Vector-borne viruses must replicate in the mosquito before transmission — geography follows the vector.",
  "Each route is a chain of shedding, survival, and entry — break any link to stop spread."],
 "requirements": [
  "Host range and tropism record above.",
  "No mathematics needed for this record."],
 "standards": ["CDC/WHO transmission terminology", "SI units throughout"],
 "citations": [CIT_CDC, CIT_WHO],
 "demo_kind": "transmission_routes",
 "sig_lens": (
  "The Signature reading treats each transmission route as a logistics "
  "channel with known failure points. Signature virology studies the "
  "channels because every defense — every mask, filter, and screen — is "
  "a deliberate break in a specific channel."),
},
{
 "key": "lytic-cycle", "name": "The Lytic Cycle: Hijack, Copy, Burst",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "The lytic cycle is the virus's blitz strategy: enter a cell, take over, "
  "mass-produce new particles, and burst the cell to release them. It runs "
  "in five textbook stages. Attachment: the virus docks onto the host "
  "cell's receptor. Penetration: the genome (sometimes the whole particle) "
  "enters the cell. Biosynthesis: the cell's machinery is redirected to "
  "copy viral genomes and manufacture viral proteins — host protein "
  "synthesis is often shut down. Assembly (maturation): new genomes are "
  "packaged into new capsids. Release: the cell ruptures (lysis), spilling "
  "hundreds or thousands of new virions — the burst size. Bacteriophage T4 "
  "bursts E. coli with about 100 to 200 new phages per cell in under half "
  "an hour. The lytic cycle is fast and lethal to the host cell, which is "
  "why lytic viruses cause acute, short, often dramatic infections — and "
  "why lytic bacteriophages are candidates for antibacterial therapy."),
 "how_it_works": (
  "Timing is everything. Immediately after entry, early genes are expressed: "
  "these encode the takeover crew — proteins that shut off host defenses, "
  "degrade host DNA, and build the replication factories. Then late genes "
  "produce the structural parts: capsid subunits and packaging motors. "
  "Genome copies are threaded into empty capsid shells (procapsids), often "
  "with a portal motor that burns ATP to stuff DNA against enormous "
  "pressure — inside phage T4's head, DNA is packed nearly as densely as "
  "in a crystal. Release is triggered by holin and lysozyme-like enzymes "
  "that punch holes in the cell membrane and chew through the cell wall. "
  "The burst size — progeny per cell — times the number of infected cells "
  "sets the exponential pace: one infected cell yielding 100 virions that "
  "each infect new cells compounds with terrifying speed."),
 "key_points": [
  "Five stages: attachment, penetration, biosynthesis, assembly, release by lysis.",
  "Early genes run the takeover; late genes build the structural parts.",
  "Burst size (e.g. ~100-200 for phage T4) times infected cells drives exponential growth.",
  "Lysis kills the host cell — lytic infections are acute and short.",
  "Lytic phages are the basis of phage therapy against bacterial infections."],
 "requirements": [
  "Viral genomes record (genome copying idea).",
  "Basic algebra for the burst-size compounding demo."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_CANN],
 "demo_kind": "lytic_burst",
 "sig_lens": (
  "The Signature reading treats the lytic cycle as a manufacturing blitz: "
  "retool the factory, run three shifts, then demolish the building to "
  "ship the product. Signature virology studies the blitz because speed "
  "is the weapon — and the vulnerability, since every fast step is a "
  "target."),
},
{
 "key": "lysogenic-cycle", "name": "The Lysogenic Cycle: The Quiet Integration",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "The lysogenic cycle is the virus's stealth strategy: instead of killing "
  "the cell, the viral genome slips into the host's own chromosome and "
  "rides along silently as the cell divides. A bacteriophage that does "
  "this is called temperate, and the integrated viral genome is a "
  "prophage; the host carrying it is a lysogen. The classic example is "
  "phage lambda in E. coli. The decision between the lytic blitz and "
  "lysogenic silence is made by a genetic switch: the cI repressor protein "
  "maintains lysogeny by blocking lytic genes, while the Cro protein "
  "pushes toward lysis. When the host cell is damaged — by ultraviolet "
  "light, for instance — the switch flips: the prophage cuts itself out "
  "of the chromosome and launches the lytic cycle. Lysogeny is not always "
  "harmless to the host: prophages sometimes carry toxin genes, which is "
  "how otherwise ordinary bacteria like Vibrio cholerae and "
  "Corynebacterium diphtheriae became killers."),
 "how_it_works": (
  "Integration is performed by the phage integrase enzyme, which splices "
  "the circular phage genome into a specific attachment site on the "
  "bacterial chromosome with single-base precision. Once integrated, the "
  "cI repressor binds the phage's own promoters and keeps every lytic "
  "gene switched off; the prophage is replicated passively each time the "
  "host divides, at zero cost to the phage. The SOS response is the trip "
  "wire: DNA damage activates the host's RecA protein, which forces cI to "
  "cut itself, lifting repression. Within minutes the prophage excises, "
  "replicates, and lyses the cell. This switch — two repressors mutually "
  "antagonizing each other — became the founding model of genetic "
  "regulatory circuits in all of molecular biology."),
 "key_points": [
  "Temperate phages integrate as prophages and replicate silently with the host chromosome.",
  "The cI/Cro genetic switch decides between lysogeny and lysis.",
  "DNA damage flips the switch: the prophage excises and goes lytic.",
  "Prophages can carry toxin genes that turn harmless bacteria into pathogens.",
  "The lambda switch is the founding model of genetic regulatory circuits."],
 "requirements": [
  "Lytic cycle record above (the contrast is the point).",
  "Basic idea of genes being switched on and off."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_STD],
 "demo_kind": "lysogeny_switch",
 "sig_lens": (
  "The Signature reading treats lysogeny as a sleeper-agent protocol: "
  "embed the code, keep it dormant, activate on a distress signal. "
  "Signature virology studies the switch because the quietest systems "
  "are the hardest to detect — and the most instructive about control."),
},
{
 "key": "viral-entry", "name": "Viral Entry: Attachment, Fusion, and Uncoating",
 "group": "Foundations", "ladder_rank": 4, "ladder_tier": "foundations",
 "description": (
  "Entry is the most vulnerable moment in a virus's life — the few minutes "
  "when it must cross from the outside world into a cell — and therefore "
  "one of the best drug targets. It unfolds in three acts. Attachment: "
  "spike proteins on the virion bind receptors on the cell surface, a "
  "reversible docking governed by binding affinity. Penetration: the "
  "genome crosses the membrane. Enveloped viruses do this by membrane "
  "fusion — their envelope merges with the cell membrane (at the surface "
  "or inside an endosome), spilling the genome inside; non-enveloped "
  "viruses punch through or are swallowed by endocytosis and then escape. "
  "Uncoating: the capsid comes apart, releasing the genome where it can "
  "be read — the nucleus for most DNA viruses, the cytoplasm for most RNA "
  "viruses. Each act is a potential blockade: antibodies that cover the "
  "spike prevent attachment; fusion inhibitors (like enfuvirtide for HIV) "
  "jam the fusion machinery; endosomal pH blockers trap viruses that need "
  "acid to escape."),
 "how_it_works": (
  "Fusion is a protein machine doing mechanical work. Class I fusion "
  "proteins (influenza hemagglutinin, coronavirus spike, HIV gp41) start "
  "folded like a loaded spring; receptor binding or low pH triggers a "
  "dramatic refolding that harpoons the target membrane with a fusion "
  "peptide, then folds back on itself, dragging the two membranes together "
  "until they merge. The energy released by refolding pays for bending "
  "membranes. Kinetically, attachment follows mass-action binding — the "
  "fraction of bound virus rises with receptor concentration and affinity "
  "— while fusion is effectively irreversible once triggered. Uncoating "
  "is often coupled to the destination: adenovirus sheds its capsid "
  "progressively as it rides microtubules to the nuclear pore, delivering "
  "the genome through the pore like thread through a needle."),
 "key_points": [
  "Three acts: attachment (reversible docking), penetration (membrane crossing), uncoating (genome release).",
  "Enveloped viruses enter by membrane fusion; non-enveloped viruses use endocytosis or membrane penetration.",
  "Fusion proteins are spring-loaded machines that refold to merge membranes.",
  "DNA viruses usually uncoat at the nucleus; RNA viruses usually uncoat in the cytoplasm.",
  "Each act is a drug target: attachment antibodies, fusion inhibitors, uncoating blockers."],
 "requirements": [
  "Virus structure (spikes) and tropism (receptors) records.",
  "Basic algebra for the binding-kinetics demo."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_PRINCIPLES],
 "demo_kind": "entry_kinetics",
 "sig_lens": (
  "The Signature reading treats entry as a breaching operation: recon "
  "(find the receptor), breach (fuse the wall), deploy (release the "
  "payload). Signature virology studies the breach because every "
  "fortress's weakest moment is the gate — in both directions."),
},
# ------------------------------------------------------------------ COMPOUNDED
{
 "key": "replication-strategies", "name": "Replication Strategies of the Seven Baltimore Classes",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Once inside, each Baltimore class runs its own replication playbook — "
  "but every playbook serves the same two goals: make messenger RNA the "
  "ribosome can read, and make new genome copies. Class I (dsDNA): the "
  "genome enters the nucleus and the cell's own machinery transcribes and "
  "replicates it, almost like a cellular gene. Class II (ssDNA): the "
  "single strand is first converted to double-stranded form, then follows "
  "the Class I path. Class III (dsRNA): the virus carries its polymerase "
  "inside the particle and transcribes mRNA from the dsRNA while keeping "
  "the genome hidden from cell defenses. Class IV (+ssRNA): the genome is "
  "itself mRNA — ribosomes start translating it immediately, first making "
  "the polymerase, which then copies the genome via a negative-sense "
  "intermediate. Class V (-ssRNA): the virus must carry its polymerase "
  "into the cell to transcribe mRNA from the negative-sense genome. "
  "Class VI (ssRNA-RT): reverse transcriptase converts the RNA genome "
  "into double-stranded DNA, which integrates into the host chromosome "
  "(HIV's provirus). Class VII (dsDNA-RT): the DNA is transcribed to RNA, "
  "which is reverse-transcribed back into DNA for packaging (hepatitis B)."),
 "how_it_works": (
  "The playbooks differ because cells only supply certain enzymes. Cells "
  "provide DNA-dependent DNA and RNA polymerases, so Class I and II "
  "viruses can freeload. No cell provides an RNA-dependent RNA polymerase "
  "or a reverse transcriptase, so Classes III through VII must encode "
  "their own — and Classes III and V must physically carry the enzyme "
  "inside the virion, since their first step cannot wait for translation. "
  "Replication always passes through a complementary intermediate: "
  "positive-sense genomes are copied via negative-sense intermediates "
  "and vice versa. Double-stranded intermediates of RNA viruses are "
  "danger signals the cell watches for, so many RNA viruses hide "
  "replication inside membrane-wrapped compartments. Antiviral drugs slot "
  "neatly into this map: nucleoside analogues jam the viral polymerases "
  "of Classes IV, V, and VI precisely because those polymerases are "
  "virus-specific."),
 "key_points": [
  "Every class must produce readable mRNA and new genome copies; the routes differ.",
  "Classes I-II freeload on cellular enzymes; classes III-VII encode their own polymerases.",
  "Classes III and V carry their polymerase inside the virion — the first step cannot wait.",
  "Replication passes through complementary intermediates, hidden from cell defenses.",
  "Virus-specific polymerases are prime antiviral targets (nucleoside analogues)."],
 "requirements": [
  "Baltimore classification and viral genomes records.",
  "Comfort with the idea of complementary copying."],
 "standards": ["Baltimore class notation (I-VII)", "ICTV nomenclature"],
 "citations": [CIT_BALTIMORE, CIT_PRINCIPLES, CIT_FIELDS],
 "demo_kind": "replication_playbook",
 "sig_lens": (
  "The Signature reading treats the seven playbooks as seven boot "
  "sequences: same destination (running code in the factory), different "
  "startup routines depending on what the disk format allows. Signature "
  "virology charts every boot sequence because the startup is where "
  "interception is cheapest."),
},
{
 "key": "reverse-transcription", "name": "Reverse Transcription: RNA Turned Back into DNA",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "Reverse transcription is the molecular U-turn at the heart of "
  "retroviruses: an enzyme called reverse transcriptase reads an RNA "
  "template and synthesizes DNA from it, reversing the cell's normal "
  "DNA-to-RNA flow. Its discovery in 1970 (Temin and Baltimore, Nobel "
  "Prize 1975) overturned the 'central dogma' that genetic information "
  "flows only from DNA to RNA to protein. HIV, the best-studied "
  "retrovirus, carries two copies of its positive-sense RNA genome plus "
  "reverse transcriptase inside each particle. After entry, the enzyme "
  "builds a DNA copy of the RNA, degrades the RNA strand, synthesizes the "
  "second DNA strand, and the resulting double-stranded DNA is integrated "
  "into the host chromosome by integrase — becoming a permanent provirus. "
  "Reverse transcriptase is famously sloppy, with no proofreading: it "
  "makes roughly one mistake per genome copied, which is why HIV evolves "
  "within a single patient and escapes immune pressure and drugs. "
  "Hepatitis B uses the same enzyme in reverse order (Class VII): it "
  "transcribes its DNA into RNA, then reverse-transcribes it back into "
  "DNA for packaging."),
 "how_it_works": (
  "Reverse transcriptase performs three jobs with one protein: it is an "
  "RNA-dependent DNA polymerase (writes DNA from RNA), it carries an "
  "RNase H activity (chews away the RNA template after copying), and it "
  "is a DNA-dependent DNA polymerase (fills in the second DNA strand). "
  "The reaction needs a primer — HIV uses a stolen host transfer RNA — "
  "and proceeds through two template 'jumps' where the growing DNA strand "
  "hops from one end of the template to the other, a maneuver that "
  "duplicates the long terminal repeats (LTRs) flanking the genome. "
  "Because the enzyme lacks the 3'-to-5' proofreading exonuclease that "
  "cellular DNA polymerases use, errors accumulate at about 10^-4 per "
  "base — thousands of times the cellular rate. Antiretroviral therapy "
  "exploits this enzyme two ways: nucleoside analogues (like AZT) get "
  "incorporated and terminate the chain, while non-nucleoside inhibitors "
  "bind a pocket near the active site and jam the mechanism."),
 "key_points": [
  "Reverse transcriptase copies RNA into DNA — reversing the normal information flow (Nobel Prize 1975).",
  "HIV's DNA copy integrates into the host chromosome as a permanent provirus.",
  "The enzyme has no proofreading: ~1 error per genome copied, driving rapid evolution.",
  "It performs three jobs: RNA-directed DNA synthesis, RNA degradation, DNA-directed DNA synthesis.",
  "Major drug target: chain-terminating nucleoside analogues and non-nucleoside inhibitors."],
 "requirements": [
  "Replication strategies record (Class VI/VII).",
  "Basic idea of complementary base pairing."],
 "standards": ["IUPAC nucleic acid notation", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_FIELDS],
 "demo_kind": "revtranscribe",
 "sig_lens": (
  "The Signature reading treats reverse transcription as a format "
  "converter: translate the payload from the cell's read-only format "
  "into its permanent archive format, then file it in the archive "
  "itself. Signature virology studies the converter because format "
  "changes are where errors — and opportunities — concentrate."),
},
{
 "key": "rdrp", "name": "RNA-Dependent RNA Polymerase: The Virus's Copy Machine",
 "group": "Compounded", "ladder_rank": 5, "ladder_tier": "compounded",
 "description": (
  "The RNA-dependent RNA polymerase — RdRp — is the engine of every RNA "
  "virus that does not reverse-transcribe: Classes III, IV, and V. No "
  "cell on Earth owns this enzyme, because cells never need to copy RNA "
  "from an RNA template. That makes RdRp purely viral: a drug that jams "
  "it harms the virus without touching any human enzyme, which is why "
  "RdRp inhibitors are among the most sought-after antivirals "
  "(remdesivir, for example, targets the coronavirus RdRp). Structurally, "
  "RdRps share a cupped right-hand shape — fingers, palm, and thumb "
  "domains — conserved across wildly different viruses, betraying their "
  "ancient common ancestry. Like reverse transcriptase, most RdRps lack "
  "proofreading, so RNA viruses mutate furiously: roughly one mutation "
  "per genome per replication for many. Coronaviruses are the striking "
  "exception — their RdRp complex carries a proofreading exonuclease, "
  "which is part of why they can maintain the largest known RNA genomes "
  "at around 30,000 letters."),
 "how_it_works": (
  "RdRp reads an RNA template and polymerizes a complementary RNA strand, "
  "using the same Watson-Crick pairing as cellular polymerases but with "
  "ribonucleotides throughout. Initiation is the hard part: some RdRps "
  "start de novo (from nothing, e.g. hepatitis C), others need a primer — "
  "influenza's polymerase famously 'snatches' caps from host messenger "
  "RNAs to prime its own transcription. Elongation then proceeds at "
  "hundreds of nucleotides per second. Fidelity is set by how tightly "
  "the active site discriminates correct versus incorrect nucleotides; "
  "without proofreading, the error rate sits near 10^-4 to 10^-5 per "
  "base — meaning a 10,000-letter genome picks up about one mutation per "
  "copy. Nucleoside-analogue drugs exploit this: the polymerase "
  "incorporates the fake building block and stalls (remdesivir causes "
  "delayed chain termination in coronaviruses)."),
 "key_points": [
  "RdRp copies RNA from RNA templates — an enzyme no cell owns, making it a clean drug target.",
  "Conserved right-hand (fingers-palm-thumb) structure reveals ancient common ancestry.",
  "Most RdRps lack proofreading: ~1 mutation per genome per replication for many RNA viruses.",
  "Coronaviruses are the exception — a proofreading exonuclease lets them keep 30,000-letter genomes.",
  "Nucleoside analogues (e.g. remdesivir) jam RdRp by stalling chain elongation."],
 "requirements": [
  "Replication strategies record.",
  "Basic algebra for the mutation-rate demo."],
 "standards": ["IUPAC nucleic acid notation", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_PRINCIPLES],
 "demo_kind": "rdrp_errors",
 "sig_lens": (
  "The Signature reading treats RdRp as a high-speed copier with the "
  "spell-checker removed: fast, cheap, and deliberately error-prone, "
  "because errors are the search strategy. Signature virology studies "
  "the copier's error dial — it is the knob that tunes a virus between "
  "stability and adaptability."),
},
{
 "key": "assembly-budding", "name": "Viral Assembly and Budding: Building New Virions",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Assembly is manufacturing: newly copied genomes and newly made "
  "proteins must find each other and pack into working particles. For "
  "many viruses, capsid proteins self-assemble — mix purified subunits in "
  "a test tube and they snap together into shells on their own, driven "
  "by the same hydrophobic and electrostatic forces that fold proteins. "
  "Genome packaging is the precision step: a packaging signal on the "
  "genome is recognized by the capsid, and a portal motor burns ATP to "
  "reel DNA inside against crushing pressure. Non-enveloped viruses "
  "finish here and wait for cell lysis. Enveloped viruses take one more "
  "step — budding: capsid or nucleocapsid components gather at a "
  "membrane (cell surface, endoplasmic reticulum, or Golgi), the membrane "
  "curves around them, and the particle pinches off, wrapping itself in "
  "a piece of the host. HIV, influenza, and coronaviruses all exit by "
  "budding, which is why their envelopes carry host membrane lipids "
  "studded with viral spikes."),
 "how_it_works": (
  "Self-assembly follows nucleation-and-growth kinetics: a slow nucleation "
  "step forms a small seed complex, then subunits add rapidly until the "
  "shell closes. The geometry is encoded in the subunit's shape — "
  "identical subunits can only tile an icosahedron, so the outcome is "
  "deterministic. Packaging motors are among the strongest molecular "
  "machines known: phage motors generate tens of piconewtons of force to "
  "compress DNA to near-crystalline density. Budding is driven by viral "
  "matrix proteins that oligomerize under the membrane and bend it; the "
  "final pinch-off uses the cell's own ESCRT membrane-scission machinery, "
  "which the virus hijacks. Because budding wraps the particle in host "
  "membrane, enveloped viruses display host proteins on their surface — a "
  "camouflage that complicates immune recognition."),
 "key_points": [
  "Capsid proteins self-assemble; geometry is encoded in the subunit shape.",
  "Packaging signals plus ATP-driven portal motors reel genomes into shells.",
  "Enveloped viruses bud through host membranes, stealing a lipid envelope.",
  "Budding hijacks the cell's ESCRT membrane-scission machinery for pinch-off.",
  "Host membrane camouflage complicates immune recognition of enveloped viruses."],
 "requirements": [
  "Virus structure and lytic cycle records.",
  "Basic idea of proteins binding and membranes curving."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_FIELDS],
 "demo_kind": "assembly_kinetics",
 "sig_lens": (
  "The Signature reading treats assembly as a self-building factory: "
  "parts that find each other, a motor that packs the cargo, and a "
  "shipping department that wraps the product in stolen packaging. "
  "Signature virology studies the line because self-assembly is the "
  "cheapest manufacturing ever discovered."),
},
{
 "key": "bacteriophages", "name": "Bacteriophages: Viruses That Hunt Bacteria",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Bacteriophages — phages for short — are viruses that infect bacteria, "
  "and they are the most numerous viruses on the planet. Every milliliter "
  "of seawater holds millions of them. The classic tailed phages "
  "(class Caudoviricetes) look like lunar landers: an icosahedral head "
  "packed with double-stranded DNA, a tail tube, and tail fibers that "
  "recognize the bacterial surface. Phage T4, the laboratory workhorse, "
  "carries a 169,000-letter genome in a 90-nanometer head. Phages shaped "
  "modern biology: the Hershey-Chase experiment (1952) used phage to "
  "prove DNA is the genetic material, and phage lambda revealed how "
  "genes are switched on and off. Today phages are returning as medicine: "
  "phage therapy uses lytic phages to kill antibiotic-resistant bacteria, "
  "a practice pioneered in Georgia and now in clinical trials worldwide. "
  "Phages also drive bacterial evolution — they shuttle genes between "
  "bacteria (transduction), including antibiotic-resistance genes."),
 "how_it_works": (
  "A tailed phage infects like a syringe: tail fibers bind the bacterial "
  "surface reversibly, then irreversibly; the tail sheath contracts, "
  "driving the tail tube through the cell wall; the genome is injected "
  "while the empty capsid stays outside. From there the phage runs the "
  "lytic or lysogenic program. Phage therapy exploits the lytic program's "
  "specificity: a phage that kills Staphylococcus aureus ignores every "
  "human cell and every beneficial gut bacterium, unlike broad-spectrum "
  "antibiotics. Treatment uses cocktails of phages (to slow resistance), "
  "and dosing is measured in multiplicity of infection (MOI) — the ratio "
  "of phage particles to bacterial cells. Transduction, the accidental "
  "packaging of bacterial DNA into phage heads, makes phages major "
  "horizontal gene-transfer agents in nature."),
 "key_points": [
  "Phages are the most numerous viruses on Earth; tailed phages (Caudoviricetes) are the classic form.",
  "Tailed phages inject DNA like a syringe; the capsid stays outside.",
  "Phage experiments proved DNA is the genetic material (Hershey-Chase, 1952).",
  "Phage therapy uses lytic phages against antibiotic-resistant bacteria — highly specific, sparing human cells.",
  "Transduction lets phages shuttle genes (including resistance genes) between bacteria."],
 "requirements": [
  "Lytic and lysogenic cycle records.",
  "Basic algebra for the MOI dosing demo."],
 "standards": ["ICTV nomenclature (Caudoviricetes)", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_CANN],
 "demo_kind": "phage_moi",
 "sig_lens": (
  "The Signature reading treats the phage as a precision instrument: a "
  "delivery vehicle that finds one bacterial strain in a sea of microbes "
  "and ignores everything else. Signature virology studies the targeting "
  "because specificity is the hardest engineering problem in medicine — "
  "and the phage solved it billions of years ago."),
},
{
 "key": "plant-viruses", "name": "Plant Viruses: TMV and the Green World",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Plant viruses were where virology began: in 1892 Dmitri Ivanovsky showed "
  "that sap from diseased tobacco plants stayed infectious after passing "
  "through bacteria-proof filters, and in 1898 Martinus Beijerinck named "
  "the agent a 'contagium vivum fluidum' — a contagious living fluid — "
  "coining the word virus. Tobacco mosaic virus (TMV), the culprit, became "
  "the most studied virus in history: a rigid rod 300 nanometers long and "
  "18 across, built from 2,130 identical coat proteins wound in a helix "
  "around a single 6,395-letter positive-sense RNA genome — exactly three "
  "nucleotides per protein subunit. Wendell Stanley crystallized TMV in "
  "1935, proving viruses are partly crystalline chemicals (Nobel Prize "
  "1946). Plant viruses spread by sap-sucking insects (aphids, whiteflies), "
  "by seed and pollen, and by mechanical wounds from tools and hands. They "
  "cause enormous agricultural losses — cassava mosaic, rice tungro, "
  "banana bunchy top — and controlling them means controlling vectors, "
  "certifying virus-free seed, and breeding resistant crop varieties."),
 "how_it_works": (
  "Plant viruses face a problem animal viruses rarely do: the rigid plant "
  "cell wall. They solve it by moving through plasmodesmata — the narrow "
  "channels connecting plant cells — using dedicated movement proteins "
  "that widen the channels and escort the genome through. Long-distance "
  "spread rides the phloem, the plant's sugar-transport plumbing. Entry "
  "requires a wound: aphid stylets, a gardener's pruning shears, or "
  "leaf-to-leaf abrasion. Because plants have no circulating immune cells, "
  "their defense is RNA silencing — chopping viral RNA into small pieces "
  "— and plant viruses counter with silencing-suppressor proteins, an "
  "arms race written into both genomes. TMV's extreme stability (it "
  "survives for years in dried leaves and even in cigarettes) comes from "
  "its tight helical packing, which also made it the first virus whose "
  "structure was solved to atomic detail."),
 "key_points": [
  "Virology began with plant viruses: Ivanovsky (1892), Beijerinck (1898), TMV crystallized by Stanley (1935).",
  "TMV: 300 x 18 nm rod, 2,130 coat proteins, 6,395-letter +ssRNA genome — 3 nucleotides per subunit.",
  "Plant viruses move cell-to-cell through plasmodesmata via movement proteins; long-distance via phloem.",
  "Spread by insect vectors, seed, pollen, and mechanical wounds; plants defend by RNA silencing.",
  "Major crop diseases (cassava mosaic, rice tungro) controlled by vector control, clean seed, resistant varieties."],
 "requirements": [
  "Virus structure (helical capsids) record.",
  "Basic idea of how plants transport sap."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_STD],
 "demo_kind": "tmv_packing",
 "sig_lens": (
  "The Signature reading treats TMV as the reference design: the "
  "simplest complete virus ever characterized, with a parts list so "
  "clean it reads like a bill of materials. Signature virology keeps "
  "TMV as the calibration standard — understand this rod and you "
  "understand the grammar of all helical viruses."),
},
{
 "key": "animal-viruses", "name": "Animal Viruses: From Pets to Livestock to Wildlife",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "Animal viruses infect every vertebrate and invertebrate group, and "
  "veterinary virology is one of the field's largest branches — because "
  "livestock epidemics can devastate food supplies and economies. Foot-and-"
  "mouth disease virus (a picornavirus) can shut down a nation's meat "
  "exports; African swine fever virus (a giant DNA virus) has killed "
  "hundreds of millions of pigs across Asia and Europe since 2018; avian "
  "influenza strains sweep through poultry flocks and occasionally jump "
  "to humans. Companion animals have their own viral burdens: canine "
  "parvovirus, feline leukemia virus (a retrovirus), rabies across "
  "mammals. Wildlife viruses form the vast reservoir from which "
  "livestock and human viruses emerge — bats, rodents, and birds carry "
  "enormous viral diversity, most of it harmless to its natural host. "
  "Studying animal viruses is therefore both veterinary medicine and "
  "pandemic prevention: nearly every emerging human virus was an animal "
  "virus first."),
 "how_it_works": (
  "The same entry, replication, and transmission principles apply, but the "
  "ecology differs by host. Livestock viruses exploit dense, genetically "
  "uniform populations — a feedlot or poultry barn is an ideal transmission "
  "network, which is why outbreaks explode so fast and why culling and "
  "movement bans are the standard response. Vector-borne animal viruses "
  "(bluetongue in sheep via midges, African horse sickness) follow their "
  "insects' seasons and ranges. Wildlife reservoirs maintain viruses "
  "through chronic or latent infections with little disease — bats "
  "tolerate viruses that would kill other mammals, partly through "
  "dampened inflammatory responses. Spillover happens at the interfaces: "
  "live-animal markets, farms bordering forests, bushmeat hunting. "
  "Veterinary vaccines (foot-and-mouth, Newcastle disease, rabies) are "
  "among the most widely deployed vaccines on Earth by dose count."),
 "key_points": [
  "Veterinary virology protects food supplies: foot-and-mouth, African swine fever, avian influenza.",
  "Dense uniform livestock populations are ideal transmission networks — outbreaks explode fast.",
  "Bats, rodents, and birds are vast reservoirs; most of their viruses are harmless to the natural host.",
  "Nearly every emerging human virus was an animal virus first — animal surveillance is pandemic prevention.",
  "Veterinary vaccines (rabies, Newcastle disease) are among the most-deployed vaccines by dose count."],
 "requirements": [
  "Transmission routes and tropism records.",
  "No mathematics needed for this record."],
 "standards": ["ICTV nomenclature", "OIE-listed disease terminology"],
 "citations": [CIT_FIELDS, CIT_WHO],
 "demo_kind": "host_matrix",
 "sig_lens": (
  "The Signature reading treats animal virology as infrastructure "
  "protection: the food supply and the human-animal interface are "
  "critical systems, and viruses are the failure mode. Signature "
  "virology maps the interfaces because that is where new failures "
  "originate."),
},
{
 "key": "respiratory-viruses", "name": "Human Respiratory Viruses: Flu, Coronaviruses, and Colds",
 "group": "Compounded", "ladder_rank": 6, "ladder_tier": "compounded",
 "description": (
  "The human airway is the most contested real estate in virology, "
  "colonized by a rotating cast of respiratory viruses. Influenza "
  "viruses (Orthomyxoviridae, negative-sense RNA in 8 segments) cause "
  "seasonal epidemics and occasional pandemics — 1918, 1957, 1968, 2009 "
  "— driven by antigenic drift (gradual mutation) and shift (segment "
  "reassortment). Coronaviruses (Coronaviridae, positive-sense RNA, "
  "~30,000 letters — the largest RNA genomes) include four endemic "
  "common-cold species plus SARS-CoV (2002), MERS-CoV (2012), and "
  "SARS-CoV-2 (2019). Rhinoviruses (Picornaviridae, 150+ types) cause "
  "most common colds. Respiratory syncytial virus (RSV) is the leading "
  "cause of infant hospitalization. What unites them is the route: "
  "shedding in airway secretions, spread in droplets and aerosols, "
  "best survival in cool dry air — the recipe for winter seasonality "
  "in temperate climates. Immunity is typically partial and "
  "short-lived, which is why reinfections recur throughout life."),
 "how_it_works": (
  "Respiratory viruses dock onto airway cell receptors — influenza's "
  "hemagglutinin binds sialic acids, SARS-CoV-2's spike binds ACE2 — "
  "and replicate in the nasal passages, throat, or lungs depending on "
  "temperature preference and receptor distribution. The segmented "
  "influenza genome allows reassortment: if a pig cell is co-infected "
  "with a human and a bird flu strain, progeny can inherit segments "
  "from both, producing a novel virus the population has never seen — "
  "the classic pandemic recipe. Coronaviruses replicate in "
  "membrane-wrapped compartments using their proofreading-equipped "
  "polymerase complex. Disease severity tracks how deep the infection "
  "goes: rhinoviruses stay in the cooler upper airway (mild colds), "
  "while viruses that reach the lower lungs (severe influenza, "
  "SARS-CoV-2 pneumonia) trigger dangerous inflammation. Vaccines "
  "target the surface proteins — hemagglutinin for flu, spike for "
  "coronaviruses — and must be updated as those proteins drift."),
 "key_points": [
  "Major families: Orthomyxoviridae (flu), Coronaviridae, Picornaviridae (rhinoviruses), Pneumoviridae (RSV).",
  "Influenza evolves by drift (mutation) and shift (segment reassortment) — shift drives pandemics.",
  "Coronaviruses carry the largest RNA genomes (~30,000 letters) with a proofreading polymerase.",
  "Winter seasonality follows cool dry air favoring aerosol survival and indoor crowding.",
  "Severity tracks infection depth: upper-airway colds versus lower-lung pneumonia."],
 "requirements": [
  "Transmission routes and replication strategies records.",
  "No mathematics needed for this record."],
 "standards": ["ICTV nomenclature", "WHO influenza terminology"],
 "citations": [CIT_FIELDS, CIT_CDC, CIT_WHO],
 "demo_kind": "r0_compare",
 "sig_lens": (
  "The Signature reading treats the airway as a shared public channel "
  "with seasonal traffic patterns. Signature virology studies the "
  "respiratory cast together because they compete for the same channel "
  "— and defenses built for one (ventilation, masks, updated vaccines) "
  "narrow the channel for all."),
},
{
 "key": "emerging-viruses", "name": "Emerging Viruses and Zoonotic Spillover",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "An emerging virus is one newly recognized in humans or rapidly "
  "expanding its range — and the roster since 1970 is long: Ebola "
  "(1976), HIV (recognized 1983), Nipah (1998), SARS-CoV (2002), "
  "MERS-CoV (2012), Zika (2015), SARS-CoV-2 (2019). The dominant "
  "mechanism is zoonotic spillover: an animal virus jumps into humans "
  "when ecology brings them together — deforestation, live-animal "
  "markets, bushmeat hunting, farms bordering wildlife habitat. Bats "
  "are the standout reservoir, hosting coronaviruses, filoviruses, "
  "henipaviruses, and lyssaviruses while rarely falling ill "
  "themselves. A successful spillover needs three things: contact, "
  "compatibility (the spike must engage a human receptor), and "
  "onward transmission between humans. Most spillovers fail at step "
  "three and die out as dead-end infections; the rare ones that "
  "transmit become epidemics. RNA viruses dominate the emerging list "
  "because their high mutation rates let them adapt to new hosts "
  "quickly."),
 "how_it_works": (
  "Spillover is a molecular negotiation. The animal virus's spike "
  "protein must bind a human receptor with workable affinity — often "
  "requiring only a few amino-acid changes, which is why surveillance "
  "watches spike sequences closely. After the jump, the virus faces "
  "human innate immunity (interferon responses) tuned differently than "
  "its reservoir host's; adaptation typically attenuates the virus's "
  "interference with interferon while improving replication. "
  "Epidemiologically, emergence follows a pattern: an index cluster "
  "linked to animal contact, then chains of human transmission whose "
  "length depends on R0. Scientists score spillover risk from viral "
  "family traits (RNA genome, broad host range, respiratory route score "
  "higher), receptor compatibility assays, and ecological contact "
  "rates — a triage system for deciding which animal viruses deserve "
  "vaccines and countermeasures before they emerge."),
 "key_points": [
  "Emerging viruses since 1970: Ebola, HIV, Nipah, SARS, MERS, Zika, SARS-CoV-2 — mostly zoonotic spillovers.",
  "Spillover needs contact, receptor compatibility, and human-to-human transmission; most fail at step three.",
  "Bats are the standout reservoir: diverse viruses, rarely ill themselves.",
  "RNA viruses dominate the emerging list — high mutation rates speed host adaptation.",
  "Risk scoring combines viral traits, receptor assays, and ecological contact rates to triage threats."],
 "requirements": [
  "Tropism and animal viruses records.",
  "Basic algebra for the risk-scoring demo."],
 "standards": ["ICTV nomenclature", "WHO emerging-disease terminology"],
 "citations": [CIT_FIELDS, CIT_WHO],
 "demo_kind": "spillover_score",
 "sig_lens": (
  "The Signature reading treats spillover as an interface breach: "
  "two systems (wildlife ecology, human networks) that were never "
  "designed to connect, now connected at scale. Signature virology "
  "studies the interface the way a security engineer studies an API "
  "— every new connection is a new attack surface, and most breaches "
  "start as unnoticed probes."),
},
{
 "key": "viral-evolution", "name": "Viral Evolution and Quasispecies",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Viruses are the fastest-evolving biological entities known, and "
  "their evolution follows rules set by their copying machinery. RNA "
  "viruses, whose polymerases lack proofreading, mutate at roughly "
  "10^-4 to 10^-5 per base per replication — about a million times "
  "the human rate — so a single infected person harbors not one viral "
  "genome but a cloud of related mutants called a quasispecies. "
  "Selection acts on the cloud: immune pressure, drugs, and new hosts "
  "favor whichever variants replicate best, and the consensus sequence "
  "shifts within days. This is why RNA virus vaccines must be updated "
  "(influenza's antigenic drift), why HIV escapes single drugs so fast "
  "that therapy requires drug cocktails, and why a virus can adapt to "
  "a new host species in a handful of passages. DNA viruses evolve "
  "slower — their polymerases proofread — but they recombine and swap "
  "genes, and segmented viruses reassort whole genome segments. "
  "Evolution also runs in the other direction: viruses lose genes "
  "they no longer need, streamlining toward minimalism."),
 "how_it_works": (
  "The quasispecies model treats the viral population, not the "
  "individual genome, as the unit of selection. With mutation rate mu "
  "per base and genome length L, each replication produces about mu "
  "times L mutations per genome — for a 10,000-letter RNA virus at "
  "mu = 10^-4, roughly one mutation per copy. Most mutations are "
  "harmful or neutral; the rare beneficial ones sweep when conditions "
  "favor them. There is an error threshold: push the mutation rate "
  "too high and the population collapses into nonviable mutants — "
  "error catastrophe — which is the rationale behind lethal "
  "mutagenesis drugs (e.g. molnupiravir) that deliberately raise the "
  "error rate. Reassortment and recombination shortcut the slow climb "
  "of point mutations by importing pre-tested gene combinations, "
  "which is why pandemic influenza strains appear suddenly rather "
  "than gradually."),
 "key_points": [
  "RNA viruses mutate ~10^-4 to 10^-5 per base — about a million times the human rate.",
  "An infection is a quasispecies: a cloud of mutants, with selection acting on the cloud.",
  "Antigenic drift forces vaccine updates; rapid escape forces multi-drug cocktails for HIV.",
  "Error catastrophe sets a ceiling — lethal mutagenesis drugs push viruses past it.",
  "Reassortment and recombination import pre-tested gene combinations, enabling sudden jumps."],
 "requirements": [
  "RdRp record (error rates) and replication strategies.",
  "Basic algebra and probability for the simulation demo."],
 "standards": ["IUPAC nucleic acid notation", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_FIELDS],
 "demo_kind": "quasispecies_sim",
 "sig_lens": (
  "The Signature reading treats the quasispecies as parallel search: "
  "a million prototypes tested against the environment at once, the "
  "winners promoted instantly. Signature virology studies the search "
  "because it is the most aggressive optimization algorithm in "
  "nature — and every defense must assume the attacker is already "
  "running it."),
},
{
 "key": "latency", "name": "Viral Latency: Herpesviruses and the Long Game",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "Latency is the virus's long game: infect once, hide for life, "
  "reactivate when conditions favor. Herpesviruses are the masters — "
  "eight infect humans, and all establish lifelong latency. Herpes "
  "simplex virus 1 hides in trigeminal nerve ganglia and reactivates "
  "as cold sores; varicella-zoster virus hides in dorsal root ganglia "
  "after chickenpox and returns decades later as shingles; Epstein-Barr "
  "virus persists silently in B cells; cytomegalovirus hides in "
  "myeloid cells. During latency the genome persists as a circular "
  "episome in the nucleus, expressing only a handful of latency genes "
  "— no new particles are made, so the immune system has almost "
  "nothing to see. Reactivation is triggered by stress, "
  "immunosuppression, or ultraviolet light: the virus re-enters the "
  "lytic program and travels back down the nerve to the surface. "
  "HIV achieves a different latency by integrating as a provirus in "
  "resting memory T cells — the reason antiretroviral therapy "
  "suppresses but cannot cure it."),
 "how_it_works": (
  "Latency is maintained by epigenetic silencing: the cell wraps the "
  "viral episome in repressive chromatin, and viral latency proteins "
  "reinforce the lockdown while blocking cell death. In neurons, HSV "
  "expresses only the latency-associated transcripts (LATs), which are "
  "not even translated into protein — pure RNA regulators. "
  "Reactivation reverses the program: stress signals activate cellular "
  "transcription factors that bind the viral genome, chromatin opens, "
  "lytic genes fire in their cascade order, and new virions assemble "
  "and travel by axonal transport back to the epithelium. The system "
  "is a bistable switch like the lambda cI/Cro circuit, but tuned for "
  "decades rather than minutes. Antivirals like acyclovir work only "
  "during reactivation — they target the lytic polymerase — which is "
  "why they suppress outbreaks but cannot purge the latent reservoir."),
 "key_points": [
  "Eight human herpesviruses all establish lifelong latency in specific cell types.",
  "Latent genomes persist as nuclear episomes expressing almost nothing — invisible to immunity.",
  "Reactivation triggers: stress, immunosuppression, UV light; virus travels back down nerves.",
  "HIV latency is integrated provirus in resting memory T cells — the barrier to a cure.",
  "Antivirals (acyclovir) hit only the lytic phase — they suppress, not cure, latency."],
 "requirements": [
  "Lysogenic cycle record (the bacterial parallel).",
  "Basic idea of genes switched on/off."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_PRINCIPLES],
 "demo_kind": "latency_markov",
 "sig_lens": (
  "The Signature reading treats latency as deep standby: power down "
  "to near zero, keep one wake-up circuit armed, resume on signal. "
  "Signature virology studies standby because the quietest state is "
  "the hardest to clear — in machines as in infections, what sleeps "
  "longest resists deletion."),
},
{
 "key": "oncogenic-viruses", "name": "Oncogenic Viruses: When Viruses Cause Cancer",
 "group": "Compounded", "ladder_rank": 7, "ladder_tier": "compounded",
 "description": (
  "About 15 percent of human cancers worldwide are caused by "
  "infections, mostly viruses — a fact that turns some cancers into "
  "vaccine-preventable diseases. The roster is well established. "
  "Human papillomaviruses (HPV), especially types 16 and 18, cause "
  "virtually all cervical cancers plus anal, throat, and other "
  "cancers — and HPV vaccines now prevent them. Hepatitis B and C "
  "cause liver cancer through decades of chronic inflammation. "
  "Epstein-Barr virus (EBV) causes Burkitt lymphoma and "
  "nasopharyngeal carcinoma. Human T-lymphotropic virus 1 (HTLV-1) "
  "causes adult T-cell leukemia. Kaposi sarcoma herpesvirus (KSHV) "
  "causes Kaposi sarcoma. Merkel cell polyomavirus causes Merkel "
  "cell carcinoma. The mechanisms converge: viral oncoproteins "
  "disable the cell's tumor-suppressor brakes (p53 and Rb), or "
  "chronic infection keeps tissues in a wound-healing state where "
  "mutations accumulate. Because the cause is infectious, the "
  "prevention is too: HBV and HPV vaccines are cancer vaccines."),
 "how_it_works": (
  "Viral oncoproteins are precision saboteurs. HPV's E6 protein tags "
  "p53 — the 'guardian of the genome' — for destruction, while E7 "
  "binds and inactivates Rb, the brake on cell division; with both "
  "brakes cut, the infected cell divides unchecked. EBV drives B "
  "cells to proliferate with its latent proteins, and in malaria-"
  "weakened immune systems the proliferation escapes control as "
  "Burkitt lymphoma. Hepatitis viruses rarely transform cells "
  "directly; instead, decades of immune attack and regeneration "
  "cycles accumulate mutations until a clone turns malignant — which "
  "is why curing hepatitis C with antivirals cuts liver cancer risk. "
  "The long delay between infection and cancer (often decades) is "
  "why the viral link was missed for so long, and why cohort studies "
  "and molecular detection were needed to prove it."),
 "key_points": [
  "~15% of human cancers are infection-caused, mostly viral — making some cancers vaccine-preventable.",
  "HPV 16/18 cause cervical and other cancers; HBV/HCV cause liver cancer; EBV causes Burkitt lymphoma.",
  "Viral oncoproteins (HPV E6/E7) disable tumor suppressors p53 and Rb.",
  "Chronic inflammation (hepatitis) drives cancer through decades of damage-regeneration cycles.",
  "HBV and HPV vaccines are cancer vaccines — prevention by immunization."],
 "requirements": [
  "Latency record (chronic infection idea).",
  "Basic idea of cells dividing and mutations."],
 "standards": ["ICTV nomenclature", "WHO cancer terminology"],
 "citations": [CIT_FIELDS, CIT_WHO],
 "demo_kind": "onco_table",
 "sig_lens": (
  "The Signature reading treats oncogenic viruses as saboteurs that "
  "cut the brakes: disable the safety interlocks and the machine "
  "runs until it destroys itself. Signature virology studies the "
  "sabotage because every engineered system needs interlocks — and "
  "needs to know exactly how an attacker defeats them."),
},
{
 "key": "diagnostics", "name": "Virus Diagnostics: PCR, Serology, Culture, and Sequencing",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Finding a virus means choosing among four detection philosophies. "
  "Nucleic-acid tests (PCR and its cousins) amplify the virus's genetic "
  "material: each thermal cycle doubles the target, so 30 cycles turn a "
  "few molecules into a billion copies — sensitive enough to catch "
  "infection days before symptoms. Antigen tests detect viral proteins "
  "directly (fast, cheap, less sensitive — the familiar rapid tests). "
  "Serology detects the host's antibodies instead of the virus, revealing "
  "past infection or vaccination rather than current disease. Viral "
  "culture grows live virus in cells — slow and demanding, but the only "
  "method that proves infectious virus is present. Metagenomic sequencing "
  "reads all genetic material in a sample and identifies viruses by "
  "matching against databases, catching the unknown as well as the "
  "known. Each method answers a different question: PCR asks 'is viral "
  "genome here now?', antigen asks 'is there enough protein to matter?', "
  "serology asks 'has the immune system seen this?', culture asks 'is it "
  "alive?', sequencing asks 'what is everything here?'."),
 "how_it_works": (
  "PCR exploits exponential amplification: with efficiency near 100%, "
  "copy number after n cycles is 2^n — 30 cycles yields about a billion-"
  "fold amplification. The cycle threshold (Ct) is quantitative: a low "
  "Ct (say 18) means abundant starting material; a high Ct (say 35) "
  "means scarce material, since each ~3.3 Ct difference is a tenfold "
  "change. Reverse-transcription PCR first converts RNA to DNA for RNA "
  "viruses. Serology uses the antibody's specificity: patient serum is "
  "exposed to viral antigen, and bound antibodies are revealed with a "
  "color or light signal (ELISA); IgM indicates recent infection, IgG "
  "indicates past infection or vaccination. Culture requires susceptible "
  "cell lines and biosafety containment, and is read by cytopathic "
  "effect — the visible wreckage virus leaves in cells. Sequencing "
  "pipelines filter out host reads, assemble the rest, and classify "
  "contigs against viral databases."),
 "key_points": [
  "PCR amplifies genome 2^n per cycle — ~10^9-fold at 30 cycles; Ct value quantifies starting material.",
  "Antigen tests are fast and cheap but less sensitive; serology reveals past infection via antibodies.",
  "Viral culture is the only proof of infectious virus, but slow and containment-demanding.",
  "Metagenomic sequencing identifies known and unknown viruses by database matching.",
  "Each method answers a different question — choose the test that matches the question."],
 "requirements": [
  "Viral genomes record (what PCR amplifies).",
  "Basic algebra (powers of two) for the demo."],
 "standards": ["MIQE guidelines for PCR", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_CDC],
 "demo_kind": "pcr_amplification",
 "sig_lens": (
  "The Signature reading treats diagnostics as a sensor suite: five "
  "different instruments, each measuring a different physical "
  "quantity, each with a known detection floor. Signature virology "
  "keeps the suite calibrated — knowing what each sensor can and "
  "cannot see is the difference between data and noise."),
},
{
 "key": "vaccines", "name": "Viral Vaccines: Platforms from Inactivated to mRNA",
 "group": "Advanced", "ladder_rank": 8, "ladder_tier": "advanced",
 "description": (
  "Vaccines are the most successful antiviral technology ever deployed: "
  "smallpox — a virus that killed hundreds of millions — was eradicated "
  "in 1980 by vaccination, and polio, measles, and rubella have been "
  "driven to near-elimination in much of the world. Five platform "
  "families do the work. Inactivated (killed) vaccines present dead "
  "virus that cannot replicate (polio IPV, hepatitis A). Live-attenuated "
  "vaccines use weakened virus that replicates briefly without causing "
  "disease (measles, mumps, rubella, yellow fever) — strong, long-lived "
  "immunity from one or two doses. Subunit and virus-like-particle "
  "vaccines present only key proteins (hepatitis B, HPV). Viral-vector "
  "vaccines use a harmless carrier virus to deliver the target's gene "
  "(some COVID-19 and Ebola vaccines). mRNA vaccines deliver messenger "
  "RNA instructing the recipient's own cells to build the viral protein "
  "(COVID-19, 2020 — the fastest vaccine development in history). "
  "Efficacy is measured against disease in trials; effectiveness is "
  "measured in the real world — both typically reported as percent "
  "reduction versus the unvaccinated."),
 "how_it_works": (
  "All platforms train the adaptive immune system without causing the "
  "disease: they present viral antigens to B cells (which make "
  "antibodies) and T cells (which kill infected cells), generating "
  "memory cells that respond in days instead of weeks on real "
  "exposure. Neutralizing antibodies are the key correlate for most "
  "viral vaccines — they bind the spike or surface protein and block "
  "entry. Live-attenuated vaccines additionally trigger the full "
  "innate alarm, which is why their immunity is so durable. mRNA "
  "vaccines work by transfection: lipid nanoparticles carry the mRNA "
  "into cells, ribosomes translate it into spike protein, and the "
  "protein is displayed to the immune system; the mRNA degrades within "
  "days and never enters the nucleus. Vaccine efficacy VE is computed "
  "as 1 minus the relative risk: if 1% of vaccinated versus 20% of "
  "unvaccinated fall ill, VE = 1 - 0.05 = 95%. Herd effects multiply "
  "individual protection when coverage is high."),
 "key_points": [
  "Smallpox eradicated (1980) by vaccination — the greatest antiviral victory in history.",
  "Five platforms: inactivated, live-attenuated, subunit/VLP, viral-vector, mRNA.",
  "Neutralizing antibodies that block entry are the key immune correlate for most viral vaccines.",
  "mRNA vaccines (2020) deliver instructions for cells to build the antigen; the mRNA degrades in days.",
  "Efficacy = 1 - relative risk; high coverage multiplies protection through herd effects."],
 "requirements": [
  "Diagnostics record (how protection is measured).",
  "Basic algebra (percentages) for the efficacy demo."],
 "standards": ["WHO vaccine terminology", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_WHO, CIT_CDC],
 "demo_kind": "vaccine_efficacy",
 "sig_lens": (
  "The Signature reading treats vaccination as pre-deployment of "
  "countermeasures: train the defense on the attacker's shape before "
  "the attacker arrives. Signature virology studies the platforms "
  "as delivery engineering — same payload (the antigen), five "
  "different logistics chains, each with its own speed, cost, and "
  "durability trade-offs."),
},
{
 "key": "antivirals", "name": "Antivirals: Drugs That Stop Viruses",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Antivirals are drugs that block specific steps of the viral life "
  "cycle — entry, genome copying, protein processing, or release — and "
  "they work precisely because those steps use virus-specific "
  "machinery that human cells lack. The classes map onto the life "
  "cycle. Entry/fusion inhibitors block docking or membrane fusion "
  "(enfuvirtide for HIV, monoclonal antibodies for several viruses). "
  "Polymerase inhibitors jam genome copying: nucleoside analogues "
  "(AZT, acyclovir, remdesivir, molnupiravir) masquerade as building "
  "blocks and stall the enzyme. Protease inhibitors stop viral "
  "proteins from being cut into working form (HIV and hepatitis C "
  "protease inhibitors; nirmatrelvir for SARS-CoV-2). Neuraminidase "
  "inhibitors (oseltamivir/Tamiflu) trap newly budded influenza "
  "viruses on the cell surface. Integrase inhibitors block HIV's "
  "genome insertion. Combination therapy — hitting several steps at "
  "once, as in HIV antiretroviral therapy — suppresses the virus "
  "below detection and makes resistance evolution nearly impossible, "
  "turning HIV from a death sentence into a manageable chronic "
  "condition. Hepatitis C antivirals (direct-acting antivirals) go "
  "further: they cure over 95% of infections."),
 "how_it_works": (
  "Drug action is quantified by dose-response curves. The IC50 is the "
  "drug concentration that inhibits 50% of viral replication in cell "
  "culture; the Hill equation describes the curve's steepness. "
  "Nucleoside analogues exploit the viral polymerase's pickiness gap: "
  "the enzyme incorporates the fake nucleotide, but the fake lacks the "
  "chemical handle for adding the next one, terminating the chain — "
  "acyclovir goes further by being activated only by the viral "
  "thymidine kinase, so it poisons infected cells selectively. Protease "
  "inhibitors are shaped to fit the viral protease's active site like "
  "a key broken off in a lock. Resistance arises when the target "
  "protein mutates to exclude the drug while keeping its function — "
  "the quasispecies cloud guarantees such mutants pre-exist at low "
  "frequency, which is why single-drug therapy fails and combinations "
  "succeed: the chance of simultaneous resistance to three drugs is "
  "the product of three small probabilities."),
 "key_points": [
  "Antivirals target virus-specific steps: entry, polymerase, protease, release, integration.",
  "Nucleoside analogues (acyclovir, remdesivir) terminate genome chains; protease inhibitors jam protein maturation.",
  "IC50 quantifies potency; the Hill equation describes the dose-response curve.",
  "HIV combination therapy suppresses virus below detection and blocks resistance evolution.",
  "Hepatitis C direct-acting antivirals cure >95% of infections — antivirals can cure, not just suppress."],
 "requirements": [
  "Replication strategies and viral evolution records.",
  "Basic algebra for the dose-response demo."],
 "standards": ["INN drug nomenclature", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_PRINCIPLES],
 "demo_kind": "antiviral_dose_response",
 "sig_lens": (
  "The Signature reading treats antivirals as sabotage tools: find "
  "the machine's most specialized moving part and throw a wrench "
  "shaped exactly like its fuel. Signature virology studies the "
  "sabotage because the same analysis that designs the wrench "
  "reveals which parts of any system are irreplaceable — and which "
  "redundancies would defeat the attack."),
},
{
 "key": "viral-epidemiology", "name": "Epidemiology of Viral Disease: R0 and Herd Immunity",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Viral epidemiology turns outbreaks into numbers. The central number "
  "is R0 (R-naught): the average number of new infections each case "
  "generates in a fully susceptible population. R0 below 1 means the "
  "outbreak shrinks; above 1 it grows. Measles, the champion, has an R0 "
  "of 12 to 18; smallpox 5 to 7; ancestral SARS-CoV-2 about 2.5 to 3; "
  "seasonal influenza about 1.3. From R0 comes the herd immunity "
  "threshold — the immune fraction that stops spread: 1 minus 1/R0. "
  "For measles that is about 93-94%, which is why measles vaccination "
  "coverage must stay extremely high; for flu at R0 1.3 it is about "
  "23%. The effective reproduction number Rt tracks the real-time value "
  "as immunity and behavior change — the dashboard number of every "
  "pandemic. Generation time (infection to onward transmission) sets the "
  "outbreak's tempo: short generations mean explosive growth. Case "
  "fatality ratio (deaths divided by cases) measures severity but is "
  "easily biased by undercounted mild cases — the infection fatality "
  "ratio, measured by serology surveys, is the honest version."),
 "how_it_works": (
  "The SIR model — Susceptible, Infectious, Recovered — captures the "
  "core dynamics with three coupled rates: infections happen when "
  "susceptible and infectious people meet (rate proportional to both), "
  "and the infectious recover at a fixed rate. R0 equals the "
  "transmission rate times the infectious period. Early in an outbreak "
  "with few immunes, cases grow exponentially with a doubling time set "
  "by R0 and the generation time. The herd threshold falls out of the "
  "same math: each case must meet fewer than one susceptible on "
  "average, so the susceptible fraction must drop below 1/R0. "
  "Vaccination moves people directly from susceptible to recovered "
  "without disease, which is how coverage above the threshold "
  "extinguishes transmission even among the unvaccinated. Real "
  "models add age structure, seasonality, waning immunity, and "
  "networks — but SIR explains why measles needs ~94% coverage and "
  "why a fast, short-generation virus outruns slow responses."),
 "key_points": [
  "R0: new infections per case in a susceptible population; >1 grows, <1 shrinks.",
  "Measles R0 12-18, smallpox 5-7, ancestral SARS-CoV-2 ~2.5-3, seasonal flu ~1.3.",
  "Herd immunity threshold = 1 - 1/R0: ~93-94% for measles, ~23% for flu.",
  "Rt is the real-time effective value tracked during outbreaks.",
  "SIR dynamics explain exponential early growth and why vaccination above threshold stops spread."],
 "requirements": [
  "Transmission routes record.",
  "Basic algebra; the demo integrates the SIR model numerically."],
 "standards": ["WHO epidemiological terminology", "SI units throughout"],
 "citations": [CIT_WHO, CIT_CDC, CIT_STD],
 "demo_kind": "sir_model",
 "sig_lens": (
  "The Signature reading treats an epidemic as a chain reaction with "
  "a measurable multiplication factor. Signature virology keeps the "
  "reactor math explicit — R0, thresholds, doubling times — because "
  "a chain reaction is controllable only through quantities you can "
  "measure and move."),
},
{
 "key": "lab-techniques", "name": "Virology Lab Techniques: Plaque Assays, Culture, and Biosafety",
 "group": "Advanced", "ladder_rank": 9, "ladder_tier": "advanced",
 "description": (
  "Working with viruses demands techniques matched to their invisibility "
  "and infectivity. Cell culture grows viruses in living cells: a "
  "susceptible cell line is inoculated, and infection is read by "
  "cytopathic effect — the visible wreckage of rounding, detaching, or "
  "fusing cells. The plaque assay quantifies infectious virus: a cell "
  "monolayer is infected with diluted virus under a semisolid overlay "
  "that restricts spread, so each infectious particle creates one "
  "visible clearing (plaque); counting plaques at a known dilution "
  "gives plaque-forming units per milliliter (PFU/mL) — the gold "
  "standard of virus titration. Serial tenfold dilutions make this "
  "possible across enormous concentration ranges. None of this happens "
  "on an open bench for dangerous pathogens: biosafety levels BSL-1 "
  "through BSL-4 escalate from basic hygiene (harmless lab strains) to "
  "full positive-pressure suits with dedicated air supply (Ebola, "
  "Marburg). Every protocol — inactivation, waste decontamination, "
  "exposure response — is written before the experiment begins."),
 "how_it_works": (
  "The plaque assay is applied Poisson statistics. If a well receives "
  "an average of m infectious particles, the fraction of cells (or "
  "wells) receiving zero follows e^-m; dilutions are chosen so plaques "
  "are countable (typically 10-100 per plate). PFU per mL equals plaques "
  "counted divided by (dilution factor times inoculum volume in mL): "
  "30 plaques from 0.1 mL of a 10^-6 dilution means 3 x 10^8 PFU/mL. "
  "Cell culture tropism doubles as a diagnostic: only susceptible lines "
  "show cytopathic effect, narrowing the suspect list. Biosafety levels "
  "are assigned by risk group: BSL-2 covers most clinical viruses "
  "(biosafety cabinet, lab coats, gloves); BSL-3 adds respiratory "
  "protection and directional airflow (tuberculosis, SARS-CoV-2 "
  "culture); BSL-4 is a sealed suit laboratory for viruses with no "
  "treatment and high lethality. The cardinal rule: never work with a "
  "pathogen at a lower level than its risk group requires."),
 "key_points": [
  "Plaque assay: one infectious particle makes one plaque; PFU/mL = plaques / (dilution x volume).",
  "Cell culture reads infection by cytopathic effect in susceptible cell lines.",
  "Serial tenfold dilutions span enormous concentration ranges for titration.",
  "BSL-1 to BSL-4 escalate containment with pathogen risk; BSL-4 means positive-pressure suits.",
  "Safety protocols are written before experiments begin — containment is designed, not improvised."],
 "requirements": [
  "Diagnostics record (what titration measures).",
  "Basic algebra and the idea of dilution series."],
 "standards": ["WHO biosafety manual terminology", "SI units throughout"],
 "citations": [CIT_PRINCIPLES, CIT_CDC],
 "demo_kind": "plaque_assay",
 "sig_lens": (
  "The Signature reading treats the virology lab as a clean room for "
  "dangerous prototypes: every procedure is a containment protocol, "
  "every measurement a calibrated instrument. Signature virology "
  "respects the lab discipline because handling live systems safely "
  "is itself the engineering achievement."),
},
{
 "key": "viral-vectors", "name": "Viral Vectors and Gene Therapy",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "If viruses are nature's gene-delivery machines, medicine can "
  "repurpose them: strip out the disease-causing genes, load therapeutic "
  "cargo, and you have a viral vector. Three platforms dominate. "
  "Adeno-associated virus (AAV) is small (4.7-thousand-letter capacity), "
  "non-pathogenic, and persists in cells without integrating — ideal for "
  "delivering a working gene copy in inherited diseases (approved "
  "therapies for spinal muscular atrophy and inherited blindness). "
  "Lentiviral vectors (derived from HIV, gutted of virulence genes) "
  "integrate their cargo into the chromosome — used ex vivo: a patient's "
  "own blood stem cells are modified in the lab and reinfused (cures "
  "for severe combined immunodeficiency, sickle-cell approaches, and "
  "CAR-T cancer therapy, where T cells are armed against tumors). "
  "Adenovirus vectors carry larger cargo and provoke strong immunity — "
  "useful for vaccines (several COVID-19 and Ebola vaccines) but limited "
  "for repeat dosing. The engineering trade-offs are capacity versus "
  "persistence versus immune visibility, and every approved therapy "
  "balances all three."),
 "how_it_works": (
  "Vector design starts by deleting virulence: the genes for replication "
  "and disease are removed, leaving the packaging signals, and the "
  "therapeutic gene plus a promoter is inserted in their place. "
  "Production uses packaging cell lines that supply the missing proteins "
  "in trans, so the vector particles that emerge can infect once but "
  "cannot replicate further — replication-incompetent by design. AAV's "
  "cargo limit (~4.7 kb including its own ends) constrains which genes "
  "fit; lentiviruses carry ~8 kb and integrate semi-randomly, which "
  "brings insertional-mutagenesis risk managed by vector design and "
  "patient monitoring. Dosing is measured in vector genomes per "
  "kilogram; efficacy is read by the therapeutic protein's activity "
  "(e.g. clotting factor levels in hemophilia trials). Pre-existing "
  "immunity to the vector (many people carry AAV antibodies) can block "
  "delivery, so serotype selection and screening are part of every "
  "protocol."),
 "key_points": [
  "Viral vectors are gutted viruses repurposed as gene-delivery vehicles — replication-incompetent by design.",
  "AAV: ~4.7 kb capacity, non-integrating, for inherited diseases (spinal muscular atrophy, blindness).",
  "Lentiviral vectors: ~8 kb, integrating, used ex vivo (SCID, CAR-T cancer therapy).",
  "Adenovirus vectors: large cargo, strong immunity — best for vaccines, limited for repeat dosing.",
  "Trade-offs: cargo capacity vs persistence vs immune visibility; pre-existing immunity can block delivery."],
 "requirements": [
  "Reverse transcription (lentiviruses) and assembly records.",
  "Basic idea of genes as deliverable instructions."],
 "standards": ["FDA gene-therapy terminology", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_STD],
 "demo_kind": "vector_capacity",
 "sig_lens": (
  "The Signature reading treats the viral vector as the ultimate "
  "repurposing: take the adversary's delivery system, remove the "
  "warhead, install your own payload. Signature virology studies "
  "the conversion because the best engineering often starts not "
  "from a blank page but from a captured machine."),
},
{
 "key": "giant-viruses", "name": "Giant Viruses and Virophages",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "In 2003, researchers examining what they thought was a bacterium "
  "inside an amoeba discovered Mimivirus — a virus 400 nanometers "
  "across with a 1.2-million-letter genome, bigger than some bacteria "
  "and visible under a light microscope. It shattered the textbook "
  "definition of a virus. Since then the giants have multiplied: "
  "Pandoravirus (up to 2.5 million letters, ~1 micrometer — larger "
  "than some parasitic bacteria), Pithovirus (revived from 30,000-year-"
  "old Siberian permafrost and still infectious to amoebae), Tupanvirus "
  "with the most complete translation gene set ever seen in a virus. "
  "Giant viruses blur the line between virus and cell: they encode "
  "proteins for translation, DNA repair, and metabolism that no "
  "textbook virus should own. And they have their own parasites: "
  "virophages — tiny viruses like Sputnik that infect the viral "
  "factories of giant viruses inside amoebae, sabotaging giant-virus "
  "replication. Parasites of parasites: the microbial world has "
  "depth."),
 "how_it_works": (
  "Giant viruses replicate in cytoplasmic 'viral factories' — "
  "organized compartments in the amoeba where the massive genome is "
  "transcribed by virus-encoded machinery, reducing dependence on the "
  "host nucleus. Their genomes are mosaics: core viral genes plus "
  "hundreds of genes apparently captured from hosts and bacteria over "
  "evolutionary time, including aminoacyl-tRNA synthetases once "
  "thought to be exclusive cellular hallmarks. Discovery methods had "
  "to change: standard 0.2-micron filtration, long used to isolate "
  "viruses, traps giants with the bacteria — modern giant-virus "
  "hunting uses amoeba co-culture instead. Virophages exploit the "
  "factory: Sputnik's 18,000-letter genome hijacks the Mimivirus "
  "factory's machinery, producing defective giant-virus particles — "
  "a hyperparasite that measurably reduces its host virus's burst "
  "size. Phylogenetic analyses place giants across the viral tree, "
  "suggesting gigantism evolved more than once."),
 "key_points": [
  "Mimivirus (2003): 400 nm, 1.2-Mb genome — shattered the small-simple virus definition.",
  "Pandoravirus: up to 2.5 Mb, ~1 micrometer — larger than some bacteria.",
  "Giants encode translation and repair proteins once thought exclusive to cells.",
  "Virophages (e.g. Sputnik) parasitize giant-virus factories — parasites of parasites.",
  "Standard virus filtration misses giants; amoeba co-culture finds them."],
 "requirements": [
  "Virus structure and measuring-viruses records.",
  "Comfort with genome-size comparisons."],
 "standards": ["ICTV nomenclature", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_STD],
 "demo_kind": "giant_compare",
 "sig_lens": (
  "The Signature reading treats giant viruses as proof that the "
  "minimal-machine story was incomplete: some viruses carry a "
  "workshop, not just a blueprint. Signature virology keeps the "
  "giants on the ladder's top rung as a standing warning — every "
  "clean definition in biology is provisional."),
},
{
 "key": "endogenous-retroviruses", "name": "Endogenous Retroviruses: Viral Fossils in Our DNA",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "About eight percent of the human genome is made of endogenous "
  "retroviruses (ERVs) — the fossilized remains of retroviruses that "
  "infected our ancestors' germline cells millions of years ago and "
  "were inherited ever since. Each ERV is a provirus flanked by long "
  "terminal repeats (LTRs), usually mutated into silence: most are "
  "broken relics that can no longer make virus. But 'fossil' "
  "undersells them. Evolution domesticated several: syncytin, the "
  "protein that fuses placental cells in every human pregnancy, is a "
  "captured retroviral envelope gene — mammals literally build "
  "placentas with viral parts. ERV sequences also serve as "
  "evolutionary clocks and species markers: humans and chimpanzees "
  "share many ERV insertions at identical genome positions, proving "
  "the insertions predate our split. Occasionally ERVs reactivate in "
  "disease — abnormal ERV expression is studied in multiple "
  "sclerosis, ALS, and cancers — making these fossils medically "
  "relevant, not just historical."),
 "how_it_works": (
  "Endogenization happens when a retrovirus infects a germline cell "
  "(sperm or egg precursor) rather than a body cell: the integrated "
  "provirus is then copied into every cell of the offspring, "
  "including its own germline, becoming a permanent Mendelian "
  "element. Over millions of years, mutations accumulate — the two "
  "LTRs flanking each ERV diverge at the host's slow mutation rate, "
  "so LTR divergence dates the insertion like a molecular clock. "
  "Most ERVs decay into solo LTRs when the internal genes are deleted "
  "by recombination. Domestication occurs when a viral gene proves "
  "useful: syncytin's fusogenic envelope was co-opted for placental "
  "syncytiotrophoblast formation, and its immunosuppressive domain "
  "may help the fetus evade maternal rejection. Genome-wide scans "
  "find ERV-derived sequences regulating nearby human genes, "
  "particularly in early embryos and the placenta."),
 "key_points": [
  "~8% of the human genome is endogenous retrovirus sequence — inherited viral fossils.",
  "Syncytin, essential for the human placenta, is a domesticated retroviral envelope gene.",
  "Shared ERV insertions at identical positions prove common ancestry (humans and chimpanzees).",
  "LTR divergence acts as a molecular clock dating each insertion.",
  "Abnormal ERV reactivation is studied in MS, ALS, and cancers — fossils with medical relevance."],
 "requirements": [
  "Reverse transcription record (how proviruses integrate).",
  "Basic idea of inheritance."],
 "standards": ["Human genome reference terminology", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_STD],
 "demo_kind": "erv_genome",
 "sig_lens": (
  "The Signature reading treats endogenous retroviruses as legacy "
  "code in the human build: ancient integrations, mostly commented "
  "out, a few promoted to load-bearing features. Signature virology "
  "reads the legacy because every mature system carries its history "
  "in its source — and the placenta runs on a captured virus."),
},
{
 "key": "viral-metagenomics", "name": "Viral Metagenomics: Discovering Viruses by Sequencing",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Most viruses on Earth have never been grown in a lab — they are "
  "known only from their sequences, discovered by viral metagenomics: "
  "sequencing all genetic material in an environmental or clinical "
  "sample and identifying the viral pieces computationally. A liter "
  "of seawater, a gram of soil, or a throat swab yields millions of "
  "short reads; pipelines filter out host and bacterial DNA, assemble "
  "overlapping reads into longer contigs, and classify them by "
  "matching against viral databases or by recognizing viral hallmark "
  "genes (like the RNA-dependent RNA polymerase palm domain). This "
  "approach has expanded the known virosphere by orders of magnitude — "
  "tens of thousands of new RNA virus species from a single "
  "environmental survey — and it is how novel pathogens are now "
  "identified: SARS-CoV-2 was recognized as a coronavirus within days "
  "of metagenomic sequencing in January 2020. The same methods "
  "monitor wastewater for outbreak early warning, tracking viral "
  "loads across whole cities from sewage samples."),
 "how_it_works": (
  "The pipeline has four stages. Extraction and sequencing produce "
  "millions of short reads (typically 100-300 letters each). Quality "
  "filtering and host depletion remove low-quality reads and the "
  "overwhelming host background — in a human sample, over 99% of reads "
  "may be human. Assembly stitches overlapping reads into contigs "
  "using de Bruijn graphs of k-mers (short words of length k); the "
  "choice of k trades sensitivity for specificity. Classification "
  "matches contigs against reference databases by sequence similarity, "
  "while hallmark-gene detection finds distant relatives that match "
  "nothing known — how entirely new viral families are recognized. "
  "Quantification maps reads back to contigs to estimate abundance. "
  "Wastewater surveillance applies the same pipeline at city scale: "
  "concentrated sewage RNA, sequenced and quantified, reveals which "
  "variants are rising days before clinical cases do."),
 "key_points": [
  "Viral metagenomics discovers viruses from sequences alone — most known viruses were never cultured.",
  "Pipeline: sequence, filter host background, assemble k-mer graphs, classify by database or hallmark genes.",
  "SARS-CoV-2 was identified as a coronavirus within days by metagenomic sequencing (January 2020).",
  "Hallmark-gene detection (e.g. RdRp palm domain) recognizes entirely new viral families.",
  "Wastewater sequencing gives city-scale outbreak early warning days ahead of clinical cases."],
 "requirements": [
  "Viral genomes and diagnostics records.",
  "Basic idea of DNA sequencing; the demo counts k-mers."],
 "standards": ["INSDC sequence database conventions", "SI units throughout"],
 "citations": [CIT_FIELDS, CIT_CDC],
 "demo_kind": "kmer_count",
 "sig_lens": (
  "The Signature reading treats metagenomics as a census of the "
  "invisible: sample everything, filter the noise, assemble the "
  "signal, file every new part. Signature virology runs the census "
  "mentality because you cannot defend against parts you have not "
  "catalogued — the unknown virosphere is the largest unmapped "
  "territory in biology."),
},
{
 "key": "pandemic-preparedness", "name": "Pandemic Preparedness and Viral Surveillance",
 "group": "Advanced", "ladder_rank": 10, "ladder_tier": "advanced",
 "description": (
  "Pandemic preparedness is virology converted into policy: the "
  "systems that detect, characterize, and blunt the next emerging "
  "virus before it becomes the next pandemic. Surveillance is the "
  "foundation — networks of laboratories sharing genome sequences "
  "globally (GISAID, INSDC databases), animal-virus sampling at "
  "high-risk interfaces, and wastewater monitoring of cities. "
  "Characterization follows: receptor-compatibility assays, animal "
  "models, and rapid diagnostics the moment a threat is flagged. "
  "Countermeasure platforms are pre-built so they can be redirected: "
  "mRNA and viral-vector vaccine platforms proved this in 2020, going "
  "from sequence to authorized vaccine in under a year. Stockpiles, "
  "manufacturing surge capacity, and pre-negotiated trial networks "
  "compress the response further. Non-pharmaceutical interventions — "
  "testing, contact tracing, ventilation, masks, targeted restrictions "
  "— buy the time countermeasures need. The honest lesson of recent "
  "history: preparedness is a maintained capability, not a purchased "
  "product — surveillance funding cut between crises is the most "
  "expensive saving in public health."),
 "how_it_works": (
  "Preparedness runs on metrics. Doubling time — computed from case "
  "counts over time — tells responders how fast the window is "
  "closing; a 3-day doubling time demands action within days, not "
  "weeks. The case fatality ratio (deaths/cases) is tracked with "
  "awareness of its biases; serology-derived infection fatality "
  "ratios correct it. Genomic surveillance measures variant growth "
  "advantages: a variant rising from 5% to 50% of sequences in a "
  "month has a quantified transmission edge. Vaccine platform "
  "readiness is measured in 'sequence-to-doses' time, rehearsed in "
  "exercises. At the facility level, preparedness means BSL "
  "capacity, diagnostic surge reagents, and staffed contact-tracing "
  "workforces that can scale tenfold. Internationally, it means "
  "sequence-sharing agreements honored in real time — because a "
  "variant sequenced anywhere is a threat assessed everywhere."),
 "key_points": [
  "Surveillance foundation: global sequence sharing (GISAID/INSDC), animal sampling, wastewater monitoring.",
  "mRNA/vector platforms proved 'sequence-to-vaccine in under a year' in 2020 — pre-built platforms beat fresh starts.",
  "Doubling time sets the response tempo; variant growth advantage is measured from sequence proportions.",
  "Non-pharmaceutical interventions buy the time countermeasures need.",
  "Preparedness is a maintained capability — surveillance cut between crises is the most expensive saving."],
 "requirements": [
  "Viral epidemiology and emerging viruses records.",
  "Basic algebra for the doubling-time demo."],
 "standards": ["WHO preparedness terminology", "SI units throughout"],
 "citations": [CIT_WHO, CIT_CDC],
 "demo_kind": "surveillance_metrics",
 "sig_lens": (
  "The Signature reading treats pandemic preparedness as systems "
  "engineering for rare catastrophes: sensors always on, platforms "
  "pre-built, response rehearsed, metrics honest. Signature virology "
  "closes the ladder here because the whole subject — structure to "
  "surveillance — exists so the next virus meets a prepared system, "
  "not a surprised one."),
},
]
